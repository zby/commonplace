# Monthly improvement triage — 2026-07-07

## Purpose

Sweep `kb/log.md` and `kb/reports/connect/*.connect.md` for improvement proposals from roughly the last month (window: 2026-06-06 through 2026-07-07) and separate low-hanging fruit from proposals with big potential but real cost. Closes when every item below is either done, explicitly dismissed, or moved into a more specific workshop.

## Method and scope

- `kb/log.md` (23 entries, all in scope — it's short enough to review whole rather than window it).
- Connect reports with mtime 2026-06-06 or later. Reports already covered by [`kb/work/connect-maintenance-observations/`](../connect-maintenance-observations/README.md) (window 2026-04-24–2026-06-23) were not re-triaged from scratch; only genuinely residual findings from full re-reads, or that workshop's still-open/partial/watch rows, are carried forward here.
- A quick mtime check of `kb/reference/proposals/` for anything freshly touched.

## Low-hanging fruit

- [x] `kb/agentic-systems/COLLECTION.md` — authorized `kb/instructions/` as an outbound-link target for procedure links from external-system analyses.
- [x] `kb/sources/in-toto-farm-to-table-guarantees.md` — ingest already existed; authored the ingest's recommended `evidence` reverse edge from `the-boundary-of-automation-is-the-boundary-of-verification.md`.
- [x] `kb/sources/prov-overview.md` — ingest already existed; authored the ingest's recommended `evidence` reverse edge from `definitions/lineage.md`.
- [x] `kb/notes/skill-discovery-re-fires-in-every-sub-agent-context.md` — added `tags: [computational-model, architecture]`.
- [x] Same note — authored the inverse `rationale` edge from `write-agent-memory-system-review/SKILL.md`'s delegating-mitigation section back to it.
- [x] `kb/notes/agent-memory-README.md` — re-curated the selective tag head so it covers the core frame, requirements map, failure boundaries, and external checks rather than only `designing-agent-memory-systems.md`.
- [x] `kb/notes/artifact-analysis-README.md` — the `complete: true` gap did not reproduce in this checkout (19 tagged notes, no missing links found); fixed the stale inbound-link phrasing in `storing-llm-outputs-is-constraining.md`, `operational-signals-that-a-component-is-a-relaxing-candidate.md`, and `automating-kb-learning-is-an-open-problem.md`.
- [x] `kb/sources/where-it-lives-retained-adaptation-2026-06-23.ingest.md` — already corrected before this pass: the stale sovereignty follow-up now points at `the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`.
- [x] Dismissed: the proposed drift check for two tracked `AGENTS.md.template` copies no longer matches the repository. There is one tracked source template; the package copy is produced by the `pyproject.toml` wheel `force-include` mapping.
- [ ] `kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md` — add SuperARC's print-statement example (flagged `FOLD` in the now-folded-in `log-triage-2026-04-27.md`; never landed, note currently has no SuperARC mention at all).

## Deprioritized

- `kb/reference/proposals/structured-output-codec-for-review-protocol.md` — not low-hanging fruit right now. Its Adoption criteria only need *a single medium the project actually uses* to expose schema output, and `kb/log.md` line 22 records a 2026-06-12 workflow-orchestrated run that did — but the project's actual review-execution focus is the live-agent file-artifact path, which has no schema-validated output surface today. Revisit only if/when the live-agent path grows an equivalent capability; until then this stays a documented option, not near-term work.

## Carried forward from connect-maintenance-observations (still open)

- Decide whether `context-engineering-README.md` needs `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` added, or whether the `kb-maintenance-README.md` listing is enough.
- Done: `adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` now has `rationale` edges from `critique-note.md` (previously ungrounded) and `composition-friction-gate.md` (added as a second edge alongside its existing one to the stall note, since it backs a distinct design point — no-verdict, routed-attention). `README-REVIEW-SYSTEM.md` was excluded: it's purely mechanics prose (freshness, acceptance rows, batch workflow) and doesn't argue the why an edge would need to rest on.
- Decide whether CrewAI / REM / cq / Binder in `symbolic-context-engineering...` should get footer evidence edges or stay inline-only.
- Decide whether ADR 029 alone suffices for the review-bundling salvage/packing insights, or whether standalone notes are warranted.
- Decide whether to write notes for the dynamic-workflows single-context failure-mode triad and the orchestration-quarantine pattern.
- **Open:** memory-sharing / "collective privacy" from the human-to-AI memory survey has no KB note — needs a scope decision (in scope for Commonplace, or source-only context).
- **Watch, rising:** harness-taxonomy sources have no dedicated index/note. Pressure is increasing — this period's `semantic-engine`, `claude-code-dynamic-workflows`, and `the-agent-loop-architecture` connect reports all add harness-taxonomy material on top of the prior batch.

## Big-potential / high-effort

- **Derived-assertions-over-recomputable-ground-truth theory** (`kb/log.md` lines 18, 20). Four-plus instances now on record (mark-semantics, stale-indexes note, the unenforced `status:` field, ADR 025, plus the frontloading/compiled-view cluster). This is the strongest promotion candidate in the log — the evidence bar the log itself set ("needs more instances before naming") looks met.
- **Two-axis agent-memory taxonomy** (content-type × hierarchy-level, `kb/log.md` line 10). Two independent decompositions (cognitive-science and computer-architecture framings) already converge on the same joint structure. Note this was *also* flagged `PROMOTE` in `kb/work/log-triage-2026-04-27.md` and still hasn't been written — over two months of recurrence without action.
- **Four-source OOD-failure convergence** (SuperARC, esolang-bench, pathway-sudoku, Ebrahimi induction-bias; `kb/log.md` line 11). Same story: also flagged `PROMOTE` in the April triage, still open. SuperARC's AIT-grounded methodology anchors it as the strongest of the four.
- **Ephemeral-helper-script substrate** (`kb/log.md` line 19). Real design gap: agents write and discard throwaway stdlib scripts that are exactly the spec-mining input the KB's own theory says should accumulate. Needs actual design decisions (location, committed vs gitignored, lifecycle/expiry, promotion signal) before it's adoptable — bigger than a note, more like a small ADR.
- **`kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md`** — not a triage candidate itself (already a finished design proposal), but it's the most recently touched file in the whole survey (edited 2026-07-04 and 2026-07-06) and worth surfacing: it generalizes the type-conformance-pairs pattern (ADR 038) to COLLECTION.md-as-gate and source-as-gate dependencies.
- **Harness-orchestrated-review engineering gaps** (`kb/log.md` line 22, FIX entry). Workflow `args` not reaching scripts (workaround exists), no shell in the script sandbox (forces deterministic sweeps into the parent conversation), no per-run token telemetry, and an unverified model-partition assertion. Each is a real fix, bigger than one sitting; the first end-to-end harness-orchestrated review run already validated the design direction.
- **Externalization-as-cognitive-burden-relocation reframe** (`kb/log.md` line 14). Cross-cutting frame touching 4+ existing notes. High conceptual leverage if it holds — needs careful checking that it's a genuine mechanism and not just relabeling existing notes.
- **Filesystem-native tool use as a distinct long-context strategy** (`kb/log.md` line 12). Four existing notes (`context-efficiency-is-the-central-design-concern-in-agent-systems.md`, `tool-loop-index.md`, `process-structure-and-output-structure-are-independent-levers.md`, the agentic-memory comparative review) already share this unnamed claim. Also flagged `PROMOTE` in the now-folded-in `log-triage-2026-04-27.md` and still unwritten — same over-two-months-unaddressed pattern as the two items above.

## Carried forward from log-triage-2026-04-27 (folded in, then deleted, 2026-07-07)

That file's 12 open "Live Queue" items were checked against current KB state. 8 were already resolved (verification-as-decomposition-constraint folded into `decomposition-heuristics-for-bounded-context-scheduling.md`; the indiscriminate-loading double failure covered across `knowledge-storage-does-not-imply-contextual-activation.md` and the soft-degradation note; quantitative grounding moved to body prose in `fixed-artifacts-split-into-exact-specs-and-proxy-theories.md`; the SuperARC integer-vs-binary example added to `first-principles-reasoning-selects-for-explanatory-reach-over.md`; diagnostic richness promoted to its own note, `diagnostic-richness-constrains-outer-loop-learning-quality.md`; Meta-Harness comprehension added to `evaluation-automation-is-phase-gated-by-comprehension.md`; Tracecraft added as a worked example to `agent-orchestration-needs-coordination-guarantees-not-just.md`; decomposition-policy acquisition added to `agent-orchestration-occupies-a-multi-dimensional-design-space.md`). Two more (two-axis taxonomy, OOD convergence) were already tracked above under Big-potential, and filesystem-native tool use was just added there too. The 2 remaining:

- Control-plane abstractions across repository/prompt/learning-architecture levels — `kb/log.md` line 9 is worded identically to the April item; transfer conditions between levels still unnamed. `KEEP` — no action yet, watch for concrete transfer-failure predictions.
- Codification lifecycle (when/what/how to commit) as a unifying note — partially distributed across `progressive-constraining-commits-only-after-patterns-stabilize.md` (when) and `codify-versus-llm-decision-heuristics.md` (what), but nothing unifies them as a staged lifecycle. Low-priority `KEEP`; April's assessment ("reads like a phase grouping more than a mechanism") still holds.

## Notes for next pass

- Reports with `Maintenance Observations: None` or only future-source-acquisition signals in this window (`mini-exercise-mismanaged-geniuses`, `skillrl-evolving-agents`, `artifacts-as-memory-beyond-agent-boundary`, `abstract-an-experience-only-when-you-can-state-the-boundary`, `verbalizable-representations-global-workspace-llms`, `palantir-ontology-vs-decision-traces`, `claude-obsidian-second-brain-guide`, `towards-automating-scientific-review-google-paper-assistant`, `dulleck-kerschbamer-doctors-mechanics-computer-specialists`, `build-systems-a-la-carte`) were left out of both buckets as not-yet-actionable.
