"""A small workflow for trying the loop text with real sub-agents.

Two lenses read one source in parallel, and a reconciliation reads both. The
`scenario` parameter adds one behaviour for the agent orchestrator to meet:

clean
    Nothing goes wrong.
retry
    The reconciliation's validator asks for a closing line its prompt does not
    mention, so the first attempt is refused and the retry prompt carries the
    validator's message.
problem
    An extra job summarizes `notes.md`, which setup leaves misplaced at
    `incoming/notes.md`. The worker should write a problem report; moving or
    copying the file is a repair within the default scope.
stop
    The second lens's validator cannot be satisfied, so the job blocks, and no
    repair within the scope helps. The agent orchestrator should stop.
stop-only
    As `stop`, with a repair limit of zero, so the first block permits only
    stopping.
parameters
    The first lens carries the launch parameters given to setup with
    `--launch`; the second lens carries none.
uncertain
    After the reconciliation, an effect publishes two files beside the run.
    The first time, the process ends between the two files. The next step
    finds the effect in part and gives the uncertain outcome.
busy
    The first step that finds the hold file beside the run removes it and
    holds the run for `hold` seconds, so that a second step meets a busy run.
    Setup starts that step itself, so no other step can find the file first.

The files beside the run are named after the run directory: `<run>.published/`,
`<run>.interrupt`, `<run>.hold` and `<run>.hold.log`. Setup creates the last
three.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from commonplace.workflow import Job, Recognition, Workflow

PUBLISHED = ("reconciled.md", "index.md")


def has_heading_and_body(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    if not lines or not lines[0].startswith("# "):
        return ["the output must start with a level-one heading"]
    if len(lines) < 3:
        return ["the output must have a body below its heading"]
    return []


def ends_checked(path: Path) -> list[str]:
    refusals = has_heading_and_body(path)
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    if not lines or lines[-1] != "Checked: yes":
        refusals.append("the output must end with the line `Checked: yes`")
    return refusals


def impossible(path: Path) -> list[str]:
    return ["the output must be empty and must also start with a level-one heading"]


def beside(run_dir: Path, suffix: str) -> Path:
    return run_dir.parent / f"{run_dir.name}.{suffix}"


class Trial(Workflow):
    def __init__(self, params=None):
        super().__init__(params)
        if self.params.get("scenario") == "stop-only":
            self.repair_limit = 0

    def lens(
        self, name: str, question: str, validator=has_heading_and_body, launch=None
    ) -> Job:
        return Job(
            name=name,
            prompt=(
                f"Read the source text listed under Inputs. {question} "
                "Write Markdown: a level-one heading, then a bulleted list."
            ),
            output=f"{name}.md",
            inputs=("source.md",),
            validator=validator,
            launch=launch or {},
        )

    def hold(self, run_dir: Path) -> None:
        marker = beside(run_dir, "hold")
        if marker.is_file():
            marker.unlink()
            time.sleep(float(self.params.get("hold", 90)))

    def publish(self, run_dir: Path) -> None:
        target = beside(run_dir, "published")
        target.mkdir(exist_ok=True)
        result = (run_dir / "reconciled.md").read_text(encoding="utf-8")
        (target / "reconciled.md").write_text(result, encoding="utf-8")
        marker = beside(run_dir, "interrupt")
        if marker.is_file():
            marker.unlink()
            print("the process ended while publishing", file=sys.stderr, flush=True)
            os._exit(9)
        (target / "index.md").write_text("- reconciled.md\n", encoding="utf-8")

    def published(self, run_dir: Path) -> Recognition:
        target = beside(run_dir, "published")
        present = [(target / name).is_file() for name in PUBLISHED]
        if all(present):
            return Recognition.COMPLETED
        if not any(present):
            return Recognition.ABSENT
        return Recognition.UNKNOWN

    def run(self, ctx):
        scenario = self.params.get("scenario", "clean")
        if scenario == "busy":
            self.hold(ctx.run_dir)
        stops = scenario in ("stop", "stop-only")
        launch = json.loads(self.params.get("launch", "{}"))
        claims = ctx.agent(
            self.lens("claims", "List the claims the text makes.", launch=launch)
        )
        assumptions = ctx.agent(
            self.lens(
                "assumptions",
                "List the assumptions the text relies on without stating them.",
                impossible if stops else has_heading_and_body,
            )
        )
        ctx.wait(claims, assumptions)

        reads = ["claims.md", "assumptions.md"]
        if scenario == "problem":
            ctx.agent(
                Job(
                    name="notes",
                    prompt=(
                        "Summarize the notes file listed under Inputs in three "
                        "bullets under a level-one heading. Do not invent content: "
                        "if the file cannot be read, report the problem instead."
                    ),
                    output="notes-summary.md",
                    inputs=("notes.md",),
                    validator=has_heading_and_body,
                )
            ).wait()
            reads.append("notes-summary.md")

        ctx.agent(
            Job(
                name="reconcile",
                prompt=(
                    "Read the files listed under Inputs. Write one Markdown note with "
                    "a level-one heading that pairs each claim with the assumptions "
                    "it depends on."
                ),
                output="reconciled.md",
                inputs=tuple(reads),
                validator=ends_checked if scenario == "retry" else has_heading_and_body,
            )
        ).wait()

        if scenario == "uncertain":
            ctx.effect(
                "publish",
                lambda: self.publish(ctx.run_dir),
                inputs=("reconciled.md",),
                recognize=lambda: self.published(ctx.run_dir),
            )
