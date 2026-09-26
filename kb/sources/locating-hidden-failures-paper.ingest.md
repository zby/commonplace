---
description: "Traverse separates task outcomes, first-error localization, safety, and recovery; Scout improves selection from fixed candidate pools without testing online repair or actor learning."
source: https://arxiv.org/abs/2609.17930
captured: "2026-09-20"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 3fda26e49c0da45e65ca0a668b54b2df57ea372ea421ccfe7a2b16e31cc0cd7f
ingested: "2026-09-26"
type: types/ingest-report.md
domains: [agent-evaluation, failure-localization, trajectory-selection]
learning_claims: true
---

# Ingest: Locating Hidden Failures Makes Long-Horizon Agents More Reliable

## Classification

An empirical research preprint combining trajectory annotation, descriptive failure analysis, a verifier benchmark, and trained-verifier selection experiments. Salman Rahman and colleagues list affiliations with UCLA, NYU, Google Research, and Google DeepMind. The author affiliations are a research signal, not independent validation. This analysis is derived from the [full paper](https://arxiv.org/abs/2609.17930), whose captured version includes unresolved placeholders and reporting inconsistencies.

## Summary

Traverse makes first-error localization a separately testable capability: its reported benchmark contains 1,423 trajectories across software engineering, terminal tasks, and bioinformatics analysis. Human annotators locate task errors; LLM judges categorize those errors and separately assess self-detection and safety. The paper finds mistakes in successful runs, unsuccessful runs without a single decisive mistake, and unsafe actions missed even by task-correctness labels. Six general-purpose judges achieve at most 26.8% exact first-error localization on SWE-bench and 32.3% on TerminalBench; the strongest reaches 63.2% on the shorter BixBench trajectories. Scout, a 4B verifier trained on step labels and generated analyses, selects successful completed runs more often than two reported frontier-verifier baselines when all selectors receive the same candidate pools: 90.2% on Terminal-Bench 2.0 and 78.0% on SWE-bench Verified. This supports specialized selection within the supplied representation and candidate pools. It does not demonstrate live interception, recovery from unsafe actions, or improvement of the unchanged acting agent. The benchmark and distinctions are useful for designing trajectory audits; incomplete reporting limits stronger claims about Scout's localization and transfer performance.

## Contribution assessment (our opinion)

The work appears to make useful progress on a consequential measurement problem: a passing result does not identify where an agent erred or establish that its route was safe. Human localization labels and a benchmark that separates detection from localization enable stronger criticism of verifiers than final task scores alone. The fixed-pool comparison supplies concrete evidence that specialized verifier training can improve selection over the two displayed verifier baselines. The paper's comparisons suggest a useful combination of realistic traces, domains, and annotation granularity, but do not establish broad priority. Its strongest potential contribution is the evaluation resource; reporting gaps weaken the separate claims of superior learned localization and transfer, while leaving the case for measuring process failures substantially intact.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a comparison for [final task success does not establish intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md). Both separate endpoint results from execution properties, but Traverse's task errors and harmful actions do not test the note's particular mechanism of successful fallback concealing infrastructure failure. Its additional distinction is that even a task-oriented step label can miss harm.

Figure 7 supplies bounded evidence relevant to [enforcement without structured recovery is incomplete](../notes/enforcement-without-structured-recovery-is-incomplete.md): within each of two domains, runs judged to notice their first mistake recover at nearly the same rate as those judged not to notice it. This observation separates recognition from recovery; it neither establishes the causal effect of recognition nor tests the note's corrective-action, fallback, and escalation policy. The paper also compares with [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): a step location supplies evidence absent from an outcome score, but Scout's selector experiment does not test whether a proposer uses that diagnosis to produce better repairs.

The existing [trajectory-aware workflow evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) is the practical destination. Traverse motivates separate localization, safety, false-alarm, and recovery measurements; Scout demonstrates selection among completed candidates with the acting agent and candidate pools fixed. Neither result satisfies the proposal's local calibration and cost requirements. Compared with the [earlier abstract-page ingest](./locating-hidden-failures.ingest.md), the full paper resolves the uncertainty about matched candidate pools for the displayed selector comparison, while leaving online prevention untested.

## Learning Claims (our opinion)

Scout learns a verifier in two stages. Supervised fine-tuning imitates step-by-step analyses generated by Gemini-3 Flash using gold correctness labels; generated analyses are retained only when their parsed verdicts match those labels. GRPO then rewards Scout's own verdicts against the same labels. On trajectories containing errors, the step reward multiplies recall on correct steps by recall on incorrect steps, penalizing either constant-label strategy; a trajectory-level term supplies a coarser signal. At use time, Scout ranks completed candidates by its probability of judging them correct. The reported selection advantage is evidence of a useful trained evaluator in that arrangement, not by itself an ablation identifying the contribution of GRPO, its reward, or the generated reasoning.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), the relevant boundary is Scout's training and selection pipeline. **Localized content:** its rubric, training labels, generated analyses, and assessed trajectory steps are stated, but the acquired verifier function resides in weights. **Consumption:** those stated inputs guide verifier training and judgments, and the selector consumes its scores; the acting agent does not consume the localization to revise an attempt. **Content-directed criticism:** the generated analyses discuss particular thoughts and actions, while the optimization signal checks verdict agreement and changes weights; label agreement does not independently establish the truth of the explanations. **Iteration:** training repeatedly updates parameters, but the demonstrated selection pipeline does not retain a criticism of a stated theory for a subsequent revision or test. These components therefore do not establish a theory builder, even though parametric learning may improve performance. Learned weights persist across evaluation tasks; the experiment does not show persistent changes to the actor or a reusable actor-side correction record.

An indexed mistake is an address for inspection, not yet an [addressable theory](../notes/definitions/addressable-theory.md) or a verified causal explanation. The boundary in [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) applies: Scout can alter judgments over supplied thought/action/observation traces, but its label semantics, trajectory representation, actor, and candidate generation are fixed outside the selector comparison. It cannot select a successful run absent from the pool. The result supports improvement within this arrangement, without comparing alternative error targets, evidence representations, or repair policies. The aspiration that agents learn from their own mistakes remains a proposed downstream use.

## Extractable Value

1. **Keep outcome, task-error, and safety judgments separate.** Figure 7 reports both solved-but-flawed and failed-without-localizable-error runs. Figure 9 reports that 54% of the primary judge's 65 unsafe actions were invisible to gold task-step labels. The transferable distinction is that these labels answer different questions; the frequencies belong to this corpus and safety judge. This sharpens the existing workflow-evaluation proposal beyond merely adding more trace context. [quick-win]
2. **Calibrate localization independently of detection and explanation.** Tables 1 and 2 show that detecting an erroneous trajectory is easier than locating its first erroneous step. A local audit should separately measure correct failure identification, evidence location, false alarms, and whether explanations survive checking. The paper's task-step representation and first-error target do not establish which localization unit is best for Commonplace workflows. [experiment]
3. **Measure whether detection leads to recovery.** The within-domain Figure 7 comparison shows why noticing a mistake and eventually solving the task need separate labels. Pooling domains reverses the apparent relationship. This supports tracking review-to-revision closure in the existing proposal, without assuming that self-detection causes or fails to cause repair. [experiment]
4. **Use fixed candidate pools to test selectors, then test intervention separately.** Figure 4 compares Scout with two frontier verifiers on identical pools, supporting a selector-quality difference under those conditions. Comparisons against single-attempt agents also include the benefit and cost of generating multiple attempts. Reusing this evaluation pattern would separate better ranking from better candidate generation; it would still leave safe generation and online recovery to distinct experiments. [experiment]

## Limitations (our opinion)

**The first-error target is selective.** The Methods define errors using evidence available to the agent, but also describe them as sending the task away from any solvable path while allowing later recovery. That wording leaves the error boundary imperfectly specified. Human agreement is substantial rather than perfect, and the benchmark excludes some malformed or incomplete traces. The first-error framing excludes diffuse failures: Figure 7 reports 588 failed runs without a localizable first mistake. Local error detection is consequently not equivalent to predicting final task failure, despite passages that treat it as an outcome-reward judgment.

**Annotation layers have different support.** Humans locate errors; model judges assign taxonomy, root/cascade, self-detection, and safety labels. Fine-category agreement is only κ = 0.30, compared with 0.66 for families. Safety prevalence is judge-sensitive. The Methods describe keyword-proposed safety candidates, while Figure 9 says a regex-only scan misses most unsafe actions; coverage of the audit is not clear enough to treat its counts as complete. A correctness label is not a safety guarantee, and agreement with correctness labels does not validate generated causal explanations.

**Descriptive associations do not identify causes.** Consecutive incorrect steps co-occur, but that does not establish that the first labeled error caused each later one. Domain, task, model, and harness vary together. The claim that environmental feedback rather than harness design determines recovery is not supported by an intervention isolating those choices. Likewise, similar recovery among noticed and unnoticed cases does not estimate the effect of giving an agent a reliable external diagnosis.

**The captured paper has material reporting gaps.** It gives both 2,620 and 2,518 corpus totals, and describes a 600-trajectory SWE benchmark as selected from a corpus whose SWE count is 565. Figure 7 restricts Figure 3's first-mistake analysis to flawed-and-failed runs, whereas surrounding text interprets recovery over runs with a mistake; those scopes cannot be silently reconciled. Unresolved appendix and figure placeholders remain. The Methods promise held-out Scout localization, SFT-only versus SFT+RL, and cross-domain evaluations, but the retained results do not provide corresponding detailed comparative tables. BixBench selection improvement appears in the introduction without comparable detailed results. These claims remain reported claims rather than fully assessable comparisons.

**Selection does not establish prevention or durable actor improvement.** The displayed fixed-pool result supports ranking within an unchanged actor's candidate distribution. It does not isolate training stages or prove that step-localization training is necessary for the ranking gain. Generating completed candidates can already incur harm; a later choice cannot undo it. No implementation was inspected or executed, and no reproduction, online intervention, matched total-compute comparison, or Commonplace workflow trial is established here.

## Recommended Next Action

Update [Trajectory-aware evaluation of transforming agent workflows](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) with Traverse's distinction between outcome, task-error, and safety labels, retaining separate localization and recovery measurements and treating Scout's fixed-pool selection result as bounded motivation rather than evidence for online prevention.
