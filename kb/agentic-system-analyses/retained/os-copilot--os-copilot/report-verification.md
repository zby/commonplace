---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of OS-Copilot's runtime, memory, epistemic, workflow and reconciliation reports at the frozen source revision."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
---

# OS-Copilot report verification

## Verification

The reports support a bounded implementation account, with the local limits below. I read all five reports, their governing types, the boundary, the records contract and the supplied check. The correction-answer files are empty. The artifact check reports no findings, so there is no structural failure requiring a routed blocker. This judgment concerns semantic support, not merely the analysts' reported validation passes.

### Source and independent tracing

The checkout HEAD equals the revision in [boundary](boundary.md#source-register), and its status is clean. I independently read the responsibility-bearing task, planner, executor, retriever, manager, curriculum and service code in SRC-1, rather than taking the reports' checks as verification. No target execution, provider call or experiment was performed. Source code supports wiring; it does not supply an observed run or causal comparison.

**Runtime and workflow.** I traced `quick_start.py` through `oscopilot/agents/friday_agent.py`, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/modules/retriever/vector_retriever.py` and `oscopilot/environments/env.py`. This supports [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph) and [workflow's account](workflow.md#workflow-account): sequential queue ownership, selected prerequisite payloads, generated-code dispatch and no explicit final return value. Planner callers ignore the cycle diagnostic, as workflow states. Replanning adds prerequisites without rollback or a global retry ceiling.

The source supports [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair): the initial status fallback is permissive, repaired completion is stricter, and output truncation applies to judging rather than repair. The local repair bound is not a task-termination guarantee. In [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), the repaired score/result replace the outer values but repaired code does not. The stored candidate can therefore differ from the successfully repaired candidate. This is a genuine implementation defect, already disclosed consistently by all relevant reports, not an unresolved contradiction.

[RT-RTE-api-qa](runtime.md#rt-rte-api-qa) correctly separates QA and API from code judgment. API dispatch resolves through Python's alias, while the executor's invocation wrapper applies only to the literal Python node type. I checked the alias and kernel launch/termination in `oscopilot/environments/py_jupyter_env.py` and the subprocess launch/write path in `oscopilot/environments/subprocess_env.py`. Inherited environment and direct dispatch support host execution authority, not confinement or reliable effects. The UI's `fronted/src/interface/api.js` reads log/error fields and process completion; it supplies no independent task-success oracle. The missing console-entry function is confirmed by `setup.py` and `quick_start.py`.

**Memory and authority.** Full manager and retriever reads support [MEM-OBJ-tool-code](memory.md#mem-obj-tool-code), [MEM-OBJ-tool-description](memory.md#mem-obj-tool-description), [MEM-OBJ-tool-vectordb](memory.md#mem-obj-tool-vectordb) and [RT-BAP-tool-context](runtime.md#rt-bap-tool-context). Description embeddings rank names; JSON getters deliver descriptions/code; models interpret that text. Stored code is not automatically invoked by retrieval. Admission metadata contains no structured score, critique or source-task lineage. The automatic writer's new-name restriction does not bind direct manager writes.

[RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) and memory's withdrawal qualification are supported: deletion changes the index and disk content but leaves the current dictionary stale. A later add encounters that stale dictionary before writing files; with assertions enabled, count mismatch can stop it after index mutation. Neither report promises transactional recovery or universal revocation. Count equality is correctly distinguished from content agreement.

I traced `course_learning.py`, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`, `oscopilot/tool_repository/basic_tools/text_extractor.py` and the merge helper in `oscopilot/utils/utils.py`. These support [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), [MEM-OBJ-course](memory.md#mem-obj-course) and [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks). Continuous mode updates memory before lesson calls; saving consumes no success result. Last-fifty selection uses dictionary order, not outcome or timestamp recency. Demo extraction takes the last planner node's value. The Prior Course prompt's completed-course framing is stronger than the driver's evidence, as the reports explicitly acknowledge.

**Epistemic checks and components.** I compared the judge and QA prompts with their actual consumers. [EPI-OBJ-judgment-result](epistemic.md#epi-obj-judgment-result), [EPI-OBJ-qa-answer](epistemic.md#epi-obj-qa-answer) and [EPI-CLM-code-judgment](epistemic.md#epi-clm-code-judgment) preserve the distinction between requested verification, a consumed status/score, and warranted factual acceptance. The ledger separates checking, disposition, retention and selection. [EPI-OBJ-candidate-code](epistemic.md#epi-obj-candidate-code) does not infer an explanatory theory from arbitrary executable code. The reports' unestablished theory-builder, learning and exercised-improvement conclusions do not erase implemented feedback-responsive adaptation.

Direct reads of `oscopilot/tool_repository/api_tools/bing/bing_service.py`, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py` and `oscopilot/tool_repository/api_tools/bing/web_loader.py` support [MEM-RTE-page-context](memory.md#mem-rte-page-context), [EPI-RTE-page-content](epistemic.md#epi-rte-page-content) and [EPI-OBJ-page-content](epistemic.md#epi-obj-page-content). The threshold precedes summary/query branching; chunk retrieval has no final token cap. Loader metadata is not forwarded with page_content, and exceptions can become empty text. Cleaning, summarization and relevance selection do not check source truth. The narrow syntax error in the illustrative cleaning deduction is retained as a local limit below, not evidence against the underlying lossy transformation.

I checked the constructors and call signatures behind [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings), [RT-CMP-image-caption](runtime.md#rt-cmp-image-caption), [RT-CMP-audio2text](runtime.md#rt-cmp-audio2text), [RT-CMP-ocr-service](runtime.md#rt-cmp-ocr-service), [MEM-CMP-web-summarizer](memory.md#mem-cmp-web-summarizer), [MEM-CMP-web-sniptter-embed](memory.md#mem-cmp-web-sniptter-embed) and [EPI-CMP-web-models](epistemic.md#epi-cmp-web-models). Their separate consumers, unpinned versions and lack of requested parameter updates are supported; provider-side fixity and operation remain uninspected. The Ollama prefix incompatibility and audio response-field uncertainty are disclosed. Service mounting in `oscopilot/tool_repository/manager/api_server.py` excludes Wolfram despite importing its router. Audio/caption wrappers add no independent factual evaluator.

The benchmark code in `examples/GAIA/run_GAIA.py` supports [EPI-RTE-gaia-comparison](epistemic.md#epi-rte-gaia-comparison): batch execution uses the inner-monologue result, comparison is exact equality after postprocessing, prior rows govern accounting/resume, and the single-item branch uses a literal answer. Additional inspection of `oscopilot/utils/utils.py` establishes that GAIA_postprocess itself makes a model call, not deterministic normalization. This does not contradict the report's explicitly narrow comparison over output strings; it prevents promoting equality into a semantic-answer or process-quality guarantee.

The additional postprocessor finding rests on this implementation passage:

> def GAIA_postprocess(question, response):
>     llm = OpenAI()
>     extractor_prompt = general_pt['GAIA_ANSWER_EXTRACTOR_PROMPT'].format(
>         question=question,
>         response=response
>     )
>     result = send_chat_prompts('', extractor_prompt, llm)
>     return result
> --- `oscopilot/utils/utils.py`

[RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) matches package doctrine in `setup.py`. [EPI-CLM-excel-learning](epistemic.md#epi-clm-excel-learning) matches the tutorial's attributed outcome in `docs/source/tutorials/self_learning.rst`, not an inspectable execution witness. The reports correctly withhold empirical improvement and causal attribution. [RT-OBJ-friday-prompts](runtime.md#rt-obj-friday-prompts) and [RT-BAP-method-instructions](runtime.md#rt-bap-method-instructions) distinguish static prompt guidance from learned weights and reliable compliance.

### Relations and reconciliation

I assessed every declaration's identity, source support and evidence status, including the operative-object and component overlaps. No evidenced-absence records are declared; the scoped uncertainties must not be extracted as repository-wide negatives. Wired route statuses describe source connections, not successful deployment.

The three supersessions in [reconciliation](reconciliation.md#reconciliation) preserve identity: description with description, curriculum with curriculum, and page-processing route with the same page-processing route. The retained findings do not select a stronger operation status. The valid web-model container can coexist with its two components. The broader candidate-code object is not identical to the retained-code part. I checked all explicit Part of relations: verdict within feedback, course text within the curriculum route, QA text within API/QA, and page reduction within the API/service route. Cross-kind containment is explained and supported. Superseding course text or page reduction does not erase their previously stated containment or qualifications.

The memory integration issues are disposed of without suppressing disagreement: stale withdrawal extends the runtime finding; insertion order qualifies course selection; page processing adds context reduction; unresolved caller/dependency behavior remains unresolved. Workflow's cycle and delivery qualifications are compatible with queue-driven runtime termination. There is no unresolved substantive cross-report conflict requiring reconciliation correction. Empty correction answers supply no contrary argument.

### Consequential omission questions and stopping decision

I used the frozen top-level tree and searches across `oscopilot/`, `examples/`, `test/` and the shipped drivers to select three challenges: whether another writer bypasses the retention gate, whether another consumer changes retained-code authority, and whether alternate loops invalidate a universal verification/context claim. Manager maintenance supplies the bypass already represented. Searches for filter, programs, planner helper and writer call sites found no additional traced consumer changing the ordinary context route. Exposed helpers remain capabilities rather than evidenced absence of future callers.

Direct reads of both LightFriday examples confirm [RT-RTE-example-loops](runtime.md#rt-rte-example-loops): growing histories, first-block execution and terminal-substring handling bypass the ordinary judge. A source diff shows the alternative FridayAgent file differs in its exception wrapper; exports select the ordinary file. The diff command's exit code 1 denotes differences, not a failed source read. No omitted controller requiring a changed boundary was identified.

The additional repair-parsing limit rests on the shared extraction after language-specific prompt assembly:

> amend_msg = send_chat_prompts(sys_prompt, user_prompt, self.llm)
> new_code = self.extract_python_code(amend_msg)
> invoke = self.extract_information(amend_msg, begin_str='<invoke>', end_str='</invoke>')[0]
> return new_code, invoke
> --- `oscopilot/modules/executor/friday_executor.py`

The producer/consumer challenge to benchmark warrant is settled by the newly inspected model postprocessor and the report's narrow equality scope. Language-specific repair inspection exposes the local comparison limit below. Further optional expansion stopped because these challenges have supported dispositions, the reports make no exhaustive inventory or universal-success claim, and no remaining identified challenge undermines the central runtime, retention or warrant account. Dependency internals, arbitrary generated programs and untraced utility definitions cannot establish absent behavior or complete coverage.

## Blockers

none

## Limits

- [EPI-RTE-page-content](epistemic.md#epi-rte-page-content) contains a local error in its concrete Python-domain illustration: `1 = 1` is not a valid Python assignment statement, because a literal cannot be an assignment target. Withhold that specific syntactic characterization. SRC-1, `oscopilot/tool_repository/api_tools/bing/web_loader.py`, does support the quoted repeated-punctuation replacement and the predicted character change. The result ceases to be a valid equality expression, so the bounded rejection of universal semantic preservation still holds. This local example error changes neither the implemented page route nor its warrant classification; no correction to the central conclusion is necessary for publication.
- [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair) and [workflow's recovery account](workflow.md#recovery-and-resumed-handoffs) leave language-specific repair parsing coarsely described. SRC-1, `oscopilot/modules/executor/friday_executor.py`, selects distinct Shell/AppleScript prompts but then uses Python-fence extraction and unconditionally indexes an invocation marker for every repair. A response lacking that marker can fail before revised code reaches Env. Withhold comparisons implying equivalent successful repair handling across languages. The supported findings remain a bounded attempted-repair loop, model-directed recovery and no demonstrated reliability; the reports already allow parsing exceptions and do not promise successful recovery.
