# Connect triage candidates

Created: 2026-04-27
Triaged: 2026-04-27

Candidates below were extracted from gitignored `kb/reports/connect/*` reports. They are kept separate from `kb/log.md` so they can be triaged as a batch.

Status legend:

- `LIVE` - still looks like a real library-work candidate.
- `KEEP` - real signal, but not enough yet for immediate promotion.
- `STALE/RESOLVED` - already covered, folded into another note/review, or no longer worth carrying as a separate candidate.

## Live

- `LIVE` - **Outer-loop harness search needs archive-objective alignment in addition to oracle strength and diagnostic richness.**
  Source report: [Huxley-Godel Machine connect](./connect/sources/huxley-godel-machine-human-level-coding-agent-development.connect.md).
  Candidate action: extend the diagnostic-richness / oracle-strength cluster with the archive-selection objective axis. The HGM ingest frames this as a three-factor model: oracle strength, diagnostic access quality, and archive-selection objective.

- `LIVE` - **Externalization reframes context engineering as cognitive burden relocation.**
  Source report: [externalization unified review connect](./connect/sources/externalization-in-llm-agents-unified-review.connect.md).
  Candidate action: promote or fold a note connecting [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [deploy-time learning](../notes/deploy-time-learning-is-the-missing-middle.md), [agent runtime decomposition](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), and [skills derive from methodology](../notes/skills-derive-from-methodology-through-distillation.md). The current KB has the pieces but not this mechanism as a named frame.

- `LIVE` - **LLM memory design is a policy stack, not a storage problem.**
  Source report: [LLM memory connect](./connect/sources/everything-you-need-to-know-about-llm-memory.connect.md).
  Candidate action: synthesize write, derive, retrieve, inject, supersede, and forget policies across [agent memory is crosscutting](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [memory management policy is oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md). The requirements map covers many pieces, but the policy-stack wording is not yet owned.

- `LIVE` - **Memory evaluation has a ground-truth horizon.**
  Source report: [LLM memory connect](./connect/sources/everything-you-need-to-know-about-llm-memory.connect.md).
  Candidate action: relate memory benchmarks degrading from direct recall toward arc change, supersession, temporal correctness, and significance recognition. [Evaluate memory by effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) covers effect-based evaluation, but not this benchmark-horizon claim.

## Keep

- `KEEP` - **Skill composition depth degrades by the same mechanism as flat-context dynamic scope.**
  Source report: [Skill Graphs 2.0 connect](./connect/sources/a-new-way-to-think-about-composing-skills-to-increase-leverage-skill-g-2047124337191444844.connect.md).
  Candidate action: keep as a possible later synthesis. [Context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) now carries the Skill Graphs depth-degradation observation, but the stronger claim that hierarchical skill composition and hierarchical context scoping are the same move remains unproven.

- `KEEP` - **Service-owned memory backends need a typed-role analysis.**
  Source report: [Stash connect](./connect/agent-memory-systems/stash.connect.md).
  Candidate action: the Stash review now covers typed operational objects and links to Hindsight, SAGE, REM, SignetAI, and OpenViking, so the raw material exists. Keep only if a future comparison needs an explicit service-owned-memory table by storage substrate, extraction schema, validation gate, activation mechanism, and typed operational objects.

- `KEEP` - **Hypothesis records may be a distinct memory lifecycle.**
  Source report: [Stash connect](./connect/agent-memory-systems/stash.connect.md).
  Candidate action: the Stash review captures hypothesis lifecycle as a borrowable idea, but the KB does not yet have a general workshop/library treatment of hypothesis records. Keep until there is a concrete use case.

## Stale Or Resolved

- `STALE/RESOLVED` - **Pairwise comparison needs order-swap or Borda mitigation to function as a soft oracle.**
  Source reports: [position-bias.connect](./connect/sources/position-bias.connect.md), [Mazur thread connect](./connect/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order-new-2046661738339430489.connect.md).
  Current coverage: [pairwise-comparison hardening](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) now includes position-swapping, position-bias rate, intransitivity, round-robin aggregation, and the Mazur benchmark as evidence; [interpretation errors](../notes/interpretation-errors-are-failures-of-the-interpreter.md) also carries the 44.8% order-flip result.

- `STALE/RESOLVED` - **Context presence does not imply contextual integration.**
  Source report: [agents-explore-but-agents-ignore connect](./connect/sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.connect.md).
  Current coverage: [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) now has an explicit "context-to-action failure" section citing Agents Explore but Agents Ignore, including the AppWorld discovery-above-90% / exploitation-below-7% result.

- `STALE/RESOLVED` - **Failure memory is an operational object.**
  Source report: [Stash connect](./connect/agent-memory-systems/stash.connect.md).
  Current coverage: [Stash](../agent-memory-systems/reviews/stash.md) now has a borrowable-ideas entry for first-class failure records and compares Stash with cass-memory and other trace-derived systems.

- `STALE/RESOLVED` - **Reach predicts resistance to bitter-lessoning.**
  Source report: [Bitter Lesson connect](./connect/sources/wikipedia-bitter-lesson.connect.md).
  Current coverage: [oracle strength spectrum](../notes/oracle-strength-spectrum.md) now states the reach/oracle-strength mechanism in its open questions, and [fixed artifacts split into exact specs and proxy theories](../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) plus [first-principles reasoning](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) carry the supporting distinction. A standalone note may still be possible, but this report entry no longer needs to carry the observation.

## Routine Report-Only Flags Not Carried Forward

- Seedling/speculative target warnings where the report already says the relationship is additive.
- qmd / SQLite / local reranking failures where `rg` and index scans covered the candidate set.
- Snapshot-format caveats unless they change how a durable note should cite the source.
- "Newly created snapshot not in generated index" flags that are resolved by index refresh.
