"""Code-scheduled workflows.

A program runs a workflow definition, keeps all run state on disk, executes
every step it can, and stops only where it needs a sub-agent. This package
imports nothing from the rest of Commonplace.

The package currently defines the API only. Its tests run on request:

    COMMONPLACE_WORKFLOW_TESTS=1 uv run pytest tests/commonplace/workflow
"""

from commonplace.workflow.engine import (
    REPORT_EVENTS,
    Block,
    Blocked,
    Context,
    Done,
    Handout,
    JobHandle,
    Launch,
    Orchestrator,
    Recognition,
    Report,
    StepResult,
    Uncertain,
    Workflow,
    load_definition,
)
from commonplace.workflow.job import DefinitionError, Job

__all__ = [
    "REPORT_EVENTS",
    "Block",
    "Blocked",
    "Context",
    "DefinitionError",
    "Done",
    "Handout",
    "Job",
    "JobHandle",
    "Launch",
    "Orchestrator",
    "Recognition",
    "Report",
    "StepResult",
    "Uncertain",
    "Workflow",
    "load_definition",
]
