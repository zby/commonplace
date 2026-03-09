---
description: Ephemeral computation — discarding generated artifacts after use — trades accumulation for simplicity, making it the inverse of crystallisation
type: note
traits: []
areas: [learning-theory]
status: current
---

# Ephemeral computation prevents accumulation

Systems that generate artifacts (code, analyses, plans) face a fork: keep the artifacts or discard them. The choice determines whether the system can learn across runs.

## The fork

**Ephemeral** systems generate an artifact, use it, and discard it. Next time the same problem appears, it's re-derived from scratch. Recursive Language Models (RLMs) work this way — the LLM writes code, the REPL executes it, the result feeds back into the conversation, and the code disappears.

**Accumulating** systems generate an artifact and persist it. The artifact enters version control, becomes available for reuse, and can be tested and reviewed. Each run potentially makes the next run easier.

```
Ephemeral:     generate → execute → discard
Accumulating:  generate → execute → save → test → version → reuse
```

## What ephemerality buys

Discarding artifacts after use, combined with restricting them to pure computation (no side effects), buys significant simplicity:

- **No approval problem.** Artifacts that can only compute and return values need no gating. Persistent artifacts that modify the world need review and trust.
- **No state management.** Each run is a clean slate. No lifecycle hooks, no resource cleanup, no accumulated dependencies.
- **No maintenance burden.** Artifacts that don't exist can't go stale, break, or accumulate technical debt.

The constraint limits what the system can do — it can't build on previous work, call APIs with lasting effects, or modify shared state. For analytical workloads (data analysis, computation, one-off queries) this is fine. For systems that need to improve over time, it's a ceiling.

## What ephemerality costs

Every pattern the system discovers must be rediscovered on the next run:

- **No learning across runs.** A good decomposition strategy is lost the moment the session ends. The system cannot get better at recurring problems.
- **No testing.** You can't write a test for an artifact that doesn't exist between runs. Correctness is verified per-execution or not at all.
- **No review.** There is no artifact for a human to inspect, approve, or improve.
- **No reuse.** Two users with the same question trigger two independent generations.

## Ephemerality as anti-crystallisation

[Crystallisation](./deploy-time-learning-the-missing-middle.md) converts stochastic LLM behavior into deterministic, testable artifacts — each step [trading generality for reliability, speed, and cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). Ephemeral computation is the deliberate refusal to crystallise. It stays permanently in the stochastic regime, re-deriving solutions each time.

This positions ephemerality and crystallisation as endpoints on a spectrum. Most practical systems sit somewhere between: some artifacts are persisted and hardened, others are generated fresh each time. The [crystallisation-softening dynamic](./crystallisation-and-softening-navigate-the-bitter-lesson-boundary.md) is about where to place each component on this spectrum — and being willing to move components in either direction as understanding changes.

## The question each system answers

**Ephemeral systems ask:** How do I solve this problem right now, as simply as possible?

**Accumulating systems ask:** How do I solve this problem in a way that makes the next problem easier?

The answer to the first is disposable computation. The answer to the second is versioned artifacts.

---

Relevant Notes:

- [Crystallisation and softening navigate the bitter lesson boundary](./crystallisation-and-softening-navigate-the-bitter-lesson-boundary.md) — the dynamic that moves components between ephemeral and crystallised
- [Deploy-time learning is the missing middle](./deploy-time-learning-the-missing-middle.md) — crystallisation's verifiability gradient
- [Stabilisation and distillation both trade generality for reliability, speed, and cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the trade-off crystallisation enacts

Topics:

- [learning-theory](./learning-theory.md)
