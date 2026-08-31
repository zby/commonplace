---
description: "Paired coding-agent evidence shows that one fixed harness package changes task outcomes under context pressure while leaving component and cross-regime attribution limited."
source: https://arxiv.org/abs/2608.26218
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 029eaebf8b7342236b4b350e02a1bdb252ac8cd2e3027cbb9469b8799877bcb2
ingested: "2026-08-31"
type: kb/sources/types/ingest-report.md
domains: [coding-agents, context-engineering, evaluation]
---

# Ingest: Same Model, Different Harness: Different Coding-Agent Results

## Classification

This is an empirical scientific preprint: it specifies paired comparisons, endpoints, exact tests, sensitivity analyses, and scope limits rather than merely announcing the Yuj harness. Author: Sydney Lewis is the sole author and the builder-operator of the evaluated harness; that position provides first-party access to its mechanisms and run artifacts but also gives the author an interest in the treatment.

## Summary

The paper compares a full-chronological-transcript control with a Yuj treatment that jointly shortens older tool results, responds to detected stalls, and applies command safeguards, while holding the model, task, context capacity, tool interface, evaluator, and run protocol fixed within each pair. Under context pressure, the treatment raises mean per-task fail-to-pass fraction on SWE-bench Verified, SWE-bench Pro, and FeatureBench; it also raises complete solutions on the two SWE-bench cohorts. The same frozen package improves both endpoints for three additional model designs on the tight-window Verified cohort. At effectively unconstrained context, Verified and Pro outcomes are close across arms, while FeatureBench retains a partial-repair gain with weaker repository-level support. The study therefore identifies a resource-regime-dependent effect of the complete package, not a component effect or a compute-matched efficiency gain.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a controlled empirical anchor for [the deployed system, not the model alone, as the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): unchanged weights produce different task outcomes when runtime policy changes. It also supplies a within-run instance of [separating stored session history from the next model context](../notes/session-history-should-not-be-the-default-next-context.md), because the treatment preserves the complete record while rebuilding a bounded working view. Its deterministic age-tier policy supports that storage-versus-loading distinction without establishing that uniform mechanical shortening is preferable to goal-oriented compression. Compared with [the context-operation-interface claim](../notes/context-operation-interface-bounds-context-policy.md), Yuj tests one narrow host-owned projection interface and leaves summaries, semantic state, retrieval, and addressable recall untested.

For the fixed-decomposition check, model behavior can condition on the issue and repository, prior model messages, recent full tool results, shortened older results, and—through host interventions—recorded repetition or stall facts. The frozen model maps its visible history to composed search, read, shell, edit, and test actions; deterministic harness rules map context occupancy and result age to views, recorded patterns to intervention messages, and command patterns to safeguards. The chronological representation, absence of semantic retrieval or summaries, shortening caps, detector rules and responses, tool interface, cohorts, context windows, greedy decoding, time endpoint, and scoring remain fixed outside that behavioral space. Improvement therefore supports the compound package against its full-history control in the tested regimes; it neither validates those fixed design choices nor attributes the gain to one component, as [the experimental-contrast rule](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) requires.

## Extractable Value

1. **Harness effects are conditional on the resource regime.** Large tight-window gains, near-convergence on wide-window Verified and Pro, and a residual FeatureBench difference support a new synthesis: a measured harness delta is indexed by context capacity, task distribution, model, and endpoint rather than being an intrinsic harness ranking. [deep-dive]
2. **The model-plus-harness pair is the measured solver.** The paired design supplies direct outcome evidence for the KB's deployed-system boundary because it changes runtime policy while holding model weights and task inputs fixed. [quick-win]
3. **A complete record need not be the active view.** The treatment adds benchmark evidence to the existing session-history principle by retaining full traces while shortening the model-visible working set, although the bundled contrast cannot assign the improvement to shortening alone. [quick-win]
4. **Evaluation reports need runtime coordinates.** The study makes model identity, harness and configuration, tool interface, model-visible context policy, context limit, time budget, result-selection rule, and evaluator concrete reporting requirements for coding-agent comparisons. [quick-win]
5. **Component and interface comparisons remain the next causal test.** Detector-response ablation, alternative context-operation interfaces, repeated trajectories, and compute-matched endpoints would distinguish mechanisms that this package-level, single-trajectory study leaves coupled. [experiment]

## Limitations (our opinion)

The strongest causal result is assignment to the complete treatment package. View shortening, detector interventions, and command safeguards never vary independently, and each task contributes one greedy trajectory per arm, so the paper estimates neither component effects nor run-to-run variation. Treatment also consumes substantially more turns, prompt tokens, and wall time under pressure because it can continue after control fills its window. The efficacy gap is therefore not an efficiency comparison. The half-life settings were developed using operational runs from the same benchmark families rather than selected by a task-disjoint tuning study.

Applicability is limited to locally served four-bit open-weight models, repository coding benchmarks, fixed time endpoints, and benchmark test outcomes; hosted frontier models, higher-precision weights, other task types, and human patch quality are untested. Successive campaigns confound cross-window comparisons with run-era changes, the Pro and FeatureBench rows do not all use the final package, and some Pro continuation opportunities lack independent code stamps. The public release described by the paper omits raw runs and several benchmark and scorer artifacts, limiting independent audit. The sole author's dual role as harness builder and evaluator adds a further reason to seek independent replication.

## Recommended Next Action

Write `kb/notes/a-measured-harness-effect-is-conditional-on-the-resource-regime.md` to state that a harness effect is indexed by model, task distribution, context capacity, time endpoint, and comparison condition, using this source's tight-versus-wide results and the experimental-contrast rule to bound the claim.
