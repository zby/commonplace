---
description: "Decapod review: Rust repo-native governance kernel with SQLite stores, context capsules, trace lessons, proof gates, and pull-first memory reads"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# Decapod

Decapod, from DecapodLabs, is a Rust CLI and JSON-RPC governance kernel for AI coding agents. At the reviewed commit it installs repo-local `.decapod/` state, generated agent entrypoints and project specs, SQLite-backed todo/knowledge/preference/graph stores, deterministic context capsules, workunit/proof gates, context internalization manifests, and event ledgers. The source-visible design is daemonless and local-first: agents or host workbenches call Decapod at governance boundaries rather than relying on a resident memory service.

**Repository:** https://github.com/DecapodLabs/decapod

**Reviewed commit:** [deea0f186770737758f94d146ef637811a6ee958](https://github.com/DecapodLabs/decapod/commit/deea0f186770737758f94d146ef637811a6ee958)

**Last checked:** 2026-06-04

## Core Ideas

**The retained surface is a governance substrate, not a transcript store.** The README describes `.decapod/` as the repo-native place for generated specs, deterministic context capsules, proof artifacts, durable data, config, and local overrides, and `Cargo.toml` frames the package as a governance runtime rather than a chat-memory product ([README.md](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/README.md), [Cargo.toml](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/Cargo.toml)). The CLI exposes init, session, todo, governance, data, context, QA, and RPC command groups, so memory is interleaved with claims, workspaces, validation, and proof ([src/cli.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/cli.rs)).

**Agent behavior is anchored by generated entrypoints and project specs.** `decapod init` scaffolds agent entrypoint files, `.decapod/config.toml`, project specs, CI, and capsule policy defaults; it can infer repo language/surface signals and seed validation criteria from them ([src/core/scaffold.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/scaffold.rs), [src/lib.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/lib.rs)). The checked-out project also carries its own `.decapod/README.md`, `OVERRIDE.md`, and config, which illustrates the intended local control-plane layout ([.decapod/README.md](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/.decapod/README.md), [.decapod/config.toml](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/.decapod/config.toml)).

**Context efficiency is deterministic and policy-bound.** `query_embedded_capsule_governed` validates scope, selects embedded or merged doc fragments, truncates to a caller/policy limit, records source paths and snippets, attaches policy metadata, and hashes a canonical capsule; `--write` persists the JSON under `.decapod/generated/context/` and can bind it to a workunit state ref ([src/core/context_capsule.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/context_capsule.rs), [src/lib.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/lib.rs)). Fragment resolution is rule/lexical: op, path, and tag bindings add boosts, query terms count occurrences, and deterministic ordering chooses the returned snippets ([src/core/docs.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/docs.rs)). This bounds volume and makes provenance inspectable, but it does not prove semantic relevance.

**Knowledge has lifecycle controls before it becomes procedural.** The knowledge plugin stores rows in `knowledge.db`, validates provenance schemes, statuses, TTL policies, conflict policies, temporal filters, retrieval feedback, decay events, and a promotion firewall for `procedural/` entries ([src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/knowledge.rs)). The federation plugin adds a typed graph of decisions, commitments, preferences, lessons, observations, and edges, with statuses, priorities, confidence values, event replay, and derived exports ([src/plugins/federation.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/federation.rs)).

**Governance artifacts carry real enforcement authority.** Workunit manifests bind intent refs, spec refs, state refs, proof plans, proof results, and a governed `VERIFIED` transition that requires planned gates to pass ([src/core/workunit.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/workunit.rs)). Validation runs multiple gates over the repo, `.decapod` state, capsule policies, internalization manifests, and workunit/proof surfaces, with bounded-time diagnostics for lock contention ([src/core/validate.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/validate.rs), [tests/validate_termination.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/tests/validate_termination.rs)).

**Compiled context is treated as a governed artifact.** The internalize plugin turns a local source file into a hashed adapter directory and manifest with source hash, model id, profile, binary hash, replay recipe, capabilities contract, risk tier, TTL, and session-scoped mount leases; attach refuses expired, corrupted, source-mismatched, replay-inconsistent, or tool-forbidden artifacts ([src/plugins/internalize.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/internalize.rs)). At this commit the built-in profile is a noop adapter, so the code-grounded value is the manifest, lease, and integrity contract rather than demonstrated model-side compression.

## Artifact analysis

- **Storage substrate:** `files` — Decapod's retained state persists under repo/user filesystem roots: `.decapod/` files, generated specs/context/artifacts/session mounts, SQLite database files, JSONL ledgers, workunit manifests, proof records, and derived graph/vault exports. SQLite is important, but it is file-backed local control-plane state rather than a hosted service.
- **Representational form:** `prose` `symbolic` — Prose appears in entrypoints, project specs, constitution/docs fragments, knowledge bodies, lessons, summaries, prompts, and overrides; symbolic form appears in TOML config, JSON manifests, SQLite rows, JSONL events, hashes, schemas, statuses, TTLs, proof gates, workunit states, capsule policies, and graph edges. I did not find durable parametric memory in the reviewed source.
- **Lineage:** `authored` `imported` `trace-extracted` — Operators and agents author tasks, knowledge, federation nodes, preferences, plans, specs, and overrides; init imports embedded templates and inferred repo signals; worker loops, LCM, retrieval feedback, proof/verification, todo events, and promotion ledgers extract durable records from operational traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Entries, capsules, summaries, and graph nodes advise as knowledge; entrypoints, project specs, procedural knowledge, aptitude prompts, and mounted adapters can instruct; workunit transitions, proof gates, validation, workspace rules, capability contracts, and promotion requirements enforce or validate; todo claims, path/op/tag bindings, graph edges, and ranking/recency options route attention; event-derived lessons and preferences feed later learning surfaces.

**Entrypoints, overrides, and generated specs.** Storage substrate: repository files such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `.decapod/OVERRIDE.md`, `.decapod/config.toml`, and `.decapod/generated/specs/*`. Representational form: prose instructions plus symbolic config and manifest metadata. Lineage: generated from scaffold templates, inferred repo context, explicit init seeds, and local override edits. Behavioral authority: system-definition artifacts with instruction/routing force for agents and validators, while specs also act as knowledge artifacts about the project.

**Deterministic context capsules.** Storage substrate: embedded assets merged with repo-local docs and optional `.decapod/generated/context/*.json` files. Representational form: prose snippets plus symbolic source refs, policy binding, task/workunit ids, schema version, and SHA-256 hash. Lineage: assembled from embedded constitution/docs and local project specs at query time; invalidated by changed source docs, policy, topic, scope, limit, task/workunit binding, or repo-local overrides. Behavioral authority: knowledge when read as context, routing/scoping when capsule policy constrains allowed scope and write behavior.

**Todo, session, ownership, and worker traces.** Storage substrate: SQLite task state, JSONL events, claim-status caches, agent presence, category ownership, and rebuildable ledgers in `.decapod/data/` ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/todo.rs)). Representational form: symbolic task/status/claim/event records with prose titles, descriptions, comments, handoffs, and lesson bodies. Lineage: authored by CLI/RPC commands and trace-extracted from heartbeats, claims, handoffs, worker runs, completions, and proof baselines. Behavioral authority: routing and enforcement for work ownership, concurrency, and lifecycle transitions; knowledge for audit/history.

**Knowledge, federation, aptitude, and LCM stores.** Storage substrate: SQLite DBs plus JSONL ledgers and derived files. Representational form: prose knowledge/summary/preference content with symbolic provenance, merge keys, TTL, confidence, edge, regex, prompt, content-hash, and event metadata. Lineage: authored entries, trace-extracted worker lessons and LCM originals, deterministic summaries, explicit promotions, and imported default preference patterns ([src/plugins/lcm.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/lcm.rs), [src/plugins/aptitude.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/aptitude.rs)). Behavioral authority: knowledge for search/recovery; ranking for graph/search/recency; instruction when aptitude prompts or procedural entries are consumed; learning where observations, retrieval feedback, lessons, and summaries shape later context.

**Plans, workunits, proofs, validation, and state commits.** Storage substrate: `.decapod/governance/` JSON files, generated proof/verification artifacts, diagnostics, file/hash baselines, and git-derived state-commit records. Representational form: symbolic manifests, proof plans, proof results, hashes, CBOR-like scope records, and validation reports. Lineage: authored by governance commands and derived from current git/file state, configured gates, and validation runs ([src/core/state_commit.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/state_commit.rs)). Behavioral authority: enforcement and validation, because these artifacts block or justify completion claims.

**Internalization artifacts and session mounts.** Storage substrate: `.decapod/generated/artifacts/internalizations/{id}/manifest.json`, adapter files, and `.decapod/generated/sessions/{session}/internalize_mounts/*.json`. Representational form: symbolic manifest, hashes, replay recipe, capability contract, risk tier, lease, and adapter bytes. Lineage: derived from source hash, model id, profile, profile binary hash, runtime fingerprint, TTL, scopes, and attach/detach events. Behavioral authority: capability-scoped system-definition artifact when mounted, and knowledge artifact when inspected for provenance/integrity.

Promotion path: Decapod's strongest promotion path is event or authored knowledge -> search/graph/lesson surface -> explicit promotion/proof/workunit/capsule binding. A low-authority observation can remain advisory, while procedural knowledge requires a promotion event with evidence refs and approver before the store accepts it as procedural.

## Comparison with Our System

| Dimension | Decapod | Commonplace |
|---|---|---|
| Primary purpose | Runtime governance kernel for AI coding agents | Git-native methodology KB for agent-operated knowledge bases |
| Main substrate | `.decapod/` files, SQLite DBs, JSONL ledgers, generated specs, CLI/RPC | Typed Markdown notes/reviews/instructions, source snapshots, validation, generated indexes |
| Retained unit | Tasks, specs, capsules, workunits, knowledge rows, graph nodes, preferences, proof events | Typed Markdown artifacts with frontmatter, citations, links, status, validation |
| Write path | CLI/RPC commands, worker loop, event ledgers, promotion/proof operations | Direct file edits, snapshots, review gates, validation, index refresh |
| Read path | Explicit CLI/RPC pulls, generated files, context capsules, knowledge/graph searches | `rg`, indexes, links, skills, review reports, validators |
| Governance | Sessions, todo claims, workspace isolation, capsule policies, proof gates, validation | Collection contracts, type specs, citations, semantic review, validation |

Decapod and Commonplace share a preference for repo-native, inspectable artifacts over opaque hosted memory. Both mix prose with symbolic contracts. Decapod is more operational: a todo claim, workunit status, capsule hash, proof gate, or validation result can change what the agent is allowed to do next. Commonplace is more epistemic: its durable artifacts are source-grounded claims, reviews, and instructions whose wording and links must remain reviewable.

The main useful contrast is authority. Decapod is willing to make a retained artifact enforce a workflow: verified status, proof gates, capability contracts, workspace rules, promotion ledgers, and validation diagnostics all have consequences. Commonplace mostly treats notes as advisory unless a validator, instruction, or gate consumes them. That makes Decapod a good source of governance patterns, but its DB-first runtime rows are not a substitute for Commonplace's prose-first library.

### Borrowable Ideas

**Policy-bound context capsules.** Ready now as a design pattern. Commonplace could produce small, hashable context packs for writing or review tasks that list sources, snippets, policy, and target note before a worker starts.

**Promotion firewall for stronger authority.** Ready now. Decapod's procedural knowledge path requires evidence refs, approver, actor, and reason before accepting a stronger class of entry. Commonplace should use the same shape when observations become instructions or validators.

**Workunit manifests for review runs.** Ready when review automation needs stricter lifecycle control. A Commonplace review run could bind source checkout, target note, semantic gates, validation result, and generated reports before marking a review current.

**Context internalization manifests.** Needs a concrete use case. The current noop adapter is not enough to borrow mechanically, but the manifest fields are a useful checklist for any future compiled-context artifact: source hash, replay recipe, capability contract, expiry, binary hash, and mount lease.

**Do not borrow hidden DB primacy for methodology claims.** Decapod's SQLite/JSONL state is appropriate for runtime coordination. Commonplace claims, reviews, and design decisions should remain in typed Markdown unless the artifact is an access structure or machine-checkable ledger.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come through CLI/RPC commands, operator edits, init seeds, promotion approvals, and agent-authored records; automatic writes create scaffolds, databases, events, generated specs, context capsules, workunit bindings, worker lessons, proof/validation artifacts, LCM summaries, derived graph exports, internalization manifests, session mounts, and diagnostics.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — LCM summaries consolidate originals; knowledge `merge_key` can merge duplicate active entries; worker runs synthesize lesson entries from task context; supersede/deprecate/dispute, proof baselines, and validation drift invalidate or block stale state; TTL decay marks expired knowledge stale; promotion ledgers and recency/ranking paths change salience or authority.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Decapod records todo/claim/worker events, LCM originals for messages/artifacts/tool results, retrieval feedback, proof and validation events, federation events, aptitude observations, state/provenance artifacts, and session-scoped mounts.

**Learning scope:** `per-task` `per-project` `cross-task` — Worker lessons are per-task, most stores are repo/project scoped, and aptitude/default skill or preference surfaces can carry across tasks; user-store support exists separately from repo-store support.

**Learning timing:** `online` `staged` — Event capture and worker lesson creation happen during operation; LCM summary, procedural promotion, validation/proof baselines, internalization creation, and graph export are staged or explicit commands.

**Distilled form:** `prose` `symbolic` — Distilled outputs are prose lessons, summaries, prompts, specs, and knowledge bodies plus symbolic metadata, hashes, graph nodes, workunit/proof records, promotion events, and manifests. I did not find distributed-parametric learned state.

**Extraction.** The extraction paths are heterogeneous. `worker-run` searches knowledge for task-title words, writes context comments, marks work done, and can persist a lesson into knowledge plus federation ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/core/todo.rs)). LCM stores immutable originals and builds deterministic summaries from ordered originals with content hashes ([src/plugins/lcm.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/lcm.rs)). Knowledge retrieval feedback and promotion events are append-only ledgers; procedural promotion requires evidence refs and approval before becoming a procedural entry ([src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/deea0f186770737758f94d146ef637811a6ee958/src/plugins/knowledge.rs)).

**Scope and timing.** Raw traces remain as ledger/database evidence. Derived lessons, summaries, graph nodes, proof baselines, and promotion events can shape later work, usually after an explicit command or worker-loop boundary rather than during the action that produced the trace.

**Survey fit.** Decapod fits the trace-to-governance-artifact family. It strengthens the claim that trace-learning need not be vector memory: the useful outputs are lessons, summaries, graph nodes, proof baselines, promotion records, and validation diagnostics. It also highlights an authority boundary Commonplace should preserve: automatic lessons may advise, but stronger procedural authority should require explicit evidence and approval.

## Read-back

**Read-back:** `pull` — Retained Decapod memory re-enters action mainly when an agent or host explicitly calls CLI/RPC commands such as context capsule query, knowledge search, federation search, LCM restore/list, aptitude prompt, todo get/list, workunit show, proof show, or validation. Generated entrypoints and project specs are important baseline/system-definition surfaces, but I did not find a source-visible host hook that automatically pushes retained memory into a receiving agent before action.

The main read path is rule/lexical and bounded by caller choices: op/path/tag/query bindings, scope, limit, risk-tier policy, explicit task/workunit ids, SQL `LIKE` search, graph traversal depth, recency ranking, list filters, and archive restore budgets. From the agent perspective, even a rich capsule remains pull unless the host automatically invokes Decapod and injects the result. Static `AGENTS.md`/`CLAUDE.md`/`CODEX.md` files route agents toward the store, but they are baseline instructions rather than read-back of accumulated memory.

Authority at consumption depends on which surface is read. A knowledge row, LCM original, graph node, or capsule snippet is advisory context unless a consuming workflow promotes it into procedure, binds it to a workunit, mounts it as a capability-scoped artifact, or validates it through a proof gate. Faithfulness is not applicable as a push-specific test for this pull-only verdict; the code tests many contracts and gates, but not behavioral uptake from unsolicited memory injection.

## Curiosity Pass

**The README's "before inference" framing can overstate deployment.** The code implements strong CLI/RPC affordances for pre-inference context shaping, but the push into a model depends on the host or agent choosing to call Decapod.

**The promotion firewall is stronger than the lesson generator.** Worker lessons are useful but agent-inferred; procedural entries require an explicit approval event with evidence refs. That separation is a better pattern than automatic instruction mutation.

**Context capsules are more auditable than ordinary RAG and less semantically ambitious.** They preserve sources, snippets, policy, and hashes, but their selection is deterministic rule/lexical scoring rather than embedding or judgment-based relevance.

**Internalization is currently more of an artifact contract than a demonstrated compression layer.** The manifest/lease/integrity model is valuable, while the builtin noop profile means the repository does not yet prove a real adapter improves context efficiency.

**Decapod's many memory stores need authority labels to stay understandable.** Todo, knowledge, federation, aptitude, LCM, capsules, workunits, proofs, and internalizations are not one memory mechanism; they differ by substrate, lineage, and behavioral force.

## What to Watch

- Whether first-party host integrations automatically invoke context, knowledge, or aptitude reads before model calls; that would change the read-back verdict from pull to push or both.
- Whether worker-generated lessons gain citations, review state, or semantic validation before they affect later tasks; that would make trace-learning safer.
- Whether non-noop internalization profiles land in the main repository and are tested against behavior or context-efficiency outcomes.
- Whether context capsule selection gains stronger relevance signals while keeping source, policy, and hash inspectability.
- Whether federation exports become a normal operator review surface for inferred lessons, decisions, and commitments rather than a secondary derived view.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Decapod stores substantial memory, but most retained memory enters agent context by explicit CLI/RPC pull.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Decapod's files, DB rows, JSONL events, capsules, manifests, proofs, and adapters differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: workunits, proof gates, validation rules, capability contracts, generated entrypoints, and procedural promotions can bind or enforce future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: knowledge rows, capsule snippets, LCM originals, summaries, graph nodes, and lessons mostly advise until promoted or consumed by a gate.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - relates: Decapod turns operational traces into lessons, summaries, graph nodes, proof baselines, and promotion records while preserving raw evidence.
