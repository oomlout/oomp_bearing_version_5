"""One-time removal of STL exports while retaining verified GLB/render caches."""
import copy
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main(**kwargs):
    from bearing_io import records, write_json
    import mechanical_model_render
    import working_oomp_populate
    import working_bearing_records
    from working_three_d_model import fingerprint
    from working_bearing_storage import remove_stl

    mechanical_model_render.renderer_identity = lru_cache(maxsize=1)(mechanical_model_render.renderer_identity)
    working_oomp_populate.main()
    working_bearing_records.main()
    updated = []
    for path, part in records():
        output = path.parent / "three_d_model"
        saved = json.loads((output / "parameters.json").read_text(encoding="utf-8"))
        recipe = part["three_d_model_details"]
        normalized = copy.deepcopy(saved)
        normalized["model_formats"] = ["glb"]
        if normalized != recipe:
            raise ValueError(f"Geometry or presentation changed: {part['oomp_id']}")
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        retained = {}
        for name, item in manifest["artifacts"].items():
            if Path(name).suffix.lower() == ".stl":
                continue
            artifact = output / name
            if hashlib.sha256(artifact.read_bytes()).hexdigest() != item["sha256"]:
                raise ValueError(f"Changed retained artifact: {artifact}")
            retained[name] = item
        write_json(path=output / "parameters.json", data=recipe)
        parameters = output / "parameters.json"
        retained["parameters.json"] = {"bytes": parameters.stat().st_size, "sha256": hashlib.sha256(parameters.read_bytes()).hexdigest()}
        manifest["artifacts"] = retained
        manifest["fingerprint"] = fingerprint(recipe=recipe)
        write_json(path=output / "manifest.json", data=manifest)
        updated.append(part["oomp_id"])
    removed = remove_stl()
    report = {}
    report["date"] = "2026-11-17"
    report["policy"] = "GLB-only exports; STL working files and Git history retired. Original OneDrive source untouched."
    report["verified_retained_model_sets"] = len(updated)
    report["removed_files"] = len(removed)
    report["removed_logical_bytes"] = sum(item["logical_bytes"] for item in removed)
    report["note"] = "Logical size is not physical space reclaimed: many legacy files were hard links. Retained GLB, view and render bytes were verified unchanged."
    report["files"] = removed
    write_json(path=ROOT / "migration/stl_retirement.json", data=report)
    print(f"Retained {len(updated)} verified model sets; removed {len(removed)} STL files", flush=True)


if __name__ == "__main__":
    main()
