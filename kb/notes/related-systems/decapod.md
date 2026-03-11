---
description: Rust governance kernel for AI coding agents that forces intent codification, proof-gated completion, and workspace isolation before code touches a repo — strongest reference for hard-oracle verification in agent workflows, but constitution documents claim transformations the code does not perform
type: note
areas: [related-systems]
status: current
last-checked: 2026-03-10
---

# Decapod

A Rust CLI binary ("governance kernel") that agents call on demand to enforce process discipline around coding tasks. The agent writes code; Decapod forces it to clarify intent, respect boundaries, and prove completion before anything lands. It ships as a daemonless binary with an embedded constitution (120+ markdown governance documents compiled into the binary at build time via `rust-embed`), a SQLite-backed state layer, and git worktree isolation. Built by DecapodLabs, MIT-licensed, v0.47.10.

**Repository:** https://github.com/DecapodLabs/decapod

## Core Ideas

**Intent must be explicit before mutation.** Decapod's first foundation demand is that agents must clarify what the human asked for before writing code. The scaffold/interview subsystem (`src/core/scaffold.rs`) generates spec artifacts — intent documents, architecture sketches, validation criteria — in `.decapod/generated/specs/`. These are plain-text files the agent and human can inspect. The mechanism is a structured questioning flow (`scaffold.next_question` / `scaffold.generate_artifacts`) that forces the agent to answer before proceeding.

**Proof-gated completion replaces narrative claims.** The `VERIFIED` status on a WorkUnit requires that every gate in a proof plan has a passing result — enforced in `src/core/workunit.rs` via `ensure_verified_ready()`, which checks that `proof_plan` is non-empty and every gate has a corresponding `"pass"` entry in `proof_results`. Proofs themselves are configurable external commands defined in `.decapod/proofs.toml` (run tests, check linting, etc.) executed via `src/core/proof.rs`. The proof runner shells out to the configured commands and records exit codes, durations, and results to `proof.events.jsonl`.

**Workspace isolation prevents protected-branch mutation.** Agents cannot work on `main`, `master`, `production`, `stable`, `release/*`, or `hotfix/*`. The workspace subsystem (`src/core/workspace.rs`) checks `is_branch_protected()` against a hardcoded pattern list and refuses to proceed. Work happens in git worktrees under `.decapod/workspaces/`, scoped to a claimed TODO item. The workspace must contain the TODO's ID or hash in the branch name.

**Embedded constitution as just-in-time context.** 120+ markdown governance documents live in `constitution/` and are compiled into the binary at build time. Agents query them via `decapod docs search` or `decapod rpc --op context.scope`, which performs deterministic lexical matching (`src/core/docs.rs`): tokenise the query, score each embedded document by term frequency plus binding boosts (operation -> document mappings), return the top-N fragments. No vector embeddings, no LLM in the retrieval path — pure string matching with a scoring function.

**Context capsules are hash-verified document excerpts.** A `DeterministicContextCapsule` (`src/core/context_capsule.rs`) packages document fragments with a SHA-256 hash over the canonical JSON (sorted, deduplicated sources and snippets). The capsule is bound to a task/workunit and carries a policy binding (risk tier, policy hash, repo revision). Validation checks that the stored hash matches recomputation, confirming the capsule has not been tampered with since creation.

**Internalization turns documents into mountable artifacts.** The internalization subsystem (`src/plugins/internalize.rs`) creates governance-tracked wrappers around external documents, with explicit create/attach/detach/inspect lifecycle, session-scoped mount leases (default 1800s), source-hash verification, and pluggable "internalizer profiles." The only shipped profile is `noop` — it writes an empty `adapter.bin` and returns. The infrastructure for running external internalizer executables exists but no non-trivial profile ships with the binary.

**Federation is a typed knowledge graph.** The federation plugin (`src/plugins/federation.rs`) stores typed memory nodes (decision, commitment, person, preference, lesson, project, handoff, observation) in SQLite with edges (relates_to, depends_on, supersedes, invalidated_by), priority levels (critical, notable, background), confidence tags (human_confirmed, agent_inferred, imported), and provenance tracking. Search is SQL `LIKE` on title/body.

**Obligation graph tracks dependency-aware work.** The obligation engine (`src/core/obligation.rs`) manages a DAG of obligations where status is derived, never asserted — an obligation is `met` only when all dependencies are `met`, all required proofs pass, and a state commit root is present. Cycle detection runs DFS on insertion.

**Validation is a parallel gate runner.** `decapod validate` (`src/core/validate.rs`) runs 30+ checks in parallel via rayon, each as a named gate with timing: namespace purity, frontmatter structure, workunit manifest integrity, capsule hash verification, spec fingerprint consistency, gitignore rules, and more. It produces a typed `ValidationReport` with pass/fail/warn counts and per-gate timings.

## Comparison with Our System

Decapod and commonplace occupy adjacent but distinct niches: Decapod governs the agent's behavior during coding tasks (process control), while commonplace structures the agent's knowledge across sessions (knowledge management). The overlap is in how both use filesystem artifacts to constrain agent behavior.

| Dimension | Decapod | Commonplace |
|---|---|---|
| Primary concern | Process governance (did the agent do the right thing?) | Knowledge governance (does the agent know the right things?) |
| Enforcement model | Hard gates: validation must pass, VERIFIED requires proof-plan | Advisory: `/validate` flags problems but does not block |
| Storage | SQLite databases + JSON files in `.decapod/` | Markdown files + git in `kb/` |
| Constitution / methodology | 120+ compiled markdown docs, queried by lexical search | CLAUDE.md + instructions + skills, loaded by agent navigation |
| Knowledge lifecycle | Federation nodes: active/superseded/deprecated/disputed | Notes: seedling/current/outdated, type transitions |
| Validation | 30+ parallel deterministic gates, bounded-time guarantee | LLM-powered skill with structural + semantic checks |
| Multi-agent | Workspace isolation via git worktrees, TODO claiming with agent assignment | Single agent per session |
| Context delivery | Just-in-time: agent queries constitution on demand, gets scored fragments | Progressive disclosure: descriptions at startup, full content on demand |
| Proof model | External commands (tests, lints) with exit-code pass/fail | No formal proof model |
| Link semantics | None — documents reference each other by path but with no typed relationships | Explicit relationship types (extends, grounds, contradicts, enables, exemplifies) |

**Where Decapod is stronger.** The proof-gated completion model is genuinely novel among reviewed systems. Rather than trusting the agent's claim that work is done, it requires external commands to pass. The workspace isolation via git worktrees solves a real multi-agent coordination problem. The bounded-time validation guarantee (tested in `tests/validate_termination.rs`) is a concrete engineering commitment we lack.

**Where commonplace is stronger.** Knowledge has a lifecycle and relationships. Our notes mature through status transitions, link semantics articulate how ideas relate, descriptions serve as retrieval filters, and area indexes provide curated navigation. Decapod's federation and knowledge stores accumulate entries with SQL `LIKE` search and status flags, but there is no maturation path, no compositional linking, no progressive disclosure. A federation node is either active or superseded — there is no equivalent of a seedling growing into a mature note through iterative refinement. The [title-as-claim](../title-as-claim-enables-traversal-as-reasoning.md) convention, which makes note titles work as prose when linked, has no analogue in Decapod's flat-titled knowledge entries.

## Borrowable Ideas

**Proof-plan gating for validation.** The pattern of defining named gates, running external commands, and requiring all gates to pass before a status transition could strengthen our validation. For commonplace, this would mean a `proofs.toml` equivalent that lists structural checks (link resolution, frontmatter validity) as named gates, each with a command and a pass/fail contract. Our [deterministic validation should be a script](../deterministic-validation-should-be-a-script.md) note already identifies this need. Decapod's `ProofDef` structure (name, command, args, required flag) is a clean, borrowable schema. *Ready to borrow.*

**Bounded-time validation contract.** Decapod commits to validation terminating within bounded time and tests this. Our `/validate` skill has no timeout or termination guarantee — a sufficiently large KB could make it hang. Adding a timeout contract (and a test that enforces it) is cheap and valuable. *Ready to borrow.*

**Workspace isolation for multi-agent.** If commonplace ever supports concurrent agents editing the KB, git worktrees scoped to claimed tasks are the right isolation primitive. The branch-must-contain-task-ID convention prevents orphaned branches. *Needs a use case first — we are single-agent.*

**Session-scoped context leases.** The internalization attach/detach model — mount a context artifact for a bounded duration, then explicitly release it — is an interesting pattern for managing which knowledge is "active" in a session. For commonplace, this could mean explicit context activation (load these notes for this session) rather than relying entirely on agent-driven retrieval. *Needs a use case first — progressive disclosure currently works well enough.*

## Curiosity Pass

### Broad pass

**The constitution surface area is staggering.** 120+ governance documents compiled into the binary, covering everything from architecture to security to frontend best practices to emergency protocols. The `docs search` retrieval is pure lexical scoring (term frequency + operation bindings). This means the agent gets keyword-matched fragments from a very large corpus. The effectiveness depends entirely on whether the right document happens to contain the query terms. With 120+ documents, many containing overlapping governance language, the signal-to-noise ratio of retrieved fragments is an open question. Our CLAUDE.md approach — a single routing document that points to deeper content — trades coverage for navigability. Decapod trades navigability for coverage.

**What can proof-gating actually verify?** The proof plan mechanism is genuine: external commands run, exit codes are checked, results are recorded. But the gates are configured by the same agent that does the work. Nothing prevents an agent from setting `proof_plan: ["cargo test"]` when the real verification should include integration tests, security scanning, or manual review. The proof plan is as strong as the agent's judgment about what needs proving. This is an [oracle-strength](../oracle-strength-spectrum.md) question: the mechanism is a hard oracle (exit code 0 or not), but the selection of what to test is a soft oracle at best.

**The aspirational/actual gap is informative.** Decapod's README honestly distinguishes guarantees from aspirations. Multi-agent coordination and deterministic context capsule output are listed as aspirational. In source, the parallel-safety claim is backed only by workspace isolation (separate worktrees), not by database-level locking or conflict resolution. The `DbBroker` in `src/core/broker.rs` wraps SQLite access, but concurrent writes to the same `.decapod/data/` databases from multiple agents in different worktrees could still produce lock contention. The honesty about this gap is valuable — it shows which claims are architecture and which are testing.

### Systematic pass: each Core Idea

**Intent must be explicit before mutation.**
1. *Property claimed:* Intent clarity — the agent cannot proceed without articulating what it will do.
2. *Transform or relocate?* The scaffold generates spec files (markdown) from agent answers (markdown/text). The input is the agent's understanding of the task; the output is the same understanding written into a file with a structured template. The scaffold imposes structure (sections, fields) but does not verify the content. An agent could write "intent: do the thing" and the scaffold would accept it. The mechanism is closer to "require the agent to write something down" than "verify the agent understands the task." This is naming (codification as a label for what is actually structured note-taking), not mechanism — the representation changes format but the content is not validated against the original human request.
3. *Simpler alternative:* A well-written AGENTS.md instruction saying "before starting, write a brief spec in `specs/` with: intent, constraints, acceptance criteria" achieves identical behavior with zero infrastructure. The agent already has the ability to create files. The scaffold adds a CLI surface and file-naming convention but not semantic verification.
4. *Ceiling:* Even working perfectly, scaffold-generated specs cannot verify alignment with human intent — that requires the human to read the spec. The mechanism's ceiling is "agent writes something structured before proceeding." This is valuable (it forces a pause for reflection) but is not the "codification" the README claims.

**Proof-gated completion replaces narrative claims.**
1. *Property claimed:* Verification — VERIFIED means the work actually passed defined checks.
2. *Transform or relocate?* This genuinely transforms the data. The input is "agent says it is done" (narrative). The output is "these specific commands returned exit code 0" (evidence). The proof results are recorded with gate names, statuses, and optional artifact references. The `ensure_verified_ready()` function in `workunit.rs` is a real gate: it checks that every proof_plan entry has a matching "pass" result. This is a hard oracle.
3. *Simpler alternative:* Running `cargo test` before committing achieves the same effect for test-based proofs. The Decapod layer adds: (a) named gates with an audit trail, (b) the requirement that all gates pass before status transition, and (c) provenance recording. Items (a) and (c) are valuable for audit; item (b) is valuable if the agent would otherwise skip tests. The complexity is not pointless — it encodes a workflow constraint.
4. *Ceiling:* The mechanism can verify that configured external commands pass. It cannot verify that the right commands were configured, that the tests are meaningful, or that passing tests implies the work meets human intent. The ceiling is "configured checks passed," which is strictly better than narrative claims but still depends on check quality.

**Workspace isolation prevents protected-branch mutation.**
1. *Property claimed:* Safety — agents cannot corrupt protected branches.
2. *Transform or relocate?* Neither — this is access control, not data transformation. The check is a string comparison against a hardcoded list of branch patterns. It is a genuine interlock.
3. *Simpler alternative:* Git server-side branch protection rules (available on GitHub, GitLab, etc.) achieve the same result without any client-side binary. The Decapod layer adds client-side enforcement (catches violations before push) and worktree provisioning (automates the isolation). For repos without server-side protection, the client-side check adds value.
4. *Ceiling:* Working perfectly, this prevents accidental writes to protected branches. It cannot prevent a determined agent from bypassing the CLI (writing directly, using raw git commands). The mechanism is advisory-with-enforcement, similar to a pre-commit hook.

**Embedded constitution as just-in-time context.**
1. *Property claimed:* Governance compliance — agents receive relevant rules when they need them.
2. *Transform or relocate?* Two layers. The *embedding* is pure relocation — `rust-embed` copies markdown verbatim into the binary with no transformation; `fs::read_to_string()` at runtime would produce identical content. But the *retrieval* is a real operation — it scores and selects fragments from a 120+ document corpus based on the current query, returning only the relevant excerpts rather than the full corpus. This is a crude form of distillation (keyword-based selection, not semantic), but it is genuinely different from `cat`. The embedding adds no value over reading files from disk; the retrieval adds real value by filtering a corpus too large to load entirely.
3. *Simpler alternative:* The conventional software engineering approach — read the constitution files from disk at runtime and run the same scoring/selection over them — produces identical behaviour without compiling content into the binary. The retrieval logic is the valuable part; the embedding is an unnecessary detour. The only benefit of embedding is single-file deployment (no external files to distribute), but the OVERRIDE.md mechanism already reads from disk at runtime, so Decapod doesn't achieve a fully hermetic binary anyway. A secondary cost: in the context of LLM tooling, "embedded" strongly implies vector embeddings or token-level operations, making the mechanism sound more sophisticated than `include_str!()` copying markdown into a const.
4. *Ceiling:* Even with perfect retrieval, the mechanism delivers text that the agent must interpret. Whether the agent follows the governance rules depends on the agent's compliance with its instructions, not on the delivery mechanism. The constitution is advisory in the same way our CLAUDE.md is advisory — the text constrains behavior only insofar as the agent follows instructions.

**Context capsules are hash-verified document excerpts.**
1. *Property claimed:* Integrity — the capsule has not been tampered with since creation.
2. *Transform or relocate?* Relocate with a hash. The input is document excerpts (text). The output is those same excerpts packaged in a JSON structure with a SHA-256 hash. The text content is unchanged. The hash verifies that the package has not been modified, but it does not verify that the content is correct, complete, or relevant.
3. *Simpler alternative:* Git commit hashes already provide tamper-evidence for any file in the repository. A context capsule adds task-scoped binding (this capsule belongs to this task) and a policy binding (risk tier, policy version). The task binding is useful for audit trails. The policy binding is useful if you want to verify that a task was executed under a specific governance version.
4. *Ceiling:* Hash verification can confirm integrity (the bits have not changed). It cannot confirm relevance (these were the right bits to include), completeness (nothing important was omitted), or correctness (the content is accurate). The mechanism is a hard oracle for integrity, not for content quality.

**Internalization turns documents into mountable artifacts.**
1. *Property claimed:* Efficiency — agents stop re-ingesting the same documents every session.
2. *Transform or relocate?* In the current implementation, relocate only. The shipped `noop` profile writes an empty `adapter.bin`. The infrastructure supports external internalizer executables that could transform documents, but none ship. The create/attach/detach lifecycle tracks which documents are "mounted" in which sessions, with source-hash verification to detect stale artifacts. The lifecycle management is real; the "turning documents into context adapters" claim describes future capability, not current behavior.
3. *Simpler alternative:* Caching a document's hash and skipping re-read if unchanged achieves the same efficiency gain (don't re-ingest unchanged documents) without the attach/detach/lease lifecycle. The lease model adds value if you need to know which sessions are using which documents for audit purposes.
4. *Ceiling:* Even with real internalizer profiles, the mechanism can only cache and track document-derived artifacts. Whether those artifacts improve agent performance depends entirely on the internalizer's quality, which is out-of-scope for the governance kernel.

**Federation is a typed knowledge graph.**
1. *Property claimed:* Structured memory — agents can store and retrieve typed knowledge with lifecycle and provenance.
2. *Transform or relocate?* Relocate into SQL. The input is structured data (title, body, type, provenance). The output is rows in SQLite accessed via `LIKE` search. The typing (decision, commitment, etc.) and lifecycle (active/superseded) are genuine structural additions. The provenance tracking (source references) adds audit value.
3. *Simpler alternative:* Markdown files in a directory with YAML frontmatter (our approach) provide the same typing, lifecycle, and provenance with better readability, git versioning, and composability. The SQLite approach adds transactional consistency and faster search over large node counts, at the cost of opacity (you cannot read the knowledge graph by browsing files).
4. *Ceiling:* A typed knowledge graph with SQL `LIKE` search can store and retrieve structured knowledge. It cannot synthesise, connect, or mature knowledge — there is no mechanism for recognising that two nodes are related, that a decision contradicts a commitment, or that an observation should be promoted. The graph has edges but no reasoning over edges.

**Obligation graph tracks dependency-aware work.**
1. *Property claimed:* Coordination — work items form a DAG with derived completion status.
2. *Transform or relocate?* Transform. Status is genuinely derived from dependency satisfaction, proof verification, and commit presence — not asserted. This is a real computation over the graph state.
3. *Simpler alternative:* For single-agent use, a flat task list with manual status tracking suffices. The obligation graph adds value for multi-agent coordination where task dependencies must be enforced across sessions.
4. *Ceiling:* The graph correctly tracks which obligations are met given the defined dependencies and proofs. It cannot determine whether the obligation definitions themselves are correct or complete.

**Validation is a parallel gate runner.**
1. *Property claimed:* Bounded, comprehensive verification of project state.
2. *Transform or relocate?* Transform. Validation computes a structured report from repository state, aggregating pass/fail/warn across 30+ gates.
3. *Simpler alternative:* A shell script running checks sequentially would achieve the same result, slower. The parallelism (rayon) matters for speed at scale; the typed report matters for programmatic consumption. The bounded-time guarantee is enforced by test.
4. *Ceiling:* Deterministic validation can check structural properties (files exist, hashes match, schemas validate). It cannot check semantic properties (is the spec good? does the code match the intent?). Decapod's validation suite is entirely structural, which is the correct scope for a [hard-oracle](../oracle-strength-spectrum.md) system.

### Findings that update Core Ideas and Comparison

The curiosity pass reveals a pattern: Decapod's README and constitution use transformation language (codify, compile, distil) for mechanisms that primarily relocate data between formats without validating or transforming content. The scaffold generates spec files but does not verify specs against intent. Context capsules hash-wrap document excerpts. Internalization creates governance metadata around documents. In each case, the infrastructure is real and well-built, but the claimed property (codification, context adaptation) overstates what the mechanism actually does.

The honest exceptions are the proof-plan gating (genuinely transforms "agent says done" into "configured checks passed"), the obligation graph (genuinely derives status from graph state), and the validation suite (genuinely computes structural correctness). These three mechanisms produce properties the inputs do not have.

For the comparison: Decapod's enforcement model is harder than ours (must pass vs. advisory flags), but both systems share the same ceiling — neither can verify that the agent's work semantically matches human intent. Our system addresses this by keeping humans in the loop (notes mature through human judgment); Decapod addresses it by encoding more process checkpoints (must write spec, must pass tests). These are complementary strategies, not competing ones.

## What to Watch

- Whether the constitution retrieval evolves beyond lexical matching. Vector embeddings or semantic search over the 120+ document corpus would substantially change retrieval quality, moving from keyword-dependent to meaning-dependent context delivery.
- Whether real internalizer profiles ship. The infrastructure is built; the value depends on whether document transformation (not just tracking) materialises.
- Whether the multi-agent coordination moves from aspirational to tested. The workspace isolation is real, but concurrent database access under contention is the hard problem.
- How the federation graph evolves relative to their knowledge store — they have two overlapping storage systems (federation for typed graph, knowledge for text entries) with different APIs and no clear delineation of when to use which.

---

Relevant Notes:

- [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md) — Decapod's proof-gated model is a production implementation of the pattern this note argues for: named gates, external commands, pass/fail contracts
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — Decapod's proof mechanism is a hard oracle (exit codes), but proof-plan selection is a soft oracle; the system demonstrates that oracle strength depends on which question you ask, not just which mechanism you use
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Decapod's just-in-time constitution delivery and context capsules are responses to context scarcity, choosing selective retrieval over progressive disclosure
- [agents-md-should-be-organized-as-a-control-plane](../agents-md-should-be-organized-as-a-control-plane.md) — Decapod's AGENTS.md is a full control-plane contract; contrast with our AGENTS.md as routing table
- [codification](../codification.md) — Decapod claims codification (turning intent into specs, documents into adapters) but source inspection shows most mechanisms relocate rather than transform; the honest exceptions (proof gating, obligation status derivation) are genuine codification
- [agentic-systems-interpret-underspecified-instructions](../agentic-systems-interpret-underspecified-instructions.md) — Decapod's constitution and scaffold attempt to reduce underspecification, but the constitution is itself natural language interpreted by the agent; only the hard gates (workspace interlock, proof gating) escape the underspecification problem
- [automated-tests-for-text](../automated-tests-for-text.md) — Decapod's validation suite is a production example of the deterministic test layer this note describes, with 30+ parallel structural checks
- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: Decapod adds a governance-first position (process control over knowledge management) not represented in existing entries

Topics:

- [related-systems-index](./related-systems-index.md)
