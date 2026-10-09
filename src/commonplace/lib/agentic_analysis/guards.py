"""Where an analysis publishes, and the guards that protect it."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis.sets import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    current_analyses,
    is_review_path,
)
from commonplace.lib.source_identity import normalize_source_identity
from commonplace.setrun import effects
from commonplace.setrun.isolation import require_clean_worktree, source_checkout

# A sibling run's publication may remain uncommitted while a batch runs.
OUTPUT_LOCATIONS: tuple[str, ...] = (f"{RETAINED_ROOT.as_posix()}/", f"{ARCHIVE_ROOT.as_posix()}/")
LOCK = Path("kb/agentic-system-analyses/state/.publication.lock")


def checkout(run_dir: Path) -> Path:
    """The Commonplace source checkout an analysis run belongs to; analyses run only there."""
    repo = source_checkout(run_dir)
    if repo is None:
        raise ValueError("analysis jobs must run inside their analysis checkout")
    return repo


def _destination_path(repo_root: Path, raw: str) -> Path:
    if not is_review_path(raw):
        raise ValueError(
            "publication destination must be kb/agentic-system-analyses/retained/<slug>/overview.md: "
            f"{raw}"
        )
    path = repo_root / raw
    if path.is_symlink() or path.resolve() != path:
        raise ValueError("publication destination must not traverse symlinks")
    return path


def require_publishable_worktree(repo_root: Path) -> None:
    """A clean worktree outside the retained and archive locations."""
    require_clean_worktree(repo_root, OUTPUT_LOCATIONS)


@contextmanager
def publication_lock(repo_root: Path) -> Iterator[None]:
    """The repository's analysis publication lock; take any run lock first."""
    with effects.publication_lock(repo_root.resolve() / LOCK):
        yield


def inspect_destination(
    *, repo_root: Path, generated_destination: str, source_identity: str,
) -> dict[str, object]:
    """Return only a replacement decision and byte identity, never prior prose."""
    repo_root = repo_root.resolve()
    path = _destination_path(repo_root, generated_destination)
    require_publishable_worktree(repo_root)
    source_identity = normalize_source_identity(source_identity)
    # Validate every current set before choosing a replacement.
    for member_set in current_analyses(repo_root):
        if member_set.overview.path != path:
            continue
        if member_set.memory.frontmatter["source-identity"] != source_identity:
            raise ValueError("publication destination belongs to another source")
        return {
            "exists": True,
            "expected_incumbent_sha256": sha256(member_set.overview.content).hexdigest(),
        }
    return {"exists": False, "expected_incumbent_sha256": "absent"}
