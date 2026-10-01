# Types

Global structural contracts used across Commonplace collections. A type-spec document tells authors and readers what an artifact of that type contains; its sibling schema enforces the deterministic part of the contract. Typed artifacts store the path to their contract under a KB root in the `type:` frontmatter field, such as `type: types/note.md`.

## Authored artifact types

- [Note](./note.md) — the base structured knowledge artifact
- [Instruction](./instruction.md) — procedures, skills, prompts, and work packets
- [Definition](./definition.md) — operational vocabulary definitions
- [Review gate](./review-gate.md) — one judgment-based quality criterion
- [Tag README](./tag-readme.md) — a tag's curated landing page at `kb/tags/<tag>-README.md`, with optional validated marks
- [Agentic system analysis overview](./agentic-system-analysis-overview.md) — entry member: identity, boundary, source register, reconciliation and public synthesis
- [Agentic system runtime report](./agentic-system-runtime-report.md) — runtime member: runtime account, probe evidence, runtime-declared records
- [Agentic system epistemic report](./agentic-system-epistemic-report.md) — epistemic member: the six-block overlay on the set's records
- [Agent memory analysis report](./agent-memory-analysis-report.md) — memory member: the specialist's accepted findings and comparison profile, unchanged

## Type-system contracts

- [Type spec](./type-spec.md) — the contract that type-spec documents themselves follow
- [Generated index](./generated-index.md) — build-time directory listings; never an authored landing page
- [Text](./text.md) — the implicit no-frontmatter case, not a selectable `type:` value

Collection-specific types live under their owning collection's `types/` directory. See [Collections and types](../reference/collections-and-types.md) for how artifacts use global and collection-local specs and how their paths resolve.

The analysis member types share the [source](../reference/agentic-analysis-sources.md)
and [record](../reference/agentic-analysis-records.md) contracts. Worker
invocations supply those files alongside the member types each job needs.
