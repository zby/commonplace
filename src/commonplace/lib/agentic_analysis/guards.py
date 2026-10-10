"""Where an analysis publishes, and the guards that protect it."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path

from commonplace.artifactrun import effects
from commonplace.artifactrun.worktree import (
    require_clean_worktree,
    require_run_code,
    require_running_package_unchanged,
    run_command,
    source_checkout,
)
from commonplace.lib.agentic_analysis.analyses import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    current_analyses,
    is_review_path,
)
from commonplace.lib.agentic_analysis.worktree import STATE_ROOT
from commonplace.lib.source_identity import normalize_source_identity

# A sibling run's publication may remain uncommitted while a batch runs.
OUTPUT_LOCATIONS: tuple[str, ...] = (f"{RETAINED_ROOT.as_posix()}/", f"{ARCHIVE_ROOT.as_posix()}/")
LOCK = Path("kb/agentic-system-analyses/state/.publication.lock")


def checkout(run_dir: Path) -> Path:
    """The Commonplace source checkout an analysis run belongs to; analyses run only there."""
    repo = source_checkout(run_dir)
    if repo is None:
        raise ValueError("analysis jobs must run inside their analysis checkout")
    return repo


def run_checkout(run_dir: Path, library: Path, *, job: str) -> Path:
    """The analysis checkout a run belongs to, after the location, library and running-code guards."""
    repo = source_checkout(run_dir)
    if repo is None or run_dir.parent != repo / STATE_ROOT:
        raise ValueError(f"{job}: an analysis run must be directly under its checkout's {STATE_ROOT}")
    if library != repo / "kb":
        raise ValueError(f"{job}: the run's recorded library must be the analysis worktree's kb directory")
    require_run_code(run_dir, cwd=Path.cwd())
    return repo


def require_prepared_method(repo: Path, commit: str, preparation: dict, *, job: str) -> None:
    """The worktree is at its preparation commit, clean, and runs that commit's package."""
    if run_command(["git", "rev-parse", "HEAD"], cwd=repo) != commit or preparation.get("commit") != commit:
        raise ValueError(f"{job}: analysis worktree HEAD differs from its preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)


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
    # Validate every current artifact before choosing a replacement.
    for analysis in current_analyses(repo_root):
        if analysis.overview.path != path:
            continue
        if analysis.memory.frontmatter["source-identity"] != source_identity:
            raise ValueError("publication destination belongs to another source")
        return {
            "exists": True,
            "expected_incumbent_sha256": sha256(analysis.overview.content).hexdigest(),
        }
    return {"exists": False, "expected_incumbent_sha256": "absent"}
