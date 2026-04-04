# Instructions: Review auto-harness for Trace-Derived Learning

## Goal

Evaluate the existing related-system review of auto-harness against [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md) and determine whether auto-harness belongs in the survey.

This is not a new review. [auto-harness](../../notes/related-systems/auto-harness.md) already has a related-system note, and the repo is already cloned locally. The task is to assess its trace-derived learning placement and, if warranted, add it to the survey note.

## Targets

- Repo: `https://github.com/neosigmaai/auto-harness`
- Local clone: `related-systems/auto-harness`
- Existing review: `kb/notes/related-systems/auto-harness.md`

## Why this candidate matters

auto-harness is a useful boundary case. It clearly learns from benchmark failures over repeated runs, but its learned artifacts may be too thin to count as a full trace-derived learning system: `suite.json` stores promoted task IDs, `results.tsv` stores score history, and `learnings.md` is freeform advisory memory. If it belongs in the survey, it likely sharpens the lower bound of trajectory-run artifact learning rather than adding a richer extraction schema.

## Inputs

Read all of:

1. [auto-harness review](../../notes/related-systems/auto-harness.md)
2. The auto-harness repository (already cloned at `related-systems/auto-harness/`)
3. [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md)
4. [Autocontext](../../notes/related-systems/autocontext.md) — closest reviewed trajectory-run artifact/weight bridge
5. [HyperAgents](../../notes/related-systems/hyperagents.md) — closest reviewed benchmark-gated self-improvement harness
6. [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md)

## Questions to answer

1. What is the actual source trace in auto-harness: benchmark task outcomes, train-task replay sets, freeform learnings text, or all three?
2. What extracted artifacts does the harness create from those traces: promoted task IDs, score logs, prompt/code edits, or something richer?
3. Is `suite.json` promotion enough to count as trace-derived artifact learning, or is it better read as a regression-selection mechanism around code mutation?
4. On axis 1 of the survey (ingestion pattern), is auto-harness a trajectory-run system like Autocontext and Reflexion, or does it fall below the survey threshold because it lacks a real mining pipeline?
5. On axis 2 (promotion target), is it symbolic artifact learning, executable-code search guided by traces, or neither?
6. Compared to Autocontext and HyperAgents, is the important difference extraction depth, promotion target, oracle strength, or just architectural thinness?
7. Should auto-harness be added to the survey as a core example, a boundary case, or not at all?

## Output spec

- Update the existing auto-harness review note to include a `Trace-derived learning placement` section
- In that section, state auto-harness's position on both survey axes and whether it should be added to the survey note
- If auto-harness should be added, write its five-stage entry (`Trigger`, `Source format`, `Extraction`, `Promotion`, `Scope`) for the survey note
- Run semantic review on the updated review note
- Run `/validate` on the updated review note

Prioritize implementation-backed claims over the repo's self-improvement framing. Do not count benchmark-gated code mutation as trace-derived learning unless you can point to a durable mined artifact or a clear survey-useful boundary case.
