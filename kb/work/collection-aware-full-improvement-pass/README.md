# Collection-aware full improvement pass

## Goal

Determine how Commonplace should improve existing prose outside `kb/notes/` without imposing a theory-note contract on artifacts that serve a different function. Any resulting procedure should respect the target collection, artifact type, local framing, quality goal, unresolved choices, and decision authority before it selects review methods or applies edits.

The workshop must also decide whether this should be one routed full-improvement procedure, a small family of collection- or artifact-specific procedures, or a narrower note-only procedure with report-only support elsewhere. Starting the workshop does not select among those designs.

## Why this workshop exists

[`run-full-improvement-pass-on-note.md`](../../instructions/run-full-improvement-pass-on-note.md) grew out of the [agent-note-improvement workshop](../agent-note-improvement/README.md) and was calibrated on theoretical library notes. Its method order, contribution packet, claim critique, premise attack, title reframe, and closing cycle are correspondingly note-shaped.

A later run applied it to a proposed experiment design in a live workshop. The pass improved organization, terminology, and the visibility of the comparison. It also converted implicit workshop text to a `note`, treated the design alternately as a claim and a procedure, and turned several reviewer-supplied experimental choices into the artifact's own prescriptions. The result was coherent on its new terms, but the closing checks did not establish that those terms were authorized by the workshop. [Case 01](./case-01-workshop-experiment-design.md) records the evidence and keeps the design response open.

This is not evidence that the current pass is defective for the theoretical notes it was built to improve. It is evidence that successful note editing does not by itself establish cross-collection method fit.

## Question

What applicability, review-routing, synthesis, mutation, and closing contracts let a full improvement pass advance an artifact according to its own collection and function rather than making every target resemble a theoretical claim note?

## Evaluation boundary

The workshop concerns authored natural-language artifacts that their governing contracts permit an agent to revise. It includes system-definition prose, such as instructions, only if a candidate design accounts for its binding behavioral effects, authority, and appropriate validation.

The workshop may investigate:

- how a pass determines its governing collection, type, local framing, artifact function, and quality goal;
- which artifact shapes are eligible for automatic editing, report-only diagnosis, or refusal;
- how review methods are selected or omitted for claims, descriptions, procedures, designs, workshop records, and other demonstrated shapes;
- how synthesis distinguishes presentation changes, clarifications, qualifications, and new substantive commitments;
- which changes require authorial or maintainer authority, including type conversion, promotion, rehoming, disposition, and selection among free parameters;
- what a packet must record so a later reader can audit both editorial quality and contract fidelity; and
- how final-byte review should vary when the target is not a theoretical note.

The workshop does not assume that every Markdown artifact should be eligible. Captured sources, generated indexes and reports, code or other symbolic artifacts, and collection contracts themselves stay outside the claimed scope unless a worked case establishes a specific reason and review method for including them. The workflow must not change a collection contract merely to make a target pass.

## Evaluation dimensions

A candidate design should be judged separately on:

1. **Applicability:** it identifies the binding contract and artifact function before expensive or mutating work.
2. **Method fit:** its reviewers ask questions that apply to that artifact rather than translating it into a familiar note shape.
3. **Contract fidelity:** the result still serves the local quality goal, role, maintenance semantics, and closure conditions.
4. **Commitment preservation:** it does not silently choose free parameters, add claims, change type, or expand authority.
5. **Material improvement:** the edit makes the artifact better for its actual use, not merely more note-like or more internally polished.
6. **Auditable restraint:** report-only and refusal outcomes remain successful outcomes when mutation is not authorized or the intended contribution is underdetermined.
7. **Closing validity:** reassessment tests the resulting artifact against the same governing contract and records residual uncertainty without certifying more than it checked.

These dimensions are deliberately non-collapsible. A fluent final artifact can improve materially while still failing commitment preservation, as Case 01 appears to have done.

## Open design decisions

The workshop has not yet chosen:

- one routed procedure versus separate procedures or adapters;
- whether the current note pass should remain unchanged, gain an early eligibility guard, or become a specialization of a broader workflow;
- whether artifact function is declared, inferred, or jointly determined from collection, type, and local framing;
- the minimum evidence needed to classify a proposed edit as clarification rather than a new commitment;
- the default mutation policy for workshop artifacts and binding instructions;
- the packet vocabulary for non-claim contributions and non-library closure conditions; or
- which existing review methods can be reused unchanged, which need an artifact mode, and which should simply be inapplicable.

These choices should be made from worked cases, not settled in the framing file.

## Case bookkeeping

Number cases as `case-NN-<slug>.md`. Each case should record:

- the frozen input identity and final output identity;
- the governing collection and type contracts plus any nearer framing artifact;
- the artifact's working function, open choices, and relevant decision authority at pass start;
- what the procedure was allowed to change and what it was not authorized to decide;
- mechanical execution results separately from editorial quality, semantic change, and contract fidelity;
- observations separately from diagnoses and design decisions; and
- whether the case informed, selected, or merely failed to rule out a candidate design.

Use frozen copies or versioned captures when a trial might mutate an artifact. Do not infer authorization to edit a live target merely because the target is in a mutable collection.

## What would close this workshop

The workshop closes when it has:

- decided, from worked comparisons, whether to retain a specialized note pass, introduce routing or adapters, or ship separate procedures;
- tested every collection/profile and artifact function that the selected design claims to support, including at least one held-out case for each supported non-theoretical profile;
- defined preflight, method-selection, commitment-preservation, mutation-authority, packet, and closing behavior, including explicit abstention paths;
- shown that the selected workflow improves its supported cases without unapproved type changes or substantive free-parameter selection;
- landed the resulting durable instruction, reference, type, gate, or ADR changes with the appropriate validation; and
- named unsupported artifact classes explicitly rather than implying universal Markdown support.

A negative result can also close the workshop: the current pass may remain intentionally theory-note-specific if broader routing does not improve artifacts reliably enough to justify its complexity. After durable conclusions are extracted, remove this workshop and its entry from `kb/work/README.md`.

## Starting evidence

- [Case 01: workshop experiment design](./case-01-workshop-experiment-design.md) — the motivating cross-contract run.
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — current operative procedure and baseline.
- [Full improvement pass closure](../../reference/full-improvement-pass-closure.md) — closing behavior calibrated on substantive note edits, with an explicit warning against generalizing it to arbitrary transforming workflows.
- [Design proposals differ from claims in kind, not confidence](../../notes/design-proposals-differ-from-claims-in-kind-not-confidence.md) — why proposal review needs problem, forces, free choices, and adoption criteria rather than claim contestability alone.
- [Workshop collection contract](../COLLECTION.md) — the local quality goal and prohibition on adding note structure merely for conformity.
