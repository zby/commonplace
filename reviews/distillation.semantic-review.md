=== SEMANTIC REVIEW: distillation.md ===

Claims identified: 14

## Step 1: Claims extracted

1. [Opening] "One of two co-equal learning mechanisms in deployed agentic systems, alongside constraining."
2. [Opening] "Distillation is compressing knowledge so that a consumer can act on it within bounded context."
3. [Opening] "Without distillation, the source material often exceeds the consumer's effective context for the task -- making the operation infeasible, not merely slow."
4. [Opening] "Even when source material would technically fit, undistilled methodology crowds out the actual work -- both by consuming tokens and by adding navigational complexity."
5. [Opening] "Different operational contexts need different extractions from the same source, so multiple distillations are normal."
6. [Context engineering paragraph] "Distillation is the main operation that architecture performs, though not the only one (routing, scoping, and maintenance are also context engineering operations)."
7. [Prior work] Survey lists four fields (technical writing, pedagogical adaptation, library science, knowledge management) as prior work. Implicit scope claim: these are the relevant precedents.
8. [How distillation works] "The rhetorical mode may shift if the task demands it... What stays constant is the medium -- unlike codification, distillation typically stays in natural language consumed by an LLM."
9. [How distillation works] The table enumerates seven source-to-distillate pairs as covering the space of distillation operations.
10. [How distillation works] "Targeting is information loss -- this is why the source persists."
11. [Warning] "a distillate can look adequate while losing behavioral influence -- compressed experience is often less active than the raw traces it replaced"
12. [Relationship to constraining] "Constraining and distillation are orthogonal -- they operate on different dimensions of the same artifacts."
13. [Terminology note] KB distillation is distinguished from ML knowledge distillation by judgment, text artifacts, and operational effectiveness rather than behavior reproduction.
14. [Description field] "co-equal learning mechanism alongside constraining" -- echoes claim 1.

## Step 2: Completeness and boundary cases

### Framework: "Two co-equal learning mechanisms" (claims 1, 12)

Grounding definition: The note defines learning mechanisms in deployed agentic systems as distillation and constraining, presented as orthogonal (the 2x2 matrix).

Boundary cases tested:

(a) **Reorganization without compression.** An agent restructures existing notes -- reordering sections, splitting a long note into several, adding cross-links -- without reducing total volume. Is this distillation? The note's definition requires "compressing knowledge," but reorganization changes extractable value without compressing. The 2x2 matrix doesn't obviously place this: it's not constraining (interpretation space doesn't narrow) and it's not clearly distillation (no compression, no extraction from something larger). It could be argued that reorganization is a form of distillation (the "consumer" is the agent scanning an index, and the reorganized form is more compressed *for that consumer*), but the fit requires stretching the definition.

(b) **Deletion / pruning.** Removing outdated or low-value notes from the KB. This changes the knowledge available to future agents. It's not compression (nothing is extracted), and it's not constraining (no interpretation narrowing). Yet it's a learning-relevant operation -- the system becomes more capable because the noise floor drops. The two-mechanism framework doesn't account for it.

(c) **Acquisition of entirely new knowledge.** An agent ingests a new external source and writes a note about something the KB never covered before. This isn't extracting from existing KB material -- it's adding. It's arguably distillation of the external source, but the note's framing (especially "Most KB learning is distillation -- explore messily, notice patterns, extract insight, write a note") treats this as distillation, which works only if "the source" is construed broadly enough to include raw observations and external material.

(d) **Schema evolution.** Adding a new frontmatter field, introducing a new note type, changing the type system. This changes system capacity without compressing or constraining any particular artifact. It's architectural learning that falls outside both mechanisms.

Findings:

- **INFO** [Completeness] Reorganization without volume reduction (reordering, splitting, linking) sits ambiguously in the 2x2 matrix. It changes extractable value without clearly being distillation (no compression) or constraining (no interpretation narrowing). The note could acknowledge arrangement as a borderline case or clarify that "compression" includes restructuring that increases density-per-task even without reducing total volume.

- **INFO** [Completeness] Deletion/pruning and schema evolution are learning-relevant operations that don't map to either mechanism. The "two co-equal mechanisms" framing may undercount -- or the note could explicitly scope its claim to content-level operations and exclude architectural/curation operations.

### Enumeration: Seven source-to-distillate pairs (claim 9)

Grounding definition: The table implicitly claims to represent the space of distillation operations in a KB context.

Boundary cases tested:

(a) **Error post-mortem to detection heuristic.** An agent analyzes a failure, extracts a pattern, and writes a "watch for X" note. This maps reasonably to "Domain artifacts -> Detection/analysis skill."

(b) **Conversation transcript to decision record.** A human-agent conversation produces a design decision. Extracting the decision into an ADR is distillation from conversational raw material. This doesn't map cleanly to any row -- it's closest to "Workshop -> Note" but the source is a conversation, not a workshop artifact.

(c) **Multiple notes to index entry.** Writing a context phrase for an index entry is distillation of several notes into a one-line summary. Not clearly captured by any row.

Finding:

- **PASS** [Completeness] The table is illustrative, not exhaustive -- it uses no scope-claiming language ("all," "the complete set"). The examples cover a reasonable range. Edge cases like conversation-to-ADR and notes-to-index-entry are unstrained extensions of existing rows.

### Definition: "Medium stays constant" (claim 8)

Boundary case: **Distillation into a diagram or table.** The note's own table (source-to-distillate pairs) is arguably a distillation of examples into a non-prose form. Is a table still "natural language consumed by an LLM"? Broadly yes, but the qualifier "typically" in the claim handles this.

- **PASS** [Completeness] The "typically" qualifier in "distillation typically stays in natural language" leaves room for borderline cases like tables and structured formats.

## Step 3: Grounding alignment

### Epiplexity source (claim: "epiplexity measures theoretically what distillation does operationally")

The distillation note's Relevant Notes section states: "epiplexity measures theoretically what distillation does operationally -- quantifies extractable structure for a given observer under computational bounds."

The epiplexity ingest says: "Distillation is operationally what epiplexity measures theoretically. The context budget shaping a distillation IS a computational bound; epiplexity explains why tighter budgets extract less."

The alignment is strong for the structural-extraction aspect. However, epiplexity specifically measures *learnable patterns in sequential data* for a *computationally bounded model*. Distillation as defined in this note operates on any knowledge source (not just sequential data) and targets any consumer (including humans, per the prior-work section listing pedagogy and technical writing). The epiplexity paper's domain is narrower than distillation's domain.

The information-value-is-observer-relative note itself flags this gap: epiplexity "captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity."

- **INFO** [Grounding/domain-coverage] The link to epiplexity says it "measures theoretically what distillation does operationally," but epiplexity covers extractable *structure in sequential data* for a *computational model*, while distillation as defined here covers any knowledge source for any consumer. The theoretical grounding covers a subset of the claimed operational space. The information-value note already flags this gap; the distillation note's link text does not.

### Faithful Self-Evolvers source (claim 11: distillates can lose behavioral influence)

The distillation note warns: "a distillate can look adequate while losing behavioral influence -- compressed experience is often less active than the raw traces it replaced."

The ingest says: "agents reliably depend on raw experience, but often ignore or misread condensed experience, even when condensed memory is the only guidance available." The ingest's own limitations section notes: "its conclusion is best read as 'current summary forms often fail' rather than 'compression as such fails.'"

The distillation note's phrasing -- "compressed experience is *often* less active" -- is appropriately hedged and consistent with the source. The word "often" matches the empirical finding without overgeneralizing.

- **PASS** [Grounding] The warning about behavioral influence loss accurately reflects the Faithful Self-Evolvers source. The hedge "often" is appropriate given the source's own scope.

### Context engineering note (claim 6: distillation is the main operation)

The distillation note says: "Distillation is the main operation that architecture performs, though not the only one (routing, scoping, and maintenance are also context engineering operations)."

The context engineering note says: "Distillation -- compressing knowledge for a specific task under a context budget -- is the main operation these components perform, but not the only one."

These are consistent. The context engineering note lists four operational components (routing, loading, scoping, maintenance) and says distillation is what they perform. The distillation note accurately attributes three of those four as "also context engineering operations" but omits "loading." This is a minor discrepancy -- loading is arguably the component most directly performing distillation, so omitting it from the "also" list is odd but not a misattribution since the claim is about the relationship, not an exhaustive list.

- **PASS** [Grounding] The distillation-as-main-operation claim is well-aligned between the two notes.

### Constraining note (claim 12: orthogonality)

The distillation note's 2x2 matrix and the constraining note's 2x2 matrix are identical. The cell labels match verbatim. The framing questions ("Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*") match verbatim. These notes are clearly maintained in tandem.

- **PASS** [Grounding] The orthogonality claim and its 2x2 matrix are perfectly mirrored in the constraining note.

### Skills-derive-from-methodology note (supporting claim 8: medium stays constant)

The skills note argues at length that the methodology-to-skill relationship is distillation specifically because the medium does not change (both are natural language for LLM consumption), distinguishing it from codification (which changes the medium). This strongly supports claim 8.

- **PASS** [Grounding] The medium-constancy claim is well-supported by the detailed argument in the skills-derive-from-methodology note.

## Step 4: Internal consistency

### Definition vs. prior-work scope

The opening defines distillation as "compressing knowledge so that a consumer can act on it within bounded context." The prior-work section lists fields where the consumer is human (pedagogy, technical writing, library science). The "What's specific to our use" line says "the context budget is a hard constraint, not a soft guideline" -- implying the prior-work fields have soft constraints.

But the opening's "bounded context" language is agent-centric (the term is used throughout the KB to mean LLM context windows). The prior-work section implicitly broadens "consumer" to include human readers. This creates a minor tension: is the note defining distillation generally (any consumer, any context) or specifically (agent consumer, token budget)? The body and examples lean agent-specific, the prior-work section leans general.

- **INFO** [Consistency/definition-drift] The opening uses "bounded context" (an agent-specific concept in this KB) but the prior-work section cites human-reader fields. The note oscillates between "distillation is a general operation that these fields also perform" and "our distillation is specific because of hard context budgets." Both framings are defensible, but a reader could be confused about whether the note is defining distillation generally or specifically.

### "Main operation" vs. "one of two co-equal mechanisms"

Claim 1 says distillation is "one of two co-equal learning mechanisms." Claim 6 says distillation is "the main operation" that context engineering performs. These are compatible (learning mechanisms and context engineering operations are different frames) but the word "main" in claim 6 could create a tension with "co-equal" in claim 1 if a reader conflates the two frames. The note does distinguish them -- context engineering has four components, and distillation is the main thing they do -- but the implicit hierarchy (distillation is "main," constraining is not mentioned in the context engineering paragraph) could suggest distillation is more central than constraining.

- **INFO** [Consistency] "Co-equal learning mechanism" (claim 1) and "main operation context engineering performs" (claim 6) are logically compatible but could create an impression that distillation is more central than constraining. The constraining note does not make a parallel "main operation" claim for any architecture.

### Summary fidelity

The description field reads: "distillation compresses knowledge so a consumer can act on it within bounded context, making operations feasible that raw source material would exceed; co-equal learning mechanism alongside constraining." This faithfully represents the body's two key claims (the definition and the co-equal framing). It omits the medium-constancy claim and the warning about behavioral influence loss, but a description is not a comprehensive summary.

- **PASS** [Consistency] The description accurately represents the note's central claims without distortion.

## Findings Summary

WARN:
(none)

INFO:
- [Completeness] Reorganization without volume reduction (reordering, splitting, linking) sits ambiguously in the 2x2 matrix -- it changes extractable value without clearly being distillation or constraining. The note could clarify whether "compression" includes restructuring that increases density-per-task even without reducing total volume.
- [Completeness] Deletion/pruning and schema evolution are learning-relevant operations that don't map to either mechanism, suggesting the "two co-equal mechanisms" framing may undercount or needs explicit scoping to content-level operations.
- [Grounding/domain-coverage] The link to epiplexity claims it "measures theoretically what distillation does operationally," but epiplexity covers extractable structure in sequential data for a computational model, while distillation covers any knowledge source for any consumer. The theoretical grounding covers a subset of the claimed operational space.
- [Consistency/definition-drift] The opening uses "bounded context" (agent-specific in this KB) but the prior-work section cites human-reader fields (pedagogy, technical writing). The note oscillates between general and agent-specific definitions of distillation.
- [Consistency] "Co-equal learning mechanism" and "main operation context engineering performs" are logically compatible but could create an impression that distillation is more central than constraining.

PASS:
- [Completeness] The source-to-distillate table is illustrative, not exhaustive -- no scope-claiming language, reasonable range of examples.
- [Completeness] The "typically stays in natural language" qualifier leaves appropriate room for borderline medium cases.
- [Grounding] The warning about behavioral influence loss accurately reflects the Faithful Self-Evolvers source with appropriate hedging.
- [Grounding] The distillation-as-main-operation claim is well-aligned with the context engineering note.
- [Grounding] The orthogonality claim and 2x2 matrix are perfectly mirrored in the constraining note.
- [Grounding] The medium-constancy claim is strongly supported by the skills-derive-from-methodology note's detailed argument.
- [Consistency] The description field accurately represents the note's central claims.

Overall: 0 warnings, 5 info
===
