"""Bump the probe package to a new major version for the upgrade test.

Usage: python3 tools/bump.py 2   (run from the probe-package directory, in your working copy)

Rewrites the version in pyproject.toml, __init__.py, and plugin.json, and every
library token suffix -V<old> to -V<new>, so a session can tell which version it read.
"""

import re
import sys
from pathlib import Path

new = int(sys.argv[1])
root = Path(__file__).resolve().parent.parent
pkg = root / "src" / "cp_delivery_probe"
for path in [root / "pyproject.toml", pkg / "__init__.py", pkg / "plugin" / ".claude-plugin" / "plugin.json"]:
    text = re.sub(r'"\d+\.0\.0"', f'"{new}.0.0"', path.read_text(), count=1)
    path.write_text(text)
for path in (pkg / "plugin" / "library").rglob("*.md"):
    path.write_text(re.sub(r"-V\d+`", f"-V{new}`", path.read_text()))
print(f"bumped to {new}.0.0")
