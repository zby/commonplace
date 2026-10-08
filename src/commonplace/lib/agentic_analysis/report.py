"""Read-only new-engine reports, separate from legacy round/completion state.

This is an operator report, not a typed retained member or a recovery decision.
Publication journals are reported as evidence only; the effect handler must
recognize their exact filesystem outcome before completing a failed attempt.
"""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from commonplace.workflow import RunStatus, current_outputs, inspect, run_lock

PUBLISH_JOB = "publish"


def engine_run_report(run_dir: Path, *, status: RunStatus | None = None) -> dict:
    """Report engine attempts, identity, refusals and stops without running jobs."""
    run_dir = Path(run_dir).resolve()
    if any((run_dir / name).exists() for name in ("workflow-state", "output", "opening.json")):
        raise ValueError("new-engine reporting rejects legacy/mixed run directories")
    if not (run_dir / "run.json").exists():
        raise ValueError("new-engine reporting requires run.json; legacy state is not converted")
    with run_lock(run_dir):
        view = inspect(run_dir)
        failures = [asdict(stop) for stop in view["failed_attempts"]]
        stops = [asdict(stop) for stop in status.stops] if status is not None else []
        exhausted = view["exhausted_jobs"]
        effects = {}
        for name in ("acquire", "publish"):
            path = run_dir / "effects" / f"{name}.json"
            if path.exists() or path.is_symlink():
                try:
                    if path.resolve() != path:
                        raise ValueError("journal redirects outside its declared path")
                    record = json.loads(path.read_bytes())
                    if not isinstance(record, dict):
                        raise TypeError("journal is not an object")
                    effects[name] = {"journal-state": record.get("state"), "verified": False}
                except (OSError, ValueError, TypeError) as error:
                    effects[name] = {"error": str(error), "verified": False}
        uncertain = any(stop["uncertain"] for stop in [*failures, *stops])
        state = "uncertain" if uncertain else "stopped" if (failures or stops or exhausted) else "running"
        if (state == "running" and view["condition"] == "publishable"
                and current_outputs(run_dir, PUBLISH_JOB) is not None):
            state = "completed"
        return {
            "format": "commonplace-engine-run-report-v1", "run-id": run_dir.name,
            "state": state, "set": str(run_dir / "set"), "publishable": view["publishable"],
            "parameters": view["parameters"], "members": view["members"],
            "open-attempts": view["open_attempts"], "failed-attempts": failures,
            "invocation-stops": stops, "exhausted-jobs": exhausted,
            "stale-acceptances": view["stale_acceptances"], "canonical-peer-drift": view["historical_bases"],
            "refusals": [asdict(item) for item in view["refusals"]],
            "attempts": view["attempts"],
            "effects": effects,
            "limitations": [
                "Publishable means engine coverage (required roles, holding acceptances, covered relations), not publication or content validation.",
                "Completed means the bound publication job completed against unchanged inputs, not a fresh filesystem audit.",
                "Holding handed judgments can refer to historical peers; canonical-peer-drift reports that separately.",
                "Reporting does not change logical run state; acquiring its lock may create state/lock.",
                "Journal state is unverified; only the effect handler recognizes completion.",
                "Invocation scheduling stops require the supplied RunStatus; they are not reconstructed.",
                "No legacy rounds or typed legacy run-state are inferred.",
            ],
        }


def render_engine_run_report(run_dir: Path, *, status: RunStatus | None = None) -> str:
    """Render the separate engine report as JSON; never write a legacy run-state."""
    return json.dumps(engine_run_report(run_dir, status=status), indent=2, sort_keys=True) + "\n"
