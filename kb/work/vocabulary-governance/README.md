# Vocabulary Governance

Workshop for deciding how shipped commonplace KBs should handle vocabulary: which definitions are global, which belong to collections, which are required by artifact types, and how write paths should discover and enforce those policies.

## Question

How should commonplace support both a shared baseline vocabulary and user- or collection-specific vocabularies without hardcoding this repo's terms into the shipped write machinery?

This repo currently wants the same basic vocabulary across most surfaces: context engineering, distillation, constraining, codification, register, workshop, and the artifact-analysis vocabulary around retained artifacts. A consuming KB may instead want its own domain terms, collection-local terms, or type-specific terminology. The framework needs a policy shape that lets each KB declare vocabulary scope without turning `cp-skill-write` into a list of built-in terms.

## Current Tension

- Collections already govern two language-facing surfaces: register and linking. Vocabulary would add a third surface, but it has different scoping needs because some terms are KB-global while others are collection-local.
- Linking is both intra-collection and inter-collection. Vocabulary policy has the same shape: a collection may define local terms, import global terms, and use shared relationship labels to connect outward.
- Audience is related but probably belongs at KB scope by default. Collections can change register, link permissions, and vocabulary imports without changing who the KB is written for.
- Always-loaded context can teach agents the local vocabulary, but shipped projects should not inherit this repo's exact terms as universal defaults.
- Definition notes give vocabulary durable homes, but writers still need to know when a term must be glossed, linked, or treated as structurally required.
- Collection conventions are the likely home for vocabulary scope, but some vocabularies may be global across all collections.
- Type specs may require terms that are not collection-wide, such as artifact-analysis fields in agent-memory-system reviews.
- Users need room to build their own vocabularies without fighting the framework's methodology vocabulary.

## Candidate Model

Split vocabulary into three levels:

1. **KB-global vocabulary** — terms whose special meaning applies across the whole KB.
2. **Collection-local vocabulary** — terms whose special meaning applies only within one collection or collection family.
3. **Type-specific vocabulary** — terms required by a particular artifact type because the type's schema, lens, or quality bar depends on them.

The generic write path should know how to load vocabulary policy, not which terms are important. A collection or type should name the active vocabulary sources and first-mention expectations.

Collections would then govern three related authoring contracts:

- **Register** — what kind of claims or artifacts belong here.
- **Linking** — what relationships this collection may create inside itself and across collection boundaries.
- **Vocabulary** — which definitions are in scope, which are local, which are imported, and how writers should gloss or link them.

Another useful framing: vocabulary behaves like a library. Using a defined term is like invoking a subroutine from an imported library: the surface word is short, but it dispatches the reader or agent into a larger interpretation routine. Under this frame, vocabulary policy needs import rules, local definitions, collision handling, and public documentation just as code libraries need namespaces, exports, and dependency boundaries.

Audience should likely be a KB-level contract rather than a collection-level contract. A KB can say "write for agents and maintainers who know the domain but may not know this KB's local terms"; collections then adjust artifact shape, not target reader. Collection-local audience should be treated as an explicit exception, not the normal design.

## Design Questions

- Does every KB need a global vocabulary declaration, or is `AGENTS.md` enough?
- Where is the KB-level audience declared, and how does it affect glossing, definition links, and register?
- Do collections ever need their own audience declarations, or only explicit exceptions from the KB-level audience?
- Should vocabulary policy live directly in each `COLLECTION.md`, or should collections point to a shared vocabulary manifest?
- Should `kb/notes/definitions/` remain the default global definitions location, or should shipped projects be able to choose a different collection?
- How should collection-local definitions be named and linked: `kb/<collection>/definitions/`, collection-local type paths, tags, or another mechanism?
- Can vocabulary reuse the same collection-boundary model as linking: local terms by default, explicit imports for shared/global terms, and articulated edges when terms cross boundaries?
- If vocabulary is a library, what are the equivalents of imports, exports, namespaces, qualified names, shadowing, and versioning?
- What should the write skill do when multiple vocabulary sources define the same term?
- Is first-mention glossing a collection rule, a type rule, or a site-publication rule?
- How should vocabulary policy interact with `defined-in` link labels and external-reader accessibility?
- Which parts should be validated mechanically, and which should stay as authoring guidance?

## Possible Outputs

- A vocabulary-policy section template for `COLLECTION.md`.
- A reference note explaining global, collection-local, and type-specific vocabulary scopes.
- A small update to `cp-skill-write` telling it to load vocabulary policy without naming terms.
- Revisions to `kb/types/definition.md` if definition notes need scope metadata.
- A migration note for this repo's current vocabulary redesign.

## Closure

Close this workshop when we have a concrete policy proposal that answers:

- where global vocabulary is declared;
- how collections import or override vocabulary;
- how type specs add required terminology;
- what the generic write path must read;
- what shipped user KBs can customize without editing framework code.
- whether audience is KB-global by default, and what counts as a valid collection-level exception.

## Grounding

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — landed artifact-analysis vocabulary that this governance workshop treats as an example vocabulary library.
- [AGENTS.md](../../../AGENTS.md) — current always-loaded vocabulary surface.
- [Writing conventions for kb/notes](../../notes/COLLECTION.md) — current collection-level definition/linking policy.
- [Definition type](../../types/definition.md) — current durable artifact shape for operational vocabulary.
- [Writing skill](../../instructions/cp-skill-write/SKILL.md) — current generic write path.
- [Link vocabulary](../../reference/link-vocabulary.md) — current relationship-label catalogue, including `defined-in`.
