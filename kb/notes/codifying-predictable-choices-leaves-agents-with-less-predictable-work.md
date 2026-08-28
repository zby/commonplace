---
description: "Explains the negative-selection mechanism by which preferential codification changes the composition of work retained at an agent boundary"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Preferential codification concentrates less predictable work at the agent boundary

Within a fixed incoming workload and routing policy, suppose a system [codifies](./definitions/codification.md) a nonzero share of recurring decision cases and every removed case is more operationally predictable than every case left to agent judgment. The residual distribution is then concentrated at the less predictable end of the original population. This note calls that selection pattern *preferential codification*. The result is universal under the stated condition; it is not a claim that deployed systems usually satisfy the condition.

Operational predictability is system-relative. A case is more predictable here when its relevant state-to-action mapping and an acceptable result can be specified and verified more cheaply and reliably under the system's adopted comparison. The distribution counts each decision case once; it is not weighted by case duration, token use, or cost. The claim is therefore about the composition of agent work, not an aggregate increase in agent effort or intrinsic task difficulty.

## Codification moves the boundary

To codify a choice is to move it from model interpretation into code, a schema, a validator, a grammar, or another symbolic artifact that assigns consequences. A stable mapping may first be retained as theory or natural-language methodology. Those artifacts narrow later interpretation, but the model still interprets them. The choice crosses into codification only when a symbolic consumer applies the mapping without asking the agent to choose it anew.

Preferential migration changes the division of work even when the surrounding domain is deterministic. A repository can be fixed while its agent boundary retains investigation, diagnosis, synthesis, and exception handling because the economically pre-specifiable cases have already moved elsewhere. The whole system can become more predictable while the agent layer contains a larger share of cases requiring interpretation. This is a negative-selection effect, not evidence that any retained case itself became harder.

## The planning consequence depends on when information arrives

Residual work can resist pre-specification because relevant state becomes available only during execution, or because execution cheaply resolves the branch that matters while advance planning would have to elaborate many branches that never occur. Both conditions favor execution-time choice. Weak verification or uneconomical symbolic implementation can also keep a choice with an agent, but neither condition alone gives execution an advantage over advance planning.

Where execution has that advantage, a plan should fix stable intent, constraints, invariants, coordination interfaces, and acceptance evidence while leaving the affected choice of means open. The corresponding authoring rule is that [an author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md). Detailed advance planning remains appropriate when the decision-relevant state is already stable and available, the relevant branch is economical to resolve, coordination requires a shared sequence, or the choice has become predictable enough to settle.

## Self-improvement moves the frontier

Residual cases also reveal where later codification may be worthwhile. A repeated successful response is only a candidate: it still needs an adequate representation, an economical implementation, and a verifier. Verification is load-bearing because [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). When those conditions are met, migration repeats the selection process and moves the agent boundary. The residual distribution thus supplies observations for later codification without guaranteeing that any particular case will migrate.

## Scope

- New work or deliberate routing of routine cases through an LLM can offset or reverse the observed composition shift; that is why the comparison holds workload and routing fixed.
- The same case can sit on different sides of the boundary when representations, implementation cost, required reliability, or verification machinery differ.
- Concentration is not purity. Residual cases can contain deterministic substeps, and economical considerations can leave some predictable cases with agents.
- The mechanism neither predicts convergence on an agent-free system nor establishes how often deployed systems preferentially codify.

---

Relevant Notes:

- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — mechanism: separates activation and response hardening on the path from interpreted guidance to symbolic control
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: explains why a stable response still needs a verifier before it can leave agent discretion
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: develops what a self-improving system must settle to move its boundary under retained governance
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — extends: applies the same selection effect at the human cut, where the selector is warrant rather than predictability
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](./productive-deferral-requires-option-evidence-and-convergence.md) — extends: tests whether a choice identified for late resolution is being deferred productively
