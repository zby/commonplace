# Evidence and counterevidence

This document exposes the evidence behind the [short pitch](./README.md). It separates facts about pinned Exo, the linked ExoWorker variant, theoretical inferences, positive external results, adverse results, unresolved gaps, and falsifiers. It is an argument ledger, not a verification protocol.

## Pinned Exo and ExoWorker facts

Evaluation boundary: canonical Exo main commit `ef4cfe057af0` and the separately linked ExoWorker branch commit `ed08a571`. The [whole-system analysis](../../agentic-systems/exo.md) is refreshed to the same `ef4cfe0` pin; the [memory-system review](../../agent-memory-systems/reviews/exo.md) remains pinned to the earlier `baa07f67`, so unchanged memory claims rely on it while refreshed claims below come from the checkout diff and branch inspection.

| Working claim | Evidence status | Basis |
|---|---|---|
| Exo preserves ordered event history across sandbox rewind | Code-grounded, unchanged | Whole-system sections “The rewind preserves the record of what was tried” and “Control surfaces”; refreshed lifecycle docs add attach/detach events without changing the invariant |
| The agent can modify symbolic behavior and retain accepted changes | Code-grounded capability, strengthened | Repository mount, shell, git, tests, prompts, executor, and rollback paths now include a managed registry for validated tools from local source or an exact Git commit |
| Exo retains natural-language memory, skills, prompts, and a self map | Code-grounded, unchanged | Memory-system artifact analysis and read-back sections; main still registers these surfaces in the practical profile |
| ExoWorker tells the agent to persist learnings in several forms | Code-grounded on the linked branch | Its prompt maps lasting facts to `remember`, reusable playbooks to `install_skill`, and repeated helpers to `install_agent_tool`; its memory tool explicitly includes lessons from failures |
| Exo has a primitive theory of promotion | Interpretation grounded in those instructions | The mapping is an explicit form-selection heuristic, but it does not generally estimate reuse versus maintenance cost, assign evidentiary authority, or state invalidation conditions |
| Self-update records retain a natural-language reason | Code-grounded at refreshed main | `rebuild_and_restart_exo` asks for a short reason and stores it with update identity, status, timestamps, conversation/agent identity, and exit code |
| Canonical Exo automatically extracts and evaluates lessons from traces | Negative at refreshed main | Memory and skill implementations are unchanged; the new tool manager performs explicit install/remove operations, and no added path mines the event log into accepted lessons |
| Canonical Exo still materializes its complete conversation history | Code-grounded, unchanged | `typescript/harness/index.ts` and the canonical turn loop were not changed by the refresh; all message and tool events remain the prompt view |
| Exo relies on traces being sufficient for all semantic learning | Not an Exo-authored claim | This would be a caricature; the pitch tests whether Exo's existing heuristics, natural-language artifacts, symbolic artifacts, and episodic reconstruction make a stronger promotion policy unnecessary |
| Exo's mechanical oracles do not establish judgment improvement | Code-grounded boundary, unchanged | Build, tests, restart outcome, and logs reject mechanical failures but can admit semantic degradation; Exo still names a cloned-sandbox canary as future work |

## What the refresh changes in the argument

The managed tool registry strengthens the control case. Exo can retain symbolic adaptation with a stable id, pinned source, validation before installation, replacement semantics, and inspection. Any semantic layer must add value beside that capable path rather than comparing itself with a weak or ephemeral tool baseline.

The self-update reason and ExoWorker weaken the original form-based pitch. Exo now demonstrates two kinds of natural-language retention: event-local reasons attached to mutations and agent-authored facts or skills meant to survive across work. “Exo learns symbolically and needs natural language” is therefore false as a system-level characterization.

They also expose the narrower gap. A rebuild reason is not independently scoped, reviewed, activated, or invalidated. ExoWorker's memory record has id, text, and creation time; its skill has a name, description, body, files, and install/update times. These surfaces can voluntarily carry rich reasoning, but the system does not require source episodes, distinguish evidence from commitment, assign epistemic status, or connect changes in the referent to revalidation. The pitch is now about whether making that selection and lifecycle explicit is worth its cost.

## Theoretical support

The argument composes several existing claims:

- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md): pre-compute a known result when doing the work again inside each consuming call costs more than inserting it, while preserving a validity window and lineage.
- [Commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md): a decision or generalization not entailed by its sources cannot be recovered by recomputation; the committed artifact becomes authoritative for what it adds.
- [Retaining the episode keeps a distilled rule re-derivable](../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md): episode and rule are complementary; evidence and tacit residue stay available when the abstraction fails.
- [Theory-mediated self-improvement needs interpretation and retention](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md): a capable interpreter without retained theory re-derives each episode and cannot selectively accumulate or revise named theories.
- [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md): natural-language and symbolic artifacts form a coupled deploy-time learning surface, with movement across the codification boundary.

These notes establish a coherent retention mechanism, not a reliable theory for selecting what deserves promotion or the empirical payoff for Exo. Both remain open claims.

## Positive external evidence

### Trajectory-Informed Memory Generation

[The ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) reports a three-stage trajectory-to-tip system evaluated on AppWorld. Its best configuration—subtask-level natural-language tips with LLM-guided retrieval—improves held-out scenario goal completion by 14.3 percentage points, with larger gains on the hardest tasks.

What it supports: semantic work extracted from trajectories can alter later behavior and transfer across tasks when recurring subtask structure and a clear completion oracle exist.

What it does not support: Exo-specific benefit, open-ended self-theory, lifecycle governance, or superiority over equally budgeted Exo with its existing memory, skills, symbolic adaptations, and episodes.

### Knowledge-Centric Self-Improvement

[The ingest](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) covers a protocol in which disposable task agents contribute evidence to task and cross-task forums and a shared knowledge artifact is distilled into scoped guidance. Reported results improve solve rates across five benchmark families. Its strongest result for this workshop is held-out transfer: a frozen generation-10 artifact helps recipient agents on Polyglot and ARC-AGI-1 across donor–recipient model-family pairings.

What it supports: an external semantic artifact can carry reusable value independently of a persistent producing agent, including across model families; scoped claims can be challenged, split, and retained as rejections.

What it does not support: which curation component caused the gain, open-ended semantic correctness, or the marginal value of governed conclusions beside Exo's existing natural-language, symbolic, and episodic layers.

### Memento-Skills and the trace-learning corpus

[Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md) reports gains from evolving mixed natural-language-plus-code skill folders around a frozen model, especially where task structure recurs. The [trace-learning survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) finds repeated trace → extraction → promotion → reinjection architectures, with promotion targets spanning rules, playbooks, skills, code, and weights.

What they support: readable semantic and symbolic artifacts are already practical learning targets, and recurrence is a boundary on their value.

What they do not support: a universal preference for natural language, or causal identification of the semantic layer independently of routing, evaluation, and symbolic changes.

## Adverse evidence, correctly scoped

### Faithful Self-Evolvers is not Meta-Harness

[Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) evaluates ExpeL, Dynamic Cheatsheet, ReasoningBank, and G-Memory—not Meta-Harness. Across its tested frameworks, backbones, and environments, perturbing raw trajectories often harms performance while perturbing automatically condensed experience often has little effect. ReasoningBank supplies a condensed-only case, so raw episodes do not explain the whole result.

This is adverse evidence against assuming that written memory is operative. It does not test the treatment proposed here:

- Its target is automatically condensed experience, not a reviewed semantic artifact with declared authority.
- The paper identifies semantic vagueness as a major failure; the tested items often do not state a precise claim, mechanism, and applicability boundary.
- Static or embedding-based insertion leaves content quality confounded with activation: a stored item can be present and still lose to current context and model priors.
- Some tested tasks are solvable from pretrained priors, making any external memory unnecessary.
- The perturbation metric measures causal uptake, not truth, warrant, or beneficial use.
- The experiment does not compare an Exo-like baseline with free-form facts, skills, symbolic changes, and retained episodes against the same system plus an explicit promotion policy and source-linked, scoped, reviewed conclusions.

The [condensation-faithfulness workshop](../condensation-faithfulness-experiment/README.md) develops this defense in detail. Its proposed treatment uses `Claim / Trigger / Mechanism / Scope / Form`, gate-checking, and an optional trigger-matched activation arm. [The condenser design](../condensation-faithfulness-experiment/condenser-design.md) records the most important constraint: ReasoningBank's native prompt already asks for concrete, actionable advice, reasons, and when not to apply it, yet its output remains inert. “Write a better summary” is not a defense. Any improvement must come from structure, enforcement, activation, and retained episode access.

The defenses limit the paper's reach; they do not establish that the proposed treatment works. That is why the workshop preserves its perturbation test as a useful evaluation method.

### Meta-Harness tests a different compression failure

[Meta-Harness](../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) is an outer-loop harness-code optimizer. In its text-classification ablation, a proposer with raw execution traces reaches 50.0 median accuracy, versus 34.6 with scores only and 34.9 with scores plus generated summaries. It is strong adverse evidence against replacing diagnostic episodes with consumer-blind summaries.

[The dedicated boundary note](../../notes/the-meta-harness-ablation-bounds-summarization-not-theory-formation.md) identifies why that ablation does not test episode-backed semantic theory:

1. Summaries replaced episodes instead of being retained beside them.
2. Summarization ran before the next proposer formed its diagnostic question and was consumer-blind.
3. The summaries had no demonstrated scoped-mechanism or reach-review operation.
4. A fixed hand-designed summarizer sat outside the search.
5. The full-trace arm bundled raw traces with short causal reports, while no traces-only/no-report arm isolated those reports' contribution.

The result rejects summarize-and-discard for that proposer, task, and compressor. It leaves unmeasured the marginal value of a post-attribution, reviewed conjecture linked back to retained episodes.

## What the adverse evidence requires

The pitch inherits real design obligations from both results:

- Preserve raw episodes and symbolic artifacts as drill-down evidence.
- Promote selectively; do not create a second lossy log.
- Shape a conclusion for a future acting consumer, not for generic readability.
- Make trigger, mechanism, scope, status, and provenance explicit.
- Treat review or gate enforcement as different from exhorting a condenser to “be concrete.”
- Test activation and behavioral uptake, not storage alone.
- Measure utility separately from faithfulness and correctness.
- Count context, maintenance, staleness, distraction, and over-application as costs.

These are constraints on a credible semantic cache, not evidence that it will pay for Exo.

## Main unresolved gaps

1. **Selection-theory gap.** No inspected result establishes a general policy that reliably separates experience worth promoting from fluent but low-value lessons, or chooses the right retained form.
2. **Marginal-value gap.** No inspected result cleanly compares Exo's existing facts, skills, symbolic learning, and episodes against the same system plus explicit promotion policy and governed conclusions.
3. **Open-oracle gap.** Positive results rely on benchmark success signals; Exo's most interesting self-theories concern judgment quality without a cheap oracle.
4. **Formation gap.** A model can produce rationales that are post-hoc, overbroad, or flattering. Structure and review may reduce this without solving it.
5. **Activation gap.** A correct artifact that is not surfaced or causally used has no behavioral value.
6. **Freshness gap.** Self-modification can invalidate conclusions about the system; a stale semantic cache may conceal its own error.
7. **Cost gap.** Selection, curation, and maintenance may cost more than just-in-time reconstruction, especially as model capability improves.
8. **Commitment/cache mixture.** Some artifacts are recomputable views; others are authoritative records of unentailed choices. Treating both as disposable caches or both as permanent ground truth creates opposite maintenance errors.

## Falsifiers and revision triggers

The central claim should be weakened or rejected if Exo's existing promotion heuristics, facts, skills, symbolic self-modification, and episode retrieval:

- matches or exceeds the semantic-cache arm after full cost accounting;
- reconstructs relevant lessons with negligible variance and no meaningful transfer loss;
- maintains current self-understanding without named semantic objects; or
- avoids stale-cache and overgeneralization failures that erase the semantic arm's gains.

The promotion claim must also be revised if no explicit theory can select valuable lessons better than unconstrained model judgment, or if another substrate provides comparable semantic identity, scope, selective criticism, revision, lineage, activation, and bounded validation without natural-language conclusions.
