# Gate system design

## Gate files

One check per markdown file:

```
kb/instructions/review-gates/
  frontmatter/
    title-body-alignment.md
    description-discrimination.md
    title-composability.md
    claim-strength.md
  prose/
    source-residue.md
    pseudo-formalism.md
    ...
  accessibility/
    undefined-term.md
    notation-opacity.md
    ...
```

Gate frontmatter:

```yaml
---
gate_id: frontmatter/title-body-alignment
name: Title-body alignment
lens: frontmatter
watches: [title, body]
staleness: rewrite(0.5)
---
```

- **`gate_id`** — stable machine identifier. Survives file renames. Recorded reviews are keyed by this, so changing it orphans history.
- **Gate change detection** — the selector computes the git blob hash of the gate file and compares it to the hash stored in the recorded review. Any change to the gate file invalidates old recordings. This is intentionally aggressive — even small wording changes could affect what the gate catches. If re-evaluation noise becomes a problem, a manual version field is a future optimization.

Gate body:

```md
## Failure mode

## Test

## Example (fail)

## Example (pass)
```

That's it. ~20-30 lines per gate.

### `watches` and `staleness`

Each gate declares what note regions it cares about and how to detect staleness:

- **`watches`** — which parts of the note the gate reads: `title`, `description`, `frontmatter`, `body`, or combinations.
- **`staleness: changed`** (default) — hash the watched regions; stale if hash differs from accepted.
- **`staleness: rewrite(threshold)`** — applies only to `body` in the watches list. Non-body watched fields (title, description, etc.) still use exact-change detection. Body changes are stale only if they exceed the threshold. This covers the title-body-alignment case: a title change always triggers re-review, but a small body edit does not.

Two staleness modes, not seven comparator primitives. The `rewrite` mode is a refinement of `changed`, not a replacement — it relaxes staleness for body only.

## Bundles

A bundle is a lens name resolved directly from the gate tree. There is no separate manifest directory:

```
kb/instructions/review-gates/
  frontmatter/
    ...
  prose/
    ...
  accessibility/
    ...
```

Running `frontmatter` means "use every gate file under `kb/instructions/review-gates/frontmatter/`."

No membership CSV or bundle manifest file. If you need to resolve a bundle programmatically, enumerate `*.md` under the corresponding lens directory.

## Recorded reviews

One recorded review per `(note, gate)`:

```
kb/reports/reviews/gates/{encoded-note-path}/{gate-id}.md
```

The review file stores its metadata in a leading comment:

```md
<!-- GATE-REVIEW
note-path: kb/notes/backlinks.md
gate-id: frontmatter/title-body-alignment
gate-hash: 3f7b2a...
recorded-commit: cfa5a8...
watched-hash: 7a4d...
recorded-at: 2026-03-26T10:15:00+01:00
-->

## Title-body alignment — kb/notes/backlinks.md

CLEAN — title matches body scope.
```

## Staleness CSV

A derived index so the selector doesn't reparse every review file:

```
kb/reports/reviews/csv/gate_reviews.csv
```

Columns:

```
note_path, gate_id, gate_hash, recorded_commit, watched_hash, recorded_at
```

Regenerated from review file metadata. The selector reads this CSV, not the review files.

## Staleness check

1. **First pass — gate change.** Compute the git blob hash of each gate file, compare to `gate_hash` in the CSV. Mismatched = stale. The gate changed; old acceptances don't count.

2. **Second pass — git filter.** `git diff --name-only <oldest-recorded-commit> HEAD` gives changed note files. Notes that haven't changed skip all gate checks. This is the big optimization — most notes won't have changed.

3. **Third pass — per gate.** For each changed note, for each gate:
   - `staleness: changed` — hash the note's watched regions, compare to `watched_hash` in CSV. Different = stale.
   - `staleness: rewrite(threshold)` — hash non-body watched fields (title, description, etc.); if any differ, stale immediately. For body: `git diff` the note at `recorded_commit` vs HEAD, measure change ratio. Above threshold = stale.

4. **Missing reviews.** If a `(note, gate)` pair has no row in the CSV, it's stale (never reviewed).

## Selection and execution are separate

**Selection** operates at the `(note, gate)` level. The selector emits stale pairs — no bundle logic, no note-level aggregation. This avoids false positives (note selected for gates that aren't stale) and false negatives (note skipped because some gates are fresh).

A bundle is a user-facing entry point, not a selection unit. "Run frontmatter-review" means: consider only gates belonging to that bundle during selection. The bundle constrains *which gates to check*, not which notes.

**Execution** groups stale pairs for review calls. Grouping affects review quality — mixing lenses (e.g. prose + accessibility) can cause the reviewer to conflate findings or lose focus. Group by `lens` (already in each gate's frontmatter):

1. Selector emits stale `(note, gate)` pairs.
2. Group by `(note, lens)`. Each group becomes one review call.
3. Load the note + the stale gates for that lens. Produce findings.
4. Feed all findings (across all lenses) for a note to an applicator with a directive. Applicator prioritizes and edits.
5. Write recorded review files. Regenerate CSV.

## What this design does not include

- Legacy adapters for current bundle reviews — start fresh
- Gate lifecycle management (candidate/active/retired) — all gates are active; delete ones that don't work
- Contract fingerprints or scope fingerprints — `gate_hash` + `watched_hash` is enough
- Separate CSV indexes for gate definitions or bundle definitions — read the files
- Comparator parameter framework — two staleness modes cover the known cases
