"""Bindings for the collection-owned analysis job declaration.

The job set is library data beside the job instructions, not generated Python.
Binding handlers grants no authority to run workers or publish analyses.
"""

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
OPEN_HANDLER = "commonplace.lib.agentic_analysis.handlers.open_analysis"
ACQUIRE_HANDLER = "commonplace.lib.agentic_analysis.handlers.acquire_analysis"
BOUNDARY_CHECK_HANDLER = "commonplace.lib.agentic_analysis.handlers.check_boundary"
ANALYST_CHECK_HANDLERS = {
    member: f"commonplace.lib.agentic_analysis.handlers.check_{member}" for member in REPORTS
}
