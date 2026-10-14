---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "EchoWiki runtime baseline tracing Obsidian and CLI ingestion, model-directed wiki writes and editable compilation instructions."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
---

# EchoWiki runtime report

## Runtime account

EchoWiki compiles incoming text into linked Markdown pages. Code owns the finite sequence; models supply summaries, create/update/related selections and page bodies. It is not a model-controlled tool loop. The shipped plugin runs the shared compiler in-process; the CLI invokes the same API with filesystem storage. Browsing the result belongs to Obsidian. The evidence is inspected implementation and declared intent in SRC-1, not a supplied run, provider result or experiment. Operation and benefit remain unobserved (SRC-1: `src/compiler-api.ts`, `src/wiki/compiler.ts`, `obsidian-plugin/src/compiler-client.ts`, `src/cli/compile.ts`, `README.md`).

### Ordinary compilation

The ordinary manual invocation is **Compile active raw file**. The user selects a text file; the plugin checks its raw-folder membership and extension, derives a document name from its basename, reads the current content and invokes the shared API. `inFlight` is keyed by vault-relative path, not document identity or output page. The plugin requires a nonempty API key and model. The API creates an OpenAI-compatible chat client from model/key/base URL settings. No provider prefix routing occurs: the prefix before `/` is discarded. This route is [RT-RTE-document-compile](#rt-rte-document-compile); the model component is [RT-CMP-llm-model](#rt-cmp-llm-model) (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/utils.ts`, `src/compiler-api.ts`, `src/llm/client.ts`).

The compiler reads stored `AGENTS.md` or a fallback, combines it with language and wikilink instructions in a system message, and places the entire input text in a user message. A summary call returns requested JSON; invalid JSON falls back to raw response text. A planning call receives those messages, the draft summary and descriptions of every existing concept/entity page. Description fallback is a flattened 150-character body preview; entity briefs also include type and source count. The model chooses create, update and related entries. Code accepts nonempty names, filters entity types and checks that related pages exist. It does not check whether a create entry already exists, enforce the requested two-to-three-concept limit, or enforce unique placement in one group (SRC-1: `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/llm.ts`, `src/wiki/prompts.ts`).

Generation tasks each receive their own explicit message array, not a growing multi-turn session. They share source, draft summary, system instructions and known-target list. Only an update task gets the selected old page body, with frontmatter removed. Other old page bodies and the planning response are not delivered to each page task. The plan determines the task set through code. Concept and entity task pools run concurrently; each pool has its own worker limit, default five, so five is not a whole-compilation request cap. Workers catch generation errors into result slots; failed pages are skipped (SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `src/config.ts`).

Code gathers results, strips unknown wikilinks against existing **and planned** targets, writes entities, optionally rewrites the summary, writes concepts, adds related links and reciprocal links, updates `index.md`, then appends an ingest entry to `log.md`. The summary rewrite receives the whitelist, not the newly generated concept/entity bodies. It therefore requests consistency with target names, not a demonstrated semantic comparison with final pages. Terminal success is a resolved void compiler promise, a plugin compiled notice/result or CLI console message, and persistent pages. Partial page-generation failures can still reach terminal success. A later writer failure can leave an earlier subset of writes behind (SRC-1: `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`, `obsidian-plugin/src/compiler-client.ts`).

> const [conceptResults, entityResults] = await Promise.all([
>     conceptTasks.length ? runWithConcurrency(conceptTasks, maxConcurrency) : Promise.resolve([]),
>     entityTasks.length ? runWithConcurrency(entityTasks, maxConcurrency) : Promise.resolve([]),
>   ]);
> --- `src/wiki/compiler.ts`

These per-task message arrays keep unrelated generation output out of a task's context. The task-frame analogy is limited: code retains explicit results, and only those results reach writers; there is no agent stack, automatic compaction or reloadable conversation. Every task still receives full input text. Brief extraction reduces old-page content for planning but enumerates all briefs; no token budget or long-document split is enforced in the inspected short-document compiler. Retained page reloads are the meaningful cross-invocation path, rather than turn-history accumulation (SRC-1: `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/llm.ts`).

### Alternate entry paths and change admission

The watcher subscribes to create/modify events, accepts supported raw files only when watch mode is enabled, and debounces each path for one second. With require-approval enabled, it persists a path/timestamp queue; otherwise it invokes compilation. Approval previews the current file and approves its path, not a frozen content snapshot or proposed generated diff. Reject removes the queue entry but leaves the raw file. Successful compilation removes the entry; a thrown failure leaves it pending. Manual active-file compilation and the CLI do not pass through this approval gate. Settings default to watch and approval enabled; actual deployed settings are unavailable. See [RT-RTE-watcher-approval](#rt-rte-watcher-approval) (SRC-1: `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/approval-modal.ts`, `obsidian-plugin/src/settings.ts`).

Voice ingestion obtains microphone permission from browser/device APIs, records audio, writes the audio into raw storage **before** requesting transcription, and then writes nonempty returned text to a timestamped transcript Markdown file. The watcher handles the transcript like other text if enabled; it does not compile audio itself. A transcription failure can leave audio without a transcript. Send-active-note copies current text into raw, adding a timestamp on collision. Neither acquisition path approves generated wiki content. See [RT-RTE-voice-ingest](#rt-rte-voice-ingest) (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/voice-modal.ts`, `obsidian-plugin/src/stt-client.ts`, `obsidian-plugin/src/utils.ts`).

The optional CLI accepts a path, reads it with Node and passes its basename/content to the shared API. It does not impose plugin raw-folder/extension/approval predicates. The public API accepts supplied storage and content; `compileShortDoc` also accepts a supplied `LlmClient`. Thus shipped caller checks are not universal compiler constraints. `src/wiki/tools.ts` exports filesystem/page/image helpers with separate lexical allowlists, but the inspected compiler routes do not register these as model tools. LLM calls pass model and messages only. Host callbacks, storage adapters and provider implementations are dependencies, not evidence of an additional autonomous tool/delegation path (SRC-1: `src/cli/compile.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts`, `src/wiki/tools.ts`, `src/llm/client.ts`).

The model proposes retained knowledge changes; code admits structurally acceptable output without per-page human review. Update prompts request full rewrites preserving prior intent; code replaces bodies. Stored instructions can be edited by the operator and are loaded next compilation without rebuilding, but no compiler path writes those instructions itself. Settings changes select endpoints/models/language and persist immediately. Maintainers change code and publish tag-triggered builds; users install the bundle. These are separate authority paths, [RT-RTE-instruction-settings](#rt-rte-instruction-settings) and [RT-RTE-release-build](#rt-rte-release-build), not model-driven product improvement (SRC-1: `templates/wiki/AGENTS.md`, `src/wiki/schema.ts`, `src/wiki/page-writer.ts`, `obsidian-plugin/src/settings-tab.ts`, `.github/workflows/release.yml`, `README.md`).

### Guarantees and forcing cases

Four source-supported forcing cases qualify the load-bearing promises:

1. **Approval enabled, manual command or CLI:** the watcher gate does not cover these routes. Owner: plugin event handler. Enforcement: `handleRawFileDetected`. Strength: policy for watcher-triggered compilation, not a universal admission invariant. External contract: Obsidian events and plugin data persistence. implementation conclusion status: wired. operation conclusion status: uninspected (SRC-1: `obsidian-plugin/src/main.ts`, `src/cli/compile.ts`).
2. **Planned page generation fails:** `knownTargets` contains all planned slugs before results succeed. The stripper enforces membership/canonicalization in that set, not actual eventual target existence. Owner: compiler. Enforcement: `stripGhostWikilinks` before generated-body writes. Strength: invariant relative to the passed whitelist; no graph-integrity guarantee. Existing/manual content and metadata paths are not globally scanned. External contract: storage listings/existence. implementation conclusion status: wired. operation conclusion status: uninspected (SRC-1: `src/wiki/compiler.ts`, `src/wiki/wikilink.ts`).
3. **Existing human-edited page chosen for update or create:** update reads and rewrites the body; create can address an existing sanitized filename without the update preservation branch. No diff/conflict gate intercepts these writes. The template's conflict instruction has only model-mediated policy force. Owner: model for requested preservation, code for replacement. Enforcement: prompt only for meaning; writer for physical replacement. Strength: policy/best effort, not an invariant. External contract: model compliance. implementation conclusion status: wired for rewriting. preservation conclusion status: claimed. operation conclusion status: uninspected (SRC-1: `templates/wiki/AGENTS.md`, `src/wiki/prompts.ts`, `src/wiki/page-writer.ts`).
4. **Concurrent documents or failed later write:** per-path `inFlight` does not lock common concept/entity/index/log files, distinct input paths can have the same basename, and writes are not a multi-file transaction. Owner: caller/storage. Enforcement: in-memory set and adapter write methods. Strength: best effort for duplicate same-path plugin work; Node temp-file rename is per-file, not whole-ingest durability. Vault storage delegates modify/create to Obsidian. Required external contracts: filesystem rename semantics, absence of symlink escape/racing writers for lexical-root confinement, host vault behavior. implementation conclusion status: wired. deployment conclusion status: uninspected. operation conclusion status: uninspected (SRC-1: `obsidian-plugin/src/main.ts`, `src/storage/node-storage.ts`, `obsidian-plugin/src/vault-storage.ts`, `src/wiki/frontmatter.ts`).

> if (this.settings.requireApproval) {
>       await this.addPendingItem(path);
>       return;
>     }
>     await this.compileRawPath(path);
> --- `obsidian-plugin/src/main.ts`

> ...[...plannedSlugs].map((slug) => `concepts/${slug}`),
>     ...[...entityPlanned].map((slug) => `entities/${slug}`),
> --- `src/wiki/compiler.ts`

> - Do not silently overwrite manually edited wiki pages — surface conflicts instead.
> --- `templates/wiki/AGENTS.md`

> await frontmatter.atomicWriteText(storage, relativePath, fmBlock + '\n' + cleanBody);
> --- `src/wiki/page-writer.ts:70-85`

The last quote's identical writer statement occurs in both concept and entity branches; its checked scope is the concept branch below in the route evidence. No universal atomic guarantee follows from the helper's name: it delegates to `storage.writeText`, Node uses rename, and Vault uses host modify/create. Node checks lexical resolved paths, not realpaths. Capability surface is host vault/file access plus model/STT network calls; effective grants are configured credentials, storage root and host permissions. Actual keys, service ACLs, host filesystem isolation and sandboxing are not supplied. Source-local folder predicates cannot establish a deployed isolation envelope (SRC-1: `src/storage/node-storage.ts`, `obsidian-plugin/src/vault-storage.ts`, `src/wiki/frontmatter.ts`, `src/llm/client.ts`, `obsidian-plugin/src/stt-client.ts`).

Recovery consists of thrown-error notices, resetting `inFlight` in `finally`, retaining failed approved queue items, skipping individual failed generation tasks, and fallback summary handling for empty/unparseable plans or failed rewrites. There is no whole-compilation rollback in these inspected paths. Re-running recomputes from current input and wiki rather than resuming a checkpoint. Status/log messages expose progression, not page-quality measurement; connection probes accept returned text without checking that LLM response equals the requested `OK`. Performance, reliability and knowledge benefit remain unmeasured (SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/settings-tab.ts`, `src/llm/client.ts`).

Inspection added no sources beyond SRC-1. This report directly inspected the compiler, parsers, prompts, readers/writers, both storage implementations and contract, API, CLI, model client/config, all operational plugin paths, settings UI, instruction template, README, root package, plugin bundling and release workflow. No target execution occurred. Provider internals, actual vault/settings/queue, host concurrency and release execution remain unobserved; these prevent outcome, deployed isolation and version-reproducibility conclusions, not the implementation traces above.

## Shared records

### Components

#### RT-CMP-llm-model
Label: Configured chat model

Identity: model selected by `llmModel`, accessed through `createOpenAI(...).chat(parseModelId(model))`. Form: distributed-parametric at the remote service; messages/results are natural-language text with requested symbolic JSON envelopes. Substrate: opaque provider infrastructure, not the local wiki. Parameters changing during operation: uninspected — no local training/update interface, provider internals excluded. Exact model version pinned: no; a configurable identifier defaults to `openai/gpt-5-mini`, not an immutable weight revision. Mutable endpoint resolving to another model: possible through editable base URL/model and remote routing; actual mapping uninspected. Evidence: SRC-1 `src/config.ts`, `src/llm/client.ts`, `obsidian-plugin/src/settings-tab.ts`.

> return openai.chat(parseModelId(model));
> --- `src/llm/client.ts`

> const { text } = await generateText({ model, messages });
> --- `src/llm/client.ts`

#### RT-CMP-stt-model
Label: Configured transcription model

Identity: configured `sttModel`, default `whisper-1`, sent to `/audio/transcriptions`. Form: distributed-parametric service computation; actual numerical implementation opaque. Substrate: remote service. Parameter changes during operation: uninspected provider internals. Exact version pinned: no immutable revision. Mutable endpoint resolution: editable base URL/model can select another service; provider alias changes uninspected. Evidence: SRC-1 `obsidian-plugin/src/settings.ts`, `obsidian-plugin/src/stt-client.ts`.

> form.append('model', model);
> --- `obsidian-plugin/src/stt-client.ts`

### Operative objects

#### RT-OBJ-agents
Label: Wiki compilation instructions

Identity: wiki-root `AGENTS.md`, with `DEFAULT_AGENTS_MD` fallback. Form: natural-language instructions interpreted by model. Substrate: WikiStorage text file or shipped TypeScript string. Operator edits are not compiler-generated updates. Consumer and authority: [RT-BAP-compiler-instructions](#rt-bap-compiler-instructions). Evidence: SRC-1 `src/wiki/schema.ts`, `src/wiki/compiler.ts`, `templates/wiki/AGENTS.md`.

> const content = await storage.readText('AGENTS.md');
>   return content ?? DEFAULT_AGENTS_MD;
> --- `src/wiki/schema.ts`

#### RT-OBJ-pending-queue
Label: Pending compilation queue

Identity: pluginData `pendingQueue` of `{path, addedAt}`. Form: symbolic entries with fixed code consumers. Substrate: plugin saved data alongside settings, reloaded by `loadSettings`. It contains identifiers/timestamps, not frozen input bodies or generated-page candidates. Evidence: SRC-1 `obsidian-plugin/src/settings.ts`, `obsidian-plugin/src/main.ts`.

> this.pluginData.pendingQueue.push({ path, addedAt: Date.now() });
>     await this.saveSettings();
> --- `obsidian-plugin/src/main.ts`

### Routes

#### RT-RTE-document-compile
Label: Document compilation and wiki admission

Endpoints/progression: plugin manual command or CLI/API input → summary → model plan → page task results → code-managed Markdown/frontmatter/link writes → index/log. Next-step owner is compiler code; model decides plan entries and generated content. Natural-language source/instructions/page bodies and symbolic JSON task plan are distinct consumption forms. Writes use host-granted storage; credentials authorize remote chat. SRC-1: `obsidian-plugin/src/main.ts`, `src/cli/compile.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compiler/API resolve void; plugin adapter returns docName/status compiled, plugin/CLI report completion after log append; thrown failures report error.
- Later read-back: Generated concept/entity descriptions feed later planning; model-selected update bodies feed later generation; humans browse summary/index/links in Obsidian.
- Delegated visibility: Chat provider receives explicit message arrays including full source, draft summary and selected retained context; no generated-page review is delegated to a second critic.
- Selection predicate: Model plan names create/update/related entries from all supplied briefs; code filters shapes/types and existing related pages, then loads update bodies by sanitized names.
- Invalidation or expiry: No scheduled expiry; compilation can replace bodies and descriptions. Old body is not retained as a compiler checkpoint.
- Activation or effect: Code wires outputs to persistent writes and later model input; changed downstream model behavior and benefit are unobserved.
- Evidence limits: No actual compilation, wiki, model result or host storage trace supplied; source demonstrates requests and admission, not faithful synthesis.

Admission: user chooses problem/input in manual mode; watcher can initiate automatically. Model proposes page selection and content; code decides eligibility and persists. Human veto is upstream via watcher queue, not per output. Model cannot invoke arbitrary tools through this client. Answer oracle: none used by this route; existing text/source are context, not expected-answer evaluation. Operating mode: open document requests, not bounded experiments/curricula. Trigger: input compile invocation. Proposed change: summary/concept/entity bodies, descriptions and links. Rejection: malformed plan fallback, filtered items, empty generation failure, unknown-link removal; malformed page JSON can fall back to raw text. Recovery: fallback/skip/re-run; no transaction rollback. Guidance: schema, source, prior selected page and prompts; pages/index/log persist, prompt-call working state does not (SRC-1: `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `src/wiki/prompts.ts`).

> if (result instanceof Error) {
>       console.warn(`  Concept generation failed: ${result.message}`);
>       continue;
>     }
> --- `src/wiki/compiler.ts`

> return { brief: '', content: raw, obj: null };
> --- `src/wiki/llm.ts`

> await frontmatter.atomicWriteText(storage, relativePath, fmBlock + '\n' + cleanBody);
> --- `src/wiki/page-writer.ts:70-85`

#### RT-RTE-watcher-approval
Label: Watcher detection and human approval

Endpoints/progression: vault create/modify event → per-path debounce → requireApproval branch → persisted queue or immediate compiler → user approve/reject. Code owns detection and branching; user decides queued-item admission. SRC-1: `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/approval-modal.ts`, `obsidian-plugin/src/settings.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Event callback schedules work; queue insertion gives notice; approve invokes compilation; reject removes queue entry.
- Later read-back: Pending paths reload from plugin data on load and are displayed for later approval; current source content is read at compile time.
- Delegated visibility: Preview opens the file in Obsidian; approval sends current text through the compiler to chat service.
- Selection predicate: TFile under raw folder with md/txt/markdown extension, watch enabled; one-second debounce and same-path inFlight guard; approval depends on setting.
- Invalidation or expiry: Successful pending compilation or reject removes entry; no timed expiry; raw source remains.
- Activation or effect: Queued approval enables compilation; no evidence that user reviewed a particular body or generated diff.
- Evidence limits: Actual queue, user decisions, restarts and races unobserved; manual/CLI bypass this gate.

Admission: user proposes source content or another vault writer supplies it; code admits detection; human may approve/reject queued path, or configured automatic mode invokes compilation. No answer oracle. Mode: open event-driven requests. Guidance: folder/extension/settings, not content-quality criteria. Proposed change is source admission to compilation, then downstream knowledge writes via [RT-RTE-document-compile](#rt-rte-document-compile). Recovery: thrown compile leaves pending item; inFlight clears in finally; rejection is queue removal, not rollback of generated content.

> await this.compileRawPath(path);
>     await this.removePendingItem(path);
> --- `obsidian-plugin/src/main.ts`

#### RT-RTE-voice-ingest
Label: Voice capture and transcript admission

Endpoints/progression: user record/stop → device microphone/MediaRecorder → raw audio write → STT request → transcript raw Markdown → watcher or later manual compile. Owners: user for record/stop, browser for permission/device, plugin for storage/request, STT provider for transcription. SRC-1: `obsidian-plugin/src/voice-modal.ts`, `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/stt-client.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Saved audio/transcript and notice on success; failure notice/status on transcription failure.
- Later read-back: Raw transcript is read by a later manual or watcher-triggered compilation; audio reload to compiler is inapplicable — compiler ingests text.
- Delegated visibility: Provider receives audio filename, model and Blob; transcript becomes vault-visible natural-language content.
- Selection predicate: User records/stops; nonempty returned text required; watcher accepts resulting transcript extension if enabled.
- Invalidation or expiry: No automatic deletion/expiry; failed STT may leave audio file.
- Activation or effect: Transcript writing triggers eligible vault event; subsequent model behavior remains unobserved.
- Evidence limits: No microphone session, audio, transcript or provider response supplied.

Admission: human starts/stops recording; service proposes transcript; software accepts nonempty text without transcript confirmation. Device permission can veto capture; requireApproval can gate later compilation, not STT network transfer. No answer oracle; open voice requests. Guidance: configured model/service and raw naming; audio and transcript persist. Recovery: device cleanup and failure notice; no audio rollback (SRC-1: `obsidian-plugin/src/voice-modal.ts`, `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/stt-client.ts`).

> await this.app.vault.createBinary(audioPath, arrayBuffer);
> --- `obsidian-plugin/src/main.ts`

> if (!payload.text?.trim()) {
>     throw new Error('STT returned empty transcript');
>   }
> --- `obsidian-plugin/src/stt-client.ts`

#### RT-RTE-instruction-settings
Label: Operator instruction and runtime configuration changes

Endpoints/progression: operator edits stored AGENTS.md or settings UI → storage/saveData → next compile loads instructions/config → provider and prompt selection. Owners: human proposal/decision, plugin persistence, compiler loading. Natural-language instructions differ from symbolic settings. SRC-1: `templates/wiki/AGENTS.md`, `src/wiki/schema.ts`, `src/wiki/compiler.ts`, `obsidian-plugin/src/settings-tab.ts`, `obsidian-plugin/src/main.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Settings callbacks save plugin data; instruction editing is an external host file operation.
- Later read-back: loadSettings reloads settings; each compilation reads AGENTS.md and uses current language/model/base URL/key.
- Delegated visibility: AGENTS.md is interpolated into system-role content; selected service receives compilation messages; credentials are sent through client authentication.
- Selection predicate: Stored AGENTS.md if non-null, otherwise fallback; explicitly configured settings and API arguments/environment select service/config.
- Invalidation or expiry: Replacement/edit changes later load; no version history or expiry in target code.
- Activation or effect: Different inputs/endpoints are wired to later calls; obedience to changed prose or improved output unobserved.
- Evidence limits: No actual edited instructions/settings or subsequent run supplied; host editing and provider internals excluded.

Admission: human chooses changes; software persists settings with field-specific trimming/defaults, loads instructions without semantic approval. Human can decline edits or replace previous values; no automatic rollback. No answer oracle or improvement trigger/evaluator; mode is open operator configuration. Guidance: template and UI descriptions; changes persist as instructions/settings, not trained parameters. Compilation does not revise its own AGENTS.md in this inspected route.

> role: 'system',
>     content: formatTemplate(SYSTEM_TEMPLATE, { schema_md: schemaMd, language }),
> --- `src/wiki/compiler.ts`

#### RT-RTE-release-build
Label: Maintainer build and release admission

Endpoints/progression: maintainer code/version/tag changes → GitHub tag push workflow → dependencies/build → release assets → external user installation. Owners: maintainer, GitHub Actions runner and installing user. Symbolic code/build configuration; substrate Git and release artifacts. SRC-1: `.github/workflows/release.yml`, `obsidian-plugin/esbuild.config.mjs`, `README.md`, `package.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Workflow is configured to create a tagged release with main.js, root manifest and plugin stylesheet.
- Later read-back: inapplicable — build consumes source/dependencies, not artifacts accumulated through compilation use.
- Delegated visibility: GitHub runner gets checkout and release token; user/Obsidian loads installed bundle, outside observed execution.
- Selection predicate: Push of any tag; plugin bundle aliases @echowiki to shared src and externalizes obsidian.
- Invalidation or expiry: New release/install can replace product; no target-managed rollback protocol shown.
- Activation or effect: Build/release path is configured; actual publication, installation and activation unobserved.
- Evidence limits: No release execution or published bundle supplied; transitive dependencies and host installation not audited.

Admission: maintainer proposes/accepts code/tag; build can fail; installing user chooses deployment. No model proposal or answer oracle; no quality test step in this workflow, root test script is a placeholder. Mode: maintainer release requests, not experimental improvement. Guidance: README version/install procedure and build configuration; code/artifacts persist. Recovery: revert/rebuild/reinstall are operator possibilities, not automated rollback in the inspected workflow.

> tags:
>       - '*'
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-conflict-policy
Label: Manual-edit conflict preservation policy

Claimed operation: template requests that manual edits not be silently overwritten, but compiler/writers provide full-body replacement without conflict detection. It is instruction doctrine, not an enforced human-edit veto. SRC-1: `templates/wiki/AGENTS.md`, `src/wiki/prompts.ts`, `src/wiki/page-writer.ts`. Supporting passage and forcing case are retained above; [RT-RTE-document-compile](#rt-rte-document-compile) identifies actual admission.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-compiler-instructions
Label: Stored instructions to compiler model

Consumer: chat model at each compilation call. Channel: stored/fallback AGENTS.md interpolated into system-role natural-language message. Force: requested model behavior, not verified obedience or permission enforcement. Horizon: across later compilations while stored file remains. Editing does not require product rebuild. Evidence: SRC-1 `src/wiki/schema.ts`, `src/wiki/compiler.ts`, `src/wiki/prompts.ts`; minimum passages in [RT-OBJ-agents](#rt-obj-agents) and [RT-RTE-instruction-settings](#rt-rte-instruction-settings).

#### RT-BAP-retained-pages
Label: Retained pages to later planning and rewriting

Consumer: planning model and selected update-generation model. Channel: all concept/entity briefs enter planning user content; model-selected prior body enters update user content. Force: contextual knowledge and continuity request, not fixed-rule authority or reliable preservation. Horizon: subsequent document compilations while pages remain. Current source can supplement or displace prior prose through model generation and code replacement. Evidence: SRC-1 `src/wiki/briefs.ts`, `src/wiki/compiler.ts`, `src/wiki/prompts.ts`.

> const conceptBriefs = await readConceptBriefs(storage);
>   const entityBriefs = await readEntityBriefs(storage);
> --- `src/wiki/compiler.ts`

> Current content of this page:
> {existing_content}
> --- `src/wiki/prompts.ts:70-83`

## Annotations

none
