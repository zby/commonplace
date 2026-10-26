# What a Commonplace skill needs from a sub-agent

Written 2026-10-26 at the operator's request, after the ADR 086 worker
amendment ruled that skills use only a harness-provided sub-agent. This file
fixes what that facility must do, so that a harness extension (pi today, others
later) can be built or checked against a list instead of against the skills'
scattered wording. It is derived from the skill texts named below, not from any
harness. When it settles it should move next to the amendment or into
`cp-skill-health-check` Step 3, whose report fields already cover depth,
isolation and capacity.

This is not the analysis workflow's worker contract.
[check-subagent-harness.md](../../instructions/check-subagent-harness.md)
covers `commonplace-analysis run` launching headless `claude -p`, `codex exec`
or `pi -p` processes under ADR 118/119. Where a requirement below matches one
there, the ID is cited; the difference is the caller: here a skill running
inside an interactive session calls a tool and gets the result back in the
same conversation.

## Who needs it

Promoted skills whose text calls for a fresh worker: `cp-skill-ingest` (one
drafting worker, one replacement; fails closed without isolation),
`cp-skill-write-multistage` (reconstructor, author, reviewer),
`cp-skill-revise-autoreason` (up to seven per pass, three judges in parallel),
and `cp-skill-health-check` (one read-only probe worker). Repository-local
instructions with the same need: `run-review-batches`,
`run-full-improvement-pass-on-note`, `critique-note`, the two gates,
`review-code`, `stage-an-article-package`, `fix-review-warnings-sweep`. The
delivery probe's `delivery-probe-delegate` skill (case 10) is the smoke test.

## Requirements

"Enforcement" says whether the skills can rely on the runtime for the property
or must state it in the handoff. "pi extension" is what this checkout's
`.pi/extensions/subagent` claims in [.pi/README.md](../../../.pi/README.md) as
of pi 1.3.0; none of it is yet tested outside this checkout.

| ID | Requirement | Demanded by | Enforcement | pi extension |
|---|---|---|---|---|
| S1 | **Fresh context.** A new conversation with none of the parent's turns, summaries or answers; not a fork. A follow-up turn to an earlier worker is not fresh. Without this the skill stops (ingest, write-multistage) or must do writeback itself (revise-autoreason tolerates a forked workspace). Matches B1. | ingest, write-multistage, revise-autoreason, the gates | runtime | yes: new persistent session, parent conversation never copied |
| S2 | **Called from the session, result returned to it.** A tool call made by the running skill, whose result arrives in the same conversation. A shell launch of a harness CLI does not qualify (ADR 086 amendment). | all; ingest forbids CLI launches | runtime | yes |
| S3 | **Rooted in the project.** The worker's working directory is the project. It loads the project's standing instructions and library pointers with binding force, or the parent knows it does not and states them (CLAUDE.md Delegation). It can read the installed library outside the project: in Claude Code the project read rule covered the sub-agent (r7 case 10). Matches B3 and B5. | all | runtime, with the parent verifying what is loaded | `cwd` parameter; children load repository context under project trust |
| S4 | **Verbatim handoff.** The task text reaches the worker unchanged, including absolute paths and multiline values whose bytes matter (ingest's `retained_quotes`). The worker can read whole files and recover truncated reads. Matches B2. | ingest, revise-autoreason (blind packets) | runtime | task string; definition body via a temporary file |
| S5 | **Tools as the handoff requires.** Read, write, edit and shell when needed; a way to give a worker fewer tools (a judge needs none but read). | all; health-check's probe worker must use no tools | runtime for the set, instruction for restraint within it | `tools` in the agent definition; malformed lists reject rather than fall back |
| S6 | **Attributable result and distinct failure.** The worker's final answer comes back as text; a crash, abort or error is reported as failure, not as an answer. Files the worker wrote are visible to the parent on the shared filesystem, or the worker returns full content for the parent to write. Matches B6. | all; revise-autoreason's writeback rule | runtime | yes: latest response plus process outcome; `sessionId`, `sessionFile`, `executionDir` |
| S7 | **Lifecycle.** Single-use workers the parent can wait on, check, cancel and release; the skills close each actor after its handoff is verified. | revise-autoreason, review batches, improvement pass | runtime | `start`, `status`, `wait`, `cancel`, `forget`; blocking call by default |
| S8 | **Parallel workers under a known limit.** Several workers at once where the skill allows (three judges; one per review job), and a capacity limit the parent can hit deterministically and queue against rather than nest. | revise-autoreason, review batches | runtime | up to 8 per call; active-job limit |
| S9 | **No nesting by the worker.** The worker launches no further agents. Preferably the worker lacks the delegation tool; otherwise the handoff forbids it (ingest's dispatch does). Health-check reports remaining depth when the runtime exposes it. | ingest, improvement pass, review batches | runtime preferred, instruction fallback | `commonplace-worker` definition has no delegation tool |
| S10 | **Information hiding.** The worker sees only the handoff plus standing rules. Fresh context gives this for the conversation; the filesystem is shared, so blind judges rely on the handoff not naming the hidden files. Matches B8: conversation isolation is not a sandbox. | revise-autoreason (judges), write-multistage (bilateral isolation) | instruction, unless the harness restricts reads | not a filesystem sandbox (stated) |
| S11 | **Inspectable record.** The child's session persists as a legible record the parent or operator can locate afterwards, so a result can be audited and further tooling built on it. This is the operator's stated reason for the sub-agent route. | the amendment | runtime | `sessionFile` plus a per-execution audit directory |
| S12 | **Model and effort selection.** Wanted, not required: no skill depends on it. `revise-autoreason` says "Codex sub-agents", which names a harness, not a model; ADR 118 workers select models for the workflow, not for a skill. | none | runtime | `model`, `thinkingLevel` overrides |
| S13 | **Permissions resolved.** The worker runs under the project's permission settings; a request it cannot satisfy reaches the operator or fails visibly, never silently. | all | runtime | project trust at pi startup; inherits settings |

S1, S2, S3, S6 and S9 are the minimum: a facility missing any of them cannot
run `cp-skill-ingest`. S7, S8 add `cp-skill-revise-autoreason` and the review
instructions. S11 is what makes the facility a sub-agent rather than a launch.

## Where Claude Code and Codex stand

Both supplied a native facility in probe revision 7 (case 10 passed in each).
Known gaps against the list: Codex's collaboration agents were not rooted in
the scratch project in the r7 run (S3; the rerun is pending). Neither run
checked S7, S8 or S11; Claude Code's session log attributed the delegated read
to the sub-agent's id, which is S11 evidence in the parent's own record.
Remaining depth (S9) is unknown in both unless the runtime states it.

## What delivery to a pi user would have to carry

The pi facility is three things, none of them in the package or in anything
init writes:

1. the extension code under `.pi/extensions/subagent/` (six TypeScript files
   plus tests), loaded by pi from the project under project trust;
2. an agent definition, `.pi/agents/commonplace-worker.md`, discovered from the
   child's working directory with `agentScope: "project"` (the default is
   user-level `~/.pi/agents/`);
3. the operator granting project trust to the installed project at pi startup.

So a pi user of an installed project needs either both `.pi/` directories in
their project, or a user-level installation of the same two pieces. Which of
these pi 1.3.0 supports cleanly, and whether init should write `.pi/` pointers
the way it writes `.claude/` and `.agents/` ones, is the open question recorded
in the workshop README as step 3's follow-up. The probe's case 10 run in a
scratch project with the chosen delivery in place is the acceptance test, and
S7, S8 and S11 need their own small checks beyond it.
