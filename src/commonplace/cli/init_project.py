"""Initialize a Commonplace project, or refresh its pointers into the installed library.

The project receives its own collections and their contracts once. On every run
init also writes the machine-specific pointers into the installed library (skill
stubs, `.commonplace/library.md`, a Claude Code read rule) and migrates copies of
the library left by earlier releases. Run it again after an upgrade that changes
the skill set, or after switching between editable and normal installs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, distribution
from importlib.resources import as_file, files
from pathlib import Path

from commonplace.lib import library
from commonplace.lib.snapshot import migrate_snapshot_types
from commonplace.scaffold_manifest import MANIFEST


@dataclass
class InitReport:
    created: list[Path] = field(default_factory=list)
    preserved_identical: list[Path] = field(default_factory=list)
    preserved_different: list[Path] = field(default_factory=list)
    refreshed: list[Path] = field(default_factory=list)
    removed: list[Path] = field(default_factory=list)
    migration_kept: list[Path] = field(default_factory=list)
    skipped_foreign: list[Path] = field(default_factory=list)
    retired_baselines: list[str] = field(default_factory=list)
    replaced_skill_copies: list[Path] = field(default_factory=list)
    rewritten_type_pointers: list[Path] = field(default_factory=list)
    repinned_result_checksums: list[Path] = field(default_factory=list)
    rewritten_snapshots: list[Path] = field(default_factory=list)
    repinned_ingests: list[Path] = field(default_factory=list)


def _record_existing(
    report: InitReport,
    rel_path: Path,
    target: Path,
    expected_bytes: bytes,
    acceptable_existing_bytes: tuple[bytes, ...] = (),
) -> None:
    if target.is_file():
        current_bytes = target.read_bytes()
        if current_bytes == expected_bytes or current_bytes in acceptable_existing_bytes:
            report.preserved_identical.append(rel_path)
            return
    report.preserved_different.append(rel_path)


def _copy_tree_files(
    src_dir: Path,
    dest_root: Path,
    target_rel: str | Path,
    report: InitReport,
) -> None:
    """Recursively copy a directory tree, classifying existing files."""
    for src_file in sorted(src_dir.rglob("*")):
        if not src_file.is_file():
            continue
        rel = src_file.relative_to(src_dir)
        rel_path = Path(target_rel) / rel
        target = dest_root / rel_path
        expected_bytes = src_file.read_bytes()
        if target.exists():
            _record_existing(report, rel_path, target, expected_bytes)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, target)
        report.created.append(rel_path)


def _copy_scaffold_file(
    scaffold_root: Path,
    src_rel: str,
    dest_root: Path,
    target_rel: str,
    report: InitReport,
) -> None:
    """Copy a single scaffold file, classifying an existing target."""
    src = _resolve_scaffold_source(scaffold_root, src_rel)
    rel_path = Path(target_rel)
    target = dest_root / rel_path
    expected_bytes = src.read_bytes()
    if target.exists():
        _record_existing(report, rel_path, target, expected_bytes)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, target)
    report.created.append(rel_path)


def _write_template(
    src: Path,
    target: Path,
    rel_path: Path,
    replacements: dict[str, str],
    report: InitReport,
) -> None:
    """Read a template, apply replacements, write to target or classify existing."""
    text = src.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    expected_bytes = text.encode("utf-8")
    if target.exists():
        _record_existing(
            report,
            rel_path,
            target,
            expected_bytes,
            acceptable_existing_bytes=(src.read_bytes(),),
        )
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    report.created.append(rel_path)


def _resolve_scaffold_source(scaffold_root: Path, src_rel: str) -> Path:
    """Resolve scaffold input from packaged data or a source checkout.

    Wheels include the scaffold under `commonplace/_data/`. Editable source
    checkouts read the canonical repo paths directly.
    """
    packaged = scaffold_root / src_rel
    if packaged.exists():
        return packaged

    source_root = Path(__file__).resolve().parents[3]
    for source in (source_root / src_rel, source_root / "src" / "commonplace" / "_data" / src_rel):
        if source.exists():
            return source

    raise FileNotFoundError(f"Scaffold source is missing: {src_rel}")


# --- pointers into the installed library ----------------------------------------


def _write_if_changed(project: Path, rel_path: Path, text: str, report: InitReport) -> None:
    target = project / rel_path
    if target.is_file():
        if library.read_text(target) == text:
            return
        library.write_text(target, text)
        report.refreshed.append(rel_path)
        return
    library.write_text(target, text)
    report.created.append(rel_path)


def _write_stubs(project: Path, root: Path, report: InitReport) -> None:
    for status in library.statuses(project, root):
        path = status.path
        if path.parent.name != "skills" or path.parent.parent.name not in (".claude", ".agents"):
            continue
        rel = path.relative_to(project)
        if status.status == "foreign":
            report.skipped_foreign.append(rel)
            continue
        if status.status == "extra":
            shutil.rmtree(path)
            report.removed.append(rel)
            continue
        skill = library.skills(root)[path.name]
        _write_if_changed(project, rel / "SKILL.md", library.render_stub(skill), report)
        marker = path / library.STUB_MARKER
        if not marker.is_file():
            library.write_text(marker, "Written by commonplace-init; rerun it to refresh.\n")


def _write_read_rule(project: Path, root: Path, report: InitReport) -> None:
    settings = library.load_settings(project)
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])
    record = project / library.RULE_RECORD
    rule = library.read_rule(root)
    previous = library.read_text(record).strip() if record.is_file() else None
    if previous == rule and rule in allow:
        return
    if previous and previous in allow:
        allow.remove(previous)
    if rule not in allow:
        allow.append(rule)
    library.write_text(project / library.SETTINGS, json.dumps(settings, indent=2) + "\n")
    library.write_text(record, rule + "\n")
    report.refreshed.append(library.SETTINGS)


def _write_gitignore(project: Path, root: Path, report: InitReport) -> None:
    path = project / ".gitignore"
    lines = library.read_text(path).splitlines() if path.is_file() else []
    if library.GITIGNORE_BEGIN in lines:
        start = lines.index(library.GITIGNORE_BEGIN)
        del lines[start : lines.index(library.GITIGNORE_END, start) + 1]
    stubs = [f"/{d.as_posix()}/{name}/" for d in MANIFEST.skills_dirs for name in library.skills(root)]
    lines += [
        library.GITIGNORE_BEGIN,
        f"/{library.OUTPUT_DIR.as_posix()}/",
        f"/{library.SETTINGS.as_posix()}",
        *stubs,
        library.GITIGNORE_END,
    ]
    _write_if_changed(project, Path(".gitignore"), "\n".join(lines) + "\n", report)


# --- migration of copies left by earlier releases ---------------------------------


def _real_files(directory: Path) -> list[Path]:
    """Regular files under directory, not following or including symlinks."""
    found = []
    for dirpath, dirnames, filenames in os.walk(directory, followlinks=False):
        here = Path(dirpath)
        dirnames[:] = [d for d in dirnames if not (here / d).is_symlink()]
        found += [here / f for f in filenames if not (here / f).is_symlink()]
    return found


def _migrate_legacy_copies(project: Path, root: Path, report: InitReport) -> None:
    """Remove library copies that match the installed library; keep and list the rest.

    A differing file may carry a local change, and the old copies record no
    version, so only exact matches are removed.
    """
    copies = [(Path(copy), root / origin) for copy, origin in MANIFEST.legacy_copies]
    copies += [
        (skills_dir / name, skill)
        for skills_dir in MANIFEST.skills_dirs
        for name, skill in library.skills(root).items()
        if not (project / skills_dir / name / library.STUB_MARKER).exists()
    ]
    for copy_rel, origin in copies:
        copy_dir = project / copy_rel
        # Never traverse or delete through a symlink: its target is not the project's copy.
        if copy_dir.is_symlink() or not copy_dir.is_dir():
            continue
        for path in sorted(_real_files(copy_dir)):
            counterpart = origin / path.relative_to(copy_dir)
            if counterpart.is_file() and counterpart.read_bytes() == path.read_bytes():
                path.unlink()
                report.removed.append(path.relative_to(project))
                if copy_rel.parent in MANIFEST.skills_dirs and copy_rel not in report.replaced_skill_copies:
                    report.replaced_skill_copies.append(copy_rel)
            # A type directory may also hold the project's own types, which are not copies.
            elif copy_rel.name != "types" or counterpart.exists():
                report.migration_kept.append(path.relative_to(project))
        for dirpath, _dirnames, _filenames in sorted(os.walk(copy_dir, followlinks=False), reverse=True):
            directory = Path(dirpath)
            if directory != copy_dir and not directory.is_symlink() and not any(directory.iterdir()):
                directory.rmdir()
        # A type directory the scaffold also creates stays, for the project's own types.
        if not any(copy_dir.iterdir()) and copy_rel not in MANIFEST.directories:
            copy_dir.rmdir()
    legacy_parent = project / "kb" / "commonplace"
    if legacy_parent.is_dir() and not any(legacy_parent.iterdir()):
        legacy_parent.rmdir()


def _is_legacy_criterion(identity: str, root: Path) -> bool:
    """A criterion recorded under a copy of the library that projects no longer hold."""
    if identity.startswith("kb/commonplace/"):
        return True
    path = Path(identity)
    return (
        path.parent.as_posix() == "kb/types"
        and (root / "types" / path.name).is_file()
    )


def _retire_legacy_baselines(project: Path, root: Path, report: InitReport) -> None:
    """Retire, once, review baselines whose criteria lived in the old library copy.

    Their criteria now have library identities, so those pairs start again as
    missing baselines; review history is kept.
    """
    from commonplace.freshness.transitions import REVIEW_PAIR_KIND, retire_target
    from commonplace.review import review_db

    db_path = review_db.resolve_db_path(project)
    if not db_path.is_file():
        return
    with review_db.connect(db_path) as conn:
        baselines = review_db.load_current_freshness_baselines(conn)
        for note_path, criterion_path, model_partition in sorted(baselines):
            if not _is_legacy_criterion(criterion_path, root):
                continue
            retire_target(
                conn,
                target_kind=REVIEW_PAIR_KIND,
                target_key={
                    "note_path": note_path,
                    "criterion_path": criterion_path,
                    "model_partition": model_partition,
                },
            )
            report.retired_baselines.append(f"{note_path} × {criterion_path} ({model_partition})")
        conn.commit()


_TYPE_LINE = re.compile(
    r"^([ \t]*(?:type|requires_type):[ \t]*)(\"?)([^\s\"]+)\2[ \t]*$", re.MULTILINE
)
_JSON_TYPE = re.compile(r'("(?:type|requires_type)"\s*:\s*)"([^"]+)"')
_SCHEMA_REF = re.compile(r'(\$ref"?\s*:\s*["\']?)([^"\'\s]+\.schema\.(?:yaml|json))')
_BARE_TYPE_NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_RESULT_PIN = re.compile(r'("?analysis-result-sha256"?\s*:\s*"?)([0-9a-f]{64})')
# Replaceable outputs are never rewritten. Report state holds live reports, whose
# type values are migrated, and frozen evidence copies, which keep their values
# as recorded; captures under .snapshots/ belong to migrate_snapshot_types.
_MIGRATION_SKIP = "kb/reports/cache/"
_FROZEN_POINTER_AREA = "kb/reports/state/"
_LIVE_STATE_TYPES = frozenset(
    {
        "agent-memory-analysis-report",
        "agentic-system-analysis-run-state",
        "connect-report",
        "full-pass-report",
    }
)


def _project_files(project: Path, pattern: str) -> list[Path]:
    kb = project / "kb"
    if not kb.is_dir():
        return []
    return [
        path
        for path in _real_files(kb)
        if path.match(pattern)
        and ".snapshots" not in path.parts
        and not path.relative_to(project).as_posix().startswith(_MIGRATION_SKIP)
    ]


def _repin_result_checksums(project: Path, rehashed: dict[str, str], report: InitReport) -> None:
    """Point `analysis-result-sha256` pins at results whose type line init rewrote."""
    if not rehashed:
        return
    for path in _project_files(project, "*.md"):
        text = library.read_text(path)
        new = _RESULT_PIN.sub(lambda m: m.group(1) + rehashed.get(m.group(2), m.group(2)), text)
        if new != text:
            library.write_text(path, new)
            report.repinned_result_checksums.append(path.relative_to(project))


def _migrate_type_pointers(project: Path, root: Path, report: InitReport) -> None:
    """Rewrite a project's type values in the form this release uses (ADR 088).

    A `type:` or `requires_type:` value (YAML or JSON-style) becomes the spec's
    path under a KB root:

    - a bare global name `X`, or a path to an old project copy of a global type
      (under `kb/types/`, `kb/sources/types/`, or `kb/reports/types/`) that init
      removed, becomes `types/X.md`;
    - a `kb/...`, `./`, or `../` path to a file in the project's `kb/` becomes
      that file's path under `kb/`.

    A kept, differing copy of a global type is therefore named `types/X.md` and
    collides with the library's file, which validation reports. A schema `$ref`
    to a removed copy's schema becomes `commonplace:types/X.schema.yaml`. Every
    rewritten file is reported.
    """
    copy_dirs = {
        (project / copy).resolve()
        for copy, origin in MANIFEST.legacy_copies
        if origin == "types"
    }
    kb = (project / "kb").resolve()
    global_names = {p.stem for p in (root / "types").glob("*.md")}
    # A retained analysis result is pinned by its checksum; rewriting its type line
    # re-pins it, so record each rewritten file's checksums.
    rehashed: dict[str, str] = {}

    def new_value(value: str, source: Path) -> str | None:
        if _BARE_TYPE_NAME.match(value):
            name, result = value, (f"types/{value}.md" if value in global_names else None)
        elif value.startswith(("kb/", "./", "../")) and value.endswith(".md"):
            target = ((project / value) if value.startswith("kb/") else (source.parent / value)).resolve()
            name = target.stem
            if target.parent in copy_dirs and not target.exists() and name in global_names:
                result = f"types/{name}.md"
            elif target.is_file() and target.is_relative_to(kb):
                result = target.relative_to(kb).as_posix()
            else:
                result = None
        else:
            return None
        frozen = source.relative_to(project).as_posix().startswith(_FROZEN_POINTER_AREA)
        if frozen and name not in _LIVE_STATE_TYPES:
            return None
        return result

    for path in _project_files(project, "*.md"):
        text = library.read_text(path)
        # Only frontmatter binds a type; the body may quote paths as prose.
        match = re.match(r"---\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$)", text, re.DOTALL)
        if match is None:
            continue
        head = match.group(0)

        def yaml_value(m: re.Match[str], source: Path = path) -> str:
            value = new_value(m.group(3), source)
            return f"{m.group(1)}{value}" if value else m.group(0)

        def json_value(m: re.Match[str], source: Path = path) -> str:
            value = new_value(m.group(2), source)
            return f'{m.group(1)}"{value}"' if value else m.group(0)

        new_head = _JSON_TYPE.sub(json_value, _TYPE_LINE.sub(yaml_value, head))
        new = new_head + text[len(head) :]
        if new != text:
            old_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            library.write_text(path, new)
            rehashed[old_hash] = hashlib.sha256(path.read_bytes()).hexdigest()
            report.rewritten_type_pointers.append(path.relative_to(project))
    _repin_result_checksums(project, rehashed, report)
    for pattern in ("*.schema.yaml", "*.schema.json"):
        for path in _project_files(project, pattern):
            text = library.read_text(path)

            def schema_ref(match: re.Match[str], source: Path = path) -> str:
                target = (source.parent / match.group(2)).resolve()
                name = target.name.split(".schema.")[0]
                if target.parent not in copy_dirs or target.exists() or name not in global_names:
                    return match.group(0)
                return f"{match.group(1)}{library.LIBRARY_IDENTITY_PREFIX}types/{target.name}"

            new = _SCHEMA_REF.sub(schema_ref, text)
            if new != text:
                library.write_text(path, new)
                report.rewritten_type_pointers.append(path.relative_to(project))


# --- init --------------------------------------------------------------------------


def init_project(root: Path, name: str | None = None) -> InitReport:
    report = InitReport()

    if name is None:
        name = root.name

    replacements = {
        "<your-project>": name,
        "{{project_name}}": name,
        "/PATH/TO/COMMONPLACE/": str(root) + "/",
    }

    # Migrate what earlier releases left before scaffolding.
    library_root = library.library_root()
    _migrate_legacy_copies(root, library_root, report)
    _migrate_type_pointers(root, library_root, report)
    _retire_legacy_baselines(root, library_root, report)
    snapshots = migrate_snapshot_types(root / "kb")
    report.rewritten_snapshots += [p.relative_to(root) for p in snapshots.rewritten_snapshots]
    report.repinned_ingests += [p.relative_to(root) for p in snapshots.repinned_ingests]

    for rel_path in MANIFEST.directories:
        target = root / rel_path
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            report.created.append(rel_path)

    log_path = root / "kb" / "log.md"
    if not log_path.exists():
        log_path.write_text("", encoding="utf-8")
        report.created.append(Path("kb/log.md"))
    else:
        _record_existing(report, Path("kb/log.md"), log_path, b"")

    data_pkg = files("commonplace") / "_data"
    with as_file(data_pkg) as scaffold_root:
        for src_rel, target_rel in MANIFEST.trees:
            src_dir = _resolve_scaffold_source(scaffold_root, src_rel)
            _copy_tree_files(src_dir, root, target_rel, report)

        for src_rel, target_rel in MANIFEST.files:
            _copy_scaffold_file(scaffold_root, src_rel, root, target_rel, report)

        for src_rel, target_rel in MANIFEST.templates:
            src = _resolve_scaffold_source(scaffold_root, src_rel)
            target = root / target_rel
            _write_template(src, target, Path(target_rel), replacements, report)

    _write_stubs(root, library_root, report)
    _write_if_changed(root, library.ROUTING, library.render_routing(library_root), report)
    _write_read_rule(root, library_root, report)
    _write_gitignore(root, library_root, report)
    return report


def check_project(root: Path) -> list[library.OutputStatus]:
    """Init's outputs in a project and their state, without writing anything."""
    return library.statuses(root)


# --- installation diagnostics ---------------------------------------------------------


def _installed_command_names() -> tuple[str, ...]:
    """Return the Commonplace console scripts declared by this installation."""

    try:
        entry_points = distribution("llm-commonplace").entry_points
    except PackageNotFoundError:
        return ()
    return tuple(
        sorted(
            entry_point.name
            for entry_point in entry_points
            if entry_point.group == "console_scripts"
            and entry_point.name.startswith("commonplace-")
        )
    )


def _uv_tool_bin() -> Path | None:
    """Return uv's configured executable directory when uv can report it."""

    if shutil.which("uv") is None:
        return None
    result = subprocess.run(
        ["uv", "tool", "dir", "--bin"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return Path(result.stdout.strip())


def _same_directory(left: Path, right: Path) -> bool:
    return os.path.normcase(os.path.abspath(left)) == os.path.normcase(
        os.path.abspath(right)
    )


def installation_warnings() -> list[str]:
    """Return actionable warnings about the user-level command installation."""

    lines: list[str] = []
    if shutil.which("uv") is None:
        lines.append(
            "uv is not on PATH, so this process cannot verify or repair the "
            "canonical user-level Commonplace tool installation. Install uv, "
            "then install llm-commonplace with 'uv tool install'."
        )

    command_names = _installed_command_names()
    resolved = {name: shutil.which(name) for name in command_names}
    missing = [name for name, path in resolved.items() if path is None]
    if missing:
        lines.append(
            "Some commands from the installed llm-commonplace package are not "
            f"on PATH: {', '.join(missing)}."
        )
        lines.append(
            "Run 'uv tool install --python \">=3.11\" llm-commonplace', then "
            "'uv tool update-shell', and fully restart the shell, IDE, or agent "
            "runtime that must use the commands."
        )

    tool_bin = _uv_tool_bin()
    if tool_bin is not None:
        conflicting = [
            f"{name} ({path})"
            for name, path in resolved.items()
            if path is not None and not _same_directory(Path(path).parent, tool_bin)
        ]
        if conflicting:
            lines.append(
                "These commands resolve outside uv's tool executable directory "
                f"({tool_bin}): {', '.join(conflicting)}. Remove or reorder the "
                "shadowing PATH entry; do not use uv tool install --force as the "
                "default repair."
            )
    return lines


def _print_section(title: str, paths: list[Path]) -> None:
    if paths:
        print(title)
        for path in paths:
            print(f"- {path.as_posix()}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="project root to initialize")
    parser.add_argument(
        "--name",
        default=None,
        help="project name (default: directory name)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report whether the project's pointers into the library are current; write nothing",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()

    if args.check:
        problems = 0
        for item in check_project(root):
            print(f"{item.status}: {item.path.relative_to(root).as_posix()}")
            problems += item.status != "ok"
        return 1 if problems else 0

    warnings = installation_warnings()
    report = init_project(root, name=args.name)

    print(f"Initialized Commonplace project at {root}")
    _print_section("Created:", report.created)
    _print_section("Refreshed pointers into the installed library:", report.refreshed)
    _print_section("Removed library copies matching the installed library:", report.removed)
    _print_section(
        "Kept library copies that differ from the installed library "
        "(they may carry local changes; review and delete them):",
        report.migration_kept,
    )
    _print_section(
        "Skipped skill directories not written by commonplace-init "
        "(remove them to receive the library's skill):",
        report.skipped_foreign,
    )
    _print_section(
        "Rewrote type values in the form this release uses (paths under a KB root such as "
        "types/note.md; commonplace: schema refs):",
        report.rewritten_type_pointers,
    )
    _print_section(
        "Retyped local snapshots to `type: types/snapshot.md` (a one-time migration):",
        report.rewritten_snapshots,
    )
    _print_section(
        "Re-pinned analysis-result checksums to results whose type line changed (commit these):",
        report.repinned_result_checksums,
    )
    _print_section(
        "Re-pinned ingest checksums to the retyped snapshots (commit these):",
        report.repinned_ingests,
    )
    if report.retired_baselines:
        print("Retired review baselines recorded under the old library copy (history kept):")
        for item in report.retired_baselines:
            print(f"- {item}")
    if report.replaced_skill_copies:
        paths = " ".join(p.as_posix() for p in report.replaced_skill_copies)
        print(
            "These skill directories held copies from an earlier release and now hold stubs "
            "with paths specific to this machine. If your version control tracks them, untrack "
            f"them and commit; with git: git rm -r --cached {paths}"
        )
    _print_section("Preserved existing files already matching scaffold:", report.preserved_identical)
    _print_section(
        "Preserved existing files differing from current scaffold output:",
        report.preserved_different,
    )
    if not any(
        (
            report.created,
            report.refreshed,
            report.removed,
            report.migration_kept,
            report.skipped_foreign,
            report.retired_baselines,
            report.rewritten_type_pointers,
            report.rewritten_snapshots,
            report.preserved_identical,
            report.preserved_different,
        )
    ):
        print("No changes needed.")

    if warnings:
        print("\nCommand installation diagnostics:")
        for line in warnings:
            print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
