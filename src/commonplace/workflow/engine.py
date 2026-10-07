"""Start a run and advance it: the engine behind kb/work/workflow-requirements.

One invocation closes the attempts the coordinator reports, runs ready code
jobs to a fixed point, and opens attempts for ready model jobs. This module
owns those transitions; `state.py` interprets the records, `handouts.py`
prepares worker prompts, and `store.py` owns how records are committed.

Words follow the workshop glossary: an input resolves to a version by its
address; an attempt pins its inputs; a judgment accepts or refuses one subject
version with its inputs as basis and declared relations as scope; a member is
the version an installing acceptance put in a role.
"""

from __future__ import annotations

import traceback
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.library import library_root

from .declaration import CodeJob, Input, ModelJob, load_job_set
from .handouts import Handout, _open, handout_for
from .state import CodeAttempt, Resolved, Run, _parse_type
from .store import RunStore, digest

MAX_CODE_RUNS = 10_000


# Public records


@dataclass(frozen=True)
class AttemptResult:
    """An attempt result closes one open model attempt as completed or failed."""

    attempt: str
    outcome: str = "completed"
    reason: str = ""
    model: str | None = None
    effort: str | None = None


@dataclass(frozen=True)
class Stop:
    """A stop names the job and attempt that ended the invocation."""

    reason: str
    job: str | None = None
    attempt: str | None = None


@dataclass(frozen=True)
class RunStatus:
    """The run status lists hand-outs, open attempts, stops and publishability."""

    handouts: tuple[Handout, ...]
    open_attempts: tuple[str, ...]
    stops: tuple[Stop, ...]
    publishable: bool


# Operations


def start_run(run_dir: Path, job_set: Path, *, parameters: Mapping[str, str] | None = None) -> None:
    """Start a run: write metadata naming the job set and the run parameters."""
    store = RunStore(Path(run_dir))
    if store.metadata.exists():
        raise FileExistsError(f"{run_dir} already holds a run")
    declaration = Path(job_set).read_text(encoding="utf-8")
    type_spec = load_job_set(declaration).type_spec
    type_text = (library_root() / type_spec).read_text(encoding="utf-8")
    layout, _ = _parse_type(type_text, str(type_spec))
    jobs = load_job_set(declaration, layout.roles)
    given = dict(parameters or {})
    missing = sorted({name for job in jobs.jobs if isinstance(job, ModelJob)
                      for name in job.run_parameters()} - set(given))
    if missing:
        raise ValueError(f"the job set substitutes run parameters not given: {', '.join(missing)}")
    store.create({
        "job_set": str(Path(job_set).resolve()),
        "declaration": declaration,
        "type_spec": str(type_spec),
        "type": type_text,
        "parameters": dict(parameters or {}),
    })


def advance(run_dir: Path, *, results: tuple[AttemptResult, ...] = ()) -> RunStatus:
    """Run one invocation over the run directory and return its run status."""
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    with store.lock():
        run = Run(store)
        stops = [stop for result in results if (stop := _close(run, result)) is not None]
        run.reload()
        _sweep(run)
        if stops:
            return _status(run, (), stops)
        stop = _run_code_jobs(run)
        if stop is not None:
            return _status(run, (), [stop])
        handouts, stops = _open_model_attempts(run)
        return _status(run, handouts, stops)


def open_handouts(run_dir: Path) -> tuple[Handout, ...]:
    """The hand-outs of every open attempt, for a coordinator that lost them."""
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    with store.lock():
        run = Run(store)
        return tuple(handout_for(run, record) for record in
                     sorted(run.attempts.values(), key=lambda r: r["seq"]) if record["state"] == "open")


def judge(
    run_dir: Path,
    *,
    role: str,
    outcome: str,
    version: str | None = None,
    scope: tuple[str, ...] = (),
    findings: str = "",
    overrides: tuple[str, ...] = (),
    basis: tuple[str, ...] = (),
) -> str:
    """Record an operator's judgment of a role's member and return its id.

    The subject is the role's current member unless `version` names an
    earlier one, which is then evidence only. `basis` names further roles
    whose current members the judgment rests on; a scoped relation needs
    its partner among them. The record is the same as a code job's: an
    attempt by the job `operator`, completed, with the judgment inside.
    """
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    with store.lock():
        run = Run(store)
        if role not in run.layout.roles:
            raise ValueError(f"the type declares no role {role}")
        subject = version or run.members().get(role)
        if subject is None:
            raise ValueError(f"role {role} has no member to judge")
        if not (store.versions / subject).is_file():
            raise ValueError(f"no version {subject} in this run")
        filler = run.jobs.filler(role)
        if outcome == "refused" and not isinstance(filler, ModelJob):
            raise ValueError(f"role {role} is filled by no model job, so nothing can answer a refusal of it")
        inputs = {"subject": Input("member", role)}
        pins = {"subject": Resolved(subject, store.get(subject), role, filler.name if filler else None)}
        for other in basis:
            inputs[other] = Input("member", other)
            pins[other] = run.resolve(other, inputs)
            if pins[other].version is None:
                raise ValueError(f"role {other} has no member to rest on")
        seq = store.next_seq()
        attempt = f"{seq:06d}-operator"
        code_attempt = CodeAttempt(run, CodeJob("operator", inputs, (), "operator"), pins)
        code_attempt.judge("subject", outcome=outcome, scope=scope, findings=findings, overrides=overrides)
        judgments = code_attempt.judgments({}, seq, attempt)
        store.commit_attempt({
            "id": attempt, "seq": seq, "job": "operator", "kind": "operator",
            "pins": {name: pinned.pin() for name, pinned in pins.items()}, "outputs": {},
        }, judgments)
        return judgments[0]["id"]


@dataclass(frozen=True)
class RefusalInForce:
    """A refusal that currently makes its producer ready: what `status` lists."""

    id: str
    job: str
    role: str | None
    version: str
    findings: str


def inspect(run_dir: Path) -> dict:
    """A read-only view of a run: members, open attempts, refusals in force, publishability."""
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    run = Run(store)
    refusals = []
    for job in run.jobs.jobs:
        if not isinstance(job, ModelJob):
            continue
        resolved = run.resolve("refusal", {"refusal": Input("refusal", job.name, required=False)})
        if resolved.version is None:
            continue
        output = run.latest_output(job)
        latest = [j for j in run.judgments if j["outcome"] == "refused"
                  and j["subject"]["producer"] == job.name and j["subject"]["version"] == output][-1]
        refusals.append(RefusalInForce(latest["id"], job.name, job.role, output or "", latest["findings"]))
    return {
        "members": dict(run.members()),
        "open_attempts": sorted(r["id"] for r in run.attempts.values() if r["state"] == "open"),
        "refusals": refusals,
        "publishable": run.publishable(),
    }


def _status(run: Run, handouts, stops) -> RunStatus:
    run.reload()
    _materialize(run)
    opened = tuple(sorted(r["id"] for r in run.attempts.values() if r["state"] == "open"))
    return RunStatus(tuple(handouts), opened, tuple(stops), run.publishable())


def _close(run: Run, result: AttemptResult) -> Stop | None:
    store = run.store
    record = run.attempts.get(result.attempt)
    if record is None:
        raise ValueError(f"no attempt {result.attempt} in this run")
    if record["state"] != "open":
        return None  # Repeated results are idempotent.
    job = run.jobs.job(record["job"])
    directory = store.handout_dir(record["id"])
    problem_path = directory / "problem.md"
    problem = problem_path.read_text(encoding="utf-8", errors="replace") if problem_path.is_file() else ""

    def fail(reason: str) -> Stop:
        # The worker's problem text is the failure's record; the hand-out
        # directory it was written in does not survive the attempt.
        if problem.strip():
            reason = f"{reason}; the worker wrote: {problem.strip()}"
        store.fail_attempt(record, reason, problem=problem, model=result.model, effort=result.effort)
        store.remove(directory)
        return Stop(reason, job.name, record["id"])

    if result.outcome == "failed":
        return fail(result.reason or "the coordinator reported a failure")
    if result.outcome != "completed":
        raise ValueError(f"outcome must be completed or failed, not {result.outcome!r}")
    outputs = {}
    for name in job.outputs:
        path = directory / "outputs" / f"{name}.md"
        if path.is_file():
            outputs[name] = store.put(path.read_bytes())
    if job.outputs[0] not in outputs:
        return fail("the worker reported a problem" if problem.strip() else "completed without its primary output")
    for name, spec in job.inputs.items():
        pinned = record["pins"].get(name, {}).get("version")
        if spec.address == "file" and pinned is not None:
            path = Path(spec.source) if Path(spec.source).is_absolute() else store.run_dir / spec.source
            now = digest(path.read_bytes()) if path.is_file() else None
            if now != pinned:
                return fail(f"file input {name} changed while the attempt was open")
    refused = [pin["refused"] for pin in record["pins"].values() if pin.get("refused")]
    if outputs[job.outputs[0]] in refused:
        return fail("answered a refusal with the refused version unchanged")
    store.commit_attempt({**record, "outputs": outputs, "model": result.model, "effort": result.effort})
    store.remove(directory)
    return None


def _sweep(run: Run) -> None:
    """Remove hand-out files that belong to no open attempt."""
    if run.store.handouts.is_dir():
        for directory in run.store.handouts.iterdir():
            record = run.attempts.get(directory.name)
            if record is None or record["state"] != "open":
                run.store.remove(directory)


def _materialize(run: Run) -> None:
    """Make `set/` hold exactly the members and the manifest, from the records.

    The manifest is the directory artifact's, not a member: the engine writes
    it naming only the type, as a working set's is. Pinning member digests is
    publication's, which copies the set out.
    """
    members = run.members()
    wanted = {run.layout.path(role): version for role, version in members.items()}
    wanted[MANIFEST_NAME] = run.store.put(f"type: {run.type_spec}\n".encode())
    set_dir = run.store.set_dir
    set_dir.mkdir(parents=True, exist_ok=True)
    for path in set_dir.iterdir():
        if path.name not in wanted:
            run.store.remove(path)
    for name, version in wanted.items():
        path = set_dir / name
        data = run.store.get(version)
        if not path.is_file() or path.read_bytes() != data:
            run.store.write_bytes(path, data)


def _pending(run: Run, permitted: set[str] | None) -> set[str]:
    return {job.name for job in run.jobs.jobs if isinstance(job, ModelJob)
            and (run.open_attempt(job.name) is not None or run.ready(job, permitted))}


def _run_code_jobs(run: Run) -> Stop | None:
    for _ in range(MAX_CODE_RUNS):
        permitted = run.permitted()
        pending = _pending(run, permitted)
        job = next((job for job in run.jobs.jobs if isinstance(job, CodeJob)
                    and run.ready(job, permitted) and not (run.producers(job) & pending)), None)
        if job is None:
            return None
        # A handler may read the set directory (draft-at-slot validation does),
        # so it must hold the current members when the job's inputs are pinned.
        _materialize(run)
        stop = _run_code_job(run, job)
        run.reload()
        if stop is not None:
            return stop
    raise RuntimeError("code jobs did not reach a fixed point")


def _moved_members(run: Run, job: CodeJob, pins: Mapping[str, Resolved]) -> list[str]:
    """Member inputs whose file in `set/` is not the pinned version.

    The set was rebuilt just before pinning, so a mismatch means something
    outside the engine changed it, or an engine defect; the job must not run
    against bytes its record would not describe.
    """
    moved = []
    for name, spec in job.inputs.items():
        if spec.address != "member" or pins[name].version is None:
            continue
        path = run.store.set_dir / run.layout.path(spec.source)
        if not path.is_file() or digest(path.read_bytes()) != pins[name].version:
            moved.append(spec.source)
    return moved


def _run_code_job(run: Run, job: CodeJob) -> Stop | None:
    store = run.store
    seq = store.next_seq()
    attempt = f"{seq:06d}-{job.name}"
    pins = {name: run.resolve(name, job.inputs) for name in job.inputs}
    for pinned in pins.values():
        if pinned.data is not None:
            store.put(pinned.data)
    record = {"id": attempt, "seq": seq, "job": job.name, "kind": "code",
              "pins": {name: pinned.pin() for name, pinned in pins.items()}}
    moved = _moved_members(run, job, pins)
    if moved:
        reason = "the set directory does not hold the pinned version of " + ", ".join(moved)
        store.fail_attempt(record, reason)
        return Stop(reason, job.name, attempt)
    code_attempt = CodeAttempt(run, job, pins)
    try:
        returned = job.resolve_handler()(code_attempt) or {}
        unknown = set(returned) - set(job.outputs)
        if unknown:
            raise ValueError(f"job {job.name} returned undeclared outputs {sorted(unknown)}")
        outputs = {name: store.put(bytes(data)) for name, data in returned.items()}
        if job.role is not None and job.outputs[0] not in outputs:
            raise ValueError(f"job {job.name} returned no primary output")
        judgments = code_attempt.judgments(outputs, seq, attempt)
    except Exception as error:  # noqa: BLE001 - a failing handler is a recorded failure
        reason = f"{type(error).__name__}: {error}"
        store.fail_attempt(record, reason, trace="".join(traceback.format_exception(error)))
        return Stop(reason, job.name, attempt)
    store.commit_attempt({**record, "outputs": outputs}, judgments)
    return None


def _open_model_attempts(run: Run) -> tuple[list[Handout], list[Stop]]:
    permitted = run.permitted()
    pending = _pending(run, permitted)
    handouts, stops, withheld = [], [], {}
    for job in run.jobs.jobs:
        if not isinstance(job, ModelJob) or job.name not in pending or run.open_attempt(job.name):
            continue
        waiting = run.producers(job) & pending
        if waiting:
            withheld[job.name] = waiting
            continue
        if job.bound is not None and run.attempt_count(job.name) >= job.bound:
            stops.append(Stop(f"bound of {job.bound} attempts exhausted", job.name))
            continue
        handouts.append(_open(run, job))
    if withheld and not handouts and not stops and not any(
            r["state"] == "open" for r in run.attempts.values()):
        # Every ready job waits for another ready job: the wait is a cycle.
        detail = "; ".join(f"{name} waits for {', '.join(sorted(on))}" for name, on in sorted(withheld.items()))
        stops.append(Stop(f"scheduling stalled: {detail}"))
    return handouts, stops
