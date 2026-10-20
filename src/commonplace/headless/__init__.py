"""Workflows as Python scripts over harnesses' headless modes, run through Workjig.

`jobs` is the one agent call, a chain of Workjig calls replayed from the run's
records; `harness` turns a worker profile into a Workjig command worker for
`claude -p`, `codex exec` or `pi -p`; `corrections` is a producer's attempts
at one output under the analysis correction protocol. The
analyse-agentic-system workflow written over them is
`commonplace.lib.agentic_analysis.workflow`.
"""
