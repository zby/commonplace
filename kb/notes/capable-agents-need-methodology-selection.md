---
description: A capable agent may know many individually relevant but mutually incompatible approaches, so task control requires selecting a governing methodology rather than merely supplying relevant knowledge
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, context-engineering, methodology]
---

# A capable agent needs methodology selection, not just relevant knowledge

A capable pretrained agent does not merely contain more facts. It contains a larger repertoire of ways to approach the same task: exploratory or specification-first development, centralized planning or delegated initiative, formal proof or empirical testing, adversarial criticism or charitable interpretation. Several of these approaches may be relevant at once while recommending incompatible actions.

This creates a control problem distinct from knowledge retrieval. Supplying relevant facts answers **what information should be available?** Selecting a methodology answers **which coherent way of interpreting and acting on that information should govern this task?** More capability does not remove this problem. By increasing the number of plausible approaches the model can competently execute, it can make methodology selection more consequential.

A methodology cue can therefore change behavior even when it supplies almost no new domain facts. A gloss such as “preserve intent and constraints; delegate execution-time choice of means” can select intent-based command, local initiative, and adaptation under constraints. The bare name *Auftragstaktik* is a still more compact candidate selector, but [intent-framed delegation is a control regime, not a short prompt](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) explains why the name alone does not fix the intended transferable package. The useful effect is not that the cue teaches the model those ideas from scratch, but that it makes one already learned cluster govern the task instead of neighboring alternatives.

This extends [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). That note distinguishes knowledge that exists from knowledge that becomes action-relevant. Methodology selection is a stronger case: the problem is not only whether a relevant proposition activates, but which mutually constraining set of propositions and decision rules becomes the frame for action.

The distinction matters especially for open-ended agent work. A prompt that only states the objective leaves the model to improvise a method from its repertoire. A prompt that also selects a methodology constrains many downstream decisions at once without prescribing each step. This is why greater agent competence can support less procedural instruction without implying less control: control can move from step specification toward methodology selection, mission specification, and explicit constraints.

The claim is not that every task needs a named methodology. Some tasks have one overwhelmingly conventional solution, and some methodologies are too weakly represented or too ambiguous for a short cue to select them reliably. When selecting the wrong reconstruction would change consequential choices, use a disambiguating gloss or target-model evidence from representative cases. The claim is that where several coherent approaches could plausibly govern the work, methodology selection is a distinct control variable and should not be collapsed into generic relevance or capability.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: separates stored knowledge, contextual exposure, and behavioral activation; methodology selection concerns which coherent behavioral regime becomes active
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — mechanism: when the governing method is not settled, capable agents must supply it through interpretation
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — complements: once selected, a methodology governs only the decisions its content actually settles
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivates: selecting a methodology can constrain many decisions without spending context on a complete procedure
