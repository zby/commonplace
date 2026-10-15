---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Engraph's truth-apt acquisition, identity extraction, structural checks and operational reliance at the frozen revision."
run-id: AAS-2026-10-14-engraph-0cd4f00695b0-01
reviewed-boundary: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
---

# Engraph epistemic report

## Source-and-claim boundary

Question: what does Engraph acquire, transform, check and license for later reliance when a vault becomes agent context? The whole-system scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identities and evidence layers are in its [Source register](boundary.md#source-register). Engraph is the vault service, not the external conversational agent. All source findings below use SRC-1, implementation unless identified as doctrine/design. No target, tests, models or examples were executed.

The public claims assessed are [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge), [EPI-CLM-search-confidence](#epi-clm-search-confidence), [EPI-CLM-health-diagnostics](#epi-clm-health-diagnostics), and [EPI-CLM-placement-learning](#epi-clm-placement-learning). The service's current-state presentation also matters: see [EPI-RTE-identity-extract](#epi-rte-identity-extract). These are not all claims that Engraph makes, nor a claim that it promises universally true answers.

Coverage distinguishes supplied runtime evidence from direct reads in this job. The runtime is a provisional baseline, not an inspection ceiling.

| Entry point / operation | SRC-1 path | Coverage and records | Limit / conclusion prevented |
| --- | --- | --- | --- |
| CLI index, search, serve, setup, identity, configure, graph, context, write, migrate, models, clear | `src/main.rs` | Direct dispatch/declaration searches and bounded reads of command enums, clear and context variants; supplied [RT-RTE-query-search](runtime.md#rt-rte-query-search), [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply), [RT-RTE-para-migration](runtime.md#rt-rte-para-migration) | Not every CLI formatting/configuration branch reread; no system-complete absence conclusion. |
| MCP tool registration, read/context/who/project, health, identity, mutation and maintenance | `src/serve.rs` | Direct registered-function search, health and identity handlers; supplied [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [RT-RTE-http-access](runtime.md#rt-rte-http-access); added [EPI-RTE-health-report](#epi-rte-health-report) | Handler wiring is not agent obedience or per-content human review. |
| HTTP discovery, search/context/health, identity, setup and mutators | `src/http.rs` | Direct endpoint/function search; supplied runtime adapter inspection; [RT-RTE-http-access](runtime.md#rt-rte-http-access) | No deployed grants, tunnel, client or endpoint runs. |
| Generated/cached/heuristic search orchestration, fusion and ranking | `src/search.rs`, `src/llm.rs`, `src/fusion.rs`, `src/store.rs` | Direct orchestration/parser/fallback, search consumers, fusion and cache-related searches; [EPI-RTE-orchestration-parse](#epi-rte-orchestration-parse), [EPI-RTE-confidence-normalize](#epi-rte-confidence-normalize) | Actual weights and model behavior unavailable; no relevance calibration or semantic preservation established. |
| Reads, section reads, list/map, person/project/topic bundles | `src/context.rs` | Direct person/project assembly and helper reads; supplied [RT-RTE-topic-context](runtime.md#rt-rte-topic-context) | Full read/section resolution and all graph internals not reread; completeness and real-world membership unestablished. |
| Note admission, metadata, links, placement, edits, move/archive/delete, cleanup | `src/writer.rs`, `src/links.rs`, `src/placement.rs` | Direct delete/archive/integrity cleanup, initial link index/protected-region code and placement rules/correction code; supplied [RT-RTE-note-admission](runtime.md#rt-rte-note-admission); added [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal) | Later auto-link application internals and all tag-resolution internals not inspected here; no blanket semantic-preservation finding. |
| Synchronization hooks, index replacement, centroid updates, identity refresh | `src/watcher.rs`, `src/indexer.rs`, `src/store.rs` | Direct startup/events/move-correction/identity-refresh/centroid and identity-store reads; [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [EPI-RTE-placement-correction](#epi-rte-placement-correction), [EPI-RTE-identity-extract](#epi-rte-identity-extract) | Event delivery, crash recovery and live freshness unobserved; ordinary changed-file indexing is not proof of L1 identity re-extraction. |
| Structural health evaluators | `src/health.rs` | Direct complete non-test implementation; [EPI-RTE-health-report](#epi-rte-health-report) | Stale-note evaluator is a stub; no semantic truth check follows from structural health. |
| Setup prompts and external-agent guidance | `README.md`, `skills/engraph/SKILL.md` | Direct selected public claims and ChatGPT instructions; supplied [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill) | Actual loading, adherence and downstream answer quality unobserved. |
| Product tests and release plane | `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `tests/` | Supplied [RT-RTE-product-release](runtime.md#rt-rte-product-release) and boundary coverage | No run results, interventions or independent component comparisons. Tests define checks rather than successful checking episodes. |
| Supporting profiles, tags, graph, temporal rules, tokenizer/chunker, optional Obsidian implementation | `src/profile.rs`, `src/tags.rs`, `src/graph.rs`, `src/temporal.rs`, `src/chunker.rs`, `src/obsidian.rs` | Supplied runtime findings where cited; supporting internals remain partly uninspected | Their possible additional material checks prevent a system-complete negative about all evaluation or criticism. |

Missing evidence has local consequences. Unknown user-vault provenance prevents endorsing imported premises. Uninspected model bytes/provider internals prevent claims about internal model knowledge, parameter learning or reliable judgment. No execution traces establish activation, successful retention/recovery, client use or benefit. No experiments identify retrieval improvements, placement improvements or component effects. Available but uninspected support modules are not source-access gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-vault-content](#epi-obj-vault-content) | see record | see record | SRC-1 `src/writer.rs` | Caller authority and premise truth unknown. |
| [EPI-OBJ-identity-facts](#epi-obj-identity-facts) | see record | see record | SRC-1 `src/identity.rs` | Extraction labels can exceed premises; some source paths discarded. |
| [EPI-OBJ-health-report](#epi-obj-health-report) | see record | see record | SRC-1 `src/health.rs` | Structural propositions only; stale empty list is not a check result. |
| [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) | Intent/date fields can assert properties of a query; expansion strings are retrieval instructions, not necessarily propositions | see record | SRC-1 `src/store.rs` | Semantic preservation and warrant unknown. |
| [RT-OBJ-search-config](runtime.md#rt-obj-search-config) | None required: current-call retrieval policy | see record | SRC-1 `src/search.rs` | Policy effect is separate from epistemic endorsement. |
| [RT-CMP-llama-embed](runtime.md#rt-cmp-llama-embed) | Not determinable for inaccessible weight content; vectors are numerical selectors, not independently warranted claims | see record | SRC-1 `src/llm.rs` | Actual distributed-parametric provenance unknown. |
| [RT-CMP-llama-orchestrator](runtime.md#rt-cmp-llama-orchestrator) | Generated intent/date interpretation; truth-apt content in weights not determinable | see record | SRC-1 `src/llm.rs` | Syntax check does not test interpretation. |
| [RT-CMP-llama-rerank](runtime.md#rt-cmp-llama-rerank) | Query–snippet relevance judgment, not snippet truth; weight content not determinable | see record | SRC-1 `src/llm.rs` | No reference-answer or calibration evidence. |

Folder centroids, proposed placements and correction metadata have their own operational consumer, assessed in [EPI-RTE-placement-correction](#epi-rte-placement-correction). This does not treat every number, path or transport object as a truth claim.

## Authority-route ledger

The ledger is a sparse overlay. Fields owned by declaring records say **see**; each row's architectural status, content relation and epistemic assessment are local findings. No observed route operation is inferred from `implemented`. A result consumed for retrieval is operational reliance, not necessarily acceptance of a claim for knowledge use.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | content transformation | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | External text acquired, source warrant unknown; adapter label not author proof | see route | see route | SRC-1 `src/writer.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | Writer's additional linking/tag/placement changes are not automatically faithful import. |
| [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | disposition/acceptance | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | no content change | see route | see route | see route | see route | see route | Operational write admission; not evidence-consuming acceptance of note truth | see route | see route | SRC-1 `src/writer.rs` | none | none | I/O, permission, collision and mtime criteria concern mutation, not claim warrant. |
| [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | retention | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | no content change | see route | see route | see route | see route | see route | Retention before epistemic acceptance; no lifecycle integration inferred | see route | see route | SRC-1 `src/writer.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | DB/disk disagreement and alternate write-path limits remain as in runtime. |
| [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh) | content transformation | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | Chunk/index representation enables locating text, not endorsing it | see route | see route | SRC-1 `src/indexer.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | Applies to text chunking/indexing; inferred mention/graph associations need separate interpretation. |
| [EPI-RTE-orchestration-parse](#epi-rte-orchestration-parse) | check/evidence production | implemented | [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) | no content change | see route | see route | see route | see route | see route | License only for accepted parser shape, not faithful query meaning | see route | see route | SRC-1 `src/llm.rs` | none | none | Empty/missing expansions rejected; string content can still be irrelevant. |
| [EPI-RTE-orchestration-parse](#epi-rte-orchestration-parse) | disposition/acceptance | implemented | [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) | no content change | see route | see route | see route | see route | see route | Operational admission or heuristic substitution; not semantic acceptance | see route | see route | SRC-1 `src/search.rs` | none | none | Cache deserialization takes a different path from generated-text parser. |
| [RT-RTE-query-search](runtime.md#rt-rte-query-search) | content transformation | implemented | [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Generated interpretation/expansion is not established as entailed or as reliably preserving scope | see route | see route | SRC-1 `src/llm.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | No output instances; prompt intent alone does not demonstrate conjecture or faithful reshaping. |
| [RT-RTE-query-search](runtime.md#rt-rte-query-search) | check/evidence production | implemented | [RT-CMP-llama-rerank](runtime.md#rt-cmp-llama-rerank) | no content change | see route | see route | see route | see route | see route | Scores judge relevance of query–snippet pairs, not factual truth of notes | see route | see route | SRC-1 `src/search.rs` | [EPI-CLM-search-confidence](#epi-clm-search-confidence) | none | Limited candidate set and snippet, no answer oracle or observed reliability. |
| [EPI-RTE-confidence-normalize](#epi-rte-confidence-normalize) | content transformation | implemented | [RT-OBJ-search-config](runtime.md#rt-obj-search-config) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Exact relative-score arithmetic within supplied lane rankings; not truth probability | see route | see route | SRC-1 `src/fusion.rs` | [EPI-CLM-search-confidence](#epi-clm-search-confidence) | none | Arithmetic inputs need not be warranted measurements of relevance. |
| [RT-RTE-query-search](runtime.md#rt-rte-query-search) | operational admission/selection/consumption | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | no content change | see route | see route | see route | see route | see route | Rank permits delivery only; high rank grants no factual endorsement | see route | see route | SRC-1 `src/search.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | Client's further reliance remains external and unobserved. |
| [RT-RTE-topic-context](runtime.md#rt-rte-topic-context) | content transformation | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | Selected/truncated disk text delivered; omitted qualifications can degrade warrant | see route | see route | SRC-1 `src/context.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | none | Selection from index and body from disk may have different freshness. |
| [EPI-RTE-identity-extract](#epi-rte-identity-extract) | content transformation | implemented | [EPI-OBJ-identity-facts](#epi-obj-identity-facts) | truth-apt transformation: ampliative conjecture | see route | see route | see route | see route | see route | OOO association and activity/importance labels exceed guaranteed premises | see route | see route | SRC-1 `src/identity.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | scope promotion | Deterministic counterexample in record; current-focus/blocked copying is separately context-lossy, not all extraction ampliative. |
| [EPI-RTE-identity-extract](#epi-rte-identity-extract) | retention | implemented | [EPI-OBJ-identity-facts](#epi-obj-identity-facts) | no content change | see route | see route | see route | see route | see route | Heuristic candidates retained as facts before a truth check | see route | see route | SRC-1 `src/store.rs` | none | none | Clearing old L1 rows is regeneration, not content-directed criticism. |
| [EPI-RTE-identity-extract](#epi-rte-identity-extract) | operational admission/selection/consumption | implemented | [EPI-OBJ-identity-facts](#epi-obj-identity-facts) | no content change | see route | see route | see route | see route | see route | Current-state presentation licenses no stronger conclusion than extraction supports | see route | see route | SRC-1 `src/identity.rs` | [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | scope promotion | Output drops source fields; client adherence and factual validity unobserved. |
| [EPI-RTE-health-report](#epi-rte-health-report) | check/evidence production | implemented | [EPI-OBJ-health-report](#epi-obj-health-report) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Bounded structural findings from indexed data/rules, not external-world truth | see route | see route | SRC-1 `src/health.rs` | [EPI-CLM-health-diagnostics](#epi-clm-health-diagnostics) | stale stub | Broken-link/orphan findings are relative to index scope; stale empty list has no derivation from age evidence. |
| [EPI-RTE-health-report](#epi-rte-health-report) | operational admission/selection/consumption | implemented | [EPI-OBJ-health-report](#epi-obj-health-report) | no content change | see route | see route | see route | see route | see route | Advisory report; no implemented semantic acceptance/rejection follows | see route | see route | SRC-1 `src/serve.rs` | [EPI-CLM-health-diagnostics](#epi-clm-health-diagnostics) | stale stub | No inspected automatic repair consumer; external action unknown. |
| [EPI-RTE-placement-correction](#epi-rte-placement-correction) | behavior/policy adaptation | implemented | see route | non-truth-apt policy/content update: folder centroids and placement metadata | see route | see route | see route | see route | see route | Moved destination treated as feedback, not a warranted proposition about optimal organization | see route | see route | SRC-1 `src/watcher.rs` | [EPI-CLM-placement-learning](#epi-clm-placement-learning) | attribution limit | Durable selector adaptation exists; improved future capacity and human intent not demonstrated. |
| [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-vault-content](#epi-obj-vault-content) | no content change | see route | see route | see route | see route | see route | Operational withdrawal on caller request or missing path, not falsification of note claims | see route | see route | SRC-1 `src/writer.rs` | none | none | Archive/delete/recovery vary; withdrawal is not universally permanent invisibility. |
| [RT-RTE-para-migration](runtime.md#rt-rte-para-migration) | operational admission/selection/consumption | implemented | see route | non-truth-apt policy/content update: proposed and applied file locations | see route | see route | see route | see route | see route | Confidence licenses moves, not proof of category truth or human review | see route | see route | SRC-1 `src/migrate.rs` | none | none | Preview application and best-effort undo remain distinct from epistemic acceptance. |
| [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply) | retention | implemented | see route | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | Supplied identity acquired with unknown warrant; detected profile drives operation | see route | see route | SRC-1 `src/onboarding.rs` | none | none | Writes can precede errors; generic caller is not authenticated human approval. |
| [RT-RTE-product-release](runtime.md#rt-rte-product-release) | check/evidence production | implemented | see route | no content change | see route | see route | see route | see route | see route | Declared format/lint/tests assess product under fixed checks, not vault truth | see route | see route | SRC-1 `.github/workflows/ci.yml` | none | none | No outcomes, enforced CI gate or improvement experiment supplied. |

No lifecycle integration after an evidence-consuming acceptance decision is established by these inspected routes. This is a bounded finding, not an assertion that an external client cannot review and accept a note. Person/project bundling is also operational: see [EPI-OBJ-vault-content](#epi-obj-vault-content); filename/folder/edge selection does not prove person identity, project membership, team membership or present task activity.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-vault-knowledge](#epi-clm-vault-knowledge) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [RT-RTE-query-search](runtime.md#rt-rte-query-search), [RT-RTE-topic-context](runtime.md#rt-rte-topic-context), [EPI-RTE-identity-extract](#epi-rte-identity-extract) | None supplied | No answer-quality comparison; index relations and extracted state have bounded meanings | Queryable retained vault context is wired | Calling it knowledge is not evidence that content was checked/accepted as true. No universal truth promise attributed. |
| [EPI-CLM-search-confidence](#epi-clm-search-confidence) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-confidence-normalize](#epi-rte-confidence-normalize), [RT-RTE-query-search](runtime.md#rt-rte-query-search) | None supplied | No calibration or relevance/answer improvement measurement | A normalized ranking percentage exists and can guide selection | Higher relative fusion score, not probability of truth or calibrated certainty. |
| [EPI-CLM-health-diagnostics](#epi-clm-health-diagnostics) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-health-report](#epi-rte-health-report) | None supplied | Indexed structure and hard-coded tag rule; no stale-age check | Orphan/broken-link/tag/inbox/index-age report wired to MCP/HTTP | Stale content detection unsupported by stub; advertised CLI `context health` absent from inspected ContextAction variants. |
| [EPI-CLM-placement-learning](#epi-clm-placement-learning) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-placement-correction](#epi-rte-placement-correction) | None supplied | No correct-placement oracle, before/after outcomes or independently varied components | Move-derived centroid adaptation can alter later placement | Improved capacity not established; only listed adapter labels qualify, not all writes/users/moves. |

Runtime's separate [RT-CLM-server-readonly](runtime.md#rt-clm-server-readonly) and [RT-CLM-write-consistency](runtime.md#rt-clm-write-consistency) already bound mutation and persistence authority. This member does not redefine those claims: read-only is not a semantic acceptance criterion; reconciliation is not confirmation of the truth or authorship of recovered content.

## Bounded conclusion

Engraph acquires caller- and filesystem-supplied Markdown, retains it, reshapes it into searchable text/numerical/graph structures, selects it and returns it to clients. Source truth is unknown. Paths and IDs preserve locatability, but snippet/budget selection can discard qualifications, and retained adapter labels do not authenticate origins. These conclusions concern [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [RT-RTE-query-search](runtime.md#rt-rte-query-search), and [RT-RTE-topic-context](runtime.md#rt-rte-topic-context), not successful downstream answering.

There are real bounded evaluators. The orchestration parser checks usable output shape and triggers heuristic replacement; the reranker evaluates query–snippet relevance; structural health evaluates index-relative links, isolation and tag conventions; fusion derives a relative percentage by explicit arithmetic. Their targets differ, and none licenses note truth. The health stale-list stub and normalized top-result confidence are concrete counterexamples to stronger readings of diagnostics or certainty. See [EPI-RTE-orchestration-parse](#epi-rte-orchestration-parse), [EPI-RTE-health-report](#epi-rte-health-report), and [EPI-RTE-confidence-normalize](#epi-rte-confidence-normalize).

Identity extraction is not merely retrieval. It promotes tags, edge prominence and keyword co-occurrence into active-project, key-person and OOO labels, then stores and formats them as current state. A source-level counterexample establishes a non-entailed OOO association. Other bullet extractions copy text while dropping checkbox/context/source distinctions. Retention and current-state delivery occur without a found evidence-consuming truth acceptance step in that inspected route; no warranted accepted ampliative claim is established. See [EPI-RTE-identity-extract](#epi-rte-identity-extract).

Caller write/apply/delete permissions and filesystem freshness/collision predicates license operations for defined paths; they do not license factual belief. Health delivery is advisory, retrieval scores rank, identity text advises the external agent, and writer/indexer mutations enforce changes to durable data. Archive/delete and missing-path cleanup withdraw operational access but do not refute claims. There is no evidence that these routes integrate claims *after* epistemic acceptance. See [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal) and the runtime admission records.

Placement correction supplies a separate automatic behavior-adaptation route: detected moved-note feedback adjusts durable centroids consumed by later semantic placement. Fixed inference parameters therefore do not imply absence of all use-derived adaptation. However, improvement of future action is unestablished without outcome/comparison evidence, and event-derived feedback is not necessarily human approval. The inspected route does not formulate content-directed criticism with blame and retain it for theory revision. External user theories may reside in notes, but their existence and delivery do not establish an internal theory-building loop. Model internals remain opaque rather than proven to lack such processing. Learning benefit, reflection, autonomous theory building and successful self-improvement receive no bundled verdict. See [EPI-RTE-placement-correction](#epi-rte-placement-correction) and the independently bounded model component records.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-vault-content
Label: Vault content

Caller text and filesystem Markdown are natural-language material on disk. Tags, frontmatter, paths, IDs, chunk headings and graph relationships have symbolic consumers; embeddings have distributed-parametric numerical consumers. Candidate truth-apt content is whatever assertions the notes contain over their own subject scopes, not every path/tag. Claimed role: retained searchable agent context. SRC-1 `src/writer.rs`, `src/indexer.rs`, `src/context.rs`; acquisition/admission/retention are supplied by [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh). No supplied operative-object record names the vault itself; [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) is distinct query-policy JSON, not note content.

Later search returns snippets with references; topic context rereads selected disk bodies. Person context assembles mention/wikilink relations; project context includes same-folder and incoming-link notes, open-checkbox tasks and people-path links. These are source-native associations, not evidence that every child belongs to a project or every people link identifies a team member. SRC-1 `src/context.rs`:

> // Files in same folder
> if let Some(folder) = &project_folder {
>     let folder_files = params.store.list_files(Some(folder), &[], None, 50)?;
> --- `src/context.rs`

> if trimmed.starts_with("- [ ] ") {
> --- `src/context.rs`

Source warrant: unknown on import; transformed selection can degrade scope by omission. Authorship and human approval cannot be inferred from `created_by`; see supplied admission record. No observed vault instance was supplied.

#### EPI-OBJ-identity-facts
Label: identity_facts

Symbolic SQLite rows carry tier/key/value/source/updated_at. Natural-language values become claims through formatter labels and client interpretation. Candidate content: active projects, key people, current focus, blocking and OOO, plus separately acquired L0 name/role/purpose in config. Claimed role: compact identity/current context. Distinct from [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache); produced within [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply) and index refresh but neither supplied record individually contains the whole object's lifecycle. SRC-1 `src/store.rs`, `src/identity.rs`:

> "INSERT INTO identity_facts (tier, key, value, source, updated_at)
>              VALUES (?1, ?2, ?3, ?4, datetime('now'))
>              ON CONFLICT(tier, key, value) DO UPDATE SET
>                source = excluded.source,
>                updated_at = datetime('now')",
> --- `src/store.rs`

OOO/focus/blocking upserts omit source paths; formatted text omits source fields even where retained. Stored update time is extraction time, not proof the represented state remains current.

#### EPI-OBJ-health-report
Label: HealthReport

Current-call symbolic Rust/JSON report: orphans, unresolved links, stale_notes, inbox_pending, tag_issues, index age and count. Truth-apt candidates are index-relative structural propositions, such as a stored unresolved target or a work-path note lacking `work`. Claimed role: vault diagnostics, not note-truth endorsement. No supplied object counterpart; adjacent [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh) produces inputs, not this report. SRC-1 `src/health.rs`:

> pub struct HealthReport {
>     pub orphans: Vec<String>,
>     pub broken_links: Vec<BrokenLink>,
>     pub stale_notes: Vec<String>,
> --- `src/health.rs`

No evidence that an empty `stale_notes` result represents an evaluated absence of stale content.

### Routes

#### EPI-RTE-orchestration-parse
Label: Orchestration parsing
Part of: [RT-RTE-query-search](runtime.md#rt-rte-query-search)

Material parser/admission part, not a replacement for the full retrieval route. Endpoints: generated text → extracted JSON → intent/string expansions/date interpretation → usable result or fallback; cached structured JSON instead goes through serde deserialization in search. Code owns parsing/progression; model proposes strings, code can veto malformed output, external client supplies query and can decline invocation. Open requests, no improvement trigger or reference-answer oracle. SRC-1 `src/llm.rs`, `src/search.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: OrchestrationResult or parse error; concrete orchestrator substitutes heuristic result on parse/generation failure.
- Later read-back: Accepted result can be cached under query hash and reused by later searches; no model/age check in supplied cache record.
- Delegated visibility: External caller sees selected search results, not necessarily the accepted expansions or parse/fallback history.
- Selection predicate: Extractable JSON object and nonempty vector of string expansions; unknown intent defaults to exploratory; dates can override intent.
- Invalidation or expiry: Cache replacement on same query; getter does not expire by age/model; CLI clear removes database as a separate operation.
- Activation or effect: Parsing result gates generated-policy use; code consumes expansions/intent/date in retrieval. Shape acceptance changes search, not warrant of the interpretation.
- Evidence limits: No actual generated outputs or runs; cache serde branch is not equivalent to generated parser checks.

Target/domain: usable orchestration JSON, not semantic equivalence to the user's query. Disposition is operative because parse failure produces heuristic replacement. No semantic acceptance criterion, rollback of incorrect meaning or original-query inclusion check was found in this parser.

> if expansions.is_empty() {
>         anyhow::bail!("no expansions in orchestration response");
>     }
> --- `src/llm.rs`

> serde_json::from_str(&cached_json).unwrap_or_else(|_| {
>                     orch.orchestrate(query)
>                         .unwrap_or_else(|_| llm::heuristic_orchestrate(query))
>                 })
> --- `src/search.rs`

A concrete deterministic contrast: generated JSON with `"expansions":["unrelated"]` and an unknown intent passes the shown shape criterion with exploratory intent. This proves permissive content admission, not that a model actually produced that input.

#### EPI-RTE-confidence-normalize
Label: Confidence normalization
Part of: [RT-RTE-query-search](runtime.md#rt-rte-query-search)

Material numerical derivation part of retrieval. Endpoints: ranked lanes/weights → RRF sums → relative maximum normalization → returned confidence field. Symbolic code owns calculation and top_n consumer; local models supply some ranks but no answer oracle. Open retrieval, no improvement experiment. SRC-1 `src/fusion.rs`, `src/search.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: FusedResult including rrf_score and confidence.
- Later read-back: inapplicable — normalized score is current-call output, not use-derived retained state in this function.
- Delegated visibility: CLI/MCP/HTTP search callers receive confidence; lane explanation is not universally returned.
- Selection predicate: Weighted reciprocal rank summed by path; maximum score after sorting supplies denominator; top_n selects delivered rows.
- Invalidation or expiry: inapplicable — no durable score in this function; next search recomputes against current lanes.
- Activation or effect: Fusion orders results and normalization changes their displayed percentage; public instructions suggest preferring higher confidence.
- Evidence limits: No calibration, measured relevance, factual correctness or executed arithmetic; deduction is from inspected implementation.

Target/domain: relative rank-fusion magnitude among this call's candidates. With a single positive-weight lane containing one file, rank 1 and k=60 give score weight/61 and normalization gives exactly 100 percent, regardless of factual accuracy or absolute relevance. This checked algebra establishes an entailed numerical result, not a newly warranted world claim. SRC-1 `src/fusion.rs`:

> let contribution = weight / (k as f64 + rank as f64);
> --- `src/fusion.rs`

> let max_score = results.first().map(|r| r.rrf_score).unwrap_or(1.0);
>     for r in &mut results {
>         r.confidence = if max_score > 0.0 {
>             (r.rrf_score / max_score) * 100.0
>         } else {
>             0.0
>         };
>     }
> --- `src/fusion.rs`

#### EPI-RTE-identity-extract
Label: Identity extraction

Distinct multi-entry extraction/retention/formatter route overlaps [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh) and [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply), with no single supplied record containing all entries and consumers. Endpoints: indexed vault/profile → clear tier-1 rows → heuristic category extraction/upserts → subsequent identity formatting/API return. CLI refresh and full shared indexing are triggers; the MCP identity handler reads existing facts. Code owns extraction and storage; callers supply vault/configuration, not per-fact approval. Open synchronization/setup, no reference-answer oracle or improvement experiment. SRC-1 `src/identity.rs`, `src/store.rs`, `src/indexer.rs`, `src/serve.rs`, `src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: L1Summary from extraction; later identity requests return formatted L0/L1 text or structured CLI JSON.
- Later read-back: identity_facts persist in SQLite; formatter reads them on subsequent requests, config supplies separately retained L0 fields.
- Delegated visibility: Formatted block groups values under Current State labels without source paths; external agent receives that text, not proof of extraction correctness.
- Selection predicate: Project tags excluding template/archive components; top-five incoming-edge-ranked people; latest dated daily priorities bullets; last-seven daily-note OOO/person substring co-occurrence; last-three blocking keyword bullets.
- Invalidation or expiry: Extraction clears all tier-1 facts before repopulation; no independent truth/age expiry. Errors after clear can leave partial replacement; normal per-file watcher refresh is not shown to regenerate facts.
- Activation or effect: Code persists candidates and formats Active projects/Key people/Current focus/Blocking/OOO for clients; actual client reliance unobserved.
- Evidence limits: No user-vault run or checked fact; categories have heuristic rather than evidence-consuming semantic admission.

Admission: code applies extraction rules with no separate acceptance check against truth, intended reliance scope or reference outcome. Caller can change source files/config or request refresh; no saved previous L1 set is restored by this procedure. Static rules guide the proposal and persist in code; extracted values persist in SQLite. The record's claims are about this exposed route, not model internals.

Concrete source-level counterexample: let a configured people folder contain Alice.md and Bob.md, and a considered daily snippet be `- Alice is in office.\n- Bob is on vacation.` The OOO regex matches `vacation`; both person names occur in the whole snippet. For Alice, `extract_ooo_detail` returns the first OOO-matching line, `Bob is on vacation.`, and upsert retains `Alice (Bob is on vacation.)` under OOO. The premise explicitly puts Alice in office, so associating her with OOO is not entailed. The implementation can create an ampliative/misassociated current-state candidate without target execution. SRC-1 `src/identity.rs`:

> if chunk
>                                     .snippet
>                                     .to_ascii_lowercase()
>                                     .contains(&person.to_ascii_lowercase())
>                                 {
>                                     // Extract context around the match.
>                                     let detail = extract_ooo_detail(&chunk.snippet, &ooo_re);
>                                     let label = format!("{} ({})", person, detail);
>                                     store.upsert_identity_fact(1, "ooo", &label, None)?;
> --- `src/identity.rs`

> if ooo_re.is_match(trimmed) {
>             // Return the line content (stripped of bullet prefix) as the detail.
> --- `src/identity.rs`

Activity and importance are also inferred rather than checked: a `project` tag admits an Active projects label; edge counts select Key people. These labels exceed the guaranteed propositions “has project tag” and “among top five incoming-edge counts.” Copying focus/blocking bullets is a different relation: code removes checkbox markers, loses daily source pointers and caps focus items. For example a priorities bullet `- [x] Ship release` becomes `Ship release` under Current focus, losing completion information. This is context-lossy reshaping; it need not invent a new sentence to weaken warrant.

> let rest = rest
>                 .strip_prefix("[ ] ")
>                 .or_else(|| rest.strip_prefix("[x] "))
>                 .or_else(|| rest.strip_prefix("[X] "))
>                 .unwrap_or(rest);
>             let clean = rest.trim().to_string();
> --- `src/identity.rs:267-291`

> out.push_str(&format!("OOO: {}\n", ooo_vals.join(", ")));
> --- `src/identity.rs`

The source-level transformation establishes a possible candidate, not an observed accepted claim. Clearing/repopulating rows is not evidence of content-directed criticism or acceptance. Updated_at records extraction recency, not state truth.

#### EPI-RTE-health-report
Label: Health reporting

Distinct diagnostic route, absent from the supplied runtime route inventory; adjacent [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh) supplies its data. Endpoints: authenticated HTTP or MCP health request → indexed structural queries and fixed tag rules → serialized HealthReport. Rust code owns progression; caller requests assessment, no model or human decides findings. Open diagnostic requests, no improvement trigger or answer oracle. SRC-1 `src/health.rs`, `src/serve.rs`, `src/http.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lists of isolated indexed paths, indexed unresolved links, inbox files, work-path tag issues, index age and total count; stale_notes always empty in inspected stub.
- Later read-back: inapplicable — health results are current-call outputs; their underlying retained index is supplied by a separate route.
- Delegated visibility: MCP/HTTP client sees the serialized report, not an enforced repair or truth decision.
- Selection predicate: No edges after configured daily/inbox exclusions; unresolved_links rows; inbox prefix; Work-path notes without exact work tag; maximum parsed indexed_at for age.
- Invalidation or expiry: inapplicable — report is regenerated per request; stale source index can still affect its input facts.
- Activation or effect: Report delivery is wired, advisory to the caller; no automatic rejection/revision consumer is implemented in the inspected health module/handlers.
- Evidence limits: No health run; computed results are index-relative and path conventions are not semantic note classification.

Evaluator targets/domains: orphan means no stored edges outside chosen exclusions; broken link means unresolved indexed wikilink; tag issue means a particular path/tag predicate. Those are bounded structural criteria. Their successful computation would not endorse note claims. The stale-note slot lacks an evaluator, and index age is time since most recent indexed file, not a completeness/freshness certificate.

> pub fn find_stale_notes(_store: &Store, _days: u32) -> Result<Vec<String>> {
>     Ok(Vec::new())
> }
> --- `src/health.rs`

> .filter(|f| f.path.contains("Work/") || f.path.contains("01-Projects/Work/"))
>         .filter(|f| !f.tags.iter().any(|t| t == "work"))
> --- `src/health.rs`

The stale empty list therefore licenses no inference that all content is current. The advertised CLI `engraph context health` has no matching variant in inspected `ContextAction`; MCP/HTTP health is a positive alternate witness, so the finding is not “health absent.”

#### EPI-RTE-placement-correction
Label: Placement correction

Distinct automatic feedback route overlapping [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), not a duplicate of initial placement/admission. Endpoints: watcher matched move → created_by/suggested_folder comparison → mean-vector centroid addition/subtraction and correction log → metadata stripping → later semantic placement. Distributed-parametric folder centroids persist as SQLite vector blobs; symbolic correction rows and suggested_folder metadata are separate parts. Code owns adaptation; external editor produces movement, but neither human identity nor intended evaluation is authenticated. SRC-1 `src/watcher.rs`, `src/placement.rs`, `src/store.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Watcher logs/continues; adjustment/log/strip failures can warn; no reference-answer judgment returned.
- Later read-back: Updated folder centroids are read by try_semantic_placement for future writes; correction logs persist but inspected selector consumes centroids, not a learned prose explanation.
- Delegated visibility: Later caller sees chosen placement/confidence; not every detected move or failed centroid update is delivered.
- Selection predicate: Detected move paired by content hash; known created_by label and nonmatching suggested/actual folders; available stored chunk vectors for centroid adjustment; future semantic similarity above 0.65 admits centroid placement unless type rules/explicit folder preempt it.
- Invalidation or expiry: Batch indexing overwrites only centroid rows for first-path-component groups represented by chunk vectors from indexed_rel_paths; unchanged files can contribute nothing in an incremental run. It does not clear all centroid rows, so nested parent-folder rows written by feedback can survive even a rebuild. Subsequent additions/removals/corrections alter affected rows; stripping removes suggested_folder/confidence from a recognized move's note. Errors can leave partial updates; no global feedback reset or coherent full-vault centroid recovery is established.
- Activation or effect: Code boosts actual and decays suggested centroid; later placement consumer is wired to changed state. No exercised placement improvement observed.
- Evidence limits: Supported adapter labels exclude http-api; file move is proxy feedback, not an authenticated approval or a truth check. Vector granularity/count consistency and benefit are unestablished.

Trigger/proposal/admission: movement plus metadata produces a software correction; code gates by label and comparison, not independently checked correctness. Users can refrain from moving, change metadata or override folders, but the route has no per-correction approval request. Guidance persists as static detection/placement rules; numeric centroids and symbolic log persist. Recovery is best effort: errors warn, and later indexing may overwrite touched first-component rows, but neither global feedback invalidation nor a saved centroid transaction rollback is established. Operating mode: open watcher feedback, no controlled improvement experiment or answer oracle. SRC-1 `src/indexer.rs`, `src/store.rs`, `src/watcher.rs` support this bounded recovery account; see also the supplied peer evidence in [MEM-OBJ-folder-centroids](memory.md#mem-obj-folder-centroids) and [MEM-RTE-placement-feedback](memory.md#mem-rte-placement-feedback).

The batch indexer averages chunk vectors only for files indexed in that invocation, grouped by first path component. Feedback instead uses the moved note's mean vector and actual parent-folder key, while adjustment treats the stored count as file-vector count. These different keys and units prevent a uniform full-vault centroid invariant. The inspected rebuild branch clears vectors, not all centroid rows; its later centroid loop only upserts represented groups.

> for rel_path in &indexed_rel_paths {
>         let folder = rel_path.split('/').next().unwrap_or("(root)").to_string();
> --- `src/indexer.rs`

> store.upsert_folder_centroid(folder, &centroid, vectors.len())?;
> --- `src/indexer.rs`

> let actual_folder = std::path::Path::new(&new_rel)
>                                         .parent()
>                                         .map(|p| p.to_string_lossy().to_string())
>                                         .unwrap_or_default();
> --- `src/watcher.rs`

> const ENGRAPH_AGENTS: &[&str] = &["claude-code", "cli", "mcp-server"];
> --- `src/placement.rs`

> // Adjust centroids: boost actual, decay suggested
> --- `src/watcher.rs`

> .map(|(o, v)| (o * nf + v) / new_n as f32)
> --- `src/store.rs`

> if best_sim > 0.65 {
> --- `src/placement.rs`

This is durable behavior-shaping adaptation without a truth-apt policy proposition. Centroid inference is not online updating of loaded model parameters. Formulated criticism with challenged claim/result/blame and retained theory revision is not established by the move-score mechanism. Improvement of future action is unestablished, independently of persistence and automatic updating. It therefore supports an adaptation mechanism, not demonstrated learning benefit or successful self-improvement.

#### EPI-RTE-content-withdrawal
Label: Content withdrawal

Distinct withdrawal/recovery functions spanning supplied [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh). Endpoints: caller archive/soft-delete/hard-delete or missing-file integrity cleanup → filesystem/index removal or movement → future selection changes. Code owns I/O; caller requests withdrawal, filesystem absence triggers orphan cleanup. SRC-1 `src/writer.rs`, `src/main.rs`; startup invocation is supplied by runtime.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Write metadata or success/error/count depending on operation; CLI clear reports removal of database or entire data directory.
- Later read-back: Archive disk copies remain; unarchive is a separate recovery request; deleted retrieval entries no longer supply the removed path until content is reintroduced/indexed. Soft delete inserts an archive file record rather than behaving identically to archive_note.
- Delegated visibility: Caller sees status/metadata, not proof every other client's copied context was withdrawn; prior tool returns remain external.
- Selection predicate: Explicit resolved file/mode for note withdrawal; path.exists false for integrity cleanup; all flag determines CLI clear scope.
- Invalidation or expiry: Reindex/reintroduction or unarchive can restore availability; hard deletion/CLI clear have no previous-body rollback in inspected procedures.
- Activation or effect: Archive removes old vectors/FTS/edges/file record and original file; hard deletion removes disk file then purges Store; integrity cleanup removes missing-path derived entries; clear deletes database or whole data directory.
- Evidence limits: No runs or crash tests; archive paths can be reconsidered by later indexing subject to its configuration. Immediate removal does not prove permanent exclusion or truth rejection.

Admission/rejection: callers propose withdrawal and server/HTTP controls can veto covered mutations, as in runtime. Integrity cleanup uses existence, not content truth. No answer oracle; open maintenance requests, not evaluation experiments. Recovery varies by mode and is not cross-resource atomic. Static archive/delete/existence rules guide operation; remaining disk artifacts or removal effects persist. Withdrawal does not revise a formulated theory or identify a false claim.

> if !full_path.exists() {
>             // Clean up orphan: vectors, FTS, edges, file record
> --- `src/writer.rs`

> // Delete disk file first, then purge store
>             std::fs::remove_file(&old_path)?;
>             store.delete_file_hard(&file_record.path)?;
> --- `src/writer.rs`

> // Delete only index files: engraph.db.
>                 let db_path = data_dir.join("engraph.db");
> --- `src/main.rs`

### Claims

#### EPI-CLM-vault-knowledge
Label: Vault knowledge API

Claimed operation: expose vault content and its connections as queryable agent knowledge/context, not an explicit promise of universally correct generated answers. No supplied claim counterpart; [RT-RTE-query-search](runtime.md#rt-rte-query-search) describes implementation, not this public claim. SRC-1 `README.md`, doctrine/design:

> engraph turns your markdown vault into a searchable knowledge graph that any AI agent can query
> --- `README.md`

Boundary already supplies this passage and its context. Implementation supports querying and associations; whether the contents merit factual reliance depends on unknown source warrant and downstream checking.

#### EPI-CLM-search-confidence
Label: Search confidence guidance

Claimed operation: display normalized confidence and advise a client to prefer higher matches. Distinct from supplied write-consistency/read-only claims; closest route is [RT-RTE-query-search](runtime.md#rt-rte-query-search). SRC-1 `README.md`, doctrine/design:

> - Results include confidence % — prefer higher confidence matches
> --- `README.md`

> - Confidence % display: search results show normalized 0-100% confidence instead of raw RRF scores
> --- `README.md`

The latter explicitly discloses normalization. The mismatch is a stronger probability/warrant reading, not proof the documentation claims calibrated factual certainty.

#### EPI-CLM-health-diagnostics
Label: Health diagnostics

Claimed operation: detect stale content along with structural issues and expose CLI/MCP diagnostics. No supplied claim counterpart; [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh) concerns maintenance, not diagnosis. SRC-1 `README.md`, doctrine/design:

> - **Vault health diagnostics** — detect orphan notes, broken wikilinks, stale content, and tag hygiene issues. Available as MCP tool and CLI command.
> --- `README.md`

> engraph context health
> --- `README.md`

Stale-content detection is unsupported by inspected stub, and ContextAction lacks a health variant. Exposed MCP/HTTP reporting remains supported.

#### EPI-CLM-placement-learning
Label: Placement correction learning

Claimed operation: learn placement corrections from user file moves. Distinct from [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), which names initial placement but not a learning claim. SRC-1 `README.md`, doctrine/design:

> - Placement correction learning from user file moves
> --- `README.md`

Inspected move-derived adaptation supports a concrete operational interpretation. Beneficial learning and intentional human correction are separate unestablished conclusions.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
