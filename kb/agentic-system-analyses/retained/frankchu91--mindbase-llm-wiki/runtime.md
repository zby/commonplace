---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MindBase runtime baseline: server contribution checkpoints, direct build/research admission, hosted builder and question consumers at c5273d2."
run-id: AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01
reviewed-boundary: c5273d2336c4d686df41c2a1495f14f085707f51
---

# MindBase runtime report

## Runtime account

### Evidence and consequential work

MindBase maintains persistent Markdown knowledge and supplies it to subsequent questions and host sessions. This report traces implementation, not successful operation. SRC-1 supplies source code and declared instructions only; no model calls, target tests or examples were executed. Every operation conclusion below remains uninspected. Model compliance, knowledge quality and benefit are not established.

The ordinary invocation selected here is a web contribution, from user text through a checkbox plan to persistent effects. Three forcing contrasts are direct server build/research, the hosted plugin builder's separate MCP write pipeline, and question answering with optional file-back. Lint supplies a bounded diagnostic side loop. These contrasts refute a single uniform approval/atomic-write interpretation without requiring an exhaustive audit of all shipped clients.

Added SRC-1 implementation coverage beyond the boundary's initial reads: `apps/server/src/routes/ops.ts`, `apps/server/src/ops/{llm,types,web-search}.ts`, `apps/server/src/ops/recipes/{contribute,build,research}.ts`, `apps/server/src/lib/daily-entry.ts`, full `apps/server/src/context.ts`, `apps/web/src/components/ops/OpRun.tsx`, `apps/mcp/src/tools/atomic-write-context.ts`, `apps/mcp/src/lib/safe-write.ts`, `packages/core/src/qa/query.ts`, `packages/core/src/adapters/{registry,ollama}.ts`. Added doctrine/design coverage: `apps/plugin/commands/build.md`. All paths are at the frozen revision; no source is added.

### Shipped entry paths and execution ownership

The Express server mounts `/api/ops`, `/api/ask`, compile, capture, tree, project and other routes; it starts capture, RSS, brief, SRS, embedding, synthesis and analysis workers (SRC-1, `apps/server/src/index.ts`). Startup wiring is not evidence of their complete semantics. The server also serves the web distribution. The MCP server independently loads its context, registers tools/resources/prompts, and connects a stdio transport (SRC-1, `apps/mcp/src/index.ts`). Plugin commands and agent definitions delegate execution to an external host rather than running through the Express coordinator.

The README's architecture diagram describes one ops engine with human approval, but the inspected paths are not one universal pipeline. See [RT-CLM-approved-changes](#rt-clm-approved-changes), [RT-RTE-contribute-plan](#rt-rte-contribute-plan), [RT-RTE-build-context](#rt-rte-build-context), [RT-RTE-research-page](#rt-rte-research-page), and [RT-RTE-plugin-build](#rt-rte-plugin-build).

### Ordinary contribution end to end

The human opens a contribution operation in the React component. The client sends `{mode:'plan', text, sourcePath?}`; the route resolves the current project and attributed user, checks model configuration and rejects v1 layout. The server, not a model, owns progression. If no source path is supplied, it first persists text in the contributor daily file. This is already a write before the wiki approval checkpoint. Repeated text matching the file's trailing body is suppressed by `appendDailyEntry`; this is not a general idempotency key (SRC-1, `apps/server/src/lib/daily-entry.ts`).

The coordinator gathers current context, README and index.yaml, but the contribution recipe actually interpolates context and README, not index.yaml. It supplies up to five related-page summaries, up to sixty existing slugs and pending slugs. Related search receives at most 300 input characters and produces 200-character summaries. These are budgeted hints, not full related-page evidence (SRC-1, `apps/server/src/routes/ops.ts`, `apps/server/src/ops/gather.ts`, `apps/server/src/ops/recipes/contribute.ts`).

A configured model receives natural-language system/user messages and emits JSON. `completeJson` schema-checks it and makes at most one corrective completion with the invalid output and parse/schema error added. It does not implement a provider-tool loop. After generation, the coordinator checks existing and reserved page slugs again, adds source citation tags to two action kinds, assigns a random plan ID and retains the plan in process memory for ten minutes. The client displays takeaways and checked actions, and sends selected action indexes only after Apply. Cancellation closes the UI; the server plan remains until consumed or pruned. The second request filters the stored actions, consumes the plan before writing and executes actions sequentially. The client receives applied and failed lists and can open resulting files. See [RT-OBJ-actions](#rt-obj-actions) and [RT-RTE-contribute-plan](#rt-rte-contribute-plan).

No model supplies the human decision. Conversely, the server receives a plan ID and indexes, not evidence of a human identity or deliberation. The inspected apply branch checks neither the current project nor the requesting user's ownership of the plan; it uses the stored project root. This is a caller-selectable checkpoint protocol, not an authorization guarantee (SRC-1, `apps/server/src/routes/ops.ts`, `apps/server/src/ops/runner.ts`).

### Guarantees and forcing cases

| Control and owner | Enforcement point and strength | Covered paths and countercase | External contract and status |
|---|---|---|---|
| Wiki-change selection; UI plus server | Stored-plan filtering; protocol | Contribution plan/apply only. Build and research apply generated actions directly; ask can auto-save. | A trusted caller must represent human selections. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Action destination restriction; server | Zod action union, then lexical `safeAbs`; invariant over validated ops action destinations | No ops action edits contributor/raw content. Source capture deliberately appends separately. MCP and host tools do not pass through this schema. Lexical checks are not a demonstrated symlink or OS sandbox. | Requires validated actions and filesystem assumptions. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Branch-specific context line checks; executor / MCP tool | Server `update_context` and `append_context_section` reject results over 400 lines; MCP replacement splits overflow; invariant only over those branches' outputs | Server `add_wikilinks` also accepts context.md and writes without a line check or snapshot. Thus the ops executor does not enforce a universal 400-line bound. MCP replacement uses temporary file plus rename and overflow page. | Filesystem write/rename semantics required; neither concurrency nor other context writers is covered by a global bound. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Source citation insertion; contribution coordinator | `ensureCitations`; invariant for missing exact tags on create-page and append-section actions | `update_context` and `add_wikilinks` return unchanged. Build/research do not call it. No claim-level truth check follows insertion. | Caller-supplied sourcePath is not checked for file existence in this route. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Restricted hosted builder; plugin definition | Tool allowlist; deployment guarantee conditional on host | Builder allows Read and selected MCP tools, not Bash/Edit/Write. This does not restrict the foreground agent, other agent definitions, the Express API or direct MCP callers. | Host must honor tool grants and isolation. implementation conclusion status: afforded; operation conclusion status: uninspected. |

The action restriction is substantive: all inspected server ops recipes use `actionsSchema`; research's prose asks for exactly one create action and at most one append, but its actual schema accepts one to three actions from the entire common union. Thus context replacement is schema-admissible in research, even though not requested. Build similarly requests a context rewrite without structurally requiring that action kind. This is an input-to-executor result, not evidence that a deployed model produced the alternative (SRC-1, `apps/server/src/ops/recipes/research.ts`, `apps/server/src/ops/recipes/build.ts`, `apps/server/src/ops/types.ts`).

Context-line forcing case: the common action schema permits `add_wikilinks` with `path: "context.md"`. The executor returns unchanged when all requested links already occur; otherwise it appends a See also line with separator newlines, without checking the resulting line count or snapshotting prior content. A context already at the checked branches' limit can therefore grow beyond it through this schema-valid branch. Contribution's selected plan, build and research all forward accepted common-union actions to this executor; the recipes' narrower prose does not reject that action. This establishes a reachable implementation alternative, not an observed model choice or deployed overflow (SRC-1, `apps/server/src/ops/types.ts`, `apps/server/src/ops/executors.ts`, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/recipes/build.ts`, `apps/server/src/ops/recipes/contribute.ts`, `apps/server/src/ops/recipes/research.ts`). Replacement and section append retain their supported rejection checks; MCP replacement retains its separate overflow behavior.

> .regex(/^(sources\/research\/[a-z0-9][a-z0-9-]*\.md|context\.md)$/, 'links may only target research pages or context.md');
> --- `apps/server/src/ops/types.ts`

> const missing = action.links.filter((l) => !current.includes(`[[${l}]]`));
>       if (missing.length === 0) return action.path;
>       const seeAlso = `See also: ${missing.map((l) => `[[${l}]]`).join(', ')}`;
>       await writeFile(abs, `${current.replace(/\n*$/, '\n\n')}${seeAlso}\n`, 'utf-8');
> --- `apps/server/src/ops/executors.ts`

Citation forcing case:

> if (a.kind === 'append_context_section' && !a.markdown.includes(tag)) {
>       return { ...a, markdown: `${a.markdown.trimEnd()} ${tag}` };
>     }
>     return a;
> --- `apps/server/src/ops/runner.ts`

The unchanged return covers supported `update_context` actions. The contribution schema accepts them and apply passes selected actions onward. Accordingly, the code does not establish the comment's broad implication that every page written from an entry deterministically cites it. Adding a tag also establishes neither source existence nor entailment.

### Persistence, recovery, coordination and limits

For the inspected ops executor, every action has its own catch and failure entry. Earlier writes remain when a later action fails; `done` is not transactional success. Context replacement snapshots prior nonempty content but then writes directly. Append-context and wikilinks use read/modify/write without the replacement snapshot. Build's lock is process-local and project-specific; it does not serialize research or contribution writes. Pending slug reservations are also process-local. A server restart loses plans. Snapshot presence affords manual recovery; no automatic restore after partial failure is established (SRC-1, `apps/server/src/ops/executors.ts`, `apps/server/src/ops/runner.ts`).

> for (const action of actions) {
>     try {
>       result.applied.push(await applyOne(root, action));
>     } catch (e) {
>       result.failed.push({ action: action.kind, error: (e as Error).message });
>     }
>   }
> --- `apps/server/src/ops/executors.ts`

The SSE adapter starts asynchronous reindexing on an applied event and ignores reindex errors. A terminal event therefore does not guarantee immediate search visibility. `context.ts` reloads Markdown into MiniSearch and a SQLite graph cache; retained contributor/raw text and synthesis have distinct index types. The ask path then re-reads selected bodies. Detailed memory transformations and provenance assessments belong to the memory member, not this baseline.

Unresolved included paths remain: capture clients and their extraction/admission branches; legacy compile/tool executors; MCP search and health variants; manual tree editing; synthesis and classification workers; schema-edit routes; evaluators and packaging beyond startup declarations. They prevent exhaustive claims about approval, security, knowledge mutation, instruction revision, context isolation or machinery change across MindBase. No product/capability/production-machinery self-modification route is established by this bounded trace; this is not an evidenced absence. Provider-side state and external host scheduling remain outside inspectable implementation. No latency or local-only guarantee follows from the README: optional cloud adapters and Brave explicitly cross the machine boundary.

## Shared records

### Components

#### RT-CMP-model
Label: Configured server model

SRC-1, `apps/server/src/context.ts`, `packages/core/src/adapters/registry.ts`, `packages/core/src/adapters/ollama.ts`. Source-native identity is the configured provider/model pair. Representational form is distributed-parametric at the provider; storage substrate is provider-owned weights, inaccessible here. Local code stores configuration and sends messages, not weight updates. Parameters are not changed by the inspected inference routes; provider-side changes remain uninspected. Exact weight/version identity is not pinned by these paths. Configurable model strings and base URLs can resolve to another model; configuration can be reloaded or saved during operation. The host builder's model is separately host-selected and uninspected, not necessarily this model.

> return createAdapter(config.provider, {
>         apiKey: config.apiKey,
>         model: config.model,
>         baseUrl: config.baseUrl || undefined,
>       });
> --- `apps/server/src/context.ts`

> model: request.model,
>           messages: request.messages,
>           tools: toOllamaTools(request.tools),
> --- `packages/core/src/adapters/ollama.ts`

OpenAI/DeepSeek and Anthropic dispatch is wired in the registry; only the Ollama request translation was traced here. Provider internals and endpoint immutability are uninspected. The mock branch in `context.ts` is an explicit alternative when `MOCK_LLM=1`, not evidence of real-model operation.

### Operative objects

#### RT-OBJ-actions
Label: Ops action envelopes

SRC-1, `apps/server/src/ops/types.ts`, `apps/server/src/ops/llm.ts`, `apps/server/src/ops/executors.ts`. Action kinds, path/slug constraints, selection indexes and JSON fields are symbolic content consumed by fixed code rules. Storage substrate is transient parsed objects, plus the process-local pending-plan map for contributions. Markdown payloads are a separate natural-language part: written to `context.md` or research pages and later interpreted by humans/models. Their semantic truth is not validated by the envelope schema. This record identifies the command envelope, not the retained knowledge corpus.

> export const actionsSchema = z.array(actionSchema).max(20);
> --- `apps/server/src/ops/types.ts`

> const parsed = opts.schema.safeParse(JSON.parse(extractJson(raw)));
>       if (parsed.success) return parsed.data;
> --- `apps/server/src/ops/llm.ts`

### Routes

#### RT-RTE-contribute-plan
Label: Contribution plan and selected application

Endpoints: React OpRun → `/api/ops/contribute` plan → pending map → apply → project files/log. Owner: server coordinator; human client chooses indexes. Identity: random planId binds generated actions and stored project root, with projectId and attributed capture user. Context, model and effects are described in the ordinary trace above (SRC-1, `apps/web/src/components/ops/OpRun.tsx`, `apps/server/src/routes/ops.ts`, `apps/server/src/ops/runner.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE phases, takeaways, guarded plan and planId; apply emits per-action success/failure and done, or error.
- Later read-back: Persisted source, context and research pages can enter subsequent builds, search and question invocations.
- Delegated visibility: inapplicable — server makes a completion, not a child agent; client sees selected plan and outcomes.
- Selection predicate: Model proposes schema-valid actions; duplicate guard filters existing/reserved research slugs; caller-selected indexes filter the stored plan.
- Invalidation or expiry: Ten-minute in-memory TTL; consumed before application; process loss discards pending plans.
- Activation or effect: Source append precedes proposal; selected actions write wiki content. Actual downstream behavioral dependence remains unobserved.
- Evidence limits: No supplied user trace or quality evaluation; caller sourcePath is accepted as a citation label without checking source existence here.

Admission: open user request. Model proposes wiki changes under the contribution recipe, current README/context and related summaries; human can veto individual wiki actions in the shipped UI. Capture text itself is user-supplied, not awaiting model approval. Software checks schema, duplicate slugs and destination constraints. An API caller can also send indexes; server does not verify a human decision. No expected-answer oracle is used. Rejection is deselection/abandonment/expiry or executor failure; recovery preserves captured text when the model step fails, but does not roll back earlier applied actions. What persists is source text, selected Markdown, links and logs, not the pending proposal across restart.

> const actions = pending.actions.filter((_, i) => selected.includes(i));
> --- `apps/server/src/ops/runner.ts`

> const selected = plan.checked.flatMap((on, i) => (on ? [i] : []));
> --- `apps/web/src/components/ops/OpRun.tsx`

#### RT-RTE-build-context
Label: Server context build

Endpoints: `/api/ops/build` → gather → completeJson → applyActions → files/log/SSE. Owner is server; projectId scopes a process-local build lock. SRC-1, `apps/server/src/routes/ops.ts`, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/gather.ts`, `apps/server/src/ops/recipes/build.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE phase and applied/failed events followed by done, or error; concurrent build reports an error.
- Later read-back: Rewritten context and created research files can be loaded by future builds, ask retrieval and session-start.
- Delegated visibility: inapplicable — no sub-agent; one completion plus at most one parse/schema repair completion.
- Selection predicate: Contributor and research Markdown modified after context.md, newest first, at most thirty files and 4,000 characters per body. Raw extracted files are not selected by this gather function.
- Invalidation or expiry: Build lock releases in finally; changed context mtime becomes the next selection threshold, not a per-source completion ledger.
- Activation or effect: Schema-valid generated actions go directly to executors; `update_context` rejects replacements over 400 lines and snapshots prior content, while `append_context_section` checks the resulting line count without snapshotting. A schema-valid `add_wikilinks` targeting context.md bypasses both checks and snapshots; this route therefore has no universal context-line bound.
- Evidence limits: Delivered source excerpts do not establish complete synthesis; no observed build, contradiction handling or improvement.

Admission: a user triggers a build; model proposes content under the build recipe, README, existing context and source excerpts. Code admits actions after structural parsing, without per-content human selection. The recipe asks to preserve still-true content, date decisions and flag contradictions; these are model instructions, not executor checks. User can choose not to initiate a build, which is not approval of each generated change. No answer oracle. Rejection is schema/error/line-cap failure, with one parse/schema retry; snapshots afford recovery of replacement context, not a transaction for the whole action list. Persisted outputs are Markdown and an operation log.

> const result = await applyActions(ctx.projectRoot, out.actions);
>     await appendOpLog(ctx.projectRoot, 'build', `applied ${result.applied.length}, failed ${result.failed.length}, sources=${sources.length} (ui)`);
> --- `apps/server/src/ops/runner.ts`

#### RT-RTE-research-page
Label: Server research synthesis

Endpoints: topic request → related wiki bodies, optionally Brave results → completion → persistent actions. Owner: server coordinator. SRC-1, `apps/server/src/routes/ops.ts`, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/recipes/research.ts`, `apps/server/src/ops/web-search.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE phases, applied/failed paths and wiki-only/web mode note, or error.
- Later read-back: Created research/context content can enter subsequent retrieval and builds.
- Delegated visibility: inapplicable — no worker agent; HTTP search and model calls return content to the coordinator.
- Selection predicate: Up to six related wiki hits, each body capped at 4,000 characters; optional top three Brave results with fetched page text capped at 5,000 characters.
- Invalidation or expiry: inapplicable — no pending approval plan or explicit generated-page expiry in this path.
- Activation or effect: Code directly applies schema-valid model actions; no contribution citation insertion or checkbox stage.
- Evidence limits: Failed web fetch uses snippets/title; failed Brave call degrades to wiki-only. Content support and model compliance are unobserved.

Admission: open topic request, with wiki-only and optional web operating modes. Model proposes under the research recipe and provided sources; software admits one to three common action-union members. Human has no per-result veto in this route. No answer oracle; retrieved sources are evidence supplied to the model, not expected answers. Recipe requirements on exact action composition, claim support and citations are not guaranteed by the schema. Executor failure gives partial results rather than whole-operation rollback. Pages/context/log persist.

> export const researchSchema = z.object({
>   actions: actionsSchema.min(1).max(3),
> });
> --- `apps/server/src/ops/recipes/research.ts`

#### RT-RTE-plugin-build
Label: Hosted builder and MCP context replacement

Endpoints: `/mb:build` host command → Task builder → MCP tools → context/snapshot/log. Next-step owner is the external agent host, guided by the shipped command and agent text. SRC-1, `apps/plugin/commands/build.md`, `apps/plugin/agents/builder.md`, `apps/mcp/src/tools/atomic-write-context.ts`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: MCP write returns projectId, snapshot path, overflow path and line count; prescribed child return is a one-line build summary.
- Later read-back: New context is read by subsequent model sessions and operations; overflow remains a research page with an in-context pointer.
- Delegated visibility: Command supplies projectId to a separate builder Task; prescribed caller-visible return is only summary. Actual host context isolation and tool-grant enforcement are external and unobserved.
- Selection predicate: Builder is instructed to validate, load, gather unbuilt sources and read them, then synthesize; MCP replacement accepts nonempty content for a resolved project without checking that those earlier steps happened.
- Invalidation or expiry: Context replaced; prior body snapshotted with minute-resolution stamp. No inspected per-tool sequence token or proof of validation.
- Activation or effect: MCP writes a temporary context file and renames it; over 400 input lines become a shortened head plus research overflow pointer.
- Evidence limits: Instructions establish requested sequence only. Host behavior, merge correctness, index rebuild and final logging by the agent are unobserved.

Admission: human triggers the command; hosted model synthesizes under README build rules and builder instructions, including preservation and contradiction flagging. MCP tool structurally admits supplied content without a human approval parameter or semantic merge check. External host may impose its own approval policy, unresolved here. No answer oracle. Invalid tool input/project is rejected. The implementation provides prior snapshots but does not automatically restore them; the snapshot name has minute resolution, so it is not an unqualified unique revision history. The tool's replacement is different from server direct-write semantics.

> const tmp = join(root, `${p.context}.tmp.${stamp}`);
>   await writeFile(tmp, finalBody, 'utf-8');
>   await rename(tmp, join(root, p.context));
> --- `apps/mcp/src/tools/atomic-write-context.ts`

#### RT-RTE-ask-answer
Label: Question retrieval, tool loop and optional answer persistence

Endpoints: `/api/ask` → core askQuestion → configured adapter/read_file → SSE answer; optional auto-save → research or legacy wiki note. Owner is core code for iteration and server for persistence; model decides whether to request file reads. SRC-1, `apps/server/src/routes/ask.ts`, `packages/core/src/qa/query.ts`, `apps/server/src/context.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sources/progress/text/thinking/done events; model errors can terminate the generator. Server optionally emits auto_saved.
- Later read-back: With autoSave enabled and an output matching AUTO_SAVE_REGEX, the answer becomes a research page in v2 or wiki note plus metadata/index in v1; later queries can retrieve it.
- Delegated visibility: inapplicable — provider tool requests are executed locally by the core loop, not delegated to a sub-agent.
- Selection predicate: Default six BM25 candidates after source boost; first three bodies capped at 3,000 characters each within source budget; recent raw IDs and one raw reference per candidate can add sources. forcedContextSlugs bypasses BM25 through a supported option, mapping to wiki/notes paths.
- Invalidation or expiry: Last ten history messages enter the invocation; at most three model iterations by default. No auto-saved-page expiry here.
- Activation or effect: Model receives instructions, candidate summaries and selected text; read_file adds requested store text. Successful answer persistence reindexes before auto_saved. Grounded correctness and causal use of a retrieved passage remain unobserved.
- Evidence limits: RetrievalBudget describes source-block clipping, not a hard bound on all messages, index, hot context or later read_file bodies. Done citations contain tool-read paths, not parsed factual citation markers.

The initial message loads `schema/query.md` or fallback natural-language citation instructions in a user-role system-reminder wrapper. Hot context and INDEX.md are added; history is sliced, not summarized. Source bodies are preferentially selected and clipped; later read_file results are not subject to that source-block budget. Only read_file is advertised; unknown tool names get an error result. This is materially different from ops' single constrained completion.

> const recent = opts.history.slice(-10);
> --- `packages/core/src/qa/query.ts`

> if (ctx.config.autoSave) {
>         const match = fullText.match(AUTO_SAVE_REGEX);
> --- `apps/server/src/routes/ask.ts`

Admission for auto-save: model text supplies title/body marker, configuration licenses saving, and the server writes without a content-specific approval stage. Human enablement is not per-answer approval. No expected-answer oracle or outcome comparator. Save failures are reported as SSE errors; v2 uses the shared executor, whereas v1 performs several sequential store writes without the inspected ops snapshot contract. The generator can yield an error and return while the server still has partial fullText; the route checks the accumulated marker, not an independent successful-answer verdict. Actual reachability of such a marked partial answer depends on provider output and is not observed.

#### RT-RTE-lint-findings
Label: Lint diagnosis and finding retention

Endpoints: `/api/ops/lint` → gather → completion → evidence verification plus deterministic findings → dated artifact/log/SSE. Owner: server; model proposes semantic findings; code computes structural findings and checks quote occurrence. SRC-1, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/gather.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Findings event, date and done; empty knowledge produces an error.
- Later read-back: Latest dated lint artifact can be fetched; dismissal writes its dismissed flag.
- Delegated visibility: inapplicable — no child worker in this coordinator path.
- Selection predicate: Up to forty research-page excerpts of 1,200 characters; source stats capped at 400; model deterministic-kind outputs discarded. Contradiction findings require two verified quotes, stale findings one.
- Invalidation or expiry: Same-day artifact path overwritten by subsequent lint; latest date selected lexically; no automatic knowledge repair in runLint.
- Activation or effect: Findings and dismissal state persist under artifacts/lint; knowledge files are not rewritten by this lint operation.
- Evidence limits: Case/emphasis/whitespace-normalized substring occurrence is not logical contradiction validation. No observed diagnosis accuracy or downstream response.

Diagnosis mode is an open audit request. Model proposes semantic findings under lintPrompt; software vetoes insufficient quote evidence for the two named kinds. Humans can dismiss retained findings but are not required to approve their initial retention. Existing page bodies are the quote-check reference, not an expected-answer oracle for semantic truth. Findings/logs persist; the inspected route has no closed automatic criticism-to-revision loop.

> const MIN_VERIFIED: Partial<Record<Finding['kind'], number>> = { contradiction: 2, stale: 1 };
> --- `apps/server/src/ops/runner.ts`

### Claims

#### RT-CLM-approved-changes
Label: Claimed human approval of AI changes

SRC-1, `README.md` claims the AI-owned layer has every change human-approved:

> **The AI** — every change human-approved
> --- `README.md`

- doctrine conclusion status: claimed

The claim is implemented as a selectable plan for web contributions, not a whole-system invariant. Direct build, research, MCP replacement and configured ask auto-save supply concrete alternate admission paths in the route records above. This qualification does not imply that users never approve those operations through an external host.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-project-rules
Label: Project README guides proposals

SRC-1, `apps/server/src/ops/recipes/contribute.ts`, `apps/server/src/ops/recipes/build.ts`. Consumer: configured server model. Channel: natural-language PROJECT RULES in the user message. Force: advisory model guidance, not executor-enforced semantic rules. Horizon: later contribution/build invocations loading the same persisted README. This is an instruction-bearing path distinct from source evidence and from the symbolic action schema. Research receives context but its recipe does not interpolate README even though core gathering loaded it.

> PROJECT RULES (README.md):\n${input.core.readme || '(none)'}
> --- `apps/server/src/ops/recipes/build.ts`

#### RT-BAP-session-context
Label: Session-start context supply

SRC-1, `apps/plugin/hooks/session-start`. Consumer: enclosing host's next agent session. Channel: hook JSON additionalContext variants containing current project README, context and index.yaml. Force: model-interpreted background/instruction content; host acceptance and compliance unobserved. Horizon: across sessions via persisted project files and config selection. Selection is currentProjectId from config; missing selection/project returns setup guidance. No content-level relevance filter or truncation is implemented in the hook. It injects retained knowledge without a contemporaneous question selecting a page.

> ## context.md (curated truth — generated by /mb:build)
> ${context}
> --- `apps/plugin/hooks/session-start`

## Annotations

none
