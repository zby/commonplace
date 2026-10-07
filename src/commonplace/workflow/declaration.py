"""The job-set declaration: a data file naming jobs, their inputs and outputs.

A job set declares the jobs that produce one type of set. It is data, not
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

ADDRESSES = ("file", "member", "output", "attempt", "handed", "judgment", "refusal")
PLACEHOLDER = re.compile(r"\{([^{}]*)\}")
RUN_PLACEHOLDERS = ("run", "run-id", "set", "workspace")
"""Values a parameter may substitute besides `param:<name>`, a run parameter."""
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
"""Job, input, output and parameter names: they become file and record names."""
RESERVED_JOBS = ("operator",)
"""Job names the engine uses for its own records."""
HANDOUT_FIELDS = ("job", "attempt", "run-id", "output", "problem", "workspace", "scratch")
HANDOUT_PREFIXES = ("output-", "previous-")
"""Names a hand-out prompt sets itself; inputs and parameters may not reuse them."""
REFUSAL_INPUT = "refusal"
"""The input name under which a role-filling model job receives its refusals."""
OUTCOMES = ("accepted", "refused")


class DeclarationError(ValueError):
    """A job set that cannot be run as declared."""


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
    """A code job runs its handler under the command."""

    name: str
    inputs: Mapping[str, Input]
    outputs: tuple[str, ...]
    handler: str
    role: str | None = None

    def resolve_handler(self) -> Callable:
        module, _, attribute = self.handler.rpartition(".")
        try:
            return getattr(importlib.import_module(module), attribute)
        except (ImportError, AttributeError) as error:
            raise DeclarationError(f"job {self.name}: handler {self.handler} does not resolve: {error}") from error


Job = ModelJob | CodeJob


@dataclass(frozen=True)
class JobSet:
    """A job set declares the jobs that produce one type of set."""

    type_spec: Path
    jobs: tuple[Job, ...]

    def job(self, name: str) -> Job:
        for job in self.jobs:
            if job.name == name:
                return job
        raise KeyError(name)

    def filler(self, role: str) -> Job | None:
        """The job whose primary output fills `role`."""
        return next((job for job in self.jobs if job.role == role), None)


def _input(job: str, name: str, raw: Any) -> Input:
    where = f"job {job}: input {name}"
    if not isinstance(raw, dict):
        raise DeclarationError(f"{where}: must be a mapping")
    unknown = set(raw) - {"address", "source", "required", "relation", "outcome", "order_only"}
    if unknown:
        raise DeclarationError(f"{where}: unknown keys {sorted(unknown)}")
    address, source = raw.get("address"), raw.get("source")
    if address not in ADDRESSES:
        raise DeclarationError(f"{where}: address must be one of {', '.join(ADDRESSES)}")
    if not isinstance(source, str) or not source:
        raise DeclarationError(f"{where}: source must be a nonempty string")
    required = raw.get("required", True)
    if not isinstance(required, bool):
        raise DeclarationError(f"{where}: required must be true or false")
    relation, outcome = raw.get("relation"), raw.get("outcome")
    if address == "judgment":
        if outcome not in OUTCOMES:
            raise DeclarationError(f"{where}: a judgment input needs an outcome of {' or '.join(OUTCOMES)}")
        if relation is not None and (not isinstance(relation, str) or relation.count(":") != 2):
            raise DeclarationError(f"{where}: relation must read <origin>:<kind>:<partner>")
    elif relation is not None or outcome is not None:
        raise DeclarationError(f"{where}: only a judgment input has a relation or an outcome")
    if address in ("output", "handed") and source.count(":") != 1:
        raise DeclarationError(f"{where}: source must read <name>:<name>")
    order_only = raw.get("order_only", False)
    if not isinstance(order_only, bool):
        raise DeclarationError(f"{where}: order_only must be true or false")
    return Input(address, source, required, relation, outcome, order_only)


def _job(raw: Any) -> Job:
    if not isinstance(raw, dict):
        raise DeclarationError("each job must be a mapping")
    name = raw.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name):
        raise DeclarationError(f"job name {name!r} must be letters, digits, '-' or '_'")
    if name in RESERVED_JOBS:
        raise DeclarationError(f"job name {name} is reserved for the engine's records")
    kind = raw.get("kind")
    raw_inputs = raw.get("inputs", {})
    if not isinstance(raw_inputs, dict):
        raise DeclarationError(f"job {name}: inputs must be a mapping")
    for key in raw_inputs:
        if not isinstance(key, str) or not NAME.fullmatch(key):
            raise DeclarationError(f"job {name}: input name {key!r} must be letters, digits, '-' or '_'")
        if key in HANDOUT_FIELDS or key.startswith(HANDOUT_PREFIXES):
            raise DeclarationError(f"job {name}: input name {key} collides with a hand-out field")
    inputs = {str(key): _input(name, str(key), value) for key, value in raw_inputs.items()}
    raw_outputs = raw.get("outputs", [])
    if not isinstance(raw_outputs, list):
        raise DeclarationError(f"job {name}: outputs must be a list of names")
    outputs = tuple(raw_outputs)
    if not all(isinstance(output, str) and NAME.fullmatch(output) for output in outputs):
        raise DeclarationError(f"job {name}: output names must be letters, digits, '-' or '_'")
    if len(set(outputs)) != len(outputs):
        raise DeclarationError(f"job {name}: output names must be unique")
    role = raw.get("role")
    if role is not None and not outputs:
        raise DeclarationError(f"job {name}: a role-filling job needs a primary output")
    if kind == "model":
        allowed = {"name", "kind", "inputs", "outputs", "instruction", "role", "max_attempts", "parameters"}
        instruction = raw.get("instruction")
        if instruction not in inputs or inputs[instruction].address != "file" or not inputs[instruction].required:
            raise DeclarationError(f"job {name}: instruction must name a required file input")
        if not outputs:
            raise DeclarationError(f"job {name}: a model job needs an output")
        max_attempts = raw.get("max_attempts")
        if max_attempts is not None and (not isinstance(max_attempts, int) or max_attempts < 1):
            raise DeclarationError(f"job {name}: max_attempts must be a positive integer")
        parameters = raw.get("parameters") or {}
        if not isinstance(parameters, dict) or not all(
                isinstance(k, str) and NAME.fullmatch(k) and isinstance(v, str) and "\n" not in v
                for k, v in parameters.items()):
            raise DeclarationError(f"job {name}: parameters must map names to one-line strings")
        reserved = {*HANDOUT_FIELDS, *RUN_PLACEHOLDERS, *inputs}
        clash = sorted(k for k in parameters if k in reserved or k.startswith(HANDOUT_PREFIXES))
        if clash:
            raise DeclarationError(f"job {name}: parameters {clash} collide with names the hand-out sets")
        for key, value in parameters.items():
            for placeholder in PLACEHOLDER.findall(value):
                if placeholder not in RUN_PLACEHOLDERS and not (
                        placeholder.startswith("param:") and placeholder != "param:"):
                    raise DeclarationError(f"job {name}: parameter {key}: unknown placeholder {{{placeholder}}}")
        job: Job = ModelJob(name, inputs, outputs, instruction, role, max_attempts, dict(parameters))
    elif kind == "code":
        allowed = {"name", "kind", "inputs", "outputs", "handler", "role"}
        handler = raw.get("handler")
        if not isinstance(handler, str) or "." not in handler:
            raise DeclarationError(f"job {name}: handler must be a dotted path")
        job = CodeJob(name, inputs, outputs, handler, role)
    else:
        raise DeclarationError(f"job {name}: kind must be model or code")
    unknown = set(raw) - allowed
    if unknown:
        raise DeclarationError(f"job {name}: unknown keys {sorted(unknown)}")
    return job


def load_job_set(text: str, roles: Mapping[str, Any] | None = None) -> JobSet:
    """Parse a declaration; with `roles`, also check it against the type's roles."""
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise DeclarationError("a job set must be a mapping")
    unknown = set(data) - {"type_spec", "jobs"}
    if unknown:
        raise DeclarationError(f"unknown keys {sorted(unknown)}")
    if not isinstance(data.get("type_spec"), str):
        raise DeclarationError("type_spec must name the set's type, relative to the KB root")
    raw_jobs = data.get("jobs")
    if not isinstance(raw_jobs, list):
        raise DeclarationError("jobs must be a list")
    jobs = tuple(_job(raw) for raw in raw_jobs)
    if not jobs:
        raise DeclarationError("a job set declares at least one job")
    job_set = JobSet(Path(data["type_spec"]), tuple(_with_refusal(job) for job in jobs))
    _check(job_set, roles)
    return job_set


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
        raise DeclarationError(f"job {job.name}: input {REFUSAL_INPUT} is reserved for its refusals")
    inputs = {**job.inputs, REFUSAL_INPUT: Input("refusal", job.name, required=False)}
    return replace(job, inputs=inputs)


def check_relations(job_set: JobSet, relations: Sequence[str]) -> None:
    """Every relation a judgment input names must be one the type declares.

    An undeclared relation would make the input permanently absent, and a
    job gated on it would wait without any stop to say why.
    """
    declared = set(relations)
    for job in job_set.jobs:
        for name, spec in job.inputs.items():
            if spec.address != "judgment" or spec.relation is None:
                continue
            if spec.relation not in declared:
                raise DeclarationError(
                    f"job {job.name}: input {name}: relation {spec.relation} is not declared by the type")
            origin, _, partner = spec.relation.split(":")
            if spec.source not in (origin, partner):
                raise DeclarationError(
                    f"job {job.name}: input {name}: role {spec.source} is at neither end of {spec.relation}")


def _check(job_set: JobSet, roles: Mapping[str, Any] | None) -> None:
    names = [job.name for job in job_set.jobs]
    if len(set(names)) != len(names):
        raise DeclarationError("job names must be unique")
    filled = [job.role for job in job_set.jobs if job.role]
    if len(set(filled)) != len(filled):
        raise DeclarationError("two jobs fill the same role")
    for job in job_set.jobs:
        if roles is not None and job.role is not None and job.role not in roles:
            raise DeclarationError(f"job {job.name}: role {job.role} is not declared by the type")
        for name, spec in job.inputs.items():
            where = f"job {job.name}: input {name}"
            if spec.address in ("member", "judgment"):
                if roles is not None and spec.source not in roles:
                    raise DeclarationError(f"{where}: role {spec.source} is not declared by the type")
                if spec.address == "member" and spec.source == job.role:
                    raise DeclarationError(f"{where}: a job never has its own role as input")
            elif spec.address in ("output", "attempt", "refusal"):
                producer, _, output = spec.source.partition(":")
                if producer not in names:
                    raise DeclarationError(f"{where}: no job named {producer}")
                if producer == job.name and spec.address != "refusal":
                    raise DeclarationError(f"{where}: a job never has its own output as input")
                if spec.address == "output" and output not in job_set.job(producer).outputs:
                    raise DeclarationError(f"{where}: {producer} has no output {output}")
            elif spec.address == "handed":
                attempt, _, _ = spec.source.partition(":")
                if attempt not in job.inputs or job.inputs[attempt].address != "attempt":
                    raise DeclarationError(f"{where}: {attempt} must be an attempt input of this job")
