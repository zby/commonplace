"""Frozen external sources: identity, Git checkouts and their acquisition.

A GitHub source is read from `related-systems/<owner>--<repo>/`, detached at
one full commit with no local changes. Code acquires that checkout before any
worker reads it, so no worker clones, fetches or checks out anything.

A missing checkout is cloned into a temporary sibling and renamed into place
only once it is detached at the commit, so an interrupted acquisition leaves
no partial checkout behind. An existing clean checkout is moved to the
commit; it is never cleaned: local changes, a foreign origin, or a commit the
origin does not have stop the run for the operator.

Acquisition keeps its own effect journal, separate from the engine's attempt
state. It records intent before mutation and the source before the engine
commits an output. A retry never silently selects a new revision when a
completed or uncertain acquisition may already have selected one.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path
from typing import Any

from commonplace.artifactrun import UncertainEffectError
from commonplace.artifactrun.effects import write_json
from commonplace.lib.source_identity import normalize_source_identity

JOURNAL = "effects/acquire.json"


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


class AcquisitionUncertainError(UncertainEffectError):
    """Acquisition cannot establish a frozen result or the absence of its effect."""


def _write_journal(path: Path, record: dict) -> None:
    write_json(path, record)


def _complete_journal(path: Path, record: dict, source: dict) -> None:
    try:
        _write_journal(path, {**record, "state": "completed", "source": source})
    except OSError as error:
        raise AcquisitionUncertainError(
            f"cannot record acquisition completion at {path}; preserve the checkout at {source['revision']}"
        ) from error


def _load_journal(path: Path, inputs_digest: str) -> dict:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise AcquisitionUncertainError(f"cannot read acquisition journal {path}; preserve it for inspection") from error
    if (
        not isinstance(record, dict)
        or set(record) != {"version", "metadata-sha256", "state", "path-existed", "initial-head", "source"}
        or type(record["version"]) is not int or record["version"] != 1
        or record["metadata-sha256"] != inputs_digest
        or record["state"] not in ("started", "completed")
        or not isinstance(record["path-existed"], bool)
        or (record["path-existed"] and not re.fullmatch(r"[0-9a-f]{40}", str(record["initial-head"])))
        or (not record["path-existed"] and record["initial-head"] is not None)
        or (record["state"] == "started" and record["source"] is not None)
    ):
        raise AcquisitionUncertainError(f"acquisition journal {path} is malformed or belongs to different inputs")
    return record


def _checkout_head(path: Path, identity: str) -> str:
    """Inspect only; do not fetch, detach, clean or repair anything."""
    if path.resolve() != path or not path.is_dir():
        raise ValueError(f"{path} is not a regular checkout at its declared path; move it aside")
    top = output(path, "rev-parse", "--show-toplevel")
    if Path(top).resolve() != path:
        raise ValueError(f"{path} is not the Git checkout root")
    origin = output(path, "remote", "get-url", "origin")
    if canonical_origin(origin) != canonical_origin(identity):
        raise ValueError(f"the checkout at {path} does not have the origin {identity}")
    if output(path, "status", "--porcelain"):
        raise ValueError(f"the checkout at {path} has local changes or untracked files; preserve them")
    head = output(path, "rev-parse", "HEAD")
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise ValueError(f"the checkout at {path} has no full 40-hex HEAD")
    return head


def _source(path: Path, identity: str, revision: str) -> dict:
    return {"kind": "git", "identity": identity, "revision": revision, "path": path.as_posix(), "sha256": None}


def _recognize(record: dict, path: Path, identity: str, revision: str | None) -> dict | None:
    """Return a verified source, None for a safe retry, or refuse uncertainty."""
    if record["state"] == "completed":
        source = record["source"]
        if not isinstance(source, dict) or not re.fullmatch(r"[0-9a-f]{40}", str(source.get("revision"))):
            raise AcquisitionUncertainError("the completed acquisition journal has no valid source record")
        if source != _source(path, identity, source["revision"]) or (revision and source["revision"] != revision):
            raise AcquisitionUncertainError("the completed acquisition journal disagrees with the frozen source inputs")
        try:
            if _checkout_head(path, identity) != source["revision"]:
                raise ValueError("the completed checkout's revision changed")
        except (ValueError, RuntimeError, OSError) as error:
            raise AcquisitionUncertainError(f"cannot verify the completed acquisition: {error}") from error
        return source
    if not os.path.lexists(path):
        if not record["path-existed"]:
            return None  # No checkout was installed, so a new clone is safe.
        raise AcquisitionUncertainError("the checkout present at acquisition start has disappeared")
    try:
        head = _checkout_head(path, identity)
    except (ValueError, RuntimeError, OSError) as error:
        raise AcquisitionUncertainError(f"cannot establish the interrupted acquisition's outcome: {error}") from error
    if revision:
        if head == revision:
            return _source(path, identity, head)
        if record["path-existed"] and head == record["initial-head"]:
            return None  # The requested deterministic checkout has not happened.
        raise AcquisitionUncertainError("the interrupted checkout is neither its original nor its requested revision")
    if not record["path-existed"] and git(path, "symbolic-ref", "-q", "HEAD").returncode == 1:
        # The clone primitive publishes only a clean, detached checkout by
        # atomic rename. Observe that installed result, not the remote tip now.
        return _source(path, identity, head)
    raise AcquisitionUncertainError(
        "cannot establish which default-branch snapshot the interrupted acquisition selected; "
        "preserve the journal and checkout for operator inspection, or start a separate run"
    )


def acquire(repo: Path, run_dir: Path, *, identity: str, revision: str | None, inputs_digest: str) -> bytes:
    """Return the frozen Git source JSON, or JSON null for a non-Git identity.

    ``identity`` is normalized and ``revision``, when given, a full commit.
    ``inputs_digest`` binds the journal to the inputs that chose them. The
    effect journal is recognition evidence, never a new analytical input. It
    is retained on ordinary failure, uncertainty and interrupted attempts.
    """
    relative = github_checkout_path(identity)
    journal = run_dir / JOURNAL
    if journal.is_symlink() or journal.parent.is_symlink():
        raise AcquisitionUncertainError("the acquisition journal must not redirect outside this run")
    if relative is None:
        if revision is not None:
            raise ValueError("source-revision requires a GitHub repository identity")
        if os.path.lexists(journal):
            raise AcquisitionUncertainError("a non-Git acquisition has an unexpected existing effect journal")
        return b"null\n"  # Explicitly not a frozen source; a worker must establish one.
    path = repo / relative
    if path.resolve() != path:
        error = AcquisitionUncertainError if os.path.lexists(journal) else ValueError
        raise error("the acquisition checkout must not redirect outside its declared path")
    if git(repo, "check-ignore", "-q", f"{CHECKOUT_ROOT}/").returncode != 0:
        raise ValueError(f"{CHECKOUT_ROOT}/ must be ignored before acquisition")
    if os.path.lexists(journal):
        record = _load_journal(journal, inputs_digest)
        source = _recognize(record, path, identity, revision)
        if source is not None:
            if record["state"] != "completed":
                _complete_journal(journal, record, source)
            return (json.dumps(source, sort_keys=True) + "\n").encode("utf-8")
    else:
        existed = os.path.lexists(path)
        initial = _checkout_head(path, identity) if existed else None
        record = {"version": 1, "metadata-sha256": inputs_digest, "state": "started",
                  "path-existed": existed, "initial-head": initial, "source": None}
        _write_journal(journal, record)
    try:
        source = freeze_checkout(repo, relative, identity=identity, origin=identity, revision=revision)
        if not isinstance(source, dict) or not re.fullmatch(r"[0-9a-f]{40}", str(source.get("revision"))):
            raise AcquisitionUncertainError("acquisition returned no valid frozen source record")
        source_revision = source["revision"]
        if (source != _source(path, identity, source_revision) or (revision and source_revision != revision)
                or _checkout_head(path, identity) != source_revision):
            raise AcquisitionUncertainError("acquisition returned a source that does not match the installed checkout")
    except AcquisitionUncertainError:
        raise
    except Exception:  # Classify the external effect before any retry.
        source = _recognize(record, path, identity, revision)
        if source is None:
            raise
        # The operation raised after installing a recognizable final result.
    _complete_journal(journal, record, source)
    return (json.dumps(source, sort_keys=True) + "\n").encode("utf-8")


def frozen_source_refusals(source: dict[str, Any]) -> list[str]:
    """Verify a clean Git checkout's commit or a capture file's exact digest."""
    path = Path(str(source.get("path") or ""))
    if not path.is_absolute():
        return ["source.path must be the absolute path of the frozen source"]
    if path.is_symlink() or path.resolve() != path:
        return ["source.path must be canonical and not redirected through a symlink"]
    if source.get("kind") == "capture":
        if not path.is_file():
            return [f"source.path {path} is not a file"]
        digest = sha256(path.read_bytes()).hexdigest()
        if source.get("sha256") != digest:
            return [f"source.sha256 must be the SHA-256 of the capture file: expected {digest}"]
        return []
    revision = str(source.get("revision") or "")
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        return ["source.revision must be a full 40-hex commit"]

    def git(*args: str) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(path), *args], capture_output=True, text=True, check=False, timeout=30,
        )
        return result.stdout if result.returncode == 0 else None

    head = git("rev-parse", "HEAD") if path.is_dir() else None
    if head is None:
        return [f"source.path {path} is not a Git checkout"]
    root = git("rev-parse", "--show-toplevel")
    if root is None or Path(root.strip()).resolve() != path:
        return ["source.path must be the Git checkout root"]
    if head.strip() != revision:
        return [f"the checkout at {path} is not at source.revision"]
    status = git("status", "--porcelain")
    if status is None or status:
        return [
            (
                f"the checkout at {path} does not hold exactly the commit's files; "
                "a clone made without checkout lists them all as deleted"
            )
        ]
    return []
