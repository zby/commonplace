<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: semantic/completeness-boundary-cases
model: opus-4.6
gate-hash: 053b48e685ea43922bddff685682f7d56447b657
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:07:09+01:00
-->
## Completeness and boundary cases review

### Framework under test

The note claims the soft bound has "at least two dimensions: volume and complexity," with irrelevant context as a possible independent third dimension. This is the central enumeration to boundary-test.

### Boundary cases tested

**1. Simplest instance: minimal context with a clear task.** A short, direct prompt with no irrelevant material and no compositional depth. The framework predicts no degradation (both dimensions near zero). This maps cleanly — the note does not claim degradation at minimal context. Pass.

**2. Most extreme instance: hard-limit-adjacent, maximally complex, full of distractors.** All dimensions at maximum. The framework predicts severe degradation across all axes. This maps cleanly. Pass.

**3. Volume without complexity (same-difficulty task, increasing token count).** Paulsen's MECW experiments (needle-in-haystack with simple data) occupy this case. The framework covers it under "Volume." Pass.

**4. Complexity without volume (short but deeply compositional).** ConvexBench at depth 100 / 5,331 tokens. The framework covers it under "Complexity." Pass.

**5. Between the enumerated items: position effects at fixed volume and complexity.** The "lost in the middle" finding shows that rearranging the same tokens (same volume, same task complexity) changes performance. The note mentions this under Volume ("primacy and recency bias"), and later lists "information arrangement" as a factor in the "invisible" section. But position is neither volume nor complexity — it is a spatial property of the same content. The note does not name position as a dimension, though it references the phenomenon. The "at least two dimensions" qualifier leaves room, but position effects are well-enough documented to warrant mention as a candidate dimension alongside the discussion of irrelevant context.

**6. Adjacent concept: output degradation vs comprehension degradation.** The note focuses on comprehension failure (missed instructions, shallow reasoning, ignored context). But soft degradation could also manifest as output-quality degradation: the model comprehends the context but generates lower-quality output due to competing attention demands. The note does not distinguish these modes. The GSM-DC dual-channel finding (path selection vs arithmetic execution degradation) partially addresses this, but the note doesn't draw the connection explicitly. This is a boundary between the note's scope and an adjacent phenomenon.

**7. Model capability as a potential dimension.** Different models have different degradation surfaces for the same prompt. The note says the bound "shifts with ... model updates" but does not list model capability as a dimension. This is a scoping choice: the note treats the soft bound as a property of a given model, then describes its dimensions within that model. Reasonable but worth flagging — the "at least two dimensions" claim is per-model, not absolute.

### Findings

**INFO — Position effects straddle the framework boundary.** The note cites lost-in-the-middle under Volume but does not address whether position constitutes an independent dimension. Rearranging tokens at fixed volume and complexity changes performance, which means position is not reducible to volume. The note's "at least two dimensions" qualifier provides coverage, but the omission is noticeable given that position effects are among the most reproduced findings in the area. Consider mentioning position as a candidate dimension alongside irrelevant context in the Open Questions section.

**INFO — Output-quality vs comprehension-quality degradation not distinguished.** The note describes degradation as "missed instructions, shallow reasoning, ignored context" (comprehension failures). GSM-DC's dual-channel finding suggests degradation also hits execution quality on correctly comprehended content. The note could acknowledge this as a sub-structure within the degradation phenomenon, not just between dimensions of the input.
