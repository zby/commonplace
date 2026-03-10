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

**Proof-gated completion is oracle enforcement.** Work units progress through Draft → Executing → Claimed → Verified, but the Verified transition only fires if a proof plan passes. The proof plan is an ordered list of gates — each gate is an oracle that checks whether the work satisfies its specification. Decapod doesn't build oracles (that's the agent's job), but it enforces that oracles exist and pass before promotion. This is the clearest production implementation of the principle that error correction requires decorrelated checks above chance — Decapod provides the enforcement infrastructure, agents supply the discriminative power.

**Embedded constitution as immutable methodology.** Over 200 governance documents (core contracts, specs, interface rules, plugin contracts, methodology guides) are compiled into the binary. Agents fetch relevant slices via context capsules rather than reading files directly. This is stabilisation taken to its logical conclusion — the methodology is crystallised into the binary, not interpreted from instructions. No agent can drift from it because it cannot be edited at runtime.

**Daemonless, repo-native state.** Everything lives in `.decapod/` — four SQLite databases (governance, memory, automation, todo), event logs, and config. No background service. Agents call the binary on demand and it exits when done. State is repo-local, version-controllable, and inspectable. This is the same filesystem-first instinct as commonplace, though the storage format diverges sharply (SQLite vs markdown).

**Typed federation graph.** Knowledge is represented as typed nodes (Decision, Commitment, Person, Preference, Lesson, Project, Handoff, Observation) connected by typed edges (relates_to, depends_on, supersedes, invalidated_by). Critical types (Decision, Commitment) are immutable after creation — evolution happens through supersession chains, not edits. All mutations are event-sourced in append-only `.jsonl` logs. The type system enforces provenance gating: critical nodes must cite sources at creation.

**RPC-first agent interface.** Agents communicate via JSON-RPC and receive structured response envelopes containing: a receipt (what happened), a context capsule (relevant doc slices), allowed next operations, blockers, interlocks (hard stops), advisories (soft guidance), and attestations (proof artifacts). This is an explicit calling convention — the agent always knows what it can do next and what's blocking it.

**Workspace isolation.** Agents must work in git worktrees under `.decapod/workspaces/`, never on main/master. Validation invariants enforce this. For multi-agent scenarios, each agent gets its own worktree, preventing silent overwrites. This is a code-level solution to the same coordination problem that bounded-context orchestration addresses architecturally.

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

**Where commonplace is stronger.** Knowledge has a maturation lifecycle — notes progress through status transitions, descriptions serve as retrieval filters, link semantics articulate how ideas relate. Decapod's federation graph stores facts about agent work but doesn't support the accumulate → stabilise → distil → discover progression. The files-first choice gives us universal readability and zero-infrastructure portability that SQLite doesn't match. Our title-as-claim convention means traversal is reasoning — following links reads as a chain of arguments. Decapod's nodes have titles, but the titles are labels, not claims.

**The methodology enforcement comparison is the most revealing.** Decapod compiles its constitution into the binary — maximum stabilisation, zero interpretive variance. Commonplace keeps methodology in markdown files that agents interpret — maximum flexibility, non-zero interpretive variance. This maps directly onto the stabilisation spectrum: Decapod is at the crystallised end, commonplace is in the partial-stabilisation middle. The trade-off is real: Decapod's methodology cannot drift but also cannot adapt without a new binary release. Ours can adapt on every session but may drift.

## Borrowable Ideas

**Proof-gated status transitions.** The principle — don't let work claim completion without passing explicit checks — is immediately applicable. In commonplace, this would mean a note can't transition from `seedling` to `current` without passing structural validation (description quality, link health, index membership). Currently `/validate` runs post-hoc; making it a gate on status transition would be a meaningful upgrade. *Ready to borrow — would require skill/hook integration, not just convention.*

**Response envelopes with allowed-next-ops.** The pattern of returning not just results but also what the agent is allowed to do next is a form of frontloading — the control plane pre-computes the decision tree so the agent doesn't waste context reasoning about permissions. For commonplace, skill outputs could include "suggested next actions" to guide agent workflow. *Needs a use case first — our single-agent model has simpler coordination needs.*

**Supersession chains for decision evolution.** Instead of editing a decision in place, create a new node that supersedes the old one. This preserves the full decision history without relying on git archaeology. For commonplace's ADRs, this would mean a superseding ADR explicitly links to its predecessor rather than having a "superseded" status with no forward pointer. *Ready to borrow — the ADR type already has a status field; adding a `supersedes` link convention is lightweight.*

**Content-addressed artifacts for drift detection.** Hashing specifications and proof artifacts means any change is detectable — you know whether the spec the agent worked against is still the current spec. For commonplace, this could apply to source snapshots: hash the snapshot at ingest time, detect if the source has changed on re-visit. *Needs a use case first — our sources are snapshots, not live references.*

**Internalization as explicit distillation.** Decapod's internalization subsystem (turn a large doc into a mountable compressed artifact) is a production implementation of distillation — targeted extraction from a larger body into a focused artifact shaped by specific circumstances. The key addition is the determinism classification: deterministic artifacts are replayable, best-effort ones carry runtime fingerprints. *Worth watching — we don't yet have a formal distillation pipeline.*

## What to Watch

- Whether the constitution-as-binary model survives contact with diverse projects. A compiled governance layer works when the methodology is stable; projects with rapidly evolving conventions may find the release cycle too slow. If Decapod adds runtime constitution overrides, it moves toward commonplace's interpreted-instructions model.
- Whether the federation graph develops maturation beyond supersession. Currently nodes are created, optionally superseded, and never revisited. If Decapod adds mechanisms for lessons to generate new decisions (learning from operational experience), it begins to converge with our accumulate-stabilise-distil model.
- Whether proof-gated completion generalises beyond code verification. Decapod's proof plans currently gate on test suites and validation passes. If they extend to knowledge quality (did the agent's analysis meet structural standards?), the control-plane pattern becomes relevant to knowledge systems, not just code shipping.
- How the dual-store model (user-scoped vs repo-scoped) evolves. This is a form of three-space separation — agent-local state vs project knowledge — and the boundary decisions will be informative.
