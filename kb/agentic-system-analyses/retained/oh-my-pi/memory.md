---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "oh-my-pi memory: branch checkpoints, backend-specific retention and recall, decision extraction and managed-skill capture"
run-id: AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01
source-identity: https://github.com/can1357/oh-my-pi
reviewed-boundary: "2431e8a8716a4da73ae327a412f6d54c22f681e5"
---

# oh-my-pi memory report

## Boundary and evidence

The subject is the shipped coding runtime's retained context and memory paths at the [boundary](boundary.md). This report preserves its **complete artifact, partial loop** limit. SRC-1 supplies implementation and doctrine/design, not observed runs. Direct reads extend the provisional [RT-RTE-session-turn](runtime.md#rt-rte-session-turn) account to session reconstruction, local memory, Hindsight and Mnemopi adapters, Sharpshooter, managed skills and automatic capture. The external Hindsight service and provider weights remain excluded. Their storage transformations and reliability are not attributed to this runtime.

The inventory below distinguishes direct inspection from supplied findings and available but uninspected mechanisms. Source paths are commit-relative to SRC-1. No file access gap was found. Positive adapter wiring is not an exhaustive account of every backend's internal algorithm.

| Entry point or operation | SRC-1 paths and inspection | Coverage and prevented conclusion |
|---|---|---|
| Session resume, branch reconstruction, reset and checkpoint replay | Direct: `packages/coding-agent/src/session/session-context.ts`; selected `packages/coding-agent/src/session/session-manager.ts`, `packages/coding-agent/src/session/session-maintenance.ts`, `packages/coding-agent/src/session/compaction-methods.ts` | [MEM-RTE-context-rebuild](#mem-rte-context-rebuild); checkpoint parts declared separately below. Producer algorithms, branch-summary authoring, foreign-session import, Redis/SQL storage and every recovery path are not fully inspected; no storage-parity or complete compaction guarantee. |
| Local startup extraction, consolidation and explicit lessons | Direct: selected `packages/coding-agent/src/memories/index.ts`; complete `packages/coding-agent/src/memories/storage.ts`, `packages/coding-agent/src/memory-backend/local-backend.ts`; `packages/coding-agent/src/prompts/memories/read-path.md` | [MEM-RTE-local-consolidation](#mem-rte-local-consolidation), [MEM-RTE-local-lessons](#mem-rte-local-lessons). Separate local output records distinguish stage-one rows, intermediate files, automatic summary, on-demand memory/procedure and script/template/example files. Initial rollout discovery and every extraction prompt were not fully read; no complete acquisition/provenance enumeration. |
| Backend resolution, exposed save/search and live changes | Direct: `packages/coding-agent/src/memory-backend/runtime.ts`, `packages/coding-agent/src/memory-backend/recall-entry.ts`; selected `packages/coding-agent/src/session/session-memory.ts`; supplied boundary resolver findings | [MEM-RTE-backend-recall](#mem-rte-backend-recall). Off is a selected alternative, not evidence that the whole system lacks memory. Full transition teardown and failure recovery remain uninspected. |
| Hindsight startup, retain, recall, pre-compaction supply and mental models | Direct: selected `packages/coding-agent/src/hindsight/backend.ts`, `packages/coding-agent/src/hindsight/state.ts` | [MEM-RTE-hindsight-retention](#mem-rte-hindsight-retention), [MEM-RTE-backend-recall](#mem-rte-backend-recall). [MEM-OBJ-mental-models](#mem-obj-mental-models) separates stable cache from persisted recall. Load/publication/deadline branches are directly inspected; full seed admission, loader rendering internals and upstream derivation remain unresolved. |
| Mnemopi startup, save/search, transcript retention, edits and consolidation | Direct: selected `packages/coding-agent/src/mnemopi/backend.ts`, `packages/coding-agent/src/mnemopi/state.ts`, `packages/mnemopi/src/core/beam/schema.ts`; search inventory of `packages/mnemopi/src/core/memory.ts`, `packages/mnemopi/src/cli.ts`, `packages/mnemopi/src/mcp-tools.ts` | [MEM-RTE-mnemopi-retention](#mem-rte-mnemopi-retention), [MEM-RTE-memory-edit](#mem-rte-memory-edit). Working, episodic, fact, JSON-embedding and binary-vector parts are separately declared under [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory); schema and adapter mutation eligibility are inspected. Core extraction, vector generation, ranking, consolidation and deletion propagation remain unresolved. No exhaustive curation or retirement guarantee. |
| Alternate Mnemopi CLI, module API and MCP admission/recall | Search inventory: `packages/mnemopi/src/cli.ts`, `packages/mnemopi/src/core/memory.ts`, `packages/mnemopi/src/mcp-tools.ts` | CLI store/import/update/delete/sleep/export, module remember/recall/update/forget/sleep, and MCP remember/shared-memory/validation operations exist. Caller authorization, import lineage, selector details and downstream wiring have not been traced. These are unresolved alternative paths, not established agent consumer routes. |
| Sharpshooter user-message extraction, scheduler consolidation and instruction injection | Direct: `packages/coding-agent/src/sharpshooter/backend.ts`, selected `packages/coding-agent/src/sharpshooter/extract.ts`, `packages/coding-agent/src/sharpshooter/consolidate.ts` | [MEM-RTE-decision-memory](#mem-rte-decision-memory). [MEM-OBJ-decision-deltas](#mem-obj-decision-deltas) owns occurrence admission/reasons; [MEM-OBJ-project-decisions](#mem-obj-project-decisions) owns replacement admission/injection. Scheduler body and queue crash recovery are not fully inspected; no exactly-once or prompt-freshness guarantee. |
| Auto-learn controller, private capture, learn and skill mutation | Direct: `packages/coding-agent/src/autolearn/controller.ts`, selected `packages/coding-agent/src/autolearn/managed-skills.ts`, `packages/coding-agent/src/tools/manage-skill.ts`, `packages/coding-agent/src/sdk.ts`; search `packages/coding-agent/src/tools/learn.ts` | [MEM-RTE-autolearn-capture](#mem-rte-autolearn-capture). Learn can retain a lesson and separately attempt a skill write; complete cross-write failure semantics remain uninspected. |
| Skill discovery and body admission | Direct selected `packages/coding-agent/src/extensibility/skills.ts`; supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | [MEM-OBJ-managed-skills](#mem-obj-managed-skills). Managed descriptions are selected with authored-name precedence; full skill invocation/forked-skill lifecycle and body read budgets remain uninspected. |
| Notebook replacement, fresh-window request, raw-history recovery and memory URLs | Direct `packages/coding-agent/src/session/context-notes.ts`, `packages/coding-agent/src/tools/context-notes.ts`; selected `packages/coding-agent/src/internal-urls/history-protocol.ts`, `packages/coding-agent/src/internal-urls/memory-protocol.ts` | [MEM-RTE-notebook-update](#mem-rte-notebook-update), [MEM-RTE-artifact-read](#mem-rte-artifact-read). Ownership checks and full-row/raw-branch access are established; all generic read transformations and URL write operations are not. |
| Child context and parent return | Supplied [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn); direct backend child-alias branches | Annotation below. Separate contexts do not imply isolated files or memory banks. |
| Request-local transforms, advisors, providers and extensions | Supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); selected SDK memory-prompt assembly | Annotation below. Complete advisor, TTSR, prewalk, pin, shake, provider-image-budget, handoff, snapcompact encoder, evaluation and cross-language client loops remain uninspected. Their existence does not establish retention or successful learning. |

## Core ideas

Three distinctions determine later consumption. First, the session journal is a branch-addressed raw trace, while the model receives a reconstruction that can substitute a checkpoint, retain a tail, insert notes and strip unsafe turns. The display transcript is not the provider context. Second, backend memory is not one uniform store: local memory injects a cached summary and lessons; Mnemopi and Hindsight stage query-selected recall; Sharpshooter injects project decision files. Third, automatic capture changes durable files through a separate agent context without making the synthetic capture instruction a human approval.

Recall stability can conflict with freshness. Both query backends preserve a first-turn recall with the transcript. Mnemopi can report changes to tracked previews as a new message instead of rewriting historical prompt bytes. Hindsight reuses the old block without that lookup. Local memory also freezes its snapshot once conversation has started. Thus successful saving, deletion or consolidation does not imply that every already-open session sees the change immediately ([MEM-RTE-backend-recall](#mem-rte-backend-recall), [MEM-RTE-local-lessons](#mem-rte-local-lessons)).

Admission strength varies. Schema checks and secret redaction admit local model summaries; Sharpshooter additionally requires each extracted evidence string to occur in the triggering user prompt. That proves textual occurrence, not that the proposed decision follows from the evidence. Retained natural language guides inference; symbolic scope, ownership and size checks constrain software operations. No observed compliance or benefit follows from either delivery path.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-session-journal
Label: Session journal

Source-native identity: SessionManager entries and selected leaf. Storage: persisted session journal with in-process indexes; JSONL sessions are established by the supplied [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn), while alternative storage implementations remain uninspected. Representational form: symbolic entry IDs, parent IDs, reset markers, settings and checkpoint metadata; message text is natural-language trace content. Lineage: user/model/tool events plus explicitly appended custom and compaction entries. This is not identical to the current provider message array or a derived knowledge store. Distinct from the supplied session-turn route: it is the retained input to reconstruction, not another declaration of that route. Evidence: SRC-1, `packages/coding-agent/src/session/session-manager.ts`, `packages/coding-agent/src/session/session-context.ts`.

> this.#recordEntry(entry);
> return entry.id;
> --- `packages/coding-agent/src/session/session-manager.ts:3530-3559`

#### MEM-OBJ-compaction-summary
Label: Compaction summary

Source-native identity: CompactionEntry summary and shortSummary. Storage: journal entry strings; form: natural-language derived context. Lineage: selected compaction method or extension output, not necessarily a model-generated summary in every method. Consumer: reconstruction emits summary before retained and later messages; display can render it at the compaction point. Reasons survive only if carried by the text or other preserved payload; a short summary does not establish preservation of all source reasoning. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): it is a retained history message, not the system-prompt object. Evidence: SRC-1, `packages/coding-agent/src/session/session-context.ts`, `packages/coding-agent/src/session/session-manager.ts`.

> if (!options?.transcript) {
> pushMessage(compactionSummaryMsg);
> }
> --- `packages/coding-agent/src/session/session-context.ts`

#### MEM-OBJ-provider-payload
Label: Provider payload

Source-native identity: preserveData.openaiRemoteCompaction replacementHistory and Anthropic compaction replay retrieved by reconstruction. Storage: checkpoint metadata in the journal; form: symbolic provider replay structures with opaque content whose internal encoding and semantic completeness are uninspected. The readable summary is a different part, [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), and cannot stand in for the payload. Consumer: reconstructed compaction message carries providerPayload; downstream provider encoding was not inspected here. OpenAI replacement history can carry the retained turns instead of replaying their visible SessionEntry counterparts. No counterpart in supplied records after comparison: [RT-RTE-session-turn](runtime.md#rt-rte-session-turn) describes context transformation, not this retained checkpoint part. SRC-1, `packages/coding-agent/src/session/session-context.ts`.

> const providerPayload = remotePayload ?? anthropicPayload;
> --- `packages/coding-agent/src/session/session-context.ts`

> if (!remoteReplacementHistory || options?.transcript) {
> --- `packages/coding-agent/src/session/session-context.ts`

#### MEM-OBJ-snapcompact-archive
Label: Snapcompact archive

Source-native identity: snapcompact archive in preserveData with frames and source-text metadata. Storage: persisted archive/frame references with lazy frame resolution; form: image-encoded history intended for visual model reading, with symbolic frame metadata. This is not a learned parameter store or necessarily semantic summarization. Consumer: reconstruction attaches history blocks subject to frame-byte budgets; transcript rendering and model emission have different budgets. The actual encoder, image quality and model recovery fidelity remain uninspected. Distinct from the text summary and provider replay parts, and from the request-local transforms in [RT-RTE-session-turn](runtime.md#rt-rte-session-turn). SRC-1, `packages/coding-agent/src/session/session-context.ts`, `packages/coding-agent/src/session/compaction-methods.ts`.

> return snapcompact.historyBlocks(archive, snapcompactHistoryBlockOptions(archive, options));
> --- `packages/coding-agent/src/session/session-context.ts`

#### MEM-OBJ-context-notes
Label: Context notes

Source-native identity: experimental_context_notes custom entry, version 1, text. Storage: branch journal; form: natural-language notebook plus symbolic version/size metadata. Lineage: whole replacement through context_notes; original authorship and the truth of notebook content are not established merely by tool acceptance. Latest valid revision after reset wins. Consumer: reconstructed model context inserts rendered notebook text even after older turns leave the active window. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): this is a durable branch-specific custom message, not the base prompt. SRC-1, `packages/coding-agent/src/session/context-notes.ts`, `packages/coding-agent/src/session/session-context.ts`.

> if (entry.type === "reset_boundary") return undefined;
> if (!isContextNotesEntry(entry) || !isContextNotesData(entry.data)) continue;
> return { text: entry.data.text, entryId: entry.id };
> --- `packages/coding-agent/src/session/context-notes.ts`

#### MEM-OBJ-local-memory
Label: Local memory

Source-native identity: local pipeline's stage1_outputs and project-scoped published memory tree. This ID remains a valid lineage/storage container, not one uniform content representation or consumer. Storage: shared SQLite job database and project-scoped files. Form: mixed; natural-language extraction and guidance, symbolic access/maintenance metadata, and potentially executable generated files are assessed in the parts below. Lineage: rollout traces → model extraction → schema/redaction → stage-one rows → bounded consolidation → independently consumed outputs. The container has no additional admission or authority beyond those parts and [MEM-RTE-local-consolidation](#mem-rte-local-consolidation). No supplied object counterpart after comparison with [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), which delivers only selected guidance, not the whole tree. SRC-1, `packages/coding-agent/src/memories/index.ts`, `packages/coding-agent/src/memories/storage.ts`.

> await Bun.write(path.join(memoryRoot, "MEMORY.md"), `${consolidated.memoryMd.trim()}\n`);
> await Bun.write(path.join(memoryRoot, "memory_summary.md"), `${consolidated.memorySummary.trim()}\n`);
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-learned-lessons
Label: Learned lessons

Source-native identity: learned.md. Storage: project local-memory root; form: natural-language bullets with optional context, distinct from consolidated files. Lineage: explicit learn/save content, normalized and secret-redacted; hand-edited non-bullet content can survive subsequent writes. Writes deduplicate the incoming bullet, insert newest-first and cap retained bullets at 100. Injection shares the summary budget and may receive no space. Source field caps are 2,000 content characters and 400 context characters. Distinct from [MEM-OBJ-local-memory](#mem-obj-local-memory) and supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): lessons have separate admission and are not overwritten by consolidation. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> const LEARNED_LESSONS_FILE = "learned.md";
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-recall-entry
Label: Recall entry

Source-native identity: memory_recall custom entry with version, scope, text and tracked memory previews; memory-recall-changes custom messages update tracking. Storage: session journal; form: selected natural-language recall text and symbolic scope/ID/cut metadata. Lineage: first-turn lookup, rendering and budget truncation, then commit. This is derived selection, not a complete copy of a bank. Consumer: resumed transcript's prompt construction; Mnemopi also compares previews to live rows. Hindsight records no tracked memories. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): it supplies a persisted part of later prompt construction rather than redeclaring that prompt. SRC-1, `packages/coding-agent/src/memory-backend/recall-entry.ts`.

> sessionManager.appendCustomEntry(MEMORY_RECALL_ENTRY_TYPE, {
> version: 1,
> scope,
> text: recall.text,
> memories: recall.memories,
> } satisfies MemoryRecallEntryData);
> --- `packages/coding-agent/src/memory-backend/recall-entry.ts`

#### MEM-OBJ-mnemopi-memory
Label: Mnemopi memory

Source-native identity: scoped Mnemopi retain/recall bank databases. This ID remains the bank container; its working text, episodic text, facts and numerical representations are separately declared below. Storage: SQLite. Form: mixed natural-language, symbolic and numerical parts; no single bank-wide form, mutation eligibility or withdrawal guarantee applies. Lineage: adapter supplies full transcript, user-only extraction text and separately prepared embedding text; core transformations remain partly uninspected. Consumers: retention, extraction/sleep, scoped recall, full-row reads and edits, each acting on the appropriate part. No supplied object counterpart after comparison with [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call), a request rather than a bank. SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/coding-agent/src/mnemopi/backend.ts`, selected `packages/mnemopi/src/core/beam/schema.ts`.

> const { transcript: extractText } = prepareUserRetentionTranscript(messages);
> const { transcript: embedText } = prepareEmbeddableRetentionTranscript(messages);
> --- `packages/coding-agent/src/mnemopi/state.ts`

#### MEM-OBJ-decision-files
Label: Decision files

Source-native identity: Sharpshooter project decision bank, including queued deltas and architecture.md/product.md/style.md. This ID remains a valid combined lineage container, not a single admission unit. Storage: project queue and files. Form: mixed symbolic delta envelopes and natural-language content, separately assessed in [MEM-OBJ-decision-deltas](#mem-obj-decision-deltas) and [MEM-OBJ-project-decisions](#mem-obj-project-decisions). Lineage: current user prompt plus bounded referent context → extraction/admission → queued deltas → consolidation with current files/project docs → replacements. The consolidator consumes deltas; foreground/advisor instruction delivery consumes files. Evidence-occurrence admission applies only to deltas, not to every sentence of a consolidated file. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), which is their delivery container. SRC-1, `packages/coding-agent/src/sharpshooter/extract.ts`, `packages/coding-agent/src/sharpshooter/consolidate.ts`, `packages/coding-agent/src/sharpshooter/backend.ts`.

> if (delta.rationale) fields.push(`rationale=${JSON.stringify(delta.rationale)}`);
> --- `packages/coding-agent/src/sharpshooter/consolidate.ts`

#### MEM-OBJ-managed-skills
Label: Managed skills

Source-native identity: managed-skills/<name>/SKILL.md, omp-managed discovery provider. Storage: isolated agent directory. Form: natural-language procedure body and sanitized description, symbolic YAML name/description and discovery metadata. Lineage: foreground tool proposals or detached trace-fed capture; actual body meaning and preserved rationale depend on generated text. The mutation primitive restricts location and size, not usefulness. Consumer: discovery selects descriptions and paths for later skill availability; managed skills defer to enabled authored skills and custom-directory names. Body invocation and any contained executable effects remain uninspected. Distinct from supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load): these are skill documents, not imported extension modules. SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`, `packages/coding-agent/src/extensibility/skills.ts`.

> if (enabledAuthoredNames.has(capSkill.name)) continue; // an enabled authored skill owns this name
> --- `packages/coding-agent/src/extensibility/skills.ts`

#### MEM-OBJ-stage1-output
Label: Stage1 output

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: stage1_outputs.raw_memory and rollout_summary, with thread/watermark/cwd identity. Storage: SQLite job database. Form: derived natural-language extraction and rollout summary plus symbolic provenance/ownership metadata; not raw untransformed logs despite the raw_memory label. Lineage and admission: maintenance model output is schema-checked, redacted and accepted only with both nonempty text fields; no-output removes the older row. Consumer: phase-two synchronization selects project rows for consolidation, not automatic foreground injection. Retention/replacement is governed by [MEM-RTE-local-consolidation](#mem-rte-local-consolidation). Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): intermediate extraction is not directly delivered there. SRC-1, `packages/coding-agent/src/memories/index.ts`, `packages/coding-agent/src/memories/storage.ts`; the route retains the no-output/deletion passages.

#### MEM-OBJ-raw-memories
Label: Raw memories

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: raw_memories.md. Storage: project memory root file. Form: natural-language extracted memory with symbolic thread/update headers. Lineage: renders selected stage-one rawMemory fields; it is derived text, not the session journal. Consumer: consolidation model receives a 20,000 approximate-token prefix; explicit file read can return it to the foreground. Software synchronization, not a fresh human decision, admits this intermediate file. It is regenerated from selected rows; no separate truth gate or exhaustive rationale preservation is established. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): only subsequent consolidated summary is automatically injected. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> const rawBody = buildRawMemoriesMarkdown(outputs);
> await Bun.write(path.join(memoryRoot, "raw_memories.md"), rawBody);
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-rollout-summaries
Label: Rollout summaries

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: rollout_summaries/*.md. Storage: project files. Form: natural-language model-derived rollout summaries with symbolic thread/update headers. Lineage: selected stage-one rolloutSummary → per-rollout file, not verbatim raw history. Consumer: lexically sorted nonempty files feed consolidation within 12,000 approximate tokens; explicit file reads are possible. Synchronization writes without per-file human approval and removes .md files outside the current keep set. Rationale/fidelity depends on extracted text. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): these are intermediate consolidation inputs. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> const body = [`thread_id: ${row.threadId}`, `updated_at: ${row.sourceUpdatedAt}`, "", row.rolloutSummary].join(
> "\n",
> );
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-memory-summary
Label: Memory summary

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: memory_summary.md. Storage: project file and session instruction snapshot. Form: natural-language consolidated guidance. Lineage: bounded stage-one-derived inputs → consolidation model → schema/redaction/nonempty admission → file; no reference-answer oracle or per-content human approval. Consumer: automatic backend instruction assembly truncates this text to summaryInjectionTokenLimit, then grants remaining space to learned lessons. It is guidance subordinate to present evidence, not executable policy. Snapshot can remain frozen after conversation starts; later file replacement need not update that session. Empty-input cleanup removes the file. Reasons survive only if written into this summary. It supplies a part of the delivered [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), not that prompt's whole identity. SRC-1, `packages/coding-agent/src/memories/index.ts`; publication is quoted in the container and caching in [MEM-RTE-local-lessons](#mem-rte-local-lessons).

> const summaryOut = snapshot.summary
> ? truncateByApproxTokens(snapshot.summary, cfg.summaryInjectionTokenLimit).trim()
> : "";
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-memory-md
Label: Memory md

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: MEMORY.md. Storage: project memory root file. Form: natural-language consolidated memory. Lineage/admission: same consolidation response and schema/redaction/nonempty gate as summary, but a different output string. Consumer: explicit artifact read, not automatic summary injection; returned text may guide a later model invocation. Generic read shaping/budget remains uninspected. Replaced by consolidation or removed on empty-input cleanup; no complete rationale retention or semantic correctness gate established. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): it is an on-demand artifact, not the injected summary or base prompt. SRC-1, `packages/coding-agent/src/memories/index.ts`; two-output publication passage is retained in the container, and access in [MEM-RTE-artifact-read](#mem-rte-artifact-read).

#### MEM-OBJ-local-skills
Label: Local skills

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: skills/<name>/SKILL.md under the local memory root. Storage: project files, distinct from managed-skills/<name>/SKILL.md in [MEM-OBJ-managed-skills](#mem-obj-managed-skills). Form: natural-language procedure text; any embedded code has no established execution path here. Lineage: consolidation-model proposal, sanitized name, redacted nonempty content. Consumer: explicit artifact read gives model guidance; normal skill discovery/body invocation is uninspected. Code admits publication, not usefulness; no independent human approval is established. Regenerated files/skill directories outside the keep set are deleted. Rationale is only what content retains. No supplied object counterpart after comparison with [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), which does not automatically inject these bodies. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> files.set("SKILL.md", `${skill.content.trim()}\n`);
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-local-scripts
Label: Local scripts

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: skills/<name>/scripts/<path>. Storage: project files. Form: generated script text intended as executable symbolic code; actual languages, executable validity and effects are uninspected. Lineage: consolidation model output → schema, safe relative-path check, secret redaction and nonempty content → file publication. This is software admission, not per-script human approval or tested capability acceptance. Consumer: explicit file read is wired through local artifacts; an interpreter/execution consumer and grants are unresolved. Reading code can provide model context but does not establish execution authority. Replaced/deleted by publication keep sets or empty-input cleanup. Complete rationale and execution rollback are not established. Distinct from supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load): these scripts are not shown being imported as extensions. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> for (const item of skill.scripts) {
> files.set(path.posix.join("scripts", item.path), `${item.content.trim()}\n`);
> }
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-local-templates
Label: Local templates

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: skills/<name>/templates/<path>. Storage: project files. Form: template text; prose versus symbolic template syntax/content is unresolved, so a uniform natural-language classification is not warranted. Lineage/admission: consolidation output, safe relative paths, redacted nonempty content and software publication; no per-template human approval. Consumer: explicit artifact read is available, but rendering/substitution/execution wiring is uninspected. No automatic injection or execution authority follows from the bucket name. Current keep sets and empty-input cleanup control physical removal; no semantic freshness or rationale guarantee. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): independently stored on-demand files. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> for (const item of skill.templates) {
> files.set(path.posix.join("templates", item.path), `${item.content.trim()}\n`);
> }
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-local-examples
Label: Local examples

Part of: [MEM-OBJ-local-memory](#mem-obj-local-memory)

Source-native identity: skills/<name>/examples/<path>. Storage: project files. Form: example text with unresolved prose/code mixture, not established executable capability. Lineage/admission: model consolidation response, safe paths, redaction/nonempty checks and publication; human per-content review not established. Consumer: explicit artifact read can supply examples as model context; running examples or ordinary discovery is uninspected. Keep-set deletion/empty-input cleanup controls files, not all historical returned text. No fidelity, rationale or benefit guarantee is established. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): on-demand file rather than automatic instruction supply. SRC-1, `packages/coding-agent/src/memories/index.ts`.

> for (const item of skill.examples) {
> files.set(path.posix.join("examples", item.path), `${item.content.trim()}\n`);
> }
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-OBJ-working-memory
Label: Working memory

Part of: [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory)

Source-native identity: working_memory content/embed_text and row metadata. Storage: scoped SQLite bank table. Form: natural-language content/embedding-input text plus symbolic ID, scope, validity and access metadata; embed_text is text, not the numerical embedding. Lineage: explicit save or transcript retention; automatic input includes assistant/tool trace while extraction uses user-only text. Admission: adapter labels explicit saves user/fact and transcripts unknown/episode; these are not truth or human-approval proofs. Consumer: scoped recall and full-row read supply model context; core extraction/consolidation consumes rows. update/forget are permitted here, unlike episodic/fact rows; invalidate uses retirement metadata. Adapter startup promotes age-eligible rows before writes can TTL-trim them, but core promotion, TTL and retirement propagation remain unresolved. FTS uses embed_text when available, which is not guaranteed identical to stored content. No supplied object counterpart after comparison with [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call). SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/mnemopi/src/core/beam/schema.ts`; input and mutation passages in [MEM-RTE-mnemopi-retention](#mem-rte-mnemopi-retention) and [MEM-RTE-memory-edit](#mem-rte-memory-edit).

> `CREATE TRIGGER IF NOT EXISTS wm_ai AFTER INSERT ON working_memory BEGIN
> INSERT INTO fts_working(id, content) VALUES (new.id, COALESCE(new.embed_text, new.content));
> END`,
> --- `packages/mnemopi/src/core/beam/schema.ts`

#### MEM-OBJ-episodic-memory
Label: Episodic memory

Part of: [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory)

Source-native identity: episodic_memory content, summary_of, tier and row metadata, excluding numerical binary_vector declared separately. Storage: SQLite bank table. Form: natural-language retained content with symbolic lineage/tier/validity metadata. Lineage: adapter requests startup/sleep promotion of working rows; actual core derivation and preservation of reasons remain uninspected. Consumer: scoped retrieval/full-row reads provide model context; core sleep/degradation is not fully traced. Admission: automatic core maintenance is invoked, not per-row human approval. memory_edit rejects update/forget outside working rows but can invalidate eligible episodic rows. Propagation to numerical representations or copies and semantic fidelity are unresolved. Distinct from supplied [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call): persisted content, not a request. SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/mnemopi/src/core/beam/schema.ts`.

> summary_of TEXT DEFAULT '',
> veracity TEXT DEFAULT 'unknown',
> tier INTEGER DEFAULT 1,
> degraded_at TEXT,
> --- `packages/mnemopi/src/core/beam/schema.ts`

#### MEM-OBJ-mnemopi-facts
Label: Mnemopi facts

Part of: [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory)

Source-native identity: facts rows with fact_id, subject/predicate/object and source_msg_id. Storage: SQLite bank facts table. Form: symbolic triple structure whose field text is interpreted as natural-language claims, with numeric confidence metadata distinct from embeddings. Lineage: adapter schedules fact extraction with user-only extractText for automatic transcripts, but extraction internals and other CLI/MCP origins remain unresolved. No per-fact human approval or factual warrant follows from extraction. Consumer: recall displays object, or subject/predicate fallback; full-row reads resolve fact metadata. memory_edit refuses all fact mutations. Adapter full-row retirement follows a retired working source; episodic or absent sources do not provide the same retirement test. Core deletion propagation remains uninspected, not guaranteed independent withdrawal. Evidence/rationale need not survive in the displayed object. Distinct from supplied [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call). SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/mnemopi/src/core/beam/schema.ts`.

> subject TEXT NOT NULL,
> predicate TEXT NOT NULL,
> object TEXT NOT NULL,
> timestamp TEXT,
> source_msg_id TEXT,
> --- `packages/mnemopi/src/core/beam/schema.ts`

#### MEM-OBJ-memory-embeddings
Label: Memory embeddings

Part of: [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory)

Source-native identity: memory_embeddings keyed by memory_id with embedding_json/model. Storage: SQLite table; JSON is the serialization substrate, not the semantic form. Form: numerical embedding representation, separate from natural-language row content. Adapter supplies separately prepared embedText, but actual vector generation, original inputs for every entry, model provenance and core admission/replacement remain uninspected. Consumer: retrieval/ranking integration is unresolved; table presence does not establish a complete selection route or direct instruction authority. memory_edit targets rows, not a separately exposed vector edit; update/forget propagation into this table remains unresolved. No complete withdrawal guarantee. Generating model parameter change during operation, exact version pin and mutable endpoint resolution are uninspected; repository pin and nullable model string do not establish fixed weights. No supplied object counterpart after comparison with [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model): vectors are retained outputs, not the foreground inference model. SRC-1, `packages/mnemopi/src/core/beam/schema.ts`, `packages/coding-agent/src/mnemopi/state.ts`.

> CREATE TABLE IF NOT EXISTS memory_embeddings (
> memory_id TEXT PRIMARY KEY,
> embedding_json TEXT NOT NULL,
> model TEXT,
> created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> )
> --- `packages/mnemopi/src/core/beam/schema.ts`

#### MEM-OBJ-binary-vector
Label: Binary vector

Part of: [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory)

Source-native identity: episodic_memory.binary_vector. Storage: SQLite BLOB column. Form: opaque numerical/vector representation; generation/encoding semantics, source lineage and any relationship to memory_embeddings remain uninspected. Consumer, budget, selector and admission/withdrawal rules are unresolved; the column alone is storage capacity, not a demonstrated retrieval or instruction path. No direct memory_edit operation on this part is established. Generating model parameter changes, exact version and mutable endpoint resolution are uninspected, including whether this part uses a model. Distinct from supplied [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) and from the separately stored JSON embedding part. SRC-1, `packages/mnemopi/src/core/beam/schema.ts`.

> addColumnIfMissing(db, "episodic_memory", "binary_vector", "BLOB");
> --- `packages/mnemopi/src/core/beam/schema.ts`

#### MEM-OBJ-decision-deltas
Label: Decision deltas

Part of: [MEM-OBJ-decision-files](#mem-obj-decision-files)

Source-native identity: queued SharpshooterDelta records. Storage: project queue files. Form: symbolic kind/source/friction/session/time envelope, natural-language statement/evidence, optional rationale/rejectedAlternative. Lineage: extraction model interprets current user prompt plus bounded referent context. Admission: statement/shape checks and evidence substring occurrence in currentPrompt; a user-authored sentence is not approval of the interpretation. Consumer: consolidator receives rendered statement, evidence and optional reasons; deltas are not directly injected as project decisions. Successful replacement consumes queue inputs; failure can retain them for retry. No truth/benefit oracle or full queue recovery guarantee. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): intermediate update material, not final guidance. SRC-1, `packages/coding-agent/src/sharpshooter/extract.ts`, `packages/coding-agent/src/sharpshooter/consolidate.ts`; admission quote in [MEM-RTE-decision-memory](#mem-rte-decision-memory), rationale quote in container.

#### MEM-OBJ-project-decisions
Label: Project decisions

Part of: [MEM-OBJ-decision-files](#mem-obj-decision-files)

Source-native identity: architecture.md, product.md and style.md in the Sharpshooter project bank. Storage: files. Form: consolidated natural-language decisions. Lineage: current files/project docs plus rendered deltas → consolidation model → validated replacements. Admission is permitted names, uniqueness, line count, redaction and all-empty-wipe rejection, not the delta evidence-occurrence check. No per-file human review or semantic oracle is established. Consumer: populated files enter budgeted developer/advisor instructions; search returns matching lines. Force: requested model guidance to follow decisions unless user overrides, not executable policy. Replacements overwrite files through sequential renames without multi-file atomic rollback. Optional delta rationale may be omitted by consolidation or budgeted delivery; downstream model is not guaranteed to receive original evidence. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): persisted content supplying that delivery container. SRC-1, `packages/coding-agent/src/sharpshooter/consolidate.ts`, `packages/coding-agent/src/sharpshooter/backend.ts`; publication and authority passages retained in [MEM-RTE-decision-memory](#mem-rte-decision-memory) and [MEM-BAP-memory-guidance](#mem-bap-memory-guidance).

#### MEM-OBJ-mental-models
Label: Mental models

Source-native identity: HindsightSessionState.mentalModelsSnippet, separate from lastRecallSnippet and the session memory_recall entry. Storage: in-process rendered cache, backed by external bank mental models whose storage/derivation remain excluded. Form: rendered natural-language instruction content with symbolic load generation/time metadata. Lineage: startup/transcript reload or explicit reload invokes tryLoadMentalModelsBlock with bank, recallTags and mentalModelMaxRenderChars; a generation check and prompt-publication result decide cache adoption. Optional auto-seed calls ensureMentalModels; complete seed content/admission and upstream generation remain unresolved. Default-read-only wording is source intent, not proof of actual operator curation. No per-content human approval follows from startup.

Consumer: backend instruction assembly inserts cache before volatile recall for foreground and parent-alias children; SDK can include backend instructions for advisors. Force: guidance, not executable policy or demonstrated action dependence. Horizon: stable transcript cache, with new-transcript or explicit reload; timeout restores previous snapshot and invalidates late publication, failed refresh can restore prior text. It is not persisted under first-turn recall tracking rules, and no ID-change notice/withdrawal guarantee is established for this cache. Distinct from supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): retained instruction input, not the full prompt. Known delivery extends [MEM-RTE-backend-recall](#mem-rte-backend-recall) without attributing recall persistence or query selection to this part. SRC-1, `packages/coding-agent/src/hindsight/state.ts`, `packages/coding-agent/src/hindsight/backend.ts`.

> if (mentalModelsSnippet) parts.push(mentalModelsSnippet);
> if (recallSnippet) parts.push(recallSnippet);
> return parts.join("\n\n");
> --- `packages/coding-agent/src/hindsight/backend.ts`

> this.mentalModelsSnippet = result.block;
> const published = await this.#refreshBaseSystemPromptAfter(
> reason,
> () => generation === this.#mentalModelsLoadGeneration,
> );
> --- `packages/coding-agent/src/hindsight/state.ts`

### Routes

#### MEM-RTE-context-rebuild
Label: Context rebuild

Endpoints/progression: selected journal leaf → root-to-leaf path → latest compaction/reset selection → summary/payload/frames plus kept tail and later messages → notes insertion and unsafe-turn filtering → later Agent context. Owner: SessionManager reconstruction and SessionMaintenance commit; code selects by branch/reset/checkpoint metadata, not by a semantic relevance judgment. Distinct from [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): it reconstructs retained context before later inference, rather than executing the turn. SRC-1, `packages/coding-agent/src/session/session-context.ts`, `packages/coding-agent/src/session/session-maintenance.ts`, `packages/coding-agent/src/session/compaction-methods.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reconstructed message array and restored settings; compaction commit swaps Agent messages and rebases plan/advisor/todo runtime state.
- Later read-back: checkpoint parts and notebook reach later invocations and resume; untouched raw journal can remain reachable through full-history access.
- Delegated visibility: child session reconstruction is separate; parent does not automatically receive the child journal.
- Selection predicate: active leaf path, latest reset versus compaction, firstKeptEntryId and provider replay markers; error/retry turns and dangling tool calls can be omitted.
- Invalidation or expiry: later checkpoint supersedes prior active checkpoint; reset elides pre-reset model context and notes; archive byte budget or legacy crash-risk guard can omit frames without deleting display history.
- Activation or effect: changes which retained material is in the next model window; semantic influence and fidelity remain unobserved.
- Evidence limits: full producer strategies and provider encoding are not traced; readable transcript is not proof of delivered opaque history.

Admission: compaction appends a structured entry and commits a reconstructed context. Configured remote/snapcompact/handoff/shake/soft choices distinguish provider compression, image archival, document generation, dropping recoverable heavy content and model summarization. Their choice metadata is inspected, not every algorithm. Selected speculative admission rejects stale branch/model/settings snapshots and bypasses speculation when extension pre-compaction handlers exist. This does not establish a general correctness oracle or per-summary human approval. Rejected speculation is not a committed checkpoint; already-committed history rewrites require their own recovery. Guarantee strength: protocol, bounded to inspected commit/rebuild logic.

> if (!this.#armedSpeculationValid(run.armed, triggerContextTokens, pendingContextTokens)) {
> --- `packages/coding-agent/src/session/session-maintenance.ts`

> this.#host.agent.replaceMessages(sessionContext.messages);
> --- `packages/coding-agent/src/session/session-maintenance.ts:2480-2480`

#### MEM-RTE-local-consolidation
Label: Local consolidation

Endpoints/progression: enabled top-level persisted session startup → eligible rollout claims → bounded model extraction → stage-one output → project-filtered consolidation inputs → schema/redaction → memory files → later prompt snapshot or explicit artifact read. Owner: local backend and job pipeline; two maintenance model calls propose text, code admits it. Distinct from supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): this is background trace transformation, not foreground inference. SRC-1, `packages/coding-agent/src/memories/index.ts`, `packages/coding-agent/src/memories/storage.ts`, `packages/coding-agent/src/memory-backend/local-backend.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asynchronous startup scheduling, output rows/job status and file writes; foreground does not receive a verified lesson result from startup scheduling itself.
- Later read-back: memory_summary.md enters cached memory guidance; MEMORY.md and generated skills are explicitly readable through local memory URLs.
- Delegated visibility: startup skips taskDepth > 0; child tool access does not prove an independent consolidation pass.
- Selection predicate: enabled, persisted top-level session; rollout age/idle/source-kind/concurrency/watermark filters; project cwd selects stage-one rows; configured maximum rows and input budgets bound coverage.
- Invalidation or expiry: newer source watermark replaces extraction; no-output completion removes old stage-one row and dirties consolidation; empty project output cleans consolidated files/skills; generated files not in new output are removed.
- Activation or effect: trace-derived text can change later prompt guidance and available procedures; improved behavior is unobserved.
- Evidence limits: rollout scanning and all prompt doctrines not fully inspected; lease success does not make multi-file writes transactional or semantics correct.

Admission is schema validation, redaction and nonempty text checks, separate from model authorship and filesystem writes. Stage-one empty output is deliberately accepted as no-output, not retried as semantic failure. SQLite tokens guard job completion; failures have retry counters/delay. Consolidation inputs cap raw memories at 20,000 approximate tokens and rollout summaries at 12,000. The apply path writes files before final ownership-success checks, so a claimed lease is not an atomic publication guarantee. No per-content human approval or reference-answer oracle appears in these inspected functions. Maintenance is an open summarization procedure, not a measured improvement curriculum.

> if (!rawMemory || !rolloutSummary) {
> return { kind: "no_output" };
> }
> --- `packages/coding-agent/src/memories/index.ts`

> db.prepare("DELETE FROM stage1_outputs WHERE thread_id = ?").run(threadId);
> enqueueGlobalWatermark(db, sourceUpdatedAt, cwd, { forceDirtyWhenNotAdvanced: true });
> --- `packages/coding-agent/src/memories/storage.ts`

#### MEM-RTE-local-lessons
Label: Local lessons

Endpoints/progression: explicit local save/learn content → normalization/redaction/caps → serialized newest-first learned.md update → later cached guidance. Owner: local backend; caller/model proposes, code admits normalized nonempty content. No independent counterpart in supplied routes: [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) supplies generic tool execution, not this retention mechanism. SRC-1, `packages/coding-agent/src/memories/index.ts`, `packages/coding-agent/src/memory-backend/local-backend.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored count and learned.md confirmation after write, or empty-content rejection.
- Later read-back: lessons enter a later snapshot's system memory guidance, subordinate to current repository/user evidence by prompt doctrine.
- Delegated visibility: same-process per-path chains serialize sibling writes; this is not a cross-process lock.
- Selection predicate: project memory root; newest-first bullets; summary gets injection budget first and lessons get the remainder.
- Invalidation or expiry: bullet deduplication and 100-bullet cap; explicit clear removes memory root; ordinary consolidation does not overwrite learned.md.
- Activation or effect: later instructions contain selected lessons, but a save does not immediately change an already-frozen prompt snapshot.
- Evidence limits: generic caller identity leaves actual human authorship unresolved; normalization does not establish truth or safety of all natural-language content.

Admission differs from semantic review: injection delimiters and secrets are normalized, content is bounded, empty lessons rejected. The write preserves hand-edited prose outside managed bullets. Guidance asks verification against current repository evidence; no answer oracle or measured benefit gate admits lessons. Snapshot caching preserves prompt bytes after conversation starts, with explicit cache-clear and pre-conversation startup refresh exceptions.

> const learnedBudget = Math.max(0, cfg.summaryInjectionTokenLimit - Math.ceil(summaryOut.length / 4));
> --- `packages/coding-agent/src/memories/index.ts`

> if (cached && cached.sessionFile === sessionFile) return cached.value;
> --- `packages/coding-agent/src/memories/index.ts`

#### MEM-RTE-hindsight-retention
Label: Hindsight retention

Endpoints/progression: configured primary state → every-N-user-turn event or forced enqueue → formatted full-session/incremental cache or overlap window → asynchronous service retain; explicit retain/learn queue uses batch retention. Owner: adapter state and external service. No supplied counterpart after comparison with [RT-RTE-session-turn](runtime.md#rt-rte-session-turn); the service request is not an established upstream transformation outcome. SRC-1, `packages/coding-agent/src/hindsight/backend.ts`, `packages/coding-agent/src/hindsight/state.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: queued or acknowledged service request and local cursor update; async true is not proof of durable upstream memory.
- Later read-back: bank/tag-scoped recall and reflect requests can return service-selected material; first-turn recall is persisted locally.
- Delegated visibility: children alias parent bank/configuration; auto-retain/auto-recall stay with parent, while explicit tools can use the shared bank.
- Selection predicate: configured service, autoRetain flag, user-turn threshold, retainMode and overlap; forced enqueue reformats current session regardless of incremental cache.
- Invalidation or expiry: scope changes and disposal affect local state; clear drains queued writes and clears local recall state, not upstream bank; upstream deletion/expiry uninspected.
- Activation or effect: session traces are submitted for later service memory; actual extraction, durable retention and future influence are unobserved.
- Evidence limits: upstream transformation, quality gates and semantic lineage remain outside the boundary; reported tool queueing is not successful retention.

Admission: caller/model content or configured automatic transcript selection triggers adapter I/O. No per-item human decision is established by startup or event subscription. Server admission and rejection rules are opaque here; adapter catches/logs failed retains. Forced retention resets incremental state to permit rebuild after missing upstream documents. Full-session and windowed inputs have distinct document IDs; neither proves trace content becomes validated knowledge.

> await this.client.retain(this.bankId, transcript, {
> documentId,
> context: this.config.retainContext,
> metadata: { session_id: this.sessionId },
> tags: this.retainTags,
> timestamp: sourceTimestamp,
> async: true,
> });
> --- `packages/coding-agent/src/hindsight/state.ts`

#### MEM-RTE-mnemopi-retention
Label: Mnemopi retention

Endpoints/progression: backend initialization/scoped SQLite banks → explicit save/retain/learn or every-N-user-turn transcript retention → remember with extraction/embedding inputs → queued extraction/flush → startup or requested sleep → later scoped recall. Owner: coding adapter and bundled Mnemopi core. Distinct from [RT-RTE-session-turn](runtime.md#rt-rte-session-turn), with unresolved core transformations retained rather than attributed from names. SRC-1, `packages/coding-agent/src/mnemopi/backend.ts`, `packages/coding-agent/src/mnemopi/state.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: row ID or failure for explicit save; transcript remember and retained-turn cursor updates for automatic retention; enqueue requests full retain/flush/sleep.
- Later read-back: selected row previews enter recall; full row content is available by ID; derived facts may enter the same retrieval surface but core derivation/selection is unresolved.
- Delegated visibility: children alias parent scoped state; explicit writes can affect shared banks, whereas automatic child transcript retention is skipped.
- Selection predicate: configured retain/recall/global scopes, autoRetain flag and user-turn threshold; adapter restores retained cursor and chooses unseen transcript suffix.
- Invalidation or expiry: startup promotes age-eligible working rows before later writes can TTL-trim them; disposal can flush without sleep; database clear removes scoped DB files and attempts reinitialization.
- Activation or effect: raw trace plus extraction/embedding inputs can persist across sessions and be recalled; no observed improvement or complete retention guarantee.
- Evidence limits: TTL, extraction, triples, embeddings and sleep internals were not fully read; core algorithms and alternative CLI/MCP admissions remain unresolved.

Admission: explicit save trims empty input and labels accepted content veracity user/fact; automatic transcript retention labels unknown/episode. These labels do not authenticate a human author or establish factual truth. User-only extraction is not full-trace extraction: assistant/tool content can remain in stored transcript while being excluded from the extraction text. Code/model admissions are separate from human approval. No reference outcome oracle is established. The inspected sleep/flush calls establish lifecycle wiring, not semantic validation or reliable consolidation.

> veracity: "unknown",
> memoryType: "episode",
> --- `packages/coding-agent/src/mnemopi/state.ts`

> await memory.flushExtractions();
> if (options.sleep === false) continue;
> if (options.full) {
> memory.sleepAllSessions(false);
> } else {
> memory.sleep(false);
> }
> --- `packages/coding-agent/src/mnemopi/state.ts`

#### MEM-RTE-backend-recall
Label: Backend recall

Endpoints/progression: first eligible prompt plus recent transcript → scoped query composition/truncation → Mnemopi local retrieval or Hindsight service recall → rendering/budget → staged commit → persisted recall → later system instructions; explicit recall/reflect returns tool text instead. Owner: adapter selector and backend, not an unsolicited external push. Automatic first-turn supply is runtime-triggered even when the foreground agent does not call recall. Distinct from [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): this record owns retained-input selection before that turn. SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/coding-agent/src/mnemopi/backend.ts`, `packages/coding-agent/src/hindsight/state.ts`, `packages/coding-agent/src/hindsight/backend.ts`, `packages/coding-agent/src/memory-backend/recall-entry.ts`, `packages/coding-agent/src/tools/memory-reflect.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: staged context with commit callback; explicit recall/reflect returns formatted memory text or service-generated answer.
- Later read-back: same-scope persisted recall is reused on resumed transcript; Mnemopi reports changed tracked previews through a new notice instead of rewriting historical block.
- Delegated visibility: child aliases suppress duplicate automatic recall; parent recall snippet can supply child backend instructions, not all bank content.
- Selection predicate: autoRecall enabled, first-turn flag, nonempty prompt, bank/tag/database scope, bounded recent-turn query; Mnemopi scoped results/limits and injectionTokenLimit; Hindsight recall budget/maxTokens/types/tags.
- Invalidation or expiry: generation/state-identity mismatch rejects commit; reset or missing followed turn requires fresh recall; scope mismatch prevents reuse; Hindsight cannot report ID-based changes on reused recall.
- Activation or effect: selected retained prose becomes model guidance/background; no observed action dependence or benefit.
- Evidence limits: ranking internals and upstream semantics remain unresolved; compaction-time recall is a distinct supported adapter operation but complete downstream use by all strategies was not traced.

Mnemopi records the delivered, budget-cut prefix and tracks partially shown memories. Hindsight persists text with an empty tracked list. Mnemopi reflect merely formats retrieved results in the inspected branch, whereas Hindsight calls a service reflect operation: the shared label does not establish the same synthesis mechanism or retained reflection. [MEM-OBJ-mental-models](#mem-obj-mental-models) is a separate stable Hindsight cache preceding volatile recall in instruction assembly, not a tracked first-turn recall entry. Generation-checked load/publication, configured rendering bound and timeout fallback are inspected; full seed admission and upstream derivation remain unresolved.

> const record = recall && this.#deliveredRecall(recall, budget);
> --- `packages/coding-agent/src/mnemopi/state.ts`

> if (persist) persistRecall(this.session.sessionManager, this.#recallScope(), { text: context, memories: [] });
> --- `packages/coding-agent/src/hindsight/state.ts`

> const summary = state.formatContextScoped(results);
> --- `packages/coding-agent/src/tools/memory-reflect.ts`

#### MEM-RTE-memory-edit
Label: Memory edit

Endpoints/progression: memory_edit operation/ID → scoped bank lookup → store-specific eligibility → redacted update, forget or invalidate → later store lookup/recall and change reporting. Owner: foreground tool plus adapter/core. Closest supplied route is [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), which mediates execution rather than defining this retention change. SRC-1, `packages/coding-agent/src/mnemopi/state.ts`, `packages/coding-agent/src/tools/memory-edit.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated/deleted/invalidated, not_found or not_editable result, with bank/store context.
- Later read-back: future live retrieval can reflect retirement; already-persisted prompt recall remains historical text, with tracked-change notice on reuse.
- Delegated visibility: alias tools can affect banks shared with parent; no independent child-bank isolation follows.
- Selection predicate: ID lookup in deduplicated retain/recall/global targets; facts are read-only; update/forget require working store; invalidate reaches eligible other rows.
- Invalidation or expiry: superseded_by and valid_until signal retirement; update redacts replacement content; no general edit undo is established.
- Activation or effect: modifies what later live retrieval can use, not necessarily what all open model contexts already contain.
- Evidence limits: core deletion propagation to embeddings/triples/episodic copies and alternative MCP validation routes are uninspected; no universal withdrawal guarantee.

Admission: model/caller proposes operation; scoped eligibility and content checks decide executor admissibility, with generic tool-policy control from the supplied route. Starting a session is not human approval of a replacement. Full-row memory:// reads let an agent inspect unseen bytes before replacing a clipped preview, but do not require it to do so or establish semantic criticism. No correctness oracle is established.

> if (store === "fact") {
> --- `packages/coding-agent/src/mnemopi/state.ts`

> if ((op === "update" || op === "forget") && store !== "working") {
> --- `packages/coding-agent/src/mnemopi/state.ts`

#### MEM-RTE-decision-memory
Label: Decision memory

Endpoints/progression: committed top-level user message → envelope with prior human/assistant referent snippets → extraction model → admitted deltas → queue → scheduler/forced consolidation with current files/project docs → replacement files → later budgeted developer instructions or search. Owner: Sharpshooter adapter/model calls; code owns admission and publication. Distinct from supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): asynchronous decision extraction operates beside foreground work. SRC-1, `packages/coding-agent/src/sharpshooter/backend.ts`, `packages/coding-agent/src/sharpshooter/extract.ts`, `packages/coding-agent/src/sharpshooter/consolidate.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asynchronous extraction and queued deltas; consolidation reports ran/reason/status metadata.
- Later read-back: populated architecture/product/style files are concatenated and approximately token-truncated into instructions; search returns matching lines, not semantic retrieval.
- Delegated visibility: automatic extraction/scheduler startup skip taskDepth > 0; instruction consumer can include selected child/advisor prompts through SDK assembly.
- Selection predicate: user message, non-slash prompt at least 16 characters, no in-flight extraction; previous-human/assistant referent context bounded to 400/800 characters with code omitted; consolidation interval/lock/nonempty queue/model checks.
- Invalidation or expiry: malformed or non-occurring evidence rejected; invalid replacement names/duplicates/line counts rejected; all-empty replacements cannot wipe populated memory; consumed queue files are removed after writes.
- Activation or effect: project decisions enter guidance to follow unless user overrides; actual fidelity, changed behavior and useful recall remain unobserved.
- Evidence limits: occurrence checks do not validate inference; sequential file renames are not a multi-file atomic transaction; not every queued reason necessarily survives consolidation.

Admission: extraction model proposes statements, code checks evidence occurrence, kind/source/friction structure; a user-authored triggering sentence is not approval of its model interpretation. Consolidation model proposes whole files, code redacts, validates and stages them. No separate reference-answer oracle or human content-review gate is established. Temp-file cleanup handles failed staging, not rollback of all earlier successful renames. Rejection can retain queue input for retry. The files' strong instruction label is qualified by their actual natural-language consumer authority.

> if (typeof raw.evidence !== "string" || !raw.evidence || !currentPrompt.includes(raw.evidence)) {
> --- `packages/coding-agent/src/sharpshooter/extract.ts`

> for (const file of staged) await fs.rename(file.tempPath, path.join(bankDir, file.name));
> --- `packages/coding-agent/src/sharpshooter/consolidate.ts`

#### MEM-RTE-autolearn-capture
Label: Autolearn capture

Endpoints/progression: substantive primary stop → live settings/abort/plan/goal gates → detached message snapshot/private provider session → capture model with current capture tools → learn/manage_skill → durable lesson or managed skill → later recall/discovery. Owner: controller, SDK capture runner and tool primitives. Distinct from [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn): private capture is not a parent task return/artifact route. SRC-1, `packages/coding-agent/src/autolearn/controller.ts`, `packages/coding-agent/src/sdk.ts`, `packages/coding-agent/src/tools/manage-skill.ts`, `packages/coding-agent/src/autolearn/managed-skills.ts`, `packages/coding-agent/src/prompts/system/autolearn-nudge-autocontinue.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: private capture completion or logged error, not a continuation reply or acceptance of pending user decisions.
- Later read-back: saved lessons follow selected backend paths; managed descriptions/paths enter discovery and bodies can be invoked later, with complete body consumption uninspected.
- Delegated visibility: detached context isolates capture conversation/provider state; shared durable write tools allow results to escape that frame.
- Selection predicate: top-level controller, live enabled/autoContinue settings, minimum tool-call threshold, non-aborted stop, outside plan/goal modes; tools resolved per capture; no capture if tools/model absent.
- Invalidation or expiry: disabled/passive mode does not insert hidden reminders; private provider state closes at completion; managed create collision, unsafe path/link, empty content and size violations reject writes; delete removes managed skill and refreshes discovery.
- Activation or effect: raw operating trace can automatically produce durable behavior-shaping prose; improvement of future capacity is not established.
- Evidence limits: capture model's decision to save useful content is requested, not demonstrated; full learn two-write recovery and skill body invocation remain unresolved.

Admission: model proposes lesson/skill, software checks format/location/size/authored-name precedence and applicable tool policy. manage_skill is a write capability and requires autolearn.enabled; it is backend-independent. The managed file limit is 64,000 final UTF-8 bytes. Mutation chains are in-process. Guidance says capture only genuinely reusable content and do nothing otherwise, then stop. Synthetic capture is explicitly not a human answer or approval. No answer oracle or beneficial-content evaluator admits files. This establishes trace-fed update wiring, not learning, autonomous theory criticism or exercised self-improvement.

> Automated capture turn — not a user reply; user has not responded to your previous turn. Do not treat this prompt as their answer, approval to continue, or acceptance of any pending action; only the user can do so.
> --- `packages/coding-agent/src/prompts/system/autolearn-nudge-autocontinue.md`

> messages: captureMessages,
> --- `packages/coding-agent/src/sdk.ts`

#### MEM-RTE-notebook-update
Label: Notebook update

Endpoints/progression: context_notes read/replacement request → owning live branch check → UTF-8 budget/abort/recheck → journal append/flush → later latest-revision injection; new_context requests a fresh window separately. Owner: foreground tool and lifecycle. Distinct from [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch): branch ownership and notebook admission are additional controls. SRC-1, `packages/coding-agent/src/tools/context-notes.ts`, `packages/coding-agent/src/session/context-notes.ts`, `packages/coding-agent/src/session/session-context.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: notebook text on read, saved entry ID on replacement, or requested flag for new_context.
- Later read-back: latest valid notebook is inserted during context rebuild/resume; empty text explicitly clears notebook.
- Delegated visibility: session identity check prevents advisor tools from using the parent's journal; each owned branch is separate.
- Selection predicate: experimental context management enabled, not disposed, matching owner/session manager, unchanged branch leaf after ensureOnDisk; replacement budget 16,384 UTF-8 bytes.
- Invalidation or expiry: changed branch, disposal, abort, wrong owner or oversize reject save; latest reset terminates notebook lookup; earlier journal versions remain trace, not active notebook.
- Activation or effect: selected notebook text survives discarded turns and can guide later inference; completeness and reliance are unobserved.
- Evidence limits: fresh-window lifecycle production is not fully traced; writing notes does not prove they contain all necessary reasoning.

Admission: model/caller chooses full replacement, code owns byte/identity checks; tool class distinguishes read from write approval. Generic wrapper policy may require human approval but no per-notebook semantic reviewer or reference outcome is established. Guidance recommends raw-history recovery for details exceeding notebook budget. This is author-directed curation, not automatic summarization merely because it is durable.

> const data: ContextNotesEntry = { version: 1, text: params.text };
> const entryId = manager.appendCustomEntry(CONTEXT_NOTES_ENTRY_TYPE, data);
> await manager.flush();
> --- `packages/coding-agent/src/tools/context-notes.ts`

#### MEM-RTE-artifact-read
Label: Artifact read

Endpoints/progression: foreground internal URL read → backend/caller or experimental branch checks → local file, scoped Mnemopi row or full current-branch formatting → resource text → read-tool consumer. Owner: internal URL handlers and caller tool. Distinct from [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch): describes selected retained content, not generic execution. SRC-1, `packages/coding-agent/src/internal-urls/memory-protocol.ts`, `packages/coding-agent/src/internal-urls/history-protocol.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resource text/metadata or wrong-scope/backend/not-found error.
- Later read-back: explicit request restores details absent from summary, clipped recall or active context; full current history is branch-bound.
- Delegated visibility: bound caller limits memory lookup; legacy contextless paths sweep registry roots/states and do not provide the same narrow ownership guarantee.
- Selection predicate: local memory://root file path, Mnemopi memory ID within caller scoped banks, or exactly history://current/full with experimental branch binding.
- Invalidation or expiry: off rejects memory protocol; known non-local callers cannot use leftover local files; Hindsight IDs reject with recall/reflect guidance; path/availability checks can fail.
- Activation or effect: retained raw or derived details become returned context; restored detail does not imply downstream correctness.
- Evidence limits: full generic read shaping/budgets and other history agent-roster routes are not fully inspected; no all-session access-isolation guarantee.

> if (backend !== undefined && backend !== "local") {
> throw fileBackedRootUnavailableError(backend);
> }
> --- `packages/coding-agent/src/internal-urls/memory-protocol.ts`

> const content = formatCurrentBranchFullHistory(branch);
> --- `packages/coding-agent/src/internal-urls/history-protocol.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-guidance
Label: Memory guidance

Consumer: foreground/child inference model, and advisors where SDK supplies the memory block. Channel: backend-built instructions appended to prompt, recalled text/tool results and reconstructed checkpoint/notebook messages. Force: natural-language guidance/background, not executable dispatch policy. Horizon: later requests and sessions reusing retained state; operation and behavior dependence unobserved. Distinct from [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance): this is the retained-memory-specific supply path, not a replacement for general prompt authority. Possible overlapping referent at the final prompt/model channel is retained for reconciliation. SRC-1, `packages/coding-agent/src/sdk.ts`, `packages/coding-agent/src/prompts/memories/read-path.md`, `packages/coding-agent/src/sharpshooter/backend.ts`.

Local doctrine subordinates memories to present facts and instructions, whereas Sharpshooter requests following project decisions unless user overrides. These are different requested authorities; neither is reliable compliance.

> Memory: heuristics/process context; current repo files, runtime output, user instruction: factual state/final decisions.
> --- `packages/coding-agent/src/prompts/memories/read-path.md`

> "Project decision memory (sharpshooter). These are friction-earned decisions; follow them unless the user overrides.",
> --- `packages/coding-agent/src/sharpshooter/backend.ts`

## Annotations

#### On [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn)

Memory-specific boundary: isolated child context resembles a separate working frame with selected input and bounded return, but persisted child sessions/artifacts can be reopened rather than discarded. Parent bank aliases are another escape from frame isolation: Hindsight/Mnemopi children can perform explicit memory operations on shared parent-backed scopes, while their automatic recall/retention is suppressed. Source: SRC-1, `packages/coding-agent/src/hindsight/backend.ts`, `packages/coding-agent/src/mnemopi/backend.ts`. Separate message arrays are not separate durable knowledge stores.

> aliasOf: parent,
> --- `packages/coding-agent/src/hindsight/backend.ts`

#### On [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt)

Memory consumer: SDK renders backend memoryInstructions and appends them to base instructions; it also formats a memory block for advisor prompts. Lineage: current configured backend and its selected/cached retained content. Natural-language delivery is not a hard policy guarantee. Managed descriptions represent availability metadata rather than proof a skill body was read. Source: SRC-1, `packages/coding-agent/src/sdk.ts`.

> advisorMemoryPrompt = formatAdvisorMemoryPrompt(memoryInstructions);
> --- `packages/coding-agent/src/sdk.ts`

> if (memoryInstructions) appendParts.push(memoryInstructions);
> --- `packages/coding-agent/src/sdk.ts`

## Write side

The automatic trace-fed paths retain more than raw logs. Local startup derives memory summaries and procedures from earlier rollouts; Mnemopi schedules extraction with separate transcript/extraction/embedding inputs; Hindsight submits transcripts to an opaque service; Sharpshooter derives decision files; private auto-learn capture can retain lessons and skill documents. Their respective downstream consumers are identified in [MEM-RTE-local-consolidation](#mem-rte-local-consolidation), [MEM-RTE-mnemopi-retention](#mem-rte-mnemopi-retention), [MEM-RTE-hindsight-retention](#mem-rte-hindsight-retention), [MEM-RTE-decision-memory](#mem-rte-decision-memory) and [MEM-RTE-autolearn-capture](#mem-rte-autolearn-capture). Only the first, fourth and fifth have inspected adapter-side model-output-to-file chains; Mnemopi core and Hindsight upstream semantic transformations remain unresolved.

Manual/foreground write surfaces coexist: notebook replacement, retain/learn, managed skill mutation, memory_edit, exposed backend save and alternate Mnemopi CLI/MCP/module APIs. Human authorship, human admission and physical persistence must not be conflated. An automatic pipeline can transform user-authored evidence without a human approving the transformed sentence; a model can write through a policy-admitted tool without an independent correctness check.

Withdrawal is consumer-relative. Local no-output extraction removes a prior row and dirties consolidation; an empty consolidation input cleans generated artifacts. Lesson bullets expire by cap; managed delete refreshes discovery. Sharpshooter consumes admitted queue inputs after replacement writes but preserves no verified semantic rollback. Mnemopi editing treats facts, working and episodic rows differently, and historical prompt snapshots can retain retired text. Hindsight clear removes local state, not upstream memory. These facts defeat a uniform claim that clear/delete immediately erases all later behavioral influence.

Compaction creates retained working memory when its checkpoint reaches a later invocation. Text, image archives and provider-native payloads are alternative checkpoint parts, not interchangeable summaries. Notes-backed context can instead preserve an authored notebook and latest request while dropping a disposable prefix. Raw full-history access can recover removed material; nothing in the model window behaves like an automatically dereferenceable heap pointer. A path string permits a future tool request, not automatic liveness or recovery.

Reasons may be carried but are not guaranteed. Sharpshooter's optional rationale reaches its consolidator; a lesson may explain what/when/why; summaries/notes may retain reasons. No inspected producer-to-consumer contract proves exhaustive rationale preservation. Original traces remain separate evidence even when a short derived artifact omits them.

## Read-back

Automatic supply is selector-driven, not plain accumulation. Local snapshots select by project root and shared summary/lesson budget. First-turn recall selects by prompt/history plus configured bank filters and limits, then preserves delivered text. Sharpshooter concatenates populated project files with an injection cap, not query-targeted selection. Notebook reconstruction chooses latest valid revision after reset; checkpoint reconstruction chooses branch/tail/payload, filters unsafe turns and budgets archive frames. These mechanisms can alter the model-visible context without any foreground recall tool call.

Explicit demand paths are different: recall/reflect tools query backend memory; memory://root reads selected local artifacts; memory://ID obtains full Mnemopi rows rather than clipped previews; history://current/full obtains raw selected branch text. The service's reflect answer is not established as a persisted derived artifact. The Mnemopi reflect branch is retrieved-context formatting, not an inspected extra model synthesis call.

Storage capabilities are not consumer routes. The inventoried Mnemopi module APIs and alternative MCP/CLI operations can persist, mutate and return data, but unspecified external callers do not establish automatic later agent consumption. Complete integration of those alternate paths remains unresolved. The report makes no deployed-use inference from exported methods.

## Integration issues

1. No supplied factual correction is required. The runtime explicitly deferred backend retention and compaction details; these records extend that account rather than overturn it.
2. [MEM-BAP-memory-guidance](#mem-bap-memory-guidance) overlaps [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) at the final inference channel. Its distinct upstream retained-material selectors support a narrower path; reconciliation should retain containment/overlap rather than silently treating it as independent model authority.
3. [MEM-RTE-context-rebuild](#mem-rte-context-rebuild) supplies the precise retained-context predecessor to [RT-RTE-session-turn](runtime.md#rt-rte-session-turn); it is not a duplicate turn route. Provider payload, archive and display summary must remain separate because visibility and budget differ. Full production algorithms remain uninspected and prevent a completeness/fidelity conclusion.
4. [MEM-OBJ-working-memory](#mem-obj-working-memory), [MEM-OBJ-episodic-memory](#mem-obj-episodic-memory), [MEM-OBJ-mnemopi-facts](#mem-obj-mnemopi-facts), [MEM-OBJ-memory-embeddings](#mem-obj-memory-embeddings) and [MEM-OBJ-binary-vector](#mem-obj-binary-vector) now own part-specific form/lineage/mutation limits. The bank ID remains a container without uniform form, edit authority or retirement guarantee. Mnemopi has unresolved material parts and alternatives: numerical embedding provenance/fixity, core fact extraction/triples, ranking/cache, sleep semantics, TTL and delete propagation, imports, CLI and MCP validation/shared memory. [MEM-OBJ-mnemopi-memory](#mem-obj-mnemopi-memory), [MEM-RTE-mnemopi-retention](#mem-rte-mnemopi-retention), [MEM-RTE-memory-edit](#mem-rte-memory-edit) retain adapter positives without pretending those parts share identical lineage, authority or withdrawal. Exact embedding model version, runtime parameter changes and mutable model endpoint resolution are uninspected for these untraced components, not established fixed.
5. [MEM-OBJ-mental-models](#mem-obj-mental-models) now separately owns Hindsight stable cache storage, generation/deadline publication and instruction delivery. Full seed admission, loader rendering internals and upstream transformation remain unresolved; first-turn recall persistence/tracking does not apply to this cache. Known stable cache delivery in [MEM-RTE-backend-recall](#mem-rte-backend-recall) must not be discarded because initialization is opaque, nor interpreted as validated knowledge. [MEM-RTE-hindsight-retention](#mem-rte-hindsight-retention) establishes submissions, not service durability or deletion.
6. Local extraction rows, intermediate files, summary, on-demand memory/procedures and script/template/example buckets are separately declared as parts of the valid local container. [MEM-OBJ-memory-summary](#mem-obj-memory-summary) owns automatic injection; [MEM-OBJ-local-scripts](#mem-obj-local-scripts) owns generated code with execution unresolved; [MEM-OBJ-local-templates](#mem-obj-local-templates) and [MEM-OBJ-local-examples](#mem-obj-local-examples) do not inherit prose form or execution authority from the container. Generated files are admitted by consolidation but execution and normal skill discovery are not traced. [MEM-OBJ-local-memory](#mem-obj-local-memory) and [MEM-RTE-artifact-read](#mem-rte-artifact-read) establish explicit reachability, not automatic execution. Managed skills have separately inspected discovery; full body-invocation wiring remains unresolved in [MEM-OBJ-managed-skills](#mem-obj-managed-skills).
7. Complete advisor, foreign-session, provider/context filtering, evaluation, branch-summary, skill-fork and cross-language host loops are uninspected. Supplied task and extension routes plus the inventory prevent their silent omission, but no global memory-control or learning conclusion follows. No additional record is a known duplicate after comparison with supplied objects/routes; possible downstream authority overlap is item 2. New parts refine valid containers without superseding their IDs.
8. [MEM-OBJ-decision-deltas](#mem-obj-decision-deltas) owns evidence-occurrence admission and optional rationale; [MEM-OBJ-project-decisions](#mem-obj-project-decisions) owns replacement validation and later instruction injection. [MEM-OBJ-decision-files](#mem-obj-decision-files) remains their combined lineage container. SRC-1 extraction/consolidation establishes distinct stages, not preservation of every delta reason or occurrence check in final model-visible files.

## Limitations and checks

HEAD was rechecked against the exact boundary revision and the source checkout had clean status. All newly inspected material is SRC-1 at that pin. No target, provider, tests, examples or services were executed; no observed activation, reliability, causal benefit or improved future capacity is claimed. Method inputs were read completely, with oversized runtime and record-contract ranges recovered separately. Source search/read is not an exhaustive audit; available uninspected paths remain explicit above.

Validation: passed the invocation-specific validate-output check. Deterministic checking establishes form, identities and quotation occurrence, not semantic support or acceptance. The report retains partial-loop limits and unresolved integration questions.
