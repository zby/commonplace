---
description: "Catalogue of Commonplace's text-contract profiles — proven, named bundles of quality goal, title conventions, attribution, and link grammar a COLLECTION.md may adopt, extend, or start from"
type: ../types/note.md
tags: []
status: current
---

# Text contract profiles

## Approach

A [text contract](../notes/definitions/text-contract.md) is the binding requirement every writable collection's `COLLECTION.md` declares. A **profile** is a named, proven bundle of contract features — orientation, quality goal, title/description conventions, attribution/evidentiality requirements, maintenance semantics, outbound link grammar — that a collection can adopt wholesale, extend, or use as a base instead of writing every clause from scratch. This page is that library: a palette, not an enum. Each `COLLECTION.md` stays authoritative for the collection's actual contract; a profile entry here is a proven starting point, not a binding source.

Promotion follows the same worked-case-first guard as [link-vocabulary.md](./link-vocabulary.md) (ADR 019): a new profile is written and exercised locally — inside a single collection or a consuming project — before it earns a shared entry here. [ADR 042](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) records the decision to open this set; the guard is what keeps it from becoming a dumping ground of one-off contracts.

## Default profiles

Three profiles ship with Commonplace itself and back its own collections. They were the entire taxonomy before ADR 042; they persist unchanged in substance, only demoted from an exhaustive partition to proven defaults.

### Theoretical

| | |
|---|---|
| Orientation | Claims about what is true |
| Quality goal | Reach |
| Title convention | Claim-as-title |
| Attribution | Not required — first-person-committed |
| Maintenance | Upstream of the other two defaults; changes flow *from* theory into prescriptions and descriptions |
| Link grammar | Inference labels — `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts` |

Used by: `kb/notes/`. See its `COLLECTION.md`.

### Descriptive

| | |
|---|---|
| Orientation | Accounts for what exists |
| Quality goal | Fidelity + economy |
| Title convention | Topical |
| Attribution | Not required — first-person-committed to the referent ("accurate to the shipped system") |
| Maintenance | Downstream of theory and prescription; changes when the referent changes |
| Link grammar | Structural labels — `part-of`/`contains`, `implements`/`implemented-by`, `supersedes`/`superseded-by`, `compares-with` |

Used by: `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`. See each collection's `COLLECTION.md`.

### Prescriptive

| | |
|---|---|
| Orientation | Directs what to do |
| Quality goal | Executability + precision |
| Title convention | Imperative |
| Attribution | Not required — first-person-committed |
| Maintenance | Downstream of theory; changes when the theory or the system it directs action on changes |
| Link grammar | Operational labels — `composition`, `precondition`, `invokes`, `applies-when`, `operates-on` |

Used by: `kb/instructions/`. See its `COLLECTION.md`.

## Promoted profiles

### Dialectical / evidential

Proven outside this repo, in the sibling `epistack-casebooks` project (`kb/lhc/notes/COLLECTION.md`), across five casebook notes over eight captured sources for an LHC/black-hole-fears case. Not yet adopted by any collection inside Commonplace itself — listed here so a future casebook-shaped collection, in this repo or another consuming project, can start from a proven bundle instead of re-deriving one.

| | |
|---|---|
| Orientation | Maps a live, sourced disagreement between parties |
| Quality goal | Faithfully represents the state of contestation — not truth, not the author's belief |
| Title convention | Topical — a sub-question or a position-holder's stance, never an assertion in the collection's own voice |
| Attribution | **Mandatory evidentiality** — every proposition needs an attributed asserter (who holds this position) plus a source-span citation: not a bare file-level link, but a prose locator plus a grounding-layer marker (verbatim / paraphrase-layer / second-hand) |
| Maintenance | "Is this still an accurate map of the debate?" — stale when attribution drifts from what a party now asserts, or a new sourced position emerges. Not stale because a maintainer's own view changed, or because a position "lost" the argument |
| Link grammar | Provisional in its origin case — plain footer labels first; a Toulmin/IBIS-style vocabulary (`supports`, `rebuts`, `undercuts`, `depends-on`) is a candidate, not yet adopted |

Promoted by: [ADR 042](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md), on the strength of the worked case above.

## Limits

This catalogue is guidance, not a closed enum — see [ADR 042](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md). A collection can adopt a profile wholesale, extend one with local exceptions, or write its contract from scratch when none fits; the `COLLECTION.md` doing the adopting is what a note writer actually reads, not this page.

Narrative/log (`kb/log.md`, workshop state, backlog logs) is a recurring, real convention that is deliberately **not** a named profile here — nobody has written out its full contract the way the dialectical profile's was exercised, and the known instances may not even be the same profile. See ADR 042, Decision 4.

## Open questions

- Does the dialectical/evidential profile need a collection-local type (a `claim` schema mechanizing the attribution requirement) before a second consuming project can adopt it cheaply, or does `COLLECTION.md` prose keep working at this scale?
- Should narrative/log be written up and promoted once a second, deliberately-specified instance of it appears?

---

Relevant Notes:

- [Text contract](../notes/definitions/text-contract.md) — defined-in: the requirement this catalogue supplies proven bundles for
- [ADR 042: register becomes a default profile under open-ended text contracts](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — rationale: the decision that opened this catalogue and promoted the dialectical/evidential entry
- [Open-ended collection text contracts](./proposals/open-ended-collection-text-contracts.md) — rationale: the proposal and worked-case evidence ADR 042 ratified
- [link-vocabulary.md](./link-vocabulary.md) — compares-with: the sibling open, worked-case-gated catalogue this page is modeled on
