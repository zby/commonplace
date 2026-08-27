# Workshop: atomic-step-adoption

## Goal

Adopt the artifact-side bound on grounding — a note is sized so its grounding check fits one pass, with the unquoted source as the unit — and retire the review-side reading caps it replaces. The mechanism question of [review-attention-price](../review-attention-price/README.md) is decided in this option's favour; what remains is the set of operational decisions the [proposal](../../reference/proposals/atomic-step-grounding-bounds-unquoted-sources-per-note.md) left free, plus the criterion and validator changes that make the decision binding.

Posed 2026-08-27 by the maintainer: "I am now convinced we should go with atomic steps." First order of business, in the maintainer's words: decide whether `sentence/concept-attribution` and `sentence/misleading-link-text` keep their limits at all — "misleading link with only head check sounds cheap" — and change the grounding gate.

## Decisions this workshop owns

In the order they should be taken; later ones depend on earlier ones.

1. **The two representation gates' limits.** Under the note-link exemption these gates are what makes the exemption sound (precondition 3 of [the exemption note](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md)), and today both read at most five distinct targets while 55% of notes link more than five. See [representation-gate-limits.md](./representation-gate-limits.md) — analysis and recommendation.
2. **The grounding gate's new shape.** `semantic/grounding-alignment` counts every linked artifact alike against sixteen. It has to distinguish linked notes (representation, head check, uncounted), quoted sources (judge the passage on the page, uncounted), and unquoted or `(snapshot required)` sources (full route, bounded by the validator rather than by the gate). Open sub-question: does the claim-level representation check on linked notes ("cited as grounding more broadly than it does") stay in this gate with a head-only reading rule, or move wholly to the two sentence gates?
3. **The validator rule.** Count of distinct source targets per note without a paired verified quotation; the `## Quotes`-section confinement of `verify_content` for ingest targets (required, per the proposal); what counts as a source — `kb/sources/` only, or also external URLs and artifacts in other library collections (ADRs, reviews), which have descriptions and their own checks and are closer to notes.
4. **N, fail-or-warn, `(snapshot required)` handling, articles.** The proposal's free choices. N is a convention for auditability, not a measurement, so this is a commitment, not an estimate.
5. **Bookkeeping.** ADR 079 is superseded; the review-attention-price workshop closes; Track A (usage telemetry) survives only if someone wants the side measurement; Mechanism B is the recorded rejected alternative.

## Evidence to gather

The eight notes over five sources: can each be quoted or split without losing its claim? This is the one force against the option that is not yet answered, and it decides fail-versus-warn more than any argument does. It runs without touching a production criterion. Watch for the quote-inflation tension the atomic-step note now names: quoting spends against the co-loading bound.

## What closes this workshop

One ADR recording decisions 1–5, the criterion edits batched with it (each edit stales its population once, so batch), the validator rule in `commonplace-validate`, the proposal moved to adopted, and this directory deleted.

## State (2026-08-27, end of day)

Decisions 1–5 are taken and recorded in [ADR 082](../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md); the three gate edits, the validator rule (WARN, N=5), the `## Quotes` confinement, and the wrapped-quote parser fix are on disk with tests. Uncommitted. Remaining, each waiting on the maintainer:

- commit the batch (ADR + gates + validator + notes + workshop);
- archive the adopted proposal (retire-artifact steps 5–7; no library artifact links into it);
- close [review-attention-price](../review-attention-price/README.md) (delete, drop its index entry);
- decide whether the two review-side proposals (*Review link budget prices reviewer attention*, *Exceeding a review budget splits the task*) and *Review budget enforcement is separable* are retired now or left on the frontier;
- conform the eight notes ([trial](./eight-note-trial.md)) and fix the three ingest defects it found;
- then flip WARN to FAIL and close this workshop.

## Files

- [representation-gate-limits.md](./representation-gate-limits.md) — decision 1: corpus data on distinct note-link targets, cost per target for each gate, recommendation
- [gate-text-drafts.md](./gate-text-drafts.md) — decision 2: the three criteria's new `## Test` text (now applied)
- [eight-note-trial.md](./eight-note-trial.md) — the conformance trial that settled N and fail-or-warn, plus the defects it exposed

## Grounding

- [Atomic-step grounding bounds unquoted sources per note](../../reference/proposals/atomic-step-grounding-bounds-unquoted-sources-per-note.md) — tests: this workshop is its adoption
- [A note is an atomic step relative to the check that reads it](../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — rests-on: the unit and what kind of number N is
- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — rests-on: the exemption and its three preconditions, the third of which decision 1 has to make true
- [review-attention-price](../review-attention-price/README.md) — supersedes: the mechanism fork is resolved; its Track A and Mechanism B designs are the retained alternatives
- [ADR 079](../../reference/adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — supersedes: the interim ceiling this replaces
