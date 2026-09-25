---
type: kb/types/note.md
description: 'Reflexion HotPotQA reasoning agents: automatic failure-derived prompt
  memory, exact-match retry control and limits of retained outcome evidence'
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-reflexion-02
source-identity: https://github.com/noahshinn/reflexion
reviewed-revision: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-reflexion-02/result.md
analysis-result-sha256: 4173ffeae7cb7e55cb0faa0c71c9bb90a22024c263ca9038cc7439bdb473968d
---

# Reflexion HotPotQA reasoning agents

Evidence basis: source code, shipped prompts and sampled historical displays at [218cf0ef1df84b05ce379dd4a8e47f17766733a0](https://github.com/noahshinn/reflexion/tree/218cf0ef1df84b05ce379dd4a8e47f17766733a0), inspected 2026-09-25. No provider execution or causal experiment was performed.

Reflexion's HotPotQA workflow retries a question with retained failure-derived guidance. A solver generates an attempt; normalized exact match against the supplied answer key determines whether the experiment retries it. Before retry, a reflection model can produce a diagnosis and plan, which the wrapper places in the next solver prompt. The answer oracle evaluates the final answer, not whether that diagnosis is true. See RTE-1 through RTE-4 in the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-reflexion-02/result.md).

> def EM(answer, key) -> bool:
>     return normalize_answer(answer) == normalize_answer(key)
> --- https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py

The strategies retain different material. Reflection-only appends generated reflections; combined last-attempt-plus-reflection keeps the latest reflection alongside the last trace. Reset clears transient scratchpad but preserves remembered text. A no-reflection baseline requires the appropriate fresh instance/class: switching an already-used CoT agent to NONE does not erase previous memory. The separate environment-based ReAct implementation has a different truncation policy and is not the class imported by the notebook.

> elif strategy == ReflexionStrategy.REFLEXION:
>     self.reflections += [self.prompt_reflection()]
>     self.reflections_str = format_reflections(self.reflections)
> --- https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py

The operative memory is natural-language text retained in the agent and automatically supplied on later attempts for the same question. Reflection branches establish a wired, online trace-learning route. Search and Lookup pull Wikipedia information; they are not retrieval tools for accumulated reflection memory. Logs and saved joblib objects provide exports, but no saved-agent-to-solver restoration route was found in the inspected HotPotQA code/notebooks.

A sampled historical log contains a concrete criticism of confusing episode release dates with air dates, followed by a changed search plan and a displayed correct answer. That is useful partial evidence of a reason-bearing artifact. It does not isolate reflection as the cause of success, and retained notebook outputs can come from code older than the pinned wrapper. The analysis therefore leaves recall faithfulness and achieved improvement unresolved. See CLM-2, CLM-3 and ABS-2.

> - I assumed that the dates of the episodes' releases were the same as the dates of the episodes' airings, when in fact they were different. I should have searched for the air dates of the episodes instead of the release dates.
> --- https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/root/ReAct/reflexion/100_questions_5_trials.txt

The agent's attempt/outcome-to-reflection-to-next-prompt connection supports a structural reflection finding. Conjectural learning and self-improvement in achieved future capacity require stronger outcome and attribution evidence. A later correct answer checks the retried solution as a bundle; it does not validate the proposed failure explanation.

## Scope

This review covers HotPotQA CoT/ReAct variants, their memory alternatives and exports. It excludes ALFWorld, programming and WebShop experiments, provider internals and live Wikipedia contents. Binary saved agents were not deserialized. API model names do not pin exact weight versions; malformed actions and over-budget truncation also limit robustness claims. No repository-wide performance or causal claim follows from this bounded pass.
