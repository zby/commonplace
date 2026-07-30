# DUAL: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium

## Remembered model

I remember DUAL as a hybrid cognitive architecture associated with Boicho Kokinov and analogy models such as AMBR. Knowledge is distributed among many small hybrid agents or micro-agents. Each carries local symbolic content or procedures while participating in connectionist activation dynamics. Temporary coalitions of these agents form the context in which perception, memory retrieval, and reasoning proceed. Retrieval and analogy are therefore constructive and context-sensitive rather than cleanly separated stages.

The exact agent types and network dynamics need checking. The potentially valuable core is a distinction between the **durable representational population** and the **temporary coalition that becomes operative now**.

## Provisional ontology

- **Micro-agent:** a small representational or procedural unit with local behavior.
- **Link:** a durable or weighted relation through which activation and constraint propagate.
- **Activation:** transient readiness to participate in current processing.
- **Coalition:** a mutually supporting active assembly that constitutes the current interpretation or context.
- **Context:** not a static input bundle but the active subnetwork produced during processing.
- **Emergent macrostructure:** a larger representation or reasoning result not stored as one central object.

This adds a useful intermediate object between repository and prompt: the active coalition of mutually reinforcing concepts and artifacts that shapes interpretation, including items never literally concatenated into one document.

## Transfer candidates

- **`DUAL-1` — distinguish durable graph from active subgraph.** Authored links describe possible relations; a task induces a much smaller operative network. Retrieval evaluation should examine the induced subgraph, not count stored links.
- **`DUAL-2` — let retrieval and interpretation interact.** An initially retrieved artifact can change the concepts used for the next retrieval. Context assembly may need iterative spreading and query reformulation rather than one top-k call.
- **`DUAL-3` — model coalition support explicitly.** Several individually weak cues can jointly justify loading a note. Ranking candidates independently misses relational support among them.
- **`DUAL-4` — keep local semantics inspectable.** Distributed activation is safer when each participating unit still exposes the claim, procedure, or relation it contributes. This may offer a middle path between a fully opaque embedding process and a centralized symbolic controller.
- **`DUAL-5` — evaluate context stability.** Small cue changes should sometimes reorganize the coalition, but uncontrolled oscillation or arbitrary path dependence would make the system unreliable. Stability under irrelevant perturbations is an evaluation target.

## Method worth borrowing

Instead of evaluating retrieval one document at a time, construct tasks whose solution requires a particular **configuration** of artifacts. Measure whether the system assembles the necessary coalition, which distractor coalitions compete, and how an early cue changes later retrieval. This is closer to compositional memory evaluation than isolated relevance judgments.

## Non-transfer and failure modes

- A micro-agent for every concept can create an unmaintainable ontology and expensive dynamics.
- Emergence can become an excuse for not specifying causal responsibility.
- Weighted activation may amplify densely linked conventional material and suppress novel but decisive evidence.
- A text context window and an active cognitive coalition are not the same object; the analogy must identify the actual causal channel.

## Grounding questions

1. What exactly is hybrid inside a DUAL micro-agent?
2. How are coalitions formed, stabilized, and dissolved?
3. In DUAL/AMBR, how do memory retrieval and analogical mapping constrain one another?
4. Which behaviors depend on distributed coalition dynamics rather than the symbolic structures alone?
