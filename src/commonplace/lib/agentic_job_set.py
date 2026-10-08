"""Fail-closed bindings for the opt-in analysis migration declaration.

The job set is library data beside the job instructions, not generated Python.
No live workflow or CLI uses it yet. Opening/acquisition, boundary and analyst
hand-outs are ported. The specialist checks remain unbound to prevent handing
out unported reconciliation instructions.
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
        "working set path: legacy consumers use output/, new-engine runs use set/; port consumers before switching",
        "worker protocol: boundary and analysts are translated; port reconciliation, verification, profile and synthesis interfaces",
        "run-state: project new-engine attempts/stops and uncertain external effects",
        "publication: enforce disposition-dependent holding acceptance coverage, preserve incumbent checks and effect recovery",
        "analyst check bindings: memory/epistemic implemented; keep unbound until reconciliation hand-outs are translated",
        "handlers: reconciliation/profile/synthesis checks, set checks, verdict application and assembly remain unported",
        "coverage: assembly/publication handlers must enforce disposition-dependent whole-set coverage",
        "memory provenance: implement the workflow check promised by the set type or remove the promise",
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
    gaps.append("set relations: decide how overview amendment-index and synthesis limit checks enter coverage")
    return tuple(gaps)
