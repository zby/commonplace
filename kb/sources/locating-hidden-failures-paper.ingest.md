---
description: "Traverse and Scout separate task success, first-error localization, and safety; fixed-pool selector gains support specialized verification, with important label and reporting limits."
source: https://arxiv.org/abs/2609.17930
captured: "2026-09-20"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: e6587dc07a99e120b78d37ec3adb432b11f5a062e7fd577f1aeae1fa77e3eeac
ingested: "2026-09-20"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, failure-localization, verifier-training, agent-safety]
learning_claims: true
---

# Ingest: Locating Hidden Failures Makes Long-Horizon Agents More Reliable

## Classification

An empirical research preprint combining annotated trajectory analysis, a failure-localization benchmark, verifier training, and retrospective candidate selection. Salman Rahman and colleagues list affiliations with UCLA, NYU, Google Research, and Google DeepMind. The methodological detail supports inspection, but the captured manuscript contains unresolved counts, placeholders, and missing result detail; institutional affiliation does not resolve those gaps. This analysis derives from the [primary paper](https://arxiv.org/abs/2609.17930).

## Summary

The paper studies long-horizon software-engineering, terminal-use, and scientific-analysis trajectories, separating final task outcome from local mistakes and destructive actions. Its methods describe 2,518 trajectories, while Traverse selects 1,423 for first-mistake evaluation. Six frontier judges achieve at best 26.8% exact localization on SWE-bench and 32.3% on TerminalBench. Scout trains a 4B verifier on correctness-labelled trajectories through supervised fine-tuning and reinforcement learning. With completed candidate pools held fixed across selectors, it reports 90.2% task success on Terminal-Bench 2.0 versus 84.3% and 80.9% for two frontier verifiers, and 78.0% on SWE-bench Verified versus 75.8% and 77.4%. These comparisons support the trained selector within the supplied trajectory representation and correctness target; they do not establish online interception, safer execution, or agent self-improvement. The most useful qualification is that both first-error labels and final outcomes leave gaps: about 43% of unsuccessful runs have no localizable mistake, and 54% of one judge's flagged unsafe actions are marked correct by the gold step labels. Several reporting inconsistencies limit precise reuse of the broader claims.

## Quotes

No source quotes have been retained yet.

## Connections Found

The safety audit supplies a concrete bounded example for [warranted autonomy being bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md). Figure 9 reports that 54% of the primary judge's 65 unsafe actions were gold-step-correct. Even a perfect match to those correctness labels would not establish safety. This is evidence about the label target, not a measurement of Scout's safety recall.

The selector experiment also makes the distinction in [an experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) operational. Section 3.3 holds candidate pools fixed across selectors, supporting a comparison of selector systems. The training recipe and task-correctness representation remain bundled, while comparison with single-attempt performance additionally includes extra candidate generation. Neither contrast tests acting on warnings during execution.

The practical destination is the existing [trajectory-aware workflow evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md). The paper motivates separate labels for task errors, safety violations, and failures without a single decisive error. It does not supply the proposal's local calibration or adoption evidence.

## Learning Claims (our opinion)

Scout learns a parametric mapping from a supplied thought/action/observation history and judging rubric to an analysis with per-step correctness verdicts. Gemini-generated training analyses receive the gold labels in advance and are regenerated until their parsed verdicts match. Supervised fine-tuning updates all verifier parameters; GRPO then rewards the verifier's own sampled analyses against the same labels. Its reward combines the product of correct-step and incorrect-step recall with a trajectory-level verdict term, using a separate all-correct rule for clean trajectories. This is a concrete training method for avoiding a reward that tolerates predicting only the majority class, though the manuscript does not provide an isolated reward-design ablation establishing that this choice caused the reported gains.

In Commonplace terms, this is parametric learning followed by application of the learned verifier, and the arrangement is not a [theory builder](../notes/definitions/theory-builder.md). Scout's judgment is in weights, so condition 1 fails for it, and SFT and GRPO against gold labels are gradient updates, not criticism of what a stated theory says (condition 3). Its generated analyses state per-step verdicts, but they criticize the acting agent's steps, not a theory, and they serve only to choose among finished runs. The acting agent's weights remain unchanged, and no next round takes the analyses up, so condition 4 fails: this is criticism that feeds nothing. The paper presents that further loop as a prospect.

The consequential fixed choices are the supplied trajectory boundary, step segmentation, correctness rubric, gold labels, and scoring interface. Scout changes its mapping within them; it does not learn which properties should count as errors or change how a selected run is executed. As the [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) requires, success inside this arrangement cannot vindicate those choices against alternatives. The safety mismatch shows omitted supervision, not that the raw histories make safety distinctions impossible to learn. Verdict agreement also does not validate the causal faithfulness of the generated explanations. The source offers a useful verifier-training case but no reason to change the theory-builder conditions.

## Extractable Value

1. **Keep task correctness and safety as separate evaluation targets.** The primary judge's safety findings overlap incompletely with gold step errors. This makes the oracle-domain limitation concrete for workflow audits: a process-aware check still warrants only the properties its labels cover. The reported 54% is conditional on 65 judged actions, not a general prevalence or Scout miss rate. [quick-win]
2. **Represent failures without forcing a first-error index.** Figure 7 separates 343 solved-but-flawed runs from 588 unsuccessful runs without a localizable mistake. The latter are about 43% of unsuccessful runs. A local benchmark can retain an explicit diffuse-failure category and measure first-error localization only where that target is adjudicable. [experiment]
3. **Use fixed candidate pools to evaluate selectors.** Scout's reported gains over two frontier selectors hold the available runs constant, providing stronger selector evidence than comparison with pass@1 alone. Transfer to Commonplace would still require local labels, uncertainty estimates, and cost measurement within the chosen representation; it would not test live recovery. [experiment]
4. **Separate annotation reliability from taxonomy detail.** Human agreement is reported as Cohen's kappa 0.77 for mistake presence and 0.73 for location. LLM agreement is 0.66 for failure family and 0.64 for root versus cascade, but only 0.30 for fine categories. Retain the coarse distinctions as diagnostic candidates rather than importing all 78 observed types as equally reliable labels. [just-a-reference]

## Limitations (our opinion)

**First-error coverage and causality.** Localizable errors are not synonymous with failed tasks. The error definition says a decision sends the task away from any solvable path, yet recovery is explicitly measured; that tension needs clarification before reproducing annotation. Adjacent-step error dependence and root/cascade judgments describe the sampled histories, not an intervention proving that correcting the first error prevents later failures. Domain, task, model, harness, and horizon covary. The paper's claims that feedback explains recovery and harness design does not are stronger than the comparisons isolate; discussion itself calls recovery and cross-domain findings directional. A within-domain length analysis retains a placeholder. These results cannot rule out harness interventions.

**Safety evidence has its own uncertainty.** The safety audit is LLM-adjudicated and judge-sensitive, separate from human first-error annotation. The reported keyword-based candidate generation and claim that regex alone misses 77% of unsafe actions need a clearer relationship before their coverage can be assessed. Selecting completed trajectories cannot undo harm already done while generating them. No online stop, rollback, or safety improvement experiment is reported.

**Training and outcome evidence remain bundled.** The fixed-pool result compares complete selector systems. It does not isolate gold-conditioned rationale generation, supervised training, reinforcement learning, reward choice, or backbone. Methods specify SFT-only and SFT-plus-RL localization evaluation on 258 decontaminated held-out trajectories, but the captured paper supplies no numerical Scout localization table supporting the claimed advantage or transfer. The introductory BixBench selection claim, 50.1% to 53.2%, lacks a corresponding detailed result panel. Significance and matched total inference-cost comparisons are not supplied. No implementation was inspected or executed for this ingest.

**The manuscript needs reconciliation.** The introduction reports 2,620 collected trajectories versus 2,518 in methods. Methods list 565 SWE trajectories in the parent corpus but 600 in its selected benchmark. Science trajectories are described as lacking full step labels, then included in a benchmark described as fully step-labelled. Missing-thought trajectories are said to be discarded, while the appendix explicitly accommodates OpenHands without thoughts. Figure 3's silent-failure bars and caption disagree, and Figure 7 describes the first-mistake analyses as restricted to flawed-and-failed runs despite recovery measures requiring solved-with-error cases. The taxonomy's 6,967 mistakes and training table's 6,994 incorrect steps may describe different populations, but their relationship is not explained. These conflicts do not erase the stated fixed-pool comparison or the distinct safety target; they prevent treating all counts and headline conclusions as one reconciled empirical account.

## Recommended Next Action

Update the [trajectory-aware workflow evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) with separate task-error, safety, and diffuse-failure labels, using this paper as bounded motivation and preserving its reporting uncertainties.
