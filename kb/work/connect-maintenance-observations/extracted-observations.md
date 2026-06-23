# Extracted maintenance observations

Window: connect reports under `kb/reports/connect/` modified on or after 2026-04-24.

This is a normalized extraction of each non-empty `## Maintenance Observations` section. See the linked report for verbatim text and surrounding connection analysis.

## Agentic systems

### [claude-code-dynamic-workflows.connect.md](../../reports/connect/agentic-systems/claude-code-dynamic-workflows.connect.md)

- `kb/notes/COLLECTION.md` needed to authorize `agentic-systems` as a destination for notes-side `evidence`, `derived-from`, and `see-also` links. Existing notes already linked to `kb/agentic-systems/claude-code-dynamic-workflows.md`, but the notes collection table lagged the newer collection.

## Notes

### [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.connect.md](../../reports/connect/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.connect.md)

- The source note was tagged `kb-maintenance` and `context-engineering` but listed in neither tag README. The kb-maintenance Detection section was the natural home.
- The build-artifact instance had a strong note-to-ADR evidence edge, but adding it required editing the note's content, so connect did not author it.

### [adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.connect.md](../../reports/connect/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.connect.md)

- Review/critique instructions did not carry rationale edges back to the adversarial-loop note, even though the note names report-only critique, review gates, and the composition-friction gate as the forcing architecture.
- The note had no inbound links outside reports at the time.
- A composition-friction note appeared intended from status/review traces, but no such note file resolved in the working tree at report time.

### [design-for-the-first-time-human-except-on-access-cost.connect.md](../../reports/connect/notes/design-for-the-first-time-human-except-on-access-cost.connect.md)

- `document-system-README.md` and `context-engineering-README.md` did not list the source despite matching tags.
- The closing paragraph names two proxy-breaks, text-as-instruction and confabulation, but links only the first.

### [llm-generation-relaxes-goals-where-human-writing-stalls.connect.md](../../reports/connect/notes/llm-generation-relaxes-goals-where-human-writing-stalls.connect.md)

- `kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md` linked to missing `current-llm-inference-removes-composition-friction-filter-signal.md`; traversal suggested it should point at this successor note or another successor.
- `kb/notes/learning-theory-README.md` says every `learning-theory` note carries one listed child tag, but the source note had only `learning-theory`.

### [prose-has-no-dereference-reinforce-facts-at-point-of-use.connect.md](../../reports/connect/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.connect.md)

- The source and `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent` are close enough that future readers could mistake them for duplicates. The report recommended an `extends` edge plus a boundary phrase.

### [symbolic-context-engineering-is-bounded-by-symbol-availability.connect.md](../../reports/connect/notes/symbolic-context-engineering-is-bounded-by-symbol-availability.connect.md)

- The source had empty `tags: []`, blocking tag-index discovery.
- The Evidence section named four external systems without footer edges to their reviews despite notes collection authorization.

## Reference

### [mark-semantics.connect.md](../../reports/connect/reference/mark-semantics.connect.md)

- The general principle "a cache must never be the only copy" appeared in multiple places without one named home.

### [unify-review-bundling-around-note-gate-pairs.connect.md](../../reports/connect/reference/unify-review-bundling-around-note-gate-pairs.connect.md)

- The proposal inlined the many-small-checks / partial-failure-salvage argument and the share-note cost rationale instead of citing dedicated transferable notes.
- The single-artifact review-bundles evidence note and the proposal reasoned about share-note bundling economics from different angles; the report flagged this as a latent pairing if a cost-justification section were added.

## Sources

### [a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.connect.md](../../reports/connect/sources/a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.connect.md)

- No note names the three crisp failure modes: agentic laziness, self-preferential bias, and goal drift.
- The snapshot had no ingest companion at report time.
- The "quarantine" privilege-separation pattern had no note home.

### [adaptation-of-agentic-ai-survey-post-training-memory-skills.connect.md](../../reports/connect/sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.connect.md)

- `research/adaptation-agentic-ai-analysis.md` analyzed the exact paper but cited only the bare external arXiv URL, not the local snapshot or ingest.
- That research note had thin frontmatter and would not surface in description/tag scans.
- The agent-memory-requirements corroboration note and the research analysis note engage the same source from complementary angles.

### [agent-harness-large-language-model-agents-survey.connect.md](../../reports/connect/sources/agent-harness-large-language-model-agents-survey.connect.md)

- The KB now has several harness-taxonomy ingests plus runtime-decomposition notes; a later synthesis pass may need a curated index or stable taxonomy note.

### [beyond-not-novel-enough-llm-assisted-scholarly-critique.connect.md](../../reports/connect/sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.connect.md)

- The snapshot preserves prose, headings, references, limitations, and captions, but not table cell structure. Use original arXiv HTML/PDF for exact table values.

### [borretti-human-routers-of-machine-words.connect.md](../../reports/connect/sources/borretti-human-routers-of-machine-words.connect.md)

- The snapshot had no ingest companion at report time; ingest would create the authored outbound surface for reverse-edge candidates.

### [can-llm-agents-infer-world-models-agentic-automata-learning.connect.md](../../reports/connect/sources/can-llm-agents-infer-world-models-agentic-automata-learning.connect.md)

- Two-column PDF extraction was readable but imperfect, with figure captions and footnotes interleaved.

### [claude-code-dynamic-workflows-docs.connect.md](../../reports/connect/sources/claude-code-dynamic-workflows-docs.connect.md)

- The KB had two snapshots covering Claude Code dynamic workflows from different angles. A future ingest pass should cross-reference them with `compares-with`.

### [fernando-borretti-human-bottlenecks.connect.md](../../reports/connect/sources/fernando-borretti-human-bottlenecks.connect.md)

- The snapshot had no ingest companion at report time.
- Two Borretti snapshots had overlapping "human in the AI loop" arguments and no ingest companions; later triage should decide whether they share one synthesis note or two.

### [from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.connect.md](../../reports/connect/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.connect.md)

- The source names shared memory and collective privacy; the KB has no note on memory-sharing privacy.

### [how-to-build-your-own-agent-harness-2060069083878408689.connect.md](../../reports/connect/sources/how-to-build-your-own-agent-harness-2060069083878408689.connect.md)

- Several source-to-note relations needed a contrast/parallel-mechanism label that `kb/sources/COLLECTION.md` does not authorize.
- The KB lacks a note on component replaceability / independent versioning behind a uniform calling convention as a first-class harness property.
- The snapshot had no ingest report at report time.

### [large-language-model-agents-are-not-always-faithful-self-evolvers.connect.md](../../reports/connect/sources/large-language-model-agents-are-not-always-faithful-self-evolvers.connect.md)

- Three notes cited the source via arXiv v2 URLs rather than the local snapshot; the snapshot captured v3.
- The snapshot had no ingest companion at report time.

### [shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.connect.md](../../reports/connect/sources/shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.connect.md)

- Both Ukrainian original and English translation are present. Downstream ingest should target the English translation for corpus consistency while preserving the Ukrainian original as provenance.

### [the-log-is-the-agent-2065129901427130678.connect.md](../../reports/connect/sources/the-log-is-the-agent-2065129901427130678.connect.md)

- The snapshot had no ingest companion at report time.
- `scaling-managed-agents-decoupling-brain-from-hands.ingest.md` already encodes substantially the same architecture and links the same notes; a future ingest should cross-reference that report and distinguish sovereignty/lock-in.

### [the-y-combinator-for-llms-solving-long-context-rot.connect.md](../../reports/connect/sources/the-y-combinator-for-llms-solving-long-context-rot.connect.md)

- The snapshot contains raw `pdftotext -layout` artifacts and repeated title/author metadata. A cleaner PDF-to-markdown path is a tooling candidate if this recurs.

### [we-should-take-text-optimization-more-seriously-2064027464926716154.connect.md](../../reports/connect/sources/we-should-take-text-optimization-more-seriously-2064027464926716154.connect.md)

- The snapshot had no ingest surface at report time.
- "Update-time compute" is a named scaling axis the KB touches but does not name.
- The text-layer external-cognition lineage returned no note matches.
- The source overlaps strongly with the same author's Meta-Harness work; future Meta-Harness snapshots should be cross-referenced.

### [where-it-lives-is-not-what-it-is-architectural-vocabulary-retained-adaptation.connect.md](../../reports/connect/sources/where-it-lives-is-not-what-it-is-architectural-vocabulary-retained-adaptation.connect.md)

- The snapshot had no ingest companion at report time.
- The paper vocabulary overlaps the KB's four definition notes plus `axes-of-artifact-analysis.md`; the report treated this as a durable lineage gap.

## Sections With `None`

- [reasoning-production-is-not-reasoning-evaluation.connect.md](../../reports/connect/notes/reasoning-production-is-not-reasoning-evaluation.connect.md)
- [an-enigma-of-artificial-reason-production-evaluation-gap-lrms.connect.md](../../reports/connect/sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.connect.md)
- [building-a-good-vertical-agent-2065190286519906657.connect.md](../../reports/connect/sources/building-a-good-vertical-agent-2065190286519906657.connect.md)
- [claude-workstream-kit-fable-agent-scaffolding.connect.md](../../reports/connect/sources/claude-workstream-kit-fable-agent-scaffolding.connect.md)
- [emergent-analogical-reasoning-transformers.connect.md](../../reports/connect/sources/emergent-analogical-reasoning-transformers.connect.md)
- [gentle-coding.connect.md](../../reports/connect/sources/gentle-coding.connect.md)
- [interpolation-extrapolation-hyperpolation.connect.md](../../reports/connect/sources/interpolation-extrapolation-hyperpolation.connect.md)
- [no-free-lunch-theorem-no-universal-learning-algorithm.connect.md](../../reports/connect/sources/no-free-lunch-theorem-no-universal-learning-algorithm.connect.md)
- [problem-first-skill-inverts-solution-jumps-2063186118409929161.connect.md](../../reports/connect/sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.connect.md)
- [skillopt-executive-strategy-self-evolving-agent-skills.connect.md](../../reports/connect/sources/skillopt-executive-strategy-self-evolving-agent-skills.connect.md)
- [the-agent-loop-architecture-2067677007140278630.connect.md](../../reports/connect/sources/the-agent-loop-architecture-2067677007140278630.connect.md)

## Reports Without A Maintenance Section

- [stash.connect.md](../../reports/connect/agent-memory-systems/stash.connect.md)
- [designing-agent-memory-systems.connect.md](../../reports/connect/notes/designing-agent-memory-systems.connect.md)
- [agent-memory-coverage.connect.md](../../reports/connect/reference/agent-memory-coverage.connect.md)
- [agent-workflow-memory.connect.md](../../reports/connect/sources/agent-workflow-memory.connect.md)
- [context-providers-the-missing-layer-between-agents-and-tools-2048817143974613089.connect.md](../../reports/connect/sources/context-providers-the-missing-layer-between-agents-and-tools-2048817143974613089.connect.md)
- [giants-generative-insight-anticipation-scientific-literature.connect.md](../../reports/connect/sources/giants-generative-insight-anticipation-scientific-literature.connect.md)
- [huxley-godel-machine-human-level-coding-agent-development.connect.md](../../reports/connect/sources/huxley-godel-machine-human-level-coding-agent-development.connect.md)
- [on-learning-how-to-learn-learning-strategies.connect.md](../../reports/connect/sources/on-learning-how-to-learn-learning-strategies.connect.md)
- [the-self-healing-agent-harness-2048912026018484317.connect.md](../../reports/connect/sources/the-self-healing-agent-harness-2048912026018484317.connect.md)
- [what-is-an-agent-harness-2046980769747533830.connect.md](../../reports/connect/sources/what-is-an-agent-harness-2046980769747533830.connect.md)
