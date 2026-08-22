**Promoted 2026-08-23** into [kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md](../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md). Both Open questions were carried over unresolved.

# Superseded choices are retained; superseded beliefs are not

When a belief is revised, the version it replaces has no standing. It was
wrong, and the KB keeps no record of having held it — the note is rewritten
and the old text survives only in git.

When a choice is superseded, the choice it replaces remains a fact about what
the system once committed to. The record is load-bearing: it explains why
downstream artifacts have the shape they do, and a later reader needs it to
tell a deliberate reversal from an accident. This is why ADR chains are
append-only while notes get holistic rework.

The asymmetry follows from what each is answerable to. A belief answers to
evidence, which does not care what anyone previously thought. A choice answers
to nothing outside the act of choosing, so the act is the only thing that ever
made it true, and deleting the record deletes the fact.

## Not already covered

[Artifact classification](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md)
assigns refresh-vs-supersede to the production relation. That is the *operation*
performed. This claim is about what happens to the *displaced content*, which
the maintenance operation does not determine.

## Open

- Does this hold for a belief retracted rather than revised — is a recorded
  retraction a fact the way a superseded choice is?
- Where does a belief that was reasonable on the evidence available then, and
  is wrong now, sit? It looks like a belief with a retained past.
