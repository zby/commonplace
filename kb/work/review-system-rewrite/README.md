# Workshop: review-system-rewrite

## Question

If we could afford a full rewrite of the review system code, what structure would best serve its goals given its real constraints?

## Why this workshop exists

The review system has grown organically through ~10 workshops and migrations. It works, but the code structure has accumulated tangles:

- Parsing logic spread across three modules (run_review_bundle, gate_sweep_format, review_decisions).
- `review_db.py` (910 lines) mixes SQL with finalization orchestration, coverage validation, and auto-acceptance rules.
- Bundle and gate-sweep are two near-duplicate pipelines that differ only in batching shape.
- Runner output handling is coupled to orchestration; subprocess and live-agent paths need a shared result contract, but not necessarily a large runner subsystem.
- Provenance flows as bare `(sha, commit)` tuples through five modules.
- Freshness logic is duplicated between review_target_selector and warn_selector.
- CLI review_sweep.py has business logic that should live in the library.
- After the base code-structure rewrite, review-specific relocation behavior now lives downstream in `commonplace.review.relocation_hook` and plugs into `commonplace.lib.relocation` through a hook protocol. This is the right dependency direction and should be preserved by any review-system rewrite.

This workshop designs the target architecture. Not a plan to execute now — a reference point for incremental refactoring and for evaluating whether future changes move toward or away from the ideal structure.

## Current grounding

- [review-architecture.md](../../reference/review-architecture.md) — code architecture overview
- [REVIEW-SYSTEM.md](../../reference/REVIEW-SYSTEM.md) — workflow contract
- [review-run-lifecycle](../review-run-lifecycle/README.md) — prior lifecycle tightening workshop
- [review-prompt-consolidation](../review-prompt-consolidation/README.md) — prior prompt consolidation workshop
- base-system code-structure rewrite — introduced `RelocationHook` and moved review export/DB rekey behavior into `commonplace.review.relocation_hook`

## Scope

**In scope:**

- Code structure: module boundaries, layering, responsibility assignment
- The interface shapes between layers (what flows where)
- Where each current concern lands in the new structure
- Design constraints the structure must respect
- Review-owned integration points with non-review core, especially relocation hooks

**Out of scope:**

- Schema changes (the four-table execution/review model is load-bearing)
- Gate definitions or review content quality
- CLI surface names or flags (those are stable contracts)
- Implementation timeline or migration sequencing

## Design constraints

1. **Append-only, auditable state.** The four-table schema (`review_runs`, `review_run_gates`, `gate_reviews`, `acceptance_events`) and the `current_gate_acceptances` view stay. Acceptance history remains append-only, and selector freshness remains driven by current acceptance state.
2. **Notes and gates are markdown files.** The review system reads them; it never owns or mutates them.
3. **Git blob SHA is the provenance key.** Freshness is computed from SHAs, not timestamps.
4. **Model-partitioned acceptance.** Reviews for different models are independent.
5. **This is a fuzzy system.** LLM output is guided by templates but not rigidly constrained. If a review is lost to bad formatting, that's acceptable — the cost of forcing structured output (e.g. JSON) degrades LLM quality. The parser should be best-effort, not a strict contract.
6. **Reviews are expensive.** Every avoided re-run matters. Freshness logic must be exact.
7. **Two review shapes must coexist.** Bundle (many gates, one note) and gate-sweep (one gate, many notes) serve different use cases.
8. **Two runner modalities.** Subprocess and live-agent (prompt-file + ingest). Live-agent is the dominant path.
9. **CLI surface is stable.** Command names and flags are contracts used by agents.
10. **Review remains downstream of core.** `commonplace.lib` must not import `commonplace.review`. Core operations such as relocation expose protocols; review code implements those protocols and the CLI composes them.

## Working direction

Organize by **layer of concern** rather than by entry point. Every entry point does the same pipeline (target resolution, prompt construction, runner invocation, parsing, finalization) — differing mostly in batching shape and execution modality.

Key hypotheses:

- A `ReviewPlan` value object can unify bundle and gate-sweep as two batching strategies over the same pipeline.
- A narrow runner result contract can keep orchestration independent of subprocess details; the live-agent path is better modeled as "prompt now, resume parse/finalize at ingest" than as a separate review pipeline.
- Snapshot value objects (`NoteSnapshot`, `GateSnapshot`) eliminate the scattered `(sha, commit)` tuples.
- Finalization belongs in an orchestration layer, not the DB layer. DB becomes pure CRUD inside a transaction boundary the orchestrator opens.
- The protocol module (prompt + parser) is the sole owner of the LLM wire format. Parser is best-effort with fallback to `unknown` — not a strict validator.
- Review-owned hooks are adapters around core workflows, not exceptions to the layering. The relocation hook should remain a review integration module with a small core-facing protocol surface.

## Files in this workshop

- [analysis.md](./analysis.md) — structural analysis of the current system (module-by-module, cross-cutting concerns)
- [target-structure.md](./target-structure.md) — proposed layer layout and design rationale
- [plan.md](./plan.md) — implementation sequencing for small, reversible refactoring slices
