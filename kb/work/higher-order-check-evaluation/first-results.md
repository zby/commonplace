# First results: two wordings on the labelled set

Stage one of this workshop, run on 2026-11-13. Both wordings missed most
labelled positives: `direct` found 3 of 16 and `claim-ownership` 2 of 16 on
`sonnet`. Neither proposed anything on 13 of the 14 kept notes. An `opus`
probe of `direct` on 10 positives and 4 kept notes proposed nothing at all.
The labels are in [labelled-set.md](./labelled-set.md), and the wordings are
[wordings/direct.md](./wordings/direct.md) and
[wordings/claim-ownership.md](./wordings/claim-ownership.md).
The counts below are counts. A set this small supports no rate estimate.

**Limit added 2026-11-13.** The operator requires `opus` for these checks.
The `sonnet` columns below were run against that requirement and are not
calibration evidence. Only the `opus` column is, and it covers the `direct`
wording on 14 of the 30 notes.

## How it was run

- **Criteria outside the catalog.** `commonplace-review run gates` resolves
  `--criteria` only as catalog gate ids, bundles and the `type`,
  `collection` and `critique` lenses (`src/commonplace/lib/review_workflows/criteria.py`).
  It rejects `..` and does not accept a repository path. The catalog is the
  library's `instructions/review-gates/`, and the library root can be
  overridden with `COMMONPLACE_LIBRARY_ROOT` (`src/commonplace/lib/library.py`).
  The runs therefore pointed that variable at a scratch library holding
  byte-identical copies of the two wording files under
  `instructions/review-gates/higher-order/`, plus a copy of
  `instructions/review-profiles.yaml`. The criterion ids were
  `higher-order/direct` and `higher-order/claim-ownership`. Nothing was
  added to `kb/instructions/review-gates/`.
- **Historical texts.** Each text was judged in a detached worktree at its
  commit, with workshop, log, report and message material deleted. The
  README's start section records the decision and the leaks left open.
- **Profile.** `sonnet` (claude-code, Sonnet, medium effort, read tools only)
  for both wordings on all 30 notes, with `--grouping pair` and
  `--max-workers 4`. `opus` with the same flags was run for `direct` on 14
  notes, and for both wordings on P01 as a cost check.
- **Where results are.** Each worktree's review state held its results.
  The run directories were copied into
  `kb/reports/state/review/runs/20261113T1650*` to `20261113T1656*`; the
  stamp-to-worktree map is below. Result files were not copied into
  `kb/reports/state/review/results/`: their notes do not exist at those paths
  in the current checkout, so they would be orphaned. The worktrees were
  removed afterwards. The copy into the state tree was made by hand, not by
  the review command; it is a deviation from this stage's write scope.
- **Guard.** All 27 sweeps exited 0 with a clean checkout guard in their
  worktree.

## Outcomes on the positives

`pass` = no proposal, `warn` = weak, `fail` = strong. A hit is `warn` or
`fail`. The kind is the one the worker gave; the label is the kind of the
historical change.

| ID | Label | direct, sonnet | claim-ownership, sonnet | direct, opus |
|---|---|---|---|---|
| P01 | reject (merge residue) | pass | pass | pass |
| P02 | different-claim | pass | pass | pass |
| P03 | reject | **fail**, different-claim | **fail**, different-claim | not run |
| P04 | reject (obsolete) | **warn**, reject | **warn**, rehome | not run |
| P05 | merge | pass | pass | pass |
| P06 | merge | pass | pass | pass |
| P07 | merge | **warn**, merge | pass | not run |
| P08 | reject (merge residue) | pass | pass | pass |
| P09 | reject, split | pass | pass | pass |
| P10 | merge | pass | pass | not run |
| P11 | split, rehome | pass | pass | pass |
| P12 | merge | pass | pass | pass |
| P13 | merge | pass | pass | pass |
| P14 | different-claim | pass | pass | pass |
| P15 | different-claim | pass | pass | not run |
| P16 | different-claim | pass | pass | not run |

The hits share a feature: the defect is visible in the note's own text or
against a file the note names. P03's own ablation section says the label
convention "is not what supplies" the self-sufficiency its title attributes
to labels. P04 rests on a `WRITING.md` placement that is no longer in the
tree. P07 repeats sections of the parent it links to. The kinds differ from
the history on P03 and P04: the operator deleted both, while the workers
proposed a retitle and a rehome.

The misses share a feature as well. Most historical decisions were value
judgments: the note was trivial, a weak satellite, or a bounded claim
expanded into a full note. Several also rested on a fact about the
collection outside the note, such as the type field being near-constant
within a collection (P01). The workers read the parent's `extends` link to
the satellite as evidence that the satellite owns its contribution. This
happened in the `claim-ownership` results for P05 and P13, and in the `opus`
result for P05. P11 is an operational policy written in the first person.
Both `sonnet` workers and the `opus` worker noticed that it reads as a
policy, and each judged that it belonged in the theory collection anyway.

## Outcomes on the kept notes

| ID | direct, sonnet | claim-ownership, sonnet | direct, opus |
|---|---|---|---|
| K01 to K09, K11 to K14 | pass | pass | K02, K06, K13: pass; others not run |
| K10 | **warn**, split | pass | pass |

On K10, the `direct` worker proposed splitting off the section "Session-loaded material
can carry episode-scoped authority". The full pass that kept K10 folded an
episode-authority section into its placement section, so that finding
touched a seam the pass also reworked.

## Weak share

| Wording and profile | weak on positives | weak on kept | strong on positives | strong on kept |
|---|---|---|---|---|
| direct, sonnet | 2 of 16 | 1 of 14 | 1 of 16 | 0 of 14 |
| claim-ownership, sonnet | 1 of 16 | 0 of 14 | 1 of 16 | 0 of 14 |
| direct, opus | 0 of 10 | 0 of 4 | 0 of 10 | 0 of 4 |

Question 4 asked whether weak is used as an escape. On this set the
opposite failure appeared: no proposal was the escape. Each wording says
that most notes need no change and tells the worker not to use WARN for
doubt it cannot ground. That instruction may push uncertain cases to
`pass`. It was not varied, so this is a hypothesis.

## Cost

Costs are the harness-reported `costUSD` per launch.

| Wording and profile | Launches | Total | Per launch |
|---|---|---|---|
| direct, sonnet | 30 | $3.55 | $0.106 to $0.134 |
| claim-ownership, sonnet | 30 | $4.13 | $0.114 to $0.168 |
| direct, opus | 14 | $4.35 | about $0.31 |
| claim-ownership, opus (P01 only) | 1 | $0.39 | $0.39 |
| **All** | **75** | **$12.42** | |

A launch took 5 to 9 turns on `sonnet`. The `claim-ownership` launches used
Grep 34 times in total, and the `direct` launches used it 3 times. On the
same note (P01), `opus` cost about 2.6 times as much as `sonnet` for `direct`
and 3.3 times as much for `claim-ownership`.

Expected cost of a whole-collection run: `kb/theory/` has about 380
reviewable notes. At these per-launch costs, `direct` on `sonnet` would cost
about $45, `claim-ownership` on `sonnet` about $52, both together about $97,
and `direct` on `opus` about $118. This assumes theory notes are about as
long as the notes here. On these results such a run would mostly measure
how often the check says nothing. Revising the wording first would be
cheaper.

## Where the outcome mapping strained

- **The kind is not a field.** The verdict carries the force. The kind is
  carried only by the `kind=` convention in the first finding line. All
  six non-pass results followed it, but nothing parses it or enforces
  it. An atom type for this check would need a kind field with a
  closed vocabulary, and a place for a second kind; the wordings push the
  second kind into INFO lines.
- **WARN means two things.** In other gates, WARN means "conforms, with
  named problems". Here it means "a change might help and the note can
  stand". The type spec's force section calls FAIL an escalation signal,
  not a blocker, which fits a strong proposal. A status sweep would mix
  this check's weak proposals with other gates' warnings in one queue,
  although they call for different handling.
- **The reading scope conflicts with the check.** The fixed prompt tells
  the worker to read only files the note links to for grounding or
  consistency checks. Judging a merge or a rehome needs notes the note does
  not link to and the collection's `COLLECTION.md`. The `claim-ownership`
  wording asks for a same-directory search, and its workers did search;
  that went past the prompt's wording. No worker read the collection
  contract, and P11's miss is the case where it mattered. The prompt sits
  outside the hashes, so changing it would not stale any result.
- **Freshness does not see neighbours.** A merge or ownership verdict
  depends on other notes. The result hashes only the note and the
  criterion, so a result stays fresh after the receiving note changes, or
  after a duplicate is written.
- **Historical texts do not fit the store.** Results are keyed by the
  current repository path. A result for a text from before a deletion or
  rename has no live pair to be fresh against, which is why these results
  stay in copied run directories.
- **Criteria outside the catalog need the library override.** Each
  wording file in this directory therefore needs a byte-identical copy in a
  scratch library. To run a draft criterion in place, the command would
  need a `--criteria` form that takes a repository path, with the path as
  the criterion id, as the result-path rule for other repository criteria
  already allows.

## What I would change in each wording

Both wordings:

- Ask for the value test the operator applied, not only duplication:
  "if this note were deleted and its one best sentence added to its parent,
  what would a reader lose?" Treat a parent's `extends` link to this note as
  neutral evidence, not as proof of ownership.
- Name the collection contract as an input to read, so a judgment about
  place can quote it. This also needs the reading-scope change above.
- Test the base-rate sentence by removing it in one variant, to see
  whether it suppresses proposals.
- Add one worked example of each kind from the labelled set, written so
  that it does not identify any labelled note.

`direct`: it had the most hits and the only false weak, at the lower cost.
Add the reverse-compression test and the collection contract, and keep it
short.

`claim-ownership`: its ownership table is easy to audit, but ownership is
the wrong question for satellites, because the parent defers to them by
link. Replace step 3's "who states it" with "who would need it": does any
other note, or the parent, lose an argument if this note goes? Make step 4
ask whether the central claim adds anything beyond its premises, which is
the test P08 failed historically.

## Stamp-to-worktree map

| Run directory under `kb/reports/state/review/runs/` | Worktree, commit | Profile, notes |
|---|---|---|
| `20261113T165045Z` | w01, 626f4e2c3 (`bbc5ef0a4^`) | sonnet, P01 |
| `20261113T165121Z` | w01 | opus, P01 |
| `20261113T165252Z` | w02, fd5b3beb8 | sonnet, P02 |
| `20261113T165252Z-1` | w03, 74c4678a4 | sonnet, P03 |
| `20261113T165252Z-2` | w04, f2c0d4634 | sonnet, P04 |
| `20261113T165252Z-3` | w05, 2e73a19a6 | sonnet, P05 |
| `20261113T165252Z-4` | w06, 02bc1d716 | sonnet, P06 |
| `20261113T165313Z` | w07, 52546a417 | sonnet, P07 |
| `20261113T165314Z` | w08, 5349c334c | sonnet, P08 |
| `20261113T165317Z` | w09, ef8285f39 | sonnet, P09 |
| `20261113T165317Z-1` | w10, 40c294c0d | sonnet, P10 |
| `20261113T165319Z` | w11, c6f59fe93 | sonnet, P11 |
| `20261113T165335Z` | w12, 817646ef6 | sonnet, P12 |
| `20261113T165336Z` | w13, 64c19b8a4 | sonnet, P13 |
| `20261113T165339Z` | w14, 57a22cbec | sonnet, P14 |
| `20261113T165339Z-1` | w15, 25895a9f7 | sonnet, P15 and K08 |
| `20261113T165343Z` | w16, 4c4a9e8a8 | sonnet, P16 |
| `20261113T165355Z` | k01, 21d4038a5 | sonnet, K01 |
| `20261113T165358Z` | k02, b1048c463 | sonnet, K02 |
| `20261113T165402Z` | k03, d9ff85f52 | sonnet, K03 and K04 |
| `20261113T165404Z` | k05, 4a7cc30de | sonnet, K05 |
| `20261113T165405Z` | k06, 40c26509a | sonnet, K06 |
| `20261113T165417Z` | k07, e71403cc1 | sonnet, K07 |
| `20261113T165419Z` | k09, e9acfcea5 | sonnet, K09 |
| `20261113T165425Z` | k10, 87f5b4d15 | sonnet, K10 |
| `20261113T165425Z-1` | k11, fa87486a9 | sonnet, K11 to K13 |
| `20261113T165425Z-2` | k14, 2932f424e | sonnet, K14 |
| `20261113T165540Z` to `-4`, `165604Z` to `-2`, `165606Z` | w02, w05, w06, w08, w09, w11, w12, w13, w14 | opus, direct |
| `20261113T165608Z`, `165632Z`, `165633Z`, `165633Z-1` | k02, k06, k10, k11 | opus, direct |

The `-N` suffixes were added when the directories were copied, to keep
same-second stamps from different worktrees apart.
