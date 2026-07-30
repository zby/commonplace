# Hierarchical Temporal Memory: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high on core concepts, lower on current canonical algorithms

## Remembered model

Hierarchical Temporal Memory (HTM), associated with Jeff Hawkins and Numenta, is a biologically inspired approach centered on sparse distributed representations, sequence learning, prediction, and online adaptation. In the remembered account, a spatial-pooling-like process forms stable sparse representations, while temporal-memory mechanisms learn transitions in context. Cells within a column can represent the same feedforward feature in different sequential contexts. The system can maintain multiple predictions and use prediction failure as anomaly evidence.

The valuable abstraction is that memory should encode **what tends to follow in context**, not only which static items resemble the current input.

## Provisional ontology

- **Sparse distributed representation (SDR):** a high-dimensional pattern with a small active subset and overlap-based similarity.
- **Column/cell:** shared feedforward content differentiated by temporal context.
- **Context:** prior active state that disambiguates the current representation.
- **Transition:** a learned relation from contextual state to likely next state.
- **Prediction:** partial activation of possible future states.
- **Burst/surprise:** failure of an expected contextual prediction.
- **Anomaly score:** degree to which current input violates predicted structure.
- **Online learning:** continual local update rather than a sharp training/deployment split.

For Commonplace, "sequence" need not mean raw token order. It can mean workflow transitions: proposal → review → decision → implementation → validation, or query → source → synthesis → action.

## Transfer candidates

- **`HTM-1` — evaluate episodic memory by transition prediction.** A useful episode model should help predict the next needed artifact, check, or failure mode given the current workflow state, not merely retrieve similar past text.
- **`HTM-2` — make violated expectations a discovery signal.** Surprise is more informative when attached to an explicit predicted transition. "A command documented as available was absent" is actionable because it violates a model, not simply because it is rare.
- **`HTM-3` — retain several possible continuations.** Context engines should preserve alternative next-step hypotheses until evidence disambiguates them, especially at workflow branch points.
- **`HTM-4` — represent the same item differently by context.** One note can play different roles in authoring, review, or incident response. A retrieval representation that ignores current process state may merge functionally different uses.
- **`HTM-5` — separate anomaly from error.** An unexpected transition deserves inspection but may represent improvement, environmental change, or a new valid case. Anomaly should trigger inquiry, not automatic rejection.

## Method worth borrowing

Construct workflow sequence benchmarks. Train or configure a selector on ordinary artifact/action transitions, then hold out valid variants, invalid transitions, and true novelties. Measure next-step prediction, anomaly calibration, adaptation without catastrophic overwriting, and whether flagged surprises lead to useful memory updates.

## Non-transfer and failure modes

- HTM's biological interpretation and empirical standing should not be inherited with its engineering abstractions.
- Markdown artifacts do not naturally form fixed-width SDRs; forcing them into one may discard semantics and authority.
- Frequent workflow sequences can encode bureaucracy rather than good practice.
- Prediction favors regularity and can suppress rare safety checks unless consequence is represented separately from probability.

## Grounding questions

1. Which HTM mechanisms are current and which belong to older formulations?
2. How are multiple predictions, bursting, and anomaly scores formally defined?
3. What evidence supports hierarchical composition beyond local sequence learning?
4. Which results compare HTM with simpler sequence and anomaly models?
