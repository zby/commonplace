# Investigation: harness-taxonomy sources need a dedicated index/note

## Item under test

From `kb/work/connect-maintenance-observations/README.md`:

> watch | Harness-taxonomy sources may need a curated index or stable taxonomy note. | No dedicated harness taxonomy index/note was found beyond existing cluster notes and ingests. | Revisit after more harness sources accumulate or repeated connect reports keep rediscovering the cluster.

Escalated in `kb/work/monthly-improvement-triage/README.md` to "Watch, rising":

> harness-taxonomy sources have no dedicated index/note. Pressure is increasing — this period's `semantic-engine`, `claude-code-dynamic-workflows`, and `the-agent-loop-architecture` connect reports all add harness-taxonomy material on top of the prior batch.

## First finding: an active workshop already existed for this exact question

Per the assignment's pointer, `kb/work/harness-taxonomy-convergence/` existed before I started (listed in `kb/work/README.md`, described there as "mapping five independent harness decompositions into one table; uncovered a structure × governance two-axis split"). I read it in full rather than starting a competing investigation. It contained:

- `README.md` — five sources (Vtrivedy10's "Anatomy of an Agent Harness," Raschka's "Components of a Coding Agent," commonplace itself, Lopopolo's "Harness Engineering" report, and the harness-engineering-as-cybernetics thread), split into two kinds: **component decompositions** (Vtrivedy10, Raschka, commonplace) and **operational/control vocabularies** (Lopopolo, cybernetics). It builds a structural convergence table and a governance table, and concludes the real finding is a **two-axis split**: runtime structure (scheduler / context engine / execution substrate) is a separate axis from runtime governance (inform / validate / correct / detect drift), and governance is not a fourth structural component but a supervisory function cutting across the other three.
- `runtime-structure-determines-governance-control-surfaces.md` — a fully-frontmattered `note`-typed draft (status: `seedling`) making the two-axis argument, already carrying a "Relevant Notes" footer linking into four existing KB notes.
- `structure-governance-matrix.md` — a companion table operationalizing the claim for commonplace itself.

**Git history shows the workshop was created and fully drafted in one day (2026-04-06) and never touched again.** In the same day's commits, the workshop's *other* outcome path — folding the three-way structural convergence table (Vtrivedy10 + Raschka + commonplace) into the existing `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` — was also executed (commit `3df7c0a5`, "Add Raschka source to runtimes-decompose... notes"; that note's "Why independent sources converge here" section already cites all four sources: Vtrivedy10, Raschka, Lopopolo, cybernetics). So half of the workshop's stated closing plan was already done. What was left undone was promoting the **stronger claim** — the structure × governance two-axis argument — out of the workshop and into `kb/notes/`. The workshop was simply never closed out; it sat as a finished-but-unpromoted draft for three months while `kb/work/README.md` kept listing it as "active."

The three-month gap between the workshop's 2026-04-06 draft and the 2026-06-23/2026-07-07 triage flags means the "watch, rising" framing is really describing new connect-report noise arriving *after* the workshop had already stalled, not new pressure the workshop failed to anticipate.

## Checking whether the three "rising pressure" sources actually add new harness-taxonomy material

I read `kb/agentic-systems/semantic-engine.md`, `kb/agentic-systems/claude-code-dynamic-workflows.md`, and `kb/sources/the-agent-loop-architecture-2067677007140278630.ingest.md` plus their connect reports (`kb/reports/connect/agentic-systems/semantic-engine.connect.md`, `kb/reports/connect/agentic-systems/claude-code-dynamic-workflows.connect.md`, `kb/reports/connect/sources/the-agent-loop-architecture-2067677007140278630.connect.md`) to check whether they genuinely feed the scheduler/context-engine/substrate (or structure/governance) taxonomy question, or whether the triage note over-read them as a cluster.

- **`semantic-engine`** — its own analysis states plainly it "is not an agentic runtime and not an agent-memory system. It has no agent loop, scheduling surface, tool-use orchestration..." Its connect report routes it toward ingest/storage-substrate notes (`files-not-database`, `distilled-artifacts-need-source-tracking`, CocoIndex), not toward the runtime-decomposition cluster at all. It does not add harness-taxonomy pressure; the triage note's inclusion of it in the "rising pressure" list appears to be an over-broad read of "harness-adjacent" as "harness-taxonomy."
- **`claude-code-dynamic-workflows`** — genuinely about a shipped harness feature, but its connect report explicitly rejects wiring it to `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`: "the source already frames itself through the bounded-context orchestration model, not the scheduler/context-engine/execution taxonomy; linking both would blur which lens the analysis uses." It's deliberately and correctly homed in the separate tool-loop/orchestration-model cluster (`computational-model-README.md`'s "Scheduling & Orchestration" section already lists it). It doesn't add unincorporated pressure to this taxonomy.
- **`the-agent-loop-architecture`** — this is the one genuine new data point. Its ingest and connect report independently decompose production agent loops into loop/skill/orchestrator, and the connect report explicitly calls this out as evidence for `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`: "the source independently decomposes production agent loops into loop, skill, and orchestrator; this maps mostly to scheduler plus execution substrate and adds a durable-execution emphasis not foregrounded in the existing runtime taxonomy." This is a real sixth (or fourth-independent, depending on how commonplace is weighted) convergence point that is not yet folded into either the existing note or the now-promoted two-axis note.

So of the three sources named as "rising pressure," only one actually contributes new convergence evidence, and the gap it represents is a small, well-scoped edit (cite one more corroborating source) rather than a missing index or taxonomy.

## Verdict: DEFER-TO-EXISTING-WORKSHOP (workshop finalized/promoted, not duplicated)

The workshop had already answered the substantive question the triage item is asking — the accumulated harness sources do converge on a stable, two-axis structure (runtime structure vs. runtime governance), on top of an already-folded three-way structural convergence (Vtrivedy10, Raschka, commonplace) in the pre-existing `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` note. The workshop's draft note was one promotion step away from being the dedicated note this triage item calls for. Writing a competing note from scratch would have duplicated that work and ignored a more defensible, already-reasoned two-axis framing.

## Action taken

Promoted rather than duplicated:

1. Merged the workshop's two draft artifacts (`runtime-structure-determines-governance-control-surfaces.md` theory note + `structure-governance-matrix.md` companion table) into a single note at `kb/notes/runtime-structure-determines-governance-control-surfaces.md`. Fixed a stale link (`inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md` → the actual current filename `inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`, renamed in commit `d605d894` after the workshop draft was written) and rewrote cross-workshop relative paths (`../../notes/...`) as in-collection paths (`./...`). Kept `status: seedling` — this promotion closes the workshop and clears the "no dedicated note" watch item, but does not itself constitute a full semantic-review acceptance pass, so seedling is the honest status.
2. Ran `commonplace-validate` on the new note: PASS (clean) — no WARN/FAIL/INFO.
3. Ran the compression-bundle review gate via a fresh, blind sub-agent per `kb/work/agent-note-improvement/run-compression-bundle-on-note.md`; report saved to `harness-taxonomy-index-gap-compression-review.md` in this directory. Overall result: **WARN**. The reviewer independently confirmed the "stapled together" risk the merge invited: the theory sections passed cleanly, but the merged matrix section's four closing "general pattern" bullets introduced unsupported side-claims (one self-contradictory about its own generality), and the table cells carried reference-register implementation detail disproportionate to a theory note. Applied all four suggested fixes directly: folded a corrected, properly-generalized version of the drift-detection observation into the existing "Execution substrate" theory paragraph; trimmed table cells to short labels; deleted all four closing bullets; tightened the scheduler-row explanation to tie back explicitly to the note's own claim. Re-ran `commonplace-validate`: PASS (clean).
4. Deleted `kb/work/harness-taxonomy-convergence/` (all three files) — the workshop's value is now fully consumed into the library note, per the workshop-layer convention that a finished workshop is deleted rather than left as a stale pointer.
5. Removed the `harness-taxonomy-convergence` line from `kb/work/README.md`'s Active Workshops list (that file is not one of the two protected coordinator-owned READMEs named in my assignment).

## Residual, non-blocking follow-up

`the-agent-loop-architecture`'s independent loop/skill/orchestrator decomposition (see above) is not yet cited in either `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` or the newly-promoted note. This is a minor, well-scoped edit (add one more corroborating source to the existing "Why independent sources converge here" section), not a missing-index problem. Leaving it for a future connect/maintenance pass rather than doing it here, since it's an edit to an already-accepted note outside this triage item's narrow scope (a missing dedicated note/index, which is now resolved), and it doesn't change the note's core argument.

## Disposition

No new competing note written. One existing stale workshop promoted and closed. Files touched: `kb/notes/runtime-structure-determines-governance-control-surfaces.md` (new), `kb/work/harness-taxonomy-convergence/` (deleted), `kb/work/README.md` (one-line removal).
