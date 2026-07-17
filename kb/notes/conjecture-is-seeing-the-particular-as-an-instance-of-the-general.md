---
description: "A conjecture posits a general concept while recognizing particulars as instances; the co-arising tightens with abstraction depth, from shared feature to generative model."
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, discovery]
---

# Conjecture is seeing the particular as an instance of the general

Conjecture — the phase of the [discovery lifecycle](./definitions/discovery-lifecycle.md) where a claim not entailed by the evidence gets posited — has a dual structure, whether in mathematics, science, or a knowledge base:

1. You **posit something general** that didn't previously exist as a named concept
2. You **recognize** that things you already knew are *instances* of it

How tightly the two halves bind depends on depth. At the shallow end, the instances are legible as a group before anyone posits the rule — repeated failures already look similar; the conjecture names what they share. At the deep end the two halves cannot be separated: the general doesn't exist until you see the particular as an instance of it, and the particular wasn't legible as an instance until you posited the general. They co-arise. A mathematician extracting a shared lemma from two theorems, Darwin seeing four unremarkable observations as axioms of a single theorem — the creative act is the same: recognizing that things from different contexts are instances of a structure that nobody had named yet.

## Three depths of abstraction

Similarity-based connections vary not by *kind* (topical vs mechanistic) but by *depth*. This hierarchy draws on [Alexander's levels of concreteness](./alexander-patterns-and-knowledge-system-design.md) — from structural templates through generative processes to mutual reinforcement:

| Depth | Operation | Power |
|-------|-----------|-------|
| **Shared feature** | Name a surface similarity | Descriptive — organizes but doesn't explain |
| **Shared structure** | Extract a common pattern | Structural — reveals form but not cause |
| **Generative model** | Propose an abstract machine that produces both phenomena | Explanatory — explains why the similarity exists and predicts new instances |

Each level subsumes the previous. But they're increasingly powerful, increasingly hard to reach, and increasingly epistemically risky — a generative model can be compellingly wrong (phlogiston, caloric theory) precisely because it explains so much. This table is the conjecture's internal grading, and it aligns with the [discovery lifecycle](./definitions/discovery-lifecycle.md)'s polation axis: shared structure extends along dimensions the cases already have (extrapolation), while a generative model posits a new dimension (hyperpolation). The dual structure above tightens along the same axis — full co-arising is the deep end's signature.

(This hierarchy covers similarity-based connections. Knowledge systems also need contrastive links (contradicts, supersedes), causal links (caused, enabled), and temporal links (preceded) — those aren't similarity at any depth.)

## Recognition is the hard problem

The hard problem in knowledge systems is not *linking* (once you see a connection, articulating it is straightforward) but *recognition* — seeing that two things share structure at some level of abstraction.

Recognition cost scales with depth:
- **Surface similarity:** cheap. Embeddings, keywords, filenames get you there.
- **Structural similarity:** expensive. Requires understanding what a note is really about, then comparing across notes.
- **Generative similarity:** very expensive. Requires *inventing the dimension along which the comparison becomes visible*.

The mathematical tradition offers a partial solution: **develop vocabulary for naming structures**. Once a structure has a name, recognizing new instances becomes cheap. The naming amortizes the cost of the conjecture that produced it. In a knowledge system, this means the highest-value act isn't linking two notes that share a mechanism — it's **creating a new note that names the mechanism**.

## Worked examples

**Mathematical lemma extraction** is the clean case. A mathematician notices that two apparently unrelated proofs make the same move and extracts that common structure as a lemma. The lemma becomes a new graph node; both theorems can now link to it, and later theorems can recognize the same structure cheaply. Category theory pushes the same move further: it makes deep structural similarity nameable across domains that looked unrelated at the surface.

**Darwin's theory of natural selection** shows the generative-model depth. Variation, overproduction, heritability, and environmental pressure were separately familiar observations. Darwin's conjecture was seeing them as premises of one abstract machine: any population with those properties adapts over time. The empirical work identified the right axioms; the creative act was positing the general model that made multiple particulars instances of the same process — the decades of subsequent evidence-gathering were the lifecycle's test phase.

**Fleming's penicillin discovery** shows the conjecture handing off to the rest of the lifecycle. A mold-contaminated plate with a bacterial inhibition zone suggested a shared-feature conjecture: this substance kills bacteria. The broader antimicrobial general did not arrive in that act; it stabilized through the later phases — extraction, purification, clinical development — that turned the conjecture into an accepted discovery. The particular opens a direction; the general is earned by the phases that follow.

**Luhmann-style linking** clarifies the KB implication. The important distinction is not topical versus mechanistic linking. Topic and mechanism are both similarity judgments at different abstraction depths. Luhmann's stronger move was judgment-based linking instead of category filing: this note connects to that note for this articulated reason. That reason may be topical, structural, analogical, contrastive, or causal; the value comes from recognizing and naming the connection rather than filing both notes under a preexisting bucket.

---

Relevant Notes:

- [alexander-patterns-and-knowledge-system-design](./alexander-patterns-and-knowledge-system-design.md) — source: the three depths draw on Alexander's levels of concreteness (structural templates → generative processes → centers strengthening centers)
- [arscontexta](../agent-memory-systems/reviews/arscontexta.md) — refines: the "controlled disorder" claim is right about judgment-based linking but the topic-vs-mechanism framing is a false dichotomy
- [Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — extends: the adjacency-vs-connection distinction maps to recognition depth, not link kind
- [constraining](./definitions/constraining.md) — suggestive parallel: constraining and conjecture depth are both gradients where each step trades generality for power, though on different axes
- [discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: the lifecycle whose conjecture phase this note describes; the three depths grade that phase along the lifecycle's polation axis
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: the recognition cost hierarchy maps to computational bounds on structure extraction
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — grounds: MVV reframes "naming amortizes discovery cost" as an optimization problem

Derived into:

- [/connect skill](../instructions/cp-skill-connect/SKILL.md) — the "name the mechanism" insight is operationalized as abstraction opportunity logging in Phase 5 reflection
