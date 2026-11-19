# Documentation consolidation

Posed by the operator on 2026-11-18. Which Commonplace documentation should an agent encounter when doing a particular task, and which overviews should remain for a human operator?

## What to preserve

For agents, the operator identifies the recurring difficulty as knowing **when to inspect another part of the system**, not understanding code or prompts once found. A useful cue starts from a task the agent recognizes and names a dependency it could otherwise miss. Keep explanations of intent, constraints and rationale that the implementation cannot supply. Do not replace a useful cue with a prose copy of the implementation.

For operators, retain readable general overviews. Someone deciding whether to run a workflow should be able to tell what it does, what it may publish and when it needs a decision without tracing code or asking an agent. They may ask an agent for implementation detail; the overview needs a reliable path to that detail, not a duplicate account of it.

A [write brief](../../types/write-brief.md) is an optional experiment for a document whose purpose might be lost in consolidation. For example, if an overview deliberately leaves implementation details to an agent but must still let the operator decide whether to run the command, a brief can preserve that boundary for its next writer. Try it on one document if the title and opening do not already make the intent clear. A brief is for the writer; keep the operator’s decision guidance in the overview and the agent’s reading cues at the task entry point. Do not make briefs a prerequisite for consolidation. The [Getting started draft](./getting-started.md) is the first trial: can a reader choose a useful request without first learning the software?

## Evidence and boundaries

The workflow continuation review supplies one concrete case. To preserve an editing restriction such as “the opening only,” it was not enough to inspect the code saving unfinished plan entries. Applying approved proposals through an answers file built a plan by a different route. [Coordination between workflow runs](../../reference/workflow-architecture.md) explains why the restriction must survive. The documentation question is where an agent changing continuation would encounter a cue to inspect **both** routes. This is a starting example, not evidence that all missed dependencies need more documentation.

Use the [reference collection's economy tests](../../reference/COLLECTION.md#text-contract-and-fidelity) and the [earlier seven-case documentation study](../../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) before proposing another rule. Coordinate with [ADR routing](../adr-routing/README.md) where the missed dependency is a binding decision; do not run a parallel redesign of ADR navigation.

## What would close this workshop

For the cases examined, record the task, its ordinary starting point, what the reader needed but missed, and which passage to keep, link, move or remove. Check the proposed result from both starting points: can an agent find the consequential dependency **without being told its name**, and can an operator make the relevant decision from the overview? Fewer files or words alone does not establish either result.

Close when the operator has accepted a consolidation or a reason to keep the current arrangement, the agreed routes and overview homes are in the library, and any untested cases are identified. Opening this workshop does not authorize a repository-wide rewrite or deletion sweep.
