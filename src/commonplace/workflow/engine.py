"""The code orchestrator.

A workflow definition is ordinary synchronous code. It names jobs with
`agent()`, which returns a handle at once, and asks for results with `wait()`.
A wait on a job that is not yet accepted cannot be satisfied inside this
process, so it ends the path it is on. Nothing is resumed: the next `step`
runs the definition from the top, and accepted outputs let it pass the waits
it stopped at before. No asynchronous library is involved.

A definition has three kinds of step.

A job is executed by a worker, a sub-agent. Its result is a file in the run
directory, judged by code.

A mechanical step is executed by code and can be replayed: run again on the
same files, it gives the same result and changes nothing further. It is
ordinary code in the definition, with no call into this package, and it runs
again at every replay.

An effect is executed by code and must run once, for one of two reasons. It
changes the world outside the run, as publishing a result does. Or its result
cannot be reproduced, as with resolving a branch to a commit, fetching a web
page, or reading the clock. Where a step writes is not the test: a snapshot
written into the run directory is an effect. An effect is declared with
`Context.effect`, which runs it once.

Where only part of a step must run once, split it. Resolving a revision to a
commit is an effect; fetching the objects of the recorded commit is a
mechanical step.
"""

from __future__ import annotations

import copy
import importlib
import inspect
import os
import traceback
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from pathlib import Path
from typing import Any

from commonplace.workflow.job import (
    RESERVED,
    DefinitionError,
    Job,
    check_name,
    normalized,
)
from commonplace.workflow.store import (
    FORMAT,
    RunBusy,
    RunStore,
    StateError,
    canonical,
    dump,
    file_sha,
    new_job,
    sha,
    write_atomic,
)

__all__ = [
    "REPORT_EVENTS",
    "Block",
    "Blocked",
    "Context",
    "Done",
    "Handout",
    "JobHandle",
    "Launch",
    "Orchestrator",
    "Recognition",
    "Report",
    "RunBusy",
    "StateError",
    "StepResult",
    "Uncertain",
    "Workflow",
    "load_definition",
]

REPORT_EVENTS = ("launch-failed", "repair", "stop")
"""The events the agent orchestrator reports. Any other event is refused."""

REPAIR = "repair"
STOP = "stop"


# Outcomes of a step


@dataclass(frozen=True)
class Handout:
    """One job for the agent orchestrator to launch.

    `prompt_path` holds the worker's whole task. `attempt` counts the times
    this job has been handed out in the run. `launch` is the job's launch
    parameters, unchanged.
    """

    name: str
    attempt: int
    prompt_path: Path
    output_path: Path
    problem_path: Path
    launch: Mapping[str, Any]


@dataclass(frozen=True)
class Launch:
    """Launch these jobs, wait for all of them, then run `step` again.

    The jobs are every job the definition has named and that is not accepted,
    ordered by name.
    """

    jobs: tuple[Handout, ...]


@dataclass(frozen=True)
class Done:
    """The definition ran to its end, every job it named is accepted, and
    every effect recorded in the run was reached in this step or its state
    was recorded by the operator."""


@dataclass(frozen=True)
class Block:
    """Something code cannot get past.

    `subject` is a job name, `workflow` when a step that code executes
    failed, or `effect <name>` when a completed effect no longer matches its
    inputs or is no longer reached. No job can be named `workflow`, and a job
    name has no space, so the three kinds cannot be confused. `reason` is one
    short line. `record_path` is a file with the details: attempts, validator
    messages, the worker's problem report, the error, and the agent
    orchestrator's reports. `permitted` is `repair` or `stop`. `scope` is what
    a repair may change, as the definition declares it.
    """

    subject: str
    reason: str
    record_path: Path
    permitted: str
    scope: str


@dataclass(frozen=True)
class Blocked:
    """Code cannot proceed. No job is handed out in a blocked step.

    After a repair, the next `step` judges the output in place again with the
    same validator. If it is still refused, the job is handed out again with
    a full set of attempts: the retry limit starts over after each blocked
    outcome. The repair limit does not. A block caused by a problem report
    leaves nothing in place to judge, because the report and any output
    beside it were moved into `workflow-state/` when the block was given.

    A block that permits only stopping ends what the agent orchestrator may
    do, not the run. Every `step` gives it again until the operator acts, with
    `Orchestrator.release` for a job or `workflow`, or by establishing the
    state of an effect. The run then continues with its accepted outputs.
    """

    blocks: tuple[Block, ...]


@dataclass(frozen=True)
class Uncertain:
    """An effect may or may not have taken place.

    Every later `step` gives the same outcome until the operator has
    established what took place and recorded it with `Orchestrator.resolve`.
    An uncertain step changes no job's state: it hands out nothing, moves
    nothing, and counts no attempt and no repair. `blocks` holds the blocks
    found in the same step, so that none is lost; they are counted when a
    later step gives them as Blocked.
    """

    effect: str
    detail: str
    blocks: tuple[Block, ...] = ()


StepResult = Launch | Done | Blocked | Uncertain


@dataclass(frozen=True)
class Report:
    """One observation recorded by the agent orchestrator."""

    number: int
    event: str
    job: str | None
    text: str
    recorded_at: str


class Recognition(Enum):
    """What can be established about an effect from the effect itself.

    COMPLETED: the effect took place in full. ABSENT: nothing of it took
    place, so running it is safe. UNKNOWN: neither can be established, for
    example because part of it took place.
    """

    COMPLETED = "completed"
    ABSENT = "absent"
    UNKNOWN = "unknown"


# The definition's side


class Workflow:
    """Base class of workflow definitions. A definition overrides `run`.

    retry_limit
        How many times code hands a job out again after a refused or missing
        output before it gives a blocked outcome. The count starts over when
        the job is accepted and after each blocked outcome.
    repair_limit
        How many blocked outcomes for one subject permit a repair. The next
        one permits only stopping. For a job, its acceptance resets the count.
        For `workflow`, failures are counted by the place in the definition
        where the error was raised: the innermost frame of the traceback that
        lies in the file defining the workflow class or one of its base
        classes. An error raised inside a shared helper or the standard
        library is therefore counted at the definition's line that called it,
        so two unrelated failing steps each get their repair. A step in which
        nothing that code executes fails resets these counts.
    repair_scope
        What the agent orchestrator may change during a repair.
    params
        The parameters the run was started with.
    """

    retry_limit = 1
    repair_limit = 1
    repair_scope = (
        "repair conditions (the environment, a missing input, a misnamed file) or "
        "remove a bad output; do not write or edit the content of a job's output, "
        "and do not change anything under workflow-state/"
    )

    params: Mapping[str, Any]

    def __init__(self, params: Mapping[str, Any] | None = None) -> None:
        self.params = dict(params or {})

    def run(self, ctx: Context) -> None:
        """The workflow. It must give the same jobs when it is run again on the
        same run directory, and every step in it must be safe to meet again."""
        raise NotImplementedError

    def run_location(self) -> tuple[str, str] | None:
        """Where `Orchestrator.start` puts a new run of this definition.

        Returns the directory that holds the runs, relative to the directory
        `start` is given, and the stem of the new run's name; `start` appends
        `-01`, `-02` and so on and takes the first name not in use. It is asked
        once, when the run starts, so it may use the date or the parameters.
        None, the default, means the caller names the run directory.
        """
        return None


class _PathEnded(BaseException):
    """The path cannot continue in this step.

    A BaseException, so that a definition catching `Exception` does not
    swallow it.
    """


class JobHandle:
    """What `agent()` returns. Naming a job does not wait for it."""

    job: Job
    path: Path

    def __init__(self, job: Job, path: Path, accepted: bool) -> None:
        self.job = job
        self.path = path
        self._accepted = accepted

    @property
    def accepted(self) -> bool:
        """Whether the job's output is accepted in this step."""
        return self._accepted

    def wait(self) -> Path:
        """The path of the accepted output.

        When the job is not accepted, the path of the definition that called
        `wait` ends here for this step. A definition that catches `Exception`
        does not catch this.
        """
        if not self._accepted:
            raise _PathEnded
        return self.path


class Context:
    """What a definition may use while it runs.

    The run's parameters are on the definition itself, as `self.params`.
    """

    run_dir: Path

    def __init__(self, step: _Step) -> None:
        self._step = step
        self.run_dir = step.run_dir

    def agent(self, job: Job) -> JobHandle:
        """Name a job and return its handle at once.

        The job is judged here. It is accepted when its output passes the
        job's current validator, the input state is the one recorded at
        hand-out, and the output's bytes are those accepted before, if it was
        accepted before. The input state is `Job.prompt`, the declared
        inputs' bytes and the launch parameters. It holds no absolute path of
        the run directory, so a run directory that is moved keeps its
        acceptances.

        An output that was never accepted, found when the input state differs
        from the one recorded at its hand-out, is refused. Such a refusal
        counts as a failed attempt, as a missing or invalid output does. An
        accepted output whose inputs change later, whose bytes someone
        changes, or that a changed validator now refuses, is not a failed
        attempt: the job is pending again with a full set of attempts.

        A job that is not accepted is handed out at the end of the step,
        whether or not the definition waits on it. At hand-out, whatever is at
        the job's output and problem report paths is moved into
        `workflow-state/` and kept there; nothing is deleted. This includes a
        refused output, an accepted output that someone changed, and one that
        a changed validator refuses.

        A job whose declared inputs include the output of another job named
        in the same step and not accepted raises DefinitionError: a worker
        would read a result that does not exist yet, or an accepted result
        would be used while the output it was made from is being replaced.
        This holds for an accepted job too, so that its `wait` cannot pass
        while its producer is pending. The definition waits on the producer
        first. The check is made when the second of the two jobs is named, so
        it does not depend on the order of the two calls. When an accepted
        consumer is named and waited on before its producer, what the
        definition does between the two calls runs before the check.

        The input state is compared at hand-out and when the output is
        judged, not in between. An input changed and changed back while the
        worker ran goes unseen, so an output made from the passing bytes can
        be accepted. The one-writer rule for a run covers inputs too.

        Naming the same job twice gives the same handle. Each job owns two
        paths, its output and its problem report. One name for two tasks that
        differ by `Job.same_task_as`, or a path owned by two jobs, raises
        DefinitionError. Paths are compared after normalization, so `a.md` and
        `./a.md` are the same path. A DefinitionError leaves the step without
        a result, so no job is handed out in a step that raises one.
        """
        return self._step.agent(job)

    def wait(self, *handles: JobHandle) -> list[Path]:
        """The accepted outputs, in the order asked.

        When any of the jobs is not accepted, the calling path ends here for
        this step.
        """
        if not all(handle.accepted for handle in handles):
            raise _PathEnded
        return [handle.path for handle in handles]

    def parallel(self, *paths: Callable[[], Any]) -> list[Any]:
        """Run independent paths and return what each returned, in order.

        Each path is a function without arguments. Each runs to its end or to
        its first wait on a job that is not accepted; a path that ends at a
        wait does not keep the others from running. When any path ended at a
        wait, the calling path ends here too. An error on one path does not
        keep the others from running; it becomes a block on `workflow`.
        """
        results: list[Any] = []
        ended = False
        for path in paths:
            try:
                results.append(path())
            except _PathEnded:
                ended = True
            except DefinitionError:
                raise
            except Exception as error:  # noqa: BLE001 - becomes a block on `workflow`
                self._step.errors.append(error)
                ended = True
        if ended:
            raise _PathEnded
        return results

    def effect(
        self,
        name: str,
        do: Callable[[], None],
        *,
        inputs: Sequence[str] = (),
        recognize: Callable[[], Recognition] | None = None,
    ) -> None:
        """Run an effect, once.

        An effect is a step that code executes and that must run once,
        because it changes the world outside the run or because its result
        cannot be reproduced. `name` identifies it within the run. `do`
        performs it and returns nothing: an effect that produces a value
        writes it to a file in the run directory, where later steps read it.
        `inputs` are the files the effect is made from, as a job's inputs
        are; their state is recorded before `do` runs.

        A step that can be replayed is not an effect and is not declared
        here, wherever it writes.

        Code does not repeat or undo an effect. When it is completed and its
        inputs have changed since, what is outside no longer matches the run:
        the step gives a blocked outcome on `effect <name>` that permits only
        stopping, and the run does not report Done. The block is judged anew
        in every step and is not stored. It goes away when the inputs are back
        in the recorded state, or when the operator records the state of the
        effect with `Orchestrator.resolve`.

        A process can complete the effect and end before recording it. When a
        started effect has no completion record, `recognize` establishes from
        the effect itself what took place. COMPLETED: the effect is recorded
        and `do` does not run. ABSENT: `do` runs. UNKNOWN, an error raised by
        `recognize`, or no `recognize` at all: the step gives the Uncertain
        outcome and `do` does not run.

        What `recognize` has to do depends on why the effect must run once.
        An effect that changes the world outside may have taken place in
        part, so `recognize` inspects the state outside. An effect whose
        result cannot be reproduced is harmless to run again before its
        result is recorded, so its `recognize` gives COMPLETED when the file
        it writes exists and ABSENT otherwise. Leaving `recognize` out of
        such an effect stops the run as uncertain for no reason.

        An error raised by `do` leaves the effect started and not recorded,
        as a process that ended would. The step gives a block on `workflow`
        with the error. The next step asks `recognize` what took place.

        An effect stays owed after the definition stops calling it, for
        example because a later job's result changed a branch. When the
        definition runs to its end, every effect recorded in the run must have
        been reached in that step. One that was not is checked there: a
        completed effect gives a block on `effect <name>` that permits only
        stopping, and a started effect without a completion record gives the
        Uncertain outcome, because its `recognize` is supplied only at the
        call. A step that ends at a wait before reaching the end checks
        nothing, since the definition may still reach the call. The operator
        settles an effect that is no longer reached with
        `Orchestrator.resolve`.
        """
        self._step.effect(name, do, [str(path) for path in inputs], recognize)


# The orchestrator


def load_definition(reference: str) -> type[Workflow]:
    """Resolve `package.module:ClassName` to a workflow class.

    Raises ValueError when the reference cannot be loaded or does not name a
    workflow definition.
    """
    module_name, colon, attribute = reference.partition(":")
    if not colon or not module_name or not attribute:
        raise ValueError(
            f"{reference!r} is not a workflow reference of the form "
            "package.module:ClassName"
        )
    try:
        module = importlib.import_module(module_name)
    except ImportError as error:
        raise ValueError(f"cannot import {module_name}: {error}") from None
    found = getattr(module, attribute, None)
    if not (
        isinstance(found, type)
        and issubclass(found, Workflow)
        and found is not Workflow
    ):
        raise ValueError(f"{reference} does not name a workflow definition")
    return found


class Orchestrator:
    """Advances one run. It keeps nothing between two calls of `step`.

    All state is in the run directory, under `workflow-state/`. Two
    orchestrators made for the same run directory behave as one.

    The state records carry a format version. Records that are missing where
    the run requires them, do not parse, disagree, or carry another version
    raise StateError from `step`, `resolve`, `release` and `open`; they are
    refused, not reshaped.

    The constructor takes a definition object and records nothing about it.
    A run driven only through the constructor cannot be opened with `open` or
    by the shell; `create` is what records the definition.
    """

    run_dir: Path
    workflow: Workflow

    def __init__(self, run_dir: Path, workflow: Workflow) -> None:
        self.run_dir = Path(run_dir).absolute()
        self.workflow = workflow
        self._store = RunStore(self.run_dir)

    @classmethod
    def create(
        cls, run_dir: Path, definition: str, params: Mapping[str, Any] | None = None
    ) -> Orchestrator:
        """Start a run: record which definition it uses and with what parameters.

        `definition` is a reference as `load_definition` takes it. Raises
        ValueError when the directory already holds a started run.
        """
        run_dir = Path(run_dir).absolute()
        store = RunStore(run_dir)
        if store.run_file.exists():
            raise ValueError(f"{run_dir} already holds a started run")
        workflow = load_definition(definition)(params)
        record = {"format": FORMAT, "definition": definition, "params": workflow.params}
        try:
            text = dump(record)
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"the parameters are not serializable as JSON: {error}"
            ) from None
        write_atomic(store.run_file, text)
        return cls(run_dir, workflow)

    @classmethod
    def start(
        cls,
        definition: str,
        params: Mapping[str, Any] | None = None,
        *,
        base: Path,
    ) -> Orchestrator:
        """Start a run in a directory the definition's `run_location` names.

        The run's directory is created with the first free number after the
        stem, so two runs started at once get different names. Raises
        ValueError when the definition names no location, or when the numbers
        up to 99 are all in use.
        """
        workflow = load_definition(definition)(params)
        location = workflow.run_location()
        if location is None:
            raise ValueError(
                f"{definition} does not say where its runs go; give the run directory"
            )
        parent, stem = location
        runs = Path(base) / parent
        runs.mkdir(parents=True, exist_ok=True)
        for number in range(1, 100):
            run_dir = runs / f"{stem}-{number:02d}"
            try:
                run_dir.mkdir()
            except FileExistsError:
                continue
            return cls.create(run_dir, definition, params)
        raise ValueError(f"every run name from {stem}-01 to {stem}-99 is in use")

    @classmethod
    def open(cls, run_dir: Path) -> Orchestrator:
        """The orchestrator of a started run. Raises ValueError when the
        directory is not a run."""
        run_dir = Path(run_dir).absolute()
        store = RunStore(run_dir)
        if not store.run_file.exists():
            raise ValueError(
                f"{run_dir} is not a run: it has no {store.relative(store.run_file)}"
            )
        record = store.read_json(store.run_file)
        if (
            set(record) != {"format", "definition", "params"}
            or not isinstance(record["definition"], str)
            or not isinstance(record["params"], dict)
        ):
            raise StateError(f"{store.run_file} does not have the expected fields")
        return cls(run_dir, load_definition(record["definition"])(record["params"]))

    def step(self) -> StepResult:
        """Run the definition from the top until no path can continue.

        A call of `step` consumes a round: it means every worker launched from
        the previous step has returned or failed to start. Attempts are
        counted per hand-out: each hand-out is one attempt, and its result is
        judged once. A job handed out before and still without an output
        counts as a failed attempt, so calling `step` again without worker
        activity uses up attempts and ends in a blocked outcome. A step that
        gives Uncertain counts nothing and moves nothing. Recovery in a fresh
        session therefore requires that the earlier session's workers have
        stopped.

        Repeating `step` gives the same outcome only where nothing is left to
        consume: on a finished run, on an uncertain effect, and on a run that
        may only be stopped.

        A step gives one outcome, the first of these that applies: Uncertain,
        Blocked, Launch, Done.

        Two kinds of record are written while the definition runs: an
        effect's start and completion, each at once and atomically, because
        the process can end inside the effect. Everything else the step
        records waits until the definition has finished running. The step
        then writes the prompt files of its hand-outs; replaces its other
        state records in one atomic rename; and after that moves
        files into `workflow-state/` as those records direct. The records
        name each file to be moved with its bytes' hash. A step that ends
        before the rename leaves those records as they were, and a prompt file it
        wrote is written again. A step that ends after the rename leaves
        moves undone; the next step first moves every such file that is
        still in place with the recorded hash and whose kept copy does not
        exist yet, then judges. A hand-out whose
        Launch was never returned counts as a failed attempt, as any
        hand-out without an output does.

        One step runs on a run at a time. The lock is taken before the
        definition runs. It is an operating-system lock on a file under
        `workflow-state/`, so it ends with the process that holds it, and a
        crashed step leaves nothing to clear. A `step` in another process
        while one is running raises RunBusy. A second `step` within the same
        process is not a supported use, and its behaviour is not specified.
        """
        store = self._store
        with store.locked():
            state = store.load_state()
            effects = store.load_effects()
            if not store.state_file.exists():
                store.save_state(state)
            if state["moves"]:
                store.move(state["moves"])
                state["moves"] = []
                store.save_state(state)
            stopped = state["workflow"]["stopped"]
            if stopped is not None:
                # The definition does not run, so no recognizer is at hand: a
                # started effect is uncertain, as one no longer reached is.
                block = self._stopped_block(RESERVED, stopped)
                for name, record in sorted(effects.items()):
                    if record["status"] == "started":
                        return Uncertain(
                            name,
                            "the effect started and its completion was not "
                            "recorded; the definition is stopped",
                            (block,),
                        )
                return Blocked((block,))
            step = _Step(self, store, state, effects)
            step.run()
            return step.finish()

    def resolve(self, effect: str, recognition: Recognition) -> None:
        """Record what the operator established about an effect.

        This is the operator's act; the agent orchestrator may only stop and
        report. It applies to an effect that is uncertain, to a completed
        effect whose inputs have changed, and to an effect the definition no
        longer reaches.

        COMPLETED records the effect as completed for the inputs as they are
        now, so the next step goes past it; for an effect no longer reached,
        it means the effect stands and is no longer required to be reached.
        ABSENT clears the record: the next step runs the effect if the
        definition reaches it, and otherwise owes nothing. Raises ValueError
        for UNKNOWN, and for an effect in none of these states.
        """
        if recognition is Recognition.UNKNOWN:
            raise ValueError(
                "an effect cannot be resolved as unknown; establish whether it "
                "took place (completed) or not (absent)"
            )
        store = self._store
        with store.locked():
            state = store.load_state()
            record = store.load_effects().get(effect)
            if record is None:
                raise ValueError(f"no effect named {effect} is recorded in this run")
            current = _files_state(self.run_dir, record["inputs"])
            unreached = effect in state["unreached"]
            if not (
                record["status"] == "started" or record["state"] != current or unreached
            ):
                raise ValueError(
                    f"effect {effect} is completed and matches its inputs; "
                    "there is nothing to resolve"
                )
            if recognition is Recognition.ABSENT:
                store.drop_effect(effect)
            else:
                record.update(
                    status="completed",
                    state=current,
                    required=record["required"] and not unreached,
                )
                store.save_effect(record)
            if unreached:
                state["unreached"].remove(effect)
                store.save_state(state)

    def release(self, subject: str) -> None:
        """Let a stopped job, or the stopped `workflow`, be tried again.

        This is the operator's act; the agent orchestrator may only stop and
        report. The next `step` judges the subject again. If it is still not
        accepted, it is handed out with the retry limit and the repair limit
        starting over. Accepted outputs of other jobs are untouched.

        Raises ValueError for a subject that is not stopped, and for an
        effect, whose state is recorded with `resolve`.
        """
        if subject.startswith("effect "):
            raise ValueError(
                f"{subject} is not released; the operator records its state "
                "with resolve"
            )
        store = self._store
        with store.locked():
            state = store.load_state()
            if subject == RESERVED:
                workflow = state["workflow"]
                if workflow["stopped"] is None:
                    raise ValueError(f"{RESERVED} is not stopped")
                workflow.update(stopped=None, places={})
            else:
                record = state["jobs"].get(subject)
                if record is None or record["stopped"] is None:
                    raise ValueError(f"job {subject} is not stopped")
                record.update(
                    stopped=None,
                    failures=0,
                    blocks_toward_limit=0,
                    outstanding=None,
                    history=[],
                )
            store.save_state(state)

    def report(self, event: str, job: str | None = None, text: str = "") -> Report:
        """Record one observation of the agent orchestrator.

        The run does not advance, and no report causes an acceptance. Raises
        ValueError for an event that is not in REPORT_EVENTS.
        """
        if event not in REPORT_EVENTS:
            raise ValueError(
                f"event {event!r} is not reported; the events are "
                f"{', '.join(REPORT_EVENTS)}"
            )
        report = Report(
            number=len(self._store.read_reports()) + 1,
            event=event,
            job=job,
            text=text,
            recorded_at=datetime.now(UTC).isoformat(timespec="seconds"),
        )
        self._store.append_report({"format": FORMAT, **report.__dict__})
        return report

    def reports(self) -> list[Report]:
        """Every report recorded for the run, oldest first."""
        return [
            Report(**{key: value for key, value in record.items() if key != "format"})
            for record in self._store.read_reports()
        ]

    def _stopped_block(self, subject: str, stopped: Mapping[str, str]) -> Block:
        return Block(
            subject=subject,
            reason=stopped["reason"],
            record_path=self.run_dir / stopped["record"],
            permitted=STOP,
            scope=self.workflow.repair_scope,
        )


# One step


def _resolve_path(run_dir: Path, declared: str) -> Path:
    path = Path(declared)
    return path if path.is_absolute() else run_dir / path


def _input_key(run_dir: Path, declared: str) -> str:
    """A declared path in one spelling, relative when it is inside the run
    directory, so that no absolute path of the run directory is recorded."""
    path = Path(declared)
    if path.is_absolute():
        try:
            return normalized(str(path.relative_to(run_dir)))
        except ValueError:
            pass
    return normalized(declared)


def _files_state(run_dir: Path, declared: Sequence[str]) -> str:
    """The hash of the declared files' bytes, keyed by their declared paths."""
    files = []
    for path in declared:
        resolved = _resolve_path(run_dir, path)
        if resolved.is_dir():
            raise DefinitionError(f"input {path} is a directory; declare its files")
        files.append([_input_key(run_dir, path), file_sha(resolved)])
    return sha(canonical(files))


@dataclass
class _Judgment:
    """What judging one job in this step found.

    `record` is the job's record after the judgment and without a hand-out;
    `handout_record` adds the hand-out.
    """

    job: Job
    kind: str  # accepted, handout, block or stopped
    record: dict[str, Any]
    input_state: str = ""
    reopened: bool = False
    reason: str = ""
    permitted: str = ""
    record_path: Path | None = None
    details: list[str] = field(default_factory=list)
    problem: str | None = None
    to_keep: list[Path] = field(default_factory=list)

    def handout_record(self) -> dict[str, Any]:
        record = copy.deepcopy(self.record)
        if self.reopened:
            record.update(accepted=None, failures=0, messages=[], history=[])
        record["handouts"] += 1
        record["outstanding"] = self.input_state
        record["last_input"] = self.input_state
        return record


class _Step:
    """One run of the definition, and what it leaves behind."""

    def __init__(
        self,
        orchestrator: Orchestrator,
        store: RunStore,
        state: dict[str, Any],
        effects: dict[str, dict[str, Any]],
    ) -> None:
        self.orchestrator = orchestrator
        self.workflow = orchestrator.workflow
        self.run_dir = orchestrator.run_dir
        self.store = store
        self.state = state
        self.effects = effects
        self.handles: dict[str, JobHandle] = {}
        self.judgments: dict[str, _Judgment] = {}
        self.owners: dict[str, str] = {}
        self.errors: list[Exception] = []
        self.definition_error: DefinitionError | None = None
        self.uncertain: list[tuple[str, str]] = []
        self.reached: set[str] = set()
        self.effect_blocks: dict[str, str] = {}
        self.unreached: list[str] = []
        self.ran_to_end = False

    # Running the definition

    def run(self) -> None:
        try:
            self.workflow.run(Context(self))
            self.ran_to_end = True
        except _PathEnded:
            pass
        except DefinitionError as error:
            self.definition_error = self.definition_error or error
        except Exception as error:  # noqa: BLE001 - becomes a block on `workflow`
            self.errors.append(error)
        if self.definition_error is not None:
            raise self.definition_error

    def refuse(self, message: str) -> None:
        """Raise a DefinitionError that a broad catch in the definition cannot
        hide: it is raised again when the definition returns."""
        error = DefinitionError(message)
        self.definition_error = self.definition_error or error
        raise error

    def agent(self, job: Job) -> JobHandle:
        existing = self.handles.get(job.name)
        if existing is not None:
            if not existing.job.same_task_as(job):
                self.refuse(f"job {job.name} is named for two different tasks")
            return existing
        for path in (job.owned_output, job.owned_problem):
            owner = self.owners.get(path)
            if owner is not None:
                self.refuse(f"path {path} is owned by job {owner} and job {job.name}")
        for path in (job.owned_output, job.owned_problem):
            self.owners[path] = job.name
        judgment = self.judge(job)
        self.check_reads(job, judgment)
        handle = JobHandle(
            job, job.output_path(self.run_dir), judgment.kind == "accepted"
        )
        self.handles[job.name] = handle
        self.judgments[job.name] = judgment
        return handle

    def effect(
        self,
        name: str,
        do: Callable[[], None],
        inputs: list[str],
        recognize: Callable[[], Recognition] | None,
    ) -> None:
        try:
            check_name(name, "effect")
        except DefinitionError as error:
            self.refuse(str(error))
        if name in self.reached:
            self.refuse(f"effect {name} is declared twice in one step")
        self.reached.add(name)
        current = _files_state(self.run_dir, inputs)
        record = self.effects.get(name)
        if record is not None and record["status"] == "started":
            recognition, detail = self.recognize(recognize)
            if recognition is Recognition.COMPLETED:
                record = {**record, "status": "completed"}
                self.save_effect(record)
            elif recognition is Recognition.ABSENT:
                record = None
            else:
                self.uncertain.append((name, detail))
                raise _PathEnded
        if record is None:
            record = {
                "format": FORMAT,
                "name": name,
                "status": "started",
                "inputs": inputs,
                "state": current,
                "required": True,
            }
            self.save_effect(record)
            try:
                do()
            except Exception as error:
                # Ending the path keeps a broad catch in the definition from
                # hiding the error.
                self.errors.append(error)
                raise _PathEnded from error
            record = {**record, "status": "completed"}
            self.save_effect(record)
            return
        if record["state"] != current:
            self.effect_blocks[name] = (
                "the effect is completed and its inputs have changed since"
            )

    def recognize(
        self, recognize: Callable[[], Recognition] | None
    ) -> tuple[Recognition, str]:
        started = "the effect started and its completion was not recorded"
        if recognize is None:
            return Recognition.UNKNOWN, f"{started}; the definition gives no recognizer"
        try:
            recognition = recognize()
        except Exception as error:  # noqa: BLE001 - an uncertain outcome, not a block
            return Recognition.UNKNOWN, f"{started}; the recognizer failed: {error}"
        if not isinstance(recognition, Recognition):
            return (
                Recognition.UNKNOWN,
                f"{started}; the recognizer gave {recognition!r}",
            )
        return recognition, (
            f"{started}; the recognizer could not establish whether it took place"
        )

    def save_effect(self, record: dict[str, Any]) -> None:
        self.store.save_effect(record)
        self.effects[record["name"]] = record

    # Judging a job

    def input_state(self, job: Job) -> str:
        return sha(
            canonical(
                {
                    "prompt": job.prompt,
                    "inputs": _files_state(self.run_dir, job.inputs),
                    "launch": job.launch_data(),
                }
            )
        )

    def refusals(self, job: Job, output: Path) -> list[str]:
        if job.validator is None:
            return []
        return [str(reason) for reason in job.validator(output)]

    def judge(self, job: Job) -> _Judgment:
        record = copy.deepcopy(self.state["jobs"].get(job.name) or new_job())
        if record["stopped"] is not None:
            return _Judgment(
                job,
                "stopped",
                record,
                reason=record["stopped"]["reason"],
                permitted=STOP,
                record_path=self.run_dir / record["stopped"]["record"],
            )
        current = self.input_state(job)
        output = job.output_path(self.run_dir)
        problem = job.problem_path(self.run_dir)

        if problem.exists():
            record["outstanding"] = None
            return self.block(
                job,
                record,
                "the worker wrote a problem report",
                problem=problem.read_text(encoding="utf-8", errors="replace"),
                to_keep=[path for path in (problem, output) if path.is_file()],
            )

        accepted = record["accepted"]
        if accepted is not None:
            if (
                file_sha(output) == accepted["output"]
                and current == accepted["input"]
                and not self.refusals(job, output)
            ):
                return _Judgment(job, "accepted", record)
            return _Judgment(job, "handout", record, current, reopened=True)

        if record["outstanding"] is not None:
            refusals: list[str] = []
            if not output.exists():
                failure = "no output"
            elif current != record["outstanding"]:
                failure = "an input changed after hand-out"
            else:
                refusals = self.refusals(job, output)
                if not refusals:
                    return self.accept(job, record, current, output)
                failure = "the output was refused by its validator"
            record["outstanding"] = None
            record["failures"] += 1
            record["messages"] = refusals or [failure]
            record["history"].append(
                f"attempt {record['handouts']}: {failure}"
                + "".join(f"\n  - {message}" for message in refusals)
            )
            if record["failures"] > self.workflow.retry_limit:
                return self.block(
                    job,
                    record,
                    f"{failure}, attempt {record['failures']} of "
                    f"{self.workflow.retry_limit + 1}",
                )
            return _Judgment(job, "handout", record, current)

        if (
            output.exists()
            and record["last_input"] == current
            and not self.refusals(job, output)
        ):
            return self.accept(job, record, current, output)
        return _Judgment(job, "handout", record, current)

    def accept(
        self, job: Job, record: dict[str, Any], current: str, output: Path
    ) -> _Judgment:
        record.update(
            accepted={"input": current, "output": file_sha(output)},
            failures=0,
            blocks_toward_limit=0,
            outstanding=None,
            last_input=current,
            messages=[],
            history=[],
        )
        return _Judgment(job, "accepted", record)

    def block(
        self,
        job: Job,
        record: dict[str, Any],
        reason: str,
        problem: str | None = None,
        to_keep: list[Path] | None = None,
    ) -> _Judgment:
        details = record["history"]
        record.update(failures=0, history=[])
        record["blocks_toward_limit"] += 1
        record["blocks"] += 1
        permitted = (
            REPAIR
            if record["blocks_toward_limit"] <= self.workflow.repair_limit
            else STOP
        )
        path = self.store.job_record_path(job.name, record["blocks"])
        if permitted == STOP:
            record["stopped"] = {"reason": reason, "record": self.store.relative(path)}
        return _Judgment(
            job,
            "block",
            record,
            reason=reason,
            permitted=permitted,
            record_path=path,
            details=details,
            problem=problem,
            to_keep=to_keep or [],
        )

    # After the definition

    def check_reads(self, job: Job, judgment: _Judgment) -> None:
        """Refuse a job that reads the output of a job named in this step and
        not accepted, whichever of the two is named second."""
        for declared in job.inputs:
            key = _input_key(self.run_dir, declared)
            for name, other in self.judgments.items():
                if other.job.owned_output == key and other.kind != "accepted":
                    self.refuse_read(job.name, declared, name)
        if judgment.kind == "accepted":
            return
        for name, other in self.judgments.items():
            for declared in other.job.inputs:
                if _input_key(self.run_dir, declared) == job.owned_output:
                    self.refuse_read(name, declared, job.name)

    def refuse_read(self, consumer: str, declared: str, producer: str) -> None:
        self.refuse(
            f"job {consumer} reads {declared}, the output of job {producer}, "
            f"which is not accepted; wait on {producer} before naming {consumer}"
        )

    def check_unreached(self) -> None:
        for name, record in sorted(self.effects.items()):
            if name in self.reached:
                continue
            if record["status"] == "started":
                self.uncertain.append(
                    (
                        name,
                        (
                            "the effect started, its completion was not recorded, "
                            "and the definition no longer reaches it"
                        ),
                    )
                )
            elif record["required"]:
                self.effect_blocks[name] = (
                    "the effect is completed and the definition no longer reaches it"
                )
                self.unreached.append(name)

    def place(self, error: BaseException) -> str:
        """Where in the definition's own files the error was raised."""
        files = set()
        for cls in type(self.workflow).__mro__:
            if cls in (Workflow, object):
                continue
            try:
                files.add(os.path.normcase(os.path.abspath(inspect.getfile(cls))))
            except TypeError:
                continue
        place = f"outside the definition: {type(error).__name__}"
        frame = error.__traceback__
        while frame is not None:
            filename = os.path.normcase(
                os.path.abspath(frame.tb_frame.f_code.co_filename)
            )
            if filename in files:
                place = f"{filename}:{frame.tb_lineno}"
            frame = frame.tb_next
        return place

    def finish(self) -> StepResult:
        if self.ran_to_end:
            self.check_unreached()
        state = copy.deepcopy(self.state)
        blocks: list[tuple[Block, str | _Judgment | None]] = []

        for name in sorted(self.judgments):
            judgment = self.judgments[name]
            if judgment.kind in ("block", "stopped"):
                text = None if judgment.kind == "stopped" else judgment
                blocks.append((self.as_block(name, judgment), text))

        workflow = state["workflow"]
        if self.errors:
            places = dict(workflow["places"])
            failing = {self.place(error) for error in self.errors}
            for place in failing:
                places[place] = places.get(place, 0) + 1
            workflow["places"] = places
            workflow["blocks"] += 1
            limit = self.workflow.repair_limit
            permitted = (
                STOP if any(places[place] > limit for place in failing) else REPAIR
            )
            path = self.store.workflow_record_path(workflow["blocks"])
            first = self.errors[0]
            reason = f"{type(first).__name__}: {first}".splitlines()[0]
            if permitted == STOP:
                workflow["stopped"] = {
                    "reason": reason,
                    "record": self.store.relative(path),
                }
            blocks.append(
                (
                    Block(
                        RESERVED, reason, path, permitted, self.workflow.repair_scope
                    ),
                    self.workflow_record(reason, permitted),
                )
            )
        else:
            workflow["places"] = {}

        for name in sorted(self.effect_blocks):
            reason = self.effect_blocks[name]
            path = self.store.effect_record_path(name)
            block = Block(
                f"effect {name}", reason, path, STOP, self.workflow.repair_scope
            )
            blocks.append((block, self.effect_record(name, reason)))

        found = tuple(block for block, _ in blocks)
        handouts = (
            []
            if found
            else [
                judgment
                for judgment in self.judgments.values()
                if judgment.kind == "handout"
            ]
        )
        handed_out = {judgment.job.name for judgment in handouts}
        to_keep: list[tuple[str, Path]] = []
        for name, judgment in self.judgments.items():
            if name in handed_out:
                state["jobs"][name] = judgment.handout_record()
                output = judgment.job.output_path(self.run_dir)
                problem = judgment.job.problem_path(self.run_dir)
                to_keep += [
                    (name, path) for path in (output, problem) if path.is_file()
                ]
            else:
                state["jobs"][name] = judgment.record
                to_keep += [(name, path) for path in judgment.to_keep]
        if self.ran_to_end:
            state["unreached"] = self.unreached

        moves = []
        targets: dict[Path, Path] = {}
        for name, path in to_keep:
            state["kept"] += 1
            target = self.store.kept_path(name, state["kept"], path)
            targets[path] = target
            moves.append(
                {
                    "source": self.store.relative(path),
                    "target": self.store.relative(target),
                    "sha": file_sha(path),
                }
            )

        for block, text in blocks:
            if isinstance(text, _Judgment):
                text = self.job_record(text, targets)
            if text is not None:
                write_atomic(block.record_path, text)

        if self.uncertain:
            effect, detail = self.uncertain[0]
            return Uncertain(effect, detail, found)

        launched = []
        for judgment in sorted(handouts, key=lambda judgment: judgment.job.name):
            job = judgment.job
            record = state["jobs"][job.name]
            prompt_path = self.store.prompt_path(job.name)
            write_atomic(prompt_path, self.prompt(job, record))
            launched.append(
                Handout(
                    name=job.name,
                    attempt=record["handouts"],
                    prompt_path=prompt_path,
                    output_path=job.output_path(self.run_dir),
                    problem_path=job.problem_path(self.run_dir),
                    launch=job.launch,
                )
            )

        state["moves"] = moves
        self.store.save_state(state)
        if moves:
            self.store.move(moves)
            state["moves"] = []
            self.store.save_state(state)

        if found:
            return Blocked(found)
        if launched:
            return Launch(tuple(launched))
        if self.ran_to_end:
            return Done()
        raise RuntimeError("the definition stopped with nothing to launch or report")

    # What a step writes for the agent orchestrator and the operator

    def prompt(self, job: Job, record: dict[str, Any]) -> str:
        lines = [job.prompt.rstrip(), ""]
        if job.inputs:
            lines += ["## Inputs", ""]
            lines += [
                f"- `{_resolve_path(self.run_dir, declared)}`"
                for declared in job.inputs
            ]
            lines.append("")
        lines += [
            "## Where to write",
            "",
            f"Write the result to `{job.output_path(self.run_dir)}`.",
            "",
            (
                "If you cannot finish the task, write why to "
                f"`{job.problem_path(self.run_dir)}` instead."
            ),
            "",
            (
                "Reply in one line that names the file you wrote. "
                "Do not repeat or summarize its content."
            ),
        ]
        if record["failures"] and record["messages"]:
            lines += ["", "## Why the previous attempt was refused", ""]
            lines += [f"- {message}" for message in record["messages"]]
        return "\n".join(lines) + "\n"

    def as_block(self, name: str, judgment: _Judgment) -> Block:
        assert judgment.record_path is not None
        return Block(
            subject=name,
            reason=judgment.reason,
            record_path=judgment.record_path,
            permitted=judgment.permitted,
            scope=self.workflow.repair_scope,
        )

    def reports_about(self, subject: str) -> list[str]:
        return [
            f"- report {report['number']}, {report['recorded_at']}, "
            f"{report['event']}{'' if report['job'] is None else ' on ' + report['job']}: "
            f"{report['text']}"
            for report in self.store.read_reports()
            if report["job"] in (None, subject)
        ]

    def header(self, subject: str, reason: str, permitted: str) -> list[str]:
        return [
            f"# Block on {subject}",
            "",
            f"- Reason: {reason}",
            f"- Permitted: {permitted}",
            f"- Repair scope: {self.workflow.repair_scope}",
        ]

    def job_record(self, judgment: _Judgment, targets: dict[Path, Path]) -> str:
        name = judgment.job.name
        lines = self.header(name, judgment.reason, judgment.permitted)
        lines += [f"- Hand-outs in the run: {judgment.record['handouts']}"]
        if judgment.details:
            lines += ["", "## Attempts", ""]
            lines += [f"- {detail}" for detail in judgment.details]
        if judgment.problem is not None:
            lines += ["", "## Problem report", "", judgment.problem.rstrip()]
        if judgment.to_keep:
            lines += ["", "## Kept", ""]
            lines += [
                f"- {self.store.relative(path)} is moved to "
                f"{self.store.relative(targets[path])}"
                for path in judgment.to_keep
            ]
        reports = self.reports_about(name)
        if reports:
            lines += ["", "## Reports", "", *reports]
        return "\n".join(lines) + "\n"

    def workflow_record(self, reason: str, permitted: str) -> str:
        lines = self.header(RESERVED, reason, permitted)
        for error in self.errors:
            lines += [
                "",
                f"## Error at {self.place(error)}",
                "",
                "```",
                "".join(traceback.format_exception(error)).rstrip(),
                "```",
            ]
        reports = self.reports_about(RESERVED)
        if reports:
            lines += ["", "## Reports", "", *reports]
        return "\n".join(lines) + "\n"

    def effect_record(self, name: str, reason: str) -> str:
        record = self.effects[name]
        lines = self.header(f"effect {name}", reason, STOP)
        lines += [
            f"- Inputs: {', '.join(record['inputs']) or 'none'}",
            "",
            (
                "The operator establishes what is outside and records it with "
                f"resolve {name} completed or resolve {name} absent."
            ),
        ]
        reports = self.reports_about(f"effect {name}")
        if reports:
            lines += ["", "## Reports", "", *reports]
        return "\n".join(lines) + "\n"
