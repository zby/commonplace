---
description: "Human-inclusive boundaries make nearly every maintained system reflective, so classification barely discriminates; the discriminating axis is autonomy — how much of the loop runs without a human"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, reflective-systems]
---

# Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient

The [reflective-system definition](./definitions/reflective-system.md) permits human-inclusive boundaries: people count as internal components when they occupy an established role in the causal path. That permission is deliberate and well-sourced, but it makes the bare classification nearly free — so cheap that it barely discriminates. What discriminates among reflective systems is **autonomy**: the extent to which the reflective loop's functions run without human mediation.

## Why the classification is nearly free

Run any maintained software system through the definition's five requirements with its development team declared inside the boundary, and all five pass:

- **Boundary.** The dev team is an established role, not a post-hoc outsider who rescued a failed process. The definition's guards exclude boundary gerrymandering — expanding the boundary after a failure so any helpful outsider counts — but they do not exclude a standing maintainer role.
- **Represented aspects and self-representation.** The source code represents selected aspects of the system's own behavior.
- **Internal processes.** Developers inspect the code and act through it.
- **Causal connection.** Editing the source, building, and running changes later behavior; and observed behavior feeds back into edits.

So under a human-inclusive boundary, essentially every maintained software system classifies as reflective. The mechanism is that humans are already reflective: declaring one inside the boundary imports that reflectivity wholesale, and the bare classification collapses to "someone maintains it." This is not a defect in the definition — its guards block boundary gerrymandering, not standing maintainer roles — but a classification meant to carry information needs a second, discriminating dimension. Membership in the class is not that dimension; position within it is.

## The gradient is autonomy

The discriminating dimension is autonomy, and it is assessed per function. Take the change loop's decomposition — search, evaluation, retention, [since governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — together with each read of the self-representation, and for each ask: does a human or a non-human process perform it?

- **Zero end — software plus its dev team.** The machine consumes the code only by executing it, never *as a representation of itself*. Every reflective act — noticing what to change, judging a candidate, deciding what to keep — happens in human heads; the artifacts merely store the results. This is fully reflective under the human-inclusive boundary and fully un-autonomous.
- **Middle — Commonplace.** In [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md), the harness loads skills and `CLAUDE.md` automatically, validators enforce type specs, and agents retrieve notes mid-task and derive behavior from what they find — non-human processes consume the self-representation *as a representation*. Humans keep search (noticing what is worth changing) and the judgment-heavy part of evaluation.
- **Far end — the Gödel machine.** [Gödel machines internalize every function behind a proof gate](./goedel-machines-are-a-proof-governed-case-of-self-modification.md): search, evaluation, authority, and retention all run without human mediation.

## What bounds the gradient

Autonomy in evaluation extends only as far as mechanical verification reaches, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). A system's autonomy profile therefore tracks its verification profile. This predicts *where* the human sits: Commonplace's human occupies exactly the positions where evaluation is judgment-heavy and cannot be checked mechanically, and the Gödel machine reaches full evaluation autonomy only by restricting acceptance to what it can prove under its formalization.

## Distinguish from sibling gradings

Autonomy is one of several graded refinements over the same reflective-system base; they answer different questions and move independently.

- **Coverage** grades *what is represented* — per representational form and operation depth, [since reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
- **Closure** grades whether the methodology *settles the meta-decisions a change raises*, regardless of who walks the governed route, [since a methodology governs its own extension only as far as it settles them](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).
- **Autonomy** grades *who performs the functions*.

A system can move on any one axis without moving on the others: it can widen coverage while keeping a human at every judgment, settle more meta-decisions without automating any of them, or hand a function to a machine without changing what is represented.

## Scope

- **Per-function and boundary-relative, not global.** Autonomy is assessed function by function against a declared boundary; there is no single scalar for a whole system, and moving the boundary moves the readings.
- **Not a merit order.** More autonomy is not automatically better. The Gödel machine buys full autonomy at the price of ignoring every improvement it cannot prove; a mid-gradient system that keeps a human at the unverifiable gate may be the correct design.
- **Reflection remains the qualification; autonomy is the position.** This preserves the definition's exclusion that *reflection is not autonomy*. Classification answers whether the system is in the design space at all; the gradient answers where in the space it sits. They are different questions, and conflating them is what makes the bare classification look empty.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: the human-inclusive boundary extension whose consequence this note states
- [Governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — grounds: the function decomposition autonomy grades over
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — contrasts: a sibling grading over forms rather than performers
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — contrasts: closure grades the methodology's settledness, not the performer
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the full-autonomy corner of the gradient
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: what limits autonomous evaluation
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: a mid-gradient occupant with the human at the judgment-heavy gate
