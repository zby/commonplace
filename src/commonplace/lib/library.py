"""The installed Commonplace library and the project files that point into it.

The library (instructions with the promoted skills, notes, reference, tags, and the
global types) ships as wheel shared data under ``<tool environment>/share/commonplace/``,
laid out like the source repository's ``kb/``. That path does not change with the
tool's Python version. An editable install reads the source tree's ``kb/`` instead,
because shared data is copied at install time.

Projects never contain library files. ``commonplace-init`` writes three
machine-specific, uncommitted outputs that point into the library:

- a stub ``SKILL.md`` per promoted skill in each runtime skill directory, which
  redirects the agent to the real ``SKILL.md`` by absolute path;
- ``.commonplace/library.md``: the library root, its entry points, and a skill
  index that emulates the skills mechanism for harnesses without one;
- a Claude Code read rule for the library root in ``.claude/settings.local.json``.

Every ``commonplace-*`` command compares these outputs with what init would
write now and warns when they are stale.
"""

from __future__ import annotations

import functools
import json
import os
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from commonplace.scaffold_manifest import MANIFEST

SHARE_NAME = "commonplace"
LIBRARY_ENV = "COMMONPLACE_LIBRARY_ROOT"  # override, for tests and custom layouts
OUTPUT_DIR = Path(".commonplace")
ROUTING = OUTPUT_DIR / "library.md"
RULE_RECORD = OUTPUT_DIR / "read-rule"
SETTINGS = Path(".claude/settings.local.json")
STUB_MARKER = ".commonplace-stub"
GITIGNORE_BEGIN = "# commonplace-init begin"
GITIGNORE_END = "# commonplace-init end"


class LibraryMissingError(RuntimeError):
    """The Commonplace library is not available from this installation."""


def _source_checkout_kb() -> Path | None:
    """The source repository's kb/ when running from an editable checkout."""
    repo = Path(__file__).resolve().parents[3]
    if (repo / "pyproject.toml").is_file() and (repo / "src" / "commonplace").is_dir():
        kb = repo / "kb"
        if (kb / "instructions").is_dir():
            return kb
    return None


def library_root() -> Path:
    """The library root: the source tree's kb/ for an editable install, else shared data.

    ``COMMONPLACE_LIBRARY_ROOT`` overrides both.
    """
    return _library_root(os.environ.get(LIBRARY_ENV))


@functools.cache
def _library_root(override: str | None) -> Path:
    if override:
        # An explicit root may hold only part of a library, as test repositories do.
        return Path(override).resolve()
    root = _source_checkout_kb() or Path(sys.prefix) / "share" / SHARE_NAME
    if not (root / "instructions").is_dir():
        raise LibraryMissingError(
            f"Commonplace library not available at {root}; reinstall llm-commonplace with uv"
        )
    return root.resolve()


def read_text(path: Path) -> str:
    """Read a text file as UTF-8, accepting a byte-order mark (Windows editors write one)."""
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# --- artifact identity -----------------------------------------------------------

LIBRARY_IDENTITY_PREFIX = "commonplace:"


def is_library_identity(identity: str) -> bool:
    return identity.startswith(LIBRARY_IDENTITY_PREFIX)


def artifact_identity(repo_root: Path, path: Path) -> str:
    """Stable identity of a file used as review input.

    A file inside the repository is named by its repo-relative path. A library
    file outside the repository is named `commonplace:<path under the library
    root>`, which stays the same when the installation moves.
    """
    resolved = path.resolve()
    try:
        return resolved.relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        pass
    try:
        rel = resolved.relative_to(library_root())
    except ValueError as exc:
        raise ValueError(f"path is neither in the repository nor in the library: {path}") from exc
    return LIBRARY_IDENTITY_PREFIX + rel.as_posix()


def artifact_file(repo_root: Path, identity: str) -> Path:
    """The file an identity names. The identity's form decides; there is no fallback."""
    if is_library_identity(identity):
        rel = identity[len(LIBRARY_IDENTITY_PREFIX) :]
        root = library_root()
        path = (root / rel).resolve()
        if not path.is_relative_to(root) or not rel:
            raise ValueError(f"library identity escapes the library: {identity}")
        return path
    return repo_root / identity


# --- skills ------------------------------------------------------------------


def skills(root: Path | None = None) -> dict[str, Path]:
    """Skill name -> real skill directory, for every skill the project receives."""
    root = root or library_root()
    found = {}
    for name in (*MANIFEST.promoted_skills, MANIFEST.router_skill):
        skill = root / "instructions" / name
        if not (skill / "SKILL.md").is_file():
            raise LibraryMissingError(f"library skill missing: {skill / 'SKILL.md'}")
        found[name] = skill
    return found


def _frontmatter(skill_md: Path) -> str:
    lines = read_text(skill_md).splitlines()
    if not lines or lines[0].strip() != "---":
        raise LibraryMissingError(f"{skill_md}: no frontmatter")
    return "\n".join(lines[1 : lines.index("---", 1)])


def _description(skill_md: Path) -> str:
    for line in _frontmatter(skill_md).splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    raise LibraryMissingError(f"{skill_md}: no description")


def render_stub(skill: Path) -> str:
    """A stub carries the real skill's frontmatter, so the harness applies it, and redirects."""
    real = skill / "SKILL.md"
    arguments = (
        "\nThe arguments for this invocation are: $ARGUMENTS\n"
        "Where the real skill refers to `$ARGUMENTS`, use these.\n"
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


# --- routing file and read rule -------------------------------------------------


def render_routing(root: Path | None = None) -> str:
    root = root or library_root()
    index = "".join(
        f"- `{name}` — {_description(skill / 'SKILL.md')}\n  {(skill / 'SKILL.md').as_posix()}\n"
        for name, skill in skills(root).items()
    )
    return (
        "# Commonplace library on this machine\n\n"
        "Generated by `commonplace-init` for this machine. Do not commit or edit; "
        "rerun `commonplace-init` to refresh it.\n\n"
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
        "also lists these skills itself, both routes lead to the same file.\n\n"
        f"{index}"
    )


def read_rule(root: Path | None = None) -> str:
    """Claude Code allow rule for reading the library. `//` marks an absolute path."""
    root = root or library_root()
    return f"Read(//{root.as_posix().lstrip('/')}/**)"


def load_settings(project: Path) -> dict:
    path = project / SETTINGS
    return json.loads(read_text(path)) if path.is_file() else {}


# --- status -------------------------------------------------------------------


@dataclass(frozen=True)
class OutputStatus:
    """One init output and its state: ok, stale, missing, foreign, or extra.

    `commonplace-init --check` also reports a project type file that collides
    with a library global type as `collision`.
    """

    status: str
    path: Path


def statuses(project: Path, root: Path | None = None) -> list[OutputStatus]:
    """Compare init's outputs in a project with what init would write now."""
    root = root or library_root()
    wanted = skills(root)
    found: list[OutputStatus] = []
    for skill_dir in MANIFEST.skills_dirs:
        directory = project / skill_dir
        for name, skill in wanted.items():
            dest = directory / name
            if not dest.exists():
                found.append(OutputStatus("missing", dest))
            elif dest.is_symlink() or not (dest / STUB_MARKER).is_file():
                # A symlinked skill directory is someone else's; never write through it.
                found.append(OutputStatus("foreign", dest))
            else:
                stub = dest / "SKILL.md"
                current = stub.is_file() and read_text(stub) == render_stub(skill)
                found.append(OutputStatus("ok" if current else "stale", dest))
        if directory.is_dir():
            for dest in sorted(directory.iterdir()):
                if dest.name not in wanted and not dest.is_symlink() and (dest / STUB_MARKER).is_file():
                    found.append(OutputStatus("extra", dest))
    routing = project / ROUTING
    if not routing.is_file():
        found.append(OutputStatus("missing", routing))
    else:
        current = read_text(routing) == render_routing(root)
        found.append(OutputStatus("ok" if current else "stale", routing))
    allowed = load_settings(project).get("permissions", {}).get("allow", [])
    record = project / RULE_RECORD
    if read_rule(root) in allowed:
        found.append(OutputStatus("ok", project / SETTINGS))
    elif record.is_file() and read_text(record).strip() in allowed:
        found.append(OutputStatus("stale", project / SETTINGS))
    else:
        found.append(OutputStatus("missing", project / SETTINGS))
    return found


def stale_outputs(project: Path) -> list[OutputStatus]:
    """Init outputs that need a rerun of init; empty for a project init never set up."""
    if not (project / OUTPUT_DIR).is_dir():
        return []
    return [s for s in statuses(project) if s.status in ("stale", "missing", "extra")]


def find_project(start: Path | None = None) -> Path | None:
    """The nearest directory at or above start that init has set up."""
    here = (start or Path.cwd()).resolve()
    for candidate in (here, *here.parents):
        if (candidate / OUTPUT_DIR).is_dir():
            return candidate
    return None


def warn_if_stale(start: Path | None = None) -> None:
    """Print a warning to stderr when this project's init outputs no longer match the library."""
    project = find_project(start)
    if project is None:
        return
    try:
        problems = stale_outputs(project)
    except LibraryMissingError as exc:
        print(f"warning: {exc}", file=sys.stderr)
        return
    if problems:
        print(
            "warning: Commonplace project files are out of date with the installed library; "
            "rerun commonplace-init:",
            file=sys.stderr,
        )
        for item in problems:
            print(f"  {item.status}: {item.path}", file=sys.stderr)


def checks_library(main: Callable[..., object]) -> Callable[..., object]:
    """Decorate a command's main so it first warns about stale init outputs."""

    @functools.wraps(main)
    def wrapper(*args: object, **kwargs: object) -> object:
        warn_if_stale()
        return main(*args, **kwargs)

    return wrapper
