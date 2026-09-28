---
name: synthesize-agent-memory-landscape
description: Use when asked to write or refresh a public cross-system synthesis from retained analyse-agentic-system sets and their memory-comparison fields. Produces one commit-bound analysis; excludes legacy reviews and Commonplace transfer scans.
type: types/instruction.md
user-invocable: true
argument-hint: "[public analysis path or response] [selected main reviews] [current or historical]"
context: fork
---

# Synthesize the agent-memory landscape

Produce a public comparison whose numbers and qualitative findings come from
one frozen population of analysis sets, identified by one commit.

## Inputs and authority

Use the requested output, selected systems, and current or historical mode from
the user request or invoking packet. A request to refresh a named artifact
supplies its output authority. Without a file destination, return the synthesis
in the response. Load the output collection's contract before writing there.

The evidence inputs are generated reviews under `kb/agentic-systems/reviews/`
and the retained sets their `analysis-artifact` paths and
`analysis-artifact-sha256` values pin under
`kb/reports/retained/agentic-system-analysis/<run-id>/`. Each set is four
members: the overview holds the boundary, source register, reconciliation,
synthesis and limitations; `runtime.md` the runtime account and the records
the runtime pass declared; `memory.md` the memory findings, memory-declared
records and the `memory-comparison` profile; `epistemic.md` the epistemic
blocks. Validate the artifact directory before reading its members. The compact review
supplies publication identity and navigation. It cannot replace a missing
member or comparison assessment.

Use `kb/types/agent-memory-analysis-report.md` for the `memory-comparison`
contract and `kb/types/agentic-system-analysis-overview.md` for the set's
identity and conventions. Each matrix row preserves its source revision, run,
analysis cutoff, evidence tier, compared memory boundary, and per-axis
coverage assessment, values, per-value evidence, and canonical records. No
legacy review, old CSV, transfer scan, or newly acquired source may supply or
repair a finding. Missing required inputs block the selected population;
report the main-analysis regeneration needed. Existing sets must not be
hand-patched to make a comparison pass.

## Freeze the evidence

1. **Select the population.** Default a refresh to current inputs. Repeat
   `--review` to select the commissioned main reviews; omit it only when the
   commission covers all generated main reviews. Record the selection rule and
   exclusions. Select one review per source identity. A small selected set is
   a bounded comparison, with no implication of historical-corpus coverage.
2. **Record the inputs commit.** Every selected review and retained set, the
   two contracts above, the reader code under `src/commonplace/lib/` and
   `scripts/`, and this instruction must be committed and unchanged in the
   worktree: `git status --porcelain -- <those paths>` prints nothing. Record
   `git rev-parse HEAD` as the inputs commit. A dirty input blocks the
   synthesis: commit it under its own authority or drop it from the selection
   with a new commit; never read an uncommitted finding. Build the matrix
   from the same selection into a temporary path, never over the public
   comparison files:

   ```bash
   uv run python scripts/build_systems_matrix.py --review <main-review-path> --output <temporary-matrix.csv>
   ```

   Repeat `--review` as needed. Require exit status zero and record the
   matrix file's SHA-256 beside the inputs commit before interpretation.
3. **Use only committed evidence.** Read members and the matrix as they are at
   the inputs commit. If a needed finding is absent, obtain it through a new
   analysis run and a new commit, then restart from selection; do not mix in
   uncommitted files. For a historical synthesis, check out or `git show` the
   recorded commit and use its contracts and instruction. A method mismatch
   between that commit and the current one requires the matching checkout.
   Legacy-corpus snapshots remain historical evidence, but this procedure
   does not rebuild or merge them into its population.

The inputs commit is the reconstructable evidence location: it holds every
input byte, the contracts and the reader code. Record it, the selection rule
and the matrix hash in the published evidence boundary. A tracked comparison
must remain auditable without ignored local run state.

## Analyse and write

4. **Compute quantitative candidates.** Query the matrix CSV mechanically,
   decoding value cells as JSON arrays. For implementation/operation counts,
   decode `<axis>_evidence` as a JSON object and use code-grounded values at
   `wired`, `observed`, or `causally supported` basis. Both `known` and
   `partial` coverage can support positive membership. Use `absent` assessments
   for evidenced negatives; omitted values and weaker evidence are not negatives.
   Complete-set distributions and set-equality queries require `known` coverage
   and strong evidence for every member, without filtering away weak members.
   Keep claimed and afforded findings separate. Keep doc-grounded findings in
   a separate qualitative section. Within each query, report partial, inapplicable,
   uninspected, and not-determinable rows separately; none is an observed
   negative. A structurally valid unknown does not block unrelated findings.

   Retain an executable query and its output in a working query ledger. Each
   candidate names the fields, value-membership or set-equality test, tier and
   basis filters, numerator, denominator, included run IDs, and exclusions.
   Count each system once per query even when its value set contains several
   stores or routes. An assessed-subset proportion must name that subset;
   a whole-population prevalence claim requires complete applicable assessment.
   A change claim requires two verified snapshots, comparable scopes/contracts,
   and an explicit treatment of population changes.
5. **Read and ground the mechanisms.** For each selected finding, read the
   members that hold it and the cited canonical records, including their
   source evidence and limitations. Preserve the external mechanism and
   explain why the Commonplace term fits. Trace every qualitative example to a
   member path, the overview hash, run ID, canonical IDs, and supporting
   section. Open-ended observations
   support named examples and contrasts, never prevalence from omitted mentions.
   Keep static wiring, observed use, contextual activation, and causal effect
   distinct. Withhold claims stronger than their records support.
   Budget the aggregate output of batched reads as well as each command. Check
   delivered output for truncation and reread omitted spans in smaller calls;
   requested line ranges and zero exit status do not establish full reading.
6. **Write one coherent snapshot.** State the evidence identity, selection,
   source-tier population, source cutoffs, and analytical lens. Select only
   findings that the available population supports; do not pad a small pilot
   into a landscape survey. Give denominators beside numbers and scope beside
   comparisons. Link qualitative claims to their retained member paths, using
   a section anchor where useful; compact reviews may additionally serve
   navigation. Do not cite the temporary matrix path. Name withheld
   conclusions and evidence gaps. Commonplace-specific recommendations belong
   in a separately commissioned transfer scan. Replace an incumbent synthesis
   as a complete snapshot, never by updating counts alone.
7. **Verify the draft.** Recompute every query from the matrix and check each
   example against its members and records. If independent review is
   commissioned, give the checker the inputs commit, the matrix hash, the
   query ledger, and the draft, without transfer scans or writer rationale.
   Otherwise perform these checks locally and report that mode.
8. **Recheck and publish.** Immediately before returning or writing, confirm
   that `git rev-parse HEAD` still equals the inputs commit or that
   `git diff --quiet <inputs-commit> HEAD -- <input paths>` succeeds, that
   `git status --porcelain -- <input paths>` prints nothing, and that
   rebuilding the matrix from the same selection reproduces the recorded
   hash. For an all-generated selection, also confirm that no review was
   added under `kb/agentic-systems/reviews/` since the inputs commit. On any
   failure, withhold the draft and restart from selection. Write the
   commissioned output only after these checks pass; run
   `commonplace-validate` on every changed Markdown artifact. Public
   matrix/table refresh is a separate output: when commissioned, pass the
   identical explicit review list to both existing build scripts and check
   their recorded input identities against the inputs commit.

## Report

Return the output path or response-only disposition; current or historical
status; selection rule and source-tier population; cutoffs; the inputs commit
and matrix hash; query verification and semantic verification mode; the final
commit and worktree recheck; validation; and withheld claims.
A fixture trial establishes procedure behavior, not external-system findings or
production corpus coverage.
