---
description: "Conjecture separating available model capability from selection: qualities weakly distinguished by the actual acceptance oracle lose to strongly verified objectives"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, llm-interpretation-errors, evaluation, self-improving-systems]
---

# Weakly discriminated qualities tend to be underselected

When a selection loop judges several qualities with oracles of unequal discriminative power, its accepted outputs improve on whatever the strong oracles distinguish and drift on whatever the weak ones barely distinguish — even when the generator is entirely capable of producing the weakly verified quality. Candidate availability and candidate selection are different bottlenecks.

This is a conjecture about proposal-selection loops, not a claim that every unmeasured quality deteriorates. It predicts a directional selection pressure when three conditions hold:

1. generated candidates vary on more than one quality;
2. acceptance or retention depends more reliably on some qualities than others; and
3. accepted outputs become the starting point, context, or training signal for later iterations.

What acts under those conditions is the **operative oracle** — the check that actually changes which candidates survive, which need not be the rubric a system says it values. A quality can be named prominently in the instructions and still exert almost no selection pressure, if nothing in the loop separates its better instances from its worse ones.

## Oracle asymmetry creates selection asymmetry

Suppose a coding loop selects patches for functional correctness and maintainability. Tests discriminate functional failures quickly: a candidate that breaks behavior is likely to be rejected. Maintainability review is delayed, noisy, or absent: two patches with very different future change costs may be equally likely to pass. Conditional on acceptance, the patch population is therefore enriched for correctness but only weakly enriched for maintainability.

No tradeoff has to be made anywhere for this to happen: nothing sacrifices maintainability in order to pass the tests. Local fixes, duplicated logic, and awkward dependencies survive simply because the acceptance mechanism sees their immediate behavior more clearly than their delayed cost. Each accepted patch then changes the codebase the next task inherits, and repetition converts a per-change blind spot into directional system drift.

The same asymmetry appears in an agent-operated KB: structural validation strongly discriminates broken frontmatter, invalid types, and unresolved links, and weakly discriminates whether a note has explanatory-reach, whether a connection reduces navigation uncertainty, or whether a synthesis captures the right mechanism. A high-throughput authoring loop can therefore converge on artifacts that validate cleanly while their semantic quality degrades, [especially when maintenance does not scale with generation](./entropy-management-must-scale-with-generation-throughput.md).

## Knowledge and selection are different hypotheses

Poor retained output is usually blamed on missing model capability: the model does not know good design, cannot recognize a deep failure, cannot write a coherent theory. That explanation is sufficient but not necessary — three distinct cases predict the same visible failure:

- **Generation failure:** the desired quality is absent from the candidates the model can produce.
- **Activation failure:** the model can produce it, but the task frame does not elicit the relevant knowledge.
- **Selection failure:** good candidates appear, but the operative oracle does not favor them strongly enough to survive.

The distinction matters because the remedies differ: better weights or broader context for generation, explicit perspectives and probes for activation, stronger external checks for selection.

[The Bug That Shipped](../sources/the-bug-that-shipped-2035319413474206122.md) shows two of these cases coming apart. Coding models rarely surfaced deployment failures under generic self-review, yet diagnosed the same failures when directly probed: the knowledge was available and the undirected review simply did not select for it. That does not establish the same mechanism for maintainability, but it does make “the model lacks the knowledge” an inadequate default explanation.

## Maintainability is the motivating case

[Why Software Factories Fail](../sources/why-software-factories-fail-2080697380379427275.md) argues that coding benchmarks strongly reward patches that pass tests while imposing little penalty for design choices whose cost appears through later changes. Its failed lights-off deployment is consistent with oracle asymmetry: immediate correctness remained visible while maintainability debt accumulated across accepted patches.

Part II responds by restoring humans at product, architecture, program-design, and code-review boundaries and by delivering [short vertical slices](../sources/why-software-factories-fail-lights-back-on-2081058573556306030.md). That limits how much work accumulates under a mistaken judgment, but it leaves the diagnosis open — missing knowledge and weak selection both predict the same failed deployment.

Intervention without new weights is the test that separates them. If explicit maintainability probes, pairwise design comparisons, repeated-change evaluations, or repository-specific structural checks reliably select better designs from the same generator, selection was a material bottleneck. If candidates stay poor even under a discriminating maintainability oracle, the better explanation is generation capacity, global codebase comprehension, or the quality definition itself.

## Stronger oracles can be assembled, but not by vote count alone

A weak oracle need not remain weak. Maintainability has multiple partial signals: dependency direction, duplication and complexity trends, change locality, mutation testing, failures on later modification tasks, independent design comparisons, and sampled human judgments. KB semantic quality likewise has partial signals from adversarial review, contradiction checks, use traces, graph structure, and human acceptance.

Combining them helps only when the individual checks have genuine discrimination and sufficiently different failure modes, [since error correction requires above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md); repeating the same model, prompt, and evidence amplifies a shared blind spot rather than quality. A composite oracle therefore needs calibration against later effects — did the code become easier to change, did the note support better decisions, did the connection improve traversal? Proxy agreement without outcome calibration merely constructs a louder proxy.

This reframes human oversight as a source of labels and calibration rather than a permanent architectural constant. Where a composite oracle reaches sufficient discrimination, [warranted autonomy can expand into its domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). Where it does not, removing the human changes actor allocation without warranting the accepted results.

## Predictions

- Strengthening an oracle for one quality should improve that quality among accepted outputs without requiring a weight change, provided the generator already produces usable variation.
- Generic self-review should underperform checks that name distinct failure perspectives when activation is part of the bottleneck.
- Sequential systems should show more drift than isolated tasks because accepted blind spots alter later starting states.
- Increasing generation throughput without proportionally strengthening weak quality checks should widen the gap between strongly and weakly verified qualities.
- Multiple correlated reviewers should plateau, while heterogeneous checks calibrated against delayed outcomes should continue to improve discrimination.

These predictions separate the conjecture from the trivial claim that “what gets measured gets managed.” The proposed mechanism is candidate selection under unequal discrimination, and it can fail in identifiable ways.

## Scope and rival explanations

- The claim requires a selection or retention pathway. In a one-shot call whose output is never compared, accepted, reused, or learned from, “underselection” is the wrong description.
- An oracle cannot select a quality absent from the candidate distribution. Strong verification does not manufacture generator capability.
- Some qualities genuinely conflict. A system may knowingly trade maintainability for latency or semantic nuance for consistency; that is objective weighting, not necessarily oracle weakness.
- Delayed quality can degrade because the model lacks global state, context, or causal understanding. Oracle asymmetry is one mechanism to test against those rivals, not a universal diagnosis.
- Human judgment is not automatically a strong oracle. It can be inconsistent, biased, expensive, or unable to observe delayed effects. Its value must also be established for the target domain.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: verification cost determines which qualities can support warranted automation
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: aggregate generator accuracy cannot replace per-instance discrimination at the acceptance boundary
- [An outcome check licenses replay; a rule needs the process verified](./an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md) — extends: outcome and process checks can strongly verify different qualities of the same candidate
- [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: states the conditions under which multiple weak checks can become a stronger composite oracle
- [Entropy management must scale with generation throughput](./entropy-management-must-scale-with-generation-throughput.md) — exemplifies: inherited weakly checked patterns compound as accepted generation becomes later context
- [Inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — enables: inspectable form supplies evidence a quality oracle can evaluate, without guaranteeing that the evaluator discriminates adequately
- [The Bug That Shipped](../sources/the-bug-that-shipped-2035319413474206122.md) — evidenced-by: explicit failure probes elicited knowledge that undirected self-review rarely surfaced
- [Why Software Factories Fail](../sources/why-software-factories-fail-2080697380379427275.md) — abstracted-from: motivates the maintainability case through benchmark incentives and a failed lights-off deployment
