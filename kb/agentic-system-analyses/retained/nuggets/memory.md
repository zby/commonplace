---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Nuggets memory: JSON facts, reconstructed HRR retrieval, session snapshots, automatic capture and conditional Markdown promotion."
run-id: AAS-2026-10-14-nuggets-c2e87e6916cc-01
source-identity: "https://github.com/NeoVertex1/nuggets"
reviewed-boundary: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
---

# Nuggets memory report

## Boundary and evidence

This report covers the shipped TypeScript memory library, Pi memory extension, migration and promotion writers, and the gateway's later consumers at SRC-1 commit `714cab8a3b1fb843aa98dfb51584d2c07a6739f3`. It follows the whole-system boundary in [boundary](boundary.md). The advertised but absent plugin workspace, external Pi internals, provider state and actual Claude loading remain outside inspectable implementation. No live facts, sessions, deployed configuration or execution traces were supplied. Findings below establish implementation wiring, not exercised memory use or benefit.

Direct reads covered all of `src/nuggets/{memory,shelf,kinds,promote,index}.ts`, `.pi/extensions/nuggets.ts`, `src/migrate-memory.ts`, `package.json` and `tests/memory.test.ts`. Core arithmetic, gateway, proactive extension, setup and doctrine findings are supplied by [runtime](runtime.md) and [boundary](boundary.md), not independent reads in this member. These are implementation and doctrine/design layers of SRC-1, not new sources. Checkout HEAD was rechecked against the full frozen revision and its status was clean.

| Entry point / operation | Source paths under SRC-1 | Coverage and conclusion limit |
|---|---|---|
| Tool remember/forget/list, command overlay | `.pi/extensions/nuggets.ts` | Direct; [MEM-RTE-fact-mutation](#mem-rte-fact-mutation), [MEM-RTE-recall-selection](#mem-rte-recall-selection); rendering is not a second memory store. |
| Input, tool-result capture | `.pi/extensions/nuggets.ts`, `src/nuggets/kinds.ts` | Direct; [MEM-RTE-hook-capture](#mem-rte-hook-capture). Failure/success of original tool is not checked. |
| Lifecycle reconstruction, hydration and injection | `.pi/extensions/nuggets.ts` | Direct; [MEM-RTE-context-rebuild](#mem-rte-context-rebuild), [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt). Host session serialization remains opaque. |
| Before/after compaction | `.pi/extensions/nuggets.ts`, `src/nuggets/promote.ts` | Direct; [MEM-RTE-compaction-extract](#mem-rte-compaction-extract), [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion). Host summary and retained tail are uninspected. |
| Public library CRUD, save/load, arbitrary shelf names | `src/nuggets/{memory,shelf,index}.ts` | Direct; [MEM-OBJ-nugget-facts](#mem-obj-nugget-facts), [MEM-RTE-fact-mutation](#mem-rte-fact-mutation), [MEM-RTE-recall-selection](#mem-rte-recall-selection). Generic API callers do not establish deployed consumers or human approval. |
| Numerical rebuilding and decoding | `src/nuggets/memory.ts`, `src/nuggets/core.ts` | Memory layer read directly; core supplied by [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors). No numerical performance experiment. |
| Legacy migration | `src/migrate-memory.ts`, `src/nuggets/kinds.ts`, `package.json` | Direct; [MEM-RTE-legacy-migration](#mem-rte-legacy-migration). No live migration result. |
| Gateway persistence and later turns | `src/gateway/{pi-pool,pi-rpc,router}.ts`, `gateway/src/` | Supplied [RT-RTE-message-turn](runtime.md#rt-rte-message-turn); session continuation requested, not independently established. |
| Scheduled request, job maintenance, proactive consumers | `.pi/extensions/proactive.ts`, `src/gateway/{cron,heartbeat,router,main,event-queue}.ts` | Supplied [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs), [RT-RTE-schedule-admission](runtime.md#rt-rte-schedule-admission), [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn). Included retained prompts; no duplicate declarations. |
| Evaluation | `tests/memory.test.ts`, `tests/core.test.ts` | Memory assertions directly read; core tests supplied by boundary. Tests not executed and not an online admission oracle. |
| Setup and usage instructions | `src/setup.ts`, `CLAUDE.md`, `NUGGETS_INSTRUCTIONS.md`, `README.md` | Supplied boundary/runtime; setup changes configuration, not per-fact approval. Root manifest has gateway/setup/migration scripts, no shipped memory CLI dispatch. Documentation does not establish Python or plugin implementation. |
| Opaque host/provider context | External Pi/provider, as identified in boundary | No frozen implementation; cannot enumerate provider checkpoints, host summary forms or host tool grants. Known extension extraction remains describable despite that limit. |

## Core ideas

Nuggets retains readable key/value strings, not just holographic vectors. Numerical vectors are rebuilt from those strings and configuration; direct fact enumeration and prompt hydration bypass numerical decoding. HRR recall first resolves a key with string/token rules, then selects a value from the current stored-value vocabulary. Its confidence is a decoding score, not a truth check. See [MEM-OBJ-nugget-facts](#mem-obj-nugget-facts), [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors) and [MEM-RTE-recall-selection](#mem-rte-recall-selection).

The extension has two partly independent memories: filesystem nuggets and a local facts map with session-history snapshots. It refreshes the shelf on operations, but does not continuously reconcile local prompt facts with disk. A model may therefore receive a local value in the system prompt and a different shelf value on explicit recall. Default kind names organize content, not users or repositories. See [MEM-RTE-context-rebuild](#mem-rte-context-rebuild) and [RT-RTE-memory-context](runtime.md#rt-rte-memory-context).

Automatic retention is rule-driven, not reviewed knowledge admission. Preference regexes, file-path capture and pre-compaction extraction derive short records from traces without preserving the source message, validation result or explanation. Those records later reach the model as memory text. The label “Learnings” does not establish improved capacity. See [MEM-RTE-hook-capture](#mem-rte-hook-capture) and [MEM-RTE-compaction-extract](#mem-rte-compaction-extract).

Withdrawal does not propagate through all copies. Local deletion may skip disk deletion, snapshot replay does not treat missing keys as tombstones, and promoted Markdown is merged rather than synchronized against deleted facts. These are distinct retained-copy mechanisms, not a global forget operation. See [MEM-RTE-fact-mutation](#mem-rte-fact-mutation), [MEM-RTE-context-rebuild](#mem-rte-context-rebuild) and the annotation on [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-nugget-facts
Label: Nugget fact content

Identity: `Nugget._facts` key/value content, persisted in `<name>.nugget.json`, normally under the OS user's `~/.nuggets`. Keys are symbolic lookup/routing identifiers; values are readable strings whose substantive meaning is interpreted by the later model or human. Disk JSON and the in-memory array are substrates, not representational forms. This is distinct from the numerical component [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors), which is reconstructed from these facts, and from the encompassing integration route [RT-RTE-memory-context](runtime.md#rt-rte-memory-context). SRC-1: `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`, `.pi/extensions/nuggets.ts`.

Lineage includes model remember calls, fixed capture hooks, generic library callers, loaded files and migration. Initial live content is unavailable. Facts retain no dedicated origin, evidence, timestamp or rationale field. A value can itself contain a reason, but the schema does not require one. Consumers include rebuilding/decoding code, direct enumeration, extension hydration and promotion. The model receives rendered text or tool text rather than the JSON envelope. Default `user`, `project`, `agent` names are categories, not isolation boundaries. Nondefault nuggets can be created through tool override or library calls, but default extension hydration and kind recall exclude them.

> interface Fact {
>   key: string;
>   value: string;
>   hits: number;
>   last_hit_session: string;
> }
> --- `src/nuggets/memory.ts`

#### MEM-OBJ-hit-metadata
Label: Fact hit metadata

Identity: the `hits` and `last_hit_session` fields attached to each persisted fact. Symbolic counters and a session marker are consumed by fixed code, not assertions of fact content. Same JSON substrate as [MEM-OBJ-nugget-facts](#mem-obj-nugget-facts), different update and consumer semantics. No supplied object counterpart; [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion) describes the downstream route. SRC-1: `src/nuggets/memory.ts`, `src/nuggets/promote.ts`.

A caller-supplied nonempty session ID enables incrementing when different from the last marker. This is not a set of all historically seen sessions: alternating old IDs can increment again. Existing key overwrite preserves the counters, so a changed value can inherit the old value's promotion eligibility. Migration takes the maximum hit count on collisions. Promotion consumes `hits >= 3`; it is an access-frequency gate, not validation or criticism. Ordinary extension recall supplies no session ID and thus creates no such hit update.

> if (fact.last_hit_session !== sessionId) {
>         fact.hits = (fact.hits || 0) + 1;
>         fact.last_hit_session = sessionId;
>         if (this.autoSave) this.save();
>       }
> --- `src/nuggets/memory.ts`

#### MEM-OBJ-session-facts
Label: Session facts and snapshots

Identity: extension-local `Map<string,string>` and the `NuggetsDetails.facts` records returned with memory tool results. Substrates: extension process RAM and, conditionally on external Pi retention, session tool-result details. Symbolic keys index natural-language values/path strings. Not the complete raw conversation or the shelf's access metadata. Distinct from disk facts [MEM-OBJ-nugget-facts](#mem-obj-nugget-facts); nearest supplied counterpart is integration [RT-RTE-memory-context](runtime.md#rt-rte-memory-context). SRC-1: `.pi/extensions/nuggets.ts`.

Lineage: branch replay, missing-key shelf hydration on session start, explicit writes and automatic captures. Each tool result snapshots the current local map, not every shelf. Later consumers are branch reconstruction, system-prompt formatter, local recall/list, and command overlay. UI recall truncation at 80 characters changes display, not the actual tool-return text. No opaque payload is hidden behind the displayed fact count; details contain a readable map, while the UI can show only a summary.

> function factsToRecord(): Record<string, string> {
> 	return Object.fromEntries(facts);
> }
> --- `.pi/extensions/nuggets.ts`

#### MEM-OBJ-task-summary
Label: Compaction task summary

Identity: `_task` value derived before host compaction and stored in local facts and the project nugget. Natural-language text under a symbolic key, on RAM/JSON substrates. A distinct part of [MEM-OBJ-nugget-facts](#mem-obj-nugget-facts) with special read-back filtering; supplied [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) already mentions it but does not declare this operative object. SRC-1: `.pi/extensions/nuggets.ts`.

The value concatenates the last three selected user messages, capped at 200 characters. It is extractive text, not the host's abstractive summary or a validated account of task completion. Reasons beyond that prefix are not retained here. Explicit recall/list can expose it; ordinary system-prompt injection and overlay filtering omit underscore keys. Its capture alone therefore does not establish automatic task restoration.

> const taskSummary = userMessages.slice(-3).join(" | ").slice(0, 200);
> 			facts.set("_task", taskSummary);
> 			shelfRemember("_task", taskSummary, "project");
> --- `.pi/extensions/nuggets.ts`

#### MEM-OBJ-promoted-memory
Label: Promoted Markdown memory

Identity: `MEMORY.md` in the current working directory's Claude-project memory directory. Natural-language fact text organized by symbolic section/key formatting; filesystem Markdown substrate. Distinct from its supplied producer [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion), not another producer route. SRC-1: `src/nuggets/promote.ts`.

Lineage: qualifying shelf facts plus parseable existing Markdown entries. Output includes section, key and value, not access metadata or original evidence. Only `##` headings and `- **key**: value` entries under sections survive parsing as entries. Free-form prior text is not generally preserved on rewrite. The intended later reader is external Claude; no included loader establishes its consumption. The “permanent context inclusion” source comment is intent, not a verified host guarantee. Merge retains old entries even when their shelf facts disappear; library forget/remove/clear do not retract this separate output.

> const factMatch = stripped.match(/^-\s+\*\*(.+?)\*\*:\s*(.+)$/);
> --- `src/nuggets/promote.ts`

### Routes

#### MEM-RTE-fact-mutation
Label: Fact mutation admission
Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

This route details explicit extension mutations within the supplied integration container; library CRUD is the underlying capability. Model chooses remember key/value, optional kind/name or forget key. Extension code decides required-field acceptance and kind fallback, then mutates the local map and shelf without human per-item approval. Library callers' human/software provenance is unresolved in general. Trimmed empty key/value is rejected silently by the library, whereas the local map is assigned before that trim check. Guidance asks for useful discoveries, preferences and one-sentence values; brevity is not a hard library length limit. Operating mode is open use; no answer oracle checks truth or usefulness. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool text reports remembered/forgotten/not-found or missing-field error and includes a local-facts snapshot; library remember returns void and forget returns removal boolean.
- Later read-back: Disk facts can hydrate new sessions, feed recall or promotion; local facts feed subsequent injection and details replay.
- Delegated visibility: Model sees formatted result and local facts through integration; direct library callers can enumerate facts, not just decoded answers.
- Selection predicate: Optional named nugget overrides; otherwise explicit valid kind or heuristic inference; updates compare shelf keys case-insensitively, while the local Map uses exact keys.
- Invalidation or expiry: Library forget/clear and shelf remove genuinely delete their own store; optional positive maxFacts evicts oldest insertion entries, default zero is uncapped. Local `facts.delete(...) || shelfForget(...)` skips disk deletion when local deletion succeeds. No propagation to old details or Markdown.
- Activation or effect: Retained facts and local state mutate, conditionally save; actual later model behavior unobserved.
- Evidence limits: No live store, concurrency test or external host trace; physical writes establish neither factual correctness nor durable global withdrawal.

Overwrite marks the numerical state dirty and normally saves via temporary file then rename. It preserves a matching fact's key spelling and hit metadata. There is no cross-process merge/lock; refreshing before mutation narrows staleness but does not make concurrent read-modify-write transactional. Recovery is another write or underlying deletion, not historical version rollback. Missing-field rejection is code admission; model authorship and filesystem I/O do not amount to human approval. The short-circuit evidence is retained in [RT-RTE-memory-context](runtime.md#rt-rte-memory-context).

> if (f.key.toLowerCase() === key.toLowerCase()) {
>         f.value = value;
>         found = true;
>         break;
>       }
> --- `src/nuggets/memory.ts`

#### MEM-RTE-hook-capture
Label: Automatic hook capture
Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Triggers: non-extension input and named tool results. Extension regex/path rules both propose and admit records; no separate human approval or truth oracle exists. Operating mode is ongoing use. Input authorship can be human-origin or other host-origin text; the code excludes source `extension` but does not authenticate human authorship. Tool paths originate in tool-call inputs exposed on result events, not file-content understanding. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/kinds.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hooks continue processing after local-map assignment and default autosaved kind write; no per-item admission receipt to the user.
- Later read-back: User preferences/learnings and project file facts hydrate future sessions and enter local per-turn prompt injection or requested recall.
- Delegated visibility: Later model receives short value/path and transformed key, not original message, tool status or surrounding rationale.
- Selection predicate: First match among always-use, prefer, never and remember-that patterns; value capped at 100 characters, derived key prefix plus first 30 characters. Tool path must be a string under file_path/path and tool name read/edit/write; basename becomes key suffix.
- Invalidation or expiry: Key collisions overwrite; same basename can conflate distinct directories. Underlying forget has the integration defects described above. No hook-specific expiry or approval veto.
- Activation or effect: Raw input/tool traces become durable short facts and potentially later prompt context, not merely raw logs.
- Evidence limits: No success check on the source tool, no reference outcome, no retained source link; correct preference extraction and useful later action unobserved.

> const value = match[1].trim().slice(0, 100);
> 			const shortKey = value.slice(0, 30).replace(/\s+/g, "-").toLowerCase();
> 			return { key: `${prefix}:${shortKey}`, value };
> --- `.pi/extensions/nuggets.ts`

#### MEM-RTE-context-rebuild
Label: Session context rebuilding
Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Lifecycle code selects retained branch details, then session start alone hydrates missing local keys from default kind nuggets. Before each agent start it pushes formatted local facts into system context. Code owns selection and delivery; Pi owns event execution, session storage and the eventual model window. This is neither a semantic relevance search nor a model summarizer. SRC-1: `.pi/extensions/nuggets.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lifecycle hooks replace the local map; before-agent hook returns an appended systemPrompt.
- Later read-back: Current-branch nuggets tool details and saved default shelf values reach a later invocation through the local map; switch/fork/tree do not run shelf hydration.
- Delegated visibility: Model sees preference/learning/fact text and at most ten active-file values, not full fact provenance or shelf counters; operator overlay is a separate human display.
- Selection predicate: Replay only nuggets toolResult details.facts; truthy values set entries, falsy values delete. Start hydration fills missing exact keys. Formatting groups key prefixes, excludes underscore-prefixed other keys and keeps the final ten file entries by Map iteration order.
- Invalidation or expiry: Replay resets map then cumulatively merges snapshots. Missing keys in a later snapshot are not deletions. Disk deletion alone does not invalidate old branch details. No global prompt token/character budget for preferences, learnings or ordinary facts.
- Activation or effect: Automatic unsolicited prompt supply is wired through the existing [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt); semantic compliance unobserved.
- Evidence limits: Host window truncation and session durability external; Map insertion order is not a reliable last-access timestamp, especially on overwrite.

A branch snapshot is accumulated rather than treated as an authoritative complete replacement. Thus even with a corrected disk forget, an earlier snapshot can recreate a deleted key when a subsequent snapshot merely omits it. On start, stale branch values also take precedence over newer shelf values because hydration only fills absent keys.

> if (details?.facts) {
> 				for (const [k, v] of Object.entries(details.facts)) {
> 					if (v) {
> 						facts.set(k, v);
> 					} else {
> 						facts.delete(k);
> 					}
> 				}
> 			}
> --- `.pi/extensions/nuggets.ts`

#### MEM-RTE-recall-selection
Label: Requested recall selection
Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

The model requests recall/query or list; the library supplies numerical retrieval and enumerative alternatives. Selector code operates on retained keys and values, not source truth. Underlying library methods are capabilities until a concrete caller is identified; the extension is that included later consumer route. SRC-1: `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`, `.pi/extensions/nuggets.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall gives decoded answer and formatted confidence/source; fallback gives matching local key/value lines or no-facts text. List returns all local facts unless a named nugget targets direct shelf enumeration.
- Later read-back: Model-invoked tool reads retained disk facts freshly; if no shelf answer, case-insensitive substring matching of local keys or values supplies potentially different retained copies.
- Delegated visibility: Extension return omits library margin and matched key from successful HRR text, while details snapshot the local map; UI collapsed recall text can show only its first 80 characters.
- Selection predicate: Key exact match, first substring match, best token overlap at least 0.5, then greedy sequence similarity at least 0.55. Decode resolves against unique stored values. Default recall compares user/project/agent stores and keeps highest confidence, ties retaining earlier kind; explicit name targets that nugget. Library broadcast instead covers all loaded nuggets.
- Invalidation or expiry: Dirty-state rebuild on mutation, deterministic rebuild on load, library deletion/eviction; extension local fallback can remain stale. Corrupt files are skipped by shelf loadAll rather than repaired.
- Activation or effect: Requested result text reaches the external model through tool return; counters update only with nonempty library session ID. Actual answer use or benefit unobserved.
- Evidence limits: Confidence/margin are arithmetic selection scores, not empirical calibration or correctness guarantees; tests are source assertions, not observed outcomes.

There is no semantic embedding model here: string rules resolve the tag and dense HRR arithmetic decodes a value. The method named recallInOrder still compares all matched stores by confidence; order provides tie precedence, not unconditional user-first selection. The final answer can be any value in the current vocabulary if decoding errs; it is not a direct key/value read. In contrast, hydration/list use exact stored strings.

> if (!best.found || result.confidence > best.confidence) {
>         best = { ...result, nugget_name: name };
>       }
> --- `src/nuggets/shelf.ts`

> return { word: this._vocabWords[bestIdx], sims: simsSum, probs };
> --- `src/nuggets/memory.ts`

#### MEM-RTE-compaction-extract
Label: Precompaction trace extraction
Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

The host supplies messagesToSummarize; deterministic extension code extracts user text and tool-call paths before host compaction. No model summarizer or per-content human gate is implemented in this extraction. The host's removal policy, summary and alternative checkpoints are external. Operating mode is routine context maintenance, with no answer oracle. SRC-1: `.pi/extensions/nuggets.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hook returns without replacing host compaction; it assigns `_task` locally and to project disk, and copies matching recent tool paths locally only.
- Later read-back: Task is explicitly recallable/listable but excluded from ordinary injection. Locally retained paths can enter subsequent Active Files injection; their durability requires prior result-hook persistence or later host-retained nuggets details.
- Delegated visibility: Later model receives selected paths or requested short task text, not all discarded messages or tool outcomes through this route.
- Selection predicate: Last three nonempty selected user text messages, joined and truncated to 200 characters; last twenty assistant tool_use blocks considered for read/edit/write paths. The code slices tool calls before matching path/tool names, not the last twenty matching paths.
- Invalidation or expiry: Subsequent task extraction overwrites `_task`; file keys overwrite by basename. Host window eviction does not itself delete extracted facts; underlying forget limits remain.
- Activation or effect: Raw conversational/tool traces yield derived facts, with a later prompt/recall channel; no improved task continuity demonstrated.
- Evidence limits: Cannot establish host summary content, verbatim tail, exact reload across host compaction or complete recovery of discarded reasoning.

The raw-to-derived chain retains selected user text/path strings, not criticism, reasons for a tool choice or outcome validation. Known retained extraction does not resolve opaque host summary alternatives. This is context trimming support, not an isolated subagent frame with a bounded return. Gateway process eviction is likewise RAM eviction with requested host continuation, not an extension-controlled summary or stack-frame return.

> for (const tc of toolCalls.slice(-20)) {
> 			const fp = tc.input?.file_path || tc.input?.path;
> --- `.pi/extensions/nuggets.ts`

#### MEM-RTE-legacy-migration
Label: Legacy memory migration

Distinct from ongoing [RT-RTE-memory-context](runtime.md#rt-rte-memory-context): this is the operator-launched manifest migration script, not a Pi callback or model action. Trigger is `migrate:memory`; code proposes and admits deterministic kind classification and case-insensitive key merges. Human launch is not per-fact approval. Existing and legacy JSON are trusted structurally; no answer oracle or semantic review. SRC-1: `src/migrate-memory.ts`, `src/nuggets/kinds.ts`, `package.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Driver writes backup and kind files, archives legacy JSON, then logs counts/paths; missing legacy file exits without migration.
- Later read-back: Default kind files feed extension hydration/recall/promotion; archived and backup JSON do not match shelf's .nugget.json suffix and are not ordinary loadAll inputs.
- Delegated visibility: Later consumers see migrated values and counters, not the merge rationale; operator receives summary counts.
- Selection predicate: All legacy facts classified by key/value heuristics; collisions in each kind take incoming key/value, maximum hits and incoming nonempty or previous session marker.
- Invalidation or expiry: Legacy file renamed after all target writes; backup supports manual recovery. No transactional multi-file rollback or automated restore is implemented.
- Activation or effect: Persistent organization and content can change when operator runs script; no migration was executed here.
- Evidence limits: Initial facts, operator intent and successful completion unavailable; malformed JSON can throw, and partial writes are not an all-or-nothing migration.

> const existing = target[idx];
>   target[idx] = {
>     key: incoming.key,
>     value: incoming.value,
>     hits: Math.max(existing.hits ?? 0, incoming.hits ?? 0),
>     last_hit_session: incoming.last_hit_session || existing.last_hit_session || "",
>   };
> --- `src/migrate-memory.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors)

Memory lineage is fact-array order, unique value vocabulary, name-derived random seed and saved dimensions/configuration. No external embedding provenance is unresolved here; these vectors are locally generated, unlike provider weights. Memory source directly read in this member confirms that load rebuilds and save serializes facts/configuration rather than `_E`. Dense representations change with facts, but are not trained provider parameters. SRC-1: `src/nuggets/memory.ts`; seed passage retained in the supplied record.

#### On [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion)

The retained output is [MEM-OBJ-promoted-memory](#mem-obj-promoted-memory), with access metadata separated as [MEM-OBJ-hit-metadata](#mem-obj-hit-metadata). Its selector has no hard output budget and scans all nuggets in the current shelf instance, unlike default kind-only hydration. The callback passes the current cached shelf, without a fresh load at that callback; intervening refresh/write operations determine its freshness. Reasons and hit histories do not reach Markdown. The intended external reader remains afforded rather than included wired consumption. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/promote.ts`.

> promoteFacts(shelf);
> --- `.pi/extensions/nuggets.ts`

The merge never synchronizes absent candidates into deletions. Existing entries are parsed, candidates assign section/key values, and the whole recognized structure is rendered. No candidate or no matching Claude project returns zero. When candidates exist, prior unrecognized prose can be lost; no-candidate return does not perform that rewrite. This narrows any general claim that promotion either always preserves or always rewrites existing text. SRC-1: `src/nuggets/promote.ts`.

> if (candidates.length === 0) return 0;
> --- `src/nuggets/promote.ts`

#### On [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs)

Retained job JSON combines symbolic scheduling/recipient controls and a separately interpreted natural-language prompt. The writer and later schedule matcher consume the former; external Pi consumes the latter as described in [RT-BAP-scheduled-prompt](runtime.md#rt-bap-scheduled-prompt). Model-authored JSONL requests are intermediate proposals, not proof of admitted jobs. The supplied runtime establishes reload, missing-default rejection, deletion and one-shot expiry; no extra memory object declaration is needed. SRC-1: `.pi/extensions/proactive.ts`, `src/gateway/cron.ts`, `src/gateway/router.ts`; supporting passages are in [RT-RTE-schedule-admission](runtime.md#rt-rte-schedule-admission) and [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn).

## Write side

Acquisition has distinct controls. Explicit remember is model-proposed with code admission; default category inference is a deterministic content heuristic. Input and tool-result capture are code-proposed and code-admitted transformations of host events. Precompaction extraction is also code-admitted, without changing Pi's compaction policy. Direct library CRUD is an exposed storage capability whose caller control is not universally known. Migration is operator-triggered but code-selected per fact. Promotion is threshold-admitted at compaction, not human approval or factual evaluation. These distinctions are traced in the route records rather than inferred from who performs disk I/O.

Source trust is permissive: required fields, kind strings, trimming and parsing are structural checks. Loaded fact strings and branch details become later context without a source-authentication or contradiction-resolution stage in these inspected routes. Error recovery includes required-field errors, corrupt-file skipping, overwrite/deletion, migration backup and caught promotion errors. None establishes factual warrant. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/{memory,shelf,promote}.ts`, `src/migrate-memory.ts`.

> if (!key || !value) return;
> --- `src/nuggets/memory.ts`

> } catch {
>         // skip corrupt files
>       }
> --- `src/nuggets/shelf.ts`

Trace-fed updates are concrete but narrow: input text → short preference/learning → JSON/local facts → later prompt; tool-call input path → basename-keyed fact → later file context; selected precompaction text → `_task` → requested recall; recall session marker → hit count → possible Markdown promotion. They retain extracted content or counters, not structured reasons/outcomes. No successful capacity improvement follows from their existence.

Evaluation tests assert CRUD, decoding, JSON reload, session hit counting, max-fact eviction and fuzzy/token matching. They do not participate in production admission. They do not test the extension's snapshot deletion semantics, gateway isolation or end-to-end promotion. Their inspected assertions are not observed test success. SRC-1: `tests/memory.test.ts`.

## Read-back

There are several non-equivalent paths:

1. **Unsolicited turn context:** branch replay plus start-only default hydration feeds the local formatter, then appended system prompt. Selector is prefix/order based, with ten file entries and no global budget. This can deliver preferences as high-priority context but does not establish obedience. [MEM-RTE-context-rebuild](#mem-rte-context-rebuild), [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt).
2. **Requested recall:** model query selects a store/key and numerical decode, or local substring fallback. This is targeted retained-content selection. Default names restrict stores; arbitrary named overrides reach additional stores. [MEM-RTE-recall-selection](#mem-rte-recall-selection).
3. **Enumeration and human display:** default list reads local facts; named list enumerates a disk nugget. `/nuggets` shows local facts in an overlay rather than sending a new automatic model prompt. Library facts/status/save/load alone establish capabilities, not unspecified consumers. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/{memory,shelf}.ts`.
4. **Host session continuation:** gateway selects per-chat hashed session directories and requests `--continue`. Host-retained messages, summaries and tool details are external opaque payloads here; the extension only specifies how it reads current-branch details. The shelf remains OS-user shared. [RT-RTE-message-turn](runtime.md#rt-rte-message-turn).
5. **Deferred requests:** cron reloads retained job prompts and passes them into Pi as later requests; heartbeat merely instructs Pi to check memory. It is not a separate implemented fact selector. Schedule admission and delivery limitations remain beside their supplied records. [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn), [RT-BAP-scheduled-prompt](runtime.md#rt-bap-scheduled-prompt).
6. **Markdown export:** implemented writer, intended external consumer, no included read-back loader. Repeated ordinary extension recall does not raise hits. [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).

Working-context controls are therefore explicit extraction/filtering/reintroduction around an opaque host window. Switching branches reconstructs selected memory; it does not isolate the shared shelf. Process eviction frees process memory while retaining a continuation address, not a frame whose only escape is a bounded result. Nothing inspected lets this report enumerate what Pi preferentially removes or whether it retains a verbatim tail alongside a summary.

## Integration issues

- **Correction to supplied compaction selection wording:** runtime says “last twenty matching tool calls”; implementation slices `toolCalls` to twenty before matching names and paths. Fewer than twenty qualifying file paths can survive that selection. [MEM-RTE-compaction-extract](#mem-rte-compaction-extract) supplies the exact loop passage; scope is the precompaction hook, not normal result capture. SRC-1: `.pi/extensions/nuggets.ts`.
- **Withdrawal consequence beyond the supplied short-circuit finding:** even if shelf deletion executes, branch replay cumulatively merges nonempty snapshots and does not delete omitted keys. Earlier details can restore a deleted local fact; promotion is an independent unretracted copy. This elaborates, not contradicts, [RT-RTE-memory-context](runtime.md#rt-rte-memory-context). See [MEM-RTE-context-rebuild](#mem-rte-context-rebuild), [MEM-RTE-fact-mutation](#mem-rte-fact-mutation), [MEM-OBJ-promoted-memory](#mem-obj-promoted-memory). SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/promote.ts`.
- **Access-count interpretation:** runtime's per-session dedup phrase is only last-marker dedup, not unique-session accounting. Value replacement preserves hits. This limits the advertised cross-session promotion meaning without disputing the runtime's missing extension session-ID finding. [MEM-OBJ-hit-metadata](#mem-obj-hit-metadata), [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion). SRC-1: `src/nuggets/memory.ts`.
- **Identity reconciliation:** the five detailed integration routes use Part of on [RT-RTE-memory-context](runtime.md#rt-rte-memory-context); they are narrower paths, not replacements. New operative objects distinguish fact content, metadata, snapshots, task text and Markdown from existing vector/route records. Migration has no supplied declaration counterpart after comparison. No same-referent duplicate declaration is intended.
- **Open host questions:** Pi session serialization, exact compaction summary/checkpoints, model tool permissions, event activation and Claude loading cannot be settled by this source. Prevented conclusions are durable host replay, complete context recovery and exercised exported-memory authority, not the known extraction/write mechanisms. Relevant records: [MEM-RTE-context-rebuild](#mem-rte-context-rebuild), [MEM-RTE-compaction-extract](#mem-rte-compaction-extract), [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).
- **Open live-state questions:** deployed fact contents, callers supplying hit-session IDs, concurrent writes, installed extension discovery and actual recall quality are unavailable. This prevents operational and benefit conclusions for [MEM-RTE-recall-selection](#mem-rte-recall-selection) and [RT-RTE-memory-context](runtime.md#rt-rte-memory-context), not static wiring findings.

## Limitations and checks

All source-dependent findings use SRC-1 at the boundary commit. Newly detailed paths remain inside its registered repository and functional scope; no new source or target implementation was introduced. Git HEAD and clean worktree status were checked. Governing member types, worker rules and record contract were read completely; runtime's final empty trailing range was recovered. No source executable, tests, providers or services were run. No prior analysis was consulted.

Consequential claims were challenged against alternative paths: direct list/hydration disproves vector-only storage; generic/named shelf access disproves default-kind exhaustive coverage; library forget disproves a blanket claim that deletion is impossible; snapshot replay and Markdown merge disprove global withdrawal; explicit recall prevents treating `_task` as wholly unreachable; no-candidate return qualifies Markdown rewrite risk. Lack of live evidence limits activation and benefit, not implementable memory capacity.

Deterministic validation: required `commonplace-run validate-output` completed successfully: “Member content check passes; invocation residue not checked.” This checks form and quotation occurrence, not claim support or job acceptance.
