# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**. It selects and coordinates how model-mediated and symbolic operations are used. Explicit artifacts can [activate](./kb/notes/knowledge-storage-does-not-imply-contextual-activation.md) model capabilities and give their use project authority; code and validators can [faithfully execute](./kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) operations that should not be reconstructed on every call. The doctrine, prompts, code, and models can all change. Like the Ship of Theseus, Commonplace remains the same project through a governed sequence of revisions, not because any component is permanent.

Its first application is an **LLM wiki**, in the sense [AI researcher Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer around a person's or project's work. Human-directed agents turn vague thoughts into retained notes, connect them to evidence and related claims, and revise both the knowledge base and its operating machinery.

This repository is Commonplace's current reference embodiment. It contains adopted doctrine, research and evidence that can challenge it, and the types, conventions, skills, schemas, validators, tests, and commands that make the current system operative. Research does not become doctrine merely by being stored here. This README covers the tool; the [rendered site](https://zby.github.io/commonplace/) is the main route into the research.

## Use it

### Install Commonplace in a project

Install the command-line tool once per OS user:

```bash
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

Restart the shell or agent runtime, then scaffold the current project:

```bash
commonplace-init --root .
```

Fill in the generated `AGENTS.md.template` and use it as the project's `AGENTS.md`. The installation supplies the Commonplace types, conventions, skills, and commands; the new knowledge base accumulates knowledge about its own project. The package does not include this repository's external-system reviews or source corpus. See [INSTALL.md](./INSTALL.md).

### Vendor the research read-only

To let agents consult the full research corpus without installing a Commonplace system, place this repository inside the project as a submodule, clone, or copy, then append `AGENTS.md.reader-fragment` to the project's agent instructions. Reader mode needs no Python; the agent runtime only needs file access and `rg`. See [Reader install](./INSTALL.md#reader-install-the-kb-as-a-vendored-reference).

### Develop Commonplace

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

Restart consumers of the command path. Ordinary source changes are then visible through the editable installation. After dependency, entry-point, build-metadata, or packaged-scaffold changes, reinstall with `uv tool install --reinstall --python ">=3.11" --editable .`. Run development checks with `uv run pytest` and `uv run ruff check .`. Do not run `commonplace-init` in the source checkout.

## What's in the box

```text
kb/                       Knowledge base
  notes/                  Transferable research claims and theory
  articles/               Self-standing technical explanations
  reference/              Current system documentation and ADRs
  types/                  Global artifact contracts and schemas
  instructions/           Skills, review gates, and procedures
  agent-memory-systems/   Reviews of agent-memory systems
  agentic-systems/        Reviews of agent runtimes and harnesses
  sources/                Snapshotted sources with analysis
  reports/                Operational state and retained reports
  work/                   In-flight workshops
  tasks/                  Work tracking
  log.md                  Improvement log
  index.md                Rendered-site homepage

src/commonplace/          Packaged operational engine
  cli/                    commonplace-* commands
  review/                 Review system
  lib/                    Shared runtime helpers
  docs/                   ProperDocs hooks and assets
```

## Core design choices

**Claims form a network.** Note titles are assertions, not topics, and links state how claims relate—such as `grounds`, `extends`, `contradicts`, or `exemplifies`. This makes traversal a form of reasoning rather than generic browsing. See [title as claim](./kb/notes/title-as-claim-enables-traversal-as-reasoning.md) and the [linking methodology](./kb/notes/links-README.md).

**Structure is earned progressively.** A frontmatter-free file is valid `text`. Add a description and note type when the material deserves a durable claim; specialize it further only when the extra contract enables useful operations. See the [wikiwiki principle](./kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md).

**Authored knowledge remains file-backed.** Markdown and Git provide a universal interface, versioning, diffs, and rollback. Derived indexes handle scale without replacing authored files. Review execution state is the scoped exception and lives in SQLite; see [ADR 010](./kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) and [ADR 035](./kb/reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md).

**Local contracts and revision solve different problems.** Different collections support different kinds of work, so task-specific types and link conventions stay local. Structures can also become obsolete as questions, evidence, or model capabilities change, so those local choices remain revisable. Shared invariants are reserved for constraints that survive both variation across collections and change over time. See why [task-fitted structure costs cross-task reuse](./kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md).

**Doctrine is explicit; exact operations can be symbolic.** Skills and conventions activate and authorize relevant model capabilities. Code, schemas, and validators carry operations whose behavior should not depend on repeated interpretation. Both sides remain revisable as evidence and model capabilities change.

## Research routes

**Theory-guided program modification.** Can a computational system use
fallible, project-specific theory to keep search, backtracking, and recovery
coherent under delayed feedback? The
[research program](./kb/articles/a-research-program-for-theory-guided-program-modification.md)
treats theory as search control rather than an oracle and separates the model's
computational search from the high-level selection still supplied by the
operator. Companion articles develop
[Naur's theory-bearer question](./kb/articles/what-bound-naurs-theory-to-programmers.md),
the [Bitter Lesson's scaling test](./kb/articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md),
and [why the hardest decisions stay human](./kb/articles/the-decisions-that-stay-human-and-what-would-move-them.md).

**Deployment-time learning.** Durable changes to prompts, rules, tools, schemas, tests, and code can affect later sessions without updating model weights. Storage is insufficient: later operation must load or enforce the result. Start with [retained system-definition artifacts enable persistent deployment-time adaptation](./kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and the [learning theory index](./kb/notes/learning-theory-README.md).

**Self-improving systems.** Improvement requires evidence-responsive change to the system's own behavior-determining organization. [Reflection](./kb/notes/definitions/reflective-system.md) is a separate property that supplies addressability, not improvement by itself. The [self-improving systems index](./kb/notes/self-improving-systems-README.md) maps the distinction, and [Commonplace as a reflective system](./kb/notes/evidence/commonplace-as-a-reflective-system.md) applies it locally.

**Agent-usable memory.** Agents need [discoverable, composable, and trusted knowledge under bounded context](./kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). The repository also contains reviews of [agent memory systems](./kb/agent-memory-systems/README.md) and [agentic systems](./kb/agentic-systems/README.md); the [comparative review](./kb/agent-memory-systems/agentic-memory-systems-comparative-review.md) focuses on activation and verification rather than storage alone.

## Commands, skills, and instructions

Commands are deterministic Python entry points called by name. Examples:

```bash
commonplace-validate kb/notes
commonplace-init --root .
commonplace-github-snapshot https://github.com/owner/repo/issues/123
```

The review system adds commands for selecting targets, queuing jobs, and finalizing outputs. `commonplace-x-snapshot` requires the `snapshot` package extra. See the [review system overview](./kb/reference/README-REVIEW-SYSTEM.md).

Skills (`cp-skill-*`) are agent procedures auto-loaded by compatible harnesses when a task matches their description. `commonplace-init` installs them into consuming projects.

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Write or edit an artifact under its collection and type contracts |
| `cp-skill-validate` | Validate artifacts, collection landings, and site redirects |
| `cp-skill-connect` | Discover connections and write a connect report |
| `cp-skill-convert` | Convert raw text into structured notes |
| `cp-skill-ingest` | Snapshot, connect, classify, and analyze an external source |
| `cp-skill-snapshot-web` | Capture a URL into ignored local snapshots |
| `cp-skill-ground` | Retain the minimum quotations needed to ground a source claim |
| `cp-skill-health-check` | Diagnose a broken Commonplace installation |
| `cp-skill-revise-autoreason` | Revise a note using incumbent, revision, and synthesis judging |

Instructions are Markdown procedures invoked explicitly rather than auto-loaded. They live under [`kb/instructions/`](./kb/instructions/README.md).

## Prerequisites

Reader mode needs only an agent runtime with project-file access and `rg`. The full installation uses:

| Tool | Required | Purpose |
|---|---|---|
| Agent runtime | yes | Load project instructions and expose installed skills |
| [uv](https://docs.astral.sh/uv/) | yes | Install Commonplace and run development dependencies |
| [git](https://git-scm.com/) | yes | Versioning and history-preserving relocation |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Search, frontmatter queries, and link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [Trafilatura](https://trafilatura.readthedocs.io/) | yes | Main-content HTML extraction and Markdown conversion |
| [Poppler](https://poppler.freedesktop.org/) | yes | PDF metadata and text extraction |
| [gh](https://cli.github.com/) | no | GitHub issue and PR snapshots |

## License

Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](./LICENSE-CODE)
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](./LICENSE)
