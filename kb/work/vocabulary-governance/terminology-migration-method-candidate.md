# Terminology migration method candidate

This is a provisional method candidate extracted from the completed `prose` → `natural-language` migration. It is not yet an instruction. One migration exercised it end to end, including a failed verification and remediation pass; the next load-bearing vocabulary change should test whether the useful parts recur without assuming that this case's exact machinery is universal.

## Candidate shape

A terminology migration should probably:

1. anchor its scope and searches to a starting revision;
2. classify occurrences before replacing them, distinguishing the successor category, a more precise noun, a visibly lossy prototype shorthand, and deliberate preservation;
3. change the vocabulary-defining spine before dependent uses;
4. keep implementation decisions in a ledger that an independent session can reconcile against both the baseline and the result;
5. audit and explain residual uses instead of treating a zero search count as the completion criterion;
6. validate semantic, structural, and executable consumers separately from independent verification of the migration record.

The migration record must be large enough to make completeness and judgment inspectable, but its format and granularity remain open. The `prose` migration needed a full occurrence table and split batches because it crossed a large corpus and executable controlled-vocabulary surfaces. A smaller change may not.

## Evidence from the first full case

The natural-language terminology workshop classified and independently verified 1,903 occurrence rows. The method exposed problems that bulk replacement and changed-file validation alone would not have found:

- precise artifact nouns were sometimes better than either the old or new category name;
- `prompt` was exact for only a consumption-path case, not as a general alias for natural-language form;
- editorial uses of **prose** and historical terminology had to survive;
- a controlled vocabulary also lived in parser code, tests, fixtures, and generated data, where the first migration pass silently dropped recognized components;
- deterministic validation caught a title-length failure caused by wording expansion;
- independent verification found semantic and executable-surface leftovers, and a later whole-table pass found four further wording defects;
- the final broad search remained nonzero, but its survivors were classified and explainable.

The durable semantic claims have already moved into [representational form](../../notes/definitions/representational-form.md) and [load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md). This candidate retains only the procedural hypothesis that has not yet earned a prescriptive home.

## Test on the next vocabulary shift

When another load-bearing vocabulary change is proposed—a future refinement of **symbolic** would qualify—read this candidate before planning the migration. Use it as a hypothesis, not a mandatory template, and record:

- which candidate steps prevented or exposed a real error;
- which steps added cost without changing the result;
- whether a full occurrence ledger was necessary, and what lighter evidence would have been sufficient;
- whether the initial scope found every executable or generated consumer before implementation;
- what the independent verifier found that execution-time validation did not.

After that comparison, decide whether the recurring core is robust enough for an instruction. Divergence should revise or reject the candidate rather than being forced into the first migration's format.

## Open questions

- What migration size or semantic risk justifies recording every occurrence?
- What is the minimum stable locator and evidence needed for independent verification?
- When should executable and generated consumers be in the initial scope rather than discovered by remediation?
- Which checks belong to execution-time validation, and which must remain independent verification?
- Is a second successful migration enough for promotion, or should promotion depend on recurrence of particular failure-prevention mechanisms?
