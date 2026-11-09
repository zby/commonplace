---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MindBase epistemic routes: candidate synthesis, bounded evidence checks, maintenance writes and later reliance at c5273d2."
run-id: AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01
reviewed-boundary: c5273d2336c4d686df41c2a1495f14f085707f51
---

# MindBase epistemic report

## Source-and-claim boundary

The question is how MindBase acquires or produces truth-apt content, checks it, grants reliance and makes it consequential. The functional inclusions, external host/provider exclusions and frozen SRC-1 identity are those in the [boundary Source register](boundary.md#source-register). This is a complete repository artifact with a partially traced operational loop, not exhaustive evidence of every shipped route. No target code, tests, examples or providers were executed. All new implementation findings below concern SRC-1 at the reviewed commit; there is no registered observed run or causal experiment.

Public claims assessed are [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes), [EPI-CLM-wiki-audit](#epi-clm-wiki-audit), [EPI-CLM-sentence-pruning](#epi-clm-sentence-pruning) and [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds). The session hook's designation of context as curated truth is a reliance label, not an independently checked result: see [RT-BAP-session-context](runtime.md#rt-bap-session-context).

Coverage distinguishes direct source inspection in this job from provisional supplied findings. Paths in this table are SRC-1 commit-relative anchors, not new sources.

| Entry point or operation | Source path | Coverage and records | Limit or conclusion prevented |
|---|---|---|---|
| Ops contribute/build/research/ask | `apps/server/src/ops/runner.ts`, `apps/server/src/ops/recipes/build.ts`, `apps/server/src/ops/recipes/research.ts`, `apps/server/src/ops/gather.ts`, `schema/query.md` | Supplied [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer); direct recipe/gather reads and selected runner ranges | Individual output truth and model compliance unobserved; ask implementation itself used as supplied evidence |
| Ops lint quote gate | `apps/server/src/ops/runner.ts`, `apps/server/src/ops/gather.ts` | Direct verifyEvidence and runLint reads; [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes), part of [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings) | Occurrence does not establish conflict; input caps defeat a whole-wiki guarantee |
| CLI dispatch, ingest and lint | `apps/cli/src/index.ts`, `apps/cli/src/commands/ingest.ts`, `apps/cli/src/commands/lint.ts`, `packages/core/src/wiki/lint.ts` | Direct dispatch/caller reads; [EPI-RTE-cli-admission](#epi-rte-cli-admission) | CLI query/init/rebuild implementations not traced; compileL1 inspected only through its opening definitions, not its full planning/execution loop |
| MCP registered tools and health | `apps/mcp/src/tools/index.ts`, `apps/mcp/src/tools/run-wiki-health.ts`, `apps/mcp/src/tools/validate-structure.ts` | Direct registry, health and structure-tool reads; correction rechecked exact-name registration/dispatch and curator grants; [EPI-RTE-health-maintenance](#epi-rte-health-maintenance) | Registry enumeration is not implementation inspection of every tool |
| Server legacy health | `apps/server/src/routes/lint.ts`, `packages/core/src/compile/l2.ts`, `packages/core/src/compile/l2_prompts.ts`, `packages/core/src/tools/executor.ts`, `packages/core/src/graph/crosslinker.ts`, `schema/lint.md` | Direct health/L2/crosslink reads and selected executor methods; [EPI-RTE-health-maintenance](#epi-rte-health-maintenance) | Layout/store compatibility and complete behavior of every executor method unobserved |
| Topic synthesis and contradiction tool | `apps/server/src/lib/synthesis.ts`, `apps/server/src/routes/synthesize.ts`, `apps/mcp/src/lib/synthesis-runner.ts`, `apps/mcp/src/tools/find-contradictions.ts`, `packages/core/src/synthesis/prompts.ts`, `packages/core/src/synthesis/validate.ts` | Direct reads; [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) | Semantic checks weaker than sentence-support promise; other MCP synthesis callers not individually traced |
| Synthesis retention/recovery | `apps/server/src/lib/synthesis-cache.ts`, `apps/server/src/lib/synthesis-worker.ts` | Direct reads; [EPI-RTE-synthesis-cache](#epi-rte-synthesis-cache) | Mark-stale producers not exhaustively traced; no universal freshness guarantee |
| Contradiction probe and consumer | `packages/core/src/compile/contradiction-probe.ts`, `packages/core/src/analysis/cache.ts`, `packages/core/src/analysis/insights.ts`, `packages/core/src/analysis/suggestions.ts`, `apps/server/src/lib/analysis-scheduler.ts`, `apps/server/src/routes/analysis.ts` | Direct reads; [EPI-RTE-contradiction-probe](#epi-rte-contradiction-probe), [EPI-RTE-probe-consumption](#epi-rte-probe-consumption) | Cue-limited selection and clipped legacy note bodies; no measured accuracy or complete cache-invalidation audit |
| Plugin commands, agents and session hook | `apps/plugin/hooks/hooks.json`, `apps/plugin/agents/builder.md`, `apps/plugin/agents/curator.md`, `apps/plugin/hooks/session-start` | Direct hook registration and agent-text reads; session-start body via supplied [RT-BAP-session-context](runtime.md#rt-bap-session-context); [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build) | External host obedience and actual context isolation unobserved; curator grant names do not match registered health-tool names, so curator-to-health reachability is unestablished |
| Other material operations | `apps/server/src/lib/capture-worker.ts`, `apps/server/src/lib/classify-worker.ts`, `packages/core/src/brief/build.ts`, `packages/core/src/srs/extract.ts`, `packages/core/src/compile/l1.ts`, `apps/server/src/routes/answer-file-back.ts` | Unassessed here except limited CLI/L1 opening inspection; no inherited exhaustive finding | Prevent complete enumeration of acquisition, evaluation, acceptance, file-back and policy-adaptation routes |
| Other exposed paths and evaluators | `apps/mcp/src/tools/ingest-execute.ts`, `apps/mcp/src/prompts/index.ts`, `apps/mcp/src/resources/index.ts`, `apps/server/src/routes/tree/crud.ts`, `apps/server/src/routes/schema.ts`, `docs/testing-walkthrough.md`, `docs/manual-smoke-checklist.md` | Enumerated or supplied as remaining scope; not directly assessed here. Mobile/browser capture, other plugin agents, tests and CI also unassessed | Prevent system-complete negatives, uniform approval or source-warrant assertions, and evaluation-performance conclusions |

Requested answer filing (`apps/server/src/routes/answer-file-back.ts`, `packages/core/src/file-back/build-plan.ts`), editable schema instructions (`apps/server/src/routes/schema.ts`) and retained classification guidance (`apps/server/src/lib/classify-worker.ts`, `packages/core/src/classify/samples.ts`, `packages/core/src/classify/classify-note.ts`, `packages/core/src/classify/prompt.ts`) remain outside this member's declared route inventory. No complete filing/admission, instruction-edit, working-context, retained-authority or policy-adaptation comparison is claimed.

Missing user corpora prevent identifying actual propositions and their original warrant. Missing execution traces prevent identifying which implemented routes produced or checked any real retained page. Missing controlled comparisons prevent attributing improvement, compounding knowledge or model accuracy. Provider weights and host internals are excluded external responsibilities, not evidence of their absence. Supplied runtime findings remain valid scoped accounts; the health pipeline below adds a consequential route omitted there, rather than superseding the ops-lint finding.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](#epi-obj-source-text) | External/user assertions; actual propositions not determinable without corpus | Inputs | see record; SRC-1 `apps/server/src/ops/gather.ts` | Source identity labels are not source authentication |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Summaries, decisions, learnings, research claims and answers | Maintained knowledge | see record; SRC-1 `apps/server/src/ops/recipes/build.ts` | A truth label or write does not prove acceptance |
| [RT-OBJ-actions](runtime.md#rt-obj-actions) | None in command envelope; Markdown is a separately interpreted payload | Execute proposed changes | see record; SRC-1 `apps/server/src/ops/types.ts` | Schema admits command shape, not claim truth |
| [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | Topic summary, threads, headings, contradiction excerpts and gap suggestions | Synthesis and diagnosis | see record; SRC-1 `packages/core/src/synthesis/validate.ts` | Entailment and excerpt occurrence unverified |
| [EPI-OBJ-citation-fields](#epi-obj-citation-fields) | Symbolic pointers to possible support, not the support relation itself | Lineage/evidence hints | see record; SRC-1 `packages/core/src/synthesis/validate.ts` | Valid line coordinates need not support adjacent prose |
| [EPI-OBJ-probe-reason](#epi-obj-probe-reason) | Model's stated reason that two pages collide or agree | Factual collision diagnosis | see record; SRC-1 `packages/core/src/compile/contradiction-probe.ts` | A verdict can instead encode missing page or parse/provider error |
| [EPI-OBJ-probe-verdict](#epi-obj-probe-verdict) | Enum encoding a page-pair relation; error fallback is not a substantive judgment | Skip/review selector | see record; SRC-1 `packages/core/src/analysis/cache.ts` | ListConfirmed selects by enum, not reason quality |
| [EPI-OBJ-lint-prose](#epi-obj-lint-prose) | Claimed contradiction, stale claim, structural issue or gap | Review artifact prose | see record; SRC-1 `apps/server/src/ops/runner.ts` | Diagnosis not established by occurrence |
| [EPI-OBJ-lint-controls](#epi-obj-lint-controls) | None beyond encoded kinds and occurrence results | Finding admission/display controls | see record; SRC-1 `apps/server/src/ops/runner.ts` | Boolean verified concerns quote occurrence only |
| [EPI-OBJ-compile-plan](#epi-obj-compile-plan) | Proposed natural-language edits inside symbolic tool calls | CLI proposal and execution input | see record; SRC-1 `apps/cli/src/commands/ingest.ts` | Approval governs calls, not proposition truth; core internals only partially inspected |

## Authority-route ledger

This ledger splits content production, checks, disposition and retention even where one canonical route implements several functions. Architectural status here concerns inspected capacity, not observed operation. Other members own activation predicates, return/read-back details and authority paths where a cell says `see`. No row asserts observed acceptance or successful downstream use.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-research-page](runtime.md#rt-rte-research-page) | content transformation | implemented | [EPI-OBJ-source-text](#epi-obj-source-text) | truth-apt transformation: acquisition/import | Caller contribution or optional web text enters model-visible evidence | Caller/import and optional fetch; no source-authentication check established | see routes | Captured source or fetched/snippet text | Supplies candidate evidence | Source warrant unknown; labels retained but truth/authenticity not established | Can condition proposal generation | see routes | SRC-1 `apps/server/src/ops/runner.ts`; see routes | none | Acquisition is not new knowledge production | Source/capture extraction branches not exhaustively assessed |
| [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan) | content transformation | implemented | [EPI-OBJ-source-text](#epi-obj-source-text), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Source to candidate takeaways/Markdown | Model; source excerpts and project guidance | see route | Candidate plan | see route | Candidate synthesis only; preservation versus derivation versus addition unresolved | Propose actions | see route | SRC-1 `apps/server/src/ops/recipes/contribute.ts`; see route | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | none | No generated instance to classify |
| [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan) | disposition/acceptance | implemented | [RT-OBJ-actions](runtime.md#rt-obj-actions) | no content change | Proposed wiki actions | Schema, slug guards and caller indexes; UI offers human veto | see route | Selected or abandoned plan | Enforcing filtering | Operational admission, not a recorded evidence-consuming truth decision | Selected actions can write | see route | SRC-1 `apps/server/src/ops/runner.ts`; see route | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | Approval scope limited | Human rationale/criterion unobserved |
| [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Existing context and selected sources to Markdown | Model instructed to preserve truth/support; no independent semantic verdict | see routes | Rewritten context or research page | Candidate production | Acquired warrant unknown; semantic preservation not demonstrated | Generate executor payloads | see routes | SRC-1 `apps/server/src/ops/recipes/build.ts`, `apps/server/src/ops/recipes/research.ts` | [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds) | Truth not checked | Could reshape, derive or conjecture; actual outputs required |
| [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build) | retention | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Generated content to persisted files | Software shape/path/line constraints; hosted synthesis external | see routes | File writes or partial failures | Enforcing I/O constraints | Retention is not acceptance or post-acceptance integration | Future builds/questions/sessions can consume | see routes and [RT-BAP-session-context](runtime.md#rt-bap-session-context) | SRC-1 `apps/server/src/ops/executors.ts`; see routes | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | Direct-write alternatives | MCP writer implemented; hosted build sequence only afforded |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Retained content to answer model | Ranked selection and model file requests | see route | Delivered source blocks and answer | Advisory content | Retrieval licenses availability, not factual endorsement | Model can answer and mark new knowledge for auto-save | see route | SRC-1 `packages/core/src/qa/query.ts`; see route | [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds) | none | Citation instructions are not sentence checks |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Retrieved sources and question to answer | Model under citation and analysis guidance | see route | Answer, optional new-knowledge marker | Candidate generation | No checked entailment or novelty decision | Supplies user response and potential auto-save input | see route | SRC-1 `schema/query.md`; see route | [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds) | Marker does not prove novelty | No actual answer/source pair supplied |
| [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) | retention | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Answer marker to stored note | autoSave configuration and regex, not evidence comparator | see route | Saved answer or error | Permissive marker then write | No novel-claim acceptance established | Later retrieval can amplify unvalidated answer | see route | SRC-1 `apps/server/src/routes/ask.ts`; see route | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | New-knowledge label not warrant | No observed saved instance |
| [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) | content transformation | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | truth-apt transformation: indeterminate | Retrieved notes to synthesis | Model receives numbered source lines | see record | Structured candidate prose | Candidate generation | Requested source-bounded synthesis, not proven reshaping or entailment | Supplies validator input | see record | SRC-1 `apps/server/src/lib/synthesis.ts` | [EPI-CLM-sentence-pruning](#epi-clm-sentence-pruning) | none | No output instance or semantic check |
| [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) | check/evidence production | implemented | [EPI-OBJ-citation-fields](#epi-obj-citation-fields) | no content change | Citation slug and line range; optional inline marker syntax | Deterministic coordinates and regex; not entailment domain | see record | Valid/invalid coordinates and pruned content | Enforcing limited filter | Validity of pointers only | Feeds retained/displayed result | see record | SRC-1 `packages/core/src/synthesis/validate.ts` | [EPI-CLM-sentence-pruning](#epi-clm-sentence-pruning) | Conditional pruning | Concrete counterexample retained below |
| [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) | disposition/acceptance | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | no content change | Thread admission and contradiction/gap filtering | Code requires nonempty pruned content and at least one valid citation; other fields have weaker gates | see record | Kept/dropped thread; summary survives separately | Enforcing output filtering | Not evidence-consuming acceptance of the prose's truth | Admitted fields returned for caching/UI/tool consumers | see record | SRC-1 `packages/core/src/synthesis/validate.ts` | [EPI-CLM-sentence-pruning](#epi-clm-sentence-pruning) | Unsupported prose can survive | No accepted ampliative claim established |
| [EPI-RTE-synthesis-cache](#epi-rte-synthesis-cache) | retention | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose), [EPI-OBJ-citation-fields](#epi-obj-citation-fields) | no content change | Result to topic cache | Code after generation; no human per-result veto | see record | JSON persists | Enforcing write | Cached candidate, not accepted knowledge | Later endpoint/tool can reuse | see record | SRC-1 `apps/server/src/lib/synthesis-cache.ts` | none | none | Server and MCP cache implementations not presumed identical |
| [EPI-RTE-synthesis-cache](#epi-rte-synthesis-cache) | lineage/freshness/recovery | implemented | [EPI-OBJ-citation-fields](#epi-obj-citation-fields) | no content change | Source hashes, reverse index and stale set | Code regeneration; cache read itself does not check hashes | see record | Regenerate or clear failed stale job | Scheduling and reuse | Freshness metadata, not truth validation | Cached result may be served pending refresh | see record | SRC-1 `apps/server/src/lib/synthesis-worker.ts` | none | Refresh not endorsement | Stale producers not fully audited |
| [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes) | check/evidence production | implemented | [EPI-OBJ-lint-findings](#epi-obj-lint-findings) | no content change | Claimed quote occurrence in files | Normalized substring check | see record | Per-item verified booleans | Produces gate inputs | Occurrence only; no logical collision license | Makes findings eligible for retention | see record | SRC-1 `apps/server/src/ops/runner.ts` | [EPI-CLM-wiki-audit](#epi-clm-wiki-audit) | Count is not semantic proof | Duplicate evidence not made independent |
| [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes) | disposition/acceptance | implemented | [EPI-OBJ-lint-findings](#epi-obj-lint-findings) | no content change | Contradiction/stale finding retention | Count at least two/one verified items respectively | see record | Kept or dropped finding | Enforcing diagnosis filter | Accepts occurrence threshold for review, not truth of conflict | Parent stores eligible findings; human may dismiss | see record and [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings) | SRC-1 `apps/server/src/ops/runner.ts` | [EPI-CLM-wiki-audit](#epi-clm-wiki-audit) | Exactness qualified | No checked distinct-page requirement |
| [EPI-RTE-contradiction-probe](#epi-rte-contradiction-probe) | check/evidence production | implemented | [EPI-OBJ-probe-reason](#epi-obj-probe-reason), [EPI-OBJ-probe-verdict](#epi-obj-probe-verdict) | truth-apt transformation: indeterminate | Specific factual collision between two page excerpts | Model judge with defined three-way rubric | see record | contradicts/compatible/unrelated, including error fallback | Diagnostic output | Model opinion within excerpt domain; not independent ground truth | Supplies cached verdict | see record | SRC-1 `packages/core/src/compile/contradiction-probe.ts` | [EPI-CLM-wiki-audit](#epi-clm-wiki-audit) | Errors collapse to unrelated | No expected-answer oracle or measured calibration |
| [EPI-RTE-contradiction-probe](#epi-rte-contradiction-probe) | retention | implemented | [EPI-OBJ-probe-verdict](#epi-obj-probe-verdict), [EPI-OBJ-probe-reason](#epi-obj-probe-reason) | no content change | Verdict to SQL cache | Any returned enum, including fallback | see record | Stored result suppresses matching future judge call | Enforcing cache skip | Caching grants no added warrant | Matching pair/model/prompt reused | see record | SRC-1 `packages/core/src/analysis/cache.ts` | none | No body hash in lookup | Other invalidation paths not exhaustively assessed |
| [EPI-RTE-probe-consumption](#epi-rte-probe-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-probe-verdict](#epi-obj-probe-verdict) | no content change | Cached enum to high-severity review suggestion | SQL verdict filter and fixed suggestion rule | see record | Contradiction flagged for user review | Ranking/advisory, not automatic factual resolution | UI category is stronger wording than model-only warrant | Prioritizes review suggestions, no compelled correction | see record | SRC-1 `packages/core/src/analysis/insights.ts` | [EPI-CLM-wiki-audit](#epi-clm-wiki-audit) | Confirmed is a cache label | Can include other model/prompt rows; no current-key filter in listConfirmed |
| [EPI-RTE-health-maintenance](#epi-rte-health-maintenance) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Health overview to model-proposed text repairs | L2 model sees summaries/index/structural issues, not every full page | see record | Rewrite, append, summary or other supported action | Direct executor dispatch | Candidate repair, no demonstrated semantic improvement | Changes files subject to handler checks | see record | SRC-1 `packages/core/src/compile/l2.ts` | [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds) | Health API writes; curator mapping unresolved | Proposed content may replace rather than preserve meaning |
| [EPI-RTE-health-maintenance](#epi-rte-health-maintenance) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Parsed L2 actions to handlers | Code dispatch; human_touched veto for inspected rewrite/update handlers | see record | Writes, handler rejection, or return-only flags/merge | Enforcing code checks, no semantic approval | Neither flag success nor queued label establishes resolved knowledge | Later consumers see successful writes, not a validated repair certificate | see record | SRC-1 `packages/core/src/tools/executor.ts` | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | Registered API writes; curator grant differs | No pipeline transaction/rollback established |
| [EPI-RTE-health-maintenance](#epi-rte-health-maintenance) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Exact-title mention to wikilink | Fixed title match and score threshold | see record | Existing words linked | Enforcing auto-mode edit | Pointer insertion only; identity of referent remains heuristic | Alters future navigable graph | see record | SRC-1 `packages/core/src/graph/crosslinker.ts` | none | Extracted does not mean semantically verified | Does not warrant title disambiguation |
| [EPI-RTE-cli-admission](#epi-rte-cli-admission) | disposition/acceptance | implemented | [EPI-OBJ-compile-plan](#epi-obj-compile-plan) | no content change | CLI compile plan to execution | Human all-or-nothing prompt or --yes bypass; distinct from ops envelopes | see record | Aborted or all actions forwarded | Enforcing caller checkpoint | Approval is permission, not evidence of truth | Calls compileL1Execute | see record | SRC-1 `apps/cli/src/commands/ingest.ts` | [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | --yes alternative | Core planning/execution loop not fully inspected |

No post-acceptance lifecycle-integration route is established in these traces: operational writes, links and retrieval occur, but an evidence-consuming acceptance decision for a produced claim was not found in these inspected pipelines. This is a route-bounded finding, not a system-complete negative. No formal derivation route from warranted premises is established here. Failure to establish entailment does not classify all synthesis as ampliative conjecture.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [EPI-RTE-health-maintenance](#epi-rte-health-maintenance), [EPI-RTE-cli-admission](#epi-rte-cli-admission) | None supplied | No intervention/comparison | Selected UI path affords human selection; several alternate write paths do not require per-content approval | Universal wording unsupported; approval still would not establish warrant |
| [EPI-CLM-wiki-audit](#epi-clm-wiki-audit) | see record | SRC-1 `README.md`; doctrine/design | Recipes and curator request diagnosis | [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings), [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes), [EPI-RTE-contradiction-probe](#epi-rte-contradiction-probe), [EPI-RTE-probe-consumption](#epi-rte-probe-consumption) | None supplied | Neither excerpt checks nor returned categories establish diagnostic accuracy | Implemented bounded auditing with quote-occurrence gate and separate model-judge review path | Whole-wiki/exact-conflict guarantee exceeds caps, normalization and count-only gate |
| [EPI-CLM-sentence-pruning](#epi-clm-sentence-pruning) | see record | SRC-1 `packages/core/src/synthesis/prompts.ts`; doctrine/design | Explicit every-sentence support requirement | [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) | None supplied | Deterministic input trace disproves universal pruning; not a model performance test | Valid reference coordinates can accompany unsupported prose | Citation-free content is preserved if its thread has valid citation metadata |
| [EPI-CLM-knowledge-compounds](#epi-clm-knowledge-compounds) | see record | SRC-1 `README.md`; doctrine/design | Build requests preservation and contradiction flags; query asks for source-supported analysis | [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [RT-BAP-session-context](runtime.md#rt-bap-session-context), [EPI-RTE-synthesis-cache](#epi-rte-synthesis-cache) | None supplied | No quality baseline, longitudinal corpus or comparison | Persistent material has routes to later models; accumulation and reuse are implemented capacities | Progressively sharper/compounding knowledge remains unestablished, not refuted by mere absence of runs |

## Bounded conclusion

MindBase has multiple routes from user/source text to retained, behaviorally consequential prose. The inspected system imports sources, selects excerpts, requests synthesis and answers, writes context/research pages and can reload them in builds, questions and sessions. Source warrant is unknown: paths and citations preserve some lineage pointers but do not authenticate content or establish that transformations preserve meaning. See [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) and [RT-BAP-session-context](runtime.md#rt-bap-session-context).

The implemented checks have different licenses. JSON schemas license command execution; citation coordinates license valid pointers; normalized quote matches license occurrence claims; a model judge supplies a bounded opinion about a pair of excerpts. None establishes a source-backed accepted ampliative proposition merely by retaining or displaying its result. The quote gate can reject fabricated quotations and the synthesis validator can reject invalid line coordinates: these are real checks, not grounds for treating every retained statement as unverified in every respect. Their missing semantic entailment checks remain consequential. See [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis) and [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes).

Operational authority is stronger than epistemic warrant in several places. Build/research and marker-triggered answer saving can persist candidates without a content-specific human decision. The registered L2 health API can directly rewrite knowledge; handler checks can veto some edits, while flag/merge success can be return-only. The curator grants and requests `mindbase_run_wiki_health`, whereas the MCP server registers `run_wiki_health` and dispatches by exact name. No inspected mapping connects those names, so the curator-to-writer path is unestablished; this mismatch is not a host-safety guarantee. Cached model verdicts influence which issues rank as high-priority review, without forcing a correction or proving a collision. These distinctions follow [EPI-RTE-health-maintenance](#epi-rte-health-maintenance), [EPI-RTE-probe-consumption](#epi-rte-probe-consumption) and the supplied runtime routes, not an inference from the word knowledge.

No produced accepted ampliative claim, warranted formal derivation or post-acceptance integration instance is established within these inspected routes. Without actual source/output pairs, model semantic updates remain indeterminate between reshaping, entailed derivation and conjecture. The deterministic crosslink example is bounded non-ampliative reshaping, not new factual knowledge. Other included but unassessed mechanisms prevent a complete system negative.

Persistent updates and advisory delivery afford later behavior changes, not demonstrated learning. No improvement comparison establishes improved future capacity. The code does not update provider parameters through these inference routes; endpoint/version uncertainty remains as stated in [RT-CMP-model](runtime.md#rt-cmp-model). Auditing a wiki is not by itself reflection about the system's operating method. Model-owned proposals and software progression establish computational roles independently of correctness; human veto exists in some routes, not all. No exercised self-improvement attribution or autonomous theory-builder verdict follows from these findings. Source-native project rules guide future proposals through [RT-BAP-project-rules](runtime.md#rt-bap-project-rules), but content-directed criticism and iterative revision of those method rules were not established by this bounded trace.

## Shared records

### Operative objects

#### EPI-OBJ-source-text
Label: Contributor and retrieved source text

SRC-1, `apps/server/src/ops/gather.ts`, `apps/server/src/ops/recipes/research.ts`. Natural-language text on project files or supplied search results, temporarily selected into model inputs. Distinct from [RT-OBJ-actions](runtime.md#rt-obj-actions): it is input evidence, not a command envelope. Source propositions and warrant are corpus-dependent and not determinable here. Supplied [RT-RTE-research-page](runtime.md#rt-rte-research-page) covers acquisition of optional web results; this is not a new acquisition route declaration.

> const MAX_SOURCE_FILES = 30;
> const MAX_SOURCE_CHARS = 4_000;
> --- `apps/server/src/ops/gather.ts`

> const fresh = withM.filter((f) => f.mtime > contextMtime).sort((a, b) => b.mtime - a.mtime).slice(0, MAX_SOURCE_FILES);
> --- `apps/server/src/ops/gather.ts`

#### EPI-OBJ-wiki-pages
Label: Context and wiki page prose

SRC-1, `apps/server/src/ops/recipes/build.ts`, `packages/core/src/tools/executor.ts`. Natural-language context/research/legacy page bodies on project storage, interpreted by later models or humans. Distinct from [RT-OBJ-actions](runtime.md#rt-obj-actions), which identifies transient command envelopes, not the retained corpus; not a part of that envelope. Existing routes cover writes/read-back rather than declaring this corpus object. Actual claim truth is unobserved.

> preserve still-true
> content; flag contradictions between sources explicitly with ⚠️.
> --- `apps/server/src/ops/recipes/build.ts`

> await this.store.writeText(mdPath, `# ${meta.title}\n\n${newContent}\n`);
> --- `packages/core/src/tools/executor.ts`

#### EPI-OBJ-synthesis-prose
Label: Synthesis prose fields

SRC-1, `packages/core/src/synthesis/validate.ts`. Natural-language summary, thread headings/content, contradiction excerpts/explanations and gap suggestions inside transient structured results and cached JSON. Symbolic references have separate identity in [EPI-OBJ-citation-fields](#epi-obj-citation-fields). No counterpart among supplied runtime objects: these are topic-synthesis outputs, not ops action envelopes. Their validation criteria differ by field; summary is passed through, contradiction excerpt occurrence is not checked.

> return { summary: raw.summary ?? '', threads, contradictions, gaps };
> --- `packages/core/src/synthesis/validate.ts`

#### EPI-OBJ-citation-fields
Label: Synthesis citation coordinates

SRC-1, `packages/core/src/synthesis/validate.ts`, `apps/server/src/lib/synthesis.ts`. Symbolic slug/line_range fields, inline marker strings and source_hashes in parsed/cached JSON. Fixed code uses coordinates to filter and hashes as lineage metadata. Distinct from supplied [RT-OBJ-actions](runtime.md#rt-obj-actions): citation metadata rather than execution commands. These are not a warrant-bearing interpretation of source text.

> const [start, end] = c.line_range;
>   if (!Number.isInteger(start) || !Number.isInteger(end)) return false;
>   if (start < 1 || end > lines.length || start > end) return false;
>   return true;
> --- `packages/core/src/synthesis/validate.ts`

#### EPI-OBJ-probe-reason
Label: Contradiction probe reason

SRC-1, `packages/core/src/compile/contradiction-probe.ts`, `packages/core/src/analysis/cache.ts`. Natural-language model explanation or program-created failure reason, transient then SQL text. Distinct from [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings): a separate legacy-page judge pipeline. The sibling enum has a distinct fixed consumer in [EPI-OBJ-probe-verdict](#epi-obj-probe-verdict).

> catch { return { verdict: 'unrelated', reason: 'page A not found' }; }
> --- `packages/core/src/compile/contradiction-probe.ts`

#### EPI-OBJ-probe-verdict
Label: Contradiction probe verdict

SRC-1, `packages/core/src/compile/contradiction-probe.ts`, `packages/core/src/analysis/cache.ts`. Symbolic three-way enum in memory and SQLite contradiction_cache; fixed code selects contradicts for review and skips cached pairs. Distinct from ops lint findings and ops command envelopes. Its apparent factual meaning can instead arise from an error fallback.

> export type Verdict = 'contradicts' | 'compatible' | 'unrelated';
> --- `packages/core/src/compile/contradiction-probe.ts`

#### EPI-OBJ-lint-findings
Label: Stored ops lint findings

Part of: [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings)

The parent is a route; this object is its retained diagnostic artifact, not a competing route identity. SRC-1, `apps/server/src/ops/runner.ts`. Natural-language diagnoses and quote text have human/model interpretation; symbolic kinds, evidence verified flags and dismissed state drive filtering/display. Stored as dated JSON. These parts are distinguished by their consumers in [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes) and the parent route: verified counts govern retention, dismissal governs later presentation, and prose communicates the proposed issue. No truth decision is encoded merely by verified=true.

> const artifact: LintArtifact = { date, findings, dropped };
> --- `apps/server/src/ops/runner.ts`

#### EPI-OBJ-lint-prose
Label: Ops lint diagnosis and quote prose

Part of: [EPI-OBJ-lint-findings](#epi-obj-lint-findings)

SRC-1, `apps/server/src/ops/runner.ts`. Natural-language diagnosis text and evidence quotations within the parent's dated JSON artifact. Human/model interpretation supplies their meaning. Distinct part from fixed-rule controls: evidence quote strings are normalized and matched by code, but that match assesses occurrence, not the diagnosis. Supporting passage is the verifyEvidence quotation in [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes), which preserves page/quote fields alongside the computed flag.

#### EPI-OBJ-lint-controls
Label: Ops lint kinds and verification flags

Part of: [EPI-OBJ-lint-findings](#epi-obj-lint-findings)

SRC-1, `apps/server/src/ops/runner.ts`. Symbolic kind, per-evidence verified flag, ID and dismissed state in the same dated JSON. Fixed code uses verified-item counts for admission and dismissal for later presentation, unlike the diagnosis prose's interpreted meaning. The parent [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings) supplies dismissal/read-back evidence; [EPI-RTE-evidence-quotes](#epi-rte-evidence-quotes) supplies the exact flag/count passages. This is a part declaration, not a competing finding-retention route.

#### EPI-OBJ-compile-plan
Label: CLI compile proposal tool calls

SRC-1, `apps/cli/src/commands/ingest.ts`. Transient plan.proposed entries carry symbolic tool-call names and argument keys plus natural-language names/Markdown edit payloads. Fixed CLI code displays call names and titles and forwards the plan to execution after batch approval. The quoted caller establishes this mixed command object; it does not establish semantic checks on text arguments. Distinct from [RT-OBJ-actions](runtime.md#rt-obj-actions): separate core compiler plan used by CLI, not ops' Zod action union or pending-plan map. No persistence of the pending CLI plan is established.

> for (const a of plan.proposed) {
>         const args = a.call.arguments as Record<string, unknown>;
>         const title = (args['name'] ?? args['concept_name'] ?? args['from'] ?? '?') as string;
>         out.info(`  ${a.call.name}  ${title}`);
>       }
> --- `apps/cli/src/commands/ingest.ts`

### Routes

#### EPI-RTE-topic-synthesis
Label: Topic synthesis and field admission

SRC-1, `apps/server/src/lib/synthesis.ts`, `apps/mcp/src/lib/synthesis-runner.ts`, `packages/core/src/synthesis/prompts.ts`, `packages/core/src/synthesis/validate.ts`. Server runSynthesis or MCP runSynthesisMCP selects up to twenty notes, builds a numbered-source prompt, collects model JSON and calls validateSynthesis. Server uses hybrid retrieval; MCP uses keyword retrieval. Both reconstruct legacy wiki/notes paths from hits, skipping unreadable notes; do not infer equivalent v2 coverage. Distinct from [RT-RTE-research-page](runtime.md#rt-rte-research-page): structured topic-result pipeline, not ops research actions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured summary, threads, contradictions, gaps, model identity and source hashes; empty output when no notes or unparseable response.
- Later read-back: Caller cache writes allow later topic/tool invocations to reuse the result; see the distinct cache route.
- Delegated visibility: inapplicable — completion calls, not worker-agent delegation.
- Selection predicate: Up to twenty search hits; only successfully loaded legacy note bodies enter the source map. A thread requires at least one valid citation and nonempty content after optional pruning.
- Invalidation or expiry: inapplicable — generation/validation itself has no retained state; caller owns cache lifecycle.
- Activation or effect: Model proposes prose; fixed code drops invalid coordinates and some threads/sentences; admitted result can be displayed or cached. Behavioral dependence is not observed.
- Evidence limits: No executed synthesis or semantic support comparator; malformed shapes beyond the expected interfaces can throw. Source hashes identify bodies, not truth.

Admission mode is an open topic request or scheduled refresh. The model proposes; software vetoes structurally inadequate thread references, unknown contradiction slugs/confidence values and gap references. There is no per-thread human approval or expected-answer oracle. guidance requests source-bounded synthesis; no persisted criticism-to-theory loop is established. Parse failure returns empty fields; code does not independently decide whether a surviving claim follows from sources.

> const validCitations = (t.citations ?? []).filter((c) => citationValid(c, sources));
>     if (validCitations.length === 0) continue;
>     const prunedContent = pruneUncitedSentences(t.content ?? '');
>     if (!prunedContent) continue;
> --- `packages/core/src/synthesis/validate.ts`

> if (!INLINE_CITE_RE.test(content)) return content.trim();
> --- `packages/core/src/synthesis/validate.ts`

> if (!c.with_slug || !sources.has(c.with_slug)) continue;
>     if (c.confidence !== 'low' && c.confidence !== 'medium' && c.confidence !== 'high') continue;
> --- `packages/core/src/synthesis/validate.ts`

Concrete implementation deduction, without execution: take source map `a → ["The sensor is blue."]` and a thread with heading `Claim`, content `The moon is cheese.`, citations `[{slug:"a",line_range:[1,1]}]`. citationValid finds source a and integer range 1..1 within its one line. There is no inline marker, so pruneUncitedSentences returns the entire trimmed content. Both thread-admission tests pass and the unrelated sentence survives. The same path also preserves a genuinely supported citation-free sentence; lack of inline markers cannot alone determine falsity. This falsifies universal sentence pruning, not model reliability measured on a corpus. When markers do occur, regex presence rather than semantic support decides which sentence fragments survive.

#### EPI-RTE-synthesis-cache
Label: Server synthesis cache and refresh

SRC-1, `apps/server/src/routes/synthesize.ts`, `apps/server/src/lib/synthesis-cache.ts`, `apps/server/src/lib/synthesis-worker.ts`. Server owns JSON persistence, reverse source index, stale set, cached SSE replay and serial regeneration. No counterpart in supplied runtime routes: this is not ops research persistence or answer auto-save. MCP find_contradictions similarly calls its cache before generation, but the detailed server cache semantics here are not silently attributed to the separate MCP cache implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE meta, thread, gap and contradiction events, then done, or error. The MCP contradiction tool returns contradiction fields from cached/generated structured synthesis.
- Later read-back: Non-forced server topic request directly replays cached fields; MCP find_contradictions returns cached contradictions when present.
- Delegated visibility: inapplicable — server worker invokes runSynthesis serially, not an agent.
- Selection predicate: Normalized topic key; reverse index maps source slugs to cached topics. Server cache hit unless force; worker selects first stale key.
- Invalidation or expiry: markStaleFor adds reverse-index topics to a set; worker polls every five seconds. Cache read does not itself compare source hashes or exclude stale keys. Worker clears stale entry after success and after caught failure.
- Activation or effect: Reuses or replaces stored candidate results and influences what a later requester sees; no observed accuracy improvement.
- Evidence limits: Mutation callers of markStaleFor not exhaustively traced; no assertion that every source edit marks every affected topic. A cache hit is not a fresh evaluation.

Owner is software; model proposes replacement content during refresh. Rejection uses the generator's parsing/filtering behavior, not a human decision. Failed refresh clears its stale queue entry to avoid retries; no automatic semantic rollback or acceptance gate was found in these files.

> const cached = await ctx.synthesisCache.readSynthesis(key);
>         if (cached) {
> --- `apps/server/src/routes/synthesize.ts`

> const result = await runSynthesis(this.ctx, key);
>       await this.ctx.synthesisCache.writeSynthesis(key, result);
>       await this.ctx.synthesisCache.clearStale(key);
> --- `apps/server/src/lib/synthesis-worker.ts`

> console.warn(`[synthesis-worker] regen failed for ${key}:`, (e as Error).message);
>       await this.ctx.synthesisCache.clearStale(key);
> --- `apps/server/src/lib/synthesis-worker.ts`

#### EPI-RTE-evidence-quotes
Label: Lint evidence quote verification

Part of: [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings)

SRC-1, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/gather.ts`. This is the parent's specific check-and-filter subroute, not a duplicate declaration of its full diagnosis/retention loop. Code resolves model page labels to files, normalizes bodies and quotes, counts matching evidence items and drops insufficient contradiction/stale findings. The check target is quotation occurrence, not factual inconsistency. In particular two items need not refer to different pages or independent passages.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Kept findings with per-item verified flags and a dropped count.
- Later read-back: Parent stores those findings in dated artifacts; later fetch/dismiss is as in the parent route, not a new knowledge-revision consumer.
- Delegated visibility: inapplicable — local code after a completion, not agent delegation.
- Selection predicate: All proposed evidence entries; contradiction needs at least two verified entries, stale at least one; other model kinds do not have this count gate.
- Invalidation or expiry: Parent overwrites same-day artifact; this gate reads current files with a per-call body cache, not a historical source snapshot.
- Activation or effect: Can reject findings from retention; it does not change the underlying page, decide which claim is true or require two distinct pages.
- Evidence limits: Normalization changes exactness; substring occurrence does not prove that the quote supports the diagnosis or that the model saw all relevant content.

The model proposes semantic findings; software can veto evidence-insufficient items; human dismissal is later and not required for admission. The reference is current page text, not an expected answer to the semantic question. No answer oracle or closed automatic correction follows from this gate.

> const normalizeQuote = (s: string): string => s.toLowerCase().replace(/[*_`]/g, '').replace(/\s+/g, ' ').trim();
> --- `apps/server/src/ops/runner.ts`

> return { page: e.page, quote: e.quote, verified: haystack !== null && haystack.includes(normalizeQuote(e.quote)) };
> --- `apps/server/src/ops/runner.ts`

> const verifiedCount = evidence?.filter((e) => e.verified).length ?? 0;
>     if (need !== undefined && verifiedCount < need) {
>       dropped += 1;
>       continue;
>     }
> --- `apps/server/src/ops/runner.ts`


Concrete implementation deduction: for an existing page containing `Water is wet.`, two evidence entries with that same page and quote each receive verified=true. A contradiction finding carrying both reaches count two and is kept. This shows lack of an independent-page or semantic-conflict test; it does not claim any deployed model produced that input.

#### EPI-RTE-contradiction-probe
Label: Cue-selected contradiction judgment and cache

SRC-1, `packages/core/src/compile/contradiction-probe.ts`, `packages/core/src/analysis/cache.ts`, `apps/server/src/lib/analysis-scheduler.ts`, `apps/server/src/routes/analysis.ts`. Distinct from [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings) and its quote subroute: a separate scheduled/manual legacy-page judge with SQL verdict storage. Scheduler starts a first delayed probe and periodic daily probes; manual recompute calls it too. Code selects unique existing-page pairs from contrast cues before wikilinks. Model judges first 4,000 characters from each hardcoded wiki/notes path against a specific factual-collision rubric.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: judged and cached counts; each judge returns verdict and reason.
- Later read-back: Matching slug pair/model/prompt cache entry suppresses later judgment; listConfirmed feeds the distinct insights consumer.
- Delegated visibility: inapplicable — local completion and cache, not sub-agent.
- Selection predicate: Contrast-cue regex, existing target in index, non-self unique pair, default maximum twenty; skip when the pair/model/prompt key already exists.
- Invalidation or expiry: Lookup has no body hash or age cutoff. Other deletion/invalidation paths are not exhaustively inspected, so no global permanence claim is made.
- Activation or effect: Produces a diagnostic verdict and persists all returned enums, including fallback unrelated results; matching cached result blocks reevaluation in this loop.
- Evidence limits: Cue selection misses other conflicts; hardcoded legacy paths can fail for indexed pages elsewhere. Verdict parsing and fallback are not external truth checks; no observed accuracy or calibration.

Diagnosis mode is scheduled bounded candidate evaluation or manual recompute. Software chooses pairs and validates enum; the model proposes/decides semantic classification without per-pair human approval. Missing pages, malformed JSON, adapter exceptions and invalid enums yield unrelated with program-generated reason. No expected-answer oracle. The intended criterion is opposing factual assertions about the same subject, for user review over excerpts; no statement that the system knows which assertion is correct is licensed.

> Be strict — only return "contradicts" if there is a specific factual collision you can point at.`;
> --- `packages/core/src/compile/contradiction-probe.ts`

> const A = bodyA.slice(0, 4000);
>   const B = bodyB.slice(0, 4000);
> --- `packages/core/src/compile/contradiction-probe.ts`

> if (existing) { cached++; continue; }
> --- `packages/core/src/compile/contradiction-probe.ts`

> WHERE slug_a = ? AND slug_b = ? AND model_id = ? AND prompt_version = ?
> --- `packages/core/src/analysis/cache.ts`

#### EPI-RTE-probe-consumption
Label: Cached contradictions to review suggestions

SRC-1, `packages/core/src/analysis/insights.ts`, `packages/core/src/analysis/cache.ts`, `packages/core/src/analysis/suggestions.ts`, `apps/server/src/routes/analysis.ts`. Owner: deterministic analysis code. Endpoints are cached verdicts → listConfirmed → AnalysisInsights/analysis cache → insights API. Distinct from all supplied runtime records and from the judge producer: it consumes rather than evaluates a pair. The consumer does not inspect model reasons to establish factual correctness and does not resolve conflicts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unified insight payload, including contradiction pairs/reasons and ranked suggestions.
- Later read-back: Derived suggestions persist in analysis cache; future analysis can reread verdicts. User-visible response is an advisory review cue, not a knowledge rewrite.
- Delegated visibility: inapplicable — no model delegation in this consumer.
- Selection predicate: SQL verdict equals contradicts, without current model/prompt filter; suggestions label contradictions high severity and cap sorted output at default five.
- Invalidation or expiry: Derived insights recompute; source-verdict freshness limitations remain those of the producer/cache. No invalidation of factual claims is implemented by generating a suggestion.
- Activation or effect: Promotes selected cached results into high-severity suggestions; future human review is possible, not enforced or observed.
- Evidence limits: No downstream accepted correction or observed human action; cached confirmed wording is not a new check.

Behavioral-authority path: insights API/UI caller receives fixed-wording suggestions, ranked ahead of lower-severity issues; advisory horizon lasts through cache reuse/recomputation and human review. Software selects the enum; a human can ignore it. No answer oracle, proposal admission or automatic repair exists in this consumer.

> WHERE verdict = 'contradicts'
>       ORDER BY computed_at DESC
> --- `packages/core/src/analysis/cache.ts`

> message: `[[${c.slugA}]] and [[${c.slugB}]] contain contradictory claims — review which is correct.`,
>       actionable: { slugs: [c.slugA, c.slugB] },
>       severity: 'high',
> --- `packages/core/src/analysis/suggestions.ts`

#### EPI-RTE-health-maintenance
Label: Health pipeline crosslink and L2 writes

SRC-1, `apps/mcp/src/tools/run-wiki-health.ts`, `apps/server/src/routes/lint.ts`, `packages/core/src/compile/l2.ts`, `packages/core/src/compile/l2_prompts.ts`, `packages/core/src/graph/crosslinker.ts`, `packages/core/src/tools/executor.ts`, `schema/lint.md`, `apps/plugin/agents/curator.md`, `apps/mcp/src/tools/index.ts`. Distinct from [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings), whose ops endpoint stores findings without rewriting knowledge. This health pipeline writes an insights page, performs automatic crosslinking, then sends a wiki overview to an L2 model and directly dispatches parsed actions to ToolExecutor. It adds an omitted consequential maintenance route; it does not supersede the valid narrower ops finding. The curator is instructed to be read-only and grants `mcp__mb__mindbase_run_wiki_health`, with process text requesting `mindbase_run_wiki_health`. The registered API is instead `run_wiki_health`, and the MCP dispatcher uses exact-name lookup. No inspected mapping establishes curator access to this writer. The API's independent write behavior remains supported; neither curator reachability nor host safety follows from the mismatched names.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP health metrics, crosslink and L2 action counts; server legacy lint SSE progress/results. Individual executor outcomes can include failure even when compileL2 returns ok=true.
- Later read-back: Successful writes to wiki bodies, summaries/index and insights can enter future search, compilation or display; actual read-back activation not observed. flag_contradiction and merge handlers inspected here return flags/status without storing a resolution or merge.
- Delegated visibility: uninspected — external host controls agent execution and tool-name exposure; the curator's prefixed health grant does not match the registered API name, and no mapping was established. Independently, the registered API performs internal L2 model work and I/O.
- Selection predicate: Graph exact-title mentions outside code/frontmatter detection feed crosslinks; exact-title score starts at six and auto mode applies extracted links. L2 gets index, one-liners, metadata and structural issues; actions come from parsed JSON array, not a per-action human checklist.
- Invalidation or expiry: Reindex follows MCP health; server reindexes on lint.ok. No pipeline-wide transaction or automatic content rollback is established in inspected orchestration. rewrite/update checks can reject human_touched pages; no equivalence asserted for every handler.
- Activation or effect: Auto crosslinks write Markdown. L2 can replace/append prose and change summaries through registered handlers. No expected-answer or semantic truth gate precedes dispatch.
- Evidence limits: No successful execution, layout compatibility test or measured improvement; not every executor method inspected. Tool return counts do not establish that all actions succeeded, nor that return-only flags affected later behavior.

Admission mode is a user/host health request. Fixed code proposes exact-title links; L2 proposes repairs under schema/lint guidance. Software selects/dispatches, with argument/path/state checks in handlers; no human per-action approval in these wrappers. Human_touched metadata supplies a software veto in the inspected rewrite/update handlers, not a general human truth decision. Failed operations can leave earlier effects; no rollback implementation was inspected in this path. What persists is changed wiki content/metadata/index and insights, not an evidenced accepted theory or its criticism history.

Concrete crosslink deduction: with indexed target title `Alpha`, a page body `Alpha is useful.` and no existing edge, titlePattern matches; score begins at six, so confidence becomes extracted. In auto mode replaceFirstOutsideCode yields `[[Alpha]] is useful.` and the changed page is written. This changes navigation without establishing a new factual proposition. It does not establish that every occurrence of a title refers to that indexed entity.

> const xlink = await crossLink(ctx.store, { mode: 'auto' });
>     const adapter = ctx.getAdapter();
>     const lint = await compileL2({ adapter, store: ctx.store, model: ctx.config.model });
> --- `apps/mcp/src/tools/run-wiki-health.ts`

> const call = actionToToolCall(action, i);
>     const result = await executor.execute(call);
>     toolResults.push({ call, result });
> --- `packages/core/src/compile/l2.ts`

> if (meta.edit_state === 'human_touched') {
>       return { ok: false, error: `concept ${slug} is human_touched, skipping rewrite` };
>     }
> --- `packages/core/src/tools/executor.ts`

> result: { slug_a: args.slug_a, slug_b: args.slug_b, flagged: true },
> --- `packages/core/src/tools/executor.ts`

> result: { keep: args.keep, absorb: args.absorb, status: 'queued_for_review' },
> --- `packages/core/src/tools/executor.ts`

> let score = 6; // exact title match (+6 per plan, guarantees EXTRACTED)
> --- `packages/core/src/graph/crosslinker.ts`

> await store.writeText(pageNode.path, modifiedBody);
> --- `packages/core/src/graph/crosslinker.ts`

> const handler = handlers.get(req.params.name);
> --- `apps/mcp/src/tools/index.ts`

> name: 'run_wiki_health',
> --- `apps/mcp/src/tools/run-wiki-health.ts`

> 2. **Run wiki health** via `mindbase_run_wiki_health({ projectId })`. This calls find_orphans + find_contradictions + find_gaps + suggest_links and returns a composite report.
> --- `apps/plugin/agents/curator.md`

> description: Sub-agent dispatched by /mb:lint. Read-only — has Read + lint MCP tools but no Edit/Write/Bash. Surfaces orphans, contradictions, stale claims, gaps. Suggests fixes; doesn't apply them.
> --- `apps/plugin/agents/curator.md`

#### EPI-RTE-cli-admission
Label: CLI ingest all-action approval

SRC-1, `apps/cli/src/index.ts`, `apps/cli/src/commands/ingest.ts`. Distinct from [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan): separate CLI caller of core compileL1Plan/Execute, not the ops pending-plan route. Local file ingestion stores raw content before planning; URL mode passes the URL string to ingestPaste rather than fetching its page in this caller. CLI uses an empty hybridSearch callback. Human sees action kinds/titles and an all-or-nothing confirmation unless --yes. The core compile implementation was not fully traced, so this record owns caller admission, not every executor guarantee.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Proposed action list, aborted message or execution results printed to terminal.
- Later read-back: uninspected — caller forwards to compileL1Execute; full persistence/read-back semantics of this core path not traced here.
- Delegated visibility: inapplicable — no sub-agent in this caller.
- Selection predicate: User confirms entire proposal, or --yes bypasses interactive confirmation; execution receives empty approvals object documented locally as all approved.
- Invalidation or expiry: inapplicable — current invocation plan, no TTL or persistent proposal cache in this caller.
- Activation or effect: Confirmation/flag gates the call to compileL1Execute; no evidence-consuming truth criterion is enforced in the CLI caller.
- Evidence limits: No runtime or human deliberation evidence; downstream core guarantees not inferred from caller intent.

Open ingest request; model proposes via core planner, human or --yes flag authorizes the batch. Aborting vetoes execution but does not reverse prior source ingestion. No expected-answer oracle. No rollback assertion beyond this caller's inspected code.

> .option('--yes', 'auto-approve all proposed actions')
> --- `apps/cli/src/commands/ingest.ts`

> const approvals = {};   // empty = all approved
> --- `apps/cli/src/commands/ingest.ts`

### Claims

#### EPI-CLM-wiki-audit
Label: Whole-wiki exact-conflict audit

SRC-1, `README.md`; doctrine/design conclusion status: claimed. Distinct from [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes): audit coverage and quote quality rather than permission to write.

> **It audits its own knowledge.** One command re-reads the whole wiki and reports contradictions with the exact conflicting sentences quoted. Notion and NotebookLM structurally cannot do this.
> --- `README.md`

The competitor comparison is attributed marketing, not independently assessed evidence. The concrete MindBase audit claim is bounded by forty research excerpts of 1,200 characters in ops gather, model judgment and normalized occurrence counts; probe uses selected legacy-page pairs. The implementation supports diagnosis capacity, not exhaustive or sound contradiction detection.

> const MAX_LINT_PAGES = 40;
> const MAX_EXCERPT_CHARS = 1_200;
> --- `apps/server/src/ops/gather.ts`

#### EPI-CLM-sentence-pruning
Label: Every synthesis sentence backed and pruned

SRC-1, `packages/core/src/synthesis/prompts.ts`; doctrine/design conclusion status: claimed. No supplied claim counterpart: this concerns the structured topic-synthesis prompt, not ops action approval. It explicitly claims a postprocessing behavior as well as requesting citation support. The validator's no-inline-marker branch is a countercase; see [EPI-RTE-topic-synthesis](#epi-rte-topic-synthesis).

> - Every sentence in "content" MUST be backed by at least one citation. Post-processing drops uncited sentences.
> --- `packages/core/src/synthesis/prompts.ts`

#### EPI-CLM-knowledge-compounds
Label: Contributions sharpen retained knowledge

SRC-1, `README.md`; doctrine/design conclusion status: claimed. Distinct from supplied approval claim: a longitudinal quality/benefit assertion. Persistence and later consumers are implemented; improving truth/coverage or future action capacity requires evidence not supplied in this run.

> Knowledge compounds. Your `context.md` gets sharper every time you contribute.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied runtime paths and new route declarations above give the assessed consumers, channels, forces and horizons without duplicating their identities.

