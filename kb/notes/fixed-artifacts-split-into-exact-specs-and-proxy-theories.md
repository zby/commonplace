---
description: "Exactness relates an artifact to its requirement; proxyhood relates the requirement to the objective above. Chains end in an adopted commitment or a conjectured decomposition; a failed proxy theory is rescoped to its requirement, not discarded"
type: kb/types/note.md
traits: []
tags: [learning-theory, constraining]
---

# Fixed artifacts split into exact specs and proxy theories

A fixed artifact can be perfectly correct relative to its own specification and still be wrong for the system-level problem. The failure mode is treating proxy theories as if they were exact specs.

The split is real, but it does not attach to the artifact in isolation. Exactness is a relation: artifact A implements requirement R exactly, while R may itself be a proxy for an objective O above it. Read as kinds of artifact, the split invites an immunization move: any hand-built component can be redescribed narrowly enough to count as "an exact implementation of the behavior we specified," which does not answer the proxy question but displaces it one level up. The classification therefore has to climb the chain, and "exact-spec artifact" is shorthand for an artifact whose requirement chain holds up when climbed.

**Exact-spec artifacts** implement problems where the spec *is* the problem. Arithmetic, sorting, schema validation, fiscal-period normalization, and legal move generation in chess all work this way once the intended variant, input encoding, and output contract are fixed. **Proxy-theory artifacts** implement precise specifications that only approximate a larger capability. Vision features such as SIFT, Haar cascades, and Canny edge detection had mathematical formulations and useful invariants — scale invariance, rotation invariance, formal optimality criteria. They were exact solutions to their own specs. The problem was treating "detect edges" as a sufficient decomposition of seeing: a theory about what seeing requires, not a definition of seeing itself.

## The chain terminates in a commitment or a conjecture

What makes the two cases feel like different kinds of artifact is a real difference, but it lives at the top of the requirement chain, in how the chain ends.

Some chains end in a **commitment**: a requirement someone adopted, which [creates its own ground truth](./commitment-not-derivation-creates-new-ground-truth.md). The specification of multiplication is multiplication because the practice defined it; a schema is the contract because the project adopted it; chess move generation is exact because the rules are constitutive of the game. A commitment does not end the chain so much as change the question's character. Below it sits correctness, checkable against the adopted requirement. Above it sits the choice — whether adopting this requirement serves the objective — which is a further link, itself a commitment or a conjecture. What the commitment supplies is a firm floor for the levels beneath and an explicit address for the contest above.

Other chains pass through a **conjecture**: a requirement posited as a component of a capability nobody defined. "Detect edges" was a theory about what seeing requires; the conjectured link — that edge maps and keypoints compose into seeing — carried the whole reach claim, was never separately testable, and is the thing that failed.

The two terminations behave differently under pressure because they answer to different oracles. A conjectured link can be tested to the extent the objective above it can be checked. Chess strategy heuristics — control the center, develop early — are conjectured decompositions of good play, but winning is exactly checkable, so the conjecture is continually exposed to refutation and can earn scope. NP-hard optimization has the same shape: feasibility and objective value are exactly checkable, while the policies for finding good candidates remain conjectures running under that check. Seeing had no such oracle; the edge-detection link could only fail at composition time, all at once. [Oracle strength](./oracle-strength-spectrum.md) above the link, not precision inside the artifact, sets how safely a conjectured requirement can be hardened. Quantitative cases sharpen the boundary from both sides: MAKER reports zero errors across a 1,048,575-step Towers of Hanoi execution by decomposing to single-step decisions with hard per-step oracles, and SuperARC shows purpose-built algorithmic machinery scoring 1.000 where frontier LLMs score 0.007–0.042 on an AIT-grounded compression benchmark — fixed machinery helps when the formalism captures the target capability, not whenever an artifact is precise.

## Condemn the link, keep the artifact

Read relationally, the vision story condemns less than it seems to. Edge detection is very far from what anyone wanted from vision in general — and it remains exact relative to its own requirement, and useful wherever that requirement is genuinely the objective: document deskewing, industrial inspection, a scoped pipeline that literally needs edges. What failed was one conjectured link with enormous claimed scope, [exactly the unearned reach that scale selects against](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md); the machinery under the link was never refuted. So the verdict on a failed proxy theory is rescoping, not disposal: the artifact drops from "component of the capability" to "solution to its own requirement, applicable where that requirement is wanted." A proxy theory that survives this demotion is smaller, not wrong.

## Composition failure is the strongest tell

Identifying where a chain's weak link sits can be hard. Exact specs are easiest to recognize when the target was formal from the start; many useful artifacts instead emerge as attempts to make an underspecified capability more tractable, and arrive without that clarity.

Composition failure is the strongest warning signal, because composition is the first event that tests the conjectured links rather than the artifacts. Local correctness lives on the artifact–requirement link; system-level wrongness lives on the links above it. That is why individually sound components can fail to compose into the larger capability — the vision features all captured something real — and why composition testing stays mandatory even when every component is provably correct against its spec. Proxy-theory artifacts often fail only after integration, when their assumptions meet the capability they were meant to support.

## Confidence signals

None of these signals is decisive. They shift confidence:

| Signal | Raises "exact spec" confidence | Raises "proxy theory" confidence |
|--------|-------------------------------|-----------------------------------|
| **Is correctness fully specifiable?** | Spec IS the problem (multiplication, sorting) | Spec approximates the problem (edge detection, sentiment) |
| **How is output verified?** | Validity checkable without judgment, even if many outputs are acceptable | Verification requires human evaluation or proxy scores |
| **Are failures local or compositional?** | Bugs sit in individual components; fixing them fixes the system | Components work in isolation but don't compose into the target capability |

The practical posture is provisional codification. Codify commitments aggressively. Codify conjectured links when they provide current leverage and the objective above them can check them, keeping the artifacts inspectable, tested, and easy to relax — and when a conjectured link fails at composition, rescope the artifact to the requirement it does satisfy rather than discarding the machinery. [Spec mining](./spec-mining-as-codification.md) improves the odds by extracting candidate specs from working behavior rather than inventing decompositions upfront; [operational relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) help detect when a conjectured link is failing.

---

Relevant Notes:

- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — parent frame: handworked artifact evolution is provisional, but durable artifact evolution is better than forgetting; cites the arithmetic regime as permanent-advantage codification
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: why an adopted requirement terminates the falsifiability question at its level — a commitment adds a resolution no source determines
- [The bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — extends: what scale does to a conjectured link whose claimed scope was never tested, and why the machinery under the link is not what gets eaten
- [Spec mining as codification](./spec-mining-as-codification.md) — method: starts from working behavior to discover candidate exact specs instead of guessing decompositions upfront
- [Operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — applies: gives earlier signals for detecting badly fitting conjectured links before full composition failure
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — refines: oracle strength above a link determines how cheaply it can be tested and how safely the artifact under it can be hardened
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: memory operations are exact-spec artifacts, while the policy for composing them is a proxy theory
- [Fintool: Lessons from Financial Services](https://x.com/nicbstme/status/2015174818497437834) — exemplifies: fiscal period normalization is a clean exact-spec artifact inside an otherwise judgment-heavy domain
- [MAKER: million-step zero errors](https://arxiv.org/abs/2511.09030) — exemplifies: decomposition to minimal subtasks with hard per-step oracles works when each subtask has exact-spec structure
- [SuperARC AIT benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — exemplifies: purpose-built algorithmic machinery succeeds when recursive compression is specified and hard-oracle verified
