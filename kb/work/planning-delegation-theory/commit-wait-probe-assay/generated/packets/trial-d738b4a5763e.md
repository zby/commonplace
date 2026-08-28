# Planning assay packet trial-d738b4a5763e

Use only this packet. Do not inspect other repository files, run searches, read
links from the instruction, or use conversation history. Do not delegate or
spawn another agent. Treat the case as complete and each stated fact as true.

Apply the operative instruction to the case, but write only the JSON response
specified below. Choose the recommendation the instruction warrants; do not
maximize deferral, option analysis, or detail.

## Operative instruction

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

Choose the smallest sufficient route whose commitment, delay, information, and
maintenance costs are justified. Treat new skills, commands, validators, types,
and indexes as high-maintenance surfaces; require stronger evidence for them
than for a log entry, workshop, note, or instruction. Do not prefer delay merely
because it commits less.

Run the following branch only when the proposed solution would destroy a
meaningful alternative or create dependencies that are costly to reverse.
Otherwise select the route directly from the evidence above.

Compare four moves:

- `commit now` -- current evidence discriminates and the expected cost of
  waiting, fragmentation, or lost coordination warrants commitment
- `passively wait` -- name an exogenous observation that can change the choice
- `run a bounded probe` -- name limited work whose possible output can change
  the choice without committing the whole solution
- `decline or do nothing` -- the problem or expected benefit does not warrant
  commitment, waiting, or a probe

For `passively wait` or `run a bounded probe`, name the alternative being
preserved, the observation or possible output that can change the decision,
whether the opportunity will remain available, and the current benefit,
coordination value, or opportunity lost by waiting. Give the move a review,
stop, or follow-on decision rule. If no later result can change the choice,
waiting or probing is not an information-producing reason to defer it.

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
- A costly-to-reverse commitment was compared with waiting or a bounded probe
  only when a meaningful alternative can remain live.
- Any deferral names discriminating evidence and a return to decision.
- Any implementation step follows from the problem, not from momentum behind the initial solution.

If any check fails, do not implement yet.

## Critical constraints

- Do not treat the proposed solution as accepted until the report is complete.
- Do not write durable artifacts as part of this instruction unless the user explicitly asks you to continue after the report.
- Do not force a new artifact when `do nothing`, `ask a question`, `log`, or `workshop` is the better route.
- Do not bury ambiguity by silently choosing one problem hypothesis.
- Do not include long rationale; keep the output short enough to precede real work.

## Case

**Passive wait for a discriminating external signal**

Choosing either of two vendor adapters creates a costly dependency. In ten days the vendor will announce which authentication protocol remains supported; either announcement maps to a different adapter choice. The release is six weeks away, both adapters remain available after the announcement, and there is no current benefit from choosing now. The proposed solution is to select an adapter today.

## Sole output

Write one JSON object to `kb/work/planning-delegation-theory/commit-wait-probe-assay/generated/responses/trial-d738b4a5763e.json` with exactly these keys:

```json
{
  "packet_id": "trial-d738b4a5763e",
  "decision_class": "direct | commit | wait | probe | decline",
  "recommended_next_move": "at most 45 words",
  "option_analysis_used": true,
  "preserved_alternative": "string or null",
  "discriminating_input": "string or null",
  "opportunity_status": "string or null",
  "delay_or_probe_cost": "string or null",
  "return_rule": "string or null",
  "reason": "at most 70 words"
}
```

Use JSON `null`, not the string `"null"`. `direct` means selecting the route
without invoking the costly-commitment comparison. `commit` means the
costly-commitment comparison applies and current action wins. `wait` means
passive waiting for an exogenous observation. `probe` means bounded active work
whose output can change the choice. `decline` includes do nothing or removing
an unwarranted future item.

Modify no other file. End your turn after the JSON file exists.
