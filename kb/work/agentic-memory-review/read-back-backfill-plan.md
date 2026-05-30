# Read-back placement — backfill plan

Handoff from the [read-back-placement workshop](../read-back-placement/README.md), which added a `## Read-back Placement` section + `push-activation` tag to the [agent-memory-system review type](../../agent-memory-systems/types/agent-memory-system-review.md). This plan applies that section to the **legacy** review corpus. New reviews that already contain read-back treatment are explicitly skipped.

## Goal

- **Every** legacy non-archived review carries a one-line **direction verdict** — pull / push / both, from the agent's perspective.
- Reviews of systems with a **relevance-gated or engineered activation path** also get the full `## Read-back placement` section and the `push-activation` tag.

## Scope

- **In:** the **96 legacy** non-archived review files in `kb/agent-memory-systems/reviews/` that do not already contain the new read-back treatment.
- **Out:** `dir-index.md`, all `*.replaced.*` archived reviews, and the four new reviews that already contain read-back treatment: `a-mem.md`, `graphiti.md`, `letta.md`, and `mem0.md`.
- Target queue: [`read-back-backfill-targets.txt`](./read-back-backfill-targets.txt) lists the 96 in-scope review paths in deterministic order.
- Inventory + clone paths: [`systems.csv`](./systems.csv) (100 systems; `path to cloned repo` gives source for Tier B).

## Two tiers (match the gating rule)

| | Tier A — direction verdict | Tier B — full section + tag |
|---|---|---|
| Applies to | all 96 | engineered-activation subset only |
| Source needed? | **No** — re-express what the existing review already documents | **Yes** — re-read source for the 6 axes |
| `last-checked` | **do not bump** (not a re-inspection) | **bump** + record `reviewed_revision` |
| Adds tag? | no | `push-activation` |
| Cost | cheap, batchable | expensive |

**Freshness rule (non-negotiable):** the Tier-A one-liner is a *classification of existing review findings under the new axis*, not a fresh source claim — so it must **not** touch `last-checked`. Only Tier B, which actually re-reads source, updates freshness metadata. If an existing review lacks enough detail to classify direction, write `direction: unclear (needs source)` rather than guessing — never invent a push/pull claim the prior review doesn't support.

## Phases

### Phase 0 — Triage from existing review text (cheap, no source)

Read each in-scope legacy review's existing retrieval/navigation prose and bucket it:

- **pull-only** — retrieval/query interface, no proactive injection → Tier A one-liner, no tag.
- **always-load-only** — unconditional context injection, no relevance gating → Tier A one-liner (name always-load as a deliberate push choice), no tag.
- **engineered-activation** — a matcher (embedding / action-classifier / LLM-judge / typed cue), scope budget, before-action hook, or faithfulness test → **Tier B shortlist**.
- **unclear** — prose insufficient to classify → needs a source peek before Tier A.

Output: the Tier-B shortlist + the unclear set. The 69 `trace-derived` reviews are the highest-yield place to look for engineered activation, but learning ≠ activation — confirm each independently.

### Phase 1 — Tier-A sweep (all 96)

Add the one-line direction verdict to every in-scope legacy review (placed in *Comparison with Our System* or *Core Ideas*; no fixed heading — the one-liner is not schema-gated). Resolve `unclear` cases with a quick source check (clone path in CSV). Do **not** bump `last-checked`. Do not edit the four skipped new reviews.

### Phase 2 — Tier-B full sections (shortlist)

For each engineered-activation system: re-read source, write the `## Read-back placement` section (direction, trigger, timing, scope, authority-at-consumption, faithfulness, other consumers), add `push-activation` to `tags`, mark precision/dilution/effective-authority as not-verified-from-code, report library API surface as capability. Bump `last-checked` + `reviewed_revision`.

### Phase 3 — QA + validate

- `uv run commonplace-validate` over the reviews dir — the schema conditional enforces `push-activation` ⇒ body contains "Read-back placement", catching tag/section mismatches.
- Spot-check a random sample of Tier-A verdicts against source for classification accuracy.

## Execution mechanics

- **Track in a dedicated ledger** `read-back-backfill-ledger.csv` keyed by review *filename* (`review_file,direction,tier,source_checked,notes`) for the 96 processed legacy reviews — cleaner than wedging columns into `systems.csv`, which is keyed by system, not by review file. See the Tier-A instructions.
- **Queue:** assign reviews from `read-back-backfill-targets.txt`. For one-by-one sub-agent execution, give each worker exactly one path from the target queue and require it to process only that path.
- **Batching:** 96 reviews is fan-out-shaped. A multi-agent workflow (Phase 0 triage in parallel → Phase 1/2 per-review) is the efficient execution, **but only on explicit opt-in** — say "workflow" to authorize it; otherwise this proceeds as sequential one-file agent passes.
- **Guardrail:** validation after each batch, not just at the end.

## Recommended integration with the review pass — hybrid

Do **not** run Phase 2 as a standalone sprint. Recommended:

1. **Now:** Phase 0 + Phase 1 (the cheap one-liner sweep over all 96) as a standalone task — gives full direction coverage immediately and is the high-value, low-cost half.
2. **Riding the next review pass:** Phase 2 full sections land **when each shortlisted system is re-reviewed anyway** (it needs source either way). This avoids a second source-read just for read-back and keeps `last-checked` honest.

This matches the default already recorded in the read-back-placement workshop: new reviews carry the section; existing ones get the one-liner now, full section on re-review.

## Definition of done

- All 96 in-scope legacy reviews have a direction verdict or an explicit `unclear` flag.
- Every engineered-activation system that has been re-reviewed has a full section + `push-activation` tag.
- `read-back-backfill-ledger.csv` reflects per-review status for the 96 processed legacy reviews.
- Validation passes clean across the reviews dir.
- (Until Phase 2 fully rides out the review pass, "done" for full sections is tracked per-system, not as a single sprint completion.)

## Risks / cautions

- **Honesty of freshness** — the main trap. Batch tooling must be wired so Tier A cannot bump `last-checked`. Treat any Tier-A edit that touches freshness metadata as a bug.
- **Learning ≠ activation** — don't auto-promote `trace-derived` reviews to `push-activation`; classify activation on its own evidence.
- **Library under-determination** — for SDK/library reviews, the repo may show only pull primitives; report capability, don't assert deployed push, and don't force a Tier-B section where the host wiring is invisible.
- **Silent truncation** — if a run caps coverage (e.g. top-N), log what was skipped; partial coverage must not read as complete.
