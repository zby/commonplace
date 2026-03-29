---
description: Higher-level scheduling operators (semantic selection, read-time compression) as syntactic sugar over the base select/call loop, with desugarings that preserve guarantees
type: note
tags: [computational-model]
status: seedling
---

# Derived operators over the select/call loop

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) is deliberately simple: a symbolic scheduler maintains state `K`, assembles prompts via `select(K)`, and issues bounded `call(P)` invocations. The model's power comes from this simplicity — optimality arguments, decomposition heuristics, and strategy comparisons all depend on the clean symbolic/semantic separation.

But applying the model to real systems repeatedly requires the same workaround: when selection itself needs semantic judgment, you encode it as an extra loop iteration where an LLM call deposits results into `K`, then `select` reads them deterministically. The base model [already acknowledges this](./bounded-context-orchestration-model.md) as a special case. The claim here is that this pattern is general enough to deserve its own vocabulary — a surface language of **derived operators** over the base loop.

## The translation discipline

Each derived operator must satisfy one requirement: an explicit desugaring into base-model loop iterations that preserves the model's invariants:

1. **Bounded context per call** — every LLM invocation stays within `M`
2. **Explicit state** — all intermediate results pass through `K`, not hidden context
3. **Symbolic orchestration** — the scheduler decides when to call, what to call with, and what to do with results; the LLM does semantic judgment only

If the desugaring preserves these three, then any optimality argument that holds for the base loop carries through to programs written in the surface language. This is the same relationship as syntactic sugar in programming languages: you write in the richer notation, but reason about properties at the core level.

## First operators

### SELECT: semantic selection

`SELECT(K, goal)` uses an LLM call to decide what subset of `K` the next task-call should see.

Desugaring:

```
# SELECT(K, goal) desugars to:
P_sel  = select(K)    // symbolic: assemble a selection-support prompt
                      // (e.g., list of available items + goal description)
r_sel  = call(P_sel)  // LLM: return relevance judgments, priorities, or a plan
K      = K + r_sel
P_task = select(K)    // symbolic: use r_sel to build the task prompt
```

The first `select` is symbolic — it assembles the selection-support prompt from `K` using deterministic logic (list items, format the goal). The `call` does the semantic work (judge relevance, rank, plan). The second `select` is again symbolic — it reads the LLM's judgments from `K` and builds the task prompt accordingly.

This is exactly what the base model already accommodates via "two iterations (one to plan, one to act on the plan)." The operator just names the pattern.

### COMPRESS: read-time compression

`COMPRESS(K, items, consumer_goal)` produces a compressed representation of `items` tailored to a specific downstream consumer, at read time rather than write time.

Desugaring:

```
# COMPRESS(K, items, consumer_goal) desugars to:
P_comp = select(K)    // symbolic: assemble items + compression instructions
                      // shaped by consumer_goal
r_comp = call(P_comp) // LLM: produce compressed artifact
K      = K + r_comp
// r_comp is now available for subsequent select(K) to load
```

This operator makes explicit what the [session-history note](./session-history-should-not-be-the-default-next-context.md) calls "compression at the execution boundary" — but positioned at read time (when the consumer's needs are known) rather than write time (when the producer guesses at them). The raw items remain in `K`; the compressed artifact is added alongside them. Different consumers can `COMPRESS` the same items differently.

### PREPARE: multi-step selection pipeline

`PREPARE(K, pipeline)` chains multiple preparatory calls before a target call — symbolic filtering, then semantic relevance judgment, then goal-oriented compression.

Desugaring: a sequence of loop iterations, some symbolic (filtering, sorting), some via `call` (relevance judgment, compression). Each deposits results into `K`. The final `select(K)` builds the task prompt from the accumulated preparation.

This is where the surface language earns its keep most clearly. Writing the full desugaring for a three-stage preparation pipeline is verbose and obscures the intent. `PREPARE` names the intent: "get ready for the real call."

## The canonical note-selection example in surface language

The [base model](./bounded-context-orchestration-model.md) includes a worked example: given many notes that don't fit in one context window, find the relevant ones and write an analysis. The original traces seven steps through the base loop. In the surface language, the structure becomes visible:

```
K = {goal: "analyse notes", notes: [n₁ ... nₖ]}

# SELECT: which notes matter?
SELECT(K, goal)
    desugars to:
    plan    = call(select(K))        # "filter then synthesise"
    K = K + plan
    for i in 1..k:
        r_i = call(select(K))        # relevance judgment on nᵢ
        K = K + r_i
    K.relevant = filter(K, relevant)  # symbolic collection

# COMPRESS (conditional): only if relevant set exceeds M
if ||K.relevant||_synthesis > M:
    COMPRESS(K, K.relevant, "synthesis-ready summaries")
        desugars to:
        for each cluster:
            r_c = call(select(K))    # cluster summary
            K = K + r_c

# Final task call — operates on prepared context
P = select(K)    # loads relevant notes or cluster summaries
r = call(P)      # synthesis
```

Three observations:

**The architecture is named.** "SELECT, then conditionally COMPRESS, then synthesize" is the whole strategy. The base-loop version requires reading seven steps to extract this.

**Monotonicity claims become local.** Each operator carries its own cost justification. For `SELECT`: k narrow relevance calls + one focused synthesis call < one synthesis call with all k notes loaded (true when k notes exceed M; when they don't, SELECT is overhead — the operator has a precondition). For `COMPRESS`: cluster summaries + synthesis over summaries < synthesis over all relevant notes (again, only above a threshold). These conditions are checkable without re-deriving the full loop.

**The conditional COMPRESS surfaces a design decision.** In the base loop, the `if ||relevant||_synthesis ≤ M` branch is inline code. In the surface language, it's a named decision: "do I need COMPRESS?" — with a named condition: "does the relevant set exceed M for this task type?" This makes the decision portable across systems that face the same structure.

Note that `SELECT` here is composite — it includes a planning call, per-item filtering, and symbolic collection. This may warrant decomposition into finer operators (`PLAN`, `FILTER`) as the vocabulary matures. For now, the coarser operator captures the intent without premature splitting.

## What the operators dissolve

The [session-history debate](./session-history-should-not-be-the-default-next-context.md) — artifact-first loading vs. smart loading from transcripts — becomes a choice between operator configurations rather than architectural camps:

- **Artifact-first** = `COMPRESS` at write time (after execution, before storage)
- **Schema-on-read** = `COMPRESS` at read time (after retrieval, before the target call)
- **Transcript inheritance** = no `COMPRESS` at all — raw history loaded directly

All three desugar into the same base loop. They differ in *when* the compression call runs and *what* it sees, not in their formal properties. The base model's guarantees hold for all three; the choice is about engineering trade-offs (latency, compression accuracy, maintenance cost).

## The sugar problem

The analogy to syntactic sugar is precise, including the difficulty it creates. In programming languages, syntactic sugar is safe because a mechanical desugaring provably preserves semantics. Here, the desugaring is explicit and the invariants are checkable. But the deeper worry is: if every real system needs `SELECT` and `COMPRESS`, then the base model's claim that `select` is "symbolic code" becomes technically true but practically misleading. The symbolic scheduler is a thin dispatch layer over LLM-produced plans.

What survives this observation: the base model's real contribution is not that scheduling is purely symbolic — it's that the **interface between scheduling and semantic work is explicit and inspectable**. Even when an LLM call informs selection, the result passes through `K` as visible state, not as hidden context inheritance. The derived operators preserve this property by construction — every intermediate result is named, stored, and available for inspection.

This is a weaker claim than "symbolic scheduling is categorically better than LLM-mediated scheduling." But it may be the right claim. The [specification-level separation note](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) already identifies an intermediate regime where naming structure gives real gains before hardening gives reliability. The surface language lives in that regime: it names the semantic/symbolic boundary without pretending the boundary is a wall.

## Open questions

- What other operators belong in the surface language? Candidates: `BRANCH` (parallel selection with merge), `RETRY` (re-select after a failed call), `DELEGATE` (sub-loop with scoped `K`).
- Can the desugaring discipline be made formal enough to support mechanical verification? Or is "check the three invariants by inspection" the realistic ceiling?
- Does the surface language suggest a natural cost model — can you estimate token cost and call count from the operator composition without expanding to the base loop?
- When does the surface language obscure rather than clarify? If the desugaring is always trivial, the operators are just names for patterns that don't need naming.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the base model that the derived operators desugar into
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — foundation: the heuristics operate at the base-loop level; derived operators may make them easier to apply
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — dissolves: the artifact-first vs. transcript debate becomes an operator-configuration choice
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — positions: the surface language lives in the intermediate regime where naming gives gains before hardening gives reliability
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — tension: if SELECT always requires an LLM call, the scheduler is partially LLM-mediated; the desugaring discipline is what prevents full degradation
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — qualifies: the derived operators admit that selection sometimes needs semantic judgment, softening the asymmetry claim from "symbolic vs. semantic" to "explicit interface vs. hidden inheritance"
- [distillation](./definitions/distillation.md) — mechanism: COMPRESS is distillation positioned at read time rather than write time
