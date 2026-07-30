# R-CAST: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium

## Remembered model

I remember R-CAST as a recognition-primed, collaborative-agent architecture associated with team cognition and recognition-primed decision making. Agents use experience or process knowledge to recognize situations and likely courses of action. They also reason about teammates' information needs, shared plans, or decision requirements so that communication can be proactive rather than limited to explicit requests.

The acronym expansion, exact relation to CAST, and internal module boundaries need checking. The promising transfer is that collaboration depends on modelling **what information another actor needs for its decision**, not merely maintaining a common data store.

## Provisional ontology

- **Situation pattern:** a recognized configuration linked to prior experience or a decision process.
- **Decision/process model:** structure saying which information matters at which stage.
- **Information requirement:** a fact or update needed by an actor to choose or execute well.
- **Shared mental/process model:** sufficiently aligned expectations about roles, state, and next actions.
- **Teammate model:** beliefs about another actor's knowledge, task, and unmet needs.
- **Proactive communication:** sending information because its need is inferred, not requested.
- **Recognition-primed option:** a plausible action retrieved from experience before exhaustive comparison.

## Transfer candidates

- **`RCAST-1` — package handoffs by downstream decision.** A parent agent or workflow should send the goal, relevant state, constraints, evidence, and expected output that the recipient cannot cheaply infer—not the whole upstream transcript.
- **`RCAST-2` — make information requirements part of roles.** Reviewers, implementers, maintainers, and schedulers need different views of the same artifact. A memory system should model these consumer-specific requirements explicitly.
- **`RCAST-3` — push only when a decision-relevant condition is met.** Proactive context loading should be tied to a known downstream choice or failure mode; otherwise "helpful" notifications become attention pollution.
- **`RCAST-4` — verify common ground at coordination boundaries.** A shared file does not prove shared interpretation. Handoffs should include compact checks of goal, terminology, authority, and completion criteria.
- **`RCAST-5` — retrieve a first workable pattern, then simulate it.** Experience-based recognition can reduce option search, but an unfamiliar or high-consequence situation should trigger critique or alternative generation before commitment.

These ideas refine [frontloading](../../notes/frontloading-spares-execution-context.md): caller-resolved information is worth packaging when it is known and decision-relevant to the recipient.

## Method worth borrowing

Construct team tasks where one actor observes information that another needs but did not request. Compare full broadcast, request-only communication, and inferred-need communication. Measure missed decisions, irrelevant messages, recovery from wrong teammate models, and the context cost imposed on recipients.

## Non-transfer and failure modes

- A wrong teammate model can confidently push misleading context or conceal needed information.
- "Shared mental model" can become vague unless represented through testable role, state, and decision expectations.
- Recognition-primed action can reproduce past local habits under distribution shift.
- Human-team findings may not transfer to agents that share files, context, or model weights in unusual ways.

## Grounding questions

1. What does R-CAST stand for and how does it differ from CAST?
2. How are process models, information requirements, and teammate beliefs represented?
3. What mechanism triggers proactive information sharing?
4. Which experiments isolate collaboration gains from extra communication volume?
