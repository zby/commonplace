# Exo evidence and counterevidence

> **Track context:** This is the evidence ledger for the [Exo-facing invitation](./for-exo-authors.md), within the broader [explanatory-theories deployment-time-learning workshop](./README.md).

This document separates facts about pinned Exo and ExoWorker, classifications grounded in those facts, theoretical inferences, later-episode evidence, evidence for semantic retention, adverse results, unresolved gaps, and falsifiers. It is an argument ledger, not a verification protocol.

## Pinned Exo and ExoWorker facts

Evaluation boundary: canonical Exo main commit `ef4cfe057af0` and the separately linked ExoWorker branch commit `ed08a571`. The [whole-system analysis](../../agentic-systems/exo.md) is refreshed to the same `ef4cfe0` pin. The [memory-system review](../../agent-memory-systems/reviews/exo.md) remains pinned to the earlier `baa07f67`, so unchanged memory claims rely on it while refreshed claims below come from the checkout diff and branch inspection. Neither review ran a live Exo instance.

| Working claim | Evidence status | Basis |
|---|---|---|
| Exo's source tree and self map provide a causally connected self-representation of the mutable executor | Structural classification grounded in code and docs | The agent can inspect the mounted repository and checked-in `SELF.md`, edit the organization that assembles prompts and tools, then rebuild and restart it into later operation |
| Exo preserves ordered event history across sandbox rewind | Code-grounded, unchanged | The Rust substrate keeps canonical events outside the rewound sandbox; refreshed lifecycle docs add attach/detach events without changing the invariant |
| The agent can modify symbolic behavior and retain accepted changes | Code-grounded capability, strengthened | Repository mount, shell, git, tests, prompts, executor, rebuild/rollback, and managed tools from local source or an exact Git commit |
| Exo retains natural-language memory, skills, prompts, a self map, and update reasons | Code-grounded capability, strengthened | Memory and skill surfaces remain; `rebuild_and_restart_exo` now stores a free-text reason with update identity, state, timestamps, and outcome |
| ExoWorker tells the agent to persist learnings in several forms | Code-grounded on the linked branch | Its prompt maps lasting facts to `remember`, reusable playbooks to `install_skill`, and repeated helpers to `install_agent_tool`; memory explicitly includes lessons from failures |
| ExoWorker expresses a primitive theory of promotion | Interpretation grounded in ExoWorker's instructions | The mapping is a form-selection heuristic; it does not generally estimate later improvement value, assign evidentiary authority, or state invalidation conditions |
| Exo exposes a broad revision envelope | Code-grounded capability | Executor source, prompts, tools, tests, adapters, memory, skills, and the self map are inspectable and mutable; the Rust substrate is protected by default policy |
| A particular Exo path keeps its redesign class open to another revision | Supported prospectively, not observed across episodes | Rebuild/restart returns to an editable source tree and the managed-tool replacement path survives an install; no inspected run traces a successor through a second improvement episode |
| Exo accumulates beneficial improvements in operation | Unestablished by the pinned review | Code establishes persistence, loading, installation, and later availability; it does not establish benefit or faithful behavioral use in a live instance |
| One Exo improvement has helped produce a later improvement | Unestablished | No inspected record measures a later improvement episode or traces its dependence on an earlier retained benefit |
| Exo's current mechanical oracles establish judgment improvement | Negative at refreshed main | Build, tests, restart outcome, and logs reject mechanical failures but can admit semantic degradation; the cloned-sandbox canary remains future work |
| Canonical Exo automatically extracts and evaluates lessons from traces | Negative at refreshed main | Memory and skill implementations remain deliberate write paths; the managed tool registry performs explicit install/remove operations and no added path mines the event log into accepted lessons |
| Canonical Exo still materializes its complete conversation history | Code-grounded, unchanged | `typescript/harness/index.ts` and the canonical turn loop still materialize all message and tool events with no implemented compaction or relevance selector |
| Exo relies on traces being sufficient for all semantic learning | Not an Exo-authored claim | This would be a caricature; the relevant baseline includes Exo's free-form memory, skills, prompts, tools, code, and capable model as well as episodes |

## What the refreshed article changes in the pitch

The original pitch centered the choice between episodes, natural-language lessons, and symbolic policy. The refreshed Exo already occupies all three forms. The updated argument therefore moves from **missing form** to **revision control and later productivity**.

The managed tool registry strengthens the baseline. Exo can retain symbolic adaptation with a stable id, pinned source, validation before installation, atomic replacement, and inspection. Any semantic layer must add value beside that capable path rather than comparing itself with weak or ephemeral tools.

The self-update reason and ExoWorker weaken a form-based claim further. Exo retains event-local reasons, free-form facts, and reusable skills. “Exo learns symbolically and needs natural language” is false as a system-level characterization.

They also expose the narrower opportunity. The pinned surfaces can voluntarily carry rich reasoning, but do not require source episodes, distinguish evidence from commitment, assign epistemic status, name affected authority paths, or connect a retained benefit to later improvement productivity. A rebuild reason is event-local. ExoWorker's heuristics do not make search, evaluation, promotion, and lifecycle one explicit revision surface.

The [reflective self-improvement article](../../articles/reflective-self-improvement.md) adds the decisive test. Retention, reuse, and task benefit can all be real without compounding. The pitch must ask whether an earlier benefit makes a later improvement cheaper, broader, more reliable, or less human-dependent, and it must trace the causal connection between episodes.

## Theoretical support

The revised argument composes the following claims:

- [Improvements can accumulate without compounding](../../notes/improvements-can-accumulate-without-compounding.md): retained gains compound only when their benefits feed into producing later improvements, directly or through observed reinvestment.
- [Compounding is tested in later improvement](../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md): the accepting metric tests the earlier change; compounding needs a displaced productivity measure and a causal trace in a later episode.
- [Reflection buys addressability](../../notes/reflection-buys-addressability.md): a reflective representation makes retained commitments and improvement machinery available for naming, criticism, selective revision, and transfer, but does not guarantee beneficial use.
- [Self-improvement is relative to a declared objective](../../notes/self-improvement-is-relative-to-a-declared-objective.md): boundary, horizon, and antecedent objective index each attribution; a candidate cannot supply the standard that licenses itself.
- [Learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): an optimizer can improve every exposed variable while remaining unable to express a consequential omission outside its effective update space.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md): pre-compute a known result when doing the work again inside each consuming call costs more than inserting it, while preserving a validity window and lineage.
- [Commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md): a decision or generalization not entailed by its sources cannot be recovered by recomputation; the committed artifact becomes authoritative for what it adds.
- [Retaining the episode keeps a distilled rule re-derivable](../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md): episode and rule are complementary; evidence and tacit residue remain available when the abstraction fails.
- [Theory-mediated self-improvement needs interpretation and retention](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md): a capable interpreter without retained theory re-derives each episode; retained theory without adequate interpretation can guide revision confidently in the wrong direction.
- [A repeatable operative path keeps a redesign class open to revision](../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md): representation, determination, admission, installation, later dependence, and continuity are distinct obligations; openness is weaker than compounding.

Together these notes establish a coherent candidate mechanism. They do not establish that Exo needs the proposed layer, that a model can form reliable self-theories, or that explicit theory improves later revision productivity.

## Evidence about later improvement

### HyperAgents supplies one local compounding link

The [HyperAgents ingest](../../sources/hyperagents.ingest.md) reports a transfer experiment in which evolved hyperagents from paper-review and robotics runs were frozen and used to generate agents for an unseen math-grading task. Across five runs, the transferred hyperagents produced stronger later agents than the initial hyperagent.

What it supports: an earlier retained improvement procedure can help produce improvements in a later, different-domain episode. Uptake is direct because the transferred procedure generates the later agents, and the later math-grading measure differs from the source-run target.

What it does not support: which bundled prompt, insight, and code changes caused the gain, an Exo-specific effect, a natural-language theory effect, or recurrent feedback. Continued evolution from transferred rather than fresh hyperagents showed no significant advantage, so sustained compounding remains unestablished.

### Nearby results stop short of the causal link

| Result | What it establishes | What remains missing |
|---|---|---|
| [Agent Optimizers](../../sources/agent-optimizers-compound-terminal-bench.ingest.md) | Retention, transfer to an expanded task set, and further optimization under RELAI-VCL | An equally budgeted later phase from a fresh artifact, or a reinvestment trace showing the first gain made the second phase more productive |
| [Co-Harness](../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) | Repeated exchange between checked harness edits, training trajectories, updated weights, and another harness round | A matched comparison separating feedback from the effect of additional training or search |
| [Knowledge-Centric Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Accumulation and transfer of natural-language knowledge across tasks and model families | A later curation episode in which an earlier retained benefit improves the productivity of knowledge revision |

These results make recurrent feedback plausible and provide pieces of a protocol. None establishes an Exo compounding pathway.

## Evidence for semantic retention and activation

### Trajectory-Informed Memory Generation

[The ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) reports a three-stage trajectory-to-tip system evaluated on AppWorld. Its best configuration—subtask-level natural-language tips with LLM-guided retrieval—improves held-out scenario goal completion by 14.3 percentage points, with larger gains on the hardest tasks.

What it supports: semantic work extracted from trajectories can alter later task behavior and transfer across tasks when recurring subtask structure and a clear completion oracle exist.

What it does not support: Exo-specific benefit, open-ended self-theory, lifecycle governance, superiority over equally budgeted Exo, or feedback from task benefit into later improvement.

### Knowledge-Centric Self-Improvement

[The ingest](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) covers a protocol in which disposable task agents contribute evidence to task and cross-task forums and a shared knowledge artifact is distilled into scoped guidance. Reported results improve solve rates across five benchmark families. Its strongest result for this workshop is held-out transfer: a frozen generation-10 artifact helps recipient agents on Polyglot and ARC-AGI-1 across donor–recipient model-family pairings.

What it supports: an external semantic artifact can carry reusable value independently of a persistent producing agent, including across model families; scoped claims can be challenged, split, and retained as rejections.

What it does not support: which curation component caused the gain, open-ended semantic correctness, the marginal value of governed conclusions beside Exo's existing layers, or later improvement productivity.

### Memento-Skills and the trace-learning corpus

[Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md) reports gains from evolving mixed natural-language-plus-code skill folders around a frozen model, especially where task structure recurs. The [trace-learning survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) finds repeated trace → extraction → promotion → reinjection architectures, with targets spanning rules, playbooks, skills, code, and weights.

What they support: readable semantic and symbolic artifacts are practical learning targets, activation matters, and recurrence bounds their value.

What they do not support: a universal preference for natural language, a general promotion theory, causal identification of the semantic layer, or compounding rather than task-side accumulation.

## Adverse evidence, correctly scoped

### Faithful Self-Evolvers is not Meta-Harness

[Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) evaluates ExpeL, Dynamic Cheatsheet, ReasoningBank, and G-Memory—not Meta-Harness. Across its tested frameworks, backbones, and environments, perturbing raw trajectories often harms performance while perturbing automatically condensed experience often has little effect. ReasoningBank supplies a condensed-only case, so raw episodes do not explain the whole result.

This is adverse evidence against assuming that written memory is operative. It does not test the full treatment proposed here:

- Its target is automatically condensed experience, not a reviewed semantic artifact with declared authority.
- The paper identifies semantic vagueness as a major failure; the tested items often do not state a precise claim, mechanism, and applicability boundary.
- Static or embedding-based insertion leaves content quality confounded with activation: a stored item can be present and still lose to current context and model priors.
- Some tested tasks are solvable from pretrained priors, making external memory unnecessary.
- The perturbation metric measures causal uptake, not truth, warrant, beneficial use, or later improvement productivity.
- The experiment does not compare an Exo-like baseline with free-form facts, skills, symbolic changes, and retained episodes against the same system plus an explicit revision theory and governed conclusions.

The [condensation-faithfulness workshop](../condensation-faithfulness-experiment/README.md) develops this defense. Its proposed treatment uses `Claim / Trigger / Mechanism / Scope / Form`, gate-checking, and an optional trigger-matched activation arm. [The condenser design](../condensation-faithfulness-experiment/condenser-design.md) records the most important constraint: ReasoningBank's native prompt already asks for concrete, actionable advice, reasons, and when not to apply it, yet its output remains inert. “Write a better summary” is not a defense. Any improvement must come from structure, enforcement, activation, and retained episode access.

Those defenses limit the paper's reach; they do not establish that the proposed treatment works. Its perturbation method remains a useful test of whether a retained artifact enters the causal path at all.

### Meta-Harness tests a different compression failure

[Meta-Harness](../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) is an outer-loop harness-code optimizer. In its text-classification ablation, a proposer with raw execution traces reaches 50.0 median accuracy, versus 34.6 with scores only and 34.9 with scores plus generated summaries. It is strong adverse evidence against replacing diagnostic episodes with consumer-blind summaries.

[The dedicated boundary note](../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) identifies why that ablation does not test episode-backed semantic theory:

1. Summaries replaced episodes instead of being retained beside them.
2. Summarization ran before the next proposer formed its diagnostic question and was consumer-blind.
3. The summaries had no demonstrated scoped-mechanism or reach-review operation.
4. A fixed hand-designed summarizer sat outside the search.
5. The full-trace arm bundled raw traces with short causal reports, while no traces-only/no-report arm isolated those reports' contribution.

The result rejects summarize-and-discard for that proposer, task, and compressor. It leaves unmeasured the marginal value of a post-attribution, reviewed conjecture linked back to retained episodes. It also leaves unmeasured whether that conjecture improves a later improvement episode rather than only the next task proposal.

## What the evidence requires

Any credible Exo treatment must:

- preserve raw episodes and symbolic artifacts as drill-down evidence;
- promote selectively rather than create a second lossy log;
- shape a conclusion for a future acting consumer, not generic readability;
- make trigger, mechanism, scope, status, provenance, and authority explicit where they affect later use;
- distinguish review or gate enforcement from exhorting a model to be concrete;
- keep the objective and comparison contract fixed independently of the candidate within an episode;
- test activation and faithful behavioral uptake rather than storage alone;
- measure task utility separately from later improvement productivity;
- trace direct use or actual reinvestment between improvement episodes; and
- count context, maintenance, staleness, distraction, over-application, and human judgment as costs.

These are constraints on a credible experiment, not evidence that the intervention will pay.

## Main unresolved gaps

1. **Occurrence gap.** The reviews establish code-grounded paths, not a live episode in which objective-relevant evidence produced a beneficial Exo self-change that later behavior used.
2. **Selection-theory gap.** No inspected result establishes a general policy that separates experience worth promoting from fluent low-value lessons or chooses the right retained form.
3. **Revision-surface gap.** Exo exposes broad mutability, but no inspected representation demonstrates that it covers every behavior-shaping relation or can detect a bad decomposition of its own improvement process.
4. **Compounding gap.** No Exo result measures a later improvement episode and traces its dependence on an earlier retained benefit.
5. **Marginal-value gap.** No result compares current Exo against the same system plus explicit revision theory and governed conclusions after full lifecycle cost accounting.
6. **Open-oracle gap.** Positive semantic-memory results rely on benchmark success signals; Exo's most interesting self-theories concern judgment quality without a cheap oracle.
7. **Formation gap.** A model can produce rationales that are post-hoc, overbroad, or flattering. Structure and review may reduce this without solving it.
8. **Activation gap.** A correct artifact that is not surfaced or causally used has no behavioral value and cannot contribute to compounding.
9. **Freshness gap.** Self-modification can invalidate conclusions about the system; a stale semantic layer may conceal its own error.
10. **Cost gap.** Selection, curation, routing, review, and maintenance may cost more than just-in-time reconstruction, especially as model capability improves.
11. **Commitment/cache mixture.** Some artifacts are recomputable views; others are authoritative records of unentailed choices. Treating both as disposable or both as permanent creates opposite maintenance failures.
12. **Evaluation-governance gap.** Keeping an evaluator revisable between episodes but fixed independently of the candidate within an episode requires a concrete authority path Exo does not yet specify as one contract.

## Falsifiers and revision triggers

The central claim should be weakened or rejected if the relevant baseline—canonical Exo or ExoWorker with its existing heuristics, facts, skills, symbolic self-modification, and episode access—matches or exceeds the explicit-theory arm on later improvement productivity after full cost accounting.

It should also be weakened if:

- retained theories are rarely retrieved or their retrieval does not change later search, evaluation, or retention;
- named revision machinery does not enable corrections that ordinary source inspection and just-in-time reasoning miss;
- the explicit layer increases stale-cache, overgeneralization, self-flattering-rationale, or context-interference failures enough to erase its gains;
- a stronger model reconstructs the relevant theories with negligible variance and no meaningful transfer or coordination loss;
- no explicit policy selects valuable lessons or revision targets better than unconstrained model judgment; or
- another substrate provides comparable semantic identity, scope, selective criticism, revision, lineage, activation, and bounded validation without maintained natural-language conclusions.

The compounding claim must remain local unless later episodes show causal dependence repeatedly. A useful lesson, a successful tool, a broader revision surface, and a repeatable rewrite path are all compatible with accumulation without compounding.
