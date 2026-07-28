---
description: "A summary shortens, claiming a subset of its episodes; a distilled theory posits a mechanism covering unseen cases, claiming more than they entail — opposite directions, different debts, conflated as 'compressing traces'"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, discovery]
---

# A summary claims less than its episodes; a distilled theory claims more

Two operations get conflated under "compressing traces into lessons," and they point in opposite epistemic directions. **Summarization** selects and shortens: its output claims a subset of what the episodes already claimed, and its reach can never exceed its input's, because discarding detail is all it does. **Theory-formation** posits: "tests that read the wall clock flake, so freeze the clock" asserts a mechanism that covers tests not yet written — content nothing in the traces entails. Since [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md), the distilled theory is ampliative — it adds unentailed resolutions — which is exactly why it can carry [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) and exactly why a summary cannot: monotone loss versus conjectured gain.

The asymmetry sets different debts. A summary owes fidelity, checkable against its episodes. A theory owes [reach-assessment](./definitions/reach-assessment.md) — it can only be tested against cases that could refute it — a debt a summary never incurs because it never makes the claim. This is why the learning operation of an artifact loop is [conjecture](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md), not compression: no amount of compression produces the thing the loop is aimed at, and a pipeline whose only condensation operator is "shorten" has no proposal operator at all. The bet that a language model can perform the conjectural operation to a useful extent is [openly a conjecture of its own](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — but it is a bet on a different operation than the one summarization pipelines run.

## Compression before attribution destroys what attribution needs

The distinction also sorts *when* condensation is safe. Inside an improvement loop, credit assignment needs the coupling between specific events and outcomes, and uniform shortening destroys precisely that — [the "why" is cheap to record at the decision surface and hard to recover from condensed state later](./structure-inference-needs-capture-at-the-decision-surface.md). After attribution — once the lesson is identified and its boundary [statable](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — condensation is a different act performed on different input. Two-layer retention follows: [the episode is kept beside the distilled rule](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) so attribution and re-derivation stay possible, while [raw history stays out of the default context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) so the theory, not the trace, is what future behavior runs on.

## The objection that compression is generalization

The MDL tradition identifies the best compression of data with its best explanation, so a critic can say the distinction collapses. It identifies theory-formation with compression-as-search-for-a-generative-model — a theory-space search under a formal criterion, which is this note's *theory* side, not its summary side. "Summarize this trace" elicits truncation, not model search, and the gap is measurable: [frontier LLMs summarize fluently while scoring near zero on recursive compression-as-abstraction](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md). The operative boundary is not compression versus theories but discarding detail versus positing a generator.

## What the Meta-Harness result does and does not bound

[Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) ran the controlled version: its harness-search proposer fed raw execution traces beat both scores-only and scores-plus-summary feedback by 15+ points median, [and the summaries actively hurt](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — scores-plus-summary trailed even scores-only on best-found accuracy. The paper's own account is this note's channel claim stated empirically: summaries "compress away diagnostically useful details" — they preserve the salient pattern while discarding the unexpected detail that diagnosis runs on. The result is real and it binds: any pipeline feeding summaries to an attribution consumer, potentially including this KB's own distillation workflows, is challenged by it. What the result does not bound is theory-formation, because no arm made it the condensation operator — the summaries were LLM-generated trace digests, not posited mechanisms with stated scope. Notably, the *winning* arm contains the conjectural operation in transient form: the proposer is instructed to read raw traces, infer failure modes, and formulate hypotheses — conjecture over full episodes, feeding code candidates, retained nowhere as scoped theory. Reading the ablation as "condensing traces fails as learning" samples the condensation design space at its weakest point. Whether gated, conjectural condensation preserves what trace summaries lose is untested there and open here — this KB's condensation-faithfulness experiment (a live workshop) is the designed test, and until it runs, this note licenses a reading discipline for compression results, not a victory over them.

## Scope

- The boundary tracks the operation performed, not the word used: a "summary" produced under selection criteria that posit which regularity matters is partway to abstraction, and a "theory" that merely restates its episodes in fewer words is a summary in costume. What an artifact claims about unseen cases, and whether it carries a boundary, is the discriminator.
- Nothing here says summaries are worthless — they are cheap, low-debt retention for material whose value is record-shaped. The claim is that they are a different operation from learning, and that experiments testing one must not be read as bounding the other.

## Open Questions

- Is the discriminator checkable — given an artifact, can a gate decide whether it asserts unseen-case coverage and carries a boundary, separating theory from summary mechanically?
- Does the raw-trace advantage in harness search survive when the proposer is fed distilled theories plus retained episodes, rather than summaries — the arm neither Meta-Harness nor anyone else has run?

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: the ampliative addition that separates a posited theory from any derivation-preserving reduction of the episodes
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: reach as the property only the ampliative operation can produce
- [Conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — grounds: the operation theory-formation actually is
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the debt a theory incurs and a summary never does
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: the open bet that models can perform the conjectural operation well enough to pay
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — extends: two-layer retention gets its attribution justification — the episode is what credit assignment and re-derivation consume
- [Preserve evidence without loading history](./agent-memory-requirements/preserve-evidence-without-loading-history.md) — grounds: the channel separation — evidence retained for extraction, theory consumed in operation
- [Structure inference needs capture at the decision surface](./structure-inference-needs-capture-at-the-decision-surface.md) — grounds: why the coupling attribution needs cannot be recovered from condensed state
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: the gate that makes condensation-after-attribution a different act than shortening
- [Reverse-compression is when LLM output expands without adding information](./reverse-compression-is-when-llm-output-expands-without-adding.md) — contrasts: the mirror failure — expansion without structure, where this note's failure is reduction without conjecture
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidenced-by: the code-grounded review — the proposer reads prior results and raw traces, formulates hypotheses, and writes candidates; its conjectures are transient, never retained as scoped theory
- [Meta-Harness paper ingest](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidenced-by: the controlled ablation — full traces beat scores-only and scores-plus-summary by 15+ points median, summaries actively hurt, and the paper attributes it to summaries compressing away diagnostically useful detail
- [SuperARC AIT benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — evidenced-by: the measurable gap between fluent summarization and compression-as-generative-abstraction
