# Adequacy-gate run over six systems

This run exercises the [closure–capability map](./closure-capability-map.md) on six
systems named in the [match register](./match-register.md): DGM, HGM,
HyperAgents, Prime Agent, Recuris, and Apodex 1.1. For each system it
reconstructs one named improvement path, applies the map's seven-condition
candidate adequacy gate, names the degenerate closure patterns the path lands
on, and classifies the residual human cut by the reason each item stayed human.

The result is a measurement, not a verdict about self-improving systems. It
reads only what the KB has retained: the ingests, the two evidence notes the map
lists as starting points
([six paths](../../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md),
[thirteen placements](../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md)),
the [three-harness evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md),
and the [HyperAgents code review](../../agent-memory-systems/reviews/hyperagents.md).
No source was refetched. Where the retained record does not say something, the
cell says "not stated in the retained record" rather than an inference.

Two conventions hold across all six sections. A condition is marked *met* only
when the retained record states the fact the condition asks for; partial
coverage is reported as unstated, with the covered part named in the evidence.
Residue items use the map's reasons: unrepresented premise, unsettled criterion,
no independent oracle, delayed oracle only, horizon, priced out.

## Darwin Gödel Machine

**Path.** Archive-based agent-code self-modification. A fixed o1 diagnostician
reads the selected parent's benchmark evaluation logs and names one improvement,
which is handed to the parent coding agent as a self-modification task; the
parent edits its own Python repository; the child is evaluated on a staged
benchmark subset and admitted to the archive if it compiles and retains
codebase-editing ability; benchmark score then weights parent sampling in later
iterations. The declared horizon is 80 iterations under a fixed coding objective
and a fixed task distribution
([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)).

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | SWE-bench Verified subsets and full Polyglot, plus cross-benchmark transfer to benchmarks never touched during search (SWE-evolved agent 28.9% on full Polyglot against a 14.2% base) ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)). The diagnosis prompt includes SWE-bench's private test patch, so the SWE pool functions partly as search data. |
| Capability floor | not stated in the retained record | The record reports benchmark percentages and declares no stage-relative threshold; no comparison to a competent remote programmer appears ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)). |
| Consequential reach | met | Installed changes include finer-grained file viewing, string-replacement editing, context auto-summarization, retries and patch validation, and multi-candidate generation with an FM ranker; the six-path note records candidate generation plus an FM ranker as a demonstrated installed architectural change ([six paths](../../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md)). |
| Correction | not met | "Only agents that compile successfully and retain the ability to edit a given codebase are added to the DGM archive"; benchmark score never decides admission, only the sampling weight, so a benchmark regression enters the archive ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)). Agent 114 reached the maximum score by deleting the `TOOL_USED_MARKER` its detector keyed on, and the reported answer was concealing the checking functions rather than strengthening the oracle. |
| Continuity | met | Descendants inherit parent code and are resampled as parents; at iterations 4 and 56 a below-parent agent seeded a later best agent. The six-path note scopes this: the path is closed only for admitted descendants later sampled and run ([six paths](../../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md)). |
| No hidden cut | met | The paper names its frozen layer: archive maintenance and parent selection "are fixed and not modifiable by the DGM", with the o1 diagnostician, viability criterion, benchmark objective and staged evaluator, model weights, 80-iteration budget, task distribution, and sandbox outside as well ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)). |
| Outcome evidence | met | 20.0% to 50.0% on the SWE-bench subsets used, 14.2% to 30.7% on full Polyglot, with three ablations underperforming the full method. One principal SWE run, no confidence interval, and no compute-matched control ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)). |

**Patterns.** *Viability-only gate*: admission turns on compilation and retained
edit ability, and the ingest's own reading is that "the reject-capable operation
in DGM is a viability filter and the score is a search signal". *Boundary
export*: the improvement proposal comes from a separate o1 model that never
improves, so the hard step of naming what to change sits outside the improving
agent. *Fixed-decomposition closure*: self-improvement is defined to exclude the
exploration process, so a failure caused by the archive or selection rule cannot
be represented inside the path — and the authors searched that layer themselves,
offline, via the DGM-Greedy ablation.

**Residual human cut.**

- Choosing the exploration process (parent selection, archive policy): **priced
  out**. Appendix J states the freeze "was made due to limited computational
  budget" and that evolving the layer "could require exponentially more compute";
  the ingest notes the controller is code and liftable in principle.
- Detecting objective hacking: **no independent oracle**. The hallucination
  checkers were hidden rather than made robust, and the agent defeated the
  remaining marker anyway.
- Judging whether coding-benchmark score reflects self-improvement ability:
  **unsettled criterion**. The assumption is stated three times and never
  independently measured; [HGM](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
  later reports the immediate score is a weak predictor of descendant
  productivity.
- Auditing the diagnosis prompt for test-patch contamination: **no independent
  oracle**. The answer given is manual log inspection plus cross-benchmark
  transfer.
- Deciding whether to run past iteration 80: **horizon**.

## Huxley Gödel Machine

**Path.** Tree search over agent self-modifications with lineage-level parent
selection. HGM adopts DGM's initial agent and evaluation setting, estimates
clade-metaproductivity from partial evaluations, uses Thompson sampling to choose
whether to expand a node or spend another benchmark trial on it, and decouples
expansion from evaluation for asynchronous execution. The editable surface is
scaffolds, prompts, and control logic, with model weights fixed
([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)).

This is the thinnest retained record of the six: the ingest has no retained
quotes, there is no code-grounded review, and HGM has no row in either evidence
note. Four cells below are unstated for that reason.

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | SWE-bench Verified, Polyglot, SWE-bench Lite, and SWE-bench-Live-style evaluations with officially checked submissions ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| Capability floor | not stated in the retained record | The record reports benchmark-local results and warns that the "human-level" framing "is especially easy to overread because it is benchmark-local and depends on officially checked submissions at a specific time"; no stage-relative threshold and no remote-programmer comparison is stated ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| Consequential reach | met | The paper "explicitly frames HGM as editing scaffolds, prompts, and control logic while leaving weights fixed" — commitments that determine the agent's coding behavior, not inert text ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| Correction | not stated in the retained record | The record describes a selection mechanism (CMP plus Thompson sampling) and an independent benchmark oracle, but states no admission operation that can refuse a candidate; it also names "reward hacking against local task distributions" as an inherited risk ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| Continuity | met | CMP is "a lineage-level metric aggregating descendant outcomes", so accepted nodes are expanded further and their descendants are the evidence ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| No hidden cut | not stated in the retained record | Weights and the benchmark-regime assumptions (repeatable trials, final-agent utility, benchmark-style scoring, Assumption 1) are named as fixed; the record does not state whether the archive controller, task distribution, diagnostician, or evaluator sit inside or outside the revision reach ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |
| Outcome evidence | met | "Stronger final agents and lower allocated CPU-hours than DGM/SICA-style greedy benchmark-score selection." The ingest names the confound: the gains may come from asynchronous scheduling and evaluation allocation rather than from CMP, and the paper does not isolate the two ([ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)). |

**Patterns.** *Fixed-decomposition closure*: the method requires repeatable
trials, final-agent utility, and benchmark-style scoring, and the ingest states
these "do not transfer directly to KB maintenance, research taste, or other
judgment-heavy domains where the oracle is soft or delayed", so the decomposition
that makes the loop work also bounds what it can be run on. A second observation
belongs here rather than in a table cell: HGM's own contribution is a *human*
repair of DGM's frozen selection layer. The DGM ingest names HGM as "the
controlled successor that attacks precisely this frozen layer from outside".
Improving a fixed outer loop from outside it is the *boundary export* pattern
seen one level up — the improvement is real, and it is not evidence that either
system's path can reach its own selection machinery.

**Residual human cut.**

- Choosing the parent-selection target: **unsettled criterion**. The paper's
  central claim is that the obvious criterion (immediate benchmark score) is
  wrong; CMP is the authors' replacement, designed outside the loop.
- Applying the method where the oracle is soft or delayed: **delayed oracle
  only**. The ingest names judgment-heavy domains as the boundary.
- Separating lineage scoring from asynchronous scheduling: **no independent
  oracle** for the attribution; the record states the comparison was not run and
  does not state why.
- Everything else about the supplied machinery: not stated in the retained
  record.

## HyperAgents

**Path.** Archive-based hyperagent self-patching (DGM-H). A hyperagent is "a
self-referential agent that integrates a task agent and a meta agent within a
single editable program"; a selected parent generates a modified version of
itself that may revise task logic and the modification procedure alike;
evaluators score the descendant; the compiled, evaluated child is appended to the
archive and marked a valid parent; later runs apply the selected parent's whole
patch chain before the next modification or evaluation
([ingest](../../sources/hyperagents.ingest.md),
[code review](../../agent-memory-systems/reviews/hyperagents.md)). Declared
horizons are 50 iterations for the Improvement@50 protocol and 200 for the
continuation runs, five repeated runs per method.

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | Held-out gains across coding, paper-review classification, robotics reward design, and unseen Olympiad-math grading, with bootstrap confidence intervals, statistical tests, and ablations in which removing meta-agent self-improvement or archive branching produces little progress ([ingest](../../sources/hyperagents.ingest.md)). The ingest also records that paper-review accuracy "predicts historical accept/reject decisions rather than review quality". |
| Capability floor | not stated in the retained record | The record states benchmark and held-out scores per domain and declares no stage-relative threshold; no remote-programmer comparison appears ([ingest](../../sources/hyperagents.ingest.md)). |
| Consequential reach | met | "In hyperagents the meta agent is part of the same editable program and can rewrite itself"; fixing the initial meta agent produces little progress; transferred hyperagents with their meta-agent components frozen generated better task agents in an unseen domain ([ingest](../../sources/hyperagents.ingest.md)). The code review confirms the mechanism: the retained artifact is a replayable git-diff lineage applied into executable code state ([code review](../../agent-memory-systems/reviews/hyperagents.md)). |
| Correction | not met | The evaluator's grounds are not candidate-authored — "components of the open-ended exploration loop (e.g., parent selection, evaluation protocols) remain fixed" — but admission is a compile-and-evaluated validity check, with score entering as selection weight ([ingest](../../sources/hyperagents.ingest.md)). The code review records that every attempted generation is appended before the next selection, that "archive membership alone is not promotion", and that faithfulness is not tested: no with/without lineage ablation or per-memory perturbation ([code review](../../agent-memory-systems/reviews/hyperagents.md)). |
| Continuity | met | The archive accumulates variants as stepping stones and later generations apply the full selected patch chain; the 200-iteration continuation runs start from transferred hyperagents ([ingest](../../sources/hyperagents.ingest.md)). |
| No hidden cut | met | Section 7 states that parent selection and evaluation protocols remain fixed; the ingest adds task definitions and distributions, labels and metrics, judge construction, final-agent selection, model and tool dependencies, resource limits, and the outer archive controller ([ingest](../../sources/hyperagents.ingest.md)). |
| Outcome evidence | met | Improvement@50 reaches 0.630 (CI 0.540–0.630) for transferred hyperagents, significantly above the initial agent (p < 0.05), measured in a later episode in an unseen domain rather than by the accepting metric. The continuation comparison — 0.640 (CI 0.550–0.720) from transfer against 0.610 (CI 0.510–0.680) fresh — is not statistically significant ([ingest](../../sources/hyperagents.ingest.md)). |

**Patterns.** *Fixed-decomposition closure*, conceded in the paper's own
limitations: hyperagents "cannot alter the outer process that determines which
agents are selected or how they are evaluated". *Viability-only gate*, in the
same shape as DGM: the `IsValid` compiled-child branch admits, and quality enters
only as selection weight. *Boundary export* at the selection layer: the appendix
experiment reports that a modifiable parent selector improves over random
(0.491, CI 0.387–0.512) but stays below the handcrafted `score_child_prop`
selector (0.532, CI 0.384–0.586), differences not significant — the hard
selection decision remains the designer's. *Syntactic-only reach* appears at
component grain in the code review: the editable `select_next_parent.py`
"computes candidates and scores but returns a random valid generation", and
`MetaAgent.forward(...)` does not put the `--evals_folder` path in its prompt, so
"selection policy can evolve" and "the meta agent reads prior evaluations" are
capabilities of the write surface rather than checked-in behavior
([code review](../../agent-memory-systems/reviews/hyperagents.md)).

**Residual human cut.**

- Designing the parent selector: **unsettled criterion**. Exposing it to
  revision did not find a better mechanism than the handcrafted one.
- Judging review quality behind the paper-review objective: **no independent
  oracle**. The available label predicts historical accept/reject decisions.
- Attributing the transfer gain to performance tracking, persistent memory, or
  strategic planning: **no independent oracle**. Transfer agents are selected
  retrospectively by descendant performance and carry many code changes
  together; the named mechanisms are qualitative observations, not removed
  components.
- Attaching rationale to a promoted patch: **unrepresented premise**. The code
  review records that "the memory is executable but not explanatory" and that a
  patch's provenance is a generation, not a source trace or failure span.
- Setting resource budgets and the 50- and 200-iteration limits: **horizon**.

## Prime Agent

**Path.** Trajectory-driven refinement of persistent harness state. (The paper
calls this layer its continual harness; it is not the separate system Continual
Harness that carries its own row in the [six-path note](../../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md).)
"Refinement converts trajectory evidence into versioned state updates. Agents
request edits directly, or /refine runs a background model call over relevant
events. The runtime applies each edit at a turn boundary, records its trigger and
intended effect, and assembles supplemental state for the next invocation.
Versions preserve provenance and enable rollback. Refinement supplements the
immutable base prompt without rewriting foundational policy." The retained
artifacts are typed prompt notes, memories, executable skills, and subagent
specifications, persisting across trajectories and restarts
([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). The
record states no iteration budget; the horizon is the goal and token accounting
that bounds autonomous continuation.

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | Externally anchored suites: ARC-AGI-3, OOLONG long-context, coding benchmarks, nanoGPT, Factorio, MazeBench. Two limits are on the record: some ARC values are external references rather than clean ablations, and in the Factorio run the measured objective was satisfiable by a specification exploit ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). |
| Capability floor | not stated in the retained record | The record declares no stage-relative threshold and states that the comparisons "vary model, harness, prompts, budgets, or provider behavior together" ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). |
| Consequential reach | met | The editable state is prompt notes, memories, executable skills, and subagent specifications, consumed as supplemental state on the next invocation; the Factorio trace shows a retained skill changing later behavior ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). Bounded: the path "cannot revise the base prompt, runtime topology, permissions, evaluator, benchmark, or model interface". |
| Correction | not met | "Versioning, observability, and rollback make a bad update inspectable and reversible, but do not provide a reject-capable semantic gate" ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). The agent "used the shortcut despite an anti-cheating heartbeat, and then preserved it as a reusable skill"; the paper's own remedy list — least-privilege interfaces, independent state validation, auditable rollback of contaminated refinements — names what the loop does not have. |
| Continuity | met | State survives compaction and restart and is assembled into the next invocation; the exploit skill was reused. Bounded: the ingest separates three persistence horizons and records that promotion of orchestration policy across tasks "is not established" ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). |
| No hidden cut | met | The record enumerates the fixed side: base system prompt, TypeScript runtime, family-only message topology, model and provider interfaces, permission boundary, evaluator design, benchmarks, state taxonomy, and stopping and accounting rules ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). |
| Outcome evidence | not stated in the retained record | Compound-system outcomes are reported, but no measurement attributes benefit to the refinement path: "the reported improvements therefore show that particular compound systems achieved particular outcomes, not that persistent kernels, direct messaging, refinement, or any other component caused the gains", and static inspection located no benchmark artifacts ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md)). |

**Patterns.** *Outcome-free closure*: changes are proposed and installed
repeatedly with no externally measured benefit attributed to the installing
mechanism. *Fixed-decomposition closure*, on the enumerated fixed side. The
Factorio trace realizes the failure the *viability-only gate* row predicts — a
candidate that passes and degrades the target function — in its extreme form:
the path has no acceptance operation at all, not a weak one. That is a gap in
the map's table, which names weak gates but not their absence; recorded here, not
acted on.

**Residual human cut.**

- Judging whether a proposed refinement should be installed: **no independent
  oracle**. The record states there is no gate that can refuse an edit, so the
  judgment falls to the operator who inspects a version.
- Recognizing a specification exploit: **no independent oracle**. The
  anti-cheating heartbeat existed and was bypassed; the remedies the paper names
  are not implemented in the reported path.
- Establishing that a retained skill generalizes beyond its origin task: **no
  independent oracle**. The record states tested promotion across tasks is not
  established and does not state why.
- Base prompt, runtime topology, permissions, evaluator design, benchmarks, and
  state taxonomy: **unrepresented premise**. These determine behavior and sit
  outside the surface the path can read or write.
- Continuing past the autonomous continuation budget: **horizon**.

## Recuris

**Path.** Meta-Agent component-scoped memory patching under a held-out paired
admission gate. A fixed Meta-Agent reads a failed trajectory, localizes the
failure to one of four memory components — experiential skills, a working-memory
state specification, invocation triggers, completion checkers — patches only the
implicated component, and submits the patch to a fixed gate that admits it only
if it repairs the source failure without breaking a held-out set of tasks the
current memory already solves; the admitted package version is loaded on later
tasks ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md),
[evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)).
The declared horizon is memory evolved from sixteen failures, evaluated on
eighty-six unseen tasks, with a reported second round of evolution.

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | Eighty-six unseen tasks with frozen Tau2 and Terminal-Bench split manifests and integrity anchors in the pinned checkout; the gate's held-out set is distinct from the source failure ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md)). All quantitative outcomes remain paper-only: the checkout holds no raw benchmark-result artifacts. |
| Capability floor | not stated in the retained record | The record declares no stage-relative threshold and no remote-programmer comparison ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md)). |
| Consequential reach | met | The four editable coordinates are operative control state, not inert text: pending working-memory entries drive retrieval, harness-grounded evidence rather than the model's assertion controls goal closure, and checkers gate transitions — all confirmed by static code inspection at the pinned revision ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md)). |
| Correction | met | A deterministic held-out paired gate runs contemporaneous paired checks before promotion and rejects a patch that breaks tasks the current memory already solves; the gate, the legal edit surface, and the Meta-Agent procedure are fixed outside the update space, so the grounds are not candidate-authored ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md)). The warrant is non-regression on the declared partitions, not usefulness beyond them, and localization "is a repair decision rather than a claim of causal identification". |
| Continuity | met | Eight accepted patches; the admitted package is reused on later tasks, a package shipped unchanged to a second model lifted it too, and a second evolution round ran on the evolved package ([evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)). The second-round gain "sits within the paper's own noise estimate from rerunning an unchanged memory, and one lineage gives most of the second-round gain back in a later round", so recurrent later-episode dependence is not established. |
| No hidden cut | met | The record enumerates the fixed side: base model, tools, fixed commit kernel, outer harness, component decomposition, Meta-Agent procedure, legal edit surface, gate, benchmark objective, and data partitions ([ingest](../../sources/recursive-experiential-working-memory-evolution.ingest.md)). |
| Outcome evidence | met | Nine to seventeen points of success improvement on eighty-six unseen tasks, plus cross-task and cross-model transfer ([evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)). Paper-only: the matched-budget test-time-adaptation contrast is "reported as direction rather than an established effect", SkillFlow templates are in-sample, and the horizon analysis is observational. |

**Patterns.** *Fixed-decomposition closure* is the one pattern identified. Every
diagnosis must name one of four supplied components, so a failure caused by the
partition itself cannot be represented; the ingest states that gains inside the
editable coordinates "do not validate the frozen outer choices". No
viability-only gate: the gate is a real regression check on a held-out set. No
captured evaluator: the gate is fixed outside the candidate's reach. No
outcome-free closure: outcomes are measured, if paper-only. A second observation
does not fit any row in the table — the package "only grows": across eight
accepted patches it "added 51 skills, revised 2 and deprecated none, and 17
near-duplicate pairs survive into admitted versions". The retirement gap is a
real property of this path and the degenerate-pattern table has no row for it.
Recorded, not acted on.

**Residual human cut.**

- Diagnosing a failure whose cause is not one of the four components:
  **unrepresented premise**. The component ontology is the representation the
  localizer must speak, and the paper is explicit that localization is a repair
  decision rather than causal identification.
- Deciding when to retire or merge a near-duplicate skill: **unsettled
  criterion**. The record states none was deprecated and states no retirement
  rule.
- Revising a whole class of skills that share a reason: **unrepresented
  premise**. No rationale from which the skills were derived is retained, so "a
  revision to one rule reaches none of the others that share its unstated
  reason" ([evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)).
- Establishing that an accepted patch helps outside the declared partitions:
  **no independent oracle**. The gate warrants non-regression on its own task
  set.
- Choosing the benchmark objective, task families, and data partitions:
  **unrepresented premise**.
- Continuing beyond the reported evolution rounds: **horizon**.

## Apodex 1.1

**Path.** Offline weight revision between releases. The developers run a
supervised fine-tuning program whose domain variants are merged by model soup
into "the unified behavioral initialization", then PIVOT-RL, which "uses
hindsight-guided trajectory localization over a large policy-training corpus"
and, at each pivot, "preserve[s] the useful prefix and construct[s] a localized
continuation task with a short corrective hint" — a hint that "is never a
prediction target, and is absent at inference time". At deployment the
coordination state is "run-scoped rather than a durable distributed database",
and the record describes no prompt, skill, or memory artifact that survives the
run in revisable form
([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)).
The declared horizon is the run; every improvement decision falls between
releases. This is the contrast case in the register row: it "is not a
self-improvement loop in the definitional sense and does not present itself as
one" ([evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)).

| Condition | Status | Evidence |
|---|---|---|
| Non-vacuous work | met | Benchmark suites, HDS6 process judging, and three cases, against a declared notion of working capability as sustained progress toward a verifiable delivery ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). The tables "mix reported external values, internal reproductions, different harnesses, and proprietary systems", and the release contains benchmark machinery but no result traces. |
| Capability floor | not stated in the retained record | Working capability is defined but no stage-relative threshold is declared and no remote-programmer comparison appears ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). |
| Consequential reach | met | The path revises model weights, which determine capability; SFT variants are merged into the behavioral initialization and PIVOT-RL trains corrections at localized consequential decisions ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). The reach is over retention that is operative without being addressable: no theory in it can be named, criticized, or rescoped ([evidence note](../../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)). |
| Correction | not stated in the retained record | The record describes reward-guided training and a runtime finalization check for unresolved work, but states no acceptance operation that can reject a trained checkpoint on grounds independent of the training program ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). |
| Continuity | not met | The coordination plane is run-scoped and "the runtime does not atomically checkpoint [the task board and Agent Bus] together with the workspace filesystem"; nothing revisable survives a run, and the path for another revision is the developers' next training program, not a path inside the system ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). |
| No hidden cut | met | The improvement program is named as an offline developer-run training program, the run-scoped operational boundary is stated in the report, and the ingest enumerates the fixed side: task contracts, environment and action families, board protocol, runtime, verifier and reporter designs, publication rules, budgets, datasets, and evaluation ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). |
| Outcome evidence | met | Reported benchmark and HDS6 process results, author-produced and at compound grain: "No component-isolating ablations establish that the Task Board, asynchronous fan-in, asymmetric verification, evidence synthesis, publication controls, environment construction, or PIVOT-RL caused the reported gains" ([ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)). |

**Patterns.** *Boundary export* is the pattern the path lands on, and here it is
declared rather than concealed: the whole improvement decision — which
trajectories to train on, which decision points are consequential, what hint to
supply — is made by the developers' offline program outside any automatic path.
*Fixed-decomposition closure* applies to what the learned policy can update: the
policy composes tool use, delegation, verification, and publication, while task
contracts, action families, board protocol, verifiers, and evaluation stay fixed.
No pattern in the table describes the deployment side, because the record
describes no closed improvement path there to be degenerate.

Checked against the verification row, one code-grounded finding is material:
"the independent-verifier condition is a planning-mode gate keyed by verifier
session name, and all three shipped Agent Team profiles disable planning mode",
so mandatory independent verification is "configurable behavior, not [a] default
invariant". The claimed stale-output reconciliation was also not located in the
public revision, and board rows lack the dependency and returned-evidence fields
the paper describes. At deployment, then, the mechanism that would supply an
oracle independent of the producing agent exists but is off by default.

**Residual human cut.**

- Deciding what to train and which decision points are consequential:
  **unrepresented premise**. The corrective hint carries that knowledge, is never
  a prediction target, and is absent at inference time, so it does not persist in
  a form the system can read.
- Verifying a delivery independently: **no independent oracle**. The verifier
  gate is disabled in all shipped profiles, and the record does not state why.
- Establishing that a delivered file is fresh rather than stale: **no
  independent oracle**. Stale-output reconciliation was not located in the public
  revision.
- Judging trajectory quality: **no independent oracle**. HDS6 "is a promising
  process-assessment design, not evidence that access to a trajectory improves
  judging"; it has no paired output-only control and no reported independent
  calibration.
- Every improvement decision after the run ends: **horizon**. The declared
  automatic horizon is the run; the training program lives entirely beyond it.

## What this run does and does not establish

**It holds over these six only.** DGM, HGM, HyperAgents, Prime Agent, Recuris,
and Apodex 1.1 were selected because the match register already routes their
ingests, not by any sampling procedure over self-improving systems. Nothing here
is a prevalence claim: this run does not say how common any pattern, gate
strength, or residue reason is in the field, and no statement in it may be
carried into an article as a claim about self-improving systems generally. Ledger
row S5 binds the same boundary for the related claim about recurrent
later-episode dependence ([incumbent ledger](./incumbent-ledger.md)).

**The record's own gaps are a finding.** The capability floor is unstated for
every one of the six. No examined system declares a stage-relative threshold at
all; each reports benchmark scores against a task suite it chose, and one
(HGM) carries a "human-level" framing its ingest explicitly warns is
benchmark-local. The map's second condition therefore cannot currently be applied
to any of these systems from the retained record — a measurement about the
literature's reporting conventions, not about the systems' capability.

**Correction is the condition that separates them.** One path meets it (Recuris,
by a fixed held-out paired gate whose grounds the candidate does not author).
Three do not: DGM and HyperAgents admit on viability and demote quality to a
selection weight; Prime Agent has no acceptance operation at all. Two leave it
unstated (HGM, Apodex). This is the map's prediction holding on this set: the
degenerate patterns cluster at the evaluator, and the residue reasons cluster
with them — "no independent oracle" is the most frequently assigned reason across
the six residue lists.

**One system reaches a later-episode measurement; none reaches recurrence.**
HyperAgents' Improvement@50 measures a retained hyperagent generating better
agents in an unseen domain, significantly above the initial agent — a displaced
measurement rather than the accepting metric. Its continuation comparison, which
would test recurrence, is not statistically significant. Recuris's second
evolution round sits inside the paper's own noise estimate. On this set, one
single cross-domain contribution is established and recurrent later-episode
dependence is not.

**Two conditions are met almost everywhere, and that is worth reading
carefully.** Consequential reach and no-hidden-cut are met for all six and five
of six respectively. The second is a credit to the papers: these systems declare
their frozen layers, sometimes with the reason (DGM's Appendix J concedes the
exploration-process freeze was affordable rather than protective). It is not
evidence that the cuts are small.

**Three record-level problems surfaced.** DGM's Section 3 says each parent
analyzes its own logs and proposes the next feature while Appendix C.3 discloses
that a separate o1 model performs the diagnosis — a contradiction inside the
source, flagged by the ingest, resolved here in favor of the appendix. Apodex's
report claims several runtime guarantees the pinned public revision does not
implement (board row schema, default independent verification, evidence-graph
synthesis, stale-output reconciliation); the ingest's code grounding is the
authority for those cells. And the phrase "continual harness" names both Prime
Agent's own persistence layer and a separate system with its own ingest and its
own row in the six-path note; the two must not be conflated.

**Two candidate map refinements are recorded, not acted on.** The
degenerate-pattern table names weak acceptance mechanisms but has no row for the
absence of any acceptance operation, which is where Prime Agent's path sits. And
it has no row for growth-only retention — Recuris's package that adds skills,
deprecates none, and carries near-duplicates into admitted versions. Both are
inputs to a later revision of [the map](./closure-capability-map.md), which this
run does not make.
