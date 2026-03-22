---
description: Distinguishes stored knowledge (retrievable on direct probe) from contextually activated knowledge (brought to bear during task execution without being directly queried); formalizes the activation gap and the expertise gap
type: note
traits: [has-external-sources]
tags: [llm-interpretation-errors, failure-modes, evaluation]
status: seedling
---

# Knowledge storage does not imply contextual activation

A model can contain relevant knowledge, prove that knowledge on demand, and still fail to surface it when it matters. Storage and activation are distinct, and most capability evaluations test only retrieval under direct query.

## The expert-witness failure mode

The model often behaves like an expert witness rather than an advisor. An expert witness gives full, accurate answers to whatever questions are put to them. An advisor proactively raises concerns the questioner hasn't thought of. The model does the first reliably and the second unreliably — even when the unsurfaced concern would change the outcome.

An experienced practitioner examining a system brings decades of hard-won pattern recognition. They see a design choice and immediately flag the failure mode it invites — not because anyone asked, but because past experience has made that association automatic. The model may have equivalent knowledge and demonstrates it the moment someone asks directly. It just does not volunteer it.

The operative distinction is not *knows* vs. *does not know* but *stored* vs. *activated in this context*. A piece of knowledge is retrievable when the model produces it in response to a direct query. It is contextually activated when the model brings it to bear during task execution without being explicitly asked. Activation failure is the regime where retrievability is high, contextual activation is low, and the value of surfacing the knowledge is high.

## Why activation fails

Activation requires more than stored capability. A plausible decomposition involves at least three stages:

1. **Cue match** — the current context must contain enough signal to trigger retrieval of the relevant knowledge.
2. **Priority arbitration** — even when partially cued, the candidate competes with other activated knowledge for limited reasoning budget.
3. **Commitment** — the model must decide to externalize the candidate rather than suppress it in favor of staying on the apparent task.

This decomposition is proposed, not established — the internal mechanics are not directly observable. But the stages are independently useful for reasoning about where interventions can help: expanding contextual cues, reducing competition, or lowering the threshold for volunteering concerns.

Most "the model can do X" demonstrations pre-supply all three stages by asking directly for X. They test execution after activation, not activation itself.

This is not uniquely an LLM phenomenon. Humans show the same structure: "I knew this, but it didn't occur to me." Inspiration is often just cue arrival — the knowledge existed; the trigger showed up in time. LLM systems make the control surface unusually explicit: prompt context is where cue match succeeds or fails, which makes the gap both more visible and more tractable than its human counterpart.

## The question-generation bottleneck

Whether relevant knowledge activates depends on whether the workflow's questions — user prompts, system prompts, checklist probes — happen to cue it. For many high-value failure modes, no question in the workflow targets the right knowledge. The question is never asked.

This reframes reliability from "does the model know enough?" to "does the workflow ask the right questions?" The model's knowledge is a necessary but insufficient condition. The question set is the binding constraint.

## The expertise gap

The question-generation bottleneck has a structural asymmetry that makes it self-reinforcing: the person who most needs activation scaffolds is usually the person least able to construct them.

The user who delegates a task to the model is typically doing so because they lack the expertise to do it themselves — which means they also lack the expertise to ask the probing questions that would activate the model's deeper knowledge. The safety net gets a hole shaped exactly like the thing it is supposed to catch.

This is not solvable at the individual interaction level. The user cannot ask questions they don't know to ask. The model has the knowledge but won't activate it without appropriate cues. Neither party can independently close the gap. This is why [elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) rather than better individual prompts — the questions must come from somewhere outside the user-model pair.

The expertise gap also explains why activation failure disproportionately affects high-stakes decisions. Routine problems get routine questions that models handle well. Novel or rare failure modes require questions that only experienced practitioners would think to ask — and those are precisely the situations where the user is most likely to be relying on the model as a substitute for that experience.

## The initiative gradient

Empirically, the activation gap scales with distance from the immediate task artifact. Models reliably catch surface-level errors (syntax, type mismatches, logical contradictions). They less reliably catch operational failure patterns (resource exhaustion, race conditions, cascading failures). They rarely catch systemic failures unprompted (deployment topology issues, organizational process gaps, second-order effects across system boundaries).

The further the failure mode lives from the artifact under review, the less likely the context provides adequate cues. This gradient appears consistent across domains, though the specific failure families differ.

## Open questions

- Does the initiative gradient (artifact → operational → systemic) hold consistently across non-technical domains?
- What is the relationship between context window size and activation probability — does more context help or hurt by diluting cues?
- Can the three-stage decomposition (cue match, priority arbitration, commitment) be empirically separated, or is it only useful as a reasoning tool?

---

Relevant Notes:

- [elicitation-requires-maintained-question-generation-systems](./elicitation-requires-maintained-question-generation-systems.md) — extends: strategies and systems for closing the activation gap described here
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — complements: distinguishes per-instance discrimination from aggregate accuracy; this note adds the prior activation requirement
- [evaluation-automation-is-phase-gated-by-comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — parallels: both require stage separation instead of aggregate score reading
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — enables: retrieval scaffolds are oracle-hardening moves for activation-limited settings
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: prompt context determines which interpretations are activated
- [silent-disambiguation-is-the-semantic-analogue-of-tool-fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — example: low activation of critical branches can be masked by superficially successful outputs
- [the-bug-that-shipped-2035319413474206122](../sources/the-bug-that-shipped-2035319413474206122.md) — evidence: deployment-failure insights retrievable on probe but often absent in undirected review
- [towards-a-science-of-ai-agent-reliability](../sources/towards-a-science-of-ai-agent-reliability.md) — context: reliability dimensions motivate separating stored capability from operationally activated behavior
