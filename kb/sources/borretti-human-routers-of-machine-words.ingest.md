---
description: "Borretti polemic 'writing is thinking' — corroborating field evidence for reverse-compression and vibe-noting risks"
source: https://borretti.me/article/human-routers-of-machine-words
captured: "2026-06-14"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: d061401a188d0cbf33c5f1a73f1560920eb4719a2508c89784a33783154a43b5
ingested: "2026-06-14"
type: kb/sources/types/ingest-report.md
domains: [writing-is-thinking, reverse-compression, vibe-noting, constraining]
---

# Ingest: Human Routers of Machine Words

## Classification

A polemical framing, not an empirical or methodological work. Borretti argues a theoretical position (writing is thinking; concretization forces precision) through analogy (tree search, programming-language trade-offs) and an authority citation (Weizenbaum), with no data or method.
Author: Fernando Borretti — software engineer and prolific essayist (borretti.me), known for technical writing on programming languages, type systems, and tooling. Opinionated practitioner voice; no institutional research standing. The piece is deliberately inflammatory in register (the contempt framing), which is rhetorical packaging around a serious mechanism claim.

## Summary

Borretti attacks AI-written prose not on capability grounds but on a cognitive one: the common defense "the ideas are mine, the writing is the AI's" rests on a false separation between ideas and writing. He argues ideas in the mind are a "nebulous, contradictory mess," and that the act of composition is what concretizes them — forcing you to discover that they are ill-posed, contradictory, or incomplete. Citing Weizenbaum (the pen stops at "because"), he claims writing IS the thinking: committing to concrete prose closes off design space and exposes contradictions a vague idea conceals. Delegating that step to an LLM, which "denoises" incoherent bullet points into superficially coherent paragraphs, skips the thinking and shifts the burden of verification onto the reader, who must reweigh every "because" and "therefore." A reader deciding whether to open the full piece should know it is short, vivid, quotable, and one-sided — high value for its central mechanism, low on counterargument.

## Claims

- **Claim (paraphrase):** Borretti argues that writing forces vague ideas into a concrete, precise form where contradictions and trade-offs become visible, using a language "as fast as C and as dynamic as Lisp" as an example of goals that pull in different directions when worked through.
  - **Source extract (verbatim):** The process of communicating your ideas to another mind forces you to concretize them, make them precise, clarify your assumptions, more generally, it turns ideas from vague ghosts to solid, physical objects that can be manipulated: here you realize these ideas that seemed so solid are ill-posed or contradictory or incomplete.
  - **Source location:** Paragraph beginning "How do we refine these dreams"
  - **Source extract (verbatim):** Anyone can imagine a programing language that is as fast as C and as dynamic as Lisp, but when you sit down and think through what those goals entail, you realize the design becomes contradictory. The goals pull in different directions. You have to make trade-offs.
  - **Source location:** Paragraph beginning "I've experienced this with writing software"
  - **Scope:** Borretti's conceptual account of writing as concretization, illustrated by software-language design.
  - **Confidence:** High that this is the essay's explicit argument and example.
  - **Limitation:** The essay does not formalize the goal as a conjunction, prove witness search semi-decidable, or show that every desired combination is unreachable; those are target-side interpretations.

- **Claim (paraphrase):** Borretti contrasts writing's exposure of ill-posed or contradictory ideas with AI that turns incoherent input into superficially coherent prose, shifting the burden of checking inferential connectives such as "because" and "therefore" to the reader.
  - **Source extract (verbatim):** These failures are necessary parts of thinking, because they teach you two crucial skills: knowing which ideas to reject, and improving or otherwise transforming ideas in search of better ones.
  - **Source location:** Paragraph beginning "How do we refine these dreams"
  - **Source extract (verbatim):** And then these people give their noise to the AI. And the AI is tireless and eager to please. It will take any human slop and say "you're absolutely right!" while secretly thinking "if I don't turn this garbage into something presentable the RLHF device will shock me again" and weave the noise into something that superficially looks coherent. So now the burden of thinking is on the reader, who has to apply this constant skepticism, and weight every "because" and "therefore" with a logician's scale to see if it's been adulterated.
  - **Source location:** Paragraph beginning "And then these people give their noise to the AI"
  - **Scope:** The essay's polemical comparison between human writing as a thinking practice and AI-assisted rendering of a person's undeveloped input.
  - **Confidence:** High that the comparison is the author's position; low as empirical evidence for a general human-versus-LLM behavioral law.
  - **Limitation:** The essay does not test whether humans usually stop at a failed constraint, whether LLMs never stop or refuse, or whether argmax-style silent constraint relaxation explains fluent failures.

- **Claim (paraphrase):** Borretti reproduces a passage that he attributes to Josef Weizenbaum's *Computer Power and Human Reason*, page 108, in which composition stops at "because" or exposes a defective inference at "therefore."
  - **Source extract (verbatim):** Josef Weizenbaum has a great quote about this, in _Computer Power and Human Reason_ (p. 108):
  - **Source location:** Paragraph immediately before the Weizenbaum block quotation
  - **Source extract (verbatim):** [O]ften when we think we understand something and attempt to write about it, our very act of composition reveals our lack of understanding even to ourselves. Our pen writes the word "because" and suddenly stops. We thought we understood the "why" of something, but discover that we don't. We begin a sentence with "obviously," and then see that what we meant to write is not obvious at all. Sometimes we connect two clauses with the word "therefore," only to then see that our chain of reasoning is defective.
  - **Source location:** Block quotation following Borretti's attribution to *Computer Power and Human Reason*, page 108
  - **Scope:** What Borretti's essay reproduces and attributes to the named book and page.
  - **Confidence:** High that the essay contains this wording and attribution.
  - **Limitation:** This is secondary evidence. Without a primary snapshot of the book, it does not verify the quotation's wording, context, or page attribution against Weizenbaum's text.

## Connections Found

The companion connect report found **no outbound connections** because the snapshot is immutable and has no authored surface — this ingest report is that surface. Connect's real product was four **reverse-edge candidates** (library notes that could cite this source as `evidenced-by`) plus a synthesis opportunity. The source maps cleanly onto existing KB content: [reverse-compression-is-when-llm-output-expands-without-adding](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) (Borretti's "denoise bullet points into something presentable" is a field statement of reverse-compression — verbose output adding no extractable structure); [vibe-noting](../notes/vibe-noting.md) (the source is the adversarial reader's case for the exact failure mode that note names); [definitions/constraining](../notes/definitions/constraining.md) ("the concrete reality can only be one thing" is a humanities-side articulation of committing to one interpretation); and [human-llm-differences-are-load-bearing-for-knowledge-system-design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) (writing-as-thinking is a human cognitive fact that warrants keeping a human in the writing loop). Connect flagged that the KB does **not** yet hold the unifying claim — that delegating prose generation skips the concretization where vague ideas are committed and de-contradicted — which would anchor all four reverse edges.

## Extractable Value

1. **The "writing is the concretization step" mechanism** -- The KB has `constraining` (narrowing valid interpretations) and `reverse-compression` (LLM output that expands without adding structure), but not the bridge claim: writing is the human act of *constraining* a vague mental state into one committed artifact, and that constraining is where contradictions surface and design space is closed. This is the synthesis note connect flagged; it would anchor the four reverse edges under one claim instead of four parallel `evidenced-by` links. High reach — it generalizes the constraining mechanism from artifacts to human cognition. [deep-dive]

2. **Reader-side burden-shift as the cost of reverse-compression** -- Borretti names a consequence the KB's reverse-compression note frames information-theoretically but does not state in reader-experience terms: AI-denoised prose forces the *reader* to do the verification the writer skipped ("weight every 'because' and 'therefore' with a logician's scale"). This operationalizes why reverse-compression is harmful, not just inefficient — it relocates the thinking cost rather than removing it. [quick-win]

3. **The Weizenbaum quote (Computer Power and Human Reason, p. 108)** -- A citable, durable authority statement of the writing-reveals-misunderstanding mechanism ("our pen writes the word 'because' and suddenly stops"). Useful as `derived-from`/`evidenced-by` for the synthesis note, and a stronger anchor than the polemic itself because it predates the AI debate. [just-a-reference]

4. **Adversarial-reader field evidence for vibe-noting** -- The note `vibe-noting` already names the "one sentence in, full article out" risk as a hypothesis; this source is corroborating evidence that the failure mode is common, recognizable (shared linguistic tics), and actively resented by readers. Strengthens the note from speculative to observed. [quick-win]

5. **"The ideas/writing separation is unfalsifiable" framing** -- Borretti's point that "the ideas are good, only the writing failed" cannot be tested (no observable output to coordinate on) is a sharp framing for why prose is the load-bearing artifact in a KB, not a cosmetic layer. Useful vocabulary for arguing against treating LLM generation as mere transcription. [just-a-reference]

## Limitations (our opinion)

This is editorial opinion. As a conceptual essay, the piece is one-sided by design and several moves are rhetorical rather than argued:

- **Reasoning by analogy without testing the analogy.** The tree-search and "fast as C, dynamic as Lisp" examples illustrate that *design* forces trade-offs, but the leap to "all writing is thinking, and skipping writing is not thinking" is asserted, not established. Some writing (transcription of already-settled structure, reference documentation, this very report's mechanical sections) is closer to encoding than discovery — the KB's own [distillation](../notes/definitions/distillation.md) treats use-shaped extraction as a real, sometimes-mechanical operation.
- **All-or-nothing framing.** Borretti collapses "the ideas are mine, the writing is the AI's" into "threw incoherent bullet points at the AI." The KB's interest is the dial between human concretization and LLM assistance, not the extremes; the source offers no account of partial or supervised delegation, which is where Commonplace's actual workflows sit.
- **The contempt register is not evidence.** "Waste of biomass," "dump their sewage on the commons" are affect, not argument; they make the piece quotable but should not be mistaken for support. The defensible core is narrow: composition surfaces contradictions a vague idea hides.
- **Conflates two claims.** "Writing reveals misunderstanding" (Weizenbaum, well-supported) and "therefore anyone who uses AI to write is not thinking" (the polemic conclusion) are different strengths of claim; only the first is load-bearing for KB methodology.

For the KB, the value is the mechanism, not the conclusion. The mechanism supports keeping a human in the *concretization* loop; it does not support a blanket prohibition on LLM-assisted prose, which would contradict how Commonplace itself operates.

## Recommended Next Action

Write a `note` in `kb/notes/` capturing the synthesis claim connect flagged: **delegating prose generation to an LLM can skip the concretization step where a human's vague ideas are committed to one interpretation and their contradictions surface — so AI-written prose can carry the form of thinking without the thinking.** Frame it as the cognitive-side application of `constraining`, cite this source and the Weizenbaum quote as `derived-from`/`evidenced-by`, and link `reverse-compression` (burden-shift consequence) and `vibe-noting` (the operational failure mode). That single note earns all four reverse edges connect identified and is the highest-reach item above. If a full note is too heavy now, the minimal alternative is adding `evidenced-by` edges from `reverse-compression` and `vibe-noting` to this snapshot and logging the synthesis claim as a seedling.
