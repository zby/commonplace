# A software factory needs a theory in Naur's meaning

A software factory changes things all the time: the software it produces, and
its own machinery for producing it.

Every change has to fit purposes and organization the factory already has.

The checks a change runs against — tests, reviews, acceptance criteria —
capture those purposes and that organization only partly.

So a change can pass every check and still not fit. The usual form of the
misfit is a local special case: the change does its job, but cuts across the
design instead of going through it.

The misfit shows up late. Not as an immediate failure, but as later changes
that get harder, because each one has to work around what the earlier change
broke.

Therefore, at change time, something in the factory must supply what the
checks do not: how the software maps onto the activity it serves, why it is
organized as it is, and how the new demand relates to that organization.

Those three capacities are what Naur (*Programming as Theory Building*, 1985)
calls the theory of a program.

So: a factory that keeps changing coherently must hold such a theory — of its
products, and of itself, because its own machinery is also long-lived software
and organization that its changes must fit.

## What the derivation assumes

Checks are partial and the evidence of misfit is delayed. A factory whose
checks fully captured its purposes and organization would not need the theory;
the checks would carry the burden. The derivation runs wherever that ideal
fails, which is everywhere software lives long enough to matter.

## What would refute it

A factory that sustains coherent change over a long horizon while nothing in
it performs the three functions — for example, one running on retrieval over
the raw production record alone. If that works, the derivation is wrong.

## What the derivation does not need

- **A bearer.** Naur argued only people can hold a theory. The derivation
  needs only that *something* performs the function. Whether it can be held
  outside human heads — and outside model weights, in retained artifacts an
  LLM reads — is the empirical question, not part of the derivation.
- **A learner boundary.** Who counts as "the factory" — the humans, the
  system, the composite — matters for attributing learning in a test. The
  derivation holds for any of them.
- **A definition of learning or a measurement instrument.** Those belong to
  testing the claim, not to deriving it.
