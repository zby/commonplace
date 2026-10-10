"""Read-only inspection of an engine run and its effect journals.

This is an operator view, not a typed member or a recovery decision.
Effect journals are reported as evidence only; the effect's handler must
recognize their exact filesystem outcome before completing a failed attempt.
"""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from commonplace.artifactrun import RunStatus, current_outputs, inspect, run_lock
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore


def run_inspection(run_dir: Path, *, final_job: str, status: RunStatus | None = None) -> dict:
    """Report attempts, refusals, stops and effects without running jobs.

    The run is completed when it is publishable and ``final_job`` has a
    current completion.
    """
    run_dir = Path(run_dir).resolve()
    if not (run_dir / "run.json").exists():
        raise ValueError("inspection requires an engine run's run.json")
    with run_lock(run_dir):
        view = inspect(run_dir)
        failures = [asdict(stop) for stop in view["failed_attempts"]]
        stops = [asdict(stop) for stop in status.stops] if status is not None else []
        exhausted = view["exhausted_jobs"]
        effects = {}
        for path in sorted((run_dir / "effects").glob("*.json")):
            try:
                if path.resolve() != path:
                    raise ValueError("journal redirects outside its declared path")
                record = json.loads(path.read_bytes())
                if not isinstance(record, dict):
                    raise TypeError("journal is not an object")
                effects[path.stem] = {"journal-state": record.get("state"), "verified": False}
            except (OSError, ValueError, TypeError) as error:
                effects[path.stem] = {"error": str(error), "verified": False}
        uncertain = any(stop["uncertain"] for stop in [*failures, *stops])
        state = "uncertain" if uncertain else "stopped" if (failures or stops or exhausted) else "running"
        waiting: dict[str, list[str]] = {}
        if state == "running" and view["condition"] == "stuck":
            # The engine found no open attempt and no ready job: say what each
            # unfinished job lacks, so nobody waits for progress that cannot come.
            state = "stuck"
            waiting = _waiting_on(run_dir)
        if (state == "running" and view["condition"] == "publishable"
                and current_outputs(run_dir, final_job) is not None):
            state = "completed"
        return {
            "format": "commonplace-engine-run-inspection-v1", "run-id": run_dir.name,
            "state": state, "artifact": str(run_dir / "artifact"), "publishable": view["publishable"],
            "waiting-on": waiting,
            "parameters": view["parameters"], "members": view["members"],
            "open-attempts": view["open_attempts"], "failed-attempts": failures,
            "invocation-stops": stops, "exhausted-jobs": exhausted,
            "stale-acceptances": view["stale_acceptances"], "canonical-peer-drift": view["historical_bases"],
            "refusals": [asdict(item) for item in view["refusals"]],
            "attempts": view["attempts"],
            "effects": effects,
            "limitations": [
                "Publishable means engine coverage (required roles, holding acceptances, covered relations), not publication or content validation.",
                "Completed means the final job completed against unchanged inputs, not a fresh filesystem audit.",
                "Holding handed judgments can refer to historical peers; canonical-peer-drift reports that separately.",
                "Reporting does not change logical run state; acquiring its lock may create state/lock.",
                "Journal state is unverified; only the effect handler recognizes completion.",
                "Invocation scheduling stops require the supplied RunStatus; they are not reconstructed.",
            ],
        }


def render_run_inspection(run_dir: Path, *, final_job: str, status: RunStatus | None = None) -> str:
    """Render the run inspection as JSON."""
    return json.dumps(run_inspection(run_dir, final_job=final_job, status=status), indent=2, sort_keys=True) + "\n"


def _waiting_on(run_dir: Path) -> dict[str, list[str]]:
    """For each job without a current completion, the required inputs that resolve to nothing."""
    run = Run(RunStore(run_dir))
    waiting = {}
    for job in run.jobs.jobs:
        if run.latest_completed(job.name) is not None:
            continue
        absent = [name for name, spec in job.inputs.items()
                  if spec.required and run.resolve(name, job.inputs).version is None]
        if absent:
            waiting[job.name] = absent
    return waiting
