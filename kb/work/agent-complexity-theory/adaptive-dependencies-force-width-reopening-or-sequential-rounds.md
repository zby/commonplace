---
description: Exact orchestration over step-dependent discovery and dense cross-item interactions must pay in prompt width, repeated reopening, or sequential rounds; parallel fan-out alone cannot remove the dependency cost
type: kb/types/note.md
traits: []
tags: [computational-model, context-engineering]
---

# Adaptive dependencies force width, reopening, or sequential rounds

In the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md), symbolic code can cache, sort, and batch arbitrary state, but only bounded calls can reveal new semantic dependency structure. That creates a second family of lower bounds beyond simple retrieval cost. For exact task families with either step-dependent discovery or dense cross-item interaction, orchestration must pay somewhere: in wider prompts that co-load the interacting material, in repeated reopening of previously seen sources, or in more sequential rounds. Parallel fan-out alone does not remove this cost, because the scheduler does not know the decisive dependency structure soon enough to exploit the width.

Two concrete forms of the claim are clean:

- **Adaptive-depth lower bound.** If the identity of the next source to inspect is semantically revealed by the current source, then a depth-`L` dependency chain requires `Omega(L)` sequential rounds regardless of parallel width.
- **Interaction-width / reopening lower bound.** If the answer depends on joint relations across `k` items and no bounded interface preserves all those relations for the downstream query family, then exact orchestration must either co-load a wide interacting set in some call or later reopen raw items to recover the lost interactions.

## Evidence

- The orchestration model already isolates the relevant boundary: symbolic operations are exact and unbounded, but new semantic facts enter state only through bounded `call(P)` steps.
- [Exact retrieval over semantically opaque items requires linear inspection](./exact-retrieval-over-semantically-opaque-items-requires-linear.md) proves that orchestration cannot avoid semantic work when symbolic state lacks relevance-correlated pointers. The present note shifts from "which items are relevant?" to "which item is needed next?" and "which items must be considered jointly?"
- [No universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md) already rules out the main escape hatch for dense interactions. If a bounded interface cannot preserve all query-relevant distinctions, then partitioning the task into narrower stages does not make the interaction disappear; it only postpones where the cost is paid.
- [Effective context is task-relative and complexity-relative, not a fixed model constant](../../notes/effective-context-is-task-relative-and-complexity-relative-not-a.md) explains why "wider prompt" here is not just about tokens. Interaction-heavy prompts are expensive because the model must use the items jointly, not merely read them side by side.
- [Decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) already treats "preserve interfaces needed for later synthesis" as a practical rule. This note is the lower-bound version: if the interface does not preserve those interactions, later exact synthesis must reopen or re-co-load the originals.

## Task families

### Adaptive chain family `A_L`

An instance of `A_L` consists of layered candidate sets `V_1, ..., V_L`, a known start node `x_1 in V_1`, and a hidden successor function `succ_t: V_t -> V_(t+1)`. The semantic content of `x_t` reveals `succ_t(x_t)` and no symbolic feature available before reading `x_t` is correlated with that successor. The target is a one-bit payload `g(x_L)` attached to the terminal node reached by following the chain.

This family isolates pure step-dependent discovery. The only way to know which node in layer `t+1` matters is to semantically inspect the node in layer `t`.

### Dense interaction family `I_(k,Q,b)`

An instance of `I_(k,Q,b)` is a tuple of raw items `y = (y_1, ..., y_k)` together with a downstream query family `Q` over the joint state. A decomposition is said to be **`b`-interface, no-reopen across a cut** if after some stage it discards access to one side of the partition and passes forward only an interface with at most `b` bits from that side. Later stages may still inspect the other side, but they may not reopen the discarded raw items.

This family isolates the case where the answer depends on cross-item relations rather than independent per-item labels.

## Results

### Theorem 1: Adaptive chain lower bound

For the task family `A_L`, every exact bounded-call orchestration algorithm requires at least `L-1` sequential semantic-dependency revelations, hence `Omega(L)` sequential rounds. This lower bound is independent of parallel fan-out width.

#### Proof sketch

Fix any program in the [select/call class](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md). Suppose it solves `A_L` in fewer than `L-1` sequential rounds. Then there is some layer `t` at which the algorithm must behave correctly about the suffix of the chain without first learning the true successor out of `V_(t+1)`.

But by construction, before semantically reading `x_t`, the scheduler has no relevance-correlated symbolic feature that distinguishes the true successor from the decoys. So there exist two worlds that are identical on everything the algorithm has seen so far but differ in which node is `succ_t(x_t)`. Make the terminal payload bits differ in those two worlds. Since the algorithm has the same symbolic state and the same prior call results in both worlds, it must make the same downstream decisions in both. That yields the same final output in both worlds, even though exactness requires different outputs. Contradiction.

Parallel calls do not change the argument. The scheduler may inspect many candidate successors in advance, but until the current node is semantically interpreted it does not know which inspected candidate is the actual next link. So one load-bearing dependency revelation is still consumed per chain step. Therefore the round complexity is `Omega(L)`.

### Theorem 2: Interaction width / reopening dichotomy

Fix a partition of the raw items in `I_(k,Q,b)` into `Y_left` and `Y_right`. Suppose the set of answer profiles induced by varying `Y_left` while holding `Y_right` and the downstream query family `Q` fixed has cardinality strictly greater than `2^b`. Then no exact decomposition that is `b`-interface, no-reopen across that cut exists.

Equivalently: under that profile-count condition, any exact algorithm must do at least one of the following:

- pass an interface larger than `b` bits across the cut,
- co-load enough raw interacting material before the cut that the needed interaction is already resolved, or
- reopen the discarded raw items later.

#### Proof sketch

Assume for contradiction that such an exact `b`-interface, no-reopen decomposition exists. After the cut, the suffix of the pipeline can only see `Y_right`, the query, and the `b`-bit interface exported from `Y_left`. But there are more than `2^b` distinct downstream-relevant profiles of `Y_left`, so by the pigeonhole principle two different left states `u != v` must map to the same exported interface even though some downstream query in `Q` requires different final answers when `u` and `v` are paired with the same right state.

The suffix of the pipeline receives identical post-cut inputs in those two worlds: same `Y_right`, same query, same exported interface. Therefore it must return the same final answer in both worlds. That contradicts exactness.

So a narrow no-reopen cut is impossible whenever the downstream interaction complexity across that cut exceeds the interface capacity. This is the dense-interaction version of the [no universal distillation](./no-universal-distillation-preserves-all-task-relevant-structure.md) argument.

## Why it matters

The two theorems isolate two different reasons a workflow resists flattening.

- `A_L` says some workflows are serial because the next sub-problem is not knowable until the current one is semantically opened.
- `I_(k,Q,b)` says some workflows resist narrow decomposition because the interaction itself is the task, and exactness forbids pretending a tiny interface preserved it all.

Together they explain why parallel fan-out is sometimes a real scaling strategy and sometimes only a throughput trick around a serial core. They also sharpen the meaning of "better planning." Better planning can exploit sparse structure that already exists; it cannot remove step-dependent or high-interaction structure that the task itself imposes.

## Caveats

- The adaptive lower bound is worst-case and exact. If the system has priors, approximate objectives, or a learned pointer layer that predicts the successor well, average-case performance can be much better.
- The interaction argument depends on the downstream query family being rich enough to require the collapsed distinctions. For coarse tasks, narrow summaries may be sufficient.
- "Repeated reopening" is not necessarily wasteful if the reopened artifact is cheap to retrieve and the interaction pattern is sparse. The theorem says the cost must appear somewhere, not that every reopening-heavy strategy is bad.
- A symbolic dependency map, ontology, or interface schema can invalidate the lower bound. But those artifacts are accumulated semantic work stored in symbolic form, not free wins from orchestration alone.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — foundation: the lower bound is stated in the select/call architecture where new dependency facts enter only through bounded semantic calls
- [any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — scope: lifts the claim from one orchestration style to the full class of clean symbolic programs with LLM calls
- [exact retrieval over semantically opaque items requires linear inspection](./exact-retrieval-over-semantically-opaque-items-requires-linear.md) — parallel lower bound: opacity blocks cheap pruning; the present note shows that hidden dependency structure also blocks cheap scheduling
- [no universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md) — mechanism: dense interaction cannot be made to disappear by universally sufficient narrow summaries
- [effective context is task-relative and complexity-relative not a fixed model constant](../../notes/effective-context-is-task-relative-and-complexity-relative-not-a.md) — clarifies: the width cost is driven by interaction complexity, not just by raw token count
- [decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: the note turns "preserve interfaces needed for later synthesis" from a heuristic into a lower-bound boundary condition
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) — mechanism: clean local frames help only when the task really decomposes; they do not erase irreducible adaptive or interaction structure
