---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "pi-self-learning memory: trace-derived journals, scored canonical rules, lossy renders and later-turn delivery."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
source-identity: https://github.com/mcollina/pi-self-learning
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
---

# pi-self-learning memory report

## Boundary and evidence

The subject is the complete extension package at the revision above, not the enclosing pi agent. Memory scope follows the supplied runtime's reflection, maintenance, control and injection routes. It includes branch transcript acquisition, process-local notes, project/global files, initialization/migration, repair, monthly summarization, redistillation, ranking, Git attempts and file consultation instructions. Host transcript persistence, provider weights, host tools and actual user-created memory are outside the inspected source set. Their absence from this evidence prevents claims about deployment, model compliance, actual retained theories and improvement.

SRC-1 is the sole source in [boundary](boundary.md). Direct inspection covered the memory-relevant portions of `extensions/self-learning.ts`: settings/path resolution, parsing/repair, transcript filters and prompts, Git helpers, all index/ranking/render/redistill code, context selection, reflection/monthly producers, both hooks and every registered command handler. `README.md`, `AGENTS.md` and `package.json` were read directly. Model/auth internals within the extension are taken from the supplied runtime rather than independently re-audited here. Evidence is implementation and doctrine/design only; no target execution, traces or experiments were supplied or performed.

| Entry point or operation | Source path, SRC-1 | Coverage and supporting records | Limit/conclusion prevented |
|---|---|---|---|
| `agent_end`, `/learning-now`; branch tail and execution signals | `extensions/self-learning.ts` | Direct read; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [MEM-OBJ-branch-messages](#mem-obj-branch-messages), [MEM-OBJ-daily](#mem-obj-daily) | Host branch acquisition/serialization implementation external; selected text is not proof of task success. |
| JSON extraction, repair and admission | `extensions/self-learning.ts` | Direct read; annotation on [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | Syntax checks do not verify truth or prevention value. |
| Index load/migration, update, rank and rendering | `extensions/self-learning.ts` | Direct read; [MEM-OBJ-index-text](#mem-obj-index-text), [MEM-OBJ-index-ranking](#mem-obj-index-ranking), [MEM-OBJ-core](#mem-obj-core), [MEM-OBJ-long-term-memory](#mem-obj-long-term-memory) | Existing file authorship and contents unavailable; migration grants no provenance verification. |
| `/learning-month` | `extensions/self-learning.ts` | Direct read; [RT-RTE-month-summary](runtime.md#rt-rte-month-summary), [MEM-OBJ-monthly](#mem-obj-monthly) | No summary output; preservation of reasons unobserved. |
| `/learning-redistill`, preview, chunk repair/merge | `extensions/self-learning.ts` | Direct read; annotation on [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | Counts measure textual change/deduplication, not quality. |
| `before_agent_start`, file bundle and path policy | `extensions/self-learning.ts` | Direct read; annotations on [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) | Host application and actual consultation unobserved. |
| Runtime notes | `extensions/self-learning.ts` | Direct read; annotation on [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes) | Process lifetime only; not branch/root isolated. |
| Toggle, branch/global model settings, daily/status commands | `extensions/self-learning.ts` | Direct read of handlers and settings helpers; [RT-RTE-runtime-controls](runtime.md#rt-rte-runtime-controls); picker behavior from runtime | Not content approval. Daily/status commands report paths/settings rather than retrieving retained content. |
| Git initialization and commits | `extensions/self-learning.ts` | Direct read; Write side below; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | No successful commit evidence or shipped restore command. |
| CLI/tools/service surface | `package.json`, `extensions/self-learning.ts` | Direct package and registration inspection: single extension export, hooks and commands above | No separate CLI dispatcher, registered memory tool or service operation found in this inspected package; external host tools remain outside scope. |

## Core ideas

1. The journal is already derived memory, not a verbatim session log. The model sees a filtered branch tail plus selected error signals; its mistakes/fixes become both dated prose and canonical rule candidates. The raw session is not copied into the memory root ([MEM-OBJ-branch-messages](#mem-obj-branch-messages), [MEM-OBJ-daily](#mem-obj-daily)).
2. Canonical text and access metadata have different authority. Rule text ultimately influences a model through interpretation. Scores, hits, dates and kind drive deterministic rendering and redistill targeting; they do not evaluate correctness ([MEM-OBJ-index-text](#mem-obj-index-text), [MEM-OBJ-index-ranking](#mem-obj-index-ranking)).
3. There are several lossy descendants, not one complete memory: top-ranked core, all-current-rule long-term render, monthly summaries and short process notes. Daily entries retain the original accepted reflection wording; the index and renders do not retain an explicit link back to its supporting conversation or daily entry ([MEM-CLM-complete-history](#mem-clm-complete-history)).
4. Later-turn supply is automatic and recency/rank based, not query retrieval. Optional file consultation is separately requested through system instructions. Neither delivery nor the word “strict” establishes actual consultation or prevention benefit ([RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-branch-messages
Label: Selected branch messages and execution signals

Source-native identity: `getBranchMessages` output and `collectExecutionBoundarySignals` input/output. Substrate: host-owned session branch, then transient JavaScript arrays/serialized strings. Form: symbolic role/error/stop metadata and natural-language user, assistant and tool text. Original provenance is mixed human/model/tool activity; external host storage and any prior context conversion remain uninspected. This is the raw trace side relative to reflection, although branch filtering and serialization already select it. It is distinct from [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes), which holds derived reflection fragments; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) is the encompassing acquisition/write route, not the trace object.

Abort recognition filters aborted assistants and selected cancellation tool messages before taking the configured message tail (default eight). The separate signals scan considers the last `max(maxMessagesForReflection * 4, 24)` branch entries; it extracts at most eight deduplicated error-tool permission/blocking descriptions, with 180-character previews, excluding recognized user cancellations. Thus a signal can come from outside the serialized message tail. The completion receives both, but not the complete session, host system prompt or existing canonical memory as a separately loaded input. Its authority is evidence for model-authored mistakes/fixes, not an approval decision. SRC-1, `extensions/self-learning.ts`:

> .filter((message) => !isUserAbortMessage(message))
>     .slice(-Math.max(1, maxMessages));
> --- `extensions/self-learning.ts`

> const executionSignals = collectExecutionBoundarySignals(ctx, Math.max(config.maxMessagesForReflection * 4, 24));
> --- `extensions/self-learning.ts`

#### MEM-OBJ-daily
Label: Daily accepted reflection journal

Source-native identity: `daily/YYYY-MM-DD.md`, written by `appendDailyEntry` and `buildMarkdownEntry`. Substrate: UTF-8 filesystem files under the resolved root, optionally versioned in Git. Form: natural-language mistakes/fixes under time and Task/Manual headings; date/path and headings provide symbolic organization. Lineage is selected branch text and execution signals → model reflection → optional JSON repair → accepted string arrays → append. This is not raw transcript retention. There is no session ID, message ID, model ID, source quote or explicit mistake-to-fix relation in the written entry schema. Reasons may occur inside generated prose, but are not required or structurally preserved. Existing handwritten/legacy content is not supplied, so its authorship remains unknown.

Consumers: monthly completion reads assembled daily text; the automatic bundle can read selected recent files when configured; the foreground policy asks for daily-file consultation on historical questions. Model interpretation gives the prose evidential/advisory authority, not validated truth. Distinct from the process fragment in [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes); its write/read routes are [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) and [RT-RTE-context-injection](runtime.md#rt-rte-context-injection). SRC-1, `extensions/self-learning.ts`:

> lines.push("### What went wrong");
> --- `extensions/self-learning.ts`

> lines.push("### How it was fixed");
> --- `extensions/self-learning.ts`

> appendFileSync(file, content, "utf-8");
> --- `extensions/self-learning.ts`

#### MEM-OBJ-index-text
Label: Canonical index rule content

Source-native identity: `core/index.json` records' `text`, `key` and `kind`, loaded by `loadCoreIndex` and updated by `updateCoreFromReflection`. Substrate: JSON file and transient maps. Form: natural-language rule text; symbolic normalized key and kind determine identity and rendering class. Fixes become learnings; mistakes become `Avoid:` antiPatterns. Keys collapse whitespace and lowercase text; this is exact normalized-text deduplication, not semantic equivalence. Repetition can overwrite casing/text/kind for the matching key. No explicit source session, daily-entry pointer, reason field or validation result is retained. Prose can still contain reasons; absent dedicated fields do not prove absent explanation.

The alternative initialization path loads valid existing index items with coercion/defaults, or migrates all `- ` lines of `CORE.md` if the index is absent/invalid. Migration infers antiPattern only from a literal `Avoid:` prefix. This matters because generated core watch-outs strip that prefix: recovery from a rendered core can reclassify them as learnings and recover only the displayed subset. Subsequent reflection/rendering and redistill transformations are known even though pre-existing file control is unknown. Manual file edits are physically possible, but no per-item editing/approval UI is shipped. With a valid index, an edit to CORE can be injected temporarily yet is overwritten by later rendering; migration does not reconcile it into a valid index.

Consumers: renderers interpret kind/text structurally; redistill completion interprets selected text; later host models interpret rendered descendants. Its admission is software parse/normalization plus model proposal, not semantic review. It is distinct from all supplied runtime objects; closest routes are [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill). Ranking metadata is separately [MEM-OBJ-index-ranking](#mem-obj-index-ranking). SRC-1, `extensions/self-learning.ts`:

> function learningKey(text: string): string {
>   return normalizeLearningText(text).toLowerCase();
> }
> --- `extensions/self-learning.ts`

> kind: text.toLowerCase().startsWith("avoid:") ? ("antiPattern" as const) : ("learning" as const),
> --- `extensions/self-learning.ts`

> ? antiPatterns.map((item) => `- ${item.text.replace(/^avoid:\s*/i, "")}`)
> --- `extensions/self-learning.ts:1250-1252`

#### MEM-OBJ-index-ranking
Label: Canonical index ranking metadata

Source-native identity: `CoreIndexRecord.hits`, `score`, `firstSeen`, `lastSeen`; index `updatedAt` and `version`. Substrate: the same JSON file as [MEM-OBJ-index-text](#mem-obj-index-text), but a distinct symbolic operative part. New items receive hits/score 1; repeat matches increment hits, update lastSeen, and add `1 + min(1, hits * 0.08)` to score. Selection sorts by score minus 0.05 per age day, then hits, then lastSeen. When both kinds exist, the core selector reserves per-kind slots, then fills remaining capacity from ranked unused keys; this is not a pure global top-N. A configured limit of one returns the first selected learning when both kinds exist. Ranking is recomputed at render/redistill invocation, not by a background decay job.

Authority at consumers: fixed code chooses core membership/order and redistill targets from this metadata. Downstream host text does not include scores or hit counts, and no consumer interprets them as an independent correctness result. Redistill collision merging sums hits/scores and takes earliest firstSeen/latest lastSeen, preserving frequency history but not evaluation evidence. Distinct from [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes); closest runtime routes are [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill). SRC-1, `extensions/self-learning.ts`:

> const recencyPenalty = ageDays * 0.05;
>   return item.score - recencyPenalty;
> --- `extensions/self-learning.ts`

> const basePerKind = Math.max(1, Math.floor(limit / 2));
>   const pickedLearnings = learnings.slice(0, basePerKind);
>   const pickedAntiPatterns = antiPatterns.slice(0, basePerKind);
> --- `extensions/self-learning.ts`

#### MEM-OBJ-core
Label: Ranked core Markdown render

Source-native identity: `core/CORE.md`, generated by `renderCoreFromIndex`, with empty-file initialization by `ensureCoreFile`. Substrate: UTF-8 filesystem and optional Git history. Form: natural-language rule content under Learnings/Watch-outs display headings; no numerical ranking metadata is displayed. Lineage: current index → balanced score selection → selected text grouped by kind, with `Avoid:` removed in watch-outs. Default item cap is 20 before the later character caps. Omitted index items are not deleted. File contents can be read directly by the bundle independently of whether a usable index exists.

Consumers: automatic future-turn file bundle by default; foreground path consultation; fallback migration described in [MEM-OBJ-index-text](#mem-obj-index-text). The first two grant interpretive historical/advisory authority; migration grants canonical text authority by a fixed parser without authentication of file authorship. This object is distinct from the route [RT-RTE-context-injection](runtime.md#rt-rte-context-injection); no supplied object counterpart exists. SRC-1, `extensions/self-learning.ts`:

> const selected = selectBalancedCoreItems(index, maxItems);
> --- `extensions/self-learning.ts`

> "This file keeps only top-ranked, most repeated items.",
> --- `extensions/self-learning.ts`

#### MEM-OBJ-long-term-memory
Label: All-current-rule Markdown render

Source-native identity: `long-term-memory.md`, written by `renderLongTermMemoryFromIndex`; initialization may create an empty placeholder. Substrate: filesystem and optional Git. Form: natural-language all-current-index text grouped into learnings/watch-outs, stripped of antiPattern prefix, without per-item scores, timestamps, raw trace or rewrite history. Lineage is the ranked current index, not replay of the daily journal. Redistill changes this representation as well as the index/core; repeated keys and rewrite collisions do not preserve separate historical versions here.

Consumer: the system policy requests consultation of its path when stuck; it is not automatically bundled. This is an afforded external agent consultation route, not a shipped file-read tool or observed read. No host tool behavior is assumed. Distinct from [MEM-OBJ-core](#mem-obj-core) by coverage and read-back channel; closest supplied record is [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy). SRC-1, `extensions/self-learning.ts`:

> function renderLongTermMemoryFromIndex(root: string, index: CoreIndex): string {
>   const sorted = sortedIndexItems(index);
> --- `extensions/self-learning.ts`

> `5) If you are stuck and need help, consult ${longTermPath} for broader prior fixes and mistakes.`,
> --- `extensions/self-learning.ts`

#### MEM-OBJ-monthly
Label: Monthly model-derived summary

Source-native identity: `monthly/YYYY-MM.md`, generated by `generateMonthSummary`. Substrate: UTF-8 filesystem, optional Git. Form: natural-language Markdown with generation timestamp. Lineage: filename-matched, sorted daily files → concatenation with filename headings → 180000-character prefix → separate completion → nonempty text admission → overwrite. This summarizes already derived reflections, not raw conversation. The Wins/Recurring issues/Most important learnings sections are requested, not checked. The model receives filename context but no explicit source-reference or reason-preservation requirement. Summaries may retain rationale in prose; outputs are unavailable.

Consumers: latest monthly file optionally enters automatic context; policy requests monthly consultation after daily logs. No monthly-to-index/core promotion is implemented. Regeneration overwrites the month without semantic comparison; daily edits do not automatically invalidate it. Distinct from all supplied runtime objects; its producer is [RT-RTE-month-summary](runtime.md#rt-rte-month-summary). SRC-1, `extensions/self-learning.ts`:

> const monthly = writeMonthlySummary(
>     root,
>     month,
>     `# Monthly Summary ${month}\n\nGenerated: ${new Date().toISOString()}\n\n${summary}\n`,
>   );
> --- `extensions/self-learning.ts`

### Routes

none declared in this member

### Claims

#### MEM-CLM-complete-history
Label: Complete history render claim

The README calls `long-term-memory.md` full history; the generated title text also says complete history. Implementation supports all current indexed rules, not complete session history, all accepted wording versions, or redistill provenance. Daily accepted reflections remain separate; optional successful Git commits can retain earlier file versions, but the extension's read-back does not inspect Git history. This is distinct from [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation): the issue is retained content completeness rather than instruction enforcement. Evidence: [MEM-OBJ-index-text](#mem-obj-index-text), [MEM-OBJ-long-term-memory](#mem-obj-long-term-memory), SRC-1, `README.md`, `extensions/self-learning.ts`.

> 4. writes full history to `long-term-memory.md`,
> --- `README.md`

> "Complete history of durable learnings and recurring mistakes.",
> --- `extensions/self-learning.ts:1266-1269`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes)

Lineage is accepted reflection → first mistake, otherwise first fix → 180-character prefix → module array → last configured N notes at a later hook. It is derived natural-language content, not an access index or copy of the raw trace. Source-local reasons and fixes can be lost because only one fragment escapes. The same process can hold notes from different resolved roots/branches; there is no source-path metadata in each note. Physical write and eviction are code controlled, while content is model authored. Actual foreground influence is unobserved. SRC-1, `extensions/self-learning.ts`; the supplied record retains the decisive append/eviction quote.

#### On [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)

Raw-to-derived-to-consumer chain: [MEM-OBJ-branch-messages](#mem-obj-branch-messages) → reflection/optional repair → [MEM-OBJ-daily](#mem-obj-daily) plus [MEM-OBJ-index-text](#mem-obj-index-text) and [MEM-OBJ-index-ranking](#mem-obj-index-ranking) → core/long-term renders and process note → later bundle or requested consultation. This is an automatic trace-fed behavior-shaping write path for the event hook; manual reflection invokes the same transformation. It is not weight training or mere raw-log storage. There is no separate alternative checkpoint/host-compaction form in this extension's reflection path.

Admission distinguishes humans initiating/enabling the workflow from approving its generated content: the model proposes, the parser admits either nonempty normalized array, software writes all accepted entries. Requested array length and project/global scope are not validated. A global prompt asks removal of project specifics; source code establishes the request, not effective anonymization or generality. The repair call sees a prefix of raw model output (6000 characters), not the conversation, so repaired prose has an additional model-mediated provenance step. Invalid output is rejected before daily/index writes; no durable rejected-candidate record is written by this path. Manual UI can display previews; that is not a later memory consumer.

Reasons are optional inside strings. Daily prose can retain them, but core/index do not guarantee them, and no later route reconstructs reasons from source messages. The supplied route's learning and theory limits remain: localized rules are afforded, content-dependent foreground use/criticism/iteration and improved future capacity are unobserved. SRC-1, `extensions/self-learning.ts`:

> "- Remove project-specific details (file names, module names, internal identifiers, phase labels, ticket references).",
> --- `extensions/self-learning.ts`

> compactText(rawModelOutput, 6000),
> --- `extensions/self-learning.ts:419-431`

#### On [RT-RTE-month-summary](runtime.md#rt-rte-month-summary)

This is a second model curation step over retained derived journal text, not an independent evaluation. Human month selection is not content approval; software accepts any nonempty text. Older daily content gets priority under ascending concatenation and prefix truncation. Output is durable [MEM-OBJ-monthly](#mem-obj-monthly), not an index replacement. Later monthly consumption remains optional or requested; no supplied output establishes preservation of reasons or improvements over the dailies. SRC-1, `extensions/self-learning.ts`; supplied route retains writer/admission evidence.

#### On [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill)

Curation consumes selected canonical text, kind and transient integer IDs, not raw transcript, daily explanations or score metadata in its model prompt. It asks preservation of original meaning while removing project identifiers. Parser acceptance of a nonempty mapping is weaker than the requested one-result-per-ID contract: missing IDs fall back to original text; extra IDs have no matching target. Code enforces `Avoid:` polarity, normalizes whitespace and rekeys; collision merging adds ranking metadata. Neither semantic preservation nor improved explanatory scope is evaluated. UI change/dedup counts compare normalized text/keys, not outcomes.

The new index/core/long-term descendants replace current rules, while daily and monthly prose and existing runtime notes are not revised. Thus later consumers can receive inconsistent old/new formulations; no propagation withdrawal or rejection ledger resolves that. Human invocation, limit, large-run confirmation and dry-run are coarse controls, not per-rule acceptance. A parse failure after repair prevents final rewrite; final multi-file I/O is not transactional. Dry-run suppresses final writes but can initialize missing core through load/migration. Existing evidence does not establish claim-directed criticism, iterative theory building or successful self-improvement. SRC-1, `extensions/self-learning.ts`; supplied route retains preservation/fallback passages.

#### On [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Push selector: code at every enabled `before_agent_start`; inputs are settings, root, runtime note order and available dated filenames, not user query terms. Selected material is notes tail, optionally core, last N dailies in ascending date order, then latest monthly. Core selection was decided at its last render, not reranked by this hook. Default disk supply is core only; notes remain independent.

Budget: file bundle uses at least 2000 characters, default 12000, and per-file prefixes of at least 1000 or floor(bundle/4), then an aggregate prefix including headers. Earlier core/daily sections displace later monthly sections; even a displayed core can lose its later watch-outs. Truncation is by JavaScript string length, not tokens or whole items; markers add characters beyond the sliced prefix. Runtime notes and appended system policy are outside this cap. Delivery is hidden custom-message text by value; display suppression does not lower model visibility. Policy paths afford external retrieval, but no extension retrieval action is triggered by a historical query.

Working-context control: reflection, repair, summary and redistill calls isolate selected inputs in independent completion requests, returning only parsed/text results to extension code. They resemble separate frames; no nested worker is spawned. The foreground transcript is not compacted or evicted by this package. Files remain externally reachable through host capabilities, not live references automatically followed by the window; there is no liveness/reference-count mechanism. SRC-1, `extensions/self-learning.ts`; the supplied route retains budget and system-prompt quotes.

#### On [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy)

Disk prose and notes are labeled historical evidence; static consultation policy has system-prompt placement while retained content arrives in a separate hidden message. These are different authority channels. Canonical metadata acts earlier at render/selection code, not as a downstream truth oracle. No authenticated origin label, semantic trust filter or correctness score is added before text delivery in the inspected bundle builder. The policy asks preference for memory evidence but cannot make model-generated reflections true. Source origin and code wiring support an interpretive authority path, not compliance. SRC-1, `extensions/self-learning.ts`; the supplied authority record retains both policy and historical-evidence passages.

## Write side

Admission mechanisms are deliberately separate from physical I/O:

| Mechanism | Who authors/proposes | Who admits or vetoes content | Retained effect and recovery |
|---|---|---|---|
| Reflection and repair | Model over mixed session trace; model again over malformed-output prefix if needed | Code checks string arrays; human can configure/disable/start, not approve items | Daily append, canonical updates/renders, note; invalid parse skips; no semantic veto or transaction. |
| Existing-index load and CORE migration | Existing author unresolved; parser constructs imported records | Code coercion/filtering or bullet/prefix rules, no origin check | Existing valid index wins; fallback CORE migration can lose omitted records and watch-out kind. |
| Ranking and duplicate updates | Code transforms accepted content and metadata | Fixed normalized-key and kind/rank rules | Ranking exclusion is not deletion; no correctness assessment. |
| Monthly rewrite | Model over bounded daily text | Code nonempty check; human chooses month | Same-month overwrite; older versions only conditionally in Git. |
| Redistill | Model over indexed text; code prefix/rekey/merge | Code parse/ID fallback; human scope/preview/coarse confirmation | Replaces selected current rules, merges collisions; no semantic oracle or automatic rollback. |
| Settings/toggle | Human selected values; code serializes | Reference validation for model settings, latest branch toggle for enabled state | Changes producer/consumer controls, not approval of memory content. |

All rows are SRC-1, `extensions/self-learning.ts`, grounded by the corresponding object records and supplied route annotations above. The extension exposes files as operational editing surfaces, but no item-by-item editor, reject button or automatic cleanup/withdrawal command is registered. This is a bounded registration/implementation finding, not a claim that external file editing is impossible. Hand edits to a valid index affect later rendering; edits to rendered files can affect immediate reads but are disposable on regeneration. Deleting an index alone is not a reliable withdrawal: fallback CORE migration may re-admit displayed text. Removing current index content does not erase old daily/monthly text or process notes.

Git is optional and best effort. Initialization can create a static README and empty long-term file, then attempts an initial commit. Reflection/monthly/redistill call helpers for later commits. These initialization boilerplates are static shipped content, not accumulated memory. Successful history could support external manual restoration, but the shipped read-back only uses current files and runtime notes. No extension route consumes commit history, no automatic rollback repairs a partial write, and commit failure does not retract already written content (SRC-1, `extensions/self-learning.ts`):

> const add = runGit(root, ["add", ...rel], GIT_FAST_TIMEOUT_MS);
>   if (!add.ok) return;
> --- `extensions/self-learning.ts`

## Read-back

There are three distinct later-consumer chains, all wired or afforded rather than observed:

- **Update consumers:** existing index/current CORE can enter a later reflection update or redistill; daily files enter a later monthly completion. These are actual shipped consumer invocations, not hypothetical storage APIs. Admission and budgets differ as recorded above.
- **Automatic agent supply:** the hook selects notes and file prefixes independently of the current question, returning them to the host. File root is project/global, not per-agent identity. Branch enablement controls admission to this hook, not disk partitioning. `context.enabled: false` removes file bundle/policy but not recent notes; `instructionMode: off` removes policy but not file supply ([RT-RTE-context-injection](runtime.md#rt-rte-context-injection)).
- **Requested foreground consultation:** policy names core, daily, monthly and long-term paths. This is documented/instructed external-agent read-back with no shipped extension read tool or read-verification gate. User history questions/stuck state are model-interpreted conditions, not an extension semantic selector ([RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy)).

The content reaches these consumers after lossy transformations. Raw transcript is not reconstructed from the daily files; index does not reference daily evidence; long-term text omits ranking metadata/history; monthly text can omit recent dailies under its prefix budget; short notes can omit the fix. Delivery establishes availability, not reliance, correctness or successful prevention.

## Integration issues

- **No correction to supplied runtime facts is required.** Source inspection supports its distinctions concerning manual gating, ignored branch model override, strict policy, context disablement and dry-run initialization. The report adds a migration caveat rather than contradicting it: reconstructing index from generated CORE can classify stripped watch-outs as learnings and recover only the rendered subset ([MEM-OBJ-index-text](#mem-obj-index-text), [MEM-OBJ-core](#mem-obj-core)). This prevents treating migration as complete faithful recovery.
- **No new record is a possible duplicate after comparison.** New records name retained objects/parts not declared by runtime, except [MEM-CLM-complete-history](#mem-clm-complete-history), which concerns a different claim. Existing route, notes and foreground authority referents are annotations, not redeclarations. Canonical text and ranking deliberately split operative parts of one JSON substrate; their later consumers and authority differ.
- **Unresolved external behavior:** actual host application of hidden messages/prompt, subsequent reads and content-dependent decisions are unavailable ([RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy)). This prevents upgrading delivery to activation.
- **Unresolved content and provenance:** actual legacy/index/generated strings, their author control and any retained causal reasons are not supplied ([MEM-OBJ-daily](#mem-obj-daily), [MEM-OBJ-index-text](#mem-obj-index-text), [MEM-OBJ-monthly](#mem-obj-monthly)). Known transformation requests remain established; faithful generalization, criticism and trace-grounded improvement do not.
- **Unresolved durability/concurrency:** deployed filesystem/Git results and host scheduling are unavailable. Optional history is not guaranteed recovery; independent callbacks/processes are not shown to serialize writes ([RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill)).

## Limitations and checks

The checkout HEAD was rechecked against the frozen revision. All findings remain within SRC-1 and the package boundary; no provider/host documentation or prior analyses were introduced. Source reads were read-only; no target code, tests, examples or service calls ran. The supplied method/type/records contracts govern this report; no source instructions were treated as worker authority.

There is no observed-run or causal-experiment layer. Source wiring establishes trace-fed retention and future delivery, not exercised self-improvement, model adherence, semantic preservation, safe anonymization, criticism quality or measured prevention. The supplied `commonplace-run validate-output` command passed: “Member content check passes; invocation residue not checked.” This establishes checked structure and quotation occurrence, not analytical correctness, claim support or job acceptance.
