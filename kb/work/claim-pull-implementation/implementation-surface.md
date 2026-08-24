# Claim-pull implementation surface

## Durable additions

| Target | Purpose |
|---|---|
| `kb/reference/adr/NNN-untracked-source-snapshots-require-ingest-grounding.md` | Promote the draft decision after implementation |
| `kb/instructions/ground-source-dependent-claims.md` | Promote the append-only grounding instruction |
| `src/commonplace/review/source_conformance.py` | Own `source` request/path identities, ingest-link applicability, and the mechanical source-conformance wrapper |

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
| `kb/instructions/cp-skill-write-multistage/SKILL.md` | Apply the same guard to `candidate.md` before promotion and retain a blocked workshop |
| `src/commonplace/review/paths.py` | Recognize ingest criteria and `source/...` IDs |
| `src/commonplace/review/resolve_criteria.py` | Pass through source requests and include `source` in the shared `--all-gates` expansion |
| `src/commonplace/review/review_target_selector.py` | Derive source pairs from resolved ingest links |
| `src/commonplace/cli/review/review_target_selector.py` | Document source requests and the expanded `--all-gates` behavior |
| `src/commonplace/cli/review/create_review_jobs.py` | Accept dynamic source pairs |
| `src/commonplace/review/protocol/prompt.py` | Render the mechanical source wrapper while embedding the raw ingest as criterion text |
| Trivial-ack CLI/help and tests | Select source pairs consistently but skip them because they declare no `watches:` |
| Review-system references, run-batches instruction, and factored-pairs proposal | Document source-as-gate adoption, selector scope, and wrapper-upgrade semantics |
| Tracked `kb/sources/*.ingest.md` | Add the canonical empty section |

The existing scaffold already ships instructions, source types, and both
promoted writer skills. No manifest, build-metadata, database-schema,
quote-verifier, review-root configuration, or freshness-version change is
expected.

## Test ownership

The separate test workstream covers:

- name pairing, checksum mismatch, changed-observation approval, and populated
  Claims rejection;
- verified backup creation, exact same-checksum Claims preservation, primary
  and repair failures, final byte restoration, and backup cleanup;
- append-only claim addition with no worker dispatch;
- ordinary-writer reuse/refusal before save and multistage reuse/refusal before
  promotion;
- structural migration and fresh installation;
- `source` and `source/<slug>` resolution, stored-path rendering,
  `--all-gates`, selector derivation/deduplication, explicit note scopes outside
  the default scan roots, and create-jobs applicability revalidation;
- raw-ingest freshness on artifact and ingest changes, prompt rendering,
  adjacent and mixed uses, and trivial-ack exclusion; and
- the retained semantic cases in `claims-shape-evidence.md`.
