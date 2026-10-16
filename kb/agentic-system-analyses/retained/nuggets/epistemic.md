---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Nuggets epistemic routes: claim acquisition, associative recall, operational reliance and promotion limits in the shipped TypeScript system."
run-id: AAS-2026-10-14-nuggets-c2e87e6916cc-01
reviewed-boundary: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
---

# Nuggets epistemic report

## Source-and-claim boundary

The question is whether the shipped memory and gateway acquire, produce, check and license claims for later reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers: see its [Source register](boundary.md#source-register). All additional source inspection below is SRC-1, implementation unless labelled doctrine/design, at the same frozen commit. No execution or causal evidence was supplied or generated.

The assessment includes explicit memory operations, automatic capture, numerical reconstruction/cleanup, recall selection, withdrawal, migration, promotion, testing and gateway consumption. The absent advertised plugin, external Pi/provider internals, external Claude memory reader, live facts and execution traces prevent conclusions respectively about plugin behavior, model-internal checking, promoted-memory activation, actual candidate provenance and exercised benefit. Provider-generated propositions are possible, but their actual truth-apt content, derivations and checks are not determinable from an uninstantiated endpoint. Excluded publication articles remain outside this assessment. These are not system-complete negatives about every possible host behavior.

Consequential source claims are [EPI-CLM-associative-recall](#epi-clm-associative-recall) and [EPI-CLM-memory-improvement](#epi-clm-memory-improvement). Transport admission has a narrower supplied claim: see [RT-CLM-ingress-control](runtime.md#rt-clm-ingress-control).

| Entry point or operation | Source path | Coverage and records / limit |
|---|---|---|
| Root dispatch; advertised CLI | `package.json` | Direct read: scripts dispatch gateway, setup, migration and Vitest; no CLI bin declared. Boundary supplies tracked-tree evidence that documented Python/CLI implementation is not shipped. No inference from CLI doctrine to an executable evaluator. |
| Library remember, load, clear, forget, recall and shelf removal | `src/nuggets/memory.ts`, `src/nuggets/shelf.ts` | Direct reads of remember/recall/forget, serialization/rebuild/decode/key matching and full shelf; clear supplied by runtime/boundary and test assertions. [EPI-RTE-fact-upsert](#epi-rte-fact-upsert), [EPI-RTE-recall-decode](#epi-rte-recall-decode), [EPI-RTE-recall-score](#epi-rte-recall-score). |
| Numerical cleanup and softmax | `src/nuggets/core.ts` | Direct read of seeds, sharpening, CORVACS-lite, similarity normalization, softmax and bind/unbind; [EPI-RTE-recall-score](#epi-rte-recall-score). Tests of other arithmetic supplied by boundary, not independently assessed. |
| All registered memory tool actions and lifecycle/input/file/compaction hooks | `.pi/extensions/nuggets.ts` | Direct reads of helper wrappers, extraction/rendering, reconstruction, all action dispatch and material hooks. UI rendering and overlay registration supplied by runtime, not a separate truth check. [RT-RTE-memory-context](runtime.md#rt-rte-memory-context), [EPI-RTE-preference-capture](#epi-rte-preference-capture), [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal). |
| Kind classification and migration | `src/nuggets/kinds.ts`, `src/migrate-memory.ts` | Direct full reads; [EPI-RTE-kind-migration](#epi-rte-kind-migration). |
| Compaction promotion | `src/nuggets/promote.ts` | Direct full read and extension caller; [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion). |
| Schedule create/delete/list, prompt supply and confirmation | `.pi/extensions/proactive.ts` | Direct full read; [RT-RTE-schedule-admission](runtime.md#rt-rte-schedule-admission). Gateway admission and removal supplied runtime findings. |
| Message output and heartbeat filtering | `src/gateway/router.ts` | Direct full read; [RT-RTE-message-turn](runtime.md#rt-rte-message-turn), [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn). Other gateway files and mirrored `gateway/src/` covered by supplied runtime, not fresh direct reads. |
| Setup and transport admission | `src/setup.ts`, `src/gateway/config.ts` | Supplied runtime findings: configuration/format/allowlist checks, not claim-truth evaluation. No credential-validity finding. |
| Memory regression tests | `tests/memory.test.ts` | Direct full read, not run; [EPI-RTE-memory-tests](#epi-rte-memory-tests). Core tests covered by supplied boundary only; no fresh assessment of their assertion completeness. |
| Public claims and instructions | `README.md`, `NUGGETS_INSTRUCTIONS.md`, `CLAUDE.md` | README claim passages directly read; remaining instruction claims supplied by boundary/runtime. Doctrine/design, not proof of operation. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-remember-value](#epi-obj-remember-value) | Key/value may assert a scoped fact; arbitrary strings need not do so | see record | SRC-1 `src/nuggets/memory.ts` | No live item or evidence provenance supplied. |
| [EPI-OBJ-preference-value](#epi-obj-preference-value) | A preference attribution may be truth-apt; requested behavior itself is policy | see record | SRC-1 `.pi/extensions/nuggets.ts` | Regex does not establish speaker endorsement or preserve surrounding qualification. |
| [EPI-OBJ-file-path](#epi-obj-file-path) | Path associated with a read/edit/write event; successful edit is not thereby established | see record | SRC-1 `.pi/extensions/nuggets.ts` | Input fields, not checked effects. |
| [EPI-OBJ-task-summary](#epi-obj-task-summary) | Truncated user text, potentially claims or requests; no actual proposition individuated | see record | SRC-1 `.pi/extensions/nuggets.ts` | Not injected through ordinary memory rendering. |
| [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors) | Numerical encoding of the stored values, not an independently warranted proposition | see record | SRC-1 `src/nuggets/memory.ts` | Decoding is associative selection, not factual confirmation. |
| [EPI-OBJ-recall-score](#epi-obj-recall-score) | Numerical score about relative decode similarity, not probability of world truth | see record | SRC-1 `src/nuggets/memory.ts` | No calibration or outcome reference. |
| [EPI-OBJ-promoted-entry](#epi-obj-promoted-entry) | Copies a retained value, with the same unresolved truth scope | see record | SRC-1 `src/nuggets/promote.ts` | Parseable old entries survive; unsupported prose may not. External reader uninspected. |
| [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs) | Symbolic scheduling fields and retained prompt, which may contain claims or requests | see record | SRC-1 `.pi/extensions/proactive.ts` | Scheduling criteria do not warrant prompt content. |
| [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model) | Actual generated truth-apt content not determinable | see record | SRC-1 `src/gateway/pi-rpc.ts` | External distributed-parametric state; no pinned model or run evidence. |

## Authority-route ledger

Fields owned by the linked declaration are given there; the ledger separates consequential functions even when they share an implementation. All implemented routes below are unobserved in this run. “No epistemic license” means the named route supplies no evidence-consuming truth acceptance, not that every imported statement is false.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-fact-upsert](#epi-rte-fact-upsert) | content transformation | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | truth-apt transformation: acquisition/import | Caller value enters store | Trimming/nonempty and case-insensitive key rules; string domain | see record | New value or replacement | Enforcing write rule | Imported warrant unknown; no source check | Permits later use as a fact | see [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt) | SRC-1 `src/nuggets/memory.ts` | none | none | Model authorship/provenance outside store. |
| [EPI-RTE-fact-upsert](#epi-rte-fact-upsert) | retention | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | no content change | In-memory facts to JSON | autoSave or explicit save | see record | Durable strings/configuration | Filesystem replacement | Retention, not acceptance | Makes values reloadable | Library/extension; JSON load; permissive; later invocations | SRC-1 `src/nuggets/memory.ts` | none | none | No evidence links or endorsement added. |
| [EPI-RTE-preference-capture](#epi-rte-preference-capture) | content transformation | implemented | [EPI-OBJ-preference-value](#epi-obj-preference-value) | truth-apt transformation: indeterminate | Input fragment becomes preference/learning | First regex match, truncation and key generation | see record | Selected fragment and generated key | Enforcing extraction | General preservation not established; specific negated context can be lost | Admits text without per-item review | see [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt) | SRC-1 `.pi/extensions/nuggets.ts` | none | Semantic-loss witness | Cannot call every extraction a faithful acquisition or a conjecture. |
| [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) | retention | implemented | [EPI-OBJ-file-path](#epi-obj-file-path) | truth-apt transformation: acquisition/import | Tool path input to fact | Named tool and string path, not success status | see record | Basename-keyed path | Enforcing capture | Warrant degraded if read as successful work | Makes path available as Active Files | see [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt) | SRC-1 `.pi/extensions/nuggets.ts` | none | none | Basename collisions overwrite; no effect oracle. |
| [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) | content transformation | implemented | [EPI-OBJ-task-summary](#epi-obj-task-summary) | truth-apt transformation: indeterminate | Last three selected user texts to 200 characters | Fixed slicing; no semantic evaluator | Before host compaction; see record | `_task` plus selected local file paths | Enforcing retention/selection | No semantic-summary license | Saves selected text; host compaction remains external | Shelf later recall/list; permissive; later invocations; ordinary prompt excludes `_task` | SRC-1 `.pi/extensions/nuggets.ts` | none | none | Omitted qualifications possible; not a model-generated summary. |
| [EPI-RTE-recall-decode](#epi-rte-recall-decode) | content transformation | implemented | [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors) | truth-apt transformation: non-ampliative reshaping | Facts to numeric vocabulary/banks and selected value | Fixed seeded encoding, unbinding, numerical cleanup | see record | Existing vocabulary string or unresolved query | Numerical transformation | No novel factual entailment or truth check | Produces candidate recall result | Library/extension; recall result; permissive; current request | SRC-1 `src/nuggets/memory.ts` | [EPI-CLM-associative-recall](#epi-clm-associative-recall) | none | Selection may associate wrong stored value; source truth unchanged. |
| [EPI-RTE-recall-score](#epi-rte-recall-score) | check/evidence production | implemented | [EPI-OBJ-recall-score](#epi-obj-recall-score) | no content change | Query/key match and value-vector similarity | Exact/substring/token/fuzzy selector; cosine/softmax over finite stored vocabulary | see record | found flag, confidence and margin | Ranking and match gate | Only within matching/decoding domain, not truth calibration | Enables result delivery and cross-store ranking | see record | SRC-1 `src/nuggets/memory.ts` | [EPI-CLM-associative-recall](#epi-clm-associative-recall) | Confidence is not warrant | No accuracy threshold on returned softmax score. |
| [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) | operational admission/selection/consumption | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | no content change | Shelf result or local substring fallback; prompt formatting | Highest confidence across ordered kinds; ties retain earlier result; local fallback only if shelf fails | see record | Answer with confidence/source label or selected facts in system prompt | Ranking/permissive context | No evidence-consuming acceptance | Supplies retained text to model before another source check | see [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt) | SRC-1 `src/nuggets/shelf.ts` | none | Priority is not first-kind-only | Model receives value and coarse kind/name, not original evidence lineage. |
| [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | no content change | Key deletion, not truth acceptance | Model-requested forget; local delete OR shelf delete | see record | Local deletion can skip durable deletion | Enforcing locally, incomplete durable withdrawal | No falsity judgment or acceptance | Can remove current injection while retained copy remains | see record | SRC-1 `.pi/extensions/nuggets.ts` | none | Retraction gap | History reconstruction and promotion can retain older copies. |
| [EPI-RTE-kind-migration](#epi-rte-kind-migration) | lineage/freshness/recovery | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | truth-apt transformation: non-ampliative reshaping | Legacy file to kind stores | Prefix/value heuristic and case-insensitive merge | see record | Buckets; incoming value wins conflict; backup/archive | Enforcing file update | No additional warrant | Changes which default-kind consumer finds an entry | see record | SRC-1 `src/migrate-memory.ts` | none | none | Preserves/max-merges counters, not evidential provenance. |
| [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion) | check/evidence production | implemented | [EPI-OBJ-promoted-entry](#epi-obj-promoted-entry) | no content change | Entry hit count at least three | Deterministic usage threshold, not truth criterion | see record | Candidate qualifies or not | Selection gate | Reuse count only | Permits promotion writer | Writer; hits field; enforcing; compaction event | SRC-1 `src/nuggets/promote.ts` | [EPI-CLM-memory-improvement](#epi-clm-memory-improvement) | Ordinary recall omits session ID | Distinct-session uniqueness is not globally tracked. |
| [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion) | retention | implemented | [EPI-OBJ-promoted-entry](#epi-obj-promoted-entry) | truth-apt transformation: non-ampliative reshaping | Selected entries to Markdown | Existing recognized sections/entries merged with candidates | see record | Rewritten `MEMORY.md` | Conditional file write | Not lifecycle integration after acceptance | Offers text for intended external context | External Claude reader; Markdown; intended advisory force; later sessions unestablished | SRC-1 `src/nuggets/promote.ts` | [EPI-CLM-memory-improvement](#epi-clm-memory-improvement) | Host consumption uninspected | Old promoted values are not removed when source is absent; free-form prose can disappear. |
| [EPI-RTE-memory-tests](#epi-rte-memory-tests) | check/evidence production | implemented | [EPI-OBJ-remember-value](#epi-obj-remember-value) | no content change | Fixture-defined memory behavior | Vitest assertions against explicit expected outputs | see record | Would pass/fail assertions | Test-run failure only | Fixture behavior domain, not world truth | No shipped fact-admission consumer | Developer; test result; advisory to development; no runtime acceptance path | SRC-1 `tests/memory.test.ts` | none | none | Not executed; no causal benefit finding. |
| [RT-RTE-schedule-admission](runtime.md#rt-rte-schedule-admission) | operational admission/selection/consumption | implemented | [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs) | non-truth-apt policy/content update: scheduled future request | Append success versus job admission | Extension shell exit versus gateway fields/default JID | see record | Confirmation before acceptance; possible later rejection | Local operational gate | Does not warrant confirmation of actual scheduled delivery | Can create/delete retained prompts for later Pi turns | see [RT-BAP-scheduled-prompt](runtime.md#rt-bap-scheduled-prompt) | SRC-1 `.pi/extensions/proactive.ts` | none | Confirmation exceeds checked scope | Intended time, recipient and completion not checked by an oracle. |
| [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn) | operational admission/selection/consumption | implemented | [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs) | no content change | Model response admitted to outgoing chat | For heartbeat: nonempty and does not contain NOTHING, case-insensitive | see record | Send or suppression | Enforcing output filter | No relevance/truth acceptance | Allows or suppresses delivery | Router; response text; enforcing; current proactive turn | SRC-1 `src/gateway/router.ts` | none | Substring sentinel | `Nothing failed; deployment succeeded` is suppressed by deduction, not observed execution. |

No lifecycle integration after evidence-consuming truth acceptance was found in the inspected local memory routes: see [EPI-ABS-truth-acceptance](#epi-abs-truth-acceptance). This is distinct from implemented retention, retrieval and operational use.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-associative-recall](#epi-clm-associative-recall) | see record | SRC-1 `README.md`; doctrine/design | see record | [EPI-RTE-recall-decode](#epi-rte-recall-decode), [EPI-RTE-recall-score](#epi-rte-recall-score) | None supplied | No benchmark, intervention or calibrated error data | Algebraic retrieval from finite stored vocabulary is implemented; tests assert selected examples | Speed/accuracy not established. Stored fact truth is outside numerical cleanup's domain. |
| [EPI-CLM-memory-improvement](#epi-clm-memory-improvement) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion), [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) | None supplied | No later behavior, cost/latency baseline or component variation; external reader missing | A conditional hit-selected context writer and independent per-turn memory injection exist | Ordinary extension recall does not accrue hits. Permanent every-session context and faster/cheaper behavior exceed evidence. |

## Bounded conclusion

Nuggets acquires caller strings and user/tool fragments, persists symbolic records and deterministically reconstructs numerical HRR state. Recall selects among stored strings; it is neither a source-truth oracle nor a route to new entailed world claims. The confidence field measures relative decoding scores. Numeric cleanup changes signals, not evidential support. See [EPI-RTE-fact-upsert](#epi-rte-fact-upsert), [EPI-RTE-recall-decode](#epi-rte-recall-decode) and [EPI-RTE-recall-score](#epi-rte-recall-score).

The routes can carry truth-apt facts, preference attributions and file-context claims, but they do not retain claim-specific source evidence. Explicit imports have unknown warrant. Automatic extraction can degrade it: surrounding negation and attribution are not checked, file captures need not reflect successful work, and the task excerpt truncates without a semantic check. Actual model-generated conjectures and provider-internal evaluation remain not determinable; source text permits no attribution of a particular candidate to that opaque processing. See [EPI-RTE-preference-capture](#epi-rte-preference-capture) and the object inventory.

Operational reliance is concrete and separate from epistemic acceptance. Prompt injection supplies selected facts unsolicited on later turns; requested recall delivers selected values with a coarse source label. User preferences can directly shape requested policy without a truth-apt transformation. Neither route enforces compliance or demonstrates improved future action. Key replacement, migration and promotion change retained context without evidence-consuming truth acceptance. Forget is not a reliable cross-copy retraction. See [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt), [EPI-RTE-kind-migration](#epi-rte-kind-migration), [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal) and [EPI-ABS-truth-acceptance](#epi-abs-truth-acceptance).

Three hits are an operational selection criterion for intended permanent context, not a criterion accepting a proposition as true. The writer retains selected values and parseable old entries; the supplied boundary does not include actual Claude read-back. Even hit counting tracks only the last session ID, not the set of sessions; alternating two IDs can repeatedly increment it. Replacing a value does not reset its counter. These counterexamples limit the claim independently of ordinary extension calls' missing session ID. See [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion), [EPI-RTE-fact-upsert](#epi-rte-fact-upsert) and [EPI-CLM-memory-improvement](#epi-clm-memory-improvement).

Scheduling and output filters have consequential but non-epistemic authority. Append success licenses a creation confirmation before gateway admission, and heartbeat substring filtering can suppress meaningful text without judging its truth or relevance. Test source supplies expected-answer oracles for fixtures, but no runtime fact-admission consumer or executed success evidence. See [RT-RTE-schedule-admission](runtime.md#rt-rte-schedule-admission), [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn) and [EPI-RTE-memory-tests](#epi-rte-memory-tests).

For the README's self-improvement claim, the assessment boundary is the shipped context-selection machinery across future sessions; its independently specifiable objective is lower time and cost for useful action. Usage evidence can select a context write, but usefulness is not evaluated; later host reading and behavior causally depending on that write are unestablished. This supports a conditional improvement-directed context pathway, not exercised or successful self-improvement. Learning benefit, content-directed criticism, reflection and autonomous theory-building do not follow from persistence or autonomous writes. Provider cognition remains uninspected rather than absent. These independent limits do not negate the implemented memory and policy-supply routes.

## Shared records

### Operative objects

#### EPI-OBJ-remember-value
Label: Remember value

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

This is the explicit caller-authored value handled inside that integration route (object within a route, not a duplicate route). Natural-language values can carry propositions or instructions; keys are symbolic routing/matching units. Storage is the local `Map`, tool-result snapshots and shelf JSON facts. Content truth depends on the actual key/value and scope; none was supplied. SRC-1 `src/nuggets/memory.ts`, `.pi/extensions/nuggets.ts`; load-bearing admission passage in [EPI-RTE-fact-upsert](#epi-rte-fact-upsert).

#### EPI-OBJ-preference-value
Label: Preference value

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

A distinct automatically extracted natural-language fragment and generated symbolic preference/learning key. It is stored in local facts and user-kind JSON, rendered as Preferences or Learnings, and interpreted by Pi/model. It differs from the explicit value by producer and extraction checks. SRC-1 `.pi/extensions/nuggets.ts`; passages in [EPI-RTE-preference-capture](#epi-rte-preference-capture).

#### EPI-OBJ-file-path
Label: File path

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Symbolic path input captured under basename-derived keys, persisted by tool-result hooks to project memory and held locally; compaction also copies selected calls' paths locally. Paths are fixed string inputs to capture, then natural-language Active Files context to the model. This records association with attempted operations, not checked filesystem effects. SRC-1 `.pi/extensions/nuggets.ts`.

> if (event.toolName === "read") {
> facts.set(`file:${basename}`, filePath);
> shelfRemember(`file:${basename}`, filePath, "project");
> } else if (event.toolName === "edit" || event.toolName === "write") {
> facts.set(`edited:${basename}`, filePath);
> shelfRemember(`edited:${basename}`, filePath, "project");
> }
> --- `.pi/extensions/nuggets.ts`

#### EPI-OBJ-task-summary
Label: Task summary

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Natural-language excerpt stored under symbolic `_task` in local facts and project JSON before host compaction. It is not an inferred summary; it may contain requests rather than claims. Ordinary injection excludes underscore-prefixed entries. Recall or explicit listing can still expose it. SRC-1 `.pi/extensions/nuggets.ts`.

> const taskSummary = userMessages.slice(-3).join(" | ").slice(0, 200);
> facts.set("_task", taskSummary);
> shelfRemember("_task", taskSummary, "project");
> --- `.pi/extensions/nuggets.ts`

#### EPI-OBJ-recall-score
Label: Recall score

A symbolic numeric result (`confidence`, `margin`, `found`) held transiently in return objects and formatted into tool text. It is a distinct part of the memory integration's recall result, not the retained value or [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors). Scope includes direct library callers, so it is not wholly contained in the extension integration. SRC-1 `src/nuggets/memory.ts`; passages in [EPI-RTE-recall-score](#epi-rte-recall-score).

#### EPI-OBJ-promoted-entry
Label: Promoted entry

Part of: [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion)

Natural-language value under a section/key in `MEMORY.md`, with Markdown providing localized organization. This object is the output part of the supplied route, not a second declaration of that route. Intended consumer is external Claude; actual loading is not inspected. SRC-1 `src/nuggets/promote.ts`.

> for (const [key, value] of entries) {
> lines.push(`- **${key}**: ${value}`);
> }
> --- `src/nuggets/promote.ts`

### Routes

#### EPI-RTE-fact-upsert
Label: Fact upsert

The library route accepts caller key/value → trimmed fact list → optional JSON save. It overlaps the explicit-write step of [RT-RTE-memory-context](runtime.md#rt-rte-memory-context), but also admits direct library writes, so it is not the same referent or wholly contained there. Owner is deterministic library code; caller/model proposes content. It checks empty strings, not truth, with no per-content human veto or answer oracle. Mode is ordinary open use; replacement and optional oldest-entry eviction are admission policy. Caller may overwrite/forget; no evidential rollback decision exists. Extension guidance asks for useful discoveries and short values, not evidence-bearing acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `remember` returns void; extension separately reports remembered content.
- Later read-back: Saved JSON reloads values for reconstruction, recall and prompt supply.
- Delegated visibility: Library receives strings, not underlying source evidence; extension/model later receives selected text.
- Selection predicate: Trimmed nonempty fields; case-insensitive key update; optional maximum-facts tail.
- Invalidation or expiry: Value replacement, forget/clear or optional oldest-entry eviction; updates retain prior hit metadata.
- Activation or effect: Facts and optionally disk content change; no observed downstream behavior.
- Evidence limits: No live content, provenance or success traces. Classification is import at the store edge; caller production may be model-generated but is not inspected here.

SRC-1 `src/nuggets/memory.ts`, `.pi/extensions/nuggets.ts`.

> key = key.trim();
> value = value.trim();
> if (!key || !value) return;
> --- `src/nuggets/memory.ts`

> if (f.key.toLowerCase() === key.toLowerCase()) {
> f.value = value;
> found = true;
> break;
> }
> --- `src/nuggets/memory.ts`

> max_facts: this.maxFacts,
> facts: this._facts,
> config: {
> --- `src/nuggets/memory.ts`

#### EPI-RTE-preference-capture
Label: Preference capture

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Input text → first matching preference/learning expression → generated key/truncated value → local and user shelf writes. Owner is extension code, not an explicit model judgment. Non-extension input triggers automatic admission, without per-item human approval, oracle or semantic veto. Mode is ordinary use; source patterns supply all guidance. Overwrite/forget can change retained material, subject to the withdrawal limits below.

Concrete static trace: the input `Do not remember that deployment is safe` matches the unanchored `remember that` pattern. Captured value is `deployment is safe`; short key is `deployment-is-safe`; retained key is `learn:deployment-is-safe`. Rendering places that value under Learnings, without the negated instruction. The input does not entail endorsement of deployment safety. This is an implementation deduction, not a target execution or evidence that such an item exists. General extraction is classified indeterminate: an unqualified actual preference can be faithfully imported, while negation, quotation and truncation can change apparent meaning. Actual input/context is required to decide each edge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Input hook continues the event after automatic local/shelf update.
- Later read-back: User-kind facts hydrate local state and reach future prompt rendering or recall.
- Delegated visibility: Later model receives generated preference/learning key and value, not the original surrounding input.
- Selection predicate: First matching regex; captured value trimmed and limited to 100 characters; key derived from first 30.
- Invalidation or expiry: Same-key overwrite or deletion; no stored link allowing automatic withdrawal when original context changes.
- Activation or effect: Automatic retention and potential prompt supply are wired; actual model reliance is unobserved.
- Evidence limits: Deterministic counterexample refutes universal semantic preservation; it does not establish every extraction is ampliative.

SRC-1 `.pi/extensions/nuggets.ts`.

> { regex: /\bremember that (.+)/i, prefix: "learn" },
> --- `.pi/extensions/nuggets.ts`

> const value = match[1].trim().slice(0, 100);
> const shortKey = value.slice(0, 30).replace(/\s+/g, "-").toLowerCase();
> return { key: `${prefix}:${shortKey}`, value };
> --- `.pi/extensions/nuggets.ts`

> const pref = extractPreference(event.text);
> if (pref) {
> facts.set(pref.key, pref.value);
> shelfRemember(pref.key, pref.value, "user");
> }
> --- `.pi/extensions/nuggets.ts`

#### EPI-RTE-recall-decode
Label: Recall decode

Library facts → unique value vocabulary/seeded vectors → superposed banks → unbinding/cleanup → best vocabulary string. Fixed code owns the route. Distinct from the supplied [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors), which identifies its numerical state, and broader than the extension-only integration in [RT-RTE-memory-context](runtime.md#rt-rte-memory-context). Values update the representation during operation, but there is no provider-weight training here. Algorithm is frozen; exact live vectors depend on unsupplied facts/configuration. No mutable model endpoint is used by this route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected existing vocabulary word, score/margin and matched key, or empty result.
- Later read-back: Facts/configuration are persisted; vectors are reconstructed rather than serialized. Returned answer is not automatically saved as a novel fact.
- Delegated visibility: Caller receives a string/result, not the full vector banks or source evidence.
- Selection predicate: Key resolution followed by maximum softmax score among stored unique values.
- Invalidation or expiry: Dirty state triggers rebuild after mutations; removing all facts clears numerical state.
- Activation or effect: Produces a recall candidate; extension may deliver it as tool text.
- Evidence limits: Selection is non-ampliative at the vocabulary edge but can misassociate a key/value. No truth check, benchmark or observed accuracy follows.

SRC-1 `src/nuggets/memory.ts`, `src/nuggets/core.ts`.

> // Build vocabulary from unique values
> const seen = new Set<string>();
> const vocab: string[] = [];
> for (const f of this._facts) {
> if (!seen.has(f.value)) {
> vocab.push(f.value);
> seen.add(f.value);
> }
> }
> this._vocabWords = vocab;
> --- `src/nuggets/memory.ts`

> return { word: this._vocabWords[bestIdx], sims: simsSum, probs };
> --- `src/nuggets/memory.ts`

#### EPI-RTE-recall-score
Label: Recall score

Query/keys and decoded numerical vector → match decision plus similarity-derived score → shelf ranking and tool display. This is the evaluator part of recall, distinct from [EPI-RTE-recall-decode](#epi-rte-recall-decode)'s string-producing transformation; both overlap [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) but include direct library consumers. Target/domain: query-to-key lexical resemblance and reconstructed signal-to-vocabulary similarity, not a proposition about the world. Program rules perform evaluation; no model/human truth judgment, reference world answer or per-item veto occurs. Ordinary open recall is the operating mode.

A static single-value case exposes the license boundary: a sole stored value is the only vocabulary candidate, so softmax has no competing factual alternative. Its near-one normalized score cannot establish that value is true. Key matching also has its own gate; a high score cannot rescue an unresolved key. Conversely a resolved key returns `found: true` without requiring a minimum confidence or margin. Across kinds, `recallInOrder` retains the greatest confidence, not simply the first matching kind. Earlier kind order matters on ties.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Found flag, confidence from top probability, and top-two margin.
- Later read-back: Scores are not retained as evidence; with a nonempty session ID the matched key's usage counter is saved for possible promotion.
- Delegated visibility: Model sees answer and rounded confidence/coarse source label; margin is not included in that extension text.
- Selection predicate: Exact/substring then token overlap at least 0.5 then fuzzy threshold; within values use maximum softmax; across shelves use greatest confidence.
- Invalidation or expiry: Recomputed from current facts/configuration; counters remain on value replacement and deduplicate only against the last session ID.
- Activation or effect: Match gates and confidence ranking can change returned content; usage counters can qualify entries for promotion.
- Evidence limits: No calibration, world-truth criterion or executed accuracy/benefit comparison. Numerical cleanup's target is signal magnitude; default sharpening and CORVACS-lite can be identity functions.

SRC-1 `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`, `src/nuggets/core.ts`, `.pi/extensions/nuggets.ts`.

> const probs = softmaxTemp(simsSum, this._tempT);
> let bestIdx = 0;
> for (let i = 1; i < V; i++) {
> if (probs[i] > probs[bestIdx]) bestIdx = i;
> }
> --- `src/nuggets/memory.ts`

> return { answer: word, confidence, margin, found: true, key: tag };
> --- `src/nuggets/memory.ts`

> if (!best.found || result.confidence > best.confidence) {
> best = { ...result, nugget_name: name };
> }
> --- `src/nuggets/shelf.ts`

> if (p === 1.0) return z;
> --- `src/nuggets/core.ts`

> if (a <= 0) return z;
> --- `src/nuggets/core.ts`

#### EPI-RTE-fact-withdrawal
Label: Fact withdrawal

Part of: [RT-RTE-memory-context](runtime.md#rt-rte-memory-context)

Explicit forget request → key requirement → short-circuit local/shelf deletion → report. This disposition part does not judge falsity. Model/caller proposes key, extension chooses deletion path, with no separate human veto or oracle. Mode is ordinary open use. Recovery is later overwrite/reload, not an atomic cross-copy withdrawal. Supplied runtime already identifies the short-circuit; additional direct inspection shows reconstruction merges positive snapshots without deletion tombstones.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reports Forgot if either attempted branch returns true; details contain only remaining current local facts.
- Later read-back: Session start can hydrate the undeleted shelf value; branch reconstruction can retain earlier snapshot keys absent from later snapshots.
- Delegated visibility: Model sees success text and remaining snapshot, not a cross-store withdrawal receipt.
- Selection predicate: Required key; local exact-key delete first, shelf helper only on false.
- Invalidation or expiry: No cascading removal of promoted Markdown; shelf deletion may remove only the first matching kind; history has no explicit tombstone for normal forget.
- Activation or effect: Local prompt content can change immediately while future shelf/history read-back revives it.
- Evidence limits: Static reachability, not an observed reappearance. Library direct forget does remove matching case-insensitive facts, so not every deletion fails.

SRC-1 `.pi/extensions/nuggets.ts`, `src/nuggets/memory.ts`; short-circuit passage supplied in [RT-RTE-memory-context](runtime.md#rt-rte-memory-context).

> for (const [k, v] of Object.entries(details.facts)) {
> if (v) {
> facts.set(k, v);
> } else {
> facts.delete(k);
> }
> }
> --- `.pi/extensions/nuggets.ts`

#### EPI-RTE-kind-migration
Label: Kind migration

Operator-launched legacy JSON → backup → heuristic buckets → case-insensitive merge into kind JSON → archive. Distinct from the supplied extension/promotion routes; runtime mentions this driver without declaring a matching route. Code owns classification/admission, operator starts the operation but does not approve individual facts. Guidance is key prefixes/value slash matching; no truth oracle or content criticism. Ordinary maintenance, not a bounded improvement experiment. Backups permit manual recovery; no automatic rollback on partial write is implemented.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Console paths/counts, or an early no-file return.
- Later read-back: Default-kind stores are loaded by the shelf and consumed by extension recall/hydration.
- Delegated visibility: Later reader sees the winning value and merged usage metadata, not the displaced alternative or merge rationale.
- Selection predicate: `inferMemoryKind`; same lowercased key merges, incoming value wins, hits become maximum.
- Invalidation or expiry: Legacy file archived after writes; backup retained. Subsequent writes can replace resulting values.
- Activation or effect: Reorganizes retained claims and can resolve conflicts by overwrite without evaluating their truth.
- Evidence limits: No live legacy file or migration trace; pure values are reshaped/selected, not accepted or semantically derived.

SRC-1 `src/migrate-memory.ts`, `src/nuggets/kinds.ts`.

> target[idx] = {
> key: incoming.key,
> value: incoming.value,
> hits: Math.max(existing.hits ?? 0, incoming.hits ?? 0),
> last_hit_session: incoming.last_hit_session || existing.last_hit_session || "",
> };
> --- `src/migrate-memory.ts`

#### EPI-RTE-memory-tests
Label: Memory tests

Developer-triggered Vitest → constructed memory fixtures → assertions. This evaluator route has no supplied canonical counterpart; boundary lists it as inspected test source, while runtime declares production routes. Test authors supply reference expected outputs, code judges results, developer can revise/reject changes; no automatic admission into the running memory store follows. Mode is bounded fixture tests, triggered by the package test script, not an online improvement loop. Target/domain: specified remember/recall/upsert/forget/save/load/hit-count/matching behavior for finite examples.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Would pass/fail assertions under Vitest; not executed here.
- Later read-back: inapplicable — test results are not wired to retained fact admission or later model prompts.
- Delegated visibility: Test runner receives fixture state and expected values; production model receives no test certificate.
- Selection predicate: Shipped test cases and explicit assertions, not random user claims or source evidence.
- Invalidation or expiry: Fixtures are recreated per test and temporary directories removed; no production rollback consumer.
- Activation or effect: Assertions can fail a developer test command, not block ordinary remember calls.
- Evidence limits: Source assertion existence does not establish passing execution, broad generalization or factual truth of arbitrary retained content.

SRC-1 `tests/memory.test.ts`, `package.json`.

> n.remember("color", "blue");
> const result = n.recall("color");
> expect(result.found).toBe(true);
> expect(result.answer).toBe("blue");
> expect(result.confidence).toBeGreaterThan(0);
> --- `tests/memory.test.ts`

### Claims

#### EPI-CLM-associative-recall
Label: Associative recall

Claim: HRR stores individually retrievable facts and recall is algebraic/sub-millisecond. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-ingress-control](runtime.md#rt-clm-ingress-control), whose subject is transport admission. Implementation supports finite-vocabulary associative recall, not a calibrated knowledge warrant or measured speed.

> - **Holographic memory** — facts are stored as superposed complex-valued vectors using Holographic Reduced Representations (HRR). Recall is algebraic, sub-millisecond, and runs locally with zero external dependencies.
> --- `README.md`

#### EPI-CLM-memory-improvement
Label: Memory improvement

Claim: repeated recalls promote a fact to permanent context, making the agent faster and cheaper. SRC-1 `README.md`, doctrine/design. It overlaps the subject of [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion) but is a claim about its effect, not that route's implementation identity; no matching supplied claim exists.

The writer selects three-hit entries and reconstructs recognized Markdown sections. This creates operational placement without truth acceptance. Additional static counterexamples: `last_hit_session` deduplicates only consecutive identical IDs, so alternating A/B/A can count three hits from two distinct sessions; upsert changes value without resetting that key's hits. Existing promoted keys remain when source facts disappear. Parsing accepts only section headers and formatted fact lines: given existing free prose plus a new qualifying candidate, the rewrite can omit the prose. No automatic withdrawal linkage exists.

> - **Self-improving** — when a fact is recalled 3+ times across sessions, it gets promoted to permanent context. The agent gets faster and cheaper over time.
> --- `README.md`

> if (fact.last_hit_session !== sessionId) {
> fact.hits = (fact.hits || 0) + 1;
> fact.last_hit_session = sessionId;
> if (this.autoSave) this.save();
> }
> --- `src/nuggets/memory.ts`

> const factMatch = stripped.match(/^-\s+\*\*(.+?)\*\*:\s*(.+)$/);
> if (factMatch && currentSection) {
> sections[currentSection][factMatch[1].trim()] = factMatch[2].trim();
> }
> --- `src/nuggets/promote.ts`

Threshold and ordinary-call evidence: see [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion). Proposed self-change is context selection over future sessions; lower action time/cost is the separately stated objective. Use evidence can shape selection and a file can change, but usefulness assessment, external loading and later causal dependence are not established. No exercised self-improvement or benefit attribution follows.

### Evidenced absences

#### EPI-ABS-truth-acceptance
Label: Truth acceptance

- implementation conclusion status: absent

Bounded absence: no evidence-consuming decision accepting a truth-apt value against a named truth/reliability criterion for a stated use/scope was found in the local memory implementation and extension routes inspected at SRC-1's frozen revision. Search boundary: `src/nuggets/memory.ts`, `src/nuggets/shelf.ts`, `src/nuggets/kinds.ts`, `src/nuggets/promote.ts`, `src/migrate-memory.ts`, material dispatch/hooks in `.pi/extensions/nuggets.ts`; test comparison in `tests/memory.test.ts`. Inspection question was whether any return/write/rejection branch consumes evidence about candidate truth rather than nonemptiness, key/string resemblance, signal similarity or usage count. The routes above enumerate those actual checks and consumers. Load-bearing passages: [EPI-RTE-fact-upsert](#epi-rte-fact-upsert), [EPI-RTE-recall-score](#epi-rte-recall-score) and supplied [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).

This is distinct from any supplied record: runtime declared no absence. It supports absence of local evidence-consuming truth acceptance and hence of lifecycle integration *after such acceptance* in these inspected paths. It does not deny that an external model/user may evaluate content before proposing a write, or that hosted tools may return evidence; those internal processes and actual cases are uninspected. It also does not deny operational admission, regression-test evaluation, policy supply or useful recall.
