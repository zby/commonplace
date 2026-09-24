---
type: kb/types/note.md
description: 'arsumbris release-wide review: typed-file memory, adapter-specific governance and instructed
  knowledge/improvement workflows'
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-23-arsumbris-02
source-identity: https://github.com/arsumbris/arsumbris
reviewed-revision: arsumbris-0.0.1-alpha-release-bundle-2026-09-23
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/result.md
analysis-result-sha256: 49ac66eed29dc93441c088883dc7589a3520e51e59b8a0fc837bae7ce0c7985d
---

# arsumbris

Evidence basis: code and documentation from the entry repository plus all 21 component repositories pinned to release `0.0.1-alpha`, captured 2026-09-23. Static inspection only; no application, agent session or trial was run. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/result.md) retains every component commit, source excerpt, runtime route and comparison field.

arsumbris is a typed-knowledge IDE and agent operating layer. Its Rust engine builds a graph over repository files; its Electron host supplies views and launch control; its MCP kernel exposes plugin tools, hooks and context to Claude Code or Codex. Those external harnesses own model turns and delegation. Knowledge, schemas, rules, skills and extension metadata share an editable substrate, so a file can serve as advisory knowledge or become instruction through a selected profile. This is a whole-system review of the release components, with external harness/provider internals excluded.

## Runtime and controls

The ordinary path is host selection → adapter launch and context preparation → harness-chosen tool → mediation → plugin/engine operation → result and observation. The kernel checks profile visibility and input shape; plugins supply policy; the engine executes file mutations and rebuilds the graph. Critical plugin load failures prevent service, while runtime metadata selects code imported into the daemon process. See exact records RTE-1, RTE-2 and RTE-3.

Controls apply at specific paths. In particular, the adapters differ when mediation fails:

| Path | Implemented behavior | Limit |
|---|---|---|
| Claude Code hook | Falls back to allowing the action when the daemon/session operation fails | Typed MCP tools still need the daemon, but native actions do not gain that dependency |
| Codex hook | Denies the action when mediation cannot complete | Depends on the harness executing the registered hooks |
| Direct kernel invoke | Checks visibility, continuity, input schema and stamps | Does not itself execute the separately requested mediator chain |

These distinctions are grounded in the pinned [Claude Code bridge](https://github.com/arsumbris/au-mcp-adapter-cc/blob/333b2117f338cd4815eeeb9ab7b3932b29fa7d62/src/bridge.ts), [Codex bridge](https://github.com/arsumbris/au-mcp-adapter-codex/blob/3b0e3a3cf67b3143819c61c590efc85d36c23bc5/src/bridge.ts) and [kernel dispatch](https://github.com/arsumbris/au-mcp/blob/3ddc3b62ed0b339a89a57f11026676df18d3b2eb/src/daemon/daemon.ts), retained as RTE-4 and RTE-5.

A stale supplied content hash can reject a write. Resulting knowledge diagnostics are advisory at the generic mutation layer. The import plugin adds its own structural/stability checks before writing; neither route establishes source truth. Extension modules execute in-process, and the release explicitly claims no sandboxing. The baseline MCP `bash` callable is a stub; native shell tools and the host terminal are separate paths. These are scoped controls, not a machine-wide isolation guarantee (RTE-2, RTE-3, RTE-12).

## Memory and context

Retained memory lives in editable files and Git history, with a derived graph and generated access material. Agents pull file content or typed relationships. Launch machinery also pushes selected retained rule bodies and linked content: exact profile keys and graph references select by identity; member-role defaults and budgets provide coarse selection. Skills are materialized before launch, so saving a rule alone does not make it active (RTE-6, RTE-9).

Session governance facts survive for recovery/resume. Session-local read hashes and freshness notices are auxiliary controls, excluded from the normalized memory comparison. The inspected adapter compaction hooks forward events or visible transcript text; external summarization is outside this review (RTE-10, RTE-11, ABS-1).

A selected correction rule instructs an agent to retain reusable human feedback. A later improvement task reads corrections and their reasons, proposes a remedy, and can revise rules, skills or capabilities for future consumers. This qualifies as **afforded trace-fed memory**, contingent on instruction following and adoption. It is not observed learning. Curation coverage, trace-source formats, learning timing and recall-faithfulness evidence remain explicitly uncertain (RTE-8, RTE-16).

## Knowledge and improvement

Weave separates graph utility from truth adjudication. Candidates are admitted for their contribution to the graph, and passage checks are prescribed before weaving. Its claim type explicitly leaves standing and contradiction resolution downstream:

> #: Standing and contradiction-resolution are downstream, not here.
> --- [claim.type.yaml](https://github.com/arsumbris/au-weave/blob/24320734e2436e8c75d44a7ff9afb6a330569840/type/claim.type.yaml)

Research, governance and competency skills prescribe consequential checks: compare interpretations with alternatives, verify a critic's finding, repeat the defect check after repair, obtain scoped human approval and demonstrate promised behavior through the intended consumer. These are substantial agent/human procedures. A `researched` or `accepted` type marker does not prove the history occurred; approval to implement is distinct from evidence that a remedy worked (RTE-7, RTE-14, RTE-15, RTE-16).

The strongest supported improvement contribution is this concrete correction-to-remedy pathway, joined to implemented persistence and later delivery. No inspected outcome comparison establishes improved future capacity attributable to criticism. [Reflection](../../notes/definitions/reflective-system.md) is wired for typed capability representation and dispatch; revision of an operative self-theory remains uninspected. A [self-improvement](../../notes/definitions/self-improving-system.md) pathway is afforded, while exercised self-improvement and [conjectural learning](../../notes/definitions/conjectural-learning.md) remain unestablished.

## Scope

The review does not establish deployed grants, model/version identity, provider behavior, converter fidelity, full UI behavior, throughput or reliability. A pinned workspace run, a correction/remedy lineage with later consumer evidence, and comparable trials varying retained guidance would resolve different parts of those limits. The exact result distinguishes implementation from doctrine and makes no product ranking or transfer recommendation.
