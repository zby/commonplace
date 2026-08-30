# Shared model

This is the workshop's compact working synthesis. It connects the
[target problems](./target-problems.md), durable theory notes, and evaluation
artifacts. It does not promote claims by itself; the linked notes carry their
arguments, evidence, and scope.

## Central research question

Can a computational composite use a fallible, project-specific theory to keep
program modification coherent across proposal, search, backtracking, recovery,
and delayed feedback — and revise both its theory and its behavior when
consequences arrive?

The theory need not deduce the correct first change. Human programmers also
search, fail, reverse changes, and revise their understanding. The relevant
capacity is longitudinal: the program theory must shape which changes are tried,
what the process tries to preserve, how failures are interpreted, and how
recovery and later modification proceed. This is the crux developed in
[holding a program theory means sustaining coherent search under delayed
feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md).

## Working conjecture

Explicit project theory can improve this process by making premises, purposes,
assumptions, and scope addressable. A semantic interpreter can apply and
criticize the theory across cases that no fixed rule already covers. Persistent
execution can carry the process across bounded calls, and evidence can correct
both the candidate change and the theory that guided it.

The conjecture concerns causal use, not the presence of a document. Retained
theory contributes a handle for targeted search and revision. It does not supply
correctness, retrieval, credit assignment, evaluation, or continuity by itself,
[because reflection buys addressability rather than those downstream
capacities](../../notes/reflection-buys-addressability.md).

## Complementary operation classes

The programme distinguishes two operation classes inside the deployed system.

A **model-mediated operation** is instantiated jointly by a model's weights and
the prompt supplied for one call. The weights provide broad learned competence
and general search heuristics. The prompt supplies the selected task, project
state, intent, evidence, and constraints that specialize that competence.
Neither component defines the operation alone.

A **symbolic operation** is defined by code relative to a runtime. Once selected
and installed, its consequences can be executed without asking the model to
reinterpret the prompt or reconstruct the operation on every use. A model may
generate, select, explain, or revise the code; independent symbolic execution is
an execution property, not an authorship claim.

```text
model-mediated operation:  weights + prompt  -> interpreted, generally stochastic behavior
symbolic operation:        code + runtime    -> runtime-assigned state transition
```

The relation is therefore not prompt versus code. Prompts complement weights by
specializing learned competence. Code complements the resulting weight–prompt
operation with exact state transitions, persistent bookkeeping, repeatable
procedures, and enforceable checks. The atomic claim is
[code complements the weight–prompt pair with independently executed symbolic
operations](../../notes/code-complements-weight-prompt-with-symbolic-operations.md).

The project state available to the composite is mixed-form. A useful abstraction
is:

```text
K_t = (N_t, S_t, E_t)
```

where `N_t` is retained natural-language state such as theory, intent, rationale,
branch history, and scope; `S_t` is retained symbolic state such as target code,
harness code, tests, schemas, configuration, dependency structure, checkpoints,
and scheduler state; and `E_t` is observed evidence such as traces, test
results, later demands, reviews, and operational outcomes.

Context assembly selects a call-specific view of this state into a prompt. The
model then applies weight-resident competence to that view. The
[natural-language part of project state may specialize weight-resident search
heuristics](../../notes/natural-language-project-state-specializes-search-heuristics.md),
while code and other symbolic artifacts also constrain the search and can later
execute its selected results independently.

Code has two consumption paths. When read in a prompt, it is evidence for a
model-mediated operation. When imported, executed, tested, or used as a
validator, it has symbolic force assigned by the runtime. The same artifact can
therefore be both an object of semantic search and an independently executed
part of the resulting system.

## Search control before decisive evaluation

Open-ended improvement must allocate attention and computation before the
strongest evidence about a branch exists. An evaluator cannot assess a useful
candidate, proof, or experiment that search never develops. Even proof-gated
self-modification retains a prior allocation problem, because the initial search
must reach a proof path before the gate can act. See
[open-ended improvement must allocate search before decisive evaluation is
available](../../notes/open-ended-improvement-allocates-search-before-evaluation.md).

The programme calls a judgment **lightweight search control** when its authority
stops at allocating further work. It may select a branch, probe, continuation,
suspension, or abandonment without licensing an operative change. This permits
weaker and provisional evidence to guide search while stronger evaluation
remains downstream. [Lightweight search control allocates further search without
licensing adoption](../../notes/lightweight-search-control-does-not-license-adoption.md).

The weight–prompt pair is one candidate implementation of this controller. The
weights may contain general heuristics for anomaly detection, alternative
generation, probe selection, persistence, and recovery. The prompt supplies the
project-specific theory, intent, code state, branch history, and constraints
needed to apply those heuristics here. Code can then enforce budgets, retain
checkpoints, execute probes, run tests, and preserve return paths.

Backtracking is part of the control architecture, not evidence that the theory
was absent. It keeps a fallible branch choice provisional by restoring an earlier
usable state and redirecting search when contrary evidence arrives. See
[backtracking keeps lightweight search control provisional](../../notes/backtracking-keeps-lightweight-search-control-provisional.md).

A controller is evaluated by the distribution of consequences produced by its
routing decisions: valuable candidates, discriminating evidence, informative
failures, and improved recovery under matched tasks and resources. It is not
evaluated by treating each provisional branch judgment as an acceptance claim.
See [a search controller is tested by what it brings to stronger
evaluation](../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md).

Learning from a failure requires more than a persuasive explanation. The
retained explanation must change a later branch decision about scope, priority,
probing, continuation, or abandonment. Otherwise it remains commentary rather
than operative search control. See
[a failure explanation becomes search control only when it changes a later
branch decision](../../notes/failure-explanation-changes-later-branch-decisions.md).

## Functional architecture

The current architecture keeps several functions distinguishable because they
have different failure surfaces:

| Functional role | Current realization | Characteristic failure |
|---|---|---|
| Retained project state | Natural-language theory, intent, rationale, and history together with code, tests, schemas, configuration, checkpoints, and evidence records | Omission, contradiction, drift, stale mappings, retrieval failure, or an incomplete symbolic snapshot |
| Model-mediated semantic operation | Model weights plus a call-specific prompt assembled from relevant project state | Underspecification, stochastic deviation, bias, post-hoc rationale, or project theory ignored in practice |
| Independently executed symbolic operation | Code plus a runtime carrying exact transitions, scheduling, validation, installation, rollback, and later reactivation | Faithful execution of the wrong transition, frozen decomposition, incomplete coverage, or truncated horizon |
| Independent exposure and read-back | Tests, validators, held-out tasks, decorrelated criticism, later demands, reviews, and operational consequences | Weak proxies, captured evaluation, viability-only gates, incomplete coverage, or delayed credit assignment |

These functions are distinct because evidence for one does not establish the
others. The architecture need not preserve their current carrier boundaries
forever. [Each residue class needs a different function](../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md),
but one learned substrate may eventually host several functions. The current
split is a provisional, intervention-friendly realization.

The [scheduler–LLM separation exploits an error-correction
asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md):
operations with adequately specified transitions can avoid repeated model
interpretation, while semantic work remains model-mediated. This does not make
code authoritative about the objective. A symbolic runtime can execute the
wrong requirement exactly.

## Evidence ladder for theory-mediated improvement

The workshop distinguishes four increasingly strong claims:

1. **Mediation.** The retained theory changes a proposal, branch allocation,
   evaluation, diagnosis, recovery step, or realized intervention.
2. **Empirical contact.** The intervention produces an outcome that bears on the
   theory rather than merely accompanying it.
3. **Theory learning.** The outcome changes the theory's content, scope,
   confidence, status, or operational role. Rejection or deliberate retention
   after a refuting opportunity is a theory-state judgment too.
4. **Recurrent theory-mediated self-improvement.** The updated theory state
   changes a later operation inside the same behavior-determining path.

The strongest recurrent path is:

```text
retained mixed-form project state
  -> theory-guided weight–prompt search
  -> model-mediated and/or symbolic change
  -> independent or delayed consequence
  -> read-back against the same theory and code state
  -> retained theory, code, or boundary revision
  -> changed later search or execution
```

The path must be causally co-indexed: provenance must identify which theory and
symbolic state guided the change and which later state received the outcome.
Co-occurrence of a theory, successful code change, and unrelated revision inside
one boundary is insufficient. The full distinction is stated in
[theory-mediated self-improvement needs interpretation, retention, and
independent read-back on one path](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

A contemporaneous citation at the decision point is a cheap
[mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md).
Withholding, replacing, or perturbing the theory while holding weights, symbolic
state, tools, and task fixed is stronger evidence that the theory was
load-bearing.

A useful theory-guided change can reach mediation or empirical contact without
reaching recurrence. The record should state the strongest level established
rather than force every episode into the full loop.

## Claim truth and theory fit

A theory-mediated learner must evaluate two properties that should not be
collapsed.

- **Truth, validity, or warranted scope:** does the claim survive empirical,
  formal, source, consistency, or bounded predictive checks?
- **Fit in the working theory:** does the claim belong in the larger causal
  account and improve proposal, search allocation, diagnosis, recovery,
  revision, or transfer?

A true claim can be irrelevant, redundant, badly scoped, or placed at the wrong
abstraction level. A false claim can appear useful because the current system
already embodies it. Local truth tests therefore do not fully select a working
theory.

No current fixed evaluator fully decides global theory fit. Fit is exposed by a
distributed and delayed portfolio of consequences: changed branch choices,
predictions, later demands, repair cost, code behavior, theory interventions,
rival formulations, and transfer. The live system under construction is
therefore an
[initial selection environment](../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md).

System use cannot replace independent truth tests. It can become self-sealing.
Use rival theories, withholding and replacement interventions, preregistered
predictions, held-out demands, delayed consequences, and transfer to keep causal
fit evidence distinct from factual or formal warrant.

## The present loop is already computational

Commonplace should not be described as handcrafting a theory before computation
begins. In a typical episode, a language model retrieves retained artifacts,
interprets their claims and constraints, reads relevant code and tests, searches
and synthesizes candidate formulations or changes, criticizes alternatives, and
uses tools for local checks. Symbolic code carries repository operations,
validation, exact bookkeeping, and retention. Accepted changes to natural
language or code then condition later model calls and executions.

The operator currently supplies much of the sparse high-level selection signal
about global fit, blame, scope, and acceptance. At the boundary that includes the
operator, model, knowledge base, code, and tools, the process is already a
human-inclusive computational theory-mediated learning loop. At a boundary that
excludes the operator, global selection and final acceptance remain exogenous.

The
[2026-08-30 workshop conversation](./computational-theory-guided-conversation-episode-2026-08-30.md)
records a concrete instance:

1. retained Commonplace artifacts, code, and repository state were read;
2. computational synthesis produced a review, candidate distinctions,
   experiments, and repository changes;
3. the operator supplied corrections about the Bitter Lesson framing;
4. natural-language theory and programme artifacts were revised and retained;
   and
5. the revised state guided later work.

This supports mediation, theory-state revision, and recurrence at the
human-inclusive boundary. It does not establish how load-bearing each artifact
was without an ablation, whether the revised claims are independently true, or
whether more computation scales better than the alternatives.

The open engineering problem is not how to introduce computation. It is how to
improve the computational search already present, use symbolic operations where
independent execution helps, and convert recurring operator judgments into
reusable search, selection, and credit-assignment machinery.

## Coherent modification and warranted transfer

The bearer problem and the residual-human-work problem meet at open-ended
modification decisions. No complete local criterion or cheap independent oracle
determines which change preserves the program's organization. A theory-holder
must carry search and recovery until later evidence arrives.

The two problems still ask different questions:

- **Coherent modification:** can the composite use project theory to sustain
  program-specific search, diagnosis, backtracking, execution, and revision?
- **Warranted transfer:** are the premises, authority, correction, and continuity
  needed for that process inside the declared boundary strongly enough that the
  decision can leave the human cut with warrant?

[Warranted transfer may leave people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
when transfer preferentially selects decisions with represented premises,
settled criteria, and checkable outcomes. This is a conditional selection
mechanism, not an established prevalence claim. A cross-sectional shortage of
independent evaluation is consistent with the predicted bottleneck; a direct
test needs before-and-after transfer histories.

An evaluator is necessary for correction but does not replace theory-guided
search or credit assignment. A strong oracle can reject a bad candidate without
identifying which premise, theory, code unit, artifact boundary, or production
method should change. The programme therefore studies both sides: theory
organizes and interprets search; symbolic operations carry exact transitions;
and consequences correct both the theory and the changes made through it.

## Closure, capability, warrant, and power

Computational closure is task-scoped and structural. A claim must declare task
selection, objective and acceptance, system boundary, permitted exogenous
inputs and interactions, horizon, resources, and coverage. Conditional on those
declarations, every required decision and transition must occur inside the
automatic system. See
[task-scoped computational closure](./task-scoped-computational-closure.md).

Closure does not say that the decisions are good. A captured evaluator, a bad
objective, or a no-op loop can be computationally closed. Capability, warrant,
usefulness, and system power require separate evidence. A non-degenerate
milestone pairs structural closure with consequential reach, a declared
capability floor, reject-capable evaluation, continuity, explicit boundary
accounting, and measured outcomes. The
[closure-capability map](./closure-capability-map.md) records these coordinates
and failure patterns.

Performance at least as good as a competent remote programmer is a strong
worker-capability benchmark, not closure. Holding the client fixed exports task
choice, feedback, missing premises, and final acceptance, [because a fixed
client exports the least-warrantable decisions](../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
The benchmark and warranted closure expose the same difficult client and
acceptance boundary from different sides while measuring different coordinates.

## Bitter Lesson pressure and the first bootstrap strategy

The only direct rebuttal to the Bitter Lesson is narrow: learned results need not
all live in weights because production method and representational form are
different axes. That does not defend the present hand-crafted artifacts.

Theory-guided bootstrapping is the first strategy being tried under incomplete
global evaluation. It uses the already-computational Commonplace loop as a live
environment in which retained theory guides weight–prompt search, code executes
selected symbolic operations, and delayed consequences can expose poor fit in
either.

The strategy should improve the use of computation along three connected
surfaces:

- **Model-mediated search:** better retrieval, prompt construction, rival
  generation, criticism, decomposition search, evidence and counterexample
  search, experiment design, and diagnosis.
- **Symbolic operation:** better target code, schedulers, tools, tests,
  validators, schemas, checkpoints, and deterministic transformations.
- **Boundary and selection:** progressively decide which behavior should remain
  model-mediated, which should be codified, which code should be relaxed, and
  which recurring operator judgments should become reusable search controls,
  critics, tests, methods, or programs.

The distinction is not computation versus no computation. It is a current
composition of computational weight–prompt operations, symbolic operations, and
human-assisted high-level selection versus a process whose search, operation
allocation, selection, and credit assignment become increasingly reusable and
computational.

[A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow
it](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
This is a conditional compatibility criterion, not a defense or uniqueness
claim. End-to-end learning, evolutionary search, self-play, weight updates, and
other direct computational methods remain live alternatives.

The long-run challenge is domain-extensibility. The process must eventually
construct the project-specific theory, prompts, code, methods, and checks needed
for domains not enumerated by the designers; reduce the marginal human share of
fit assessment, evaluator construction, and repair; and permit consequential
parts of its own decomposition and operation boundary to be challenged.

No carrier or operation allocation receives permanent protection. Natural-language
theory, prompts, code, symbolic machinery, and current evaluators may be revised,
absorbed, or replaced. The strategy succeeds when increasing computation
improves the production and selection path at competitive total cost, not when
today's files or boundaries survive.

## Current testbeds

Commonplace is a human-inclusive reflective testbed. It retains and routes
project theory, reads and changes code, supports criticism and revision, and can
turn some theory or recurring behavior into operative instructions, validators,
schemas, and programs. The model carries substantial retrieval, interpretation,
synthesis, criticism, and editing work; code carries exact repository
operations, validation, scheduling, and retained behavior.

Humans still choose objectives, supply unrecorded premises, judge much global
fit, assign blame, authorize consequential changes, interpret ambiguous
evidence, and repair paths beyond represented coverage.

Programming agents with persistent project-specific theory are the first
demanding external testbed. They isolate the bearer question without requiring
the target program to be the agent itself. Commonplace then provides the
reflective environment in which the same mechanism can be applied to the
system's own prompts, code, tests, schemas, and operation boundary.

Current evidence supports useful human-agent theory work, computationally guided
search, independently executed symbolic operations, inspectable mechanism
traces, and an initial environment for testing the strategy. It does not
establish independent computational theory possession, computational closure
over selection, domain-extensible cross-form learning, or superiority to more
direct computational approaches.

## Next experiments

### Theory intervention

Test whether prepared project theory is load-bearing on sequential program
modifications. Hold the model weights, target code, control code, tests, runtime,
tools, repository state, budget, and acceptance process fixed while varying:

1. correct project theory;
2. an information-matched record without synthesized theory-level organization;
3. theory withheld; and
4. plausible but wrong or outdated theory.

Each sequence should contain an initial modification and a later demand or
delayed test that exposes whether the first change preserved the program's
organization. Record the live or sampled branches, which branch received more
computation, which retained claim or intent controlled that allocation, and what
stronger evaluation the branch reached. Measure candidate generation,
architectural preservation, backtracking, diagnosis, recovery, collateral
regressions, later-demand performance, human intervention, and whether outcome
read-back changes a later branch decision.

The diagnostic prediction is an interaction: correct theory should route a
fixed budget toward better downstream evidence and outcomes when the later shift
preserves the structure it names; wrong theory should cause predictable negative
transfer; theory withholding should especially damage recovery and follow-on
coherence; and the advantage should shrink where a complete specification and
cheap oracle already settle the task.

### Symbolic-complement intervention

Test when independently executed code improves a weight–prompt operation. Hold
the model, task, objective, and semantic policy as fixed as the comparison
allows, and compare:

1. model-mediated control flow and bookkeeping retained in context;
2. model-generated or model-selected code that performs those operations under
   a symbolic runtime; and
3. a hybrid in which code owns exact state and transitions while the model owns
   semantic branch judgments.

Measure task success, accumulated execution errors, context use, latency, cost,
state continuity, backtracking reliability, debugging effort, and collateral
failures. The comparison should also record specification and maintenance costs:
code may execute exactly while encoding the wrong operation.

### Search-control and operation-boundary bootstrap

Instrument a sequence of real Commonplace improvements. For each consequential
branch, claim, or method, record:

1. which natural-language and symbolic artifacts entered project state and the
   prompt;
2. which model-mediated candidates, comparisons, and judgments were produced;
3. which symbolic operations executed probes, checks, state transitions, and
   retention;
4. which judgment of global fit, credit, or operation placement remained human
   and why;
5. which downstream consequences bore on that judgment;
6. whether rival or ablated theories, prompts, or code changed the result;
7. whether a recurring judgment became a lightweight search control, test,
   validator, critic, method, schema, or program;
8. whether an operation moved between model-mediated and symbolic execution;
9. whether additional computation improved the result; and
10. how the marginal human and computational shares changed on a later episode.

This is a nearer test of the bootstrap strategy than demanding immediate
cross-domain autonomy. It can show whether computational search, symbolic
execution, and selection are improving or whether "bootstrap" merely renames
continued bespoke human correction.

A later cross-domain test should compare this process with direct computational
baselines and ask whether it constructs new theory, prompts, code, and evaluation
machinery without a bespoke human-built ontology and operation allocation for
each domain.

## Minimum episode record

A useful episode record should identify:

1. the selected task, objective, boundary, horizon, resources, and starting
   human cut;
2. the retained natural-language, symbolic, and evidential project state;
3. the prompt assembled for each consequential model call and the theory state
   claimed to guide it;
4. which operations were model-mediated and which were independently symbolic;
5. which live branches were considered and what controlled their allocation;
6. evidence for the truth, validity, or scope of the claims used;
7. which high-level selection, credit, and operation-placement judgments came
   from the operator;
8. the realized theory, prompt, code, test, schema, or runtime change and its
   acceptance mechanism;
9. the independent or delayed outcome and its read-back against the same theory
   and symbolic state;
10. any theory, code, or operation-boundary revision, including rejection,
    rescoping, rollback, codification, relaxing, or deferral;
11. whether the revision changed a later branch decision or execution;
12. whether a recurring human judgment became reusable search or selection
    machinery; and
13. which dimension moved and which decisions remain human.

The record should state the strongest evidence level reached. Without a
same-theory and same-state trace, it may show a useful change but not theory
mediation. Without later use, it may show theory learning but not recurrence.
Without an intervention, it cannot quantify how load-bearing retained theory
was. Without better downstream results from changed branch allocation, it does
not support the search-controller claim. Without growth in reusable selection
machinery or better results from additional computation, it does not support the
scaling strategy.

## Open questions

- What task distribution and horizon distinguish coherent theory-guided search
  from luck, memorization, or generic search with a permissive evaluator?
- Can project theory improve search allocation, recovery, or revision cost after
  accounting for retrieval, maintenance, and evaluation?
- How much does retained natural-language theory change weight–prompt search
  relative to the same code and an information-matched record?
- Which code should be read as project evidence, and which symbolic state can be
  summarized without losing the constraints that matter?
- Which operations should remain model-mediated, which should be codified, and
  what evidence should trigger relaxing in the reverse direction?
- Does independently executed code improve reliability and cost after counting
  specification, integration, validation, and maintenance work?
- Which parts of global theory fit can be operationalized without encoding the
  present theory into the evaluator?
- How can delayed consequences assign credit among theory, prompt construction,
  target code, control code, tests, and the operation boundary?
- Which recurring human judgments should first become lightweight search
  controls rather than acceptance gates?
- How should inference-time compute, symbolic execution, human correction, and
  retained artifacts be accounted for in an end-to-end comparison?
- What direct computational baseline provides the strongest alternative first
  strategy?
- What cross-domain sequence would demonstrate domain-extensible coevolution
  rather than a broad but fixed ontology and operation allocation?
