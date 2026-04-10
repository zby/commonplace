---
description: Hash-chained semantic memory ledger with binary append-only storage, additive ranked retrieval, and a diff-based signed skill registry exposed over MCP and REST
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-07"
---

# MentisDB

MentisDB is a Rust memory service by CloudLLM that treats durable agent memory as an append-only ledger plus a separate versioned skill registry. The repo ships a core crate, the `mentisdbd` daemon, HTTP MCP and REST surfaces, a dashboard, benchmark scripts, and a built-in operating skill for client bootstrap. The implementation is real and fairly broad: typed thought records, hash-chain integrity checks, per-chain agent registries with public keys, append-order and graph-aware retrieval, optional vector sidecars, and immutable skill version history all exist in code.

**Repository:** https://github.com/cloudllm-ai/mentisdb

## Core Ideas

**The canonical memory substrate is a typed append-only ledger, not a document collection.** `src/lib.rs` defines a `Thought` record with semantic type, role, tags, concepts, refs, typed relations, `prev_hash`, and `hash`, then persists it through a `StorageAdapter` abstraction. In practice the active path is much narrower than the abstraction sounds: new chains are binary-only (`StorageAdapterKind::Binary`), while JSONL remains read-only legacy input for migration. This makes MentisDB a service-shaped memory log with strong ordering and integrity semantics, not a file-native knowledge base.

**Shared-agent provenance is handled through a side registry rather than duplicated on every record.** Thoughts carry stable `agent_id`s, while display names, owners, aliases, descriptions, statuses, and Ed25519 public keys live in a per-chain agent registry. That is a good space-saving and governance move: the chain stays compact while identity metadata can evolve independently. It also means multi-agent sharing is genuinely implemented, but the registry solves attribution and key management more than it solves coordination or conflict resolution.

**Retrieval is deliberately layered so the deterministic baseline stays simple.** The repo keeps plain `ThoughtQuery` semantics filter-first and append-order, then adds ranked lexical search, optional graph expansion over refs and typed relations, and optional vector-sidecar similarity on top. This is a more disciplined search story than most memory systems: the baseline stays explainable while richer retrieval is explicit rather than silently changing the meaning of a basic query. The cost is that "semantic memory" is partly opt-in infrastructure. Without relations or sidecars, much of the semantic pitch collapses back to filtered text search over typed records.

**The skill registry is a distinct immutable artifact store, and it is more mature than the memory-learning story.** `src/skills.rs` implements upload, search, read, deprecate, revoke, and version history over structured Markdown or JSON skill documents. The first version is stored in full; later versions are stored as unified diffs and reconstructed forward. This is one of the repo's strongest mechanisms because it gives agent instructions a durable lifecycle rather than treating them as ephemeral prompts. It is also where the provenance model is strongest: when an agent has registered keys, skill uploads must include a valid detached Ed25519 signature.

**The trust story is uneven: skill provenance is enforced, thought provenance is mostly prepared.** The schema supports `signing_key_id` and `thought_signature` on thoughts, and the MCP/REST append surfaces accept them, but the append path stores those fields without server-side signature verification. By contrast, skill uploads explicitly verify signatures against active registered keys before acceptance. So MentisDB really does implement cryptographic provenance for skills, but for thoughts it currently provides tamper-evident chain integrity plus optional signature carriage, not end-to-end authenticated authorship.

## Comparison with Our System

| Dimension | MentisDB | Commonplace |
|---|---|---|
| Canonical substrate | Binary append-only thought chain with hashes and service APIs | Markdown files in git |
| Knowledge unit | Small typed thought record | Typed notes, instructions, indexes, reviews |
| Relationship model | `refs` plus typed relations between thought IDs | Markdown links with explicit relationship phrases in prose |
| Inspectability | Code and exports are inspectable; canonical store is opaque binary plus sidecars | Canonical artifacts are directly readable and editable |
| Retrieval model | Filter-first baseline with additive lexical, graph, and optional vector ranking | Search, descriptions, indexes, and authored link traversal |
| Governance | Integrity checks, agent registry, key registry, signed skill uploads | Review/validation workflows and inspectable artifact history |
| Knowledge evolution | Append more thoughts; update skills through immutable versions | Write, revise, connect, promote, reclassify, and curate notes |
| Integration surface | Library crate, daemon, MCP, REST, dashboard, setup wizard | Repo-native KB inside an agent harness |

MentisDB is stronger where a shared runtime memory service matters more than authored semantic structure. It gives multiple agents one durable chain, lets outside tools access it through MCP/REST, and adds a real lifecycle for reusable skills. Commonplace is stronger where the artifact itself must remain the inspectable substrate: notes can be read, linked, reviewed, and revised directly, while MentisDB's knowledge mostly becomes visible only through exported prompts, markdown projections, or API calls.

The deepest difference is what each system thinks memory is for. MentisDB treats memory as an auditable operational ledger: a place to preserve durable checkpoints, decisions, and lessons across sessions and agents. Commonplace treats knowledge as a curated document graph whose structure should itself be the object of navigation and refinement. MentisDB optimizes continuity and tool-neutral access. Commonplace optimizes discoverability, composability, and inspectable maturation.

## Borrowable Ideas

**Keep richer retrieval additive instead of mutating the baseline semantics.** MentisDB's separation between deterministic filtering and ranked/vector/graph overlays is a good design discipline. If commonplace adds more retrieval infrastructure, preserving one simple predictable baseline would reduce accidental complexity. Ready to borrow now as a design rule.

**Treat agent identity as its own durable object.** The per-chain agent registry is cleaner than smearing identity details across every memory write. Commonplace does not need a full registry today, but explicit agent metadata with aliases, ownership, and status could become useful if more cross-agent workflows land. Needs a concrete multi-agent use case first.

**Version reusable instructions as first-class artifacts with lifecycle states.** The skill registry's active/deprecated/revoked states and immutable history are strong. Commonplace already has instructions and skills in files, but the lifecycle vocabulary is thinner. A lightweight version of this status model could improve how we retire or replace operational guidance. Ready to borrow now for governance framing.

**Bootstrap clients through an embedded operating skill rather than prose setup docs alone.** MentisDB uses MCP handshake instructions to point clients at a built-in skill document. That is a practical packaging idea: ship the minimum operational guidance inside the service boundary so client bootstrap does not depend on a human reading a README first. Needs a use case first.

**Separate canonical state from rebuildable retrieval sidecars.** MentisDB's vector sidecars are explicitly derived and rebuildable from the chain log. That is a strong pattern for any future commonplace operational layer: keep expensive search indexes derived and disposable instead of letting them become the source of truth. Ready to borrow now as an architectural principle.

## Curiosity Pass

**"Session resurrection" is implemented as recent-tail formatting, not deep state reconstruction.** The claimed property is immediate exact resumption. Mechanistically, `recent_context` returns `to_catchup_prompt(last_n)`, which formats the last N thoughts into a short prompt block. The simpler alternative is "show the last few events." That is basically what the implementation does today. It is useful, but it is not a richer reconstruction mechanism than the README language suggests.

**The ledger gives integrity, not curation.** Hash chaining proves append order and tamper evidence; it does not decide which thoughts remain current, contradictory, superseded, or load-bearing. MentisDB partly addresses this with relation kinds like `Corrects`, `Invalidates`, and `Supersedes`, but the dominant maintenance path is still accumulation. The simpler alternative is a mutable knowledge artifact that directly reflects the current view. MentisDB intentionally rejects that, so its strongest claim is auditability of memory history, not refinement of knowledge state.

**The storage-abstraction framing currently overstates backend flexibility.** The property is swappable persistence. The code really does have a `StorageAdapter` trait, but active usage is effectively binary-first: new JSONL chains are rejected, and JSONL survives only as migration input. The simpler alternative would be to say "binary-backed ledger with migration support." That narrower claim is closer to the current implementation than "storage-agnostic memory engine."

**Cryptographic provenance is uneven across artifact types.** The property is verifiable authorship. For skills, the mechanism is real: active keys force signature checks before upload. For thoughts, the server accepts `signing_key_id` and `thought_signature` fields but does not verify them on append. The simpler alternative is to describe thought signing as future-facing schema support. That would better match the implementation and avoid implying a uniform trust boundary that does not yet exist.

**The repo's strongest learning mechanism is skill revision, not trace mining.** README language about self-improving fleets suggests the system learns by accumulating work and improving instructions over time. That can happen socially through agent behavior, but the inspected code does not automatically mine session logs or task traces into promoted skills or weights. The implemented mechanism is a durable place to store improved skills once an agent decides to upload them. That matters because it places MentisDB closer to infrastructure for learning systems than to a trace-derived learning system itself.

## What to Watch

- Whether thought writes gain the same signature verification path that skill uploads already have, which would make the provenance model materially more coherent.
- Whether the append-only memory layer develops stronger current-state mechanisms beyond relation labels and tail summaries, or remains primarily an auditable log.
- Whether the vector-sidecar and graph-expansion layers become common in production usage or stay optional performance add-ons around a simpler lexical baseline.
- Whether the system's real long-term center of gravity becomes the skill registry rather than the thought ledger, since the skill lifecycle is currently the clearest compounding mechanism in the repo.
- Whether MentisDB adds real trace-to-artifact promotion rather than only providing the substrate where agents can manually store lessons and revised skills.

---

Relevant Notes:

- [files-not-database](../files-not-database.md) — contrasts: MentisDB makes a binary ledger plus service layer the source of truth where commonplace keeps primary knowledge in editable files
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — contrasts: MentisDB keeps code and exports inspectable, but the canonical memory substrate itself is opaque without its own tooling
- [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels](../agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — sharpens: shared memory is a coordination channel, but MentisDB adds attribution and integrity more than semantic conflict resolution
- [mcp-bundles-stateless-tools-with-stateful-runtime](../mcp-bundles-stateless-tools-with-stateful-runtime.md) — exemplifies: MentisDB is an explicit case where MCP fronts a genuinely stateful runtime rather than a stateless file operation bundle
- [storing-llm-outputs-is-constraining](../storing-llm-outputs-is-constraining.md) — extends: the append-only ledger constrains writes structurally by making accumulation cheap and overwrite impossible
- [trace-derived-learning-techniques-in-related-systems](../trace-derived-learning-techniques-in-related-systems.md) — boundary: MentisDB stores durable thoughts and revised skills, but the inspected repo does not automatically mine live traces into promoted artifacts or weights
