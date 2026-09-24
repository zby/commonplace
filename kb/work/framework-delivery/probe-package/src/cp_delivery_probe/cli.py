"""Commands a harness-neutral agent uses to find the probe library.

The package data under ``plugin/`` is the only tree: skills, the library they
link to by relative paths, and a Claude Code plugin manifest.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from importlib.resources import files
from pathlib import Path

from cp_delivery_probe import __version__


def _plugin_dir() -> Path:
    root = Path(str(files("cp_delivery_probe") / "plugin")).resolve()
    if not root.is_dir():
        sys.exit(f"cp-delivery-probe {__version__}: plugin directory missing at {root}")
    return root


def library_root() -> None:
    """Print the library root. Instructions are under instructions/, types under types/."""
    print(_plugin_dir() / "library")


def plugin_path() -> None:
    """Print the plugin directory, for a Claude Code command-source marketplace entry."""
    print(_plugin_dir())


def instruction() -> None:
    """Print the path of one library instruction, or list them all."""
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-instruction")
    parser.add_argument("name", nargs="?", help="instruction name without .md; omit to list")
    args = parser.parse_args()
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
    """Link or copy each packaged skill into a harness skill directory, or remove them."""
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-install-skills")
    parser.add_argument("target", help="harness skill directory, e.g. ~/.agents/skills")
    parser.add_argument("--mode", choices=["link", "copy"], default="link")
    parser.add_argument("--remove", action="store_true", help="remove the probe skills instead")
    args = parser.parse_args()
    target = Path(args.target).expanduser()
    skills = _plugin_dir() / "skills"
    for skill in sorted(p for p in skills.iterdir() if p.is_dir()):
        dest = target / skill.name
        if args.remove:
            if dest.is_symlink() or dest.is_file():
                dest.unlink()
            elif dest.is_dir():
                shutil.rmtree(dest)
            print(f"removed {dest}")
            continue
        if dest.exists() or dest.is_symlink():
            sys.exit(f"{dest} already exists; remove it first with --remove")
        target.mkdir(parents=True, exist_ok=True)
        if args.mode == "link":
            dest.symlink_to(skill, target_is_directory=True)
        else:
            shutil.copytree(skill, dest)
        print(f"{args.mode}: {dest} -> {skill}")
