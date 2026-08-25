---
description: "Accepted decision that git holds the change narrative of the source checkout, reference and ADRs retain only premises that a named change operation must read, and instructions declare the git read paths"
type: ../types/adr.md
tags: []
status: accepted
---

# 074-Git is the change-history layer

**Status:** accepted
**Date:** 2026-08-25

## Context

Commonplace is a reflective system: its documentation is part of the machinery
by which it changes itself. An agent performing a change reads reference docs,
ADRs, contracts, and instructions as premises. What those artifacts should
contain has so far been decided by intuition and by per-passage economy tests
in `kb/reference/COLLECTION.md`. No rule said which kinds of content a change
operation needs and which merely record that a change happened.

The criterion already exists elsewhere in the KB. A change pathway is part of
the system only when later operation actually reads what it installed; "a
commit or research note is not enough when later runs neither read nor obey
it" (`kb/work/self-revision-design-space`). A retained artifact has
system-definition force only through a consumption path
([system-definition artifact](../../notes/definitions/system-definition-artifact.md)).
Applied to documentation, this says: a reference passage is justified by
naming the change operation that must read it before acting.

Git's position was underspecified in the other direction. [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md)
and [ADR 039](./039-tool-visibility-is-package-owned-and-git-is-never-invoked.md)
removed git from tool correctness. [ADR 056](./056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)
established that git history is not the archive for deleted content, because
shallow clones cannot see it. `storage-architecture.md` therefore says commits
carry no framework-wide semantic meaning. Nothing gave git a declared read
path, so nothing could be left to it with confidence. The narrative of each
change — what moved, what was renamed, which docs were updated to match — went
into ADRs and reference docs by default, where it competes for the context of
every agent loading them to act.

## Decision

**Git is the change-history layer of the source checkout.** What changed, when,
in what order, and the transition performed live in commits. Reference
artifacts and ADRs do not restate that narrative.

**Reference retains premises of change operations.** A passage belongs in
`kb/reference/` when a named operation of changing the system must read it
before acting and cannot cheaply recover it from the implementation. This
extends the existing rule that live implementation is the default read path
for exact implementation facts: git is the default read path for change
history, and the same economy tests apply.

**ADRs retain what the revise operation needs.** An ADR keeps the forces that
would recur if the decision were reverted (Context), the choice (Decision), the
options weighed (Considered alternatives), and what consumes the decision and
what becomes easier or harder (Consequences). Migration steps, before-state
described as a diff rather than as a force, implementation details recoverable
from source, inventories of affected files, and bookkeeping about which
documents were edited to match are cut. Existing ADRs are trimmed to this
standard through a reviewed sweep; the ADR type spec carries the rule for new
ones.

**Instructions declare the git read paths.** An operation that needs history
reaches it through an instruction that names the git query, not through an
agent's initiative. The first declared path is ADR revision: before revising
or superseding an ADR, read `git log --grep='ADR 0NN'` for the commits that
implemented or later touched it. Commit messages support this path: when a
commit implements or revises an ADR, proposal, or workshop, the body names it.
The subject remains an imperative summary of the change.

**Boundary.** Git holds only what an operator of this source checkout needs.
Anything a reader install, vendored copy, installed project, or shallow clone
must know stays in tracked artifacts. ADR 039 stands: `commonplace-*` commands
still never invoke git. This decision adds an instruction-level read path, not
a tool dependency.

**Amendment to ADR 056.** ADR 056 rejected deletion because git history fails
at shallow clone depth, and it named dated corpus measurements — the
evidentiary warrant behind a live decision — as the residue that justifies
in-repo retention. This decision narrows that argument. Content a durable
artifact cites, or that any consumer without history needs, still stays
in-repo; the proposal archive is unchanged. Measurements that only a decision
audit consults are different: the ADR carries the compressed warrant (the
numbers as reasons), and the full measurement is read from the implementing
commits. The one actor who performs that audit is the operator revising a
Commonplace decision, and that operator works in this checkout. A shallow
clone is therefore not a reason to keep the measurement in-repo but an
operator precondition: unshallow before revising. ADR 056 itself was drafted
in a shallow clone, which shows the precondition is real, not that history is
unavailable.

## Considered alternatives

**Keep git outside the system (status quo).** Rejected. With no declared home
for change narrative, it accumulates in ADRs and reference docs, and no
criterion says when it may be cut. The per-passage economy tests cannot answer
the question because they ask whether a passage is useful, not which operation
consumes it.

**Make git a tool dependency.** Commands could read `git log` to reconstruct
lineage or freshness. Rejected for the forces recorded in ADR 032 and ADR 039:
users and agents use git differently, installed projects may not use git at
all, and correctness must not depend on repository history.

**Keep a tracked change log.** A `CHANGELOG` or per-decision episode record in
the repo would be visible to shallow clones and readers. Rejected as the
default because it duplicates git for the one consumer that has git — the
source-checkout operator — while the boundary rule already sends anything
other consumers need into tracked artifacts. `kb/log.md` is an observation
inbox, not a change log, and is not repurposed. A tracked episode record
remains available for the specific case of evidence a durable artifact cites
(as `kb/notes/evidence/` already does).

**Formal commit trailers.** A `Decision-Id:` or similar trailer with parsed
semantics would make the read path machine-checkable. Deferred: a plain
name-in-body convention is enough for `git log --grep`, and formalizing before
the read path is exercised would be premature. The model-provenance question
in `kb/work/lineage-mechanisms/` stays open and may later motivate a trailer.

**Derive reference contents from an operations catalogue now.** An enumerated
list of self-modification operations, each with the premises it needs, would
let both sides be audited: every reference artifact traces to an operation,
every operation's premises have a home. Left open as the natural next step;
this decision fixes the criterion and the git layer first so the catalogue has
a defined target.

## Consequences

Operativity path: `kb/reference/COLLECTION.md` carries the placement rule and
the git-as-default-read-path clause, loaded by writers and reviewers of that
collection; `kb/reference/types/adr.md` carries the retention rule and the
revision read path, loaded by ADR authors; `AGENTS.md` `## Git` carries the
commit-message convention, loaded by every agent in this checkout. The force is
an authoring contract; no validator enforces it.

The ADR set can be trimmed with a criterion instead of taste, which is the
precondition for indexing it: an index of decisions should not be built over
records that are half migration narrative.

Change history becomes invisible to consumers without git, by design. The
boundary rule bounds the exposure: only source-checkout operators depend on
history, and only through declared instruction paths. Those operators need a
full-history clone; the ADR type spec says to unshallow before revising.

The commit-message convention is unenforced and will drift. `git log --grep`
degrades gracefully: a commit that fails to name its ADR is harder to find, not
lost. If drift is observed, the trailer alternative is the fix.

`storage-architecture.md` remains accurate at the framework level — commits
carry no *portable* semantics — and records the source-checkout exception.
