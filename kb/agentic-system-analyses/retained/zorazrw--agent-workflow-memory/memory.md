---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Agent Workflow Memory's text-file induction, trace admission, exemplar selection and optional episode scratchpad at the frozen commit."
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
source-identity: "https://github.com/zorazrw/agent-workflow-memory"
reviewed-boundary: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
---

# Agent Workflow Memory memory report

## Boundary and evidence

Agent Workflow Memory (AWM) retains web-task procedures as text, then supplies that text to a model choosing later actions. This report covers both shipped benchmark loops, offline and online induction, rule/manual admission, evaluator records, concrete exemplars, the optional retrieval CLI and the legacy episode scratchpad. It uses SRC-1 at commit **8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1**. The source register and external-dependency limits are supplied by [boundary](boundary.md#source-register). BrowserGym's internal trace storage, provider weights and downloaded benchmark inputs are not available evidence; their exclusion prevents host-internal, exact-model, input-quality and reproduced-performance conclusions.

The evidence is inspected implementation and prompt doctrine, not observed operation. Direct reads covered the paths in the table below; static website files were sampled at their first 30 lines, and the large exemplar JSON at its first 25 lines. Those samples establish retained content and format, not complete correctness, origin or induction history. Runtime findings supply the provider-component and basic-agent account; these are distinguished from direct reads. No source ID is added.

| Operation or retained surface | Source path, inspection | Coverage and conclusion limit |
|---|---|---|
| Mind2Web offline/online scheduling and initialization | `mind2web/pipeline.py`, `mind2web/run_mind2web.py`, direct complete reads | [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission); [MEM-OBJ-mind-workflows](#mem-obj-mind-workflows). The `action` mode explicitly raises `NotImplementedError`, so it is not a second working memory consumer. |
| Mind2Web induction, formatting and filtering | `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `mind2web/utils/data.py`, direct complete reads | [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission); annotations below distinguish annotated examples from model conversations and filtering from verification. |
| Mind2Web workflow/exemplar delivery and trace persistence | `mind2web/memory.py`, direct complete read; `mind2web/data/memory/exemplars.json`, sample | [MEM-OBJ-mind-workflows](#mem-obj-mind-workflows), [MEM-OBJ-exemplar-content](#mem-obj-exemplar-content), [MEM-OBJ-exemplar-specifier](#mem-obj-exemplar-specifier), [MEM-OBJ-conversation](#mem-obj-conversation). Static exemplars are a context source, not demonstrated use-produced read-back. |
| Both Mind2Web induction prompt variants | `mind2web/prompt/instruction_action.txt`, `mind2web/prompt/instruction_abstract.txt`, `mind2web/prompt/one_shot_action.txt`, `mind2web/prompt/one_shot_abstract.txt`, direct complete reads | [MEM-OBJ-mind-workflows](#mem-obj-mind-workflows). Request for abstraction does not establish compliant output. |
| Random/semantic workflows and concrete-example retrieval | `mind2web/workflow/retrieve.py`, direct complete read | [MEM-RTE-workflow-selection](#mem-rte-workflow-selection), [MEM-RTE-exemplar-ablation](#mem-rte-exemplar-ablation). Semantic workflow route has broken index handoff; ablation uses a different handoff and must be assessed separately. |
| WebArena pipeline, empty-file initialization and workflow consumption | `webarena/pipeline.py`, `webarena/run.py`, `webarena/agents/legacy/agent.py`, direct complete reads | [RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows). External experiment storage is not AWM-owned persistence. |
| Neural and rule/manual trace transformations | `webarena/induce_prompt.py`, `webarena/induce_rule.py`, direct complete reads | [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [MEM-OBJ-arena-traces](#mem-obj-arena-traces). Neural cleanup removes scroll/noop; rule cleanup does not. |
| Text/vision evaluation and retained judgments | `webarena/autoeval/evaluate_trajectory.py`, `webarena/autoeval/evaluator.py`, direct complete reads | [MEM-OBJ-autoeval-signal](#mem-obj-autoeval-signal), [MEM-OBJ-autoeval-thoughts](#mem-obj-autoeval-thoughts). No actual evaluator outputs supplied. |
| WebArena instruction, demonstration and five shipped website files | `webarena/prompt/instruction.txt`, `webarena/prompt/one_shot.txt`, complete; `webarena/workflow/gitlab.txt`, `webarena/workflow/map.txt`, `webarena/workflow/reddit.txt`, `webarena/workflow/shopping.txt`, `webarena/workflow/shopping_admin.txt`, samples | [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows). Shipped examples include concrete query/thought/action text; their origin and approval history are unresolved. |
| Episode scratchpad and context shrinking | `webarena/agents/legacy/dynamic_prompting.py`, scoped direct reads of MainPrompt, Memory, HistoryStep, History and fit_tokens | [MEM-RTE-episode-memory](#mem-rte-episode-memory), [RT-CLM-context-budget](runtime.md#rt-clm-context-budget). Not an exhaustive dynamic-prompt helper audit. |
| Providers, embeddings, auxiliary basic caller and score aggregation | Supplied runtime records and boundary account, not independently audited here | [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client), [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings), [RT-RTE-basic-action](runtime.md#rt-rte-basic-action). Basic caller is not a workflow-memory route; aggregate metrics are reporting, not a demonstrated admission consumer. |

## Core ideas

1. **A workflow file is context, not an executable workflow graph.** Mind2Web supplies it as a user exemplar; WebArena appends it to the system message. The consumer model interprets action-like text; there is no inspected dispatch by workflow name. Delivery and possible influence are established, compliance and benefit are not ([RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar), [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system); SRC-1, `mind2web/memory.py`, `webarena/agents/legacy/agent.py`).
2. **Trace trust is route-specific.** Offline Mind2Web starts from annotated examples; its online route takes predictions without a success gate. WebArena takes a model success Boolean or external reward before induction, while manual rule mode adds a human veto. These admission mechanisms do not test the resulting abstract procedure ([RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)).
3. **Replacement is regeneration, not cumulative editing of the prior workflow.** Writers overwrite files; old workflow text is not their explicit prompt input. Previously consumed workflows can still affect source traces indirectly. Localized examples and procedures remain readable, but generated workflow files do not carry a structured source-to-procedure map or admission rationale. Concrete rule outputs preserve selected thoughts instead of inducing new abstraction ([MEM-OBJ-mind-workflows](#mem-obj-mind-workflows), [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows); SRC-1, `mind2web/online_induction.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`).
4. **Selection differs from supply.** Default consumers request a configured file and supply all its text, subject to Mind2Web omission on token limits. That is not task-targeted workflow retrieval or an independent unsolicited push. Optional retrieval preprocesses a file; WebArena's workflow addition bypasses the main-prompt token fit ([MEM-RTE-workflow-selection](#mem-rte-workflow-selection), [RT-CLM-context-budget](runtime.md#rt-clm-context-budget)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-mind-workflows
Label: Mind2Web workflow text

Source-native identity: induction output at `args.output_path` or website text file under `args.output_dir`; source substrate is local plaintext. Natural-language procedure descriptions and action notation are interpreted by the prediction model, not directly executed. Distinct retained output of [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), not a duplicate of its transformation route; runtime declares no corresponding object.

Lineage: offline annotated training action representations or online saved prediction inputs/outputs → fixed instruction and one-shot → provider output → `filter_workflows` → text overwrite. The action and abstract prompts request different degrees of substitution; examples expose scope conditions such as being on a flight booking page. Authorship is model-generated; software admits after textual filtering, while an operator selects tags/mode/paths. Starting induction and choosing a split are not per-content approval. Read-back is `get_exemplars` at later samples, with user-exemplar authority, and possible omission on budget. Training inputs and actual outputs are not supplied; model reasoning and output compliance remain uninspected (SRC-1, `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `mind2web/memory.py`, `mind2web/prompt/one_shot_abstract.txt`).

> blocks = [b for b in blocks if "delta" not in b.lower()]
> return '\n\n'.join(blocks)
> --- `mind2web/utils/data.py`

The filter can remove any block containing “delta”, not just a demonstration header. It is a textual curation rule, not a correctness check. Whole-file replacement has no built-in version history in these writers; historical reconstruction from external files is unresolved.

#### MEM-OBJ-exemplar-content
Label: Concrete exemplar message content

Source-native identity: `content` and `role` entries in `mind2web/data/memory/exemplars.json`. Local JSON holds natural-language tasks, textual HTML observations and action examples; roles are symbolic message-delivery metadata, not learned weights. This is the concrete context source of [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action), distinct from the route and induced workflow output. Its initial author, extraction history and approval control are not established by the sampled JSON or consumer. Known subsequent transformation: random selection after tag filtering, removal of specifiers and sequential token-budget admission. Consumer: prediction model, user/assistant demonstration channel, later samples; static shipment alone is not trace-fed read-back (SRC-1, `mind2web/data/memory/exemplars.json`, `mind2web/memory.py`).

> memory += random.sample(concrete_examples,
>         min(args.retrieve_top_k, len(concrete_examples)))
> memory = [[{k:v for k,v in m.items() if k!="specifier"} for m in e] for e in memory]
> return memory
> --- `mind2web/memory.py`

#### MEM-OBJ-exemplar-specifier
Label: Exemplar selector metadata

Source-native identity: `specifier` fields in the same local JSON. These readable website/domain/subdomain/task strings operate as symbolic selector inputs under substring tests, separate from the delivered demonstration content. Initial metadata provenance and human admission are unresolved. `get_exemplars` uses the first message's specifier to filter candidate exemplars, then removes all specifiers before model delivery. The ablation route embeds the first specifier instead and maps its index back to the full message contents. Distinct metadata part of the exemplar source associated with [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action); runtime has no object counterpart (SRC-1, `mind2web/memory.py`, `mind2web/workflow/retrieve.py`).

> texts = [ex[0]["specifier"] for ex in train_examples]
> memory = FAISS.from_texts(texts=texts, embedding=embedding, metadatas=metadatas)
> --- `mind2web/workflow/retrieve.py`

#### MEM-OBJ-conversation
Label: Mind2Web saved conversations

Source-native identity: per-task JSON `conversation` emitted by `eval_sample`. Local JSON container separates natural-language model inputs/outputs from symbolic predicted/target actions, token statistics and accuracy arrays. The input can already contain workflow/exemplar text and annotated prior actions. This is a raw prediction record, not browser-execution experience. Producer software automatically persists it without per-content approval; default file name is the driver task index. Online induction selects only input/output dictionaries, then only the last input message plus the output, discarding metrics, targets, earlier messages and explicit success evidence. Thus failed context-limit records can still qualify as input/output examples. Distinct output/input object joining [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action) and [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), not identical to either route (SRC-1, `mind2web/memory.py`, `mind2web/online_induction.py`).

> step = {
>             "env": "# " + item["input"][-1]["content"],
>             "action": item["output"],
>         }
> trajectory.append(step)
> --- `mind2web/online_induction.py`

The later update consumer receives a lossy projection, not the whole saved conversation. The unsorted directory-to-sample zip leaves task attribution unresolved, even though physical files persist.

#### MEM-OBJ-arena-workflows
Label: WebArena workflow text

Source-native identity: text read from `flags.workflow_path`, including shipped `workflow/{website}.txt` concrete examples and generated neural/rule files. Substrate is local plaintext; content includes readable query/thought/action demonstrations or model-induced procedures plus fixed action reminders. Action syntax is natural-language model guidance at this consumer, not executable installation. Distinct output of [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) and [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); no object counterpart is supplied.

Lineage of generated content is selected experiment traces → neural abstraction or rule curation → overwrite. Neural authorship/admission is computational after a trace-level gate. Rule authorship is extracted model trace content; admission includes exact human `y` unless `--auto`. Initial provenance and admission control of the five shipped files are unresolved. Each sampled file begins with concrete query/thought/action material, not evidence of successful induction. The legacy model receives all file text in a system message on each action request, across episodes and file replacements, without expiry or task-level selection here. Explicit model reasoning during induction is opaque; retained `<think>` text describes task reasoning, not necessarily reasons for admitting that workflow (SRC-1, `webarena/induce_prompt.py`, `webarena/induce_rule.py`, `webarena/agents/legacy/agent.py`, `webarena/workflow/gitlab.txt`, `webarena/workflow/map.txt`, `webarena/workflow/reddit.txt`, `webarena/workflow/shopping.txt`, `webarena/workflow/shopping_admin.txt`).

> with open(args.output_path, 'w') as fw:
>         fw.write('\n\n\n'.join(["## Concrete Examples"] + manual_workflows))
> --- `webarena/induce_rule.py`

The prompt's “at least two steps” rule is requested doctrine, not enforcement: its own one-shot Workflow 2 contains only a final response action (SRC-1, `webarena/prompt/instruction.txt`, `webarena/prompt/one_shot.txt`).

> Workflow 2: Obtain order information, such as date or order number
> <think>
> To find the earliest purchase date, I need to look at the "Date" column in the "Orders" table and identify the earliest date listed. The dates currently visible are: 4/27/22, 4/5/22, 3/10/22, 3/2/22, 3/2/22. The earliest date visible is 3/2/22. I will respond with this date.
> </think>
> <action>
> send_msg_to_user('The earliest purchase date is 3/2/2022.')
> </action>
> --- `webarena/prompt/one_shot.txt`

#### MEM-OBJ-arena-traces
Label: WebArena experiment evidence inputs

Source-native identity: externally persisted `experiment.log`, `summary_info.json` and screenshots under result directories. AWM's caller delegates storage to BrowserGym. Operative parts differ: readable thoughts/action strings are projected to induction; symbolic `cum_reward` admits whole traces under `gt`; final image content enters vision evaluation, not neural induction. Screenshot encoding/storage internals and trace-generation implementation remain external. These are expected raw episode evidence, not demonstrated retained runs. AWM automatically reads/parses them; human control over external production is unresolved. The later readers are evaluators and both induction alternatives, so traces can influence durable workflow updates. Distinct input bundle shared by [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) and [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); not a duplicate route (SRC-1, `webarena/run.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`).

> elif "scroll(" in a or "noop(" in a:
>             continue
> else:
>             valid_actions.append(a)
> --- `webarena/induce_prompt.py`

Neural cleanup discards scroll/noop and malformed checked actions before pairing thoughts with actions. Rule cleanup retains scroll/noop. Both parse logs with `eval`; their “invalid” filter is not an isolation guarantee. The provider sees selected query/thought/action text, not complete original observations; vision evaluator sees only the final screenshot ([RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission); SRC-1, `webarena/autoeval/evaluator.py`).

#### MEM-OBJ-autoeval-signal
Label: Autoevaluation admission signal

Source-native identity: `rm` in `{model}_autoeval.json`, alongside `gt`, task/trajectory identifiers. Substrate is local JSON; operative form is symbolic: induction tests the first record's `rm` for truth. Producer is evaluator software mapping model status to Boolean; model supplies judgment, not a reference oracle. `gt` stores external summary reward, while `--criteria gt` bypasses `rm` and rereads summary files. Automatic admission control, without a per-record human gate, shapes which raw traces enter workflow regeneration. Distinct retained gate object within the evidence chain of [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), also consumed by [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) (SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`).

> if out["status"].lower() == "success": eval_result = True
> else: eval_result = False
> --- `webarena/autoeval/evaluate_trajectory.py`

The exception branch returns a dictionary rather than the normal one-element list, with `rm: None`; consumers using `record[0]` do not implement a general tolerant rejection path. Actual malformed artifacts are not supplied.

#### MEM-OBJ-autoeval-thoughts
Label: Autoevaluation reasons and display logs

Source-native identity: evaluator `thoughts`, JSONL `outputs.jsons` and Markdown `{traj_name}.md` reporting output, captions, images and prompt. Local text/JSON stores readable natural-language judgments separately from the symbolic `rm` gate. Software automatically retains them; human review is afforded by readable files, not an inspected approval requirement. Both induction scripts read `rm`, not evaluator thoughts; retained judgment reasons therefore do not reach the workflow model through this inspected chain. Distinct reason/display part of evaluation associated with [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), not equivalent to the signal object (SRC-1, `webarena/autoeval/evaluator.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`).

> md_file.write(f"## RM\n\n{eval_str}\n\n")
> md_file.write(f"## Final Response {info['response']}\n\n")
> --- `webarena/autoeval/evaluator.py`

### Routes

#### MEM-RTE-workflow-selection
Label: Optional workflow selection

Endpoints/progression: CLI operator request → workflow directory enumeration → blank-line block parser → random selection or intended embedding search → text-file overwrite → configurable later Mind2Web consumer. Owner: `main` in retrieval CLI. Context is candidate workflow files; state includes parsed blocks, numeric index metadata and optional FAISS store. Distinct preprocessing route from [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action), using [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) on semantic branch. The default pipeline does not call it (SRC-1, `mind2web/workflow/retrieve.py`, `mind2web/pipeline.py`).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Selected block content overwrites `output_path` on random branch; semantic branch cannot complete as wired because `build_memory` returns metadata instead of the queried store.
- Later read-back: Afforded file handoff to `get_exemplars` if the operator sets its workflow path; no default pipeline connection selects this output.
- Delegated visibility: Semantic provider sees workflow name plus docstring for embedding, not the full action body; selected output restores full block content for later prediction.
- Selection predicate: Parsed blocks of at least four lines; random mode samples exactly top_k without task input. Intended semantic mode embeds task queries, pools returned indices/scores across tasks and sorts descending scores before keeping top_k; successful ranking is unestablished.
- Invalidation or expiry: Output replacement, optional index save; no store reload or expiry in this CLI. Non-null workflow suffix additionally references undefined `args.suffix`.
- Activation or effect: Static random file selection is implemented, optional later delivery is afforded; semantic activation and behavioral effects are unobserved.
- Evidence limits: No run or input files; external embedding/index semantics and score ordering not independently established; random sampling can fail when fewer candidates than top_k.

Admission: operator initiates and sets paths/count; software parser and selector decide individual content, with no per-content veto or generated-content test. Proposed change is replacement of a context file, not model weights. This is preprocessing for bounded benchmark use, not answer-oracle selection. Existing retained text supplies guidance; no admission rationale is written. Failed selection has no implemented rollback transaction; whole-file write occurs only after selection.

> if memory_path is not None:
>         memory.save_local(memory_path)
> return metadatas
> --- `mind2web/workflow/retrieve.py`

This defect does not apply to every embedding consumer: the ablation below constructs and passes the actual FAISS store.

#### MEM-RTE-exemplar-ablation
Label: Concrete example retrieval ablation

Endpoints/progression: `--run_ablation` dispatch → shipped exemplar JSON → embeddings of first-message specifiers → FAISS search by benchmark tasks → pooled score/index sorting → full selected message contents flattened to plaintext → output file. Owner: `ablation`; bounded benchmark preprocessing. Distinct from workflow-block selection and default exemplar sampling in [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action); same provider component [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings), different index handoff (SRC-1, `mind2web/workflow/retrieve.py`).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Selected full examples written to output_path as joined message contents, without role/specifier fields.
- Later read-back: Afforded through a later prediction invocation configured to use the output as workflow_path; not wired into default pipelines, and static exemplars alone are not use-produced read-back.
- Delegated visibility: Embedding service sees specifiers and task queries; output recipient gets full message content rather than metadata-only summaries.
- Selection predicate: Dense search per filtered task, pooled indices/scores sorted descending, top_k entries; no deduplication of repeated indices. The relative `../data/memory/exemplars.json` path requires an appropriate invocation directory.
- Invalidation or expiry: Output overwritten; this branch neither saves nor reloads its FAISS index and shows no expiry policy.
- Activation or effect: Concrete-example file extraction is afforded, not observed. No proof of task-relevant ranking or accuracy gain.
- Evidence limits: No external task data or run; score semantics and working-directory setup not tested. Empty retrieval results can fail at the diagnostic first-item access.

Human chooses invocation and count, not each example. Software selects existing content and writes it without human approval or answer oracle. No new abstraction is induced, no criticism reason retained, and no automatic recovery is implemented. This conditional branch is a counterexample to interpreting the workflow route's metadata-return defect as universal semantic-retrieval failure.

> if args.run_ablation: ablation()
> else: main()
> --- `mind2web/workflow/retrieve.py`

#### MEM-RTE-episode-memory
Label: Optional episode scratchpad

Part of: [RT-RTE-browser-action](runtime.md#rt-rte-browser-action)

This names the scratchpad production/read-back subroute inside the supplied action route, not a replacement for it. Endpoints/progression: model optional `<memory>` output → parser → in-process `self.memories` list → HistoryStep text → later model call when flags permit. Owner: legacy agent and dynamic prompt classes. Natural-language scratchpad content is retained in process memory, separate from raw observation/action lists and persisted workflow files. It can be a model-derived note about previous action effects, but the implementation does not require summarization or replace the full history with it. No checkpoint variant or cross-episode scratchpad reload is established by these paths (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/dynamic_prompting.py`).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Optional memory text parsed with the action, appended to the episode list and returned in diagnostic metadata.
- Later read-back: HistoryStep includes retained memory on a subsequent call when `use_history` and `use_memory` permit display; shipped run.py explicitly sets use_memory=False, so the ordinary caller does not enable scratchpad delivery.
- Delegated visibility: Model sees emitted memory as human-message history, not as a system workflow; BrowserGym receives parsed metadata, but external persistence of this field is uninspected.
- Selection predicate: Prior per-step memories with non-null content and display flags; no task-semantic retrieval. History/diff/observation shrinking is best effort and not a durable summary writer.
- Invalidation or expiry: Lists reset in agent construction; no disk-backed reload or cross-task expiry mechanism in this route.
- Activation or effect: Programmatic display path is afforded; ordinary CLI disables memory display, and actual scratchpad-dependent decisions are unobserved.
- Evidence limits: No trace of memory production/use; requested next-step remembering does not establish reliable compliance or benefit.

Model proposes optional text, parser accepts optional memory tags and software retains them; no human per-note admission or answer oracle. This is episode action operation, not a retained-method revision test. Constructor reset is recovery to empty state, not rollback of learned workflows.

> if self.flags.use_memory and self.memory is not None:
>             prompt += f"\n### Memory:\n{self.memory}\n"
> --- `webarena/agents/legacy/dynamic_prompting.py`

> use_memory=False,  # "Enables the agent with a memory (scratchpad)."
> --- `webarena/run.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission)

Trace-fed update is established as static wiring for the online branch: saved input/output pairs project to action/environment examples, a model derives text, software filters/overwrites and later samples can receive the text as a user exemplar. Original trace origin is mixed model predictions plus benchmark-supplied observations and annotated previous actions, not executed browsing. The offline branch derives from external annotated training data and is not shown to learn from the agent's own executions. Online saved metric/reward fields are not admission predicates. The result retains procedures rather than the model's induction reasoning; no subsequent reader of discarded metrics or induction reasons is shown in this route (SRC-1, `mind2web/online_induction.py`, `mind2web/offline_induction.py`, `mind2web/memory.py`; [MEM-OBJ-conversation](#mem-obj-conversation), [MEM-OBJ-mind-workflows](#mem-obj-mind-workflows)).

#### On [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action)

Read-back request is implicit in each sample invocation's configured workflow path. The selector includes the entire non-empty workflow first, then tag-filtered randomly sampled concrete exemplars; top_k counts concrete examples, not workflow subroutines. There is no semantic workflow selector in this consumer. Each added exemplar is checked against system plus query plus already admitted demonstrations; the first overflowing exemplar stops the loop, rather than trying smaller later examples. Consequently an oversized workflow can prevent all subsequent concrete exemplars from being supplied. Authority is demonstration text to the model, not an action oracle; annotation scoring occurs afterward (SRC-1, `mind2web/memory.py`; [MEM-OBJ-exemplar-content](#mem-obj-exemplar-content), [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar)).

> if total_num_tokens > MAX_TOKENS[args.model]:
>                 logger.info(
>                     f"Using {e_id} / {len(exemplars)} exemplars due to context limit"
>                 )
>                 break
> --- `mind2web/memory.py`

#### On [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission)

The retained symbolic admission result and retained evaluator explanation have different consumers. Selection reads `record[0]["rm"]` but does not forward evaluator thoughts or screenshots to the induction prompt. Induction uses task intent and selected thought/action projections; its fixed instruction requests recurrent subroutines and invariant IDs. Cleanup also removes scroll/noop, and per-template random sampling limits examples, not prompt tokens. The 2048-token generation cap is an output cap, not an input-budget guarantee. Model-authored abstractions plus fixed reminders persist; trace identifiers, reward and admission rationale are not explicitly attached to individual output workflows. Whole-file overwrite discards unregenerated content; selected traces remain separately available if the external result directory persists (SRC-1, `webarena/induce_prompt.py`; [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows), [MEM-OBJ-autoeval-signal](#mem-obj-autoeval-signal), [MEM-OBJ-autoeval-thoughts](#mem-obj-autoeval-thoughts)).

#### On [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Curation selects one example per task template, deduplicates by action name and first argument (or name alone for send_msg_to_user), then samples one per resulting key. This key is selection metadata; the stored workflow remains concrete query/thought/full-action text, including values omitted from the key. Exact human `y` is content approval; automatic mode bypasses it. Rejected candidates and rejection reasons are not written to the resulting file. Selected thoughts can retain task-level reasons, but no human admission rationale accompanies them to the later model (SRC-1, `webarena/induce_rule.py`; [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows)).

> if action != "send_msg_to_user":
>                 arg = a[s+1: e]
>                 abstract.append(f"{action}({arg})")
> else:
>                 abstract.append(f"{action}")
> --- `webarena/induce_rule.py`

#### On [RT-RTE-browser-action](runtime.md#rt-rte-browser-action)

The workflow is reread from disk for every action request, without per-task filtering, local provenance checking or expiry. It is added after fitting the main prompt, so its whole-file size is outside that fit. Consumer-facing authority is system-message guidance; actual compliance remains unobserved. The optional scratchpad is a separate in-process delivery path, disabled by the shipped caller, not evidence that retained workflows themselves are disabled (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/run.py`; [RT-CLM-context-budget](runtime.md#rt-clm-context-budget), [MEM-RTE-episode-memory](#mem-rte-episode-memory)).

## Write side

**Acquisition and initialization.** Mind2Web reads downloaded examples/ranking inputs and a shipped concrete-example file; WebArena reads external episode logs/rewards/screenshots and shipped workflow text. Initial authorship/admission of shipped examples is unresolved, but later transformations are inspectable. Both benchmark callers create an empty workflow file if the selected path does not exist. That software initialization does not approve substantive content; operators choose paths, while actual content enters through model induction or manual/rule curation (SRC-1, `mind2web/run_mind2web.py`, `webarena/run.py`; object records above).

**Automatic transformation.** Online Mind2Web is raw saved model messages → last-input/output projection → fixed-guidance induction → textual filtering → durable workflow file → later prediction prompt. Offline replaces the first two steps with annotated training action representations. WebArena is external trace → outcome predicate → cleanup and template sampling → fixed-guidance neural induction → durable system-guidance file → later action call. These are trace-fed artifact updates where applicable, not parameter training; provider components are already described by [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) and [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client). Learned capacity or improved performance does not follow from persistence alone.

**Maintenance, rejection and withdrawal.** Neural writers overwrite rather than edit the previous file. Mind2Web's textual filter can remove headers/delta blocks; WebArena's outcome gate rejects traces and parse exceptions skip trajectories. Rule mode adds deterministic deduplication and optional human content rejection, then writes only accepted examples. File replacement withdraws omitted old guidance from future file reads, but no invalidation event deletes the underlying result logs, reverts a model decision already made or rolls back an interrupted write. These statements are bounded to the inspected writers, not an assertion that external operators cannot back up or edit plaintext (SRC-1, `mind2web/utils/data.py`, `mind2web/online_induction.py`, `mind2web/offline_induction.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`; supplied admission routes and annotations).

**Reasons and alternatives.** Neural output is not guaranteed rationale-free: the WebArena one-shot explicitly includes `<think>` reasons, and rule outputs preserve selected thoughts. What is not carried through the inspected chains is structured induction/admission justification tied to each retained procedure. Evaluator reasons persist separately but selectors use the Boolean. There is no durable history compaction/checkpoint writer in the inspected legacy history helpers; they shrink displayed observations/diffs, while optional scratchpad notes are appended to a separate in-process list. This bounded account prevents conflating ordinary history fitting, episode notes and cross-task workflow induction (SRC-1, `webarena/prompt/one_shot.txt`, `webarena/autoeval/evaluator.py`, `webarena/agents/legacy/dynamic_prompting.py`; [MEM-OBJ-autoeval-thoughts](#mem-obj-autoeval-thoughts), [MEM-RTE-episode-memory](#mem-rte-episode-memory)).

## Read-back

The default paths are **request-time file supply**, not a targeted memory search followed by independent push. Mind2Web loads the file per sample and repeats admitted demonstrations in each prediction request; WebArena reads it per action and appends it to system guidance. Stored existence does not establish delivery when Mind2Web's budget omits it, and delivery never establishes activation. Website filenames identify configured stores, not a consumer's semantic matching decision ([RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar), [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system); annotations above).

Optional retrieval operates before prediction. Workflow search uses names/docstrings as embedding keys and restores full bodies via indices, whereas concrete ablation embeds specifiers and restores message contents. Neither implies that the later model sees vectors, index metadata or selector reasons. Only the workflow branch returns the wrong object to its search method; the ablation does not. There is no default pipeline connection to either output ([MEM-RTE-workflow-selection](#mem-rte-workflow-selection), [MEM-RTE-exemplar-ablation](#mem-rte-exemplar-ablation); SRC-1, `mind2web/workflow/retrieve.py`, `mind2web/pipeline.py`).

The secondary read-back consumers are update models and selectors: online induction reads reduced saved prediction records; WebArena selection reads rewards/`rm`, induction reads cleaned thoughts/actions, and human rule review reads concrete examples. Those consumer roles have different authority from the final acting model. Evaluator reasons are display evidence rather than an inspected later update input. The optional episode scratchpad returns to the action model only through enabled history flags and has an episode-limited horizon ([MEM-OBJ-conversation](#mem-obj-conversation), [MEM-OBJ-autoeval-signal](#mem-obj-autoeval-signal), [MEM-OBJ-autoeval-thoughts](#mem-obj-autoeval-thoughts), [MEM-RTE-episode-memory](#mem-rte-episode-memory)).

## Integration issues

- **Supported corrections to supplied facts:** none. The runtime account's semantic workflow failure holds, but must not be generalized to concrete ablation. [MEM-RTE-exemplar-ablation](#mem-rte-exemplar-ablation) adds the distinct CLI-dispatched path; [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) remains its component. Evidence: SRC-1, `mind2web/workflow/retrieve.py`. Consequence: optional semantic workflows and concrete retrieval have different implementation limits.
- **Duplicate/containment review:** no object counterparts are declared by runtime. New objects name retained inputs/results, not the existing admission/action routes. [MEM-RTE-episode-memory](#mem-rte-episode-memory) explicitly names a part of [RT-RTE-browser-action](runtime.md#rt-rte-browser-action); workflow and exemplar retrieval are separate preprocessing routes, not duplicate action decisions. No likely duplicate remains after comparison with supplied records.
- **Task/trace identity unresolved:** Mind2Web unsorted saved-file/sample pairing does not establish correct task labeling, and WebArena neural selection takes all admitted result directories while default output naming assumes one site. These defects limit claimed lineage precision and same-site memory scope, not physical retention ([MEM-OBJ-conversation](#mem-obj-conversation), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission); SRC-1, `mind2web/online_induction.py`, `webarena/induce_prompt.py`).
- **Default evidence handoff unresolved:** evaluator/inducer filenames differ as runtime reports, and evaluator exception output has a different JSON shape from the selector's assumed list. Source wiring is insufficient for successful default admission ([MEM-OBJ-autoeval-signal](#mem-obj-autoeval-signal), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission); SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`).
- **Initial content control unresolved:** sampled shipped exemplars and website files expose content but no original author/admission history. Keep uncertainty local; known selection, replacement and downstream authority do not depend on resolving it ([MEM-OBJ-exemplar-content](#mem-obj-exemplar-content), [MEM-OBJ-exemplar-specifier](#mem-obj-exemplar-specifier), [MEM-OBJ-arena-workflows](#mem-obj-arena-workflows)).
- **Effect unresolved:** no supplied runs establish delivered-workflow dependence, improved capacity, or successful abstraction. Input-budget risks, missing benchmark data and external service semantics prevent end-to-end conclusions despite inspectable write/read routes ([RT-CLM-context-budget](runtime.md#rt-clm-context-budget), [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action), [RT-RTE-browser-action](runtime.md#rt-rte-browser-action); [boundary](boundary.md#boundary-and-evidence)).

## Limitations and checks

The registered checkout HEAD was rechecked as 8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1. Supplied invocation, types, members, collection, worker rules and record contract were read completely, including recovery of boundary-range tails. Identity fields copy the supplied boundary/run values; direct new reads remain within SRC-1. No target code, tests, providers or examples were executed; no agents were launched and no prior analyses consulted.

Counterexamples were checked before settling strong conclusions: concrete retrieval differs from broken workflow retrieval; rule outputs retain task thoughts; the one-shot violates the requested minimum-step doctrine; optional episode memory exists although run.py disables it. Static file samples and scoped history-helper reads do not warrant exhaustive content/provenance or helper-correctness claims. All operation/effect fields retain uninspected limits.

Validation: the invocation-specific deterministic output check passed with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The initial check rejected only the pending-validation placeholder; that placeholder was removed. This check establishes structure and quotation occurrence, not analytical truth or acceptance.
