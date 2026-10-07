"""Start a run and advance it: the engine behind kb/work/workflow-requirements.

One invocation closes the attempts the coordinator reports, runs ready code
jobs to a fixed point, and opens attempts for ready model jobs. Everything it
knows comes from the files under the run directory; see `store.py`.

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
from commonplace.lib.directory_layout import Layout, parse_layout
from commonplace.lib.library import library_root
from commonplace.lib.note_parser import parse_document

from .declaration import PLACEHOLDER, CodeJob, Input, Job, ModelJob, load_job_set
from .reading import READ_BATCH_BYTES, reading_batches, reading_ranges
from .store import RunStore, canonical, digest

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
class Handout:
    """A hand-out is an open model attempt's prompt and output paths."""

    attempt: str
    job: str
    prompt: Path
    outputs: Mapping[str, Path]
    problem: Path


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


# Resolution


@dataclass(frozen=True)
class Resolved:
    """What an input resolves to: a version and its bytes, or absence."""

    version: str | None
    data: bytes | None = None
    role: str | None = None
    producer: str | None = None
    refused: str | None = None  # For a refusal: the refused version.

    def pin(self) -> dict:
        return {"version": self.version, "role": self.role, "producer": self.producer, "refused": self.refused}


ABSENT = Resolved(None)


def _spec(spec: Input) -> dict:
    return {"address": spec.address, "source": spec.source, "required": spec.required,
            "relation": spec.relation, "outcome": spec.outcome}


def _input(raw: dict) -> Input:
    return Input(raw["address"], raw["source"], raw.get("required", True), raw.get("relation"), raw.get("outcome"))


class Run:
    """One consistent reading of a run directory."""

    def __init__(self, store: RunStore) -> None:
        self.store = store
        metadata = store.read_metadata()
        # The type is fixed for the run like the declaration: read from run.json,
        # never from the library, so a later edit or another checkout changes nothing.
        self.layout, self.relations = _parse_type(metadata["type"], metadata["type_spec"])
        self.type_spec = metadata["type_spec"]
        self.parameters = metadata.get("parameters", {})
        self.jobs = load_job_set(metadata["declaration"], self.layout.roles)
        self.reload()

    def reload(self) -> None:
        self.attempts = {record["id"]: record for record in self.store.attempt_records()}
        completed = {i for i, record in self.attempts.items() if record["state"] == "completed"}
        # A judgment counts only once its attempt's record is written whole.
        self.judgments = sorted(
            (record for record in self.store.judgment_records() if record["attempt"] in completed),
            key=lambda record: record["seq"],
        )
        self._holds: dict[str, bool] = {}
        self._members: dict[str, str] | None = None

    # Attempts

    def latest_completed(self, job: str) -> dict | None:
        records = [r for r in self.attempts.values() if r["job"] == job and r["state"] == "completed"]
        return max(records, key=lambda r: r["seq"], default=None)

    def open_attempt(self, job: str) -> dict | None:
        return next((r for r in self.attempts.values() if r["job"] == job and r["state"] == "open"), None)

    def attempt_count(self, job: str) -> int:
        return sum(1 for r in self.attempts.values() if r["job"] == job)

    def latest_output(self, job: Job) -> str | None:
        """The producing job's latest completed primary output."""
        record = self.latest_completed(job.name)
        return None if record is None or not job.outputs else record["outputs"].get(job.outputs[0])

    # Members

    def members(self) -> dict[str, str]:
        if self._members is None:
            members: dict[str, str] = {}
            for judgment in self.judgments:
                if judgment["installs"]:
                    members[judgment["subject"]["role"]] = judgment["subject"]["version"]
            self._members = members
        return self._members

    def permitted(self) -> set[str] | None:
        documents = {}
        for role, version in self.members().items():
            document, _ = parse_document(self.store.get(version).decode("utf-8", errors="replace"))
            if document is not None:
                documents[self.layout.path(role)] = document
        required, permitted = self.layout.requirement(documents)
        self._required = required
        return permitted

    # Judgments

    def holds(self, judgment: dict) -> bool:
        if judgment["id"] not in self._holds:
            self._holds[judgment["id"]] = True  # A basis never depends on its own judgment.
            specs = {name: _input(entry["input"]) for name, entry in judgment["basis"].items()}
            self._holds[judgment["id"]] = all(
                self.resolve(name, specs).version == entry["version"]
                for name, entry in judgment["basis"].items()
            )
        return self._holds[judgment["id"]]

    def superseded(self, refusal: dict) -> bool:
        scope = {entry["relation"] for entry in refusal["scope"]}
        for judgment in self.judgments:
            if (judgment["seq"] > refusal["seq"] and judgment["outcome"] == "accepted"
                    and judgment["subject"]["role"] == refusal["subject"]["role"]
                    and judgment["subject"]["version"] == refusal["subject"]["version"]
                    and (scope <= {e["relation"] for e in judgment["scope"]}
                         or refusal["id"] in judgment["overrides"])):
                return True
        return False

    def resolve(self, name: str, inputs: Mapping[str, Input]) -> Resolved:
        spec = inputs[name]
        if spec.address == "file":
            path = Path(spec.source)
            path = path if path.is_absolute() else self.store.run_dir / path
            if not path.is_file():
                return ABSENT
            data = path.read_bytes()
            return Resolved(digest(data), data)
        if spec.address == "member":
            version = self.members().get(spec.source)
            filler = self.jobs.filler(spec.source)
            if version is None:
                return ABSENT
            return Resolved(version, self.store.get(version), spec.source, filler.name if filler else None)
        if spec.address == "output":
            producer, _, output = spec.source.partition(":")
            job = self.jobs.job(producer)
            record = self.latest_completed(producer)
            version = None if record is None else record["outputs"].get(output)
            if version is None:
                return ABSENT
            role = job.role if output == job.outputs[0] else None
            return Resolved(version, self.store.get(version), role, producer)
        if spec.address == "attempt":
            record = self.latest_completed(spec.source)
            if record is None:
                return ABSENT
            data = canonical(record)
            return Resolved(digest(data), data, None, spec.source)
        if spec.address == "handed":
            attempt_input, _, handed = spec.source.partition(":")
            record = self.latest_completed(inputs[attempt_input].source)
            entry = None if record is None else record["pins"].get(handed)
            if entry is None or entry["version"] is None:
                return ABSENT
            return Resolved(entry["version"], self.store.get(entry["version"]), entry["role"],
                            entry["producer"], entry.get("refused"))
        if spec.address == "refusal":
            job = self.jobs.job(spec.source)
            output = self.latest_output(job)
            refusals = [j for j in self.judgments if j["outcome"] == "refused"
                        and j["subject"]["producer"] == job.name and j["subject"]["version"] == output]
            if output is None or not refusals or self.superseded(refusals[-1]):
                return ABSENT
            refusal = refusals[-1]
            text = (f"Refusal {refusal['id']} of version {output}\n"
                    f"Scope: {', '.join(e['relation'] for e in refusal['scope']) or 'none'}\n\n"
                    f"{refusal['findings']}\n").encode()
            return Resolved(digest(text), text, job.role, None, output)
        if spec.address == "judgment":
            matches = [j for j in self.judgments if j["subject"]["role"] == spec.source
                       and j["outcome"] == spec.outcome
                       and (spec.relation is None or spec.relation in {e["relation"] for e in j["scope"]})]
            if not matches:
                return ABSENT
            judgment = matches[-1]
            current = self.members().get(spec.source) == judgment["subject"]["version"]
            if not (current and self.holds(judgment)):
                return ABSENT
            # Identity is the judged claim, not the record: re-recording the same
            # claim, as an apply job does after an unchanged verdict, is no change.
            data = canonical({
                "subject": judgment["subject"]["version"],
                "outcome": judgment["outcome"],
                "scope": sorted((e["relation"], e["other_version"]) for e in judgment["scope"]
                                if spec.relation is None or e["relation"] == spec.relation),
                "findings": judgment["findings"],
            })
            return Resolved(digest(data), data)
        raise ValueError(f"unknown address {spec.address}")

    # Readiness

    def ready(self, job: Job, permitted: set[str] | None) -> bool:
        """Ready by inputs alone, before the upstream wait and the bound."""
        if self.open_attempt(job.name) is not None:
            return False
        if job.role is not None and permitted is not None and job.role not in permitted:
            return False
        current = {name: self.resolve(name, job.inputs) for name in job.inputs}
        if any(spec.required and current[name].version is None for name, spec in job.inputs.items()):
            return False
        last = self.latest_completed(job.name)
        if last is None:
            return True
        return any(
            resolved.version is not None and resolved.version != last["pins"].get(name, {}).get("version")
            for name, resolved in current.items()
        )

    def producers(self, job: Job) -> set[str]:
        """Model jobs whose pending work would change one of `job`'s inputs.

        Code jobs run to a fixed point before model jobs are handed out, so
        only model jobs are ever pending when readiness is decided.
        """
        names = set()
        for spec in job.inputs.values():
            if spec.address == "member":
                filler = self.jobs.filler(spec.source)
                names.add(filler.name if filler else None)
            elif spec.address in ("output", "attempt"):
                names.add(spec.source.partition(":")[0])
            elif spec.address == "handed":
                names.add(job.inputs[spec.source.partition(":")[0]].source)
        return {name for name in names
                if name and name != job.name and isinstance(self.jobs.job(name), ModelJob)}

    # Coverage

    def publishable(self) -> bool:
        members = self.members()
        permitted = self.permitted()
        if not self._required <= set(members):
            return False
        if permitted is not None and not set(members) <= permitted:
            return False  # A member left over from before the disposition changed.
        return all(self.covered(relation, origin, partner)
                   for origin, partner, relation in self.relations
                   if origin in members and partner in members)

    def covered(self, relation: str, origin: str, partner: str) -> bool:
        members = self.members()
        for judgment in self.judgments:
            if judgment["outcome"] != "accepted" or not self.holds(judgment):
                continue
            subject = judgment["subject"]
            for entry in judgment["scope"]:
                if entry["relation"] != relation:
                    continue
                other = partner if subject["role"] == origin else origin
                if (subject["version"] == members.get(subject["role"])
                        and entry["other_version"] == members.get(other)):
                    return True
        return False


def _parse_type(text: str, where: str) -> tuple[Layout, list[tuple[str, str, str]]]:
    document, error = parse_document(text)
    if document is None or not document.frontmatter or "layout" not in document.frontmatter:
        raise ValueError(f"{where}: not a type with a layout ({error or 'no layout'})")
    layout = parse_layout(document.frontmatter["layout"], where=f"{where}: layout")
    relations = []
    for role in layout.roles.values():
        for partner in role.cites:
            if partner != role.name:
                relations.append((role.name, partner, f"{role.name}:cites:{partner}"))
        for source in role.identity:
            if source.role != role.name:
                relations.append((role.name, source.role, f"{role.name}:identity:{source.role}"))
    return layout, relations


# Code jobs


class CodeAttempt:
    """A code attempt gives a handler its pinned inputs and stages its judgments."""

    def __init__(self, run: Run, job: CodeJob, pins: Mapping[str, Resolved]) -> None:
        self._run = run
        self._job = job
        self._pins = dict(pins)
        self._staged: list[dict] = []

    def read(self, name: str) -> bytes | None:
        if name not in self._pins:
            raise KeyError(f"job {self._job.name} declares no input {name}")
        return self._pins[name].data

    def judge(self, subject: str, *, outcome: str, scope: tuple[str, ...] = (),
              findings: str = "", overrides: tuple[str, ...] = ()) -> None:
        if outcome not in ("accepted", "refused"):
            raise ValueError(f"outcome must be accepted or refused, not {outcome!r}")
        own = bool(self._job.outputs) and subject == self._job.outputs[0] and subject not in self._pins
        if not own:
            if subject not in self._pins:
                raise KeyError(f"job {self._job.name} has no input or primary output {subject}")
            pinned = self._pins[subject]
            if pinned.version is None or pinned.role is None:
                raise ValueError(f"{subject} is not a present version of a role")
        elif self._job.role is None:
            raise ValueError(f"job {self._job.name} fills no role, so its output cannot be judged")
        self._staged.append({"subject": subject, "own": own, "outcome": outcome, "scope": tuple(scope),
                             "findings": findings, "overrides": list(overrides)})

    def judgments(self, outputs: Mapping[str, str], seq: int, attempt: str) -> list[dict]:
        """Resolve staged judgments against the committed outputs."""
        run, job = self._run, self._job
        declared = {relation for _, _, relation in run.relations}
        records = []
        for index, staged in enumerate(self._staged):
            if staged["own"]:
                role, producer = job.role, job.name
                version = outputs.get(staged["subject"])
                if version is None:
                    raise ValueError(f"job {job.name} judged its output but returned none")
                installs = True
            else:
                pinned = self._pins[staged["subject"]]
                role, version, producer = pinned.role, pinned.version, pinned.producer
                filler = run.jobs.filler(role)
                producer = producer or (filler.name if filler else None)
                producing = run.jobs.job(producer) if producer else None
                installs = producing is not None and run.latest_output(producing) == version
            scope = []
            for relation in staged["scope"]:
                if relation not in declared:
                    raise ValueError(f"{relation} is not a relation the type declares")
                origin, _, partner = relation.split(":")
                if role not in (origin, partner):
                    raise ValueError(f"{relation} does not have {role} at either end")
                other = partner if role == origin else origin
                ends = [p.version for p in self._pins.values() if p.role == other and p.version is not None]
                if not ends:
                    raise ValueError(f"{relation}: no version of {other} is in the basis")
                scope.append({"relation": relation, "other_role": other, "other_version": ends[0]})
            records.append({
                "id": f"{seq:06d}-{job.name}-{index}",
                "seq": seq * 1000 + index,
                "attempt": attempt,
                "job": job.name,
                "subject": {"role": role, "version": version, "producer": producer},
                "outcome": staged["outcome"],
                "installs": staged["outcome"] == "accepted" and installs,
                "scope": scope,
                "findings": staged["findings"],
                "overrides": staged["overrides"],
                "basis": {name: {"input": _spec(job.inputs[name]), "version": pinned.version}
                          for name, pinned in self._pins.items()},
            })
        return records


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
        for judgment in judgments:
            store.write_json(store.judgments / f"{judgment['id']}.json", judgment)
        store.write_json(store.attempts / f"{attempt}.json", {
            "id": attempt, "seq": seq, "job": "operator", "kind": "operator", "state": "completed",
            "pins": {name: pinned.pin() for name, pinned in pins.items()},
            "outputs": {}, "judgments": [j["id"] for j in judgments],
        })
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
    directory = store.handouts / record["id"]
    problem_path = directory / "problem.md"
    problem = problem_path.read_text(encoding="utf-8", errors="replace") if problem_path.is_file() else ""

    def fail(reason: str) -> Stop:
        # The worker's problem text is the failure's record; the hand-out
        # directory it was written in does not survive the attempt.
        if problem.strip():
            reason = f"{reason}; the worker wrote: {problem.strip()}"
        record.update(state="failed", pins={}, reason=reason, problem=problem,
                      model=result.model, effort=result.effort)
        store.write_json(store.attempts / f"{record['id']}.json", record)
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
    refused = [pin["refused"] for pin in record["pins"].values() if pin.get("refused")]
    if outputs[job.outputs[0]] in refused:
        return fail("answered a refusal with the refused version unchanged")
    record.update(state="completed", outputs=outputs, model=result.model, effort=result.effort)
    store.write_json(store.attempts / f"{record['id']}.json", record)
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
        record.update(state="failed", pins={}, reason=reason)
        store.write_json(store.attempts / f"{attempt}.json", record)
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
        record.update(state="failed", pins={}, reason=reason,
                      trace="".join(traceback.format_exception(error)))
        store.write_json(store.attempts / f"{attempt}.json", record)
        return Stop(reason, job.name, attempt)
    for judgment in judgments:
        store.write_json(store.judgments / f"{judgment['id']}.json", judgment)
    record.update(state="completed", outputs=outputs, judgments=[j["id"] for j in judgments])
    store.write_json(store.attempts / f"{attempt}.json", record)
    return None


def _open_model_attempts(run: Run) -> tuple[list[Handout], list[Stop]]:
    permitted = run.permitted()
    pending = _pending(run, permitted)
    handouts, stops = [], []
    for job in run.jobs.jobs:
        if not isinstance(job, ModelJob) or job.name not in pending or run.open_attempt(job.name):
            continue
        if run.producers(job) & pending:
            continue
        if job.bound is not None and run.attempt_count(job.name) >= job.bound:
            stops.append(Stop(f"bound of {job.bound} attempts exhausted", job.name))
            continue
        handouts.append(_open(run, job))
    return handouts, stops


def _substitute(value: str, values: Mapping[str, str], parameters: Mapping[str, str]) -> str:
    def one(match) -> str:
        name = match.group(1)
        if name.startswith("param:"):
            return parameters[name.removeprefix("param:")]
        return values[name]
    return PLACEHOLDER.sub(one, value)


def _open(run: Run, job: ModelJob) -> Handout:
    """Open an attempt and write its hand-out prompt.

    The prompt keeps the shape the analysis workers already follow: one line
    naming the instruction, then `name = value` lines for the job, its
    parameters, every input, the outputs, the problem file and the workspace,
    then reading batches over the inputs.
    """
    store = run.store
    seq = store.next_seq()
    attempt = f"{seq:06d}-{job.name}"
    directory = store.handouts / attempt
    scratch = directory / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    (directory / "outputs").mkdir(parents=True, exist_ok=True)
    pins = {name: run.resolve(name, job.inputs) for name in job.inputs}
    paths: dict[str, Path | None] = {}
    for name, pinned in pins.items():
        if pinned.data is None:
            paths[name] = None
            continue
        store.put(pinned.data)
        spec = job.inputs[name]
        if spec.address == "file":
            # A file is handed at its own path, so an instruction's relative
            # links still resolve. Its pinned version is recorded; a method
            # that changes mid-run makes the run unpublishable anyway.
            source = Path(spec.source)
            paths[name] = source if source.is_absolute() else store.run_dir / source
            continue
        path = directory / "inputs" / f"{name}.md"
        store.write_bytes(path, pinned.data)
        paths[name] = path
    outputs = {name: directory / "outputs" / f"{name}.md" for name in job.outputs}
    problem = directory / "problem.md"
    run_values = {"run": str(store.run_dir), "run-id": store.run_dir.name,
                  "set": str(store.set_dir), "workspace": f"{directory}/"}
    values = {"job": job.name, "attempt": attempt, "run-id": store.run_dir.name}
    values |= {key: _substitute(value, run_values, run.parameters) for key, value in job.parameters.items()}
    values |= {name: (str(path) if path else "absent") for name, path in paths.items() if name != job.instruction}
    values["output"] = str(outputs[job.outputs[0]])
    values |= {f"output-{name}": str(path) for name, path in outputs.items() if name != job.outputs[0]}
    values |= {"problem": str(problem), "workspace": f"{directory}/", "scratch": f"{scratch}/"}
    previous = run.latest_completed(job.name)
    if previous is not None:
        for name, version in previous["outputs"].items():
            path = directory / "previous" / f"{name}.md"
            store.write_bytes(path, store.get(version))
            values[f"previous-{name}"] = str(path)
    instruction = paths[job.instruction]
    lines = [f"Follow {instruction} with:", *(f"{key} = {value}" for key, value in values.items())]
    readable = [str(path) for name, path in paths.items() if path is not None and name != job.instruction]
    readable += [value for key, value in values.items() if key.startswith("previous-")]
    if readable:
        lines += ["", "## Input reading batches", "",
                  f"Read the named job instruction {instruction} before these reading batches.", "",
                  ("Load inputs in these batches to avoid truncated reads. Use one tool "
                   "call per batch, return the complete command result, and recover any "
                   "truncation before continuing. Read oversized files in bounded ranges."), ""]
        lines += [f"{number}. " + ", ".join(batch) for number, batch in enumerate(reading_batches(readable), 1)]
        oversized = [Path(path) for path in readable if Path(path).stat().st_size > READ_BATCH_BYTES]
        if oversized:
            lines += ["", "Oversized-file ranges:",
                      ("Read each range in a separate tool call. A single oversized line "
                       "still needs a smaller read if delivery is truncated.")]
            for path in oversized:
                spans = "; ".join(f"{start}-{end}" for start, end in reading_ranges(path))
                lines.append(f"- {path}: lines {spans}")
    lines += ["", "If you cannot produce the output, write the problem to the problem path."]
    prompt = directory / "prompt.md"
    store.write_bytes(prompt, ("\n".join(lines) + "\n").encode("utf-8"))
    store.write_json(store.attempts / f"{attempt}.json", {
        "id": attempt, "seq": seq, "job": job.name, "kind": "model", "state": "open",
        "pins": {name: pinned.pin() for name, pinned in pins.items()},
    })
    return Handout(attempt, job.name, prompt, outputs, problem)
