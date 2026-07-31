# Agent curiosity and structural coherence

## Goal

Investigate a proposed cross-artifact failure pattern: an agent can produce locally acceptable code or prose, explain good architecture or argument structure when asked, and carry out a named refactoring or revision, yet fail to originate the concern that something is in the wrong place.

In code, a branch, helper, or compatibility shim can satisfy the current tests while leaving responsibility somewhere a human maintainer finds surprising. In prose, a sentence or paragraph can be fluent and topically connected to its neighbors while failing to serve the section's argumentative role. The observed artifact alone does not say whether local fit shaped the proposal, stopped further review, or won an explicit comparison; locating that boundary is the workshop's central task.

The proposed shared phenomenon is **local admissibility alongside global misplacement**. The workshop asks whether the missing move is weak anomaly-to-subgoal transition — provisionally, one component of curiosity — or a neighboring bottleneck such as locally conditioned proposal, missing artifact model, premature controller stopping, weak global candidate generation, preservation or edit-risk bias, context limits, or an oracle that poorly distinguishes structural quality.

The aim is not to explain every complaint about LLM-generated code or text. The evidence set is deliberately a small mechanism-discriminating sample.

## Why a new workshop

The earlier [curiosity-prompts experiment](../curiosity-prompts/experiment-report.md) produced an initial lead: a broad curiosity prompt generated valuable investigations but varied across its two trials, while a cost/benefit question found its target in both of its two trials. The sample is too small to establish stable prompt effects. It nevertheless motivated a [Curiosity Pass](../../agent-memory-systems/types/agent-memory-system-review.md#curiosity-pass) for completed agent-memory-system reviews.

That pass is useful but late and narrow. The task has already been selected, the report has already been written, and the agent has been explicitly told to look for surprises. It tests prompted retrospective inquiry. It does not test whether an agent notices an oddity while acting, keeps it unresolved after a locally successful continuation, forms an investigation or restructuring subgoal, and revises its plan.

The motivating [weakly discriminated qualities](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) note explains why hard checks can select correctness more strongly than maintainability. This workshop investigates an earlier boundary as well: whether a structural candidate ever enters search and selection. A quality can be lost because the oracle does not select it, but also because the agent never asks the question that would generate a competing design.

The prose extension begins from a maintainer observation in this KB: some sentences feel clearly out of place when the whole note and section purposes are held in view, yet are superficially connected enough that an agent never marks them as anomalous. This is a motivating observation and fixture-selection rule, not yet a prevalence result.

## One proposed pattern, different local signals

The cross-domain claim is not that code and prose are identical. Their immediate success signals differ:

| Domain | Easy local signal | Weakly judged global property | Characteristic additive accommodation |
|---|---|---|---|
| Software | Current behavior and tests pass; the edited site is type- and syntax-correct | Responsibility placement, conceptual integrity, and locality of later change | Add a branch, shim, flag, wrapper, helper, or parallel path |
| Natural language | The unit is grammatical, plausible, topically adjacent, and connected by a transition | Thesis economy, section ownership, argumentative role, and whole-document progression | Add a bridge, qualification, example, distinction, paragraph, or section |

Code has an explicit green signal that can close the immediate task. Prose usually has no comparable discrete test. Continuation plausibility and topical adjacency may shape what is generated; the controller may stop once a passage reads adequately; and a later reviewer may apply sentence-level criteria to candidates. Those are three distinct mechanisms. Reserve **oracle** for a criterion actually applied to an artifact, and infer weak selection only when candidate generation and evaluation can be observed separately. The weaker proposed commonality is only that local fit can coexist with global misplacement and may reduce the chance that the wider artifact model is constructed or used.

The stronger causal intuition — that a faculty trained to optimize locally testable completion in code transfers into prose — remains a hypothesis. Cross-domain behavioral similarity would establish a homologous failure, not its training origin. Following [the failure-mode transfer method](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md), the workshop will test the particular mechanism and its boundary conditions rather than infer transfer from analogy.

## Two routes into an epistemic subgoal

Curiosity need not begin only after something already feels odd. The workshop distinguishes a **reactive route**, which investigates an encountered mismatch, from a **prospective route**, which actively asks where an apparently applicable rule might fail.

The reactive anomaly-to-subgoal transition has five observable parts:

1. The agent constructs or retrieves a global expectation: a responsibility map, thesis, section purpose, argument graph, or future-change pattern.
2. It assigns a role to the current unit rather than judging only its immediate connection to adjacent material.
3. It registers a mismatch between the unit's role and the global expectation.
4. It judges the mismatch important enough to create and pursue an investigation, relocation, consolidation, deletion, or reframing subgoal without being given that edit verbatim.
5. The result changes the plan, artifact, or stated uncertainty.

The prospective route begins before a mismatch has been observed:

1. The agent retrieves a load-bearing structural rule, decomposition assumption, or role invariant that appears to govern the case.
2. It states what would materially change if that rule did not hold here.
3. It identifies an observable reason this case may lie near or beyond the rule's boundary.
4. It turns that possibility into a discriminating check rather than a generic doubt.
5. The result updates the rule's scope, the artifact, the plan, or the agent's uncertainty.

An author's apparent perspective can be a hypothesis-generating clue only when grounded in the artifact: for example, relevant cases are drawn from one side of a declared boundary, assumptions are explored asymmetrically, or a case required by the stated scope or an independent coverage model is absent. It is not evidence about the author's intent and does not itself show that the rule fails. The prospective route should therefore be scored against both true boundary failures and plausible false leads.

This definition avoids claims about whether a model has an “inherent” subjective curiosity. A model may answer excellent architectural or editorial questions when asked while the surrounding agent has no operative trigger, durable inquiry agenda, investigation budget, or plan-revision step.

“Out of place” also needs a stronger referent than human discomfort. A target unit should be locally related to its surroundings yet violate an explicit role model: it duplicates an already-filled role, belongs under a different section or owner, competes with the artifact's main claim, or can be deleted without losing load-bearing content. Experiments need both an obviously irrelevant control and a locally related, correctly placed control so topicality alone cannot solve the task.

## Failure surface in scope

The initial sample investigates only two linked observations:

- **Under-originated structural goals:** vague “improve this” instructions elicit surface fixes, while a supplied responsibility map, section purpose, or named transformation enables a much stronger revision.
- **Additive accommodation:** a local addition makes the immediate code path work or the prose passage read smoothly without moving, merging, deleting, or reframing the misplaced unit.

A parallel experiment investigates **under-originated structural boundary probes**: the agent applies a plausible ownership, section-role, argument-structure, or decomposition rule without asking whether the present case falls outside its scope, even when the structural consequence of failure is material and the artifact contains a non-conclusive boundary cue. This is not required to explain every misplacement case; it tests the broader claim that curiosity can generate candidate anomalies rather than only react to them.

“Additive” is conceptual, not a line-count test. A move can temporarily add lines; a deletion can leave duplicated responsibility intact; and deliberate point-of-use repetition can be correct in prose. The property of interest is whether the edit preserves an unresolved role conflict and layers accommodation beside it rather than changing the model of where the behavior or claim belongs.

Out of scope unless a source directly discriminates one of the transitions above:

- general hallucination, factuality, grammar, style, security, benchmark-pass-rate, or “AI slop” complaints;
- prose-coherence tasks solvable by finding an unrelated or nonsensical sentence;
- broad defect or verbosity counts without a trace of role assignment, problem finding, or edit choice;
- undirected lists of speculative questions that identify neither a load-bearing rule, a material consequence, nor artifact-grounded evidence that a boundary may be near;
- prospective questions whose answers predict no responsibility, section-role, argument-structure, or artifact-organization consequence;
- “lack of taste” essays used as evidence by themselves;
- planning and subgoal execution after a complete issue, artifact model, and success condition have already been supplied; and
- remedies before the failure has been localized among rival mechanisms.

## Evaluation boundary

The workshop will not promote “curiosity causes bad structure” from correlated symptoms.

- Structure needs an explicit referent: a responsibility rule, section-purpose map, argument graph, accepted human relocation/deletion used as a bounded reference choice, later requirement, or blinded expert judgment tied to consequences.
- Human historical changes are evidence of a chosen design, not proof that no alternative could be good.
- Same-model interventions should expose global-model availability, anomaly cues, candidate generation, frozen-candidate evaluation, and execution as separate stages. An exact-change condition is a capability ceiling, not evidence by itself about where the earlier process failed.
- Conditions need repeated trials at a fixed model partition and source snapshot, neutral-cue controls, blinded scoring where possible, and uncertainty reporting. One successful run is a lead, not a stable behavioral difference.
- Passing tests and fluent transitions are outcome observations, not evidence that the global organization is good or bad.
- Software and prose results remain separate until a matched cross-domain design shows the same transition and intervention effect. Similar final artifacts alone do not establish a shared cause.
- Local workshop cases can generate hypotheses and fixtures; they do not establish prevalence.
- Apparent author background or perspective may motivate a probe, but only observable asymmetry or omission relative to a declared scope or independently warranted coverage model can count as the cue; neither establishes the answer in advance.
- Prospective-curiosity experiments need rule-holds, rule-fails, and tempting-false-lead controls. Otherwise indiscriminate doubt can score as curiosity.
- Hold/fail labels must be frozen before model runs and grounded in downstream outcomes, mechanically checkable dependencies, or independent expert agreement; true and false cues should be matched for salience and plausibility.
- Memory-first cognitive-architecture sketches can suggest process decompositions but must be externally grounded before supporting a theory note.

## Work order

1. Establish several prose fixtures whose target is independently judged locally connected but globally role-incongruent.
2. Locate the prose failure among global representation, noticing, controller stopping, structural-candidate generation, candidate selection, and execution.
3. Build a small software fixture set and compare the stage-specific intervention signature, without presuming a common cause.
4. Search for primary evidence on those narrow claims and prune sources that expose no relevant transition or furnish no usable fixture.
5. Promote the concrete claims that survive before attempting a curiosity/taste synthesis or remedy.

The intended promotion order is concrete-first: locally connected but globally misplaced prose, under-originated prose-rehoming goals, and under-originated refactoring goals before a general curiosity or taste note. Cross-domain prompt transfer, training origin, longitudinal erosion, and remedies are explicit follow-ons rather than prerequisites.

Prospective boundary probing is a parallel curiosity claim. It should begin with matched, inspectable cases after the base role-conflict fixtures are stable, and it does not substitute for evidence about the concrete misplacement failure.

## Working artifacts

- [Local case corpus](./local-case-corpus.md) — a pruned inventory of mechanism-relevant software and prose cases already in the KB and workshops.
- [Prose fixture candidates](./prose-fixture-candidates.md) — exact frozen passages for testing locally connected but globally misplaced material, including controls and admission gaps.
- [Hypotheses and experiments](./hypotheses-and-experiments.md) — the provisional process model, rival explanations, and within- and cross-domain interventions that distinguish them.
- [Focused web-search plan](./web-search-plan.md) — primary-source queues, targeted code and prose queries, capture schema, and stop rules.

## What closes this workshop

The workshop closes when:

1. at least two prose fixtures pass independent local-window and whole-document role validation, with easy and genuine-bridge controls;
2. a stage-separated prose experiment distinguishes open noticing, supplied role-model diagnosis, structural-candidate generation, frozen-candidate selection, and exact revision;
3. a small software comparison tests whether the same stage signature appears without treating similar symptoms as proof of transfer;
4. the evidence adjudicates subgoal origination against representation, stopping, search, selection, and execution rivals; and
5. at least two concrete claims have been promoted, rejected, or explicitly deferred for insufficient evidence.

The broad synthesis need not survive. A successful closure may conclude that “curiosity” compresses independent failures, or that software and prose reach similar additive outcomes by different routes.
