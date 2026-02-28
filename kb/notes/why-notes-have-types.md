---
description: Six roles of the type system — navigation hints, metadata enforcement, verifiable structure, local extensibility, output quality through structured writing discipline, and maturation through stabilisation
type: note
areas: [document-system]
status: seedling
---

# Why notes have types

The type system serves six distinct roles. Each is developed in its own note; this page provides context and links.

## Navigation

Agents are stateless and context is finite. [Types give agents structural hints before opening documents](./types-give-agents-structural-hints-before-opening-documents.md) — a `spec` says "you can implement from this," a `structured-claim` says "there's a developed argument with evidence," an `index` says "follow links from here." The type plus description let an agent narrow from hundreds of files to the few it needs without opening any of them.

## Metadata enforcement

Navigation depends on metadata existing reliably. The [type system enforces metadata that navigation depends on](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions exist because the [note base type](../../types/note.md) requires them. Without enforcement, agents and humans under time pressure skip metadata, and the knowledge base degrades to a collection navigable only by opening every document.

## Verification

Types must assert [verifiable structural properties, not subject matter](./document-types-should-be-verifiable.md). "This is a design note" is not verifiable — every note in a design KB is about design. "This has Evidence and Reasoning sections" is verifiable. The verification gradient means types can be checked at different levels of cost — from deterministic (does the frontmatter have a description?) through LLM rubric (is the description discriminating?) to corpus-level (does this contradict existing claims?).

## Extensibility

Different knowledge domains need different document structures. [Directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — the global layer stays thin ([text](../../types/text.md) and [note](../../types/note.md)), while each collection has its own `types/` subdirectory with templates that extend the base. This keeps per-session context cost low and lets users introduce new types by adding a template locally, with no global configuration changes.

## Output quality

Types don't just organise — they shape what gets written. When a `structured-claim` template requires Evidence, Reasoning, and Caveats sections, the writer must actually produce those things. With LLMs specifically, three independent arguments support this:

- [Human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — LLMs exhibit human-like failures (conflating evidence with opinion, skipping qualifications), so structures that prevent those failures in humans prevent them in LLMs too.
- [Structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — structured templates steer autoregressive generation toward scientific papers and formal arguments rather than unstructured web text.
- [Structured output is easier for humans to review](./structured-output-is-easier-for-humans-to-review.md) — separated sections let a reader check facts and logic independently, regardless of how the LLM produced them.

The arguments are independent and complementary. Each stands alone; together they cover the full chain: the LLM might reason better, the output will be shaped better, and the human reader can evaluate it better.

## Maturation

Content starts as [text](../../types/text.md) (no frontmatter, no structure) and gains type information as it develops — gradual typing applied to documents. The maturation path is: raw capture → add frontmatter (`note`) → accumulate traits → promote to a specific type when structural criteria are met. A bare note that persists without promotion is a signal. This mirrors the broader [stabilisation pattern](./methodology-enforcement-is-stabilisation.md): practices start stochastic and harden as they prove out.

## Why free-form, not enum

The `type` field is a string, not validated against a list. This is deliberate:

- **New domains.** Workshop documents, scenario types, recurring tasks — these emerged after the initial type system. A closed enum would have required updating a global definition for each.
- **User adaptation.** Installed claws serve different purposes. A research project might need `experiment` and `literature-review` types. A product team might need `user-story` and `retrospective`. These should be addable locally.
- **Tolerance of fuzziness.** Types are assigned by agents and humans, not compilers. The system must tolerate misclassification — nothing breaks if a type is wrong or novel. Types are search aids, not enforcement boundaries.

Convention establishes common values. Directory `types/` folders document structural expectations. But the system doesn't require permission to use a new value.

---

Relevant Notes:
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — foundation: the verifiability principle that shapes what types can be
- [document-classification](./document-classification.md) — the taxonomy: base types table and migration history
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — the economic argument for thin global types and local extension
- [types-give-agents-structural-hints-before-opening-documents](./types-give-agents-structural-hints-before-opening-documents.md) — develops: the navigation role of types
- [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md) — develops: the enforcement role that makes navigation reliable
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — develops: the failure-mode transfer argument for output quality
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — develops: the distribution-selection argument for output quality
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — develops: the readability argument for output quality
- [a-functioning-claw-needs-a-workshop-layer-not-just-a-library](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — the workshop layer that will need its own type extensions

Topics:
- [document-system](./document-system.md)
