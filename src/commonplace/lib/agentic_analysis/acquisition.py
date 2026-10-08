"""Acquire a frozen analysis source with consumer-owned effect recognition.

The journal belongs to the acquisition effect, not to the engine's attempt
state or the typed set. It records intent before mutation and the source
before the engine commits an output. A retry never silently selects a new
revision when a completed or uncertain acquisition may already have selected
one. Git operations use the checkout primitive. Non-Git sources remain the
boundary worker's responsibility.
"""

from __future__ import annotations

import json
import os
import re
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis import checkout
from commonplace.lib.agentic_analysis.guards import atomic_write
from commonplace.lib.agentic_analysis.sets import normalize_source_identity
from commonplace.workflow import UncertainEffectError

JOURNAL = "effects/acquire.json"


class AcquisitionUncertainError(UncertainEffectError):
    """Acquisition cannot establish a frozen result or the absence of its effect."""


def _write_journal(path: Path, record: dict) -> None:
    atomic_write(path, (json.dumps(record, sort_keys=True, indent=2) + "\n").encode())


def _complete_journal(path: Path, record: dict, source: dict) -> None:
    try:
        _write_journal(path, {**record, "state": "completed", "source": source})
    except OSError as error:
        raise AcquisitionUncertainError(
            f"cannot record acquisition completion at {path}; preserve the checkout at {source['revision']}"
        ) from error


def _load_journal(path: Path, metadata_digest: str) -> dict:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise AcquisitionUncertainError(f"cannot read acquisition journal {path}; preserve it for inspection") from error
    if (
        not isinstance(record, dict)
        or set(record) != {"version", "metadata-sha256", "state", "path-existed", "initial-head", "source"}
        or type(record["version"]) is not int or record["version"] != 1
        or record["metadata-sha256"] != metadata_digest
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
    top = checkout.output(path, "rev-parse", "--show-toplevel")
    if Path(top).resolve() != path:
        raise ValueError(f"{path} is not the Git checkout root")
    origin = checkout.output(path, "remote", "get-url", "origin")
    if checkout.canonical_origin(origin) != checkout.canonical_origin(identity):
        raise ValueError(f"the checkout at {path} does not have the origin {identity}")
    if checkout.output(path, "status", "--porcelain"):
        raise ValueError(f"the checkout at {path} has local changes or untracked files; preserve them")
    head = checkout.output(path, "rev-parse", "HEAD")
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
    if not record["path-existed"] and checkout.git(path, "symbolic-ref", "-q", "HEAD").returncode == 1:
        # The clone primitive publishes only a clean, detached checkout by
        # atomic rename. Observe that installed result, not the remote tip now.
        return _source(path, identity, head)
    raise AcquisitionUncertainError(
        "cannot establish which default-branch snapshot the interrupted acquisition selected; "
        "preserve the journal and checkout for operator inspection, or start a separate run"
    )


def acquire_source(repo: Path, run_dir: Path, metadata_bytes: bytes) -> bytes:
    """Return the frozen Git source JSON, or JSON null for boundary-owned captures.

    Only opening metadata supplies source identity and an optional revision.
    The effect journal is recognition evidence, never a new analytical input.
    It is retained on ordinary failure, uncertainty and interrupted attempts.
    """
    metadata = json.loads(metadata_bytes)
    if not isinstance(metadata, dict):
        raise TypeError("acquisition opening metadata must be a JSON object")
    identity = metadata.get("source-identity")
    revision = metadata.get("source-revision")
    if not isinstance(identity, str) or not identity or normalize_source_identity(identity) != identity:
        raise ValueError("opening metadata must carry the normalized source identity")
    if revision is not None and (not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision)):
        raise ValueError("opening metadata source-revision must be a full 40-hex commit")
    relative = checkout.github_checkout_path(identity)
    journal = run_dir / JOURNAL
    if journal.is_symlink() or journal.parent.is_symlink():
        raise AcquisitionUncertainError("the acquisition journal must not redirect outside this run")
    if relative is None:
        if revision is not None:
            raise ValueError("source-revision requires a GitHub repository identity")
        if os.path.lexists(journal):
            raise AcquisitionUncertainError("a non-Git acquisition has an unexpected existing effect journal")
        return b"null\n"  # Explicitly not a frozen source; the boundary must establish it.
    path = repo / relative
    if path.resolve() != path:
        error = AcquisitionUncertainError if os.path.lexists(journal) else ValueError
        raise error("the acquisition checkout must not redirect outside its declared path")
    if checkout.git(repo, "check-ignore", "-q", f"{checkout.CHECKOUT_ROOT}/").returncode != 0:
        raise ValueError(f"{checkout.CHECKOUT_ROOT}/ must be ignored before acquisition")
    metadata_digest = sha256(metadata_bytes).hexdigest()
    if os.path.lexists(journal):
        record = _load_journal(journal, metadata_digest)
        source = _recognize(record, path, identity, revision)
        if source is not None:
            if record["state"] != "completed":
                _complete_journal(journal, record, source)
            return (json.dumps(source, sort_keys=True) + "\n").encode("utf-8")
    else:
        existed = os.path.lexists(path)
        initial = _checkout_head(path, identity) if existed else None
        record = {"version": 1, "metadata-sha256": metadata_digest, "state": "started",
                  "path-existed": existed, "initial-head": initial, "source": None}
        _write_journal(journal, record)
    try:
        source = checkout.freeze_checkout(repo, relative, identity=identity, origin=identity, revision=revision)
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
