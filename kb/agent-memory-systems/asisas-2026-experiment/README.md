# ASISAS-2026 Agent-Memory Corpus Experiment

This directory is the frozen corpus artifact for the ASISAS-2026 paper revision of "Where It Lives Is Not What It Is." It snapshots the agent-memory-system reviews, comparison matrix, review type contract, Karpathy LLM Wiki gist source evidence, and local rebuild scripts used for the paper's corpus counts.

The living survey remains in `kb/agent-memory-systems/`. This directory is a citable experiment snapshot.

## Data

- [`systems.csv`](./systems.csv) - frozen machine-readable matrix, 141 code-grounded review rows.
- [`systems-table.md`](./systems-table.md) - frozen human-readable table derived from the matrix.
- [`reviews/`](./reviews/) - frozen per-system code-grounded reviews.
- [`types/`](./types/) - frozen copy of the review type contract and schema used by the reviews; relative links and schema refs are adjusted to resolve from this experiment directory.
- [`karpathy-gist-agent-memory-reproducible-core.md`](./karpathy-gist-agent-memory-reproducible-core.md) - consolidated 51-member Karpathy LLM Wiki gist core.
- [`karpathy-gist-comments-2026-06-18.json`](./karpathy-gist-comments-2026-06-18.json) - raw gist comment API snapshot used as source evidence for the core.

## Review Provenance

Each review records the external system revision it inspected before the main sections:

- `**Repository:**` names the inspected source repository.
- `**Reviewed commit:**` or `**Reviewed revision:**` pins the external source state used for the code-grounded claims.
- `last-checked` in frontmatter records the date the source was inspected.

All 141 frozen reviews have a reviewed external commit or revision. That field is about the reviewed system, not this Commonplace repository.

The reviews were generated under the Commonplace agent-memory review workflow: the review type contract copied into [`types/agent-memory-system-review.md`](./types/agent-memory-system-review.md), source-grounded review writing, deterministic validation, semantic review gates where applied, and collection navigation/linking machinery such as the connect workflow. The copied type spec is the main reusable instruction artifact for review production; the broader system-definition artifacts live in the Commonplace repository, not in each review.

For citation, the corpus must also be pinned to a Commonplace release tag or commit. Until the release is cut, treat the Commonplace generation snapshot as pending:

```text
Commonplace release tag: TODO
Commonplace commit: TODO
Zenodo DOI: TODO
```

Once the release is cut, replace the TODOs above. That release is the authoritative snapshot of the generation machinery: review instructions, semantic gates, validators, scripts, and skills.

## Field Operationalization

The matrix does not infer artifact classes directly from filenames, languages, or storage locations. Reviews classify the behavior-shaping **operative parts** of each system, then the matrix parser lifts explicit lead tokens from the frozen review text.

For representational form, reviewers use:

- `prose` when the operative part is natural-language content interpreted by a model or human.
- `symbolic` when the operative part has assigned, inspectable consequences in the system: code, commands, schemas, manifests, route tables, validators, typed fields, tests, configuration keys, or Markdown structures that a consumer treats as binding structure. This is an architectural use of "symbolic," not a claim about classical symbolic AI; the distinction is operative semantics, not syntax.
- `parametric` when behavior is carried by numerical model-derived state such as embeddings, dense indexes, adapters, checkpoints, learned rankers, reward models, or controllers.

Bundled artifacts can carry several forms at once. For example, a skill package can be `prose` guidance plus a `symbolic` manifest and tests, and a retrieval package can be `prose` records plus `parametric` embeddings. The review records all applicable tokens in the `**Representational form:**` lead line; the parser one-hot encodes those authored tokens into `form_prose`, `form_symbolic`, and `form_parametric`.

Under this broad operationalization, `form_symbolic` is saturated in the frozen code-grounded corpus: every reviewed system has some symbolic operative part. That does **not** mean every system is primarily symbolic, uses symbolic AI, or promotes retained lessons into symbolic control. It means all reviewed software systems expose at least one behavior-shaping structure with assigned consequences. For the paper's aggregate table, the discriminating representational-form result is therefore "no distributed-parametric form" (`form_parametric == 0`), not "has symbolic form."

## Provenance Limitation

The 141 reviews were authored across multiple Commonplace revisions. Review instructions, semantic review gates, validators, and connection workflows evolved during that period. We did not rerun every review under one final instruction version for this paper artifact.

For this experiment, the frozen review texts are the corpus. The matrix is generated from explicit lead-token fields in those frozen texts, and the reported aggregate counts use coarse fields (`storage_substrate`, `form_parametric`, `read_back_direction`, `auth_enforcement` / `auth_validation`, and `trace_derived`) that were normalized before publication. The expected impact of instruction drift is therefore on review prose depth and auxiliary links, not on the headline aggregate variables. Remaining risk is recorded as corpus-construction bias rather than a field-wide estimate.

## Rebuild Scope

Use the experiment-local builder for this frozen matrix:

```bash
python3 kb/agent-memory-systems/asisas-2026-experiment/scripts/build_systems_matrix.py
```

It reads only this experiment directory and writes only `./systems.csv`. Use the root `scripts/build_systems_matrix.py` for the living survey matrix.
