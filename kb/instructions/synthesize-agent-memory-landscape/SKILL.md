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
- Determine whether the requested result is current or historical. A current result requires a matrix rebuilt from the current reviews with `flags: 0` and a human table regenerated from those exact matrix bytes; mutate those generated artifacts only when their paths are separately authorized. Otherwise describe an exact existing matrix as historical only when its matching review and ontology inputs and zero-flag build status can also be reconstructed.
- A published result requires an immutable input boundary: either one repository revision that contains the exact matrix, row-linked reviews, type/schema, parser, and ontology inputs, or an authorized retained snapshot containing those bytes. If neither exists, return response-only and report that publication lacks a reconstructable evidence boundary.

## Evidence boundary

Before interpreting the corpus, materialize a read-only evidence bundle in a temporary directory. Include the exact matrix; every code-grounded review named by its rows; `kb/agent-memory-systems/COLLECTION.md`; the review type, schema, and framework-design note; `src/commonplace/lib/systems_matrix.py`; `scripts/build_systems_matrix.py`; `kb/instructions/synthesize-agent-memory-landscape/SKILL.md`; and every additional ontology artifact used in the analysis. Create a newline-terminated canonical manifest sorted by repository-relative path, with one `sha256<TAB>byte-length<TAB>repository-relative-path` row per input, then record the manifest SHA-256, matrix SHA-256, row count, source-tier population, repository revision or retained-snapshot identity, and analysis cutoff. Use only the bundled bytes for analysis and checking. Record each cited review's SHA-256 in the published evidence boundary so qualitative examples remain auditable without treating the combined manifest digest as a file list.

The matrix and bundled reviews are canonical inputs. Never use `kb/reports/state/agentic-system-transfer/` or any `Comparison with Our System`, `Borrowable Ideas`, or `What to Watch` section retained in a legacy review as corpus evidence. When a complete legacy review contains those sections, ignore them. Treat its `Curiosity Pass` and concluding summary as leads only and verify any example against the source-grounded characterization, write-side, or read-back account.

The Commonplace ontology is the declared analytical lens, not a claim of perspective-free classification. Preserve two layers in qualitative examples: what the external system does in its own mechanism and why the Commonplace term fits.

Treat evidence shapes differently:

- Closed, population-complete controlled fields may support counts, proportions, and cross-tabs.
- A missing controlled value means unassessed unless the field contract explicitly gives it assessed-absent semantics.
- Open-ended mechanism observations may support named examples, variants, combinations, and ontology stress cases. They do not support prevalence claims until every member has been assayed for that concept.
- Transfer findings are local, interest-conditioned judgments and support no public corpus claim.

## Steps

1. **Prove the build is usable.** For a current result, rebuild the matrix, capture the build report, and stop before analysis unless it says `flags: 0`; then regenerate the human table from those bytes. For a historical result, require a contemporaneous zero-flag build report or rerun the parser against the matching pinned reviews and require zero flags. A flagged field is unresolved input, not a warning the writer may work around or omit from selected findings.
2. **Pin the complete snapshot.** Build the temporary bundle and canonical manifest described above. Confirm every matrix `review_file` resolves exactly once inside it, the row count equals the code-grounded review population, and the matrix, reviews, and ontology inputs share the recorded revision or retained-snapshot identity. Do not silently mix a newer review or field contract with an older matrix classification.
3. **Generate quantitative candidates mechanically.** Use Python's standard library or an existing repository script against the bundled CSV to compute every count, denominator, cross-tab, missingness value, and change claim. Keep a working query ledger that states the fields, filters, numerator, and denominator for each candidate. Do not tally rows manually.
4. **Select public findings.** Choose four to six findings that change how a reader understands the design space. Prefer contrasts, interactions, rare mechanisms, and evidence limits over a tour of every column. State the denominator next to every quantitative result.
5. **Ground qualitative interpretation.** For each selected finding, read the relevant complete review from the bundle. Give representative mechanisms, a contrasting case when one materially bounds the claim, and links to the evidence-bearing reviews. Do not infer a system property from its one-line matrix description alone.
6. **Write one snapshot analysis.** Open with the complete evidence identity: matrix and manifest SHA-256 values, population, zero-flag build status, review/ontology revision or retained snapshot, cited-review hashes, cutoff, and ontology lens. Present the selected findings, then explicit corpus and evidence limits. General implications for memory-system designers are allowed when the findings support them; Commonplace-specific recommendations belong in a transfer scan. Replace an incumbent synthesis as one coherent snapshot rather than patching counts into prose written against another population.
7. **Verify independently where authorized.** Give a fresh checker the frozen bundle, query ledger, and draft, but no live corpus paths, transfer scans, or writer rationale. Require it to recompute every number, verify every example against the bundled review, check code-grounded/doc-grounded separation, and flag causal language unsupported by the data. When independent delegation is not authorized or available, rerun all quantitative queries against the bundle and report that semantic verification was local.
8. **Recheck, publish, and validate.** Immediately before writing, recompute the live or retained-snapshot manifest and require it to equal the pinned manifest. If any input drifted, discard the draft and restart from step 1. Apply supported corrections, write only the authorized analysis path plus any separately authorized generated matrix/table paths, and run `commonplace-validate` on every changed Markdown artifact.

## Report

Report the output path or response-only disposition; matrix and manifest SHA-256 values; population; zero-flag build result; review/ontology revision or retained-snapshot identity; current-versus-historical status; quantitative-query verification; qualitative verification mode; final manifest recheck; validation result; and any finding withheld because its evidence was not population-complete.

## Verify

- The article names one reconstructable matrix, review, and ontology snapshot and never mixes revisions silently.
- The matrix build has zero flags; unresolved controlled fields block synthesis.
- Every number is mechanically reproducible from the pinned CSV with an explicit denominator.
- Every qualitative example resolves to a hash-identified bundled review and retains the external mechanism behind the ontology mapping.
- No open-ended observation is presented as prevalence without a corpus-wide assay.
- No transfer scan or legacy Commonplace-comparison section is used as public evidence.
- Limitations distinguish code-visible wiring, observed operation, activation, and causal effect.
- The final manifest recheck matches the analysis bundle.
- The published artifact is coherent as a replacement snapshot and passes deterministic validation.
