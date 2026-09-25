---
description: "A tertiary overview of recursive self-improvement that helps separate self-modification, retained improvement, and evidence of recursive compounding."
source: https://en.wikipedia.org/wiki/Recursive_self-improvement
captured: "2026-09-17"
capture: trafilatura
capture_scope: full-source
genre: reference-article
snapshot_sha256: cba9f11b617756846e5d4a86c4a7a52175b155ae86076011b334e36d85a37b79
ingested: "2026-09-17"
type: kb/sources/types/ingest-report.md
domains: [self-improving-systems, artificial-intelligence, learning-theory]
learning_claims: true
---

# Ingest: Recursive self-improvement

## Classification

This is a collaboratively edited tertiary reference article. It combines a conceptual definition, a hypothetical seed architecture, short summaries of reported systems, and a risk survey rather than presenting one original argument or experiment.
Author: Wikipedia contributors; the author signal is public editorial aggregation, without named subject-matter authorship or peer review for the synthesis itself.

## Summary

The article defines recursive self-improvement as an advanced AI changing its own code and capabilities through repeated cycles, then sketches a seed improver with programming, goal pursuit, tests, and retained changes. It groups Voyager, STOP, self-rewarding language models, and AlphaEvolve as experimental movement toward that idea, while acknowledging that none demonstrates an intelligence explosion or superintelligence. For KB decisions, it is useful as a map of common RSI terminology and examples, but its broad category should be split into self-modification, evaluation and retention, observed improvement, and evidence that earlier improvements make later improvement episodes more productive.

## Quotes

No source quotes have been retained yet.

## Connections Found

The article is best used as a tertiary orientation source and terminology counterpoint for the self-improving-systems cluster. Its code-rewrite framing is broader than the causal, frame-indexed definition of a [self-improving system](../notes/definitions/self-improving-system.md); its seed architecture becomes more precise when separated into search, reject-capable evaluation, and operative retention as in [a proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). The jump from repeated change to intelligence explosion remains unsupported without the later-episode productivity test in [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). Its AlphaEvolve summary gives a concrete illustration of why [warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): automated evaluation enables selection only where that evaluator is a valid judge. The code-grounded [Voyager](../agent-memory-systems/reviews/voyager.md) and [Exo](../agentic-systems/reviews/exo.md) reviews supply narrower mechanism-level cases than the article's umbrella category.

## Learning Claims (our opinion)

On the source's account, improvement comes from an agent proposing changes to code, algorithms, skills, model behavior, or architecture; evaluating those changes through game feedback, tests, reward signals, or performance metrics; and retaining candidates that score better. That account maps most directly to proposal selection and operative retention. It does not by itself establish a [theory builder](../notes/definitions/theory-builder.md). Keeping the candidates that score better is trial and error unless a stated reason bears on what a candidate says, and the article describes no such reason, so condition 3 is not shown and decides the verdict. Several examples fall outside on other grounds as well: self-rewarding models change weights, which fails condition 1. Retained work products such as Voyager's programs or AlphaEvolve's algorithms are localized and may guide later work (conditions 1, 2, and 4), but the article does not show criticism of their content. The reported gains are a separate learning claim and do not settle membership.

The reported systems also occupy different effective update spaces. Voyager can compose and retain generated Minecraft programs from game feedback; STOP searches scaffolding code around a fixed language model; self-rewarding models alter model behavior through generated feedback and training; AlphaEvolve mutates and combines algorithms under automated metrics. Their goals, tests or reward functions, proposal machinery, representational choices, and much of their substrate remain fixed outside those updates. Improvement within one such boundary shows that the compound setup can find better candidates there; it does not validate the fixed decomposition or show recursive compounding. Because the article offers only brief tertiary summaries, the exact histories, hypothesis classes, ablations, and causal contribution of each mechanism remain unresolved.

## Extractable Value

1. **Use the article as an RSI terminology map, with the local causal definition governing classification.** This preserves the source's broad public framing without letting code writability, tool production, or stored outputs count automatically as system improvement. [quick-win]
2. **Separate accumulation from recursive compounding.** The article's own statement that reported attempts have not shown an intelligence explosion supports withholding the stronger claim until an earlier retained improvement is shown to increase the productivity of a later improvement episode. [quick-win]
3. **Treat automated evaluation as a domain boundary.** AlphaEvolve's dependence on automated evaluation functions provides a concise example of why iterative search warrants unattended adoption only inside the evaluator's valid domain. [quick-win]
4. **Compare examples by effective update space rather than one RSI ladder.** Voyager, STOP, self-rewarding models, and AlphaEvolve expose different signals, operations, mappings, and fixed design choices; a primary-source comparison could reveal which apparent differences actually govern improvement. [deep-dive]
5. **Use the risk survey only as a route to stronger sources.** Its discussions of instrumental goals, misalignment, unpredictable evolution, and model collapse identify research questions, but the article's uneven mix of books, papers, popular reporting, and commentary is not enough to settle them. [just-a-reference]

## Limitations (our opinion)

The article is a tertiary synthesis with no stated selection method for examples or evidence. It combines hypothetical architecture, empirical systems, and speculative safety pathways without consistently distinguishing what was implemented, what improved, what caused the improvement, and what would count as recursive compounding. Several consequential claims rely on popular or advocacy sources rather than the primary studies, and the short experiment summaries omit baselines, ablations, evaluator validity, and fixed design choices. The full-page capture supports analysis of this Wikipedia article, but not independent verification of the works it cites or confidence that its current taxonomy reflects expert consensus.

## Recommended Next Action

Classify this ingest as a source-only orientation record for recursive self-improvement terminology pending primary evidence of later-episode compounding.
