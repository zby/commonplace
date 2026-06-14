"""Initialize a local Commonplace project tree."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import dataclass, field
from importlib.resources import as_file, files
from pathlib import Path

from commonplace.scaffold_manifest import MANIFEST


@dataclass
class InitReport:
    created: list[Path] = field(default_factory=list)
    preserved_identical: list[Path] = field(default_factory=list)
    preserved_different: list[Path] = field(default_factory=list)
    skipped: list[tuple[Path, str]] = field(default_factory=list)


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


def _copy_scaffold_tree(
    scaffold_root: Path,
    src_rel: str,
    dest_root: Path,
    target_rel: str,
    report: InitReport,
) -> None:
    """Recursively copy a scaffold subtree, classifying existing files."""
    src_dir = _resolve_scaffold_source(scaffold_root, src_rel)
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


def _create_junction(target: Path, link: Path) -> bool:
    """Create a Windows directory junction at ``link`` pointing to ``target``.

    Junctions need neither admin rights nor Developer Mode, unlike real symlinks.
    Uses the stdlib ``_winapi.CreateJunction`` (Windows-only, undocumented but
    stable). Returns ``True`` on success, ``False`` if the call is unavailable
    or fails. The target is resolved to an absolute path, as junctions require.

    ``CreateJunction`` creates the ``link`` directory itself (via
    ``CreateDirectoryW``) and then sets its reparse point, so ``link`` must not
    already exist — the caller guarantees this by only falling back here after
    the ``symlink_to`` attempt on an absent path.
    """
    try:
        import _winapi

        _winapi.CreateJunction(str(target.resolve()), str(link))
    except (OSError, AttributeError, ImportError):
        return False
    return True


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
    # via symlinks. The source is the local kb/commonplace/instructions/<name>
    # directory (scaffolded above from the shipped library), not the scaffold
    # package itself.
    for skill_name in MANIFEST.promoted_skills:
        skill_src = root / "kb" / "commonplace" / "instructions" / skill_name
        if not skill_src.is_dir():
            raise FileNotFoundError(
                f"Promoted skill source is missing: kb/commonplace/instructions/{skill_name}"
            )
        for skills_dest in MANIFEST.skills_dirs:
            link = root / skills_dest / skill_name
            link.parent.mkdir(parents=True, exist_ok=True)
            # Compute relative path from the link's parent to the source.
            target = Path(os.path.relpath(skill_src, link.parent))
            if link.is_symlink():
                if link.resolve() == skill_src.resolve():
                    report.preserved_identical.append(skills_dest / skill_name)
                    continue
                link.unlink()
            elif link.exists():
                # A real directory or file may be an intentional runtime-specific
                # skill projection on platforms that cannot follow symlinks.
                report.preserved_different.append(skills_dest / skill_name)
                continue
            try:
                link.symlink_to(target, target_is_directory=True)
            except OSError as exc:
                # On Windows, real symlinks need admin rights or Developer Mode.
                # A directory junction needs neither and is followed transparently
                # by tools reading the directory, so fall back to one. Junctions
                # require an absolute target on the same local volume, so they do
                # not survive a project move the way the relative symlink does.
                # `_create_junction` returns False off Windows (no `_winapi`), so
                # this path is a no-op there and the projection stays skipped.
                if _create_junction(skill_src, link):
                    report.created.append(skills_dest / skill_name)
                    continue
                report.skipped.append((skills_dest / skill_name, str(exc)))
                continue
            report.created.append(skills_dest / skill_name)

    return report


def direnv_warnings(root: Path) -> list[str]:
    """Return setup-warning lines about loading the project command environment.

    `commonplace-init` writes a `.envrc` but does not install direnv or run
    `direnv allow`. Without those manual steps the `.envrc` is a silent no-op:
    `.venv/bin` never lands on PATH and `commonplace-*` commands do not resolve
    by bare name. Surface the gap at init time instead of letting the user
    discover it as a "command not found" later. Returns an empty list when
    nothing actionable is detected.
    """
    lines: list[str] = []
    if sys.platform == "win32":
        lines.append(
            "Windows detected. The generated .envrc is for Unix-like shells; "
            "activate the project venv before running commonplace-* commands "
            "or starting an agent runtime."
        )
        lines.append(
            "PowerShell: run '.\\.venv\\Scripts\\Activate.ps1'. cmd: run "
            "'.venv\\Scripts\\activate.bat'."
        )
        lines.append(
            "Skill projection uses a directory junction on Windows (no admin "
            "rights or Developer Mode needed). If even that is skipped (network "
            "volume, sandboxed filesystem), install the cp-skill-* directories "
            "into your agent runtime's skill surface manually."
        )
        lines.append(
            "See INSTALL.md step 2 (Install the library and make the commands "
            "work) for examples."
        )
        return lines

    if shutil.which("direnv") is None:
        lines.append(
            "direnv is not installed. The generated .envrc puts .venv/bin on "
            "PATH so commonplace-* commands run by bare name, but it stays a "
            "no-op until the environment is activated."
        )
        lines.append(
            "Recommended: install direnv, add its shell hook, then run "
            "'direnv allow' in this directory."
        )
        lines.append(
            "Without direnv: add 'export PATH=\".venv/bin:$PATH\"' to your "
            "shell rc instead."
        )
    else:
        lines.append(
            "direnv is installed. Run 'direnv allow' in this directory so the "
            "generated .envrc activates and .venv/bin lands on PATH; install "
            "the direnv shell hook first if you have not already."
        )
    lines.append("See INSTALL.md (Appendix: direnv) for examples.")
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
    pre_init_warnings: list[str] = []
    if sys.platform == "win32":
        pre_init_warnings = direnv_warnings(root)
        if pre_init_warnings:
            print("Environment setup:")
            for line in pre_init_warnings:
                print(f"- {line}")
            print()

    try:
        report = init_project(root, name=args.name)
    except OSError as exc:
        if sys.platform == "win32":
            print(f"Failed to initialize Commonplace project at {root}: {exc}")
            if not pre_init_warnings:
                print("\nEnvironment setup:")
                for line in direnv_warnings(root):
                    print(f"- {line}")
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
    if report.skipped:
        print("Skipped optional runtime skill projections:")
        for path, reason in report.skipped:
            print(f"- {path.as_posix()}: {reason}")
        print(
            "Install the matching kb/commonplace/instructions/cp-skill-* directories "
            "through your agent runtime's own skill mechanism if needed."
        )
    if (
        not report.created
        and not report.preserved_identical
        and not report.preserved_different
        and not report.skipped
    ):
        print("No changes needed.")

    warnings = [] if pre_init_warnings else direnv_warnings(root)
    if warnings:
        print("\nEnvironment setup:")
        for line in warnings:
            print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
