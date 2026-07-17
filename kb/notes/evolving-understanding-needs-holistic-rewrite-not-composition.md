---
description: When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-reconciled narrative, rewritten holistically on change, keeps the whole picture within feasible bounds
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, context-engineering, distillation]
---

# Evolving understanding needs holistic rewrite, not composition

A note graph distributes knowledge across composable fragments — each note makes one claim, links provide traversal. This works for durable knowledge: the consumer picks what to load, coherence is local to each note.

When understanding is evolving and a consumer needs the whole picture — current beliefs, tried approaches, ongoing strategy — fragment reconciliation may not be feasible. Loading many notes, identifying which are current, and assembling a coherent view competes for [context budget](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). The cost falls on two dimensions: volume (loading N fragments) and complexity (discriminating current from stale, resolving tensions). As fragment count grows, reconciliation can exceed effective context — making the operation infeasible, not merely expensive.

A pre-reconciled narrative sidesteps this. The author — human or agent — performs reconciliation once and produces a single document sized for effective context: accumulated understanding is the source, the consumer needing the current picture is the target, and the narrative is the use-shaped artifact. When understanding changes, you rewrite holistically rather than let fragments diverge until reconciliation breaks — the narrative is a dependent artifact of the understanding it summarizes, stale until reworked when that understanding moves ([theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) states the maintenance regime).

## Why composition is expensive here

At least three properties of evolving understanding push fragment-based reconciliation toward the effective context boundary:

1. **The whole picture must be loaded at once** — before addressing their actual task, a consumer must load many notes, infer currency, and reconstruct connections. Each fragment competes for the same context budget as the task itself.

2. **Discrimination complexity grows with change rate** — when new evidence contradicts earlier understanding, notes get added or revised individually. The consumer must then discriminate current from stale across the whole set. The faster understanding evolves, the harder this becomes: a note may be mostly current but wrong on one point corrected by a later note — a signal easy to miss.

3. **Coherence requires simultaneous loading** — each note can be internally coherent while the set is collectively inconsistent. Resolving this requires holding all relevant notes in context at once and reconciling tensions between them. This is where the feasibility constraint bites hardest: reconciliation demands context proportional to the number and interdependence of fragments.

## The general pattern

The pattern applies when:
- Knowledge is accumulating from ongoing work, not static
- A consumer needs the whole picture to act, not just a slice
- Value is consumed (informs current action) rather than accumulated (builds a long-term graph)

Examples: onboarding documents tracking a changing system, investigation summaries during incident response, evolving design rationales during architecture exploration, theory documents during engineering campaigns.

The lifecycle is workshop, not library — the narrative lives and dies with the period of active evolution. When understanding stabilizes, insights should be [extracted into durable notes](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md), a second reshaping into a different form for a different consumer.

## Evidence: theorist

The [theorist](https://github.com/blader/theorist) skill (MIT, blader, 2026) implements this pattern as `THEORY.MD`: a single narrative, holistically rewritten rather than appended, capped at 200 lines to enforce concision. It updates when understanding shifts, not when code changes. When earlier understanding is superseded, the document records the shift ("initially X, but Y revealed Z") rather than preserving the old version — it always reads as a present-tense narrative.

Theorist is illustrative rather than confirmatory: it demonstrates the pattern's mechanics but offers no controlled evidence that holistic rewriting outperforms composition. The strongest signal is indirect — teams using theory docs report easier mid-project onboarding, because there is one document to read instead of a trail of notes and chat history. Whether this holds at scale or for agent consumers remains open.

## Open questions

- Can agents perform holistic rewrite reliably, or does it require human judgment about what's still true?
- What's the right extraction bridge when the evolution period ends? The narrative's insights need to become durable notes, but extraction is itself a reshaping step that could lose context.
- How does a size constraint interact with scope? Forced concision is the use-shaping doing its work — but complex situations may resist compression into a single document.
- When does the rewrite cost exceed the reconciliation cost it prevents? If fragments are few and stable, a consumer can reconcile within effective context. The threshold depends on fragment count, change rate, and interdependence.

---

Relevant Notes:

- [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the narrative is a dependent fast-path artifact over accumulated understanding; holistic rewrite is its stale-until-reworked maintenance
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: the bounded context that makes fragment reconciliation infeasible past a threshold
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: reconciliation complexity reduces effective context, so the feasibility boundary depends on the task, not just fragment count
- [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — the narrative's lifecycle is workshop, not library; extraction into durable notes is a second reshaping step
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — tension: composition maximizes combinatorial discovery but reconciliation can exceed effective context when the consumer needs a coherent whole
- [Storing LLM outputs is constraining](./storing-llm-outputs-is-constraining.md) — contrast: storing constrains by freezing; holistic rewriting is the opposite, rewriting to maintain coherence
- [Augment bidirectional spec](https://x.com/augmentcode/status/2025993446633492725) — extends: distributes the holistic-rewrite burden between human review and agent-generated updates
