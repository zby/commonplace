---
description: "LLMs can inflate compact seeds into verbose artifacts without adding extractable structure; a KB resists this only when links make additional structure accessible"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, discovery]
---

# Reverse compression is when LLM output expands without adding information

Compression removes redundancy to preserve information. Reverse-compression is the inverse: expanding a compact signal into verbose prose without adding extractable structure. This is the common failure mode of [vibe-noting](./vibe-noting.md) — a human offers a one-sentence insight, the agent builds a whole article grounded in its training knowledge, and the result reads like depth but teaches the reader nothing beyond the seed.

## Epiplexity motivates one part of the measure

What counts as "adding information" depends on who you measure against. Three candidate tests, each more precise than the last:

1. **Does the body contain claims not in the title?** Insufficient — an LLM can generate novel-looking claims by connecting the seed to common knowledge.
2. **Does the body contain information not derivable from the title combined with the LLM's training knowledge?** Well-defined but wrong — it measures novelty relative to the model, not usefulness to the reader.
3. **Does the body make structure accessible to the *reader* that wasn't before?** The right question — usefulness is relative to the audience, not the source.

[Epiplexity](https://arxiv.org/html/2601.03220v1) formalizes one component of this test: structural information extractable from data by a computationally bounded model under a runtime constraint. It is task-agnostic and does not by itself formalize relevance, surprise, or usefulness relative to an individual reader. Test 3 is this note's operational extension: compare what structure an intended reader can access with and without the artifact, given that reader's prior knowledge and goals. A connection to common knowledge can pass that test when it makes a surprising or previously unavailable pattern accessible. When the connection is already obvious to the audience, the elaboration adds tokens without changing what that reader can extract. A reverse-compressed article is one where the relevant structure was already accessible to its intended readers without the article.

## How a linked KB resists reverse-compression

In a linked KB, each link can carry the reader to a node with independently extractable structure — a practitioner report with quantified results, a formal framework, or a prior argument with its own evidence. The network is where accessible epistemic complexity accumulates, not the prose of any single note.

But this resistance requires that links are [load-bearing](./linking-theory.md) — the linked notes must actually contribute to the argument. A note full of "see also" links to tangentially related material is still reverse-compressed; the links are decorative, not structural. The test: remove the links — does the argument collapse, or does it read identically?

## The same failure appears in code generation

SuperARC gives a mechanically classified instance outside KB writing. In its sequence-reproduction code tasks, the report says most programs classified as correct directly printed target sequences. The framework labels direct prints Type 3 and weights non-trivial solutions more heavily, so a correct output need not encode a generative rule. The report also says print-statement solutions dominated correct outputs across programming languages and that temperature variations produced nearly identical no-compression percentages. Those results make the finding robust to the reported language and temperature variations; because the capture omits the named languages, settings, counts, and uncertainty, they do not rule out sampling effects beyond those runs. Calling this reverse-compression is local analysis: the emitted code reproduces the requested output while adding no reusable generative rule for the capability the benchmark scores.

## Toward a validation gate

A reverse-compression check is semantic, not structural — it can't be grepped. One heuristic worth testing manually before mechanizing into `/validate`:

For the intended reader (an agent or human with access to this KB and general training knowledge), does the note's body — including the nodes its links reach — make structure accessible that wasn't before? If the answer is no, the note is reverse-compressed regardless of its length or link count.

---

Relevant Notes:

- [vibe-noting](./vibe-noting.md) — context: the inflation failure mode this note names and analyzes
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: separates compute-bounded structural extraction from this note's reader-relative relevance test
- [Epiplexity paper](https://arxiv.org/html/2601.03220v1) — source: the formal measure of extractable structure for bounded observers
- [SuperARC AIT benchmark](../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — evidenced-by: reports direct-print programs classified as correct and their dominance under the paper's language and temperature variations; classifying this as reverse-compression is local analysis
- [linking-theory](./linking-theory.md) — enables: the load-bearing vs decorative distinction is a core question for linking theory
- [skills derive from methodology](./skills-derive-from-methodology.md) — contrasts: skill derivation is the productive inverse — compressing while preserving; reverse-compression is the failure mode — expanding while adding nothing
