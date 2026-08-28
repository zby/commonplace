---
description: "Distinguishes unpredictability in residual agent work from uncertainty in the surrounding domain, then derives planning and self-improvement consequences"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Codifying predictable choices leaves agents with less predictable work

When a system [codifies](./definitions/codification.md) a recurring choice previously assigned to an agent, it moves that choice into a symbolic control whose consequences are assigned by a formal consumer. The core claim is conditional: when a system preferentially codifies choices that are more predictable than the choices it leaves to agents, the residual agent workload becomes less predictable. Here, *predictable* means that the relevant state-to-action mapping and an acceptable result can be specified and verified cheaply and reliably enough to replace open-ended judgment.

This is a selection effect. It does not require the surrounding domain to be stochastic. A repository can be deterministic, a dataset fixed, and a knowledge base fully stored on disk while an agent's task remains unpredictable in this operational sense. The system may already have extracted the decisions whose responses could be fixed economically in advance, leaving investigation, diagnosis, synthesis, and exception handling at the agent boundary.

## Codification moves the boundary

Repeated operation can expose a stable mapping between a situation and a response. The system may first retain that regularity as theory or natural-language methodology. Those artifacts narrow later interpretation, but they remain interpreted. The choice crosses into codification only when a schema, validator, program, or other symbolic artifact gives it formally assigned consequences.

```text
open-ended judgment
        ↓ repeated cases expose a stable mapping
explicit theory or natural-language methodology
        ↓ trigger, response, and verification become settled
schema / validator / program / other symbolic control
```

Each successful migration changes the division of work. It can lower uncertainty across the whole system while increasing the share of hard-to-pre-specify decisions within the agent layer. Better automation can therefore make the work assigned to agents less routine even as the system becomes more predictable overall.

## The planning consequence depends on when information arrives

Residual work can resist pre-specification for several reasons: relevant facts may arrive only during execution, the contingency space may be too expensive to enumerate, verification may be weak, or implementation may cost more than continued agent judgment. Only the first two reasons necessarily give the executor an information advantage over an earlier planner.

For those cases, a detailed plan is brittle when it commits to actions whose premises are not yet available. During execution, the agent can inspect the actual state, run tests, follow links, observe failures, and revise its model. The practical rule is to commit early to stable intent, constraints, invariants, coordination points, and verification requirements, while deferring a choice when its decision-relevant information is expected to arrive during execution.

Detailed advance planning remains appropriate when the relevant state is already known, coordination requires a shared sequence, verification demands an explicit procedure, or the choice has become predictable enough to settle. The selection effect supports adaptive planning only where execution changes the available evidence.

## Self-improvement moves the frontier

An unfamiliar case can supply the observation that starts the next migration. Repeated successful responses expose a regularity; retained theory explains it; methodology narrows the admissible response; verification establishes whether a symbolic control is safe; codification then removes that choice from future open-ended judgment. Verification is load-bearing because [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

This loop expands the symbolic control surface and moves the agent frontier toward the cases that still require interpretation. Retained methodology can govern the transition only insofar as [it settles the meta-decisions that its own extension raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). Progressive codification therefore need not converge on an agent-free system. The frontier may shrink, stabilize, or move as new work arrives and available representations, costs, and verification methods change.

## Scope

- The claim compares work before and after selective migration under a fixed incoming workload and routing policy. New work or deliberate routing of routine tasks through an LLM can offset or reverse the observed shift.
- Predictability is relative to the available representations, implementation cost, required reliability, and verification machinery. The same choice can sit on different sides of the boundary in different systems.
- The claim predicts enrichment, not purity. Residual agent tasks can contain deterministic substeps, and some predictable work may remain with agents because moving it is not economical.
- Natural-language instructions and methodology can constrain choices without codifying them. This note reserves *codification* for the move into a symbolic artifact with formally assigned consequences.
- The mechanism does not establish how often real systems satisfy its selection condition. Evidence that deployed systems usually retain predictable choices in agent discretion, or codify without favoring predictable choices, would defeat a prevalence claim built from this mechanism.

---

Relevant Notes:

- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — mechanism: separates activation and response hardening on the path from interpreted guidance to symbolic control
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: explains why a stable response still needs a verifier before it can leave agent discretion
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: develops what a self-improving system must settle to move its boundary under retained governance
