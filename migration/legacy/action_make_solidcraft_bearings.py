"""Explicit bearing-only launcher; defaults to planning, never legacy actions."""
from pathlib import Path
import subprocess
import sys

HELPER = Path(r'C:\od\OneDrive\docs\software_cad_mcp_helper')

if __name__ == '__main__':
    raise SystemExit(subprocess.call([str(HELPER/'.venv/Scripts/python.exe'),
        str(HELPER/'action_build_bearing_catalogue.py'), '--root', str(Path(__file__).resolve().parent), *sys.argv[1:]], cwd=HELPER))
