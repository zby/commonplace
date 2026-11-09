# Vocabulary Governance

Workshop for deciding how shipped commonplace KBs should handle vocabulary: which definitions are global, which belong to collections, which are required by artifact types, and how write paths should discover and enforce those policies.

## Current Status

Part of the workshop has landed:

- **Active vocabulary** is now the KB-global term list declared in `AGENTS.md`.
- **Definition notes** are backing documentation for active vocabulary and other sharpened terms.
- **First-mention behavior** belongs in the write path: authors should gloss and link active vocabulary terms when the reader may not know the term.
- **Definition type guidance** now distinguishes term-boundary guidance from technique guidance: definition notes answer when to use the word, not when or how to perform the operation the word names.
- **Audience** is still assumed KB-global by default; no collection-local audience policy has been introduced.

The unresolved part is collection and type scope: how a KB should declare collection-local vocabulary, type-specific terminology, imports, collisions, and validation expectations without hardcoding this repo's terms into framework skills.

A second unresolved thread is how to migrate a load-bearing term after its boundary changes. The completed `prose` → `natural-language` workshop produced a [terminology migration method candidate](./terminology-migration-method-candidate.md). It remains provisional: the next vocabulary shift should test the candidate and determine whether a recurring core deserves promotion to an instruction.

A constraint on that design arrived from the distillation migration and is now a library note: [vocabulary collisions are prevented at write time, not resolved at read time](../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) (promoted 2026-07-17 from this workshop's [prose-has-no-scope.md](./prose-has-no-scope.md), which retains the evidence pointers and open policy items). Prose offers no read-time scoping and context assembly is concatenation without a linker, so two senses of one term merge silently whenever notes co-load — and the sub-agent isolation remedy cannot apply to library artifacts that exist to be co-loaded. Consequence for the candidate model: imports, qualified names, and shadowing have no prose implementation; collision *handling* must mean collision *prevention* — a one-term-one-sense invariant across all vocabulary sources that can co-load, with multi-word coinages as the collision-free naming path.

## Operator direction: investigate vocabulary checks during revision

During the frontier-work reconsideration on 2026-11-08, the operator declined
adding a naming-time collision check to the writing instructions. Keep the
writing path unchanged: the writer should retain maximum freedom rather than
carry another mandatory check.

The hard part is recognizing that a passage introduces a new technical term,
not executing an exact-string search after the term has been identified.
Detection requires interpreting whether a name is being given a special,
consequential meaning, including when no definition is explicitly announced.
The operator therefore rejected treating the screen as nearly cost-free.

The candidate direction is to revise more often and include vocabulary checks
among routine revision checks. This is a proposal to investigate, not an adopted
cadence, new gate, or authorization to redesign revision workflows. A possible
check would first identify names carrying technical meanings, compare them with
existing definitions and terminology decisions, and then assess whether different
uses create consequential ambiguity. Search supplies occurrences, not that
judgment; ordinary wording must not be classified as a new technical term merely
because it is unfamiliar.

Next, examine what existing revision already checks and try the missing part on
a real revision. Retain candidate terms, consequential findings, false alarms,
and effort before deciding whether a routine check or more frequent revision is
worth adopting. A zero-finding pass need not justify more machinery. Do not
implement the registry or expand the write skill as a prerequisite.

### Draft gate

The [vocabulary-reconciliation gate](./vocabulary-reconciliation.md) is a typed
workshop draft for collision detection during review. It recognizes implicit
technical meanings and compares a name's existing uses. Only supported collisions
determine the verdict. Unification candidates encountered in the inspected
material are retained separately for their ledger, without claiming coverage or
requiring broader discovery. Systematic unification needs a separate comparative
pass over a bounded related set. The gate does not judge whether a coinage earns
its place; that is the complementary jargon question.

The draft is not in the live gate catalog. Promotion needs a review path that
permits scoped vocabulary discovery and records the comparison inputs in the
evidence-validity boundary. The current note-and-criterion freshness hashes do
not track changes in all comparison artifacts. Automatic ledger insertion also
needs pending-entry semantics for the collision ledger, duplicate handling and
coordinator-owned writes. None of those runtime or ledger changes is implemented
by this draft. Detection performance has not been calibrated.

## Question

How should commonplace support both a shared baseline vocabulary and user- or collection-specific vocabularies without hardcoding this repo's terms into the shipped write machinery?

This repo currently wants the same basic vocabulary across most surfaces: context engineering, distillation, constraining, codification, register, workshop, and the artifact-analysis vocabulary around retained artifacts. A consuming KB may instead want its own domain terms, collection-local terms, or type-specific terminology. The framework needs a policy shape that lets each KB declare vocabulary scope without turning `cp-skill-write` into a list of built-in terms.

## Current Tension

- Collections already govern two language-facing surfaces: register and linking. Vocabulary may add a third surface, but the global case is now handled separately through `AGENTS.md` active vocabulary.
- Linking is both intra-collection and inter-collection. Vocabulary policy has the same shape: a collection may define local terms, import global terms, and use shared relationship labels to connect outward.
- Audience is related but probably belongs at KB scope by default. Collections can change register, link permissions, and vocabulary imports without changing who the KB is written for.
- Always-loaded context can teach agents the local vocabulary, but shipped projects should not inherit this repo's exact terms as universal defaults.
- Definition notes give vocabulary durable homes, but writers still need to know which vocabulary sources are active for the artifact they are writing.
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

- A vocabulary-policy section template for `COLLECTION.md` if collection-local vocabulary is introduced.
- A reference note explaining global, collection-local, and type-specific vocabulary scopes.
- A small update to `cp-skill-write` telling it to load collection/type vocabulary policy without naming terms.
- Optional revisions to type specs if type-specific vocabulary requirements become real.
- A migration note for consuming projects if active vocabulary becomes part of `commonplace-init`.
- A tested terminology-migration instruction, but only if another vocabulary shift confirms the provisional method candidate.

## Closure

Close this workshop when we have a concrete policy proposal that answers:

- where global vocabulary is declared; **answered for this repo: `AGENTS.md` active vocabulary**
- how collections import or override vocabulary;
- how type specs add required terminology;
- what the generic write path must read;
- what shipped user KBs can customize without editing framework code.
- whether audience is KB-global by default, and what counts as a valid collection-level exception; **current default: KB-global unless explicitly exceptional**

## Grounding

- [Axes of artifact analysis](../../theory/axes-of-artifact-analysis.md) — landed artifact-analysis vocabulary that this governance workshop treats as an example vocabulary library.
- [AGENTS.md](../../../AGENTS.md) — current always-loaded vocabulary surface.
- [Writing conventions for kb/theory](../../theory/COLLECTION.md) — current collection-level definition/linking policy.
- [Definition type](../../types/definition.md) — current durable artifact shape for operational vocabulary.
- [ADR-022: active vocabulary and write-path first mentions](../../reference/adr/022-active-vocabulary-and-write-path-first-mentions.md) — landed decision for KB-global active vocabulary in `AGENTS.md`.
- [Writing skill](../../instructions/cp-skill-write/SKILL.md) — current generic write path.
- [Link vocabulary](../../reference/link-vocabulary.md) — current relationship-label catalogue, including `defined-in`.
- [Terminology migration method candidate](./terminology-migration-method-candidate.md) — provisional procedure extracted from one fully verified migration and awaiting a second test.
