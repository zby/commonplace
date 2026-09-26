# Workshop: write-brief pilot

## Goal

Test, under conditions where they could fail, the conjectures behind the [per-artifact write-brief proposal](../../reference/proposals/per-artifact-write-briefs.md): that a retained commission changes what later writers preserve, that its value lies in what the artifact cannot show, and that it cannot be rebuilt from the finished artifact. The expected result ("briefs help") is close to obvious. The pilot is worth running only if it could come out otherwise, so the conjectures, refutation conditions, and scoring are fixed in [protocol.md](./protocol.md) before any run.

The result feeds two consumers: the adoption decision on the write-brief proposal (which option, and whether delivery Route A is enough), and an evidence note in `kb/notes/evidence/` that records what the runs establish and where that stops, whichever way they come out.

## Posed

By the operator, 2026-09-26, after the proposal was decoupled from the context assembler (`c8eba794`). The operator's framing: the pilot looks trivial, but something surprising may appear, and the record may later be kept as evidence. The operator asked for a Popperian design.

## Status

Protocol drafted, awaiting operator approval. **No run may start before the commit that marks the protocol `frozen`.** That commit is the pre-registration.

## What closes this workshop

1. All runs in the protocol completed and scored, including null and failed runs.
2. Each conjecture recorded as refuted, survived, or undecided, against the refutation conditions as frozen.
3. An evidence note written in `kb/notes/evidence/`, whatever the outcome.
4. The write-brief proposal's current-state anchor updated with the result, with a link to the evidence note, and any option the result forecloses removed.

Then delete the workshop. The stripped briefs, rubric, and raw scores stay recoverable from git.

## Evaluation boundary

The evidence concerns this installation's `cp-skill-write`, with Claude models as writers and scorers, on ten targets whose commissions were written inside multistage runs or workshops before the final draft. Those commissions are unusually careful, not typical ones. Generalization beyond that goes through the evidence note's stated limits, not through this record.

## Pre-run observations

Recorded before any experimental run, so they cannot be read as results.

- **Target 4 lost its commissioned content within a day.** The commissioned portfolio row landed at `69cbae6a` (2026-08-29) and was removed at `2b406eea` (2026-08-30), inside a large squashed recenter by another model whose messages do not mention it. The per-portion rule itself survives in another note. Whether the removal was deliberate is not recoverable from the record.
- **Target 5's commissioned rewrite never reached the library.** The candidate passed acceptance and won a blind comparison 3–0 against the incumbent, but the workshop closed at `c7484bea` with the library note untouched pending a human promotion that never happened.
- **Several targets moved away from their briefs, apparently deliberately** (targets 8 and 10; target 6 through its own amendment). A retained brief would be stale for them. See `drift-at-head/`.

## Constraints

- No run edits a library artifact. Every write goes to a copy inside this workshop.
- Deviations from the frozen protocol are recorded in `deviations.md` with their reason before the affected run, never after its score is seen.
- Scorers never learn which arm produced an output.

## Bookkeeping

- `protocol.md` — conjectures, refutation conditions, arms, targets, rubric, and procedure
- `briefs/` — the ten original commissions with run-bound items removed (prepared before freeze; operator-reviewed)
- `rubric/` — commission items per target and their recoverability classification (prepared before freeze)
- `runs/` — one directory per run: input packet, output candidate
- `scores/` — blind scores
- `deviations.md` — created on first deviation

Plain markdown, no frontmatter.

---

- [Per-artifact write briefs](../../reference/proposals/per-artifact-write-briefs.md) — tests: the proposal whose conjectures this pilot tries to refute
- [Genre-drift cohort result](../popperian-maintenance-episode/genre-drift-cohort-result.md) — draws-on: the earlier question refuted for lacking a denominator; why every run is counted here
