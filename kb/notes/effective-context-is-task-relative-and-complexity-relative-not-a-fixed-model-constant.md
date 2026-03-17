---
description: Synthesizes Paulsen MECW, ConvexBench, and the two-axis context-cost model — usable context varies with task type and prompt difficulty, so nominal window size is a misleading abstraction
type: note
traits: [has-external-sources]
tags: [computational-model, foundations]
status: seedling
---

# Effective context is task-relative and complexity-relative not a fixed model constant

How much context an LLM can actually use is not a fixed property of the model. It depends on the task and on the prompt's effective difficulty for the model. A model may handle a large window for one task shape and fail at a much smaller window for another. Two prompts at similar token counts may consume very different amounts of effective budget — one compositionally shallow and cleanly framed, the other requiring deep structured reasoning or burying the relevant information in a harder-to-use presentation.

Two independent sources converge on this:

**Volume varies by task type.** Paulsen ([2025](../sources/paulsen-maximum-effective-context-window-mecw.md)) measures Maximum Effective Context Window (MECW) across 11 frontier models and finds it far smaller than advertised limits. Crucially, the threshold shifts by problem type. This rejects the common simplification that a model has one stable "usable context length."

**Complexity can dominate volume.** ConvexBench ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)) shows performance collapsing with compositional depth at just 5,331 tokens — far below nominal limits — then recovering when recursive steps get focused local frames. Token count alone does not determine whether a prompt is usable.

The synthesis is **effective context is relational**: model choice matters, task type matters, and prompt difficulty changes the effective cost of a prompt. This is weaker and cleaner than treating MECW as a single parameterized scalar `MECW(model, task_type, complexity)`. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), this note interprets that relationship more naturally as a task-shaped cost measure `||P||_t ≤ M` — the cost norm depends on what you're asking the model to do.

This sharpens the [context-efficiency](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) note's two-axis model. Volume and complexity are not independent benchmarks you read off a spec sheet. In the interpretation developed here, they are two dimensions along which prompts consume bounded effective budget. Long-context claims and raw token counts hide that dependence, which is why architectural responses must manage scope, framing, and decomposition — not just chase larger windows.

**Caveats.** The evidence is convergent, not final. Paulsen does not cleanly isolate pure volume from task difficulty (counting, sorting, and filtering are themselves LLM-hard). ConvexBench does not measure a joint volume-complexity surface — it shows complexity alone can dominate. Position, framing, and scope contamination may also affect usable context, and this note treats those as part of prompt difficulty rather than as separately measured variables. The claim should stay qualitative: effective context is not a fixed per-model constant, and any theory that treats it as one is too coarse.

## Open Questions

- Is there a clean empirical regime where volume can be varied while task difficulty and compositional complexity stay mostly fixed?
- Can the task-shaped cost measure `||·||_t` be made concrete enough for useful prediction, or is it mainly explanatory?
- Which natural-language tasks exhibit the same complexity-dominant collapse that ConvexBench shows in symbolic reasoning?

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — complexity can dominate context usability even at trivial token counts.
- Paulsen (2025). [Context Is What You Need — The Maximum Effective Context Window](../sources/paulsen-maximum-effective-context-window-mecw.md) — MECW is much smaller than MCW and varies by problem type.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — extends: names the implication of that note's two-axis model for how effective context should be treated
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — sharpens: explains why task dependence belongs naturally in the effective-cost measure rather than only in the threshold
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: clean local frames reduce effective cost by stripping irrelevant dependencies
- [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — consequence: if effective context is relational, decomposition and representation choice become first-class scheduling decisions
