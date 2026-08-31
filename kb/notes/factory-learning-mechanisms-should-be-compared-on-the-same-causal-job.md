---
description: "Compares learning mechanisms by how they turn production experience into retained factory changes that affect later production, rather than by representational form or readability"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, learning-theory, self-improving-systems]
---

# Factory-learning mechanisms should be compared on the same causal job

A fair comparison among factory-learning mechanisms asks how each turns production experience into a retained change to reusable production machinery that affects later production. Comparing natural language with code or weights, or readability with end-to-end optimization, mixes representational form with the causal job being performed.

The shared job is:

```text
production experience
  -> allocation of search or update effort
  -> candidate or direct factory change
  -> evaluation or other update control
  -> retention and later behavioral effect
```

Not every mechanism exposes all of these steps as separate components. A direct optimizer may combine proposal and selection in one update. A trajectory-reuse system may retrieve an earlier procedure without constructing a new artifact. A theory-mediated process may guide search before a candidate exists. The comparison should preserve these architectural differences while asking whether the same downstream transition was achieved.

## Live mechanism families

| Mechanism | Typical retained state | Characteristic strength | Characteristic risk |
|---|---|---|---|
| Trial-and-error retention | A tool, workflow, policy, prompt, or configuration associated with observed success | Makes few assumptions about why a change works | Weak transfer and expensive search when feedback is sparse or delayed |
| Trajectory or episode reuse | Stored traces, summaries, plans, demonstrations, or retrieved procedures | Reuses concrete experience with low abstraction cost | Copies incidental details, can fail under shift, and may not expose which part should be revised |
| Program search | Symbolic programs, schemas, workflows, evaluators, or tool compositions | Produces executable and testable machinery | Search spaces and evaluators can encode decisive human specialization |
| Learned construction or selection policy | Parametric or artifact-based policy for choosing or building machinery | Amortizes repeated decisions and can improve with scale | Hidden credit assignment, distribution shift, and limited inspectability |
| Direct optimization | Weights, adapters, continuous policies, scores, or other directly updated state | Can integrate large amounts of feedback without explicit hand decomposition | Update cost, catastrophic interference, weak localization, and difficulty coordinating heterogeneous artifacts |
| Theory mediation | Addressable natural-language claims about tasks, solvers, failures, interventions, evidence, and scope | Can coordinate search and revision across several artifact kinds through one interpretable medium | Plausible rationalization, interpretation error, maintenance cost, and dependence on model reading and application |
| Mixed mechanisms | Different forms and update methods at different layers or timescales | Matches mechanisms to the structure and verifiability of each subproblem | Cross-layer inconsistency and opaque responsibility for failures |

The table is a working comparison, not an exhaustive taxonomy. A concrete system can instantiate several rows at once.

## Comparison dimensions

Mechanisms should be evaluated on at least these dimensions:

- **Evidence use:** What observations, tests, corrections, telemetry, examples, or interactions can affect the update?
- **Search allocation:** How does the mechanism decide which production machinery to examine or change before decisive evaluation is available?
- **Reach:** Which schemas, tools, workflows, evaluators, representations, prompts, code, or parametric state can it alter?
- **Credit assignment:** How does later success or failure bear on earlier factory decisions?
- **Operative retention:** How does the selected or updated state enter later production, and can it be rolled back?
- **Transfer:** Does the retained change help a distinct task, product variation, or family without new target-specific human design?
- **Negative transfer:** How are overgeneralized or harmful lessons detected and revised?
- **Total cost:** Count model calls, environment interaction, compute, human judgment, artifact maintenance, validation, and recovery.
- **Warrant:** What independent checks or accepted error bounds support consequential use?

No single dimension settles the comparison. A mechanism can be cheap but narrow, broad but poorly warranted, interpretable but ineffective, or powerful but expensive to update.

## Representation and production method are orthogonal

The same representational form can be produced by different learning mechanisms. A person can write a prompt; an optimizer can search for one; a theory-mediated agent can derive one from an explanation. All three results are natural-language artifacts, but the production methods and evidence paths differ.

Likewise, symbolic software can be handcrafted, generated from a supplied schema, selected through search, learned from trajectories, or revised through theory. Parametric state can encode either general machinery or target-specific specialization. The [Bitter Lesson production-method distinction](./the-bitter-lesson-selects-production-methods-not-representational.md) therefore applies directly: the carrier does not determine whether useful structure was found by a scalable computational method.

## Proposal selection is one architecture, not the universal definition

When a system exposes rejectable candidates, a complete proposal-selection path needs search, evaluation, and operative retention. The [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) states that requirement.

But some mechanisms update state directly or retrieve previously retained machinery without presenting explicit alternatives. They should be judged by causal controls appropriate to their architecture rather than forced into candidate terminology. The common requirement is that production experience determine a retained factory change used later, as defined by [factory-level continual learning](./a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md).

## Fair experimental contrasts

A useful comparison holds constant, as far as possible:

- model and tool access;
- task and product-family selection;
- permitted evidence and interaction;
- total compute and wall-clock budget;
- human interventions and supplied specialization;
- acceptance conditions and later-use horizon; and
- accounting for failures, abstentions, retries, and recovery.

Information matching is especially important. A theory condition should not receive extra facts hidden in its theory artifact. A trajectory condition should not receive more worked examples. A direct optimizer should not be credited with human-designed target-specific reward shaping that other conditions must infer.

The strongest comparisons intervene on the mechanism while preserving the information available to it. Theory can be withheld, flattened into an information-matched record, or deliberately made wrong. Trajectories can be shuffled or stripped of outcomes. Search policies can be replaced while keeping the candidate language fixed. The experiment identifies only the contrast it actually runs.

## What a result can establish

- Better immediate product output shows task performance, not factory learning.
- A retained change used later supports the learning path, but not necessarily improvement.
- Transfer to a distinct admitted product variation supports family-level reuse.
- Repeated transfer across families with falling target-specific human work supports broader acquisition reach.
- A mechanism winning in one feedback regime does not establish universal superiority; sparse delayed feedback, dense automated feedback, and safety-critical deployment may favor different mechanisms.

## Scope

- The note compares mechanisms, not complete systems; system architecture and evaluator quality can dominate results.
- Readability, addressability, exact execution, and parametric compression are properties with costs and benefits, not rankings.
- Mixed mechanisms are the default serious alternative to any single-method claim.
- Theory mediation earns support only through comparative causal and outcome evidence, not because the research program is described in theoretical language.

---

Relevant Notes:

- [A software factory learns when production experience changes reusable machinery used later](./a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md) — grounds: supplies the shared causal job
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: separates how useful state is produced from where it is stored
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: bounds conclusions from mechanism comparisons
- [Open-ended improvement allocates search before evaluation](./open-ended-improvement-allocates-search-before-evaluation.md) — extends: identifies search allocation as a central comparison dimension under weak feedback
