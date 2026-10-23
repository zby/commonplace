# Full Theory rename: implementation inventory and handoff

## Intent and authority

Make the existing theoretical collection consistently **Theory** in current
code, paths, scaffold, contracts, navigation and operator instructions. Its
members remain **notes**. This packet prepares that change; it does not
approve or execute it. The operator is inclined toward a full rename and
commissioned repository-wide preparation before deciding.

A successful implementation leaves `kb/theory/` in place of `kb/notes/`, ships
`theory/` in the installed library, scaffolds `kb/theory/` for new projects,
and lets runtime commands operate on eligible collections without depending
on their names. Existing published addresses continue to resolve. Historical records and arbitrary user collection names
are not silently relabelled. The current workshop framing records an evidence
sort as a prerequisite; complete that separately before the collection move.
Do not add a new note type, new review traversal or unrelated cleanup to the
rename.

**Start with the decision gates below, then the runtime table.** The TSV files
supply exact paths and line locations. An implementer need not rediscover the
repository-wide reference set. Reading the named files and checking drift is
still necessary. The inventories are evidence at one revision, not permission
to change every matching word.

## Runtime independence: operator direction

The separate [hardwired-collections removal plan](./hardwired-collections-plan.md)
is now the runtime workstream's implementation handoff. It expands the survey
beyond Notes and defines the coordination boundary with collection-spec typing.
Its execution status and retained exceptions govern that work; the runtime
table below distinguishes completed changes from the rename's remaining layout
work. Generic scopes landed in `43a98d836`, special roles are documented by
`94c0f71f7`, and ADR 122's collection-owned source bound landed in `daed61d59`.
Keep relocation, scaffold and publication migration in this plan.

The operator directed that code should be collection-independent and approved
revising this plan on that basis. **Remove unnecessary runtime coupling; do
not replace Notes hardcoding with Theory hardcoding.** Collection discovery,
operation scope and shipped layout are separate concerns:

- Generic runtime code discovers collections through `COLLECTION.md` or accepts
  an explicit collection/path. A directory name does not determine eligibility.
- Each operation still needs a defined scope. Discovery of Reports, Sources or
  a frozen collection is not permission to validate, promote or review all its
  contents. Use the existing visibility and validation-ignore boundaries where
  applicable; preserve explicit-target behavior. Do not invent new eligibility
  metadata without a concrete requirement and an approved contract.
- Build/scaffold manifests, this KB's routing instructions, and shipped-library
  addresses legitimately name the selected layout. Those declarations change
  to Theory; generic runtime helpers and status fields must not.

The TSVs remain observations of the old code, not instructions to rename its
identifiers. This revised runtime table and scope gate supersede the original
mechanical rename recommendations.

## Concurrent workshop updates and precedence

During this audit another session added [a general plan](./plan.md) and
[an evidence sort](./evidence-sort.md), and the [framing](./README.md) recorded
an operator decision to sort evidence before renaming. Those changes were
not authored by this inventory task. Preserve them. The recorded evidence
prerequisite supersedes this audit's initial recommendation to move all
subareas intact. The per-file sort is provisional and still needs its named
confirmations.

The inventories below are **pre-sort baseline evidence**, not a post-sort
execution manifest. After the prerequisite moves, reconcile their exact old/new
paths, backlink effects and redirects before the collection move; do not use
the 431-file count as a fixed target. The general plan has been synchronized
with this runtime-independence revision and the final audit categories.
Review-state continuity is not required (operator, 2026-10-23). Keep existing
historical state without migrating database keys or freshness baselines. The
operator considers the reviews old and expects a separately designed replacement
system; this rename does not commission that design or a database rewrite. Refresh both plans' execution counts and
worklists after the prerequisite moves.

## Evidence boundary and inventory map

Audited HEAD: `073eca55f4dcc703eb65f34f73f3b880b0b4cac2`. No rename or production
code change was applied. The installed command was exercised in dry-run mode:

```bash
commonplace-relocate-directory kb/notes kb/theory
```

The audit enumerated Git-tracked text, tracked symlinks, every file in the
source collection, and the actual Markdown walk used by relocation. It also
simulated that command's link and `source_notes` rewrites in memory to identify
what would remain. It did not inspect every ignored source snapshot or every
external consuming checkout. Untracked local reports are included only when
the relocation walk would touch them. No outside-project migration is implied.

| Inventory | What it gives the implementer |
|---|---|
| [Summary](./inventory-summary.json) | Revision, counts and audit categories. |
| [Moves](./moves.tsv) | All 431 payload files, exact old/new paths, tracked status and pre-move SHA-256. |
| [Relocation updates](./relocation-updates.tsv) | Every one of the 2,119 Markdown paths the unfiltered command would rewrite; tracked status, category and rewrite count. This is a blast-radius list, not an approved edit list. |
| [Reference files](./reference-files.tsv) | All 3,043 tracked text files matching `notes`, related identifiers or filenames; original matching line numbers, automatic rewrite counts, residual counts and proposed disposition. Includes generic-word matches deliberately kept. |
| [Live residuals](./residual-live.tsv) | 1,263 candidate lines in 203 files that the command leaves behind: code, fixtures, contracts, templates, labels, examples and URLs. Excerpts are bounded to 360 characters; locations refer to simulated post-relocation content, at the original source path. |
| [Record residuals](./residual-records.tsv) | 440 historical/source/frozen files with remaining literals; line locations and preserve disposition, without duplicating their contents. |
| [Workshop residuals](./residual-workshops.tsv) | 338 workshop files with remaining literals. Distinguish current plans and drafts from experimental captures using the rules below. |
| [Redirect changes](./redirect-changes.tsv) | Exact 164 existing redirect targets to retarget, 427 moved-page redirects to add, and six virtual-index redirects to add. Existing keys are preserved. |

The reference inventory is deliberately broader than the required changes.
`Notes` in a talk's speaker-note CSS and an external system's note memory is
not the Commonplace collection. The HTML talk and the generated memory matrix
were inspected as such false positives; do not rename their vocabulary.

The move contains **429 Markdown files and two YAML schemas**. There are 366
root Markdown files. The relative subtree structure stays unchanged. Two
Markdown files are write briefs and receive no public redirects.

### The relocation blast radius

The dry run reports 2,119 Markdown updates: 1,122 tracked paths and 997
untracked paths. `CLAUDE.md` is a symlink alias of `AGENTS.md`, so these are
path counts, not necessarily distinct underlying files.

| Audit category | Automatic update paths |
|---|---:|
| Live contracts, articles, navigation and ordinary content | 109 |
| Frozen Agent Memory Systems reviews | 172 |
| Retained evidence, analysis members and archived accounts | 59 |
| ADRs and reference proposals | 76 |
| Source ingests | 517 |
| Workshops | 189 |
| Local report cache/state | 997 |

These counts replace the framing's approximate inbound-link estimate. They
count files the command would change, not just explicit `kb/notes/` literals.
The untracked local files are not to be staged, published or treated as new
migration deliverables.

## Decisions required before mutation

The operator authorized implementation after the plan update. The scaffold
policy below and the subsequent frozen-record and freshness clarifications
govern execution. Record these choices in the rename ADR before relocation.

1. **Full rename and its meaning.** Approve `kb/notes/` → `kb/theory/`, library
   `notes/` → `theory/` and collection label `Theory`. Replace unnecessary
   collection-specific runtime assumptions with generic behavior below. Keep
   `note`, `types/note.md`, filenames expressing claims about notes, and generic
   note APIs. Read
   [ADR 116](../../reference/adr/116-one-word-per-concept-across-prose-and-code.md).
   The new ADR records this collection change; it need not reopen that rule.
2. **Finish the recorded evidence prerequisite.** The current
   [contract](../../notes/COLLECTION.md) already places definitions and
   theory-facing evidence here; it does not make every episode theoretical.
   Follow the framing's scope-of-inference decision and resolve the provisional
   per-file sort in `evidence-sort.md`. Decide retained form, link semantics
   and contract changes before those moves; commit each relocation alone.
   Keep the remaining subareas intact unless separately directed. Refresh the
   move and redirect manifests after the prerequisite. This inventory does
   not commission those content changes or approve the provisional sort.
3. **Installed-project policy: decided (operator, 2026-10-23).** The scaffold
   keeps seeding `kb/notes/` from the existing soft `user-notes-*` templates: a
   project's general domain-understanding layer, a different concept from this
   KB's strict Theory, so it keeps its own name. Only this checkout's
   collection and the shipped library (`commonplace:theory/...`,
   `<library>/theory/...`) rename. Init never creates a Theory collection, so
   refresh cannot create a twin, and existing consumers keep their collections
   unchanged. Consumers still reconcile references into the shipped library and
   changed command/status APIs. A compatibility shim needs a named consumer,
   owner and removal condition; do not invent that need. An optional
   add-collection skill offering Theory as a prototype was discussed and
   deferred until a project asks for it.
4. **Frozen backlink policy: inspect the actual obligation.** The operator
   clarified that ADRs are semantically, not byte-for-byte, frozen: update
   navigational links without changing the recorded decision. Apply the same
   distinction by inspecting each record's governing contract and role, not by
   treating a historical collection as uniformly immutable. Legacy reviews
   preserve findings and review boundaries; ingests preserve snapshot identity
   and quotations while retaining an active authored linking surface. Exact
   captures, hash-pinned analysis members, manifests and experimental versions
   remain byte-preserved. Identify the exact protected subset before applying
   relocation; the command has no exclusion option. Site redirects do not
   provide repository-relative filesystem compatibility for protected old links.
5. **Local review/freshness state: continuity not required (operator,
   2026-10-23).** The reviews are already old. Keep historical state without
   migrating database keys, carrying reviews forward, mass-acknowledging
   freshness or repairing old report packets. Back up state before relocation;
   do not delete or rewrite it. Moved artifacts acquire new path identities and
   may lack current reviews. A replacement review/freshness system is separate
   future work, not part of this rename.

6. **Operation scope and rule applicability: resolved.** Preserve the explicit
   scopes implemented in `43a98d836`, summarized below. The governing collection
   contract's `unquoted-source-limit` field selects the source bound
   ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md));
   it moves with the contract and needs no type-registration update. Retain
   intentional special roots and the excluded lifecycle/archive policies. Do
   not treat discovery as eligibility or reopen these decisions merely to
   rename the shipped layout.

The ADR, consuming-project migration instruction and release communication
are **new files**, so their final names/ADR number are not part of the scanned
existing-file inventory. Select the next free ADR number at implementation
time. Read the reference collection and ADR type before authoring it; read
the instruction contract and instruction type before authoring the migration
procedure. The implementation must not mark an ADR accepted without the
operator's approval.

## 1. Runtime and build changes

The runtime refactor is implemented before the collection move, with tests for
Notes, arbitrary and namespaced collections, and a KB with neither Notes nor
Theory. Preserve that behavior while changing the shipped layout. Keep relocation
in its own commit; intermediate commits need not be independently releasable.
Do not release until the full rename sequence passes verification.

### Implemented runtime scopes

| Operation | Implemented contract | Rename responsibility |
|---|---|---|
| Explicit validation target | Generic collection-name/path resolution; no special `notes` branch. | Verify `theory` resolves through the same path as unrelated names. |
| `today` / `recent` validation | Required `--collection NAME_OR_PATH`; date filtering over the selected validation surface, with structure checks and ignore boundaries. | Keep scope in drill-down commands and retain non-Theory regression fixtures. |
| Status validation summary | Required `--collection NAME_OR_PATH`; generic `notes_validation` field includes `scope`. Git, lifecycle and optional review retain their separate scopes. | Verify the selected Theory scope; do not introduce `theory_validation`. |
| Promotion candidates | Required collection argument; reports at `kb/reports/cache/promotion-candidates/<collection-relative-path>/report.md`, with path-derived links. | Verify Theory output and links without changing arbitrary-collection support. |
| Review selection and trivial acknowledgement | Required explicit `--note` targets; `--user-verified` only filters that scope. Directory selection stays shallow and refuses validation-ignored sweeps. | Keep metadata/type/index exclusions and no implicit Notes/Reference/Theory roots. |
| Unquoted-source rule | Governing `COLLECTION.md` sets `unquoted-source-limit`; Notes and Articles set 5 under ADR 122. | Carry the field with the relocated contract and verify it still binds. No registration edit. |

The original runtime coupling locations remain useful audit anchors, not a
second implementation worklist. Current code and the runtime handoff define the
implemented interfaces. Reopen a public API or policy only for a concrete new
requirement; no role registry, root configuration or type-binding mechanism is
needed for this rename.

All paths in the following table are repository-relative.

| File | Required change and constraint |
|---|---|
| `hatch_build.py` | Change `SHIPPED` from `notes` to `theory` and its library description. This controls both wheel shared data (`share/commonplace/theory`) and sdist `kb/theory`. Missing this breaks the package build, even if local commands work. |
| `src/commonplace/scaffold_manifest.py` | Scaffold `kb/theory` and `kb/theory/types`; point the two renamed template sources at `kb/theory/COLLECTION.md` and `kb/theory/README.md`. |
| `src/commonplace/lib/project_paths.py` | Done in Track 1: the Notes-only helper is removed; `resolve_collection` handles explicit names/paths within the KB. Preserve generic enumeration and note terminology. |
| `src/commonplace/cli/validate_notes.py` | Done in Track 1: generic target lookup and explicit collection-scoped date validation. Keep the generic module name, note counters, ignore boundaries and scoped drill-down commands. |
| `src/commonplace/lib/validation.py` | No change for the unquoted-source rule (ADR 122 moved it to the contract field). |
| `src/commonplace/lib/project_status.py` | Done in Track 1: supplied collection scope, scope-derived details commands and explicit `notes_validation.scope`. Preserve separate Git/review/lifecycle responsibilities. |
| `src/commonplace/cli/status.py` | Done in Track 1: required `--collection` and the actual validation scope in output. No Theory-specific heading or field is needed. |
| `src/commonplace/lib/promotion.py` | Done in Track 1: explicit collection input, validation-aware enumeration, separate scoped reports and links from actual paths. Preserve arbitrary/namespaced-collection tests. |
| `src/commonplace/cli/promotion_candidates.py` | Done in Track 1: required positional collection input. Command name stays unchanged; no missing-scope default is introduced. |
| `src/commonplace/review/review_target_selector.py` | Done in Track 1: fixed root tuple removed; explicit targets with optional user-verification filter. Preserve shallow selection and metadata/type/index/ignored-directory boundaries. |
| `src/commonplace/review/collection_conformance.py` | Update examples/docstrings to `collection/theory` and `kb/theory/COLLECTION.md`; collection identity resolution is already generic. |
| `src/commonplace/cli/review/review_target_selector.py` | Change help's `collection/notes` example to `collection/theory`. |
| `src/commonplace/cli/relocate_directory.py` | Replace old-current-collection examples with Theory examples, including the redirect example. Do not change the CLI's operation name. Historical examples may instead be explicitly labelled migration examples. |
| `src/commonplace/cli/relocate_note.py` | Update default-collection examples, not the operation name or generic note vocabulary. |
| `src/commonplace/lib/library.py` | Update the enumerated library collections in the opening description. `Tag heads (browse the notes by topic)` is generic and may stay. Library root detection itself is not hardcoded to the old collection. |
| `pyproject.toml` | Update the library-collection comment. Keep `commonplace-validate = "commonplace.cli.validate_notes:main"` unless separately renaming that generic module; that rename is unnecessary here. No dependency change or lockfile update is inherently required. |
| `scripts/article_dependency_inventory.py` | Change `DEFINITION_DIRS` and both classification-prefix checks to `kb/theory/...`. Keep article `source_notes` terminology. |
| `.github/workflows/ci.yml` | Change the required library landing from `kb/notes/README.md` to `kb/theory/README.md`. |

The explicit collection examples in help and the two source-repository tooling
rows below are layout declarations, not rules for generic consumer runtime
eligibility. In particular, `scripts/article_dependency_inventory.py` remains
a repository-specific analysis script unless separately commissioned otherwise.

### Inspected code that needs no collection rename

`src/commonplace/docs/properdocs_hooks.py` discovers collection directories
and derives the menu label from the directory name. It already turns `theory`
into `Theory`. Alphabetical discovery moves Theory after Reference; approve
that natural order or separately request an explicit ordering change. Its
virtual directory listings are generated, not tracked files to move manually.

`index_directory.py`'s `notes_dir`, `index_generated.py`'s `notes_by_tag`,
`validation.py`'s parsed-note cache, review batches/protocol/telemetry and
warn selectors use **note** generically. They are not names for this collection.
Do not sweep those names. `scripts/migrate_analysis_publications.py` calls
`rewrite_source_notes`; that is the article field, not a collection alias.
The broad reference inventory also records these no-change matches.

The skill symlinks under `.agents/skills/` and `.claude/skills/` point into
Instructions or the analysis collections, not Notes. Keep their targets.
Edit canonical skill files only. `CLAUDE.md` remains a symlink to `AGENTS.md`;
do not turn it into a second independently edited root instruction file.

## 2. Scaffold and consuming-project control plane

**Superseded in part by Gate 3's decision:** the scaffold keeps `kb/notes/`,
the `user-notes-*` templates keep their names, and the tags template keeps
`participating: [notes, ...]`. What remains here: `AGENTS.md.template`'s
*library* routing row and library search recipe change to `theory`, while its
project `kb/notes/` rows stay; consumer upgrade reconciles library references
only. Read the rest of this section with that in mind.

Rename these template files to `user-theory-COLLECTION.md` and
`user-theory-README.md` under the same template directory:

- `src/commonplace/_data/templates/user-notes-COLLECTION.md`
- `src/commonplace/_data/templates/user-notes-README.md`

The collection template's heading, destination paths and local-type example
become Theory/theory; the landing heading becomes `# Theory`. Its members may
still be called notes, including the initial empty-state sentence.

Update collection destinations/declarations in these sibling templates:

- `src/commonplace/_data/templates/user-instructions-COLLECTION.md`
- `src/commonplace/_data/templates/user-reference-COLLECTION.md`
- `src/commonplace/_data/templates/user-reports-COLLECTION.md`
- `src/commonplace/_data/templates/user-sources-COLLECTION.md`
- `src/commonplace/_data/templates/user-tags-COLLECTION.md`
- `src/commonplace/_data/templates/user-work-COLLECTION.md`

For the tags template, change `participating: [notes, reference, instructions]`
to use `theory`, as well as the example member path. Destination cells naming
`notes` as a collection become `theory`; generic references to authored notes
stay. The workshop template's list of destination collections must agree.

`AGENTS.md.template` needs changes to vocabulary examples, project and library
routing rows (`kb/theory/`, `<library>/theory/`), and all three search recipes.
The runtime-generated library pointer comes from `lib/library.py`; inspect
its output during installation checks. Do not manually edit installed package
copies, generated stubs or machine-local pointers in this checkout.

**Existing projects cannot be migrated by rerunning init alone.**
`src/commonplace/cli/init_project.py` creates missing scaffold directories and
preserves existing divergent files. After a package upgrade, rerunning it
could create an unwanted empty Theory beside an existing Notes collection
while preserving its original participation declarations. The upgrade procedure
must handle refresh without requiring a consumer-owned directory rename:

1. Back up/checkpoint the consumer. Decide whether it keeps its collection
   names or voluntarily adopts the new scaffold layout. Stop on a destination
   collision if renaming; do not merge collections automatically.
2. Reconcile references to the shipped library namespace `commonplace:notes/...`
   and `<library>/notes/...`; those become `commonplace:theory/...` and
   `<library>/theory/...` on upgrade regardless of the consumer's own layout.
   This checkout cannot enumerate references in outside consuming projects.
3. Only if the consumer elects to rename its own collection, use directory
   relocation under the approved preservation/state policy and update its
   local types, schemas, contracts, participation and root instructions. Do
   not replace customized contracts with ours.
4. Use the approved existing-project init-refresh policy to regenerate pointers
   and stubs without accidentally creating a second content collection. Test
   this explicitly in `src/commonplace/cli/init_project.py` and
   `tests/commonplace/installation/test_init_project.py`. The behavior change
   needs an agreed Gate 3 design; no new suppression flag is assumed here.
   Run init and `--check` in the consumer or a disposable project only.
5. Verify operations against both retained arbitrary names and any voluntarily
   renamed collection, using the approved explicit/default scopes. Document
   changed command/status APIs and preserve customized content.

No automatic directory migrator or dual-root lookup is required for runtime
collection independence. If the upgrade needs further compatibility, return
the concrete consumer case rather than adding a speculative shim.

## 3. Mechanical relocation and its gaps

The supported operation is:

```bash
commonplace-relocate-directory kb/notes kb/theory
# Only after gates, dry-run review and an approved preservation route:
commonplace-relocate-directory kb/notes kb/theory --apply
```

`src/commonplace/lib/relocation.py:relocate_directory` moves all payload files,
rewrites ordinary relative inline Markdown links ending in `.md`, rebases
links in moved Markdown, and rewrites frontmatter `source_notes` lists.
It preserves anchors in supported links. The directory move carries the two
briefs and the YAML schemas without a separate move operation.

Unlike individual-note relocation, **directory relocation does not retarget
all existing redirects or create one redirect per moved page**. Its optional
`--redirect OLD:NEW` adds only a single entry. Do not mistake that option for
collection-wide publication migration.

The command also does **not** rewrite:

- Literal paths in inline code, fenced examples, shell recipes or Python.
- Frontmatter `type:` values, schema `const:` values or declared collection names.
- YAML/JSON/CSV/plain-text manifests and other non-Markdown references.
- Reference-style links, non-`.md` directory links, absolute site/GitHub URLs,
  or every possible Markdown link syntax.
- Review/freshness database keys or report packet identities.

The residual inventories are the separate worklist for those surfaces.
Do not run a repository-wide `notes` → `theory` replacement.

### Preservation route

Prefer executing in a clean checkout/worktree without ignored local reports.
Review `relocation-updates.tsv` against the approved frozen policy first.
If the existing command would alter protected records, choose and verify a
bounded preservation route **before applying it**. One route needs no product
feature: capture the exact protected originals, run relocation, restore only
those protected originals, and prove their bytes match the capture. This is
not a blanket `git restore` over a dirty checkout. The current inventories
identify the candidate paths; separate the protected subset under the adopted
policy. Do not smuggle record edits into the later namespace sweep.

If policy instead requires changes to protected content, stop and obtain
explicit authority; tool access is not that authority. A small relocation
filter feature is another possible route, but is not pre-authorized or
necessary simply to complete this rename.

Commit the relocation result alone: moved payload and approved command-produced
backlinks, without headings, `type:` edits or prose changes. Review rename
recognition and sample `git log --follow` afterwards. Subsequent schema/type
fixes go in the namespace/content commit, not the relocation commit.

## 4. Local types, contracts and authoring defaults

### Local type identity is easy to miss

The moved local specs are:

- `kb/notes/types/structured-claim.md`
- `kb/notes/types/structured-claim.schema.yaml`
- `kb/notes/types/theory-proposal.md`
- `kb/notes/types/theory-proposal.schema.yaml`

Their new prefixes are `theory/types/`. Change both schema `const` values,
body tables/templates naming the old type, and all live instance pointers.
Relative `schema: ./...schema.yaml` pointers remain valid. Keep global
`type: types/note.md`, `types/type-spec.md` and their schemas unchanged.

At the audited revision, **eight live instances** carry a Notes-local type:

- `kb/notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md`
- `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context.md`
- `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md`
- `kb/notes/index-completeness-does-not-determine-editorial-orientation.md`
- `kb/notes/skill-discovery-re-fires-in-every-sub-agent-context.md`
- `kb/notes/skills-derive-from-methodology.md`
- `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md`
- `kb/notes/proposals/revise-behavioral-authority-decomposition.md`

Other files contain examples of these values; use the residual locations,
including authored drafts under Work. Preserve old values inside genuinely
captured historical inputs. Such inputs are not current type instances to
repair. The schema fixture under
`tests/commonplace/validation/fixtures/schemas/flat/kb/notes/types/structured-claim.schema.yaml`
also needs a Theory destination and value if it remains the default local-type
fixture; update its loading test together.

### Contracts

Edit the moved `kb/theory/COLLECTION.md` and `README.md`; retain their meaning,
change the collection name, routing paths and destination declarations.
Update current cross-collection contracts:

- `kb/instructions/COLLECTION.md`
- `kb/reference/COLLECTION.md`
- `kb/sources/COLLECTION.md`
- `kb/tags/COLLECTION.md`
- `kb/reports/COLLECTION.md`
- `kb/articles/COLLECTION.md`
- `kb/agentic-systems/COLLECTION.md`
- `kb/agentic-system-analyses/COLLECTION.md`
- `kb/types/COLLECTION.md`
- `kb/work/COLLECTION.md`

Change destinations such as `notes`, `notes/definitions`, `notes/evidence`
to `theory`, `theory/definitions`, `theory/evidence` in declared slots, not
just backticked paths. The tags contract's `participating` entry is operational:
leaving it at `notes` loses the entire moved collection from tag discovery.
The frozen `kb/agent-memory-systems/COLLECTION.md` is separately policy-gated;
do not silently treat its frozen status as permission for a contract rewrite.

### Skills and instructions

The exact existing-file worklist is in `residual-live.tsv`. The critical
behavioral/default changes, beyond mechanical backlinks, are:

- `kb/instructions/cp-skill-write/SKILL.md`: default collection, shorthand
  resolution, examples and collection/type distinction. Default **type**
  remains `types/note.md`.
- `kb/instructions/cp-skill-connect/SKILL.md`: collection inference examples
  and collection identifier used for report routing.
- `kb/instructions/cp-skill-validate/SKILL.md`: use Theory as this KB's example,
  but explain generic collection targets and the approved `today`/`recent`
  scope. Do not present Theory as a special runtime target.
- `kb/instructions/cp-skill-convert/SKILL.md` and
  `kb/instructions/cp-skill-revise-autoreason/SKILL.md`: bare-name search roots.
- `kb/instructions/cp-skill-health-check/SKILL.md`: source-checkout detection
  example `kb/{notes,reference,instructions}/`; a slash-prefix-only search
  would miss this brace-list reference.
- Current procedure examples, onboarding, warning fixes, source grounding
  gates, full-pass procedures, article/type templates and task instructions:
  update this KB's concrete targets at the supplied residual locations.
  Shipped procedures must distinguish scaffold defaults from an existing
  consumer's actual collection paths; do not require a consumer named Theory.
  Preserve `source_notes`, `Relevant Notes` and generic note operations.

## 5. Documentation, navigation, publication and records

### Current documentation

`AGENTS.md`, `AGENTS.md.template`, `README.md`, `INSTALL.md`, `kb/README.md`
and `kb/index.md` must agree. The root README and KB homepage are separate
files: update both. Change the homepage `[Notes]` label to `[Theory]` as well
as its destination. Change root layout trees, search recipes and validation
examples; Markdown-link rewriting does not repair their code blocks.

The detailed reference worklist is in `residual-live.tsv`, notably:

- `kb/reference/architecture.md`
- `kb/reference/collections-and-types.md`
- `kb/reference/collection-prototypes.md`
- `kb/reference/content-routing.md`
- `kb/reference/definitions/collection.md`
- `kb/reference/documentation-site.md`
- `kb/reference/instruction-generation.md`
- `kb/reference/navigation.md`
- `kb/reference/README.md`
- `kb/reference/README-REVIEW-SYSTEM.md`
- `kb/reference/commands.md`
- `kb/reference/link-vocabulary.md`
- `kb/reference/validation-contract.md`

Update prose that specifically names the collection, including the status
validation summary and `collection/theory` review selector. Do not rewrite
historical ADR titles such as ADR 070's Notes wording, retired command names
such as `commonplace-generate-notes-index`, or generic type/operation terms.
Link display text containing an obsolete path is a separate edit even where
the command has already repaired the destination.

### Redirects

Apply `redirect-changes.tsv` to `properdocs.yml` after relocation:

- Retain all **215 existing `notes/...` source keys**. They are historical URL
  addresses, not live naming errors. Some now redirect out of this collection.
- Retarget **164 values** beginning `notes/` to `theory/`, regardless of whether
  their source key begins `notes/`, `articles/`, `reference/` or `work/`.
- Add **427** old-current-page redirects to the corresponding Theory page.
  This includes collection heads and local type specs but excludes two briefs.
- Add the **six** generated `dir-index.md` addresses listed in the inventory.
  They are not physical files in the move manifest.

The 597 proposed map changes have distinct keys at the audited revision.
Flatten targets to actual live pages. Preserve old keys and avoid chained
redirects; do not prefix-replace both sides of the map. Verify redirect
validation and a site build, including generated listings and menu labels.

Site redirects preserve website addresses, not GitHub `blob/main/kb/notes/...`
links or files read from a checkout. Current authored absolute links need
explicit retargeting at the residual locations. Captured historical URLs may
remain historical. Do not advertise site redirects as filesystem compatibility.

### Records, analysis sets and workshops

Use `residual-records.tsv` as an intentional-retention list, not a cleanup
queue. In particular, do not rewrite retained analysis YAML/JSON identifiers,
capture manifests, source snapshots, trial bundles, hashes or old report
packet paths to make a text search empty. Do not regenerate analyses or the
memory matrix merely because the word `notes` appears in external-system
characterizations. Rebuild generated outputs only if their actual inputs or
paths require it; use their owning command.

Use `residual-workshops.tsv` to update *current* framing, next-step paths,
authored draft type pointers and executable plans. Preserve historical
protocol inputs, observed outputs, session transcripts, manifests, experiment
versions, generated prompt/log/result trees and vendor source copies. Do not
rewrite those in bulk. If the distinction is consequential and unclear,
return the named file to its owner rather than silently editing evidence.
This is a bounded owner decision over listed files, not another whole-repo
search. `kb/work/README.md` and its collection contract are current navigation
and must agree with the new path. This workshop's own baseline inventory keeps
its old source paths as audit evidence until closure.

### Review and freshness identities

Relocation does not migrate the local store. `src/commonplace/store-schema.sql`
keys artifacts by path; review pairs also carry note and criterion paths, and
freshness target keys contain those identities. Moving the collection changes
note paths, local type criterion paths and the collection-conformance criterion
path. Backlink edits elsewhere also change content hashes. Consequently some
unmoved artifacts can become stale while moved ones look new. This is expected
under the recommended state policy, not evidence that the rename failed.

Existing pending jobs/full-pass packets may refer to old paths and captured
bytes. Do not execute them without reconciling their targets using the owning
workflow. Do not mass-acknowledge freshness or rewrite captured hashes merely
to make status green. If continuity becomes a release requirement, revisit
Gate 5; a safe database migration needs a separate design and tests.

## 6. Tests and acceptance

The runtime handoff records tests already run for the completed refactor. The
coverage below is still required for the future rename; runtime test success
is not evidence that relocation, packaging or consumer migration has passed.

### Existing test worklist

`reference-files.tsv` lists all **53 matched files under `tests/commonplace/`**,
including no-change generic mentions; `residual-live.tsv` gives precise
namespace-literal locations for the actionable subset. Additional scenarios
and connect fixtures are listed there too. Migrate the default Theory fixtures
and their expectations together, particularly:

- `tests/commonplace/general/test_project_paths.py`, `test_library.py`,
  `test_type_resolver.py`: generic discovery/enumeration under unrelated
  collection names, removed special helper, checkout library and local types.
- `tests/commonplace/installation/test_init_project.py`,
  `test_library_build.py`: manifest, empty scaffold, wheel/sdist library trees,
  custom-file preservation and init refresh.
- `tests/commonplace/docs/test_collection_landing_integrity.py`,
  `test_properdocs_hooks.py`, `test_type_schemas.py`,
  `test_redirect_map_integrity.py`: Theory nav/label/order, type location,
  old/new addresses and flat redirects. Generic historical `notes/old.md`
  fixtures may remain when they intentionally test arbitrary redirect keys.
- `tests/commonplace/indexing/test_promotion_candidates.py`: explicit generic
  collection input, approved no-argument behavior and report-relative links;
  `test_tag_space.py`: renamed shipped participation and arbitrary names.
- `tests/commonplace/review/test_status.py`: agreed collection-neutral JSON
  shape, scope-derived details commands and summary.
  `test_review_target_selector.py`: approved selection scope, arbitrary names
  and unchanged per-root traversal; `test_collection_conformance.py` and
  `test_type_conformance.py`: new collection/local-type criterion identities.
- Other review/freshness tests listed in the residuals: default fixture roots,
  path-bearing expected protocol/store values and pair keys. Preserve generic
  `note_path`/`criterion_path` field names and any deliberately historical data.
- `tests/commonplace/validation/test_validate_notes.py`: equal generic target
  resolution for Notes, Theory and another name, plus approved `today`/`recent`
  scope; `test_validation_unquoted_sources.py`: the bound follows the contract
  field into the relocated collection and stays off collections without it; `test_pinned_validation_contracts.py` and the flat schema
  fixture: changed collection-local identity and applicability declaration.
- `tests/commonplace/validation_helpers.py` and its full-pass/guard/article
  consumers: keep generated fixture paths and expected report paths consistent.
- Relocation suites: use Theory for current-collection examples, retain old
  Notes paths where explicitly testing the migration; preserve generic support
  for arbitrarily named collections.

Do not mechanically rename every test function/variable containing `note` or
require third-party KBs to call their own collections Theory. Fixtures using
an arbitrary collection name can remain if the test does not depend on our
shipped default. Add an explicit non-Theory collection case where a fixture
change would otherwise lose that coverage.

### Regression cases to add or make explicit

1. A new scaffold has Theory and its tag participation. Refreshing an existing
   consumer that retains Notes or another name preserves custom files and does
   not create an unwanted Theory twin under the approved refresh policy. An
   optional consumer rename demonstrates the collision stop.
2. Installed library, wheel and wheel-from-sdist contain Theory, resolve its
   internal links, and work from a consumer whose own collection is not Theory.
3. Explicit validation resolves Notes, Theory and a third name through the same
   code path. `today`/`recent` respect approved scope/ignore boundaries and do
   not silently include protected captures.
4. Promotion accepts unrelated collection names; emitted links resolve from the
   report location. No-argument behavior follows the approved scope policy.
5. Review selection follows approved eligibility independently of names and
   preserves per-root depth. Generic collection-conformance selectors and both
   relocated local type identities work.
6. The unquoted-source bound fails at the same limit in the relocated Theory
   collection, because its contract carries `unquoted-source-limit: 5`.
   Articles stays bound; collections without the field stay unbound.
7. Status JSON and human output agree on the actual selected/aggregate scope.
   No default probe or field assumes Notes or Theory. Include a repository
   with neither directory to catch renamed hardcoding.
8. Old live-page and virtual-index URLs redirect directly to live Theory pages;
   existing historical redirects still resolve without chains or shadowing.
9. Protected records, source quotes, symlinks and brief pairings meet the adopted
   preservation policy. The moved briefs remain unpublished.

### Verification commands and checks

Follow [test selection](../../../tests/README.md). Foundational paths, scaffold,
packaging and multiple consumers change: **run the full suite, including slow
tests**, not just renamed tests.

```bash
uv run ruff check .
uv run pytest -m ''
commonplace-validate theory
commonplace-validate types
commonplace-validate landings
commonplace-validate redirects
commonplace-validate lifecycle
```

Validate each other edited live artifact/collection using the relevant target;
there is no authorized repository-wide `commonplace-validate all` target.
Record pre-existing failures separately, but all tests required for the
implementation must pass. Inspect the site build's generated Theory listings,
nav order and redirects. Follow
[editable installation](../../../INSTALL.md#2-install-commonplace-as-a-user-level-tool)
for build/scaffold changes and the disposable installed scenarios documented
in `tests/scenarios/installed/README.md`. Never run `commonplace-init` in this
checkout. Test `commonplace-init`/`--check` in a disposable consuming project.

A final residual search is a drift/acceptance check, not the discovery strategy:
compare its results against the explicit history, arbitrary-collection,
generic-note and redirect-key exemptions in this packet. Do not demand zero
instances of the word `notes`. Confirm no runtime helper, root literal,
status scope or rule binding assumes a collection is named Notes or Theory.
Intentional build/scaffold/layout declarations and exact current type identities
are different from runtime eligibility assumptions; document their roles.

## 7. Suggested integration sequence and stop conditions

The implementer may choose another route with the same separation and safety:

1. Resolve gates and record the ADR; checkpoint the checkout and local state.
   Complete the separately recorded evidence prerequisite and reconcile the
   general plan with this handoff. Compare the resulting payload, backlinks
   and redirect map with these pre-sort inventories. Refresh the move/update/
   redirect worklists for that known change set and any unrelated drift before
   applying the collection move; do not stage the baseline TSVs as if they
   were the post-sort manifest.
2. Confirm the implemented runtime interfaces from resolved Gate 6 and ADR 122;
   preserve their arbitrary-collection regressions. No new scope or type-binding
   design is required. Prepare layout/build changes and relocate only after
   the evidence-split handoff, refreshed manifests and approved preservation
   route. Keep relocation in its own commit. Do not release an intermediate
   broken tree.
3. Apply local-type/schema fixes, current contracts, scaffold/template moves,
   operator documentation and complete redirect-map changes. Review whole
   artifacts rather than partially staging unrelated navigation edits.
4. Run full verification and installation/site checks. Exercise the consumer
   migration in a disposable project before publishing changed defaults.
5. Document actual frozen/state/consumer handling and remaining exceptions in
   the ADR and migration procedure. After acceptance, extract any durable
   operational guidance, remove this workshop and its Active Workshops entry.

Stop before mutation if a gate is unresolved. Stop on a destination collision,
unexplained protected-record changes, command/inventory disagreement that
changes ownership or scope, a concrete consumer requiring unsupported
compatibility, or a need to migrate review state. Report the affected paths and
choice needed. A partial implementation is not ready to ship, but a partial
inventory remains useful: retain completed findings and explicitly return the
unresolved category instead of claiming the rename is complete.
