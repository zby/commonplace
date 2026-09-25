# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

It has two goals. The practical one is an **LLM wiki**, in the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer in which agents, directed by people, turn a person's or project's work into retained, connected notes. The theoretical one is a new learning paradigm, the **theory builder**: a system that states theories, acts on them, criticizes them, and keeps what criticism shows for the next round, following Karl Popper's method of conjecture and criticism. We bet that a fully automated theory builder that learns can be built with today's LLMs, their weights held fixed. No test of the bet has been run yet.

The goals reinforce each other, because memory is always about learning: a note is worth something when it changes what the system does next. Theories that are acted on, criticized, and revised are what make a wiki learn, and [real use of the wiki supplies the problems and criticism](./kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) a theory builder learns from.

[Reflection](./kb/notes/definitions/theory-builder.md#qualifiers) is the core of the method. Commonplace's doctrine, how it writes, connects, and revises notes, is one of the theories it criticizes and revises, so [an improvement to the method is reused by all later work](./kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

This repository holds the adopted doctrine, research and evidence that can challenge it, and the tool: the types, conventions, skills, schemas, validators, tests, and commands that you can install to build a knowledge base of the same kind in your own project. Research does not become doctrine merely by being stored here. This README covers the tool; the research routes below point into the rest.

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

Fill in the generated `AGENTS.md.template` and use it as the project's `AGENTS.md`, and rename `CLAUDE.md.template` to `CLAUDE.md`. The installation supplies the Commonplace types, conventions, skills, and commands, which the project reads in place from the installed package rather than copying; the new knowledge base accumulates knowledge about its own project. The package does not include this repository's external-system reviews or source corpus. See [INSTALL.md](./INSTALL.md).

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

**Local contracts stay revisable.** Different parts of the knowledge base support different kinds of work, so task-specific types and link conventions stay local to each part. Structures can also become obsolete as questions, evidence, or model capabilities change, so those local choices remain revisable. Shared rules are kept for constraints that hold across parts and over time. See why [task-fitted structure costs cross-task reuse](./kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md).

**Doctrine is explicit; exact operations are code.** Skills and conventions tell the model what to do and which of its capabilities to use. Code, schemas, and validators carry operations whose behavior should not depend on repeated interpretation, because code [executes them the same way every time](./kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md). Both sides remain revisable as evidence and model capabilities change.

## Research routes

The [rendered site](https://zby.github.io/commonplace/) is the main route into the research. Starting points:

- [Can a Theory Builder Running on Fixed-Weight LLMs Learn?](./kb/articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md) — the lead article, with supplements on [testing](./kb/articles/testing-whether-a-theory-builder-learns.md), [bootstrapping](./kb/articles/bootstrapping-an-autonomous-theory-builder.md), [existing systems](./kb/articles/which-existing-self-improving-systems-are-theory-builders.md), and [the software house](./kb/articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md).
- [Deployment-time learning](./kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and the [learning theory index](./kb/notes/learning-theory-README.md) — durable changes to prompts, rules, tools, and code that affect later sessions without updating model weights.
- [Self-improving systems](./kb/notes/self-improving-systems-README.md) and [Commonplace as a reflective system](./kb/notes/evidence/commonplace-as-a-reflective-system.md).
- Reviews of [agent memory systems](./kb/agent-memory-systems/README.md) and [agentic systems](./kb/agentic-systems/README.md), with a [comparative review](./kb/agent-memory-systems/agentic-memory-systems-comparative-review.md).

## Commands, skills, and instructions

Commands are deterministic Python entry points called by name. Examples:

```bash
commonplace-validate kb/notes
commonplace-init --root .
commonplace-github-snapshot https://github.com/owner/repo/issues/123
```

The review system adds commands for selecting targets, queuing jobs, and finalizing outputs. `commonplace-x-snapshot` requires the `snapshot` package extra. See the [review system overview](./kb/reference/README-REVIEW-SYSTEM.md).

Skills (`cp-skill-*`) are agent procedures auto-loaded by compatible harnesses when a task matches their description. They stay in the installed package; `commonplace-init` writes a small stub for each into a consuming project's skill directories that points the agent to the real skill.

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Write or edit an artifact under its collection and type contracts |
| `cp-skill-validate` | Validate artifacts, collection landings, and site redirects |
| `cp-skill-connect` | Discover connections and write a connect report |
| `cp-skill-convert` | Convert a plain text file into a structured note |
| `cp-skill-ingest` | Turn one URL or local snapshot into a tracked source analysis |
| `cp-skill-snapshot-web` | Capture a URL into ignored local snapshots |
| `cp-skill-ground` | Retain the minimum quotations needed to ground a source claim |
| `cp-skill-health-check` | Diagnose a broken Commonplace installation |
| `cp-skill-revise-autoreason` | Experimentally revise a note with critic, author, synthesizer, and blind-judge agents, keeping the original as fallback |
| `cp-skill-write-multistage` | Write or rebuild an unsettled artifact through staged authorship and independent review |
| `cp-skill-library` | Find and follow a Commonplace library procedure, instruction, or type by name |

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