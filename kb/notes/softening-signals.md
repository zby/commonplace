# Operational signals that a component is a softening candidate

The [bitter lesson boundary](./bitter-lesson-boundary.md) says some crystallised components are calculators (spec is the problem) and others are vision features (spec is a theory). The note offers heuristics ("prefer what over how"), but doesn't give testable signals for detecting vision-feature components in a running system.

## Signals that a component encodes theory, not specification

**Brittleness under paraphrase or reordering.** If the component breaks when inputs are rephrased, reordered, or padded with irrelevant content, it's relying on surface patterns rather than capturing the underlying structure. Metamorphic tests can detect this systematically. Rabanser et al.'s [agent reliability study](../sources/towards-a-science-of-ai-agent-reliability.md) operationalises this signal as the R_prompt metric and finds it is the key differentiator among robustness dimensions: models handle genuine faults gracefully yet remain vulnerable to surface-level instruction rephrasings — empirical confirmation at scale that paraphrase brittleness detects vision-feature components.

**Isolation-vs-integration gap.** The component performs well on unit tests but fails in integration. This was exactly the vision-features pattern: each feature (edge detection, corner detection) worked in isolation, but they didn't compose into "seeing." A growing gap between unit and integration performance is a softening signal.

**Process constraints rather than outcome constraints.** The component encodes "always do steps A, B, C" rather than "output must satisfy property X." Process constraints are theories about how to achieve an outcome; outcome constraints are closer to specifications. The more process-heavy, the more likely it's a softening candidate.

**Hard to specify failure conditions.** If you can't articulate what a failure of this component would look like *before* seeing one, the spec is probably a theory. Calculator failures are obvious (wrong number); vision-feature failures are only obvious in retrospect.

**High sensitivity to distribution shift.** If the component works on training/development data but degrades on slightly different inputs, it has overfit to a particular theory of what inputs look like.

## Using the signals

These aren't binary tests. They're indicators that shift your confidence about where a component sits on the [oracle strength spectrum](./oracle-strength-spectrum.md).

When signals fire:
- Keep the component in a **replaceable slot** — clean interface, swappable implementation.
- Invest in **integration tests** over unit tests for this component.
- Maintain **alternative candidates** (different decompositions, learned replacements) so softening is cheap when the time comes.
- Monitor for **composition failure** — the strongest signal that the underlying theory is wrong.

When signals don't fire:
- The component is likely in the calculator regime. Crystallise harder — more tests, stricter contracts, deterministic implementation where possible.

## Open questions

- Can these signals be measured automatically, or do they require human judgment? Brittleness and distribution sensitivity seem measurable; "hard to specify failure" seems inherently subjective.
- Is there a feedback loop? Investing in integration tests for suspected vision-features might *itself* reveal whether the theory is wrong, accelerating the softening decision.
