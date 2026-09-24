"""Commands a harness-neutral agent uses to find the probe library.

The library is the only tree. It mirrors a KB layout: instructions (with each
skill in its own directory there) and types. A normal install places it under
``<environment>/share/cp-delivery-probe/``, a path that survives a change of the
tool's Python version. An editable install reads it from the source tree,
because shared data is copied at install time.

Harnesses discover skills only in their own skill directories, so
``install-skills`` writes a stub there for each skill. A stub carries the skill's
name and description and redirects the agent to the real SKILL.md at its
absolute path, so the real skill runs in place with ordinary relative links.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from cp_delivery_probe import __version__

SHARE_NAME = "cp-delivery-probe"
STUB_MARKER = ".cp-delivery-probe-stub"
DEFAULT_SKILL_DIRS = [".claude/skills", ".agents/skills"]


def _source_library_dir() -> Path:
    # src/cp_delivery_probe/cli.py -> the package root's library/ directory
    return Path(__file__).resolve().parents[2] / "library"


def _library_dir() -> Path:
    """The library: the source tree for an editable install, else shared data."""
    source = _source_library_dir()
    root = source if (source / "instructions").is_dir() else Path(sys.prefix) / "share" / SHARE_NAME
    if not root.is_dir():
        sys.exit(f"cp-delivery-probe {__version__}: library directory missing at {root}")
    return root.resolve()


def _skills() -> dict[str, Path]:
    """Skill name -> the real skill directory, for every instructions/<name>/SKILL.md."""
    instructions = _library_dir() / "instructions"
    return {p.parent.name: p.parent for p in sorted(instructions.glob("*/SKILL.md"))}


def _frontmatter(skill_md: Path) -> str:
    """The frontmatter block of a SKILL.md, without the --- fences."""
    lines = skill_md.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        sys.exit(f"{skill_md}: no frontmatter")
    end = lines.index("---", 1)
    return "\n".join(lines[1:end])


def _render_stub(skill: Path) -> str:
    real = skill / "SKILL.md"
    return (
        f"---\n{_frontmatter(real)}\n---\n\n"
        f"# {skill.name}\n\n"
        "This skill is installed as a stub. Read the real skill at\n\n"
        f"{real}\n\n"
        "and follow it exactly. Resolve every relative link in it against that file's "
        "directory, not this stub's.\n"
    )


def _skill_dirs() -> list[Path]:
    """Skill directories to check: the current project's defaults plus CP_DELIVERY_PROBE_SKILL_DIRS."""
    extra = os.environ.get("CP_DELIVERY_PROBE_SKILL_DIRS", "")
    names = DEFAULT_SKILL_DIRS + [d for d in extra.split(os.pathsep) if d]
    return [Path(d).expanduser() for d in names]


def _statuses(directory: Path) -> list[tuple[str, Path]]:
    """(status, entry) for each skill and each leftover stub in one skill directory.

    Status is one of: ok, stale, missing, foreign, extra.
    """
    skills = _skills()
    found = []
    for name, skill in skills.items():
        dest = directory / name
        if not dest.exists():
            found.append(("missing", dest))
        elif not (dest / STUB_MARKER).is_file():
            found.append(("foreign", dest))
        else:
            current = (dest / "SKILL.md").is_file() and (dest / "SKILL.md").read_text() == _render_stub(skill)
            found.append(("ok" if current else "stale", dest))
    if directory.is_dir():
        for dest in sorted(directory.iterdir()):
            if dest.name not in skills and (dest / STUB_MARKER).is_file():
                found.append(("extra", dest))
    return found


def _warn_on_problems() -> None:
    problems = [
        f"{dest}: {status}"
        for directory in _skill_dirs()
        if directory.is_dir()
        for status, dest in _statuses(directory)
        if status in ("stale", "extra")
    ]
    if problems:
        print(
            "warning: delivery-probe skill stubs do not match this package "
            f"({__version__}); rerun cp-delivery-probe-install-skills <dir>:",
            file=sys.stderr,
        )
        for line in problems:
            print(f"  {line}", file=sys.stderr)


def library_root() -> None:
    """Print the library root. Instructions are under instructions/, types under types/."""
    _warn_on_problems()
    print(_library_dir())


def instruction() -> None:
    """Print the path of one library instruction, or list them all."""
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-instruction")
    parser.add_argument("name", nargs="?", help="instruction name without .md; omit to list")
    args = parser.parse_args()
    _warn_on_problems()
    instructions = _library_dir() / "instructions"
    if args.name is None:
        for path in sorted(instructions.glob("*.md")):
            print(path.stem)
        return
    path = instructions / f"{args.name}.md"
    if not path.is_file():
        sys.exit(f"no instruction named {args.name!r}; run without arguments to list them")
    print(path)


def install_skills() -> None:
    """Write, check, or remove the probe's skill stubs in one harness skill directory.

    Writing is idempotent: stubs this package wrote are replaced, stubs for skills
    the package no longer has are removed, and anything else is left alone.
    """
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-install-skills")
    parser.add_argument("target", help="harness skill directory, e.g. .claude/skills")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--remove", action="store_true", help="remove the probe's stubs")
    action.add_argument("--check", action="store_true", help="report status; exit 1 on problems")
    args = parser.parse_args()
    target = Path(args.target).expanduser()
    skills = _skills()
    failed = False
    for status, dest in _statuses(target):
        if args.check:
            print(f"{status}: {dest}")
            failed |= status != "ok"
            continue
        if status == "foreign":
            print(f"skipped {dest}: exists and is not a cp-delivery-probe stub", file=sys.stderr)
            failed = True
            continue
        if status != "missing":
            shutil.rmtree(dest)
        if args.remove or status == "extra":
            print(f"removed {dest}" if status != "missing" else f"absent {dest}")
            continue
        dest.mkdir(parents=True)
        (dest / "SKILL.md").write_text(_render_stub(skills[dest.name]))
        (dest / STUB_MARKER).write_text(__version__ + "\n")
        verb = "wrote" if status == "missing" else f"replaced ({status})"
        print(f"{verb} stub: {dest} -> {skills[dest.name] / 'SKILL.md'}")
    if failed:
        sys.exit(1)
