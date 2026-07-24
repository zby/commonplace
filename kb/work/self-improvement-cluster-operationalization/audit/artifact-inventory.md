# Phase-1 artifact inventory and coverage map

Inventory taken 2026-07-23. Counts include documentation and schema files because they alter an agent's available behavior or constrain generated artifacts. Files sharing one consumer and force are audited as a family; exceptions appear in the analytic reports.

## Authority and routing

| Surface | Files | Consumer / channel | Force | Report |
|---|---|---|---|---|
| Root agent contract | `AGENTS.md`, `AGENTS.md.template`, `AGENTS.reader.md`, `CLAUDE.md` | Agents load root instructions; template/init regenerates project variants | Default behavior and routing authority | [authority-and-authoring](./authority-and-authoring.md) |
| Collection contracts | `kb/agent-memory-systems/COLLECTION.md`, `kb/agentic-systems/COLLECTION.md`, `kb/instructions/COLLECTION.md`, `kb/notes/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/sources/COLLECTION.md`, `kb/work/COLLECTION.md`, `kb/work/dialectical-sample/COLLECTION.md` | Agents entering a collection; validators where a rule is mechanically encoded | Local normative contract | [authority-and-authoring](./authority-and-authoring.md) |
| Scaffolded collection contracts | `src/commonplace/_data/templates/user-{instructions,notes,reference}-COLLECTION.md` | `commonplace-init` | Retained defaults for new projects | [authority-and-authoring](./authority-and-authoring.md) |

## Type and schema authority

All 16 files under `kb/types/` were covered: the `definition`, `index`, `instruction`, `note`, `review-gate`, `tag-readme`, `text`, and `type-spec` Markdown specifications and their associated YAML schemas, including the shared note-base schema. Their consumers are the type resolver, deterministic validator, review criterion resolver, and authoring agents. Markdown carries semantic intent; YAML supplies executable shape constraints. See [validation-freshness-and-code](./validation-freshness-and-code.md).

## Instruction authority

The 81 files under `kb/instructions/` divide into these behavior surfaces:

- Twelve promoted skill entry points: `cp-skill-connect`, `cp-skill-convert`, `cp-skill-health-check`, `cp-skill-ingest`, `cp-skill-revise-autoreason`, `cp-skill-revise-iterative`, `cp-skill-snapshot-web`, `cp-skill-validate`, `cp-skill-write`, `evaluate-scenarios`, `roughdraft-review`, and `write-agent-memory-system-review`.
- Review orchestration and lifecycle: `run-review-batches`, `review-triage`, `critique-note`, `verify-review-quote-grounding`, `migrate-semantics-preserving-gate-changes`, `refresh-agent-memory-review-taxonomy`, and `composition-friction-gate`.
- Full-pass and revision workflows: `run-full-improvement-pass-on-note`, `resolve-full-pass-disposition`, `revise-note`, `run-compression-bundle-on-note`, and the four compression gates plus bundle README.
- Fix subsystem: `FIX-SYSTEM`, `fix-review-warnings`, `fix-review-warnings-sweep`, `fix-descriptions`, and `fix-strategy-taxonomy`.
- Authoring, ingestion, and maintenance: `write-instruction`, `evaluate-log-entry-for-note-creation`, `ingest-directory`, `re-ingest`, `maintain-curated-indexes`, `invert-solution-shaped-requests`, and `example-onboard-second-brain`.
- Thirty-eight catalog review gates: accessibility (4), complexity (4), frontmatter (5), prose (9), semantic (7), sentence (6), and structural (3).
- `README.md` and `COLLECTION.md`, which route and constrain the family.

Instructions are direct procedural authority only when selected. Gate files are criterion authority consumed by prompt construction and review jobs. Their semantic judgments are not deterministic validation. See [authority-and-authoring](./authority-and-authoring.md) and [review-and-fix-loop](./review-and-fix-loop.md).

## Executable behavior

All 90 files under `src/commonplace/` were covered by subsystem:

- Validation and parsing: `lib/validation.py`, `type_resolver.py`, `frontmatter.py`, `note_parser.py`, `quote_verification.py`, naming/index helpers, and `cli/validate_notes.py` / `verify_quotes.py`.
- Review search and evidence: `review/` criterion resolution, target selection, prompt/protocol, job creation, batch handling, parsing, finalization, acknowledgement, conformance checks, model normalization, DB access, and warn selection; matching `cli/review/` adapters.
- Freshness bookkeeping: `freshness/` keys, models, revisions, baselines, selector, snapshots, status, integrity, transitions, and versioning; matching freshness CLI commands.
- Guarded change operations: relocation, promotion candidates, full-pass report guard, snapshot acquisition, initialization, and their CLI adapters.
- Retained state and scaffolding: `store.py`, `store-schema.sql`, `scaffold_manifest.py`, migrations, and `_data/templates/`.
- Documentation and extraction support: `docs/`, `lib/extraction/`, project paths, systems matrix, and package initializers.

The audit treats CLI adapters and their libraries as one behavior surface unless an adapter changes force—for example, an explicit `accept`, `ack`, `retire`, relocation, or initialization command. See [validation-freshness-and-code](./validation-freshness-and-code.md).

## Repository evidence artifacts

The report schemas and README contracts under `kb/reports/` were inspected where they are consumers or outputs of the audited workflows: full-pass, connect, critique, reviews, promotion candidates, and link vocabulary. No populated review store or fix-report corpus exists in this checkout.
