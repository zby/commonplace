---
description: "Analysis of Will Brown's depth-1 RLM examples, which separate recursive host programs from nested language-model calls"
source: https://x.com/willccbb/status/2085469602017161229
captured: "2026-08-07T08:38:03.220556+00:00"
capture: xdk
genre: conceptual-essay
snapshot_sha256: 1bc3421afcf98bf97cc971633a17554c5cc0df033dad8b67891cfbef7551e83a
status_id: 2085469602017161229
conversation_id: 2085469602017161229
post_count: 5
ingested: "2026-08-07"
type: kb/sources/types/ingest-report.md
domains: [computational-model, orchestration, context-engineering, tool-loop]
---

# Depth-1 RLM recursion examples — ingest

## Classification

A short technical argument supported by executable-shaped pseudocode, diagrams, and implementation claims in follow-up replies
- **Author:** Will Brown (`@willccbb`); the thread presents him as speaking from experience with `prime-agent`, but this snapshot supplies no independent biography or code-level verification
- **Evidence level:** illustrative — the examples make the computational distinction concrete, but the thread includes no execution trace, implementation, benchmark, or correctness evaluation

## Summary

Brown argues that a recursive language model (RLM) can perform “true recursion” while its language-model call graph remains at depth one. The recursion lives in the host program: ordinary code repeatedly divides a problem, while each `ask` invocation is a leaf model call whose model cannot invoke another model. One example recursively summarizes document chunks and merges the summaries. Another implements quicksort with an LLM-backed semantic comparison operator. The accompanying diagram contrasts the host program's logarithmic recursion depth with the flat model-call graph.

Follow-up replies describe a related agent runtime. A parent receives a child handle immediately, the child receives a parent handle, and both can send messages into each other's context queues. These claims add an asynchronous coordination mechanism, but they are distinct from the pseudocode's narrower point: recursive control flow does not require recursively capable model calls.

## Quotes

No source quotes have been retained yet.

## Connections Found

The examples are direct evidence for [RLM has the model write ephemeral orchestrators over sub-agents](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md): the generated host program supplies the recursive control structure while model calls remain bounded leaves. They also give a compact witness for [The practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md).

Both programs are worked examples of the decomposition lemma in [Any barrier-delimited symbolic program with LLM calls is a batched select/call program](../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md). Their execution between calls is symbolic, so their recursion stacks, control locations, pending work, and partial results can be reified as machine state `K`. Each next `ask` call is the singleton batch `B = (C)`; after `R = (r)` returns, `transition(K, B, R)` can record the result and resume the computation. Semantic quicksort is the clearest witness because it changes an ordinary recursive algorithm only by substituting an LLM call for its comparison operator. The lemma preserves the program's behavior, not its correctness: an inconsistent or non-transitive model comparator remains inconsistent after conversion.

The thread sharpens the distinction already present in the [original RLM ingest](recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) and provides a useful contrast with [lambda-RLM](the-y-combinator-for-llms-solving-long-context-rot.ingest.md): unrestricted host-language recursion and typed recursive composition can produce similar recursive structures while imposing different controls. Its categorical claim that Claude Code cannot express the pattern needs scoping. The captured [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) expose a returning `agent(prompt, opts)` primitive inside model-authored JavaScript, so ordinary host-language control flow can potentially express this pattern even though saved-workflow nesting is separately limited.

## Extractable Value

1. **[quick-win] Separate recursion graphs.** Host-program call-stack depth, language-model invocation depth, saved-workflow nesting, and agent-delegation depth are different system properties. “Depth one” is ambiguous unless it names the graph being measured.
2. **[quick-win] Treat the model as an operator, not necessarily as a recursive agent.** Semantic quicksort shows that an ordinary symbolic algorithm can remain structurally recursive while outsourcing only one semantic operation to the model.
3. **[just-a-reference] Use divide-and-merge as a concrete scheduler witness.** The `answer` example makes the host language's scheduling role visible without requiring a nested model-call capability.
4. **[deep-dive] Separate invocation from result delivery.** Immediate handles and bidirectional context queues would let parent and child agents proceed asynchronously, but their usefulness depends on cancellation, ordering, failure, backpressure, and termination guarantees that the thread does not specify.
5. **[quick-win] Scope capability comparisons to the exposed control surface.** “Claude Code cannot do this” is defensible only for a surface without a returning agent-call primitive; it does not transfer automatically to dynamic-workflow variants that expose one inside JavaScript.

## Limitations (our opinion)

The thread demonstrates an idea rather than a working system. It provides no code, execution trace, cost analysis, concurrency limit, failure behavior, or evaluation of answer quality. The divide-and-merge prompt asks the model to preserve facts and disagreements, but nothing checks that merges remain faithful as the tree grows. Its pseudocode also evaluates the left and right branches sequentially even though the replies describe child agents as asynchronous, so it should not be treated as a specification of `prime-agent` scheduling.

The semantic-quicksort example assumes that model comparisons behave like a stable ordering relation. An LLM comparator can be inconsistent or non-transitive, which breaks the assumptions behind quicksort and may make the result order-dependent. More generally, calling this “true recursion” can obscure the precise result: the host program is recursive, while the language-model invocation graph is intentionally not.

The runtime statements in the replies are author claims rather than code-grounded findings. The unqualified Claude Code comparison is also time- and surface-sensitive; the local dynamic-workflows snapshot supplies a counterexample to the broad form of the claim.

## Recommended Next Action

Update [Agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) with a recursion-topology dimension that separately records host-program recursion, language-model call nesting, saved-workflow nesting, and delegation depth, using this thread as the motivating witness and Claude Code dynamic workflows as the boundary case.
