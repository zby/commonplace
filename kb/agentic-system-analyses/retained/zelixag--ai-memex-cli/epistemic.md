---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of ai-memex-cli: source lineage, structural checks, delegated judgment and later reliance"
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
reviewed-boundary: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
---

# ai-memex-cli epistemic report

## Source-and-claim boundary

The question is whether source capture, wiki maintenance and later answering establish warranted content, rather than only retained or operationally usable content. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). This is source inspection, not target execution. Public claims are [EPI-CLM-memory-compounds](#epi-clm-memory-compounds), [EPI-CLM-synthetic-pages](#epi-clm-synthetic-pages), [EPI-CLM-consistent-vault](#epi-clm-consistent-vault) and the supplied [RT-CLM-management-use](runtime.md#rt-clm-management-use).

Coverage below distinguishes new direct reads from supplied runtime findings. Newly inspected files remain SRC-1 implementation or attributed doctrine/design, not new sources. Dispatch inventory was checked with a scoped search of `src/cli.ts`, installed command definitions in `src/commands/install-hooks.ts`, repository slash prompts and installed workflow references. The direct CLI read includes lint, link-check, search, new/log and injection dispatch. No additional provider-native tool registry is established by that inspection; external host internals are outside the target.

| Entry point or operation | Source path | Coverage / supporting records |
|---|---|---|
| URL/search/crawl capture, delegated capture | `src/core/fetcher.ts`; `src/commands/fetch.ts` | Direct helper read plus supplied [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); [EPI-RTE-fetch-render](#epi-rte-fetch-render) adds lineage assessment. Live extraction fidelity remains unknown. |
| Mechanical and delegated session capture | `src/core/distiller.ts`; `src/commands/distill.ts` | Direct parser/renderer and selected command/prompt reads; [EPI-RTE-session-render](#epi-rte-session-render), [RT-RTE-session-distill](runtime.md#rt-rte-session-distill). |
| Ingest and lint-feedback prompt | `src/commands/ingest.ts` | Direct prompt read plus supplied [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write). |
| Mechanical lint, semantic lint | `src/commands/lint.ts`; `src/core/schema.ts`; `src/core/linker.ts`; `src/core/wiki-index.ts` | Direct complete reads; [EPI-RTE-mechanical-check](#epi-rte-mechanical-check), [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint). |
| Watch/loop and after-clean context refresh | `src/core/ingest-lint-loop.ts`; `src/commands/watch.ts` | Direct complete loop read, supplied watcher account; [EPI-RTE-loop-disposition](#epi-rte-loop-disposition), [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair). |
| Standalone link-check, including --fix | `src/commands/link-check.ts` | Direct complete read and dispatch read; [EPI-RTE-link-check](#epi-rte-link-check). Additional exposed reporting path, not an omitted semantic evaluator. |
| Query/slash/skill synthesis | `templates/skills/ai-memex/references/query-workflow.md`; `.claude/commands/memex/query.md`; `src/commands/install-hooks.ts` | Direct reads of reference, local query prompt and installed command registry; [EPI-OBJ-query-answer](#epi-obj-query-answer), [RT-CLM-management-use](runtime.md#rt-clm-management-use). |
| Search/inject/glob/context delivery | `src/commands/search.ts`; `src/commands/inject.ts`; `src/commands/glob.ts`; `src/commands/context.ts` | Supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not a new exhaustive audit of backends or projection helpers. |
| New page, action log, status | `src/commands/new.ts`; `src/commands/log.ts`; `src/commands/status.ts`; `templates/synthesis.md` | Direct complete reads. Scaffolding, caller-supplied action entries and counts, not factual acceptance gates; supplied [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) covers the alternate page writer. |
| Init/onboard/config/migrate/install/update | `src/cli.ts`; `src/commands/install-hooks.ts`; `src/commands/migrate.ts`; `src/commands/update.ts` | Dispatch inventory plus supplied [RT-RTE-install-update](runtime.md#rt-rte-install-update), [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) and [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write). Onboarding interaction and full helper correctness not independently audited; no system-complete security or evaluator-exhaustiveness claim. |
| Source, citation and contradiction instructions | `templates/AGENTS.md`; `templates/skills/ai-memex/references/ingest-workflow.md`; `templates/skills/ai-memex/references/safety-rules.md` | Direct complete reads; [EPI-CLM-synthetic-pages](#epi-clm-synthetic-pages), [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt). |

No real vault, transcript, generated answer, semantic-lint finding or approval record was supplied. Those gaps prevent identifying actual candidate propositions, checking source-to-page fidelity or establishing acceptance and downstream activation. No trace or experiment establishes better answering, factual accuracy, convergence or causal improvement. External inference and qmd internals remain uninspected; model weights, exact versions and training changes are bounded by [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent). Available but unread repository-local prompt variants and design documents prevent an exhaustive doctrine inventory, not the narrower route findings below.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-material](#epi-obj-raw-material) | Imported web claims and recorded session utterances; actual propositions not determinable without inputs | see record | SRC-1, `src/core/fetcher.ts` | A recorded utterance is not evidence that its embedded factual assertion is true. Tool evidence can be omitted. |
| [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | Source claims, comparisons and proposed insights; actual propositions not determinable | see record | SRC-1, `templates/AGENTS.md` | Page type and citation fields do not establish warrant. |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Assertions about indexed links, inbound references and metadata validity | see record | SRC-1, `src/commands/lint.ts` | Truth scope is the implemented predicates on selected pages, not world facts. |
| [EPI-OBJ-query-answer](#epi-obj-query-answer) | Requested source-backed answer, synthesis or inference; actual proposition unavailable | see record | SRC-1, `templates/skills/ai-memex/references/query-workflow.md` | No answer instance or evidence-consuming acceptance decision. |
| [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt) | Schema directives are policies; embedded index and lint assertions may be truth-apt | see record | SRC-1, `src/commands/ingest.ts` | Split by consumer below: structural feedback versus live-schema guidance. |
| [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent) | Cannot individuate propositions in distributed-parametric state | see record | SRC-1, `src/core/agent-adapter.ts` | Invocation is inspectable; internal representations and parameter updates are not. |

## Authority-route ledger

Fields owned by supplied records are referenced rather than redefined. Linked entries using one route record separate its consequential functions; they do not allocate replacement identities.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-fetch-render](#epi-rte-fetch-render) | content transformation | implemented | [EPI-OBJ-raw-material](#epi-obj-raw-material) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | URL/date lineage retained; source warrant unknown; full-document lineage degraded by selection | see record | see record | SRC-1, `src/core/fetcher.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Extraction is not verification. |
| [EPI-RTE-session-render](#epi-rte-session-render) | content transformation | implemented | [EPI-OBJ-raw-material](#epi-obj-raw-material) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Retained text records speech, not its correctness; supporting tool-result context can be lost | see record | see record | SRC-1, `src/core/distiller.ts` | none | lineage-loss | Concrete input deduction in record; not executed. |
| [RT-RTE-session-distill](runtime.md#rt-rte-session-distill) | content transformation | implemented | [EPI-OBJ-raw-material](#epi-obj-raw-material) | truth-apt transformation: indeterminate | Session to best-practice document | External agent; role/session scope, no oracle | see record | see record | see record | Requested implicit lessons could reshape or add claims; no output supports entailment classification | see record | see record | SRC-1, `src/commands/distill.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Need source/output pair to distinguish compression, derivation and conjecture. |
| [RT-RTE-session-distill](runtime.md#rt-rte-session-distill) | behavior/policy adaptation | implemented | [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt) | non-truth-apt policy/content update: requested session-learning notes in live schema | Session experience to future guidance | External agent decides notes; CLI does not validate their use | see record | see record | see record | No increased capacity or factual license established | see record | see [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt) | SRC-1, `src/commands/distill.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Notes can contain truth-apt rationale, but no instance individuates it. |
| [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) | content transformation | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | truth-apt transformation: indeterminate | Sources to source/entity/concept/synthetic pages | Child agent under live schema; collaborative discussion requested, no enforced per-claim gate | see record | see record | see record | Citations, labelled inference and preserved conflicts are requested; no checked derivation or factual acceptance established | see record | see record | SRC-1, `src/commands/ingest.ts` | [EPI-CLM-synthetic-pages](#epi-clm-synthetic-pages) | none | Neither synthesis label nor failure to prove entailment establishes ampliation. |
| [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) | retention | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | no content change | Durable writes, index and log | see record | see record | see record | see record | Operational retention precedes any established acceptance | see record | see record | SRC-1, `src/commands/ingest.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Agent writes are requested, not verified by caller. Not lifecycle integration after acceptance. |
| [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) | check/evidence production | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Conditional deduction over parsed index and metadata; not source truth, semantic consistency or useful knowledge | see record | see record | SRC-1, `src/core/linker.ts` | [EPI-CLM-consistent-vault](#epi-clm-consistent-vault) | scope-overclaim | Parser fidelity and selected-page scope bound the result. |
| [EPI-RTE-loop-disposition](#epi-rte-loop-disposition) | disposition/acceptance | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | no content change | see record | see record | see record | see record | see record | Accepts structural-clean stop condition only, not wiki factual content | see record | see record | SRC-1, `src/core/ingest-lint-loop.ts` | [EPI-CLM-consistent-vault](#epi-clm-consistent-vault) | scope-overclaim | No content rejection/rollback gate; retained edits survive stall/cap. |
| [EPI-RTE-link-check](#epi-rte-link-check) | check/evidence production | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Only exact extracted target membership among basename IDs | see record | see record | SRC-1, `src/commands/link-check.ts` | none | none | --fix does not fix or withdraw content. |
| [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint) | check/evidence production | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | truth-apt transformation: indeterminate | Cross-page contradictions, stale claims and other schema categories | Child agent scans wiki; no independent answer oracle | see record | see record | see record | Can propose content criticism; no supplied finding establishes its correctness or coverage | see record | see record | SRC-1, `src/commands/lint.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | New diagnostic assertions may be reshaping, derived or conjectural; output needed. |
| [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint) | disposition/acceptance | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | no content change | Safe repair versus unresolved review item | Model judges safety/ambiguity; no CLI evidence-consuming factual acceptance record | see record | see record | see record | Direct edit permission, not established acceptance of an ampliative claim | see record | see record | SRC-1, `src/commands/lint.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Ambiguity defers review in prompt; no implementation gate verifies the deferral. |
| [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair) | behavior/policy adaptation | implemented | [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt) | non-truth-apt policy/content update: prioritize structural repairs in next invocation | Prior report to repair priorities | Code forwards report; child interprets instructions | see record | see record | see record | Structural defects guide work, not an epistemic oracle for claims | see record | see record | SRC-1, `src/commands/ingest.ts` | [EPI-CLM-consistent-vault](#epi-clm-consistent-vault) | none | This is feedback-driven work selection, not demonstrated theory criticism or improvement. |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | no content change | Select pages/snippets/includes/digest for outer host | see record | see record | see record | see record | Delivery grants availability, no additional truth license | see record | see [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap) for installed path; other consumers see route | SRC-1, `src/commands/context.ts` | [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | none | Task/token flags do not enforce relevance/budget; excerpts and old projection files can limit evidence. |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | content transformation | doctrine only | [EPI-OBJ-query-answer](#epi-obj-query-answer) | truth-apt transformation: indeterminate | Wiki evidence to foreground answer | Outer agent instructed to distinguish facts, synthesis, inference and unknowns | see record | see record | Advisory reference text | No answer acceptance or derivation check established | Requested answer in current session; saving is a separate requested workflow | see record | SRC-1, `templates/skills/ai-memex/references/query-workflow.md` | [RT-CLM-management-use](runtime.md#rt-clm-management-use) | none | CLI implements delivery, not the foreground synthesis algorithm. |
| [RT-RTE-install-update](runtime.md#rt-rte-install-update) | operational admission/selection/consumption | implemented | [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) | non-truth-apt policy/content update: expose workflows or replace distribution | Hook installation or product replacement | see record | see record | see record | see record | Package/build success is not knowledge-quality evaluation | see record | see record | SRC-1, `src/commands/update.ts` | none | none | Explicit upgrade is not self-directed improvement. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-compounds](#epi-clm-memory-compounds) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | None supplied | No comparison or activation evidence; semantic checks are optional and model-dependent | Persistent pages and reuse channels support an accumulation mechanism | Already-flagged contradictions and synthesis reflecting everything read are not established guarantees. |
| [EPI-CLM-synthetic-pages](#epi-clm-synthetic-pages) | see record | SRC-1, `templates/AGENTS.md`, doctrine/design | see record | [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-session-distill](runtime.md#rt-rte-session-distill) | None supplied | No concrete input/output propositions or acceptance record | System requests synthetic content and provenance-preserving treatment | Cannot infer actual conjecture, checked entailed derivation or accepted new knowledge from type labels. |
| [EPI-CLM-consistent-vault](#epi-clm-consistent-vault) | see record | SRC-1, `src/core/ingest-lint-loop.ts`, implementation message/design claim | see record | [EPI-RTE-mechanical-check](#epi-rte-mechanical-check), [EPI-RTE-loop-disposition](#epi-rte-loop-disposition) | None supplied | Zero mechanical issues licenses only the selected structural predicates | Deterministic stop and best-effort refresh are wired | “Knowledge base is consistent” exceeds evaluator domain if read semantically. |
| [RT-CLM-management-use](runtime.md#rt-clm-management-use) | see record | SRC-1, `templates/skills/ai-memex/SKILL.md`, doctrine/design | see record | [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | None supplied | External host controls actual use; schema and query reference differ on saving | Child maintenance and foreground-use guidance are distinct | No uniform read-only query or per-content approval invariant. |

## Bounded conclusion

**Retention and reuse are wired; warrant is route-specific.** [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) requests durable wiki/index/log writes. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) makes selected retained content available by search, includes, copies or host digest. Neither route establishes that a user actually relied on it or that reliance improved an answer. Retention is not post-acceptance lifecycle integration.

**Acquisition preserves some attribution but not full evidential context.** [EPI-RTE-fetch-render](#epi-rte-fetch-render) retains URL/date with extracted Markdown, while full source warrant remains unknown. [EPI-RTE-session-render](#epi-rte-session-render) preserves selected utterance text and role metadata but can discard the tool-result evidence behind it. The source-supported countercase to “distill is semantic learning” is its mechanical default; the countercase to “mechanical means lossless transcript” is block-level omission. Both matter for later source citation.

**Structural checks have real but narrow force.** [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) and [EPI-RTE-link-check](#epi-rte-link-check) derive diagnostic propositions over parsed pages, not warranted world knowledge. [EPI-RTE-loop-disposition](#epi-rte-loop-disposition) consumes zero issues as a criterion for stopping this repair run and attempting registered context refresh. Its intended use is structural maintenance of the selected vault; its horizon is this loop and the subsequently refreshed host projection. Nonzero reports can prioritize another agent invocation, while no-change/cap stops leave edits available. That is operational disposition, not factual acceptance or withdrawal. A missing/unchecked citation cannot be cured merely by zero link issues.

**Semantic judgment is delegated, not absent, but its results are unobserved.** [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint) requests content-directed diagnosis, direct safe repairs and review pages for ambiguity. It is the source-supported countercase to claiming that the system checks only structure. Schema and reference guidance also request evidence, explicit inference and preservation of contradictions. However, no supplied proposition, checked derivation, evaluator finding or evidence-consuming decision establishes produced accepted ampliative knowledge. Neither novelty nor the synthesis directory settles the transformation class. A later factual acceptance and its lifecycle integration remain unestablished, rather than universally impossible.

**Instruction adaptation has a separate path.** [RT-RTE-session-distill](runtime.md#rt-rte-session-distill) requests appending session learnings to the live schema, and [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt) identifies a later interpreted guidance channel. [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair) also feeds structural observations into subsequent priorities. These are inspectable update requests and feedback mechanisms; no parameter-training operation is established by the inspected caller, and external parameter changes remain uninspected. Future-capacity improvement, exercised self-improvement, content-directed theory criticism and autonomous success do not follow from those mechanisms. Their absence is not inferred from model opacity either. No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-raw-material
Label: Captured raw material

Source-native identity: `raw/` web Markdown and session Markdown. Representational form: natural-language assertions/utterances, with symbolic URL/date/role/frontmatter fields. Storage substrate: UTF-8 Markdown files under raw scenes. Content truth and source reliability are not established by capture. Distinct from [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt): persisted evidence inputs, not an invocation prompt. It is an object spanning the outputs of [RT-RTE-capture-source](runtime.md#rt-rte-capture-source) and [RT-RTE-session-distill](runtime.md#rt-rte-session-distill), not a replacement or part of exactly one route. Evidence: SRC-1, `src/core/fetcher.ts`, `src/core/distiller.ts`, implementation; load-bearing passages appear in the transformation records below.

#### EPI-OBJ-wiki-content
Label: Wiki page content

Source-native identity: `wiki/<scene>/` page bodies and frontmatter. Representational form: natural language consumed by agents and symbolic page IDs, links and metadata consumed by index/lint code. Storage substrate: Markdown in the vault. Distinct from [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt): durable content produced/loaded across invocations, not its prompt carrier. Closest supplied routes are [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); object versus writer/reader, not duplicate referents. Evidence: SRC-1, `templates/AGENTS.md` (doctrine/design), `src/core/wiki-index.ts` (implementation).

> const id = basename(filePath, '.md');
> const links = extractWikiLinks(body);
> --- `src/core/wiki-index.ts`

#### EPI-OBJ-lint-report
Label: Mechanical lint report

Source-native identity: `LintReport` and `LintIssue` arrays. Representational form: symbolic typed fields interpreted by the loop; issue descriptions/JSON also become natural-language evidence for agents. Storage substrate: current-run objects and output JSON/text; not intrinsically durable accepted knowledge. Distinct from [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt), which can embed it, and [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair), which consumes it. Evidence: SRC-1, `src/commands/lint.ts`, implementation; report construction and predicate passages below.

#### EPI-OBJ-query-answer
Label: Foreground query answer

Source-native identity: answer requested by Query Workflow. Representational form: natural-language synthesis/citations, potentially other schema-requested output forms. Storage substrate: outer session response; durable page only via a further writing workflow. Closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) describes delivery and foreground use, not a concrete answer object; no supplied object counterpart. Evidence: SRC-1, `templates/skills/ai-memex/references/query-workflow.md`, doctrine/design.

> 6. Distinguish:
>    - known facts from the wiki
>    - source-backed synthesis
>    - inference
>    - unknown or missing knowledge
> --- `templates/skills/ai-memex/references/query-workflow.md`

### Routes

#### EPI-RTE-fetch-render
Label: Direct fetch extraction and rendering
Part of: [RT-RTE-capture-source](runtime.md#rt-rte-capture-source)

Endpoints/progression: network body → DOM/optional aggressive stripping → Readability selection → Turndown Markdown → URL/date-wrapped raw document; outer fetch command owns persistence. This part assesses direct extraction, not the alternate agent fetch path. Evaluator/condition: HTTP status rejects errors at or above 400; extraction libraries select body text, not factual credibility. No factual oracle. Mode: open source capture. User/query selects sources; code admits converted output, caller may cancel/dry-run in the parent route; no claim-level approval or rollback added here. Evidence: SRC-1, `src/core/fetcher.ts`, implementation.

- Immediate return: `FetchResult`, then Markdown string for the command's writer.
- Later read-back: written raw document can enter ingest/search via the parent route.
- Delegated visibility: inapplicable — this extraction part calls no coding agent.
- Selection predicate: supplied URL and optional aggressive DOM stripping; Readability article or body fallback.
- Invalidation or expiry: no extraction TTL; repeated destination writes belong to parent capture route.
- Activation or effect: deterministic extraction and attribution wrapping implemented; factual endorsement not performed.
- Evidence limits: third-party extraction fidelity and live source truth uninspected; no fetched instance supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Source warrant is unknown. URL and fetch date survive, but source completeness is not preserved by article extraction; optional nav/header/footer removal supplies a concrete loss channel. Acquisition is not production of the imported assertions.

> const htmlContent = article?.content ?? dom.window.document.body?.innerHTML ?? '';
> const content = td.turndown(htmlContent);
> --- `src/core/fetcher.ts`

> source-url: ${result.url}
> fetched: ${result.fetchedAt}
> word-count: ${result.wordCount}
> --- `src/core/fetcher.ts`

#### EPI-RTE-session-render
Label: Mechanical session normalization and rendering
Part of: [RT-RTE-session-distill](runtime.md#rt-rte-session-distill)

Endpoints/progression: selected file → `parseSessionStructured` → normalized messages → `renderSessionMarkdown` → raw Markdown written by mechanical command. Code owns selection/serialization; no model evaluator, oracle or semantic acceptance. Open conversion request; caller selects input/mode. Admission is parser-recognized messages or whole-text fallback when none parse. No content-specific veto or automatic rollback in this part. Evidence: SRC-1, `src/core/distiller.ts`, `src/commands/distill.ts`, implementation.

- Immediate return: rendered Markdown and write destination message.
- Later read-back: raw session document is a later ingest source; sources metadata points to original file path.
- Delegated visibility: inapplicable — mechanical branch launches no agent.
- Selection predicate: structured parser recognizes supported message shapes; block flattening selects text and tool names, discards tool-result blocks; malformed/unrecognized records may be skipped.
- Invalidation or expiry: default current-session path uses mtime skip through parent route; explicit mechanical conversion writes selected output, with no general TTL.
- Activation or effect: normalizes and writes a transcript projection; no evidence of learning or correctness checking.
- Evidence limits: input/output deduction below uses inspected code, not a target run; other provider formats remain bounded by parser recognition.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction: take one JSONL object `{"message":{"role":"assistant","content":[{"type":"text","text":"The test passed."},{"type":"tool_result","content":"FAIL"}]}}`. `toStructured` takes the Claude-style branch; `flattenContent` keeps `The test passed.` and discards the `tool_result`. Rendering emits an Assistant heading and that text, but no `FAIL`. This is non-ampliative selection/reshaping of text, not truth validation of the retained assertion. It degrades the retained evidential context. A source path is provenance, not a substitute for omitted counterevidence. Conversely, the structured renderer can preserve a standalone generic role `tool` message with string content; this is not a claim that all tool evidence is always removed. The legacy `mechanicalExtract` skips system/tool-use/tool-result lines, but the command calls the structured parser/renderer, not that legacy extractor.

> } else if (t === 'tool_result') {
>   /* 丢弃工具结果 */
> --- `src/core/distiller.ts`

> const raw = await readFileUtf8(normalized);
> const messages = parseSessionStructured(raw);
> --- `src/commands/distill.ts`

> const bodyText = m.text.trim() || '_(空)_';
> return `## ${label}${ts}\n\n${bodyText}${toolLine}`;
> --- `src/core/distiller.ts`

#### EPI-RTE-mechanical-check
Label: Mechanical wiki predicate evaluation

Distinct identity: shared evaluator implementation, rather than the whole controller [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair) or delegated [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint). It serves multiple callers and is not contained in exactly one supplied route. Endpoints/progression: wiki files → parsed page index → optional scene subset → requested predicate families → `LintReport`. Owner: deterministic code. Target/domain: exact extracted basename-ID membership, inbound links and required/allowed metadata fields on selected indexed pages. Expected factual answers are not supplied; predicates themselves define the structural criterion. No human/model diagnosis in this evaluator. Mode: open lint request. Evidence: SRC-1, `src/commands/lint.ts`, `src/core/linker.ts`, `src/core/schema.ts`, `src/core/wiki-index.ts`, implementation.

- Immediate return: structured report; command can print text/JSON or forward it to semantic pass.
- Later read-back: report can shape a subsequent ingest invocation within the loop; no durable report retention by `runLint` itself.
- Delegated visibility: semantic/repair agents receive report representation via parent callers, not hidden semantic evidence from this evaluator.
- Selection predicate: configured checks default to orphans, broken-links and missing-frontmatter; optional scene subset is used before link checks.
- Invalidation or expiry: recomputed from files on each call; report superseded by later loop report.
- Activation or effect: diagnostic facts derive from current parsed inputs; parent decides continuation and refresh separately.
- Evidence limits: no check of factual page bodies, citation support or source reliability. Same-basename collisions, parsing and scoped-page selection limit what “link exists” means.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The conditional entailment is concrete: with parsed page IDs `{a}` and outbound target `{b}`, membership test entails a broken-link entry for `a → b`. A page with all required metadata, no outbound links and no inbound links remains an orphan; a false factual body can pass other predicates. `sources` is optional and its evidential support is not inspected. `index.md` is outside the wiki index used here; adding only an index entry need not clear an orphan, despite feedback suggesting it. These scope restrictions prevent semantic-consistency inference.

> if (!allIds.has(link)) {
>   broken.push({ source: page.id, target: link });
> }
> --- `src/core/linker.ts`

> export const REQUIRED_FIELDS: (keyof Frontmatter)[] = ['name', 'description', 'type', 'scene'];
> --- `src/core/schema.ts`

> if (options.scene) {
>   pages = pages.filter((p) => p.scene === options.scene);
> }
> --- `src/commands/lint.ts`

#### EPI-RTE-loop-disposition
Label: Mechanical report disposition
Part of: [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)

Endpoints/progression: report → empty/nonempty/repeated predicates → clean return and optional context refresh, another repair iteration or stalled/capped/signal return. Code owns this disposition. Criterion/intended use/scope: zero issues means no reported mechanical defects for the loop's lint invocation, sufficient to stop structural repair and attempt registered-host refresh. It is not factual acceptance of page claims. Proposer: prior ingest may edit pages; decider: loop code; veto/limits: caller stop, cap and repeat guard, with force bypass of repeat guard. Mode: open repair, no answer oracle beyond structural predicates. Recovery: stops do not roll back writes. Evidence: SRC-1, `src/core/ingest-lint-loop.ts`, implementation.

- Immediate return: iteration count, stop reason and final report.
- Later read-back: nonclean report enters next invocation; clean report can trigger durable host-context refresh, later consumed by host.
- Delegated visibility: next ingest gets report through prompt formatting; no per-claim acceptance record.
- Selection predicate: zero issues; otherwise bounded iteration, signal or sameIssueSet guard. Repeat keys omit frontmatter error detail.
- Invalidation or expiry: report replaced at next iteration; no claim withdrawal, expiry or rollback.
- Activation or effect: enforces loop continuation/stopping and invokes best-effort refresh; does not enforce truth or host compliance.
- Evidence limits: clean can follow failed/unchanged ingestion; neither convergence nor semantic correctness follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (report.issues.length === 0) {
>   logger.success('[loop] lint clean — knowledge base is consistent.');
> --- `src/core/ingest-lint-loop.ts`

> if (!opts.skipContextRefresh) {
>   await silentRefreshContexts(opts.vault, opts.cwd);
> }
> return { iterations: i, stopped: 'clean', finalReport: report };
> --- `src/core/ingest-lint-loop.ts`

#### EPI-RTE-link-check
Label: Standalone link reporting

Distinct identity: additional CLI entry point not separately recorded in runtime. It reuses the broken-link evaluator of [EPI-RTE-mechanical-check](#epi-rte-mechanical-check), but reports independently rather than controlling [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair). Endpoints/progression: CLI → vault index → exact link-target membership → terminal diagnostic. Owner/evaluator: deterministic code; target is extracted wiki links, domain is basename IDs in indexed wiki pages. Caller requests scan; no claim proposals or per-content approval. Open diagnostic mode, no semantic oracle. `--fix` logs an unimplemented message; no revision admission, rejection or rollback. Evidence: SRC-1, `src/commands/link-check.ts`, `src/cli.ts`, implementation.

- Immediate return: valid-links message or broken source/target list; optional manual-fix advice.
- Later read-back: inapplicable — this route writes no retained content or report.
- Delegated visibility: inapplicable — no delegated agent call; terminal reader may act manually.
- Selection predicate: all pages returned by buildWikiIndex, then findBrokenLinks.
- Invalidation or expiry: inapplicable — current scan output only, no retained artifact managed here.
- Activation or effect: advisory reporting; --fix performs no automated repair.
- Evidence limits: link existence is not cited-claim support or truth, and output consumption is unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (options.fix && broken.length) {
>   logger.info('Auto-fix not implemented in MVP. Agent should resolve these manually.');
> }
> --- `src/commands/link-check.ts`

### Claims

#### EPI-CLM-memory-compounds
Label: Memory that compounds

Claimed operation: agent-maintained retained knowledge accumulates, cross-references and contradiction flags are already available, and synthesis reflects what has been read. Source: SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-management-use](runtime.md#rt-clm-management-use): knowledge accumulation/coverage claim rather than work-context separation. No observed-run or causal layer.

> Your AI agents, finally with a memory that compounds.
> --- `README.md`

> Cross-references are already there. Contradictions have already been flagged. The synthesis already reflects everything you've read.
> --- `README.md`

#### EPI-CLM-synthetic-pages
Label: Derived insights and honest contradictions

Claimed operation: synthetic page types carry derived insights and connections; ingestion preserves explicit source conflict rather than silently replacing it. Source: SRC-1, `templates/AGENTS.md`, with source/inference constraints in `templates/skills/ai-memex/references/ingest-workflow.md`, doctrine/design. Closest [RT-CLM-management-use](runtime.md#rt-clm-management-use) concerns delegation and saving, not the epistemic role of page content. This claim has no instance-level derivation or acceptance evidence.

> - `synthesis` — derived insights, theses, or non-trivial connections (`syntheses/`)
> --- `templates/AGENTS.md`

> - Every new factual claim should trace to a raw file or existing wiki page.
> - If a claim is synthesized from multiple sources, cite all important sources.
> - If sources conflict, preserve the conflict instead of flattening it.
> - If a statement is an inference, label it as an inference.
> --- `templates/skills/ai-memex/references/ingest-workflow.md`

> Do not choose a winner unless the evidence clearly supports it or the user decides.
> --- `templates/skills/ai-memex/references/safety-rules.md`

#### EPI-CLM-consistent-vault
Label: Clean lint means consistent knowledge base

Claimed operation: a success message describes the knowledge base as consistent after zero mechanical issues. Source: SRC-1, `src/core/ingest-lint-loop.ts`, implementation text carrying a design/warrant implication, not an observed success. No counterpart among supplied claims after comparison with [RT-CLM-management-use](runtime.md#rt-clm-management-use). Closest supplied route [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair) already limits the predicates; [EPI-RTE-loop-disposition](#epi-rte-loop-disposition) supplies the exact passage. Interpreted narrowly as structural cleanliness the message matches; interpreted as factual consistency it exceeds the evaluator's domain.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
