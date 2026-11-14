# Third results: one revised wording, run twice on opus

Round three, run on 2026-11-13 on `opus` only. The wording
[direct-tests](./wordings/direct-tests.md) was run twice on the same 30
labelled notes. It found 5 of 16 positives in the first run and 6 of 16 in
the second, and it proposed nothing on any of the 14 kept notes in either run.
Seven positives were hit in at least one run and four in both. The two
runs gave the same outcome on 27 of 30 notes. They gave the same outcome
and kind on 26. The different-claim positives the round was meant to reach
(P02, P14, P15, P16) were still missed in both runs. The wrong-place case
P11 was hit in both. The counts below are counts, not estimates of
anything.

## Read this first: the wording was fitted to these notes

This round's wording was written after seeing which notes earlier wordings
missed, and on the same 30 notes. Each of its three tests targets named
misses from [second-results.md](./second-results.md). A gain on this set is
therefore weak evidence that the wording generalizes. The reserve cases in
[labelled-set.md](./labelled-set.md) were left untouched and unrun. They are
held back as a test set for a wording that is about to be adopted.

## The wording

[direct-tests](./wordings/direct-tests.md), id `higher-order/direct-tests`,
starts from [direct-value](./wordings/direct-value.md) and applies changes 1
to 3 from second-results.md:

- **Parent-loss test.** Count as loss only a claim, mechanism or condition
  the parent does not already state. Elaboration of the parent's point,
  such as worked mechanisms, defeat conditions, scope and examples, does
  not count. A parent's `extends` link stays neutral.
- **Title-against-body test.** State the claim the body ends up arguing,
  taken from its later sections and from any reported test or revision,
  not from the opening. Compare it with the title.
- **Policy-or-claim test.** Decide from the text, before reading the
  collection contract, whether the central content says what to do or what
  this KB adopts (a policy, procedure or proposal), or what is true of
  systems of this kind. Then quote the contract.

It keeps the base-rate paragraph, the five kinds, the outcome mapping and
the finding-line format of direct-value. It has no worked examples.

**Keeping the two runs apart.** The second run used
[direct-tests-repeat](./wordings/direct-tests-repeat.md), id
`higher-order/direct-tests-repeat`, which is byte-identical to direct-tests
except for the `gate_id` line. Each run therefore wrote its own result file
per note, and neither overwrote the other. Each run was its own sweep, made
one after the other with separate launches, and no answer was replayed.
The worker sees the criterion text, so in run two it could read the word
"repeat" in the gate id; nothing else differed.

## How it was run

The method was the same as in rounds one and two. Each note was judged in a
detached worktree at its commit, in the session scratch directory, with
`kb/work/`, `kb/reports/`, `kb/log.md`, `kb/messages/` and the
session-start hook script deleted. `COMMONPLACE_LIBRARY_ROOT` pointed at a
scratch library holding byte-identical copies of the two wording files.
Nothing was added to `kb/instructions/review-gates/`. Every run used the
`opus` profile with `--grouping pair` and `--max-workers 4`. All 52 sweeps
exited 0 with a clean guard. All worktrees were removed.

## Outcomes on the positives

A hit is `warn` (weak) or `fail` (strong). "Agree" means the same outcome in
both runs; a different kind under the same outcome is marked.

| ID | Label | Run 1 | Run 2 | Agree | direct-value, round two |
|---|---|---|---|---|---|
| P01 | reject (merge residue) | pass | pass | yes | warn, merge |
| P02 | different-claim | pass | pass | yes | pass |
| P03 | reject | **fail**, different-claim | **fail**, different-claim | yes | fail, different-claim |
| P04 | reject (obsolete) | **fail**, rehome | **fail**, merge | outcome yes, kind no | fail, reject |
| P05 | merge | **warn**, merge | pass | no | pass |
| P06 | merge | pass | pass | yes | pass |
| P07 | merge | **warn**, merge | **warn**, merge | yes | warn, merge |
| P08 | reject (merge residue) | pass | pass | yes | pass |
| P09 | reject, split | pass | pass | yes | pass |
| P10 | merge | pass | pass | yes | pass |
| P11 | split, rehome | **warn**, split | **warn**, split | yes | pass |
| P12 | merge | pass | **warn**, different-claim | no | pass |
| P13 | merge | pass | **warn**, different-claim | no | warn, merge |
| P14 | different-claim | pass | pass | yes | pass |
| P15 | different-claim | pass | pass | yes | pass |
| P16 | different-claim | pass | pass | yes | pass |

Paraphrased grounds of the hits that are new or that differ between runs:

- P04, run 1: the central content is an unadopted placement policy for this
  KB, so `rehome`. Run 2: the principle is already stated in the skills note
  it links to, so `merge`. Round two's direct-value said `reject`, as
  obsolete. Three kinds for one note, all of which remove it from theory.
- P05, run 1: the parent's "Consequences for closure" paragraph already
  states the claim, both mechanisms in compressed form, and the warrant
  consequence. Run 2 passed it. This is the first hit on P05 in three
  rounds.
- P11, both runs: the note combines a first-person adoption policy for this
  KB with a claim about transfer, so `split`. The policy-or-claim test found
  what the contract read in round two did not.
- P12, run 2: the title's generalization claim is argued in early sections,
  but the later sections argue something else, so `different-claim`. The
  historical change was a merge into the conjecture note.
- P13, run 2: the title says camouflage is searched for, while the body
  says twice that it is shaped by training and not chosen, so
  `different-claim`. Run 1 passed it. Round two's direct-value proposed
  `merge`, the historical kind.

## Outcomes on the kept notes

| ID | Run 1 | Run 2 |
|---|---|---|
| K01 to K14 | pass | pass |

No proposal on any kept note in either run, as in round two.

## Counts

| | Run 1 | Run 2 | Both runs | Either run | direct-value, round two |
|---|---|---|---|---|---|
| Strong on positives | 2 | 2 | 2 | 2 | 2 |
| Weak on positives | 3 | 4 | 2 | 5 | 3 |
| Hits on positives | 5 of 16 | 6 of 16 | 4 of 16 | 7 of 16 | 5 of 16 |
| Proposals on kept | 0 of 14 | 0 of 14 | 0 | 0 | 0 of 14 |
| Same outcome as the other run | | | 27 of 30 | | |
| Same outcome and kind | | | 26 of 30 | | |

The three outcome disagreements (P05, P12, P13) were all between `pass` and
`warn`. The strong proposals and the kept notes were stable across runs.
Weak is where the runs differ. With three weak flips in 30 notes, a one-note
difference in weak hits between two wordings, as between direct-value and
either run here, is within the variation of one wording against itself.

## What the three changes did

- **Parent-loss test (change 1).** It reached P05 in one run of two. It
  did not reach P06, P08, P10 or P12 as merges, and it lost P01, which
  direct-value had found as a weak merge in its single run. On this
  evidence it does not reliably move developed satellites to `merge`.
- **Title-against-body test (change 2).** It did not reach any of the four
  different-claim positives. It produced two `different-claim` proposals on
  merge positives in run 2 (P12, P13). Those notes were removed historically,
  so the proposals are hits, but with a kind the history did not use.
- **Policy-or-claim test (change 3).** It reached P11 in both runs, the
  first hit on P11 in three rounds, without a proposal on any kept note.
  This is the one change with a clear effect on this set.

## Cost

Harness-reported `costUSD` per launch.

| Run | Launches | Total | Per launch | Turns |
|---|---|---|---|---|
| Run 1, direct-tests | 30 | $12.19 | $0.306 to $0.486 | 8 to 13 |
| Run 2, direct-tests-repeat | 30 | $12.06 | $0.307 to $0.477 | 8 to 14 |
| **Round total** | **60** | **$24.25** | | |

That is within the round's limit of 62 launches and $27. One run costs
about $0.40 per note, close to direct-value's $0.38. A whole-collection run
of about 380 notes would cost about $155 per run. It was not made.

## What I would change next

1. Keep the policy-or-claim test. It is the one change that reached a
   missed case in both runs and caused no false proposal.
2. Drop or rewrite the title-against-body test. It missed the cases it was
   written for. In P02 the mismatch is on the page: the body had been
   generalized beyond Commonplace collections while the title still named
   them. The workers still read the two as one claim, perhaps because the
   body keeps the word "collection" in its ordinary sense. Whether the
   mismatch is equally visible in P14, P15 and P16 has not been checked.
   Before rewriting the test, read the four different-claim positives side
   by side.
3. Treat weak proposals as noisy. Report a weak proposal only when two runs
   agree, or run the check twice and act on the union of strong proposals
   and the intersection of weak ones. On this set that rule would keep
   P03, P04, P07 and P11 and drop the three flips.
4. Stop tuning on these 30 notes. The next wording should be judged on
   the reserve cases in labelled-set.md, which no wording has seen, and on
   the operator's sample of strong proposals from a collection run if one
   is approved.

## Stamp-to-worktree map

Run directories were copied by hand from each worktree into
`kb/reports/state/review/runs/`; `-N` suffixes keep same-second stamps
apart. Result files were not copied into the results store.

| Worktree, commit | Notes | Run 1 directory | Run 2 directory |
|---|---|---|---|
| w01, 626f4e2c3 | P01 | `20261113T214402Z` | `20261113T214838Z` |
| w02, fd5b3beb8 | P02 | `20261113T214402Z-1` | `20261113T214838Z-1` |
| w03, 74c4678a4 | P03 | `20261113T214402Z-2` | `20261113T214838Z-2` |
| w04, f2c0d4634 | P04 | `20261113T214401Z` | `20261113T214838Z-3` |
| w05, 2e73a19a6 | P05 | `20261113T214402Z-3` | `20261113T214838Z-4` |
| w06, 02bc1d716 | P06 | `20261113T214442Z` | `20261113T214915Z` |
| w07, 52546a417 | P07 | `20261113T214448Z` | `20261113T214917Z` |
| w08, 5349c334c | P08 | `20261113T214448Z-1` | `20261113T214922Z` |
| w09, ef8285f39 | P09 | `20261113T214449Z` | `20261113T214927Z` |
| w10, 40c294c0d | P10 | `20261113T214456Z` | `20261113T214931Z` |
| w11, c6f59fe93 | P11 | `20261113T214523Z` | `20261113T214951Z` |
| w12, 817646ef6 | P12 | `20261113T214530Z` | `20261113T215004Z` |
| w13, 64c19b8a4 | P13 | `20261113T214530Z-1` | `20261113T215004Z-1` |
| w14, 57a22cbec | P14 | `20261113T214539Z` | `20261113T215011Z` |
| w15, 25895a9f7 | P15, K08 | `20261113T214541Z` | `20261113T215021Z` |
| w16, 4c4a9e8a8 | P16 | `20261113T214616Z` | `20261113T215048Z` |
| k01, 21d4038a5 | K01 | `20261113T214617Z` | `20261113T215049Z` |
| k02, b1048c463 | K02 | `20261113T214620Z` | `20261113T215051Z` |
| k03, d9ff85f52 | K03, K04 | `20261113T214622Z` | `20261113T215108Z` |
| k05, 4a7cc30de | K05 | `20261113T214628Z` | `20261113T215115Z` |
| k06, 40c26509a | K06 | `20261113T214702Z` | `20261113T215132Z` |
| k07, e71403cc1 | K07 | `20261113T214703Z` | `20261113T215132Z-1` |
| k09, e9acfcea5 | K09 | `20261113T214703Z-1` | `20261113T215137Z` |
| k10, 87f5b4d15 | K10 | `20261113T214705Z` | `20261113T215154Z` |
| k11, fa87486a9 | K11 to K13 | `20261113T214724Z` | `20261113T215202Z` |
| k14, 2932f424e | K14 | `20261113T214738Z` | `20261113T215209Z` |
