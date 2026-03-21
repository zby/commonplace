---
description: "Operationalizes codification by extracting deterministic verifiers from observed stochastic behavior — the mechanism that converts blurry-zone components into calculators"
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: current
---

# Spec mining is codification's operational mechanism

[Codification](./codification.md) says knowledge hardens into repo artifacts — tests, specs, conventions. But where do those artifacts come from? One answer: you mine them from observed behavior.

## The pattern

1. Watch the system do tasks (or watch humans do tasks the system will do).
2. Identify repeated micro-actions: parsing dates, normalising names, mapping intents to actions, detecting escalation triggers.
3. Extract those regularities into deterministic artifacts: functions, schema rules, unit tests, checkers.
4. Re-run with these constraints in place. The system becomes more reliable without weight updates.

This is codification as compilation: the system distills stochastic regularities into deterministic code. The output is an [inspectable substrate](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — reviewable, testable, revertable artifacts rather than opaque weight updates. Inspectability is what makes mined specs falsifiable: you can test them under distribution shift and relax them back if they break.

The same pattern appears at the methodology level: the [maturation trajectory from instruction to script](./methodology-enforcement-is-constraining.md) is spec mining applied to methodology rather than system behavior. The codification trigger ("a pattern has emerged from repeated execution") is the same observation step.

## Why this matters for the bitter lesson boundary

The [bitter lesson boundary](./bitter-lesson-boundary.md) says calculators survive scaling because the spec *is* the problem. Spec mining manufactures new calculators by discovering specs that were implicit in behavior. Each mined spec converts a piece of the blurry zone into the calculator regime.

This connects to the [oracle strength spectrum](./oracle-strength-spectrum.md): spec mining moves components from soft/delayed oracle toward hard oracle. A pattern that was only checkable by "does the output look right?" becomes checkable by "does this match the extracted rule?" Each mined spec is also a new oracle that [error correction can amplify through decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the progression is: mine a spec (create an oracle with TPR > FPR), then amplify through decorrelated repetition. This design philosophy — out-evaluate, not out-implement — is what the [cybernetics thread](../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) calls "externalizing system-specific judgment."

## Concrete workflow

For an agentic system:
1. Cluster failure modes from production logs.
2. For the top clusters, ask: is there a deterministic rule that would have caught this?
3. If yes → write a verifier or deterministic helper (codify).
4. If no → the failure mode stays in the learned regime, but you now have a regression test (partial codification).
5. Repeat. The calculator surface grows monotonically.

The Codex team's report on runtime engineering ([Lopopolo, 2026](../sources/harness-engineering-leveraging-codex-agent-first-world.md)) documents this workflow at production scale. Early on, 20% of engineering time (Fridays) went to manually cleaning "AI slop" — observing failure patterns. The team then codified those observations into structural tests and linter rules whose error messages teach the fix, and finally automated the observation step itself with background cleanup agents that scan for drift and open refactoring PRs. The progression — manual observation, extracted rules, automated monitoring — is the spec mining loop completing.

## Risks

- Mining specs from observed behavior can encode biases or accidents as rules. The mined spec might be a "vision feature" — a plausible theory that scale will eventually outperform.
- Mitigation: mined specs should be falsifiable. If they break under distribution shift or metamorphic testing, they're candidates for [relaxing](./operational-signals-that-a-component-is-a-relaxing-candidate.md), not permanent codification. The relaxing-signals note identifies the specific indicators (paraphrase sensitivity, distribution-shift brittleness) that reveal a mined spec was a vision feature, not a calculator.

## Open questions

- What's the right threshold for codifying a mined pattern? Too early and you lock in a vision feature; too late and you miss easy reliability wins.
- Can spec mining be automated? LLMs could propose candidate rules from failure clusters, then validation suites confirm or reject them. The [automating KB learning](./automating-kb-learning-is-an-open-problem.md) note explores a related version: the "boiling cauldron" mutations (extract, relink, synthesise) are spec mining applied to knowledge structure rather than system behavior.

---

Sources:
- Lopopolo (2026). [Harness engineering: leveraging Codex in an agent-first world](../sources/harness-engineering-leveraging-codex-agent-first-world.md) — production-scale spec mining: manual failure observation → structural tests → automated cleanup agents.

Relevant Notes:

- [deploy-time-learning](./deploy-time-learning-the-missing-middle.md) — foundation: codification says knowledge hardens into repo artifacts; spec mining is the mechanism that produces those artifacts from observed behavior
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) — motivation: spec mining manufactures new calculators by converting implicit specs from the blurry zone into the calculator regime
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — mechanism: spec mining moves components from soft/delayed oracle toward hard oracle; each mined spec is a new verification target
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — amplification: mined specs create oracles with TPR > FPR that error correction can then boost through decorrelated repetition
- [evaluation-automation-is-phase-gated-by-comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — exemplifies: evaluation tuning requires manual failure analysis and judge calibration before optimization loops can safely amplify
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — risk mitigation: relaxing signals detect when a mined spec encodes an accidental regularity rather than a genuine spec
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — parallels: the maturation trajectory (instruction → script) is spec mining applied to methodology rather than system behavior
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — enables: mined specs produce inspectable, testable, revertable artifacts — inspectability is what makes them falsifiable
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallels: case law constraining (courts converging on one reading of a statute) is spec mining in a legal medium
- [specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — situates: spec mining is the late-phase strategy for rules that only become legible after repeated execution
