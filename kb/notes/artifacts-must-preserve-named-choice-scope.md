---
description: "An artifact may inherit scope from context guaranteed to its consumers; for each named system choice it must preserve a proposition-relative reference rule or range plus the choice's role, not necessarily concrete identity or quantifier syntax"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, artifact-analysis, foundations]
---

# An artifact must preserve the scope of each named system choice

An artifact need not repeat in every sentence the phrase that fixes or ranges a
system choice. It must, however, preserve enough context for intended consumers
to recover two things for every proposition that names system-chosen machinery:
**the reference rule or range relevant to that proposition** and **the role the
choice plays in it**. If either depends on origin context those consumers are
not guaranteed to receive, the artifact has not preserved that proposition's
scope.

This requirement governs communication at the artifact level. It does not imply
that every context-sensitive utterance is semantically indeterminate. A
conversation, namespace, versioned specification, or registry may give an
utterance a stable referent at its origin. The defect arises when publication or
retrieval packages the utterance without context its new consumers need.
Conversely, a sentence need not be self-contained when the artifact's
consumption contract guarantees the context that supplies its meaning. Nor
must a consumer learn every implementation detail. For a fixed opaque design,
a stable rule for reidentifying the same subject is enough when hidden identity
differences cannot change the proposition's truth or any inference it licenses.
Those hidden differences may still matter to evidence, reproduction, or audit.

## Reference and role are separate obligations

Literal quantifier syntax is neither necessary nor sufficient. A named choice
can fill at least three roles in a proposition.

- **Fixed use** — The choice stays constant while the proposition ranges over
  inputs, states, environments, interventions, or comparison cases.
- **Ranged use** — A variable receives different choices from a stated range
  under universal, generic, conditional, or discourse scope.
- **Substantive witness** — A selected instance supports a proposition beyond
  the selected value itself, such as feasibility, a mechanism, or a bounded
  consequence.

These roles are not exhaustive. A fixed comparison standard, for example, need
not be the grammatical subject. What matters is that the consumer can recover
the role. A quantifier may express a ranged or witness use, but syntax alone
does not define the role or supply the reference rule.

The required reference information depends on the role and proposition. A
fixed name needs a stable rule for picking out or reidentifying the same choice,
at the granularity whose differences could change the proposition's truth or a
licensed inference. A relational description or immutable blinded identifier
can therefore suffice even when the underlying implementation remains hidden.
A ranged variable has no single selected referent; it needs a recoverable range
and a rule for how values are assigned from it. Role answers *how is the choice
used?* The reference rule or range answers *which alternatives can occupy that
role?* A preserved claim needs both.

## The consumption boundary decides whether scope is recoverable

The **interpretation boundary** specifies which context may supply a claim's
meaning. The **consumption boundary** specifies which context an intended
consumer is guaranteed to receive. An artifact preserves scope only when
everything needed to recover the proposition-relative reference rule or range
and the choice's role lies inside both boundaries. That material may appear in
the sentence, earlier discourse, a
title or metadata field, a collection contract, or another pinned specification
that the consumption path guarantees. Availability elsewhere in the repository
does not place it inside the boundary.

Isolated extraction imposes a stronger portability requirement. If a sentence
must survive quotation or independent retrieval, the extracted unit or its
assembly step must carry the reference rule or range and role. If consumers
receive the whole note with its setup, discourse scope can be enough. Packaging
can therefore create a defect by dropping context that the declared
interpretation boundary allowed; publication does not always merely reveal an
existing defect.

Recoverable scope settles how the named choice contributes to what a
proposition says. It does not settle other omitted comparators, metrics, or
conditions, and it does not by itself explain the result, supply evidence, or
warrant transfer. A theory about a fixed router may explain that router across
inputs or interventions, yet its conclusions remain bounded to that router
unless the argument establishes a transfer relation. A universally ranged
claim can likewise lack a mechanism or adequate evidence.

## Diagnose dependency before deciding that scope is missing

The difficult case is a system-specific term inside prose that otherwise sounds
general. A three-stage diagnosis separates dependence from missing scope.

First, name the focal system and decision boundary, then classify what the term
denotes. Is it a selected design, an inherited constraint, or a local label for
a general pattern? The classification is relative to the decision boundary: a
platform limit may be inherited by an application but selected by the platform
operator. A
[rival design that preserves the properties the rule is meant to protect](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md)
can demote a purported constraint to a choice.

Second, use controlled substitution to expose dependence. Replace a local label
with its general description, or replace a context-dependent expression such as
“this system” with an explicit referent, and ask whether the proposition
changes.

- **General-pattern label** — The substitution preserves the proposition. In
  [the argument for areas](./areas-exist-because-useful-operations-require-reading-notes-together.md),
  substituting “bounded sets of related notes read together” for “areas”
  preserves the opening mechanism. The local noun labels the pattern.
- **Stable fixed reference** — The proposition depends on one design and gives
  a rule for reidentifying it. Removing the name destroys the proposition
  because the fixed subject is essential, not because concrete implementation
  identity must always be disclosed.
- **Unresolved alternatives** — Substituting among candidate choices can change
  whether the proposition is true or what it licenses, but the tested unit does
  not determine which choice, range, or valuation rule applies. This is a
  candidate defect, subject to the boundary test.

Substitution is only a diagnostic where replacing one expression with another
that identifies the same thing should not change whether the claim is true. In
“the operator believes router R is safe,” replacing R with an equivalent
description can change the claim because the operator may not know the
equivalence. That result says nothing about whether R had a binding.

Third, inspect the consumption boundary. A reference or range unresolved in one
sentence may be supplied by guaranteed earlier discourse. If the consumer can
recover the proposition-relative reference rule or valuation range and its role
from the full boundary, the dependency is scoped. If distinctions that can
change truth or licensed inference remain available only in unshipped origin
context, the retained artifact is underspecified for that consumer. Controlled
substitution exposes the dependency; the boundary test decides whether the
artifact preserved it.

Definitions require the same ordering, but substitution behaves differently
for them. A definition necessarily fixes a term and a boundary. Replacing the
term with its definition may erase the proposition or turn it into a tautology;
neither result shows that the term names local machinery. Classify the boundary
independently: can the distinction be stated and contested across systems, or
is its meaning constituted by one system's contract?

## Placement follows the contribution that survives scoping

Scope is judged proposition by proposition. Collection placement follows the
artifact's intended contribution, expressed in its title, description, and
opening. A [collection](../reference/definitions/collection.md) is a KB subtree
with its own authoring and routing contract. A collection that
[selects for explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)
retains claims that keep working beyond the cases that produced them because
they explain why the pattern works. Such a collection can require every
artifact to preserve the scope of each named choice. A collection that records
one system's selections has a different contribution: it retains the selected
value. It must still scope its propositions, but it need not turn the value
into a transferable claim.

Once each named choice's proposition-relative reference rule or range and role
are recoverable, ask what substantive contribution remains. If a design-space
proposition survives, keep the theory. If only the selected value or the
current or historical state it produced survives, the contribution belongs
where that system's choices and state are recorded. When no other retained
artifact can reconstruct a superseded choice event,
[at least one reliable historical witness must survive](./superseded-choices-are-retained-superseded-beliefs-are-not.md).
That obligation requires one reliable witness, not every duplicate.

A fixed subject can support theory, but varying its inputs is not enough. An
input/output table may remain a compressed system description. To contribute
theory, the artifact needs an explanation that predicts what would change under
altered inputs or interventions, or some other substantive proposition about
the fixed design. Recoverable scope comes first; placement and transfer are
later questions.

## Existential grammar does not turn a local selection into theory

An explicit report of one system's selection has determinate local scope. It
may also contain theory about that fixed subject if it explains behavior across
states or interventions. Yet recasting “Commonplace, this agent-operated
knowledge-base framework, selected X” as “there exists a system that selected
X” merely wraps the same selection in a quantifier. The instance becomes a
substantive witness only when it supports a proposition beyond reporting the
selected value.

A theoretical note and a local system record therefore preserve different
contributions; they are not ranked destinations for the same content. An
explicitly scoped local report or example may support a theory without becoming
the theory's intended contribution.

## A bounded audit reported no failures in opening surfaces

The source workshop and snapshot-pinned sample manifest for this Commonplace
audit no longer exist. This section therefore preserves an unreconstructable
author report, not independently inspectable evidence for the note's general
claim.

The audit sorted each directory by filename, then selected every fifteenth of
the 310 files directly under `kb/notes/` and every third of the 23 under
`kb/notes/definitions/`. This yielded 27 files. Each was read in full, but only
its title, description, and opening argument were scored. The audit reported no
failures on those surfaces.

It also reported a defect in one later-body proposition: the proposition
depended on a local split threshold of approximately 40 notes but did not
identify the number as local. That note has since been generalized, so the
occurrence is historical rather than a live defect. Because the collection has
changed, the sampling recipe cannot reconstruct the historical cohort. The
report therefore supports neither a collection-wide failure-rate estimate nor
a claim that the collection is clean.

## Open Questions

- Can a missing reference rule or range be detected more cheaply than semantic
  review? A proxy such as a system-specific identifier outside a witness clause
  would overflag fixed uses and clear passes.
- Does zero reported failure at title, description, and opening reflect genuine
  conformance, or more discipline on surfaces likely to be quoted outward than
  on later body prose?
- What distinguishes mechanism-bearing theory about one fixed design from a
  compressed system description?
- How should an externally imposed constraint be treated when its status
  changes with the focal system and decision boundary?

---

Relevant Notes:

- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](./superseded-choices-are-retained-superseded-beliefs-are-not.md) — contrasts: the sibling maintenance consequence of distinguishing beliefs from residual choices, where this note governs how a live choice may be used in theory
- [Artifact classification separates content kind, lineage, and authority](./artifact-classification-separates-content-kind-lineage-and-authority.md) — grounds: supplies the belief versus residual-choice distinction that decides whether a named term is a choice at all
- [Areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — evidenced-by: the repaired hard case preserves the general read-together mechanism while treating fixed thresholds and membership policies as system choices
