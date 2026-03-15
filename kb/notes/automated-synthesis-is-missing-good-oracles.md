---
description: Generating synthesis candidates (cross-note connections, novel combinations) is easy — LLMs do it readily. The hard part is evaluating whether a candidate is genuine insight or noise.
type: note
traits: []
tags: [learning-theory]
status: speculative
---

# Automated synthesis is missing good oracles

LLMs can combine existing notes and produce plausible-sounding connections with minimal prompting. Experiments with this KB confirm that automated synthesis readily surfaces interesting candidates — combinations that a human reviewer recognizes as genuinely insightful. The problem is not generating synthesis; it's knowing which candidates are good.

## Extraction vs synthesis: the oracle gap

**Automated extraction** works because verification is easier. At the explicit end, it's mechanical — does the structured output match what the source says? At the implicit end (claims a source implies without stating), it requires LLM judgment — but that judgment is still simpler than synthesis evaluation, because you have one source to check against.

**Automated synthesis** of natural-language knowledge fails at scale because most of what it produces is not useful — obvious connections, plausible truisms, and occasional nonsense alongside the genuine insights. Discriminating the valuable from the noise requires judgment that is not substantially cheaper than producing the synthesis in the first place — and that's the oracle gap. (Note the scope: in formal domains like mathematics or code composition, synthesis verification *can* be cheap — proof checkers and test suites serve as hard oracles. The problem is specific to natural-language knowledge where value is a judgment call, not a formal check.)

This is an instance of [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md): synthesis generation capability outpaces synthesis verification capability, so the system cannot run unsupervised.

## Current attempts

The [comparative review](./related-systems/agentic-memory-systems-comparative-review.md) found that across eleven systems, everyone automates extraction but almost nobody automates synthesis. The few attempts:

- **Tip consolidation** ([trajectory-informed-memory paper](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md)) — clusters semantically similar tips and LLM-merges them. Works because task completion provides an oracle: consolidated tips either improve performance or don't. The oracle is narrow but real.
- **A-MEM memory evolution** — neighboring notes update their context when new notes arrive. This is enrichment (adding context to existing items), not synthesis (producing something new from combination). No oracle needed because the operation is conservative.
- **Cognee memify** — promises synthesis-like operations but ships simpler extraction. The gap between ambition and shipping is itself evidence of the difficulty.
- **This KB's `/connect` skill** — surfaces synthesis opportunities by finding cross-note patterns. Human-triggered and human-evaluated. The human is the oracle.

The pattern: synthesis works when there's an oracle (tip consolidation has task completion; `/connect` has a human reviewer). It stalls when there isn't one.

## Why the oracle is hard to build

For extraction of explicit claims, quality is fidelity — did you faithfully represent what's in the source? For synthesis, quality is novelty plus validity — did you produce something new that's also true? These are different evaluation problems, though the boundary is a gradient (extracting implicit claims sits in between):

- **Fidelity** can be checked by comparison (does the output match the input?). Automatable.
- **Novelty** requires knowing what already exists (is this actually new, or a restatement?). Partially automatable through similarity search.
- **Validity** requires domain judgment (is this connection real, or a surface-level pattern match?). This is the hard part.

The [quality signals brainstorm](./quality-signals-for-kb-evaluation.md) proposes manufacturing a composite oracle from many weak signals. Whether that composite has enough discriminative power for synthesis evaluation — as opposed to the simpler problem of note quality scoring — is untested.

## Relationship to the boiling cauldron

The [automating KB learning](./automating-kb-learning-is-an-open-problem.md) note lists "Synthesise" as one of seven boiling cauldron mutations. This note narrows the problem: generation is not the bottleneck. The unsolved piece is building an oracle that can evaluate synthesis candidates cheaply enough to run at scale without human review of every proposal. Until then, synthesis remains human-triggered — which is fine for a small KB but limits scale.

## Open questions

- Could a tiered oracle work? Fast heuristic filters (graph distance, embedding similarity, contradiction detection) discard obvious noise, human reviews only the survivors. What false-negative rate is acceptable?
- The tip consolidation oracle (task completion) works because it has a closed evaluation loop. Could scenario-based evaluation provide a similar loop for KB synthesis? Run the synthesis, then test whether a scenario agent performs better with the synthesized note loaded.
- Is there a "synthesis complexity spectrum" analogous to the oracle strength spectrum? Simple combinations (two notes that cite the same source but don't reference each other) vs deep combinations (two notes from different traditions that share unnamed structure).

---

Relevant Notes:

- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: synthesis is an instance of the general principle; generation outpaces verification, so automation stalls
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — narrows: that note lists seven mutations; this note develops why one of them (synthesis) has a specific bottleneck distinct from the others
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — parallels: same oracle-dependency pattern in a different domain (memory management vs synthesis), same conclusion that the bottleneck is the oracle not the mechanism
- [agentic memory systems comparative review](./related-systems/agentic-memory-systems-comparative-review.md) — evidence: the "everyone extracts, almost nobody synthesizes" convergence finding across eleven systems
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — potential solution: composite oracle from weak signals, untested for synthesis evaluation specifically
- [oracle strength spectrum](./oracle-strength-spectrum.md) — extends: synthesis evaluation sits in the weak-oracle zone; the spectrum predicts that engineering effort should go to oracle construction, not generation improvement
- [synthesis is not error correction](./synthesis-is-not-error-correction.md) — shared structure: multi-agent output synthesis and knowledge synthesis both fail for the same reason — combining inputs without an oracle to evaluate the combination; error amplification (Kim et al.) is the within-task manifestation, spurious connections are the across-KB manifestation
