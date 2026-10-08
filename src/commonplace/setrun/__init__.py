"""Running a typed set on the workflow engine: the parts any consumer reuses.

The engine (``commonplace.workflow``) schedules, pins, judges and covers; it
knows nothing of validation, Git or files outside its store. A consumer such
as the agentic-system analysis supplies handlers and domain rules. Between
them sit candidate checks and the correction protocol (``checks``), frozen
external sources (``sources``), journaled effects (``effects``), commit-bound
worktrees (``isolation``) and run reports (``report``).

This package depends on the engine and ``commonplace.lib``, never on a
consumer. Consumer constants (paths, role names, run naming) arrive as
arguments.
"""
