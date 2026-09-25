"""Decorate every commonplace-* command's main with checks_library.

Mechanical edit across the command modules, so it is a migration rather than
24 staged copies. `commonplace-init` is skipped: it is the repair.
"""

import re
import subprocess
import tomllib
from pathlib import Path

ROOT = globals().get("ROOT") or Path.cwd()
IMPORT = "from commonplace.lib.library import checks_library\n"

decorated = []
scripts = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["scripts"]
for name, target in scripts.items():
    if name == "commonplace-init":
        continue
    module, _, function = target.partition(":")
    path = ROOT / "src" / Path(*module.split(".")).with_suffix(".py")
    text = path.read_text(encoding="utf-8")
    if "@checks_library" in text:
        continue
    text, count = re.subn(rf"^def {function}\(", f"@checks_library\ndef {function}(", text, count=1, flags=re.M)
    if count != 1:
        raise SystemExit(f"{path}: no top-level def {function}(")
    future = "from __future__ import annotations\n"
    if future in text:
        text = text.replace(future, future + "\n" + IMPORT, 1)
    else:
        first = re.search(r"^(import |from )", text, flags=re.M)
        text = text[: first.start()] + IMPORT + text[first.start():]
    path.write_text(text, encoding="utf-8")
    decorated.append(str(path))
    print(f"decorated {path.relative_to(ROOT)}")

# Place the new import where the project's import ordering puts it.
if decorated:
    subprocess.run(["uv", "run", "--quiet", "ruff", "check", "--select", "I", "--fix", *decorated], cwd=ROOT, check=True)
