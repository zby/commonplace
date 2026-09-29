"""Small workflow definitions and a scripted agent orchestrator for tests.

Nothing here uses a model. `ScriptedAgent` plays the agent orchestrator: it
runs `step`, and for each job handed out it runs a scripted worker that writes
files the way a sub-agent would.
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping
from functools import partial
from pathlib import Path

import pytest

from commonplace.workflow import (
    Handout,
    Job,
    Launch,
    Orchestrator,
    StepResult,
    Workflow,
)

on_request = pytest.mark.skipif(
    not os.environ.get("COMMONPLACE_WORKFLOW_TESTS"),
    reason="the code orchestrator is not implemented; set COMMONPLACE_WORKFLOW_TESTS=1 to run",
)

Worker = Callable[[Handout], None]


def has_heading(path: Path) -> list[str]:
    if path.read_text(encoding="utf-8").startswith("# "):
        return []
    return ["output must start with a level-one heading"]


def write_valid(handout: Handout) -> None:
    handout.output_path.write_text(f"# {handout.name}\n", encoding="utf-8")


def write_invalid(handout: Handout) -> None:
    handout.output_path.write_text("no heading\n", encoding="utf-8")


def write_nothing(handout: Handout) -> None:
    """A worker that never ran, or ran and wrote no file."""


def write_problem(text: str) -> Worker:
    def worker(handout: Handout) -> None:
        handout.problem_path.write_text(text, encoding="utf-8")

    return worker


def lens_job(name: str) -> Job:
    return Job(
        name=name,
        prompt=f"Apply {name} to the source.",
        output=f"{name}.md",
        inputs=("source.md",),
        validator=has_heading,
    )


class OneJob(Workflow):
    def run(self, ctx):
        ctx.agent(lens_job("only")).wait()


class TwoLenses(Workflow):
    """Two independent lenses, then a reconciliation that reads both."""

    order = ("lens-a", "lens-b")

    def lens(self, ctx, name):
        return ctx.agent(lens_job(name)).wait()

    def run(self, ctx):
        ctx.parallel(*(partial(self.lens, ctx, name) for name in self.order))
        ctx.agent(
            Job(
                name="reconcile",
                prompt="Reconcile the two lenses.",
                output="reconciled.md",
                inputs=("lens-a.md", "lens-b.md"),
                validator=has_heading,
            )
        ).wait()


class TwoLensesReversed(TwoLenses):
    order = ("lens-b", "lens-a")


class UnequalPaths(Workflow):
    """One path has two stages, the other has one."""

    def long_path(self, ctx):
        ctx.agent(lens_job("long-first")).wait()
        ctx.agent(
            Job(
                name="long-second",
                prompt="Check the first stage.",
                output="long-second.md",
                inputs=("long-first.md",),
                validator=has_heading,
            )
        ).wait()

    def short_path(self, ctx):
        ctx.agent(lens_job("short")).wait()

    def run(self, ctx):
        ctx.parallel(partial(self.long_path, ctx), partial(self.short_path, ctx))


class NamedBeforeWaited(Workflow):
    """Names two jobs, then waits on them one after the other."""

    def run(self, ctx):
        first = ctx.agent(lens_job("first"))
        second = ctx.agent(lens_job("second"))
        first.wait()
        second.wait()


class ScriptedAgent:
    """Plays the agent orchestrator with scripted workers and no model."""

    def __init__(
        self,
        orchestrator: Orchestrator,
        workers: Mapping[str, Worker] | None = None,
        default: Worker = write_valid,
    ) -> None:
        self.orchestrator = orchestrator
        self.workers = dict(workers or {})
        self.default = default
        self.launched: list[str] = []

    def round(self) -> StepResult:
        result = self.orchestrator.step()
        if isinstance(result, Launch):
            for handout in result.jobs:
                self.launched.append(handout.name)
                self.workers.get(handout.name, self.default)(handout)
        return result

    def run(self, max_rounds: int = 20) -> list[StepResult]:
        results = []
        for _ in range(max_rounds):
            result = self.round()
            results.append(result)
            if not isinstance(result, Launch):
                return results
        raise AssertionError(f"run did not finish in {max_rounds} rounds")


def new_run(tmp_path: Path, source: str = "source text\n") -> Path:
    run_dir = tmp_path / "run"
    run_dir.mkdir(parents=True)
    (run_dir / "source.md").write_text(source, encoding="utf-8")
    return run_dir
