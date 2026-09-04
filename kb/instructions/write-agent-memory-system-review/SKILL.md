---
name: write-agent-memory-system-review
description: Run only when analyse-agentic-system invokes the legacy review-publication workflow for a detected external memory, knowledge, or context-engineering system; do not select or invoke directly.
type: kb/types/instruction.md
user-invocable: false
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
argument-hint: "frozen source and candidate-publication paths from analyse-agentic-system"
---

# Write Agent Memory System Review

Generate one legacy-collection review from the source boundary frozen by
`analyse-agentic-system`. Validate a private candidate before replacing the
public review. The parent owns source scope, the destination, final publication,
and the run's success or failure.

Invocation authorizes the candidate, one public review, and workflow-owned
semantic-QA state. It does not authorize source changes, auxiliary collection
edits, comparison refreshes, landscape synthesis, or Git staging and commits.

## Inputs

Require:

- parent `AAS-*` run ID;
- selected subject and stable slug;
- `source-tier`: `code-grounded` or `doc-grounded`;
- frozen `SRC-*` register and readable source locations;
- reviewed Git commit or capture identity and citation format;
- evidence limitations;
- a candidate path inside the parent's run directory; and
- the final public path under `reviews/` for code-grounded work or
  `lightweight/` for doc-grounded work.

The public path may replace only a generated review of the same subject and
source identity. If it belongs to another source or has uncommitted local
changes, fail without changing it.

## Failure rule

A missing input, changed source boundary, drafting failure, semantic-QA
failure, or validation failure returns one concise failure to the parent. Leave
the incumbent untouched. Do not archive, restore, or maintain retry state; the
parent marks its run failed and a later analysis reruns the work.

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
5. Run `commonplace-validate <candidate-path>`. Then perform ontology and
   taxonomy QA against the type contract and run the semantic review bundle
   through `kb/instructions/run-review-batches.md`. Apply clearly valid fixes
   to the candidate and validate it again. If semantic QA cannot run, fail the
   subworkflow; do not substitute a shell-launched agent.
6. Immediately before publication, inspect the destination's frontmatter and
   `git status --short`. Confirm it is absent or is a same-subject,
   same-source review with no local modifications. Publish the exact validated
   candidate bytes in one replace operation. Do not archive the incumbent;
   Git preserves committed history.
7. Run `commonplace-validate <public-path>` and verify its source anchors. A
   successful return contains the public path and SHA-256. The candidate is no
   longer authoritative.

## Downstream comparison

A code-grounded review changes the source set for `systems.csv` and
`systems-table.md`. Refresh both only when the caller separately authorized
both paths; otherwise report the pair stale. Never hand-edit either generated
artifact. A doc-grounded review does not enter that matrix.

Refresh a current landscape synthesis only when separately commissioned with
authorized inputs and output. Otherwise report an affected synthesis as
historical. These downstream dispositions do not change whether the review
candidate itself passed.

## Report

Return the parent run ID, reused source boundary, public review path and
SHA-256, drafting mode, ontology/taxonomy QA result, semantic-QA result, final
validation result, and comparison/synthesis disposition. On failure return
only the failed operation and reason needed for a clean rerun.

## Constraints

- Never inspect or edit an incumbent's analytical body while drafting.
- Never publish a candidate that has not passed structural and semantic QA.
- Never run an agent CLI to bypass unavailable harness delegation.
- Never add `user-verified`; this workflow cannot grant human attestation.
- Never stage or commit unless the caller separately requested it.
