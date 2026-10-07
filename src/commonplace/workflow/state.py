"""Interpretation of a run's records: members, readiness, judgments, coverage.

`Run` is one consistent reading of a run directory. It resolves inputs to
versions, decides which jobs are ready and which roles have members, and
says whether the set is publishable. `CodeAttempt` is a handler's view of
one code attempt; it turns staged judgments into records. Nothing here
writes: commits are the store's, transitions are the engine's.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

from commonplace.lib.directory_layout import Layout, parse_layout
from commonplace.lib.note_parser import parse_document

from .declaration import CodeJob, Input, Job, ModelJob, load_job_set
from .store import RunStore, canonical, digest


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
            "relation": spec.relation, "outcome": spec.outcome, "trigger": spec.trigger}


def _input(raw: dict) -> Input:
    return Input(raw["address"], raw["source"], raw.get("required", True), raw.get("relation"),
                 raw.get("outcome"), raw.get("trigger", True))


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
        self.library = Path(metadata["library"])
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

    def installed(self) -> dict[str, str]:
        """The version each installing acceptance last put in a role."""
        installed: dict[str, str] = {}
        for judgment in self.judgments:
            if judgment["installs"]:
                installed[judgment["subject"]["role"]] = judgment["subject"]["version"]
        return installed

    def members(self) -> dict[str, str]:
        """Installed versions of the roles the type permits.

        A role the disposition no longer permits has no member; its versions
        and judgments stay recorded and return if the disposition does.
        """
        if self._members is None:
            installed = self.installed()
            permitted = self._permitted_given(installed)
            self._members = {role: version for role, version in installed.items()
                             if permitted is None or role in permitted}
        return self._members

    def _requirements_given(self, members: Mapping[str, str]) -> tuple[set[str], set[str] | None]:
        documents = {}
        for role, version in members.items():
            document, _ = parse_document(self.store.get(version).decode("utf-8", errors="replace"))
            if document is not None:
                documents[self.layout.path(role)] = document
        return self.layout.requirement(documents)

    def _permitted_given(self, members: Mapping[str, str]) -> set[str] | None:
        return self._requirements_given(members)[1]

    def requirements(self) -> tuple[set[str], set[str] | None]:
        """The roles the type requires and the roles it permits (None: all)."""
        return self._requirements_given(self.members())

    def permitted(self) -> set[str] | None:
        return self.requirements()[1]

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
            path = self.file_path(spec)
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

    def file_path(self, spec: Input) -> Path:
        """A file input's path: absolute as declared, else under the run's library root."""
        path = Path(spec.source)
        return path if path.is_absolute() else self.library / path

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
            job.inputs[name].trigger and resolved.version is not None
            and resolved.version != last["pins"].get(name, {}).get("version")
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
            elif spec.address == "judgment":
                # The judging job is a code job, run to a fixed point; the
                # pending work behind it is the model jobs filling the roles
                # its judgment relates: the subject and the relation's ends.
                roles = {spec.source}
                if spec.relation:
                    origin, _, partner = spec.relation.split(":")
                    roles |= {origin, partner}
                for role in roles:
                    filler = self.jobs.filler(role)
                    names.add(filler.name if filler else None)
        return {name for name in names
                if name and name != job.name and isinstance(self.jobs.job(name), ModelJob)}

    # Coverage

    def publishable(self) -> bool:
        members = self.members()
        required, permitted = self.requirements()
        if not required <= set(members):
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
        self._parameters = MappingProxyType(dict(run.parameters))
        self._staged: list[dict] = []

    @property
    def parameters(self) -> Mapping[str, str]:
        """The run parameters fixed at start, read-only and not rerun triggers."""
        return self._parameters

    @property
    def run_dir(self) -> Path:
        """The absolute run directory, for consumer-owned environment checks."""
        return self._run.store.run_dir.resolve()

    @property
    def library(self) -> Path:
        """The library root recorded at start, not the process's current library."""
        return self._run.library

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
                ends = {p.version for p in self._pins.values() if p.role == other and p.version is not None}
                if not ends:
                    raise ValueError(f"{relation}: no version of {other} is in the basis")
                if len(ends) > 1:
                    raise ValueError(f"{relation}: the basis holds {len(ends)} versions of {other}; "
                                     "a scoped relation needs exactly one")
                scope.append({"relation": relation, "other_role": other, "other_version": ends.pop()})
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
