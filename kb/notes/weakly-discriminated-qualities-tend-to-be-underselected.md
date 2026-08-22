---
description: "Statistical conjecture: under named proposal-selection conditions, unequal oracle discrimination yields unequal enrichment; absolute degradation needs an additional directional mechanism"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, llm-reliability, evaluation, self-improving-systems]
---

# Weakly discriminated qualities tend to be underselected

Underselection means less enrichment through acceptance, not necessarily absolute decline. The **operative oracle** is the check that actually changes which candidates survive. Holding the candidate distribution and the rest of the acceptance rule fixed, a directionally aligned oracle creates greater expected enrichment in a quality when it more reliably separates better instances from worse ones.

**Claim mode: statistical. Discovery-lifecycle stage: conjecture.** This note conjectures that, in actual proposal-selection loops satisfying the conditions below, weakly discriminated qualities usually gain less from acceptance than strongly discriminated qualities. Candidate availability and candidate selection are different bottlenecks. Representative qualifying loops in which weakly discriminated qualities usually receive equal or greater acceptance enrichment would refute the conjecture.

The argument separates three conditions; the third is needed only for accumulation:

1. Generated candidates vary on more than one quality.
2. Acceptance or retention distinguishes better from worse instances of some qualities more reliably than others, strongly enough to affect survival after scoring weights, hard constraints, and correlations among qualities are accounted for.
3. Accepted outputs materially affect the candidates, context, decisions, or training signal of later iterations.

The first two conditions permit unequal enrichment within one selection round. The third lets that difference propagate. Absolute degradation additionally requires some adverse directional mechanism. Examples, not an exhaustive list, include adverse correlation between qualities, production biased toward locally expedient changes, irreversible accumulation of harmful changes, and repair costs that grow unless the weak quality is actively selected for. A loop can widen the gap between two qualities while the weakly discriminated one stays flat or improves more slowly.

The operative oracle need not match the rubric a system says it values. A quality can be prominent in instructions or a schema yet exert little selection pressure if nothing in the loop separates its better instances from its worse ones.

## Oracle asymmetry creates selection asymmetry

[Why Software Factories Fail](https://x.com/dexhorthy/status/2080697380379427275) argues that coding benchmarks reward patches that pass tests while imposing little penalty for design costs that appear through later changes. Consider candidates that vary in functional correctness and maintainability. Tests reject behavioral failures quickly, while delayed or noisy maintainability review gives patches with different future change costs similar survival chances. Conditioning on acceptance then enriches the patch population more strongly for correctness than for maintainability.

The source's failed *lights-off deployment*—an unattended run expected to operate without active human intervention—is consistent with this mechanism but does not isolate it. Missing generation capacity, weak global codebase comprehension, and poor activation predict similar visible failures. Local fixes, duplicated logic, and awkward dependencies can accumulate when candidate production favors immediate progress and later repair is costly, but unequal discrimination alone establishes only weaker enrichment.

The same asymmetry can arise in an agent-operated KB. Structural validation strongly distinguishes broken frontmatter, invalid types, and unresolved links. It may distinguish less reliably whether a note has [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)—whether its explanation keeps working beyond the cases that produced it—or whether a connection reduces navigation uncertainty. A high-throughput authoring loop can therefore enrich accepted artifacts more strongly for structural validity than for semantic quality, [especially when maintenance capacity falls behind harmful-artifact inflow](./maintenance-capacity-must-match-harmful-artifact-inflow.md). Semantic decline follows only if production or inheritance also pushes in that direction.

## A commensurate operational comparison

A test needs to compare discrimination and enrichment across qualities without treating unlike raw scales as equal. For each quality, predeclare a binary adequacy outcome tied to an independently assessed behavioral or downstream result: for example, whether a patch passes a later modification task or whether a note supports a specified decision. Assess this outcome independently of the operative oracle. The threshold may differ by quality, but it must be fixed before observing selection results and mean a comparably decision-relevant success. If no such thresholds can be defended, the cross-quality test does not qualify; use a within-quality oracle intervention instead.

Use disjoint calibration and evaluation blocks for each [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md):

1. **Estimate discrimination on the calibration block.** Within each candidate set, form pairs that differ on the quality outcome but satisfy the same hard constraints and are matched within declared tolerances on the other measured qualities. The quality's discrimination score is the fraction of pairs in which acceptance favors the adequate candidate minus the fraction in which it favors the inadequate candidate; acceptance ties contribute zero. This signed concordance lies between -1 and 1. Designate a quality as stronger or weaker only when this block supplies enough matched pairs to order their scores.
2. **Measure enrichment on the evaluation block.** For each episode and quality `q`, let `p_q` be the adequacy prevalence among all offered candidates and `a_q` its prevalence among accepted candidates. Compute `E_q = (a_q - p_q) / (1 - p_q)`. This is the fraction of available improvement headroom captured by acceptance. A quality with `p_q = 1` has no headroom and does not qualify for that episode. Predeclare minimum headroom and sample support, publish both raw prevalences, and compare quality pairs within baseline-prevalence strata so near-ceiling or sparse candidates cannot dominate the normalized result.
3. **Test the held-out ordering.** Within each loop, compare `E_q` for the quality classified as stronger with `E_q` for the one classified as weaker, then average the episode-level paired differences. The evaluation block must not be reused to choose those labels. The resulting `E_strong - E_weak` is the loop-level result.

The representative-loop sampling frame must also be declared before results are known. Name the intended population and construct a registry of projects or deployed loops without screening on their discrimination or enrichment scores. Draw a stratified random sample across the declared domains and loop designs, then include every consecutive qualifying selection episode in a fixed time window. Predeclare the quality pairs, adequacy tests, matching tolerances, and exclusions. Aggregate at the loop level so a high-volume loop does not stand in for many independent loops. The conjecture predicts a positive median paired difference and a positive difference in more than half of representative qualifying loops. A nonpositive median, or equal or greater enrichment for the weak quality in at least half, is the explicit prevalence refuter. No such representative prevalence evidence is presently supplied here.

This protocol does not make absolute decline part of the test. Decline is a separate outcome: it requires the accepted population's independently assessed quality to worsen over iterations, together with evidence for an adverse production or propagation mechanism.

## Propagation and stronger-oracle interventions

Material propagation is behavioral, not literal reuse. Start two branches from the same pre-selection state and force acceptance of matched outputs that differ on the target quality. Hold later tasks, instructions, and selection rules fixed, and repeat enough stochastic trials to compare the branches. The accepted quality materially propagates when that intervention changes later candidate distributions, acceptance decisions, or calibrated downstream outcomes. Copying an output into context is neither necessary nor sufficient: a later process can reconstruct its effects without copying it, or an authoritative specification can erase them despite literal inclusion.

Poor retained output can still arise from three distinct bottlenecks:

- **Generation failure:** Candidates with the desired quality are not produced.
- **Activation failure:** The generator exhibits the quality under some task frames, but the current frame does not elicit it.
- **Selection failure:** Usable candidates appear in the current process, but the operative oracle does not favor them strongly enough to survive.

[The Bug That Shipped](https://x.com/KatanaLarp/status/2035319413474206122) reports that coding models rarely surfaced deployment failures under generic self-review yet diagnosed them when directly probed. That behavior distinguishes the current task frame from one that activates the relevant response; it does not show good candidates losing at an acceptance boundary.

A stronger-oracle intervention isolates selection only when it holds the candidate set and other acceptance conditions fixed. Ranking disagreement is insufficient. The stronger oracle must change which candidate is actually retained—in a randomized deployment or a paired sandbox where both choices can be executed—and the changed acceptance must improve an independently calibrated downstream outcome for the target quality without violating declared constraints. If it does not change acceptance, it was not a material selection bottleneck; if it changes acceptance without improving the outcome, it has not earned the claim of stronger discrimination.

Combining checks helps only when each adds above-chance marginal discrimination and their failure modes differ, [since error correction requires above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). Any composite must still be calibrated by whether its changed acceptances improve the target outcome. Agreement among proxies, including human judgments, is not enough.

## Scope

- The one-round claim requires comparison or an acceptance decision over offered candidates. When output is produced without a reject-capable selection pathway, “underselection” is the wrong description.
- The compounding claim additionally requires material propagation under the branching intervention above. Mere sequencing or literal reuse does not establish it.
- An oracle cannot select a quality absent from the candidate distribution. Strong verification does not manufacture generation or activation.
- Objective weights, hard constraints, and genuine conflicts among qualities can dominate discrimination. A deliberate maintainability-for-latency trade is not necessarily oracle weakness.
- Delayed quality can suffer because the system lacks global state, sufficient context, or representations that support reliable prediction of system-wide effects. Oracle asymmetry is one mechanism to test against these rivals, not a universal diagnosis.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: verification cost determines which qualities can support warranted automation
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: aggregate generator accuracy cannot replace per-instance discrimination at the acceptance boundary
- [A checked outcome licenses retaining an episode, not abstracting its explanation](./checked-outcome-licenses-episode-retention-not-abstraction.md) — extends: outcome and process checks can strongly verify different qualities of the same candidate
- [Inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — enables: inspectable form supplies evidence a quality oracle can evaluate, without guaranteeing that the evaluator discriminates adequately
