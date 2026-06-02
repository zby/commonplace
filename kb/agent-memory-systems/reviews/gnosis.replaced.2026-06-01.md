---
description: "Review of Gnosis, a repo-local CLI memory system where agents search and write JSONL decision entries through doctrine-mediated workflow"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Gnosis

> Replaced 2026-06-01. See [gnosis](./gnosis.md) for the current review.

Gnosis is a small Go CLI for repo-local agent memory by Stavros Korokithakis. It asks coding agents to search project memory before work, write decisions while context is fresh, and review the session afterward; the durable memory is a `.gnosis/entries.jsonl` file in the repository, with a disposable SQLite FTS5 index in a per-repo cache directory.

**Repository:** https://github.com/skorokithakis/gnosis

**Reviewed commit:** [1eb0aa7e575945154c79b65871446cffa07a1847](https://github.com/skorokithakis/gnosis/commit/1eb0aa7e575945154c79b65871446cffa07a1847)

## Core Ideas

**The memory contract is two AGENTS.md lines plus a CLI.** The README's adoption path is deliberately small: add instructions telling agents to run `gn help plan` at task start and `gn help review` after finishing ([README](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/README.md)). The repo's own `AGENTS.md` repeats the contract as a workflow: search before implementation, record decisions as they happen, and review at the end ([AGENTS.md](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/AGENTS.md)). That makes the behavior-shaping artifact a prose system-definition artifact when loaded by an agent, while the CLI is the symbolic tool surface that stores and retrieves entries.

**Entries are repo-local knowledge artifacts with a narrow schema.** The canonical stored object is `Entry`: `id`, normalized `topics`, free-form `text`, `related` IDs, and timestamps ([storage.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/storage/storage.go)). Writes normalize and deduplicate topics, validate related ID prefixes, timestamp the entry, and append one JSON object per line to `.gnosis/entries.jsonl` ([write.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/write.go)). The stored entry is prose plus light symbolic metadata; its authority is advisory evidence for future agents unless AGENTS.md or human instruction makes a specific entry binding.

**The source of truth, index, and runtime lock are separated.** `.gnosis/entries.jsonl` is the durable storage substrate. The SQLite FTS5 `index.db` and flock file live under an XDG cache path keyed by a hash of the repo root, not in the repository ([paths.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/paths/paths.go), [index.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/index/index.go)). `EnsureFresh` rebuilds the index when the JSONL mtime changes, and `reindex` can force a rebuild ([index.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/index/index.go), [reindex.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/reindex.go)). This is a clean lineage rule: cache state is regenerated from JSONL, while JSONL is the retained artifact that travels with the code.

**Search is activation by doctrine, not background scheduling.** `gn search` sanitizes bare queries, preserves intentional FTS5 syntax, ensures the index is fresh, and prints ID/date/topic/snippet rows ([search.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/search.go)). The `plan` doctrine tells agents to search with task keywords before writing code and surface conflicting recorded decisions before proceeding ([plan.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/plan.txt)). The system has no automatic router that injects relevant entries into the prompt; activation depends on agents obeying the loaded instructions.

**Show, edit, remove, latest, and topics keep the store inspectable.** `show` dispatches short targets to ID-prefix lookup and longer targets to topic lookup, then prints full entries with related IDs and timestamps ([show.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/show.go)). `edit` supports both `$EDITOR` and non-interactive body replacement, preserving metadata unless the interactive buffer changes it ([edit.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/edit.go)). `rm` removes entries but only warns about dangling related references rather than silently mutating survivors ([rm.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/rm.go)). The lifecycle is therefore manual and auditable, but not governed by review states, validation gates, or supersession semantics beyond optional related links.

**The doctrine is a noise filter.** `plan.txt` and `review.txt` tell agents to record human knowledge, rejected alternatives, cross-cutting decisions, empirical observations, and future intent, while excluding reproducible code analysis, API contracts, TODOs, and facts that belong in comments or docs ([plan.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/plan.txt), [review.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/review.txt)). This is the central governance mechanism: the system relies on prose instruction at capture time rather than schema enforcement at storage time.

## Comparison with Our System

| Dimension | Gnosis | Commonplace |
|---|---|---|
| Primary durable store | Repo-local `.gnosis/entries.jsonl` | Git-tracked typed Markdown artifacts |
| Storage/index split | JSONL source of truth; SQLite FTS5 cache outside repo | Markdown source artifacts plus generated indexes/reports |
| Representational form | Prose entries with symbolic topic, ID, relation, timestamp metadata | Prose, frontmatter, schemas, commands, indexes, skills, and validation rules |
| Behavioral authority | Doctrine instructs agents; entries advise future agents unless promoted by outside instruction | Collection/type specs, AGENTS.md, skills, validation, and reviews distinguish advice from instruction/enforcement |
| Lineage | Entry timestamps, git history, optional related IDs; cache regenerated from JSONL | Source links, derivation notes, frontmatter, git history, generated indexes, review lifecycle |
| Activation | Agent must run search because doctrine says so | Agent navigation, indexes, skills, type contracts, validation, and explicit loading conventions |
| Governance | Prose capture policy and manual edit/remove | Structural validation, collection rules, semantic review, generated indexes, and lifecycle states |

Gnosis is much smaller and more adoption-oriented than commonplace. It optimizes for a one-commit adoption path: install a binary, commit two AGENTS.md lines, and let future agents accumulate "why" entries in the repo. Commonplace asks for a full knowledge-base methodology: typed collections, review gates, generated indexes, and more authoring discipline.

The most important alignment is that both systems treat repo-local, inspectable artifacts as the right substrate for agent memory. The difference is contract strength. In Gnosis, entries are intentionally lightweight knowledge artifacts, and behavioral authority mostly comes from the doctrine that tells agents when to search and write. In commonplace, many retained artifacts are system-definition artifacts with explicit instruction, validation, routing, or review force.

Gnosis also draws a sharper line between canonical storage and runtime acceleration than many memory systems. The SQLite index is disposable, keyed outside the repo, and rebuilt from JSONL. Commonplace's generated indexes follow a similar principle, but commonplace makes more derived surfaces visible in the repository because they are part of navigation and review.

**Read-back:** pull — doctrine tells agents to run `gn search`; entries are not injected automatically.

## Borrowable Ideas

**Adopt through native agent instructions.** The two-line AGENTS.md adoption path is immediately borrowable as a packaging lesson. Commonplace skills and commands are more powerful, but each promoted workflow should have an equally small "how an agent starts using this" contract.

**Keep the first memory primitive boring.** JSONL plus FTS5 is enough for a useful per-repo "why" memory. Commonplace should keep richer types where they pay for themselves, but Gnosis is evidence that an initial capture path can be deliberately simple and still behavior-changing.

**Separate canonical memory from caches aggressively.** Gnosis's JSONL/cache split is ready to borrow as a documentation pattern for generated surfaces: name the source of truth, name the rebuild path, and make disposable acceleration state visibly non-authoritative.

**Use doctrine as a capture oracle before adding schema.** The "record what the human knows" rule is a good filter for agent-written memory. Commonplace can reuse the principle when writing capture instructions, while still relying on stronger type contracts for promoted notes.

**Expose manual lifecycle commands early.** `edit`, `rm`, `reindex`, `latest`, and `topics` are small, but they make the store livable. Commonplace's maintenance commands are broader; the borrowable lesson is that memory systems need first-class cleanup and inspection from the start, not only write/search.

## Trace-derived learning placement

Gnosis qualifies as trace-derived learning only in a narrow, doctrine-mediated sense. It does not automatically mine transcripts, tool logs, commits, or hidden execution traces. Instead, the loaded agent is instructed to inspect the live task context and extract durable memory entries through explicit CLI calls during and after the session.

**Trace source.** The source trace is the current agent work session: user context, decisions made during implementation, rejected alternatives, empirical observations, and end-of-session review. The `plan` and `review` doctrine define these boundaries and repeatedly prefer human-supplied context over agent-reproducible code analysis ([plan.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/plan.txt), [review.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/review.txt)).

**Extraction.** The extraction oracle is the acting agent following prose doctrine. The agent decides what is worth retaining, then uses `gn write <topics> <text> [--related id,id]` to create the retained entry ([write.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/commands/write.go)). There is no separate judge, summarizer, classifier, confidence score, or automatic transcript pass.

**Storage substrate.** Raw session context is not stored by Gnosis. Distilled entries live as JSONL in `.gnosis/entries.jsonl`; search acceleration lives in an external SQLite FTS5 cache; lock files are runtime coordination state ([storage.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/storage/storage.go), [index.go](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/index/index.go)).

**Representational form.** The retained operative part is prose text, with symbolic topics, IDs, related links, and timestamps. The index is distributed over SQLite FTS structures for retrieval, but it is not the canonical retained memory.

**Lineage.** Entry lineage is thin: timestamps, git history for the JSONL file, and optional related IDs. The repo's own `.gnosis/entries.jsonl` demonstrates the intended entry shape: concise decision records with topics, rationale, rejected alternatives, and timestamps ([entries.jsonl](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/.gnosis/entries.jsonl)). There is no retained pointer back to a specific chat transcript or tool trace.

**Behavioral authority.** The raw session is ephemeral evidence. The JSONL entries are knowledge artifacts when future agents read them as context or evidence. `AGENTS.md` and doctrine are system-definition artifacts because they instruct agents to search, surface conflicts, write entries, and tidy stale knowledge ([AGENTS.md](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/AGENTS.md), [plan.txt](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/internal/doctrine/plan.txt)).

**Scope and timing.** The scope is per-repository and cross-session. Extraction happens online during the task and in a staged end-of-session review, not offline over a corpus of accumulated transcripts.

**Survey placement.** Gnosis strengthens the survey claim that trace-derived memory often depends more on the capture oracle than on the storage technology. It sits on the manual/live-extraction end of the axis: the trace is available to the acting agent, but the system only retains the agent's explicit distilled entry.

## Curiosity Pass

**The system's strongest behavior is outside the binary.** The CLI stores, searches, edits, removes, and indexes. The agent-memory behavior comes from whether future agents actually obey `gn help plan` and `gn help review`. That makes adoption cheap, but also makes activation fragile when an agent ignores or only partially follows repository instructions.

**There is no promotion ladder inside Gnosis.** A Gnosis entry can warn, explain, or influence a future agent, but the system does not promote high-confidence entries into stronger artifacts such as tests, scripts, validation rules, AGENTS.md changes, or typed docs. Promotion must happen through ordinary development work outside Gnosis.

**Topic length is an artifact of CLI dispatch.** Topics must normalize to at least seven characters so `show` can treat six-or-fewer characters as ID prefixes. This is a practical symbolic constraint created by the human-facing command surface, not by the memory model itself.

**The related-link model is intentionally weak.** Entries can point to related IDs, but deletion only warns about dangling references. That keeps cleanup simple and auditable, while leaving graph integrity and supersession policy to agents and humans.

**The product strategy is coherent with the implementation.** The docs frame Gnosis as "agent memory infrastructure" that spreads through repos rather than org-wide tooling, and the code matches that strategy: shell CLI, repo-local JSONL, cache outside repo, and no server or MCP dependency ([PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/1eb0aa7e575945154c79b65871446cffa07a1847/docs/PRODUCT_STRATEGY.md)).

## What to Watch

- Whether Gnosis adds an MCP server or keeps betting on shell access as the common interface for coding agents.
- Whether signal-to-noise pressure leads from doctrine-only filtering toward structural fields such as source, confidence, expiry, reviewer, or promotion target.
- Whether entries gain explicit supersession or stale-state semantics beyond remove and related links.
- Whether AGENTS.md adoption remains enough once multiple agent harnesses interpret instructions differently.
- Whether the JSONL format grows import/export or merge-resolution tooling as `.gnosis` directories become shared through normal git collaboration.

---

Relevant Notes:

- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Gnosis entries advise future agents as retained evidence and context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: AGENTS.md and doctrine carry instruction force for agent behavior
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same prose may advise as an entry or instruct as loaded doctrine
- [lineage](../../notes/definitions/lineage.md) - frames: JSONL is canonical while FTS index state is regenerated cache
- [retained artifact](../../notes/definitions/retained-artifact.md) - grounds: only explicit entries persist; raw session context is not retained by Gnosis
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - compares-with: Gnosis depends on doctrine-driven search before implementation
- [Memory management policy is learnable but oracle dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - explains: Gnosis's capture quality depends on the agent's doctrine-following judgment
