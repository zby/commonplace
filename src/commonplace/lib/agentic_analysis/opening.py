"""Analysis opening and acquisition handlers, and the boundary and analyst declared checks.

Opening is read-only outside the engine's attempt commit. Acquisition passes
the opening's source pins to the shared effect. The declared checks run
inside the standard check, on its pinned candidate and criterion bytes;
environment guards stay separate from content validation.
"""

from __future__ import annotations

import datetime
import json
import os
import re
from hashlib import sha256
from pathlib import Path

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.checks import Candidate
from commonplace.artifactrun.sources import acquire, github_checkout_path
from commonplace.artifactrun.worktree import (
    preparation_for,
    require_run_code,
    require_running_package_unchanged,
    run_command,
    source_checkout,
)
from commonplace.lib.agentic_analysis.analyses import (
    RETAINED_ROOT,
    analysis_layout,
    source_slug,
    worker_profile,
)
from commonplace.lib.agentic_analysis.boundary import boundary_refusals
from commonplace.lib.agentic_analysis.guards import (
    checkout,
    inspect_destination,
    require_publishable_worktree,
)
from commonplace.lib.agentic_analysis.records import declared_ids
from commonplace.lib.agentic_analysis.worktree import STATE_ROOT
from commonplace.lib.note_parser import parse_document
from commonplace.lib.source_identity import normalize_source_identity


def _head(repo: Path) -> str:
    commit = run_command(["git", "rev-parse", "HEAD"], cwd=repo)
    if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
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
    if "review-path" in parameters:
        raise ValueError("review-path is no longer a run parameter; publication uses the source slug")
    system = parameters["system"]
    if "\n" in system or "\r" in system:
        raise ValueError("system must be a single-line name")
    raw_identity = parameters["source-identity"].strip()
    if "\n" in raw_identity or "\r" in raw_identity:
        raise ValueError("source-identity must normalize to a nonempty single-line identity")
    identity = normalize_source_identity(raw_identity)
    if not identity:
        raise ValueError("source-identity must normalize to a nonempty single-line identity")
    worker = worker_profile(attempt.read("worker-profiles"), parameters["worker-profile"])
    revision = parameters.get("source-revision")
    if revision is not None:
        if not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{40}", revision) is None:
            raise ValueError("source-revision must be a full 40-hex Git commit")
        if github_checkout_path(identity) is None:
            raise ValueError("source-revision requires a GitHub repository identity")

    run_dir = attempt.run_dir
    repo = source_checkout(run_dir)
    if repo is None or run_dir.parent != repo / STATE_ROOT:
        raise ValueError(f"a new-engine analysis run must be directly under its checkout's {STATE_ROOT}")
    if attempt.library != repo / "kb":
        raise ValueError("the run's recorded library must be the analysis worktree's kb directory")
    require_run_code(run_dir, cwd=Path.cwd())
    preparation = preparation_for(repo)
    slug = source_slug(identity, system)
    token = preparation["token"]
    if re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(slug)}-{token}-\d{{2}}", run_dir.name) is None:
        raise ValueError("analysis run ID does not match the source slug and worktree preparation token")
    commit = _head(repo)
    if preparation.get("commit") != commit:
        raise ValueError("analysis worktree HEAD differs from its preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)
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
        "command-path": str(repo / ".venv" / ("Scripts" if os.name == "nt" else "bin")),
        "capture-directory": str(run_dir / "sources"),
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
    metadata_bytes = attempt.read("metadata")
    metadata, repo = locate(attempt)
    identity = metadata.get("source-identity")
    revision = metadata.get("source-revision")
    if not isinstance(identity, str) or not identity or normalize_source_identity(identity) != identity:
        raise ValueError("opening metadata must carry the normalized source identity")
    if revision is not None and (not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision)):
        raise ValueError("opening metadata source-revision must be a full 40-hex commit")
    return {"source": acquire(repo, attempt.run_dir, identity=identity, revision=revision,
                              inputs_digest=sha256(metadata_bytes).hexdigest())}


def locate(attempt: CodeAttempt) -> tuple[dict, Path]:
    """The opened run's metadata and checkout; opening and publication own the guards."""
    return json.loads(attempt.read("metadata")), checkout(attempt.run_dir)


# Declared checks: the standard check calls each with the candidate it built;
# each returns refusal reasons and reads only inputs its plan entry declares.


def bound_boundary(check: Candidate) -> list[str]:
    """Bind the boundary to its run: run id and source from opening and acquisition.

    The boundary fills the plan's frozen-source role, so the standard check
    inspects the candidate's own source only after this binding passes. A
    corrected candidate must also bind to the incumbent's pinned source.
    """
    attempt = check.attempt
    metadata, repo = locate(attempt)
    frozen = json.loads(attempt.read("source"))
    if frozen is not None and (not isinstance(frozen, dict) or frozen.get("kind") != "git"):
        raise ValueError("boundary check requires a Git source object or explicit JSON null")
    # Only an accepted boundary establishes the capture pin. A declared member
    # input preserves it across later corrections without a second source record.
    incumbent_bytes = attempt.read("incumbent-boundary")
    incumbent_source = None
    if incumbent_bytes is not None:
        incumbent, error = parse_document(incumbent_bytes.decode("utf-8"))
        if incumbent is None or error:
            raise ValueError("boundary check cannot read the incumbent boundary")
        incumbent_source = (incumbent.frontmatter or {}).get("source")
    reasons = ["[invocation] " + reason for reason in boundary_refusals(
        check.data, repo_root=repo, run_id=metadata["run-id"],
        identity=metadata["source-identity"], frozen=frozen,
        capture_directory=Path(metadata["capture-directory"]),
    )]
    if incumbent_source is not None and incumbent_source != frozen:
        reasons += ["[incumbent] " + reason for reason in boundary_refusals(
            check.data, repo_root=repo, run_id=metadata["run-id"],
            identity=metadata["source-identity"], frozen=incumbent_source,
        )]
    return reasons


def preserved_records(check: Candidate) -> list[str]:
    """A corrected report keeps every record its accepted predecessor declared; others cite them."""
    incumbent = check.attempt.read("incumbent-report")
    if incumbent is None:
        return []
    dropped = sorted(set(declared_ids(incumbent.decode("utf-8")))
                     - set(declared_ids(check.data.decode("utf-8", errors="replace"))))
    if not dropped:
        return []
    return ["[correction] record declarations: keep every record the accepted predecessor declared: "
            + ", ".join(dropped) + "; correct its finding without changing its referent"]


def memory_source_identity(check: Candidate) -> list[str]:
    """The memory report carries the opening's normalized source identity, which the profile copies."""
    if not check.fields:
        return []
    opened = json.loads(check.attempt.read("metadata"))["source-identity"]
    if check.fields.get("source-identity") != opened:
        return ["[invocation] source-identity must be the opening's normalized source identity"]
    return []
