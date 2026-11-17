"""Materialize current records, keeping legacy short names and specialist metadata."""
from pathlib import Path
import yaml
from bearing_io import ROOT, records, write_yaml


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT))
    options = dict(kwargs)
    options["store"] = "parts_source"
    count = 0
    for path, source in records(**options):
        destination = root / "parts" / source["oomp_id"] / "working.yaml"
        part = yaml.load(destination.read_text(encoding="utf-8"), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)) if destination.exists() else {}
        part.update(source)
        # Legacy directories can contain robot actions with machine-specific paths.
        # Preserve them as evidence; this deterministic pipeline never executes them.
        write_yaml(path=destination, data=part)
        count += 1
    print(f"Materialized {count} bearing records", flush=True)
    return count
