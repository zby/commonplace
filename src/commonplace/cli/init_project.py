"""Initialize a local Commonplace project tree."""

from __future__ import annotations

import argparse
import os
import shutil
from dataclasses import dataclass, field
from importlib.resources import as_file, files
from pathlib import Path


DEFAULT_DIRS = [
    Path("kb/types"),
    Path("kb/notes"),
    Path("kb/notes/types"),
    Path("kb/reference"),
    Path("kb/reference/types"),
    Path("kb/sources"),
    Path("kb/sources/types"),
    Path("kb/tasks/backlog"),
    Path("kb/tasks/active"),
    Path("kb/tasks/completed"),
    Path("kb/work"),
    Path("kb/instructions"),
    Path("kb/reports"),
    Path("kb/reports/connect"),
    Path("kb/reports/types"),
]

# Scaffold paths to copy, relative to the scaffold package.
# Each entry is (scaffold_relative_path, target_relative_path).
SCAFFOLD_TREES = [
    ("kb/instructions", "kb/instructions"),
    ("kb/notes", "kb/notes"),
    ("kb/reference", "kb/reference"),
    ("kb/reports/types", "kb/reports/types"),
    ("kb/sources/types", "kb/sources/types"),
    ("kb/types", "kb/types"),
]

# Individual scaffold files to copy. Used when only one file from a tree is
# scaffolded (avoiding a full tree walk that would copy unrelated content).
SCAFFOLD_FILES = [
    ("kb/reports/collection-topology.md", "kb/reports/collection-topology.md"),
]

# Skills directories for supported runtimes.
SKILLS_DIRS = [
    Path(".claude/skills"),
    Path(".agents/skills"),
]

PROMOTED_SKILLS = [
    "cp-skill-compile-collections",
    "cp-skill-write",
    "cp-skill-validate",
    "cp-skill-connect",
    "cp-skill-convert",
    "cp-skill-ingest",
    "cp-skill-snapshot-web",
    "cp-skill-revise-iterative",
    "cp-skill-revise-autoreason",
]


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


def _copy_scaffold_tree(
    scaffold_root: Path,
    src_rel: str,
    dest_root: Path,
    target_rel: str,
    report: InitReport,
) -> None:
    """Recursively copy a scaffold subtree, classifying existing files."""
    src_dir = scaffold_root / src_rel
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
    src = scaffold_root / src_rel
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
    for rel_path in DEFAULT_DIRS:
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
        for src_rel, target_rel in SCAFFOLD_TREES:
            _copy_scaffold_tree(scaffold_root, src_rel, root, target_rel, report)

        for src_rel, target_rel in SCAFFOLD_FILES:
            _copy_scaffold_file(scaffold_root, src_rel, root, target_rel, report)

        # Resolve templates with project-specific values.
        templates = [
            ("AGENTS.md.template", "AGENTS.md.template"),
            (".envrc.template", ".envrc"),
        ]
        for src_rel, target_rel in templates:
            src = scaffold_root / src_rel
            target = root / target_rel
            _write_template(src, target, Path(target_rel), replacements, report)

        # Generate qmd config from the assets template.
        assets_pkg = files("commonplace.assets")
        with as_file(assets_pkg) as assets_root:
            qmd_src = assets_root / "qmd-collections.yml"
            qmd_target = root / "qmd-collections.yml"
            _write_template(
                qmd_src,
                qmd_target,
                Path("qmd-collections.yml"),
                replacements,
                report,
            )

    # Promote selected instruction directories into runtime skills directories
    # via symlinks. The source is the local kb/instructions/<name> directory
    # (already scaffolded above), not the scaffold package.
    for skill_name in PROMOTED_SKILLS:
        skill_src = root / "kb" / "instructions" / skill_name
        if not skill_src.is_dir():
            raise FileNotFoundError(
                f"Promoted skill source is missing: kb/instructions/{skill_name}"
            )
        for skills_dest in SKILLS_DIRS:
            link = root / skills_dest / skill_name
            link.parent.mkdir(parents=True, exist_ok=True)
            # Compute relative path from the link's parent to the source.
            target = Path(os.path.relpath(skill_src, link.parent))
            if link.is_symlink():
                if link.resolve() == skill_src.resolve():
                    report.preserved_identical.append(skills_dest / skill_name)
                    continue
                link.unlink()
            elif link.is_dir():
                # Replace old copied directory with a symlink.
                shutil.rmtree(link)
            link.symlink_to(target)
            report.created.append(skills_dest / skill_name)

    return report


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
    report = init_project(root, name=args.name)

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
