# Development implications exposed by the talk

The talk suggests that Commonplace's next development should be an **observable reuse loop**. This is a workshop conclusion, not yet a roadmap commitment or library claim.

Commonplace already has strong components for writing, review, validation, and navigation. The missing layer is an end-to-end path that connects them and tests whether the resulting knowledge helps a later task:

```text
raw observation
  → explicit candidate
  → independent review + human disposition
  → note | instruction | codification candidate | reject/merge
  → fresh agent loads it for a real task
  → measured effect and new observations
```

The talk makes this gap visible because both of its worked cases had to be reconstructed manually. The [vibe-noting revision trace](../../notes/evidence/vibe-noting-trace-shows-persistence-enables-revision-not-certification.md) preserves its initiating observation, candidate prose, later corrections, and compressed retained artifact as a bounded evidence case. The tag-README case required a separate commit-by-commit trace to show how an operational strain became changed methodology and machinery. Neither path is yet an ordinary, observable Commonplace operation.

## Why this is the next gap

[`cp-skill-write`](../../instructions/cp-skill-write/SKILL.md) begins once the intended contribution is substantially determined. [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) develops a consequential artifact once a target question or purpose exists. Before that point, Commonplace has `kb/log.md`, exploratory workshops, connect observations, mechanical findings, and human initiative, but no reliable bridge from an observation into an explicit candidate. [Where change candidates come from in Commonplace](../../reference/where-change-candidates-come-from-in-commonplace.md) says that promotion from these channels still requires an unautomated triage step.

The read side has the complementary gap. Titles, descriptions, indexes, links, `rg`, and skills provide progressive routing, but [agent-memory coverage](../../reference/agent-memory-coverage.md) records that activation quality, behavioral uptake, context efficiency, and promotion economics are not first-class metrics. Commonplace can inspect whether an artifact exists and whether it passes review; it does not yet routinely test whether a fresh agent finds and uses it correctly under a context budget.

The [agent-memory gap plan](../../reference/commonplace-agent-memory-gap-plan.md) already names both needs: a candidate surface between observations and durable artifacts, followed later by activation and behavioral-uptake evaluation. The talk connects them into one round trip rather than two independent features.

## 1. Candidate-development episodes

The immediate increment should be a human-directed candidate-development workflow. Each episode should retain:

- the raw observation or source pointer;
- the proposed contribution and intended destination;
- complete candidate revisions rather than invisible in-place edits;
- review findings and their dispositions;
- human decisions that change scope, confidence, or authority;
- final disposition: promote, merge, reject, defer, or turn into a system-change candidate.

The [auditable LLM editing conclusion](../auditable-llm-editing/experiment-conclusion.md) supplies much of the internal shape: sparse explicit contracts, saved candidates, independent verification, and explicit acceptance, rejection, or merge decisions. The candidate path should reuse those results rather than inventing a parallel editing ontology.

Start workshop-local. Do not define a universal candidate schema, queue service, or automatic promotion mechanism before several real episodes show which fields and transitions recur. A candidate surface must also have expiry and disposition; otherwise it becomes a second, weakly trusted library—the failure already identified by [lifecycle management](../lifecycle-management/README.md).

## 2. A cold-session reuse assay

“Write for reuse” needs an operational test:

> Can a fresh agent discover, interpret, and correctly use the artifact without replaying the session that produced it?

For each representative task, record:

- the routing surfaces available at the start;
- the pointers followed and artifacts opened;
- relevant artifacts missed and irrelevant artifacts loaded;
- pointer and full-body context consumed;
- whether the artifact's scope and authority were interpreted correctly;
- whether using it changed the downstream task outcome.

The [description-length measurement plan](../description-length-optimization/measurement-plan.md) already measures relevant selection, irrelevant opens, pointer cost, full-body tokens, and downstream success. The reuse assay should extend that method from one pointer field to the whole navigation path.

This assay should precede another retrieval subsystem. Its results can distinguish whether a failure calls for better descriptions, routing, ranking, semantic search, situation cues, or a different artifact shape. “Load for the task” becomes measured behavior rather than an architectural preference.

## 3. A codification handoff

Candidate disposition should include a path from a semantic finding to a proposed schema, validator, instruction, test, script, or command. That handoff should require:

- a stable and precisely stated rule;
- a sufficiently strong oracle;
- a named consumer;
- evidence of the repeated cost or failure it prevents;
- tests for the deterministic behavior;
- a retained reason for choosing code rather than continued model or human judgment.

This operationalizes the tag-README lesson without attempting automatic spec mining. The [codify-versus-LLM heuristics](../../notes/codify-versus-llm-decision-heuristics.md) already supply the decision lenses. The missing part is a repeatable transition that applies them to a live candidate and records an accept, reject, or defer decision. The same record should support later relaxation if the codified rule becomes brittle.

## First experiment

Before implementing a durable surface, run one tightly scoped workshop around this question:

> Can Commonplace carry three real observations through candidate development, promotion or rejection, and cold-session reuse while retaining enough evidence to inspect every transition?

Use three different cases:

1. A new conceptual observation.
2. A substantive revision to an existing note.
3. A stable mechanical rule that might become a validator or other system-definition artifact.

At least one candidate should be rejected or merged. Otherwise the experiment demonstrates generation and retention, not evaluation. Run a fresh-context reuse task for each promoted artifact. Do not manufacture a codification case merely to fill the third slot; wait for a real checkable rule if none appears.

The experiment closes when it can answer:

- which candidate state was necessary across all three cases;
- which review and human-decision boundaries were load-bearing;
- whether the promoted artifacts were discovered and correctly used later;
- whether the context spent on routing and loading was justified by the task result;
- what, if anything, deserves promotion into a reusable skill, type, report, or command.

## Not the next work

The talk does not by itself justify:

- another review bundle—the current gap is composition of existing checks, not another lens;
- a new semantic-search backend—the read-path failure has not yet been measured end to end;
- broad automatic session-trace capture—authority, redaction, retention, and loading policy remain unresolved;
- automatic extraction or promotion—the first loop should remain human-directed;
- a comprehensive candidate schema—the workshop should discover the minimal state from use.

The development target is therefore the thin observable loop that makes Commonplace's existing components operate as one knowledge-development system. It should produce evidence before it produces infrastructure.

---

- [DSW talk outline](./outline.md) — motivates: the two worked cases and the “write for reuse; load for the task” synthesis that expose the missing round trip
- [Where change candidates come from in Commonplace](../../reference/where-change-candidates-come-from-in-commonplace.md) — rests-on: current noticing channels do not themselves promote observations into explicit candidates
- [Commonplace agent-memory gap plan](../../reference/commonplace-agent-memory-gap-plan.md) — see-also: independently proposes a candidate surface followed by activation and behavioral evaluation
- [Agent memory coverage](../../reference/agent-memory-coverage.md) — evidenced-by: current activation, context-efficiency, and behavioral-uptake gaps
- [Auditable LLM editing experiment conclusion](../auditable-llm-editing/experiment-conclusion.md) — draws-on: saved candidates, independent verification, and human-directed disposition
- [Description-length measurement plan](../description-length-optimization/measurement-plan.md) — draws-on: the existing retrieval and context-cost measurements the cold-session assay should extend
- [Lifecycle management](../lifecycle-management/README.md) — depends-on: candidate disposition and expiry must not create a shadow library
