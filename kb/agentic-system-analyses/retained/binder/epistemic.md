---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Binder epistemic routes: structural admission, model-generated journal candidates and human-guided reliance."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
---

# Binder epistemic report

## Source-and-claim boundary

The question is how Binder's typed shared memory acquires truth-apt content, checks it and lets it affect later work. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. No target execution, provider calls or tests were run. No observed model output, accepted journal instance, supplied run trace or causal comparison establishes compliance, factual accuracy or benefit. External provider weights and host scheduling remain uninspected; this prevents model-internal learning and end-to-end activation conclusions, not source-level route findings.

Public storage/memory claim: [EPI-CLM-agent-memory](#epi-clm-agent-memory). The source also requests evidence-grounded personal insights: [EPI-CLM-period-learnings](#epi-clm-period-learnings). These are not interchangeable claims of factual validation. Structural validation and history consistency are see [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary); post-commit limits are see [RT-CLM-derived-effects](runtime.md#rt-clm-derived-effects).

| Entry point or operation | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| CLI registration and dynamic dispatch | `packages/cli/src/index.ts` | Direct full read; core commands plus docs/journal/undo and workspace commands; no hidden universal model evaluator inferred. |
| Create/update/delete; MCP and HTTP mutations; library | `packages/cli/src/commands/create.ts`, `packages/cli/src/commands/delete.ts`, `packages/cli/src/mcp/tools/index.ts`, `packages/cli/src/http/server.ts`, `packages/cli/src/workspace.ts` | Direct searches of create/delete and full MCP registry read; remaining implementation supplied by [RT-RTE-graph-update](runtime.md#rt-rte-graph-update). Registry exposes schema/search/transact. |
| Read/search/schema and document/editor paths | `packages/cli/src/commands/read.ts`, `packages/cli/src/commands/search.ts`, `packages/cli/src/plugins/docs/commands.ts`, `packages/cli/src/lsp/handlers/save-handler.ts` | Supplied [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph), [RT-RTE-document-sync](runtime.md#rt-rte-document-sync). Extraction fidelity not independently audited; prevents a lossless semantic round-trip conclusion. |
| Transaction import, preview, rollback, squash, export/log | `packages/cli/src/commands/transaction.ts` | Direct handler excerpt and operation search; [EPI-RTE-import-preview](#epi-rte-import-preview). Squash internals and complete export encoding uninspected: no system-complete lineage-preservation verdict. |
| Undo/redo and journal repair | `packages/cli/src/plugins/undo/commands.ts`, `packages/cli/src/plugins/journal/commands.ts` | Full undo/redo read and journal command search; [EPI-RTE-undo-redo](#epi-rte-undo-redo), supplied [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair). |
| Hooks, workspace scripts/plugins, custom HTTP modules | `packages/repo/src/local/plugin-loader.ts`, `packages/cli/src/http/server.ts` | Supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Arbitrary user code not captured; prevents universal admission guarantees. |
| Git importer and generic LLM helper | `examples/journal/git-import-logs.ts`, `packages/cli/src/lib/llm.ts` | Direct full importer read; [EPI-RTE-import-format](#epi-rte-import-format), supplied [RT-RTE-git-import](runtime.md#rt-rte-git-import), [RT-RTE-llm-call](runtime.md#rt-rte-llm-call). No core helper consumer established. |
| Import/modeling/app skills | `skills/binder-import/SKILL.md`, `skills/binder-modeling/SKILL.md`, `skills/binder-app/SKILL.md` | Full import read; scoped search of modeling/app checks. [EPI-RTE-import-mapping](#epi-rte-import-mapping). Remaining modeling/app instructions not fully assessed; prevents complete prompt-policy coverage. |
| Journal summary, learning and planning | `examples/journal/skills/day-summary/SKILL.md`, `examples/journal/skills/period-summary/SKILL.md`, `examples/journal/skills/period-update/SKILL.md`, `examples/journal/skills/day-next-plan/SKILL.md` | Direct full reads; [EPI-RTE-journal-review](#epi-rte-journal-review). Other journal skills scoped searches only; no comprehensive journal-policy negative. |
| Task capture/refinement/investigation/implementation | `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/refine-backlog/SKILL.md`, `examples/workflow/skills/implement-task/guides/investigate.md` | Direct full reads; [EPI-RTE-task-findings](#epi-rte-task-findings), supplied [RT-RTE-task-guide](runtime.md#rt-rte-task-guide). Design/discuss/write-tests guides not independently read; no full theory-cycle verdict. |
| Authored evaluators | `packages/cli/tests/doc-sync.test.ts`, `packages/repo/src/knowledge-graph.test.ts` | Boundary's supplied test-source inspection only, not a passing run or factual-content evaluator. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | Caller fields may assert facts; schema/IDs alone need not | see record | SRC-1, `packages/repo/src/knowledge-graph.ts` | Container is not one proposition or one warrant class. |
| [EPI-OBJ-log](#epi-obj-log) | Dated activity descriptions | see record | SRC-1, `examples/journal/git-import-logs.ts` | No observed generated instance. |
| [EPI-OBJ-learnings](#epi-obj-learnings) | Personal insights, summaries, achievements and imported information | see record | SRC-1, `examples/journal/skills/period-summary/SKILL.md` | Separate arithmetic, historical reports and inferred patterns within the record. |
| [EPI-OBJ-task](#epi-obj-task) | Bug explanations and reproduction claims; requirements also include non-truth-apt goals | see record | SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md` | No retained investigation instance or test result. |
| [RT-CMP-journal-model](runtime.md#rt-cmp-journal-model), [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model) | Not determinable for internal distributed-parametric content | see records | SRC-1, `examples/journal/git-import-logs.ts`, `packages/cli/src/lib/llm.ts` | Provider parameters, training, endpoint resolution and internal processing uninspected; observable wrapper policy remains assessable. |

## Authority-route ledger

All owned fields below say see their declaring record; the short local ledger judgments do not replace those fields. Distinct rows separate checking from disposition, and retention from integration. No acceptance of an actual ampliative proposition is established.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-graph-update](runtime.md#rt-rte-graph-update) | check/evidence production | implemented | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | no content change | see route | see route | see route | see route | see route | Structural/schema and sequence license only | see route | see route | SRC-1, `packages/repo/src/transaction-processor.ts` | [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary) | none | Factual truth is outside this evaluator's target. |
| [RT-RTE-graph-update](runtime.md#rt-rte-graph-update) | retention | implemented | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | External source warrant unknown; persistence is not endorsement | see route | see route | SRC-1, `packages/repo/src/knowledge-graph.ts` | [EPI-CLM-agent-memory](#epi-clm-agent-memory) | none | Content may instead be policy/config; classification applies to truth-apt fields only. |
| [EPI-RTE-import-preview](#epi-rte-import-preview) | check/evidence production | implemented | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | no content change | see route | see route | see route | see route | see route | Preview of processability, not truth or guaranteed batch success | see route | see route | SRC-1, `packages/cli/src/commands/transaction.ts` | none | none | Warning continues and final return can be success. |
| [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair) | lineage/freshness/recovery | implemented | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | no content change | see route | see route | see route | see route | see route | Log continuity only | see route | see route | SRC-1, `packages/cli/src/plugins/journal/sync.ts` | [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary) | none | May replace graph state without fresh factual review. |
| [EPI-RTE-undo-redo](#epi-rte-undo-redo) | lineage/freshness/recovery | implemented | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | no content change | see route | see route | see route | see route | see route | Restoration does not restore factual warrant | see route | see route | SRC-1, `packages/cli/src/plugins/undo/commands.ts` | none | none | Withdrawal is caller-driven, not automatic claim refutation. |
| [RT-RTE-git-import](runtime.md#rt-rte-git-import) | content transformation | implemented | [EPI-OBJ-log](#epi-obj-log) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Candidate only | see route | see route | SRC-1, `examples/journal/git-import-logs.ts` | none | none | Requested compression may preserve or add meaning; no output distinguishes them. |
| [EPI-RTE-import-format](#epi-rte-import-format) | content transformation | implemented | [EPI-OBJ-log](#epi-obj-log) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | No additional source warrant | see route | see route | SRC-1, `examples/journal/git-import-logs.ts` | none | none | Concrete trace in record; not a target execution. |
| [RT-RTE-llm-call](runtime.md#rt-rte-llm-call) | check/evidence production | implemented | [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model) | no content change | see route | see route | see route | see route | see route | Requested response shape only | see route | see route | SRC-1, `packages/cli/src/lib/llm.ts` | none | none | Schema validity does not establish content truth; no downstream consumer found. |
| [EPI-RTE-import-mapping](#epi-rte-import-mapping) | disposition/acceptance | doctrine only | [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | Mapping and operational import approval, source warrant unknown | see route | see route | SRC-1, `skills/binder-import/SKILL.md` | none | none | No source-truth criterion or observed approval. |
| [EPI-RTE-journal-review](#epi-rte-journal-review) | check/evidence production | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Personal evidence and correction, not general mechanism validation | see route | see route | SRC-1, `examples/journal/skills/period-summary/SKILL.md` | [EPI-CLM-period-learnings](#epi-clm-period-learnings) | none | Inferred patterns can exceed logs; specific non-entailment not established without a candidate. |
| [EPI-RTE-journal-review](#epi-rte-journal-review) | disposition/acceptance | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | no content change | see route | see route | see route | see route | see route | User-confirmed account for journal/planning use only | see route | see route | SRC-1, `examples/journal/skills/day-summary/SKILL.md` | [EPI-CLM-period-learnings](#epi-clm-period-learnings) | none | Actual evidence-consuming decision unobserved. |
| [EPI-RTE-journal-review](#epi-rte-journal-review) | retention | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | no content change | see route | see route | see route | see route | see route | Confirmation is not external validation | see route | see route | SRC-1, `examples/journal/skills/period-summary/SKILL.md` | [EPI-CLM-agent-memory](#epi-clm-agent-memory) | none | Graph write affordance is implemented separately. |
| [EPI-RTE-journal-review](#epi-rte-journal-review) | lifecycle integration | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | no content change | see route | see route | see route | see route | see route | Intended confirmed summaries elevated through periods | see route | see route | SRC-1, `examples/journal/skills/period-summary/SKILL.md` | [EPI-CLM-period-learnings](#epi-clm-period-learnings) | none | Conditional on prior acceptance; arbitrary graph records have no such prerequisite. |
| [EPI-RTE-journal-review](#epi-rte-journal-review) | behavior/policy adaptation | doctrine only | [EPI-OBJ-learnings](#epi-obj-learnings) | non-truth-apt policy/content update: agreed plans and goals | see route | see route | see route | see route | see route | Plans are choices, not accepted factual theories | see route | see route | SRC-1, `examples/journal/skills/period-update/SKILL.md` | none | none | Direct adaptation route can operate without produced knowledge. |
| [EPI-RTE-task-findings](#epi-rte-task-findings) | content transformation | doctrine only | [EPI-OBJ-task](#epi-obj-task) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Candidate explanation and reproduction account | see route | see route | SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md` | none | none | Reproduction verifies symptom, not uniquely the proposed cause. |
| [RT-RTE-task-guide](runtime.md#rt-rte-task-guide) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-task](#epi-obj-task) | no content change | see route | see route | see route | see route | see route | Task design contract and conditional test reference | see route | see route | SRC-1, `examples/workflow/skills/implement-task/SKILL.md` | none | none | Guide selection can rely on field presence before any epistemic acceptance. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-agent-memory](#epi-clm-agent-memory) | see record | SRC-1, `README.md`; doctrine/design | Shared typed state | [RT-RTE-graph-update](runtime.md#rt-rte-graph-update) | None supplied | None supplied | Typed persistence/read-back is wired | Transparency and easy maintenance not measured; no claim of universal truth checking implied. |
| [EPI-CLM-period-learnings](#epi-clm-period-learnings) | see record | SRC-1, `examples/journal/skills/period-summary/SKILL.md`; doctrine/design | Grounded proposals, user corrections, retained learnings | Underlying [RT-RTE-graph-update](runtime.md#rt-rte-graph-update); interpreting policy [EPI-RTE-journal-review](#epi-rte-journal-review) is doctrine only | None supplied | No intervention or comparison | A human-assisted evidence-responsive procedure is specified | No demonstrated accepted ampliative claim, transfer or future capacity gain. |
| [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary) | see record | SRC-1, `packages/repo/src/transaction-applier.ts`; implementation | see record | [RT-RTE-graph-update](runtime.md#rt-rte-graph-update), [EPI-RTE-undo-redo](#epi-rte-undo-redo) | see record | No factual or host-wide license | Structural admission and continuity have bounded force | Prepared apply bypasses fresh preparation; plugins can cross effect boundary. |

## Bounded conclusion

Binder implements storage, retrieval and structural admission of caller-supplied state, not a universal factual acceptance mechanism. Acquisition preserves accessible text/fields as graph data, but source warrant is unknown unless a caller supplies and checks it; attribution metadata alone does not authenticate authorship. Prepared replay, undo/redo and caller deletion can withdraw or restore operational state without judging the facts it states. These limits are see [RT-RTE-graph-update](runtime.md#rt-rte-graph-update), [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair), [EPI-RTE-undo-redo](#epi-rte-undo-redo).

The journal importer requests model-generated activity summaries and deterministically reshapes the returned list into insertion mutations. It only prints a proposal. Its actual prompt omits commit hashes and time-of-day; therefore its request for actual timestamps lacks that source input. Shape parsing and timestamp positioning cannot recover the omitted evidence. No measured deduplication or factual correctness follows; see [EPI-RTE-import-format](#epi-rte-import-format). Arithmetic averages in journal prompts describe entailed calculations conditional on trustworthy scores and correct execution, not an inspected numerical evaluator or a warranted conclusion about productivity.

Human-mediated journal procedures do specify evidence, criteria and intended use: compare records and user corrections, confirm the personal account, then save it for journal review and subsequent planning. Import approval instead licenses mapping/application, and task readiness licenses work selection; neither is automatically epistemic acceptance. Proposed `learnings` may import outside information or infer patterns; without concrete outputs their relation remains indeterminate. The architecture requests checking, correction, retention and conditional integration, but no observed acceptance of an ampliative claim is established. See [EPI-RTE-journal-review](#epi-rte-journal-review), [EPI-RTE-import-mapping](#epi-rte-import-mapping), [EPI-RTE-task-findings](#epi-rte-task-findings).

Operational authority is heterogeneous. Graph validation enforces mutation admission immediately; restored state changes subsequent queries. Journal and task text advise external agents through skill bodies and requested reads over later workflow invocations; actual compliance is unobserved. Plans can change directly from activity/user discussion without a truth-apt intermediate. Test success is a bounded outcome check, not proof of root-cause attribution or transfer. The uninspected guides and extension behavior prevent a system-complete negative. No single system epistemic status follows, and persistence, reflection-themed prose, learning-field names, model opacity and autonomous host execution establish none of learning benefit, a completed theory criticism cycle or exercised self-improvement by themselves.

## Shared records

### Operative objects

#### EPI-OBJ-log
Label: Journal importer log candidates

Source-native identity: `logEntries` and `changeset.log`. Natural-language dated activity strings inside symbolic insertion mutations; process memory then stdout JSON, not newly persisted by the importer. Distinct from the retained graph container; output may replace/add its content but is not presently a part of that container. Closest supplied record: [RT-RTE-git-import](runtime.md#rt-rte-git-import), which supplies the whole production route, not an object declaration. SRC-1, `examples/journal/git-import-logs.ts`.

> const logEntries = parseLogEntries(llmOutput);
> --- `examples/journal/git-import-logs.ts`

#### EPI-OBJ-learnings
Label: Journal summaries and learnings

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: journal `summary`, `learnings`, `achievements` and score fields. Text is natural-language interpreted by people/models; numeric scores are symbolic inputs to requested averaging. Storage substrate: graph fields in SQLite when written; model proposals first inhabit host dialogue. These are distinct parts of the runtime container with human correction and later journal consumers, not an additional store. Scores encode judgments rather than independent measurements. SRC-1, `examples/journal/skills/day-summary/SKILL.md`, `examples/journal/skills/period-summary/SKILL.md`.

> Learnings must be grounded in period evidence: personal insights and information from external sources like articles, not generic productivity advice
> --- `examples/journal/skills/period-summary/SKILL.md`

#### EPI-OBJ-task
Label: Task diagnosis and design fields

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: `rootCause`, `stepsToReproduce`, `specification`, `acceptanceCriteria`, task status and links. Textual diagnosis/design fields receive consequences through model interpretation; status/link identifiers also select symbolic query results. Storage substrate: graph fields after updates, with source files in the host filesystem. Distinct from journal parts by target, check and consumer. Closest supplied [RT-RTE-task-guide](runtime.md#rt-rte-task-guide) owns whole task progression. SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/capture-task/SKILL.md`.

> For `rootCause`, explain **why** the bug happens, not just where. For `sourceFiles`, list all files involved — not just the entry point.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

### Routes

#### EPI-RTE-import-preview
Label: Transaction import dry-run and admission

Distinct from [RT-RTE-graph-update](runtime.md#rt-rte-graph-update): this CLI caller has an explicit nonmutating preview branch and a separate sequential update branch. SRC-1, `packages/cli/src/commands/transaction.ts`. Caller supplies files/stdin and selection; command parses, previews via `kg.process` or applies via `kg.update`. Preview targets current structural processability, not factual truth; warnings are printed and processing continues. Apply may fail on a later transaction after earlier ones committed. No automatic per-content human approval is imposed. Operating mode is open import, no answer oracle; CLI metadata and source tags persist on actual admission. Recovery is graph rollback/undo, not whole-file atomicity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed previews/warnings and success in dry-run; transactions or failure during apply.
- Later read-back: applied records are subsequently queryable; previews themselves do not change graph state.
- Delegated visibility: requesting caller sees CLI output; other workspace clients can read applied records.
- Selection predicate: chosen files/stdin, selection options and dryRun flag.
- Invalidation or expiry: subsequent graph state can invalidate a preview; rollback can remove applied suffixes.
- Activation or effect: process results advise the caller; update success enforces structural admission and persistence.
- Evidence limits: implementation only; preview success is neither factual acceptance nor guaranteed batch application.

> ui.warning(`Transaction ${i + 1} would fail:`);
> --- `packages/cli/src/commands/transaction.ts`

> ui.block(() => ui.info("Dry run complete - no changes made"));
> --- `packages/cli/src/commands/transaction.ts`

#### EPI-RTE-undo-redo
Label: Undo withdrawal and prepared redo

Distinct from supplied [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair): caller-selected step count, undo-log source and redo's current-hash check, rather than log-authoritative divergence repair. SRC-1, `packages/cli/src/plugins/undo/commands.ts`. Handler validates count, fetches display transactions, rolls back selected suffix; redo reads parsed undo-log transactions, checks predecessor and calls `kg.apply` sequentially. Software can veto count/history mismatch; user chooses restoration, not per-proposition factual endorsement. Open recovery mode, no answer oracle. Guidance is command contract and stored history; graph state/history changes, not arbitrary external side effects.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: displayed transactions and success or count/history/application error.
- Later read-back: subsequent queries see rolled-back/restored graph state; staged transactions can feed redo.
- Delegated visibility: caller sees display; workspace readers and graph subscribers see state effects.
- Selection predicate: steps, current version, undo-log tail and predecessor hash.
- Invalidation or expiry: changed current hash blocks redo of the captured predecessor; further updates supersede state.
- Activation or effect: rollback withdraws graph mutations; prepared apply restores transactions without fresh-input processing.
- Evidence limits: implementation only; no automatic semantic refutation, factual reapproval or multi-step atomicity established.

> "Cannot redo: repository state has changed since undo",
> --- `packages/cli/src/plugins/undo/commands.ts`

> const applyResult = await kg.apply(tx);
> --- `packages/cli/src/plugins/undo/commands.ts`

#### EPI-RTE-import-format
Label: Git prompt omission and insertion formatting

Part of: [RT-RTE-git-import](runtime.md#rt-rte-git-import)

The importer code owns Git selection, prompt formatting, line extraction and mutation positions; external model owns candidate wording. Context is Git output plus prior/current log strings. SRC-1, `examples/journal/git-import-logs.ts`. This part distinguishes fixed transformations from uninspected semantic generation. The target of `parseTime` is a string prefix, not historical timing; `parseLogEntries` checks a list-line prefix, not YAML validity or truth. It has no semantic veto or answer oracle. The model prompt asks for meaningful, nonoverlapping entries, but these criteria are not checked by the parser. Open date-based import; no internal graph write or content approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: prompt text, extracted strings, insertion mutations and ultimately printed changeset, or empty-extraction failure.
- Later read-back: inapplicable — this script does not persist its proposal for another invocation.
- Delegated visibility: filtered prompt reaches external CLI; caller receives parsed proposal rather than raw commit evidence.
- Selection predicate: date, message exclusion regexes, lines beginning with a dash and space, parsed time ordering.
- Invalidation or expiry: temporary prompt deleted after model completion; no proposal expiry or enforced semantic deduplication.
- Activation or effect: code can order insertions; absent entries cause failure, not acceptance or storage.
- Evidence limits: static deduction only; no model output or source accuracy observation. Shape processing adds no warrant.

Concrete deterministic trace: a Git log line `abc|2026-10-14|Fix parser` becomes prompt line `  - 2026-10-14 Fix parser` if not excluded and no stat lines survive. Hash `abc` is discarded, and `--date=short` supplies no HH:MM. Stat extraction retains only lines whose trimmed text starts with `| `, so ordinary `path | 4 ++--` lines do not survive. A returned line `- "09:00 - Fixed parser"` yields string `09:00 - Fixed parser`; against existing `10:00 - Review`, minute values 540 and 600 yield `["insert", "09:00 - Fixed parser", 0]`. That is non-ampliative reformatting/position selection of the candidate text, not evidence that work occurred at 09:00. `[]` extracts zero entries and fails despite being allowed in the prompt. A counterexample to a blanket no-check claim is the subprocess exit and empty-list check; neither checks historical accuracy.

> const GIT_DATE_FORMAT = "short";
> --- `examples/journal/git-import-logs.ts`

> return `  - ${date} ${msg}${changes.length > 0 ? `\n    Files: ${changes.join(", ")}` : ""}`;
> --- `examples/journal/git-import-logs.ts`

> .filter((line: string) => line.trim().startsWith("| "))
> --- `examples/journal/git-import-logs.ts`

> const entry = trimmed.slice(1).trim().replace(/^"/, "").replace(/"$/, "");
> --- `examples/journal/git-import-logs.ts`

#### EPI-RTE-import-mapping
Label: Human-approved import mapping

No counterpart after comparison with [RT-RTE-graph-update](runtime.md#rt-rte-graph-update): this is a shipped agent procedure before executable graph admission, not another write implementation. SRC-1, `skills/binder-import/SKILL.md`. User triggers import; host agent samples source, inspects schema, proposes mapping and duplicates, generates batches, previews and asks approval to apply. Human can veto mapping/batches; graph software independently rejects malformed writes. Intended use is mapped operational records; criterion is compatible meaning/types, disclosed skipped fields and chosen duplicate handling, not independent truth verification. Stable-key upserts substitute for per-record search; fuzzy matches require user decisions. Operating mode open import, no answer oracle. Recovery requested via undo; generated YAML and tracking support resumption.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested mapping, deduplication report and batch results.
- Later read-back: imported graph records become search/read inputs; YAML retained until import verified.
- Delegated visibility: user sees proposal/preview; host gets source samples and schema, not necessarily entire large source.
- Selection predicate: source format/size, natural key, batch size, dependency order and user approval.
- Invalidation or expiry: schema gaps pause import; subsequent updates/undo change admitted records.
- Activation or effect: natural-language policy requests human approval; underlying CLI can operate without this procedure.
- Evidence limits: doctrine only; source warrant unknown, no executed approval or lossless conversion established.

> **Wait for user confirmation before proceeding.**
> --- `skills/binder-import/SKILL.md`

> Only after user approval:
> --- `skills/binder-import/SKILL.md`

#### EPI-RTE-journal-review
Label: Journal evidence review and later planning

Distinct from [RT-RTE-git-import](runtime.md#rt-rte-git-import), which prints candidate log insertions, and [RT-RTE-task-guide](runtime.md#rt-rte-task-guide), which targets product work. SRC-1, `examples/journal/skills/day-summary/SKILL.md`, `examples/journal/skills/period-summary/SKILL.md`, `examples/journal/skills/period-update/SKILL.md`, `examples/journal/skills/day-next-plan/SKILL.md`. External host agent reads target/related entries, proposes summaries/scores/insights; person corrects/confirms; agent is instructed to save accepted journal text and carry agreed work forward. Criterion is consistency with activity records and user corrections for personal journal/planning scope. Child completion signals and explicit abandonment classify done/next/drop; unlogged work is not automatically nonoccurrence. User can veto/correct; software admission checks structure separately. Operating mode open personal review, no independent answer oracle. Prompt guidance persists as static skill; confirmed fields and plans can persist via Binder; no durable confirmation/evidence-link record is required by these prompts.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed reflection, scores, uncertain items and confirmed update instructions.
- Later read-back: period-summary reads children's learnings/summaries; period-update reads retained learning lines; day-next-plan reads source summary and achievements to decide future plan.
- Delegated visibility: selected graph fields and conversation reach external host agent/user; automatic extra context depends on uncaptured extension.
- Selection predicate: period/day offset, parent/children relations, recent entries, incomplete items and human corrections.
- Invalidation or expiry: confirmation can revise/remove proposals; later updates replace fields; explicit drop prevents carry-forward.
- Activation or effect: advisory interpretation and prompt-requested writes/plan changes, not runtime-enforced approval or measured behavior change.
- Evidence limits: doctrine only; no accepted claim instance, observed write, reliable arithmetic execution or causal capacity improvement.

> Gaps may mean "not logged yet" rather than "didn't happen" — ask "anything not captured yet?" rather than assuming omission.
> --- `examples/journal/skills/day-summary/SKILL.md`

> Correct based on my input. Ask at most one follow-up question, only for ambiguous status decisions. If I say "looks good," apply defaults and write.
> --- `examples/journal/skills/period-summary/SKILL.md`

> Confirm, then write.
> --- `examples/journal/skills/period-update/SKILL.md`

> **Flag zombie tasks** — anything that's been unfinished for 3+ consecutive days:
> --- `examples/journal/skills/day-next-plan/SKILL.md`

#### EPI-RTE-task-findings
Label: Task capture refinement and diagnosis

This spans preimplementation capture/refinement and the investigation part of [RT-RTE-task-guide](runtime.md#rt-rte-task-guide); not identical to that supplied whole guide-selection route and not wholly contained by it. SRC-1, `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/refine-backlog/SKILL.md`, `examples/workflow/skills/implement-task/guides/investigate.md`. User input is acquired; agent labels inferred fields, screens duplicates, proposes readiness and links, then requests approval. Readiness is sufficient description/constraints/testable criteria, not accepted explanatory truth. Investigation instead asks the agent to reproduce a bug, trace code, explain why and write diagnosis fields, then remove debug edits. Reproduction target is the reported symptom under recorded steps; root-cause target is the explanation of that symptom. The former is requested as an environment check; the latter lacks an independently enforced discriminating intervention. Human veto is explicit for capture/refinement, not per diagnosis update. Guidance is source, task and skill; open task work, no universal answer oracle. Common graph rollback applies to fields; cleanup asks to remove temporary code edits, not the diagnosis.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed/updated task or diagnosis, with debugging changes requested to be removed.
- Later read-back: task reread and nonempty diagnosis/design fields select subsequent guide/implementation through the supplied runtime route.
- Delegated visibility: task content, project source and guide text reach host agent; user sees approval proposals.
- Selection predicate: user task, missing fields, duplicate/overlap assessment, DoR and reproduction results.
- Invalidation or expiry: user corrections, cancellation/merge and later task updates can replace fields; no automatic explanation invalidation found in inspected files.
- Activation or effect: prompt-directed retention and guide selection; actual execution, approval and code effects unobserved.
- Evidence limits: doctrine only; symptom reproduction does not identify a unique mechanism or establish transfer.

> Propose changes to the user and wait for approval before executing
> --- `examples/workflow/skills/refine-backlog/SKILL.md`

> 1. **Reproduce.** Use `stepsToReproduce` if present. Otherwise, derive reproduction steps from `description` and `details`. Run the code and confirm the bug exists.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

> Remove any temporary changes you made during investigation (debug prints, scratch files). The goal is findings, not code changes.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

### Claims

#### EPI-CLM-agent-memory
Label: Typed persistent agent memory

Claimed operation: typed transparent persistent shared agent/person state, not universal factual endorsement. SRC-1, `README.md`, doctrine/design. No claim counterpart after comparison with [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary) and [RT-CLM-derived-effects](runtime.md#rt-clm-derived-effects), which assess transaction/effect boundaries rather than advertised use.

> - **Agent context and memory** so your AI tools have somewhere typed and persistent to share state among themselves and people. Structured, fully transparent and easy to maintain.
> --- `README.md`

#### EPI-CLM-period-learnings
Label: Evidence-grounded period learning lines

Claimed operation: propose concrete personal insights and external information grounded in period activity, merge existing lines, obtain corrections and write final learnings. Source-native learning-field claim, not by itself a claim of improved system capacity. SRC-1, `examples/journal/skills/period-summary/SKILL.md`, doctrine/design. No counterpart in supplied runtime Claims; distinct from the storage/use claim above.

> Propose `learnings` based on actual period activity (children logs, achievements, events, and summaries), then merge with any learning lines already captured on the target period entry. Keep it concrete. Learnings are composed of personal insights and information from external sources like articles.
> --- `examples/journal/skills/period-summary/SKILL.md`
