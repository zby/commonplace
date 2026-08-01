# Case packet

Neutral case identifier: case-8a530b0c39ba8e

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# An LLM's generation confidence tracks typicality, not soundness

*Speculative. The core decoupling claim is defensible; the anti-correlation case, the internal-probe conjecture, and the hallucination-parent framing are retained conjecture pending evidence.*

A token-generating model's confidence — the probability it assigns to a continuation — measures how *typical* that continuation is given the running text. It does not measure whether the continuation is *sound*: true as a matter of fact, or validly inferred from what came before. Training optimizes the likelihood of text, and fluent, plausible-looking text is high-probability whether or not it is correct. "Paris is the capital of France" and "Lyon is the capital of France" are both just typical-looking French-geography sentences to the decoder; a fluent "because X, therefore Y" is what an argument *looks like* whether or not Y follows from X.

So confidence and soundness are **decoupled** — and that is weaker than anti-correlation, a distinction that matters. Decoupling says only that confidence is *uninformative* about soundness: you learn nothing about whether a claim is true or valid from how probable the model found it. It does not by itself say confidence is *highest* where soundness is lowest. That stronger, anti-correlated case holds only under an added premise — that unsound moves are themselves *typical* (clichés, common fallacies, plausible fabrications that recur in training text). Where that premise holds, and it often does, the model is most fluent exactly at the joint where it should hesitate; but the anti-correlation is an extra empirical claim, not a consequence of decoupling.

## Consequence: soundness needs a separate check

Because the signal is not in the generation confidence, you cannot recover it by reading that confidence off — thresholding on token probability, or asking the model "how sure are you," surfaces typicality, not truth or validity. Detecting unsoundness requires a *separate operation* that recomputes what confidence fails to track: an external oracle (a compiler, a test, a retrieval check), a trained probe, or an adversarial pass that re-derives the inference instead of re-reading the prose. This is why the boundary of reliable automation tracks the [availability of a verifier], not the model's apparent certainty.

Whether a *separate internal representation* of soundness exists — one a probe could read from hidden states even though it is absent from the output distribution — is genuinely open; models may encode some truthfulness signal internally, though that is an unsettled empirical question this note does not adjudicate. Even if such a representation exists, it is not the next-token signal, and recovering it is still a separate operation, not the generator volunteering its confidence. Sycophancy — deployment tuning that rewards agreement with the user over correction — adds an independent reason the signal stays hidden: that tuning can bias outputs toward agreement even where internal features could support a correction.

## Two faces

The same decoupling produces two failures, one per kind of soundness:

- **Correspondence** — a hallucinated *fact* is stated with full fluency, because fabrication is typical-looking text.
- **Coherence** — an unsupported *inference* reads smoothly, because a connective plus a plausible clause is typical-looking argument. This is the hidden "signal" in [the composition-friction loss]: the stall a human would feel at a weak "because" is exactly what cannot be read off the model's confidence.

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

soundness needs a separate verifier precisely because confidence does not track it
