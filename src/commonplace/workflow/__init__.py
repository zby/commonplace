"""Workflow engine: one command advances a run directory.

A run directory declares its job set through the metadata `start_run` writes.
Each `advance` closes reported attempts, runs ready code jobs to a fixed
point, and hands out ready model jobs for a coordinator to run. The design
and its vocabulary are in kb/work/workflow-requirements/.
"""

from commonplace.workflow.declaration import (
    CodeJob,
    DeclarationError,
    Input,
    JobSet,
    ModelJob,
    load_job_set,
)
from commonplace.workflow.engine import (
    AttemptResult,
    CodeAttempt,
    Handout,
    RunStatus,
    Stop,
    advance,
    judge,
    start_run,
)

__all__ = [
    "AttemptResult",
    "CodeAttempt",
    "CodeJob",
    "DeclarationError",
    "Handout",
    "Input",
    "JobSet",
    "ModelJob",
    "RunStatus",
    "Stop",
    "advance",
    "judge",
    "load_job_set",
    "start_run",
]
