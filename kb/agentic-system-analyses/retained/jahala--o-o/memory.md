---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "o-o memory: document-local research reuse, editable maintenance guidance and lossy library projections."
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
source-identity: https://github.com/jahala/o-o
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
---

# o-o memory report

## Boundary and evidence

o-o retains research and maintenance guidance in the same local HTML/bash files that later updates and browsers consume. This account covers the whole shipped workflow at SRC-1, commit b0d5063e37b4eafdbc23c1899a31f1836168b989. It includes generated initialization, ordinary and sentinel contracts, article and image retention, manifest control inputs, source/fact caches, change summaries, configuration edits, code propagation, index rebuilding and browser preferences. Claude's internal sessions, compaction, permissions, model parameters and provider storage remain external and uninspected, not absent. External research pages were not acquired. See [RT-CMP-claude](runtime.md#rt-cmp-claude).

Direct reads: SRC-1 `README.md`; `example/index.o-o.html` generation and complete shell dispatch/configuration/index/sync code; `example/anthropic-leadership.o-o.html` manifest, complete browser JS, contract, cache, changelog, opening paragraphs and references; `example/agi-declared.o-o.html` and `example/trump-incarceration.o-o.html` complete operative contracts, caches and changelogs. These supply implementation, doctrine/design and attributed retained content, respectively. Other article-instance coverage and shared-block equality are supplied boundary findings, not independent reinspection here. Image payloads were located but not decoded or visually reviewed. No target was executed.

| Entry or operation | Source path in SRC-1 | Coverage and limits |
|---|---|---|
| Quick/interactive creation, empty-state initialization | `example/index.o-o.html` | Direct; [RT-RTE-batch-create](runtime.md#rt-rte-batch-create), objects below; user parameters select a stub, not approved research. |
| Default, forced and batch updates | `example/index.o-o.html` | Direct; [RT-RTE-document-update](runtime.md#rt-rte-document-update), [RT-RTE-batch-create](runtime.md#rt-rte-batch-create); no update trace. |
| Ordinary cache admission and reuse | `example/anthropic-leadership.o-o.html` | Direct; [MEM-OBJ-source-cache](#mem-obj-source-cache), [MEM-OBJ-facts](#mem-obj-facts), update annotation; actual reuse unobserved. |
| Sentinel alternative guidance and structured caches | `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html` | Direct; [MEM-OBJ-contract](#mem-obj-contract), cache objects; event evaluation delegated, not an executable oracle. |
| Content, images, change history | `example/anthropic-leadership.o-o.html`, `example/index.o-o.html` | Direct selected article passages and full retained JSON; [MEM-OBJ-article](#mem-obj-article), [MEM-OBJ-images](#mem-obj-images), [MEM-OBJ-changelog](#mem-obj-changelog). Image semantics and full article accuracy unassessed. |
| Configuration supply, replacement and removal; `--show` | `example/index.o-o.html` | Direct; [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit), contract and manifest objects. Display is a subset, not policy enforcement. |
| Shared shell/JS/CSS copying and custom-style withdrawal | `example/index.o-o.html` | Direct; [RT-RTE-code-sync](runtime.md#rt-rte-code-sync), [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell); prior versions not retained by sync. |
| Recursive index projection, browser rendering/search | `example/index.o-o.html`, `example/anthropic-leadership.o-o.html` | Direct; [RT-RTE-library-read](runtime.md#rt-rte-library-read), [MEM-OBJ-index-content](#mem-obj-index-content); projection drops research evidence. |
| Browser theme storage/reload | `example/anthropic-leadership.o-o.html` | Direct; [MEM-OBJ-oo-theme](#mem-obj-oo-theme); UI memory only. |
| Other five ordinary article instances | `example/ai-model-landscape.o-o.html`, `example/competitor-costco.o-o.html`, `example/openclaw.o-o.html`, `example/vendor-comparison-vector-dbs.o-o.html`, `example/yc-w26-batch.o-o.html` | Supplied boundary inspection of matching instructions/shared code and state shapes; no claim of uniform cache schema or research quality. |
| External tool loop, hooks, sessions and compaction | `example/index.o-o.html` | Direct dispatch establishes only the external CLI/tool request. No local registered-tool service, hook or library API appears in the inspected shell router; external mechanisms remain unresolved. Their context eviction and checkpoint behavior cannot be classified. |

## Core ideas

1. **The file is the cross-invocation handoff.** A fixed prompt identifies one document; the contract asks the agent to read its previous research and update in place. There is no separate semantic retrieval selector in the inspected handoff. The filename targets a document, not a ranked subset of facts. See [MEM-BAP-cache-reuse](#mem-bap-cache-reuse).
2. **Research content and control metadata have different authority.** Cached facts are interpreted as prior research by the model; manifest date/interval and budget are parsed by shell rules. Both can affect later work, but a timestamp is not evidence that sources remain true. See [MEM-OBJ-facts](#mem-obj-facts), [MEM-OBJ-manifest](#mem-obj-manifest).
3. **Retention is model-curated and weakly specified.** The contract requests source preservation, not immutable snapshots or automatic validity checking. The populated ordinary cache uses coarse strings despite instructions requesting URL/title/tier/access date; sentinel caches demonstrate that richer records are also possible. Thus neither a uniform schema nor complete provenance follows from the cache label. See [MEM-OBJ-source-cache](#mem-obj-source-cache).
4. **Downstream readers receive different projections.** Future agents are requested to read the whole file; humans receive article HTML and references; index cards receive a short excerpt without its citation tokens. Display and discoverability are not independent verification. See [MEM-OBJ-index-content](#mem-obj-index-content).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-cache
Label: Source cache source records

Source-native identity: `oo-source-cache.sources` and cache-level `last_updated` in each article. Storage: JSON text in the local polyglot file. Form: symbolic container, dates and locator fields; natural-language titles and source descriptions interpreted by the research agent. These are retained source pointers/descriptions, not downloaded page snapshots. Distinct from the update route [RT-RTE-document-update](runtime.md#rt-rte-document-update); no supplied operative-object counterpart after comparison.

Lineage: generation emits empty `sources` and null `last_updated`; the maintenance contract requests agent updates from web research, preserving sources still valid. Actual sample authorship and tool traces are unverified. The ordinary article retains domain-level strings, including vague multi-page descriptions, without per-source access dates or tiers. Sentinel articles instead retain objects with `id`, `url`, `title`, `tier`, `accessed`. These are alternative representations within the same source-native field, not evidence that every document has either shape. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`.

>     "anthropic.com/news (multiple)",
>     "cnbc.com - funding, board, leadership coverage",
> --- `example/anthropic-leadership.o-o.html`

>     {"id": "s2", "url": "https://www.nature.com/articles/d41586-026-00285-6", "title": "Does AI already have human-level intelligence? The evidence is clear", "tier": "academic_journal", "accessed": "2026-02-17"},
> --- `example/agi-declared.o-o.html`

Later consumer: the next research agent, by requested file read. Tier/access labels are attributed research metadata, not executable trust enforcement or authentication. No automatic expiry removes entries. A normal browser/index read does not select this cache for display. See [MEM-BAP-cache-reuse](#mem-bap-cache-reuse).

#### MEM-OBJ-facts
Label: Cached research facts

Source-native identity: `oo-source-cache.facts`; natural-language strings in local JSON. Distinct from source pointers and article presentation: these are condensed prior conclusions for the next research agent. Closest supplied record is [RT-RTE-document-update](runtime.md#rt-rte-document-update), a route rather than this retained part. SRC-1: `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`.

>     "Rahul Patil (ex-Stripe CTO) joined as CTO in Oct 2025",
>     "Sam McCandlish transitioned from CTO to Chief Architect (Oct 2025)",
> --- `example/anthropic-leadership.o-o.html`

Generation initializes an empty list; populated examples retain assertions and event-status conclusions. They do not provide field-level links from each fact to its supporting source, raw tool output or derivation. Their likely research derivation is declared by the contract; execution provenance remains uninspected. The contract explicitly requests reading facts, but its write instruction specifies source metadata rather than a fact-update algorithm. Maintenance granularity is therefore left to the agent. Prior factual assertions can shape later research through interpretation; this does not establish reliable correction or improved capacity.

#### MEM-OBJ-manifest
Label: Document manifest

Source-native identity: operative `oo-manifest`, separate from the literal template inside the shared shell. Storage: local JSON text. Form: symbolic date, interval, version and title fields consumed by shell/browser rules; the ordinary example also carries natural-language `changelog` summaries. Distinct retained control object used by [RT-RTE-document-update](runtime.md#rt-rte-document-update), [RT-RTE-batch-create](runtime.md#rt-rte-batch-create) and [RT-RTE-library-read](runtime.md#rt-rte-library-read), not a duplicate route. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

>   "title": "Anthropic Leadership Team",
>   "update_every_days": 7,
>   "version": 3,
>   "as_of": "2026-02-17",
> --- `example/anthropic-leadership.o-o.html`

Generation emits version zero, empty date and seven-day interval; later agents are requested to increment version and date. Operators can set the interval directly. Shell first-match parsing affects whether research is dispatched; browser/index parsers display metadata; the agent uses `as_of` to focus on changes. Persisted version/date are access and progress metadata, not source warrant. The manifest's prose summaries are an additional readable change representation, not an automatic rollback checkpoint; browser metadata code does not display that array.

#### MEM-OBJ-contract
Label: Document update contract

Source-native identity: operative `oo-contract`, excluding the copied generation-template literal. Local JSON text contains natural-language role, procedure, scope, search intents and source preferences plus symbolic budget/image/output settings. Different consumption paths matter: the shell extracts budget as a number; the model interprets research instructions; CLI/browser displays expose selected identity/research/budget fields. It is distinct from the fixed initial prompt of [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt), though both guide the same agent. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

>       "10. Update oo-source-cache: record all sources you used (url, title, tier, accessed date). Preserve previous sources that are still valid.",
> --- `example/anthropic-leadership.o-o.html:435-435`

Initialization copies the shipped procedure and inserts user subject/scope; interactive creation also accepts audience/tone/budget. The sample contracts' precise creation history is not verified. Later operator edits persist instructions for future updates through [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit). Ordinary maintenance asks to preserve rather than revise the procedure. Sentinel contracts add model-evaluated event criteria and concise non-event reporting while retaining ordinary enrichment guidance; this limits any claim that all documents pursue unrestricted growth. Source preference/denial and HTTPS guidance are instructions, not an inspected fetch-filter implementation. Reasons for general procedure choices are not required retained operational evidence.

#### MEM-OBJ-article
Label: Article prose and reference structure

Source-native identity: `<article id="article">`, its HTML headings, paragraphs, stable `pid` comments and references. Storage: same local file. Form: natural-language claims for human/model interpretation, with symbolic HTML, paragraph identifiers and numbered-reference structure for browser processing. This excludes image payloads below. Distinct object consumed along [RT-RTE-document-update](runtime.md#rt-rte-document-update) and [RT-RTE-library-read](runtime.md#rt-rte-library-read). SRC-1: `example/anthropic-leadership.o-o.html`, `example/index.o-o.html`.

> <li>[s1] <a href="https://www.anthropic.com/company">Anthropic &mdash; Company</a>, anthropic.com</li>
> --- `example/anthropic-leadership.o-o.html`

User-supplied title/scope initialize a stub; the agent is requested to synthesize researched HTML, preserve paragraph IDs and edit sections. Existing article content is available on later whole-file reads, not only through the separate fact cache. Browsers construct TOC and citation links; humans interpret the prose. Links retain some claim-to-reference context but do not retain full source pages, search traces or rejection reasons. Browser code assigns reference targets from list order, not cache IDs. No automatic referential-integrity test follows research admission.

#### MEM-OBJ-images
Label: Embedded article images

Source-native identity: figure `img` data URIs and adjacent caption/source links. Storage: base64 payloads inline in local HTML, unlike transient image downloads under `/tmp`. Form: opaque encoded media decoded for browser display, not distributed model parameters or a textual research summary; captions and source links are separately readable natural-language/locator metadata. Distinct part of [MEM-OBJ-article](#mem-obj-article) in presentation, with different inspection and transformation limits; closest supplied record [RT-RTE-document-update](runtime.md#rt-rte-document-update) names the update pathway, not this object. SRC-1: `example/anthropic-leadership.o-o.html`, `example/index.o-o.html`.

> - Check size: if over max_file_kb, reduce further or skip
> - Encode: base64 < /tmp/oo_img_N_r.ext
> --- `example/index.o-o.html`

The prompt requests download, format-preserving resize, size rejection/reduction, embedding, attribution and temporary-file cleanup. Located payloads in the ordinary article establish retention, not successful resizing, authenticity or compliance. Browser viewing is the explicit media consumer. Future whole-file agent reads expose the encoded text but do not establish that the agent sees decoded image content. Encoded data could enlarge a file read; no o-o token-budget policy selectively omits it.

#### MEM-OBJ-changelog
Label: Research change summaries

Source-native identity: `oo-changelog`. Storage: local JSON. Form: natural-language summaries plus symbolic version/date/timestamp/count/section fields. Generation emits an empty `entries` object; sentinel examples retain that wrapper; the ordinary article instead uses a bare array with `date`. These forms are not equivalent to a raw execution log or saved prior document. Distinct from the manifest's additional prose summaries and from [RT-RTE-document-update](runtime.md#rt-rte-document-update), the admitting route. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`.

>     "summary": "Initial document creation with full coverage of leadership team, board of directors, and research leadership.",
>     "sources_added": 16,
> --- `example/anthropic-leadership.o-o.html`

The contract requests appending summaries; examples report earlier changes but do not authenticate those operations. Later whole-file agent reads are requested, so summaries are reachable; no explicit later selection or decision rule uses them as evaluation feedback. Counts are not scores or answer oracles. Summaries omit full old text, tool outcomes and systematic reasons for rejected sources. Their retention therefore establishes neither trace-fed method learning nor recoverable checkpoints.

#### MEM-OBJ-index-content
Label: Persisted library projection

Source-native identity: `INDEX-CONTENT-START` through `INDEX-CONTENT-END`, with document-count/last-scan displays. Local HTML is symbolic navigation/table structure carrying natural-language titles and excerpts. Material output of [RT-RTE-library-read](runtime.md#rt-rte-library-read), not another route. SRC-1: `example/index.o-o.html`.

>   # Build card grid (top 8 most recently updated)
> --- `example/index.o-o.html`

Shell rebuild derives table rows from recursively discovered documents and cards from the eight latest date-sort keys. It strips tags and `[sN]` tokens from the first matched paragraph and limits the excerpt to 120 characters. This curation changes representation and removes local citation context; it is not a model-authored assessment. All table rows and only selected cards persist for later browser viewing. Search/filter and column sorting manipulate the current DOM, not the source documents. Rebuild replaces the projection; deletion from the directory can remove a listing on rebuild but does not retract content in copies or browser views. Basename links may not preserve recursive directory locations, as the runtime notes.

#### MEM-OBJ-oo-theme
Label: Browser theme preference

Source-native identity: localStorage key `oo-theme`. Storage is browser-managed localStorage; form is a symbolic light/dark string interpreted by JS. Source lineage is a user's theme-toggle click; code writes it and later page initialization reloads it. It is distinct UI state associated with [RT-RTE-library-read](runtime.md#rt-rte-library-read), not article research memory. SRC-1: `example/anthropic-leadership.o-o.html`.

>   var saved=localStorage.getItem('oo-theme');
>   if(saved)r.setAttribute('data-theme',saved);
> --- `example/anthropic-leadership.o-o.html`

No automatic expiry is specified by this JS. Effective browser-origin scope, persistence settings and actual reload are unobserved; this state does not reach the research agent through the inspected dispatch.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-cache-reuse
Label: Prior research authority channel

Consumer: later external research agent. Channel: requested direct file read of `oo-source-cache` under the operative document contract. Force: prior research to build on, with validity left to model judgment, not a binding trusted-fact store. Horizon: repeated updates to that file until content is edited or removed; persistence across sessions is afforded by the file rather than a local agent-session implementation. Distinct from the initial task-prompt channel [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt). SRC-1: `example/anthropic-leadership.o-o.html`.

>       "3. Read the oo-source-cache JSON block to see what sources and facts were gathered previously. Build on prior research, do not start from scratch.",
> --- `example/anthropic-leadership.o-o.html:428-428`

The source establishes the reuse request, not observed cache delivery, decision dependence or benefit. Cached prose is not promoted to an independently verified authority by its JSON location. Retrieved external material and previous agent assertions can enter this channel; no source-trust enforcement or injection resistance is established by the inspected instruction.

## Annotations

#### On [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Memory read-back trigger is a later eligible/forced invocation. The user-selected file path and fixed prompt initiate requested reads; the model selects research within the whole document using scope, intents, date and previous cache. No deterministic fact ranking, token quota, cache-size bound, automatic compaction or selective eviction is supplied in SRC-1 `example/index.o-o.html`. Monetary budget limits the requested spend, not a stated model-visible context budget. Whether the external host trims, summarizes, reloads or checkpoints file reads is uninspected.

Retained inputs include article, manifest, contract, source/fact cache and summaries. Outputs remain in that same file; subsequent agent reads and browser/index consumption are distinct later consumers. Whole-file delivery is instructed rather than automatic prompt concatenation. The initial prompt is small; eventual tool reads may be large and include machinery, duplicate template literals and encoded media. The record's preservation quote and [MEM-BAP-cache-reuse](#mem-bap-cache-reuse) supply the requested raw-file-to-agent chain. Research summaries derive from requested web research, not inspected execution traces. No observed behavior change closes the activation link.

#### On [RT-RTE-batch-create](runtime.md#rt-rte-batch-create)

Initialization retains the selected user parameters, empty source/fact lists, empty changelog, version zero, empty date and copied procedure/machinery. Quick creation and interactive creation differ in configurable inputs, not cache admission policy. Each child Claude process is supplied its own document path; the batch does not concatenate articles or return a research summary to a parent model. This is process-per-document context separation at o-o's boundary, not evidence about host subagent frames or session isolation. Only child command success/count reaches the shell before index rebuilding; file changes persist outside the child. SRC-1: `example/index.o-o.html`.

#### On [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit)

The operator decides the supplied scalar/array change; software writes it directly. This is human content selection, unlike merely starting an agent update. Values persist for future dispatch/file reads; CLI/browser display is not approval. The `--remove` implementation filters matching lines across the file, so its withdrawal effect can extend beyond the named array and does not ensure removal of a value embedded in an inline array. A success message does not validate the resulting JSON. No prior content is retained for rollback by this mechanism. SRC-1: `example/index.o-o.html`.

#### On [RT-RTE-code-sync](runtime.md#rt-rte-code-sync)

Retained code is copied rather than learned from update traces. Selected shell/JS/CSS sections replace siblings' sections; future Bash/browser invocations consume the replacements. During CSS sync, prior custom blocks are removed, then local `oo.css`, if present, is injected; thus absence of that file withdraws previous custom styling on this route. The file is a supported external local input, not a frozen inspected custom-style payload. There is no retained old-block checkpoint in this copying operation. Selection and admission are explicit operator choices, not per-sibling human review. SRC-1: `example/index.o-o.html`.

#### On [RT-RTE-library-read](runtime.md#rt-rte-library-read)

The retained index is a derived selection, not the cache itself. Selector inputs are filenames, first metadata matches, file size, first paragraph excerpt and dates. Card budget is eight entries; table membership includes all discovered non-SELF files. Browser delivery includes links, title/date/version and excerpt, not cached facts, source tiers or change history. Browser contract display is also selective. The research source lists and change summaries are not rendered by the inspected JS. Separately, theme clicks write `oo-theme` and subsequent initialization reads it. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

## Write side

Acquisition begins with human topic/configuration supply and code-generated empty state. Research updates then ask an external agent to search/fetch, select claims, edit article/cache/manifest and append summaries. Starting the update is not per-claim approval. Authorship is requested model synthesis; physical I/O is delegated to tools; admission is direct mutation, not a candidate-and-accept transaction. The supplied runtime route establishes these distinctions and lack of post-edit acceptance/rollback within this driver. See [RT-RTE-document-update](runtime.md#rt-rte-document-update).

Curation includes model-requested incremental synthesis, preservation of still-valid sources, stable paragraph IDs, and image selection/resize/rejection; code-derived index excerpts are a different transformation. Source denial/preference and sentinel evaluation guide model judgment, not a deterministic evaluator. No supplied expected answers adjudicate facts. The ordinary article's coarse source strings disprove a stronger uniform-metadata claim; the sentinel objects disprove a weaker claim that caches can only store domain names. See [MEM-OBJ-source-cache](#mem-obj-source-cache).

Rejection and withdrawal are local: the agent is requested to skip or reduce oversized images and need preserve only valid sources, but source rejection reasons and fact retraction/tombstone semantics are unspecified. Temporary image deletion removes staging files, not embedded media. Direct operator configuration removal and code replacement have separate admission owners and recovery limits. An in-place research failure can leave a partly changed file; neither appended summaries nor version counters reconstruct the old document. See [MEM-OBJ-images](#mem-obj-images), [MEM-OBJ-changelog](#mem-obj-changelog), and the configuration/sync annotations.

No raw-tool-trace-to-derived-behavior-rule chain is established by the inspected update contract. It requests research facts and product change summaries, not durable criticism of the agent's own execution method. The sample summaries report changes without execution provenance; they are not hidden raw traces or alternative session checkpoints. Host compaction and checkpoint forms remain uninspected. Research references retain some grounds for article assertions, but caches lack per-fact derivation and changelogs lack systematic rejection reasons. The later whole-file reader can access the retained summaries; no specific reason-reading policy is supplied. These limits prevent inferring trace learning, successful learning or evidence-responsive method improvement from persistence alone.

## Read-back

The principal research route is request-driven: an invocation selects one file, supplies its path, and asks the external model to read the file and cache. The cache is not independently pushed by a background retrieval mechanism. Selection within a read, tool truncation, and compliance with incremental reuse are model/host-dependent and unobserved. Freshness decides whether to invoke; it does not expire the retained facts. Scope/intents and `as_of` target the next research task rather than proving a query-ranked cache lookup. See [MEM-BAP-cache-reuse](#mem-bap-cache-reuse) and the update annotation.

Two deterministic later consumers differ from the model: shell freshness/budget extraction consumes metadata to gate or configure a process, and index/browser consumers produce navigation/presentation. Index rebuilding persists a lossy document projection; later browsers receive that projection without the underlying evidence. Theme preference is read back only for presentation. Static shipped contracts and machinery are not themselves accumulated research memory, but operator-edited versions persist into later behavior. See [MEM-OBJ-manifest](#mem-obj-manifest), [MEM-OBJ-index-content](#mem-obj-index-content), [MEM-OBJ-oo-theme](#mem-obj-oo-theme), and the configuration/sync annotations.

## Integration issues

- No supported correction to supplied runtime facts is required. Its fixed prompt and source-cache reuse account are consistent with direct inspection. One documentation inconsistency deserves retention: the dispatch prompt places the contract below `window.stop()`, but the actual operative contract precedes it and browser JS can display selected fields. Selection should use block identity, not that positional description. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`; concerns [MEM-OBJ-contract](#mem-obj-contract), [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt).
- New operative objects distinguish retained parts rather than re-declare supplied routes. No duplicate supplied record was identified after comparison. The cache authority channel supplements, rather than replaces, [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt). Epistemic/workflow peer declarations were not supplied; reconciliation must check any overlap concerning research evidence, configuration and changelogs.
- Cache and changelog schemas vary across inspected instances; template initialization is not a schema guarantee. The literal template also repeats block IDs and empty state inside the shell text. A later whole-file model reader must distinguish the operative instance from the generation template; no inspected deterministic extraction stage enforces that distinction for the agent. Concerns [MEM-OBJ-source-cache](#mem-obj-source-cache), [MEM-OBJ-facts](#mem-obj-facts), [MEM-OBJ-changelog](#mem-obj-changelog), [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell). SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.
- Which prior facts were actually read, corrected, rejected or influential remains unresolved without an update trace. Retained lists and dates cannot answer it. Host context limits and file-read treatment are likewise unresolved; they prevent concluding complete delivery or bounded model context, not source-level persistence. Concerns [MEM-BAP-cache-reuse](#mem-bap-cache-reuse), [RT-CMP-claude](runtime.md#rt-cmp-claude).

## Limitations and checks

Source identity was rechecked with Git HEAD at the registered checkout: b0d5063e37b4eafdbc23c1899a31f1836168b989; status was clean. The job instruction, supplied member types, collection, worker rules and complete shared records contract governed this report. Direct inspection tested consequential generalizations against ordinary versus sentinel cache shapes and contract modes, plus forced/configuration/sync alternatives. No providers, target scripts, examples or tests were executed.

This is source-level wiring and requested behavior, not observed reuse or benefit. Sample research claims, provenance, source availability, image correctness, browser behavior and external permissions remain unverified. The inspected source supports file-based memory and differing consumer projections; it does not establish actual incremental-research quality, successful retraction, token-budget control, trace learning or reliable source-trust enforcement.

Validation: deterministic invocation-specific `validate-output` check passed; this establishes structural and quotation checks, not semantic acceptance or observed operation.
