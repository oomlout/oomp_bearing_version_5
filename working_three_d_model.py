"""Build both mesh qualities, seven vector views and four Blender studio renders."""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import tempfile

from bearing_io import ROOT, records, write_json, write_text


def fingerprint(**kwargs):
    digest = hashlib.sha256(json.dumps(kwargs["recipe"], sort_keys=True).encode())
    for name in ["working_three_d_model.py", "bearing_model_geometry.py", "mechanical_model_render.py", "mechanical_model_blender.py", "mechanical_model_pose.py", "mechanical_model_views.py", "requirements-three-d-model.txt"]:
        digest.update((ROOT / name).read_bytes())
    from mechanical_model_render import renderer_identity
    digest.update(json.dumps(renderer_identity(), sort_keys=True).encode())
    return digest.hexdigest()


def cached(**kwargs):
    output = Path(kwargs["output"])
    try:
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        return manifest["fingerprint"] == kwargs["fingerprint"] and bool(manifest["artifacts"]) and all(
            (output / name).is_file() and hashlib.sha256((output / name).read_bytes()).hexdigest() == item["sha256"]
            for name, item in manifest["artifacts"].items()
        )
    except (OSError, ValueError, KeyError):
        return False


def generate_assets(**kwargs):
    import numpy as np
    import trimesh
    from bearing_model_geometry import build_model, export_mesh, write_scad
    from mechanical_model_views import export_views
    from mechanical_model_render import render_studio

    part = kwargs["part"]
    recipe = part["three_d_model_details"]
    if recipe["model_formats"] != ["glb"]:
        raise ValueError("Repopulate bearing recipes before building: only GLB is retained")
    folder = Path(kwargs["folder"])
    output = folder / "three_d_model"
    current = fingerprint(recipe=recipe)
    write_scad(part=part, folder=folder)
    if not kwargs.get("force", False) and cached(output=output, fingerprint=current):
        return "cached"
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".build-", dir=output) as temporary:
        stage = Path(temporary)
        write_json(path=stage / "parameters.json", data=recipe)
        write_text(path=stage / "model_notes.md", text=recipe["modelling_note"] + "\n")
        meshes = {}
        measurements = {}
        for variant in recipe["variants"]:
            mesh = build_model(recipe=recipe, variant=variant)
            meshes[variant] = mesh
            measurements[variant] = {}
            measurements[variant]["triangles"] = len(mesh.faces)
            measurements[variant]["watertight"] = bool(mesh.is_watertight)
            measurements[variant]["connected_solids"] = mesh.body_count
            measurements[variant]["volume_mm3"] = float(mesh.volume)
            measurements[variant]["bounds_mm"] = mesh.bounds.tolist()
            measurements[variant]["dimensions_mm"] = mesh.extents.tolist()
            for suffix in recipe["model_formats"]:
                export_mesh(mesh=mesh, path=stage / f"model_{variant}.{suffix}", material=recipe["material"])
            glb = trimesh.load(stage / f"model_{variant}.glb", force="scene")
            if not np.allclose(glb.extents, mesh.extents[[0, 2, 1]] * .001, atol=3e-8):
                raise ValueError("GLB metre/Y-up dimensions mismatch")
            export_views(mesh=mesh, p=recipe["parameters"], variant=variant, output=stage)
        if len(meshes["display"].faces) >= len(meshes["full"].faces) / 2:
            raise ValueError("Display model must have less than half the full triangle count")
        render_studio(meshes=meshes, p=recipe["parameters"], recipe=recipe, output=stage)
        artifacts = {}
        for path in sorted(stage.rglob("*")):
            if path.is_file():
                artifacts[path.relative_to(stage).as_posix()] = {"bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        manifest = {}
        manifest["schema_version"] = 1
        manifest["fingerprint"] = current
        manifest["models"] = measurements
        manifest["artifacts"] = artifacts
        for name in artifacts:
            destination = output / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            (stage / name).replace(destination)
        write_json(path=output / "manifest.json", data=manifest)
    return "generated"


def main(**kwargs):
    jobs = kwargs.get("model_jobs", 2)
    if type(jobs) is not int or not 1 <= jobs <= 8:
        raise ValueError("model_jobs must be an integer from 1 to 8")
    tasks = list(records(**kwargs))
    counts = {"generated": 0, "cached": 0, "failed": 0}
    failures = []
    with ProcessPoolExecutor(max_workers=jobs) as executor:
        futures = {}
        for path, part in tasks:
            future = executor.submit(generate_assets, part=part, folder=path.parent, force=kwargs.get("force", False))
            futures[future] = part["oomp_id"]
        for index, future in enumerate(as_completed(futures), 1):
            try:
                result = future.result()
                counts[result] += 1
                print(f"[{index}/{len(tasks)}] {result}: {futures[future]}", flush=True)
            except Exception as error:
                counts["failed"] += 1
                failures.append({"id": futures[future], "error": str(error)})
                print(f"[{index}/{len(tasks)}] FAILED: {futures[future]}: {error}", flush=True)
    write_json(path=Path(kwargs.get("root", ROOT)) / "three_d_model_build.json", data={"filter": kwargs.get("filter", ""), "counts": counts, "failures": failures})
    if failures:
        raise RuntimeError(f"{len(failures)} bearing model builds failed")
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="")
    parser.add_argument("--model-jobs", type=int, default=2)
    parser.add_argument("--force", action="store_true")
    main(**vars(parser.parse_args()))
