---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Sparks memory: human capture, agent-derived wiki, deterministic collections and manifest-mediated later retrieval."
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
source-identity: https://github.com/YogiRK/sparks
reviewed-boundary: "49abddc848ea55f78518bfbbbe04c3d37a5f2705"
---

# Sparks memory report

## Boundary and evidence

This report covers retained vault material and the operations that deliver it to later agents or people at SRC-1, commit 49abddc848ea55f78518bfbbbe04c3d37a5f2705. The [boundary](boundary.md#source-register) supplies the sole source registration. The [runtime](runtime.md#runtime-account) supplies provisional invocation, recovery and adapter findings. Direct reads below extend that account through every collection extractor, affected-collection selection, index description preservation, manifest filtering, diagnostics and viewer consumption. Implementation and shipped doctrine are separate evidence layers; no target execution, actual vault, model session or causal experiment was supplied or performed.

Included: inbox preparation/archive, raw sources, semantic wiki pages and revisions, index descriptions, log blocks, task state, seven regenerated collections, manifest file/frontmatter/link/session state, instruction delivery, query, brief, diagnostics and viewer. Excluded enclosing harness/provider state prevents conclusions about conversation persistence, context precedence, model-internal learning, compaction or instruction obedience. Static embedded instructions are described but are not accumulated operational memory. Repository build admission remains the supplied runtime's scope; no new source or deployment evidence is introduced.

### Coverage inventory

“Direct” means inspected source text in this job; “supplied” means supported by the runtime member, not independently verified here. All paths are SRC-1 commit-relative paths.

| Entry point / part | Source path and inspection | Supporting records / limit |
|---|---|---|
| CLI dispatch and stdio registered tools | Direct: `cmd/sparks/main.go`, `internal/mcp/serve.go` | [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools); registered calls include affected, lint, index and tasks. No collection-regen/abort tool in this registry. No separate hook registration appears in these dispatchers. System Git hooks remain supplied runtime evidence, not a memory selector. |
| Prepare/finalize and archived raw | Direct: `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`; supplied CLI abort/Git details | [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), [MEM-OBJ-raw](#mem-obj-raw); live inbox is not a prepared snapshot. |
| Agent page creation, alias check, revisions, source links, log and index append | Direct doctrine: `internal/contract/contract.md` | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-log](#mem-obj-log), [RT-BAP-agent-contract](runtime.md#rt-bap-agent-contract); actual semantic edits/compliance unobserved. |
| Scan, tombstones, frontmatter and graph | Direct: `internal/core/scan.go`, `internal/manifest/manifest.go`, `internal/manifest/frontmatter.go`, `internal/manifest/wikilinks.go` | [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections), [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); available metadata can lag bodies. |
| Quotes, Bookmarks, Media, Ideas | Direct: `internal/collections/quotes.go`, `internal/collections/bookmarks.go`, `internal/collections/media.go`, `internal/collections/ideas.go` | [MEM-OBJ-collections](#mem-obj-collections), [MEM-RTE-collection-regeneration](#mem-rte-collection-regeneration); distinct source selectors listed below. |
| Books, ReadingList, Projects | Direct: `internal/collections/books.go`, `internal/collections/reading_list.go`, `internal/collections/projects.go` | Same collection records; archived capture and manifest routes, not just configurable raw globs. |
| Collection dispatch and header | Direct: `cmd/sparks/collections.go`, `internal/collections/collections.go`, `internal/collections/header.go` | [MEM-RTE-collection-regeneration](#mem-rte-collection-regeneration); no subsequent scan/commit in caller. Glob helper implementation not independently assessed; no completeness claim for arbitrary glob patterns. |
| Affected-collection suggestions | Direct: `internal/core/affected.go`, `internal/manifest/queries.go`, `internal/core/ingest.go` | [MEM-RTE-affected-selection](#mem-rte-affected-selection); hints and historical metadata are different selectors. |
| Index regeneration | Direct: `internal/core/index.go` | [MEM-OBJ-index](#mem-obj-index), annotation on [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). |
| Task add/complete; future task selection and brief | Direct: `internal/core/tasks.go`, `internal/core/brief.go` | [MEM-OBJ-tasks](#mem-obj-tasks); live task state, not regenerated from historical capture. |
| Query and brief | Direct: `internal/manifest/queries.go`, `internal/core/brief.go`, `internal/mcp/serve.go`; supplied CLI adapters | [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) annotation; exact metadata retrieval versus file-body reads. |
| Evaluation and rejection | Direct: `internal/lint/lint.go`; supplied fmt/lint CLI behavior | [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity), maintenance annotation; reports do not automatically reject knowledge. |
| Withdrawal and archive | Direct: contract, scan, manifest, collection extractors | Raw moves do not retract dependent wiki claims; scan filters missing wiki files from ListPages. Stale graph edges need separate qualification below. |
| Viewer | Direct: `internal/view/server.go` | [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) annotation; direct Markdown display plus manifest navigation. Render helper internals not assessed; no HTML/security assurance. |
| Init/instruction refresh, describe, product build | Direct contract and MCP describe; supplied installer/build | [RT-OBJ-contract](runtime.md#rt-obj-contract), [RT-RTE-contract-install](runtime.md#rt-rte-contract-install), [RT-RTE-product-build](runtime.md#rt-rte-product-build); external loader precedence unknown. |

## Core ideas

1. **Sources, derived prose and access state have different authority.** Raw content is the declared source of truth; wiki pages are externally authored interpretations; manifest rows are executable lookup state, not source meaning. Human source provision does not establish human approval of a particular derived page. The contract preserves reasons through source links and requested contradiction sections, but code does not verify semantic fidelity ([MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages)).

> **Raw** is the source of truth. **Wiki** is a derived view. **Manifest** tracks state for incremental operations. All three are plain files on disk (the manifest is a single SQLite file), versioned by git.
> --- `internal/contract/contract.md`

2. **Memory retrieval is staged, not a search-to-prompt guarantee.** Query returns metadata. The external agent must select and read page bodies before synthesis. Brief delivers selected log/task text but only metadata for updated pages and raw files. Caller-requested structured gathering is not unsolicited push, and delivery does not demonstrate behavioral activation ([RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume)).
3. **Generated text has several lineage paths.** Collections select quote text, URLs, captured hints or manifest fields. Index regeneration additionally preserves old agent-authored descriptions. Regeneration does not mean wholly new semantic authorship or fully reconstructible provenance ([MEM-OBJ-collections](#mem-obj-collections), [MEM-OBJ-index](#mem-obj-index)).
4. **Evaluation supplies revisit signals, not automatic revision.** Lint detects structural symptoms; brief reuses some symptoms. Retained log text can reach later synthesis, but neither log retention nor deterministic indexing establishes an automatic trace-to-behavior-policy learning loop. The supplied session budget is prose, not an implemented window manager ([RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), maintenance and consumption annotations).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw capture and inbox archive

Source-native identity: `inbox.md`, human-added `raw/` source files, CLI-appended `raw/inbox/YYYY-MM-DD.md`, and retired notes moved to `raw/archive/`. Storage substrate: ordinary vault files, optionally Git-versioned. Representational form: source prose is natural language for later human/agent interpretation; separators, dates, URL/hint tokens and paths are symbolic inputs to fixed parsers. Scan retains hashes/mtime for raw files without interpreting raw Markdown semantics. Initial content comes from human capture by doctrine; actual imported payload authorship/trust is not authenticated here. Archive copies entry content after trimming trailing newlines and grouping by capture date, rather than retaining a model conversation or semantic completion receipt. Later consumers include collection extractors and browser page reads; raw body reads by an answering agent remain externally chosen.

Closest supplied record: [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), a route rather than this payload object; no supplied object counterpart. Evidence: SRC-1, `internal/contract/contract.md`, `internal/core/scan.go`, `internal/inbox/archive.go`.

> if _, err := fmt.Fprintf(f, "---\n%s\n", strings.TrimRight(e.Content, "\n")); err != nil {
> return fmt.Errorf("write entry %d: %w", e.Index, err)
> }
> --- `internal/inbox/archive.go`

#### MEM-OBJ-wiki-pages
Label: Agent-derived wiki pages

Source-native identity: entity, concept, summary and synthesis Markdown pages under `wiki/`, including requested `## Revision` sections. Storage: files. Form: natural-language page body for agent/human interpretation; frontmatter fields have a separate symbolic lookup consumption path in [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections). Lineage: external agent derives pages from inbox/source material and existing pages; sources and dates are supplied by that writer, not recovered from a mandatory derivation receipt. Direct edits can replace content. Contract requests alias-aware dedup, preference for updating, seed maturity and explicit conflicting sources. Those are protocol-level curation/admission constraints, not software vetoes. Reasons can persist in a Revision section; later full-page reading affords their consumption, whereas metadata query does not return those reasons. Actual reasons retained and used remain unobserved.

Closest supplied records: semantic stage of [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) and consumer [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume); object distinct from both routes. Evidence: SRC-1, `internal/contract/contract.md`.

> 4. If an existing wiki page contradicts a new entry, append a `## Revision` section noting the contradiction and both sources. Never silently overwrite.
> --- `internal/contract/contract.md`

#### MEM-OBJ-log
Label: Chronological wiki operation log

Source-native identity: `wiki/log.md`. Storage: Markdown file. Form: natural-language operation summaries chunked by symbolic dated headings. Lineage: contract asks agent to append ingest change summaries, not verbatim execution traces or automatic extracted lessons. Later consumer: Brief reads complete blocks from the date window and delivers their text to an external synthesizing agent. This is operational-history read-back, not demonstrated trace-fed policy updating. No automatic saved brief or log-to-instruction transformation in the inspected Brief path. The contents of an actual log are unavailable, so granularity, reasoning retention and truthfulness cannot be assessed.

Closest supplied record: [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume); distinct retained input, not a duplicate route. Evidence: SRC-1, `internal/contract/contract.md`, `internal/core/brief.go`.

> 7. Append an entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | summary of changes`.
> --- `internal/contract/contract.md`

#### MEM-OBJ-tasks
Label: Live Tasks collection

Source-native identity: `wiki/collections/Tasks.md`. Storage: file. Form: task text and project labels are natural language for humans/agents; headings and checkbox markers are symbolic state consumed by add/done and Brief. Lineage: agent/direct edits or deterministic caller-requested appends/completions. Human capture may seed a task, but generic CLI/MCP caller identity does not establish per-task human approval. Duplicate suppression remains the agent's duty. Done selects a unique case-insensitive substring, else a sole or score-separated fuzzy match, and can reject ambiguous/not-found requests; success changes the open marker to completed. Future done calls omit completed tasks and Brief omits them from open count/preview. Historical capture does not overwrite this live status.

Closest supplied record: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); distinct payload with two actual consumers. Evidence: SRC-1, `internal/core/tasks.go`, `internal/core/brief.go`, `internal/contract/contract.md`.

> lines[idx] = strings.Replace(lines[idx], "- [ ]", "- [x]", 1)
> --- `internal/core/tasks.go`

#### MEM-OBJ-index
Label: Wiki index and preserved descriptions

Source-native identity: `wiki/index.md`. Storage: file. Form: symbolic wikilink catalog and source counts plus natural-language descriptions interpreted by readers. Lineage: agent appends entries by doctrine; Index later regenerates type-grouped links from ListPages while preserving descriptions parsed from the existing file, matched by folded wiki-relative path then folded title. The resulting text is neither raw capture nor wholly regenerated from page content. An unmatched old description can disappear; no semantic validation updates a matched description when its page changes. File-reading agents/humans can consume this catalog; query itself does not read its description text. It is a navigation affordance, not automatically injected model context.

Closest supplied record: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); distinct file whose retained descriptions are an input to the next rebuild. Evidence: SRC-1, `internal/core/index.go`, `internal/contract/contract.md`.

> desc, kept := descriptions[linkKey]
> if !kept {
> desc, kept = descriptions[titleKey]
> }
> --- `internal/core/index.go`

#### MEM-OBJ-collections
Label: Regenerated collection pages

Source-native identity: seven output files in `wiki/collections/` named by OutputFilename. Storage: Markdown files. Form: extracted natural-language text and labels for people/agents, with symbolic links/frontmatter/counts from fixed rules. They are separate from live Tasks. Lineage and selected retained parts differ:

| Collection | Selector input → retained output | Provenance and interpretation limit |
|---|---|---|
| Quotes | Configured/default quote glob → parsed blockquote text and attribution | QuoteRecord has source path, but output emits text/attribution without that path; missing attribution is explicitly displayed. |
| Bookmarks | Configured/default weblinks glob → every URL and surrounding-line description, grouped by source filename title | Removes URL from description; heading is a display title rather than full source path. |
| Books | Default Quotes glob, not its override, plus archived `book:` lines → title groups and contexts | Heuristic attribution splitting; quote context truncates above 80 bytes; inbox context names archive path. |
| ReadingList | Archived `to-read:` lines → case-sensitive exact-text deduped queue | Keeps first matching archive path; no task-style read/completed status. |
| Media | Configured/default media glob → heading/filename title and first URL | Body omitted; raw-derived wikilink is generated. |
| Ideas | Configured/default ideas glob → titles grouped by status plus raw paths | Contrary to the contract's “+ inbox hints” table entry, extractor does not read archived inbox; scanned H1 assignments can replace earlier H1s. |
| Projects | Manifest entity pages tagged project → wikilinks grouped by maturity | Maps working/stable/seed/historical to Building/Shipped/Exploring/Archived; these are display interpretations of maturity, not observed shipping evidence. |

All outputs use `sources: []` and reset created/updated to the regeneration date. The blanket `maturity: stable` is generated metadata, not proof of human review. Reasons for semantic claims in sources are generally not carried through these projections. Later readers can open the output pages, including via the viewer; after scan they become manifest-query candidates. No automatic consumer needs the complete extracted source bodies. Closest supplied record: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); this aggregate records the payload family with its distinct parts, while the route below owns write controls. Evidence: SRC-1, all seven `internal/collections/` extractors named in the coverage table and `internal/collections/header.go`.

> maturity: stable
> sources: []
> created: %s
> updated: %s
> --- `internal/collections/header.go`

> quotes, err := parseQuotesFromGlob(v.Root, DefaultGlobs["Quotes"])
> --- `internal/collections/books.go`

> "working":    "Building",
> "stable":     "Shipped",
> "seed":       "Exploring",
> "historical": "Archived",
> --- `internal/collections/projects.go`

#### MEM-OBJ-manifest-projections
Label: Manifest file, frontmatter and link projections

Source-native identity: SQLite files/frontmatter/wikilinks state in `sparks.db`. Storage: SQLite, including WAL setup; form: symbolic records consumed by SQL/Go. Lineage: scan derives hashes, size, mtime and scan time from files, frontmatter from wiki headers, and resolved link edges from page bodies plus page titles/aliases. Raw file contents remain opaque to this parser, not inaccessible to later agents. This is access/state metadata, not stored semantic embeddings, opaque learned policy payloads or full source-body summaries. Text-valued title/alias/source fields are symbolic selectors in Query; their display to an agent does not substitute for the page body.

Consumers: query, link resolution, lint, index, Projects, affected selection, Brief metadata and viewer navigation/backlinks. Thus these rows have deterministic selection authority even when a prose source is not loaded. Deletion marks file rows; ListPages excludes deleted file parents. Graph replacement occurs only for current listed pages, with a separate stale-edge qualification below. Initial database creation/migration is supplied boundary/runtime coverage; subsequent transformations are directly inspected. Separate ingest-history referent already exists as [RT-OBJ-ingests](runtime.md#rt-obj-ingests), so this object excludes those lifecycle rows. Closest other supplied record: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write), a producer route, not a duplicate object. Evidence: SRC-1, `internal/core/scan.go`, `internal/manifest/manifest.go`, `internal/manifest/frontmatter.go`, `internal/manifest/wikilinks.go`.

> FROM frontmatter f
> JOIN files fl ON fl.path = f.path
> WHERE fl.deleted = 0 AND f.path LIKE 'wiki/%'
> --- `internal/manifest/wikilinks.go`

### Routes

#### MEM-RTE-collection-regeneration
Label: Collection regeneration and later page consumption
Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

This is the collection-specific part of the supplied multi-operation route, not a competing identity. Trigger: explicit CLI `collections regen [name...]` or exposed Regenerate library call. Caller chooses names/dry-run; code chooses configured/default inputs and runs the seven fixed extractors. It writes [MEM-OBJ-collections](#mem-obj-collections), which a later viewer/page-reading agent can consume. Owner: caller schedules, deterministic extractors transform/admit and filesystem writes persist. Context: raw files, archived inbox, manifest and collection config; no model invocation. Evidence: SRC-1, `cmd/sparks/collections.go`, `internal/collections/collections.go`, extractor paths in the inventory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-collection name/path/bytes or error entries; dry-run generates output without writing it.
- Later read-back: Files persist for later direct page reads/viewer; scan is separately needed to refresh their metadata for query/index consumers.
- Delegated visibility: CLI caller receives results; external harness sharing and actual later agent visibility are uninspected.
- Selection predicate: Explicit names or OrderedNames, then extractor-specific inputs in the collection object table; no relevance ranking or token budget.
- Invalidation or expiry: Requested regeneration replaces whole generated files, overwriting manual edits; omitted outputs remain until separately regenerated/removed.
- Activation or effect: Filesystem replacement is implemented; later changed synthesis from the generated text is unobserved.
- Evidence limits: Source wiring, not a completed regeneration or accurate extraction result; some extractor open/read failures are skipped, so successful dispatch is not source completeness.

Admission: caller requests outputs, software determines exact text; no content-specific human approval or semantic oracle. Unknown names and extractor failures become result errors, I/O can return an error; dry-run is caller-controlled. No transaction or rollback spans outputs. Recovery is external edit/Git or another regeneration, not restored prior generated files. Guidance is compiled extractor rules plus source-native capture conventions; outputs, not evaluation reasons, persist. Operating mode: open maintenance. The CLI caller neither scans nor commits afterward, despite stronger contract language. Only affected-name suggestions are incremental; requesting all collections still regenerates all seven.

> body, err := extractor(v, db, glob)
> if err != nil {
> results = append(results, Result{Name: name, Error: err.Error()})
> continue
> }
> --- `internal/collections/collections.go`

#### MEM-RTE-affected-selection
Label: Historical change metadata selects collection suggestions

Trigger: CLI/MCP affected request. Progression: latest completed ingest timestamp → nondeleted file scan times → prefix or special-case mapping → collection names plus reasons → caller may request regeneration. Owner: fixed Go/SQL selector; caller owns subsequent action. It reads [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections) and [RT-OBJ-ingests](runtime.md#rt-obj-ingests), not raw page semantics. Closest supplied records: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) is downstream regeneration, [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) has a different prepare-time hint selector. Neither is this separate historical lookup. Evidence: SRC-1, `internal/core/affected.go`, `internal/manifest/queries.go`, `internal/mcp/serve.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Affected names and per-name triggering path/reason lists, or error.
- Later read-back: A later invocation consumes prior scan timestamps and completed-ingest history to suggest work; the returned suggestion itself is not automatically persisted or executed.
- Delegated visibility: Requesting CLI/MCP caller; onward agent delegation is uninspected.
- Selection predicate: Nondeleted files scanned after latest completion, or all nondeleted files before any completion; configured/default glob prefix matching, wiki/entities prefix for Projects, raw/inbox prefix for Books/ReadingList.
- Invalidation or expiry: Next completed-ingest timestamp changes the baseline; no queued work receipt survives this result automatically.
- Activation or effect: Metadata influences returned maintenance suggestions; regeneration depends on another call and exercised agent scheduling is unobserved.
- Evidence limits: Selector is not a complete dependency graph; Books also reads default quote files but its special-case suggestion only checks inbox archive changes. Deleted file paths are excluded from the changed set.

No content change is admitted here; no answer oracle or candidate grader. It is an open diagnostic request. It is not an automatic trace-fed instruction update: operational metadata determines a suggestion, not a durable revised behavior rule. Prepare's hint-based suggestions are distinct and include Tasks even though Tasks cannot be regenerated.

> if name == "Projects" {
> if anyMatches(changed, func(p string) bool { return strings.HasPrefix(p, "wiki/entities/") }) {
> reason[name] = append(reason[name], "wiki/entities/* changed")
> }
> continue
> }
> if anyMatches(changed, func(p string) bool { return strings.HasPrefix(p, "raw/inbox/") }) {
> reason[name] = []string{"raw/inbox/* changed"}
> }
> --- `internal/core/affected.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)

Memory-specific distinction: prepare returns the parsed live entry list without persisting entry snapshots. Finalize archives a newly parsed live list, not proof that the derived wiki contains every entry. Raw-to-wiki derivation is agent protocol; raw-to-archive copying is deterministic. Persisted semantic revision reasons exist only if the writer adds them. An archive is retained capture, not a learned summary, and an ingest row is recovery metadata, not a page-level semantic acceptance record. Finalize clears after archive and runs Scan but does not invoke collection regeneration. Evidence: SRC-1, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`; supported batch-budget counterexample and minimum passages are already in the supplied record.

#### On [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Memory curation/admission is operation-specific. Scan software admits derived metadata after filesystem observation; humans/agents write the source files independently. Size+mtime can bypass reparse; per-file errors do not create a semantic admission barrier. Index software preserves matched old descriptions while replacing links; TasksAdd accepts nonempty caller text without dedup; TaskDone can reject ambiguity but a fuzzy winner receives no second approval. Collections use the distinct part route above. Lint's fixed checks return current diagnostic issues; inspected Run does not retain those issues or automatically rewrite pages. Brief later recomputes stale/thin from lint rather than loading a saved critic report. Human invocation does not establish per-content review of any output. Recovery is external file edits/Git, not automatic semantic rollback. Evidence: SRC-1, `internal/core/scan.go`, `internal/core/index.go`, `internal/core/tasks.go`, `internal/lint/lint.go`, `internal/core/brief.go`; supplied record establishes CLI diagnostics behavior.

> issues = append(issues, checkThinAndStale(v, pages)...)
> issues = append(issues, checkDeadSources(v, pages)...)
> issues = append(issues, checkDuplicateAliases(pages)...)
> --- `internal/lint/lint.go`

#### On [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume)

Read-back targeting and budget: Query's externally requested title/alias/tag/type/maturity/graph/state filters return PageInfo metadata from ListPages, not page text, source body or Revision rationale. Exact title/alias/tag matches are case-insensitive; filters combine with AND, without result/token cap in Query. Foreground agent then chooses external file reads by doctrine. This is an afforded external-agent content route plus wired metadata delivery; actual model context inclusion and changed answers remain uninspected. QueryFilter.Thin is not tested in Query; generic arbitrary frontmatter lookup claimed by the contract also exceeds the fields inspected here. Metadata selection authority belongs to fixed rules; selected prose influences an agent only through its interpretation.

Brief is another explicit request, not background push. Code selects log blocks by heading date; raw file metadata by stored mtime excluding raw/inbox and raw/archive; wiki metadata by updated date; revisit paths by fresh lint/seed-orphan signals; open task count and first five texts in file order. Default window is seven days; there is no overall token cap. It returns log text but not full raw/wiki bodies or task-section context. The changed knowledge remains in files; Brief itself neither saves a summary nor replaces a conversation checkpoint. Supplied doctrine says stdout unless asked to save. A later agent can synthesize from retained operation history, but this does not demonstrate automatic learning from a trace.

Viewer's requested URL reads a Markdown body, while its navigation/backlinks come from manifest state. A body can reflect an edit before a scan refreshes catalog metadata. Requested raw and wiki routes allow browser consumption without any model. No consumer authority to execute source instructions is implemented by these read paths; source provenance does not make arbitrary page prose harness policy. Evidence: SRC-1, `internal/manifest/queries.go`, `internal/manifest/wikilinks.go`, `internal/core/brief.go`, `internal/view/server.go`, `internal/contract/contract.md`.

> r.LogEntries = logDays
> --- `internal/core/brief.go`

> data, err := os.ReadFile(full)
> if err != nil {
> http.Error(w, fmt.Sprintf("page not found: %s", relPath), http.StatusNotFound)
> return
> }
> --- `internal/view/server.go`

#### On [RT-OBJ-contract](runtime.md#rt-obj-contract)

Static instruction lineage is embedded product text copied to a vault, not memory derived from operation. A copied file can persist across sessions and diverge from a newer binary when preserved by default. Its behavioral force is still external loader/model interpretation, not permission enforcement. Read paths for the contract include describe and conventional harness loading; those do not prove activation. Evidence supplied by [RT-RTE-contract-install](runtime.md#rt-rte-contract-install) and [RT-BAP-agent-contract](runtime.md#rt-bap-agent-contract), including minimum passages; direct SRC-1 `internal/contract/contract.md`, `internal/mcp/serve.go` confirm content and describe delivery.

## Write side

The write mechanisms above must not be collapsed into “the model remembers.” Human capture supplies evidence; the external agent authors derived prose under non-enforcing source/revision rules; deterministic code appends archive content, derives access metadata, extracts collection projections and mutates task markers. Actual initial vault content and external-agent decision traces are unavailable, but that uncertainty does not erase directly inspected subsequent transformations ([MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-RTE-collection-regeneration](#mem-rte-collection-regeneration)).

A retained rationale route is specifically afforded by Revision sections → later full page read. Neither Query metadata nor most collection summaries carries that rationale. Index descriptions survive through a separate file-to-file preservation step, not fresh summarization. Log blocks preserve agent-written operation summaries; Brief forwards selected blocks for synthesis. There is no demonstrated raw-conversation → automatic compacted checkpoint → later invocation chain within these inspected routes; external harness compaction and alternative checkpoint forms remain outside scope, not established absent system-wide. No model parameters or embeddings are written by these deterministic transformations ([MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-log](#mem-obj-log), consumption annotation).

**Rejection and withdrawal have limited downstream force.** Ambiguous task completion can be rejected; unknown collection names/failed extraction can leave prior files intact; lint issues report symptoms without vetoing finalize or retracting a claim. Raw retirement is a human move by doctrine. Existing source paths can then become dead-source warnings, but derived prose remains unless separately edited. A new regeneration only removes items absent from that extractor's current input; an item archived elsewhere may remain in old generated outputs until regeneration. ReadingList has no completed/withdrawn state beyond changing its source set, unlike Tasks (SRC-1, `internal/lint/lint.go`, `internal/collections/reading_list.go`, `internal/core/tasks.go`; [MEM-OBJ-collections](#mem-obj-collections)).

A missing wiki file is tombstoned and omitted from ListPages, so future Query/Index/Projects catalogs drop that page. That is not complete withdrawal from graph consumers: rebuildLinks iterates only current pages, ReplaceLinks clears edges only for the given current source, and IncomingLinks/BrokenLinks do not join against nondeleted source files. Thus edges previously originating from a removed page can remain and affect orphan/backlink checks. Direct file reads fail if the file is gone, but surviving metadata/links are not equivalent to source content. This qualifies, rather than rejects, the supplied scan graph-rebuild description (SRC-1, `internal/core/scan.go`, `internal/manifest/manifest.go`, `internal/manifest/wikilinks.go`; [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections)).

> return d.queryLinks(`SELECT source, target, COALESCE(resolved, '') FROM wikilinks WHERE resolved = ?`, target)
> --- `internal/manifest/wikilinks.go`

## Read-back

| Retained input | Later trigger and selector | Delivered material / consumer / authority |
|---|---|---|
| Semantic pages, sources and revisions | Question → agent's query filters → external page read | Metadata first, then selected body to agent by doctrine; interpreted knowledge, not mechanically enforced instruction. Actual body-read choice and influence unobserved. |
| Log and tasks | Brief request → date window and first-five-open rule | Complete selected log blocks; task texts/count without all task context; agent synthesizes. No automatic saved derived policy. |
| Manifest file/frontmatter/graph | Query, lint, affected, index, Projects, viewer requests | Fixed-rule selection authority; paths/titles/counts/status, not source-body meaning. |
| Raw archive hints and source files | Explicit collection regeneration | Extracted payload persists in generated files; later browser/file readers receive its projection rather than all original context. |
| Old index descriptions | Index request → path/title-key match | Existing natural-language descriptions survive into a new catalog for future readers; code preserves text without reevaluating truth. |
| Live task state | Later done or Brief | Completed markers exclude tasks from future open candidates/previews; actual later operation remains unobserved. |
| Copied contract | Later external harness load or explicit describe | Static instructions, not read-back of accumulated experience; precedence/compliance external. |

These are caller-requested routes, not unsolicited delivery. Prepare returns all entries even though doctrine suggests 10–15 per session; Brief caps task preview, not complete context. No inspected Sparks mechanism removes old turns, isolates a sub-agent frame, pops such a frame or reloads an evicted conversation summary. External page retrieval supplies data by value; an unreturned path is only a pointer the agent may choose to follow. Therefore a stack-frame analogy is not evidenced here, and manifest paths are not model-window liveness references. Harness window control remains uninspected. These limits concern the inspected dispatch/core/contract paths, not a claim about every possible host ([RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume); SRC-1, `internal/core/brief.go`, `internal/mcp/serve.go`).

## Integration issues

1. **Scan does not make missing-frontmatter pages normal query candidates.** The supplied [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity) quotes a scan comment saying path queries can succeed. Actual refreshFrontmatter deletes the metadata row on parse failure, and ListPages inner-joins frontmatter. Query therefore omits that page; WikiFilesWithoutFrontmatter can still find it for lint. The runtime's broader tolerated-scan finding is sound, but the quoted path-query implication must not be adopted as implementation fact. Evidence: SRC-1, `internal/core/scan.go`, `internal/manifest/wikilinks.go`, `internal/manifest/queries.go`; [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections).
2. **Graph rebuild has a withdrawal limit.** Supplied [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) says missing files are marked deleted and edges replaced. This is true for currently listed sources, not wholesale edge removal for disappeared source pages. Stale outgoing edges can remain available to graph consumers after deletion. The consequence is narrower orphan/backlink reliability, not continued full-body availability. Evidence and passage in Write side; [MEM-OBJ-manifest-projections](#mem-obj-manifest-projections).
3. **Suggestion coverage differs from extraction dependencies.** Books consumes quote files, but affected's Books special case only tracks inbox archive changes, and deleted paths are not returned by ChangedSinceLastIngest. Prepare suggestions are a third hint selector, not proof of eventual regeneration. No automatic refresh guarantee follows. Evidence: SRC-1, `internal/core/affected.go`, `internal/core/ingest.go`, `internal/manifest/queries.go`, `internal/collections/books.go`; [MEM-RTE-affected-selection](#mem-rte-affected-selection), [MEM-OBJ-collections](#mem-obj-collections).
4. **Shipped doctrine can overstate what generated text means.** Ideas' documented inbox-hint input is not read by its extractor; Projects maturity-to-shipping labels and generated stable metadata do not establish review or shipping events. Query's generic frontmatter and thin claims also exceed inspected implementation. These qualify source claims rather than contradict the supplied runtime's already bounded lookup account. Evidence: SRC-1, `internal/contract/contract.md`, `internal/collections/ideas.go`, `internal/collections/projects.go`, `internal/collections/header.go`, `internal/manifest/queries.go`; [MEM-OBJ-collections](#mem-obj-collections), [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume).
5. **Unresolved actual agent integration.** The supplied source cannot show which file bodies/revision reasons entered a real question's context, whether the copied contract was loaded, whether source prose was misread as instruction, or whether any resulting answer/behavior improved. This prevents activation, semantic-completeness, trace-learning benefit and exercised-learning claims; it does not prevent the wired storage/selection findings. Concerns [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-log](#mem-obj-log), [RT-BAP-agent-contract](runtime.md#rt-bap-agent-contract), [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume). Evidence limit: boundary lacks vault/session traces and harness implementation.

Record overlap check: collection regeneration is explicitly a part of the supplied maintenance route; the affected-selection route has distinct endpoints and output. New objects identify retained payloads/projections not separately declared in runtime; ingest lifecycle and static contract are deliberately annotated/reused rather than redeclared. No possible duplicate requiring supersession was found. Peer memory/epistemic/workflow findings were not supplied; cross-specialist conflicts cannot yet be assessed.

## Limitations and checks

Source identity recheck: checkout HEAD was read as 49abddc848ea55f78518bfbbbe04c3d37a5f2705, equal to the boundary. All new source reads are paths in that registered checkout; no other revision, external page or prior characterization was used. Method identity: supplied memory type, boundary/runtime types, collection contract, records contract and worker rules govern this member. Only assigned report, empty answers and worker identity outputs were written; no target execution or source mutation was performed.

The report establishes storage/selection wiring and requested semantic behavior, not exercised retention quality or causal benefit. Supporting glob/render helper internals and external harness decisions remain uninspected where explicitly named. No independent semantic evaluator, cross-operation rollback guarantee or complete deletion propagation is inferred from diagnostic labels.

Deterministic validation: completed with the invocation's validate-output command; successful result recorded after checking the complete output. Validation checks form, identity and quotation occurrence, not analytical truth or acceptance.
