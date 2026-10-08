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
from pathlib import Path

from commonplace.lib.agentic_analysis.acquisition import acquire_source
from commonplace.lib.agentic_analysis.boundary import (
    boundary_refusals,
    frozen_source_refusals,
)
from commonplace.lib.agentic_analysis.checkout import github_checkout_path
from commonplace.lib.agentic_analysis.checks import (
    correction_findings,
    refusal_findings,
)
from commonplace.lib.agentic_analysis.guards import (
    inspect_destination,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_analysis.validation import criterion_bytes
from commonplace.lib.agentic_analysis.worktree import (
    STATE_ROOT,
    preparation_for,
    reject_legacy_run,
    require_run_code,
    source_checkout,
)
from commonplace.lib.agentic_set import (
    RETAINED_ROOT,
    SET_TYPE,
    analysis_layout,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.directory_layout import parse_layout
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_draft_at_slot
from commonplace.workflow import CodeAttempt


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
    metadata_bytes = attempt.read("metadata")
    metadata, repo = _opened_environment(attempt, metadata_bytes, job="acquisition")
    source = acquire_source(repo, attempt.run_dir, metadata_bytes)
    _require_opened_method(repo, metadata, job="acquisition")
    return {"source": source}


def _require_opened_method(repo: Path, metadata: dict, *, job: str) -> None:
    preparation = preparation_for(repo)
    if metadata["run-id"].rsplit("-", 2)[-2:-1] != [preparation["token"]]:
        raise ValueError(f"{job} preparation token differs from the opened run")
    commit = metadata.get("inputs-commit")
    if _head(repo) != commit or preparation.get("commit") != commit:
        raise ValueError(f"{job} worktree differs from the opened preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)


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


def _analysis_layout(attempt: CodeAttempt):
    """Read the declared layout, never the mutable installed set type."""
    data = attempt.read("set-type")
    if data is None:
        raise ValueError("analysis check requires the pinned set type")
    document, error = parse_document(data.decode("utf-8"))
    if document is None or error:
        raise ValueError("analysis check cannot read the pinned set type")
    return parse_layout((document.frontmatter or {}).get("layout"), where=SET_TYPE)


def check_boundary(attempt: CodeAttempt) -> dict[str, bytes]:
    """Judge the pinned boundary, never a mutable set projection or hand-out file.

    Content checks see a one-member snapshot at its intended set path. Invocation
    checks bind its run identity and source to opening/acquisition. Self-citations
    are content checks, not engine relations; no downstream coverage is claimed.
    The declaration binds this check only with translated downstream hand-outs.
    """
    metadata, repo = _opened_environment(attempt, attempt.read("metadata"), job="boundary check")
    candidate = attempt.read("candidate")
    source_bytes = attempt.read("source")
    if candidate is None or source_bytes is None:
        raise ValueError("boundary check requires its candidate and acquisition result")
    frozen = json.loads(source_bytes)
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
        candidate, repo_root=repo, run_id=metadata["run-id"],
        identity=metadata["source-identity"], frozen=frozen,
        capture_directory=Path(metadata["capture-directory"]),
    )]
    if incumbent_source is not None and incumbent_source != frozen:
        reasons += ["[incumbent] " + reason for reason in boundary_refusals(
            candidate, repo_root=repo, run_id=metadata["run-id"],
            identity=metadata["source-identity"], frozen=incumbent_source,
        )]
    source_pin = frozen
    if frozen is None and not reasons:
        document, error = parse_document(candidate.decode("utf-8", errors="replace"))
        if document is not None and not error:
            source_pin = (document.frontmatter or {}).get("source")
    findings = validate_draft_at_slot(
        attempt.run_dir / "set", "boundary.md", candidate, repo_root=repo, members={},
        manifest=f"type: {SET_TYPE}\n".encode(), criteria=criterion_bytes(attempt),
        frozen_source=source_pin,
    )
    reasons += ["[set] " + finding.render() for finding in findings if not finding.info]
    _require_opened_method(repo, metadata, job="boundary check")
    attempt.judge(
        "candidate", outcome="refused" if reasons else "accepted", findings="\n".join(reasons),
    )
    return {}


def _check_analyst(attempt: CodeAttempt, member: str) -> dict[str, bytes]:
    metadata, repo = _opened_environment(attempt, attempt.read("metadata"), job=f"{member} check")
    candidate = attempt.read("candidate")
    if candidate is None:
        raise ValueError(f"{member} check requires a candidate")
    partners = ["boundary", *[role for role in ("runtime", "memory", "epistemic") if role != member]]
    layout = _analysis_layout(attempt)
    snapshot = {}
    present = []
    for role in partners:
        data = attempt.read(role)
        if data is not None:
            snapshot[layout.path(role)] = data
            present.append(role)
    boundary, error = parse_document(snapshot["boundary.md"].decode("utf-8"))
    if boundary is None or error or not isinstance((boundary.frontmatter or {}).get("source"), dict):
        raise ValueError(f"{member} check requires a boundary with a frozen source")
    source = boundary.frontmatter["source"]
    findings = validate_draft_at_slot(
        attempt.run_dir / "set", layout.path(member), candidate,
        repo_root=repo, members=snapshot, manifest=f"type: {SET_TYPE}\n".encode(),
        criteria=criterion_bytes(attempt), frozen_source=source,
    )
    reasons = ["[set] " + finding.render() for finding in findings
               if not finding.info and not finding.warn and not finding.absent]
    reasons += ["[invocation] " + reason for reason in frozen_source_refusals(source)]
    try:
        document, _ = parse_document(candidate.decode("utf-8"))
    except UnicodeError:
        document = None
    if document is not None:
        fields = document.frontmatter or {}
        if fields.get("run-id") != metadata["run-id"]:
            reasons.append("[invocation] run-id must be the opening's run identity")
        if member == "memory" and fields.get("source-identity") != metadata["source-identity"]:
            reasons.append("[invocation] source-identity must be the opening's normalized source identity")
    answered = attempt.read("answered-refusal")
    producer_bytes = attempt.read("producer-attempt")
    if producer_bytes is None:
        raise ValueError("analyst check requires the producer attempt")
    producer = json.loads(producer_bytes)
    reasons += ["[correction] " + reason for reason in correction_findings(
        candidate, member=member, incumbent=attempt.read("incumbent-report"),
        refusal=answered, answers=attempt.read("answers"),
        previous_version=producer["previous_outputs"].get("report"),
    )]
    _require_opened_method(repo, metadata, job=f"{member} check")
    scope = [f"{member}:cites:{role}" for role in present]
    scope.append(f"{member}:identity:boundary")
    attempt.judge(
        "candidate", outcome="refused" if reasons else "accepted", scope=tuple(scope),
        findings=refusal_findings(reasons, member=member, answered=answered) if reasons else "",
    )
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
