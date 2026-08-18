---
gate_id: semantic/epistemic-status-blur
name: Epistemic status blur
description: 'Claims of different epistemic status — observation, derivation, proposed mechanism, conjecture — read with uniform confidence, or support for one claim is presented as covering another.'
type: kb/types/review-gate.md
lens: semantic
watches: [title, description, body]
staleness: changed
---

## Failure mode

The note mixes claims with different support — reported observations, consequences derived from stated premises, proposed mechanisms, conjectures — but the prose presents them with uniform confidence, so a reader cannot recover which claim carries what support. A variant of the same failure is spread: evidence that attaches to one claim is presented, by wording or placement, as if it licensed a neighbouring claim it does not support. One document may legitimately combine all of these statuses; the failure is collapsing them, not mixing them.

## Test

1. Inventory the material claims — the assertions doing argumentative work, not transitions or illustrations.
2. Classify each claim as the note presents it: reported observation or result; consequence derived from stated premises; proposed mechanism or explanation; conjecture or hypothesis.
3. Check recoverability: can a reader assign each load-bearing claim its status from the text? Formal labels are not required — a "may", "we conjecture", a working-hypothesis phrase, a Scope entry, or an Open Questions entry suffices, as does placement in a clearly named hypotheses section. Conjectural force stated once in the title, description, or opening covers the claim it governs.
4. Check spread: for each cited or reported piece of support, identify which claim it supports. Flag places where wording or adjacency presents that support as establishing a different claim — a proposed mechanism inheriting the confidence of the observations it was proposed to explain is the canonical case.
5. Do not repair. Judge the presentation on the page, not a relabelling that would fix it.

WARN when a load-bearing proposed mechanism or conjecture reads as established, or when support that attaches to one claim is presented as covering another. INFO when statuses are recoverable but only through effortful reading — markers exist but are distant from the claims they govern.

Do not flag here: an honestly-presented claim whose scope exceeds its support (`semantic/unwarranted-scope` — a status can be accurate while the scope overreaches); a claim ambiguous between materially different readings (`semantic/underspecified-assertions`); a citation that does not say what the note claims (`semantic/grounding-alignment`); hedging language added to dodge counterexamples without improving the explanation (`semantic/explanatory-reach`, ad-hoc accommodation).

## Example (fail)

A note reports latency measurements from one deployment, proposes queue saturation as the cause, and then builds its recommendation on the queue mechanism using the same declarative register throughout: "Saturation begins at 80% utilisation, so schedulers must reserve headroom." The measurements are real; the mechanism is a hypothesis; the recommendation reads as if both were measured. Nothing on the page lets a reader separate them.

## Example (pass)

The same note, with the mechanism marked: "The measurements are consistent with queue saturation — the working hypothesis this note adopts — and if saturation is the cause, schedulers should reserve headroom." The observation, the hypothesis, and the derived recommendation each carry their own status, without any formal labelling apparatus.

---

Relevant Notes:

- [Mixed epistemic status must be preserved below the document level](../../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) — rests-on: the preservation requirement this gate enforces
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: warrant is tracked below the document level, so a document-level confidence register misreports the claims it covers
