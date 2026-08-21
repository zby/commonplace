# Evidence ledger for the Exo retained-theory proposal

> **Status:** Workshop evidence ledger. This file records pinned Exo facts, adjacent supporting and adverse evidence, unresolved gaps, and falsifiers. The [Exo case](./exo-case.md) owns the argument, and the [experiment design](./experiment-design.md) owns the protocol.

## Pinned Exo and ExoWorker facts

Evaluation boundary: canonical Exo main commit `ef4cfe057af0` and the separately linked ExoWorker branch commit `ed08a571`. The [whole-system analysis](../../agentic-systems/exo.md) uses the same canonical Exo pin. The [memory-system review](../../agent-memory-systems/reviews/exo.md) remains pinned to the earlier `baa07f67`; unchanged memory claims rely on that review, while refreshed claims rely on the checkout diff and branch inspection. Neither review ran a live Exo instance.

| Claim | Evidence status | Pinned basis |
|---|---|---|
| Exo exposes a causally connected self-representation of its mutable executor | Structural classification grounded in code and documentation | The agent can inspect the mounted source tree and checked-in `SELF.md`, edit prompt and tool assembly, then rebuild and restart the executor |
| Ordered event history survives sandbox rewind | Code-grounded, unchanged | The Rust substrate retains canonical events outside the rewound sandbox; refreshed attach/detach events preserve this invariant |
| The agent can retain symbolic behavior changes | Code-grounded capability, strengthened | Repository, shell, git, tests, rebuild/rollback, and managed tools from local or exact-commit sources provide inspectable write and installation paths |
| Exo retains several natural-language forms | Code-grounded capability, strengthened | Memory, skills, prompts, the self map, and free-text rebuild reasons persist through explicit paths |
| ExoWorker instructs the agent to retain learnings in different forms | Code-grounded on the separate branch | Its prompt maps lasting facts to `remember`, reusable playbooks to `install_skill`, and repeated helpers to `install_agent_tool`; memory includes lessons from failures |
| ExoWorker contains a primitive promotion heuristic | Interpretation of the branch instructions | The form mapping does not generally estimate later improvement value, assign evidentiary authority, or state invalidation conditions |
| Exo exposes a broad revision envelope and repeatable write paths | Code-grounded capability; later reuse unobserved | Executor source, prompts, tools, tests, adapters, memory, skills, and self map are mutable; rebuild/restart and tool replacement return to editable state, but no inspected run follows a successor through another improvement episode |
| Exo accumulates beneficial improvements in operation | Unestablished | Persistence, loading, installation, and later availability are code-grounded; benefit and faithful behavioral use are not observed in a live instance |
| One Exo improvement has helped produce a later improvement | Unestablished | No inspected record measures a later improvement episode or traces dependence on an earlier retained benefit |
| Current mechanical oracles establish judgment improvement | Negative at the refreshed pin | Builds, tests, restart outcomes, logs, and registry validation can reject mechanical faults but admit semantic degradation; the cloned-sandbox canary remains future work |
| Canonical Exo automatically extracts and evaluates lessons from traces | Negative at the refreshed pin | Memory and skill writes are deliberate, the registry performs explicit install/remove operations, and no added path mines the event log into accepted lessons |
| Canonical Exo materializes complete conversation history | Code-grounded, unchanged | The canonical turn loop still materializes all message and tool events without an implemented history window, token budget, compaction, or relevance selector |

The baseline must include all of these existing surfaces. Exo already retains episodes, natural-language artifacts, and symbolic policy. Its managed registry adds stable identity, pinned source, pre-installation validation, atomic replacement, and inspection for tools. A fair treatment therefore compares current Exo with the same system plus an explicit theory lifecycle; it does not compare theory against raw traces or ephemeral tools alone.

Current artifacts may voluntarily contain rich reasoning, but the pinned system does not require them to state premises, scope, status, or an invalidation path. A rebuild reason remains event-local. ExoWorker's form-selection instructions are evidence of a heuristic, not evidence that the agent follows it reliably or that the resulting artifacts mediate later decisions. None of these artifacts should be relabelled `T_n` without evidence that it functions as a retained theory.

## Adjacent supporting evidence

These results support parts of the proposed pathway. None establishes the Exo treatment as a whole.

| Source | What it supports | What it does not support |
|---|---|---|
| [HyperAgents](../../sources/hyperagents.ingest.md) | In five runs, frozen hyperagents evolved on paper review and robotics generated stronger agents for unseen math grading than the initial hyperagent (`Improvement@50 = 0.630`). This is one bundled, cross-domain contribution from an earlier retained improver to later improvement. | The causal contribution of any prompt, insight, code change, or theory; an Exo effect; or sustained compounding. Continued evolution from transferred rather than fresh hyperagents had no significant advantage. |
| [Agent Optimizers](../../sources/agent-optimizers-compound-terminal-bench.ingest.md) | Retention, transfer to an expanded task set, and further optimization under RELAI-VCL. | An equally budgeted fresh start or a trace showing that the first gain made the later phase more productive. |
| [Co-Harness](../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) | Repeated exchange among checked harness edits, training trajectories, updated weights, and another harness round. | A matched comparison separating feedback from additional training or search. |
| [Trajectory-Informed Memory Generation](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) | Subtask-level natural-language tips with LLM-guided retrieval improve held-out AppWorld scenario completion by 14.3 percentage points. Semantic extraction and activation can transfer across recurring task structure with a clear oracle. | Exo-specific value, open-ended self-theory, lifecycle governance, a matched current-Exo baseline, or feedback into later improvement. |
| [Knowledge-Centric Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | A frozen generation-10 semantic artifact improves held-out Polyglot and ARC-AGI-1 solve rates across donor–recipient model pairings. Scoped claims can be challenged, split, and retained as rejections. | The contribution of any one curation component, open-ended semantic correctness, marginal value beside Exo's existing forms, or later curation productivity. |
| [Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md) and the [trace-learning survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) | Readable natural-language and symbolic artifacts are practical learning targets; retrieval and recurrence constrain their value. | A universal preference for natural language, a general promotion theory, causal identification of the semantic component, or compounding rather than task-side accumulation. |

## Adverse evidence and its boundary

### Condensed experience may be inert

[Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) studies ExpeL, Dynamic Cheatsheet, ReasoningBank, and G-Memory. Across its tested frameworks, models, and environments, perturbing raw trajectories often changes behavior while perturbing automatically condensed experience often does not. The result is direct adverse evidence against assuming that a written memory artifact is operative.

The experiment does not test a reviewed, episode-linked system theory with declared scope and authority, nor an Exo baseline with facts, skills, tools, code, and retained episodes. It also measures causal uptake, not truth, warrant, benefit, or later improvement productivity. Those boundaries prevent overgeneralization; they do not rescue the proposal. ReasoningBank's native prompt already asks for concrete, actionable advice, reasons, and exceptions, so “write a better summary” is not an adequate answer. Any proposed advantage must come from an observed combination of structure, gating, activation, and retained source evidence.

### Consumer-blind summaries can damage search

[Meta-Harness](../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) reports 50.0 median text-classification accuracy when its proposer can inspect raw traces, compared with 34.6 for scores only and 34.9 for scores plus generated summaries. This is strong adverse evidence against replacing diagnostic episodes with fixed, consumer-blind summaries.

The tested summary arm removed raw-trace access, ran before the next proposer formed its diagnostic question, and supplied no demonstrated scoped mechanism or review operation. The full-trace arm also bundled raw traces with short causal reports. The contrast therefore rejects that summarize-and-discard treatment in the reported setup. It does not identify an episode-backed theory constructed for a named decision or show whether such a theory helps a later improvement episode. A credible Exo treatment must preserve the source episodes and measure the theory's marginal effect.

## Unresolved gaps

1. **Occurrence:** The reviews establish write paths, not a live episode in which objective-relevant evidence produced a beneficial Exo self-change that later behavior used.
2. **Selection theory:** No inspected result establishes a policy that distinguishes promotable experience from fluent low-value lessons or chooses the right retained form.
3. **Revision surface:** Broad mutability does not show that Exo represents every behavior-shaping relation or can detect a bad decomposition of its improvement process.
4. **Compounding:** No Exo result measures a later improvement episode and traces its dependence on an earlier retained benefit.
5. **Marginal value:** No result compares current Exo with the same system plus explicit theory after full lifecycle costs.
6. **Open oracle:** Positive semantic-memory results rely on benchmark success signals; Exo's most consequential self-theories may concern judgment quality without a cheap oracle.
7. **Formation:** A model can produce post-hoc, overbroad, or self-flattering explanations. Structure and review may reduce this failure without solving it.
8. **Activation:** A correct retained artifact that is not retrieved and causally used has no behavioral value.
9. **Freshness:** A self-change can invalidate a theory about the system, allowing a stale theory to conceal its own error.
10. **Cost:** Selection, review, routing, and maintenance may cost more than reconstruction, especially as model capability improves.
11. **Commitment versus cache:** Recomputable views and authoritative records of unentailed choices require different invalidation and retention policies.
12. **Evaluation governance:** Exo does not yet expose one contract that keeps an evaluator independent of the active candidate while allowing separate, between-episode revision.

## Falsifiers and revision triggers

Reject or narrow the proposal if canonical Exo or ExoWorker—with existing facts, skills, symbolic self-modification, heuristics, and episode access—matches or exceeds the explicit-theory treatment on later improvement productivity after full cost accounting.

Also narrow it if:

- retained theories are rarely retrieved, or retrieval does not change later search, evaluation, evidence acquisition, interpretation, or retention;
- named revision machinery enables no correction that ordinary source inspection and just-in-time reasoning miss;
- stale theories, overgeneralization, self-flattering rationales, or context interference erase the measured gains;
- a stronger model reconstructs the relevant theories with negligible variance and no material transfer or coordination loss;
- no explicit policy selects valuable lessons or revision targets better than unconstrained model judgment; or
- another substrate provides comparable semantic identity, scope, criticism, revision, lineage, activation, and bounded validation without maintained natural-language theories.

Keep any compounding claim local unless later episodes repeatedly show causal dependence. A useful lesson, successful tool, broader revision surface, or repeatable rewrite path remains compatible with accumulation without compounding.
