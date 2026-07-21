"""What commonplace-init installs: the scaffold manifest as data.

`commonplace.cli.init_project` executes this manifest. Changing what ships —
directories, scaffold trees, templates, promoted skills — is an edit here,
not in installer code.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ScaffoldManifest:
    """One Commonplace project scaffold.

    Tree/file/template entries are (scaffold_relative_path, target_relative_path)
    pairs; sources resolve from packaged `commonplace/_data/` or a source
    checkout.
    """

    directories: tuple[Path, ...]
    trees: tuple[tuple[str, str], ...]
    files: tuple[tuple[str, str], ...]
    templates: tuple[tuple[str, str], ...]
    skills_dirs: tuple[Path, ...]
    promoted_skills: tuple[str, ...]


MANIFEST = ScaffoldManifest(
    directories=(
        # Shared top-level (types are shared between library and user).
        Path("kb/types"),
        # User collections — start empty; user adds their own content.
        Path("kb/notes"),
        Path("kb/notes/types"),
        Path("kb/reference"),
        Path("kb/reference/types"),
        Path("kb/instructions"),
        # User-space directories — no shipped content.
        Path("kb/sources"),
        Path("kb/sources/types"),
        Path("kb/tasks/backlog"),
        Path("kb/tasks/active"),
        Path("kb/tasks/completed"),
        Path("kb/work"),
        Path("kb/reports"),
        Path("kb/reports/connect"),
        Path("kb/reports/types"),
    ),
    # Shipped library content lands under kb/commonplace/ (ADR-021). Shared
    # types stay at top-level kb/types/. User-space type scaffolds (sources,
    # reports) land in their conventional locations under the user's tree.
    trees=(
        ("kb/instructions", "kb/commonplace/instructions"),
        ("kb/notes", "kb/commonplace/notes"),
        ("kb/reference", "kb/commonplace/reference"),
        ("kb/reports/types", "kb/reports/types"),
        ("kb/sources/types", "kb/sources/types"),
        ("kb/types", "kb/types"),
    ),
    # Single files copied without a tree walk. User-collection COLLECTION.md
    # templates land in the user's empty collections so write skills have a
    # starting register/convention stub to fill in.
    files=(
        ("templates/user-notes-COLLECTION.md", "kb/notes/COLLECTION.md"),
        ("templates/user-reference-COLLECTION.md", "kb/reference/COLLECTION.md"),
        ("templates/user-instructions-COLLECTION.md", "kb/instructions/COLLECTION.md"),
    ),
    # Resolved with project-specific replacements at install time.
    templates=(
        ("AGENTS.md.template", "AGENTS.md.template"),
        (".envrc.template", ".envrc"),
    ),
    # Skill directories for supported runtimes; promoted skills are copied
    # into each from kb/commonplace/instructions/<name>.
    skills_dirs=(
        Path(".claude/skills"),
        Path(".agents/skills"),
    ),
    promoted_skills=(
        "cp-skill-write",
        "cp-skill-validate",
        "cp-skill-connect",
        "cp-skill-convert",
        "cp-skill-health-check",
        "cp-skill-ingest",
        "cp-skill-snapshot-web",
        "cp-skill-revise-autoreason",
    ),
)
