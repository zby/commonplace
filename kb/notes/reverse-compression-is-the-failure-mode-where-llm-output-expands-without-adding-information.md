---
description: LLMs can inflate a compact seed into verbose prose that carries no more extractable structure — the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count
type: note
traits: []
tags: [learning-theory]
status: seedling
---

# Reverse-compression (inflation) is the failure mode where LLM output expands without adding information

Compression removes redundancy to preserve information. Reverse-compression is the inverse: expanding a compact signal into verbose prose without adding extractable structure. This is the common failure mode of [vibe-noting](./vibe-noting.md) — a human offers a one-sentence insight, the agent builds a whole article grounded in its training knowledge, and the result reads like depth but teaches the reader nothing beyond the seed.

## Why epiplexity is the right measure

What counts as "adding information" depends on who you measure against. Three candidate tests, each more precise than the last:

1. **Does the body contain claims not in the title?** Insufficient — an LLM can generate novel-looking claims by connecting the seed to common knowledge.
2. **Does the body contain information not derivable from the title combined with the LLM's training knowledge?** Well-defined but wrong — it measures novelty relative to the model, not usefulness to the reader.
3. **Does the body make structure accessible to the *reader* that wasn't before?** The right question — usefulness is relative to the audience, not the source.

[Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — [epistemic complexity extractable by a bounded observer](./information-value-is-observer-relative.md) — formalizes test 3. Connecting to common knowledge *can* raise epiplexity — when the connection is surprising to the reader, when the reader lacks that specific piece, or when the juxtaposition makes a pattern visible that the reader wouldn't have extracted on their own. But when the connections are obvious to the audience, the elaboration adds tokens without adding epiplexity. A reverse-compressed article is one where the structure was already accessible to its readers without the article.

## How a linked KB resists reverse-compression

In a linked KB, each link can carry the reader to a node with its own epiplexity — a practitioner report with quantified results, a formal framework, a prior argument with independent evidence. The network is where epistemic complexity accumulates, not the prose of any single note.

But this resistance requires that links are [load-bearing](./link-contracts-framework.md) — the linked notes must actually contribute to the argument. A note full of "see also" links to tangentially related material is still reverse-compressed; the links are decorative, not structural. The test: remove the links — does the argument collapse, or does it read identically?

## Toward a validation gate

A reverse-compression check is semantic, not structural — it can't be grepped. One heuristic worth testing manually before mechanizing into `/validate`:

For the intended reader (an agent or human with access to this KB and general training knowledge), does the note's body — including the nodes its links reach — make structure accessible that wasn't before? If the answer is no, the note is reverse-compressed regardless of its length or link count.

---

Relevant Notes:

- [vibe-noting](./vibe-noting.md) — context: the inflation failure mode this note names and analyzes
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: epiplexity formalizes what "adds information for a bounded observer" means
- [distillation](./distillation.md) — contrasts: distillation compresses while preserving essential structure; reverse-compression expands while adding none
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — source: the formal measure of extractable structure for bounded observers
- [link contracts framework](./link-contracts-framework.md) — enables: articulated link relationships are what make links load-bearing rather than decorative
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — contrasts: distillation is the productive inverse — compressing while preserving; reverse-compression is the failure mode — expanding while adding nothing
