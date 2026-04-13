---
description: How commonplace resolves a note's type contract at authoring and validation time - collection-scoped lookup, collection conventions, and skill-driven on-demand loading
type: note
tags: []
status: current
---

# Type loading

How commonplace loads a type's structural contract when an agent authors a note or the validator checks one. For *which* types ship and where their files live, see [available-types](./available-types.md).

## The core mechanism

Commonplace stores a type's structural contract as files on disk — typically a `{type}.template.md`, a `{type}.instructions.md`, and a `{type}.schema.yaml` — rather than compiling the contract into code. Loading a type means finding and reading those files. Nothing else knows what an `adr` or a `source-review` is.

Two code paths read them:

- **Authoring.** A skill (e.g., `cp-skill-write`) opens the template and instructions for the type it is about to produce, so the agent generates content against the contract.
- **Validation.** `commonplace-validate` reads the schema for the type recorded in the note's frontmatter and checks the note's frontmatter and body against it.

Both paths resolve the same way: they start from the note's location on disk and walk outward to find a matching type name.

## Collection-scoped lookup

A note's [collection](./definitions/collection.md) is the top-level `kb/` subdirectory that owns it (`kb/reference/`, `kb/sources/`, `kb/reports/`, and so on). Each collection can carry its own `types/` subdirectory with its own specialised type definitions. The resolver for a note at `kb/<collection>/.../foo.md` with `type: X` in its frontmatter:

1. Looks for `kb/<collection>/types/X.*` first.
2. Falls back to the global `kb/types/X.*` if no collection-scoped definition exists.

The consequence is that bare type names are scoped by where the note lives: `type: adr` under `kb/reference/` resolves to `kb/reference/types/adr.*`, and the same name under another collection would resolve to that collection's definition. Adding a new type is an authoring step — drop the template, instructions, and schema into the owning collection's `types/` — with no code change. Per [ADR-012](./adr/012-types-for-structure-traits-for-review.md), the validator reads these schemas rather than carrying a hard-coded type-profile map.

Name collisions stay unambiguous as long as no two collections define the same type name with incompatible structure. Qualified canonical ids were considered and deferred.

## The default note path

The `note` base type is the one type whose template is carried by the write skill rather than loaded on demand. Most writes are plain notes, so the marginal cost of keeping the small template on the default path beats the cost of an extra file read per write. [ADR-002](./adr/002-inline-global-types-in-writing-guide.md) originally accepted inlining into a central `WRITING.md`; [ADR-017](./adr/017-collection-md-is-the-register-convention-boundary.md) replaces that with collection-level `COLLECTION.md` files for register conventions while keeping the default structural scaffold in the write skill.

Every other shipped type stays in its collection's `types/` directory and loads only when an agent is explicitly writing one. A skill or routing table line points at the specific template file (e.g., `kb/reference/types/adr.template.md`) rather than relying on the agent to remember every type definition.

## What authoring loads

Per [ADR-016](./adr/016-custom-types-use-template-instruction-pairs.md), a specialised type ships as a template plus an instructions pair:

- The template is a markdown skeleton the agent copies and fills in.
- The instructions explain how to fill each section, what to search for first, and what to link.

A write skill that already knows the target type opens the template and instructions in one hop and produces a note against them. The agent does not need every type definition loaded simultaneously — only the one it is about to produce.

## What validation loads

Per [ADR-015](./adr/015-standardize-authored-type-definitions-on-json-schema.md), schemas are authored as JSON Schema in YAML. `commonplace-validate` reads the note's frontmatter `type:` field, resolves it through the collection-scoped lookup described above, and checks the parsed note document against the resolved schema. The validator carries no hard-coded knowledge of any specific type; introducing a new type in a consuming project is an authoring step rather than a code change.

## Open questions

- How should `/validate` surface directory-local expectations that aren't captured in the schema yet? Some conventions still live in prose READMEs.
- Does the `type:` frontmatter field stay useful as a search filter once directory scoping becomes load-bearing? `rg '^type: note'` still works today, but adding more directory-local type names in consuming projects could fragment the filter.

---

Relevant Notes:

- [available-types](./available-types.md) — the shipped type inventory this note complements with loading-mechanism detail
- [002-inline-global-types-in-writing-guide](./adr/002-inline-global-types-in-writing-guide.md) — superseded decision: inlining `note` template into WRITING.md
- [012-types-for-structure-traits-for-review](./adr/012-types-for-structure-traits-for-review.md) — decision: types define structural requirements; directory-local `types/` scope definition lookup
- [015-standardize-authored-type-definitions-on-json-schema](./adr/015-standardize-authored-type-definitions-on-json-schema.md) — decision: JSON Schema in YAML as the authoring form for type definitions
- [016-custom-types-use-template-instruction-pairs](./adr/016-custom-types-use-template-instruction-pairs.md) — decision: specialised types use template + instructions files
- [017-collection-md-is-the-register-convention-boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — decision: collection-level COLLECTION.md files own register conventions while types stay structural
- [architecture](./architecture.md) — shipped architecture: where the type loading mechanism sits inside the installed surface
