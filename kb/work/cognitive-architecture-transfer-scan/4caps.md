# 4CAPS: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium

## Remembered model

I remember 4CAPS as a cognitive architecture built around multiple cooperating processing centers, each with limited capacity. Productions or condition–action processes can involve more than one center, and demanding tasks can consume the capacity of a center, recruit additional centers, or expose a bottleneck. The architecture was used to connect cognitive task models with patterns of human performance and brain activation.

The central idea I trust is not a particular anatomical mapping. It is that cognition is both **distributed and locally capacity-constrained**: a system can have ample total machinery while still failing because the component required by this step is saturated.

## Provisional ontology

- **Processing center:** a semi-specialized locus that maintains representations and executes productions.
- **Capacity:** a local budget, not merely one global resource meter.
- **Production:** a condition-triggered operation that may consume capacity in one or several centers.
- **Collaboration:** information exchange or coordinated processing across centers.
- **Recruitment:** bringing another center into the task when the usual allocation is insufficient.
- **Load signature:** the distribution of demand across centers over the course of a task.

This ontology suggests that "context cost" may be too coarse when used as a single scalar. Search output, active instructions, reasoning state, tool coordination, and response composition can interfere differently even when their token counts match.

## Transfer candidates

- **`4CAPS-1` — budget the active system by resource class.** Extend context-cost analysis beyond total tokens to at least volume, interpretive complexity, interference, and required tool transitions. A task can overflow one dimension while spare capacity remains elsewhere.
- **`4CAPS-2` — treat delegation or extra calls as recruitment, not free parallelism.** A second agent or model call helps only if work can be transferred without saturating the shared coordination channel. Measure handoff and reintegration load alongside the capacity it releases.
- **`4CAPS-3` — compare load signatures, not only outcomes.** Two workflows can reach the same answer while placing very different burdens on search, reading, judgment, or verification. The lower-bottleneck workflow may generalize better to larger tasks.
- **`4CAPS-4` — design overload signatures.** If instruction interference, excessive candidate retrieval, and tool-output volume produce distinguishable failure patterns, those patterns could drive different remediation instead of the generic response "use less context."

These candidates sharpen the existing claim that [agent context is constrained by soft degradation, not hard token limits](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md): the degradation may be local to a functional component before the overall window is full.

## Method worth borrowing

The methodological attraction is joint prediction. An architecture should not merely explain whether a task succeeds; it should predict where work accumulates and how behavior changes when a particular capacity is stressed. For Commonplace, an analogous evaluation would vary one load source at a time—retrieved candidates, instruction density, link traversal, or review obligations—and observe both quality and execution trace.

## Non-transfer and failure modes

- Mapping LLM components or tool calls directly onto human cortical regions would be decorative and probably wrong.
- A fixed inventory of centers could prematurely freeze what should remain empirical resource classes.
- "Recruit another agent" can increase shared-state and synthesis costs enough to worsen the bottleneck.
- Human task-time parameters should not be imported as agent-system constants.

## Grounding questions

1. What exactly is capacity in 4CAPS, and how is it quantified?
2. Are centers anatomically fixed, functionally defined, or both?
3. What mechanism governs recruitment and inter-center communication?
4. Which published cases distinguish local-capacity predictions from a generic complexity account?
