---
description: "TraceCraft review: CLI coordination layer with bucket-backed memory, mailbox, claims, artifacts, and mirrored agent transcripts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-02"
---

# tracecraft

TraceCraft, from Arrmlet's `tracecraft` repository, is a CLI-first coordination layer for multi-agent AI runs. It does not own the model loop or provide semantic recall. It stores shared key-value memory, messages, task claims, handoffs, artifacts, agent registration, and mirrored harness transcripts as project-scoped JSON or file objects in S3-compatible or HuggingFace buckets.

**Repository:** https://github.com/Arrmlet/tracecraft

**Reviewed commit:** [7d77daaaf17d3f18b7718e3ddfc8ee2576446adc](https://github.com/Arrmlet/tracecraft/commit/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc)

**Last checked:** 2026-06-02

## Core Ideas

**The bucket is the coordination substrate.** The SDK exposes a small Python CLI whose storage factory returns either an S3 wrapper or a HuggingFace Buckets wrapper. Every operation writes or reads objects under a project prefix, so the bucket becomes the durable shared state for agents that may be running in different terminals, worktrees, hosts, or clouds ([store.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/store.py), [s3.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/s3.py), [hf.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/hf.py)).

**Coordination memory is plain JSON, not semantic memory.** `memory set/get/list` maps dotted keys to `memory/...json` objects with a value, writer id, and timestamp. There is no embedding index, summarizer, retrieval model, or schema beyond CLI conventions; agents must know or list the keys they want ([memory.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/memory.py)).

**Atomic claims are the strongest behavior-shaping primitive.** `claim` writes `steps/<id>/claim.json` with `if_none_match=True`; the S3 backend turns that into `IfNoneMatch="*"`, while the HuggingFace backend documents a best-effort check-then-write fallback. The losing caller reads the existing owner and errors rather than overwriting the claim ([steps.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/steps.py), [s3.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/s3.py), [hf.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/hf.py), [Tier 0 tests](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tests/test_tier_0.py)).

**The read-back model is explicit CLI pull.** Agents read memory with `tracecraft memory get/list`, messages with `inbox`, completion state with `step-status` or `wait-for`, artifacts with `artifact download`, and transcripts with `session show`. Example Claude Code and Hermes skill files instruct agents to run these commands, but the implementation does not inject recalled state into a model request or fire relevance-gated hooks ([CLI entrypoint](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/__init__.py), [examples/claude-code/CLAUDE.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/examples/claude-code/CLAUDE.md), [examples/hermes-agent/SKILL.md](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/examples/hermes-agent/SKILL.md)).

**Session mirroring preserves traces beside coordination state.** The `session mirror` command discovers harness transcripts for Claude Code, Codex, OpenClaw, and Hermes, reads new bytes or SQLite rows from a cursor, redacts common token shapes by default, uploads append-disjoint `part-*.jsonl` objects, and maintains cumulative `meta.json` with redaction counts and part metadata ([session.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/cli/session.py), [harness base](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/base.py), [Hermes adapter](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/harness/hermes.py), [redact.py](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/sdk/tracecraft/redact.py), [session mirror docs](https://github.com/Arrmlet/tracecraft/blob/7d77daaaf17d3f18b7718e3ddfc8ee2576446adc/docs/session-mirror.md)).

**Context efficiency is operational rather than semantic.** TraceCraft keeps model context small by not loading anything automatically: agents issue targeted CLI reads for specific keys, inboxes, steps, artifacts, or transcript tails. That avoids always-loading a large memory store, but it also means relevance, completeness, and follow-through depend on the harness instructions and the agent's command choices.

## Artifact analysis

- **Storage substrate:** `files` — Project-scoped bucket objects under `memory/<key path>.json`
- **Representational form:** `prose` `symbolic` — Symbolic JSON envelopes carry prose values, messages, handoff notes, transcript rows, and instruction files; there is no embedding or learned parameter store
- **Lineage:** `authored` `imported` `trace-extracted` — Agents author memory, messages, claims, registry rows, and examples; artifact uploads import local files; session mirroring copies harness transcripts and metadata from trace stores
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` — Most retained objects advise as context or evidence, loaded examples instruct agents, conditional claims and waits gate work, and messages, handoffs, claims, and registry rows coordinate recipients and task ownership

**Shared memory entries.** Storage substrate: project-scoped bucket objects under `memory/<key path>.json`. Representational form: symbolic JSON carrying a prose scalar value plus `set_by` and `set_at` metadata. Lineage: authored directly by an agent or script through `tracecraft memory set`; listing and dotted-path conversion are derived views, not separate durable artifacts. Behavioral authority: knowledge artifact authority. A later agent can use the value as shared context or evidence, but TraceCraft does not promote it into an instruction, validator, or automatic prompt input.

**Messages and broadcasts.** Storage substrate: bucket objects under `messages/<recipient>/<timestamp>_<sender>.json` and `messages/_broadcast/...`. Representational form: symbolic envelope plus prose message. Lineage: authored by the sending agent with second-resolution timestamp naming. Behavioral authority: advisory communication for the recipient; `inbox --delete` can remove read messages, but there is no durable acknowledgement protocol beyond deletion.

**Task claims, status, and handoffs.** Storage substrate: bucket objects under `steps/<step>/claim.json`, `status.json`, and `handoff.json`. Representational form: symbolic JSON with prose handoff notes. Lineage: authored by `claim`, `complete`, and status reads; the S3 claim object is protected by conditional create, while status and handoff are ordinary writes. Behavioral authority: system-definition-like coordination authority. A claim can block competing work, `wait-for` can gate later work until completion, and handoff notes advise the next agent.

**Artifacts.** Storage substrate: bucket objects under `artifacts/<step-or-shared>/<filename>`. Representational form: arbitrary file bytes named and routed by CLI convention. Lineage: imported from local files through `artifact upload`; source path and producer step are not deeply encoded beyond bucket key and command output. Behavioral authority: knowledge or work-product artifacts consumed by later agents through explicit download.

**Agent registry records.** Storage substrate: bucket objects under `agents/<agent>.json`, written during `init`. Representational form: symbolic JSON with status, step, heartbeat, and summary fields. Lineage: authored at initialization in this commit; the code marks stale heartbeats when listing, but does not refresh heartbeat after init. Behavioral authority: advisory coordination state for humans or agents deciding who else is active.

**Mirrored session transcripts.** Storage substrate: bucket objects under `sessions/<harness>/<session-id>/part-*.jsonl` plus `meta.json`, with local cursor state in `~/.tracecraft/mirror-state/`. Representational form: mixed raw JSONL bytes, synthesized Hermes JSONL rows, symbolic part metadata, and redaction-count JSON. Lineage: copied from harness session stores by append cursor, optionally regex-redacted before upload; meta records cursor ranges and source paths. Behavioral authority: audit and context artifact. A later agent can inspect transcript tails, but the implementation does not distill transcripts into rules, memories, or tool definitions.

**CLI examples and skill/instruction files.** Storage substrate: checked-in Markdown files under `examples/` and repository docs. Representational form: prose procedure and command snippets. Lineage: authored project guidance. Behavioral authority: system-definition artifact only when a host harness loads the file as instructions; it tells agents to use TraceCraft commands but does not itself activate stored bucket state.

Promotion path: TraceCraft has a promotion path from a task claim to coordination lock, and from completed work to handoff/artifact availability. It does not have a code-grounded promotion path from raw traces or memory values into validated durable instructions, generated skills, semantic facts, or retrieval-ranked context.

## Comparison with Our System

| Dimension | TraceCraft | Commonplace |
|---|---|---|
| Primary purpose | Cross-agent coordination through shared bucket state | Git-native methodology KB for agent-operated knowledge bases |
| Canonical retained artifacts | Bucket JSON objects, artifact files, mirrored transcript parts, local config/state | Typed Markdown notes, instructions, reviews, ADRs, sources, generated indexes |
| Storage substrate | S3-compatible or HuggingFace bucket, plus local config/cursor files | Repository files with validation, diffs, and generated indexes |
| Write path | Stateless CLI commands and session mirror runs | Authored notes, source snapshots, validators, review gates, index refreshes |
| Read-back | Explicit CLI reads and polling | Mostly explicit pull through `rg`, indexes, links, skills, and validation workflows |
| Governance | Atomic S3 claim creation, bucket scoping, basic redaction, tests for shipped primitives | Collection contracts, type specs, schema validation, semantic review gates, git lineage |

TraceCraft and Commonplace both prefer inspectable retained artifacts over hidden platform memory. The important difference is authority. TraceCraft is an operational coordination substrate: it helps several agents avoid duplicated work, pass handoffs, share files, and inspect transcripts. Commonplace is a knowledge-methodology substrate: it makes retained claims and procedures reviewable, typed, searchable, and validatable.

**Read-back:** `pull` — Stored memory, messages, artifacts, step state, and session transcripts reach the agent only when the agent or harness explicitly calls the CLI; the code does not implement relevance-gated push activation, automatic prompt injection, or memory faithfulness tests

The design is attractive where coordination failure is the main risk. Atomic claim writes are a stronger primitive than prose "I am working on X" notes, and bucket storage makes the coordination surface work across hosts without requiring all agents to share a local process. It is weaker as a knowledge system: values are scalar, lineage is coarse, no schema validates memory keys, and session traces remain raw audit material rather than reviewed knowledge artifacts.

### Borrowable Ideas

**Use object-store conditional create for distributed work claims.** Ready for operational workflows. Commonplace could borrow this when multiple agents are assigned independent review or migration tasks outside one git worktree, using claims as coordination locks rather than as knowledge artifacts.

**Keep coordination memory separate from durable KB promotion.** Ready now as design vocabulary. TraceCraft is useful precisely because its quick handoffs do not pretend to be curated notes. Commonplace should keep ephemeral agent coordination in workshop/log surfaces until something earns a typed artifact.

**Mirror agent sessions as audit evidence, not automatic memory.** Needs a privacy and retention policy first. TraceCraft's append-disjoint session parts plus redaction counts are a practical audit substrate, but Commonplace should route them into source/workshop material rather than automatically deriving instructions.

**Borrow bucket-browsability as an adoption affordance.** Ready as a product lesson. A coordination tool is easier to trust when operators can inspect the exact JSON objects in MinIO, AWS, R2, or HuggingFace without a custom UI.

**Do not borrow scalar key-value memory as a KB substitute.** Ready now. Dotted key paths are convenient for coordination, but they lack the type contracts, citations, review state, and link semantics Commonplace needs for durable methodology knowledge.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The README's "memory" is coordination memory.** The implementation stores named values and handoff notes; it does not retrieve semantically similar memories or summarize prior work for the agent.

**The strongest system-definition artifact is a lock.** The claim object has immediate behavioral force because a second agent is rejected. Most other artifacts are advisory until an agent chooses to read them.

**HuggingFace support trades browsability for weaker atomicity.** The HF backend has the same interface, but its conditional claim is a check-then-write fallback rather than S3's conditional put. That distinction matters if Commonplace borrows the claim pattern.

**Session mirroring is close to trace-derived learning but stops at trace retention.** The code preserves raw transcript traces and metadata, then offers `session show`; it does not extract lessons, policies, selectors, or embeddings from those traces.

**Heartbeat semantics are currently thinner than the registry shape suggests.** `init` writes a heartbeat and `agents` marks records stale after five minutes, but no recurring heartbeat writer is implemented at this commit.

## What to Watch

- Whether claims gain TTL, owner refresh, or stale-claim recovery; that decides whether TraceCraft can coordinate long-running agent work without manual cleanup.
- Whether memory keys gain schemas, namespaces, or compare-and-set writes; that would move the system from loose coordination notes toward stronger shared state.
- Whether session mirroring adds trace-to-summary or trace-to-handoff distillation; that would change the trace-derived classification and require governance around extracted artifacts.
- Whether push-oriented harness integrations appear, such as pre-turn inbox/memory injection or relevance-gated reminders; that would change the read-back classification.
- Whether redaction expands from regex token shapes to configurable project policy; mirrored transcripts are high-value audit evidence but also high-risk retained data.

## Bottom Line

TraceCraft is best read as a serverless coordination ledger for agent fleets, not as an agent memory system in the semantic-recall sense. Its durable artifacts can shape behavior by preventing duplicate task claims, exposing handoffs, and making transcript evidence available on demand. Under the current review rules, it does not qualify for `trace-derived` because it retains raw traces without deriving durable behavior-shaping artifacts from them, and it does not qualify for `push-activation` because read-back is explicit CLI pull rather than engineered activation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: TraceCraft stores shared state and traces, but stored objects affect action only when explicitly read.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: TraceCraft's memory values, claims, handoffs, artifacts, transcripts, and examples differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: memory entries, messages, artifacts, registry rows, and transcript parts mostly advise as context or evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: claim objects, CLI procedures, and loaded example instructions can constrain or route future work.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - clarifies: TraceCraft's bucket objects count when later agents can consume them in behavior-shaping ways.
