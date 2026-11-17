"""Preserve the original bearing catalogue without modifying the OneDrive copy."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import filecmp


def main(**kwargs):
    source = Path(kwargs.get("source", r"C:\od\OneDrive\docs\oomp_bearing"))
    root = Path(kwargs.get("root", Path(__file__).resolve().parents[1]))
    records = []
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if not path.is_file() or any(p in {"__pycache__", ".pytest_cache", ".git"} for p in relative.parts) or path.suffix.lower() in {".tmp", ".stl"}:
            continue
        if relative.parts[0] in {"parts", "parts_source", "solidcraft_library", "source_file"}:
            destination = root / relative
        else:
            destination = root / "migration/legacy" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        method = "copy"
        immutable = path.suffix.lower() in {".solidcraft", ".stl"} and (relative.parts[0] == "solidcraft_library" or "solidcraft" in relative.parts) and path.stat().st_size > 1_000_000
        if immutable and destination.exists():
            if not destination.resolve().is_relative_to(root.resolve()):
                raise ValueError(f"Destination escapes migration root: {destination}")
            if not os.path.samefile(path, destination):
                temporary = destination.with_name(destination.name + ".migration-link")
                os.link(path, temporary)
                os.replace(temporary, destination)
            method = "hardlink_immutable_native"
        if destination.exists():
            if method == "hardlink_immutable_native":
                pass
            elif filecmp.cmp(destination, path, shallow=False):
                method = "existing"
            else:
                destination = root / "migration/legacy" / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
        if method not in {"existing", "hardlink_immutable_native"}:
            # These historical native binaries are never edited by the new pipeline.
            if immutable:
                os.link(path, destination)
                method = "hardlink_immutable_native"
            else:
                shutil.copy2(path, destination)
        if destination.stat().st_size != path.stat().st_size:
            raise RuntimeError(f"Migration size mismatch: {relative}")
        record = {}
        record["source"] = relative.as_posix()
        record["destination"] = destination.relative_to(root).as_posix()
        record["bytes"] = path.stat().st_size
        record["method"] = method
        records.append(record)
    manifest = {}
    manifest["source"] = str(source)
    manifest["destination"] = str(root)
    manifest["source_retained"] = True
    manifest["native_history_policy"] = "Large historical .solidcraft and .stl files are immutable hard links on this workstation. Copy to a new filename before editing; Git clones contain independent files."
    manifest["files"] = records
    (root / "migration/manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Preserved {len(records)} files, {sum(r['bytes'] for r in records):,} logical bytes", flush=True)


if __name__ == "__main__":
    main()
