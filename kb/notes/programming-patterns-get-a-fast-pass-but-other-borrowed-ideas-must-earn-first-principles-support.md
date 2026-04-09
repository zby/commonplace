---
description: We borrow from any source but adopt based on first-principles support — except programming patterns, which get a fast pass because the bet is that knowledge bases are a new kind of software system
type: note
traits: []
status: seedling
tags: [foundations]
---

# Programming patterns get a fast pass but other borrowed ideas must earn first-principles support

The KB's design draws on programming language theory, cognitive science, HCI, and empirical observation. Any source is valid — the [related-systems](./related-systems/related-systems-index.md) reviews exist precisely to widen the input surface. What varies is the adoption gate: not all sources face the same bar.

## The programming fast pass

We borrow programming patterns without a complete theory for why they transfer — types, validation, testing, progressive compilation, version control, structural typing, the maturity ladder as gradual typing. The bet is that agents interpreting prompts are doing something structurally similar to interpreters interpreting programming languages: both are bounded processors composing text under constraints. If that bet is right, programming patterns transfer because the mechanisms are the same, not by analogy.

Programming systems are formal, compositional, text-based. LLM knowledge systems are also formal (frontmatter schemas), compositional (notes link and compose), and text-based (markdown files). When we say "types mark affordances" or "validation is testing" or "promotion is progressive typing," these aren't metaphors — they describe the same mechanisms operating on different substrates.

Evidence for the bet: [Thalo](../notes/related-systems/thalo.md) independently arrived at building an actual compiler for knowledge management — Tree-Sitter grammar, typed entities, 27 validation rules. Someone else looked at the same problem and reached for the same toolbox. Convergence across independent projects is stronger evidence than any single design argument.

## First principles: the main filter for everything else

If we can derive *why* something works from the constraints of the domain — finite context windows, no import/resolution mechanism, agents reason over text, everything loaded must compete for attention — we adopt it with confidence. The [context loading economy](./instruction-specificity-should-match-loading-frequency.md) and [directory-scoped types](./directory-scoped-types-are-cheaper-than-global-types.md) arguments are examples: they follow directly from the constraints without needing analogies.

Cognitive science patterns, HCI patterns — these get adopted when first-principles reasoning supports them. [Three-space memory](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) is in the KB because it maps to a real architectural need (separating concerns with different churn rates), not because Tulving's taxonomy is authoritative for LLM agents. [Arscontexta's](../notes/related-systems/arscontexta.md) 249 research claims grounded in cognitive psychology are acknowledged but not adopted wholesale — the spreading activation model may not predict anything useful about how a 200k token context window behaves.

The asymmetry between programming and cognitive science isn't about one field being better. It's about the nature of the target system. Human cognition is associative, embodied, affective. LLM agents process text in a fixed-size window with no persistent state between sessions. The mechanisms are different enough that cognitive science analogies need independent justification — they might transfer, but you can't assume they do.

## Legal drafting: compelling but untested

Law has centuries of methodology for the same problem: writing natural language specifications interpreted by a judgment-exercising processor. Unlike programming, [legal drafting operates in the same medium as prompts](./legal-drafting-solves-the-same-problem-as-context-engineering.md): natural language with irreducible ambiguity. The structural parallel is compelling (precedent is constraining, canons of interpretation narrow the reading space), but we haven't yet borrowed a concrete technique from law and applied it successfully. Until we have examples of legal techniques improving prompt or KB design in practice, this stays a hypothesis, not a fast pass.

## Empirical observation: a different path entirely

Direct observation of what works and what doesn't — the improvement log, friction notes, prose reviews — doesn't go through the borrowing/adoption filter at all. It's evidence from *this* system, not transferred from another domain. The [verifiability gradient](./deploy-time-learning-is-the-missing-middle.md) was discovered by watching patterns in use, not derived from first principles or borrowed from another field.

The asymmetry with first principles is quantity vs weight. Observations are plentiful — every session generates friction signals, every review surfaces patterns. But each individual observation is weak: it could be a local quirk, a one-time context, an artefact of current scale. First principles are scarce — we have only a handful (finite context, no import mechanism, text-in text-out) — but each one is strong because it's derived from real constraints that won't change. A single first principle can reshape the whole design; a single observation usually can't. Observations accumulate into confidence through repetition; first principles carry confidence immediately.

The [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) applies: capture observations freely, then refine — the ones that recur across sessions and contexts graduate into durable patterns worth codifying.

---

Relevant Notes:

- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — example of first-principles design: loading economy derived directly from context window constraints
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — example of first-principles design, explicitly frames directory-scoping as workaround for absent import mechanism
- [Thalo](../notes/related-systems/thalo.md) — independent convergence on programming patterns as evidence for the "knowledge bases are software" bet
- [Ars Contexta](../notes/related-systems/arscontexta.md) — the cognitive science alternative grounding; acknowledged, diverged from
- [underspecification and indeterminism complicate the transfer](./underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md) — develops: the practices transfer but two LLM properties make them harder in distinct ways; testing is doubled for two different reasons
- [constraining](./definitions/constraining.md) — example of empirical observation becoming theory
