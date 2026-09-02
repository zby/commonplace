# A software house needs a theory in Naur's meaning

A [software house](../../notes/definitions/software-house.md) is the complete persistent system that
develops and evolves software in response to its users and operating
environment. Its production machinery and whatever fills its internal roles
are inside the boundary; its users are outside. Product scope and operating
horizon are parameters.

The definition deliberately stops there. Revising the system's own machinery
and revising it from the system's own production experience — learning — are
bigger steps, taken explicitly later, not parts of the definition.

In operation such a system changes things all the time: the software it
produces and, in any long-lived setting, its own machinery for producing
it.

Every change has to fit purposes and organization the system already has.

The checks a change runs against — tests, reviews, acceptance criteria —
capture those purposes and that organization only partly.

So a change can pass every check and still not fit. The usual form of the
misfit is a local special case: the change does its job, but cuts across the
design instead of going through it.

The misfit shows up late. Not as an immediate failure, but as later changes
that get harder, because each one has to work around what the earlier change
did to the design.

Therefore, if misfits are not to accumulate, something must supply what the
checks do not. Judging fit has three parts: knowing what the software is for
— how it maps onto the activity it serves; knowing why it is organized as it
is; and relating the new demand to that organization. Nothing less decides
whether a passing change fits.

Those three capacities are what Naur (*Programming as Theory Building*, 1985)
calls the theory of a program.

So: a software house that keeps changing coherently must hold such a theory —
of its products; and of itself wherever it also changes its own machinery,
since those changes run under the same conditions: partial checks, delayed
misfit.

The function need not run at change time. A software house can let misfits
land and repair them when they surface. But repair needs the same three
capacities — to restore a design you must know what it should have been —
applied later, against more accumulated structure, at higher cost. Deferral
moves the theory-need in time; it does not remove it.

## What the derivation assumes

Checks are partial and the evidence of misfit is delayed. A software house
whose checks fully captured its purposes and organization would not need the
theory; the checks would carry the burden. The derivation runs wherever that
ideal fails.

Product scope controls whether it fails. Fix the scope so that every
admissible demand is pre-analyzed, and the checks can be complete: a
generator for such a scope works trivially, with no theory needed at change
time. The operative sense of scope is novelty, not size — a scope can be
large yet fully enumerated. Scoping is itself a codification move: it
codifies the demand space rather than the knowledge, and it extends the
fully automatic reach only trivially, exactly over the pre-analyzed region
where no theory was needed. The derivation bites when the demand stream
brings what nobody pre-analyzed; relating that to the existing organization
is what needs the theory. Whether an economically useful software house can
exclude novelty over its operating horizon is a separate empirical question.

## What would refute it

A software house that sustains coherent change over a long horizon, on a scope
that keeps admitting novel demands, with no project-specific state performing
the three functions beyond the raw production record and a general-purpose
model. If that works, the derivation is wrong.

The refuter disciplines us as much as the rival: we may not relabel every
success as an implicit theory after the fact. The rival condition is fixed in
advance — raw record, general model, nothing organizing them.

## What the derivation does not need

- **A bearer.** Naur argued only people can hold a theory. The derivation
  needs only that *something* performs the function. Whether it can be held
  outside human heads — and outside model weights, in retained artifacts an
  LLM reads — is the empirical question, not part of the derivation; the
  holding conjecture states the program's bet on how.
- **A learner boundary.** Which parts of the software house count as the
  learner — the humans, the technical machinery, the composite — matters for
  attributing learning in a test. The derivation holds regardless. In
  particular, a human-operated software house whose people hold the theory
  meets the derivation in full. The derivation poses no problem; the costs of
  each way of meeting it do.
- **A definition of learning or a measurement instrument.** Learning is
  derived separately, in the learning derivation; measuring it belongs to
  testing.
