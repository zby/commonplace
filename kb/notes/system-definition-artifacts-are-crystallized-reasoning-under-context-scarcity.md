---
description: Heuristic system-definition artifacts (tips, playbooks, rules) are mostly crystallized reasoning — pre-compiled shortcuts for what a capable LLM would derive if it had all facts and unlimited compute; under unbounded context heuristic prose collapses into knowledge plus read-time derivation, authority-bearing constraints persist regardless, and codification has a compound motivation that partly collapses (scale decomposition) and partly survives (constraining compound)
type: kb/types/note.md
traits: [has-comparison, title-as-claim]
tags: [learning-theory]
---

# System-definition artifacts are crystallized reasoning under context scarcity

## Thought experiment: unbounded context

Imagine unbounded context plus a capable LLM. All facts load at once, multi-hop reasoning runs in a loop until it converges, nothing gets truncated. How much of what we currently call **system-definition** — tips, playbooks, skills, decision rules, prompts — would still need to exist?

Most of it wouldn't. Tips are compressed lessons from prior trajectories; the LLM could re-derive them from raw traces. Playbooks are abstractions over successful sequences; they'd get reconstructed case-by-case. Even the "what kind of agent" core melts: user preferences become facts — "the user prefers concise answers," "the user is a senior Go developer" — and get retrieved like any other datum. In practice there is no separate policy store for values; the values live as data about the user.

Under this view, **heuristic system-definition artifacts are mostly crystallized reasoning**: pre-compiled shortcuts for what the LLM would derive if it had infinite context and infinite time. [Distillation](./definitions/distillation.md) is the operator that produces them, because distillation compresses prior reasoning into task-ready artifacts. Under unbounded context, distillation stops being *necessary* — deferred reasoning at read-time is available. It may still pay as an optimization (shorter reads are faster and cheaper), but the substrate no longer depends on it.

The "heuristic" qualifier matters because not every policy-like artifact exists to save reasoning. Authority-bearing constraints — permissions, safety rules, scoping boundaries, interface contracts, coordination commitments — have force as explicit commitments, not as compressed reasoning. An unbounded model might know the facts behind them, but the artifact itself carries binding authority the facts don't. The crystallization claim is strongest for tips, playbooks, skills, and decision rules; weaker for authority-bearing constraints, which the thought experiment leaves untouched.

## What this reframes about the role axis

[Axes of substrate analysis](./axes-of-substrate-analysis.md) distinguishes **knowledge substrate** (consumed as fact) from **system-definition artifact** (consumed as policy). The crystallization view sharpens what that distinction is about:

- **Knowledge reads** defer reasoning to a single read-time pass. Adding facts grows reach additively — no ahead-of-time conflicts to resolve.
- **System-definition reads** *are* pre-committed: the policy is fixed at write-time, whether as crystallized reasoning or as explicit commitment. Two commitments made under different assumptions or by different authorities can collide. Writes are mutative.

The mutative-vs-additive asymmetry isn't a deep ontological fact about "policy vs data." It's a downstream consequence of *when* the content was fixed — write-time vs read-time. For crystallized reasoning, write-time fixing is driven by context scarcity; authority-bearing constraints fix at write-time for their own reasons, but share the same mutative consequence.

## Codification: partly scarcity patch, partly structural

[Codification](./definitions/codification.md) has a compound motivation, and only part of it is independent of context.

**The scarcity part.** Map-reduce over a 10TB dataset decomposes a problem that doesn't fit in a single LLM pass into bounded operations composed by an interpreter. The LLM writes the map function (one bounded reasoning episode); the interpreter runs it across shards. This answers the same question prose distillation does — "what do we do when the work doesn't fit the window?" — with a more powerful move: decompose across a deterministic substrate rather than compress into a shorter artifact. Under unbounded context this motivation softens: one LLM pass could in principle handle the whole dataset.

**The structural part.** The rest of what codification buys is [constraining's reliability/speed/cost/verifiability compound](./definitions/constraining.md) pushed to its strongest form — and that compound is independent of context budget. Deterministic code is cheaper than reasoning at any scale, formal semantics enable exact checks that read-time re-derivation cannot replicate, and code runs the same way every invocation while reasoning drifts. These survive the thought experiment intact.

The point: codification is a compound move, and the unbounded-context premise dissolves one of its components while leaving the others untouched. Part of codification's motivation is the same scarcity pressure that makes prose artifacts exist at all; part is independent of it.

## Implications

The thought experiment is a **diagnostic**, not a prediction. It separates what exists because context is scarce from what exists for other reasons. Whether the scarcity pressure actually relaxes as context grows is an empirical question the thought experiment alone cannot settle — there's reason to expect task complexity to scale alongside context (so pressure stays roughly binding), but that's a separate argument this note doesn't make.

What the diagnostic does show:

- **Heuristic prose system-definition** is almost entirely scarcity-driven. Its value is conditional on the binding constraint — so whether it thins in practice tracks whether that constraint relaxes, not anything intrinsic to prose.
- **Authority-bearing prose system-definition** (permissions, safety rules, scoping, contracts, commitments) persists for reasons the thought experiment doesn't address — it binds even when facts are abundant and reasoning is free.
- **Symbolic system-definition** has a compound motivation: scale decomposition (scarcity-driven, same dynamic as prose) plus the [constraining compound](./definitions/constraining.md) (structural, independent of context). Only the structural part would persist under genuine unbounded-context conditions, if those ever arrived.
- The [readable-substrate loop](./readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md) evolves asymmetrically across the prose/symbolic boundary for reasons partly downstream of this split — symbolic has a structural component that prose lacks, giving it a floor prose doesn't have — but the full asymmetry story involves iteration dynamics this note doesn't treat.

---

Relevant Notes:

- [Axes of substrate analysis](./axes-of-substrate-analysis.md) — foundation: the role axis this note reframes as write-time vs read-time reasoning
- [Distillation](./definitions/distillation.md) — operator: the compression step that produces crystallized reasoning
- [Constraining](./definitions/constraining.md) — operator: narrows interpretation, trading generality for reliability/speed/cost/verifiability
- [Codification](./definitions/codification.md) — phase transition: prose → symbolic, where crystallization changes computational regime
- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — applies: the mutative/additive asymmetry falls out of write-time vs read-time reasoning
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: coevolution of prose and symbolic, which this note diagnoses as differently motivated (heuristic prose scarcity-driven, authority-bearing prose independent, symbolic compound)
- [The readable-substrate loop is the tractable unit for continual learning](./readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md) — applies: the loop that evolves asymmetrically across prose and symbolic substrates
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: the context is where knowledge and policy merge at read-time
