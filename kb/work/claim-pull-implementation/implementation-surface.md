# Claim-pull implementation surface

## Durable additions

| Target | Purpose |
|---|---|
| `kb/reference/adr/NNN-untracked-source-snapshots-require-ingest-grounding.md` | Promote the draft decision after implementation |
| `kb/instructions/ground-source-dependent-claims.md` | Promote the append-only grounding instruction |
| `src/commonplace/review/source_conformance.py` | Define the virtual `source` lens and wrapper |

## Amendments

| Target | Change |
|---|---|
| `kb/sources/COLLECTION.md` | Distinguish external authority from the tracked Claims record |
| `kb/sources/types/ingest-report.md` | Specify Claims shape, append-only grounding, and refresh preservation |
| `kb/sources/types/ingest-report.schema.yaml` | Require one Claims heading |
| `kb/instructions/draft-ingest-report.md` | Retain supplied Claims during refresh |
| `kb/instructions/cp-skill-ingest/SKILL.md` | Keep name-derived pairing; own deterministic Claims-only append, refresh preservation, validation, and ordinary failure restore |
| `kb/instructions/re-ingest.md` | Resolve the name-paired snapshot, gate changed observations, and audit inbound uses after success |
| `kb/instructions/cp-skill-write/SKILL.md` | Add the bounded Claims guard and literal refusal route |
| `src/commonplace/review/paths.py` | Recognize ingest criteria and `source/...` IDs |
| `src/commonplace/review/review_target_selector.py` | Derive source pairs from resolved ingest links |
| `src/commonplace/cli/review/create_review_jobs.py` | Accept dynamic source pairs |
| Review prompt/batch helpers | Apply the fixed source-consistency wrapper and worst-use verdict contract |
| Review-system references and factored-pairs proposal | Document source-as-gate adoption |
| Tracked `kb/sources/*.ingest.md` | Add the canonical empty section |

The existing scaffold already ships instructions, source types, and both
promoted skills. No manifest, build-metadata, database-schema, quote-verifier,
or multistage-writer change is expected.

## Test ownership

The separate test workstream covers name pairing and checksum mismatch,
re-ingest preservation and rejection, append-only claim addition, writer
reuse/refusal without dispatch, migration, source-pair derivation and
freshness, fresh installation, and the retained semantic cases.
