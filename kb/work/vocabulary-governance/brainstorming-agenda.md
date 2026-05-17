# Brainstorming Agenda

Use this file to structure the longer session. The goal is not to decide immediately; it is to surface the design space cleanly enough that a later note or ADR can be extracted.

## 1. Inventory Current Surfaces

- Always-loaded vocabulary in `AGENTS.md`.
- Definition notes under `kb/notes/definitions/`.
- Definition type contract in `kb/types/definition.md`.
- Collection conventions in `kb/*/COLLECTION.md`.
- Existing collection responsibilities: register and linking policy.
- Type-specific requirements in `kb/*/types/*.md`.
- Review gates that mention undefined terms, jargon, notation, or explication quality.
- Public reading concerns from ADRs or reference docs.

## 2. Separate Use Cases

- This repo's methodology vocabulary should apply broadly across the KB.
- Consuming user KBs should be able to define their own domain vocabulary.
- Some collections may need local vocabulary that should not leak everywhere.
- Some artifact types may require specialized terms even when the collection does not.
- Public readers need glosses and links even when agents already loaded definitions.
- The KB likely needs one audience definition that collections inherit by default.

## 3. Policy Shapes To Compare

### KB-Level Audience

Audience is a KB-wide writing contract by default. Collections vary register, linking, and vocabulary, but they usually do not vary who the KB is for.

Questions:

- Where should a KB declare its audience: `AGENTS.md`, a reference page, root README, or generated project config?
- How does audience differ from register?
- Should `COLLECTION.md` inherit audience silently, restate it, or only document exceptions?
- What would justify a collection-local audience exception?
- Does public-site publishing imply a secondary audience even when the operational audience is agents?

### Vocabulary As Library

Using a defined term is like invoking a subroutine from an imported library. The term compresses a larger interpretation routine into a short symbol.

Questions:

- What counts as importing a vocabulary library into a collection?
- Are definition notes the exported functions?
- Can a collection define a local term that shadows a global term?
- Do terms need qualified names when multiple vocabularies define nearby meanings?
- What is the public documentation equivalent of an API reference?
- How should agents discover the active vocabulary libraries before writing?

### Collection As Language Boundary

Collections already define register and linking. Add vocabulary as a parallel contract:

- Register says what kind of artifact this collection contains.
- Linking says what relationships this collection can assert within and beyond itself.
- Vocabulary says what terms are active here, which are imported, and which are local.

Questions:

- Does vocabulary belong beside register and linking in every `COLLECTION.md`?
- Should global vocabulary be an implicit import or an explicit import?
- Should cross-collection terms require the same kind of explicit relationship articulation as cross-collection links?

### Collection-Only Policy

Each `COLLECTION.md` declares vocabulary sources and first-mention rules.

Questions:

- How does a collection import a KB-global vocabulary?
- Does every collection duplicate the same policy?
- Can this support type-specific required vocabulary cleanly?

### Global Manifest Plus Collection Imports

A root or reference file declares global vocabulary sources; collections import it and add local sources.

Questions:

- Is this extra machinery worth it?
- What is the manifest path?
- Does validation need to understand it?

### Definition Metadata

Definition notes carry scope metadata, such as `scope: global` or `scope: collection`.

Questions:

- Does scope belong in the definition artifact or in the importing collection?
- How are moved or shared definitions handled?
- Would metadata help validation, or add maintenance overhead?

### Type-Spec Requirements

Type specs declare vocabulary that must appear, or must be understood, for that artifact type.

Questions:

- Is this only guidance, or can it be validated?
- How does it compose with collection vocabulary?
- Should type-specific vocabulary be listed as required concepts, required sections, or both?

## 4. Write-Path Contract

Candidate generic contract:

1. Read the target collection's `COLLECTION.md`.
2. Load any vocabulary policy named by the collection.
3. Load the selected type spec and its type-specific vocabulary requirements.
4. When drafting, gloss/link defined terms on first meaningful mention when the target reader may not already know them.
5. Do not hardcode any term names in the generic write skill.

Open questions:

- What counts as "first meaningful mention"?
- Should glossing be mandatory for internal notes, only public notes, or all library artifacts?
- Should the write skill search definitions before drafting, or only follow explicit vocabulary sources?

## 5. Validation Possibilities

- Warn when a term listed in active vocabulary appears without a `defined-in` link.
- Warn when a required type-specific term is absent.
- Warn when a definition note lacks scope or boundary sections.
- Keep validation advisory because term detection is noisy.

## 6. Extraction Targets

Possible durable artifacts after the workshop:

- `kb/reference/vocabulary-policy.md`
- revised `kb/notes/COLLECTION.md`
- revised `kb/reference/COLLECTION.md`
- revised `kb/instructions/COLLECTION.md`
- revised `kb/types/definition.md`
- small `cp-skill-write` change to load vocabulary policy
- ADR if the policy affects shipped framework behavior
