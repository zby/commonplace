"""Interpretation of a run's records: members, readiness, judgments, coverage.

`Run` is one consistent reading of a run directory. It resolves inputs to
versions, decides which jobs are ready and which roles have members, and
says whether the artifact is publishable. `CodeAttempt` is a handler's view of
one code attempt; it turns staged judgments into records. Nothing here
writes: commits are the store's, transitions are the engine's.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

import yaml

from commonplace.lib.directory_layout import Layout, parse_layout
from commonplace.lib.note_parser import parse_document

from .plan import CodeJob, Input, Job, ModelJob, load_plan
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
            "relation": spec.relation, "outcome": spec.outcome, "order_only": spec.order_only}


def _input(raw: dict) -> Input:
    return Input(raw["address"], raw["source"], raw.get("required", True), raw.get("relation"),
                 raw.get("outcome"), raw.get("order_only", False))


class Run:
    """One consistent reading of a run directory."""

    def __init__(self, store: RunStore) -> None:
        self.store = store
        metadata = store.read_metadata()
        # The type is fixed for the run like the declaration: read from run.json,
        # never from the library, so a later edit or another checkout changes nothing.
        self.layout, self.relations = _parse_type(metadata["type"], metadata["type_spec"])
        self.type_spec = metadata["type_spec"]
        self.type_text = metadata["type"]
        self.parameters = metadata.get("parameters", {})
        self.library = Path(metadata["library"])
        self.jobs = load_plan(metadata["declaration"], self.layout.roles)
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
            data = canonical({key: record[key] for key in ATTEMPT_FIELDS if key in record})
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
            text = refusal_document(refusal["id"], output, [e["relation"] for e in refusal["scope"]],
                                    refusal["findings"])
            return Resolved(digest(text), text, job.role, None, output)
        if spec.address == "coverage":
            evidence = self.coverage(spec.source or None)
            if evidence is None:
                return ABSENT
            data = canonical(evidence)
            return Resolved(digest(data), data)
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
        """Ready by inputs alone, before the upstream wait and max attempts."""
        if self.open_attempt(job.name) is not None:
            return False
        if job.role is not None and permitted is not None and job.role not in permitted:
            return False
        current = {name: self.resolve(name, job.inputs) for name in job.inputs}
        if any(spec.required and current[name].version is None for name, spec in job.inputs.items()):
            return False
        latest = max((r for r in self.attempts.values() if r["job"] == job.name),
                     key=lambda r: r["seq"], default=None)
        if latest is not None and latest["state"] == "failed":
            # Failure requires a retry even if inputs reverted to those of an
            # earlier completion. Presence and permission checks still apply.
            return True
        last = self.latest_completed(job.name)
        if last is None:
            return True
        def changed(name: str, resolved: Resolved) -> bool:
            spec = job.inputs[name]
            if (spec.order_only or resolved.version is None
                    or resolved.version == last["pins"].get(name, {}).get("version")):
                return False
            if isinstance(job, ModelJob) and spec.address == "refusal" and spec.source == job.name:
                # Restoring earlier bytes can expose an earlier refusal again.
                # Reading it in a completed attempt answered it; a structural
                # repair must not spend another model attempt on that identity.
                return not any(
                    record["job"] == job.name and record["state"] == "completed"
                    and record["pins"].get(name, {}).get("version") == resolved.version
                    for record in self.attempts.values()
                )
            return True

        return any(changed(name, resolved) for name, resolved in current.items())

    def producers(self, job: Job) -> set[str]:
        """Model jobs whose pending work would change one of `job`'s inputs.

        Code jobs run to a fixed point before model jobs are handed out, so
        only model jobs are ever pending when readiness is decided.
        """
        names = set().union(*(self._input_producers(job, spec) for spec in job.inputs.values()))
        return {name for name in names
                if name and name != job.name and isinstance(self.jobs.job(name), ModelJob)
                and not self._consumes_completed_subjects(job, self.jobs.job(name))}

    def _input_producers(self, job: Job, spec: Input) -> set[str]:
        """Declared producers for one input, before the completed-subject exception."""
        names = set()
        if spec.address == "member":
            filler = self.jobs.filler(spec.source)
            names.add(filler.name if filler else None)
        elif spec.address in ("output", "attempt"):
            names.add(spec.source.partition(":")[0])
        elif spec.address == "handed":
            names.add(job.inputs[spec.source.partition(":")[0]].source)
        elif spec.address == "coverage":
            # Every model job filling a role in scope can still change coverage.
            for role in self.layout.roles:
                filler = self.jobs.filler(role)
                if role != spec.source and filler is not None:
                    names.add(filler.name)
        elif spec.address == "judgment":
            # The judging job is code; the pending work behind it is the
            # model jobs filling the subject and the relation's ends.
            roles = {spec.source}
            if spec.relation:
                origin, _, partner = spec.relation.split(":")
                roles |= {origin, partner}
            for role in roles:
                filler = self.jobs.filler(role)
                names.add(filler.name if filler else None)
        return {name for name in names if name}

    def checks_before_downstream(self, job: CodeJob, peer: ModelJob) -> bool:
        """Prioritize a new upstream candidate over a ready optional downstream peer.

        Only the wait is waived: the check still pins the current peer member,
        and a later peer version makes that basis stale. Historical handed
        subjects have a separate exception in `producers`.
        """
        if self.open_attempt(peer.name) is not None:
            return False
        peer_inputs = [spec for spec in job.inputs.values()
                       if peer.name in self._input_producers(job, spec)]
        if not peer_inputs or any(
            spec.address != "member" or spec.required for spec in peer_inputs
        ):
            return False
        last = self.latest_completed(job.name)
        for name, spec in job.inputs.items():
            if spec.address != "output":
                continue
            producer, _, output = spec.source.partition(":")
            upstream = self.jobs.job(producer)
            if (not isinstance(upstream, ModelJob) or upstream.role is None
                    or self.jobs.filler(upstream.role) != upstream
                    or output != upstream.outputs[0]):
                continue
            candidate = self.latest_output(upstream)
            if candidate is None or (last is not None
                    and last["pins"].get(name, {}).get("version") == candidate):
                continue
            if any(dependency.address == "member" and dependency.required
                   and dependency.order_only and dependency.source == upstream.role
                   for dependency in peer.inputs.values()):
                return True
        return False

    def _consumes_completed_subjects(self, job: Job, producer: Job) -> bool:
        """A code consumer of handed members can apply completed work before a rerun.

        This is scheduling only. Readiness, exact judgment subjects and refusal
        supersession are unchanged. A check reading only its producer's answered
        refusal is not historical verdict application and must still wait.
        """
        if not isinstance(job, CodeJob) or not isinstance(producer, ModelJob):
            return False
        record = self.latest_completed(producer.name)
        if record is None or not any(
            spec.address == "attempt" and spec.source == producer.name and not spec.order_only
            for spec in job.inputs.values()
        ):
            return False
        handed_member = False
        for spec in job.inputs.values():
            if spec.address == "refusal" and spec.source == producer.name:
                return False  # A live refusal is not part of the completed record.
            if producer.name not in self._input_producers(job, spec):
                continue
            if spec.address == "attempt":
                continue
            if spec.address == "output":
                # resolve() selects outputs from this same latest completed attempt,
                # including recorded absence of an optional auxiliary output.
                continue
            if spec.address != "handed":
                return False  # Current members and judgment gates retain their wait.
            _, _, name = spec.source.partition(":")
            declared = producer.inputs.get(name)
            pin = record["pins"].get(name)
            if declared is None or pin is None:
                return False  # No exemption for an arbitrary historical address.
            if (declared.address == "member" and declared.source != producer.role
                    and pin["version"] is not None and pin["role"] == declared.source):
                handed_member = True
        return handed_member

    # Coverage

    def coverage(self, excluded: str | None = None) -> dict | None:
        """The evidence that the artifact minus `excluded` is covered, or None while it is not.

        Three conditions: every required role is present, every member has a
        holding acceptance, and every relation between members is covered.
        The evidence names members and covering claims, never record ids, so
        re-recording an unchanged claim changes nothing.
        """
        members = {role: version for role, version in self.members().items() if role != excluded}
        required, permitted = self.requirements()
        if not required - {excluded} <= set(members):
            return None
        if permitted is not None and not set(members) <= permitted:
            return None  # A member left over from before the disposition changed.
        relations = [(origin, partner, name) for origin, partner, name in self.relations
                     if origin in members and partner in members]
        accepted = [j for j in self.judgments if j["outcome"] == "accepted"
                    and members.get(j["subject"]["role"]) == j["subject"]["version"] and self.holds(j)]
        claims = set()
        for role, version in members.items():
            mine = [j for j in accepted if j["subject"]["role"] == role]
            if not mine:
                return None
            claims |= {(role, version, None, None) for _ in mine[:1]}
        for origin, partner, name in relations:
            covering = {
                (j["subject"]["role"], j["subject"]["version"], name, entry["other_version"])
                for j in accepted for entry in j["scope"]
                if entry["relation"] == name
                and entry["other_version"] == members[partner if j["subject"]["role"] == origin else origin]
            }
            if not covering:
                return None
            claims |= covering
        return {"members": dict(sorted(members.items())),
                "claims": sorted([list(claim) for claim in claims], key=lambda c: [str(x) for x in c])}

    def publishable(self) -> bool:
        """The whole artifact is covered: requirement 9's three conditions hold."""
        return self.coverage() is not None

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


# The published fields of an attempt-record input; the rest of the record is internal.
ATTEMPT_FIELDS = ("id", "job", "kind", "outputs", "previous_outputs", "model", "effort", "worker_model")


def refusal_document(refusal: str, version: str, scope: list[str], findings: str) -> bytes:
    """A refusal input's bytes: the published fields as frontmatter, the findings as body."""
    fields = yaml.safe_dump({"refusal": refusal, "version": version, "scope": scope}, sort_keys=False)
    return f"---\n{fields}---\n{findings}".encode()


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
    def layout(self) -> Layout:
        """The type's layout, fixed at start like the declaration."""
        return self._run.layout

    @property
    def relations(self) -> tuple[tuple[str, str, str], ...]:
        """The type's relations as (origin, partner, name), fixed at start."""
        return tuple(self._run.relations)

    @property
    def type_text(self) -> str:
        """The type's text fixed at start, for validators that need it."""
        return self._run.type_text

    @property
    def type_spec(self) -> str:
        """The type's library path recorded at start, for keying its text."""
        return self._run.type_spec

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

    def read_files(self) -> dict[str, bytes]:
        """The pinned file inputs under the library, keyed by library path."""
        files: dict[str, bytes] = {}
        for name, spec in self._job.inputs.items():
            data = self._pins[name].data
            if spec.address != "file" or Path(spec.source).is_absolute() or data is None:
                continue
            files[Path(spec.source).as_posix()] = data
        return files

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
