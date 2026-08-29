---
type: kb/types/type-spec.md
name: instruction
description: Prescriptive procedure, skill body, wrapper prompt, or review gate used by agents and maintainers
schema: kb/types/instruction.schema.yaml
---

# Instruction

## Authoring Instructions

Use `instruction` for prescriptive content: procedures, skill bodies, wrapper prompts, review gates, work packets handed to sub-agents. The shared property is that the content tells an agent or maintainer what to do, not what is true.

## Frontmatter

- Set `type: kb/types/instruction.md`.
- Write `description` as the trigger condition: when an agent should use this instruction.
- Additional frontmatter is governed by the specific runtime consumer (the harness for skills, the review system for gates, etc.).

## Structure

- Title imperatively or as an action.
- Make the instruction context-complete relative to its declared consumption
  path. It may inherit Commonplace doctrine, collection and type contracts, or
  a skill only when the actual consumer receives them with binding force. Do
  not rely on the author's conversation or on a link the executor is not
  required to open. With no verified baseline, carry the needed rule directly.
- State the goal first: one sentence saying what the procedure exists to make true. It is the only rationale the body keeps; an executor holding the goal can re-route around a blocked step instead of failing on it.
- Keep the body executable on first reading.
- State prerequisites, scope boundaries, decision points, and verification checks where they matter.
- When the instruction delegates consequential work, make the packet a delta
  from the verified Commonplace doctrine. Give the task-specific purpose,
  result and acceptance, deviations, fixed choices, and choices deliberately
  left to authorized execution evidence. State owned outputs, input and
  mutation authority, coordination, verification, and return conditions where
  the inherited contracts cannot determine them. The defaults that leave
  scheduling, integration, and recovery with the parent and prohibit
  unauthorized nested delegation may be inherited when delivered; any transfer
  or exception remains explicit.
  The listed surfaces are an audit heuristic, not fields every packet repeats.
- Fix what the executor cannot safely determine from verified doctrine, the
  task commission, and authorized evidence: intent, constraints, what *done*
  means, privileged or external facts, cross-task coupling, and choices whose
  independent selection would break coordination. Leave a bounded choice to
  execution when purpose and authorized live or produced evidence permit the
  executor to select or construct it. A harmless decoupled choice can be
  irrelevant. If no inherited rule, delegated judgment, or irrelevant
  variation closes an unstated choice, treat it as a gap. A fixed live-state
  detail is an authoring-time snapshot that may go stale; a value whose inputs
  are static and remain valid may safely be resolved upstream.
- When an instruction deliberately leaves a consequential future choice coarse,
  name the evidence or observation that can discriminate, how control returns,
  who owns the next decision, and what invalidates prior work or ends retries.
  Do not add this machinery to ordinary queueing or harmless, cheap-to-reverse
  choices merely because they happen later.
- Keep rationale minimal. Put durable reasoning in `kb/notes/` and link from there.
- Prefer outcome and boundary over a prescribed sequence when several means can
  satisfy the goal and execution evidence can discriminate among them. Fix an
  exact command, ordering, output grammar, or handoff protocol when a machine
  interface, irreversible mutation, isolation requirement, or coordination
  dependency makes that exactness load-bearing.

## Operativity

An instruction changes system behavior only through a path: something consumes it, over some channel, with some force. Before writing or editing one, name that path — what loads this text (harness skill selection, a collection contract, a link from another instruction, a human invoking it) and when it fires. An instruction nothing loads is inert: it persists, stays true, and changes nothing — and it fails silently, because no consumer means no error either.

The same path defines what the instruction may omit as inherited. When a packet
depends on an upstream contract by omitting one of its rules, a change to that
contract reopens the packet. Record narrow dependencies through source-side
lineage. Treat a change to universal root, collection, or type doctrine as
recommissioning the whole class of instructions that emits worker packets
under that baseline. Freeze and search that cohort, then review it before a
dependent packet relies on the changed rule as an omission source.

- For link- and search-mediated consumers, the `description` is the retrieval wire: write it to match the query an agent would issue at the moment the instruction should fire, not the vocabulary of the instruction's own content.
- If the instruction should fire on a condition (a kind of change, a kind of artifact), check that a surface loaded in that situation actually routes here. If nothing does, add the route or record the gap — do not assume discovery.

## Template

```markdown
---
description: "{When to use this instruction}"
type: kb/types/instruction.md
---

# {Imperative title}

{Goal: one sentence on what this procedure exists to make true.}

{What this instruction does and when to use it. Body sections follow the
shape that fits the work.}
```

---

Relevant Notes:

- [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) - rationale for the detail-level rule: which details to fix and which to leave to the executor
- [Operative change](../notes/definitions/operative-change.md) - rationale for the operativity rule: a change operates only through a consumer, channel, and force over a declared horizon
- [A retrieval miss is a local reflective-path failure](../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) - rationale for the description and routing rules: retrieval is the wire a retained instruction acts along, and it is best-effort unless a loaded surface enumerates the route
- [Intent-framed delegation is a control regime; prompt length does not establish it](../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) - rationale for the consequential-worker handoff and retained-parent-control rule
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../notes/productive-deferral-requires-option-evidence-and-convergence.md) - rationale for the return and convergence rule on intentionally coarse consequential choices
