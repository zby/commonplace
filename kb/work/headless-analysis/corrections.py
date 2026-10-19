"""A producer's attempts at one output: the first, and corrections of refusals.

The engine's protocol (`src/commonplace/artifactrun/checks.py` and
`engine.py`, ADRs 098-117), kept unchanged by the port: a producer whose
output was refused is asked again with the input `refusal` (a body with
`## Findings`, `## Blockers` and any further sections, with or without
frontmatter) and `previous-<name>` for each output of its previous attempt.
A producer with an `answers` output writes one `- corrected: <reason>` or
`- declined: <reason>` line per blocker, in blocker order; an entry that says
corrected while the primary output's bytes equal the previous version's is
refused; a refusal without a Blockers section, such as operator findings,
counts as one blocker. A producer without an `answers` output repairs in its
primary output alone. Either way, an answer that leaves the refused version
unchanged and writes no new auxiliary output is refused.

When an attempt is rejected by the checks, the next attempt answers a
structural refusal: the rejected attempt's findings, with the blockers and
other sections of the refusal it answered (if any) carried forward, since only
the latest refusal is in force. Its previous outputs are the rejected
attempt's, so repeating that attempt's bytes is refused too. So one call
covers a first attempt without a refusal (`refusal=None`) and its check-driven
retries, as well as a correction of a verifier's refusal. As the engine did,
a rerun of a job hands `previous-<name>` whether or not a refusal is in force.

`correction_findings` and `refusal_findings` are the engine's own functions;
they already take plain values. Phase 6 of the port moves them out of the
engine package. Until then this module needs the `commonplace` package on the
path, as the worktree's venv provides.
"""

from __future__ import annotations

from jobs import Answer, Run, digest

from commonplace.artifactrun.checks import correction_findings, refusal_findings

ANSWERS = "answers"


def produce(run: Run, job: str, build_prompt, check, outputs: list[str], *, member: str,
            attempts: int, refusal: str | None = None, previous: dict[str, str] | None = None,
            inputs: dict[str, str] | None = None) -> Answer:
    """Ask the producer for its outputs, answering `refusal` over `previous` when given.

    `outputs[0]` is the primary output, the only one the worker must write;
    the others, `answers` among them, are optional, so a missing answers
    file is a content finding the next attempt sees, not an incomplete
    result. `build_prompt(given)` returns the prompt for an attempt handed
    the inputs `given`: the job's own `inputs`, `previous-<name>` for each
    of the previous attempt's outputs when there was one, and `refusal` when
    one is in force. `check(answer)` is the job's own content check; the
    correction findings follow its findings, as in the engine. Attempt
    counting is `Run.checked`'s.
    """
    primary, auxiliary = outputs[0], list(outputs[1:])
    state = {"refusal": refusal, "previous": dict(previous or {}), "given": {}}

    def prompt(problems: list) -> str:
        return build_prompt(dict(state["given"]))

    def given(problems: list, last: Answer | None) -> dict[str, str]:
        if last is not None:
            state["previous"] = dict(last.outputs)
            answered = None if state["refusal"] is None else state["refusal"].encode()
            state["refusal"] = refusal_findings(problems[-1], member=member, answered=answered)
        handed = {f"previous-{name}": text for name, text in state["previous"].items()}
        if state["refusal"] is not None:
            handed["refusal"] = state["refusal"]
        state["given"] = {**(inputs or {}), **handed}
        return dict(state["given"])

    def checked(answer: Answer) -> list[str]:
        findings = check(answer)
        if state["refusal"] is None:
            return findings
        before = state["previous"]
        corrections: list[str] = []
        if ANSWERS in auxiliary:
            answers = answer.outputs.get(ANSWERS)
            corrections += correction_findings(
                answer.outputs[primary].encode(), member=member, refusal=state["refusal"].encode(),
                answers=None if answers is None else answers.encode(),
                previous_version=None if before.get(primary) is None else digest(before[primary]))
        # An answer can reconcile a refusal without changing the subject, but only with a new auxiliary output.
        changed_auxiliary = any(name in answer.outputs and answer.outputs[name] != before.get(name)
                                for name in auxiliary)
        if answer.outputs[primary] == before.get(primary) and not changed_auxiliary:
            corrections.append("answered a refusal with the refused version unchanged and no new auxiliary output")
        return findings + ["[correction] " + finding for finding in corrections]

    return run.checked(job, prompt, checked, [primary], auxiliary, attempts, given)
