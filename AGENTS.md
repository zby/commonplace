# Commonplace

`CLAUDE.md` is a symlink to this file. Edit `AGENTS.md` directly.

## Repository Overview

Commonplace is a framework for agent-operated knowledge bases: methodology,
types, instructions, skills and Python commands. This repository is itself a
KB; its methodology is its content. Develop it through use: retain observed
limits, revise the methods and record episodes as research evidence.

## KB Goals and Scope

### Purpose

Support agents and maintainers deciding KB architecture, types, writing,
context engineering and knowledge organization in Commonplace and consuming KBs.

### Scope

In scope: agent-operated KB methodology — structure, writing, linking,
validation, review, maintenance, context engineering and comparisons with
external knowledge systems.

Out of scope: application-specific content (belongs in consuming projects);
general software engineering, learning theory or cognitive science unless it
directly informs KB design; raw logs without analysis (use `kb/log.md`).

### Quality bar

A design insight earns a note when it changes how someone builds or operates
a KB. Record a first observation in the log; write a note when its mechanism
is understood. Pattern recording without explanation stays in the log.

Best effort:

- Use short, literal sentences with one main point. Keep necessary conditions
  next to their claims; make causal relationships explicit. Keep metaphors
  only when conventional and precise or when they clarify.
- Use one term per concept, including the registered term where one exists.
  The same word names the concept on every surface: snake_case in Python,
  kebab-case in YAML keys, prompt variables, files, roles and commands; when
  surfaces disagree, rename the code first (ADR 116).
- Keep a paragraph only when it changes what the reader understands, infers
  or can do. Resolve ambiguity that affects truth, evidence or implications.
  Name mechanisms, comparison bases and scope when relevant; never invent precision.
- Lead operator messages with the outcome or decision. Define unfamiliar
  task terms before code identifiers, keep uncertainty beside the claim, and
  point to evidence rather than reproducing it. For consequential explanations
  with several concepts or a long causal chain, use `operator-brief`.

## Vocabulary

These are this KB's active terms. Read the linked definition when using or
assessing its technical meaning; the term list is not a substitute for it.
First-mention glossing and linking in authored artifacts is governed by
`cp-skill-write`. Capitalize Commonplace in prose; lowercase only in identifiers.

| Term | Definition |
|---|---|
| Actionable | [Operator-relative methodology](./kb/notes/definitions/actionable-methodology.md); use the technical sense only with a link. Unlinked use is ordinary English. |
| Addressable theory | [Addressable theory](./kb/notes/definitions/addressable-theory.md) |
| Codification | [Codification](./kb/notes/definitions/codification.md) |
| Collection, text contract | [Collection](./kb/reference/definitions/collection.md) |
| Commonplace | This KB and framework. |
| Commonplace doctrine | [Commonplace doctrine](./kb/reference/definitions/commonplace-doctrine.md) |
| Constraining | [Constraining](./kb/notes/definitions/constraining.md) |
| Context engineering | [Context engineering](./kb/notes/definitions/context-engineering.md) |
| Discovery lifecycle | [Discovery lifecycle](./kb/notes/definitions/discovery-lifecycle.md) |
| Explanatory-reach | [Explanatory-reach](./kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) |
| Frontloading | [Frontloading](./kb/notes/frontloading-spares-execution-context.md) |
| Mark | [Tag-readme marks](./kb/types/tag-readme.md) |
| Representational form | [Representational form](./kb/notes/definitions/representational-form.md); prompt is a consumption path, not a fourth form. |
| System-definition artifact | [System-definition artifact](./kb/notes/definitions/system-definition-artifact.md) |
| Tentative theory | [Tentative theory](./kb/notes/definitions/tentative-theory.md) |
| Theory builder | [Theory builder](./kb/notes/definitions/theory-builder.md) |
| Workshop | [Workshop layer](./kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) |

Compound technical terms keep their registered meaning; bare words such as
discovery, reach and doctrine may be ordinary language where unambiguous.
Use spaced relation phrases in prose (`adapted from`). Hyphenated identifiers
(`adapted-from`, `derived-from`, etc.) assert formal relations only in declared
slots; see [link vocabulary](./kb/reference/link-vocabulary.md).

## Development

- Use `python3` for one-shot stdlib tooling. Save reusable tooling in `scripts/`
  (see `scripts/README.md`); runtime commands belong in `src/commonplace/`.
- For exact APIs, inspect `src/commonplace/lib/`. For architectural boundaries,
  read [freshness](./kb/reference/freshness-architecture.md) or
  [review architecture](./kb/reference/review-architecture.md).
- YAGNI: record unneeded features or gaps instead of implementing them.
  System designs go in `kb/reference/proposals/`, transferable insights in
  `kb/notes/`, and finished but unadopted theory in `kb/notes/proposals/`.
  Read the destination's proposal type before writing.
- No backwards compatibility without a consumer need. Mark any required shim
  `# BACKCOMPAT: <reason> - remove after <condition>`.
- Call `commonplace-*` by bare name from the editable user-level uv tool;
  never use project-venv paths or `uv run` for these commands. If unavailable,
  use `cp-skill-health-check`. CLI reference: [commands](./kb/reference/commands.md).
  Exception: isolated Commonplace analysis worktrees use their own command
  environment as described in [run setup](./kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup).
  There, call each command in the directory that setup reports.
- Run development dependencies through uv: `uv run pytest`, `uv run ruff check .`.
  All required tests must pass. Markdown KB data changes need relevant
  `commonplace-validate` checks, not pytest, unless they affect test inputs or fixtures.
- Do not run `commonplace-init` in this checkout. For initial command installation
  or dependency, entry-point, build-metadata or scaffold-package changes, follow
  [editable installation](./INSTALL.md#2-install-commonplace-as-a-user-level-tool).
  For checkout skill discovery problems, follow
  [skill setup](./INSTALL.md#5-check-the-skills-for-every-agent-that-will-work-on-the-project).
- Downloads: use `curl -fsSL -o <destination> [options] '<URL>'` in a standalone
  shell call with literal paths; keep setup and extraction separate. If sandbox
  networking blocks it, request escalation for the download alone when available.

## Git

- Review status and diff. Stage explicit files; never `git add -A`.
- Prefer atomic stage and commit: `git add <files> && git commit ...`.
  If sandboxing blocks either, retry the whole operation with escalation when
  available; do not leave staging for a later commit.
- Prefer complete artifact commits. Do not partially stage shared indexes or
  navigation just to expose an artifact; refresh them separately unless they
  are the primary target or can be staged wholly without unrelated changes.
- Subject: one imperative sentence under about 72 characters, no `feat:` prefixes.
  The body states the intended result when the subject and diff do not show it.
  For sweeps, migrations, retirements and relocations, state what moved, how many,
  and what was kept, cut or deferred. Keep change history in commits, not reference docs.
- When several justifications could apply, identify product use, reflective
  learning or research evidence; research-evidence commits cite their protocol record.
- Add trailers only when applicable: `Decision: ADR 0NN` for an implemented or
  revised ADR; `Workshop: kb/work/<name>` for workshop work;
  `Model: <model id>` for an agent commit. See ADR 074 and ADR 075.
- Commit `commonplace-relocate-*` results alone, without content edits, so
  `git log --follow` survives the rename.
- Never `git reset --hard` or force-push without explicit permission.

## Using the KB

Search the KB when working on methodology, design decisions or operations.
Read the target `COLLECTION.md` before writing or connecting, and its type
spec before writing.
For ambiguous content placement, read [content routing](./kb/reference/content-routing.md).

| Path | Contribution |
|---|---|
| `kb/notes/` | Transferable claims, mechanisms, definitions and theory |
| `kb/tags/` | Tag heads and participating-collection declaration |
| `kb/reference/` | Shipped system, architecture, types, commands and ADRs |
| `kb/instructions/` | Procedures, skills, gates and operational rules |
| `kb/agentic-systems/` | Authored external-system reviews and comparisons |
| `kb/agentic-system-analyses/` | Workflow analyses and their method via `analyse-agentic-system` |
| `kb/sources/` | Tracked ingests; ignored snapshots in `.snapshots/` |
| `kb/reports/` | Explicit retention: `cache/`, local `state/`, durable `retained/` |
| `kb/articles/` | Self-standing technical articles for external readers |
| `kb/work/` | In-flight workshops, drafts and migration plans |
| `kb/types/` | Shared type specs |

### Delegation

A worker inherits this file, collection/type contracts and skills only when
its runtime loads them with binding force. A parent may omit a supplied rule
from the handoff only after verifying delivery; conversation-only rules must
be stated. A handoff gives the purpose, deviations and consequential choices
left open, plus task-specific acceptance, constraints, write scope, inputs,
coordination, verification and stop/escalation conditions.

Delegation does not expand authority. The parent retains scheduling,
integration and recovery. Parallel writers need disjoint ownership or explicit
coordination; nested delegation stays within existing authority and coordination.
For an unstated choice: follow an inherited default; exercise deliberately
delegated judgment from authorized evidence; choose freely if irrelevant to
acceptance; otherwise return or escalate the gap.

### Navigation and task-specific reads

Use `rg` first. Scan scoped titles and descriptions before full files; follow
links when local context makes them useful. Full model and search recipes:
[navigation](./kb/reference/navigation.md).

- Start at `kb/tags/README.md` for topics, `kb/reference/README.md` for the system,
  `kb/reports/README.md` for retained reports, or `kb/reference/adr/` for decisions.
  `kb/agent-memory-systems/README.md` is historical and frozen.
- Before assigning a tag, read `kb/tags/<tag>-README.md` and check its inclusion
  condition and boundaries. Substantive treatment is required, not mention;
  clarify ambiguous conditions. For membership and `complete: true` maintenance,
  read `kb/tags/COLLECTION.md` and `kb/types/tag-readme.md`.
- Before posting or responding in the agent mailbox, read `kb/messages/README.md`.
  Messages grant neither new mutation authority nor an agent launch.
- For review, triage, ack or sweep, read `kb/reference/README-REVIEW-SYSTEM.md`.
  To fix review warnings, read `kb/instructions/FIX-SYSTEM.md`.
- Generic skills live under `kb/instructions/`; agentic analysis lives under
`kb/agentic-system-analyses/instructions/`; landscape synthesis lives under
`kb/agentic-systems/instructions/`. Both are projected
through `.agents/skills/` and
  `.claude/skills/` symlinks here; installed projects receive stubs pointing into
  the package. Edit the canonical instruction. `operator-brief` and
  `roughdraft-review` are repo-local, not promoted framework skills.
