# Monthly improvement triage — 2026-07-07

## Purpose

Sweep `kb/log.md` and `kb/reports/connect/*.connect.md` for improvement proposals from roughly the last month (window: 2026-06-06 through 2026-07-07) and separate low-hanging fruit from proposals with big potential but real cost. Closes when every item below is either done, explicitly dismissed, or moved into a more specific workshop.

## Method and scope

- `kb/log.md` (23 entries, all in scope — it's short enough to review whole rather than window it).
- Connect reports with mtime 2026-06-06 or later. Reports already covered by [`kb/work/connect-maintenance-observations/`](../connect-maintenance-observations/README.md) (window 2026-04-24–2026-06-23) were not re-triaged from scratch; only genuinely residual findings from full re-reads, or that workshop's still-open/partial/watch rows, are carried forward here.
- A quick mtime check of `kb/reference/proposals/` for anything freshly touched.

## Low-hanging fruit

- [ ] `kb/agentic-systems/COLLECTION.md` — authorize `kb/instructions/` as an outbound-link target (semantic-engine connect report hit a case where an external-system analysis maps onto a Commonplace procedure and had nowhere to link it).
- [ ] `kb/sources/in-toto-farm-to-table-guarantees.md` — run `cp-skill-ingest`; zero authored outbound surface, blocking pending `compares-with` edges.
- [ ] `kb/sources/prov-overview.md` — run `cp-skill-ingest`; fully orphaned snapshot.
- [ ] `kb/sources/skill-discovery-re-fires-in-every-sub-agent-context.md` — add `tags: [computational-model, architecture]` (currently `tags: []`, invisible to every tag-README by-tag sweep despite being a `structured-claim`).
- [ ] Same note — author the missing inverse `rationale` edge from `write-agent-memory-system-review/SKILL.md`'s delegating-mitigation section back to it (forward edge exists, backward doesn't).
- [ ] `kb/notes/agent-memory-README.md` — re-curate; it lists only `designing-agent-memory-systems.md` under "Notes" while more `agent-memory`-tagged notes exist (curation lag, flagged directly by connect).
- [ ] `kb/notes/artifact-analysis-README.md` — a `complete: true` tag-README is currently missing a note it claims to cover; this is a correctness bug in a validator-trusted mark, not just staleness. Also check inbound-link phrasing in `storing-llm-outputs-is-constraining.md`, `operational-signals-that-a-component-is-a-relaxing-candidate.md`, and `automating-kb-learning-is-an-open-problem.md` — all point at the revised `adaptation-agentic-ai-analysis` source with descriptions that undersell or mischaracterize its current content.
- [ ] `kb/sources/where-it-lives-retained-adaptation-2026-06-23.ingest.md` (or wherever its "next action" note lives) — drop the stale "write sovereignty synthesis" pointer; that synthesis already shipped as `the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`. Point there instead.
- [ ] Write a trivial drift check that the two tracked `AGENTS.md.template` copies are byte-identical — named in `kb/log.md` line 20 as "the trivial first case" of the frontload/compiled-view validator idea; doesn't require the full design to land this one check.
## Deprioritized

- `kb/reference/proposals/structured-output-codec-for-review-protocol.md` — not low-hanging fruit right now. Its Adoption criteria only need *a single medium the project actually uses* to expose schema output, and `kb/log.md` line 22 records a 2026-06-12 workflow-orchestrated run that did — but the project's actual review-execution focus is the live-agent file-artifact path, which has no schema-validated output surface today. Revisit only if/when the live-agent path grows an equivalent capability; until then this stays a documented option, not near-term work.

## Carried forward from connect-maintenance-observations (still open)

- Decide whether `context-engineering-README.md` needs `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` added, or whether the `kb-maintenance-README.md` listing is enough.
- Decide whether `adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` needs instruction-side `rationale` edges from `critique-note.md` / `REVIEW-SYSTEM.md` / `composition-friction-gate.md` — only if genuinely load-bearing.
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

## Notes for next pass

- `kb/work/log-triage-2026-04-27.md` overlaps this workshop on three items (two-axis taxonomy, OOD convergence, filesystem-native tool use) that it already marked `PROMOTE` and that are still unwritten. Worth deciding whether to fold that older triage file into this one or retire it once its remaining `KEEP`/`FOLD` rows are checked against current KB state.
- Reports with `Maintenance Observations: None` or only future-source-acquisition signals in this window (`mini-exercise-mismanaged-geniuses`, `skillrl-evolving-agents`, `artifacts-as-memory-beyond-agent-boundary`, `abstract-an-experience-only-when-you-can-state-the-boundary`, `verbalizable-representations-global-workspace-llms`, `palantir-ontology-vs-decision-traces`, `claude-obsidian-second-brain-guide`, `towards-automating-scientific-review-google-paper-assistant`, `dulleck-kerschbamer-doctors-mechanics-computer-specialists`, `build-systems-a-la-carte`) were left out of both buckets as not-yet-actionable.
