# Asking the revise assessor to compare smaller repairs: three-model trial, 2026-11-23

**Keep the existing [revise assessor instruction](../../instructions/simplification-passes/revise-an-article-or-note.md).** Asking for an explicit comparison with keeping a passage or making a smaller repair changed one model’s placement decision. It did not consistently improve the plan, and it lengthened all six paired assessments.

## Test

Two historical assessor packets tested different decisions. The mixed-edit case asked whether to move a library-hours example while also fixing ambiguous references in the same note. The stop case asked whether to revise prose when choosing between two meanings of “requires” in a claim about continual learning would change what dependent notes could cite. The second decision belonged to the operator.

For each case and model, two fresh sessions received the same frozen inputs. One used the instruction at `318458e48`; the other added a paragraph asking the assessor to separate independent edits, compare a contested edit with a smaller repair or no edit, and identify any reader priority that would reverse the recommendation. No other instruction changed. Within each model and case, a fresh baseline was the comparator, not the historical plan. A GPT-6.2 Astra reader for each model compared its outputs blind to condition. Astra and Sol assessors ran under Pi; Opus ran under Claude Code. All 12 plans passed the revise controller’s checks.

## Observations

Arrows show baseline → amended. Word counts cover the prose assessments, not the plans.

| Assessor | Library example | Blind appraisal of mixed-edit plans | Words: mixed | Words: stop |
|---|---|---|---:|---:|
| GPT-6.2 Astra | Keep → keep | Better reason to keep the example; no clear plan advantage. | 1,051 → 1,252 | 1,147 → 1,250 |
| GPT-6.2 Sol | Keep → move | Preferred the amended placement beside the facts-versus-values distinction, but it unnecessarily deferred identifying Commonplace on first mention. | 1,636 → 1,859 | 1,668 → 1,805 |
| Claude Opus 5.5 | Move → move | Preferred baseline: amended explained the move but left two bounded overclaim repairs to the operator. | 1,761 → 2,429 | 1,609 → 2,078 |

All six mixed-edit plans kept the straightforward referent repairs. All six stop-case plans stopped with no executable passes. The historical mixed plan moved the example, whereas fresh baseline Astra kept it: using the historical plan alone would have mistaken run variation for an effect of the amendment.

These were two selected cases, one response per model, condition and case. Word count is not measured reading time. No edit pass ran and no reader used a revised note. A direct follow-up would compare the two example placements on the same reader task while holding unrelated edits fixed.

**Audit trail.** The exact amendment, hashed inputs, 12 plans and assessments, and three blind appraisals remain in Git at `8dfa39903530fc10fe917ff5b651ad1da3930b0f`, under `kb/work/revise-assessor-comparisons/`. For the protocol and condition keys, run `git show 8dfa39903:kb/work/revise-assessor-comparisons/replication.md` and `git show 8dfa39903:kb/work/revise-assessor-comparisons/README.md`.
