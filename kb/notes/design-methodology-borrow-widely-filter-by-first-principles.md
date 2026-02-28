---
description: We borrow from any source but adopt based on first-principles support — except programming patterns, which get a fast pass because the bet is that claws are a new kind of software system
type: note
traits: []
status: seedling
areas: [claw-design]
---

# Design methodology — borrow widely, filter by first principles

The claw's design draws on programming language theory, cognitive science, HCI, and empirical observation. The methodology isn't about which source to prefer — it's about what gets an idea through the adoption gate.

## The adoption filter

**Any source is valid.** Cognitive science, programming, HCI, other claw-like systems, personal friction during use. We're not dogmatic about where ideas come from. The [related-systems](../../project_claw/notes/related-systems/related-systems-index.md) reviews exist precisely to widen the input surface.

**First principles reasoning is the main filter.** If we can derive *why* something works from the constraints of the domain — finite context windows, no import/resolution mechanism, agents reason over text, everything loaded must compete for attention — we adopt it with confidence. The [context loading economy](./context-loading-strategy.md) and [directory-scoped types](./directory-scoped-types-are-cheaper-than-global-types.md) arguments are examples: they follow directly from the constraints without needing analogies.

**Programming patterns get a fast pass.** We borrow programming patterns even without a complete theory for why they transfer — types, validation, testing, progressive compilation, version control, structural typing, the maturity ladder as gradual typing. The bet is that claws are a new kind of software system, not a new kind of cognitive tool. If that bet is right, programming patterns transfer structurally, not just by analogy. A compiler doesn't just *resemble* what we're doing — it *is* what we're doing, at a different point on the formalization spectrum.

Evidence for the bet: [Thalo](../notes/related-systems/thalo.md) independently arrived at building an actual compiler for knowledge management — Tree-Sitter grammar, typed entities, 27 validation rules. Someone else looked at the same problem and reached for the same toolbox. Convergence across independent projects is stronger evidence than any single design argument.

**Everything else earns its way in.** Cognitive science patterns, HCI patterns — these get adopted when first-principles reasoning supports them. [Three-space memory](./three-space-agent-memory-maps-to-tulving-taxonomy.md) is in the KB because it maps to a real architectural need (separating concerns with different churn rates), not because Tulving's taxonomy is authoritative for LLM agents. [Arscontexta's](../notes/related-systems/arscontexta.md) 249 research claims grounded in cognitive psychology are acknowledged but not adopted wholesale — the spreading activation model may not predict anything useful about how a 200k token context window behaves.

## Why the asymmetry

The asymmetry between programming and cognitive science isn't about one field being better. It's about the nature of the target system.

Human cognition is associative, embodied, affective. LLM agents process text in a fixed-size window with no persistent state between sessions. The mechanisms are different enough that cognitive science analogies need independent justification — they might transfer, but you can't assume they do.

Programming systems are formal, compositional, text-based. LLM knowledge systems are also formal (frontmatter schemas), compositional (notes link and compose), and text-based (markdown files). The structural similarity is close enough that programming patterns are more likely to transfer without independent justification. When we say "types mark affordances" or "validation is testing" or "promotion is progressive typing," these aren't metaphors — they describe the same mechanisms operating on different substrates.

**Empirical observation is the second strongest source — but weaker than first principles.** Direct observation of what works and what doesn't — the [what works](./what-works.md) and [what doesn't work](./what-doesnt-work.md) reviews, the improvement log, friction notes — doesn't go through the borrowing/adoption filter at all. It's evidence from *this* system, not transferred from another domain. The [verifiability gradient](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) was discovered by watching patterns in use, not derived from first principles or borrowed from another field.

The asymmetry with first principles is quantity vs weight. Observations are plentiful — every session generates friction signals, every review surfaces patterns. But each individual observation is weak: it could be a local quirk, a one-time context, an artefact of current scale. First principles are scarce — we have only a handful (finite context, no import mechanism, text-in text-out) — but each one is strong because it's derived from real constraints that won't change. A single first principle can reshape the whole design; a single observation usually can't. Observations accumulate into confidence through repetition; first principles carry confidence immediately.

The [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) applies: capture observations freely, then refine — the ones that recur across sessions and contexts graduate into durable patterns worth codifying.

---

Relevant Notes:
- [context loading strategy](./context-loading-strategy.md) — example of first-principles design: loading economy derived directly from context window constraints
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — example of first-principles design, explicitly frames directory-scoping as workaround for absent import mechanism
- [Thalo](../notes/related-systems/thalo.md) — independent convergence on programming patterns as evidence for the "claws are software" bet
- [Ars Contexta](../notes/related-systems/arscontexta.md) — the cognitive science alternative grounding; acknowledged, diverged from
- [programming practices apply to prompting](../notes/programming-practices-apply-to-prompting.md) — the general principle behind the programming fast pass
- [stabilisation is learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — example of empirical observation becoming theory
- [what works](./what-works.md) — empirical source

Topics:
- [claw-design](./claw-design.md)
