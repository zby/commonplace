---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Claude Code dynamic workflows memory: session-result replay, reusable scripts, prefix caching and isolated working context."
run-id: AAS-2026-10-14-workflows-f9c2f80a3a94-01
source-identity: "https://code.claude.com/docs/en/workflows"
reviewed-boundary: "workflows-2026-10-14"
---

# Claude Code dynamic workflows memory report

## Boundary and evidence

The subject is the documented workflow subsystem, not Claude Code's general memory system. I directly read all of SRC-1, the frozen 506-line `workflows-2026-10-14.md` capture, and compared it with the supplied runtime member. All positive mechanisms are doctrine/design contracts. Implementation and operation remain uninspected. The [boundary](boundary.md) registers the exact capture and excludes linked documentation, executable bundled/saved/plugin scripts, provider internals and enclosing session implementation.

Included surfaces are saved worker results, run and reusable scripts, prompt-prefix caching, launch/settings persistence, progress displays, final-result selection and retry context loss. General session compaction, external file versioning, provider training and worker context construction cannot be established from this page. The capture supplies no CLI implementation, hook implementation, tool registration code or service/library implementation to inspect; its documented commands and Workflow permission alternatives are included instead.

| Entry point or operation | Direct source scope in SRC-1 | Records and coverage limit |
| --- | --- | --- |
| `agent()`, `pipeline()`, `parallel()` and final return | `What the saved script looks like`; `How a workflow runs` | [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration), [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results); isolated variables and example filtering inspected; complete worker context unknown |
| Save, edit, `/reload-skills`, named project/personal/plugin commands, `args` | `Save the workflow for reuse`; `Distribute a workflow in a plugin`; `Pass input to a saved workflow`; `Edit a saved script` | [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script), [RT-RTE-script-admission](runtime.md#rt-rte-script-admission); actual scripts, plugin admission and authoring reference excluded |
| Pause, stop, relaunch, background, local resume and cloud reopening | `Manage runs`; `Resume after a pause`; `Resume after you leave the session` | [RT-RTE-run-replay](runtime.md#rt-rte-run-replay); ordered-prefix reuse and both persistence substrates covered; encoding and cleanup unknown |
| Stall/manual restart and usage-limit handling | `When an agent stalls and restarts`; `When a run hits your usage limit` | [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery); transcript discarded but edits retained; usage-wait restart context unspecified |
| Shared prompt prefix | `Prompt caching in a fan-out` | [MEM-OBJ-prompt-cache](#mem-obj-prompt-cache), [MEM-RTE-prefix-reuse](#mem-rte-prefix-reuse); provider cache encoding and exact prefix contents unknown |
| Consent, permission rules/hooks/host callbacks, guidelines and disabling | `Approve the plan before it runs`; `Set a size guideline`; `Turn workflows off` | [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch), [MEM-OBJ-workflow-settings](#mem-obj-workflow-settings); settings consumers described, full permission/revocation internals excluded |
| `/workflows` detail and terminal report | `Watch the run`; `Read the report`; `Bundled workflows` | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results), [RT-CLM-research-report](runtime.md#rt-clm-research-report); partial tool display and report filtering covered; trace storage and retention unspecified |
| Model state | `Cost` | [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model); requested model can be substituted; parameter provenance/update unavailable |

## Core ideas

1. **Result replay is recovery memory, not a transcript reload.** Worker outputs retained during a run can replace worker execution in a later relaunch. The runtime selects an ordered valid prefix, not semantically relevant knowledge. Failure or prompt divergence invalidates a suffix, including completed work. See [RT-RTE-run-replay](runtime.md#rt-rte-run-replay).
2. **Reusable scripts retain orchestration.** Saving and editing preserve symbolic control flow and embedded interpreted task text for future sessions. They do not automatically extract a better method from run traces. The reasons for a change and a later reader of those reasons are unestablished. See [RT-RTE-script-admission](runtime.md#rt-rte-script-admission).
3. **Working context and durable effects differ.** Intermediate results stay out of the foreground context, while script variables, progress inspection, saved results and changed files remain separate channels. A restarted worker loses its transcript without rolling back files. The stack-frame analogy fits selected worker inputs and returned values, but breaks at those surviving effects. See [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) and [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery).
4. **Prefix sharing is not experience sharing.** The documented cache shares matching tools/system prefixes, not sibling findings or transcripts. Its TTL and hold budget affect request processing, not a demonstrated quality improvement. See [MEM-RTE-prefix-reuse](#mem-rte-prefix-reuse).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-prompt-cache
Label: Prompt cache

Source-native identity: a workflow agent's tools-and-system-prompt prefix cache. Storage substrate: opaque provider/request-cache infrastructure; no physical file or internal cache representation is specified. Representational form: the delivered prefix contains tool definitions and system-prompt content, with symbolic interfaces and interpreted instruction text; its stored cache encoding is uninspected. It is not established as model parameters or a store of worker task outcomes.

Lineage: matching requests build the prefix; a sibling's begun response permits later matching first requests to reuse it. Automatic software/provider admission is described, not human approval of each cache write. Exact initialization and provider eviction implementation remain unknown. Later consumer is a matching worker request. TTL is five minutes by default, configurable to one hour. No content-directed revision or trace-derived behavioral instruction is established.

Distinct identity: [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) holds task return values, whereas this object caches tools/system prefixes. [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) mentions the cache but declares no counterpart object. Evidence: SRC-1, `Prompt caching in a fan-out`:

> Agents in the same run can read each other's [prompt cache](/docs/en/prompt-caching#subagents-and-the-cache). Two agents that run with the same model, effort level, agent type, tools, output schema, and working directory build the same tools-and-system-prompt prefix, so an agent that starts after a matching sibling's response has begun reads that sibling's cache on its first request.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### MEM-OBJ-workflow-settings
Label: Workflow settings

Source-native identity: auto-launch consent in user settings, named workflow/project consent, workflow size guideline, disable settings, and session or persistent ultracode configuration. These are access/control metadata and authoring advice, not task-result content. Representational form: symbolic keys/values and scope identities; a size guideline also becomes interpreted advice to foreground Claude. Storage substrate: user/settings files and managed configuration where named, session state for session-only ultracode; exact named-consent encoding and administrative storage are uninspected.

Lineage and admission: human Yes records auto-mode consent; named approval records scoped consent; a user or organization chooses settings. Physical persistence is performed by Claude Code or configuration tooling; permission to launch is not approval of individual worker results. Consumers are later launch evaluation, opt-in surfaces and foreground script authoring. User settings can therefore change later prompts or approval behavior without encoding an acquired factual claim. Retirement semantics of consent are not specified. Environment disable configuration is read at startup; guidelines change the next prompt; disabling leaves an existing run active.

Distinct identity: [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch) describes consumption of this control state, and [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits) describes guideline advice; neither declares a settings object. No task content overlaps [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results). Evidence: SRC-1, `Approve the plan before it runs`, with consent passage in [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch); `Set a size guideline`, with advice passage in [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits); and `Turn workflows off`:

> * Set `"disableWorkflows": true` in `~/.claude/settings.json`. Persists across sessions.
> * Set `CLAUDE_CODE_DISABLE_WORKFLOWS=1`. Read at startup, so it applies wherever you set it.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Routes

#### MEM-RTE-prefix-reuse
Label: Prefix reuse

Endpoints and progression: matching worker requests → prefix cache population → automatic sibling hold/release → later worker's first request reads the matching prefix. Owner: Claude Code scheduling and opaque provider cache. Retained input is [MEM-OBJ-prompt-cache](#mem-obj-prompt-cache), not worker results. This is a distinct processing-reuse path from the task-result flow of [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) and the session-result replay of [RT-RTE-run-replay](runtime.md#rt-rte-run-replay).

- Immediate return: first request begins its response; held matching siblings are released to submit requests using the shared prefix.
- Later read-back: subsequent matching worker first requests consume a cached tools/system prefix; exact underlying delivery encoding is uninspected.
- Delegated visibility: shared prefix only; no sibling task progress, findings or transcript sharing is established.
- Selection predicate: same model, effort, agent type, tools, output schema and working directory; first sibling response begins, with a bounded hold for simultaneous fan-out.
- Invalidation or expiry: cache defaults to five minutes or configured one hour; hold defaults to 5,000 ms and can be disabled with zero; additional eviction rules uninspected.
- Activation or effect: claimed reuse avoids uncached prefix processing; changed reasoning, observed savings and causal benefit unestablished.
- Evidence limits: doctrine/design only; provider storage and actual request matching not inspected.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Prompt caching in a fan-out`, with prefix content passage in [MEM-OBJ-prompt-cache](#mem-obj-prompt-cache):

> When a fan-out starts several matching agents at once, Claude Code holds all but the first until the first agent's response begins, then releases the held agents together so their first requests read the shared prefix instead of each processing it uncached. Claude Code caps the hold at [`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS`](/docs/en/env-vars) milliseconds, `5000` by default. Set it to `0` to disable the hold.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results)

Memory lineage: model-backed workers generate prose or schema-shaped JSON from task inputs and tool-accessible material. Initial sources may mix project content and external sources; the capture does not identify every input. Return values are derived task products, not full raw execution traces. Runtime persistence automatically admits these outputs for recovery without documented human per-result approval. Shape validation is not knowledge validation.

Later authority: a saved result delivered instead of executing an agent becomes a JavaScript value; script rules can use it to choose later calls and output. It is not automatically an instruction to a worker. A script can pass content onward, but the example passes discovery filenames into audit prompts rather than all raw tool traces. Foreground Claude receives the selected terminal answer, not every intermediate value. Local session storage and cloud conversation-history persistence are documented in the supplied object and replay records; internal encoding, result budgets and cleanup are unknown.

Display is not payload equivalence: SRC-1, `Watch the run`, says the full prompt/result can be expanded, but listed tool calls expose only the start of each result. This UI witness cannot establish complete retained tool transcripts:

> Press `Enter` to expand the detail. The prompt and result then show in full, and each listed call shows its input and the start of its result.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### On [RT-RTE-run-replay](runtime.md#rt-rte-run-replay)

Memory selector inputs are prior agent-start order, completion/failure and current-versus-prior prompt equality. Selected retained parts are completed values before the first invalid slot; delivery is automatic substitution into the relaunched script after a human/Claude relaunch request. No semantic retrieval query or independent unsolicited knowledge injection is described. Reuse is session-associated, including reopened local/cloud sessions; a fresh session starts a new run. No token-based selection budget is specified. Evidence: SRC-1, `Which agents run again`, supplied verbatim in this record.

These automatically retained task outputs change recovery decisions and can shape later script computation. The source does not establish a trace-to-revised-method transformation. A saved prefix can remain applicable according to prompt equality even though the document does not specify what happens when models, options, tools or external file state change. Therefore freshness under those changes is unresolved, not guaranteed.

#### On [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script)

Memory lineage: foreground Claude authors task-specific orchestration; runtime stores the run copy; human save action creates a reusable copy. Human or Claude edits can then change future scripts. Embedded prompts retain natural-language task guidance alongside symbolic control flow and metadata. Runtime/loader consumers have symbolic execution authority; downstream workers interpret prompt text under separate permissions. The session-run artifact permits inspection/diff/relaunch; the project/personal/plugin copies extend consumption beyond one session. The script need not retain the author's rationale or a criticism history. Evidence: SRC-1, `How a workflow runs`, quoted in this object, and `Save the workflow for reuse` / `Edit a saved script`, traced in [RT-RTE-script-admission](runtime.md#rt-rte-script-admission).

#### On [RT-RTE-script-admission](runtime.md#rt-rte-script-admission)

Admission separates human content choices from software checks: the human chooses a run and location to save; direct human edits or requested Claude edits supply revised content; symlink/metadata/syntax checks validate a path or structure, not the method's truth. A later launch gate is not retroactive approval of every embedded claim. Named invocation selects by command and directory/namespace precedence, not semantic relevance. `/reload-skills` re-reads edited directories; versioned rollback and complete deletion/update behavior are unknown. Guidance from `/workflow-authoring` is recommended, but its text is excluded. Persistence of explanatory reasons and any later reason-consuming route are unestablished. Evidence: SRC-1, `Save the workflow for reuse`, `Edit a saved script`, passages supplied by this record.

#### On [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery)

Working-context transformation: a stall or manual restart replaces the attempt using the same original prompt, without its prior transcript. No summary checkpoint or verbatim transcript tail is documented for that restart. Changed files remain, so a later attempt can encounter prior effects through tools; the source does not guarantee it reads those files or reconstructs their rationale. Tool-result storage and UI retention across attempts are unknown. Usage-limit waits are a separate retry route whose exact context retention is unspecified. Evidence: SRC-1, `When an agent stalls and restarts`, transcript-loss passage supplied by this record.

#### On [RT-CLM-research-report](runtime.md#rt-clm-research-report)

Material selection: search/fetch products feed cross-checking and voting; a cited report is delivered to the foreground with non-surviving claims omitted. Uncheckable claims remain marked unverified, which counters a simple retained/refuted dichotomy. This is declared content curation of a task output, not evidence of a durable learned knowledge store. The actual verifier prompts, thresholds, preservation of rejected claims/reasons and later consumer of a rejection record are unknown because the bundled script is excluded. Report persistence beyond ordinary result/session persistence is unspecified. Evidence: SRC-1, `Read the report` and `Bundled workflows`; supplied uncertainty passage in this record.

## Write side

The mechanisms have different admission controls. Runtime result tracking automatically retains agent outputs for replay; humans may start, stop or restart a run but do not approve each value. Structured-output checks can reject contradictory schemas before a worker starts and invalid outputs after retries; these are format checks rather than factual admission. The script can filter the resulting list. SRC-1, `What the saved script looks like`, states:

> An `agent()` call resolves to `null` if you stop it mid-run or it hits an unrecoverable API error. `pipeline()` keeps each `null` in the results array, which is why the example ends with `.filter(Boolean)` to drop those entries, including the slot of [an agent that stalled on every attempt](#when-an-agent-stalls-and-restarts).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

Consequently, a returned audit list is not a complete account of all discovered files. The more specific direct-await stall error case in [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery) also prevents treating every failure as a null-valued result. Whether null/error records themselves are persisted is unspecified.

Saving scripts is deliberate human selection of reusable orchestration, followed by software I/O and loader checks. Editing is human or requested model authorship, not automatic extraction from task traces. See [RT-RTE-script-admission](runtime.md#rt-rte-script-admission). Prefix writes are automatic processing-cache population, with configuration controlling TTL, not content approval. Consent/settings writes retain human choices and software control state, as [MEM-OBJ-workflow-settings](#mem-obj-workflow-settings) distinguishes.

No compaction transformation can be established from SRC-1. Known raw-to-derived chains are task/tool inputs → worker answer → saved return value → replayed script, and fetched material → verified/filtered report → foreground. Full raw trace retention, reason preservation and later consumption of rejected claims are unknown. Transcript discard on restart is known even though initialization of the worker context is not. Withdrawal is partly logical: replay invalidates a suffix, stopping an individual agent marks failure, and script filtering removes output entries. Physical deletion of old checkpoints or rejected claims is unspecified. Disabling launch surfaces does not withdraw an already running workflow.

## Read-back

[RT-RTE-run-replay](runtime.md#rt-rte-run-replay) is the principal retained-result read-back: a relaunch request triggers code selection and substitution into script calls. Prefix reuse is independently automatic on matching worker requests, with the trigger, matching inputs, TTL and hold budget recorded in [MEM-RTE-prefix-reuse](#mem-rte-prefix-reuse). Neither route uses a semantic relevance score or establishes improved capacity.

Saved scripts reach future named invocations through directory/namespace selection and launch permissions. Static bundled scripts do not themselves become use-acquired memory; a saved task-generated script does. [RT-BAP-script-control](runtime.md#rt-bap-script-control) and [RT-BAP-agent-prompts](runtime.md#rt-bap-agent-prompts) identify distinct downstream authorities. Persisted consent and settings influence later launch/authoring behavior through [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch), rather than supplying task evidence.

Ordinary same-run variables are working state, not by themselves retained read-back. Script isolation keeps intermediate values out of foreground context; workers' return values cross into script computation and only the selected final output returns to the conversation. Human inspection can nevertheless expose prompt/result details and a partial tool-call display. The documentation's “only the final answer” claim therefore describes orchestration delivery, not universal inaccessibility of intermediates. No precise context-token budget, complete inherited worker context or automatic summary-reload mechanism is established.

## Integration issues

- No supported correction to the supplied runtime record values was found. Its prompt-cache mention is elaborated, not contradicted, by [MEM-OBJ-prompt-cache](#mem-obj-prompt-cache) and [MEM-RTE-prefix-reuse](#mem-rte-prefix-reuse). These are distinct from [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) and [RT-RTE-run-replay](runtime.md#rt-rte-run-replay); no possible duplicate declaration is proposed.
- [MEM-OBJ-workflow-settings](#mem-obj-workflow-settings) supplies a distinct control-state object whose consumers overlap [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch) and [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits), not a replacement for either record.
- Replay freshness under model/options/tool/file changes remains unresolved: SRC-1, `Which agents run again`, specifies prompt/order/failure invalidation only. This prevents a complete cache-key or semantic-freshness conclusion for [RT-RTE-run-replay](runtime.md#rt-rte-run-replay).
- Saved-result serialization, deletion/retention policy, crash consistency, null/error persistence and raw transcript lifetime remain unresolved in SRC-1, `How a workflow runs`, `Watch the run`, and `Resume after you leave the session`. They prevent identifying a complete trace store or physical cleanup mechanism for [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results).
- The full worker context and usage-wait checkpoint form remain unknown in SRC-1, `How a workflow runs` and `When a run hits your usage limit`; no summary mechanism is inferred for [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) or [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery).
- Rejected-claim reasons and later consumers, and saved-script revision reasons, are unestablished because actual bundled/reusable scripts and the authoring reference are excluded. This prevents attributing trace-fed method revision or retained criticism to [RT-CLM-research-report](runtime.md#rt-clm-research-report) or [RT-RTE-script-admission](runtime.md#rt-rte-script-admission).
- Exact prefix encoding/eviction and consent revocation remain opaque in SRC-1, `Prompt caching in a fan-out` and `Approve the plan before it runs`; this limits [MEM-OBJ-prompt-cache](#mem-obj-prompt-cache) and [MEM-OBJ-workflow-settings](#mem-obj-workflow-settings), without negating their documented consumers.

## Limitations and checks

Identity was rechecked against the supplied boundary: run ID, source identity and capture label are unchanged. The method inputs are the supplied job, worker rules, collection, member types and records contract; no prior analysis or linked source was used. Direct reads covered the entire frozen capture. There was no target execution, implementation inspection or experiment. No observed activation, quality improvement, causal benefit, complete trace retention or general self-improvement conclusion follows.

Deterministic validation: the supplied `commonplace-run validate-output` command passed the member content check. Its result states that invocation residue was not checked. This establishes structure and quotation occurrence, not job acceptance or claim support.
