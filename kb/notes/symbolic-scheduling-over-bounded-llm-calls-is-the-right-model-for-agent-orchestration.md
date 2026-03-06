---
description: Agent orchestration is best modelled as an unbounded symbolic scheduler making bounded LLM calls; the scheduler chooses decompositions, prompt representations, and intermediate artifacts over an evolving external store
type: note
traits: []
areas: [computational-model, kb-design]
status: seedling
---

# Symbolic scheduling over bounded LLM calls is the right model for agent orchestration

Many agent tasks have the same surface shape as a classical bounded-working-set problem: there is a large body of material in external storage, a small working context window, and a need to schedule reads and writes so the task remains feasible. The closest intuition is a two-level I/O model or a pebbling game, though the analogy is loose.

But these classical models are not quite right. In agent orchestration, the scheduler does not only decide **what to load when**. It also decides **how to represent loaded material**, **what compressed artifacts to materialise**, and often **what subproblems to create at all**. The computation graph is not fully fixed in advance.

The result is a slightly richer model:

- an unbounded symbolic scheduler that holds state, assembles prompts, and orchestrates the workflow
- unbounded external storage of artifacts
- bounded clean context windows for each LLM call — the only expensive, stochastic operation
- optional lossy intermediate artifacts written back to storage
- a decomposition tree that is partly chosen during execution

This is closer to "I/O-like scheduling over a dynamically constructed, lossy computation graph" than to classical pebbling on a fixed DAG.

## Why the I/O analogy is still useful

The fit with the I/O model is real:

- **Context is fast memory.** Each agent call gets a bounded working set.
- **Files, notes, and logs are slow memory.** They are effectively unbounded but must be brought into context to be used by an LLM.
- **Reads and writes dominate feasibility.** Whether a task can be done depends on what can be loaded together into a single clean frame.
- **Recomputation competes with storage.** Instead of keeping a large body of material live in context, the system can write summaries, labels, or extracted claims to external storage and reload those later.

This already explains why frontloading and sub-agent isolation matter: they are the agent-system analogues of reorganising a computation so the semantically relevant material fits into one bounded call.

## Where the analogy breaks

Classical I/O models assume the computation DAG is fixed. The optimisation problem is to schedule transfers between slow and fast memory while respecting the DAG's dependencies.

Agent orchestration differs in two ways.

**1. The DAG is partly a choice.** The orchestrator may insert new nodes such as "check whether note N is relevant", "summarise cluster C", or "merge partial syntheses". These nodes are not just a schedule for an existing computation; they are a decomposition of the task into a new computation graph.

**2. Representation choice matters.** Loading the full text of six notes, loading six task-specific extracts, and loading six one-paragraph summaries are not the same state. They are different artifacts with different token cost and different usefulness to a bounded observer. In the classical I/O model, data is moved between slow and fast memory unchanged. Here, intermediate artifacts are lossy, task-shaped compressions — the scheduler chooses not just what to load but what form it should take.

Moreover, framing matters as much as selection: an instruction that says "here are six documents, synthesise them" is less useful than one that says "documents A and B establish X, documents C and D contradict it, resolve the tension." Same material, different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md). Prompt construction is part of the optimisation, not just artifact movement.

So the key decision is not only "which values should occupy fast memory?" It is also "which values should exist?"

## A minimal model

The following notation makes the structure precise; later sections use it informally.

Let:

- `K` be the scheduler's full symbolic state, including the external artifact store as one component
- `A(K)` be the external artifact store contained in scheduler state `K`
- each artifact `a ∈ A(K)` have token size `s(a)`
- `M` be the maximum context size of one agent call
- `G` be the user goal

There are two kinds of computation:

**Symbolic steps.** Deterministic procedures outside LLM context: file listing, retrieval by name, sorting, thresholding, prompt assembly, deduplication. In the simplest model these are cheap and unbounded.

**Agent calls.** Each call has:

- a task `τ`
- a selected input view `S = view(K)` derived from scheduler state
- a prompt constructor `φ`

The constructor builds the actual prompt:

`P = φ(τ, S)`

subject to the feasibility constraint:

`|P| ≤ M`

Executing the call produces one or more new artifacts `r`, which are written back to external storage.

The crucial point is that `r` need not be an exact subresult of the original task. It can be a task-shaped intermediate artifact such as:

- a relevance label
- a short rationale
- an extracted claim list
- a cluster summary
- a contradiction table
- a partial synthesis

These are not just stored values in the classical sense. They are newly materialised representations chosen because they are cheap to reload later and useful under bounded context.

Operationally, the scheduler drives a loop:

```
K₀ = initial symbolic state
for i = 1, 2, ...
    (Sᵢ, φᵢ, τᵢ) = select(G, Kᵢ₋₁)    # choose artifacts, constructor, task
    rᵢ             = call(φᵢ(τᵢ, Sᵢ))   # bounded LLM call
    Kᵢ             = absorb(Kᵢ₋₁, rᵢ)    # update symbolic state and artifacts
    if satisfied(G, Kᵢ): return
```

Each iteration the scheduler selects what to load and how to frame it, delegates a bounded LLM call, and absorbs the result into its symbolic state for use by later iterations. Some of that state is persisted as external artifacts; some may be exact metadata maintained by the scheduler itself. The `select` step is where the optimisation lives — it must choose both the input view over `K` and the prompt construction. The loop is an operational convenience; the model equally covers a recursive scheduler with an explicit stack in `K`.

## The canonical note-selection example

Suppose the task is: given many notes, find the relevant ones and write an analysis. The full set of notes does not fit in one context window.

A natural decomposition is:

1. Symbolically enumerate note names.
2. For each note `n`, run a small agent call `filter(G, n)` that reads only that note and produces a relevance artifact:
   - relevant / not relevant
   - a short rationale
   - maybe a few extracted claims
3. Write those relevance artifacts to external storage.
4. Symbolically select the notes marked relevant.
5. If the selected note bodies fit into one prompt, construct a synthesis prompt that loads them together and asks for the analysis.
6. If they do not fit, insert another layer:
   - cluster the relevant notes
   - summarise each cluster
   - synthesise over cluster summaries, with pointers back to originals when needed

This is exactly a bounded-memory schedule, but on a graph the orchestrator created.

## What is being optimised

The optimisation problem is:

Choose a decomposition, a prompt-construction strategy, and a schedule of reads and writes that maximises expected task utility while respecting the per-call bound `M`.

Even before underspecified semantics enter, there are several objective terms:

- total token traffic between storage and agent contexts
- number of agent calls
- peak prompt size
- information loss from compression
- preservation of cross-artifact interactions needed by later synthesis

This makes the problem different from ordinary knapsack-style context packing. The scheduler must trade off:

- **early filtering** against the risk of discarding something that matters later
- **aggressive summarisation** against the risk of destroying interactions needed for synthesis
- **many narrow calls** against the overhead of orchestration
- **loading raw artifacts** against **materialising task-shaped intermediate ones**

The first two are about optionality — paying context now to keep options open later. The latter two are about cost structure — choosing between representations and decompositions with different efficiency profiles. Both kinds of trade-off are present in every scheduling decision.

## General decomposition rules

Several broad rules follow from the model.

**Separate selection from joint reasoning.** First use cheap narrow calls to discover sparsity. Only then pay for wide calls that need multiple artifacts together.

**Use symbolic operations wherever exactness is available.** Retrieval, thresholding, sorting, prompt assembly, and name-based routing should be outside the LLM window whenever possible.

**Materialise reusable intermediate artifacts.** Relevance labels, extracted claims, and task-specific summaries are worth writing to external storage when they are much cheaper to reload than the originals.

**Delay expensive co-loading until interactions justify it.** Joint loading is valuable only when the task depends on relations between artifacts rather than independent judgments about them.

**Do not compress away needed interfaces.** If the final answer depends on tensions, contradictions, or alignments between sources, summaries should preserve pointers or extracted structures that keep those interactions recoverable.

**Choose representations, not just subsets.** The main optimisation variable is often not which notes to load, but whether to load bodies, extracts, summaries, or previous synthesis artifacts.

**Exploit clean frames recursively.** When the relevant set is still too large, apply the same pattern again: filter, cluster, compress, and merge in a tree rather than a flat history.

## The symbolic scheduler

The decomposition rules above assume the scheduler can perform exact bookkeeping. This raises the question of what kind of computation the scheduler itself should be.

In agent orchestration, exact bookkeeping and prompt assembly should be factored into symbolic computation rather than LLM calls. The symbolic scheduler can hold unlimited state, perform arbitrary deterministic computation, read and write files, and assemble prompts. The only thing it cannot do is semantic judgment — for that, it schedules an LLM call.

This separation is not inherited from the classical I/O model — classical models give you one algorithm operating across bounded and unbounded memory tiers, not a separate free controller. It is a design choice motivated by the nature of the two kinds of computation available in agent systems: LLMs are good at semantic judgment; they are bad at bookkeeping. The bookkeeping that recursive decomposition demands — tracking processed items, collecting results, managing the recursion stack — is exactly the wrong task for an LLM.

In practice this means the orchestrator should:

- hold accumulated state in program variables or files, not in an LLM conversation history
- use LLM calls for judgment (relevance, decomposition, synthesis) but return results to code
- assemble the next prompt symbolically from stored results, not by relying on the LLM to remember prior steps

This model also accommodates Recursive Language Models-style architectures. The LLM may emit a symbolic control program rather than a direct natural-language answer; the scheduler can read and execute that program, using it to inspect symbolic state, manipulate artifacts, and trigger further bounded LLM calls. The symbolic scheduler remains the exact stateful substrate, while the LLM supplies control decisions within it.

## Why this is the right model

This is the right model not because all current systems implement it cleanly, but because it isolates the real limiting resource. The central bottleneck in agent systems is bounded LLM context: what can be jointly loaded, attended to, and semantically processed in one call. Symbolic bookkeeping, exact state storage, and deterministic control are not the fundamental constraint and should be idealised away when asking what such systems can ultimately do.

That makes this the right optimisation problem. Given otherwise unbounded symbolic computation and storage, what can be computed with bounded LLM calls, and how should those calls be selected, decomposed, and framed to maximise capability? A system that keeps bookkeeping inside an LLM conversation is not expressing a different fundamental model; it is an inefficient implementation of this one. The clean model reveals what the most powerful system in this regime would look like: one that uses symbolic scheduling to devote bounded LLM calls only to the semantic judgments they are uniquely needed for.

## When the scheduler is LLM-mediated

The model above assumes the scheduler is a program with unbounded exact state. In practice, many current systems (Claude Code, Codex, chat-based agent loops) carry orchestration state partly in an LLM conversation. The LLM serves as both scheduler and executor — it decides what to do next based on its accumulated conversation history.

This makes the scheduler effectively bounded: it suffers the same attention dilution and compositional overhead as the sub-agent calls it is trying to orchestrate. The clean separation between unbounded scheduler and bounded LLM calls collapses.

Three responses restore the separation to increasing degrees:

1. **Compaction.** Keep summaries and conclusions rather than raw results in the conversation, applying [distillation](./distillation.md) to the scheduler's own state. This reduces degradation but does not eliminate it.

2. **Externalisation.** Write intermediate state to files and re-read selectively. This moves scheduler state out of the conversation and into unbounded storage — partially recovering the clean model.

3. **Factoring into code.** Encode the bookkeeping and recursion as a program that runs outside the LLM conversation entirely. This fully recovers the clean model. The LLM is called only for judgment steps; the scheduler is code.

Each recovery moves the system closer to the clean model — bookkeeping, recursion, and exact state management in the symbolic layer; bounded LLM calls reserved for the semantic judgments they are uniquely needed for — and the architectural direction is toward the third option.

## Open Questions

- What approximation results are possible when the graph is not fixed in advance?
- Can prompt constructors be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- Which classes of lossy intermediate artifacts preserve enough structure for later synthesis?
- When is it better to pass artifact names and let a sub-agent load them, versus constructing the full prompt symbolically in the orchestrator?
- Can the stochastic, underspecified semantics of agent calls be modelled as noisy operators on artifacts without losing the main scheduling insights?

---

Relevant Notes:
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — foundation: frontloading removes derivation procedures from bounded context by precomputing what can be known earlier
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: context is the scarce resource and has both volume and complexity dimensions
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — explains why representation choice matters: different artifacts expose different structure to a bounded observer
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: fresh sub-agent frames provide the bounded working memory assumed by the model
- [distillation](./distillation.md) — mechanism: many written-back artifacts are distillations shaped for later reload under bounded context

Topics:
- [computational-model](./computational-model.md)
- [kb-design](./kb-design.md)
