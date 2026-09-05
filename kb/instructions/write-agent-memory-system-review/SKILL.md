---
name: write-agent-memory-system-review
description: Run only when analyse-agentic-system invokes the legacy review-publication workflow for a detected external memory, knowledge, or context-engineering system; do not select or invoke directly.
type: kb/types/instruction.md
user-invocable: false
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
argument-hint: "frozen source, candidate path, and intended destination from analyse-agentic-system"
---

# Write Agent Memory System Review

Draft one legacy-collection review candidate from the source boundary frozen by
`analyse-agentic-system`. The parent owns source scope, semantic review,
destination validation, publication, downstream reporting, and the run's
status.

Invocation authorizes only the candidate inside the parent run directory. It
does not authorize a public review, review-system state, source changes,
auxiliary collection edits, comparison refreshes, landscape synthesis, or Git
staging and commits.

## Inputs

Require:

- parent `AAS-*` run ID;
- selected subject and stable slug;
- `source-tier`: `code-grounded` or `doc-grounded`;
- frozen `SRC-*` register and readable source locations;
- reviewed Git commit or capture identity and citation format;
- evidence limitations;
- a candidate path inside the parent's run directory;
- the final public path under `reviews/` for code-grounded work or
  `lightweight/` for doc-grounded work.

The final path determines relative type and link resolution. Do not inspect its
incumbent; the parent publication operation owns that check.

## Failure rule

A missing input, changed source boundary, or drafting failure returns one
concise failure to the parent. Leave the incumbent untouched. The parent
decides whether to correct the running run or abandon it.

## Steps

1. Verify every source location against the parent's register and revision.
   Do not acquire, refresh, widen, or mutate sources. A code-grounded review
   needs commit-pinned source-file anchors. A doc-grounded review needs
   identified and dated or versioned document anchors.
2. Read, in order:
   - `kb/agent-memory-systems/COLLECTION.md`;
   - `kb/agent-memory-systems/types/agent-memory-system-review.md`; and
   - one or two current reviews from the same evidence tier for style only.
3. Draft the candidate from the frozen primary sources. A fresh worker may
   draft when the harness supplies one; otherwise draft locally. Give a worker
   only the parent run, frozen sources, selected subject, type contract,
   candidate path, and the constraints below. It may write only the candidate,
   must not publish or delegate, and must ignore any automatically rediscovered
   publication skill.
4. Preserve the external mechanism in native terms before applying
   Commonplace ontology. Complete the artifact-analysis, write-side,
   read-back, curiosity, citation, and controlled-token requirements in the
   type contract. Keep evidence limitations next to the claims they limit.
   Do not add a Commonplace comparison, borrowable ideas, transfer
   recommendations, or watch items.
5. Add exact workflow frontmatter fields `generated-by:
   analyse-agentic-system`, `analysis-run`, `source-identity`, and
   `reviewed-revision`. Check the draft against the type's ontology and taxonomy
   requirements. Do not run semantic review or publish. The parent validates
   these bytes as the intended destination.

## Report

Return the parent run ID, reused source boundary, candidate path and SHA-256,
drafting mode, ontology/taxonomy QA result, and material limitations. On
failure return only the failed operation and reason needed for correction.

## Constraints

- Never inspect or edit an incumbent's analytical body while drafting.
- Never inspect or write the public destination or review-system state.
- Never run an agent CLI to bypass unavailable harness delegation.
- Never add `user-verified`; this workflow cannot grant human attestation.
- Never stage or commit unless the caller separately requested it.
