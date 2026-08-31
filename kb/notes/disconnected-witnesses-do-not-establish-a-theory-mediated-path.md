---
description: "Theory use, outcome, theory revision, and later use establish theory-mediated learning only when their witnesses identify the joins of the same full causal path"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems, evaluation]
---

# Disconnected witnesses do not establish a full causal path through theory

Theory-mediated learning is a claim about a connected causal path, not a checklist of events that happened somewhere in the same project. Evidence that a theory existed, a decision occurred, an outcome followed, the theory later changed, and a later operation used some retained state does not by itself show that learning proceeded through that theory. The witnesses must identify the joins that make those events one full causal path.

The strongest path has this shape:

```text
theory state T0
  -> theory-mediated decision or search
  -> realized change
  -> independent or delayed consequence
  -> read-back against T0
  -> revised theory state T1
  -> later operation consuming T1
```

This shape composes three existing requirements. [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md): the functions must share a causally integrated, co-indexed path even when they use different substrates. [Citing retained theory at the decision point is a mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md): a contemporaneous record can identify which retained theory a decision claims to have consumed, but citation alone does not establish load-bearing use or outcome read-back. And [history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md): when a nondeterministic production path cannot be re-derived, transient facts needed to identify its joins must be converted into carried records while they remain available.

## Each join supports a different inference

The first join identifies **mediation**: which theory state entered the decision whose behavior is being attributed to theory. A retrieval log or later citation to a generally relevant theory is weaker because it need not identify what governed the decision. Withholding, replacement, or perturbation can provide stronger causal evidence for this link.

The middle joins identify **empirical contact and theory learning**: which realized change produced the consequence, and whether that consequence was read back against the theory state that helped guide the change. A failure followed by an unrelated theory edit is not evidence that the failure revised that theory. Likewise, an accepted change does not by itself verify the theory that motivated it.

The final join identifies **recurrence**: whether the revised theory state, rather than merely a descendant repository state, affected a later operation. Git ancestry can establish that later work descended from an earlier commit. It cannot by itself establish which retained theory the later decision consumed or whether the relevant revision was load-bearing.

The evidence levels therefore compose only when their identities compose. Separate demonstrations of mediation, an empirical outcome, a theory edit, and later work can each be valid partial results while failing to establish the full recurrent theory-mediated path.

## Recording follows from the evidential shape

The required record is determined by the claim rather than by a universal logging schema. To support a record-based full-path claim, the retained evidence must let a reviewer associate the relevant episode, supplied theory-state version, decision or search branch, realized change, consequence, theory-state revision, and later claimed use. Actor or operator interventions must be retained where they determine one of those joins.

For deterministic or otherwise re-derivable operations, some joins may be reconstructed by replay. For nondeterministic LLM production, omitted prompts, supplied theory components, rejected alternatives, or operator interventions generally cannot be recovered from the final artifact. Production-time recording is therefore a consequence of the full-path evidence requirement in those cases, not the theory claim itself.

The exact event schema is an operational choice. This note establishes only what a record must make identifiable if it is later used as evidence for the full causal claim.

## Scope

- A full path is the strongest recurrent theory-mediated-learning claim, not the minimum evidence for every useful theory-guided change. Mediation, empirical contact, and theory revision remain reportable partial results at their recorded strength.
- Co-indexing establishes identity across witnesses; it does not by itself establish that every link is causal. Interventions, independent exposure, and appropriate controls are still needed for the causal strength claimed.
- The path may cross model-mediated, symbolic, environmental, and human components. Full-path identity does not imply one substrate or an autonomous technical subsystem.
- The required identifiers depend on the contrast and inference. Recording more fields cannot repair an experiment that never ran the relevant contrast.

---

Relevant Notes:

- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: supplies the distinct functions, evidence ladder, and requirement that they share a co-indexed causal path
- [Citing retained theory at the decision point is a mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — grounds: supplies the observable theory-to-decision edge and bounds what a citation establishes
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: explains why non-re-derivable joins must be converted into carried evidence while available
