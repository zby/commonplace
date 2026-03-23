=== PROSE REVIEW: trace-derived-learning-techniques-in-related-systems.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The note's core analytical contribution is the two-axis taxonomy (ingestion pattern + promotion target), the artifact-structure spectrum, and the "what remains open" synthesis. These occupy roughly the final third of the note. The per-system catalog occupies roughly the first two-thirds. The catalog is necessary evidence, but the synthesis sections that do the comparative work -- "What the comparison makes concrete," the artifact-structure spectrum, "What looks borrowable," "What remains open" -- are where the title's promise ("trace-derived learning techniques") gets paid off. As written, a reader must traverse ~5000 words of per-system description before reaching the comparative analysis that gives those descriptions meaning. The per-system sections are individually well-executed, but their aggregate weight buries the payoff.
  Recommendation: Consider whether the two-axis taxonomy and artifact-structure spectrum could move earlier (after the recurring-stages framework and before the per-system catalog), so readers encounter the analytical frame before the evidence. The per-system sections would then serve as elaboration rather than prerequisite. Alternatively, consider splitting the per-system catalog into a separate companion note, leaving this note as the comparative analysis with links to per-system details.

- [Confidence miscalibration] "The same five stages appear" (line 17) and the five-stage framework (Trigger, Source format, Extraction schema, Promotion/storage, Reinjection) are the note's own analytical construction imposed on the survey data -- a reasonable decomposition, but not a finding reported by the systems themselves. The assertive framing ("the same five stages appear") presents this as discovered structure rather than proposed structure. Compare with the more careful "The systems separate on two axes" later, which at least frames the taxonomy as an observation rather than an inherent property.
  Recommendation: Hedge the framing to signal construction: "Across these systems, the same five stages recur in our reading" or "We organize each system around five recurring stages." The per-system descriptions already demonstrate that the framework fits; the opening sentence can afford to be honest that it is an imposed lens.

INFO:
- [Proportion mismatch] The "What looks borrowable" section (lines 312-323) is a bulleted list of twelve design patterns without development. Each bullet names a pattern and gives one sentence of context, but none explains the tradeoff or limitation. Compare with "What remains open" (lines 327-336), which develops its points with reasoning. The borrowable-patterns list reads as a brainstorm dump rather than analysis at the same level as the rest of the note.

- [Redundant restatement] The opening of "What the comparison makes concrete" (line 253: "The systems separate on two axes") repeats what the introduction already stated (line 11: "this note reviews what each system actually does, then draws out the two axes that separate them"). The repetition is mild and arguably serves as a structural anchor after the long catalog, but in a note this long it reinforces the sense that the catalog and the analysis were written as separate pieces.

CLEAN:
- [Source residue] The note surveys seventeen systems and uses system-specific terminology (session files, JSONL, Chroma, MCTS, etc.) throughout. All such terms belong to the systems being described and are appropriate to the note's claimed scope -- a code-inspected cross-system comparison. No domain-specific framing leaked from a narrower source context. The vocabulary is consistently at the level of agent-system engineering.

- [Pseudo-formalism] The note contains no formal notation, equations, or mathematical apparatus. The five-stage framework and two-axis taxonomy are presented as verbal decompositions. The table in "Log formats matter more than the prompts" is descriptive, not pseudo-formal. No decorative formalism detected.

- [Orphan references] Scanned for specific numbers, named studies, or empirical claims. The note's empirical claims are all grounded in the code-inspected systems described in the note itself, with system names and code paths serving as implicit citations. The source-only systems (AgeMem, Trajectory-Informed Memory Generation) are explicitly flagged as lower-confidence and link to their ingest notes. No unsupported specific figures or orphan data points found.

- [Unbridged cross-domain evidence] The note stays within its domain (agent and LLM systems that learn from traces). All evidence comes from code inspection of systems in the same domain as the note's claims. No cross-domain transfer claims are made without bridging.

- [Anthropomorphic framing] Scanned for agency language. The note consistently uses mechanical/system language: "mines," "extracts," "promotes," "stores," "consumes," "writes." Systems are described as performing operations, not as knowing, understanding, or believing. The phrase "decides what deserves trust and persistence" (line 336) is applied to the open problem of evaluation, not attributed to a model's internal states. No problematic anthropomorphic framing detected.

Overall: 2 warnings, 2 info
===
