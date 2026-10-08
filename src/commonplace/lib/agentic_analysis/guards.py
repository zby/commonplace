"""Repository and destination guards shared by analysis opening and publication."""

from __future__ import annotations

import fcntl
import os
import subprocess
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis.sets import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    current_analyses,
    is_review_path,
    normalize_source_identity,
)

# A sibling run's publication may remain uncommitted while a batch runs.
OUTPUT_LOCATIONS: tuple[str, ...] = (f"{RETAINED_ROOT.as_posix()}/", f"{ARCHIVE_ROOT.as_posix()}/")


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


def _git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, check=False,
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot run git {args[0]} in the repository") from exc


def _status_entries(porcelain: str) -> list[tuple[str, str]]:
    """Parse ``git status --porcelain -z`` into ``(code, path)`` pairs.

    A rename or copy entry is followed by its origin path, reported as a
    second entry with the same code so both sides are checked.
    """
    fields = porcelain.split("\0")
    entries: list[tuple[str, str]] = []
    index = 0
    while index < len(fields):
        field_text = fields[index]
        index += 1
        if len(field_text) < 4:
            continue
        code, path = field_text[:2], field_text[3:]
        entries.append((code, path))
        if code[0] in "RC" and index < len(fields):
            entries.append((code, fields[index]))
            index += 1
    return entries


def require_publishable_worktree(repo_root: Path) -> None:
    """Require a worktree clean outside the workflow's own output locations.

    Under an output location, an untracked file or an unstaged modification
    of a tracked file is allowed: a sibling run's uncommitted publication, new
    or replacing an existing review. Anywhere else no tracked file may be
    modified or staged, and no untracked file may sit under ``kb/``. Ignored
    paths never count.
    """
    status = _git(repo_root, "status", "--porcelain", "-z", "--untracked-files=all")
    if status.returncode != 0:
        raise ValueError("cannot inspect the repository's Git status")
    changed: list[str] = []
    untracked: list[str] = []
    for code, path in _status_entries(status.stdout):
        in_outputs = path.startswith(OUTPUT_LOCATIONS)
        if code == "??":
            if path.startswith("kb/") and not in_outputs:
                untracked.append(path)
        elif not (code == " M" and in_outputs):
            changed.append(path)
    problems = []
    if changed:
        problems.append("tracked files with local changes: " + ", ".join(sorted(changed)))
    if untracked:
        problems.append(
            "untracked files under kb/ outside the publication outputs: "
            + ", ".join(sorted(untracked))
        )
    if problems:
        raise ValueError(
            "publication requires a clean worktree outside its output locations; "
            + "; ".join(problems)
        )


def running_package_root() -> Path:
    """The checkout whose ``src/commonplace`` supplies the running code.

    Commonplace is installed editable from one checkout; commands run inside
    a batch worktree still execute that checkout's source.
    """
    import commonplace

    return Path(commonplace.__file__).resolve().parents[2]


def require_running_package_unchanged(inputs_commit: str) -> None:
    """Require the executing package source to equal ``inputs-commit``.

    The opening metadata pins the publishing tree's method; this check covers
    the code actually running, which may come from another checkout.
    """
    root = running_package_root()
    if not (root / ".git").exists():
        raise ValueError(
            f"running commonplace package is not a source checkout ({root}); "
            "cannot confirm it matches inputs-commit"
        )
    if _git(root, "cat-file", "-e", f"{inputs_commit}^{{commit}}").returncode != 0:
        raise ValueError(
            f"inputs-commit {inputs_commit} is unknown to the checkout running "
            f"commonplace ({root})"
        )
    changed = _git(root, "diff", "--name-only", inputs_commit, "--", "src/commonplace")
    untracked = _git(root, "ls-files", "--others", "--exclude-standard", "--", "src/commonplace")
    if changed.returncode != 0 or untracked.returncode != 0:
        raise ValueError("cannot compare the running package source against inputs-commit")
    paths = sorted({*changed.stdout.split(), *untracked.stdout.split()})
    if paths:
        raise ValueError(
            f"running commonplace source ({root}) differs from inputs-commit "
            f"{inputs_commit}: " + ", ".join(paths)
        )


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


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


@contextmanager
def publication_lock(repo_root: Path) -> Iterator[None]:
    """Serialize cooperating publishers in this repository, including rollback.

    The persistent lock file lives in the ignored analysis state root. Never
    unlink it: waiters must keep using the same inode. Acquire any per-run lock
    first, then this lock; do not acquire a run lock while holding this one.
    This advisory lock is not exclusive ownership of publication files.
    Non-cooperating writes still require authority-level exclusivity.
    """
    path = repo_root.resolve() / "kb/agentic-system-analyses/state/.publication.lock"
    if path.resolve() != path:
        raise ValueError("publication lock must not traverse symlinks")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)
