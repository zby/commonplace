---
description: Without explicit goals in the always-loaded control-plane file, agents cannot reject well-written but off-scope material — a universal quality guide provides writing criteria but not domain scope
type: kb/types/note.md
tags: [architecture]
status: seedling
---

# KB goals in always-loaded context guide inclusion decisions

Every time an agent creates a note, it makes an inclusion decision: does this knowledge belong in *this* KB? A writing guide can provide universal quality criteria (claim titles, retrieval-oriented descriptions, composability) but says nothing about domain scope. A [routing table](./agents-md-should-be-organized-as-a-control-plane.md) can say where artifacts go, but not whether they should exist.

This gap doesn't surface in a KB about its own domain — a methodology KB about methodology is self-defining. It surfaces the moment a KB is deployed for a specific domain (legal research, system architecture, API design), where the agent otherwise has no basis for:

- Rejecting knowledge that's well-written but out of scope
- Deciding whether a source is worth ingesting
- Choosing between a note and a log entry for marginal material
- Evaluating whether accumulated knowledge serves the KB's purpose

## Where goals belong

The [control-plane model](./agents-md-should-be-organized-as-a-control-plane.md) defines three layers: invariants, routing, escalation boundaries. KB goals are a new invariant in Layer 1 — "this KB is about X, not Y" is a rule that must hold in every session. They define the *domain scope* within which routing operates. They belong in the control-plane file (the always-loaded agent instructions) because:

1. **Every write is an inclusion decision.** The question "does this belong here?" is as frequent as "where does this go?" — both need zero-hop access.
2. **Loading frequency is high, failure cost is high.** An agent that ingests off-topic material wastes context and pollutes search results. Both placement criteria from the control-plane model point to always-loaded.
3. **No extra hop.** A separate `GOALS.md` would add one tool call to every write path. Since the control-plane file is already loaded, embedding goals there costs nothing.

## What varies per installation

| Concern | Per-installation or universal? |
|---|---|
| Purpose — what decisions/actions the KB supports | Per-installation |
| Domain — what the KB is about (scope boundary) | Per-installation |
| Include — what types of knowledge belong | Per-installation |
| Exclude — what doesn't belong despite seeming relevant | Per-installation |
| Quality bar — domain-specific "good enough" standards | Per-installation |
| Routing, type system, writing conventions, link semantics | Universal (framework-provided) |

Only the per-installation rows require human input. The universal rows are shipped by the framework and can be updated mechanically on upgrade.

## What makes each subsection work

**Purpose** — Start from the users, not the domain. Who will use this KB? What are they trying to do better? A good purpose statement names the decisions or actions the KB supports: "supports the API team in making design decisions about the payment service" is actionable; "stores knowledge about payments" is not.

**Domain** — Draw a scope boundary. Everything inside is in scope, everything outside is not. Be specific enough that an agent can decide "does this belong?" without asking. Name adjacent domains and clarify whether they're in or out: "adjacent systems (auth, billing) are in scope only where they interact with payments."

**Include** — What types of knowledge belong here? Design decisions, failure analysis, integration patterns, operational procedures? This section is less critical than Exclude because the routing table already covers structural placement.

**Exclude** — The most valuable subsection. Scope creep is the default failure mode of a KB — every piece of knowledge looks relevant in isolation. Name specific things that seem relevant but don't belong: "business rules live in the product wiki, not here." "General distributed systems theory is out of scope unless it directly informs a specific design decision." The Exclude list is what makes the Include list meaningful.

**Quality bar** — When is a piece of knowledge worth a note vs. a log entry vs. nothing? A writing guide says how to write well; this subsection says when to write at all. Domain-specific standards: "a design decision is worth a note when it affects more than one endpoint; single-endpoint details belong in code comments."

## Relation to reach

The KB Goals section is not a replacement for the [reach criterion](./first-principles-reasoning-selects-for-explanatory-reach-over.md). Reach is a quality criterion — knowledge with explanatory depth that transfers to new situations. Goals are the domain filter — *which* situations this KB cares about transferring to. A note can have high reach but be out of scope (a brilliant insight about compiler optimization in a KB about payment architecture), or low reach but in scope (a specific failure case that the team needs to remember).

Both filters apply. Goals first (is this in scope?), then reach (is this worth the context it costs?).

## Goal revision

Goals are set at installation time but domains evolve. When a KB's scope shifts — new responsibilities, deprecated subsystems, changed team boundaries — the Goals section should be updated to match. Stale goals are worse than absent goals: they actively misdirect the agent into rejecting relevant material or accepting irrelevant material. Review goals when the KB's domain changes, not on a schedule.

---

Relevant Notes:

- [control-plane-goals](../reference/control-plane-goals.md) — current-state: how commonplace realises this argument today through `AGENTS.md`, the scaffold template, and the install-time fill-in flow
- [AGENTS.md should be organized as a control plane](./agents-md-should-be-organized-as-a-control-plane.md) — extends: adds domain scope as a new invariant (Layer 1) in the control-plane model
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: goals must be always-loaded because the inclusion question arises every session
- [generate instructions at build time](./generate-instructions-at-build-time.md) — enables: the structural sections of the fragment are generated; only goals require human input
- [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — grounds: goals complement artifact-quality and ingress constraints but do not replace them
