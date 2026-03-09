# Improvement log

Append one line per observation. Don't fix anything — just record it.

Format: `- path/to/note.md: what needs improving`

- kb/notes/related-systems/related-systems-index.md: Koylanai Personal Brain OS has an ingest but no related-system review note, despite being one of the most connection-rich sources in the KB
- kb/notes/related-systems/agent-skills-for-context-engineering.md: does not mention that the same author built Personal Brain OS — the theory/implementation relationship between these two systems is uncaptured
- kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md: no practitioner evidence cited for the volume dimension; the Koylanai 40% token savings and voice guide degradation data points would strengthen the argument
- kb/notes/llm-context-is-composed-without-scoping.md: the "What exists today" section lists ad hoc scoping examples but none from practitioner knowledge systems; Personal Brain OS's 11-module isolation is the strongest practitioner case. Also: "sub-agents as scoping" covers only fresh-spawn isolation; forking (context-preserving isolation) is unaddressed
- kb/notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md: no production exemplars cited; Spacebot's cortex is the strongest case and should be referenced once the related-system note exists
- kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md: the augmentation/automation reliability threshold (from Rabanser Recommendation 4) deserves its own note rather than being buried in the predictability gap section
- kb/notes/operational-signals-that-a-component-is-a-softening-candidate.md: has no frontmatter (type, description, areas, status fields missing) — should be converted to a proper note with description as a retrieval filter
- kb/notes/oracle-strength-spectrum.md: open question "does oracle strength predict bitter-lessoning?" could be addressed by connecting to Deutsch's reach concept from first-principles-reasoning note — reach provides the theoretical mechanism. Also: missing the MAKER paper as a concrete success case in the hard-oracle regime
- kb/notes/bitter-lesson-boundary.md: Relevant Notes has only one entry; should reference oracle-strength-spectrum (refines the boundary into a gradient), crystallisation-and-softening (operationalizes the boundary), and voooooogel source (applied analysis for agent infrastructure)
- kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md: recommended next action (add credibility erosion section to quality-signals-for-kb-evaluation) has not been executed
- kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md: status is still seedling despite being listed in the learning-theory index and linked from multiple notes; the note is well-developed with examples and hierarchy
- kb/notes/files-not-database.md: cites Koylanai as independent validation but not Fintool, which is stronger evidence (commercial scale, paying users, S3+PostgreSQL derived-index pattern)
- kb/notes/bitter-lesson-boundary.md: Fintool's fiscal period normalization (10,000+ company calendars) is a concrete calculator-regime example worth adding; the "model eats scaffolding" thesis is a practitioner articulation of the softening prediction
- kb/notes/related-systems/related-systems-index.md: Fintool is not listed as a tracked system despite having an ingest report and strong architectural convergence with the filesystem-first pattern
- kb/notes/related_works/granular-software.md: has no frontmatter (type, description, status fields missing) — a text file that should be converted to a proper note
- kb/sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md: recommended next action (add "Grounding evidence" section to bitter-lesson-boundary citing kappa metric and destructive interference) has not been executed
- kb/notes/bitter-lesson-boundary.md: still has only one Relevant Notes entry despite being a core note linked by 5+ other notes; the induction-bias paper's kappa results are the strongest quantitative evidence for the calculator regime and should be cited
- kb/notes/oracle-strength-spectrum.md: status is seedling but the note is well-developed with a full manufacture/amplify/monitor pipeline; should be promoted to current or near-current
- kb/notes/operational-signals-that-a-component-is-a-softening-candidate.md: areas field is empty — should be [learning-theory]; note is not listed in learning-theory index despite belonging in the Stabilisation section
- kb/notes/operational-signals-that-a-component-is-a-softening-candidate.md: index.md entry (line 106) has no description suffix, unlike most other entries — may need index regeneration
- kb/notes/research/adaptation-agentic-ai-analysis.md: description is generic ("Analysis of agentic AI adaptation paper and llm-do implications") — should be a retrieval-quality filter describing the softening/stabilizing signals catalogue and llm-do mapping
- kb/notes/research/adaptation-agentic-ai-analysis.md: Relevant Notes section has only one entry (stabilisation.md) despite connecting to bitter-lesson-boundary, softening-signals, and unified-calling-conventions
- kb/notes/methodology-enforcement-is-stabilisation.md: the enforcement gradient lacks a concept of structured recovery (what to do after a soft violation is detected); ABC's recovery mechanisms (typed corrective actions with fallback chains) fill this gap
- kb/sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md: only referenced by legal-drafting note and sources/index.md despite ingest identifying 7 strong connections to KB notes; most connections are unidirectional from ingest outward
- kb/notes/spec-mining-as-crystallisation.md: Relevant Notes section has only one entry (legal-drafting) despite the note body linking to 6+ other notes; the section is incomplete
