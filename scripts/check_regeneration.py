"""Check byte-for-byte repeatability of a complete, filtered bearing pipeline."""
import hashlib
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def snapshot(**kwargs):
    folder = Path(kwargs["folder"])
    return {path.relative_to(folder).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in folder.rglob("*") if path.is_file() and "solidcraft" not in path.parts}


def main(**kwargs):
    identifier = "hardware_bearing_600_series_608_size_8_mm_id_22_mm_od_7_mm_depth"
    command = [sys.executable, "action_make_all.py", "--filter", "_608_size_", "--model-jobs", "1"]
    subprocess.run(command, cwd=ROOT, check=True)
    before = snapshot(folder=ROOT / "parts" / identifier)
    source = (ROOT / "parts_source" / identifier / "working.yaml").read_bytes()
    subprocess.run(command, cwd=ROOT, check=True)
    after = snapshot(folder=ROOT / "parts" / identifier)
    changed = sorted(key for key in set(before) | set(after) if before.get(key) != after.get(key))
    if source != (ROOT / "parts_source" / identifier / "working.yaml").read_bytes():
        changed.append("parts_source/working.yaml")
    if changed:
        raise RuntimeError(f"Regeneration changed files: {changed}")
    print(f"Repeatability passed: {len(after)} part files and source YAML unchanged")


if __name__ == "__main__":
    main()
