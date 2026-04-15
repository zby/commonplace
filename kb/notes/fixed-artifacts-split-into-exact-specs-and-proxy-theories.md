---
description: Fixed artifacts are safe when their spec fully captures the problem; they are risky when they encode proxy theories whose components may not compose into the larger capability
type: note
traits: []
tags: [learning-theory]
status: current
---

# Fixed artifacts split into exact specs and proxy theories

A fixed artifact can be perfectly correct relative to its own specification and still be wrong for the system-level problem. The failure mode is treating proxy theories as if they were exact specs.

**Exact-spec artifacts** implement problems where the spec *is* the problem. Arithmetic, sorting, schema validation, fiscal-period normalization, and legal move generation in chess all work this way. The specification of multiplication is multiplication; there is no separate target capability hiding behind it. If the implementation satisfies the spec, it has solved the problem.

**Proxy-theory artifacts** implement precise specifications that only approximate a larger capability. Vision features such as SIFT, Haar cascades, and Canny edge detection had mathematical formulations and useful invariants — scale invariance, rotation invariance, formal optimality criteria. They were exact solutions to their own specs. The problem was that "detect edges" was a theory about what seeing requires, not a definition of seeing itself. The artifacts met their local specs, but the local specs did not compose into the target capability.

Both kinds can be narrow, domain-specific, and human-engineered. The relevant difference is not scope — it is whether the specification fully captures the problem or approximates it.

## The split can live inside one system

**Chess** has both kinds at once. The rules — legal moves, win conditions, board state — are fully specified, so move generation is an exact-spec artifact. Strategy is different: controlling the center, developing pieces early, and protecting king safety are theories about good play, not definitions of it. The rules survive as exact machinery; the strategic heuristics remain proxy theories that should be revised when better evidence appears.

NP-hard optimization has the same shape. The objective and constraints can be fully specified, so any candidate solution can be checked. But policies for *finding* good candidates are often proxy theories — search heuristics, decompositions, and priority rules that may fail under distribution shift or composition pressure.

## Composition failure is the strongest tell

Identifying which side an artifact sits on can be hard. Exact specs are easiest to recognize when the target was formal from the start; many useful artifacts instead emerge as attempts to make an underspecified capability more tractable, and arrive without that clarity.

Composition failure is the strongest warning signal. The vision features were genuinely useful in isolation — edges, corners, and scale-invariant keypoints all captured something real. The failure was that the pieces did not add up to seeing. When individually sound components fail to compose into the larger capability, their specs are probably proxy theories rather than definitions.

Local correctness can hide system-level wrongness. Proxy-theory artifacts often fail only after integration, when their assumptions meet the larger capability they were meant to support.

## Confidence signals

None of these signals is decisive. They shift confidence:

| Signal | Raises "exact spec" confidence | Raises "proxy theory" confidence |
|--------|-------------------------------|-----------------------------------|
| **Is correctness fully specifiable?** | Spec IS the problem (multiplication, sorting) | Spec approximates the problem (edge detection, sentiment) |
| **How is output verified?** | Single correct answer, checkable without judgment | Verification requires human evaluation or proxy scores |
| **Are failures local or compositional?** | Bugs sit in individual components; fixing them fixes the system | Components work in isolation but don't compose into the target capability |

The practical posture is provisional codification. Codify exact specs aggressively. Codify proxy theories when they provide current leverage, but keep them inspectable, tested, and easy to relax. [Spec mining](./spec-mining-as-codification.md) improves the odds by extracting candidate specs from working behavior rather than inventing decompositions upfront; [operational relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) help detect when a proxy theory is failing.

---

Relevant Notes:

- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — parent frame: handworked artifact evolution is provisional, but durable substrate evolution is better than forgetting
- [Spec mining as codification](./spec-mining-as-codification.md) — method: starts from working behavior to discover candidate exact specs instead of guessing decompositions upfront
- [Operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — applies: gives earlier signals for detecting badly fitting proxy theories before full composition failure
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — refines: oracle strength determines how cheaply exactness can be checked and how safely an artifact can be hardened
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: memory operations are exact-spec artifacts, while the policy for composing them is a proxy theory
- [Fintool: Lessons from Financial Services](../sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md) — exemplifies: fiscal period normalization is a clean exact-spec artifact inside an otherwise judgment-heavy domain
- [MAKER: million-step zero errors](../sources/meyerson-maker-million-step-llm-zero-errors.md) — exemplifies: decomposition to minimal subtasks with hard per-step oracles works when each subtask has exact-spec structure
