# Connect maintenance observation triage

## Purpose

Extract and triage the `## Maintenance Observations` sections from connect reports touched in the last 60 days.

Window: reports under `kb/reports/connect/` modified on or after 2026-04-24, checked on 2026-06-23.

Close this workshop when every `open` or `partial` row below is either promoted to a concrete maintenance edit/proposal/note, explicitly dismissed, or moved into a more specific workshop.

## Method

- Selected reports by filesystem mtime in the calendar window beginning 2026-04-24.
- Extracted text under `## Maintenance Observations` until the next `##` heading.
- Checked likely immediate implementations against the current worktree using targeted `rg`, file existence checks, and spot reads of affected artifacts.
- No library artifacts were changed during the initial extraction pass; this workshop is the triage surface.

## Scan Summary

- 47 recent connect reports scanned.
- 26 reports had non-empty maintenance observations.
- 11 reports had `Maintenance Observations: None`.
- 10 reports had no maintenance-observations section.

The extracted observations are in [extracted-observations.md](./extracted-observations.md).

## Status Legend

- `done` - observation is already reflected in the current worktree.
- `partial` - the obvious immediate implementation exists, but a residual action remains.
- `open` - still actionable.
- `watch` - useful signal, but no immediate edit is clearly warranted.
- `not-actionable` - capture/tooling limitation or future-only condition.

## Triage

| status | observation cluster | implementation check | next triage question |
|---|---|---|---|
| done | Notes collection contract did not authorize links to `kb/agentic-systems/`. | `kb/notes/COLLECTION.md` now includes `agentic-systems` under `evidence`, `derived-from`, and `see-also`. | None. |
| partial | `a-derived-copy-of-recomputable-truth...` was missing from tag READMEs and lacked the strongest system evidence edge. | It is now listed in `kb-maintenance-README.md`, and the note links `mark-semantics` plus ADR 027. It is still absent from the sparse `context-engineering-README.md`. | Decide whether context-engineering index membership is worth adding or whether kb-maintenance is enough. |
| partial | `adversarial-loop-can-reconstruct...` lacked inbound links and instruction-side rationale edges. | It now has an inbound note edge from `reasoning-production-is-not-reasoning-evaluation.md`; `composition-friction-gate.md` links to the related LLM-generation note, not to this one. | Add instruction-side `rationale` edges only if `critique-note.md`, `REVIEW-SYSTEM.md`, or `composition-friction-gate.md` genuinely rest on the adversarial-loop note. |
| open | `design-for-the-first-time-human...` missing from `document-system` and `context-engineering` curated heads; closing paragraph names two proxy breaks but links one. | It is still absent from both tag READMEs and still only links the text-as-instruction exception. | Add index entries and/or an edge for the confabulation proxy break if a target note exists. |
| done | `llm-generation-relaxes-goals...` had a stale proposal link and no child tag under `learning-theory`. | `automated-note-refinement-as-search-over-source-bundle.md` now links the successor note; the note has `tags: [learning-theory, llm-interpretation-errors]`. | None. |
| done | `prose-has-no-dereference...` needed disambiguation from `a-derived-copy...`. | The note now has an `exemplifies` link explaining the prose-regime boundary. | None unless a future reader still confuses the pair. |
| partial | `symbolic-context-engineering...` had empty tags and prose-named external systems without edges. | Tags are now non-empty (`context-engineering`, `agent-memory`), and footer evidence edges exist for the comparative review, EQUIPA, and Atomic. Some prose-named systems remain inline only. | Decide whether CrewAI, REM, cq, and Binder should get footer evidence edges or stay inline examples. |
| done | `mark-semantics` observed that "a cache must never be the only copy" lacked one named home. | `a-derived-copy-of-recomputable-truth...` now states that general form and links back to `mark-semantics`. | None. |
| partial | Review-bundling proposal lacked separate rationale notes for salvage and packing-axis insights. | ADR 029 now accepted the pair-protocol design and states salvage and packing-choice consequences. No separate transferable notes were written. | Decide whether ADR 029 is enough or whether the salvage/packing insights need standalone notes. |
| partial | Dynamic-workflows source lacked an ingest; the failure-mode triad and quarantine pattern had no note home. | `a-harness-for-every-task-dynamic-workflows.ingest.md` now exists and preserves those gaps as extractable values. | Decide whether to write notes for single-context failure modes and orchestration quarantine. |
| open | Adaptation survey research note used external-only citation and thin frontmatter. | The source ingest exists, but `kb/notes/research/adaptation-agentic-ai-analysis.md` still cites only arXiv and has no status/tags/traits. | Add local lineage link and normal note metadata, or convert/move the research note if it is intentionally outside the normal note contract. |
| watch | Harness-taxonomy sources may need a curated index or stable taxonomy note. | No dedicated harness taxonomy index/note was found beyond existing cluster notes and ingests. | Revisit after more harness sources accumulate or repeated connect reports keep rediscovering the cluster. |
| not-actionable | Scholarly-critique snapshot lacks precise table-cell structure. | Current snapshot is adequate for prose/caption capture; precise values require the source HTML/PDF. | Only improve snapshot tooling if this recurs. |
| done | `borretti-human-routers...` had no ingest companion. | `borretti-human-routers-of-machine-words.ingest.md` now exists. | Remaining synthesis belongs to Borretti-cluster note triage, not ingest creation. |
| not-actionable | PDF extraction artifacts in automata/world-model and long-context-rot snapshots. | These are capture-quality limitations, not graph-maintenance actions. | Track only if PDF capture quality becomes a recurring tooling issue. |
| partial | Claude dynamic-workflows docs and practitioner article should cross-reference. | The agentic-system analysis links both snapshots; the docs ingest names the paired source and future `compares-with` work. | Decide whether source-to-source `compares-with` belongs in a future synthesis note/ingest revision. |
| done | `fernando-borretti-human-bottlenecks` had no ingest companion. | `fernando-borretti-human-bottlenecks.ingest.md` now exists. | Remaining action is synthesis selection across the two Borretti ingests. |
| open | Memory-sharing privacy from the human-to-AI memory survey has no KB note. | Search found shared-memory mentions but no memory-sharing/privacy treatment. | Decide whether "collective privacy" is in scope for Commonplace or only source context. |
| partial | `how-to-build-your-own-agent-harness...` had no ingest and exposed a sources-label/theory gap. | The ingest exists and records component replaceability as extractable value. `kb/sources/COLLECTION.md` still has no `contrasts`/`parallels` source-to-note label. | Decide whether to add source-link label guidance and whether to write the component-replaceability note. |
| done | Faithful Self-Evolvers citations pointed at arXiv v2 instead of the local v3 snapshot/ingest. | The three note citations now point at the local snapshot/ingest paths. | None. |
| partial | `the-log-is-the-agent...` had no ingest and overlaps `scaling-managed-agents...`. | The ingest now exists. Near-duplicate/cross-reference handling still needs a targeted comparison pass. | Decide whether to cross-reference the two ingests and extract the sovereignty/lock-in distinction. |
| not-actionable | Long-context-rot PDF capture contains raw `pdftotext -layout` artifacts. | Snapshot is faithful enough; cleaner PDF-to-markdown is a tooling improvement only if repeated. | Track under snapshot tooling if it recurs. |
| partial | Text-optimization source had no ingest and surfaced "update-time compute" plus external-cognition lineage gaps. | `we-should-take-text-optimization-more-seriously.ingest.md` now exists and records both gaps. No `update-time compute` note/definition exists. | Decide whether `update-time compute` should become a definition/note. |
| partial | Where-it-lives source lacked ingest and appeared to need attribution edges from the vocabulary notes. | The ingest exists and corrects the direction: the paper was distilled from the notes, so note-to-paper `derived-from` is wrong. The sovereignty-risk axis remains open. | Write a sovereignty-risk synthesis only if it changes artifact-analysis practice. |

## Reports Without Actionable Maintenance Text

Reports with no `## Maintenance Observations` section: `stash`, `designing-agent-memory-systems`, `agent-memory-coverage`, `agent-workflow-memory`, `context-providers`, `giants`, `huxley`, `on-learning-how-to-learn`, `self-healing-agent-harness`, `what-is-an-agent-harness`.

Reports whose maintenance section was exactly `None`: `reasoning-production-is-not-reasoning-evaluation`, `an-enigma-of-artificial-reason`, `building-a-good-vertical-agent`, `claude-workstream-kit-fable-agent-scaffolding`, `emergent-analogical-reasoning`, `gentle-coding`, `interpolation-extrapolation-hyperpolation`, `no-free-lunch`, `problem-first-skill`, `skillopt`, `the-agent-loop-architecture`.
