---
name: synthesize-agent-memory-landscape
description: Use when asked to write or refresh a public cross-system synthesis from retained analyse-agentic-system results and their memory-comparison fields. Produces one snapshot-bound analysis; excludes legacy reviews and Commonplace transfer scans.
type: kb/types/instruction.md
user-invocable: true
argument-hint: "[public analysis path or response] [selected main reviews] [current or historical]"
context: fork
---

# Synthesize the agent-memory landscape

Produce a public comparison whose numbers and qualitative findings come from
one frozen population of main-analysis results.

## Inputs and authority

Use the requested output, selected systems, and current or historical mode from
the user request or invoking packet. A request to refresh a named artifact
supplies its output authority. Without a file destination, return the synthesis
in the response. Load the output collection's contract before writing there.

The evidence inputs are generated reviews under `kb/agentic-systems/reviews/`
and the exact retained results named by their `analysis-result` paths and
`analysis-result-sha256` values. Read the full retained results for findings:
source register, shared records, memory/context lens, reconciliation, and limits.
The compact review supplies publication identity and navigation. It cannot
replace a missing full result or comparison assessment.

Use `kb/types/agentic-system-analysis-result.md` for the `memory-comparison`
contract. Each row preserves its source revision, run, analysis cutoff, evidence
tier, compared memory boundary, and per-axis assessment, basis, values, and
canonical records. No legacy review, old CSV, transfer scan, or newly acquired
source may supply or repair a finding. Missing required inputs block the
selected population; report the main-analysis regeneration needed. Existing
results must not be hand-patched to make a comparison pass.

## Freeze the evidence

1. **Select the population.** Default a refresh to current inputs. Repeat
   `--review` to select the commissioned main reviews; omit it only when the
   commission covers all generated main reviews. Record the selection rule and
   exclusions. Select one review per source identity. A small selected set is
   a bounded comparison, with no implication of historical-corpus coverage.
2. **Create a new bundle.** Run from the repository root:

   ```bash
   uv run python scripts/bundle_agentic_landscape.py prepare --output <new-bundle-directory> --review <main-review-path>
   ```

   Repeat `--review` as needed. Add `--ontology <kb/notes/path.md>` for each
   additional ontology artifact actually used. The command reads main results
   directly, derives `matrix.csv`, and captures the exact review/result bytes,
   result contracts, reader code, producing and consuming instructions, and
   dependency declarations under their repository-relative paths. It writes
   `snapshot.json` and a canonical `MANIFEST.tsv` containing sorted
   `sha256<TAB>byte-length<TAB>path` rows. Require exit status zero and save the
   reported manifest hash outside the bundle before interpretation. Existing
   bundle directories are never replaced. The command does not update public
   matrix or table files.
3. **Use only bundled evidence.** Treat the bundle as immutable. If a needed
   finding or ontology input is absent, create a new complete bundle before
   drafting; do not mix in live files. For an existing historical bundle,
   verify it with its previously recorded manifest hash and use its bundled
   instruction and contracts. A method mismatch requires the matching pinned
   checkout. Legacy-corpus snapshots remain historical evidence, but this
   procedure does not rebuild or merge them into its population.

A temporary bundle suffices for a response or workshop trial. Before publishing,
ensure the exact bundle and every cited original retained result are kept in
Git, or identify a repository revision containing every input byte. A commit ID
alone is insufficient when an input differs from that revision. Record the
manifest hash, matrix hash, input file identities, and the reconstructable
revision or retained-snapshot location in the published evidence boundary.
A tracked comparison must remain auditable without ignored local run state.

## Analyse and write

4. **Compute quantitative candidates.** Query the bundled CSV mechanically,
   decoding value cells as JSON arrays. For implementation/operation counts,
   use code-grounded rows with `known` values at `wired`, `observed`, or
   `causally supported` basis, plus `absent` assessments for evidenced negatives.
   Keep claimed and afforded findings separate. Keep doc-grounded findings in
   a separate qualitative section. Within each query, report inapplicable,
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
5. **Read and ground the mechanisms.** For each selected finding, read the full
   bundled result and the cited canonical records, including their source
   evidence and limitations. Preserve the external mechanism and explain why
   the Commonplace term fits. Trace every qualitative example to a result path,
   hash, run ID, canonical IDs, and supporting section. Open-ended observations
   support named examples and contrasts, never prevalence from omitted mentions.
   Keep static wiring, observed use, contextual activation, and causal effect
   distinct. Withhold claims stronger than their records support.
6. **Write one coherent snapshot.** State the evidence identity, selection,
   source-tier population, source cutoffs, and analytical lens. Select only
   findings that the available population supports; do not pad a small pilot
   into a landscape survey. Give denominators beside numbers and scope beside
   comparisons. Link qualitative claims to their original retained result
   paths, using a section anchor where useful; compact reviews may additionally
   serve navigation. Do not cite the temporary bundle path. Name withheld
   conclusions and evidence gaps. Commonplace-specific recommendations belong
   in a separately commissioned transfer scan. Replace an incumbent synthesis
   as a complete snapshot, never by updating counts alone.
7. **Verify the draft.** Recompute every query from bundled bytes and check each
   example against its full result and records. If independent review is
   commissioned, give the checker the frozen bundle and expected hash, query
   ledger, and draft, without live corpus paths, transfer scans, or writer
   rationale. Otherwise perform these checks locally and report that mode.
8. **Recheck and publish.** Immediately before returning or writing, run:

   ```bash
   uv run python scripts/bundle_agentic_landscape.py verify <bundle-directory> --sha256 <recorded-manifest-hash> --source-root .
   ```

   For a historical snapshot, omit `--source-root`; always keep the externally
   recorded hash. The command checks the manifest, captured bytes, and exact
   matrix/result agreement. For current inputs it also checks source-file drift
   and population changes, including additions to an all-generated selection.
   On failure, withhold the draft and restart from selection. Write the
   commissioned output only after verification and evidence retention are
   satisfied; run `commonplace-validate` on every changed Markdown artifact.
   Public matrix/table refresh is a separate output: when commissioned, pass
   the identical explicit review list to both existing build scripts and check
   their recorded input identities against this bundle.

## Report

Return the output path or response-only disposition; current or historical
status; selection rule and source-tier population; cutoffs; manifest and matrix
hashes; reconstructable evidence location; query verification and semantic
verification mode; final bundle/source recheck; validation; and withheld claims.
A fixture trial establishes procedure behavior, not external-system findings or
production corpus coverage.
