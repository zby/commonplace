"""Virtual critique assay identity and installed/source path resolution."""

from __future__ import annotations

from pathlib import Path


CRITIQUE_LENS = "critique"
SOURCE_CRITIQUE_PATH = Path("kb/instructions/critique-note.md")
INSTALLED_CRITIQUE_PATH = Path("kb/commonplace/instructions/critique-note.md")


def is_critique_request(value: str) -> bool:
    return value.strip() == CRITIQUE_LENS


def critique_criterion_path(repo_root: Path) -> str:
    installed = repo_root / INSTALLED_CRITIQUE_PATH
    source = repo_root / SOURCE_CRITIQUE_PATH
    path = installed if installed.is_file() else source
    if not path.is_file():
        raise FileNotFoundError(f"critique instruction not found: {path.relative_to(repo_root)}")
    return path.relative_to(repo_root).as_posix()


def is_critique_criterion_path(path: str) -> bool:
    normalized = Path(path).as_posix()
    return normalized in {
        SOURCE_CRITIQUE_PATH.as_posix(),
        INSTALLED_CRITIQUE_PATH.as_posix(),
    }


def result_kind_for_criterion_path(path: str) -> str:
    return "report" if is_critique_criterion_path(path) else "verdict"
