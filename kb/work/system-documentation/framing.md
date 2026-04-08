# System Documentation Workshop

## The real problem

Practitioners get commonplace as a working system — the skills, the type system, the validation, the review gates, the indexes. They also get ~150 notes containing general theory about agent systems, design patterns for agentic KBs, and this system's specific implementation choices — all mixed together.

**The core question: when reading any note, can you tell whether it's general theory or depends on local choices?**

Today you can't. A note like "instruction specificity should match loading frequency" reads as a general principle but is grounded entirely in this system's loading hierarchy. A note like "context efficiency is the central design concern" is genuinely general. A note like "directory-scoped types are cheaper than global types" is clearly system-specific. But there's no per-note signal distinguishing them.

This matters because practitioners need to know:
- Which notes describe principles they should follow regardless of their own design choices
- Which notes describe this system's choices that they might override
- Which notes do both (validate a general principle using this system as evidence)

### The documentation side

The system also needs documentation — not theory, just "how does this work." Skills, the type system, validation, review gates, the workshop layer, the linking conventions. ADRs document *decisions* but not *current state*. CLAUDE.md is a *router* for the agent, not documentation for the practitioner. Instruction files are *procedures*, not explanations.

A practitioner who installs commonplace and wants to understand how the skill system works, or how review gates compose, or what the type/trait distinction means, currently has to piece it together from scattered notes, ADRs, instruction files, and CLAUDE.md entries.

## What's needed

Two things, which may or may not be the same mechanism:

1. **A per-note signal** indicating whether a note is general theory, transferable pattern, or system-specific implementation. So a practitioner reading any note knows what they're looking at.

2. **System documentation** that explains how the installed system works — organized by subsystem (skills, types, validation, review, linking, workshop), current-state not decision-history, aimed at someone who has the system and needs to understand and extend it.

3. **A clear practitioner contract** — what's framework (mechanism the practitioner uses as-is) vs what's local (our content choices they'll replace with their own). See [practitioner-contract.md](./practitioner-contract.md). Key distinctions already identified:
   - Framework types: `note`, `text`, `index`. Everything else is our local types.
   - Validation: framework (deterministic, domain-agnostic). Review gates: mixed (some universal, some domain-specific).
   - WRITING.md: functional requirements (description-as-filter, claim titles) are framework because skills depend on them. Quality bar is practitioner-customizable.
   - Tags, directories, indexes: entirely the practitioner's vocabulary.

## Options for the per-note signal

### A. Scope trait in frontmatter

Add a `scope` value to the `traits` list: `scope-general`, `scope-pattern`, `scope-local`. Uses existing trait infrastructure (ADR-012 already separates types from traits). Filterable, validatable, visible in frontmatter.

**Cost:** Touch ~100 notes. Judgment calls on straddling notes.
**Benefit:** Any reader (human or agent) can immediately see what kind of note they're reading. Indexes can be generated from the trait.

### B. Scope field in frontmatter

Add `scope: general | pattern | local` as a dedicated field alongside `type`, `status`, `tags`.

**Cost:** New field to validate, new schema to maintain. Same classification effort as option A.
**Benefit:** Cleaner than overloading traits. First-class in the schema.

### C. Convention in description

Start descriptions with a scope marker: "[general]", "[pattern]", "[local]". No schema change.

**Cost:** Ugly, easy to forget, not machine-filterable without regex.
**Benefit:** Zero infrastructure change.

### D. Let the indexes carry the signal

Don't mark individual notes. Instead, curate scope-specific indexes that classify notes by reference. A note's scope is determined by which indexes include it and what context phrase they give it.

**Cost:** Maintain multiple indexes. Classification is distributed, not per-note.
**Benefit:** No notes touched. Straddling notes appear in multiple indexes naturally.

**Lean:** Start with D (indexes) to discover the right categorization. If it stabilizes, codify as A or B (per-note markers). This follows the progressive formalization principle.

## Options for system documentation

### I. Subsystem guide pages

One document per subsystem: skills, types/traits, validation, review gates, linking, workshop layer. Each explains current state (how it works now), links to ADRs (why), links to theory notes (the principle it instantiates).

### II. Annotated architecture overview

One document mapping all subsystems and their relationships, with links into the subsystem details. The "how does it hang together?" document.

### III. Both

The overview links to the subsystem guides. Progressive disclosure applied to documentation itself.

**Lean:** III — an overview plus subsystem guides. Start with skills (practitioners will need it first) and the type system (most complex).

## The practitioner contract for `kb/`

ADR-006 establishes the two-tree split: `kb/` is the practitioner's content, `commonplace/` is framework. But the contract for what's *inside* `kb/` is implicit. The install step creates:

```
kb/
  instructions/WRITING.md     # Copied from framework
  notes/types/                # Copied from framework
  sources/types/              # Copied from framework
  tasks/types/                # Copied from framework
  tasks/backlog/
  tasks/active/
  work/
  log.md
```

The practitioner then builds their own KB inside `kb/notes/`. **They should be able to organize it however they want.** Our `kb/notes/` has subdirectories (`adr/`, `related-systems/`, `definitions/`), indexes (`tags-index.md`, `learning-theory-index.md`), and 150+ notes — but those are *our content*, not framework structure.

### What's framework vs what's our content

| What | Framework or content? | Practitioner should... |
|------|----------------------|----------------------|
| `kb/notes/types/` | Framework (copied at install) | Keep, extend with their own types |
| `kb/instructions/WRITING.md` | Framework (copied at install) | Keep, customize the quality bar section |
| Skills (symlinked from `commonplace/`) | Framework | Use as-is, write their own additional skills |
| `kb/notes/adr/` directory | Convention (recommended, not required) | Use if they make architectural decisions |
| `kb/notes/related-systems/` | Our content | Ignore unless they're also comparing systems |
| `kb/notes/tags-index.md` | Our content | Create their own indexes for their own tags |
| `kb/notes/learning-theory-index.md` | Our content (general theory) | Read for theory, but it's not about their KB |
| `kb/log.md` | Convention (recommended) | Use for improvement logging |
| Subdirectory structure in `kb/notes/` | Their choice | Organize by topic, project, whatever fits |

### The contract, stated clearly

The framework provides **mechanism**. The practitioner provides **vocabulary and organization**.

**Framework provides (don't change these):**
- Frontmatter schema: `type`, `status`, `description`, `tags`, `traits` fields
- Type templates in `*/types/` directories (extensible — add your own types)
- Validation rules that check frontmatter, links, structure
- Skills that operate on `kb/notes/`, `kb/sources/`, `kb/tasks/`
- Review gates that assess notes against quality criteria
- `WRITING.md` conventions (customizable quality bar section)
- `log.md` as improvement log convention

**Practitioner provides (entirely theirs):**
- Which tags exist and what they mean
- Directory structure under `kb/notes/` — flat, nested by topic, by project, whatever
- Which indexes exist and how they're organized
- What their notes are about
- Custom types beyond the base set
- Their own skills

**The constraint:** skills assume top-level paths (`kb/notes/`, `kb/sources/`, `kb/tasks/`). Within those, any structure works — skills search recursively. A practitioner who puts notes in `kb/notes/payments/fraud/` doesn't break `/connect` or `/validate`. But renaming `kb/notes/` itself would.

### Implication for our notes

If `kb/` is entirely theirs, then the 150+ notes in `commonplace/kb/notes/` are a **read-only reference library** that ships with the framework — not part of the practitioner's KB. The practitioner's agent can search into `commonplace/kb/` for methodology (per ADR-006), but these notes aren't the practitioner's content.

This means the scope signal question applies specifically to `commonplace/kb/notes/`: which reference notes are general theory (useful background for any KB builder) vs framework methodology (explains how commonplace works)? A practitioner might want to read the theory but doesn't need to understand our review gate implementation details unless they're modifying the framework.

Our indexes (`tags-index.md`, `learning-theory-index.md`, etc.) are also our content — they navigate our notes. The practitioner creates their own indexes for their own tags and topics. The framework could ship an example index as a template, but not as structure they're expected to keep.

## Open questions

1. **Is it two scopes or three?** "General theory" and "local implementation" are clear poles. Is "transferable pattern" a real middle, or just general theory that happens to be validated here?

2. **What about straddling notes?** A note like "files beat a database" argues a general principle but grounds it in this system's experience. Is it `general` (the principle transfers), `local` (the grounding is system-specific), or `pattern` (the principle transfers, the evidence is local)?

3. **Should system documentation live in `kb/notes/` or `kb/instructions/`?** Instructions are imperative ("how to do X"). System docs are descriptive ("how X works"). Neither fits cleanly. Maybe a new location like `kb/docs/` or `kb/guides/`.

4. **How does this relate to the MkDocs site?** ADR-011 committed to external accessibility. Scope signals and system docs should be reflected in site navigation.

5. **What skills assume about directory structure.** If `/ingest` assumes `kb/sources/` and `/connect` assumes `kb/notes/`, these are implicit contracts. They should be documented and ideally configurable.

6. **What's the minimum viable step?** Probably: document the practitioner contract (what's framework, what's theirs, what conventions skills assume), then tag 10-15 notes in `commonplace/kb/notes/` to test the scope classification.

## Related notes

- [CLAUDE.md](../../CLAUDE.md) — current routing table
- [ADR-011: notes must be accessible to external readers](../notes/adr/011-notes-must-be-accessible-to-external-readers.md) — the commitment to external readership that makes this workshop load-bearing
- [a-good-agentic-kb-maximizes-contextual-competence](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — the theory this system instantiates
- [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — why good routing/documentation matters: every session is day one
- [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) — the methodology-is-content principle
- [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — exemplifies the straddling problem (general principle, specific instantiation)
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — the note that prompted this workshop: general theory that should be extractable for practitioners
- [synthesis-ideal-memory-system](./agent-memory-design/synthesis-ideal-memory-system.md) — possible model for practitioner-facing synthesis documents
