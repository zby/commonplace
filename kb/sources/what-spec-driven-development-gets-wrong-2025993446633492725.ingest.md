---
description: Augment's argument that spec-driven development fails unless agents co-maintain the spec — bidirectional spec as a mechanism for matching maintenance throughput to generation throughput
source_snapshot: what-spec-driven-development-gets-wrong-2025993446633492725.md
ingested: 2026-03-10
type: practitioner-report
domains: [spec-driven-development, agent-architecture, documentation-maintenance]
---

# Ingest: What spec-driven development gets wrong

Source: what-spec-driven-development-gets-wrong-2025993446633492725.md
Captured: 2026-03-10
From: https://x.com/augmentcode/status/2025993446633492725

## Classification

Type: practitioner-report — Augment describes what they built (Intent) and why, grounded in a specific design problem they encountered. Not a conceptual essay: it makes an architectural claim backed by a product they shipped.

Domains: spec-driven-development, agent-architecture, documentation-maintenance

Author: @augmentcode — the official account for Augment Code, an AI coding tool company. This is a vendor post describing their own product (Intent). Credibility comes from having built and shipped the system; bias comes from the same source.

## Summary

Augment argues that spec-driven development (SDD) fails for the same reason all documentation-first initiatives fail: documents decay because maintenance is invisible, unrewarded work that humans reliably won't do. Stale specs are worse than stale docs because agents execute them confidently without flagging mismatches. Their proposed fix is the bidirectional spec: a coordinator agent drafts a spec from human intent, agents update it as they discover reality diverges from the plan, and the human reviews at any point. The core design challenge is update granularity — surfacing directional decisions ("found an existing auth context, wired into that") without narrating every line. The "junior engineer" analogy captures the desired relationship: agents report interpretation choices, not implementation details.

## Connections Found

The `/connect` discovery found 11 connections across the KB, with 5 strong, 4 moderate, and 2 weaker-but-genuine.

**Strong connections:**

- [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: The entire SDD argument rests on the underspecification framework. The dark mode example ("found an existing theme context provider") is an interpretation choice being surfaced rather than silently committed. The bidirectional spec is a mechanism for making projections visible.

- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — **exemplifies**: The dark mode example is a disambiguation failure surfacing mid-execution. The human's spec assumed a new store; the agent found an existing context provider. The bidirectional spec catches disambiguation failures in real time rather than at iteration boundaries.

- [deploy-time-learning-is-agile-for-human-ai-systems](../notes/deploy-time-learning-is-agile-for-human-ai-systems.md) — **exemplifies**: Augment independently arrives at the same co-evolution loop — prose spec and code co-evolve, with the spec updating as agents discover reality. The spec isn't temporary backlog waiting to become code; it's a persistent co-maintained artifact.

- [entropy-management-must-scale-with-generation-throughput](../notes/entropy-management-must-scale-with-generation-throughput.md) — **extends**: The core observation ("documentation-first initiatives fail because maintenance is invisible work") is the entropy management problem stated for specs. The bidirectional spec is Augment's answer to throughput matching — agents maintain the spec as a side effect of work, so maintenance scales automatically with generation.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **exemplifies**: The bidirectional spec IS an inspectable substrate — a plain-text artifact that any party can inspect, diff, and review.

**Moderate connections:** deploy-time-learning-the-missing-middle (the spec is a deploy-time learning artifact on the verifiability gradient), constraining (progressive narrowing of interpretation space through agent discovery and human approval), [storing-llm-outputs-is-constraining](../notes/storing-llm-outputs-is-constraining.md) (sharpens — each accepted spec update commits one interpretation of the evolving plan into a durable artifact, not just a transient conversation state), [spec-mining-as-codification](../notes/spec-mining-as-codification.md) (contrasts — bidirectional spec keeps the artifact current during discovery, while spec mining is the later move where recurring discoveries harden into deterministic checks or code), active-campaign-understanding (extends the single-coherent-narrative pattern by making it bidirectional), Decapod (contrasts — verified vs evolved specs, complementary strategies for different confidence phases).

**Synthesis opportunities identified:** (1) Bidirectional artifact maintenance as a general design pattern for any long-lived working document in agent systems. (2) Disambiguation-failure detection mechanisms across agile, SDD, and proof-gating approaches. (3) An unnamed "confidence trap" mechanism where authoritative artifacts suppress fallback discovery when stale.

## Extractable Value

1. **Bidirectional spec as throughput-matching mechanism** — agents maintain the spec as a side effect of doing the work, which is a concrete architecture where maintenance throughput automatically matches generation throughput. This is a specific design pattern the [entropy-management](../notes/entropy-management-must-scale-with-generation-throughput.md) note can reference as evidence. [quick-win]

2. **Update granularity as a design variable** — "Too much and the spec becomes noise you learn to ignore. Too little and you're back to guessing what happened." This is a signal-to-noise tradeoff on inspectable substrates that the KB hasn't articulated. What counts as a "directional decision" worth surfacing? [experiment]

3. **The "confidence trap" of stale authoritative artifacts** — "A stale spec misleads agents that don't know any better. They'll execute a plan that no longer matches reality, confidently." This generalizes the [stale-indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) phenomenon: any artifact that agents treat as authoritative is actively harmful when stale, because it suppresses the fallback to more current information. Multiple notes share this pattern but it hasn't been named. [deep-dive]

4. **The junior engineer analogy as a design spec for agent reporting** — surface interpretation choices, not implementation details. This is a concrete operationalization of what "inspectable substrate" means in practice for agent-to-human communication. [just-a-reference]

5. **Bidirectional spec contrasted with Decapod's verified spec** — two complementary strategies for spec lifecycle: verify the spec was followed (Decapod) vs evolve the spec to match reality (Augment). Different assumptions about when the plan can be trusted. [experiment]

## Limitations (our opinion)

**What is not visible:**

- **Vendor bias.** This is Augment's official account describing their own product. The dark mode example is a marketing scenario, not a case study. We don't know how Intent performs on messy real-world tasks where the "found an existing X, wired into that" narrative breaks down — e.g., when the agent's discovery is wrong, when multiple agents update the spec with contradictory findings, or when the spec becomes too large to review.

- **Survivorship in the junior engineer analogy.** Good juniors surface directional decisions. Bad juniors either narrate everything or surface nothing. The post assumes agents reliably identify what's directional — but this is exactly the interpretation-underspecification problem the KB's [projection model](../notes/agentic-systems-interpret-underspecified-instructions.md) identifies. The agent must decide which of its decisions are "directional" using... an underspecified spec of what "directional" means.

- **Sample size of one design.** The bidirectional spec is presented as THE answer, but alternatives exist: background cleanup agents (the [harness engineering](harness-engineering-leveraging-codex-agent-first-world.ingest.md) approach), proof-gating (Decapod), or automated spec mining. These are complementary strategies, not competitors, but the post doesn't acknowledge the design space.

- **Scaling limits unaddressed.** What happens when the spec grows to hundreds of subtasks? When multiple agents update it concurrently? When the human can't review all updates? The post describes a three-subtask example. The interesting failure modes are at scale.

- **No evidence that it works.** The post describes a design and an example, but offers no data on whether bidirectional specs actually stay current in practice, whether humans review the updates, or whether the approach reduces the failure modes it claims to solve.

## Recommended Next Action

Update [entropy-management-must-scale-with-generation-throughput](../notes/entropy-management-must-scale-with-generation-throughput.md): add the bidirectional spec as a second design pattern (alongside harness engineering's background cleanup agents) for achieving maintenance-generation throughput matching. The note currently has one concrete architecture (OpenAI Codex's cleanup agents); the Augment approach is a structurally different solution to the same problem — maintenance as a side effect of generation rather than maintenance as a parallel process.
