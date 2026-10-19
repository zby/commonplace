---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ClawVault epistemic routes: candidate production, proxy admission, fact supersession and consequential memory consumers."
run-id: AAS-2026-10-17-clawvault-38c16ae4ab34-01
reviewed-boundary: bd702e9cce436bc3065827714cd576e8be20c375
---

# ClawVault epistemic report

## Source-and-claim boundary

The question is how ClawVault turns supplied text into material licensed for later reliance, and what its checks actually establish. Scope and exclusions are those of the [boundary and Source register](boundary.md#source-register). All new inspection uses SRC-1 at the frozen commit, in the implementation layer unless expressly labelled doctrine/design. Nothing here executes the target or supplies observed-run or causal evidence.

The supplied runtime is a baseline, not a coverage limit. Direct source inspection checks plugin registration, the shipped CLI's maintenance/session dispatch, fact production and consumers, outbound rewriting, entity synthesis, replay, router admission, maintenance cleanup and benchmark scoring. These disclose materially different admission domains. A successful file write, confidence label, similarity hit or heading check is not an evidence-consuming decision that a proposition is true for an intended use.

Public/design claims include [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory), [RT-CLM-autonomous-research](runtime.md#rt-clm-autonomous-research) and [EPI-CLM-memory-answer](#epi-clm-memory-answer). The first is principally a storage/context claim, not an explicit universal factual-accuracy promise. The recall mandate is separately an instruction to consult memory: see [RT-OBJ-recall-mandate](runtime.md#rt-obj-recall-mandate).

### Coverage

“Supplied” below means the runtime's source-grounded finding was read; “direct” means this analyst additionally inspected source. Every path is under SRC-1. Uninspected included operations prevent a system-complete negative about epistemic evaluation or acceptance.

| Entry point or operation | Source path | Coverage and record or limit |
|---|---|---|
| Package/CLI dispatch and exported API | `bin/clawvault.js`, `bin/register-maintenance-commands.js`, `bin/register-session-lifecycle-commands.js`, `src/cli/index.ts`, `src/index.ts` | Direct dispatch inspection/search; replay, benchmark, entities and archive are exposed, not merely unused library functions. See [EPI-RTE-replay-import](#epi-rte-replay-import), [EPI-RTE-fixture-scoring](#epi-rte-fixture-scoring). Task/project/patch/migration branches are not traced; no uniform validation conclusion. |
| Actual host registrations | `src/openclaw-plugin.ts` | Direct: memory_search/get, prompt-build, outbound, start/end/reset/compaction/agent-end hooks; supplied [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall), [RT-RTE-tool-recall](runtime.md#rt-rte-tool-recall), [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter). Host delivery remains external. |
| Direct storage and capture | `src/plugin/slot.ts`, `src/lib/vault.ts`, `src/capture/service.ts`, `src/capture/quality.ts` | Supplied [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn); direct service search and synthesis inspection. Extractor internals not fully read: exact candidate semantics remain unresolved. |
| Observer/compressor and routing | `src/observer/compressor.ts`, `src/observer/router.ts` | Direct fallback, routing/admission, category append and fact branches; supplied [RT-RTE-observe-session](runtime.md#rt-rte-observe-session); new [EPI-RTE-router-admission](#epi-rte-router-admission), [EPI-RTE-fact-extraction](#epi-rte-fact-extraction). Full task conversion, normalization and auto-linking remain uninspected. |
| Compaction/reset fact path | `src/plugin/fact-extractor.ts`, `src/plugin/hooks/observation.ts`, `src/plugin/hooks/session-lifecycle.ts`, `src/lib/fact-extractor.ts`, `src/lib/fact-store.ts` | Direct collector/persistence/rule/conflict/query trace; hook call sites searched. See [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-supersession](#epi-rte-fact-supersession). LLM extraction parser and adapter internals not fully read. |
| Fact/context assembly | `src/commands/context.ts` | Direct fact selection, source grouping and final budget trace: [EPI-RTE-fact-context](#epi-rte-fact-context). Full graph expansion and budget-fitting helper not audited. |
| Outbound rewrite helpers | `src/plugin/communication-protocol.ts`, `src/plugin/hooks/message-sending.ts` | Direct complete helpers/handler: [EPI-RTE-question-rewrite](#epi-rte-question-rewrite). |
| Entity refresh/read | `src/entities/synthesis.ts`, `src/commands/entities.ts` | Direct synthesis/helpers and read path; command references searched. See [EPI-RTE-entity-synthesis](#epi-rte-entity-synthesis). Parser not fully read. |
| Inbox curation, distillation, cleanup | `src/lib/maintenance/distiller-worker.ts`, `src/lib/maintenance/janitor-worker.ts`, `src/commands/maintain.ts` | Direct distiller and janitor action branches; supplied combined [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox). Heuristic/parser and archive-loader details remain uninspected; no semantic equivalence or complete withdrawal claim. |
| Weekly reflection, archive, recovery | `src/observer/reflection-service.ts`, `src/commands/sleep.ts`, `src/commands/wake.ts` | Supplied [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week), [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff). Standalone rebuild/archive details not directly traced; no universal replay or recovery guarantee. |
| Retrieval, numerical providers | `src/lib/in-process-search.ts`, `src/lib/hosted-embeddings.ts`, `src/lib/hosted-rerank.ts` | Supplied runtime components and recall routes; provider weights/execution unavailable. No source-truth conclusion from relevance scores. |
| Peer admission and Python | `src/lib/tailscale.ts`, `python/src/clawvault/vault.py` | Supplied [RT-RTE-peer-sync](runtime.md#rt-rte-peer-sync), [RT-RTE-python-vault](runtime.md#rt-rte-python-vault). SDK helper and peer-server internals not inspected here. |
| Fixture scoring and change admission | `src/observer/benchmark/scoring.ts`, `autoresearch/experiment.sh`, `autoresearch/program.md` | Direct scoring; supplied [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change). Fixture correctness, stored result provenance and actual development rounds unassessed. |
| Separate evaluation, display and deployment | `eval/run_v35_full.py`, `dashboard/server.js`, `scripts/observe-active-sessions.sh`, `scripts/observe-stale-sessions.sh` | Boundary/runtime descriptions only. Evaluation adapter/reader/scorer unassessed; dashboard not treated as a factual evaluator. No end-to-end benchmark or deployment efficacy conclusion. |

Missing host traces prevent claims of actual model reliance or delivered cancellations. Missing candidate/input/output traces prevent attributing a persisted observation to a particular model/fallback/check route. Missing provider internals prevent parameter-level assessment beyond the supplied request wiring. No registered observed-run or causal layer establishes improved future capacity, successful self-improvement or a component effect. Available uninspected source is not an access failure.

## Epistemic-object inventory

Owned fields below are in the cited declarations; the inventory adds no alternate identity or status.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | Caller assertions, observations, handoffs and distilled prose; selectors are a distinct symbolic part | see record | SRC-1, `src/lib/vault.ts` | A file can contain assertions without being accepted as true; raw caller warrant unknown. |
| [RT-OBJ-recall-mandate](runtime.md#rt-obj-recall-mandate) | None: imperative policy, not an empirical result | see record | SRC-1, `src/plugin/hooks/before-prompt-build.ts` | Instruction delivery is not compliance. |
| [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | Entity–relation–value claims; validity/confidence fields separately drive selection | see record | SRC-1, `src/lib/fact-store.ts` | Attribution and scope can be lost even though rawText/source are retained. |
| [EPI-OBJ-entity-profile](#epi-obj-entity-profile) | Kind conjecture, copied summary, link-cooccurrence counts and file-mtime metadata are separate parts | see record | SRC-1, `src/entities/synthesis.ts` | Cooccurrence is not a world relationship; copied snippet may be incomplete. |
| [EPI-OBJ-outbound-message](#epi-obj-outbound-message) | Foreground text plus appended claims that memory contains relevant details | see record | SRC-1, `src/plugin/communication-protocol.ts` | Question punctuation replacement is not answer derivation. |
| [EPI-OBJ-scoring-result](#epi-obj-scoring-result) | Formal claims about token matches and weighted fixture metrics | see record | SRC-1, `src/observer/benchmark/scoring.ts` | Metric names do not license semantic accuracy. |
| [RT-CMP-hosted-embeddings](runtime.md#rt-cmp-hosted-embeddings), [RT-CMP-hosted-rerank](runtime.md#rt-cmp-hosted-rerank) | Not individually identifiable world propositions in accessible dense state/scores | see records | SRC-1, `src/lib/hosted-embeddings.ts`, `src/lib/hosted-rerank.ts` | Truth-apt content in weights is not determinable; ranking role is inspectable. |

## Authority-route ledger

Every row has its own function and architectural assessment. “See” delegates the declaring record's mechanism fields, not this report's assessment. No listed implementation is asserted to have operated. All evidence is SRC-1 implementation; claim evidence is separately labelled below. “No acceptance” means no evidence-consuming truth decision in the named inspected route, not a system-wide absence. Retention and operational use are deliberately not labelled lifecycle integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-slot-store](runtime.md#rt-rte-slot-store) | retention | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: acquisition/import | Caller text becomes retained Markdown | see record; naming/collision rules, not truth | see record | see record | Permissive write | Source warrant unknown; serialization does not validate assertions | Later document availability changes | Vault loader/search, Markdown/index, permissive, subsequent calls | SRC-1, `src/lib/vault.ts` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | Direct writes bypass capture checks. |
| [RT-RTE-python-vault](runtime.md#rt-rte-python-vault) | retention | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: acquisition/import | Python caller text becomes retained Markdown | see record; independent category/collision rules | see record | see record | Permissive write | Caller warrant unknown | Independent SDK read availability changes | Python list/search/wake, files, permissive, later calls | SRC-1, `python/src/clawvault/vault.py` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | API resemblance is not validation parity. |
| [RT-RTE-peer-sync](runtime.md#rt-rte-peer-sync) | retention | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: acquisition/import | Peer file becomes local retained content | see record; manifest/hash/time/direction criteria | see record | see record | Direct overwrite and optional deletion | Peer source warrant unknown; timestamp is not endorsement | Local content availability changes | Later local loaders, transferred files, permissive, future loads | SRC-1, `src/lib/tailscale.ts` | none | none | No content gate or automatic index refresh established here. |
| [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn) | check/evidence production | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | no content change | Extractor candidates' confidence/noise/similarity/quality | see record; candidate hygiene domain | Before write | Pass or rejection reason | Gate result supplied to capture loop | Proxy qualification only; no factual license | Makes candidate eligible/ineligible | Capture loop, quality result, enforcing, current capture | SRC-1, `src/capture/quality.ts` | none | none | Extractor semantics remain partly uninspected. |
| [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn) | disposition/acceptance | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | no content change | Admit passing candidate up to cap | see record | After quality result | Persist or skip | Enforcing local admission | Operational admission, not truth acceptance | Stores up to configured accepted count | Store loop, decision branch, enforcing, current turn and retained files | SRC-1, `src/capture/service.ts` | none | none | Other writes bypass this gate. |
| [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) | content transformation | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: indeterminate | Messages plus prior observations to compressed statements | see record and [RT-CMP-compressor](runtime.md#rt-cmp-compressor); model request or symbolic fallback | Threshold or flush | Candidate observations | Model/fallback output conditions write | Prompt asks for durable observations, not proof; per-output preservation unestablished | Daily observations can be replaced and routed | Observer then wake/router/reflection, Markdown, permissive/advisory, later invocations | SRC-1, `src/observer/compressor.ts` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | Alternatives include reshaping and non-entailed generation; paired content needed. Deterministic fallback also filters/calibrates, so not all output is LLM-produced. |
| [EPI-RTE-router-admission](#epi-rte-router-admission) | disposition/acceptance | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | no content change | Importance, category, duplicate candidacy | see record; threshold/string-overlap domain | After compression | Skip or category append | Enforcing category admission | No truth acceptance; overlap need not mean equivalent propositions | Makes selected observations available in category files | Router, branching and append, enforcing, this routing and later loads | SRC-1, `src/observer/router.ts` | none | none | Task conversion and independent fact branch differ; source record bounds them. |
| [EPI-RTE-fact-extraction](#epi-rte-fact-extraction) | content transformation | implemented | [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | truth-apt transformation: indeterminate | Text to normalized propositions | see record; regex or requested LLM extraction | Reset/compaction or observer routing | Candidate triples | Candidates proceed to store without truth test | Ordinary literal extraction may reshape; fictional/quoted text can yield non-entailed user assertions | Enables fact persistence | FactStore, extracted records, permissive, subsequent queries | SRC-1, `src/lib/fact-extractor.ts`, `src/plugin/fact-extractor.ts` | none | scope-loss witness | Concrete fictional example below is ampliative conjecture, not warranted derivation. LLM per-output relation unestablished. |
| [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | disposition/acceptance | implemented | [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | no content change | Same normalized entity/relation, similar or exclusive value | see record; fixed conflict policy | On addFacts | Old validUntil set; new indexed | Enforcing active-set change | Fresh arrival is not evidence that old claim is false/new claim true | Old fact excluded by active queries | FactStore queries, validity field, enforcing, future calls until replacement | SRC-1, `src/lib/fact-store.ts` | none | none | Arrival order rather than source credibility controls; duplicate ID can replace history. |
| [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | retention | implemented | [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | no content change | In-memory facts to JSONL and graph | see record | After mutation | Rewritten store, graph snapshot in plugin route | File writes | Persistence adds no warrant | State available for later reload | Fact consumers, JSONL, permissive, cross-invocation | SRC-1, `src/lib/fact-store.ts`, `src/plugin/fact-extractor.ts` | none | none | Not append-only in save; graph is not proven consumed by every context route. |
| [EPI-RTE-fact-context](#epi-rte-fact-context) | operational admission/selection/consumption | implemented | [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | truth-apt transformation: non-ampliative reshaping | Active facts to context entries | see record; lexical match, preference expansion, confidence, profile caps and budget | Explicit buildContext | Triple snippets/rationale in returned context; possibly omitted/truncated Markdown | Ranking and permissive delivery | Licenses selection only, not factual endorsement | Promotes selected facts into assembled context | Caller/agent if delivered, returned context/Markdown, advisory/ranking, current invocation with future reload | SRC-1, `src/commands/context.ts` | none | none | Does not show plugin automatically uses this builder. RawText is not delivered in fact snippet. |
| [EPI-RTE-entity-synthesis](#epi-rte-entity-synthesis) | content transformation | implemented | [EPI-OBJ-entity-profile](#epi-obj-entity-profile) | truth-apt transformation: ampliative conjecture | Entity kind from category/name | see record; category counts and name regex | Capture synthesis or refresh | person/project/org/place/unknown | Label written, not independently checked | Candidate type only; name/category does not entail real entity kind | Type appears in retained profile | Profile readers, Markdown/frontmatter, advisory or symbolic selector where consumed, later reads | SRC-1, `src/entities/synthesis.ts` | none | none | A title in people can describe a company; no checked world premise entails person. |
| [EPI-RTE-entity-synthesis](#epi-rte-entity-synthesis) | content transformation | implemented | [EPI-OBJ-entity-profile](#epi-obj-entity-profile) | truth-apt transformation: entailed derivation | Link-cooccurrence strength, evidence document IDs, max file mtime | see record; finite file/link computation | Synthesis | Counts/top-eight relationships and lastMentioned | Computed fields rendered | Only syntactic link cooccurrence and file modification recency, conditional on parsed inputs | Organizes profiles | Profile readers, generated fields, advisory, later reads | SRC-1, `src/entities/synthesis.ts` | none | none | Neither substantive relationship strength nor actual mention time is established. |
| [EPI-RTE-entity-synthesis](#epi-rte-entity-synthesis) | content transformation | implemented | [EPI-OBJ-entity-profile](#epi-obj-entity-profile) | truth-apt transformation: indeterminate | Newest document's leading 180 characters to entity summary | see record | Synthesis | Copied prefix, terminal period added if needed | Summary persisted | Conditional source-content carriage; truncation/reference ambiguity may degrade warrant | Supplies summary to readers | Profile read, Markdown/string, advisory, later calls | SRC-1, `src/entities/synthesis.ts` | none | none | Newest document snippet is not necessarily about this entity. |
| [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox) | content transformation | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: indeterminate | Long-form inbox to facts/decisions/lessons | see record; model JSON or heuristic insights | Pending long-form inputs | Distilled files with inbox hash/path | Parsed entries written | Traceable candidate extraction, not truth acceptance | Adds categorized candidate prose | Future vault consumers, Markdown, permissive/advisory, later queries | SRC-1, `src/lib/maintenance/distiller-worker.ts` | none | none | Input samples/parser/heuristics do not establish entailment for each output. |
| [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox) | disposition/acceptance | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | no content change | Duplicate/stale inbox membership | see record; normalized grouping and 30-day age branch | Janitor run | Later duplicates/stale files archived; merged files emitted | Moves/writes; report recommendations are advisory | Hygiene/age decisions, not truth rejection | Changes ordinary inbox eligibility | Inbox readers, file placement, enforcing, later maintenance | SRC-1, `src/lib/maintenance/janitor-worker.ts` | none | none | LLM hygiene recommendations follow automatic actions; complete retrieval withdrawal unestablished. |
| [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week) | check/evidence production | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | no content change | Nonempty rewrite and required headings | see record; structural text domain | Before reflection output choice | Accept rewritten shape or use deterministic draft | Output selector consumes result | Section presence only; not preservation/truth | Permits model rewrite or fallback | Reflection writer, shape check, enforcing, current weekly output | SRC-1, `src/observer/reflection-service.ts` | none | none | No evidence-consuming claim acceptance. |
| [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week) | retention | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: indeterminate | Consolidated weekly candidate and source archive | see record | After structural selection, unless dry-run | Weekly Markdown plus older-input archive | Writes/archive alter future consolidation | Retention before demonstrated truth acceptance | Future reflection excludes prior keys; originals move | Later reflection/search where eligible, files/keys, enforcing selection and advisory prose, future weeks | SRC-1, `src/observer/reflection-service.ts` | none | none | Not lifecycle integration under this contract. |
| [EPI-RTE-replay-import](#epi-rte-replay-import) | content transformation | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: acquisition/import | Historical export messages into observer | see record | Explicit replay, not dry-run | Date-grouped messages, observation and reflection requests | Import then ordinary observer admission | Imported source warrant unknown; normalization not truth checking | Backfills retained content | Observer/reflection then later memory consumers, text/files, permissive, cross-invocation | SRC-1, `src/commands/replay.ts` | none | none | Downstream compression relation separate above; normalizer semantic fidelity uninspected. |
| [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall) | operational admission/selection/consumption | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: non-ampliative reshaping | Retained text to bounded unsolicited snippets | see record; relevance/recency thresholds | Prompt-build event | Context additions or no content on fetch failure | Advisory privileged-channel delivery | Source content unverified; shortened excerpts can lose qualifications | Supplies selected material before model invocation | see [RT-BAP-system-context](runtime.md#rt-bap-system-context) | SRC-1, `src/plugin/vault-context-injector.ts` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | Selection/formatting is non-ampliative, not guaranteed semantically safe. |
| [RT-RTE-tool-recall](runtime.md#rt-rte-tool-recall) | operational admission/selection/consumption | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: non-ampliative reshaping | Foreground search request to result snippets | see record; sanitized query, score and limit | Agent tool request | Scored/path-labelled snippets | Ranking/advisory | Relevance and estimated citation location only | Makes selected text available to agent | Host model, tool result, advisory/ranking, current response | SRC-1, `src/plugin/memory-manager.ts` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | Agent selection and actual grounding unobserved. |
| [RT-RTE-tool-recall](runtime.md#rt-rte-tool-recall) | operational admission/selection/consumption | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: non-ampliative reshaping | Explicit detail path to whole/sliced text | see record; MEMORY.md or memory/* lexical allowlist | memory_get request | File text, empty missing result or rejection | Path restriction enforcing; text advisory | No truth license from allowed path | Permits/blocks detail reads | Tool consumer, result/error, enforcing path gate and advisory prose, one call | SRC-1, `src/plugin/memory-manager.ts` | none | search/get scope mismatch | A search hit can name a path detail lookup rejects. |
| [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff) | operational admission/selection/consumption | implemented | [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) | truth-apt transformation: indeterminate | Stored handoff/checkpoint/observations to wake context | see record; handoff limit, recency/importance, optional summary | Explicit wake | Recovery/context result | Advisory return | Caller-originated work state, not checked adequacy or truth | Offers continuity material for next invocation | Caller/agent if delivered, wake string/result, advisory, resumed session | SRC-1, `src/commands/wake.ts` | [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | none | Selection alone reshapes; optional summary semantics unverified. |
| [EPI-RTE-question-rewrite](#epi-rte-question-rewrite) | content transformation | implemented | [EPI-OBJ-outbound-message](#epi-obj-outbound-message) | truth-apt transformation: ampliative conjecture | Question plus hits to relevance assertion | see record; punctuation and snippet appending | On hits above search threshold | Original question punctuation replaced; relevance claim appended | Rewritten text returned | Retrieval relevance does not establish that hits answer the question | Replaces proposed outgoing content | Message hook/host, content override, enforcing if honored, current outbound message | SRC-1, `src/plugin/communication-protocol.ts` | [EPI-CLM-memory-answer](#epi-clm-memory-answer) | hit-is-not-answer | No answer entailment evaluator; this is not merely a tone edit. |
| [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter) | operational admission/selection/consumption | implemented | [EPI-OBJ-outbound-message](#epi-obj-outbound-message) | non-truth-apt policy/content update: phrase and question filtering | Outbound string eligibility | see record; feature flag and question detector | message_sending | Replacement or cancel if question remains | Hook requests enforcement | No factual license | Can suppress delivery or replace message | Host sending path, hook return, enforcing if honored, one send | SRC-1, `src/plugin/hooks/message-sending.ts` | [EPI-CLM-memory-answer](#epi-clm-memory-answer) | none | Other channels and host compliance unobserved. |
| [EPI-RTE-fixture-scoring](#epi-rte-fixture-scoring) | check/evidence production | implemented | [EPI-OBJ-scoring-result](#epi-obj-scoring-result) | truth-apt transformation: entailed derivation | Parsed expected/actual observation strings | see record; token overlap, type equality, keyword presence | Benchmark fixture run | Weighted scalar and diagnostics | Evaluation returned to benchmark/script | Formal metrics within specified parser/token domain, not world truth | Supplies selection signal | Benchmark then experiment gate, report/scalar, ranking then enforcing, experiment rounds | SRC-1, `src/observer/benchmark/scoring.ts` | [RT-CLM-autonomous-research](runtime.md#rt-clm-autonomous-research) | metric-domain-limit | Negation discarded; concrete contrast below. |
| [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change) | disposition/acceptance | implemented | [EPI-OBJ-scoring-result](#epi-obj-scoring-result) | no content change | Edited repository versus prior best | see record; build/subset tests and strict overall-score gain | External agent supplies edit/commit | Keep, discard/reset, or crash | Enforcing branch/result gate | Acceptance for fixture score objective only, not an accepted explanatory/world claim | Keeps machinery changes or rejects commit | Script/Git then prescribed next agent round, score/branch state, enforcing, development rounds | SRC-1, `autoresearch/experiment.sh` | [RT-CLM-autonomous-research](runtime.md#rt-clm-autonomous-research) | doctrine/script divergence | No demonstrated production installation, activation or causal gain. |

Additional load-bearing passages for the direct refinements of supplied routes follow. They support the local mechanism assessments above, not observed execution or semantic accuracy.

For [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox), distiller source linkage and automatic writes are explicit:

> const body = `## ${sectionTitle}\n${entries.map((line) => `- ${line}`).join('\n')}\n\n---\nDistilled from \`${item.relativePath}\`.\n`;
> --- `src/lib/maintenance/distiller-worker.ts`

> const insights = llmInsights.get(item.hash) ?? extractHeuristicInsights(item.content);
> writeDistilledEntries(ctx, item, 'facts', 'Facts', insights.facts, logger, actions);
> writeDistilledEntries(ctx, item, 'decisions', 'Decisions', insights.decisions, logger, actions);
> writeDistilledEntries(ctx, item, 'lessons', 'Lessons', insights.lessons, logger, actions);
> --- `src/lib/maintenance/distiller-worker.ts`

For the same supplied route, janitor age-based withdrawal is independent of the later recommendation request:

> const staleCutoffMs = ctx.now().getTime() - (30 * 24 * 60 * 60 * 1000);
> for (const item of refreshItems) {
> if (item.capturedAt.getTime() >= staleCutoffMs) {
> continue;
> }
> const archiveDir = path.join(ctx.vaultPath, 'inbox', 'archive', 'stale');
> const moved = moveToArchive(item.path, archiveDir, ctx.dryRun);
> --- `src/lib/maintenance/janitor-worker.ts`

For [RT-RTE-observe-session](runtime.md#rt-rte-observe-session), the deterministic fallback filters candidates and calibrates metadata rather than only storing raw text:

> if (this.shouldDropLowSignalCandidate(candidate.content)) {
> continue;
> }
> const calibrated = this.calibrateFallbackCandidate(candidate);
> --- `src/observer/compressor.ts`

There is no evidenced lifecycle-integration row: within these inspected routes, content is retained, organized and consumed without a prior named evidence-consuming truth acceptance. This is a bounded finding about the rows, not an absence declaration for unassessed operations.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory) | see record | SRC-1, `package.json`, doctrine/design | Typed persistent memory/context | see [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall) | None registered | No utility experiment; alternate writes/checks differ | Durable text and selection/delivery are implemented capacities | Slogan about never forgetting is not a demonstrated completeness guarantee. |
| [EPI-CLM-memory-answer](#epi-clm-memory-answer) | see record | SRC-1, `src/plugin/communication-protocol.ts`, doctrine/design and implementation | Consult memory, avoid questions already answered | see [EPI-RTE-question-rewrite](#epi-rte-question-rewrite), [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter) | None registered | Hook takes search hits, not an answer test | Code can rewrite/suppress on this channel | A hit can trigger relevance language without answering the question; host delivery unknown. |
| [RT-CLM-autonomous-research](runtime.md#rt-clm-autonomous-research) | see record | SRC-1, `autoresearch/program.md`, doctrine/design | External agent hypothesis/edit/benchmark/keep-discard loop | see [EPI-RTE-fixture-scoring](#epi-rte-fixture-scoring), [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change) | No exercised round established | Editable metrics/fixtures, no independent transfer or component intervention | Dormant benchmark-guided change-admission capacity | Script strict aggregate gain differs from doctrine's dimension/no-regression rule; no autonomous editing implemented by runner alone. |

## Bounded conclusion

ClawVault implements several distinct routes to operational reliance. Caller and peer text can enter files without capture checks. Capture checks proxy quality and duplication. Compression, distillation and reflection produce retained candidates; the structural reflection gate does not establish semantic preservation. Imported content is acquired with unknown source warrant, not newly produced warranted knowledge. These mechanisms support persistent memory/context capacity, not a uniform truth-admission pipeline: see [RT-RTE-slot-store](runtime.md#rt-rte-slot-store), [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn), [RT-RTE-observe-session](runtime.md#rt-rte-observe-session), [RT-RTE-maintain-inbox](runtime.md#rt-rte-maintain-inbox), [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week).

The fact path exposes a particularly consequential distinction. Rule extraction can lose quotation/fictional scope; recency/conflict policy then marks the prior value inactive, and context assembly delivers the normalized triple without its rawText. Thus retaining provenance does not ensure that the later consumer receives its qualifications. The operational license is active-set membership and context priority, not evidence that a newly arrived assertion is true: see [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-supersession](#epi-rte-fact-supersession), [EPI-RTE-fact-context](#epi-rte-fact-context).

Entity synthesis supplies an independent positive: finite link counts and maximum file-mtime values follow from its parsed inputs in that syntactic domain. They do not prove world relationships or event dates. Entity kind is heuristic conjecture, while copying the newest prefix is not a checked summary of an entity. No warranted world premises or evidence-consuming acceptance were established for these parts: see [EPI-RTE-entity-synthesis](#epi-rte-entity-synthesis).

Retrieval selects material by relevance and recency and can deliver it in host system context, but privileged delivery supplies no factual endorsement. The outbound path goes further: a search hit licenses actual proposed-message replacement and sometimes cancellation. Its deterministic helper does not derive an answer from evidence. This is a code-mediated behavioral-authority path, distinct from the advisory recall mandate: see [RT-BAP-system-context](runtime.md#rt-bap-system-context), [EPI-RTE-question-rewrite](#epi-rte-question-rewrite), [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter).

Checks with operative force do exist: capture hygiene gates, router thresholds/dedup, structural reflection selection, fact active-set changes, janitor archive rules and development score admission. Their licenses remain separate. Benchmark arithmetic derives formal fixture measurements, and the development script accepts a commit for a named scalar objective after build/subset-test checks. That is neither truth acceptance of generated claims nor causal evidence of improved real memory. No examined route supplies the prior acceptance needed to call its subsequent organization lifecycle integration under this contract. Unassessed evaluation/adapters and mutation paths prevent generalizing this negative to the complete system: see [EPI-RTE-fixture-scoring](#epi-rte-fixture-scoring), [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change).

Learning, reflection, autonomy and self-improvement remain independent. The supplied development record affords reflection through editable machinery and reports, prescribes autonomous iteration, and wires scalar selection; it does not establish content-directed criticism or exercised self-improvement. In particular evidence-responsive determination of an actual update and its later live deployment/use remain unestablished. The source-native weekly “reflection” is consolidation, not evidence by its name alone of theory criticism. Distributed-parametric clients request inference with mutable model aliases/endpoints, not inspected parameter updates; inaccessible provider state cannot settle other learning claims. See [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change), [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week), [RT-CMP-compressor](runtime.md#rt-cmp-compressor), [RT-CMP-worker-llm](runtime.md#rt-cmp-worker-llm), [RT-CMP-hosted-embeddings](runtime.md#rt-cmp-hosted-embeddings), [RT-CMP-hosted-rerank](runtime.md#rt-cmp-hosted-rerank). No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-extracted-facts
Label: Extracted facts

Source-native ExtractedFact records combine natural-language entity/value/rawText with symbolic relation, category, source, confidence, validFrom/validUntil and hashed identity in `.clawvault/facts.jsonl`. The plugin additionally serializes an entity-graph snapshot. They are distinct from [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents): these are JSONL records with active-set queries, not Markdown documents. Confidence/validity metadata has fixed selection consumers; rawText has contextual prose content. SRC-1, `src/lib/fact-extractor.ts`, `src/lib/fact-store.ts`, `src/plugin/fact-extractor.ts`.

> this.factsPath = path.join(vaultPath, '.clawvault', 'facts.jsonl');
> --- `src/lib/fact-store.ts`

> confidence: 0.7, // Rule-based gets moderate confidence
> category: extracted.category,
> source,
> rawText: trimmed
> --- `src/lib/fact-extractor.ts`

#### EPI-OBJ-entity-profile
Label: Entity profile

Part of: [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents)

Source-native EntityProfile becomes `entities/*.md`: summary is natural-language text; kind, aliases, lastMentioned, relationship counts and evidence IDs are structured fields rendered for later readers. Different parts have different epistemic licenses despite sharing a file. SRC-1, `src/entities/synthesis.ts`. This specializes a material document family, not an alternative identity for the entire vault.

> kind,
> summary: buildSummary(name, records),
> relationships,
> lastMentioned
> --- `src/entities/synthesis.ts`

#### EPI-OBJ-outbound-message
Label: Outbound message

Source-native outbound `content` and ProtocolRewriteResult are transient strings in the plugin's sending path. Natural-language text affects the recipient by interpretation; content/cancel fields are symbolic host controls. Unlike [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents), this is not a retained memory; unlike [RT-OBJ-recall-mandate](runtime.md#rt-obj-recall-mandate), it is a current outgoing message. SRC-1, `src/plugin/hooks/message-sending.ts`, `src/plugin/communication-protocol.ts`.

> return { content };
> --- `src/plugin/hooks/message-sending.ts`

#### EPI-OBJ-scoring-result
Label: Fixture scoring result

Source-native FixtureScoringResult holds symbolic numerical metrics, matches and diagnostic lists, computed in memory and passed to benchmark reporting. It is distinct from [RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents), and is an intermediate evidence object within [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change), not a product-memory assertion. SRC-1, `src/observer/benchmark/scoring.ts`.

> metrics: computed.metrics,
> matches,
> missedImportant: computed.missedImportant,
> noiseObservations: computed.noiseObservations,
> keywordSet,
> missingKeywords: computed.missingKeywords,
> keywordRewriteFlags: computed.keywordRewriteFlags
> --- `src/observer/benchmark/scoring.ts`

### Routes

#### EPI-RTE-fact-extraction
Label: Fact extraction

The plugin collector sanitizes/truncates strings to 6,000 characters, recursively collects selected event keys, deduplicates, then rule-extracts and persists. Source is a hook label, not an authenticated speaker. The observer router separately runs rule/LLM/hybrid extraction on observation Markdown; asynchronous LLM branches can return zero before their eventual write. This spans and is distinct from the broader [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) and hook-driven observation described in the runtime account: neither individuates the common fact-proposition construction mechanism. SRC-1, `src/plugin/fact-extractor.ts`, `src/lib/fact-extractor.ts`, `src/observer/router.ts`.

The rule's target is a text pattern, not the truth of the extracted proposition. A source-level deduction gives a counterexample to universal semantic preservation: `In a fictional example I prefer tea.` is split at the final period; the unanchored preference regex matches `I prefer tea`, captures `tea`, and emits entity user/relation prefers/value tea with confidence 0.7 and the fictional sentence in rawText. The premise about a fictional example does not entail a preference of the actual user. This is a non-entailed candidate in this concrete case; other direct first-person statements may merely reshape supplied assertions. Therefore the generic route relation is indeterminate, not universally ampliative or entailed. No target execution is needed for this implementation deduction.

Computation proposes and admits candidates; no per-fact human veto or expected-answer oracle appears in this inspected path. Operating mode is open event/observation processing, triggered by hooks/routing. The guidance in the extraction module seeks structured facts, but fixed confidence and pattern matches do not supply source warrant. What persists is the constructed claim, rawText and metadata. Recovery after partial fact/graph writes is not established.

- Immediate return: Plugin counts, or router synchronous count while LLM persistence can finish later.
- Later read-back: FactStore and buildContext reload persisted facts; see [EPI-RTE-fact-context](#epi-rte-fact-context).
- Delegated visibility: Optional LLM receives observation text via extraction adapter; event rule path uses no model.
- Selection predicate: Collected nonempty event fragments or configured router extraction mode; sentence/pattern/value-length checks.
- Invalidation or expiry: New facts enter separate conflict handling; no standalone expiry in extraction.
- Activation or effect: Constructs records that can be retained and selected for later context; actual behavioral activation unobserved.
- Evidence limits: Provider output and normalizer semantics unobserved; LLM parser/adapter not fully inspected. Concrete counterexample is implementation-layer deduction only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> pattern: /\b(?:i|user|they)\s+(?:prefer|like|love|enjoy|want|favor)s?\s+(.+?)(?:\.|,|$)/i,
> extract: (m) => ({
> entity: 'user',
> relation: 'prefers',
> value: m[1].trim(),
> category: 'preference'
> })
> --- `src/lib/fact-extractor.ts`

> const sentences = text.split(/[.!?\n]+/).filter(s => s.trim().length > 5);
> --- `src/lib/fact-extractor.ts`

> const source = `hook:${sourceLabel}`;
> --- `src/plugin/fact-extractor.ts`

#### EPI-RTE-fact-supersession
Label: Fact supersession

Source-native FactStore.addFacts/findConflict/save owns a separate disposition/retention mechanism, downstream of [EPI-RTE-fact-extraction](#epi-rte-fact-extraction). No exact supplied counterpart was found; the broader [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) does not individuate active-fact replacement. Software compares normalized entity/relation and string similarity or an exclusive-relation allowlist, sets existing.validUntil from the incoming timestamp, indexes the incoming ID and saves a full rewritten file. Confidence, evidence quality and timestamp ordering are not comparison conditions in findConflict. This is operational recency/update policy, not epistemic acceptance or falsification. Same-ID indexing can overwrite an old object, so universal preservation of superseded history is unsupported. SRC-1, `src/lib/fact-store.ts`.

A concrete deduction: active Alice/lives_in/Paris followed by Alice/lives_in/London is a conflict because lives_in is exclusive, even if the second assertion lacks evidence or has an earlier timestamp. Active queries then omit the old fact through validUntil; no evidence consumption settles which city is true. A countercase bounds replacement: unrelated nonexclusive values can coexist. Generic ingestion supplies candidates; software decides/vetoes active-set membership without per-item human approval or an answer oracle. Operating mode is ordinary store update. Rejected/withdrawn availability is via active filtering; no automatic rollback on later factual criticism is established. Plugin graph regeneration follows store save and is not shown transactional.

- Immediate return: Conflict count; save returns after file write.
- Later read-back: Active fact queries omit validUntil records; getFactsAt can use bounded validity intervals.
- Delegated visibility: Files and plugin graph snapshot are available to independent local clients; no worker launch.
- Selection predicate: Entity/relation plus equal/contained value or exclusive relation; save iterates current map.
- Invalidation or expiry: Incoming conflict sets validUntil; same ID can replace prior map entry.
- Activation or effect: Changes which claims future active queries expose and retains current map on disk.
- Evidence limits: No factual oracle, rollback trace, atomicity guarantee or observed conflict handling supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> existing.validUntil = fact.validFrom;
> conflicts++;
> --- `src/lib/fact-store.ts`

> if (this.isExclusiveRelation(newFact.relation)) {
> return existing;
> }
> --- `src/lib/fact-store.ts`

> getEntityFacts(entity: string): ExtractedFact[] {
> const norm = normalizeEntity(entity);
> const ids = this.byEntity.get(norm);
> if (!ids) return [];
> return Array.from(ids)
> .map(id => this.facts.get(id)!)
> .filter(f => f && !f.validUntil);
> }
> --- `src/lib/fact-store.ts`

#### EPI-RTE-fact-context
Label: Fact context assembly

The context command's buildFactContextItems/buildContext reads active fact records, uses lexical query matching, expands preference queries with all preferences, takes up to ten matches and formats entity/relation/value. It scores confidence times 0.8 with preference/temporal boosts. Profile ordering, source caps/dedup and optional final token budget can omit entries. If no whole block fits, a top entry may remain in the structured return while its Markdown is truncated; a header-only budget can remove all entries. SRC-1, `src/commands/context.ts`. This is distinct from the supplied [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall), which uses vault.find in the plugin; it is an explicit context-builder route, not evidence that every host prompt consumes facts.

The truth target is not evaluated. Code grants selection priority to stored claims; neither source authenticity nor rawText qualifies the delivered triple. No answer oracle or per-entry human decision is wired. Fixed prioritization is operational guidance, not retained theory criticism. Source files remain reachable after context omission, but the returned string holds content by value, not a live reference. No host-window eviction is implemented by this builder.

- Immediate return: ContextResult with entries, Markdown, task/profile and generation time.
- Later read-back: Previously extracted facts reach an explicit later context build; actual caller/model use unobserved.
- Delegated visibility: Caller receives selected context, not full rawText/fact log; no subagent.
- Selection predicate: Active queries, lexical match/preference expansion, first ten, score/profile caps, dedup and budget.
- Invalidation or expiry: Rebuild reflects current active set; caller-held strings can outlive replacement.
- Activation or effect: Delivers ranked fact assertions for potential later reliance, without epistemic acceptance.
- Evidence limits: Full fitWithinBudget helper and enclosing caller behavior not inspected; no plugin automatic-use inference.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const factText = `${fact.entity} ${fact.relation} ${fact.value}`;
> let score = fact.confidence * 0.8;
> --- `src/commands/context.ts`

> const { context, markdown } = applyTokenBudget(ordered, normalizedTask, options.budget);
> --- `src/commands/context.ts`

#### EPI-RTE-router-admission
Label: Observer router admission

Part of: [RT-RTE-observe-session](runtime.md#rt-rte-observe-session)

The router takes parsed observation candidates, skips importance below 0.4, categorizes and appends. Category append can independently skip normalized duplicates or containment/overlap above 0.8, then add wiki-links and write scored lines. A routed-list entry is pushed before append, so routed count alone does not prove a new category line was written. The separate task branch can act on work items and is not fully traced; independent fact extraction runs on observationMarkdown outside this per-item threshold loop. SRC-1, `src/observer/router.ts`. These narrow the container's admission account without superseding it.

The target is route/duplicate eligibility, not truth. Software decides from model/symbolic candidate metadata; no expected-answer oracle, human per-item veto or factual acceptance criterion is present in these branches. Prompt guidance comes upstream from compression. Ordinary open observation mode; resulting category state persists. No semantic rollback is demonstrated.

- Immediate return: Routed list, summary and synchronous factsExtracted count.
- Later read-back: Category Markdown can enter subsequent vault retrieval; full archive/index refresh behavior uninspected.
- Delegated visibility: No independent agent launch; code receives observation text/context.
- Selection predicate: Importance, task/category rules, destination matching and normalized similarity.
- Invalidation or expiry: Duplicate omission affects admission, not retraction of an existing false claim; separate maintenance may move files.
- Activation or effect: Writes selected category text, creates work-item effects in a partly uninspected branch, invokes fact extraction independently.
- Evidence limits: Category/task helpers, addWikiLinks and full fact-mode adapter not completely inspected; no system-wide semantic preservation guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (item.importance < 0.4) continue;
> --- `src/observer/router.ts`

> routed.push(routedItem);
> this.appendToCategory(category, routedItem, knownProjectDefinitions);
> --- `src/observer/router.ts`

> if (longer.includes(shorter) || this.similarity(normalizedNew, normalizedExisting) > 0.8) return;
> --- `src/observer/router.ts`

#### EPI-RTE-entity-synthesis
Label: Entity profile synthesis

This is a distinct stage mentioned but not individuated in [RT-RTE-capture-turn](runtime.md#rt-rte-capture-turn), also reachable through entity refresh/read APIs. It loads documents, collects names from wiki-links and people/project titles, takes leading snippets, computes cooccurrence relationships and infers kind. Software owns proposal and write decisions; no factual evaluator, answer oracle or per-profile human veto. Ordinary refresh/capture mode. Rules, rather than an LLM, shape this proposal. What persists is a Markdown profile; later readEntityProfile/ensureEntityProfiles can return it without regeneration if profiles already exist. SRC-1, `src/entities/synthesis.ts`.

Counterexamples prevent treating all synthesis as either conjecture or entailed knowledge. For `Acme Inc` with no people/project category evidence, the name regex returns org, although a fictional place can bear that name: real kind is not entailed. Conversely relationship strength counts actual inspected link cooccurrences, and lastMentioned takes max document.modified; these are entailed file-domain values given correctly parsed documents, not real relationship/mention facts. Summary uses the newest document's leading 180 characters, not an entity-targeted explanation. It may cut qualifications or summarize a different subject. No evidence-consuming acceptance precedes writes, hence organization is not lifecycle integration here.

- Immediate return: Sorted EntityProfile array; read APIs return existing/matched profile or null.
- Later read-back: Persisted entity files are parsed on later reads and may be included by general vault indexing.
- Delegated visibility: Local API/CLI consumers receive profile content; no model/backend call in inspected synthesis.
- Selection predicate: Link/title mentions, category/name kind heuristics, newest mtime snippet and top-eight cooccurrence counts.
- Invalidation or expiry: Refresh writes current profile files; ensure returns any existing collection without forced refresh. Complete orphan cleanup not established.
- Activation or effect: Creates candidate labels/summaries and derived file-domain metadata for later readers; behavior unobserved.
- Evidence limits: Parser details and any downstream kind selectors not fully audited; output does not prove a fact about the world.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (/\b(inc|corp|llc|ltd|org|foundation|company)\b/i.test(name)) {
> return 'org';
> }
> --- `src/entities/synthesis.ts`

> current.count += 1;
> current.evidence.add(mention.document.id);
> adjacency.set(related, current);
> --- `src/entities/synthesis.ts`

> const content = document.content.replace(/\s+/g, ' ').trim();
> if (!content) return `Referenced in ${document.id}`;
> return content.slice(0, 180);
> --- `src/entities/synthesis.ts`

#### EPI-RTE-question-rewrite
Label: Question evidence rewrite

Part of: [RT-RTE-outbound-filter](runtime.md#rt-rte-outbound-filter)

The deterministic helper consumes outgoing question text and up to two memory hits. It changes question marks to periods and appends snippets under an assertion that memory already contains relevant details. This isolates the previously uninspected semantic transformation from the container's search/cancellation route. SRC-1, `src/plugin/communication-protocol.ts`, `src/plugin/hooks/message-sending.ts`.

Concrete deduction: input `Where does Alice live?` plus a qualifying snippet `Alice likes tea.` becomes `Where does Alice live.` followed by `Memory already contains relevant details:` and `- Alice likes tea.`. The handler can return that content because no question mark remains. A nonempty search hit does not entail that the memory answers a residence question. The relevance statement is a non-entailed candidate; punctuation edits alone are policy transformations. If a hit's snippet contains a question mark recognized by containsQuestion, the handler instead requests cancellation. Thus cancellation is not a general semantic answer validator.

Software proposes/decides; the host must honor the result. There is no human veto or answer oracle inside the handler. Search threshold is an eligibility test in an open outbound workflow. Static communication rules shape the rewrite; no durable proposal/decision or automatic rollback is retained.

- Immediate return: Helper string, then handler content override or cancel request.
- Later read-back: Retained snippets are retrieved into this later sending invocation; the rewrite decision itself is not persisted here.
- Delegated visibility: Host sending channel receives the replacement, not an adjudicated answer/proof.
- Selection predicate: Enabled filter, question detection, nonempty hits above configured/default 0.35 threshold; at most two snippets.
- Invalidation or expiry: Recomputed per send; no retained acceptance state.
- Activation or effect: Can change proposed outgoing text or suppress its delivery if host applies hook; actual operation unobserved.
- Evidence limits: Deduction traces inspected text logic, not deployed execution; retrieval relevance and host enforcement are not guaranteed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const cleaned = originalContent.replace(/\?/g, ".").replace(/\s+\./g, ".").trim();
> --- `src/plugin/communication-protocol.ts`

> "Memory already contains relevant details:",
> ...topHits
> --- `src/plugin/communication-protocol.ts`

#### EPI-RTE-fixture-scoring
Label: Fixture observation scoring

Part of: [RT-RTE-autoresearch-change](runtime.md#rt-rte-autoresearch-change)

The benchmark's scoreFixtureObservations parses expected and actual Markdown, greedily matches important expected records to unused actual records by expected-token overlap, checks type equality/keyword presence and calculates weighted metrics. The fixture author supplies the answer oracle: expected observations, importance/type labels and keyword hints. This is a bounded fixture experiment domain, not an oracle for the world's truth or end-to-end host answers. The downstream development script owns keep/discard; this record owns only evidence production. SRC-1, `src/observer/benchmark/scoring.ts`; see the supplied container for the script consumer and its separate admission criterion.

A concrete implementation deduction challenges semantic-score interpretation: `Alice works at Acme` and `Alice does not work at Acme` lose stopword `not`, and have several identical tokens. Although works/work differ, expected-overlap matching can exceed default 0.35 and regard them as a match. An even stricter contrast, `Alice lives in Paris` versus `Alice lives not in Paris`, yields the same non-stopword set. Therefore matching cannot certify agreement on negation. It does compute the named token-domain metric correctly given its inputs; mathematical scoring does not establish reference truth, encoding fidelity or transport benefit. No observed fixture execution or causal comparison is claimed.

- Immediate return: Metrics, matches, missed-important/noise lists, keywords and rewrite flags.
- Later read-back: Benchmark reports/TSV can guide prescribed later development rounds; actual later agent use unobserved.
- Delegated visibility: Benchmark consumer receives symbolic scores/diagnostics; compressor provider receives fixture material upstream, not a truth certificate.
- Selection predicate: Parsed records, default overlap threshold 0.35, importance cutoff 0.5, greedy one-to-one matches and keyword rules.
- Invalidation or expiry: Recomputed for each run; edits to fixtures/scorer can change the measurement basis.
- Activation or effect: Provides implemented score signal to development admission; no demonstrated production behavioral effect.
- Evidence limits: Fixture oracle quality, observation parser fidelity and stored source-native result provenance not assessed. No independent test-set or component-effect inference.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return overlap / expectedTokens.size;
> --- `src/observer/benchmark/scoring.ts`

> 'updated', 'working', 'session', 'assistant', 'user'
> --- `src/observer/benchmark/scoring.ts`

> 'your', 'about', 'after', 'before', 'can', 'did', 'do', 'done', 'if', 'into', 'just', 'not', 'now',
> --- `src/observer/benchmark/scoring.ts`

> precision * 0.30 +
> recall * 0.35 +
> keywordPreservation * 0.20 +
> typeAccuracy * 0.15
> --- `src/observer/benchmark/scoring.ts`

#### EPI-RTE-replay-import
Label: Historical replay import

Replay is exposed by shipped CLI dispatch, normalizes four export families, filters/groups dates, supplies role-prefixed text to an Observer with threshold 1 and date-specific clock, flushes and runs reflection over the span. This is a distinct importer feeding [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) and [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week), not a duplicate of either. SRC-1, `src/commands/replay.ts`, `bin/register-maintenance-commands.js`.

Caller selects source/input/range and dry-run; software admits normalized messages and invokes downstream transformations without per-claim human approval. File/date validity checks are not truth tests and no answer oracle is consulted. Source warrant is unknown; the import is not production of new warranted knowledge. Source/transcript ID/timestamp accompany processMessages, but supplied noon timestamps/fallback dates and basename ID do not authenticate original utterance time or origin. No automatic rollback across all imported days/reflection is demonstrated.

- Immediate return: Completion/dry-run/no-messages console output or exception.
- Later read-back: Written observations/reflections can feed subsequent vault/recovery consumers via ordinary routes.
- Delegated visibility: Normalized message strings reach Observer and configured provider downstream; no host-agent delegation.
- Selection predicate: Supported source, existing input, normalizer file filters, optional lexical date range and grouping.
- Invalidation or expiry: Ordinary observer/reflection replacement/archive rules apply; importer itself establishes no content expiry or all-days rollback.
- Activation or effect: Historical content can be retained and consolidated; actual later reliance unobserved.
- Evidence limits: Four normalizers and downstream execution not inspected; exact preservation of export role/time/content remains unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await observer.processMessages(messages, {
> source,
> transcriptId: path.basename(resolvedInput),
> timestamp: nowForDate()
> });
> await observer.flush();
> --- `src/commands/replay.ts`

### Claims

#### EPI-CLM-memory-answer
Label: Memory informed communication

The shipped communication appendix instructs the host not to ask when memory contains the answer, while the helper emits a statement that memory contains relevant details. This is distinct from [RT-CLM-structured-memory](runtime.md#rt-clm-structured-memory): it concerns warrant for outgoing communication, not storage capacity; it complements the recall instruction [RT-OBJ-recall-mandate](runtime.md#rt-obj-recall-mandate). SRC-1, `src/plugin/communication-protocol.ts`, doctrine/design for the instruction and implementation for emitted text. Neither is observed compliance.

> "- Do not ask questions when memory already contains the answer.",
> "- Use memory tools proactively before answering memory-sensitive prompts."
> --- `src/plugin/communication-protocol.ts`
