# Practitioner Contract

What the framework provides, what the practitioner owns, and where the boundary sits.

## The two-tree split

[ADR-006](../notes/adr/006-two-tree-installation-layout.md) establishes:

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

**Notes collection (`kb/notes/types/`):**

| Type | What it's for | Framework or local? |
|------|--------------|-------------------|
| `note` | Default structured writing type. Has frontmatter, claim title, description. | Framework — every KB needs this |
| `text` | No frontmatter. Raw capture, pre-formalization. | Framework — every KB needs a low-friction entry point |
| `structured-claim` | Evidence/Reasoning/Caveats sections. For claims that need explicit argumentation. | Framework — transferable pattern for any KB that makes arguments |
| `index` | Curated navigation hub. Entries must have context phrases. | Framework — every KB needs navigation |
| `adr` | Architecture Decision Record. Context/Decision/Consequences. | Local to us — only useful if your project makes architectural decisions. A cooking KB wouldn't need this. |
| `related-system` | External system review with structured comparison. | Local to us — specific to our practice of reviewing comparable systems. A payments KB would define `vendor-evaluation` instead. |
| `spec` | Specification document. | Framework — transferable, though many KBs won't need it |
| `review` | Dated review with findings. | Local to us — tied to our review gate system |

**Sources collection (`kb/sources/types/`):**
| Type | Framework or local? |
|------|-------------------|
| `source-review` | Framework — any KB that ingests external sources needs a review type |

**Tasks collection (`kb/tasks/types/`):**
| Type | Framework or local? |
|------|-------------------|
| `task-backlog`, `task-active`, `task-recurring` | Framework — basic task lifecycle, applicable to any KB |

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

Skills are executable operations symlinked from `commonplace/kb/instructions/` into the agent runtime's discovery directory. The practitioner uses them as-is and can write their own.

Skills assume top-level paths:
- `/ingest` → reads from and writes to `kb/sources/`
- `/connect` → searches `kb/notes/`
- `/validate` → checks files under `kb/`
- `/snapshot-web` → writes to `kb/sources/`

Within those top-level directories, skills search recursively. Any internal directory structure works.

### Validation and review gates

Validation checks structural contracts (frontmatter present, links resolve, type-specific requirements met). Review gates check semantic quality (grounding alignment, confidence calibration, internal consistency, etc.).

Both operate on whatever types exist in `*/types/`. Custom types get the same validation and review treatment as built-in types, as long as their `.yaml` definition specifies the requirements.

### WRITING.md

Copied from framework at install. Contains the writing checklist (claim titles, description quality, composability, index membership) and templates for `note` and `structured-claim`.

The practitioner should customize the **Quality bar** section for their domain — what's worth a note vs a log entry depends on the project.

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
| Base types | Ships `note`, `text`, `structured-claim`, `index`, `spec`, task types | Adds domain-specific types |
| Local types | Ships `adr`, `related-system`, `review` (examples, not required) | Defines their own |
| Tags | Validates format | Chooses vocabulary |
| Directory structure | Provides top-level collections | Organizes freely within them |
| Indexes | Ships examples in `commonplace/kb/notes/` | Creates their own |
| Skills | Ships core set | Extends with their own |
| Validation & review | Provides machinery | Gets automatic coverage for custom types |
| WRITING.md | Ships template | Customizes quality bar |
| Theory notes | Ships as reference library | Reads, doesn't modify |
