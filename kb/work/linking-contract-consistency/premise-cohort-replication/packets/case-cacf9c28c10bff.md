# Case packet

Neutral case identifier: case-cacf9c28c10bff

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Evaluation automation is phase-gated by comprehension

When an evaluation loop improves score without improving real behavior, the failure is often not weak search but an objective grounded too weakly in observed failure. Evaluation automation in practice follows a characteristic sequence: **comprehension first, specification second, generalization third**.

Comprehension is the first gate because it supplies the observations that specification turns into verifiers. Before automation can improve output quality, the system needs direct evidence of real failures, a way to identify concrete failure modes, and a route for turning those failures into discriminative judges.

## The three phases

1. **Comprehension**: Read outputs directly, observe where and why the system fails, build non-theoretical intuition for failure patterns.
2. **Specification**: Convert observations into a failure taxonomy and evaluators, then calibrate those evaluators against manually labeled examples.
3. **Generalization**: Run automated optimization against calibrated evaluators with broader input coverage.

This sequencing matches a practitioner pattern described in one detailed field report: auto-generated tests and judges produced early score gains, then degraded real quality exposed that the objective was wrong. The loop functioned correctly; the objective did not.

## Why this is a gate, not a style preference

Skipping comprehension leaves specification unconstrained by observed reality. Skipping specification leaves optimization unconstrained by discriminative checks. Both cases amplify proxy quality rather than task quality.

This is why "more automation" cannot reliably substitute for the early verifier-construction work in cold-start or subjective domains. Automation can help once failure patterns and judges exist, but it cannot safely assume them from zero context.

Meta-Harness shows the important boundary condition. In hard-oracle domains, rich diagnostic access can automate part of comprehension: the proposer can inspect raw execution traces, prior harness code, and scores to infer why candidates failed before writing the next candidate. The phase gate is not "a human must always understand first." It is "optimization needs enough diagnostic access to form a causal failure model before it generalizes." Scores alone do not supply that model, and Meta-Harness's ablation suggests summaries may not preserve it either.

## Scope limits

- In hard-oracle domains (compilers, strict schemas, deterministic tests), comprehension can be shorter or partly automated when the proposer has rich diagnostic traces, not just scalar scores.
- In soft-oracle domains (writing quality, strategic reasoning, product judgment), comprehension is load-bearing and usually human-led.
- This claim applies to early and mid-stage system tuning. Mature systems may partially automate parts of comprehension, but only after prior manual cycles have stabilized the taxonomy.

## Practical implication

Evaluation pipelines should enforce explicit verifier-construction stage gates before optimization:

1. Output-read pass completed on diverse inputs
2. Failure taxonomy written from observed failures
3. Judges calibrated on a hand-scored mini set

Without these gates, score improvements are weak evidence of capability improvement.

---

Relevant Notes:

- [oracle-strength-spectrum] — frames (provisional — target is speculative): the three phases can be read as a local oracle-hardening sequence before heavy automation

## Artifact B

# Spec mining is codification's operational mechanism

[Codification] says knowledge hardens into repo artifacts — tests, specs, conventions. But where do those artifacts come from? One answer: you mine them from observed behavior.

## The pattern

1. Watch the system do tasks (or watch humans do tasks the system will do).
2. Identify repeated micro-actions: parsing dates, normalising names, mapping intents to actions, detecting escalation triggers.
3. Extract those regularities into deterministic artifacts: functions, schema rules, unit tests, checkers.
4. Re-run with these constraints in place. The system becomes more reliable without weight updates.

This is codification as compilation: the system mines stochastic regularities and codifies them into deterministic code. The output is an [inspectable artifact] — reviewable, testable, revertable artifacts rather than opaque weight updates. Inspectability is what makes mined specs falsifiable: you can test them under distribution shift and relax them back if they break.

The same pattern appears at the methodology level: the [maturation trajectory from instruction to script] is spec mining applied to methodology rather than system behavior. The codification trigger ("a pattern has emerged from repeated execution") is the same observation step.

## Why this matters for exact specs

The [fixed-artifact distinction] says exact-spec artifacts are safest when the spec *is* the problem. Spec mining manufactures new exact-spec artifacts by discovering specs that were implicit in behavior. Each mined spec converts a piece of the blurry zone into a harder verification target.

This connects to the [oracle strength spectrum]: spec mining moves components from soft/delayed oracle toward hard oracle. A pattern that was only checkable by "does the output look right?" becomes checkable by "does this match the extracted rule?" Each mined spec is also a new oracle that [error correction can amplify through decorrelated checks] — the progression is: mine a spec (create an oracle with TPR > FPR), then amplify through decorrelated repetition. This design philosophy — out-evaluate, not out-implement — is what the [cybernetics thread] calls "externalizing system-specific judgment."

## Concrete workflow

For an agentic system:
1. Cluster failure modes from production logs.
2. For the top clusters, ask: is there a deterministic rule that would have caught this?
3. If yes → write a verifier or deterministic helper (codify).
4. If no → the failure mode stays in the learned regime, but you now have a regression test (partial codification).
5. Repeat. The calculator surface grows monotonically.

The Codex team's report on runtime engineering ([Lopopolo, 2026]) documents this workflow at production scale. Early on, 20% of engineering time (Fridays) went to manually cleaning "AI slop" — observing failure patterns. The team then codified those observations into structural tests and linter rules whose error messages teach the fix, and finally automated the observation step itself with background cleanup agents that scan for drift and open refactoring PRs. The progression — manual observation, extracted rules, automated monitoring — is the spec mining loop completing.

## Risks

- Mining specs from observed behavior can encode biases or accidents as rules. The mined spec might be a proxy theory rather than an exact spec.
- Mitigation: mined specs should be falsifiable. If they break under distribution shift or metamorphic testing, they're candidates for [relaxing], not permanent codification. The relaxing-signals note identifies the specific indicators (paraphrase sensitivity, distribution-shift brittleness) that reveal a mined spec was an accidental proxy theory, not an exact spec.

## Open questions

- What's the right threshold for codifying a mined pattern? Too early and you lock in a proxy theory; too late and you miss easy reliability wins.
- Can spec mining be automated? LLMs could propose candidate rules from failure clusters, then validation suites confirm or reject them. The [automating KB learning] note explores a related version: the "boiling cauldron" mutations (extract, relink, synthesise) are spec mining applied to knowledge structure rather than system behavior.

---

Sources:
- Lopopolo (2026). [Harness engineering: leveraging Codex in an agent-first world] — production-scale spec mining: manual failure observation → structural tests → automated cleanup agents.

Relevant Notes:

- [operational-signals-that-a-component-is-a-relaxing-candidate] — risk mitigation: relaxing signals detect when a mined spec encodes an accidental regularity rather than a genuine spec

## Under-review context phrase

converting observed failures into reusable evaluators is spec mining
