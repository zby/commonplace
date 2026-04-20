---
description: Objective-vs-subjective intelligence essay arguing that AI's real bottleneck is taste and boringness judgment, not benchmarked competence
source_snapshot: adam-mastroianni-infinite-midwit.md
ingested: "2026-04-06"
type: kb/sources/types/ingest-report.md
source_type: conceptual-essay
domains: [automation-boundary, oracle-theory, research-methodology, writing-quality]
---

# Ingest: Infinite midwit

Source: adam-mastroianni-infinite-midwit.md
Captured: 2026-04-06
From: https://www.experimental-history.com/p/infinite-midwit

## Classification

Type: conceptual-essay — Mastroianni is arguing for a framing distinction, not presenting a system, dataset, or empirical study. The piece is built from analogy, examples, and lived-practice observations about writing and research.

Domains: automation-boundary, oracle-theory, research-methodology, writing-quality

Author: Adam Mastroianni is a psychologist and essayist at Experimental History. He is worth attending to here as a sharp observer of writing and research practice, but this is still an argumentative essay rather than an empirical demonstration.

## Summary

Mastroianni argues that recent AI progress has increased his confidence, not his fear, because the systems keep getting better at what he calls objective intelligence while still lacking subjective intelligence. Objective intelligence covers tasks with clear boundaries, reinforcement signals, and validation; subjective intelligence covers writing, idea selection, taste, judgment, and the ability to tell whether something is interesting rather than merely correct. His strongest examples come from writing and research: AI is useful as an infinite statistician, coder, and literature assistant, but it cannot tell whether a project is boring, whether a sentence is alive, or whether a direction is worth pursuing. The core thesis is that no amount of more-of-the-same benchmarkable competence guarantees the missing judgment layer.

## Connections Found

`/connect` found a tight fit to the KB's oracle/verification cluster rather than to general "AI writing" discussion.

- [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **grounds**: the source restates the same structural claim in objective-vs-subjective language
- [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) — **grounds**: objective intelligence maps to hard-oracle work; subjective intelligence maps to soft/no-oracle work
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **grounds**: the source gives a vivid prose-level case where local competence still lacks per-instance judgment
- [automated-synthesis-is-missing-good-oracles](../notes/automated-synthesis-is-missing-good-oracles.md) — **extends**: "boringness" is a concrete name for the otherwise abstract synthesis-evaluation bottleneck
- [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) — **extends**: the essay sharpens the value of knowing what not to do, not just how to execute more cheaply
- [when-code-is-free-research-is-all-that-matters-2031072399731675269.ingest](./when-code-is-free-research-is-all-that-matters-2031072399731675269.ingest.md) — **extends**: same claim from a different rhetorical angle, with labor economics and research taste instead of objective/subjective intelligence

The key fit is that the source does not primarily add a new automation-boundary claim; it adds a more intuitive, human-facing vocabulary for why the existing oracle-boundary notes feel true in writing and research practice.

## Extractable Value

1. **Objective vs subjective intelligence as a human-facing oracle vocabulary.** The source gives the KB's hard-oracle/no-oracle distinction a more intuitive rendering: "objective" names work with clear validation loops, while "subjective" names work where taste and judgment remain load-bearing. High reach: this vocabulary transfers beyond writing to many automation-boundary discussions. [quick-win]

2. **"Boringness" as a practical negative oracle.** The essay names the actual filter many experts apply in soft-oracle domains: not just "is this correct?" but "is this dead, boring, or unworthy of further investment?" That sharpens [automated-synthesis-is-missing-good-oracles](../notes/automated-synthesis-is-missing-good-oracles.md) by giving the missing oracle a recognizable operational form. High reach: applies to research, writing, strategy, and curation. [quick-win]

3. **Madame Stats and Mr. Encyclopedia as the stable AI-help decomposition.** The source cleanly decomposes where AI remains structurally useful even if the taste problem stays unsolved: infinite statistics help, coding help, and recall help. That is a reusable design pattern for research workflows and workshop tooling — optimize for execution support while keeping direction-setting human. High reach: transfers to any domain where execution bottlenecks and idea bottlenecks separate. [experiment]

4. **Bottleneck blindness as the anti-maximalist correction.** The essay's claim is not just "AI lacks taste" but "removing one bottleneck reveals the next one." That is a more general explanation for why capability gains need not collapse human work: once objective intelligence becomes cheap, direction, buy-in, motivation, and taste become the visible constraints. High reach: this generalizes well beyond this essay's AI examples. [experiment]

5. **Reputation as a social oracle and liability shield.** Human experts contribute not only judgment but accountability: if Madame Stats or Mr. Encyclopedia are wrong, their reputation is on the line, whereas AI carries no comparable liability. This is a useful extension of verification theory into social systems where trust and blame assignment matter. Medium reach: strongest in high-consequence or collaborative domains. [deep-dive]

6. **Taste may be trained through repeated exposure to an expert's boredom threshold.** The PhD anecdote suggests a mechanism for how taste develops: not through more execution, but through repeated contact with someone who can reject bad directions quickly. That is potentially useful for workshop design, mentor loops, and human-in-the-loop curation. Medium reach: plausible and valuable, but still anecdotal. [deep-dive]

## Limitations (our opinion)

The two-intelligences framing may be rhetorically stronger than it is analytically necessary. A simpler account is the KB's existing oracle theory: tasks with cheap verification scale, tasks without it do not. The essay gives us better phenomenology for that boundary, but it does not show we need a new ontology of intelligence rather than a verifier-centric task distinction.

The evidence is heavily anecdotal and cherry-picked. Writing quality, nerd social failure, Scott Adams, and the author's research practice all point in the same direction, but the piece does not examine counterexamples or mixed cases where soft-oracle tasks improve more than expected. That weakens any claim stronger than "this is a useful framing."

The essay names the missing thing more clearly than it explains it. "Subjective intelligence," "taste," and "how to be bored correctly" are vivid, but they do not decompose the mechanism much further. This is the same risk noted in the related Tam ingest: naming the scarce faculty is not yet explaining how it works or how to cultivate it reliably.

The permanence claim is under-argued. The essay insists that the central hole "shows no signs of shrinking," but as of March 31, 2026 that is still a judgment from lived practice, not a demonstrated trend analysis. The structural part of the argument is strongest when recast as an oracle claim, and weakest when recast as a confident forecast about the persistence of a particular capability gap.

## Recommended Next Action

Write a note titled `Research taste is no-oracle reach judgment` connecting to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md), [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — it would argue that what practitioners call "taste" is the ability to select high-reach directions where no cheap verifier exists.
