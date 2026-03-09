# Improvement log

Append one line per observation. Don't fix anything — just record it.

Format: `- path/to/note.md: what needs improving`

- kb/notes/related-systems/related-systems-index.md: Koylanai Personal Brain OS has an ingest but no related-system review note, despite being one of the most connection-rich sources in the KB
- kb/notes/related-systems/agent-skills-for-context-engineering.md: does not mention that the same author built Personal Brain OS — the theory/implementation relationship between these two systems is uncaptured
- kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md: no practitioner evidence cited for the volume dimension; the Koylanai 40% token savings and voice guide degradation data points would strengthen the argument
- kb/notes/llm-context-is-composed-without-scoping.md: the "What exists today" section lists ad hoc scoping examples but none from practitioner knowledge systems; Personal Brain OS's 11-module isolation is the strongest practitioner case
- kb/notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md: no production exemplars cited; Spacebot's cortex is the strongest case and should be referenced once the related-system note exists
- kb/sources/agentic-memory-systems-comparative-review.md: has no frontmatter — a text file that could benefit from /convert to add type and description
- kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md: the augmentation/automation reliability threshold (from Rabanser Recommendation 4) deserves its own note rather than being buried in the predictability gap section
- kb/notes/softening-signals.md: has no frontmatter (type, description, areas, status fields missing) — should be converted to a proper note with description as a retrieval filter
- kb/notes/spec-mining-as-crystallisation.md: has no frontmatter — should have type, description, and areas fields added
- kb/notes/oracle-strength-spectrum.md: open question "does oracle strength predict bitter-lessoning?" could be addressed by connecting to Deutsch's reach concept from first-principles-reasoning note — reach provides the theoretical mechanism
- kb/notes/softening-signals.md: should cross-reference spec-mining-as-crystallisation — together they describe both operational directions of the crystallise/soften boundary but neither mentions the other
- kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md: Relevant Notes section has only two entries (crystallisation, deploy-time-learning) — thin for a note that connects to spec mining, oracle hardening, and the methodology enforcement gradient
- kb/notes/methodology-enforcement-is-stabilisation.md: the "crystallisation trigger" description is operationally identical to spec mining but doesn't link to spec-mining-as-crystallisation — the maturation trajectory IS spec mining applied to methodology
- kb/notes/oracle-strength-spectrum.md: missing the MAKER paper as a concrete success case in the hard-oracle regime — the ingest file recommended adding a section on architectural error correction and oracle strength, but this has not been done
- kb/notes/bitter-lesson-boundary.md: the Relevant Notes section has only one entry (memory-management-policy); a note about the boundary between calculators and vision features should reference more empirical examples — MAKER is the strongest available
- kb/sources/meyerson-maker-million-step-llm-zero-errors.ingest.md: recommended next action (update oracle-strength-spectrum) has not been executed
- kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md: recommended next action (add credibility erosion section to quality-signals-for-kb-evaluation) has not been executed
- kb/notes/agents-navigate-by-deciding-what-to-read-next.md: missing reference to Notes Without Reasons source as the negative case for what happens when pointers lack context — identified in the ingest report but not added
- kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md: Relevant Notes section still has only two entries despite connecting to many more concepts (noted previously, now additionally missing link to Notes Without Reasons source for "you cannot reason about reasoning you cannot inspect")
- kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md: has no frontmatter — a synthesis report that could benefit from type, description, and areas fields for discoverability
- kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md: uses Toulmin as its primary running example but does not link to the Toulmin source (kb/sources/purdue-owl-toulmin-argument.md) — the formal framework behind the illustration is uncited
- kb/notes/writing-styles-are-strategies-for-managing-underspecification.md: uses the term "warrant" from Toulmin (in the explanatory style description) without linking to the Toulmin source that defines it
- kb/notes/title-as-claim-enables-traversal-as-reasoning.md: status is still seedling despite being a foundational note linked from multiple indexes and many other notes
- kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-learning-operations.md: has no frontmatter — its accretion-vs-curation framing is valuable but trapped in a source report without type/description
- kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md: status is still seedling despite being listed in the learning-theory index and linked from multiple notes; the note is well-developed with examples and hierarchy
- kb/notes/llm-context-is-composed-without-scoping.md: the "sub-agents as scoping" section covers only fresh-spawn isolation; forking (context-preserving isolation, a distinct primitive) is unaddressed despite being a natural extension of the scoping model
- kb/notes/bitter-lesson-boundary.md: Relevant Notes still has only one entry; the voooooogel source is a direct applied analysis of the boundary for agent infrastructure that could be referenced
