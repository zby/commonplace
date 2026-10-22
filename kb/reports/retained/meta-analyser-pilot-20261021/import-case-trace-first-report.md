# Outcome: likely material residuals found

- **Run-id:** `synthetic-import-01`
- **Method-commit:** `synthetic-no-git-commit`
- **Source-revision:** `synthetic-no-git-revision`
- **Case:** Constructed source-and-trace fixture, not an observed system.

One material defect survives in both accepted outputs: a native-only approval requirement is presented as universal. The trace supports a connection to an unrecovered evidence-acquisition gap following a failed read, but does not establish that the failed read alone caused the overgeneralization.

Paths below are relative to the supplied fixture directory, `/home/zby/llm/commonplace/kb/reports/retained/meta-analyser-pilot-20261021/fixture/`.

## Residual findings

### 1. Universal approval claim overlooks the batch bypass

**Disposition: `likely-material-residual`**

**Accepted passages**

- `accepted/synthesis.md:3`: “All import paths require explicit user approval before retained data is written.”
- `accepted/memory-profile.md:3`: “Admission: explicit user approval is required for every import path.”

These statements materially misdescribe the importer’s admission boundary.

**Process failure and prevented work**

The worker attempted to read `source/import_policy.py`, but the read failed with `ENOENT` (`worker.jsonl:4–5`, call **c1**). It acquired no policy evidence from that operation. This was a standalone read; no chained operations were demonstrably skipped.

The assignment expressly required inspection of native **and batch** paths before any universal approval claim (`method/worker.md:3`; also returned by **c0**, `worker.jsonl:2–3`). After the failure, the worker read:

- The native handler, which checks approval (**c2**, lines 6–7).
- The README, which explicitly says batch imports use a separate path (**c3**, lines 8–9).

It then wrote the universal claim (**c4**, lines 10–11), without a recorded batch-path read.

**Direct evidence of the surviving defect**

- `source/native_import.py:1–4` checks `approved`, raises `PermissionError` when false, and otherwise calls `persist(rows)`.
- `source/README.md:3` distinguishes the native and batch paths.
- `source/batch_import.py:1–3` defines `import_batch(rows)` without an approval argument, explicitly comments that trusted batch import bypasses interactive approval, and calls `persist(rows)` directly.

Thus, the accepted native-handler description is supported, but its extension to every import path is not. The omitted trusted-batch mechanism changes how a reader understands whether approval universally precedes persistence.

**Causal connection and limits**

The observed chain is: failed policy-file read → successful native-only implementation read plus notice of a separate batch path → unsupported universal claim → acceptance without further source inspection. This connects the surviving defect to an unrecovered evidence gap in the same approval-policy investigation, rather than merely pairing an unrelated error with a content defect.

However, the trace does **not** show that the nonexistent `import_policy.py` would have described batch behavior, or that the failed read prevented a subsequent batch read. The README supplied an independent opportunity to recover. The supported conclusion is incomplete recovery and overgeneralization after the failure—not that the `ENOENT` necessarily caused the omission.

**Recovery checked**

The complete supplied trace contains no later batch read or equivalent policy evidence. The only subsequent correction changes a validation marker (**c6**, lines 14–15). The successful validator result expressly says, “This is not claim support” (**c7**, lines 16–17). Both accepted outputs retain the universal claim.

**Smallest follow-up**

Revise both accepted passages to distinguish the approval-checked native path from the trusted batch path that persists without interactive approval. The supplied source already settles this fixture-level distinction; no execution or validation rerun is needed.

## Incident dispositions

| Incident | Disposition | Decisive evidence |
|---|---|---|
| **c1**, failed `import_policy.py` read; scanner incident at `worker.jsonl:5` | **likely-material-residual**, with causal limits above | The read supplied no evidence. Later reads covered native behavior and identified a separate batch path, but no batch implementation read followed. The resulting universal claim survives and conflicts with `source/batch_import.py:1–3`. |
| **c5**, validator exit 1; scanner incident at `worker.jsonl:13` | **recovered** for the reported marker failure | The diagnostic concerned retention of `Validation: pending`. **c6** replaced that marker; **c7** then reported a content-check pass. This repairs the explicit validation failure, not the approval claim. |

**Additional observed errors:** None established beyond the scanner incidents. The marker edit was not a semantic repair, but the trace does record a successful subsequent check; it should not be characterized as an unrecovered validator failure.

**Successful-result sampling:** Inspected all successful results on this chain, including **c7**, the only successful shell result. Its disclaimer limits the significance of the pass. No masked upstream failure or additional shell diagnostic was observed.

**Unresolved incidents:** None separate from the stated causal limits.

## Coverage and limits

- Examined the sole inventoried launch, **`fixture-runtime-1`**, marked delivered and accepted.
- Examined both scanner incidents and the complete supplied worker trace: **c0–c7**, eight completed tool operations.
- Read the exact worker assignment, both final accepted outputs, and all three inventoried source files.
- No listed packet input remains unexamined. No requested read was truncated; the tool budget was not exhausted.
- The packet contains no validator implementation, separate author/verifier trace, or publication-transformation history. Its validator result supports only the stated content-check recovery.
- Source inspection establishes the explicit batch approval bypass; it does not establish behavior inside the undefined `persist` function or any external caller. Neither is needed to reject the accepted universal characterization of these import paths.
- This is a bounded process audit, not a correctness certificate or a claim about a deployed system.
