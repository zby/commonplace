---
description: "Argues deploy-time learning and agile share the same core innovation — co-evolving prose and code — but deploy-time learning extends it by treating some prose as permanently load-bearing"
type: note
traits: []
areas: [learning-theory]
status: seedling
---

# Deploy-time learning is agile for human-AI systems

Waterfall's core assumption was sequential handoff: finish all the specs, then write all the code. The specs are input, the code is output, they don't mix. Agile's real innovation was not "shorter cycles" or "embracing change" — it was deciding that code and specs can coexist and co-evolve. Running code informs and revises specs; revised specs drive new code. The two media feed each other continuously.

Deploy-time learning follows the same pattern with a different pair of media: deterministic code and LLM prompts co-evolving. You deploy with some behavior in prompts, observe what works, and progressively crystallise the understood parts into code — while the prompts evolve in response to what the code now handles. The process shape is identical to an agile sprint.

## The same learning loop

Both agile and deploy-time learning implement the same cycle:

1. **Start underspecified** — you don't know enough to crystallise yet
2. **Deploy** — run the system to observe what actually happens
3. **Learn** — identify which parts are now understood well enough to harden
4. **Crystallise** — move understood parts from the flexible medium (natural language / prompts) into the rigid medium (code / tests)
5. **Repeat** — the remaining underspecified parts continue to evolve

At any given moment during an agile project, you have a mix: some things are already code, some are stories and specs still in natural language, and the crystallisation boundary moves each iteration. A deploy-time learning system looks the same: some behavior is deterministic code, some is still in prompts, and the boundary moves as understanding accumulates.

## Where they diverge

The difference is in where the boundary stops moving.

Agile treats natural-language specs as temporary — stories waiting to become code. The implied end state is fully crystallised software. Deploy-time learning recognises that some parts *should stay in prose* because they require judgment, interpretation, or context-sensitivity that deterministic code can't capture. The data report example makes this concrete: statistics move to Python, but narrative interpretation stays with the LLM. There's no expectation to crystallise that last part.

This is a more mature position on the specification problem. Agile implicitly assumes everything can be crystallised if you iterate enough. Deploy-time learning says: identify the boundary between what can be hardened and what should remain flexible, then maintain both permanently. The system is a durable hybrid.

## The waterfall backdrop

Both innovations are responses to the same underlying problem: natural language lacks the precise semantics needed for unambiguous specification. Waterfall tried to solve this by demanding complete specs upfront. Formal methods tried to solve it by abandoning natural language for mathematics. Agile and deploy-time learning solve it by accepting the imprecision and building a process that learns its way to the right interpretation incrementally — through deployment, not through specification.

Moreover, what agile calls "changing requirements" [partly conflates genuine change with late-surfacing disambiguation failures](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — downstream specs silently commit to one interpretation of an underspecified upstream spec, and the error only surfaces when deployed. Short iterations limit how far wrong interpretations can propagate, not just how fast teams respond to genuine change.

The progression: waterfall (separate the media, specs first) → agile (co-evolve the media, code wins eventually) → deploy-time learning (co-evolve the media, both persist).

## Open Questions

- Are there specific agile practices (retrospectives, story splitting, velocity tracking) that have direct analogues in deploy-time learning workflows?
- In agile, uncrystallised specs are backlog — work not yet done. In deploy-time learning, uncrystallised prompts might be the finished design. Does this change how teams decide what to prioritise for crystallisation?
