"""The agentic-system analysis: its workflow, lifecycle, checks and retained data.

``workflow`` runs the method's plan over headless harness workers with the
primitives in ``commonplace.headless``; ``worktree`` and ``preparation``
allocate, pin, inspect and integrate runs in prepared worktrees;
``opening``, ``sources``, ``checks``, ``verification``, ``declared_checks``,
``boundary`` and ``publication`` are the domain rules the workflow calls
with plain values. The ``analyses``, ``records`` and ``ledger`` modules
provide artifact contracts and retained-data validation without importing
the workflow.
"""
