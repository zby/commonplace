# Informed direction and autonomous judgment

## Purpose and status

Posed by the Commonplace operator on 2026-11-08 while discussing agents continuing substantial implementation without surfacing difficulties that could change the operator's decision. The operator chose to park the hypothesis and wait for examples from our own KB work, rather than promote a claim from an external anecdote. This workshop preserves the question and the distinctions needed to examine such examples.

**Status: parked hypothesis; no admitted local cases.** This is not a new execution policy, a claim about training, or authorization to run experiments, retrieve private sessions, or modify other artifacts. Ordinary work can supply cases; the workshop does not commission a search through session histories. Its presence in the Active Workshops list makes it discoverable, not automatically supplied to every agent.

## Working hypothesis

An agent may treat an operator's requested direction as informed acceptance of its difficulties, while the operator relies on the agent to identify and report those difficulties. Work then continues without either participant checking the assumption that matters to the goal.

The possible mistake is not obedience itself. It is inferring that the requester understands and accepts a consequential risk without adequate grounds. A human collaborator may reasonably pursue an apparently infeasible approach when a trusted expert requests it. The expert may understand the standard objection, have information the collaborator lacks, or intend original research. Conversely, a novice may issue the same instruction expecting expert guidance. Knowledge of the requester changes the interpretation of the request.

The hypothesis therefore concerns how the agent uses evidence about the operator's knowledge, purpose, and reliance on its judgment. It does not assume that every instruction requires a warning or confirmation.

## Why this matters for autonomous work

An interactive session can contain consequential autonomous decisions. User messages may select the next activity without supervising the design assumptions behind it. Message frequency alone does not establish informed oversight.

In longer work, implementation progress may further obscure an unresolved obstacle. Passing component tests or completing supporting infrastructure does not establish the intended end-to-end function. A possible failure is continuing to present delivery progress after the work has effectively become an investigation into whether the approach can deliver at all. That transition may be reasonable, but it changes what the operator is committing to.

The competing requirements are real: act autonomously, respect direction, use technical judgment, support novel research, and report consequential difficulties without interrupting for every uncertainty. Neither unconditional compliance nor automatic refusal resolves them. Raising a decision-relevant objection may reconcile them, but whether to investigate independently, report without pausing, or ask for a decision depends on the task and granted discretion. This workshop does not prescribe a universal escalation gate.

## Comparison with conceptual blending: preserving uncertainty may not permit action

In a follow-up on 2026-11-08, the operator identified a possible common structure with the [conceptual-blending workshop](../epistemic-relevance-and-conceptual-blending/README.md): the agent faces a choice without the information needed to settle it, under conflicting pressures to acknowledge what it does not know and to finish the task. This is a proposed comparison, not evidence that the two failures share a cause.

The operator distinguished opposite errors involving a second reading of the request:

- In conceptual blending, the agent develops an additional reading but merges it into the main line without warrant. It could instead pursue both readings separately, preserving the distinction without settling which was intended.
- Here, the agent may fail to consider the additional reading: the operator could be relying on its feasibility judgment rather than knowingly accepting the difficulty. Following the explicit direction alone can miss that reliance.

The candidate shared requirement is to consider an alternative interpretation without silently adopting it or blending it into the explicit request. But that does not supply a general solution for autonomous action.

In an interactive session, the agent can surface the objection and establish the operator's understanding or purpose. Without an available operator, the readings may require incompatible actions: continue a knowingly exploratory attempt, or stop or redirect work intended to deliver a feasible result. The agent cannot necessarily do both. An asynchronous warning preserves reporting but does not determine the next action.

Some interpretive uncertainties can therefore remain explicit in an output; others must be resolved, or provided for, before consequential action. Prior knowledge of the operator, delegated discretion, or an agreed fallback might supply grounds for action. Without those grounds, further technical reasoning cannot establish the operator's intended commitment, and there may be no well-grounded choice available. This is a limit to investigate, not a new requirement to stop whenever intent is uncertain.

## Distinctions to preserve

- **Requested versus informed continuation.** An instruction establishes what was requested, not necessarily what risks the operator understood.
- **Noticing versus reporting.** Failure to identify a difficulty differs from identifying it but treating operator direction as a reason not to mention it.
- **Available objection versus prior knowledge.** Producing a persuasive objection after a targeted prompt does not show that the agent recognized it earlier or that the objection is correct.
- **Difficulty versus impossibility.** An untested assumption, a failed implementation, and a demonstrated impossibility warrant different reports. Novel work can reasonably proceed despite low confidence.
- **Objection versus veto.** Surfacing a concern need not withdraw support for a knowingly exploratory choice.
- **Reflection versus changed decisions.** Critical prose matters here only insofar as it informs what is tested, built, deferred, abandoned, or knowingly pursued.

## Origin and evidence boundary

The discussion arose from the [Goedecke essay ingest](../../sources/llms-are-terrible-at-designing-ai-systems.ingest.md) and the [original memory-tool report ingest](../../sources/vibe-coding-agent-memory-contradictions.ingest.md). These are pointers to the motivating accounts, not admitted evidence for this hypothesis. No claim about the actual division of judgment in those sessions is adopted here. Original session logs would be needed to examine who selected the direction, what objections appeared when, and what the operator knowingly accepted; seeking those logs is not commissioned.

The present human-agent discussion supplied the hypothesis and corrected its framing: from poor architecture choice, through failure to reflect or report difficulties, to the question of whether the agent assumed an informed requester. These successive formulations are one discussion, not independent observations.

## Competing explanations and counterexamples

A local episode might instead show missing technical knowledge, poor problem diagnosis, goal drift, excessive confidence, weak progress reporting, or simple failure to test the central function. It might show an explicit warning followed by informed operator acceptance. It might also show reasonable independent investigation within delegated authority, with no decision yet requiring interruption.

The authority-related hypothesis earns specificity only if the evidence distinguishes it from those alternatives. An agent's retrospective explanation that it was obeying the operator is a conjecture about the cause, not privileged access to it. Do not infer training deficiencies from the behavior alone.

Useful counterexamples include an agent appropriately continuing after an informed choice, raising a concern without stopping useful work, and over-warning an expert about an already accepted risk. A record containing only failures cannot establish where the boundary should lie.

## Evidence to retain when a case arises

The aim is to reconstruct the division of judgment at the consequential decision, not collect a complete transcript by default. Preserve enough contemporaneous material to establish:

- The requested work, intended result, and discretion granted to the agent.
- What the agent could know about the operator's expertise, research purpose, and dependence on its advice.
- The difficulty and its basis, including whether it was visible then or identified only retrospectively.
- Any objection actually raised, its specificity, and the operator's response.
- Subsequent tests, construction, progress claims, and changes of direction.
- Whether an alternative reading was considered, kept separate, blended into the main course, or omitted.
- Whether useful work could preserve both readings, or the next action required choosing between them; if so, what prior agreement or delegated discretion supplied grounds for the choice.
- What remains unknown, and which rival explanation best fits the available evidence.

Keep exact excerpts or stable session references where available. Distinguish observations from participant recollections and later interpretations. Count successive corrections in one task as one episode. No formal case schema is needed before the first example shows what information is useful.

## Neighbors, reopening, and closure

[Knowledge storage does not imply contextual activation](../../theory/knowledge-storage-does-not-imply-contextual-activation.md) supplies the existing distinction between answering a prompted question and raising an unasked concern. The [structural-coherence workshop](../agent-curiosity-and-structural-coherence/README.md) investigates failures to originate structural concerns during otherwise locally competent work. These are neighboring questions, not evidence of one shared cause. The operator subsequently identified conceptual blending as the other failure under comparison; the proposed relationship and its autonomous-action limit are retained above.

Reopen when an independently arising local case materially distinguishes unnoticed difficulty, unreported difficulty, assumed informed direction, or informed acceptance. A strong counterexample is equally useful. The first review should ask whether this framing adds anything beyond existing knowledge-use and delegation accounts, and narrow, split, or reject it accordingly. No recurrence count or deadline is imposed.

Close by extracting a warranted contribution, documenting why the hypothesis is rejected or already covered, or an explicit operator decision to stop. Follow the workshop collection lifecycle: preserve any durable result in its appropriate collection, then remove this directory and its active entry. Until then, keep this as a focused question rather than expanding it into a general theory of autonomous agency.
