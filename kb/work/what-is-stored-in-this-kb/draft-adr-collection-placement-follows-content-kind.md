# DRAFT ADR — Notes bind choices; reference records Commonplace selections and state

**Promoted 2026-08-23** as
[ADR 070](../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md).
The accepted record is authoritative. It also records the final decision that
unresolved evidence stays in `kb/work/`, first occurrences or pure pattern
records stay in `kb/log.md`, and `kb/notes/evidence/` requires its own bounded
inference even when the larger theory remains incomplete.

**Draft status:** promoted
**Date:** 2026-08-23

## Context

The two main collections state what they hold in prose that mixes criteria.
`kb/notes/` retains "transferable claims about what is true — mechanisms,
principles, and arguments that should hold across systems." `kb/reference/`
holds "accounts of what exists in the shipped Commonplace system."

Those clauses leave one case underspecified: a theoretical claim may be derived
from or evidenced by a particular system without becoming a system record. The
existing formulation constraint already requires a note's title and opening to
be statable in general terms, but the collection boundary does not yet explain
how a particular case can meet that requirement or when it instead belongs in
reference.

`kb/notes/evidence/` holds seven artifacts, five grounded in observations of
this repository — a six-path addressability audit, a note-history trace,
review-bundle cost telemetry, three simplification passes of one article, and
two rewrites of one note. Their titles and openings state what the cases
establish and bound the inference, so the particular serves as a witness.
Meanwhile `kb/reference/` holds three superficially similar artifacts:
`tag-readme-trace-observed-causal-connection.md`,
`harness-sub-agent-model-selection-regression.md`, and
`commonplace-as-a-reflective-system.md`. Some may make the same witness move;
others may principally record a local incident or current state. The contracts
need a rule that distinguishes them rather than treating truth-aptness or a
particular subject as decisive.

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

This decision resolves only the boundary between `kb/notes/` and
`kb/reference/`. It does not replace the special routing rules in the local
contracts for instructions, sources, work, external-system analyses, articles,
or other collections. Apply those rules first when an artifact has their
operative, fidelity, lifecycle, subject-system, or publication role.

`kb/notes/` holds beliefs about the design space, with particular system
choices bound. `kb/reference/` holds the choices Commonplace made and faithfully
describes the current or historical state those choices produced.

Apply the placement test to an artifact's intended contribution, stated by its
title, description, and opening: **after every particular system choice it
names is bound, does a substantive claim about the design space remain?** Bind
a choice universally, through equivalent generic or conditional grammar, or
existentially when the particular is a witness for feasibility, mechanism, or a
bounded consequence. If binding leaves only “Commonplace selected X” or
“Commonplace currently does Y,” the artifact records this system and belongs in
reference.

This replaces the proposed counterfactual test. Asking whether a proposition
would remain true had Commonplace chosen differently cannot distinguish an
observation from a choice record: both may vary with the choice. Binding tests
whether the particular is a parameter or witness in a theoretical contribution,
or whether the local assignment and its resulting state are the contribution.

Subject matter does not decide placement. A note may discuss machinery at
length when its claim ranges over any system built the same way. A reference
artifact may contain supporting belief propositions without becoming a note.

This is a sharper statement of `kb/notes/`'s existing formulation constraint,
not a new obligation: “statable in general terms” is the requirement, and
binding is how a claim naming a system choice meets it. The clarification does
not make previously conforming notes non-conforming. Any old body residue that
already violated the general-form requirement remains ordinary targeted cleanup,
not migration debt created by this decision.

The test has two dispositions. If a substantive proposition remains with the
selection as a parameter, bind it and keep the theory in notes. If the whole
contribution is the selected value or the state it produced, reference preserves
the local record; existential grammar alone does not turn that record into
theory.

## Considered alternatives

**Use truth-aptness alone.** Put every truth-apt proposition in notes and reserve
reference for non-truth-apt selections. Rejected because current-state
descriptions and historical reports of adoption are truth-apt too. Truth-aptness
classifies propositions; it does not decide whether an artifact contributes
theory or a local system record.

**Use the counterfactual “would this remain true had Commonplace chosen
differently?”** Rejected because observations and choice records can both change
under the varied choice. The test does not distinguish the classes it is meant
to route.

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

Three reference artifacts become **reassessment candidates**, not authorized
moves: the two traces and the reflective-system application named above. Move
one only if its intended contribution already uses Commonplace as a substantive
witness for a claim about the design space. The harness regression is primarily
an operational incident about an external tool and may remain reference or move
with its external-system evidence.

Requirements decompose rather than forming a third kind. A requirement
typically pairs a belief that supports it with a commitment that adopts it,
joined by `rests-on`. What resists is externally imposed constraint — a
platform limit or inherited interface nobody here selected — which remains
unplaced.

**Current-state descriptions belong in reference.** `architecture.md`,
`lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture halves of
`review-architecture.md` and `freshness-architecture.md` faithfully represent
the state Commonplace's choices produced. Whether each should be generated,
registered for staleness against the code it describes, partly authored, or
minimized is a maintenance decision that does not change its collection.

Content kind still attaches to a proposition or operative region, while a
collection boundary is file-level. Placement therefore follows the artifact's
intended contribution. Supporting local observations, rationale, and explicitly
scoped choice reports may remain. Mixed artifacts are decided case by case;
splitting is preferred when it yields atomic, independently useful notes. This
decision does not define a universal mixed-artifact threshold.

---

Relevant Notes (on promotion):

- Superseded choices are retained; superseded beliefs are not — rests-on
- A theory may name a choice only as a bound variable — rests-on
- [Artifact classification separates content kind, lineage, and authority](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) — rests-on: supplies the belief/residual-choice distinction used inside the binding test without making region-level content kind a whole-file classifier
- [ADR 069](../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) — see-also: removed the profile labels whose absence exposed the missing criterion
