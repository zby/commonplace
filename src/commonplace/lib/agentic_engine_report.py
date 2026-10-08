"""Read-only new-engine reports, separate from legacy round/completion state.

This is an operator report, not a typed retained member or a recovery decision.
Publication journals are reported as evidence only; the effect handler must
recognize their exact filesystem outcome before completing a failed attempt.
"""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from commonplace.workflow import RunStatus
from commonplace.workflow.engine import inspect
from commonplace.workflow.state import Run
from commonplace.workflow.store import RunStore


def engine_run_report(run_dir: Path, *, status: RunStatus | None = None) -> dict:
    """Report engine attempts, identity, refusals and stops without running jobs."""
    run_dir = Path(run_dir).resolve()
    if any((run_dir / name).exists() for name in ("workflow-state", "output", "opening.json")):
        raise ValueError("new-engine reporting rejects legacy/mixed run directories")
    store = RunStore(run_dir)
    if not store.metadata.exists():
        raise ValueError("new-engine reporting requires run.json; legacy state is not converted")
    with store.lock():
        view = inspect(run_dir)
        run = Run(store)
        attempts = sorted(run.attempts.values(), key=lambda r: r["seq"])
        failures = [asdict(stop) for stop in view["failed_attempts"]]
        stops = [asdict(stop) for stop in status.stops] if status is not None else []
        exhausted = [job.name for job in run.jobs.jobs
                     if getattr(job, "max_attempts", None) is not None
                     and run.attempt_count(job.name) >= job.max_attempts
                     and run.ready(job, run.permitted())]
        stale = [judgment["id"] for judgment in run.judgments
                 if judgment["outcome"] == "accepted" and not run.holds(judgment)]
        drift = []
        members = run.members()
        for judgment in run.judgments:
            if judgment["outcome"] != "accepted" or not run.holds(judgment):
                continue
            basis = judgment["basis"]
            for name, entry in basis.items():
                spec = entry["input"]
                if spec["address"] != "handed":
                    continue
                alias, _, handed = spec["source"].partition(":")
                producer = run.jobs.job(basis[alias]["input"]["source"])
                original = producer.inputs.get(handed)
                if (original is not None and original.address == "member"
                        and entry["version"] != members.get(original.source)):
                    drift.append({"judgment": judgment["id"], "input": name,
                                  "role": original.source, "handed": entry["version"],
                                  "current": members.get(original.source)})
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
        publication = next((job for job in run.jobs.jobs
                            if getattr(job, "handler", None)
                            == "commonplace.lib.agentic_job_publication.publish_analysis"), None)
        if (state == "running" and publication is not None and view["publishable"]
                and not view["open_attempts"] and run.latest_completed(publication.name) is not None
                and not run.ready(publication, run.permitted())):
            state = "completed"
        return {
            "format": "commonplace-engine-run-report-v1", "run-id": run_dir.name,
            "state": state, "set": str(run_dir / "set"), "publishable": view["publishable"],
            "parameters": dict(run.parameters), "members": view["members"],
            "open-attempts": view["open_attempts"], "failed-attempts": failures,
            "invocation-stops": stops, "exhausted-jobs": exhausted,
            "stale-acceptances": stale, "canonical-peer-drift": drift,
            "refusals": [asdict(item) for item in view["refusals"]],
            "attempts": [{key: record.get(key) for key in
                          ("id", "job", "kind", "state", "model", "effort", "reason", "uncertain")}
                         for record in attempts],
            "effects": effects,
            "limitations": [
                "Publishable means engine relation coverage, not publication or content validation.",
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
