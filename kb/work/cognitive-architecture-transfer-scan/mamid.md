# MAMID: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** low-medium

## Remembered model

I remember Eva Hudlicka's MAMID work as a methodology or architecture for modelling affect and individual differences in cognition. Emotional state and personality-like parameters influence attention, perception, interpretation, memory retrieval, decision thresholds, and action selection rather than appearing only as explicit symbolic content. The remembered emphasis is on tracing how a global state creates systematic cognitive bias across several processing stages.

I do not trust the exact expansion of MAMID or whether it should be classified as one architecture, a modelling methodology, or a family of models. The transferable conjecture concerns **control-state modulation**.

## Provisional ontology

- **Control state:** a relatively global condition that modulates processing.
- **Appraisal:** evaluation of a situation against goals, expectations, or coping capacity.
- **Trait/parameter:** a more stable bias in how state changes or influences processing.
- **Bias vector:** changes to salience, retrieval, interpretation, thresholds, depth, or risk preference.
- **Stage-specific effect:** the point in the process where modulation becomes causal.
- **Behavioral signature:** a cross-task pattern predicted by the control state.

For agents, useful non-anthropomorphic control states might include urgency, epistemic caution, exploration pressure, failure recovery, or review strictness. These should be modeled as settings that alter selection and thresholds, not as prose mood labels.

## Transfer candidates

- **`MAMID-1` — make global operating stance explicit.** A workflow can enter exploratory, conservative, incident-response, or publication-ready modes that alter search breadth, acceptance thresholds, verification depth, and willingness to modify state.
- **`MAMID-2` — locate the causal stage of a bias.** If an agent overlooks dissent, determine whether dissent was not retrieved, was interpreted as irrelevant, lost action competition, or failed a too-strict evidence threshold. "Bias" without a processing locus is not actionable.
- **`MAMID-3` — test a stance across several tasks.** A real control parameter should produce a coherent behavioral signature rather than a one-off wording change.
- **`MAMID-4` — separate actor profile from artifact authority.** Different models or operators may require different presentation and verification, but the truth or binding force of a KB artifact must not depend on the consumer's simulated temperament.
- **`MAMID-5` — govern state transitions.** Urgency that lowers deliberation cost may be useful during response and dangerous during durable knowledge promotion. Entry, exit, and reset conditions matter.

## Method worth borrowing

Use stage-local perturbations. Hold the task and retained knowledge fixed, vary one control-state parameter, and measure candidate generation, retrieval diversity, evidence weighting, decision threshold, and final action separately. This can show whether an "agent persona" has a real process effect or merely changes style.

## Non-transfer and failure modes

- Anthropomorphic emotion labels can obscure ordinary control parameters and invite unsupported psychological claims.
- A global stance can amplify error across the entire pipeline.
- Individual-difference models fitted to humans may not explain variation across LLMs, prompts, or harnesses.
- The remembered description may merge MAMID with Hudlicka's broader affective-computing work.

## Grounding questions

1. What does MAMID stand for, and is it an architecture or a modelling methodology?
2. Which cognitive stages and affect variables are explicitly represented?
3. How are personality, transient emotion, appraisal, and behavior causally connected?
4. Which experiments distinguish stage-specific modulation from generic parameter fitting?
