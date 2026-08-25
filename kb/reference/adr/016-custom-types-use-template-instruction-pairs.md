---
description: Accepted decision that specialized and practitioner-defined types use separate template and instructions files; the former WRITING.md loading assumption is superseded by ADR-017
type: ../types/adr.md
tags: []
status: accepted
---

# 016-custom-types-use-template-instruction-pairs

**Status:** accepted
**Date:** 2026-04-10
**Refines:** [ADR-002](./002-inline-global-types-in-writing-guide.md) (single-hop optimization limited to the default `note` path) and operationalizes the type-surface split in [ADR-012](./012-types-for-structure-traits-for-review.md).
**Superseded in part by:** [ADR-017](./017-collection-md-is-the-register-convention-boundary.md) — the parts describing `WRITING.md` as the generic always-loaded writing guide; the template/instructions pair decision remains current.

## Context

[ADR-002](./002-inline-global-types-in-writing-guide.md) optimized the common write path by putting the default `note` template directly in [`kb/notes/COLLECTION.md`](../../notes/COLLECTION.md). That works for the always-loaded path because the agent needs generic writing conventions and the default note scaffold together on almost every write.

Specialized types have a different loading profile. ADRs, indexes, related-system reviews, source reviews, task types, and practitioner-defined local types are all less common and more collection-specific. They should not bloat `WRITING.md`, but they still need a stable authoring interface.

Before this split, several local types were represented by a single markdown file that mixed the literal scaffold with natural-language guidance about how to use each section well. That coupling made the type surface less predictable: agents and tooling had no simple convention for "load the structure" versus "load the authoring advice", and the generic writing guide risked re-absorbing type-specific conventions because there was no clear place for them to live.

The type system after [ADR-012](./012-types-for-structure-traits-for-review.md) and [ADR-015](./015-standardize-authored-type-definitions-on-json-schema.md) already had three distinct jobs:

- agent-facing structure for drafting
- natural-language guidance for filling the structure well
- machine-readable validation

The file layout needed to make those roles explicit for every custom type.

## Decision

For every specialized type outside the default `note` path, Commonplace uses a companion file pair in the local `types/` directory:

- `{type}.template.md` defines the literal draft scaffold the agent should follow.
- `{type}.instructions.md` explains how to fill that scaffold in well.

When structural validation exists, the same type also keeps its machine-readable schema alongside that pair.

`WRITING.md` remains the generic always-loaded writing guide. It keeps the default `note` template and universal note-writing conventions, but it does not inline specialized or practitioner-defined type guidance.

The write flow loads `WRITING.md`, then for a specialized or practitioner-defined type the template and, if present, its instructions. Type discovery for custom types follows the template file naming convention rather than hardcoded routing for each type.

## Consequences

**Easier:**
- The boundary between scaffold and advice is explicit. Templates can stay terse and copyable, while instructions can explain intent and section quality without polluting the scaffold.
- `WRITING.md` stays focused on the universal write path instead of accumulating low-frequency type-specific rules.
- Practitioner-defined types get a predictable extension contract: drop a template pair into `kb/*/types/`, and the write flow can discover it without changing the global guide.
- The three type surfaces now line up cleanly: template for drafting, instructions for execution guidance, schema for validation.

**Harder:**
- Specialized-type writes now require extra reads on purpose: the agent pays an additional hop for the template and usually another for the companion instructions.
- Maintainers must keep template, instructions, and schema aligned when a type evolves.

---

Relevant Notes:

- [002-inline-global-types-in-writing-guide](./002-inline-global-types-in-writing-guide.md) — the companion decision for the always-loaded `note` path
