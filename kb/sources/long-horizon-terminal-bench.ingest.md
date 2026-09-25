---
description: "Long-Horizon-Terminal-Bench distinguishes partial completion and false finishes with deterministic final-state subtasks; it offers evaluation design evidence, not a tested memory remedy."
source: https://arxiv.org/abs/2607.08964
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 6f3c0465ca34ae84c5184c4bc697ca3871d8e29514faec95bdbb490f25fce93e
ingested: "2026-09-24"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, long-horizon-agents, verification]
---

# Ingest: Long-Horizon-Terminal-Bench

## Classification

A benchmark paper reporting task construction, deterministic grading, a 17-model comparison, and descriptive failure analysis. The retained version is arXiv v2; the capture does not establish peer review. Authors include Zongxia Li, Zhongzhi Li, and Yucheng Shi, with Tencent and university affiliations. They are the benchmark's designers and evaluators, so the results are first-party measurements.

## Summary

[Long-Horizon-Terminal-Bench](https://arxiv.org/abs/2607.08964) evaluates agents on 46 containerized terminal tasks with graded subtasks, including scientific audits, software repair, and games. A deterministic grader computes a weighted partial-credit score from the final container state. Within this fixed task and grading design, the paper reports that ten of 17 models solve no tasks at a perfect-score threshold, while partial scores distinguish their progress. The strongest reported configuration achieves 28.3% completion at a 0.95 threshold and 19.6% at 1.0. Most models use Terminus-2; GPT-5.3 uses Codex. Termination records combined with scores distinguish timeouts from voluntary exits that leave substantial work unfinished. This makes the paper useful for designing evaluation evidence, but its fixed subtasks, mostly shared harness, and nominal 90-minute budget do not isolate memory, planning, or verification as the cause of failure or test an intervention that improves them.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a comparison case for [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): keeping subtask scores distinguishes degrees of failure that a pass/fail summary erases. It does not test whether feeding those scores to a later proposer improves learning. Alongside [oracle strength](../notes/oracle-strength-spectrum.md), it illustrates a narrower distinction: the same deterministic checks can support both a strict acceptance decision and a more discriminating account of partial completion. Changing the reported aggregation does not establish stronger correctness coverage.

For the [trajectory-aware evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md), the benchmark supplies an adjacent design option: retain checks of intermediate deliverables in the final state. Under this representation, richer outcome evidence remains insufficient to establish chronological ordering, worker isolation, or recovery behavior. Those proposal questions still need execution evidence.

## Extractable Value

1. **Separate acceptance from progress reporting.** Under one fixed set of deterministic subtask checks, a threshold answers whether a run passes while the score describes how much of the checked work survives. The reported ten-way tie at zero perfect completions shows why retaining both can help diagnose difficult workflows. This is a reusable evaluation pattern, conditional on having meaningful, separately checkable subgoals; it does not validate those subgoals as a complete account of quality. [quick-win]
2. **Combine progress with termination cause.** The paper identifies 14 high-reward voluntary exits among 124 early exits, including several legal-workflow runs that stop with roughly 20 minutes remaining. These examples motivate a distinct completion-verification test rather than treating every failure as budget exhaustion. A controlled intervention would need to hold task, model, harness, and budget fixed; the paper supplies no such comparison. [experiment]
3. **Distinguish final-state detail from process visibility.** Section 2.2 specifies grading at rollout end, even though the paper also uses process-reward language. Subtask scores can reveal missing deliverables without exposing when or why execution diverged. This boundary helps scope the evidence needed by Commonplace's proposed workflow evaluation. [quick-win]

## Limitations (our opinion)

The model comparison varies models within a chosen task decomposition and mostly shared harness. It does not compare alternative subtask boundaries, scoring weights, state representations, planning methods, or memory mechanisms. GPT-5.3's different harness further prevents treating the whole leaderboard as a model-only comparison. Task difficulty was calibrated using DeepSeek V4 Pro, and the reported evaluation does not establish variability across repeated runs or a human-calibrated task horizon.

Timeout is a termination condition, not a causal diagnosis. Domain difficulty, local errors, tool speed, context handling, and exploration can all produce unfinished work. Likewise, a voluntary exit with hidden-test failures does not alone establish that further verification available to the agent would have found the defect. The proposed planning and memory remedies remain hypotheses. As the diagnostic-richness note emphasizes, a score can select or distinguish outcomes without explaining their causes.

Several numerical details are inconsistent. Figure 4 reports 50 passes among 782 runs, implying 732 unresolved runs, but section 3.4 uses 660 unresolved runs for its failure proportions without reconciling the populations. Figure 4's caption gives 68 runs in the 0.85–0.95 band while the plotted label gives 31. Section 2.4 says 21 categories despite the nine-category figure and appendix. Table 1 includes a 176.1-minute average for Hy3 despite the stated 90-minute timeout. These discrepancies limit reuse of precise failure shares and cross-model budget claims.

Deterministic hidden tests check the chosen specification; they do not establish that weighted reward is proportional to useful work or that a high score means little work remains. The implementation and raw trajectories were not inspected or executed for this ingest, so benchmark results and grader behavior remain paper-reported evidence.

## Recommended Next Action

Review the [trajectory-aware evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) to distinguish requirements checkable from retained final-state deliverables from requirements that need chronological execution evidence, using LHTB as the bounded example of the former.
