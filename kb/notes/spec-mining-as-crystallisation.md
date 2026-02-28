# Spec mining is crystallisation's operational mechanism

[Crystallisation](./deploy-time-learning-the-missing-middle.md) says knowledge hardens into repo artifacts — tests, specs, conventions. But where do those artifacts come from? One answer: you mine them from observed behavior.

## The pattern

1. Watch the system do tasks (or watch humans do tasks the system will do).
2. Identify repeated micro-actions: parsing dates, normalising names, mapping intents to actions, detecting escalation triggers.
3. Extract those regularities into deterministic artifacts: functions, schema rules, unit tests, checkers.
4. Re-run with these constraints in place. The system becomes more reliable without weight updates.

This is crystallisation as compilation: the system distills stochastic regularities into deterministic code.

## Why this matters for the bitter lesson boundary

The [bitter lesson boundary](./bitter-lesson-boundary.md) says calculators survive scaling because the spec *is* the problem. Spec mining manufactures new calculators by discovering specs that were implicit in behavior. Each mined spec converts a piece of the blurry zone into the calculator regime.

This connects to the [oracle strength spectrum](./oracle-strength-spectrum.md): spec mining moves components from soft/delayed oracle toward hard oracle. A pattern that was only checkable by "does the output look right?" becomes checkable by "does this match the extracted rule?"

## Concrete workflow

For an agentic system:
1. Cluster failure modes from production logs.
2. For the top clusters, ask: is there a deterministic rule that would have caught this?
3. If yes → write a verifier or deterministic helper (crystallise).
4. If no → the failure mode stays in the learned regime, but you now have a regression test (partial crystallisation).
5. Repeat. The calculator surface grows monotonically.

## Risks

- Mining specs from observed behavior can encode biases or accidents as rules. The mined spec might be a "vision feature" — a plausible theory that scale will eventually outperform.
- Mitigation: mined specs should be falsifiable. If they break under distribution shift or metamorphic testing, they're candidates for softening, not permanent crystallisation.

## Open questions

- What's the right threshold for crystallising a mined pattern? Too early and you lock in a vision feature; too late and you miss easy reliability wins.
- Can spec mining be automated? LLMs could propose candidate rules from failure clusters, then validation suites confirm or reject them.
