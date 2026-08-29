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
        # User-space operating directories; collection files are seeded below.
        Path("kb/sources"),
        Path("kb/sources/types"),
        Path("kb/tasks/backlog"),
        Path("kb/tasks/active"),
        Path("kb/tasks/completed"),
        Path("kb/work"),
        Path("kb/reports"),
        Path("kb/reports/cache"),
        Path("kb/reports/cache/connect"),
        Path("kb/reports/state"),
        Path("kb/reports/retained"),
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
    # Single files copied without a tree walk. User-collection contract,
    # landing, and local-policy templates seed empty collections.
    files=(
        ("kb/sources/.gitignore", "kb/sources/.gitignore"),
        ("templates/user-sources-COLLECTION.md", "kb/sources/COLLECTION.md"),
        ("templates/user-sources-README.md", "kb/sources/README.md"),
        ("templates/user-notes-COLLECTION.md", "kb/notes/COLLECTION.md"),
        ("templates/user-notes-README.md", "kb/notes/README.md"),
        ("templates/user-reference-COLLECTION.md", "kb/reference/COLLECTION.md"),
        ("templates/user-reference-README.md", "kb/reference/README.md"),
        ("templates/user-instructions-COLLECTION.md", "kb/instructions/COLLECTION.md"),
        ("templates/user-instructions-README.md", "kb/instructions/README.md"),
        ("templates/user-reports-COLLECTION.md", "kb/reports/COLLECTION.md"),
        ("templates/user-reports-README.md", "kb/reports/README.md"),
        ("templates/user-reports-cache-README.md", "kb/reports/cache/README.md"),
        ("templates/user-reports-state-README.md", "kb/reports/state/README.md"),
        ("templates/user-reports-retained-README.md", "kb/reports/retained/README.md"),
        ("templates/user-reports-gitignore", "kb/reports/.gitignore"),
        (
            "templates/user-reports-cache-validation-ignore",
            "kb/reports/cache/.commonplace-validation-ignore",
        ),
        (
            "templates/user-reports-state-validation-ignore",
            "kb/reports/state/.commonplace-validation-ignore",
        ),
    ),
    # Resolved with project-specific replacements at install time.
    templates=(
        ("AGENTS.md.template", "AGENTS.md.template"),
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
        "cp-skill-write-multistage",
        "cp-skill-ground",
    ),
)
