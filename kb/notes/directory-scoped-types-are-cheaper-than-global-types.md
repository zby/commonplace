---
description: Global types tax every session's context; directory-scoped types load only when working in that directory — most structural affordances are directory-local, so the type system should match that economy
type: note
traits: []
status: seedling
areas: [document-system]
---

# Directory-scoped types are cheaper than global types

The [document classification](./document-classification.md) spec defines seven global base types: `text`, `note`, `structured-claim`, `spec`, `review`, `index`, `adr`. Every agent that touches the KB needs to know this vocabulary — it lives in the classification spec, is referenced from CLAUDE.md, and shapes how `/validate` works. Every global type is a permanent tax on context, loaded every session whether relevant or not.

But most structural affordances are directory-local. An agent working in `notes/` doesn't need to know what sections an ADR requires. An agent working in `adr/` doesn't need to know what a related-system review looks like. The real structural expectations — what sections to write, what metadata to include, what validation to run — come from directory conventions (READMEs, templates), not from the global type field.

## Where affordances actually live

| Structural expectation | Currently defined in | Global type says |
|---|---|---|
| Core Ideas / Comparison / Borrowable Ideas | `related-systems/` README + template | `note` |
| Context / Decision / Consequences | `adr/` convention | `adr` |
| Goal / Tasks checklist / Current State | `tasks/` README | (nothing) |
| Summary / Key Claims / Relevance | `sources/` ingest pipeline | `source-review` |
| Evidence / Reasoning / Caveats | `structured-claim` template | `structured-claim` |

The global type mostly says `note` — which tells an agent almost nothing about what it can do with the document. The thick affordances are already directory-local. The global type system is paying for precision it doesn't deliver.

## Why this doesn't happen in programming

In programming, types are global (at least fully qualified names are) — and cheap. You can define a thousand types; only the ones you import are in scope. The compiler resolves references automatically. Declaration cost is near zero; resolution is free.

In an LLM context, there's no compiler and no import mechanism. Every type the agent needs to reason about must be *in the context window*. The agent either knows what `structured-claim` means because it was loaded upfront, or it doesn't. There's no `from claw.types import StructuredClaim` that pulls in the definition on demand.

So the cost difference isn't really about types being global vs local — it's about the resolution mechanism. Programming has cheap declaration + automatic resolution. LLM instructions have expensive pre-loading and no resolution at all. Directory-scoping is a workaround for this: the directory README is a primitive import mechanism. "You're in this directory; here's what types mean here." If we had real on-demand type resolution — "when you encounter `type: related-system-review`, load its definition from X" — types could be global names with on-demand definitions, just like programming.

## The economic argument

Given that we don't have automatic resolution, [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) establishes the loading hierarchy: always-loaded surfaces should be slim, task-specific detail loads on demand. The same principle applies to types:

- **Global layer:** loaded every session. Should be as thin as possible. Only types that carry affordances relevant across all directories.
- **Directory layer:** loaded when you work there (read the README, see the template). Types that carry affordances specific to that directory. Zero cost when elsewhere.

A thin global layer might be just the maturity ladder:

| Global type | What it tells an agent |
|---|---|
| `text` | No frontmatter — raw capture, always valid |
| `note` | Has frontmatter with description — searchable, connectable, validatable |

Everything else — `adr`, `source-review`, `structured-claim`, `review`, `index` — is a directory-local specialisation of `note`. An ADR is a note that lives in `adr/` and has Context/Decision/Consequences sections. A related-system review is a note that lives in `related-systems/` and has Core Ideas/Comparison/Borrowable Ideas. The directory README defines the type; the template provides the structure; validation checks against the directory's expectations.

## What moves between directories?

The orthogonality note argued that a `structured-claim` works identically in `notes/`, `claw-design/`, or anywhere. But in practice, how many documents actually move between directories? ADRs stay in `adr/`. Source reviews stay in `sources/`. Tasks stay in `tasks/`. Related-system reviews stay in `related-systems/`.

The types that genuinely move are `text` and `note` — and those are exactly the maturity ladder, not domain types. The portable types are the thin global ones. The non-portable types are the ones currently paying global cost for no global benefit.

## What this would change

**CLAUDE.md gets thinner.** The routing table stays (agents still need to know which directory to put things in). The type vocabulary shrinks to `text` vs `note` (has frontmatter or not).

**Directory READMEs become type definitions.** Each directory's README says what structure is expected, what metadata matters, what validation applies. This is already happening informally — `tasks/README.md`, `related-systems/README.md`. Making it explicit means the README *is* the type spec for that directory.

**Validation becomes directory-aware.** Instead of one global `/validate` checking all types, validation reads the directory's conventions and checks against those. The global layer validates only the universal properties (frontmatter exists, description is non-empty, links resolve).

**Templates stay where they are.** `project_claw/templates/` already provides per-type scaffolds. The change is that the template is authoritative for the directory it serves, not a convenience wrapper around a global type.

## What stays global

Some things genuinely apply everywhere:

- **Frontmatter conventions** — description, status, areas. Every note has these regardless of directory.
- **Status ladder** — seedling/current/speculative/outdated. Universal commitment tracking.
- **Link conventions** — how to link, what semantics to use. Directory-independent.
- **The text → note promotion** — adding frontmatter to a raw capture. Universal maturity step.

These are the real global affordances. They're thin — which is the point.

## Current implementation

The CLAUDE.md routing table and content workflow now implement this proposal:

- **Global types** (`types/` at repo root) define `text` and `note`. The `note` template is inlined in `kb/WRITING.md` (per [ADR-002](./adr/002-inline-global-types-in-writing-guide.md)), so the agent gets it in the same hop as writing conventions. This covers ~80% of writes.
- **Directory types** (`kb/*/types/`) are loaded only when the routing table points to a specific type. The routing table says "Default `note` type" for ordinary notes and gives an explicit file path (`kb/notes/types/adr.md`) only for specialized types. The content workflow makes this explicit: "Read the directory type — only if the routing table points to a specific type template. Skip this step for plain notes."

This is progressive disclosure applied to the type system: the agent always has `note`, and only loads `adr`, `structured-claim`, `index`, etc. when it's actually writing one.

## Open questions

- Does `structured-claim` stay global? Its template is inlined in WRITING.md alongside `note`, so in practice it loads at the same cost. But conceptually it's a specialization of `note`, not a base type.
- How does `/validate` discover directory-local expectations? Does it read the README? A machine-readable schema in the directory? Or does each directory get its own validation skill?
- What happens to the `type:` frontmatter field? Does it become just `text` vs `note`? Or does it carry the directory-local type name (`type: related-system-review`) for searchability?
- Does this make it harder to search across directories by type? `rg '^type: note'` currently finds all notes. If everything is `note`, you lose that filter. But `rg '^type: note' project_claw/notes/related-systems/` already scopes by directory.

---

Relevant Notes:
- [document classification](./document-classification.md) — the global type system this note proposes to thin out
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — foundation: the loading economy argument applies to types the same way it applies to instructions
- [why directories despite their costs](./why-directories-despite-their-costs.md) — directories already carry local conventions; this note proposes making that load-bearing for types
- [document types should be verifiable](./document-types-should-be-verifiable.md) — the verifiability principle still applies, but verification becomes directory-scoped
- [a functioning claw needs a workshop layer](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — workshop subsystems (tasks, queues) already define their own types locally; this generalises that pattern

Topics:
- [document-system](./document-system.md)
