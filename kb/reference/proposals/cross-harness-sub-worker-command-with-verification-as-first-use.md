---
description: "Proposal: a commonplace-sub-worker command that launches one headless worker on any configured harness and model through Workjig, first used by an operator-directed verify skill whose detail findings the calling agent integrates"
type: reference/types/design-proposal.md
---

# Cross-harness sub-worker command with verification as first use

Consider adding `commonplace-sub-worker`, a command that makes one call to a
headless worker through Workjig and prints the result. A worker launched this
way by an agent is called a sub-worker here, to keep it distinct from a
sub-agent, which is a worker the harness's own facility provides. The caller names a
worker profile, so the worker can run on a different harness and model from
the calling agent. The first use would be a verify skill: the operator asks
the agent to check its work with a named model, the agent launches one
worker, and it integrates the findings.

The problem is that models differ in what they are good at, and some models
are reachable only through particular harnesses. A harness's own sub-agent
facility launches workers inside that harness only. An agent in one harness
therefore cannot hand a subtask to a model that lives in another. The
operator's working judgment (2026-11-28) is that one model is strong on
detail, another on reading the user's need, and a third on the overall
picture, and that no single harness reaches all three.

The intended outcome is one general launch mechanism that reaches every
configured harness and model, so the caller does not need to know the harness
command or its options. The mechanism is not limited to consultation; a
worker may also be given a writing subtask. The explanatory case is that
`commonplace.headless` already hides harness commands behind worker profiles
for the workflow commands, so exposing one call of it gives agents the same
reach.

The sub-worker does not replace the harness sub-agent. Rebuilding what the
harnesses already provide would be a lot of work for no new reach. The
sub-worker approximates a sub-agent for the one case the native facility
cannot serve: a worker on another harness. Where the calling agent's own
harness offers a suitable model, the native sub-agent stays the path.

This is an unadopted proposal. Its first use needs an operator decision that
narrows ADR 086's worker amendment (see "The decision this needs").

## Current state (as of 2026-11-28)

- **Skills use only native sub-agents.** The worker amendment to
  [ADR 086](../adr/086-projects-read-the-library-from-the-installed-package.md)
  (2026-10-24) rules that skills needing a fresh-context worker use only a
  sub-agent facility the harness provides. A headless harness process
  launched from the shell is "not an emulation of one". The operator's
  reason: a sub-agent is a two-way, inspectable relationship, while a
  headless launch is one-way. `cp-skill-ingest` states the rule as "never
  launch `codex`, `codex exec`, `claude`, or another agent CLI from the shell".
- **Native sub-agents stay inside their harness.** No harness facility in use
  here launches a worker on another harness.
- **Workflow commands already launch headless workers through Workjig.**
  `commonplace-analysis`, `commonplace-review`, the worker-launching modes of
  `commonplace-revise` and `commonplace-task` all launch through
  `commonplace.headless`. ADR 086 classes these as a workflow engine's
  workers, not a skill's sub-agents
  ([ADR 119](../adr/119-analysis-workers-launch-through-workjig.md)).
- **The launch layer is harness-neutral.** `commonplace.headless.harness`
  maps a worker profile (harness, launch model, effort, flags) to a Workjig
  command worker for `claude-code`, `codex`, `pi` and `antigravity`. It also
  reads the model each harness recorded for a launch.
  `commonplace.headless.jobs` provides `Run.ask(job, prompt, outputs)`: named
  input and output files, a problem file as a result, and the launch and
  attempt rules of ADR 119.
- **Workjig has no command-line entry point.** An agent cannot call it from
  the shell without a Commonplace command.
- **A one-call command already exists in a narrow form.** `commonplace-task run`
  (`src/commonplace/lib/tasks.py`, about 150 lines) makes one `Run.ask`, then
  checks the worker's commit against git. It accepts only runbooks under
  `kb/tasks/` and profiles from `kb/tasks/profiles.yaml`.
- **Worker profiles live in three files, and each mixes model and permission.**
  These are the analysis method's `worker-profiles.yaml`,
  `kb/instructions/review-profiles.yaml` and `kb/tasks/profiles.yaml`. The
  review profiles are read-only grants; the task profiles grant edits and
  commits.
- **Read-only is not enforceable on every harness.** The review profiles
  record that Codex cannot make the checkout read-only while keeping one
  subdirectory writable, and that Antigravity keeps workspace writes
  available. Both rely on the prompt and on a checkout guard that reports
  changes.
- **Workjig runs leave records in the state tree, which is published.** The
  Workjig-based commands write one run directory per run under
  `kb/workflow-state/data/current/<workflow>/`. That tree is a separate
  repository, ignored by the main one and public. It excludes only the
  harness `stdout.log` and `stderr.log` files. Its README names, per
  workflow, what the directory holds and what deleting it loses; the
  [workflow-state contract](../../workflow-state/COLLECTION.md) lets only
  the owning workflow set the cleanup rule.

## The design

Flag names, file names and record locations below are illustrative, not
binding.

### commonplace-sub-worker

```text
commonplace-sub-worker run --profile NAME --brief PATH
    [--input NAME=PATH ...] [--output NAME ...] [--write] [--timeout SECONDS]
```

- **One call.** The command makes one `Run.ask` call in the current checkout
  and returns after it settles. The worker loads the checkout's normal
  project configuration, as other headless workers do. The default output is
  one answer file.
- **Fixed frame.** The command wraps the brief in a frame that states only
  what is true of every such worker: another agent launched it, nobody will
  answer questions, it writes the named outputs, and it writes the problem
  file if it cannot proceed. Everything specific to the task comes from the
  brief.
- **Profiles name a model.** A profile maps a name to harness, launch model
  and effort. It says which capability the caller wants, not what the worker
  may do.
- **Permission is a separate choice.** Each profile carries a read flag set
  and a write flag set. Read is the default, and `--write` selects the other.
  Without this split, a general mechanism needs a read and a write variant
  of every model.
- **A writing worker does not commit.** It edits files. The calling agent
  reads the diff, integrates and commits. Delegation does not expand
  authority, and the parent keeps integration.
- **The command reports checkout changes in both modes.** It compares
  `git status` before and after the call. In read mode any change is a
  violation. In write mode the list is the result. On harnesses that cannot
  enforce read-only, this report is the actual check.
- **Result.** The command prints JSON: call status, output paths or the
  worker's problem text, the model the harness recorded, the run directory
  and the checkout changes. Exit codes separate an answer from a problem
  file, a failed launch, a usage limit and a setup error.
- **Records.** Every call leaves a run directory under
  `kb/workflow-state/data/current/sub-worker/`: Workjig's call and launch
  records, the brief and inputs as delivered, the outputs, an event log and
  the harness's stdout and stderr. The printed result names it.
- **No conversation.** A follow-up is a new call that takes the previous
  answer as an input. Parallel calls each get their own run directory;
  disjoint write scopes are the caller's responsibility.

The records have three consequences.

- **Briefs and outputs become public once committed to the state
  repository.** A verify brief carries the operator's request and
  constraints, and a target may be unpublished work. The calling agent
  therefore writes a brief as a document that may be published, and the
  skill says so. Material that must stay private does not go through the
  command in this design.
- **The command owns its directory.** The state repository's README gets a
  row for `sub-worker/`. The calling agent reads a run once, when the call
  returns. Deleting a run loses the brief, the worker's answer and the
  record of which model gave it; nothing else reads it, so removal is safe
  once no open work cites it.
- **Runs accumulate.** Each verification adds a directory, and nothing
  prunes them. This is accepted until the volume is observed.

The command adds an entry point over existing code, not a new runtime.
`commonplace-task` is the feasibility witness: it is the same call plus
runbook loading and commit checks.

### Uses are skills over the command

Each use is a brief template plus a rule for handling the result. The
command knows nothing about any use. Candidate later uses need no new code:
a check of the user's need with one model, an overall-picture read with
another, or a writing subtask handed to a model that does it better.

### The verify skill

The first use is operator-directed. The operator asks the agent to verify an
artifact or a proposed solution with a named profile. The skill has three
steps.

1. **Brief.** The worker does not see the conversation. The agent writes the
   operator's request, the constraints the operator set, the target paths
   and the lens of the check. A proposal that exists only in conversation
   goes in as an input file. The brief leaves out the agent's own doubts and
   conclusions, because
   [exclusion guarantees non-exposure where instructions to ignore do not](../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md).
2. **Run.** One read-mode call. The worker returns numbered findings, each
   with a location, the problem and a suggested fix, or states that it found
   none.
3. **Integrate.** The agent gives each finding one of three outcomes.
   *Apply*: the finding is local, checkable against the file or its source,
   and changes no direction. *Decline*: the agent checked it and it is wrong
   or not worth the change; the agent records a one-line reason. *Escalate*:
   the finding changes direction, contradicts an operator decision, widens
   scope, or the agent disagrees and the point matters. The agent reports
   the counts and lists every declined and escalated finding.

The integration rule is keyed on the kind of finding, not on the profile.
The operator expects a detail-oriented model to return mostly findings that
are applied, which is why integrating its feedback can be automatic.
Findings from a model consulted on direction would mostly be escalated, with
no per-profile configuration.

The check is advisory. Its warrant is that the worker has a fresh context
and, usually, a different model, so its errors are partly decorrelated from
the agent's
([error correction with decorrelated checks](../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)).
Neither source of decorrelation has been measured here. The skill never
grants `user-verified` and does not replace human verification.

## The decision this needs

The command alone does not conflict with ADR 086 when the operator directs
its use; it is one more worker-launching command. The verify skill does
conflict: it is a skill that obtains a worker through a headless launch,
which the worker amendment forbids.

Adoption would keep the amendment's rule and add one exception. A skill
still uses the native sub-agent for a worker on its own harness. A skill may
use a sub-worker only when it needs a model on another harness, and it
declares that. The amendment said a headless launch is not an emulation of a
sub-agent. The proposal agrees: the sub-worker is an approximation that
keeps the delegation shape (fresh context, a brief in, named results out,
integration by the parent) and gives up the rest. The operator's stated
reason for the rule was inspectability and two-way interaction. The
approximation meets these only in part:

| Property | Native sub-agent | `commonplace-sub-worker` |
|---|---|---|
| Model on another harness | no | yes |
| Parent can send a follow-up to the same child | yes, where the harness supports it | no; a follow-up is a new call |
| Child's session locatable afterwards | harness-dependent | yes, when the profile turns on Workjig's native-session tracking |
| Durable call record | no | yes |
| Recorded served model | harness-dependent | yes |
| Harness depth, concurrency and approval controls apply | yes | no; the shell call escapes them |
| Needs network and writable state outside the workspace from the shell | no | yes; the same sandbox issue as other worker-launching commands |
| Blocks on the shell tool's timeout | no | yes, unless run in the background (requirement A1 in [check a subagent harness](../../instructions/check-subagent-harness.md)) |

The loss of two-way interaction is real. One-shot uses such as verify do not
need it. Skills whose workers are repaired in conversation might. Existing
worker-dependent skills such as `cp-skill-ingest` and
`cp-skill-write-multistage` keep their native sub-agents.

## Option space

1. **Status quo: native sub-agents only.** This costs nothing. An agent
   reaches only the models its own harness offers. Cross-model checks happen
   by the operator carrying text between sessions.
2. **The general command beside native sub-agents, verify as its first
   skill (this proposal).** It needs the cross-harness exception to ADR 086's
   worker amendment.
   Reversing it means deleting one command, one profile file and one opt-in
   skill.
3. **A consultation-only command.** The command would be read-only and built
   around findings. This is smaller and avoids the write mode's weak
   enforcement. It forecloses handing a writing subtask to a better-suited
   model, which the operator named as part of the need, and a later
   generalization would rename the command.
4. **The command as the worker path for all skills.** This would replace
   the native sub-agent, which the operator rules out (2026-11-28): it is a
   lot of work, ingest's and multistage's handoff repair would lose two-way
   interaction, and every worker-dependent skill would take on the sandbox
   and timeout issues. It is listed for comparison only.
5. **Rival decomposition: cross-harness reach as a harness extension.** Each
   harness would get an extension, like the checkout's `.pi/extensions/subagent`,
   that launches other harnesses through the native sub-agent interface. This
   keeps ADR 086 intact and keeps the harness's controls. It needs one
   extension per calling harness, and not every harness has an extension
   point. No feasibility argument exists for Claude Code or Codex, so this
   remains an unresolved region, not an available option.
6. **Rival for the first use: verify as a `commonplace-review` criterion.**
   Review already launches headless workers from a profile file and accepts
   `--criterion-file`. No new command and no amendment would be needed. Its
   limits are that it reviews notes, that its results are gate findings held
   in review state and not returned to a writing agent, and that it gives no
   general mechanism.

## Open choices

- **Name.** In this KB "sub-agent" means the harness facility. ADR 086 and
  ADR 118 define headless launches as not sub-agents, and the
  [worker collision record](../vocabulary-collisions/worker.md) relies on that
  distinction. The operator chose "sub-worker" (2026-11-28) so the command
  does not claim to be a sub-agent. Two points stay open. "Worker" in the
  collision record already covers both harness sub-agents and headless
  processes, so "sub-worker" separates the two only by the definition given
  here; adoption would register it. And "verify" is close to `user-verified`,
  which means human verification.
- **Read and write as a flag or as separate profiles.** The flag keeps one
  profile per model. Separate profiles match the three existing files.
- **Profile file.** The command adds a fourth profile file. A shared model
  roster for all four would remove the duplication; nothing yet requires it.
- **Record location.** The design puts runs in the published state tree,
  like the other Workjig-based commands. An unpublished scratch root would
  keep briefs private and need no README row. It would lose the backup and
  put the command's records outside the collection that holds every other
  workflow's.
- **Relation to `commonplace-task`.** The task command could later be built
  on this one. Nothing requires that now.

## Operativity and warrant

- **Command.** It is consumed by an agent, through a shell call that the
  operator or a skill step directs. No consumer exists yet; the verify skill
  must be built.
- **Verify skill.** It is consumed by the calling agent, which applies,
  declines or escalates each finding. Applied findings change the artifact
  without operator review of each one, so the force is more than advisory
  for detail findings. The oracle is a model judgment filtered by the
  calling agent's own check. Its warrant comes from decorrelation and from
  the apply condition, which admits only findings checkable against the file
  or its source. The warrant stops at three points: no measured
  discrimination, no authority over direction, and no substitute for human
  verification.

## Adoption criteria

- An operator decision that adds the cross-harness exception to ADR 086's
  worker amendment, and registration of the term "sub-worker".
- The command built over `Run.ask`, with fake-harness tests for each exit
  class and for the checkout-change report, as the existing headless suites
  do.
- A row for `sub-worker/` in the state repository's README, and the
  publication rule for briefs stated in the verify skill.
- A route for the long shell call under each calling harness's tool timeout,
  such as a background call.
- Operator-directed use as the trial. Adoption is cheap to reverse, so a
  few real verifications are enough to start. Two results would change the
  design. If applied findings often need reverting, the apply condition is
  too loose and integration returns to the operator. If the missing
  follow-up proves a frequent obstacle, the harness-extension rival
  (option 5) becomes worth a feasibility probe.

---

Relevant Notes:

- [ADR 086](../adr/086-projects-read-the-library-from-the-installed-package.md) — decided-by: its worker amendment is the rule adoption would amend
- [ADR 119](../adr/119-analysis-workers-launch-through-workjig.md) — decided-by: fixes the launch and attempt rules the command would inherit
- [context contamination operates below an agent's compliance reasoning](../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) — rests-on: why the verify brief excludes the agent's conclusions instead of asking the worker to ignore them
- [error correction works with above-chance oracles and decorrelated checks](../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rests-on: the warrant for a fresh-context, different-model check and its limit
- [check a subagent harness](../../instructions/check-subagent-harness.md) — see-also: the harness requirements a headless launch must meet, including the long shell call
