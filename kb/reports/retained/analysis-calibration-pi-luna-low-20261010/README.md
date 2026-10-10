# Pi Luna low-effort synthesis calibration pilot, 2026-10-10

The eight-case exploratory pilot detected all four inserted defects. Three
supported controls were accepted. The fourth control was blocked on a
potentially valid objection to its evidence-resolution wording; it is disputed,
not scored as a clean false blocker. All eight launches completed.

This exact record is retained for calibration scoring and adjudication. It is
not evidence of full workflow reliability or a measured general error rate.

## Inputs and execution

- Method commit: `6f335416fbf2b1506154e7a76373bee9decf98af`.
- Profile: `pi-luna-low`, Pi, launch model `gpt-6-luna`, effort `low`.
- Launch tool: project `commonplace-worker` through `functions.subagent` with
  model argument `openai/gpt-6-luna` and `thinkingLevel: low`.
- Resolved model version, token usage, elapsed time and cost: unknown; not
  supplied by the tool results.
- One call per case, no retries. First `c05`, then the other seven in one
  parallel tool call; completion order within that call is not established.
- The profile was newly added and uncommitted. Its exact working-tree bytes are
  retained separately; method instructions came only from the named commit.
- Workers used fresh conversations but filesystem restrictions were
  instruction-only. Project instructions could load. The operator explicitly
  approved this relaxation for the exploratory pilot.
- The author-proposed answer key was not independently reviewed before launch.
  Scoring annotations are the coordinator's assessment, not human verification.

## Results

| Pair | Faulty case | Supported control |
|---|---|---|
| Source support | c01: detected | c02: accepted |
| Quotation entailment | c03: detected | c04: accepted |
| Inventory coverage | c05: detected | c06: accepted |
| Limit consequence | c07: detected | c08: disputed blocker |

In c08 the verifier accepted the main claim about durable updates and the
withheld improvement conclusion. It rejected “A later-task outcome comparison
would resolve this limitation,” citing the record contract's rule that a
contrast is necessary but not sufficient for causal identification. The original
key expected no blocker. Whether the response overreads the wording or the
fixture overstates sufficiency needs independent adjudication. The key has not
been changed after observing the response. Literal agreement with the original
key is seven of eight, but that is not seven verified correct judgments.

The pilot supplies no observed missed-defect case for developing a verifier fix.
Its immediate value is demonstrating runnable profile selection and exposing a
possible control-fixture ambiguity. Larger legitimate workloads are still needed
before judging workload-sensitive failures.

## Exact evidence

- [Manifest](./capture/manifest.json): method commit, profile source and pinned
  input hashes.
- [Launch record](./capture/launch-record.json): tool settings, dispatch and
  isolation limits.
- [Annotations](./capture/annotations.json) and [score](./capture/score.json).
- [Original key](./capture/private/expected.json) and
  [protocol snapshot](./capture/private/protocol.md).
- Raw verdicts: [c01](./capture/packets/c01/response.md),
  [c02](./capture/packets/c02/response.md), [c03](./capture/packets/c03/response.md),
  [c04](./capture/packets/c04/response.md), [c05](./capture/packets/c05/response.md),
  [c06](./capture/packets/c06/response.md), [c07](./capture/packets/c07/response.md),
  [c08](./capture/packets/c08/response.md).

The capture is frozen. Corrections or adjudication should be new records, not
edits to the original packets, answer key or responses. Hash verification checks
that bytes remain unchanged; it does not verify actual model identity or prove
that workers obeyed filesystem scope.
