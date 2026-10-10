"""The analysis's declared check: the boundary's source binding.

The standard check calls it with the candidate it built, including the
role's incumbent; it returns refusal findings and reads only inputs the job
declares. Environment guards stay separate from content validation.
"""

from __future__ import annotations

import json
from pathlib import Path

from commonplace.artifactrun.checks import Candidate
from commonplace.lib.agentic_analysis.boundary import boundary_refusals
from commonplace.lib.agentic_analysis.opening import locate
from commonplace.lib.note_parser import parse_document


def bound_boundary(check: Candidate) -> list[str]:
    """Bind the boundary's source to its run's acquisition and capture directory.

    The boundary fills the plan's frozen-source role, so the standard check
    inspects the candidate's own source only after this binding passes. A
    corrected candidate must also bind to the incumbent's pinned source. The
    run-id is a run-bound identity field, which draft validation checks.
    """
    attempt = check.attempt
    metadata, repo = locate(attempt)
    frozen = json.loads(attempt.read("source"))
    if frozen is not None and (not isinstance(frozen, dict) or frozen.get("kind") != "git"):
        raise ValueError("boundary check requires a Git source object or explicit JSON null")
    # Only an accepted boundary establishes the capture pin. The check's
    # incumbent input preserves it across later corrections without a second source record.
    incumbent_bytes = check.incumbent
    incumbent_source = None
    if incumbent_bytes is not None:
        incumbent, error = parse_document(incumbent_bytes.decode("utf-8"))
        if incumbent is None or error:
            raise ValueError("boundary check cannot read the incumbent boundary")
        incumbent_source = (incumbent.frontmatter or {}).get("source")
    findings = ["[invocation] " + refusal for refusal in boundary_refusals(
        check.data, repo_root=repo, identity=metadata["source-identity"], frozen=frozen,
        capture_directory=Path(metadata["capture-directory"]),
    )]
    if incumbent_source is not None and incumbent_source != frozen:
        findings += ["[incumbent] " + refusal for refusal in boundary_refusals(
            check.data, repo_root=repo, identity=metadata["source-identity"], frozen=incumbent_source,
        )]
    return findings
