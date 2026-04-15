---
description: Weights, memory entries, prompts, schemas, and scripts span three substrate classes (opaque, prose, symbolic) stored across many backends; conflating substrate, backend, and artifact form blurs substrate comparisons
type: note
traits: [has-comparison, title-as-claim]
tags: [learning-theory]
status: current
---

# Substrate class, backend, and artifact form are separate axes that get conflated

Agent-learning comparisons conflate three axes. The **substrate class** axis distinguishes how the learned result is represented: as non-interpretable distributed state, as natural-language units, or as formal-semantic units. The **artifact form** axis distinguishes what a learned unit looks like (memory entries, rules, schemas, scripts). The **storage backend** axis distinguishes where units live (repo files, database rows, memory services). Mixing the axes blurs the comparison space: you end up arguing "memory entries vs weights" when the real contrast is between substrate classes, or treating "repo artifacts" as an umbrella when it's one backend choice among many.

## Three substrate classes

The three substrate classes differ in representation, consumer, and semantics:

- **Opaque substrate** (the non-interpretable case) — the learned result lives in model weights or other hidden state; consumed by the model itself, not readable as discrete units. AgeMem and [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) are clean examples.
- **Prose substrate** — the learned result lives in discrete *natural-language* objects — notes, memory entries, reflections, rules, prompts, playbooks. Consumed by an LLM interpreting [underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md). Readable and diffable, but semantics are underspecified.
- **Symbolic substrate** — the learned result lives in discrete objects with **formal semantics** — schemas, tests, scripts, tools, types. Consumed by a deterministic interpreter. Readable, diffable, *and* exactly verifiable.

The split sits across two orthogonal axes: opaque vs. readable, and (within readable) informal vs. formal semantics. The prose/symbolic boundary is the phase transition [codification](./definitions/codification.md) crosses and [constraining](./definitions/constraining.md) aims for — medium changes (markdown → code), consumer changes (LLM → interpreter), verification regime changes (underspecified → formal).

Opacity isn't binary — any substrate becomes practically opaque at enough scale, so what distinguishes substrates in practice is their opacity at operational scale. Distributed representations cross into opacity almost immediately: meaning is smeared across many weights jointly, so even a modestly-sized network resists per-unit inspection. Truly tiny networks can be read by hand (mechanistic interpretability on toy models does this), but the threshold is very low. Localized substrates stay readable at much larger aggregates: per-unit readability plus search, diffing, and modular revision let you work with scales that would be hopeless in a weight matrix of comparable size.

## Backend: where artifacts live

A substrate class says nothing about storage. Prose and symbolic artifacts both live in many backends — repo files, database rows, service-managed memory objects, graph stores, or vector stores with attached records and provenance. This is why "repo artifacts" is too narrow as the umbrella term. Repo-hosted markdown is one important backend, especially for commonplace, but neither substrate is tied to it. [Cognee](../agent-memory-systems/reviews/cognee.md) keeps prose-substrate units in a database-backed poly-store; the backend changed, the substrate class did not.

## Artifact form: what the units look like within a substrate

Within a substrate, systems can produce many artifact forms. Prose-substrate forms include memory entries, reflections, ranked memories, and playbook entries, differing in granularity, retrieval mode, and how directly they constrain later behaviour. Symbolic-substrate forms include schemas, tests, runnable scripts, and extracted tools. Artifact form is downstream of substrate but largely orthogonal to backend — you can push code into a database or memory entries into a repo, though backends differ in their affordances for each form.

## Why the distinction matters

Separating the three axes prevents category mistakes that keep recurring in comparisons across this KB.

[Files beat a database for agent-operated knowledge bases](./files-not-database.md) argues that a database schema forces premature commitment to access patterns — a claim about **which backend** to pick, not about which substrate class to use. Separating the axes makes that scope visible: files can beat a database for a young KB without implying anything about the prose/symbolic boundary.

The comparison between [trajectory-informed memory generation](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) — whose learned result is short natural-language entries the paper calls *tips* — and [AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md) sharpens too. The real contrast is not "tips vs weights" but **prose substrate vs opaque substrate**. Tips are one artifact form on the prose side.

[Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) can span all three substrates — fine-tuning and LoRA are deploy-time learning in the opaque substrate, at smaller scale than full training. Commonplace's version stays on the readable substrates: prose-substrate learning (notes, skills, prompts, rules) dominates day-to-day, while [codification](./definitions/codification.md) is the move to symbolic-substrate learning (schemas, tests, scripts). The repo is a backend choice — a different system could do the same two-substrate loop through a memory service or database.

The taxonomy that falls out:

| Learned result | Substrate class | Backend | Artifact form |
|---|---|---|---|
| AgeMem memory policy | Opaque | Model weights | Learned policy |
| Trajectory-informed memory | Prose | Memory store / DB / files | Tips (short natural-language memories) |
| Commonplace notes, skills, prompts | Prose | Repo | Notes, rules, playbooks |
| Commonplace codified procedures | Symbolic | Repo | Schemas, tests, scripts, tools |

With the levels separated, substrate trade-offs become easier to state. Opaque learning usually buys tighter optimisation at the cost of per-unit inspection. Prose learning recovers readability, diffability, and composability but keeps underspecified semantics and depends on retrieval and lifecycle design. Symbolic learning adds formal semantics on top — exact verification, deterministic execution — at the cost of needing a strong enough oracle to commit to one interpretation.

---

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: argues that non-weight adaptation is still learning if it durably changes capacity
- [codification](./definitions/codification.md) — defines the phase transition between prose and symbolic substrates
- [constraining](./definitions/constraining.md) — the mechanism that operates across prose substrate and reaches symbolic substrate at its far end
- [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — applies: commonplace's main loop, spanning prose and symbolic substrates
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: already distinguishes promotion targets; this note separates substrate class from backend and artifact form
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — sharpens: backend choice is downstream of substrate choice
- [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: readability is shared by both non-opaque substrates
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a clean opaque case that makes the substrate split visible
- [Cognee](../agent-memory-systems/reviews/cognee.md) — counterexample: database-backed prose artifacts show that files are not the only backend
