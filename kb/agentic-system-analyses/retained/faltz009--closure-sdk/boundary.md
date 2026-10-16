---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Closure-SDK's current Closure EA geometric memory and learning subsystem at commit 9735f48a6ddd00b6f429a91443489531b3a115ef, including shipped Rust callers and evaluators."
run-id: AAS-2026-10-13-closure-sdk-294e6865ca51-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: subsystem-only
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/faltz009/Closure-SDK
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/closure-sdk-294e6865ca51/related-systems/faltz009--Closure-SDK
  revision: "9735f48a6ddd00b6f429a91443489531b3a115ef"
  sha256: null
---

# Closure-SDK boundary

## Boundary and evidence

This run analyses **the current Closure EA Rust geometric memory and learning subsystem within Closure-SDK**, not the entire monorepo and not just the Python data-integrity API. Its intended use is to explain how this subsystem admits carriers into memory, reads retained state, changes it through feedback and consolidation, and serializes it for reuse. The target class is `memory/knowledge/context-engineering system`; the boundary kind is `subsystem-only`.

The repository presents several distinct products. The root README calls `closure_ea/` the Geometric Computer, `closure_sdk/` the data-integrity SDK, and `closure_dna/` the geometric database. The Python package publishes integrity and database commands, whereas the current learning subsystem has its own Rust crate and public `ThreeCell` surface. These are separate shipped responsibilities, not an external host inferred merely from a library-call boundary (SRC-1, `README.md`, `pyproject.toml`, `closure_ea/Cargo.toml`, `closure_ea/src/lib.rs`, `closure_ea/__main__.py`).

The subsystem qualifies on its implemented memory and learning functions. This does **not** classify it as an LLM agent harness or establish a model-provider integration. Its declared substrate is quaternion geometry; the inspected learning caller obtains a prediction from a field read, commits it, and evaluates it against a supplied target. The source's use of “brain,” “semantic,” or “cognitive” is not evidence of human-like cognition (SRC-1, `closure_ea/src/lib.rs`, `closure_ea/src/teach.rs`).

> //! - [`genome`] — DNA + epigenetic layers, Law 3 ingest, nearest neighbor.
> //!   Bootstrap seeds DNA; chunked learning writes epigenetic.
> //! - [`field`] — RESONATE and ZREAD over `genome ∪ buffer`.
> --- `closure_ea/src/lib.rs`

> brain.commit_prediction(predicted, source);
> brain.evaluate_prediction(target);
> --- `closure_ea/src/teach.rs`

### Functional scope

Included paths are the current crate's `closure_ea/src/` modules, its manifest, `closure_ea/examples/` shipped drivers and evaluators, and the inline tests in `closure_ea/src/lib.rs`. This includes substrate embedding and addressing, transient buffering, genome reads and writes, hierarchy emission, prediction feedback, consolidation, generation, state save/load, curriculum drivers, and runtime-backed execution consumers. The subsystem's own `closure_ea/README.md` and `closure_ea/docs/` supply declared design; documentation claims remain distinct from implementation evidence. The initial inspected paths below are not an allowlist: further inspection of included paths at the same commit is permitted under SRC-1.

The entry-point trace establishes more than an API inventory:

- `closure_ea/src/lib.rs` exports `ThreeCell`, `BrainState`, memory modules and curriculum functions. `ThreeCell::ingest` receives a carrier, reads the genome and buffer, records closure-related admission signals, promotes eligible expired entries, and invokes consolidation. The boundary includes the entire implementation of these responsibilities, not only the initially read ranges (SRC-1, `closure_ea/src/lib.rs`, `closure_ea/src/three_cell.rs`).
- `closure_ea/src/teach.rs` drives ingestion and delayed target feedback. `closure_ea/examples/exp_neuromodulated_learning.rs` is a shipped caller that supplies context, commits predictions, evaluates them and forces consolidation. It is **included**, not treated as an excluded application because it supplies state (SRC-1, `closure_ea/src/teach.rs`, `closure_ea/examples/exp_neuromodulated_learning.rs`).
- `closure_ea/examples/exp_associative_memory.rs` writes input/target pairs through `learn_response` and later consumes the retained pairs through `brain.evaluate`. Its recall and interference checks are included evaluator code, not observed experimental results (SRC-1, `closure_ea/examples/exp_associative_memory.rs`).
- `closure_ea/src/execution.rs` embeds `ThreeCell` in `OrbitRuntime`, seeds orbit memory, and consumes it through evaluation. Those helpers and their shipped Rust example callers remain inside this boundary (SRC-1, `closure_ea/src/execution.rs`).
- `ThreeCell` exposes JSON file persistence and reconstruction. The inline round-trip test constructs nontrivial state, snapshots it, restores it and checks retained fields. This is source evidence for a persistence contract and an evaluator, not evidence that the test passed during this run (SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/lib.rs`).

> let genome = brain.hierarchy_mut().genome_at_mut(0);
> for k in 0..N_PAIRS {
>     genome.learn_response(&inputs[k], &targets[k]);
> }
> --- `closure_ea/examples/exp_associative_memory.rs`

> pub fn load_state_from_file(path: &str) -> Result<Self, Box<dyn std::error::Error>> {
>     let json = std::fs::read_to_string(path)?;
>     let state: BrainState = serde_json::from_str(&json)?;
>     Ok(Self::from_brain_state(state))
> }
> --- `closure_ea/src/three_cell.rs`

### Exclusions and limits

| Material | Treatment and role | Conclusion prevented |
|---|---|---|
| `closure_sdk/`, `closure_cli/`, `closure_rs/`, `rust/`, `examples/`, `benchmarks/`, `data/`, `tests/` | Deliberately excluded sibling integrity product, shared Python-extension core, SDK examples, benchmarks and fixtures. Package metadata, SDK exports/operations and CLI dispatch were inspected to distinguish this surface from the selected Rust crate. | No full SDK integrity, stream-diagnosis, benchmark or Python-extension assessment. |
| `closure_dna/` | Deliberately excluded sibling database, including its table storage, SQL, web workbench, persistence callers and evaluators. Its README and command entry point were inspected for placement. | No account of database durability, SQL semantics, resonance-query implementation or database-to-EA integration. |
| `closure_ea/archive/legacy_runtime/` | Deliberately excluded archived Python runtime and music/walking tracks. Its README describes a different adaptive runtime and persistent genome. | No claims about legacy lattice persistence, Bach generation, PyBullet learning or migration equivalence. |
| `closure_ea/demos/enkidu_alive/` | Deliberately excluded separate homeostasis demonstration. The inspected Python driver imports the SDK stream classifier and chooses movement from drive magnitudes; it is not the current Rust `ThreeCell` caller traced above. | No end-to-end claims about that agent's navigation, survival or use of current EA memory. |
| `docs/` | Deliberately excluded browser site, visualizers and JavaScript demonstrations. Repository searches identified browser material but no current Rust `ThreeCell` caller there. | No browser/Rust equivalence or deployed-site behavior claims. |
| Root SDK/application/CLI documents, old README, benchmark/test reports, standalone geometric paper and Zeroth Law PDF, images, `.github/`, `.gitignore`, `LICENSE` | Outside the selected functional subsystem; root README and packaging metadata were inspected for orientation. | No comprehensive theoretical proof audit, release/CI assessment or validation of reported performance. |

These are deliberate scope exclusions, not inaccessible source. Included module bodies and examples not yet read are **not yet inspected**, not access gaps. There is no established source-access gap at this pin. The Rust crate declares `sha2`, `serde` and `serde_json` dependencies (SRC-1, `closure_ea/Cargo.toml`); their implementations, the compiler, filesystem guarantees and any enclosing application's scheduling are external and not attributed to Closure EA. A caller is responsible for supplying carriers and target feedback and choosing when to save or reload; the included crate methods and shipped callers establish only their own responsibilities.

The frozen repository is `https://github.com/faltz009/Closure-SDK` at `9735f48a6ddd00b6f429a91443489531b3a115ef`. HEAD was checked against the supplied acquisition pin. The applicability cutoff is **2026-10-13**, the supplied run date; it is not an assertion that later repository revisions behave identically. Overall evidence is **code-grounded**, supplemented by source-native doctrine/design. No target code, tests, examples, model calls or services were executed. No execution traces or causal experiments are registered. Source inspection therefore cannot establish measured correctness, learning effectiveness, runtime performance or deployment reliability.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/faltz009/Closure-SDK` | 9735f48a6ddd00b6f429a91443489531b3a115ef | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/closure-sdk-294e6865ca51/related-systems/faltz009--Closure-SDK`. Tracked repository tree and bounded consumer/provider searches. Implementation: `pyproject.toml`; `closure_sdk/__init__.py`, `closure_sdk/ops.py`; `closure_cli/__main__.py`; `closure_dna/__main__.py`; `closure_ea/__main__.py`, `closure_ea/Cargo.toml`; public exports and round-trip test portions of `closure_ea/src/lib.rs`; ingestion, consolidation entry points, evaluation/generation and save/restore portions of `closure_ea/src/three_cell.rs`; teaching/evaluation functions in `closure_ea/src/teach.rs`; construction and slot-read portions of `closure_ea/src/execution.rs`; learning episode driver in `closure_ea/examples/exp_neuromodulated_learning.rs`; write/recall/interference portion of `closure_ea/examples/exp_associative_memory.rs`; full `closure_ea/demos/enkidu_alive/homeostasis.py`. Doctrine/design: full `README.md`, `closure_ea/README.md`, `closure_dna/README.md`, `closure_ea/archive/legacy_runtime/README.md`, and inspected inline module/API comments. | Implementation: [public crate surface](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/closure_ea/src/lib.rs), [state loop and persistence](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/closure_ea/src/three_cell.rs), [curriculum](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/closure_ea/src/teach.rs), [memory evaluator](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/closure_ea/examples/exp_associative_memory.rs). Doctrine/design: [repository overview](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/README.md), [current EA description](https://github.com/faltz009/Closure-SDK/blob/9735f48a6ddd00b6f429a91443489531b3a115ef/closure_ea/README.md). | No established checkout access gap. Implementation scope is static code inspection, not observed operation. Design statements are attributed intent, not proofs or measured outcomes. Deliberate subsystem exclusions above prevent whole-monorepo conclusions. No observed run or causal experiment was supplied or performed. |
