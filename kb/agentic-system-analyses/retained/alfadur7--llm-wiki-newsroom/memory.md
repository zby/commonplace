---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki-newsroom memory: layered wiki files, derived navigation, bounded grounding and trace-fed guideline revision."
run-id: AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01
source-identity: https://github.com/alfadur7/llm-wiki-newsroom
reviewed-boundary: 8e209cab483da544852d7213f0e25291d06d8a88
---

# llm-wiki-newsroom memory report

## Boundary and evidence

The memory boundary includes raw acquisition, source reflections, hubs, higher-layer narratives, generated navigation and maintenance indices, browser/export/email consumers, role-context selection, defect/feedback retention and subsequent instruction revision. This is file-based knowledge maintenance operated by an external agent host, not an implemented model runtime. The source is SRC-1 in [boundary](boundary.md#source-register), at the revision above. `git rev-parse HEAD` matched that revision. Source inspection and supplied runtime findings are distinguished below. No target program, tests, examples, model or service was executed.

The runtime routes organize this account, but do not exhaust it. Direct reads add the GROUND ladder, previous-partition reuse, browser body-bundle producer, defect-mining selectors, checkpoint behavior, demotion safeguards and email delivery transformations. Evidence layers are implementation for Python/JavaScript/configuration, doctrine/design for instructions, and retained artifact evidence for the sampled source page and defect ledger. The sample establishes retained content, not authenticated execution of its reported measurements.

### Coverage inventory

All source paths below belong to SRC-1. “Supplied” means supported by the handed runtime record rather than an independent full retrace here. Included but incompletely inspected surfaces remain explicit; their presence is not an evidenced absence.

| Entry point or operation | Source paths and inspection | Covering records or local limit |
|---|---|---|
| Natural request, ingest, inbox, news, alternate hosts | Supplied: `.claude/commands/wiki-ingest.md`, `AGENTS.md`, `GEMINI.md`; runtime's news/inbox account | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); source authoring and sample independently read in [MEM-OBJ-source](#mem-obj-source). Fetch/crawl retry details and individual raw payloads not independently audited; no end-to-end acquisition or fidelity conclusion. |
| Source, hub, overview, contradiction, synthesis, timeline, trail authoring | Direct: `.claude/layers/README.md`, `.claude/layers/source.md`; supplied publication route; direct bundle/staleness runbooks | [MEM-OBJ-hub](#mem-obj-hub), [MEM-OBJ-narratives](#mem-obj-narratives), annotations on ingest/build. Per-type full rubrics other than source not independently read; no uniform gate or quality guarantee. |
| Build dispatch and index mutation | Direct: `tools/build.py`, `tools/_build/index.py` URL synchronization and scan entry | [RT-RTE-build-lint](runtime.md#rt-rte-build-lint), [MEM-OBJ-access-indices](#mem-obj-access-indices). Full dedup collision policy not independently audited. |
| Graph generation and graph query | Direct: `tools/_build/graph.py` collection and relation promotion, `tools/_query/graph.py` loading/edge-cost/filter code and budget sites; supplied query route | [MEM-OBJ-graph](#mem-obj-graph); annotation on [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). |
| Cluster history, label matching and AUTO blocks | Direct selected functions in `tools/_build/clusters.py`, dispatch in `tools/build.py` | [MEM-OBJ-clusters](#mem-obj-clusters), [MEM-RTE-cluster-rebuild](#mem-rte-cluster-rebuild). Exact label-anchor matching and all catalog rendering branches not fully audited. |
| Contradiction extraction, theme assignment, overlays | Direct dispatch/docs and dependency reader: `tools/build.py`, `.claude/layers/source.md`, `tools/_build/dependencies.py`; supplied build route | [MEM-OBJ-conflict-data](#mem-obj-conflict-data). Extraction/classification and overlay algorithms not independently traced end to end; no claim-completeness or semantic-correctness conclusion. |
| Dependency staleness and regrounding | Direct: `tools/_build/dependencies.py`, `tools/_lint/staleness.py` baseline selection, `.claude/operations/staleness-reground-runbook.md`, `bundle-reground-runbook.md` | [MEM-OBJ-dependencies](#mem-obj-dependencies); build annotation. `_editor_date.py` internal git-diff parsing not audited; dates are signals, not semantic freshness proof. |
| Demotion/deletion | Direct: `tools/_lint/hub_demotion.py` contract, filters and run entry | [MEM-RTE-hub-withdrawal](#mem-rte-hub-withdrawal). No observed deletion or universal archive exclusion. |
| Graph browser bodies and link display | Direct: `tools/_build/pages.py`; targeted `graph/graph.html` fetch/reading-panel search results | [MEM-OBJ-pages](#mem-obj-pages), [MEM-RTE-browser-read](#mem-rte-browser-read). Browser safety/rendering details not audited; generated local body bundle unavailable. |
| Hosted export | Direct: `tools/export.py` cleaning, budget, merging, locator and pruning; supplied export route | Annotation on [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export). Hosted ingestion/context use outside source; no hosted-completeness guarantee. |
| Email briefing | Direct: `tools/send_briefing.py`, `tools/_briefing/render.py` idmap/deeplink conversion | [MEM-RTE-briefing-read](#mem-rte-briefing-read). SMTP internals and actual receipt uninspected. |
| Discovery, link/tag suggestions, gap crawl | Direct: `tools/discover.py`, `tools/_discover/surprising.py` selector; supplied news/query account; inventory of `_ingest/` and `_news/` | Graph/cluster consumers in [MEM-OBJ-graph](#mem-obj-graph). Discovery ranks bridge hubs, not truth. Suggestion and gap-query internals not fully traced; no exhaustive retrieval coverage claim. |
| Role frames, grounding, faction transcripts | Direct GROUND ladder; supplied delegation/faction records | [MEM-RTE-grounding-ladder](#mem-rte-grounding-ladder); annotations on [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation) and [RT-RTE-faction-authoring](runtime.md#rt-rte-faction-authoring). Host compaction and actual isolation remain external. |
| Hook/tool registration and pushed diagnostics | Direct `.claude/settings.json`, `dispatch.py` post handler; supplied protection/chain account | Annotation on [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback). These inject current diagnostics/static instructions, not an established durable summary store. |
| Feedback/defect mining, checkpoints, change admission | Direct `tools/mine_feedback.py` scan/checkpoint, `mine_failures.py`, `_review.py`, `log_defect.py`; selected Editor-in-Chief sections and ledger sample | [MEM-OBJ-defect-log](#mem-obj-defect-log), [MEM-OBJ-review-watermarks](#mem-obj-review-watermarks), [MEM-RTE-failure-review](#mem-rte-failure-review), [MEM-RTE-feedback-review](#mem-rte-feedback-review), supplied [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change). |
| Local notes and host auto-memory | Direct `CLAUDE.md` Local Memory and `.gitignore`; only `.gitkeep` tracked | [MEM-OBJ-local-memory](#mem-obj-local-memory). Initialization, actual contents and real reads unavailable; known later lookup obligation retained. |
| Evaluation artifacts and raw diagnostics | Direct judge-experiment README and `.gitignore`; supplied improvement acceptance rule | `docs/experiments/judge-model-2026-09/README.md` identifies labels, scores, manifests and hidden scorer. Full arrays/analysis not inspected here: no experiment efficacy conclusion or established automatic score-to-guidance route. `graph/_health-log.jsonl`, `lint-report.md` are local diagnostic artifacts; no demonstrated behavior-shaping derived memory inferred from raw logging. Fixed/fresh held-out consumers remain in [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change); individual canary contents not audited. |

External QMD storage, embeddings, model weights, provider state and host transcript/auto-memory internals remain opaque, not absent. Raw originals and local notes/watermarks are not shipped. These gaps prevent full lineage reconstruction, whole-deployment memory enumeration and causal benefit claims. Model alias/version limits remain in the runtime components, including [RT-CMP-qmd](runtime.md#rt-cmp-qmd).

## Core ideas

1. **Persistent pages carry interpreted knowledge; generated indices carry access rules.** Source pages retain claims and quotations with provenance pointers. Hubs and narratives selectively synthesize them. Graphs, clusters, backlinks and dedup maps make them findable but do not preserve every argument or certify source truth. [MEM-OBJ-source](#mem-obj-source), [MEM-OBJ-hub](#mem-obj-hub), [MEM-OBJ-narratives](#mem-obj-narratives), [MEM-OBJ-graph](#mem-obj-graph).
2. **Context selection is explicit and bounded.** The author climbs from mandatory grounding through indices and declared links to semantic search, then whole-corpus reading only if it fits. Query answers request full bodies for at most ten leading pages. Fresh role contexts isolate deliberation but share persistent file effects. There is no inspected host compaction implementation. [MEM-RTE-grounding-ladder](#mem-rte-grounding-ladder), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation).
3. **Rebuilding is not regrounding.** Software can refresh membership blocks, links and dates without revising narrative meaning. Staleness and bundle review separately request model rereading and correction. Demotion is triage plus a Desk/graph-integrity procedure, not automatic forgetting. [MEM-OBJ-dependencies](#mem-obj-dependencies), [MEM-OBJ-narratives](#mem-obj-narratives), [MEM-RTE-hub-withdrawal](#mem-rte-hub-withdrawal).
4. **Operational experience has a separate retention route.** Defects and decision rationales survive in a committed ledger; filtered human utterances and local checkpoints form another channel. Miners select candidate issues; Editor-in-Chief interpretation and operator adoption stand between those reports and revised guidance. Retention and recurrence signals do not establish improved capacity. [MEM-RTE-failure-review](#mem-rte-failure-review), [MEM-RTE-feedback-review](#mem-rte-feedback-review), [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source
Label: source reflections and raw pointers

Source-native identity: `wiki/sources/<slug>.md`. Natural-language summary, atomized attributed claims and quotations are Markdown on disk; tags, grade tokens, dates, raw paths, URLs and typed connection prefixes are symbolic parts consumed by checks/build. These parts are not equivalent: the model interprets claim content while software interprets markers. Raw inputs are external documents landed in `raw/`; they are evidence inputs, not operational interaction traces. A source reflection is a derived selection, not a raw transcript. Its raw lineage is declared through `source_file`/`source_url`; actual originals are unavailable here. The sampled `wiki/sources/deepseek-r1-release.md` has those pointers and preserves vendor attribution rather than turning its openness claim into narrator fact. SRC-1: `.claude/layers/source.md`, `wiki/sources/deepseek-r1-release.md`.

> Read the raw document end to end
> --- `.claude/layers/source.md`

> If the raw has a direct quotation from the speaker themselves, preserve it verbatim (do not replace it with a one-line summary)
> --- `.claude/layers/source.md`

Write agency is model authoring under layer guidance, followed by the supplied ingest review protocol, not human approval of each claim. Later consumers are query/authoring/review models through body reads and software through the symbolic parts. Content authority is evidence for synthesis, not executable instructions; delivery does not prove factual reliability or prompt-injection resistance. Distinct object from the process [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); no supplied object counterpart.

#### MEM-OBJ-hub
Label: entity and concept hubs

Source-native identity: `wiki/entities/` and `wiki/concepts/` pages. Markdown files retain natural-language extracted abstractions; symbolic frontmatter `sources`, `type`, `kind`, tags and dates serve separate build/check consumers. Lineage runs from source reflections and author rereading, with Reporter stubs and Columnist full authoring. They are not raw traces or model parameters. Later authoring/query readers interpret the body; graph, dependency and demotion consumers parse metadata/links. Hub narrative changes and source-list appends need not have the same date effect. SRC-1: `.claude/layers/README.md`, `tools/_build/dependencies.py`, `tools/_lint/hub_demotion.py`.

> A hub's `last_updated` is its narrative date and no
> longer bumps on a pure `sources:` append
> --- `tools/_build/dependencies.py`

Admission/revision uses [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [MEM-RTE-hub-withdrawal](#mem-rte-hub-withdrawal). This object separates semantic hubs from derived access indices; the supplied routes have no object counterpart.

#### MEM-OBJ-narratives
Label: derived narratives and generated blocks

Source-native identities: overview, contradiction, synthesis, timeline and trail Markdown pages, plus root overview/contradiction. Their prose is natural-language interpretation on disk; embedded AUTO membership/statistics blocks are generated symbolic listings rendered as text. Columnist authors the prose, code updates designated blocks. These must not be assigned one semantic-admission rule. Source-native lineage differs: overview derives from cluster hubs, contradiction themes from claim sources, synthesis from cited sources, timeline from linked events/hubs, trail from ordered path hops; roots aggregate their own axis. SRC-1: `.claude/layers/README.md`, `tools/_build/dependencies.py`, `tools/_build/clusters.py`.

> Files without AUTO markers are skipped with a warning — never overwrites
>     hand-authored content.
> --- `tools/_build/clusters.py`

Later query/readers, bundle Desk and reground Columnist consume the prose, while build only has authority over designated blocks. Saving a query synthesis requires explicit approval ([RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)); scheduled freshness is not automatic rewriting. Bundle review assembles one cluster's already-published pages in one context and routes attribution disputes back to raw comparison:

> differing attribution → **not the Desk's authority to settle** (it cannot verify new facts). Hand to the Reporter for a raw-source comparison.
> --- `.claude/operations/bundle-reground-runbook.md`

This container groups related reader-facing narratives but preserves the different lineage and checks above; it asserts no uniform rubric. Distinct from runtime's authoring/build routes; no supplied object counterpart.

#### MEM-OBJ-graph
Label: graph nodes and typed edges

Source-native identity: `graph/_graph.json`, symbolic JSON on disk derived from wiki pages. Node IDs/labels/types are access metadata, not full bodies. Source/entity/concept material supplies nodes; meta types are excluded from node/edge production and instead represented elsewhere as overlays. Per-file repeated target links are collapsed, relation priority and grade priority can promote separate fields; the result is not a lossless claim archive. SRC-1: `tools/_build/graph.py`.

> Per file we keep at most one edge per (from, to); when the same target
>         # appears in multiple sections we promote to the highest-priority
>         # relation. Grade is attached when any matching line carries a marker.
> --- `tools/_build/graph.py`

Later graph query consumes these fields using fixed filters and costs (explicit 1.0, inferred 2.0/confidence); browser displays them; clustering uses a weighted hub subgraph. Discovery consumes graph/cluster files and ranks bridge hubs by betweenness × cross-cluster ratio / log(degree+2), default top 15, rather than validating facts. SRC-1: `tools/_query/graph.py`, `tools/_discover/surprising.py`. Calling an explicit edge “ground truth” in the query docstring means explicit link evidence, not an independently verified factual relationship. Build invocation admits generated state automatically; no per-edge human gate inside the producer. Related route: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint); no supplied object counterpart.

#### MEM-OBJ-clusters
Label: clusters and prior partition

Source-native identity: `graph/_clusters.json`, with `graph/cluster_labels.json` supplying stable label definitions. Symbolic JSON persists membership, label assignments and source-assignment weights. It derives from graph topology and labels, with prior partition/label history also influencing the next build. Numerical membership indices are localized symbols, not distributed model weights. Initial label authorship/approval history is not reconstructed; the supplied human gate covers new cluster slugs, while subsequent partition transformations are software-controlled. SRC-1: `tools/_build/clusters.py`, `CLAUDE.md`.

> Distinct from `_load_prev_assignments` (label hysteresis): this captures
>     the partition *structure* — every cluster including auto-labelled ones
> --- `tools/_build/clusters.py`

Consumers are later clustering, catalogs/AUTO blocks, dependency generation, discovery, export and browser. Prior state has direct algorithmic authority at the next clustering call, unlike narrative text interpreted by a model. See [MEM-RTE-cluster-rebuild](#mem-rte-cluster-rebuild). Distinct retained object within runtime's build route, not its duplicate.

#### MEM-OBJ-access-indices
Label: dedup and reverse-link indices

Source-native identities: `wiki/sources/_source_map.json`, `wiki/_backlinks.json`, index/catalog listings. Symbolic file-based access metadata rendered partly as Markdown. Lineage is current page metadata and links plus cluster state. Dedup maps route future ingest by URL/path; backlinks and catalogs support future grounding/navigation, not proof that selected page content is true. SRC-1: `tools/_build/index.py`, `tools/_build/pages.py`; URL-first/path-fallback use is supplied by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

A consequential write-side exception: build can enrich a source page's URL, not merely produce sidecar indices:

> current_url present and differs → mismatch (advisory; do NOT overwrite,
>       since the wiki frontmatter may be the canonical URL deliberately set
>       against an AMP/redirect/utm raw variant).
> --- `tools/_build/index.py`

The code physically admits missing URL values from raw Markdown automatically on build; it preserves existing mismatches. This is metadata normalization, not model-generated claim revision or per-value human approval. Distinct from the graph and prose objects; runtime supplies processes, no equivalent object declaration.

#### MEM-OBJ-conflict-data
Label: contradiction databases and overlays

Source-native identities: `wiki/contradictions/_contradictions.json`, `_contradictions_themes.json`, `graph/_overlays.json`. Symbolic files retain extracted claim references/theme membership and browser overlay structures, not complete authoring rationales. Connections' `contradicts:` lines are the declared extraction source; build dispatch refreshes contradiction data before overlays. Theme/claim membership supplies dependency upstreams; overlays give browser membership and reverse lookup. SRC-1: `.claude/layers/source.md`, `tools/build.py`, `tools/_build/dependencies.py`.

> The `contradicts:` line is the **single SoT of the theme contradiction DB**
> --- `.claude/layers/source.md`

This is not an independent contradiction detector with demonstrated semantic completeness. Exact extraction, classification and theme-admission internals remain incompletely inspected here; the supplied build/guideline routes and source layer provide the bounded facts above. Changing claim membership can require theme narrative regrounding per `.claude/operations/staleness-reground-runbook.md`. Distinct object from [RT-RTE-build-lint](runtime.md#rt-rte-build-lint).

#### MEM-OBJ-dependencies
Label: dependency and freshness state

Source-native identity: `graph/_dependencies.json`. Symbolic JSON is regenerated from frontmatter, links, cluster membership and contradiction claim sources. It retains upstream IDs and newest dates, not reasons why narrative claims are warranted. Source content dates prefer scraped/published rather than structural edit dates; hub propagation combines narrative and newest cited content dates. The later staleness checker also obtains narrative body dates from Git. SRC-1: `tools/_build/dependencies.py`, `tools/_lint/staleness.py`.

> Rule (consumes `graph/_dependencies.json`, built by `tools/_build/dependencies.py`):
>
>     page is STALE  ⇔  upstream_max_date > page.effective_date
> --- `tools/_lint/staleness.py`

The dependency builder's docstring says root dates are null/out of scope; the actual later checker explicitly includes roots through body-edit dates. Thus null stored root dates do not imply absent root freshness checking. Source pages have no tracked raw upstream, so this mechanism cannot verify raw-source freshness. Consumer authority is advisory selection for rechecking, not automatic exclusion from query or automatic narrative repair. See build annotation and [MEM-OBJ-narratives](#mem-obj-narratives). No supplied object counterpart.

#### MEM-OBJ-pages
Label: reading-panel body bundle

Source-native identity: ignored `graph/_pages.json`. JSON stores natural-language Markdown bodies under symbolic maps: `pages`, `idmap`, `backlinks`, `overviews`, `meta_pages`. Its lineage is existing graph nodes and wiki bodies; it does not author new semantic summaries. Backlinks are filtered to graph-resolvable node IDs, titles dropped in favor of graph labels; overview/meta pages have separate body maps. SRC-1: `tools/_build/pages.py`.

> meta_pages→ {rel: raw markdown}  for the 4 overlay types
>                 (trails/timelines/syntheses/contradictions) so clicking an
>                 overlay row renders its page. Active files only (no _archive).
> --- `tools/_build/pages.py`

The body bundle is a reloadable display copy, not an embedding payload or shortened model memory. Later browser consumes its bodies; briefing renderer uses only `idmap`. Build regenerates it, including a second refresh after current backlinks. Exact generated deployment payload unavailable, but producer and consumer are inspectable. Distinct from [MEM-OBJ-graph](#mem-obj-graph) and runtime's export route.

#### MEM-OBJ-defect-log
Label: defect and transition ledger

Source-native identity: committed `tools/_defect-log.jsonl`. Symbolic JSON fields describe stages, clusters, decisions, model-generation labels and treatment categories; natural-language mechanism/rationale/note/change/delta fields preserve interpreted diagnoses and reasons. These are derived operational records, not complete raw lint outputs, reviewer transcripts or parameter updates. Editor-in-Chief is instructed to load one escaped-defect batch per authoring cycle, while CLI accepts caller-supplied records with schema validation. Physical append does not independently verify provenance or operator approval. SRC-1: `tools/log_defect.py`, `.claude/agents/editor-in-chief.md`.

> corpus accumulates longitudinal recurrence rates; unlike the review watermarks
> (`_feedback-review.json`, `_failure-review.json`) it is committed, so a fresh clone starts
> with the recurrence history rather than blind.
> --- `tools/log_defect.py`

Later `mine_failures.py` reads the corpus; Editor-in-Chief interprets its reports and can reread full rationale. The sampled first ledger transition retains a rationale, commit, sampled tasks, mixed-model note and explicit post-adoption measurement caveat; this is a retained assertion about a measurement, not independently checked causal support. SRC-1: `tools/_defect-log.jsonl`. Separate from [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change)'s process; see [MEM-RTE-failure-review](#mem-rte-failure-review).

#### MEM-OBJ-review-watermarks
Label: local review windows and recurrence histories

Source-native identities: ignored `tools/_feedback-review.json`, `tools/_failure-review.json`. Symbolic JSON stores `last_review` and histories; free-text notes accompany per-channel counts/recurrence data. They are access/checkpoint metadata plus diagnostic aggregates, not copies of all raw transcripts or adopted guidance. Known subsequent transformations are implemented by `_review.py` and both miners; actual initialization actor and stored deployment contents are unavailable. SRC-1: `tools/_review.py`, `tools/mine_feedback.py`, `tools/mine_failures.py`, `.gitignore`.

> Is `when` inside the review window — **boundary day included**. An item
>     with no date is included too (never hide it).
> --- `tools/_review.py`

A plain mining read does not advance the checkpoint. Read-side corruption falls back to an empty mapping; checkpoint history loading aborts on unreadable existing data to avoid silently replacing history. Later miners use the watermark as selector input and counts as diagnostic history. Fresh clones lack these local states, unlike the committed ledger. Distinct from the ledger and supplied guideline-change process.

#### MEM-OBJ-local-memory
Label: rejected directions and local decisions

Source-native identity: `.claude/memory/` notes, with host auto-memory explicitly separate outside the repository. Intended local Markdown is natural-language feedback/decision content on disk; only `.gitkeep` is available here. Content, original provenance, initial admission actor and actual consumer reads are unavailable. The known contract requires provenance and lookup of rejected directions before reproposing. SRC-1: `CLAUDE.md`, `.claude/agents/editor-in-chief.md`, `.gitignore`.

> **When read**: on entering related work.
> --- `CLAUDE.md`

> before proposing a new edit, check the rejected directions in `.claude/memory/` to avoid re-proposing the same direction
> --- `.claude/agents/editor-in-chief.md`

Local notes have advisory authority for the proposing model; shared conventions belong in tracked guidance, because local notes and auto-memory are unreachable from fresh clones/cloud routines. This preserves a known read-back protocol without claiming supplied note contents or host loading behavior. Distinct object related to [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change), no supplied object counterpart.

### Routes

#### MEM-RTE-grounding-ladder
Label: bounded grounding expansion

Endpoints/progression: content-authoring entry → Reporter/Columnist mandatory grounds → indices/declared edges → undeclared semantic relations → optional exhaustive read → authoring and final-rung handoff. The authoring model judges insufficiency under role guidance; the host executes Reads/searches. Retained wiki files are requested on demand, not independently pushed. SRC-1: `.claude/agents/README.md`.

> **Rise** — only on an insufficiency signal: a claim with no evidence span secured · an unresolved wikilink · consecutive empty searches.
> --- `.claude/agents/README.md`

> **Provisional caps**: 3 consecutive empty results at the same rung ends that rung · 15 total expansion operations (Read·search calls) outside R0 ends GROUND.
> --- `.claude/agents/README.md`

This is a content-authoring selection subprocedure, not a second declaration of [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) or [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation). It spans authoring routes rather than being contained in one. R4 depends on corpus fitting the host context budget; source-reported corpus sizes are not a universal capacity. Guideline editing instead reads touched files whole and searches defect patterns; it has no separate ladder.

- Immediate return: selected bodies/search results and final `grounded_at: R<n>` author handoff.
- Later read-back: retained sources, hubs, narratives, catalog/backlinks and graph results reach a later author invocation through requested reads.
- Delegated visibility: each author reads its own grounds; final rung and products escape the role frame; the defect loader preserves the authoring-time rung rather than retroactively raising it after ADAPT.
- Selection predicate: mandatory guide-named dependencies, insufficiency signals and evidence sufficiency; jump directly to an appropriate rung, not exhaustive sequential traversal.
- Invalidation or expiry: no automatic expiry; ADAPT can widen reads; at insufficient cap use R4 if available, otherwise limit authored claims and disclose the shortfall.
- Activation or effect: protocol requests model interpretation of selected grounds; reliable use and quality gain not demonstrated.
- Evidence limits: host window sizing, truncation and compaction not implemented here; installed QMD retrieval remains external.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### MEM-RTE-cluster-rebuild
Label: prior partition read-back

Part of: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Endpoints/progression: `build.py clusters` or full build → cluster builder loads prior partition/assignments → chooses reuse, warm native computation or fallback → persists replacement `_clusters.json` → later catalogs/browser/dependencies and next build. Owner is deterministic software once invoked; operator decides invocation and gated label changes, not each partition assignment. SRC-1: `tools/_build/clusters.py`, `tools/build.py`.

> Reuse before recompute. Without the native backend an unchanged graph
>     # still has a valid committed partition, so keep the degraded fallback off
>     # the path entirely
> --- `tools/_build/clusters.py`

The reused partition requires matching graph fingerprint and hub-set coverage. Native warm start supplies direct old memberships, neighbor-majority memberships for new nodes, or fresh communities. `--cold` disables structural warm start/reuse; prior stable-label matching is loaded separately. Non-native changed-graph fallback cannot warm-start. This counterexample prevents describing all regeneration as stateless derivation. No substantive answer oracle or measured-improvement selection is involved; admission is algorithm output, rejection is code validity checks or later operator review, recovery is corrected inputs/rebuild/cold recomputation, not atomic narrative rollback.

- Immediate return: new cluster artifact and diagnostics naming method/history reuse.
- Later read-back: previous `_clusters.json` membership is input to a subsequent clustering invocation; produced clusters also select later authoring/navigation context.
- Delegated visibility: inapplicable — this deterministic subroute does not spawn a role frame.
- Selection predicate: backend availability, `cold`, graph fingerprint, exact hub coverage, existing-node lookup and neighbor-majority initialization; labels have separate prior-assignment matching.
- Invalidation or expiry: rebuild replaces artifact; missing/invalid prior state falls back; cold computation overrides structural reuse but is not a universal history purge.
- Activation or effect: prior membership directly initializes or replaces computation in code; actual deployed branch and resulting quality unobserved.
- Evidence limits: inspectable algorithmic dependence is not learning benefit or semantic validation of communities; backend libraries not executed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-failure-review
Label: defect history to proposal context

Part of: [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change)

Endpoints/progression: escaped defects/measurement decisions → caller-authored batch → `log_defect.py` schema admission and append → `mine_failures.py` aggregation → Editor-in-Chief diagnosis → proposed guidance change and operator-governed adoption. The first two software steps do not automatically edit guidance. Operating mode is recurring review of open operational failures. Verifiers supply observations, not a fixed answer oracle; models propose diagnoses; operator can reject adoption. SRC-1: `tools/log_defect.py`, `tools/mine_failures.py`, `.claude/agents/editor-in-chief.md`.

> Being a prefilter, it prescribes nothing — it only
> aggregates and prioritizes; which surface to fix is judged by the Editor-in-Chief who
> reads it
> --- `tools/mine_failures.py`

Whole-corpus transitions inform latest verdict and latest preventive-treatment boundaries even when defects are window-filtered. New diagnostic results can therefore reflect old decisions. Reject/defer lowers priority; accept with detect/remediate does not count as prevention. Audit-stage discoveries do not establish post-treatment recurrence; the code's sweep exclusion explicitly covers only `audit`, leaving other retrospective sweeps a stated limitation. This is automatic trace-derived selection, but durable behavior-shaping instruction revision still requires the enclosing interpreted admission route. Full reasons survive in the ledger; screen output truncates the surface to 76 characters and a literal “Re-open when” sentence to 88, not the whole rationale.

- Immediate return: ranked clusters, stage/support counts, treatment/verdict markers and examples; default three target examples, `--pages` requests all.
- Later read-back: future review invocation reloads ledger and watermark; later accepted instruction text is required grounding under the enclosing guideline-change protocol.
- Delegated visibility: Editor-in-Chief receives report context; blind review/measurement frames follow the enclosing route, not the miner.
- Selection predicate: date window for defects, addressable split, latest reject/defer tier, recurrence dated after latest prevent/both treatment, then support; all-history decisions inform windowed ranking.
- Invalidation or expiry: append-only history retains decisions; latest verdict wins, equal-date later append wins; explicit checkpoint advances local review boundary, not deletion; failed edits revert/isolate by enclosing protocol.
- Activation or effect: code shapes proposal context; accepted guidance can shape later agents if read/followed; no exercised benefit inferred from counts.
- Evidence limits: schema acceptance verifies neither defect truth nor human approval; support measures review effort, not a defect-rate denominator; truncated summaries require full-ledger lookup for reasons.
- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### MEM-RTE-feedback-review
Label: human utterance mining

Part of: [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change)

Endpoints/progression: host transcript JSONL → user-text filtering/window/pattern scan → correction/operation/success batches and bounded samples → Editor-in-Chief review → optional provenance-bearing note or guideline proposal → explicit checkpoint history. Software selects matches; the model decides whether to encode them; operator governs adopted changes. Human authorship of a reaction is not human approval of its machine encoding. SRC-1: `tools/mine_feedback.py`, `tools/_review.py`, `.claude/agents/editor-in-chief.md`.

> if is_kickoff:
>                         continue  # a task-kickoff instruction (not a reaction), excluded from feedback
> --- `tools/mine_feedback.py`

The scan also excludes system/teammate notifications and long/structured messages, retains at most the requested samples per pattern (CLI default five), and clips sample text to 200 characters. Raw-to-derived lineage is human reaction text → regex hit/count/sample → interpreted encoding/proposal → optionally revised tracked guidance read next cycle. The sample/report is not itself that final behavior-shaping result. Initialization and actual private transcripts are unavailable; the installed selector is inspectable. Recurrence history compares correction-pattern-set intersections, not independently verified resolution of each underlying problem. Open feedback review is not an expected-answer experiment.

- Immediate return: three categorized minibatches, counts and clipped utterance samples; no automatic guidance edit.
- Later read-back: subsequent mining reloads transcripts and local history; encoded local notes are requested on related work; adopted guidance has the enclosing next-cycle grounding consumer.
- Delegated visibility: selected snippets enter review context, not every original transcript turn; preserved provenance allows reinspection where transcripts exist.
- Selection predicate: extracted user text, inclusive date window, exclude session kickoff and injected notifications, match channel patterns; `--all`/`--since` can override stored boundary.
- Invalidation or expiry: mining alone leaves boundary unchanged; explicit checkpoint records counts/history and date; unreadable existing checkpoint history aborts rather than overwriting it.
- Activation or effect: filtered human feedback can guide a model's proposal; later adoption and effective behavior are not observed here.
- Evidence limits: regex and clipped samples can omit relevant nuance; private transcript/notes/history contents unavailable; lower pattern recurrence is not causal improvement evidence.
- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### MEM-RTE-hub-withdrawal
Label: hub demotion and deletion triage

Endpoints/progression: `lint.py hub demotion` → graph/prose/source-count scan → candidate report → Desk secondary judgment → retain, absorb, demote or delete with link repair. Software nominates, Desk judges narrative centrality/importance; ordinary operator publication gates remain as supplied in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). No substantive answer oracle. This is a maintenance route distinct from the generic build/lint dispatcher and ordinary ingest; its proposed content withdrawal needs interpreted admission, not file I/O alone. SRC-1: `tools/_lint/hub_demotion.py`.

> Demotion/deletion is finalized by the Desk's secondary gate (narrative centrality /
> figure importance) + graph-integrity handling (redirect inbound [[wikilink]] or
> substitute plain text before deletion), so `--fix` is not supported.
> --- `tools/_lint/hub_demotion.py`

Thresholds are source count ≤2, inbound ≤3, distinct inbound clusters ≤1 and zero navigational inbound. A direct prose scan supplements graph inbound because meta bodies are not graph nodes. `gate: full|delegated|absorbed` excludes completed cases from triage. These selection rules nominate candidates, not automatic proof of redundancy. Rejection keeps the hub; repair/rebuild follows authoring procedures; no transactional rollback or observed deletion is established.

- Immediate return: graded demotion/deletion candidates and gate-resolved exclusions; no content deletion in the inspected entry.
- Later read-back: approved edits change later body/link selection; retained absorbed/delegated anchors remain reachable rather than being silently removed.
- Delegated visibility: Desk receives candidates and source context by procedure; no isolated frame implementation inside this checker.
- Selection predicate: low sources/inbound/clusters, absence of navigational embedding, plus exclusions for finalized gates; archived inbound excluded from counts.
- Invalidation or expiry: rescan current state; rewrite inbound links/plain text before deletion; no universal downstream/export invalidation guarantee.
- Activation or effect: implementation supplies triage, protocol requests content withdrawal/repair; actual maintenance and subsequent consumers unobserved.
- Evidence limits: graph-builder collection does not establish a universal archive directory filter; this route's archive exclusion is local to its counts, not a system-wide forgetting rule.
- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### MEM-RTE-browser-read
Label: browser body reload

Endpoints/progression: retained wiki/graph → `pages.run` body/maps → browser graph/cluster/overlay fetch → lazy body-bundle fetch on reading → selected Markdown display and link navigation. Owner is build code for copying and reader/browser for selection. Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)'s agent answer and [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export)'s hosted bundle. SRC-1: `tools/_build/pages.py`, `tools/build.py`, `graph/graph.html`.

> pages[nid] = fp.read_text(encoding="utf-8", errors="replace")
> --- `tools/_build/pages.py`

- Immediate return: rendered selected body, backlinks/labels and navigable node/overlay context.
- Later read-back: reader opens persisted material after generation; body bundle supplies prose, not merely graph labels.
- Delegated visibility: inapplicable — human-facing browser route does not delegate a model task.
- Selection predicate: selected node/overlay/overview and idmap resolution; graph fetch determines available nodes, meta bodies use separate maps.
- Invalidation or expiry: rebuild refreshes bundle; missing wiki files skipped; deployment refresh/browser cached copies not proven globally synchronized.
- Activation or effect: source wires loading/display; readers' reliance or later actions unobserved.
- Evidence limits: exact ignored `_pages.json` unavailable; renderer safety, browser execution and deployed data/version coherence not tested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-briefing-read
Label: retained briefing distribution

Endpoints/progression: persisted `wiki/syntheses/weekly-briefing-*.md` → explicit file or numerically latest year/week → Markdown-to-email render → SMTP or dry-run HTML → external recipient. This is a distribution consumer, not new knowledge admission or an answer oracle. Software selects latest when requested; caller selects file/recipients/mode; underlying prose admission belongs to synthesis authoring. SRC-1: `tools/send_briefing.py`, `tools/_briefing/render.py`.

> `[[slug|alias]]` → `[alias](base#q=key)` if it is a node, else plain `alias`.
> --- `tools/_briefing/render.py`

- Immediate return: rendered/sent diagnostics or saved dry-run HTML; SMTP errors return failure.
- Later read-back: retained briefing body reaches later email readers; graph-node links offer another reader-initiated retrieval channel.
- Delegated visibility: inapplicable — deterministic send/render route does not create a model frame.
- Selection predicate: explicit `--file` or maximum integer year/week; links require graph base plus truthy bundle idmap entry; nonnodes become plain aliases, plaintext always loses link targets.
- Invalidation or expiry: later source edits do not recall sent email; refreshing node idmap requires rebuild; actual delivery/retraction controls outside inspected scope.
- Activation or effect: code prepares content and calls sender; receipt and human use unobserved.
- Evidence limits: no complete evidence that links to all referenced meta pages survive; missing idmap/private graph removes links without removing prose.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Memory lineage distinguishes landed raw originals, source reflections, hub additions and later narrative synthesis. Models author interpretations; code writes derived access structures; starting ingest does not approve each generated claim. The durable semantic results are [MEM-OBJ-source](#mem-obj-source), [MEM-OBJ-hub](#mem-obj-hub), [MEM-OBJ-narratives](#mem-obj-narratives). Source-format rules request retained quotes/attribution; original-document fidelity remains unverified without raw originals. Physical writes precede final review according to this supplied route, so “not yet published” is not a filesystem quarantine guarantee. Future query/authoring reads give content evidential, model-interpreted authority; typed links separately have fixed parser consequences.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

The selection/delivery chain is question classification → model-authored search intent/lex/vec or structural edge request → ranked pointers → full-body get/read → Reporter synthesis. Default read budget is top ≤10 bodies, not proof that ten contain complete evidence. Graph query's own output budget defaults to 60 lines (`DEFAULT_BUDGET = 60` in SRC-1 `tools/_query/graph.py`); line truncation is neither a token budget nor content freshness filtering. QMD ranking/embedding payload and model context remain opaque. No-save output need not become retained wiki memory; explicit save starts a new reviewed synthesis object. Supplied source quotations in this route ground the body-get and save distinctions.

#### On [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation)

Fresh invocation keeps deliberation/tool traffic outside the caller's context; final report and shared file effects escape. This resembles a selected-input task frame, not an in-memory pointer heap: later access requires another tool read, and shared files outlive the frame independently. The supplied route establishes the requested fresh/re-read behavior, not the host's actual isolation. Resume is an alternative context-retaining checkpoint form, not a derived wiki summary; its actual transcript/window storage is outside SRC-1. No host trimming/compaction policy can be inferred from fresh-role instructions.

#### On [RT-RTE-faction-authoring](runtime.md#rt-rte-faction-authoring)

Persistent advocate contexts retain camp framing until session end; neutral synthesis uses a fresh context. Reports/full grounding cross to synthesis, not the full internal camp state by default. Missing reports can be recovered from host JSONL transcripts; that is explicit raw-transcript read-back for handoff recovery, not automatic trace-to-guidance learning. Host transcript persistence and actual recovery unobserved. The supplied route's source passage and context account establish this alternative to ordinary anonymous frame disposal.

#### On [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Build persistence spans graph, clusters, contradiction/overlay state, catalog/AUTO blocks, access indices, body bundle and dependencies; see their separate objects above. [MEM-RTE-cluster-rebuild](#mem-rte-cluster-rebuild) is a genuine prior-result consumer. Most other build outputs are copied/parsed current wiki state, not automatically learned experience. Source-URL enrichment is a narrowly automatic metadata admission path distinct from model prose admission.

Staleness diagnostics select candidates for later regrounding but do not withhold stale prose from ordinary reads. The current checker includes roots through Git body dates even though the dependency-builder docstring says otherwise. The operator-triggered reground runbook narrows overview rereads to new primary-source deltas; high-risk prose gets Desk, timelines/trails get lint/main spot review. On deletion it requests checking every removed segment against the current body, not trusting the author's remembered deletion set. SRC-1: `tools/_lint/staleness.py`, `.claude/operations/staleness-reground-runbook.md`.

> If the update deletes anything, pull every deleted segment with `git diff --word-diff -U0 HEAD -- <page>` and check each against that page's current body
> --- `.claude/operations/staleness-reground-runbook.md`

#### On [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export)

Export delivers a materially reduced retained corpus: root meta and selected narrative merges plus source title/slug/date locators, not source/entity/concept bodies. `_clean_body` removes comments except a guarded link-bearing case, so editorial sourcing memos/reasons do not reliably survive. `_source_locator_line` deliberately omits summaries. Uploaded/pasted context is operator-controlled; the future hosted answerer interprets surviving prose and instructions, while graph links allow reader retrieval of details rather than guaranteeing automated fact access. SRC-1: `tools/export.py`.

The code estimates 0.25 tokens/English character or 0.75 in Korean mode, greedily recommends Core under 200,000 estimated tokens and marks overflow Optional. This is a recommendation generated by code, not enforcement of provider context limits or installed upload membership. Local stale Markdown is pruned; remote uploads/answers are not recalled. The code's “loaded whole” comment is provider-facing doctrine, not inspected provider behavior.

> Summary snippets were dropped — they added
>     ~118K tokens (the dominant share of this index) for marginal value over the
>     headline, and the full summary is one deep-link away in the graph.
> --- `tools/export.py`

#### On [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change)

Trace origin is mixed: human utterances in one channel, verifier/model/deterministic defects and claimed measurement decisions in the other. [MEM-RTE-feedback-review](#mem-rte-feedback-review) and [MEM-RTE-failure-review](#mem-rte-failure-review) preserve the intermediate selectors, retained histories and limits. The final durable behavior-shaping result is edited tracked guidance/checks/hooks, not the miner's score alone. Consumers are future role invocations through the supplied [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance), or deterministic tools through their changed code/configuration. Reasons persist in transition rationale and rejected notes, but routine next-cycle grounding is of the new guidance, not proof of rereading every historical rationale. Rejected notes must be consulted before reproposing; `.claude/memory/` itself is unavailable. No observed future-use or improved-capacity conclusion follows merely from a retained accept record.

#### On [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback)

This is an automatic push into current context: Write/Edit event path and content select static reminders; post-edit broken-link checking rereads the file. Up to eight broken links are named with an overflow count, multiple messages merge into `additionalContext`; exceptions can silence the probe. This supplies selected current state, not necessarily accumulated memory. CLI/shell bypass limitations remain as supplied. SRC-1: `.claude/settings.json`, `.claude/hooks/dispatch.py`.

> hits = ", ".join(f"`[[{b}]]`" for b in bad[:8])
> --- `.claude/hooks/dispatch.py`

## Write side

**Knowledge acquisition and authoring.** Source documents are external evidence, not traces of the wiki's own decisions. Reporter derives source reflections; Columnist derives broader narratives; symbolic frontmatter/links survive alongside interpreted prose. Ingest, optional query-save, regrounding and legacy-host entry paths must not be collapsed into one universal Desk gate. Per-content human admission is established for optional synthesis save and named human-gate cases, not all source claims. Relevant records: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-OBJ-source](#mem-obj-source), [MEM-OBJ-narratives](#mem-obj-narratives).

**Automatic transformations.** Build regenerates metadata and display bundles; it preserves narrative regions rather than proving semantic updates. URL enrichment is automatic when blank, preserves mismatches. Prior partition reuse/warm initialization is a different retained-result dependency from re-parsing current pages. Mechanical fixes, emitted rewrite instructions and interpreted content rewrites have distinct admission mechanisms. Guidance to act is not completed action. [MEM-OBJ-access-indices](#mem-obj-access-indices), [MEM-RTE-cluster-rebuild](#mem-rte-cluster-rebuild), [RT-RTE-build-lint](runtime.md#rt-rte-build-lint).

**Rejection and withdrawal.** Defects return to authors and can block publication by protocol. Demotion nominates, Desk judges, link repair precedes deletion. Absorbed/delegated citation anchors may remain. Regrounding checks removed segments; build/export reconstruct local selected outputs, but stale hosted copies and email are separate persistence horizons. No global transactional rollback, universal archive filter or guaranteed removal from every downstream consumer is established. [MEM-RTE-hub-withdrawal](#mem-rte-hub-withdrawal), [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export), [MEM-RTE-briefing-read](#mem-rte-briefing-read).

**Trace-fed update.** Raw host turns are filtered to snippets/counts; verifier outcomes are encoded into structured defects. These intermediate results feed diagnosis and proposed guidance. Accepted edits can enter later role/tool behavior through instruction reads or changed executable machinery. The ledger retains reasons, while display summaries can omit or truncate them; rejected local notes carry a reread obligation but do not travel with fresh clones. Schema admission, model interpretation, operator approval and physical append/edit are separate steps. Checkpointing prevents repeated review from being mistaken for content learning, and raw logs alone establish neither an update nor improved capacity. [MEM-RTE-feedback-review](#mem-rte-feedback-review), [MEM-RTE-failure-review](#mem-rte-failure-review), [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change).

No inspected mechanism here compacts host conversation into a retained summary consumed by later model calls. This is a boundary limit, not an evidenced absence of host compaction: host internals, auto-memory and complete transcripts are outside or unavailable. Known alternatives are fresh frames, resumed IDs, persistent faction frames, explicit transcript recovery and reloadable external wiki files. [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation), [RT-RTE-faction-authoring](runtime.md#rt-rte-faction-authoring).

## Read-back

| Later consumer | Selection and delivery | Authority and limits |
|---|---|---|
| Reporter answering | Question intent and graph/QMD ranking → pointer → full body, top ≤10; graph output default 60 lines | Evidence for model synthesis, not executable truth; QMD internals and actual use unobserved. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) |
| Reporter/Columnist authoring | GROUND ladder requested reads and bounded expansion; guide-required context bypasses expansion count | Model interprets retained evidence; sufficiency is judgment. [MEM-RTE-grounding-ladder](#mem-rte-grounding-ladder) |
| Desk/reground author | Per-page upstream/delta or one-cluster bundle; original rereads for attribution | Advisory dates nominate, model review can reject/route correction; no automatic freshness withholding. [MEM-OBJ-dependencies](#mem-obj-dependencies), [MEM-OBJ-narratives](#mem-obj-narratives) |
| Next clustering/build | Prior partition and label history; graph fingerprint/hub coverage/backend/cold selectors | Fixed algorithmic effect, not model interpretation or demonstrated quality gain. [MEM-RTE-cluster-rebuild](#mem-rte-cluster-rebuild) |
| Editor-in-Chief proposing changes | Requested miner report, latest historical decisions, local rejected directions | Diagnostic/proposal context; reasons partly require full-ledger/local-note lookup; operator governs adoption. [MEM-RTE-failure-review](#mem-rte-failure-review), [MEM-RTE-feedback-review](#mem-rte-feedback-review) |
| Future role/tool invocation | New guidance explicitly re-grounded; code/check/config changed under same admission route | Interpreted instruction authority or fixed code consequences, not evidence of compliance or benefit. [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change) |
| Foreground model after edit | Event-selected reminder and current broken-link diagnostics automatically pushed | Current context intervention, not retained semantic summary. [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback) |
| Browser reader | Graph-selected node/overlay/overview → lazy body maps | Display knowledge and navigation; no model consuming all graph content automatically. [MEM-RTE-browser-read](#mem-rte-browser-read) |
| Hosted answerer / email reader | Operator-uploaded reduced export or selected retained weekly briefing | Export omits bodies/reasons; email rewrites or drops links. Remote loading, reliance and refresh remain unobserved. [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export), [MEM-RTE-briefing-read](#mem-rte-briefing-read) |

## Integration issues

- **No supplied-record correction required.** The memory findings elaborate the runtime without changing its declared identity or values. New object records have no runtime object counterpart; new specialized routes are either explicit parts of the build/change routes or distinct selectors/consumers with comparisons stated locally. No known duplicate declaration remains.
- **Source documentation disagrees about root staleness.** `tools/_build/dependencies.py` describes root dates as null/out of scope, but `tools/_lint/staleness.py` and the reground runbook include roots through Git body dates. [MEM-OBJ-dependencies](#mem-obj-dependencies) preserves both and follows the later consumer. Consequence: do not infer absent root checking from the serialized date alone.
- **Admission is not quarantine.** Supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) places writes before final review; direct CLI/export consumers have no established universal approval predicate. Open operational question: can deployments expose those writes before review? Missing invocation/publication evidence prevents a deployment-level answer, not the source-level distinction.
- **Archive/withdrawal is consumer-specific.** [MEM-RTE-hub-withdrawal](#mem-rte-hub-withdrawal) excludes archived inbound counts; [MEM-OBJ-pages](#mem-obj-pages) separately filters active meta bodies; graph's inspected `os.walk` collection does not establish blanket archive-directory pruning. Consequence: no system-wide “archived means forgotten” classification or propagation guarantee.
- **Historical reasons versus display summaries.** [MEM-RTE-failure-review](#mem-rte-failure-review) retains full ledger reasons but shows truncated proposal/reopen text; [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export) removes comments and source summaries. Consequence: future consumers cannot be credited with reasons not delivered to them. Whether operators/models reread complete reasons in a deployment is unresolved.
- **Trace labels can mislead improvement attribution.** The failure miner's own implementation notes that only audit-stage retrospective sweeps are excluded from recurrence ordering; other retrospective stages can remain. The human miner compares pattern recurrence rather than adjudicated treatment success. [MEM-RTE-failure-review](#mem-rte-failure-review), [MEM-RTE-feedback-review](#mem-rte-feedback-review). Neither signal establishes causal learning benefit.
- **Unavailable local/opaque parts remain included uncertainties.** Initial local-note control, actual transcript/window/checkpoint contents, QMD embeddings/storage, host compaction and hosted export installation remain unresolved at their respective records. Known subsequent read/write mechanisms remain positive findings; missing local evidence must not erase them.
- **Evaluation closure remains incomplete.** The judge README names stored labels/scores but withholds scorer/question wording; these arrays were not independently analyzed in this role. No established automatic experiment-output admission route supplements [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change). Retained experiment availability does not establish runtime benefit.

## Limitations and checks

Source identity was rechecked against the registered Git revision. All added paths are under SRC-1 at that revision; no new source, prior characterization or target execution was used. Required invocation, job, member/peer types, collection, worker rules, complete record contract, boundary and runtime were read; truncated deliveries were recovered before continuing. Supplied runtime is provisional evidence, not an instruction to restrict source inspection. Method identity is the supplied job/type/contracts; no method revision was made or inferred from unrelated worktree history.

The report supports implemented file transformations and requested role behavior, not successful deployment, reliable model compliance, full source fidelity, exhaustive retrieval, causal benefit or exercised self-improvement. Thin/uninspected branches and unavailable material are enumerated in the coverage inventory and integration issues, not converted into absences.

Validation: the required role-aware Commonplace content validation passed. This establishes structural/reference/quotation checks only, not semantic acceptance or efficacy.
