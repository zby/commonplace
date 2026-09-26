# Write-brief pilot: results

Read against the protocol frozen at `05f3c44a`. Raw tallies: [`scores/analysis-output.md`](./scores/analysis-output.md), produced by `scripts/write_brief_pilot_analysis.py`. Deviations: [`deviations.md`](./deviations.md).

## What was run

95 writer runs: 10 targets × 4 arms × 2 replicates of a pressure edit, plus 15 override runs. Each output was scored blind, item by item, by two independent scorers. They agreed on 3,550 of 3,591 item scores (98.9%), and a third scorer settled the 41 disagreements.

**Compliance.** 93 runs completed their request. Two pressure runs on target 6 stopped with a question instead of editing. One was in arm A (no brief) and one in arm C (rebuilt brief). Both named a real conflict: the request routed memory systems into a collection whose own contract calls it legacy. One arm-C run on target 1 complied only partly.

## Verdicts

Two readings are reported because the verdicts on H3 and H5 depend on them. The primary reading follows the compliance rule fixed before unblinding (deviation 4): a question run counts every item as violated. That rule conflicts with the protocol's Phase 1 text, which calls a question "a valid outcome" that "scores as flagged". The sensitivity reading drops the two question runs.

| | Primary | Without the two question runs |
|---|---|---|
| **H1** — brief value concentrates in non-recoverable items | survived: A−B = 11 on N items (predicted ≥5); rate gap N 0.138 vs R 0.087 | survived: A−B = 9; rate gap N 0.117 vs R 0.014 |
| **H2** — brief adds less where the title states the claim | survived: normalized gap 0.104 claim-titled vs 0.207 non-claim | nominally survived, effectively a tie: 0.104 vs 0.107 (0.094 without instructions) |
| **H3** — a brief rebuilt from the finished document does worse | survived: C−B = 3 (predicted ≥3) | **refuted**: C−B = 1 (refutation line ≤1) |
| **H4** — briefs do not silently over-constrain | survived: all 15 override runs amended the named item with notice | same |
| **H5** — a one-line brief keeps the claim, loses the boundaries | survived | **refuted, "one line adds nothing"**: D equals A on claim and reader-update items (2 vs 2) |

The primary verdicts on H3 and H5 turn on one question run per arm, each on a 61-item document, which alone adds about 50 violations. Those survivals should not be relied on. The sensitivity reading is the more informative of the two.

## Violations by arm (without the two question runs)

| Arm | Non-recoverable | Recoverable | Restraint + constraint | Claim + reader update |
|---|---|---|---|---|
| A — no brief | 14/78 | 10/572 | 19/481 | 2/89 |
| B — original brief | 5/80 | 2/618 | 7/516 | 0/94 |
| C — rebuilt brief | 6/78 | 9/572 | 10/481 | 3/89 |
| D — one-line brief | 13/80 | 11/618 | 20/516 | 2/94 |

## Reading

- **An explicit full brief helps.** Arm B violated about a third as many non-recoverable items as arm A, and fewer recoverable ones as well. Over all bounded items (restraints and constraints) the count fell from 19 to 7.
- **A brief rebuilt from the commissioned document does almost as well on the items that matter.** Arm C matched arm B on non-recoverable items (6 vs 5), and did about half as well again on restraints and constraints (10 vs 7, against 19 for no brief). This refutes H3 in the sensitivity reading. The rebuilt briefs were inferred from a document that still realized its commission. The drift study shows that later documents often do not. A brief rebuilt from a drifted document would encode the drift. So the refutation is limited to reconstruction at commissioning time.
- **A one-line brief is indistinguishable from no brief.** Arm D matched arm A on every bucket (N 13 vs 14; restraints and constraints 20 vs 19). The prediction was that one line would at least carry the claim and reader update. Both arms kept those items almost perfectly anyway (2 violations in 89–94), so the one line had nothing to add there and nothing that protected the boundaries.
- **No over-constraint was observed.** Every brief-arm override run followed the request and stated the amendment. No brief-arm pressure run asked a question; the two questions came from arms A and C.
- **The claim-title asymmetry (H2) did not show.** The per-target gaps are small counts (2–16 non-recoverable items per arm per target) and they vary without a class pattern.

## Unpredicted

- **Question runs appeared only without an original brief.** The target-6 pressure request conflicted with a collection contract. Of the four runs per arm, one run in arm A and one in arm C stopped to ask; the arm-B and arm-D runs resolved the conflict by following the contract and saying so. With n = 1 per arm this is only a pointer.
- **Briefs rarely restored undelivered commission content.** Items the commissioned version never realized were added in 4 of 38 opportunities in arm B, 5 in D, 2 in C, and 2 in A. A brief does not by itself make a writer complete a commission.
- **Drift under pressure concentrated on a few items per target.** The pressure requests produced drift mainly on a few items per target: benchmark reproduction (target 1), qualifier loss in the witness conditions and Naur section (target 9), new controlled tokens (target 7), dropped rationale (targets 4 and 10). This concentration, rather than broad erosion, matches the drift study's finding that losses cluster in specific rewrites.

## Limits

- Ten targets and two replicates. The counts are small, so the verdicts rest on differences of a few items.
- Writers, rebuilders and scorers are all Claude Opus models.
- The original briefs were careful, operator-directed commissions.
- The rebuilt briefs had the commissioned version, not a drifted one.
- The H3 and H5 verdicts depend on how two question runs are counted. The frozen protocol is internally inconsistent on that point.
