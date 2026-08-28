---
description: "Agent work is systematically enriched for unpredictable decisions because sufficiently predictable decisions can be moved into cheaper deterministic machinery; progressive codification therefore moves rather than removes the judgment frontier"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Agent work is selected for unpredictability because predictable decisions can be codified

LLM agents are useful for work whose relevant contingencies cannot yet be economically enumerated in advance. This is not merely because agents can tolerate uncertainty. It follows from a **selection effect**: once a recurring decision becomes predictable enough to specify reliably, the system can move that decision out of open-ended agent judgment and into a cheaper, more deterministic representation such as a workflow, schema, validator, or program. The decisions left for the agent are therefore systematically enriched for cases where the right action depends on information that is difficult to anticipate before execution.

This makes unpredictability a structural property of the **agent boundary**, not necessarily of the surrounding domain. A repository may be deterministic, a scientific dataset fixed, and a knowledge base fully stored on disk, while the agent's task remains unpredictable because the system has already automated the parts whose relevant states and responses could be specified ahead of time. The residual work is investigation, diagnosis, synthesis, exception handling, and other judgment over states not economically captured by the deterministic shell.

## Progressive codification moves the boundary

Let a body of work contain decisions with different degrees of predictability. A system can initially leave many of them to an LLM. Repeated operation can expose stable regularities, which can then be retained as methodology and, where sufficiently settled and verifiable, [codified](./definitions/codification.md) into stronger mechanisms.

The progression is not a claim that every decision eventually becomes code:

```text
open-ended judgment
        ↓ recurring regularity
explicit theory or methodology
        ↓ sufficiently settled and verifiable
instruction / schema / validator / deterministic code
```

Each successful codification removes some predictable work from the agent's discretion. The remaining agent workload is consequently a moving residual: the current frontier of decisions for which open-ended interpretation is still useful.

This yields an apparent paradox. Better automation can make the work *given to agents* less routine rather than more routine. The system automates what has become routine and keeps the agent where adaptation is still required. The absolute amount of uncertainty may fall while the agent layer remains concentrated on uncertainty.

## Why detailed advance plans are suspect at the agent boundary

The selection effect creates a temporal information asymmetry. At planning time, some consequential execution states are not known or are too costly to enumerate. During execution, the agent can inspect the actual repository, run tests, follow links, query tools, observe failures, and revise its model. The executor can therefore possess decision-relevant information that the earlier planner did not.

A detailed plan that commits in advance to choices whose premises will only become known during execution tries to pre-specify precisely the class of decisions that remained at the agent boundary because pre-specification was inadequate. This does **not** imply that detailed plans are always harmful. Advance commitment is appropriate where the relevant state is already known, coordination requires it, verification demands it, or the choice has already become predictable enough to settle.

The more general rule is:

> Commit at planning time to decisions for which planning-time information is sufficient; defer decisions whose relevant information is expected to arrive during execution.

This separates stable intent, constraints, invariants, and verification requirements from adaptive means. It also gives a first-principles reason to investigate command methodologies such as *Auftragstaktik*: their source domain reaches a similar downstream problem through a different cause. Warfare produces unpredictable execution states through opposition, friction, and changing conditions; agent systems can produce the same planner-executor information gap because predictable cases have already been selected out for codification. The transfer, if useful, rests on that shared mechanism rather than on treating agents as soldiers.

## Relation to self-improvement

In a theory-mediated self-improving system, agent judgment can generate candidates for moving the boundary. A successful response to an unpredictable case may expose a regularity; retained theory can explain it; methodology can prescribe it; verification can establish when a stronger mechanism is safe; codification can then remove that choice from future open-ended judgment.

The loop therefore has two coupled effects:

1. **The deterministic shell expands** as understood, recurring decisions are operationalized.
2. **The agent frontier moves** toward the remaining cases that still require interpretation and adaptation.

This explains why progressive codification need not converge toward an agent-free system. It can instead continually change what the agent is for. Whether the frontier eventually disappears is a separate empirical question about the domain and available representations, not a consequence of codification itself.

## Scope and falsifiers

- The claim concerns systems that actually migrate sufficiently predictable decisions out of agent discretion. A system that continues routing routine work through an LLM for convenience, uniformity, or low engineering cost weakens the selection effect.
- "Predictable" is relative to the cost and reliability of available implementation mechanisms. A decision may be theoretically specifiable but still cheaper to leave to an agent.
- Unpredictability need not come from stochastic or adversarial environments. The claim is about inability to economically determine the appropriate response before execution, including incomplete knowledge of a fixed environment.
- Agent work can contain deterministic substeps. The claim predicts enrichment, not purity: open-ended tasks commonly contain tool calls and procedures that are themselves fully specified.
- A counterexample to the planning consequence is a class of residual agent tasks where detailed planning made before execution consistently outperforms adaptive planning despite important decision-relevant information arriving only during execution. Such a result would show that execution-time epistemic advantage alone does not justify deferral.

---

Relevant Notes:

- [Codification](./definitions/codification.md) — defined-in: names the move from interpretation-dependent natural-language control into a more deterministic symbolic mechanism
- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: supplies the gradient by which stable methodological choices can acquire stronger enforcement
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — constrains: predictable behavior cannot safely migrate into autonomous deterministic machinery beyond what the system can verify
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: recurring agent judgment can move into methodology only where the resulting consequential decisions are sufficiently settled
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — complements: leaving judgment to an agent avoids enumerating contingencies in context, while codification can move stable control outside the context window entirely
- [A borrowed pattern transfers only as far as source and target share a mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md) — applies: Auftragstaktik is interesting here only insofar as both domains share the planner-executor information asymmetry, despite different sources of unpredictability
