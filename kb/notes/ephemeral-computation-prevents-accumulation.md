---
description: "Discarding an intermediate artifact loses that artifact's reuse path, not all learning; cross-run accumulation fails only when no experience-dependent state survives to affect later work"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis]
---

# Discarding all experience-dependent state prevents cross-run accumulation

An ephemeral computation generates an artifact, uses it, and discards it.
That removes one path for later reuse. It prevents learning across runs only
when nothing learned from the episode survives elsewhere and affects later
work. The boundary is the [deployed
system](./the-deployed-system-not-the-model-is-the-unit-of-learning.md), not
one generated file.

## What must survive

Consider two runs with the same new inputs, fixed models, machinery, and
sampling rules. If no state carrying the first run's experience reaches the
second, that experience cannot change the second run's behaviour. The state
could have been retained as code, a theory, examples, test results, a policy,
or model parameters where those are writable. An external record later read
by the system is also a possible path; it must be included in the account.

A generated script can therefore disappear while learning persists. The house
may keep the failure it exposed, a corrected dependency account, or a test for
later scripts. Conversely, retaining every script establishes storage, not
learning: unused files may change nothing.

```text
artifact discarded + no retained effect       -> no cross-run accumulation
artifact discarded + retained useful lesson  -> learning remains possible
artifact retained + no later causal use      -> storage alone
```

## What discarding saves and costs

Discarding a generated artifact avoids maintaining that particular reusable
object: version compatibility, stale assumptions, dependencies, and retrieval
need not be managed for it. Reuse instead requires regeneration or a different
retained carrier. Which route is cheaper depends on repeated construction cost,
validation cost, and the value of preserving what was learned.

Testing and review can happen before disposal. A temporary program can be
checked against a retained test suite, inspected before execution, and leave a
record of its result. What disposal removes is the ability to inspect or rerun
those exact bytes later, unless another record preserves them. Independent
regeneration need not reproduce the same program.

Ephemerality also does not imply safety or purity. Temporary code can consume
resources, expose data, or change persistent state. Even a pure computation's
output may guide a consequential decision. Approval, isolation, and result
checking depend on those effects, not on whether the generated file survives.

Kirsch's [critique of ephemeral software](https://www.blackhc.net/essays/future_of_software/)
identifies production knowledge that must survive replacement: discovered edge
cases, integration constraints, interface expectations, and audit-relevant
decisions. That motivates retaining the knowledge; it does not require every
version of the code to be its sole carrier.

## Retention and codification are different choices

[Codification](./definitions/codification.md) assigns an operation to a symbolic
consumer. Retention determines whether an artifact or its effects remain
available later. A generated program is symbolic while it runs even when it is
deleted afterward. A retained natural-language procedure accumulates knowledge
without becoming executable code.

A house can combine both choices: keep a theory and examples, generate a
short-lived implementation, test it, then retain the result that matters.
Alternatively it can install a reusable implementation. The
[codification–relaxing account](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
addresses when to move operations between interpretation and assigned
execution; it should not be read as a binary choice between learning and
forgetting.

## Scope

The no-accumulation conclusion assumes no experience-dependent causal path
into the later run. Changed inputs, persistent environment state, retained
records, and parameter updates can each defeat that assumption. Improvement
within one episode is also possible without cross-run retention. The relevant
question is what survives the horizon across which learning is claimed.

---

Relevant Notes:

- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: sets the boundary over which retained effects must be checked
- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — extends: describes one useful retention path
- [Codification](./definitions/codification.md) — contrasts: execution form is separate from artifact lifetime
- [Discarding software requires preserving the operational knowledge later work needs](./ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — extends: asks which knowledge must survive regeneration
- [The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/) — evidenced-by: supplies the production-knowledge pressures motivating durable carriers
