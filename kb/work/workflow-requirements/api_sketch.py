"""Public API sketch for requirements.md; implementations deliberately use `...`.

Not runtime code. The run metadata names a fixed job-set file, which names the
set type. Attempts, versions and judgments live beside the typed set.
Job declarations below describe the data-file schema, not executable Python
configuration. Operator entry points are outside this sketch by request.
Storage records and currency calculations are not public APIs.
Names follow glossary.md.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class Input:
    """An input is something a job depends on, required or optional.

    The engine resolves it to one version when an attempt opens and pins it.
    `address` names what it resolves to:

    file: run-relative or explicitly absolute path.
    member: the current member of a type-declared role.
    output: 'producer-job:output-name', the producer's latest completed output.
    attempt: producer-job name, its latest completed attempt record, including
        the versions it was handed. The record itself is a rerun trigger.
    handed: 'attempt-input-name:producer-input-name', the version that the
        declared attempt record says that attempt was handed. The indirection
        is fixed in the declaration; it adds no dependency at run time. The
        role is preserved, so judge() can take that version as its subject.
    judgment: latest judgment addressed by role, relation and outcome.
        A required judgment input is present only while that judgment holds.
    refusal: producer-job name, the latest refusal of its latest completed
        output, with the refused version, the findings and the refusal's
        identity, which an override names; never a historical refusal.

    All addresses resolve to content identity. Optional absence is recorded explicitly.
    An input that lapses has not changed and schedules no rerun. A refusal
    input lapses after a newer output; a required judgment input lapses when
    the judgment stops holding. Handed inputs require a declared attempt
    input; unknown names or missing version records are errors, never a
    fallback to the current member.
    """

    address: Literal["file", "member", "output", "attempt", "handed", "judgment", "refusal"]
    source: str
    required: bool = True
    relation: str | None = None  # Judgment address, '<kind>:<partner role>'.
    outcome: Literal["accepted", "refused"] | None = None  # Judgment address.


@dataclass(frozen=True)
class ModelJob:
    """A model job is handed out to a worker; the command never calls a model."""

    name: str
    inputs: Mapping[str, Input]
    outputs: tuple[str, ...]
    instruction: str  # Name of a required file input.
    role: str | None = None  # The role its primary output fills; disposition gates it.
    bound: int | None = None  # Most attempts in the run; never reset.
    # The previous output is always supplied by identity; it is not an input.


@dataclass(frozen=True)
class CodeJob:
    """A code job runs its handler under the command."""

    name: str
    inputs: Mapping[str, Input]
    outputs: tuple[str, ...]
    handler: str  # Dotted package path; handler(attempt) returns named output bytes.
    role: str | None = None
    # No bound: code-job failure stops the invocation.


@dataclass(frozen=True)
class JobSet:
    """A job set declares the jobs that produce one type of set.

    It is the schema of a declaration file under the workflow instructions,
    not code. The loader resolves handlers from dotted paths into the
    package; instruction trees install as shared data, not Python modules.
    A role-filling job's first output is its primary output; other outputs
    are auxiliary. The type supplies roles and relations only; it neither
    names producers nor points back to this declaration.
    """

    type_spec: Path  # Relative to the KB root.
    jobs: tuple[ModelJob | CodeJob, ...]


class CodeAttempt:
    """A code attempt gives a handler its pinned inputs and stages its judgments.

    The handler returns named output bytes. Outputs and judgments commit
    together, with the whole attempt record written last. Raising commits no
    outputs or judgments, retains a failure record, and stops the invocation.
    Handlers are trusted, not sandboxed; no live-directory reader is supplied.
    """

    def read(self, name: str) -> bytes | None:
        """Read a declared input by name; None records optional absence."""
        ...

    def judge(
        self,
        subject: str,
        *,
        outcome: Literal["accepted", "refused"],
        scope: tuple[str, ...] = (),
        findings: str = "",
        overrides: tuple[str, ...] = (),
    ) -> None:
        """Stage a judgment of one subject version, with this attempt's inputs as basis.

        subject is the name of a declared member, output or handed input, or
        this job's primary output name (resolved from the bytes the handler
        returns). The role is resolved from the declaration. Scope names
        relations as '<kind>:<partner role>', whose partners must be in the
        basis. Overrides name refusal identities. For publication, a relation
        is covered only when the partner version in the basis is that
        partner's current member; handed versions alone cannot supply coverage.

        Acceptance installs only the producing job's latest completed output.
        A judgment of an earlier version is evidence only and moves nothing;
        only refusals of the latest completed output enter its producer's
        refusal input. The engine knows nothing about structural checks or
        verdict documents; consumer code parses documents and calls this
        same primitive.
        """
        ...


@dataclass(frozen=True)
class AttemptResult:
    """An attempt result closes one open model attempt as completed or failed.

    completed captures the staged outputs against the attempt's pinned
    inputs; missing output makes it failed. failed closes a worker problem or
    abandonment with a nonempty reason. A killed worker's attempt stays open
    until reported. The coordinator must stop or join a worker before
    reporting its abandonment as failed. model and effort identify the worker.
    """

    attempt: str
    outcome: Literal["completed", "failed"] = "completed"
    reason: str = ""
    model: str | None = None
    effort: str | None = None


@dataclass(frozen=True)
class Handout:
    """A hand-out is an open model attempt's prompt and output paths."""

    attempt: str
    job: str
    prompt: Path  # Pinned inputs, optional absences and the previous output.
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


def advance(
    run_dir: Path,
    *,
    results: tuple[AttemptResult, ...] = (),
) -> RunStatus:
    """Run one invocation over the run directory and return its run status.

    Load the fixed job set named in this run's opening metadata. Editing its
    bounds grants no further attempts in this run; a changed declaration is
    a method change and makes the run unpublishable.

    Under one coordinator lock, close reported attempts before readiness;
    re-materialize members from acceptance records; run ready code jobs to a
    fixed point; open all ready model attempts. Stop on failure, uncertainty
    or an exhausted bound. Existing open attempts are left alone and
    reported. Repeated attempt results are idempotent.

    Currency is content-only. An input that appears or differs triggers
    readiness; one that lapses does not. Missing required inputs still block
    readiness. Refusal readiness and scoped supersession follow requirement
    7. Failed attempts record no inputs and stay ready for a later
    invocation. Type disposition gates role-filling jobs. Bounds never reset
    or increase within the run; another model attempt requires a new run.
    Publication coverage is the union of holding acceptances of current
    members, counting a relation only when its partner in the basis is the
    partner's current member.
    """
    ...
