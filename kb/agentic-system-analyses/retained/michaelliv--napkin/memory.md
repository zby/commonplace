---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Napkin's retained Markdown, context note, retrieval caches, auxiliary stores and benchmark memory consumers at the frozen revision."
run-id: AAS-2026-10-12-napkin-2b85bef38252-01
source-identity: "https://github.com/Michaelliv/napkin"
reviewed-boundary: "7582d6a46f5a11995956e60a59c41a5b242109f1"
---

# Napkin memory report

## Boundary and evidence

Napkin retains files for later caller-selected retrieval. The memory scope includes Markdown notes, daily notes, NAPKIN.md, templates and folder descriptions; configuration and derived retrieval caches; base, canvas and bookmark surfaces; distill/tend instructions; and all three shipped benchmark ingestion/answer drivers. The source register is in [boundary](boundary.md). Every source reference below is SRC-1 at the shared frozen commit. Direct source inspection supplies implementation or doctrine/design evidence, never observed operation. HEAD was rechecked as `7582d6a46f5a11995956e60a59c41a5b242109f1`, and the checkout had no reported changes.

The supplied [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), [RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault), [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) and [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change) provide the baseline, not an inspection limit. Their memory-specific findings are annotated rather than redeclared. The following inventory distinguishes added direct reads from inherited findings. Source paths are commit-relative.

| Entry point / memory operation | Source paths and inspection | Coverage / admission, consumer and limit |
|---|---|---|
| CLI dispatch, SDK exports and hook | Direct: `src/main.ts`, `src/sdk.ts`, `src/index.ts` | Reviewed complete dispatch/export surfaces. CLI preAction hook captures stdout for clipboard; it is not a retention scheduler. Exposed auxiliary paths are covered below. External registered kb_search/kb_read tools remain outside SRC-1. |
| Discovery, initialization, configuration | Direct: `src/utils/vault.ts`, `src/core/init.ts`, config defaults/effectiveConfig in `src/utils/config.ts`; supplied configuration-write account | Caller selection plus missing-file scaffold checks; [RT-OBJ-vault-info](runtime.md#rt-obj-vault-info), [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change). Generic caller does not identify a human approval decision. Config write/Obsidian synchronization details rely on supplied runtime, not fresh full inspection. |
| Markdown create, read, append/prepend, move, delete | Direct: `src/core/crud.ts`, `src/utils/files.ts`, `src/utils/vault-internals.ts` | Existing-target guard is only one admission branch. [MEM-OBJ-markdown-notes](#mem-obj-markdown-notes); annotations on mutation/retrieval. Trash exclusion does not block exact-path reads. |
| Distill / tend | Direct: both `skills/*/SKILL.md` | Model admission and conservative curation are requested policies; supplied skill routes and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). No execution or enforced trust boundary supplied. |
| Background automatic distillation | Direct: `docs/distill.md`; supplied external-integration gap | [MEM-RTE-background-distill](#mem-rte-background-distill). Claimed separate model writes; scheduler, parse/admission details and actual injection unavailable. |
| Search, snippets and search cache | Direct: `src/core/search.ts`, `src/utils/search-cache.ts`, `src/utils/fingerprint.ts` | [MEM-OBJ-search-cache](#mem-obj-search-cache); caller query/limit/folder, symbolic cache admission. Dependency index payload is opaque here, not a prose summary or embedding. |
| Overview and context | Direct: option/constants, exclusions, about extraction, note-data, keyword selection and assembly/cache ranges of `src/core/overview.ts`; complete `src/commands/overview.ts`, `src/utils/overview-cache.ts` | [MEM-OBJ-napkin](#mem-obj-napkin), [MEM-OBJ-overview-cache](#mem-obj-overview-cache); [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes). Some tokenizer/collapse internals not fully inspected: no exhaustive quality or exposure claim. |
| Daily, template insert/read, property/task edits | Direct: complete `src/core/daily.ts`, `src/core/templates.ts`, `src/core/properties.ts`, `src/core/tasks.ts`, `src/utils/frontmatter.ts` | [MEM-RTE-auxiliary-edits](#mem-rte-auxiliary-edits), [MEM-OBJ-note-templates](#mem-obj-note-templates). Caller admits content; existence/parse/task checks are structural, not truth tests. |
| Links, tags, aliases, metadata, outline and word counts | Direct: complete `src/core/links.ts`; SDK/dispatch for remaining projections | Link diagnostics feed tend and backlink ranking. Tag/alias/outline extraction internals not fully read; no claim of semantic validation from these displays. They expose existing files, not separately established durable knowledge stores. |
| Base query/create | Direct: complete `src/core/bases.ts`; collection/database and query assembly ranges in `src/utils/bases.ts` | [MEM-OBJ-base](#mem-obj-base), [MEM-RTE-structured-access](#mem-rte-structured-access), auxiliary edits. SQL/filter/formula internals partly uninspected: prevents complete expression-semantics assessment. |
| Canvas and bookmarks | Direct: complete `src/core/canvas.ts`, `src/core/bookmarks.ts`, SDK/dispatch | [MEM-OBJ-canvas](#mem-obj-canvas), [MEM-OBJ-bookmarks](#mem-obj-bookmarks), structured-access route. No ordinary search indexing of these payloads established. |
| Graph | Direct: node collection, link construction and graph-data ranges in `src/commands/graph.ts`; dispatch | Snapshot includes full Markdown content, excluding templates and index.md. Renderer/server continuation not fully inspected: human UI consumption is afforded by dispatch/description, not an audited delivery or retention loop. Not treated as a new persistent memory object. |
| LongMemEval | Direct: ingestion, answer/trace parsing/cleanup and result-log ranges in `bench/longmemeval-eval.ts`; supplied prompt/scoring account | Annotation on [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), [MEM-OBJ-evaluation-results](#mem-obj-evaluation-results). Driver admits raw rounds; evaluation does not gate retained knowledge. |
| LoCoMo / HotpotQA | Direct: ingestion, answer invocation/parsing/cleanup ranges of `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`; LoCoMo shared-vault/result-log loop | [MEM-RTE-benchmark-variants](#mem-rte-benchmark-variants), [MEM-OBJ-session-summary](#mem-obj-session-summary). Supplied summaries have opaque upstream derivation; retained results are not later answer context. |
| Overview exposure scorer | Direct: complete `bench/overview-exposure.ts`, `bench/exposure-all.sh` | Scorer's corpus call disagrees with current signature; see integration issues. Prevents treating shipped scorer as executable validation of keyword quality. |
| Installed update, release and legacy forwarders | Supplied runtime/boundary only | Product-version changes, not established trace-fed knowledge updates; external package implementation excluded from memory conclusions. |

External pi, providers, pi-napkin and the benchmark extension, actual datasets/results and private corpora are unavailable as described in boundary. Provider weights are an opaque external component, not a locally retained vault part: [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model). No target, test, evaluator or model was executed. Uninspected available ranges above limit completeness of individual internals, not the existence of covered source-native paths.

## Core ideas

1. **Durable content and routing metadata are separate.** Notes hold readable knowledge or raw dialogue. Paths, mtimes, links and title terms affect access. Search adds backlinks and relative recency to lexical relevance; it does not score truth or distinguish user evidence from assistant assertions. NAPKIN.md provides caller-requested broad context, while `_about.md` describes folder intent. See [MEM-OBJ-markdown-notes](#mem-obj-markdown-notes), [MEM-OBJ-napkin](#mem-obj-napkin) and the retrieval annotation (SRC-1, `src/core/search.ts`, `src/core/overview.ts`).
2. **Trace transformation lives in agent guidance, not the core.** Distill asks a host model to turn session material into declarative, topic-based notes, preserve decisions' reasons, mark generalizations and integrate contradictions. Tend edits the resulting library. These are separate admission policies from the generic caller's structural I/O checks. The benchmark provides a counterexample to a system-wide distilled-memory account: it writes raw dialogue and supplied summaries with skills disabled. See the skill annotations and [MEM-RTE-benchmark-variants](#mem-rte-benchmark-variants) (SRC-1, both skill files, `bench/locomo-eval.ts`).
3. **Progressive disclosure is a callable route, not mandatory context budgeting.** Overview reduces the visible map; search truncates hit count and optionally returns matching lines; read returns a whole file. The code has per-operation size controls, not a shared model-token budget. Direct reads bypass the staged route. Ordinary defaults are depth 3, quality-governed keywords (0), search limit 30 and zero surrounding snippet lines. A matching line can still be long; full NAPKIN.md has no enforced 200-word limit. See retrieval annotation and [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes) (SRC-1, `src/utils/config.ts`, `src/core/search.ts`, `src/core/crud.ts`, `src/core/overview.ts`).
4. **Cached projections are derived memory, not authored epistemic warrants.** Search cache retains an index and access metadata; overview cache retains a display projection plus context. Later invocations consume these under fingerprint checks. Normal edits invalidate them, but preserved mtimes can leave stale routing or context. Search rereads content for snippets even while reusing an older index. See [MEM-OBJ-search-cache](#mem-obj-search-cache) and [MEM-OBJ-overview-cache](#mem-obj-overview-cache) (SRC-1, `src/core/search.ts`, `src/utils/fingerprint.ts`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-markdown-notes
Label: Markdown notes and their access metadata

Source-native identity: vault `.md` files, including daily notes and `_about.md`. Storage substrate: files under resolved contentPath. Representational form: natural-language bodies at human/model readers; symbolic frontmatter fields, task markers and wikilink targets at parsers. Arbitrary code or prose remains uninterpreted bytes to CRUD. Notes can originate from caller input, copied templates, skill-mediated session synthesis, imported benchmark text or pre-existing files; generic initialization provenance and human authorship are unresolved. Distill asks for reasons and inferred-claim marks, but the core does not enforce their presence. Consumers: later full reads, lexical search, overview extraction, property/task/link/base projections and skill-consuming agents. Evidence and overlap: SRC-1, `src/core/crud.ts`, `src/core/daily.ts`, `src/core/overview.ts`, `src/utils/bases.ts`; distinct persisted objects used by [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) and [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), not replacements for those routes. Paths/stat mtimes are access metadata, not stored reasons or evidence quality. Trash is a location change, not semantic erasure; exact-path resolution bypasses listFiles exclusions.

> const ref = fileRef.endsWith(".md") ? fileRef : `${fileRef}.md`;
>     const fullPath = path.join(vaultPath, ref);
>     return fs.existsSync(fullPath) ? [ref] : [];
> --- `src/utils/files.ts`

#### MEM-OBJ-napkin
Label: NAPKIN.md broad context

Source-native identity: content-root `NAPKIN.md`. Storage substrate: Markdown file, also copied into overview-cache result. Representational form: natural-language context, possibly symbolic wikilinks at other consumers. Lineage: empty bare-vault initialization; scaffold template text; caller/skill edits; benchmark-generated context or roster. The coding template offers project description, conventions, decisions and active work; actual file content is caller-controlled. Consumer: overview returns nonempty trimmed text without query selection; a host may then deliver it to a model. Distill's “always-loaded” description does not prove external automatic loading. Knowledge and convention authority depends on that consumer, not filename. SRC-1, `src/utils/vault.ts`, `src/core/init.ts`, `src/templates/coding.ts`, `src/core/overview.ts`, `skills/distill/SKILL.md`. Distinct persisted part used by [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), not a duplicate route or VaultInfo.

> const contextPath = path.join(contentPath, "NAPKIN.md");
>   const context = fs.existsSync(contextPath)
>     ? fs.readFileSync(contextPath, "utf-8").trim()
>     : undefined;
> --- `src/core/overview.ts`

#### MEM-OBJ-note-templates
Label: Persisted note templates

Source-native identity: `Templates/*.md` by default, configurable templates.folder. Storage substrate: Markdown files scaffolded or edited in the vault. Representational form: natural-language section guidance plus symbolic date/time/title placeholders. Lineage: shipped VaultTemplate.files or caller-created content; initial author of a generic existing template unresolved. Update consumer: create can copy a resolved template instead of supplied content; ensureDaily copies Daily Note if present; insertTemplate substitutes variables then concatenates to a target. readTemplate substitutes only when requested. Thus substitution is not universal across template consumers. The external distillation design also claims to read templates, with implementation unavailable. SRC-1, `src/core/templates.ts`, `src/core/daily.ts`, `src/core/crud.ts`, `src/core/init.ts`, `docs/distill.md`. Persisted output/use of [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change), distinct from its process-local registry.

> templateContent = resolveVariables(templateContent, title);
>
>   const targetPath = path.join(v.contentPath, targetResolved);
>   const existing = fs.readFileSync(targetPath, "utf-8");
>   fs.writeFileSync(targetPath, existing + templateContent);
> --- `src/core/templates.ts`

#### MEM-OBJ-search-cache
Label: Search index and metadata cache

Source-native identity: `SearchCacheData` in `search-cache.json` under configPath. Storage substrate: JSON file. Representational form: symbolic serialized index string, document IDs/paths/basenames/mtimes and backlink counts; no embedding endpoint in the inspected writer. Serialized dependency index internals are opaque here; metadata is readable but not a summary of all payload semantics. Lineage: buildIndex reads all selected Markdown bodies and basenames; backlink counts scan the whole vault. The serialized index is retained while separate cached docs omit content; cached-load branch rereads bodies. Consumer: loadSearchCorpus for later query ranking and overview probes. Authority: affects result order and selection, not truth or knowledge acceptance. Fingerprint mismatch or JSON read/parse failure is a miss; index-load recovery is not established. SRC-1, `src/core/search.ts`, `src/utils/search-cache.ts`, `src/utils/fingerprint.ts`. Distinct retained object of [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval).

> docs: docs.map(({ content: _, ...rest }) => rest),
>       backlinkCounts: Object.fromEntries(backlinkCounts),
> --- `src/core/search.ts`

#### MEM-OBJ-overview-cache
Label: Cached overview projection

Source-native identity: `OverviewCacheData<VaultOverview>` in `overview-cache.json`. Storage substrate: JSON under configPath. Representational form: symbolic folder counts, keyword/coverage-number arrays, tags and cache keys; natural-language about/context values at the caller. Lineage: algorithmic extraction from note bodies, titles/frontmatter, folder names and `_about.md`, with unchanged full trimmed NAPKIN.md copied into result. This is not model-authored summarization or conversation compaction. Consumer: later getOverview returns the cached result on fingerprint/options match; CLI displays context/about/keywords but leaves tags in JSON. Authority: orientation and search suggestions; cached result is not a complete vault account. SRC-1, inspected `src/core/overview.ts` ranges, `src/commands/overview.ts`, `src/utils/overview-cache.ts`, `src/utils/fingerprint.ts`. Distinct from search cache though both belong to [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval).

> if (data.fingerprint !== fingerprint) return null;
>     if (data.optionsKey !== optionsKey) return null;
>     return data.result;
> --- `src/utils/overview-cache.ts`

#### MEM-OBJ-base
Label: Base query definitions

Source-native identity: `.base` YAML and BaseConfig. Storage substrate: caller-authored files; transient SQLite database derived from Markdown on query. Representational form: symbolic filters, view/order/limit/formula definitions; natural-language values in returned metadata remain human/model-readable. Lineage: generic existing base authorship is unknown; buildDatabase gathers paths, stats, frontmatter, tags, links, backlinks and embeds. It is not a persistent SQL knowledge store. Consumer: queryBaseFile builds the database, executes selected view and closes it; result supplies columns/rows/groups/summaries/display names, not full note bodies. Authority: deterministic query selection/projection, not semantic acceptance. SRC-1, `src/core/bases.ts`, inspected `src/utils/bases.ts` collection/query ranges. No supplied counterpart for this object; auxiliary capability mention in runtime is not a declaration. [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) is closest but covers different retrieval operations.

> const config = parseBaseFile(content);
>   const db = await buildDatabase(vaultPath);
> --- `src/core/bases.ts`

#### MEM-OBJ-canvas
Label: Canvas content and structure

Source-native identity: `.canvas`, Canvas.nodes and Canvas.edges. Storage substrate: JSON files in contentPath. Representational form: symbolic IDs, geometry, type and file/URL references; text/label fields natural-language at caller readers. Lineage: caller creates empty canvas or adds/edits structure through operations; existing-file provenance unknown. Consumers: canvasRead, nodes listing and subsequent node/edge mutations. File/URL reference is retained access information; resolveCanvas does not load referenced note contents or fetch URLs. Authority: caller-visible organization and mutable content; no inspected automatic model injection or Markdown search admission. SRC-1, `src/core/canvas.ts`, `src/sdk.ts`, `src/main.ts`. Distinct from runtime's Markdown mutation/retrieval routes, which only mention this capability in prose.

> const content = fs.readFileSync(path.join(vaultPath, filePath), "utf-8");
>   const canvas: Canvas = JSON.parse(content);
> --- `src/core/canvas.ts`

#### MEM-OBJ-bookmarks
Label: Bookmark access records

Source-native identity: Bookmark entries in `bookmarks.json` under obsidianPath. Storage substrate: JSON file. Representational form: symbolic paths, saved query, URL, subpath and group structure; optional readable title. Lineage: addBookmark appends caller entry to loaded items; generic existing authorship unresolved. Consumers: later bookmarks reads and flattenBookmarks, or append on a subsequent mutation. Force: exposes access records, not automatic execution of their queries or fetching their references. Read/parse failure becomes empty items, so subsequent append can replace unreadable prior data. SRC-1, `src/core/bookmarks.ts`, `src/sdk.ts`. No supplied counterpart; distinct from [RT-OBJ-vault-info](runtime.md#rt-obj-vault-info), which locates but does not contain this store.

> const items = readBookmarks(obsidianPath);
>   items.push(entry);
>   writeBookmarks(obsidianPath, items);
> --- `src/core/bookmarks.ts`

#### MEM-OBJ-session-summary
Label: LoCoMo supplied summaries and observations

Source-native identity: `sample.session_summary` and `sample.observation` copied into session Markdown. Storage substrate: same temporary files as raw Dialogue sections; representational form: natural-language derived content, separately from symbolic session/date/adjacency metadata. Lineage: dataset-provided summary/observation strings; upstream authorship, model and derivation are uninspected because dataset contents/producer are unavailable. Driver copies them, not a Napkin summarizer. Later pi question invocations can retrieve these sections together with raw dialogue. Authority: candidate answer evidence; no consistency check against dialogue or separate trust tier is applied by this writer. SRC-1, `bench/locomo-eval.ts`. No supplied record contains this LoCoMo part; unlike [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), which is LongMemEval raw-round ingestion.

> const summary = sample.session_summary?.[`session_${num}_summary`] ?? "";
>     const observations = sample.observation?.[`session_${num}_observation`] ?? [];
> --- `bench/locomo-eval.ts`

#### MEM-OBJ-evaluation-results
Label: Benchmark answers and evaluation results

Source-native identity: QResult arrays and `bench/results/` JSONL/optional JSON reports. Storage substrate: driver process memory then result files. Representational form: symbolic retrieval proxies, timing/counts and scores; natural-language question, expected answer and agent answer. Lineage: external pi events are parsed, text/args/tool-results combined for accessed-note string matching, and answers scored; full tool event history is not equivalent to the retained result fields. Consumer: same evaluator's aggregation/reporting; no inspected next-question prompt or vault update reads result records as knowledge. This is retained evaluation output, not a demonstrated trace-fed improvement mechanism. SRC-1, `bench/longmemeval-eval.ts`, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts` inspected result paths. Distinct object produced by [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) and [MEM-RTE-benchmark-variants](#mem-rte-benchmark-variants), not a duplicate route.

> const allText = [agentText, ...toolArgs, ...toolResults].join("\n");
>     const accessed = extractAccessedNotes(allText, sessionNoteNames);
> --- `bench/longmemeval-eval.ts`

### Routes

#### MEM-RTE-auxiliary-edits
Label: Caller-controlled auxiliary note edits

Trigger/owner: explicit daily, property/task, template-insert or SDK baseCreate calls. Caller proposes content/status/template/path and admits it; human versus software identity is unspecified. Core executes structural checks, parsing and physical writes, not distill KEEP/SKIP. Operating mode: open requests; answer oracle: inapplicable — no semantic candidate scoring. Rejection can arise from unresolved target/template, malformed frontmatter or non-task line; daily append/prepend instead creates an empty missing file. createBaseItem writes without createFile's existing-target check. Rollback is caller rewrite or external file history, not a supplied transaction. Guidance is caller arguments, daily/template settings and stored templates; changed Markdown persists. Closest supplied route is [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), but these separately exposed implementations have different checks and transformations. SRC-1, `src/core/daily.ts`, `src/core/templates.ts`, `src/core/properties.ts`, `src/core/tasks.ts`, `src/core/bases.ts`, `src/utils/frontmatter.ts`, `src/sdk.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/path/status/property/template result values.
- Later read-back: Changed Markdown is available to later daily/full reads, search/overview and structured projections; template insertion copies transformed content into the note.
- Delegated visibility: CLI stdout or SDK values reach caller; external model forwarding is host-owned.
- Selection predicate: Today's configured path; exact note and property/task-line identifiers; template name and target; caller baseCreate path/name. These identifiers select direct targets, not inferred query relevance.
- Invalidation or expiry: Normal path/mtime changes invalidate caches; no semantic expiry or automatic reasons archive.
- Activation or effect: Writes are implemented; later behavioral dependence is uninspected without traces.
- Evidence limits: Generic caller does not establish per-content human approval; parser/template operations do not establish claim truth or semantic curation.

> const fullPath = path.join(vaultPath, targetPath);
>   fs.mkdirSync(path.dirname(fullPath), { recursive: true });
>   fs.writeFileSync(fullPath, opts.content || "");
> --- `src/core/bases.ts`

#### MEM-RTE-structured-access
Label: Structured access and store maintenance

Three distinct branches share explicit caller control, not automatic context push. Base: caller selects base/view, implementation reloads YAML and projects current note metadata via transient database. Canvas: caller reads full JSON or selected node types, or proposes create/add/remove; core rejects existing creation, unsupported node type or missing endpoint, then rewrites JSON. Bookmarks: caller requests flattened entries or admits an appended entry; implementation reads and rewrites JSON without knowledge-content approval. Operating mode: explicit open requests. Caller owns proposal/decision/veto; human identity unknown; answer oracle is inapplicable — structural operations have no gold-answer evaluation. Recovery: base query closes its transient DB; canvas/bookmark restoration requires caller rewrite/external history. No version archive in inspected code. SRC-1, `src/core/bases.ts`, `src/core/canvas.ts`, `src/core/bookmarks.ts`, `src/sdk.ts`, `src/main.ts`, `src/utils/bases.ts` inspected ranges. Distinct from [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval) and [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation), though runtime mentions these capabilities.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Base columns/rows and derived groups/summaries; canvas data/node or mutation results; flattened bookmark entries or added entry.
- Later read-back: Later query reloads retained base definitions and note metadata; later canvas/bookmark reads reload changed JSON. No inspected ordinary search consumer of canvas/bookmark text or saved query execution.
- Delegated visibility: SDK/CLI caller receives returned structured values; forwarding or rendering elsewhere is external.
- Selection predicate: Base file plus view filters/order/limit; canvas file, node type or ID/prefix; bookmark list flattens groups. A saved bookmark query is output data, not an automatically run selector.
- Invalidation or expiry: Reload from disk on operation; canvas remove-node also removes incident edges; no TTL. Bookmarks read errors return empty items, bounding data preservation.
- Activation or effect: Store writes and query execution are wired; model behavior change or benefit is uninspected.
- Evidence limits: Partly unread filter/formula internals prevent exhaustive base semantics; JSON references alone do not establish actual note/URL consumption.

> canvas.nodes = canvas.nodes.filter((n) => n.id !== node.id);
>   canvas.edges = canvas.edges.filter(
>     (e) => e.fromNode !== node.id && e.toNode !== node.id,
>   );
> --- `src/core/canvas.ts`

#### MEM-RTE-benchmark-variants
Label: LoCoMo and HotpotQA retained-context evaluation

LoCoMo driver admits all nonempty conversation sessions with supplied summary/observations, dialogue and adjacent-session links into one temporary vault per sample; successive question-agent invocations use that vault before sample cleanup. HotpotQA driver admits supplied paragraph contexts as title-named files, synthesizes links when another title occurs in body text, and creates a context roster; one question invocation precedes cleanup. Authors are dataset suppliers for source text, driver for formatting/links, and external agent for answer. Selection/admission is deterministic ingestion, not per-note human approval. User chooses evaluation arguments, not individual retained facts. Operating mode: bounded benchmark questions; oracle: dataset answer and evidence-session/supporting-title labels, compared through accessed-text proxies and answer token F1. Source inspection does not establish actual use of the evidence. Guidance: prompts request napkin-only retrieval and short answer; skills are disabled. Failed calls return null; cleanup removes temporary content, not a semantic rollback of a long-lived library. SRC-1, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts` inspected ingestion/invocation/cleanup ranges. These are separate dataset routes from supplied LongMemEval [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), not its parts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: QResult or null; later aggregation reports evaluation metrics and can retain result files.
- Later read-back: LoCoMo sample notes remain for multiple later question subprocesses; HotpotQA retained paragraph notes are requested during its one question. Results do not enter an inspected answer-context update.
- Delegated visibility: Pi receives model flag, external extension path, cwd, inherited environment and prompt; bash tool text can reach answer model. Extension injection is uninspected.
- Selection predicate: Agent is instructed to search/read relevant notes; base search settings are limit 10/snippetLines 3. Driver gold labels select scoring references, not admission/retrieval policy.
- Invalidation or expiry: Temporary vault removed per LoCoMo sample or HotpotQA question; no checkpoint continuation across samples/questions established.
- Activation or effect: Ingestion, subprocess request and scoring are wired; exercised retrieval, answer dependence and improvement are uninspected.
- Evidence limits: Dataset summaries' derivation and actual results unavailable; string-matched accesses are not complete-read evidence. Skills disabled means no inference of distill/tend compliance.

> if (summary) content += `## Summary\n${summary}\n\n`;
>     content += `## Dialogue\n${bodyLines.join("\n")}\n`;
> --- `bench/locomo-eval.ts`

> fs.writeFileSync(path.join(napkinDir, `${sanitize(title)}.md`), content);
> --- `bench/hotpotqa-eval.ts`

#### MEM-RTE-background-distill
Label: Claimed external background distillation

Trigger: external pi timer notices new conversation entries; manual /distill is claimed to process everything. Producer/decider: separate model call, not the working agent according to design. Model proposes parseable path/content notes; NO_DISTILL can reject retention. Operating mode: open background session retention; answer oracle: none specified. Authoring is model-directed, physical write is extension-directed; no per-note human approval is described. Guidance: new user/assistant messages plus vault context/templates. Proposed output is structured notes; reasons appear in example Decision/Context/Consequences but universal rationale preservation is not established. Rollback, path admission validation and incremental checkpoint format are uninspected because extension source is outside boundary. SRC-1, `docs/distill.md`; compare packaged-agent [RT-RTE-distill-session](runtime.md#rt-rte-distill-session), which has a different declared producer/control procedure. Possible integration overlap if an external host implements one through the other; no supplied implementation resolves it.

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Claimed parsed notes or NO_DISTILL skip.
- Later read-back: Claimed vault writes afford ordinary later overview/search/read; actual incremental cursor persistence and consumer delivery unresolved.
- Delegated visibility: Design says separate model receives new messages, NAPKIN.md and templates; automatic delivery of output to working agent not established.
- Selection predicate: New entries since prior run, configurable template set and model capture judgment; no context/token budget specified.
- Invalidation or expiry: uninspected — extension implementation is unavailable, including cursor reset and overwrite/withdrawal behavior.
- Activation or effect: Claimed direct note writing; no observed activation or benefit supplied.
- Evidence limits: Design/config description is not a shipped scheduler or verified automatic trace-fed update; cannot equate it with core CRUD enforcement or packaged skill execution.

> The agent doesn't do the distillation. A separate, cheap model call does. The agent keeps working; distill runs alongside it.
> --- `docs/distill.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval)

Memory selection is request-driven. Overview selects a derived folder map and includes the whole nonempty trimmed NAPKIN.md, with no query-specific context-note selection. `_about.md` description frontmatter is returned trimmed but untruncated; prose fallback is approximately 140 characters. Overview excludes templates, root NAPKIN.md and `_about.md` from keyword candidate grouping, not from search's Markdown corpus. Thus search can retrieve those files while overview exposes them differently. Collapsed keyword rows cap at 16; positive maxKeywords truncates further; contains roster caps at 12. No shared token budget or automatic external push follows. Full read returns untruncated content. These operations deliver data to a caller; external forwarding and model interpretation determine behavioral force. SRC-1, `src/core/overview.ts` inspected exclusion/about/selection/cache ranges, `src/core/search.ts`, `src/core/crud.ts`, `src/commands/overview.ts`, `src/utils/config.ts`. Supplied route quotes support score/fingerprint conclusions.

> if (data.collapsed) entries = entries.slice(0, COLLAPSED_INDEX_CAP);
>   if (ctx.maxKeywords > 0) entries = entries.slice(0, ctx.maxKeywords);
> --- `src/core/overview.ts`

#### On [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation)

Writes have no generic origin/truth distinction: supplied text, raw traces and inferred notes all persist through the same core. Default delete changes storage location to .trash, which walkers skip; permanent delete unlinks. Exact `.md` paths resolve by existence, so .trash is withdrawn from ordinary search/listing, not made unreadable or revoked from all consumers. Restoring is a manual move/write; basename-only trash retains no original directory metadata in the inspected result. Direct overwrite and move do not archive rationale or old versions. SRC-1, `src/core/crud.ts`, `src/utils/files.ts`, `src/utils/vault-internals.ts`; supplied mutation quotes support trash/overwrite branches, while [MEM-OBJ-markdown-notes](#mem-obj-markdown-notes) retains the exact-path exception.

#### On [RT-RTE-distill-session](runtime.md#rt-rte-distill-session)

Trace-fed transformation is a requested chain: current-session user/agent findings → external model KEEP/SKIP and topic clustering → merge or declarative note → future search/read. Raw conversation is not the requested retained output. Reasons are explicitly selected; inferred generalizations get a visible mark rather than stronger provenance. Later readers can receive Why/Context and reasons with full notes, but partial snippets need not retain the reasons beside each selected claim. Trust boundary applies to the update consumer: quoted/conversation instructions are data, while the skill directs behavior. The core does not enforce this interpretation. Automatic invocation makes SKIP stricter; explicit request is a starting preference, not per-content human approval. Skill requests ~200-word NAPKIN.md only for fundamental project changes; no I/O size check enforces it. SRC-1, `skills/distill/SKILL.md`, `src/core/search.ts`; the supplied route retains trust and inferred-marker passages.

> Keep: decisions and their why, root causes, confirmed behaviors, procedures,
>   mental models that took effort to reach.
> --- `skills/distill/SKILL.md`

#### On [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault)

Curation is requested semantic integration, link/tag normalization, reconnection, retirement and conservative placement, not a core semantic validator. Duplicate loser goes to trash after merging; backlink inspection before delete supports planned repair but does not make move/delete automatically rewrite links. Schema candidate is reported for user decision rather than admitted as a template. Leftovers report is immediate output; no prescribed durable task queue or criticism log. Later retrieval can consume edited notes and corrected NAPKIN.md, but no execution evidence establishes actual improvement. SRC-1, `skills/tend/SKILL.md`, `src/core/crud.ts`, `src/core/links.ts`; source quote for user/schema authority is retained in supplied route.

#### On [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

LongMemEval retains raw user/assistant rounds, not the distill skill's declarative synthesis. The driver labels speaker roles, groups by day and sets mtimes from session time plus round offset, giving trace dates an access-ranking effect. Source trust remains interpretation by answering model. Only the first round of each session is mapped for retrieval scoring; all raw-round files can be retrieved, so proxy session coverage is not exhaustive exposure evidence. The question consumer gets selected search snippets or requested notes through external pi; actual extension injection is unavailable. Cleanup destroys the question vault; result logs retain answer/metric records, not an inspected next-question behavioral update. SRC-1, `bench/longmemeval-eval.ts` ingestion, answer and result-log ranges; [MEM-OBJ-evaluation-results](#mem-obj-evaluation-results).

> // Map first round of each session for recall tracking
>       if (ri === 0) {
>         sessionNoteNames.set(sessionId, roundName);
>       }
> --- `bench/longmemeval-eval.ts`

#### On [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change)

Configuration is symbolic retrieval/layout machinery, not knowledge prose. Persisted settings can control subsequent selection budgets; injected config fixes that instance and overrides file settings. The process registry itself is static caller-maintained runtime state, while scaffolded templates/context become persistent future inputs. Missing-file checks preserve prior files rather than reconcile their content with a changed registry. This separates human schema decision requested by tend from unrestricted caller registry/scaffold APIs. SRC-1, `src/core/init.ts`, `src/utils/config.ts`, `src/sdk.ts`; supplied route quotes support config/registry authority.

> if (!fs.existsSync(fullPath)) {
>       fs.mkdirSync(path.dirname(fullPath), { recursive: true });
>       fs.writeFileSync(fullPath, content);
>       created.push(filePath);
> --- `src/core/init.ts`

## Write side

The inventory distinguishes admission from authorship and physical I/O. Generic callers admit Markdown and auxiliary-store edits; core checks path existence, resolvability, parseability or structural endpoints. A human caller may make that decision, but source alone does not identify one. Distill/tend instead request external-model semantic decisions, with tend reserving new schema adoption for the user. Background design claims a separate model decision and extension writer, without inspected enforcement. Benchmark drivers deterministically admit dataset content; user evaluation launch is not per-note approval. Automatic cache writers admit derived state through algorithm and freshness keys, not knowledge judgment (SRC-1, core/skill/benchmark paths cited in records above).

Known transformations do not depend on knowing original authorship. Property serialization changes frontmatter; template insertion substitutes and concatenates; task edits change a status marker; overview/search derive routing projections; skill-directed merge rewrites meaning if performed. Reasons can persist in distilled notes, but ordinary overwrite/template/benchmark paths do not guarantee them. No inspected compaction/checkpoint consumer replaces an enclosing agent's active conversation state; the identified trace transformation is session-to-vault guidance, with external cursor state unresolved, not an invented core summary checkpoint (SRC-1, `skills/distill/SKILL.md`, `docs/distill.md`, `src/core/templates.ts`, `src/core/overview.ts`).

Rejection and withdrawal have different downstream effects. Distill can choose nothing; tend can defer uncertain merges. Neither produces a prescribed persistent rejected-candidate store. CRUD rejection returns an error before its write branch, but auxiliary baseCreate has no equivalent existing-file guard. Trash withdraws from ordinary walkers while retaining explicit-read capacity; unlink permanently removes that file. Cache mismatch rebuilds derived state on later use, but mtime-preserving edits do not establish invalidation. Evaluation failure retains an error/result-log record where driver handles it; temporary note cleanup proceeds regardless of score rather than adopting or rejecting knowledge by correctness (SRC-1, `src/core/crud.ts`, `src/core/bases.ts`, `src/utils/files.ts`, `src/utils/fingerprint.ts`, both skills, inspected benchmark cleanup/log ranges).

## Read-back

The core pull routes are wired: later calls request overview, query-ranked snippets or a named full file. Broad context delivery is bundled into requested overview; this is not proof of unsolicited host injection. Caches are automatic internal retained inputs to those requests, and metadata has real selector authority without being propositional knowledge. Direct reads and structured routes are alternative access paths, so staged disclosure is optional (SRC-1, `src/core/overview.ts`, `src/core/search.ts`, `src/core/crud.ts`, `src/sdk.ts`; retrieval annotation and [MEM-RTE-structured-access](#mem-rte-structured-access)).

Template read/copy/insert is read-back at an update consumer: retained format/guidance shapes newly written note bytes. Later full-note readers can then receive that content. Distill/tend policy compliance and meaningful note dependence remain unobserved. Benchmarks implement a later subprocess consumer of earlier driver-written files: LoCoMo can reuse one sample's vault across questions; LongMemEval and HotpotQA use per-question vaults. Driver aggregation reads evaluation results, not a model improvement loop. Source establishes these consumer paths and their requested budgets, not exercised relevance or benefit (SRC-1, template/daily modules and benchmark ranges cited in corresponding records).

## Integration issues

- **New forcing correction: overview exposure caller/signature mismatch.** `bench/overview-exposure.ts` calls loadSearchCorpus with contentPath and configPath strings, while `src/core/search.ts` expects VaultInfo and optional folder and destructures contentPath/configPath from its first argument. This prevents treating the scorer as a verified executable check at this pin. It does not disprove runtime keyword-selection wiring or [RT-CLM-keyword-probes](runtime.md#rt-clm-keyword-probes), which uses a VaultInfo inside overview. The boundary's inclusion of the scorer remains valid; any stronger evaluation claim must retain this defect. SRC-1, both paths; implementation evidence only.

> const corpus = loadSearchCorpus(n.vault.contentPath, n.vault.configPath);
> --- `bench/overview-exposure.ts`

> export function loadSearchCorpus(
>   vault: VaultInfo,
>   folder?: string,
> ): SearchCorpus {
>   const { contentPath, configPath } = vault;
> --- `src/core/search.ts`

- **Withdrawal qualification, not contradiction:** supplied [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation) correctly says ordinary deletion hides notes from listings. [MEM-OBJ-markdown-notes](#mem-obj-markdown-notes) adds exact-path read-back of trash; reconciliation must not strengthen withdrawal into inaccessible deletion (SRC-1, `src/utils/files.ts`, `src/core/crud.ts`).
- **Alternative admission qualification:** [MEM-RTE-auxiliary-edits](#mem-rte-auxiliary-edits) extends the supplied generic caller-write account with baseCreate's unguarded write and daily/template transformations. The createFile guarantee in runtime is branch-scoped and remains correct. Do not transfer it to all writers (SRC-1, `src/core/bases.ts`, `src/core/daily.ts`, `src/core/templates.ts`).
- **Potential duplicate/overlap:** [MEM-RTE-background-distill](#mem-rte-background-distill) and [RT-RTE-distill-session](runtime.md#rt-rte-distill-session) both concern conversation retention, but separate model/extension doctrine is not identical to packaged-agent guidance. Unknown external wiring prevents merger or a composite enforced-admission claim. All other new object/route declarations state their nearest runtime comparison; none is proposed as a replacement for a supplied referent.
- **Included opaque material:** [MEM-OBJ-session-summary](#mem-obj-session-summary) has known subsequent copying and consumers despite unknown original derivation. [MEM-OBJ-search-cache](#mem-obj-search-cache) has an opaque serialized dependency payload alongside known metadata and loader. [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model) has inaccessible provider state. These uncertainties prevent lineage/model-update conclusions, not supported filesystem read-back.
- **Unresolved consumer delivery:** external extension context injection, automatic timer/cursor persistence and actual tool registration remain unavailable. Skill "always-loaded" wording must not turn [MEM-OBJ-napkin](#mem-obj-napkin) into a verified push route. Partial graph renderer and formula/tokenizer reads prevent exhaustive UI/query/selector semantics; coverage table retains the limits. No observed agent compliance, learning benefit or causal improvement is supplied.

## Limitations and checks

Frozen-source identity and clean tracked status were checked before inspection; source references stay at the registered revision. Consequential generalizations were challenged against alternate writers, direct reads, trash exact-path access, keyword fallback and supplied benchmark summaries. The report therefore distinguishes requested semantic curation from deterministic cache derivation, raw traces from supplied derived summaries, and delivery from activation.

Inspection covers callable memory surfaces rather than every line of dependency, tokenizer, renderer or evaluator internals. No prior analysis, target execution, external provider call or new source was used. Missing execution/dataset/extension evidence prevents measured relevance, comprehensive exposure, actual rationale preservation, external scheduler fidelity and exercised behavioral improvement conclusions. Form and quote validation do not establish those conclusions.

Validation: passed the invocation's role-specific commonplace-validate check; this reports form, relations and quotation occurrence, not semantic acceptance.
