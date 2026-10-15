---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Incremental self-improvement's probabilistic instruction runtime as described in the frozen revised FKI-198-94 report."
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  kind: capture
  identity: https://people.idsia.ch/~juergen/fki198-94.pdf
  revision: fki198-94-revised-1995-01-31-captured-2026-10-14-text
  path: /home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt
  sha256: c6fb513ff17ded4cd5cc3efaa3c3267ce6683d69895219674571a3be26987b5b
---

# Incremental self-improvement boundary

## Boundary and evidence

This analysis concerns the incremental self-improvement paradigm and its concrete probabilistic instruction runtime in Jürgen Schmidhuber's *On Learning How to Learn Learning Strategies*, Technical Report FKI-198-94, revised January 31, 1995. Its intended use is to explain the described action-generation, self-modification and retention loop, not to establish present-day implementation performance (SRC-1, captured text, §§2–5).

The target is an **enclosing runtime** for a reinforcement-learning agent, rather than a tool called by an unspecified agent host. It owns the repeated instruction cycle, action selection, working storage and top-level credit assignment. Its model-dependent operation uses a mutable probabilistic policy over instructions and arguments, sampled by the interpreter; no language-model API or external model provider is described. This is the basis for including this older agent-learning architecture, not a claim that it is an LLM system (SRC-1, captured text, §§3.1–3.2).

> a primitive and the corresponding arguments are chosen randomly according to the current probability
> distributions, as already described.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

The boundary kind is **complete artifact, partial loop**. The entire report's extracted text was inspected, including its algorithm, limitations, illustrative experiments and references. No repository or executable implementation was supplied. Consequently there is no repository tree or shipped entry-point/consumer trace to inspect. The report describes an implementation but is not its source code. The boundary permits a complete account of the documented design while preventing a whole-system claim about shipped execution paths, implementation fidelity or operational coverage.

| Document scope | Treatment and role | Conclusion prevented by exclusion or gap |
|---|---|---|
| Title, abstract and §§1–2 | Included: artifact identity, motivation and general paradigm | None within the documentary scope |
| §§3.1–3.2 and Table 1 | Included: instruction interpreter; program and work cells; probability initialization, sampling, introspection and modification; self-delimitation; stack saving and restoration; fixed credit-assignment strategy | No executable code is available in the capture, so actual implementation behavior is not established |
| §4 | Included: declared constraints, proposed variations, causal-attribution limits and distinctions between implemented and planned features | Proposed extensions cannot be treated as implemented |
| §§5.1–5.3 and Table 2 | Included: task interfaces, reward generation, time accounting, variable-writing and navigation experiments, reported comparisons | No raw traces, executable drivers or independent measurements are supplied; results remain reported operation |
| §§6–7 and references | Inspected: author-supplied historical context, future work and bibliography | Referenced works themselves are outside this capture; their mechanisms and results cannot be independently assessed here |

Functional inclusions cover the policy distributions, sampled primitive execution, persistent in-life work storage, environment input/output interface, self-modification programs and their probability-change history. The documented consumers of retained changes are later instruction selections, including later self-modification programs. The documented retention evaluator is the unmodifiable top-level strategy; the illustrative task environments supply inputs and reward (SRC-1, captured text, §§3–5).

> Neither storage nor environment are re-initialized
> after each run.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

External dependencies in the design are finite computing hardware and an environment providing task-specific observations, action effects and payoff. The report's experimental environments are included as documented parts of the loop, not excluded merely because they supply state. Arbitrary real-world environments, later implementations, neural-network variants mentioned as future work, cross-process persistence and deployment machinery are not supplied. This prevents conclusions about practical integration, durability across restarts, later adoption or general empirical effectiveness (SRC-1, captured text, §§3.2, 4, 5 and 6).

The frozen evidence is the exact UTF-8 text capture named in `source`, extracted with `pdftotext -layout` from the supplied PDF URL. Its capture label is `fki198-94-revised-1995-01-31-captured-2026-10-14-text`; its SHA-256 is `c6fb513ff17ded4cd5cc3efaa3c3267ce6683d69895219674571a3be26987b5b`. The downloaded PDF is retained alongside it as acquisition provenance at `sources/fki198-94.pdf`, with SHA-256 `cc153d45ebabae8e357b43a157453b4944340c48d7fb2912c394fe0eb962d06c`. The registered analytical capture is the text, not a moving URL or an implicit allowance to inspect other documents. PDF text extraction visibly degrades some ligatures, symbols and equations; ambiguous mathematical details cannot be established from damaged extraction alone.

The applicability cutoff is 2026-10-14, the supplied run date. The report's own revision date remains January 31, 1995; the cutoff does not imply evidence of any intervening development. The overall tier is **doc-grounded**. Algorithm descriptions supply doctrine/design; the experimental narrative supplies reported operation. Neither an inspectable run artifact nor an independently inspectable causal experiment is present.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | capture | `https://people.idsia.ch/~juergen/fki198-94.pdf` | fki198-94-revised-1995-01-31-captured-2026-10-14-text | doctrine/design; reported operation | doctrine/design: complete captured report, title through references, with mechanism inspection in §§2–4; reported operation: complete §5, including task definitions, self-modification-disabled comparisons and author interpretations | `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`; doctrine/design: §§2, 3.1, 3.2, Table 1, §4; reported operation: §§5.1–5.3, Table 2 | No executable implementation, raw run logs or experimental artifacts in the frozen capture: cannot establish implementation fidelity, independently observed operation, reproducibility or causal improvement beyond the author's reported comparisons. Extraction damage limits exact mathematical interpretation. Referenced works and later systems are not part of the source. |
