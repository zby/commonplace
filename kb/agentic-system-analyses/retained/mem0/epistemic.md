---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Mem0's extraction, admission, reliance and withdrawal routes, separating stored conversation claims from warranted knowledge."
run-id: AAS-2026-10-14-mem0-5b642a1731b4-01
reviewed-boundary: "0724291bd864cf807e88ee8981c8226644e8fb42"
---

# Mem0 epistemic report

## Source-and-claim boundary

The question is how conversation content becomes retained claims, what checks license reliance, and which consumers give those claims consequential force. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identities and evidence layers are see [Source register](boundary.md#source-register). This is a complete artifact, partial loop: hosted internals, evaluation-submodule contents, external model weights and host execution are unavailable. These respectively prevent hosted epistemic reconstruction, benchmark-protocol assessment, internal reasoning assessment and observed host-compliance conclusions. No run or causal experiment is supplied. Source reconstruction is not successful operation.

The knowledge/warrant declarations assessed here are [EPI-CLM-evidence-bound](#epi-clm-evidence-bound), [EPI-CLM-platform-scores](#epi-clm-platform-scores) and [EPI-CLM-atomic-update](#epi-clm-atomic-update). The table distinguishes direct inspection from the provisional runtime. Available but uninspected mechanisms prevent a system-complete negative about evaluation or acceptance.

| Entry point or operation | Source path under SRC-1 | Coverage and conclusion limit |
| --- | --- | --- |
| Python inferred add | `mem0/memory/main.py`; `mem0/configs/prompts.py` | Direct reads of model call, parsing, eligibility, insertion and selected active-prompt rules; see [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), [EPI-RTE-extraction-checks](#epi-rte-extraction-checks). Prompt read is selected rules, not exhaustive instruction audit. |
| Python raw/procedural write, update/delete | `mem0/memory/main.py` | Direct reads of persistence, procedural summary, explicit update/delete; see [RT-RTE-direct-write](runtime.md#rt-rte-direct-write). |
| Python search and expiry | `mem0/memory/main.py`; `mem0/utils/lemmatization.py` | Direct synchronous search/formatting and keyword preprocessing reads; validation/get/async details supplied by [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), [RT-RTE-direct-write](runtime.md#rt-rte-direct-write). Ranking quality and provider internals unresolved. |
| README chat and proxy | `README.md`; `mem0/proxy/main.py` | README claim passages directly read; consumer/proxy reconstruction supplied by [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories), [RT-RTE-proxy-chat](runtime.md#rt-rte-proxy-chat). Proxy incompatibility prevents treating intended recall delivery as a successful current path. |
| OpenClaw hooks/add/recall | `integrations/openclaw/index.ts`; `integrations/openclaw/recall.ts`; `integrations/openclaw/tools/memory-add.ts` | Supplied [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add). Host execution and fact selection unobserved. |
| OpenClaw registered operations and maintenance | `integrations/openclaw/tools/index.ts`; `integrations/openclaw/tools/memory-update.ts`; `integrations/openclaw/tools/memory-delete.ts`; `integrations/openclaw/tools/memory-event-status.ts`; `integrations/openclaw/skills/memory-triage/SKILL.md` | Registration directly read: search/add/get/list/update/delete/event-list/event-status. Direct update/delete/event-status bodies and selected triage update rules; see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal), [EPI-RTE-event-status](#epi-rte-event-status). Get/list/event-list bodies not directly inspected; no exhaustive provider or host verdict. |
| Python CLI dispatch/add/import | `cli/python/pyproject.toml`; `cli/python/src/mem0_cli/app.py`; `cli/python/src/mem0_cli/commands/memory.py`; `cli/python/src/mem0_cli/commands/utils.py`; `cli/python/src/mem0_cli/backend/platform.py` | Entry point and command inventory searched; add forwarding, add command body, import body and platform add body directly read; see [EPI-RTE-cli-import](#epi-rte-cli-import). Other command bodies not inspected; command availability is not backend warrant. |
| Node CLI | `cli/node/src/index.ts` | Dispatch inventory searched: memory CRUD/import, entities, events, configuration, setup and agent-rush. Command bodies uninspected; no Python parity or system-complete admission conclusion. |
| Server controls/configuration and hosted Python | `server/main.py`; `server/server_state.py`; `mem0/client/main.py` | Supplied [RT-RTE-server-access](runtime.md#rt-rte-server-access), [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config), [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client). Generated instructions are proposals until separately installed. Hosted acceptance is opaque. |
| TypeScript engine, other integrations/dashboard/examples/providers | `mem0-ts/src/oss/src/memory/index.ts`; `integrations/`; `server/`; `examples/`; `mem0/` | TypeScript extraction supplied by runtime; remaining implementations not directly assessed here. Prevents system-complete negatives or cross-language equivalence. |
| Evaluators | `tests/test_memory.py`; `README.md`; `.gitmodules` | Direct source read of mocked extraction/embedding regression test; test inventory searched. No test execution. Other evaluators uninspected; benchmark submodule unavailable per boundary. Neither test source nor reported scores establishes observed truth checking on a memory. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-data](#epi-obj-data) — raw message part | Caller statements and possibly instructions | Direct retained content | see record; [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | Source truth/authorship unknown; bypasses extraction |
| [EPI-OBJ-data](#epi-obj-data) — extracted statement part | Preferences, events, recommendations and agent actions | Conversation-derived fact candidate | see record; [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) | Model producer; recommendation occurrence is not its correctness |
| [EPI-OBJ-data](#epi-obj-data) — procedural summary part | Claims about prior task actions, outputs and state | Continuation summary | see record; [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | Model producer; preservation requested, not independently checked |
| [EPI-OBJ-data](#epi-obj-data) — replacement text part | Caller-proposed revised claims | Explicit revision | see record; [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | ID/existence checks are not truth checks |
| [EPI-OBJ-text-lemmatized](#epi-obj-text-lemmatized) | None as an independently warranted proposition; derived matching terms | Keyword retrieval index | see record | Lossy token representation is not an accepted claim |
| [RT-OBJ-custom-instructions](runtime.md#rt-obj-custom-instructions) | Usually policy, not truth-apt; arbitrary configured text remains possible | Extraction guidance | see record | Model compliance unobserved |
| [RT-OBJ-config-overrides](runtime.md#rt-obj-config-overrides) | None inherent in provider/settings mapping | Production configuration | see record | Installation and truth acceptance differ |
| [RT-CMP-openai-llm](runtime.md#rt-cmp-openai-llm) | Not determinable as localized claims inside weights | Generation component | see record | External internals and exact numerical version uninspected |
| [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding) | No individuated truth claim in dense vectors | Similarity representation | see record | Stored vectors change; training or warrant does not follow |

Raw messages, extracted facts, procedural summaries and replacement facts are different content/producer parts of the data object. Their routes below remain separate; they do not share a universal extraction check. Prior messages are independently retained/reloaded as see [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), not an independently accepted evidence archive.

## Authority-route ledger

Fields owned by declaring records are `see` citations. All implemented entries concern source wiring, with activation and timing conditional on invocation, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) | content transformation | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: indeterminate | Conversation to proposed statements | Model under additive instruction | see route | Proposed factual text | Candidate generation | Requested source fidelity; no demonstrated entailment | Permits candidates to enter eligibility processing | see [RT-BAP-extraction-context](runtime.md#rt-bap-extraction-context) | see route | [EPI-CLM-evidence-bound](#epi-clm-evidence-bound) | Fidelity request is not fidelity verification | Could reshape, derive or conjecture; deciding actual relation requires inputs and outputs |
| [EPI-RTE-extraction-checks](#epi-rte-extraction-checks) | check/evidence production | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Nonempty embeddable text; hash membership | Python parsing/map/hash checks, structural domain | After generation, before insertion | Skip or eligible record | Enforcing eligibility signal | Shape and bounded hash membership only | Determines what proceeds to insertion | see record | see record | [EPI-CLM-evidence-bound](#epi-clm-evidence-bound) | Eligibility is not truth | No source-veracity or semantic-equivalence test established by these checks |
| [EPI-RTE-extraction-checks](#epi-rte-extraction-checks) | disposition/acceptance | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Eligibility result consumed | Code branches | see record | Candidate excluded or admitted | Enforcing | Operational admission, not evidence-consuming truth acceptance | Skip duplicate/missing text or prepare insertion | see record | see record | none | none | Admission criterion is procedural |
| [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) | retention | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Eligible text to stores | Adapter success and history/entity attempts | see route | ADD result or error/partial effects | Permissive retention | No extra truth license from persistence | Makes candidate available to future retrieval | see route | see route | none | none | Not atomic across stores |
| [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | content transformation | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: acquisition/import | Raw caller text | Non-system-message branch | see route | Verbatim text stored | Permissive | External source warrant unknown, not upgraded | Bypasses extraction | see route | see route | none | none | Caller can import false content |
| [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | content transformation | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: indeterminate | Procedural history to summary | Summary model; nonempty-content check | Agent/procedural branch | Stored summary | Permissive | Requested preservation, not checked semantic completeness | Summary becomes retrievable | see route | see route | none | none | No actual summary trace; semantics unresolved |
| [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | disposition/acceptance | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: acquisition/import | Explicit replacement/deletion | Caller proposal, shape/existence and adapter checks | Explicit mutation | Replace/remove ID and history event | Enforcing mutation | Caller-selected revision, no independent veracity criterion | Later reads reflect replacement/withdrawal if adapters succeed | see route | see route | [EPI-CLM-atomic-update](#epi-clm-atomic-update) | Cross-store atomicity not established | History is not automatic rollback |
| [EPI-RTE-keyword-index](#epi-rte-keyword-index) | content transformation | implemented | [EPI-OBJ-text-lemmatized](#epi-obj-text-lemmatized) | non-truth-apt policy/content update: keyword representation | Text to matching terms | Lemmatizer/fallback | Writes and query preprocessing | Matching representation | Ranking input | No independent proposition license | Influences candidate scores | see record | see record | none | none | Does not replace stored source text |
| [EPI-RTE-memory-selection](#epi-rte-memory-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Search candidates for query | Scores, scope and expiry rules | Search before delivery | Ranked text-bearing results | Ranking | Relevance estimate, not truth probability | Chooses content visible to caller | see record | see record | none | none | Expiry is visibility, not universal withdrawal |
| [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories) | content transformation | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: indeterminate | Memory context to answer | External answer model | see route | Assistant answer | Advisory natural-language dependence | No independent answer acceptance | Answer returned after addition | see [RT-BAP-answer-context](runtime.md#rt-bap-answer-context) | see route | none | none | Answer and extraction can reintroduce assistant-origin claims |
| [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks) | operational admission/selection/consumption | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Retained facts to host prompt | Plugin selection and budgeting | see route | Recalled context; static protocol | Advisory/ranking | No truth endorsement from recall | Changes host input | see route | see route | none | none | Host compliance unobserved |
| [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add) | disposition/acceptance | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: acquisition/import | Foreground proposed facts | Agent choice and tool noise/session checks | see route | Direct provider add request | Permissive | Warrant of agent deduction unknown | Skills branch requests infer:false | see route | see route | none | none | Fact label does not prove deduction or acceptance |
| [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Selected memory to deletion request | ID, query uniqueness/score, bulk confirmation | Foreground tool | Delete or candidates/blocked response | Enforcing request gate | Search match does not establish falsity | Can remove content from later recall | see record | see record | none | Matching is not criticism | Provider semantics separate |
| [EPI-RTE-event-status](#epi-rte-event-status) | check/evidence production | implemented | [EPI-OBJ-data](#epi-obj-data) | no content change | Remote processing event | Backend-reported status | Explicit tool call | Status/results to host | Advisory | Processing report, not factual truth | Host may decide follow-up; no automatic rollback shown | see record | see record | none | none | Hosted evaluator opaque |
| [EPI-RTE-cli-import](#epi-rte-cli-import) | content transformation | implemented | [EPI-OBJ-data](#epi-obj-data) | truth-apt transformation: acquisition/import | File content to hosted add | JSON/content selection and HTTP wrapper | CLI import | Request/counts | Permissive | Source warrant unknown | Imports without per-item truth approval | see record | see record | none | Import count is not accepted knowledge | Backend processing opaque |
| [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config) | behavior/policy adaptation | implemented | [RT-OBJ-custom-instructions](runtime.md#rt-obj-custom-instructions) | non-truth-apt policy/content update: extraction guidance/configuration | Proposed settings to live engine | Admin and construction checks | see route | Installed configuration or proposal only | Enforcing installation/advisory generation | Installation does not validate instruction efficacy | Reconstructs later extraction machinery | see route | see route | none | none | No automatic evidence-responsive improvement established |

The active prompt also supplies a doctrine-level ampliative witness: it prescribes interpreting “I used to love hiking” as “no longer loves hiking.” The former can be true while the person still loves hiking; cessation is a pragmatic inference, not entailed by the sentence alone. This challenges a universal meaning-preservation claim without claiming the model actually made that inference. See [EPI-CLM-evidence-bound](#epi-clm-evidence-bound). No warranted-premise entailed claim production is established from supplied traces. No lifecycle-integration row is inferred merely from indexing/entity linking: acceptance against a named epistemic criterion has not been established for those retained items.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-evidence-bound](#epi-clm-evidence-bound) | Evidence-bound, accurate, meaning-preserving extraction | see record | Explicit integrity and attribution rules | see [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), [EPI-RTE-extraction-checks](#epi-rte-extraction-checks) | None supplied | No input/output comparison; model inference opaque | Implemented request for fidelity plus procedural admission | Prescribed cessation inference is not universal entailment; truth/fidelity check not established |
| [EPI-CLM-platform-scores](#epi-clm-platform-scores) | Platform recall/performance gains | see record | Attributed benchmark table and platform qualification | see [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client) | None inspectable here | Model stack/top_200 declaration is not protocol or intervention evidence; evaluation submodule unavailable | Reported platform results, not OSS efficacy or mechanism attribution | Remote optimizations and evaluators opaque |
| [EPI-CLM-atomic-update](#epi-clm-atomic-update) | Atomic update preserving ID/history | see record | Tool description and triage protocol | see [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) | None supplied | Tool awaits provider; local vector update precedes separate SQLite history write | ID-preserving replacement and attempted history are implemented locally | Universal cross-store atomicity unsupported; hosted guarantee unresolved |

## Bounded conclusion

Mem0 implements acquisition, generation of conversation-derived candidates, retention and consequential delivery. Source warrant is unknown on imports and is not upgraded by storage. Extraction requests preserve detail and attribution, but the implemented eligibility checks establish parse/embedding/hash conditions rather than truth. The hash check has an operative rejection consumer; it is not merely a logged metric. Direct writes, procedural summaries and skills-mode agent facts are counterpaths to any universal extraction gate. See [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add), [EPI-RTE-extraction-checks](#epi-rte-extraction-checks).

Retained text gains operational availability before epistemic acceptance is established. Search ranks and filters; README delivery then discards IDs, scores and attribution and puts memory strings into the answer system message. Thus source-side attribution support is not a provenance check at the answer consumer. The horizon spans later additions and chats, subject to scope/store survival; the force is ranking followed by model-interpreted context, not guaranteed compliance. Existing memories and recent messages also influence later extraction. See [RT-BAP-answer-context](runtime.md#rt-bap-answer-context), [RT-BAP-extraction-context](runtime.md#rt-bap-extraction-context), [EPI-RTE-memory-selection](#epi-rte-memory-selection).

The inspected model routes leave semantic relation indeterminate at the instance level. Doctrine includes at least one ampliative inference, but no observed conjecture test, evidence-consuming acceptance decision, or post-acceptance integration is established for an extracted claim. Explicit update/delete and OpenClaw maintenance instructions are real revision/withdrawal affordances, not evidence that criticism was formulated or exercised. The delete query gate judges target match rather than claim truth. Expiry hiding is neither retraction nor erasure. Event status reports processing, not warrant. See [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal), [EPI-RTE-event-status](#epi-rte-event-status).

Configuration changes directly adapt future extraction policy, while generated instructions alone remain proposals. External default models are separately assessed by see [RT-CMP-openai-llm](runtime.md#rt-cmp-openai-llm), [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding): inference adapters do not establish weight learning, exact version fixity, or internal epistemic procedures. Retained experience can shape later input without establishing improved capacity, reflection, autonomous criticism or exercised self-improvement. These remain independent properties; lack of run evidence does not erase implemented retention and delivery. Uninspected included operations and opaque hosted routes prevent a system-wide no-acceptance verdict. Platform performance remains reported, not causally supported within this boundary.

## Shared records

### Operative objects

#### EPI-OBJ-data
Label: Memory data text

Source-native identity: vector payload `data`, returned as `memory`. Natural-language representation, stored in the configured vector-store payload with old/new copies attempted in SQLite history. Its material parts are raw message text, extracted factual statements, procedural summaries and explicit replacement text. They have different producers/checks, separated in the ledger. No operative-object counterpart appears among supplied runtime objects: [RT-OBJ-custom-instructions](runtime.md#rt-obj-custom-instructions) is input policy, not retained fact text. The data participates in [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) and [RT-RTE-direct-write](runtime.md#rt-rte-direct-write); it is not the entirety of either route. SRC-1, `mem0/memory/main.py`, implementation.

> mem_metadata["data"] = text
>             mem_metadata["text_lemmatized"] = text_lemmatized
>             mem_metadata["hash"] = mem_hash
> --- `mem0/memory/main.py:1032-1034`

#### EPI-OBJ-text-lemmatized
Label: Lemmatized keyword text

Source-native identity: `text_lemmatized`, a symbolic search-term string stored beside the natural-language `data` in vector payloads; query-side counterpart is transient. Distinct from [EPI-OBJ-data](#epi-obj-data): lossy terms drive fixed matching rather than model interpretation of factual sentences. No counterpart among supplied runtime objects; overlaps the indexing part of [RT-RTE-extract-add](runtime.md#rt-rte-extract-add). SRC-1, `mem0/utils/lemmatization.py`, `mem0/memory/main.py`, implementation; storage passage is above.

> for token in doc:
>         if token.is_punct or token.is_stop:
>             continue
> --- `mem0/utils/lemmatization.py`

### Routes

#### EPI-RTE-extraction-checks
Label: Extraction eligibility checks
Part of: [RT-RTE-extract-add](runtime.md#rt-rte-extract-add)

Model proposes text on open inferred additions; Python decides eligibility and vetoes missing text/embeddings or matching hashes before insertion. No per-item human approval or expected-answer oracle is supplied. Guidance is the additive extraction prompt; admitted text/metadata persist, not the checks' reasoning. This is a check and its disposition subroute, not a second declaration of the entire addition. SRC-1, `mem0/memory/main.py`, implementation.

- Immediate return: Loop continuation for rejected items or assembled insertion records; outer add returns persisted ADD records or errors.
- Later read-back: Admitted text can enter subsequent search/extraction; rejected proposal text has no insertion through this subroute.
- Delegated visibility: Embedding provider receives generated text before hash disposition; store sees assembled eligible records.
- Selection predicate: Nonempty text in embed_map; MD5 absent from retrieved-existing and within-batch hash sets.
- Invalidation or expiry: Separate explicit update/delete and expiry visibility rules; this check cannot roll back earlier store effects.
- Activation or effect: Eligibility branches enforce candidate skipping before insertion; no observed execution supplied.
- Evidence limits: Hash membership is bounded to retrieved records and batch; no semantic or source-truth oracle; malformed object shapes can still fail outside these guards.

Behavioral-authority path: insertion loop consumes code eligibility branches with enforcing force in the current addition; resulting stored text reaches later extraction/search under their separate selection rules.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> text = mem.get("text")
>             if not text or text not in embed_map:
>                 continue
>
>             mem_hash = hashlib.md5(text.encode()).hexdigest()
>             if mem_hash in existing_hashes or mem_hash in seen_hashes:
>                 logger.debug(f"Skipping duplicate memory (hash match): {text[:50]}")
>                 continue
> --- `mem0/memory/main.py`

A concrete deduction: two proposals with identical text `User likes Python`, both embeddable, and no retrieved hash match: first adds its MD5 to seen_hashes; second is skipped. This proves bounded identical-text filtering from code, not truthful content or global uniqueness.

> seen_hashes.add(mem_hash)
> --- `mem0/memory/main.py:1026-1026`

#### EPI-RTE-keyword-index
Label: Keyword index transformation

Text → lemmatization/fallback → stored keyword representation or query matching. Code owns transformation; spaCy supplies lemmas if available. This indexing subroute overlaps [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) and [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), so is not contained in exactly one supplied route. SRC-1, `mem0/utils/lemmatization.py`, `mem0/memory/main.py`, implementation.

- Immediate return: Space-joined selected terms, or original text on unavailable NLP.
- Later read-back: Stored text_lemmatized can participate in future keyword matching; query terms are transient, not retained experience.
- Delegated visibility: NLP consumes lowercase text; store receives keyword representation; semantic embedding still consumes original text.
- Selection predicate: Skip punctuation/stop tokens; retain alphanumeric lemmas and qualifying original -ing forms.
- Invalidation or expiry: Explicit text update rebuilds the keyword field; deletion removes its payload.
- Activation or effect: Keyword results supply scoring inputs; no observed relevance benefit.
- Evidence limits: NLP output and provider keyword-search behavior untested; index is not a meaning-preserving factual statement.

Behavioral-authority path: keyword-search provider consumes stored/query terms through a symbolic matching channel; ranking force reaches future search calls while the payload survives.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> nlp = get_nlp_lemma()
>     if nlp is None:
>         return text
>
>     doc = nlp(text.lower())
> --- `mem0/utils/lemmatization.py`

> return " ".join(tokens)
> --- `mem0/utils/lemmatization.py`

Concrete conditional trace: input `I like Python`, when get_nlp_lemma returns None, exits unchanged as `I like Python`. With NLP available, code lowercases it and drops token classes above; exact terms require the external model result. Neither branch changes the original stored data through this function.

#### EPI-RTE-memory-selection
Label: Python memory selection

Query/scope → semantic candidate pool plus keyword/entity scores → expiry filtering → score/rank → memory objects. Python owns selection; configured stores supply scores. Distinct from the supplied addition and chat routes: this is the read selector called by [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories), not the driver. Caller chooses query/scope; code ranks/vetoes eligibility; optional reranker can reorder under the runtime-described fallback. No human approval or expected-answer oracle; open search requests, not an improvement experiment. SRC-1, `mem0/memory/main.py`, implementation.

- Immediate return: Ranked memory objects with text, ID, scores and promoted attribution/identity/expiry fields.
- Later read-back: Previously inserted data is returned to subsequent caller invocations; search itself does not accumulate new text.
- Delegated visibility: Embedder/store receive query; caller receives selected payload text and metadata; README forwards only memory strings.
- Selection predicate: Scope-filtered semantic candidate pool, keyword/entity score inputs, threshold/top_k and expiry; empty data omitted.
- Invalidation or expiry: Search omits expired payloads unless show_expired; direct ID reads and raw admin listings are counterpaths per runtime.
- Activation or effect: Ranking changes which stored claims are offered for later model use; behavioral activation unobserved.
- Evidence limits: Scores assess matching, not factual correctness; adapter filtering and ranking accuracy remain dependencies.

Behavioral-authority path: caller consumes selected results through API return; ranking force governs the current retrieval. README and host hooks subsequently supply selected text through model-input channels over later invocations, as their supplied records describe.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for mem in semantic_results:
>             payload = mem.payload if hasattr(mem, 'payload') else {}
>             if not show_expired and _payload_is_expired(payload):
>                 continue
> --- `mem0/memory/main.py:1682-1685`

> memory=payload.get("data", ""),
> --- `mem0/memory/main.py:1724-1724`

#### EPI-RTE-memory-withdrawal
Label: OpenClaw memory withdrawal

Foreground agent/user-supplied ID or query → session guard/search gate → provider deletion → host result. Distinct from [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add): this is destructive withdrawal, not fact admission. Tool description directs deletion of wrong/obsolete/user-forgotten content, but code judges session, target match and bulk confirmation, not claim falsity. Computational proposer is the host agent where it invokes the tool; human authorship of request and actual tool approval are unresolved. No expected-answer oracle; open explicit mutation. Errors become tool responses, with no automatic rollback; deletion is described as irreversible. SRC-1, `integrations/openclaw/tools/memory-delete.ts`, implementation and doctrine/design.

- Immediate return: Deleted/candidate/confirmation-required/subagent-blocked response or caught error.
- Later read-back: Deleted provider item should no longer enter later recall, conditional on provider contract; exact remote semantics uninspected.
- Delegated visibility: Provider receives ID or scoped query/bulk user ID; host receives target text/candidates or deletion status.
- Selection predicate: ID directly; query deletes first result when unique or score above 0.9; otherwise host must choose; bulk requires confirm:true; recognized subagents blocked.
- Invalidation or expiry: Explicit destructive request; no automatic restore or fact revalidation.
- Activation or effect: Deletion request is code-gated; eventual provider deletion and host reliance unobserved.
- Evidence limits: Confirmation is an agent-supplied boolean, not proof of human approval; high similarity is not evidence of falsity.

Behavioral-authority path: provider consumes deletion request through its mutation API with destructive operational force; subsequent recall loses that item conditional on provider deletion semantics, over future sessions until reintroduced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (results.length === 1 || (results[0].score ?? 0) > 0.9) {
>             await provider.delete(results[0].id);
> --- `integrations/openclaw/tools/memory-delete.ts`

> if (!confirm) {
>             return { content: [{ type: "text", text: "Bulk deletion requires confirm: true." }], details: { error: "confirmation_required" } };
> --- `integrations/openclaw/tools/memory-delete.ts`

The triage doctrine supplies content-directed revision guidance, a countercase to treating all Mem0 maintenance as additive:

> **Temporary vs permanent changes**: A temporary constraint (e.g., injury pausing a hobby) does NOT contradict the underlying preference. Store the constraint as a new memory; don't delete the preference.
> --- `integrations/openclaw/skills/memory-triage/SKILL.md`

This is shipped guidance, not evidence of a formulated criticism actually changing reliance or a retained criticism shaping another round.

#### EPI-RTE-event-status
Label: OpenClaw processing status

Event ID → backend getEvent → formatted status/results → host. Distinct from [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client) add/search: this operation reports processing outcomes. No automatic disposition consumer exists in this tool; its operative force is advisory host delivery. SRC-1, `integrations/openclaw/tools/memory-event-status.ts`, implementation.

- Immediate return: Status/results text and full event details; platform-only/error response otherwise.
- Later read-back: Remote event is retrieved on a later explicit request; this tool does not itself retain a new event or memory.
- Delegated visibility: Backend sees event ID; host sees reported status, latency, timestamps and result snippets.
- Selection predicate: Exact event_id with configured platform backend.
- Invalidation or expiry: uninspected — remote event retention policy unavailable.
- Activation or effect: Supplies processing report to host; no code-wired rollback or factual rejection from that status.
- Evidence limits: Backend status producer opaque; successful get is not independent verification of stored fact truth or processing completeness.

Behavioral-authority path: host agent consumes tool-result text/details with advisory force for its next decision; no installed policy change or mandatory consequence is wired by this reporting tool.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const ev = await deps.backend.getEvent(eventId);
>
>         const status = String(ev.status ?? "—");
> --- `integrations/openclaw/tools/memory-event-status.ts`

#### EPI-RTE-cli-import
Label: CLI file import

CLI file → JSON list normalization → memory/text/content selection → backend add → added/failed counters. Python command owns iteration; caller selects file and optional identity overrides; remote backend owns memory admission. No per-item human approval or expected-answer oracle. Open import operation; empty content and raised errors counted as failures, otherwise counted as added; guidance is field-selection/defaults, not truth criteria. No bulk rollback/retry is wired. Distinct from [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client): shipped CLI importer adds content-selection and accounting consumers around a separate backend wrapper. SRC-1, `cli/python/src/mem0_cli/commands/utils.py`, `cli/python/src/mem0_cli/backend/platform.py`, implementation.

- Immediate return: Added/failed counts or file-parse error; counts track wrapper outcomes, not epistemic acceptance.
- Later read-back: Imported content is offered to later hosted reads subject to remote processing; internals uninspected.
- Delegated visibility: Backend receives selected content, caller/item identity and item metadata; CLI emits counts rather than per-item provenance.
- Selection predicate: memory field preferred over text then content; nonempty content; caller user/agent ID overrides item ID.
- Invalidation or expiry: Separate backend mutations; importer has no rollback or individual truth withdrawal.
- Activation or effect: Calls add and increments counters; actual retention/benefit unobserved.
- Evidence limits: Successful request can precede remote processing; import does not preserve all file provenance or certify content.

Behavioral-authority path: backend consumes wrapped user-message requests with permissive import force; CLI consumes request outcome in current-run counters. Hosted future memory consumers are opaque, so their precise force/horizon cannot be established here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> content = item.get("memory", item.get("text", item.get("content", "")))
> --- `cli/python/src/mem0_cli/commands/utils.py`

> elif content:
>             payload["messages"] = [{"role": "user", "content": content}]
> --- `cli/python/src/mem0_cli/backend/platform.py`

Concrete code trace: item {"text": "I prefer dark mode"} selects that exact text; backend wraps it as a user message without changing the proposition. It does not establish that the original file author was the user. The ordinary add command separately forwards infer=not no_infer; import omits that option and thus uses the backend default.

### Claims

#### EPI-CLM-evidence-bound
Label: Evidence-bound extraction

Active additive prompt claims/requested role: accurate evidence-bound factual extraction, exact meaning, no fabrication and correct attribution. No supplied runtime claim counterpart; relevant implementation is [RT-RTE-extract-add](runtime.md#rt-rte-extract-add). SRC-1, `mem0/configs/prompts.py`, doctrine/design. These are instructions, not observed results.

> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> --- `mem0/configs/prompts.py`

> - **No Fabrication**: Every detail must trace to the inputs. If you can't point to where it came from, don't include it.
> --- `mem0/configs/prompts.py`

> - "I used to love hiking" = no longer loves hiking, NOT currently loves hiking
> --- `mem0/configs/prompts.py`

The last rule supplies a prescribed non-entailed current-state inference. This qualifies strict preservation doctrine without proving actual output errors. Mocked regression tests cannot settle real semantic fidelity:

> mock_llm.generate_response.return_value = json.dumps(
>         {"memory": [{"text": "The user enjoys Python"}]}
>     )
> --- `tests/test_memory.py`

#### EPI-CLM-platform-scores
Label: Platform benchmark gains

README reports improved memory benchmark scores, with managed-platform qualification. No supplied runtime claim counterpart; [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client) is a delegation mechanism, not benchmark evidence. SRC-1, `README.md`, reported operation and doctrine/design.

> | **LoCoMo** | 71.4 | **92.5** | 7.0K  | 0.88s  |
> --- `README.md`

> All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops) at a top_200 retrieval budget. Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md`

#### EPI-CLM-atomic-update
Label: Atomic memory update

OpenClaw tool declares update atomic and ID/history-preserving. No supplied runtime claim counterpart; relevant local mutation is [RT-RTE-direct-write](runtime.md#rt-rte-direct-write). SRC-1, `integrations/openclaw/tools/memory-update.ts`, doctrine/design; `mem0/memory/main.py`, implementation. The wrapper awaits a provider, while local code writes vector state then history separately; no shared transaction/rollback in this body licenses cross-store atomicity. Hosted atomicity remains unknown.

> description: "Update an existing memory's text in place when a stored fact has changed -- requires the memory ID. Atomic and preserves the ID and history, so prefer this over deleting and re-adding.",
> --- `integrations/openclaw/tools/memory-update.ts`

> self.vector_store.update(
>             vector_id=memory_id,
>             vector=embeddings,
>             payload=new_metadata,
>         )
>         logger.info(f"Updating memory with ID {memory_id=} with {data=}")
>
>         self.db.add_history(
> --- `mem0/memory/main.py`
