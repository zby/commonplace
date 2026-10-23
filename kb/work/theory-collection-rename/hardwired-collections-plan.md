# Remove hardwired collection assumptions from runtime operations

## Intent and commission

The operator requested this separate implementation plan after directing that
runtime code should be collection-independent. The result is for an
implementer removing collection-name assumptions before the Theory rename.
The operator subsequently confirmed that collection-type work was complete
and authorized removal. Track 1 is implemented below. Content migration,
accepted-policy changes and other agents' files remain outside this authority.

A [collection](../../reference/definitions/collection.md) is a `COLLECTION.md`-
bearing subtree under `kb/`. Its directory name identifies its location, not
its eligibility for validation, promotion, review or a special lifecycle rule.
Generic operations should consume resolved targets and declared contracts.
Ordinary collection discovery does not assign system roles. The reserved
names and existing path-based policies documented below are intentional
exceptions, not generic operation defaults.

Success means the affected operations work with unrelated collection names,
including a consuming KB with neither Notes nor Theory. It does **not** mean
removing every directory literal from the repository. Build manifests,
explicit type identities, tool-owned output paths and this site's selected
layout answer different questions and need different treatment.

This plan owns the runtime-independence workstream. The
[rename implementation inventory](./implementation-plan.md) owns the directory,
backlink, scaffold and publication migration. Its old-code TSVs remain useful
locators, not prescriptions to replace Notes-specific identifiers with
Theory-specific ones. No collection relocation is part of this workstream.

## Execution status

Track 1 is implemented against completed collection-type commits `3c9f97761`
and `98c5efbf8`. No content, scaffold, collection-contract spec, state store or
retained evidence was migrated. The generic `notes_validation` API field is
retained; it now reports an explicit scope rather than a named collection.

Chosen route from Gates A–C: require explicit scope instead of inventing
implicit eligibility or new collection metadata.

| Operation | Implemented interface and behavior |
|---|---|
| Validation | Collection names use generic resolution. `commonplace-validate today --collection NAME_OR_PATH` (also `recent`) uses validation-aware enumeration and retains structure/ignore checks. Drill-down commands preserve that scope. |
| Status | `commonplace-status --collection NAME_OR_PATH` scopes notes validation only. `notes_validation.scope` and lifecycle `scope` identify their separate domains; optional review status retains project scope. |
| Promotion | `commonplace-promotion-candidates NAME_OR_PATH`; reports go to `kb/reports/cache/promotion-candidates/<collection-relative-path>/report.md`. Distinct scopes do not overwrite each other and links derive from actual paths. Validation-ignored captures are excluded. |
| Review and trivial acknowledgement | Explicit `--note` targets are required. `--user-verified` filters that scope and is no longer mutually exclusive with it. Directory expansion stays top-level-only, excludes typed collection contracts, and refuses validation-ignored directory sweeps; explicit file inspection remains possible. |

The Notes-only path helper and fixed Notes/Reference review-root tuple are
removed. Tests cover arbitrary/namespaced collections, a KB with neither
Notes nor Theory, scoped source links, omitted/invalid targets, contract
exclusion, ignored captures and acknowledgement refusal without targets.

Verification: before changes, `uv run pytest -m ''` passed **1,391 tests**;
after changes the same full suite passed **1,418 tests**. The intermediate
selected general/review/indexing/validation suite passed 442 tests before the
last drill-down regression was added. `uv run ruff check .` and
`git diff --check` passed. Final Markdown validation is recorded in the task
handoff, not represented as a runtime-suite result.

### Final runtime integration verification

After ADR 122, the first full integration run reported 1,408 passes and 14
analysis-workflow failures. The new collection-policy read made
`types/COLLECTION.md` a dependency of pinned type-spec validation, but the
workflow's captured criteria did not include it. Commit `59464f3ac` closes the
capture over governing collection contracts and their type/schema dependencies.
It preserves fail-closed validation; no live-file fallback was added.

Three new regressions in
`tests/commonplace/agentic_analysis/test_criteria_collection_closure.py` cover
arbitrary/namespaced governing collections, immutable captured policy after a
live edit, and exclusion of unrelated collections. The initial implementation
failed two of those tests; the corrected implementation passes them.

Final coverage with the fix and lifecycle warning:

- `uv run pytest -m ''`: **1,425 passed**, including the slow workflow tests.
- General, agentic-analysis and validation suites with `-m 'not slow'`:
  **715 passed, 112 deselected**.
- `uv run ruff check .` and `git diff --check`: passed.
- All four changed workshop Markdown files: deterministic validation passed
  without warnings or failures.

Commit `e47ce02c2` adds the pending-design warning to
`src/commonplace/lib/lifecycle_validation.py`, without changing behavior.
The runtime workstream is complete for the agreed scope. This is not evidence
that the collection rename, packaging changes or consumer migration have run.
The evidence-splitting agent owns the content prerequisite; inventories remain
pre-sort baseline evidence and must not be refreshed until its handoff.

### Adopted Track 2 dispositions

The operator directed this work to systematize the current system, allowing
bounded consistency fixes rather than speculative redesign. Work, Tasks and
proposal lifecycle modeling are excluded from this workshop. Preserve existing
checks; do not infer an adopted task/mailbox workflow from scaffold or code.
The lifecycle module carries an all-caps warning that overall design is pending:
these bounded checks are neither a broader lifecycle architecture nor a
backward-compatibility requirement without an explicit design decision.

ADR 122 is the adopted consistency fix: the collection contract now owns the
unquoted-source bound. Other Track 2 policies retain current behavior. No
portable type-binding mechanism, root configuration or additional role registry
is needed. Reopen a design only for a concrete inconsistency or consumer need.

| Finding | Current disposition and return trigger |
|---|---|
| Exact local type-rule binding (2A) | Retain canonical type-path dispatch for the remaining type rules. The unquoted-source bound left it: the collection contract's `unquoted-source-limit` field now selects where it applies, set in Notes and Articles ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md), operator decision 2026-10-23). No other type rule names a Notes-local type, so the rename needs no registration update. |
| Source-root/pin handling (2B) | Operator decision: reserve `sources` at `kb/sources/`, with no root configuration. Retain its source-recognition, snapshot/cache and grounding rules; root generalization is out of scope. Reopen only through a new operator decision if another location is needed. |
| Workshop eligibility/archive/lifecycle roots (2C) | Explicitly out of scope by operator decision. Leave Work's type exception, the proposal archive guard and Work/Tasks lifecycle scans unchanged. Retain their named path dependencies as exceptions to this refactor; lifecycle modeling belongs to separate work when the operator reopens it. |
| Tag root and site policy (2D) | Operator decision: reserve `tags` at `kb/tags/`, required even when empty, with no root configuration. Retain centrally declared participation and no per-collection namespace selection. Root generalization is out of scope unless a new operator decision reopens it. Preserve the existing publication boundary; site layout stays separately owned. |

Track 1 is committed as `43a98d836`; special-role documentation is in
`94c0f71f7`, and ADR 122's source-bound implementation is in `daed61d59`.
The runtime design questions are resolved. The Theory rename needs no source
bound registration edit, but its preservation and consumer/state migration
choices remain separate. Another agent owns the evidence split. Do not edit
that agent's evidence-sort file, move content or refresh the pre-sort inventories
before its completed handoff.

## Parallel ownership: binding coordination boundary

The other agent completed the collection-contract type and its application to
collection specs/templates. Do not edit that agent's contracts, schemas,
templates or related validation code without an explicit ownership handoff.
The implementer does not acquire those files merely because this plan lists
them as dependencies.

The final [`collection-contract` type](../../types/collection-contract.md) and
[its schema](../../types/collection-contract.schema.yaml) define a type for
`COLLECTION.md`, an optional description and `participating` for the tag
collection. Unlike the initial inspection's draft, the completed change
**requires** that type on every contract; validation checks it without treating
the contract as collection content. Structural collection lookup still uses
the `COLLECTION.md` boundary, while validation enforces its type. ADR 122 adds the specific `unquoted-source-limit` quality-standard field.
The type does not define a universal operation-eligibility registry, publication
policy or portable imperative-rule bindings. Schema acceptance of extra keys
does not make invented keys meaningful.

Before implementing any shared boundary/type behavior:

1. Obtain the other agent's completed contract and exact file ownership or
   commit boundary. Re-read the final type/schema and affected tests; these
   observations describe in-flight files, not a frozen API.
2. Record which files each implementer may write. Serialize changes to
   `project_paths.py`, `type_resolver.py`, `validation.py`, shared fixtures,
   collection-contract specs and collection templates when ownership overlaps.
3. Resolve any needed declaration with the contract owner. Do not start a
   second collection-spec schema or infer roles from the new `type:` value:
   every typed collection uses that same value.
4. Keep unrelated working-tree changes intact. Use targeted patches and
   explicit-file commits. At integration, review both branches' behavior,
   not just whether Git reports a textual conflict.

Read-only investigation and tests authored in an agreed disjoint new file may
proceed before handoff. Changes to shared production files wait for ownership.
No agent launches, mailbox posts, migration runs or freezes are commissioned
by this document. Coordinate a freeze with the rename owner before either
workstream moves paths.

## Inspection boundary

Inspected repository HEAD: `1191fbfa19a003e392509f044dcdafc613b8a267`, plus the
concurrent uncommitted collection-spec changes described above. Locations below
are search anchors from that inspection, not line numbers guaranteed after
parallel edits. Reopen the named regions before editing; do not redo an
unbounded repository scan.

The bounded survey covered collection-root literals and collection-name atoms
under `src/commonplace/`, generic path/type discovery, validation dispatch,
source/snapshot paths, tag discovery, lifecycle checks and site policies.
It distinguishes executable coupling from help examples and generic terms
such as `notes_by_tag`, `source_notes` and `note_path`. It is not a survey of
outside consuming projects or permission to rewrite retained evidence.

## Architecture boundary

### Reuse existing mechanisms

`src/commonplace/lib/project_paths.py` already provides:

- `collection_dirs`: discovers visible `COLLECTION.md`-bearing collections,
  including collections under a non-collection namespace directory.
- `collection_for_path`: resolves the owning collection.
- `list_collection_note_paths`: generic note enumeration, not identical to
  validation enumeration.
- `list_collection_validation_paths` and `validation_ignored_dirs`: validation
  scope, including directory artifacts and ignore-marker boundaries.
- `list_kb_note_paths`: collection-wide note enumeration. Do not use it as a
  universal substitute for every operation's eligibility policy.

`validate_notes.py:resolve_validation_target` already resolves arbitrary
collection names and paths. `collection_conformance.py` already resolves
collection criteria from the supplied collection-relative path. Reuse these
paths instead of creating a second collection finder.

### Keep three decisions separate

1. **Discovery:** where are the declared collections?
2. **Scope/eligibility:** which targets did this invocation request, and which
   artifacts may this operation consume there?
3. **Semantics:** what rule applies to a resolved artifact/type or a declared
   operational role?

Never replace a fixed tuple with “all discovered collections” without settling
steps 2 and 3. That can pull exact captures, local state, archived material or
procedures into operations previously scoped to ordinary content. Validation
ignore markers do not automatically define review or promotion policy.

### Special collections and reserved names

The operator chose to make special collections explicit: reserved collection
names identify defined system roles rather than acting as undocumented defaults
in generic operations. On 2026-10-23 the operator widened the set to every
collection whose fixed name commands rely on: `tags`, `sources`, `reports`,
`work`, `types` and `agentic-system-analyses`, as the
[special collection definition](../../reference/definitions/special-collection.md)
records. They have fixed locations under `kb/` and no root configuration or
alias mechanism. The table below covers the first two, which this survey
examined in detail. Do not add configurable special-collection locations as part of this
work. The agreed cases are:

| Reserved KB-relative name | System role |
|---|---|
| `sources` | Tracked source ingests and their snapshot/cache and grounding rules, at `kb/sources/`. |
| `tags` | Required in every KB, even with no tag heads or members. Holds the KB's single tag namespace, its heads and central participation declaration at `kb/tags/`. Member collections do not select independent tag namespaces. |

These roles do not make every collection special or authorize a wider scan.
Generic validation, promotion and review still use their explicit input scopes.
The [collections and types reference](../../reference/collections-and-types.md#special-collections)
defines this distinction and points to the existing collection contracts for
allowed content and scope. This workshop retains the implementation survey,
not a second configuration schema.
The operator decided that every KB has a Tags collection, even when empty;
init already seeds its contract and landing without heads. This requirement
does not imply the same existence requirement for every other reserved name.
Missing/invalid Tags diagnostics still need to be specified by the durable
contract; this decision record does not change current validation behavior.

Work's staging exception and archive policy remain existing path conventions
in 2C, without new declarations or relocation support.
Tasks is an operational location that need not be a collection. Installed
framework addresses and tool-owned output locations are also distinct from
reserved content-collection roles; do not combine them into an inferred role
registry.

### Prefer explicit inputs before persistent configuration

The minimum route is to pass resolved scope into generic library functions and
expose it at their command boundary. Require an explicit scope where no safe
implicit policy has been approved. An omitted scope must not select Notes,
Theory, the first discovered collection or every collection by accident.

Do not add a global role registry, plugin system, arbitrary Python rule loader,
collection-name alias table or settings file just to avoid passing an input.
If a reusable automatic policy is needed, establish its consumer and contract
with the collection-spec owner before adding it. Path-valued inputs must stay
inside the intended KB boundary unless an existing explicit-file interface
already permits otherwise; do not unintentionally change that interface.

## Adopted decisions and change boundaries

The operator chose explicit scopes for generic operations and preservation of
current semantic policies. The table records those decisions and the boundary
that requires reopening one; it is not a list of unanswered design questions.

| Gate | Adopted route | Reopen before |
|---|---|---|
| A. Invocation scopes | Implemented: required collection inputs for promotion, validation status and `today`/`recent`; required explicit `--note` review scope with optional user-verification filter. | Changing CLI signatures, status JSON or selection scope. |
| B. Implicit policy | Do not invent eligibility from directory names, frontmatter type alone, or broad discovery. If automatic defaults are required, agree their declarations and missing/invalid behavior with the collection-spec owner. | Before the first implicit multi-collection scan. |
| C. Public interfaces | Implemented: generic `notes_validation` field with explicit scope; scoped promotion output paths and path-derived links; no Theory-only roots, helpers or status fields. | Introducing another public interface or changing actual scope. |
| D. Special role policies | Retain reserved Tags/Sources roots and current Work, archive, lifecycle and site policies. No new root configuration or declarations. | Changing an existing special-case guarantee or its location. |
| E. Type applicability | Retain canonical type identity for type rules. The unquoted-source bound is attached by the collection contract instead ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md)); the Theory contract carries it through the rename. Test that the relocated contract still binds and an unrelated collection does not. | Introducing a further rule-attachment mechanism or changing another rule's applicability. |
| F. Completion scope | Track 1 removes generic operation defaults. Track 2 records intentional policies; not every path literal must disappear. Preserve all checks through the rename. | Claiming arbitrary relocation support for the retained special paths. |

These decisions close the runtime design work, not the relocation commission.
A new requirement must name the affected files and concrete inconsistency or
consumer need. Do not reopen settled gates simply because an intentional fixed
path remains. Generic operation independence does not claim arbitrary relocation
support for every system location.

## Track 1 — Generic content operations

This track is implemented in `43a98d836`, before changing the collection layout.
The original file-level worklist below is retained for traceability, not as
instructions to implement the same refactor again. The execution-status table
above states the actual APIs. It required no new collection metadata.

| Production file and original inspection anchor | Completed change / boundary |
|---|---|
| `src/commonplace/lib/project_paths.py:list_notes_collection_paths` | Remove this collection-specific convenience helper after its callers use the appropriate generic enumerator. Keep collection discovery filename-based and compatible with both typed and frontmatter-free contracts unless the contract owner's accepted design changes that rule. |
| `src/commonplace/cli/validate_notes.py:resolve_validation_target` | Remove the `arg == "notes"` branch; ordinary collection resolution handles Notes, Theory or any other name. Reserved operation targets such as `types`, `landings`, `redirects` and `lifecycle` are command grammar, not evidence that every collection must have those names. Preserve an explicit path route for name collisions. |
| `src/commonplace/cli/validate_notes.py` — `today` / `recent` | Replace the Notes-only helper with the approved scope input and validation-aware enumeration. Preserve date/time semantics, ignored subtrees, directory-artifact behavior and explicit-target behavior; document any deliberate difference. |
| `src/commonplace/lib/project_status.py:load_notes_validation_status`, `ProjectStatus`, `_actions`, `load_project_status` | Validate supplied scope rather than `kb/notes`; keep per-collection structure findings correctly anchored. Derive details commands and counts from that scope. Choose the neutral status shape at Gate C; do not silently sum errors into a success. |
| `src/commonplace/cli/status.py` | Accept/report the agreed validation scope and render the generic status result. Preserve existing Git, review and lifecycle status responsibilities. Report unavailable/omitted components accurately rather than implicitly treating them as successful. |
| `src/commonplace/lib/promotion.py:write_promotion_candidates_report` | Accept a resolved collection target; remove `root / "kb" / "notes"`. Preserve candidate/exclusion/ranking rules and invalid-frontmatter separation. Compute links from the actual output parent to each source, replacing all three literal `../../notes/` constructions. Decide output naming/collision handling if more than one collection can be requested. |
| `src/commonplace/cli/promotion_candidates.py:main` | Expose the agreed input and pass it through. Define no-argument behavior explicitly. Do not introduce a hidden Theory default. Treat invalid collection inputs as operator errors without writing a report. |
| `src/commonplace/review/review_target_selector.py:NOTES_ROOT`, `REFERENCE_ROOT`, `REVIEWABLE_ROOTS`, `list_reviewable_notes` | Replace fixed eligibility roots with approved scope selection. Preserve current per-root top-level scan depth, frontmatter/index/type exclusions and user-verification filtering. Removing name coupling does not commission recursive review or review of raw captures. |
| `src/commonplace/cli/review/review_target_selector.py` | Describe the approved target/default policy; retain generic `collection/<path>` conformance selection. Include a non-Theory example. |
| `src/commonplace/review/collection_conformance.py` | Reuse its generic criterion resolver. Change only examples/docs or adaptations actually required by the final collection-spec type; do not turn the new contract type into reviewable content automatically. |

### Track 1 tests and authored surfaces

Tests to update/add, with arbitrary names as the primary regression fixtures:

- `tests/commonplace/general/test_project_paths.py`
- `tests/commonplace/validation/test_validate_notes.py`
- `tests/commonplace/validation/test_validation_exclusions.py`
- `tests/commonplace/validation/test_directory_artifact.py`
- `tests/commonplace/indexing/test_promotion_candidates.py`
- `tests/commonplace/review/test_status.py`
- `tests/commonplace/review/test_review_target_selector.py`
- `tests/commonplace/review/test_collection_conformance.py`
- `tests/commonplace/review/test_review_batch.py`
- `tests/commonplace/review/test_review_jobs_live_and_direct.py`

Also inspect `src/commonplace/cli/review/ack_trivial_note_changes.py` and its
test consumers of the shared selector; a broader selector must not silently
broaden acknowledgements. Run the review/freshness/relocation consumer suites,
not only the directly edited tests.

Update the agreed API/help in `kb/reference/commands.md`,
`kb/reference/README-REVIEW-SYSTEM.md`, `kb/reference/validation-contract.md`,
`kb/instructions/cp-skill-validate/SKILL.md` and instructions that invoke the
changed commands. The existing rename `residual-live.tsv` locates old examples;
use the command/type definition as authority rather than repeating old scope.
If status or promotion acquires new syntax, add its concrete callers/tests to
the worklist when the API is chosen. Do not rename generic note vocabulary.

## Track 2 — Semantic policies currently selected by paths

These findings extend beyond the original Notes rename. The selected route
is to retain their current semantics and document intentional dependencies,
not generalize every path. Each section identifies the behavior and the bounded
verification needed if a consistency fix or relocation touches it. No accepted
contract is silently amended.

### 2A. Imperative type-rule binding

The unquoted-source bound is no longer a type rule: `validation.py` applies it
to every artifact whose governing collection contract sets
`unquoted-source-limit` ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md)). Article lineage and the historical
external-system review type keep exact type-path registrations. Other workflow modules
register their own local types. These strings identify **types**, not default
content collections.

[ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md)
and the current [validation contract](../../reference/validation-contract.md)
require resolved canonical identity, not a bare type name. Do not “generalize”
by matching every `structured-claim` name, every artifact in Theory, or every
schema that happens to resemble the framework type. Same-named local contracts
must not inherit unrequested framework checks.

Retain the remaining canonical registrations. None names a Notes-local type,
so the Theory rename changes no registration. The source bound moves with the
relocated `COLLECTION.md`, whose frontmatter carries the field. Do not
introduce further declarative check attachment, portable type IDs or
KB-authored code execution without a demonstrated need.
Preserve the pinned-validation adapter's fail-closed rule/dependency boundary;
`validate_pinned_artifact_snapshot` rejects unsupported member dispatch rather
than skipping it. Any new attachment becomes an input to its captured contract
closure and requires explicit tests. Commit `59464f3ac` captures governing
collection contracts transitively so ADR 122's policy read is part of that
closed input set.

For the rename, no production edit is needed here: the contract field moves
with the collection.
Test in `test_validation_unquoted_sources.py`, `test_pinned_validation_contracts.py`,
`test_type_resolver.py`, `test_type_conformance.py` and the affected analysis
pinned-draft/publication suites. At minimum prove intended checks survive a
relocation and unrelated same-named types do not acquire them.

### 2B. Source classification and snapshot paths

**Operator decision:** reserve `sources` at `kb/sources/`, with no root
configuration or alias mechanism. Keep source recognition, snapshot/cache and
grounding semantics unchanged. Arbitrary source-root support is not a deferred
implementation requirement for this workshop. The operator may reopen it for
a concrete consumer need. Bound applicability is settled separately in 2A.

| File and anchor | Intentional behavior to retain |
|---|---|
| `src/commonplace/lib/validation.py:validate_unquoted_sources` | Count tracked ingest links under `kb/sources/`; use the governing collection's declared limit. Preserve Quotes-only support and `(snapshot required)` counting. |
| `src/commonplace/review/job_prompt.py:_required_snapshot_path` | Recognize `kb/sources/` ingest paths and derive the paired sibling `.snapshots/<slug>.md`. Do not broaden source-read eligibility. |
| `src/commonplace/lib/validation.py:validate_ingest_quotes` | Keep citation paths under `kb/sources/.snapshots` and preserve source pin/locator checks. |
| `src/commonplace/lib/validation.py:validate_source_snapshot_cache` | Audit the reserved Sources collection, not every hidden directory named `.snapshots`. |
| `src/commonplace/lib/quote_verification.py`, `lib/source_identity.py`, `lib/validation.py:_name_paired_snapshot` | Preserve existing identity normalization and sibling pairing; no new classifier. |
| `src/commonplace/lib/snapshot.py:SNAPSHOT_DIR`, `cli/github_snapshot.py`, `cli/x_snapshot.py` | Retain current output-directory APIs and CLI defaults. No new root configuration is needed. |

Tests: `tests/commonplace/validation/test_validation_unquoted_sources.py`,
`test_validate_notes.py`, `test_pinned_validation_contracts.py`,
`tests/commonplace/sources/test_snapshot.py`, `test_quote_matching.py`,
`test_quote_verification.py`, `test_github_snapshot.py`, `test_x_snapshot.py`,
and `tests/commonplace/review/test_job_prompt.py`/`test_review_telemetry.py`.
Retain negative cases for non-ingest Markdown, external paths, wrong pins and
ungranted snapshots. Renamed-source-collection support is not acceptance for
this work; no source relocation or network inspection is commissioned.

### 2C. Workshop eligibility, archives and lifecycle

**Out of scope:** the operator excluded Work/Tasks/proposal lifecycle modeling
from this collection-name refactor. Leave the path dependencies listed below
unchanged. Their preservation is not adoption of a new lifecycle model or a
claim that task/mailbox workflows are established. Do not remove Work's staging
exception or the archive boundary. No role declarations or root configuration
are introduced. A future lifecycle commission may revisit them; no such
redesign is a prerequisite for the Theory rename. The source-module warning
makes the pending overall design visible at the point a future agent would
extend the checks. It does not change their current behavior.

| File and anchor | Existing behavior to retain |
|---|---|
| `src/commonplace/lib/type_resolver.py:validate_type_eligibility` | Grants any valid peer-local type beneath the first path segment `work`. This is an explicit path-based exception in [ADR 068](../../reference/adr/068-collection-contracts-stop-enumerating-available-types.md), not an accidental helper. Moving it to caller context or a declaration requires an accepted amendment that preserves staging without copied types. Do not grant the exception to every collection or remove it without a replacement. |
| `src/commonplace/lib/validation.py:validate_proposal_archive_links`, `_PROPOSAL_ARCHIVE_RELATIVE_PATH` | Hardcodes the Reference proposal archive and Work exemption. Preserve the distinction between frozen archive content, its landing, internal archive links and external load-bearing links. Agree archive/staging context before removing either guard. |
| `src/commonplace/lib/project_paths.py:is_proposal_archive` | Already recognizes the `proposals/archive` structural convention across paths. Do not confuse this existing convention with a fixed root collection; it may still need consistency tests against the special Reference-only guard. |
| `src/commonplace/lib/lifecycle_validation.py` | Scans fixed Work and Tasks areas. These are operational lifecycle roots, and Tasks need not be a collection. Retain the current roots; do not substitute a generic collection scan. |
| `src/commonplace/cli/validate_notes.py` — lifecycle target; `lib/project_status.py:load_lifecycle_status` | Retain the lifecycle invocation and report its actual fixed scope. No silent disappearance of workshop/task checks under a generic collection refactor. |

Tests: `tests/commonplace/general/test_type_resolver.py`,
`tests/commonplace/validation/test_validation_exclusions.py`,
`test_lifecycle_validation.py`, `test_validate_notes.py`,
`tests/commonplace/review/test_status.py`, and archive-boundary tests located
by their existing `validate_proposal_archive_links`/archive fixtures.
The collection-contract type does not carry this policy. The retained path
conventions distinguish staging from ordinary durable content.

### 2D. Tags and site-specific policy

**Operator decision:** retain Tags as a special collection at `kb/tags/`, with
one namespace per KB and a central participation list. Do not introduce
multiple tag collections or require member collections to choose a namespace.
Root generalization is out of scope; there is no root configuration. The
existing scaffold already creates an empty Tags collection in every new KB.
Site-specific publication policy remains separately owned.

`src/commonplace/lib/index_generated.py:tags_collection` fixes the head location
at `kb/tags`; participation is **already declared**, not inferred from member
collection names. Validation and the site consume the same collector. Keep
that single source of membership truth.

[ADR 089](../../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)
explicitly fixes one namespace and canonical head location. Do not quietly
replace it with “find any contract with a `participating` key,” multiple tag
namespaces or a `name == tags` compatibility shim. No ADR amendment or new root
input is needed to retain this behavior. The consumers below identify what to
verify when the Theory rename changes participation and member links, not a
commission to relocate Tags:

- `src/commonplace/lib/index_generated.py`: root, heads and participation reader.
- `src/commonplace/lib/validation.py`: head placement, completeness, missing-head
  checks and path-specific diagnostic text.
- `src/commonplace/docs/properdocs_hooks.py`: tag tails, rendered tag links,
  nav preference and cached tag space.
- `src/commonplace/lib/library.py`, scaffold and root instructions: preserve
  the Tags hub; update only renamed member-collection references where needed.

Tests: `tests/commonplace/indexing/test_tag_space.py`,
`tests/commonplace/validation/test_validation_tag_readme.py`,
`tests/commonplace/docs/test_properdocs_hooks.py` and the contract/type fixtures.
Prove participation does not broaden, contract metadata never becomes a member,
and malformed participation declarations never imply an all-collection scan.

The site hook also has fixed Instructions depth, Reports/Messages publication
rules, hidden menu collections and an Agentic Systems grouping. Those are
**this publication's selected policy**. Keep them distinct from generic
collection validation/review eligibility. Do not extract a configurable site-policy framework in this work or infer
publication permission from collection discovery.
`tests/commonplace/docs/test_site_publication_boundaries.py` is a required
consumer suite for any such change. No automatic expansion of published data
is authorized.

## Intentional constants and explicit exclusions

These were inspected as a different class of path, not forgotten. Retain them
unless a concrete consumer requires relocation and its owner approves it:

| Files / constants | Why not a generic content-collection assumption |
|---|---|
| `hatch_build.py:SHIPPED`, `scaffold_manifest.py`, `_data/templates/`, `.github/workflows/ci.yml` | Declare this product's shipped layout and fresh-project defaults. The Theory rename owns their change. |
| `lib/library.py` — Instructions root/skill lookup; `review/paths.py` | Locate the installed framework library and its gate/skill catalog. They are not a rule that user collections must be named Instructions. |
| `lib/type_resolver.py:GLOBAL_TYPE_VALUE`, `global_types_dir`; `project_paths.py` — `types` subdirectory rules | `types/` is a registered global/local type-address convention, not arbitrary content selection. Changing it is a type-system migration, not collection independence. |
| `store.py:DEFAULT_DB_PATH`, `review/artifacts.py:REVIEW_JOBS_ROOT`, `lib/full_pass.py` | Tool-owned state/output and packet identity conventions. Some already support explicit override. Do not move stores or break packet guards while generalizing content input. |
| `lib/promotion.py` — report output under Reports/cache | Output destination is independent of which collection supplied candidates. Keep a documented default unless a demonstrated multiple-scope collision requires output selection. |
| `lib/agentic_analysis/analyses.py`, `guards.py`, `worktree.py`, `audit.py` and pinned workflow contract paths | Belong to the explicitly located analysis workflow. They do not claim to be generic content scans. Keep workflow evidence/lock/identity boundaries intact. |
| `lib/validation.py:validate_pinned_artifact_snapshot` — required `reference/validation-contract.md` | Explicit frozen method dependency. Do not substitute an arbitrary discovered Reference-like collection or silently drop the pin. |

An exception is acceptable only when its role is explicit. A directory literal
hidden in a generic helper cannot be excused by calling it a default. Conversely,
zero text matches is not a useful acceptance criterion.

## Implementation route and deliverables

The executor may choose another route with the same boundaries and acceptance.

1. **Reconcile ownership and gates.** Capture the final parallel collection-spec
   change set; record approved scopes/APIs and Track 2 decisions. Read affected
   collection/type contracts. New contract/ADR work follows its destination's
   authoring rules; no accepted ADR is silently amended by code.
2. **Baseline tests.** Establish the same chosen test coverage before and after.
   Add regression fixtures with names such as `claims`, `manuals`, `inbox` and
   `staging`; none should receive privilege solely from its spelling. Include
   typed and untyped contracts, ignored data, a namespaced collection and a
   directory without `COLLECTION.md`. Do not weaken fixture isolation.
3. **Implement Track 1 in a bounded commit series.** Pass resolved scope through
   library/CLI layers. Test it on the existing layout and a KB with neither
   Notes nor Theory. Update public help/docs with the chosen interfaces.
4. **Systematize Track 2's retained policies.** Document the current behavior
   and intentional path dependencies. A concrete consistency fix includes all
   affected consumers and tests; no new configuration is implied. Do not leave
   type-rule dispatch or protected-record checks silently disabled during the
   rename. Reopen a policy only for a demonstrated inconsistency or consumer
   need, not merely because its implementation contains a directory literal.
5. **Integrate with the rename.** Give its owner the new APIs, policy decisions,
   completed/deferred findings and exact changed paths. Refresh the rename
   worklist for these known changes. The collection move and its backlink-only
   commit remain separate. Generic input support must not require a consumer
   to rename its collection or migrate its review store.
6. **Close the workstream.** Retain durable API/architecture/ADR changes in
   Reference and operational instructions in Instructions. Remove or reduce
   this plan only when its findings have implemented or explicitly deferred
   dispositions and the rename owner no longer needs it.

Deliver a final file-level change list, selected test results, interface changes,
remaining intentional constants and any concrete unresolved inconsistencies.
Distinguish generic operation independence from retained path-based policy;
do not assert that every directory dependency has been removed.

## Acceptance and verification

### Required behavior

- Explicit generic operations treat Notes, Theory and an unrelated collection
  name equally; no replacement Theory-only helpers/fields/default roots exist.
- No-argument behavior follows an approved policy and reports its actual scope.
  Missing or malformed declarations produce defined errors or explicit omitted
  status, not success or accidental whole-KB scanning.
- Collection lookup and contract validation behave according to the final
  parallel type's contract; frontmatter-free contracts are still structurally
  located but fail the required contract-type validation. A type declaration does not turn `COLLECTION.md`
  into content for validation, promotion, tags or default review.
- Existing visibility, validation-ignore, archive, source-grounding and pinned
  method boundaries survive. Discovery grants neither write authority nor new
  publication, review, source-read or tag-membership scope.
- Report links resolve from the real output directory for multiple unrelated
  input roots. Repeated requests do not accidentally overwrite a different
  scope's report under an undocumented policy.
- Remaining type rules keep canonical dispatch, not bare-name matching. The
  unquoted-source limit follows the governing collection contract through the
  rename, independently of artifact type; collections omitting it remain
  unbound. Pinned validation consumes the captured contract declaration.
- Existing consuming projects can keep their content layout. Build/scaffold and
  site declarations remain explicit; no state-store/content relocation or
  freshness acknowledgement is hidden in this refactor.

### Test coverage

Follow [test selection](../../../tests/README.md). Track 1 touches foundational
paths, validation and review selectors; Track 2 can reach sources, indexing,
installation and pinned analysis. For the combined refactor, run the **full
suite including slow tests**, plus lint:

```bash
uv run ruff check .
uv run pytest -m ''
```

Use targeted general plus affected consumer suites during development; report
exact directories and marker filters. Run relevant deterministic validation
for authored contract/spec/instruction/reference changes. For packaging,
entry-point, scaffold or init changes, follow
[editable installation](../../../INSTALL.md#2-install-commonplace-as-a-user-level-tool)
and the disposable installed scenarios. Never run init in this checkout.
No source network calls are needed to test path independence.

The execution status above records the completed Track 1 test run. Later code
changes require their own relevant verification; this survey does not establish
that proposed consistency fixes or the Theory rename have passed.

### Stop and return

Stop shared-file edits on ownership conflict or collection-spec interface drift.
Stop before changing an implicit scope, special policy or public API whose gate
is unresolved. Stop on a proposed bare-name type dispatch, unbounded scan of
captures, silent loss of a check, or evidence/state migration outside this
commission. Return the named files and decision needed. Continue disjoint
approved work only; do not improvise a compatibility layer or role field to
make the other branch fit.
