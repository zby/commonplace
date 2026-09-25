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
    checkout. The library itself is not scaffolded: projects read it from the
    installed package (see `commonplace.lib.library`).
    """

    directories: tuple[Path, ...]
    trees: tuple[tuple[str, str], ...]
    files: tuple[tuple[str, str], ...]
    templates: tuple[tuple[str, str], ...]
    skills_dirs: tuple[Path, ...]
    promoted_skills: tuple[str, ...]
    router_skill: str
    legacy_copies: tuple[tuple[str, str], ...]


MANIFEST = ScaffoldManifest(
    directories=(
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
    # The project's own report and source collections receive their type
    # contracts. The library stays in the installed package.
    trees=(
        ("kb/reports/types", "kb/reports/types"),
        ("kb/sources/types", "kb/sources/types"),
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
        ("templates/CLAUDE.md.template", "CLAUDE.md.template"),
    ),
    # Skill directories for supported runtimes; init writes a stub per skill
    # into each, redirecting to the real skill in the installed library.
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
    # Indexes the library's instructions by name; receives a stub like the others.
    router_skill="cp-skill-library",
    # Where earlier releases copied the library into a project, and the library
    # path each copy came from. Migration removes copies that match the library.
    legacy_copies=(
        ("kb/commonplace/instructions", "instructions"),
        ("kb/commonplace/notes", "notes"),
        ("kb/commonplace/reference", "reference"),
        ("kb/types", "types"),
    ),
)
