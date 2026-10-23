---
description: "Goedecke argues coding agents invent unrequested requirements such as mutexes, re-checks and consistency guards; stated tolerances and review that scans for added coordination are his repairs"
source: https://www.seangoedecke.com/what-requirements-dont-you-have/
captured: "2026-10-19"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 418ec6aaec2fe66cc0a637912faaf23302e60df0c72e93f7cfa0a0e5eeb50599
ingested: "2026-10-19"
type: types/ingest-report.md
domains: [agentic-coding, specification, maintainability, llm-reliability]
---

# Ingest: What requirements don't you have?

## Classification

This is a short argued position, not a report of one project: it states a design principle, illustrates it with well-known systems, and supports its agent section with the author's own review experience. The agent-related evidence is practitioner observation without counts, samples or worked diffs.
Author: Sean Goedecke is a working software engineer who writes regularly about engineering practice and AI-assisted coding. His signal is first-hand review of AI-generated changes. He is not reporting a study.

## Summary

Goedecke argues that elegant system designs come from deliberately dropping requirements: Unicorn drops shared mutable state and slow-client handling, S3 drops atomic multi-key updates, StatsD drops delivery guarantees, edge caches drop freshness, SQLite drops concurrent writes, and Cursor's git backend accepts high tail latency. Deciding which requirements to drop needs both technical and business judgment, and distrust between engineers and product managers often blocks that joint decision. The part relevant to this KB is the third move. Coding agents are trained to satisfy a grader (RLVR) and lack business context, so they treat hypothetical unsatisfied requirements as bugs and add mutexes, mid-flight re-checks, TOCTOU-style guards and consistency handling the task did not ask for. Goedecke reports that about half of the large AI-generated changes he reviews contain such an invented requirement. His repairs are to state tolerances in the prompt (stale or briefly inconsistent data is acceptable) and to review diffs specifically for unrequested coordination. He warns that unchecked invented requirements accumulate and "petrify" a codebase.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source's role in this KB is a practitioner illustration of agent output that over-satisfies an underspecified task, with two named repairs. It does not corroborate any statistical or general claim; every agent-related statement is anecdote.

Its strongest landing is [Weakly discriminated qualities tend to be underselected](../theory/weakly-discriminated-qualities-tend-to-be-underselected.md) (is-evidence-for). That note asks for an adverse directional mechanism before claiming absolute decline. Goedecke proposes one: grader-shaped generators add coordination and re-checks that tests do not penalise, because the code stays correct, and the additions accumulate. His review base rate is unquantified, so the source qualifies and illustrates the note rather than testing it.

For specification, [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) (is-evidence-for) gains a case where the author-only knowledge is a tolerance: acceptable staleness is a business acceptance condition that the executor cannot read from code. [LLM output deviation requires three-way diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md) (is-evidence-for) explains why the two repairs do not substitute for each other: a silent spec admits both the mutex and the no-mutex design, the stated tolerance narrows that admissible set before generation, and review filters the produced output afterwards. [Brainstorming: maintainability oracles for agentic development](../theory/brainstorming-maintainability-oracles-for-agentic-development.md) (is-evidence-for) gains a cheap candidate signal: requirements present in the diff but absent from the task, such as added locks, indirection layers or re-checks.

Among sources, [Ingest: Why LLMs can't make your code simpler](./why-llms-cant-make-your-code-simpler.ingest.md) compares-with this one on the source of LLM-added complexity. Alvarez Vecino attributes it to missing design context and proposes ADRs; Goedecke adds a training-induced disposition and proposes stated tolerances and review. In both, simplicity is bought by dropping a product requirement. [Ingest: Simplification](./simplification-2090443748077416467.ingest.md) compares-with it on who decides what is unnecessary in agent code: both keep that verdict with the human, but Briggs concerns agent-led removal and Goedecke concerns agent-added scope.

## Extractable Value

1. **Stated non-requirements as a specification move** -- Existing specification notes frame author fixes as added constraints. Goedecke's "I don't mind the data being stale" widens the acceptable set explicitly so the agent does not narrow it on its own. Together with the Alvarez Vecino case, this suggests that explicit tolerances are a constraint type, not an absence of constraint. The evidence is two practitioner anecdotes, so record it in `kb/log.md` until a mechanism or test exists. [quick-win]
2. **A named directional mechanism for maintainability decline** -- RLVR-shaped requirement invention plus accumulation is a candidate for the adverse mechanism that the weakly-discriminated-qualities note says absolute decline needs. It bounds that note's scope discussion without corroborating it. The RLVR attribution is the author's conjecture. [quick-win]
3. **A cheap review oracle: scope present in the diff but absent from the task** -- Scanning for added mutexes, indirection and mid-flight re-checks is a concrete, low-cost check for the maintainability-oracles brainstorm. Goedecke's "about half" hit rate is an uncalibrated starting hypothesis that an agent-run diff audit could test. [experiment]
4. **Two repairs act at different points** -- A prompt tolerance acts before generation, and review acts after it. This gives the three-way diagnosis note a concrete practitioner example of remedies that address different relations. [just-a-reference]
5. **Design-elegance examples** -- The Unicorn, S3, StatsD, SQLite and edge-cache cases illustrate requirement relaxation in general system design. That is outside this KB's scope except as background. [just-a-reference]

## Limitations (our opinion)

The agent claims rest on one engineer's review experience. "About half the time", "invariably" and "in every single system I've worked on" are unquantified, unsampled and self-reported; no diff, task or model is named. The causal story, that RLVR training produces grader-obsessed over-satisfaction, is a plausible framing but is not tested. A simpler account fits the same observations: an underspecified prompt admits many designs, and any interpreter without business context will choose some extra guards. Distinguishing a training-induced bias from ordinary underspecification would need comparison against human engineers or differently trained models given the same tasks. The source does not show that the added checks were harmful in the reviewed cases rather than merely unnecessary, and the "petrify" claim is a forecast with no longitudinal evidence. Survivorship also applies: Goedecke reports the requirements he caught, not those he missed or those that turned out to be needed. The essay's argument that elegance comes from dropped requirements is persuasive in its chosen examples, but selected successes do not show how often relaxing a requirement goes wrong.

## Recommended Next Action

Add a `kb/log.md` entry recording the candidate claim that explicit tolerances (stated non-requirements) are a distinct specification move against agent over-satisfaction, citing this ingest and the Alvarez Vecino ingest as its two anecdotal cases, and leave note promotion until a mechanism or test exists.
