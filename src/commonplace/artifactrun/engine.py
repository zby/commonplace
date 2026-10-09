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

import json
import traceback
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import yaml

from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.library import library_root

from .compact import expand_text
from .handouts import (
    WORKER_RUNTIME,
    Handout,
    _open,
    handout_for,
    handout_slots,
    render_handout,
)
from .plan import CodeJob, Input, ModelJob, PlanError, check_relations, load_plan
from .run import CodeAttempt, Resolved, Run, _parse_type
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


class UncertainEffectError(RuntimeError):
    """A consumer cannot establish an external effect's outcome; do not blindly repeat it.

    Recognition and recovery stay in the consumer handler. The engine only
    preserves this distinction in the failed attempt and operator reports.
    """


@dataclass(frozen=True)
class Stop:
    """A stop names the job and attempt that ended the invocation."""

    reason: str
    job: str | None = None
    attempt: str | None = None
    uncertain: bool = False


@dataclass(frozen=True)
class RunStatus:
    """The run status lists hand-outs, open attempts, stops and publishability."""

    handouts: tuple[Handout, ...]
    open_attempts: tuple[str, ...]
    stops: tuple[Stop, ...]
    publishable: bool


# Operations


def start_run(run_dir: Path, plan: Path, *, parameters: Mapping[str, str] | None = None) -> None:
    """Start a run: write metadata naming the plan and the run parameters."""
    store = RunStore(Path(run_dir))
    if store.metadata.exists():
        raise FileExistsError(f"{run_dir} already holds a run")
    library = library_root().resolve()
    # A compact plan is expanded here; the run fixes and runs the expansion.
    source = Path(plan).read_bytes()
    declaration = expand_text(source.decode("utf-8"), library=library, plan_dir=Path(plan).resolve().parent)
    type_spec = load_plan(declaration).type_spec
    type_text = (library / type_spec).read_text(encoding="utf-8")
    layout, relations = _parse_type(type_text, str(type_spec))
    jobs = load_plan(declaration, layout.roles)
    check_relations(jobs, [relation for _, _, relation in relations])
    given = dict(parameters or {})
    missing = sorted({name for job in jobs.jobs if isinstance(job, ModelJob)
                      for name in job.run_parameters()} - set(given))
    if missing:
        raise ValueError(f"the plan substitutes run parameters not given: {', '.join(missing)}")
    if jobs.handout is not None:
        _check_handout(jobs, library, layout, str(type_spec), given)
    store.create({
        "plan": str(Path(plan).resolve()),
        "plan_sha256": digest(source),
        "declaration": declaration,
        "type_spec": str(type_spec),
        "library": str(library),
        "type": type_text,
        "parameters": dict(parameters or {}),
    })


def _check_handout(jobs, library: Path, layout, type_spec: str, parameters: Mapping[str, str]) -> None:
    """Render the hand-out template for every model job, so an unknown placeholder fails the plan at start."""
    path = Path(jobs.handout)
    path = path if path.is_absolute() else library / path
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        raise PlanError(f"handout {jobs.handout}: {error}") from error
    for job in jobs.jobs:
        if not isinstance(job, ModelJob):
            continue
        values = {key: value for key, value in job.parameters.items()}
        try:
            render_handout(text, handout_slots(job, layout, type_spec, values), parameters)
        except KeyError as error:
            raise PlanError(f"handout {jobs.handout}: job {job.name} has no value for {{{error.args[0]}}}") from None


def advance(run_dir: Path, *, results: tuple[AttemptResult, ...] = ()) -> RunStatus:
    """Run one invocation over the run directory and return its run status."""
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    with store.lock():
        run = Run(store)
        stops = []
        for result in results:
            if (stop := _close(run, result)) is not None:
                stops.append(stop)
            # Closure is final: later results, even conflicting ones in this
            # batch, must see the closed record just as a later invocation does.
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
        inputs = {"subject": Input("role", role)}
        pins = {"subject": Resolved(subject, store.get(subject), role, filler.name if filler else None)}
        for other in basis:
            inputs[other] = Input("role", other)
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
    """A read-only view including each job's latest attempt when it has failed.

    Failure records preserve uncertain external effects without running their
    recognizers. Bounds and scheduling stops are invocation results, not failed
    attempts, and are not reconstructed here.
    """
    store = RunStore(Path(run_dir))
    if not store.metadata.exists():
        raise FileNotFoundError(f"{run_dir} holds no run; start it first")
    with store.lock():
        return _inspect(Run(store))


def _inspect(run: Run) -> dict:
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
    latest = {}
    for record in sorted(run.attempts.values(), key=lambda r: r["seq"]):
        latest[record["job"]] = record
    failures = [Stop(r["reason"], r["job"], r["id"], r.get("uncertain", False))
                for r in latest.values() if r["state"] == "failed"]
    permitted = run.permitted()
    exhausted = [job.name for job in run.jobs.jobs
                 if isinstance(job, ModelJob) and job.max_attempts is not None
                 and run.attempt_count(job.name) >= job.max_attempts and run.ready(job, permitted)]
    opened = sorted(r["id"] for r in run.attempts.values() if r["state"] == "open")
    failed = {stop.job for stop in failures}
    publishable = run.publishable()
    # A failed or exhausted job stops the run even while others wait on it.
    if opened:
        condition = "running"
    elif failed or exhausted:
        condition = "stopped"
    elif publishable:
        condition = "publishable"
    elif any(run.ready(job, permitted) for job in run.jobs.jobs):
        condition = "running"
    else:
        condition = "stuck"
    return {
        "condition": condition,
        "parameters": dict(run.parameters),
        "declaration": _declaration_identity(run),
        "attempts": [{key: record.get(key) for key in
                      ("id", "job", "kind", "state", "model", "effort", "worker_model", "worker_effort", "reason", "uncertain")}
                     for record in sorted(run.attempts.values(), key=lambda r: r["seq"])],
        "failed_attempts": failures,
        "exhausted_jobs": exhausted,
        "members": dict(run.members()),
        "open_attempts": opened,
        "refusals": refusals,
        "stale_acceptances": [j["id"] for j in run.judgments
                              if j["outcome"] == "accepted" and not run.holds(j)],
        "historical_bases": _historical_bases(run),
        "publishable": publishable,
    }


def _declaration_identity(run: Run) -> dict:
    """Which plan and type the run fixed at start, by path and content digest.

    `plan_sha256` is the plan file as shipped; `sha256` is the declaration the
    run fixed, which differs for a compact plan the engine expanded.
    """
    metadata = run.store.read_metadata()
    return {"plan": metadata["plan"], "plan_sha256": metadata.get("plan_sha256"),
            "sha256": digest(metadata["declaration"].encode("utf-8")),
            "type_spec": metadata["type_spec"], "type_sha256": digest(metadata["type"].encode("utf-8"))}


def _historical_bases(run: Run) -> list[dict]:
    """Holding acceptances whose basis has a handed member that is no longer current."""
    members = run.members()
    found = []
    for judgment in run.judgments:
        if judgment["outcome"] != "accepted" or not run.holds(judgment):
            continue
        basis = judgment["basis"]
        for name, entry in basis.items():
            if entry["input"]["address"] != "handed":
                continue
            alias, _, handed = entry["input"]["source"].partition(":")
            producer = run.jobs.job(basis[alias]["input"]["source"])
            original = producer.inputs.get(handed)
            if (original is not None and original.address == "role"
                    and entry["version"] != members.get(original.source)):
                found.append({"judgment": judgment["id"], "input": name, "role": original.source,
                              "handed": entry["version"], "current": members.get(original.source)})
    return found


def current_outputs(run_dir: Path, job: str) -> dict[str, bytes] | None:
    """A job's outputs while its completion is current, else None.

    A completion is current while its pins still resolve to the same
    versions, no attempt of the job is open and the job is not ready.
    """
    store = RunStore(Path(run_dir))
    with store.lock():
        run = Run(store)
        declared = run.jobs.job(job)
        last = run.latest_completed(job)
        if last is None or run.open_attempt(job) is not None or run.ready(declared, run.permitted()):
            return None
        pins = {name: run.resolve(name, declared.inputs).pin() for name in declared.inputs}
        if pins != last["pins"]:
            return None
        return {name: store.get(version) for name, version in last["outputs"].items()}


@contextmanager
def run_lock(run_dir: Path) -> Iterator[None]:
    """Hold the run lock so no invocation changes the run meanwhile."""
    with RunStore(Path(run_dir)).lock():
        yield


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
        return None  # First closure wins, including conflicting later reports.
    job = run.jobs.job(record["job"])
    directory = store.handout_dir(record["id"])
    problem_path = directory / "problem.md"
    problem = problem_path.read_text(encoding="utf-8", errors="replace") if problem_path.is_file() else ""
    runtime_path = directory / WORKER_RUNTIME

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
    try:
        worker_runtime = json.loads(runtime_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return fail("completed without a valid worker-runtime JSON report")
    if (not isinstance(worker_runtime, dict) or set(worker_runtime) != {"model", "effort"}
            or any(not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value
                   for value in worker_runtime.values())):
        return fail("worker-runtime report needs exactly nonempty one-line model and effort strings")
    for name, spec in job.inputs.items():
        pinned = record["pins"].get(name, {}).get("version")
        if spec.address == "file" and pinned is not None:
            path = run.file_path(spec)
            now = digest(path.read_bytes()) if path.is_file() else None
            if now != pinned:
                return fail(f"file input {name} changed while the attempt was open")
    refused = [pin["refused"] for pin in record["pins"].values() if pin.get("refused")]
    if outputs[job.outputs[0]] in refused:
        previous = run.latest_completed(job.name)
        previous_outputs = previous["outputs"] if previous is not None else {}
        # An answer can reconcile a refusal without changing the subject. Only
        # a produced auxiliary version counts; dropping a file is not an answer.
        changed_auxiliary = previous is not None and any(
            name in outputs and outputs[name] != previous_outputs.get(name)
            for name in job.outputs[1:]
        )
        if not changed_auxiliary:
            return fail("answered a refusal with the refused version unchanged and no new auxiliary version")
    store.commit_attempt({**record, "outputs": outputs, "model": result.model, "effort": result.effort,
                          "worker_model": worker_runtime["model"].strip(),
                          "worker_effort": worker_runtime["effort"].strip()})
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
    """Make `artifact/` hold exactly the members and the manifest, from the records.

    The manifest is the directory artifact's, not a member: the engine writes
    it naming only the type, as a working artifact's is. Pinning member digests is
    publication's, which copies the artifact out.
    """
    members = run.members()
    wanted = {run.layout.path(role): version for role, version in members.items()}
    wanted[MANIFEST_NAME] = run.store.put(yaml.safe_dump({"type": run.type_spec}).encode())
    artifact_dir = run.store.artifact_dir
    artifact_dir.mkdir(parents=True, exist_ok=True)
    for path in artifact_dir.iterdir():
        if path.name not in wanted:
            run.store.remove(path)
    for name, version in wanted.items():
        path = artifact_dir / name
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
                    and run.ready(job, permitted)
                    and all(run.checks_before_downstream(job, run.jobs.job(peer))
                            for peer in run.producers(job) & pending)), None)
        if job is None:
            return None
        # A handler may read the artifact directory (draft validation in a role does),
        # so it must hold the current members when the job's inputs are pinned.
        _materialize(run)
        stop = _run_code_job(run, job)
        run.reload()
        if stop is not None:
            return stop
    raise RuntimeError("code jobs did not reach a fixed point")


def _moved_members(run: Run, job: CodeJob, pins: Mapping[str, Resolved]) -> list[str]:
    """Member inputs whose file in `artifact/` is not the pinned version.

    The artifact was rebuilt just before pinning, so a mismatch means something
    outside the engine changed it, or an engine defect; the job must not run
    against bytes its record would not describe.
    """
    moved = []
    for name, spec in job.inputs.items():
        if spec.address != "role" or pins[name].version is None:
            continue
        path = run.store.artifact_dir / run.layout.path(spec.source)
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
        reason = "the artifact directory does not hold the pinned version of " + ", ".join(moved)
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
        uncertain = isinstance(error, UncertainEffectError)
        store.fail_attempt(record, reason, uncertain=uncertain, trace="".join(traceback.format_exception(error)))
        return Stop(reason, job.name, attempt, uncertain)
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
        if job.max_attempts is not None and run.attempt_count(job.name) >= job.max_attempts:
            stops.append(Stop(f"max attempts ({job.max_attempts}) exhausted", job.name))
            continue
        handouts.append(_open(run, job))
    if withheld and not handouts and not stops and not any(
            r["state"] == "open" for r in run.attempts.values()):
        # Every ready job waits for another ready job: the wait is a cycle.
        detail = "; ".join(f"{name} waits for {', '.join(sorted(on))}" for name, on in sorted(withheld.items()))
        stops.append(Stop(f"scheduling stalled: {detail}"))
    return handouts, stops
