"""Use the preserved materialized ID's exact spelling on case-sensitive systems."""
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT)).resolve()
    changes = []
    for store in ["parts_source", "parts"]:
        parent = root / store
        for path in list(parent.glob("*/working.yaml")):
            part = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.CSafeLoader)
            name = part.get("oomp_id")
            original = path.parent
            if not name or original.name == name:
                continue
            if original.name.lower() != name.lower():
                raise ValueError(f"Non-case identity mismatch: {original}")
            temporary = parent / (original.name + ".case-migration")
            target = parent / name
            if not all(p.resolve().is_relative_to(parent) for p in [original, temporary, target]):
                raise ValueError("Folder casing target escapes its active store")
            original.rename(temporary)
            temporary.rename(target)
            changes.append({"store": store, "before": original.name, "after": name})
    if changes:
        (root / "migration/folder_casing.json").write_text(json.dumps(changes, indent=2) + "\n", encoding="utf-8")
    print(f"Normalized {len(changes)} folder spellings")


if __name__ == "__main__":
    main()
