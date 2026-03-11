# Decapod source audit: strongest claims vs. actual implementation

An audit of the five strongest claims in `decapod-original.md` against the Rust source at `related-systems/decapod/`.

## Method

Each claim was read as a prediction: "if this is true, the code must do X." Then the code was checked for X.

---

## Claim 1: Proof-gated completion (Draft -> Executing -> Claimed -> Verified, gate on proof plan)

**Prediction.** There must be (a) an enum with exactly these four states, (b) a transition function that rejects invalid paths, and (c) a guard on Claimed->Verified that checks every gate in a proof plan has a passing result.

**What the code does.**

- `workunit.rs` defines `WorkUnitStatus` with exactly `Draft`, `Executing`, `Claimed`, `Verified`. Match.
- `can_transition()` allows only `Draft->Executing`, `Executing->Claimed`, `Claimed->Verified`, plus self-loops and `Executing->Draft` as a rollback. This is stricter than the report implies -- there's no way to skip a stage.
- `ensure_verified_ready()` is called on the `Claimed->Verified` transition. It checks two things: the proof plan must be non-empty, and every gate in the plan must have a corresponding result with `status == "pass"`. If any gate lacks a passing result, the transition returns `Err`.
- The `publish_workspace()` function in `workspace.rs` additionally verifies that any workunit associated with the branch is in `Verified` status before allowing publish. It also calls `verify_capsule_policy_lineage_for_task`, which checks content-addressed integrity of context capsules bound to the task.

**Verdict: confirmed, and actually stronger than stated.** The report says "Verified transition only fires if a proof plan passes." The code enforces not just proof plan passage, but also capsule integrity and policy lineage binding at publish time. The report understates the enforcement depth.

---

## Claim 2: Embedded constitution compiled into binary (200+ governance documents)

**Prediction.** There must be a compile-time embedding mechanism that includes constitution files as string constants in the binary, plus a lookup function.

**What the code does.**

- `assets.rs` defines an `embedded_docs!` macro that uses `include_str!` to embed files from `constitution/` at compile time. Each file becomes a `pub const` string.
- The macro generates `get_embedded_doc(path) -> Option<String>` for lookup and `list_docs() -> Vec<String>` for discovery.
- Counting the entries in the macro invocation: 8 core + 9 specs + 12 interfaces + 6 methodology + 10 architecture + 11 docs + 20 plugins = **76 embedded documents**, not 200+.
- There is a `get_merged_doc()` function that layers project-local overrides from `.decapod/OVERRIDE.md` on top of embedded content -- so the constitution is not fully immutable at runtime as the report implies.

**Verdict: partially confirmed, partially overstated.** The embedding mechanism works exactly as described -- `include_str!` bakes docs into the binary. But the count is ~76, not "over 200." And the override mechanism means the methodology is not completely "codified into the binary" -- projects can append per-component overrides. The report's claim that "no agent can drift from it because it cannot be edited at runtime" is inaccurate; the OVERRIDE.md mechanism exists precisely to allow runtime-ish adaptation.

---

## Claim 3: Typed federation graph with immutable critical nodes and supersession chains

**Prediction.** There must be (a) an enum or validated set of node types matching the 8 claimed types, (b) typed edges matching the 4 claimed types, (c) an immutability guard on critical types, (d) a supersede operation that creates edges and transitions status, (e) event-sourced append-only logs with replay.

**What the code does.**

- `VALID_NODE_TYPES` = `["decision", "commitment", "person", "preference", "lesson", "project", "handoff", "observation"]`. Exactly 8 types. Match.
- `VALID_EDGE_TYPES` = `["relates_to", "depends_on", "supersedes", "invalidated_by"]`. Exactly 4 types. Match.
- `CRITICAL_NODE_TYPES` = `["decision", "commitment"]`. The `is_critical()` function also treats any node with `priority == "critical"` as critical.
- `edit_node()` checks `is_critical()` and returns an error with "Cannot edit critical node... Use 'supersede' instead." This is a real enforcement gate, not advisory.
- The `Supersede` command exists in the CLI. The `add_node` function enforces provenance for critical types: `if is_critical(...) && sources.is_empty()` -> error.
- Every mutation (`add_node`, `edit_node`, `supersede`, `link`, etc.) appends a `FederationEvent` to both the SQLite `federation_events` table and an append-only `.jsonl` file.
- `rebuild_from_events()` replays the `.jsonl` log into a fresh SQLite database, enabling deterministic reconstruction.

**Verdict: confirmed across all sub-claims.** The implementation matches precisely. The only nuance is that `is_critical` extends beyond the two type names to include any node with critical priority -- a detail the report misses but that strengthens the claim.

---

## Claim 4: RPC response envelopes with allowed-next-ops, blockers, interlocks, advisories, attestations

**Prediction.** There must be a response struct containing all of these fields as distinct types, not just a flat JSON blob.

**What the code does.**

- `rpc.rs` defines `RpcResponse` with these fields:
  - `receipt: Receipt` (op, timestamp, inputs_hash, outputs_hash, touched_paths, governing_anchors)
  - `context_capsule: Option<ContextCapsule>` (fragments, spec, architecture, security, standards)
  - `allowed_next_ops: Vec<AllowedOp>` (op name, reason, required params)
  - `blocked_by: Vec<Blocker>` (kind enum, message, resolve_hint)
  - `interlock: Option<Interlock>` (code, message, unblock_ops, evidence)
  - `advisory: Option<Advisory>` (reconciliation sets with must/recommended, verification plan, loop signal, notes)
  - `attestation: Option<Attestation>` (id, op, timestamp, input_hash, touched_paths, interlock_code, outcome, trace_path)
  - `mandates: Vec<Mandate>` (not mentioned in the report)

- The `success_response()` and `error_response()` factory functions populate these consistently. Even error responses include `allowed_next_ops` (defaulting to `agent.init`).
- `workspace.rs` has `get_allowed_ops()` which computes context-sensitive next operations based on workspace state.

**Verdict: confirmed, and richer than described.** The report mentions receipt, context capsule, allowed_next_ops, blockers, interlocks, advisories, and attestations. The code has all of these as first-class types plus `mandates` (governing constitutional fragments) which the report omits. The advisory type is more structured than implied -- it contains reconciliation sets (must vs. recommended), verification plans, and loop detection signals.

---

## Claim 5: Workspace isolation via git worktrees under `.decapod/workspaces/`

**Prediction.** There must be code that (a) detects protected branches and blocks work on them, (b) creates git worktrees in `.decapod/workspaces/`, (c) enforces per-agent isolation.

**What the code does.**

- `PROTECTED_PATTERNS` = `["main", "master", "production", "stable", "release/*", "hotfix/*"]`. `is_branch_protected()` checks against these.
- `get_workspace_status()` adds a `ProtectedBranch` blocker if on a protected branch, with resolve hints pointing to `decapod todo claim` + `decapod workspace ensure`.
- `ensure_workspace()` enforces: (a) must have an assigned open task (`get_assigned_open_tasks`), (b) branch name must contain the todo ID/hash, (c) creates worktrees via `git worktree add -b <branch> <path>` under `.decapod/workspaces/`.
- Worktree naming encodes agent ID, todo scope, and branch: `format!("{}-{}-{}", agent_id, todo_scope, branch)`.
- `publish_workspace()` gates on worktree status, protected branch check, provenance manifests, workunit verification status, eval gates, and capsule policy lineage.

**Verdict: confirmed, and more constrained than described.** The report says "agents must work in git worktrees." The code also requires a claimed todo before a worktree can be created, and the branch name must encode the todo scope. The publish path checks workunit verification status, provenance manifests, and eval gates -- the workspace is not just isolated, it's locked into a full governance pipeline.

---

## Summary of findings

| Claim | Accuracy | Key discrepancy |
|---|---|---|
| Proof-gated completion | Stronger than stated | Publish gate adds capsule integrity + policy lineage checks beyond proof plan |
| 200+ compiled constitution docs | Mechanism correct, count wrong | ~76 documents, not 200+; OVERRIDE.md allows runtime adaptation |
| Typed federation graph w/ immutability | Precise match | `is_critical` extends to priority="critical" (report only mentions type-based) |
| Response envelopes | Richer than stated | Also includes mandates, structured reconciliation sets, loop signals |
| Workspace isolation | More constrained than stated | Requires claimed todo, todo-scoped branch naming, multi-gate publish |

The report's characterizations are directionally correct across all five claims. The proof-gated completion and response envelope claims are understated (the implementation is more thorough than described). The constitution embedding count is overstated by roughly 2.5x, and the "cannot be edited at runtime" framing is contradicted by the OVERRIDE.md mechanism. The federation graph and workspace isolation claims are accurate to slightly understated.

The most revealing finding is the OVERRIDE.md mechanism. The report frames Decapod's methodology as maximally codified, at the opposite end of a constraining spectrum from commonplace's interpreted instructions. But Decapod has its own interpreted-override layer -- it's not at the extreme the report places it. The actual position is: compiled baseline with project-scoped override appendices, which is closer to commonplace's model than the report acknowledges.
