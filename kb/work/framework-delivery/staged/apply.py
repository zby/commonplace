"""Apply the framework-delivery stage to a repository tree.

Usage:
  python3 apply.py <repo root>            apply: copy files, delete paths, run migrations
  python3 apply.py <repo root> --check    report what would change and any base mismatches
  python3 apply.py --record <path>...     record the current live content of staged paths as their base

A staged file replaces its live counterpart completely, so apply refuses to
overwrite a file whose live content differs from the base recorded when it was
staged: that live file changed after staging and the staged copy must be rebased.
A file that tools would read as live configuration (pyproject.toml) is stored
with a `.staged` suffix, which apply strips.
"""

from __future__ import annotations

import hashlib
import json
import runpy
import shutil
import sys
from pathlib import Path

STAGE = Path(__file__).resolve().parent
FILES = STAGE / "files"
BASES = STAGE / "bases.json"
DELETE = STAGE / "delete.txt"
MIGRATIONS = STAGE / "migrations"
CHECKOUT = STAGE.parents[3]  # staged -> framework-delivery -> work -> kb -> repo


def _sha(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def _bases() -> dict[str, str | None]:
    return json.loads(BASES.read_text(encoding="utf-8")) if BASES.is_file() else {}


SUFFIX = ".staged"  # stored name suffix for files that tools would treat as live config (pyproject.toml)
IGNORED_PARTS = {".ruff_cache", "__pycache__", ".pytest_cache"}


def _target(stored: Path) -> str:
    """Repository path for a stored staged file: its path under files/, minus the .staged suffix."""
    rel = stored.relative_to(FILES).as_posix()
    return rel[: -len(SUFFIX)] if rel.endswith(SUFFIX) else rel


def _stored() -> dict[str, Path]:
    return {
        _target(p): p
        for p in sorted(FILES.rglob("*"))
        if p.is_file() and not IGNORED_PARTS & set(p.relative_to(FILES).parts)
    }


def _staged() -> list[str]:
    return sorted(_stored())


def _deletions() -> list[str]:
    if not DELETE.is_file():
        return []
    lines = DELETE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def record(paths: list[str]) -> None:
    """Record the checkout's current content of each path as the base for its staged copy."""
    bases = _bases()
    for rel in paths:
        bases[rel] = _sha(CHECKOUT / rel)
        print(f"base {rel}: {bases[rel] or 'new file'}")
    BASES.write_text(json.dumps(bases, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def apply(root: Path, check: bool) -> None:
    bases = _bases()
    unrecorded = [rel for rel in _staged() if rel not in bases]
    mismatched = [rel for rel in _staged() if rel in bases and _sha(root / rel) != bases[rel]]
    for rel in unrecorded:
        print(f"no base recorded: {rel}", file=sys.stderr)
    for rel in mismatched:
        print(f"live file changed since staging: {rel}", file=sys.stderr)
    if check:
        for rel in _staged():
            print(f"{'new' if bases.get(rel) is None else 'replace'} {rel}")
        for rel in _deletions():
            print(f"delete {rel}")
        for script in sorted(MIGRATIONS.glob("*.py")):
            print(f"migrate {script.name}")
    if unrecorded or mismatched:
        sys.exit(1)
    if check:
        return
    for rel, stored in _stored().items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(stored, target)
    for rel in _deletions():
        target = root / rel
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists() or target.is_symlink():
            target.unlink()
    for script in sorted(MIGRATIONS.glob("*.py")):
        print(f"running {script.name}")
        runpy.run_path(str(script), init_globals={"ROOT": root}, run_name="__main__")
    print(f"applied {len(_staged())} files, {len(_deletions())} deletions; now make the changes in CHANGES.md")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--record"]:
        record(args[1:])
    elif args:
        apply(Path(args[0]).resolve(), check="--check" in args[1:])
    else:
        sys.exit(__doc__)
