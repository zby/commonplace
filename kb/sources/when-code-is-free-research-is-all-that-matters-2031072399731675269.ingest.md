---
description: Investor/researcher argument that oracle availability (not capability) determines automation boundary for cognitive work — research taste is unautomatable because problem selection has no ground truth
source_snapshot: when-code-is-free-research-is-all-that-matters-2031072399731675269.md
ingested: 2026-03-10
type: conceptual-essay
domains: [automation-boundary, research-methodology, oracle-theory, labor-economics]
---

# Ingest: When code is free, research is all that matters

Source: when-code-is-free-research-is-all-that-matters-2031072399731675269.md
Captured: 2026-03-10
From: https://x.com/amytam01/status/2031072399731675269

## Classification

Type: **conceptual-essay** — argues a thesis (research taste as the scarce skill in an AI-automated world) through framing and analogy rather than data. No experimental methodology, no system being described; the coin-flipping metaphor and market-pricing examples serve a rhetorical function.

Domains: automation-boundary, research-methodology, oracle-theory, labor-economics

Author: Amy Tam (investor at Bloomberg Beta), co-written with E Chi and Trenton Chang (researchers/founders at Quadrillion). Tam's perspective is that of a venture investor reasoning about where value accrues as engineering labor becomes commoditized. Bloomberg Beta's future-of-work focus gives her a legitimate vantage point on labor market dynamics; Quadrillion's focus on research tools gives the co-authors a practitioner stake in the thesis.

## Summary

Tam argues that as AI coding tools commoditize software engineering, the scarce differentiator shifts from implementation (finding solutions to known-solvable problems) to research (deciding which problems are worth solving when solutions might not exist). The core mechanism: engineering has built-in verification — tests, specs, benchmarks — that enables RL-driven automation, while research lacks ground truth. "Research taste" — the ability to select which of a vast number of possible problems deserve investment — is portable across domains (physicists become quants become AI researchers), hard to train, and hard to automate because neither success data nor failure data is publicly available. Current AI tools like Karpathy's autoresearch automate execution (hyperparameter sweeps) but not problem selection. Tam expects the gap to close, but argues the bottleneck is currently the researcher deciding what to try and what to skip.

## Connections Found

The `/connect` discovery found 7 connections, all clustering tightly around the KB's oracle theory and learning theory neighborhoods:

- **[oracle-strength-spectrum](../notes/oracle-strength-spectrum.md)** — exemplifies: Tam's engineering-vs-research distinction IS the oracle-strength spectrum. Engineering sits at the hard-oracle end (tests, specs, exact verification); research sits at the no-oracle or delayed-oracle end (you don't know if a solution exists). Tam's claim that AI automates engineering first is the oracle-strength prediction stated in market-economics language.

- **[the-augmentation-automation-boundary-is-discrimination-not-accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md)** — grounds: Tam's argument about why research resists automation (no ground truth to optimize against) is the augmentation-automation boundary restated. The KB note's two routes — external hard oracles (route b, which works) vs self-assessment (route a, which stagnates) — explain precisely why engineering automates first and research doesn't.

- **[bitter-lesson-boundary](../notes/bitter-lesson-boundary.md)** — exemplifies: autoresearch doing hyperparameter sweeps (arithmetic regime) but not problem selection (vision-feature regime) is a concrete instance of the boundary running through a single system, exactly like the chess example in the KB note.

- **[automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md)** — extends: both describe the same structural bottleneck at different scales. KB learning stalls on judgment-heavy mutations; research stalls on problem selection. Both are oracle-absent.

- **[first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md)** — grounds: "research taste" in Deutsch's vocabulary is selecting for explanatory reach. The hyperparameter-sweeping agent does adaptive work; the researcher's cross-domain portability is a direct statement of the reach property.

- **[discovery-is-seeing-the-particular-as-an-instance-of-the-general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)** — grounds: the coin-flipping expert recognizes which problems are tractable by seeing particular research questions as instances of general tractability patterns. Naming amortizes discovery cost, explaining taste's portability.

- **[memory-management-policy-is-learnable-but-oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)** — extends: AgeMem succeeds where research taste fails, precisely because task completion is a clear oracle and research outcomes aren't.

The connections are dense and coherent. This source lands squarely in the KB's existing oracle-theory cluster and restates several of its claims using different vocabulary (market economics, labor value) and different examples (quant hiring, Meta compensation packages, Karpathy's autoresearch).

## Extractable Value

1. **The autoresearch example as a concrete bitter-lesson-boundary instance.** Karpathy's system ran 126 experiments overnight but only explored hyperparameter sweeps — a vivid case of the boundary running through a single tool. Could be added to bitter-lesson-boundary.md alongside chess and vehicle routing. [quick-win]

2. **Market pricing as oracle-strength evidence.** Quant firms paying \$600k to undergrads and Meta offering \$300M packages to researchers is an external signal that the market has priced in the oracle-strength prediction: verification-absent skills command extreme premiums. Not proof, but a novel evidential angle the KB hasn't used. [just-a-reference]

3. **"What to not try" as a missing dimension of KB automation.** The automating-kb-learning note focuses on what to try (propose mutations). Tam emphasizes that knowing what to skip is equally valuable and even harder. This reframes the KB's automation challenge: the open problem isn't just "generate good candidates" but "prune the space before generation." [experiment]

4. **Taste rigidity as a failure mode.** "The researcher who was right about everything from 2018 to 2024 may be pattern-matching by 2026." This is a softening signal for human oracles — the same dynamic the KB describes for crystallised components. Could inform the softening-signals note or a new note on human-oracle degradation. [experiment]

5. **The halting problem analogy for research.** Tam frames research as a version of the halting problem: you can't know in advance whether a solution exists. This is a sharper framing than "no ground truth" — it says the oracle is not just absent but computationally impossible to construct for the general case. Worth examining whether this is technically accurate or merely suggestive. [deep-dive]

6. **Synthesis opportunity: "The boundary of automation is the boundary of verification."** The connect report flags this: oracle-strength-spectrum, augmentation-automation-boundary, automating-KB-learning, and this source all converge on the same claim from different angles. A synthesis note could unify them. [experiment]

## Limitations (our opinion)

**Unfalsifiable framing.** Tam's central claim — research taste is hard to automate — is unfalsifiable as stated. She acknowledges the gap "will close, probably faster than most people expect" but provides no criterion for evaluating when it has closed or what evidence would challenge the claim. If autoresearch improves to select problems well, was it always going to? If it doesn't, was she right? The halting problem analogy, while vivid, is misleading: real research operates in constrained domains where meta-learning about problem tractability is plausible, unlike the general halting problem which is provably undecidable. The analogy conflates practical difficulty with impossibility.

**Survivorship bias in the market-pricing argument.** Quant firms paying \$600k to undergrads does not demonstrate that "research taste" is the skill being purchased. It may reflect tournament dynamics (overpaying many to find the one who succeeds), domain-specific mathematical ability, or simple market competition for a small talent pool. The compensation data is consistent with many theories, not only the taste theory.

**Cherry-picked automation examples.** The autoresearch example (hyperparameter sweeps only) may already be outdated. Tam chose the weakest version of AI-assisted research to argue her point. More sophisticated systems (AlphaFold's approach to protein structure, AI-driven mathematical conjecture generation) do perform problem selection in narrow domains, and Tam doesn't engage with these counterexamples.

**Conflating naming with explaining.** "Research taste" names a phenomenon (some researchers are better at picking problems) without explaining the mechanism. The coin-flipping metaphor is vivid but vacuous — saying the expert "weaves through with a preternatural air" and recognizes "faint differences in the weight of the metal" doesn't explain how taste works, what its components are, or how to develop it. The KB's own vocabulary (explanatory reach, oracle strength, discovery-as-recognition) provides more analytical traction than "taste."

**Investor incentive.** The authors include the founder and a researcher at Quadrillion, which appears to be a research-tools company. The essay's thesis — research taste is the scarce skill — is also a pitch for tools that enhance research taste. This doesn't invalidate the argument but should be noted when evaluating the source's independence.

## Recommended Next Action

Write a note titled "The boundary of automation is the boundary of verification" connecting to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md), [the-augmentation-automation-boundary](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md), and [bitter-lesson-boundary](../notes/bitter-lesson-boundary.md). It would argue that across engineering, research, and knowledge curation, tasks become automatable precisely when verification becomes cheap — the hard problem is always oracle construction, never generation capability. This source, the oracle-strength note, and the augmentation-automation note each state a version of this claim from different domains; the synthesis note would unify them under a single thesis and test whether it holds as a general principle.
