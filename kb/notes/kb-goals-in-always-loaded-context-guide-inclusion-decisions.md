---
description: Without explicit goals in the always-loaded control-plane file, agents cannot reject well-written but off-scope material — WRITING.md provides quality criteria but not domain scope
type: note
tags: []
status: seedling
---

# KB goals in always-loaded context guide inclusion decisions

Every time an agent creates a note, it makes an inclusion decision: does this knowledge belong in *this* KB? [WRITING.md](../instructions/WRITING.md) provides universal quality criteria (claim titles, retrieval-oriented descriptions, composability) but says nothing about domain scope. The [routing table](./agents-md-should-be-organized-as-a-control-plane.md) says where artifacts go, but not whether they should exist.

This gap doesn't surface in commonplace itself — the domain is self-defining (KB methodology about KB methodology). It surfaces at installation time, when a user creates a KB about a specific domain (legal research, system architecture, API design). Without explicit goals, the agent has no basis for:

- Rejecting knowledge that's well-written but out of scope
- Deciding whether a source is worth ingesting
- Choosing between a note and a log entry for marginal material
- Evaluating whether accumulated knowledge serves the KB's purpose

## Where goals belong

The [control-plane model](./agents-md-should-be-organized-as-a-control-plane.md) defines three layers: invariants, routing, escalation boundaries. KB goals are a new invariant in Layer 1 — "this KB is about X, not Y" is a rule that must hold in every session. They define the *domain scope* within which routing operates. They belong in the control-plane file (CLAUDE.md/AGENTS.md) because:

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
| Routing table — where artifacts go | Universal (from commonplace) |
| Type system — what structural forms exist | Universal (from commonplace) |
| Writing conventions — how to write well | Universal (from commonplace) |
| Link semantics — how notes connect | Universal (from commonplace) |

Only the per-installation rows require human input. Everything else is generated from commonplace and can be updated mechanically on upgrade.

## How to fill in the Goals section

The [control-plane template](../../AGENTS.md.template) includes a KB Goals section with five subsections. Guidance for each:

**Purpose** — Start from the users, not the domain. Who will use this KB? What are they trying to do better? A good purpose statement names the decisions or actions the KB supports: "supports the API team in making design decisions about the payment service" is actionable; "stores knowledge about payments" is not.

**Domain** — Draw a scope boundary. Everything inside is in scope, everything outside is not. Be specific enough that an agent can decide "does this belong?" without asking. Name adjacent domains and clarify whether they're in or out: "adjacent systems (auth, billing) are in scope only where they interact with payments."

**Include** — What types of knowledge belong here? Design decisions, failure analysis, integration patterns, operational procedures? This section is less critical than Exclude because the routing table already covers structural placement.

**Exclude** — The most valuable section. Scope creep is the default failure mode of a KB — every piece of knowledge looks relevant in isolation. Name specific things that seem relevant but don't belong: "business rules live in the product wiki, not here." "General distributed systems theory is out of scope unless it directly informs a specific design decision." The Exclude list is what makes the Include list meaningful.

**Quality bar** — When is a piece of knowledge worth a note vs. a log entry vs. nothing? WRITING.md says how to write well; this section says when to write at all. Domain-specific standards: "a design decision is worth a note when it affects more than one endpoint; single-endpoint details belong in code comments."

## Relation to reach

The KB Goals section is not a replacement for the [reach criterion](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md). Reach is a key quality criterion — knowledge with explanatory depth that transfers to new situations. Goals are the domain filter — *which* situations this KB cares about transferring to. A note can have high reach but be out of scope (a brilliant insight about compiler optimization in a KB about payment architecture), or low reach but in scope (a specific failure case that the team needs to remember).

Both filters apply. Goals first (is this in scope?), then reach (is this worth the context it costs?).

## Goal revision

Goals are set at installation time but domains evolve. When a KB's scope shifts — new responsibilities, deprecated subsystems, changed team boundaries — the Goals section should be updated to match. Stale goals are worse than absent goals: they actively misdirect the agent into rejecting relevant material or accepting irrelevant material. Review goals when the KB's domain changes, not on a schedule.

---

Relevant Notes:

- [AGENTS.md should be organized as a control plane](./agents-md-should-be-organized-as-a-control-plane.md) — extends: adds domain scope as a new invariant (Layer 1) in the control-plane model
- [commonplace installation architecture](./commonplace-installation-architecture.md) — enables: the installation step that generates the control-plane fragment
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: goals must be always-loaded because the inclusion question arises every session
- [generate instructions at build time](./generate-instructions-at-build-time.md) — enables: the structural sections of the fragment are generated; only goals require human input
- [a good agentic KB maximizes contextual competence](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — grounds: the reach criterion and quality theory that goals complement but don't replace
- [control-plane template](../../AGENTS.md.template) — implements: the template that operationalizes this note

Distilled into:

- [INSTALL.md](../../INSTALL.md) — the "Fill in the KB Goals section" guidance in step 4
