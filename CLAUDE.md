# Commonplace

A framework for building agent-operated knowledge bases (claws). This repo contains the methodology, type definitions, writing conventions, skill templates, and scripts that get installed into projects.

The commonplace repo is itself a claw — it uses its own knowledge system to document the methodology for building claws. There is no separation between "user content" and "methodology" here; the methodology IS the content.

## Knowledge System

### Routing Table

| What you're doing | Where it goes | Type guidance |
|---|---|---|
| Design note or insight | `kb/notes/` | Default `note` type (template in `kb/WRITING.md`) |
| Structured argument | `kb/notes/` | Read `kb/notes/types/structured-claim.md` — needs Evidence/Reasoning/Caveats |
| Architecture decision | `kb/notes/adr/` | Read `kb/notes/types/adr.md` — needs Context/Decision/Consequences |
| Related system review | `kb/notes/related-systems/` | Read `kb/notes/types/related-system.md` |
| Improvement opportunity noticed during traversal | `kb/log.md` | Append one line — don't fix it now, don't context-switch |
| External source snapshot | `kb/sources/` | Use `/snapshot-web` skill |
| Source analysis | `kb/sources/` | Use `/ingest` skill — produces `.ingest.md` |
| Task | `kb/tasks/backlog/` or `kb/tasks/active/` | Status encoded by directory, not frontmatter |
| Scenario cost evaluation | `kb/scenarios/` | Read `kb/scenarios/types/scenario.md` |
| Area index (curated) | `kb/notes/` | Read `kb/notes/types/index.md` — entries MUST have context phrases |

### Content Workflow

1. **Search first** — find related notes before writing. This is especially important in this repo where the related notes ARE the methodology the new note builds on.
2. **Read WRITING.md** — `kb/WRITING.md` has the full checklist (title-as-claim, description quality, index membership, composability) and templates for `note` and `structured-claim`. It's the authority on how to write. For most notes, this is all you need.
3. **Read the directory type** — only if the routing table points to a specific type template (adr, index, related-system, scenario). Skip this step for plain notes.
4. **Write** the note.
5. **Connect** — link the new note from related notes and area indexes. Use `/connect` or do it manually. Don't skip this step — an unconnected note is invisible to future search.

### Search Patterns

```bash
# Find notes by keyword
rg "keyword" kb/notes/ --glob "*.md"

# Find notes by description
rg "^description:" kb/notes/ --glob "*.md"

# Find notes by type
rg "^type: structured-claim" kb/notes/ --glob "*.md"

# Find notes by area
rg "^areas:.*claw-design" kb/notes/ --glob "*.md"

# Find orphan notes (no inbound links)
for f in kb/notes/*.md; do
  fname=$(basename "$f")
  rg -q "$fname" --glob "*.md" kb/notes/ || echo "Orphan: $f"
done

# Find text files (no frontmatter — raw captures)
rg -L "^---" kb/notes/*.md
```

### Key Indexes

- `kb/notes/claw-design.md` — main index: foundations, observations, decisions, gaps
- `kb/notes/links.md` — linking methodology: semantics, navigation, contracts
- `kb/notes/related-systems/related-systems-index.md` — external system comparisons
- `kb/notes/index.md` — auto-generated directory listing (rebuild with `scripts/generate_notes_index.py`)
- `kb/sources/index.md` — auto-generated source listing

## Types Architecture

Types use progressive disclosure: global types cover most work; directory-scoped types load on demand only when the routing table points to them.

### Global types (`types/`) — always available

- `text` — no frontmatter, no requirements. The starting point for raw captures.
- `note` — has frontmatter with description, status, traits, areas. Templates inlined in `kb/WRITING.md`. **This is the default type for most writing — don't read directory types unless you need a specialized structure.**

### Directory-scoped types — load on demand

Each collection has a `types/` subdirectory with templates that extend `note`. Read these only when the routing table directs you to a specific type:

- `kb/notes/types/` — `structured-claim`, `adr`, `index`, `related-system`
- `kb/sources/types/` — `source-review`
- `kb/tasks/types/` — `task-active`, `task-backlog`, `task-recurring` (no frontmatter — status encoded by directory)
- `kb/scenarios/types/` — `scenario`

The base type distinction: **no frontmatter** = `text` (no requirements); **has frontmatter** = `note` or more specific type (full quality checks apply, inheriting from global `types/note.md`).

## Skills

Skills live in `skills/` and are symlinked into `.claude/skills/`. In installed projects, the symlinks point from the project's `.claude/skills/` into `commonplace/skills/`.

| Skill | Purpose |
|---|---|
| `/validate` | Schema validation — checks frontmatter, descriptions, types, links, structure |
| `/connect` | Find connections between notes, update indexes, weave knowledge graph |
| `/convert` | Convert notes between types (text→note, note→structured-claim) |
| `/ingest` | Ingest external source: snapshot → connect → classify → analyse |
| `/snapshot-web` | Capture URL to `kb/sources/` (web, GitHub, X/Twitter, PDF) |
| `/evaluate-scenarios` | Measure scenario costs — hops and instruction bytes from source files |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/generate_notes_index.py` | Regenerate directory index for a collection |
| `scripts/sync_topic_links.py` | Sync `Topics:` footer from `areas:` frontmatter |
| `scripts/github_snapshot.py` | Snapshot GitHub issues/PRs |
| `scripts/x_snapshot.py` | Snapshot X/Twitter posts |

Run scripts with `uv run scripts/<script>`.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command (`git add <files> && git commit -m "..."`). Leaving files staged without committing risks another agent's commit sweeping in unrelated changes.

## Conventions

- **Links**: Standard markdown links, not wiki-links. Relative paths from source file. `[title](./title.md)`
- **Link semantics**: Every link must articulate the relationship (extends, grounds, contradicts, enables, exemplifies). "Related" is not a relationship.
- **Filenames**: Lowercase, hyphens for spaces, `.md` extension. Derived from the `# Title` heading.
- **Frontmatter**: YAML between `---` delimiters. `description` is the most important field — it's a retrieval filter, not a summary.
- **No wiki-links**: This KB uses standard markdown links exclusively.
