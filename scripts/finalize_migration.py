"""Archive superseded source aliases and retain exact original metadata snapshots."""
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from working_oomp_declarations_bearing import declarations


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT)).resolve()
    source = Path(kwargs.get("source", r"C:\od\OneDrive\docs\oomp_bearing"))
    aliases = []
    canonical = {part["oomp_id"].lower() for part in declarations()}
    for store in ["parts_source", "parts"]:
        for path in (source / store).glob("*/working.yaml"):
            target = root / "migration/legacy_metadata" / path.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    for folder in (root / "parts_source").iterdir():
        if folder.is_dir() and folder.name.lower() not in canonical:
            target = root / "migration/legacy_source_aliases" / folder.name
            if not folder.resolve().is_relative_to(root / "parts_source") or not target.resolve().is_relative_to(root / "migration"):
                raise ValueError("Migration archive path escapes workspace")
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise ValueError(f"Alias archive already exists: {target}")
            shutil.move(str(folder), str(target))
            aliases.append(folder.name)
    (root / "migration/source_aliases.json").write_text(json.dumps(aliases, indent=2) + "\n", encoding="utf-8")
    print(f"Archived {len(aliases)} obsolete source aliases; retained original metadata")


if __name__ == "__main__":
    main()
