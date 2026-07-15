---
description: "Human-inclusive boundaries make nearly every maintained system reflective, so classification barely discriminates; the discriminating axis is autonomy — how much of the loop runs without a human"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient

The [reflective-system definition](./definitions/reflective-system.md) permits human-inclusive boundaries: people count as internal components when they occupy an established role in the causal path. That permission is deliberate and well-sourced, but it makes the bare classification nearly free — so cheap that it barely discriminates. What discriminates among reflective systems is **autonomy**: the extent to which the reflective loop's functions run without human mediation.

## Why the classification is nearly free

Run any maintained software system through the definition's five requirements with its development team declared inside the boundary, and all five pass:

- **Boundary.** The dev team is an established role, not a post-hoc outsider who rescued a failed process. The definition's guards exclude boundary gerrymandering — expanding the boundary after a failure so any helpful outsider counts — but they do not exclude a standing maintainer role.
- **Represented aspects.** The system's own structure and behavior, at the granularity the source expresses them.
- **Self-representation.** The source code, which developers read *as a description of the running system*, not merely as the input that produced it.
- **Internal processes.** Developers inspect the code and act through it.
- **Causal connection.** Editing the source, building, and running changes later behavior; and observed behavior feeds back into edits, through an established maintenance process that keeps the source true to what runs.

So under a human-inclusive boundary, essentially every maintained software system classifies as reflective, and the bare classification collapses to "someone maintains it."

The two requirements doing the work are the third and the fifth: the artifact must be consumed as a representation of the same declared whole, and a standing process must keep it true. A maintained system satisfies both by default, which is why the bar is so low — but not vacuously. A team operating a sealed third-party service, with no access to its internals and only external telemetry and vendor tickets to work through, fails both: nothing inside the declared boundary represents that service to itself, and no process the team runs keeps such a representation true. The definition still discriminates; it just does not discriminate among the systems anyone builds. A classification meant to carry information therefore needs a second dimension. Membership in the class is not that dimension; position within it is.

## The gradient is autonomy

The discriminating dimension is autonomy, and it is assessed per function. The systems compared here all improve through a proposal-selection loop, so take that loop's decomposition — search, evaluation, retention, [since a proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — together with each read of the self-representation, and for each ask: does a human or a non-human process perform it? (A direct evidence-driven pathway is graded the same way over whatever performs its updates; it simply has fewer separable functions to hand over.)

- **Zero end — software plus its dev team.** The machine consumes the code only by executing it, never *as a representation of itself*. Every reflective act — noticing what to change, judging a candidate, deciding what to keep — happens in human heads; the artifacts merely store the results. This is fully reflective under the human-inclusive boundary and fully un-autonomous.
- **Middle — Commonplace.** In [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md), the harness loads skills and `CLAUDE.md` automatically, validators enforce type specs, and agents retrieve notes mid-task and derive behavior from what they find — non-human processes consume the self-representation *as a representation*. Humans keep search (noticing what is worth changing) and the judgment-heavy part of evaluation.
- **Far end — the Gödel machine.** [Gödel machines internalize every function behind a proof gate](./goedel-machines-are-a-proof-governed-case-of-self-modification.md): search, evaluation, authority, and retention all run without human mediation.

## What bounds the gradient

*Warranted* autonomy in evaluation — running unattended and still deserving trust — extends only as far as mechanical verification reaches, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). Bare autonomy is not bounded at all: any gate can be handed to a fallible judge tomorrow. A system's *defensible* autonomy profile therefore tracks its verification profile. This predicts *where* the human sits: Commonplace's human occupies exactly the positions where evaluation is judgment-heavy and cannot be checked mechanically, and the Gödel machine reaches full evaluation autonomy only by restricting acceptance to what it can prove under its formalization.

## Distinguish from sibling gradings

Autonomy grades *who performs the functions*. It is one of three graded refinements over the same reflective-system base, alongside coverage — *what is represented*, [since reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — and closure — *what the methodology settles*, [since a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

They move independently: a system can widen coverage while keeping a human at every judgment, settle more meta-decisions without automating any of them, or hand a function to a machine without changing what is represented. Autonomy is the one that discriminates *among reflective systems*, which is this note's claim. Over the broader self-improving base a fourth grading joins them — retention form, [since reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — and [four independent gradings place a self-improving system](./four-independent-gradings-place-a-self-improving-system.md) collects the full scheme.

## Scope

- **Per-function and boundary-relative, not global.** Autonomy is assessed function by function against a declared boundary; there is no single scalar for a whole system, and moving the boundary moves the readings.
- **Autonomy is separate from merit.** It does not decide whether a system is [self-improving](./definitions/self-improving-system.md) — a human-inclusive loop still is one. More autonomy strengthens the autonomy attribution but is not automatically a better design; [warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md).
- **The gradient does not repeal the exclusion.** *Reflection is not autonomy* still holds: classification answers whether the system is in the design space at all, and the gradient answers where in it the system sits.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: the human-inclusive boundary extension whose consequence this note states
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the function decomposition autonomy grades over
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — contrasts: a sibling grading over forms rather than performers
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — contrasts: closure grades the methodology's settledness, not the performer
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the full-autonomy corner of the gradient
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: what limits autonomous evaluation
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — mechanism: the oracle limit on autonomy that remains trustworthy
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: a mid-gradient occupant with the human at the judgment-heavy gate
