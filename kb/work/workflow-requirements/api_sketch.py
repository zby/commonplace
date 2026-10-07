"""Public API sketch for requirements.md; implementations deliberately use `...`.

Not runtime code. The run metadata names a fixed job-set file, which names the
set type. Attempts, versions and judgments live beside the typed output set.
Storage records and currency calculations are not public APIs.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class Read:
    """A file/view resolved and pinned when an attempt opens.

    file: run-relative or explicitly absolute path.
    member: type-declared slot name.
    output: 'producer-job:output-name', its current candidate/output version.
    judgment: latest judgment addressed by member, relation and outcome.
        A required judgment read is present only while that judgment holds.
    refusal: producer-job name, its latest refusal with version and findings.

    All views have content identity. Optional absence is recorded explicitly.
    """

    kind: Literal["file", "member", "output", "judgment", "refusal"]
    source: str
    required: bool = True
    relation: str | None = None  # Judgment address; None means unscoped.
    outcome: Literal["accepted", "refused"] | None = None  # Judgment address.


@dataclass(frozen=True)
class ModelJob:
    name: str
    reads: Mapping[str, Read]
    outputs: tuple[str, ...]
    instruction: str  # Alias of a required file read.
    member: str | None = None  # Type disposition gates a member producer.
    max_attempts: int | None = None  # Optional run-wide bound, never reset.
    # Previous attempt outputs are always supplied as pinned context, not reads.


@dataclass(frozen=True)
class CodeJob:
    name: str
    reads: Mapping[str, Read]
    outputs: tuple[str, ...]
    run: Callable[[CodeContext], Mapping[str, bytes]]
    member: str | None = None
    # No bound: code-job failure stops the invocation for operator action.


@dataclass(frozen=True)
class JobSet:
    """Declared in its own file under the workflow instructions.

    A member-producing job's first output is its primary member output. Other
    named outputs are auxiliary files. The type supplies slots and relations only;
    it neither names producers nor points back to this declaration.
    """

    type_spec: Path
    jobs: tuple[ModelJob | CodeJob, ...]


class CodeContext:
    """Declared immutable reads and staged judgments for one code attempt.

    The handler returns named output bytes. Outputs and judgments commit
    together, with the whole attempt record written last. Raising commits no
    outputs or judgments, retains a failure record, and stops the invocation.
    Handlers are trusted, not sandboxed; no live-directory reader is supplied.
    """

    def read(self, name: str) -> bytes | None:
        """Read a declared input alias; None records optional absence."""
        ...

    def judge(
        self,
        target: str,
        *,
        outcome: Literal["accepted", "refused"],
        relations: tuple[str, ...] = (),
        findings: str = "",
        overrides: tuple[str, ...] = (),
    ) -> None:
        """Stage a judgment of one exact version, against this attempt's reads.

        target is a declared member/output input alias, or this job's primary
        member output name (resolved from the bytes returned by the handler).
        The member slot is resolved from the declaration. Covered relation
        partners must be among the declared reads. Overrides name refusal IDs.

        Acceptance installs that version at its slot, including historical
        versions. Refusal supplies its producer with the version and findings.
        The engine knows nothing about structural checks or verdict documents;
        consumer code parses documents and calls this same primitive.
        """
        ...


@dataclass(frozen=True)
class Completion:
    """Close an open model attempt explicitly, using its original input pins.

    finished captures the staged outputs; missing output makes it a failure.
    failed closes a worker problem or abandonment with a nonempty reason.
    A killed worker's attempt remains open until reported. The coordinator must
    stop/join a worker before reporting abandonment as failed.
    """

    attempt: str
    outcome: Literal["finished", "failed"] = "finished"
    reason: str = ""
    runner: str | None = None
    model: str | None = None
    effort: str | None = None


@dataclass(frozen=True)
class OperatorJudgment:
    """The command-line operator uses the same judgment primitive.

    version is a retained version identity, not new bytes. Reads are explicitly
    supplied basis files/views, pinned at this invocation; scope must be covered
    by them. Accepting a historical version restores it at the member slot.
    """

    member: str
    version: str
    outcome: Literal["accepted", "refused"]
    reads: Mapping[str, Read]
    relations: tuple[str, ...] = ()
    findings: str = ""
    overrides: tuple[str, ...] = ()


@dataclass(frozen=True)
class Handout:
    attempt: str
    job: str
    prompt: Path  # Pinned reads, optional absences and previous attempt outputs.
    outputs: Mapping[str, Path]
    problem: Path


@dataclass(frozen=True)
class Stop:
    reason: str
    job: str | None = None
    attempt: str | None = None


@dataclass(frozen=True)
class Advance:
    handouts: tuple[Handout, ...]
    open_attempts: tuple[str, ...]
    stops: tuple[Stop, ...]
    publishable: bool


def advance(
    directory: Path,
    *,
    completions: tuple[Completion, ...] = (),
    judgments: tuple[OperatorJudgment, ...] = (),
) -> Advance:
    """Load the fixed job set named in this run's opening metadata.

    Under one coordinator lock, process reported completions and operator
    judgments before readiness; re-materialize slots from acceptance records;
    run ready code jobs to a fixed point; open all ready model attempts.
    Stop on failure, uncertainty or an exhausted model bound. Existing open
    attempts are left alone and reported. Completion retries are idempotent.

    Currency is content-only. Refusal readiness and scoped supersession follow
    requirement 7. Failed attempts record no reads and stay ready for a later
    invocation. Type disposition gates member producers. Publication coverage
    is the union of holding acceptances for current member versions.
    """
    ...
