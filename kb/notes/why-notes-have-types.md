---
description: Seven roles of the type system — navigation hints, metadata enforcement, verifiable structure, local extensibility, content-layer identification, output quality through structured writing discipline, and maturation through constraining
type: kb/types/note.md
tags: [type-system]
---

# Why notes have types

The type system serves seven distinct roles. Each is developed in its own note or nearby register theory; this page provides context and links.

## Navigation

Agents are stateless and context is finite. [Types give agents structural hints before opening documents](./types-give-agents-structural-hints-before-opening-documents.md) — a `spec` says "you can implement from this," a `structured-claim` says "there's a developed argument with evidence," an `index` says "follow links from here." The type plus description let an agent narrow from hundreds of files to the few it needs without opening any of them.

## Metadata enforcement

Navigation depends on metadata existing reliably. The [type system enforces metadata that navigation depends on](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions exist because the [note base type](../types/note.md) requires them. Without enforcement, agents and humans under time pressure skip metadata, and the knowledge base degrades to a collection navigable only by opening every document.

## Verification

Types must assert [verifiable structural properties, not subject matter](./document-types-should-be-verifiable.md). "This is a design note" is not verifiable — every note in a design KB is about design. "This has Evidence and Reasoning sections" is verifiable. The verification gradient means types can be checked at different levels of cost — from deterministic (does the frontmatter have a description?) through LLM rubric (is the description discriminating?) to corpus-level (does this contradict existing claims?).

## Extensibility

Different knowledge domains need different document structures. [Directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — the global layer stays thin ([text](../types/text.md) and [note](../types/note.md)), while each collection has its own `types/` subdirectory with templates that extend the base. This keeps per-session context cost low and lets users introduce new types by adding a template locally, with no global configuration changes.

## Communicative-profile identification

Types also help identify which communicative profile governs an artifact. The profile is not always encoded by the type name alone: a `note` in `kb/notes/` is theoretical, a `note` in `kb/reference/` is descriptive, and an `instruction` is prescriptive. But the `type:` field plus the collection-local type path gives tools and readers enough information to infer the relevant quality goal: explanatory-reach for theory, fidelity and economy for description, executability and precision for prescription.

This connects the type system to [the classifier that separates profile, content kind, lineage, and authority](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md). Once the communicative profile is deducible from collection and type, validation and review can become profile-specific without adding a separate field everywhere. That inference does not classify individual regions or consumption paths.

## Output quality

Beyond organisation, types shape what gets written. When a `structured-claim` template requires Evidence, Reasoning, and Caveats sections, the writer must actually produce those things. With LLMs specifically, two arguments support this role and one evidential limit prevents overclaiming its mechanism:

- [Human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — LLMs exhibit human-like failures (conflating evidence with opinion, skipping qualifications), so structures that prevent those failures in humans prevent them in LLMs too.
- [Structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md) — measured gains do not isolate a higher-quality training distribution from format constraints, task decomposition, or extra computation.
- [Structured output is easier for humans to review](./structured-output-is-easier-for-humans-to-review.md) — separated sections let a reader check facts and logic independently, regardless of how the LLM produced them.

The two positive arguments are independent, while the causal limit keeps their benefits from being misattributed. Together they justify structure through the work it requires and the review it enables without assuming a training-data mechanism.

## Maturation

Content starts as [text](../types/text.md) (no frontmatter, no structure) and
gains type information as it develops — gradual typing applied to documents.
The maturation path is: raw capture → add valid note frontmatter
(`description` plus `type: kb/types/note.md`) → accumulate traits → promote to
a specific type when structural criteria are met. A bare note that persists
without promotion is a signal. This mirrors the broader [constraining
pattern](./methodology-enforcement-is-constraining.md): practices start
stochastic and harden as they prove out.

## Why path-valued, not a closed enum

The `type` field points to a type-spec document rather than selecting from one framework-wide enum. This keeps the set extensible without making type identity free-form:

- **New domains.** Workshop documents, scenario types, recurring tasks — these emerged after the initial type system. A closed enum would have required updating a global definition for each.
- **User adaptation.** Installed knowledge bases serve different purposes. A research project might need `experiment` and `literature-review` types. A product team might need `user-story` and `retrospective`. These should be addable locally.
- **Path identity.** A new value is valid only when its path resolves to a real type spec. Different paths remain different contracts even if their specs use the same shorthand name.

Type choice remains a fallible authoring judgment, but the selected contract is an enforcement boundary: its schema and type-conformance review apply to the artifact. Extensibility comes from adding a type spec, not from inventing an unresolvable value.

---

Relevant Notes:

- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — foundation: the verifiability principle that shapes what types can be
- [collections and types](../reference/collections-and-types.md) — the current path-valued type model and examples
- [directory-scoped-types-are-cheaper-than-global-types](./directory-scoped-types-are-cheaper-than-global-types.md) — the economic argument for thin global types and local extension
- [artifact classification separates profile, content kind, lineage, and authority](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — explains the communicative-profile role that type and collection jointly identify, and the other questions they do not
- [types-give-agents-structural-hints-before-opening-documents](./types-give-agents-structural-hints-before-opening-documents.md) — develops: the navigation role of types
- [type-system-enforces-metadata-that-navigation-depends-on](./type-system-enforces-metadata-that-navigation-depends-on.md) — develops: the enforcement role that makes navigation reliable
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — develops: the failure-mode transfer argument for output quality
- [Structured-prompt gains do not establish training-distribution selection](./structured-prompt-gains-do-not-establish-distribution-selection.md) — contrasts: limits what prompt-performance evidence establishes about the mechanism behind output quality
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — develops: the readability argument for output quality
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — the workshop layer that will need its own type extensions
