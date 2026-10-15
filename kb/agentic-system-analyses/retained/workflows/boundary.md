---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Claude Code dynamic workflows bounded to the workflows documentation captured on 2026-10-14."
run-id: AAS-2026-10-14-workflows-f9c2f80a3a94-01
result-disposition: complete
target-class: workflow
boundary-kind: subsystem-only
reviewed-boundary: workflows-2026-10-14
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  kind: capture
  identity: https://code.claude.com/docs/en/workflows
  revision: workflows-2026-10-14
  path: /home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md
  sha256: 764adc113891e88b0c6fc70e6aa51d3c5d207a773e9747f9e4f4e9b0e1a392e9
---

# Claude Code dynamic workflows boundary

## Boundary and evidence

This run supports an account of the documented dynamic-workflow mechanism, not a whole-system review of Claude Code. The target is in scope as a model-dependent workflow: Claude generates an orchestration script and its runtime coordinates model-backed subagents. Its target class is `workflow`; its boundary kind is `subsystem-only` (SRC-1, frozen capture, opening paragraphs).

> A dynamic workflow is a JavaScript script that orchestrates many [subagents](/docs/en/sub-agents) at once. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

The functional boundary includes the documented entry routes (bundled commands, explicit requests, ultracode, saved and plugin workflows), launch approval, script authoring and loading, orchestration primitives, background progress and controls, results, saved scripts, replay, interruption, failures, resource limits, model selection, and disable settings. The entire captured page was inspected, including its JavaScript example. These are documented responsibilities, not traced implementation behavior (SRC-1, sections `Have Claude write a workflow`, `How a workflow runs`, and `Manage runs`).

The script runtime and worker execution are distinct in the documented contract:

> | No direct filesystem or shell access from the workflow itself | Agents read, write, and run commands. The script coordinates the agents |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

External dependencies include the enclosing Claude Code session and its permission evaluation, subagent execution and tools, model services, subscription or API access, local project/session storage, and cloud or other host surfaces where used. The page describes their interfaces to workflows; their independent internals are excluded. This prevents attributing the enclosing session's general reasoning, worker-tool safety, provider reliability, or host persistence implementation to the workflow script itself. The documented `/deep-research` dependency on WebSearch is included as a declared requirement, not as evidence of search quality (SRC-1, `Bundled workflows`, `Approve the plan before it runs`, `How a workflow runs`, `Cost`, and `Turn workflows off`).

The evidence is one immutable Markdown response captured from `https://code.claude.com/docs/en/workflows` using an HTTP request accepting `text/markdown`. The capture label is `workflows-2026-10-14`; the exact-byte SHA-256 and absolute access path appear above. The analysis cutoff is 2026-10-14, the supplied run date and capture date. The label is a local capture identity, not an upstream release or a claim that every documented feature exists in every version. Version qualifications in the page remain conditions on later claims. Applicability after the capture is unestablished.

Overall evidence is `doc-grounded`, supplying declared contracts and design. No implementation repository was supplied or acquired; no repository tree or executable entry-point consumers are available within this document-only boundary. No implementation repository is inferred. Accordingly, implementation coverage, actual enforcement, physical storage formats and crash consistency cannot be concluded. No execution trace or experiment is supplied, so observed reliability, cost, performance and causal quality improvements cannot be concluded. Linked documentation, the advertised documentation index, the bundled authoring skill's full reference, actual bundled/saved/plugin script files, and underlying permission and subagent specifications are outside the single capture. Their omission prevents establishing full API semantics or behavior beyond what this page states; those links are not additional frozen sources.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | capture | `https://code.claude.com/docs/en/workflows` | workflows-2026-10-14 | doctrine/design | Entire 506-line Markdown capture, titled “Orchestrate subagents at scale with dynamic workflows”; opening definition, comparison table, bundled workflow, entry routes and consent, saving/loading and plugins, example script and primitives, runtime constraints, cache and replay, interruption/retries, limits/cost/settings. Absolute access root is the frontmatter capture path. | Frozen file `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`; local headings `When to use a workflow`, `Run a bundled workflow`, `Have Claude write a workflow`, `How a workflow runs`, `Manage runs`, `Turn workflows off`. | No implementation or run evidence: cannot establish actual enforcement, reliability, performance or causal benefit. Linked pages and executable workflow artifacts are deliberately excluded: cannot establish their full contracts or inspect bundled orchestration. Capture alone does not establish upstream release identity or later applicability. |
