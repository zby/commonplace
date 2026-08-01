# Post-run audit of the premise-cohort replication

This audit was written after scored output was frozen. It corrects the interpretation and provenance record without changing the frozen protocol, records, aggregation, or `REOPENS` decision under that protocol.

## Substantive interpretation

The run's single-choice mapper taxonomy combines different questions:

- C1–C12 mostly classify the semantic relation asserted from A to B;
- C13–C14 classify whether the relationship deserves formal representation;
- C15 records an epistemic failure of the frozen observation.

Those outcomes are not mutually exclusive on one semantic axis. A relationship can, for example, be semantically a premise while belonging only in connective prose. Counting C13 as an alternative to C1 therefore supports withholding a registered edge but does not refute the premise relation itself.

The controls are asymmetric. Sixteen negative controls test whether the pipeline indiscriminately overcalls C1, and 0/16 received a C1 majority. There is no known-positive C1 cohort, so the run does not test whether the observer/mapper pipeline systematically undercalls premise relationships. The exact alternative taxonomy was also unstable: 15/49 primary rows and 26/78 total rows had three different mapper classes.

The result consequently supports one action: do not migrate the historical cohort from its existing ledger. It does not support deleting `premised-on`, assigning the mapper alternatives to individual rows, or treating the alternative-class distribution as a discovered vocabulary.

## Relation to the original reversal condition

The frozen protocol defined every stable non-C1 majority and every unstable row as adverse. The earlier grounds review had proposed a narrower reversal condition: roughly 20% of P rows triggering design/rule reconsideration rather than truth/applicability reassessment. C4 is the mapper class that directly represents that alternative, and 9/49 primary rows had a stable C4 majority.

The 44/49 outcome therefore crosses the run's pre-registered gate but does not literally instantiate the earlier reversal condition. The protocol result remains `REOPENS`; the defensible interpretation is a migration hold and demand for a calibrated instrument, not reversal of the semantic decision.

## Execution deviations discovered afterward

1. **The exact fixture builder was not retained.** An attempted patch adding `fixture-build.py` failed, and the successful build ran as a one-shot heredoc in the orchestrating session. `fixture-build.md` describes the transformations and the retained manifests bind their outputs by digest, but the run directory does not preserve the exact executable algorithm or neutral-ID salt. The outputs are inspectable; the fixture cannot be reproduced solely from committed run artifacts.
2. **Mapper order was not independently randomized.** Stage 2 consumed each observation JSONL in its frozen Stage-1 order. This departs from the instruction requiring a newly randomized mapper order. The deviation was consistent across passes but leaves case-order effects uncontrolled.
3. **One unreported observer dispatch was aborted.** Before the concurrent launcher was used, `observer-1-1` completed and a sequential `observer-1-2` process was interrupted approximately 13 seconds after launch. It produced no retained scored output. The final nine observer passes are complete, but the abandoned launch should have appeared in the run amendments.
4. **Repository-root governance exposure is unknown.** Scored commands used `-C` with the external fixture root, and that root had no `AGENTS.md`. No trace read the Commonplace root. The frozen protocol's statement that Commonplace's root `AGENTS.md` remained ambient is therefore unsupported and likely false under ordinary working-directory instruction discovery. The exact ambient instruction payload was not captured, so absence cannot be proven from the retained run alone.
5. **The worker's `git diff --check` did not cover untracked artifacts.** A direct hygiene scan found one missing final newline in the non-scored `calibration/synthetic-sanitized.md`; no other whitespace failure was found. The newline was added after the audit and `synthetic-check.json` was updated from the original digest `a865fa93476145654773a905528db2d7e1cf6a41947588526dff7dfd12cd4311` to the repaired digest. No scored content changed.

The orchestrating Codex session carrying the builder and aborted-dispatch evidence has session ID `019fb20f-f1d9-7c41-ac45-b10bc97f6a39`. It is external provenance, not part of the retained run bundle.

## Retry sensitivity

The two malformed mapper attempts were preserved and retried with identical prompts. Their valid records differ materially from the corresponding retry records, which reinforces that exact alternative assignments are not stable. A hybrid recomputation using valid first-attempt records and retry output only for the missing or malformed record yields 45/49 adverse primary rows and 0/16 C1-majority negative controls. The migration hold does not depend on choosing the retry records.

Ten primary rows were unanimously non-C1, exactly the run's count boundary under the stricter sensitivity of requiring three matching non-C1 votes. This supports the protocol-level hold, while the missing positive controls still prevent an inference about the premise relation's sensitivity.
