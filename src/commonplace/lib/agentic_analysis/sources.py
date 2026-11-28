"""Acquire persistent, revision-pinned Git sources shared by analysis worktrees."""

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

from commonplace.lib.agentic_analysis.effects import (
    UncertainEffectError,
    publication_lock,
    write_json,
)
from commonplace.lib.source_identity import normalize_source_identity

JOURNAL = "effects/acquire.json"


CHECKOUT_ROOT = "related-systems"
GITHUB_REPOSITORY = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
SSH_GITHUB = re.compile(r"git@github\.com:(.+)")


class CheckoutError(ValueError):
    """The requested source checkout cannot be acquired safely."""


def github_checkout_name(identity: str) -> str | None:
    """The owner-qualified directory name for a GitHub repository identity."""
    match = GITHUB_REPOSITORY.fullmatch(normalize_source_identity(identity))
    if match is None:
        return None
    return f"{match[1]}--{match[2]}"


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


def checkout_root(repo: Path) -> Path:
    """Resolve the shared storage setting from this Git repository."""
    setting = "commonplace.relatedSystemsDir"
    config = git(repo, "config", "--local", "--get", setting)
    worktrees = output(repo, "worktree", "list", "--porcelain", "-z")
    main = Path(worktrees.split("\0", 1)[0].removeprefix("worktree "))
    if config.returncode == 1:
        root = main / CHECKOUT_ROOT
    elif config.returncode == 0:
        root = Path(config.stdout.rstrip("\n"))
    else:
        raise CheckoutError(f"cannot read {setting}: {config.stderr.strip()}")
    if not root.is_absolute() or root != root.resolve():
        raise CheckoutError(f"{setting} must be a canonical absolute path: {root}")
    for tree in (main, repo):
        if root.is_relative_to(tree):
            relative = root.relative_to(tree)
            if not relative.parts or git(tree, "check-ignore", "-q", "--", f"{relative}/").returncode:
                raise CheckoutError(f"checkout directory {root} must be ignored by {tree}")
    return root


def require_commit(path: Path, commit: str, *, origin: str) -> None:
    """Make `commit` available in the checkout, fetching it when missing."""
    if (
        git(path, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0
        and git(path, "fetch", "--quiet", "origin", commit).returncode != 0
    ):
        raise CheckoutError(f"the requested commit {commit} is not available from {origin}")


def clone(path: Path, *, origin: str, revision: str, seed: Path | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{path.name}-", dir=path.parent))
    try:
        result = subprocess.run(
            ["git", "clone", "--quiet", str(seed or origin), str(staging)],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(f"git clone {origin} failed: {result.stderr.strip()}")
        if seed:
            output(staging, "remote", "set-url", "origin", output(seed, "remote", "get-url", "origin"))
        require_commit(staging, revision, origin=origin)
        output(staging, "checkout", "--quiet", "--detach", revision)
        staging.rename(path)
    finally:
        shutil.rmtree(staging, ignore_errors=True)


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


def _load_journal(path: Path, binding: dict, revision: str | None) -> dict:
    try:
        record = json.loads(path.read_bytes())
        if (not isinstance(record, dict) or record.keys() != binding.keys() | {"state", "source", "revision"}
                or any(record[key] != value for key, value in binding.items())
                or not isinstance(record["revision"], str) or not re.fullmatch(r"[0-9a-f]{40}", record["revision"])
                or (revision is not None and record["revision"] != revision)
                or record["state"] not in ("started", "completed")
                or (record["state"] == "started" and record["source"] is not None)):
            raise ValueError("journal disagrees with acquisition inputs")
    except (OSError, ValueError) as error:
        raise AcquisitionUncertainError(f"cannot verify acquisition journal {path}: {error}") from error
    return record


def _checkout_head(path: Path, identity: str) -> str:
    """Inspect only; do not fetch, detach, clean or repair anything."""
    if path.resolve() != path or not path.is_dir():
        raise CheckoutError(f"{path} is not a regular checkout at its declared path; move it aside")
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


def acquire(repo: Path, run_dir: Path, *, identity: str, revision: str | None, inputs_digest: str) -> bytes:
    """Pin the selected commit before installing its checkout. Retries use the journaled pin."""
    name = github_checkout_name(identity)
    journal = run_dir / JOURNAL
    if journal.resolve() != journal:
        raise AcquisitionUncertainError("the acquisition journal must not redirect outside this run")
    if name is None:
        if revision is not None:
            raise ValueError("source-revision requires a GitHub repository identity")
        if os.path.lexists(journal):
            raise AcquisitionUncertainError("a non-Git acquisition has an unexpected existing effect journal")
        return b"null\n"

    root = checkout_root(repo)
    primary = root / name
    with publication_lock(root / ".locks" / name):
        existing = journal.exists()
        binding = {"version": 2, "metadata-sha256": inputs_digest, "root": str(root), "identity": identity}
        if existing:
            record = _load_journal(journal, binding, revision)
            commit = record["revision"]
        else:
            commit = revision or output(repo, "ls-remote", "--exit-code", identity, "HEAD").split("\t")[0]
            if not re.fullmatch(r"[0-9a-f]{40}", commit):
                raise CheckoutError("source revision must be a full 40-hex commit")
            record = {**binding, "revision": commit, "state": "started", "source": None}

        secondary = root / ".revisions" / name / commit
        if existing and record["state"] == "completed":
            source = record.get("source")
            if source not in (_source(primary, identity, commit), _source(secondary, identity, commit)):
                raise AcquisitionUncertainError("completed acquisition journal has an invalid source")
            path = Path(source["path"])
            try:
                if _checkout_head(path, identity) != commit:
                    raise ValueError("checkout revision changed")
            except (OSError, ValueError, RuntimeError) as error:
                raise AcquisitionUncertainError(f"cannot verify the completed acquisition: {error}") from error
        else:
            head = _checkout_head(primary, identity) if os.path.lexists(primary) else None
            path = primary if head in (None, commit) else secondary
            if path.resolve() != path:
                raise CheckoutError(f"checkout must not redirect outside its declared path: {path}")
            if path == secondary and os.path.lexists(path) and _checkout_head(path, identity) != commit:
                raise CheckoutError(f"checkout at {path} has changed revision")
            if not existing:
                _write_journal(journal, record)
            if not path.exists():
                try:
                    clone(path, origin=identity, revision=commit, seed=primary if path == secondary else None)
                except Exception as error:
                    if not os.path.lexists(path):
                        raise
                    if _checkout_head(path, identity) != commit:
                        raise AcquisitionUncertainError(f"cannot verify interrupted clone at {path}") from error
            if _checkout_head(path, identity) != commit:
                raise CheckoutError(f"checkout at {path} differs from the pinned commit")
            source = _source(path, identity, commit)
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
