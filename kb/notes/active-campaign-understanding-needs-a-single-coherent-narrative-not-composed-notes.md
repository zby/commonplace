---
description: Why durable-knowledge graph composition (many linked notes) is wrong for tracking understanding during active engineering — a single holistically rewritten narrative maintains the coherence that working memory requires
type: note
traits: [has-external-sources]
areas: [claw-design]
status: seedling
---

# Active-campaign understanding needs a single coherent narrative, not composed notes

The claw's note graph works well for durable knowledge: many composable notes, each making a single claim, linked into a traversable structure. But for tracking understanding during an active engineering campaign — the evolving mental model of what the problem is, what's been tried, and what the current strategy is — graph composition is the wrong structure. What's needed is a single narrative document that gets holistically rewritten as understanding evolves.

The distinction maps to different coherence requirements:

| Dimension | Durable knowledge (notes) | Working understanding (theory) |
|---|---|---|
| Coherence unit | Individual note | Entire narrative |
| Success criteria | Findable by future agent who doesn't know it exists | Legible to collaborator joining the campaign now |
| Update pattern | Add new note, refine existing, connect | Rewrite the whole document |
| History | Explicit (pivots noted in prose, links to predecessors) | Implicit (git history; document always reads as present state) |
| Composability | Essential — each note must work in multiple contexts | Irrelevant — there's one document per campaign |
| Lifecycle | Accumulates value (more links, more references) | Consumed (value transfers to code, decisions, notes) |

The key insight is that **coherence at the campaign level requires holistic rewrite, not composition**. When you add a new note to a graph, coherence is local — each note is internally consistent and its links are semantically labeled. But no single document tells you "here is what we currently believe about this problem." An index comes closest, but indexes are curated collections with context phrases, not narratives. They organize knowledge; they don't narrate understanding.

## Evidence: theorist

The [theorist](https://github.com/blader/theorist) skill (MIT, blader, 2026) implements exactly this pattern. It maintains a single `THEORY.MD` at the repo root — a 1-3 page narrative covering problem thesis, operating theory, strategy, key discoveries, and open questions. Its design choices are instructive:

- **Rewrite, don't append** — the document is rewritten holistically, never appended to. Old theories are noted as pivots ("initially X, but Y revealed Z"), but the document always reads as a coherent present-tense narrative. This is neither logging (append-only) nor note evolution (seedling→evergreen on individual notes). It's a third pattern: a document that maintains coherence through complete rewrite.
- **Update when theory changes, not when code changes** — the trigger is epistemological (understanding shifted) not operational (code was committed). This is a useful general principle: knowledge artifacts should track understanding, not activity.
- **Always-on activation** — no invocation required. The skill stays active throughout a session and updates frequently during active work loops (investigate → implement → verify). This matches the workshop layer's need for low-friction maintenance.
- **200-line maximum** — forces concision. A reader should grasp the full strategic picture in under 5 minutes. This is the opposite of the note graph's strategy of distributing depth across many linked documents.

## Relationship to the workshop layer

This is a concrete exemplar of the [workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) the claw identified as missing. THEORY.MD has all the predicted workshop properties: lifecycle (lives and dies with a campaign), consumed value (transfers into decisions and notes), state changes (rewritten as understanding evolves), and temporal sensitivity (coherence matters now, not for archival).

It fills the "session logs" slot from the workshop note, but with a crucial difference: session logs are append-only records of what happened. A theory document is a rewritten narrative of what is currently understood. The rewrite discipline is what makes it useful — it forces the author to reconcile new evidence with existing understanding rather than just stacking observations.

## The bridge question

The open question is what happens when a campaign ends. Theorist doesn't address this. The workshop note predicted the need for extraction bridges (workshop → library) — a `/crystallize` operation that distills durable insights from temporal documents into notes. For THEORY.MD specifically:

- Key discoveries → notes in the KB
- Strategy pivots → material for ADRs or structured claims
- Open questions → seeds for future investigation

Without this bridge, THEORY.MD's insights die with the campaign. The git history preserves the text but not the knowledge — no one will search git log for design insights.

## Open questions

- Can the rewrite discipline work for agents, or does it require human judgment about what's still true? Theorist is designed for LLM agents, but holistic rewrite is hard — it requires understanding what changed and what didn't.
- Is one theory doc per repo the right granularity? Multiple concurrent workstreams get brief mentions rather than full treatment. A claw might need theory docs per area or per task.
- How does the 200-line maximum interact with complex, multi-front campaigns? The constraint forces triage — what's important enough to include — which is valuable but may lose important context.

---

Relevant Notes:
- [a-functioning-claw-needs-a-workshop-layer-not-just-a-library](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — theorist exemplifies the workshop layer this note predicts; THEORY.MD has all the workshop properties (lifecycle, consumed value, temporal sensitivity)
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — holistic rewrite is the opposite of append-only stabilization; THEORY.MD is deliberately *un*stable, rewritten to maintain coherence rather than frozen to preserve a decision
- [agent-statelessness-means-harness-should-inject-context-automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — theorist's always-on activation is automatic context injection; the theory doc is the harness injecting strategic context every session

Topics:
- [claw-design](./claw-design.md)
