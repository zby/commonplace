# Decapod Investigation: What Surprised Me and What I Found

## What Triggered Curiosity

After reading the report and then the source, several things surprised me. I will work through them in order of how interesting the gap turned out to be between the report's claims and the actual implementation.

## 1. The "Embedded Constitution" Is Verbatim Copy, Not Codification

The report's strongest architectural claim is this:

> Over 200 governance documents are compiled into the binary. [...] This is constraining taken to its logical conclusion — the methodology is codified into the binary, not interpreted from instructions. No agent can drift from it because it cannot be edited at runtime.

This frames the embedding as a qualitative transformation: methodology gets "codified" into something agents cannot reinterpret or drift from.

**What the code actually does.** In `src/core/assets.rs`, the `embedded_docs!` macro uses `include_str!()` to copy each markdown file verbatim into the binary as a string constant:

```rust
macro_rules! embedded_docs {
    ($($path:expr => $const_name:ident),* $(,)?) => {
        $(
            pub const $const_name: &str =
                include_str!(concat!("../../constitution/", $path));
        )*
        // ...
    };
}
```

The `get_embedded_doc()` function returns these strings unchanged. The `get_merged_doc()` function optionally appends override text from `.decapod/OVERRIDE.md`. The `docs.rs` module then does keyword-frequency scoring (tokenize, count occurrences, boost by path/op bindings) to select which fragments to surface.

**No transformation occurs.** The markdown goes in as markdown and comes out as markdown. Agents receive raw prose slices that they must interpret — exactly the same interpretation challenge as reading markdown files from disk. The embedding achieves two things: (a) the binary is self-contained (no external file dependency), and (b) agents access docs through a search/retrieval API rather than filesystem reads. Neither of these is "codification." Reading the same markdown through `include_str!()` vs. `fs::read_to_string()` produces identical bytes. The interpretive variance is unchanged — it lives in how the LLM processes the prose, not in how the bytes are packaged.

**The OVERRIDE.md mechanism further undermines the claim.** Runtime overrides are explicitly supported — a project's `.decapod/OVERRIDE.md` can inject additional text into any constitution document. So the constitution is not only not codified, it is explicitly designed to be mutable at the project level without rebuilding the binary.

**What the report should have said:** Decapod bundles its methodology as embedded markdown for hermetic deployment, and gates access through a search API. This is a packaging decision, not a constraining mechanism. Interpretive variance is identical to reading the same files from disk.

## 2. Proof-Gated Completion Is Real But Thinner Than Described

The report claims:

> The Verified transition only fires if a proof plan passes. [...] This is the clearest production implementation of the principle that error correction requires decorrelated checks above chance.

**What the code actually does.** In `src/core/workunit.rs`, the `ensure_verified_ready()` function checks that every gate in the `proof_plan` has a corresponding entry in `proof_results` with status `"pass"`. The transition from Claimed to Verified is blocked if any gate lacks a passing result:

```rust
fn ensure_verified_ready(manifest: &WorkUnitManifest) -> Result<(), error::DecapodError> {
    if manifest.proof_plan.is_empty() {
        return Err(/* ... "cannot transition to VERIFIED without proof_plan gates" */);
    }
    for gate in &manifest.proof_plan {
        let hit = manifest.proof_results.iter()
            .any(|r| &r.gate == gate && r.status == "pass");
        if !hit { return Err(/* ... */); }
    }
    Ok(())
}
```

This is genuinely enforced — you cannot reach VERIFIED status without passing gates. The `proof.rs` module runs external commands from `proofs.toml` and records pass/fail based on exit code.

**But the decorrelation claim is aspirational.** Decapod does not verify that proof gates are decorrelated. The agent defines the proof plan and the proof commands. Nothing prevents an agent from defining a trivial gate (`echo pass && exit 0`) and satisfying it. The infrastructure enforces that *some* gates exist and pass; it says nothing about whether those gates are good. The report's framing as "error correction requiring decorrelated checks above chance" attributes discriminative power to the infrastructure when it actually lives entirely in the quality of the proofs the agent writes.

## 3. The Co-Player System Is Genuinely Novel

The `coplayer.rs` module was the biggest positive surprise. The report doesn't mention it at all, but it implements something interesting: **per-agent reliability tracking with policy derivation.**

Decapod scans the trace log to build a reliability profile for each agent (success rate, total ops, common operations). It then derives deterministic policy constraints: unknown agents get mandatory handshakes and 100-line diff limits; high-reliability agents get 500-line limits; low-reliability agents are forbidden from broad refactors and must provide extra proofs. The critical invariant is that policies only tighten — no agent, regardless of track record, can skip validation gates.

This is a real mechanism for adaptive trust that the report missed entirely. It maps to an interesting design principle: the system starts maximally restrictive and relaxes constraints only as evidence accumulates, but never below a hard floor.

## 4. The Obligation System Has an Unusual "Derived, Never Asserted" Invariant

The `obligation.rs` module (distinct from the `mentor.rs` obligations) implements a dependency-aware obligation graph where **status is always computed, never set directly.**

The comment at the top of the file states the key principle:
> Completion is DERIVED, never asserted. Status is computed from: dependencies satisfied, proofs verified, state_commit present. No user-settable status field.

The `derive_obligation_status()` function checks three conditions: all dependencies must be Met, all required proofs must be VERIFIED in the health cache, and a state_commit_root must be present. Only when all three hold does the obligation reach Met status.

This is a stronger version of the proof-gated completion. Where workunits let the agent define and satisfy its own proof plan, obligations tie into the health subsystem's claim tracking and require a state commit (a cryptographic merkle root over the changed files). The gap between "claim completion" and "prove completion" is smaller here.

## 5. The State Commit System Uses Hand-Rolled CBOR

`state_commit.rs` implements a Merkle tree over git diff entries with hand-rolled CBOR encoding. The `compute_scope_record()` function manually emits CBOR bytes for arrays, maps, strings, uints, and bools. The `compute_merkle_root()` function builds a binary Merkle tree over sorted file entries.

This is surprising because (a) it avoids the `cbor` crate despite already depending on `serde`, and (b) the hand-rolled encoding panics on strings > 255 bytes or arrays > 255 elements (`panic!("string too long")`), which is a hard limit that could easily be hit by a real file path.

## 6. The Assurance Engine's Loop Detection Is Interesting

The `assurance.rs` module detects when agents are stuck in loops — repeatedly editing the same file or hitting the same interlock gate. It scans the last 40 attestation events and emits a `LoopSignal` if any file has been touched 3+ times or any interlock has fired 3+ times. This is a practical mechanism for breaking agent perseveration that I haven't seen in other systems.

## 7. The Interview Engine Is Surprisingly Rigid

The report describes the interview engine as a mechanism for "refining human intent into explicit specifications." In practice (`src/core/interview.rs`), it's a fixed questionnaire — 12 hardcoded questions across 6 sections (overview, purpose, runtime, architecture, security, operations). The answers slot into template documents. There is no dynamic question generation, no branching based on answers, no learning from past interviews. The one-liner question and the language choice populate string templates. This is closer to a project scaffolding wizard than an intent refinement engine.

## 8. The Federation Graph's Supersession Is Correct But Simple

The federation graph implements supersession as described: old nodes get status "superseded" and a `supersedes` edge links the new node to the old. Critical node types (decision, commitment) are immutable after creation — the `edit` command explicitly rejects edits to critical nodes. Evolution happens only through supersession chains.

The provenance gating is also real: critical nodes must have at least one source with a scheme prefix (file:, url:, cmd:, commit:, event:). The regex validation is strict.

## Summary

The biggest finding is that **the "embedded constitution" claim is the report's most significant overstatement.** The constitution is bundled as raw markdown with `include_str!()`, no transformation occurs, and runtime overrides are explicitly supported via OVERRIDE.md. Calling this "codification" attributes a constraining property that the mechanism does not provide. The actual interpretive variance is identical to reading the same markdown from disk — the packaging changes, the semantics don't.

The proof-gating infrastructure is real but the discriminative power lives in agent-written proof definitions, not in the infrastructure. The co-player trust system, obligation-based derived status, and loop detection are genuinely interesting mechanisms that the original report did not cover.
