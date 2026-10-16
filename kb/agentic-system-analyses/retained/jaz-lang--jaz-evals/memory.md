---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "jaz-evals memory: ACE advice admission, history handoffs, opaque Letta state and retained diagnostic consumers."
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
source-identity: https://github.com/jaz-lang/jaz-evals
reviewed-boundary: "2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72"
---

# jaz-evals memory report

## Boundary and evidence

This report covers retained guidance, history transfer and working-context control in jaz-evals at the boundary's frozen commit. It includes ACE's explicit trace-to-playbook loop; the JAZ improvement and long-horizon history instructions; fresh task frames and the CodeAct filter; smolagents' history wrapper and handoff cue; Letta's configured memory, message delivery and summarizer instrumentation; and post-run diagnostic read-back. It does not treat benchmark world state as a knowledge store or infer external-runtime internals from adapter names. The external JAZ, Letta, smolagents and benchmark implementations remain outside the supplied evidence, as established in [boundary](boundary.md#boundary-and-evidence).

Direct source inspection adds SRC-1 implementation reads of `src/jaz_evals/harnesses/ace.py` (task/adaptation loop, rendering, seed/snapshot and dedup paths), `src/jaz_evals/harnesses/ace_playbook.py` (count stripping, ADD application and validation), `src/jaz_evals/harnesses/ace_dedup.py` (complete file), Letta creation/delivery/cleanup ranges in `src/jaz_evals/harnesses/letta_harness.py`, the complete `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py`, attempt discovery/reporting in `src/jaz_evals/analyze_cli.py`, and trace-layout selection in `src/jaz_evals/analysis.py`. Direct doctrine/design reads cover both TTSI prompts, all four long-horizon prompts, and the relevant JAZ/smolagents configuration cues. Bounded symbol searches checked entry points, history hooks, Letta search/compaction seams and diagnostic consumers. Runtime findings below are supplied evidence, not represented as new direct full-file inspection.

| Entry point / operation | Source paths, SRC-1 | Coverage and limit |
| --- | --- | --- |
| Central attempt persistence and CLI dispatch | `pyproject.toml`, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/analyze_cli.py` | Supplied [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt); entry-point search and direct diagnostic dispatch read; [MEM-RTE-artifact-analysis](#mem-rte-artifact-analysis). Not a solver resume path. |
| ACE seed, per-task update and next-solver supply | `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py` | Direct reads; [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) annotated below; [MEM-OBJ-playbook](#mem-obj-playbook), [MEM-OBJ-playbook-counts](#mem-obj-playbook-counts), [MEM-OBJ-adaptation-artifacts](#mem-obj-adaptation-artifacts). Seed authorship remains unknown. |
| ACE optional refinement and public helper alternative | `src/jaz_evals/harnesses/ace_dedup.py`, `src/jaz_evals/harnesses/ace.py` | Direct reads; [MEM-RTE-playbook-dedup](#mem-rte-playbook-dedup), including merge-free library operation, not merely the model-merge harness path. |
| JAZ TTSI prompt/helper editing | `prompts/ttsi/jaz.md`, `prompts/ttsi/jaz_codeact_subagents.md`, `src/jaz_evals/harnesses/jaz_harness.py` | Direct prompt reads plus supplied [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue). Adapter affords changes; model-authored artifacts and actual reuse unavailable. |
| JAZ long-horizon recall and delegation | `configs/stulife_jaz.yaml`, `prompts/long_horizon/jaz.md`, `prompts/long_horizon/jaz_codeact_subagents.md` | Direct doctrine/design; [MEM-RTE-jaz-history](#mem-rte-jaz-history). External hook and history representation implementation unavailable. |
| Per-task frame discard / CodeAct exclusion | `src/jaz_evals/harnesses/jaz_per_task.py`, `src/jaz_evals/hooks.py` | Supplied [RT-RTE-fresh-session](runtime.md#rt-rte-fresh-session), [RT-RTE-codeact-filter](runtime.md#rt-rte-codeact-filter), plus scoped history-hook search. No new retained artifact inferred from eviction. |
| smolagents continuation / wrapped history | `configs/stulife_smolagents.yaml`, `prompts/long_horizon/smolagents.md`, `src/jaz_evals/harnesses/smolagents_harness.py` | Direct configuration/prompt and source-symbol reads plus supplied [RT-RTE-smolagents-chain](runtime.md#rt-rte-smolagents-chain); [MEM-RTE-smolagents-history](#mem-rte-smolagents-history). Wrapper construction and full-history fidelity depend on model compliance. |
| Letta core blocks, conversation and archived/summary state | `src/jaz_evals/harnesses/letta_harness.py`, `prompts/long_horizon/letta.md`, `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py` | Direct adapter/patch/prompt reads; [MEM-OBJ-memory-blocks](#mem-obj-memory-blocks), [MEM-OBJ-conversation](#mem-obj-conversation), [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-OBJ-archival-memory](#mem-obj-archival-memory). Server storage, exact search selection, update authorization and summary insertion remain opaque. |
| Method-specific log views, plots/releases and native AppWorld resume | `src/jaz_evals/harnesses/letta_log_viewer.py`, `src/jaz_evals/harnesses/smolagents_log_viewer.py`, `scripts/`, `scripts/run_appworld_official_react.sh` | Viewer entry points checked; implementations and plot/release helpers not audited. Supplied [RT-RTE-official-baseline](runtime.md#rt-rte-official-baseline) records requested external skip-if-finished. Prevents exhaustive archival-transformation or native-resume conclusions. |

No target code, provider, container, tests or examples were executed. There is no observed-run or causal-experiment layer. Implementation delivery is distinguishable from model reliance and benefit throughout.

## Core ideas

1. **ACE carries advice rather than a solver frame.** A fresh solver receives the current count-stripped playbook. Its task trajectory and completion report feed separate reflector and curator calls; admitted advice then reaches later sessions. Stored counters and diagnostic sidecars are not equivalent to the advice that a solver sees. See [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation) and [MEM-OBJ-playbook](#mem-obj-playbook).
2. **Refinement is similarity-driven rewriting, not correctness-based forgetting.** Embeddings group advice, and a merge model may replace several bullets. Cross-section grouping and overlapping groups mean neither section preservation nor strict removal of redundancy is guaranteed by the algorithm. A syntactically parseable merge is not a semantic validation. See [MEM-RTE-playbook-dedup](#mem-rte-playbook-dedup).
3. **A bounded display is not bounded retained content.** The smolagents cue asks for a wrapper whose representation shows a suffix while `unwrap()` retains the full list. A progress summary is a separate authored interpretation, not the full history. JAZ similarly asks successors to search passed history instead of resending it all to the model. These are afforded, model-mediated routes, not proof of actual lossless handoffs. See [MEM-RTE-jaz-history](#mem-rte-jaz-history) and [MEM-RTE-smolagents-history](#mem-rte-smolagents-history).
4. **Letta's adapter exposes memory-relevant inputs without exposing the whole memory engine.** Task messages, core blocks and a returned compaction string are inspectable seams. Archive retrieval and exact summary replacement remain dependency responsibilities. The instrumentation ledger counts calls; it does not preserve a readable replacement history. See the Letta objects below.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-playbook
Label: ACE playbook advice

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

This object is the route's retained guidance state, not a duplicate route. Source-native identity: `playbook`, held as a Python string and written to `ace/playbook_after_task_<index>.txt` and `ace/playbook_final.txt`. Its advice is natural-language content interpreted by solver, reflector and curator; section/bullet syntax is symbolic structure used by local transformations. Lineage: configured seed file or empty sections, curator ADDs derived from task traces/reflection, then optional merges. Initial seed authorship and human approval are not specified by a path. Subsequent admission is computational, not a per-update human decision (SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`).

Consumer authority is advisory, not environment-rule authority, as made explicit in the actual solver template. The next invocation receives all current advice after count removal; it is not a task-keyed retrieval. The live string, rather than a just-written snapshot being reloaded, carries the within-run update. Snapshots afford later explicit `initial_playbook` loading, not automatic recovery. Related supplied authority record: [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance).

> You have a playbook of accumulated guidance from earlier tasks. It is advisory, not authoritative: \
> follow it where it applies, and ignore any bullet that does not fit the task in front of you.
> --- `src/jaz_evals/harnesses/ace.py`

> if seed.is_file():
>     return seed.read_text()
> --- `src/jaz_evals/harnesses/ace.py`

#### MEM-OBJ-playbook-counts
Label: ACE stored helpful and harmful counters

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Distinct state part from [MEM-OBJ-playbook](#mem-obj-playbook): symbolic per-bullet ID/count fields in the same stored string/files. New ADDs initialize helpful/harmful to zero; `strip_counts` removes the counts from solver, reflector and curator copies. These are not outcome-derived reliability estimates or an advice access-frequency policy. Model merges can output numeric counts and the parser accepts them; neither their presence nor their names proves measured helpfulness. Section headers and IDs remain visible after stripping. SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`, `src/jaz_evals/harnesses/ace_dedup.py`.

> out.append(f"{match.group(1)} {match.group(2)}" if match else line)
> --- `src/jaz_evals/harnesses/ace_playbook.py`

> pending.append((section, format_bullet(bullet_id, 0, 0, str(op.get("content", "")))))
> --- `src/jaz_evals/harnesses/ace_playbook.py`

#### MEM-OBJ-adaptation-artifacts
Label: ACE trajectories and adaptation call records

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

Source-native identities: per-session `agent.atif.json`, adaptation call markdown sidecars, `calls.jsonl`, `curator_failures.jsonl`, `dedup.jsonl` and adaptation exception records. Storage: attempt-local files. Raw trajectories/call bodies contain mixed natural-language and symbolic code/tool material; diagnostic indices, costs and failure counters have symbolic consumers. They are evidence and accounting artifacts, not themselves the admitted playbook. The trajectory is supplied to adaptation after a 400,000-character head cap; the original trace file is not thereby truncated. Task prefixes are 2,000 characters for reflector and 1,000 for curator. The full reflection reaches the curator, but curator reasoning is not installed as a separate reason field attached to each advice bullet. Sidecars preserve prompts/responses for an operator; the inspected solver/adaptation route does not reload historical sidecars to reconstruct rationale. SRC-1, `src/jaz_evals/harnesses/ace.py`.

> return text[:_MAX_TRAJECTORY_CHARS] + "\n... (trajectory truncated)"
> --- `src/jaz_evals/harnesses/ace.py`

> """Write one adapter call's prompt and response as markdown, and return the path."""
> --- `src/jaz_evals/harnesses/ace.py`

#### MEM-OBJ-memory-blocks
Label: Letta human and persona core-memory blocks

Part of: [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge)

Source-native identity: `memory_blocks` supplied to `client.agents.create`. Natural-language human/persona text is serialized in symbolic label/value mappings, stored in external server agent state with its exact substrate and later editing rules uninspected. The adapter supplies configured values; their original author and per-content approval are unresolved. Creation installs them in the agent configuration; the unavailable runtime determines how they enter model context and whether base tools can edit them. Distinct from conversation and archival state; not a duplicate of [RT-CMP-letta-model](runtime.md#rt-cmp-letta-model), which denotes the model, not these contents. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`.

> memory_blocks=[
>     {"label": "human", "value": self.human},
>     {"label": "persona", "value": self.persona},
> ],
> --- `src/jaz_evals/harnesses/letta_harness.py`

#### MEM-OBJ-conversation
Label: Letta conversation and searchable task messages

Part of: [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge)

Source-native identity: user messages passed to `client.agents.messages.create`, remote conversation records, and their host-side `letta_messages.jsonl` export. Storage: external server history during the attempt and JSONL diagnostics on the host; exact server schema/index unavailable. Representational form: mixed natural-language task/tool/message bodies and symbolic roles/IDs; optional dense search representations belong to the external retrieval machinery. The configured delivery path requests task text from the environment, sends new text verbatim as a user message, and substitutes a nudge for unchanged text or a delivery exception. This is an implemented selection affecting what becomes searchable; it does not independently establish server search completeness. The long-horizon prompt requests targeted `conversation_search` calls for no-longer-visible messages. Search ranking, result budget, tool-message exclusions and exact retained coverage are not independently verified here. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`, `prompts/long_horizon/letta.md`.

> if text == last_delivered:
>     return _CONTINUE_CURRENT, last_delivered
> --- `src/jaz_evals/harnesses/letta_harness.py`

> To recall information from earlier in the
> session, *search for this information with `conversation_search`*.
> --- `prompts/long_horizon/letta.md`

Task text and tool responses are observations/input material, not newly approved system guidance. Search output would be interpreted by the agent; its delivery does not authenticate its contents. The local export is not wired back into a recreated remote agent. Cleanup drains diagnostics before container teardown, destroying ephemeral server state; durable exported traces are distinct from live recoverable memory.

#### MEM-OBJ-compaction-summary
Label: Letta summarizer return text

Part of: [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge)

Distinct derived object from [MEM-OBJ-conversation](#mem-obj-conversation): natural-language summary text returned by the patched `_execute_summarizer_request`; local storage is transient Python return data and subsequent persistence is external. The non-streaming branch requests a completion and returns stripped content, rejecting `None`; the streaming branch delegates to the original function. The patch writes usage/model metadata, not the summary body, to `compaction_stats/usage.jsonl`. Exact source-message selection, summarizer trigger/budget, what verbatim tail survives, replacement checkpoint format, later injection and summary editing/withdrawal remain uninspected in Letta. Consequently this is an inspected production seam, not a fully established raw-to-summary-to-later-consumer route. Source reasoning retained inside the summary is unknown. SRC-1, `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py`.

> if response.choices[0].message.content is None:
>     raise Exception("Summary failed to generate")
> return response.choices[0].message.content.strip()
> --- `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py`

#### MEM-OBJ-archival-memory
Label: Letta archival-memory and search index seam

Part of: [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge)

Source-native identity: archival memory and message-search embedding operations mentioned by the adapter, with optional `turbopuffer_region` and base tools enabled for `letta_v1_agent`. This is a distinct opaque state part, not the agent's core blocks or the compaction string. Raw archive payload form, lineage, retention, author/admission principal and access checks remain unresolved in the external server. The adapter describes dense embeddings used for archival writes/queries and optionally messages; it does not implement archive admission, retrieval, semantic curation or deletion. Those reported seams must not be promoted to inspected model-memory routes. Host ledgers record embedding spend, not enough content to reconstruct the archive. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`.

> Letta embeds archival-memory writes/queries (and every message, under Turbopuffer) and discards the
> --- `src/jaz_evals/harnesses/letta_harness.py`

### Routes

#### MEM-RTE-playbook-dedup
Label: ACE similarity-selected bullet replacement

Part of: [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

This is the optional refinement subroute, not a duplicate of the entire task/adaptation cycle. Trigger: accepted ADD application when dedup is enabled. Owner: Python grouping/rebuild; encoder supplies vectors and model supplies a merged bullet. Endpoints: current playbook → parse bullet blocks → embed contents/normalize → greedy similarity groups → merge/parse → replacement and absorbed-range removal → returned playbook. Vector state is derived for selection, not a persistent vector store. The encoder is already declared in [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer). SRC-1, `src/jaz_evals/harnesses/ace_dedup.py`, `src/jaz_evals/harnesses/ace.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `DedupResult` with rewritten playbook and before/after/failure counts; harness writes diagnostic JSONL and returns the text to adaptation.
- Later read-back: replacement advice enters the next solver and adaptation prompts through the live playbook and is included in snapshots; no similarity retrieval occurs at solver-read time.
- Delegated visibility: merge model sees selected bullet texts, IDs and summed counts; solver sees resulting advice without counts, not embeddings or dedup diagnostics.
- Selection predicate: code compares all parsed bullet contents using normalized embedding similarity and configured threshold; greedy groups can span sections and overlap in absorbed members.
- Invalidation or expiry: successfully merged groups replace the first block and remove other whole blocks; unparseable merge leaves the group intact. With dedup disabled the harness skips this path. Whole adaptation exceptions preserve the prior live playbook.
- Activation or effect: deterministic rewrite reaches later prompt construction; semantic preservation, reduced redundancy and changed solver behavior remain unobserved.
- Evidence limits: encoder/model implementation and generated merge texts are unavailable; similarity is not task correctness or semantic equivalence.

Admission: model proposes merged wording; regex parsing admits it and code applies it without a human per-content gate or semantic-success test. The prompt requests concise preservation of all important information, but parseability cannot enforce that. Library `deduplicate(..., merge=None)` is a materially different exposed operation: retain the first bullet and absorb the rest without model synthesis. The shipped harness instead supplies a merge closure. Rejection/recovery is structural; neither branch is an outcome-based withdrawal of harmful advice. Operating mode is the parent route's bounded curriculum; no answer oracle participates in this subroute. The parent record supplies independent theory and self-improvement assessments; this subroute establishes rewriting, not generated criticism or successful learning.

> if merge is None:
>     # `merge=None` is the paper's merge-free variant: dropping the rest of the group IS the
>     # policy there, so absorbing without a model call is correct.
>     replacement[group[0]] = members[0]
> --- `src/jaz_evals/harnesses/ace_dedup.py`

The counterexample to a strong redundancy-removal claim is in the executable grouping rule: previously visited later members are not filtered. A bullet may influence two replacements. This is source-grounded possibility, not an observed run finding.

> similar = [j for j in range(i + 1, len(embeddings)) if similarity(i, j) >= threshold]
> --- `src/jaz_evals/harnesses/ace_dedup.py`

#### MEM-RTE-jaz-history
Label: JAZ history handoff and targeted read-back

Part of: [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)

Distinct subroute from TTSI advice editing: configured long-horizon warning asks a successor to receive the predecessor history plus current `__history__`, state, progress summary and next steps. The successor's prompt asks it to search concrete terms in `prev_history` and display context around hits. This retains task experience as searchable content, rather than necessarily distilling general advice. Ownership is model-directed delegation/search under configured guidance; actual history runtime and display limits are external. SRC-1, `configs/stulife_jaz.yaml`, `prompts/long_horizon/jaz.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: requested child result returns to predecessor; the configured template returns that invocation result.
- Later read-back: successor receives the accumulated history object and can print selected output windows into a later model turn.
- Delegated visibility: selected input variables, history and state are passed explicitly; natural-language progress summary is separate from the raw history payload. Automatic inherited history is not established.
- Selection predicate: warning configured at 0.7 window fraction requests delegation; foreground model chooses search terms and code selects matching output plus a 1,000-character preceding and 2,000-character following window.
- Invalidation or expiry: new invocation separates working context; retained history remains reachable only if actually forwarded. Cross-attempt persistence/reload is unestablished.
- Activation or effect: prompt supplies a concrete search/handoff procedure; model compliance and whether retrieved facts affect actions are unobserved.
- Evidence limits: JAZ history object serialization, warning dispatch, exact display budget and actual handoffs are outside this source implementation.

> prev_history=globals().get("prev_history", []) + __history__,
> --- `configs/stulife_jaz.yaml`

> start = max(0, pos - 1000)
> end = min(len(repl_output), pos + 2000)
> --- `prompts/long_horizon/jaz.md`

The CodeAct long-horizon prompt instead requests a model-maintained `output_history` list. That is authored trace collection, not proof of complete native history capture (SRC-1, `prompts/long_horizon/jaz_codeact_subagents.md`; see [RT-RTE-codeact-filter](runtime.md#rt-rte-codeact-filter)).

#### MEM-RTE-smolagents-history
Label: smolagents wrapped history handoff

Part of: [RT-RTE-smolagents-chain](runtime.md#rt-rte-smolagents-chain)

Memory-specific subroute: warning guidance asks the model to concatenate predecessor history with its self-recorded output list, wrap the result, and supply it through child `additional_args`; instructions/guidance and a progress summary are copied into task text. This is distinct from the chain topology/return-guard route, and from JAZ's native history. Natural-language trace contents and derived progress summaries are interpreted by successor models; wrapper methods and search code are symbolic. Storage is model-created executor objects, with exact external executor transport behavior uninspected. SRC-1, `configs/stulife_smolagents.yaml`, `prompts/long_horizon/smolagents.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: child answer passes back through the requested `final_answer(subagent_...)` chain.
- Later read-back: child can call `prev_history_wrapped.unwrap()`, search the retained list, and print matching context windows for later model consumption.
- Delegated visibility: configured wrapper displays only a suffix; its stored `_obj` and unwrap result retain the full list if built as instructed. Summary/next-step strings are visible separately and are not substitutes for that payload.
- Selection predicate: wired callback cues handoff at configured input-token fraction when a child exists; model decides to execute it. `handoff_history_max_chars` is 50,000 in the inspected configuration; it controls the requested display suffix, not list truncation. Later recall is model-requested substring search.
- Invalidation or expiry: fresh child context keeps prior turns out of its initial window except passed representations; full retained list remains reachable through the wrapper. Reset and object transport semantics remain dependency responsibilities.
- Activation or effect: code appends a cue, not a forced eviction, summary or delegation; actual recording fidelity, complete forwarding and behavioral reliance are unobserved.
- Evidence limits: ordinary printed outputs absent from the model-maintained list cannot be recovered by its search. A faithful wrapper is prescribed, not installed automatically by the adapter.

> def unwrap(self):
>     return self._obj
> --- `configs/stulife_smolagents.yaml`

> def __repr__(self):
>     return str(self._obj)[-{max_chars}:]
> --- `configs/stulife_smolagents.yaml`

#### MEM-RTE-artifact-analysis
Label: Retained traces to operator diagnostics

Distinct downstream read-back from [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt), not an agent-guidance reload. Trigger: caller invokes `jaz-evals-analyze` on file, attempt or run directory. Owner: deterministic CLI/parser code. Endpoints: discover retained attempt markers → select available trace layout and method-specific analysis → compute reports → print diagnostics for an operator. SRC-1, `src/jaz_evals/analyze_cli.py`, `src/jaz_evals/analysis.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted diagnostics and success/failure return code.
- Later read-back: previously retained task results and trajectories feed a new analysis invocation; no inspected route automatically feeds those printed reports into the solver.
- Delegated visibility: inapplicable — this is post-run host analysis, not agent delegation.
- Selection predicate: explicit path and discovered markers select attempts. Attempt-level ATIF takes precedence over numerically ordered session traces; analysis falls back to smolagents trace or log when applicable. Unknown tool names suppress the reports requiring them rather than guessing.
- Invalidation or expiry: files remain until external deletion/change; regenerated diagnostics depend on available artifacts. No general retention TTL is implemented in these inspected selection functions.
- Activation or effect: diagnostic computation/printing is wired; operator decisions, regenerated published results and feedback into subsequent agent configuration are unobserved.
- Evidence limits: this is not a full audit of viewer, release or plotting consumers. Missing traces prevent their corresponding reconstructions; complete archived runs were not supplied.

> root = attempt_dir / "agent.atif.json"
> if root.is_file():
>     return [root]
> return sorted(attempt_dir.glob("session_*/agent.atif.json"), key=lambda p: _session_index(p))
> --- `src/jaz_evals/analysis.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation)

The raw-to-derived chain is explicit: session ATIF plus environment-returned feedback and exception text → reflection → curator JSON → admitted ADD content → optional rewritten advice → later solver/adaptation prompts. Task and trajectory prefixes limit the evidence that can shape advice. A source-supported counterexample to a "whole run retained as lessons" reading is the head cap; a counterexample to "all curator reasoning becomes reusable advice" is that `apply_add_operations` stores content, not the top-level reasoning. The stored call bodies can preserve reasons for human audit, but the later solver gets only rendered playbook advice and ordinary instructions. Individual bullets may themselves include reasons; no generated artifact permits assessing that here. SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`; see [MEM-OBJ-adaptation-artifacts](#mem-obj-adaptation-artifacts).

Unknown sections are dropped individually; malformed reply structure rejects the update. Empty or questionable advice content is not independently tested for truth by the validator: content is later converted with `str(...)`. Seed-file loading is a separate file-read admission seam, not the curator validator. Thus initialized content trust remains unresolved without concealing the known subsequent computational transformations. The next task receives the resulting live string automatically, not on a task-targeted query. SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`.

> if "reasoning" not in payload:
>     raise ValueError("curator reply is missing the 'reasoning' field")
> --- `src/jaz_evals/harnesses/ace_playbook.py`

#### On [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)

TTSI distinguishes returned raw histories from derived reusable prompts/helpers. Native TTSI asks for `__history__`; the CodeAct variant asks a model to return a list of code/output/exception entries instead. Neither prompt is evidence that those lists were complete. Both ask the root to diagnose failure mechanisms and remove ineffective helpers. Actual admissions are model-mediated invocation inputs rather than a separately enforced content gate. The retained rationale's form, checkpointing and later reader depend on what the root authors; the adapter alone does not supply a durable per-edit rationale store. SRC-1, `prompts/ttsi/jaz.md`, `prompts/ttsi/jaz_codeact_subagents.md`; the supplied route and [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment) retain the operative passages.

#### On [RT-RTE-fresh-session](runtime.md#rt-rte-fresh-session)

Fresh per-task frames keep prior task reasoning out, while the answer crosses to the driver and the environment may preserve world state. This is working-context isolation, not trace-fed instruction learning. ACE uses the same broad frame pattern but explicitly carries updated advice, so fresh context does not entail absence of all cross-task memory. Evidence: supplied route and [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), SRC-1, `src/jaz_evals/harnesses/jaz_per_task.py`, `src/jaz_evals/harnesses/ace.py`.

#### On [RT-RTE-codeact-filter](runtime.md#rt-rte-codeact-filter)

The hook excludes native history and string bindings plus corresponding naming guidance; it does not erase ordinary textual instructions. A model-maintained output list is a separate possible acquisition path after native history removal. Thus exclusion of one binding is not an absence claim about task experience or all recall. Supplied route provides implementation evidence and its checked passage; SRC-1, `src/jaz_evals/hooks.py`, `prompts/long_horizon/jaz_codeact_subagents.md`.

#### On [RT-RTE-letta-bridge](runtime.md#rt-rte-letta-bridge)

Memory read-back is bounded by its external runtime, not established by the bridge's host tool forwarding. The adapter directly wires core-block initialization and user-message production; long-horizon guidance affords targeted conversation search; archive/summary retention and result selection remain opaque. The supplied route's broad memory statement should be read at these separate evidence layers. Task delivery is important because it changes the retained message channel before any retrieval. Cleanup drains exported diagnostics before destroying the ephemeral server DB; durable host files do not prove cross-run agent-memory recovery. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`; [MEM-OBJ-conversation](#mem-obj-conversation), [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-OBJ-archival-memory](#mem-obj-archival-memory).

> # container's DB is ephemeral, so whatever is not drained here is destroyed with it.
> --- `src/jaz_evals/harnesses/letta_harness.py`

## Write side

**ACE admission has several gates, not a quality oracle.** Initial content comes from an arbitrary configured file or generated empty sections. Original author/approval is unknown. Reflector and curator are computational authors; parser/section whitelist and code application admit their updates. Unknown sections lose the individual operation; invalid JSON or schema preserves prior advice. Ordinary adaptation exceptions also keep the prior caller state, including when an ADD followed by dedup fails before the tuple returns. Freeze stops later update attempts but does not retract existing advice. See [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation), [MEM-OBJ-playbook](#mem-obj-playbook), [MEM-RTE-playbook-dedup](#mem-rte-playbook-dedup); SRC-1, `src/jaz_evals/harnesses/ace.py`.

**ACE withdrawal is narrower than the label "curation" suggests.** Ordinary operations admit ADD only. Deletion/replacement happens through similarity-group refinement, not a harmfulness score, content contradiction test or explicit curator DELETE. The model-merge path preserves a group on parse failure; the public merge-free helper deliberately removes all but its first member. Merging can cross section boundaries and need not preserve each original bullet's wording/reasons. No per-content human veto is wired in those functions. Starting the evaluation is a different decision. See [MEM-OBJ-playbook-counts](#mem-obj-playbook-counts), [MEM-RTE-playbook-dedup](#mem-rte-playbook-dedup); SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`, `src/jaz_evals/harnesses/ace_dedup.py`.

**JAZ/smolagents collect and forward experience by request.** Native histories, manually recorded output lists, progress summaries and optimized guidance are distinct products with different fidelity. The prompts ask models to author/forward them; warning callbacks do not mechanically admit a complete history or verify a proposed helper's reliability. TTSI asks rejection of ineffective edits but actual edits and rejection decisions were not supplied. The write agency is model/code at subsequent seams; no human per-change approval is established. See the JAZ annotation and the two history routes.

**Letta writes remain partly opaque.** The adapter creates core blocks and sends selected environment text. It enables base tools but does not expose their memory edit/archive authorization logic. The compaction patch produces a summary string and writes usage metadata; it does not establish the summary's later installation or preserve its full source-to-output lineage in that ledger. Cleanup destroys server state after best-effort diagnostics extraction, not after serializing a known restorable memory checkpoint. See the four Letta objects. No missing-internals claim is used to negate the inspected writes.

## Read-back

- **ACE push:** task completion triggers adaptation; the code supplies all resulting advice, count-stripped, in every later solver prompt and adaptation prompt. Its inspected read operation has no task-similarity selection or fixed advice-length cap. The 400,000-character cap applies to diagnostic input, not solver advice. Snapshots enable explicit file seeding on another run; they are not automatically reloaded mid-run. Authority is advisory natural language under [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance).
- **JAZ/smolagents requested recall:** a warning requests a new context; explicit input transfer keeps histories outside most of the initial visible window and makes them reachable by model-written search. New model turns receive printed hit windows. Display suffix limits and progress summaries are not evidence that the full payload was truncated. Frame isolation resembles a stack call, but the analogy breaks because histories can be explicitly passed as external objects and their displayed text is copied into a new window, not automatically dereferenced there. See [MEM-RTE-jaz-history](#mem-rte-jaz-history), [MEM-RTE-smolagents-history](#mem-rte-smolagents-history).
- **Letta recall:** long-horizon guidance requests one concrete search target per query and later action after results, not independent unsolicited memory supply. Exact query ranking, archive use, summary-tail composition and returned budgets remain external. A callable storage/search API alone is not treated as proof of actual model consumption. See [MEM-OBJ-conversation](#mem-obj-conversation), [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-OBJ-archival-memory](#mem-obj-archival-memory).
- **Operator read-back:** retained traces/results feed shipped analysis through explicit path selection and method-aware parsers. This changes diagnostic visibility, not automatically solver guidance. See [MEM-RTE-artifact-analysis](#mem-rte-artifact-analysis). Native AppWorld's requested skip-if-finished remains external resume behavior, not a jaz-evals memory guarantee ([RT-RTE-official-baseline](runtime.md#rt-rte-official-baseline)).

## Integration issues

1. No supplied fact requires correction. The statement about counters is a precision addition: stored helpful/harmful names must not be interpreted as measured update authority. Evidence and affected states: [MEM-OBJ-playbook-counts](#mem-obj-playbook-counts), [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation); SRC-1, `src/jaz_evals/harnesses/ace_playbook.py`.
2. The new records are parts or downstream consumers, not replacement declarations. Dedup and history subroutes refine the supplied combined routes via explicit Part of fields; ACE/Letta objects identify retained state within their parent routes. [MEM-RTE-artifact-analysis](#mem-rte-artifact-analysis) overlaps the later-read-back field of [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt), but denotes the later analysis invocation, not the producer attempt. No possible whole-record duplicate remains after this comparison.
3. Initial seed/control remains unresolved for [MEM-OBJ-playbook](#mem-obj-playbook) and [MEM-OBJ-memory-blocks](#mem-obj-memory-blocks): configuration and physical reads establish supply, not the original human author/approver. This prevents generalizing computational subsequent admission into a human-control claim about initialization.
4. Opaque Letta alternatives remain: exact core-block context/edit policy, searchable message eligibility/ranking/budget, archived payload and write controls, summary trigger/selection/persistence and later injection. The adapter and patch provide real seams but not those missing facts. This prevents classifying the full read-back/curation mechanism from this repository alone; see all four Letta objects and their source anchors.
5. Model compliance and actual retained artifacts remain unresolved for [MEM-RTE-jaz-history](#mem-rte-jaz-history), [MEM-RTE-smolagents-history](#mem-rte-smolagents-history), [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue). Prescribed full-history transfer and TTSI validation are not observed operations. Actual reason preservation, learned benefit and exercised self-improvement cannot be inferred.
6. Viewer, plot/release and native-resume internals are not audited here. Their unresolved scope is named in the coverage table; [MEM-RTE-artifact-analysis](#mem-rte-artifact-analysis) supports a real downstream consumer but not exhaustive post-run transformation or reproducibility. The external source gaps remain those of [boundary](boundary.md#boundary-and-evidence).

## Limitations and checks

The checkout HEAD was rechecked as `2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72` and its working tree was clean. Source identity and run identity match the supplied boundary/invocation. Method identity is the supplied memory member type, job instruction, worker rules and shared records contract; no external authoring procedure or prior characterization was used. Only assigned outputs and identity were written.

The counterchecks were concrete: dedup's overlapping grouping rule limits redundancy claims; the merge-free API differs from the shipped merge closure; count stripping limits reliability-metadata interpretations; curator reasoning does not automatically survive as advice rationale; and diagnostic export does not establish restorable Letta state. These limits coexist with positive implemented advice delivery and diagnostic consumers. No source execution establishes activation, improvement or historical score reconstruction.

Validation: `commonplace-run validate-output` reported: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The deterministic content pass does not establish semantic acceptance, observed operation or an invocation-residue check.
