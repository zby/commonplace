---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Letta Code memory: committed local projections, deferred and skill reads, transcript compaction, reflection integration and hosted/shared-memory limits."
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
source-identity: "https://github.com/letta-ai/letta-code"
reviewed-boundary: "271f119dcf37d58649a18e6c733386b3c710a456"
---

# Letta Code memory report

## Boundary and evidence

The memory scope follows the supplied runtime's foreground history/prompt route, auxiliary compaction call and background memory workers. It also includes shipped CLI, listener, hook and shared-repository alternatives. All added evidence is SRC-1 implementation or doctrine/design at the boundary's frozen commit. Direct reads below supplement, rather than merely repeat, [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript) and [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task). No target or tests were executed.

External Letta service state, embedding pipelines, providers and live user memories remain outside the captured source. Code's service requests are included; their successful acceptance, internal persistence and later server selection are not established. Static bundled skills and instructions are guidance for memory operations, not themselves read-back accumulated through use. Package replacement and executable mods remain the runtime's separate change routes. Dynamic project/global skill content is uncaptured. These exclusions prevent an end-to-end quality, privacy, learning-benefit or hosted-memory guarantee.

### Coverage inventory

Paths in this table are SRC-1 commit-relative anchors. “Direct” means this worker read implementation text or bounded implementation ranges; “supplied” means runtime evidence. Uninspected means available source remains, not an access failure.

| Entry/operation | Inspected path and layer | Coverage and prevented conclusion |
|---|---|---|
| CLI dispatch | Direct `src/cli/subcommands/router.ts`, implementation | Dispatches memory/memfs, shared-memory, messages and skills; routes below cover material memory paths. |
| Fresh local agent memory and Git initialization | Direct `src/backend/local/initial-memory.ts`, `src/agent/memory-git.ts`, implementation | [MEM-RTE-memory-admission](#mem-rte-memory-admission); creation-body authorship is unresolved, not assumed human. |
| Commit policy and budgets | Direct `src/agent/memory-git-hooks.ts`, `src/agent/memory-constraints.ts`, `src/memory-constraints.ts`, `src/memory-frontmatter.ts`, implementation | [MEM-OBJ-memory-constraints](#mem-obj-memory-constraints), [MEM-RTE-memory-admission](#mem-rte-memory-admission); no universal non-bypassable gate. |
| Core compilation and revision changes | Direct `src/backend/local/system-prompt-compilation.ts`, `src/agent/memory-format.ts`, `src/backend/local/local-backend.ts`, implementation; supplied provider consumer | [MEM-RTE-core-projection](#mem-rte-core-projection), [RT-BAP-provider-context](runtime.md#rt-bap-provider-context). |
| Registered deferred tool, ordinary Read/Bash alternatives | Direct `src/tools/impl/memory.ts`; registration search in `src/tools/manager.ts`, implementation | [MEM-RTE-deferred-read](#mem-rte-deferred-read); ordinary file tools need not obey projection selection. Their grants are supplied runtime findings. |
| Skill discovery and invocation | Direct ranges of `src/agent/client-skills.ts`, `src/agent/shared-memory-skills.ts`, `src/tools/impl/skill.ts`, `src/headless.ts`, implementation | [MEM-RTE-skill-loading](#mem-rte-skill-loading); all discovery precedence and UI injection branches not exhaustively audited. |
| Raw history and compaction | Direct ranges of `src/backend/local/local-store.ts`, `src/backend/local/local-backend.ts`, `src/backend/local/compaction.ts`; supplied transcript/model records | [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-RTE-transcript-compaction](#mem-rte-transcript-compaction); session replay internals remain uninspected. |
| Recall/message search | Direct `src/backend/message-search.ts`, bounded `src/backend/local/transcript-search.ts`, `src/backend/conversation-search.ts`; caller search in `src/cli/subcommands/messages.ts` | [MEM-RTE-transcript-search](#mem-rte-transcript-search); ranking algorithm and every exported API caller not fully read. |
| Automatic/manual and multi-conversation reflection | Direct `src/cli/helpers/post-turn-reflection.ts`, bounded `src/cli/helpers/reflection-transcript.ts`, `src/cli/helpers/reflection-launcher.ts`, `src/cli/helpers/reflection-completion.ts`; doctrine `src/agent/subagents/builtin/reflection-v2.md` | [MEM-RTE-reflection-integration](#mem-rte-reflection-integration); normalization dependency and complete conversation-selection machinery not inspected. |
| Merge, rejection and cleanup; generic memory workers | Direct ranges/search in `src/agent/memory-worktree.ts`, direct `src/cli/helpers/reflection-integration.ts`, implementation/design | Reflection route below; generic worker integration is distinguished in Write side, not assigned reflection's stricter gate. |
| Paired reflection arena | Direct finalize range and bounded search in `src/cli/helpers/reflection-arena.ts`, implementation | [MEM-RTE-arena-selection](#mem-rte-arena-selection); candidate launch, human UI response provenance and uploaded feedback consumers not fully traced. |
| Shared attach/detach, clean-commit sync, optional mirror | Direct `src/cli/subcommands/shared-memory.ts` ranges, `src/agent/attached-repositories.ts`, `src/agent/attached-repository-git-sync.ts` ranges, `src/reminders/memory-git-sync.ts`, `src/agent/memory-git.ts`, `src/agent/memory-git-hooks.ts`, implementation | [MEM-RTE-repository-sync](#mem-rte-repository-sync); server non-skill prompt projection is opaque. |
| Listener list/read/ref/diff/write/delete | Direct write range and bounded dispatch search in `src/websocket/listener/commands/memory.ts`, implementation | Admission route below. Delete commit wiring is visible by search; complete delete validation and rollback behavior are uninspected. Ref/history views afford inspection, not autonomous later adoption. |
| Conflict/invalid-history repair | Direct sync caller; bounded search of `src/agent/memory-conflict-repair.ts`, implementation | Claim state suppresses duplicate attempts; repair launcher and worker's precise content edits remain uninspected, preventing a complete repair/admission-quality conclusion. |
| Cloud reflection progress and hosted memory | Direct completion client; supplied `src/backend/backend.ts` findings | [MEM-OBJ-hosted-memory](#mem-obj-hosted-memory); external payload/storage/selection unknown. |
| Initialization, migration, curation skills and evaluators | Boundary inventories `src/skills/builtin/initializing-memory/SKILL.md`; this worker searched memory/compaction/reflection test paths but did not read/run all tests or maintenance skills | Available guidance/evaluators remain uninspected; no complete import provenance, migration semantics or passing-evaluator conclusion. |
| Hooks, exported library methods, installed extensions | Direct MemFS hooks and `commitMemoryWrite`; supplied executable-extension/hook runtime | Arbitrary external callers and installed hook content are uncaptured. API existence alone does not establish a later memory consumer. |

## Core ideas

1. **Commit selection and model interpretation are different controls.** Local core compilation uses Git HEAD, not filesystem dirty bytes. Root-layout Markdown becomes always-supplied context; child indexes become directory pointers. Neither the compiler nor the commit validator proves the truth of a remembered assertion. [MEM-RTE-core-projection](#mem-rte-core-projection), [MEM-RTE-memory-admission](#mem-rte-memory-admission).
2. **There are multiple read-back forms.** History is loaded automatically; core memory is pushed with a turn; deferred memory is requested by a path; skills have metadata discovery followed by full-content injection. The latter routes read files rather than necessarily the committed snapshot. A single “only commits affect context” slogan is therefore too broad. [MEM-RTE-deferred-read](#mem-rte-deferred-read), [MEM-RTE-skill-loading](#mem-rte-skill-loading).
3. **Trace retention and trace-derived memory are separate.** Compaction replaces the active history projection with a summary plus a retained tail. Reflection instead proposes edits to agent memory/skills and integrates them through Git. Raw transcript retention alone establishes neither transformation. The summary and edited files can reach later model calls; exercised quality gains are not supplied. [MEM-RTE-transcript-compaction](#mem-rte-transcript-compaction), [MEM-RTE-reflection-integration](#mem-rte-reflection-integration).
4. **Rejection affects retry as well as storage.** Failed reflection proposals are cleaned up without successful transcript consumption; verified success advances progress. Shared detach removes discovery eligibility but leaves bytes on disk. Optional mirroring is not the same persistence route as the Letta remote. [MEM-RTE-arena-selection](#mem-rte-arena-selection), [MEM-RTE-repository-sync](#mem-rte-repository-sync).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-core-memory
Label: Committed MemFS core memory

Source-native identity: root Markdown including `MEMORY.md` in memfs-v2; legacy `system/` Markdown in memfs-v1. Storage: per-agent local Git repository/filesystem and, for API-backed agents, a remote repository contract. Form: natural-language bodies; path and frontmatter metadata are symbolically selected, while descriptions also supply model-readable discovery cues. Lineage: initial create-body blocks, ordinary edits, imported remote history or integrated worker changes. Initial block author/prior derivation is unresolved. Distinct from the transcript container and the compiled delivery route within [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn). SRC-1: `src/backend/local/initial-memory.ts`, `src/agent/memory-format.ts`, `src/backend/local/system-prompt-compilation.ts`.

> if (format === "memfs-v2") return !normalized.includes("/");
> --- `src/agent/memory-format.ts`

The compiler removes frontmatter and renders body text; root `MEMORY.md` and other root files enter core memory. Moving text into a child directory changes automatic delivery; a label such as `ARCHIVE.md` does not exclude a root file from core consumption.

#### MEM-OBJ-deferred-memory
Label: Deferred MemFS files and indexes

Source-native identity: child-directory `MEMORY.md` indexes and deeper files. Storage: same Git checkout, but a distinct operative part because automatic core and requested file consumers differ. Natural-language indexes/content coexist with symbolic path structure. Projection eligibility requires ancestor indexes; the Memory tool's direct filesystem reads do not enforce that entire committed-tree predicate. Current working-tree bytes can therefore differ from committed core context. No supplied record is the same referent; closest is [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn). SRC-1: `src/agent/memory-format.ts`, `src/tools/impl/memory.ts`.

> if (!allPaths.has(`${current}/MEMORY.md`)) return false;
> --- `src/agent/memory-format.ts`

#### MEM-OBJ-agent-skills
Label: Agent and attached-repository skills

Source-native identity: `skills/<name>/SKILL.md` and companion resources. Storage: agent/shared/project/global files; bundled static skills are an additional source, not trace-derived memory. Body text is natural-language procedure; executable companion scripts are distinct symbolic behavior when actually invoked. Name/description/path/source records are access metadata, not the full procedure. Reflection may generate or revise agent skill content from transcripts; other acquisition provenance is uncaptured. Closest supplied route is [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), not an identical skill referent. SRC-1: `src/agent/client-skills.ts`, `src/tools/impl/skill.ts`, `src/agent/subagents/builtin/reflection-v2.md`.

> const sortedSkills = discovery.skills.filter(isModelInvocableSkill);
> --- `src/agent/client-skills.ts`

#### MEM-OBJ-memory-constraints
Label: MemFS admission constraints

Source-native identity: `.memfs.config.json`, installed pre-commit hook and trusted layout policy. Storage: tracked JSON policy plus hook/common-Git metadata; symbolic consumer rules. Default root-layout budgets are depth 2, per-file 20,000 characters and aggregate core 65,536 characters; overrides and read-only globs are supported. Character caps are not provider token guarantees. This is distinct from [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context), which carries execution grants rather than memory-tree policy. SRC-1: `src/memory-constraints.ts`, `src/agent/memory-constraints.ts`, `src/agent/memory-git-hooks.ts`.

> maxDepth: 2,
>     maxFileCharacters: 20_000,
>     maxCoreMemoryCharacters: 65_536,
> --- `src/memory-constraints.ts`

The hook requires a machine-readable authorization environment value for policy edits; the error's phrase “human approval” does not authenticate who supplied that value.

#### MEM-OBJ-compaction-summary
Label: Retained local compaction summary

Part of: [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript)

Source-native identity: `summaryMessage`, its text and `metadata.compaction.summary`. Storage: resident projection and JSONL compaction entry; natural-language derived text inside symbolic IDs, role, stats and kept-entry metadata. Raw messages are not interchangeable with this lossy summary. The stored message uses role `user` although its text wraps a `system_alert`; authority is model-interpreted history, not an independent host policy. SRC-1: `src/backend/local/local-store.ts`, `src/backend/local/compaction.ts`.

> const compactedMessages = [
>       summaryMessage,
>       ...(input.remainingMessages ?? []).map(cloneLocalMessage),
>     ];
> --- `src/backend/local/local-store.ts`

#### MEM-OBJ-reflection-payload
Label: Reflection transcript payload and progress

Source-native identity: normalized transcript slice files, multi-transcript manifest and per-conversation reflection state. Storage: local files with locked state updates. Transcript prose is evidence supplied to a model; manifest/checkpoint fields are symbolic selectors and retry state. Lineage is conversation capture followed by range selection and normalization, not necessarily a full provider transcript. Mixed original inputs include user, assistant and tool activity. Payload bounds and partial normalization prevent a complete-evidence claim. This is distinct from the generic background output in [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task). SRC-1: `src/cli/helpers/reflection-transcript.ts`.

> sourceContext: { partial: true },
>     bounds: {
>       toolArguments: { maxCharacters: null },
>     },
>     filters: { toolResults: "include" },
> --- `src/cli/helpers/reflection-transcript.ts`

#### MEM-OBJ-hosted-memory
Label: Hosted and attached memory contracts

Source-native identity: external agent memory/repositories and conversation state addressed by the API backend and attachment list. Storage, internal encoding, initial/embedding lineage and server-side selectors are opaque in SRC-1; readable local mounts and API response metadata do not reveal the entire payload. Local mounted text and skills are covered separately. Closest supplied route is [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn); this object names external retained state rather than redeclaring that client route. SRC-1: `src/agent/attached-repositories.ts`, `src/cli/subcommands/shared-memory.ts`; hosted inference limits also follow the supplied runtime.

> .filter(
>       (repository) => !repository.is_primary && repository.name !== "memory",
>     )
> --- `src/agent/attached-repositories.ts`

### Routes

#### MEM-RTE-memory-admission
Label: Memory authoring and commit admission

Distinct from [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn): this route admits retained files rather than client tool effects. Endpoints: creation-body/file/tool/listener producer → working-tree bytes → staged tree → installed hook checks → Git commit. Owner: producer for content, Git/hook for commit acceptance. SRC-1: `src/backend/local/initial-memory.ts`, `src/agent/memory-git.ts`, `src/agent/memory-git-hooks.ts`, `src/websocket/listener/commands/memory.ts`.

- Immediate return: commit/no-change result and SHA, or error; listener can already have written bytes before a commit failure.
- Later read-back: committed core enters compilation; deferred/skill file reads can independently consume checkout bytes.
- Delegated visibility: workers receive scoped memory directories; listener request supplies content/path and optional reason.
- Selection predicate: local initialization converts supplied blocks to root files; commits stage explicit pathspecs; v2 hook validates full staged memory tree, excluding skill bodies from memory frontmatter rules.
- Invalidation or expiry: later edit/delete/merge replaces active content; Git retains historical commits. Commit rejection does not establish rollback of working-tree bytes.
- Activation or effect: admitted committed text can reach later prompt compilation; direct reads have a different admission boundary.
- Evidence limits: hooks constrain form/budgets/protected paths, not semantic accuracy; direct Git/remote writes and bypassable local hooks prevent a universal guarantee. Caller content authorship is unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller or model proposes content; software rejects invalid layout/frontmatter/budgets and protected changes. Human initiation is not per-content review. Policy-edit authorization is `LETTA_MEMORY_CONSTRAINTS_UPDATE=1`, not proof of human approval. Operating mode: open memory editing, not an expected-answer experiment. Answer oracle: inapplicable — validators test structural policy, not correctness. Guidance: layout/metadata contracts plus model instructions; persisted result is committed text, not a guaranteed warrant.

> if (configChanged && process.env[CONFIG_UPDATE_ENV] !== "1") {
>     errors.push(
>       CONFIG_PATH + " is protected and requires human approval to change",
>     );
>   }
> --- `src/agent/memory-constraints.ts`

#### MEM-RTE-core-projection
Label: Automatic committed core projection

Part of: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Endpoints: agent/conversation turn → committed tree selector → compiled prompt/cache or memory-update message → provider context. Owner: local backend/compiler. Input is [MEM-OBJ-core-memory](#mem-obj-core-memory); no separate automatic semantic relevance ranker is established. SRC-1: `src/backend/local/system-prompt-compilation.ts`, `src/backend/local/local-backend.ts`; downstream consumer is [RT-BAP-provider-context](runtime.md#rt-bap-provider-context).

- Immediate return: compiled text, core memory, hash/revision and compilation time.
- Later read-back: future turn reloads committed core; unchanged raw prompt with new memory revision delivers a mid-conversation memory update while retaining original compiled content.
- Delegated visibility: model gets selected bodies and directory pointers, not every deferred file or Git rationale.
- Selection predicate: local MemFS enabled, committed HEAD, Markdown path/layout; v2 root files and child-index directory references versus v1 system bodies/external tree.
- Invalidation or expiry: raw-system hash or committed revision changes cache use; explicit recompile and compaction also compile. Unreadable committed files are skipped best-effort.
- Activation or effect: automatic delivery is wired; compliance and resulting action changes are unobserved.
- Evidence limits: compiler selection is not truth assessment; hosted compiler behavior and a global provider-token cap are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const raw = gitOutput(memoryDir, ["show", `HEAD:${relativePath}`]);
> --- `src/backend/local/system-prompt-compilation.ts`

No separate semantic budget clips core text here; admission budgets and provider context pressure are different controls. The v2 compiler supplies top-level directory pointers, not the full deferred descriptions claimed by some reflection guidance.

#### MEM-RTE-deferred-read
Label: Requested deferred memory read

Distinct from automatic projection within [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn). Endpoints: model-proposed Memory(path) → registered scoped tool → filesystem content/listing → tool result → continuation model. Owner: tool implementation and ordinary runtime execution policy. SRC-1: `src/tools/impl/memory.ts`, `src/tools/manager.ts`.

- Immediate return: selected file body or directory index plus direct-child metadata; errors for root, skills, traversal, unavailable, oversized or binary targets.
- Later read-back: subsequent invocation requests stored content; returned text also joins conversation context.
- Delegated visibility: model receives bounded readable text/descriptions and absolute fallback paths, not every descendant's content.
- Selection predicate: active v2 directory and supplied relative path; directory children sorted by latest edit then name and capped by MEMORY_MAX_ENTRIES. This is path selection, not semantic retrieval.
- Invalidation or expiry: latest filesystem state is read; moves/deletes invalidate paths; no HEAD-based cache used here.
- Activation or effect: bounded file delivery is wired; automatic adoption or correct interpretation is unobserved.
- Evidence limits: ordinary Read/Bash can be alternative consumers; canonical projection membership and committed status are not this tool's full read predicate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const content = readFileSync(fullPath, "utf8").trimEnd();
> --- `src/tools/impl/memory.ts`

Budgets include Read line/per-line/total-character caps, entry cap, a 10 MiB file ceiling and binary-prefix check. These can omit content; fallback instructions tell the agent to use Read ranges.

#### MEM-RTE-skill-loading
Label: Metadata discovery and requested skill loading

Distinct from [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task): no child is required to interpret this procedure. Endpoints: eligible skill discovery → client metadata/available-skills block → model selects name → Skill tool reads/rendered body → queued user-message injection → next model request. SRC-1: `src/agent/client-skills.ts`, `src/agent/shared-memory-skills.ts`, `src/tools/impl/skill.ts`, `src/backend/local/system-prompt-compilation.ts`, `src/headless.ts`.

- Immediate return: tool says Launching skill; full content is queued separately when toolCallId is supplied.
- Later read-back: retained skill files are read on invocation and injected as user text; available-skills metadata advertises names/descriptions without full bodies.
- Delegated visibility: loaded body and resource paths reach model; companion resource contents are not eagerly read.
- Selection predicate: invocable skill filter, configured sources/name resolution and active attachment eligibility; local agent IDs do not use shared-memory skill discovery.
- Invalidation or expiry: payload cache generations, source/context changes and explicit invalidation; detach invalidates discovery even though the mount remains on disk.
- Activation or effect: full-content injection is wired in inspected headless path; selecting/loading alone does not prove procedure execution.
- Evidence limits: generic API calls without toolCallId do not get queue injection from this function; all precedence, deprecation handling and UI branches not audited. No provider token budget for the whole rendered body established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> queueSkillContent(toolCallId, wrapSkillContent(skillName, fullContent));
> --- `src/tools/impl/skill.ts`

> text: sc.content,
> --- `src/headless.ts:4291-4295`

#### MEM-RTE-transcript-compaction
Label: Transcript-derived compaction and later continuation

Distinct from [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model), the model component used by this transformation; consumes a part of [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript). Endpoints: manual/pressure compaction → all/sliding-window planner → summary model → packaged summary and retained-tail state → later history consumer. Owner: local backend/planner/store. SRC-1: `src/backend/local/local-backend.ts`, `src/backend/local/compaction.ts`, `src/backend/local/local-store.ts`.

- Immediate return: counts, summary and stats, or error.
- Later read-back: stored user-role summary plus retained tail replaces active message projection for subsequent model calls; later summarization can consume an earlier summary again.
- Delegated visibility: summary model gets formatted selected transcript, not unlimited raw tool output; next turn gets packaged summary and surviving messages, not the full summarization input.
- Selection predicate: all mode summarizes all except pending tool-call preservation; sliding-window plans an assistant-boundary cutoff with estimated tokens. Planning failure or insufficient reduction falls back to all mode.
- Invalidation or expiry: later compaction replaces active projection; JSONL compaction checkpoint records summary/first-kept lineage. Raw append history is not a promise of full active context.
- Activation or effect: automatic trace-fed summarization and persistence are wired; summary fidelity and useful behavior changes are unobserved.
- Evidence limits: tool returns initially truncated to 2,000 characters, overflow retries use bounded transcripts, output defaults to a 50,000-character clip; full session-replay algorithm was not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: model generates summary under configured/default summarization instructions. Decider: backend admits returned text after trim/clip; software chooses cutoff/fallback. Human review is not required in this inspected path. Operating mode: context maintenance, not candidate quality comparison. Answer oracle: inapplicable — prompt demands fidelity but no independent reference outcome validates it. Recovery: errors propagate; planning fallback changes scope, not an undo of earlier admitted summaries. Guidance requests goals, actions, details and lookup hints; reasons may survive only if the generated/clipped text retains them.

> const clipChars = input.clipChars === undefined ? 50000 : input.clipChars;
>   if (clipChars !== null && summary.length > clipChars) {
>     summary = `${summary.slice(0, clipChars)}${SUMMARY_TRUNCATION_SUFFIX}`;
>   }
> --- `src/backend/local/compaction.ts`

#### MEM-RTE-reflection-integration
Label: Trace-fed reflection proposals and memory integration

Distinct maintenance subroute supported by [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), spanning transcript, worktree and memory delivery rather than redeclaring generic task execution. Endpoints: post-turn/manual reflection → selected transcript/payload and parent snapshot → memory-scoped subagent → committed proposal → automatic or explicit integration → core/skill read-back. SRC-1: `src/cli/helpers/post-turn-reflection.ts`, `src/cli/helpers/reflection-transcript.ts`, `src/cli/helpers/reflection-launcher.ts`, `src/agent/memory-worktree.ts`, `src/cli/helpers/reflection-integration.ts`; requested curation is doctrine in `src/agent/subagents/builtin/reflection-v2.md`.

- Immediate return: background launch/result, integration status and completion notice, not guaranteed semantic improvement.
- Later read-back: merged memory/skill files reach later core projection or requested loading; progress checkpoints affect subsequent transcript selection. Successful no-change reflection can consume input without changing memory.
- Delegated visibility: subagent receives payload path, parent-memory snapshot and scoped worktree; multi manifest selects unreflected slices or replay slices, with reasons/priorities where supplied.
- Selection predicate: enabled MemFS plus step-count/compaction trigger or manual request, suppression/backoff/capacity and available new content. Multi payload defaults to 50 replay turns per conversation and 150,000 total characters; first slice can exceed that total check.
- Invalidation or expiry: dirty worktree, failed child, dirty parent or merge conflict causes cleanup/retry rather than accepted memory; only successful completion advances reflected-through state. Replay slices do not advance it.
- Activation or effect: source wires transcript-fed edits, commit/merge and later context channels. Requested filtering/contradiction correction/skill generalization is not proof the model performed it.
- Evidence limits: no exercised traces; external normalization and complete selection machinery not audited; explicit integration is another agent conversation, not necessarily human per-content approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes updates guided by correction, lasting-value, duplication and reusable-workflow filters. Installed Git checks and finalizer veto unsafe repository states; optional explicit primary-agent integration reviews/edits under user-configured instructions. That mode asks the agent to work without interrupting the user. Default successful clean proposals merge mechanically; no semantic oracle is established. Operating mode: open trace-driven maintenance; answer oracle: inapplicable — transcript/user feedback are inputs, not independently supplied expected answers. Persisted reasons are requested in commit messages and final reports, but normal core/Skill consumers read file bodies, not those explanations. Git history views afford later human inspection; no automatic causal-reason read-back established.

> If new information contradicts existing memory, fix the stale entry at the source. Do not append the new version alongside the old.
> --- `src/agent/subagents/builtin/reflection-v2.md`

> Do not ask the user questions or wait for input. Handle the integration as far as you safely can and explain any remaining blocker in your final response. If integration remains incomplete, the harness will clean up this proposal without consuming the source transcript so reflection can retry later.
> --- `src/cli/helpers/reflection-integration.ts`

#### MEM-RTE-arena-selection
Label: Reflection arena selection and discard

Distinct candidate-admission alternative to [MEM-RTE-reflection-integration](#mem-rte-reflection-integration); closest supplied record is [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), not an identical arena referent. Endpoints: paired candidates in awaiting_choice → supplied choice → chosen integration or tie/no-merge → losers discarded → choice log/progress. Owner: arena finalizer and reflection integration. SRC-1: `src/cli/helpers/reflection-arena.ts`.

- Immediate return: completed run and message with choice/integration result.
- Later read-back: successfully merged winner enters memory consumers; choice record is persisted locally, but a later learning consumer of that feedback is uninspected.
- Delegated visibility: selector sees candidate reports/identities; chosen worktree reaches integration; losers are not installed as memory.
- Selection predicate: awaiting_choice state and choice label 1/2/tie; successful child/integration checks still apply to selected content.
- Invalidation or expiry: tie discards both; unchosen branches cleaned; source transcript advances only on completionSuccess, not merely recorded choice.
- Activation or effect: choice-controlled admission and discard are wired; no causal quality comparison is supplied.
- Evidence limits: choice API alone does not authenticate a human principal; user-facing questions afford human selection, but exercised review and uploaded feedback use are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Candidates are model proposals; supplied choice decides which may integrate, and repository checks can veto it. Mode: bounded paired comparison of proposals, not an expected-answer curriculum. Answer oracle: inapplicable — preference/notes are not an independent reference outcome. Guidance is ordinary reflection guidance; choice persists separately from admitted files. The choice log is not itself proof of parameter learning or future selection adaptation.

> await finalizeReflectionMemoryWorktree(candidate.worktree, {
>       shouldMerge: false,
>       knownNoChanges: candidateIsConfirmedNoOp(candidate),
>     });
> --- `src/cli/helpers/reflection-arena.ts`

#### MEM-RTE-repository-sync
Label: Repository attachment synchronization and withdrawal

Distinct from [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn): transport/membership can occur outside a model turn. Endpoints: attach/sync/detach request or post-turn clean-commit check → local mount/remote Git → cache invalidation/recompile/reminders → later eligible file/skill consumers. Owner: CLI and synchronization helpers, external service for attachment acceptance. SRC-1: `src/cli/subcommands/shared-memory.ts`, `src/agent/memory-git.ts`, `src/agent/attached-repository-git-sync.ts`, `src/reminders/memory-git-sync.ts`, `src/agent/shared-memory-skills.ts`, `src/agent/memory-git-hooks.ts`.

- Immediate return: mount/sync/status responses or warnings; attach can succeed while recompile fails, with failure reported rather than attachment undone.
- Later read-back: current attachments govern shared-skill eligibility; sync warnings can reach later turns through reminder queues. Hosted non-skill projection remains an external contract.
- Delegated visibility: mounted files and discovered skill metadata/body; remote request receives repository/agent identity and commits. Optional mirror gets main-branch commits separately.
- Selection predicate: attached non-primary repository list; writable permissions and clean pending commits for shared push. Agent-memory push additionally audits pending history. Local-only backend skips Letta-remote push.
- Invalidation or expiry: detach invalidates client skills and requests recompile but leaves mount bytes; push failure retains pending commits for retry; non-fast-forward can rebase then retry; conflicts remain for repair.
- Activation or effect: transport/membership and later eligible reads are wired; successful remote convergence and server adoption are unobserved.
- Evidence limits: attached-repository push has no identical pending-history audit in the inspected branch; optional post-commit mirror is asynchronous/log-only on failure. Generic filesystem tools may still read detached bytes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller requests attachment/detachment; service decides acceptance. Content authors separately edit/commit; software gates clean/writable pushes. Neither membership nor sync is semantic curation. Human per-content approval is unresolved. Mode: repository maintenance; answer oracle: inapplicable — clean Git state is not a correctness reference. Recovery is retained commits/rebase/retry, not guaranteed rollback or deletion. Optional mirroring runs only for main and has no demonstrated read-back consumer in SRC-1.

> note: "The local mount was left in place; delete it manually if no longer needed.",
> --- `src/cli/subcommands/shared-memory.ts`

> if (!params.remoteSupported) {
> --- `src/agent/attached-repository-git-sync.ts`

#### MEM-RTE-transcript-search
Label: Requested transcript and conversation search

Distinct retrieval route over the container [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript), not a redeclaration of automatic history loading. Endpoints: CLI/UI search request → backend-specific selector → ranked bounded message/summary results → caller. Owner: local search implementation or external service. SRC-1: `src/backend/message-search.ts`, `src/backend/local/transcript-search.ts`, `src/backend/conversation-search.ts`; shipped caller references in `src/cli/subcommands/messages.ts` and `src/cli/components/MessageSearch.tsx`.

- Immediate return: message search results or conversation metadata with readable summary, not automatically an adopted memory assertion.
- Later read-back: subsequent caller searches retained transcripts; CLI use through an agent's shell can return results as tool output, while UI receives them for human interpretation.
- Delegated visibility: selected message text/metadata or matched conversation summary; hidden conversations excluded unless requested.
- Selection predicate: query terms/phrases, optional agent/conversation/date filters and result limit; local message search rejects vector/hybrid. Default limit is 100. Local conversation search first lists recent limited conversations then matches summary terms.
- Invalidation or expiry: later requests search available stored content; active conversation's newest user message and search echoes are demoted for unscoped recall. Complete index-cache invalidation not audited.
- Activation or effect: query-driven returned content is wired; whether a user/model relies on it is unobserved.
- Evidence limits: local conversation rrf_score label is term-match proportion, not proof of vector retrieval; hosted vector/hybrid algorithms and embedding lineage remain opaque. API methods alone do not establish a deployed consumer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> rrf_score: matchedTerms / terms.length,
> --- `src/backend/conversation-search.ts`

### Claims

#### MEM-CLM-visibility-boundary
Label: Committed context is narrower than all memory reads

Claimed operation: committed HEAD determines local automatic core compilation, but Memory and Skill read working-tree files. Therefore the prompt's claim that changes affect future context only after commitment is reliable only for the inspected automatic core route, not every tool-fed context route. Closest supplied claim context is [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn); its committed-core finding is not contradicted. SRC-1: `src/backend/local/system-prompt-compilation.ts`, `src/tools/impl/memory.ts`, `src/tools/impl/skill.ts`. Supporting passages are in the corresponding route records.

#### MEM-CLM-archive-projection
Label: Root archive text remains core

Claimed operation: reflection guidance says to use root ARCHIVE.md for content no longer load-bearing, but the local v2 selector includes every root Markdown file. Following that placement does not by itself remove the archived text from automatic context. This is a source-supported mismatch, not observed agent behavior. No supplied counterpart after comparison. SRC-1: `src/agent/subagents/builtin/reflection-v2.md`, `src/agent/memory-format.ts`; root selector passage is in [MEM-OBJ-core-memory](#mem-obj-core-memory).

> Use the root file `ARCHIVE.md` when content should no longer be load-bearing but may still be useful as historical context — shrink or remove the active source, then append a concise dated entry to `ARCHIVE.md`.
> --- `src/agent/subagents/builtin/reflection-v2.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-context
Label: Memory text to later model context

Consumer: later turn model. Channel: core compiled prompt/mid-conversation update, requested deferred tool return or loaded skill user-message text. Force: model-interpreted instructions/context, not host-enforced obedience. Horizon: subsequent turns and sessions while files/history remain eligible. Distinct retained-part paths feeding [RT-BAP-provider-context](runtime.md#rt-bap-provider-context), not a replacement for that provider-context container. Selection differences remain owned by the route records above. SRC-1: `src/backend/local/system-prompt-compilation.ts`, `src/backend/local/local-backend.ts`, `src/tools/impl/memory.ts`, `src/tools/impl/skill.ts`, `src/headless.ts`. Their passages establish delivery wiring; no source trace establishes activation or benefit.

#### MEM-BAP-reflection-progress
Label: Reflection progress to later maintenance selection

Consumer: reflection payload selector and trigger logic, not turn model. Channel: reflected-through ID/completed-step/checkpoint fields. Force: symbolic exclusion/replay/threshold rules. Horizon: later reflection attempts across turns and sessions; failed integration does not advance successful progress. Distinct from [RT-BAP-provider-context](runtime.md#rt-bap-provider-context), whose consumer interprets text. SRC-1: `src/cli/helpers/reflection-transcript.ts`, `src/cli/helpers/post-turn-reflection.ts`.

> state.reflected_through_message_id = selection.endMessageId;
> --- `src/cli/helpers/reflection-transcript.ts`

## Annotations

#### On [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript)

Memory-specific distinction: raw history is stored independently from the active summary-plus-tail projection. Derived summary text is [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary); first-kept entry and stats are control/lineage metadata, not remembered prose. Search can inspect message and compaction rows; full append/replay reconstruction was not audited. SRC-1: `src/backend/local/local-store.ts`, `src/backend/local/transcript-search.ts`. Later turn consumer receives selected history, not guaranteed full raw history. No initial transcript source or external provider reasoning fidelity is inferred.

#### On [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model)

Memory-specific input/output boundary: transcript formatter truncates tool results; overflow fallback can reduce input further, and output is clipped before persistence. The component's Fable fallback identity does not make the retained summary complete. SRC-1: `src/backend/local/compaction.ts`; [MEM-RTE-transcript-compaction](#mem-rte-transcript-compaction) supplies the retained-result route and passage.

## Write side

Fresh local create bodies become root-layout files, with collision/path checks and synthesized metadata where needed. Existing HEAD prevents reseeding; initialization refreshes local Git setup instead. Unknown caller authorship stays local to initialization and does not suppress known later trace transformations. Ordinary agent tools, listener byte writes and worker proposals are distinct producers feeding [MEM-RTE-memory-admission](#mem-rte-memory-admission). SRC-1: `src/backend/local/initial-memory.ts`, `src/agent/memory-git.ts`.

Git checks separate physical writes from admission. V2 memory excludes skills from memory-file frontmatter validation; skill validation/discovery is a separate surface. Legacy protection consults previous accepted read_only metadata; v2 uses tree policy/read-only globs and ancestor indexes. The installed gate rejects structurally unacceptable commits but does not authenticate the proposed facts. A commit author string naming an agent also does not establish who authored the content. SRC-1: `src/memory-frontmatter.ts`, `src/agent/memory-git-hooks.ts`, `src/memory-constraints.ts`.

Two automatic trace-fed chains are wired. Compaction selects raw/previously summarized history, transforms bounded input with the summary model, and persists summary-plus-tail for later invocation. Reflection selects transcript slices, requests extraction/correction/generalization, commits proposed memory or skills, and integrates into later consumers. Alternative summary checkpoints retain first-kept lineage; multi-reflection manifests retain replay/unreflected distinctions. Reasons are requested but not guaranteed to survive formatting, generation, clipping or a later body-only read. [MEM-RTE-transcript-compaction](#mem-rte-transcript-compaction), [MEM-RTE-reflection-integration](#mem-rte-reflection-integration).

Generic memory-worker integration is not identical to reflection: the source explicitly allows a dirty parent where Git can merge without overwriting it; conflict leaves the branch for later repair. This challenges a system-wide assertion that every worker proposal is discarded whenever the parent is dirty. Exact task finalization and later retry consumers remain uninspected. SRC-1: `src/agent/memory-worktree.ts`.

> * Unlike reflection, a dirty parent does not block the merge: Git refuses only
> * when the parent's uncommitted files overlap the worker's commits, and that
> * surfaces as a conflict here.
> --- `src/agent/memory-worktree.ts`

Rejection/withdrawal is substantive state handling. Reflection failure and conflict clean proposals while keeping source input eligible; arena tie installs neither candidate. Detach removes shared-skill eligibility without deleting its mount. Delete/forget instructions request removal of sensitive/wrong files, but Git history remains unless separately removed; no secure erasure guarantee is supported. Automatic invalid/conflict repair has retained attempt suppression and warning delivery, but worker content/semantic acceptance is unresolved. SRC-1: `src/agent/memory-worktree.ts`, `src/cli/helpers/reflection-arena.ts`, `src/cli/subcommands/shared-memory.ts`, `src/agent/memory-conflict-repair.ts`, `src/reminders/memory-git-sync.ts`.

## Read-back

Automatic push selects committed core by layout and revision, not by the current problem. Provider authority is interpretation of supplied text, and cache invalidation differs from memory truth revision. Requested Memory(path) uses path/recency and bounds output; it is not embedding-based targeting. Skill(name) resolves metadata-selected procedures, queues full text and injects it as user content; its display summary is not the procedure. Transcript search uses query filters/ranking and returns retained messages/summary text. These routes are not interchangeable. [MEM-RTE-core-projection](#mem-rte-core-projection), [MEM-RTE-deferred-read](#mem-rte-deferred-read), [MEM-RTE-skill-loading](#mem-rte-skill-loading), [MEM-RTE-transcript-search](#mem-rte-transcript-search).

The later reflection selector consumes successful-progress metadata symbolically; the reflection model consumes selected normalized evidence and current memory as text. The turn model later consumes admitted output through core/deferred/skill channels. This separates evidence authority at the update consumer from instruction/context authority at the operational consumer. Whether these paths improve capacity or instantiate a theory-building process is not established by the label reflection or by persistence alone. [MEM-BAP-reflection-progress](#mem-bap-reflection-progress), [MEM-BAP-memory-context](#mem-bap-memory-context).

Optional repository mirrors, feedback uploads, export/history views and general library read methods are storage/inspection affordances unless a later consumer is identified. Shared skills have such a consumer; hosted non-skill projections and arena-feedback training consumers remain opaque/uninspected. SRC-1: `src/agent/memory-git-hooks.ts`, `src/cli/helpers/reflection-arena.ts`, `src/agent/shared-memory-skills.ts`, `src/cli/subcommands/memory.ts`.

## Integration issues

- Scope qualification, not a correction to the runtime's committed-core finding: [MEM-CLM-visibility-boundary](#mem-clm-visibility-boundary) limits the shipped commit-only doctrine to automatic core compilation. Deferred and skill reads can use dirty bytes. Consequence: do not extend [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)'s revision-cache account to all memory consumers.
- Source doctrine/compiler mismatch: [MEM-CLM-archive-projection](#mem-clm-archive-projection) shows root ARCHIVE.md remains automatically supplied. Consequence: requested archival is not evidence of reduced authority or context load.
- Source visibility claim qualification: reflection-v2 says the primary always sees filesystem tree and deferred descriptions; the directly inspected local v2 compiler supplies root content plus first-level directory pointers. Requested Memory(directory) supplies further descriptions. Other paths may supply richer views; universal visibility is not established. SRC-1: `src/agent/subagents/builtin/reflection-v2.md`, `src/backend/local/system-prompt-compilation.ts`, `src/tools/impl/memory.ts`; [MEM-RTE-core-projection](#mem-rte-core-projection), [MEM-RTE-deferred-read](#mem-rte-deferred-read).
- Worker gate distinction: generic workers and reflection have different dirty-parent/conflict handling. Consequence: [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task) must not inherit reflection's gate as a universal task property. Exact generic worker retry wiring remains uninspected. SRC-1: `src/agent/memory-worktree.ts`.
- All new declarations were compared with supplied records. Core delivery is explicitly part of the supplied foreground route; summary is explicitly part of the transcript. Other objects/routes have distinct referents named in their declarations. [MEM-BAP-memory-context](#mem-bap-memory-context) overlaps the terminal segment of [RT-BAP-provider-context](runtime.md#rt-bap-provider-context), but names retained selection/delivery paths rather than all provider context. Reconciliation should preserve the supplied container, not duplicate or replace it. No unresolved same-referent duplicate is asserted.
- Included incomplete parts: full session replay/search ranking/cache implementation, reflection normalization/automatic conversation selection, generic worker completion/repair edits, arena UI principal/feedback consumers, migration/import guidance and all evaluator coverage remain uninspected. Their source paths and prevented conclusions are in the inventory. These limits prevent complete enumeration of provenance/curation behavior, not the supported positive routes.
- External unknowns: hosted memory encoding/embedding origin, server-side curation/selection and attachment enforcement cannot be resolved within SRC-1. Local readable metadata does not settle them. [MEM-OBJ-hosted-memory](#mem-obj-hosted-memory), [MEM-RTE-repository-sync](#mem-rte-repository-sync).

## Limitations and checks

Source identity was rechecked with Git HEAD and clean status: 271f119dcf37d58649a18e6c733386b3c710a456 at the supplied access root. The run/source fields exactly repeat the supplied boundary/invocation. This worker read the full invocation, member types, supplied boundary/runtime, collection, job, worker rules and record contract; source reads were bounded. No additional sources, agents, runtime fixtures or target execution were used. Method identity is the supplied job/member-type/records contract in this prepared worktree; no unprovided method commit is inferred.

Countercase checks qualified commit-only visibility, archive placement, uniform worker gates, universal deferred descriptions, vector-like local labels and human-approval wording. No observed trace or causal experiment supports quality, activation, learning benefit, secure erasure or reliable hosted convergence. Available uninspected paths remain named limits rather than evidenced absences. Deterministic validation result: the required commonplace-validate member content check passed. It reported that invocation residue was not checked and that this is not job acceptance or claim support. Validation establishes form/quotation occurrence only, not semantic acceptance.
