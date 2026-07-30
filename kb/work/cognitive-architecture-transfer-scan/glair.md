# GLAIR: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium

## Remembered model

I remember GLAIR as the Grounded Layered Architecture with Integrated Reasoning, associated with SNePS and embodied or situated agents. Its layers connect a knowledge/reasoning level to perceptual and motor implementation and then to sensors and actuators. The same agent can reason in symbolic terms while its primitive actions and percepts remain grounded through lower-level processes in a particular environment.

The layer names and boundaries need verification. The transferable issue is clear: a knowledge-level symbol such as "open," "inspect," or "notify" has behavioral meaning only through a maintained path to sensing or action.

## Provisional ontology

- **Knowledge-level term:** a symbol used in beliefs, plans, or reasoning.
- **Primitive action/percept:** the lowest operation still meaningful to the reasoning layer.
- **Perceptuo-motor implementation:** the environment-specific process realizing that primitive.
- **Sensor/actuator state:** raw interface to the environment.
- **Grounding relation:** the maintained mapping from symbol to possible perception or action.
- **Agent body/interface:** the set of capacities through which knowledge can affect and be corrected by the world.
- **Situated state:** current environmental and self state relevant to interpretation.

In Commonplace terms, an instruction's prose, the tool or command that realizes it, and the filesystem or service state it changes are different layers. A link between prose and command name does not prove the grounding path works.

## Transfer candidates

- **`GLAIR-1` — require an execution grounding path for binding instructions.** For every operational verb in a high-authority artifact, identify the consumer, callable interface, preconditions, observable effect, and failure signal. This makes [behavioral authority](../../notes/definitions/behavioral-authority.md) concrete.
- **`GLAIR-2` — test grounding, not documentation correspondence.** Validate that the named command exists and produces the claimed state transition in the target environment; prose and implementation can agree lexically while the path is broken.
- **`GLAIR-3` — keep environment adapters below stable knowledge terms.** Cross-platform command differences should be handled at the implementation boundary where possible, leaving the conceptual operation stable.
- **`GLAIR-4` — include perception grounding.** An agent must not only execute actions but detect their real outcomes. "Validation passed" should map to checked output and exit state, not to the intention to run validation.
- **`GLAIR-5` — expose embodiment boundaries in system reviews.** A memory or agent architecture should say which capacities belong to the model, harness, tools, repository, and humans. Otherwise the cognitive story silently credits the wrong component.

## Method worth borrowing

Trace a small set of knowledge-level operations down and back up the stack: symbolic request → adapter/tool invocation → environment transition → sensed result → belief update. Fault-inject each boundary. This can reveal instructions that are semantically clear but operationally ungrounded.

## Non-transfer and failure modes

- Calling a CLI an agent's "body" can obscure more than it explains unless a design decision follows.
- Layering can introduce duplication and stale mappings between prose, wrapper, command, and environment.
- Some knowledge artifacts are advisory and intentionally lack direct execution paths.
- The remembered relationship between GLAIR and SNePS may be incomplete or historically specific.

## Grounding questions

1. What are GLAIR's canonical layers and their exact responsibilities?
2. How are primitive actions and percepts grounded across layers?
3. How does the architecture represent the agent itself, time, and ongoing action?
4. Which demonstrations test grounding rather than symbolic reasoning alone?
