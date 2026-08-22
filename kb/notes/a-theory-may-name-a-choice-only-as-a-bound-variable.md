---
description: "A claim offered as theory must quantify over any system choice it names — universally, existentially as a witness, or through generic or conditional grammar; a free occurrence keeps no reach past its origin system"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, artifact-analysis, foundations]
---

# A theory may name a choice only as a bound variable

A claim offered as general theory may name a particular system's choice only
under a quantifier. Three forms bind it. **Universal**: for any system that
chooses X, Y follows. **Existential, as a witness**: at least one system does
X, so X is feasible. **Generic or conditional grammar**: the same work done
without the formula. What fails is a *free occurrence* — the sentence reads as
general, but its truth conditions depend on a selection the reader does not
share.

The defect becomes visible at publication, because publication removes the
shared background that was silently supplying those truth conditions. Strip
the local context and a free choice-variable leaves a claim that is false or
empty for anyone who chose differently — which is every reader outside the
system that wrote it. Nothing about publishing creates the problem; it just
runs the test that the origin system's context was suppressing.

## Binding is what produces reach

A claim with a free choice-variable does not carry beyond its origin system,
so this is not a stylistic rule standing beside a quality goal. It is how a
collection that
[selects for explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)
meets that goal at the level of one sentence. "Statable in general terms" is
the requirement; quantification is the mechanism that satisfies it, and the
grammar of the claim is where the mechanism is visible.

Vary the premise and the requirement moves with it. A collection whose purpose
is to record what one particular system selected has no such requirement, and
should not acquire one — there, the choice *is* the content, and
[the record is the only thing carrying it](./superseded-choices-are-retained-superseded-beliefs-are-not.md).
The binding constraint is therefore derivable from what a theoretical
collection is for, rather than being a convention it happens to adopt.

## Binding is often grammatical rather than formulaic

Generic and conditional constructions bind without announcing that they do.
"A system that chooses X," "for runtimes organized as X," "under X," and
"when X" each range over systems or scope the claim to the selected design,
and each is a binding in good standing. A contract or reviewer that recognizes
only a literal quantifier phrase will manufacture failures against claims that
are already general.

## The removal test discriminates the hard cases

The hard case is a system-specific term sitting inside a claim that is
otherwise general. Replace the term with its general description and ask what
happened to the claim's truth conditions.

- **Unchanged** — the term was a label for the general pattern, not a
  variable. In
  [the argument for areas](./areas-exist-because-useful-operations-require-reading-notes-together.md),
  substituting "bounded sets of related notes read together" for "areas"
  leaves the opening mechanism intact, so the local noun is not the defect
  even though it also named selected machinery.
- **Gone** — removing the term removed the proposition, because the term was
  recording something the system stipulated. In the same note, "the split
  threshold of ~40 notes isn't arbitrary" has no general residue once the
  number goes. What survives is the dependence on a usable context budget,
  with 40 as one system's instantiation of it.

Definitions need this test most, because a definition necessarily selects a
word and draws a boundary. That selection alone cannot be the defect, or every
definition would fail. A definition fails when removing its local term also
removes the proposition — when the term records stipulated machinery rather
than marking a distinction that can be stated and contested across systems.

## An explicit local report fails a different test

A passage that says outright it reports one system's selection does not
present as general, so it carries no free-variable defect at all. It can still
be in the wrong place. Two properties are at work and they are independent:
binding asks whether a claim offered as general has general truth conditions;
placement asks which collection owns the proposition. Passing the binding test
is not sufficient for staying in a theoretical collection — an honestly
labelled choice report belongs where choices are recorded.

## Two repairs, selected by what survives the counterfactual

A claim that fails can be bound and kept, or the proposition can be relocated
to where that system's choices are recorded. Which repair is available depends
on what remains when the choice is varied. If a general proposition survives
with the selection as a parameter, bind it: that adds reach rather than moving
content. If the whole content of the proposition is the selection, there is
nothing left to bind, and relocation preserves a record that binding would
destroy. The two are not ranked alternatives for the same case.

## What one sweep found

Commonplace is a witness that the constraint can describe existing practice
rather than prescribe a migration. A systematic sample took every fifteenth of
the 310 files directly under `kb/notes/` and every third of the 23 under
`kb/notes/definitions/`, sorted by filename — 27 files, each read whole. The
scored surface was title, description, and opening argument. No sampled file
failed. Later body material in one sampled note did carry free choice
propositions, including the ~40-note threshold above.

Two limits bound what this shows. A 27-file sample cannot establish a low rate
throughout a collection, and the definition stratum happened to miss
machinery-first candidates that a separate audit had already flagged. The
result is enough to say that adopting the constraint at the scored surfaces
creates no broad migration debt in this KB, and not enough to say the
collection is clean.

## Scope

- The unit is the proposition, not the file. A note can bind at its title and
  opening and still carry free occurrences further down, which is what the
  sweep observed.
- Naming a system after a general claim is illustration or witness use.
  Existential naming is a way of binding, not an exception to the
  requirement.
- The requirement applies to claims offered as general. Collections that
  retain a particular system's choices are outside it by construction.
- Detecting the defect is semantic work. Nothing here supplies a syntactic
  check.

Detecting that a rule is really a choice is a separate question with its own
machinery: a
[rival design that preserves the boundary invariants](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md)
demotes a framework rule to a choice. That test classifies rules; this one
governs how a theory claim may mention whatever it classified.

## Open Questions

- Is a free occurrence detectable more cheaply than semantic review? The
  obvious proxy — a system-specific identifier appearing outside a witness
  clause — would have flagged several of the sweep's clear passes, so the
  cheap version is not obviously sound.
- Does zero measured failure at title, description, and opening reflect
  genuine conformance, or a selection effect in which the surfaces most likely
  to be quoted outward get discipline the rest of the body escapes? The two
  readings predict differently for a KB whose notes are never distilled for
  outside readers.
- Where does an externally imposed constraint sit? A platform limit nobody
  selected is not a choice and needs no binding, yet it is still particular,
  and a claim resting on it reaches only as far as the platform does.

---

Relevant Notes:

- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: supplies the quality goal from which the binding requirement is derived rather than added
- [Superseded choices are retained; superseded beliefs are not](./superseded-choices-are-retained-superseded-beliefs-are-not.md) — contrasts: the sibling consequence of the same belief/choice boundary, governing what happens to a displaced choice where this note governs how a live one may be mentioned
- [Artifact classification separates content kind, lineage, and authority](./artifact-classification-separates-content-kind-lineage-and-authority.md) — grounds: supplies the belief versus residual-choice distinction that decides whether a named term is a choice at all
- [A framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) — contrasts: classifies a rule as chosen or inherited, where this note says how a theory claim may name whatever that test found
- [Areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — evidenced-by: the worked hard case for the removal test, passing at its opening mechanism and carrying free choice propositions later
