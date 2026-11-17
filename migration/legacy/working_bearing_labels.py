"""Regenerate only the two bold bearing labels and their native Jinja actions."""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
from functools import lru_cache
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

from jinja2 import Environment, StrictUndefined
import yaml

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = Path("source_file/template_jinja/label_bearing_bold")
FORMATS = {"3x2": (76.2, 50.8, 2), "1_5x1": (38.1, 25.4, 1)}
START = "# BEGIN GENERATED BEARING BOLD LABELS\n"
END = "# END GENERATED BEARING BOLD LABELS\n"
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def identifier(part):
    # In parts_source, `id` is a diameter, not the OOMP identifier.
    return "_".join(str(part[f"taxonomy_{i}"]) for i in range(1, 16) if part.get(f"taxonomy_{i}"))


@lru_cache(maxsize=1)
def wordlist():
    words = (ROOT / TEMPLATE_DIR / "bip_39_wordlist.txt").read_text(encoding="utf-8").split()
    if len(words) != 2048:
        raise ValueError("Expected the 2048-word English BIP39 list")
    return words


def bip39_name(part):
    existing = part.get("bip_39_3_word_space") or " ".join(part.get("bip_39_3_word_array", []))
    if existing:
        if len(existing.split()) != 3:
            raise ValueError(f"Expected three BIP39 words: {existing!r}")
        return " ".join(existing.split())
    digest = part.get("md5") or hashlib.md5(identifier(part).encode()).hexdigest()
    bits = f"{int(digest, 16):0128b}"
    words = wordlist()
    return " ".join(words[int(bits[i:i + 11], 2)] for i in (0, 11, 22))


def load(path):
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=LOADER) or {}


def source_path(root, part_name):
    # populate_helper normalizes decimal dots in source folder names; OOMP does not.
    path = Path(root) / "parts_source" / part_name / "working.yaml"
    normalized = Path(root) / "parts_source" / part_name.replace(".", "_") / "working.yaml"
    return normalized if not path.is_file() and normalized.is_file() else path


def merge_details(part):
    details = dict(part)
    details.update(part.get("label_source", {}))
    details.update(part.get("label_manual", {}))
    return details


def number(value, name):
    try:
        n = Decimal(str(value).replace("_", "."))
    except InvalidOperation as error:
        raise ValueError(f"Missing or invalid {name}: {value!r}") from error
    if not n.is_finite() or n <= 0:
        raise ValueError(f"Invalid {name}: {value!r}")
    return n


def validate(part):
    d = merge_details(part)
    raw_id = d.get("id_mm", d.get("inner_diameter", d.get("id", "")))
    try:
        inner = number(raw_id, "ID")
    except ValueError:
        inner = number(str(d.get("taxonomy_5", "")).removesuffix("_mm_id"), "ID")
    outer = number(d.get("od_mm", d.get("od", str(d.get("taxonomy_6", "")).removesuffix("_mm_od"))), "OD")
    number(d.get("width_mm", d.get("width", d.get("depth", str(d.get("taxonomy_7", "")).removesuffix("_mm_depth")))), "width")
    if inner >= outer:
        raise ValueError(f"ID {inner} must be smaller than OD {outer}")
    if not (d.get("size") or d.get("taxonomy_4")):
        raise ValueError("Missing bearing designation")
    if not (d.get("family") or d.get("series") or d.get("taxonomy_3")):
        raise ValueError("Missing bearing family/series")


def add_actions(part, count=0, root=ROOT, part_name=None):
    root = Path(root).resolve()
    part_name = part_name or identifier(part).lower()
    directory = root / "parts" / part_name
    if not directory.resolve().is_relative_to(root / "parts"):
        raise ValueError("Part path escapes parts directory")
    for size in FORMATS:
        output = f"label_bearing_bold_{size}.svg"
        key = next((k for k, v in part.items() if k.startswith("oomlout_ai_roboclick_")
                    and isinstance(v, dict) and any(a.get("file_output") == output
                    for a in v.get("actions", []))), None)
        if key is None:
            index = 1
            while f"oomlout_ai_roboclick_{index}" in part:
                index += 1
            key = f"oomlout_ai_roboclick_{index}"
        part[key] = {"file_test": "", "actions": [{
            "command": "text_jinja_template", "description": f"Bold bearing label {size}",
            "file_template": str(root / TEMPLATE_DIR / f"{size}.svg.j2"),
            "file_output": output,
            # Native roboclick reads these YAML files afresh at render time.
            "dict_data_yaml_files": {
                "label_source": str(source_path(root, part_name)),
                "label_manual": str(directory / "working_manual.yaml")},
            "convert_to_pdf": False, "convert_to_png": False}]}
    return count + len(FORMATS)


def render(part, size, root=ROOT):
    validate(part)
    context = dict(part)
    if not context.get("bip_39_3_word_space"):
        context["bip_39_3_word_space"] = bip39_name(part)
    template = Environment(undefined=StrictUndefined).from_string(
        (Path(root) / TEMPLATE_DIR / f"{size}.svg.j2").read_text(encoding="utf-8"))
    svg = template.render(p=context)
    ET.fromstring(svg)
    return svg


def export_pdf(svg_path):
    """Keep the editable SVG, but make its print PDF independent of fonts."""
    inkscape = shutil.which("inkscape")
    if not inkscape:
        raise RuntimeError("Inkscape must be installed and available on PATH for PDF export")
    svg_path = Path(svg_path)
    output = svg_path.with_suffix(".pdf")
    temporary = output.with_name(output.stem + ".pending.pdf")
    try:
        subprocess.run([inkscape, str(svg_path), "--export-area-page",
                        "--export-text-to-path", f"--export-filename={temporary}"],
                       check=True, capture_output=True, text=True)
        if not temporary.is_file() or temporary.stat().st_size == 0:
            raise RuntimeError(f"Inkscape did not produce a PDF for {svg_path}")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    return output


def check_pdf_font():
    # The templates' fitting uses this exact face; a wider fallback overlaps.
    if os.name == "nt":
        directories = [Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts",
                       Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Windows/Fonts"]
        if not any((directory / "arialnb.ttf").is_file() for directory in directories):
            raise RuntimeError("Install Arial Narrow Bold (ARIALNB.TTF) before generating PDFs. "
                               "Font substitution changes the label spacing. Existing outlined PDFs need no font.")


def regenerate(root=ROOT, pdf=False, bearing_codes=None):
    root = Path(root).resolve()
    parts_root = (root / "parts").resolve()
    sources = {p.parent.name: p for p in parts_root.glob("*/working.yaml")}
    sources.update({identifier(load(p)).lower(): p for p in (root / "parts_source").glob("*/working.yaml")})
    if not sources:
        raise ValueError(f"No bearings found under {root}")
    if bearing_codes:
        requested = {str(code).casefold() for code in bearing_codes}
        selected = {}
        found = set()
        for name, source in sources.items():
            details = load(source)
            code = str(details.get("size") or str(details.get("taxonomy_4", "")).removesuffix("_size")).casefold()
            if code in requested:
                selected[name] = source
                found.add(code)
        if requested - found:
            raise ValueError(f"Unknown bearing codes: {', '.join(sorted(requested - found))}")
        sources = selected
    if pdf and not shutil.which("inkscape"):
        raise RuntimeError("Inkscape must be installed and available on PATH for PDF export")
    if pdf:
        check_pdf_font()
    count = deleted = 0
    for name, source in sorted(sources.items()):
        directory = parts_root / name
        if not directory.resolve().is_relative_to(parts_root):
            raise ValueError(f"Part path escapes parts directory: {directory}")
        current = load(source)
        path = directory / "working.yaml"
        original = path.read_text(encoding="utf-8") if path.exists() else yaml.safe_dump(current, sort_keys=False)
        base = re.sub(re.escape(START) + r".*?" + re.escape(END), "", original, flags=re.S)
        metadata = yaml.load(base, Loader=LOADER) or {}
        before = set(metadata)
        if not metadata.get("bip_39_3_word_space"):
            metadata["bip_39_3_word_space"] = bip39_name(current)
        previous_blocks = {k for k,v in metadata.items() if k.startswith("oomlout_ai_roboclick_")
                           and any(a.get("file_output", "").startswith("label_bearing_bold_") for a in v.get("actions", []))}
        add_actions(metadata, root=root, part_name=name)
        context = dict(metadata, label_source=current)
        manual = directory / "working_manual.yaml"
        if manual.is_file():
            context["label_manual"] = load(manual)
        outputs = {size: render(context, size, root) for size in FORMATS}
        if previous_blocks:
            # Updating blocks created by the standard OOMP pipeline.
            saved = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
        else:
            block = {k: v for k, v in metadata.items() if k not in before}
            saved = base.rstrip() + "\n" + START + yaml.safe_dump(block, allow_unicode=True, sort_keys=False) + END
        directory.mkdir(parents=True, exist_ok=True)
        for size, svg in outputs.items():
            svg_path = directory / f"label_bearing_bold_{size}.svg"
            svg_path.write_text(svg, encoding="utf-8")
            if pdf:
                export_pdf(svg_path)
            count += 1
        path.write_text(saved, encoding="utf-8")
        for png in directory.rglob("label_bearing_bold*.png"):
            if not png.is_symlink() and png.resolve().is_relative_to(directory.resolve()):
                png.unlink()
                deleted += 1
    print(f"Generated {count} bold bearing labels for {len(sources)} bearings; deleted {deleted} stale label PNG renders.")
    if pdf:
        print(f"Exported {count} PDFs with lettering converted to vector outlines.")
    return count, deleted


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--pdf", action="store_true", help="Also export outlined PDFs through Inkscape")
    parser.add_argument("--bearing", action="append", help="Limit to this bearing code; repeat for more codes")
    args = parser.parse_args()
    regenerate(args.root, pdf=args.pdf, bearing_codes=args.bearing)
