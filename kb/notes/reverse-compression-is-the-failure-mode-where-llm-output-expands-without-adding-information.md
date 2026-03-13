---
description: LLMs can inflate a compact seed into verbose prose that carries no more extractable structure — the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count
type: note
traits: []
tags: [kb-design, learning-theory]
status: seedling
---

# Reverse-compression (inflation) is the failure mode where LLM output expands without adding information

[Compression](./distillation.md) removes redundancy to preserve information. Reverse-compression is the inverse: expanding a compact signal into a verbose one that is *larger* but no more informative. This is the common failure mode of [vibe-noting](./vibe-noting.md) — a human offers a one-sentence insight, the agent builds a whole article grounded in its training knowledge, and the result carries no more extractable structure than the seed. It reads like depth, but you learn nothing beyond what the seed already said.

## Why epiplexity is the right measure

Three candidate tests, each more precise than the last:

1. **Does the body contain claims not in the title?** Insufficient — an LLM can generate novel-looking claims by connecting the seed to common knowledge it already has.
2. **Does the body contain information not derivable from the title combined with the LLM's training knowledge?** Well-defined but wrong — it measures information gain over the LLM, not over the reader.
3. **Does the body make structure accessible to the *reader* that wasn't before?** This is the right question, because usefulness is relative to the reader, not to the model.

[Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — [epistemic complexity extractable by a bounded observer](./information-value-is-observer-relative-because-extraction-requires-computation.md) — formalizes test 3. A reverse-compressed article has high token count but low epiplexity for its intended audience: the structure was already accessible to them without the article. Connecting to common knowledge *can* be useful — when the connection is surprising to the reader, when the reader lacks that specific piece, or when the juxtaposition reveals something neither the seed nor the common knowledge contained alone. But when the connections are obvious to the audience, the elaboration adds tokens without adding epiplexity.

## How a linked KB resists reverse-compression

In a linked KB, each link can carry the reader to a node with its own epiplexity — a specific practitioner report, a formal framework, a prior argument with its own evidence. The network, not the prose, is where epistemic complexity accumulates.

The test: does reading note B after note A tell you something you couldn't have derived from A alone? If consistently yes, the KB is accumulating knowledge. If notes are elaborating their own titles without connecting to anything that adds information, the KB is growing in tokens without growing in extractable structure.

This resistance is not automatic. Links must be [load-bearing](./link-contracts-framework.md) — the linked notes must actually add information to the argument. A note full of "see also" links to tangentially related material is still reverse-compressed; the links are decorative, not structural.

## Toward a validation gate

A reverse-compression check is semantic, not structural — it can't be grepped. Two heuristics worth testing manually:

- **Link load-bearing test**: remove all links from the note — does the argument collapse, or does it read identically? If identical, the links are decorative and the note is likely reverse-compressed.
- **Audience epiplexity test**: for the intended reader (an agent or human with access to this KB and general LLM training knowledge), does the body make structure accessible that wasn't before?

Whether these can be mechanized into `/validate` is an open question.

---

Relevant Notes:

- [vibe-noting](./vibe-noting.md) — context: the inflation failure mode this note names and analyzes
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — grounds: epiplexity formalizes what "adds information for a bounded observer" means
- [distillation](./distillation.md) — contrasts: distillation compresses while preserving essential structure; reverse-compression expands while adding none
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — source: the formal measure of extractable structure for bounded observers
- [link contracts framework](./link-contracts-framework.md) — enables: articulated link relationships are what make links load-bearing rather than decorative
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — contrasts: distillation is the productive inverse — compressing while preserving; reverse-compression is the failure mode — expanding while adding nothing
