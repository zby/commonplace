# LIDA: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

LIDA—the Learning Intelligent Distribution Agent architecture—is remembered as an implementation-oriented development of Global Workspace Theory. A recurring cognitive cycle moves from perception and recognition into a workspace, where attention codelets form coalitions. A winning coalition is globally broadcast, allowing otherwise specialized processes to respond. Action schemes compete for selection and execution. Perceptual, episodic, procedural, and attentional learning can occur around the cycle.

The key transferable distinction is a causal chain: information can be sensed, recognized, present in a workspace, selected for broadcast, received by action-selection processes, and learned from—each transition can succeed or fail independently.

## Provisional ontology

- **Percept:** interpreted current input.
- **Workspace:** transient situational model assembled from perception and memory.
- **Attention codelet:** small process seeking support for some salient coalition.
- **Coalition:** a candidate content bundle competing for global access.
- **Global broadcast:** selected content made widely available to specialized processes.
- **Action scheme:** a possible response conditioned on the broadcast and current state.
- **Action selection/execution:** commitment followed by environmental effect.
- **Learning:** changes to memories or selection tendencies induced by the cycle.

This offers a finer process vocabulary for the existing [storage/read-back/activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) distinction. "Loaded into the prompt" may correspond only loosely to workspace presence; influence on action still requires uptake and selection.

## Transfer candidates

- **`LIDA-1` — make a context bundle an explicit broadcast artifact.** Record what was selected for task-wide availability, why it won, which downstream processes consumed it, and whether it changed action.
- **`LIDA-2` — separate candidate context from broadcast context.** Search results, open files, and tentative thoughts can coexist in a private workspace without all receiving equal global authority or salience.
- **`LIDA-3` — evaluate context by downstream uptake.** A successful broadcast should change proposals, checks, or actions in the processes for which it was selected. Mere presence is insufficient.
- **`LIDA-4` — attach learning to cycle events.** Surprises, selection conflicts, and action outcomes create different update candidates. Do not send all experience through one generic summarizer.
- **`LIDA-5` — treat broadcast capacity as governance.** What enters the shared context can coordinate the system but can also propagate error. Selection policy should consider authority and uncertainty, not just salience.

## Method worth borrowing

Instrument an agent loop as event transitions: available → recognized → workspace → candidate coalition → selected/broadcast → consumed → action → outcome → retained update. Counterfactually remove or replace content at one transition and observe whether the predicted downstream effect disappears. This is stronger evidence of activation than asking the model to recite the content.

## Non-transfer and failure modes

- A prompt or shared scratchpad is not automatically a Global Workspace in the theoretical sense.
- Fixed cognitive-cycle timing may be inappropriate for asynchronous tools and human-in-the-loop workflows.
- Global broadcast can waste context or spread low-quality material to every subsystem.
- The architecture's many memory and codelet types may encourage premature one-component-per-term implementation.

## Grounding questions

1. What is the canonical LIDA cognitive cycle and which stages may overlap?
2. What makes a coalition win attention, and what receives the broadcast?
3. Which learning mechanisms are actually implemented versus architectural aspirations?
4. What observations distinguish broadcast from ordinary central-state access?
