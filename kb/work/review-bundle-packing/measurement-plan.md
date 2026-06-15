# Review Bundle Packing Measurement Plan

## Measurement goal

Determine when packing more gates into one review prompt stops being efficient and starts damaging review quality or reliability.

The main comparison is:

- **Bundle-local:** one note, one bundle/lens, one review run.
- **Cross-bundle:** one note, multiple bundles or all gates, one review run.

The expected policy is bundle-local unless measurements show a safe exception.

## Prompt-size measurements

Measure prompt size before running any model:

- characters
- approximate tokens
- target note body tokens
- gate definition tokens
- resolved-link table tokens
- output-template tokens
- expected output tokens by gate count

Cases:

| Case | Shape | Purpose |
|---|---|---|
| A | one note x `complexity` | small bundle baseline |
| B | one note x `prose` | large bundle baseline |
| C | one note x `semantic` | link-following-heavy baseline |
| D | one note x all bundles | accidental worst case |
| E | one gate x 5 notes | gate-sweep comparison |

Use at least three notes:

- short/simple note
- medium current note
- long note with several links

## Reliability measurements

For each shape, collect:

- runner return code
- parser success/failure
- missing pair count
- duplicate pair count
- wall-clock duration
- telemetry model partition
- input/output/reasoning tokens when available
- number of WARN findings
- number of obviously duplicated or generic findings

The output should distinguish:

- **mechanical failure**: subprocess failure, parser failure, missing blocks
- **focus failure**: shallow reviews, repeated boilerplate, missed obvious gate failures
- **economic failure**: prompt too large or too slow for routine review work

## Quality checks

Use review output only after manual inspection. Count-based metrics are not enough.

For a sampled note, compare bundle-local and cross-bundle outputs:

- Did cross-bundle review miss WARNs found by bundle-local review?
- Did cross-bundle review produce more generic findings?
- Did findings cite the right gate failure mode?
- Did semantic gates follow the required linked neighborhood, or did attention collapse into local-only review?
- Did accessibility/sentence gates get worse when semantic/prose gates were present in the same prompt?

## Script behavior questions

Questions to answer before patching:

1. Should `commonplace-run-review-bundle note prose semantic` split into two review runs, or reject mixed bundle/lens input?
2. Should `commonplace-create-review-run --with-prompt` reject mixed bundle/lens input because its JSON response is single-run/single-output-path?
3. Should explicit gate ids from the same lens be allowed in one run?
4. Should explicit gate ids from different lenses be rejected unless an opt-in flag is provided?
5. Should `commonplace-review-sweep --all-gates` ignore current acceptances from mixed runs when deciding whether bundle-local runs exist?

## Candidate invariants

Strict invariant:

- A single review run may include only gates whose ids share the same first path segment, such as `prose/*`.
- `--all-gates` always means multiple bundle-local runs, never one all-gates run.
- Mixed-lens input is a CLI error unless a future explicit experimental flag exists.

Split invariant:

- `commonplace-run-review-bundle` may accept mixed bundle arguments but splits them into one run per lens.
- `commonplace-create-review-run --with-prompt` rejects mixed lenses because one call returns one prompt and one output path.
- Internal batch/orchestrator APIs may still prepare arbitrary note-gate pairs when they own the multi-run output artifact.

The workshop should decide between these after measurement, not before.

## Notes from the motivating incident

On 2026-06-15, an all-bundles review was run for `kb/notes/llm-generation-relaxes-goals-where-human-writing-stalls.md` in a single prompt. The command completed and persisted 36 current acceptances under the actual `gpt-5-5-high` partition, but it demonstrated that the current CLI permits cross-bundle packing without making that choice explicit.

An interrupted follow-up complexity-only command completed as a separate four-gate run, which shows bundle-local execution still works. The workshop should not treat those historical rows as data quality problems; they are useful evidence about command behavior.
