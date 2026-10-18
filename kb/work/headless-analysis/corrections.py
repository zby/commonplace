"""A correction: the producer of a refused output answers the refusal.

The engine's protocol (`src/commonplace/artifactrun/checks.py`, ADRs 098-117),
kept unchanged by the port: the producer is asked again with the input
`refusal` (a body with `## Findings`, `## Blockers` and any further sections,
with or without frontmatter) and `previous-<name>` for each output of its
previous attempt. Besides its outputs it writes `answers`: one
`- corrected: <reason>` or `- declined: <reason>` line per blocker, in blocker
order. An entry that says corrected while the primary output's bytes equal the
previous version's is refused. A refusal without a Blockers section, such as
operator findings, counts as one blocker.

When a correction attempt is itself rejected by the checks, the next attempt
answers a structural refusal: the rejected attempt's findings, with the
blockers and other sections of the refusal it answered carried forward, since
only the latest refusal is in force. Its previous outputs are the rejected
attempt's, so repeating that attempt's bytes as "corrected" is refused too.

`correction_findings` and `refusal_findings` are the engine's own functions;
they already take plain values. Phase 2 of the port moves them out of the
engine package. Until then this module needs the `commonplace` package on the
path, as the worktree's venv provides.
"""

from __future__ import annotations

from jobs import Answer, Run, digest

from commonplace.artifactrun.checks import correction_findings, refusal_findings

ANSWERS = "answers"


def correct(run: Run, job: str, build_prompt, check, outputs: list[str], *, member: str,
            refusal: str, previous: dict[str, str], attempts: int, optional: list[str] = ()) -> Answer:
    """Ask the producer to answer `refusal` over its `previous` outputs, checking the answers.

    `outputs[0]` is the primary output. `answers` is asked for as an optional
    output so that a missing answers file is a content finding the next
    attempt sees, not an incomplete result. `check(answer)` is the job's own
    content check; the correction findings follow its findings, as in the
    engine. Attempt counting is `Run.checked`'s.
    """
    primary = outputs[0]
    optional = list(optional) + ([ANSWERS] if ANSWERS not in outputs and ANSWERS not in optional else [])
    state = {"refusal": refusal, "previous": dict(previous)}

    def inputs(problems: list, last: Answer | None) -> dict[str, str]:
        if last is not None:
            state["previous"] = dict(last.outputs)
            state["refusal"] = refusal_findings(problems[-1], member=member, answered=state["refusal"].encode())
        return {"refusal": state["refusal"],
                **{f"previous-{name}": text for name, text in state["previous"].items()}}

    def checked(answer: Answer) -> list[str]:
        previous_primary = state["previous"].get(primary)
        answers = answer.outputs.get(ANSWERS)
        findings = correction_findings(
            answer.outputs[primary].encode(), member=member, refusal=state["refusal"].encode(),
            answers=None if answers is None else answers.encode(),
            previous_version=None if previous_primary is None else digest(previous_primary))
        return check(answer) + ["[correction] " + finding for finding in findings]

    return run.checked(job, build_prompt, checked, outputs, optional, attempts, inputs)
