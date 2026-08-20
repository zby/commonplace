---
description: "Statistical conjecture: under named proposal-selection conditions, unequal oracle discrimination yields unequal enrichment; absolute degradation needs an additional directional mechanism"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, llm-reliability, evaluation, self-improving-systems]
---

# Weakly discriminated qualities tend to be underselected

Underselection means less enrichment through acceptance, not necessarily absolute decline. The **operative oracle** is the check that actually changes which candidates survive. All else equal, under a fixed candidate distribution and acceptance rule, a directionally aligned oracle creates greater expected enrichment in a quality when it more reliably separates better instances from worse ones.

This note conjectures a statistical tendency in actual proposal-selection loops: under the conditions below, weakly discriminated qualities usually gain less from acceptance than strongly discriminated qualities, even when the generator produces usable variation in both. Candidate availability and candidate selection are therefore different bottlenecks. Representative loops that satisfy these conditions but usually produce equal or greater acceptance enrichment for weakly discriminated qualities would refute the conjecture.

The argument separates three conditions; the third is needed only for accumulation:

1. Generated candidates vary on more than one quality.
2. Acceptance or retention distinguishes better from worse instances of some qualities more reliably than others, strongly enough to affect survival after accounting for scoring weights, hard constraints, and correlations among qualities.
3. For the selection difference to accumulate, accepted outputs carry the relevant qualities into the starting point, context, or training signal for later iterations.

The first two conditions create unequal enrichment within one selection round. The third lets that difference propagate. Absolute degradation requires another directional mechanism, such as adverse correlation between qualities, production biased toward locally expedient changes, irreversible accumulation of harmful changes, or repair costs that grow unless the weak quality is actively selected for. A loop can widen the gap between two qualities while the weakly discriminated one stays flat or improves more slowly.

The operative oracle need not match the rubric a system says it values. A quality can be prominent in instructions or a schema yet exert little selection pressure if nothing in the loop separates its better instances from its worse ones.

## Oracle asymmetry creates selection asymmetry

[Why Software Factories Fail](../sources/why-software-factories-fail-2080697380379427275.md) argues that coding benchmarks reward patches that pass tests while imposing little penalty for design costs that appear through later changes. Consider a candidate set that varies in functional correctness and maintainability. Tests reject behavioral failures quickly, while delayed or noisy maintainability review gives patches with different future change costs similar survival chances. Conditioning on acceptance then enriches the patch population more strongly for correctness than for maintainability.

The source's failed lights-off deployment is consistent with this mechanism but does not isolate it: missing generation capacity, weak global codebase comprehension, and poor activation predict similar visible failures. Absolute maintainability decline also needs an adverse production or inheritance dynamic. Local fixes, duplicated logic, and awkward dependencies can accumulate when candidate production favors immediate progress and later repair is costly, but unequal discrimination alone establishes only weaker enrichment.

The same asymmetry can arise in an agent-operated KB. Structural validation strongly distinguishes broken frontmatter, invalid types, and unresolved links. It may distinguish less reliably whether a note has [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)—whether its explanation keeps working beyond the cases that produced it—or whether a connection reduces navigation uncertainty. A high-throughput authoring loop can therefore enrich accepted artifacts more strongly for structural validity than for semantic quality, [especially when maintenance does not scale with generation](./entropy-management-must-scale-with-generation-throughput.md). Semantic decline follows only if later production or inheritance also pushes in that direction.

## Generation, activation, and selection are different hypotheses

Poor retained output is often attributed to missing generator capability, but three different bottlenecks can produce the same visible failure:

- **Generation failure:** The desired quality is absent from the candidates the generator can produce.
- **Activation failure:** The generator can produce the quality under some prompts or contexts, but the current task frame does not elicit it.
- **Selection failure:** Usable candidates appear in the current process, but the operative oracle does not favor them strongly enough to survive.

The distinction matters because the remedies differ: improve the generator for generation failure, change the task frame or add probes for activation failure, or strengthen the acceptance checks for selection failure.

[The Bug That Shipped](../sources/the-bug-that-shipped-2035319413474206122.md) separates generation capacity from activation. Coding models rarely surfaced deployment failures under generic self-review yet diagnosed the same failures when directly probed. The changed task frame elicited behavior that generic review did not. The case does not show candidates with the desired quality appearing and then losing at an acceptance boundary, so it is not by itself evidence of selection failure.

A controlled stronger-oracle intervention tests selection. Hold the candidate set fixed, or otherwise control its distribution, then compare the rankings produced by generic review with those produced by explicit maintainability probes, pairwise design comparisons, repeated-change evaluations, or repository-specific structural checks. If the stronger oracle reliably favors better designs in the same candidate set, selection was a material bottleneck. If candidates remain poor even under a discriminating oracle, generation capacity, activation, global comprehension, or the quality definition remains the better explanation. Changing the prompt that produces candidates does not isolate selection because it may also change activation.

## Stronger oracles require independent discrimination

A weak oracle can be strengthened from partial signals, but not by vote count alone. Combining checks helps only when each contributes genuine discrimination and their failure modes differ, [since error correction requires above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). Repeating the same model, prompt, and evidence can amplify a shared blind spot.

A composite oracle also needs calibration against effects on the target quality. For maintainability, later change locality or performance on modification tasks can test whether accepted designs became easier to change. For KB quality, later decisions and traversal behavior can test whether a note or connection helped. Proxy agreement without outcome calibration constructs a louder proxy. Human judgment is another candidate signal, not an automatic strong oracle; it must earn discrimination in the target domain too.

## Predictions

- On a fixed candidate set, strengthening discrimination for one quality should increase that quality's enrichment among accepted outputs without a weight change, provided usable variation exists.
- Across representative loops satisfying the named conditions, weakly discriminated qualities should usually receive less acceptance enrichment than strongly discriminated qualities. Equal or greater enrichment for the weak qualities would refute the statistical tendency.
- Generic self-review should underperform checks that name distinct failure perspectives when activation contributes to the bottleneck.
- Sequential systems should widen quality gaps only when accepted outputs materially shape later iterations; mere sequencing without inheritance is insufficient.
- Absolute decline should appear only where candidate production, quality covariance, irreversibility, or repair costs supply an adverse direction.
- Correlated reviewers should plateau, while heterogeneous checks should help only when they add above-chance marginal signal and remain calibrated against later outcomes.

These predictions distinguish the conjecture from “what gets measured gets managed.” The proposed mechanism is unequal candidate enrichment under unequal discrimination. Compounding and absolute decline make additional commitments that can fail separately.

## Scope and rival explanations

- The claim requires a selection or retention pathway. When output is produced without comparison or an acceptance decision, “underselection” is the wrong description. Reuse or learning is additionally required only for the effect to compound across iterations.
- An oracle cannot select a quality absent from the candidate distribution. Strong verification does not manufacture generator capability.
- Discrimination need not dominate scoring weight, hard constraints, or quality correlations in every loop. The population-level dominance needed for the stated tendency remains conjectural.
- Some qualities genuinely conflict. A system may knowingly trade maintainability for latency or semantic nuance for consistency; that is objective weighting, not necessarily oracle weakness.
- Delayed quality can degrade because the model lacks global state, context, or causal understanding. Oracle asymmetry is one mechanism to test against those rivals, not a universal diagnosis.
- Human judgment can be inconsistent, biased, expensive, or unable to observe delayed effects. Its value must also be established for the target domain.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: verification cost determines which qualities can support warranted automation
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: aggregate generator accuracy cannot replace per-instance discrimination at the acceptance boundary
- [A checked outcome licenses retaining an episode, not abstracting its explanation](./checked-outcome-licenses-episode-retention-not-abstraction.md) — extends: outcome and process checks can strongly verify different qualities of the same candidate
- [Inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — enables: inspectable form supplies evidence a quality oracle can evaluate, without guaranteeing that the evaluator discriminates adequately
