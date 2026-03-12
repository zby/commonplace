# Commonplace

A framework for building agent-operated knowledge bases. This repo contains the methodology, type definitions, writing conventions, instructions and skills, and scripts that get installed into projects.

The commonplace repo is itself a knowledge base — it uses its own knowledge system to document the methodology for building knowledge bases. There is no separation between "user content" and "methodology" here; the methodology IS the content.

## Fast Path (Default)

If you need to act quickly and are unsure which specialized path applies, do this:

1. Write a `note` in `kb/notes/` (default type).
2. Follow the checklist/template in `kb/instructions/WRITING.md`.
3. Connect the note to related notes and at least one index (`/connect` or manual links with explicit relationship semantics).
4. Run `/validate` to check structure, frontmatter, and links.

Use specialized types only when the routing table explicitly points to one.

## Knowledge System

### Routing Table

| What you're doing | Where it goes | Type guidance |
|---|---|---|
| Design note or insight | `kb/notes/` | Default `note` type (template in `kb/instructions/WRITING.md`) |
| Structured argument | `kb/notes/` | Read `kb/notes/types/structured-claim.md` — needs Evidence/Reasoning/Caveats |
| Architecture decision | `kb/notes/adr/` | Read `kb/notes/types/adr.md` — needs Context/Decision/Consequences |
| Related system review | `kb/notes/related-systems/` | Read `kb/notes/types/related-system.md` |
| Improvement opportunity noticed during traversal | `kb/log.md` | Append one line — don't fix it now, don't context-switch |
| External source snapshot | `kb/sources/` | Use `/snapshot-web` skill |
| Source analysis | `kb/sources/` | Use `/ingest` skill — produces `.ingest.md` |
| Task | `kb/tasks/backlog/` or `kb/tasks/active/` | Status encoded by directory, not frontmatter |
| Reusable procedure | `kb/instructions/` | Imperative steps, frontloaded, minimal reasoning |
| Area index (curated) | `kb/notes/` | Read `kb/notes/types/index.md` — entries MUST have context phrases |

### Content Workflow

1. **Search first** — find related notes before writing. This is especially important in this repo where the related notes ARE the methodology the new note builds on.
2. **Read WRITING.md** — `kb/instructions/WRITING.md` has the full checklist (title-as-claim, description quality, index membership, composability) and templates for `note` and `structured-claim`. It's the authority on how to write. For most notes, this is all you need.
3. **Read the directory type** — only if the routing table points to a specific type template (adr, index, related-system). Skip this step for plain notes.
4. **Write** the note.
5. **Connect** — link the new note from related notes and area indexes. Use `/connect` or do it manually. Don't skip this step — an unconnected note is invisible to future search.

### Search Patterns (Core)

```bash
# Find notes by keyword
rg "keyword" kb/notes/ kb/instructions/ --glob "*.md"

# Find notes by description
rg "^description:" kb/notes/ kb/instructions/ --glob "*.md"

# Find notes by type
rg "^type: structured-claim" kb/notes/ kb/instructions/ --glob "*.md"

# Find notes by area
rg "^areas:.*kb-design" kb/notes/ kb/instructions/ --glob "*.md"
```

Use `/validate` for specialized audits and consistency checks.

### Escalation Boundaries

Stop and load deeper guidance when any of these are true:

- You cannot map the artifact cleanly through the routing table -> read `kb/instructions/WRITING.md` before creating or moving files.
- You are editing notes in a directory with a local `types/` template -> read that template first.
- You touch `kb/sources/` content and there is no corresponding `.ingest.md` -> run `/ingest` (or ask the user which ingest workflow to use) instead of improvising classification.
- The task is an externally triggered operation class (maintenance sweep, audit, bulk refactor) -> use the operations catalogue/instructions path, not the default AGENTS flow.

This file is a control-plane router. It does not inventory capabilities; harness-injected skills provide capability discovery.

### Key Indexes

- `kb/notes/kb-design.md` — main index: foundations, observations, decisions, gaps
- `kb/notes/links.md` — linking methodology: semantics, navigation, contracts
- `kb/notes/related-systems/related-systems-index.md` — external system comparisons
- `kb/notes/index.md` — auto-generated directory listing (rebuild with `scripts/generate_notes_index.py`)
- `kb/sources/index.md` — auto-generated source listing

## Type Routing

- `text` = no frontmatter (raw capture).
- `note` = has frontmatter (default structured writing type).
- For specialized structures, load the directory-local type templates only when the routing table points there:
  `kb/notes/types/`, `kb/sources/types/`, `kb/tasks/types/`.
- `kb/instructions/WRITING.md` is the authority for note-writing checklist and the default templates.

## Vocabulary

Terms used in this KB with specific meanings:

- **Distillation** — targeted extraction from a larger body of reasoning into a focused artifact shaped by specific circumstances (use case, context budget, agent). Not ML knowledge distillation (training a student model to mimic a teacher). Here it means: take knowledge, optimize it for a specific consumer facing a specific task, produce a text artifact. Examples: methodology → skill, accumulated understanding → campaign narrative, caller's knowledge → refined sub-agent prompt. See `kb/notes/distillation.md`.
- **Constraining** — narrowing the interpretation space of an artifact (less generality, more reliability/speed/cost). Orthogonal to distillation. See `kb/notes/constraining.md`.
- **Codification** — committing a procedure to a symbolic medium (natural language → code). The far end of constraining. See `kb/notes/codification.md`.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command (`git add <files> && git commit -m "..."`). Leaving files staged without committing risks another agent's commit sweeping in unrelated changes.

## Conventions

- **Links**: Standard markdown links, not wiki-links. Relative paths from source file. `[title](./title.md)`
- **Link semantics**: Every link must articulate the relationship (extends, grounds, contradicts, enables, exemplifies). "Related" is not a relationship.
- **Filenames**: Lowercase, hyphens for spaces, `.md` extension. Derived from the `# Title` heading.
- **Frontmatter**: YAML between `---` delimiters. `description` is the most important field — it's a retrieval filter, not a summary.
- **No wiki-links**: This KB uses standard markdown links exclusively.
