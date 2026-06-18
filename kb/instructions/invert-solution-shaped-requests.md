---
description: Use before accepting a solution-shaped request as the task; recover the underlying problem, evidence status, alternative framings, and least-committing next move.
type: kb/types/instruction.md
---

# Invert solution-shaped requests

Use this instruction when a request arrives as a proposed artifact, feature, command, validator, skill, type, workflow, or system change before the underlying problem is clear.

Treat the proposed solution as evidence of a latent problem, not as the task itself. Do not start implementing until the inversion is complete.

## When to use

Use this instruction for prompts shaped like:

- "build X"
- "add Y"
- "make a skill for Z"
- "write a validator for..."
- "create a new type"
- "maybe we need a command for..."
- "we should document..."
- "this should become a note/proposal/instruction"

Do not use it when:

- the user explicitly asks for direct implementation and the problem is already stated
- the requested change is mechanical, reversible, and already scoped
- a validated design, ADR, or accepted proposal already fixes the problem and solution
- the task is emergency repair, where diagnosis should happen inside the repair workflow

## Output contract

Produce a short report with these sections:

1. `Proposed solution`
2. `Underlying problem`
3. `Evidence status`
4. `Assumption challenges`
5. `Alternative framings`
6. `Commonplace routing`
7. `Recommended next move`

The report is complete when the underlying problem is clear enough that the next artifact choice is no longer solution-jumping.

## Steps

### 1. State the proposed solution

Restate the requested solution in one sentence.

Name the kind of surface it would add or change:

- note
- source ingest
- reference document
- proposal or ADR
- instruction
- skill
- validator, script, or command
- index or navigation surface
- code change
- no durable artifact

### 2. Recover the underlying problem

Ask: what problem would make this solution seem reasonable?

Write one concise problem statement in this shape:

```text
{actor} cannot {needed action or judgment} because {missing capability, evidence, context, constraint, or feedback}, causing {consequence}.
```

If one statement is not enough, list up to three problem hypotheses and mark the most likely one.

If the problem cannot be stated clearly, stop after the report and recommend a question or workshop, not implementation.

### 3. Classify evidence status

Choose exactly one evidence status:

- `none` -- no concrete instance, source, user need, repeated failure, or local pattern is available
- `anecdotal` -- one example or informal report exists, but no local recurrence
- `local-pattern` -- the problem has appeared more than once in this KB, codebase, workflow, or review history
- `validated` -- there is explicit local evidence, accepted design rationale, test failure, review finding, or maintained source analysis
- `contradicted` -- available evidence suggests the proposed problem framing is wrong

Name the evidence in one to three bullets. If there is no evidence, say so directly.

### 4. Challenge assumptions

Write three to five assumption checks in this exact shape:

```text
- Assumption: ...
  Risk if wrong: ...
  Cheapest validation: ...
```

Prefer validations that are local and cheap: `rg`, reading one collection contract, checking existing notes, inspecting one command, running one validator, or asking one focused user question.

### 5. Generate alternative framings

Generate three to five alternative framings. Use these defaults unless the task clearly needs different ones:

- **User/problem framing** -- what user or maintainer pain is this addressing?
- **Workflow/process framing** -- is the bottleneck sequencing, handoff, review, or decision discipline?
- **Context/routing framing** -- is the issue that agents do not load the right knowledge at the right time?
- **Validation/enforcement framing** -- is the issue that a known rule is not reliably checked or followed?
- **Artifact/type framing** -- is the issue that the current artifact shape lacks the right affordance?

For each framing, state the different solution class it would imply.

### 6. Route to the smallest sufficient Commonplace outcome

Choose exactly one route:

- `do nothing` -- the problem is not real enough, or the solution adds maintenance burden without decision value
- `ask a question` -- one missing fact determines the path
- `log` -- the observation is real but still pattern-recording
- `workshop` -- the problem needs exploratory work before library changes
- `note` -- there is a transferable claim or mechanism
- `source ingest` -- the value is mainly in preserving and analysing an external source
- `reference/proposal` -- the problem concerns a shipped-system design or proposed system change
- `instruction` -- the recurring need is a judgment-bearing procedure an agent can execute from text
- `validator/script/command` -- the rule is precise enough for deterministic enforcement or automation
- `skill` -- the procedure needs user-facing invocation, arguments, special tool permissions, model/context policy, or repeated direct use

Prefer the least-committing route that preserves learning. Treat new skills, commands, validators, types, and indexes as high-maintenance surfaces; require stronger evidence for them than for a log entry, workshop, note, or instruction.

### 7. Recommend one next move

Recommend exactly one next action.

Good recommendations are concrete:

- ask a named question
- run a named search
- inspect a named file or collection
- open a workshop with a stated question
- update a named artifact
- write a named artifact type
- defer with the reason stated

Do not give a menu. If the evidence is weak or the problem is ambiguous, recommend clarification rather than implementation.

## Verify

Before acting on the original solution, confirm:

- The problem statement is clearer than the proposed solution.
- Evidence status is explicit.
- At least one alternative framing would lead to a different solution class.
- The recommended route is the smallest sufficient outcome.
- Any implementation step follows from the problem, not from momentum behind the initial solution.

If any check fails, do not implement yet.

## Critical constraints

- Do not treat the proposed solution as accepted until the report is complete.
- Do not write durable artifacts as part of this instruction unless the user explicitly asks you to continue after the report.
- Do not force a new artifact when `do nothing`, `ask a question`, `log`, or `workshop` is the better route.
- Do not bury ambiguity by silently choosing one problem hypothesis.
- Do not include long rationale; keep the output short enough to precede real work.
