---
description: "Proposal: warn readers of unreviewed notes with a standardized top-of-note banner derived from review-state, kept consistent with the canonical status by a validator check"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# A reader-facing banner for unreviewed notes

The KB's bet is that quality comes from a human judging in the loop — *the work is reviewing.* But unreviewed notes get published anyway (the maintainer routinely promotes seedlings without a review pass), and the only "treat with caution" signal is the `status` frontmatter field. That field is invisible to a human reading rendered markdown and easy for an agent to skim past in the body. So the KB ships unjudged content with no signal at the point of reading — which makes the review discipline invisible and silently asks every reader to trust content the loop never checked. This proposal holds a design for the missing signal: a standardized **trust banner** at the top of a note, derived from its review-state, that warns the reader when the loop has not judged it — and a validator check that keeps the banner honest.

## Current state (as of 2026-06-30)

- **`status` exists but is metadata-only.** Notes carry `status: seedling | speculative | current` in frontmatter. It is machine-readable but not surfaced in the body; a reader of rendered markdown never sees it, and an agent reading the body may not foreground it.
- **Review-state is tracked, separately.** The review subsystem records accepted gate reviews in SQLite through `review_jobs`, `review_pairs`, and `acceptance_events` (consumed by `commonplace-review-target-selector`, `commonplace-warn-selector`, and ack commands). Whether a note has passed review is therefore known — but it lives in the review DB, not in the note.
- **Maturity and review-state are different axes.** A note can be `seedling` but reviewed, or `current` but stale-reviewed. `status` is a maturity proxy; it is not the same as "the loop judged this."
- **An ad-hoc precedent already exists.** Some notes (e.g. `llm-generation-confidence-tracks-typicality-not-soundness.md`) carry a hand-written italic `*Speculative…*` line under the H1. It is exactly this banner, done once, by hand, unstandardised and unenforced.
- **The validator counts seedlings** as a batch signal but checks no in-body warning.

## The design

A **trust banner**: a single standardized line immediately under the H1, present whenever a note's review-state warrants caution and absent (or downgraded) once the loop has judged it. Markdown-native — a callout or italic line that renders in any viewer and sits at the top of the body, where both a human and an agent meet it first. No new rendering surface is required.

**Keyed to review-state, not maturity.** The signal the reader needs is "has the loop judged this?", so the banner is driven by review-state (unreviewed / reviewed / stale-reviewed) where that is available, with `status` (seedling) as the cheap first proxy until the review-DB wiring is in place.

**Why denormalize — and why that is safe here.** The banner duplicates the canonical `status`/review-state: it is a denormalized copy, which a "one source of truth" instinct resists. For prose consumed at the point of reading, that instinct is wrong — the signal has to be *in the prose*, not only in metadata the reader never opens. The cost of denormalization is drift, and the **validator is the guard that removes it**: it checks that a banner is present exactly when review-state warrants, and that its text matches the canonical source. Denormalize the human-facing copy for reach-at-point-of-reading; normalize the *check*. (This trade is a transferable claim that may deserve its own note.)

**Tooling that keeps it honest.**

- `cp-skill-write` stamps the banner on creation for any note whose initial state warrants it.
- The **validator** enforces present-iff-warranted and text-matches-state — the load-bearing guard against drift.
- Review / promotion updates or clears the banner when a note is judged, so it never outlives the state it reports.

## Free choices

- **Key: `status` vs review-DB.** Drive the banner from `status` (cheap, available now, but a maturity proxy) or from accepted-review state in the review DB (principled, matches "the loop judged this", but needs wiring). Status-first with a review-DB upgrade path is the likely sequence.
- **Which states warrant a banner.** `seedling` only; `seedling` + `speculative`; or also `current`-but-stale-reviewed. Wider coverage is more honest but risks banner fatigue.
- **Form.** Italic line (the existing precedent), a blockquote/admonition callout, or an HTML-comment marker a render layer expands into a coloured badge. The italic/callout forms are agent-visible; a badge alone is not.
- **Scope.** All collections, or only `kb/notes/` (where unreviewed claims are most load-bearing). Reference and instruction artifacts may want a different signal.
- **Render-layer colour.** Out of scope for the markdown KB; available later if a rendered view is built, layered on the same status/review-state. Colour is not load-bearing — an agent cannot read it.

## Adoption criteria

Adopt when:

- a reader — human or agent — can tell judged from unjudged content **without opening frontmatter or the review DB**;
- the validator enforces banner-matches-state with low false-positive friction (it does not nag on notes that are correctly banner-free);
- the banner is cleared or downgraded automatically on review/promotion, so it does not become a stale label of its own;
- coverage is wide enough to be trustworthy but not so wide that readers learn to ignore it (if most notes are genuinely unreviewed, an honest banner on most notes is acceptable signal, not noise).

## Risks

- **Banner blindness.** If nearly every note carries it, readers tune it out. Mitigation: key it to a state that is actually discriminating, and downgrade it promptly on review.
- **Drift.** A denormalized banner the validator does not enforce becomes a false label — worse than none. The validator check is not optional; it is the reason denormalization is acceptable.
- **Wrong key.** Keying to `seedling` when the real signal is review-state under-warns reviewed seedlings and over-warns unreviewed `current` notes. Treat `status` as a temporary proxy, not the endpoint.
- **Scope creep into a render layer.** Colour is tempting but pulls toward building a rendering surface; keep the markdown banner load-bearing and colour strictly optional.

---

Relevant Notes:

- [Prose has no reliable dereference, so a declared fact must be reinforced where it applies](../../notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — rationale: the banner is a denormalized restatement of status/review-state at the point of reading, and the validator is the normalized check that makes the denormalization safe — this note's claim, applied
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — rationale: delegating the rendering is safe but the judgment must keep a human; an unreviewed note is one where that judgment has not yet happened, which is exactly what the banner must surface
