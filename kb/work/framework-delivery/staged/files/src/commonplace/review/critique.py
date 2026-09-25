"""Virtual critique assay identity; the critique instruction lives in the library."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_identity,
    is_library_identity,
    library_root,
)

CRITIQUE_LENS = "critique"
CRITIQUE_REL = "instructions/critique-note.md"


def is_critique_request(value: str) -> bool:
    return value.strip() == CRITIQUE_LENS


def critique_criterion_path(repo_root: Path) -> str:
    """Identity of the critique instruction, read from the installed library."""
    path = library_root() / CRITIQUE_REL
    if not path.is_file():
        raise FileNotFoundError(f"critique instruction not found: {path}")
    return artifact_identity(repo_root, path)


def is_critique_criterion_path(path: str) -> bool:
    normalized = Path(path).as_posix() if not is_library_identity(path) else path
    return normalized in {f"kb/{CRITIQUE_REL}", LIBRARY_IDENTITY_PREFIX + CRITIQUE_REL}


def result_kind_for_criterion_path(path: str) -> str:
    return "report" if is_critique_criterion_path(path) else "verdict"
