"""Version-1 public API proposal; all behavior is deliberately `...`.

Not runtime code. See api-design.md for invariants and deferred features.
The directory type supplies slots, relations and disposition requirements.
No public storage records, hashes, judgment constructors or operator overrides.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class Read:
    """A named declared input, with absence recorded even when optional.

    file: a run-relative or explicitly absolute file path.
    member: a type-declared member name.
    candidate/verdict: 'producer-job:output-name'. Verdict reads additionally
        track the producing input identities, even for identical verdict bytes.
    acceptance: holding coverage for a member and the named relations.
    findings: a member's current correction findings, managed by the engine.
        Includes structural rejection and its designated verifier's findings.
    """

    kind: Literal["file", "member", "candidate", "verdict", "acceptance", "findings"]
    source: str
    required: bool = True
    relations: tuple[str, ...] = ()  # Only for acceptance reads.


@dataclass(frozen=True)
class ModelJob:
    name: str
    reads: Mapping[str, Read]
    outputs: tuple[str, ...]
    instruction: str  # Alias of a required declared file read.
    max_attempts: int
    member: str | None = None  # Disposition gate; one primary member output.
    previous: bool = False  # Prior output in the prompt, pinned but not a trigger.


@dataclass(frozen=True)
class CodeJob:
    name: str
    reads: Mapping[str, Read]
    outputs: tuple[str, ...]
    run: Callable[[CodeContext], Mapping[str, bytes]]
    max_attempts: int
    member: str | None = None  # Also gates checks of disposition-specific members.


@dataclass(frozen=True)
class JobSet:
    type_spec: Path
    jobs: tuple[ModelJob | CodeJob, ...]
    # One semantic apply job owns the complete verifier findings per member.
    # Structural candidate checks are separate, not additional semantic owners.
    verifier_owners: Mapping[str, str] = field(default_factory=dict)


class CodeContext:
    """Only declared, immutable attempt inputs are available here.

    Judgment calls stage changes; the engine commits them with returned output
    bytes only after the handler succeeds. Raising leaves a failure record,
    installs nothing and stops the invocation. Handlers are trusted, not sandboxed.
    """

    def read(self, name: str) -> bytes | None:
        """Read an input alias; None means an optional input was absent."""
        ...

    def accept_candidate(self, name: str, *, relations: tuple[str, ...]) -> None:
        """Accept a candidate/verdict input at its producer's member slot.

        Basis is the check's pinned reads. Covered partners must be declared.
        Late acceptance never restores an obsolete candidate over a newer one.
        """
        ...

    def refuse_candidate(self, name: str, *, findings: str) -> None:
        """Reject this candidate structurally; its producer receives the findings."""
        ...

    def apply_verdict(
        self,
        name: str,
        *,
        scopes: Mapping[str, tuple[str, ...]],
        findings: Mapping[str, str],
    ) -> None:
        """Translate a parsed verdict into judgments of the versions it saw.

        `name` is a declared verdict input. Keys in scopes/findings are member
        input aliases of its producing model job; scope values are relation
        names of those members. An alias absent from findings is accepted;
        a present alias is refused with nonempty findings. Findings keys must
        be a subset of scopes. This is the owner's COMPLETE finding set, not
        a patch. The handler parses the consumer's document format first.

        The engine supplies subject versions and basis from producer pins,
        validates ownership/relations, and rejects invalid claims. Stale
        verdicts remain historical; they neither settle nor restore replacements.
        This does not structurally accept the verdict document itself.
        """
        ...


@dataclass(frozen=True)
class Completion:
    """Report a hand-out by attempt ID, never infer completion from file presence.

    finished captures the hand-out's staged outputs; failed retains a worker
    problem; abandoned asserts the coordinator has stopped/joined the worker.
    Failure and abandonment require a reason and consume the attempt budget.
    """

    attempt: str
    outcome: Literal["finished", "failed", "abandoned"]
    reason: str = ""
    runner: str | None = None
    model: str | None = None
    effort: str | None = None


@dataclass(frozen=True)
class Handout:
    attempt: str
    job: str
    prompt: Path  # Contains pinned input paths, optional absences and previous output.
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
    jobs: JobSet,
    *,
    completions: tuple[Completion, ...] = (),
) -> Advance:
    """Validate declarations and completions under one coordinator lock.

    Capture reported completions with their opening pins; recover derived slots;
    run ready code jobs to a fixed point; open all ready model attempts. Stop
    on failure, uncertainty or exhausted bounds. Existing open attempts remain
    visible, not presumed dead. Repeated identical completions are idempotent.
    All storage, currency, coverage and recovery records are internal.
    """
    ...
