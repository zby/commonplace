"""Analysis opening, acquisition, boundary and analyst-check handlers.

Opening is read-only outside the engine's attempt commit. Acquisition owns its
external-effect journal. Checks use pinned candidate and criterion bytes;
invocation and environment guards remain separate from content validation.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
from dataclasses import replace
from pathlib import Path

from commonplace.lib.agentic_analysis.acquisition import acquire_source
from commonplace.lib.agentic_analysis.boundary import (
    boundary_refusals,
)
from commonplace.lib.agentic_analysis.candidate import (
    answer_reasons,
    candidate,
    content_reasons,
    judge,
    review,
)
from commonplace.lib.agentic_analysis.checkout import github_checkout_path
from commonplace.lib.agentic_analysis.guards import (
    inspect_destination,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_analysis.sets import (
    RETAINED_ROOT,
    analysis_layout,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.agentic_analysis.worktree import (
    STATE_ROOT,
    preparation_for,
    reject_legacy_run,
    require_run_code,
    source_checkout,
)
from commonplace.lib.note_parser import parse_document
from commonplace.workflow import CodeAttempt

ANALYSTS = ("runtime", "memory", "epistemic")


def _head(repo: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=repo, check=True,
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError(f"cannot inspect the analysis worktree HEAD: {repo}") from error
    commit = result.stdout.strip()
    if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        raise ValueError("analysis worktree HEAD must be a full 40-hex commit")
    return commit


def open_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Open a prepared new-engine analysis by returning checked run metadata.

    Run parameters are fixed by start_run, not read from a file input. The
    executing code, library, run location, preparation token, method commit,
    worktree cleanliness and incumbent all pass the existing opening guards.
    No source is acquired and no legacy opening/run-state/output copy is made.

    Legacy state is rejected, not converted. Its engine is retired; preserved
    run directories are historical evidence, not inputs to this workflow.
    New-engine analysis runs require a ready token-bearing preparation record.
    """
    parameters = attempt.parameters
    for name in ("system", "source-identity", "source"):
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
    revision = parameters.get("source-revision")
    if revision is not None:
        if not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{40}", revision) is None:
            raise ValueError("source-revision must be a full 40-hex Git commit")
        if github_checkout_path(identity) is None:
            raise ValueError("source-revision requires a GitHub repository identity")

    run_dir = attempt.run_dir
    reject_legacy_run(run_dir)
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
    _, repo = _locate(attempt)
    return {"source": acquire_source(repo, attempt.run_dir, attempt.read("metadata"))}


def _require_opened_method(repo: Path, metadata: dict, *, job: str) -> None:
    preparation = preparation_for(repo)
    if metadata["run-id"].rsplit("-", 2)[-2:-1] != [preparation["token"]]:
        raise ValueError(f"{job} preparation token differs from the opened run")
    commit = metadata.get("inputs-commit")
    if _head(repo) != commit or preparation.get("commit") != commit:
        raise ValueError(f"{job} worktree differs from the opened preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)


def _locate(attempt: CodeAttempt) -> tuple[dict, Path]:
    """The opened run's metadata and checkout; opening and publication own the guards."""
    repo = source_checkout(attempt.run_dir)
    if repo is None:
        raise ValueError("analysis jobs must run inside their analysis checkout")
    return json.loads(attempt.read("metadata")), repo


def _opened_environment(attempt: CodeAttempt, metadata_bytes: bytes | None, *, job: str) -> tuple[dict, Path]:
    if metadata_bytes is None:
        raise ValueError(f"{job} requires the opening metadata")
    metadata = json.loads(metadata_bytes)
    if not isinstance(metadata, dict) or metadata.get("run-id") != attempt.run_dir.name:
        raise ValueError(f"{job} opening metadata must name this run")
    repo = source_checkout(attempt.run_dir)
    if repo is None or attempt.run_dir.parent != repo / STATE_ROOT or attempt.library != repo / "kb":
        raise ValueError(f"{job} must use this run's analysis checkout and recorded library")
    require_run_code(attempt.run_dir, cwd=Path.cwd())
    _require_opened_method(repo, metadata, job=job)
    return metadata, repo


def check_boundary(attempt: CodeAttempt) -> dict[str, bytes]:
    """Judge the pinned boundary, never a mutable set projection or hand-out file.

    Content checks see a one-member snapshot at its intended set path. Invocation
    checks bind its run identity and source to opening/acquisition; later checks
    rely on that binding. Self-citations are content checks, not engine
    relations, so no scope is claimed.
    """
    metadata, repo = _locate(attempt)
    check = candidate(attempt, "boundary", ())
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
    source_pin = frozen if frozen is not None or reasons else check.fields.get("source")
    reasons += content_reasons(replace(check, source=source_pin))
    judge(check, reasons)
    return {}


def _check_analyst(attempt: CodeAttempt, member: str) -> dict[str, bytes]:
    check = candidate(attempt, member, ("boundary", *(role for role in ANALYSTS if role != member)))
    reasons = review(check) + answer_reasons(
        check, record="producer-attempt", output="report", incumbent="incumbent-report",
    )
    # The memory report is the source of the profile's source identity.
    if member == "memory" and check.fields:
        opened = _locate(attempt)[0]["source-identity"]
        if check.fields.get("source-identity") != opened:
            reasons.append("[invocation] source-identity must be the opening's normalized source identity")
    judge(check, reasons)
    return {}


def check_runtime(attempt: CodeAttempt) -> dict[str, bytes]:
    """Judge a runtime candidate and its correction answers against pinned inputs."""
    return _check_analyst(attempt, "runtime")


def check_memory(attempt: CodeAttempt) -> dict[str, bytes]:
    """Judge a memory candidate and its correction answers against pinned inputs."""
    return _check_analyst(attempt, "memory")


def check_epistemic(attempt: CodeAttempt) -> dict[str, bytes]:
    """Judge an epistemic candidate and its correction answers against pinned inputs."""
    return _check_analyst(attempt, "epistemic")
