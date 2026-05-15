---
description: NeurIPS 2023 research scaffolding where failed task attempts become short natural-language reflections that are appended to the next prompt; per-task rolling memory tail of three, no cross-task consolidation, no weight updates
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Reflexion

Reflexion is a research repo for language agents that improve by verbally reflecting on their own failures. It holds the experimental code for the NeurIPS 2023 paper by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. The repo contains four task-specific scaffolds — decision-making on ALFWorld, web navigation on WebShop, reasoning on HotPotQA, and programming on HumanEval/LeetCode/MBPP — each implementing a variant of the same loop: attempt a task, detect failure, prompt the same LLM to produce a short plan or self-reflection about what went wrong, prepend that reflection to the next attempt. The head of `main` hasn't moved substantively since January 2025; this remains a frozen research artifact rather than an evolving system.

**Repository:** https://github.com/noahshinn/reflexion

## Core Ideas

**A reflection is a short plan-shaped string tied to a single task instance.** In `alfworld_runs/generate_reflections.py`, `_generate_reflection_query` feeds the failed log and prior memory into a prompt that asks for "a concise, new plan of action that accounts for your mistake with reference to specific actions that you should have taken" and emits text after a "New plan:" marker. `webshop_runs/generate_reflections.py` uses the same shape with an "Instruction:" scenario split. The unit of memory is one such string per failed trial for one environment; nothing gets cross-indexed, typed, or linked.

**The persistent state is an in-memory list per task, checkpointed to JSON.** `alfworld_runs/main.py` initializes `env_configs` as a list of dicts `{'name', 'memory': [], 'is_success': False, 'skip': False}` and, after each trial, writes `env_results_trial_{n}.json` alongside a `world.log`. Between trials it calls `update_memory(...)` which mutates `env_configs[i]['memory']` in place. There is no database, no embedding store, no cross-env aggregation — reflections stay pinned to the env index that produced them.

**Memory is a rolling tail of the last three reflections.** The crucial clamp sits in `update_memory`:

```python
if len(env['memory']) > 3:
    memory: List[str] = env['memory'][-3:]
else:
    memory: List[str] = env['memory']
```

That slice is what the next reflection generator sees as "Plans from past attempts" and what `EnvironmentHistory._get_base_query` renders into the next trial's prompt header as numbered `Trial i:` blocks. Older memory is never deleted from the JSON record, but the prompt only ever sees the trailing three. This is memory as a bounded hint buffer, not a growing corpus.

**The oracle is binary task success from the benchmark harness.** `alfworld_runs/main.py` only generates a new reflection if `not env['is_success'] and not env['skip']`. In `programming_runs/reflexion.py`, the loop runs per-item and gates on `exe.execute(cur_func_impl, tests_i)` returning a passing state; `self_reflection` is called only after a failed unit-test run, and the outer break also requires passing the held-out `exe.evaluate(... item["test"] ...)`. There is no human judge, no LLM judge, no cross-sample aggregation — success or failure on the benchmark test determines whether a reflection is emitted.

**Programming runs do not persist reflections across tasks.** Unlike ALFWorld, `programming_runs/reflexion.py` re-initializes `reflections = []`, `implementations = []`, `test_feedback = []` for every dataset item and the inner `while cur_iter < max_iters` loop is the only scope where reflections influence generation. The reflection is used once to condition the next implementation attempt within the same item's pass-at-k budget, then discarded. The `reflections` list is written to the output jsonl record purely as a log, not as reusable state. Cross-task generalization simply does not happen in the programming variant.

**Reinjection is a prompt-time concat, not a retrieval step.** In ALFWorld and WebShop, `EnvironmentHistory._get_base_query` prepends a `Your memory for the task below:\nTrial 0:\n...\nTrial 1:\n...` block to the task prompt. In HotPotQA, `hotpotqa_runs/agents.py` sets `self.reflections_str` via `format_reflections(self.reflections, ...)` and the agent prompt template substitutes it in. No similarity search, no selection policy — the whole (clamped) list goes into every prompt for that env.

**Four `ReflexionStrategy` modes codify what gets carried forward.** `hotpotqa_runs/agents.py` defines `NONE`, `LAST_ATTEMPT`, `REFLEXION`, `LAST_ATTEMPT_AND_REFLEXION`. The middle two isolate a clean experimental question — is the value in feeding forward the raw reasoning trace, the distilled self-reflection, or both? The `CoTAgent` applies the strategy inside `run(...)` only when `self.step_n > 0 and not self.is_correct()`, so the reflection path is triggered the same way as ALFWorld's: one shot per failed attempt.

**Implementation is per-task scaffolding, not a library.** `alfworld_runs/`, `webshop_runs/`, `hotpotqa_runs/`, and `programming_runs/` each re-implement their own `EnvironmentHistory`, `generate_reflections.py`, or equivalent. There is no shared `reflexion` package; the loop is copy-pasted with task-specific seams. The repo is essentially four experiments that share a paper, not a reusable framework.

## Comparison with Our System

Reflexion is a foundational reference for the "feedback becomes text, text conditions the next attempt" idea, but it is much narrower than any workshop-memory system in our review set. The retained form is a per-task prompt-visible tail of up to three plan strings, while older entries remain only in the run log. The oracle is benchmark-task success. Commonplace maintains a typed, linked graph of notes curated by humans; the two systems share only the broad readable-prose form.

| Dimension | Reflexion | Commonplace |
|---|---|---|
| Trace source | Failed-trial logs from one benchmark task (ALFWorld/WebShop/HotPotQA) or failed unit-test output (programming) | Human+agent editing, notes, links, workshop artifacts |
| Learned substrate | Per-env prompt-visible tail of up to three plan strings; prompt-only in programming | Typed notes, links, instructions, ADRs, indexes |
| Addressable unit | None — prompt-visible memory is `env_configs[i]['memory']`, sliced `[-3:]`; older entries remain in the JSON run record | Individual markdown files with frontmatter |
| Update style | Append reflection, clamp tail at three, feed forward | Manual curation with validation and review bundles |
| Oracle | Binary benchmark success / unit-test pass | Weak human judgment plus local validators |
| Scope | One env or one programming item — never cross-task | Cross-domain methodology KB |
| Persistence | JSON per trial, log files per env, discarded after run | Git-tracked markdown across the project lifetime |
| Retrieval | No retrieval; whole (clamped) list injected | Agent-driven navigation over linked markdown |

**Where Reflexion is stronger.** The loop is minimal and legible: four source files per task implement the full learning cycle, and the data flow is traceable in an afternoon. The strong oracle (benchmark pass/fail) means the system doesn't need any metadata machinery to decide when to reflect. The three-slot prompt-visible tail is a useful demonstration that bounded memory can still produce measurable improvement, which is something our larger artifact stores cannot take for granted.

**Where commonplace is stronger.** Separately addressable artifacts, typed frontmatter, link semantics, and workshop-vs-library layering. Reflexion has none of these — a reflection is a free-text plan with a trial index and nothing else. It also has no notion of an artifact maturing, being superseded, or being cross-referenced; each reflection is born, lives for up to three trials at the prompt front, and is overwritten by newer ones.

**Trace-derived learning placement.** Trace source: per-trial logs of failed attempts at a single benchmark task, with the trigger boundary at one full task attempt (for ALFWorld/WebShop/HotPotQA) or one failed unit-test run (for programming). Extraction: a second LLM call reads the failed trajectory plus the last three prior plans and emits a fresh plan or self-reflection string; the oracle is binary benchmark success, and `update_memory` is the gate. Promotion target: prompt-visible text only — `env_configs[i]['memory']` is the active store for the next prompt, while the JSON trial record keeps the older history for resume and logging. Scope: per-task and per-benchmark only; programming runs discard reflections across items, ALFWorld/WebShop keep them per env index. Timing: online within a multi-trial run, sequential, one reflection per failed trial. On the [survey's](../trace-derived-learning-techniques-in-related-systems.md) axis 1, Reflexion fits the **trajectory-run pattern** — repeated bounded attempts at the same task rather than a single live session or an event stream. On axis 2, it is squarely **artifact-learning** at its lowest structure — a list of free-text plans clamped at three, with no CRUD verbs, no counters, no typed fields. Reflexion is adjacent to deploy-time artifact learning: it mutates prompt-visible text during a run without weight updates, but it lacks the cross-session durability that the deploy-time-learning note treats as central. No new subtype is warranted.

## Borrowable Ideas

**Fail-then-plan as a minimum reflection unit.** Ready now as a workshop pattern. The ALFWorld loop is as small as a reflection skill can get — failed trajectory in, one concise plan out, next attempt conditioned on that plan. Anywhere we want an agent to improve a workshop artifact between iterations, the "only reflect on failure, emit a plan, cap the memory" shape is a useful floor.

**Bounded memory tail.** Ready now as a constraint. The `[-3:]` clamp is a pragmatic reminder that not every artifact-learning loop should accumulate indefinitely. For commonplace, the analogue is limiting how many prior workshop reflections get injected into a new task — a clamp is cheaper than summarization and often sufficient.

**Strategy enum as an experimental seam.** Ready as a framing. `ReflexionStrategy` separates the question "what do we carry forward?" (raw trace, distilled reflection, both, nothing) from the rest of the agent. If we ever automate workshop-to-library handoff, an explicit enum for injection modes — `NONE`, `LAST_TRAJECTORY`, `DISTILLATION_ONLY`, `BOTH` — would make experiments legible without changing the rest of the loop.

**Treat per-task memory and cross-task memory as different substrates.** Needs a use case first. Reflexion's programming variant cannot generalize across items because it never stores reflections across them; the paper's descendants (ExpeL, ReasoningBank) earn their complexity precisely by adding that missing store. For commonplace, the lesson is architectural: the workshop already has per-task memory; any cross-task promotion path needs a distinct store, not a deeper version of the workshop buffer.

## Curiosity Pass

**What property does the reflection loop claim to produce?** A next-attempt prompt that is better conditioned than the previous attempt's prompt — where "better" means containing a short plan that names the earlier mistake. On ALFWorld and WebShop, the claim is that enough such plans, injected across trials, push task success rates up.

**Does the mechanism transform the data, or just relocate it?** It transforms. A failed trajectory plus old plans go in, a new plan string comes out — the new plan is not a slice of the trajectory, it is an LLM-produced distillation conditioned on it. But the transformation is opaque; no code inspects the result. The only quality signal is whether the next trial succeeds, which comes from the benchmark environment, not from the reflection module.

**What is the simpler alternative?** The repo itself ships one: `LAST_ATTEMPT` carries forward the raw reasoning trace instead of a reflection, and `NONE` carries forward nothing. These strategies are the direct ablations, and whether `REFLEXION` beats `LAST_ATTEMPT` on each benchmark is the genuine experimental question rather than a marketing claim. Outside the repo, an even simpler alternative — "append the failed log and let the model re-read it" — is one prompt concat away.

**What could this mechanism achieve even if it worked perfectly?** A prompt prefix that encodes the lessons of the last three failed trials on this exact task. It cannot: generalize across tasks, compose lessons into a reusable playbook, detect when a stored plan is misleading (nothing retracts plans — they just roll off the tail), or survive the run beyond whatever JSON happens to be checkpointed.

**The programming variant is almost a different system.** A close re-read of `programming_runs/reflexion.py` shows that reflections there never cross dataset items. That makes the programming loop structurally closer to a within-sample retry with scratchpad than to "learning from experience" — which the paper name suggests but the code does not support at the inter-item level. Descendants like ExpeL had to add an explicit cross-task consolidation pass to bridge that gap; Reflexion itself does not.

**The "N trials, memory tail of three" design is fragile to benchmark design.** The loop relies on the same env being replayed across trials, so the reflection for env_7 only ever helps env_7. If trials were shuffled or env identities were not stable, the whole memory indexing scheme would break. The simplicity is real, but it depends on benchmark assumptions that a production memory system cannot make.

## What to Watch

- Whether later descendants retain the "fail-only reflection" gate or start reflecting on successes (ExpeL already does compare-successes-vs-failures; ReasoningBank formalizes it further).
- Whether the per-env fixed-index memory store shows up anywhere outside benchmark scaffolds, or is abandoned once systems need cross-task generalization.
- Whether the programming-variant pattern (reflections live only within a single item's retry budget) reappears as "per-turn scratchpad" in agentic systems, distinct from cross-run memory.
- Whether verbal-only reinforcement continues to be a competitive baseline as weight-update paths (GRPO, reward modeling on traces) mature.
- Whether the frozen 2025-01 state of this repo means the reference implementation drifts out of date relative to how people now describe "Reflexion" in papers that cite it.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Reflexion is the historical anchor for trajectory-run artifact learning and the structural floor against which ExpeL, Dynamic Cheatsheet, and ACE add maintenance machinery
- [ExpeL](./expel.md) — sharpens: ExpeL embeds the Reflexion retry loop but adds a cross-task consolidation pass with CRUD-verb rule maintenance; Reflexion itself never consolidates across tasks
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) — contrasts: both keep a prompt-visible text artifact without weight updates, but Dynamic Cheatsheet carries forward one evolving document across an ordered benchmark pass, while Reflexion keeps per-env lists clamped at three
- [ClawVault](./clawvault.md) — contrasts: both preserve inspectable text, but ClawVault runs a richer typed artifact lifecycle while Reflexion clamps to a rolling three-slot buffer
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Reflexion depends on a strong binary task-success oracle, and its memory policy (append on failure, clamp tail at three) would degrade under weaker signals
- [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) — sharpens: Reflexion sits squarely in deploy-time artifact-update space, where learning happens by mutating prompt-visible text rather than training weights
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: Reflexion's memory is pure workshop — no library, no promotion path, no cross-task accumulation
