---
type: types/note.md
description: "Standing query on how to judge whether a KB note is worth keeping or selecting as autonomous production grows, beyond repo and collection goals."
---

# How do we value notes?

## Stakes

Root `AGENTS.md` and each collection's `COLLECTION.md` set baseline scope and quality bars, such as [explanatory-reach](../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) (how broadly an explanation transfers beyond the cases that produced it) in `kb/theory/` or fidelity and economy in `kb/reference/`. Those goals decide what a collection admits in principle, but they do not exhaust how to rank, keep, or reject candidate notes.

The question becomes urgent as autonomous production increases note volume. Every retained artifact adds maintenance, navigation, and exposure cost; [maintenance capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md). Without a clearer way to distinguish high-value notes from merely valid ones, autonomous authoring can accumulate well-formed clutter faster than review and curation can keep up.

This query stays open as long as candidate selection relies on ad-hoc judgment rather than a tested valuation practice; it would narrow or retire once Commonplace adopts and validates an explicit selection mechanism.

## Current answer

Commonplace currently spreads note valuation across five partial lenses rather than one rule:

- **Admission and answerability.** A note enters a knowledge collection only when it is [answerable](../reference/definitions/answerability.md): its contract can name what referent or outcome it answers to, what correctness or currency property it asserts, and what discrepancy triggers revision or retirement.
- **Validity separate from value.** [Choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md): a note can be grounded and coherent yet redundant or too narrow to justify its maintenance cost. Similarly, [a claim's test record does not determine its fit in a working theory](../theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md) separates whether a claim is well-tested from whether it helps the current theory handle its problem.
- **Reader update and comparative work gain.** For substantive writing, [warranted reader update is the objective of substantive writing](../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) asks what nontrivial change the note warrants relative to the intended reader and existing KB beyond a generic treatment. [Defining improvement for open-ended work](../theory/defining-improvement-for-open-ended-work.md) grounds that test in expected downstream work and compares adding a note against a cheaper alternative such as adding a link to an existing record.
- **Counterfactual use in live work.** Where no fixed oracle decides theory fit, [system use is an initial selection environment when theory fit lacks a fixed oracle](../theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) looks for counterfactual effect: whether withholding or replacing a note actually changes search, diagnosis, decisions, or recovery.
- **Structural and curation proxies.** For ranking at scale, [notes need quality scores to scale curation](../theory/notes-need-quality-scores-to-scale-curation.md) and [quality signals for KB evaluation](../theory/quality-signals-for-kb-evaluation.md) combine structural maturity (type), review verdicts, recency, and link-strength-weighted inbound links.

## Unsettled

- **Root questions versus sub-questions inside notes.** Weighted inbound links measure reuse when one note answers a local sub-question raised inside another note — what Commonplace's reader-need labels (`grounds`, `mechanism`, `defined-in`, `evidenced-by` in [link vocabulary](../reference/link-vocabulary.md)) already express. Thinking also organizes directly around recurring **root questions** rather than a single claim. Without explicit query-centered notes as roots, a top-level note that answers a live question can look orphaned if no other claim cites it, while a tightly linked cluster can answer each other's sub-questions in a closed loop without serving any real inquiry. We have no established way to represent query-centered root notes or propagate value from them down through answering notes and their subroutines.
- **Asymmetric selection pressure under autonomous production.** Structural validation, source grounding, and critique gates check validity more strongly than anything checks learning value or reader update. Under the conjecture that [weakly discriminated qualities tend to be underselected](../theory/weakly-discriminated-qualities-tend-to-be-underselected.md), an autonomous authoring loop can enrich accepted notes more strongly for validity than for usefulness, and if production favors fluent local additions, clutter can accumulate.
- **Cold-start selection at admission.** Inbound links and counterfactual system use only become observable after a note has been retained and used. Autonomous production needs a way to filter, quarantine, or trial new candidates before those downstream signals exist.
- **Combining dimensions without Goodharting.** Even where several signals exist (reader update, subroutine reuse, demand-root coverage, counterfactual use, maintenance cost), we do not yet know how to weigh them or when a coarse triage check outperforms a composite score.

---

Relevant Notes:

- [Choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — see-also: separates trustworthiness from whether a candidate earns its maintenance burden
- [Warranted reader update is the objective of substantive writing](../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) — see-also: defines substantive writing value relative to the reader's prior and existing KB
- [Notes need quality scores to scale curation](../theory/notes-need-quality-scores-to-scale-curation.md) — see-also: candidate structural and review signals for ranking notes as the corpus grows
- [System use is an initial selection environment when theory fit lacks a fixed oracle](../theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) — see-also: counterfactual use in live work as a selection signal when no fixed oracle exists
- [Answerability](../reference/definitions/answerability.md) — evidenced-by: Commonplace's admission invariant naming referent, asserted property, and revision trigger
