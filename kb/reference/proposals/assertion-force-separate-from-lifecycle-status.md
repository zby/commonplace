---
description: "Proposal: split status semantics — lifecycle stays a structural enum; what commitment 'current' expresses (endorsed, attributed, captured) becomes contract-defined assertion force"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system]
status: seedling
---

# Assertion force separate from lifecycle status

The base note type defines `status` as a **commitment level** (`seedling`, `current`, `speculative`, `outdated`). That one field fuses two axes: **lifecycle** (how far along the artifact is — structural, genuinely global) and **assertion force** (what the KB's relation to the content is — first-person endorsement, today, everywhere). The fusion is invisible while every collection is first-person-committed, and breaks the moment one isn't: for an attributed claim ("Rootclaim asserts X"), `status: current` is ambiguous between "I still endorse X" and "this still accurately records what Rootclaim asserts" — different maintenance questions with different falsifiers. This proposal separates the axes: the enum stays structural in the type, and what commitment `current` expresses becomes a feature each collection's `COLLECTION.md` declares.

## Current state (as of 2026-07-08)

- `kb/types/note.md` defines `status` as "Commitment level: `seedling`, `current`, `speculative`, or `outdated`" — endorsement semantics hardwired at the global type surface, one level above the collection contracts that own other text features (ADR 017).
- Assertion force is currently encoded **implicitly by collection placement**: `kb/notes/` artifacts are endorsed ("do I still believe this?" maintenance, falsifier practice), `kb/sources/` artifacts are captured (answerable to their source, not endorsed). No artifact or contract states this; it is folklore that holds because every existing collection is first-person-committed.
- The system already solved the mirror-image problem on the other side: [behavioral authority](../../notes/definitions/behavioral-authority.md) exists because "is this artifact active?" was ambiguous for system-definition artifacts, and the fix was to name consumer/channel/force explicitly. Knowledge artifacts have no analogous concept for who asserts the content and with what force.
- The pressure case is live: the epistack casework (see the `kb/work/epistack-framework-additions/` workshop) plans a stance-neutral collection of *attributed* claims the KB explicitly does not endorse, where the fused field is ambiguous on every artifact. Its `claim` type sketch has already tripped over this once (a `contested`/`settled`/`open` status enum colliding with its own no-stance-fields rule).
- This is the predicted fourth instance of the taxonomy demotion pattern — rationale: [a universal knowledge framework demotes content taxonomies to defaults and keeps answerability](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) names the status/endorsement fusion as "one answerability relation hardwired one level too high."

## The design

1. **Lifecycle stays in the type.** The `status` enum and its values are structural and remain global: every knowledge artifact ripens, holds, or goes stale, whatever its force. Validators keep checking the enum unchanged.
2. **Assertion force becomes a contract feature.** Each writable collection's `COLLECTION.md` states what commitment its artifacts carry — equivalently, what an artifact here *answers to* and therefore what `current` asserts. For `kb/notes/`: "current = the KB still endorses this claim." For a casebook collection: "current = the attribution is still accurate; the KB endorses nothing here." For `kb/sources/`: "current = the capture is faithful; content force is quoted."
3. **No new frontmatter field by default.** Force is uniform within a collection, so placement plus contract carries it — the same encoding choice ADR 017 made for register, for the same reason (a per-artifact field would be one more thing to set wrongly). A per-artifact field becomes worth revisiting only if a real collection needs mixed force in one directory.
4. **A small named vocabulary as the default library.** Endorsed / attributed / captured cover the known cases and give contracts a shared word; the set is open under the same worked-case guard as other demoted taxonomies.

## Forces

- **For: the ambiguity is real and cheap to fix.** The fix is prose in contracts that already exist, plus one clarifying edit to the `status` field's definition ("commitment level" → "lifecycle; the commitment it expresses is defined by the collection contract").
- **For: precedent symmetry.** Behavioral authority already establishes that "what force does this have?" is contract-and-consumption-path information, not a property of bytes; this applies the same move to knowledge artifacts.
- **Against: no shipped collection needs it yet.** Every current collection is first-person-committed, so today the change buys only definitional hygiene. Adopting before the casework proves the need would violate the build-local-first boundary.
- **Against: implicit-by-placement has a failure mode.** An artifact moved between collections silently changes force, just as ADR 017 accepted for register conventions. The mitigation is the same: moves between collections are already semantic events.

## Free choices

- **Naming.** "Assertion force" (parallel to behavioral authority's force) vs. "epistemic commitment" vs. reusing "answerability relation" from the theory note.
- **Whether `speculative` folds into the same axis.** `speculative` is arguably force (reduced endorsement), not lifecycle — under this split it could become a contract-level note rather than an enum value. Cheapest is to leave the enum untouched and let contracts gloss it.
- **Where the default vocabulary lives** — in the type spec, in a definition note, or only in each contract.

## Adoption criteria

Adopt when the first non-endorsed collection ships and its contract has to answer "what does `current` mean here" — the epistack casebook's collection is the expected trigger. Adopt whichever mechanism its worked case actually used; if the casework never needs the distinction, retire this proposal as YAGNI.

---

Relevant Notes:

- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — rationale: assertion force is one answerability relation among several; hardwiring one at the type level is the fusion this proposal undoes
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rationale: the precedent — force belongs to the consumption path and contract, not to bytes; this proposal is its knowledge-artifact mirror
- [ADR-017: COLLECTION.md is the register convention boundary](../adr/017-collection-md-is-the-register-convention-boundary.md) — part-of: the contract surface and the placement-carries-semantics trade-off this proposal reuses
- [Open-ended collection text contracts](./open-ended-collection-text-contracts.md) — see-also: companion proposal; both demote a fused global commitment to a contract-declared feature
