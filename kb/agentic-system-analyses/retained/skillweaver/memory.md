---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SkillWeaver memory: trace-derived Python skills, documentation and test metadata, checkpoint reload and native/controller consumers."
run-id: AAS-2026-10-14-skillweaver-c921cc7a5ed0-01
source-identity: https://github.com/OSU-NLP-Group/SkillWeaver
reviewed-boundary: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
---

# SkillWeaver memory report

## Boundary and evidence

The subject is SkillWeaver's builder and its shipped consumers at the frozen revision above. Evidence is SRC-1 from the [source register](boundary.md#source-register). The checkout HEAD was rechecked against that revision. Direct inspection covers the full knowledge-base implementation, prompt construction and relevant templates, task execution/persistence, exploration update/checkpoint progression, recovery disabling, state persistence and the Browser-Use handoff. The supplied runtime supplies the execution and benchmark baseline; it is not treated as observed operation.

Included memory surfaces are executable skill bodies, model-readable skill documentation, test/version/reference metadata, semantic text, raw browser/action artifacts, synthesis diagnostics and optional embedding cache. Working-context selection and task-frame disposal are included even when they produce no retained summary. Website-side state, browser authentication and external provider parameters are dependencies, not SkillWeaver's learned library. External Browser-Use context management and provider internals are uninspected; the report cannot determine their hidden retention, training or prompt truncation. Static shipped templates and skill libraries are inputs, not evidence of within-run learning. No execution or causal experiment was supplied or performed.

| Entry point or memory operation | Source path in SRC-1 | Coverage and conclusion limits |
|---|---|---|
| Synthesize, merge, save and load | `skillweaver/knowledge_base/knowledge_base.py` | Direct complete read; [MEM-OBJ-code](#mem-obj-code), [MEM-OBJ-docstring](#mem-obj-docstring), [MEM-OBJ-metadata](#mem-obj-metadata), annotations on [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). |
| Test scheduling, success judgment and checkpoints | `skillweaver/explore.py` | Direct selection/update progression and CLI reload read; [MEM-OBJ-metadata](#mem-obj-metadata), [MEM-OBJ-traces](#mem-obj-traces); supplied [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice). |
| Code checks and update guidance | `skillweaver/knowledge_base/code_verification.py`, `skillweaver/templates/kb_procedural_update_base.md`, `skillweaver/templates/kb_procedural_update_single.md` | Direct complete reads; annotation on [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Static checks do not guarantee final rejection. |
| Native relevance selection and fallback | `skillweaver/create_skill_library_prompt.py`, `skillweaver/templates/predict_relevant_functions.md`, `skillweaver/templates/__init__.py` | Direct complete reads; annotation on [RT-RTE-native-task](runtime.md#rt-rte-native-task). |
| Native prompt reconstruction, trajectory formatting and artifact persistence | `skillweaver/agent.py`, `skillweaver/attempt_task.py`, `skillweaver/environment/state.py` | Direct relevant formatting/persistence ranges and complete state read; [MEM-OBJ-traces](#mem-obj-traces). Execution assembly additionally relies on supplied [RT-RTE-native-task](runtime.md#rt-rte-native-task). |
| Recovery, task-local disabling and alternative trace display | `skillweaver/environment/patches.py`, `skillweaver/agent.py` | Direct disabling and formatter reads; annotation on [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery). No guaranteed durable locator repair. |
| Semantic text | `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/templates/propose_skill.md`, `skillweaver/templates/kb_procedural_update_single.md` | Direct reads; [MEM-OBJ-semantic-knowledge](#mem-obj-semantic-knowledge). Initial content provenance unknown; inspected update does not synthesize new semantic text. |
| Embedding similarity API/cache | `skillweaver/knowledge_base/knowledge_base.py` | Direct complete read; [MEM-RTE-embedding-selection](#mem-rte-embedding-selection), supplied [RT-CMP-embed](runtime.md#rt-cmp-embed). No shipped consumer found by scoped Python call-site search. |
| OpenAI tool-schema exports | `skillweaver/knowledge_base/knowledge_base.py` | Direct complete read; [MEM-OBJ-docstring](#mem-obj-docstring). Exposed export capability, no caller found by scoped Python call-site search; no end-to-end consumer inferred. |
| Browser-Use registered actions | `skillweaver/attempt_task_browser_use.py`, `skillweaver/knowledge_base/knowledge_base.py` | Direct retrieval/handoff and complete controller reads; annotation on [RT-RTE-browser-use](runtime.md#rt-rte-browser-use). External planner behavior uninspected. |
| Benchmark reload and retained scores | `skillweaver/evaluation/evaluate_benchmark.py`, `skillweaver/evaluation/evaluate_single_task.py` | Supplied [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation); no independent evaluator-body audit. Cannot establish score correctness or working clean-tree entry. |
| Shipped skill initial content | `skillnet/map/map_kb_post_code.py` | Direct opening sample; reported usage documentation, not observed executions. Other library contents are inventoried/sampled by boundary, not fully inspected here; no all-skills correctness or provenance claim. |
| Model/provider state | `skillweaver/lm.py` | Supplied [RT-CMP-lm](runtime.md#rt-cmp-lm); hidden provider persistence and exact weights uninspected. |

## Core ideas

SkillWeaver retains experience principally as Python functions, not as a searchable transcript archive. Task execution produces raw artifacts; a selected text trajectory and success decision can prompt synthesis; same-name function replacement changes future executable machinery. Function documentation is a separate, model-interpreted channel: retrieval presents signatures/docstrings, while native execution can access the full code library. These two selections are not the same capability boundary ([MEM-OBJ-code](#mem-obj-code), [MEM-OBJ-docstring](#mem-obj-docstring), [RT-BAP-library-execution](runtime.md#rt-bap-library-execution)).

Test metadata affects which functions get practice and which descriptions appear as verified. An automatic test-counter increment means the last action's source contains a matching named-call AST node and its result records no exception or recovery attempt. It establishes neither dynamic execution of that skill nor verified task semantics. Caller-supplied metadata or `mark_all_as_tested` can also create that visibility state ([MEM-OBJ-metadata](#mem-obj-metadata)).

The context budget is primarily structural: select library descriptions once per task, show current browser observation, format earlier actions, and use separate model calls for retrieval, success and synthesis. There is no source-supported persisted conversation summary on this route. Rich artifacts remain on disk, but the builder's synthesis input omits intermediate states and recovery annotations by default ([MEM-OBJ-traces](#mem-obj-traces)). This omission matters more than the label “trajectory.”

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-code
Label: KnowledgeBase function bodies

Source-native identity: `KnowledgeBase.code`, specifically the callable Python definitions apart from their documentation channel. Representational form: symbolic Python. Storage: in-process string, AST during merge, `_code.py` on disk, imported native action module or captured controller function objects at consumption. Lineage: optional caller-provided code/library or empty initialization, then model synthesis from practice and selected existing source. Initial authorship and approval of an arbitrary loaded prefix remain unknown. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`.

> merged_tree = ast.Module(body=list(updated_functions.values()), type_ignores=[])
> --- `skillweaver/knowledge_base/knowledge_base.py`

The merge keeps only function definitions; same-name candidates replace bodies, omitted existing names remain. It is not a deletion-by-omission protocol. A replacement loses the previous body in the live object, though earlier checkpoint files can retain it. Native and controller consumers give this material execution authority, not just interpretive influence. Closest supplied record is [RT-BAP-library-execution](runtime.md#rt-bap-library-execution): this object is its retained input, not a duplicate path. Admission belongs to [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), not physical `save` I/O.

#### MEM-OBJ-docstring
Label: Function documentation and readable skill display

Source-native identity: AST-extracted function `docstring`, signature and `format_function_as_pretty_string` display. Form: natural-language explanations and usage logs, with symbolic signatures/schema fields. Storage: embedded in the same `_code.py` artifact as [MEM-OBJ-code](#mem-obj-code), extracted into transient `Function` dictionaries and prompt strings. Distinct operative part: retrieval and model guidance consume this readable display rather than executing it. Closest supplied [RT-RTE-native-task](runtime.md#rt-rte-native-task) and [RT-RTE-browser-use](runtime.md#rt-rte-browser-use) are consuming routes, not the documentation object. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`.

> return f"# Skill: {_get_function_signature_string(fn)}\n{_get_unindented_docstring(fn)}\n\n"
> --- `skillweaver/knowledge_base/knowledge_base.py`

The synthesis template requests generalized behavior, unexpected outcomes, feedback and usage logs. These may retain reasons, but compliance is not established by the request or by a docstring-presence check. A shipped sample reports successful uses; it is reported operation, not independently authenticated trace evidence (SRC-1, `skillweaver/templates/kb_procedural_update_base.md`, `skillnet/map/map_kb_post_code.py`).

> In your docstring, you must include a "usage log" which describes the different times you've used the function and what happened.
> --- `skillweaver/templates/kb_procedural_update_base.md`

Later readers include the relevance model, action model, synthesis model through selected complete sources, and external controller through registered action documentation. They receive model-interpreted guidance, not guaranteed obedience. Exposed OpenAI chat/responses schema exporters truncate function descriptions to a default 1000 characters and argument descriptions similarly; no shipped Python caller was found for these exporters, so these are offered representations, not established read-back routes. Native pretty displays have no equivalent fixed truncation in this implementation (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`).

#### MEM-OBJ-metadata
Label: Function test, version and lineage metadata

Source-native identity: `metadata['functions']` and `global_version`. Form: symbolic counters, function names, reference strings and event lists. Storage: mutable dictionary and `_metadata.json`; distinct from executable content and documentation. `_apply` records update references/events and resets test count; `increment_test_count` increments the count and records `exception_free_test`. Consumers use `test_count > 0` for visibility/verified filtering, untested scheduling and synthesis inclusion; version affects practice utility. References are access/lineage metadata, not the experience content itself. No automatic traversal from reference string to the original trace was found in the full knowledge-base read. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/explore.py`.

> def is_tested(self, function_name: str) -> bool:
>     return function_name in self.metadata["functions"] and (
>         self.metadata["functions"][function_name]["test_count"] > 0
>     )
> --- `skillweaver/knowledge_base/knowledge_base.py`

> def rate_practice_utility(self, fn: Function):
>     return (
>         count_interactions(fn) - self.metadata["functions"][fn["name"]]["version"]
>     )
> --- `skillweaver/knowledge_base/knowledge_base.py`

Admission differs by operation: builder code increments after a syntactic named-call plus result-field shortcut; merge resets after candidate application; a supplied metadata file is accepted by `json.load` without replaying tests. The automatic shortcut searches the entire parsed last-action source for a matching `ast.Name` call node, then checks recorded exception/recovery fields. It does not establish that the named function executed: a call under `if False` can satisfy the source search without running. Thus the stored event label `exception_free_test` is not execution coverage. The source passages and countercase are supplied by [EPI-RTE-test-check](epistemic.md#epi-rte-test-check); the later counter authority agrees with [EPI-RTE-tested-label](epistemic.md#epi-rte-tested-label). The exposed `mark_all_as_tested` method sets each stored entry's test count/version to one and replaces references/events with a marker. Its ultimate caller/approval principal is not established; this capability is not evidence that all entries were tested. Missing metadata falls back to entries for top-level asynchronous definitions except `main`; that fallback is not a test or a complete schema repair. Exploration CLI reload deliberately discards references, but preserves other loaded fields including events. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/explore.py`.

> if discard_references:
>     for fn_name in kb.metadata["functions"].keys():
>         kb.metadata["functions"][fn_name]["references"] = []
> --- `skillweaver/knowledge_base/knowledge_base.py`

`copy` passes the same metadata dictionary into another object; it is not an independently isolated metadata snapshot. These source-supported alternatives qualify any interpretation of “verified” as behavioral proof or complete preserved lineage. Closest supplied records are [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice) and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission): this is shared state consumed/changed by both, not a new declaration of either route.

#### MEM-OBJ-semantic-knowledge
Label: Semantic knowledge text

Source-native identity: `semantic_knowledge`. Form: natural-language text by intended prompt use; arbitrary caller-provided contents are not audited. Storage: instance string and `_semantic_knowledge.txt`, with missing file defaulting to empty. This is distinct from function documentation and numeric metadata; closest supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) lists it as input, not an independently updated semantic store. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/templates/kb_procedural_update_single.md`, `skillweaver/templates/propose_skill.md`.

> semantic_update_diagnostics = None
> --- `skillweaver/knowledge_base/knowledge_base.py`

> with open(prefix_path + "_semantic_knowledge.txt", "w") as f:
>     f.write(self.semantic_knowledge)
> --- `skillweaver/knowledge_base/knowledge_base.py`

Initialization control and provenance of a supplied text file are unresolved. The inspected update preserves this field without synthesizing new semantic text; the model does receive it in the procedural-update template. The task-proposal model also receives it with current observation and existing names. Direct native action prompt construction does not include it: its template helper has the semantic argument commented out (SRC-1, `skillweaver/templates/__init__.py`). Thus loaded text can influence task proposals and skill synthesis; a separate trace-derived semantic-memory update is not established. These facts do not exclude an external caller editing the public field/file.

#### MEM-OBJ-traces
Label: Raw task artifacts and selected trajectory

Source-native identity: saved `State` artifacts, action JSON, `trajectory_pretty.txt`, `kb_update_diagnostics.json` and task/relevance/success diagnostics. Form: mixed symbolic structured records/code, natural-language reasoning and output, screenshots and DOM/accessibility observations; no inference that images are parametric memory. Storage: per-task/iteration filesystem artifacts and transient state/action lists. Lineage: browser observations, action-model responses, Python output/exceptions, optional recovery responses and synthesis/checker responses. These are evidence inputs or diagnostics, not the derived reusable library. Closest supplied [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice) and [RT-RTE-native-task](runtime.md#rt-rte-native-task) produce/consume these artifacts; no supplied operative-object counterpart exists. SRC-1, `skillweaver/environment/state.py`, `skillweaver/attempt_task.py`, `skillweaver/agent.py`, `skillweaver/explore.py`.

> def codegen_trajectory_to_string(
>     states: list[State],
>     actions: list[dict],
>     only_initial=True,
>     include_recoveries=False,
> ) -> str:
> --- `skillweaver/agent.py`

The native attempt writes an expanded trajectory with intermediate states and successful recovery annotations, but exploration subsequently overwrites the same file using the defaults and supplies that default string to success/synthesis. The latter contains initial state/tree, action reasoning/code, stdout/results/warnings and shortened exceptions; it omits intermediate state displays and recovery annotation insertion. The success checker separately receives the final screenshot. Raw action JSON and saved state artifacts still retain richer data. This is selective serialization, not a model-authored summary. SRC-1, `skillweaver/attempt_task.py`, `skillweaver/explore.py`, `skillweaver/agent.py`.

> string = codegen_trajectory_to_string(
>             states,
>             actions,
>             only_initial=False,
>             include_recoveries=True,
>         )
> --- `skillweaver/attempt_task.py`

> trajectory_string = codegen_trajectory_to_string(states, actions)
> --- `skillweaver/explore.py`

Synthesis diagnostics retain prompt instructions, candidate code, checker violations and response reasoning separately from checkpoint files. Loader reads code, metadata and semantic text, not these diagnostics. A folder-reconstruction helper can reload states/actions; that capability alone does not establish an automated later consumer. Reasons reach future action prompts only if carried into retained documentation, not automatically from diagnostic reasoning. Saving raw traces alone is not the trace-fed behavior change: that chain completes architecturally only through admission into code/documentation and later consumers.

### Routes

#### MEM-RTE-embedding-selection
Label: Optional embedding similarity selection

Endpoints: caller task string → `get_most_relevant_functions_via_embedding_similarity` → visible function descriptions/task embeddings → dot products → at most five function dictionaries returned. Owner: knowledge-base method; external embedding service supplies vectors. Distinct from model-mediated retrieval in [RT-RTE-native-task](runtime.md#rt-rte-native-task); uses [RT-CMP-embed](runtime.md#rt-cmp-embed), not a duplicate model component. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: all visible functions if fewer than five, otherwise top-five dot-product matches.
- Later read-back: uninspected — no shipped caller found in scoped Python call-site search; this is selection capability, not an established end-to-end agent route.
- Delegated visibility: embedding service gets function name plus docstring and task string; returned dictionaries include full source for a hypothetical caller.
- Selection predicate: current `get_functions` visibility followed by dot-product ranking; five-item budget, not a token budget.
- Invalidation or expiry: process-local `_embed_cache` is keyed by exact input string; changed text yields a different key, while old vectors have no explicit eviction in this method/file.
- Activation or effect: selection can choose library entries; no demonstrated action influence through this API.
- Evidence limits: numerical representation comes from external alias endpoint; no persisted vector index or actual consumer activation established.

> scores = np.dot(function_embeddings, task_embedding)
>         # choose top 5 scores
>         top5 = np.argsort(scores)[-5:]
>         best_matches = [fns[i] for i in top5]
>         return best_matches
> --- `skillweaver/knowledge_base/knowledge_base.py`

The cache is derived numerical access material, not skill content or changed provider weights. Parameter fixity and alias limits are in [RT-CMP-embed](runtime.md#rt-cmp-embed). This API performs request-directed selection, not independent unsolicited memory injection.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Write lineage is task/selected trajectory → synthesis prompt → candidate functions/docstrings → retry feedback → AST merge → checkpoint → later retrieval/execution. In the native builder, initial task acquisition includes current website state and possibly prior skills; resulting experience therefore has mixed browser, model and retained-code origins. The prompt asks for generalization and documentation, not verbatim transcript retention. Existing source is filtered to tested functions, the named test target or explicitly supplied additional-used names; the builder call supplies no additional-used list. This can withhold an untested function used during exploration from source context despite its call appearing in the trajectory. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/explore.py`.

Authorship is model synthesis; automatic caller success judgment triggers it. No per-candidate human approval is wired in this branch. Checker feedback is criticism of code constraints, not an independent website-outcome oracle. As the runtime notes, retry exhaustion is not a final veto. Replacement resets test count but retained code is immediately available to native module assembly; the visibility reset is not executable revocation. A prior checkpoint can be selected by a future caller, but neither automatic rollback nor best-checkpoint promotion is established. Diagnostics preserve reasons separately; ordinary reload does not restore them as model context ([MEM-OBJ-traces](#mem-obj-traces)).

#### On [RT-RTE-native-task](runtime.md#rt-rte-native-task)

Read-back is task-request-directed, not unsolicited push. Production tasks always request relevance selection; exploration/test can use the caller's fallback mode. The relevance model gets all currently visible pretty descriptions and the task; its selected names are matched against available entries, unknown names are dropped, and matched signatures/docstrings become the action-model library string. There is no explicit count/token budget in `retrieve`; selection quality is not guaranteed. In fallback testing, only verified functions plus the target are displayed; fallback exploration displays all visible functions. Reference-only fallback can display bodies, but retrieval itself still returns the pretty display. SRC-1, `skillweaver/create_skill_library_prompt.py`, `skillweaver/knowledge_base/knowledge_base.py`.

> if function is not None:
>                 fns_string += format_function_as_pretty_string(function)
>                 valid_functions.append(function)
> --- `skillweaver/knowledge_base/knowledge_base.py`

Selection happens once before the task loop. A fresh prompt at each action uses current screenshot/tree/title/URL and formatted earlier actions, not old screenshots or intermediate trees. `State.get_axtree_string` first filters out-of-view nodes. Action exception text is shortened to the first five lines. These are code-owned context filters; prior full state remains on disk rather than in a summary. No explicit aggregate history token budget or automatic history compaction appears in the inspected formatter. Task-local state/action lists and disabled names start empty; returned states/actions escape to the builder, while its shared library outlives the frame. This resembles a task frame with selected arguments and a returned trace, not a reference-tracked context heap. Provider-side context handling remains opaque. SRC-1, `skillweaver/attempt_task.py`, `skillweaver/agent.py`, `skillweaver/environment/state.py`.

#### On [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice)

The syntactic named-call plus result-field shortcut increments access/scheduling metadata without rewriting skill bodies. It checks source occurrence and recorded absence of exceptions/recovery attempts, not dynamic execution of the named function. A passing shortcut can therefore mark an unexecuted skill as tested; later filtering and practice still consume that counter. Attempts not passing the shortcut can trigger synthesis only after model success judgment; a negative judgment still leaves raw artifacts and a checkpoint, not an automatic corrective skill revision. That is narrower than the template's general advice about documenting unsuccessful uses. Each iteration checkpoint contains the shared library at save time, not just that worker's contribution; selection/admission are lock-protected but full attempts are not. Later iterations consume live shared changes, and later CLI invocations can load a caller-selected prefix. SRC-1, `skillweaver/explore.py`, `skillweaver/knowledge_base/knowledge_base.py`.

> load_knowledge_base(knowledge_base_path_prefix, discard_references=True)
> --- `skillweaver/explore.py`

This initialization preserves supplied code/semantic text and most metadata but deliberately clears reference lists; events remain. Neither user initiation nor file loading establishes per-content human approval. Trace-fed synthesis is wired into later behavior-shaping storage, but observed use, improved capacity and causal benefit remain unestablished.

#### On [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery)

A library function that triggers recovery is appended to a task-local disabled-name list. This is transient guidance/checker input for subsequent generated actions, not deletion or durable withdrawal of the stored function. Immediate recovery uses an alternative locator; it does not patch `KnowledgeBase.code`. Successful recovery annotations can be rendered into an expanded trajectory, but the builder's default serialization omits that insertion ([MEM-OBJ-traces](#mem-obj-traces)). Raw action diagnostics still preserve recovery data; an automatic read-back of those raw diagnostics into synthesis is not wired in the inspected builder. SRC-1, `skillweaver/environment/patches.py`, `skillweaver/agent.py`, `skillweaver/explore.py`.

> disabled_function_names.append(error_function_name)
> --- `skillweaver/environment/patches.py`

#### On [RT-RTE-browser-use](runtime.md#rt-rte-browser-use)

The adapter reloads a saved prefix and explicitly requests retrieval, then passes selected names to controller construction. Controller construction parses all functions ignoring verification visibility, asserts that selected names exist, executes library code to capture the requested functions, and registers selected wrappers with docstrings. Its memory result is executable callbacks plus interpretive descriptions, not a transferred transcript. The selected-name controller boundary differs from native full-library module availability; execution of library code while constructing callbacks still prevents treating selection as a sandbox. Exact downstream prompt budget, dialogue retention and callback activation remain uninspected beyond the external `Agent.run` handoff. SRC-1, `skillweaver/attempt_task_browser_use.py`, `skillweaver/knowledge_base/knowledge_base.py`; the supporting execution passages are in the supplied record.

#### On [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)

Supplied runtime evidence establishes per-task reload and output score retention, subject to its clean-source entry defects. It does not establish score-fed skill updates, automatic score-based withdrawal or a benchmark-result consumer that modifies the library. Retained scores and existing-task skipping are evaluation/cache behavior, not a demonstrated improvement loop. This annotation relies on the supplied record rather than a new evaluator audit (SRC-1, `skillweaver/evaluation/evaluate_benchmark.py`, `skillweaver/evaluation/evaluate_single_task.py`).

## Write side

The automatic content-admission mechanism is [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission): modeled success plus bounded checker repair leads to function merge. [MEM-OBJ-code](#mem-obj-code) and [MEM-OBJ-docstring](#mem-obj-docstring) share that admission but differ at consumption. Candidate reasoning/checker feedback remains in [MEM-OBJ-traces](#mem-obj-traces), not in ordinary reloaded memory unless documentation incorporates it. Save/load performs physical persistence, not independent approval. Model judgments, software predicates and caller initialization must not be conflated with human curation.

[MEM-OBJ-metadata](#mem-obj-metadata) has distinct write controls: automatic shortcut-driven increments labeled `exception_free_test`, merge-driven resets, supplied JSON, and an exposed blanket marking method. The automatic label records the syntactic named-call/result-field predicate, not proof of exercised skill use. Clearing references is explicit initialization cleanup; no inferred loss of every event or skill body follows. Missing metadata and missing semantic text have loader defaults, but arbitrary initialization provenance remains unresolved. [MEM-OBJ-semantic-knowledge](#mem-obj-semantic-knowledge) is passed through rather than automatically learned by the inspected update.

Rejection and withdrawal are limited. Checker violations cause retries, not guaranteed final rejection. Negative success judgments do not enter the synthesis branch. Replacement supersedes same-name code; omission does not delete old names. Recovery disables names within a task but does not persist revocation. No automatic rollback to an earlier checkpoint is shown by these inspected paths. These are local boundaries on the concrete mechanisms, not claims that an external caller cannot edit or replace files.

## Read-back

The concrete routes are the native prompt/execution path, live shared-library use by later builder iterations, caller-selected save/reload for later tasks, and Browser-Use callback registration. Their consumers and force are supplied by [RT-BAP-library-execution](runtime.md#rt-bap-library-execution) and the route annotations. Documentation influences model choices; bodies execute when invoked; counters affect visibility, inclusion and practice scheduling even though automatic increments do not establish dynamic skill execution; semantic text informs proposals and synthesis. Delivery alone establishes neither invocation nor benefit.

Optional embedding selection and tool-schema exports are available APIs without established shipped downstream consumers. Raw artifact reconstruction is similarly an offered reload capability, not proof that a future agent receives the retained full trace. No autonomous unsolicited memory-push route is inferred: even code-injected skill guidance follows caller task/retrieval operations. Native current-observation replacement and separate specialist model calls control working context without generating a durable summary.

## Integration issues

1. The prior memory report's “error-free named call” interpretation is corrected in Core ideas, [MEM-OBJ-metadata](#mem-obj-metadata), the practice annotation and write/read-back descriptions. Direct reinspection of SRC-1, `skillweaver/attempt_task.py` and `skillweaver/explore.py` confirms source occurrence plus result-field checks, not dynamic execution. [EPI-RTE-test-check](epistemic.md#epi-rte-test-check) supplies the passages and countercase; [EPI-RTE-tested-label](epistemic.md#epi-rte-tested-label) confirms that visibility, synthesis inclusion and scheduling authority remain real despite that evidential limit. These peer routes concern operations on the metadata object, not duplicate object declarations. The corrected supplied runtime already retains the same distinction. The report also refines the runtime's recovery caveat: the native attempt initially writes expanded recovery-aware text, but exploration overwrites that file and feeds the default representation to success/synthesis. Raw JSON still survives. This concerns [MEM-OBJ-traces](#mem-obj-traces), [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery) and [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice); it prevents treating saved filename identity as evidence that recovery details reached synthesis (SRC-1, `skillweaver/attempt_task.py`, `skillweaver/explore.py`).
2. No possible duplicate declaration identified after comparison: new objects are operative inputs/results of supplied routes, and [MEM-RTE-embedding-selection](#mem-rte-embedding-selection) is an alternative API, not [RT-RTE-native-task](runtime.md#rt-rte-native-task). The optional numerical cache remains covered by supplied [RT-CMP-embed](runtime.md#rt-cmp-embed).
3. Initial library/text provenance and approval are unresolved for arbitrary loaded prefixes; the shipped sample's usage logs do not supply original traces. This concerns [MEM-OBJ-code](#mem-obj-code), [MEM-OBJ-docstring](#mem-obj-docstring) and [MEM-OBJ-semantic-knowledge](#mem-obj-semantic-knowledge), and prevents attributing all initial content to autonomous practice (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillnet/map/map_kb_post_code.py`). Known subsequent transformations remain supported.
4. Ultimate users of exported tool schemas, blanket test marking and embedding selection are not established by the scoped Python search. APIs establish capability only; they cannot be upgraded to activated consumer routes. See [MEM-OBJ-metadata](#mem-obj-metadata), [MEM-OBJ-docstring](#mem-obj-docstring), [MEM-RTE-embedding-selection](#mem-rte-embedding-selection) (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`).
5. The metadata-free loader constructs only a partial metadata shape, and `copy` aliases its dictionary. Without exercising consumers this report does not establish all compatibility/failure consequences; it does establish that fallback initialization is not verification and copy is not isolated metadata rollback. This limits [MEM-OBJ-metadata](#mem-obj-metadata), not the known normal save/reload representation (SRC-1, `skillweaver/knowledge_base/knowledge_base.py`).

## Limitations and checks

The source boundary and supplied run identity were rechecked. This analysis used the supplied memory type, worker rules and records contract; no other source, prior analysis or live target execution was used. Direct inspection and supplied-only coverage are distinguished above. Call-site searches were bounded to frozen `skillweaver/**/*.py`; they do not prove absent external callers. All skill bodies, evaluator details and external host/provider implementations were not audited. No observed activation, successful generalization, reliable documentation, complete lineage or causal improvement is established.

Deterministic validation: completed successfully with the invocation's `commonplace-run validate-output` command. This checks output form, identities, references and quotation occurrence, not semantic correctness or exercised behavior.
