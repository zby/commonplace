---
description: "Accepted decision that notes bind particular system choices in transferable claims while reference records Commonplace selections and resulting state"
type: ../types/adr.md
tags: []
status: accepted
---

# 070-Notes bind choices; reference records Commonplace selections and state

**Status:** accepted
**Date:** 2026-08-23

## Context

The two main library collections described what they held through different
criteria. `kb/notes/` retained "transferable claims about what is true —
mechanisms, principles, and arguments that should hold across systems."
`kb/reference/` accounted for "what exists in the shipped Commonplace system."

Those clauses left one case underspecified: a theoretical claim may be derived
from or evidenced by a particular system without becoming a system record. The
existing notes formulation constraint already required a title and opening to
be statable in general terms, but the collection boundary did not explain how
a particular case could meet that requirement or when it instead belonged in
reference.

`kb/notes/evidence/` holds seven artifacts, five grounded in observations of
this repository. Their titles and openings state what a bounded experiment,
trace, audit, or casebook establishes and delimit the inference, so the
particular serves as a witness. Meanwhile `kb/reference/` holds three
superficially similar artifacts: `tag-readme-trace-observed-causal-connection.md`,
`harness-sub-agent-model-selection-regression.md`, and
`commonplace-as-a-reflective-system.md`. Some may make the same witness move;
others may principally record a local incident or current state. Truth-aptness
or a particular subject does not distinguish them.

Subject matter creates a second failure. It admits any artifact whose topic is
methodology, including vocabulary true only because Commonplace stipulated it.
The definition audit found exactly that: `text-contract` defined selected
collection machinery from inside the theoretical collection, and its stable
meaning disguised the placement error.

[ADR 069](./069-collection-contract-bundles-become-one-time-prototypes.md)
removed the profile labels and made each collection state its purpose directly.
That exposed the problem rather than causing it: without the shared labels, the
two contracts visibly lacked one placement criterion.

## Decision

This decision resolves only the boundary between `kb/notes/` and
`kb/reference/`. It does not replace the special routing rules for instructions,
sources, work, external-system analyses, articles, or other collections. Apply
those rules first when an artifact's operative, fidelity, lifecycle,
subject-system, or publication role decides its home.

`kb/notes/` holds beliefs about the design space, with particular system
choices bound. `kb/reference/` holds the choices Commonplace made and faithfully
describes the current or historical state those choices produced.

Apply the placement test to an artifact's intended contribution, stated by its
title, description, and opening: **after every particular system choice it
names is bound, does a substantive claim about the design space remain?** Bind
a choice universally, through equivalent generic or conditional grammar, or
existentially when the particular is a witness for feasibility, mechanism, or
a bounded consequence. If binding leaves only “Commonplace selected X” or
“Commonplace currently does Y,” the artifact records this system and belongs
in reference.

This replaces the proposed counterfactual test. Asking whether a proposition
would remain true had Commonplace chosen differently cannot distinguish an
observation from a choice record: both may vary with the choice. Binding tests
whether the particular is a parameter or witness in a theoretical contribution,
or whether the local assignment and its resulting state are the contribution.

Subject matter does not decide placement. A note may discuss machinery at
length when its claim ranges over any system built the same way. A reference
artifact may contain supporting belief propositions without becoming a note.

`kb/notes/evidence/` is not a staging exception. A bounded dataset, experiment,
trace, or casebook belongs there once the artifact states what it establishes
about the design space and the limit of that inference. The larger theory may
remain incomplete. An observation whose theory-facing inference is still
unresolved remains in `kb/work/`; a first occurrence or pure pattern record
without explanation belongs in `kb/log.md`. A current or historical system
description retained for fidelity remains in reference.

The binding rule sharpens `kb/notes/`'s existing formulation constraint rather
than adding a new obligation: “statable in general terms” is the requirement,
and binding is how a claim naming a system choice meets it. The clarification
does not make previously conforming notes non-conforming. Old body residue that
already violated the general-form requirement remains targeted cleanup, not
migration debt created by this decision.

The test has two dispositions. If a substantive proposition remains with the
selection as a parameter, bind it and keep the theory in notes. If the whole
contribution is the selected value or the state it produced, reference preserves
the local record. Existential grammar alone does not turn that record into
theory.

The nearest `COLLECTION.md` is the complete authoring authority for its subtree.
Agents writing or reviewing artifacts load that contract through repository
routing instructions and skills, so the corresponding edits to
`kb/notes/COLLECTION.md` and `kb/reference/COLLECTION.md` are the operativity
path for this decision. This ADR records why the rule exists; agents do not need
to load the ADR to apply it.

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

**Keep subject matter as the criterion.** Methodology theory would stay in notes
and material about this system in reference. Rejected because this admits any
stable term whose topic is methodology, including terms true only by
stipulation. Stability is what disguises the error.

**Use `kb/notes/evidence/` as a pre-thesis staging area.** Rejected because an
observation whose evidential meaning is still unresolved is work in flight.
Evidence may be promoted before the larger theory is complete, but only after
the artifact can state its own bounded inference and limit. Otherwise
`kb/notes/evidence/` would duplicate the workshop layer.

**Classify each proposition without changing collection placement.** Rejected
because collections are the surface agents actually load. A classification
with no placement consequence has no reader, while artifact classification
already supplies the proposition-level analytical model.

## Consequences

Beliefs and choices acquire different revision regimes, and the difference
becomes derivable rather than conventional. A belief is revised against
evidence and rewritten in place; a superseded choice is retained as a fact
about what the system committed to. This is why ADR chains are append-only
while notes get holistic rework.

Evidence acquires an explicit lifecycle boundary. A raw first occurrence may
enter `kb/log.md`; an unresolved investigation may develop in `kb/work/`; a
bounded observation enters `kb/notes/evidence/` when it states what it
establishes and what it does not. A later theory may cite it, but promotion does
not wait for that larger synthesis.

Three reference artifacts become reassessment candidates, not authorized moves:
the two traces and the reflective-system application named above. Move one only
if its intended contribution already uses Commonplace as a substantive witness
for a claim about the design space. The harness regression is primarily an
operational incident about an external tool and may remain reference or move
with its external-system evidence.

**Follow-up, 2026-08-23.** The causal-connection trace and reflective-system
classification now live in `kb/notes/evidence/`: each states the bounded
design-space inference the Commonplace case supports and what the case does not
establish. The harness model-selection regression remains in reference because
its intended contribution is the dated operational incident and its effect on
Commonplace review provenance.

The definition audit applied the same rule. `answerability` moved to
`kb/reference/definitions/` because its intended force is Commonplace's
stipulated admission boundary. The standalone `directed reading` term was
retired because context-engineering language and the claim-routed-reading note
carry its useful distinctions without another canonical name. `discovery
lifecycle` remains theory as an explicitly bounded ideal-type model; its local
adoption remains a framework choice recorded by ADR 053 and operative
instructions. `actionable methodology` remains theoretical, while the rule
that technical uses of *actionable* link the definition moved to the operative
root vocabulary. `reach-assessment` remains a definition after its developed
route arguments were compressed into links to ordinary theory notes.

The provisional artifact-analysis definitions also remain in theory.
`operative part`, `retained artifact`, and `storage substrate` separate
part-level behavior, persistence eligibility, and operational location across
systems. `knowledge artifact` and `system-definition artifact` remain cheap,
path-relative behavioral-authority shorthands rather than intrinsic artifact
classes. `coordination value` remains a distinct warrant source. The global
`definition` type now says explicitly that type does not decide collection;
the intended contribution does.

Requirements usually decompose rather than forming a third kind. A requirement
typically pairs a belief that supports it with a commitment that adopts it,
joined by `rests-on`. Externally imposed constraints—a platform limit or
inherited interface nobody here selected—remain an open placement case.

Current-state descriptions belong in reference. `architecture.md`,
`lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture portions of
`review-architecture.md` and `freshness-architecture.md` faithfully represent
the state Commonplace's choices produced. Whether each should be generated,
registered for staleness, partly authored, or minimized is a maintenance
decision that does not change its collection.

Content kind still attaches to a proposition or operative region, while a
collection boundary is file-level. Placement therefore follows the artifact's
intended contribution. Supporting local observations, rationale, and explicitly
scoped choice reports may remain. Mixed artifacts are decided case by case;
splitting is preferred when it yields atomic, independently useful notes. This
decision does not define a universal mixed-artifact threshold.

---

Relevant Notes:

- [Superseded choices are retained; superseded beliefs are not](../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — rests-on: explains the different maintenance consequences of beliefs and choices
- [A theory may name a choice only as a bound variable](../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md) — rests-on: supplies the formulation and disposition rule applied by the two collection contracts
- [Artifact classification separates content kind, lineage, and authority](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md) — rests-on: supplies the belief/residual-choice distinction without making region-level content kind a whole-file classifier
- [ADR 069: Collection contract bundles become one-time prototypes](./069-collection-contract-bundles-become-one-time-prototypes.md) — see-also: removed the profile labels whose absence exposed the missing criterion
