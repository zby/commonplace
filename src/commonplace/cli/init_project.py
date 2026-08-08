"""Initialize a local Commonplace project tree."""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, distribution
from importlib.resources import as_file, files
from pathlib import Path

from commonplace.scaffold_manifest import MANIFEST


LEGACY_GENERATED_ENVRC = (
    b'export PATH="$PWD/.venv/bin:$PATH"\n'
    b'export UV_CACHE_DIR="$PWD/.uv-cache"\n'
)


@dataclass
class InitReport:
    created: list[Path] = field(default_factory=list)
    preserved_identical: list[Path] = field(default_factory=list)
    preserved_different: list[Path] = field(default_factory=list)


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


def _copy_scaffold_tree(
    scaffold_root: Path,
    src_rel: str,
    dest_root: Path,
    target_rel: str,
    report: InitReport,
) -> None:
    """Recursively copy a scaffold subtree, classifying existing files."""
    src_dir = _resolve_scaffold_source(scaffold_root, src_rel)
    _copy_tree_files(src_dir, dest_root, target_rel, report)


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

    Wheels include canonical repo files under `commonplace/_data/` through
    Hatch force-includes. Editable source checkouts do not duplicate those
    files under `_data`; they read the canonical repo paths directly.
    """
    packaged = scaffold_root / src_rel
    if packaged.exists():
        return packaged

    source_root = Path(__file__).resolve().parents[3]
    source = source_root / src_rel
    if source.exists():
        return source

    raise FileNotFoundError(f"Scaffold source is missing: {src_rel}")


def _is_filesystem_link(path: Path) -> bool:
    """True for a symlink or a Windows reparse point (junction).

    Earlier versions projected skills as symlinks with a junction fallback;
    re-init replaces those with real copies. ``Path.is_junction`` only exists
    on Python 3.12+, so junctions are detected through ``st_file_attributes``
    (present only on Windows stat results).
    """
    if path.is_symlink():
        return True
    try:
        attributes = os.lstat(path).st_file_attributes  # type: ignore[attr-defined]
    except (OSError, AttributeError):
        return False
    return bool(attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def _remove_filesystem_link(path: Path) -> None:
    """Remove a symlink or junction without touching its target's contents."""
    try:
        path.unlink()
    except OSError:
        # On Windows, directory symlinks and junctions are removed with rmdir.
        os.rmdir(path)


def init_project(root: Path, name: str | None = None) -> InitReport:
    report = InitReport()

    if name is None:
        name = root.name

    replacements = {
        "<your-project>": name,
        "{{project_name}}": name,
        "/PATH/TO/COMMONPLACE/": str(root) + "/",
    }

    # Create directory structure.
    for rel_path in MANIFEST.directories:
        target = root / rel_path
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            report.created.append(rel_path)

    # Create starter log file.
    log_path = root / "kb" / "log.md"
    if not log_path.exists():
        log_path.write_text("", encoding="utf-8")
        report.created.append(Path("kb/log.md"))
    else:
        _record_existing(report, Path("kb/log.md"), log_path, b"")

    # Copy scaffold files from the installed package data.
    data_pkg = files("commonplace") / "_data"
    with as_file(data_pkg) as scaffold_root:
        for src_rel, target_rel in MANIFEST.trees:
            _copy_scaffold_tree(scaffold_root, src_rel, root, target_rel, report)

        for src_rel, target_rel in MANIFEST.files:
            _copy_scaffold_file(scaffold_root, src_rel, root, target_rel, report)

        # Resolve templates with project-specific values.
        for src_rel, target_rel in MANIFEST.templates:
            src = _resolve_scaffold_source(scaffold_root, src_rel)
            target = root / target_rel
            _write_template(src, target, Path(target_rel), replacements, report)

    # Promote selected instruction directories into runtime skills directories
    # by copying. The source is the local kb/commonplace/instructions/<name>
    # directory (scaffolded above from the shipped library), not the scaffold
    # package itself. Copies work on every platform; the symlinks (and Windows
    # junction fallback) earlier versions used kept breaking on Windows, so a
    # legacy link found at the destination is replaced with a real copy.
    for skill_name in MANIFEST.promoted_skills:
        skill_src = root / "kb" / "commonplace" / "instructions" / skill_name
        if not skill_src.is_dir():
            raise FileNotFoundError(
                f"Promoted skill source is missing: kb/commonplace/instructions/{skill_name}"
            )
        for skills_dest in MANIFEST.skills_dirs:
            target = root / skills_dest / skill_name
            if _is_filesystem_link(target):
                _remove_filesystem_link(target)
            _copy_tree_files(skill_src, root, skills_dest / skill_name, report)

    return report


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


def installation_warnings(root: Path) -> list[str]:
    """Return actionable warnings about the user-level command installation."""

    lines: list[str] = []
    envrc = root / ".envrc"
    if envrc.is_file():
        content = envrc.read_bytes()
        if content.replace(b"\r\n", b"\n") == LEGACY_GENERATED_ENVRC:
            lines.append(
                "This project still has the exact .envrc generated by an older "
                "Commonplace release. It is no longer required; review and remove "
                "it after confirming the uv-tool commands work in fresh processes."
            )
        elif b".venv/bin" in content or b".venv\\Scripts" in content:
            lines.append(
                "This project has an edited .envrc that adds a project venv to "
                "PATH. It may shadow the user-level Commonplace tool; review it "
                "manually because commonplace-init will not alter edited files."
            )

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
            "Run 'uv tool install --python \"\u003e=3.11\" llm-commonplace', then "
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="project root to initialize")
    parser.add_argument(
        "--name",
        default=None,
        help="project name (default: directory name)",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    warnings = installation_warnings(root)

    try:
        report = init_project(root, name=args.name)
    except OSError as exc:
        if sys.platform == "win32":
            print(f"Failed to initialize Commonplace project at {root}: {exc}")
            return 1
        raise

    print(f"Initialized Commonplace project at {root}")
    if report.created:
        print("Created:")
        for path in report.created:
            print(f"- {path.as_posix()}")
    if report.preserved_identical:
        print("Preserved existing files already matching scaffold:")
        for path in report.preserved_identical:
            print(f"- {path.as_posix()}")
    if report.preserved_different:
        print("Preserved existing files differing from current scaffold output:")
        for path in report.preserved_different:
            print(f"- {path.as_posix()}")
    if (
        not report.created
        and not report.preserved_identical
        and not report.preserved_different
    ):
        print("No changes needed.")

    if warnings:
        print("\nCommand installation diagnostics:")
        for line in warnings:
            print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
