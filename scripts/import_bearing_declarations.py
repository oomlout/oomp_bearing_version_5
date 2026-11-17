"""One-time conversion of reviewed legacy facts to editable Python declarations."""
import json
import hashlib
import importlib.util
from pathlib import Path
import pprint
import yaml


def missing_identity(**kwargs):
    """Resolve the one absent materialized identity with the existing OOMP rules."""
    identifier = kwargs["identifier"]
    helper = Path(kwargs.get("identity_helper", r"C:\gh\oomlout_oomp_version_5\oomp_bip39.py"))
    spec = importlib.util.spec_from_file_location("legacy_oomp_bip39", helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    digest = hashlib.md5(identifier.encode()).hexdigest()
    data = {}
    data["md5"] = digest
    for count in [5, 6, 10]:
        data[f"md5_{count}"] = digest[:count]
        data[f"md5_{count}_upper"] = digest[:count].upper()
    number = int(digest[:6], 16)
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    while number:
        number, remainder = divmod(number, 36)
        encoded = alphabet[remainder] + encoded
    data["md5_6_alpha"] = encoded or "0"
    data["md5_6_alpha_upper"] = data["md5_6_alpha"].upper()
    data.update(module.get_bip39_variants(md5_value=digest))
    return data


def assignments(**kwargs):
    target = kwargs["target"]
    value = kwargs["value"]
    if isinstance(value, dict):
        lines = [f"    {target} = {{}}"]
        for key, item in value.items():
            lines.extend(assignments(target=f"{target}[{key!r}]", value=item))
        return lines
    formatted = pprint.pformat(value, sort_dicts=False, width=88, compact=False)
    return [f"    {target} = " + formatted.replace("\n", "\n    ")]


def main(**kwargs):
    root = Path(kwargs.get("root", Path(__file__).resolve().parents[1]))
    legacy = Path(kwargs.get("legacy", r"C:\od\OneDrive\docs\oomp_bearing"))
    plan = json.loads((legacy / "solidcraft_plan.json").read_text(encoding="utf-8"))
    lines = ['"""Editable bearing declarations, imported from the reviewed October 2026 catalogue.',
             '', 'Edit these explicit dictionaries, then run action_make_all.py.',
             'Dimensions and illustrative internal geometry are deliberately separate.',
             'The original source evidence is retained under source_file/solidcraft/.',
             '"""', '', 'import copy', '', '', 'def declarations(**kwargs):', '    options = []', '']
    for entry in plan["entries"]:
        source_name = next(n for n in entry["input_hashes"] if n.startswith("parts_source"))
        source = yaml.safe_load((legacy / source_name).read_text(encoding="utf-8"))
        part = {}
        part["oomp_id"] = entry["id"]
        part["legacy_source_id"] = Path(source_name).parent.name
        part["size"] = entry["size"]
        part["series"] = entry["series"]
        part["family"] = entry["spec"]["family"]
        part["dimensions"] = entry["dimensions_mm"]
        for name in ("flange_diameter", "flange_thickness", "contact_angle_deg"):
            if name in entry["spec"]["parameters"]:
                part["dimensions"][name] = entry["spec"]["parameters"][name]
        part["dimension_authority"] = entry["dimension_authority"]
        part["sources"] = [s.replace("\\", "/") for s in entry["sources"]]
        part["source_checked"] = "2026-10-27"
        part["internal_geometry"] = entry["spec"]
        part["model_note"] = entry["limitation"] + " The mesh shows open races and balls; retainers, seals and exact contact surfaces are omitted."
        part["catalogue_metadata"] = {}
        for key, value in source.items():
            if key not in {"svg_details", "id", "od", "width", "depth", "series", "size"} and not key.startswith("taxonomy_"):
                part["catalogue_metadata"][key] = value
        if not (legacy / "parts" / entry["id"] / "working.yaml").exists():
            part["catalogue_metadata"].update(missing_identity(identifier=entry["id"]))
        lines.append(f'    # {part["size"]}: {part["family"].replace("_", " ")}')
        lines.append('    option = {}')
        for key, value in part.items():
            lines.extend(assignments(target=f"option[{key!r}]", value=value))
        lines.extend(['    options.append(copy.deepcopy(option))', ''])
    lines.extend(['    return options', ''])
    (root / "working_oomp_declarations_bearing.py").write_text('\n'.join(lines), encoding="utf-8")
    print(f"Imported {len(plan['entries'])} editable declarations")


if __name__ == "__main__":
    main()
