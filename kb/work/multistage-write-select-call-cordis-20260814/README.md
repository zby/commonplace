# Select/call and Cordis integration workshop

This workshop tests how Cordis and its use in DeepSeek Harness change the scope, state model, and downstream use of the select/call decomposition lemma. It is an edit-mode `cp-skill-write-multistage` run. The library target remains untouched until a reconciled candidate passes audit and acceptance review.

## Run identity

- Immutable run key: `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md`
- Current intended target: `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md`
- Mode: edit
- Collection: `kb/notes/`
- Type: `kb/types/note.md`
- Acceptance review: required — the note is a load-bearing formal claim used to transfer results across the computational-model cluster

## Governing question

Under what exact conditions does the select/call decomposition remain valid when the harness is dynamically composed, executes non-LLM effects, or lets an LLM produce control decisions? The revision should preserve the mechanical lemma where it holds while preventing readers from treating an LLM-call trace normal form as complete operational semantics for an effectful harness.

## Inputs

Local evidence and theory:

- [`original.md`](./original.md) — byte-for-content copy of the incumbent at workshop initialization
- [`brief.md`](./brief.md) — fixed commission, scope, and evidence boundary
- [`../../sources/a-programming-paradigm-for-spatiotemporal-composability.md`](../../sources/a-programming-paradigm-for-spatiotemporal-composability.md) — Cordis paper snapshot
- [`../../sources/a-programming-paradigm-for-spatiotemporal-composability.ingest.md`](../../sources/a-programming-paradigm-for-spatiotemporal-composability.ingest.md) — source analysis and fixed-decomposition limit
- [`../../notes/bounded-context-orchestration-model.md`](../../notes/bounded-context-orchestration-model.md) — base model the lemma supports
- [`../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md`](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — architectural-quality claim currently conflated with the mechanical lemma
- [`../../notes/the-practical-scheduler-is-the-host-language.md`](../../notes/the-practical-scheduler-is-the-host-language.md) — host-program interpretation of `select` and `K`
- [`../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — limit on what plugin-level mutability establishes about the fixed meta-machine

Pinned primary implementation sources (DeepSeek Harness revision [`47f943859bef60e4160492346772ded9b24f765a`](https://github.com/deepseek-ai/deepseek-harness/commit/47f943859bef60e4160492346772ded9b24f765a), observed 2026-08-14):

- <https://github.com/deepseek-ai/deepseek-harness/tree/47f943859bef60e4160492346772ded9b24f765a>
- <https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/architecture.md>
- <https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/subsystems/core.md>
- <https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/agent-lifecycle.md>
- <https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/tool-execution-pipeline.md>
- <https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/capability-seams.md>

DeepSeek Harness is a developer preview. The pin fixes the workshop's implementation evidence; claims about later revisions require fresh inspection.

## Workflow state

- [x] Incumbent preserved in `original.md`
- [x] `brief.md`
- [ ] `reconstruction.md`
- [ ] `claim-skeleton.md`
- [ ] `draft.md`
- [ ] `audit.md`
- [ ] `candidate.md`
- [ ] `acceptance.md` — required
- [ ] Promotion and deterministic validation

## Unresolved decisions and blockers

- No current blocker to source reconstruction.
- The current run owns one target only. A general effectful `select/dispatch` normal-form note is a possible synthesis outcome, not an authorized second target in this run.
- Whether dynamic composition state belongs inside `K` or should be named separately as a configuration `Γ` is an open theoretical choice. Reconstruction and the claim skeleton must compare both formulations before drafting.
- DeepSeek Harness evidence is revision-scoped to `47f943859bef60e4160492346772ded9b24f765a`. The Cordis paper must independently warrant any general mechanism claim.

## What closes this workshop

The workshop closes when it produces and promotes a validated revision that:

1. states whether the lemma is a complete execution normal form or only an LLM-call trace normal form;
2. gives exact treatment to external effects, dynamic code/configuration, and LLM-produced control decisions;
3. preserves downstream theorem transfer only under explicit preconditions;
4. uses Cordis as a mechanism-level challenge or witness without generalizing from DeepSeek Harness adoption or preview status;
5. resolves every audit finding and passes a fresh acceptance review.

Because the user requested a workshop, retain this directory and its active-workshop entry until promotion is separately requested or completed.
