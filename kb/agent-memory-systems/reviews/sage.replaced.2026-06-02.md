---
description: "SAGE review: governed agent memory infrastructure with CometBFT writes, validator votes, RBAC, encryption, and MCP/REST recall surfaces"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# SAGE

SAGE, by l33tdawg, is a Go-based governed memory service for agents. It stores facts, observations, inferences, tasks, votes, corroborations, challenges, access grants, organizations, and pipeline messages behind REST, MCP, browser-extension, dashboard, and SDK surfaces. Its distinctive claim is not just persistent recall, but consensus-validated institutional memory: memory writes are signed, broadcast through CometBFT, mirrored into query storage only after commit, and filtered through RBAC, classification, confidence, decay, and optional at-rest encryption.

**Repository:** https://github.com/l33tdawg/sage

**Reviewed commit:** [765dc91b71e9a3703f86e32aa168e35cd3a7e89b](https://github.com/l33tdawg/sage/commit/765dc91b71e9a3703f86e32aa168e35cd3a7e89b)

**Last checked:** 2026-05-16

## Core Ideas

**The write path separates raw submission, consensus state, and query records.** A REST memory submission validates content/type/domain/confidence, computes content and embedding hashes, embeds the caller's Ed25519 proof, signs a protobuf transaction with the node key, stages non-consensus supplementary data, and uses `broadcast_tx_commit` so the client returns only after CometBFT finalization ([api/rest/memory_handler.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/api/rest/memory_handler.go), [internal/tx/types.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/tx/types.go)). Inside ABCI, the committed transaction writes memory hashes, statuses, classifications, votes, governance state, and access metadata into BadgerDB, while full memory records, embeddings, triples, votes, challenges, corroborations, and task fields are buffered for SQLite/Postgres flush ([internal/abci/app.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/abci/app.go)). The raw memory submission is therefore not the same artifact as the committed record or the validator metadata around it.

**CometBFT gives SAGE ordering and replay, but personal mode is closer to a deterministic validation pipeline than a distributed trust network.** The architecture docs describe four ABCI nodes plus four CometBFT validators over PostgreSQL and Ollama for full deployments, while the README says personal mode still runs a real CometBFT node with four in-process application validators ([README.md](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/README.md), [docs/ARCHITECTURE.md](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/docs/ARCHITECTURE.md)). The implementation's strongest consensus property is the commit boundary: offchain writes flush before BadgerDB height is saved, and the node panics rather than silently advancing if the query layer cannot persist committed writes ([internal/abci/app.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/abci/app.go)). In single-node use, the Byzantine framing is mostly ceremony around durable ordering, replay, and deterministic state transitions.

**Application validators are concrete, but their "BFT" work is heuristic content gating.** The four app validators are sentinel, dedup, quality, and consistency. Sentinel accepts, dedup rejects committed duplicate hashes, quality rejects noise/too-short/empty reflection content, and consistency checks confidence thresholds and required domains; three accepts out of four passes pre-validation ([internal/appvalidator/validator.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/appvalidator/validator.go), [internal/appvalidator/manager.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/appvalidator/manager.go)). Separately, on-chain memory votes are accepted only from the validator set, recorded in BadgerDB and the SQL vote table, and cause a memory to become committed when quorum is reached or deprecated when all validators vote without quorum ([internal/abci/app.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/abci/app.go)). This is useful governance metadata, but it is not semantic fact checking.

**Provenance is cryptographic identity plus audit rows, not source-grounded citation.** API requests and embedded transaction proofs use Ed25519 signatures over canonical request hashes, timestamps, and optional nonces; ABCI re-verifies the agent proof instead of trusting REST middleware ([internal/auth/ed25519.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/auth/ed25519.go), [internal/abci/app.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/abci/app.go)). A committed memory carries submitter, content hash, parent hash, memory type, domain, classification, status, timestamps, votes, challenges, corroborations, linked memories, and optional triples ([internal/memory/model.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/memory/model.go), [internal/store/store.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/store/store.go)). That proves who submitted and which validators/voters touched the record. It does not, by itself, preserve external evidence, source spans, extraction prompts, or a regeneration rule for a claim.

**Confidence, corroboration, challenges, and task status form a lightweight lifecycle.** Memories have statuses `proposed`, `validated`, `committed`, `challenged`, and `deprecated`, plus task-specific statuses `planned`, `in_progress`, `done`, and `dropped` ([internal/memory/model.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/memory/model.go), [internal/memory/lifecycle.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/memory/lifecycle.go)). Recall recomputes confidence with exponential decay and a logarithmic corroboration boost; open tasks do not decay ([internal/memory/confidence.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/memory/confidence.go), [api/rest/memory_handler.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/api/rest/memory_handler.go)). A challenge that is included in a block immediately deprecates the memory, and corroborations add evidence rows consumed by confidence calculation ([internal/abci/app.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/abci/app.go)). The lifecycle is operationally meaningful but coarse: disputes do not produce adjudicated replacements or merged claim histories.

**RBAC and classification are real system-definition state.** SAGE models clearance levels from public to top secret, domain access, visible-agent filters, org membership, departments, federation agreements, and grants ([internal/tx/types.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/tx/types.go), [internal/store/store.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/store/store.go)). REST read paths enforce domain access, submitting-agent visibility, multi-org access, and per-record classification before returning memories ([api/rest/memory_handler.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/api/rest/memory_handler.go)). Governance proposals can add, remove, and adjust validators through deterministic proposal state and integer quorum math ([internal/governance/engine.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/governance/engine.go), [internal/governance/quorum.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/governance/quorum.go)). These artifacts shape behavior through enforcement, not advice.

**Storage modes trade inspectability for governed service behavior.** Personal mode uses SQLite plus BadgerDB; multi-node mode uses PostgreSQL/pgvector plus BadgerDB; retrieval can use FTS5, vector similarity, or hybrid BM25/vector reciprocal-rank fusion ([docs/ARCHITECTURE.md](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/docs/ARCHITECTURE.md), [internal/store/store.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/store/store.go), [internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/mcp/tools.go)). SQLite can attach an AES-256-GCM vault derived from an Argon2id-protected data key; encrypted content disables FTS and forces semantic/vector paths ([internal/vault/vault.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/vault/vault.go), [internal/store/sqlite.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/store/sqlite.go)). This is strong local privacy packaging, but memories are opaque database rows rather than reviewable files.

**The agent-facing surfaces are broader than memory CRUD.** MCP tools cover remember, recall, list, timeline, status, inception, turn, reflect, tasks/backlog, agent registration, pipeline send/inbox/result, and governance proposal/vote/status ([internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/internal/mcp/tools.go)). REST exposes the same system to dashboards, SDKs, a browser extension, OAuth/PKCE MCP transport, and signed local hooks. Pipeline messages are task dispatch objects with claim/result lifecycle and optional auto-journal summaries, not full memory records until journaled ([api/rest/pipe_handler.go](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/api/rest/pipe_handler.go)). Claude Code hooks can direct-write session bookends and nudge the model to call `sage_turn` or `sage_reflect`, but the maintainers explicitly leave conversation-level distillation to the LLM because only it has enough context to decide what matters ([docs/HOOKS.md](https://github.com/l33tdawg/sage/blob/765dc91b71e9a3703f86e32aa168e35cd3a7e89b/docs/HOOKS.md)).

## Comparison with Our System

| Dimension | SAGE | Commonplace |
|---|---|---|
| Primary purpose | Governed service for multi-agent memory, recall, tasks, access, and validator governance | Agent-operated methodology KB with durable notes, sources, instructions, ADRs, reviews, and validation |
| Storage substrate | BadgerDB for consensus state; SQLite or PostgreSQL/pgvector for readable/query records; optional AES-256-GCM vault | Git-tracked Markdown, schemas, source snapshots, generated indexes, scripts, and validation outputs |
| Representational form | Prose memory content, symbolic metadata/governance/RBAC/task records, embeddings, hashes, validator votes, pipeline messages | Mostly prose and structured frontmatter, with symbolic links, schemas, commands, and validation code |
| Lineage | Cryptographic submitter identity, content hash, parent hash, votes, challenges, corroborations, block height, timestamps | Source-pinned notes, authored citations, replacement archives, status fields, validation, and review gates |
| Activation | MCP/REST recall, turn-cycle recall+write, boot instructions, hooks, hybrid search, dashboard surfaces | `rg`, indexes, descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Enforced access/consensus/governance plus prompt/tool instructions returned to agents | Advice, instruction, routing, validation, review, and governance authority in inspectable artifacts |

SAGE is much stronger than commonplace on service-side enforcement. Domain clearance, visible-agent filtering, challenge deprecation, validator-set governance, request signatures, vault lock state, and CometBFT commit ordering do not depend on a cooperative agent reading an instruction. They are system-definition artifacts consumed with enforcement, validation, routing, or configuration force.

Commonplace is stronger on epistemic inspectability. A commonplace review or note is a knowledge artifact with source citations, a type contract, status, links, and validation. SAGE can tell a future agent that a memory was submitted by an Ed25519 identity, committed by quorum, and corroborated by other agents. It usually cannot tell that agent which source passage made the claim true or how to regenerate the claim from source material.

The key artifact split is:

- Raw memory submissions: proposed prose/symbolic payloads with submitter identity, type, domain, confidence, classification, optional embedding/triples, and optional parent hash.
- Committed records: query-layer memory rows whose status changed only after consensus and quorum processing.
- Validator and consensus metadata: votes, validator scores, governance proposals, block heights, hashes, and app state in BadgerDB.
- Storage substrate: BadgerDB plus SQLite/PostgreSQL/pgvector, optionally encrypted; not a file substrate.
- Runtime/tool surfaces: REST, MCP, OAuth transport, browser extension interception, dashboard, hooks, SDKs, and pipeline tools.
- Behavior-shaping artifacts: RBAC grants, clearance, domain ownership, validator set, memory mode instructions, boot instructions, task records, and injected recall results.

The behavioral-authority boundary moves with the channel. A stored memory is a knowledge artifact when retrieved as context, evidence, or advice. A clearance rule, validator-set proposal, challenge transition, vault lock, or MCP tool schema is a system-definition artifact because it enforces, validates, routes, configures, or instructs behavior. Retrieved memories can temporarily gain stronger authority when `sage_inception`, `sage_turn`, or boot instructions tell the agent how to use them, but SAGE does not distinguish reviewed rules from ordinary recollections as sharply as commonplace does.

**Read-back:** both — agents can pull memories through MCP and REST recall, while hooks, boot instructions, and turn surfaces activate memory into runtime context.

## Borrowable Ideas

**Separate commit authority from query storage.** Worth borrowing as an operational pattern if commonplace ever adds a database-backed workshop layer. SAGE's flush-before-height-save rule is a concrete design for avoiding divergence between source-of-truth state and derived query indexes.

**Expose filter observability.** SAGE's query layer returns filtered metadata and headers when RBAC or classification hides results. Commonplace search tools could similarly report when index scope, status filters, or review gates hid likely matches.

**Model tasks as memory records with different decay.** Ready as vocabulary, not as a direct port. The open-task exemption from confidence decay is a useful reminder that "memory" includes commitments and work state, not only factual recall.

**Use explicit authority labels for runtime settings.** SAGE's clearance levels, domain grants, validator governance, memory modes, and vault lock state are better understood as system-definition artifacts than as metadata. Commonplace should keep this distinction when describing future active layers.

**Do not borrow consensus branding for personal mode.** The commit/replay machinery is useful, but commonplace should describe a single-node governed pipeline as a governed pipeline. Byzantine language should be reserved for real independent-fault settings.

**Do not borrow automatic high-authority memory instructions wholesale.** SAGE's inception/turn prompts are effective activation surfaces, but they can make ordinary memories feel more authoritative than their evidence supports. Commonplace should keep promotion into instructions, skills, tests, or schemas review-gated.

## Takeaways

**SAGE is a governed memory infrastructure system, not just a personal memory database.** The code implements signed requests, on-chain agent identity checks, consensus-first writes, validator votes, RBAC, classifications, task memories, challenge/corroboration records, encrypted storage, and multiple runtime surfaces.

**The consensus claim is partly supported and partly overstated.** Multi-node deployments have a real CometBFT/ABCI architecture. Personal mode still benefits from ordering and replay, but its in-process validators are deterministic heuristics rather than independent witnesses.

**Its strongest mechanism is enforcement, not knowledge transformation.** SAGE can decide who may write, who may read, which records are committed, and which records are deprecated. It does less to transform raw experience into citable, reviewed, maintainable claims.

**Confidence is retrieval metadata, not truth.** Decay, corroboration boosts, challenge deprecation, and validator votes help rank and lifecycle memories. They do not replace source citation, semantic review, contradiction resolution, or claim-level adjudication.

**Trace-derived status is not supported for this review.** SAGE stores agent-written per-turn observations, reflections, task records, pipeline summaries, and session bookends. The inspected code does not show a durable extractor that transforms raw traces or outcomes into stronger reviewed artifacts that later shape behavior independently. The agent writes the memory; SAGE governs and activates it.

## Curiosity Pass

The surprising part is how much of SAGE's value lives outside "memory" proper. Governance proposals, clearance, OAuth/MCP transport, vault state, dashboard workflows, and pipeline claims matter as much as recall quality because they decide what the agent is allowed to know and do.

The simpler architecture would be a signed local SQLite/pgvector memory service with RBAC and validation hooks. SAGE's CometBFT layer earns its keep when multiple independent nodes or operators exist; for personal use, the same user-facing behavior could be achieved with fewer moving parts if Byzantine fault tolerance is not a requirement.

The browser extension and hooks are pragmatic adoption bridges. The extension maps text-like calls from ChatGPT into signed REST requests, and hooks compensate for agents forgetting to call memory tools. These are consumer-surface mechanisms, not storage mechanisms, and they may be the parts most likely to affect real use.

The provenance story is precise about identity but thin about evidence. Signed authorship and block inclusion are useful for accountability, yet a bad claim can still be signed, committed, corroborated, and later recalled. For commonplace's purposes, that makes SAGE a governance reference more than a knowledge-curation reference.

## What to Watch

- Whether SAGE adds source-aware extraction or citation fields that connect memories to transcripts, files, tool traces, or external evidence.
- Whether challenges evolve from immediate deprecation into adjudication, replacement, contradiction records, or claim merge histories.
- Whether validator scores and Proof-of-Experience become operative voting weights rather than mostly recorded metadata.
- Whether personal mode keeps the full CometBFT stack or grows a lighter local governed-storage mode.
- Whether Claude Code and other host hooks move from nudges/session bookends to batched trace-to-artifact extraction.
- Whether encrypted nodes get a retrieval strategy that preserves both privacy and lexical inspectability.

## Bottom Line

SAGE is best read as an enforcement-heavy memory control plane. It gives agents durable memory records, signed identity, consensus commit boundaries, access control, lifecycle metadata, encrypted local storage, and many activation surfaces. For commonplace, the most borrowable lesson is the artifact split: raw memories, committed records, consensus metadata, access policy, task state, storage substrate, retrieval scores, and tool instructions all carry different behavioral authority. The least borrowable part is the tendency to treat consensus-validated personal memories as if they were source-validated knowledge.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - classifies: SAGE's memories, votes, grants, tasks, and tool prompts need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: stored memories and corroboration evidence advise later behavior when recalled.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: SAGE's RBAC, validator governance, vault state, and MCP tool schemas enforce or instruct behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SAGE invests heavily in MCP, hooks, inception, turn, and recall surfaces so storage actually reaches the agent.
