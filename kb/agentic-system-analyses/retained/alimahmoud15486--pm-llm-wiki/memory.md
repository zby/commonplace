---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "pm-llm-wiki memory: PM-curated sources, maintained Markdown product beliefs, index-first retrieval and optional answer file-back."
run-id: AAS-2026-11-09-pm-llm-wiki-4c3839e25928-01
source-identity: https://github.com/alimahmoud15486/pm-llm-wiki
reviewed-boundary: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
---

# pm-llm-wiki memory report

## Boundary and evidence

This report covers the complete shipped prompt-and-Markdown knowledge loop, not the external coding-agent host. SRC-1 at the [boundary](boundary.md) supplies doctrine/design and fictional reported operation. The retained pilot is inspectable content, not an authenticated agent execution. Sources, synthesized product state, operation records, access metadata, optional filed answers and changed maintainer instructions are included. External host conversation storage, provider state, tool permissions and context compaction are excluded; no conclusions about their retention, isolation or automatic injection follow.

Direct reads used SRC-1, `README.md`, `PM-Wiki-Content-Model.md`, `template/SCHEMA.md`, `pilot/CLAUDE.md`, `pilot/index.md`, `pilot/log.md`, all seven `pilot/sources/` files, and all eight `pilot/wiki/` pages. The tracked-tree listing and HEAD were also checked. Supplied runtime findings provide the provisional route inventory; direct reads checked their memory endpoints and counterexamples. References, contribution policy and infrastructure packaging are covered by the supplied boundary/runtime, not independently reread here. No additional source identity or evidence layer is introduced.

| Entry or memory operation | SRC-1 source paths | Coverage and limits |
|---|---|---|
| Initialization and instruction reload | `README.md`, `pilot/CLAUDE.md`, `template/SCHEMA.md` | Direct; [RT-OBJ-schema](runtime.md#rt-obj-schema), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent). PM copies and adds context; external host loading remains unspecified. |
| PM-supplied individual source | all seven files in `pilot/sources/`, `template/SCHEMA.md` | Direct; [MEM-OBJ-sources](#mem-obj-sources), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Source authorship varies; PM selection is not proof of truth. |
| High-volume digest admission | `pilot/sources/2026-06-27_digest_support-reviews-week26.md`, `template/SCHEMA.md` | Direct; [MEM-OBJ-digest](#mem-obj-digest), [MEM-RTE-digest-admission](#mem-rte-digest-admission). Raw exports and omission choices unavailable. |
| Problem synthesis and counters | both `pilot/wiki/problems/` pages | Direct; [MEM-OBJ-problems](#mem-obj-problems). Source mentions and raw item counts differ. |
| Belief/rationale maintenance | `pilot/wiki/assumptions.md`, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md` | Direct; [MEM-OBJ-assumptions](#mem-obj-assumptions), [MEM-OBJ-decisions](#mem-obj-decisions). Policy gates are not host enforcement. |
| Gap and contradiction retention, lint | `pilot/wiki/open-questions.md`, `pilot/log.md`, `template/SCHEMA.md` | Direct; [MEM-OBJ-open-questions](#mem-obj-open-questions), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). No executable evaluator or observed detection completeness. |
| Living synthesis and competitor maintenance | `pilot/wiki/overview.md`, `pilot/wiki/competitors/gymjoy.md`, `pilot/CLAUDE.md` | Direct; [MEM-OBJ-overview](#mem-obj-overview), [MEM-OBJ-gymjoy](#mem-obj-gymjoy), [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade). New schema does not demonstrate later compliance. |
| Index-first query and raw-source fallback | `pilot/index.md`, `template/SCHEMA.md`, `pilot/wiki/prd-adaptive-plans-v1.md`, `pilot/log.md` | Direct; [MEM-OBJ-index](#mem-obj-index), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback). Model relevance judgment; no token budget or deterministic ranker. |
| Optional answer admission and later availability | `pilot/wiki/prd-adaptive-plans-v1.md`, `pilot/index.md`, `pilot/log.md` | Direct; [MEM-OBJ-prd](#mem-obj-prd). Filed answer is cataloged; no later PRD-consuming invocation supplied. |
| Skip, pending approval, supersession, staleness | `template/SCHEMA.md`, `pilot/log.md`, decision page | Direct; ingest/lint/stage routes and [MEM-OBJ-log](#mem-obj-log). Rejection can prevent writes; staleness requests review rather than eviction. |
| CLI dispatch, hooks, tools, service/library operations | full tracked-tree listing; `README.md`, `template/SCHEMA.md` | Packaging cross-check supports supplied runtime's prompt-only account. No executable entry point in tree. Stage-3 search/hooks are prospective; external host tools uninspected, so no exhaustive host-route claim. |
| Broader model and lineage proposals | `PM-Wiki-Content-Model.md`; references via boundary | Draft explicitly proposes additional entities/search. Not silently treated as activated memory mechanisms. |

## Core ideas

The persistent artifact is an editable product account, not merely a transcript archive. Immutable source files support separately maintained problems, beliefs, rationale and questions. The model is instructed to carry forward their meaning into later answers, while preserving evidence and disagreement ([MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-assumptions](#mem-obj-assumptions), [MEM-OBJ-decisions](#mem-obj-decisions)). This establishes a designed reuse path, not improved model capacity.

The catalog is a working-context control: read it first, then select relevant pages. It keeps unrelated material out by a model-interpreted relevance rule. It is not an embedding index, a host memory pointer mechanism, a hard context budget or summarization of old conversation. The PRD's reported raw-source use falsifies a stronger claim that queries consume only precomputed wiki summaries ([MEM-OBJ-index](#mem-obj-index), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)).

Admission is heterogeneous. PM source curation and digest approval precede ingestion; model-authored ordinary wiki updates are mostly ungated; decisions, belief-status changes, supersession and schema edits require a direct PM reply. Starting an ingest does not approve every protected change. Physical writes remain external file-tool operations. Neither source trust nor write authorization is enforced by repository code ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-RTE-digest-admission](#mem-rte-digest-admission)).

Answers may return only in the conversation, or become retained explorations. That optional file-back preserves derived reasoning with source links, but does not convert inference into independent evidence. Changed schema also persists and can guide future maintenance; it is a different authority path from product knowledge ([MEM-OBJ-prd](#mem-obj-prd), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-sources
Label: Curated source files

Identity/storage/form: `sources/`, instantiated by the seven Markdown files under `pilot/sources/`. Natural-language evidence notes, quoted excerpts and numerical findings, not executable facts or numerical model parameters. These are upstream inputs relative to the wiki; they are not necessarily raw observations. Interviews are paraphrased transcript excerpts, analytics is a readout rather than raw data, intel is compiled commentary, and the digest is already derived. All pilot evidence is explicitly fictional (SRC-1, the seven source files).

Lineage/admission: PM curates which files enter; authors include interviewers, an analyst, meeting participants/intel compilers and the model-drafted approved digest. No external original recordings, datasets, exports or approval conversations are supplied. Consumers: ingestion extracts meaning into wiki pages; later query can return to originals for evidence. Behavioral force is evidential context, not permission or governing instruction. Sources are retained read-only by policy, with no automatic expiry; the agent is told never to edit or delete them. Closest supplied record is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), a transformation route, not this storage object; no supplied object counterpart.

> Key moments (paraphrased transcript excerpts):
> --- `pilot/sources/2026-06-22_interview_churned-user-maria.md`

> Findings (the readout, not the raw data):
> --- `pilot/sources/2026-06-25_analytics_cohort-retention-readout.md`

#### MEM-OBJ-digest
Label: Weekly feedback digest

Identity: `pilot/sources/2026-06-27_digest_support-reviews-week26.md`, a material derived source within [MEM-OBJ-sources](#mem-obj-sources). Substrate: Markdown. Form: natural-language ranked themes, counts and representative quote. Lineage: reported model summary of support/review exports, PM-approved as a source. The raw exports are not present, so selection losses and item-level derivation cannot be checked. This is product-interaction evidence, not the maintainer agent's own execution trace. Later ingestion and problem pages receive themes/counts, not the exports; the PRD repeats the 14-mention theme. Approval is admission control separate from model authorship and file I/O. Closest supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) includes this alternative input, but declares no distinct digest object (SRC-1, digest, problem page and PRD).

> FICTIONAL source, part of the FitLoop pilot demo. Digest drafted by LLM from raw exports,
> --- `pilot/sources/2026-06-27_digest_support-reviews-week26.md`

#### MEM-OBJ-problems
Label: Problem pages

Identity: `pilot/wiki/problems/plans-dont-adapt.md` and `pilot/wiki/problems/price-value-gap.md`; two instances under the same admission and consumer policy. Substrate: Markdown; form: natural-language statements, affected users, supporting/contradicting evidence and links, with status/severity/mention/date fields interpreted by the maintainer. No shipped parser applies these fields. Lineage: synthesized from interviews, analytics, digest and intel. Agent authors and can update freely; source thresholds guide status and measured impact is required for `addressed`. Query uses them for problem framing, lint for rising unresolved problems, and ingest for cumulative evidence. Closest supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback) are producer/consumer routes, not duplicate objects (SRC-1, both problem pages, schema).

The `mentions: 4` of the adaptivity page is not the raw digest's 14 mentions; the journal reports the page counter reaching four on digest ingestion. Do not interpret this metadata as 4 users or 14 independent source files. Meaning and supporting evidence persist together, but referent precision of the counter is not fully formalized.

> - Week-26 digest: "repetitive plans" was the top theme, 14 mentions; review quote: "Three months
>   in and it keeps giving me the same leg day."
>   (source: 2026-06-27_digest_support-reviews-week26.md)
> --- `pilot/wiki/problems/plans-dont-adapt.md`

#### MEM-OBJ-assumptions
Label: Assumption register

Identity: `pilot/wiki/assumptions.md`, A1–A4. Natural-language belief content, for/against evidence, status, history and source pointers in Markdown. Lineage: product explanations and solution expectations derived from the fictional sources. Agent proposes; PM admits status changes; unchanged-status evidence additions have the explicit free-write exception, with a conflicting blanket prohibition noted below. Initialization of new assumptions is not cleanly categorized by the detailed gate; journal reports PM approval for A1/A2 and a PM-approved decision alongside A3/A4 registration. Do not infer universal autonomous admission or universal per-entry approval.

Consumers: ingest checks every assumption, lint looks for counter-evidence, query uses the status and caveats. A1 keeps the reason for weakening; A2's correlational caveat reaches the PRD rollout section; A4's untested status reaches PRD risks. Thus the example preserves reasons, not only state labels. This object differs from supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), whose theory assessment concerns its update route, and [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback), its downstream consumer (SRC-1, register and PRD).

> - evidence against: none yet; no causal experiment run (see Q1)
> - history: 2026-06-25 untested → validated-correlational (per: cohort readout)
> --- `pilot/wiki/assumptions.md`

#### MEM-OBJ-decisions
Label: Decision pages

Identity: `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`. Markdown natural-language context, alternatives, evidence, rationale and observable reversal conditions; status/date/decider are descriptive metadata consumed under instructions. Lineage: leadership steer plus product evidence; PM approval precedes agent filing. No supplied object counterpart; closest supplied [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) reads its conditions, and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) admits new decisions.

Consumers: later "why" queries, deliverable drafting, ingest/lint reversal checks. Force: recorded organizational decision and constraints interpreted in synthesis; not an executable roadmap change. Old rationale must persist, including wrong turns. Withdrawal is supersession by a new decision plus old status and forward link, not deletion; these edits need approval. Pilot has an active decision, not a demonstrated supersession event. PRD copies its measurement threshold; later intel checks the early-AND-strong condition rather than automatically reopening (SRC-1, decision, schema, PRD, log).

> - GymJoy Coach ships early AND demonstrably strong, making fast-follow pointless and
>   differentiation-elsewhere (e.g. social) more attractive.
> --- `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`

#### MEM-OBJ-open-questions
Label: Open questions queue

Identity: `pilot/wiki/open-questions.md`, Q1–Q7 including answered Q4. Form/substrate: natural-language questions, origins, resolution-path tags, status and answer links in Markdown. Lineage: ingested evidence and lint findings; agent can write freely, PM triages actual research. Queue consumers are discovery-plan/interview-script queries and subsequent review, not an automatic research executor. Q5 retains the churned-user sampling gap; Q4 retains its answer pointer and Q6 continues monitoring. No queue-specific expiry is specified. Closest supplied [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) produces queue entries but is not the same object (SRC-1, queue and schema).

> - origin: lint 2026-07-01 — all evidence so far is from churned/complaining users; retention
>   drivers are unstudied (gap, not contradiction)
> - status: open — schedule 2–3 interviews with month-6+ monthly-plan users
> --- `pilot/wiki/open-questions.md`

#### MEM-OBJ-overview
Label: Living product overview

Identity: `pilot/wiki/overview.md`. Markdown natural-language synthesis of product state, strategy and blind spots, with source and page links. Lineage: derived evidence and maintained entities; agent refreshes freely when the picture changes. It is not a raw trace or authority to change a protected decision. Later relevant-page queries can consume the current synthesis; lint can compare it with other pages and data. It is editable rather than append-only; original raw evidence and decision rationale reside elsewhere. Closest supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) names its update, but no supplied object duplicates it (SRC-1, overview and schema).

> **Biggest known blind spot:** all evidence so far comes from churned or complaining users;
> retained users are unstudied (Q5).
> --- `pilot/wiki/overview.md`

#### MEM-OBJ-gymjoy
Label: GymJoy competitor page

Identity: `pilot/wiki/competitors/gymjoy.md`. Markdown natural-language snapshot, capability assessment, dated timeline and implications; `threat` is an agent-interpreted label, not a numerical embedding or executable rule. Derived from both intel files. PM-approved entity activation and schema change precede page creation in reported operation; subsequent intel updates are prescribed in the activated competitor spec, without a separate per-update human approval requirement. Query and review can select the page; linked implications feed problem framing, A4 and reversal monitoring. Closest supplied [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade) produces the entity but is not a duplicate object. Unlike [RT-OBJ-schema](runtime.md#rt-obj-schema), this is product content, not maintainer instructions (SRC-1, competitor page, `pilot/CLAUDE.md`, log).

> - Shipped shallow → differentiation window on real progression still open; bar for our v1
>   reception is *above* rest-days/swaps (feeds A4 in [assumptions](../assumptions.md) and the
>   [Q3 decision](../decisions/2026-06-30_q3-retention-focus.md) reversal condition 3; monitored
>   monthly via [Q6](../open-questions.md)).
> --- `pilot/wiki/competitors/gymjoy.md`

#### MEM-OBJ-prd
Label: Filed PRD exploration

Identity: `pilot/wiki/prd-adaptive-plans-v1.md`, draft-v0.1 exploration for Dana and Omar. Form/storage: natural-language generated deliverable with citation links and descriptive metadata in Markdown. Lineage: model synthesis of retained pages plus raw sources, not independent customer evidence or an agent session transcript. The journal reports in-message drafting first and later file-back on PM confirmation. Its claims inherit evidence rules; inferences remain marked. No later reader invocation or product execution is supplied. Future relevant queries are the afforded consumer; intended human audience is not observed consumption. Closest supplied [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback) already covers its admission/return, not its object identity (SRC-1, PRD, index and log).

> *Drafted by the wiki agent on PM request for Q3 kickoff; generated from wiki pages + raw
> sources. Every claim cited; inferences flagged. Filed back per the query workflow.*
> --- `pilot/wiki/prd-adaptive-plans-v1.md`

#### MEM-OBJ-index
Label: Page catalog

Identity: `pilot/index.md`. Markdown grouped titles, paths, one-line display summaries and updated dates. Access metadata is distinct from full page content: links provide addresses, while summaries such as "A1 weakening" are lossy natural-language displays. External tools may resolve literal paths, but the shipped selector is a model following an index-first instruction; no programmatic ranking or metadata filter is supplied. The agent updates the catalog on every write without per-entry PM approval. Later task/query context receives it first, then selected pages. Persistence spans future tasks if reloaded; no fixed token/page budget or access-based eviction is defined. Catalog omissions or misleading summaries can impair discovery even while files persist. Closest supplied [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback) uses this object; no supplied object counterpart (SRC-1, index and schema).

> `index.md`: every page, grouped by type — `- [title](path) — one-liner (updated YYYY-MM-DD)`.
> Update on every write.
> --- `template/SCHEMA.md`

#### MEM-OBJ-log
Label: Operation journal

Identity: `pilot/log.md`. Append-only Markdown summaries of ingest/query/lint/decision operations. Natural language plus date/operation prefixes intended for grep; not raw tool calls, model reasoning or authenticated approval events. The agent writes freely. It preserves skipped items, pending proposals, direct-approval reports and entity activation history. Intended PM review and later bookkeeping can read it, but query is not instructed to read the entire journal on every invocation. The pilot gives reported operation, not proof that described admissions actually occurred. Closest supplied [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) append to it; neither is this object (SRC-1, log and schema).

> - Tracking-sync bug noted, not filed (eng owns, fix week 28) — skip rule applied.
> --- `pilot/log.md`

### Routes

#### MEM-RTE-digest-admission
Label: Export to approved digest

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This distinct subroute covers admission of derived high-volume source material before ordinary wiki synthesis, not a replacement for the parent ingest route. Trigger: high-volume feedback/review/news stream. Endpoints: export → agent-authored digest → PM source approval → retained digest → ingest and later cited pages. Alternative: PM supplies the digest directly. Owner/decider/veto: PM; proposer and summarizer: external model; file I/O: host. PM initiation alone does not admit a model-drafted digest. Operating mode: open maintenance request; no expected-answer oracle or score-based comparison is supplied. Guidance is keep signal-rich themes rather than raw dumps. Rejection withholds source admission; no rejected-candidate archive or technical rollback is specified. Pilot digest attribution reports approval; original exports, transformation prompt and approval exchange are not supplied (SRC-1, schema and digest).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: draft digest for PM approval, or receipt of PM-provided digest; conversational wording is unspecified.
- Later read-back: approved Markdown digest becomes source evidence for problem/assumption updates and cited query output; later consumer sees themes/counts/quote rather than full exports.
- Delegated visibility: uninspected — external host context transfer is not specified; no shipped separate summarizer worker.
- Selection predicate: PM source curation plus model theme selection from the export; no explicit item-ranking algorithm, retention quota or token budget.
- Invalidation or expiry: source is subsequently read-only by policy; erroneous content can be challenged by later evidence/questions, but digest replacement or retraction procedure is unspecified.
- Activation or effect: prescribed source admission and subsequent knowledge synthesis; reported digest lineage does not establish accurate summarization or beneficial decisions.
- Evidence limits: fictional derived digest and doctrine; unavailable raw exports prevent reconstruction of omitted evidence or per-theme accuracy.

> High-volume streams (support tickets, reviews, competitor news): never ingest raw dumps; the PM
> provides a weekly digest file, or you draft one from an export and the PM approves it as a source.
> --- `template/SCHEMA.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-synthesis
Label: Retained product state to synthesis

Consumer: external agent answering a later PM query or planning discovery. Channel: index-selected Markdown pages, with raw-source reads as needed. Force: evidence, retained belief statuses, organizational decisions and resolution-path guidance interpreted by the model; not hard tool permissions or automatic product execution. Horizon: later operations and potentially sessions on the same product folder. Schema authority is distinct: [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent) governs *how* the agent operates; these objects supply *what* it knows and treats as decided or unresolved. Actual effect and improved capacity are unobserved. Source trust is PM curation and citation-chain policy, not validation of original truth. SRC-1, `template/SCHEMA.md`, queue, decision and PRD; closest supplied route [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback) delivers these materials but is not the authority-path record.

> Every contradiction, gap, or triggered reversal condition lands here. When the PM plans discovery,
> generate interview scripts / analysis plans FROM this queue.
> --- `template/SCHEMA.md`

## Annotations

#### On [RT-OBJ-schema](runtime.md#rt-obj-schema)

Retained instruction edits are distinct from product-content updates. Product context begins as human-supplied setup input; Stage-2 schema extension is agent-proposed and PM-admitted. The pilot retains both the activated competitor spec and a statement of its trigger/approval, while the log retains the operation history. Later maintainer tasks are meant to reload these instructions; no post-upgrade session demonstrates effect. Reasons for the entity addition are retained, not just an opaque version marker (SRC-1, `pilot/CLAUDE.md`, `pilot/log.md`).

> The schema below is copied from the template (v0.1) — this instance is at Stage 1, with one
> Stage-2 entity activated: `wiki/competitors/` (trigger fired on the 2nd competitor-intel ingest;
> PM approved 2026-07-03).
> --- `pilot/CLAUDE.md`

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Read-back changes meaning rather than merely accumulating raw records: source → derived problem/evidence, belief history, decision context, questions, overview → later query/review. Product-interaction traces can enter through a PM-approved digest, but the journal itself is not shown as an automatic input to a method-learning transformation. The known subsequent synthesis does not resolve the digest's missing item-level provenance. No automatic unsolicited memory push is specified. The skip branch leaves a journal trace without a new thematic page; pending protected updates remain proposals (SRC-1, schema, digest, log). Supporting passages and write exceptions are retained in the parent record and [MEM-RTE-digest-admission](#mem-rte-digest-admission).

#### On [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)

Selection input is the PM question and full catalog; selected retained parts are relevant pages, with optional raw-source support. Delivery is file content in the external task context, followed by model synthesis, not a search-service result with a fixed budget. File-back changes a conversational answer into durable Markdown and refreshes index/log. The pilot demonstrates a cataloged artifact and reports its generation, not a later invocation reading it. Supplied route passages and [MEM-OBJ-prd](#mem-obj-prd) support this chain. No source retention or host-conversation trimming is implied by the relevance rule (SRC-1, `template/SCHEMA.md`, `pilot/index.md`, `pilot/log.md`).

#### On [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)

The retained outputs are questions and proposed/approved belief edits, not a quality score or garbage-collected store. Review targets include dates, links, counter-evidence and decision conditions. A stale page remains reachable; an answered question retains the answer location. Q5 preserves the sampling gap and Q4/Q6 preserve transition from launch inquiry to ongoing monitoring. The queue is designated input to later discovery work, but no supplied execution shows that work being done (SRC-1, `template/SCHEMA.md`, `pilot/wiki/open-questions.md`; [MEM-OBJ-open-questions](#mem-obj-open-questions)).

#### On [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade)

Persistence splits into governing instructions and a new knowledge page; index metadata exposes the latter. The journal retains the trigger, pending relay and direct approval report. The added competitor spec says to link rather than duplicate details, yet the retained problem pages and overview still contain substantial intel detail. Thus activation of a spec is not evidence that all old content was normalized or that duplication was removed (SRC-1, `pilot/CLAUDE.md`, `pilot/wiki/problems/plans-dont-adapt.md`, `pilot/wiki/overview.md`, `pilot/log.md`).

> decisions, assumptions, questions). All claims source-cited. Problem/decision pages link here
> instead of duplicating intel details. Update on every `intel` ingest touching that competitor;
> staleness checked at lint.
> --- `pilot/CLAUDE.md`

## Write side

Acquisition has two admission mechanisms: PM selection of individual sources and PM provision/approval of a digest. Authorship and I/O remain separate: a model can draft a digest which a human admits and an external file tool persists. Subsequent wiki transformations are known even where original raw provenance is unavailable ([MEM-OBJ-sources](#mem-obj-sources), [MEM-RTE-digest-admission](#mem-rte-digest-admission)).

Ordinary source-driven problem, overview, question, catalog and journal edits are model-admitted under instructions. Belief-status changes, decisions, supersession and instruction edits are PM-admitted. The explicit unchanged-status evidence exception means the register is not uniformly human-gated; new-entry treatment and the blanket prohibition remain ambiguous. These are policy distinctions, not authenticated authorization. Reasons persist in evidence sections, histories, rationale and question origins, and some reach the PRD. No automatic rewriting of model weights is attributable to this repository ([MEM-OBJ-assumptions](#mem-obj-assumptions), [RT-CMP-llm-agent](runtime.md#rt-cmp-llm-agent)).

The digest path is the clearest automatic transformation of product-interaction records into behavior-shaping material: support/review exports → model digest → PM-approved source → updated problem/evidence pages → PRD. Its origin is customer/product traces, not the maintainer's action/outcome trace. No observed benefit or improved future capacity is established. Answer file-back is a separate conversation-derived transformation: generated answer → offered persistence → exploration page plus catalog entry. It retains reasoning and uncertainty, but no later consuming round is supplied. The operation journal records bookkeeping and approval reports; retaining it alone does not establish trace-driven methodological learning ([MEM-OBJ-digest](#mem-obj-digest), [MEM-OBJ-prd](#mem-obj-prd), [MEM-OBJ-log](#mem-obj-log)).

Cleanup is conservative. No-change inputs take a log-only branch. Contradictions become questions rather than silently deleted claims. Sources are read-only; decisions are superseded, not erased. Lint flags staleness (>30 days in active areas) without deleting content or expiring authority automatically. A triggered reversal proposes reconsideration; it does not itself reopen a decision. Unapproved protected changes stay pending. No transaction, conflict resolution or automatic rollback implementation is shipped; optional Git is user tooling ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [MEM-OBJ-decisions](#mem-obj-decisions)).

## Read-back

The later reader actively requests the query; the agent then uses the catalog to select pages and deliver retained content into the external model context. There is no independently triggered push selector. Topic/title summaries guide relevance, not an explicit identifier filter or embedding similarity score. No hard budget, top-k, exact token cap or truncation rule is prescribed. Raw sources remain reachable and the PRD reports reading them; derived material is not the sole accessible layer ([MEM-OBJ-index](#mem-obj-index), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)).

Ingest is also a later consumer: it is told to check every assumption and active decision conditions against new evidence. Lint selects retained claims, conditions, links and dates for review; discovery queries select resolution-path questions; schema reload supplies the changed maintainer rules. These differ from passive file availability. The PRD is a concrete retained downstream product of the example's wiki state, but evidence is reported operation rather than raw execution; later PRD consumption is not supplied ([MEM-BAP-wiki-synthesis](#mem-bap-wiki-synthesis), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent)).

Working-context control is limited to instruction loading and index-first relevance selection in the shipped material. There are no prescribed subagent frames or frame-return restrictions, no turn trimming, host summarization, checkpoint alternatives or reload-after-eviction protocol to characterize. Those host mechanisms remain uninspected, not established absent. File catalog addresses can lead to fresh reads, but are not live references whose presence retains other context; reading a file puts its contents into a host-managed window. Persistence outside that window is the folder's retention policy, not a defined liveness/garbage-collection rule (SRC-1, `README.md`, `template/SCHEMA.md`; [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)).

## Integration issues

1. **Gate ambiguity carried, not corrected away.** The detailed free-write clause permits unchanged-status assumption evidence additions; the final blanket prohibition is broader, and new-entry admission remains underspecified. Runtime already identifies this. It affects the per-write admission account, not the existence of retained beliefs. The pilot's conservative approval of A4 evidence is not a universal rule ([MEM-OBJ-assumptions](#mem-obj-assumptions), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `template/SCHEMA.md`, `pilot/log.md`).
2. **Instruction context can lag current evidence.** `pilot/CLAUDE.md` still calls GymJoy adaptivity a waitlist signal, while the competitor page, overview, questions and PRD know it shipped. A later task reading only startup context could receive stale product state. No precedence or automatic context refresh resolves this conflict. This limits claims that one current synthesis always reaches the model; it does not refute the query route's prescribed relevant-page reads ([RT-OBJ-schema](runtime.md#rt-obj-schema), [MEM-OBJ-gymjoy](#mem-obj-gymjoy), [MEM-OBJ-overview](#mem-obj-overview)).

> Main competitor: GymJoy (€5.99/mo, adaptivity signaled via 'Coach' waitlist).
> --- `pilot/CLAUDE.md`

3. **Normalization remains incomplete in the example.** Competitor spec requests links instead of repeated intel, but overview/problem pages retain details. Retention of derived copies creates multiple update surfaces; later lint is prescribed but not proof of synchronized updates. This qualifies stage-upgrade effects, not its reported admission ([RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade), [MEM-OBJ-problems](#mem-obj-problems), [MEM-OBJ-gymjoy](#mem-obj-gymjoy); SRC-1, `pilot/CLAUDE.md`, problem pages and overview).
4. **Counter semantics and original evidence remain local uncertainties.** `mentions` is not fully defined in terms of users/items/sources, and the digest lacks original exports. Do not use its 14 mentions or the problem's four as independently verified sample sizes or infer exhaustive transformation accuracy ([MEM-OBJ-problems](#mem-obj-problems), [MEM-OBJ-digest](#mem-obj-digest); SRC-1, digest, log and adaptivity page).
5. **Identity comparison.** New objects have no supplied object counterparts; supplied runtime routes already cover their producers/consumers and receive annotations instead of duplicate route declarations. The digest-admission route explicitly declares containment in the ingest route; the product-state authority path differs from the supplied schema authority path. No proposed supersession or correction to a supplied fact is required. Peer epistemic/workflow reports were not supplied, so possible peer duplicates cannot be settled here ([MEM-RTE-digest-admission](#mem-rte-digest-admission), [MEM-BAP-wiki-synthesis](#mem-bap-wiki-synthesis), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent)).

## Limitations and checks

The account establishes prescribed memory structure and read-back affordances with fictional reported examples. It does not establish actual agent compliance, authenticated PM decisions, accurate lossless digests, host context behavior, later activation of the filed PRD or schema upgrade, or beneficial outcomes. Missing provider and execution evidence does not negate the documented capacity to reuse maintained files. Sources and histories preserve reasons, but evidence-chain presence does not validate their truth or entail improved future capacity.

Source identity was rechecked by Git HEAD: 64fb748ac9d187be4c51636aa56bfee1d9e5b116; tracked paths match the frozen source. Method identity for this invocation is the supplied memory job, member type, worker rules, records contract and collection contract, read completely before source analysis. No target execution, tests, dependencies, external links or prior analyses were used. Deterministic validation: the required role-specific content and quotation check passed (exit 0); this establishes form and quote occurrence, not semantic acceptance or observed behavior.
