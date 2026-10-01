# Agentic analysis layout migration, 2026-10-01

This record supports verification and recovery of the collection ownership
migration. It establishes that the method and report locations changed without
new analytical judgments. The operator authorized implementation on 2026-10-01.
The baseline is commit `7ee3521c3456c4675f02a0b896469da58566ba9f`.

The migration moves 108 files through 22 directory, document and schema-sidecar
mappings. The collection owns eight type/schema pairs, including the existing
generated-review pair. Python commands remain packaged. The current population
contains one published set; 72 archive files include exact payloads and their
policy metadata. There are 42 archived review pins, all checked against the
preserved historical bytes.

## Transformation and byte pins

[The mapping](./mapping.json) records old/new paths and SHA-256 values. Raw
tracked inputs are recoverable with `git show <base-commit>:<old-path>`. Local
pre-migration copies remain in
`/tmp/commonplace-agentic-localization-baseline/` until acceptance completes.

For the current set, change only the frontmatter type identity, preserving
YAML quoting. Preserve already-correct intra-set link spellings; all five
current member bodies stay byte-identical. Relocation rebases review links
whose destination changes. Recompute each member hash in
`ARTIFACT.yaml`, then its manifest pin in the generated review. Rewrite the
review's retained path and relative citations. The copied complete run's output
bytes equal the migrated retained bytes; its run state receives the new type,
output path, manifest hash and review hash.

Compare each member's frontmatter excluding only `type`. Compare bodies after
resolving relative links through the declared path map. Require unchanged
source identity and revision, boundary, evidence assessments, record and run IDs,
comparison fields and historical `inputs-commit`. Materialize all proposed bytes
in disposable copies before applying them. No source refresh, target execution
or new analysis is part of this migration.

Archived payload and manifest bytes keep their historical types. Update only
archived reviews' pin paths and navigation links. Their pins still verify against
the same hashes. Archive README and validation markers describe this disposition;
current readers do not select these archives. Commit-bound comparison snapshots
retain their original inputs commit, hashes and findings.

## Local state and concurrent run

The baseline inventory includes 96 ignored state directories. Copy the completed
published `AAS-2026-10-01-instinctual-memory-07` run for explicit validation at the
new location. Keep its intermediate reports and engine receipts unchanged as
recovery evidence; do not resume them under the new method. Other ignored runs
remain at their original location with their original bytes. Their individual
dispositions are recorded in the mapping. Old ignored state is not a cache and
is not deleted by this migration.

Implementation and checks use the `localize-agentic-analysis` branch in
`/home/zby/llm/commonplace-agentic-localization`, with a separate editable uv tool
under `/tmp/commonplace-agentic-localization-tools/`. The shared tool imports
`/home/zby/llm/commonplace/src/commonplace/` even from another worktree; a Git
worktree does not isolate that implementation. The concurrent Luna run in
`/home/zby/.codex/worktrees/b9ad/commonplace` was blocked before analysis because
its pinned-source checkout was missing. The corrected acquisition method must
be committed in the invoking worktree before opening a fresh run. A historical
run must retain its opening method and use an isolated tool at that method.
The operator authorized collection-layout cutover into the shared checkout.
If additional outputs are adopted, inventory and migrate them
under the same bounded transformation before cutover; never rewrite their
method commits.

## Consumer change packet

1. **Declaration.** ADR 099 and the collection contract declare ownership;
   local type specs, schemas and Python constants enforce the new identities.
2. **Scope.** Analysis, landscape synthesis and taxonomy maintenance are
   collection-specific. Generic instruction/type contracts and base schemas
   stay global. Ordinary local-type eligibility is unchanged.
3. **Consumers.** [Search inventory](./search-inventory.json) records eight
   literal searches over baseline tracked files and ignored state. Adapted
   classes are emitters, set/run-state readers, validators, schema references,
   publication method/output boundaries, comparison readers, worker input
   contracts, trial tooling, skill projections, collection/routing rules,
   navigation, article/legacy-collection citation rules, site exclusions/redirects,
   package and initialization consumers,
   and tests. Exact APIs and transformed literals are in the implementing diff.
4. **Pins.** Five current members, their manifest, generated review and completed
   working outputs are re-pinned. All 42 historical review pins retain their
   original hashes and resolve at the new archive path. Historical synthesis
   provenance is not presented as a pin to new current bytes.
5. **Spellings.** The migration covers quoted/unquoted YAML types, schema
   constants and relative references, Python strings and composed Path values,
   repository-relative paths, Markdown targets and illustrative code paths.
   Frozen quotations and historical path examples remain witnesses.
6. **Projections.** Both runtimes retain the two moved skill names through four
   updated symlinks. The build hook excludes the research collection and
   rewrites shipped links to it using the existing external-link rule. Site
   publication excludes state and admits only retained analysis members.
7. **Fresh install.** The wheel retains generic skills, instruction/type
   contracts and base schemas; analysis and landscape documents and stubs are
   absent. A fresh scratch project validates its landing pages and generic note.
8. **Existing installs.** Initialization preserves an old ignored run-state
   capture. Its retired global type fails explicit validation, as expected:
   init performs no implicit data migration. Generic content validates, and
   a second init leaves both scratch projects byte-identical. Source clones
   receive the path changes and skill projections through Git.
9. **Diagnostics.** Scripted publication rejects changed method inputs,
   invalid evidence and replacement failures while preserving the incumbent.
   Explicit completed-state validation verifies frozen source and exact output
   hashes. Archive/state exclusions apply only to sweeps, not selected runs.
10. **Acceptance.** Commands and results appear below and in the package probe.
11. **Drift guard.** Tests discover every local type/schema and shared analysis
    contract, require method pin coverage, exclude changing outputs, check both
    runtime projections, and verify the real packaged library's research
    exclusion. No test hardcodes today's number of local types.
12. **Historical witnesses.** Exact archives, old-method ignored state, retained
    research captures, dated proposal observations, historical comparisons and
    workshop examples retain their
    producing layouts. ADRs 083, 084 and 087 name their applicable amendments.
    Redirect sources and this mapping deliberately record old identities.
13. **Conventional identity.** Only `AAS-<date>-<slug>-<nn>` directories are
    analysis runs. The migration report uses a distinct directory name. There
    are no resolver aliases and no accidental current-analysis populations.
14. **Shared exclusions.** Current readers select generated main reviews and
    their retained sets. Type-contract integrity tests use the validator's
    shared Markdown iterator, so archived old contracts remain historical.
15. **Relocation effects.** Relocation was committed separately. Re-run type,
    collection, publication and byte-pin checks after adapting consumers. Every
    changed current pin and each preserved historical pin is recorded here.

## Acceptance evidence

[Acceptance receipts](./acceptance.json) retain check results and log hashes.
[Operational rescan](./operational-rescan.json) records the zero-match live
consumer searches and the explicit historical dispositions.

- Focused workflow/publication checks: 201 passed before final drift guards.
- Instruction composition, runtime projections, package boundaries and site
  publication checks: 17 passed. Type-contract integrity checks: 10 passed.
- Full Python suite: 1,232 passed, including acquisition of a missing checkout
  at a requested commit older than the clone's default HEAD.
- `uv run ruff check .`: passed. Retained source captures are excluded from
  linting rather than edited; two frozen import-order findings remain exact.
- `commonplace-validate kb/agentic-systems`: passed without warnings or failures;
  archived captures and local state are explicitly excluded from the sweep.
- Explicit current `ARTIFACT.yaml` set, generated review and complete run-state
  validation: passed.
- [Comparison check](./comparison-check.json): one code-grounded row before and
  after, with identical populations, axes, evidence and supporting records.
  Only `review_sha256`, `artifact_file` and `artifact_sha256` change.
- [Package probe](./package-probe.json): build through sdist, direct wheel build,
  isolated wheel installation, fresh/existing init, repeat-init byte equality,
  generic validation and preserved legacy-state diagnosis passed. No relocated
  research documentation is shipped.
- Operational rescan: live code, procedures, schemas and contracts have no retired
  dependency. Historical witnesses above and redirect sources are retained.
- Redirect validation found an existing redirect that shadowed the newly
  regenerated instinctual-memory review. Remove that stale redirect so the live
  page is served. Maintain redirects for 96 moved published Markdown files.
  Publication does not retire stale site redirects automatically; corpus-refresh
  adoption must run `commonplace-validate redirects` after reinstating reviews.
