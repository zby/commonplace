---
description: Decomposition, scoping, and verification may form a strict dependency chain (topology → isolation → verification) rather than independent design choices — tests the simpler account that decomposition alone implies the other two
type: kb/types/note.md
tags: [computational-model, llm-interpretation-errors]
status: speculative
---

# Topology, isolation, and verification form a causal chain for reliable agent scaling

This KB treats hierarchical decomposition, scope isolation, and error correction as largely independent design concerns — developed in [bounded-context orchestration model](./bounded-context-orchestration-model.md), [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md), and [error correction with above-chance oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) respectively. [Tu (2026)](../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.md) argues they form a causal dependency chain instead: topology creates decomposition boundaries, isolation manufactures verifiable atomic units, verification exploits the structure they produce. If the dependency is real, you cannot "just add verification" to a flat system — you must first have decomposition and isolation in place.

## The dependency argument

**Topology → isolation.** Hierarchical decomposition creates the boundaries that make isolation possible. Without decomposition, everything lives in one context — there are no units to isolate. The [select/call loop](./bounded-context-orchestration-model.md) already builds this step: it decomposes work into bounded calls, each with a [fresh, scoped context](./llm-context-is-composed-without-scoping.md). But the KB frames this as an architectural choice, not a prerequisite for what follows.

**Isolation → verification.** The [error correction framework](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) requires decorrelated checks — the verifier's error modes must differ from the generator's. Isolation plausibly contributes to this (though neither the error correction note nor Tu makes the argument directly): a verifier assessing an isolated unit operates on clean context, so it is less likely to share the generator's biases than one working in the same flat, accumulated state. Without isolation, the [coordination guarantees note](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) predicts contamination — frame-local information remaining globally visible, biasing both generation and verification toward the same errors.

**The combined effect.** Sequential reasoning hits a hard ceiling: success probability decays exponentially with the number of steps, because each step has some probability of error. Tu argues that hierarchical structure bypasses this by reducing sequential depth from linear to logarithmic while distributing total work across parallel branches, with exponential error suppression at each level.

## KB evidence for the chain

Several existing notes contain evidence consistent with the dependency ordering, though none name it explicitly:

- **ConvexBench** ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)): F1 collapses from 1.0 to ≈0.2 at depth 100 under flat accumulation, but recovers to 1.0 when history is pruned to direct dependencies. Under the chain framing, topology was always present (the compositional function structure) and the intervention added isolation — without verification, full performance already recovers. This supports the chain but equally supports the simpler account below.

- **MAKER** ([Meyerson et al., 2025](../sources/meyerson-maker-million-step-llm-zero-errors.md)): Maximal decomposition (m=1) with voting achieves zero errors over 1M steps — under the chain framing, all three mechanisms present. The [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) call this "exploit clean frames recursively."

- **Scheduler-LLM separation** ([seedling](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)): Already develops two-thirds of the chain — symbolic substrates eliminate error for bookkeeping (topology + isolation), leaving semantic error correction for bounded calls. Tu's two-channel failure model (global drift = depth-driven, residual leaf errors = work-driven) offers a different decomposition of the same phenomenon.

- **Kim et al.'s error amplification** ([synthesis is not error correction](./synthesis-is-not-error-correction.md)): 17.2× amplification when agents solve the same task with outputs merged, not voted. Consistent with the chain, but all three mechanisms are absent (no task decomposition, no scoping, synthesis instead of voting), so the evidence cannot isolate which missing mechanism is responsible.

## The simpler account: decomposition with two corollaries

The three mechanisms might reduce to one. If you decompose well enough:

- **Isolation is automatic** — each piece gets its own context by construction. Sub-agents in the [orchestration model](./bounded-context-orchestration-model.md) already receive fresh frames; no separate isolation mechanism is needed.
- **Verification becomes tractable** — small, atomic pieces are easier to check than large, entangled ones. MAKER's voting works precisely because maximal decomposition produces single-answer steps.

Under this account, "topology → isolation → verification" describes the same thing at three levels of abstraction rather than three genuinely independent mechanisms.

## Distinguishing the two framings

The dependency claim makes predictions the simpler account does not:

1. **Decomposition without isolation should fail.** A system that decomposes into sub-tasks but shares mutable state across them (e.g., sub-agents writing to a shared scratchpad) should show verification degrading even though topology is present. The [coordination guarantees note](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) predicts this via contamination, but no KB source demonstrates it experimentally with decomposition held constant.

2. **Isolation without topology should partially succeed.** A flat system with strong scoping conventions (role markers, XML delimiters) but no decomposition should show some verification benefit. If the simpler account is right, this configuration shouldn't exist: you can't have meaningful isolation without decomposition.

3. **Verification without isolation should degrade with scale.** An LLM judge reviewing outputs from a flat, unscoped system should see its discriminative power shrink as context grows, because shared context biases the judge toward the generator's errors. The [content effects evidence](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) already suggests this: content bias is shared across model families and survives scaling. This is the most tractable test — if the dependency claim is right, shared context should measurably degrade judge accuracy; if verification is independent of isolation, it should not.

## Open Questions

- Tu's two-channel failure model (global drift vs. residual leaf errors) and the KB's three-phenomena model (underspecification, indeterminism, bias) in the [scheduler-LLM separation note](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) appear orthogonal. Does one subsume the other, or do they capture different aspects?
- The linear collapse argument assumes independent per-step errors. The KB's [error correction note](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) documents correlated errors extensively (content effects shared across model families). How does the causal chain change under correlated errors?
- Tu notes that "no current approach fully engages all three mechanisms." Is this because full engagement is hard to achieve, or because the mechanisms are not as independent as the chain suggests?
- Does "managerial capacity" — a parent agent's ability to manage children, which limits branching factor — belong in the KB's [decomposition heuristics](./decomposition-heuristics-for-bounded-context-scheduling.md) as an explicit constraint on topology?

---

Sources:

- Tu (2026). [Structured Test-Time Scaling: From Multi-Agent Systems to General Inference Architectures](../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.md) — the causal dependency chain claim this note examines

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the select/call loop provides the topology layer; this note argues topology is the first prerequisite in a dependency chain
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — foundation: sub-agents-as-lexical-frames provides the isolation layer; this note argues isolation is the second prerequisite, dependent on topology
- [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — foundation: the verification layer; this note argues verification depends on isolation to maintain decorrelation
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — extends: the four failure modes map to what goes wrong when elements of the chain are missing
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — extends: Tu's two-channel model provides an alternative decomposition that now supports keeping the note as a seedling rather than a pure speculation
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — exemplifies: "exploit clean frames recursively" implements the topology → isolation step
- [synthesis is not error correction](./synthesis-is-not-error-correction.md) — grounds: the voting/synthesis distinction explains why verification requires atomic units from isolation rather than merged outputs
