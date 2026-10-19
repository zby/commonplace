"""Workflows as Python scripts over harnesses' headless modes.

`jobs` is the one agent call and its content-keyed cache; `harness` launches
a worker profile through `claude -p`, `codex exec` or `pi -p`; `corrections`
is a producer's attempts at one output under the analysis correction
protocol. The analyse-agentic-system workflow written over them is
`commonplace.lib.agentic_analysis.workflow`.
"""
