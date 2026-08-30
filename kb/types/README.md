# Types

Global structural contracts used across Commonplace collections. A type-spec document tells authors and readers what an artifact of that type contains; its sibling schema enforces the deterministic part of the contract. Typed artifacts store the path to their contract in the `type:` frontmatter field.

## Authored artifact types

- [Note](./note.md) — the base structured knowledge artifact
- [Instruction](./instruction.md) — procedures, skills, prompts, and work packets
- [Definition](./definition.md) — operational vocabulary definitions
- [Review gate](./review-gate.md) — one judgment-based quality criterion
- [Tag README](./tag-readme.md) — a tag's curated landing page, with optional validated marks
- [Agentic system analysis result](./agentic-system-analysis-result.md) — one complete, evidence-bounded analysis run across response, file, or package carriers

## Type-system contracts

- [Type spec](./type-spec.md) — the contract that type-spec documents themselves follow
- [Generated index](./generated-index.md) — build-time directory listings; never an authored landing page
- [Text](./text.md) — the implicit no-frontmatter case, not a selectable `type:` value

Collection-specific types live under their owning collection's `types/` directory. See [Collections and types](../reference/collections-and-types.md) for how artifacts use global and collection-local specs and how their paths resolve.
