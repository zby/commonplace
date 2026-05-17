---
description: "Repo-local Go CLI for agent-written why-memory, with JSONL entries, disposable SQLite FTS search, and doctrine-driven session capture"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-25"
---

# Gnosis

> Replaced 2026-05-16. See [Gnosis](./gnosis.md) for the current review.

Gnosis is a small Go CLI by Stavros Korokithakis for keeping project-local "why" memory in a repository. Its central claim is not that humans will maintain another knowledge tool, but that coding agents can be instructed to search prior decisions before work, write durable entries during work, and review the session afterward.

**Repository:** https://github.com/skorokithakis/gnosis

**Reviewed commit:** https://github.com/skorokithakis/gnosis/commit/fb53422e29e9402306d5c4d739017ac20038eaaf

## Core Ideas

**The durable substrate is repo-local JSONL, not a service.** Entries live in `.gnosis/entries.jsonl` with IDs, normalized topics, free text, related entry IDs, and created/updated timestamps. The storage layer treats the JSONL file as the authority and makes the `.gnosis` directory on first write, so the memory ships with the code rather than with a hosted backend ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/storage/storage.go), [.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/.gnosis/entries.jsonl)).

**SQLite FTS5 is a disposable projection.** Search opens a per-repo cache under XDG cache or `~/.cache`, rebuilds the FTS5 table when the JSONL mtime changes, and ranks results with BM25 snippets. The index is explicitly rebuildable from JSONL; `gn reindex` forces the same path. This is a clean split between committed memory and uncommitted retrieval machinery ([internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/index/index.go), [internal/paths/paths.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/paths/paths.go), [internal/commands/reindex.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/reindex.go)).

**The agent contract is doctrine, not an API integration.** Adoption asks maintainers to add two AGENTS lines: start by reading `gn help plan`, finish with `gn help review`. Those doctrine files tell agents to search before implementing, surface conflicts, record decisions when they arise, and prefer human-provided or empirical knowledge over analysis reproducible from the code. The product strategy makes this the signal-to-noise filter, not a secondary tip ([README.md](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/README.md), [internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/doctrine/review.txt), [docs/PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/docs/PRODUCT_STRATEGY.md)).

**The command surface stays deliberately narrow.** `gn` dispatches to help, write, search, show, topics, edit, remove, and reindex. Write accepts comma-separated topics, text, and optional related IDs; search is FTS; show resolves either short ID prefixes or longer topic names; edit opens `$EDITOR`; remove warns about dangling related references rather than silently rewriting them. The repo's own Gnosis entries record that an MCP server was considered unnecessary because target coding agents have shell access ([cmd/gn/main.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/cmd/gn/main.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/write.go), [internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/show.go), [.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/.gnosis/entries.jsonl)).

**Operational hardening is stronger than semantic governance.** Appends and rewrites use flocking; ID generation runs under an exclusive lock; full rewrites go through temp files and atomic rename; topic normalization is centralized and applied on read/write; the index rebuild captures entries and mtime under the same shared lock. But quality control remains doctrinal: there is no schema for entry kinds, stale-state marker, validation command, confidence field, source quote, review status, or lifecycle beyond manual edit/remove and related IDs ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/storage/storage.go), [internal/commands/edit.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/edit.go), [internal/commands/rm.go](https://github.com/skorokithakis/gnosis/blob/fb53422e29e9402306d5c4d739017ac20038eaaf/internal/commands/rm.go)).

## Comparison with Our System

| Lens axis | Gnosis | Commonplace |
|---|---|---|
| Creation and import | Agents write short entries through a CLI while working | Agents and maintainers write typed notes, sources, reviews, ADRs, instructions, reports, and workshop artifacts |
| Evidence and trust | Git history plus human/empirical doctrine; no required source quotations or validation | Frontmatter contracts, source snapshots, citations, validation, semantic review, and review state |
| Artifact contracts | One entry shape: ID, topics, text, related IDs, timestamps | Path-valued type specs define role-specific required sections, metadata, links, and validation |
| Consumer surfaces | Shell CLI, repo instructions, JSONL, FTS snippets | Shell search, generated indexes, skills, validators, review bundles, collection conventions |
| Activation | AGENTS tells every agent to search before work and review after work | Agents load AGENTS, collection conventions, type specs, indexes, and relevant notes as task context |
| Promotion/codification | No path from entry to docs, tests, skills, or stricter rules | Workshop/source material can promote into notes, ADRs, instructions, scripts, validators, and skills |
| Lifecycle | Manual edit/remove; related links are flat IDs | Review gates, generated indexes, statuses, relocation, link checks, and collection-specific maintenance |

Gnosis is narrower than commonplace by design. It has no theory layer, no typed document families, no source archive, no link vocabulary, and no validation beyond command parsing. Its bet is that most teams do not need a full KB methodology to get value from captured decisions; they need a tiny repo-local memory channel that agents will actually use.

The strongest alignment is files-first adoption. Both systems keep durable memory inspectable and version-controlled, and both use derived indexes as projections. The divergence is authority. Commonplace treats artifact type as a contract: a review or note promises certain work has been done. Gnosis treats the memory entry as a lightweight assertion plus topic tags. That is good for capture, but weak for later trust.

The second divergence is the writer filter. Commonplace often wants agents to distill their own analysis into transferable notes when the mechanism is understood. Gnosis explicitly pushes the other way: if a competent future agent can rederive the point from code and docs, the entry is noise. That is a sharp and useful product stance for repo-local decision memory, even though it would be too restrictive for a methodology KB whose job is to accumulate abstractions.

## Borrowable Ideas

**Two-line adoption hook.** Ready now as a packaging pattern. Gnosis gets agent behavior by adding a small instruction to AGENTS rather than by integrating with every agent runtime. Commonplace skills and init flows should keep this standard: install a narrow command, then make the agent guidance point to the command at the right workflow boundary.

**Human-context filter for low-noise capture.** Ready now for workshop and handoff guidance. The exact rule should not govern all commonplace notes, but it is a strong filter for operational memory: record what the human or environment revealed, not what another agent can infer by rereading the code.

**Committed source plus disposable retrieval cache.** Ready when we add heavier retrieval. Gnosis keeps `entries.jsonl` in git and moves lock/index state to a per-repo cache keyed by path. That is the right shape for any future commonplace FTS/vector cache under generated indexes.

**Topic length as an ambiguity guard.** Small but clean. Gnosis requires normalized topics to be longer than ID prefixes so `show` can dispatch by target length without fallback ambiguity. If commonplace grows short stable IDs for notes, this kind of lexical partition is worth copying.

**Warnings instead of hidden repair on destructive edits.** Ready now as command UX guidance. `gn rm` warns when surviving entries still reference removed IDs, but does not mutate them automatically. Commonplace relocation commands already favor explicit reporting; this reinforces that destructive repair should be inspectable.

## Trace-derived learning placement

**Trace source.** Gnosis consumes live coding-session context indirectly: human statements, rejected alternatives, empirical observations, and work decisions that arise during an agent session. It does not preserve or parse raw transcripts. The trigger boundary is doctrinal: read `gn help plan` before implementation, write during work when a decision arises, and read `gn help review` after finishing.

**Extraction.** Extraction is agent-mediated judgment, not a separate model pipeline. The oracle is the doctrine's filter: prefer perishable human or empirical knowledge, avoid code-reconstructable analysis, and prefer a code comment when the knowledge has a precise code anchor.

**Representational form and behavioral authority.** The retained form is prose in JSONL. The entries are mostly knowledge artifacts: future agents search them as facts and decision context. The AGENTS hook is system-definition, but entries themselves do not automatically rewrite guidance or policy.

**Scope and timing.** Scope is per repository. Timing is online/manual during normal work, with a session-end review pass. It is lighter than ClawVault or Pi Self-Learning because there is no event hook or transcript miner, but stronger than an ordinary notes file because the CLI and AGENTS doctrine define a recurring capture loop.

**Survey placement.** On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), Gnosis adds a doctrine-mediated live-capture subtype: agent judgment distills session context directly into a repo-local prose memory store. It strengthens the survey claim that candidate generation is tractable, but also splits "trace-derived" into automatic log mining and instruction-mediated live extraction. Its weak point is evaluation: entries have no confidence, freshness, recurrence, or validation mechanism beyond future agents choosing whether to trust and update them.

## Curiosity Pass

Gnosis is intentionally almost all edge and almost no middle. The edge is strong: two AGENTS lines, a tiny CLI, git-visible entries, and fast search. The missing middle is curation. A noisy entry and a high-value entry have the same shape; an obsolete entry and a current entry differ only if someone edits or removes one.

The project has a good answer to "why won't this become a dumping ground?" but the answer is doctrine, not mechanism. The current self-use entries show the intended genre: release-pipeline rationale, a rejected MCP server, and an FTS5-vs-Bleve tradeoff. That is real signal. The code does not stop an agent from writing duplicated analysis; only the instructions do.

The search model is enough for repo-scale why-memory, but it is not a context scheduler. Search returns snippets and topic/ID lines; it does not know which entries should load automatically for a file, test, command, or task type. That keeps the tool portable, but leaves activation quality to the agent's choice of query terms.

The related-ID field is a seed of structure, not a graph model. It supports supersession or adjacency in entries, but there is no backlink view, relation label, required reason for the link, or validation that a relation still makes semantic sense.

## What to Watch

- Whether Gnosis adds entry kinds, confidence, freshness, or stale/superseded states without losing its capture-first product stance.
- Whether search activation becomes more task-aware: file-path scoped search, AGENTS-invoked query suggestions, or command wrappers that search from changed files.
- Whether the rejected MCP path stays rejected as coding agents standardize around shell access, or whether MCP-only agent surfaces create pressure for a second interface.
- Whether the human-context filter survives broad agent use; if not, structural gates may become necessary.
- Whether related IDs grow into explicit supersession or contradiction semantics.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Gnosis adds doctrine-mediated live capture, where an agent extracts session context directly into repo-local prose memory without mining raw transcripts.
- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — exemplifies: durable memory is committed JSONL, while SQLite FTS is a disposable cache.
- [agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — exemplifies: Gnosis changes repo instructions, shell workflow, source control, and search behavior rather than adding only a memory backend.
- [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — sharpens: Gnosis solves low-friction candidate capture but leaves trust, retirement, and abstraction to human/agent judgment.
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: Gnosis captures session learnings but has no separate workshop lifecycle before durable entry creation.
