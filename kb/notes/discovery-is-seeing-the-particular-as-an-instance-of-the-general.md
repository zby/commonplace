---
description: Proposes that discovery has a dual structure — positing a new general concept while recognizing existing particulars as instances of it — and that similarity-based connections vary by abstraction depth (shared feature → shared structure → generative model), not link kind. Scoped to similarity connections; contrastive and causal links are a different axis.
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Discovery is seeing the particular as an instance of the general

Discovery — whether in mathematics, science, or a knowledge base — has a dual structure that can't be decomposed:

1. You **posit something general** that didn't previously exist as a named concept
2. You **simultaneously recognize** that things you already knew are *instances* of it

The general doesn't exist until you see the particular as an instance of it. And the particular wasn't legible as an instance until you posited the general. They co-arise. A mathematician extracting a shared lemma from two theorems, Darwin seeing four unremarkable observations as axioms of a single theorem — the creative act is the same: recognizing that things from different contexts are instances of a structure that nobody had named yet.

## Three depths of abstraction

Similarity-based connections vary not by *kind* (topical vs mechanistic) but by *depth*. This hierarchy draws on [Alexander's levels of concreteness](./alexander-patterns-and-knowledge-system-design.md) — from structural templates through generative processes to mutual reinforcement:

| Depth | Operation | Power |
|-------|-----------|-------|
| **Shared feature** | Name a surface similarity | Descriptive — organizes but doesn't explain |
| **Shared structure** | Extract a common pattern | Structural — reveals form but not cause |
| **Generative model** | Propose an abstract machine that produces both phenomena | Explanatory — explains why the similarity exists and predicts new instances |

Each level subsumes the previous. But they're increasingly powerful, increasingly hard to discover, and increasingly epistemically risky — a generative model can be compellingly wrong (phlogiston, caloric theory) precisely because it explains so much.

(This hierarchy covers similarity-based connections. Knowledge systems also need contrastive links (contradicts, supersedes), causal links (caused, enabled), and temporal links (preceded) — those aren't similarity at any depth.)

## Recognition is the hard problem

The hard problem in knowledge systems is not *linking* (once you see a connection, articulating it is straightforward) but *recognition* — seeing that two things share structure at some level of abstraction.

Recognition cost scales with depth:
- **Surface similarity:** cheap. Embeddings, keywords, filenames get you there.
- **Structural similarity:** expensive. Requires understanding what a note is really about, then comparing across notes.
- **Generative similarity:** very expensive. Requires *inventing the dimension along which the comparison becomes visible*.

The mathematical tradition offers a partial solution: **develop vocabulary for naming structures**. Once a structure has a name, recognizing new instances becomes cheap. The naming amortizes the discovery cost. In a knowledge system, this means the highest-value act isn't linking two notes that share a mechanism — it's **creating a new note that names the mechanism**.

Extended examples (Darwin, Fleming, lemma extraction) and unprocessed observations are in [discovery examples](../work/discovery-examples.md).

---

Relevant Notes:

- [alexander-patterns-and-knowledge-system-design](./alexander-patterns-and-knowledge-system-design.md) — source: the three depths draw on Alexander's levels of concreteness (structural templates → generative processes → centers strengthening centers)
- [arscontexta](./related-systems/arscontexta.md) — refines: the "controlled disorder" claim is right about judgment-based linking but the topic-vs-mechanism framing is a false dichotomy
- [Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md) — extends: the adjacency-vs-connection distinction maps to recognition depth, not link kind
- [constraining](./constraining.md) — suggestive parallel: constraining and discovery are both gradients where each step trades generality for power, though on different axes
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: the recognition cost hierarchy maps to computational bounds on structure extraction
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — grounds: MVV reframes "naming amortizes discovery cost" as an optimization problem

Distilled into:

- [/connect skill](../instructions/connect/SKILL.md) — the "name the mechanism" insight is operationalized as abstraction opportunity logging in Phase 5 reflection
