# Theory rename residual audit checkpoint

## Scope and result

The source/library layout, current collection contracts, shipped skill routing,
consumer guidance and publication have changed to Theory. Generic note APIs,
`source_notes`, the note type and consumer Notes scaffolds retain their names.
The remaining old spellings cannot be classified by string replacement alone.
This checkpoint is not a claim that every historical/workshop occurrence has
received its final disposition.

## Searches performed

- Git-tracked readable text: `kb/notes`, `commonplace:notes/`, `<library>/notes/`,
  `notes/types/`, and relative `../notes/` forms. First follow-up output:
  `/tmp/theory-final-path-residuals.txt`, captured at `f698aa90d`.
- Tracked plus ignored/local Markdown, Python, YAML, JSON, JSONL, text and TSV
  under `kb/`, `src/` and `tests/`: literal `kb/notes/`, `commonplace:notes/`,
  `<library>/notes/` and `notes/types/`. Git metadata was excluded. Output:
  `/tmp/theory-final-including-local-residual-paths.txt`, after `af299464c`
  and the execution-document update. It lists 20,138 matching paths, including
  18,675 under report state and 1,056 under report cache. These are matching
  paths, not unique artifacts, broken links or authorized mutation targets.
- All 1,072 protected relocation candidates and all 516 affected ingest Quotes
  sections were checked against their checkpoint hashes. Affected ingest
  frontmatter was also compared in full. No mismatch was found. Current pinned
  analysis members have no diff from the preflight commit.
- The backed-up and current SQLite tables have identical row counts and row
  values; current integrity check is `ok`. No state rewrite is commissioned.

The tracked scan covers the root templates, CI, packaging, scripts and tests.
The local scan does not search arbitrary external consuming checkouts. Searching
an ignored capture does not authorize editing it.

## Dispositions established

| Surface | Disposition |
|---|---|
| Init templates, scaffold manifest, installed scenarios and CI consumer smoke | Keep project `kb/notes/`; do not create Theory or rename customized collections. |
| Current portable skills | Resolve collection from the explicit input or project routing; neither Notes nor Theory is an alias. |
| Upgrade instruction | Keep old namespace strings as literal search/reconciliation inputs, beside their replacements. |
| Theory's dated corpus measurements and experimental case descriptions | Keep the original observed population/path boundary. |
| ADRs, authored ingests and legacy system accounts | Relocation repaired navigation to the same artifact; retain historical findings, source identity and exact quotations. |
| Exact inputs, captured prompts/logs, experimental versions and hash-pinned members | Preserve bytes; old paths inside them are historical, not filesystem aliases. |
| Ignored state and cache | Preserve their old identities and captured contents. Do not infer eligibility or migrate state from search results. |
| Old published source keys | Keep as redirect keys; all 593 rename changes have checked emitted HTML and built targets. |
| Generic tests using Notes or arbitrary collections | Keep their original collection choices; these guard collection-independent behavior. |

The first follow-up scan found two live structured-claim drafts still naming
`notes/types/structured-claim.md`. Reading their workshop and full artifacts
confirmed that they are editable drafts, not experimental captures. Commit
`af299464c` changes their type pointers and current routing/captions in nine
workshop framings. All 11 artifacts validate. Dated lifecycle alternatives,
trial targets, captured audit rows and completed-task observations were not
mechanically relabelled.

## Remaining closeout

Review the remaining workshop/historical occurrences by artifact role, not by
parent directory or validation-ignore marker alone. In particular, distinguish
current handoffs and pending-target queues from trial inputs and dated results.
Repair any remaining current navigation or live type pointer; keep exact inputs
and historical statements. Then retain the final acceptance/disposition record,
extract any durable guidance not already in ADR 123 or the consumer upgrade
instruction, and remove this workshop and its active-list entry. Until then,
this is an implementation/verification checkpoint, not release clearance.
