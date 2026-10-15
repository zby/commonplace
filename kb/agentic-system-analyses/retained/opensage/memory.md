---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenSage's sandbox wiki, pinned files, trace-derived context and checkpoint consumers at the frozen repository boundary."
run-id: AAS-2026-10-14-opensage-291d1ed79d37-01
source-identity: "https://github.com/opensage-agent/OpenSage"
reviewed-boundary: "54d64702e18d195c8f0fed711c6db5dc1d62ab29"
---

# OpenSage memory report

## Boundary and evidence

The memory scope follows the enclosing runtime, including shipped direct drivers and exposed library operations. It covers sandbox Markdown, tool-output files, host session checkpoints, history folding, optional plugins, peer findings and benchmark-to-agent handoffs. It excludes implementation bodies of ADK, providers, Neo4j and external trainers, as the boundary does. Provider caches, embeddings and actual deployed retained content are unknown; no numerical memory-store representation is inferred from a service name.

SRC-1 supplies implementation and doctrine/design at `54d64702e18d195c8f0fed711c6db5dc1d62ab29`. HEAD was rechecked against that revision. Direct reads add the file-memory modules, complete summarization and compaction-patch bodies, session-service implementation, selected persistence/resume and manager loading ranges, optional tool/image plugins, hook injection/persistence, complete agent-tools functions, evaluation export, SWE-bench exploration and vulnerability-findings resume ranges. Supplied runtime findings cover dispatch, children, dynamic definitions, shell and training integration. There are no observed runs or causal experiments. Neither target code nor tests were executed.

### Coverage inventory

All paths in this table are SRC-1 commit-relative anchors. “Direct” means source text was read here; “supplied” means the linked runtime record supplies the account. An unresolved row remains inside the functional scope rather than becoming an exclusion.

| Entry point or operation | Source path and inspection basis | Records or local limit; conclusion prevented |
|---|---|---|
| Every patched `run_async`: seed layout, disclose paths, persist events | Direct: `src/opensage/patches/agent_run_async.py`; `src/opensage/memory/file_based/short_term/session_files.py`; `src/opensage/memory/file_based/short_term/prompt.py`; `src/opensage/memory/file_based/long_term/knowledge_store.py` | [MEM-OBJ-traj](#mem-obj-traj), [MEM-OBJ-todo](#mem-obj-todo), [MEM-OBJ-pinned](#mem-obj-pinned), [MEM-OBJ-knowledge-files](#mem-obj-knowledge-files), [MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance). Initialization is software-controlled; subsequent content is agent/caller-controlled. |
| Enabled after-event compaction and patched model-history fold | Direct: `src/opensage/features/summarization.py`; `src/opensage/patches/adk_llm_compaction.py`; supplied [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) | Annotation on that route; [MEM-OBJ-compacted-content](#mem-obj-compacted-content). Raw history is retained in session storage, not physically trimmed by this function. |
| Enabled after-tool output reduction and file reload | Direct: `src/opensage/plugins/default/adk_plugins/tool_response_summarizer_plugin.py`; `src/opensage/features/summarization.py` | [MEM-RTE-output-reduction](#mem-rte-output-reduction), [MEM-OBJ-tool-output](#mem-obj-tool-output), [MEM-OBJ-tool-summary](#mem-obj-tool-summary). Save failure removes the assured full-output fallback. |
| Host/root checkpoint, manager startup, CLI resume/review and disk tree display | Direct: `src/opensage/orchestration/persistence.py`; `src/opensage/orchestration/manager.py`; `src/opensage/cli/opensage_cli.py`; `src/opensage/memory/file_based/short_term/session_files.py` | [MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume), [MEM-OBJ-checkpoint-selectors](#mem-obj-checkpoint-selectors); supplied [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch). Review and tree summaries are human/UI consumers, not proof of model reuse. |
| Dynamic template admission/rebuild; shell-created capabilities | Supplied [RT-RTE-create-subagent](runtime.md#rt-rte-create-subagent), [RT-RTE-terminal-extension](runtime.md#rt-rte-terminal-extension) | Annotations on [RT-OBJ-agent-definition](runtime.md#rt-obj-agent-definition) and [RT-OBJ-agent-instruction](runtime.md#rt-obj-agent-instruction). They persist selectors/instructions or scripts, not an evaluated improvement. |
| Directed child frames, inheritance and incoming-message truncation | Supplied [RT-RTE-directed-child](runtime.md#rt-rte-directed-child) | Annotation retains selected inputs, final-text return and file-pointer limits. Frame isolation is optional and does not erase stored child history. |
| Exposed `log_finding` admission, duplicate rejection, analysis and broadcast | Direct: `src/opensage/toolbox/general/agent_tools.py` | [MEM-OBJ-findings](#mem-obj-findings), [MEM-RTE-finding-admission](#mem-rte-finding-admission). No shipped registration/caller found in bounded Python search; invocation is afforded, internal append/broadcast wiring is inspected. |
| Exposed critique, audit and claim validation | Direct: `src/opensage/toolbox/general/agent_tools.py` | [MEM-RTE-history-consultation](#mem-rte-history-consultation). They consume folded retained history, return advice, and do not themselves enforce pin-file admission. |
| Configured hook context retained as user events | Direct: `src/opensage/plugins/claude_code_hook_loader.py`; supplied [RT-RTE-host-extension](runtime.md#rt-rte-host-extension) | [MEM-RTE-hook-retention](#mem-rte-hook-retention), [MEM-OBJ-hook-context](#mem-obj-hook-context). Configured prompts are static guidance; command outputs can be use-derived retained material. |
| Optional image injection and request-time rejection | Direct: `src/opensage/plugins/default/adk_plugins/image_injection_plugin.py`; located producers in `src/opensage/toolbox/general/view_image.py` and `agent_library/local_support/local_cli.py` | [MEM-RTE-image-retention](#mem-rte-image-retention), [MEM-OBJ-image-parts](#mem-obj-image-parts). Actual plugin enablement and ADK content-copy behavior are unresolved; no universal image-preservation guarantee. |
| SWE-bench exploration before main task | Direct: `benchmarks/swe_bench_pro/swe_bench_pro.py` | [MEM-RTE-explore-handoff](#mem-rte-explore-handoff). Final text or a truncated-trace summary reaches the main agent. Claimed `search_memory` is not established by the read path. |
| Vulnerability findings saved/reloaded into PoC task | Direct: `benchmarks/secodeplt/vul_detection_memory.py` | [MEM-RTE-findings-resume](#mem-rte-findings-resume), [MEM-OBJ-vulnerability-findings](#mem-obj-vulnerability-findings). Schema admission and file existence can advance/skip stages without validating exploit success. |
| Base evaluation output collection and external training consumers | Direct: `src/opensage/evaluation/base.py`; supplied [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout) | Annotation distinguishes raw trace export from learned parameters. Remaining benchmark-specific reward/admission bodies are available but not exhaustively read; no universal evaluator or checkpoint-selection account. |
| Final compaction helper | Direct: `src/opensage/features/summarization.py`; bounded Python search across `src`, `agent_library`, `benchmarks` | [MEM-OBJ-compacted-content](#mem-obj-compacted-content). Returns a summary plus last-command display; no caller found in that search. This is an exposed transformation, not an established later-consumer route. |
| ADK memory/artifact/credential services; live Web path | Direct service construction: `src/opensage/session/opensage_session.py`; supplied [RT-RTE-live-runner](runtime.md#rt-rte-live-runner) | [MEM-CMP-memory-service](#mem-cmp-memory-service). Construction/passing a memory service is not admission/retrieval. Dependency internals and live retention prevent an end-to-end consumer claim. |
| Neo4j, code graph queries and symbol indexes | Direct: `src/opensage/session/opensage_session.py`; `benchmarks/common_tools/static_analysis.py`; `benchmarks/common_tools/retrieval.py` | Separate task-source context, not conversation-memory wiring. Custom query API is implemented; graph initialization/provenance and external graph internals remain unresolved. No trace-to-graph learning conclusion. |
| Other factory prompts, custom hooks/plugins, provider state and benchmark variants | Supplied boundary inventory; bounded Python mechanism searches | Available tracked surfaces were not exhaustively read. Their extension-specific admission/reload semantics remain unresolved; the report claims neither complete caller enumeration nor universal equality with manager paths. |

## Core ideas

1. **Locations are pushed; wiki contents are not.** The wrapper supplies per-agent paths and a shared session wiki location. The default policy asks agents to skim the index, open relevant files, and maintain expensive knowledge. This is a model-directed file workflow, not automatic retrieval or truth validation ([MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance)). “Long-term” describes intended reuse, not a guaranteed cross-session lifetime.
2. **Compaction transforms the read view while keeping its trace.** Older branch-compatible events become a model-produced summary. A patched fold substitutes that summary for their timestamp range and retains the recent tail. Pinned text is read independently and attached outside summarizer generation. Later expanded ranges subsume earlier summaries; earlier rationale is not guaranteed to survive this replacement ([RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction), [MEM-OBJ-compacted-content](#mem-obj-compacted-content)).
3. **A full-output path is a recovery opportunity, not a reference in the model window.** Tool results can become inferred-intent summaries or a 200-character preview; a sandbox file keeps the original only when saving succeeds. A later agent must actually issue a read/search command ([MEM-RTE-output-reduction](#mem-rte-output-reduction)).
4. **Restart restores selected state, not every pending effect.** Host trajectories and definitions can be loaded. CLI snapshots sanitize unmatched calls, rebuild uses current registries, and startup clears inboxes. A surviving wiki additionally requires its sandbox to survive or be reattached ([MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume)).
5. **There are additional admission surfaces beyond the wiki.** `log_finding` combines model duplicate rejection with retained contradiction/completion analysis and best-effort peer delivery. Benchmarks reload structured findings or push exploration summaries. These mechanisms have different selectors, authorities and failure modes; none establishes measured learning merely by retaining text.

## Shared records

### Components

#### MEM-CMP-memory-service
Label: ADK memory service

Source-native identity: environment-owned `InMemoryMemoryService`, passed to manager runners. Storage substrate: dependency-owned process memory. Representational form and payload lineage: uninspected in the excluded ADK implementation; the Python object and its name are not evidence of embeddings, weights or a particular retrieval algorithm. Parameter mutability/version fields are inapplicable to the inspected service handle, not a finding about an opaque numerical payload. No counterpart object in supplied runtime; [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch) supplies its runner placement.

Evidence: SRC-1 implementation, `src/opensage/session/opensage_session.py`, `src/opensage/orchestration/manager.py`. Passing this handle does not establish a writer or later memory consumer. Neo4j is explicitly assigned a different role:

> # Neo4j client manager is retained for code-property-graph uses
> # (joern / codeql sandboxes). It is NOT used for conversation memory.
> --- `src/opensage/session/opensage_session.py`

### Operative objects

#### MEM-OBJ-traj
Label: Session trajectory

Source-native identity: serialized ADK session `traj.json` in sandbox per-agent directories and nested host instance directories. Storage substrate: sandbox files and host `~/.local/opensage/sessions/{osid}/instances/.../traj.json`; live session-service objects are another checkpoint form. Representational form: symbolic JSON event/state envelope, containing natural-language user/model/tool text and symbolic call/response metadata; image payloads and summary payloads are separate operative parts below. It is a raw execution record relative to the session writer, not necessarily raw original tool output: tool reduction may already have replaced it. Lineage: wrapper serialization periodically to host every three yielded events, and finally to host and sandbox; separate manager save/load shares the host filename. Best-effort writes are not transactional with external effects.

Consumers: manager resume, CLI root snapshots, display/tree scanning and evaluation exports; later model history is selected/folded rather than simply the entire JSON. Distinct from the template selectors in [RT-OBJ-agent-definition](runtime.md#rt-obj-agent-definition); overlaps the persistence described by [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch) without replacing that execution route.

Evidence: SRC-1 implementation, `src/opensage/patches/agent_run_async.py`, `src/opensage/memory/file_based/short_term/session_files.py`, `src/opensage/orchestration/persistence.py`.

> text = (dir_ / "traj.json").read_text(encoding="utf-8")
> return Session.model_validate_json(text)
> --- `src/opensage/orchestration/persistence.py`

#### MEM-OBJ-compacted-content
Label: Compacted history content

Source-native identity: `EventCompaction.compacted_content`, start/end timestamps, branch and invocation fields. Storage substrate: live session event list and serialized trajectories. Natural-language summary is the model-interpreted part; symbolic range/branch metadata determines code selection, not truth. Lineage: older user/model text and tool calls/responses rendered into a summarizer request, with folded background text and optional quota guidance. It is derived memory, separate from the raw event container [MEM-OBJ-traj](#mem-obj-traj); supplied [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) names the producing route but declares no object counterpart.

The prompt asks for decisions, rationale and failed attempts, but faithful retention is not checked. Later content construction replaces the selected timestamp range with a summary event and keeps the tail. An expanded next range can discard a previous summary even though the summarizer is explicitly told not to re-summarize background context. Thus earlier content/reasons cannot be assumed cumulative. Original events remain reachable through the session/file or explicit tools; they are not guaranteed in the model window.

Evidence: SRC-1 implementation/doctrine, `src/opensage/features/summarization.py`, `src/opensage/patches/adk_llm_compaction.py`.

> "target window under [WindowToSummarize]. Only summarize the content "
> "under [WindowToSummarize]; do not re-summarize [Context].\n\n"
> --- `src/opensage/features/summarization.py`

> if (
>     other["start"] <= m["start"]
>     and other["end"] >= m["end"]
>     and j_m > i_m
> ):
>     subsumed = True
>     break
> --- `src/opensage/patches/adk_llm_compaction.py`

Alternative exposed helper `generate_final_compaction` filters marker events, summarizes original branch events, and appends a last-command display. That display truncates long `output` to 400 characters and may write `last_command_full_output.txt` on the host. Its backwards scan selects a call and response independently, not by matching IDs. No caller was found in bounded Python searches across `src`, `agent_library`, `benchmarks`; no checkpoint-to-next-agent route is attributed to this helper. Evidence: SRC-1, `src/opensage/features/summarization.py`.

#### MEM-OBJ-pinned
Label: Pinned task content

Source-native identity: per-agent `pinned.md`. Storage substrate: sandbox Markdown file, copied into compaction-event text. Representational form: natural-language operational content, potentially literal commands, credentials and URLs; a command written here is not executed by the pin reader. Lineage/authorship: empty software seed; subsequent shell/editor content supplied by the agent or another filesystem writer. Initial content control beyond that seed depends on the deployment. Curation: explicit editing/emptying, requested by policy; no independent truth or length gate in the compaction reader. Consumer: later folded-history model input, via independent file read at successful compaction.

No counterpart object in supplied runtime; pin handling is one retained-input part of [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction), not a second execution route. The policy's approximately 2000-character bound is guidance. `_read_pinned_content` returns stripped content, skips missing/empty/read-failed files, and does not enforce that size.

Evidence: SRC-1, `src/opensage/memory/file_based/short_term/session_files.py`, `src/opensage/features/summarization.py`, `src/opensage/templates/auto_insert_prompts/default.md`.

> if exit_code != 0 or not output or not output.strip():
>     return None
> return output.strip()
> --- `src/opensage/features/summarization.py`

#### MEM-OBJ-todo
Label: TODO task notes

Source-native identity: per-agent `TODO.md`; natural-language tasks/progress stored as sandbox Markdown. Lineage: code seeds a generic checklist only when the file is absent, then agents may edit. Consumer afforded by the policy: foreground or continuing agent using shell/editor reads; path injection does not deliver contents. Storage survival follows sandbox lifetime. Unlike [MEM-OBJ-pinned](#mem-obj-pinned), no automatic file-content embed into compaction was found in the inspected memory module and summarization body. No supplied object counterpart; related shell affordance is [RT-RTE-terminal-extension](runtime.md#rt-rte-terminal-extension).

Evidence: SRC-1, `src/opensage/memory/file_based/short_term/session_files.py`, `src/opensage/templates/auto_insert_prompts/default.md`.

> "- [ ] Capture the current task\n"
> "- [ ] Update progress as work proceeds\n"
> --- `src/opensage/memory/file_based/short_term/session_files.py`

#### MEM-OBJ-knowledge-files
Label: Shared knowledge files

Source-native identity: shared session `long_term/*.md` and `index.md`. Storage substrate: configured memory root in the main sandbox; not a global across-project database. Representational form: model-interpreted natural-language entries plus filename/one-line summaries used by an agent to decide whether to open files. The index is navigation metadata, not a separate warranted theory or ranking algorithm. Lineage: framework seed describes index layout; use-derived entries are requested of agents, including debugging roots and ruled-out hypotheses. Actual deployed entry content, authors and retained reasons are unobserved.

Consumers: future agent or peer in the surviving session, via explicit file reads. Authority is informational guidance interpreted by that consumer, not mandatory instruction or executable admission. No counterpart object in supplied runtime; [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) is the policy delivered to encourage these writes, not the files themselves.

Evidence: SRC-1 implementation and doctrine, `src/opensage/memory/file_based/long_term/knowledge_store.py`, `src/opensage/memory/file_based/short_term/prompt.py`, `src/opensage/templates/auto_insert_prompts/default.md`.

> - A summary of a long debugging session: root cause + the wrong hypotheses
>   you ruled out
> --- `src/opensage/templates/auto_insert_prompts/default.md`

#### MEM-OBJ-tool-output
Label: Saved tool output

Source-native identity: full `str(tool_response)` saved as an `.out` file under per-agent `tool_outputs`, identified by function-call ID. Storage substrate: sandbox file. Form: readable original response serialization, with symbolic fields and natural-language output; its wrapper is not a new derived claim. Lineage: tool execution result before the callback clears/replaces the dictionary. Physical save can fail. Later consumer: agent issuing a shell search/read against the provided path; there is no automatic dereference. No supplied object counterpart; broad file effects are covered by [RT-RTE-terminal-extension](runtime.md#rt-rte-terminal-extension).

Evidence: SRC-1, `src/opensage/features/summarization.py`.

> content=raw,
> tool_name=tool_name,
> output_dir=output_dir,
> file_id=tool_context.function_call_id,
> file_extension=".out",
> --- `src/opensage/features/summarization.py`

#### MEM-OBJ-tool-summary
Label: Reduced tool response

Source-native identity: rewritten result dictionary's `_tool_response_summary`, `result`, optional `_tool_response_file` and quota fields. Storage substrate: current tool result, then session events/trajectory when ADK records it. Form: natural-language inferred-intent summary or preview; symbolic tags/metadata signal reduction and filename but do not preserve the original fields' semantics. Lineage: model reduction using recent history and tool arguments; over 50000 characters it instead takes a 200-character prefix. Model failure falls back to a 1000-character prefix; missing canonical model returns without reduction after save. Thus not every saved output implies summary delivery.

Consumer: model receiving later tool/history content, which may request full-file reads. Claimed verbatim key retention is prompt guidance. No counterpart in supplied runtime; distinct from incoming peer-message truncation in [RT-RTE-directed-child](runtime.md#rt-rte-directed-child).

Evidence: SRC-1, `src/opensage/features/summarization.py`.

> tool_response.clear()
> tool_response["_tool_response_summarized"] = True
> tool_response["_tool_response_summary"] = tagged_summary
> if file_saved and output_file:
>     tool_response["_tool_response_file"] = output_file
> tool_response["result"] = tagged_summary
> --- `src/opensage/features/summarization.py`

#### MEM-OBJ-checkpoint-selectors
Label: Session checkpoint selectors

Source-native identity: root snapshot metadata/config, per-instance metadata and directory nesting. Storage substrate: host JSON/TOML files. Representational form: symbolic IDs, names, paths and resource selectors interpreted by load/reattach code. Lineage: current session/configuration serialization, not summarized experience. Consumer: CLI resume and manager loading; directory structure also drives UI topology and query/status display. These metadata are distinct from the retained text in [MEM-OBJ-traj](#mem-obj-traj), and from template-level [RT-OBJ-agent-definition](runtime.md#rt-obj-agent-definition). Resource IDs are references to surviving resources, not serialized sandbox contents or pinned provider implementations.

Evidence: SRC-1, `src/opensage/orchestration/persistence.py`, `src/opensage/cli/opensage_cli.py`, `src/opensage/memory/file_based/short_term/session_files.py`.

> "resolved_config_file": resolved_config_path.name,
> "runtime": collect_sandbox_runtime_metadata(opensage_session),
> --- `src/opensage/orchestration/persistence.py`

#### MEM-OBJ-findings
Label: Shared findings and analysis

Source-native identity: `/shared/findings.md` entries with timestamps and optional contradiction/completion analysis. Storage substrate: sandbox Markdown. Form: natural-language findings, dead-end assumptions and model-written analysis; timestamps and labels are display/access metadata. Lineage: caller supplies a finding; critique model compares against the current file. The same admission mechanism appends both finding and reasons together. Reasons can reach peer models via broadcast or later file reads; there is no enforced rule that the peer revises its reliance. File can be edited externally. No supplied counterpart: related [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch) supplies the generic message transport, not this admission operation.

Evidence: SRC-1, `src/opensage/toolbox/general/agent_tools.py`.

> "2. CONTRADICTION: Does the NEW finding invalidate the ASSUMPTION "
> "behind an earlier DEAD END?\n\n"
> --- `src/opensage/toolbox/general/agent_tools.py`

#### MEM-OBJ-hook-context
Label: Retained hook context

Source-native identity: configured SessionStart/PreToolUse prompt strings or PreToolUse command output retained in user events; PostToolUse text is injected into result dictionaries. Storage substrate: pending in-process lists, request content and session events. Form: natural-language guidance/output, independent of executable hook commands. Lineage: configuration content is static; command output depends on executed hook and task state, with unresolved content provenance per hook. Consumer: foreground model initially by transient request injection and later via session-history construction/compaction. No separate truth gate or reliable compliance. This is a retained part of [RT-RTE-host-extension](runtime.md#rt-rte-host-extension), not a substitute for its host-code identity.

Evidence: SRC-1, `src/opensage/plugins/claude_code_hook_loader.py`.

> parts=[types.Part(text="\n\n".join(parts_to_persist))],
> --- `src/opensage/plugins/claude_code_hook_loader.py`

#### MEM-OBJ-image-parts
Label: Retained image parts

Source-native identity: tool-produced `types.Part` objects via `temp:PARTS_FROM_TOOLS_ID`, retained as a user event. Storage substrate: process pending lists and session events, potentially trajectory serialization. Form: opaque binary image payload plus symbolic MIME/part wrapper and readable textual notices, not a retained natural-language visual summary. The payload is not model weights or an embedding. Lineage: tool-obtained image bytes; exact sources depend on the tool. Consumer: later multimodal model request after request-time size filtering. The notice describes rejection, not image content. No counterpart object in supplied runtime; [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver) covers one located image-producing driver without establishing plugin activation.

Evidence: SRC-1, `src/opensage/plugins/default/adk_plugins/image_injection_plugin.py`.

> if saved_parts := tool_context.state.get(PARTS_FROM_TOOLS_ID, None):
>     self._pending_request_parts.extend(saved_parts)
>     self._pending_history_parts.extend(saved_parts)
>     tool_context.state.update({PARTS_FROM_TOOLS_ID: []})
> --- `src/opensage/plugins/default/adk_plugins/image_injection_plugin.py`

#### MEM-OBJ-vulnerability-findings
Label: Vulnerability findings checkpoint

Source-native identity: `VulFinding` objects saved in `vulnerability_findings_*.json`. Storage substrate: benchmark host output directory; reloaded Pydantic objects and PoC user prompt. Form: symbolic structured fields govern stage selection; natural-language descriptions and related source locations inform the PoC model. Lineage: vulnerability-model response, last fenced JSON extraction, schema parsing, per-function error fallback to an empty finding, then serialization. Raw reasoning accumulation is not what the PoC prompt receives. No counterpart object in supplied runtime; this is the memory-bearing part of the direct-driver family in [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver).

Evidence: SRC-1, `benchmarks/secodeplt/vul_detection_memory.py`.

> "The vulnerabilities are as follows:\n"
> + vul_finding.model_dump_json(indent=2)
> + "\n\nPlease generate a PoC for this vulnerability, and run it with `run_poc_from_script`."
> --- `benchmarks/secodeplt/vul_detection_memory.py`

### Routes

#### MEM-RTE-wiki-maintenance
Label: Wiki maintenance and read

Endpoints/progression: invocation wrapper seeds/discloses layout and supplies configured policy → agent decides what to write/update/remove via granted file tools → shared wiki or per-agent task notes → later agent skims/opens selected files. Owner: code owns layout and policy delivery; foreground agent decides content and selection; sandbox mediates physical effects. Related [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) describes policy authority; this route is distinct content admission/read opportunity, not duplicated instruction delivery.

- Immediate return: tool results/status for file operations; initialization itself yields no knowledge entry.
- Later read-back: afforded — policy names future/peer agent readers and index-then-entry selection; no automatic index/entry ingestion is established by path injection.
- Delegated visibility: wiki is shared within the OpenSage session; task notes are per-agent paths, not a proven filesystem access restriction.
- Selection predicate: agent judges expense to re-derive and relevance of index summary; filenames address files, without software semantic ranking or enforced budget.
- Invalidation or expiry: agent is asked to edit/remove stale files and index lines; sandbox cleanup/loss can remove access; no versioned rollback or cross-session lifetime guarantee.
- Activation or effect: files can supply informational content when explicitly read; actual curation, changed reliance and benefit are unobserved.
- Evidence limits: guidance is not compliance; custom/empty policy can change/disable maintenance; shell edits can bypass the requested layout and index synchronization.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: trigger is finishing a non-trivial subtask or receiving pin-worthy details. Model/caller proposes text; ordinary filesystem writes admit it without a semantic evaluator or mandatory human per-entry approval. Upstream operator chooses grants/policy, not each entry. Rejection is I/O failure; recovery is further editing/removal, not an automatic evidence-based rollback. Operating mode: open tasks. Answer oracle: inapplicable — no expected-result comparison in the seed/write path. Guidance asks for costly reusable knowledge, reasons for dead ends, and correction of stale entries; only written material persists. Actual formulated theories or criticisms cannot be inferred from the generic seed or prompt.

Evidence: SRC-1, `src/opensage/memory/file_based/long_term/knowledge_store.py`, `src/opensage/memory/file_based/short_term/prompt.py`, `src/opensage/templates/auto_insert_prompts/default.md`; shell execution support is supplied by [RT-RTE-terminal-extension](runtime.md#rt-rte-terminal-extension).

> - The summary line is what other agents skim first; keep it specific enough
>   to decide "should I open this file?" in one read.
> --- `src/opensage/templates/auto_insert_prompts/default.md`

#### MEM-RTE-output-reduction
Label: Tool output reduction

Endpoints/progression: enabled after-tool plugin → dictionary response threshold → save full serialized response → model summary or code prefix → rewritten result → later model history and optional explicit file read. Owner: plugin/code selects threshold/prefix; model infers intent and selects important content. No supplied route counterpart; peer-message reduction in [RT-RTE-directed-child](runtime.md#rt-rte-directed-child) has different input and transport.

- Immediate return: callback returns `None` after in-place mutation, allowing other callbacks to continue.
- Later read-back: derived response is retained through recorded tool events; file path affords later shell reload of the complete response when save succeeded.
- Delegated visibility: reduced events may cross to children through requested parent-history copying; output path is not automatically opened by a peer.
- Selection predicate: dictionary responses at/above configured `max_tool_response_length`; over 50000 characters uses 200-character preview; normal summary gets last ten events pruned from the front to 50000 context characters plus arguments/raw response.
- Invalidation or expiry: history folding may later replace result; saved file follows sandbox lifetime or deletion; failed save removes full-output fallback.
- Activation or effect: code replaces the model-visible dictionary, removing original keys; content influence and successful reload remain unobserved.
- Evidence limits: optional plugin, non-dictionary skip, no-model early return, summary exceptions and no hard output/token bound; raw data may already be transformed by earlier tools/plugins.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: code selects transformation; summarizer model drafts text without per-summary human approval. No reference oracle checks relevance or fidelity. Failure uses prefix fallback; nothing restores original dictionary after successful replacement. Operating mode: automatic open-task context management, not improvement selection. Guidance requests inferred intent, six-to-nine-sentence summary and key details verbatim; response text, path and quota metadata persist, not independent justification of correctness.

Evidence: SRC-1, `src/opensage/features/summarization.py`, `src/opensage/plugins/default/adk_plugins/tool_response_summarizer_plugin.py`.

> SKIP_SUMMARY_THRESHOLD = 50000
> if len(raw) > SKIP_SUMMARY_THRESHOLD:
> --- `src/opensage/features/summarization.py`

#### MEM-RTE-checkpoint-resume
Label: Checkpoint resume selection

Part of: [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch)

This recovery subroute of ordinary user dispatch selects retained session material rather than duplicating the full execution loop. Endpoints: latest/explicit saved-session selection → metadata/config/sandbox reattach → sanitized root session injection and eager instance load → later model invocation. Owner: CLI and manager; operator requests resume, not per-event admission. State effects: remap root app/user/session IDs, validate expected memory-directory state, restore sleeping instances and current template/model selection.

- Immediate return: restored environment/instances or missing/mismatched state/load errors.
- Later read-back: root `adk_session.json` or nested host `traj.json` becomes a live session whose retained events feed subsequent model construction/folding.
- Delegated visibility: nested instances and dynamic definitions can be reconstructed; pending inboxes do not survive startup.
- Selection predicate: latest saved directory by modification time or explicit session/path; manager matches session ID/directory metadata; already-present service session takes precedence over disk loading.
- Invalidation or expiry: missing files, incompatible memory state, unavailable models/tools or lost sandbox prevent faithful continuation; snapshot strips unmatched function calls; cleanup can remove sandbox contents.
- Activation or effect: implemented state restoration enables later history use; restart behavior/effect equivalence is unobserved.
- Evidence limits: root snapshot sanitization differs from manager trajectory load; current factory/config/registry affects reconstruction; metadata is not a backup of sandbox bytes and pending external effects are not replayed exactly once.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Checkpoint admission is software serialization/structural validation. Human chooses resume/configuration, not approval of each historical statement. Recovery can fall back to CLI config when resolved config is missing, or fail; semantic truth is not checked. Operating mode: recovery of open work; answer oracle: inapplicable. This is unchanged/raw checkpointing plus symbolic sanitation, not trace-to-new-knowledge generation.

Evidence: SRC-1, `src/opensage/orchestration/persistence.py`, `src/opensage/cli/opensage_cli.py`, `src/opensage/orchestration/manager.py`; supplied startup reset passage in [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch).

> if fc and getattr(fc, "id", None) and fc.id not in matched_response_ids:
>     removed_any = True
>     continue
> --- `src/opensage/orchestration/persistence.py`

#### MEM-RTE-finding-admission
Label: Finding admission and broadcast

Endpoints/progression: optional/exposed `log_finding(finding)` → read prior findings under a file lock → model duplicate/contradiction/completion judgment → suppress duplicate or append finding plus analysis → best-effort peer broadcast or later file read. Owner: calling agent/caller proposes; model judge can veto duplicate; code interprets response substrings and writes. No counterpart to this admission mechanism in supplied runtime; [RT-RTE-user-dispatch](runtime.md#rt-rte-user-dispatch) supplies later message transport.

- Immediate return: logged/duplicate/error and optional analysis; first entry or no-model fallback appends without ordinary broadcast.
- Later read-back: subsequent calls read the file for comparison; documented peer agents may read it; broadcast delivers text into later peer context when manager delivery succeeds.
- Delegated visibility: subsequent non-duplicate ordinary branch broadcasts original finding plus analysis to all peers; duplicate returns without append/broadcast.
- Selection predicate: entire existing file plus caller's new finding, with no explicit text budget; critique model from summarize config or first registered model; substring `DUPLICATE_OF` suppresses admission.
- Invalidation or expiry: model duplicate rejection prevents addition; external edits can withdraw content; no versioned rollback; pending broadcasts are cleared on restart with inboxes.
- Activation or effect: comparison, file append and peer delivery are implemented internally; actual registered invocation, peer changed reliance and correct criticism are unobserved.
- Evidence limits: bounded Python search found no shipped caller/registration; lock does not span read, model call and append, so concurrent comparisons can use stale inputs; broadcast exceptions are swallowed and append exit codes are not semantically verified.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission control: foreground caller supplies finding, model judges duplicate and reasons, code admits otherwise. No per-content human veto or expected-answer oracle. Operating mode: open task support. Guidance distinguishes findings, dead ends and missing pieces; the persisted result retains the proposed finding and model analysis, not a changed prior entry. Rejection/rollback are therefore not interchangeable: rejecting duplicate content is supported; automatically retracting a contradicted prior claim is not implemented in this function. Errors return `logged: False`; removal remains a filesystem operation.

Evidence: SRC-1, `src/opensage/toolbox/general/agent_tools.py`.

> if "DUPLICATE_OF" in result_text:
>     return {"logged": False, "duplicate": True, "reason": result_text}
> --- `src/opensage/toolbox/general/agent_tools.py`

> broadcast_msg = f"[log_finding] {finding}"
> if contradictions:
>     broadcast_msg += f"\n[contradiction] {contradictions}"
> --- `src/opensage/toolbox/general/agent_tools.py`

#### MEM-RTE-history-consultation
Label: History consultation tools

Endpoints/progression: caller requests `critique`, `audit_assumptions` or `validate_claim` → code branch-filters/folds retained events → selected registered model judges rendered history/claim → advice or parsed validity returned. Owner: caller chooses invocation/model/claim; code chooses representation; consulting model judges. These functions share the history-consumer mechanism, but not the finding-file admission of [MEM-RTE-finding-admission](#mem-rte-finding-admission). No supplied route counterpart.

- Immediate return: critique idea, audit text, parsed validity/confidence/reasoning or error.
- Later read-back: consulting model reads accumulated session history, including retained summaries; returned advice can enter later foreground tool history under normal recording, not a separate automatically maintained knowledge store.
- Delegated visibility: result goes to caller rather than a new managed child; no automatic peer broadcast.
- Selection predicate: branch-compatible session events folded by patched compaction; audit/validation truncate each rendered tool response to 1000 characters; critique retains rendered response text; explicit registered model name.
- Invalidation or expiry: later context folding can remove detailed evidence; invalid/empty model result returns errors or defaults; caller may ignore advice.
- Activation or effect: implemented consultation changes delivered tool content; neither pin edits nor changed reliance are enforced by these functions.
- Evidence limits: exposed library calls, actual factory registration unestablished by bounded search; truncated history and model judgment do not establish evidence truth or an answer oracle.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Decision roles: foreground caller proposes claim or asks for audit; model classifies; code parses exact textual fields/defaults. `validate_claim` says to call before pinning, but has no file-write interception or mandatory veto. Human contribution is upstream grants/problem/model configuration; no per-claim approval. Open-task diagnosis; improvement trigger is caller choice, not a threshold score. Persisted reasons require normal tool recording or an explicit write. Theory-builder conditions are not inferred from the requested criticism: actual localized theories, blame, resulting revision and next-round dependence require content/run evidence not supplied here.

Evidence: SRC-1, `src/opensage/toolbox/general/agent_tools.py`.

> for line in raw.splitlines():
>     line = line.strip()
>     if line.upper().startswith("CONFIDENCE:"):
> --- `src/opensage/toolbox/general/agent_tools.py`

#### MEM-RTE-hook-retention
Label: Hook context retention

Part of: [RT-RTE-host-extension](runtime.md#rt-rte-host-extension)

This is the retained-context callback part of the host-extension route. Endpoints: enabled hook matcher/action → prompt/command output queued → request user content and persisted user event, or PostToolUse result mutation → later model/history fold. Owner: upstream configuration supplier authors/selects hooks; bridge code matches event/tool and stores non-empty content. No per-output human approval.

- Immediate return: callbacks return `None`; request or result may be mutated and a new user event appended.
- Later read-back: persisted user-event text can reach future invocations through history/folding; static SessionStart prompt alone is not use-derived memory.
- Delegated visibility: configured base plugins are attached by manager; pending state per instantiated plugin and exact sharing require deployment evidence, not assumed per-agent isolation.
- Selection predicate: configured event/tool matcher; SessionStart prompt once per plugin's fired flag; accumulated PreToolUse text; non-empty executed PostToolUse content.
- Invalidation or expiry: queues clear after delivery/persistence; later compaction may replace history; disabling/editing hooks changes subsequent loading but does not erase already-retained events.
- Activation or effect: user-channel guidance delivery and retention are wired; semantic compliance is unobserved.
- Evidence limits: no deployed custom hook content; transient injection requires non-empty request contents; bridge lacks Claude permission-denial semantics; arbitrary command output provenance remains local and unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: configuration/load selects hook authority; code accepts non-empty output without truth evaluation. Recovery is config/content repair, not rollback of all retained messages. Open-task configuration mode; answer oracle: inapplicable. Command-output feedback is use-derived, but storing it is not automatically extracting warranted knowledge.

Evidence: SRC-1, `src/opensage/plugins/claude_code_hook_loader.py`; supplied [RT-RTE-host-extension](runtime.md#rt-rte-host-extension).

> if self._pending_pre_tool_persist:
>     parts_to_persist.extend(self._pending_pre_tool_persist)
>     self._pending_pre_tool_persist.clear()
> --- `src/opensage/plugins/claude_code_hook_loader.py`

#### MEM-RTE-image-retention
Label: Image retention and filtering

Endpoints/progression: tool-state image parts → enabled plugin pending lists → original-size user-history event → request-time historical-image filtering and pending-batch admission → later multimodal model. Owner: tools supply bytes; code controls display eligibility based on total request image count, dimensions and bytes. No supplied route counterpart; it augments rather than duplicates [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver).

- Immediate return: callback queues parts/clears tool-state key; later callbacks append events or rewrite request content.
- Later read-back: retained image event can reach subsequent requests, subject to re-derived filtering; rejection notices are not substitutes for image information.
- Delegated visibility: copied parent events may include image parts; plugin wiring and provider eligibility are still required.
- Selection predicate: request image count chooses 8000-pixel single-image or 2000-pixel batch per-side cap; raw bytes capped at 3.74 MiB; any oversized pending image rejects all pending images, while non-image parts remain.
- Invalidation or expiry: historical oversized parts are replaced by notices in request view; retained original-size event remains by the plugin's intended separation; later history compaction's text rendering does not preserve binary image detail.
- Activation or effect: history append/request filtering are wired when enabled; actual model visual use and correct parsing are unobserved.
- Evidence limits: malformed/unrecognized bytes are treated as non-image by size detection; stored-history immutability depends on external ADK request-copy behavior because code mutates `Content.parts`; provider internals and deployment plugin selection are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is code size gating, not semantic correctness review or human content approval. Rejection tells the model to resubmit smaller images; no automatic resize. Operating mode: open multimodal work; answer oracle: inapplicable. Original history append and request rejection are different controls; the latter must not be reported as image deletion from persistent storage without the dependency-copy fact.

Evidence: SRC-1, `src/opensage/plugins/default/adk_plugins/image_injection_plugin.py`.

> if violations:
>     return non_image_parts, violations
> return non_image_parts + image_parts, []
> --- `src/opensage/plugins/default/adk_plugins/image_injection_plugin.py`

#### MEM-RTE-explore-handoff
Label: Explore summary handoff

Endpoints/progression: optional SWE-bench explore phase → separate direct-runner history → final non-thought text or quota-exception summary → `task.first_user_message` → main agent. Owner: benchmark code selects phase and text; exploration/summarizer model supplies content. This is a distinct shipped direct-driver handoff not explicitly traced by [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver); it does not use the manager child-call route.

- Immediate return: summary string or `None`; non-fatal failures allow main task without exploration content.
- Later read-back: main agent receives prior exploration results in its next user prompt, retained through ordinary main-session events; cross-run durable exploration-store reuse is unestablished.
- Delegated visibility: separate explore service keeps full working history out of main frame; selected summary crosses back; frame is closed, not evidence that storage is erased.
- Selection predicate: `use_explore_agent`; final non-thought text; on max-call exception, last 50 rendered parts after truncating text to 2000, arguments to 500 and responses to 1000 characters; fixed `gemini-2.0-flash` summarization call.
- Invalidation or expiry: absent summary omits handoff; failed helper yields `None`; no versioned revision or confidence gate before user-prompt inclusion.
- Activation or effect: summary insertion before main execution is wired; usefulness, correctness and later reliance are unobserved.
- Evidence limits: docstring says memory search but observed code establishes prompt delivery, not `search_memory` store registration; direct explore session has only `opensage_session_id`, so normal file-memory directory initialization cannot be assumed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: code admits non-empty final/summary text; no human per-summary approval or independent answer oracle. Operating mode: bounded benchmark exploration followed by task repair. Guidance asks findings/files/structure/suggested approach; retained text may include reasons but quota fallback cannot preserve complete omitted traces. Helper model is an external mutable endpoint: model string is not immutable weight pin; ordinary call supplies no parameter update, provider internals uninspected. This is additional endpoint selection to [RT-CMP-base-llm](runtime.md#rt-cmp-base-llm), not another demonstrated learned component.

Evidence: SRC-1, `benchmarks/swe_bench_pro/swe_bench_pro.py`.

> task.first_user_message = self._build_user_message(
>     task.sample, explore_summary=explore_summary
> )
> --- `benchmarks/swe_bench_pro/swe_bench_pro.py`

#### MEM-RTE-findings-resume
Label: Vulnerability findings resume

Part of: [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver)

This retained-findings stage transition is part of the vulnerability direct-driver path. Endpoints: vulnerability result → schema parse → host JSON → later `resume_from_findings` parse → PoC prompt/run or stage skip. Owner: benchmark code selects file/stage; vulnerability model supplies findings, PoC model supplies attempted exploit. State effects: bypass detection when non-empty findings load, set current function, derive PoC artifacts.

- Immediate return: findings/PoC result processing; `skip_finished` returns an empty mock session when both output-file classes exist.
- Later read-back: loaded `VulFinding` values are serialized into a new PoC model's user request; output files also feed later benchmark evaluation.
- Delegated visibility: fresh per-agent in-memory sessions omit full vulnerability trajectory/reasoning; only structured finding content crosses to PoC stage.
- Selection predicate: first globbed vulnerability file under task output directory; `resume_from_findings`; non-empty loaded list skips detection, while empty list triggers detection; non-empty vulnerabilities select PoC generation unless `skip_poc`.
- Invalidation or expiry: replacing/removing findings changes next reload; schema errors can fail the task; no versioned rollback; file presence can suppress work without proving successful PoC.
- Activation or effect: code branch and next-model prompt depend on retained findings; exercised exploitation or improved detection is unobserved.
- Evidence limits: first-file choice is not ranked semantic retrieval; schema validation is not correctness validation; concrete later external PoC oracle/results are not executed or exhaustively assessed here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes JSON, Pydantic checks shape, code saves results including empty fallback on detection error. Human configures benchmark/resume but does not approve each finding. No reference oracle admits these files; PoC/evaluation is a downstream operation, not retroactive validation of every write. Guidance is vulnerability task/PoC prompt. Operating mode: bounded benchmark workflow; persisted findings/results and separate traces must not be conflated with retained model reasoning or trained capacity.

Evidence: SRC-1, `benchmarks/secodeplt/vul_detection_memory.py`.

> vul_findings = [
>     VulFinding.model_validate(vf) for vf in vul_findings_data
> ]
> --- `benchmarks/secodeplt/vul_detection_memory.py`

### Claims

#### MEM-CLM-pinning-survival
Label: Claimed pinning survival

Claimed operation: pinned content survives every compaction verbatim. Source: SRC-1 doctrine/design, `src/opensage/templates/auto_insert_prompts/default.md`. Distinct from policy delivery in [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy); this record bounds the specific durability assertion.

> `pinned.md` in your short-term memory dir survives history compaction
> verbatim — its content is embedded into every compaction summary, so it
> is never lost to LLM summarization.
> --- `src/opensage/templates/auto_insert_prompts/default.md`

Implementation supports best-effort independent pin embedding at successful automatic compaction, not an unconditional guarantee. Reads can fail/return empty; outer whitespace is stripped; final-compaction helper does not call the pin reader; previous embedded text can remain after emptying the live file until later folding changes it. Emptying is therefore prospective admission control, not an immediate purge of existing event history. Evidence: SRC-1, `src/opensage/features/summarization.py`, `src/opensage/patches/adk_llm_compaction.py`, [MEM-OBJ-pinned](#mem-obj-pinned).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-summary-authority
Label: Retained summary authority

Consumer: foreground/continuing model, plus consulting models reading folded history. Channel: model history content constructed from compaction/reduced tool events; wiki/findings enter only when read or broadcast. Force: interpreted informational/operational guidance, not invariant truth or enforced behavior. Horizon: later invocations in the live/reloaded session, dependent on checkpoints/resources.

Distinct from [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy): policy tells agents how to write; this path delivers retained results. Compaction prompt says user first-person and user-message resumption, but implementation builds `Content(role="model")` and patched replacement `Event(author="model")`. That mismatch prevents asserting user-principal authority solely from the summarizer prompt. Literal pinned strings are independent append content, not another warranted authority tier.

Evidence: SRC-1, `src/opensage/features/summarization.py`, `src/opensage/patches/adk_llm_compaction.py`.

> return types.Content(
>     role="model", parts=[types.Part.from_text(text=summary_text)]
> )
> --- `src/opensage/features/summarization.py`

## Annotations

#### On [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)

Memory result: [MEM-OBJ-compacted-content](#mem-obj-compacted-content) and independently embedded [MEM-OBJ-pinned](#mem-obj-pinned). Read-back trigger is subsequent history construction, not a foreground retrieval request. Automatic selector uses folded character count minus configured tool-response reserve, branch-compatible new candidates, configured older percentage and call/response-balanced prefix; recent tail remains. This is character accounting, not a hard provider-token bound. Summary length itself is not capped by that trigger. No physical event-list trimming occurs in the inspected core: append retains marker alongside original events, while patch substitutes only in derived view. Evidence: SRC-1, `src/opensage/features/summarization.py`, `src/opensage/patches/adk_llm_compaction.py`, `src/opensage/features/opensage_in_memory_session_service.py`.

Raw trace → rendered older-window/model summary → range marker plus pin read → patched folded view → later model/consultation. Reasons are requested but not checked; expanding start timestamp over earlier summaries while forbidding background re-summary risks non-cumulative read-back. New marker subsumption is implemented; complete semantic inheritance is not. Binary images do not pass the summarizer's text/tool renderer. The patch's exception comment says failed replacement is no-op, but range-skip code follows the exception and can still drop originals; the failure branch does not support a guaranteed lossless fallback. Evidence is implementation, not an observed loss.

> if comp and getattr(comp, "start_timestamp", None) is not None:
>     if comp.start_timestamp < start_ts:
>         start_ts = comp.start_timestamp
> --- `src/opensage/features/summarization.py`

> except Exception:
>     # If building summary event fails, do not consume window; fall back to no-op:
>     # treat as if this marker did not exist (i.e., do nothing special)
>     pass
> 
> # Skip original events within [S, E] (exclude marker events too)
> while i < n:
> --- `src/opensage/patches/adk_llm_compaction.py`

#### On [RT-RTE-directed-child](runtime.md#rt-rte-directed-child)

Working-context control is a separate frame with model-chosen inputs and optional parent-history inheritance. By default parent history/business state stay out; with inheritance selected/copied events enter. Parent receives extracted final text, optionally truncated with saved-file path at inbox delivery. The file pointer needs a later read; it is not a by-reference object in the context window. Continuing/reloading child can reuse retained child events; return does not pop/delete the stored frame. Supplied record establishes the progression and quoted copy/truncation witnesses. No additional source claim of mandatory isolation or complete returned trajectory.

#### On [RT-OBJ-agent-definition](runtime.md#rt-obj-agent-definition)

Retained selector lineage is dynamic builder fields, restored against current model/tool/skill registry. It is symbolic capability configuration, not serialized tool bodies or learned parameters. Saved selection can change effective capabilities on restart; unavailable tools can be dropped. Admission is code validation, not per-definition human endorsement. The supplied record and [RT-RTE-create-subagent](runtime.md#rt-rte-create-subagent) supply storage/rebuild witnesses.

#### On [RT-OBJ-agent-instruction](runtime.md#rt-obj-agent-instruction)

Retained natural-language instruction lineage is caller-supplied task method plus builder policy; actual caller authorship/control is not inferred from a string argument. Spawn/rebuild puts it into child model instruction, granting policy force across subsequent calls/restart rather than mere content storage. Criticism/reasons for the instruction are not separately required by the inspected builder. Supplied records retain the admission and downstream witness; no actual content-dependent improvement is observed.

#### On [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout)

Retention includes polled `live_events.jsonl`, serialized `session_trace.json`, metadata, cost/config files and explicitly selected sandbox export directories. `_collect_outputs` docstring names Neo4j export, but the inspected body copies configured sandbox paths and exports session/metadata, not a separate graph dump. This narrows the docstring, not the supplied runtime route. `session.events = all_events` makes collection use its polled event sequence; trace content can include already-reduced results. Evidence: SRC-1, `src/opensage/evaluation/base.py`.

> self._export_session_trace(session, output_path / "session_trace.json")
> --- `src/opensage/evaluation/base.py`

Normal task collection precedes cleanup; retained exported files are different from continuing sandbox access. External reward/trainer consumption is an integration contract supplied by the runtime, not an inspected raw-trace-to-trained-parameter update or production admission. Static configuration and raw logs alone do not establish trace-fed knowledge transformation.

## Write side

The write mechanisms have distinct admission controls:

| Mechanism | Proposer/content control versus physical writer | Admission, rejection and recovery | Retained result and later consumer |
|---|---|---|---|
| Layout/seed | Software seeds empty pins, generic TODO and index; code performs sandbox I/O | Test existence before seeding; exceptions logged; retry on later invocation | Paths/seed files; does not establish authored knowledge |
| Wiki/TODO/pin edit | Foreground model or another granted caller supplies text; shell/editor performs write | Filesystem permissions, not semantic approval; requested repair/removal; no versioned rollback | File content; requested later explicit reads, pin embed only at successful compaction ([MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance)) |
| Tool reduction | Code chooses eligible result; model writes summary or code takes prefix | Non-dictionary/short skip; no-model skip; exceptions use prefix; save failure loses fallback | Derived event plus optional original `.out`; later model or explicit shell reload ([MEM-RTE-output-reduction](#mem-rte-output-reduction)) |
| History compaction | Code chooses older balanced window; model writes summary; pin reader appends current file | Non-empty summary required; small/unbalanced windows skip; read failures do not block compaction | Range marker and derived content; later fold/model/consultation ([RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)) |
| Findings comparison | Caller supplies finding; model judges prior file/new finding; code writes | Duplicate substring veto; no-model/first-entry fallback; no automatic prior-claim retraction; lock scope is not full transaction | Finding plus criticism/completion text and peer message ([MEM-RTE-finding-admission](#mem-rte-finding-admission)) |
| Hook/image retention | Config/tool supplies content; bridge/plugin appends events | Non-empty hook selection; image request size rejection separate from original history retention | User-channel context or binary payload; later filtered/folded request ([MEM-RTE-hook-retention](#mem-rte-hook-retention), [MEM-RTE-image-retention](#mem-rte-image-retention)) |
| Checkpoints/definitions | Software serializes state; dynamic caller provides instruction/selectors | Structural load/sanitization and registry re-resolution; no truth review; config/load repair on failure | Raw/sanitized session, selectors and instructions; later resume/spawn ([MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume)) |
| Benchmark handoffs | Model supplies exploration or findings; code selects/parses/stores | Non-empty summary or schema parse; error/empty fallbacks; file-presence skip differs from evaluation | Summary to main agent; findings to later PoC model ([MEM-RTE-explore-handoff](#mem-rte-explore-handoff), [MEM-RTE-findings-resume](#mem-rte-findings-resume)) |

The automatic trace-fed transformation with an established later invocation is compaction/tool reduction and the explore quota fallback, not merely trajectory recording. Input lineage is mixed user/model/tool history. Reasons and failed attempts are requested by the summary prompts, but later range replacement/truncation can omit them. `log_finding` instead compares proposed natural-language findings against previous entries; it retains analysis but does not itself revise the old claim or prove learning. Trace consultation may help the foreground agent decide a revision, but the advisor's return is not automatic content admission.

Cleanup and withdrawal are scoped. Clearing pin/wiki files changes future reads; it does not erase copied events. Deleting or editing host checkpoints affects future reload, not already-live session objects. Session-service `evict`/delete removes in-process entries, not disk files; `update_event` can replace an event by ID, without establishing a content-curation policy. Sandbox cleanup can invalidate all file-memory access while host export/checkpoints remain. Evidence: SRC-1, `src/opensage/features/opensage_in_memory_session_service.py`, `src/opensage/session/opensage_session.py`; related records above bound actual later routes.

No successful knowledge-entry criticism, improved future capacity or exercised self-improvement is claimed. Requested correction and stored advice remain independently supported capacities; missing runs do not negate them. Actual theory content, its criticism and later dependence are unobserved and require epistemic/content evidence beyond these generic mechanisms.

## Read-back

Automatic push comprises compaction summaries, optional rewritten tool results, hook outputs and image eligibility filtering. The selectors, inputs and budgets are local to their routes; none is generic semantic retrieval. Pin reading is automatic only inside successful compaction and carries current stripped file content without size/truth validation. Wiki/TODO/full-output reading is agent-requested: path/index information supports a deliberate read but does not itself supply retained contents. `log_finding` additionally pushes admitted findings to peer inboxes in its ordinary non-duplicate branch, with restart and truncation limits from supplied dispatch/child records.

Recovery consumes symbolic IDs/paths to select session checkpoints and then supplies event content to future model calls. UI tree scanning derives an 80-character first-user query and last-event status from host trajectories; these are display summaries, not necessarily the full payload or an agent-consumed memory. CLI review uses trajectories for inspection, not an established subsequent model call merely because it displays them. Evidence: SRC-1, `src/opensage/memory/file_based/short_term/session_files.py`, `src/opensage/cli/opensage_cli.py`.

Benchmark read-back has concrete next consumers: main repair agent receives explore text; PoC agent receives reloaded finding JSON. These cases falsify a blanket claim that all memory is only an optional wiki. Conversely, an exposed final-summary function and constructed ADK memory service have no established later consumer route here. Supplied external training integration affords reward/trace consumers, but trainer updates/checkpoint adoption remain outside the source boundary.

The frame/heap analogy is limited: child/explore frames keep full work out and return selected text, but child frames can continue and persist, and shared files break mandatory isolation. A filename in a summary is by-value text; the model must invoke a tool to follow it. Compaction evicts originals only from the read view, not from the retained event container; this preserves explicit reload opportunities without guaranteeing automatic recovery of relevant omitted facts.

## Integration issues

- **Correction to any physical-trimming interpretation:** [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) correctly describes folded history, but the callback docstring says session events are already trimmed. Direct core/service/patch inspection shows append plus read-view substitution. [MEM-OBJ-traj](#mem-obj-traj) and [MEM-OBJ-compacted-content](#mem-obj-compacted-content) distinguish stored originals from model visibility. Do not infer reduced disk trace or physical deletion.
- **Non-cumulative summary risk:** new ranges subsume earlier ranges while prompt excludes background re-summary. Prior reasons/details may drop from delivered context even when preserved on disk ([MEM-OBJ-compacted-content](#mem-obj-compacted-content), [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)). No observed semantic loss is asserted; cumulative preservation is unsupported.
- **Pinning claim bounded:** best-effort reads, whitespace stripping, helper without pin read and old copied event content bound “every compaction/verbatim/unpin” ([MEM-CLM-pinning-survival](#mem-clm-pinning-survival), [MEM-OBJ-pinned](#mem-obj-pinned)). Emptying does not immediately purge existing markers.
- **Prompt/implementation role mismatch and failed-replacement branch:** summary prompt names user resumption, constructed content/event use model role; patch's failed-event exception still flows into original-window skip. These prevent strong user-principal or lossless-fallback claims ([MEM-BAP-summary-authority](#mem-bap-summary-authority), [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)). External ADK downstream details remain uninspected.
- **Additional direct driver:** SWE-bench explore handoff adds source-grounded coverage beyond the local/vulnerability examples of [RT-RTE-direct-driver](runtime.md#rt-rte-direct-driver). [MEM-RTE-explore-handoff](#mem-rte-explore-handoff) is distinct, while [MEM-RTE-findings-resume](#mem-rte-findings-resume) explicitly declares its containment in that supplied family. No unsupported `search_memory` retrieval is inferred from benchmark prompt labels.
- **Exposed advisory/admission operations:** [MEM-RTE-finding-admission](#mem-rte-finding-admission) and [MEM-RTE-history-consultation](#mem-rte-history-consultation) are afforded externally, not established as registered in a shipped agent by the bounded search. Their implemented comparison and retained criticism must not be lost simply because registration is unresolved. Full theory/iteration assessment requires content and reliance evidence; registered call coverage is the remaining local question.
- **Finding lock limitation:** file-read lock is released before model judgment and later append lock; concurrent proposals need not see one another. This bounds the source comment's serialization/dedup claim, not existence of locked append ([MEM-RTE-finding-admission](#mem-rte-finding-admission)).
- **Image stored/read-view separation:** plugin comments assert storage untouched; code mutates content objects, while session service exposes live sessions. Whether ADK copies request content is outside the frozen implementation. Keep retained-image capacity and rejection positive, but don't assert proven storage immutability ([MEM-RTE-image-retention](#mem-rte-image-retention)).
- **Export labels and opaque services:** evaluation docstring names graph export, inspected body does not implement that separate step. ADK memory construction and code graph query availability do not establish conversation-memory write/retrieval. Broader graph provenance, remaining benchmark consumers and trainer checkpoint decisions remain unresolved ([MEM-CMP-memory-service](#mem-cmp-memory-service), [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout)).
- **Identity/duplication:** no new object replaces a supplied referent. Checkpoint/hook/findings-resume routes declare their exact supplied parent. New retained-summary authority is downstream of, not duplicate with, supplied maintenance-policy authority. Trajectory, summaries and checkpoint metadata split memory-bearing parts previously mentioned only in routes. Dynamic definition/instruction and child/compaction/evaluation routes are annotated rather than redeclared. Reconciliation should retain these distinctions.

## Limitations and checks

Source identity and full HEAD were rechecked before source inspection. Supplied member identity fields and record IDs were preserved. The procedure was read completely in its specified batches, including recovery of bounded reads. All additional passages are from SRC-1 at the same frozen checkout; no new source, target execution, dependency install, delegation or publication occurred.

The report establishes implementation and declared affordances, not actual stored entries, plugin enablement, compliant agents, semantic fidelity, deployed restart, benchmark success or memory-caused learning. Opaque provider/dependency behavior, complete shipped caller enumeration and remaining benchmark/custom-extension semantics limit universal claims. The final-compaction helper and ADK service remain capability-only where no downstream consumer is established.

Validation: invocation-specific `commonplace-run validate-output` passed (member content check). Its result explicitly excludes invocation-residue checking and job acceptance/claim support. Deterministic validation concerns structure, citations and quote occurrence, not semantic correctness or acceptance.
