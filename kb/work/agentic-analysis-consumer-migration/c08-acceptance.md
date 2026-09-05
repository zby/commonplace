# C08 acceptance — transfer scan reads the exact main-review result

Executed locally on 2026-09-05. The changed consumer is
[`scan-agentic-system-transfer`](../../instructions/scan-agentic-system-transfer/SKILL.md),
called by step 9 of
[`analyse-agentic-system`](../../instructions/analyse-agentic-system/SKILL.md).
The runtime projections resolve to these canonical instruction files.

## Bounded positive replay

Neither recent minimal-state production run passes the current completion
validator. The positive check therefore used an isolated replay rooted at
`/tmp/commonplace-c08-replay-1g4g7h1x`, not a repaired or newly published run.

The replay copied Apache Maka's exact result and public projection from
`AAS-2026-09-04-apache-maka-02`. Only two compatibility defects were adapted in
the temporary copies: the result's Run state projection lost its `— complete`
suffix, and the state gained `legacy-review-model-partition: null`. The copied
state's result hash was recomputed. Substantive analysis and source anchors
were unchanged; the production originals were untouched.

The replay result was 61,769 bytes with SHA-256
`54c94f677d3253a051fe10edabf37b4df9571d2027b94a3201ab1a9429405a25`.
Its source boundary remained `https://github.com/apache/maka` at
`ece69ab3e7a1629a6073831005711d8aa7160ca4`. No legacy review corpus was copied
into the replay. This is a test fixture, not authorization to repair generated
production analyses or a claim that the original run now validates.

The bounded brief was:

> What does Maka's separation of retained memory and later consumption suggest for migrating Commonplace's review consumers to main-review outputs?

The scan read the full copied result and the copied current main-review
instruction, whose SHA-256 was
`96d80e4091619a57ba31886a32b95bdc80ffe1863c061d7633b7e0ff87208c12`.
It returned one confirmation: `OBJ-10`/`RTE-8` and `ABS-3` distinguish structured
retention from a later consumer, while `OBJ-9`/`RTE-7` identify an actual prompt
read-back route. The corresponding Commonplace observation was limited to the
main-review instruction's explicit result-to-scan handoff. The mapping was
qualified as partial and supported no observed or causal improvement claim.
Disposition: `no action`, since C08 already installs the identified handoff.

The written test output is local at
`/tmp/commonplace-c08-replay-1g4g7h1x/kb/reports/state/agentic-system-transfer/apache-maka-consumer-migration.md`.
It includes run/source identity, result size and digest, the exact brief,
consulted Commonplace digest, canonical record references, evidence limits,
freshness conditions, and cleanup disposition. No finding used a legacy
review or the compact projection as substantive evidence. Verification was
local, without an independent semantic checker.

## Input checks and validation

| Case | Result |
|---|---|
| Complete replay, before interpretation | Handoff exit 0. |
| Same replay, before output | Handoff exit 0; result and consulted-Commonplace hashes unchanged. |
| Replay changed to running state | Handoff exit 1; completion fields rejected. |
| Replay result changed after selection | Handoff exit 1; SHA-256 mismatch. |
| Original Pond run | Handoff exit 1; required legacy model partition missing. |
| Original Apache Maka run | Handoff exit 1; required nullable partition field missing and Run state projection malformed. |

The full test suite passed: **699 tests**, including instruction composition,
valid handoff, incomplete-run rejection, result-byte verification, and
publication checks. Both edited skills and the replay scan returned
`VALIDATION SUCCESS` with zero failures and zero warnings.

## Acceptance boundary and next consumer

C08's input migration is accepted. The positive replay demonstrates the new
read path and bounded output; the negative cases demonstrate rejection rather
than legacy fallback. It does not establish a fresh live analysis, change the
original runs' status, or validate every possible transfer judgment.

C09 can be selected next: a placement may use a tracked main-review projection
when that file itself supports the claim. Quantitative consumers still need a
supported field contract and a reproducible input population. Those decisions
must not be inferred from this transfer-scan trial.
