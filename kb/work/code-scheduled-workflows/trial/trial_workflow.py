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
    `incoming/notes.md`. The worker should write a problem report; moving the
    file is a repair within the default scope.
stop
    The second lens's validator cannot be satisfied, so the job blocks, and no
    repair within the scope helps. The agent orchestrator should stop.
"""

from __future__ import annotations

from pathlib import Path

from commonplace.workflow import Job, Workflow


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


class Trial(Workflow):
    def lens(self, name: str, question: str, validator=has_heading_and_body) -> Job:
        return Job(
            name=name,
            prompt=(
                f"Read the source text listed under Inputs. {question} "
                "Write Markdown: a level-one heading, then a bulleted list."
            ),
            output=f"{name}.md",
            inputs=("source.md",),
            validator=validator,
        )

    def run(self, ctx):
        scenario = self.params.get("scenario", "clean")
        lens_b_validator = impossible if scenario == "stop" else has_heading_and_body
        claims = ctx.agent(self.lens("claims", "List the claims the text makes."))
        assumptions = ctx.agent(
            self.lens(
                "assumptions",
                "List the assumptions the text relies on without stating them.",
                lens_b_validator,
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
