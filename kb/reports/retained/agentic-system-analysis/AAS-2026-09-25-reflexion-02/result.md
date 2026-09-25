---
type: kb/types/agentic-system-analysis-result.md
description: 'Reflexion HotPotQA workflow: failed-attempt reflection, question-specific
  memory delivery and answer-key retry control with bounded historical display evidence'
run-id: AAS-2026-09-25-reflexion-02
system: Reflexion
run-date: '2026-09-25'
result-disposition: complete
target-class: workflow
boundary-kind: subsystem-only
reviewed-boundary: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: wired
      note: Past traces supply evidence; reflection plans are delivered under an instruction
        to use them. Neither prose artifact is an enforced rule, answer validator
        or learned parameter.
      records:
      - OBJ-2
      - OBJ-3
      - BAP-1
      - RTE-4
      - RTE-6
      values:
      - instruction
      - knowledge
    curation_operations:
      assessment: known
      basis: wired
      note: Reflection adds a diagnosis/plan to retained execution material; latest-only
        strategies forget older operative entries. This is not deduplication or revision
        of an existing reflection. Temporary truncation does not consolidate the retained
        source trace.
      records:
      - RTE-3
      - OBJ-5
      - RTE-6
      values:
      - decay
      - synthesize
    distilled_form:
      assessment: known
      basis: wired
      note: The qualifying derived artifact is a prose diagnosis/plan. Model weights
        and executable policies are not written by these routes.
      records:
      - OBJ-3
      - RTE-3
      - RTE-6
      values:
      - natural-language
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      note: Inspected runners and test source provide no content-dependence intervention.
        Sampled logs show displayed reflection and later action, not causal dependence;
        uninspected binary artifacts and unsampled log regions prevent a universal
        negative.
      records:
      - CLM-2
      - ABS-2
      values: []
    learning_scope:
      assessment: known
      basis: wired
      note: Each runner creates an agent per question and retries its question; the
        separate environment class also binds one question/environment. set_qa can
        leave stale memory but has no inspected caller establishing cross-task learning.
      records:
      - RTE-2
      - RTE-3
      - RTE-6
      values:
      - per-task
    learning_timing:
      assessment: known
      basis: wired
      note: Reflection is created synchronously at a retry boundary and inserted before
        that next attempt; there is no offline learning job or distinct staged deployment.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      values:
      - online
    lineage:
      assessment: known
      basis: wired
      note: ReAct copies external observations into its retained trace; reasoning,
        outcome text and reflection plans derive from execution. Shipped hand-authored
        examples are static inputs, not accumulated memory.
      records:
      - OBJ-2
      - OBJ-3
      - RTE-1
      - RTE-3
      - RTE-6
      values:
      - imported
      - trace-extracted
    read_back_direction:
      assessment: known
      basis: wired
      note: Before reasoning calls the host automatically assembles that agent's trace/reflections.
        The model does not request memory through a read interface; save functions
        establish no pull route.
      records:
      - RTE-4
      - RTE-6
      values:
      - push
    read_back_signal:
      assessment: known
      basis: wired
      note: Agent-local availability, selected strategy and recency choose all accumulated
        reflections or the latest attempt. There is no identity-match lookup, semantic
        ranking or content-based selection among retained entries.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      values:
      - coarse
    representational_form:
      assessment: known
      basis: wired
      note: The later solver consumes trace prose and reflection prose, including
        action strings as historical text. Serialization containers and counters do
        not add a second operative representation; unknown non-memory payloads in
        saved agents are not consumed by an inspected read-back route.
      records:
      - OBJ-2
      - OBJ-3
      - OBJ-5
      - RTE-6
      values:
      - natural-language
    storage_substrate:
      assessment: known
      basis: wired
      note: Agent strings/lists survive retries; utilities and notebooks export logs
        and agent objects to files. Git is distribution of retained examples, not
        a runtime memory backend.
      records:
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - RTE-5
      - RTE-6
      values:
      - in-memory
      - files
    trace_learning:
      assessment: known
      basis: wired
      note: Reflection branches automatically derive persistent-in-agent plans from
        failed attempts and deliver them to later attempts. Raw replay and NONE do
        not independently establish learning; benefit is not claimed.
      records:
      - RTE-3
      - RTE-4
      - OBJ-3
      - RTE-6
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: wired
      note: CoT provides thought/action/outcome trajectories; ReAct trajectories additionally
        contain Search/Lookup tool observations. Exported log files are not the input
        to reflection.
      records:
      - OBJ-2
      - RTE-3
      - RTE-6
      values:
      - trajectories
      - tool-traces
    write_agency:
      assessment: known
      basis: wired
      note: A human chooses notebook strategy and starts execution; code captures
        traces, calls the reflection model and exports artifacts without a memory-edit
        approval step.
      records:
      - RTE-1
      - RTE-3
      - RTE-5
      - RTE-6
      values:
      - automatic
  scope: HotPotQA accumulated attempt text, reflection text, formatted delivery views
    and their file exports; CoT with/without context, notebook ReAct alternatives
    and the separate environment-based ReAct implementation. Static prompts/data,
    provider parameters and non-memory payloads inside opaque saved agents are outside
    this operative memory profile. Saved-agent contents remain uninspected; no archive-to-agent
    consuming route is established.
---

# Reflexion HotPotQA reasoning workflow

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-reflexion-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/reflexion.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-reflexion-02/memory-report.md`

**Memory analysis report SHA-256:** 2becf30aa863f6e9cc42884148023e9177c6445f349a75dc1ea2f58795393ce9

## Boundary and evidence

Evidence basis: implementation and shipped prompt/README doctrine at 218cf0ef1df84b05ce379dd4a8e47f17766733a0, frozen 2026-09-25. Subsystem-only analysis of the HotPotQA reasoning workflow: CoT with/without supplied context, ReAct, reflection strategies, trial selection, prompt read-back and log/save surfaces. Target class: workflow. ALFWorld, programming and WebShop are excluded independent task families; this prevents assigning their evaluators, memory lifetimes or results to this workflow. OpenAI provider internals, live Wikipedia contents and benchmark source provenance beyond supplied answer keys remain uninspected. No execution or causal experiment was performed; a specialist inspected historical retained displays, which are separated from current source wiring.

The corrected caller-supplied repository https://github.com/noahshinn/reflexion is the sole evidence allowlist. Earlier unavailable URL supplied no system findings. All reads use the full commit at `/home/zby/llm/commonplace/related-systems/noahshinn--reflexion`; no prior review or linked paper was used.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/noahshinn/reflexion` | 218cf0ef1df84b05ce379dd4a8e47f17766733a0 | implementation | agents, model wrapper, runner notebook code cells, util logging/save | `hotpotqa_runs/agents.py`; `hotpotqa_runs/llm.py`; `hotpotqa_runs/util.py`; `hotpotqa_runs/notebooks/ReactQA.ipynb`; `hotpotqa_runs/react.py`; `hotpotqa_runs/environment.py`; `hotpotqa_runs/tests.py` | no API execution or deserialization of saved binary agents; no observed causal benefit |
| SRC-2 | Git | `https://github.com/noahshinn/reflexion` | 218cf0ef1df84b05ce379dd4a8e47f17766733a0 | doctrine/design | prompts and README reasoning instructions | `hotpotqa_runs/prompts.py`; `README.md` | instruction intent does not prove successful diagnosis or activation |
| SRC-3 | Git | `https://github.com/noahshinn/reflexion` | 218cf0ef1df84b05ce379dd4a8e47f17766733a0 | observed run | historical reconstructed log display and notebook error artifact | `hotpotqa_runs/root/ReAct/reflexion/100_questions_5_trials.txt:1927-1943`; `hotpotqa_runs/notebooks/CotQA_context.ipynb:151-165` | retained outputs need not come from this pinned source version; no causal intervention or exact prompt provenance |

## Shared records

### Components

CMP-1 — `AnyOpenAILLM` chooses completion vs chat wrapper by model-name prefix; agent defaults specify `gpt-3.5-turbo`, temperature zero and separate action/reflection token budgets. Distributed-parametric state is external; runtime calls are wired, exact weight pinning and provider parameter changes are uninspected. A source-model name is not immutable model bytes. Source: SRC-1, `hotpotqa_runs/llm.py`, `hotpotqa_runs/agents.py` constructors.

> model_name = kwargs.get('model_name', 'gpt-3.5-turbo')
> if model_name.split('-')[0] == 'text':
>     self.model = OpenAI(*args, **kwargs)
>     self.model_type = 'completion'
> else:
>     self.model = ChatOpenAI(*args, **kwargs)
>     self.model_type = 'chat'
> --- `hotpotqa_runs/llm.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

CMP-2 — Notebook trial loop and normalized exact-match function own continuation/evaluation. Symbolic code; implementation conclusion status: wired. The dataset/operator supplies the answer key. Source: SRC-1, `hotpotqa_runs/notebooks/ReactQA.ipynb`, `hotpotqa_runs/agents.py`, `EM`.

CMP-3 — Wikipedia-backed `DocstoreExplorer` supplies Search/Lookup to ReAct. Symbolic interface over mutable external text; implementation conclusion status: wired. Live contents and retrieval reliability uninspected; no truth guarantee from a returned excerpt. Source: SRC-1, `hotpotqa_runs/agents.py`, `ReactAgent` constructor/step.

### Operative objects

OBJ-1 — Question, optional supplied context and answer key remain fixed task inputs in the notebook route. They are not accumulated memory. Context and question enter reflection prompts; the key is used by deterministic exact match and is not explicitly inserted into reflection prompts. The exported display later appends the key. SRC-1 `hotpotqa_runs/agents.py:58-60,142-153,319-323,389-390`, `hotpotqa_runs/util.py:24-30`. Conclusion status: wired.



OBJ-2 — Raw attempt scratchpad. In-memory natural-language trace with labelled thoughts, action strings, observations and correctness feedback. It imports tool observations and records model/evaluator execution. The solver reads it within an attempt; RTE-3 reads a failed attempt and may retain it across retries. It is historical evidence at replay, not an executable command stream. Reset erases the current copy; last-attempt retention can keep another copy. SRC-1 `hotpotqa_runs/agents.py:81-104,109-111,126-140,191-235,255-258,301-303`. Conclusion status: wired.

>         if action_type == 'Search':
>             try:
>                 self.scratchpad += format_step(self.docstore.search(argument))
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

OBJ-3 — Generated reflection text, held in a list and rendered into prompt text. Derived from a failed trace by a model asked to diagnose a reason and devise a plan. `REFLEXION` retains all returned strings; the combined strategy keeps one. No stable entry IDs, evidence pointers, revision histories or entry acceptance criteria are added. The output may contain its own rationale; the whole string is delivered later, so rationale is available to the solver. No field or validation guarantees that a reason was emitted or used. SRC-1 `hotpotqa_runs/agents.py:106-124,298-330`; SRC-2 `hotpotqa_runs/prompts.py:21-30,117-124`. Conclusion status: wired.



OBJ-4 — Saved artifacts combine two distinct export surfaces: text logs reconstructed from assembled prompts, and joblib serialization of whole agent instances. Logs add answer keys and remove few-shot examples; they are readable summaries of state, not exact request transcripts or a specification of binary contents. RTE-5 writes both, with no inspected route restoring saved-agent memory into a solver. Existing binary files establish artifact presence only. SRC-1 `hotpotqa_runs/util.py:9-32,40-67`, `hotpotqa_runs/notebooks/ReactQA.ipynb:158-161`. Export conclusion status: wired. Existing binary payload conclusion status: uninspected.

>     log += '------------- BEGIN CORRECT AGENTS -------------\n\n'
>     for agent in correct:
>         log += remove_fewshot(agent._build_agent_prompt()) + f'\nCorrect answer: {agent.key}\n\n'
> 
>     log += '------------- BEGIN INCORRECT AGENTS -----------\n\n'
>     for agent in incorrect:
>         log += remove_fewshot(agent._build_agent_prompt()) + f'\nCorrect answer: {agent.key}\n\n'
> --- `hotpotqa_runs/util.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

> def save_agents(agents, dir: str):
>     os.makedirs(dir, exist_ok=True)
>     for i, agent in enumerate(agents):
>         joblib.dump(agent, os.path.join(dir, f'{i}.joblib'))
> --- `hotpotqa_runs/util.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

OBJ-5 — formatted memory delivery string, including bounded last-attempt view. This separates raw OBJ-2, generated OBJ-3 and the string actually consumed. `reflections_str` may contain only reflections, a truncated raw attempt, or their combination. `format_last_attempt` builds a copy; truncation does not edit the retained original scratchpad. It is in-memory derived natural-language text, with source lineage inherited from its inputs and instruction/evidence force supplied by BAP-1. SRC-1 `hotpotqa_runs/agents.py:109-118,301-310,351-371`. Conclusion status: wired.

> def format_reflections(reflections: List[str],
>                         header: str = REFLECTION_HEADER) -> str:
>     if reflections == []:
>         return ''
>     else:
>         return header + 'Reflections:\n- ' + '\n- '.join([r.strip() for r in reflections])
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

> def truncate_scratchpad(scratchpad: str, n_tokens: int = 1600, tokenizer = gpt2_enc) -> str:
>     lines = scratchpad.split('\n')
>     observations = filter(lambda x: x.startswith('Observation'), lines)
>     observations_by_tokens = sorted(observations, key=lambda x: len(tokenizer.encode(x)))
>     while len(gpt2_enc.encode('\n'.join(lines))) > n_tokens:
>         largest_observation = observations_by_tokens.pop(-1)
>         ind = lines.index(largest_observation)
>         lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
>     return '\n'.join(lines)
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

> def format_last_attempt(question: str,
>                         scratchpad: str,
>                         header: str = LAST_TRIAL_HEADER):
>     return header + f'Question: {question}\n' + truncate_scratchpad(scratchpad, tokenizer=gpt2_enc).strip('\n').strip() + '\n(END PREVIOUS TRIAL)\n'
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

### Routes

RTE-1 — Notebook/operator creates an agent with a question and supplied key, and optional context for CoT. ReAct loops Thought/Action/Observation until Finish or a code halt; permitted source-native actions are Search, Lookup and Finish. CoT makes a Thought and Finish-style action without a search loop. Model output chooses the next action; Python dispatches effects into Wikipedia reads or answer assignment. Implementation conclusion status: wired. Ordinary effects are external lookup and in-process answer/scratchpad updates, not general shell/code execution. Recovery converts search/lookup errors into observations; malformed action parsing can return `None` before tuple unpacking, so there is no universal tolerant-action guarantee. Source: SRC-1, `hotpotqa_runs/agents.py`, `CoTAgent.step`, `ReactAgent.step`, `parse_action`.

> if action_type == 'Finish':
>     self.answer = argument
>     if self.is_correct():
>         self.scratchpad += 'Answer is CORRECT'
>     else:
>         self.scratchpad += 'Answer is INCORRECT'
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

RTE-2 — Answer-key evaluator normalizes case, punctuation, articles and whitespace, then compares equality. A Finish both marks the attempt finished and records correctness feedback. The notebook selects only agents not yet correct for later trials. Implementation conclusion status: wired; guarantee strength: invariant for equality under this normalization, not semantic correctness outside that domain. The supplied answer key is an explicit oracle, distinct from the reflection model's judgment. It checks the final answer, not the truth of the diagnosis or plan. Principal is experiment operator; code controls retry selection; no human approval is required by this loop. Source: SRC-1, `hotpotqa_runs/agents.py`, `normalize_answer`/`EM`; notebook cell 12.

> def EM(answer, key) -> bool:
>     return normalize_answer(answer) == normalize_answer(key)
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>     "agent_cls = ReactReflectAgent if strategy != ReflexionStrategy.NONE else ReactAgent\n",
>     "agents = [agent_cls(row['question'], row['answer']) for _, row in hotpot.iterrows()]"
> --- `hotpotqa_runs/notebooks/ReactQA.ipynb` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>     "for i in range(n):\n",
>     "    for agent in [a for a in agents if not a.is_correct()]:\n",
>     "        if strategy != ReflexionStrategy.NONE:\n",
>     "            agent.run(reflect_strategy = strategy)\n",
>     "        else:\n",
>     "            agent.run()\n",
> --- `hotpotqa_runs/notebooks/ReactQA.ipynb` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

RTE-3 — A completed/halted incorrect attempt triggers reflection before the next reset/run. Depending on strategy it retains the previous scratchpad, accumulates reflection text, or replaces reflection while carrying the last attempt. The reflection prompt asks for a possible failure explanation and a concise high-level plan; the model proposes, code admits generated text directly to memory without a separate diagnosis-quality gate. Implementation conclusion status: wired. RTE-2 supplies outcome feedback but does not verify the proposed causal reason. Runtime/API failure recovery and durable rollback are not established for this admitted text; strategy reset/replacement is described in the memory overlay. Source: SRC-1, `hotpotqa_runs/agents.py`, `CoTAgent.reflect`, `ReactReflectAgent.run`/`reflect`; SRC-2, `hotpotqa_runs/prompts.py`.

> if (self.is_finished() or self.is_halted()) and not self.is_correct():
>     self.reflect(reflect_strategy)
> 
> ReactAgent.run(self, reset)
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

> In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure.
> --- `hotpotqa_runs/prompts.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

Guidance/theory account: a diagnosis-plus-plan is a formulated candidate solution (wired generation request), and its later prompt use is wired on RTE-4. The prompt asks for criticism of the previous attempt; content-directed criticism is afforded, with CLM-2 additionally retaining a concrete criticism of a previous assumption; its actual generating process and effect are not established. Updating after a failed answer does not prove criticism of a prior plan's content. Revision/changed reliance through retained strategy text is wired; improved future capacity attributable to that process is uninspected. Natural-language explanations/plans are addressable as sentences but lack a field-level assumption/scope contract; historical reason can be included in the diagnosis and is read with the plan, without a truth check.

>         if strategy == ReflexionStrategy.LAST_ATTEMPT:
>             self.reflections = [self.scratchpad]
>             self.reflections_str = format_last_attempt(self.question , self.reflections[0])
>         elif strategy == ReflexionStrategy.REFLEXION:
>             self.reflections += [self.prompt_reflection()]
>             self.reflections_str = format_reflections(self.reflections)
>         elif strategy == ReflexionStrategy.LAST_ATTEMPT_AND_REFLEXION:
>             self.reflections_str = format_last_attempt(self.question , self.scratchpad)
>             self.reflections = [self.prompt_reflection()]
>             self.reflections_str += '\n'+ format_reflections(self.reflections, header = REFLECTION_AFTER_LAST_TRIAL_HEADER)
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>     def run(self,
>             reflexion_strategy: ReflexionStrategy = ReflexionStrategy.REFLEXION) -> None:
>         if self.step_n > 0 and not self.is_correct() and reflexion_strategy != ReflexionStrategy.NONE:
>             self.reflect(reflexion_strategy)
>         self.reset()
>         self.step()
>         self.step_n += 1
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>     def reset(self) -> None:
>         
>         self.scratchpad: str = ''
>         self.finished = False
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

Memory route audit: producer is the reflection model or direct previous-trace copy; admission is automatic string retention with no diagnosis gate. Reset clears scratchpad, not reflections. All-reflection strategy appends; combined/latest-attempt strategies replace operative lists, forgetting earlier active entries. Immediate return is stored text; subsequent RTE-4 consumes it. Selection is agent-local strategy/recency, not a semantic or identifier lookup. Lifetime is the question-bound agent unless overwritten/recreated; no TTL or automatic rollback. Delegated visibility is uninspected. Rationale is present if the returned string contains it; no field guarantees it. Each qualifying reflection route is online, per-task, trajectory-fed (including ReAct tool traces) and distilled as natural language; raw replay/export alone do not qualify. Formulation and supply are wired; content criticism of a specific prior retained plan and improvement remain separate uninspected claims.

RTE-4 — The next solver prompt inserts `reflections_str` alongside static examples, question/context and current scratchpad. This is the later consuming invocation, distinct from immediate return of reflection generation. Implementation conclusion status: wired; behavioral activation and benefit uninspected. Source: SRC-1, `hotpotqa_runs/agents.py`, `_build_agent_prompt` methods; SRC-2 prompt templates.

>     def _build_agent_prompt(self) -> str:
>         return self.agent_prompt.format(
>                             examples = self.react_examples,
>                             reflections = self.reflections_str,
>                             question = self.question,
>                             scratchpad = self.scratchpad)
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>             return self.model(
>                 [
>                     HumanMessage(
>                         content=prompt,
>                     )
>                 ]
>             ).content
> --- `hotpotqa_runs/llm.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

The consuming wrapper receives the whole assembled prompt as one HumanMessage for chat. Coarse automatic push uses the current agent's retained string, not model-requested recall. Active solver prompt/step limits differ from the reflection-input truncator; neither ensures retention of diagnostic evidence. CoT NONE bypasses new writes but does not clear a previously populated reflection string. The notebook's NONE branch creates plain ReactAgent; calling ReactReflectAgent with NONE after failure instead reaches an unsupported-strategy branch. Source: SRC-1 `hotpotqa_runs/agents.py:73-77,109-120,292-312`; the fresh-instance condition is necessary for a clean baseline.

The public `set_qa` changes question/key without clearing answer, scratchpad or reflections. This is a reuse hazard, not an inspected cross-task learning route: runners instantiate one object per question.

>     def set_qa(self, question: str, key: str) -> None:
>         self.question = question
>         self.key = key
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

RTE-5 — `log_trial`/`log_react_trial` serialize current prompt and supplied correct answer into experiment logs; `save_agents` writes joblib objects. Implementation conclusion status: wired; serialization alone establishes neither automatic resume nor cross-task transfer. Saved object bytes were not deserialized. Source: SRC-1, `hotpotqa_runs/util.py`, runner notebook cell 14.


RTE-6 — separate environment-based ReAct reflection in `react.py`. Its class appends generated reflection strings after failed terminated/truncated execution, resets its scratchpad/environment, and supplies all reflections in subsequent solver prompts. It uses `QAEnv` as the outcome interface. Its trace-budget reduction selects largest lines of any kind, unlike `agents.py`'s observation-only policy. The notebook imports `agents`, not `react`; no in-scope caller of this separate implementation was found. Producer-to-consumer wiring is present in the class, but this is not evidence that the supplied notebook exercises it. Same natural-language, agent-local, per-task online memory mapping; no strategy alternatives in this class. SRC-1 `hotpotqa_runs/react.py:46-49,90-92,121-156`, `hotpotqa_runs/environment.py:23-26,28-70`. Implementation conclusion status: wired. Notebook activation conclusion status: absent.

>     def run(self, reset = True) -> None:
>         if (self.is_terminated() or self.is_truncated()) and not self.is_correct():
>             self.reflect()
> 
>         ReactAgent.run(self, reset)
>     
>     def reflect(self) -> None:
>         self.reflections.append(self.prompt_reflection())
> --- `hotpotqa_runs/react.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

>     def _build_agent_prompt(self) -> str:
>         return self.agent_prompt.format(
>                             examples = self.react_examples,
>                             reflections = format_reflections(self.reflections),
>                             question = self.question,
>                             scratchpad = self.scratchpad)
>     
>     def _format_scratchpad(self) -> str:
>         lines = self.scratchpad.split('\n')
>         lines_by_tokens = sorted(lines, key=lambda x: len(self.enc.encode(x)))
>         while len(self.enc.encode('\n'.join(lines))) > 1600:
>             ind = lines.index(lines_by_tokens.pop(-1))
>             line = lines[ind]
>             lines[ind]  = line.split(':')[0] + ': ...'
>         return '\n'.join(lines)
> --- `hotpotqa_runs/react.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

Route audit: explicit method call owns progression; environment outcome triggers reflection before reset, with model-generated text appended and later prompt assembly selecting all retained reflections. Immediate return is attempt completion; persistence is object-local, export/reload is not established for this class. Selection is coarse; no expiry or dedicated rollback is wired. External caller/delegated activation is uninspected. This shares the per-question online natural-language trace-learning mapping but retains its distinct all-line truncation policy. No dedicated answer oracle beyond QAEnv's supplied key is inferred. Guidance asks for failure diagnosis/plan, not a verified self-theory; formulation/supply are wired and attributable improvement uninspected.

### Claims

CLM-1 — README presents failed-attempt traces/reflections as strategies for the next attempt. Conclusion status: claimed, with wired prompt/retention support; no improvement measurement is adopted. SRC-2, `README.md`, Reflexion Strategies.

> `ReflexionStrategy.REFLEXION` - The agent is given its self-reflection on the last attempt as context.
> --- `README.md` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

CLM-2 — a sampled ReAct log displays a reflection that distinguishes release dates from air dates, followed by search/reasoning and a correct finish. This supports presence of a reason-plus-plan in retained text. The log is a reconstructed display, not a recorded intervention on memory; it cannot establish causal use, fidelity to an internal reason, or a performance gain from reflection. The implementation places the complete string in later prompts, but sampled old logs are not guaranteed executions of this exact code revision. SRC-3 `hotpotqa_runs/root/ReAct/reflexion/100_questions_5_trials.txt:1927-1943`; `hotpotqa_runs/util.py:40-60`. Display conclusion status: observed.

> - I assumed that the dates of the episodes' releases were the same as the dates of the episodes' airings, when in fact they were different. I should have searched for the air dates of the episodes instead of the release dates.
> --- `hotpotqa_runs/root/ReAct/reflexion/100_questions_5_trials.txt` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

> Thought 3: To SquarePants or Not to SquarePants aired on July 17, 2009. 2009 (To SquarePants or Not to SquarePants) < 2010 (The Clash of Triton), so To SquarePants or Not to SquarePants aired first.
> Action 3: Finish[To SquarePants or Not to SquarePants]
> Observation 3: Answer is CORRECT
> Correct answer: To SquarePants or Not to SquarePants
> --- `hotpotqa_runs/root/ReAct/reflexion/100_questions_5_trials.txt` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

CLM-3 — Historical context-notebook output records a HumanMessage validation error, while pinned `llm.py` uses the corrected content parameter. Display conclusion status: observed; failure of the current pinned wrapper: uninspected. This demonstrates why stored outputs must not automatically be attributed to current source. SRC-3 `hotpotqa_runs/notebooks/CotQA_context.ipynb:151-165`; SRC-1 `hotpotqa_runs/llm.py:23-29`.

>      "ename": "ValidationError",
>      "evalue": "1 validation error for HumanMessage\ncontent\n  field required (type=value_error.missing)",
>      "output_type": "error",
> --- `hotpotqa_runs/notebooks/CotQA_context.ipynb` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

### Evidenced absences

ABS-1 — no saved-agent-to-runtime reload route found in the inspected HotPotQA Python sources and three notebook code-cell sets. Source search for `joblib.load` finds only dataset loading in those notebooks. `save_agents` is one-way in this boundary. This prevents a claim of wired cross-process memory restoration; it does not prove saved objects are unrestorable. SRC-1 `hotpotqa_runs/util.py:64-67`, `hotpotqa_runs/notebooks/ReactQA.ipynb:47,158-161`, `hotpotqa_runs/notebooks/CotQA_context.ipynb:48,194-196`, `hotpotqa_runs/notebooks/CotQA_no_context.ipynb:47,157-159`. Conclusion status: absent.

ABS-2 — the inspected reflection builders, runners and test file contain no content-dependence intervention or diagnosis-validation route. The test file runs an agent and prints prompts; it even imports `react_cls`, absent from the pinned HotPotQA tree. That file is neither a successful test run nor a faithfulness result. Searching scoped text for ablation/shuffle/faithfulness terms added no relevant evidence. This prevents positive faithfulness and rationale-validation conclusions from inspected surfaces, not a universal negative about every uninspected artifact. SRC-1 `hotpotqa_runs/tests.py:1-14`, `hotpotqa_runs/agents.py:106-147,298-330`, `hotpotqa_runs/react.py:123-156`. Conclusion status: absent.

> agent = ReactReflectAgent(test_q, test_a)
> 
> agent.run()
> 
> print(agent._build_agent_prompt())
> print(agent._build_reflection_prompt())
> --- `hotpotqa_runs/tests.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

### Behavioral-authority paths

BAP-1 — Retained reflection/last-attempt text enters a later solver's ordinary prompt under explicit instruction to improve strategy; force is instructional/advisory, horizon the retried question. Delivery is wired, activation uninspected.

> REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'
> --- `hotpotqa_runs/prompts.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

The source shows instruction supply, not enforced compliance. Prior trace is historical evidence; normalized key equality has separate BAP-2 authority and does not validate remembered prose.

BAP-2 — Normalized key equality determines whether the notebook schedules another attempt; enforcing force within that trial loop, horizon its bounded experiment. A passed answer stops retry but does not endorse the reflection's causal account. Source: SRC-1, notebook trial selection and `EM`.

## Runtime account

Ordinary ReAct invocation: dataset question/key initialize an agent; wrapper calls generate a thought then action; symbolic dispatch searches/looks up Wikipedia or finishes; key comparison marks feedback; the notebook retries unsuccessful agents across its chosen number of trials. Before a repeated attempt, ReactReflectAgent retains/generates strategy material, resets transient scratchpad and injects retained material into the next model call. Terminal result is answer/finished-or-halted status, with logs/saved agent objects on the runner's save path. CoT variants use supplied or omitted context and a shorter one-attempt structure.

Material alternatives: `NONE` selects plain ReactAgent in the notebook, last-attempt-only bypasses reflection generation, reflection-only accumulates diagnoses, and combined mode carries both a trace and newly generated reflection. The source prompt says as many steps as necessary, but ReAct code halts above the configured step count or a 3896-token prompt threshold. The code, not that natural-language invitation, owns the operational limit.

> return ((self.step_n > self.max_steps) or (len(self.enc.encode(self._build_agent_prompt())) > 3896)) and not self.finished
> --- `hotpotqa_runs/agents.py` @ `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

Static forcing cases: (1) a wrong Finish triggers reflection on a later run, while a correct answer is not selected by the notebook; (2) a halted trace can be reflected without a submitted answer; (3) oversized observations are truncated for reflection, so context delivery is lossy; (4) malformed action parsing may fail before friendly invalid-action feedback. API credentials/dependencies are required for live runs and were not tested. No dynamic check planned: these branches are inspectable without provider calls or mutable Wikipedia observations; no reproduced execution or causal result is asserted.

This is a bounded experiment, not open-request service administration. The operator provides tasks, reference keys, strategy and trial budget; code schedules; model proposes actions and diagnoses; the answer-key comparator gates retry. Current API grant set, provider versions and deployment isolation are uninspected. No weight-update route is inferred from the name verbal reinforcement learning; the examined adaptation changes retained prompt material.

## Lens scoping

### Memory/context scope

Full lens on failed-attempt retention, generated reflections, prompt read-back, strategy alternatives, trace truncation and logging/save surfaces, within HotPotQA only. Trigger records: OBJ-2, OBJ-3, OBJ-4 and RTE-3, RTE-4, RTE-5. Other task families and provider state excluded.

### Epistemic scope

Full lens on answer candidates, exact-match outcome, failure diagnoses/plans and their later operational use. The explicit supplied answer oracle is central; its authority must not be extended to diagnosis truth or causal improvement.

## Lens outputs

### Memory/context lens


The profile's complete value sets cover the operative memory text in all scoped branches, including the alternate environment-based implementation. OBJ-4 additionally records opaque saved objects, without pretending that a readable log describes their complete payload. If integration expands the profile to restored non-memory internals of binary objects, representational form must become uninspected/not-determinable; this report does not license an extrapolation from strings to an opaque payload.

`storage_substrate` follows OBJ-2, OBJ-3, OBJ-4, RTE-5 and RTE-6: strings/lists live in memory and exported artifacts live in files. There is no runtime Git retrieval or model-weight writing. `representational_form` is natural language at the actual consumer, including historical action text that is not re-executed as a command. `lineage` combines imported tool excerpts with trace extraction and transformation. Static few-shots, dataset questions and supplied context are not accumulated memory and do not create an `authored` memory route.

`behavioral_authority` combines instruction from BAP-1's plan wrapper with knowledge from past attempts. The independent answer evaluator BAP-2 is not the authority of recalled prose, so it does not add validation or enforcement. `write_agency` is automatic under RTE-1, RTE-3, RTE-5 and RTE-6. `curation_operations` covers synthesis of a new diagnosis and branch-dependent forgetting, as detailed under Write side; text concatenation and export do not establish consolidation, deduplication or promotion.

`read_back_direction` is push and `read_back_signal` coarse under RTE-4 and RTE-6. A model generates reflection content, but it does not judge which stored entries to retrieve. An object holding a question does not implement an identifier-match selector. Token budgeting is coarse filtering, not inferred semantic selection.

The four learning descriptors cover the same qualifying reflection routes RTE-3 and RTE-6: trajectories and tool traces; per-task; online at retry boundaries; natural-language diagnosis/plan. NONE and last-attempt-only contribute ordinary retention/read-back but do not negate `trace_learning: yes` for the scoped union. The public `set_qa` method can change the question while preserving reflections; there is no inspected caller establishing a cross-task learning route. This is an isolation hazard, not evidence of a learned cross-task policy.

Faithfulness is deliberately not-determinable rather than a guessed yes or a blanket no. ABS-2 supports a bounded negative about inspected test/implementation surfaces. CLM-2 supports retained text presence only. Unsampled log regions and forbidden opaque binaries were not checked for qualifying intervention evidence. A yes would require retained execution evidence testing dependence on recalled content; no such evidence was established here.


All material memory alternatives were inventoried, including the separate environment-based class RTE-6. The source pass found no archive-to-agent restoration route (ABS-1), and no recalled-content intervention on the inspected test surfaces (ABS-2). CLM-2 retains a reason-bearing example but not dependence or benefit. This yields known memory-value sets at wired basis and a not-determinable faithfulness result, not an observed improvement claim.

### Epistemic lens

1. Boundary: SRC-1/SRC-2 implementation/doctrine plus SRC-3 historical retained displays and all selected HotPotQA routes. External live evidence/provider behavior, other task families and aggregate benchmark effects unassessed; CLM-1 is scoped to strategy delivery.

2. Object overlay: OBJ-1 includes acquired question/context and supplied oracle key; OBJ-2 contains actions, observations and tentative answers; OBJ-3 contains model-generated explanation/plan candidates; OBJ-4 preserves state/output, not additional warrant. OBJ-5 is the formatted memory view, a non-ampliative delivery transformation limited by truncation, not a separate accepted truth claim. Generic identity stays in shared records.

3. Authority ledger:

| Route | Function | Architectural status | Object / relation | Check target, evaluator, result and timing | Epistemic authority | Operational/behavioral authority | Limit |
|---|---|---|---|---|---|---|---|
| RTE-1 | content transformation | implemented | OBJ-2 answer; indeterminate without a candidate | solver uses question/context/Wikipedia; returns answer/action | no independent truth acceptance | dispatches bounded search/finish | SRC-1 agents; inference may be entailed or conjectural |
| RTE-2 | check/evidence production | implemented | answer in OBJ-2; no content change | normalized equality to supplied OBJ-1 key after Finish | exact-match benchmark correctness only | creates correct/incorrect observation | does not test explanation/plan |
| RTE-2 | disposition/acceptance | implemented | answer in OBJ-2; no content change | equality result consumed by notebook | accepts answer for this supplied-key experiment | stops retry via BAP-2 | key quality and other semantic answers uninspected |
| RTE-3 | content transformation | implemented | OBJ-3; ampliative failure diagnosis/plan | reflection model, after failed/halted attempt | candidate explanation, no independent warrant | admits strategy text for next attempt | a possible reason does not follow uniquely from failure |
| RTE-3 | retention | implemented | OBJ-3/retained OBJ-2; no further content change | selected strategy stores/replaces strings | retention grants no acceptance | enables later read-back | no separate diagnosis truth gate shown |
| RTE-4 | operational admission/selection/consumption | implemented | OBJ-3/OBJ-2; no content change in insertion | next solver prompt uses retained strategy | guidance, not verified truth | BAP-1 instruction | delivery not behavioral improvement |
| RTE-5 | retention | implemented | OBJ-4; serialization | operator runner save point | audit/persistence only | no extra consumer inferred | binary artifact filenames are not execution evidence |

4. Lifecycle: answers in OBJ-2 have indeterminate content relation, but RTE-2 implements acceptance under exact normalized key equality. OBJ-3 diagnosis is an ampliative conjecture: failed attempt provides anomaly; RTE-3 generates a possible explanation and plan; no explicit consequence-derivation or diagnosis-specific test is established. A later answer match tests the attempted solution as a bundle, not that explanation. Diagnosis acceptance and post-acceptance integration architectural status: not determinable within inspected routes; it is operationally used before such acceptance. Observed candidate state for the historical OBJ-3 diagnosis and answer on CLM-2 is not determinable for their production, diagnosis testing and acceptance phases: the reconstructed display preserves candidates but lacks complete execution provenance. Its displayed correct finish is observed only as retained text. Other uninstantiated route branches have no instance observed. Do not attribute this display to execution of the exact pinned implementation. CLM-3 demonstrates that older notebook outputs can disagree with current code. OBJ-1 is imported input, discovery lifecycle not applicable; OBJ-4 is serialization, lifecycle not applicable.

RTE-6 has the same implemented candidate-generation/retention/consumption functions as RTE-3/RTE-4, but a separate QAEnv evaluator and all-line trace budget. No notebook activation is established. For OBJ-5, discovery lifecycle is not applicable to formatting; truncation can omit evidence without producing warrant.

5. Claim comparison: CLM-1 has wired retention/delivery support; CLM-2 supplies a compatible historical display, not activation/causal support for the current implementation. CLM-3 limits source-to-output attribution. The prompt's aspirational improvement wording is not an improvement result. The code's limits also narrow prompt language permitting unlimited steps.

6. Conclusion: Reflexion's HotPotQA workflow turns outcome feedback into retained strategy candidates and retries with them. The answer oracle checks final answers, while the model's diagnosis stays a candidate. This establishes an operative feedback route without establishing the explanation's truth or the cause of any later success.

## Reconciliation

Checked report run/source/boundary, complete status, unchanged input/method hashes and exact report digest. Mappings: MEM-OBJ-1 → OBJ-5; MEM-RTE-1 → RTE-6; MEM-ABS-1 → ABS-1; MEM-ABS-2 → ABS-2; MEM-CLM-1 → CLM-2. SRC-3 separates historical output evidence from SRC-1 implementation; CLM-3 retains the historical/current-wrapper mismatch.

All ten integration issues accepted: keep formatted view distinct; include separate environment implementation without notebook activation; preserve bounded absences/faithfulness uncertainty; distinguish append vs replacement strategies; qualify NONE by fresh instance and class; preserve set_qa state-reuse hazard without upgrading task horizon; separate rationale delivery from truth/benefit; distinguish exports from restoration; and separate historical output failures from current wiring. No substantive conflict remains. Specialist source analysis does not independently clear the full result.

## Bounded synthesis

The strongest supported contribution is a wired per-question retry mechanism that carries failure-derived natural-language guidance into a later model invocation. It can criticize prior behavior by asking for a diagnosis and altered plan. CLM-2 additionally preserves a concrete failure explanation and changed search plan followed by a displayed correct answer; this supplies a partial result without establishing the explanation caused success. No inspected intervention establishes that criticism improved capacity for future action, so conjectural learning remains uninspected at the outcome level.

Reflection as a structural mechanism is wired at the reasoning-agent boundary: its own attempt trace and outcome are represented, generated diagnosis is retained, and subsequent prompt construction mediates later behavior. That does not establish a reflective theory-builder's self-theory of its organization. Self-improvement in achieved capacity remains uninspected; a connected revision route is partial support, not measured improvement. These conclusions differ deliberately: a self-representing feedback path can exist without demonstrated benefit.

A candidate-linked trial trace with an independently varied reflection condition would sharpen activation and effect claims. Merely serializing agents, observing one later correct answer, or using a stronger model would not isolate why performance changed.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Source-only pass | SRC-1, RTE-3, RTE-4 | HotPotQA code/prompts | observed diagnosis/activation or causal improvement | candidate-linked runs and controlled contrasts |
| Other task families excluded | SRC-1 | HotPotQA only | repository-wide evaluator/memory claims | separate branch analyses |
| Provider/live Wikipedia external | CMP-1, CMP-3 | wrappers/interfaces | exact weights and retrieved-source truth | pinned deployment and retained retrieval evidence |
| Supplied key authority bounded | RTE-2, BAP-2 | normalized exact match | diagnosis warrant and general semantic correctness | independently checked claims/reference quality |
| Historical displays are not exact-version executions | SRC-3, CLM-2, CLM-3 | sampled text and notebook outputs | current-code operation or causal memory benefit | execution provenance and intervention records |

## Verification and blockers

### Semantic verification

Checked strategy routing, outcome oracle, code halt versus prompt wording, next-trial delivery and malformed-action branch. Learning/theory properties retain separate statuses and no outcome acceptance is transferred to diagnosis truth. Profile scope includes all operative text branches and exports, while excluding unconsumed opaque non-memory saved-agent internals; no representation inference comes from their filenames. RTE-3 and RTE-6 qualify as automatic retained-reflection routes; raw replay and export do not independently qualify. Their descriptors remain trajectories/tool traces, per-task, online and natural language. RTE-4/RTE-6 push is coarse agent-local supply, not identifier matching or semantic retrieval. ABS-1 prevents a restoration claim; ABS-2/CLM-2 preserve uncertain faithfulness. Historical observed displays remain separate from implementation and causal evidence.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-reflexion-02/result.md`; `commonplace-validate --full` passed after specialist integration.

### Blockers

none
