# Multistage write prompt: Context-operation interface

$cp-skill-write-multistage

Run the multistage workflow in new-write mode and produce exactly one durable KB note.

## Target

- Provisional path: `kb/notes/context-operation-interface-bounds-context-policy.md`
- Collection: `kb/notes/`
- Type: `kb/types/note.md`
- Provisional title: The context-operation interface bounds what a context policy can realize
- Produce this note first. Do not create or modify other durable artifacts except for grounding and lineage actions explicitly required by the skill. Record any additional artifact, system-review, or matrix work as a pending handoff.

## Governing question

How does the operation interface between retained state and active context constrain the context-management policies an agent can realize, independently of the quality of the controller operating that interface?

## Central contribution

Given a retained substrate, model, and resource budget, the operations a runtime exposes—and the compositions it permits—bound which projections from retained state into active context a context policy can realize. Learning or improving the policy can improve choices within that space, but does not by itself expand, validate, or establish the optimality of the interface.

This is the authoritative intended contribution. Do not replace it with a broad memory-system survey, a ranking of systems, or a claim that programmable interfaces always perform better.

## Audience and reader outcome

The audience is designers and evaluators of agent runtimes, context engines, and agent-memory systems. The reader should be able to:

- distinguish the context-operation interface from the controller or learned invocation policy;
- compare systems that retain similar evidence but expose different transformations and projection boundaries;
- recognize that policy gains inside a fixed interface do not validate the interface decomposition;
- identify which interface assumptions an evaluation holds fixed.

## Required distinctions

- Retained substrate versus active context.
- Interface versus policy/controller.
- Operation availability versus successful activation.
- Open-ended programming versus restricted composition versus fixed memory operations.
- Model-selected, learned-controller, host/proxy-selected, and mixed push/pull projection.
- Within-run persistence, cross-restart persistence, and cross-task retained policy.
- A fixed operation set versus an invocation policy that can itself change.
- Storage fidelity versus fidelity of the projection that actually reaches the model.

Define “context-operation interface” as the operations and allowed compositions through which a controller locates, materializes, transforms, and exposes retained state as active context.

Do not use “action alphabet” as a synonym. That phrase already refers elsewhere in the KB to world-effect capabilities and authority. If “alphabet” appears at all, explicitly distinguish the two senses; prefer “context-operation interface.”

## Comparison axes

Use only the axes needed to establish the central claim:

1. retained substrate and fidelity;
2. addressable unit;
3. available locate, expand, transform, summarize, filter, delete, and expose operations;
4. controller and policy learner;
5. projection boundary;
6. persistence horizon;
7. whether the operation interface or invocation policy can change.

A compact comparison table is acceptable if it advances the argument. Do not turn the note into an exhaustive catalog.

## Core evidence paths

Treat the connection report as advisory navigation, not factual authority:

- `kb/reports/connect/sources/context-as-an-environment.connect.md`

Use the following as the representative comparison corpus. Preserve each artifact’s evidence tier, and include only systems that do real argumentative work:

- `kb/sources/context-as-an-environment.ingest.md`
  - Scroll: exact event log, persistent Python namespace, model-written transformations, explicit print projection.
- `kb/sources/prime-agent-a-self-improving-rlm-harness.ingest.md`
  - Open-ended programmable context with persistent kernels, recursive sessions, and longer persistence horizons.
- `kb/agentic-systems/fractal.md`
- `kb/sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md`
  - Simpler RLM/programmatic-context family.
- `kb/sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md`
  - Restricted typed combinators rather than arbitrary Python.
- `kb/sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md`
- `kb/agent-memory-systems/lightweight/agemem.md`
  - Learned policies operating over hand-designed fixed operation sets.
- `kb/agent-memory-systems/reviews/virtual-context.md`
  - Proxy-owned assembly, layered retrieval, and paging.
- `kb/agent-memory-systems/reviews/letta.md`
  - Mixed push/pull context through core blocks, recall, archival tools, and compaction.
- `kb/agent-memory-systems/reviews/openviking.md`
  - Hierarchical filesystem operations and L0/L1/L2 disclosure.
- `kb/agent-memory-systems/reviews/playground.md`
  - Budgeted temporal-cover selection and range retrieval.
- `kb/sources/recursive-experiential-working-memory-evolution.ingest.md`
  - Verified state/event-grounded activation and an editable invocation policy.

## Optional boundary cases

Use these only if they sharpen a boundary; do not force them into the artifact:

- `kb/sources/the-log-is-the-agent-2065129901427130678.ingest.md`
  - Retention without a sufficiently specified projection policy.
- `kb/sources/coding-agents-are-effective-long-context-processors.ingest.md`
  - Generic filesystem search, slicing, and scripting as a programmable baseline.
- `kb/sources/slate-moving-beyond-react-and-rlm.ingest.md`
  - Projection through bounded sub-agent episodes rather than a memory-query interface.

## Existing theory to evaluate and cite rather than duplicate

- `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`
- `kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md`

## Landscape context, advisory rather than a required target

- `kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`
- `kb/agent-memory-systems/systems-table.md`
- `kb/agent-memory-systems/systems.csv`

The existing comparison matrix covers storage, read-back direction, targeting, trace learning, and enforcement. It does not yet encode operation interface or projection boundary. Mention that gap only if it helps motivate the claim; do not modify the matrix in this run.

## Scope and exclusions

- Make a transferable architecture claim, not a description of Scroll.
- Do not claim that arbitrary Python is practically superior to restricted interfaces. Restricted operations may improve reliability, safety, inspectability, training, or cost.
- Do not infer interface optimality from benchmark gains obtained inside a fixed decomposition.
- Do not claim that an interface is unrestricted: sandbox capabilities, allowed compositions, model capability, and budgets remain bounds.
- Do not rank the systems or reproduce their headline benchmark tables.
- Do not collapse code-grounded reviews and paper/doc-grounded analyses into one evidential tier.
- Do not create a Scroll system review, alter `systems.csv`, extend the matrix schema, or write a design proposal in this run.
- Do not perform an external-literature novelty assessment; this is ordinary named-source synthesis.
- Prefer a few discriminating contrasts over one paragraph per system.

## Grounding

Follow the multistage skill’s source-dependency guard exactly. An ingest’s analytical summary is not source support at promotion time. For every named-source claim retained in the candidate, use its Quotes section, invoke `cp-skill-ground` when required, or use the exact snapshot-required route returned by grounding. Report any quotes added. Omit claims whose support is unnecessary or unavailable rather than filling gaps plausibly.

## Artifact shape

Aim for one importable central proposition. Comparisons, examples, implications, and limitations should establish or bound that proposition rather than become independent claim clusters. Do not add the `synthesis` trait merely because several systems are compared; use it only if claim disposition establishes that the inferential composition itself requires it.

The note should explain the mechanism: the interface defines a reachable set of projections from retained state into bounded active context, while the controller chooses within that set. It should then state the design and evaluation consequence: controller improvement is conditional evidence about that reachable set, not evidence that excluded operations were unnecessary.

Validate the promoted note with `commonplace-validate`. After successful promotion, recommend `cp-skill-connect` for the new note. Leave a Scroll code-grounded review and any matrix extension as explicit later handoffs.
