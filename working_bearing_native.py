"""Explicit bridge to the retained native-bearing author, never the scaffold plate."""
import os
from pathlib import Path
import subprocess
from bearing_io import ROOT


def main(**kwargs):
    helper = Path(kwargs.get("native_helper", os.environ.get("OOMP_BEARING_NATIVE_HELPER", r"C:\od\OneDrive\docs\software_cad_mcp_helper")))
    executable = helper / ".venv/Scripts/python.exe"
    script = helper / "action_build_bearing_catalogue.py"
    if not executable.is_file() or not script.is_file():
        raise FileNotFoundError("Native bearing generation requires OOMP_BEARING_NATIVE_HELPER; see README_GENERATOR.md. Mesh and render generation is independent.")
    command = [str(executable), str(script), "--root", str(Path(kwargs.get("root", ROOT)).resolve()), "--build"]
    pattern = kwargs.get("filter", "") or kwargs.get("solidcraft_context", {}).get("part_filter", "")
    if pattern:
        command += ["--filter", pattern]
    subprocess.run(command, cwd=helper, check=True)
    # The external author can emit disposable STL alongside its native CAD.
    from working_bearing_storage import remove_stl
    remove_stl(root=kwargs.get("root", ROOT))
