# Worked case: `storage-architecture.md`

Executed 2026-08-24. The fifth artifact taken through the full disposition
procedure.

## Result

**Minimized around authority and lifecycle across representations.** The page
remains the place that says which artifacts are canonical, reconstructable,
regenerable, stateful, or merely derived. It no longer catalogues the installed
directory tree, type resolution, generated-site mechanics, commands, migration
state, or the SQLite schema.

The edit reduced the page from 8,256 bytes to 6,680 bytes. Its line count rose
from 94 to 113 because the retained distinctions are wrapped and the role map
is explicit; the exact implementation inventories and their maintenance
obligations are gone.

## Consumption events and dispositions

| Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Maintenance form | Disposition | Retrieval path |
|---|---|---|---|---|---|---|---|---|
| Authored-directory inventory | What is installed under `kb/`? | exact | duplicate | scaffold source and `architecture.md` | seven-row table | live scaffold plus focused architecture | omit | `architecture.md`; scaffold source |
| Type-pointer resolution | How is an artifact's type loaded? | exact | duplicate | validator plus focused type reference | one paragraph | stronger focused reference | consolidate | `collections-and-types.md` |
| Cross-representation role map | Which copy is authoritative, derived, local, or stateful? | architectural | distributed | multiple packages, configs, ADRs, and instructions | implicit across six sections | authored synthesis | keep and make explicit | storage role table |
| Version-control boundary | Does correctness or freshness depend on Git history? | architectural | distributed choice boundary | command behavior plus ADRs 032 and 039 | two paragraphs | authored synthesis beside storage authority | keep and compress | file-authority section |
| Source ingest versus snapshot | Which artifact owns external-source identity? | architectural | recoverable only by combining contracts | ingest type, snapshot skill, ADR 072 | one paragraph | authored role boundary linked to stronger owners | keep and compress | reconstructable-source section |
| Generated-index and site inventory | What exactly is built and excluded? | operational exactness | duplicate | ProperDocs config and focused site reference | table plus config paragraph | live config plus focused reference | omit exact mechanics | `documentation-site.md`; `properdocs.yml` |
| Report lifecycle | Can a missing report be regenerated? | architectural | mixed | connect producer, review artifacts, report ADRs, full-pass type and instruction | two paragraphs | authored distinction among views, evidence, and state | keep and sharpen | derived/stateful section |
| SQLite paths, migration warning, and schema table | What database objects and migration state exist now? | exact | recoverable; table already incomplete | `store.py`, `store-schema.sql`, migrations | path paragraph plus six-row table | executable source | omit | live store source and SQL resource |
| Database authority boundary | What state belongs in SQLite rather than authored files? | architectural | distributed | store, freshness, review finalization, ADRs | several implementation paragraphs | authored synthesis | keep and compress | operational-database section |
| Status, selection, integrity, and pruning behavior | What do current operations do? | exact | recoverable | command help and owning symbols | one dense paragraph | help and live source | omit | command help; freshness/review source |

## Recovery and drift experiment

Task-vocabulary searches for `store`, `schema`, `COMMONPLACE_STORE`, and the
documented table names selected `commonplace.store` and its packaged SQL
resource directly. Those two units answer exact path, migration, schema, and
integrity questions without reading a prose approximation first.

The old table claimed to inventory the operational store but listed six
tables. The live `EXPECTED_TABLES` set requires seven:
`freshness_target_generations` had been added without entering this page. That
omission did not make the page broadly stale—the role boundaries still held—but
it showed that exact schema cataloguing imposed a separate obligation while
remaining insufficient for exact consumers.

The old page also repeated the retained legacy-store migration warning and a
dense list of status, selector, integrity, and pruning behaviors. All are
recoverable from small, vocabulary-selected source units and still required
source inspection for safe operational use.

## Why the document survives

No one executable unit answers whether an ignored artifact is a disposable
cache, a reconstructable source copy, retained evidence, or a packet that owns
unresolved state. That answer composes the ingest authority decision, the
generated-index decision, the report contracts, full-pass resolution, and the
freshness/review database boundary. The comparison also corrected a tempting
overgeneralization: generated review result files retain judgment bodies that
SQLite does not store, so “generated” and “ignored” do not mean “regenerable.”

The retained page makes that relation explicit in one table, then records the
two consequential exceptions: Git history is useful but not correctness state,
and SQLite is canonical only for scoped operational state. This saves repeated
cross-subsystem reconstruction without pretending to be the exact interface of
any subsystem.

## Maintenance form

The page now names semantic triggers. It needs review when authority or
lifecycle moves between storage roles. A new directory, schema table, column,
store version, command, or build flag does not trigger it by itself. Exact
changes remain visible through scaffold source, configuration, command help,
and executable schema ownership.

## Next

[The `architecture.md` worked case](./worked-case-architecture.md) retained the
installed topology as approximate orientation, but removed its duplicate role
table and installer manual. Exact scaffold membership now routes to
`commonplace.scaffold_manifest`.
