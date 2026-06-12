---
description: "Review execution is unified on (note, gate) pairs: one sentinel grammar keyed by the full pair, one prompt renderer, one batch executor with a salvage failure policy; bundle and gate sweep become packing strategies over the same pair protocol"
type: ../types/adr.md
tags: []
status: accepted
---

# 029-Review execution unified on (note, gate) pairs

**Status:** accepted
**Date:** 2026-06-12

## Context

The unit of review work is one (note, gate) pair — the database already keys `gate_reviews` and acceptance on it — but execution ran through two divergent paths that differed only in which axis they held constant when packing pairs into one LLM call: `run_review_bundle` (one note, many gates, `GATE REVIEW START/END` sentinels) and `run_gate_sweep` (one gate, many notes, `NOTE START/END` sentinels wrapping gate blocks). Each path carried its own prompt renderer, parser, footer-rewriter, and failure policy. The duplication produced concrete defects: the sweep path re-rendered extracted reviews as synthetic single-note bundles and re-parsed them to reach the shared finalize tail; usage-exhaustion detection existed only in the bundle path and interrupt handling only in the sweep path; and parsing was all-or-nothing per call, so one missing block discarded every already-parsed review in the batch. All sweep modules were flagged experimental, so the grammar was free to change.

## Decision

1. **One pair grammar.** Every output block is keyed by the full pair: `=== PAIR REVIEW START: {note_path} :: {gate_id} ===` … `=== PAIR REVIEW END: … ===` (`protocol/format.py`). The ` :: ` separator is rejected in note paths and gate ids at render time, as are reserved `=== … ===` sentinel lines inside embedded note or gate text.
2. **One renderer.** `render_pairs_prompt` (`protocol/prompt.py`) takes N note targets and M gate definitions, embeds each note text and each gate text exactly once, and requests one block per requested pair. Note contents are always embedded (`Do not read them from disk`), in both single-note and multi-note shapes; the multi-note shape adds the evaluate-independently rule. `output_mode` (`stdout`/`file`) is preserved for the live-agent path.
3. **One parser with salvage semantics.** `parse_pair_bundle` (`protocol/parser.py`) raises on structural anomalies (nested, mismatched, unterminated, unexpected, duplicate, or empty blocks) because the rest of the stream is untrustworthy, but a missing expected pair is reported in `missing`, not raised — callers salvage what parsed.
4. **One executor.** `executor.execute_batch` owns the shared lifecycle: render, one runner call, telemetry and model-mismatch handling, usage-exhaustion and interrupt handling, parse, then per-run finalize. A run whose pairs all came back is finalized; a run with missing pairs is failed individually with the raw batch output attached; other runs in the batch are unaffected. Within one run finalization stays all-or-nothing (coverage validation in `record_and_finalize_run` is unchanged).
5. **Batching is a packing choice, not a protocol.** `run_review_bundle` is the share-note packing (one note's gates per call) and `run_gate_sweep` the share-gate packing (one gate over a chunked note list, one single-gate run per note); both are thin callers of the executor. `review_sweep`'s thread-pool fan-out over `run_bundle` is untouched. The live-agent path (`create-review-run --with-prompt` → agent writes `bundle-output.md` → `ingest-bundle-output`) consumes the same grammar; per the consolidation decision its single-run ingest remains all-or-nothing.
6. **Per-run artifacts are pair-grammar slices.** Each run's `bundle-output.md` and DB `raw_bundle_markdown` hold the run's own canonical pair blocks; the full raw batch output is preserved in the debug log and attached to failed runs.

Old-grammar text stored in historical `gate_reviews` rows stays readable: decision parsing (`protocol/decisions.py`) is grammar-independent and unchanged.

## Consequences

Easier:
- Protocol changes (new fields, sentinel rules, coverage checks) are made once; the parse→render→parse round trip and the twin parsers/rewriters are gone.
- Partial batch failures salvage completed reviews and fail only the missing runs — the dominant efficiency win when many small checks run at scale.
- Failure policy (usage exhaustion, interrupts, runner errors) is uniform across packing shapes.
- Mixed-axis packing (arbitrary pairs per call) is structurally supported by the renderer/parser/executor, available when a caller wants it.

Harder / accepted costs:
- Notes whose body contains a reserved `=== … ===` line can no longer be reviewed by either path (previously the single-note bundle path did not embed the note and tolerated this). Render fails loudly; an escaping scheme can be added if this bites.
- The pair key repeats the shared axis in every sentinel — a small token cost paid for a parser that never infers a missing axis from prompt context.
- Packing shape is not yet recorded as run provenance; per-pair cost attribution from per-call telemetry remains approximate. Recording strategy/batch id on `review_runs` is a candidate follow-up, as is re-asking only missing pairs in a follow-up call.

---

Relevant Notes:

- [review architecture](../review-architecture.md) — part-of: the subsystem this decision restructures
- [gate learning from accepted edits](../proposals/gate-learning-from-accepted-edits.md) — see-also: adjacent undecided extension; per-gate accounting interacts with the packing axis
