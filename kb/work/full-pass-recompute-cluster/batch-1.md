# Batch 1 — most-depended-on

Run [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md)
once per note, one note at a time. Read the
[workshop README](./README.md) for operating constraints before starting.

Status: not started.

## Notes

| # | Path | Status |
|---|---|---|
| 1 | `kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md` | not started |
| 2 | `kb/notes/documentation-generates-the-system-rather-than-describing-it.md` | not started |
| 3 | `kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md` | not started |
| 4 | `kb/notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md` | not started |

Order within the batch is not binding; all four are cited by batch 2, so any
order finishes the batch before batch 2 should start.

## Per-note context

**1. `llm-recompute-cost-inverts`** — the oldest note here and the least
examined against its new neighbours. Received a scope paragraph on 2026-08-23
naming the volume condition under which its materialization default flips back,
plus a `contrasts` edge to `addressability-grain`. That addition is a
propagation of a caveat its sibling `frontloading-spares-execution-context`
already carried, not a correction; the note's own instances sit far on the safe
side of the condition.

**2. `documentation-generates-the-system`** — written here, committed by a
concurrent session, which is why a commit-trailer filter misses it. Its central
move is a reconciliation with `commitment-not-derivation-creates-new-ground-truth`
rather than a flat inversion: the pair is bidirectionally irrecoverable, so
artifact-level "source of truth" is malformed.

**3. `superseded-choices-are-retained`** — scoped against
`artifact-classification`, which assigns the maintenance *operation*; this note
claims only what happens to *displaced content*. Watch that the distinction
survives a pass, since it is narrow.

**4. `human-recompute-is-dear-and-rare`** — retitled on 2026-08-23 from
"audience segmentation cannot be decided from one reader property", with a
redirect in `properdocs.yml`. Carries four consecutive "Consequence:" sections;
one of them, segmentation strips the drift detector from the low-traffic layer,
is a maintenance claim on an economics note and more general than its host.
Split candidate. Also cites Commonplace as an existential witness — the
collection-fit check is a live test of the bound-variable requirement here.
