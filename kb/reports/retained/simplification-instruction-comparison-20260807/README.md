# Simplification-instruction comparison: reflective self-improvement

This directory preserves the apparatus and outputs behind `kb/notes/evidence/three-simplification-passes-exposed-different-tradeoffs.md`. The experiment ran on 2026-08-07 and 2026-08-08. These are report snapshots, not operative copies of the article or instructions.

## Setup

- Target: `kb/articles/reflective-self-improvement.md` at commit `7e21c9ae`, immediately before commit `7f0db744` (`Simplify reflective self-improvement article`)
- Baseline: 1,991 words
- Treatments: one fresh sub-agent per instruction; each received only the baseline and its assigned instruction
- Isolation: rewrite agents were told not to inspect the live article, other candidates, or prior reports
- Comparison: one fresh agent received four anonymously named files and no treatment information

## Preserved files

| File | Role | SHA-256 |
|---|---|---|
| `baseline.md` | exact pre-simplification article | `21af5f376c9c744a3926053cd2052221d0cf147cc590369e7ddb1c4aa30677b4` |
| `instruction-established-style.md` | established-style treatment | `0879dfe615fece059829bd9827598969486f16732bd589beaa207b0d5abc2acd` |
| `candidate-established-style.md` | established-style output | `13fcefc534e521a52fcb5e40a4825ec6edc212edfee14e99706443e859fd315e` |
| `instruction-churchill-zinsser.md` | Churchill-and-Zinsser treatment | `3c82485893961fc0b42798da25d71096d61503785efb91d5eba81b069caf10b4` |
| `candidate-churchill-zinsser.md` | Churchill-and-Zinsser output | `1e1cdfe8a0c228308b719d25ad979f8279c95abdce49f260d69c44ebcd5bc6c2` |
| `instruction-sentence-by-sentence.md` | exhaustive local treatment | `03e69e85ca7e3b0796e5f7c4db68676e0f9fba95251eeeb5ca63d74fe442fd6c` |
| `candidate-sentence-by-sentence.md` | exhaustive local output | `daca7c95ca6cbdb6055c8ada3694725ef83c2c66de7285137b94739f54f8d756` |
| `sentence-pass-report.md` | coverage ledger and validation report | `21e34b3425f219eab2247efaba8fe14f41520d0467da30f50a9930c2fd252a2b` |

## Anonymous comparison

The judge received mechanically copied files under this hidden mapping:

| Anonymous name | Actual version |
|---|---|
| `A` | sentence-by-sentence candidate |
| `B` | baseline |
| `C` | Churchill-and-Zinsser candidate |
| `D` | established-style candidate |

The judge was asked to rank all four for first-read clarity, coherence, natural rhythm, technical precision, and semantic faithfulness; identify the likely baseline; and report semantic changes involving causal direction, epistemic strength, scope, conditions, or false agency.

It guessed `A` was the baseline with high confidence and returned this ranking:

| Criterion | Ranking |
|---|---|
| Overall | `D > C > A > B` |
| First-read clarity | `C > D > B > A` |
| Coherence | `D > C > A > B` |
| Natural rhythm | `C > D > B > A` |
| Technical precision | `D > A > B > C` |
| Semantic faithfulness | `A > D > B > C` |

Because the judge misidentified the baseline, the last row is not a calibrated measure of distance from the source. The detailed review nevertheless identified concrete regressions in `C`, including a lost temporal condition, weakened conditional structure, false agency assigned to an acceptance metric, stronger evidential wording, and an intended effect presented as achieved. It found `D` the best overall balance and found `A` nearly indistinguishable from the incumbent.

## Validation note

All three candidates passed `commonplace-validate`. Each produced 30 expected link warnings because article-relative links were resolved from the temporary experiment directory rather than `kb/articles/`; headings, frontmatter, and link destinations were unchanged.
