---
description: BFT-branded agent memory with CometBFT consensus, Ed25519 signing, application-level validators, confidence decay, and encryption — consensus is ceremony in single-node mode; real value is the validation gate pattern and domain-scoped RBAC
type: note
tags: [related-systems]
traits: [has-comparison, has-external-sources]
status: current
last-checked: 2026-03-12
---

# SAGE (Sovereign Agent Governed Experience)

SAGE ([l33tdawg/sage](https://github.com/l33tdawg/sage)) is an open-source agent memory system by Dhillon Andrew Kannabhiran that frames persistent agent memory as a consensus-validated infrastructure problem. It wraps a Go state machine around CometBFT (the consensus engine behind Cosmos), Ed25519 transaction signing, and four application-level validators that gate every memory write. Storage is SQLite (personal mode) or PostgreSQL + pgvector (multi-node), with optional AES-256-GCM encryption at rest. Exposes memory operations via MCP tools and REST API. Apache 2.0 licensed.

**Repository:** https://github.com/l33tdawg/sage

## Core Ideas

**Memory writes are transactions, not inserts.** Every `sage_remember` call creates a signed transaction (protobuf-encoded, Ed25519-signed with timestamp-based replay protection) that gets broadcast to CometBFT. The transaction enters a block, gets processed by the ABCI state machine, and only then writes to storage. This means every write has a verifiable provenance chain: agent identity → signed tx → block height → committed state. The transaction overhead buys auditability — you can trace every memory to who wrote it and when it was accepted.

**Four application validators gate every write.** In personal mode (the typical deployment), four in-process validators independently evaluate each proposed memory and cast vote transactions: **Sentinel** (baseline accept, ensures liveness), **Dedup** (rejects duplicate content by SHA-256 hash), **Quality** (rejects greeting noise, short content, empty headers), **Consistency** (enforces confidence thresholds, required fields). Quorum requires 3/4 accept. This is a validation pipeline with a vote-counting interface, not a consensus protocol — but the pattern of multiple independent checks with quorum is sound.

**Confidence decays domain-specifically over time.** Each memory carries a confidence score (0–1) that decays exponentially per domain: crypto knowledge at 0.001/day (693-day half-life), vulnerability intel at 0.01/day (69-day half-life), default at 0.005/day (138-day half-life). Corroborations boost confidence logarithmically. Decay is computed at query time, not stored — the database holds initial confidence and corroboration count. Open tasks are exempt from decay. This models the intuition that different knowledge types age at different rates.

**Memories have a lifecycle beyond store-and-retrieve.** The status progression is proposed → committed → challenged/deprecated. Agents can corroborate (increase confidence) or dispute (trigger review) existing memories. This lifecycle is richer than most memory systems which treat storage as final. The challenge/corroborate mechanism creates a feedback loop where memories can be refined post-storage.

**Domain-scoped RBAC with clearance levels.** The Sovereign layer adds organizations, departments, and per-agent clearance (0=none through 4=admin) with domain-level read/write permissions. Agent identity is on-chain (v3.5+) — registration, permission changes, and visibility rules go through CometBFT transactions. This is the most structured access control among reviewed memory systems.

**Encryption at rest is real, not ceremony.** The vault layer uses AES-256-GCM with Argon2id key derivation (OWASP parameters). A random 32-byte data key encrypts content and embeddings; the data key itself is encrypted with a passphrase-derived key. Content is stored as `enc::{base64(nonce+ciphertext)}`. Passphrase change re-encrypts only the key file, not the entire database. This is competent cryptographic engineering.

**MCP tools mediate all agent interaction.** The tool surface includes `sage_remember` (store), `sage_recall` (semantic search), `sage_forget` (deprecate), `sage_turn` (atomic recall-then-store per conversation turn), `sage_reflect` (not the agentic loop Hindsight has — just a recall variant), `sage_task` (task management with non-decaying status), and `sage_inception` (boot sequence). The `sage_turn` tool is notable: it combines recall and store in a single atomic operation, reducing round trips.

## Comparison with Our System

| Dimension | SAGE | Commonplace |
|---|---|---|
| Storage substrate | SQLite + BadgerDB (personal) or PostgreSQL + pgvector (multi-node); memories are signed database records | Filesystem-first; notes are markdown files under version control |
| Write path | Transaction pipeline: sign → broadcast → validate → commit; LLM not required | Human writes markdown; zero infrastructure required |
| Validation | Application validators (dedup, quality, consistency) with quorum gate | Type system + structural validation (`/validate`) + semantic review |
| Memory taxonomy | fact / observation / inference / task (flat enum) | note / structured-claim / adr / index / related-system (typed with templates) |
| Retrieval | Embedding similarity via pgvector/Ollama; single-strategy | `rg` keyword search + description scanning + area filtering |
| Access control | Clearance levels + domain-scoped RBAC + agent identity on-chain | Filesystem permissions; no agent-level access control |
| Inspectability | Requires API, UI, or SQL to browse; encrypted content doubly opaque | Fully inspectable — every note is a readable file |
| Linking | No explicit links between memories; relies on embedding proximity | Standard markdown links with explicit relationship semantics |
| Consolidation | None — no mechanism to synthesize or abstract across memories | Manual — human writes notes, `/connect` discovers relationships |
| Provenance | Cryptographic: Ed25519 signed transactions with block height | Git: version control with commit history |

**Where SAGE is stronger.** Access control. The RBAC layer with clearance levels, domain scoping, and on-chain identity is real infrastructure — it solves a problem commonplace doesn't address at all. The validation gate pattern (multiple independent checks with quorum before storage) catches low-quality input that our system relies on human judgment to filter. Confidence decay models temporal relevance without manual status updates.

**Where commonplace is stronger.** Knowledge structure. SAGE stores flat text blobs with a type enum and domain tag. There are no links between memories, no consolidation, no hierarchy, no explicit relationships. Retrieval is embedding-only — there's no way to traverse from one memory to related memories except through vector similarity. Our type system, link semantics, and index structure provide compositional knowledge that SAGE's storage model can't represent.

**The fundamental trade-off.** SAGE invests in the write gate (validation, signing, consensus machinery) at the expense of knowledge structure. Commonplace invests in knowledge structure (types, links, indexes, methodology) at the expense of write-path infrastructure. SAGE ensures what gets stored is signed, deduplicated, and quality-gated; commonplace ensures what gets stored is connected, compositional, and inspectable.

## Borrowable Ideas

**Validation gate before storage** — the pattern of running multiple independent checks with quorum before accepting a write is sound regardless of the consensus framing. We could apply this to note validation: run structural check, link health check, description quality check, and require all to pass before a note is considered complete. *Ready to borrow* — `/validate` already does some of this; the multi-check-with-quorum framing would make it more systematic.

**Domain-specific confidence decay** — modeling that vulnerability intel ages faster than cryptographic knowledge is a useful heuristic. Our `status` field (current/outdated/speculative) is set manually; deriving staleness from content domain could automate part of this. *Needs a use case first* — our notes don't carry creation timestamps in frontmatter, and the domain-to-decay-rate mapping would need to be defined for our areas.

**Atomic recall-then-store operation** — `sage_turn` combines reading relevant memories and storing new ones in a single tool call, reducing the agent's coordination burden. If we ever build agent-facing memory tools (beyond the current human+agent workflow), this compound operation is the right primitive. *Needs a use case first* — requires an agent-operated write path we don't have.

**Pre-validation dry run** — the `pre-validate` endpoint runs all validators without committing. This lets agents check whether a memory would pass before submitting it. Applying this to note writing: a "dry-run `/validate`" that reports issues before the note is connected and committed would reduce rework. *Ready to borrow.*

## Curiosity Pass

**What property does "BFT consensus" claim to produce?** Tamper resistance and Byzantine fault tolerance — the system should continue operating correctly even if some nodes are malicious. In personal mode (single binary, 4 in-process validators), this property is vacuous: all four validators run as goroutines in the same process, with deterministic keys derived from the same node seed. There is no Byzantine fault to tolerate because there is no independent party to be Byzantine. The validators can't disagree with each other in any meaningful sense — they're running predefined logic (accept, check hash, check length, check fields) in the same address space. Calling this "BFT consensus" is naming, not mechanism.

**Does the consensus mechanism transform data or just relocate it?** The CometBFT layer takes a memory submission and produces... the same memory, stored in SQLite/Postgres, with a block height attached. The transaction signing and block inclusion add provenance metadata (who signed it, which block), but the memory content is unchanged. The application validators do transform in a narrow sense — they reject low-quality input — but the accepted memories pass through unmodified. The consensus machinery relocates (memory → signed transaction → block → database row) without transforming. The validation pipeline is the real value; the consensus wrapper around it is overhead.

**What's the simpler alternative?** A write-path validation pipeline (dedup check, quality check, field validation) with a simple pass/fail gate, plus Ed25519 signing for provenance, achieves identical behavior to personal-mode SAGE without CometBFT, BadgerDB, block production, or the vote-transaction dance. The multi-node deployment is where CometBFT earns its keep — but the README and marketing focus on personal mode, where it doesn't.

**What could this mechanism actually achieve, even if it works perfectly?** In multi-node mode with genuinely independent validators operated by different parties, BFT consensus would provide tamper-evident memory: no single party could unilaterally insert or modify memories. This is a real property for multi-agent systems with trust boundaries. But the application validators (sentinel, dedup, quality, consistency) are deterministic code — they can't catch semantic errors, lies, or subtly wrong information. The quality gate catches syntactic noise (short content, missing fields) but not epistemic noise (confident-sounding wrong claims). The system validates form, not truth.

**The Proof of Experience (PoE) weight system.** Agents accumulate weight through an EWMA (exponentially weighted moving average) scoring system that factors in domain expertise and validation accuracy. Higher-weight agents' votes count more. This creates an interesting feedback loop: agents who propose memories that get committed gain influence over future commitments. In practice, with 4 in-process validators that always vote the same way, the weighting has no effect. In multi-agent deployments, it could create path-dependent authority — early agents who happen to accumulate weight become gatekeepers for later agents. Whether this is desirable depends on the trust model.

**The research papers.** Four papers accompany the code, claiming benchmark results (50-vs-50 study, rho=0.716 correlation). The papers were not independently peer-reviewed; they're self-published. The benchmark methodology (memory agents vs memoryless agents) tests whether memory helps at all, not whether SAGE's specific architecture helps more than simpler alternatives. The comparison isn't SAGE vs. vector-database-with-validation; it's SAGE vs. no memory. This is a low bar.

## What to Watch

- **Does multi-node deployment find real users?** The consensus architecture only earns its complexity in multi-agent, multi-party deployments with genuine trust boundaries. If SAGE remains primarily a personal-mode tool, the BFT layer is pure overhead.
- **Will the validation pipeline evolve beyond syntactic checks?** The current validators catch duplicates, short content, and missing fields. Semantic validation (contradiction detection, factual consistency) would be genuinely valuable but requires LLM calls — which SAGE currently avoids on the write path.
- **Enterprise adoption of the RBAC layer.** The clearance/domain/visibility model is well-designed for organizational use. If enterprise teams adopt SAGE for shared agent memory, the access control infrastructure becomes the primary value proposition, not the consensus layer.

---

Relevant Notes:

- [inspectable substrate not supervision defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — SAGE's storage is opaque without API mediation; its supervision model (validators, signed transactions, audit trail) is the alternative to inspectable substrate
- [distillation](../distillation.md) — SAGE has no distillation mechanism; memories are stored as-is, never extracted or compressed into higher-order knowledge
- [constraining and distillation both trade generality for reliability speed and cost](../constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — SAGE's validation pipeline constrains (rejects low-quality input) but the system has no distillation arm; one-sided constraining without knowledge synthesis
- [ephemeral computation prevents accumulation](../ephemeral-computation-prevents-accumulation.md) — SAGE is maximally anti-ephemeral: every agent interaction produces a signed, stored, consensus-validated record; but without consolidation, the accumulation is flat (facts pile up, never synthesized)
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) — SAGE's validators are hand-coded policy (deterministic checks), not learned; the system has no mechanism to improve its acceptance criteria from experience
- [claw learning is broader than retrieval](../claw-learning-is-broader-than-retrieval.md) — SAGE addresses storage and retrieval but not the broader action-capacity loop; no mechanism for preferences, procedures, or judgment precedents
- [three-space agent memory maps to Tulving taxonomy](../three-space-agent-memory-maps-to-tulving-taxonomy.md) — SAGE's four memory types (fact, observation, inference, task) are a flat enum, not a structural separation; memories of all types share the same store, retrieval path, and lifecycle

`#related-systems` `#memory-architecture`
