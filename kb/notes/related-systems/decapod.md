---
description: Daemonless control plane for AI coding agents that forces intent specification, boundary enforcement, and proof-gated completion before work can land — production exemplar of oracle-as-infrastructure
type: note
areas: [related-systems]
status: current
last-checked: 2026-03-10
---

# Decapod

A daemonless, local-first control plane for AI coding agents, built in Rust by DecapodLabs. Agents call it on demand to refine human intent into explicit specifications, enforce boundaries, and produce proof-backed completion guarantees. Humans never interact with Decapod directly — it sits invisibly between agents and code. The distinguishing commitment is that no work can be promoted without passing proof gates: "VERIFIED" is a status earned by evidence, not claimed by narrative.

**Repository:** https://github.com/DecapodLabs/decapod

## Core Ideas

**Control plane, not knowledge system.** Decapod is infrastructure for governing agent behaviour, not a medium for accumulating and evolving knowledge. Its federation graph stores decisions, commitments, and lessons — but these serve agent coordination, not learning. The knowledge exists to constrain future agent actions, not to build understanding. This is a fundamentally different purpose from commonplace, which treats knowledge as the primary output.

**Proof-gated completion is oracle enforcement.** Work units progress through Draft → Executing → Claimed → Verified, but the Verified transition only fires if a proof plan passes. The proof plan is an ordered list of gates — each gate is an [oracle](../oracle-strength-spectrum.md) that checks whether the work satisfies its specification. Decapod doesn't build oracles (that's the agent's job), but it enforces that oracles exist and pass before promotion. This is the clearest production implementation of the principle that [error correction requires decorrelated checks above chance](../error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — Decapod provides the enforcement infrastructure, agents supply the discriminative power.

**Embedded constitution as immutable methodology.** Around 60 governance documents (core contracts, specs, interface rules, plugin contracts, methodology guides) are embedded into the binary via `include_str!()` macros. Agents fetch relevant slices via context capsules rather than reading files directly. This is [stabilisation](../stabilisation.md) taken past its useful range — the markdown is copied verbatim into the binary with no transformation, so the embedding hides the methodology from users without adding any build-time guarantee. See "The Compilation Question" below for the full analysis.

**Daemonless, repo-native state.** Everything lives in `.decapod/` — four SQLite databases (governance, memory, automation, todo), event logs, and config. No background service. Agents call the binary on demand and it exits when done. State is repo-local, version-controllable, and inspectable. This is the same filesystem-first instinct as commonplace, though the storage format diverges sharply (SQLite vs markdown).

**Typed federation graph.** Knowledge is represented as typed nodes (Decision, Commitment, Person, Preference, Lesson, Project, Handoff, Observation) connected by typed edges (relates_to, depends_on, supersedes, invalidated_by). Critical types (Decision, Commitment) are immutable after creation — evolution happens through supersession chains, not edits. All mutations are event-sourced in append-only `.jsonl` logs. The type system enforces provenance gating: critical nodes must cite sources at creation.

**RPC-first agent interface.** Agents communicate via JSON-RPC and receive structured response envelopes containing: a receipt (what happened), a context capsule (relevant doc slices), allowed next operations, blockers, interlocks (hard stops), advisories (soft guidance), and attestations (proof artifacts). This is an explicit calling convention — the agent always knows what it can do next and what's blocking it.

**Workspace isolation.** Agents must work in git worktrees under `.decapod/workspaces/`, never on main/master. Validation invariants enforce this. For multi-agent scenarios, each agent gets its own worktree, preventing silent overwrites. This is a code-level solution to the same coordination problem that [bounded-context orchestration](../bounded-context-orchestration-model.md) addresses architecturally.

## How It Actually Works

Decapod's self-description — "invisible layer between agents and code" — suggests a proxy or middleware. The actual mechanism is simpler and more familiar: it's an instruction-injecting CLI that agents call voluntarily.

### Agent Integration: Instruction Injection, Not Interception

Decapod hooks into agent CLIs through the same mechanism as commonplace's CLAUDE.md: it writes markdown entrypoint files into the repo root. `decapod init` generates `CLAUDE.md`, `GEMINI.md`, `CODEX.md`, and `AGENTS.md`. These are ordinary files that agent CLIs already know to load — Claude Code reads `CLAUDE.md`, Gemini reads `GEMINI.md`, etc. All of them point to `AGENTS.md` as the "universal contract."

There is no proxy, no MCP server, no hooks, no protocol-level interception. The "integration" is entirely instructional: the entrypoint files tell the agent to run `decapod` commands at specific checkpoints. The agent must voluntarily comply. If an agent ignores the instructions, nothing stops it — the enforcement is social (the agent follows instructions) not mechanical (the system intercepts calls).

This means Decapod works with any CLI that loads markdown entrypoint files. It doesn't require tool-specific plugins or adapters. But it also means the "control plane" controls only as much as the agent obeys. The entrypoint templates are generated from hardcoded Rust functions in `assets.rs` — `template_named_agent()` produces identical content for CLAUDE.md, GEMINI.md, and CODEX.md, differing only in the filename header.

The AGENTS.md contract instructs a mandatory initialization sequence:

```
decapod validate          → check repo consistency
decapod docs ingest       → dump constitution to stdout for agent absorption
decapod session acquire   → get session token
decapod rpc --op agent.init → initialize, get capabilities and allowed actions
decapod workspace ensure  → create isolated git worktree
```

Each step is an explicit CLI invocation. The agent shells out, reads stdout, and decides what to do next. Between calls, Decapod holds no state in memory — it reads from and writes to `.decapod/` on every invocation.

### The Constitution: include_str!() at Compile Time

The "compiled constitution" is implemented via Rust's `include_str!()` macro. A build script (`build/constitution_index.rs`) scans seven directories under `constitution/` — core, specs, plugins, interfaces, methodology, architecture, docs — and registers ~60 markdown files for change tracking. At compile time, `assets.rs` embeds each file as a `pub const` string literal using a declarative macro:

```rust
embedded_docs! {
    "core/DECAPOD.md" => EMBEDDED_CORE_DECAPOD,
    "specs/INTENT.md" => EMBEDDED_SPECS_INTENT,
    // ... ~60 entries
}
```

The macro generates `get_embedded_doc(path)` (a match statement returning the corresponding const) and `list_docs()` (returning all paths). This is straightforward compile-time embedding — the files become string constants in the binary. No serialization, no compression, no indexing.

At runtime, agents access the constitution through three commands:

- **`decapod docs show <path>`** — prints one document. Supports `--source embedded|override|merged` to control whether project-local overrides are appended.
- **`decapod docs ingest`** — iterates over ALL embedded documents and dumps them sequentially to stdout with `--- BEGIN <path> ---` / `--- END <path> ---` delimiters. The agent is expected to absorb this entire dump into its context window. For ~60 documents of governance prose, this is a significant context cost — the constitution competes with the actual task for context space.
- **`decapod docs search --query <text>`** — returns scoped fragments using lexical keyword matching. Tokenizes the query into 3+ character lowercase terms, counts occurrences in each document, boosts scores for operation/path/tag bindings (hardcoded in a `get_bindings()` function), and returns the top-N fragments. No embeddings, no vector search — pure substring counting with a static boost table.

The override mechanism (`OVERRIDE.md` in `.decapod/`) uses markdown heading structure: content under `### core/DECAPOD.md` gets appended to the embedded base when an agent requests the merged view. A "CHANGES ARE NOT PERMITTED ABOVE THIS LINE" marker prevents overriding the override format itself.

### The RPC: Synchronous CLI, Not a Server

Despite the "RPC" nomenclature, there is no server. The agent runs:

```bash
decapod rpc --op agent.init
decapod rpc --op context.resolve --params '{"query":"...","limit":5}'
```

The binary parses the operation name from `--op`, optionally reads JSON from `--params` or stdin, dispatches through a hardcoded match statement in `lib.rs`, executes synchronously, prints a JSON response envelope to stdout, and exits. Each invocation is a fresh process.

The response envelope is the most interesting mechanical detail. Every RPC response includes:

- **receipt** — operation name, timestamp, input/output hashes, touched paths, governing constitution anchors
- **context_capsule** — relevant doc fragments scoped to the operation
- **allowed_next_ops** — typed list of legal next operations with reasons and required parameters
- **blocked_by** — typed list of blockers with resolution hints
- **interlock** / **advisory** / **attestation** — binding constraints, non-binding guidance, proof artifacts

The `allowed_next_ops` field is the mechanism by which Decapod attempts to guide agent workflow without a persistent connection. After each call, the agent knows what it's permitted to do next — not because a server is tracking state, but because the binary re-derives the answer from `.decapod/` state on every invocation.

### Proof Gates: Shell Commands with Exit Codes

The proof system reads `.decapod/proofs.toml`, which lists shell commands:

```toml
[[proof]]
name = "tests"
command = "cargo"
args = ["test"]
required = true
```

`decapod proof run` executes each command via `std::process::Command`, captures exit code and output (truncated to 1000 chars), and records results to `proof.events.jsonl`. A proof passes if exit code is 0. The proof plan is a simple sequential loop — no parallel execution, no dependency ordering between proofs.

The connection to work unit status is the key enforcement: `VERIFIED` status can only be set if all required proofs pass. This is enforced by a test (`tests/workunit_publish_gate.rs`), not by the runtime — the invariant is that the code path setting VERIFIED checks proof results, and the test suite verifies that code path works correctly.

Proofs don't block the agent in real time. The agent can work, run `decapod validate`, see failures, fix them, and retry. The gate is at status transition, not at command execution.

### Validation: Convention Enforcement via Coded Checks

`decapod validate` runs parallel validation gates using Rust's rayon. Each gate checks a specific invariant:

- Namespace purge (no legacy references to previous product names)
- Schema consistency across SQLite databases
- Work unit manifest integrity
- Store boundary (agents haven't directly mutated `.decapod/` files)
- Workspace isolation (protected branches untouched)

The gates use a `gate!` macro that captures timing and pass/fail. The result is a structured report: pass count, fail count, failure messages. Validation is bounded by design — a test enforces that it terminates within a time limit.

### The Compilation Question

The compile-time embedding is the most puzzling design choice. The constitution files are raw markdown — no transformation, no indexing, no compilation into a different representation. `include_str!()` copies the text verbatim into the binary; at runtime, `get_embedded_doc()` returns it unchanged via a match statement. The same result could be achieved with `fs::read_to_string("constitution/core/DECAPOD.md")` at negligible cost.

What embedding buys: hermetic deployment (single binary, no external files to distribute). What it costs: 464KB of invisible governance prose that users cannot read, modify, or even inspect without running `decapod docs show`. The OVERRIDE.md mechanism — which reads from disk at runtime — already concedes that projects need to customize governance. But overrides are append-only; users can add rules, not see, remove, or replace the embedded base.

For compiled code, embedding makes sense — the compiled artifact is structurally different from the source and benefits from build-time guarantees. For natural language prose interpreted by an LLM, the "compilation" is just hiding. The markdown isn't being compiled *into* anything; the embedded representation is identical to the source representation. A `constitution/` directory shipped alongside the binary — or even vendored into `.decapod/` at `decapod init` — would give users the same hermetic deployment with full visibility, editability, and no recompilation required.

This is [over-stabilisation](../stabilisation.md): the methodology is crystallised past the point of benefit. The governance prose needs interpretive flexibility (hence OVERRIDE.md), but the embedding mechanism denies it. The useful stabilisation is in the CLI itself — the validation gates, proof enforcement, and response envelope structure are genuinely compiled behaviour. The constitution content could live as files without losing any enforcement capability.

### What the "Invisible Layer" Claim Actually Means

Decapod describes itself as "invisible" because humans don't interact with it — only agents do. But mechanistically, it's visible to agents in exactly the same way commonplace is: through markdown files that instruct agent behaviour. The differences are:

1. **Structured responses.** Commonplace returns prose (skill output, validation messages). Decapod returns typed JSON with explicit fields for blockers, allowed operations, and proof artifacts.
2. **State in databases.** Commonplace's state is readable markdown. Decapod's state is in SQLite — agents must use the CLI to read it, they can't `cat` a database file.
3. **Constitution as binary, not as repo files.** Commonplace's methodology lives in `CLAUDE.md`, `WRITING.md`, `instructions/` — files the agent reads directly. Decapod's methodology is compiled in and served through the CLI.

But the fundamental integration mechanism is identical: markdown entrypoint files that instruct agents to call tools. Neither system intercepts agent communication at the protocol level. Neither has hooks that fire automatically. Both depend on agent compliance with written instructions.

## Comparison with Our System

Decapod governs agents; commonplace educates them. The comparison is between control (enforce boundaries, gate promotions, prove completion) and knowledge (accumulate understanding, evolve through maturation, support contextual competence). The overlap is in shared concerns: how to represent structured knowledge, how to enforce methodology, how to coordinate agent work.

| Dimension | Decapod | Commonplace |
|---|---|---|
| Primary purpose | Govern agent behaviour | Accumulate and evolve knowledge |
| Storage | SQLite (4 databases) + event logs | Markdown files + git |
| Knowledge types | 8 node types (enum in Rust) | Document types (YAML frontmatter, convention-enforced) |
| Relationships | Typed graph edges (4 types), DAG-enforced | Markdown links with prose semantics |
| Methodology enforcement | Compiled constitution + invariant validation | CLAUDE.md + instructions + skills (interpreted) |
| Evolution model | Supersession chains (immutable nodes) | In-place editing with status transitions |
| Agent interface | JSON-RPC with response envelopes | Markdown instructions + skill dispatch |
| Verification | Proof plans with ordered gates | Validation scripts + convention checks |
| Multi-agent | Workspace isolation (worktrees) + task claiming | Single-agent per session |
| Context delivery | Context capsules (scoped doc slices) | Progressive disclosure (descriptions first, full on demand) |

**Where Decapod is stronger.** Proof-gated completion is a real enforcement mechanism — work cannot be promoted without evidence. Our validation is advisory: `/validate` flags problems but doesn't block anything. Decapod's response envelopes give agents structured awareness of what's allowed and what's blocked, where our agents must interpret prose instructions. The supersession model creates an auditable history of how decisions evolved, where our in-place editing loses intermediate states (git history notwithstanding, no agent will traverse it).

**Where commonplace is stronger.** Knowledge has a [maturation lifecycle](../learning-theory.md) — notes progress through status transitions, descriptions serve as retrieval filters, link semantics articulate how ideas relate. Decapod's federation graph stores facts about agent work but doesn't support the accumulate → stabilise → distil → discover progression. The [files-first choice](../files-not-database.md) gives us universal readability and zero-infrastructure portability that SQLite doesn't match. Our [title-as-claim](../title-as-claim-enables-traversal-as-reasoning.md) convention means traversal is reasoning — following links reads as a chain of arguments. Decapod's nodes have titles, but the titles are labels, not claims.

**The methodology enforcement comparison is the most revealing.** Decapod embeds its constitution into the binary — but since the embedding is verbatim (no transformation, no structural guarantees), the "crystallisation" is illusory. The governance prose is still interpreted by an LLM at runtime; the only thing compilation changes is who can read and edit it. The real stabilisation is in Decapod's coded enforcement — validation gates, proof checks, workspace isolation — which genuinely cannot be reinterpreted. Commonplace keeps methodology in markdown files that agents interpret directly. This maps onto the [stabilisation spectrum](../methodology-enforcement-is-stabilisation.md), but the interesting boundary is between coded enforcement (Decapod's gates, our hooks and scripts) and prose governance (Decapod's constitution, our CLAUDE.md), not between compiled and uncompiled prose.

## Borrowable Ideas

**Proof-gated status transitions.** The principle — don't let work claim completion without passing explicit checks — is immediately applicable. In commonplace, this would mean a note can't transition from `seedling` to `current` without passing structural validation (description quality, link health, index membership). Currently `/validate` runs post-hoc; making it a gate on status transition would be a meaningful upgrade. *Ready to borrow — would require skill/hook integration, not just convention.*

**Response envelopes with allowed-next-ops.** The pattern of returning not just results but also what the agent is allowed to do next is a form of [frontloading](../frontloading-spares-execution-context.md) — the control plane pre-computes the decision tree so the agent doesn't waste context reasoning about permissions. For commonplace, skill outputs could include "suggested next actions" to guide agent workflow. *Needs a use case first — our single-agent model has simpler coordination needs.*

**Supersession chains for decision evolution.** Instead of editing a decision in place, create a new node that supersedes the old one. This preserves the full decision history without relying on git archaeology. For commonplace's ADRs, this would mean a superseding ADR explicitly links to its predecessor rather than having a "superseded" status with no forward pointer. *Ready to borrow — the ADR type already has a status field; adding a `supersedes` link convention is lightweight.*

**Content-addressed artifacts for drift detection.** Hashing specifications and proof artifacts means any change is detectable — you know whether the spec the agent worked against is still the current spec. For commonplace, this could apply to source snapshots: hash the snapshot at ingest time, detect if the source has changed on re-visit. *Needs a use case first — our sources are snapshots, not live references.*

**Internalization as explicit distillation.** Decapod's internalization subsystem (turn a large doc into a mountable compressed artifact) is a production implementation of [distillation](../distillation.md) — targeted extraction from a larger body into a focused artifact shaped by specific circumstances. The key addition is the determinism classification: deterministic artifacts are replayable, best-effort ones carry runtime fingerprints. *Worth watching — we don't yet have a formal distillation pipeline.*

## What to Watch

- How far the `OVERRIDE.md` mechanism gets pushed. Decapod already has runtime constitution overrides (project-local markdown sections appended to compiled docs), but these are append-only — you can add rules, not remove or replace embedded ones. If projects start needing to suppress or contradict embedded governance, the override model may not suffice, and Decapod moves toward commonplace's fully-interpreted approach.
- Whether the federation graph develops maturation beyond supersession. Currently nodes are created, optionally superseded, and never revisited. If Decapod adds mechanisms for lessons to generate new decisions (learning from operational experience), it begins to converge with our accumulate-stabilise-distil model.
- Whether proof-gated completion generalises beyond code verification. Decapod's proof plans currently gate on test suites and validation passes. If they extend to knowledge quality (did the agent's analysis meet structural standards?), the control-plane pattern becomes relevant to knowledge systems, not just code shipping.
- How the dual-store model (user-scoped vs repo-scoped) evolves. This is a form of [three-space separation](../three-space-agent-memory-maps-to-tulving-taxonomy.md) — agent-local state vs project knowledge — and the boundary decisions will be informative.

---

Relevant Notes:

- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — exemplifies: proof-gated completion is oracle enforcement as infrastructure; Decapod doesn't build oracles but ensures they exist and pass
- [methodology-enforcement-is-stabilisation](../methodology-enforcement-is-stabilisation.md) — exemplifies: embedded constitution is stabilisation at the crystallised extreme; comparison illuminates the trade-off between interpretive flexibility and enforcement rigidity
- [files-not-database](../files-not-database.md) — contrasts: Decapod chose SQLite + event sourcing where commonplace chose files + git, making it the strongest counterpoint to the files-first argument among systems reviewed at code depth
- [bounded-context-orchestration-model](../bounded-context-orchestration-model.md) — extends: workspace isolation and RPC response envelopes are code-level implementations of scheduler-mediated agent coordination
- [stabilisation](../stabilisation.md) — exemplifies: the supersession model (immutable nodes, evolution through new nodes) is a pure stabilisation strategy — once crystallised, a decision never reverts
- [distillation](../distillation.md) — exemplifies: internalization subsystem is a production distillation pipeline with determinism classification
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: context capsules address the volume dimension by delivering scoped doc slices rather than full documents
- [agent-statelessness-makes-routing-architectural-not-learned](../agent-statelessness-makes-routing-architectural-not-learned.md) — exemplifies: Decapod's mandatory initialization sequence and `allowed_next_ops` response field are architectural routing solutions for stateless agents — the binary re-derives permitted actions from disk state on every invocation because no agent remembers the last call
- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: Decapod adds a new position (control-plane governance, proof-gated completion, compiled constitution) not covered by existing entries

Topics:

- [related-systems-index](./related-systems-index.md)
