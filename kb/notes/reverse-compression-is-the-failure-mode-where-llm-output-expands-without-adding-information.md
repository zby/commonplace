---
description: LLMs can inflate a compact seed into verbose prose that carries no more extractable structure — the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count
type: note
traits: []
tags: [kb-design, learning-theory]
status: seedling
---

# Reverse-compression (inflation) is the failure mode where LLM output expands without adding information

Compression removes redundancy to preserve information. Reverse-compression is the inverse: expanding a compact signal into a verbose one that is *larger* but no more informative. An LLM given one sentence can produce a full article that reads like depth — paragraphs, structure, examples — but carries no more extractable structure than the seed. The training knowledge creates the appearance of elaboration without actual information gain.

This is the common failure mode of vibe-noting. A human offers a one-sentence insight, the agent builds a whole article grounded in its vast training knowledge, and the result is a waste of time to read because you learn nothing beyond the seed.

## Why epiplexity is the right measure

The naive test — "does the body contain claims not in the title?" — is insufficient. An LLM can generate novel-looking claims by connecting the seed to common knowledge it already has. The reader, if they share that common knowledge (as most do), gains nothing from seeing it spelled out. But sometimes connecting to common knowledge *is* useful — when the connection is surprising, when the reader lacks that specific piece of common knowledge, or when the juxtaposition reveals something neither the seed nor the common knowledge contained alone.

[Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — epistemic complexity extractable by a bounded observer — is the right measure because it accounts for what the *reader* can extract, not just what the text contains. A reverse-compressed article has high token count but low epiplexity for its intended audience: the structure that's there was already accessible to them without the article. A genuinely informative note has high epiplexity because it makes structure accessible that wasn't before — through novel connections, specific evidence, or juxtapositions the reader wouldn't have made on their own.

## How a linked KB resists reverse-compression

A KB that links notes to each other should resist this failure mode because each link can add information the original sentence didn't contain. When a note cites a specific practitioner report, connects to a specific theoretical framework, or extends a specific prior argument, the link carries the reader to a node with its own epiplexity. The network, not the prose, is where epistemic complexity accumulates.

The test: does reading note B after note A tell you something you couldn't have derived from A alone? If the answer is consistently yes, the KB is accumulating knowledge. If notes are just elaborating their own titles without connecting to anything that adds information, the KB is reverse-compressing — growing in tokens without growing in extractable structure.

But this resistance is not automatic. A note can link to other notes and still be reverse-compressed if the links are decorative rather than load-bearing — if the linked notes don't actually add information to the argument being made. The links must be [articulated relationships](./link-contracts-framework.md) (extends, grounds, contradicts), not just "see also."

## Toward a validation gate

A reverse-compression check would need to be semantic, not structural. Possible heuristics worth testing manually:

- **Seed reconstruction test**: can you state the note's full contribution in one sentence? If yes, and that sentence is essentially the title, the note may be reverse-compressed.
- **Link load-bearing test**: remove all links from the note — does the argument collapse, or does it read identically? Load-bearing links resist reverse-compression; decorative links don't.
- **Audience epiplexity test**: for the intended reader (an agent or human with access to this KB and general LLM training knowledge), does the body make structure accessible that wasn't before?

These are judgment calls, not grep-able checks. Whether they can be mechanized into `/validate` is an open question.

---

Relevant Notes:

- [vibe-noting](./vibe-noting.md) — context: the inflation failure mode this note names and analyzes
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — grounds: epiplexity formalizes what "adds information for a bounded observer" means
- [distillation](./distillation.md) — contrasts: distillation compresses while preserving essential structure; reverse-compression expands while adding none
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — source: the formal measure of extractable structure for bounded observers
- [link contracts framework](./link-contracts-framework.md) — enables: articulated link relationships are what make links load-bearing rather than decorative
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — contrasts: distillation is the productive inverse — compressing while preserving; reverse-compression is the failure mode — expanding while adding nothing
