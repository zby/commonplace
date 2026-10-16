---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Voyager memory: executable skills, description indexes, QA cache, chest and progress retention, event replay and bounded action frames."
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
source-identity: https://github.com/MineDojo/Voyager
reviewed-boundary: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
---

# Voyager memory report

## Boundary and evidence

This member covers retained skills and their two consumers, QA, chest observations, task histories, event checkpoints, recent block records and working-context replacement in Voyager's learning and inference drivers. SRC-1 is the repository and commit registered in boundary.md. Direct source inspection supplies implementation evidence; shipped prompts and library instructions supply doctrine/design. No target execution or provider call was performed. Model internals, resolved Chroma/embedding behavior and external community checkpoints remain outside the frozen source. No observed learning gain, cache correctness or actual invocation of a retrieved skill is established.

The supplied runtime was used as a route inventory, then checked directly against `voyager/voyager.py`, all four agent implementations, the recorder, observation base/chests/voxels, skill loader, chest primitive, setup and public import. Prompt skill summarization and a trial1 wood-log code/description pair were read directly. The runtime's executor account supplies the remaining execution evidence. Paths below are SRC-1 anchors; records identify which findings are direct additions versus annotations on supplied findings.

| Entry point / operation | Source path | Coverage and limits |
|---|---|---|
| Learning admission, overwrite and resume | `voyager/agents/skill.py`; `voyager/voyager.py` | Direct: annotation on [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [MEM-OBJ-skills-code](#mem-obj-skills-code), description and index parts below. |
| Skill retrieval and execution read-back | `voyager/agents/skill.py`; `voyager/agents/action.py` | Direct: [MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval); supplied executor [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution). |
| Caller-supplied library / inference / decomposition | `voyager/voyager.py`; `skill_library/README.md` | Direct constructor and inference reads; [RT-RTE-task-inference](runtime.md#rt-rte-task-inference), [MEM-RTE-qa-cache](#mem-rte-qa-cache), [MEM-RTE-progress-update](#mem-rte-progress-update). Inference does not add skills but does update other retained state. |
| QA exact and semantic reuse | `voyager/agents/curriculum.py` | Direct: [MEM-RTE-qa-cache](#mem-rte-qa-cache). Separate answer payload and question index; actual distance semantics depend on unfrozen dependency. |
| Chest acquisition, replacement and removal | `voyager/env/mineflayer/lib/observation/chests.js`; `voyager/control_primitives/useChest.js`; `voyager/agents/action.py` | Direct: [MEM-RTE-chest-update](#mem-rte-chest-update). Invalid markers remove entries, but proximity omission does not. |
| Success/failure history cleanup | `voyager/agents/curriculum.py` | Direct: [MEM-RTE-progress-update](#mem-rte-progress-update). |
| Event persistence and resume-derived counters | `voyager/utils/record_utils.py` | Direct: [MEM-RTE-event-replay](#mem-rte-event-replay). Raw events are not an action-transcript reload. |
| Tick-based block memory / observation buffer | `voyager/env/mineflayer/lib/observation/voxels.js`; `voyager/env/mineflayer/lib/observation/base.js`; `voyager/env/mineflayer/index.js` | Direct: [MEM-OBJ-block-records](#mem-obj-block-records), [MEM-RTE-context-refresh](#mem-rte-context-refresh). Bot recreation initializes records anew; no disk reload traced. |
| Current action frames / critic and QA isolation | `voyager/voyager.py`; `voyager/agents/action.py`; `voyager/agents/critic.py`; `voyager/agents/curriculum.py` | Direct: [MEM-RTE-context-refresh](#mem-rte-context-refresh); supplied [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance). |
| Public API, HTTP operations and injected helpers | `voyager/__init__.py`; `setup.py`; `voyager/env/mineflayer/index.js`; `voyager/env/mineflayer/lib/skillLoader.js` | Direct public import/setup/registration reads and endpoint search. No console-entry declaration in inspected setup; shipped API and HTTP routes, not an invented CLI, define this inventory. Skill loader wraps bot methods and emits chat/save, not a separate learned-library loader. Direct executor remains [RT-RTE-environment-step](runtime.md#rt-rte-environment-step). |
| Shipped learned state | `skill_library/README.md`; `skill_library/trial1/skill/code/mineWoodLog.js`; `skill_library/trial1/skill/description/mineWoodLog.txt` | Direct sample and tree inventory. Other bodies and trial payloads not exhaustively read; parquet/bin/pkl payloads not decoded. Unknown initial authorship, embedding version and historical run lineage prevent asserting learned provenance or valid indexes for all three trials. |
| Bundled collection-plugin internals / other primitives | `voyager/env/mineflayer/mineflayer-collectblock/`; `voyager/control_primitives/` | Included executor dependencies, not exhaustively inspected for internal transient queues. Supplied runtime covers execution boundary; no claim of exhaustive plugin-state characterization or all individual action correctness. |

## Core ideas

1. Skill selection and execution authority differ. A semantic query selects descriptions but returns code to the action model. Independently, every active skill definition enters Node's executable programs string. Top-k is not an execution allowlist ([MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution)).
2. Retention is not one store. QA answers are model-generated guidance; chest maps summarize game observations; task lists change curriculum disclosure and inference indexing; event replay reconstructs accounting. Their admission and withdrawal rules differ ([MEM-RTE-qa-cache](#mem-rte-qa-cache), [MEM-RTE-chest-update](#mem-rte-chest-update), [MEM-RTE-progress-update](#mem-rte-progress-update), [MEM-RTE-event-replay](#mem-rte-event-replay)).
3. The action window is replaced, not compacted by a summarization model. Last code, current observations and latest critique survive into the next frame; regex-extracted unmet requirements affect retrieval. Other diagnostic turns remain outside the next call. Curriculum filtering and separate critic/QA/description calls impose other context boundaries ([MEM-RTE-context-refresh](#mem-rte-context-refresh)).
4. Admission preserves a successful program and generated description, not a structured explanation of why it succeeded. Model/human task success gates learning admission; direct manager calls bypass that gate. Reuse benefit and exercised self-improvement remain unobserved ([RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-skills-code
Label: skills code entries

Source-native identity: `self.skills[program_name]["code"]`. Symbolic JavaScript; Python map and `skill/skills.json`, with separate versioned `skill/code/*.js` archival copies. Lineage: parsed action function declarations admitted after learning success, or loaded from a caller-selected checkpoint. Unlike [RT-OBJ-program-code](runtime.md#rt-obj-program-code), this is the retained active library mapping across tasks, not the current action parser result. It supplies prompt examples and executable definitions. Same-name replacement changes the active value; archived filenames are not the reload source. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`; admission passage in [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

#### MEM-OBJ-skill-description
Label: skill description entries

Source-native identity: `self.skills[program_name]["description"]` and `skill/description/*.txt`. Natural-language summary inside a JavaScript-shaped display wrapper, stored as text and JSON; not the skill implementation. Generated from code and main name by the description model, then embedded for selection. The prompt requests omission of helper/chat detail and at most six sentences; it does not assess correctness or retain critic reasons. Distinct from runtime's current program and admission route; paired with [MEM-OBJ-skills-code](#mem-obj-skills-code). Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/prompts/skill.txt`, sampled `skill_library/trial1/skill/description/mineWoodLog.txt`.

> 3) There might be some helper functions before the main function, but you only need to describe the main function.
> 4) Try to summarize the function in no more than 6 sentences.
> --- `voyager/prompts/skill.txt`

#### MEM-OBJ-skill-vectordb
Label: skill_vectordb

Source-native identity: Chroma `skill_vectordb` in `skill/vectordb`. Description documents are natural-language content in wrappers; name metadata/IDs are symbolic lookup keys; embeddings are distributed-parametric numerical access representations. Disk Chroma storage and an external embedding service are distinct. The embedding component's mutability limits are [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings); vectors are outputs, not the service's parameters. Voyager stores the generated description, ID and name metadata, then uses the returned name to fetch actual code. Shipped binary payloads were enumerated, not decoded; exact historic embeddings remain unresolved. Evidence: SRC-1, `voyager/agents/skill.py`; [MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval). No supplied object counterpart after comparison; this is the index, not the runtime admission route or current program.

#### MEM-OBJ-qa-cache
Label: qa_cache

Source-native identity: `CurriculumAgent.qa_cache`, question → answer map in Python and `curriculum/qa_cache.json`. Natural-language questions/answers with symbolic exact-key lookup. Initial checkpoint authorship is unresolved; new answers come from QA model calls, not verified game traces. Model-generated observation questions and normalized task questions both enter it. Curriculum and action task context consume answers as guidance; no independent answer oracle is established. Distinct retained object behind [RT-RTE-task-selection](runtime.md#rt-rte-task-selection), not that route itself. Evidence: SRC-1, `voyager/agents/curriculum.py`; [MEM-RTE-qa-cache](#mem-rte-qa-cache).

#### MEM-OBJ-qa-questions
Label: qa_cache_questions_vectordb

Source-native identity: Chroma question collection in `curriculum/vectordb`. Natural-language question documents, numerical distributed-parametric embeddings and symbolic collection/access metadata. Answers remain in [MEM-OBJ-qa-cache](#mem-obj-qa-cache), not necessarily in the returned document. Semantic reuse fetches the answer using returned question text. Same external embedding-version limits as [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings); no parameter-training operation is established by adding documents. Distinct from supplied component: this is retained index output. Evidence: SRC-1, `voyager/agents/curriculum.py`.

#### MEM-OBJ-chest-memory
Label: chest_memory

Source-native identity: `ActionAgent.chest_memory`. Symbolic position-keyed item-count maps and `Unknown` markers, Python map plus `action/chest_memory.json`. Derived from Node observation data, not an action transcript. Human-readable rendering is a separate natural-language display for action, curriculum and critic consumers. Updates retain prior knowledge for unmentioned positions; explicit `Invalid` removes them. No timestamp/freshness validation is applied by the inspected updater. Distinct state used by supplied judgment/selection routes, not duplicate of them. Evidence: SRC-1, `voyager/agents/action.py`, `voyager/env/mineflayer/lib/observation/chests.js`; [MEM-RTE-chest-update](#mem-rte-chest-update).

#### MEM-OBJ-task-histories
Label: completed_tasks and failed_tasks

Source-native identity: curriculum lists in Python and `curriculum/{completed_tasks,failed_tasks}.json`. Task strings are natural-language content; membership, order and completed-count are symbolic control state. Outcome lineage is critic/human success or driver exception failure, not an independently verified reference outcome. Completed strings are deduplicated; repeated failures remain except for tasks later completed. Their count controls disclosure, difficulty and inference indexing. Distinct retained parts of the state used by [RT-RTE-task-selection](runtime.md#rt-rte-task-selection) and [RT-RTE-task-inference](runtime.md#rt-rte-task-inference). Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/voyager.py`.

#### MEM-OBJ-events
Label: events checkpoint

Source-native identity: recorder's task/timestamp-named JSON files under `events/`. Symbolic event records with embedded natural-language chat/error text; raw observation traces rather than learned skill explanations. Derived recorder summaries (`item_history`, item/time/iteration maps, elapsed time and position history) are symbolic in-memory accounting. Resume reconstructs these from files. Event recorder iteration controls the learning loop, so this is not merely write-only logging; no replay into the action message list is wired by the inspected driver. Distinct from [RT-RTE-environment-step](runtime.md#rt-rte-environment-step)'s immediate response. Evidence: SRC-1, `voyager/utils/record_utils.py`, `voyager/voyager.py`; [MEM-RTE-event-replay](#mem-rte-event-replay).

#### MEM-OBJ-block-records
Label: BlockRecords.records

Source-native identity: `BlockRecords.records`, a symbolic JavaScript Set of encountered block-name strings in the bot observation object. Every 100 physics ticks, blocks in an 8×2×8 offset neighborhood that are not current inventory item names are added. `observe()` returns names; curriculum computes “other blocks” by subtracting present voxels and inventory names. This is a derived encounter memory, not saved coordinates or a spatial map. Bot recreation constructs a new Set; an explicit reset method also clears it, but the inspected observation base does not call it after every observe. It can therefore span multiple observations within one bot lifetime. Distinct material part of the observation state behind [RT-RTE-environment-step](runtime.md#rt-rte-environment-step), with a later curriculum consumer. Evidence: SRC-1, `voyager/env/mineflayer/lib/observation/voxels.js`, `voyager/env/mineflayer/lib/observation/base.js`, `voyager/env/mineflayer/index.js`, `voyager/agents/curriculum.py`.

> getSurroundingBlocks(this.bot, 8, 2, 8).forEach((block) => {
>     if (!items.has(block)) this.records.add(block);
> });
> --- `voyager/env/mineflayer/lib/observation/voxels.js`

### Routes

#### MEM-RTE-skill-retrieval
Label: Skill retrieval read-back

Driver reset or executed step → manager query/Chroma search → metadata-name lookup in active skills → action system message. Python owns selector/delivery. This is the read half downstream of [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), not a duplicate admission or execution route. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`, `voyager/agents/action.py`.

- Immediate return: list of actual skill code strings, empty when collection count is zero.
- Later read-back: changed active skill code reaches subsequent action calls, across tasks and reloads; descriptions/vectors only select which code.
- Delegated visibility: Chroma receives query; action model receives selected code and primitive context, not scores, all stored descriptions or the entire library.
- Selection predicate: task context at reset; context plus regex-extracted unmet crafting/mining needs after execution; k is min(collection count, configured retrieval_top_k), default five, without a local score threshold or token budget.
- Invalidation or expiry: same-name admission deletes old index ID and replaces active map; reload loads skills.json, not versioned archives. No failure-triggered skill withdrawal in inspected manager/driver.
- Activation or effect: selected code supplies model guidance; all active code independently enters executor via the supplied runtime authority path. Specific invocation and benefit unobserved.
- Evidence limits: Chroma ranking internals/version unresolved; count equality alone cannot prove matching identities or semantics.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for doc, _ in docs_and_scores:
>     skills.append(self.skills[doc.metadata["name"]]["code"])
> return skills
> --- `voyager/agents/skill.py`

#### MEM-RTE-qa-cache
Label: QA cache write and reuse

Curriculum question generation or requested task context → exact/semantic cache decision → QA model on miss → JSON/index persistence → curriculum prompt or action context. Curriculum code owns reuse/admission; QA model authors answers. New observation questions include three fixed biome questions plus parsed model proposals. Trigger is task-context lookup or context-enabled curriculum rendering; operating mode is guidance during learning/inference, not evaluation against an answer oracle. No per-answer human approval, correctness veto or automatic rollback is wired here. The prompt/render filter is not a store-admission check. Distinct write/read mechanism behind [RT-RTE-task-selection](runtime.md#rt-rte-task-selection). Evidence: SRC-1, `voyager/agents/curriculum.py`.

- Immediate return: question/answer lists from run_qa or formatted task context from get_task_context.
- Later read-back: cached answers affect future curriculum messages and action task contexts; resume reloads QA JSON and opens persisted index.
- Delegated visibility: answer model gets a question and dedicated QA prompt, not the action transcript; selected answers reach curriculum/action as text.
- Selection predicate: run_qa uses one nearest question when its score is below 0.05; task context instead normalizes underscores, ore/ores and periods and uses exact cache keys. Curriculum shows at most five eligible pairs, skips answers containing Answer: Unknown or language model, and applies progress/probability context gating; task-context path does not apply those answer filters.
- Invalidation or expiry: no automatic TTL, answer correction or retraction in inspected methods; a hit reuses an answer, not a new verified response. Constructor asserts index count equals cache size.
- Activation or effect: software admits generated answers without human per-content approval; delivered answers are advisory model context, not enforced facts or expected-result keys.
- Evidence limits: semantic threshold behavior depends on external Chroma; generated answers may be wrong; initial checkpoint authority unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if docs_and_scores and docs_and_scores[0][1] < 0.05:
>     question_cached = docs_and_scores[0][0].page_content
>     assert question_cached in self.qa_cache
>     answer_cached = self.qa_cache[question_cached]
> --- `voyager/agents/curriculum.py`

> if question in self.qa_cache:
>     answer = self.qa_cache[question]
> else:
>     answer = self.run_qa_step2_answer_questions(question=question)
> --- `voyager/agents/curriculum.py`

#### MEM-RTE-chest-update
Label: Chest observation retention

Bot chest discovery/close/remove events → Node chestsItems → final nearbyChests → Python updater → chest JSON/rendering → later action/curriculum/critic. Code owns acquisition and admission, not a human curator. The chest primitive can aggregate actual container counts, emit an empty map, or mark a missing chest Invalid. Observations can also contain Unknown for discovered but unopened chests. This is a distinct retained-state path used by supplied [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment). Evidence: SRC-1, `voyager/control_primitives/useChest.js`, `voyager/env/mineflayer/lib/observation/chests.js`, `voyager/agents/action.py`, `voyager/voyager.py`, `voyager/agents/critic.py`.

- Immediate return: updater mutates map and dumps JSON; renderer returns position/item summaries grouped as populated, empty, then unknown.
- Later read-back: saved map reloads on resume; later action and critic messages include rendered map; curriculum can select deposit work from it.
- Delegated visibility: models see rendered content, not container handles or full event provenance; action omits chest display for deposit tasks.
- Selection predicate: Node finds chest blocks within distance 16, count limit 999, plus chest event state; Python processes every supplied position and retains others. Renderer has no top-k/token cap.
- Invalidation or expiry: explicit Invalid removes existing positions; dict observations replace counts; Unknown does not overwrite an existing known dict. Omitted positions persist without TTL. These rules can preserve stale information.
- Activation or effect: an automatic trace-fed map update changes later context and may trigger hardcoded inventory management; no observed task consequence established.
- Evidence limits: generated code can emit bot events; observational lineage is not an authenticated source guarantee, and game synchronization remains external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if isinstance(chest, dict):
>     self.chest_memory[position] = chest
> if chest == "Invalid":
>     print(
>         f"\033[32mAction Agent removing chest {position}: {chest}\033[0m"
>     )
>     self.chest_memory.pop(position)
> --- `voyager/agents/action.py`

#### MEM-RTE-progress-update
Label: Task progress retention

Rollout info or caught learning exception → curriculum success/failure append → cleanup → JSON → later curriculum and inference. Driver/critic or manual human determines input success; cleanup code decides list membership. No independent answer oracle or human approval of each list mutation. Deposit tasks are rejected from progress recording. This expands retained-state maintenance, not duplicate identity with the enclosing [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop) or [RT-RTE-task-inference](runtime.md#rt-rte-task-inference). Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/voyager.py`.

- Immediate return: updated deduplicated completed list and failure list are persisted; no substantive return value.
- Later read-back: resume reloads lists; contents enter curriculum prompts, count changes warmup disclosure and game difficulty, and inference uses count as next-subgoal index.
- Delegated visibility: curriculum model sees text of admitted history subject to rendering rules; driver sees count, not a calibrated competence estimate.
- Selection predicate: success appends completed, failure appends failed; completed strings are kept once in order and removed from failed history, while repeat failures otherwise remain.
- Invalidation or expiry: inference clears in-memory histories before subgoal execution; later updates dump those new histories. Cleanup withdraws failed membership after success, not associated skill code or QA answers.
- Activation or effect: automatic outcome-derived state shapes future work and context; no measured improvement established.
- Evidence limits: task labels are not execution proofs; repeated/duplicate inference subgoals can stall progress as supplied runtime notes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # remove completed tasks from failed tasks
> for task in updated_completed_tasks:
>     while task in updated_failed_tasks:
>         updated_failed_tasks.remove(task)
> --- `voyager/agents/curriculum.py`

#### MEM-RTE-event-replay
Label: Event checkpoint replay

Environment events → recorder JSON → constructor resume / public resume(cutoff) → derived metrics and iteration → learning-loop limit. Recorder code owns persistence/reconstruction; no separate human admission, semantic curation or answer oracle. Unlike skill retention this does not synthesize an executable capability. Distinct route after [RT-RTE-environment-step](runtime.md#rt-rte-environment-step). Evidence: SRC-1, `voyager/utils/record_utils.py`, `voyager/voyager.py`.

- Immediate return: record increments iteration, updates item/time accounting and writes event list under sanitized task/timestamp filename; no substantive return.
- Later read-back: resume sorts event files by timestamp and reconstructs item, elapsed-time and position histories; iteration is consulted by learn's max_iterations condition.
- Delegated visibility: recorder receives full returned events; no inspected driver path supplies reconstructed event files as the action transcript.
- Selection predicate: every recorded action attempt; resume scans timestamp-named files, optionally stops past cutoff. It is chronological replay, not targeted semantic retrieval.
- Invalidation or expiry: no automatic file expiry in inspected recorder; derived summaries are rebuilt. Empty initial event lists can break position initialization, so recording is not guaranteed for every attempted parse failure.
- Activation or effect: resumed accounting can terminate later learning; the other summaries are analysis/accounting capabilities, with no further model consumer established in inspected driver.
- Evidence limits: raw records do not establish authenticated observed runs in this analysis; no target was executed. Same-second filename collision and arbitrary filesystem edits are not protected by a transaction here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> events = load_json(f_join(self.ckpt_dir, "events", record))
> --- `voyager/utils/record_utils.py`

> if self.recorder.iteration > self.max_iterations:
>     print("Iteration limit reached")
>     break
> --- `voyager/voyager.py`

#### MEM-RTE-context-refresh
Label: Working context replacement

Executed action/events and latest critique → code-selected new system/human pair → next action model call. Driver owns replacement; action renderer and regex helper select content. This is the transformation inside supplied [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance), not a duplicate of that authority path. Parallel context controls isolate critic, description and QA calls; curriculum has progress/probability filtering. Evidence: SRC-1, `voyager/voyager.py`, `voyager/agents/action.py`, `voyager/agents/critic.py`, `voyager/agents/curriculum.py`, `voyager/agents/skill.py`; runtime's two-message replacement quote supports the core operation.

- Immediate return: new two-message context after execution; rollout returns final messages and diagnostic conversations in info. Parse failure keeps prior messages.
- Later read-back: latest code/current observations/latest critique cross to next attempt, retained skill/chest/QA/history state can re-enter later calls. Old conversations have no automatic reload in inspected driver.
- Delegated visibility: diagnostic triples retain system/human/AI text in Python but are not the next message list; critic sees selected final state/task/context/chests, not program or full transcript. Skill-description model sees code/main name; QA-answer model sees question; only selected returned text escapes these frames.
- Selection predicate: refresh after valid execution, retrieve again with context plus regex chat extraction; last code and configured error/chat text survive. Curriculum hides categories until thresholds, then includes nonzero-threshold categories with probability 0.8; optional inventory is regex-filtered early, QA capped at five eligible pairs. No general action token-budget cap is wired.
- Invalidation or expiry: reset clears per-task conversation diagnostics and replaces frame; next execution replaces previous critique/code. Node observe clears cumulativeObs after delivery, not every observer's internal state; blockRecords can still feed later curriculum observations until bot recreation.
- Activation or effect: copied text guides the next model invocation, not executable references into out-of-window state; specific compliance remains unobserved.
- Evidence limits: no model-generated compaction is involved in the inspected replacement; arbitrary external LangChain/provider context handling remains uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return "I also need " + ", ".join(chatlog) + "." if chatlog else ""
> --- `voyager/agents/action.py`

> const result = bot.cumulativeObs;
> bot.cumulativeObs = [];
> return JSON.stringify(result);
> --- `voyager/env/mineflayer/lib/observation/base.js`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Memory-specific lineage: action-model response → parsed function declarations → successful learning info → active code map; separate code/main-name → description model → description document/embedding. Critic success licenses admission but its critique and full diagnostic conversations are not fields in the stored skill entry. Code comments may retain local reasons; the mechanism does not retain a structured success explanation or critic rationale for future retrieval. Consumers receive code or selection metadata, not the old task judgment record. Evidence: SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`, `voyager/prompts/skill.txt`; [MEM-OBJ-skills-code](#mem-obj-skills-code), [MEM-OBJ-skill-description](#mem-obj-skill-description), [MEM-OBJ-skill-vectordb](#mem-obj-skill-vectordb).

Admission control is software-conditioned on task success in learn, with manual human success judgment only in manual critic mode. No further human editing/approval is required. Public add_new_skill accepts supplied info without inspecting its success field. Caller-selected skill_library_dir loads existing content even without general resume; caller identity does not establish human per-entry authorship. Initial shipped-library control stays unresolved.

Same-name writes first delete the index ID, then generate the next available V-number archive filename, add the new description under the original name, replace active JSON/map entry and persist. Old text files survive but are not automatically rolled back into active use. Count assertions test cardinality, not key/content agreement or atomicity. Failure at a later task does not remove that skill. Evidence: SRC-1, `voyager/agents/skill.py`.

> if program_name in self.skills:
>     print(f"\033[33mSkill {program_name} already exists. Rewriting!\033[0m")
>     self.vectordb._collection.delete(ids=[program_name])
> --- `voyager/agents/skill.py`

#### On [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution)

Stored active code, not description-only display stubs, is concatenated for execution; primitive code is appended separately. No retrieval top-k or description score bounds this channel. Loaded checkpoint content acquires executable definition authority at eval without passing a new critic decision. Actual calls depend on generated function references; delivery is not proof that every loaded skill runs. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`; supplied execution quote and [MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval).

## Write side

Acquisition has several independent admission controls. Skill authorship is model-generated code and a separately generated description, while learning admission is the driver's success-conditioned call and manager's deposit-prefix exclusion. QA admission is miss-driven cache insertion, not answer validation. Chest retention automatically transforms observed container counts and explicit invalidation into a persistent map. Progress retention transforms success/failure into cleaned lists. Event persistence keeps traces and reconstruction produces accounting, not skill proposals. No one of these write controls should stand for the others. The corresponding route records above retain their human/software distinction and later consumers.

There are three clear trace-fed behavior-shaping chains: action outcome → admitted skill → later model/executor; chest event → merged map → later context/task override; task outcome → cleaned history → later task selection/disclosure/indexing. QA answers instead originate in model prior knowledge, although observation context helps generate questions. Events → replay counters → learning limit is a trace-fed control-state reconstruction, not semantic reflection. Block encounter sets provide transient derived memory across observations. None of these chains by itself proves improved capacity.

Withdrawal is local: replacement retires an active skill name's former content but keeps archival files; progress cleanup removes failures after success; Invalid chest markers remove that position; frame replacement evicts old turns. QA insertion has no corresponding automatic answer correction in the inspected methods. A failed transfer does not trigger coordinated retraction of skill code, description, QA answer or success history. These conclusions are bounded to the directly inspected manager, agents and driver, not external checkpoint editing tools.

## Read-back

[MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval) is a driver-requested selection chain, not an independently unsolicited memory push. Its query targets task context and unmet requirements. Names returned by Chroma are actual code-lookup keys; file identifiers alone would not establish that selection. The distinct all-programs delivery is automatic whenever the driver executes an action, with no top-k filter.

[MEM-RTE-qa-cache](#mem-rte-qa-cache) has two non-equivalent read paths. Semantic nearest-question reuse and exact normalized-task lookup can return different answers. Only curriculum display filters unsuitable-answer strings and caps eligible QA pairs; task-context delivery can pass those answers unchanged. [MEM-RTE-chest-update](#mem-rte-chest-update) renders the retained map wholesale, so proximity controls acquisition rather than a global freshness or read budget. [MEM-RTE-progress-update](#mem-rte-progress-update) supplies both interpreted task history and fixed-rule control counts. [MEM-RTE-event-replay](#mem-rte-event-replay) supplies accounting on resume, not a conversational history.

Working contexts resemble separate call frames with selected textual returns: latest critique, descriptions and QA answers escape their producing calls, while entire old action turns are not accumulated in the next call. The analogy breaks at references: the next model receives text by value, not dereferenceable pointers to old conversations. Retained files remain reachable only through the explicit skill/QA/chest/history/replay paths, not through an implicit context heap ([MEM-RTE-context-refresh](#mem-rte-context-refresh)).

## Integration issues

- No supplied finding requires correction. A useful qualification to runtime's context account is that clearing the cumulative observation response does not clear BlockRecords.records. Its 100-tick derived encounter set remains available to later curriculum rendering within a bot lifetime. Evidence: SRC-1, `voyager/env/mineflayer/lib/observation/voxels.js`, `voyager/env/mineflayer/lib/observation/base.js`; [MEM-OBJ-block-records](#mem-obj-block-records), [MEM-RTE-context-refresh](#mem-rte-context-refresh), [RT-RTE-environment-step](runtime.md#rt-rte-environment-step).
- No possible duplicate declaration is identified after comparison. Stored library code differs from the current [RT-OBJ-program-code](runtime.md#rt-obj-program-code); indexes differ from [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings); new routes isolate mechanisms within the supplied enclosing routes. Existing admission/execution referents receive annotations, not redeclarations.
- Shipped trial index contents, historical embedding identities and initial content approval are unresolved. The tree/sample and loader establish a consumption path but not consistent or beneficial historical learning. Evidence: SRC-1, `skill_library/README.md`, `voyager/agents/skill.py`; [MEM-OBJ-skill-vectordb](#mem-obj-skill-vectordb), [MEM-OBJ-skills-code](#mem-obj-skills-code). This prevents attributing all distributed skills to the inspected learning process.
- Chroma score semantics and provider state remain unfrozen. The code establishes a below-0.05 question reuse condition and top-k skill request, not calibrated semantic similarity or reproducible embeddings. Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/agents/skill.py`; [MEM-RTE-qa-cache](#mem-rte-qa-cache), [MEM-RTE-skill-retrieval](#mem-rte-skill-retrieval).

## Limitations and checks

HEAD was rechecked as 55e45a880755d0c8c66ca7fb5fe7962ac8974f89; source identity matches the supplied boundary and run. No source identity or scope change, target execution, model request, external acquisition or prior-analysis reading was used. A nonexistent guessed blockRecords filename was resolved by searching the actual observation tree and reading voxels.js; no absence conclusion was drawn from that failed read. Available but unread library/plugin payloads remain identified in coverage rather than treated as absent evidence.

This is implementation/doctrine evidence only. Static forcing cases include direct manager admission bypassing learn's gate, exact QA lookup bypassing curriculum filtering, stale chest entries surviving omission, and all-skill execution supply bypassing prompt top-k. They bound conclusions without claiming observed failures. Validation: the required `commonplace-run validate-output` check passed with “Member content check passes; invocation residue not checked.” This establishes form/quote occurrence, not operation, benefit, job acceptance or claim support.
