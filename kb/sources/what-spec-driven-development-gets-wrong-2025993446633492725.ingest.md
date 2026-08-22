---
description: Augment's argument that spec-driven development fails unless agents co-maintain the spec — bidirectional spec as a mechanism for matching maintenance throughput to generation throughput
source: https://x.com/augmentcode/status/2025993446633492725
captured: "2026-03-10T13:09:52.885228+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: 3b77dfcef8ff0b5d30ac33cbc4239005ad12c64f5211ae2399477073f87f382f
status_id: 2025993446633492725
conversation_id: 2025993446633492725
post_count: 1
ingested: "2026-03-10"
type: kb/sources/types/ingest-report.md
domains: [spec-driven-development, agent-architecture, documentation-maintenance]
---

# Ingest: What spec-driven development gets wrong

## Classification

Augment describes what they built (Intent) and why, grounded in a specific design problem they encountered. Not a conceptual essay: it makes an architectural claim backed by a product they shipped.

Author: @augmentcode — the official account for Augment Code, an AI coding tool company. This is a vendor post describing their own product (Intent). Credibility comes from having built and shipped the system; bias comes from the same source.

## Summary

Augment argues that spec-driven development (SDD) fails for the same reason all documentation-first initiatives fail: documents decay because maintenance is invisible, unrewarded work that humans reliably won't do. It treats stale specs as especially risky because agents execute them confidently without flagging mismatches. Its proposed fix is the bidirectional spec: a coordinator agent drafts a spec from human intent, agents update it as they discover reality diverges from the plan, and the human reviews at any point. The core design challenge is update granularity — surfacing directional decisions ("found an existing auth context, wired into that") without narrating every line. The "junior engineer" analogy captures the desired relationship: agents report interpretation choices, not implementation details.

## Connections Found

The `/connect` discovery found 11 connections across the KB, with 5 strong, 4 moderate, and 2 weaker-but-genuine.

**Strong connections:**

- [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: The entire SDD argument rests on the underspecification framework. The dark mode example ("found an existing theme context provider") is an interpretation choice being surfaced rather than silently committed. The bidirectional spec is a mechanism for making projections visible.

- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — **exemplifies**: The dark mode example is a disambiguation failure surfacing mid-execution. The human's spec assumed a new store; the agent found an existing context provider. The bidirectional spec catches disambiguation failures in real time rather than at iteration boundaries.

- [deploy-time-learning-is-the-missing-middle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — **exemplifies**: Augment independently arrives at the same co-evolution loop — a natural-language spec and code co-evolve, with the spec updating as agents discover reality. The spec isn't temporary backlog waiting to become code; it's a persistent co-maintained artifact.

- [maintenance-capacity-must-match-harmful-artifact-inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) — **extends**: The core observation ("documentation-first initiatives fail because maintenance is invisible work") is the harmful-inflow problem stated for specs. A bidirectional spec couples preventive maintenance to ordinary work and may reduce the rate at which stale specifications enter use; the source does not establish that capacity automatically matches the resulting risk.

- [inspectable-artifact-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — **exemplifies**: The bidirectional spec IS an inspectable substrate — a plain-text artifact that any party can inspect, diff, and review.

**Moderate connections:** deploy-time-learning-the-missing-middle (the spec is a deploy-time learning artifact on the verifiability gradient), constraining (progressive narrowing of interpretation space through agent discovery and human approval), [Selecting an LLM output fixes a result, not its interpretation](../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) (sharpens — each accepted spec update selects a version for operative use, fixing which artifact guides implementation without making its natural-language meaning unique), [spec-mining-as-codification](../notes/spec-mining-as-codification.md) (contrasts — bidirectional spec keeps the artifact current during discovery, while spec mining is the later move where recurring discoveries harden into deterministic checks or code), [evolving-understanding-needs-re-distillation-not-composition](../notes/evolving-understanding-needs-holistic-rewrite-not-composition.md) (extends the re-distillation pattern by making it bidirectional), Decapod (contrasts — verified vs evolved specs, complementary strategies for different confidence phases).

**Synthesis opportunities identified:** (1) Bidirectional artifact maintenance as a general design pattern for any long-lived working document in agent systems. (2) Disambiguation-failure detection mechanisms across agile, SDD, and proof-gating approaches. (3) An unnamed "confidence trap" mechanism where authoritative artifacts suppress fallback discovery when stale.

## Extractable Value

1. **Bidirectional spec as prevention-coupled maintenance** — agents update the spec as a side effect of doing the work, which can reduce the rate at which stale specifications become harmful retained artifacts. This is a candidate design witness for [maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md), but the source supplies no outcome evidence that the coupled maintenance is sufficient. [quick-win]

2. **Update granularity as a design variable** — "Too much and the spec becomes noise you learn to ignore. Too little and you're back to guessing what happened." This is a signal-to-noise tradeoff on inspectable substrates that the KB hasn't articulated. What counts as a "directional decision" worth surfacing? [experiment]

3. **The "confidence trap" of stale authoritative artifacts** — "A stale spec misleads agents that don't know any better. They'll execute a plan that no longer matches reality, confidently." This generalizes the mechanism in [stale indexes reduce discovery when they suppress fallback search](../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md): an outdated artifact can lower discovery recall when consumers treat it as exhaustive and therefore skip a more current check. [deep-dive]

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

Evaluate [maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) against the bidirectional spec as a second design pattern alongside Harness Engineering's background cleanup agents. Augment's approach couples preventive maintenance to the work that changes the spec rather than running repair in parallel, but the source offers no evidence that it keeps harmful inflow within a quality bound.
