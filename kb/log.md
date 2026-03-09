# Improvement log

Append one line per observation. Don't fix anything — just record it.

Format: `- path/to/note.md: what needs improving`

- kb/notes/related-systems/related-systems-index.md: Koylanai Personal Brain OS has an ingest but no related-system review note, despite being one of the most connection-rich sources in the KB
- kb/notes/related-systems/agent-skills-for-context-engineering.md: does not mention that the same author built Personal Brain OS — the theory/implementation relationship between these two systems is uncaptured
- kb/notes/llm-context-is-composed-without-scoping.md: the "What exists today" section lists ad hoc scoping examples but none from practitioner knowledge systems; Personal Brain OS's 11-module isolation is the strongest practitioner case. Also: "sub-agents as scoping" covers only fresh-spawn isolation; forking (context-preserving isolation) is unaddressed
- kb/notes/bounded-context-orchestration-model.md: ConvexBench and MAKER added as academic exemplars; Spacebot's cortex remains the strongest production case and should be referenced once the related-system note exists
- kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md: the augmentation/automation reliability threshold (from Rabanser Recommendation 4) deserves its own note rather than being buried in the predictability gap section
- kb/notes/oracle-strength-spectrum.md: open question "does oracle strength predict bitter-lessoning?" could be addressed by connecting to Deutsch's reach concept from first-principles-reasoning note — reach provides the theoretical mechanism. Also: missing the MAKER paper as a concrete success case in the hard-oracle regime
- kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md: recommended next action (add credibility erosion section to quality-signals-for-kb-evaluation) has not been executed
- kb/notes/related_works/: legacy directory with underscore naming; remaining files need triage (convert to related-systems/ or delete)
- kb/notes/methodology-enforcement-is-stabilisation.md: the enforcement gradient lacks a concept of structured recovery (what to do after a soft violation is detected); ABC's recovery mechanisms (typed corrective actions with fallback chains) fill this gap — a synthetic note on structured recovery could bridge ABC, methodology-enforcement, and error-messages-that-teach
- kb/sources/convexbench-can-llms-recognize-convex-functions.ingest.md: recommended next action (update scoping note's "Undeveloped directions" section with ConvexBench evidence) has been partially done but the ingest does not reflect this
- kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md: the highest-leverage action is creating the synthesis note `information-value-is-observer-relative-because-extraction-requires-computation.md` to properly mediate epiplexity connections; direct links to bitter-lesson-boundary and learning-is-not-only-about-generality were reviewed and found dubious (speculative/orthogonal)
- kb/notes/information-value-is-observer-relative-because-extraction-requires-computation.md: missing connection to MVO source — MVO is a concrete external example of "making structure accessible to bounded observers" via vocabulary bootstrap
- kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md: the "naming amortizes discovery cost" claim has no external examples; MVO's "conceptual thresholds" from pedagogy research would ground it
- kb/sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md: connections section identifies 4 connections but 3 of them remain unidirectional from the ingest outward — only context-efficiency links back
- kb/sources/mem0-memory-layer.md: no frontmatter — text file that should be converted via /convert to add frontmatter with status: seedling
- kb/notes/related-systems/related-systems-index.md: Mem0 mentioned in paragraph text but has no entry in the Systems list, unlike CrewAI Memory and other tracked systems with only ingest-level coverage; inconsistent with other lightweight-coverage entries like Fintool which do have a list entry
- kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md: status is speculative but describes a concrete taxonomy with testable predictions; still appropriate given the Tulving mapping is decorative caveat, but should be revisited after the comparative review confirmed cross-contamination patterns
- kb/notes/related-systems/crewai-memory.md: mentions Mem0 in the "Relation to Other Reviewed Systems" section but says "Mem0, Graphiti, Cognee, Letta" — should reference the comparative review note by link rather than listing systems inline
- kb/sources/cognee-knowledge-engine.md: no frontmatter — text file that should be converted via /convert to add frontmatter with status: seedling (same issue as mem0-memory-layer.md)
- kb/notes/related-systems/sift-kg.md: does not mention Cognee despite both being LLM-driven document-to-knowledge-graph pipelines; the schema-discovery (sift-kg) vs schema-definition (Cognee Pydantic) contrast is the sharpest axis of comparison between them
- kb/notes/related-systems/related-systems-index.md: Graphiti mentioned in paragraph text but has no Systems list entry, same inconsistency already noted for Mem0 and Letta
- kb/sources/graphiti-temporal-knowledge-graph.md: no frontmatter — text file that should be converted via /convert to add frontmatter with status: seedling
- kb/sources/graphiti-temporal-knowledge-graph.ingest.md: recommended next action (update files-not-database to acknowledge Graphiti as counterexample) remains unexecuted
- kb/notes/learning-theory.md: Memory & Architecture section lists A-MEM and AgeMem sources but not Graphiti, despite Graphiti having the strongest temporal model in the surveyed systems
