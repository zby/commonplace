# kb/log.md triage — 2026-03-09

## Summary

- 16 entries reviewed
- 1 entry already resolved in the KB
- 15 entries still live, but they collapse into 5 backlog tasks rather than 15 unrelated fixes
- `kb/log.md` left unchanged; this report records disposition without rewriting the append-only capture log

## Disposition by entry

1. `kb/notes/related-systems/related-systems-index.md` — `re-scoped`
   - On review, Koylanai should not be promoted into `related-systems` from the current evidence base. We only know it through a thin article/post, so source-level ingest coverage is the right level for now.
   - Routed to: [`kb/tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md`](../tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md)

2. `kb/notes/related-systems/agent-skills-for-context-engineering.md` — `backlog`
   - The same-author relationship can still be captured, but only with provisional language. The implementation details of Personal Brain OS remain thin-source evidence.
   - Routed to: [`kb/tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md`](../tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md)

3. `kb/notes/llm-context-is-composed-without-scoping.md` — `backlog`
   - The note still lacks forking coverage. Koylanai may still be usable as a weak anecdotal example for module isolation, but it should not be treated as the strongest practitioner case from the current evidence base.
   - Routed to: [`kb/tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md`](../tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md)

4. `kb/notes/bounded-context-orchestration-model.md` — `blocked`
   - Spacebot exists as a source snapshot/ingest, but the note is still waiting on a proper related-system note before citing it as the production exemplar.
   - Routed to: [`kb/tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md`](../tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md)

5. `kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md` — `backlog`
   - The augmentation/automation threshold exists only as a short paragraph; there is still no dedicated note.
   - Routed to: [`kb/tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md`](../tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md)

6. `kb/notes/oracle-strength-spectrum.md` — `backlog`
   - The note still asks whether oracle strength predicts bitter-lessoning and still lacks the reach-based mechanism and MAKER hard-oracle success case.
   - Routed to: [`kb/tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md`](../tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md)

7. `kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md` — `resolved`
   - `kb/notes/quality-signals-for-kb-evaluation.md` now has a `## Credibility erosion` section, and the concept is also threaded into later notes.
   - No new task.

8. `kb/notes/methodology-enforcement-is-constraining.md` — `backlog`
   - The note cites ABC as formal grounding, but the missing structured-recovery layer is still not promoted into its own note.
   - Routed to: [`kb/tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md`](../tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md)

9. `kb/sources/agentic-code-reasoning.ingest.md` — `backlog`
   - The KB still lacks a note that cleanly separates process structure from output structure.
   - Routed to: [`kb/tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md`](../tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md)

10. `kb/notes/oracle-strength-spectrum.md` — `backlog`
    - The Table 4 task-suitability dataset is still only mentioned in source material, not used in the oracle-strength note.
    - Routed to: [`kb/tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md`](../tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md)

11. `kb/notes/distillation.md` — `backlog`
    - The note still describes extraction but not the return path from distillate back to the full solution.
    - Routed to: [`kb/tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md`](../tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md)

12. `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` — `backlog`
    - Shannon is cited in the ingest and connected from the source side, but the note’s own maturation path still does not use Shannon as explicit support.
    - Routed to: [`kb/tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md`](../tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md)

13. `kb/notes/structure-activates-higher-quality-training-distributions.md` — `partially-resolved`
    - Lampinen-backed content-bias evidence already appears in `human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md`, but this note still does not use that evidence directly.
    - Routed to: [`kb/tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md`](../tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md)

14. `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md` — `partially-resolved`
    - The source is now reflected in the human-writing/failure-mode note, but the stronger claim it should support remains live: content bias survives scaling and instruction tuning, so structured types are architectural rather than temporary.
    - Routed to: [`kb/tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md`](../tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md)

15. `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` — `backlog`
    - The decorrelation section still does not account for shared content bias as a source of correlated model error.
    - Routed to: [`kb/tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md`](../tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md)

16. `kb/notes/oracle-strength-spectrum.md` — `backlog`
    - Same cluster as entries 6 and 10; still one research pass, not three separate fixes.
    - Routed to: [`kb/tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md`](../tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md)

## Backlog clusters created

- [`kb/tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md`](../tasks/backlog/re-scope-koylanai-and-promote-spacebot-coverage.md)
- [`kb/tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md`](../tasks/backlog/extract-recovery-and-augmentation-threshold-notes.md)
- [`kb/tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md`](../tasks/backlog/strengthen-oracle-strength-with-reach-maker-and-task-suitability-data.md)
- [`kb/tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md`](../tasks/backlog/thread-process-structure-and-content-bias-into-structured-reasoning-notes.md)
- [`kb/tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md`](../tasks/backlog/integrate-shannon-operators-into-distillation-and-discovery-notes.md)
