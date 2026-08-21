# Theory-mediated learning in adaptive-system experiments

> **Status:** Exploratory Commonplace workshop. The theory-mediated additions below are our proposals, not claims made or tested by the cited systems.

Several current experiments expose different parts of a learning or improvement loop. [HCL](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) proposes, evaluates, and retains harness changes; [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) generates and filters executable learning environments; [Exo](../../agentic-systems/exo.md) exposes an inspectable, mutable substrate in which accepted self-changes can remain operative. We think each could test a missing treatment: make a scoped, criticizable theory of system behavior an explicit intermediate between evidence and the decisions made from it.

Commonplace has developed parts of this idea as [theory-mediated learning](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md): an LLM constructs or retrieves a theory and uses its consequences to guide diagnosis, candidate search, candidate selection, evidence acquisition, and outcome interpretation. The first experiments can construct a working theory inside each episode. Later experiments can ask whether [retaining and revising theories](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) improves subsequent episodes. The workshop turns that proposal into comparisons that can fail; it does not assume that the theory is correct, useful, or cheaper than direct search and full evaluation.

## Reading map

### Core proposal

- [Theory-mediated improvement loop](./theory-mediated-improvement-loop.md) — where theory enters search, selection, evaluation, and retention.
- [Selective-evaluation model](./selective-evaluation-model.md) — the costly-evidence application.
- [Experiment design](./experiment-design.md) — comparisons of direct, on-the-spot-theory, and retained-theory treatments.

### Experimental connections

- **HCL:** [reading](./hcl-reading.md) and [author invitation](./for-hcl-authors.md).
- **SPADE:** [source analysis](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) and [author invitation](./for-spade-authors.md).
- **Exo:** [case](./exo-case.md), [evidence ledger](./exo-evidence.md), and [author invitation](./for-exo-authors.md).

## Closing the workshop

Close when the proposed comparisons are precise enough to hand off or reject, and any durable conclusions have been promoted to the library or explicitly declined.
