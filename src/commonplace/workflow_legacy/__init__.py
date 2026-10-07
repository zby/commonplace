"""Code-scheduled workflows: the engine the analysis workflow still runs on.

# BACKCOMPAT: analyse-agentic-system runs on this engine - remove after the
# analysis workflow runs on commonplace.workflow (kb/work/workflow-requirements).


A program runs a workflow definition, keeps all run state on disk, executes
every step it can, and stops only where it needs a sub-agent. This package
imports nothing from the rest of Commonplace.

The shell is the `commonplace-workflow` command (`commonplace.workflow_legacy.shell`);
see its module docstring.
"""

from commonplace.workflow_legacy.engine import (
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
    RunBusy,
    StateError,
    StepResult,
    StopRun,
    Uncertain,
    Workflow,
    load_definition,
)
from commonplace.workflow_legacy.job import DefinitionError, Job

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
    "RunBusy",
    "StateError",
    "StepResult",
    "StopRun",
    "Uncertain",
    "Workflow",
    "load_definition",
]
