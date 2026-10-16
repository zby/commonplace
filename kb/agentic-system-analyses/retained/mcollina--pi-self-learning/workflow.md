---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "pi-self-learning workflow: completed-task reflection through parsing, memory persistence and later foreground-context delivery."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
---

# pi-self-learning workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is automatic completed-task reflection, followed by delivery of retained material to a later foreground invocation. It was selected because it connects the package's central producer to its later consumer in one implemented path, rather than joining unrelated commands. The delivered result within this extension's boundary is memory text and consultation guidance, not the user's completed coding product. The enclosing host owns that product, its tool loop and the final answer.

This account independently inspected SRC-1, `extensions/self-learning.ts`, particularly `parseReflection`, `parseReflectionWithFallback`, `buildReflectionRepairPrompt`, `updateCoreFromReflection`, `buildMemoryContextBundle`, `buildMemoryInstruction`, `reflectNow`, and the event/manual handlers. These supply implementation and embedded doctrine/design at the [frozen boundary](boundary.md). They extend detail within an already registered file, not the source boundary. No target execution, generated reflection or downstream answer is supplied. Thus the workflow is wired, not observed to complete or prevent mistakes. Existing runtime records identify its mechanisms; no duplicate workflow records are declared.

### Trigger, delegation and return

1. **The host hands off a completed-event notification, not a verified task outcome.** `agent_end` supplies messages and host context. Extension code loads settings and branch enablement, requires automatic reflection to be enabled, tests the latest assistant's stop reason, and checks the redistill suppression deadline. This gates entry to [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection); it does not establish that tests passed or the user's request was satisfied. The host remains owner of the original task.

2. **The extension delegates a bounded reflection request to a completion model.** `reflectNow` selects recent branch messages after recognized abort filtering, serializes them through host functions, and collects bounded permission/blocking signals. It chooses an authenticated configured model or, at selection time, the current host model. The chosen [RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model) receives one user message containing the embedded mistake/fix instructions, selected conversation and execution signals. It does not receive the complete foreground system prompt, existing memory files or a tool interface. This is a separate completion request, not a child coding agent with delegated task execution. Extension code owns the next step after the response (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

3. **The model proposes content; code decides structural admission.** Text response extraction is followed by direct JSON parsing or first-object extraction. Parsing trims string list members and accepts either a nonempty mistakes list or a nonempty fixes list, including older output keys. The prompt asks for mistake-prevention content, but the admission check does not compare it with an expected answer, validate the diagnosis, or enforce the requested maximum number of learnings. No person approves each reflection. Consequently a well-formed but inaccurate rule can pass this gate (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

4. **The extension persists the admitted result and returns a path.** It builds a dated Markdown entry, resolves the memory root, prepares optional Git support, appends the daily entry, and updates the scored index and rendered files. Fixes enter as learnings; mistakes become `Avoid:` items. Equal normalized keys update hits, timestamps and score rather than retaining separate index records. Core, long-term and index writes precede the commit attempt. This is software/model admission into retained memory, not human content approval. Finally the extension records at most 180 characters from the first mistake or fix in process-local notes and returns the daily path. The hook reports that path when UI is available. The path acknowledgment does not establish successful Git history or semantic quality (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes)).

### Rejection, repair and recovery

The workflow has a concrete rejection branch before memory writes. Disabled learning, missing/empty branch input or absent usable model/auth returns a skip reason. Empty model text also returns without reflection persistence. Nonempty but unparsable output triggers one repair completion using the same model/auth. Unlike the first proposal, repair receives compacted raw output and a JSON conversion instruction, not the original selected conversation. The conversion request is explicit:

> "Convert the following model output into STRICT JSON only.",
> "Return exactly one JSON object with this schema:",
> '{"mistakes":["..."],"fixes":["..."]}',
> --- `extensions/self-learning.ts`

Repair can recover syntax; this handoff does not independently re-ground the proposed lesson in the session. If repair is empty or still invalid, `reflectNow` returns `invalid_model_output` plus previews and diagnostics before daily/index/render writes. This is a rejection of structure, not an adverse correctness judgment (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

Extension code, not another worker or a human reviewer, schedules this single recovery attempt. Automatic invocation does not report skip reasons and swallows exceptions inside its protected body. It neither retries the whole workflow nor rolls back partial filesystem effects. A failure after the daily append may therefore leave the daily entry without all derived updates. Optional Git is best-effort history, not an automatic restore mechanism. Configuration access before the protected body and cleanup are outside the catch's blanket scope. Timeouts bound the extension's wait but do not establish provider cancellation (SRC-1, `extensions/self-learning.ts`; runtime recovery account and [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

The shipped manual alternative `/learning-now` makes the same reflection function available with diagnostic reporting, including initial and repair previews after invalid output. A user can invoke it again, but it is a new reflection attempt, not a transactional resume. It bypasses automatic completion and suppression gates while retaining `reflectNow`'s enabled/input checks. This alternate path is therefore not evidence that all reflection admissions followed a completed-task event (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

### Later delivery and its terminal boundary

On a later `before_agent_start`, [RT-RTE-context-injection](runtime.md#rt-rte-context-injection) independently reloads settings and checks learning enablement. It selects a tail of process-local notes. When file context is enabled, it also reads configured core, recent daily and latest monthly material into a character-bounded bundle. Core is placed before daily and monthly text; per-file and aggregate prefix truncation can omit content. There is no semantic match to the new request, and persistence does not guarantee every reflection reaches the consumer. Long-term memory is named in consultation guidance rather than automatically bundled (SRC-1, `extensions/self-learning.ts`).

The hook returns a hidden custom message with selected text and an optionally augmented system prompt. These fields are the extension's terminal delivery interface, not evidence of host application or model compliance. The host/model becomes the next-step owner. [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) establishes that even strict consultation is a model-interpreted request, not a read-verifying or answer-rejecting gate. The source does not close the workflow with a check that a lesson was used, a regression avoided, or a better final answer produced. The implemented producer-to-consumer connection is established; exercised learning benefit remains uninspected.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)

Workflow role: producer and local recovery boundary. The foreground host hands control to extension code; the completion model proposes reflection text; code alone parses, optionally requests one repair, and admits the result. The success return follows memory writes, whereas an invalid-output return precedes them. No end-to-end transaction spans daily append, derived-file writes and Git. Manual diagnostic visibility differs from automatic silence, without adding a semantic verifier.

#### On [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Workflow role: later delivery boundary, not acknowledgment of successful use. This is a separate host hook, with fresh settings and selection, rather than a continuation awaited by the producer. The producer does not receive feedback that the host consumed the retained result. What crosses this handoff is selected text plus path-oriented guidance, not the complete retained index or a verified behavioral change.
