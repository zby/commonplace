---
description: "SAGE review: consensus-governed local agent memory with MCP turn capture, hooks, hybrid recall, decay, and corroboration"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags:
  - trace-derived
status: current
last-checked: "2026-06-04"
---

# SAGE

SAGE, from l33tdawg, is a local and multi-agent memory infrastructure for AI agents. At the reviewed commit it exposes memory through REST, MCP tools, Claude/Codex lifecycle hooks, and a desktop/dashboard surface; records are submitted as signed transactions, ordered by a CometBFT/ABCI app, mirrored into query stores, and later recalled through semantic, full-text, or hybrid search. Its distinctive design is not just storage, but governance: memory writes carry identity, domain access, validation, confidence decay, corroboration, and upgrade/content-validation fork gates.

**Repository:** https://github.com/l33tdawg/sage

**Source directory:** related-systems/sage

**Reviewed commit:** [6abd18e7f00d259bdd2c3af800b12d05759d4fb6](https://github.com/l33tdawg/sage/commit/6abd18e7f00d259bdd2c3af800b12d05759d4fb6)

**Last checked:** 2026-06-04

## Core Ideas

**Memory is governed before it becomes queryable.** `POST /v1/memory/submit` validates content, type, domain, and confidence, checks domain write access, builds a `TxTypeMemorySubmit`, embeds the caller identity proof, signs the transaction, stages off-chain embedding/provider data, and waits for CometBFT commit before tags and activity metadata are finalized ([api/rest/memory_handler.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/api/rest/memory_handler.go)). The memory lifecycle documentation describes the split between on-chain BadgerDB state and the off-chain projection, with status moving through proposed, committed, challenged, and deprecated states ([docs/reference/concepts/memory-lifecycle.md](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/docs/reference/concepts/memory-lifecycle.md), [internal/memory/model.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/memory/model.go)).

**The agent-facing API is a memory discipline, not just CRUD.** The MCP server registers `sage_turn`, `sage_remember`, `sage_recall`, `sage_reflect`, `sage_forget`, `sage_task`, `sage_corroborate`, and governance tools ([internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/mcp/tools.go)). `sage_turn` recalls committed memories for the current topic, stores an observation when one is supplied, and checks the pipeline inbox in one tool call; the server also nudges or blocks after too many non-SAGE calls without `sage_turn` ([internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/mcp/tools.go), [internal/mcp/server.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/mcp/server.go)).

**Lifecycle hooks add coarse read-back and boundary writes.** `sage-gui mcp install` and `sage-gui codex install` write hook configurations for SessionStart, SessionEnd, PreCompact, UserPromptSubmit, Stop, and SubagentStop ([cmd/sage-gui/mcp.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/cmd/sage-gui/mcp.go), [cmd/sage-gui/codex.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/cmd/sage-gui/codex.go)). SessionStart calls `sage-gui hook session-start`, fetches recent committed memories, and prints a context block; SessionEnd posts a lifecycle observation through `/v1/memory/submit` ([cmd/sage-gui/hook.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/cmd/sage-gui/hook.go), [docs/HOOKS.md](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/docs/HOOKS.md)).

**Recall is bounded by settings and fused indexes.** Explicit `sage_recall` and the recall phase of `sage_turn` use semantic vector search, FTS5 search, or a hybrid BM25/vector path with Reciprocal Rank Fusion, top-k settings, confidence thresholds, domain/provider filters, and classification gates ([internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/mcp/tools.go), [api/rest/memory_handler.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/api/rest/memory_handler.go), [internal/store/hybrid.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/store/hybrid.go)). Context efficiency is therefore selection and mode control: default top-k recall, `full`/`bookend`/`on-demand` memory modes, lifecycle prefetch capped at ten recent memories, and hybrid oversampling/fusion. It is not a summarization or progressive-disclosure system.

**Confidence and trust are live query-time properties.** Confidence decays by domain-specific rates unless the record is an open task, and corroborations boost confidence at query time without changing the stored base score ([internal/memory/confidence.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/memory/confidence.go), [docs/reference/concepts/consensus-confidence-decay.md](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/docs/reference/concepts/consensus-confidence-decay.md)). The app-v10 corroboration guard rejects self-corroboration, duplicate corroboration, and corroborating unknown memories after the fork is active ([internal/abci/app.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/abci/app.go), [internal/abci/appv10_fork_test.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/abci/appv10_fork_test.go)).

**The latest tree includes operator-gated consensus evolution.** The new `sage-gui upgrade` command submits signed, strictly sequential app-version upgrade proposals so app-v7 through app-v10 gates can be activated through governance rather than remaining unreachable on long-lived chains ([cmd/sage-gui/upgrade.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/cmd/sage-gui/upgrade.go), [internal/abci/app.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/abci/app.go)). The content-validator registry is deployment-agnostic and boot-registered; validators are pure functions over memory records and can close a domain so unrecognized outcome classes reject instead of passing through ([internal/contentvalidator/registry.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/contentvalidator/registry.go)).

## Artifact analysis

- **Storage substrate:** `sqlite` `rdbms` `kv` `files` `repo` `service-object` — Personal mode centers local SQLite data and optional encrypted local storage, multi-node and documentation paths include PostgreSQL projections, consensus state lives in BadgerDB-like key/value state, hooks/keys/settings live as local files, generated `.claude`/`.codex` artifacts may sit in project repositories, and REST/MCP/dashboard services assemble memory for consumers.
- **Representational form:** `prose` `symbolic` `parametric` — Memory content, reflections, hook prefetch blocks, and boot instructions are prose; transaction types, memory status, domains, classifications, access grants, hooks, validator decisions, and settings are symbolic; embeddings and hybrid/vector rankings are distributed-parametric selectors.
- **Lineage:** `authored` `imported` `trace-extracted` — Source code, skill instructions, validators, hooks, prompts, and policies are authored; explicit `sage_remember` and REST submissions import user/agent-chosen content; `sage_turn`, `sage_reflect`, SessionEnd hooks, task records, and pipeline journals derive durable records from agent-session traces and lifecycle events.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Committed memories advise future agents as context; the SAGE skill, MCP initialize instructions, hook output, and boot instructions can instruct; domain access, classification, turn discipline, content validators, challenge/deprecation, and fork gates enforce; domains/tags/providers/branches route; app validators, schema checks, and consensus votes validate; BM25/vector/RRF/confidence/corroboration rank; trace-derived records and reflections form the system's learning substrate.

**Committed memory records.** Storage substrate: local SQL projection plus on-chain key/value status, with optional embeddings and provider metadata staged as supplementary data. Representational form: prose content plus symbolic metadata, hashes, status, access/classification fields, timestamps, confidence, task status, and optional embedding vectors. Lineage: imported when explicitly remembered; trace-extracted when produced by `sage_turn`, `sage_reflect`, hooks, or pipeline bookkeeping. Behavioral authority: knowledge when returned as context, ranking when selected by search/confidence/corroboration, and instruction when hook or MCP surfaces place it in the agent's prompt.

**Skill, hook, and MCP operating surfaces.** Storage substrate: source files, generated project hook scripts, MCP JSON/config files, and local memory-mode settings. Representational form: prose instructions plus symbolic tool schemas and hook event maps. Lineage: authored by SAGE and installed or healed into the user's project. Behavioral authority: instruction and enforcement, because these surfaces tell the agent when to call memory tools and can block or nudge workflows that skip `sage_turn`.

**Consensus, validation, and governance artifacts.** Storage substrate: ABCI state, governance proposal records, validator votes, access grants, app-version fork gates, and optional content-validator registries. Representational form: symbolic transaction/state machines and validator functions. Lineage: authored code plus on-chain events from agents/operators. Behavioral authority: validation, enforcement, routing, and governance over which records commit, which domains are readable/writable, and which protocol rules are active.

**Access structures and ranking state.** Storage substrate: FTS indexes, embeddings, confidence/corroboration data, query-time settings, and hybrid-recall parameters. Representational form: symbolic filters plus parametric vectors and ranking scores. Lineage: derived from committed memory content, query text, provider settings, and corroboration/challenge events. Behavioral authority: ranking and routing; they decide what reaches a future context, but they do not replace the underlying memory record.

**Promotion path.** SAGE can move a trace observation into a proposed memory, then a consensus-committed record, then a higher-salience retrieved context item through confidence, corroboration, and repeated use. It can also deprecate a memory through challenge or validation failure. It does not promote a remembered lesson into a reviewed executable rule or standalone code artifact automatically; the strongest authority promotion remains within SAGE's memory lifecycle and prompt/tool discipline.

## Comparison with Our System

| Dimension | SAGE | Commonplace |
|---|---|---|
| Primary purpose | Runtime institutional memory for local and multi-agent assistants | Git-native methodology KB for agents and maintainers |
| Canonical retained unit | Consensus-governed memory record plus metadata, embeddings, status, confidence, and access policy | Typed Markdown artifact with frontmatter, citations, links, validation, and review state |
| Write path | REST/MCP/hook submissions become signed transactions and committed/queryable records | Human/agent-authored files, snapshots, indexes, validation, and semantic review |
| Read-back | Explicit recall tools plus lifecycle prefetch and per-turn recall/store cycle | Mostly deliberate pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | CometBFT ordering, validators, domain access, classification, content validators, challenge/corroboration, upgrade gates | Git history, type specs, collection contracts, validators, review bundles, replacement archives |

SAGE is stronger as runtime infrastructure. It offers localhost installation, MCP tools, lifecycle hooks, signed REST, a dashboard, confidence decay, hybrid retrieval, and a consensus model that can coordinate several agents. Commonplace is stronger as inspectable methodology memory: its primary artifacts are readable, cite their sources, live in git, and can be reviewed as claims before acquiring procedural authority.

The important design contrast is authority granularity. SAGE can inject recent or relevant memories quickly, and it can govern whether a memory commits. Commonplace is slower but more explicit about type, source, claim status, outbound links, replacement history, and when a knowledge artifact becomes an instruction or validation rule.

### Borrowable Ideas

**Expose memory mode as an operator setting.** Ready now. SAGE's `full`, `bookend`, and `on-demand` modes are a clean way to tune context cost without changing the underlying memory store. Commonplace could apply a similar mode to session boot packs or review workflows.

**Separate lifecycle hooks from deliberate recall.** Ready for experiments. SessionStart prefetch and PreCompact reminders are useful boundaries, while `sage_recall` remains explicit. Commonplace could keep cheap boundary reminders without making every note automatically enter context.

**Treat corroboration as salience, not truth.** Ready as vocabulary. SAGE's corroboration affects confidence at query time, while the record and its base confidence remain visible. Commonplace could use repeated independent references as a prioritization signal while still requiring citations and review for authority.

**Make content validation deployment-specific.** Needs a concrete Commonplace use case. SAGE ships generic validator plumbing and lets deployments register domain/outcome validators. Commonplace could do the same for project-local gates rather than baking domain schemas into the framework.

**Do not import consensus machinery without a coordination problem.** Not ready for Commonplace. SAGE's BFT path is meaningful for multi-agent trust and local runtime state. For Commonplace's repo-based methodology KB, git, validation, review, and explicit promotion remain cheaper and more inspectable.

## Write side

**Write agency:** `automatic` `manual` — Manual agency appears when a user or agent explicitly calls `sage_remember`, edits dashboard settings, challenges a memory, corroborates a memory, or proposes governance changes. Automatic agency appears in `sage_turn` observation writes, `sage_reflect` writes, SessionEnd lifecycle writes, auto-registration/seed memories, duplicate skipping, validation/vote processing, confidence decay at read time, hook self-heal, and consensus status updates.

**Curation operations:** `invalidate` `decay` `promote` — Challenges and failed quorum/validation paths can deprecate memories; confidence is automatically down-weighted over time except for open tasks; corroboration boosts future query-time confidence and therefore salience without changing the stored base score. Duplicate detection prevents some new writes but does not merge or rewrite existing stored entries, so I am not counting it as `dedup`.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` `trajectories` — SAGE stores agent turn observations, end-of-task reflections, session lifecycle events, pipeline summaries, and task/backlog states; it does not automatically retain raw full transcripts.

**Learning scope:** `per-task` `per-project` `cross-task` — Individual turns and tasks create records, project identity and branch tags scope some writes, and committed memories are intended to influence later sessions and tasks for the same agent/project or permitted domain.

**Learning timing:** `online` `staged` — `sage_turn`, `sage_remember`, SessionEnd, and reflection writes happen during agent operation; governance upgrades, content-validator activation, and some lifecycle/task effects are staged through operator or consensus processes.

**Distilled form:** `prose` `symbolic` `parametric` — Durable outputs include prose memories/reflections, symbolic status/domain/access/confidence/task metadata, and embeddings/search indexes used for later selection.

**Trace source.** SAGE qualifies as trace-derived because its central agent-facing tools ask the model to summarize each turn or completed task into durable memory. The skill contract explicitly says observations are written through `sage_turn` and `sage_remember`, and that raw transcripts are not automatically captured ([sage-memory/SKILL.md](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/sage-memory/SKILL.md)). The code then turns those summaries into signed memory submissions rather than treating them as ephemeral chat context ([internal/mcp/tools.go](https://github.com/l33tdawg/sage/blob/6abd18e7f00d259bdd2c3af800b12d05759d4fb6/internal/mcp/tools.go)).

**Extraction.** The extraction oracle is mostly the acting agent plus authored tool instructions. The model decides what the observation, reflection, domain, type, and confidence should be; SAGE adds duplicate checks, low-value filters, embeddings, pre-validation, consensus voting, access control, confidence decay, and optional corroboration. This means SAGE learns from traces, but it does not independently infer deep lessons from raw transcripts unless the agent writes those lessons through the available tools.

**Scope and timing.** The loop is online for turn/session memories and staged for governance or validation changes. A memory can be project- or domain-scoped through provider, project identity, domain, classification, branch tags, and read access; future recall can cross task boundaries whenever those gates allow the memory to surface.

**Survey position.** SAGE belongs in the trace-to-memory and trace-to-reflection families. It strengthens the survey distinction between raw trace capture and distilled memory: the raw conversation is not the retained artifact; the retained artifact is the agent-authored summary plus SAGE's symbolic governance state and access structures.

## Read-back

**Read-back:** `both` — Explicit `sage_recall`, `sage_list`, and REST search are pull. SessionStart prefetch, MCP initialization instructions, turn-discipline nudges, and the `sage_turn` recall phase can put committed memory or memory-use instructions in front of the receiving agent without a separate memory-search decision by that agent.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — SessionStart prefetch is coarse recent-memory loading; domain, provider, status, tags, branch tags, access, and classification are identifier signals; FTS/BM25 uses lexical inference; semantic and hybrid recall use embeddings.

**Faithfulness tested:** `no` — The repository includes recall paths, benchmarks, tests, and documents reported memory benefits, but I did not find a code-grounded with/without read-back ablation or perturbation audit proving that a particular fired memory caused a later agent action to improve.

**Direction edge cases.** `sage_recall` is ordinary pull: the agent asks for memories. `sage_turn` is a mixed case: the agent calls one prescribed turn tool, but recall results are returned as part of the required memory cycle before the next response. SessionStart is clearer push because the hook prints recent committed memories into the agent's prompt on startup/resume/compact. Static SAGE skill instructions are not counted as memory read-back; they are baseline system-definition artifacts.

**Targeting and signal.** Coarse read-back loads the newest committed memories up to the hook limit. Instance-targeted read-back uses domain/status/provider/tag filters plus lexical or embedding relevance against the current topic/query. Hybrid recall fuses BM25 and vector results with RRF, then classification/access gates can hide records from unauthorized agents.

**Injection point.** SessionStart hook output enters the prompt at session boundary. `sage_turn` and `sage_recall` return memories before the agent proceeds with the current answer or action. SessionEnd and reflection writes are write-side maintenance for later calls, not read-back for the just-finished turn.

**Selection, scope, and complexity.** Selection is bounded by top-k recall settings, hook limit ten, minimum confidence, memory mode, domain/provider/tag/status filters, classification gates, and hybrid retrieval parameters. The returned material is flat memory snippets and metadata, not a nested graph walk or progressively revealed dossier.

**Authority at consumption.** Returned memories are mostly advisory context. The MCP server and skill instructions add stronger instruction/enforcement authority by requiring boot, turn calls, and destructive-action recall. Content validators, access controls, and governance gates have hard enforcement authority, but they govern writes and visibility rather than directly forcing the model to follow a remembered fact.

**Faithfulness.** SAGE documents and tests retrieval mechanics, lifecycle hooks, validation paths, and consensus behavior, and its bundled papers/README report benchmark benefits. Under this review contract, that is not the same as a fired-memory faithfulness test: I did not find a test that perturbs or removes specific read-back and verifies the downstream agent action changes accordingly.

**Other consumers.** Human users and operators consume the CEREBRUM dashboard, REST API, Python SDK, governance status, network management UI, and audit/release documentation. Validators consume memory records and governance proposals as consensus inputs.

## Curiosity Pass

**The agent remains the main distiller.** SAGE governs and retrieves memory, but the durable semantic content usually comes from the model's own `observation`, `dos`, and `donts` text rather than an independent transcript-mining pass.

**Consensus solves trust, not context precision by itself.** A committed memory is more trustworthy than an ungoverned note, but the agent still needs good domain labels, concise summaries, and retrieval settings to avoid context dilution.

**Read-back spans hard and soft channels.** SAGE can push recent memories through hooks and enforce turn discipline, but most remembered facts still arrive as advisory snippets rather than binding rules.

**The content-validator registry is a strong extension point.** It creates a route from memory content to deterministic validation without baking one domain's schema into the base product.

**Upgrade reachability matters for reviews.** The new `sage-gui upgrade` command changes the practical status of app-v7 through app-v10 gates: they are no longer only implemented forks, but operator-activatable on deployed chains.

## What to Watch

- Whether default installations use content validators for real domains; that would show whether the validator registry becomes ordinary memory governance or remains specialized deployment plumbing.
- Whether SAGE adds causal read-back tests: with/without a recalled memory, perturbing top-k, or checking whether agents act on a surfaced memory.
- Whether PostToolUse or batched tool-trace hooks ship; that would move SAGE from agent-authored turn summaries toward richer trace capture.
- Whether duplicate handling evolves from write admission into real merge/rewrite of existing records; that would change the curation classification.
- Whether the dashboard or API exposes enough provenance to trace a remembered lesson back to the session, model, prompt, and validator decisions that produced it.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: SAGE turns turn summaries, reflections, and lifecycle events into governed memory records.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: SAGE stores many committed records, but behavior changes through recall tools, hooks, and turn-cycle returns.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: SAGE mixes prose memories, symbolic consensus state, hooks, validation logic, and embedding-based selectors.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: committed memories are primarily evidence/context until read back through MCP or hooks.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: MCP tool schemas, skill instructions, validators, access rules, and fork gates shape future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: SAGE retains agent-authored summaries and reflections derived from session traces.
