"""Link the new router skill into the source checkout's runtime skill directories.

The source checkout keeps committed relative symlinks from `.claude/skills/` and
`.agents/skills/` into `kb/instructions/` (operator decision, 2026-09-25); the new
`cp-skill-library` skill needs the same links. Skipped outside the source checkout.
"""

import os
from pathlib import Path

ROOT = globals().get("ROOT") or Path.cwd()
SKILL = "cp-skill-library"

if (ROOT / "src" / "commonplace").is_dir() and (ROOT / "kb" / "instructions" / SKILL).is_dir():
    for skills_dir in (".claude/skills", ".agents/skills"):
        link = ROOT / skills_dir / SKILL
        if link.is_symlink() or link.exists():
            continue
        link.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(f"../../kb/instructions/{SKILL}", link, target_is_directory=True)
        print(f"linked {skills_dir}/{SKILL}")
