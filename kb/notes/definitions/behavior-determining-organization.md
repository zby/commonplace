---
description: "Definition — retained structure inside a declared system boundary that shapes later operation; a work product belongs when the system also retains and consumes it in that role"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Behavior-determining organization

A system's **behavior-determining organization** is the retained structure
inside its declared boundary that causally shapes how it operates on later
inputs. The term distinguishes changes to the producer from changes only to
what it delivers. Whether an artifact belongs depends on its later role, not
on whether it was originally produced as an output.

The [self-improving system](./self-improving-system.md) definition requires a
change to this organization. Such a change can alter later behaviour without
improving it; benefit relative to the declared objective needs separate
evidence.

## Scope

What counts, across representational forms and boundary types:

- **Parameters and weights** — a model's weights or a controller's gains.
- **Policies and rules** — decision procedures, routing rules, review gates,
  and acceptance criteria, including the update procedure itself.
- **Memory and retained artifacts** — notes, lessons, indexes, and caches
  that later operation consumes.
- **Workflows and procedures** — prescribed sequences, checklists, escalation
  paths, and, within a declared human-agent boundary, human procedures.
- **Code, tools, and architecture** — the executable substrate, available
  tools, and the structure connecting components.

The common test is whether changing the retained structure can change later
operation, with the new inputs and other relevant conditions held fixed.
Storage alone is insufficient: there must be a consumption path.

A work product can have a second role here. A [software
house](./software-house.md) includes the product whose evolution it remains
responsible for. Product code is delivered output, but also retained structure
that the house reads, executes, tests, and changes on later requests. A report
reused as a decision premise or a generated tool installed for later work can
likewise enter the organization. Merely labelling an output as internal does
not establish that causal role.

## Exclusions

- **Outputs with no retained internal role.** A delivered answer or compiled
  program does not change the producer merely by being good. A compiler that
  optimizes an output without changing its own later operation has improved
  that output, not itself.
- **Transient state outside the claimed horizon.** Scratch reasoning and
  intermediate results that cease to affect operation when the episode ends
  do not support a cross-episode claim. State that governs later decisions
  within an episode can belong to a system assessed over that shorter horizon.
- **External effects alone.** A thermostat changing room temperature changes
  its environment. That effect is not a change to the thermostat's retained
  control organization, even though later readings may differ.

## Misuse Cases

- Counting a persistent product patch as learning without testing whether
  experience changed capacity on later work. Retention and a changed starting
  state are not by themselves evidence of learning.
- Excluding every work product because it was first created as output.
- Excluding evaluators or update procedures when they govern later behaviour.
- Treating organization as only code or only weights rather than examining the
  declared boundary and consumption paths.

---

Relevant Notes:

- [Self-improving system](./self-improving-system.md) — defined-in: the definition whose organization-change condition this term sharpens
- [Software house](./software-house.md) — exemplifies: a producer whose maintained product lies inside its functional boundary
- [Operative change](./operative-change.md) — contrasts: whether a change takes effect is separate from whether it targets the organization
- [Behavioral authority](./behavioral-authority.md) — extends: identifies the consumer, channel, and force through which a retained artifact governs operation
- [Representational form](./representational-form.md) — extends: classifies how the organization's parts are encoded and consumed
