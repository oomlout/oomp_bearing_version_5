"""Audit every active bearing's metadata, drawings, topology, units, renders and links."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import fitz
import numpy as np
from PIL import Image, ImageStat
import trimesh
import yaml

from bearing_io import ROOT, records, write_json


def check_links(**kwargs):
    path = kwargs["path"]
    text = path.read_text(encoding="utf-8")
    if '<!-- bearing-catalogue:start -->' in text:
        text = text.split('<!-- bearing-catalogue:start -->', 1)[1].split('<!-- bearing-catalogue:end -->', 1)[0]
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)]+)\)', text):
        target = target.split(' "', 1)[0]
        url = urlsplit(target)
        if url.scheme or target.startswith('#'):
            continue
        destination = (path.parent / unquote(url.path)).resolve()
        if not destination.exists():
            raise ValueError(f"Broken link in {path}: {target}")


def validate_part(**kwargs):
    path, part = kwargs["path"], kwargs["part"]
    root = Path(kwargs.get("root", ROOT))
    folder = path.parent
    if folder.name != part["oomp_id"]:
        raise ValueError("Part folder spelling differs from its preserved OOMP ID")
    source = yaml.load((root / "parts_source" / folder.name / "working.yaml").read_text(encoding="utf-8"), Loader=yaml.CSafeLoader)
    for key in ["dimensions_mm", "svg_details", "three_d_model_details", "oobb_details", "label_details", "readme_details"]:
        if source[key] != part[key]:
            raise ValueError(f"Population/materialization mismatch: {key}")
    recipe = part["three_d_model_details"]
    output = folder / "three_d_model"
    saved = json.loads((output / "parameters.json").read_text(encoding="utf-8"))
    if saved != recipe:
        raise ValueError("Rendered recipe differs from populated recipe")
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    for name, item in manifest["artifacts"].items():
        file = output / name
        if file.stat().st_size != item["bytes"] or hashlib.sha256(file.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError(f"Changed or incomplete artifact: {name}")
    d = part["dimensions_mm"]
    diameter = d.get("flange_diameter", d["outside"])
    for variant in ["full", "display"]:
        glb = trimesh.load(output / f"model_{variant}.glb", force="scene")
        mesh = glb.to_mesh()
        mesh.merge_vertices()
        mesh.apply_transform(np.array([[1000, 0, 0, 0], [0, 0, -1000, 0], [0, 1000, 0, 0], [0, 0, 0, 1]]))
        if not mesh.is_watertight or not mesh.is_winding_consistent or mesh.volume <= 0:
            raise ValueError(f"Invalid {variant} mesh")
        if mesh.body_count != 2 + recipe["parameters"]["ball_count"]:
            raise ValueError("Missing race or ball")
        if not np.allclose(mesh.extents, [diameter, diameter, d["width"]], atol=3e-5):
            raise ValueError("Mesh envelope differs from declared dimensions")
        radial = np.linalg.norm(mesh.vertices[:, :2], axis=1)
        if not np.isclose(radial.min(), d["bore"] / 2, atol=3e-5):
            raise ValueError("Mesh bore differs from declaration")
        if not np.allclose(glb.extents, mesh.extents[[0, 2, 1]] * .001, atol=3e-8):
            raise ValueError("GLB units or axis convention differ")
        for view in recipe["views"]:
            ET.parse(output / variant / (view + ".svg"))
    for render in recipe["renders"].values():
        with Image.open(output / render["file"]) as image:
            if image.size != (render["pixels"], render["pixels"]):
                raise ValueError("Render resolution mismatch")
            if max(ImageStat.Stat(image.convert("RGB")).stddev) < 12:
                raise ValueError("Render appears blank")
    for name, dimensions in [("working_dimension_a4.pdf", [297, 210]), ("label_bearing_3x2.pdf", [76.2, 50.8]), ("label_bearing_1_5x1.pdf", [38.1, 25.4])]:
        with fitz.open(folder / name) as pdf:
            if len(pdf) != 1 or not np.allclose([pdf[0].rect.width, pdf[0].rect.height], np.array(dimensions) * 72 / 25.4, atol=.02):
                raise ValueError(f"Incorrect PDF page size: {name}")
            if part["size"] not in pdf[0].get_text():
                raise ValueError(f"Missing bearing designation: {name}")
    for name in ["working_dimension.svg", "working_svg.svg", "label_bearing_3x2.svg", "label_bearing_1_5x1.svg"]:
        ET.parse(folder / name)
    if not (folder / "3dpr.scad").is_file():
        raise ValueError("Missing editable SCAD")
    if recipe["model_formats"] != ["glb"] or any(file.suffix.lower() == ".stl" for file in folder.rglob("*")):
        raise ValueError("Bearing records must not retain STL files")
    check_links(path=folder / "README.md")
    return {"id": part["oomp_id"], "status": "passed", "family": part["family"], "models": manifest["models"]}


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT))
    report_path = root / ("build_validation_filtered.json" if kwargs.get("filter") else "build_validation.json")
    write_json(path=report_path, data={"status": "running", "filter": kwargs.get("filter", "")})
    results = []
    for path, part in records(**kwargs):
        try:
            results.append(validate_part(path=path, part=part, root=root))
        except Exception as error:
            results.append({"id": part["oomp_id"], "status": "failed", "error": str(error)})
        if len(results) % 25 == 0:
            print(f"Audited {len(results)} bearings", flush=True)
    failures = [result for result in results if result["status"] != "passed"]
    if not results:
        failures.append({"error": "No populated bearings selected for validation"})
    pages = [root / "README.md", *sorted((root / "navigation").rglob("README.md"))] if not kwargs.get("filter") else []
    for path in pages:
        try:
            check_links(path=path)
        except Exception as error:
            failures.append({"page": str(path.relative_to(root)), "error": str(error)})
    if not kwargs.get("filter"):
        with (root / "source_file/dimension/oomp_bearing_sizes.csv").open(encoding="utf-8-sig") as handle:
            source_rows = list(csv.DictReader(handle))
        expected = len(source_rows)
        source_dimensions = {(row["series"], row["size"]): [float(row[key]) for key in ["id", "od", "width"]] for row in source_rows}
        for _, part in records(root=root):
            measured = [part["dimensions_mm"][key] for key in ["bore", "outside", "width"]]
            if source_dimensions.get((part["series"], part["size"])) != measured:
                failures.append({"id": part["oomp_id"], "error": "Dimensions differ from the retained source CSV"})
        sources = list((root / "parts_source").glob("*/working.yaml"))
        if len(results) != expected or len(sources) != expected:
            failures.append({"error": f"Catalogue coverage mismatch: CSV={expected}, source={len(sources)}, parts={len(results)}"})
        if {path.parent.name for path in sources} != {result["id"] for result in results}:
            failures.append({"error": "Source and materialized folder spellings differ"})
    report = {}
    report["status"] = "failed" if failures else "passed"
    report["filter"] = kwargs.get("filter", "")
    report["parts"] = len(results)
    report["passed"] = sum(result["status"] == "passed" for result in results)
    report["failures"] = failures
    report["checks"] = ["source/part recipe equality", "recipe/artifact equality", "artifact hashes", "GLB topology, bore and envelope", "GLB metre/Y-up dimensions", "seven SVG views per quality", "four nonblank renders at declared resolution", "A4 and label PDF sizes/text", "SCAD availability and no retained STL", "generated Markdown links", "full catalogue CSV dimensions and exact folder spellings"]
    report["results"] = results
    write_json(path=report_path, data=report)
    print(json.dumps({key: value for key, value in report.items() if key != "results"}, indent=2), flush=True)
    if failures:
        raise SystemExit(1)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="")
    main(**vars(parser.parse_args()))
