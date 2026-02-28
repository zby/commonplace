# Commonplace

Reactive team knowledge system — OpenClaw with WikiWiki spirit.

Commonplace provides the methodology, type system, writing conventions, skills, and scripts that let an agent autonomously navigate, extend, and maintain a structured knowledge base of markdown files.

This repo is itself a commonplace knowledge base. It uses its own knowledge system to document the methodology for building them. The methodology IS the content.

## What's in the box

```
types/                       Global types (text, note)

kb/                          Knowledge base
  WRITING.md                 Writing conventions and quality checklist
  notes/                     Notes — the primary knowledge unit
    types/                   Note type templates (structured-claim, adr, index, ...)
    adr/                     Architecture Decision Records
    agent-learnings/         Observations agents make during work
    related-systems/         External system comparisons
  sources/                   Snapshotted external sources + analysis
  tasks/                     Work tracking (status encoded by directory)
  scenarios/                 Concrete use cases with cost decomposition

skills/                      Agent skills (Claude Code slash commands)
  validate/                  Schema and quality validation
  connect/                   Find connections, weave knowledge graph
  convert/                   Convert notes between types
  ingest/                    Ingest external sources
  snapshot-web/              Capture URLs to markdown
  evaluate-scenarios/        Measure scenario costs

scripts/                     Standalone automation
  generate_notes_index.py    Regenerate directory indexes
  sync_topic_links.py        Sync areas ↔ topics frontmatter
  github_snapshot.py         Snapshot GitHub issues/PRs
  x_snapshot.py              Snapshot X/Twitter posts
```

## Key ideas

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning.

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text` type with zero structural requirements. Add frontmatter to make it a `note`. Add Evidence/Reasoning/Caveats sections to make it a `structured-claim`. Structure is earned, not imposed.

**Files, not database.** Universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth.

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible.

**Externalized methodology.** Knowledge accumulates in the KB, but the procedures for working with it — how to write, connect, validate — live in skills and docs, not in the agent's head. The agent reads them fresh every time. The KB is the memory; the skills are the manual.

## Skills

Skills are invoked as slash commands in Claude Code:

| Skill | Purpose |
|---|---|
| `/validate` | Check frontmatter, descriptions, types, links, structure |
| `/connect` | Find connections between notes, update indexes |
| `/convert` | Convert notes between types (text → note → structured-claim) |
| `/ingest` | Ingest external source: snapshot → connect → classify → analyse |
| `/snapshot-web` | Capture a URL to `kb/sources/` |
| `/evaluate-scenarios` | Measure scenario costs in hops and instruction bytes |

## Content workflow

### Reading

Search the KB, read matching notes, follow links to deepen understanding. Link semantics (extends, grounds, contradicts) help the agent decide which connections are worth following. Good descriptions act as retrieval filters — they discriminate between similar notes so the agent reads fewer irrelevant ones.

### Writing

1. **Search first** — find related notes before writing
2. **Read `kb/WRITING.md`** — it's the authority on how to write, and includes templates for `note` and `structured-claim`. For most notes, this is all you need.
3. **Read the directory type** — only if you're writing a specialized type (adr, index, related-system, scenario). Skip this step for plain notes.
4. **Write** the note
5. **Connect** — link the new note from related notes and indexes. Use `/connect` or do it manually. Don't skip this — an unconnected note is invisible to future search.

## Usage

### Direct use (this repo)

Clone the repo and start working. The repo is a functioning knowledge base out of the box — skills, types, writing conventions, and methodology are all in place.

```bash
git clone https://github.com/anthropics/commonplace.git
cd commonplace
```

The `.claude/skills/` directory contains symlinks to `skills/`, so Claude Code picks up all slash commands automatically. The `kb/` directory is both the methodology and your workspace — new notes go alongside the existing ones.

This is the right mode when:
- You want to explore or contribute to the commonplace methodology itself
- You want a standalone knowledge base without attaching it to another project
- You're evaluating the system before installing it elsewhere

### Installing into a project

Commonplace can be installed into an existing project as a submodule or cloned subdirectory. This creates a two-tree layout: your content lives in `kb/` at the project root, while the framework lives in `commonplace/`. Operational artifacts (`types/`, `WRITING.md`) are copied into your `kb/` for fast access; methodology notes stay in `commonplace/` and are consulted on demand.

**1. Add commonplace to your project:**

```bash
# Option A: git submodule (versioned, reproducible)
git submodule add https://github.com/anthropics/commonplace.git commonplace

# Option B: clone + gitignore (simpler)
git clone https://github.com/anthropics/commonplace.git commonplace
echo "commonplace/" >> .gitignore
```

**2. Create the kb/ directory structure and copy operational artifacts:**

```bash
# Create directories
mkdir -p types kb/notes/types kb/notes/agent-learnings kb/sources/types kb/tasks/types kb/tasks/backlog kb/tasks/active

# Copy operational artifacts
cp commonplace/kb/WRITING.md kb/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/
cp commonplace/kb/tasks/types/* kb/tasks/types/
```

**3. Symlink skills into `.claude/skills/`:**

```bash
mkdir -p .claude/skills
for skill in commonplace/skills/*/; do
  name=$(basename "$skill")
  ln -sfn "../../commonplace/skills/$name" ".claude/skills/$name"
done
```

**4. Add a Knowledge System section to your project's `CLAUDE.md`** with a routing table and search patterns. See `commonplace-installation-architecture.md` for the full fragment design.

The resulting layout:

```
my-project/
  kb/                        Your content
    WRITING.md               Copied from commonplace
    notes/
      types/                 Copied from commonplace
    sources/
    tasks/
  commonplace/               Framework (submodule or clone)
  .claude/skills/            Symlinked → commonplace/skills/
  CLAUDE.md                  Routing table + commonplace reference
```

**Updating:** pull new changes (`git submodule update --remote` or `cd commonplace && git pull`), then re-copy operational artifacts. Commonplace-provided type files are replaced; any custom types you've added are left untouched.

See `commonplace-installation-architecture.md` for the full design rationale.

## Prerequisites

| Tool | Required | Purpose |
|---|---|---|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | yes | Agent runtime — skills are Claude Code slash commands |
| [uv](https://docs.astral.sh/uv/) | yes | Python script runner — `uv run` handles dependencies automatically |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `/convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `/snapshot-web` |
| [gh](https://cli.github.com/) | no | GitHub issue/PR snapshots in `/snapshot-web` and `github_snapshot.py` |
| [qmd](https://github.com/qmdnotes/qmd) | no | Semantic search — hybrid BM25 + vector + reranking. Skills degrade gracefully to grep-only when unavailable |

### Setting up qmd

qmd adds semantic search — it finds notes by meaning, not just keywords. Without it, skills fall back to ripgrep, which works but misses vocabulary mismatches (e.g. searching for "modularity" won't find a note about "composability").

1. [Install qmd](https://github.com/qmdnotes/qmd) and ensure it's on your PATH.

2. Copy the collection config:

```bash
cp scripts/qmd-collections.yml ~/.config/qmd/commonplace.yml
```

3. Build the index:

```bash
qmd --index commonplace update && qmd --index commonplace embed
```

4. Search:

```bash
qmd --index commonplace query "your search terms"
```

After adding or editing notes, re-run `qmd --index commonplace update && qmd --index commonplace embed` to keep the index current. Both commands are idempotent and fast.

For installed projects, create a project-specific config (e.g. `~/.config/qmd/my-project.yml`) pointing to your project's `kb/` directories.

## Scripts

Scripts require uv. Dependencies are declared in `pyproject.toml` — `uv run` installs them automatically on first use.

```bash
uv run scripts/generate_notes_index.py kb/notes   # Rebuild directory index
uv run scripts/sync_topic_links.py kb/notes/       # Sync areas ↔ topics
uv run scripts/github_snapshot.py <url>             # Snapshot a GitHub issue/PR
uv run scripts/x_snapshot.py <url>                  # Snapshot an X/Twitter post
```

## License

[CC BY 4.0](LICENSE)
