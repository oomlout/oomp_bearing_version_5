"""Small deterministic file helpers shared by the bearing build stages."""
import fnmatch
import json
from pathlib import Path
import os
import tempfile
import yaml

ROOT = Path(__file__).resolve().parent


def write_text(**kwargs):
    path = Path(kwargs["path"])
    text = kwargs["text"]
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def write_yaml(**kwargs):
    write_text(path=kwargs["path"], text=yaml.dump(kwargs["data"], Dumper=getattr(yaml, "CSafeDumper", yaml.SafeDumper), sort_keys=False, allow_unicode=True))


def write_json(**kwargs):
    write_text(path=kwargs["path"], text=json.dumps(kwargs["data"], indent=2) + "\n")


def records(**kwargs):
    root = Path(kwargs.get("root", ROOT))
    pattern = kwargs.get("filter", "")
    store = kwargs.get("store", "parts")
    for path in sorted((root / store).glob("*/working.yaml")):
        if pattern and pattern not in path.parent.name and not fnmatch.fnmatchcase(path.parent.name, pattern):
            continue
        part = yaml.load(path.read_text(encoding="utf-8"), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        if part.get("catalogue_schema") == "oomp_bearing_v5":
            yield path, part
