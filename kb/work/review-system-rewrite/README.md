# Workshop: review-system-rewrite

## Question

If we could afford a full rewrite of the review system code, what structure would best serve its goals given its real constraints?

## Why this workshop exists

The review system has grown organically through ~10 workshops and migrations. It works, but the code structure has accumulated tangles:

- Parsing logic spread across three modules (run_review_bundle, gate_sweep_format, review_decisions).
- `review_db.py` (910 lines) mixes SQL with finalization orchestration, coverage validation, and auto-acceptance rules.
- Bundle and gate-sweep are two near-duplicate pipelines that differ only in batching shape.
- Runner distinction (subprocess vs live-agent) is a fork inside run_review_bundle, not a strategy.
- Provenance flows as bare `(sha, commit)` tuples through five modules.
- Freshness logic is duplicated between review_target_selector and warn_selector.
- CLI review_sweep.py has business logic that should live in the library.

This workshop designs the target architecture. Not a plan to execute now — a reference point for incremental refactoring and for evaluating whether future changes move toward or away from the ideal structure.

## Current grounding

- [REVIEW.md](../../../src/commonplace/docs/REVIEW.md) — code architecture overview
- [REVIEW-SYSTEM.md](../../instructions/REVIEW-SYSTEM.md) — workflow contract
- [review-run-lifecycle](../review-run-lifecycle/README.md) — prior lifecycle tightening workshop
- [review-prompt-consolidation](../review-prompt-consolidation/README.md) — prior prompt consolidation workshop

## Scope

**In scope:**

- Code structure: module boundaries, layering, responsibility assignment
- The interface shapes between layers (what flows where)
- Where each current concern lands in the new structure
- Design constraints the structure must respect

**Out of scope:**

- Schema changes (the three-table append-only model is load-bearing)
- Gate definitions or review content quality
- CLI surface names or flags (those are stable contracts)
- Implementation timeline or migration sequencing

## Design constraints

1. **Append-only, auditable state.** The three-table schema (review_runs, gate_reviews, acceptance_events) and the current_gate_acceptances view stay. Any design must preserve total acceptance history.
2. **Notes and gates are markdown files.** The review system reads them; it never owns or mutates them.
3. **Git blob SHA is the provenance key.** Freshness is computed from SHAs, not timestamps.
4. **Model-partitioned acceptance.** Reviews for different models are independent.
5. **This is a fuzzy system.** LLM output is guided by templates but not rigidly constrained. If a review is lost to bad formatting, that's acceptable — the cost of forcing structured output (e.g. JSON) degrades LLM quality. The parser should be best-effort, not a strict contract.
6. **Reviews are expensive.** Every avoided re-run matters. Freshness logic must be exact.
7. **Two review shapes must coexist.** Bundle (many gates, one note) and gate-sweep (one gate, many notes) serve different use cases.
8. **Two runner modalities.** Subprocess and live-agent (prompt-file + ingest). Live-agent is the dominant path.
9. **CLI surface is stable.** Command names and flags are contracts used by agents.

## Working direction

Organize by **layer of concern** rather than by entry point. Every entry point does the same pipeline (target resolution, prompt construction, runner invocation, parsing, finalization) — differing only in batching shape and runner strategy.

Key hypotheses:

- A `ReviewPlan` value object can unify bundle and gate-sweep as two batching strategies over the same pipeline.
- A `Runner` protocol can cleanly abstract subprocess vs live-agent, with the live-agent path modeled as "run that suspends and resumes at ingest".
- Snapshot value objects (`NoteSnapshot`, `GateSnapshot`) eliminate the scattered `(sha, commit)` tuples.
- Finalization belongs in an orchestration layer, not the DB layer. DB becomes pure CRUD inside a transaction boundary the orchestrator opens.
- The protocol module (prompt + parser) is the sole owner of the LLM wire format. Parser is best-effort with fallback to `unknown` — not a strict validator.

## Files in this workshop

- [analysis.md](./analysis.md) — structural analysis of the current system (module-by-module, cross-cutting concerns)
- [target-structure.md](./target-structure.md) — proposed layer layout and design rationale
