# Linking foundations

## Purpose

Develop a defensible theory of authored links for an agent-operated knowledge base before Commonplace finishes normalizing its link vocabulary. Linking is not merely graph decoration here: it shapes what an agent reads, which inferences it can inspect, and what later changes should trigger reconsideration.

The immediate question is whether one flat relationship label is being asked to carry several different things:

- a source→target assertion about the represented subject matter;
- an inferential role such as premise, evidence, warrant, or incompatibility;
- a discourse function or reader action;
- a maintenance consequence when the target changes;
- an associative retrieval signal.

The workshop should determine which of those belong in authored link semantics, which belong in the context phrase or link position, and which should remain derived views.

## Relationship to existing workshops

The sibling [linking-contract-consistency](../linking-contract-consistency/README.md) workshop owns current vocabulary decisions, corpus migrations, collection authorization, reciprocal-link procedure, validation, and backlink delivery. It may use findings from this workshop, but should not settle foundational questions incidentally during a label migration.

The [philosophy-borrowing](../philosophy-borrowing/README.md) workshop applies an operational adoption test to philosophical concepts across Commonplace. This workshop owns the deeper link-specific synthesis, including cognitive-science and discourse-theory evidence that does not belong in a general philosophy survey.

The [lineage-mechanisms](../lineage-mechanisms/README.md) workshop continues to own derivation carriers, invalidation, and source-change propagation. This workshop may clarify the general meaning of a dependency edge without absorbing lineage implementation.

## Current grounding

Commonplace already has a substantial local theory:

- [Linking theory](../../notes/linking-theory.md) treats link quality as navigation uncertainty reduced per unit of context.
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) treats labels as names for reader needs.
- [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) models link-following as a relevance decision under bounded context.
- [Link strength is encoded in position and prose](../../notes/link-strength-is-encoded-in-position-and-prose.md) separates commitment strength from relationship type.
- [Inbound and outbound links serve asymmetric reader needs](../../notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md) separates authored outbound edges from derived inverse views.
- [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) requires every directional identifier to complete `source <label> target`.

The [initial theoretical lenses](./theoretical-lenses-and-working-model.md) record the new forcing distinctions without treating them as adopted conclusions. The [current case](./current-case.md) traces the implemented evidence and rationale migrations, the grounds adjudication, and the unresolved 128-edge mechanism surface that makes the foundational question concrete. The [formal-link brainstorming brief](./brainstorm-formal-link-theory.md) fixes the established observations and instructs a later investigation to keep generated possibilities separate from findings. The [competing link models](./competing-link-models.md) file executes that brief: four candidate models, a projection-based synthesis candidate, candidate practical conclusions with adoption routes, and the discriminating evidence — none of it adopted. The [generator retrodiction run](./generator-retrodiction-run.md) executes the cheapest of those discriminating tests: blind stage-1 predictions recovered each collection's family structure but not its label table, supporting the seed-then-harvest generator over seed-alone.

## Questions

1. What kind of thing is an authored link: a proposition, an inference license, a discourse act, a navigation affordance, a maintenance dependency, or a structured combination?
2. Should the registered identifier name the subject-matter relation, the reader action, or the revision consequence? Which information belongs in the context phrase and link position instead?
3. Are premise, evidence, warrant, explanation, mechanism, cause, enablement, definition, realization, contradiction, and association genuinely different reader decisions in this KB?
4. When does a relation describe artifacts, the claims named by their titles, or the phenomena those claims discuss? Can one assertion template move among those levels safely?
5. Which relations should be authored because they carry commitments, and which should be computed from backlinks, lexical/embedding similarity, usage, or graph structure?
6. How should semantic symmetry differ from reciprocal authoring and from a derived inverse view?
7. What evidence would show that a distinction helps agents choose, reason, or maintain better rather than merely making the vocabulary more philosophically precise?

## Boundaries

In scope:

- philosophy of inference, argument, explanation, causation, and mechanism;
- discourse coherence, relevance, navigation, and semantic-memory models;
- the relation between link semantics, reader action, and maintenance consequences;
- worked analysis of Commonplace edges when needed to test a theoretical distinction;
- evaluation designs for agent follow/skip, reasoning, and revision behavior.

Out of scope:

- migrating a live label or changing collection contracts before a conclusion is handed to the consistency workshop;
- treating a philosophical vocabulary as authoritative merely because it is established elsewhere;
- building an ontology or knowledge-graph engine without a demonstrated Commonplace consumer;
- generic retrieval or embedding-system design except where it decides what should remain a derived association;
- lineage storage and invalidation implementation.

## Adoption bar

A borrowed distinction earns a place only when it changes at least one concrete operation: authoring, follow/skip choice, inference inspection, review, change-impact analysis, validation, or retrieval. It must outperform the current reader-need and articulation tests on worked Commonplace cases. Decorative renaming and taxonomies without a consumer do not pass.

## Closure

Close the workshop when:

1. a durable model states what an authored link commits the source to;
2. the model assigns assertion, reader function, strength, revision consequence, and associative activation to explicit surfaces rather than leaving them conflated;
3. the important relation families have worked cases and boundary tests;
4. at least one agent-facing evaluation establishes what distinctions improve navigation, reasoning, or maintenance—or explicitly records why corpus judgment is the best available oracle;
5. durable conclusions are promoted into theory notes and, where warranted, a catalogue/contract proposal or ADR;
6. concrete vocabulary consequences are handed to `linking-contract-consistency` without retaining a second competing vocabulary here.
