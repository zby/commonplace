---
description: "Compares factory-learning mechanisms on their shared causal job — experience-responsive retention — while separating update mechanisms from the project-theory function needed for open-ended coherent modification"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, learning-theory, self-improving-systems]
---

# Factory-learning mechanisms should be compared on the same causal job

> TODO! remove or update to use software house instead of software factory

A fair comparison among factory-learning mechanisms asks how each turns production experience into a retained change to reusable production machinery that affects later production. Comparing natural language with code or weights, or readability with end-to-end optimization, mixes representational form with the causal job being performed.

The shared job is:

```text
production experience
  -> allocation of search or update effort
  -> candidate or direct factory change
  -> evaluation or other update control
  -> retention and later behavioral effect
```

This is experience-responsive retention, the causal job every factory-learning mechanism must perform. It does not by itself establish the harder capacity to modify a long-lived program coherently when local acceptance criteria do not exhaust its purpose and organization. A mechanism can change later production and still fail that test.

Not every mechanism exposes all of these steps as separate components. A direct optimizer may combine proposal and selection in one update. A trajectory-reuse system may retrieve an earlier procedure without constructing a new artifact. A theory-mediated process may guide search before a candidate exists. The comparison should preserve these architectural differences while asking whether the same downstream transition was achieved.

## Live mechanism families

| Mechanism | Typical retained state | Characteristic strength | Characteristic risk |
|---|---|---|---|
| Trial-and-error retention | A tool, workflow, policy, prompt, or configuration associated with observed success | Makes few assumptions about why a change works | Weak transfer and expensive search when feedback is sparse or delayed |
| Trajectory or episode reuse | Stored traces, summaries, plans, demonstrations, or retrieved procedures | Reuses concrete experience with low abstraction cost | Copies incidental details, can fail under shift, and may not expose which part should be revised |
| Program search | Symbolic programs, schemas, workflows, evaluators, or tool compositions | Produces executable and testable machinery | Search spaces and evaluators can encode decisive human-supplied family knowledge |
| Learned construction or selection policy | Parametric or artifact-based policy for choosing or building machinery | Amortizes repeated decisions and can improve with scale | Hidden credit assignment, distribution shift, and limited inspectability |
| Direct optimization | Weights, adapters, continuous policies, scores, or other directly updated state | Can integrate large amounts of feedback without explicit hand decomposition | Update cost, catastrophic interference, weak localization, and difficulty coordinating heterogeneous artifacts |
| Theory mediation | Addressable project-specific claims about tasks, solvers, failures, interventions, evidence, and scope | Makes the theory-bearing function explicit, selectively revisable, and usable across several artifact kinds | Plausible rationalization, interpretation error, maintenance cost, and dependence on model reading and application |
| Mixed mechanisms | Different forms and update methods at different layers or timescales | Matches mechanisms to the structure and verifiability of each subproblem | Cross-layer inconsistency and opaque responsibility for failures |

The table is a working comparison, not an exhaustive taxonomy. A concrete system can instantiate several rows at once.

## Update mechanisms and project theory answer different questions

The rows are not all substitutes for project theory. Trial and error can supply evidence; program search can generate candidate machinery; trajectories can preserve concrete episodes; optimization can revise retained state; and learned policies can amortize recurring choices. Any of them may construct, revise, apply, compile, or implicitly embody a theory of the program being changed.

For open-ended coherent modification, the additional question is whether some project-specific state or capacity performs the functions Naur assigns to program theory: mapping the program to the activity it supports, accounting for why it is organized as it is, and relating new demands to that organization. The theory may be distributed across weights, artifacts, tools, and participants. It need not appear as one explicit document.

An explicit natural-language theory is therefore one proposed realization of a theory-bearing capacity, not merely another update algorithm. A system that succeeds without an addressable theory surface may still realize the same function implicitly. The serious rival to the functional claim is a system that sustains coherent modification without any project-specific state performing those mapping, justification, and integration roles.

## Comparison dimensions

Mechanisms should be evaluated on at least these dimensions:

- **Evidence use:** What observations, tests, corrections, telemetry, examples, or interactions can affect the update?
- **Search allocation:** How does the mechanism decide which production machinery to examine or change before decisive evaluation is available?
- **Reach:** Which schemas, tools, workflows, evaluators, representations, prompts, code, or parametric state can it alter?
- **Credit assignment:** How does later success or failure bear on earlier factory decisions?
- **Operative retention:** How does the selected or updated state enter later production, and can it be rolled back?
- **Transfer:** Does the retained change help a distinct task, product variation, or family without new target-specific human construction of production knowledge?
- **Negative transfer:** How are overgeneralized or harmful lessons detected and revised?
- **Total cost:** Count model calls, environment interaction, compute, human judgment, artifact maintenance, validation, and recovery.
- **Warrant:** What independent checks or accepted error bounds support consequential use?

No single dimension settles the comparison. A mechanism can be cheap but narrow, broad but poorly warranted, interpretable but ineffective, or powerful but expensive to update.

## Representation and production method are orthogonal

The same representational form can be produced by different learning mechanisms. A person can write a prompt; an optimizer can search for one; a theory-mediated agent can derive one from an explanation. All three results are natural-language artifacts, but the production methods and evidence paths differ.

Likewise, symbolic software can be handcrafted, generated from a supplied schema, selected through search, learned from trajectories, or revised through theory. Parametric state can encode either general machinery or target-specific family knowledge. The [Bitter Lesson production-method distinction](./the-bitter-lesson-selects-production-methods-not-representational.md) therefore applies directly: the carrier does not determine whether useful structure was found by a scalable computational method.

## Proposal selection is one architecture, not the universal definition

When a system exposes rejectable candidates, a complete proposal-selection path needs search, evaluation, and operative retention. The [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) states that requirement.

But some mechanisms update state directly or retrieve previously retained machinery without presenting explicit alternatives. They should be judged by causal controls appropriate to their architecture rather than forced into candidate terminology. The common requirement is that production experience determine a retained factory change used later, as defined by [experience-responsive retention](./factory-learning-is-experience-responsive-retention-that-improves.md).

## Fair experimental contrasts

A useful comparison holds constant, as far as possible:

- model and tool access;
- task and product-family selection;
- permitted evidence and interaction;
- total compute and wall-clock budget;
- human interventions and supplied family-specific production knowledge;
- acceptance conditions and later-use horizon; and
- accounting for failures, abstentions, retries, and recovery.

Fact matching is especially important. A theory condition should not receive extra facts hidden in its theory artifact. A trajectory condition should not receive more worked examples. A direct optimizer should not be credited with human-designed target-specific reward shaping that other conditions must infer.

The strongest comparisons intervene on the mechanism while preserving the information available to it. Theory can be withheld, flattened into a fact-matched record, or made plausibly wrong. Trajectories can be shuffled or stripped of outcomes. Search policies can be replaced while keeping the candidate language fixed. The experiment identifies only the contrast it actually runs.

A theory-surface intervention tests whether making project theory explicit and addressable improves the path. It does not by itself establish that every successful alternative lacks theory: a policy or parametric learner may carry the relevant project-specific organization implicitly.

## What a result can establish

- Better immediate product output shows task performance, not factory learning.
- A retained change used later supports the retention path, but not necessarily improvement — so not yet learning.
- Transfer to a distinct admitted product variation supports family-level reuse.
- Repeated transfer across families with falling target-specific human construction of production knowledge supports broader acquisition reach.
- Better coherent modification under delayed feedback supports the tested theory-bearing realization, not the unique necessity of its carrier.
- A mechanism winning in one feedback regime does not establish universal superiority; sparse delayed feedback, dense automated feedback, and safety-critical deployment may favor different mechanisms.

## Scope

- The note compares update mechanisms at the shared retention relation; system architecture and evaluator quality can dominate results.
- The program's scoped claim that open-ended coherent modification requires a project-theory function is a stronger adequacy condition, not part of the minimal retention condition.
- Readability, addressability, exact execution, and parametric compression are properties with costs and benefits, not rankings.
- Mixed mechanisms are the default serious alternative to any single update method.
- Natural-language theory mediation earns support only through comparative causal and outcome evidence; indispensability attaches to the theory-bearing function, not automatically to this carrier.

---

Relevant Notes:

- [Factory learning is experience-responsive retention that improves the factory](./factory-learning-is-experience-responsive-retention-that-improves.md) — grounds: supplies the shared causal job
- [Naur binds program theory to humans by equating machine execution with formulated criteria](./naur-equates-machine-execution-with-formulated-criteria.md) — grounds: supplies the mapping, justification, and coherent-extension functions whose human-only allocation is reopened
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — extends: states the stronger adequacy test beyond a retained factory update
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: separates how useful state is produced from where it is stored
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: bounds conclusions from mechanism comparisons
- [Open-ended improvement allocates search before evaluation](./open-ended-improvement-allocates-search-before-evaluation.md) — extends: identifies search allocation as a central comparison dimension under weak feedback
