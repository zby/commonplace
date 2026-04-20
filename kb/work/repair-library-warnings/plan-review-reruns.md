# Plan — agent-memory-system-review reruns

## Goal

Bring 4 reviews into conformance with the current `agent-memory-system-review` schema, which requires `## Core Ideas`, `## Comparison with Our System`, `## Borrowable Ideas`, `## Curiosity Pass`, `## What to Watch` (plus optional `## Trace-derived learning placement` when applicable).

## Targets

| Review | Missing sections | Likely state |
|---|---|---|
| `sift-kg.md` | `## Curiosity Pass` | Near-complete; one section to add |
| `siftly.md` | `## Curiosity Pass` | Near-complete; one section to add |
| `spacebot.md` | `## Core Ideas`, `## Comparison with Our System`, `## Curiosity Pass` | Half-review; likely early stub |
| `thalo.md` | `## Comparison with Our System`, `## Borrowable Ideas`, `## Curiosity Pass` | Half-review; likely early stub |

All four live under `kb/agent-memory-systems/reviews/`.

## Pre-action: keep / patch / delete decision (REQUIRED)

**Before any rerun**, the user decides per-review:

1. **Keep + rerun** — system is still worth tracking; invest the LLM spend on a full code-grounded rerun covering all required sections.
2. **Keep + patch** — system is still worth tracking but the gap is small; add the missing section(s) as a focused edit without a full rerun. Only viable for `sift-kg` and `siftly` (1 section each).
3. **Delete** — system is no longer worth tracking; remove the review file and sweep any backlinks.

Present the decision table to the user and wait for approval before any action.

## Preconditions for any rerun

For every review going down the **keep + rerun** path:

- `related-systems/<repo>/` checkout exists and its refresh marker is < 24h old (the review instruction enforces this).
- `repo_url` is known.
- Target path is `kb/agent-memory-systems/reviews/<system>.md`.

If the checkout is stale or missing, refresh it (or clone) first. Do not attempt a rerun against a stale local checkout.

## Execution model — keep + rerun

**Each kept review runs in its own subagent, sequentially.** Not parallelised. Sequential runs match the review-bundle discipline, keep each review's context and diff clean, and let the outer agent spot quality issues before moving on.

Per-subagent prompt shape:

- **Input:** `repo_url`, `checkout_dir`, `note_path`, plus the existing review file as prior art.
- **Action:** author a full review per `kb/instructions/write-agent-memory-system-review.md`. The review is written from the code outward and must cover all required sections.
- **Output:** overwritten `<system>.md` conforming to the current schema.
- **Post-action in the subagent:** run `commonplace-validate <path>` and report any residual warnings.

Outer-agent loop:

1. Refresh the checkout or confirm it is fresh.
2. Spawn subagent N for the next review.
3. Wait for completion.
4. Review the output:
   - All required sections present.
   - Claims are grounded in the reviewed commit, not marketing.
   - Borrowable-ideas section names a concrete commonplace shape, not a vague gesture.
   - Curiosity Pass surfaces real second-pass observations, not filler.
5. If acceptable, commit. If not, re-prompt with tighter guidance or abort that review.
6. Move to subagent N+1.

## Execution model — keep + patch

For `sift-kg` and `siftly`, if chosen:

- Load the existing review.
- Briefly re-read the reviewed commit's code for grounding (even a patch must be code-grounded).
- Add the missing `## Curiosity Pass` section: surprises in the mechanism, simpler alternatives, capability ceilings even if the system works perfectly.
- Commit per review.

Can be done by a subagent with the existing review loaded, or directly by the outer agent. Either way, grounding in the repo is required.

## Execution order

1. Patch path first (cheap): `sift-kg`, `siftly` if chosen keep+patch.
2. Sequential reruns: `spacebot`, then `thalo` (if kept).

## Closure

- Each kept review passes `commonplace-validate kb/agent-memory-systems/reviews/<file>.md` on headings.
- Each deleted review has its file removed and any backlinks cleaned.
- The decision table is recorded as an appendix to this plan (or a short `decisions.md` alongside it).

## Deferred / out of scope

- Review schema changes. If the schema's section requirements are themselves wrong, that's a separate workshop.
- Bulk review creation for systems without existing reviews.
- Trace-derived placement refactors across the existing review corpus.

## Appendix — decision record

To be filled in at gate time:

| Review | Decision | Notes |
|---|---|---|
| `sift-kg.md` | Keep + patch | Added missing `## Curiosity Pass`; existing review already had required core/comparison/borrow/watch sections. |
| `siftly.md` | Keep + patch | Added missing `## Curiosity Pass`; existing review already had required core/comparison/borrow/watch sections. |
| `spacebot.md` | Keep + patch | Source re-read showed the review was not a half-stub; required content existed under older mechanism-specific headings. Renamed section structure and added `## Curiosity Pass` instead of doing a full rerun. |
| `thalo.md` | Keep + patch | Source re-read showed comparison and borrowable material existed under older local headings. Renamed section structure and added `## Curiosity Pass` instead of doing a full rerun. |
