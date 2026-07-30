# ASMO: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** low

## Remembered model

I remember ASMO chiefly as an attention-centered cognitive architecture used in robotic or situated systems. I do not trust my recall of the acronym expansion, module inventory, or learning rules. The stable-looking theme is selection among competing perceptual, cognitive, and goal-relevant demands under bounded processing.

This scan therefore extracts only from that broad theme. It intentionally does not attribute a specific salience equation or component structure to ASMO.

## Provisional ontology

The concepts worth checking appear to be:

- **Attention candidate:** something that could receive scarce processing now.
- **Priority signal:** a contribution from novelty, urgency, current goals, learned relevance, or persistent commitments.
- **Selector:** the arbitration process that combines signals and commits resources.
- **Attended item/process:** the winner or small active set.
- **Inhibition or persistence:** mechanisms preventing either thrashing or permanent capture.
- **Attention shift:** a transition that should have a reason visible in the execution trace.

The important distinction is between an item's content and the reason it wins attention. A highly authoritative rule, a surprising observation, and a user-designated goal can all deserve priority for different reasons.

## Transfer candidates

- **`ASMO-1` — make context selection inspectable.** A context engine should be able to report which candidates competed, which priority sources mattered, and why a candidate was excluded. Similarity rank alone is not an attention explanation.
- **`ASMO-2` — keep priority channels typed.** Novelty, goal relevance, risk, authority, and recency should not become one uninterpretable score unless their trade-offs are explicit. Typed channels permit policy changes and postmortems.
- **`ASMO-3` — add persistence and interruption rules.** Agent loops need a principled balance between staying with the current inquiry and reacting to newly salient evidence. This could become a control-policy vocabulary: interrupt, queue, decay, or ignore.
- **`ASMO-4` — evaluate attention by opportunity cost.** A selector is not good merely because chosen items are relevant; evaluation should include important candidates that lost and the work displaced by the winners.

These are candidate refinements to [designing agent memory from consumer effects](../../notes/designing-agent-memory-systems.md): memory activation needs an arbitration story when more useful material is available than can be loaded.

## Method worth borrowing

An attention architecture encourages perturbation tests. Hold the available information constant while varying the goal, novelty, urgency, or persistence signal; then predict which item becomes active and what action changes. That is more diagnostic than measuring retrieval precision against a context-free relevance label.

## Non-transfer and failure modes

- The remembered attention theme may omit ASMO's actual distinguishing mechanism.
- A centralized selector can become a fictitious homunculus unless its inputs and decision rule are implemented.
- A single priority score can conceal normative choices about whose goal or risk dominates.
- Robot sensor salience may transfer poorly to text-heavy knowledge work.

## Grounding questions

1. What does ASMO stand for, and what problem was it explicitly designed to solve?
2. Is attention centralized, distributed, learned, or rule-based?
3. Which priority sources does the architecture distinguish?
4. What robotic or non-laboratory results actually depend on the attention mechanism?
