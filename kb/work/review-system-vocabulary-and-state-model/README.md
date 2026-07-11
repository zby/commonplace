# Review system vocabulary and state model

## Purpose

Bring the review subsystem's names and state model into one coherent vocabulary, then implement the agreed target in one sweep. The criterion-axis refactor removed the largest historical leak (`gate_path` for every assay), but exposed adjacent places where one concept has two names, one word carries two concepts, or a stored field combines states that should be distinguished.

This is now a state-model design problem, not a bulk rename. The workshop exists to settle the target before another schema change so Commonplace does not accumulate serial schema versions, transitional aliases, or compatibility code.

## Current baseline

The retained operational evidence store is at schema v5. The repository has already committed the criterion-axis direction: the generic assay axis is `criterion`, while `gate` is reserved for closed-ended, verdict-kind criteria and their catalog. That decision is recorded in [ADR 035](../../reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) and described by the [review system](../../reference/README-REVIEW-SYSTEM.md).

This workshop starts from that position. Its migration question is how to carry the retained v5 evidence into the next complete target model after the remaining vocabulary and state decisions are settled.

The remaining candidate refactors are recorded in [inventory.md](./inventory.md). They fall into two groups:

- **lexical alignment** — the model is already understood, but code and interfaces use different or overloaded names;
- **semantic alignment** — choosing the name requires deciding what states the system actually represents.

The lexical changes may be mechanically simple, but they should land with the semantic changes only after the target schema is fixed.

## Scope

In scope:

- job grouping terminology (`grouping` / `packing`);
- the overloaded use of `bundle` for both gate-catalog bundles and review-job output;
- freshness-baseline terminology currently expressed as acceptance;
- pair completion state and timestamps;
- verdict/outcome/error representation;
- stale-reason granularity, especially `missing-review`;
- conformance-source helper names;
- acknowledgement/carry-forward vocabulary if baseline terminology makes the current command unclear;
- one next target schema, Python/JSON/artifact/CLI surface, documentation update, and v5→target evidence-preservation policy.

Out of scope:

- whether review state should remain SQLite or move to an append-only source of truth — owned by [src architecture alternatives](../src-architecture-alternatives/README.md);
- the general lineage model for derived artifacts — owned by [lineage mechanisms](../lineage-mechanisms/README.md);
- prompt-quality decisions about mixing catalog bundles in one job — owned by [review bundle packing](../review-bundle-packing/README.md);
- new assay kinds, new gates, scheduling, leases, workers, or executor adapters;
- backward compatibility for external consumers. Evidence preservation for the one real review store is in scope; a general migration framework is not.

## Evaluation boundary

Judge a candidate model against these constraints:

1. **One concept, one name.** CLI, schema, Python records, JSON, manifests, protocol prose, and documentation use the same term unless they represent genuinely different layers.
2. **Names expose invariants.** A reader should be able to distinguish job grouping, pair completion, assay result, execution failure, and freshness state without loading historical explanations.
3. **Gate remains narrow.** `gate`, authored `gate_id`, `review-gates/`, and `--all-gates` continue to mean closed-ended verdict criteria, not every assay criterion.
4. **Freshness is not endorsement.** The current baseline must not imply approval, handling, or global note quality.
5. **Completion is not decision.** Verdict and report pairs both complete; only the result protocol determines whether a decision/outcome is present.
6. **Operational failure is not silently a substantive judgment.** The treatment of `ERROR` must state whether it is an assay outcome, an inability to judge, or an execution failure.
7. **Preserve paid evidence deliberately.** No real review store is deleted or transformed without a backup, version check, row-count/integrity checks, and an explicit migration path.
8. **No transitional aliases.** Once adopted, the target replaces the old surface directly.

## Evidence-preservation boundary

Treat the retained v5 store at `kb/reports/review-store.sqlite` as the migration input for this workshop. Historical migrations that produced it are complete operational history, not part of the design.

Before implementing the next schema:

- back up the v5 store;
- record its hash, schema version, table counts, acceptance count, and foreign-key status;
- decide whether the target receives a narrow in-place v5→target migration or an evidence export/import path;
- rehearse that route on a copy and repeat the integrity checks;
- retain the untouched v5 backup until the target store and its derived artifacts are verified.

Do not require an intermediate store merely because the repository passed through an intermediate schema during development. The preservation route should move from the retained v5 evidence to the final model this workshop adopts.

## Working rules

- Record adopted choices and their rejected alternatives in this workshop before editing the schema again.
- Prefer a single target schema and implementation series after the decisions converge.
- Do not mutate the real review store while exploring schema alternatives; use copies and synthetic fixtures.
- Keep historical ADR wording historical. Promote the final decision as a new ADR or a clearly scoped amendment, then update current reference and instruction surfaces.
- Keep unrelated architecture improvements out even when the refactor exposes them; record them as follow-up proposals rather than expanding this implementation.

## Expected outputs

- a resolved terminology map with no undecided generic identifiers;
- a target state model for jobs, pairs, results/errors, and freshness baselines;
- a target SQL schema and explicit old→new field/table mapping;
- a v5→target preservation plan for the retained store;
- one implementation checklist spanning code, commands, artifacts, tests, and docs;
- a durable ADR or amendment describing the adopted model;
- updated review-system reference and operating instructions.

## Closure

Close this workshop when:

1. The retained v5 store has been inventoried and backed up, and the v5→target preservation route has passed on a copy without evidence loss.
2. Every decision in [inventory.md](./inventory.md) is adopted or explicitly dropped with a reason.
3. One final target schema and migration/evidence-preservation route are fixed.
4. Code, SQL, Python APIs, JSON, manifests, protocol text, commands, tests, and current documentation implement the same model.
5. The full test suite, deterministic KB validation, schema integrity checks, and a copied-store migration rehearsal pass.
6. The durable decision is promoted to `kb/reference/adr/` or an accepted ADR amendment.
7. Any follow-up work outside scope is routed to a proposal or neighboring workshop.
8. This directory and its entry in `kb/work/README.md` are deleted.

## Grounding

- [Review system](../../reference/README-REVIEW-SYSTEM.md) — current concepts and operator surface.
- [Review architecture](../../reference/review-architecture.md) — current code and schema invariants.
- [Storage architecture](../../reference/storage-architecture.md) — current SQLite boundary.
- [ADR 035](../../reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — current job, result-kind, acceptance, and criterion-axis decision history.
- [Review bundle packing](../review-bundle-packing/README.md) — neighboring prompt-packing experiment whose quality question remains separate from terminology.
- [src architecture alternatives](../src-architecture-alternatives/README.md) — neighboring review-store source-of-truth investigation.
