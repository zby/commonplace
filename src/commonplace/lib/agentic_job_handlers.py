"""Ported analysis code jobs; the opt-in declaration binds them one at a time.

Opening is read-only outside the engine's attempt commit. Acquisition owns its
external-effect journal, but stays unbound until boundary hand-outs are ported.
Checks, verdict application, assembly and publication are still fail-closed.
This module does not switch the live analysis workflow or reinterpret its state.
"""

from __future__ import annotations

import datetime
import json
import re
import subprocess
from pathlib import Path

from commonplace.lib.agentic_acquisition import acquire_source
from commonplace.lib.agentic_checkout import github_checkout_path
from commonplace.lib.agentic_publication import (
    inspect_destination,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_set import (
    RETAINED_ROOT,
    analysis_layout,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.analysis_worktree import (
    STATE_ROOT,
    preparation_for,
    require_run_code,
    source_checkout,
)
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

    Legacy state is rejected here, not converted. It remains resumable through
    its own workflow and command environment until a later explicit retirement.
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
    legacy = [name for name in ("workflow-state", "output", "opening.json") if (run_dir / name).exists()]
    if legacy:
        raise ValueError(
            "legacy analysis state cannot be opened by the new engine: " + ", ".join(legacy)
            + "; resume it with its legacy workflow, or start a separate new-engine run"
        )
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
        "review-path": destination,
        "expected-incumbent-sha256": str(incumbent["expected_incumbent_sha256"]),
    }
    return {"metadata": (json.dumps(record, indent=2) + "\n").encode("utf-8")}


def acquire_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Acquire from pinned opening metadata without launching an analyst.

    This handler is tested with a code-only declaration. Keep the production
    binding fail-closed until the next model job's hand-out is ported too.
    Git results are frozen source objects; JSON null means the boundary still
    has to establish a non-Git capture, not that a source check succeeded.
    """
    metadata_bytes = attempt.read("metadata")
    if metadata_bytes is None:
        raise ValueError("acquisition requires the opening metadata")
    metadata = json.loads(metadata_bytes)
    if not isinstance(metadata, dict) or metadata.get("run-id") != attempt.run_dir.name:
        raise ValueError("acquisition opening metadata must name this run")
    repo = source_checkout(attempt.run_dir)
    if repo is None or attempt.run_dir.parent != repo / STATE_ROOT or attempt.library != repo / "kb":
        raise ValueError("acquisition must use this run's analysis checkout and recorded library")
    require_run_code(attempt.run_dir, cwd=Path.cwd())
    commit = metadata.get("inputs-commit")
    preparation = preparation_for(repo)
    if metadata["run-id"].rsplit("-", 2)[-2:-1] != [preparation["token"]]:
        raise ValueError("acquisition preparation token differs from the opened run")
    if _head(repo) != commit or preparation.get("commit") != commit:
        raise ValueError("acquisition worktree differs from the opened preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)
    source = acquire_source(repo, attempt.run_dir, metadata_bytes)
    if _head(repo) != commit:
        raise ValueError("analysis worktree HEAD changed during acquisition")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)
    return {"source": source}
