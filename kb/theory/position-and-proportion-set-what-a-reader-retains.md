---
type: types/note.md
description: "Why opening placement can guide human theme identification, why LLM order effects warrant a separate test, and how to test the conjecture that support competes with a claim through disproportionate space."
traits: [title-as-claim, has-external-sources]
tags: [prose-readability, document-system]
brief: position-and-proportion-set-what-a-reader-retains.brief.md
---

# Opening position can signal a human reader's theme; proportion remains conjectural

An intelligible opening claim gives a human reader an early cue to what a document is about. This is a reason to move an obscured claim forward, not a guarantee that the reader will remember it. The related idea that supporting material can compete with the claim by occupying disproportionate space is a conjecture. Both ideas concern whether presentation points toward the intended claim, but they have different evidence. LLM judgments can be sensitive to order; the available evidence does not establish the same within-document mechanism for models.

## Position supplies a cue, not a substitute for meaning

In [Kieras's experiments on technical passages](../sources/kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md), readers' immediate main-idea statements resembled the intended theme sentence more closely when it appeared first than when it was embedded in the middle. The proposed explanation is that readers derive the theme largely from meaning, with initial mention guiding that process. Position does not completely determine the theme, and other signals can outweigh it. These were immediate judgments designed to minimize memory demands, not tests of durable recall.

Recall has separate evidence. [Freebody and Anderson's 1981 Technical Report No. 219](../sources/freebody-anderson-serial-position-rated-importance-1981.ingest.md) found that rated importance and serial position independently predicted proposition recall. The overall fitted pattern favored early propositions and, to a lesser extent, late ones. Explained variance was limited, and the pattern was uneven across individual passages. Passage features such as a concluding encapsulation could also contribute. This does not establish a causal chain in which opening placement increases perceived importance and thereby improves recall.

For LLMs, the [position-bias benchmark](../sources/position-bias.ingest.md) compared sibling story edits in both display orders. Judges sometimes changed their underlying preference after the swap. The direction varied by model, including a preference against the first-shown version. This is evidence about comparative writing judgment on those story pairs. It motivates testing order sensitivity in a document-reading task, not assuming that moving a document's claim forward improves an LLM's comprehension or retention.

## Proportion may make support compete with the claim

The conjecture is that space allocated beyond a passage's explanatory role can make its topic seem more central than the claim it supports. A reader might take extended treatment as an importance signal and identify the supporting topic as the document's theme. No position finding above tests this mechanism.

Proportion is relative to what the explanation requires. A short claim may need extensive evidence, qualifications or intermediate reasoning. That support can improve understanding rather than compete with the claim. Its role must therefore be identified independently of the reader's eventual answer: calling everything that precedes a failed answer “disproportionate” would make the conjecture impossible to challenge.

For an LLM, [the argument that context lacks enforced local scope](./llm-context-is-composed-without-scoping.md) supplies a narrower reason to investigate this possibility: labeling material as support does not isolate it from the response. It supplies no law that influence grows with token count. Human use of space as an importance cue and model influence across assigned roles remain different proposed explanations.

A test would compare matched versions with the same intended claim, essential conditions and required support. With claim placement and total length fixed, it would reallocate nonessential elaboration between the claim's explanation and a supporting branch whose role was identified beforehand. The comparison must not strengthen the evidence or remove a needed inference step. Position would be tested separately by moving the claim while preserving content.

The proportion conjecture predicts more substitutions of the supporting topic for the intended claim in the branch-heavy version. No increase, or improved claim identification, would count against that prediction under the tested conditions; the comparison and uncertainty rule must be fixed before observing results. For humans, immediate main-idea selection, later proposition recall and understanding of essential conditions would be separate measures. For LLMs, main-claim extraction or summary would be a specified task, not a durable-memory measure. Reader groups and model configurations would be evaluated separately, with presentation counterbalanced and no exposure to alternative versions. Failure caused by loss of necessary explanation would not establish competition from excess support.

## The repair must address the cause

When placement obscures a claim, moving it addresses placement directly. Shortening elsewhere need not do so. Deleting preceding material can nevertheless help by changing the claim's position or removing competing signals. The rationale favors a cause-specific edit, not brevity for its own sake; it is not a reported experimental comparison of these repairs.

Where support interrupts the reading path, an informative pointer can preserve it elsewhere. This is appropriate only when the claim remains intelligible and its essential conditions stay visible. A pointer changes immediate availability and reading effort, so its benefit needs a separate check: can the reader recover the support when needed and still understand the conditions? A shorter version's success alone would not isolate a proportion effect.

The [compression bundle](../instructions/compression-bundle/README.md) supplies procedures for reviewing placement and the role of supporting material. The rationale here explains why those questions matter without establishing that every flagged passage should be cut.

## Scope

The human placement evidence concerns tested technical passages, not every document genre. Kieras's two-topic main-item materials were explicitly unrepresentative of ordinary prose. The recall findings neither guarantee an opening advantage in each passage nor eliminate late-position advantages. The LLM benchmark used mostly general story situations and measured comparative judgment, not effects of beginning, middle or end placement inside one document.

This note concerns organization inside an opened document. [Claim-bearing titles](./title-as-claim-enables-traversal-as-reasoning.md) instead expose propositions during index scanning and link traversal, before the full note is read. Neither an informative title nor a pointer ensures that a reader follows it. The proposed proportion test remains needed for both human and LLM readers; the cited position studies motivate and bound the rationale rather than corroborate that conjecture.
