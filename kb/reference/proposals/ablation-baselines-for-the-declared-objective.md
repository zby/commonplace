---
description: "Proposal: compare work quality and human effort on matched repository tasks with and without curated theory, review, episodic examples, or a stronger model"
type: reference/types/design-proposal.md
tags: [evaluation]
---

# Ablation baselines for the declared objective

This proposal tests [Commonplace's objective](../commonplace-declared-frame.md#what-commonplace-chooses-to-count) on matched tasks in a declared area. The traced tag-readme episode establishes local conformance and one pathway's success, and [a successful composition episode is one bit about a whole configuration](../../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md): compatible with the decomposition being right, with one component compensating for another, with the maintainer quietly repairing the result, and with the same outcome occurring without the framework. [The reach-to-objective link is a bet the loop places and never checks](../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md). More traces of the same kind cannot separate these; only comparison can. This proposal holds the design space for that comparison, prompted by an external review of the reflective self-improvement article (2026-07-28) that named the ablation family directly.

[Commonplace as an instrument](../case-studies/commonplace-as-an-instrument.md) names baseline comparison against the declared objective alongside four other evidence shapes — outcomes on the open rationale questions, independent-operator and cross-domain tests, a faithfulness test by intervention, and composition failures attributed back. Those four test whether the machinery behaves and transfers as described; this proposal develops the comparative ablation shape that tests whether having the machinery beats not having it.

## Current state (as of 2026-07-28)

- At the time of this proposal, the instrument note stated the objective; the proposed comparison had not been run.
- One composition trace exists (the tag-readme episode), plus two worked provenance instances. All were produced and assessed inside the system.
- The knowledge-centric self-improvement preprint (arXiv 2607.19592, ingested) demonstrates a workable protocol shape for one arm: agents held generic and disposable, the knowledge artifact frozen, transfer measured across tasks and model families.
- The `condensation-faithfulness-experiment` workshop (named, not linked) is designing an adjacent, narrower experiment — condensation methodology against naive auto-summary under a perturbation protocol. It ablates one mechanism; this proposal ablates the framework.
- The Commonplace repository is public. Its content, including the methodology being tested, may enter model training corpora — a live confound for any "bare stronger model" arm.
- (2026-08-02) The later-episode compounding protocol now has its own note: [compounding is tested in later improvement, not by the accepting metric](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — displaced measures, uptake traces, and three baselines whose stronger-model arm carries this proposal's contamination force. The two target different quantities: that note tests whether a retained benefit helps produce later improvement; this proposal tests whether the framework earns its cost on the selected tasks.

## Problem

Design a comparison that could show the framework failing to earn its cost. The conditions the external review proposed — and this proposal treats as the canonical arm set to select from — are matched repository tasks run with:

1. the curated theory and contracts (the framework as operated);
2. raw repository history and documentation, no curated layer;
3. episodic examples without distilled theory;
4. the same artifacts with reach-oriented review disabled;
5. a stronger model with no Commonplace layer at all.

measuring task quality, escaped errors, retrieval failures, negative transfer, human decisions and minutes, and later maintenance cost. Arms 2–3 test the distillation claim, arm 4 tests the review claim, arm 5 tests the absorption objection — the same objections the article now answers argumentatively would be answered empirically, in either direction.

## Design space

1. **Prospective battery.** Pre-register a task set, run all arms concurrently. Cleanest comparison, highest cost, and the task authoring itself imports bias.
2. **Historical replay.** Re-run real past repository tasks (recoverable from git history with their accepted outcomes) under ablated conditions, comparing against what actually shipped. Cheap task sourcing and real tasks, but the accepted outcome leaks into every corpus-trained model and the operator's memory.
3. **Outside-operator transfer.** A maintainer who did not build the system runs matched tasks with and without the KB on their own project — subsumes the instrument note's "outside assessment" while adding the ablated control. Strongest external validity, hardest to arrange.
4. **Frozen-artifact transfer (KSI-shaped).** Freeze the KB, hand it to different model families with disposable agents, measure gains against no-KB controls on held-out tasks. Bypasses the operator confound entirely; tests only the artifact layer's value, not the human-inclusive loop.

Free choices, marked as such: the task battery composition; metric weights across quality, error, and human-minutes; how many arms a first run buys (the full five-arm design is the ceiling, not the entry point).

## Forces

- **Operator repair can hide the cost of an arm.** Record who intervened on the matched tasks, what they decided, and how long it took. Decisions and minutes describe the effort in this comparison; neither supplies a universal unit of judgment.
- **Oracle validity.** "Useful and warranted work" has no hard oracle, and [an automated judge's warrant would be bounded by what it can assess](../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md); fresh-context judge panels, downstream escaped-error counts, and human blind grading have different validity/cost profiles, and the choice is itself a proxy decision.
- **Contamination.** The public repository, and any model trained after it, poisons arm 5 in the framework's favor or against it depending on what was absorbed; the KSI-shaped arm inherits the same problem across model families.
- **Operator inclusion.** The declared pathway is human-inclusive; ablating the framework while keeping the same experienced operator leaves the internalized methodology in place — the operator has absorbed the theory even where the model has not.
- **One-bit yield per run.** Each task-arm pair exercises a whole configuration; small N invites reading noise as signal, and the cost of informative N is the main reason this stays a proposal rather than a plan.

## Operativity and warrant

Adoption produces a protocol document and, once run, a results report consumed as evidence in `kb/reference/` — evidence force, not instruction force; no behavior-determining organization changes until someone acts on the results. If any arm uses automated judges, the judges' oracle warrant must be stated per the criterion they apply and is itself part of the protocol's reviewable surface. "No consumer yet; the protocol must be authored" is the current operativity answer for every option.

## Adoption criteria

- A named decision the result would change — which mechanism gets retired, doubled, or left alone at which outcome — stated before the protocol is authored; an experiment no decision consumes is not worth its cost.
- A priced first run: task count, arms bought, human-minutes metering method, and judge validity argument, small enough to actually happen.
- The contamination and operator-inclusion confounds explicitly handled or explicitly accepted in the protocol, not discovered after.
- Agreement on what a null or adverse result commits the project to reporting — the objective was declared so that failure could be visible; the protocol must not launder it.
