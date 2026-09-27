---
description: "Weco separates autonomous improvement, human-baseline gains, better improvers and accelerating returns; its outcome ladder leaves theory-builder membership open."
source: https://www.weco.ai/blog/4-levels-of-recursive-self-improvement
captured: "2026-09-27"
capture: trafilatura
capture_scope: partial-source
genre: conceptual-essay
snapshot_sha256: 3209389947ae9b4b10a7f14871a8b12a5a217ace1efafc7fab29db78b70e76a3
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [recursive-self-improvement, research-productivity, evaluation]
learning_claims: true
---

# Ingest: 4 Levels of Recursive Self-Improvement

## Classification

A conceptual essay proposing an outcome-based classification and measurement protocol for recursive self-improvement. It refers readers to a separate AIDE² results article rather than presenting that experiment here. Author: Weco Team, the organization developing the system that the framework is meant to assess; this gives the account direct relevance to Weco's intended claims and a stake in their framing.

## Summary

Weco distinguishes four levels of recursive self-improvement against a human-led research baseline: autonomous research that remains less efficient than humans; sustained, transferable gains that exceed that baseline under a fixed physical budget; a successor that becomes a better improver than its predecessor; and feedback strong enough to overcome diminishing returns so successive gains grow at fixed effort. The central distinction is between improving task performance and improving the process that produces future improvements. The proposed test for the latter lets the successor conduct another improvement campaign and compares its result with what the predecessor could produce at the same budget. The essay tentatively places existing systems on its ladder and links a separate AIDE² results report. It does not establish those placements or demonstrate accelerating returns in the retained text.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source provides the outcome criteria needed to separate Weco's recursive-improvement claims from the KB's [theory-builder definition](../notes/definitions/theory-builder.md). Its ladder concerns research productivity, whereas membership depends on stated content, its consumption, criticism directed at that content, and uptake into later rounds. Neither classification establishes the other.

Its successor-versus-predecessor campaign test closely matches the need to test [compounding in later improvement episodes](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Compared with [the distinction between accumulation and compounding](../notes/improvements-can-accumulate-without-compounding.md), Weco adds a human-baseline requirement and separates better improvers from acceleration despite diminishing returns. These are related classifications, not interchangeable thresholds: a local causal contribution to later improvement could count as compounding in Commonplace without establishing Weco's sustained advantage over humans.

## Learning Claims (our opinion)

The proposed mechanism is feedback from research into the capacity of the researcher. A system first produces improvements, then promotes an improved version into the role of researcher. If the successor produces better later improvements at equal budget, the feedback has improved research capacity; if successive gains also grow despite harder problems, the stronger acceleration claim is met. The essay distinguishes transfer from an optimization measure to other tasks from transfer to the ability to improve again. This sharpens the evaluation of learning without prescribing its implementation.

Against the four theory-builder conditions, the evidence remains uneven. **Localized content:** the Level 0 description says the system forms hypotheses, but supplies no retained examples or representation sufficient to establish localized theories. **Consumption:** improved versions taking over research establishes the intended use of a changed system, but does not show stated theories guiding decisions through their content. **Criticism:** running experiments is compatible with tests of stated consequences, but the essay does not establish stated criticism aimed at identified content; selection by score would also fit its ladder. **Iteration:** version succession establishes the intended reuse of improvements across campaigns, but does not establish retention and uptake of criticism. Persistence is specified conceptually across generations of a research campaign; the storage mechanism and persistence across unrelated problems are not given. Membership therefore remains open, rather than failing on evidence of absence.

The framework also leaves model weights, harness code, feedback representations and permitted revisions unspecified. It neither requires nor demonstrates fixed-model learning, a particular outer/inner-loop architecture, or reflection in Commonplace's sense. A method can become a better improver through selection without criticizing stated claims about its own methods. The source's concern about the limited ceiling of narrow optimization is compatible with the [limits of a fixed update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), but it does not compare alternative decompositions or show which boundaries AIDE² can revise. Its contribution is a proposed test of improved future capacity, not evidence that a particular mechanism passes it.

## Extractable Value

1. **Keep outcome claims separate from theory-builder membership.** The Weco/AIDE² case can use the ladder to distinguish automation, advantage over humans, improved research capacity and acceleration while assessing content-directed criticism independently. The essay supplies the intended outcome meanings, not the implementation evidence. [quick-win]
2. **Compare successor and predecessor on later improvement.** A matched-budget campaign supplies a concrete candidate test for feedback into research productivity. Applying it requires defining the shared starting state, research opportunity and resource accounting so an easier campaign does not explain the gain. [experiment]
3. **Separate transfer to other tasks from transfer to improvement work.** Success beyond the optimization measure does not by itself show that the researcher became better at improving. This is a useful qualification when interpreting generalization results as compounding. [quick-win]

## Limitations (our opinion)

The capture is partial: it retains the essay's text but not its interactive graphics. The reported semiconductor productivity trend and the presentation of the plotted comparisons cannot be checked from those omitted displays. The historical claims about research productivity and biological versus machine feedback are motivation rather than tests of the proposed ladder.

The ladder gives useful distinctions but leaves operational choices unresolved: how to compare human and machine budgets, what counts as sustained improvement, how much transfer establishes generality, and which performance scale makes increasing gains meaningful. Its tentative placements of other systems are author judgments, not matched comparisons shown here. Weco's claim that recursive self-improvement is likely to lead to an intelligence explosion receives no probability estimate or supporting test in the retained text.

A better successor outcome could reflect a better starting system or a different research opportunity rather than increased improvement productivity. The proposed same-budget comparison addresses expenditure, but causal interpretation still needs matched campaign conditions and a clear measure of additional gain. No experiment here tests that distinction. The separate AIDE² results, implementation details and any evidence of stated criticism must be assessed from their own sources.

## Recommended Next Action

Use this essay's outcome distinctions when drafting the Weco/AIDE² case in `kb/articles/which-existing-self-improving-systems-are-theory-builders.md`, keeping its theory-builder judgment dependent on separate evidence of the system's criticism and revision process.
