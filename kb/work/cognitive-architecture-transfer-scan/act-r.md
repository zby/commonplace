# ACT-R: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

ACT-R models cognition as the interaction of specialized modules through a small set of buffers. Declarative memory contains chunks; procedural memory contains productions. A production matches the currently buffered state and initiates operations such as requesting a retrieval. Chunk activation reflects factors including past use and current cues, and activation affects retrieval probability and latency. Production utilities arbitrate among applicable actions. Learning changes chunks, activation, utilities, and—under suitable conditions—can compile sequences of productions into a faster production.

The most reusable point is architectural: possession, accessibility, selection, and execution are separate events with separate failure modes.

## Provisional ontology

- **Chunk:** a typed bundle of declarative content.
- **Module:** a specialized subsystem such as declarative memory, vision, or motor control.
- **Buffer:** a narrow interface exposing a module's current result to procedural control.
- **Production:** a condition–action rule over buffered state.
- **Activation:** context-sensitive readiness of a chunk for retrieval.
- **Utility:** learned action preference among matching productions.
- **Retrieval request/result/failure:** explicit stages rather than an invisible read.
- **Compilation:** construction of a faster procedural path from a practiced sequence.

ACT-R therefore offers a more articulated vocabulary than "the agent knows the note." A retained artifact can exist, match a cue weakly, lose retrieval competition, arrive in context, or still fail to affect the selected action.

## Transfer candidates

- **`ACTR-1` — model retrieval as a state transition with failure.** Record the cue, candidate set, selected artifact, latency/cost, and whether the result changed the next decision. This would connect retrieval evaluation to [contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) rather than stopping at relevance.
- **`ACTR-2` — distinguish content activation from action utility.** A note can be highly relevant yet lose to a habitual workflow. Retrieval rank and procedure-selection rank should not be conflated.
- **`ACTR-3` — treat frequency, recency, and situational cues as different retrieval evidence.** A single similarity score hides whether an artifact is generally practiced, recently useful, or specifically cued by the current situation.
- **`ACTR-4` — use repeated deliberation as a proceduralization signal.** When the same multi-step interpretation repeatedly resolves the same condition, propose a skill, validator, route, or other fast path. This is already adjacent to the [two-layer execution-system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) account; ACT-R may contribute sharper eligibility and miscompilation questions.
- **`ACTR-5` — expose narrow interfaces between subsystems.** A module may hold rich state while only a small result crosses into the active decision context. This is a useful restraint on "load everything" memory designs.

## Method worth borrowing

ACT-R tries to make a process account earn its keep through traces and quantitative consequences, not only plausible verbal decomposition. The analogue for Commonplace is to evaluate a proposed memory mechanism against observable selection sequences, retries, misses, costs, and outcome changes. Even without importing ACT-R's equations, explicit predicted traces would make architecture claims easier to falsify.

## Non-transfer and failure modes

- ACT-R's fixed modules and single-buffer-like bottlenecks should not be assumed to describe an LLM agent.
- Human latency equations do not automatically transfer to model calls or filesystem operations.
- Frequency and recency can amplify popular but wrong artifacts; authority and provenance remain separate.
- Compilation can overgeneralize. A fast path needs scope conditions, lineage, validation, and a fallback—not merely recurrence.

## Grounding questions

1. Which activation terms and learning mechanisms are central versus optional in current ACT-R?
2. What exact conditions and safeguards govern production compilation?
3. How are retrieval failures and partial matching represented?
4. Which empirical methods best distinguish ACT-R's process account from alternative models?
