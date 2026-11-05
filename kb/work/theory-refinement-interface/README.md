# Workshop: theory refinement as an interface

## Goal

Reconcile the [interface investigation](./theory-refinement-interface.md),
which proposes derive, compare, locate, revise, evaluate, and apply as the
operations any theory-refinement machinery must implement, with the
established theory-refinement literature, without claiming the generic
refinement loop, tentative theories, or revision search as new. The
investigation's own claims that every operation is available for any
readable representation, that the interpreted update space is open, and
that certain classical results transfer at task level need source and
mechanism checks before any of it is promoted.

The reason to do this work is the account it would give of why language
models change the possible scope of theory refinement without solving it:
in a symbolic system the operations have mechanically assigned semantics; in
a model-mediated system the same operations are interpreted and therefore
fallible; codification progressively moves particular operations back from
interpreted to mechanical. That account describes Commonplace's own
construction and is a candidate for an article once it is grounded.

Posed by the operator on 2026-09-17 as closing condition 3 of
the theory-builder workshop (adoption recorded in git commit `28a2ea8d`),
moved here so its promotion and terminology migration can close independently.

## What closes the workshop

1. Each of the six operations has a stated task-level description separated
   from any implementation guarantee, with the classical result it restates
   named and the condition under which the restatement holds. A trace
   identifies candidate repair locations without guaranteeing a unique
   fault; a particular search algorithm's local-optimum result is not a
   theorem about all implementations of the roles.
2. The claims that need source checks are checked against the completed
   ingests, including EITHER, FORTE, the AGM and belief-base papers, the
   assumption-based TMS, and the knowledge-engineering method-construction
   papers, and each is kept, narrowed, or dropped with the reason recorded.
3. The reconciled account is either folded into the
   [addressable-theory definition](../../theory/definitions/addressable-theory.md)
   as a section on the classical repair interface, or promoted as its own note
   with the definition linking it. It does not define membership in a
   [theory builder](../../theory/definitions/theory-builder.md).
   The investigation file is then deleted.

## Evaluation boundary

Evidence is the investigation file as moved here, the addressable-theory
definition, the theory-builder definition, and the source ingests
named above. The exploratory
[ideal-interpreter workshop](../ideal-interpreter/README.md) owns the
question of modelling the LLM as an interpreter of semantics; this workshop
does not reopen it, and nothing here may depend on it.

Write scope while open: this directory only.

## Received question

From [open-ended-work-economics](../open-ended-work-economics/README.md),
direction 4 of its [reconciliation map](../open-ended-work-economics/reconciliation.md),
delivered 2026-11-05: for each of the six operations, what does it cost
interpreted versus mechanical, and does reuse across theories amortize the
cost of making it mechanical? The economics workshop found the interface
asks expressiveness and guarantee questions but not this cost question,
and records that a gap in scope, not a disagreement. Domain examples are
evidence for the architecture-level conjecture and stay with
[its proposal](../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md).
The same map notes that several operation lists coexist unreconciled (this
interface, the discovery lifecycle's six phases, the theory-builder Boundary
list, the reflective operation profile, the change-operations catalogue);
reconciling them is a separate question this workshop may take or decline.
