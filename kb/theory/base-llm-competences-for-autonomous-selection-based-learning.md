---
description: "Working hypothesis: harness code can supply much of an autonomous selection-based learning loop, leaving three conjectured semantic competences on the frozen base LLM"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# Harness code may offload much of a selection loop, leaving three base LLM competences

**Working hypothesis.** Holding model weights fixed while updating a store of procedures, hypotheses, and code does not remove dependence on the base model's weights. Yet an autonomous [selection-based learning](./definitions/selection-based-learning.md) loop does not need the frozen LLM to perform every loop function on its own. Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), harness code can take over much of the loop's machinery:

- **Enforcement and context assembly:** running codified validators and schemas, routing and loading the relevant artifacts, and enforcing token budgets.
- **Evidence capture and replay:** recording which artifacts loaded during a run, annotating telemetry coverage gaps, replaying past cases, and running targeted ablations or bisects.
- **Store bookkeeping:** tracking unused or stale entries, flagging rising failure rates, scheduling periodic reviews, and executing rollbacks.

Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head. Harness code can relocate mechanical and structural work, yet [semantic work can be relocated without being eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md). In open-ended work where new failure modes, commitments, and remedies keep arriving, our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM:

1. **Interpreting unformalized text into action.** The model must read natural-language procedures, hypotheses, and constraints that have not yet been codified into code and let them govern its behavior under realistic context loads ([operative change](./definitions/operative-change.md)).
2. **Diagnosing novel failures and synthesizing candidates across text and code.** It must turn an unanticipated failure and its trace into a causal diagnosis and propose novel remedies—new procedures, testable hypotheses, checks, or executable harness code ([diagnostic richness](./diagnostic-richness-constrains-outer-loop-learning-quality.md)).
3. **Judging unformalized trade-offs and recognizing missing evidence.** It must weigh competing consequences against stated commitments where no fixed check settles the choice, keep genuinely contested or under-evidenced comparisons open, and recognize when an existing check is misleading ([on-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md)).

Under this split, store-level maintenance and [criterion revision](./definitions/single-loop-and-double-loop-learning.md) do not require a separate model competence. Detecting bloat, stale entries, or rising regressions belongs to harness code; spotting semantic conflicts between prose rules, refactoring them into a cleaner abstraction, or proposing a revised check reduces to competences 2 and 3 applied to the store and its criteria.

These three competences can fail independently and sit at different capability thresholds. A model may follow clear prose procedures while still misdiagnosing noisy traces or overclaiming certainty on incomplete records. Separating them lets a human-assisted bootstrap identify which competence currently binds: people temporarily supply the missing semantic step while transfer tests check each kind of decision on its own.

A bounded empirical illustration of a base-model floor appears in [Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md), where the three weakest tested models produced no held-out gains under the same harness-evolution loop that improved stronger models. Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates.

## Scope

- This split is a **working hypothesis**, not an established impossibility result. Any sub-task shown to be reliably offloadable to harness code moves out of the LLM column, and concrete bottlenecks discovered in practice can add to it.
- Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning.

## Open Questions

- Which of the three competences binds first on current frontier models in real software and knowledge-base maintenance?
- How far can better harness interfaces—such as structured replay harnesses, dependency graphs, and explicit coverage annotations—lower the base-model floor required for competences 2 and 3?

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: the loop whose autonomous operation sets these prerequisites
- [Scheduler–LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: why bookkeeping, replay, and enforceable checks belong in harness code while semantic interpretation stays on the model
- [Semantic work can be relocated, not eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md) — grounds: why harness offloading narrows the base-LLM floor without eliminating it
- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — extends: develops competence 3 and how to test an LLM selector
- [Single-loop and double-loop learning](./definitions/single-loop-and-double-loop-learning.md) — defined-in: criterion revision, treated here as competences 2 and 3 applied to working checks
- [Operative change](./definitions/operative-change.md) — defined-in: why loading a prose procedure without behavioral dependence fails competence 1
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — extends: how the harness's evidence interface interacts with competence 2
- [Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md) — evidenced-by: weak-model lines produced no held-out harness gains under a loop that lifted stronger models (bounded to one benchmark and loop)
