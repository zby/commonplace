# Delegated authoring surface sweep

## Question and boundary

This pass asked where current Commonplace machinery writes a command, plan,
worker packet, mailbox request, or generated prompt for another agent, and
whether the planning/delegation workshop supports a concrete refinement.

It covered all 101 tracked canonical files under `kb/instructions/` other than
the multistage target while that target was being rebuilt. It also covered all
18 tracked `kb/types/` files, `kb/messages/README.md`, all seven tracked
`kb/tasks/` files, `AGENTS.md`, `AGENTS.md.template`, and all 97 tracked Python
files under `src/commonplace/`. Generated skill projections, source ingests,
historical workshops, and vendored artifacts were excluded. Tests were opened
only to verify generated-prompt and relocation behavior.

The primary searches combined these terms over the scoped tracked files:

```text
delegate | sub-agent | worker | handoff | dispatch | spawn | parallel | fresh context
prompt | brief | packet | plan | checklist | task text | command
defer | pending | follow-up | future work | revisit | resume | trigger | return condition
invoke | run | execute | cp-skill-* | review bundles and gates
```

The instruction sweep screened 28 delegation candidates, 37 prompt/plan
candidates, 27 deferral candidates, and 14 composition-call candidates before
reading the substantive hits and their direct siblings. The non-instruction
sweep enumerated the complete scoped file sets and found one shipped generated
model-prompt surface: the review-job renderer.

## Transfer test

This report keeps three layers separate:

1. The outside methodologies describe their own domains. They do not prescribe
   Commonplace files, stages, fields, or worker counts.
2. The shared mechanisms are intent-preserving allocation of execution-time
   choice; progressive commitment when later evidence can discriminate; option
   preservation when commitment is costly to reverse; explicit adaptation
   conditions; and preservation of alternatives when evidence has not selected
   one.
3. The Commonplace consequence is local and conditional. A consequential
   worker packet fixes intent, authority, coupling, ownership, verification,
   and return conditions while leaving evidence-dependent means open. A coarse
   future decision needs evidence and convergence only when it preserves a
   meaningful choice. Ordinary queueing, worker-slot waiting, diagnostic open
   items, and cheap reversible choices do not acquire real-options machinery.

## Multistage writer result

`cp-skill-write-multistage` now has a three-role universal core:

1. one isolated source reconstructor;
2. one consolidated candidate author that freezes source-first disposition
   before incumbent reveal; and
3. one fresh independent reviewer whose `accept` or `block` decision is bound
   to the exact candidate SHA-256.

The parent owns admission, intent and evidence, run state, decisions,
invalidation, grounding, scheduling, integration, drift detection, promotion,
validation, lineage, recovery, and close. The author chooses decomposition,
section order, paragraph structure, examples, and prose within that commission.
The rewrite removes the required claim-skeleton worker/file, draft-only worker,
mutable audit, and conditional second acceptance call. Conditional composition
procedures may use only the extra workers and artifacts their own contracts
explicitly authorize.

Eight independent-audit findings were resolved before acceptance: complete
claim disposition, common collection loading, initial evidence acquisition,
post-review convergence accounting, conditional literature workers,
assessment-owned grounding reuse, recoverable relocation, and relocation-time
digest/validation safety. The accepted and promoted bytes have SHA-256
`387472373f8cc1ef79b0f5a02cbeadeeb6f8dca4693835c0f1b4fabd03184da8`.
The named-source guard was not applicable because the procedural rewrite added
no claim dependent on a named outside source. Target validation was clean, and
the scaffold projection test passed all 18 cases.

The maintainer selected universal final acceptance and the three-role topology,
with no retitle or additional-artifact decision in this run. Promotion changed
no lineage source and produced no grounding side effect. The disposable
multistage workshop was removed after this account captured its audit,
acceptance, digest, and validation result.

## Low-hanging changes applied

| Surface | Problem | Shared mechanism and bounded change |
|---|---|---|
| `kb/types/instruction.md` | Consequential worker packets were covered, but intentionally coarse future choices had no type-level return rule. | Require discriminating evidence, return owner, invalidation, and retry boundary only for consequential deferral; exclude queues and cheap reversible choices. |
| `kb/instructions/COLLECTION.md` | The `invokes` link rule preferred fresh context merely to reset context, contradicting the collection's stronger delegation rule. | Use a fresh worker only for a named isolation, later-evidence, or independent-judgment advantage and a complete consequential packet. |
| `kb/instructions/write-instruction.md` | The reusable authoring procedure lagged the type's information-allocation rule. | Fix upstream-only intent/coupling facts; leave evidence-dependent means open; require return and convergence for consequential deferral. |
| `kb/messages/README.md` | Self-contained mailbox requests named edit/report authority but not the rest of a consequential handoff. | Add a conditional compact request contract while preserving that a message neither expands authority nor launches an agent. |
| `evaluate-log-entry-for-note-creation.md` | “Keep in the log” could defer indefinitely. | Name the missing mechanism/evidence, discriminating observation, and re-evaluation trigger; reject when no later evidence can decide. |
| `simplify-prose-sentence-by-sentence.md` | `defer` returned only a generic larger problem. | Return the exact author-owned choice or missing evidence, affected units, recipient/procedure, and resume condition. |
| warning-fix instruction, sweep, and `FIX-SYSTEM.md` | Deferred findings were underspecified, and every note was automatically delegated for parallelism. | Return exact substantive choices; execute locally by default; delegate only disjoint notes with a named context/capacity benefit and exact note/report ownership. |
| `revise-note.md` | A tag edit automatically launched a worker over unspecified nearby files. | Parent inventories exact impact and authority first; local execution is default, and any worker gets exact paths, deltas, validation, and stops. |
| `cp-skill-revise-autoreason/SKILL.md` | Fresh actors could rediscover the parent revision skill or delegate recursively. | Mark each actor packet complete, ignore auto-loaded orchestration skills, and forbid further delegation. |
| `run-full-improvement-pass-on-note.md` | The copyeditor received only an outcome phrase while being expected to write a specific path and preserve semantic invariants. | Supply exact input/output, allowed transformations, preserved commitments, sole write scope, anti-recursion rule, and substantive-change stop. |
| `write-agent-memory-system-review/SKILL.md` | The isolated drafting worker explicitly permitted undefined grandchildren when tools existed. | Forbid further delegation and return a blocker when direct completion is impossible. |
| review prompt renderer | Report jobs forbade `ERROR` although the parser already treats it as the job-failing escalation route; generated prompts were silent on delegation. | Permit exact `REPORT|ERROR`, explain when `ERROR` is required, forbid guessing and delegation, and test the rendered contract. |

## Deliberate non-changes

- `AGENTS.md`, `AGENTS.md.template`, the instruction collection's main
  delegation section, and the instruction type's worker-packet rule already
  allocate authority and integration correctly.
- `cp-skill-ingest` plus `draft-ingest-report` remains the strongest complete
  isolation packet: exact inputs, sole output, checksum/backup verification,
  no auto-skill recursion, no nested worker, one repair, and recovery.
- `run-review-batches` preserves exact generated prompts, disjoint job-owned
  outputs, parent finalization, and single-use workers.
- compression, composition-friction, premise-decomposition, and critique
  workers use fresh context for independent judgment and remain report-only.
- review/fix queues, full-pass pending state, connect observations, and generic
  backlog delay are workflow state rather than preserved costly options.
- no shipped generic worker-command runner exists. Review jobs deliberately
  remain parent-dispatched; adding a scheduler would lack a second consumer and
  a demonstrated failure case.

## Separate follow-ups

- `analyse-agentic-system/SKILL.md` should receive concrete memory- and
  epistemic-lens packet templates. This is a larger skill redesign, not a local
  wording repair.
- The bilateral literature branch and its ground→ingest composition chain need
  one coordinated review of exact nested authority, outputs, and lifecycle.
  The multistage writer now permits only the chain the loaded sibling actually
  authorizes, but it does not repair sibling packet omissions.
- The demoted `cp-skill-revise-iterative` still shells out to `claude -p`.
  Retirement or a harness-native rebuild is preferable to prompt polishing.
- The memory-system review workflow's archive-before-draft and recovery paths
  need a dedicated failure-path pass; the local no-grandchild fix does not
  address that state machine.
- `kb/tasks/` and `kb/messages/` are source-checkout-only today. Before changing
  active/recurring task contracts or stale task placement, decide whether that
  subsystem should ship to consuming projects or be labeled explicitly as
  source-only.
- Review-prompt scaffolding is outside freshness hashes. The `ERROR` and
  no-delegation repair changes failure behavior, not criterion judgment, so it
  does not justify bulk re-review; future judgment-shaping renderer changes
  must make that decision explicitly.

## Conclusion

The sweep supports a compact operative center rather than a new planning
framework. Intent-framed delegation remains the best small cue for assigning
execution-time means. Rolling-wave, real-options, DAPP, and set-based theory
refine when to leave a choice open, what evidence should close it, and how to
avoid premature commitment. They do not displace the operative core, and they
do not warrant universal planning fields or extra worker stages.

## Validation

- All 17 changed or newly created Markdown artifacts passed explicit
  `commonplace-validate` calls without warnings or failures.
- Focused review-prompt lint and 26 protocol/report tests passed.
- The promoted-skill scaffold projection test passed all 18 cases.
- The full suite passed all 599 tests in 44.24 seconds.
- `git diff --check` passed before commit.
