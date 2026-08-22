# Proposed COLLECTION.md edits

Exact replacement text for the two contracts, pending the
[draft ADR](./draft-adr-collection-placement-follows-content-kind.md). Not yet
applied. Line references are as of 2026-08-23, after ADR 069.

## `kb/notes/COLLECTION.md`

### 1. Replace the opening scope sentence

Currently:

> This collection retains transferable claims about what is true — mechanisms, principles, and arguments that should hold across systems.

Proposed:

> This collection retains **beliefs** — truth-apt claims whose truth does not depend on what Commonplace chose. Mechanisms, principles, and arguments that hold across systems belong here, and so do observations about this system, which are equally truth-apt and record no selection.
>
> The placement test is a counterfactual: **would this still be true if Commonplace had chosen differently?** If yes, it is a belief and belongs here. If no, it is a choice and belongs in `kb/reference/`. Subject matter does not decide this — a note may discuss Commonplace's machinery at length and remain a belief, if what it asserts would hold for any system built the same way.

### 2. Replace the Formulation constraint

Currently:

> **Formulation constraint.** Title and opening argument must be statable in general terms, even when derived from a specific system.

Proposed:

> **Formulation constraint — bind the choices you name.** The title, description, and opening argument must be statable in general terms, even when derived from a specific system. Where a load-bearing claim names a choice some system made, bind it universally, existentially as a witness, or through equivalent generic or conditional grammar. A system-specific term is not a free occurrence when replacing it with its general description leaves the claim's truth conditions unchanged. An unbound occurrence that reads as general but depends on a selection the reader does not share fails: bind the choice and keep the claim, or move the proposition to `kb/reference/` because it only reports what Commonplace selected.

Wording settled by the [bound-variable sweep](./bound-variable-sweep-findings.md), which found 0/27 failures and corrected three underspecifications in the first draft: the measured surfaces were unnamed, binding was written as though it required the literal "for any" formula when most passing notes bind with generic or conditional grammar, and the removal test lived only in the sweep task rather than in the clause. Note the sweep's caveat — an explicitly local choice report may avoid the free-variable defect and still belong in `kb/reference/` under the placement rule.

Leave the adjacent **Theory-independence constraint** unchanged. It governs
citations ("must stand if any single cited description is removed"), which is
a different failure from a free choice-variable — a claim citing nothing can
still carry one.

### 3. Add one line to "What does NOT belong here"

> - Records of what Commonplace selected, and descriptions of what those selections produced → `kb/reference/`

The existing line "Descriptions of how a specific system works → `kb/reference/`
or `kb/agent-memory-systems/`" needs narrowing or it now contradicts the
opening: an *observation* about how this system behaved is a belief and stays.
Suggested replacement:

> - Descriptions of the contract, interface, or current construction of a specific system → `kb/reference/` or `kb/agent-memory-systems/`

## `kb/reference/COLLECTION.md`

### 4. Replace the opening scope sentence

Currently:

> This collection accounts for what exists in the shipped Commonplace system — architecture, type system, operator surface, and decision history. Aim at faithful representation of the system as built, not transferable theory.

Proposed:

> This collection holds the **choices** Commonplace made and the state they produced — architecture, type system, operator surface, and decision history. Content belongs here when it is true because Commonplace adopted, implemented, or currently exposes it; that is, when it would not survive the counterfactual "would this still be true if we had chosen differently?" Aim at faithful representation of the system as built, not transferable theory.
>
> A reference artifact may contain belief propositions without becoming a note. What decides placement is the artifact's dominant contribution.

### 5. Add one line to "What does NOT belong here"

> - Observations about this system that record no selection — traces, audits, measurements → `kb/notes/`, alongside `kb/notes/evidence/`

## Not covered by these edits

- The three relocation candidates named in the ADR. Contract text first, moves
  after, so the moves are applications of a stated rule rather than opinion.
- Current-state descriptions. The rule flags them as homeless; no contract
  clause disposes of them yet, and inventing one before the disposition is
  decided would pre-commit the answer.
- `kb/instructions/`, `kb/sources/`, and the external-system collections. Their
  boundaries are unaffected, but `kb/instructions/` deserves a check: an
  instruction is a choice with an imperative surface, and its contract should
  not read as though it competes with reference for the same content.
