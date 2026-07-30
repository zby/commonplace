# SOSIEL: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium

## Remembered model

SOSIEL is remembered as an agent architecture for social simulation and policy analysis, aimed at modelling heterogeneous individuals or organizations whose behavior changes through experience, innovation, imitation, and social influence. Agents have needs, goals, values, or preferences; select among behavioral rules; evaluate satisfaction or outcomes; and may generate or adopt new rules when existing behavior is inadequate. Population-level patterns emerge from agents situated in social and institutional environments.

The exact cognitive cycle and learning mechanisms need checking. The distinctive transfer is to treat adoption and effectiveness as **population-relative**, not as properties of one idealized agent.

## Provisional ontology

- **Actor/agent:** a member of a heterogeneous population with local state and capabilities.
- **Need/value/goal:** a dimension against which outcomes matter.
- **Behavioral alternative/rule:** a candidate action pattern available in a situation.
- **Satisfaction or discrepancy:** feedback comparing outcomes with aspirations.
- **Innovation:** creation or modification of a behavioral alternative.
- **Social learning:** adoption influenced by other actors' behavior or success.
- **Role/institution:** external constraints and affordances shaping available behavior.
- **Macro-pattern:** aggregate outcome emerging from many local selections and interactions.

For Commonplace, the relevant population may be models, harnesses, maintainers, reviewers, and consuming projects. A methodology can work for one expert agent yet fail as shared infrastructure because adoption, interpretation, and incentives differ.

## Transfer candidates

- **`SOSIEL-1` — evaluate methodology across actor profiles.** Test instructions and artifact types with different models, experience levels, tool access, operating systems, and task roles. Mean success can hide a subgroup failure.
- **`SOSIEL-2` — distinguish invention from diffusion.** Creating a better rule does not make it behaviorally operative across the project. Discovery, codification, publication, loading, uptake, and sustained use are separate transitions.
- **`SOSIEL-3` — model social copying as a memory pathway.** Agents and maintainers copy examples, conventions, and neighboring artifacts even when no formal rule instructs them. Examples therefore have behavioral authority that should be evaluated.
- **`SOSIEL-4` — use dissatisfaction as a search trigger, not proof of improvement.** Repeated failure can justify generating alternatives, while reject-capable evaluation must still decide whether the new behavior is better.
- **`SOSIEL-5` — examine policy distributional effects.** A stricter validation or review policy can improve aggregate quality while imposing disproportionate cost on certain artifact types or workflows.

## Method worth borrowing

Run multi-profile simulations or empirical trials where actors encounter the same methodology under different resources and incentives. Track who discovers a rule, who adopts it, local outcomes, abandonment, and system-level effects. Sensitivity analysis matters more than a single plausible trajectory.

## Non-transfer and failure modes

- Social simulations can produce precise-looking outcomes from weak behavioral assumptions.
- LLM instances do not have human needs or social identities; functional actor profiles must replace anthropomorphic mapping.
- Emergent aggregate patterns do not establish that the micro-level theory is true.
- Optimization for adoption can favor easy but inferior methodology.
- The remembered description may omit SOSIEL's domain-specific constructs or overstate its generality.

## Grounding questions

1. What does SOSIEL stand for and what is its canonical agent cycle?
2. How are needs, values, satisfaction, innovation, and imitation represented?
3. Which policy domains and empirical calibration methods have been used?
4. What evidence distinguishes the architecture from a generic agent-based simulation framework?
