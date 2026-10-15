---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AIDE2's agent-harness improvement loop as described in a frozen text capture of arXiv:2609.26457v1."
run-id: AAS-2026-10-14-2609-26457-6b3bcd4791cf-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: arxiv-2609.26457v1-2026-10-14
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  kind: capture
  identity: https://arxiv.org/abs/2609.26457
  revision: arxiv-2609.26457v1-2026-10-14
  path: /home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt
  sha256: 8bb54e9df49aa71a3e21fe27569bfa4031a9f53185c84861854e89b1f5e5d772
---

# AIDE2 boundary

## Boundary and evidence

This analysis characterizes the agent-harness improvement mechanism presented in *Recursive self-improvement of AI research agents*. Its intended use is to explain the documented design, context-management mechanisms and evaluation limits, not to certify an executable implementation. The target is in scope because model-driven research agents propose harness rewrites and evaluate the resulting agents. It is a **builder or improvement plane**, not merely a memory library: context management is one editable component of the research agent (SRC-1, captured paper §§1–2 and §3.5).

> In the inner loop, a research agent optimizes code against a measurable objective on problems drawn from a diverse set of AI R&D tasks.
> The outer loop performs a meta-level optimization over this inner-loop research process, rewriting the research agent with the objective of improving the research efficiency of the inner-loop agent.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

The functional inclusions are the documented two-loop search; generation and review of task solutions; aggregation of private evaluation scores; incumbent selection and reuse of accepted agent code; and the discovered agents' search, prompt compaction, failure-memory and robustness mechanisms. The original and human-engineered agents belong to the account in their documented roles as initial agent, outer-loop driver and comparison baseline. The reported selection trajectory, held-out evaluations, ignition test and appendices are also included, but only as author-reported design and operation (SRC-1, §§2–3, §5, appendices A–E).

> The agent then returns one solution of its own choosing, which we denote x^t\hat{x}_{t}. Which candidate to edit next, which to return, and how to structure the agent’s memory are all part of the agent’s code and are editable by the outer loop.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

External dependencies include model APIs, task codebases and public/private scoring procedures, and execution infrastructure for benchmark solutions. The paper names different models for the two loops and CPU/GPU infrastructure for held-out evaluations; those descriptions establish dependencies, not independently inspected provider or infrastructure behavior (SRC-1, §2.2 and appendix A). Model training, provider internals, benchmark implementations and the wider Weco production product are excluded. Their exclusion prevents conclusions about model-weight self-improvement, evaluator integrity beyond the paper's account, deployment guarantees or the full production agent.

The boundary kind is **complete artifact, partial loop**. The complete paper text is frozen, but no repository or executable checkout was supplied or acquired. Repository-tree coverage and shipped entry-point/consumer tracing therefore cannot be performed within this source. This is not a whole-system implementation boundary. The paper describes state production, acceptance and subsequent consumption, but does not provide inspectable code paths, full prompts, persistence/reload contracts or raw execution traces in this capture. Those gaps prevent verification of actual state lifecycles, runtime enforcement and independent reproduction. They do not prevent a bounded account of the documented mechanism.

| Captured material | Treatment and initial inspection | Limit or conclusion prevented |
|---|---|---|
| Title, abstract, introduction and method (§§1–2; algorithm 1) | Included and inspected for identity, two-loop responsibilities, grading and code reuse | Design declarations do not verify an implementation. |
| Experiments (§3), discussion (§5) | Included and inspected for reported operation, discovered context mechanisms and stated uncertainty | Aggregate author reports are not raw observed runs or independently inspected causal experiments. |
| Appendices A–E | Included and inspected for protocols, baseline roles, cross-model tests, rejected proposals and prompt-size reconstruction | No executable evaluators, raw proposal archive or complete generated harnesses are present in the captured text. |
| Related work (§4) and references | Retained in the complete capture; inspected only incidentally and by bounded link search | Cited external systems and documents are not frozen evidence for this run. |
| Figure captions and tables | Included as extracted text | Image pixels are absent; plotted values unavailable in prose/tables cannot be read from this capture. Math extraction sometimes duplicates rendered and TeX forms; exact mathematical transcription requires care. |
| arXiv navigation and rendering notices | Retained but excluded from system characterization | They carry no evidence about agent operation. |

The immutable source is `arxiv-2609.26457v1-2026-10-14`, a UTF-8 text capture derived from `https://arxiv.org/html/2609.26457v1`. HTML entities were decoded, whitespace normalized, and scripts/styles omitted. The capture header records the original HTML digest and extraction limits. The frontmatter SHA-256 pins the exact resulting capture bytes. The applicability cutoff is 2026-10-14, the supplied run date; the captured paper identifies itself as v1 dated 22 September 2026. No later revision, live page, linked repository or cited paper is part of the evidence boundary. The overall evidence tier is **doc-grounded**.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | capture | `https://arxiv.org/abs/2609.26457` | arxiv-2609.26457v1-2026-10-14 | doctrine/design; reported operation | Access file: `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`. Doctrine/design: §§1–2, algorithm 1 and §3.5. Reported operation: §§3 and 5, appendices A–E. Full paper text retained; related work/references not used for external-system conclusions. | Doctrine/design: captured §2.1 “Recursive self-improvement”, §2.2 “AIDE2”, §3.5 “The self-improved agent”. Reported operation: §§3.1–3.6, §5 “Discussion”, appendices A–E. Quotes resolve to the absolute capture path above. | No implementation checkout, full prompt templates, raw run artifacts or executable evaluator code in this capture: cannot verify execution, persistence, hidden-score isolation or reproduce outcomes. Figure images omitted: cannot extract unreported plotted values. Author-reported experiments support attributed outcomes and conditions, not independently inspected causal evidence. |
