---
name: synthesize-agent-memory-landscape
description: Use when asked to write or refresh public cross-system analysis from the agent-memory review corpus and its generated matrix. Produces a snapshot-bound landscape synthesis; do not use Commonplace transfer scans as evidence.
type: kb/types/instruction.md
user-invocable: true
argument-hint: "[authorized public analysis path] [current or historical matrix snapshot]"
context: fork
---

# Synthesize the Agent-Memory Landscape

Produce a public, source-auditable synthesis of the agent-memory-system corpus from one pinned matrix snapshot and the ontology-normalized reviews that justify it.

## Prerequisites

- Use the output path and current-versus-historical mode supplied in `$ARGUMENTS`, the user request, or an invoking worker packet. Do not infer file-mutation authority from a request for analysis alone.
- Read `kb/agent-memory-systems/COLLECTION.md`, `kb/agent-memory-systems/types/agent-memory-system-review.md`, and `kb/agent-memory-systems/review-framework-design.md` before analysing the corpus.
- Use `kb/agent-memory-systems/systems.csv` as the quantitative source and code-grounded reviews as its qualitative support. Doc-grounded reviews may appear only in a separately labelled qualitative section.
- Require an authorized output path for publication. Without one, return the proposed synthesis in the response and do not edit the existing public analysis.
- Determine whether the requested result is current or historical. A current result requires a matrix rebuilt from the current reviews and a regenerated human table; mutate those generated artifacts only when their paths are separately authorized. Otherwise describe the exact existing matrix as a historical snapshot.

## Evidence boundary

Compute and record the matrix SHA-256, row count, source-tier population, and analysis cutoff before interpreting it. The matrix and reviews are canonical inputs. Never use `kb/reports/state/agentic-system-transfer/` or any `Comparison with Our System`, `Borrowable Ideas`, or `What to Watch` section retained in a legacy review as corpus evidence. When a complete legacy review contains those sections, ignore them. Treat its `Curiosity Pass` and concluding summary as leads only and verify any example against the source-grounded characterization, write-side, or read-back account.

The Commonplace ontology is the declared analytical lens, not a claim of perspective-free classification. Preserve two layers in qualitative examples: what the external system does in its own mechanism and why the Commonplace term fits.

Treat evidence shapes differently:

- Closed, population-complete controlled fields may support counts, proportions, and cross-tabs.
- A missing controlled value means unassessed unless the field contract explicitly gives it assessed-absent semantics.
- Open-ended mechanism observations may support named examples, variants, combinations, and ontology stress cases. They do not support prevalence claims until every member has been assayed for that concept.
- Transfer findings are local, interest-conditioned judgments and support no public corpus claim.

## Steps

1. **Pin the snapshot.** Record the matrix identity, SHA-256, row count, field definitions, and whether the build represents the current review set or an explicitly historical snapshot. Do not silently mix a newer review with an older matrix classification.
2. **Generate quantitative candidates mechanically.** Use Python's standard library or an existing repository script to compute every count, denominator, cross-tab, missingness value, and change claim from the pinned CSV. Keep a working query ledger that states the fields, filters, numerator, and denominator for each candidate. Do not tally rows manually.
3. **Select public findings.** Choose four to six findings that change how a reader understands the design space. Prefer contrasts, interactions, rare mechanisms, and evidence limits over a tour of every column. State the denominator next to every quantitative result.
4. **Ground qualitative interpretation.** For each selected finding, read the relevant complete reviews. Give representative mechanisms, a contrasting case when one materially bounds the claim, and links to the evidence-bearing reviews. Do not infer a system property from its one-line matrix description alone.
5. **Write one snapshot analysis.** Open with the evidence boundary and ontology lens. Present the selected findings, then explicit corpus and evidence limits. General implications for memory-system designers are allowed when the findings support them; Commonplace-specific recommendations belong in a transfer scan. Replace an incumbent synthesis as one coherent snapshot rather than patching counts into prose written against another population.
6. **Verify independently where authorized.** Give a fresh checker the pinned matrix, query ledger, draft, and cited review paths, but no transfer scans or writer rationale. Require it to recompute every number, verify every example against its review, check code-grounded/doc-grounded separation, and flag causal language unsupported by the data. When independent delegation is not authorized or available, rerun all quantitative queries and report that semantic verification was local.
7. **Publish and validate.** Apply supported corrections, write only the authorized analysis path plus any separately authorized generated matrix/table paths, and run `commonplace-validate` on every changed Markdown artifact.

## Report

Report the output path or response-only disposition, matrix SHA-256 and population, current-versus-historical status, quantitative-query verification, qualitative verification mode, validation result, and any finding withheld because its evidence was not population-complete.

## Verify

- The article names one matrix snapshot and never mixes populations silently.
- Every number is mechanically reproducible from the pinned CSV with an explicit denominator.
- Every qualitative example resolves to a complete review and retains the external mechanism behind the ontology mapping.
- No open-ended observation is presented as prevalence without a corpus-wide assay.
- No transfer scan or legacy Commonplace-comparison section is used as public evidence.
- Limitations distinguish code-visible wiring, observed operation, activation, and causal effect.
- The published artifact is coherent as a replacement snapshot and passes deterministic validation.
