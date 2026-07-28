# Theoretical lenses and working model

This is an initial map, not an adopted vocabulary. Its purpose is to keep several useful traditions from being collapsed into one intuition about “relations.”

## The lenses

### Informal argumentation

Toulmin separates claim, data, warrant, backing, qualifier, and rebuttal. The operational lesson is that a premise, an observation offered as evidence, and the rule licensing the move from observation to claim are not interchangeable forms of support. Commonplace already uses a Toulmin-derived structured-claim type, but the old `grounds` label blurred these roles in the link vocabulary.

- Local source: [Toulmin argument model ingest](../../sources/purdue-owl-toulmin-argument.ingest.md)
- Existing application: [Claim notes should use Toulmin-derived sections](../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md)

### Inferentialism

On an inferentialist view, grasping a claim includes grasping its circumstances of application, consequences, and incompatibilities. For links, the useful question is not only “what is the target?” but “what commitment does accepting this edge undertake, and what must change if one endpoint is rejected?” This lens may give theoretical support to the counterfactual and maintenance tests already emerging from label migrations.

- External starting point: [Robert Brandom, *Articulating Reasons*](https://sites.pitt.edu/~rbrandom/Courses/2024%20Philosophy%20of%20Language/Texts/Brandom%20Articulating%20Reasons%20An%20Introduction%20to%20Inferentialism.pdf)

### Philosophy of scientific mechanism

Machamer, Darden, and Craver analyze mechanisms as organized entities and activities productive of regular change. That is narrower than “a note that helps explain how.” This supplies a forcing test for the current `mechanism` corpus: distinguish a relation to an explanatory claim from a claim that the source phenomenon literally operates through the target machinery.

- External starting point: [Machamer, Darden, and Craver, “Thinking about mechanisms”](https://philosophy.wustl.edu/files/philosophy/imce/thinking_about_mechanisms.pdf)

### Rhetorical Structure Theory

RST describes coherence through functional relations between text spans, including evidence, cause, enablement, elaboration, and contrast. Relations are partly characterized by their intended effect on the reader, and inventories can vary with text type. This supports reader-oriented, collection-sensitive vocabularies while warning that a discourse function is not automatically an ontological relation between the subjects discussed.

- External starting point: [Mann and Thompson, “Rhetorical Structure Theory”](https://doi.org/10.1515/text.1.1988.8.3.243)
- Authors' archive: [RST resources at Simon Fraser University](https://www.sfu.ca/rst/)

### Relevance theory

Relevance theory treats relevance as cognitive effects achieved relative to processing effort. Commonplace's decision-cost theory has nearly the same operational shape: a pointer earns its context cost by letting a reader predict a useful result. This lens bears on whether labels should name reader questions and why context phrases are not optional decoration.

- External starting point: [Wilson and Sperber, “Relevance Theory”](https://www.phon.ucl.ac.uk/home/PUB/WPL/02papers/wilson_sperber.pdf)

### Associative semantic memory

Spreading-activation models treat semantic accessibility as graded and context-sensitive rather than as a small set of authored categorical relations. Their likely lesson for Commonplace is negative: similarity, topical association, and activation strength are usually retrieval-layer properties. They may be derived from content, graph position, and use rather than asserted as durable edges.

- External starting point: [Collins and Loftus, “A spreading-activation theory of semantic processing”](https://doi.org/10.1037/0033-295X.82.6.407)

## Working decomposition

The current hypothesis is that a link may carry several separable dimensions:

| dimension | question | candidate surface |
|---|---|---|
| assertion | What does the source claim about the target? | registered identifier and endpoint-role signature |
| reader function | Why would a reader follow it here? | label reader-need plus local context phrase |
| commitment strength | How load-bearing is the target for the source text? | inline/footer position and connective prose |
| revision consequence | What should be reconsidered if the target changes or is rejected? | catalogue maintenance semantics; possibly later validation/review routing |
| associative activation | How likely is the target to help in this context? | derived search, ranking, backlinks, graph signals, or usage—not necessarily authored metadata |

This decomposition is deliberately provisional. The dimensions may collapse in worked cases, or one may prove too expensive to author. Its value is that disagreements can now identify which dimension they concern.

## Candidate relation signature

Before registering a directional identifier, try describing it with:

| field | question |
|---|---|
| source role | assertion, observation, design, rule, procedure, description, phenomenon, system, or other |
| target role | premise, evidence, warrant, explanation, mechanism, prerequisite, definition, realization, or other |
| assertion template | Does `source <label> target` state the intended relation without reversing endpoints? |
| reader question | What unmet need makes following worthwhile? |
| revision consequence | What changes when the target is rejected, revised, or disappears? |
| inverse | Is an inverse assertion useful, and is it distinct from reciprocal authoring or a computed backlink? |

The signature is an evaluation device, not yet a schema requirement. It should be rejected if authors cannot apply it reliably or if it duplicates information already visible from collection and prose.

## The mechanism forcing case

The current migration work exposes three candidate assertions that must not be treated as synonyms without review:

- a source assertion is **explained by** a target claim;
- a source phenomenon or system **operates through** a target process or component;
- a source assertion is **premised on** a target claim about how something works.

The first is epistemic/discourse-facing, the second is a stronger subject-matter claim, and the third is inferential. They may nevertheless collapse for Commonplace if agents cannot use the distinction consistently or if the artifact/claim/phenomenon levels cannot be recovered from note titles and context phrases.

## Evidence still needed

- Reclassify worked edges using the full signature and measure inter-reviewer agreement, especially on explanation versus mechanism.
- Test whether labels plus context phrases improve agent follow/skip decisions over titles and context phrases alone.
- Test whether revision consequences predict useful downstream review targets better than source/destination collection alone.
- Examine whether weak associative links help retrieval enough to justify authoring or whether search and derived backlinks dominate them.
- Identify relation distinctions that are philosophically respectable but operationally invisible to agents; those should not enter the vocabulary.

