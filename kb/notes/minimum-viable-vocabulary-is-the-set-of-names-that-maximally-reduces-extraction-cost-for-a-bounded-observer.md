---
description: Reframes "minimum viable ontology" as an optimization problem — the vocabulary that, once acquired, maximally reduces a bounded observer's extraction cost for a domain; grounds the pedagogical intuition of "conceptual thresholds" in the KB's information-theoretic framework
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Minimum viable vocabulary is the set of names that maximally reduces extraction cost for a bounded observer

When entering an unfamiliar domain, a bounded observer — a human without domain experience, an agent without domain vocabulary in context — faces a gap between the information present in domain artifacts and the information they can extract. The full structure is there in the textbooks, codebases, and papers. The observer cannot reach it because extraction requires computation they lack: the right categories, the right distinctions, the right names.

Kim (2026) calls a curated term list that closes enough of this gap a "minimum viable ontology," framing the terms as "conceptual thresholds" — vocabulary that, once acquired, unlocks comprehension. The pedagogical intuition is sound, but the framing is imprecise: which terms? how many? what makes a term "threshold" rather than merely useful? This note uses "vocabulary" rather than Kim's "ontology" because the claim is about names that reduce extraction cost, not about a formal ontological commitment.

The KB's information-theoretic framework turns this imprecise intuition into an optimization problem. [Information value is observer-relative](./information-value-is-observer-relative.md) because extraction requires computation — a restructuring that preserves or even reduces Shannon entropy can still make structure accessible to a bounded observer that could not previously extract it. The minimum viable vocabulary is the smallest set of names such that, once in context, the observer can extract domain structure that was previously inaccessible. It is, in other words, the vocabulary that maximally reduces extraction cost for a given observer.

Two mechanisms already in the KB explain why a set of names can have this effect — why vocabulary, specifically, is the right unit of extraction cost reduction.

**Naming amortizes discovery cost.** [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) argues that the highest-value act in a knowledge system is creating a named concept — once a structure has a name, recognizing further instances becomes cheap. Each term in a minimum viable vocabulary is a discovery someone else already made, packaged so the newcomer can recognize instances without repeating the original discovery.

**Distillation targets a bounded observer.** [Distillation](./distillation.md) is targeted extraction shaped by a use case, a context budget, and an agent. A minimum viable vocabulary is a distillation of domain knowledge where the target is a newcomer and the context budget is minimal. Because each distillation is shaped by a specific observer's bounds, multiple minimum viable vocabularies for the same domain are expected — a human learning 3D graphics and an agent parsing 3D file formats face different computational limits, so the vocabulary that maximally reduces extraction cost differs for each.

Together, the two mechanisms ground the optimization claim: naming provides the unit of cost reduction (each name amortizes a discovery), and distillation explains why the optimal set varies by observer (each observer has different computational bounds). This framing also makes the concept testable in principle. Given two candidate vocabularies and the same set of domain artifacts, the better vocabulary is the one that enables a bounded observer to extract more structure. The test requires a measure of extraction — the [epiplexity framework's](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md) prequential coding is one candidate — and a fixed observer. Kim's prototype (domainmaps.co) provides neither, but the framework specifies what an evaluation would need.

## Open Questions

- Does the pedagogical literature on threshold concepts (Meyer & Land) provide selection criteria that map onto extraction cost? Their criteria — transformative, irreversible, integrative, bounded, troublesome — sound like properties of names that unlock large amounts of previously inaccessible structure, which is what extraction cost reduction measures.
- Is there a meaningful difference between minimum viable vocabulary for humans (who retain vocabulary across sessions) and for agents (who need it injected each session)? The agent case maps directly to [context injection](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — the vocabulary must be loaded, not learned.

---

Sources:

- [Minimum Viable Ontology tweet thread (Kim, 2026)](../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md) — origin: names the concept and the "conceptual thresholds" framing; this note regrounds the intuition in the KB's information-theoretic framework

Relevant Notes:

- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: MVV is a concrete instance of deterministic transformation that makes structure accessible to bounded observers
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — mechanism: naming amortizes discovery cost; MVV packages pre-named structures for reuse by newcomers
- [distillation](./distillation.md) — mechanism: MVV is distillation where the target is a domain newcomer and the context budget is minimal
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — enables: MVV is knowledge compressed to fit context constraints when full domain methodology won't fit
- [agent statelessness means the context engine should inject context automatically](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — extends: for agents, MVV must be injected each session rather than retained
