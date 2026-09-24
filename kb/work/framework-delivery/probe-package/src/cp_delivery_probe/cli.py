"""Commands a harness-neutral agent uses to find the probe library.

The package data under ``plugin/`` is the only tree: skills, the library, and a
Claude Code plugin manifest. Skills find library files through these commands;
relative links are only a fallback.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from importlib.resources import files
from pathlib import Path

from cp_delivery_probe import __version__

# A skill entry is ours when its link target, or its copy marker, says so.
# The marker text is independent of the install path, so it survives a move.
OWNED_TARGET = f"cp_delivery_probe{os.sep}plugin{os.sep}skills{os.sep}"
COPY_MARKER = ".cp-delivery-probe-managed"
DEFAULT_SKILL_DIRS = ["~/.agents/skills", "~/.claude/skills"]


def _plugin_dir() -> Path:
    root = Path(str(files("cp_delivery_probe") / "plugin")).resolve()
    if not root.is_dir():
        sys.exit(f"cp-delivery-probe {__version__}: plugin directory missing at {root}")
    return root


def _skill_dirs() -> list[Path]:
    """Harness skill directories to check: the defaults plus CP_DELIVERY_PROBE_SKILL_DIRS."""
    extra = os.environ.get("CP_DELIVERY_PROBE_SKILL_DIRS", "")
    names = DEFAULT_SKILL_DIRS + [d for d in extra.split(os.pathsep) if d]
    return [Path(d).expanduser() for d in names]


def _is_owned(entry: Path) -> bool:
    if entry.is_symlink():
        return OWNED_TARGET in os.readlink(entry)
    return (entry / COPY_MARKER).is_file()


def _skill_status(entry: Path, source: Path) -> str:
    """One of: ok, stale-copy, dangling, elsewhere, foreign, missing."""
    if not (entry.exists() or entry.is_symlink()):
        return "missing"
    if not _is_owned(entry):
        return "foreign"
    if entry.is_symlink():
        if not entry.exists():
            return "dangling"
        return "ok" if entry.resolve() == source.resolve() else "elsewhere"
    marker = (entry / COPY_MARKER).read_text().strip()
    return "ok" if marker == __version__ else "stale-copy"


def _problems() -> list[str]:
    """Installed probe skills that no longer serve the current package."""
    skills = _plugin_dir() / "skills"
    found = []
    for directory in _skill_dirs():
        if not directory.is_dir():
            continue
        for skill in sorted(p for p in skills.iterdir() if p.is_dir()):
            status = _skill_status(directory / skill.name, skill)
            if status in ("dangling", "elsewhere", "stale-copy"):
                found.append(f"{directory / skill.name}: {status}")
    return found


def _warn_on_problems() -> None:
    problems = _problems()
    if problems:
        print(
            "warning: installed delivery-probe skills do not match this package "
            f"({__version__}); rerun cp-delivery-probe-install-skills <dir>:",
            file=sys.stderr,
        )
        for line in problems:
            print(f"  {line}", file=sys.stderr)


def library_root() -> None:
    """Print the library root. Instructions are under instructions/, types under types/."""
    _warn_on_problems()
    print(_plugin_dir() / "library")


def plugin_path() -> None:
    """Print the plugin directory, for a Claude Code command-source marketplace entry."""
    print(_plugin_dir())


def instruction() -> None:
    """Print the path of one library instruction, or list them all."""
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-instruction")
    parser.add_argument("name", nargs="?", help="instruction name without .md; omit to list")
    args = parser.parse_args()
    _warn_on_problems()
    instructions = _plugin_dir() / "library" / "instructions"
    if args.name is None:
        for path in sorted(instructions.glob("*.md")):
            print(path.stem)
        return
    path = instructions / f"{args.name}.md"
    if not path.is_file():
        sys.exit(f"no instruction named {args.name!r}; run without arguments to list them")
    print(path)


def install_skills() -> None:
    """Install, check, or remove the probe skills in one harness skill directory.

    Installing is idempotent: entries this package owns (links into any install
    of it, or marked copies) are replaced; anything else is left alone.
    """
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-install-skills")
    parser.add_argument("target", help="harness skill directory, e.g. ~/.agents/skills")
    parser.add_argument("--mode", choices=["link", "copy"], default="link")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--remove", action="store_true", help="remove the probe skills")
    action.add_argument("--check", action="store_true", help="report status; exit 1 on problems")
    args = parser.parse_args()
    target = Path(args.target).expanduser()
    skills = _plugin_dir() / "skills"
    failed = False
    for skill in sorted(p for p in skills.iterdir() if p.is_dir()):
        dest = target / skill.name
        status = _skill_status(dest, skill)
        if args.check:
            print(f"{status}: {dest}")
            failed |= status != "ok"
            continue
        if status == "foreign":
            print(f"skipped {dest}: exists and is not managed by cp-delivery-probe", file=sys.stderr)
            failed = True
            continue
        if status != "missing":
            if dest.is_symlink():
                dest.unlink()
            else:
                shutil.rmtree(dest)
        if args.remove:
            print(f"removed {dest}" if status != "missing" else f"absent {dest}")
            continue
        target.mkdir(parents=True, exist_ok=True)
        if args.mode == "link":
            dest.symlink_to(skill, target_is_directory=True)
        else:
            shutil.copytree(skill, dest)
            (dest / COPY_MARKER).write_text(__version__ + "\n")
        verb = "installed" if status == "missing" else f"replaced ({status})"
        print(f"{verb} {args.mode}: {dest} -> {skill}")
    if failed:
        sys.exit(1)
