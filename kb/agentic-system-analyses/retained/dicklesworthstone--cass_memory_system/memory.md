---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "cass_memory_system memory mechanisms: session-derived playbooks, feedback attribution, withdrawal, provenance read-back and retained safety patterns"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
source-identity: "https://github.com/Dicklesworthstone/cass_memory_system"
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
---

# cass_memory_system memory report

## Boundary and evidence

CM retains session summaries, rule content, feedback and safety patterns for later coding work. This report covers the shipped CLI, HTTP tools/resources, session-end initiation, manual/onboarding/import/starter admissions, feedback, maintenance, exports and generated guard consumers within the [boundary](boundary.md). External cass indexes and agent transcripts supply history; CM does not own their production. Provider weights and enclosing-agent compliance remain outside inspectable source behavior. No target, tests, providers or services were executed.

SRC-1 supplies implementation and doctrine/design, not observed operation. Direct inspection added selected ranges in `src/types.ts`, `src/diary.ts`, `src/playbook.ts`, `src/curate.ts`, `src/commands/playbook.ts`, `src/commands/context.ts`, `src/commands/why.ts`, `src/commands/serve.ts`, `src/commands/project.ts`, `src/outcome.ts`, `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/audit.ts`, `src/commands/validate.ts`, `src/commands/trauma.ts`, `src/trauma.ts`, `src/commands/init.ts`, `src/starters.ts`, `src/commands/starters.ts`, `src/semantic.ts`, `src/tracking.ts`, `src/utils.ts`, `src/reflect.ts` and `src/orchestrator.ts`. Bounded searches covered registered dispatch in `src/cm.ts`, onboard bookkeeping in `src/onboard-state.ts`, and tool registrations. Tests read were selected portions of `test/learning-loop.e2e.test.ts` and `test/context-retrieval-benchmark.test.ts`. Remaining helper branches are available but not exhaustively inspected; they are not access gaps.

| Entry point / memory operation | Source paths (SRC-1) and inspection basis | Covering records or explicit limit |
|---|---|---|
| Task context; semantic fallback; optional delivery logging | Direct: `src/commands/context.ts`, `src/semantic.ts`, `src/utils.ts`; supplied runtime | [RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-OBJ-context-log](#mem-obj-context-log), [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache) |
| Reflection; incremental/retry bookkeeping; inline feedback; auto-outcomes | Direct: `src/orchestrator.ts`, `src/reflect.ts`, `src/diary.ts`, `src/tracking.ts`, `src/outcome.ts`; supplied runtime for hook/provider details | [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [MEM-OBJ-diary-entry](#mem-obj-diary-entry), [MEM-OBJ-processed-log](#mem-obj-processed-log), [MEM-RTE-outcome-feedback](#mem-rte-outcome-feedback) |
| Standalone diary and LLM-free checkpoint alternative | Direct: `src/diary.ts`; scoped source search: `src/commands/diary.ts` | [MEM-OBJ-diary-entry](#mem-obj-diary-entry); fast summary does not establish extracted reusable lessons |
| Onboarding/manual single and batch add | Supplied runtime; direct selected add/import ranges in `src/commands/playbook.ts`; bookkeeping search in `src/onboard-state.ts` | [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add); detailed onboarding gap/sampling implementation not re-read, so no independent completeness assessment |
| Init/starter/custom starter | Direct selected: `src/commands/init.ts`, `src/starters.ts`, `src/commands/starters.ts` | [MEM-RTE-portable-admission](#mem-rte-portable-admission); overwrite/backups outside selected init ranges rely on supplied boundary inventory, not an audited reset guarantee |
| Import/export and project instruction files | Direct: `src/commands/playbook.ts`, `src/playbook.ts`, `src/commands/project.ts` | [MEM-RTE-portable-admission](#mem-rte-portable-admission), [MEM-RTE-provenance-read](#mem-rte-provenance-read) |
| Mark/MCP feedback; outcome record/apply | Supplied runtime for mark; direct: `src/outcome.ts`, `src/commands/serve.ts` | [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update), [MEM-RTE-outcome-feedback](#mem-rte-outcome-feedback) |
| Curation, conflict checks, replacement, merge, inversion, retirement | Direct: `src/curate.ts`, `src/playbook.ts`, selected `src/commands/playbook.ts` | [MEM-RTE-rule-curation](#mem-rte-rule-curation); conflict reporting differs from rejection at admission |
| Forget, remove, undo, scrub | Direct: `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts`, `src/playbook.ts` | [MEM-RTE-rule-withdrawal](#mem-rte-rule-withdrawal), [MEM-OBJ-blocked-entry](#mem-obj-blocked-entry) |
| Why/get/list/top/stale/stats/similar/usage | Direct why and formatting/cache paths; dispatch search; supplied runtime for retained state | [MEM-RTE-provenance-read](#mem-rte-provenance-read); selected consumer families, not full output audit of every diagnostic command |
| HTTP resources and alternate substring search | Direct: `src/commands/serve.ts` | [RT-RTE-http-tools](runtime.md#rt-rte-http-tools), [MEM-RTE-provenance-read](#mem-rte-provenance-read); these bypass context's task ranking/budget |
| Validate, audit, benchmark and learning-loop evaluators | Direct selected: `src/commands/validate.ts`, `src/commands/audit.ts`, named tests; supplied runtime for reflection validator | [MEM-CLM-evaluation-limits](#mem-clm-evaluation-limits); no run results or automatic audit-to-revision route established |
| Trauma scan/init/add/import/heal/remove; guard and CLI warning | Direct: `src/trauma.ts`, `src/commands/init.ts`, `src/commands/trauma.ts`, `src/commands/context.ts`; supplied runtime for generated guards | [MEM-RTE-trauma-admission](#mem-rte-trauma-admission), [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard); import/heal/remove located, not exhaustive schema/Python-regex compatibility audit |
| Config/privacy/doctor/hook installation and product update | Boundary inventory and runtime only | Supporting controls, not evidence of a new learned-content store. Detailed diagnostic repair/config admission uninspected; no deployed permissions, confidentiality or upgrade claim |
| Opaque model/host context and external raw corpus | Supplied boundary/runtime | [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model); cannot infer hidden retained provider state, host compaction or corpus completeness |

## Core ideas

1. **Two derived layers mediate trace influence.** A sanitized exported transcript becomes a persisted diary. The reflector receives diary fields and up to three related snippets, then proposes rule deltas. Curated YAML rules reach later context requests and reflector calls. The diary is not a verbatim transcript, and a rule is not its evidential dossier ([MEM-OBJ-diary-entry](#mem-obj-diary-entry), [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)).
2. **Content and standing change independently.** Rule words are natural-language guidance. Events, scores and retirement flags have fixed software consumers that can reorder or exclude those words. Counts labelled helpful/harmful need not demonstrate causal utility ([MEM-OBJ-feedback-events](#mem-obj-feedback-events), [MEM-RTE-outcome-feedback](#mem-rte-outcome-feedback)).
3. **Reasons survive selectively.** Reflection additions retain their proposal reason, but context shortens that reason; metadata can substitute when it is missing. The reflector's existing-rule formatter omits it. Replacement and merge do not preserve every proposed reason in the resulting bullet ([MEM-OBJ-reasoning](#mem-obj-reasoning), [MEM-RTE-rule-curation](#mem-rte-rule-curation)). Thus changed guidance can recur without the full criticism episode recurring.
4. **Withdrawal has a second memory channel.** Forgetting persists blocked content as well as retiring its current ID. Merged loads consult blocked logs and suppress exact or high-overlap matches. A later similar copy can be excluded without sharing the original ID ([MEM-OBJ-blocked-entry](#mem-obj-blocked-entry), [MEM-RTE-rule-withdrawal](#mem-rte-rule-withdrawal)).
5. **Advisory retrieval and symbolic safety differ.** Task context is requested guidance with best-effort budgeting. Trauma regexes feed a matcher that can emit host denial; the associated explanation is display text. Neither returned guidance nor a denial signal proves deployed compliance ([RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance), [RT-BAP-guard-denial](runtime.md#rt-bap-guard-denial)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-diary-entry
Label: DiaryEntry derived session summary

Source-native identity: `DiaryEntry`, keyed by a deterministic session/content-derived ID. Natural-language operative content consists of accomplishments, decisions, challenges, preferences and keyLearnings; JSON storage is under configured `diaryDir`, normally the global diary directory. Session path, agent/workspace/status/timestamp and related-session references are symbolic provenance and selection metadata, not the linguistic summary. They remain distinguishable fields of this container. The input is an exported, sanitized historical agent session or supplied sanitized content. Source identity of the originating agent is metadata/path attribution, not independently authenticated origin (SRC-1: `src/diary.ts`).

Distinct from [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update): this is its retained intermediate, not the admission route. It is also distinct from [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet), whose content is derived downstream. The reflector reads formatted summary fields; why/resources provide later cross-invocation diary readers. The formatter does not reload the raw transcript for those summary fields (SRC-1: `src/reflect.ts`, `src/commands/why.ts`, `src/commands/serve.ts`).

> const diaryPath = path.join(expandPath(config.diaryDir), `${diary.id}.json`);
> await atomicWrite(diaryPath, JSON.stringify(diary, null, 2));
> --- `src/diary.ts`

LLM-free generation instead uses a first task/line summary, regex-inferred status and file tags, leaving decisions/challenges/preferences empty. Its keyLearnings field can contain a session description rather than a learned generalization. This still persists and is later readable; the configured no-LLM reflector does not generate rule deltas. No correctness or full-trace preservation conclusion follows (SRC-1: `src/diary.ts`, `src/reflect.ts`).

> keyLearnings: summary ? [summary] : [],
> --- `src/diary.ts`

#### MEM-OBJ-reasoning
Label: Playbook reasoning and withdrawal explanations

Source-native identity: `PlaybookBullet.reasoning` and `deprecationReason`, natural-language fields in YAML. These are distinct from the instruction content identified by [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet), not a duplicate instruction record. Reflection add copies `delta.reason` into reasoning; deprecate stores reason and optional replacement pointer. Import can fill missing reasoning. Context displays reasoning through a 200-character formatter; deprecation reasons support diagnostic display, not active-rule execution (SRC-1: `src/curate.ts`, `src/playbook.ts`, `src/utils.ts`, `src/commands/context.ts`, `src/commands/playbook.ts`).

> if (typeof delta.reason === "string" && delta.reason.trim()) {
>   newBullet.reasoning = delta.reason.trim();
> }
> --- `src/curate.ts`

> const MAX_LENGTH = 200;
> --- `src/utils.ts`

Metadata fallback can yield “From … session on …” instead of a causal reason; source-session arrays and feedback logs do not accompany the context projection. In the inspected existing-playbook prompt formatter, the reflector receives IDs/content/counts/maturity icons, not these stored reasons. Thus a later caller can see a shortened reason while the next proposal round can receive only the guidance and standing. Replacement changes text without refreshing reasoning; merge creates a new bullet with synthetic `merged` provenance and does not transfer the optional merge reason into its reasoning field (SRC-1: `src/reflect.ts`, `src/curate.ts`, `src/utils.ts`; [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet) supplies the formatter passage).

#### MEM-OBJ-feedback-events
Label: FeedbackEvents and rule standing

Source-native identity: `feedbackEvents`, helpful/harmful counts, maturity/state/deprecated/pinned fields surrounding the instruction. Representational form: symbolic labels, IDs, timestamps and numbers in YAML. Lineage includes explicit mark, model feedback deltas, inline transcript comments, outcome-derived grading and imported events. These are distinct control metadata from [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet); [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update) is one writer, not the object.

Their software authority is scoring, promotion/demotion, deduplication and active filtering; context exposes aggregate standing but omits the event log. Event reason/context prose is an explanatory part separately identified below, not the numerical score itself. Initial learned/manual add constructs zero counts and candidate/draft standing; imports and starters can supply other standing without verified session evidence (SRC-1: `src/types.ts`, `src/playbook.ts`, `src/curate.ts`, `src/outcome.ts`, `src/commands/context.ts`, `src/starters.ts`).

> state: "draft",
> maturity: "candidate",
> --- `src/playbook.ts`

#### MEM-OBJ-feedback-context
Label: Feedback event explanatory context
Part of: [MEM-OBJ-feedback-events](#mem-obj-feedback-events)

Source-native identity: each feedback event's optional `context` and human-readable reason display. Form: natural-language explanation, with enumerated harmful reason codes as symbolic companions. Storage: event entries inside YAML. Origins include caller explanation, reflected or inline judgment and outcome scorer's comma-separated signal labels. `why` reads recent event explanations; context does not expose this history. It can support diagnostic interpretation but does not supply an independently verified criticism episode or oracle (SRC-1: `src/types.ts`, `src/curate.ts`, `src/outcome.ts`, `src/commands/why.ts`). No supplied object counterpart: the closest route is [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update).

> context: e.context,
> --- `src/commands/why.ts`

#### MEM-OBJ-context-log
Label: Context delivery and outcome records

Source-native identities: `ContextLogEntry` in `context-log.jsonl` and `OutcomeRecord` in `outcomes.jsonl`. These are related symbolic records linked by session identity, not a raw conversation or a content store of rules. Context logs retain sanitized task text plus shown rule/anti-pattern IDs, workspace/session and time when explicitly enabled. Outcomes retain asserted/classified status, rulesUsed and optional performance/sentiment signals, notes/task and recordedAt. Human-readable task/notes are descriptive inputs, not themselves scored rule instructions. Default scope resolution prefers current repo state where applicable, otherwise global (SRC-1: `src/commands/context.ts`, `src/outcome.ts`).

Distinct from [RT-RTE-context-read](runtime.md#rt-rte-context-read) and [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update): these are persisted attribution inputs for another updater. Outcome feedback consumes the most recent matching session log if rulesUsed is missing. This is evidence of delivery, not adherence; code marks backfilled outcomes autoGraded to restrict blanket harm. It backfills ruleIds, not antiPatternIds. Outcomes/resources and feedback application are actual later consumers (SRC-1: `src/outcome.ts`, `src/commands/serve.ts`).

> return { ...outcome, rulesUsed: match.ruleIds, autoGraded: true };
> --- `src/outcome.ts`

#### MEM-OBJ-processed-log
Label: ProcessedLog and onboarding recovery metadata

Source-native identity: `ProcessedLog` entries and separate onboarding processedSessions state. Symbolic storage: reflection processed logs under the global reflection directory, and onboarding JSON state. These record session identities, diary references/progress and, for reflection, record/hash growth watermarks, observed message/time/size signals and failed-attempt retry metadata. They do not retain the transcript or formulate a rule. Distinct from [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update) and [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add): these are their cross-run scheduling inputs (SRC-1: `src/tracking.ts`, `src/onboard-state.ts`, `src/diary.ts`).

Reflection discovery uses them to skip unchanged sessions, reopen growth or retry failures. Diary lookup can use processed diaryId before a bounded scan. Missing old watermarks suppress incremental discovery rather than proving that old content was reconsidered. Onboarding progress is a separate ledger and should not be treated as the same reflection checkpoint (SRC-1: `src/tracking.ts`, `src/diary.ts`, `src/onboard-state.ts`).

> if (entry.recordCount === undefined) return "skip";
> return sessionHasGrown(entry, observed) ? "grown" : "skip";
> --- `src/tracking.ts`

#### MEM-OBJ-embedding-cache
Label: EmbeddingCache bullet vectors

Source-native identity: `EmbeddingCache` / `embeddings/bullets.json`. Storage: JSON keyed by bullet ID with contentHash, vector and computedAt, plus model/version metadata. Vectors are distributed numerical representations; IDs/hashes/version are symbolic access and invalidation metadata. They are outputs of [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), not its weights and not a duplicate model component. Direct cache inspection confirms later reuse for context similarity and semantic duplicate checks (SRC-1: `src/semantic.ts`, `src/commands/context.ts`).

> if (cache.model !== model || cache.version !== EMBEDDING_CACHE_VERSION) {
>   return createEmptyEmbeddingCache(model);
> }
> --- `src/semantic.ts`

Software computes/adopts cache entries under locking; no human content approval or model-training operation is involved in this path. Model name/version and content hashes constrain reuse, but do not authenticate immutable embedding-provider weights. A changed provider behind the same name remains an unresolved provenance limit inherited from the component. Numerical similarity can change rank or dedup selection without changing the rule's linguistic content. Backend failure can fall back to keyword scoring (SRC-1: `src/semantic.ts`, `src/commands/context.ts`).

#### MEM-OBJ-blocked-entry
Label: BlockedEntry withdrawal memory

Source-native identity: `BlockedEntry` containing ID/content/reason/forgottenAt in global or repository blocked logs, with legacy toxic-log paths also consumed. Symbolic content hash/token comparisons give stored text matching authority; natural-language reason is an explanatory payload. Distinct from the rule instruction in [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet): its operative consumer is the merged-load filter, not the agent interpreting an active rule. It persists withdrawn content so exact/high-Jaccard copies can be retired in the merged view even under another ID (SRC-1: `src/playbook.ts`, `src/commands/forget.ts`).

> if (isBlocked) {
>   // Keep state fields consistent with other deprecations
>   deprecateBullet(merged, b.id, "BLOCKED_CONTENT");
> }
> --- `src/playbook.ts`

A variable comment calls Jaccard matching “Semantic Match”; the inspected consumer is token overlap, not embedding or semantic truth assessment. Undo removes selected ID entries from current blocked logs; historical/toxic paths remain additional reload inputs. Scope and copying matter: an ID restored in one file need not prove every independent blocked entry was removed (SRC-1: `src/playbook.ts`, `src/commands/undo.ts`).

#### MEM-OBJ-trauma-entry
Label: TraumaEntry matching state

Source-native identity: `TraumaEntry.id`, regex pattern, scope/project/status and trigger-event reference. Symbolic encoding stored in global/project `traumas.jsonl`; the matcher reloads active entries. Entries arise from manual add/import or an initialization scan followed by bulk approval. Severity and labels do not establish historical catastrophe. Distinct from [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard): this object is its persisted input. Its natural-language explanation is separately recorded below (SRC-1: `src/types.ts`, `src/trauma.ts`, `src/commands/trauma.ts`, `src/commands/init.ts`).

> status: "active",
> trigger_event: {
>   session_path: "manual-entry",
>   timestamp: now(),
>   human_message: message,
> },
> --- `src/commands/trauma.ts`

Regex admission compiles the manually supplied pattern in JavaScript. Guard matching is generated Python, so this check is not a demonstrated cross-engine equivalence guarantee. Heal removes active matching authority through status; remove deletes entries. Host installation/enforcement remains unobserved (SRC-1: `src/commands/trauma.ts`, `src/trauma.ts`; [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard)).

#### MEM-OBJ-human-message
Label: Trauma human_message explanation
Part of: [MEM-OBJ-trauma-entry](#mem-obj-trauma-entry)

Source-native identity: `trigger_event.human_message`. Natural-language form in the same JSONL entry; independent of the symbolic pattern's matching meaning. Origins include caller `--message`, default manual text or generated scan description, so the field name is not proof of a human-authored incident account. The CLI task warning and guard denial display it alongside source reference. It explains the signal to the recipient; regex matching does not semantically evaluate it (SRC-1: `src/commands/trauma.ts`, `src/commands/init.ts`, `src/commands/context.ts`; [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard) supplies guard channel evidence).

> human_message: `Auto-detected from history: ${c.description}`,
> --- `src/commands/init.ts`

### Routes

#### MEM-RTE-outcome-feedback
Label: Outcome-derived feedback admission

Endpoints: explicit/auto-recorded outcome plus optional context-delivery log → symbolic scorer → located rule event/maturity → saved playbook → later scoring/context. Owner: `applyOutcomeFeedback`; software decides credit/harm/abstention, caller or transcript classifier supplies signals. This is distinct from [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update), which admits an explicit judgment directly, and overlaps [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update) at post-reflection outcome production (SRC-1: `src/outcome.ts`, `src/orchestrator.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: applied count and missing IDs; record and application are distinguishable effects.
- Later read-back: event/count/maturity changes are reloaded by scoring, curation and context; outcomes can be replayed with timestamp/session/type deduplication.
- Delegated visibility: context/resources expose projected state or outcomes; they do not expose proof of rule compliance.
- Selection predicate: explicit rulesUsed or most recent matching session's shown ruleIds, then score policy and existing target IDs; repo target preferred.
- Invalidation or expiry: duplicate event suppression, later feedback/undo/scrub and time decay change standing; reading the last bounded log slice can omit older attribution inputs.
- Activation or effect: admitted events change stored standing; resulting external-agent behavior and useful learning are uninspected.
- Evidence limits: a rule ID appearing in text or a delivery log is not a verified causal contributor; signals are heuristic or caller asserted.

Trace origin: historical agent session text stripped of CM subprocess payloads supplies inline judgments and outcome signals; explicit outcomes may instead be caller reports. Inline feedback IDs are excluded from auto-outcome grading to avoid a second signal. The automatic writer's durable result is feedback metadata, not just a retained raw log. Broad autoGraded sets cannot receive blanket harm; weak ambiguous negatives can abstain (SRC-1: `src/orchestrator.ts`, `src/outcome.ts`).

> if (inlineFeedback.length > 0) {
>   allDeltas.push(...inlineFeedbackToDeltas(inlineFeedback, sessionPath));
>   inlineFeedbackDeltaCount += inlineFeedback.length;
> }
> --- `src/orchestrator.ts`

> if (!enriched.rulesUsed || enriched.rulesUsed.length === 0) continue;
> --- `src/outcome.ts`

Admission is computational with no per-event human approval. Proposed change is reliance metadata, not automatically rewritten text. Missing rules and neutral scores veto updates; locking/fresh load/deduplication support replay recovery, not semantic undo of a falsely attributed event. Direct undo/scrub provide later correction. Operating mode is open maintenance; no independent expected-answer oracle is supplied. Condition 3 content-directed criticism cannot be inferred from aggregate outcome labels; the theory conclusions of the reflection baseline are not strengthened by this path.

#### MEM-RTE-rule-curation
Label: Rule delta curation and inversion

Endpoints: normalized/validated deltas plus fresh target/context playbooks → deterministic dedup/conflict/feedback/text-change logic → saved changed content and standing → later context/reflector. Owner: curator code; model/caller proposes deltas, policy decides. This is a material admission stage of [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), not a replacement for its end-to-end route (SRC-1: `src/curate.ts`, `src/orchestrator.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: applied/skipped/pruned counts, promotions, inversions and decision entries to the caller/orchestrator.
- Later read-back: saved words, reasoning, counts and withdrawal fields reach later loaders; decision-entry existence does not by itself establish a later consumer of the whole decision log.
- Delegated visibility: context projects changed active rules; reflector sees IDs/content/counts, not full reasons or decision history.
- Selection predicate: target routing, exact/hash/Jaccard and optional semantic duplicates, existing IDs, feedback idempotency, decay thresholds and pin/negative exclusions. Detected directive conflicts produce warnings, not candidate vetoes; directive disagreement excludes matches from lexical and embedding duplicate selection.
- Invalidation or expiry: replace mutates text; merge creates a successor and retires sources; deprecate/inversion remove originals from active selection; subsequent updates can alter standing.
- Activation or effect: changes persistent guidance and its selection metadata; no inspected execution evidence of downstream compliance.
- Evidence limits: fixed lexical/directive/score checks and model proposals do not guarantee semantic equivalence, truth or utility.

Add can copy a proposal reason; replace preserves old reasoning while changing content. Merge requires all requested bullets to exist and at least two; its new bullet starts with synthetic provenance. Feedback-threshold inversion creates `AVOID` content and retires the positive original. Already-negative rules are deprecated instead of inverted, and pinned/anti-pattern exclusions qualify any claim that all harmful rules become prohibitions (SRC-1: `src/curate.ts`).

> bullet.content = delta.newContent;
> bullet.updatedAt = now();
> --- `src/curate.ts`

> if (bullet.deprecated || bullet.pinned || bullet.kind === "anti_pattern") continue;
> --- `src/curate.ts`

This is software admission, not evidence of human approval. Missing required add fields, missing targets and duplicate branches can reject/skip proposals. Detected directive conflicts only append warnings and decision entries; their logged action `skipped` does not describe rejection of the candidate. The conflict loop has no rejection exit and proceeds to duplicate checks, then potentially `addBullet`. The inspected add progression confirms the warning-only account in [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), which retains the enforcement passages (SRC-1: `src/curate.ts`). Configured validation gates are upstream and do not cover every change kind. File saving/retry and later explicit maintenance are recovery paths, not preservation of a full semantic revision history. Guidance is the shipped reflector prompt plus current diary/rules; optional semantic comparison is a selector, not an answer oracle. Operating mode: open rule maintenance. Whole-bullet addressability and persistence are implemented; conditions 1–4 remain as separately assessed in [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update). In particular, retained reasons and software inversion do not establish a model criticism trace identifying claim/result/blame or that a kept criticism shaped the next round. Learning benefit remains uninspected.

#### MEM-RTE-portable-admission
Label: Import and starter rule admission

Endpoints: caller-selected YAML/JSON portable bullets or builtin/custom starter → parse/normalize → selected playbook merge/save → later loader. Owner: CLI/import/init software; external author supplies content and often standing. Distinct admission branches from [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add): these can preserve imported metadata or seed preset established rules, rather than starting from ordinary manual-add zero counts (SRC-1: `src/commands/playbook.ts`, `src/starters.ts`, `src/commands/init.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: import validation errors and added/merged/updated/skipped/conflict counts; init/starter selection returns initialization results.
- Later read-back: saved imported/seeded rules and standing enter later context/reflection; matching duplicates union feedback/provenance.
- Delegated visibility: portable export strips sourceSessions/sourceAgents; later context omits full event history even when imported.
- Selection predicate: requested file/starter/target, schema-valid imported bullet subset, same ID and content/overlap match, optional replace flag; starter duplicate IDs/content normally preserve existing rules.
- Invalidation or expiry: ID replacement can replace a whole imported object; retirement and later feedback/maintenance govern future reads.
- Activation or effect: content/standing becomes persistent without the reflection historical evidence gate; external interpretation remains uninspected.
- Evidence limits: external/custom authorship and factual provenance are unresolved; imported count/history assertions are not independently authenticated observations.

> delete exported.sourceSessions; // Not portable between systems
> delete exported.sourceAgents; // Not portable/privacy sensitive
> --- `src/commands/playbook.ts`

> if (flags.replace) {
>   const idx = existingPlaybook.bullets.indexOf(sameId);
>   existingPlaybook.bullets[idx] = bullet;
>   updated++;
> }
> --- `src/commands/playbook.ts`

Software schema validation admits valid subsets even when other bullets fail. Same-ID different content is skipped unless replace; same-content copies merge events and retain existing ID/text. Newly added contradictions are reported after merging, not vetoed by that report. Starter content is shipped or loaded from custom files; source/maturity tags are assigned, not earned by this initialization (SRC-1: `src/commands/playbook.ts`, `src/playbook.ts`, `src/starters.ts`).

Starting import/init is caller control of the batch, not demonstrated per-rule human review. Admission can reject parse/schema failures and skip collisions; overwrite/replace is explicit caller control. Recovery uses file persistence and later correction; detailed initializer backup policy was not audited here. Operating mode: open initialization/import, no expected-answer oracle. Potential theory content and actual external criticism are uninspected; whole-unit editability does not establish all four theory-builder conditions for the authoring system. Persistence into later sessions is wired.

#### MEM-RTE-rule-withdrawal
Label: Rule withdrawal and support scrubbing

Endpoints: caller rule ID/reason or session-pattern selection → forget/remove/undo/scrub → playbook and optionally blocked-log changes → later merged-load filtering/scoring. Owner: command and loader code. Distinct from [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update): this route explicitly removes content or support, can persist rejection memory, and can restore it (SRC-1: `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts`, `src/playbook.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed/deleted/restored IDs or scrub before/after counts, backup paths and errors; dry-run reports without saving.
- Later read-back: current active filtering, score recalculation and blocked-content matching affect later loads; residual stored reasons remain diagnostic evidence.
- Delegated visibility: context omits retired originals and can offer an inverted anti-pattern; full stored retired objects remain available through explicit diagnostic/resource/export paths.
- Selection predicate: exact or command-resolved rule ID; scrub session substrings/globs or tagged CM subprocess paths; optional orphan deprecation excludes pinned/already-deprecated bullets.
- Invalidation or expiry: hard removal deletes the bullet; soft retirement preserves it; undo restores selected state/removes selected blocked IDs; scrub removes matching events/source references without rewriting rule text.
- Activation or effect: removes or changes later guidance eligibility; not a guarantee that previously exported host instruction files were erased.
- Evidence limits: separate file effects are not a multi-file transaction; provenance withdrawal does not prove reconstructed meaning is corrected or that every copy was withdrawn.

Forget requires a reason, logs blocked content, optionally creates `AVOID` guidance and retires the original. Remove supports hard deletion or deprecation. Undo supports last-event removal or undeprecation. Scrub recalculates standing from retained events without promoting it, optionally deprecates orphaned bullets, and backs up changed files before saving (SRC-1: `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts`, `src/playbook.ts`).

> bullet.maturity =
>   MATURITY_RANK[recomputed] < MATURITY_RANK[before.maturity] ? recomputed : before.maturity;
> --- `src/playbook.ts`

Admission control is explicit caller selection with deterministic guards, not generic proof of human approval. A reason is not an expected-answer oracle. Operating mode: open maintenance/recovery. Rejection can be reversed explicitly, but prior false feedback is not automatically semantically diagnosed. This path changes reliance without requiring a rewritten theory; content-directed human/computational criticism remains uninspected absent its episode. It is not evidence of successful self-improvement.

#### MEM-RTE-provenance-read
Label: Provenance and alternate retained-state reads

Endpoints: caller ID/query/resource/export request → selected retained bullets/diaries/events or formatted instruction snapshot → CLI/HTTP/file → external recipient. Owner: deterministic requested reader; recipient owns subsequent interpretation. Distinct from [RT-RTE-context-read](runtime.md#rt-rte-context-read), and an expansion of the alternate readers afforded by [RT-RTE-http-tools](runtime.md#rt-rte-http-tools), not a second declaration of those routes (SRC-1: `src/commands/why.ts`, `src/commands/serve.ts`, `src/commands/project.ts`, `src/playbook.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: why evidence/feedback snippets, resource data, substring search results or rendered/exported playbook; optional project output path.
- Later read-back: why reloads retained diaries/events across invocations; resources return accumulated playbooks/diaries/outcomes; exported AGENTS/Claude text is an afforded later host input, with no inspected host loader trace.
- Delegated visibility: why limits source sessions to five/ten and events to eight/twenty; diary resource returns up to fifty; memory_search projects ID/content/category/scope/maturity, not reasons/events.
- Selection predicate: requested ID or resource; why source references plus creation-date proximity; memory_search lowercased substring over content/category/scope; project active rules sorted by effective score within categories with optional topN.
- Invalidation or expiry: requested loaders read current state; exported files are snapshots and no automatic propagation of later withdrawal is established.
- Activation or effect: display and materialized guidance files; host adoption/behavioral dependency are uninspected.
- Evidence limits: proximity-based diary snippets are not proof they caused the rule; resource and project reads bypass task-context relevance/budget guarantees.

> return { uri, mimeType: "application/json", data: playbook };
> --- `src/commands/serve.ts`

> await atomicWrite(outputPath, output);
> --- `src/commands/project.ts`

Why resolves source refs as diary IDs/files/session paths, then additionally takes nearby diaries from the latest fifty. This is a diagnostic reader of reasoning context, not autonomous retrieval into every model invocation. `cm://playbook` can expose the full merged container, including metadata omitted by context. Project can output full JSON/YAML or active scored instruction text; it requires explicit overwrite permission for an existing destination. The documented agent-file purpose affords an external later consumer, but writing a named file alone does not prove a host read it (SRC-1: `src/commands/why.ts`, `src/commands/serve.ts`, `src/commands/project.ts`, `src/playbook.ts`).

#### MEM-RTE-trauma-admission
Label: Trauma acquisition and maintenance

Endpoints: selected historical sessions or caller pattern/file → scan candidates/manual validation → persisted trauma entries → future guard and CLI warning loads. Owner: scanner/admission command; interactive initializer can ask a human to approve the whole candidate set. Distinct from [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard), which consumes the result (SRC-1: `src/trauma.ts`, `src/commands/init.ts`, `src/commands/trauma.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: audit candidates or add/import/heal/remove results; scan alone does not save candidate entries.
- Later read-back: global/project entries feed future guard matches and CLI context warnings; healed status removes active matching and removal withdraws entries.
- Delegated visibility: candidate evidence/context is displayed; saved entry retains regex, incident reference and description, not necessarily the full candidate evidence text.
- Selection predicate: apology-keyword cass search capped at fifty hits, unique sessions, known dangerous-command patterns over exported tool-call records with textual fallback; manual add validates regex/scope/severity.
- Invalidation or expiry: status maintenance/healing or deletion; malformed patterns/storage errors have guard limits described by runtime.
- Activation or effect: persists symbolic future matching authority after admission; actual host denial and safety benefit remain uninspected.
- Evidence limits: textual fallback may match discussion rather than execution; scan is not exhaustive history or a verified causal catastrophe detector.

> const importAll = await promptYesNo(
>   "\nAdd these patterns to your permanent safety blocklist? [Y/n]: ",
> );
> --- `src/commands/init.ts`

The interactive scan has real batch human-decision supply, unlike per-delta reflection software admission. Manual/add/import caller identity remains unresolved; pattern authorship is separate from saveTrauma I/O. Audit emits review candidates and instructions to add; it is not itself a writer of scars. Initializer approval persists the predefined matched pattern and generated description. No independent oracle is supplied; operating mode is open historical scanning/maintenance with heuristic candidate selection. Heal/remove provide explicit recovery, not proof the original risk disappeared. These symbolic safety constraints need no inference about formulated theories or hidden model criticism.

### Claims

#### MEM-CLM-evaluation-limits
Label: Evaluation does not establish deployed learning

SRC-1 `src/commands/validate.ts` returns a proposed-rule verdict/refinement/evidence; selected `src/commands/audit.ts` returns rule violations or trauma candidates. Neither inspected command automatically commits its returned judgment as a rule revision. They are separate evaluative read/return surfaces; reflection's gate is an admission consumer, while standalone validation/audit output requires another explicit step. Closest supplied record: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), whose validation bypasses limit universal warrant claims.

> return printResult(output, options, { command, startedAtMs });
> --- `src/commands/validate.ts:123-123`

The source retrieval benchmark labels expected rule IDs and reconstructs an incumbent ranker for comparison. These labels are an oracle for that bounded ranking test, not an oracle of rule truth. The learning-loop test uses a mock session and `CM_REFLECTOR_STUBS` to test persistence/feedback integration. These are inspectable evaluator designs; no tests were run, and neither their names nor assertions supply observed model extraction or causal improvement evidence (SRC-1: `test/context-retrieval-benchmark.test.ts`, `test/learning-loop.e2e.test.ts`).

> const reflectA = runCm(["reflect", "--session", sessionAPath, "--json"], testDir, {
>   CM_REFLECTOR_STUBS: JSON.stringify([
> --- `test/learning-loop.e2e.test.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet)

Memory lineage: learned rules originate through diary/model/curation, manual/onboarding content through an external caller, starter words through shipped/custom presets, imported words through portable files, and merged/inverted words through software transformations. The YAML substrate does not determine whether those words have good reasons. Source-session pointers are software-supplied provenance and may be synthetic or stripped during portable export; actual authorship remains local to each write route (SRC-1: `src/curate.ts`, `src/playbook.ts`, `src/starters.ts`, `src/commands/playbook.ts`; [MEM-RTE-portable-admission](#mem-rte-portable-admission), [MEM-RTE-rule-curation](#mem-rte-rule-curation)).

#### On [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

Memory chain: historical exported agent transcript → sanitized/possibly incremental content → JSON diary → proposed/validated deltas → YAML content and standing → next reflector or requested context. Derived reasons persist selectively as [MEM-OBJ-reasoning](#mem-obj-reasoning). Grading additionally uses payload-stripped text, inline comments and referenced IDs to update standing. Processed watermarks govern what is read next; they are not a substitute summary of removed turns. Retained diary/whole original external session can remain reachable while only the new slice is processed. CM does not establish host conversation trimming or a verbatim-tail checkpoint (SRC-1: `src/orchestrator.ts`, `src/diary.ts`, `src/reflect.ts`, `src/tracking.ts`).

#### On [RT-RTE-context-read](runtime.md#rt-rte-context-read)

Selection is request-directed, not unsolicited push. Code combines task keywords/optional dense similarity with bounded feedback influence, active/workspace filtering and approximate projected-bullet budgeting. Omitted rules remain in YAML for later requests; external history and searchPointer suggestions permit further requested investigation. The full history/warnings/task and host window are outside this bullet budget. The first relevant bullet may exceed it. Context does not include feedback events/source-session arrays/embedding, and explicit reasoning can be shortened or replaced with a metadata fallback (SRC-1: `src/commands/context.ts`, `src/utils.ts`; [MEM-OBJ-reasoning](#mem-obj-reasoning)).

> finalScore: relevanceScore * getFeedbackMultiplier(b, config),
> --- `src/commands/context.ts:559-559`

The CLI wrapper separately matches active trauma patterns against task text and adds a nonblocking warning. The HTTP tool calls the shared generator, not that wrapper; the inspected generator does not perform this trauma-warning branch. Therefore CLI/MCP sharing of rule selection does not establish identical safety-warning payloads (SRC-1: `src/commands/context.ts`, `src/commands/serve.ts`). This supplements, rather than contradicts, the baseline's shared-selection finding.

#### On [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard)

Retained matcher input is [MEM-OBJ-trauma-entry](#mem-obj-trauma-entry); [MEM-OBJ-human-message](#mem-obj-human-message) supplies recipient explanation, not the regex decision. Healing/deletion withdraw active matching on reload. The retained future authority is symbolic and conditionally host-enforced, unlike rule context's advisory natural-language delivery. Initialization scan plus batch approval and manual/import surfaces must remain separate from consumption (SRC-1: `src/trauma.ts`, `src/commands/trauma.ts`, `src/commands/init.ts`; [MEM-RTE-trauma-admission](#mem-rte-trauma-admission)).

## Write side

CM has several admission owners, not one universal knowledge gate. Reflection is computational proposal/validation/curation with no wired per-content human approval; explicit invocation supplies the problem, not necessarily content assent. Manual/onboarding additions delegate semantic authorship to a generic caller and optionally check it. Imports preserve or merge asserted standing; starters assign preset standing. Initialization's trauma scan explicitly asks for batch human approval. All these can coexist, so neither “all knowledge is autonomous” nor “all memory is human-approved” fits the source ([RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add), [MEM-RTE-portable-admission](#mem-rte-portable-admission), [MEM-RTE-trauma-admission](#mem-rte-trauma-admission)).

Trace-fed updates include two behavior-shaping results: session-derived rule text and graded rule standing. Raw transcript retention alone would not establish either. Transcript text contains user/assistant/tool material with path/provider metadata; CM strips its own subprocess payloads for grading to prevent self-credit. These safeguards qualify origin and admission but do not authenticate every source or establish truth. Fast diaries and recovery watermarks are alternative retained forms, not evidence of a learned generalization or host compaction ([MEM-OBJ-diary-entry](#mem-obj-diary-entry), [MEM-OBJ-processed-log](#mem-obj-processed-log), [MEM-RTE-outcome-feedback](#mem-rte-outcome-feedback)).

Curation edits words and reliance separately. Add reasons survive; replacement/merge can lose or stale their explanatory lineage. Rejected/skipped proposals can appear in returned decision entries, but no later reader of a durable complete rejection/criticism dossier was established by the inspected orchestrator/curator. This prevents calling the next model round a reconstruction from retained criticism merely because admitted words recur. Whole-unit theories are addressable; actual content, criticism and next-round semantic dependence remain separately limited by the runtime theory account ([MEM-RTE-rule-curation](#mem-rte-rule-curation), [MEM-OBJ-reasoning](#mem-obj-reasoning)).

Withdrawal is not only deletion. Soft retirement keeps content and reasons; blocked logs preserve negative admission history; inversion synthesizes an anti-pattern. Scrub withdraws support and provenance without necessarily rewriting meaning. Undo can restore eligibility, but does not rewind every export, legacy blocklist or separate-file effect. These are operational revisions, not demonstrated successful learning ([MEM-RTE-rule-withdrawal](#mem-rte-rule-withdrawal)).

## Read-back

The principal coding-agent route is a requested context call. CM selects retained content independently of the model that will interpret it, then returns a projection and pointers. MCP uses the same generator for those rule selections. Optional context logging records what was offered, not what was obeyed. Independent unsolicited rule injection was not established; session-end automation is a write trigger, not a push context reader ([RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-OBJ-context-log](#mem-obj-context-log)).

The update consumer is a second model call: diary plus existing-rule formatting and related snippets supply a constrained reflection context. This keeps raw/session detail out of that call while leaving exported history and diaries reachable elsewhere. Provider CLI execution resembles a separate call frame with selected prompt inputs and JSON return; CM's source does not establish the host's popped context, hidden tools or retained provider state. This is context supply control, not evidence that CM trims the enclosing agent's accumulated turns ([RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model), [MEM-OBJ-diary-entry](#mem-obj-diary-entry)).

Explicit why/resource/search/project requests are materially different read-back routes. They have their own selectors and visibility, including larger/full containers and provenance snippets. Project snapshots can become host method text only if an external host adopts/loads them; that later consumer is afforded by the generated agent-file purpose, not observed. Retired rules can remain visible diagnostically even when excluded from task guidance ([MEM-RTE-provenance-read](#mem-rte-provenance-read)).

The guard is automatic retained-state consumption on a host event: active patterns → fixed regex match → deny JSON or Git failure. Its trigger is not a task query and its budget is not context's estimated tokens. Pattern explanation goes to the human/agent recipient, while the matcher consumes symbolic state. CLI task warnings are an additional advisory branch. Installed host enforcement and behavioral effect remain uninspected ([RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard), [MEM-OBJ-trauma-entry](#mem-obj-trauma-entry)).

## Integration issues

- **No supplied-fact correction required.** The baseline is accurate at its stated scope. Supplement its shared context generator with the CLI-only trauma-warning distinction; otherwise identical rule selection must not be generalized into identical complete CLI/MCP payloads (SRC-1: `src/commands/context.ts`, `src/commands/serve.ts`; [RT-RTE-context-read](runtime.md#rt-rte-context-read)).
- **Conflict-reporting correction:** [MEM-RTE-rule-curation](#mem-rte-rule-curation) corrects its prior conflict-specific rejection claim and selection wording. Conflict reporting is warning-only, while required-field, missing-target and duplicate branches can block changes. The inspected conflict loop continues to duplicate checks and new admission; its `skipped` log label is not a candidate veto. This agrees with [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update) and prevents classifying warning collection as preventive conflict curation (SRC-1: `src/curate.ts`).
- **Closest-record relationships:** [MEM-RTE-rule-curation](#mem-rte-rule-curation) is a stage within [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update); [MEM-RTE-outcome-feedback](#mem-rte-outcome-feedback) overlaps it at trace classification and is distinct from direct [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update). Their distinct stages/results need not supersede the baseline. [MEM-RTE-provenance-read](#mem-rte-provenance-read) elaborates alternate consumers inside [RT-RTE-http-tools](runtime.md#rt-rte-http-tools); [MEM-RTE-portable-admission](#mem-rte-portable-admission) separates import/starter branches mentioned alongside [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add). No candidate duplicate referent is proposed. Object records identify stored intermediates or metadata, not the supplied instruction-content/model/route referents.
- **Rationale horizon:** [MEM-OBJ-reasoning](#mem-obj-reasoning) can be stale after replacement and omitted from existing-rule reflection prompts; merge has synthetic lineage. This prevents inferring criticism iteration from repeated rule loading. Corpus-specific theory content, blame placement and demonstrated next-round dependence remain uninspected ([MEM-RTE-rule-curation](#mem-rte-rule-curation), [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update); SRC-1: `src/curate.ts`, `src/reflect.ts`).
- **Opaque inputs and provenance:** originating transcripts, provider weights/endpoints, imported/custom authors and configured corpus are not supplied. Cache model naming and session labels do not authenticate them. This prevents completeness, immutable model identity and truth claims while retaining the known transformations ([MEM-OBJ-embedding-cache](#mem-obj-embedding-cache), [MEM-RTE-portable-admission](#mem-rte-portable-admission), [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model); SRC-1: `src/semantic.ts`, `src/commands/playbook.ts`).
- **Residual copies and enforcement:** withdrawing current rules does not establish that exported host files or independent legacy blocked entries are updated. JavaScript regex acceptance is not a Python-equivalence guarantee. These constrain rollback and deployed safety conclusions ([MEM-RTE-rule-withdrawal](#mem-rte-rule-withdrawal), [MEM-RTE-provenance-read](#mem-rte-provenance-read), [MEM-OBJ-trauma-entry](#mem-obj-trauma-entry); SRC-1: `src/playbook.ts`, `src/commands/undo.ts`, `src/commands/project.ts`, `src/commands/trauma.ts`).
- **Available uninspected depth:** onboarding sampling, all init/reset/doctor recovery branches and every maintenance/import/guard helper were not exhaustively audited. The coverage table names these limits; they prevent exhaustive admission/recovery equivalence guarantees, not completion of this bounded memory account.

## Limitations and checks

Frozen checkout HEAD was rechecked as `8aca3bbb6732321dca041b32c155617784687897`; Git status was clean. Frontmatter source identity and boundary match the supplied inputs. All new source findings remain SRC-1 at that revision. Governing job, three member types, collection, worker rules, records contract, supplied members, refusal and previous output were read in the prescribed batches; bounded runtime reads were continued through EOF. This correction re-read the curator's conflict, duplicate and add progression at the frozen revision. Unrelated findings and existing coverage limits are carried from the supplied previous report, not newly re-audited. No prohibited prior analyses or other run metadata were read, and no target execution occurred.

The strongest conclusions are source wiring, retained forms and actual software consumers. No observed compliance, generated-lesson correctness, safety effectiveness, retrieval performance or causally attributable improved capacity can be reported. Positive trace-to-rule and trace-to-standing pathways coexist with those limits. [MEM-CLM-evaluation-limits](#mem-clm-evaluation-limits) records why source tests are not deployment evidence.

Deterministic validation: the supplied `commonplace-run validate-output` command was run on this invocation; its successful result establishes structural and quotation checks, not semantic acceptance or operational benefit.
