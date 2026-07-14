# Freshness module review — findings

Reviewed: `src/commonplace/freshness/` at `9c38b070`. Line numbers are from that revision.

All 18 tests in `tests/commonplace/freshness/` pass. Nothing here is currently breaking in production use — the correctness findings are landmines held safe by caller conventions, and the rest is dead weight. Ordered by what I'd fix first.

## 1. `commonplace-freshness-accept` is a shipped command that can never succeed

`V1_ACCEPT_TARGET_KINDS` is `frozenset()` (`transitions.py:285`). `accept_target_observations` (`transitions.py:342`) guards on it:

- `target_kind == "review-pair"` → raises "must use review capture finalization"
- anything else → raises "not supported for generic accept in v1"

There is no input that reaches the body. Verified by running it:

```
$ echo '{"schema":"commonplace-freshness-accept/1","target_kind":"collection-maintenance", ...}' \
    | commonplace-freshness-accept --input -
commonplace-freshness-accept: error: target kind 'collection-maintenance' is not supported for generic accept in v1
```

Unreachable as a result: ~95 lines of the function body (snapshot capture, revision allocation, baseline insert/update, input rewrite), the 73-line `cli/freshness_accept.py`, and the console-script entry in `pyproject.toml:35`. The two tests that cover it (`test_transitions.py:31`, `:53`) only assert that it raises — they pin the disabled state, not the feature.

This is the `AGENTS.md` YAGNI rule inverted: the generic-target accept path was built, then switched off, and left in the tree with a user-facing command that exists only to print an error.

**Fix:** delete the function, the CLI, the console script, and the two tests. Keep `InputObservation`, `parse_input_observation`, and `parse_target_key` — the ack and retire CLIs use them. If generic (non-review-pair) targets are still wanted, that belongs in `kb/reference/proposals/`, not in disabled code.

Downstream: `canonical_json` (`keys.py:8`) survives only through `_target_key_json`'s non-review-pair branch, which after this deletion is reachable only from `commonplace-freshness-retire --target-kind <anything-else>` — a call that can never match a row, because no such baseline can be created. Harmless, but it is scaffolding for a feature that does not exist.

## 2. Normalization asymmetry inside `refresh_review_baseline_from_captures`

In `baselines.py`, the read path normalizes the model partition and the write path does not.

- `_assert_capture_revision` builds its key with `normalize_model_partition(model_partition)` (line 93)
- `load_review_target` normalizes (line 33)
- but line 156 builds `target_key_json` from the **raw** argument, and hands that to the `INSERT` (line 167) and to both generation-ledger calls (lines 162, 178)

Every current entry point normalizes before calling — `review_db.py:746` and `ack_target_inputs` (`transitions.py:452`) — so this is latent. But it means the function is correct only because of a convention it does not enforce. A new call site passing an unnormalized partition (`"claude-opus-4-8[1m]"`, say) would CAS against one baseline row and write to a different key, splitting the generation ledger.

**Fix:** normalize once at the top of the function and use that value throughout.

## 3. A CAS function whose default is "don't CAS"

`refresh_review_baseline_from_observation` (`baselines.py:224`) takes `expected_baseline_revision: int | None = None`. When it is `None`:

```python
cas_revision = expected_baseline_revision if expected_baseline_revision is not None else current.revision
if cas_revision != current.revision:   # trivially false
```

The guard degrades to asserting a value equals itself. The one production caller (`review_db.py:802`) does pass a revision, so the default is never exercised — but a compare-and-swap whose default silently disables the compare is a footgun.

**Fix:** make the parameter required.

## 4. The same docstring states an invariant the function doesn't hold

`refresh_review_baseline_from_observation`'s docstring says "preserve evidence pair id". It does not — it forwards whatever `evidence_review_pair_id` the caller passes straight into `refresh_review_baseline_from_captures`, which deletes and reinserts the evidence row.

The preservation lives in one of its two callers: `ack_target_inputs` reads the existing id out of `review_freshness_evidence` first (`transitions.py:467-477`) and passes it back in. The other caller, `review_db.py`'s observation branch, passes a **new** evidence pair and replaces it. So the docstring describes one caller's behaviour and misdescribes the other's.

## 5. Triple CAS on the ack path

One ack checks the same revision three times inside a single transaction, with nothing able to change between them:

1. `ack_target_inputs` (`transitions.py:461`)
2. `refresh_review_baseline_from_observation` (`baselines.py:250`)
3. `_assert_capture_revision`, via the call at `baselines.py:255` (`baselines.py:111`)

Layer 2 is a thin wrapper that mostly re-does what layer 3 already does. Collapsing 2 into its callers would leave one CAS at the boundary and one at the write, which is the defensible shape.

## 6. Dead exports and dead returns

| Symbol | Location | Status |
|---|---|---|
| `refresh_target_from_captures` | `transitions.py:557` | Zero callers. Pure passthrough to `baselines.refresh_review_baseline_from_captures`. |
| `superseded_target_id` | 2nd element of `refresh_review_baseline_from_captures`'s return tuple | Never consumed. `review_db.py:781` discards the tuple; `transitions.py:269` discards it as `_`; the only other reader is the dead passthrough above. |
| `ArtifactSnapshot.path` | `models.py:15` | Unused alias for `artifact_path`. |
| `V1_ACCEPT_TARGET_KINDS` | `transitions.py:285` | Exists only to disable finding 1. |

`refresh_review_baseline_from_captures` should return `int | None`, not a tuple.

## 7. The selector re-hashes the same files once per baseline

`_changed_inputs_for_baseline` (`selector.py:65`) calls `resolve_file_text` — read + SHA256 — for each of a baseline's two inputs, with no memoization across baselines. Criterion files are shared by many notes, so they get re-read and re-hashed once per note that cites them.

Measured against the live store:

| | count |
|---|---|
| baselines | 262 |
| file reads + hashes per `freshness-status` run | 524 |
| distinct criterion paths | 37 |

Each criterion file is re-hashed roughly seven times per run, and the redundancy grows with the KB. A `dict` cache keyed on path, scoped to one `select_stale_review_targets` call, removes most of it.

## 8. Snapshots are never collected, and the integrity check is O(store)

`assert_snapshot_hash_integrity` (`integrity.py:10`) pulls every snapshot's full `content_text` into Python and rehashes it. At today's 59 snapshots / 258 KB that is nothing, but it is an unbounded full-table scan.

The reason it is unbounded: nothing ever deletes `artifact_snapshots` rows. `retire_target` deletes the baseline, and the FK cascades clear `freshness_inputs` and `review_freshness_evidence` — but the snapshots those inputs pointed at are left behind with no referent. Both the table and the check grow monotonically for the life of the store.

Whether that matters is a judgement call (snapshots are also the evidence trail), but it should be a decision, not an oversight.

## 9. Minor

- **`selector.py:96-121`** — three `except` blocks, two with byte-identical bodies. `UnicodeDecodeError` is a subclass of `ValueError`, so it is redundant in the tuple at line 96. The whole thing collapses to `except (ValueError, OSError)`.
- **`parse_input_observation`** (`transitions.py:609`) — checks `len(content_sha256) == 64` but never checks the characters are hex, while the error message promises "64 lowercase hex". A non-hex 64-char string passes and is caught later by the schema `CHECK` with a worse message.
- **`status._accepted_text`** (`status.py:92`) — guards `snapshot.content_text is not None` on a field typed `str` backed by a `NOT NULL` column. Dead check; mirrored at `review_db.py:756` and `:762`.
- **`status._attach_diffs`** (`status.py:59`) — reads the file with a bare `read_text`, bypassing `normalize_repo_relative_path` / `resolve_file_text`, with no handling for a file that vanishes between selection and diffing.

## Checked and found sound

Recording these so a later pass doesn't re-derive them:

- **FK cascade on retire.** `PRAGMA foreign_keys = ON` is set in `store.connect` (`store.py:43`), so `retire_target`'s single `DELETE FROM freshness_baselines` does cascade to `freshness_inputs` and `review_freshness_evidence`. (I initially thought the pragma was missing — that was a bad `rg -r` invocation on my side mangling its own output, not a real gap.)
- **Revision monotonicity across retire and recreate.** The invariant `baseline.revision == ledger.next_revision - 1` holds through both `allocate_initial_revision` and `allocate_successor_revision`, and `retire_target` deliberately leaves `freshness_target_generations` alone. A pair queued against a target that is then retired and recreated fails CAS, which is the point of the ledger.
