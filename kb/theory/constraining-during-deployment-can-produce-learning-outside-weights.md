---
description: Evaluated constraints retained during deployment can change later behavior without weight updates; persistence and successful composition require separate assessment
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, deploy-time-learning, self-improving-systems, continual-learning]
---

# Constraining during deployment can produce learning outside weights

[Constraining](./definitions/constraining.md) commits choices about what a rule permits or prefers. When deployment experience leads a system to select and retain a useful constraint, later executions can benefit without changing the model's weights. This is one path within [deployment-time adaptation through retained artifacts](./retained-artifacts-enable-persistent-deployment-time-adaptation.md).

Retention makes the change available for later use. To establish an improvement, the system must also check what the constraint changes and whether those effects serve the task. Saving an instruction or committing a validator does not by itself establish a gain in adaptive capacity.

## What a retained constraint can improve

A constraining step [can trade generality for reliability, speed, or cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) when its committed reading fits the task. The benefit depends on the change:

- Specifying a date format and timezone rule removes choices that a general date-formatting instruction leaves open. A tested implementation can then apply the rule without repeated model calls.
- Retaining house-style examples gives later sessions the same guidance. Whether the examples improve tone consistency needs comparison against the style requirement.
- Requiring a validation script at publication checks its encoded predicates on each candidate. The predicates still need to represent the intended requirements.

These changes can improve different dimensions. Faster execution, lower cost and better conformance should be assessed separately, as the [verifiability examples](./verifiability-gradient.md) illustrate.

## Persistence does not establish composition

Versioning preserves an artifact and makes rollback possible. Its benefit persists only while later executions use it under conditions where the commitment remains useful.

Two useful constraints can also conflict. A rule requiring every quotation to include a source URL can improve traceability; a separate rule forbidding URLs in public output can protect private locations. Used together on a quotation from a private source, they require a decision about applicability or precedence. Keeping both rules does not settle that decision or preserve both benefits.

Evaluate a retained change with the other rules it will encounter. Record the conditions under which it helped and revise or remove it when those conditions change. Accumulation supplies more retained commitments; successful composition is a further result to establish.

## When this counts as learning

The capacity-change account in [learning is not only about generality](./learning-is-not-only-about-generality.md) does not require weight updates. Here, deployment evidence drives a proposed constraint, evaluation selects it, and operative retention changes later behavior. The relevant capacity belongs to the deployed system, including its instructions, tools and checks.

This claim concerns that evaluated adaptation loop. An arbitrary durable edit is not evidence of improvement, and not all adaptation constrains behavior: new evidence can instead justify reopening a commitment. [Automating the judgment-heavy parts](./automating-kb-learning-is-an-open-problem.md) includes deciding what to commit, how to evaluate it and when to reconsider it.

## Scope

Constraining is one possible mechanism of learning outside weights. This note does not claim that retained constraints cover most deployment needs, reproduce the effects of weight training, or improve simply by accumulating.

---

Relevant Notes:

- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — grounds: distinguishes evidence-responsive adaptation from arbitrary durable maintenance
- [Constraining](./definitions/constraining.md) — defined-in: the commitment operation whose evaluated use this note examines
- [Constraining and extraction can trade generality for reliability, speed, or cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) — grounds: benefits depend on the committed reading fitting the task
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: capacity change can concern reliability, speed or cost
- [The verifiability gradient](./verifiability-gradient.md) — mechanism: compares checks for particular requirements without ranking artifact forms
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — extends: develops the automation problem for selecting and evaluating retained changes
