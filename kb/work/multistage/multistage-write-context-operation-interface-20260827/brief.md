# Brief: context-operation interface bounds context policy

## Governing question

How does the operation interface between retained state and active context constrain the context-management policies an agent can realize, independently of the quality of the controller operating that interface?

## Audience and reader outcome

The audience is designers and evaluators of agent runtimes, context engines, and agent-memory systems. The reader should be able to distinguish the context-operation interface from its controller or learned invocation policy; compare systems retaining similar evidence but exposing different transformations and projection boundaries; recognize that gains within a fixed interface do not validate its decomposition; and identify interface assumptions held fixed by an evaluation.

## Target and contract

- Intended target: `kb/notes/context-operation-interface-bounds-context-policy.md`
- Mode: new-write
- Collection: `kb/notes/`
- Type: `kb/types/note.md`
- Collection contribution: one transferable, truth-apt architecture claim with explanatory reach, proposition-relative scoping for named systems, and theory that remains if any one cited description is removed.
- Type shape: valid note frontmatter, a discriminating one-sentence description, a claim title with `title-as-claim`, the main mechanism near the top, and an explicit `## Scope` section for real limits. Add only contract-authorized traits and fields.
- Artifact shape: one importable central proposition. Comparisons, examples, implications, and limitations must establish or bound it rather than form independent claim clusters. Do not add `synthesis` merely because several systems are compared.

## Authoritative intended contribution

Given a retained substrate, model, and resource budget, the operations a runtime exposes—and the compositions it permits—bound which projections from retained state into active context a context policy can realize. Learning or improving the policy can improve choices within that space, but does not by itself expand, validate, or establish the optimality of the interface.

Define **context-operation interface** as the operations and allowed compositions through which a controller locates, materializes, transforms, and exposes retained state as active context.

The note must explain the mechanism: the interface defines a reachable set of projections from retained state into bounded active context, while the controller chooses within that set. It must then state the design and evaluation consequence: controller improvement is conditional evidence about that reachable set, not evidence that excluded operations were unnecessary.

This commission is authoritative. Do not replace it with a broad memory-system survey, a ranking of systems, a claim that programmable interfaces always perform better, or an external-literature novelty assessment.

## Required distinctions

- Retained substrate versus active context.
- Interface versus policy/controller.
- Operation availability versus successful activation.
- Open-ended programming versus restricted composition versus fixed memory operations.
- Model-selected, learned-controller, host/proxy-selected, and mixed push/pull projection.
- Within-run persistence, cross-restart persistence, and cross-task retained policy.
- A fixed operation set versus an invocation policy that can itself change.
- Storage fidelity versus fidelity of the projection that actually reaches the model.

Do not use “action alphabet” as a synonym. That term names world-effect capabilities and authority elsewhere in the KB. Prefer “context-operation interface”; if “alphabet” appears, explicitly distinguish the senses.

## Comparison axes

Use only axes needed to establish the central claim: retained substrate and fidelity; addressable unit; available locate, expand, transform, summarize, filter, delete, and expose operations; controller and policy learner; projection boundary; persistence horizon; and whether the operation interface or invocation policy can change. A compact table is allowed only if it advances the argument. Prefer a few discriminating contrasts over one paragraph per system.

## Source and evidence paths

Authoritative user direction:

- `kb/work/context-operation-interface-multistage-prompt.md` — source: current user commission; subject: governing question, contribution, scope, corpus, and handoffs; scope: this run; role: authoritative for intent and selection, not factual warrant for named-system claims.

Collection and type contracts:

- `kb/notes/COLLECTION.md`
- `kb/types/note.md`

Advisory navigation, not factual authority:

- `kb/reports/connect/sources/context-as-an-environment.connect.md`

Core comparison evidence, preserving each artifact's evidence tier:

- `kb/sources/context-as-an-environment.ingest.md`
- `kb/sources/prime-agent-a-self-improving-rlm-harness.ingest.md`
- `kb/agentic-systems/fractal.md`
- `kb/sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md`
- `kb/sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md`
- `kb/sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md`
- `kb/agent-memory-systems/lightweight/agemem.md`
- `kb/agent-memory-systems/reviews/virtual-context.md`
- `kb/agent-memory-systems/reviews/letta.md`
- `kb/agent-memory-systems/reviews/openviking.md`
- `kb/agent-memory-systems/reviews/playground.md`
- `kb/sources/recursive-experiential-working-memory-evolution.ingest.md`

Optional boundary cases; use only when they sharpen a necessary boundary:

- `kb/sources/the-log-is-the-agent-2065129901427130678.ingest.md`
- `kb/sources/coding-agents-are-effective-long-context-processors.ingest.md`
- `kb/sources/slate-moving-beyond-react-and-rlm.ingest.md`

Existing theory to evaluate and cite rather than duplicate:

- `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`
- `kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md`

Advisory landscape context; do not modify in this run:

- `kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`
- `kb/agent-memory-systems/systems-table.md`
- `kb/agent-memory-systems/systems.csv`

## Scope and exclusions

- Make a transferable architecture claim, not a description of Scroll.
- Do not claim that arbitrary Python is practically superior to restricted interfaces. Restricted operations may improve reliability, safety, inspectability, training, or cost.
- Do not infer interface optimality from benchmark gains inside a fixed decomposition.
- Do not call an interface unrestricted: sandbox capabilities, allowed compositions, model capability, and budgets remain bounds.
- Do not rank systems or reproduce benchmark tables.
- Do not collapse code-grounded reviews and paper- or document-grounded analyses into one evidential tier.
- Do not create a Scroll review, alter the comparison matrix, extend its schema, or write a design proposal in this run.
- Storage fidelity does not establish the fidelity of the projection that reaches the model.
- At promotion, analytical ingest summaries are not source support. Every retained named-source dependency must pass the multistage source guard against retained Quotes, with `cp-skill-ground` or the exact snapshot route used only when required.

## Known uncertainties and evidence policy

No specification gap or presently known blocking evidence gap remains. The comparison corpus is intentionally larger than the expected published evidence: reconstruction should inventory it, but disposition and drafting should retain only the few systems that do argumentative work. Omit unnecessary or unsupported system details rather than complete them plausibly. Any claim requiring unavailable support may remain an explicit limitation only if the central contribution does not depend on it.

## Reserved decisions and later work

This run produces exactly one durable note. Record, but do not execute, a Scroll code-grounded review and a possible matrix extension for operation-interface and projection-boundary axes. Any additional durable claim discovered during disposition requires a separate user-authorized run.

