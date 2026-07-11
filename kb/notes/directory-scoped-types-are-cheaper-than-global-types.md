---
description: Global types tax every session's context; directory-scoped types load only when working in that directory — most structural affordances are directory-local, so the type system should match that economy
type: kb/types/note.md
traits: [title-as-claim]
tags: [type-system]
---

# Directory-scoped types are cheaper than global types

A global type system taxes every session's context. Every type an agent might encounter must be in the context window, because there's no compiler or import mechanism to load definitions on demand. Making every type global means paying the load cost every session whether the type is relevant or not.

But most structural affordances are directory-local. An agent working in a notes area doesn't need to know what sections an ADR requires. An agent working in an ADR directory doesn't need to know what a related-system review looks like. The real structural expectations — what sections to write, what metadata to include, what validation to run — come from directory conventions (READMEs, templates), not from a global type name.

The global type name mostly tells an agent "this is a structured document" — which is useful, but thin. The thick affordances live next to the documents they describe. A type system that ignores this ends up paying global cost for precision it doesn't deliver.

## Why this doesn't happen in programming

In programming, types are global (at least fully qualified names are) — and cheap. You can define a thousand types; only the ones you import are in scope. The compiler resolves references automatically. Declaration cost is near zero; resolution is free.

In an LLM context, there's no compiler and no import mechanism. Every type the agent needs to reason about must be *in the context window*. The agent either knows what a given type means because it was loaded upfront, or it doesn't. There's no `from kb.types import StructuredClaim` that pulls in the definition on demand.

So the cost difference isn't really about types being global vs local — it's about the resolution mechanism. Programming has cheap declaration + automatic resolution. LLM instructions have expensive pre-loading and no resolution at all. Directory scoping is a workaround for this: the directory's conventions are a primitive import mechanism. "You're in this directory; here's what types mean here." If we had real on-demand type resolution — "when you encounter this type name, load its definition from X" — types could be global names with on-demand definitions, just like programming.

## The economic argument

Given that there's no automatic resolution, [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) establishes the loading hierarchy: always-loaded surfaces should be slim, task-specific detail loads on demand. The same principle applies to types:

- **Global layer:** loaded every session. Should be as thin as possible. Only types that carry affordances relevant across every directory.
- **Directory layer:** loaded when you work there (read the README, read the template). Types that carry affordances specific to that directory. Zero cost when elsewhere.

A thin global layer might be just the maturity ladder:

| Global type | What it tells an agent |
|---|---|
| `text` | No frontmatter — raw capture, always valid |
| `note` | Has frontmatter with description — searchable, connectable, validatable |

Everything else — ADRs, source reviews, structured claims, reviews, indexes — is plausibly a directory-local specialisation of `note`. A specialised type is a note that lives in a specific directory and has a specific section structure. The directory's template defines the structure; validation checks against the directory's expectations.

## What moves between directories?

An argument against directory scoping is that it prevents types from being portable. But in practice, how many documents actually move between directories? ADRs stay with their decisions. Source reviews stay in the source-review collection. Tasks stay in the task tree. Related-system reviews stay in the related-systems area.

The types that genuinely move are `text` and `note` — and those are exactly the maturity ladder, not domain types. The portable types are the thin global ones. The non-portable types are the ones currently paying global cost for no global benefit.

## What this would change

**The control-plane file gets thinner.** The routing table stays (agents still need to know which directory to put things in). The global type vocabulary shrinks to `text` vs `note` (has frontmatter or not).

**Directory READMEs and templates become the type definitions.** Each directory's conventions say what structure is expected, what metadata matters, what validation applies. This is already happening informally in any KB with collection-level READMEs; making it explicit means the README *is* the type spec for that directory.

**Validation becomes directory-aware.** Instead of one global validator checking all types, validation reads the directory's conventions and checks against those. The global layer validates only the universal properties (frontmatter exists, description is non-empty, links resolve).

**Templates stay where they are.** A per-directory `types/` folder already provides per-type scaffolds. The change is that the template is authoritative for the directory it serves, not a convenience wrapper around a global type.

## What stays global

Some things genuinely apply everywhere:

- **Frontmatter conventions** — description, status, tags. Every note has these regardless of directory.
- **Status ladder** — seedling/current/speculative/outdated. Universal commitment tracking.
- **Link conventions** — how to link, what semantics to use. Directory-independent.
- **The text → note promotion** — adding frontmatter to a raw capture. Universal maturity step.

These are the real global affordances. They're thin — which is the point.

---

Relevant Notes:

- [type-loading](../reference/type-loading.md) — current-state: how Commonplace instantiates the thin-global, directory-scoped split today, including which types live in `kb/types/` vs `kb/*/types/`
- [type-system](../reference/available-types.md) — current-state: the full Commonplace type inventory this argument thins out
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — foundation: the loading economy argument applies to types the same way it applies to instructions
- [why directories despite their costs](./why-directories-despite-their-costs.md) — directories already carry local conventions; this note proposes making that load-bearing for types
- [document types should be verifiable](./document-types-should-be-verifiable.md) — the verifiability principle still applies, but verification becomes directory-scoped
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — workshop subsystems (tasks, queues) already define their own types locally; this generalises that pattern
