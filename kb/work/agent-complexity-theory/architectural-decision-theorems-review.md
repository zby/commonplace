# Architectural decision theorems: review and proposed pivot

This records a ChatGPT review supplied by the maintainer on 2026-08-04. It is a proposal for the workshop, not an independently verified literature review. The elementary arguments below can be checked directly. The communication-complexity positioning, competitive-analysis claim, and links to prior work still need source review before promotion.

## Proposed standard for this workshop

The workshop should pivot from resource lower bounds to **architectural decision theorems**. A theorem earns its place when it does at least one of these:

1. rules out a plausible decomposition;
2. chooses between summarization, retention, and reopening;
3. gives a measurable crossover threshold;
4. produces a scheduling or verification policy.

The proposed central family is:

> A decomposition creates an information cut. The cost of that cut is determined by the downstream distinctions that must cross it.

This retains the useful lower bounds but makes them inputs to design decisions. The answer-profile result becomes the central theorem. Opaque retrieval remains a limiting case. The archive and call-width models become accounting frameworks until they produce thresholds or policies.

## 1. Decomposition cuts as communication channels

Let `x` be a source state in `X`. An upstream stage sees `x`, constructs a `b`-bit artifact `sigma(x)`, and discards `x`. A downstream stage later receives a query `q` from `Q` and must recover `q(x)` from only `sigma(x)` and `q`.

Define query equivalence by

`x ~_Q x'` exactly when `q(x) = q(x')` for every `q` in `Q`.

Let `K_Q` be the number of equivalence classes.

### Exact answer-profile characterization

Under an information-only model that does not charge local symbolic computation or decoder size,

`b_min = ceil(log_2 K_Q)`.

The existing [bounded-summary note](./no-bounded-summary-preserves-all-distinctions-for-a-rich-query-family.md) proves the lower half. Fewer than `K_Q` codes collapse two states that some query distinguishes. The matching upper half assigns one code to each answer profile. The decoder returns the coordinate selected by `q`.

For a general task `F(x, y)`, where the downstream stage learns `y` only after the cut, the same setup is a deterministic one-way communication protocol:

- the upstream stage holds `x`;
- the downstream stage holds `y`;
- the artifact is the message;
- the downstream stage cannot reopen `x`.

The minimum fixed-width exact message is therefore the ceiling of the base-two logarithm of the number of distinct rows `F(x, .)`. This is the answer-profile theorem stated in communication language.

### Frozen-decomposition corollary

If a cut permits only `b` bits but its upstream states induce more than `2^b` downstream answer profiles, then no improvement confined to the components can make that fixed no-reopen decomposition exact. The architecture must instead do at least one of these:

- increase interface capacity;
- move the cut so interacting information is co-located;
- allow reopening or interaction;
- narrow the query family or accept error.

This is the strongest connection to reflective self-improvement. A decomposition is part of the reflective surface because some failures are properties of the cut, not of the prompts or components on either side.

### Addressability separation

Consider `x` in `{0,1}^N`, a late-bound coordinate query `i` in `[N]`, and `F(x, i) = x_i`. Every state has a distinct answer profile, so a source-replacing summary that answers every later coordinate query needs at least `N` bits.

An addressable architecture retains the `N` source bits outside active context. Once `i` is known, the active retrieval exchange needs only `ceil(log_2 N)` selector bits plus the requested answer bit. The original information has not disappeared. Storage cost and query-time active bandwidth have been separated.

The resulting design claim is:

> For late-bound query families, retaining addressable sources can require asymptotically less active interface bandwidth than any source-replacing universal summary.

This distinguishes “summary plus source pointer” from “summary and discard source.” A formal reopening theorem should state the storage-access or interaction model precisely before identifying its savings with an interactive communication-complexity gap.

## 2. Correction: adaptivity trades rounds for speculative breadth

The width-independent `Omega(L)` claim in [Adaptive dependencies force width, reopening, or sequential rounds](./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md) is false for its stated family. The candidate layers are known. With unrestricted fan-out, an orchestrator can inspect every node in every layer in one batch, recover every successor mapping, and follow the realized path symbolically. This can require enormous work, but not `L` rounds.

### One-batch speculative-lookahead theorem

Use a hidden `B`-ary pointer tree with `B >= 2`. Inspecting one node reveals which child continues the path. Starting at a known node, resolving `h` successive hidden choices in one nonadaptive batch requires exactly

`T_B(h) = 1 + B + B^2 + ... + B^(h-1) = (B^h - 1) / (B - 1)`

worst-case node inspections.

**Lower bound.** Every internal node in the depth-`h` prefix must be inspected. If one is omitted, an adversary can route the true path through it and choose two different successors in otherwise indistinguishable worlds.

**Upper bound.** Inspect the complete depth-`h` prefix, then follow the returned pointers symbolically.

With per-round inspection budget `P`, guaranteed lookahead is therefore at most

`h <= floor(log_B((B - 1)P + 1))`.

For `B = 5`, removing four dependent round trips costs `1 + 5 + 25 + 125 = 156` speculative inspections.

The architectural decision is now explicit: accept another dependent round, pay exponentially growing speculative work, or improve the pointer/index layer so the effective branching factor falls.

For depth `D` and `R` rounds, inspecting a complete subtree of depth about `D/R` at each realized frontier gives an immediate balanced-block upper bound of about `R * T_B(ceil(D/R))` total inspections. A matching lower bound must handle prefetching across future frontiers. Until that proof is complete and positioned against pointer-chasing literature, the full rounds-versus-work frontier is a conjecture.

## 3. A stopping rule for decomposition

Let:

- `W` be total effective semantic workload;
- `w_i` be the workload assigned to stage `i`;
- `c(w)` be the expected cost of a call of effective width `w`, including latency, failure, and retry costs;
- `h` be the cost added by each interface;
- `sum_i w_i = W`.

For `k` stages,

`C = sum_i c(w_i) + (k - 1)h`.

Assume `c` is convex and the pieces are independent apart from the fixed interface cost.

### Optimal granularity under separability

For fixed `k`, equal pieces minimize cost by convexity:

`w_i = W/k`.

Write the common piece width as `x = W/k`. An interior continuous optimum satisfies

`x c'(x) - c(x) = h`.

For `c(x) = a x^gamma` with `gamma > 1`,

`x* = (h / (a(gamma - 1)))^(1/gamma)`.

This yields the rule:

> Continue splitting while the reduction in superlinear within-call cost exceeds the extra interface cost.

The result deliberately excludes cross-piece dependencies. When those matter, `h` must include the communication burden from the cut theorem and may depend on where the cut falls. Convex call cost determines how much independent work belongs in a call; interface complexity determines where splitting is permissible.

The empirical program is to measure `c(w)` for a task class, measure interface construction/retrieval/validation cost, predict the optimum, and test whether observed performance follows it.

## 4. When reasoning should crystallize into an artifact

Let:

- `B` be the cost to build, validate, integrate, and maintain a retained artifact over its useful life;
- `r` be the per-use cost of deriving the result again;
- `u < r` be the per-use cost of retrieving and applying the artifact;
- `T` be the number of uses before invalidation.

### Materialization threshold

Materialization pays exactly when

`B + Tu <= Tr`,

or

`T >= B / (r - u)`.

When future reuse is unknown, let `Delta = r - u`. Re-derive until cumulative avoidable cost reaches `B`, then materialize. In the simple no-invalidation model this is the standard deterministic rent-or-buy threshold and is 2-competitive with an offline policy that knows future reuse.

This gives a direct runtime policy:

- log repeated semantic derivations;
- estimate derivation, retrieval, validation, and maintenance costs;
- materialize when accumulated avoidable re-derivation cost crosses build cost;
- reset or recompute the decision when source changes invalidate the artifact.

Stronger models lower `r` and therefore raise the threshold. They do not imply that no retained artifact pays.

## 5. Verification spacing instead of a generic chain warning

The reliability discussion in [Few calls require width and long chains require verification](./few-calls-require-width-and-long-chains-require-verification.md) needs a correlation correction. Arbitrary correlation does not necessarily worsen exponential decay. If every stage shares one perfectly correlated failure event, total success can remain `1 - epsilon` for every chain length.

Let:

- `k` be the number of stochastic steps between verifiers;
- `v` be verifier cost in step-equivalents;
- `q(k)` be the probability that a `k`-step attempt is correct;
- the verifier detect every failed attempt;
- the retry policy have the same measured success probability `q(k)` on each attempt.

Then expected cost per committed step is

`C(k) = (k + v) / (k q(k))`.

Choose the integer `k` that minimizes this measured quantity. No independence assumption among steps inside a segment is needed when `q(k)` is measured directly. The geometric retry calculation still assumes the retry process is stable enough for expected attempts to be `1/q(k)`; persistent correlated failures require a richer retry model.

Under independent per-step error probability `epsilon`, let `lambda = -ln(1 - epsilon)`. Then `q(k) = (1 - epsilon)^k`, and the continuous minimizer is

`k* = (sqrt(v^2 + 4v/lambda) - v) / 2`.

For small `epsilon` and moderate `v`,

`k* ~= sqrt(v/epsilon)`.

Cheap verification and high failure hazard imply shorter segments. Expensive verification and reliable steps justify longer segments.

For a lower-bound statement, independence can be replaced with the conditional hazard assumption

`P(E_t | no prior surviving error) >= epsilon`.

That assumption implies exponential decay. Correlation by itself does not.

## 6. Positive sufficient conditions

### Mergeable summaries

A hierarchical summary architecture needs a bounded summary map `sigma` and merge operator `mu` such that

`sigma(A union B) = mu(sigma(A), sigma(B))`.

If each summary fits the interface, is sufficient for the declared query family, and remains sufficient after merging, then `N` partitions can be reduced in logarithmic depth with bounded fan-in.

The practical requirement is a **merge contract**, not just a prose format. Depending on the task, tests should cover associativity, order invariance, identifier preservation, size bounds, and preservation of query-relevant distinctions. Without these properties, a summary tree remains a heuristic.

### Adaptive witness coverage

The [opaque-retrieval bound](./exact-retrieval-over-semantically-opaque-items-requires-linear.md) should remain as a boundary lemma. Its opacity assumption intentionally removes every useful retrieval signal.

For practical retrieval, represent progress as coverage of required evidence or witnesses. If expected marginal witness coverage is adaptive monotone and adaptive submodular, adaptive greedy selection has guarantees against the best adaptive policy. The operational rule is:

> Inspect the candidate with the highest expected new witness coverage per unit cost.

The open empirical question is which semantic research tasks approximately satisfy those conditions.

## Proposed workshop reorganization

### Information cuts and addressability

Combine the bounded-summary, interaction-width, and interface-capacity arguments into:

- the exact answer-profile characterization;
- the cut/one-way-communication equivalence;
- the frozen-decomposition corollary;
- the addressability separation.

### Adaptivity and speculative work

Replace the width-independent round claim with:

- the exact one-batch speculative-lookahead theorem;
- the per-round breadth/lookahead corollary;
- a clearly marked conjecture for the full rounds/work frontier.

### Online architectural policies

Develop:

- the materialization threshold;
- optimal decomposition granularity;
- verifier spacing;
- later, pointer/index amortization.

### Positive sufficient conditions

Develop:

- mergeable sufficient summaries;
- adaptive-submodular retrieval or witness coverage.

### Transfer to agent programs

Prove each result first in the smallest source/query/oracle model. Use [select/call universality](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) only afterward as a transfer corollary. This keeps the theorem model visible and separates the new architectural reduction from standard operational-semantics machinery.

## Priority and status

| Result | Workshop treatment |
|---|---|
| Exact profile characterization and cut equivalence | Headline theorem; next standalone proof note |
| Frozen-decomposition corollary | Main reflective-self-improvement consequence |
| Addressability separation | Main Commonplace-specific architectural consequence |
| Full rounds/speculative-work frontier | Most promising proof project; currently conjectural |
| Materialization threshold | Most immediately implementable policy |
| Optimal granularity and verifier spacing | Empirical calibration programs |
| Opaque retrieval | Retain as a boundary lemma |
| Archive model and call-width frontier | Retain as accounting frameworks until they choose an architecture |

The proposed next theorem note is **“Decomposition cuts are one-way communication channels.”** It should contain the exact profile theorem, addressability separation, and frozen-decomposition corollary.

## Literature pointers supplied by the review

These are leads for source verification, not yet evidence audited by this workshop:

- [Pointer chasing, rounds, and communication tradeoffs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol325-itcs2025/html/LIPIcs.ITCS.2025.75/LIPIcs.ITCS.2025.75.html)
- [Rent-or-buy / ski-rental reference cited for the threshold policy](https://arxiv.org/abs/2308.05067)
- [Mergeable summaries](https://pure.au.dk/portal/en/publications/mergeable-summaries/)
- [Adaptive submodularity](https://arxiv.org/abs/1003.3967)
