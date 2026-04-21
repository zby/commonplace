# Commonplace

A knowledge base about building agentic systems — how AI agents learn, operate, and improve through inspectable artifacts. An agent-operated knowledge base is the primary testbed: the repo uses its own methodology to document the theory, and ships the framework (type system, writing conventions, skills, and Python commands) for building more.

**The content is AI-generated** through human-AI collaboration: a human directs the inquiry, and AI agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

## What's in the box

```
kb/                          Knowledge base
  types/                     Global types (text, note, instruction, definition, index)
  notes/COLLECTION.md         Writing conventions (theoretical register)
  reference/COLLECTION.md     Writing conventions (descriptive register)
  instructions/COLLECTION.md  Writing conventions (prescriptive register)
  log.md                     Improvement log — one-line observations appended during traversal
  notes/                     Notes — the primary knowledge unit
    types/                   Note-local type templates (structured-claim)
    adr/                     Architecture Decision Records
    related-systems/         External system comparisons
  sources/                   Snapshotted external sources + analysis
  tasks/                     Work tracking (status encoded by directory)
  work/                      Workshop space — connect reports, ingest staging, explorations
  instructions/              Framework skills, local procedures, and operator guidance
    write/SKILL.md           Promoted framework skill source
    connect/SKILL.md         Promoted framework skill source
    ingest/SKILL.md          Promoted framework skill source
    evaluate-scenarios/SKILL.md  Measure scenario costs
    re-ingest.md             Instruction (not yet promoted to skill)
    review-gates/            Review gates grouped by bundle/lens name (e.g. semantic/)
    ...

test/
  scenarios/                 Scenario fixtures for cost decomposition and evaluation

src/commonplace/             Packaged operational engine
  cli/                       User-facing commands
  review/                    Review system commands + support modules
  lib/                       Shared runtime helpers
  docs/                      MkDocs hooks and documentation assets
```

## Key ideas

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning.

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text` type with zero structural requirements. Add frontmatter to make it a `note`. Add Evidence/Reasoning/Caveats sections to make it a `structured-claim`. Structure is earned, not imposed.

**Files, not database.** Authored knowledge stays file-backed: universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth. The current scoped exception is the experimental review system, which stores review state in SQLite because that state behaves like local operational metadata rather than library content; see [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md).

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible.

**Externalized methodology.** Knowledge accumulates in the KB, but the procedures for working with it — how to write, connect, validate — live in skills and docs, not in the agent's head. The agent reads them fresh every time. The KB is the memory; the skills are the manual.

## Skills and instructions

Framework skills are sourced from `kb/instructions/` and promoted by `commonplace-init` into `.claude/skills/` and `.agents/skills/` with a `cp-skill-` prefix. The prefix keeps them distinct from both a project's own skills and the `commonplace-*` CLI commands. Plain KB procedures remain under `kb/instructions/` and load on demand. The project control-plane file (`CLAUDE.md` or `AGENTS.md`) still handles KB discovery and scoping.

Framework skills:

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Route and draft a note, index, or discovered specialized type |
| `cp-skill-validate` | Check frontmatter, descriptions, types, links, structure |
| `cp-skill-connect` | Discover connections and write a `connect-report` artifact |
| `cp-skill-convert` | Convert notes between types (text → note → structured-claim) |
| `cp-skill-ingest` | Ingest external source: snapshot → connect → classify → analyse |
| `cp-skill-snapshot-web` | Capture a URL to `kb/sources/` |
| `cp-skill-revise-iterative` | Iteratively revise a note without changing its claims |
| `cp-skill-revise-autoreason` | Revise a note with AutoReason-style incumbent/revision/synthesis judging |

Repo-local skills and procedures remain under `kb/instructions/`. Examples:
- `evaluate-scenarios` — scenario-cost measurement for this repo's methodology work
- Agent-memory-system reviews are handled by writing with the `agent-memory-system-review` type — workflow in `kb/agent-memory-systems/types/agent-memory-system-review.md`

## Content workflow

### Reading

Search the KB, read matching notes, follow links to deepen understanding. Link semantics (extends, grounds, contradicts) help the agent decide which connections are worth following. Good descriptions act as retrieval filters — they discriminate between similar notes so the agent reads fewer irrelevant ones.

### Writing

1. **Search first** — find related notes before writing
2. **Read the target collection's `COLLECTION.md`** — each collection has its own writing conventions, quality goals, and default templates. For notes, read `kb/notes/COLLECTION.md`.
3. **Read the directory type** — only if you're writing a specialized type (adr, index, related-system, or scenario in `test/scenarios/`). Skip this step for plain notes.
4. **Write** the note
5. **Connect** — link the new note from related notes and indexes. Use the `cp-skill-connect` skill or do it manually. Don't skip this — an unconnected note is invisible to future search.

## Usage

### Direct use (this repo)

Clone the repo and start working. The repo is a functioning knowledge base out of the box — skills, types, writing conventions, and methodology are all in place.

```bash
git clone https://github.com/anthropics/commonplace.git
cd commonplace
```

If you use `direnv`, run `direnv allow` once after entering the repo. The `.envrc` sets `PATH` and `UV_CACHE_DIR` for the project.

Skills are installed into `.claude/skills/cp-skill-*/` and `.agents/skills/cp-skill-*/` by `commonplace-init`. The root `AGENTS.md` provides the project routing layer. The `kb/` directory is both the methodology and your workspace — new notes go alongside the existing ones.

This is the right mode when:
- You want to explore or contribute to the commonplace methodology itself
- You want a standalone knowledge base without attaching it to another project
- You're evaluating the system before installing it elsewhere

### Installing into a project

Commonplace can be installed into any project as a Python package. See **[INSTALL.md](INSTALL.md)** for the setup flow.

## Prerequisites

| Tool | Required | Purpose |
|---|---|---|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or Codex | yes | Agent runtime — use the runtime's skill surface plus `AGENTS.md` |
| [uv](https://docs.astral.sh/uv/) | yes | Install and run the Commonplace Python package |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [gh](https://cli.github.com/) | no | GitHub issue/PR snapshots in `snapshot-web` and `commonplace-github-snapshot` |

## Commands

Install the package first, then use the commands directly:

```bash
commonplace-generate-notes-index kb/notes
commonplace-relocate-note old-note "New note title" --apply
commonplace-relocate-note old-note --dir kb/notes/definitions --apply
commonplace-github-snapshot <url>
commonplace-x-snapshot <url>
```

## License

[CC BY 4.0](LICENSE)
