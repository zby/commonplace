# DRAFT ADR — Collection placement follows content kind

Workshop draft. Number provisional (070 is next free as of 2026-08-23, but
another session may claim it). Type/frontmatter to be added on promotion.

**Status:** proposed
**Date:** 2026-08-23

## Context

The two main collections state what they hold in prose that mixes criteria.
`kb/notes/` retains "transferable claims about what is true — mechanisms,
principles, and arguments that should hold across systems." `kb/reference/`
holds "accounts of what exists in the shipped Commonplace system."

Those are two different tests wearing one label. One is generality:
transferable versus about-a-particular. The other is subject matter: KB
methodology versus this shipped system. They usually agree, which is why the
mixture went unnoticed, and they come apart in practice.

`kb/notes/evidence/` holds seven artifacts, five of them observations of this
repository — a six-path addressability audit, a note-history trace,
review-bundle cost telemetry, three simplification passes of one article, and
two rewrites of one note. Under the generality reading these are misfiled;
they are accounts of a particular system. They have nonetheless been accepted
practice for months. Meanwhile `kb/reference/` holds three artifacts of the
same shape: `tag-readme-trace-observed-causal-connection.md`,
`harness-sub-agent-model-selection-regression.md`, and
`commonplace-as-a-reflective-system.md`. One class, two homes, no stated rule
distinguishing them.

The subject-matter reading fails differently. It admits any artifact whose
topic is methodology, including vocabulary that is true only because
Commonplace stipulated it. The workshop's definition audit found exactly that:
`text-contract` defined chosen collection machinery from inside the
theoretical collection, and its stable meaning was what made the placement
look defensible.

[ADR 069](../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md)
removed the profile labels and had each collection state its purpose directly.
That exposed the problem rather than causing it: with the shared vocabulary
gone, the two contracts visibly do not share a criterion.

## Decision

Collection placement follows **content kind**. `kb/notes/` holds beliefs.
`kb/reference/` holds the choices Commonplace made and the state those choices
produced.

The test is a counterfactual applied to an artifact's dominant contribution:
**would this still be true if Commonplace had chosen differently?** A belief
survives it. A choice does not, because the choice is what the counterfactual
varies. Particular observations about this system survive it and are therefore
notes; stipulated vocabulary does not and is therefore reference.

Subject matter does not decide content kind. A note may discuss machinery at
length and remain a belief if what it asserts would hold for any system built
the same way. A reference artifact may contain belief propositions without
becoming a note.

`kb/notes/` additionally requires that **a claim naming a choice bind it as a
variable** — universally ("for any system that chooses X, Y follows") or
existentially as a witness ("at least one system does X, so X is feasible"). A
free occurrence, where the sentence reads as general but its truth conditions
depend on a selection the reader does not share, fails the contract. This
sharpens the existing formulation constraint rather than adding a rule beside
it: "statable in general terms" is the requirement, and quantification is how
it is met.

Failing the test has two repairs, and the choice between them is the author's:
bind the variable and keep the claim in notes, or move the proposition to
reference because it was only ever a report of what was selected.

## Considered alternatives

**Keep generality as the criterion.** Transferable claims in notes, particular
accounts in reference. Rejected because it misfiles `kb/notes/evidence/` — an
established directory whose contents the KB has been treating as notes — and
because it gives no principle distinguishing a particular observation about
this system from one about an external system, which already routes to
`kb/agent-memory-systems/` rather than reference.

**Keep subject matter as the criterion.** Methodology theory in notes, this
system in reference. Rejected because it admits any stable term whose topic is
methodology, including terms true only by stipulation. That is the error the
definition audit found, and stability is what disguises it.

**Classify per proposition with no collection consequence.** Keep the
classification analytical and let placement stay conventional. Rejected
because collections are the surface agents actually load. A classification
with no placement consequence has no reader, and the existing artifact
classification already occupies the analytical role.

## Consequences

Beliefs and choices acquire different revision regimes, and the difference
becomes derivable rather than conventional. A belief is revised against
evidence and rewritten in place; a superseded choice is retained as a fact
about what the system committed to. This is why ADR chains are append-only
while notes get holistic rework — previously a separate convention.

Three reference artifacts become **relocation candidates**, not authorized
moves: the two traces and the reflective-system application named above. The
harness regression may instead be a source observation about an external tool.

Requirements decompose rather than forming a third kind. A requirement
typically pairs a belief that supports it with a commitment that adopts it,
joined by `rests-on`. What resists is externally imposed constraint — a
platform limit or inherited interface nobody here selected — which remains
unplaced.

**Current-state descriptions have no home under this rule.** `architecture.md`,
`lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture halves of
`review-architecture.md` and `freshness-architecture.md` assert neither a
belief about the design space nor a choice within it; they are derived state.
The rule flags the class and does not dispose of it. Generation, staleness
registration against the code they describe, or minimization are the candidate
dispositions, deferred to separate work.

The unit mismatch is accepted, not solved. Content kind attaches to a
proposition; a collection boundary is file-level. The rule tracks an artifact's
dominant contribution, and a genuinely mixed artifact must be split rather
than filed.

---

Relevant Notes (on promotion):

- Superseded choices are retained; superseded beliefs are not — rests-on
- A theory may name a choice only as a bound variable — rests-on
- [Artifact classification separates content kind, lineage, and authority](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) — rests-on: supplies the belief/residual-choice distinction this decision promotes to a placement rule
- [ADR 069](../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) — see-also: removed the profile labels whose absence exposed the missing criterion
