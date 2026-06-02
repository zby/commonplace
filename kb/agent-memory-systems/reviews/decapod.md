---
description: "Decapod review: Rust local-first governance kernel with repo-native specs, capsules, SQLite stores, trace lessons, proof gates, and pull-first activation"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-01"
---

# Decapod

Decapod, from DecapodLabs, is a Rust CLI governance kernel for AI coding agents. It installs repo-native `.decapod/` state, agent entrypoint contracts, generated project specs, embedded constitution/docs access, task/session/workspace controls, context capsules, knowledge and federation stores, proof gates, and trace/verification ledgers. The reviewed implementation is daemonless and local-first: agents call the CLI or JSON-RPC operations at governance boundaries rather than relying on a resident memory service.

**Repository:** https://github.com/DecapodLabs/decapod

**Reviewed commit:** [f09db9b9cb0b44d3fb450e88b67bd4d79f3142be](https://github.com/DecapodLabs/decapod/commit/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be)

**Last checked:** 2026-06-01

## Core Ideas

**The memory surface is a control plane, not a chat-history store.** The top-level CLI groups state into init, session, todo, governance, data, automation, QA, inference, trace, and context commands ([src/cli.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/cli.rs)). The README frames `.decapod/` as the repo-native substrate for generated specs, context, proof artifacts, durable data, config, and overrides ([README.md](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/README.md)).

**Agent behavior is anchored by generated entrypoints and local project specs.** `decapod init` scaffolds agent entrypoint files, `.decapod/config.toml`, generated specs, CI, and context capsule policy defaults ([src/core/scaffold.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/scaffold.rs)). The repository's own `AGENTS.md` tells agents to read the agent API corpus, acquire a session, claim a todo, resolve context, use isolated workspaces, and validate before completion ([AGENTS.md](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/AGENTS.md), [docs/agent/api-index.md](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/docs/agent/api-index.md)).

**Context is selected through deterministic capsules and orientation packets.** `context_capsule` resolves scoped fragments from embedded/merged docs, records sources/snippets, binds policy metadata, and hashes the canonical capsule; optional `--write` persists it under `.decapod/generated/context/` ([src/core/context_capsule.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/context_capsule.rs)). `docs::resolve_scoped_fragments` combines operation/path/tag bindings with lexical matching and deterministic ordering ([src/core/docs.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/docs.rs)). `infer orientation` builds a bounded packet with allowed/forbidden scope, proof requirements, known unknowns, and decision gates from task intent and todo state ([src/lib.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/lib.rs)).

**Governance artifacts carry enforcement authority.** Plans keep intent, todo IDs, proof hooks, unknowns, human questions, stop conditions, forbidden paths, and file-touch budget; execution readiness blocks on approval, unresolved unknowns, missing todos, and scope violations ([src/core/plan_governance.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/plan_governance.rs)). Workunit manifests bind intent refs, spec refs, state refs, proof plan, proof results, and a VERIFIED state that requires every planned proof gate to pass ([src/core/workunit.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/workunit.rs)).

**Knowledge is split across simple stores with explicit provenance.** The project has SQLite-backed todo, knowledge, aptitude, federation, feedback, health, and governance data plus append-only JSONL event ledgers. The knowledge plugin enforces provenance schemes, statuses, TTL policy, conflict policy, temporal filters, retrieval feedback events, decay events, and a promotion firewall for procedural entries ([src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/knowledge.rs)). Federation adds a typed provenance graph with node types, statuses, priorities, confidence values, edge types, event replay, and derived Markdown/graph exports ([src/plugins/federation.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/federation.rs)).

**Context efficiency is explicit but heuristic.** Decapod avoids dumping all memory into the agent: capsules have scopes, limits, risk-tier policy caps, source snippets, and hashes; `context.resolve` uses op/path/tag/query signals and a limit; `infer init` excludes high-volume or low-value paths and reports a token budget ([src/core/capsule_policy.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/capsule_policy.rs), [src/lib.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/lib.rs)). The selection is deterministic and inspectable, but it is mostly lexical/rule-based rather than embedding or LLM-ranked.

## Artifact analysis

- **Storage substrate:** `files` — Repository files such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `.decapod/config.toml`, and `.decapod/generated/specs/*`
- **Representational form:** `mixed` — Prose plus symbolic TOML/manifest metadata

**Entrypoint contracts and generated project specs.** Storage substrate: repository files such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `.decapod/config.toml`, and `.decapod/generated/specs/*`. Representational form: prose plus symbolic TOML/manifest metadata. Lineage: generated or preserved by init/scaffold from inferred repo context, user-provided seeds, embedded templates, and local overrides. Behavioral authority: system-definition artifacts with instruction and routing force for agents, plus knowledge-artifact context when agents read specs as project facts.

**Embedded constitution/docs fragments and deterministic context capsules.** Storage substrate: embedded assets merged with repo-local docs and optional `.decapod/generated/context/*.json` capsule files. Representational form: prose snippets with symbolic source refs, policy binding, task/workunit ids, and a SHA-256 capsule hash. Lineage: assembled from embedded constitution/docs and local project specs at query time; regenerated when source docs, policy, repo revision, topic, scope, or limit changes. Behavioral authority: knowledge artifact when returned as context; routing and scoping system-definition artifact when capsule policy controls scopes, limits, and write permission.

**Todo, session, ownership, and event ledgers.** Storage substrate: SQLite task database plus `todo.events.jsonl`, claim-status cache rows, agent presence, category ownership, and rebuild logic ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/todo.rs)). Representational form: symbolic task/state records and JSON events. Lineage: authored by CLI/RPC operations, heartbeats, claims, handoffs, status transitions, and comments; the database can be rebuilt from the JSONL event log. Behavioral authority: system-definition artifact for work routing, ownership, concurrency, and lifecycle transitions; knowledge artifact for audit/history.

**Knowledge entries, federation nodes, aptitude preferences, and feedback proposals.** Storage substrate: SQLite databases under `.decapod/data/`, JSONL promotion/retrieval/decay ledgers, and federation derived files. Representational form: mixed prose bodies, symbolic status/provenance/TTL/confidence/edge fields, and regex patterns for aptitude. Lineage: directly authored, imported from events, merged/superseded, inferred from worker-loop lessons, or proposed from operator feedback. Behavioral authority: mostly knowledge artifact for search, hints, provenance, and audit; system-definition authority appears in procedural knowledge promotion, aptitude prompts, regex matchers, and federation graph lifecycle.

**Governed plans, workunits, proofs, and verification artifacts.** Storage substrate: `.decapod/governance/plan.json`, `.decapod/governance/workunits/*.json`, proof event ledgers, verification event ledgers, and file/hash baselines. Representational form: symbolic JSON manifests and normalized proof-output hashes. Lineage: authored by plan/workunit/proof commands, generated from configured proof definitions, and verified against current workspace state. Behavioral authority: enforcement and validation system-definition artifacts: they block execution, block VERIFIED transitions, prove completion, and detect drift ([src/core/proof.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/proof.rs), [src/plugins/verify.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/verify.rs)).

**LCM originals and summaries.** Storage substrate: append-only `lcm.events.jsonl` and derived `lcm.db`. Representational form: raw prose/tool-result content with symbolic metadata, plus deterministic prose summaries and hash pointers. Lineage: originals are trace-like messages/events/artifacts/tool results; summaries are derived by ordered concatenation, truncation, and hashing, and the index is rebuildable from the ledger ([src/plugins/lcm.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/lcm.rs)). Behavioral authority: raw originals are knowledge artifacts for recovery and audit; summaries are lower-volume knowledge artifacts that can shape later context selection when explicitly shown.

**Internalized context artifacts and mounts.** Storage substrate: `.decapod/generated/artifacts/internalizations/{id}/manifest.json`, adapter files, and session mount leases under `.decapod/generated/sessions/`. Representational form: mixed symbolic manifest, replay recipe, hashes, capability contract, and external adapter bytes. Lineage: derived from a local source file, base model id, profile, binary hash, runtime fingerprint, TTL, scopes, and adapter hash. Behavioral authority: capability-scoped system-definition artifact when attached to a session/tool; knowledge artifact when inspected for provenance and integrity ([src/plugins/internalize.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/internalize.rs)).

The main promotion path is event/task/session material -> knowledge/federation/LCM artifacts -> explicit promotion, proof, or context use. Decapod is unusually clear about separating raw evidence, derived views, and enforcement artifacts, but its quality checks are mostly deterministic structure/proof checks rather than semantic truth review.

## Comparison with Our System

| Dimension | Decapod | Commonplace |
|---|---|---|
| Primary purpose | Runtime governance kernel for AI coding agents | Git-tracked methodology KB for agents and maintainers |
| Main substrate | `.decapod/` files, SQLite DBs, JSONL ledgers, generated specs, CLI/RPC | Markdown notes/reviews/instructions, source snapshots, schemas, scripts, generated indexes |
| Retained unit | Tasks, plans, workunits, capsules, knowledge rows, graph nodes, proof events | Typed Markdown artifacts with frontmatter, citations, links, status, validation |
| Activation | Entrypoint instructions plus CLI/RPC pull commands | Mostly deliberate pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Sessions, todo claims, workspace isolation, proof gates, policy caps, validation | Collection contracts, type specs, validation, review gates, git lifecycle |
| Trace learning | Worker lessons, LCM summaries, retrieval/feedback/promotion ledgers | Review/workshop artifacts promoted into durable notes through explicit writing and gates |

Decapod and Commonplace share a strong preference for repo-native, inspectable artifacts over opaque hosted memory. Both use human-readable prose alongside symbolic contracts. Decapod is more operational: it wants to govern the agent's next command, workspace, proof, and completion claim. Commonplace is more epistemic: it wants durable claims to be source-pinned, typed, linked, reviewed, and retrievable over time.

Decapod's most useful contrast is that it treats agent memory as part of governance. A todo claim, capsule hash, proof result, or workunit status can change what an agent is allowed to do, not just what it remembers. Commonplace has validators and review gates, but most notes remain advisory unless a script or instruction consumes them with stronger authority.

Decapod's weaker point for Commonplace purposes is that many retained facts live in SQLite rows or generated JSON rather than reviewable prose artifacts. Its provenance and event logs are good, but a lesson or federation node is not the same as a source-pinned review note unless a promotion path makes it inspectable, curated, and semantically checked.

**Read-back:** `both` — But mostly pull. Decapod has unconditional entrypoint/config push when an agent workbench loads `AGENTS.md`; its distinctive context, memory, proof, and governance content reaches the agent through explicit CLI/RPC calls, so it does not qualify for `push-activation` under the stricter relevance-gated rule

### Borrowable Ideas

**Context capsules with policy-bound hashes.** Ready now as a design pattern. Commonplace could produce small, source-listed, hashable context packs for review or writing tasks, with the policy and source set visible inside the artifact.

**Workunit manifests tying intent, specs, state, and proof.** Ready when Commonplace needs stronger workflow enforcement. A local review run could have a manifest that records source snapshot, target note, review gates, and proof artifacts before marking a review current.

**Promotion firewall for procedural knowledge.** Ready now. Decapod's procedural knowledge path requires a promotion event with evidence refs, approver, and reason before accepting a stronger class of entry. Commonplace should use the same shape when turning observations into instructions.

**Flight recorder over event ledgers.** Useful with more automation. Decapod's trace renderer collects broker, todo, federation, proof, watcher, map, and LCM events into a governance timeline ([src/core/flight_recorder.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/flight_recorder.rs)). Commonplace review runs could benefit from the same cross-ledger audit view.

**Do not borrow hidden DB-first memory as the primary durable layer.** SQLite/JSONL is good for runtime state and ledgers, but Commonplace's durable methodology claims should remain in typed Markdown unless they are generated indexes or machine-checkable evidence.

## Trace-derived learning placement

**Trace source.** Decapod qualifies as trace-derived learning. The trace sources are task/todo event streams, worker-loop execution records, LCM originals with `event`, `message`, `artifact`, and `tool_result` kinds, retrieval feedback events, proof/verification ledgers, and operator feedback records. These are not model transcripts by default, but they are durable event and action traces from agent operation.

**Extraction.** There are several extraction paths. The worker loop summarizes task context by searching knowledge for title words, comments the task with that context, marks it done, captures a baseline, and records a lesson into knowledge plus federation when lesson persistence is enabled ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/core/todo.rs)). LCM stores immutable originals and builds deterministic summaries from ordered originals with content-hash lineage ([src/plugins/lcm.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/lcm.rs)). Feedback can generate a non-binding preference proposal, while procedural knowledge requires an explicit promotion event with evidence and approval before it is accepted as procedural ([src/plugins/feedback.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/feedback.rs), [src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/f09db9b9cb0b44d3fb450e88b67bd4d79f3142be/src/plugins/knowledge.rs)).

**Substrate, form, lineage, and authority.** Raw trace material persists as JSONL event ledgers and SQLite rows; distilled outputs persist as knowledge rows, federation nodes, LCM summaries, promotion ledgers, and proof/verification baselines. The representational form is mostly prose plus symbolic metadata and hashes, with no distributed-parametric state in the reviewed implementation. Lineage is explicit for event IDs, content hashes, provenance strings, promotion evidence refs, and rebuildable ledgers. Behavioral authority rises from knowledge artifact evidence/audit in raw traces to ranking/search hints in knowledge, graph neighborhood context in federation, and system-definition authority when a procedural promotion, proof gate, workunit transition, or validation baseline controls later action.

**Scope and timing.** The trace-derived paths are repo/store scoped, with session scoping for LCM and internalization mounts. Timing is staged: raw event capture happens during operation, worker lessons are produced after task completion, summaries are produced on explicit summarize calls, and procedural promotion requires a separate approval event. These artifacts affect later work, not the action that produced the trace.

**Survey placement.** Decapod belongs in the trace-to-governance-artifact and trace-to-retrieval-substrate families. It strengthens the survey claim that useful trace learning does not have to be vector memory: event streams become lessons, summaries, promotion records, graph nodes, and proof baselines. It also strengthens the raw-versus-distilled split because raw ledgers remain rebuildable evidence while derived lessons and procedural entries carry stronger future behavioral authority.

**Curation policy.** The oracle is mostly deterministic plus explicit human approval where authority increases. Worker lessons are automatic and agent-inferred; LCM summaries are deterministic compression; feedback proposals are non-binding; procedural knowledge needs a promotion ledger event with evidence refs and approver. That is a better authority boundary than automatic instruction mutation, though semantic correctness of a lesson is still not established by the code alone.

## Curiosity Pass

The README describes Decapod as "pre-inference faculty," but the source-visible mechanism is still an agent-callable CLI/RPC surface. Unless the host workbench automatically calls it, Decapod cannot push context into an agent beyond the static entrypoint contract.

The implementation has several memory subsystems with different names and authority: knowledge, federation, aptitude, LCM, internalize, todo, proof, and context capsules. Calling all of them "memory" would hide the important split between evidence, routing, instruction, enforcement, ranking, and audit.

The context capsule design is more reviewable than ordinary RAG because it records sources, snippets, policy binding, repo revision, and a hash. It is also less semantically powerful than RAG because ranking is deterministic lexical/rule scoring, not learned relevance.

The internalization plugin is ambitious but conservative at this commit: non-local sources and stdin are rejected, the builtin profile is a noop adapter, and the value is mostly in the manifest/replay/integrity contract rather than model-side compression.

The strongest governance idea is the promotion firewall. Decapod lets low-authority observations and feedback exist without immediately becoming instructions, then requires evidence and approval for procedural knowledge.

## What to Watch

- Whether host integrations start invoking Decapod automatically before actions. That would change read-back from mostly pull to engineered push and could justify `push-activation`.
- Whether worker-loop lessons gain source excerpts, review states, and semantic validation before they influence later task context. That would make `trace-derived` learning safer and more comparable to Commonplace note promotion.
- Whether internalization profiles move beyond `builtin:noop` in the main repository. Real adapters would make the substrate a stronger example of compiled context artifacts.
- Whether context capsule ranking gains stronger relevance signals while preserving source/policy/hash inspectability. That is the main design tension for borrowing capsules into Commonplace.
- Whether federation-derived Markdown becomes the operator-facing review surface for inferred lessons, decisions, and commitments. That would narrow the gap between Decapod's DB-first state and Commonplace's prose-first library.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Decapod turns task/event/message/tool-result traces into lessons, summaries, graph nodes, promotion records, and proof baselines.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Decapod stores many artifacts, but most read-back depends on explicit CLI/RPC calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Decapod's files, DB rows, JSONL ledgers, capsules, manifests, and proof events differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: plans, workunits, proof gates, capsule policies, entrypoint contracts, and procedural promotions carry enforcement or instruction force.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: source snippets, lessons, LCM originals, summaries, and federation nodes mostly provide evidence/context unless promoted or enforced.
