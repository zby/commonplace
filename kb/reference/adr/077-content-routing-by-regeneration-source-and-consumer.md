---
description: "Accepted decision that content placement is decided first by what an interpreter cannot regenerate from implementation, git, and general knowledge, then by the consuming operation's force; content-routing.md is the table; limits get a named section"
type: ../types/adr.md
tags: []
status: accepted
---

# 077-Content routing by regeneration source and consumer

**Status:** accepted
**Date:** 2026-08-25

## Context

[ADR 074](./074-git-is-the-change-history-layer.md) gave change history a home
and gave `kb/reference/` a criterion — a passage earns its place by naming the
change operation that must read it. It settled one content kind. The general
question stayed open: for every other kind an agent produces — an intent, a
world-side constraint, a rejected alternative, a limit, an observation — the
placement call was made by taste, and each collection contract answered only
for its own doorway. Nothing said whether a piece of content should be written
down at all.

The criterion that answers both follows from Naur's theory-building account
plus the interpreter/retained-text split this KB already assumes. A theory
holder can map program parts to world affairs, justify each part, and judge
whether a new demand is a natural extension. An LLM interpreter regenerates
most of that at read time from three sources: the implementation, git, and its
own general knowledge. Decision premises it cannot faithfully recover from
those three must be held by tracked artifacts — relevance decisions, intents,
project-particular forces, rejected alternatives, and applicability scope are
the common instances
([design rationale must preserve decision premises its interpreter cannot regenerate](../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md)).
The rule runs one way. Recoverable explanation is a cache, judged by cache
economics rather than by truth, only when the passage carries no independent
authority, cross-check, provenance, activation, or exact-record role.

Regenerability decides *whether*; it does not decide *where*. Among retained
kinds the consuming operation and its force on the reader sort the
destinations: binding content the reader executes, premises it must know
before changing the system, decisions it must not silently reverse, theory it
reasons with, audit trail it reconstructs, observations nobody consumes yet,
and in-flight work consumed by the workshop that produced it.

Within the retained set the kinds may not be equal. A companion note
conjectures that an unrecoverable governing intent reconstructs more local
rationale per token than the same budget of rationale snippets, since one
stated purpose stands upstream of many per-part justifications and most
relevance decisions. That comparison is unmeasured, so it ranks no rows here.
Independent of it, the choice among equally intent-serving designs, a
world-side constraint particular to this project, a limit of applicability, and
an arbitrary convention are contingent facts, not inferences: no interpreter
strength derives them from an intent alone. The derivation was
worked out in the documentation-disposition workshop, now closed; its retained
form is the two notes in the footer.

## Decision

**Placement is decided in two steps: regeneration source, then consumer and
force.** Ask first what already carries the content — the implementation, git,
or the reader's general knowledge; if one of them does, it is not retained. Of
what remains, the operation that consumes it and the force it carries pick the
destination.

**`kb/reference/content-routing.md` is the routing table.** Seventeen content
kinds, each with its regeneration source, consuming operation, destination,
and shape, plus the force-to-destination map. It is a premise of every write
operation and is reached from `AGENTS.md` Collection Routing and the reference
README. It does not replace a collection contract; a writer still reads the
target `COLLECTION.md`, and the table answers the prior question of which
collection is the target.

**Instructions state their goal.** An instruction opens with one sentence
saying what the procedure exists to make true. The rule to cut per-step *why*
stands: the goal is not regenerable from the steps, while the per-step reasons
are regenerable from the goal plus the step.

**Commit bodies open with the change's intent** when the subject and the diff
do not already show it. The diff records what changed, not what for, and the
commit is the decision surface where change-grain intent is cheapest to
capture.

**The reference economy test names its regeneration sources.** The third test
now asks whether a passage is a premise or something the reader regenerates,
and names implementation, git, and general knowledge explicitly, so a writer
can say which one makes the passage redundant.

**Applicability limits get a section of their own.** A note states its
assumptions, applicability conditions, and known failure cases under `## Scope`
(`## Caveats` in a `structured-claim`); an ADR states in its own paragraph of
`Consequences` where the decision stops applying; the premise-decomposition
gate routes a LOCAL failure's qualification there. A limit with its own section
can be narrowed by a rescoping edit without rewriting the claim, and the
scope-testing review gates have a place to look.

**A workshop framing records who posed the question and in what role** —
operator direction, or an agent's proposal awaiting adoption. That attribution
is the part a later session cannot recover from the question itself.

Operativity path. `kb/types/instruction.md` and `kb/instructions/COLLECTION.md`
carry the goal rule, loaded by writers of instructions; `AGENTS.md` `## Git`
carries the commit-intent convention, loaded by every agent in this checkout;
`kb/reference/COLLECTION.md` carries the named regeneration sources, loaded by
writers and reviewers of reference; `kb/types/note.md` carries the `## Scope`
rule in its writing shape and template, loaded by note writers and by the
structural and semantic gates; `kb/reference/types/adr.md` carries the limit
paragraph, loaded by ADR authors; `kb/instructions/premise-decomposition-gate.md`
carries the LOCAL-qualification routing and is loaded when that gate runs;
`kb/work/COLLECTION.md` carries the framing-authorship clause, loaded by
workshop authors; the table is reached by the `AGENTS.md` pointer and the
reference README. The force is an authoring contract in every case. No
validator enforces any of them.

## Considered alternatives

**Retain intents only.** If intent plus implementation regenerates most
justifications, an intent-only strategy would be the strongest bet on
interpreter strength. Rejected. The choice among alternatives, world-side
forces, applicability limits, and arbitrary conventions are facts rather than
inferences, and Naur's two failure cases are exactly where an intent runs out:
a change that reverses a decision by accident, and a change that extends past
an unrecorded limit. However well an intent seeds reconstruction, the other
kinds are what a seed cannot produce.

**Leave the instructions "cut the why" rule unchanged.** It reads as a blanket
ban on rationale, which is why goals were being cut with the reasons.
Rejected: the two are asymmetric. The rule now distinguishes them instead of
weakening.

**Merge the table into `design-rationale-management.md`.** Rejected. That
table is organized by the lifecycle state of a rationale — exploring,
undecided, implemented, displaced — and this one by content kind, including
kinds that are not rationale at all: intents, scope, implementation facts,
change narrative, observations, sources. They cross-link and agree on every
shared cell.

**Enforce the instruction-goal and commit-intent conventions.** A validator
check on instruction bodies and a commit-msg hook are both cheap. Deferred
until drift is observed, matching ADR 074's stance on the commit convention;
an unexercised convention formalized early fixes the wrong shape.

**Require a `## Scope` section on every note.** Rejected. A claim with no
known limit would get an empty section or an invented one, and an invented
limit is worse than a missing one. The heading is expected where a limit
exists, not mandated everywhere.

**One further change the derivation implied is handed off, not rejected.**
Giving decisions a declared consumer — the force gap behind ADRs being
"consulted by luck" — is the proposal *Decisions bind their consumers through
site back-pointers*, whose retrofit worklist the change-operations catalogue
would supply; it stays a recorded gap in the table rather than being settled
here.

**The retained-intent record ships only its source clause.** A workshop framing
now fixes who posed the question and in what role. The `status` field — whether
the intent still applies, who maintains it, when it decays — is deferred:
shipping it without maintenance semantics would create a hand-maintained
trusted cache, which the KB's mark rule forbids. `AGENTS.md` KB Goals get no
source line, since the operator's own instruction file is its source.

## Consequences

Placement becomes answerable from a table rather than from taste, and a
disagreement about placement now has a citable row to argue over. The one
recorded gap — decision consumers — is visible as a row with no reliable
consumer rather than as an absence.

A rescoping edit now has a target: a limit found to be wrong is narrowed in the
`## Scope` section or the ADR's limit paragraph instead of being argued out of
the claim text, and the two notes written under this decision already carry
`## Scope` sections. Workshop intent becomes attributable, and its currency
is read from the container rather than a field: a workshop question is current
while the workshop is in the Active list, a proposal's problem while it is in
the frontier, the KB goals while `AGENTS.md` is the operator's instruction
file. A `status` field would duplicate that position by hand and drift from
it; the framing's date posed lets a triage of the Active list catch a stale
question. Intents that persist outside such a container — retained user
direction in harness memory — need the full source/subject/scope/status record,
and that belongs to the memory system, not to a KB artifact field.

The intent-leverage claim is a conjecture with a stated refuter, not a ranking
this decision rests on. The prediction has two halves: an agent given an
artifact plus its intent should reconstruct per-part justifications better than
one given the same token budget of per-step rationale, and should do worse at
avoiding reversal of a recorded decision, recovering a world-side constraint,
and respecting an unrecorded limit. The first half is refuted if equal-budget
rationale snippets match or beat the intent on held-out justifications. Losing
the second half is the evidence the non-intent rows need. Until the test is
run, no row is weighted above another on this basis.

Two of the four conventions are unenforced authoring rules on high-traffic
surfaces and will drift; drift degrades gracefully, since a missing goal
sentence or a bare commit body loses regeneration leverage without breaking
anything, and the validator and hook remain available as the fix.

Installed projects and vendored copies inherit ADR 074's boundary unchanged:
the regeneration sources assume a source-checkout operator with implementation
and history, so anything a reader without git must know stays in tracked
artifacts. The table does not re-derive that boundary and does not weaken it.

---

Relevant Notes:

- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) — rests-on: supplies the one-way retention rule that decides whether content must be written down, and when recoverable explanation is only a cache
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) — rests-on: the untested conjecture behind keeping the instruction goal and the commit intent line, and why the table still keeps the rows an intent cannot supply
- [Content routing](../content-routing.md) — implemented-by: the routing table this decision adopts and points the write operations at
- [ADR 074 — Git is the change-history layer](./074-git-is-the-change-history-layer.md) — extends: generalizes its one-kind criterion into a routing rule for every content kind
- [An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the goal survives in an instruction body while situational rationale is cut
- [Bottom-up structure inference needs capture at the decision surface](../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — rests-on: why change-grain intent is recorded in the commit rather than reconstructed later
