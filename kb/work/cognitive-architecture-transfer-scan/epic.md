# EPIC: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium-high

## Remembered model

EPIC, remembered as Executive-Process/Interactive Control, models human performance through interacting perceptual, cognitive, and motor processors. Perceptual and motor activities can proceed in parallel, while an executive strategy expressed through production rules coordinates them. Components have distinct timing and concurrency constraints, allowing the architecture to model multitasking and human-computer interaction without treating all task time as serial thinking.

The transferable lesson is that end-to-end behavior depends on **resource scheduling across heterogeneous channels**. A slow workflow may be bottlenecked by orchestration, observation, or action even when the core reasoning step is cheap.

## Provisional ontology

- **Processor:** a component responsible for a class of perception, cognition, or action.
- **Store/interface:** the state through which processors exchange information.
- **Production/executive rule:** a condition-triggered coordination decision.
- **Task strategy:** the chosen scheduling and control arrangement, distinct from fixed component abilities.
- **Parallel activity:** operations that can overlap without sharing a bottleneck.
- **Serial bottleneck:** a resource or dependency that forces ordering.
- **Timing prediction:** a consequence derived from component and strategy interactions.

For an agentic workflow, analogous resources might include model judgment, filesystem search, network requests, tool execution, human approval, and write verification. The mapping is functional, not psychological.

## Transfer candidates

- **`EPIC-1` — model tools and judgment as separate resources.** Do not attribute elapsed time or failure to "reasoning" when the actual bottleneck is sequential I/O, approval latency, context reintegration, or a shared executor.
- **`EPIC-2` — treat orchestration policy as an independent design lever.** The same components can perform differently under a different ordering, prefetch, batching, or overlap strategy. Compare strategies before replacing components.
- **`EPIC-3` — derive concurrency from dependencies.** Parallelize operations whose inputs are already fixed; keep adaptive dependencies sequential. This turns parallelism from a slogan into a task graph.
- **`EPIC-4` — predict an execution trace before benchmarking.** State which operations should overlap, where the bottleneck should appear, and how a perturbation should shift it. Wall-clock measurements then test an architectural claim.
- **`EPIC-5` — distinguish process structure from result structure.** A well-formatted output does not reveal whether work was scheduled effectively, matching the existing [process/output separation](../../notes/process-structure-and-output-structure-are-independent-levers.md).

## Method worth borrowing

EPIC's model-based HCI stance suggests parameterized task traces. Represent the workflow as processors, queues, dependencies, and executive rules; predict completion ordering and resource occupancy; then compare with logs. The value is not high-fidelity human timing but locating the causal bottleneck and evaluating alternative orchestration policies.

## Non-transfer and failure modes

- Human perceptual and motor timing constants do not transfer to tools or model calls.
- Overly detailed simulation can cost more than the scheduling decision warrants.
- Apparent parallel resources may contend for the same model context, rate limit, filesystem state, or human attention.
- A faster executive strategy can reduce verification quality; latency is only one outcome.

## Grounding questions

1. Which processors can truly overlap in canonical EPIC, and what central bottlenecks remain?
2. How are task strategies represented and compared?
3. Which HCI predictions depended on architecture rather than fitted parameters?
4. What is the exact expansion and scope of the EPIC name?
