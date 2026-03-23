---
description: Brainstorming note that turns the pairwise-comparison hypothesis into a staged test plan for open-ended LLM evaluation loops
type: note
traits: [has-external-sources]
tags: [evaluation, llm-interpretation-errors, context-engineering]
status: seedling
---

# Brainstorming: how to test whether pairwise comparison can harden soft oracles

The [Koylan source on pairwise comparison](../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy-for-scient-2035982137539559616.ingest.md) suggests a plausible mechanism: in open-ended tasks, asking a judge "which of these two outputs is better?" may be easier and more stable than asking "score this output 1-5." That is an interesting hypothesis, but still only a hypothesis. Before promoting it into a stronger claim, we need a test design that can distinguish genuine oracle hardening from mere prompt reformulation.

The core question is not whether pairwise comparison *sounds* more natural. It is whether it improves the properties that actually matter for a soft oracle: discrimination, stability, calibration, and usefulness inside an optimization loop.

## What would count as "hardening" here?

On the [oracle strength spectrum](./oracle-strength-spectrum.md), pairwise comparison would count as hardening only if it moves a judge toward a more useful signal, not merely a differently formatted one. At least one of these should improve:

- **Higher discrimination** — pairwise judgments separate better outputs from worse ones more reliably than scalar scores do
- **Lower variance** — repeated judgments on the same examples fluctuate less
- **Better optimization utility** — loops that optimize against pairwise judgments produce better outputs than loops using scalar judgments
- **Better bias behavior** — the new format reduces one failure mode without introducing worse ones elsewhere

If none of these improve, then pairwise comparison is not hardening the oracle. It is just changing the judge's interface.

## The simplest test is not enough

A trivial comparison like "do humans prefer pairwise prompts?" would be too weak. Evaluator comfort is not the point; the point is whether the resulting signal supports selection and improvement better than scalar scoring. Likewise, it is not enough to show that pairwise comparison can produce a ranking. Scalar scores can also produce a ranking. The question is whether the ranking tracks quality more faithfully.

So the test plan should climb a ladder from weakest evidence to strongest:

1. **Judgment quality**
2. **Ranking quality**
3. **Loop-improvement quality**

Each step asks a stricter question than the one before it.

## Test 1: judgment quality on a hand-labeled set

The cheapest useful experiment is an offline benchmark built from a manually adjudicated mini-corpus.

Setup:
- Pick one open-ended task family where absolute scoring is known to be noisy: note critiques, synthesis candidates, prompt rewrites, or short analytical answers
- For each prompt, generate multiple candidate outputs from the same model and prompt family
- Have a human create a gold preference ordering, or at minimum a set of pairwise winner labels

Then compare two judging schemes on the same examples:
- **Scalar judge** — score each output independently on a 1-5 or 1-10 scale
- **Pairwise judge** — compare outputs in pairs, optionally with position-swapping as recommended in [Agent Skills for Context Engineering](./related-systems/agent-skills-for-context-engineering.md)

Measures:
- Agreement with human pairwise labels
- Run-to-run variance on repeated judgments
- Position bias rate
- Intransitivity rate (A > B, B > C, C > A)

This is the first gate. If pairwise judgment does not beat scalar judgment here, there is no strong reason to spend more effort on ranking or loop-level tests.

## Test 2: ranking quality over candidate sets

The source's stronger idea is not just that pairwise calls are locally better, but that many pairwise calls can be aggregated into a useful ranking via tournament win rate. That requires a separate test.

Setup:
- For each prompt, generate `N` candidates
- Build two rankings:
  - scalar ranking from independent quality scores
  - pairwise ranking from round-robin win rates
- Compare both against a human-produced ranking or top-k selection

Measures:
- Top-1 match rate with human choice
- Top-k overlap
- Rank correlation with human ordering
- Sensitivity to candidate-set changes: does adding one bad candidate distort the ranking?

This matters because pairwise comparison might work locally while still producing unstable or misleading global rankings. Non-transitivity is the clearest failure mode to watch.

## Test 3: optimization-loop value

The strongest version of the idea is that pairwise comparison is not just a better evaluator, but a better optimization primitive. That requires a loop test.

Setup:
- Choose one loop where a soft oracle already drives selection: prompt refinement, candidate-answer selection, or KB mutation ranking
- Run two otherwise identical optimization loops:
  - one selects by scalar score
  - one selects by pairwise tournament ranking
- Keep generation budget approximately matched so the comparison is not just "more judge calls wins"

Measures:
- Human-rated quality of the final selected outputs
- Diversity retained in the beam or candidate pool
- Improvement per unit judge cost
- Whether repeated optimization produces drift toward obviously bad proxies

This is the test that decides whether pairwise comparison is actually useful in context engineering. An offline signal can be interesting on its own, but if it does not improve loop outcomes, the original intuition weakens substantially.

## Good benchmark choices

The benchmark should be hard enough that absolute scoring is noisy, but bounded enough that human adjudication remains feasible.

Promising candidates:
- **Prompt rewrite selection** — many plausible outputs, weak hard oracle, easy human pairwise labeling
- **Short synthesis-note drafts** — relevant to this KB, but risk of evaluator overfitting to local style
- **Critique quality** — ask which critique would more help a writer improve a draft
- **Related-note connection proposals** — ask which connection explanation is more useful or more defensible

Poor candidates:
- **Pure coding tasks with tests** — if a hard oracle already exists, pairwise soft-oracle improvement is less interesting
- **Tasks with no adjudicable quality difference at all** — if humans cannot label the data consistently, the experiment collapses before judge comparison even begins

## Failure modes the experiment must distinguish

Several easy false positives need to be ruled out:

- **Format effect without signal improvement** — pairwise prompts feel better but agreement with humans does not improve
- **Cost masking** — pairwise wins only because it spends far more judgment budget
- **Bias trade** — pairwise reduces scalar compression noise but introduces strong position or anchoring bias
- **Overfitting to the benchmark** — one prompt template works on the hand-labeled set but not in a live loop
- **Tournament illusion** — round-robin produces a precise ranking from noisy and cyclic preferences, creating false confidence

A real win should survive these checks. Beating a weak baseline on one metric is not enough.

## What would falsify the idea?

These outcomes should count against the thesis:

- Pairwise judgments are no more stable than scalar ones on repeated runs
- Human agreement does not improve after controlling for position bias
- Tournament rankings correlate no better with human rankings than scalar scores do
- Optimization loops selected by pairwise ranking do not improve final output quality enough to justify extra cost
- Gains disappear once prompts are rewritten or models are swapped

If most of these happen, the right conclusion is probably not "pairwise can harden soft oracles," but something narrower like "pairwise is a useful interface trick in a few settings."

## The easiest high-value experiment for this KB

Inside commonplace, the most practical first experiment is probably candidate selection for short analytical outputs.

One concrete design:
- Sample 20-30 prompts asking for a short explanation, critique, or synthesis
- Generate 4 candidates per prompt
- Ask a human to pick the best candidate and maybe rank the top two
- Compare:
  - scalar judge selecting best of 4
  - pairwise round-robin judge selecting best of 4
- Repeat judgments several times to estimate variance

Why this is a good first pass:
- cheap enough to run manually
- directly relevant to our note-writing and evaluation work
- produces both pairwise and ranking data
- avoids pretending we already have a mature autonomous loop

If that works, the next step would be a mutation-based KB experiment where the judge chooses between candidate link additions, rewrites, or synthesis proposals.

## Open questions

- Does pairwise judgment improve discrimination itself, or mostly reduce prompt-interpretation noise?
- Is round-robin the right aggregation method, or would partial tournaments / Swiss-style comparisons preserve most of the benefit at lower cost?
- Are there tasks where scalar scores are actually better because absolute thresholds matter more than local comparisons?
- How much human agreement is required before this becomes a meaningful judge benchmark rather than a disagreement study?
- Should the benchmark optimize for winner selection only, or for full ranking fidelity?

---

Relevant Notes:

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — **extends**: turns that note's abstract oracle-hardening question into a concrete experimental program
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **qualifies**: asks whether pairwise comparison improves the base signal before amplification, rather than replacing amplification
- [Agent Skills for Context Engineering](./related-systems/agent-skills-for-context-engineering.md) — **grounds**: supplies the concrete pairwise-comparison and position-bias-mitigation practices this note would test
- [Autocontext](./related-systems/autocontext.md) — **example**: offers a live evaluation loop where pairwise ranking could be compared against scalar LLM judging
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — **parallel**: another brainstorming note about manufacturing better soft oracles, but at KB-wide rather than candidate-ranking scope
- [Koylan pairwise-comparison source](../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy-for-scient-2035982137539559616.ingest.md) — **source**: origin of the specific hypothesis this note turns into a test plan
