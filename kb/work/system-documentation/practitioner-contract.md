# Practitioner Contract

What the framework provides, what the practitioner owns, and where the boundary sits.

## The two-tree split

[ADR-006](../reference/adr/006-two-tree-installation-layout.md) establishes:

- `kb/` — the practitioner's knowledge base. Their content, their organization, their git history.
- `commonplace/` — the framework. Methodology, theory, type definitions, skills, scripts. A submodule or clone, read-only in normal use.

The install step copies a small set of operational artifacts from `commonplace/` into `kb/` for fast agent access. Everything else stays in `commonplace/` and is consulted on demand.

## What the framework provides

The framework provides **mechanism** — the machinery that makes a KB work, regardless of what it's about.

### Frontmatter schema

Every note has YAML frontmatter. The framework defines and validates these fields:

| Field | Required? | What it does |
|-------|-----------|-------------|
| `type` | Yes | Routes validation and review gates. Must match a type template in `*/types/` |
| `status` | Yes | Lifecycle stage: `seedling`, `current`, `speculative`, `outdated` |
| `description` | Yes | Retrieval filter — how the agent decides whether to load the full note |
| `tags` | No | Freeform list. Framework validates format (list of strings), not values |
| `traits` | No | Structural/review markers. Framework defines some (`has-external-sources`, `title-as-claim`); practitioner can add their own |

The framework validates *structure* (field present, correct YAML type). It does not validate *content* (which tags are allowed, what descriptions should say beyond length).

### Base types

These ship with the framework and are copied into `kb/*/types/` at install. They work for any KB:

**Current state:** the install step copies *all* type templates into the practitioner's `kb/*/types/` — every type we define, including our local ones. There is no framework/local distinction in what gets installed today.

**All types that ship today:**

| Type | Core or local? | Notes |
|------|---------------|-------|
| `note` | Core | Default structured writing type. Every KB needs this. |
| `text` | Core | No frontmatter. Raw capture. Every KB needs a low-friction entry point. |
| `index` | Core | Curated navigation hub. Tags need indexes to become navigable — without them, tags are just strings in frontmatter. |
| `structured-claim` | Local (ours) | Evidence/Reasoning/Caveats sections. Useful but not required. |
| `adr` | Local (ours) | Architecture Decision Records. Only useful if the project makes architectural decisions. |
| `related-system` | Local (ours) | External system reviews. Specific to our practice. |
| `spec` | Local (ours) | Specification documents. |
| `review` | Local (ours) | Dated reviews with findings. Tied to our review gate system. |
| `source-review` | Core | Source analysis reports. Ingestion is a basic KB operation — any KB ingests external sources. |
| `task-backlog`, `task-active`, `task-recurring` | Local (ours) | Task lifecycle types. |

**Planned change:** narrow the install to copy only core types (`note`, `text`, `index`, `source-review`). Local types would stay in `commonplace/kb/*/types/` as examples the practitioner can copy if they want them. Framework skills would depend only on core types. This separation hasn't landed yet — today everything gets copied.

### The local types pattern

Practitioners will define their own types for their domain. Examples:

- A **payments KB** might add: `incident-report`, `integration-spec`, `vendor-evaluation`, `compliance-requirement`
- A **research KB** might add: `hypothesis`, `experiment`, `literature-review`, `finding`
- A **product KB** might add: `user-story`, `design-decision`, `competitor-analysis`

To add a type, the practitioner creates two files in `kb/notes/types/`:
1. A `.yaml` file defining frontmatter requirements and validation rules
2. A `.md` file as a prose template / writing guide for that type

The framework's validation, review gates, and skills treat custom types identically to built-in types. No registration step — putting the files in `types/` is the registration.

### Skills

Framework skills live in `commonplace/skills/` and are discovered by plugin install or runtime symlinks into the agent's discovery directory. The practitioner uses them as-is and can write their own.

Skills assume top-level paths:
- `/ingest` → reads from and writes to `kb/sources/`
- `/connect` → searches `kb/notes/`
- `/validate` → checks files under `kb/`
- `/snapshot-web` → writes to `kb/sources/`

Within those top-level directories, skills search recursively. Any internal directory structure works.

### Validation and review gates

**Validation** is framework — deterministic, code-only, no LLM calls. It checks structural contracts: frontmatter present, correct YAML types, links resolve, type-specific required fields. It works on any KB that uses the frontmatter schema, regardless of content domain. Custom types get the same validation as built-in types, as long as their `.yaml` definition specifies the requirements.

**Review gates** are mixed — framework vs local. Some gates check universal prose quality that applies to any KB (redundant restatement, compound bullets, bridge paragraph duplication, internal consistency). Others check domain-specific concerns (e.g., `prose/anthropomorphic-framing` is only relevant for AI systems writing). The gate classification — which are framework-portable and which are our local gates — is an open question.

### WRITING.md

Copied from framework at install. Contains two distinct layers:

**Functional requirements** (framework — skills depend on these):
- **Description as retrieval filter, not summary.** `/connect` and other discovery skills use descriptions to decide relevance without loading full notes. If descriptions are summaries, the agent must load every note to judge relevance — defeating progressive disclosure under bounded context. This is a functional requirement, not a style preference.
- **Claim titles.** Titles that carry the argument enable traversal-as-reasoning — the agent can scan an index and build understanding from titles alone. Skills that search and connect rely on titles being informative.
- **Composability check.** "Can this note be linked without dragging irrelevant context?" ensures notes work as building blocks. Connection skills assume this.
- **Index membership.** An unconnected note is invisible to future search and traversal.

**Quality bar** (practitioner-customizable):
- What's worth a note vs a log entry depends on the domain. The template includes a section the practitioner fills in for their project — "a design decision is worth a note when it affects more than one endpoint" vs "any recipe variation worth remembering gets a note."
- Templates for specific note types. The framework ships templates for `note`; the practitioner adds templates for their custom types.

## What the practitioner provides

The practitioner provides **vocabulary and organization** — the content-specific structure that makes the KB useful for their domain.

### Tags

Entirely theirs. The framework validates that `tags` is a list of strings but doesn't constrain which strings. Our tags (`learning-theory`, `computational-model`, `tool-loop`) are about our content. A payments KB would have `fraud-detection`, `settlement`, `compliance`.

### Directory structure

Entirely theirs within the top-level collections (`kb/notes/`, `kb/sources/`, `kb/tasks/`, `kb/work/`). Flat, nested by topic, nested by team — whatever works. Skills and validation search recursively.

### Indexes

Entirely theirs. Our indexes (`tags-index.md`, `learning-theory-index.md`, `related-systems-index.md`) navigate our content. The practitioner creates their own indexes for their own tags and topics, using the `index` type template.

### Custom types

As described above. The practitioner extends the type system for their domain by adding templates to `*/types/`.

### Custom skills

The practitioner can write skills specific to their workflow. These go in their own skills directory and are symlinked into the agent runtime alongside the framework skills.

## What's in `commonplace/kb/notes/`

Our 150+ notes are a **read-only reference library** that ships with the framework. They serve two purposes:

1. **General theory** — notes about context engineering, learning theory, activation gaps, etc. Useful background for anyone building an agentic KB. The practitioner reads these for understanding.

2. **Framework methodology** — notes about how commonplace works, why certain designs were chosen, how skills are structured. Useful for understanding or extending the framework. Less relevant to practitioners who just want to use it.

The practitioner's agent can search `commonplace/kb/` for methodology (per ADR-006) but these are not the practitioner's content. They don't modify them, don't add links to them from their notes, and don't organize them.

An open question from the [workshop framing](./framing.md): should these reference notes carry a scope signal so practitioners can tell which are general theory vs framework-specific?

## Summary

| Aspect | Framework | Practitioner |
|--------|-----------|-------------|
| Frontmatter fields | Defines and validates | Uses, chooses values |
| Framework types | Ships `note`, `text`, `index`, `source-review` | Uses as base |
| Local types | Ships examples in `commonplace/` (not installed) | Defines their own, optionally copies ours |
| Tags | Validates format | Chooses vocabulary |
| Directory structure | Provides top-level collections | Organizes freely within them |
| Indexes | Ships examples in `commonplace/kb/notes/` | Creates their own |
| Skills | Ships core set | Extends with their own |
| Validation | Framework — deterministic, domain-agnostic | Gets automatic coverage for custom types |
| Review gates | Mixed — some universal, some domain-specific | May define domain-specific gates |
| WRITING.md | Ships functional requirements (description-as-filter, claim titles, composability) | Customizes quality bar for their domain |
| Theory notes | Ships as reference library | Reads, doesn't modify |
