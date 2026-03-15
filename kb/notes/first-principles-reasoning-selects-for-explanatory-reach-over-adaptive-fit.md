---
description: Deutsch's adaptive-vs-explanatory distinction — explanatory knowledge has "reach" (transfers to new contexts) because it captures why, not just what works; grounds the KB's first-principles filter as selecting for reach over fit
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# First-principles reasoning selects for explanatory reach over adaptive fit

David Deutsch distinguishes two kinds of knowledge that mainstream usage conflates:

**Adaptive information** — structures that help a system cope with the world. A genome encodes successful adaptations. A neural network's weights encode useful patterns. An animal's instincts encode strategies that work. These are useful, but they don't explain *why* they work, can't be deliberately varied, and don't transfer beyond their training distribution.

**Explanatory knowledge** — says *why* the world works a certain way, can be deliberately varied and criticized, and supports transfer to new contexts because it captures deeper structure rather than successful habit. A gene "knows" how to build an eye but contains no theory of optics. Newton's optics is explanatory — it reaches contexts no eye ever encountered.

The distinguishing property is **reach**: explanatory knowledge applies beyond its original context because the explanation captures structure that isn't context-dependent.

## Why this matters for the KB

The KB's [first-principles methodology](./design-methodology-borrow-widely-filter-by-first-principles.md) is, in Deutsch's terms, a filter that selects for explanatory reach over adaptive fit. When a note derives a design pattern from constraints (finite context, no scoping mechanism, text-in/text-out), the derivation is explanatory — it says *why* the pattern works, which means it predicts where the pattern will fail (change the constraint, change the conclusion). When a note records "X works in practice," that's adaptive — useful but brittle to context change.

The [computational-model](./computational-model-index.md) area exemplifies reach. Programming-language concepts (scoping, partial evaluation, scheduling) were developed for compilers, but they *reach* into KB design because they capture structure that isn't programming-specific — they describe what happens when bounded processors compose text under constraints. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) doesn't just analogize to dynamic scoping — it identifies the same mechanism producing the same pathologies, and predicts the same remedies (lexically scoped sub-frames).

## The negative test

Deutsch's distinction provides a quality check orthogonal to the KB's type system. A well-formed note can pass every structural check (good title, description, links, area) while being merely adaptive — recording a pattern without explaining the mechanism. The test:

1. **Can you vary the explanation?** If you changed one premise, could you predict what changes in the conclusion? If yes, the note captures causal structure. If no, it may be recording correlation.
2. **Does it reach?** Would this insight apply in a domain you haven't considered? If yes, the mechanism is deeper than the specific case. If no, the note may be context-fitted.
3. **Can it be criticized?** Is there a specific way the explanation could be wrong, not just incomplete? The [falsifier blocks](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) practice operationalizes this.

These map to the three depths in [discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md): shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory with reach).

## The programming fast-pass as a reach bet

The [design methodology](./design-methodology-borrow-widely-filter-by-first-principles.md) gives programming patterns a "fast pass." In Deutsch's terms, this is a reach bet — we expect programming patterns to transfer because agents interpreting prompts are structurally similar to interpreters interpreting programming languages, not because of surface analogy. The full argument and evidence (including [Thalo's](./related-systems/thalo.md) convergent evolution) are in the methodology note.

## Open Questions

- Where in the KB are notes that are well-formed but merely adaptive? Those are candidates for deepening.
- The [discovery note's](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) hierarchy (feature -> structure -> generative model) parallels Deutsch's hierarchy (adaptive -> partially explanatory -> fully explanatory). Are these the same axis?
- Should "has explanatory reach" become a trait or quality signal, or is it better as an informal check during writing? (See also the [reach brainstorming note's](./brainstorming-how-reach-informs-kb-design.md) parallel question on surfacing reach explicitly.)

---

Relevant Notes:

- [design methodology — borrow widely, filter by first principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — grounds: first-principles filtering IS selecting for explanatory reach; this note explains why that filter works
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — parallels: the generative model depth maps to explanatory knowledge with reach
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — extends: Deutsch and Popper are allied — explanatory knowledge is the kind criticism can test; falsifier blocks operationalize one of the three tests
- [computational-model](./computational-model-index.md) — exemplifies: Programming-language concepts reaching into KB design is explanatory reach in action
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative.md) — complements: reach means the explanation makes structure accessible to observers in multiple contexts, not just the original one
- [a good agentic KB maximizes contextual competence](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — extends: places reach as the quality criterion within a full theory connecting learning operations to knowledge properties

Distilled into:

- [review-explanatory-reach](../tasks/recurring/review-explanatory-reach.md) — the three-part negative test (vary / reach / criticize)
- [WRITING.md](../instructions/WRITING.md) — lightweight reach check (item 5 in the pre-save checklist)
- [ingest SKILL.md](../instructions/ingest/SKILL.md) — reach assessment in extractable value and hard-to-vary test in curiosity gate
