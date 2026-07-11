---
description: "llm-context-base review: markdown-only LLM wiki template with metadata routing, training-period write-back, lint protocols, and multi-agent shims"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# llm-context-base

llm-context-base, from `asakin/llm-context-base`, is a portable Markdown template for an LLM-maintained personal wiki. At the reviewed commit it ships no runtime service: the retained system is a repo of Markdown directories, config, instruction modules, templates, Obsidian settings, and tool-specific bootstrap files that host agents read and write.

**Repository:** https://github.com/asakin/llm-context-base

**Reviewed commit:** [6d01cba8e2c22f9ca2519c70073a05cd54378a8c](https://github.com/asakin/llm-context-base/commit/6d01cba8e2c22f9ca2519c70073a05cd54378a8c)

**Last checked:** 2026-06-04

## Core Ideas

**The repo is the memory substrate, not the agent runtime.** The philosophy and design docs state the boundary plainly: llm-context-base is a "pile of markdown" that external agents, MCP servers, workers, or GitHub Actions can operate on, while code extensions live above the repo ([PHILOSOPHY.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/PHILOSOPHY.md), [docs/design-decisions.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/design-decisions.md)). This makes adoption easy across agents, but it shifts faithfulness to whether the host tool follows the prose instructions.

**Metadata routing is the main context-efficiency mechanism.** The README and metadata docs require YAML frontmatter with `type`, `summary`, `tags`, `status`, and `updated`; the query protocol tells the agent to scan directory READMEs and summaries first, then read only one to three relevant files ([README.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/README.md), [docs/metadata-standard.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/metadata-standard.md), [_meta/instructions/knowledge-query.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-query.md)). It avoids a central growing index and relies on concise document summaries as the cheap routing layer.

**Instruction loading is staged by session and task.** Tool shims for Claude, Cursor, Copilot, Windsurf, AGENTS-compatible tools, and others point to `_config/config.md` and `_meta/instructions/general.md`; `general.md` then routes to modules such as query, lint, write, definition-of-done, and optimization only when triggers fire ([AGENTS.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/AGENTS.md), [.claude/CLAUDE.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/.claude/CLAUDE.md), [_meta/instructions/general.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/general.md), [docs/supported-tools.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/supported-tools.md)). The context budget policy is progressive disclosure through file protocols rather than embeddings or a server-side retriever.

**Training is write-back into durable config, not learned weights.** `_config/config.md` holds the user's profile, training controller, training log, personal context pointer, and conventions; `general.md` instructs agents to record new preferences, structure changes, and conventions immediately in config, context, README, instructions, or `WIKI-LOG.md` ([_config/config.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/config.md), [_config/context.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/context.md), [_meta/instructions/general.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/general.md), [docs/training-phases.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/training-phases.md)). This is memory by authored Markdown mutation: durable, inspectable, and diffable, but not automatically mined from retained execution traces by code in the repo.

**The health model is procedural lint, not enforced validation.** The lint module specifies checks for stale inbox items, missing metadata, stale active files, orphaned files, context-size review, non-timestamped filenames, and raw path formats; the migration script can convert older bullet metadata to YAML frontmatter ([_meta/instructions/knowledge-lint.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-lint.md), [migrate-to-yaml-frontmatter.py](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/migrate-to-yaml-frontmatter.py)). There is no standing validator wired into the substrate; the agent or user must invoke and execute the protocol.

## Artifact analysis

- **Storage substrate:** `repo` `files` — The retained state is a Git repository of Markdown files, templates, Obsidian config, README files, and thin agent bootstrap files. There is no local database, vector store, graph store, or service object in the reviewed repo.
- **Representational form:** `prose` `symbolic` — The operative parts are prose instructions, docs, templates, and wiki pages plus symbolic YAML frontmatter, directory names, statuses, tags, dates, routing tables, tool manifests, git history, and script logic. The repo does not retain embeddings or model weights.
- **Lineage:** `authored` `imported` — Users and agents author wiki pages, decisions, project files, config entries, training logs, and instruction updates; captured external material enters through `_inbox/` and optionally `_sources/`. The implementation evidence does not show an automatic trace-mining loop that qualifies as `trace-extracted`.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` — Content pages serve as knowledge and reference; `_config/`, `_meta/instructions/`, AGENTS/CLAUDE/Cursor/Copilot/Windsurf shims, and templates instruct agents; metadata, directory READMEs, routing tables, and `related` links route lookup; lint and definition-of-done protocols validate; bootstrap/session-start gates and privacy/gitignore rules are prose enforcement for compliant agents.

**Instruction substrate.** `_config/config.md`, `_config/context.md`, `_config/standard.md`, `_config/tools.md`, and `_meta/instructions/*.md` are system-definition artifacts. They change future behavior by telling agents what to load, what to ask, where to file captures, what metadata to require, how to lint, and when to keep or discard sources ([_config](https://github.com/asakin/llm-context-base/tree/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config), [_meta/instructions](https://github.com/asakin/llm-context-base/tree/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions)).

**Wiki content substrate.** `_inbox/`, `_sources/`, `_output/`, `1-Projects/`, `2-Knowledge/`, `3-Journal/`, and `4-Private/` are authored or imported knowledge surfaces with lifecycle rules. Frontmatter summaries and tags are operative because they decide what an agent reads before spending context on full files ([docs/directory-structure.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/directory-structure.md), [_config/standard.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/standard.md)).

**Tool shims and extension manifests.** AGENTS, Claude, Cursor, Copilot, and Windsurf files are small bootstraps that point agents back to the same canonical config and instruction modules; `_config/tools.md` declares optional local tools by purpose, install command, trigger, status, and docs ([AGENTS.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/AGENTS.md), [docs/supported-tools.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/supported-tools.md), [_config/tools.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_config/tools.md)). These artifacts make the same memory substrate portable across tools without adding an executable integration layer.

Promotion path: captures start in `_inbox/`, can be filed into durable content directories, and can become stronger system-definition artifacts when an observed convention is written into config or instruction modules. Decision records also have an `## Outcome` loop that turns past choices into later decision evidence. The path is manual or agent-authored; the repo does not independently promote entries through code-run gates.

## Comparison with Our System

| Dimension | llm-context-base | Commonplace |
|---|---|---|
| Primary purpose | Personal LLM wiki template and agent instruction substrate | Agent-operated methodology KB with typed library/workshop/source layers |
| Canonical artifact | Markdown files with YAML frontmatter and agent instructions | Typed Markdown artifacts with collection contracts and validation |
| Runtime | None in repo; host agents execute prose protocols | Python CLI commands, validators, indexers, review tooling, plus Markdown |
| Retrieval | Agent scans README, filenames, summaries, tags, and selected files | `rg`, generated indexes, links, type specs, reports, and explicit navigation rules |
| Governance | Lint protocols and prose rules followed by agents | Deterministic validation, review gates, schemas, generated indexes, git diffs |

Both systems treat a repo of Markdown artifacts as behavior-shaping memory for future agents. llm-context-base is deliberately lighter: it optimizes for immediate adoption by ordinary users and many tools, with no build step and no runtime dependencies. Commonplace is heavier and more formal: collection contracts, type specs, deterministic validation, and generated indexes make the KB less portable but more mechanically checkable.

The strongest design divergence is authority. In llm-context-base, a convention becomes active when an agent writes it into config or instructions and later agents comply. In Commonplace, many artifacts must also satisfy schemas, collection-local routing contracts, and validation. That gives Commonplace better auditability for methodology work, while llm-context-base remains easier to fork into a personal operating system.

### Borrowable Ideas

**Thin cross-tool shims.** Ready now. Commonplace could keep tool-specific bootstrap files minimal and point them at a canonical instruction surface, reducing drift between agents.

**Training-period explicitness.** Needs a concrete use case. A Commonplace workshop could borrow a time-bounded "learning the operator" mode, but durable methodology artifacts should not inherit personal preference logs without review.

**Metadata-first retrieval for non-indexed directories.** Ready now as a fallback pattern. llm-context-base's summary-first rule is a clean human-readable version of route-before-load.

**Inbox TTL as operational pressure.** Needs policy design. Commonplace has workshop and source layers; a TTL could help temporary captures stop masquerading as durable library knowledge.

**Keep zero-runtime mode credible.** Ready as a product boundary lesson. llm-context-base shows that Markdown-only systems can still carry useful behavior, but Commonplace should be explicit about which guarantees require CLI validation.

## Write side

**Write agency:** `manual` `automatic` — Humans and host agents create, edit, file, archive, and update Markdown artifacts; the only in-repo automatic write implementation I found is the metadata migration script, while most "automatic" behavior is instruction for the external agent to perform captures, lint logging, README updates, training-log updates, and filing decisions.

**Curation operations:** `none` — The repo specifies maintenance checks and agent-authored write-back, but it does not implement a code-run curation loop over stored memories from which consolidate/dedup/evolve/synthesize/invalidate/decay/promote can be verified as automatic operations.

## Read-back

**Read-back:** `both` — Accumulated config/context memory is pushed at session start by the mandatory protocol, while ordinary wiki knowledge re-enters action when the host agent deliberately follows query protocols, scans summaries/tags/READMEs, reads selected files, or follows related links.

**Read-back signal:** `coarse` — The push path is always-load session-start context: `_config/config.md`, `_meta/instructions/general.md`, `_config/context.md`, and phase-dependent files are read because the agent is in the wiki, not because a specific task instance matched a memory item.

**Faithfulness tested:** `no` — The repo specifies the protocol and ships examples/docs, but I did not find tests or an evaluation showing that pushed config/context memory changes downstream agent behavior faithfully.

The most important pull mechanism is summary-first search. The query module routes by question type, checks target directory READMEs, scans summaries, reads one to three relevant files, and cites sources with updated dates ([_meta/instructions/knowledge-query.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-query.md)). There is no implemented retriever that injects ordinary wiki content into the agent's context without the agent initiating the lookup.

Context scope and complexity are controlled by directory routing and metadata, not by token accounting in code. The docs claim summary scanning scales to hundreds of documents, but the reviewed repo does not contain tests or a runtime that measures retrieval precision, context dilution, or behavioral effect.

## Curiosity Pass

**"Learns how you work" means durable instruction edits.** The phrase can sound like trace learning, but the inspected implementation is an authored write-back loop into config, context, README, instructions, and logs.

**The system's weakness is also its adoption advantage.** Because the repo has no runtime, it has no service-level failure mode or telemetry surface. The cost is that lint, query routing, and privacy rules are only as reliable as the host agent's compliance.

**The training log is high-authority personal memory.** `_config/config.md` tells agents to read it at session start and adjust behavior from it. That makes it more like system-definition memory than ordinary wiki content.

**The future-directions file keeps automation out of scope.** Heartbeats, MCP servers, event-driven orchestration, GitHub Actions, and smarter training are named as extension territory rather than implemented substrate behavior ([docs/future-directions.md](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/docs/future-directions.md)).

## What to Watch

- Whether GitHub Actions, MCP, or heartbeat/event files move from future direction into shipped code; that would change the system from Markdown-only substrate to an actively scheduled memory layer.
- Whether lint becomes an executable validator instead of a prose protocol; that would raise metadata and lifecycle rules from agent-followed advice to mechanically enforced governance.
- Whether training write-back gains source-span provenance linking each learned preference or convention to a conversation, capture, or decision artifact.
- Whether external-source preservation defaults change; preserving `_sources/` by default would shift the system closer to Karpathy's raw-source layer and improve auditability at the cost of accumulation.
- Whether supported tool shims diverge from the canonical instruction modules as more agent ecosystems add proprietary rule formats.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: llm-context-base pushes accumulated config/context at session start, while ordinary wiki content is pull-only unless the host agent deliberately loads it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: config, instruction modules, templates, metadata, and content files differ by form and authority even though all live in one repo.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, decisions, references, inbox captures, sources, and query answers mainly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `_config`, `_meta/instructions`, templates, tool shims, and lint protocols instruct, route, validate, or constrain future agents.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: metadata routing and just-in-time instruction loading are context-selection mechanisms rather than ordinary documentation.
