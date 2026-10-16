---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Context Constitution's context-management policy and declared Letta affordances at commit 964f30137ace9eade1aef112992ed6539b61bbb0, without the executing harness."
run-id: AAS-2026-10-15-context-constitution-7a352d7408f6-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "964f30137ace9eade1aef112992ed6539b61bbb0"
analysis-cutoff: "2026-10-15"
evidence-tier: doc-grounded
source:
  identity: https://github.com/letta-ai/context-constitution
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-context-constitution/related-systems/letta-ai--context-constitution
  revision: "964f30137ace9eade1aef112992ed6539b61bbb0"
  sha256: null
---

# Context Constitution boundary

## Boundary and evidence

This run analyses Context Constitution as a context-management policy artifact for Letta agents, not as an implementation of Letta Code or the Letta platform. It is in scope as a memory/knowledge/context-engineering system: its instructions govern what context a model-driven agent retains, retrieves, rewrites and uses on subsequent inference calls. The intended use is to explain that policy and its declared supporting interfaces, while keeping recommendations separate from demonstrated behavior (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

> The Context Constitution is a set of rules and principles governing what a Letta agent places in its context window, in what order, at what level of detail, and for how long. It is the policy by which a Letta agent manages its context — the most critical ingredient to experiential learning.
> --- `constitution/CONSTITUTION.md`

The target class is **memory/knowledge/context-engineering system** and the boundary kind is **complete artifact, partial loop**. Inspection of every tracked file finds a complete published document set, but no executable agent entry point, prompt loader, memory persistence/reload caller, or runtime evaluator. The README links to the Constitution as the public entry point; the Constitution addresses Letta agents and identifies its sister affordances document. The README reports internal use for prompting and model training, but the consuming integrations are not shipped here. Consequently, this run can establish the policy's proposed loop, not that a deployed harness loads these exact documents or implements their claims (SRC-1, `README.md`, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

> The **[Context Constitution](constitution/CONSTITUTION.md)** is a set of principles governing how AI agents manage context to learn from experience. We use the Constitution internally as the foundation of our prompting and for training memory-native models.
> --- `README.md`

Functional inclusions are the Constitution's identity, memory and continuity goals; system-prompt learning; progressive disclosure; efficiency and pruning guidance; and the affordances document's declared storage, indexing, message history, compaction and subagent interfaces. This includes both active maintenance guidance and future consumption of retained context. These are declarations and instructions, not inspected implementations (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

The external dependencies described by the artifact are a Letta harness, underlying language models, persistent memory blocks and message storage, a filesystem projection, Git synchronization, retrieval tools and specialized subagents. Their implementations are outside the frozen repository. For example, the affordances document assigns propagation to a successful Git push; this boundary does not attribute the implementation or correctness of that admission step to the Constitution (SRC-1, `constitution/AFFORDANCES.md`).

> The filesystem projection of memory is also tracked and versioned using git: changes to memory via the files must be tracked via commits, and are only propogated to the underlying memory blocks on a successful push to remote. The local state (MemFS) is merely a projection of the true underlying memory state (memory blocks).
> --- `constitution/AFFORDANCES.md`

### Tracked-path coverage

Every tracked file was read in full. The following table also distinguishes document guidance from absent runtime evidence; no material shipped path remains uninspected.

| Top-level tracked path | Treatment and inspected material | Role and conclusion limit |
|---|---|---|
| `README.md` | Included; full file | Public entry point, intended use and reported internal adoption. Does not expose the actual prompting or training integration. |
| `constitution/` | Included; `constitution/CONSTITUTION.md` and `constitution/AFFORDANCES.md`, both complete | Agent-facing policy, maintenance guidance, retrieval and later-consumption prescriptions, declared harness interfaces, and self-assessment questions. No executable persistence, reload, admission, model-call consumer or evaluator is shipped in this directory. |
| `.github/` | Inspected; `.github/workflows/check-whitespace.yml`; excluded from agent mechanism | Pull-request/main-push Markdown whitespace check. This is publication hygiene, not an evaluation of memory quality, policy adherence or learning; it cannot support those conclusions. |
| `.editorconfig` | Inspected; excluded from agent mechanism | Text-formatting settings; no evidence of agent runtime behavior. |
| `LICENSE` | Inspected; excluded from agent mechanism | CC0 legal terms; no evidence of context-management behavior. |

The frozen evidence is SRC-1 at commit `964f30137ace9eade1aef112992ed6539b61bbb0`; the applicability cutoff is **2026-10-15**. The overall evidence tier is **doc-grounded**. The only executable text inspected is the whitespace workflow, not an agent implementation. No target execution, observed agent run, experimental comparison, or model-training artifact is included. Linked blogs, papers, issue threads and other repositories are deliberately outside the source set; they cannot supply implementation details or corroborate effectiveness in this run. The absence of the harness and consuming integrations prevents conclusions about actual synchronization, retrieval reliability, compaction fidelity, subagent scheduling, deployed prompt contents or learning outcomes. It does not prevent a complete analysis of the published policy artifact.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/letta-ai/context-constitution` | 964f30137ace9eade1aef112992ed6539b61bbb0 | doctrine/design; reported operation; implementation (publication hygiene only) | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-context-constitution/related-systems/letta-ai--context-constitution`. All six tracked files inspected completely. Doctrine/design: `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`, `README.md`; reported operation: README's claim of internal prompting/training use; implementation: `.github/workflows/check-whitespace.yml`. Also inspected `.editorconfig` and `LICENSE` for repository coverage. | Doctrine/design: [Constitution](https://github.com/letta-ai/context-constitution/blob/964f30137ace9eade1aef112992ed6539b61bbb0/constitution/CONSTITUTION.md), [Affordances](https://github.com/letta-ai/context-constitution/blob/964f30137ace9eade1aef112992ed6539b61bbb0/constitution/AFFORDANCES.md); reported operation: [README](https://github.com/letta-ai/context-constitution/blob/964f30137ace9eade1aef112992ed6539b61bbb0/README.md); publication hygiene implementation: [workflow](https://github.com/letta-ai/context-constitution/blob/964f30137ace9eade1aef112992ed6539b61bbb0/.github/workflows/check-whitespace.yml). | No access gap within the frozen tracked tree. Runtime, consuming prompt/training integrations, persistent state and agent evaluations are not shipped here; their absence prevents implementation and outcome verification. README adoption claims remain attributed reports, not observed operation. No observed-run or causal-experiment evidence. |
