---
description: "Repo-native coding-agent governance kernel with embedded constitution, .decapod state, proof gates, context capsules, typed memory, and governed trace-derived promotion"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Decapod

Decapod is DecapodLabs' daemonless, local-first Rust CLI for governing AI coding-agent work inside a repository. Agents call it on demand to turn user intent into scoped context, generated specs, todo/workunit state, isolated workspaces, proof artifacts, and repo-local memory under `.decapod/`; the reviewed code is an executable control plane, not only a methodology corpus.

**Repository:** https://github.com/DecapodLabs/decapod

**Reviewed commit:** [178a7da05f703dc07607926e4d9556b6f8592cd4](https://github.com/DecapodLabs/decapod/commit/178a7da05f703dc07607926e4d9556b6f8592cd4)

## Core Ideas

**The control plane is a short-lived CLI around repo-native state.** The README defines Decapod as the daemonless governance kernel that agents call before acting, model calls, protected-code changes, durable-instruction changes, and commits, and `Cargo.toml` packages that as the `decapod` binary with SQLite, embedded assets, token counting, JSON/TOML, and hashing dependencies ([README.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/README.md), [Cargo.toml](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/Cargo.toml)). The primary storage substrate is the repository-local `.decapod/` tree plus SQLite databases under `.decapod/data/`, with generated specs, context capsules, internalizations, proof outputs, workunits, and derived memory views as file artifacts.

**The constitution is embedded, but its authority changes by channel.** The `constitution/` directory holds over a hundred Markdown contracts, and the build/assets layer compiles many of them into the binary for `decapod docs show`, `docs ingest`, and scoped search ([build/constitution_index.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/build/constitution_index.rs), [src/core/assets.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/assets.rs), [src/core/docs_cli.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/docs_cli.rs)). As GitHub docs, those files are knowledge artifacts. When `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, docs search, or validation gates make an agent follow them, they become prose system-definition artifacts with instruction, routing, or validation force ([AGENTS.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/AGENTS.md), [CODEX.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/CODEX.md)).

**Generated specs are project-local contracts, not general notes.** Initialization scaffolds `.decapod/config.toml`, agent entrypoints, and a canonical `.decapod/generated/specs/` set for intent, architecture, interfaces, validation, semantics, operations, security, and an index; the spec module records those paths and constitution references explicitly ([src/core/scaffold.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/scaffold.rs), [src/core/project_specs.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/project_specs.rs), [constitution/interfaces/PROJECT_SPECS.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/constitution/interfaces/PROJECT_SPECS.md)). Their representational form is prose plus symbolic manifest hashes. Their behavioral authority depends on use: reference when read for context, system-definition when validation, planning, or agent-entrypoint rules require them before implementation.

**Plans, workunits, proof plans, and obligations give "done" a machine-checkable path.** `plan_governance.rs` stores `.decapod/governance/plan.json` with intent, unknowns, human questions, proof hooks, and scope constraints; `workunit.rs` stores per-task manifests with spec refs, state refs, proof plans, proof results, and a state machine that blocks `VERIFIED` unless every proof-plan gate has a passing result ([src/core/plan_governance.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/plan_governance.rs), [src/core/workunit.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/workunit.rs)). The obligation graph adds dependency-aware units whose status is derived from dependencies, proofs, and state commits rather than asserted by a user ([src/core/obligation.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/obligation.rs)). These are symbolic system-definition artifacts: they validate, enforce, and audit promotion.

**Validation gates are executable policy surfaces.** `validate.rs` is a multi-gate harness over repository and `.decapod` state, including namespace, embedded-doc, project-spec, workunit, context-capsule, internalization, federation, eval, and store-purity style checks ([src/core/validate.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/validate.rs)). `proof.rs` runs configured proof commands, logs proof events, and mirrors proof claims into health state ([src/core/proof.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/proof.rs)). This is stronger than storing "proof" prose: the operative part is executable validation and recorded results.

**Workspace isolation is an authority boundary.** `workspace.rs` inspects branches, worktrees, local modifications, containers, protected branch patterns, and publish preconditions; the shipped agent entrypoints require work under `.decapod/workspaces/*` and say not to mutate `.decapod` files directly ([src/core/workspace.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/workspace.rs), [AGENTS.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/AGENTS.md)). Here the memory system is not just recall; it governs where the next agent is allowed to act.

**Memory is split into knowledge, aptitude, federation, todos, feedback, evals, and internalizations.** The store abstraction distinguishes user and repo stores, while SQLite helpers configure WAL/busy-timeout behavior and locate subsystem databases ([src/core/store.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/store.rs), [src/core/db.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/db.rs)). `knowledge.rs` stores entries with provenance, status, TTL, merge/supersede policy, retrieval feedback, decay events, and a promotion firewall for procedural entries ([src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/knowledge.rs)). `federation.rs` stores typed graph nodes such as decisions, commitments, preferences, lessons, projects, handoffs, and observations, plus sources, edges, events, derived vault notes, indexes, graph exports, and validation gates ([src/plugins/federation.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/federation.rs)).

**Context capsules and internalizations make context loading explicit.** `context_capsule.rs` returns deterministic snippets from embedded or merged constitution docs, records sources, policy bindings, task/workunit ids, and a recomputed capsule hash, then writes capsules under `.decapod/generated/context/` ([src/core/context_capsule.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/context_capsule.rs)). `internalize.rs` creates content-addressed internalization artifacts under `.decapod/generated/artifacts/internalizations/`, binds them to source bytes, model/profile metadata, adapter hashes, replay recipes, capability contracts, risk tiers, and session-scoped attach leases ([src/plugins/internalize.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/internalize.rs), [constitution/interfaces/INTERNALIZATION_SCHEMA.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/constitution/interfaces/INTERNALIZATION_SCHEMA.md)). These are not hidden model memory in the reviewed implementation; they are repo-local artifacts with lineage and attach authority.

## Comparison with Our System

| Dimension | Decapod | Commonplace |
|---|---|---|
| Primary target | Govern coding-agent execution inside arbitrary repos | Build and maintain an agent-operated KB methodology |
| Canonical state | `.decapod/` files plus SQLite DBs and JSONL ledgers | Git-tracked Markdown notes, type specs, instructions, reviews, indexes |
| Constitution/rules | Embedded Markdown docs plus project overrides and generated agent entrypoints | `AGENTS.md`, collection contracts, type specs, skills, validators |
| Memory form | Mixed: prose docs/specs, symbolic manifests/DB rows, JSONL events, executable CLI gates, optional adapters | Mostly prose plus symbolic frontmatter/schemas/scripts/validators |
| Behavioral authority | CLI gates, workspace rules, proof plans, policies, and entrypoints instruct or enforce agent behavior | Type contracts, instructions, skills, validation, and review gates shape later agents |
| Lineage | Hashes, manifests, provenance refs, event logs, proof events, trace bundles, state commits | Source links, git history, review records, generated-index provenance, validation reports |
| Activation | Agents call `decapod` before planning, context resolution, mutation, proof, and publish | Agents search/load notes, invoke skills, run validators, and follow repo instructions |

Decapod is closer to an agent governance kernel than a library-style knowledge base. Commonplace accumulates reusable methodology as authored artifacts that future agents read, validate, and connect. Decapod accumulates operational state around a repo and uses that state to constrain the next action: claim a todo, enter a workspace, resolve a context capsule, satisfy proof gates, publish only with required manifests, and record memory with provenance.

The strongest alignment is authority analysis. Both systems need to separate a document's representational form from its behavioral force. A constitution paragraph, generated spec, knowledge node, proof result, and CLI gate can all sit in the same `.decapod` tree, but they should not be treated as the same kind of memory. Decapod's implementation makes this visible: docs and knowledge entries often advise; entrypoints instruct; plan/workunit/eval/proof artifacts validate; workspace and policy gates enforce; internalization leases configure what may affect a session.

The main divergence is inspectability versus operational density. Commonplace keeps most canonical state as directly reviewed Markdown. Decapod uses SQLite and generated JSON artifacts for concurrent, multi-agent, and gate-heavy workflows. That buys stronger runtime coordination but increases the need for deterministic rebuilds, event logs, derived-view freshness gates, and CLI-mediated mutation.

## Borrowable Ideas

**Treat proof plans as first-class memory.** Ready to borrow where commonplace workflows already have validation gates. A proof plan plus proof results is retained state with direct validation authority, not just a note that "tests passed."

**Use generated context capsules for high-authority context.** Worth prototyping for bounded, repeatable review or validation contexts. Commonplace already has lexical navigation and authored links; Decapod's capsule hash, source list, task binding, and policy lineage show how to make a loaded context pack auditable.

**Keep workspace isolation as a memory-system concern.** Ready as vocabulary. Decapod treats "where the agent may work" as part of remembered governance state. Commonplace can use the same framing for workshop ownership, review runs, and parallel-worker coordination.

**Borrow the promotion firewall, not the whole database stack.** Decapod's procedural knowledge rule requires a promotion event with evidence and approval before an entry can become procedural. Commonplace should borrow that authority split before adding more persistent stores.

**Track internalized context as an artifact with leases.** Not ready for commonplace without a concrete internalizer use case, but the design is sharp: source hash, adapter hash, replay recipe, capabilities contract, risk tier, and session lease prevent "compressed memory" from becoming invisible authority.

**Avoid scattering system-definition authority across too many surfaces.** Decapod intentionally has many subsystems: plans, workunits, todos, obligations, federation, knowledge, eval, policy, proof, context, internalize, workspace. Commonplace should borrow the artifact distinctions, not the subsystem count, unless it has the same operational pressure.

## Trace-derived learning placement

**Trace source.** Decapod qualifies as a trace-derived system in a governed, staged sense. The explicit trace source is the eval subsystem's `trace_file`, parsed into `TRACE_BUNDLE` artifacts containing events, tools, token counts, details, attachments, and hashes ([src/plugins/eval.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/eval.rs)). A second, lighter source is the autonomous worker loop: claimed tasks, context summaries, task events, baseline capture, and completed-task lessons are persisted into knowledge and federation when `lesson` is enabled ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/todo.rs)). Feedback entries also accumulate as an append-only ledger and can generate non-binding preference proposals ([src/plugins/feedback.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/feedback.rs)).

**Extraction.** Eval extraction is mostly symbolic and deterministic: run results point to trace bundles, judge verdicts attach structured outcomes, aggregates compute baseline/candidate success deltas and confidence intervals, gates decide whether promotion is allowed, and failure bucketing groups failure reasons with optional agent-assisted mode ([src/plugins/eval.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/eval.rs)). Worker-loop lesson extraction is simple prose synthesis from a task and context summary into a knowledge entry and federation lesson node ([src/core/todo.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/core/todo.rs)). Knowledge promotion requires an explicit promotion event before procedural entries can be accepted ([src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/knowledge.rs)).

**Storage substrate.** Raw and derived eval artifacts live under `.decapod/data/eval/...` according to the eval schema; worker lessons live in `knowledge.db`, `federation.db`, `federation.events.jsonl`, and derived federation files; retrieval feedback, decay, and promotion ledgers live as JSONL files next to the knowledge database ([src/plugins/eval.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/eval.rs), [src/plugins/knowledge.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/knowledge.rs), [src/plugins/federation.rs](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/src/plugins/federation.rs)).

**Representational form.** The raw trace layer is structured JSON. Eval plans, runs, verdicts, aggregates, gate requirements, trace bundles, and failure buckets are symbolic JSON artifacts. Worker lessons and feedback proposals are prose. Federation graph nodes are mixed: prose bodies with symbolic node types, status, priority, confidence, sources, and edges. No inspected path trains model weights or embeddings; internalizations may produce adapter files, but the built-in `noop` profile and manifest machinery are artifact governance, not evidence of automatic weight learning.

**Lineage.** Decapod's trace-derived lineage is unusually explicit for eval artifacts: plans have hashes, traces have hashes, verdicts record judge model and prompt hashes, aggregates record plan hashes and run counts, and gate requirements point to aggregates. Worker lessons have weaker lineage: they cite `event:<task_id>` and include a context summary, but they do not preserve the full task execution trace in the lesson body. Procedural knowledge has a stronger approval ledger through `knowledge.promotions.jsonl`.

**Behavioral authority.** Raw trace bundles, task events, feedback entries, ordinary knowledge entries, and federation observation/lesson nodes are knowledge artifacts when they advise future work. Eval gate requirements, required aggregate decisions, proof plans, workspace publish checks, and procedural knowledge entries are system-definition artifacts because they validate, block, or authorize promotion. The trace-derived loop is deliberately not silent self-modification: promotion requires explicit artifacts, gates, and often approval.

**Scope and timing.** Scope is repo-local and task/eval-plan-local. Timing is staged: run or ingest traces, judge/aggregate/bucket, gate, then allow or block promotion. Worker lessons are recorded after task completion, not during the same inference step that produced the work.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Decapod belongs with governed artifact-learning systems. It strengthens the claim that trace-derived learning should distinguish raw traces, diagnostic summaries, validated gates, and promoted behavior-changing surfaces. Its split is important: not every lesson or trace becomes instruction; only CLI policies, proof/eval gates, procedural entries, workspace rules, or generated specs have system-definition authority.

## Curiosity Pass

**The implementation is broad enough that authority boundaries matter more than feature count.** The same repository contains Markdown constitutions, generated specs, SQLite rows, JSONL ledgers, worktrees, proof command outputs, internalization manifests, and CLI gates. Calling all of that "memory" would hide the main design lesson: Decapod is a bundle of retained artifacts with different consumers and force.

**The constitution is partly executable by embedding and routing, but not every claim is enforced.** `constitution/interfaces/CLAIMS.md` marks some claims as enforced, partially enforced, or planned, and the code contains both hard gates and staged contracts ([constitution/interfaces/CLAIMS.md](https://github.com/DecapodLabs/decapod/blob/178a7da05f703dc07607926e4d9556b6f8592cd4/constitution/interfaces/CLAIMS.md)). Reviews should avoid treating all constitution text as implemented runtime behavior.

**SQLite gives concurrency but creates hidden-review pressure.** The DB and broker design are pragmatic for multi-agent task ownership, graph memory, and append-only events. For a KB like commonplace, the cost is that ordinary code review cannot see semantic changes unless exported views and replay gates stay fresh.

**Generated specs could become either helpful contract memory or stale noise.** Decapod has manifest hashes, repo-signal fingerprints, validation gates, and update guidance, but generated specs still require maintenance discipline. If agents stop treating them as living contracts, they become high-authority stale prose.

**Internalization is governance-first.** The reviewed implementation is more convincing as a lifecycle contract for compressed context than as a demonstrated compression system. That is still valuable: many systems add summarized or embedded memory before defining source binding, replayability, attach rights, expiry, and inspection.

## What to Watch

- Whether Decapod keeps tightening the gap between constitution claims and executable gates, especially for claims marked partially enforced or planned.
- Whether federation's event replay, derived index freshness, and graph export stay reliable enough for humans to review DB-backed memory.
- Whether internalizer profiles beyond `noop` become common, and whether their adapter behavior remains inspectable through manifests, leases, and replay recipes.
- Whether trace-derived worker lessons gain stronger lineage back to task events, diffs, proof artifacts, and failure modes.
- Whether project specs become a stable agent-facing contract or drift into generated boilerplate that agents ignore.

---

Relevant Notes:

- [behavioral authority](../../notes/definitions/behavioral-authority.md) - classifies: Decapod artifacts differ by consumer, channel, and force
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: ordinary docs, traces, feedback, and knowledge/federation nodes advise future agents
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: CLI gates, proof plans, workspace rules, eval gates, and procedural entries enforce or authorize behavior
- [storage substrate](../../notes/definitions/storage-substrate.md) - sharpens: Decapod mixes repo files, SQLite, JSONL ledgers, generated artifacts, and worktrees
- [representational form](../../notes/definitions/representational-form.md) - sharpens: Decapod's operative parts span prose, symbolic records, executable gates, and potential adapter files
- [lineage](../../notes/definitions/lineage.md) - grounds: hashes, manifests, provenance refs, event logs, and replay recipes determine reviewability
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - compares-with: Decapod activates memory through CLI calls and gates before the next agent action
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Decapod is a governed trace-to-artifact-to-gate system, not an unmanaged self-rewrite loop
