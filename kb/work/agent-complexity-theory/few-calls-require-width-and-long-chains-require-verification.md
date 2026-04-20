---
description: "Decomposition sits on a width-loss-reliability frontier: exact short pipelines need wide prompts or high-bandwidth interfaces, while long unchecked chains accumulate error and therefore need verifier or redundancy stages"
type: kb/types/note.md
traits: []
tags: [computational-model, context-engineering, llm-interpretation-errors]
status: seedling
---

# Few calls require width and long chains require verification

Decomposition is not a free optimization knob. In the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md), reducing call count means each call must absorb more of the task-relevant state directly or inherit a richer intermediate representation from earlier stages. Increasing call count makes local prompts easier, but it lengthens the stochastic chain through which errors can survive. So bounded-call design sits on a frontier: **few calls require width or lossy compression; long chains require verification, redundancy, or both**.

The claim has two parts:

- **Exactness frontier.** If later stages cannot reopen the raw sources, then each compression boundary must preserve all downstream-relevant distinctions that cross it. Cutting the pipeline shorter therefore forces some stage to carry more task-relevant structure directly, either as wider prompt context or as a larger intermediate artifact.
- **Reliability frontier.** If the final answer depends on `L` load-bearing stochastic calls after the last verifier, then unchecked error accumulates with `L`. In the common regime where stage errors are at least weakly independent, success decays multiplicatively. To keep end-to-end reliability bounded away from zero as chains grow, systems need verifier stages, voting, or other error-correcting structure.

## Evidence

- [No universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md) already gives the core exactness lower bound. A bounded summary can only preserve a bounded number of query-induced distinctions.
- [Adaptive dependencies force width, reopening, or sequential rounds](./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md) shows the operational consequence for decomposition: if a task's interaction structure is real, making the pipeline shallower does not eliminate the structure; it only moves where the system pays for it.
- [Effective context is task-relative and complexity-relative, not a fixed model constant](../../notes/effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) explains why "few calls require width" is substantive. Prompt width means larger effective burden on the bounded call, not just more raw tokens.
- [Error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) identifies the positive side of the reliability claim: long chains are viable when the architecture periodically inserts checks with real discriminative power.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) already argues that verification is not an optional cosmetic add-on. This note supplies the tradeoff reason: decomposition changes both context cost and where reliability must be restored.

## Formal setup

Consider a bounded-call pipeline

`K_0 -> K_1 -> ... -> K_C`

where each stage may inspect raw state, call the model, and export an intermediate artifact to the next stage.

For each cut `i`, let `B_i` denote everything from the prefix that remains available to stages `i+1, ..., C` without reopening earlier raw state. This `B_i` may be a summary, schema instance, extracted claim set, table, or any other interface artifact.

For reliability, define an **unverified tail** to be a maximal suffix of stochastic stages between two verifier events. A verifier event is any step strong enough to reject, repair, or majority-correct upstream errors rather than merely passing them along.

## Results

### Proposition 1: Interface capacity lower bound

Fix a cut `i` and a downstream exact query family `Q_i` that must be answerable by the suffix using only `B_i` and the post-cut state. Let `N_i` be the number of distinct downstream-relevant answer profiles induced across that cut. Then any exact no-reopen pipeline must satisfy

`|B_i| >= log_2 N_i`

bits of effective interface capacity at cut `i`.

#### Proof sketch

This is the same counting argument as in [No universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md), applied locally to a single pipeline cut. If `B_i` carried fewer than `log_2 N_i` bits, then it would have fewer than `N_i` possible codes. Two prefix states with different downstream-relevant profiles would collapse to the same exported interface. Since the suffix sees the same post-cut inputs in both worlds, it must return the same answer in both, contradicting exactness.

The consequence is local but important. Every cut has a minimum interface burden. A decomposition does not make this burden vanish; it decides where in the pipeline that burden is carried.

### Corollary: Fewer calls shift burden onto wider stages or richer interfaces

If a task family requires large `N_i` across some conceptual boundary, then a shorter exact pipeline can only remain correct by paying that burden somewhere else: wider prompts in a merged stage, richer exported artifacts, or later reopening of raw sources. Removing stages does not remove the distinctions that must survive.

This is the formal core of the "few calls require width" side of the frontier. A short pipeline is exact only when some surviving stage internalizes the cross-cut structure that would otherwise have been represented explicitly across multiple cuts.

### Proposition 2: Unverified tails have exponentially decaying success

Consider an unverified tail of `L` load-bearing stochastic stages. Let `E_t` be the event that stage `t` introduces an error that survives to the output of that tail. If the `E_t` are independent with probabilities `epsilon_t`, then

`P(success on the tail) = product_t (1 - epsilon_t) <= exp(-sum_t epsilon_t)`.

In particular, if `epsilon_t >= epsilon > 0` for all tail stages, then

`P(success on the tail) <= exp(-epsilon L)`.

#### Proof sketch

Under the stated independence assumption, the tail succeeds only if every stage avoids a surviving error, so the success probability is the product of the per-stage success terms. Applying `1 - x <= e^(-x)` gives the exponential upper bound. Under a uniform lower bound `epsilon_t >= epsilon`, the exponent is at least `epsilon L`.

The theorem is intentionally minimal. It does not assume catastrophic failure at every mistake, only that each stage has some nonzero probability of introducing an error that persists until the next verifier.

### Corollary: Long pipelines need periodic verification

To keep tail success at least `rho`, an architecture with per-stage surviving-error rate at least `epsilon` cannot permit unverified tails longer than

`L <= (1 / epsilon) log(1 / rho)`.

So once decomposition creates long stochastic chains, verification is not optional bookkeeping. It is the mechanism that resets the error budget by cutting the chain into shorter verified segments.

## Why it matters

The two propositions explain why decomposition should be treated as an explicit optimization over coupled costs, not as a free modularity win.

- Proposition 1 says every cut carries an interface obligation. If the task family induces many downstream-relevant distinctions, then exact short pipelines need wide prompts, large exported structures, or raw reopening.
- Proposition 2 says every unverified suffix carries an error obligation. If the chain is long, some verifier or redundancy structure must cut it back down.

Together they yield the intended engineering rule: planner decisions should be evaluated on a **cost / reliability frontier**. More decomposition usually lowers per-call complexity, but it increases interface count and creates more places where surviving stochastic error must be corrected. Less decomposition reduces chain length, but only by forcing some remaining stage to shoulder more joint structure directly.

## Caveats

- The exactness argument is worst-case and exact. If the future query family is narrow or distributionally concentrated, a small interface may be enough in practice.
- The exponential reliability formula uses independence. Real agent errors are often correlated, in which case naive repetition helps less. That strengthens the practical need for decorrelated verifiers rather than weakening it.
- Not every verifier must be an LLM judge. Tests, schema checks, type checks, and retrieval-consistency checks are often cheaper and stronger whenever the task admits them.
- The frontier is qualitative here, not a full optimization theorem. Real systems also care about latency, human oversight, and the cost of building stronger intermediate artifacts.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — foundation: decomposition is analyzed inside the select/call architecture where prompt width and chain depth are first-class costs
- [no universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md) — exactness lower bound: narrow interfaces cannot preserve every downstream distinction for rich query families
- [adaptive dependencies force width reopening or sequential rounds](./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md) — companion result: shows where the lost interaction cost reappears operationally when a task resists shallow decomposition
- [effective context is task-relative and complexity-relative not a fixed model constant](../../notes/effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — clarifies: the "width" side of the frontier is effective burden on bounded calls, not merely token count
- [decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: the heuristics can be read as moves along an explicit frontier rather than as free improvements
- [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: gives the positive theorem for recovering reliability after long stochastic chains
- [topology, isolation, and verification form a causal chain for reliable agent scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) — extends: explains why deeper decompositions need isolation and verification structure rather than assuming chain length is harmless
- [synthesis is not error correction](../../notes/synthesis-is-not-error-correction.md) — boundary: adding more stages or more agent outputs without adjudication is not reliability improvement
