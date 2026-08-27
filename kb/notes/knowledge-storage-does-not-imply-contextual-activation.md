---
description: Separates knowledge that exists, knowledge loaded into context (read-back), and knowledge that actually changes behavior (activation); explains why retrieval and long context do not guarantee activation
type: kb/types/note.md
traits: [has-external-sources]
tags: [llm-reliability, failure-modes, evaluation]
---

# Knowledge storage does not imply contextual activation

An agent system can have the right knowledge and still fail to use it. The knowledge may exist in model weights, notes, memory records, documentation, source files, or even the live context window. That does not mean it will affect the next answer or action.

The missing step is **contextual activation**: making available knowledge action-relevant in the current task. Retrieval proves that the system can produce a fact when asked. Context presence proves that the fact was visible to the model. Activation is stronger: the fact changes what the agent notices, says, checks, or does without the user naming it directly.

This is why "the model knows X" is often the wrong operational question. The useful question is: will X be brought to bear at the moment when it matters?

Bringing stored memory into that context is **read-back**: the return of *retained memory* — content the system accumulated from use, whether authored (a note, a project decision) or trace-learned — into a future action, reached either by the agent's own lookup (*pull*) or by unsolicited arrival (*push*). The boundary is accumulation: runtime injection of shipped, static documentation — tool specs, repo docs, installed skills — is *not* read-back, because that content arrives *with* the system rather than accumulating *from use of* it. Read-back is the necessary first move, not activation itself. The gap between the two is what a faithfulness test measures — "we read it back" is not the claim "it worked." The [agent-memory-system reviews](../agent-memory-systems/types/agent-memory-system-review.md) operationalise read-back by classifying every system's direction and, for push-capable paths, its selection signal.

## Two Places The Transition Fails

Activation can fail before knowledge reaches the context window — read-back failing — or after it is already there.

**Storage-to-context failure.** Relevant knowledge exists somewhere, but the workflow never retrieves or loads it. This is the ordinary second-brain failure: a note, memory, or prior lesson is stored, but nothing cues it during the task. In a [first-person practitioner report](../sources/the-second-brain-trap-2041486539067154753.ingest.md) about a year spent building a “second brain” with more than 10,000 notes, folders, and AI summaries, the author says he did not use the material while writing, building, or deciding, leading him to start from zero and rethink it. His stated reason is "Because it wasn't accessible in context." ([The Second Brain Trap, section 2](../sources/the-second-brain-trap-2041486539067154753.ingest.md), verbatim). The report is an instance, not evidence that note volume caused the failure or that knowledge graphs generally solve it.

**Context-to-action failure.** Relevant knowledge is visible, but the agent does not connect it to the task, plan, or next action. The problem is not missing information: visible information remains background instead of changing the active computation.

Engländer et al.'s [solution-injection experiments](../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) make this boundary observable. In AppWorld's validation split, "discovery@1 exceeds 90% for all models, yet interaction@1 never surpasses 6.3%" ([Agents Explore but Agents Ignore, section 3.1](../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md), verbatim). The paper counts discovery when an attempt executes a command that surfaces the injected solution in context, and detects interaction when a command references the injected solution. The result separates exposure from observable follow-through, but its artificial injections and process metrics do not estimate ordinary-workflow prevalence or prove semantic incorporation.

Gao and Chen's [coding-agent documentation traces](../sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md) occupy a less controlled point on the same boundary. Within three events of documentation consultation, testing and building were less frequent, while the association with code editing remained unresolved across the unadjusted and adjusted analyses. The authors also warn that a near-zero adjacent read-to-code transition can miss longer-range influence. These observations do not establish that a consulted document contained a task-relevant proposition or caused a later action. Their narrower value is to show why consultation is an exposure measure rather than evidence of activation.

Both failures produce the same practical result: a lesson that could have changed the outcome does not enter the active computation.

The form of the loaded knowledge matters too. Across four self-evolving-agent frameworks, thirteen LLM backbones, and nine environments, [causal perturbations changed behavior more consistently for raw trajectory experience than for condensed experience](../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md); weak dependence on condensed experience persisted when it was the only experience supplied. The intervention result does not establish that the model read a semantically faithful condensation or that condensation always reduces task performance. It does show that reshaping experience can preserve its presence while weakening measured behavioral dependence on it.

## The Expert-Witness Pattern

Models can behave like expert witnesses rather than advisors. An expert witness answers the question asked. An advisor raises the concern the questioner did not know to ask about. Current models can succeed at the first while failing at the second.

The gap is easiest to see in review tasks. A model may explain a failure mode perfectly when prompted directly, yet omit it during an open-ended review where that failure mode would change the decision. The knowledge is retrievable. It is not reliably self-triggering.

A model-internal measurement shows the same separation. In Anthropic's Jacobian-lens experiments, many computations the authors call automatic do not causally route through the verbalizable workspace, though "the same underlying information is available to the model and used for task computations" ([Verbalizable Representations, J-space section](../sources/verbalizable-representations-global-workspace-llms.ingest.md), verbatim). That is presence without use inside one model, not evidence about workflow-level activation.

Two human studies supply historical antecedents for this failure shape, not direct LLM evidence. In an immediate word-recall experiment, [Tulving and Pearlstone](../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) found higher recall when category names were supplied as cues and interpreted the extra recoveries as traces "available in the memory storage, but not accessible for retrieval" ([Availability versus accessibility, abstract](../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md), verbatim). This isolates the storage-to-retrieval gap; it does not study action. In Gick and Holyoak's [Experiment IV](../sources/gick-holyoak-analogical-problem-solving.ingest.md), 11 of 12 hinted participants produced the analogical solution, versus 3 of 15 without the hint, while gist recall of the source story did not differ significantly between groups. This reaches task use, but a human hint/no-hint contrast cannot tell whether the hint retrieved the story or made a retrieved story salient, and it does not establish the same mechanism in an LLM.

The familiar human report is therefore a useful analogy: "I knew this, but it did not occur to me." LLM systems make the control surface more explicit. Prompt context, retrieved notes, tool observations, role assignments, and checklists are the cues that decide what becomes active.

## What Helps

Different interventions target different transitions.

Storage-to-context failures need routing: indexes, search, retrieval filters, skill triggers, maintained summaries, and explicit loading rules.

Context-to-action failures need integration pressure: reflection prompts, "revise the plan in light of observations" steps, mandatory investigation of surprising evidence, salience checks, and process structures that make the agent ask whether visible information should change the current plan. [Process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md): changing the reasoning process can change behavior without changing the final answer format. Treating such a change as an activation intervention is this note's hypothesis, not a result established by that linked note.

Both transitions are affected by context scarcity. More context can help by making knowledge present, but it can also hurt by diluting cues or increasing competition. [Soft degradation can bind before the hard cap even when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) is the broader mechanism: well-formed output can hide the fact that important material in the context was ignored.

## Why It Matters

Evaluations that make the relevant knowledge explicit collapse these stages. They ask whether the model can answer a question, solve a task, or use information after its relevance has been named. That tests capability after activation. It does not test whether the system will activate the right knowledge unprompted.

Evaluation should therefore keep at least four results separate: the artifact exists; the artifact reaches or is consulted by the consumer; the consumer's behavior changes in the intended direction; and the downstream task result improves. Each rung can hold while the next fails. Presence does not establish exposure, exposure does not establish uptake, and uptake does not establish benefit.

The expertise problem makes this worse. The user who most needs the model's latent expertise is often least able to ask the question that would activate it. That is why [elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md), not just better one-off prompts. The missing questions have to come from somewhere outside the novice user and the activation-limited model.

For memory and KB design, the implication is simple: storing more knowledge is not enough, and loading more context is not enough. The system must also create reliable routes from stored knowledge to context, and from context to action.

## Open Questions

- How often does context-to-action failure occur in ordinary agent workflows, and what instrumentation can distinguish exposure, semantic uptake, and downstream effect without treating event proximity as causality?
- Which process structures most cheaply convert visible information into plan updates?
- Does the activation gap reliably grow with distance from the immediate artifact: syntax, operational behavior, system-level consequences?
- Does measuring performance across inference-compute budgets, rather than at one budget, separate activation quality from raw capability, and would such a protocol belong in KB or memory evaluation?

---

Relevant Notes:

- [elicitation-requires-maintained-question-generation-systems](./elicitation-requires-maintained-question-generation-systems.md) — extends: strategies and systems for closing the activation gap described here
- [Soft degradation can bind before the hard cap even when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — complements: soft degradation explains why adding more context can suppress activation through cue dilution and irrelevant-context interference
- [process-structure-and-output-structure-are-independent-levers](./process-structure-and-output-structure-are-independent-levers.md) — enables: reflection and investigation prompts can improve context-to-action integration without changing output format
- [silent-disambiguation-is-the-semantic-analogue-of-tool-fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — see-also: both show how superficially successful output can hide a missing process signal; silent disambiguation does not establish an activation failure
- [the-bug-that-shipped-2035319413474206122](https://x.com/KatanaLarp/status/2035319413474206122) — evidenced-by: deployment-failure insights retrievable on probe but often absent in undirected review
- [The Second Brain Trap ingest](../sources/the-second-brain-trap-2041486539067154753.ingest.md) — evidenced-by: a first-person note-taking failure report that frames the problem as stored knowledge failing to activate in working context
- [Agents Explore but Agents Ignore ingest](../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) — evidenced-by: solution injection separates commands that surface an explicitly labelled complete solution into live context from subsequent commands that interact with it; AppWorld reports discovery@1 above 90% and interaction@1 never above 6.3% across tested models
- [From Agent Behaviour to Agent-Friendly Documentation](../sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md) — evidenced-by: bounded coding-agent traces separate explicit documentation consultation from immediate implementation and verification without treating that separation as a causal activation-failure estimate
- [Faithful Self-Evolvers ingest](../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — evidenced-by: causal perturbations show stronger behavioral dependence on raw trajectories than on condensed experience across the tested frameworks, backbones, and environments; this does not establish semantic preservation or a general performance loss from condensation
- [Availability versus accessibility of information in memory](../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) — evidenced-by: category cues recover additional words in immediate recall, supporting the narrower storage-to-retrieval distinction but not the context-to-action transition
- [Analogical Problem Solving](../sources/gick-holyoak-analogical-problem-solving.ingest.md) — evidenced-by: a relevance hint changes analogical solution use despite comparable story recall in one human task; the result does not establish an LLM mechanism
- [Verbalizable Representations Form a Global Workspace in Language Models](../sources/verbalizable-representations-global-workspace-llms.ingest.md) — evidenced-by: in controlled tasks, the same underlying information can support automatic computation without causally routing through measured J-space, while task demands surface it there for explicit report or flexible inference
