---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MCMA-OpenMemory workflow: browser question through deterministic recall, optional generation, capture, delivery and archive-based interruption recovery."
run-id: AAS-2026-11-08-mcma-openmemory-a023f4989e1c-01
reviewed-boundary: "556954d95f0d6d6894c5d46ffcc25a907150b0a7"
---

# MCMA-OpenMemory workflow report

## Workflow account

### Selection and evidence

This account selects the shipped browser question workflow, following an ordinary question that needs generation and then checking interruption recovery. It connects request identity, retrieval decisions, bounded context, provider delegation, durable capture and delivery in one implemented path. Direct recall is an earlier terminal branch, not a separate agent workflow assembled from unrelated features. The system's agents here are deterministic PHP service roles; the model receives a generation request, not responsibility for scheduling successors. See [RT-RTE-web-request](runtime.md#rt-rte-web-request) and [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer).

All source findings use SRC-1 at the frozen revision in [boundary.md](boundary.md). Added implementation inspection covers the browser's pending-request, submission, result-rendering and recovery functions in `apps/web/public/app.js`; ask dispatch, request lookup, archive reconstruction and persistence helpers in `packages/core/src/Web/WebApplication.php`; request lookup in `packages/core/src/Interaction/InteractionArchiveService.php`; and generation/context/capture progression in `packages/core/src/Ask/AskService.php`. These are source-text observations, not observed executions. No target code, test or example was run. The account establishes wiring, not successful recovery, correctness of generated answers or benefit from retained context.

### Request, service delegation and decision ownership

1. **The browser supplies a stable request identity.** On submission it creates a random request ID, obtains the conversation ID, and stores both with the question and timestamp in sessionStorage before sending the POST. The request also carries current/remember flags, response language and any selected mutation reference. This browser state is a recovery pointer and original question, not a saved answer. Storage exceptions are swallowed, so retention of the pointer is best effort. SRC-1, `apps/web/public/app.js`; [WF-RTE-request-recovery](#wf-rte-request-recovery).

2. **The web service admits and dispatches the request.** It checks origin, resolves the principal and user library, bounds the question, validates IDs and language, then looks for an archived request before doing more work. An existing interaction returns immediately. Mutation/save syntax intercepts before ordinary asking; this account follows neither intercept. Consequently an ordinary question is not a delegated edit request. PHP constructs the services and owns the next step. The billing-enabled branch uses BillableAskService; the other branch still wraps configured providers for metering. The service handoff supplies the question, ai role, thresholds, capture options, conversation ID and response language. See [RT-RTE-web-request](runtime.md#rt-rte-web-request), [RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture) and [RT-RTE-memory-mutation](runtime.md#rt-rte-memory-mutation). SRC-1, `packages/core/src/Web/WebApplication.php`.

3. **PHP tries retained answers before generation.** Broad canonical recall, when requested and satisfied, returns directly. Otherwise ordinary exact knowledge reuse precedes semantic retrieval. The exact/semantic paths assess validation, confidence and freshness; semantic selection also applies similarity or configured rerank thresholds. These are eligibility decisions, not factual verification against an answer oracle. Broad recall has a separate canonical policy and does not receive currentRequired, so current=true is not a universal demand for generation or external research. If no generator is configured after recall fails, AskService returns provider-required instead of an invented answer. These branches and limits belong to [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer). SRC-1, `packages/core/src/Ask/AskService.php`.

4. **Builders select the material visible to the generator.** For the chosen generation branch, code reuses the semantic candidate pool for multi-memory context; if that builder fails, it attempts single-memory context instead. Conversation and broad-recall builder failures are logged and leave their respective context null. PHP passes only non-null assembled contexts, the question and request metadata to generate. The provider does not receive a Library handle or an isolated subagent task frame. The builders select, clip and reload durable content rather than compact an ongoing autonomous agent's live window. Their budgets do not bound the complete provider prompt. See [RT-RTE-context-supply](runtime.md#rt-rte-context-supply). The connectors' instruction to treat memories as untrusted references is policy requiring model cooperation, not an enforced guarantee of compliance: [RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference). SRC-1, `packages/core/src/Ask/AskService.php`.

### Acceptance, persistence and delivery

5. **Generation has a minimal output gate, not an independent answer judge.** AskService calls the configured provider once in this progression, trims its text and rejects an empty answer. This does not check whether the answer is true, follows the reference-data policy or preserves uncertainty. No model-selected retry or revision cycle is established by this path. SRC-1, `packages/core/src/Ask/AskService.php`:

> $generated = $this->generationProvider->generate($question, $generationContext);
> $text = trim((string)($generated['text'] ?? ''));
> if ($text === '') throw new RuntimeException('Generation provider returned an empty answer');
> --- `packages/core/src/Ask/AskService.php`

6. **Capture is a separate software admission decision.** With remember enabled, no existing exact record and a Librarian, code submits generated text with provenance and configured freshness/reuse metadata. Default capture is unverified/0.5, not promotion to trusted knowledge. Existing exact records are preserved even if stale, disputed or unverified; generation alone is not authority to overwrite them. The model proposes answer text, PHP decides capture eligibility, and Librarian performs the write. There is no per-answer human approval in this step. See [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer). Later approval/discard is a distinct owner-facing route, not a prerequisite to delivery: [RT-RTE-interaction-approval](runtime.md#rt-rte-interaction-approval). SRC-1, `packages/core/src/Ask/AskService.php`.

7. **Answer return, knowledge capture and conversation archiving are different outcomes.** After AskService returns, the web attempts a context trace and interaction archive even when remember=false. Those helpers catch persistence errors; they do not retract a successful answer. JSON return is the server delivery boundary. In the browser, applyChatResult renders answer.value (or the serialized result if absent), updates metadata and distinguishes an archived response from a response without persistent-archive confirmation. Thus an answer can be delivered without the archive needed for later recovery. See [RT-RTE-web-request](runtime.md#rt-rte-web-request). SRC-1, `packages/core/src/Web/WebApplication.php`, `apps/web/public/app.js`:

> }else{
>       composerStatus.textContent='Respuesta recibida, pero el archivo persistente no confirmó esta interacción.';
>     }
> --- `apps/web/public/app.js`

### Failure and recovery

The supported interruption branch does not blindly repeat generation. A POST error with no status, or a 502–504 status without an application error code, causes browser polling of the request lookup endpoint. The endpoint asks the archive for that conversation/request pair; it does not resume a suspended provider call. A missing archived record yields pending, which does not prove the original computation is still running. Successful lookup reconstructs an answer and selected metadata, not the whole original result. Details and minimum evidence are retained in [WF-RTE-request-recovery](#wf-rte-request-recovery).

Recovery ownership is split: the server archives and exposes lookup; the browser decides whether to poll, retain a pending pointer or show a permanent error. Authorization/invalid-input errors during polling are rethrown. Exhausted transient recovery leaves the pointer for another lookup on session initialization. Other errors clear it. Empty generation is a rejection path, not a command to regenerate automatically. Archive failure can make a previously delivered answer unrecoverable through this lookup; concurrent duplicate requests are not proven exactly-once by an initial archive check. No source execution evidence shows any of these failure paths succeeding in deployment.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-request-recovery
Label: Browser request recovery

Part of: [RT-RTE-web-request](runtime.md#rt-rte-web-request)

This is the material interruption/lookup subroute of the supplied web request record, not a replacement web invocation or duplicate archive object. Endpoints are browser submission state, session-authorized GET request lookup, indexed archive read and browser result rendering. JavaScript decides polling; PHP decides lookup/reconstruction. SRC-1 implementation, `apps/web/public/app.js`, `packages/core/src/Web/WebApplication.php`, `packages/core/src/Interaction/InteractionArchiveService.php`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lookup returns 202/pending when no interaction is found, or completed with a reconstructed result. Browser renders a recovered answer through applyChatResult or reloads the stored conversation after startup recovery.
- Later read-back: sessionStorage retains request/conversation/question/timestamp for startup lookup; the server rereads durable interactions via the conversation index and matching request suffix. It does not regenerate an answer during GET recovery.
- Delegated visibility: Browser receives reconstructed answer, route, provider/billing/stored fields and archive metadata. resultFromArchivedInteraction does not restore original context_used, context_trace, memory_attempt or all canonical-reference fields returned by other routes. Recovery is answer delivery, not a full replay of decision evidence.
- Selection predicate: Submission recovery follows a missing HTTP status or a 502–504 without an application error code. Polls default to 45 attempts with two-second sleeps; startup recovery uses 15. Server validates conversation ID and reads the session principal's library, then matches request ID within that conversation.
- Invalidation or expiry: Successful application clears the pending pointer. Ordinary failure clears it; polling exhaustion retains it through the specific keep-pending error path. No age-based expiry test is implemented in the inspected pending-state functions despite the stored timestamp. SessionStorage persistence remains browser/session dependent.
- Activation or effect: Successful lookup supplies archived answer content without a new POST or model call in this recovery subroute. Pending means lookup found no archive entry, not a verified server execution state. A separate repeated POST can short-circuit on an existing archive, but no exactly-once concurrency guarantee follows.
- Evidence limits: No observed network interruption, successful archive lookup or billing outcome is supplied. Archive discovery depends on the conversation index; absence there is not proof that no ciphertext was ever written. Polling is bounded, authorization can fail, and best-effort archive/pointer persistence can prevent recovery.

The browser's transient predicate and handoff are explicit:

> const transient=(!error.status)||(error.status>=502&&error.status<=504&&!error.code);
>         if(!transient)throw error;
> --- `apps/web/public/app.js`

> result=await recoverRequest(requestId,conversationId,45);
> --- `apps/web/public/app.js`

Polling accepts completed results and stops on selected admission failures:

> if(data.status==='completed'&&data.result)return data.result;
>       }catch(error){
>         if(error.status===401||error.status===403||error.status===400)throw error;
> --- `apps/web/public/app.js`

Server pending is an archive lookup result, not a job-status database:

> if($interaction===null){
>                 return HttpResponse::json([
>                     'ok'=>true,'status'=>'pending','request_id'=>$m[1],'conversation_id'=>$conversationId,
>                 ],202);
>             }
> --- `packages/core/src/Web/WebApplication.php`

The archive lookup depends on the conversation index before it reads an interaction:

> $conversation=$index['conversations'][$conversationId]??null;
>         if(!is_array($conversation)) return null;
>         foreach($conversation['interaction_refs']??[] as $logicalRef){
>             if(!is_string($logicalRef)||!str_ends_with($logicalRef,'/'.$requestId)) continue;
> --- `packages/core/src/Interaction/InteractionArchiveService.php`

Guarantee strength is best effort: browser polling avoids a new model request in this subroute, but cannot guarantee archival completion or recovery. This is an open-request transport recovery mode, not candidate comparison or an improvement experiment; no answer oracle or new product/knowledge admission occurs in GET lookup.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
