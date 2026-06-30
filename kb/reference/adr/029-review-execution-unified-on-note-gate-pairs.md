---
description: "Review execution is unified on note-gate pairs: one sentinel grammar, renderer, parser, and finalization path; note and gate packing are strategies over the same protocol"
type: ../types/adr.md
tags: []
status: accepted
---

# 029-Review execution unified on (note, gate) pairs

**Status:** accepted
**Date:** 2026-06-12

## Context

The unit of review work is one (note, gate) pair — the selector and acceptance state already reasoned on that key — but execution previously ran through two divergent paths that differed only in which axis they held constant when packing pairs into one LLM call. Each path carried its own prompt renderer, parser, footer-rewriter, and failure policy. The duplication produced concrete defects: one path re-rendered extracted reviews as synthetic single-note bundles and re-parsed them to reach the shared finalize tail; failure detection differed across paths; and parsing was all-or-nothing per call, so one missing block discarded every already-parsed review in the batch. The experimental grammar was free to change.

## Decision

1. **One pair grammar.** Every output block is keyed by the full pair: `=== PAIR REVIEW START: {note_path} :: {gate_id} ===` … `=== PAIR REVIEW END: … ===` (`protocol/format.py`). The ` :: ` separator is rejected in note paths and gate ids at render time, as are reserved `=== … ===` sentinel lines inside embedded note or gate text.
2. **One renderer.** `render_pairs_prompt` (`protocol/prompt.py`) takes N note targets and M gate definitions, embeds each note text and each gate text exactly once, and requests one block per requested pair. Note contents are always embedded (`Do not read them from disk`), in both single-note and multi-note shapes; the multi-note shape adds the evaluate-independently rule. `output_mode` (`stdout`/`file`) is preserved for the live-agent path.
3. **One parser with salvage semantics.** `parse_pair_bundle` (`protocol/parser.py`) raises on structural anomalies (nested, mismatched, unterminated, unexpected, duplicate, or empty blocks) because the rest of the stream is untrustworthy, but a missing expected pair is reported in `missing`, not raised — callers salvage what parsed.
4. **One finalization path.** Shared job-output code owns parse, result-file writes, pair completion, missing-pair marking, acceptance events, and job status. A job whose pairs all came back is completed; a job with missing pairs is failed with the raw batch output attached while completed pairs remain salvageable.
5. **Batching is a packing choice, not a protocol.** Note-packed jobs and gate-packed jobs both use the same pair grammar, parser, and finalization path. The parent agent or harness owns fan-out; Commonplace owns deterministic job creation and finalization.
6. **Per-job artifacts are pair-grammar slices.** Each job's `bundle-output.md` holds the job's own pair-block stream; parsed result files are named from the job's packing strategy, and `MANIFEST.json` maps pairs to those files. Later storage work moved review bodies out of DB columns, so the DB now records artifact paths instead of storing raw review markdown.

ADR 031 later makes the same pair unit persistent in the SQLite schema by replacing the earlier gate-specific rows with `review_pairs`.

## Consequences

Easier:
- Protocol changes (new fields, sentinel rules, coverage checks) are made once; the parse→render→parse round trip and the twin parsers/rewriters are gone.
- Partial batch failures salvage completed reviews and fail only the missing runs — the dominant efficiency win when many small checks run at scale.
- Failure policy is uniform across packing shapes.
- Mixed-axis packing (arbitrary pairs per call) is structurally supported by the renderer/parser boundary, available if a future caller needs it.

Harder / accepted costs:
- Notes whose body contains a reserved `=== … ===` line can no longer be reviewed by either path (previously the single-note bundle path did not embed the note and tolerated this). Render fails loudly; an escaping scheme can be added if this bites.
- The pair key repeats the shared axis in every sentinel — a small token cost paid for a parser that never infers a missing axis from prompt context.
- Per-pair cost attribution from per-call telemetry remains approximate. Re-asking only missing pairs in a follow-up call is a candidate follow-up.

---

Relevant Notes:

- [review architecture](../review-architecture.md) — part-of: the subsystem this decision restructures
- [gate learning from accepted edits](../proposals/gate-learning-from-accepted-edits.md) — see-also: adjacent undecided extension; per-gate accounting interacts with the packing axis
- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — see-also: the storage refinement that makes this protocol's pair unit the persistent row
