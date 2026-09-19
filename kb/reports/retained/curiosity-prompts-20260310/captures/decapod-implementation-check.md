# Decapod: Does the implementation match the impressive claims?

The [original report](./decapod-original.md) makes several claims that sound hard to actually build. I checked the source at `related-systems/decapod/` against the five most impressive ones.

## 1. Proof-gated completion (Claimed -> Verified only if proof plan passes)

**Claim:** Work units progress through Draft -> Executing -> Claimed -> Verified, but the Verified transition only fires if a proof plan passes.

**What the code actually does:** This is real, and it is enforced at multiple layers.

The workunit state machine in `src/core/workunit.rs` defines explicit transition guards. `ensure_verified_ready()` (line 262) checks two things: that `proof_plan` is non-empty, and that every gate in the proof plan has a corresponding passing result in `proof_results`. If either fails, the transition to Verified is rejected with a hard error.

What makes this genuinely enforced rather than advisory: the same check runs in *three* independent locations:
- At transition time (`transition_status` in `workunit.rs`)
- During `decapod validate` (in `validate.rs`, line 1846)
- At publish time (`verify_workunit_gate_for_publish` in `workspace.rs`, line 984)

And there are integration tests proving each path (`tests/workunit_publish_gate.rs`).

**The gap:** The proof plan is an *honor system* between the agent and the control plane. The agent sets the proof plan (`set_proof_plan`), runs proofs externally, then manually records results (`record_proof_result`). There is no automatic connection between `run_proofs()` (which reads `proofs.toml` and actually executes commands) and the workunit's proof results. The agent has to bridge them. This means the agent defines what counts as proof, runs the proof, and reports whether it passed -- all the same actor. The gate enforces that *some* proof was recorded, but cannot enforce that the recorded proof corresponds to an actual execution. The `ProofExec` capability does restrict which binaries can be invoked, adding a layer of control, but the attestation chain from "proof ran" to "workunit records pass" has an agent-mediated gap.

**Verdict:** The state machine enforcement is real and multi-layered. The integrity of the proof results themselves depends on trusting the agent to faithfully report what happened.

## 2. Over 200 governance documents compiled into the binary

**Claim:** Over 200 governance documents are compiled into the binary.

**What the code actually does:** The `constitution/` directory contains **94 markdown files**. The `embedded_docs!` macro in `src/core/assets.rs` uses `include_str!` to bake a subset -- roughly **66 documents** -- directly into the binary at compile time via Rust's compile-time file inclusion. This is genuinely compiled in; no external files are needed at runtime.

Not all 94 constitution files are embedded. Some (like `constitution/architecture/UI.md`, `constitution/core/EMERGENCY_PROTOCOL.md`, several interface docs) exist on disk but are not listed in the `embedded_docs!` macro, so they are not in the binary.

**Verdict:** The embedding mechanism is real and uses a sound approach (`include_str!` is a standard Rust compile-time embed). But the count is inflated by roughly 3x. The actual number is 66 embedded, 94 on disk -- not "over 200."

## 3. Typed federation graph with immutable critical nodes and event sourcing

**Claim:** Knowledge is represented as typed nodes connected by typed edges. Critical types (Decision, Commitment) are immutable after creation. All mutations are event-sourced in append-only `.jsonl` logs.

**What the code actually does:** This is the claim that holds up best.

The federation module (`src/plugins/federation.rs`) implements a typed graph stored in SQLite with 8 node types and 4 edge types, exactly as described. The immutability enforcement for critical nodes is implemented in `edit_node()` (around line 688): before allowing any edit, it checks `is_critical(&nt, &pri)` and returns a hard error: "Cannot edit critical node ... Use 'supersede' instead." Critical means either the node type is `decision` or `commitment`, or its priority is `critical`.

The event sourcing is dual-written: every mutation (add, edit, supersede, deprecate, link, unlink) writes both to SQLite and appends a structured JSON event to `federation.events.jsonl`. There is even a `Rebuild` command that can reconstruct the SQLite database deterministically from the event log.

The provenance gating is also real: critical nodes *require* at least one provenance source at creation time, validated against a scheme regex (`file:`, `url:`, `cmd:`, `commit:`, `event:`).

**Verdict:** Matches the claims accurately. The immutability, event sourcing, provenance gating, and supersession chains are all implemented as described.

## 4. Content-addressed artifacts for drift detection

**Claim:** Hashing specifications and proof artifacts means any change is detectable.

**What the code actually does:** Content addressing is used pervasively but in different subsystems:

- **Work unit manifests** (`workunit.rs`): canonicalized and SHA-256 hashed via `canonical_hash_hex()`.
- **Context capsules** (`context_capsule.rs`): each capsule excludes the hash field from its canonical representation, computes SHA-256 over the canonical JSON, and stores the hash. The publish gate (`verify_capsule_policy_lineage_for_task`) re-derives the hash and compares it to the stored value -- real tamper detection.
- **Internalization artifacts** (`internalize.rs`): the source file is hashed at creation time, and on inspect/attach the hash is re-verified against the file on disk. If the file changed, attach is refused with `SourceIntegrityFailed`.
- **RPC receipts** (`rpc.rs`): every response includes SHA-256 hashes of both inputs and outputs.

**Verdict:** Real and thorough. The content addressing is not a single feature but a pattern applied across multiple subsystems. The most impressive part is how the publish gate chains it: you cannot publish a workunit unless the context capsule it references is present, unmodified, and bound to the correct task.

## 5. Internalization subsystem (distillation with determinism classification)

**Claim:** A subsystem that turns large documents into mountable compressed artifacts, with a determinism classification distinguishing replayable from best-effort artifacts.

**What the code actually does:** `src/plugins/internalize.rs` is a ~1180-line module implementing the full lifecycle: `create`, `attach` (with session-scoped leases), `detach`, and `inspect`.

The determinism classification exists: `DeterminismClass::Deterministic` vs `DeterminismClass::BestEffort`, and `ReplayClass::Replayable` vs `NonReplayable`. The logic connecting them is in `build_replay_recipe()` -- a deterministic profile with a pinned binary hash is considered replayable; a best-effort profile or one missing a binary hash is not.

The only production-ready internalizer profile is `noop` -- it writes an empty `adapter.bin` and returns immediately. Real internalization requires an external executable that the profile configuration points to. The system explicitly rejects non-local sources: "MVP only supports local file sources; URL and stdin sources are intentionally not implemented."

The session-scoped mount lease system is fully implemented -- artifacts are attached to sessions with TTL, and the attach checks integrity (source hash, adapter hash, expiry, tool permissions, replayability claims) before granting a lease.

**Verdict:** The governance infrastructure is complete and impressive. The actual "turning a large document into a compressed artifact" part is a no-op in the default profile. The system provides the provenance, lifecycle, and integrity layer, but delegates the actual distillation work to an external binary that does not ship with Decapod. This is more of a framework for governing internalization than a working distillation pipeline.

## Overall pattern

The report's claims are directionally accurate but systematically generous on three axes:

1. **Counts are inflated** -- 94 constitution files, not "over 200"; ~66 embedded, not all of them.
2. **Agent mediation gaps are omitted** -- the proof gate enforces that proof results exist but cannot verify the agent faithfully recorded actual execution outcomes.
3. **Framework vs. implementation** -- the internalization subsystem has thorough governance infrastructure but the actual "turn docs into artifacts" step is an external binary that doesn't ship.

The federation graph is the strongest feature: immutability enforcement, event sourcing, provenance gating, and supersession chains all work as advertised. The proof-gated completion is the second strongest, with the caveat that the chain of custody has an agent-trust gap. The content-addressing pattern is pervasive and well-integrated. The constitution embedding is real but smaller than claimed.
