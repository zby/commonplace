# Agentic-system analysis operability replay

This retained set is the acceptance record for implementing the operability
hardening plan against a real `analyse-agentic-system` replay. It preserves the
recovered original output and failure account, the new canonical replay result,
and the exact operational receipts needed to audit source identity, phase
progression, worker packet identity, reconciliation, validation, and handoff.

## Inputs and method

The replay analysed Academic Research Skills at Git commit
`94436237913091d4739870159d241660527e8338`. The source came from the public
codeload URL
`https://codeload.github.com/Imbad0202/academic-research-skills/tar.gz/94436237913091d4739870159d241660527e8338`.
The archive was 12,341,902 bytes with SHA-256
`e298af69dc06ffb6642e5a64141954f3b4169e793626db907bedb0decd22d08c`.
It contained 2,976 entries under one expected root and no absolute or
parent-traversal member names. The archive itself is not retained because its
immutable public identity and digest are sufficient to reacquire and verify it.

Run `AAS-2026-09-03-academic-research-skills-02` declared its retained carrier,
consumer, cleanup condition, compact projection, and write authority before
source acquisition. It then advanced monotonically through `opened`,
`source-frozen`, `runtime-sealed`, `lenses-issued`, `lenses-complete`,
`reconciled`, `assembled`, `validated`, and `handoff-ready`. Fresh
memory/context and epistemic workers received immutable P1 packets built from
the same sealed runtime baseline. Both returns matched their seven identity
fields and baseline digest. Reconciliation accepted both, registered their new
record proposals, advanced CANON-v1 to CANON-v2, and required no correction
packet. The original same-revision persistent-FAIL conflict remains unresolved.

## Results and retained identities

- [Canonical replay result](./AAS-2026-09-03-academic-research-skills-02.md):
  59,578 bytes; SHA-256
  `d178c554ed843caf50b6177e35dc498708454668c15bf72f30b945f3374fad9d`.
- [Recovered original result](./original-run-captures/AAS-2026-09-03-academic-research-skills-01.md):
  exact 49,210-byte copy; SHA-256
  `d2115eee13c2afc528a74a8a2abc722562215af1dd9c97452a3305036886041c`.
- [Recovered original failure account](./original-run-captures/academic-research-skills-aas-2026-09-03-01.failures.md):
  exact 6,062-byte copy; SHA-256
  `7d010f16e5deeba6bbbf57cfbe26d360adc88a87a4a4f19495043fb98c77c095`.
- [Sealed runtime baseline](./replay-receipts/runtime-baseline.md): SHA-256
  `29dadeea6a5b2e76fc9959f91a18dc9e70f1f9d70d43ff5aab0785ccb715d458`.
- Memory packet and return: SHA-256
  `6d719519f501033d6c459958f28007c5b148e24e04c3c1cfae5cf5ce910941b9`
  and
  `9adbac7f277fde6dcd30b7876f0609b0ae60a091df55c4dab3b1252fab867376`.
- Epistemic packet and return: SHA-256
  `b20703fc0dd1134ee301fec93c2fb0d1dbacbe7f7186771ff40eb37e4fd9f1cd`
  and
  `3110fdf594ea9572a82970d838f043a7d36c1808f2dc4ddf730163954a5ba621`.
- [Reconciliation](./replay-receipts/reconciliation.md): SHA-256
  `34ce025349973362925f5f10225f1e0b9fefdbf620f7f6391e5866486f7ba3b0`.
- [Decisive validation receipt](./replay-receipts/validation.json): exact JSON,
  SHA-256
  `d7308e9fce3f2b2bfc194a2ab71193eeff1a704db3841925404e27f2e0f0f988`.
  It reports schema `commonplace.validation.v1`, status `success`, one intended
  `agentic-system-analysis-result`, and zero warnings and failures.
- [Final run state](./replay-receipts/run-state-final.md): SHA-256
  `e9f12349e4fb6fb5520cf38d3d6ab5bf1df03eb8bb36abdcc46634463a788ffa`.

The compact library projection is
[Academic Research Skills](../../../agentic-systems/academic-research-skills.md).
Reconciliation found material drift only in its persistence account. The note
now names the additional executable human-read, inquiry-ledger, update-state,
and claim-standing read-back routes and links to the retained replay. It does
not replace the exact result.

## Original failure dispositions

| Original failure area | Replay disposition | Acceptance meaning |
|---|---|---|
| Source acquisition | The commit-pinned codeload route completed with exit 0; archive identity and member safety were recorded. The original command, working directory, environment, exit status, and exact output are unavailable. | The replay proves a clean preselected route and better evidence capture. It does not prove that a reconstructed Git or credential defect was fixed. |
| Inspection commands | One broad orientation search returned truncated output and was explicitly invalidated. Bounded file counts and line reads supplied accepted evidence. Every source command used the frozen source root as its working directory. | Truncation and wrong-directory evidence contamination were contained before synthesis. |
| In-flight correction | The load-bearing persistent-FAIL source conflict was registered before dispatch. Both fresh P1 packets used the same sealed baseline; neither required correction. The validator and tests still enforce immutable replacement packet/version rules if a later conflict does require correction. | This replay exercises clean issue/return/reconciliation. It does not erase the original run's valid P1 invalidation and replacement history. |
| Deterministic validation | The canonical result was assembled first, hashed, and then checked by one JSON validation target. The retained receipt names exactly one normalized artifact type and zero warnings or failures. The original validator behavior cannot be reconstructed from the surviving summary. | The new receipt removes result/type ambiguity. It is prevention evidence, not proof of a specific historical validator defect repair. |
| Output routing | The carrier, physical form, named future consumer, retention, cleanup, projection, and write authority were fixed in `opened`; assembled and handoff hashes match it. | A compact projection can no longer silently stand in for a requested exact result. |
| Retention | The recovered original, failure account, canonical replay, and replay receipts are retained together. | A clean checkout can audit the acceptance comparison without an ignored cache or live temporary directory. |
| Shared worktree | Writes stayed within declared replay/implementation paths. The two pre-existing workshop changes were neither edited nor included in any implementation or replay commit. | Concurrent user work was contained and remains independently reviewable. |
| Source-side conflict | The runtime baseline and final result preserve the contradictory persistent-FAIL rules without selecting a winner. | Operability hardening changed analysis control and evidence, not the external system's doctrine. |

## Implementation and verification

Three implementation commits precede this retained replay:

1. `d2efffdf` exposes validated artifact identities and normalized types in JSON
   output.
2. `046166a7` adds checked analysis-run state, immutable packet/return identity,
   carrier and retention declarations, phase gates, and skill instructions.
3. `2c0581d6` permits accepted new-record proposals to advance the reconciled
   canonical register without falsely requiring a correction packet.

The implementation suite passed 648 tests, and Ruff reported no findings. The
canonical replay result, final run state, and compact projection each pass
their relevant deterministic validation. The decisive result receipt is the
retained JSON file above.

## Limits

This acceptance run is code-grounded, not an observed execution of the external
plugin and not a causal evaluation. It establishes that the hardened workflow
can preserve authority, source, packet, reconciliation, output, and validation
identity through a realistic two-lens analysis. It cannot establish external
host adherence, model or human activation, service correctness, research
quality, or that the original run's unrecorded commands behaved in any
particular way.
