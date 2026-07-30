# CHREST: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

CHREST—Chunk Hierarchy and REtrieval STructures, if memory serves—models expertise as the gradual acquisition of domain-specific chunks and retrieval structures. Perceived patterns are sorted through a discrimination network. When existing nodes cannot adequately distinguish a new pattern, learning either adds a new node or enriches a known chunk. Richer templates can contain stable structure plus slots for variable information. Short-term capacities and the time required to perceive, learn, and retrieve constrain performance.

The transferable idea is that expertise is not a larger undifferentiated store. It is a learned organization that recognizes consequential patterns quickly and knows which detail can remain variable.

## Provisional ontology

- **Pattern:** structured input encountered in a domain.
- **Test/discrimination:** a feature that routes a pattern through memory.
- **Discrimination network:** the learned index used for recognition and retrieval.
- **Chunk:** a familiar structured unit reached through that index.
- **Image/content:** what the recognized node retains about the pattern.
- **Template:** a chunk with stable components and variable slots.
- **Short-term store:** a narrow active set constraining immediate manipulation.
- **Learning history:** the sequence of exposures that shaped the network.

This separates an artifact from the index that makes it recognizable. Adding a note does not automatically add the discriminations by which a future agent will find it.

## Transfer candidates

- **`CHREST-1` — learn indexes from confusions.** When search repeatedly returns the wrong sibling or an agent cannot distinguish two artifact types, add the smallest discriminating feature that separates them. Retrieval errors become evidence for index design.
- **`CHREST-2` — treat curated routing as acquired expertise.** Tag READMEs, descriptions, collection contracts, and decision trees can be understood as compressed recognition structures. Evaluate them by whether they route consequential cases quickly, not by taxonomic elegance.
- **`CHREST-3` — promote repeated structures into templates with slots.** A useful template preserves invariant relations while leaving situation-dependent fields open. This aligns with the rule that [an author should fix what the executor cannot determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md).
- **`CHREST-4` — preserve acquisition order in evaluation.** A routing system that works after seeing the whole corpus may not be learnable incrementally. Test whether useful distinctions can be added without reorganizing every prior artifact.
- **`CHREST-5` — measure recognition cost.** Retrieval quality includes how much content must be inspected before the correct structure is recognized, not only whether the final document appears in a result list.

## Method worth borrowing

CHREST's expertise orientation suggests comparing novice and expert representations of the same corpus. Give one agent only flat search and another a learned or curated discrimination structure; compare not just answer quality but search path, inspected material, and transfer to structurally similar cases. Eye-movement analogues need not be literal: file opens, link follows, backtracks, and query reformulations can expose recognition strategy.

## Non-transfer and failure modes

- A tree-like discrimination index may be too rigid for artifacts that need several independent access paths.
- Observed frequency can encode a narrow experience distribution rather than a durable distinction.
- Chunking can hide provenance and exception structure if compression is treated as lossless.
- Human short-term-memory limits and learning times should not be copied into LLM context policy.

## Grounding questions

1. How exactly do familiarisation and discrimination learning differ?
2. What is the formal relationship among chunks, images, templates, and slots?
3. Which task traces are treated as evidence that the learned network models expertise?
4. How path-dependent is the resulting representation, and how does CHREST handle restructuring?
