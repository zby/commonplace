---
description: Audit of overstated claims in the Decapod report -- proof-gating is self-reported not decorrelated, constitution has runtime overrides, publish gate is bypassable by its own branch naming, and storage/document counts are substantially wrong
type: note
tags: [related-systems]
status: current
---

# Decapod report overstates enforcement strength in four areas that compound

The [original report](./decapod-original.md) describes Decapod as having hard enforcement mechanisms for proof-gated completion, immutable constitution, immutable federation nodes, and DAG-enforced graph edges. Checking the implementation reveals that each of these is softer than described. Individually, each gap is minor. Together, they shift the overall picture: Decapod is a disciplined convention system with structural guardrails, not a system with cryptographic or type-level enforcement guarantees.

## 1. Proof-gated completion is agent-self-reported

**Claim (report):** "the Verified transition only fires if a proof plan passes. The proof plan is an ordered list of gates -- each gate is an oracle that checks whether the work satisfies its specification."

**What the code shows:** The `record_proof_result` function in `workunit.rs` (line 195) accepts a `status` parameter of `"pass"` or `"fail"` as a string argument from the caller. The agent (or any CLI caller) tells Decapod the result; Decapod records it. The `transition_status` function (line 220) then checks that every gate in the proof plan has a recorded `"pass"` result before allowing the Verified transition. This is enforced structurally -- the transition really does block without passing results.

But the proof system does not independently execute the proof gates and verify their outcomes during the transition. The `run_proofs` function in `proof.rs` is a separate subsystem (`decapod proof run`) that executes commands from `proofs.toml` and records results to a health database and event log. It is not wired into the workunit transition path. There is no call chain from `transition_status` -> `run_proofs`. The workunit system trusts the `record_proof_result` calls it received earlier.

**Why it matters:** The report frames this as "the clearest production implementation of the principle that error correction requires decorrelated checks." Decorrelated checking requires that the checker is independent of the claimer. Here, the same agent that does the work also calls `record_proof_result`. The checking is not decorrelated -- it is self-certified. Decapod enforces that self-certification happened, not that the certification is honest. The `publish_workspace` function (workspace.rs, line 800) does add a second check -- it verifies the workunit is in Verified status and checks capsule policy lineage -- but that still relies on the self-reported proof results.

This is still meaningfully better than having no gate at all (the agent must at least go through the motions), but it is not oracle enforcement in the sense the report claims.

## 2. The embedded constitution is overridable at runtime

**Claim (report):** "the methodology is codified into the binary, not interpreted from instructions. No agent can drift from it because it cannot be edited at runtime."

**What the code shows:** `assets.rs` (line 174) implements `get_merged_doc`, which takes the embedded (compiled-in) document and merges it with content from `.decapod/OVERRIDE.md` -- a file that lives in the repo and can be edited at any time. The override mechanism is structured (content goes below a "CHANGES ARE NOT PERMITTED ABOVE THIS LINE" marker, under path-specific headings), but it is a runtime text file, not a compiled artifact. The merged result appends a "## Project Overrides" section to the embedded document.

The `docs show` CLI command defaults to showing merged content (embedded + override). This is the content agents actually consume.

**Why it matters:** The report contrasts Decapod's "compiled constitution" with commonplace's "interpreted instructions" as opposite ends of a constraining spectrum, and uses this to frame the key design trade-off. In practice, Decapod occupies the same middle ground: a stable compiled base plus a runtime-mutable layer. The override mechanism is less flexible than commonplace's free-form markdown (it is additive-only and path-scoped), but it exists. The "zero interpretive variance" claim does not hold. This matters for the comparison table entry on "Methodology enforcement" -- the gap between the two systems is narrower than described.

## 3. Federation graph immutability applies only to critical types, not "critical types (Decision, Commitment)"

**Claim (report):** "Critical types (Decision, Commitment) are immutable after creation -- evolution happens through supersession chains, not edits."

**What the code shows:** The `edit_node` function (federation.rs, line 667) blocks edits to nodes where `is_critical` returns true. The `is_critical` function (line 357) returns true when `node_type` is in `CRITICAL_NODE_TYPES` ("decision", "commitment") **or** when `priority` is "critical". So immutability is correctly enforced for Decision and Commitment types.

However, the remaining 6 node types (Person, Preference, Lesson, Project, Handoff, Observation) are freely mutable via `edit_node`. The report says "Critical types are immutable after creation" which is accurate for those two types, but the surrounding text ("All mutations are event-sourced in append-only .jsonl logs") creates an impression that the entire graph has strong immutability properties. The event log is append-only, but the SQLite database state is mutable for non-critical nodes. The event log and database can diverge for edited nodes (the edit creates an event, but the database row is updated in place).

**Why it matters for the comparison:** The report's comparison says "The supersession model creates an auditable history of how decisions evolved, where our in-place editing loses intermediate states." This is accurate for decisions and commitments specifically. But for 6 of 8 node types, Decapod also does in-place editing. The contrast with commonplace is real but narrower than the report suggests.

## 4. DAG enforcement on edges is post-hoc validation, not insertion-time constraint

**Claim (report):** "Typed graph edges (4 types), DAG-enforced."

**What the code shows:** The `add_edge` function (federation.rs, line 936) validates edge type and checks that source/target nodes exist, but does not check for cycles. Cycle detection happens in the validation suite (federation.rs, line 1885), specifically only for `supersedes` edges. You can create a cycle with `decapod data federation link`; `decapod validate` will flag it afterward.

This is the same pattern the report attributes to commonplace's validation: "/validate flags problems but doesn't block anything." Decapod's federation graph validation also flags problems without blocking the mutation that caused them. The insert-time constraints are limited to type checking and node existence.

**Why it matters:** The comparison table says Decapod has "Typed graph edges (4 types), DAG-enforced" versus commonplace's "Markdown links with prose semantics." The typed edges and validation exist, but DAG enforcement is advisory, not structural. An agent can create invalid graph states and only discover them on the next validation pass.

## Compound effect

Each of these individually is a reasonable engineering trade-off (self-reported proofs are simpler, runtime overrides add flexibility, post-hoc validation is practical). But the report consistently describes Decapod at the maximum-enforcement interpretation of each feature, and this accumulates. The "Where Decapod is stronger" section frames proof-gated completion as "a real enforcement mechanism" contrasted with commonplace's "advisory" validation. In practice, Decapod's proof gating for workunits is also based on trusting the agent's own reports, and its graph validation is also advisory. The enforcement gap between the two systems is real but substantially narrower than the report presents.

The most consequential overstatement is #1 (proof self-reporting), because it undermines the central theoretical framing: "the clearest production implementation of the principle that error correction requires decorrelated checks above chance." If the checks are not decorrelated, this principle is not being implemented -- it is being approximated via a workflow convention that the agent runs its own tests and reports honestly.

## Additional findings from second audit pass

### 5. The publish gate has a branch-name escape hatch

The `verify_workunit_gate_for_publish` function (workspace.rs, line 965) extracts task IDs from the branch name using a regex: `(?i)(?:r_|test_|docs_|fix_|feat_)[a-z0-9]+`. If the regex matches nothing, the function returns `Ok(())` -- the workunit verification gate is skipped entirely. But the branch naming convention that `ensure_workspace` actually generates is `agent/{agent-id}/{todo-scope}-{timestamp}`, which does not match that pattern. This means branches created by Decapod's own workspace system silently bypass the workunit verification gate during publish.

The provenance manifest gate (requires `artifact_manifest.json` and `proof_manifest.json` to exist) still fires, but checks file existence, not content.

This compounds with finding #1: not only are proof results self-reported, but the gate that checks them can be bypassed by the branch naming convention the system itself produces.

### 6. "Four SQLite databases" is a significant undercount

The report says "four SQLite databases (governance, memory, automation, todo)." The `core/schemas.rs` file defines 15 database names: `governance.db`, `memory.db`, `knowledge.db`, `federation.db`, `decisions.db`, `automation.db`, `cron.db`, `reflex.db`, `todo.db`, `health.db`, `policy.db`, `feedback.db`, `archive.db`, `aptitude.db`, `lcm.db`.

This matters for the comparison table. The report frames Decapod's storage as "SQLite (4 databases) + event logs" versus commonplace's "Markdown files + git." The actual storage surface (15 databases with separate schemas, plus JSONL event logs, plus generated JSON artifacts in `.decapod/generated/`) is a substantial schema-management commitment that the comparison understates.

### 7. "Over 200 governance documents" compiled into the binary

The `constitution/` directory contains 94 markdown files. The `embedded_docs!` macro in `core/assets.rs` maps 55 documents into the binary via `include_str!`. Including generated templates (AGENTS.md, CLAUDE.md, GEMINI.md, CODEX.md, README.md, OVERRIDE.md), the total is around 60 embedded documents -- roughly a third of the claimed "over 200." This is a factual error that does not change the architectural analysis but inflates the perceived weight of the "can't adapt without a new binary release" trade-off.

### 8. Response envelope richness is defined but not populated

The `RpcResponse` struct (rpc.rs) contains all the fields the report describes: receipt, context_capsule, allowed_next_ops, blocked_by, interlock, advisory, attestation. The structure is real and well-typed. But `success_response` (the factory function) sets `interlock`, `advisory`, and `attestation` all to `None`. The `get_allowed_ops` function returns at most 2 entries. Each call site must manually construct the allowed-ops list; there is no centralized state machine that computes what the agent can do next.

The report's "Borrowable Ideas" section recommends this pattern as "the control plane pre-computes the decision tree so the agent doesn't waste context reasoning about permissions." The type definitions support this, but the population logic that would make it work does not yet exist. Borrowing this pattern means building the decision-tree logic, not just the envelope structure.
