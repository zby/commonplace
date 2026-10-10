"""The analysis's declared checks: the boundary binding and the analyst checks.

The standard check calls each with the candidate it built; each returns
refusal findings and reads only inputs its plan entry declares. Environment
guards stay separate from content validation.
"""

from __future__ import annotations

import json
from pathlib import Path

from commonplace.artifactrun.checks import Candidate
from commonplace.lib.agentic_analysis.boundary import boundary_refusals
from commonplace.lib.agentic_analysis.opening import locate
from commonplace.lib.agentic_analysis.records import declared_ids
from commonplace.lib.note_parser import parse_document


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
    findings = ["[invocation] " + refusal for refusal in boundary_refusals(
        check.data, repo_root=repo, run_id=metadata["run-id"],
        identity=metadata["source-identity"], frozen=frozen,
        capture_directory=Path(metadata["capture-directory"]),
    )]
    if incumbent_source is not None and incumbent_source != frozen:
        findings += ["[incumbent] " + refusal for refusal in boundary_refusals(
            check.data, repo_root=repo, run_id=metadata["run-id"],
            identity=metadata["source-identity"], frozen=incumbent_source,
        )]
    return findings


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
