# Workshop: Input-vs-Output-Driven Memory Design

## Question

When designing a memory system, do you start from the **input stream** (observe what flows in, decide what's worth keeping) or from the **output requirement** (specify what the system needs to serve, work backwards to elicitation)?

## Working position

This KB is predominantly **output-driven**. The Goals section in `CLAUDE.md` (purpose, domain, include/exclude, quality bar) is effectively an output spec: it defines what the KB should serve, which then becomes the criterion for whether any given observation is worth capturing.

The reason is that **"what to store" is not easy to answer from inputs alone**. Without a target, every conversation looks potentially worth keeping, or potentially not — there is no criterion for inclusion. The observer has nothing to measure against.

## The two approaches

| | Input-driven | Output-driven |
|---|---|---|
| Starting point | The incoming stream | The intended consumer / use case |
| Default operation | Observe, filter, retain | Declare need, elicit, fill |
| Strength | Cheap; runs in the background | Explicit coverage; visible gaps |
| Weakness | Invisible gaps; drift without a target | Requires articulated goals; needs active elicitation |
| Typical failure | Accumulates whatever happens to come up | Breaks when goals drift or go stale |

## Where this KB expresses the output-driven stance

- **Goals in `CLAUDE.md`** — purpose/domain/include/exclude define what the KB is for before any note gets written.
- **`cp-skill-write`** starts from a *type* and a *topic* (what artifact is needed), not from a transcript to mine.
- **`COLLECTION.md` files** per collection codify the output spec at the register level (theoretical/descriptive/prescriptive).
- **Ingestion is the one input-driven entry point**, and even it routes through classification against the existing output structure.
- **Claude Code's auto-memory system** (in this repo's `.claude/projects/.../memory/`) is input-driven by contrast — it watches the conversation and applies heuristics. The tradeoff is visible: gaps are invisible, coverage of the user-profile category is whatever happens to have come up.

## Working hypotheses

- Output-driven design is the harder path because it requires goals to be articulated upfront and kept current. Input-driven systems can run with a vague purpose.
- The two approaches are not mutually exclusive. A mature system probably runs input-driven capture in the background and uses output-driven audits to detect missing categories and trigger targeted elicitation.
- "What to store" being hard to answer is domain-dependent: in narrow domains (e.g., bug reports) the input itself constrains what matters; in open domains (methodology, preferences, goals) the output spec has to do the work.

## Open threads

1. What does output-driven *elicitation* look like in practice — does the system ask questions, or does the operator write the spec and the system passively fills it?
2. How does the output spec itself get maintained? If goals drift, the whole criterion drifts with them — who audits the Goals section, and how often?
3. Where does input-driven make sense even in this KB? (Log entries? First-occurrence observations that haven't yet been understood as mechanisms?)
4. Does the output-driven stance break down at the boundary where the KB's purpose is itself uncertain or exploratory?
5. Relationship to the [agent-memory-design workshop](../agent-memory-design/README.md): that workshop asks *what architecture* makes store-everything + selective-loading work. This workshop is upstream — it asks *whether you should be storing everything in the first place*, or only what the output spec calls for.

## Graduated artifacts

- [distillation-is-transformation-not-selection](../../notes/distillation-is-transformation-not-selection.md) — the shape-change claim graduated to `kb/notes/`. Distillation produces artifacts of a different kind (preferences, ADRs, rules, skills); it is not lossy selection from the trace. The question *into what shape?* — which is where this workshop's output-driven framing would enter — remains open and has not been graduated.

## Possible graduation

If the analysis holds up, the extractable claim for `kb/notes/` is something like: *"Output-driven memory design is preferable when 'what to store' is hard to answer; the Goals section functions as the output spec that makes inclusion decisions possible."* This would sit alongside existing context-engineering theory.
