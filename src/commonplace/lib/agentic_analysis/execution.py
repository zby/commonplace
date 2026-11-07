"""Pinned-child entry points and machine-readable execution outcomes.

The coordinator invokes these through the prepared command, never by importing
another worktree's workflow into its own process.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis.durable import save
from commonplace.lib.agentic_analysis.preparation import require_run_code
from commonplace.lib.agentic_analysis.worktree import (
    STATE_ROOT,
    allocation_path,
    inspect_analysis,
    start_analysis,
)


def outcome(view: dict) -> str:
    audit = view.get("advisory-audit") or {}
    if (view.get("uncertain") or view.get("unsettled-launches") or view["state"] in ("running", "interrupted")
            or view.get("stop-type") in ("UncertainEffectError", "UncertainLaunchError", "RecordError")
            or audit.get("unsettled-launches") or audit.get("state") in ("running", "interrupted")):
        return "operator-attention"
    if view.get("command-failed"):
        return "command-failed"
    return {"published": "published", "local": "local-complete", "stopped": "stopped",
            "allocated": "allocated", "withdrawn": "stopped"}.get(view["state"], "operator-attention")


def inspect_execution(worktree: Path, key: str) -> dict:
    require_run_code(worktree, cwd=Path.cwd())
    journal = allocation_path(worktree, key)
    result_path = journal.with_suffix(".result.json")
    binding = json.loads(journal.read_text()) if journal.is_file() else None
    view = None
    if binding is not None:
        run = worktree / STATE_ROOT / binding["run-id"]
        if run.parent != worktree / STATE_ROOT or run.is_symlink():
            raise ValueError("invalid execution allocation path")
        if (run / "parameters.json").is_file():
            view = inspect_analysis(run)
    return {"allocation": binding, "inspection": view,
            "result": json.loads(result_path.read_text()) if result_path.is_file() else None}


def execute(worktree: Path, key: str, *, parameters: dict, timeout: float, max_workers: int) -> int:
    from commonplace.lib.agentic_analysis.workflow import run_analysis

    require_run_code(worktree, cwd=Path.cwd())
    result_path = allocation_path(worktree, key).with_suffix(".result.json")
    code, error, view = 1, None, None
    try:
        run = start_analysis(worktree, **parameters, allocation_key=key)
        receipt = run_analysis(run, timeout=timeout, max_workers=max_workers)
        code = 2 if receipt is None else 0
    except Exception as exc:  # noqa: BLE001 - preserve command failure alongside the worker evidence
        error = f"{type(exc).__name__}: {exc}"
        print(error, file=sys.stderr)
    try:
        view = inspect_execution(worktree, key)["inspection"]
    except Exception as exc:  # noqa: BLE001 - unreadable evidence is not success
        error = f"{error or ''}; inspection failed: {type(exc).__name__}: {exc}"
    status = outcome(view) if view is not None else "command-failed"
    if error and status != "operator-attention":
        status = "command-failed"
    result = {"schema": "commonplace.analysis-execution.v1", "allocation-key": key,
              "status": status, "exit-code": code, "error": error, "inspection": view}
    save(result_path, result)
    print(json.dumps(result, indent=2))
    return code
