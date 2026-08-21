# Explanatory theories in deployment-time learning

> **Workshop status:** This is an exploratory Commonplace workshop combining a general model with system-specific readings and outreach drafts. It is not a validated deployment-time-learning method, an implementation specification, or a safety claim.

This workshop asks how evidence from real-world tasks could train a deployed agent system. Here, training means using task outcomes, feedback, failures, and later consequences to propose and select persistent changes to behavior-shaping system state. It does not require updating the base model's weights, and a task result is evidence for an update rather than an update by itself.

[Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md), [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md), and [Exo](../../agentic-systems/exo.md) contribute different parts of the inquiry. HCL develops a governed proposal-evaluation-commitment protocol in controlled benchmark streams. SPADE supplies a separate precedent for generating, filtering, and valuing executable environments. Exo supplies a concrete mutable substrate in which accepted changes can remain operative, together with the sharper question of whether an earlier retained benefit improves the productivity of a later improvement episode. None establishes the explicit theory lifecycle proposed here or the value of such a lifecycle. HCL does not establish the controlled-to-deployment transfer, SPADE does not establish theory-guided procedure generation, and Exo's inspected affordances do not establish beneficial self-improvement or compounding.

## Workshop question

Could an explicit theory of system behavior with genuine [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) improve search for candidate changes, selection among them, and acquisition of costly evidence? Does retaining and revising that theory across deployment episodes add value beyond reconstructing a provisional theory on the spot?

The working proposal treats a system theory as a shared intermediate object across a proposal-selection loop. A theory can diagnose a failure, choose where to search, generate and prioritize candidate changes, derive their expected benefits and impacts, and guide which evaluation evidence to acquire. Evidence can then select a system change and separately support accepting, rejecting, or revising the theory.

The first experiments would have an LLM construct a working theory `tau_n` inside each run. This can test immediate reasoning value, but it is an **ephemeral-theory** treatment. The stronger cumulative theory-mediated self-improvement claim requires an addressable `T_n` to be retained, retrieved into later working theories, and selectively revised across episodes. Constructing a plausible theory on demand does not establish that the system has accumulated one; deployment-time learning can still occur through retained harness changes without retaining a theory.

The Exo track adds a further distinction. A theory of how the system behaves can guide diagnosis, change search, and impact projection. A theory of promotion and revision instead governs what evidence becomes a retained artifact, in which form and with what authority, and how that artifact is later activated or revised. The latter is a meta-level theory of the improvement process, not automatically an object-level theory of the system being changed. Both can be explicit and revisable, but evidence for one is not evidence for the other.

Deployment-time learning, accumulation, and compounding also name different claims. An episode can produce an operative retained change without retaining any theory. Useful changes can accumulate without making the next change easier to produce. The stronger Exo-facing claim requires a later improvement episode whose lower cost, greater reliability, broader reach, or reduced dependence on human judgment can be traced to an earlier retained benefit. Exo's source-pinned capabilities make it a concrete target for testing that claim; they are case facts about the available substrate, not general evidence that explicit theories improve deployment-time learning.

The impact question is intervention-shaped, so causal theories are an important route to `I_tau`. They are not the umbrella. A theory may instead or additionally expose dependency and authority paths, invariants or proofs, compositional program structure, semantic contracts, or action-conditioned predictions. What makes search or selection theory-guided is that it changes in ways derived from a criticizable account of why the system behaves as it does. Calling the account causal or explanatory does not establish explanatory-reach; that remains an empirical and argumentative liability.

The proposal is conditional. A theory can narrow search or evaluation in the wrong direction, and using the same model to propose the theory, candidate, and evidence surface can make the loop self-confirming. Local evaluation is plausible only when changes are sparse in a matching decomposition, dependencies and authority paths are explicit, and downstream impact is bounded. A sound theory may instead project broad impact and correctly recommend running most or all checks. Selecting less evidence changes what acceptance can honestly mean: omitted checks remain unknown unless a separately justified residual-risk rule accounts for them, and that rule remains exposed to errors in the theory, its scope, or the derivation of its impact projection.

## Reading map

- [From controlled HCL benchmarks to deployment-time learning](./hcl-reading.md) — the proposed transfer, HCL's sampled-retention boundary, the conditional evaluator-growth calculation, and why its harness partition is not assumed to be a complete explanatory decomposition or causal graph.
- [A provisional theory-mediated improvement loop](./theory-mediated-improvement-loop.md) — the two coupled system-change and theory-change loops, the roles of theory in search and selection, and the difference between on-the-spot construction and retained revision.
- [A provisional theory-guided selective-evaluation model](./selective-evaluation-model.md) — the system-theory/impact-projection distinction, derivation routes and baselines, acceptance semantics, theory error, selective-observation problem, and limits of the locality hypothesis.
- [Experiment design for theory-mediated deployment-time learning](./experiment-design.md) — staged comparisons of theory-guided candidate search, candidate selection, evidence selection, ephemeral versus retained theories, and SPADE-inspired procedure generation.
- [An invitation to the HCL authors](./for-hcl-authors.md) — the shorter HCL-facing account and questions.
- [An invitation to the SPADE authors](./for-spade-authors.md) — the shorter SPADE-facing account and questions about adaptive executable evaluations.
- [An invitation to the Exo authors](./for-exo-authors.md) — the Exo-facing case for testing whether an earlier retained benefit helps produce a later improvement.
- [The Exo case](./exo-case.md) — Exo's mutable revision substrate, accumulation-versus-compounding distinction, promotion and revision theory, evaluation boundary, and proposed comparison.
- [Exo evidence and counterevidence](./exo-evidence.md) — source-pinned Exo and ExoWorker facts, neighboring results, adverse evidence, unresolved gaps, and falsifiers.

## Current boundary

The workshop has not established that HCL's controlled techniques transfer to learning from real-world tasks, that any candidate system theory has genuine explanatory-reach, that explicit theory construction improves change search or candidate choice, that theory-derived impact projections are accurate, that selective evaluation lowers total cost, that retaining a theory beats reconstructing one, or that an Exo improvement has compounded into a later one. It has not chosen the theory representation, theory-acceptance rule, primary evaluation registry object, evidence-selection objective, candidate-decision rule, materiality threshold, loss units, prediction horizon, assessment protocol, or final harness-acceptance rule. A controlled comparison needs measured search quality and diversity, candidate quality, costs, detection coverage, harmful misses, route-appropriate calibration or soundness checks, held-out retention, deliberate observation of checks the selector would otherwise omit, and tests that vary load-bearing premises and distinguish rival theories on unseen change families. Evidence of deployment value or an Exo compounding pathway would require a later study in the target setting.

## Closing the workshop

This workshop can close in one of three ways:

- **Promote a method claim** only after the ontology and separate harness- and theory-acceptance semantics are explicit and controlled comparisons supply evidence for the proposed explanatory mechanism as well as measured search, candidate-quality, cost, detection, harmful-miss, route-appropriate calibration or soundness, expenditure, and cross-episode retention results.
- **Hand off an experiment or proposal** if the maintainer authorizes separately scoped work to gather missing evidence or choose an implementation, without promoting effectiveness claims.
- **Close without promotion** if the evidence is negative, the required assumptions cannot be defended, or the inquiry is not worth continuing.

The maintainer must choose the disposition and any promotion order. A durable note, proposal, experiment, implementation, or external contact is separate work. Author replies would be welcome but are not required for closure.

The Exo-facing track can exit independently once its pitch has survived or failed scoped criticism, its durable conclusions have been extracted or explicitly declined, and the maintainer has decided whether to contact the Exo authors. It need not wait for the general HCL/SPADE experimental program, and author contact or reply is not a condition for closing the wider workshop.
