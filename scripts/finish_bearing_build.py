"""Wait for the current full model batch, then publish pages and audit all assets."""
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main(**kwargs):
    from working_oomp_declarations_bearing import declarations
    expected = len(declarations())
    last_count = -1
    while True:
        complete = len(list((ROOT / "parts").glob("*/three_d_model/manifest.json")))
        if complete != last_count:
            print(f"Complete model sets: {complete}/{expected}", flush=True)
            last_count = complete
        try:
            report = json.loads((ROOT / "three_d_model_build.json").read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError):
            report = {}
        counts = report.get("counts", {})
        if report.get("filter") == "" and sum(counts.values()) == expected:
            if counts.get("failed"):
                raise RuntimeError(f"Model batch reported failures: {report['failures']}")
            break
        time.sleep(10)
    print("Model batch complete; regenerating documentation", flush=True)
    import working_bearing_documentation
    working_bearing_documentation.main()
    print("Auditing every bearing and generated link", flush=True)
    import working_validate_bearings
    working_validate_bearings.main()


if __name__ == "__main__":
    main()
