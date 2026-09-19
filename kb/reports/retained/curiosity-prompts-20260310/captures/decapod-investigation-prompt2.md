# Decapod Investigation: Unusual Choices and Cost/Benefit Analysis

Prompt: "What choices seem unusual -- where the cost/benefit isn't obvious? Follow your curiosity and investigate mechanistically."

## 1. The "Compiled Constitution" Is Just `include_str!()`

**The claim (from the report):** "Over 200 governance documents are compiled into the binary. Agents fetch relevant slices via context capsules rather than reading files directly. This is constraining taken to its logical conclusion -- the methodology is codified into the binary, not interpreted from instructions. No agent can drift from it because it cannot be edited at runtime."

**What's unusual:** Compiling documents into a binary sounds like a heavy architectural commitment -- you lose the ability to update methodology without rebuilding, you inflate binary size, and you get coupling between content and release cycles. The payoff is supposed to be "zero interpretive variance" and "codification."

**What the code actually does:** In `src/core/assets.rs`, the mechanism is a macro:

```rust
macro_rules! embedded_docs {
    ($($path:expr => $const_name:ident),* $(,)?) => {
        $(
            pub const $const_name: &str =
                include_str!(concat!("../../constitution/", $path));
        )*
```

`include_str!()` is a Rust compile-time macro that copies the file contents verbatim into the binary as a string constant. No transformation, no compilation, no parsing, no codification. The markdown is carried as-is. At runtime, `get_embedded_doc()` returns the raw string. The `docs.rs` module then does lexical keyword matching against these strings to find relevant fragments.

Furthermore, the system explicitly supports runtime overrides. `get_merged_doc()` in `assets.rs` checks for a `.decapod/OVERRIDE.md` file and merges its contents into the embedded document. So "no agent can drift from it" is incorrect -- the override mechanism exists precisely to allow runtime modification.

**The real cost/benefit:** The cost (binary-size inflation, rebuild-to-update, no runtime adaptation) is being paid. But the benefit (true codification, zero interpretive variance) is not being received. The documents are still raw markdown that agents interpret just as they would from files. The `include_str!()` approach is functionally equivalent to reading files from a known path at runtime, with the single operational benefit of not requiring the constitution directory to be present on disk. This is a deployment convenience, not a semantic guarantee.

## 2. Hand-Rolled CBOR Encoding in `state_commit.rs`

**What's unusual:** The state commit module (`src/core/state_commit.rs`) contains a hand-rolled partial CBOR encoder -- `encode_uint`, `encode_string`, `encode_bool`, `encode_array`, `encode_map` -- used to produce deterministic binary representations of file state for Merkle root computation.

This is a surprising choice because:
- Rust has well-maintained CBOR libraries (`ciborium`, `serde_cbor`) that handle encoding correctly.
- Hand-rolling encoding is error-prone (note the `panic!("uint too large")` for values >= 65536, and `panic!("string too long")` for strings >= 256 bytes, meaning the system will crash on moderately large file paths).
- The stated purpose (deterministic encoding for content-addressing) is valid, but canonical CBOR (RFC 8949 Section 4.2) is a well-defined standard that libraries implement.

**Why it might exist:** Deterministic serialization is genuinely important for content-addressing. `serde_json::to_vec` doesn't guarantee stable ordering. The hand-rolled CBOR avoids pulling in a dependency and gives exact control over byte output. But the implementation has hard limits that would break on real repositories (256-byte path length limit, 65536-item limit).

## 3. The Obligation System's "Derived, Never Asserted" Status -- With a Writable Status Column

**The claim:** The obligation module's header comment states: "KEY PRINCIPLE: Completion is DERIVED, never asserted. Status is computed from: dependencies satisfied, proofs verified, state_commit present. No user-settable status field - status is always derived."

**What the code does:** The `ObligationNode` struct has a `status: ObligationStatus` field. The database schema stores it. The `add_obligation` function writes `status: "open"` at creation. The `derive_obligation_status` function computes what the status should be from the obligation's dependencies, proofs, and commit state. But this computed status is never written back -- `derive_obligation_status` returns a validation result but doesn't update the database. The stored `status` column just sits there holding its initial value.

This means: there are two sources of truth. The stored `status` field (always "open" unless manually changed), and the derived status (computed on demand). The code that lists obligations returns the stored status. The code that verifies obligations returns the derived status. There's no reconciliation. If you ask "list my obligations" you get one answer; if you ask "verify obligation X" you may get a different one. The "derived, never asserted" principle is aspirational -- the code has the assertion mechanism (the stored field) but doesn't use the derivation to update it.

## 4. Two-Phase Audit Logging in the Broker: Pending Without Recovery

**What's unusual:** The `DbBroker` in `src/core/broker.rs` implements two-phase audit logging for write operations. It logs a "pending" event before the write, executes the write, then logs "success" or "error" after. There's a `verify_replay` method that scans the log for pending events without terminal status, which indicates a crash between the two phases.

But `verify_replay` is purely diagnostic -- it reports divergences but doesn't repair them. There's no WAL, no redo log, no compensating action. The two-phase pattern creates the appearance of crash recovery infrastructure without providing actual crash recovery. The underlying SQLite already has its own WAL and ACID guarantees, so the broker's two-phase logging is redundant for data integrity and insufficient for application-level recovery.

The matching logic in `verify_replay` is also fragile: it matches pending events to terminal events by `intent_ref + op + db_id`, but if two operations share the same intent_ref and op targeting the same database (not uncommon), one success could clear a different pending event.

## 5. The Internalization Subsystem: Full Lifecycle for a `noop` Profile

**What's unusual:** The internalize plugin (`src/plugins/internalize.rs`) implements a complete lifecycle for converting documents into "mountable, verifiable context adapters": create, attach (with leases), detach, inspect (with integrity checking). It tracks source hashes, adapter hashes, binary hashes, runtime fingerprints, determinism classification, replay recipes, capabilities contracts, TTL-based expiry, and session-scoped mounts.

But the only built-in profile is `noop`:

```rust
pub fn noop() -> Self {
    Self {
        name: "noop".to_string(),
        executable: "builtin:noop".to_string(),
        adapter_format: "noop".to_string(),
        determinism_class: DeterminismClass::Deterministic,
        ...
    }
}
```

The noop profile writes an empty file as the "adapter." The entire governance apparatus -- integrity checking, lease management, expiry tracking, provenance chains, replay recipes -- operates over an empty file. The infrastructure anticipates external internalizer executables but none are provided. This is a full type system and lifecycle for a capability that doesn't yet exist.

## 6. Risk-Tiered Context Capsule Policy: Complexity for Three Tiers

**What's unusual:** The capsule policy system (`src/core/capsule_policy.rs`) implements a full policy contract with risk tiers (low/medium/high/critical), each specifying allowed scopes, maximum context limits, and write permissions. It resolves the current git HEAD revision, hashes the policy file, and binds all of this into a cryptographic chain that gets embedded in every context capsule.

But the scope space is tiny: `core`, `interfaces`, `plugins`. The tier space is four levels. The actual enforcement amounts to: "low-risk requests can only see `interfaces` docs (max 4); medium can also see `core` (max 6); high/critical can see everything." This is a two-line lookup table wrapped in a crypto-binding framework.

The `repo_revision` binding is particularly expensive: every capsule query shells out to `git rev-parse HEAD`, creating a subprocess for each context lookup. The result is embedded in the capsule for tamper detection -- but the capsule is a local JSON file on the same filesystem where the git repo lives. An adversary who can tamper with the capsule can also tamper with the git history.

## 7. External Action Capability Broker: Allowlists That Allow Everything

The external action system (`src/core/external_action.rs`) implements a capability-scoped broker for subprocess execution. Each external command must match an allowlist for its capability type. The default config allows: git for VCS reads/writes, `cargo`/`decapod`/`git`/`bash`/`sh` for proof execution, `decapod` for verification, and `lsof` for system inspection.

The proof_exec capability allowing `bash` and `sh` means any proof gate can execute arbitrary commands. Since proof gates are user-defined in `proofs.toml`, and the proof system runs them via the external action broker, the "capability-scoped" restriction on proof execution is illusory -- you can run anything through a bash proof.

## Summary

The pattern across these findings is consistent: governance infrastructure that is architecturally elaborate but operationally thin. The constitution embedding is file copying called codification. The CBOR encoder is a partial reimplementation with hard-coded panic limits. The obligation status is claimed to be derived but is stored and never reconciled. The two-phase audit log detects but doesn't recover. The internalization lifecycle governs an empty file. The capsule policy crypto-binds a three-entry lookup table. The capability allowlist allows bash.

Each of these mechanisms incurs real complexity costs: code to maintain, abstractions to understand, failure modes to debug. The benefits they advertise -- codification, crash recovery, deterministic governance, capability restriction -- are either not delivered by the implementation or are delivered at a level much simpler than the infrastructure suggests.
