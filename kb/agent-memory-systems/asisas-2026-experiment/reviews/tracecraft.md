---
description: "Tracecraft review: serverless bucket-backed multi-agent coordination with JSON memory, atomic claims, mailboxes, artifacts, and session mirroring"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# Tracecraft

Tracecraft, from `Arrmlet/tracecraft`, is a Python CLI and SDK for coordinating multiple AI agents through a shared S3-compatible or HuggingFace bucket. At the reviewed commit it stores project-scoped JSON objects for agent presence, key-value memory, messages, task claims, step status, handoffs, artifacts, and mirrored harness sessions without running a server or database.

**Repository:** https://github.com/Arrmlet/tracecraft

**Reviewed commit:** [7d77daaaf17d3f18b7718e3ddfc8ee2576446adc](https://github.com/Arrmlet/tracecraft/commit/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc)

**Last checked:** 2026-06-05

## Core Ideas

**The bucket is the coordination substrate.** Tracecraft writes every shared object under a project prefix: `agents/`, `memory/`, `messages/`, `steps/`, `artifacts/`, and `sessions/`. S3 uses `put_object`, `get_object`, paginated `list_objects_v2`, upload/download, and conditional `IfNoneMatch`; the HuggingFace backend exposes the same interface through `HfFileSystem`, with best-effort check-then-write for conditional puts ([README.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/README.md), [sdk/tracecraft/s3.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/s3.py), [sdk/tracecraft/hf.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/hf.py)).

**Memory is explicit shared state, not semantic recall.** `tracecraft memory set` stores a string value with `set_by` and `set_at`; `memory get` reads one key; `memory list` enumerates keys by prefix. Dotted names become object paths, but there is no embedding index, learned retriever, or consolidation loop over stored memories ([sdk/tracecraft/cli/memory.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/memory.py)).

**Task ownership is enforced by object creation, not an agent scheduler.** `claim` writes `steps/<id>/claim.json` with `if_none_match=True`; the first writer wins and later claimers read the existing owner. `complete` writes status plus a handoff note, and `wait-for` polls status until dependencies are complete ([sdk/tracecraft/cli/steps.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/steps.py), [sdk/tests/test_tier_0.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tests/test_tier_0.py)).

**Context efficiency is procedural and pull-oriented.** Tracecraft does not assemble a prompt context or decide which memories are relevant. It keeps shared state outside the model until an agent deliberately calls `memory get`, `inbox`, `step-status`, `wait-for`, `artifact download`, or `session show`; the main efficiency win is that agents can fetch small coordination records instead of pasting a full shared run history into every prompt ([sdk/tracecraft/cli/__init__.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/__init__.py), [examples/claude-code/CLAUDE.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/examples/claude-code/CLAUDE.md)).

**Session mirroring records traces for inspection, not learning.** The mirror command tails Claude Code, Codex, OpenClaw, or Hermes sessions, redacts known token shapes by default, uploads append-disjoint JSONL parts, and maintains `meta.json` with cursor ranges and redaction counts. The implementation preserves traces and provides list/show/tail operations; I did not find code that distills these traces into future instructions, rules, rankings, or learned memory ([docs/session-mirror.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/docs/session-mirror.md), [sdk/tracecraft/cli/session.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/session.py), [sdk/tracecraft/redact.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/redact.py)).

**Harness integration is adapter-light.** Claude Code, Codex, and OpenClaw adapters tail append-only JSONL files; Hermes reads a live SQLite database read-only and emits new `messages` rows as JSONL. The shared `Harness` protocol keeps discovery, active-session selection, incremental reads, and cursor sizing separate from storage ([sdk/tracecraft/harness/base.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/base.py), [sdk/tracecraft/harness/claude_code.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/claude_code.py), [sdk/tracecraft/harness/codex.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/codex.py), [sdk/tracecraft/harness/openclaw.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/openclaw.py), [sdk/tracecraft/harness/hermes.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/hermes.py)).

## Artifact analysis

- **Storage substrate:** `files` `kv` `service-object` - The durable store is bucket objects containing JSON records and uploaded files; shared memory is a key-value object namespace; local `.tracecraft.json` and mirror-state files hold credentials, project/agent identity, and cursors; S3 or HuggingFace bucket services provide the actual cross-agent substrate ([sdk/tracecraft/config.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/config.py), [sdk/tracecraft/store.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/store.py), [docs/s3-architecture.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/docs/s3-architecture.md)).
- **Representational form:** `prose` `symbolic` - Message bodies, handoff notes, memory values, and transcript contents are prose-like payloads; object paths, JSON schemas, timestamps, agent ids, step ids, cursor ranges, redaction counters, and status values are symbolic. The reviewed code does not persist embeddings, model weights, or a learned ranker.
- **Lineage:** `authored` `imported` `trace-extracted` - Agents and users author memory entries, messages, claims, statuses, and handoff notes through CLI commands; artifact uploads import local files into the bucket; session mirroring extracts raw harness traces from local JSONL files or Hermes SQLite rows into bucket parts.
- **Behavioral authority:** `knowledge` `routing` `enforcement` `validation` - Memory entries, messages, handoffs, artifacts, and session traces provide knowledge/reference context; step ids, agent ids, inbox paths, project prefixes, and wait barriers route work; S3 conditional creation enforces single-owner claims on S3-compatible backends; config checks, credential handling, gitignore insertion, redaction counts, and tests provide validation/governance evidence. Tracecraft does not turn retained state into prompt instructions by itself.

**Coordination JSON.** `agents/*.json`, `memory/**/*.json`, `messages/**/*.json`, and `steps/**/{claim,status,handoff}.json` are small symbolic/prose records. Their authority is strongest for routing and enforcement around work ownership; their content is otherwise advisory knowledge for the agents that explicitly read it.

**Artifacts.** Uploaded files under `artifacts/` are imported project outputs. Their form is arbitrary, but Tracecraft treats them as opaque files: it uploads, downloads, lists, and names them by step or shared scope rather than interpreting their contents ([sdk/tracecraft/cli/artifacts.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/artifacts.py)).

**Session parts and metadata.** Mirrored sessions are raw trace artifacts: append-disjoint `part-NNNNN-<uuid>.jsonl` objects plus `meta.json` with source path, cursor range, byte counts, redaction counts, and upload times. They are evidence and observability records, not distilled memory.

**Local config and mirror state.** `.tracecraft.json` and `~/.tracecraft/mirror-state/<session>.json` are system-definition artifacts for the CLI. They decide which project, bucket, backend, agent identity, and cursor position future commands use, but they are not shared agent memory.

Promotion path: Tracecraft can move an agent-produced file or note into a shared artifact, and it can move a local harness transcript into a bucket trace. It does not currently promote traces or repeated coordination records into instructions, validators, summaries, or higher-salience memories.

## Comparison with Our System

| Dimension | Tracecraft | Commonplace |
|---|---|---|
| Primary purpose | Cross-agent coordination through a shared bucket | Typed, source-grounded methodology KB for agents and maintainers |
| Canonical retained artifact | Project-scoped JSON objects, uploaded files, and mirrored session parts | Git-native Markdown notes, sources, reviews, indexes, schemas, and commands |
| Context control | Explicit CLI reads and small object namespaces | Search, indexes, links, collection/type contracts, validation, review gates |
| Write path | CLI writes objects; mirror copies traces; S3 conditional puts enforce claims | Authored file edits, snapshots, generated indexes, validation, semantic review |
| Read-back | Pull through commands such as `memory get`, `inbox`, `wait-for`, `artifact download`, and `session show` | Mostly pull through lexical search, indexes, links, and selected instructions |
| Governance | Bucket ownership, object-level history if backend supports it, redaction counts, tests | Git history, schemas, link checks, citations, review gates, collection contracts |

Tracecraft is closer to a shared coordination substrate than to a knowledge base. It gives multiple agents a lightweight, inspectable place to coordinate without owning their model loop. Commonplace gives agents durable methodology artifacts whose type, links, provenance, and validation status are part of the artifact itself.

The main divergence is authority. Tracecraft's strongest system authority is operational: claims, waits, inboxes, and artifacts help agents avoid collision. Commonplace's strongest system authority is semantic and procedural: type contracts, instructions, and validators determine what an artifact means and how it may change behavior.

Tracecraft's session mirror is valuable evidence capture, but it deliberately stops before distillation. Commonplace would treat those traces as source material or workshop evidence until a reviewed note, instruction, or validator is written from them.

### Borrowable Ideas

**Bucket-native coordination for parallel review work.** Ready when Commonplace needs multi-agent concurrency beyond git branches. A small object store namespace for claims, handoffs, and artifacts could prevent duplicate review work without making the bucket the KB source of truth.

**Atomic claim files as a coordination primitive.** Ready now as an operational pattern. Commonplace already has review runs and gates; a conditional-create claim object could make "one agent owns this note/run" explicit in distributed workflows.

**Keep traces and coordination events in one project namespace.** Useful with a concrete audit viewer. If Commonplace captures agent run traces, storing them beside review-run status and handoffs would make postmortems easier than splitting logs across tools.

**Append-disjoint trace parts with cumulative redaction metadata.** Ready for source snapshot workflows that handle long logs. The part-plus-meta design keeps uploads cheap and makes redaction visible without pretending regex redaction is complete.

**Do not borrow object-store authority for KB artifacts.** Tracecraft's bucket model is good for coordination, but Commonplace's durable knowledge value depends on repo review, diffability, schemas, and link validation. Bucket JSON should remain operational state or source evidence unless it is exported into typed files.

## Write side

**Write agency:** `manual` `automatic` - Agents and users manually write memory, messages, claims, completions, and artifacts through CLI calls; automatic command paths register agents during init, append `.tracecraft.json` to `.gitignore`, tail harness sessions, redact copied bytes, upload session parts, update session metadata, and advance local mirror cursor state.

**Curation operations:** `none` — Tracecraft does not perform the review contract's curation operations on existing stored memory. It overwrites simple key-value entries, updates status/meta records, and appends new trace parts, but I did not find automatic deduplication, consolidation, evolution, synthesis, invalidation, decay, or salience promotion over retained memories. Session mirroring is acquisition/preservation of traces, not trace-derived learning into new behavior-shaping artifacts.

## Read-back

**Read-back:** `pull` - Retained Tracecraft state reaches an agent when the agent, user, or surrounding harness deliberately calls CLI commands such as `memory get`, `memory list`, `inbox`, `step-status`, `wait-for`, `artifact download`, `session list`, or `session show`; the inspected implementation does not push stored memory into a model invocation or auto-inject retrieved content into prompts.

`wait-for` is still pull from the agent's perspective: the agent chooses to block on a step and receives completion only through that command. Broadcast messages and direct messages are also pull until an agent checks `inbox`. Static example instructions tell a Claude Code agent how to use Tracecraft, but they are shipped baseline guidance rather than read-back of accumulated memory.

Selection is symbolic and explicit. Agents choose keys, prefixes, step ids, recipient ids, artifact names, session ids, or harness names; there is no lexical, embedding, or judgment-based relevance selection over stored objects. Effective context dilution is therefore host-controlled: Tracecraft can keep reads small, but an agent can still choose to load too many messages, artifacts, or transcript tail lines.

Authority at consumption is mostly advisory context, except for coordination commands whose return values govern operational choices such as whether a step is already claimed or complete. The system does not test whether a fetched memory or handoff actually changes downstream model behavior.

## Curiosity Pass

**The system calls one namespace "memory," but its strongest mechanism is coordination.** The key-value memory API is intentionally simple; atomic claims, inboxes, handoffs, artifacts, and waits are the parts that most directly change what parallel agents do.

**Trace preservation is not trace learning.** Tracecraft mirrors sessions into the same bucket as coordination records, which is useful for audit and replay, but the current implementation does not create summaries, rules, skills, ranking signals, or prompt policy from those traces.

**The backend abstraction changes the guarantee.** S3-compatible backends can enforce first-writer-wins claims through `IfNoneMatch`; HuggingFace Buckets use a racy check-then-write fallback. A review of coordination reliability should not treat those as equivalent.

**Plain JSON is both the adoption win and the semantic limit.** Any agent can inspect bucket objects with a CLI or console, but Tracecraft has no typed interpretation layer beyond its command conventions.

**The session mirror is already a useful source-capture tool.** Even without learning, preserving redacted session parts and coordination records in one namespace can support later review, replay, and failure analysis.

## What to Watch

- Whether the planned replay surface ships and merges session traces with coordination events; that would turn Tracecraft from a coordination CLI into a run-inspection system with stronger Commonplace relevance ([plans/TRACES_V1_PLAN.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/plans/TRACES_V1_PLAN.md)).
- Whether session traces gain summarization, lessons, or policy extraction; that would change the review from raw trace storage to qualifying trace-derived learning.
- Whether TTL/heartbeat refresh, stale claim handling, or claim release policies land; those would strengthen operational enforcement for long-running multi-agent work.
- Whether HuggingFace conditional writes get a stronger compare-and-set mechanism; today Tracecraft's atomic-claim story is strongest on S3-compatible backends.
- Whether an agent-facing plugin or hook begins automatically injecting inbox, memory, or handoff content before prompts; that would change read-back from pull-only to push or both.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Tracecraft stores shared state and traces, but agents must explicitly read them for context.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: coordination JSON, artifacts, session traces, and local config have different substrates, forms, lineage, and authority.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: Tracecraft selection depends on explicit keys, step ids, agent ids, artifact names, and session ids.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrast: Tracecraft captures traces but does not yet extract behavior-shaping artifacts from them.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: memory values, messages, handoffs, artifacts, and session parts are evidence/reference unless a host agent gives them stronger authority.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: claims, waits, config, and mirror cursor state affect routing and enforcement rather than serving as ordinary knowledge.
