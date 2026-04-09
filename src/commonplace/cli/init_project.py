"""Initialize a local Commonplace project tree."""

from __future__ import annotations

import argparse
import shutil
from importlib.resources import as_file, files
from pathlib import Path


DEFAULT_DIRS = [
    Path("kb/notes"),
    Path("kb/notes/types"),
    Path("kb/sources"),
    Path("kb/sources/types"),
    Path("kb/tasks/backlog"),
    Path("kb/tasks/active"),
    Path("kb/tasks/completed"),
    Path("kb/work"),
    Path("kb/instructions"),
    Path("kb/reports"),
    Path("types"),
]

# Scaffold paths to copy, relative to the scaffold package.
# Each entry is (scaffold_relative_path, target_relative_path).
SCAFFOLD_TREES = [
    ("kb/instructions", "kb/instructions"),
    ("types", "types"),
]

# Skills directories for supported runtimes.
SKILLS_DIRS = [
    Path(".claude/skills"),
    Path(".agents/skills"),
]

PROMOTED_SKILLS = [
    "write",
    "validate",
    "connect",
    "convert",
    "ingest",
    "snapshot-web",
    "revise-iterative",
]

SKILL_PREFIX = "commonplace-"


def _copy_scaffold_tree(
    scaffold_root: Path, src_rel: str, dest_root: Path, target_rel: str
) -> list[Path]:
    """Recursively copy a scaffold subtree, skipping existing files."""
    copied: list[Path] = []
    src_dir = scaffold_root / src_rel
    dest_dir = dest_root / target_rel
    for src_file in sorted(src_dir.rglob("*")):
        if not src_file.is_file():
            continue
        rel = src_file.relative_to(src_dir)
        target = dest_dir / rel
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, target)
        copied.append(Path(target_rel) / rel)
    return copied


def _write_template(
    src: Path, target: Path, replacements: dict[str, str]
) -> bool:
    """Read a template, apply replacements, write to target. Skip if target exists."""
    if target.exists():
        return False
    text = src.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return True


def init_project(root: Path, name: str | None = None) -> list[Path]:
    created: list[Path] = []

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
            created.append(rel_path)

    # Create starter log file.
    log_path = root / "kb" / "log.md"
    if not log_path.exists():
        log_path.write_text("", encoding="utf-8")
        created.append(Path("kb/log.md"))

    # Copy scaffold files from the installed package.
    scaffold_pkg = files("commonplace.scaffold")
    with as_file(scaffold_pkg) as scaffold_root:
        for src_rel, target_rel in SCAFFOLD_TREES:
            copied = _copy_scaffold_tree(scaffold_root, src_rel, root, target_rel)
            created.extend(copied)

        # Resolve templates with project-specific values.
        templates = [
            ("AGENTS.md.template", "AGENTS.md.template"),
            (".envrc.template", ".envrc"),
        ]
        for src_rel, target_rel in templates:
            src = scaffold_root / src_rel
            target = root / target_rel
            if _write_template(src, target, replacements):
                created.append(Path(target_rel))

        # Generate qmd config from the assets template.
        assets_pkg = files("commonplace.assets")
        with as_file(assets_pkg) as assets_root:
            qmd_src = assets_root / "qmd-collections.yml"
            qmd_target = root / "qmd-collections.yml"
            if _write_template(qmd_src, qmd_target, replacements):
                created.append(Path("qmd-collections.yml"))

        # Promote selected instruction directories into runtime skills directories.
        for skill_name in PROMOTED_SKILLS:
            skill_src_rel = f"kb/instructions/{skill_name}"
            if not (scaffold_root / skill_src_rel).is_dir():
                raise FileNotFoundError(
                    f"Promoted skill source is missing from scaffold: {skill_src_rel}"
                )
            prefixed_name = SKILL_PREFIX + skill_name
            for skills_dest in SKILLS_DIRS:
                target_rel = str(skills_dest / prefixed_name)
                copied = _copy_scaffold_tree(
                    scaffold_root,
                    skill_src_rel,
                    root,
                    target_rel,
                )
                created.extend(copied)

    return created


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
    created = init_project(root, name=args.name)

    print(f"Initialized Commonplace project at {root}")
    if created:
        print("Created:")
        for path in created:
            print(f"- {path.as_posix()}")
    else:
        print("No changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
