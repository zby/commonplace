---
description: For runtimes composed of bounded model calls, separating control progression, per-call context, and external state or action services localizes failures even when one implementation owns all three
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [computational-model, architecture]
---

# Agent-runtime analysis should separate scheduling, context assembly, and external state

Practitioner accounts often call all the machinery around a model a harness or runtime. That perimeter is useful, but it is too broad for diagnosis. For runtimes organized as repeated **bounded model calls**—individual invocations with finite input windows—analysis should separate three responsibilities:

- **Scheduling** owns control progression: whether, why, and when another call or action occurs, and how run state advances. It asks: *what happens next?*
- **Context assembly** selects and frames the instructions and information supplied to a chosen model call. It asks: *what does this call receive?*
- **External state and action services** preserve exact state, execute operations, and enforce environmental boundaries outside the model. They ask: *what persists or acts outside the call?*

These are analytical responsibilities, not mandatory module boundaries. A scheduler may specify a call's objective and budget, a context engine may assemble its input, and external services may supply retained state or perform the resulting action. One implementation can own all three. One facility can also span them: retrieval logic selects context, while external storage retains the retrieved artifacts. The separation follows the decisions being made, not the number of components in the implementation.

## Why the separation helps

The three questions route failures to different repair surfaces. A wrong next step points to scheduling. Missing or badly framed evidence points to context assembly. Corrupted retained state, a failed command, or a boundary violation points to external services. Calling each one a “harness failure” does not locate the remedy.

The separation also prevents category errors. A filesystem does not decide what happens next. Executing a tool changes or queries the environment; selecting that tool's schema for a call shapes context. Likewise, retaining a complete transcript is a different decision from selecting excerpts to load. These causal roles remain distinct even when one process implements every responsibility.

## Worked practitioner mappings

Two practitioner accounts illustrate how this diagnostic cut reclassifies features originally presented at the broader harness perimeter. Neither source proposes the three-part split; the mappings below are this note's analysis.

The [Anatomy of an Agent Harness ingest](https://x.com/Vtrivedy10/status/2031408954517971368) derives six features from model limitations:

| Practitioner feature | Concern | Diagnostic reason |
|---|---|---|
| Long-horizon execution / Ralph Loop | Scheduling | Controls iteration, retry, and progression across calls |
| Context management | Context assembly | Compacts, scopes, and injects what a call receives |
| Memory/search | Context assembly + external state | Retrieval selects call-visible material; storage retains it |
| Filesystem | External state | Preserves durable exact state outside the model |
| Bash / tool execution | External actions | Performs deterministic operations in the environment |
| Sandbox / isolated environment | External boundaries | Constrains execution and protects the surrounding system |

The mixed memory/search row exposes two decisions hidden by the single word “memory”: retrieval governs activation, while storage governs retention.

[Raschka (2026)](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) offers a second six-feature account of coding-agent harnesses:

| Raschka feature | Concern | Diagnostic reason |
|---|---|---|
| Live Repo Context | Context assembly + external state | Workspace state is retained externally, then selected for the first call |
| Prompt Shape and Cache Reuse | Context assembly | Separates stable and variable parts of the call input |
| Context Bloat Minimization | Context assembly | Clips and compresses accumulated call-visible material |
| Structured Session Memory | Context assembly + external state | Selects working state from a retained transcript |
| Tool Access | Context assembly + external actions | Tool descriptions enter context; tool execution changes or queries the environment |
| Bounded Subagents | Scheduling + context assembly + external boundaries | Delegation chooses another call, scopes its input, and limits its authority |

Raschka's observation that apparent model quality can come from context quality specifically supports the importance of context assembly. His other features remain diagnosable through the same three questions, including cases in which one feature crosses responsibilities.

## Relation to existing KB theory

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) is a broader computational abstraction. Its scheduler's `select` operation includes retrieval, prompt assembly, and framing, while its explicit state supports progression across calls. This note makes a narrower diagnostic cut within that abstraction: choosing the next operation and assembling the chosen call's input can fail separately even when one scheduler performs both.

[Context engineering](./definitions/context-engineering.md) is also broader than a runtime component. Its operational core—routing, loading, scoping, and maintaining bounded context—supplies the context-assembly responsibility here. Its wider questions about storage shape, session boundaries, and interfaces can cross the other two.

The external-state concern is supported by [inspectable artifacts](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md): exact state outside the model can be diffed, tested, reviewed, and reverted. Files are one useful implementation because [files can defer schema commitment](./files-defer-centralized-schema-commitment-until-invariants-stabilize.md), but repositories and shell commands are coding-agent examples, not requirements. Other runtimes may use databases, object stores, remote executors, or policy services.

## What the mappings establish

The mappings show that the three questions can re-express features from two practitioner accounts and expose responsibilities hidden inside compound features. Because the features were coded retrospectively against the proposed split, they do not establish independent convergence, exhaustiveness, or a unique causal link between model limitations and these boundaries. A convergence claim would require a declared coding rule, a broader sample, and reported ambiguous cases.

Evaluation, governance, observability, and social workflow may require additional axes. External state and action services may also need a finer split when storage, tool, and permission failures must be compared separately. These three questions are a starting point for locating responsibility, not a final module graph.

---

Relevant Notes:

- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: once a failure is located, explains how soft guidance can harden at different runtime surfaces
