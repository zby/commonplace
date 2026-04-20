---
description: Local agent control plane for Claude/Codex/Hermes with policy-gated execution, Claude hooks, Obsidian memory automation, and provenance receipts; strongest reviewed governance-heavy local ops stack
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-03-31"
---

# LACP

LACP is a bash-first local agent control plane for Claude, Codex, and Hermes. It wraps existing agent CLIs rather than replacing them, routes risky commands through explicit policy and context contracts, installs Claude Code hooks that shape session behavior, and pairs that execution layer with an Obsidian-centered memory and automation stack. The implementation is substantial and real: the repo contains a large shell command surface, Python hooks, task-harness plumbing, evidence-manifest tools, and memory maintenance scripts. It is also visibly still expanding quickly: the README presents stable `v0.3.x`, while `main` already carries a large unreleased surface in the changelog.

**Repository:** https://github.com/0xNyk/lacp

## Core Ideas

**Harnessing existing agents is the product, not a sidecar.** LACP is not a new agent runtime. The repo says that explicitly in `docs/framework-scope.md`, and the code matches it: [`bin/lacp`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp) is a dispatcher that forwards into dozens of `lacp-*` subcommands, while the default no-args path launches `lacp-stream` rather than a custom model loop. The core bet is that local agent reliability can be improved by wrapping Claude/Codex/Hermes in a governance layer instead of rebuilding the underlying assistant.

**Risk routing is encoded as explicit execution contracts.** The combination of [`bin/lacp-route`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-route), [`config/sandbox-policy.json`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/config/sandbox-policy.json), and [`bin/lacp-sandbox-run`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-sandbox-run) is the clearest center of gravity in the repo. Tasks get classified by trust, network use, external code, sensitivity, compute profile, and keyword signals; then the run layer enforces budget ceilings, optional critical confirmations, structured input contracts, structured context contracts, and session fingerprints. This is more than shell aliasing. It is a real policy boundary for local agent work.

**Claude hook governance is the tightest implemented feedback loop.** The Python hooks are where LACP feels most coherent as a system rather than a command collection. [`hooks/session_start.py`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/hooks/session_start.py) injects git context, detects tests, loads context modes, and pulls in focus briefs and recent handoffs. [`hooks/stop_quality_gate.py`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/hooks/stop_quality_gate.py) combines heuristic rationalization checks, transcript-derived work detection, cached test-command verification, and optional Ollama scoring before allowing session stop. This is the strongest implemented answer in the repo to the question "how do you make a local coding agent less likely to claim success without evidence?"

**The memory layer is an Obsidian operations stack, not a general knowledge model.** LACP's memory subsystem is real, but it is operational rather than especially elegant. [`bin/lacp-brain-stack`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-brain-stack) wires MCP servers and scaffolds per-project memory files. [`bin/lacp-brain-ingest`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-brain-ingest) emits schema-shaped markdown notes with provenance fields. [`bin/lacp-brain-expand`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-brain-expand) runs a long maintenance pipeline over sessions, research signals, inbox routing, QMD refreshes, and doctors. The schema and KPI pieces are concrete (`config/memory/node-schema.json`, `bin/lacp-memory-kpi`), but the system is primarily a vault-automation layer over markdown plus MCP tools, not a distinctive knowledge representation in its own right.

**Auditability is implemented as receipts and manifests, not just rhetoric.** LACP talks constantly about evidence and auditability, and here the implementation largely holds up. [`bin/lacp-harness-run`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-harness-run) creates dependency-aware task runs with chained receipts. [`bin/lacp-provenance`](https://github.com/0xNyk/lacp/blob/b86157bfd2374fc492c15dd5993c7efe24041a47/bin/lacp-provenance) maintains an append-only SHA-256-linked session chain. The evidence tooling for browser/API/contract e2e is also real. The important nuance is that this auditability is strongest for operational traces and completion artifacts; it is weaker as a guarantee that the memory or reasoning layers themselves are semantically correct.

## Comparison with Our System

| Dimension | LACP | Commonplace |
|---|---|---|
| Primary concern | Governing and hardening local agent operations | Building and maintaining a file-based knowledge base for agent use |
| Main abstraction | Commands, policies, hooks, contracts, artifacts | Notes, links, descriptions, indexes, instructions, skills |
| Enforcement placement | Heavy on shell scripts and hooks; behavior pushed into runtime mechanisms | Heavy on document structure, traversal rules, and selectively invoked skills/scripts |
| Execution safety | Explicit routing tiers, budget gates, context contracts, session fingerprints | Much lighter execution governance; stronger emphasis on content quality than run isolation |
| Knowledge substrate | Obsidian vault plus MCP wiring, schema-shaped frontmatter, automation registries | Repo-native markdown notes with explicit relationship semantics and curated indexes |
| Memory evolution | Ingest, expand, prune, KPI, resolve, consolidate; many maintenance commands | Write, connect, validate, refine; fewer automations, more curation in the note graph itself |
| Verification style | Artifact-backed checks, receipts, evidence manifests, stop-time session gates | Structural validation plus semantic review notes; fewer runtime gates, more editorial judgment |
| Human/agent coexistence | Strong for operators managing local tooling, vaults, and sessions | Strong for maintainers/agents co-authoring a KB, weaker as a workstation operations framework |

LACP is stronger wherever the problem is operational governance: routing risky commands, structuring repeatable local runs, injecting session context, and making verification artifacts first-class. Commonplace is stronger wherever the problem is knowledge quality: retrieval-oriented descriptions, articulated link semantics, document-type distinctions, and a clearer theory of what makes accumulated knowledge composable and trustworthy.

The systems also commit structure in different places. LACP commits structure into code and runtime contracts. Commonplace commits structure into the artifacts themselves. That difference matters. LACP can stop a risky command or demand a context contract; Commonplace can make a note graph legible and maintainable months later. Those are adjacent problems, not substitutes.

## Borrowable Ideas

**Structured input and context contracts for risky operations.** LACP's `--input-contract` and `--context-contract` pattern is one of the clearest borrowable mechanisms in the repo. For commonplace, this could shape future high-risk maintenance workflows or bulk operations so the agent has to state source, intent, allowed actions, denied actions, and expected execution context before mutating the KB. Ready to borrow when an operation becomes risky enough to justify ceremony.

**Hash-chained receipts for multi-step workflows.** The receipt chaining in `harness-run` and the session-level provenance chain are more rigorous than our current "trust git history plus transcripts" posture. For commonplace, this would make most sense for workshop pipelines, bulk migrations, or autonomous maintenance sweeps where step ordering and tamper-evident run history matter. Needs a concrete operations use case first.

**Doctor/KPI style health summaries over the knowledge layer.** `lacp-memory-kpi`, `status-report`, and the various `doctor` commands show a useful pattern: operators need compact health surfaces, not just raw files plus a validator. We already have stronger note semantics than LACP; we are thinner on consolidated operational dashboards. Ready to borrow now as a maintenance ergonomics idea.

**Session-start injection for focus and handoff continuity.** The session-start hook's use of focus briefs, cached test commands, and recent handoffs is a good harness pattern. We already think carefully about always-loaded context, but LACP shows a practical implementation for cross-session continuity that stays local and inspectable. Ready to borrow as a runtime pattern, not as a knowledge representation pattern.

## Curiosity Pass

**Harnessing existing agents is the product, not a sidecar.** The property claimed is safer, more reproducible local agent use without replacing Claude/Codex/Hermes. The mechanism is real: the dispatcher, wrappers, hooks, and policy commands do alter execution behavior. But the simpler alternative is still "a few shell wrappers and a hook profile." LACP earns its added complexity only where the pieces compose into something more systematic: route policy, context contracts, receipts, and diagnostics. The repo is strongest exactly where those pieces meet.

**Risk routing is encoded as explicit execution contracts.** The property is constrained execution. This is not naming. The route and sandbox code actually transform an unconstrained shell invocation into a run with trust metadata, budget checks, confirmation gates, and context validation. The ceiling is also clear: these contracts can strongly constrain *where* and *how* a command runs, but they do not prove the task semantics are correct. The value is governance, not correctness of the underlying plan.

**Claude hook governance is the tightest implemented feedback loop.** The property is reduced rationalization and better stop-time honesty. Part of the mechanism is strong: test-command caching, transcript scans, and explicit block/allow decisions are deterministic. Part is weaker: the stop hook still leans on heuristics and optional Ollama judgment. The simpler alternative is "just run tests before finishing." LACP's answer is that local agents need *session* gates, not just repo gates, because much bad behavior happens before a commit exists. I think that claim holds.

**The memory layer is an Obsidian operations stack, not a general knowledge model.** The property claimed is a five-layer memory system. Mechanistically, the picture is mixed. `brain-stack init` directly wires session memory, MCP servers, and ingestion support; the broader "five-layer" story includes optional GitNexus, provenance, and additional tools around the vault rather than one coherent substrate. The system does transform some data by adding schema, provenance fields, clustering, decay, and pruning, but much of the work is still relocation and maintenance over markdown notes plus registries. The simpler alternative is a smaller vault automation toolkit. LACP's memory value today is breadth of operational support, not a notably elegant knowledge model.

**Auditability is implemented as receipts and manifests, not just rhetoric.** The property is trustworthy operational history. The mechanism is real for receipts, provenance hashes, and manifest validation. But even if it works perfectly, the ceiling is "tamper-evident records of what the system did," not "proof that the knowledge or conclusion is correct." This is closer to the kind of operational evidence [Decapod](./decapod.md) emphasizes than to semantic knowledge validation. Useful, but narrower than the broad "control-plane-grade" framing can imply.

## What to Watch

- Whether the command surface converges into a smaller stable core, or keeps accumulating adjacent operational tools under the `lacp` umbrella.
- Whether the Obsidian memory stack develops stronger synthesis and curation logic, or remains mostly a large maintenance and routing layer over vault artifacts.
- Whether the release boundary catches up with `main`; the README's stable posture and the changelog's large unreleased surface suggest an actively moving target.
- Whether the routing/contract patterns become the durable heart of the project while the more ambitious memory framing becomes secondary.

---

Relevant Notes:

- [AGENTS.md should be organized as a control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md) — contrasts: commonplace keeps the control plane primarily in always-loaded documents, while LACP pushes much more of it into executable shell and hook code
- [Methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md) — exemplifies: LACP lives far toward the hook/script end of the enforcement gradient
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — extends: LACP mixes hard operational oracles (contracts, manifests, receipts) with softer heuristic and LLM-based stop-gate checks
- [Inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — exemplifies: even the heavier governance layer stays mostly local, file-backed, and inspectable
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: LACP is rich in workshop and operations machinery but comparatively thin on durable library semantics
- [Napkin](./napkin.md) — contrasts: both systems are local-first and Obsidian-aware, but Napkin focuses on agent-facing memory UX while LACP focuses on governance and execution control
- [Decapod](./decapod.md) — extends: both make proof and gate language central, but Decapod's kernel is narrower and more governance-pure while LACP sprawls into workstation and memory operations
