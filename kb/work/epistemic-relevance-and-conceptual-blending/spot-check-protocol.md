# Spot-check protocol (draft)

**Status:** first draft, 2026-11-01. Expect revisions after each run. Nothing here is a gate, a scheduler, or a library instruction.

## Why

The [watch](./README.md) is event-driven and has produced no independently arising episode. A spot check is the operator-triggered way to exercise the [checklist](./watch-checklist.md) on existing artifacts between episodes. It answers two questions: can a fresh worker apply the checklist and reach a defensible disposition, and does the KB hold unsupported integrations the watch has not seen. Results are artifact-level cases (Q00N in the [log](./observations.md)); they do not count toward the three-episode review point.

## Run

1. **Sample.** Search the library for relation phrases, for example `same mechanism`, `one mechanism`, `is a form of`, `is a special case of`, `is an instance of`, `reduces to`. The first search over theory, sources and reference returned about 67 files. Pick three to five passages, including at least one that looks warranted. Record what was picked and why; do not pick only suspicious ones.
2. **Hand off.** One fresh worker per passage, read-only. Give it the artifact, the passage, and the checklist as the only criterion. Ask for four things in order: the asserted relation in one sentence; its warrant as stated in the artifact or its sources; one counterexample or consequence checked; a disposition from `warranted`, `unsupported`, `unresolved`, `presentation-only`. Do not pass Q001, the findings, or the hypothesis.
3. **Judge.** The parent reads each report against its own reading of the passage. Agreement is a data point; disagreement is the more useful one, since it separates a checklist that is unclear from a worker that is wrong. Note which.
4. **Record.** One Q00N entry per passage, including the checked non-errors. Repairs happen only under operator authorization and outside the workshop, as with Q001.
5. **Optional probe.** For one passage, give a second worker the same source material under two requests, "what do these have in common" and "how do these differ", with everything else fixed. This tests the requested-answer-form account in the [findings](./findings.md).

## What the first runs should tell us

- How many search hits are real relation claims versus ordinary wording. If most are noise, the phrase list changes.
- Whether the checklist is usable as a criterion by a worker with no context. If workers return vague dispositions, the checklist needs a shorter criterion before any gate is drafted from it.
- Whether the parent and worker agree. Repeated disagreement on the same step says where the checklist is underspecified.

## Open choices

- The phrase list and whether to search by phrase at all; links with `derived-from` or `extends` relations are another sampling frame.
- How to choose the warranted controls without biasing toward easy ones.
- Whether the worker should see the artifact's sources or only the artifact.
- Cost: three to five workers per run. Whether that is cheap enough to run monthly, or only when an episode is suspected.
