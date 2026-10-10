"""Artifact runs: producing composite artifacts by executing a plan.

A composite artifact is one whose members are typed artifacts made by
separate jobs that must agree. A plan names those jobs; one execution of a
plan, producing one artifact, is an artifact run. A run directory declares
its plan through the metadata `start_run` writes. Each `advance` closes
reported attempts, runs ready code jobs to a fixed point, and hands out
ready model jobs for a coordinator to run.

The core modules ``plan``, ``run``, ``store``, ``handouts`` and ``engine``
schedule, pin, judge and cover; they know nothing of validation, Git or
files outside the store; ``start_run`` expands a compact plan through
``compact``, which derives the structural jobs from the type's layout. The
other modules are what code-job handlers and the coordinator's command
line reuse: standard handlers a plan names directly (``handlers``),
candidate checks and the correction protocol
(``checks``), frozen external sources (``sources``),
journaled effects (``effects``), commit-bound worktrees (``worktree``) and
run reports (``report``). This package exports only the core's public names.

The package never imports a consumer. A consumer such as the agentic-system
analysis supplies handlers and domain rules; its constants (paths, role
names, run naming) arrive as arguments. The design and its vocabulary are in
kb/work/workflow-requirements/.
"""

from commonplace.artifactrun.engine import (
    AttemptResult,
    CodeAttempt,
    Handout,
    RunStatus,
    Stop,
    UncertainEffectError,
    advance,
    current_outputs,
    inspect,
    judge,
    open_handouts,
    run_lock,
    run_values,
    start_run,
)
from commonplace.artifactrun.plan import (
    CodeJob,
    Input,
    ModelJob,
    Plan,
    PlanError,
    load_plan,
)

__all__ = [
    "AttemptResult",
    "CodeAttempt",
    "CodeJob",
    "Handout",
    "Input",
    "ModelJob",
    "Plan",
    "PlanError",
    "RunStatus",
    "Stop",
    "UncertainEffectError",
    "advance",
    "current_outputs",
    "inspect",
    "judge",
    "load_plan",
    "open_handouts",
    "run_lock",
    "run_values",
    "start_run",
]
