"""Freeze the Git checkout an agentic-system analysis reads.

A GitHub source is read from `related-systems/<owner>--<repo>/`, detached at
one full commit with no local changes. Code acquires that checkout before the
boundary job runs, so no worker clones, fetches or checks out anything.

A missing checkout is cloned into a temporary sibling and renamed into place
only once it is detached at the commit, so an interrupted acquisition leaves
no partial checkout behind. An existing clean checkout is moved to the
commit; it is never cleaned: local changes, a foreign origin, or a commit the
origin does not have stop the run for the operator.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from commonplace.lib.agentic_analysis.sets import normalize_source_identity

CHECKOUT_ROOT = "related-systems"
GITHUB_REPOSITORY = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
SSH_GITHUB = re.compile(r"git@github\.com:(.+)")


class CheckoutError(ValueError):
    """The requested source checkout cannot be acquired safely."""


def github_checkout_path(identity: str) -> Path | None:
    """The checkout of a GitHub repository identity, relative to the
    repository root, or None when the identity names no GitHub repository."""
    match = GITHUB_REPOSITORY.fullmatch(normalize_source_identity(identity))
    if match is None:
        return None
    return Path(CHECKOUT_ROOT) / f"{match[1]}--{match[2]}"


def canonical_origin(url: str) -> str:
    """One form for the HTTPS and SSH spellings of a remote."""
    ssh = SSH_GITHUB.fullmatch(url.strip())
    return normalize_source_identity(f"https://github.com/{ssh[1]}" if ssh else url)


def git(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(path), *args], capture_output=True, text=True, check=False
    )


def output(path: Path, *args: str) -> str:
    """The output of a Git command that must succeed."""
    result = git(path, *args)
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed in {path}: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def freeze_checkout(
    repo_root: Path, checkout: Path, *, identity: str, origin: str,
    revision: str | None = None,
) -> dict[str, Any]:
    """Freeze `checkout` (relative to `repo_root`) and return the boundary's
    `source` record for it.

    The commit is `revision`, or else the tip of `origin`'s default branch. A
    missing checkout is cloned from `origin`; a clean existing one is fetched
    when it lacks the commit. Either is detached at the commit, except that a
    checkout already there is left as it is.
    """
    path = repo_root / checkout
    if os.path.lexists(path):
        commit = refreeze(path, origin=origin, revision=revision)
    else:
        commit = clone(repo_root, path, origin=origin, revision=revision)
    if output(path, "rev-parse", "HEAD") != commit or output(path, "status", "--porcelain"):
        raise CheckoutError(f"the checkout at {path} is not exactly the files of {commit}")
    return {
        "kind": "git",
        "identity": normalize_source_identity(identity),
        "revision": commit,
        "path": path.as_posix(),
        "sha256": None,
    }


def refreeze(path: Path, *, origin: str, revision: str | None) -> str:
    top = git(path, "rev-parse", "--show-toplevel") if path.is_dir() else None
    if top is None or top.returncode != 0 or Path(top.stdout.strip()) != path.resolve():
        raise CheckoutError(f"{path} exists but is not a Git checkout; move it aside")
    remote = git(path, "remote", "get-url", "origin")
    if remote.returncode != 0 or canonical_origin(remote.stdout) != canonical_origin(origin):
        raise CheckoutError(f"the checkout at {path} does not have the origin {origin}")
    if output(path, "status", "--porcelain"):
        raise CheckoutError(
            f"the checkout at {path} has local changes or untracked files; "
            "the operator must keep or discard them"
        )
    if revision is None:
        output(path, "fetch", "--quiet", "origin", "HEAD")
        commit = output(path, "rev-parse", "FETCH_HEAD")
    else:
        commit = revision
        require_commit(path, commit, origin=origin)
    # A checkout already at the commit keeps its branch.
    if output(path, "rev-parse", "HEAD") != commit:
        output(path, "checkout", "--quiet", "--detach", commit)
    return commit


def require_commit(path: Path, commit: str, *, origin: str) -> None:
    """Make `commit` available in the checkout, fetching it when missing."""
    if (
        git(path, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0
        and git(path, "fetch", "--quiet", "origin", commit).returncode != 0
    ):
        raise CheckoutError(f"the requested commit {commit} is not available from {origin}")


def clone(repo_root: Path, path: Path, *, origin: str, revision: str | None) -> str:
    if git(repo_root, "check-ignore", "-q", f"{CHECKOUT_ROOT}/").returncode != 0:
        raise CheckoutError(f"{CHECKOUT_ROOT}/ is not ignored by the repository at {repo_root}")
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{path.name}-", dir=path.parent))
    try:
        result = subprocess.run(
            ["git", "clone", "--quiet", origin, str(staging)],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(f"git clone {origin} failed: {result.stderr.strip()}")
        commit = revision or output(staging, "rev-parse", "HEAD")
        require_commit(staging, commit, origin=origin)
        output(staging, "checkout", "--quiet", "--detach", commit)
        staging.rename(path)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return commit
