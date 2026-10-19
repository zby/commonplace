---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki memory: retained wiki state and history, hub routing, access-derived demotion and human-approved L1 verification."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
source-identity: "https://github.com/MehmetGoekce/llm-wiki"
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
---

# llm-wiki memory report

## Boundary and evidence

The memory boundary includes setup-generated config/schema/indexes, ingested and imported wiki pages, optional query write-back, access logging, archive demotion, lint repairs and Dashboard feedback, and maintenance of an optional external Claude memory directory. The target supplies a prompt-managed knowledge loop rather than a memory server. The registered source is SRC-1 at the reviewed commit. All operational conclusions about the main loop are doctrine/design, not observations of model compliance. Bash/Python setup supplies the narrower implementation layer.

I directly read the complete `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`, both plugin manifests, `config.example.yml`, all eight templates and `docs/l1-l2-architecture.md`. The last document extends the initial boundary inspection; its examples and pilot account are design/reported operation, not captured runs. A tracked-tree enumeration checks the shipped entry surface: the scripts and plugin/skill paths expose no additional target-owned CLI service, registered retrieval tool or hook. This finding does not inventory the external host's tools. Supplied runtime records organize the analysis but do not substitute for those direct reads. SRC-1, `SKILL.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/init-wiki.sh`, `setup.sh`.

Excluded implementations are Claude Code's session, provider, compaction and L1 loading, and Logseq/Obsidian link resolution. User vaults, original source collections and real L1 files were not supplied. Consequently actual memory contents, provenance completeness, host payloads, loading budgets, executed checks and later behavioral effects remain uninspected. Provider numerical state is already bounded in [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code); no target embedding store or learned retrieval model is established by the inspected routes.

| Entry/operation | Directly inspected SRC-1 paths | Coverage and limits |
|---|---|---|
| Plugin and copied-command dispatch | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `setup.sh`, `SKILL.md` | [RT-BAP-skill-dispatch](runtime.md#rt-bap-skill-dispatch); static procedure loading, not use-derived read-back. External activation uninspected. |
| Script setup, skill setup, installer replacement | `scripts/init-wiki.sh`, `setup.sh`, `SKILL.md`, all `templates/logseq/` and `templates/obsidian/` files | [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [MEM-OBJ-config](#mem-obj-config), [RT-OBJ-schema](runtime.md#rt-obj-schema). Initial controls known; real user corpus absent. |
| URL/file/text ingest and Markdown import | `SKILL.md`, both Schema templates | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-page-state](#mem-obj-page-state), [MEM-OBJ-page-history](#mem-obj-page-history). Import's routing-description completeness remains unspecified. |
| Query, fallback, optional write-back/re-promotion | `SKILL.md`, both Hub and Access-Log templates | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-OBJ-hub-index](#mem-obj-hub-index), [MEM-OBJ-access-log](#mem-obj-access-log), [MEM-BAP-wiki-answer](#mem-bap-wiki-answer). No actual retrieval trace or eviction proof. |
| Access profiling, archive demotion | `SKILL.md`, both Hub templates | [RT-RTE-index-prune](runtime.md#rt-rte-index-prune), [MEM-OBJ-hub-archive](#mem-obj-hub-archive). Trace-derived index changes are prescribed, not observed. |
| L1 classify/check/correct/demote/delete | `SKILL.md`, `docs/l1-l2-architecture.md`, both Schema templates | [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification), [MEM-OBJ-l1-rules](#mem-obj-l1-rules), [MEM-OBJ-l1-index](#mem-obj-l1-index). Initial authoring/admission and host loading remain external. |
| Lint, lint --fix, status | `SKILL.md`, both Dashboard templates | [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance), [MEM-OBJ-dashboard](#mem-obj-dashboard). No separate executable evaluator or quality outcome supplied. |
| Session isolation, trimming, compaction, checkpoints | Complete `SKILL.md`, manifests and setup scripts | Query specifies selective reads and JIT batching; no target-controlled frame-pop, context deletion or checkpoint form is specified in these paths. Host alternatives uninspected; cannot conclude their absence. |

## Core ideas

1. **Selection metadata precedes detailed content.** A question selects namespace hubs, then descriptions/tags select three child pages, at most five. The retained index is a lossy page-level description, not a semantic-vector representation. It can omit relevant facts or misroute questions. Grep is an explicit alternate path, so missing routing does not mean inaccessible knowledge. [MEM-OBJ-hub-index](#mem-obj-hub-index), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).
2. **Current state and superseded state coexist.** Ingest rewrites the active statement while retaining old wording under History. Folding is a display convention, not evidence that full-page tool reads hide history from the model. The page count limit does not bound bytes or tokens. [MEM-OBJ-page-state](#mem-obj-page-state), [MEM-OBJ-page-history](#mem-obj-page-history).
3. **Access traces influence later selection, not factual truth.** Full-page reads generate Access-Log lines. Prune uses recency plus exemptions and human confirmation to change the live index; status exposes hot pages and matching reasons. Raw logs are distinct from the durable behavior-shaping archive/index change. Neither popularity nor selection demonstrates usefulness. [MEM-OBJ-access-log](#mem-obj-access-log), [RT-RTE-index-prune](runtime.md#rt-rte-index-prune).
4. **L1 freshness is reviewed rather than enforced at use.** Classification and verification dates select rules for local evidence checking; approved corrections reach body, description and index. Demotion changes always-loaded instructions into on-demand history. A date does not veto a stale rule at an action boundary. [MEM-OBJ-l1-rules](#mem-obj-l1-rules), [MEM-OBJ-l1-index](#mem-obj-l1-index), [RT-ABS-action-gate](runtime.md#rt-abs-action-gate).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-config
Label: llm-wiki configuration

Source-native `llm-wiki.yml` is filesystem YAML generated from setup flags/user answers; `config.example.yml` illustrates the fields. Paths, mode and namespace names are symbolic configuration in the initializer, then model-interpreted selectors in the skill. The initializer does not create or populate L1 from `memory_path`; it records the pointer. `l1_verify_days` is optional, defaulting to 90 in the skill rather than being emitted by initialization. Persistence is across invocations until edited/replaced. It contains access/selection metadata, not retrieved knowledge. SRC-1, `scripts/init-wiki.sh`, `config.example.yml`, `SKILL.md`.

Closest supplied record: [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) produces this object; that route and [RT-OBJ-schema](runtime.md#rt-obj-schema) are not duplicate configuration objects. Later command consumers are specified by [RT-BAP-skill-dispatch](runtime.md#rt-bap-skill-dispatch).

> Read `llm-wiki.yml` from the wiki root FIRST (every command except `setup`, which creates it).
> --- `SKILL.md`

#### MEM-OBJ-page-state
Label: Wiki current state

Wiki content is natural-language knowledge, decisions, workflows, and code examples on filesystem Markdown pages. Logseq uses flat `pages/Wiki___...md`; Obsidian uses `Wiki/...md`. Properties and links expose localized fields, but the inspected maintenance/query consumers interpret them through the model rather than an implemented type checker. External UI consumption is not inspected. Lineage is user URL/file/text extraction, Markdown conversion, confirmed answer write-back, or L1 demotion; original source retention and precise fact-to-source derivation are not universally specified. A source property is required for entity pages and import, not a universal complete evidence chain. SRC-1, `SKILL.md`, `templates/logseq/Schema.md`, `templates/obsidian/Schema.md`.

No supplied object counterpart: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) produce/consume this state. Unlike [RT-OBJ-schema](runtime.md#rt-obj-schema), this is the maintained knowledge, not the conventions. Later query treats it as answer material; maintenance treats it as editable state, not automatically trusted instruction. Correctness and source authenticity are not independently established.

> Phase 2 - Synthesize:
>   - Combine information from multiple wiki pages
>   - Note confidence levels (from page properties)
>   - Check staleness (updated dates)
>   - Formulate comprehensive answer with source attribution
> --- `SKILL.md`

#### MEM-OBJ-page-history
Label: Wiki History and Change log

Natural-language historical content is retained inside the same Markdown substrate but distinguished from active state by a collapsed Logseq child or folded Obsidian callout. Hub change notes use Change log; superseded statements use History. Lineage is explicit movement of old wording, dated newest-first; a demoted L1 rule supplies a carry-over summary/history block marked `source:: l1-demotion`. That summary can drop information, unlike ingest's verbatim superseded wording. Full-page query and maintenance can receive this history, but no separate query policy guarantees examination of historical reasons. Reasons survive only insofar as old wording or the carry-over summary contains them; an independently persisted verification-evidence report is not required. SRC-1, `SKILL.md`.

No supplied object counterpart; related producer is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), with an additional producer [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification). History is not a context checkpoint and does not encode the full host conversation.

> - Delete nothing, but overwrite stale state: superseded statements move verbatim into the block's
>   collapsed `History` (§ State + History) — never append "Status <date>:" addenda to running prose.
>   Blocks without a new state stay untouched
> --- `SKILL.md`

#### MEM-OBJ-hub-index
Label: Hub Index routing lines

Each namespace hub stores a live `### Index`: page links plus natural-language descriptions, capped at 120 characters, and tags mirroring page tags. This is derived access metadata rather than the full knowledge payload. The foreground model ranks it against the question. Links have symbolic-looking structure, but the inspected ranking is model-mediated. Ingest creates/refreshes lines; lint --fix backfills from title, first content block and tags; confirmed re-promotion restores an archived line. User-chosen namespaces and template placeholders initialize the structure, not a populated corpus. SRC-1, `SKILL.md`, `templates/logseq/Hub.md`, `templates/obsidian/Hub.md`.

No supplied object counterpart: [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) and [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) operate on this metadata. It differs from static schema guidance and the archived lines below. Ranking inputs can change without changing page content.

> - Description <=120 chars, distinctive (it is the routing key), no filler ("Info about ...")
> - Tags mirror the page's own #tags — multi-match across tags is fine
> --- `SKILL.md`

#### MEM-OBJ-hub-archive
Label: Hub Archive routing lines

`### Archive` stores demoted routing lines verbatim in hub Markdown. The linked page remains at its old path with an `archived` date and, only for entity pages, archived status. Thus this object retains prior selection metadata; it is not a deleted-content bin. Its later consumers are maintenance/re-promotion and a human inspecting the hub. Ordinary query's preferred selector reads live Index; grep can rediscover the underlying page. A full hub read can physically expose Archive text even though routing instructions exclude it from preferred selection. SRC-1, `SKILL.md`, both Hub templates.

No supplied object counterpart; producer is [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) and alternate read-back is [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). This is a separate operative part from live Index because selection treatment and recovery differ.

> - Move the routing line from the hub's `### Index` VERBATIM into the hub's `### Archive` section
>       (move, not delete)
> --- `SKILL.md`

#### MEM-OBJ-access-log
Label: Access-Log read traces

Source-native `Wiki/Reference/Access-Log` is append-only filesystem Markdown in the selected format. Date/page/query fields are structured trace metadata; a short natural-language `matched:` reason records a routing description/tag or grep term. The template seeds a bootstrap line, not a user query. Legacy lines without reasons remain valid. The log is not a transcript, source evidence, content summary or independent success signal. No automatic retention limit is specified. SRC-1, `SKILL.md`, `templates/logseq/Access-Log.md`, `templates/obsidian/Access-Log.md`.

No supplied object counterpart; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) produces it, [RT-RTE-index-prune](runtime.md#rt-rte-index-prune) and [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance) consume it. Only actual full-page query reads are required to enter it, not hub reads, arbitrary host reads or later utility. The fixed-position parsing rule is specified in prose, not implemented as a target parser.

> - prune/status parse the date + `[[page]]` from fixed positions (split on ` -- `); the `matched:` suffix is
>   irrelevant to LRU aggregation and does not affect parsing
> --- `SKILL.md`

#### MEM-OBJ-l1-rules
Label: L1 memory rule files

Source-native L1 files reside in the configured memory directory. Bodies and frontmatter descriptions are natural-language behavior rules, preferences, identity or credential references; `asserts-current-behavior` and `verified` are structured maintenance selectors interpreted by the agent. Initial files, authorship, admission controls and secret representations are not supplied. Known subsequent transformations remain inspectable: classification adds confirmed metadata; re-verification stamps the date, with corrected text on contradictions; demotion/deletion removes approved files after reference repair. Metadata can be top-level or under `metadata:` and other keys must survive unchanged. SRC-1, `SKILL.md`.

No supplied object counterpart: [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) is the maintenance route; [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) is the external consumer/runtime, not these files. Host loading of body versus description is not independently inspected. Corrections are requested on both surfaces, avoiding the unsupported assumption that only bodies steer future work.

> - Writes MUST NOT reorder or remove other frontmatter keys
> - The L1 index file (e.g. MEMORY.md) carries neither key
> --- `SKILL.md`

#### MEM-OBJ-l1-index
Label: L1 memory index

The index, exemplified by `MEMORY.md`, is a separate Markdown access/summary surface. It points to rule files and may point to L2. Its lines can carry claim text; deleting a file is insufficient if its index line still states the claim. It is excluded from rule classification/due selection but included in correction and reference repair. One line can point to several files. Initial authorship and the exact host-selected payload/budget remain uninspected. SRC-1, `SKILL.md`, `docs/l1-l2-architecture.md`.

No supplied object counterpart; [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification) maintains it. This is not the L2 hub Index: a different store, loading contract and deletion policy apply.

> - Scan every L1 memory file EXCEPT the index file (e.g. MEMORY.md — an index, not a rule). Its lines are
>     auto-loaded too: keep them in step whenever a rule is corrected, demoted, or deleted
> --- `SKILL.md`

#### MEM-OBJ-dashboard
Label: Wiki Dashboard metrics

Generated Dashboard is Markdown containing namespace/schema links, then lint health metrics and timestamp. It is derived evaluation metadata, not an independent evaluator, correctness certificate or full diagnostic history. Status can compare against it; the main status procedure explicitly requests no modifications. Template wording attributing updates to status therefore does not establish a status write path. Historical metric-series retention is unspecified. SRC-1, `SKILL.md`, `templates/logseq/Dashboard.md`, `templates/obsidian/Dashboard.md`.

No supplied object counterpart; producer/consumer is [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance). Dashboard differs from the direct returned status report.

> Phase 5 - Dashboard Update:
>   - Update Dashboard page with current health metrics
>   - Timestamp the lint run
> --- `SKILL.md`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-answer
Label: Retained wiki knowledge to answers

Consumer: a later foreground query agent. Channel: requested hub reads, selected full-page Read results, or grep fallback followed by selected reads. Force: natural-language informational evidence for synthesis with source attribution, dates and confidence, not an independently enforced instruction priority. Horizon: later query invocations across sessions while pages remain. Delivery, actual reliance and improved answers are distinct; only the prescribed route is established. SRC-1, `SKILL.md`; the synthesis passage in [MEM-OBJ-page-state](#mem-obj-page-state) supplies the direct warrant. This path is distinct from [RT-BAP-schema-guidance](runtime.md#rt-bap-schema-guidance), which delivers maintenance conventions, and supplements the existing [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) rather than duplicating a route.

#### MEM-BAP-l1-loading
Label: L1 rules and index to later sessions

Consumer: external Claude Code sessions. Channel: host automatic memory loading as described by the target. Force: behavior-steering rules/preferences and index summaries supplied as natural-language context. Horizon: subsequent sessions until corrected or removed. This is an afforded external consumer role, not inspected loading wiring or proof every file body loads. The maintenance operation specifically corrects body, description and index; exact host selection and budget are unknown. SRC-1, `SKILL.md`, `docs/l1-l2-architecture.md`; [MEM-OBJ-l1-index](#mem-obj-l1-index) supplies the loading passage. Unlike [RT-BAP-skill-dispatch](runtime.md#rt-bap-skill-dispatch), the payload is use-maintained personal memory, not the installed skill. No action-time stale-rule gate is implied: [RT-ABS-action-gate](runtime.md#rt-abs-action-gate).

## Annotations

#### On [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup)

Known initial lineage is templates plus date/namespace/path substitution. The script persists Schema, Dashboard, hubs, Access-Log and configuration; it does not create personal L1 rules. Physical writes are executable Python after argument validation. Skill setup collects human choices, the shell installer collects answers directly, and direct initializer invocation has only caller-supplied flags; that last path does not establish per-content human review. Existing-path checks preserve files, but installer-confirmed config removal is a distinct admission/replacement step. Static copied skill/schema delivery is not use-derived read-back. SRC-1, `scripts/init-wiki.sh`, `setup.sh`, `SKILL.md`; [MEM-OBJ-config](#mem-obj-config).

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

The model authors derived content and descriptions, while host tools perform I/O. User invocation supplies the source but does not individually approve extracted facts. The schema/quality gate is model-mediated admission. Existing current state becomes dated historical material; no full input transcript or universal provenance graph is required. Import is a separate bulk lineage and only explicitly requires child links, not complete descriptions. These outputs reach later query, lint and prune consumers through [MEM-OBJ-page-state](#mem-obj-page-state), [MEM-OBJ-page-history](#mem-obj-page-history) and [MEM-OBJ-hub-index](#mem-obj-hub-index). SRC-1, `SKILL.md`, both Schema templates; supplied route quotations support the transformation and gate. Quick-rule routing recommends Memory; it is not an inspected automatic L1 admission path.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Read-back is request-driven: the human asks, the foreground model chooses namespaces and ranks retained index lines, and tools deliver selected page text. The instruction selects three children, maximum five, with at most three loaded simultaneously. No token budget, hub-count cap, separate task context, eviction operation or summary checkpoint is specified. Already returned text remains host-managed; JIT describes preferential admission, not a demonstrated frame-pop. In a stack-frame analogy no isolated callee frame is established; links name external files but are not by-reference window objects that can be freed. SRC-1, `SKILL.md`; the route supplies the fallback and limits.

Raw query-read traces persist separately from selected page content. Access logging is prescribed without per-content confirmation. Optional page write-back and archive re-promotion require user acceptance; they must not be conflated with log admission. [MEM-OBJ-access-log](#mem-obj-access-log) retains the short selector reason, not whether synthesis was correct. Full-page delivery can include current state and history; collapsed UI markup does not establish model-visible omission. Whether a host strips/folds payloads is uninspected.

#### On [RT-RTE-index-prune](runtime.md#rt-rte-index-prune)

The trace chain is full-page query reads -> append-only date/page records -> latest-access profile, with creation date as missing-log proxy -> model-proposed cold candidates -> human-confirmed archived marker and routing-line move -> later preferred query selection. It is use-trace-fed selection maintenance, not automatic unapproved learning. The intermediate profile need not persist; the durable behavior-shaping result is live Index membership versus Archive. The original log remains available to explain access recency, and the archived line preserves the routing description. No per-demotion persisted rationale beyond markers/log/history/Git is required. Later query is not instructed to consult the original access evidence before using the changed index. SRC-1, `SKILL.md`; [MEM-OBJ-access-log](#mem-obj-access-log), [MEM-OBJ-hub-archive](#mem-obj-hub-archive). The source's LRU/access-frequency language describes thresholded last-access pruning, not a capacity-bounded least-recently-used eviction algorithm.

#### On [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification)

Initial L1 authorship/admission remains unknown; subsequent classification, correction, date changes and deletion have explicit per-item human control. The body, description and index are separate later-loading surfaces. Due dates select review, not automatic expiration. The per-claim evidence/verdict is shown to the user; no separate durable evidence report or later reader of the full checking rationale is required. Retained outputs are metadata/corrected claims, rewritten references, and optional L2 carry-over history. SRC-1, `SKILL.md`; [MEM-OBJ-l1-rules](#mem-obj-l1-rules), [MEM-OBJ-l1-index](#mem-obj-l1-index), [MEM-OBJ-page-history](#mem-obj-page-history).

Demotion changes authority: a corrected L1 rule can steer later sessions through host loading; demoted text becomes query-selected historical knowledge. A successful wiki write is a required predecessor of deleting the L1 file. Carry-over summaries name kept/dropped content before approval, so demotion does not guarantee complete verbatim preservation. Skip rejects change and stays due; deletion intentionally retains nothing. Credentials cannot take the demotion path. The supplied theory account remains bounded: retained correction can shape later checking/loading, but no actual improvement, autonomous admission or exercised theory revision is established.

#### On [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance)

Lint --fix is caller-authorized model editing, not individual confirmation for each repair. It can derive routing descriptions from title/first block/tags, downgrade stale confidence, create stubs and add links; these are content/selection transformations beyond mere counting. Current-state judgment is explicitly withheld for oversized blocks. Plain lint still writes Dashboard metrics, whereas status requests no modifications. L1 stays read-only even with --fix. SRC-1, `SKILL.md`; [MEM-OBJ-hub-index](#mem-obj-hub-index), [MEM-OBJ-page-state](#mem-obj-page-state), [MEM-OBJ-dashboard](#mem-obj-dashboard).

> - Backfill routing lines: an active page with no index entry -> generate a routing line from the page
>     title + first content block (as a one-sentence description) + its existing #tags, insert into the
>     hub `### Index` (bootstraps old hubs that only carry bare link lists)
> --- `SKILL.md`

## Write side

The acquisition/admission boundaries differ by mechanism, not merely by file writer:

| Mechanism | Author/transformation | Admission and rejection | Persisted result / later consumer |
|---|---|---|---|
| Setup | Script renders shipped templates and chosen settings | User choices in wrappers; syntax/existence guards in initializer; direct caller control unresolved as human review | Config/schema/skeleton; later commands |
| Ingest/import | Model extracts, converts, redistributes and links supplied content | Workflow invocation plus model quality/lint checks; no per-fact approval | Current state/history/index; query and maintenance |
| Query trace | Model records actual full-page reads and short matching reason | Prescribed append, no per-query confirmation | Access-Log; prune/status |
| Query knowledge write-back | Model proposes gap fill/summary | Human confirms or declines | Page/index content; later query |
| L2 pruning / re-promotion | Model profiles age or detects archive re-hit | Human confirms candidates/re-promotion | Index/Archive and archive marker; later query |
| L1 classification/verification | Model proposes class, checks evidence and recommends actions | Per-item human approval, override, skip or delete | Rule text/date/description/index or L2 history; later host loading/query |
| Lint repairs / Dashboard | Model diagnoses and generates repairs/metrics | --fix enables repairs; no per-fix approval; plain lint still updates Dashboard; L1 changes prohibited | Page/index repairs and Dashboard; later query/status |

This table follows the source contract in SRC-1, `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`, with the supporting passages in the annotated runtime records. It does not assume the host enforces these policies.

Source trust is limited to the user's source choice, model extraction and schema/credential checks; URLs can be fetched, and the inspected ingest route supplies no independent authenticity or prompt-injection boundary. Confidence and dates are retained qualifiers, not independent truth judgments. L1 checks have stronger local evidence instructions but can remain partial or inconclusive; user knowledge can admit re-verification. The documentation's phrase “hard security boundary” is not supported as target-enforced isolation: model-interpreted credential policy and a requested lint scan are the inspected mechanisms. SRC-1, `SKILL.md`, `docs/l1-l2-architecture.md`; [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification).

Withdrawal is not uniform. Wiki supersession retains old text; L2 demotion retains file and links; lint can remove orphaned metadata; L1 deletion removes the file and references after approval, without Git undo. “Delete nothing” cannot be generalized to L1. Structural Git commits support manual recovery of wiki edits, not atomic multi-file rollback; failed commits and partially completed setup remain possible. No target session-compaction or alternative checkpoint persistence path is specified in the inspected operational files. SRC-1, `SKILL.md`, `scripts/init-wiki.sh`; [MEM-OBJ-page-history](#mem-obj-page-history), [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup).

## Read-back

The material read-back routes are already declared by runtime and annotated here; none needs a duplicate route ID.

- **Question to answer:** question -> namespace hubs -> description/tag ranking -> three to five full pages -> synthesis. Fallback grep selects from all wiki pages, including archived ones. Targeting is semantic model judgment over natural-language metadata, not an identifier-only lookup. The channel is foreground tool results; authority is informational at synthesis. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-BAP-wiki-answer](#mem-bap-wiki-answer).
- **Use traces to future selection:** Access-Log -> recency/exemptions -> approved demotion -> live-index change -> later query selector. No unsolicited model-context push is established: the user/external scheduler requests prune and a subsequent question requests retrieval. [RT-RTE-index-prune](runtime.md#rt-rte-index-prune).
- **Retained content to maintenance:** later ingest reads existing target pages; lint reads all page properties/link graph and optional L1 metadata; prune reads access traces; status reads log/Git/Dashboard. These routes can revise future inputs but are not answer-quality experiments. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance).
- **L1 to sessions and reviews:** automatic loading is an attributed host role, with unknown exact payload and budget; llm-wiki itself requests rule scans for review and optional L1 reads during query. Approved corrected text/index can survive to later sessions; demoted text reaches only L2 retrieval unless some external host route also reads it. [MEM-BAP-l1-loading](#mem-bap-l1-loading), [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification).

The explicit page-count limit bounds selected objects, not the window. No inspected target operation removes prior turns/tool results or isolates a child task. The cost and benefit of hub-first retrieval and archive demotion remain unmeasured, consistently with [RT-CLM-cache-precision](runtime.md#rt-clm-cache-precision).

## Integration issues

1. **No correction to a supplied runtime fact is required.** It already distinguishes JIT policy from eviction, import from ingest, log writes from approved knowledge write-back, and host loading from target control. New objects describe retained parts not separately declared there; the annotations retain its route identities. No possible duplicate declaration was identified after comparison with the supplied records. The new behavioral-authority paths concern knowledge/L1 payloads, not static skill/schema instructions.
2. **Unresolved host L1 payload and initial admission.** SRC-1, `SKILL.md` and `docs/l1-l2-architecture.md` describe automatic files/index loading, but no host implementation or actual L1 contents are frozen. Body/description/index distinctions must survive integration; do not turn [MEM-BAP-l1-loading](#mem-bap-l1-loading) into a guarantee that every body enters every window. Initial control remains unknown in [MEM-OBJ-l1-rules](#mem-obj-l1-rules); subsequent per-item control is known in [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification).
3. **Nonuniform routing production.** Import requires child links but not explicitly descriptions; lint --fix supplies a recovery path. Generated Hub templates also contain illustrative SubTopic text rather than proven real child targets. The source does not establish a complete usable index immediately after setup/import. This limits the preferred-route completeness of [MEM-OBJ-hub-index](#mem-obj-hub-index) without blocking grep fallback. SRC-1, `SKILL.md`, both Hub templates; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).
4. **Status/Dashboard wording drift.** Dashboard templates say “Last updated via `/llm-wiki status` or `/llm-wiki lint`.” The main status procedure says no modifications, matching runtime. Treat lint as the specified writer and status as consumer, not a proven baseline-series writer. SRC-1, both Dashboard templates, `SKILL.md`; [MEM-OBJ-dashboard](#mem-obj-dashboard), [RT-RTE-health-maintenance](runtime.md#rt-rte-health-maintenance).
5. **Security and freshness labels exceed their machinery.** `docs/l1-l2-architecture.md` calls credential separation a hard boundary and states files load every session; these remain target doctrine about an external host. The initializer's generated ignore lists cover UI/cache files, not an arbitrary configured memory directory. Therefore Git exclusion of L1 depends on placement/external configuration; it is not enforced for every `memory_path`. Preserve runtime's policy qualification and [RT-ABS-action-gate](runtime.md#rt-abs-action-gate). SRC-1, `scripts/init-wiki.sh`, `SKILL.md`, `docs/l1-l2-architecture.md`; [MEM-OBJ-config](#mem-obj-config), [MEM-OBJ-l1-rules](#mem-obj-l1-rules).
6. **Logical hub names versus Obsidian paths.** Initializer writes `_index.md` while skill links use namespace names. As already bounded by runtime, actual UI resolution is uninspected; no successful route is inferred from names alone. SRC-1, `scripts/init-wiki.sh`, `SKILL.md`; [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup), [MEM-OBJ-hub-index](#mem-obj-hub-index).
7. **Retained reasons are partial.** Access-Log retains short selection reasons, not outcomes; L1 re-verification retains dates/corrections but no required full evidence ledger; demotion can drop material after a carry-over summary. These limits prevent reconstructing a universal raw-trace-to-rationale-to-later-decision chain. SRC-1, `SKILL.md`; [MEM-OBJ-access-log](#mem-obj-access-log), [MEM-OBJ-page-history](#mem-obj-page-history), [RT-RTE-l1-verification](runtime.md#rt-rte-l1-verification).

## Limitations and checks

The source checkout HEAD was rechecked as `11538c1195666db24e25e23cc64bb1d70587aef9`; Git status reported no changes. The registered source identity, supplied boundary/runtime identity fields, member type, job instruction and records contract govern this report. New supporting documentation was read only inside SRC-1; no other source or prior analysis was consulted. No target command, test, example, host/provider call or runtime fixture was executed.

The inspected evidence establishes prescribed retained-state transformations and a small executable initialization path. It cannot establish credential isolation, model compliance, actual page contents, exact host payload selection, context reclamation, improved retrieval, learning or later causal dependence on a change. These limits do not erase the supported human/model write controls or request-driven selection mechanisms.

Validation: the invocation's deterministic `commonplace-run validate-output` check passed. This checks form, identities, references and quotation occurrence, not analytical correctness or actual operation.
