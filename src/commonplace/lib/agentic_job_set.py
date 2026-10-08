"""Fail-closed bindings for the opt-in analysis migration declaration.

The job set is library data beside the job instructions, not generated Python.
No live workflow or CLI uses it yet. All model hand-outs and consumer handlers
are declared. Coherence review is retained in the workshop; production routing
and full-pipeline evidence remain separate adoption work. Binding grants no run authority.
"""

from __future__ import annotations

from pathlib import Path

from commonplace.lib.agentic_set import SET_TYPE
from commonplace.lib.directory_layout import parse_layout
from commonplace.lib.note_parser import parse_document

JOB_SET = "agentic-system-analyses/instructions/analyse-agentic-system/job-set.yaml"
REPORTS = ("runtime", "memory", "epistemic")
RECORDS = (*REPORTS, "reconciliation")
MODEL_ROLES = {
    "boundary": "boundary",
    "runtime": "runtime",
    "memory": "memory",
    "epistemic": "epistemic",
    "reconcile": "reconciliation",
    "verify": "record-verification",
    "profile": "memory-profile",
    "verify-profile": "profile-verification",
    "synthesize": "synthesis",
    "verify-synthesis": "synthesis-verification",
}
HANDLER = "commonplace.lib.agentic_job_set.unported"
OPEN_HANDLER = "commonplace.lib.agentic_job_handlers.open_analysis"
ACQUIRE_HANDLER = "commonplace.lib.agentic_job_handlers.acquire_analysis"
BOUNDARY_CHECK_HANDLER = "commonplace.lib.agentic_job_handlers.check_boundary"
ANALYST_CHECK_HANDLERS = {
    member: f"commonplace.lib.agentic_job_handlers.check_{member}" for member in REPORTS
}


def unported(_attempt):
    """Never turn a migration placeholder into a successful attempt."""
    raise NotImplementedError(
        "analysis job-set migration: remaining code handlers are not ported; "
        "do not launch workers or publish from this declaration"
    )


def contract_gaps(library: Path) -> tuple[str, ...]:
    """Name adoption blockers, not permission to run the declaration."""
    document, error = parse_document((library / SET_TYPE).read_text(encoding="utf-8"))
    if document is None or error:
        raise ValueError(f"cannot read analysis set type: {error}")
    layout = parse_layout(document.frontmatter["layout"], where=SET_TYPE)
    gaps = [
        "working set path: legacy consumers use output/, new-engine runs use set/; select formats explicitly before switching",
        "live routing: skill/CLI remain legacy; opt-in handler bindings are not production adoption",
        "verification: coherence review completed; end-to-end proof omitted at the operator's request, not established by fixture counts",
        "reporting: use engine attempts/stops and uncertain-effect reports, never manufacture legacy run-state",
        "publication coordination: shared repository locks serialize cooperating publishers; exclude non-cooperating writers",
        "publication policy: non-complete sets finish locally; public replacement requires an explicit consumer/type decision",
        "worker provenance: the retained manifest permits one identical worker identity, not heterogeneous role workers",
        "legacy runs: opening rejects legacy state; keep legacy consumers intact until an explicit retirement",
        "startup: port run allocation and binding checks in preparation/CLI consumers before a production switch",
    ]
    if layout.required.by_role != "boundary":
        gaps.append("disposition: the layout discriminator must be available before overview assembly")
    for verifier, subjects in (
        ("record-verification", RECORDS),
        ("profile-verification", ("memory-profile",)),
        ("synthesis-verification", ("synthesis",)),
    ):
        for subject in subjects:
            if subject not in layout.roles[verifier].cites:
                gaps.append(f"missing verdict relation: {verifier}:cites:{subject}")
    gaps.append(
        "set relations: amendment-index and carried limits remain content checks, not new engine relation kinds"
    )
    return tuple(gaps)
