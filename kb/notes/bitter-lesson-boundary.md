---
description: The bitter lesson has a boundary — calculators vs vision features illustrate when exact solutions survive scaling and when they don't
type: structured-claim
traits: []
areas: [learning-theory]
status: current
---

# The bitter lesson stops at calculators

The [bitter lesson](../sources/wikipedia-bitter-lesson.md) says general methods leveraging computation beat hand-crafted domain knowledge. It is the dominant strategic frame in AI right now — which makes its limits consequential, not academic. Misapplying it in one direction means over-investing in hand-crafted solutions that scale will eat. Misapplying it in the other means dismissing exact solutions that scale can't replace, building unreliable systems where reliable ones were available.

The bitter lesson does have a boundary. Both calculators and hand-crafted vision features are narrow, domain-specific, human-engineered solutions. The bitter lesson predicts both should lose to general methods plus scale. Only one did.

## Evidence

### Specs that are the problem vs. theories about the problem

**Vision features** (SIFT, Haar cascades, Canny edge detection) had mathematical formulations and provable properties — scale invariance, rotation invariance, formal optimality criteria. They looked like exact solutions. But they were exact solutions to the wrong specifications. "Detect edges" was a human theory of what seeing requires, not a definition of seeing itself. The algorithms perfectly met their specs, but the specs were approximations of the real problem. Scale revealed this: learned features, which never committed to a theory of seeing, worked better.

**Calculators** (arithmetic, sorting, cryptography) implement algorithms for formally specified problems. The specification of multiplication IS multiplication — there is no gap between spec and problem, nothing left for a general method to discover. It's irrational to bet on emergent reliability via scale when deterministic code gives you perfect correctness at near-zero cost.

Both are narrow. Both are human-engineered. The difference isn't scope — it's whether the specification fully captures the problem.

### In practice, the boundary is a working heuristic

The boundary between calculators and vision features is real, but identifying which side you're on is not. Calculators are the easy case: we know exactly what we want, and we've known since the start. But most practical solutions don't arrive with that clarity. The transistor wasn't obviously practical. Neither was the Fourier transform, or public-key cryptography before the internet. Practicality emerged from composition, not from any single step. You can't use "is this obviously practical?" as a reliable test.

The vision researchers faced exactly this. Each individual feature — edge detection, corner detection, scale-invariant keypoints — was genuinely useful in isolation. The failure was in composition: the pieces didn't add up to "seeing." But that failure was only visible in retrospect, after learned representations demonstrated a better path. **Composition failure is the tell** — when individually sound components don't compose into the larger capability, the specs are probably theories, not definitions.

## Reasoning

### Crystallisation and softening

[Crystallisation](./deploy-time-learning-the-missing-middle.md) encodes knowledge into repo artifacts — tests, specs, conventions — each at a different grade of verifiability. Each crystallisation step [trades generality for compound gains in reliability, speed, and cost](./learning-is-capacity-change.md). But every such artifact also encodes a decomposition of some larger problem, and the calculator/vision-feature boundary determines whether that trade-off is real:

- **Calculator decompositions**: the spec fully captures the subproblem, so crystallisation is pure gain — reliability+speed+cost improve and there's no generality loss, because the spec exhausts the problem space. There's nothing for a general method to discover.
- **Vision-feature decompositions**: the spec is a plausible theory, so crystallisation involves the real trade-off — you gain the compound but lose generality. When scale makes the general approach good enough on reliability+speed+cost, the generality loss isn't worth it anymore.

Since you can't reliably tell which regime you're in until scale tests the distinction, practical systems will always be hybrids — part crystallised, part learned.

Crystallisation therefore has a complement: **softening**. Where crystallisation trades generality for the reliability+speed+cost compound, softening is the reverse: replacing a crystallised component with a learned or general-purpose one when scale makes that viable — accepting higher cost and lower reliability in exchange for regaining generality. The bitter lesson describes a trajectory, not a law of nature — and the trajectory runs in both directions. Edge detection was crystallised (hand-coded algorithms), softened (replaced by learned features), and may re-crystallise at a different level of the stack (as an accelerator inside a learned architecture). FlashAttention is hand-crafted algorithmic optimization inside learned architectures; tokenizers are engineered preprocessing that learned models depend on. Approaches that get bitter-lessoned away at one level sometimes reappear embedded within the general method at another.

Working heuristics for a hybrid system:

1. **Crystallise for current leverage, not permanence.** A test that checks "does this function return the right number" is probably a calculator. A convention that says "always decompose agents into these three phases" is probably a vision feature. Crystallise both — but expect the second kind to eventually soften.

2. **Prefer specs that describe what over how.** The more a crystallised artifact encodes a theory of how something works (rather than what it should produce), the more likely it is a softening candidate. "This endpoint returns X given Y" survives longer than "always process requests in three stages."

3. **Watch for composition failure as a softening signal.** If crystallised conventions don't compose into better systems, that's the signal to soften — replace the rigid decomposition with a learned one.

## Caveats

- **The boundary is real but hard to identify in advance.** You often can't tell which side you're on until scale tests the distinction. The confidence signals below shift your confidence but none are decisive.
- **Composition failure is only visible in retrospect.** The vision researchers' individual features were genuinely useful in isolation; the failure to compose into "seeing" was only clear after learned representations demonstrated a better path.
- **The trajectory runs in both directions.** Approaches that get bitter-lessoned away at one level sometimes reappear embedded within the general method at another (FlashAttention, tokenizers).

### Confidence signals: calculator or vision feature?

| Signal | Raises "calculator" confidence | Raises "vision feature" confidence |
|--------|-------------------------------|-----------------------------------|
| **Is correctness fully specifiable?** | Spec IS the problem (multiplication, sorting) | Spec approximates the problem (edge detection, sentiment) |
| **Is the spec a definition or a proxy metric?** | Output has a single correct answer verifiable without judgment | Verification requires human evaluation or proxy scores |
| **Are failures local or compositional?** | Bugs are in individual components; fixing them fixes the system | Components work in isolation but don't compose into the target capability |

Topics:
- [learning-theory](./learning-theory.md)
