---
description: The three-space memory claim is testable because flat memory predicts specific cross-contamination failures
areas: [learning-theory]
status: speculative
---

# Three-space memory separation predicts measurable failure modes

The "living memory" article (Cornelius, Agentic Note-Taking #19) claims that agent memory should be split into three spaces — knowledge (semantic), self (episodic), and operational (procedural) — because conflating them produces specific failure modes. This claim is worth validating because the alternative — a single flat memory — is simpler and cheaper to build.

## The predicted failure modes

The article lists three categories of cross-contamination when memory is flat:

1. **Operational debris pollutes search.** Session observations, processing notes, and transient friction reports appear alongside durable knowledge when the agent searches for a concept. Signal-to-noise degrades as operational volume grows.

2. **Identity scatters across ephemeral logs.** Self-knowledge (what patterns work, how to calibrate confidence) ends up embedded in session transcripts rather than consolidated in a persistent location. Each session re-derives operational wisdom from scratch.

3. **Insights trapped in session state.** Genuine discoveries made during processing never graduate to the knowledge graph because there is no explicit boundary between "working memory" and "permanent memory." The insight lives and dies in the session that produced it.

These are concrete enough to observe. We don't need to build a flat-memory alternative — we already run a system with partial three-space separation (`docs/notes/`, `arscontexta/self/`, `arscontexta/ops/`). The validation is observational: watch for evidence of the failure modes during normal use and record what we find.

## Observation protocol

During regular sessions, watch for and log instances of:

**Failure mode 1 — search pollution:**
- When searching for a concept, do operational/transient notes appear in results alongside durable knowledge?
- Does the agent waste time reading irrelevant operational artifacts to answer a knowledge question?
- Does this get worse as note count grows?

**Failure mode 2 — identity scatter:**
- Does the agent re-derive operational wisdom that it already learned in a prior session?
- Is self-knowledge (what works, what doesn't) findable when needed, or buried in session logs?
- When the agent starts a new session, does it have access to its accumulated operational patterns?

**Failure mode 3 — insight trapping:**
- Do genuine insights emerge during session work (extraction, connection-finding) that never get written to the knowledge graph?
- At session end, is there material worth preserving that would be lost without explicit graduation?
- What fraction of session-generated observations actually become durable notes?

Each observation gets a short log entry: date, which failure mode, what happened, severity (noise / mild friction / blocked work).

## What counts as evidence

**For the claim (separation helps):** Failure modes are rare or absent in the spaces that are well-separated, but appear where separation is weakest. For example, if `docs/notes/` stays clean but `arscontexta/ops/` content leaks into knowledge searches, that's evidence the boundary matters.

**Against the claim (separation is decorative):** Failure modes don't manifest at our current scale, or they manifest equally regardless of separation. If 30 notes in a flat directory are just as navigable as 30 notes in three directories, the overhead isn't justified yet.

**The boring explanation:** If the only benefit is that `grep` scoped to `docs/notes/` doesn't hit operational files, the value is real but trivial — it's file hygiene, not cognitive architecture. The Tulving mapping adds no explanatory power beyond "keep your folders tidy."

## Open questions

- At what scale do the failure modes become noticeable? We may need 50+ notes before search pollution is measurable.
- Does the current system's separation actually match the article's three-space model, or is it an accidental approximation?
- Is "different metabolic rates" (knowledge grows steadily, operations churn, self evolves slowly) observable in our commit history?

---

Relevant Notes:
- [deploy-time-learning](../notes/deploy-time-learning-the-missing-middle.md) — the verifiability gradient that motivates durable knowledge in the first place
- [storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md) — graduation from operational space to knowledge graph is a form of stabilization
- [claw-learning-is-broader-than-retrieval](./claw-learning-is-broader-than-retrieval.md) — argues these failure modes are symptoms of forcing action-oriented knowledge (preferences, procedures, precedents) into a retrieval-oriented structure

Topics:
- [learning-theory](./learning-theory.md)
