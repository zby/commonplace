"""Archive debugging evidence and reset a job's active dependency closure.

Code handlers with external effects expose a sibling ``reset_<handler>``
context manager. Under its effect locks it yields a preparation callable returning
Replacements. Preparation is read-only; all replacements are snapshotted before
mutation. The context manager also supplies locks during interrupted-reset recovery.
There are no hard-coded consumer imports or worker launches.
"""
from __future__ import annotations

import importlib
import json
import os
import shutil
import uuid
from contextlib import ExitStack
from dataclasses import dataclass
from pathlib import Path

from .engine import _materialize, _run_store
from .plan import CodeJob, ModelJob
from .run import Run
from .store import RunStore, digest

PENDING = ".reset-pending.json"


@dataclass(frozen=True)
class Replacement:
    """Replace a handler-owned path with a copy of source, or remove it.

    Both the original path and source are copied into debugging history before
    anything changes. Inside the run only effects/ may be replaced; other paths
    must be outside the run and must not overlap another replacement.
    """

    path: Path
    source: Path | None = None


def affected_jobs(run: Run, start: str) -> set[str]:
    """Forward dependencies, not correction feedback or optional check context.

    A candidate check's optional role partners are context, not ownership: their
    loss must not discard an upstream author's installed work. Normal readiness
    will recheck that context when it changes. Refusals likewise remain ordinary
    correction-loop inputs rather than reset edges.
    """
    run.jobs.job(start)  # Reject unknown jobs before creating history.
    installers: dict[str, set[str]] = {}
    judges: dict[str, set[str]] = {}
    for judgment in run.judgments:
        role = judgment["subject"]["role"]
        if judgment["job"] == "operator":
            continue
        judges.setdefault(role, set()).add(judgment["job"])
        judging = run.jobs.job(judgment["job"])
        primary = (run.jobs.input_role(judging, "candidate")
                   if "candidate" in judging.inputs else judging.role)
        # A verifier may also re-install its handed subjects. That is feedback,
        # not a forward dependency of every reader of those upstream members.
        if judgment["installs"] and primary == role:
            installers.setdefault(role, set()).add(judgment["job"])

    def fillers(role: str) -> set[str]:
        filler = run.jobs.filler(role)
        return ({filler.name} if filler else set()) | installers.get(role, set())

    dependencies = {}
    for job in run.jobs.jobs:
        parents: set[str] = set()
        for spec in job.inputs.values():
            if spec.address in ("output", "attempt"):
                parents.add(spec.source.partition(":")[0])
            elif spec.address == "handed":
                parents.add(job.inputs[spec.source.partition(":")[0]].source)
            elif spec.address == "role":
                if (isinstance(job, CodeJob) and "candidate" in job.inputs and not spec.required):
                    continue
                if spec.source != job.role:  # An author's incumbent is not a forward edge.
                    parents |= fillers(spec.source)
            elif spec.address == "judgment":
                parents |= fillers(spec.source) | judges.get(spec.source, set())
            elif spec.address == "coverage":
                for role in run.layout.roles:
                    if role != spec.source:
                        parents |= fillers(role) | judges.get(role, set())
        dependencies[job.name] = parents - {job.name}
    affected = {start}
    while True:
        expanded = affected | {name for name, parents in dependencies.items() if parents & affected}
        if expanded == affected:
            return affected
        affected = expanded


def _copy(source: Path, destination: Path) -> None:
    if source.is_symlink():
        raise ValueError(f"reset cannot copy a symlink: {source}")
    if source.is_dir():
        # Never follow links into an unrelated checkout or a live source tree.
        shutil.copytree(source, destination, symlinks=True)
    elif source.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def _replace(source: Path, destination: Path) -> None:
    if destination.is_symlink():
        raise ValueError(f"reset cannot replace a symlink: {destination}")
    RunStore(destination.parent).remove(destination)
    _copy(source, destination)


def _effect_contents(path: Path) -> dict[str, str] | None:
    if path.is_symlink() or path.resolve() != path.absolute():
        raise ValueError(f"reset effect traverses a symlink: {path}")
    if not path.exists():
        return None
    if path.is_file():
        return {".": digest(path.read_bytes())}
    contents = {"/": "directory"}
    for member in path.rglob("*"):
        if member.is_symlink():
            raise ValueError(f"reset effect contains a symlink: {member}")
        if member.is_file():
            contents[member.relative_to(path).as_posix()] = digest(member.read_bytes())
    return contents


def _check_effects(archive: Path, paths: list[str]) -> None:
    # An interruption can leave an absent path or a partially copied/deleted
    # known tree. Never overwrite unrelated bytes introduced before recovery.
    for index, raw in enumerate(paths):
        current = _effect_contents(Path(raw))
        if current is None:
            continue
        states = [_effect_contents(archive / "effects" / str(index) / state) for state in ("before", "next")]
        if not any(state is not None and current.items() <= state.items() for state in states):
            raise ValueError(f"reset effect changed since preparation; preserve pending reset: {raw}")


def reset_run(run_dir: Path, job: str) -> dict:
    """Reset active state, leaving worker launch and advance to the coordinator.

    A pending marker fences ordinary engine operations during application. Calling
    reset again with the same job completes that reset from prepared snapshots;
    it does not take a snapshot of the partial state or rerun effect preparation.
    """
    store = _run_store(Path(run_dir).resolve())
    marker = store.run_dir / PENDING
    with store.lock():
        pending = json.loads(marker.read_text()) if marker.exists() else None
        if pending is not None:
            if pending["job"] != job:
                raise ValueError(f"finish pending reset from {pending['job']} first")
            archive = Path(pending["archive"])
            report = json.loads((archive / "reset.json").read_text())
            # Read the untouched archived run for handler identities and locks.
            run = Run(RunStore(archive / "before"))
            affected = set(report["jobs"])
        else:
            run = Run(store)
            if any(record["state"] == "open" for record in run.attempts.values()):
                raise ValueError("reset requires an idle run; settle all open attempts first")
            latest = {}
            for record in sorted(run.attempts.values(), key=lambda record: record["seq"]):
                latest[record["job"]] = record
            if any(record.get("uncertain") for record in latest.values()):
                raise ValueError("resolve uncertain external effects before resetting the run")
            affected = affected_jobs(run, job)
        with ExitStack() as locks:
            preparations = []
            for declared in run.jobs.jobs:
                if declared.name not in affected or not isinstance(declared, CodeJob):
                    continue
                module, _, name = declared.handler.rpartition(".")
                hook = getattr(importlib.import_module(module), f"reset_{name}", None)
                if hook is not None:
                    # Recovery needs the original run path, not the archive path.
                    preparations.append(locks.enter_context(hook(store.run_dir, declared)))
            if pending is None:
                replacements = [replacement for prepare in preparations for replacement in prepare()]
                paths = [replacement.path.absolute() for replacement in replacements]
                for i, path in enumerate(paths):
                    inside = path.is_relative_to(store.run_dir)
                    effect = path.is_relative_to(store.run_dir / "effects")
                    if (path.resolve() != path or (inside and not effect)
                            or store.run_dir.is_relative_to(path)):
                        raise ValueError(f"unsafe reset effect path: {path}")
                    if any(path.is_relative_to(other) or other.is_relative_to(path) for other in paths[:i]):
                        raise ValueError("reset effect paths overlap")
                archive = store.run_dir.parent / ".reset-history" / store.run_dir.name / uuid.uuid4().hex
                archive.mkdir(parents=True)
                # Nothing active is mutated until every snapshot and next state exists.
                _copy(store.run_dir, archive / "before")
                next_store = RunStore(archive / "next")
                _copy(archive / "before", next_store.run_dir)
                removed = {r["id"] for r in run.attempts.values() if r["job"] in affected}
                roles = {declared.role for declared in run.jobs.jobs if declared.name in affected and declared.role}
                # Operator decisions about reset subjects/bases are not fresh evidence.
                withdrawn = {judgment["id"] for judgment in run.judgments if judgment["attempt"] in removed}
                for judgment in run.judgments:
                    if judgment["job"] == "operator" and (
                        judgment["subject"]["role"] in roles
                        or any(entry["input"]["address"] == "role" and entry["input"]["source"] in roles
                               for entry in judgment["basis"].values())
                        or set(judgment["overrides"]) & withdrawn
                    ):
                        removed.add(judgment["attempt"])
                for attempt in removed:
                    next_store.remove(next_store.attempts / f"{attempt}.json")
                    next_store.remove(next_store.handout_dir(attempt))
                for record in next_store.judgment_records():
                    if record["attempt"] in removed:
                        next_store.remove(next_store.judgments / f"{record['id']}.json")
                # Renew correction budgets without discarding valid upstream outputs.
                floor = max((r["seq"] for r in run.attempts.values()), default=0)
                next_store.write_json(next_store.state / "attempt-budget.json", {
                    declared.name: floor for declared in run.jobs.jobs if isinstance(declared, ModelJob)
                })
                _materialize(Run(next_store))
                for index, replacement in enumerate(replacements):
                    _copy(replacement.path, archive / "effects" / str(index) / "before")
                    if replacement.source is not None:
                        if not replacement.source.exists():
                            raise ValueError(f"reset replacement source is missing: {replacement.source}")
                        _copy(replacement.source, archive / "effects" / str(index) / "next")
                report = {"job": job, "jobs": sorted(affected), "attempts": sorted(removed),
                          "archive": str(archive), "effects": [str(path) for path in paths], "state": "prepared"}
                _check_effects(archive, report["effects"])
                store.write_json(archive / "reset.json", report)
                store.write_json(marker, {"job": job, "archive": str(archive)})
            # Idempotent roll-forward. The marker prevents readers using a partial state.
            _check_effects(archive, report["effects"])
            for index, path in enumerate(report["effects"]):
                _replace(archive / "effects" / str(index) / "next", Path(path))
            for directory in ("attempts", "judgments", "handouts"):
                _replace(archive / "next" / "state" / directory, store.state / directory)
            _replace(archive / "next" / "state" / "attempt-budget.json", store.state / "attempt-budget.json")
            _replace(archive / "next" / "artifact", store.artifact_dir)
            # Keep the lock inode, sequence counter, immutable versions and run identity.
            # _materialize may have added a manifest version to the prepared state.
            for version in (archive / "next" / "state" / "versions").iterdir():
                if not (store.versions / version.name).exists():
                    _copy(version, store.versions / version.name)
            report = {**report, "state": "completed"}
            store.write_json(archive / "reset.json", report)
            os.unlink(marker)
            return report
