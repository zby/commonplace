"""Analysis opening and acquisition handlers.

Opening is read-only outside the engine's attempt commit. Acquisition passes
the opening's source pins to the shared effect.
"""

from __future__ import annotations

import datetime
import json
from hashlib import sha256
from pathlib import Path

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.sources import acquire, github_checkout_path
from commonplace.artifactrun.worktree import (
    preparation_for,
    require_running_package_unchanged,
    run_command,
)
from commonplace.lib.agentic_analysis import run_ids
from commonplace.lib.agentic_analysis.analyses import (
    RETAINED_ROOT,
    analysis_layout,
    resolve_worker_profile,
    source_slug,
)
from commonplace.lib.agentic_analysis.guards import (
    checkout,
    inspect_destination,
    require_prepared_method,
    require_publishable_worktree,
    run_checkout,
)
from commonplace.lib.source_identity import normalize_source_identity


def _head(repo: Path) -> str:
    commit = run_command(["git", "rev-parse", "HEAD"], cwd=repo)
    if not run_ids.is_commit(commit):
        raise ValueError("analysis worktree HEAD must be a full 40-hex commit")
    return commit


def open_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Open a prepared analysis by returning checked run metadata.

    Run parameters are fixed by start_run, not read from a file input. The
    executing code, library, run location, preparation token, method commit,
    worktree cleanliness and incumbent all pass the opening guards. No source
    is acquired. Analysis runs require a ready token-bearing preparation record.
    """
    parameters = attempt.parameters
    for name in ("system", "source-identity", "source", "worker-profile"):
        if not isinstance(parameters.get(name), str) or not parameters[name].strip():
            raise ValueError(f"analysis opening requires a nonempty {name} run parameter")
    system = parameters["system"]
    if "\n" in system or "\r" in system:
        raise ValueError("system must be a single-line name")
    identity = parameters["source-identity"]
    normalized = "" if "\n" in identity or "\r" in identity else normalize_source_identity(identity)
    if not normalized:
        raise ValueError("source-identity must normalize to a nonempty single-line identity")
    # Members bind their source identity to this run value, so it must already be canonical.
    if normalized != identity:
        raise ValueError(f"source-identity must be given normalized, as {normalized!r}")
    worker = resolve_worker_profile(attempt.read("worker-profiles"), parameters["worker-profile"])
    revision = parameters.get("source-revision")
    if revision is not None:
        if not run_ids.is_commit(revision):
            raise ValueError("source-revision must be a full 40-hex Git commit")
        if github_checkout_path(identity) is None:
            raise ValueError("source-revision requires a GitHub repository identity")

    run_dir = attempt.run_dir
    repo = run_checkout(run_dir, attempt.library, job="opening")
    preparation = preparation_for(repo)
    slug = source_slug(identity, system)
    token = preparation["token"]
    if not run_ids.is_run_id(run_dir.name, token=token, slug=slug):
        raise ValueError("analysis run ID does not match the source slug and worktree preparation token")
    commit = _head(repo)
    require_prepared_method(repo, commit, preparation, job="opening")
    destination = (RETAINED_ROOT / slug / analysis_layout().path("overview")).as_posix()
    incumbent = inspect_destination(
        repo_root=repo, generated_destination=destination, source_identity=identity,
    )
    if _head(repo) != commit:
        raise ValueError("analysis worktree HEAD changed during opening")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)
    record = {
        "run-id": run_dir.name,
        "system": system,
        "source-identity": identity,
        "source": parameters["source"],
        "source-revision": revision,
        "worker": worker,
        "inputs-commit": commit,
        "run-date": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "review-path": destination,
        "expected-incumbent-sha256": str(incumbent["expected_incumbent_sha256"]),
    }
    return {"metadata": (json.dumps(record, indent=2) + "\n").encode("utf-8")}


def acquire_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Acquire from pinned opening metadata without launching an analyst.

    Its next model job consumes the engine-specific boundary hand-out.
    Git results are frozen source objects; JSON null means the boundary still
    has to establish a non-Git capture, not that a source check succeeded.
    """
    metadata, repo = locate(attempt)
    return {"source": acquire(repo, attempt.run_dir, identity=metadata["source-identity"],
                              revision=metadata["source-revision"],
                              inputs_digest=sha256(attempt.read("metadata")).hexdigest())}


def locate(attempt: CodeAttempt) -> tuple[dict, Path]:
    """The opened run's metadata and checkout; opening and publication own the guards."""
    return json.loads(attempt.read("metadata")), checkout(attempt.run_dir)
