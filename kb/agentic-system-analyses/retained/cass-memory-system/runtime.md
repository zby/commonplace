---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "cass_memory_system runtime baseline: context retrieval, reflection admission, caller-assisted onboarding, HTTP tools and host safety hooks at the frozen revision"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
---

# cass_memory_system runtime report

## Runtime account

CM supplies memory services to an enclosing coding agent. It does not own that agent's next coding action. The claimed work is to turn historical sessions into reusable rules and deliver selected rules to later tasks. The package's `cm` and `cass-memory` aliases dispatch the CLI; `cm serve` supplies HTTP JSON-RPC tools, while installed session-end hooks start reflection. These shipped responsibilities are inside the [boundary](boundary.md); cass indexing, the originating agent, model services and host enforcement remain external contracts (SRC-1: `package.json`, `src/cm.ts`, `src/commands/serve.ts`, `src/commands/hook.ts`).

### Ordinary invocation and working context

For `cm context "fix auth timeout" --json`, the principal is the caller under the process's OS identity. CM loads configuration, canonicalizes the requested workspace or cwd, loads the corresponding merged playbooks, extracts task keywords, and filters active bullets by workspace applicability. Code ranks these bullets with lexical relevance, optionally embedding similarity, and effective feedback-derived scores. Code then applies relevance floors, count limits and an approximate token budget. It splits rules from anti-patterns, separately queries cass history with a timeout, adds conflict/deprecation warnings and search pointers, projects compact rule fields, and returns the result. The caller owns interpretation, subsequent tool use and task completion. This is [RT-RTE-context-read](#rt-rte-context-read), using [RT-CMP-embedding-model](#rt-cmp-embedding-model), not an autonomous task-execution loop (SRC-1: `src/commands/context.ts`).

The returned projection retains rule content, IDs, state, maturity, scores and reasoning, but excludes the feedback-event log, source-session list and embedding. History is capped and its snippets shortened. Therefore delivery is neither a full playbook nor a full evidential dossier. Cass failure can leave playbook-only context; semantic failure can leave keyword ranking with a surfaced mode/reason. Optional logging retains a sanitized task and delivered IDs, not proof that those IDs were followed (SRC-1: `src/commands/context.ts`).

This controls what external material is offered to the caller; it does not trim an enclosing agent's accumulated conversation. Code, not the retrieval model, chooses the final set. Omitted rules remain in storage and can be selected on another request; search pointers support further cass queries. In the separate reflection computation, a diary condenses transcript content before another model call. CLI-provider calls run in a separate subprocess context with selected prompt inputs and return JSON; their transcripts are tagged and normally segregated to avoid feeding CM's own prompts back as work sessions. This resembles a call frame whose result escapes, but host tools, context retention and subprocess model internals are outside CM's inspected control. None of these mechanisms proves a host window was compacted or that omitted content was later reloaded (SRC-1: `src/diary.ts`, `src/reflect.ts`, `src/llm.ts`, `src/orchestrator.ts`).

### Production and admission

Reflection takes an explicit transcript or discovers sessions through cass, serializes the workspace reflection driver, snapshots playbook context, and performs model work without holding playbook merge locks. Incremental processing uses transcript growth/watermarks; forced reprocessing suppresses repeated helpful/harmful grading on already-graded material. Exported content becomes a persisted diary; the reflector sees that diary, formatted existing bullets and up to three related-history snippets, not necessarily the whole original trace. It proposes structured deltas. Validation can reject adds; curation checks required fields and handles duplicates before applying deltas to fresh playbooks under ordered locks. Curator conflict detection only records warnings: a logged conflict does not veto admission, and contrary directives are excluded from duplicate matching rather than rejected. Persisted results are later loaded by context retrieval. [RT-RTE-reflection-update](#rt-rte-reflection-update) records the computational admission route and its limits (SRC-1: `src/orchestrator.ts`, `src/diary.ts`, `src/reflect.ts`, `src/validate.ts`, `src/curate.ts`).

A session-end hook is a separate initiation and return path into the same driver. It decides skip versus reflect from host payload and subprocess context, starts `reflect --session ... --json`, and ordinarily detaches with stdout/stderr redirected to a log. Immediate PID return does not mean rules were saved. `--wait` instead waits for exit status. No installed hook or delivered host event was observed here (SRC-1: `src/commands/hook.ts`).

[RT-RTE-onboard-add](#rt-rte-onboard-add) is materially different: CM supplies historical sessions and an extraction protocol, while the calling agent formulates rules and invokes playbook additions. These additions do not share the reflection evidence gate. Batch/import, starter and manual maintenance surfaces are additional symbolic admissions, not evidence that every retained rule was independently checked against history. Feedback and outcome paths can change later scores/maturity without rewriting rule text; [RT-RTE-feedback-update](#rt-rte-feedback-update) traces direct feedback separately (SRC-1: `src/commands/onboard.ts`, `src/commands/playbook.ts`, `src/starters.ts`, `src/commands/mark.ts`, `src/outcome.ts`). Detailed memory revisions and corpus properties remain for the memory analyst.

### Control coverage and forcing cases

Four source-supported forcing cases qualify the load-bearing claims:

1. **An uncorroborated rule can be admitted.** `validateDelta` skips non-add deltas, disabled validation and very short content; it also accepts draft proposals with no success signal. The evidence gate's success/failure language is a heuristic over retrieved snippets, not an independently supplied expected answer. Manual add has optional `--check`, and strict rejection applies only in that checking branch. Thus the owner is CM admission code, strength is **policy**, and implementation is **wired**, but an invariant that every rule has corroborating evidence would be false. Coverage is the reflection add branch and optional manual checks, not arbitrary file writes or all delta kinds. Required contracts are cass's returned hits and the model's judgment; operational correctness is **uninspected** (SRC-1: `src/validate.ts`, `src/commands/playbook.ts`).
2. **A tiny context budget can be exceeded.** The selector always keeps the first relevant bullet even when its projected cost exceeds the budget. The budget applies to projected bullets, not the task, all warnings, history or a host's complete model window. Owner is `selectContextBullets`, enforcement is code selection, strength is **best effort**, implementation is **wired**, operation is **uninspected**. CLI and MCP context use the same generator; a host that reads a resource or exports the whole playbook is not covered by this selector (SRC-1: `src/commands/context.ts`, `src/commands/serve.ts`, `src/commands/project.ts`).
3. **HTTP admission is conditional, not universal authorization.** `serve` defaults to loopback and refuses a non-loopback unauthenticated bind unless an unsafe override is set. When a token is configured, it rejects unmatched POST requests before tool dispatch. The owner is the server; enforcement is bind setup and request handling; strength is **policy**; implementation is **wired** and operation **uninspected**. This is not a per-tool role grant and does not cover CLI, direct filesystem access, host callbacks, model SDK calls or provider subprocesses. External network placement, OS access and client credentials determine the deployed isolation envelope (SRC-1: `src/commands/serve.ts`).
4. **Trauma guard coverage stops at the hook's effect boundary.** The generated pre-tool script checks only a host tool named `Bash` and emits host-native deny JSON for a matching active trauma pattern. Other tool names and malformed input are allowed; storage read errors fail open and invalid regexes are skipped. The Git hook instead scans staged text and can exit nonzero. Neither is a universal shell sandbox. Owner is the installed generated hook plus the host consuming its decision; strength is **best effort**; implementation is **wired**, host activation **uninspected**. CM's own subprocess calls, provider-native tools, extension code, alternative shells and remote workers are not routed through this Python check by the inspected CM code (SRC-1: `src/trauma_guard_script.ts`, `src/commands/guard.ts`, `src/llm.ts`, `src/cass.ts`).

Persistence is also scoped. Reflection locks and fresh reloads coordinate cooperating writers. Each playbook save uses an atomic write, and processed-session marking follows rule persistence. This supports orderly admission and retry bookkeeping, not a multi-file transaction: repo writes, global writes, log append and best-effort post-merge outcomes are separate effects. A crash between them can leave partial durable work; duplicate checks and retries mitigate rather than eliminate that possibility. The owner is the orchestrator and file-writing helpers; strength is **best effort** across files, implementation **wired**, operation **uninspected** (SRC-1: `src/orchestrator.ts`, `src/playbook.ts`, `src/lock.ts`).

### Capability, grants and evidence strength

CM can read/write the configured local state, run cass locally or over SSH, invoke model SDKs or configured agent CLIs, install host hooks, and expose read and mutation tools through HTTP. The current deployed credential set, hook installation, filesystem permissions and isolation envelope were not supplied. Claude CLI flags suppress inherited MCP configuration for that subprocess; they do not establish a general tool sandbox for all supported providers. The SDK path returns structured generation; the CLI path spawns a separately installed program with inherited environment. Provider fallback can change both endpoint and model. [RT-CMP-generation-model](#rt-cmp-generation-model) records the resulting parameter/version uncertainty (SRC-1: `src/llm.ts`, `src/cass.ts`, `src/commands/serve.ts`, `src/commands/hook.ts`).

Product/production changes enter through source builds, compiled artifacts, installation and explicit hook settings changes; inspected runtime reflection changes data, not executable source or weights. The source inspection does not establish a deployed upgrade admission or rollback policy. Package/build and installer source are delivery mechanisms, not observed release success (SRC-1: `package.json`, `install.sh`, `src/commands/hook.ts`).

Added inspection under SRC-1 covers selected implementation ranges in context selection/projection, diary extraction, reflector normalization/iteration, validation bypasses, manual add, direct feedback, merge persistence, HTTP admission, CLI provider execution and generated guards. No new source was registered. No target, tests, providers or services were executed. Source-authored tests remain contracts, not observed runs; model compliance, useful learning, safety effectiveness and causal benefit remain unobserved. Further details of maintenance/import/starter branches and evaluator coverage remain available for specialist inspection; this baseline does not claim exhaustive validation of them.

## Shared records

### Components

#### RT-CMP-generation-model
Label: Configured generation model

The source-native generation component is the provider/model selected through `createModel`, `resolveEffectiveLLMConfig` and `generateObjectSafe`. Representational form: distributed-parametric model, consumed through natural-language prompts and structured response schemas. Storage substrate: external provider service, local Ollama installation or separately installed CLI model; provider internals are uninspected. CM stores configuration, not model weights (SRC-1: `src/llm.ts`).

Parameters changing during operation: no parameter-update operation is exposed in the inspected CM generation path; actual provider-side parameter changes are uninspected. Exact version pinned: no immutable weight/version identity is established by the configured model string. Mutable endpoint resolving to another model: possible through configured base URLs, CLI resolution and automatic provider/model fallback. An explicit model name alone does not remove this uncertainty.

> return { ...config, provider: fallback, model: FALLBACK_MODELS[fallback] };
> --- `src/llm.ts`

The SDK path constructs provider models and structured calls; the CLI path pipes an enhanced prompt to a subprocess, parses response JSON, validates schema and retries failures. Retry feedback can request JSON self-correction, not independently verify factual validity. CM does not demonstrate online weight learning here.

#### RT-CMP-embedding-model
Label: Semantic embedding model

Source-native identity: embedding backend `xenova` or `ollama`, default Xenova model `Xenova/all-MiniLM-L6-v2`. Representational form: distributed-parametric encoder and dense numerical outputs. Storage substrate: transformer model cache or external Ollama service; embeddings are cached numerical data used for similarity, not generation instructions (SRC-1: `src/semantic.ts`).

> export const DEFAULT_EMBEDDING_MODEL = "Xenova/all-MiniLM-L6-v2";
> --- `src/semantic.ts`

Parameters changing during operation: inspected operations perform inference/cache updates, not training; external service mutation remains uninspected. Exact version pinned: a name/tag is supplied, but no immutable weight revision is established in these calls. Mutable endpoint resolving to another model: Ollama configuration can change base URL/model; model cache/download provenance is not an immutable provider guarantee. Semantic failure falls back to lexical retrieval, so this component is not mandatory for a context return (SRC-1: `src/semantic.ts`, `src/commands/context.ts`).

### Operative objects

#### RT-OBJ-playbook-bullet
Label: Playbook bullet instruction content

Source-native identity: each `PlaybookBullet`'s `id` and `content`. Representational form here is the natural-language instruction content interpreted by a reflector or later agent. Storage substrate: global or repository YAML playbook. Symbolic feedback, state and scoring fields are surrounding control metadata, not the instruction's linguistic meaning; numerical embeddings are separately described above. This record identifies the runtime consumption part, leaving detailed memory-part records to the specialist (SRC-1: `src/playbook.ts`, `src/reflect.ts`, `src/commands/context.ts`).

> output += `- [${b.id}] ${maturity} ${b.content} (${b.helpfulCount}+ / ${b.harmfulCount}-)\n`;
> --- `src/reflect.ts`

The reflector receives content with IDs and counts. Context returns a compact projection; it does not return the full feedback log or source-session array. Text is therefore available as guidance, not a mandatory action rule enforced by CM.

#### RT-OBJ-reflector-prompt
Label: Shipped reflector method text

Source-native identity: `PROMPTS.reflector`. Representational form: natural-language method instructions with symbolic delta shapes. Storage substrate: shipped TypeScript template; interpolated diary/playbook/history fields form each invocation's prompt. The method requests specific, reusable deltas and lists allowed change kinds. It is static shipped guidance, not evidence of a method revised through use (SRC-1: `src/llm.ts`).

> - REUSABLE: Would help a DIFFERENT agent on a similar problem
> --- `src/llm.ts`

### Routes

#### RT-RTE-context-read
Label: Task-directed context read

Endpoints: caller task/workspace → merged playbooks and cass search → selected context result. Owner: deterministic generator/selector; the caller owns the next task action. Context/state: task keywords, configured ranking policy, active bullets, optional embeddings and history hits. Effects: returning guidance; optional context log. No foreground-agent command is executed by the result itself (SRC-1: `src/commands/context.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON/text context with selected rules, anti-patterns, bounded history, warnings, search pointers and retrieval mode/statistics.
- Later read-back: previously retained playbooks and cass history are reloaded for each request; optional delivery logs can support outcome matching, not proof of compliance.
- Delegated visibility: external CLI/MCP callers receive the projection; source-session arrays, embeddings and feedback logs are not included in context bullets.
- Selection predicate: workspace applicability and active state, lexical/optional semantic relevance, effective score ranking, absolute/relative relevance floors, count and estimated token limits.
- Invalidation or expiry: later requests reload current playbooks; retirement/deprecation and score changes affect selection. Omitted material stays reachable in storage.
- Activation or effect: CM constructs guidance and warnings; changed behavior of the enclosing agent is uninspected.
- Evidence limits: source wiring only; no caller trace or retrieval-quality result was supplied.

Decision roles: caller supplies problem; code decides selection; caller can ignore it. Operating mode: open task requests, not a curriculum or controlled experiment. Answer oracle: inapplicable — retrieval has no supplied expected answer; rank scores are not truth judgments. Working-context control is selective external-material delivery, not host conversation pruning.

> if (tokenBudget > 0 && selected.length > 0 && estimatedTokens + cost > tokenBudget) {
> --- `src/commands/context.ts`

This condition is the forcing witness for approximate, non-hard budget coverage. The first relevant bullet survives even if too large.

#### RT-RTE-reflection-update
Label: Session reflection admission

Endpoints: explicit/discovered transcript → export → diary → model deltas → validation/curation → durable playbooks and processed log. Principal: CLI/MCP caller or host session-end hook, running with CM's OS credentials. Owner: orchestrator controls progression; generation model proposes; validation and curator code decide admission. No per-delta human approval is wired into this driver (SRC-1: `src/orchestrator.ts`, `src/reflect.ts`, `src/validate.ts`, `src/curate.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reflection outcome with processed-session/delta counts, merge results and errors; detached session-end initiation instead returns a PID before this outcome exists, while wait mode returns child exit status.
- Later read-back: saved rule changes reach later context and reflection calls; diaries and processed-session state persist for later readers/recovery.
- Delegated visibility: generation sees summarized diary, formatted bullets and selected related history; CLI subprocess receives a constructed prompt and returns structured JSON, not an unrestricted copy of all CM state by this interface.
- Selection predicate: explicit session or unprocessed discovery, growth/watermark and retry eligibility, self-generated-session exclusions, schema-normalized/deduplicated deltas, configured validation branches and curator required-field/duplicate checks; curator conflict warnings do not filter admission.
- Invalidation or expiry: processed marks suppress unchanged work; growth reopens incremental work; forced full passes avoid double grading; curation can replace, merge or retire rules.
- Activation or effect: admitted deltas change durable playbooks; later retrieval is wired, but external-agent behavioral activation and benefit are uninspected.
- Evidence limits: source only; incomplete/missing external transcripts and opaque model judgment prevent correctness and exhaustive historical-coverage conclusions.

Admission account: trigger is explicit reflection or discovered work, including installed host callbacks. Proposed changes are add/helpful/harmful/replace/deprecate/merge deltas. Guidance is the shipped reflector method applied to session summaries and existing rules. Validation can reject adds. Curator rejects an add missing content or category, and its duplicate branches can suppress a new addition or reinforce an existing target rule. In particular, deprecated exact/similar matches and matches only in another playbook layer can skip an addition. These are required-field and duplicate controls, not contradiction-based vetoes: detected conflicts are appended to warnings and logged with action `skipped`, but execution continues to duplicate checks and can reach `addBullet`. Directive disagreement excludes a rule from both lexical and embedding duplicate matching, preserving contrary advice as distinct rather than rejecting it. Starting the run is not human approval of content. Rollback/recovery: individual files are atomically saved under locks; failed sessions remain retryable, with errors and failure bookkeeping; merge/log/outcome stages are not one transaction. Other-repository write failures can fall back to workspace-scoped global storage (SRC-1: `src/orchestrator.ts`, `src/playbook.ts`).

Curator enforcement witnesses (SRC-1: `src/curate.ts`, inspected add progression and both duplicate helpers):

> if (!delta.bullet?.content || !delta.bullet?.category) {
>           logDecision(decisionLog, "add", "rejected", "Missing required content or category", {
>             content: delta.bullet?.content?.slice(0, 100),
>           });
>           break;
>         }
> --- `src/curate.ts`

> // Conflict detection (warnings only)
> --- `src/curate.ts`

> logDecision(decisionLog, "conflict", "skipped", c.reason, {
>             content: content.slice(0, 100),
>             bulletId: c.id,
>             details: { conflictingContent: c.content.slice(0, 100) },
>           });
> --- `src/curate.ts`

The conflict loop has no rejection exit. The subsequent new-add branch calls `addBullet` and records acceptance if no duplicate branch intervenes. The log action therefore does not describe the candidate's admission disposition.

> applied = true;
>         logDecision(decisionLog, "add", "accepted", "New bullet added to playbook", {
> --- `src/curate.ts`

> // Final log save - only mark processed AFTER rules are persisted
> --- `src/orchestrator.ts`

> if (delta.type !== "add") {
> --- `src/validate.ts`

> if (gate.suggestedState === "draft" && gate.successCount === 0) {
> --- `src/validate.ts`

Decision roles: model proposes wording and feedback; code/schema/evidence gate/optional validator and curator required-field/duplicate branches decide acceptance, while curator conflict detection supplies warnings only; operator can configure validation or later edit state, but human identity and per-content veto are unresolved for generic callers. Answer oracle: no expected answer supplied. Historical snippets and success/failure regex counts are evidence heuristics; model verdicts are judgments. Operating mode: open session-driven maintenance with bounded model iterations, not a causal experiment. `CASS_MEMORY_LLM=none` is a configured no-reflection branch; reflector stub environment inputs are another bypass used by source test harnesses, not ordinary model execution (SRC-1: `src/reflect.ts`, `src/validate.ts`).

Theory account: rule units can formulate conditional guidance. Existing rules shape model proposals; harmful/replace/deprecate requests can direct criticism toward a named rule, but requesting that criticism does not establish its occurrence or reliability. The method prompt stays fixed while persisted rules/feedback change. Theory-builder conditions 1–4: condition 1 implementation conclusion status: afforded — whole rule content is addressable by ID, but actual corpus theory content was not supplied; condition 2 conclusion status: claimed — the prompt asks the model to judge existing rules by their content; supplying text is wired, but actual semantic dependence and downstream-agent dependence are uninspected; condition 3 conclusion status: claimed — harmful/replace/deprecate requests invite content-directed judgment, but no criticism trace shows claim/result/blame/revision; condition 4 conclusion status: uninspected — saved changes reach later prompts, but no retained criticism and next-round dependency was observed. Within-run reflector iterations reuse the same formatted existing bullets and deduplicate proposals; this alone is not iterative criticism.

Addressability: whole bullets can be inspected/replaced by ID; finer assumption decomposition is not established. Persistence: rule content/feedback across sessions; the detailed retention of rationale is left to memory analysis. Learning: later behavioral influence is afforded through persistence/retrieval, improved capacity and attribution are uninspected. Reflection: session aspects and rule feedback have an implemented representation/update/return path, but CM is not thereby shown to revise its own method. Reflective theory builder and autonomous theory builder: uninspected — no evidence that every criticism/iteration condition, or criticism of the method against its own operation, was exercised. This is not an inference that these behaviors are absent.

#### RT-RTE-onboard-add
Label: Caller-assisted onboarding and add

Endpoints: selected historical sessions and extraction instructions → external caller's formulated rules → playbook add → saved YAML. Owner: CM supplies selection/protocol and performs I/O; caller owns semantic extraction. Source-native instructions tell the agent to seek successful/problematic patterns, formulate contextual imperative rules and invoke batch/single add (SRC-1: `src/commands/onboard.ts`, `src/commands/playbook.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: onboarding status/session/prompt data, then add results including bullet IDs or validation failures when invoked.
- Later read-back: saved additions enter later playbook reloads; supplied session provenance can mark onboarding work processed.
- Delegated visibility: calling agent receives exported session material and method text; CM receives resulting rule text/file, not proof of the caller's reasoning.
- Selection predicate: unprocessed session and gap-related sampling for onboarding; user-specified single content or batch file for add; optional quality/similarity/category checks.
- Invalidation or expiry: onboarding progress suppresses already-processed sessions unless requested otherwise; rule retirement and later edits affect consumption.
- Activation or effect: successful add persists caller-supplied instruction content; later compliance is uninspected.
- Evidence limits: caller may be a human or computational agent; starting onboarding establishes neither per-rule human approval nor faithful session analysis.

Admission account: trigger is caller-selected onboarding or manual add. Caller proposes content guided by extraction text; software accepts into a selected global/repo target. `--check` requests validation; `--strict` can veto on issues inside that branch. Omitting strict can add despite warnings; this is not the reflection historical evidence gate. Recovery is file-level saving/explicit later correction, not an inspected automatic semantic rollback. Operating mode: open guided extraction. Answer oracle: inapplicable — no expected correct rule supplied (SRC-1: `src/commands/playbook.ts`).

> // Validate if --check flag is set
> --- `src/commands/playbook.ts:1057-1057`

> "Or omit --strict to add anyway.",
> --- `src/commands/playbook.ts`

This route also admits natural-language guidance, but CM does not inspect the external caller's theory-building operations. Formulation/criticism/iteration of theories by that caller remain uninspected rather than attributed to CM.

#### RT-RTE-feedback-update
Label: Direct rule feedback update

Endpoints: rule ID plus helpful/harmful flag → target playbook reload under lock → feedback event/count/maturity update → saved file. Owner: `recordFeedback` executes the update; caller supplies the judgment. Repo playbook is tried before global. Unknown IDs fail instead of fabricating a target (SRC-1: `src/commands/mark.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: feedback type, effective score and resulting maturity state, or an error.
- Later read-back: saved events/counts and maturity affect later scoring and selection.
- Delegated visibility: caller sees result metadata, not an independently verified outcome or explanation of its own judgment.
- Selection predicate: exact bullet ID and exactly one helpful/harmful flag; repository target first, then global.
- Invalidation or expiry: time-sensitive scoring and subsequent events can alter influence; harmful maturity transition can set retired/deprecated state.
- Activation or effect: code changes scores/state and can retire a rule; external task impact remains uninspected.
- Evidence limits: feedback labels can be asserted without an outcome trace; causality and truthful attribution are not established.

Admission account: trigger is explicit mark or MCP feedback; proposal is an outcome judgment, optionally reason/session context; software admits the event and computes maturity. Invalid flags/unknown IDs veto. Caller identity does not resolve human control. Recovery is subsequent maintenance, not a demonstrated undo transaction. Operating mode: open feedback. Answer oracle: none supplied; caller labels are not verified expected outcomes. This route changes reliance without requiring text revision, but counts alone do not establish content-directed criticism.

> targetBullet.feedbackEvents.push(event);
> --- `src/commands/mark.ts`

#### RT-RTE-http-tools
Label: HTTP tool dispatch

Endpoints: HTTP POST JSON-RPC request → configured-token check → argument validation/tool dispatch → shared generator or mutation driver → MCP content response. Owner: server/admission controller; principal: requesting client with token when configured. Tools include context, feedback, outcomes, search and reflection; resources expose retained state. This is not a separate agent planner (SRC-1: `src/commands/serve.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON-RPC result wrapped as MCP content or validation/execution/busy error.
- Later read-back: context/search/resource reads expose existing retained data; mutation tools invoke the same durable feedback/reflection paths described separately.
- Delegated visibility: remote/local client receives requested tool/resource data; grants are not subdivided into inspected per-tool roles.
- Selection predicate: POST method, configured token match, named tool/resource and validated arguments; cass-backed work additionally passes bounded admission control.
- Invalidation or expiry: per-request state reloads follow shared implementations; pending cass work can receive a retryable busy response.
- Activation or effect: dispatch permits reads and explicitly requested writes; enclosing-agent action depends on the external client.
- Evidence limits: no deployed network, token, client grant set or host compliance supplied.

Admission of content uses the delegated driver, not HTTP authentication as content approval. Operator chooses exposure/token; a credentialed requester can invoke advertised mutation tools. Operating mode: open service requests; answer oracle: inapplicable — dispatch validates requests, not task answers. Required external contract: OS/network confinement for unauthenticated loopback deployments and client safeguarding of credentials.

> if (!loopback && !token && !allowInsecureNoToken) {
> --- `src/commands/serve.ts`

This bind policy explicitly permits an unsafe override and does not cover CLI/file paths.

#### RT-RTE-trauma-guard
Label: Retained trauma guard consumption

Endpoints: active global/project trauma entries → generated Python hook → host command or staged-diff check → host denial/commit failure or allow. Owner: installed hook for matching; enclosing host/Git for honoring its result. Retained natural-language human messages supply the explanation, while regex patterns and fixed matching logic form the symbolic control part (SRC-1: `src/trauma_guard_script.ts`, `src/commands/guard.ts`, `src/trauma.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: pre-tool deny JSON on a match, otherwise successful exit without denial; Git variant returns nonzero on a staged-content match.
- Later read-back: each invocation reloads active persisted trauma entries.
- Delegated visibility: host receives pattern/reason/reference/ID; Git caller receives the match report.
- Selection predicate: active stored entries with usable regex; pre-tool path only checks nonempty Bash command strings, while Git variant checks staged changed lines.
- Invalidation or expiry: healed/inactive entries no longer match active-entry loading; invalid regex is skipped and storage errors can fail open.
- Activation or effect: wired denial signal/exit status; actual prevention depends on installation and host enforcement, both uninspected.
- Evidence limits: not a general sandbox, not protection for every shell/tool/subprocess route, and no safety outcome evidence.

> if tool_name != "Bash" or not isinstance(command, str) or not command:
> --- `src/trauma_guard_script.ts`

> "permissionDecision": "deny",
> --- `src/trauma_guard_script.ts`

The channel's force is conditional host enforcement, unlike the advisory context route. Healing/changing trauma state is a distinct maintenance admission; no human approval or safety effectiveness should be inferred solely from regex storage.

### Claims

#### RT-CLM-automatic-learning
Label: Agent protocol automatic learning claim

The shipped skill's end-of-work instruction claims automatic learning. It is doctrine/design, not an observed deployment result. Hook installation, delivery, model availability and successful admissions condition the mechanism; configured LLM-free mode and detached-start return prevent equating session completion with useful learning (SRC-1: `SKILL.md`, `src/commands/hook.ts`, `src/reflect.ts`).

> 4. END:      Just finish. Learning happens automatically.
> --- `SKILL.md`

#### RT-CLM-rule-criticism
Label: Reflector rule criticism request

The reflector asks for rule-specific harmful/replace/deprecate changes. It establishes a prompt affordance for criticism, not a trace showing the challenged claim, result, blame and revision. Its force is model instruction, with downstream schema/curation restrictions (SRC-1: `src/llm.ts`).

> - harmful: Existing bullet caused problems (reference by ID, explain why)
> --- `src/llm.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-rule-guidance
Label: Rule text to model guidance

Consumer: CM reflector or external coding agent. Channel: interpolated reflector prompt or returned context payload. Force: natural-language guidance interpreted by the model, not a CM-enforced obligation to act. Horizon: retained playbooks can influence subsequent sessions; prompt text is current-call input. Update-consumer visibility is wired; external-agent activation is uninspected. Evidence: SRC-1 `src/reflect.ts`, `src/llm.ts`, `src/commands/context.ts`; [RT-OBJ-playbook-bullet](#rt-obj-playbook-bullet) retains the formatting witness. Delivery alone does not prove decisions depended on the rule.

#### RT-BAP-guard-denial
Label: Trauma pattern to host denial

Consumer: generated Python matcher, then enclosing host/Git. Channel: persisted active regex entries, PreToolUse JSON or Git exit status. Force: symbolic matcher produces a deny signal or failed commit; effective command prevention requires the host to honor the installed hook. Horizon: repeated future matching while active, until healing or other state changes. Evidence: SRC-1 `src/trauma_guard_script.ts`; [RT-RTE-trauma-guard](#rt-rte-trauma-guard) retains the matching/denial witnesses. This channel has stronger intended force than returned advice, but its deployment guarantee is uninspected.

## Annotations

none
