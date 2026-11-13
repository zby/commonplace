# Second results: three revised wordings on opus

Round two of this workshop, run on 2026-11-13 on `opus` only. The two
revised direct wordings found 5 of the 16 labelled positives and proposed
nothing on the 14 kept notes. The stage-one `opus` probe of the old direct
wording had found 0 of the 10 positives it covered. Removing the base-rate
sentence changed no outcome. The revised claim wording found 4 of 16 and
proposed nothing on the 7 kept notes it was run on. Most positives are still
missed. The counts below are counts. A set this small supports no rate
estimate. The labels are in [labelled-set.md](./labelled-set.md).

## The wordings

- (a) [direct-value](./wordings/direct-value.md), id
  `higher-order/direct-value`: the stage-one direct wording, plus four
  changes. It asks the value test ("if this note were deleted and its one
  best sentence added to its parent, what would a reader lose?"). It says
  that a parent's `extends` link is neutral and not evidence of ownership.
  It names the collection's `COLLECTION.md` as an input to read before
  judging place. It also lists the notes that link to this one as inputs.
- (b) [direct-value-no-base-rate](./wordings/direct-value-no-base-rate.md),
  id `higher-order/direct-value-no-base-rate`: (a) with one paragraph
  removed. That paragraph says that most notes need no change, and that
  WARN must not be used for doubt the worker cannot ground. Everything
  else, including the name and description, is byte-identical to (a)
  except the gate id.
- (c) [claim-need](./wordings/claim-need.md), id `higher-order/claim-need`:
  the stage-one claim-ownership wording, revised. Step 3 asks which notes
  would need each contribution, not which note states it. Step 4 asks
  whether the central claim adds anything beyond its premises. Step 5 asks
  the worker to quote the collection contract on place. It keeps the
  base-rate paragraph, as (a) does.

No wording has worked examples. A neutral example of each kind would have
to be written from outside the labelled set, and that is not done yet.

## How it was run

- **Method.** Same as stage one. Each note was judged in a detached
  worktree at its commit, in the session scratch directory, with
  `kb/work/`, `kb/reports/`, `kb/log.md`, `kb/messages/` and the
  session-start hook script deleted. `COMMONPLACE_LIBRARY_ROOT` pointed at a
  scratch library holding byte-identical copies of the three wording files.
  Nothing was added to `kb/instructions/review-gates/`.
- **Profile.** `opus` (claude-code, Opus, medium effort, read tools only),
  `--grouping pair`, `--max-workers 4`.
- **Coverage.** (a) and (b) ran on all 30 notes. (c) ran on the 16
  positives and on K01 to K07, which is 23 notes. It stopped there to stay
  inside the spend limit; K08 to K14 were not run with (c). The kept notes
  for (c) were chosen in labelled-set order before any (c) result existed.
- **Collection contract.** The fixed prompt confines grounding reads to
  linked files. It did not stop the read: 29 of 30 (a) launches, 28 of 30 (b)
  launches and all 23 (c) launches read the note's `COLLECTION.md`. The
  reading-scope conflict recorded in stage one is therefore a wording
  conflict, not a block on `opus`.
- **Guard and exits.** All 52 sweeps exited 0 with a clean guard.

## Outcomes on the positives

A hit is `warn` (weak) or `fail` (strong). The kind is the one the worker
gave. The stage-one `opus` column is the old direct wording, for comparison
("—" where stage one did not run it).

| ID | Label | (a) direct-value | (b) no base rate | (c) claim-need | stage one, direct, opus |
|---|---|---|---|---|---|
| P01 | reject (merge residue) | **warn**, merge | **warn**, merge | pass | pass |
| P02 | different-claim | pass | pass | pass | pass |
| P03 | reject | **fail**, different-claim | **fail**, different-claim | **fail**, different-claim | — |
| P04 | reject (obsolete) | **fail**, reject | **fail**, reject | **fail**, reject | — |
| P05 | merge | pass | pass | pass | pass |
| P06 | merge | pass | pass | pass | pass |
| P07 | merge | **warn**, merge | **warn**, merge | **warn**, merge | — |
| P08 | reject (merge residue) | pass | pass | pass | pass |
| P09 | reject, split | pass | pass | pass | pass |
| P10 | merge | pass | pass | pass | — |
| P11 | split, rehome | pass | pass | pass | pass |
| P12 | merge | pass | pass | pass | pass |
| P13 | merge | **warn**, merge | **warn**, merge | **warn**, merge | pass |
| P14 | different-claim | pass | pass | pass | pass |
| P15 | different-claim | pass | pass | pass | — |
| P16 | different-claim | pass | pass | pass | — |

Paraphrased grounds of the hits:

- P01 (a, b): beyond its linked neighbours the note adds about one sentence,
  the split between type and description, so it should merge into
  `why-notes-have-types.md`.
- P03 (a, b, c): the title asserts the label mechanism that the note's own
  label-ablation section rejects.
- P04 (a, b, c): the principle the note proposes is already the adopted rule
  in the collection contract and in the skills note, so the note is
  obsolete. Here the contract read did the work.
- P07 (a, b, c): the note's one distinct contrast fits as a paragraph in the
  apparent-success parent, which already states its core claim.
- P13 (a, b, c): the mechanism restates the parent's argmax-over-plausibility
  hypothesis. The (c) worker said in so many words that the parent's
  `extends` link is only a split-out marker.

Kinds against the labels. P01 got `merge` against a historical delete whose
residue went nowhere. P03 got `different-claim` against a deletion. P04,
P07 and P13 match. A merge proposal and a delete both remove the note, so
P01's kind would lead to the same action. P03's would not, since a retitle
keeps the note.

## Outcomes on the kept notes

| ID | (a) direct-value | (b) no base rate | (c) claim-need |
|---|---|---|---|
| K01 to K07 | pass | pass | pass |
| K08 to K14 | pass | pass | not run |

No wording proposed anything on any kept note.

## Counts

| Wording | Strong on positives | Weak on positives | Hits on positives | Proposals on kept |
|---|---|---|---|---|
| (a) direct-value | 2 of 16 | 3 of 16 | 5 of 16 | 0 of 14 |
| (b) no base rate | 2 of 16 | 3 of 16 | 5 of 16 | 0 of 14 |
| (c) claim-need | 2 of 16 | 2 of 16 | 4 of 16 | 0 of 7 |
| stage one, direct, opus | 0 of 10 | 0 of 10 | 0 of 10 | 0 of 4 |

## What the (a)/(b) difference shows

On this set it shows none. All 30 outcomes and all five kinds are the same
in (a) and (b), and on the five hits the grounds name the same passages and
the same receiving notes. The base-rate paragraph did not suppress proposals
here. The stage-one hypothesis that it pushed uncertain cases to `pass` is
not supported. The quietness has other causes. One possibility is that the
stated tests apply to only some of the historical decisions; the misses
below point that way. This is one run per pair, so run-to-run variation is
not measured. Two identical runs of one wording might differ as much as (a)
and (b) would.

## What the misses show

- The value test is applied, but the worker answers it with the note's own
  development: mechanisms, defeat conditions and scope sections. On P05,
  P08 and P12, the (a) worker named those as the reader's loss and passed
  the note. The operator judged the same material not worth a separate
  note. The test as written lets developed text count as value.
- P11 (a first-person adoption policy) passed under all three wordings,
  even with the contract read. The worker quoted the collection's
  "transferable claims" sentence and judged the policy to be a transferable
  claim about adoption. The contract at that commit did not settle the
  question for the worker as it did for the operator.
- The four different-claim positives other than P03 (P02, P14, P15, P16)
  were all missed. In each, the mismatch is between the title and a body
  that had been rewritten, or between the title and a premise later found
  defective. The workers read the body and title as one claim.
- P09 (a categorical claim contradicted by a channel the note itself
  concedes) passed. The defect was found by a full pass that decomposed
  premises. One check over the note's text did not reproduce it.

## Cost

Harness-reported `costUSD` per launch.

| Wording | Launches | Total | Per launch | Turns |
|---|---|---|---|---|
| (a) direct-value | 30 | $11.40 | $0.295 to $0.449 | 7 to 12 |
| (b) no base rate | 30 | $11.94 | $0.328 to $0.466 | 7 to 12 |
| (c) claim-need | 23 | $9.75 | $0.365 to $0.524 | 8 to 16 |
| **Round total** | **83** | **$33.09** | | |

That is within the round's limit of 100 launches and $35. The revised
direct wording costs about $0.38 per note on `opus`, up from about $0.31 for
the stage-one direct wording, because it reads the contract and the citers.
For about 380 reviewable notes in `kb/theory/`, (a) would cost about $145
and (c) about $160.

## Which wording to carry forward

Carry (a) direct-value forward, and retire (b) as a variant: (b) gave the
same outcomes, so the base-rate sentence can stay or go on other grounds.
(a) found everything (c) found plus P01, at lower cost, with no kept-note
proposal.

Next changes to (a), in order:

1. Make the value test count only what a reader of the parent would miss.
   Elaborations, defeat conditions and scope sections of a point the
   parent already states should count as the parent's material, not as
   loss. This targets P05, P06, P08, P10 and P12.
2. Add a title-against-body test that states the body's claim from its last
   sections, not its opening. Retitles happened after rewrites, so the
   opening and the title still agree, and the later sections diverge. This
   targets P02, P14 and P16.
3. Add a place test that asks whether the note tells the reader what to do
   or what the KB does, in the first person. That would separate a policy
   from a claim about policies without relying on the contract's wording.
   This targets P11.
4. Run each new wording twice on the same notes before reading a
   difference between wordings, to learn how much one wording varies
   between runs.

P09 and P15 rest on premise defects that a full pass found by decomposing
premises. They may be out of reach for a single check. If the next round
still misses them, they should be relabelled as outside this check's scope,
not counted against it.

## Stamp-to-worktree map

Run directories were copied by hand from each worktree into
`kb/reports/state/review/runs/`; `-N` suffixes keep same-second stamps
apart. Result files were not copied into the results store.

| Run directory | Worktree, commit | Wordings, notes |
|---|---|---|
| `20261113T195514Z` | w05, 2e73a19a6 | (a), P05 |
| `20261113T195605Z` | w01, 626f4e2c3 | (a) and (b), P01 |
| `20261113T195605Z-1` | w02, fd5b3beb8 | (a) and (b), P02 |
| `20261113T195605Z-2` | w03, 74c4678a4 | (a) and (b), P03 |
| `20261113T195605Z-3` | w04, f2c0d4634 | (a) and (b), P04 |
| `20261113T195605Z-4` | w05, 2e73a19a6 | (b), P05 |
| `20261113T195639Z` | w06, 02bc1d716 | (a) and (b), P06 |
| `20261113T195639Z-1` | w07, 52546a417 | (a) and (b), P07 |
| `20261113T195645Z` | w08, 5349c334c | (a) and (b), P08 |
| `20261113T195651Z` | w09, ef8285f39 | (a) and (b), P09 |
| `20261113T195659Z` | w10, 40c294c0d | (a) and (b), P10 |
| `20261113T195715Z` | w11, c6f59fe93 | (a) and (b), P11 |
| `20261113T195723Z` | w12, 817646ef6 | (a) and (b), P12 |
| `20261113T195725Z` | w13, 64c19b8a4 | (a) and (b), P13 |
| `20261113T195731Z` | w14, 57a22cbec | (a) and (b), P14 |
| `20261113T195739Z` | w15, 25895a9f7 | (a) and (b), P15 and K08 |
| `20261113T195801Z` | w16, 4c4a9e8a8 | (a) and (b), P16 |
| `20261113T195802Z` | k01, 21d4038a5 | (a) and (b), K01 |
| `20261113T195807Z` | k02, b1048c463 | (a) and (b), K02 |
| `20261113T195808Z` | k03, d9ff85f52 | (a) and (b), K03 and K04 |
| `20261113T195825Z` | k05, 4a7cc30de | (a) and (b), K05 |
| `20261113T195836Z` | k06, 40c26509a | (a) and (b), K06 |
| `20261113T195840Z` | k07, e71403cc1 | (a) and (b), K07 |
| `20261113T195850Z` | k09, e9acfcea5 | (a) and (b), K09 |
| `20261113T195850Z-1` | k10, 87f5b4d15 | (a) and (b), K10 |
| `20261113T195901Z` | k11, fa87486a9 | (a) and (b), K11 to K13 |
| `20261113T195910Z` | k14, 2932f424e | (a) and (b), K14 |
| `20261113T200023Z` to `-3` | w01 to w04 | (c), P01 to P04 |
| `20261113T200103Z`, `200105Z`, `200105Z-1`, `200113Z` | w05 to w08 | (c), P05 to P08 |
| `20261113T200214Z`, `-1`, `200215Z`, `-1` | w09, w11, w10, w12 | (c), P09, P11, P10, P12 |
| `20261113T200259Z`, `200300Z`, `200301Z`, `200309Z` | w13 to w16 | (c), P13 to P16 |
| `20261113T200340Z`, `200345Z`, `200400Z` | k01, k02, k03 | (c), K01, K02, K03 and K04 |
| `20261113T200506Z`, `-1`, `-2` | k05, k06, k07 | (c), K05, K06, K07 |
