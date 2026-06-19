---
description: "Memwiki review: npm CLI protocol scaffold for AGENTS/hook files, hot-cache wiki memory, agent-maintained trace updates, and coarse push read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-18"
tags: [trace-derived]
---

# memwiki

memwiki, by Swapnil, is a small TypeScript/npm scaffold for adding a file-backed project memory protocol to an AI coding workspace. At the reviewed commit it implements `init` and `update` commands that create root hook files, an `AGENTS.md` protocol, and starter `.memory/wiki/` Markdown files; ongoing memory behavior is delegated to host agents that read those instructions and edit the wiki during ordinary work.

**Repository:** https://github.com/hereisSwapnil/memwiki

**Reviewed commit:** [8034a3da991ac2639b87875172a9572903ecf1d5](https://github.com/hereisSwapnil/memwiki/commit/8034a3da991ac2639b87875172a9572903ecf1d5)

**Source directory:** `related-systems/hereisSwapnil--memwiki`

## Core Ideas

**The package installs a memory protocol, not a retrieval service.** `src/index.ts` parses only `init` and `update`, then writes a fixed map of protocol and wiki files into the current working directory. There is no server, MCP layer, vector store, search index, background watcher, or model call in the package code ([src/index.ts](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.ts), [package.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package.json)).

**Root hook files are the activation surface.** The scaffold writes `.cursorrules`, `CLAUDE.md`, and `.github/copilot-instructions.md`, each telling the corresponding host to read `AGENTS.md` and `.memory/wiki/hot.md` before coding. The memory system relies on those existing agent products loading workspace instructions, so the protocol is vendor-agnostic but host-dependent ([src/index.ts](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.ts), [.cursorrules](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.cursorrules), [CLAUDE.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/CLAUDE.md), [.github/copilot-instructions.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.github/copilot-instructions.md)).

**Context efficiency is a hot-cache plus index convention.** The protocol tells agents to read `.memory/wiki/hot.md` first, then consult `.memory/wiki/index.md` only when the hot cache is insufficient. The README describes `hot.md` as short-term context around 500 words and `index.md` as a map of content for larger projects. There is no token budget enforcement or automatic selection beyond these prose instructions ([README.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/README.md), [AGENTS.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/AGENTS.md), [.memory/wiki/hot.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.memory/wiki/hot.md), [.memory/wiki/index.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.memory/wiki/index.md)).

**The write model is agent-maintained Markdown.** `AGENTS.md` instructs agents to update `patterns.md`, `bugs.md`, `decisions.md`, `hot.md`, and `log.md`, synthesize `.memory/.raw/` inputs into wiki pages, create domain pages as needed, and never delete knowledge. The CLI only creates or updates protocol files; the substantive memory curation happens when the host agent follows the installed prose protocol ([AGENTS.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/AGENTS.md), [src/index.ts](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.ts), [.memory/wiki/log.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.memory/wiki/log.md)).

**Adoption affordances are strong, governance is weak.** The system is just Markdown and a dependency-light Node CLI. Users can inspect, diff, and edit the wiki without a hosted service. The tradeoff is that freshness, correctness, linking, and command execution are prompt-following properties; the repository has no tests, validators, review status, or faithfulness checks for whether agents actually read or maintain the wiki ([package.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package.json), [tsconfig.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/tsconfig.json), [AGENTS.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/AGENTS.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — The durable memory surface is project-local Markdown under `.memory/wiki/`, immutable user-supplied sources under `.memory/.raw/`, and root instruction files in the repository or workspace. The npm package itself stores protocol templates as TypeScript string literals that are compiled into the CLI.
- **Representational form:** `prose` `symbolic` — Wiki pages and protocol text are prose; filenames, fixed paths, root hook locations, slash-command names, checkboxes, wikilinks, npm metadata, and CLI command names are symbolic. The inspected source contains no embeddings, model weights, database schema, or learned ranker.
- **Lineage:** `authored` `imported` `trace-extracted` — The scaffolded protocol and starter wiki files are authored package templates; `.memory/.raw/` is an imported-source lane; session work, learned project patterns, bug fixes, decisions, and end-of-session summaries are meant to be extracted from the agent's work trace into wiki files by the host agent.
- **Behavioral authority:** `knowledge` `instruction` `routing` `learning` — Wiki pages serve as remembered knowledge; root hooks and `AGENTS.md` instruct the host agent; `hot.md` and `index.md` route context loading; the protocol turns recurring work experience and session endings into learned durable state. Enforcement and validation are not implemented beyond prose imperatives.

**Protocol scaffold.** The operative system-definition artifacts are `AGENTS.md`, `.cursorrules`, `CLAUDE.md`, and `.github/copilot-instructions.md`. They are authored prose with symbolic path conventions. Their authority is instruction and routing: they tell the host agent what memory files to read and when to update them.

**Wiki pages.** The default wiki contains `hot.md`, `index.md`, `log.md`, `stack.md`, `patterns.md`, `bugs.md`, and `decisions.md`. The pages are authored or trace-extracted prose knowledge with lightweight symbolic structure. `hot.md` has special routing authority because it is the first memory page named by the root hooks and session-start protocol.

**Raw-source lane.** `.memory/.raw/` is created by the CLI but seeded empty. The protocol treats files dropped there as immutable source material that agents may read and synthesize into wiki pages. That gives imported documents a source-of-truth role, but there is no citation format, checksum, or deterministic extraction step in the code.

**Slash-command protocol.** `/memwiki-ingest`, `/memwiki-lint`, and `/memwiki-fold` are not executable CLI subcommands; they are chat commands described inside `AGENTS.md` and the README. Their authority depends on a host agent recognizing the phrase and following the prose workflow.

Promotion path: Memwiki can promote raw documents into wiki pages, recent session state into `hot.md` and `log.md`, and repeated project facts into domain pages linked from `index.md`. It does not promote memory into validators, route tables, enforced gates, embeddings, or independently testable system behavior.

## Comparison with Our System

Memwiki and Commonplace share the file-first premise: durable agent memory should be inspectable Markdown plus workspace instructions, not only hidden service state. Both use an `AGENTS.md`-style entry point and rely on agents navigating local files.

The systems diverge sharply on artifact authority. Memwiki is a thin protocol installer; after setup, the active host agent is responsible for reading, judging, synthesizing, updating, and folding memory. Commonplace encodes more of that work in collection contracts, type specs, validators, review workflows, generated indexes, and explicit source-grounding rules.

Memwiki's strongest move is adoption. It can be dropped into an arbitrary project with one npm command and no service dependency. Its weakest point is governance: a remembered fact can become future context with no retained evidence, status, validation, or review. Commonplace should preserve the low-friction entry idea without importing the weak truth-maintenance model.

### Borrowable Ideas

**Protocol update that preserves user memory.** Ready now as a product principle. Memwiki's `update` command overwrites root protocol files but leaves `.memory/wiki/` untouched, separating system-definition upgrades from user knowledge.

**Tiny hot cache for active work.** Useful with guardrails. Commonplace workshops could maintain a short current-state file for resumability, but it should be scoped to the workshop and explicitly lower authority than reviewed library artifacts.

**Cross-host hook fanout.** Needs a concrete packaging use case. Memwiki writes Cursor, Claude, Copilot, and `AGENTS.md` hooks from one template set; Commonplace could borrow that for project initialization across agent harnesses.

**Do not borrow unreviewed autonomous memory writes for library content.** Memwiki tells agents to append or refine project memory whenever they learn something. That is acceptable for a project-local scratch wiki, but Commonplace library artifacts need source grounding, type checks, and review.

## Write side

**Write agency:** `manual` `automatic` — Users can manually edit wiki files or drop source documents into `.memory/.raw/`; the installed protocol also instructs agents to update wiki files during work, before session end, and when slash commands are invoked. The automatic side is prose-mediated agent behavior, not a deterministic background process.

**Curation operations:** `consolidate` `evolve` — `/memwiki-fold` tells the agent to condense older `log.md` entries, and the session-end/hot-cache protocol tells the agent to update existing current-state memory as work changes. There is no code-level deduplication, decay, contradiction handling, or promotion-by-recurrence.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — The durable signal is the host agent's work session: what it learned, which bug it fixed, what decision it made, what current state remains, and what summary should be appended before context is lost. The repository does not expose a raw transcript parser; extraction happens through the agent following `AGENTS.md`.

**Extraction.** The oracle is the current host agent. The protocol tells it to decide when a pattern, bug, decision, raw document, or current-state update matters enough to write into the wiki. That makes the learned artifact inspectable but not independently verified.

**Learning scope:** `per-project` — Memory is rooted in the project directory where `npx memwiki init` or `update` runs.

**Learning timing:** `online` `staged` — Online learning happens during ordinary work and at session end; staged learning happens when the user invokes `/memwiki-ingest`, `/memwiki-lint`, or `/memwiki-fold`.

**Distilled form:** `prose` `symbolic` — The retained output is Markdown prose plus symbolic filenames, links, headings, checkboxes, and command/path conventions.

Memwiki fits the trace-to-prose-wiki family in the trace-derived survey. It strengthens the claim that low-friction trace learning can be packaged as host instructions, but it also shows the weakness of prose-only learning: the protocol can request updates, but it cannot prove they are faithful, complete, or later used.

## Read-back

**Read-back:** `both` — Root hooks and `AGENTS.md` push `hot.md` into the beginning of a host-agent session when the host honors workspace instructions; broader memory is pulled when the agent consults `index.md`, reads domain pages, or follows `/memwiki-*` workflows.

**Read-back signal:** `coarse` — The push path is an always-read convention for `AGENTS.md` and `.memory/wiki/hot.md`, not a task-specific identifier, lexical search, embedding lookup, or LLM relevance judgment.

**Faithfulness tested:** `no` — The source includes no tests or harness that compares behavior with and without the pushed memory, audits whether agents read `hot.md`, or verifies that slash-command memory updates happened.

The injection point is pre-invocation or session start, as mediated by the host. Cursor, Claude Code, and Copilot-style hooks tell the agent to read the protocol and hot cache before coding. If the host does not load those root files, Memwiki has no independent read-back mechanism.

Selection and complexity control are simple. `hot.md` is meant to stay short, while `index.md` routes to topic pages as the wiki grows. There is no retrieval scoring, top-k, token-budget enforcement, stale-entry filter, or automatic domain-page selection. Effective context dilution is therefore a convention and agent-behavior question, not something verified by the package code.

Authority at consumption is advisory-to-instructional. The hook and protocol files are instructions to the agent; the wiki pages are project knowledge. Memwiki does not distinguish reviewed facts, tentative notes, source-backed claims, and generated summaries through types or validation.

## Curiosity Pass

**The README is more ambitious than the executable surface.** The package advertises persistent project memory, active ingestion, linting, and folding, but the npm CLI only creates and updates files. The "commands" are instructions for the chat agent, not implemented subcommands.

**The checked-in generated JavaScript lags the TypeScript source.** `src/index.js` only supports `init`, while `src/index.ts` supports `init` and `update`. The package `main` and `bin` point to `dist/index.js`, which is not checked in, and `prepack` builds it from TypeScript. The review treats TypeScript as the intended source while noting the repository does not retain the built runtime artifact ([src/index.js](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.js), [src/index.ts](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.ts), [package.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package.json)).

**The repository is also a Memwiki example.** Its checked-in `.memory/wiki/log.md` records a `/memwiki-ingest` pass that populated stack, patterns, and decisions. That is useful evidence for intended operation, but it is not a deterministic test of the package behavior.

**The package metadata undercuts the zero-dependency claim.** The README advertises zero dependencies, but `package.json` and `package-lock.json` list `memwiki` itself as a runtime dependency. That looks accidental; it does not change the memory architecture, but it matters for the packaging/adoption claim ([README.md](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/README.md), [package.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package.json), [package-lock.json](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package-lock.json)).

## What to Watch

- Whether `/memwiki-ingest`, `/memwiki-lint`, and `/memwiki-fold` become real CLI or MCP commands; that would move curation authority from prompt-following into testable code.
- Whether Memwiki adds validation for `hot.md` length, index link integrity, raw-source citation, or stale entries; that would narrow the current governance gap with Commonplace.
- Whether host-specific hooks grow beyond "read these files" into bounded context assembly; that would change read-back from coarse push toward targeted push.
- Whether the packaging mismatch around `dist/`, stale `src/index.js`, and self-dependency is resolved; adoption claims depend on the npm artifact being as boring as the protocol.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Memwiki stores a wiki, but only hook loading and explicit page reads activate it for an agent.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: protocol files, hot cache, wiki pages, raw sources, and slash-command instructions carry different authority.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames: Memwiki turns session experience into durable prose memory through agent-mediated extraction.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages and raw-source syntheses are advisory remembered context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: root hooks and `AGENTS.md` are behavior-shaping instruction and routing artifacts.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: Memwiki depends on stable paths, filenames, page names, and slash-command strings as its routing symbols.
