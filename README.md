# Commonplace
**The theory of LLM wikis, running as one.**

Commonplace is a framework for agent-operated knowledge bases — LLM wikis in the sense [Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked markdown layer that AI agents build and maintain around your own work. It ships the type system, writing conventions, agent skills, and Python commands to run one.

A wiki is two things — notes and the links between them — and an LLM wiki is one where the agent produces both: it **concretizes** a vague thought into a committed note, then **connects** it to everything you've already written. That turns an ephemeral chat, where the insight scrolls away, into a durable, growing body of your thinking. The agent takes the two slow parts, drafting and filing. Judging whether it's _true_ still falls to you — though we're moving more of that into the agents too: critique passes, review gates, refinement loops.

It is **self-hosting**, in the bootstrapping sense. The theory of how to build LLM wikis lives in this repository as notes, and the methodology those notes lay out is executed here, not just described: LLM agents follow it to maintain the very wiki the theory lives in. The skills agents use to write, connect, and validate notes are themselves artifacts in the wiki, written and maintained the same way; the writing conventions govern the very files they are written in. Nothing here is documentation _about_ a separate system. The wiki is the system, and reading this repo is watching it run.

**The content is AI-generated** through human-AI collaboration: a human directs the inquiry, and AI agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

Rendered notes are available at <https://zby.github.io/commonplace/>. The HTML site is easier to browse than raw Markdown when reading across the KB.
## What's in the box
```
kb/                       Knowledge base
  types/                  Global types (text, note, instruction, definition, index)
  notes/                  Notes — the primary knowledge unit (theoretical register)
  reference/              Shipped-system docs and ADRs (descriptive register)
  instructions/           Framework skills, review gates, and operator procedures (prescriptive register)
  agent-memory-systems/   Reviews of external agent-memory and knowledge systems
  agentic-systems/        Reviews of external agentic systems and harnesses
  sources/                Snapshotted external sources + analysis
  reports/                Generated review, connect, and fix reports
  work/                   Workshop space — in-flight drafts and explorations
  tasks/                  Work tracking
  log.md                  Improvement log
  index.md                Top-level entry point

src/commonplace/          Packaged operational engine
  cli/                    The commonplace-* commands
  review/                 Review system
  lib/                    Shared runtime helpers
  docs/                   Rendered-site (MkDocs) hooks and assets
```
## Key ideas
**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning — [why this works](https://github.com/zby/commonplace/blob/main/kb/notes/title-as-claim-enables-traversal-as-reasoning.md).

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text`, with zero structural requirements. Add frontmatter and it becomes a `note`. A note can later take a specialized type — a `definition`, an `adr` — but only when its content earns the extra structure. Structure is earned, not imposed ([the wikiwiki principle](https://github.com/zby/commonplace/blob/main/kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).

**Files, not database.** Authored knowledge stays file-backed: universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth. The current scoped exception is the experimental review system, which stores review state in SQLite because that state behaves like local operational metadata rather than library content; see [ADR 010](https://github.com/zby/commonplace/blob/main/kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md).

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible ([linking methodology](https://github.com/zby/commonplace/blob/main/kb/notes/links-README.md)).

**Externalized methodology.** The procedures for working the wiki — how to write a note, connect it, validate it — are written down as skills and conventions, not baked into a particular model or assistant. Every agent reads them fresh, so a different model, or a new session, produces consistent work: the manual is on disk, not in the weights.
## Skills, instructions, and commands
Commonplace gives agents three kinds of operative artifact.

**Commands** (`commonplace-*`) are the Python CLI — deterministic operations called by name. Install the package, then:

```bash
commonplace-validate kb/notes        # check frontmatter, types, links, structure
commonplace-init                     # scaffold Commonplace into a project
commonplace-github-snapshot <url>    # snapshot a GitHub issue/PR into kb/sources/
commonplace-x-snapshot <url>         # snapshot an X/Twitter thread
```

The review system ships as a further family of `commonplace-*` commands; see the [review system overview](https://github.com/zby/commonplace/blob/main/kb/reference/REVIEW-SYSTEM.md).

**Skills** (`cp-skill-*`) are agent procedures the harness auto-loads from their descriptions: when a task matches a skill, the agent invokes it. `commonplace-init` installs them into a consuming project.

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Route and draft a note, index, or specialized type |
| `cp-skill-validate` | Check frontmatter, descriptions, types, links, structure |
| `cp-skill-connect` | Discover connections and write a `connect-report` |
| `cp-skill-convert` | Convert raw text captures into structured notes |
| `cp-skill-ingest` | Ingest an external source: snapshot → connect → classify → analyse |
| `cp-skill-snapshot-web` | Capture a URL into `kb/sources/` |
| `cp-skill-health-check` | Diagnose a broken Commonplace install |
| `cp-skill-revise-iterative` | Iteratively revise a note without changing its claims |
| `cp-skill-revise-autoreason` | Revise a note with AutoReason-style incumbent/revision/synthesis judging |

**Instructions** are the same kind of artifact as skills — procedures written in Markdown — but without the description-based auto-loading. They are invoked explicitly — by the user, or by another skill — and live under `kb/instructions/`.
## Content workflow
### Reading
Search the KB, read matching notes, follow links to deepen understanding. Link semantics (extends, grounds, contradicts) help the agent decide which connections are worth following. Good descriptions act as retrieval filters — they discriminate between similar notes so the agent reads fewer irrelevant ones.
### Writing
The agent retrieves related notes first, reads the target collection's `COLLECTION.md` to match its conventions and quality bar, then writes the note ([`cp-skill-write`](https://github.com/zby/commonplace/blob/main/kb/instructions/cp-skill-write/SKILL.md)).

**Connecting** is a separate step: link the new note from related notes and indexes ([`cp-skill-connect`](https://github.com/zby/commonplace/blob/main/kb/instructions/cp-skill-connect/SKILL.md)). An unconnected note is invisible to future search, so it is not optional.
## Usage
### Direct use (this repo)
Clone the repo and start working. The repo is a functioning knowledge base out of the box — skills, types, writing conventions, and methodology are all in place.

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
```

If you use `direnv`, make sure your shell has the direnv hook installed, then run `direnv allow` once after entering the repo. The `.envrc` sets `PATH` and `UV_CACHE_DIR` for the project. Start Codex or Claude Code from that direnv-loaded interactive shell so the runtime inherits the project venv; otherwise launch it with `direnv exec . <command>`.

The `kb/` directory is both the methodology and your workspace — new notes go alongside the existing ones, and the root `AGENTS.md` provides the project routing layer.

This is the right mode when:

- You want to explore or contribute to the Commonplace methodology itself
  
- You want a standalone knowledge base without attaching it to another project
  
- You're evaluating the system before installing it elsewhere
  
### Installing into a project
Commonplace can be installed into any project as a Python package. See [**INSTALL.md**](https://github.com/zby/commonplace/blob/main/INSTALL.md) for the setup flow.
## Prerequisites
| Tool | Required | Purpose |
| --- | --- | --- |
| Agent runtime | yes | Codex, Claude Code, or another internal LLM/IDE that can load project instructions and expose the `cp-skill-*` skill directories |
| [uv](https://docs.astral.sh/uv/) | yes | Install and run the Commonplace Python package |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [gh](https://cli.github.com/) | no  | GitHub issue/PR snapshots in `snapshot-web` and `commonplace-github-snapshot` |
## License
Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](https://github.com/zby/commonplace/blob/main/LICENSE-CODE)
  
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](https://github.com/zby/commonplace/blob/main/LICENSE)
