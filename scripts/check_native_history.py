"""Verify migrated native files against their historical manifests without CAD."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT)).resolve()
    results = []
    failures = []
    for pointer in sorted(root.glob("parts/*/solidcraft/latest_success.json")):
        part_id = pointer.parents[1].name
        try:
            data = json.loads(pointer.read_text(encoding="utf-8"))
            manifest_path = (pointer.parent / data["manifest"]).resolve()
            if not manifest_path.is_relative_to(pointer.parent.resolve()):
                raise ValueError("Native manifest escapes part history")
            if hashlib.sha256(manifest_path.read_bytes()).hexdigest() != data["manifest_sha256"]:
                raise ValueError("Native manifest hash mismatch")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            native_files = []
            omitted_stl = []
            for name, expected in manifest["artifacts"].items():
                path = (manifest_path.parent / name).resolve()
                if not path.is_relative_to(manifest_path.parent):
                    raise ValueError("Native artifact escapes generation")
                if path.suffix.lower() == ".stl":
                    omitted_stl.append(name)
                    continue
                if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                    raise ValueError(f"Native artifact hash mismatch: {name}")
                if path.suffix == ".solidcraft":
                    native_files.append(path.relative_to(root).as_posix())
            if not native_files:
                raise ValueError("Native generation contains no SolidCraft file")
            results.append({"id": part_id, "native_files": native_files, "intentionally_omitted_stl": omitted_stl, "status": "passed"})
        except Exception as error:
            failures.append({"id": part_id, "error": str(error)})
    report = {}
    report["scope"] = "Historical manifests and retained non-STL artifacts only. STL exports were intentionally removed; CAD was not reopened or regenerated."
    report["passed"] = len(results)
    report["failures"] = failures
    report["results"] = results
    (root / "native_history_validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "results"}, indent=2))
    if failures or len(results) != 339:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
