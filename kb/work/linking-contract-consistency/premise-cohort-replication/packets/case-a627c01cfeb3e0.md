# Case packet

Neutral case identifier: case-a627c01cfeb3e0

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Weakly discriminated qualities tend to be underselected

When a selection loop judges several qualities with oracles of unequal discriminative power, its accepted outputs improve on whatever the strong oracles distinguish and drift on whatever the weak ones barely distinguish — even when the generator is entirely capable of producing the weakly verified quality. Candidate availability and candidate selection are different bottlenecks.

This is a conjecture about proposal-selection loops, not a claim that every unmeasured quality deteriorates. It predicts a directional selection pressure when three conditions hold:

1. generated candidates vary on more than one quality;
2. acceptance or retention depends more reliably on some qualities than others; and
3. accepted outputs become the starting point, context, or training signal for later iterations.

What acts under those conditions is the **operative oracle** — the check that actually changes which candidates survive, which need not be the rubric a system says it values. A quality can be named prominently in the instructions and still exert almost no selection pressure, if nothing in the loop separates its better instances from its worse ones.

## Oracle asymmetry creates selection asymmetry

Suppose a coding loop selects patches for functional correctness and maintainability. Tests discriminate functional failures quickly: a candidate that breaks behavior is likely to be rejected. Maintainability review is delayed, noisy, or absent: two patches with very different future change costs may be equally likely to pass. Conditional on acceptance, the patch population is therefore enriched for correctness but only weakly enriched for maintainability.

No tradeoff has to be made anywhere for this to happen: nothing sacrifices maintainability in order to pass the tests. Local fixes, duplicated logic, and awkward dependencies survive simply because the acceptance mechanism sees their immediate behavior more clearly than their delayed cost. Each accepted patch then changes the codebase the next task inherits, and repetition converts a per-change blind spot into directional system drift.

The same asymmetry appears in an agent-operated KB: structural validation strongly discriminates broken frontmatter, invalid types, and unresolved links, and weakly discriminates whether a note has explanatory-reach, whether a connection reduces navigation uncertainty, or whether a synthesis captures the right mechanism. A high-throughput authoring loop can therefore converge on artifacts that validate cleanly while their semantic quality degrades, [especially when maintenance does not scale with generation].

## Knowledge and selection are different hypotheses

Poor retained output is usually blamed on missing model capability: the model does not know good design, cannot recognize a deep failure, cannot write a coherent theory. That explanation is sufficient but not necessary — three distinct cases predict the same visible failure:

- **Generation failure:** the desired quality is absent from the candidates the model can produce.
- **Activation failure:** the model can produce it, but the task frame does not elicit the relevant knowledge.
- **Selection failure:** good candidates appear, but the operative oracle does not favor them strongly enough to survive.

The distinction matters because the remedies differ: better weights or broader context for generation, explicit perspectives and probes for activation, stronger external checks for selection.

[The Bug That Shipped] shows two of these cases coming apart. Coding models rarely surfaced deployment failures under generic self-review, yet diagnosed the same failures when directly probed: the knowledge was available and the undirected review simply did not select for it. That does not establish the same mechanism for maintainability, but it does make “the model lacks the knowledge” an inadequate default explanation.

## Maintainability is the motivating case

[Why Software Factories Fail] argues that coding benchmarks strongly reward patches that pass tests while imposing little penalty for design choices whose cost appears through later changes. Its failed lights-off deployment is consistent with oracle asymmetry: immediate correctness remained visible while maintainability debt accumulated across accepted patches.

Part II responds by restoring humans at product, architecture, program-design, and code-review boundaries and by delivering [short vertical slices]. That limits how much work accumulates under a mistaken judgment, but it leaves the diagnosis open — missing knowledge and weak selection both predict the same failed deployment.

Intervention without new weights is the test that separates them. If explicit maintainability probes, pairwise design comparisons, repeated-change evaluations, or repository-specific structural checks reliably select better designs from the same generator, selection was a material bottleneck. If candidates stay poor even under a discriminating maintainability oracle, the better explanation is generation capacity, global codebase comprehension, or the quality definition itself.

## Stronger oracles can be assembled, but not by vote count alone

A weak oracle need not remain weak. Maintainability has multiple partial signals: dependency direction, duplication and complexity trends, change locality, mutation testing, failures on later modification tasks, independent design comparisons, and sampled human judgments. KB semantic quality likewise has partial signals from adversarial review, contradiction checks, use traces, graph structure, and human acceptance.

Combining them helps only when the individual checks have genuine discrimination and sufficiently different failure modes, [since error correction requires above-chance, decorrelated oracles]; repeating the same model, prompt, and evidence amplifies a shared blind spot rather than quality. A composite oracle therefore needs calibration against later effects — did the code become easier to change, did the note support better decisions, did the connection improve traversal? Proxy agreement without outcome calibration merely constructs a louder proxy.

This reframes human oversight as a source of labels and calibration rather than a permanent architectural constant. Where a composite oracle reaches sufficient discrimination, [warranted autonomy can expand into its domain]. Where it does not, removing the human changes actor allocation without warranting the accepted results.

## Predictions

- Strengthening an oracle for one quality should improve that quality among accepted outputs without requiring a weight change, provided the generator already produces usable variation.
- Generic self-review should underperform checks that name distinct failure perspectives when activation is part of the bottleneck.
- Sequential systems should show more drift than isolated tasks because accepted blind spots alter later starting states.
- Increasing generation throughput without proportionally strengthening weak quality checks should widen the gap between strongly and weakly verified qualities.
- Multiple correlated reviewers should plateau, while heterogeneous checks calibrated against delayed outcomes should continue to improve discrimination.

These predictions separate the conjecture from the trivial claim that “what gets measured gets managed.” The proposed mechanism is candidate selection under unequal discrimination, and it can fail in identifiable ways.

## Scope and rival explanations

- The claim requires a selection or retention pathway. In a one-shot call whose output is never compared, accepted, reused, or learned from, “underselection” is the wrong description.
- An oracle cannot select a quality absent from the candidate distribution. Strong verification does not manufacture generator capability.
- Some qualities genuinely conflict. A system may knowingly trade maintainability for latency or semantic nuance for consistency; that is objective weighting, not necessarily oracle weakness.
- Delayed quality can degrade because the model lacks global state, context, or causal understanding. Oracle asymmetry is one mechanism to test against those rivals, not a universal diagnosis.
- Human judgment is not automatically a strong oracle. It can be inconsistent, biased, expensive, or unable to observe delayed effects. Its value must also be established for the target domain.

---

Relevant Notes:

## Artifact B

# The boundary of automation is the boundary of verification

Tasks become automatable when verification is cheap and resist automation when verification is expensive — regardless of raw model capability. This is not an observation about current limitations. It's a structural claim: generation without verification produces output, not automation. Where automation stalls, the bottleneck is typically oracle construction, not generation.

Five sources arrive at this claim through different reasoning, from different domains, using different vocabulary. They are not fully independent — the oracle-theory notes already cite Tam et al. and Rabanser et al. — but the reasoning paths are distinct enough that the convergence is informative.

## The evidence

**Oracle theory (internal).** The [oracle-strength spectrum] proposes a gradient from hard oracles (exact, cheap, deterministic) to no oracle (vibes). The [augmentation-automation boundary] identifies the mechanism: crossing from augmentation to automation requires per-instance discrimination (knowing *this* output is wrong), not aggregate accuracy. [Rabanser et al.] find that calibration improves across model generations but discrimination trends are mixed — improving on some benchmarks, worsening on others — suggesting self-assessment is not reliably scaling, which favors external oracles. The [MAKER system] demonstrates the endpoint: zero errors over a million steps, achieved entirely through external hard oracles, with no reliance on model self-knowledge.

**Human factors (Bainbridge).** [Ironies of Automation] (1983) reached the same structure four decades earlier: an operator asked to monitor a system installed *because it outperforms the human* "has been given an impossible task" — real-time verification of the superior system's decisions is exactly what the human cannot supply. The residue automation leaves behind is the work past verification.

**Labor economics (Tam et al.).** [When code is free, research is all that matters] argues that AI commoditizes engineering (which has tests, specs, benchmarks — hard oracles in our vocabulary, though Tam doesn't use that term) while research taste resists automation because problem selection has no ground truth. Tam argues market pricing reflects this — quant firms paying $600k for "research taste" — though this could also reflect tournament dynamics or talent scarcity rather than oracle strength per se. Karpathy's autoresearch automates hyperparameter sweeps (verifiable) but not problem selection (unverifiable) — the boundary runs through a single tool.

**Capability-timeline predictions (Amodei).** [Amodei's interview] shows a confidence gradient: strong optimism on coding and math (where progress is measurable against tests and benchmarks) but acknowledged uncertainty on novel writing and scientific discovery (where quality is harder to verify). Amodei doesn't use oracle vocabulary — this is our interpretive frame — but the pattern is consistent: his confidence correlates with verification availability, not raw capability claims.

**Supply-chain integrity (in-toto).** [in-toto] makes supply-chain trust decisions automatable by turning an otherwise social/process question ("did the right steps produce this artifact?") into signed, hash-checked metadata over the whole chain. The domain has unusually hard oracles — byte identity, signatures, and declared artifact-flow rules — so it does not solve the KB's judgment-heavy verification problem. It does show the positive case cleanly: once the verifier exists and is cheap enough to run at deployment boundaries, an operational trust decision can move from manual review to automation.

## Why convergence matters

Any single source is explainable without the framework. Amodei's confidence split could be mere selection bias (he has benchmarks for coding, not for novels). Tam's labor-economics argument could be an investor thesis dressed up as analysis. The oracle-strength spectrum could be an internally consistent theory that happens not to be true. in-toto could be dismissed as a special property of cryptographic byte workflows.

But five sources — theory, market economics, supply-side capability predictions, supply-chain security engineering, and 1980s human-factors research — arriving at the same structural claim through different reasoning is harder to explain away than any single source. The convergence makes this a candidate for a general principle rather than a domain-specific observation, though the shared citations between the sources temper the evidential weight.

## The practical implication

If this holds, the leverage point for expanding automation is not better models but better oracles. The engineering priority becomes: invest in verification infrastructure before capability. [Spec mining] manufactures oracles. [Error correction] amplifies weak ones. The path to automating any task starts with the question: *can we build a verifier?*

This applies to KB curation directly. [Automating KB learning] stalls on judgment-heavy mutations (synthesis, connection quality, what to skip) — exactly the operations where oracle construction is hardest. The bottleneck is not that agents can't generate candidate mutations; it's that no one can cheaply verify whether a proposed mutation improves the KB.

## Caveats

- **The claim is about structure, not permanence.** Oracle construction difficulty is not fixed. Domains that are no-oracle today may become hard-oracle tomorrow through better tooling, better metrics, or domain decomposition. The claim predicts *where* automation stalls, not that it stalls forever.
- **Convergence is not proof.** Three sources agreeing could reflect a shared assumption rather than an independent discovery. All three operate within a broadly rationalist, verification-oriented worldview — a critic from a different tradition (e.g., one that values tacit knowledge or embodied practice) might see the convergence as circular.
- **Error-cost tolerance is a separate variable.** Some tasks get automated despite poor verification because errors are cheap — machine translation for low-stakes content, draft generation for human review. The framework focuses on verification cost but doesn't account for domains where tolerance for unverified output is high enough that oracle construction becomes unnecessary.
- **Oracle gaming is unaddressed.** The framework treats oracle availability as uniformly positive, but cheap oracles can produce pathological automation — recommendation algorithms optimizing engagement metrics, teaching to the test, RL reward hacking. In these cases, the oracle exists and is cheap, yet automation against it is actively harmful. Oracle *quality* matters, not just oracle *availability*.
- **The framework may not cover all cases.** Some tasks resist automation for reasons other than verification difficulty — regulatory constraints, trust requirements, liability concerns. The title uses "the" boundary as a claim title, but the argument defends verification as *the primary structural* boundary, not the only one.

---

Relevant Notes:

## Under-review context phrase

verification cost determines which qualities can support warranted automation
