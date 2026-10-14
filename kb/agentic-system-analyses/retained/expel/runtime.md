---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ExpeL runtime baseline tracing benchmark acting, reflection, insight admission and evaluation at the frozen Git revision."
run-id: AAS-2026-10-14-expel-efd908f05069-01
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
---

# ExpeL runtime report

## Runtime account

This is a static, code-grounded account of SRC-1 at the boundary's reviewed commit. No execution trace, generated rule set, checkpoint corpus or causal comparison was supplied. Wiring is inspectable; successful operation, behavioral activation and benefit are unobserved. Additional inspection covers the complete acting and reflection classes, the material `ExpelAgent` training, extraction, retrieval and rule-parser bodies, all three drivers, provider wrapper, embedding dispatch, persistence helpers and benchmark action adapters. These supply implementation evidence; prompts and configuration supply doctrine/design evidence (SRC-1: `agent/react.py`, `agent/reflect.py`, `agent/expel.py`, `train.py`, `insight_extraction.py`, `eval.py`, `models/llm.py`, `memory/__init__.py`, `utils.py`, `envs/hotpotqa/hotpotqa.py`, `envs/fever/fever.py`, `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py`). This is not a branch-correctness certification.

### Ordinary shipped invocation

The shipped loop has three entry paths, not one always-on learner. Hydra supplies benchmark, task list, agent class, prompts, model and retrieval settings. `train.py` constructs the agent, optionally restores the last saved dictionary, and repeatedly calls training mode. The foreground driver owns task scheduling; the agent owns action progression and retry state. The model proposes text, a benchmark parser produces an action, and a Python adapter executes it. Training invokes `ReflectAgent`; failed attempts can produce a separate reflection-model invocation before another attempt. `ExpelAgent.next_task` classifies and retains trajectories, then the driver snapshots selected attributes. The output is logs, serialized state and aggregate result summaries, not a returned answer object ([RT-RTE-training-loop](#rt-rte-training-loop); SRC-1: `train.py`, `agent/expel.py`, `agent/react.py`, `agent/reflect.py`).

`insight_extraction.py` reloads training state and computes training IDs by subtracting each evaluation fold's task IDs before calling `create_rules`. The compare branch resolves those IDs through `idx2task`; the success-group branch instead tests dictionary enumeration positions against them. Effective held-out-task exclusion in that branch requires the success-history insertion order to match task-index order, which restored dictionaries need not preserve. Resumed success extraction reuses saved groups rather than reselecting them. No actual leakage is established. Each critique call receives existing rules plus either a successful/failed pair or a group of successful trials. Model output requests symbolic operations on natural-language rule units. Software parses and applies them without per-rule human approval. Intermediate and final checkpoints support subsequent extraction or evaluation ([RT-RTE-rule-admission](#rt-rte-rule-admission); SRC-1: `insight_extraction.py`, `agent/expel.py`, `prompts/templates/human.py`).

`eval.py` restores retained state but excludes many current-run and configuration fields. It switches the agent to evaluation mode, supplies `no_rules`, and either creates fold rules or loads cached rules. Evaluation calls `ReactAgent.run`, not the training reflection loop. At acting calls, retrieval selects successful trajectories and shipped examples, then replaces the old fewshot text in the accumulated prompt. Rules are inserted before the task unless disabled. Results and state are saved after each evaluated task ([RT-RTE-evaluation-context](#rt-rte-evaluation-context); SRC-1: `eval.py`, `agent/expel.py`).

The decision-generating and embedding components are separately recorded in [RT-CMP-gpt-wrapper](#rt-cmp-gpt-wrapper) and [RT-CMP-embedder](#rt-cmp-embedder). No inspected route fine-tunes their parameters; retained text changes independently of model weights. Provider names and embedding model names are not immutable weight identities.

### Effect boundaries and controls

The action capability surface is benchmark-specific. HotpotQA permits Search, Lookup and Finish; Finish compares the proposed answer with the supplied key using `EM`. FEVER forwards parsed actions to the Wikipedia wrapper and treats reward 1 as success. ALFWorld forwards actions to an external environment and reads `info['won'][0]`. WebShop changes session/page state and fetches server content; Buy Now terminates the benchmark session. This is not evidence of purchasing on a real commerce service. Actual grants consist of the selected adapter, configured service/data access and provider credential; deployment isolation and external service permissions are uninspected. The Python process also reads and writes local checkpoint files. The benchmark action grammar is not a sandbox for the enclosing process (SRC-1: `envs/hotpotqa/hotpotqa.py`, `envs/fever/fever.py`, `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py`, `utils.py`).

All inspected acting, reflection and critique model calls use the wrapper, except testing branches which obtain response text from `input()`. There is no provider-native tool execution in these inspected call sites: text is interpreted by repository code. This bounded observation does not certify arbitrary imported libraries or a customized caller. Direct `ReactAgent.run` and the evaluation branch materially bypass training reflection and trajectory admission; directly loading checkpoints also changes agent fields without critique. No sub-agent or remote-worker handoff participates in these inspected loops. External adapters and model services return observations/responses rather than assuming task scheduling (SRC-1: `agent/react.py`, `agent/reflect.py`, `agent/expel.py`, `models/llm.py`).

Checkpoint loading trusts local pickle content, then uses `setattr` for fields outside each driver's exclusion list. File overwrite confirmation is a run-level human decision, not approval of each retained trajectory or insight. Persistence writes files separately and supplies no inspected transactional rollback. Resume markers provide recovery affordances; crash-consistent restoration and exact replay remain unobserved ([RT-RTE-checkpoint-restore](#rt-rte-checkpoint-restore); SRC-1: `utils.py`, `agent/react.py`, `train.py`, `eval.py`, `insight_extraction.py`). Product code, prompts, model configuration and environment implementations are supplied by installed files/configuration; the inspected runtime's automatic change path revises retained rules, not those files.

### Forcing cases and guarantee coverage

1. **Training versus evaluation:** the explicit mode dispatch defeats a claim that every attempt reflects or admits new trajectories. Evaluation goes directly to ReAct, while training uses reflection. Retrieval is also skipped while `self.training` is true (SRC-1: `agent/expel.py`).
2. **Over-limit or malformed rule proposals:** parser checks formatting, terminal punctuation and some duplicate/index conditions. The updater does not enforce the prompt's four-operation limit, one-operation-per-existing-rule limit, semantic generality or a hard `max_num_rules` cap. The configured maximum affects prompting and removal strength. These are policy requests, not invariants; malformed index edge cases are not certified safe (SRC-1: `agent/expel.py`, `prompts/templates/human.py`).
3. **Context/error fallback:** ordinary acting falls back to `gpt-3.5-turbo-16k` after `InvalidRequestError`, with an interactive acknowledgment unless previously passed. Reflection and critique fall back without that acknowledgment. The provider wrapper retries rate limits six times; QA search retries arbitrary exceptions indefinitely. Thus turn/step limits do not give a wall-clock completion guarantee (SRC-1: `agent/react.py`, `agent/reflect.py`, `agent/expel.py`, `models/llm.py`, `envs/hotpotqa/hotpotqa.py`).
4. **Rules bypass and cached state:** `no_rules` suppresses rule insertion and fold extraction; cache loading formats stored rules without re-evaluating their content. Retrieval can still deliver examples. A missing cache key yields an empty list, not fresh extraction. Knowledge quality is not enforced by either path (SRC-1: `eval.py`, `agent/expel.py`).

The loop-limit owner is Python agent/environment code. Enforcement is `ReactAgent.run`'s termination/truncation predicate, `BaseAgent.is_truncated`'s token check and adapter step counting. Guarantee strength: best effort for bounded completed interaction, not total termination. Covered paths: ordinary training/evaluation ReAct loops; alternates: thoughts and external retries can consume time before the next predicate, and direct step/model invocations do not inherit a run-loop budget. Required external contract: model/service calls must return and token accounting/parsers must operate. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1: `agent/react.py`, `agent/base.py`, `envs/base.py`, `models/llm.py`, `envs/hotpotqa/hotpotqa.py`).

Rule-format enforcement belongs to `parse_rules` and `update_rules`, not the critic model. Its strength is a protocol for recognized operations plus best-effort filtering, not a truth guarantee. It covers `create_rules` output; checkpoint restoration and cache loading bypass it. The semantic policy owner is the prompt author/model, with no inspected independent correctness veto. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1: `agent/expel.py`, `prompts/templates/human.py`, `agent/react.py`).

Working context is controlled by Python task reset, reflection scratchpad truncation, mode-specific rule insertion and retrieval replacement. Task reset discards the acting frame; selected reflections cross into a retry, while retained training trajectories remain externally reachable through retrieval. Reflection replaces longest trial lines with their prefix plus `...` until its token target is met. Fewshot replacement removes old examples by string matching and injects selected ones; collapse of adjacent messages is concatenation, not semantic summarization. This resembles a per-task frame with selected values escaping, but there are no live references in the model window. Exact substitution success and budget sufficiency are unobserved; token filtering bounds individual selected trajectories, not all message content (SRC-1: `agent/react.py`, `agent/reflect.py`, `agent/expel.py`).

## Shared records

### Components

#### RT-CMP-gpt-wrapper
Label: GPTWrapper acting and critique model

Source-native identity: `GPTWrapper`, built through `LLM_CLS`. Representational form: distributed-parametric external model; input/output messages are natural language, separate from weights. Storage substrate: provider-managed parameters, opaque to this repository. The default is `gpt-3.5-turbo`; long-context construction substitutes `gpt-3.5-turbo-16k`. Parameters are not updated by inspected routes. Exact weight/version is not pinned. A mutable provider endpoint can resolve to a changed model; provider internals and retention are uninspected. Temperature zero is a request, not deterministic output evidence (SRC-1: `models/llm.py`, `configs/agent/expel.yaml`).

> if long_ver:
>     llm_name = 'gpt-3.5-turbo-16k'
> --- `models/llm.py`

#### RT-CMP-embedder
Label: ExpelAgent embedder

Source-native identity: `self.embedder`, instantiated with `embedder_path`. Representational form: distributed-parametric embedding model and dense numerical representations. Storage substrate: dependency-managed weights or provider endpoint; vectors reside in in-process FAISS stores constructed from documents. Default `all-mpnet-base-v2` uses HuggingFace embeddings. Dispatch also affords OpenAI, LlamaCpp and GPT4All alternatives. No parameter-training operation is wired here; exact weights are not pinned. Remote alternatives can resolve to a changed provider model, and local named artifacts have no inspected immutable revision guarantee. Embedding provenance and dependency behavior remain uninspected (SRC-1: `memory/__init__.py`, `agent/expel.py`, `configs/agent/expel.yaml`).

> self.embedder = embedder(model_name=embedder_path)
> --- `agent/expel.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-training-loop
Label: Training acting and reflection loop

Endpoints: `train.py` task driver → `ExpelAgent.run('train')` → reflection/ReAct → benchmark adapter → `next_task` → checkpoint writer. Owner: driver schedules tasks; code schedules trials; model selects thought/action text and proposes retry reflections. Context: task, shipped instructions/examples, accumulated observations and formatted prior reflections. State: task index, reflection counter, previous trial, prompt histories, reward and retained success/failure dictionaries. Effects: benchmark action execution and later state admission. This is a bounded benchmark curriculum, not an open-ended autonomous problem selector (SRC-1: `train.py`, `agent/react.py`, `agent/reflect.py`, `agent/expel.py`).

- Immediate return: Agent run returns no answer value; observations, final response text and reward remain in agent/environment state, then appear in logs.
- Later read-back: Training trajectories and past reflections enter saved dictionaries; later extraction and evaluation reload them.
- Delegated visibility: inapplicable — no delegated worker; reflection uses a separate model prompt assembled from the same task's trial.
- Selection predicate: Failure and available reflection depth trigger retry reflection; success or maximum reflection depth permits advancing the task.
- Invalidation or expiry: Acting history resets for each attempt; reflections clear when moving tasks; retained histories survive through checkpoint reload.
- Activation or effect: Parsed actions are passed to the adapter; reflection text is inserted into retry prompts. Changed behavior due to that text is unobserved.
- Evidence limits: Static control flow only; external execution, actual reflections and outcome quality are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Diagnosis roles: the model proposes a reflection; code chooses whether to retry and whether the task is successful. Humans provide configuration/problems and can supply response text in testing mode; ordinary content admission is computational. Answer oracles: QA uses the supplied answer key/EM, FEVER reward comes from its wrapper, ALFWorld uses simulator win, WebShop uses server reward equal to 1. These signals classify experience; they do not independently assess reflection correctness. Improvement trigger: failed attempt. Guidance: shipped reflection instructions/examples ask for a new plan based on prior failure. What persists: reflections and input/outcome trajectories. Recovery: driver reloads saved attributes; exact external environment replay is uninspected (SRC-1: `agent/reflect.py`, `agent/expel.py`, `train.py`, `envs/hotpotqa/hotpotqa.py`, `envs/fever/fever.py`, `envs/alfworld/alfworld.py`, `envs/webshop/webshop.py`).

> if self.perform_reflection and not self.is_success():
>     self.reflect()
> ReactAgent.run(self, reset)
> --- `agent/reflect.py`

Theory scope: reflection is requested natural-language diagnosis of the agent's trial, not observed formulated criticism. Theory-builder conditions 1–4: condition 1 afforded — whole reflection text is retained, but its actual theoretical content is uninspected; condition 2 afforded — text reaches the acting model, dependence on its content is unobserved; condition 3 claimed — prompts request failure-sensitive revision, but no generated criticism/blame assignment is supplied; condition 4 wired — retained reflections enter subsequent retries. Addressability: whole reflection units are inspectable, with no inspected operation targeting individual assumptions. Persistence horizon: retries on one task, with saved reflections available across runs. Learning: claimed, not demonstrated improved future capacity. Reflection: wired self-representation of trials and a feedback delivery path, with actual representation-mediated behavior unobserved. Reflective theory builder: uninspected — no evidence that method texts themselves are criticized and revised. Autonomous theory builder: afforded computational trial/diagnosis/retry roles, but actual theory production and content-directed criticism remain uninspected. None of these fields establishes exercised self-improvement.

#### RT-RTE-rule-admission
Label: Trace-fed insight extraction and rule admission

Endpoints: extraction driver or evaluation fold → `create_rules` → critique model → parser/updater → numbered rule text/cache/checkpoint. Owner: driver selects fold training IDs; model proposes operations; Python determines accepted syntactic operations and counter-based retention. Representational policy: natural-language prompts and rules interpreted by models, with symbolic operation types/indices/counters controlling updates. Context is existing rules plus selected successful/failed trajectories, not the complete acting conversation (SRC-1: `insight_extraction.py`, `eval.py`, `agent/expel.py`, `prompts/templates/human.py`).

- Immediate return: `create_rules` returns critique logs and changes rule fields; cached-load mode sets formatted rules and returns without critique.
- Later read-back: Current rules shape subsequent critique prompts; cache/checkpoint rules can reach later evaluation model inputs.
- Delegated visibility: inapplicable — critic calls are synchronous model invocations, not independently scheduled workers.
- Selection predicate: Drivers subtract held-out fold IDs to obtain training IDs. Compare inputs resolve each training ID through `idx2task`. Success groups select first successful trajectories by dictionary enumeration position in `training_ids`, not task identity; effective held-out-task exclusion there requires insertion-order/task-index alignment. Resumed success extraction reuses saved groups.
- Invalidation or expiry: Fresh extraction clears the working rule pool; resumed extraction continues saved state; nonpositive counters remove rules; no time-based expiry is inspected.
- Activation or effect: Parsed operations change the rule pool and later prompts; actual changes in task behavior and quality remain unobserved.
- Evidence limits: No generated rules or content-specific critiques supplied; symbolic admission does not establish truth, generality or beneficial learning. Success-history insertion order and saved-group provenance are unobserved, so effective holdout is not established for every extraction input; no actual leakage is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger and proposal: curriculum traces prompt ADD/EDIT/REMOVE/AGREE operations. Software can reject malformed/duplicate operations, decrement counters and remove nonpositive rules; no separate human per-content veto or held-out validation gate is wired before admission. Run-level overwrite confirmation does not supply one. Oracle: stored benchmark success/failure classifications select inputs; no independent rule oracle. Operating mode: bounded fold extraction and evaluation, not arbitrary production adaptation. Guidance requests general, high-level tips for better Thought and Action and requests semantic criticism of duplication, contradiction and insufficient generality. The evolving rule text and counters persist, while logs preserve inputs and requested operations; later acting reads rules, not necessarily that rationale. Rollback: old checkpoint files can be loaded by a caller, but there is no inspected automatic semantic rollback on task regression (SRC-1: `agent/expel.py`, `prompts/templates/human.py`, `insight_extraction.py`, `eval.py`).

> training_ids = set(range(num_training_tasks)) - set(eval_idxs)
> --- `insight_extraction.py`

> training_task = self.idx2task[training_id]
> --- `agent/expel.py`

> for idx, task in enumerate(self.succeeded_trial_history):
>     if idx in training_ids and len(self.succeeded_trial_history[task]) > 0:
>         all_success.append((task, self.succeeded_trial_history[task][0].trajectory))
> --- `agent/expel.py`

> all_success = loaded_dict['critique_summary_all_success']
> --- `agent/expel.py`

> parsed_operations = parse_rules(llm_output)
> --- `agent/expel.py`

> self.rule_items_with_count = update_rules(self.rule_items_with_count, parsed_operations, list_full = self.max_num_rules+5 <= len(self.rule_items_with_count))
> --- `agent/expel.py`

> rules = [rules[i] for i in range(len(rules)) if rules[i][1] > 0] # remove rules when counter reach 0
> rules.sort(key=lambda x: x[1], reverse=True)
> --- `agent/expel.py`

Theory account: localized prose rules can carry general claims, but no actual rule payload is supplied to establish that every retained tip is a theory. Critique applies shipped method guidance to trial evidence and existing rule content; the method guidance is not itself updated. Theory-builder conditions 1–4: condition 1 afforded — whole rule units are localized and revisable; condition 2 afforded — existing rule content is supplied to the critic and actor, without observed decision dependence; condition 3 claimed — the prompt requests content-directed criticism and revisions, but actual challenged claim/result/blame is unobserved; condition 4 wired — updater output becomes the next critique's existing rules. Addressability: rule-level text/index operations; assumptions and scope conditions are not separately parsed. Persistence: rounds of extraction and later task/run consumption through cache/checkpoints. Learning: source-directed improvement objective, but improved future capacity and attribution are uninspected. Reflection: wired feedback from represented agent trials to rule revisions and later acting inputs; behavior mediated by those representations is unobserved. Reflective theory builder: uninspected — method-text self-criticism is not established. Autonomous theory builder: afforded model/code proposal and admission roles, but generated theoretical criticism is uninspected. Self-improvement boundary: ExpeL including its retained instruction state, across extraction and later evaluation; objective is better benchmark task performance. This is a dispositional improvement-directed self-change pathway: trace evidence enters update determination, rules can change its context policy, and [RT-BAP-rules-acting](#rt-bap-rules-acting) can reach later behavior. Exercised causal dependence and successful improvement are not established.

#### RT-RTE-evaluation-context
Label: Evaluation and retrieved context selection

Endpoints: `eval.py` → cache or extraction → `ExpelAgent.run('eval')` → `ReactAgent.run` → prompt refresh → model → parser/adapter. Owner: driver selects evaluation indices; Python controls delivery and filtering; embedding similarity ranks candidates; actor selects actions. State: retained success histories, rules/cache, current task/history and rebuilt FAISS documents (SRC-1: `eval.py`, `agent/expel.py`).

- Immediate return: Agent returns no answer value; task outcome and success index remain in state and logs.
- Later read-back: Training experience and rules are consumed from reloaded state; evaluation checkpoints support resume. The run branch does not invoke training `next_task` trajectory admission.
- Delegated visibility: inapplicable — no worker handoff; provider sees assembled acting messages.
- Selection predicate: Strategy chooses task/thought/action/step keys, filters environment type and some WebShop trajectories, retrieves a buffered similarity set, optionally reranks, selects shortest trajectories, and skips over-budget, same-task and duplicate-task examples.
- Invalidation or expiry: Reset rebuilds the acting prompt; refresh replaces prior fewshot text. `no_rules` omits rules; `fewshot_strategy == 'none'` skips dynamic updates, not necessarily all shipped examples.
- Activation or effect: Selected prose reaches the acting prompt if replacement succeeds; action selection still depends on model interpretation. Behavioral activation is unobserved.
- Evidence limits: Retrieval quality, exact string replacement success, configured alternative-strategy correctness and downstream benefit are not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles and oracle: code selects context and the model proposes task actions; benchmark adapters judge task success, not relevance or truth of retrieved material. Mode: benchmark evaluation on driver-designated held-out fold IDs, with the success-group extraction qualification in [RT-RTE-rule-admission](#rt-rte-rule-admission). Retrieval independently builds its pool from the full restored success-history dictionary plus shipped examples, without filtering that pool by fold training IDs; it skips the current task, not every task in the evaluation fold. This is a separate exposure route, not evidence that it delivered any held-out trajectory in an actual run. This read route does not approve knowledge revisions; its optional extraction branch uses [RT-RTE-rule-admission](#rt-rte-rule-admission). Forcing exception: `reflection_similarity` appears in configuration comments/filter mapping but has no final strategy branch in the inspected dispatcher; it should not be assumed equivalent to supported strategies. Defaults select task similarity. The code uses FAISS directly despite storing a retriever class (SRC-1: `agent/expel.py`, `configs/agent/expel.yaml`).

> combined_history = dict(self.succeeded_trial_history)
> --- `agent/expel.py`

> if self.training or self.fewshot_strategy == 'none':
>     return
> --- `agent/expel.py`

> self.prompt_history[i] = message_type(content=history_message.content.replace(old_fewshots, new_fewshots))
> --- `agent/expel.py`

#### RT-RTE-checkpoint-restore
Label: Checkpoint persistence and restore

Endpoints: driver-selected agent dictionaries → local pickle/text files → `load_trajectories_log` → `load_checkpoint` attribute restoration. Owner: Python driver and caller configuration. State/effects: retained histories, rules, counters, indices and selected run state can be restored; runtime objects are reconstructed rather than wholly serialized. Form: symbolic Python containers plus contained natural-language text; storage: local files (SRC-1: `utils.py`, `agent/react.py`, `train.py`, `insight_extraction.py`, `eval.py`).

- Immediate return: Writer emits files; loader returns dictionaries/logs; checkpoint method sets attributes.
- Later read-back: Subsequent training, extraction and evaluation invocations load the last saved snapshot.
- Delegated visibility: inapplicable — local synchronous persistence, without delegated executor.
- Selection predicate: Drivers filter attributes by concrete type and use different exclusion lists during restoration; saved metadata controls resume positions.
- Invalidation or expiry: Files are overwritten for the configured run name; human confirmation protects some new-run overwrites. No automatic expiry is inspected.
- Activation or effect: Restored fields change subsequent prompts and control state; pickle loading requires trusted file provenance, and semantic validity is not rechecked by `load_checkpoint`.
- Evidence limits: No supplied checkpoint or recovery trace; external environment state is not shown to be faithfully replayed and writes are not shown atomic.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: the caller chooses paths and starts/resumes the workflow; software admits restored fields outside exclusion lists with no per-item content gate. Oracle: inapplicable — restoration uses no expected-answer check. Mode: restart/reuse. Proposed change: replacement of agent attributes from saved state. Rejection ability: exclusion lists prevent selected fields loading; no independent rule-truth rejection. Recovery: callers can choose another available snapshot/file, but no automated rollback is inspected. Guidance: current driver configuration supplies rebuilt objects and exclusion lists, not a new model critique (SRC-1: `agent/react.py`, `utils.py`, `eval.py`).

> with open(f'{path}/{run_name}.pkl', 'rb') as f:
>     out['dicts'] = pickle.load(f)
> --- `utils.py`

> setattr(self, k, v)
> --- `agent/react.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-rules-acting
Label: Retained rules to acting model

Consumer: acting `GPTWrapper` model. Channel: `rule_template` human message inserted before task in evaluation, subsequently merged with adjacent messages. Force: benchmark-specific natural-language guidance, not a symbolic action veto; FEVER says MANDATORY while other templates ask to use experiences as references. Horizon: evaluation tasks after extraction/cache load, including later processes via checkpoints. Delivery is wired, compliance and causal behavior change unobserved; `no_rules` bypasses the path (SRC-1: `agent/expel.py`, `prompts/templates/human.py`, `eval.py`).

> self.rule_template.format_messages(rules=self.rules)[0]
> --- `agent/expel.py`

#### RT-BAP-fewshots-acting
Label: Experience examples to acting model

Consumer: acting model. Channel: retrieved task/trajectory prose replacing fewshots in the acting prompt. Force: interpretive demonstration of actions and observations, not enforced commands. Horizon: subsequent model calls and later tasks/runs that load training history. Selection and delivery are covered by [RT-RTE-evaluation-context](#rt-rte-evaluation-context); actual influence is unobserved. The shortest trajectory selected for delivery need not be the same unit whose thought/step matched the query (SRC-1: `agent/expel.py`).

> fewshots.append(self.combined_history[fewshot_doc.metadata['task']][idx].task + '\n' + shortest_fewshot)
> --- `agent/expel.py`

## Annotations

none
