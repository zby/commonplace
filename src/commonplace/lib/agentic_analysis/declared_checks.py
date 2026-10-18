"""The analysis's declared check: the boundary's source binding.

The standard check calls it with the candidate it built, including the
role's incumbent; it returns refusal findings and reads only inputs the job
declares. Environment guards stay separate from content validation.
"""

from __future__ import annotations

import json

from commonplace.artifactrun.checks import Candidate, source_field
from commonplace.lib.agentic_analysis.analyses import CAPTURE_DIRECTORY
from commonplace.lib.agentic_analysis.boundary import acquired_source, boundary_refusals
from commonplace.lib.agentic_analysis.guards import checkout


def bound_boundary(check: Candidate) -> list[str]:
    """Bind the boundary's source to its run's acquisition and capture directory.

    The boundary fills the plan's frozen-source role, so the standard check
    inspects the candidate's own source only after this binding passes. A
    corrected candidate must also bind to the incumbent's pinned source. The
    run-id is a run identity field, which draft validation checks.
    """
    metadata = json.loads(check.inputs["metadata"])
    repo = checkout(check.run_dir)
    frozen = acquired_source(check.inputs["source"], job="the boundary check")
    # Only an accepted boundary establishes the capture pin. The check's
    # incumbent input preserves it across later corrections without a second source record.
    incumbent_source = source_field(check.incumbent) if check.incumbent is not None else None
    findings = ["[invocation] " + refusal for refusal in boundary_refusals(
        check.data, repo_root=repo, identity=metadata["source-identity"], frozen=frozen,
        capture_directory=check.run_dir / CAPTURE_DIRECTORY,
    )]
    if incumbent_source is not None and incumbent_source != frozen:
        findings += ["[incumbent] " + refusal for refusal in boundary_refusals(
            check.data, repo_root=repo, identity=metadata["source-identity"], frozen=incumbent_source,
        )]
    return findings
