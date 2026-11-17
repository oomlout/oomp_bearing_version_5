"""Remove disposable STL exports from this catalogue, preserving linked originals."""
from pathlib import Path
from bearing_io import ROOT


def remove_stl(**kwargs):
    root = Path(kwargs.get("root", ROOT)).resolve()
    removed = []
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() != ".stl" or not path.is_file():
            continue
        relative = path.relative_to(root)
        if ".git" in relative.parts:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"STL path escapes catalogue: {path}")
        item = {}
        item["path"] = relative.as_posix()
        item["logical_bytes"] = path.stat().st_size
        # Unlink only this directory entry; historical hard-linked originals stay.
        path.unlink()
        removed.append(item)
    return removed
