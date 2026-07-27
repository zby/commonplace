---
description: "Proposal: surface committed user verification at the point of reading through a standardized Markdown banner without turning absence into a review or truth verdict"
type: ../types/design-proposal.md
tags: [kb-maintenance]
---

# A reader-facing banner for user verification

[ADR 044](../adr/044-user-verification-replaces-global-note-status.md) retired the original version of this proposal: a warning derived from global note `status` or review-database state. It also supplied the narrower portable signal that makes a different banner possible. `user-verified: true` records one human attestation to the current substantive contents; absence records no attestation and says nothing about truth, maturity, currency, or review history. The open design question is whether and how that committed fact should be reinforced in the body where readers encounter it.

## Current state (as of 2026-07-26)

- The base note schema permits only `user-verified: true`; false is represented by absence. The [note type](../../types/note.md) owns the exact semantics.
- Creation, conversion, validation, and review never grant verification. A substantive edit removes it; only explicit human authorization may preserve it across a mechanical change.
- ProperDocs already renders `**User verified:** yes` in generated page metadata when the field is present. Raw Markdown consumers still have to notice and interpret frontmatter; there is no body-level signal.
- Review evidence remains local, criterion-specific, and model-partitioned in SQLite. It is deliberately not an input to user verification and cannot produce a universal reviewed/unreviewed banner.
- No validator checks a body banner against `user-verified`, because no standardized banner exists.

## Problem

The portable trust signal exists, but its presentation depends on the reader. ProperDocs promotes it into generated metadata; an agent or human reading the file directly must inspect frontmatter and know the field's semantics. A Markdown-native banner would put the attestation at the point of reading across renderers, but committing it would duplicate a recomputable fact. The design must make that duplicate coherent without strengthening the meaning of either presence or absence.

The old warning design is foreclosed. “Unreviewed” is not derivable from `user-verified`, and “not verified” easily reads as a truth warning even though absence means only that no human attestation is committed. Any banner must use the ADR 044 vocabulary exactly.

## Design space

1. **Keep generated presentation only.** ProperDocs continues to show the positive label; raw-file readers use frontmatter. No duplicate can drift, but the signal is not reinforced in every consumption channel.
2. **Commit a positive-only banner.** When `user-verified: true` is present, place a standardized line immediately below the H1: `> **User verified.** A human has verified the current substantive contents of this artifact.` Absence produces no banner. This is low-noise and cannot turn missing attestation into a warning, but readers cannot distinguish “not verified” from “banner mechanism not used.”
3. **Commit a binary banner.** Verified artifacts carry the positive line; all others carry `> **No current user verification.** No human attestation is committed for the current contents.` This makes absence explicit and universally visible, but puts a warning-shaped line on most artifacts and risks readers inferring more than the sentence says.
4. **Generate a banner at render time.** ProperDocs promotes its existing metadata label into a banner, positive-only or binary. This avoids a committed derived copy but reaches only the site; agents, GitHub readers, and other Markdown renderers still see no body signal.

Options 2 and 3 require deterministic consistency enforcement. The banner is a copy of frontmatter truth and must be checked or absent; author discipline alone is not enough.

## Forces

- **Semantic restraint.** Verification is human attestation to current contents, not certification, review completion, maturity, or currency.
- **Point-of-use visibility.** A body banner reaches file readers and agents that never consume the ProperDocs-generated metadata line.
- **Derived-copy safety.** A committed banner can outlive removal of `user-verified` unless a validator checks both directions.
- **Revocation cost.** Substantive editing already removes the field; a committed banner adds a second location every editing workflow must keep aligned.
- **Banner fatigue.** A binary banner would appear on most artifacts until verification becomes common, possibly teaching readers to ignore it.
- **Presentation duplication.** ProperDocs already presents the positive fact, so a body banner may repeat it on the rendered site unless the hook suppresses one form.

## Free choices

- Positive-only versus binary presentation.
- Committed Markdown versus render-time generation.
- Scope: ordinary note-family artifacts only, or any type that admits `user-verified`.
- Exact standardized wording and whether the rendered site suppresses its existing metadata label when a body banner is present.
- Whether banner insertion/removal belongs to general editing workflows or a dedicated human-authorized verification command.

## Operativity and warrant

A committed banner is consumed directly by human and agent Markdown readers with advisory presentation force: it exposes an attestation but changes no artifact authority. The validator would compare frontmatter presence with the exact banner form and fail on disagreement. Editing workflows that remove `user-verified` would also remove the banner, but no workflow may add either without explicit human authorization.

A generated banner is consumed only through the ProperDocs build channel; the hook already reads the field and would need only a presentation change.

The deterministic check warrants representational consistency only: “the banner agrees with committed frontmatter.” It cannot warrant that the human review was competent, that the contents are true, or that later external events have not made them stale. Those boundaries must remain explicit in the banner text and validator message.

## Adoption criteria

- A worked comparison shows that the banner improves recognition of committed human attestation for raw Markdown readers, not only on the ProperDocs site.
- Readers do not interpret absence as a review verdict or the positive banner as certification; the chosen wording preserves ADR 044's exact semantics.
- If the banner is committed, validation enforces presence, absence, and exact wording against `user-verified`, and substantive-edit workflows revoke both together.
- The rendered site has one clear presentation rather than an accidental duplicate label plus banner.
- The standing context and maintenance cost is lower than the reader error it prevents; otherwise the existing generated metadata label remains sufficient.

## Risks

- **False assurance.** “User verified” can be read as “true” or “approved” unless the attested object—current substantive contents—is named.
- **Negative-label overreach.** A missing attestation is not adverse evidence. Binary presentation may create that implication despite careful wording.
- **Drift.** An unchecked committed banner can claim verification after the field has been revoked. This is worse than relying on frontmatter alone.
- **Noise.** Ubiquitous negative banners can dominate short notes and become invisible through repetition.
- **Split presentation.** A body banner and generated metadata may diverge in wording or appear twice on the same page.

---

Relevant Notes:

- [ADR 044 — User verification replaces global note status](../adr/044-user-verification-replaces-global-note-status.md) — part-of: defines the portable signal and the semantic boundaries this proposal must preserve
- [Note type](../../types/note.md) — implemented-by: owns `user-verified` authoring and revocation semantics
- [Natural-language content lacks reliable dereference, so facts need reinforcement at point of use](../../notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — rationale: a body banner would restate the attestation at its consumption point
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: a committed banner is safe only when mechanically checked against frontmatter
- [Representational form](../../notes/definitions/representational-form.md) — defined-in: distinguishes committed Markdown presentation from the ProperDocs-generated view
