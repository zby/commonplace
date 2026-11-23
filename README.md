# Commonplace

**Research on knowledge systems, running as one.**

LLM-written text can be useful even when no person reads it directly, because it can improve how an LLM answers your questions. Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

Commonplace combines two things:

- **A research direction — [deployment-time machine learning by LLM-selected updates](./kb/articles/deployment-time-machine-learning-llm-selected-updates.md) (draft).** A deployed system can learn while its model weights stay fixed by changing what it retains between tasks—procedures, rules, notes, and scripts—through updates that are proposed, evaluated on whether they make later work better, and can be rejected. Our empirical bet is that fixed-weight LLMs can help search for candidate updates and perform that selection for open-ended knowledge work where no single score settles a change, allowing the loop to run without per-update human judgment. No automated end-to-end test of that bet has been run yet.
- **A practical system — an agent-operated LLM wiki.** In the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), a persistent, linked Markdown-and-Git layer where agents, directed by people, turn a project's work and sources into retained, connected notes, backed by installable types, skills, validators, and review workflows.

They reinforce each other because memory is about learning: a note earns its keep when it changes what the system does next. A wiki that agents read and edit is the kind of addressable store a selection-based learner needs, and [real use supplies the problems and criticism](./kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) its judgments draw on. Commonplace also keeps its own operating rules—how it writes, links, validates, and revises notes—inside the store it edits ([reflection](./kb/theory/definitions/reflective-system.md)). When a method improves, [later work reuses it](./kb/theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

This repository holds the KB and the installable `llm-commonplace` package (types, conventions, skills, schemas, validators, and CLI commands) for running a knowledge base of the same kind in your own project. Browse the theory and articles on the [rendered site](https://zby.github.io/commonplace/); this README covers installing, operating, and developing the tool.

## Quick start

### Install Commonplace in a project

Install the command-line tool once per OS user:

```bash
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

Restart the shell or agent runtime, then scaffold the target project:

```bash
commonplace-init --root .
```

Fill in the generated `AGENTS.md.template` and use it as the project's `AGENTS.md`, and rename `CLAUDE.md.template` to `CLAUDE.md`. Projects read Commonplace's types, conventions, and skills in place from the installed package rather than copying them; the scaffolded `kb/` accumulates knowledge about your own project. The package does not bundle this repository's source corpus.

See [INSTALL.md](./INSTALL.md) for the full setup flow, [Getting started](./kb/reference/getting-started.md) for a first worked session with your agent, and [Commonplace architecture](./kb/reference/architecture.md) for the installed topology.

### Consult the research with your agent

You can ask an agent to consult this repository or the [rendered site](https://zby.github.io/commonplace/) without installing anything. For example:

> Use https://github.com/zby/commonplace to advise the author of <project URL>, covering quick fixes and structural improvements.

Start with a concrete decision or failure in the target project. Use the [topic guides](./kb/tags/README.md) to find relevant [theory](./kb/theory/). Each guide links selected entries.

- Much of Commonplace's design draws on the theory here. When a claim fits your project's problem, use the [reference docs](./kb/reference/README.md) and [code](./src/commonplace/) to see how Commonplace put it into practice and which parts you could adapt.
- Browse [ongoing investigations](./kb/work/) for questions Commonplace is still exploring.
- For comparisons, consult [external-system reviews](./kb/agentic-systems/) and [analyses](./kb/agentic-system-analyses/). Check which observations support a broader claim and which depend on that system's design.

### Develop Commonplace

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

Restart consumers of the command path. Ordinary Python edits take effect immediately through the editable install; reinstall with `uv tool install --reinstall --python ">=3.11" --editable .` after dependency, entry-point, build-metadata, or packaged-scaffold changes. Do not run `commonplace-init` in this source checkout.

Run lint with `uv run ruff check .`. For tests, start with `uv run pytest tests/commonplace/general` and follow [test selection](./tests/README.md) for affected subsystems, relevant slow tests, and pre-push verification.

## Core design choices

- **Claims form a network.** Note titles are assertions, not topics, and links state how claims relate — such as `grounds`, `extends`, `contradicts`, or `exemplifies` — turning traversal into reasoning under bounded context. See [title as claim](./kb/theory/title-as-claim-enables-traversal-as-reasoning.md) and [link methodology](./kb/tags/links-README.md).
- **Typed documents with two-part types.** Each document type pairs a syntactic part checked deterministically by software (YAML schema, required fields, links, and structural validation via `commonplace-validate`) with a semantic part checked by agents (prose authoring contracts, traits, and LLM review criteria via `commonplace-review`). See [verifiable document types](./kb/theory/document-types-should-be-verifiable.md).
- **Structure is earned progressively.** A frontmatter-free Markdown file is valid `text`. Add a description and note type when material deserves a durable claim; specialize further only when extra structure enables useful checks or workflows. See [the wikiwiki principle](./kb/theory/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md).
- **Authored knowledge and review state stay file-backed.** Markdown and Git supply a universal interface, versioning, diffs, and rollback. Derived views handle scale without replacing authored files. Review state is stored as one hash-checked result file per `(note, criterion)` pair ([ADR 127](./kb/reference/adr/127-review-runs-as-workflows-over-result-files.md)).
- **Local contracts stay revisable.** Task-specific types and link conventions stay local to each collection so structures can evolve as questions, evidence, or model capabilities change; shared rules are reserved for cross-cutting invariants ([current task fit does not warrant costly entrenchment](./kb/theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)).
- **Explicit doctrine paired with deterministic code.** Skills and prose instructions direct model judgment; Python commands enforce repeatable operations and bookkeeping ([scheduler–LLM separation](./kb/theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)).
- **Separated review and editing.** `commonplace-review` runs headless criteria against notes and never modifies them; `commonplace-revise` is the only review/editing workflow that writes a note ([Review and editing system](./kb/reference/README-REVIEW-SYSTEM.md)).

## Commands, skills, and instructions

### CLI commands

Commands are deterministic Python entry points installed on `PATH` by `llm-commonplace`. Examples:

```bash
commonplace-status
commonplace-validate kb/notes
commonplace-init --root .
commonplace-github-snapshot https://github.com/owner/repo/issues/123
```

`commonplace-review` evaluates notes against criteria with headless workers without editing files; `commonplace-revise` runs simplification passes, finding fixes, triage, or source-grounded rewrites. See the full [CLI command catalogue](./kb/reference/commands.md) and the [review and editing system overview](./kb/reference/README-REVIEW-SYSTEM.md).

### Installed skills

Skills (`cp-skill-*`) are agent procedures auto-loaded by compatible harnesses when a task matches their description. `commonplace-init` writes lightweight stubs into `.claude/skills/` and `.agents/skills/` pointing to the canonical skills in the installed package:

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Write or edit an artifact under its collection and type contracts |
| `cp-skill-connect` | Discover connections and write a connect report without mutating notes |
| `cp-skill-convert` | Convert a plain text file into a structured note |
| `cp-skill-ingest` | Turn one URL or local snapshot into a tracked source analysis |
| `cp-skill-snapshot-web` | Capture a URL into ignored local snapshots |
| `cp-skill-ground` | Retain the minimum verbatim quotations needed to ground a source claim |
| `cp-skill-review` | Review KB notes against criteria without editing them |
| `cp-skill-revise` | Edit, improve, triage findings on, or rewrite a KB note |
| `cp-skill-add-collection` | Add a new collection with its contract, landing, tag assignment policy, and routing |
| `cp-skill-health-check` | Diagnose a broken Commonplace installation |
| `cp-skill-library` | Find and follow a Commonplace library procedure, instruction, or type by name |

Explicitly invoked Markdown procedures and review gates live under [`kb/instructions/`](./kb/instructions/README.md).

## Research: selection-based learning

Standard machine learning updates opaque weights against a scalar loss or reward. At the opposite extreme, Schmidhuber's [Gödel machine](./kb/theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) rewrites its own code only when it can formally prove higher expected utility, which leaves most real-world improvements out of reach. Commonplace uses **reflective self-improvement by selection**—proposing and judging edits to the instructions and checks that govern its own later work, currently with human maintainers inside the boundary for both search and selection—and explores whether fixed-weight LLMs can run that loop autonomously, relying on reversibility and later evidence to catch mistakes.

The [rendered site](https://zby.github.io/commonplace/) is the primary reading surface for the research. Key entry points:

- **Core theory:** the [selection-based learning definition](./kb/theory/definitions/selection-based-learning.md), [local comparison suffices](./kb/theory/selection-based-learning-needs-only-a-local-comparison.md), [defining improvement for open-ended work](./kb/theory/defining-improvement-for-open-ended-work.md), and [necessary preference](./kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md).
- **The judgment bet:** [Can an LLM Judge Which Changes Are Worth Making?](./kb/articles/can-an-llm-judge-which-changes-are-worth-making.md) (draft) — packet curation vs. tool-using inquiry, a three-arm diagnostic test, and keeping working definition, judge competence, and framework prompting apart.
- **Test program:** [Testing Autonomous Selection-Based Learning](./kb/articles/testing-autonomous-selection-based-learning.md) (draft) — discriminating comparisons for admission, targeted correction, criterion revision, and whole-loop net gain, plus a proposed first experiment.
- **Deployment-time learning:** [Deployed systems can learn from feedback with fixed model weights](./kb/theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), the [deployment-time learning index](./kb/tags/deploy-time-learning-README.md), the [learning theory index](./kb/tags/learning-theory-README.md), and the published ECSA 2026 paper and ASISAS 2026 slides in [Articles](./kb/articles/README.md).
- **Self-improving and reflective systems:** the [self-improving systems index](./kb/tags/self-improving-systems-README.md), the [improvement loop index](./kb/tags/improvement-loop-README.md), the [robust comparison index](./kb/tags/robust-comparison-README.md), [Commonplace as a reflective system](./kb/theory/evidence/commonplace-as-a-reflective-system.md), and [What an Automated Reviewer Should Measure](./kb/articles/what-an-automated-reviewer-should-measure.md) (draft).

## Repository layout

```text
kb/                       Knowledge base
  articles/               Standalone technical articles, published paper, and talks
  theory/                 Transferable research claims, mechanisms, and definitions
  notes/                  Short replies, examples, and comparisons
  tags/                   Curated topic heads across collections
  reference/              Shipped system documentation, contracts, and ADRs
  types/                  Global artifact contracts and schemas
  instructions/           Skills, review gates, and procedures
  sources/                Snapshotted external sources (local) and tracked ingests
  reports/                Operational state and retained reports
  work/                   In-flight workshops
  tasks/                  Work tracking
  log.md                  Improvement log
  index.md                Rendered-site homepage

src/commonplace/          Packaged operational engine
  cli/                    commonplace-* command entry points
  review/                 Review criteria, result files, and runners
  headless/               Headless worker orchestration
  freshness/              Hash-based staleness tracking
  artifactrun/            Multi-stage artifact workflow runner
  lib/                    Shared validation, path, and KB helpers
  docs/                   ProperDocs build hooks and assets
  scaffold_manifest.py    Declarative manifest executed by commonplace-init
```

## Prerequisites

Installing and operating a Commonplace knowledge base uses:

| Tool | Required | Purpose |
|---|---|---|
| Agent runtime | yes | Load project instructions and expose installed skills |
| [uv](https://docs.astral.sh/uv/) | yes | Install Commonplace and run development dependencies |
| [git](https://git-scm.com/) | yes | Versioning and history-preserving relocation |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Search, frontmatter queries, and link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [Poppler](https://poppler.freedesktop.org/) | yes | PDF metadata and text extraction |
| [Trafilatura](https://trafilatura.readthedocs.io/) | no | Web-page capture in `snapshot-web`; without it, paste the page text |
| [gh](https://cli.github.com/) | no | GitHub issue and PR snapshots |

## License

Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](./LICENSE-CODE)
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](./LICENSE)
