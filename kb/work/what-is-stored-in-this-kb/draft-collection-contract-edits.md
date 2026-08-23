# Applied COLLECTION.md edits

Execution record for the six changes applied with
[ADR 070](../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md)
on 2026-08-23. Final review added the evidence/work/log lifecycle boundary and
the `kb/agentic-systems/` route to the five originally drafted changes.

## `kb/notes/COLLECTION.md`

### 1. Replace the opening scope sentence

Replaced:

> This collection retains transferable claims about what is true — mechanisms, principles, and arguments that should hold across systems.

Applied:

> This collection retains **beliefs about the design space** — transferable truth-apt claims about how systems of this kind can work. A claim may be grounded in a particular system, including Commonplace, when the particular is bound as a substantive witness for feasibility, mechanism, or a bounded consequence. Truth-aptness of a local observation alone does not place it here.
>
> Apply the placement test to the artifact's intended contribution: **after every particular system choice it names is bound, does a substantive claim about the design space remain?** Bind a choice universally, through equivalent generic or conditional grammar, or existentially as a witness. If binding leaves only what Commonplace selected or the current or historical state that selection produced, the artifact belongs in `kb/reference/`.

### 2. Replace the Formulation constraint

Replaced:

> **Formulation constraint.** Title and opening argument must be statable in general terms, even when derived from a specific system.

Applied:

> **Formulation constraint — bind the choices you name.** The title, description, and opening argument must be statable in general terms, even when derived from a specific system. Where one of those surfaces names a choice some system made, bind it universally, existentially as a substantive witness, or through equivalent generic or conditional grammar. A system-specific term is not a free occurrence when replacing it with its general description leaves the claim's truth conditions unchanged. Existential grammar is not enough when the sentence merely restates the selected value. If no substantive claim remains after binding, move the artifact to `kb/reference/` because its intended contribution is what Commonplace selected or the state that selection produced. Claims offered as theory later in the body obey the same binding rule; explicitly scoped local reports and examples may support the theory without becoming the artifact's intended contribution.

Wording sharpened by the [bound-variable sweep](./bound-variable-sweep-findings.md), which found 0/27 failures at the title, description, and opening surfaces. The rule is not new: it makes the collection's longstanding “statable in general terms” clause operational. The sweep's later body residue is pre-existing targeted cleanup, not migration debt caused by this clarification.

Leave the adjacent **Theory-independence constraint** unchanged. It governs
citations ("must stand if any single cited description is removed"), which is
a different failure from a free choice-variable — a claim citing nothing can
still carry one.

### 3. Add one line to "What does NOT belong here"

> - Records of what Commonplace selected, and descriptions of the current or historical state those selections produced → `kb/reference/`

The former line "Descriptions of how a specific system works → `kb/reference/`
or `kb/agent-memory-systems/`" was narrowed because a bounded observation may
serve as a theoretical witness. Applied replacement:

> - Descriptions of a specific system's contract, interface, or current construction → `kb/reference/` for Commonplace, or `kb/agent-memory-systems/` and `kb/agentic-systems/` for external systems

### 4. Clarify the evidence/work/log lifecycle

Applied replacement for the evidence-placement paragraph:

> Use `kb/notes/evidence/` when a note's primary contribution is what a bounded dataset, experiment, trace cohort, or comparative casebook establishes about the design space. These remain theoretical notes under this collection contract: state both the inference the evidence supports and its limit. The larger theory may still be incomplete, but the evidence artifact must make its own bounded inference. Keep observations whose theory-facing inference is unresolved in `kb/work/`; put first occurrences and pure pattern records without explanation in `kb/log.md`. Put raw captures in `kb/sources/` and descriptions retained to represent a particular system's current or historical state in that system's descriptive collection.

## `kb/reference/COLLECTION.md`

### 5. Replace the opening scope sentence

Replaced:

> This collection accounts for what exists in the shipped Commonplace system — architecture, type system, operator surface, and decision history. Aim at faithful representation of the system as built, not transferable theory.

Applied:

> This collection holds the **choices** Commonplace made and faithfully describes the **current or historical state** they produced — architecture, type system, operator surface, and decision history. Content belongs here when its intended contribution is the selected value, adopted contract, implemented interface, exposed behavior, or prior system state rather than a substantive claim about the design space that remains after those choices are bound. Aim at faithful representation of the system as built, not transferable theory.
>
> A reference artifact may contain supporting belief propositions without becoming a note. What decides placement is the artifact's intended contribution, stated by its title, description, and opening.

### 6. Add one line to "What does NOT belong here"

> - Bounded datasets, experiments, traces, or casebooks whose intended contribution states what they establish about the design space and the limit of that inference → `kb/notes/evidence/`

## Not covered by these edits

- The three relocation candidates named in the ADR. Contract text first, moves
  after, so the moves are applications of a stated rule rather than opinion.
- The maintenance form of current-state descriptions. They belong in reference;
  the remaining per-artifact choice is whether to generate them, register them
  for staleness, author only irrecoverable content, or minimize them.
- `kb/instructions/`, `kb/sources/`, and the external-system collections. Their
  boundaries are unaffected, but `kb/instructions/` deserves a check: an
  instruction is a choice with an imperative surface, and its contract should
  not read as though it competes with reference for the same content.
