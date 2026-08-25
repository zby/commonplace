---
description: "Proposal: make a recorded decision reach the operations it constrains by having each ADR declare the artifacts it binds and each bound artifact carry a checked back-pointer, rather than a hand-maintained decision index"
type: ../types/design-proposal.md
tags: []
---

# Decisions bind their consumers through site back-pointers

Commonplace holds 76 ADRs. Nothing routes a change run into the ones that
constrain what it is about to touch. An ADR is pointed *at* by artifacts that
cite it and never routed *to* from a task, so it is consulted by luck: full
authoring and maintenance cost, unreliable consumption.

The consequence is stated in the vocabulary the KB already uses for itself. An
ADR asserts what was decided and why; it binds nothing on its own, because
nothing consults it. Retention without a consumer is storage, not
[operative change](../../notes/definitions/operative-change.md) — and a
decision whose record no operation reads is not a
[system-definition artifact](../../notes/definitions/system-definition-artifact.md)
however carefully it was written. The ADR type spec has required a named
operativity path since 2026-07-24, but that path is prose inside the ADR: it
names a consumer without giving the consumer anything to read.

This proposal is the design object for that gap. It does not argue that the
gap should be closed now; it records the option space so an adoption decision
has something to choose from.

## Current state (as of 2026-08-25)

- `kb/reference/adr/` holds 76 ADRs and has no index — no README, no INDEX
  file. `AGENTS.md` names the directory as a navigation entry point, which is
  discovery by listing.
- No instruction routes anyone to the ADR set before a change. The instruction
  files that mention `adr/` cite specific ADRs as sources for a claim; none
  tells an actor to consult the decision set before changing something. The
  change loop is the only operating loop in the KB without an instruction of
  its own.
- [ADR 074](../adr/074-git-is-the-change-history-layer.md) established the
  shape a working read path has: an operation that needs history reaches it
  through an instruction that names the query (`git log --grep='ADR 0NN'`),
  not through an agent's initiative. That pattern currently covers one
  operation, ADR revision.
- [`kb/reference/types/adr.md`](../types/adr.md) requires ADRs dated 2026-07-24
  or later to name the decision's operativity path — consumer, channel, force
  — in `Consequences` or `Decision`. The requirement is satisfied by prose and
  is not machine-checkable in its current form.
- [ADR 077](../adr/077-content-routing-by-regeneration-source-and-consumer.md)
  routes content by regeneration source and consumer. Its table names row 4,
  the decision itself, as consumed by "any change touching what it binds" —
  and records decision consumers as the one row with no reliable consumer,
  handing the gap to this design rather than settling it.
- [`kb/reference/COLLECTION.md`](../COLLECTION.md) already states the site
  rule for a neighbouring case: where a passage warns a future changer, prefer
  the site it constrains over this collection, because a warning found only by
  someone who thought to read a reference document is a warning most changers
  will miss.
- The mark rule is shipped and enforced. A cached value recomputable from
  ground truth elsewhere is either validator-checked or absent
  ([`kb/types/tag-readme.md`](../../types/tag-readme.md), ADR 026); the
  `complete` and `covered_by` marks on tag-READMEs are the working precedent.
- A change-operations catalogue exists in the workshop layer as an
  observational first pass: eighteen operations, each with observed instances,
  premises the actor must know before acting, the current home of those
  premises, and the gap. It carries no completeness mark and nothing in the
  library links to it. Several of its rows record the same failure — a rule
  that lives only in an ADR, which nothing routes to at change time.

## The problem

A change operation — altering a type spec, revising a collection contract,
adding a validation check, changing the link vocabulary — has premises that
were fixed by earlier decisions. Those premises are recorded. They are not
delivered. The actor either already knows which ADRs apply, or searches on a
hunch, or proceeds without them and reverses a decision by accident.

Two constraints bound any fix.

**A partial index is worse than none.** A stale or incomplete routing surface
suppresses fallback search: an agent that finds three relevant decisions stops
looking for the fourth. Any surface either carries a completeness guarantee it
can keep, or must not read as complete.

**Anything recomputable that gets cached must be checked.** A routing surface
that copies information derivable from the ADR set is subject to the mark
rule: machine-checked against its source, or absent. Hand-maintained and
trusted is the forbidden middle.

## Option space

### A. Hand-maintained decision index, keyed by operation or artifact

A README under `kb/reference/adr/` listing decisions by the change operation
or the artifact they govern. Cheap to start, immediately readable, and the
first shape anyone reaches for.

**Rejected.** It is exactly the surface both constraints forbid. Nothing
recomputes it from the ADR set, so it is a hand-maintained cache of
recomputable truth; and an index that is silently partial is worse than no
index, because it converts "I should search" into "I found the list." Neither
defect is fixed by care at authoring time — the index goes stale on the next
ADR nobody remembers to file.

### B. Instruction-declared read paths, per operation

Generalize the ADR 074 pattern: each change operation's instruction names the
decisions that operation must read before acting. The force is the same force
an instruction already has, and the ADR set stays a passive record consulted
through a declared path.

**Sound, but blocked on coverage and on missing instructions.** The
instruction must know which decisions bind its operation, which means the
operations catalogue has to reach usable coverage first — and the catalogue is
explicitly an observational list with no completeness mark. Worse, the
operations most in need are the ones with no instruction at all: the catalogue
records that the change loop itself has none, and that altering a collection
contract has none. This option routes well wherever an instruction exists and
is silent everywhere else, and its silence is invisible.

### C. Site back-pointers, checked from the decision side — candidate

Invert the direction. Instead of routing an actor to the decisions, put each
decision at the site it binds, and make the decision side responsible for
completeness.

1. **An ADR declares its consumers machine-readably.** The prose operativity
   path names what the decision binds; a structured declaration — a frontmatter
   list of the artifacts constrained, a collection contract, a type spec, an
   instruction, a validator module — makes the same statement addressable.
   This turns an already-required authoring obligation into a checkable one
   rather than adding a new obligation.
2. **Each bound artifact carries a back-pointer.** One line naming the
   decisions that constrain it. It is loaded exactly when the operation
   happens, because a writer reads the contract before acting. The
   back-pointer is the consumer the operativity path has been missing — not a
   surface an agent must think to visit.
3. **A validator checks reciprocity.** Every artifact a decision declares as
   bound carries the matching back-pointer, and every back-pointer names a
   decision that claims it. The back-pointer is then a *checked* derived copy,
   which the mark rule permits, rather than a trusted index, which it forbids.

Completeness is enforced from the decision side, where a new ADR is the event
that would otherwise be forgotten. The residual gap is bounded and nameable:
ADRs that carry no declaration. That is a retrofit worklist, not an open-ended
maintenance burden, and the operations catalogue's audit can drive it.

This is the candidate direction. It is not free of cost — see Forces and Risks
— and the granularity, placement, and retrofit questions below are left open
on purpose.

### D. Status quo, with the gap recorded

Keep ADR 077's row 4 as a visible gap and consult decisions by initiative.

**Rejected as the default.** Not because recording a gap is wrong — it is the
correct interim state, and it is why this proposal exists — but because the
gap is what makes the ADR content inert. The set keeps growing at full
authoring cost while the consumption side stays at luck. Deferring is a
choice to keep paying for a record nothing reads.

## Operativity path

**Option C.** Consumer: the writer or reviser of the bound artifact, who reads
that artifact before changing it. Channel: the artifact's own text — the
back-pointer line — plus the validator run that checks reciprocity. Force: the
binding force the bound artifact already carries (a `COLLECTION.md` back-pointer
is loaded with contract force; one on a reference doc is advisory), plus a
deterministic check that the pointer exists.

**Option B.** Consumer: the actor executing the operation. Channel: the
instruction. Force: instruction force, which is real but reaches only the
operations that have instructions.

**Option A.** Consumer: an agent that decides to look at the index. Channel:
a document nothing routes to. Force: none — which is the current situation
with an extra file to maintain.

**Option D.** No consumer; the recorded gap is the honest statement of that.

## Oracle warrant

Option C adds a deterministic check, so the limit of that check must be stated
where the check ships.

The validator can verify **presence and reciprocity**: the declared target
exists, and it carries a pointer back to the declaring decision. Both facts are
recomputable from the two files, which is what licenses the cached
back-pointer under the mark rule.

The validator cannot verify that the decision **still applies** to the
artifact, that the declaration is **complete** for that artifact, or that the
writer **read** the decision before acting. Those remain authoring-contract
obligations, and the check must not be described in a way that implies
otherwise: a green validator run means the wiring is intact, not that the
decisions are current or obeyed. A checked pointer set that readers take as
certified currency reproduces the stale-index failure one level up.

## Forces

- **Completeness versus partiality.** A pointer set that reads as complete
  while missing entries misleads more than an absence does, because it stops
  fallback search. Whatever is claimed must be enforced from the side where
  the omission would occur.
- **Push to the site versus pull from an index.** Loading frequency is the
  whole difference. A site is read by the operation that touches it; an index
  is read only by an agent that thinks to look. The site rule in
  `kb/reference/COLLECTION.md` already resolves this force for warnings; a
  decision pointer is the same shape.
- **Checked derived copies versus hand-maintained ones.** The mark rule admits
  a cache only with a validator behind it. This decides the *form* of the
  back-pointer, not whether one is wanted.
- **Binding force versus advisory presence.** The same line means different
  things at different sites. On a collection contract it inherits contract
  force; on a reference doc it is advice. The design should not pretend the
  force is uniform.
- **Retrofit cost versus prospective-only adoption.** 76 existing ADRs is a
  bounded but real sweep. Prospective-only adoption is cheap and leaves the
  existing set exactly as inert as it is today — and the existing set is where
  the accumulated premises live.
- **Granularity of the declared target.** A file-level target is easy to check
  and coarse; a section-level target is precise and creates a second thing
  that can drift. Coarse targets tend toward whole collections, at which point
  the pointer stops discriminating.
- **Authoring load at the decision surface.** Requiring a declaration makes
  writing an ADR marginally harder at the moment when the author actually
  knows the answer. That is the cheapest moment it will ever be, which is an
  argument for it, but it is still load.

## Free choices

- Whether a consumer declaration is **required** for new ADRs or optional. A
  required field with an explicit "binds nothing yet" value differs from an
  optional field mainly in what a missing value means.
- Whether existing ADRs are **retrofitted as a sweep** or adoption is
  prospective-only, with the operations catalogue's audit table as the
  worklist if a sweep happens.
- **Where the back-pointer sits** at the bound artifact: a frontmatter field,
  or a line in the body or footer. Frontmatter is easier to check; a body line
  is read by an agent that loads the artifact for its content.
- Whether the back-pointer is **generated by a command** from the declarations
  and checked, or **written by hand** and checked. Both satisfy the mark rule;
  they differ in who does the work and in how a conflict is resolved.
- Whether **section-level targets** are permitted, or declarations name whole
  files only.
- Whether a decision may declare a target it does not yet bind, for a decision
  whose implementation lands later.

## Adoption criteria

- Every artifact a decision declares as bound carries a reciprocal pointer,
  and the reciprocity is validator-verified rather than asserted.
- No hand-maintained decision index exists. If one would be useful, it is
  generated from the declarations and checked, not curated.
- A change operation on a bound artifact encounters the decisions that
  constrain it without any agent taking the initiative to search — the pointer
  arrives with the artifact the operation was going to read anyway.
- Where a completeness property is claimed, it is enforced from the decision
  side; where it is not claimed, nothing in the surface reads as complete.
- The retrofit worklist, if there is one, is derived from the operations
  catalogue's audit rather than assembled by taste, and its residue — ADRs
  with no declaration — is countable at any time.
- The validator's warrant is stated where it ships: presence and reciprocity,
  not currency and not compliance.
- ADR 077's row 4 gap is closed and the routing table updated to name the
  consumer it now has.

## Risks

- **Pointer clutter on always-loaded surfaces.** A collection contract is read
  before every write into that collection. If every decision that touches it
  adds a line, the contract accumulates a decision list that competes with the
  contract itself for the reader's context — on the artifact least able to
  afford it.
- **Granularity drift toward whole collections.** The easiest declaration to
  write is the broadest one. A pointer set where most decisions bind
  `kb/reference/COLLECTION.md` discriminates nothing and costs the same to
  maintain.
- **Certified wiring, stale content.** A validator that verifies reciprocity
  can make a set of pointers look maintained while the decisions behind them
  have been overtaken. The check's silence about currency is a property
  readers will forget unless the surface says so.
- **Retrofit by guess.** A sweep that assigns declarations to 76 existing ADRs
  under time pressure will produce plausible-looking targets that nobody
  verified against what the decision actually constrains — a checked pointer
  set built on unchecked judgments.
- **A second authoring obligation that quietly lapses.** The prose operativity
  path is already unenforced in substance. Adding a structured declaration
  without deciding whether it is required creates a field that is present on
  recent ADRs and absent everywhere else, which is the partial-index failure
  wearing different clothes.

---

Relevant Notes:

- [Operative change](../../notes/definitions/operative-change.md) — rests-on: a retained decision reaches later behavior only through a consumer, a channel, and a force, which is the property the ADR set currently lacks
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) — rests-on: binding force comes from a consumption path, so an ADR nothing consults is data rather than a system definition
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why the candidate's back-pointer must be validator-checked and why the hand-maintained index option is rejected outright
- [Stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — rests-on: why a partial routing surface is worse than none, the constraint that eliminates option A
- [Agent statelessness makes routing architectural, not learned](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — rests-on: why consultation cannot be left to accumulated habit and must be built into what the operation loads
- [ADR 074 — Git is the change-history layer](../adr/074-git-is-the-change-history-layer.md) — compares-with: the precedent for an instruction-declared read path, which option B generalizes
- [ADR 077 — Content routing by regeneration source and consumer](../adr/077-content-routing-by-regeneration-source-and-consumer.md) — compares-with: the routing table whose row 4 records this gap and hands it here
- [ADR type spec](../types/adr.md) — see-also: the operativity-path requirement this proposal would make checkable
