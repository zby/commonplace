---
description: "Explains why an input stream alone can't answer 'what to store' in open-domain memory design; a declared output spec supplies the missing inclusion criterion."
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [agent-memory, context-engineering]
---

# Open-domain memory retention needs a declared output spec

A memory system facing an open-ended input stream — conversations, observations, sessions — must decide which items are worth retaining. That decision needs a criterion: something to measure a candidate observation against. Two places can supply it.

| | Input-driven | Output-driven |
|---|---|---|
| Criterion source | Properties of the incoming item (novelty, frequency, salience) | A declared account of what the system must serve |
| Default operation | Observe, filter, retain | Declare need, elicit, fill |
| Strength | Cheap; runs in the background without upkeep | Explicit coverage; gaps are checkable against the spec |
| Failure mode | Accumulates whatever happens to come up; gaps are invisible because nothing defines what should be there | Breaks when the spec drifts or goes stale |

In a narrow domain, input-driven heuristics can work because the input itself encodes what matters — a bug report already carries severity and category signals that make a keep/drop decision answerable from the item alone. In an open domain — general conversation, general project knowledge — no such signal exists. Every observation is a plausible candidate for retention, so a purely input-driven filter has nothing to filter against: it either keeps everything at a low bar or substitutes an unstated, un-auditable judgment call for the missing criterion.

An output spec resolves this by declaring, ahead of any specific observation, what the system must be able to serve: purpose, domain boundaries, what's excluded, a quality bar. Retention then becomes: does this item serve the declared use? That converts an unanswerable question ("is this worth keeping?") into an answerable one ("does this serve the stated purpose?").

## Where this shows up in practice

This KB's own Goals section (`CLAUDE.md`: purpose, scope, quality bar) is an output spec in this sense — it is what makes "does this observation deserve a note?" answerable before any note is drafted. `cp-skill-write` starts from a declared type and topic — a need to fill — rather than a transcript to mine, which is the same output-driven move applied to the authoring workflow itself. `COLLECTION.md` files extend the same spec to the register level (theoretical, descriptive, prescriptive), so each collection carries its own local admission criterion.

Claude Code's own conversational auto-memory system, by contrast, is input-driven: it watches sessions and applies retention heuristics with no declared spec to check coverage against. The tradeoff described above is visible in practice — coverage of any given memory category is whatever happened to come up in conversation, and a missing category produces no signal that anything is missing.

## Scope

This is not an argument against input-driven capture. The two are complementary: a system can run cheap input-driven capture in the background and use output-driven audits — periodic checks of the declared spec against what has and hasn't been captured — to catch invisible gaps and drive targeted elicitation. The claim here is narrower: in an open domain, an inclusion criterion has to come from *somewhere*, and only a declared output spec supplies one that can be audited rather than merely inferred after the fact.

## Open Questions

- How should the output spec itself be kept current? If the declared purpose drifts and nobody revisits it, the inclusion criterion drifts silently along with it.
- Where does input-driven capture still belong inside an otherwise output-driven KB — log entries, or first-occurrence observations not yet understood as mechanisms?

---

Relevant Notes:

- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — contrasts: ingress work makes captured material usable after admission; this note addresses the admission criterion that has to be settled before ingress applies
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — extends: applies the effects-first design principle at the granularity of a single retention decision, rather than overall system architecture
- [Context engineering](./definitions/context-engineering.md) — defined-in: knowledge lifecycle (what enters storage in the first place) is one of the architectural determinants named there
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) — extends: supplies the output-driven capture-policy option that note's axis table omits — its listed choices (heuristic trigger, LLM curator, post-session mining) are all input-driven
- [Elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) — enables: its seed/enforce/log-misses/distill/prune loop is the maintenance machinery this note's open question about keeping the output spec current still needs
- [What the matrix shows across 148 agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidence: the automatic-capture-and-push camp versus the curated-pull-only camp found across 148 reviewed systems corroborates the input-driven/output-driven split at aggregate scale
