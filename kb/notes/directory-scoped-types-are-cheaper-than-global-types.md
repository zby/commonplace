---
description: Globally eligible types widen every collection's authoring choices; collection-local types keep specialized contracts scoped while path pointers load either kind on demand
type: kb/types/note.md
traits: [title-as-claim]
tags: [type-system]
---

# Directory-scoped types are cheaper than global types

A globally eligible type widens the authoring choice set in every collection. Its contract must also make sense everywhere it is eligible. A collection-local type enters the choice set only where its specialized structure applies.

Most structural affordances are collection-local. An agent writing theory does not need the sections of an ADR or an agent-memory-system review. Those contracts belong beside the collection that can use them. Global types are justified when their structure is reusable across collections.

Commonplace makes that scope explicit in the filesystem. Global type specs live under `kb/types/`; collection-local specs live under the owning collection's `types/` directory. The validator permits a global spec or the artifact's own collection-local spec, while rejecting a peer collection's local spec.

## Why this doesn't happen in programming

In programming, types are global (at least fully qualified names are) — and cheap. You can define a thousand types; only the ones you import are in scope. The compiler resolves references automatically. Declaration cost is near zero; resolution is free.

In an LLM context, loading still costs context, but a path-valued type pointer supplies a simple import mechanism. An existing artifact names its contract directly. The agent follows that pointer and loads one type spec on demand instead of preloading a global vocabulary.

Path resolution removes the old preload cost, but it does not erase eligibility cost. A new write given only a shorthand still searches the live type specs and requires one exact `name:` match. More importantly, making a type global claims that its contract is appropriate across collections. Collection-local placement keeps that claim narrow without sacrificing on-demand loading.

## The economic argument

Since [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md), a writer should load the selected contract rather than a catalogue of every possible contract. Scope still determines which contracts enter a writing decision:

- **Global layer:** eligible across collections. Use it for structures whose meaning and authoring contract are genuinely reusable.
- **Collection-local layer:** eligible in the owning collection. Use it for structure whose operations or sections only make sense there.

A small portable core can cover ordinary capture and note authoring:

| Form | What it tells an agent |
|---|---|
| implicit [`text`](../types/text.md) | No frontmatter; raw capture with no type-specific structural checks. |
| [`kb/types/note.md`](../types/note.md) | Structured note frontmatter: required path-valued `type` and `description`; optional `traits`, `tags`, and `user-verified`. |

Other global contracts remain possible when their structure is reusable. Specialized contracts such as ADRs, structured claims, articles, source artifacts, and agent-memory-system reviews stay collection-local. The type spec defines their structure, and validation checks the resolved schema.

## What moves between directories?

An argument against local scoping is that it prevents types from being portable. But the relevant boundary is the collection, not every subdirectory. A structured claim can move anywhere inside `kb/notes/` while retaining `type: kb/notes/types/structured-claim.md`. Moving it to another durable collection requires either a globally eligible contract or a deliberate type change.

Frontmatter-free text and the global note contract are portable because their structure is collection-independent. A local type is intentionally less portable: its narrower eligibility records that the contract is intended only for artifacts in that collection.

## How Commonplace applies the split

**Existing artifacts import one contract.** Their `type:` field stores a repository-relative or file-relative path to a type spec. The path, not the spec's shorthand `name:`, is type identity.

**New writes discover without a hand-maintained menu.** An exact path is opened directly. A shorthand search inspects type-spec frontmatter and succeeds only on one exact `name:` match. The filesystem remains the inventory.

**Validation enforces scope.** Global specs under `kb/types/` are eligible everywhere. A local spec is eligible in its owning collection. The workshop subtree is the deliberate staging exception and may use any valid type spec.

**The type spec is authoritative.** Its body contains the semantic authoring contract and any template; its `schema:` pointer names the deterministic structural contract.

## What stays global

The base note contract supplies the shared structured-note surface:

- **Required fields** — a path-valued `type` and a non-empty `description`.
- **Optional shared fields** — `traits`, `tags`, and `user-verified`. Absence of
  `user-verified` says nothing about maturity, truth, currency, or review state.
- **Text → note promotion** — adding complete note frontmatter with
  `description` and `type: kb/types/note.md` to a raw capture. This is a
  structural change, not a global lifecycle transition.

Collections own their text and outbound-link conventions. Specialized types may own coherent local lifecycle fields, but ordinary notes have no global `status`.

---

Relevant Notes:

- [collections and types](../reference/collections-and-types.md) — current-state: how Commonplace instantiates the thin-global, collection-local split and resolves both scopes by path
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — foundation: the loading economy argument applies to types the same way it applies to instructions
- [why directories despite their costs](./why-directories-despite-their-costs.md) — directories already carry local conventions; this note proposes making that load-bearing for types
- [document types should be verifiable](./document-types-should-be-verifiable.md) — the verifiability principle still applies, but verification becomes directory-scoped
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — workshop subsystems (tasks, queues) already define their own types locally; this generalises that pattern
