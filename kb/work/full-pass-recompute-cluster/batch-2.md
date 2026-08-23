# Batch 2

Run [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md)
once per note, one note at a time, **in the order listed**. Read the
[workshop README](./README.md) for operating constraints before starting.

**Do not start until [batch 1](./batch-1.md) is complete**, including any
reframe follow-up it triggers. Every note here cites batch 1, so a batch-1
reframe moves these notes' premises before their own pass would read them.

Status: blocked on batch 1.

## Notes

| # | Path | Status |
|---|---|---|
| 5 | `kb/notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md` | blocked |
| 6 | `kb/notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md` | blocked |
| 7 | `kb/notes/addressability-grain-not-compression-ratio-decides-whether-a.md` | blocked |

Order is binding: 7 cites 5, so 5 must settle first. This is the one dependency
edge that falls inside a batch rather than across the boundary.

## Inbound dependencies on batch 1

- 5 `human-recompute` **contrasts** batch 1's note 1.
- 6 `a-theory-may-name` **contrasts** batch 1's note 2 and cites batch 1's note
  3 `evidenced-by`.
- 7 `addressability-grain` **grounds** on batch 1's note 1, **extends** batch 1's
  note 4, and **contrasts** note 5 in this batch.

Recheck each edge before its pass: if the target was reframed, the citing
sentence here may state a claim its target no longer makes.

## Per-note context

**5. `human-recompute-is-dear-and-rare`** — retitled on 2026-08-23 from
"audience segmentation cannot be decided from one reader property", with a
redirect in `properdocs.yml`. Carries four consecutive "Consequence:" sections;
one of them, segmentation strips the drift detector from the low-traffic layer,
is a maintenance claim on an economics note and more general than its host.
Split candidate — deciding it before the pass would be legitimate, but deciding
it *during* is what the pass is for. Cites Commonplace as an existential
witness, so the collection-fit check is a live test of the bound-variable
requirement here.

**6. `a-theory-may-name-a-choice-only-as-a-bound-variable`** — two authors. The
initial write was revised by a second agent, which replaced a section and
dropped a ranking of the two repairs in favour of a selection rule. Its
empirical section restates sweep evidence rather than citing it, because the
notes contract forbids outbound links into `kb/work/` and the source workshop
has since been deleted; that restatement is deliberate and should survive the
pass. This note also states the rule the pass's own collection-fit check
applies, so a finding against it deserves extra scrutiny either way.

**7. `addressability-grain`** — newest of the seven, written last. Its claim is
scoped to the recoverable-cache partition, which is what keeps the "only when"
universal rather than hedged; a pass that widens the scope would break that. Its
central evidence is a pair of instances running opposite ways under one rule, so
a compression finding that trims one instance would remove the discrimination
the note rests on. Cites Commonplace as an existential witness.
