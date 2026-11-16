# Results: commit-plus-note fixture reconstruction

Executed 2026-11-14 under the operator-authorized [protocol](./provenance-reconstruction-trial.md), using existing commands and file/Git tools. No runtime implementation was added.

## Outcome

**Fixture reconstruction worked; complete execution-environment equivalence did not.** A committed KB plus the retained uncommitted target produced two independent review fixtures. Both made a new paid call on exactly the captured note and committed criterion, returned WARN and passed the checkout guard. The second harness launch advertised 38 additional Scry tools. Neither worker called them, but their different availability prevents claiming that only model-driven variation differed between the runs.

This is a successful bounded reconstruction exercise with an exposed harness-control gap, not a demonstrated fully controlled experiment, correctness test or verdict-stability estimate.

## What was reconstructed

- KB and executable-source commit at capture: `22841ddf938c0cd1e15f3d568862356650595c9b`.
- Target path: `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md`.
- Retained target SHA-256: `5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47`.
- Committed target SHA-256: `d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548`.
- Criterion: `prose/proportion-mismatch`; SHA-256 `1fbc48555406234f5fe384374a02c315b1c999ddb2c6e9d5cf7f311ca44c8fce`.

The two target hashes differ: this actually exercised uncommitted-text retention, not merely restoring a committed note. Each detached worktree started at the recorded commit, received the captured target at its original path, and had no review history. Other uncommitted main-checkout edits were deliberately not overlaid.

The current editable `commonplace-review` installation supplied code; the worktree supplied the library and profile. Explicit profile `opus`, pair grouping, one worker and a 180-second launch timeout were used. `--force` requested new evaluation; no `--resume` was used. Execution-source files were clean at capture and their recorded hashes remained unchanged through both runs. The main note still matched the original capture after execution.

## Execution accounting

| Trial | Run | Launches | Retries | Infrastructure failures | Outcome | Harness-reported cost |
|---|---|---|---|---|---|---|
| 1 | `20261114T165029Z` | 1 | 0 | 0 | WARN | $0.2497154 |
| 2 | `20261114T165109Z` | 1 | 0 | 0 | WARN | $0.2526004 |

Total: two launches, approximately **$0.5023**. Both report `claude-opus-5-5` through Claude Code `2.1.325`. Harness-reported durations were 23.544 and 26.618 seconds; these are not billing records or total fixture-setup times. No result was supplied by answer replay. Provider prompt-cache hits occurred; caching prompt computation is not reusing a previous review answer.

Both reviews identified excess ADR history in the library/workshop section relative to the core boundary model. This match was assessed by reading both outputs, not by an independent evaluator. The reviews differed in how they grouped findings and in their proposed treatment of the quality-scores paragraph. No edits were applied to the target and no claim of correctness follows from agreement.

## Verification

- Both launch input files matched the retained target byte for byte.
- Both criterion input files matched the committed criterion hash.
- Prompt texts matched after replacing worktree, run and launch path identifiers. This is equality of the controller's prompt, not of the entire harness-assembled model input.
- Both CLI reports said one pair was reviewed, and each retained run had exactly one distinct launch directory and a successful harness result event.
- Both checkout guards were clean. Per-worktree Git status before and after was identical: only the intended target overlay differed from the baseline.
- Recorded explicit tool calls in each trial were three Reads (prompt, criterion, note) and one Write (review output), all inside that trial's worktree. No linked-context, external-service or additional-agent tool call was observed.
- Fingerprints of the user settings file and user `CLAUDE.md` were unchanged. This is not an inventory or capture of every user-level resource.

## The control gap and its consequence

The initial harness event advertised the same base tools and skills, but trial 2 additionally listed 38 `mcp__scry__*` tools. The cause was not investigated. Unchanged settings fingerprints did not guarantee equal effective tool availability. Even unused tool availability can affect the input environment; the result does not establish that it had no effect here.

The existing profile's allowed-tools setting is not evidence that the harness exposes only those tools: the observed initial lists were much broader. A future trial claiming a fixed harness environment needs to explicitly restrict/configure that environment and verify the effective tool list, or retain this as an uncontrolled factor. No global harness settings were changed in this exercise.

Other limits:

- User-level resources, automatically loaded context and hosted inference internals were not fully captured. The retained launch trace is not asserted to be a complete serialized model request.
- A worktree and prompt restrictions do not prevent absolute-path access elsewhere. Explicit observed file reads stayed inside; this does not prove filesystem confinement or account for all automatic loading.
- The committed criterion has a supporting link, but neither worker followed it. This gate therefore did not exercise dynamic dependency discovery or ignored-snapshot recovery.
- No non-Git operational input was required by this selected gate. Connect and grounding operations still need their own dependency checks.
- The executable matched the KB commit here. Installing a historical executable from a different commit was not tested; dependency/package environments were not fully archived.

## Retained evidence and cleanup

Raw evidence is local at `kb/reports/state/stochastic-operation-testing/provenance-reconstruction-20261114/`:

- `manifest.json`: capture time, commit, target/criterion hashes, execution identity, source-code hashes and limited user-configuration fingerprints;
- `target.md`, `target.diff`, `main-status-before.txt`, `protocol.md`;
- `committed-tree.tar.gz`: 39,282,932-byte archive of the committed repository tree, allowing recovery of fixture content independently of a future branch tip;
- `trial-1/` and `trial-2/`: exact command records, exit codes, stdout/stderr, before/after status and complete copied review state, including launch inputs, prompts, outputs and traces;
- `verification.json`: input checks, accounting, observed tool calls, environment differences and archive digest;
- `worktree-cleanup.txt`: cleanup disposition.

The archive's SHA-256 is `041acafd348aafeff192de6368ac80e16df66f91e8b41e07d25dc435990a639e`. The two trial-owned worktrees were removed only after evidence copying and verification. Historical absolute paths in traces were left unchanged. The main checkout's target and review result store were not used as trial output locations. No commit or public upload was made.

Deleting this evidence would lose exact outputs and the recoverable fixture overlay. Preserve it for this workshop's design comparison; it is not disposable merely because it is ignored by Git.

## What this changes in the design

1. **Use commit plus retained target as the minimal content baseline.** This exercise demonstrates reconstruction for an actually uncommitted target with current tools. It does not require a new runner.
2. **Separate fixture identity from effective execution configuration.** Source and profile identities are necessary but insufficient: verify actual tool availability and state capture gaps.
3. **Keep ordinary and experimental costs separate.** The comprehensive repository archive was retained for the experiment, not proposed for every ordinary review.
4. **Add infrastructure only around demonstrated repetition or mistakes.** Shared capture/manifest generation and fixture preflight are plausible small improvements. A universal dependency graph or new orchestration engine is not justified by this exercise.
5. **Next controlled comparison needs a harness decision.** Either constrain the effective tool/configuration surface and verify it, or explicitly narrow the comparison's claim. No additional paid run is commissioned by this result.
