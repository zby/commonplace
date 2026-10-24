"""The probe's stand-in for ``commonplace-init``, plus one ordinary command.

Revision 7 mirrors ``commonplace.lib.library`` and ``commonplace.cli.init_project``
as of 2026-10-24. The library is the only tree. It mirrors a KB layout:
instructions (with each skill in its own directory there), types, and the two
landings the routing file points at (tags, reference). A normal install places
it under ``<environment>/share/cp-delivery-probe/``, a path that survives a
change of the tool's Python version. An editable install reads it from the
source tree, because shared data is copied at install time.

Agents reach the library by reading files, never by running a command.
``cp-delivery-probe-init`` writes machine-specific, uncommitted outputs into a
project, exactly as ``commonplace-init`` does:

- a stub SKILL.md per promoted skill in ``.claude/skills/`` and
  ``.agents/skills/``, which redirects to the real SKILL.md by absolute path and
  passes ``$ARGUMENTS`` through when the real skill uses them;
- ``.cp-delivery-probe/library.md``, giving the library root, entry points and a
  skill index as full paths (AGENTS.md points to it, CLAUDE.md imports it);
- a Claude Code read rule for the library root in ``.claude/settings.local.json``,
  in the ``Read(//<posix path>/**)`` form, where ``//`` marks an absolute path;
- a ``.gitignore`` block covering all of the above.

It also writes, once, the two committed control-plane templates
(``AGENTS.md.template``, ``CLAUDE.md.template``) that a project adopts by
renaming, as ``commonplace-init`` does. The real init also scaffolds the
project's own collections; the probe omits that, since it tests delivery only.

Every command checks those outputs and warns when they no longer match.
``--remove`` is probe-only, for cleanup; ``commonplace-init`` has no such flag.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from cp_delivery_probe import __version__

SHARE_NAME = "cp-delivery-probe"
OUTPUT_DIR = Path(".cp-delivery-probe")
ROUTING = OUTPUT_DIR / "library.md"
RULE_RECORD = OUTPUT_DIR / "read-rule"
SETTINGS = Path(".claude/settings.local.json")
STUB_MARKER = ".cp-delivery-probe-stub"
SKILL_DIRS = (Path(".claude/skills"), Path(".agents/skills"))
GITIGNORE_BEGIN = "# cp-delivery-probe-init begin"
GITIGNORE_END = "# cp-delivery-probe-init end"
# The real init takes the skill set from a manifest, not from a directory glob;
# a skill directory in the library that is not listed here gets no stub.
PROMOTED_SKILLS = ("delivery-probe-read", "delivery-probe-delegate", "delivery-probe-echo")
ROUTER_SKILL = "delivery-probe-library"
TEMPLATES = ("AGENTS.md.template", "CLAUDE.md.template")


def read_text(path: Path) -> str:
    """UTF-8, accepting a byte-order mark (Windows editors write one)."""
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# --- library -------------------------------------------------------------------


def _source_library_dir() -> Path:
    # src/cp_delivery_probe/cli.py -> the package root's library/ directory
    return Path(__file__).resolve().parents[2] / "library"


def _library_dir() -> Path:
    """The library: the source tree for an editable install, else shared data."""
    source = _source_library_dir()
    root = source if (source / "instructions").is_dir() else Path(sys.prefix) / "share" / SHARE_NAME
    if not (root / "instructions").is_dir():
        sys.exit(f"cp-delivery-probe {__version__}: library not available at {root}; reinstall with uv")
    return root.resolve()


def _skills() -> dict[str, Path]:
    """Skill name -> the real skill directory, for every skill the project receives."""
    root = _library_dir()
    found = {}
    for name in (*PROMOTED_SKILLS, ROUTER_SKILL):
        skill = root / "instructions" / name
        if not (skill / "SKILL.md").is_file():
            sys.exit(f"library skill missing: {skill / 'SKILL.md'}")
        found[name] = skill
    return found


def _frontmatter(skill_md: Path) -> str:
    lines = read_text(skill_md).splitlines()
    if not lines or lines[0].strip() != "---":
        sys.exit(f"{skill_md}: no frontmatter")
    return "\n".join(lines[1 : lines.index("---", 1)])


def _description(skill_md: Path) -> str:
    for line in _frontmatter(skill_md).splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    sys.exit(f"{skill_md}: no description")


def _render_stub(skill: Path) -> str:
    """A stub carries the real skill's frontmatter, so the harness applies it, and redirects."""
    real = skill / "SKILL.md"
    arguments = (
        "\nThe arguments for this invocation are: $ARGUMENTS\n"
        "Where the real skill names its argument placeholder, use these.\n"
        if "$ARGUMENTS" in read_text(real)
        else ""
    )
    return (
        f"---\n{_frontmatter(real)}\n---\n\n"
        f"# {skill.name}\n\n"
        "This skill is installed as a stub. Read the real skill at\n\n"
        f"{real.as_posix()}\n\n"
        "and follow it exactly. Resolve every relative link in it against that file's "
        "directory, not this stub's.\n"
        f"{arguments}"
    )


def _render_routing() -> str:
    """The routing file: library root, entry points, and a skill index.

    The skill index emulates the skills mechanism for harnesses without one, and
    serves agents outside it; stubs are generated from the same skills.
    """
    root = _library_dir()
    index = "".join(
        f"- `{name}` — {_description(skill / 'SKILL.md')}\n  {(skill / 'SKILL.md').as_posix()}\n"
        for name, skill in _skills().items()
    )
    return (
        "# Delivery-probe library on this machine\n\n"
        "Generated by `cp-delivery-probe-init` for this machine. Do not commit or edit; "
        "rerun `cp-delivery-probe-init` to refresh it.\n\n"
        f"Library root: {root.as_posix()}\n\n"
        f"- Instructions and skill bodies: {(root / 'instructions').as_posix()}/ "
        "(find one by searching the `description:` lines)\n"
        f"- Tag heads (browse the notes by topic): {(root / 'tags' / 'README.md').as_posix()}\n"
        f"- Reference: {(root / 'reference' / 'README.md').as_posix()}\n"
        f"- Global types: {(root / 'types').as_posix()}/\n\n"
        "Read library files by full path. Links inside a library file are relative to that file.\n\n"
        "## Skills\n\n"
        "When a task matches a skill's description, read that skill's SKILL.md at the path "
        "given and follow it, resolving its links relative to that file. Where the harness "
        "also lists these skills itself, both routes lead to the same file. If the request "
        "carries arguments, use them wherever the skill names its argument placeholder; "
        "reading the file does not substitute them.\n\n"
        f"{index}"
    )


def _read_rule() -> str:
    """Claude Code allow rule for reading the library. `//` marks an absolute path."""
    return f"Read(//{_library_dir().as_posix().lstrip('/')}/**)"


def _load_settings(project: Path) -> dict:
    path = project / SETTINGS
    return json.loads(read_text(path)) if path.is_file() else {}


# --- status --------------------------------------------------------------------


def _statuses(project: Path) -> list[tuple[str, Path]]:
    """(status, output) for every init output. Status: ok, stale, missing, foreign, extra."""
    wanted = _skills()
    found = []
    for skill_dir in SKILL_DIRS:
        directory = project / skill_dir
        for name, skill in wanted.items():
            dest = directory / name
            if not dest.exists():
                found.append(("missing", dest))
            elif dest.is_symlink() or not (dest / STUB_MARKER).is_file():
                # A symlinked skill directory is someone else's; never write through it.
                found.append(("foreign", dest))
            else:
                stub = dest / "SKILL.md"
                current = stub.is_file() and read_text(stub) == _render_stub(skill)
                found.append(("ok" if current else "stale", dest))
        if directory.is_dir():
            for dest in sorted(directory.iterdir()):
                if dest.name not in wanted and not dest.is_symlink() and (dest / STUB_MARKER).is_file():
                    found.append(("extra", dest))
    routing = project / ROUTING
    if not routing.is_file():
        found.append(("missing", routing))
    else:
        found.append(("ok" if read_text(routing) == _render_routing() else "stale", routing))
    allowed = _load_settings(project).get("permissions", {}).get("allow", [])
    record = project / RULE_RECORD
    if _read_rule() in allowed:
        found.append(("ok", project / SETTINGS))
    elif record.is_file() and read_text(record).strip() in allowed:
        found.append(("stale", project / SETTINGS))
    else:
        found.append(("missing", project / SETTINGS))
    return found


def _type_collisions(project: Path) -> list[tuple[str, Path]]:
    """Project `kb/types/<name>.md` files that shadow a library global type."""
    library_types = _library_dir() / "types"
    project_types = project / "kb" / "types"
    if not project_types.is_dir():
        return []
    return [
        ("collision", path)
        for path in sorted(project_types.glob("*.md"))
        if (library_types / path.name).is_file() and (library_types / path.name).resolve() != path.resolve()
    ]


def _initialized(project: Path) -> bool:
    """Whether init has set this project up. The bare output directory is not evidence."""
    return (project / ROUTING).is_file() or (project / RULE_RECORD).is_file()


def _find_project(start: Path) -> Path | None:
    """The nearest directory at or above start that init has set up."""
    here = start.resolve()
    for candidate in (here, *here.parents):
        if _initialized(candidate):
            return candidate
    return None


def _warn_if_stale(start: Path) -> None:
    project = _find_project(start)
    if project is None:
        return
    problems = [(s, p) for s, p in _statuses(project) if s in ("stale", "missing", "extra")]
    if problems:
        print(
            f"warning: cp-delivery-probe project files are out of date with the installed library "
            f"({__version__}); rerun cp-delivery-probe-init:",
            file=sys.stderr,
        )
        for status, path in problems:
            print(f"  {status}: {path}", file=sys.stderr)


def library_root() -> None:
    """Print the library root, for testers. Like every command, check the current project first."""
    _warn_if_stale(Path.cwd())
    print(_library_dir())


# --- writing ---------------------------------------------------------------------


def _write_if_changed(project: Path, rel: Path, text: str, report: dict[str, list[Path]]) -> None:
    target = project / rel
    if target.is_file():
        if read_text(target) == text:
            return
        write_text(target, text)
        report["refreshed"].append(rel)
        return
    write_text(target, text)
    report["created"].append(rel)


def _write_stubs(project: Path, report: dict[str, list[Path]]) -> None:
    skills = _skills()
    for status, path in _statuses(project):
        if path.parent.name != "skills" or path.parent.parent.name not in (".claude", ".agents"):
            continue
        rel = path.relative_to(project)
        if status == "foreign":
            report["skipped_foreign"].append(rel)
            continue
        if status == "extra":
            shutil.rmtree(path)
            report["removed"].append(rel)
            continue
        _write_if_changed(project, rel / "SKILL.md", _render_stub(skills[path.name]), report)
        marker = path / STUB_MARKER
        if not marker.is_file():
            write_text(marker, "Written by cp-delivery-probe-init; rerun it to refresh.\n")


def _write_read_rule(project: Path, report: dict[str, list[Path]]) -> None:
    settings = _load_settings(project)
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])
    record = project / RULE_RECORD
    rule = _read_rule()
    previous = read_text(record).strip() if record.is_file() else None
    if previous == rule and rule in allow:
        return
    if previous and previous in allow:
        allow.remove(previous)
    if rule not in allow:
        allow.append(rule)
    write_text(project / SETTINGS, json.dumps(settings, indent=2) + "\n")
    write_text(record, rule + "\n")
    report["refreshed"].append(SETTINGS)


def _gitignore_lines(project: Path) -> list[str]:
    path = project / ".gitignore"
    lines = read_text(path).splitlines() if path.is_file() else []
    if GITIGNORE_BEGIN in lines:
        start = lines.index(GITIGNORE_BEGIN)
        del lines[start : lines.index(GITIGNORE_END, start) + 1]
    return lines


def _write_gitignore(project: Path, report: dict[str, list[Path]]) -> None:
    stubs = [f"/{d.as_posix()}/{name}/" for d in SKILL_DIRS for name in _skills()]
    lines = [
        *_gitignore_lines(project),
        GITIGNORE_BEGIN,
        f"/{OUTPUT_DIR.as_posix()}/",
        f"/{SETTINGS.as_posix()}",
        *stubs,
        GITIGNORE_END,
    ]
    _write_if_changed(project, Path(".gitignore"), "\n".join(lines) + "\n", report)


def _write_templates(project: Path, report: dict[str, list[Path]]) -> None:
    """The committed control-plane templates, written once; an existing file is preserved."""
    for name in TEMPLATES:
        target = project / name
        text = (Path(__file__).resolve().parent / "templates" / name).read_text(encoding="utf-8")
        if target.exists():
            report["preserved_identical" if read_text(target) == text else "preserved_different"].append(Path(name))
            continue
        write_text(target, text)
        report["created"].append(Path(name))


def _remove(project: Path) -> None:
    """Probe-only cleanup: delete everything init wrote."""
    for skill_dir in SKILL_DIRS:
        directory = project / skill_dir
        if not directory.is_dir():
            continue
        for dest in sorted(directory.iterdir()):
            if not dest.is_symlink() and (dest / STUB_MARKER).is_file():
                shutil.rmtree(dest)
                print(f"removed {dest}")
        for empty in (directory, directory.parent):
            if empty.is_dir() and not any(empty.iterdir()):
                empty.rmdir()
    settings = _load_settings(project)
    allow = settings.get("permissions", {}).get("allow", [])
    record = project / RULE_RECORD
    for rule in {_read_rule(), read_text(record).strip() if record.is_file() else ""}:
        if rule in allow:
            allow.remove(rule)
    if "permissions" in settings and not allow:
        settings["permissions"].pop("allow", None)
        if not settings["permissions"]:
            del settings["permissions"]
    if settings:
        write_text(project / SETTINGS, json.dumps(settings, indent=2) + "\n")
    else:
        (project / SETTINGS).unlink(missing_ok=True)
    lines = _gitignore_lines(project)
    if lines:
        write_text(project / ".gitignore", "\n".join(lines) + "\n")
    else:
        (project / ".gitignore").unlink(missing_ok=True)
    shutil.rmtree(project / OUTPUT_DIR, ignore_errors=True)
    for name in TEMPLATES:
        (project / name).unlink(missing_ok=True)
    for d in SKILL_DIRS:
        for empty in (project / d, project / d.parent):
            if empty.is_dir() and not any(empty.iterdir()):
                empty.rmdir()
    print(f"removed {project / OUTPUT_DIR}, the read rule, the .gitignore block, and the templates")


def _print_section(title: str, paths: list[Path]) -> None:
    if paths:
        print(title)
        for path in paths:
            print(f"- {path.as_posix()}")


def init() -> None:
    """Write or check this package's outputs in one project. Idempotent."""
    parser = argparse.ArgumentParser(prog="cp-delivery-probe-init", description=__doc__)
    parser.add_argument("--root", default=".", help="project root to initialize")
    action = parser.add_mutually_exclusive_group()
    action.add_argument(
        "--check",
        action="store_true",
        help="report whether the project's pointers into the library are current; write nothing",
    )
    action.add_argument("--remove", action="store_true", help="probe-only: remove everything init wrote")
    args = parser.parse_args()
    project = Path(args.root).resolve()
    if args.check:
        problems = 0
        for status, path in (*_statuses(project), *_type_collisions(project)):
            print(f"{status}: {path.relative_to(project).as_posix()}")
            problems += status != "ok"
        sys.exit(1 if problems else 0)
    if args.remove:
        _remove(project)
        return
    sections = ("created", "refreshed", "removed", "skipped_foreign", "preserved_identical", "preserved_different")
    report: dict[str, list[Path]] = {key: [] for key in sections}
    _write_templates(project, report)
    _write_stubs(project, report)
    _write_if_changed(project, ROUTING, _render_routing(), report)
    _write_read_rule(project, report)
    _write_gitignore(project, report)
    print(f"Initialized delivery-probe project at {project}")
    _print_section("Created:", report["created"])
    _print_section("Refreshed pointers into the installed library:", report["refreshed"])
    _print_section("Removed obsolete skill stubs:", report["removed"])
    _print_section(
        "Skipped skill directories not written by cp-delivery-probe-init "
        "(remove them to receive the library's skill):",
        report["skipped_foreign"],
    )
    _print_section("Preserved existing files already matching scaffold:", report["preserved_identical"])
    _print_section("Preserved existing files differing from current scaffold output:", report["preserved_different"])
    if not any(report.values()):
        print("No changes needed.")
