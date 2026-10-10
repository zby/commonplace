"""The plan: a data file naming jobs, their inputs and outputs.

A plan declares the jobs that produce one type of artifact. It is data, not
code: code jobs name their handlers by dotted path into the package.
"""

from __future__ import annotations

import importlib
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

import yaml

ADDRESSES = ("file", "role", "output", "attempt", "handed", "judgment", "refusal", "coverage")
PLACEHOLDER = re.compile(r"\{([^{}]*)\}")
RUN_PLACEHOLDERS = ("run", "run-id", "artifact", "workspace")
"""Values a parameter may substitute besides `param:<name>`, a run parameter."""
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
"""Job, input, output and parameter names: they become file and record names."""
RESERVED_JOBS = ("operator",)
"""Job names the engine uses for its own records."""
FRAME_LINES = ("job", "attempt", "run-id", "output", "problem", "worker-identity", "workspace", "artifact", "scratch")
"""Lines the frame prints for every model attempt."""
ROLE_LINES = ("role", "identity", "cites", "verifies")
"""Lines the frame prints for a role-filling job: its role and the layout's facts about it."""
HANDOUT_FIELDS = FRAME_LINES + ROLE_LINES
HANDOUT_PREFIXES = ("output-", "previous-")
"""Names a hand-out prompt sets itself; inputs and parameters may not reuse them."""
REFUSAL_INPUT = "refusal"
"""The input name under which a role-filling model job receives its refusals."""
PROMPT_SECTION_INPUT = "prompt-section"
"""The input name under which every model job receives the plan's prompt section."""
OUTCOMES = ("accepted", "refused")


class PlanError(ValueError):
    """A plan that cannot be run as declared."""


@dataclass(frozen=True)
class Input:
    """An input is something a job depends on, required or optional.

    A file source may be relative; it is resolved against the library root
    the run was started with. An order-only input, as in Make's order-only
    prerequisites, orders the job after it without making it a rerun
    trigger: it must be present for the job to be ready, and its version is
    recorded, but a change is no signal.
    """

    address: str
    source: str
    required: bool = True
    relation: str | None = None
    outcome: str | None = None
    order_only: bool = False


@dataclass(frozen=True)
class ModelJob:
    """A model job is handed out to a worker; the command never calls a model."""

    name: str
    inputs: Mapping[str, Input]
    outputs: tuple[str, ...]
    instruction: str
    role: str | None = None
    max_attempts: int | None = None
    parameters: Mapping[str, str] = field(default_factory=dict)

    def run_parameters(self) -> set[str]:
        """The run parameters this job's parameters substitute."""
        return {name.removeprefix("param:") for value in self.parameters.values()
                for name in PLACEHOLDER.findall(value) if name.startswith("param:")}


@dataclass(frozen=True)
class CodeJob:
    """A code job runs its handler under the command.

    `extensions` is data for the handler that the engine stores with the plan
    and never interprets; a change to it is a change of plan, not an input.
    """

    name: str
    inputs: Mapping[str, Input]
    outputs: tuple[str, ...]
    handler: str
    role: str | None = None
    extensions: Mapping[str, Any] = field(default_factory=dict)

    def resolve_handler(self) -> Callable:
        module, _, attribute = self.handler.rpartition(".")
        try:
            return getattr(importlib.import_module(module), attribute)
        except (ImportError, AttributeError) as error:
            raise PlanError(f"job {self.name}: handler {self.handler} does not resolve: {error}") from error


Job = ModelJob | CodeJob


@dataclass(frozen=True)
class Plan:
    """A plan declares the jobs that produce one type of artifact."""

    type_spec: Path
    jobs: tuple[Job, ...]
    prompt_section: str | None = None
    """The library path of the plan's prompt section, or None for the bare frame."""
    frozen_source: str | None = None
    """The role whose `source` field pins the checkout the run may inspect, or None."""

    def job(self, name: str) -> Job:
        for job in self.jobs:
            if job.name == name:
                return job
        raise KeyError(name)

    def filler(self, role: str) -> Job | None:
        """The job whose primary output fills `role`."""
        return next((job for job in self.jobs if job.role == role), None)

    def input_role(self, job: Job, name: str) -> str | None:
        """The role whose versions `job`'s input `name` holds, by declaration alone.

        A role input holds its role; a producer's primary output holds the
        producer's role; a handed input holds what the producer's own input
        of that name held. Anything else holds no role.
        """
        spec = job.inputs[name]
        if spec.address == "role":
            return spec.source
        if spec.address == "output":
            producer, _, output = spec.source.partition(":")
            upstream = self.job(producer)
            return upstream.role if upstream.outputs and output == upstream.outputs[0] else None
        if spec.address == "handed":
            attempt, _, handed = spec.source.partition(":")
            producer = self.job(job.inputs[attempt].source)
            return self.input_role(producer, handed) if handed in producer.inputs else None
        return None


def reject_underscored_keys(data: Any, where: str = "plan") -> None:
    """Plan keys and names are hyphenated; an underscore is a misspelling."""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, str) and "_" in key:
                raise PlanError(f"{where}: key {key!r} uses an underscore; plan keys and names use hyphens")
            reject_underscored_keys(value, f"{where}: {key}")
    elif isinstance(data, list):
        for item in data:
            reject_underscored_keys(item, where)


def _input(job: str, name: str, raw: Any) -> Input:
    where = f"job {job}: input {name}"
    if not isinstance(raw, dict):
        raise PlanError(f"{where}: must be a mapping")
    unknown = set(raw) - {"address", "source", "required", "relation", "outcome", "order-only"}
    if unknown:
        raise PlanError(f"{where}: unknown keys {sorted(unknown)}")
    address, source = raw.get("address"), raw.get("source")
    if address not in ADDRESSES:
        raise PlanError(f"{where}: address must be one of {', '.join(ADDRESSES)}")
    if address == "coverage":
        # The scope is derived: the artifact minus the declaring job's own role,
        # filled in once the job's role is known.
        if source is not None:
            raise PlanError(f"{where}: a coverage input has no source; its scope is derived")
        source = ""
    elif not isinstance(source, str) or not source:
        raise PlanError(f"{where}: source must be a nonempty string")
    required = raw.get("required", True)
    if not isinstance(required, bool):
        raise PlanError(f"{where}: required must be true or false")
    relation, outcome = raw.get("relation"), raw.get("outcome")
    if address == "judgment":
        if outcome not in OUTCOMES:
            raise PlanError(f"{where}: a judgment input needs an outcome of {' or '.join(OUTCOMES)}")
        if relation is not None and (not isinstance(relation, str) or relation.count(":") != 2):
            raise PlanError(f"{where}: relation must read <origin>:<kind>:<partner>")
    elif relation is not None or outcome is not None:
        raise PlanError(f"{where}: only a judgment input has a relation or an outcome")
    if address in ("output", "handed") and source.count(":") != 1:
        raise PlanError(f"{where}: source must read <name>:<name>")
    order_only = raw.get("order-only", False)
    if not isinstance(order_only, bool):
        raise PlanError(f"{where}: order-only must be true or false")
    return Input(address, source, required, relation, outcome, order_only)


def _job(raw: Any) -> Job:
    if not isinstance(raw, dict):
        raise PlanError("each job must be a mapping")
    name = raw.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name):
        raise PlanError(f"job name {name!r} must be letters, digits, '-' or '_'")
    if name in RESERVED_JOBS:
        raise PlanError(f"job name {name} is reserved for the engine's records")
    kind = raw.get("kind")
    raw_inputs = raw.get("inputs", {})
    if not isinstance(raw_inputs, dict):
        raise PlanError(f"job {name}: inputs must be a mapping")
    for key in raw_inputs:
        if not isinstance(key, str) or not NAME.fullmatch(key):
            raise PlanError(f"job {name}: input name {key!r} must be letters, digits, '-' or '_'")
        if key in HANDOUT_FIELDS or key.startswith(HANDOUT_PREFIXES):
            raise PlanError(f"job {name}: input name {key} collides with a hand-out field")
    inputs = {str(key): _input(name, str(key), value) for key, value in raw_inputs.items()}
    raw_outputs = raw.get("outputs", [])
    if not isinstance(raw_outputs, list):
        raise PlanError(f"job {name}: outputs must be a list of names")
    outputs = tuple(raw_outputs)
    if not all(isinstance(output, str) and NAME.fullmatch(output) for output in outputs):
        raise PlanError(f"job {name}: output names must be letters, digits, '-' or '_'")
    if len(set(outputs)) != len(outputs):
        raise PlanError(f"job {name}: output names must be unique")
    role = raw.get("role")
    if role is not None and not outputs:
        raise PlanError(f"job {name}: a role-filling job needs a primary output")
    inputs = {key: replace(spec, source=role or "") if spec.address == "coverage" else spec
              for key, spec in inputs.items()}
    if kind == "model":
        allowed = {"name", "kind", "inputs", "outputs", "instruction", "role", "max-attempts", "parameters"}
        instruction = raw.get("instruction")
        if instruction not in inputs or inputs[instruction].address != "file" or not inputs[instruction].required:
            raise PlanError(f"job {name}: instruction must name a required file input")
        if not outputs:
            raise PlanError(f"job {name}: a model job needs an output")
        max_attempts = raw.get("max-attempts")
        if max_attempts is not None and (not isinstance(max_attempts, int) or max_attempts < 1):
            raise PlanError(f"job {name}: max-attempts must be a positive integer")
        parameters = raw.get("parameters") or {}
        if not isinstance(parameters, dict) or not all(
                isinstance(k, str) and NAME.fullmatch(k) and isinstance(v, str) and "\n" not in v
                for k, v in parameters.items()):
            raise PlanError(f"job {name}: parameters must map names to one-line strings")
        reserved = {*HANDOUT_FIELDS, *RUN_PLACEHOLDERS, *inputs}
        clash = sorted(k for k in parameters if k in reserved or k.startswith(HANDOUT_PREFIXES))
        if clash:
            raise PlanError(f"job {name}: parameters {clash} collide with names the hand-out sets")
        for key, value in parameters.items():
            for placeholder in PLACEHOLDER.findall(value):
                if placeholder not in RUN_PLACEHOLDERS and not (
                        placeholder.startswith("param:") and placeholder != "param:"):
                    raise PlanError(f"job {name}: parameter {key}: unknown placeholder {{{placeholder}}}")
        job: Job = ModelJob(name, inputs, outputs, instruction, role, max_attempts, dict(parameters))
    elif kind == "code":
        allowed = {"name", "kind", "inputs", "outputs", "handler", "role", "extensions"}
        handler = raw.get("handler")
        if not isinstance(handler, str) or "." not in handler:
            raise PlanError(f"job {name}: handler must be a dotted path")
        extensions = raw.get("extensions") or {}
        if not isinstance(extensions, dict) or not all(isinstance(key, str) for key in extensions):
            raise PlanError(f"job {name}: extensions must be a mapping with string keys")
        job = CodeJob(name, inputs, outputs, handler, role, dict(extensions))
    else:
        raise PlanError(f"job {name}: kind must be model or code")
    unknown = set(raw) - allowed
    if unknown:
        raise PlanError(f"job {name}: unknown keys {sorted(unknown)}")
    return job


def load_plan(text: str, roles: Mapping[str, Any] | None = None) -> Plan:
    """Parse a declaration; with `roles`, also check it against the type's roles."""
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise PlanError("a plan must be a mapping")
    reject_underscored_keys(data)
    unknown = set(data) - {"type", "criteria", "jobs", "prompt-section", "frozen-source"}
    if unknown:
        raise PlanError(f"unknown keys {sorted(unknown)}")
    groups = _criteria_groups(data.get("criteria", {}))
    if not isinstance(data.get("type"), str):
        raise PlanError("type must name the artifact's type, relative to the KB root")
    raw_jobs = data.get("jobs")
    if not isinstance(raw_jobs, list):
        raise PlanError("jobs must be a list")
    jobs = tuple(_job(_expand_criteria(raw, groups)) for raw in raw_jobs)
    if not jobs:
        raise PlanError("a plan declares at least one job")
    section = data.get("prompt-section")
    if section is not None and (not isinstance(section, str) or not section):
        raise PlanError("prompt-section must name the prompt section file, relative to the KB root")
    frozen = data.get("frozen-source")
    if frozen is not None and (not isinstance(frozen, str) or not frozen):
        raise PlanError("frozen-source must name a role")
    if frozen is not None and roles is not None and frozen not in roles:
        raise PlanError(f"frozen-source: role {frozen} is not declared by the type")
    plan = Plan(Path(data["type"]), tuple(_with_prompt_section(_with_refusal(job), section) for job in jobs),
                section, frozen)
    _check(plan, roles)
    return plan


def _criteria_groups(raw: Any) -> dict[str, dict[str, str]]:
    """Named groups of file inputs: each maps input names to library paths."""
    if not isinstance(raw, dict):
        raise PlanError("criteria must map group names to input mappings")
    groups = {}
    for name, members in raw.items():
        if (not isinstance(name, str) or not NAME.fullmatch(name) or not isinstance(members, dict)
                or not members or not all(isinstance(k, str) and isinstance(v, str) for k, v in members.items())):
            raise PlanError(f"criteria group {name!r} must map input names to library paths")
        groups[name] = dict(members)
    return groups


def _expand_criteria(raw: Any, groups: Mapping[str, Mapping[str, str]]) -> Any:
    """Replace a job's `criteria` list with the file inputs its groups name."""
    if not isinstance(raw, dict) or "criteria" not in raw:
        return raw
    name = raw.get("name")
    listed = raw["criteria"]
    if not isinstance(listed, list) or not all(isinstance(group, str) for group in listed):
        raise PlanError(f"job {name}: criteria must list group names")
    inputs = dict(raw.get("inputs") or {})
    for group in listed:
        if group not in groups:
            raise PlanError(f"job {name}: no criteria group {group}")
        for key, path in groups[group].items():
            given = {"address": "file", "source": path}
            if key in inputs and inputs[key] != given:
                raise PlanError(f"job {name}: input {key} disagrees with criteria group {group}")
            inputs[key] = given
    return {**{k: v for k, v in raw.items() if k != "criteria"}, "inputs": inputs}


def _with_prompt_section(job: Job, section: str | None) -> Job:
    """Give every model job the plan's prompt section as a file input.

    Pinned like the instruction, so editing the section is a change of
    input, not a silent change of every later prompt.
    """
    if section is None or not isinstance(job, ModelJob):
        return job
    if PROMPT_SECTION_INPUT in job.inputs:
        raise PlanError(f"job {job.name}: input {PROMPT_SECTION_INPUT} is reserved for the plan's prompt section")
    return replace(job, inputs={**job.inputs, PROMPT_SECTION_INPUT: Input("file", section)})


def _with_refusal(job: Job) -> Job:
    """Give a role-filling model job its refusal input if the declaration did not.

    A job's refusals are an input of that job whether or not it is declared;
    without one, a refusal of its output could be recorded and never answered.
    """
    if not isinstance(job, ModelJob) or job.role is None:
        return job
    if any(spec.address == "refusal" and spec.source == job.name for spec in job.inputs.values()):
        return job
    if REFUSAL_INPUT in job.inputs:
        raise PlanError(f"job {job.name}: input {REFUSAL_INPUT} is reserved for its refusals")
    inputs = {**job.inputs, REFUSAL_INPUT: Input("refusal", job.name, required=False)}
    return replace(job, inputs=inputs)


def check_relations(plan: Plan, relations: Sequence[str]) -> None:
    """Every relation a judgment input names must be one the type declares.

    An undeclared relation would make the input permanently absent, and a
    job gated on it would wait without any stop to say why.
    """
    declared = set(relations)
    for job in plan.jobs:
        for name, spec in job.inputs.items():
            if spec.address != "judgment" or spec.relation is None:
                continue
            if spec.relation not in declared:
                raise PlanError(
                    f"job {job.name}: input {name}: relation {spec.relation} is not declared by the type")
            origin, _, partner = spec.relation.split(":")
            if spec.source not in (origin, partner):
                raise PlanError(
                    f"job {job.name}: input {name}: role {spec.source} is at neither end of {spec.relation}")


def _check(plan: Plan, roles: Mapping[str, Any] | None) -> None:
    names = [job.name for job in plan.jobs]
    if len(set(names)) != len(names):
        raise PlanError("job names must be unique")
    filled = [job.role for job in plan.jobs if job.role]
    if len(set(filled)) != len(filled):
        raise PlanError("two jobs fill the same role")
    for job in plan.jobs:
        if roles is not None and job.role is not None and job.role not in roles:
            raise PlanError(f"job {job.name}: role {job.role} is not declared by the type")
        for name, spec in job.inputs.items():
            where = f"job {job.name}: input {name}"
            if spec.address in ("role", "judgment"):
                if roles is not None and spec.source not in roles:
                    raise PlanError(f"{where}: role {spec.source} is not declared by the type")
                if spec.address == "role" and spec.source == job.role:
                    raise PlanError(f"{where}: a job never has its own role as input")
            elif spec.address in ("output", "attempt", "refusal"):
                producer, _, output = spec.source.partition(":")
                if producer not in names:
                    raise PlanError(f"{where}: no job named {producer}")
                if producer == job.name and spec.address != "refusal":
                    raise PlanError(f"{where}: a job never has its own output as input")
                if spec.address == "output" and output not in plan.job(producer).outputs:
                    raise PlanError(f"{where}: {producer} has no output {output}")
            elif spec.address == "handed":
                attempt, _, handed = spec.source.partition(":")
                if attempt not in job.inputs or job.inputs[attempt].address != "attempt":
                    raise PlanError(f"{where}: {attempt} must be an attempt input of this job")
                producer = job.inputs[attempt].source
                if handed not in plan.job(producer).inputs:
                    raise PlanError(f"{where}: {producer} declares no input {handed} to hand")
