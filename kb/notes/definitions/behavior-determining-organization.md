---
description: "Definition — the retained structure that shapes how a system will operate: parameters, policies, memory, rules, workflows, tools, code, architecture, evaluators; outputs and environment excluded"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Behavior-determining organization

A system's **behavior-determining organization** is the retained structure that causally shapes how the system will operate on future inputs — as opposed to the outputs it produces and the environment it acts on. It is what the [self-improving system](./self-improving-system.md) definition requires the change to land *in*: change the organization and later behavior changes; change only an output and nothing about the system has improved.

## Scope

What counts, across representational forms and boundary types:

- **parameters and weights** — a model's weights, a controller's gains, a step-mechanism's setting;
- **policies and rules** — decision procedures, routing rules, review gates, acceptance criteria (the evaluator is itself organization, which is what makes improving the improvement process a self-change like any other);
- **memory and retained artifacts** — notes, lessons, indexes, and caches that later runs load and act on;
- **workflows and procedures** — prescribed sequences, checklists, escalation paths, and, in a declared socio-technical boundary, organizational procedures;
- **code, tools, and architecture** — the executable substrate, the tool surface, and the structure connecting components.

The common test: would the change still make a difference to behavior on an input the system has not seen yet? Retained structure passes; a produced answer does not.

## Exclusions

- **Work products.** An answer, a patch to someone else's codebase, a compiled program, a report — outputs the system makes for the world. A compiler that optimizes programs improves its outputs, not its organization. Refining the current answer, however many iterations it takes, changes a work product.
- **Transient episode state.** Scratch reasoning, context contents, and intermediate results that determine nothing once the episode ends. (Where episode-scoped structure does govern the rest of a declared horizon, whether the change counts is an [operativity](./operative-change.md) question, not an organization one.)
- **The environment.** A thermostat switching the heater changes the world, not itself — first-order control output, Ashby's regulation.

## Misuse Cases

- Counting output generation as self-improvement because the output was good — the improvement has to be in what the system *is*, not in what it just made.
- Excluding the evaluator or the improvement procedure from the organization — acceptance criteria and update rules are retained structure and can themselves be the object of improvement.
- Treating "organization" as only code or only weights — the term deliberately spans every representational form a behavior-bearing structure can take.

---

Relevant Notes:

- [Self-improving system](./self-improving-system.md) — defined-in: the definition whose "its own organization" clause this term sharpens
- [Operative change](./operative-change.md) — contrasts: whether a change to the organization *takes effect* is a separate question from whether it targeted the organization at all
- [Behavioral authority](./behavioral-authority.md) — extends: the consumer, channel, and force through which retained structure actually determines behavior
- [Representational form](./representational-form.md) — extends: the prose/symbolic/distributed-parametric axis the organization's components span
