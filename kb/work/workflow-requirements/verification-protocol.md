# The correction and verification protocol as implemented

What the analysis workflow does today when a candidate is refused, when a
producer answers a refusal, and when a verifier judges other members. This
is a description of the code and instructions on 2026-10-09, written so
that the [plans-without-consumer-code](../../reference/proposals/plans-without-structural-wrapper-code.md)
design can say which parts are a reusable protocol, which are policy a
consumer chooses, and which are this consumer's alone. Sol's review of
that proposal asked for this: a standard apply handler assumes a verdict
language, and the layout does not supply one.

The protocol has three layers. The engine fixes the first for every
consumer. The reuse module `artifactrun/checks.py` implements the second
and any consumer may use it. The analysis package, its types and its
worker instructions supply the third.

## Layer 1: what the engine fixes

These hold for every plan ([ADR 113](../../reference/adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md),
[requirements](./requirements.md) 5 to 8).

- **A judgment** is a code job's verdict on one subject version: accepted
  or refused, with findings, a basis (the job's pinned inputs) and a scope
  (relations it covers). An acceptance of the producer's latest completed
  output installs it in its role. A refusal of any version is evidence; a
  refusal of the latest completed output is what the producer answers.
- **The refusal input.** Every model job that fills a role has an optional
  `refusal` input the loader adds unless the plan declared one
  (`plan._with_refusal`), resolving to the latest refusal of its latest
  completed output, as a document: frontmatter `refusal` (identity), `version` and
  `scope`; body, the findings verbatim (`run.refusal_document`). An
  attempt that read a refusal has answered it; only a newer refusal makes
  the job ready again. A later acceptance supersedes a refusal when its
  scope includes the refusal's scope or names it as overridden.
- **Handed inputs.** A code job may declare the version a model attempt
  was handed, by attempt record and input name. An apply job judges those
  exact versions, never the current members.
- **The auxiliary-output rule.** An attempt answering a refusal with its
  primary output unchanged completes only if it produced a changed
  auxiliary output, such as answers; otherwise it fails. Completion is not
  acceptance: the check job decides whether the answers resolve the
  refusal.
- **Max attempts** per model job, counting identical and failed attempts,
  never reset. Exhaustion stops the run; the recourse is an operator
  override or a new run.

The engine does not know what findings mean, what a blocker is, or that
a verification is a judgment of something.

## Layer 2: the shared check protocol

`artifactrun/checks.py` is the reuse module every analysis check and
apply handler calls. It fixes the following for any consumer that uses it.

- **The candidate.** `candidate(attempt, role, partners)` reads the
  `candidate` input, snapshots the partner roles' versions from the
  attempt's pinned inputs, and may bind a frozen source from one partner.
  `review()` runs draft validation in the role against the pinned criteria,
  plus frozen-source refusals.
- **The refusal packet.** A refusal's findings are a Markdown document:
  `## Findings` with one line per reason, then `## Blockers`, then every
  other section of the refusal the producer had answered, carried forward
  unchanged (`refusal_findings`). The Blockers section is copied from the
  answered refusal, so a structural refusal of a correction attempt keeps
  the semantic blockers the attempt was answering. An unstructured refusal,
  such as an operator's `judge --findings`, counts as one blocker addressed
  to the refused role (`correction_blockers`).
- **The answers grammar.** When a producer declares an `answers` output,
  the check requires exactly one `- corrected: <reason>` or
  `- declined: <reason>` line per blocker of the answered refusal, in
  order, and no other `- ` line; an entry saying `corrected` with the
  primary output byte-identical to the handed previous version is a
  failure (`correction_findings`). The check reads the producer's attempt
  record for the previous version and the handed `answered-refusal`.
- **The scope rule.** `judge(check, reasons, subjects=...)` accepts or
  refuses the candidate over the type's relations from its role to the
  partners present in the snapshot, excluding the named subjects. This is
  how a verification's content acceptance is kept from covering the
  relations its apply job owns.

What this layer does not fix: who the subjects are, what a blocker
addresses, what happens to roles a verdict does not address, and what a
verifier must say about a structural failure. Those are layer 3.

## Layer 3: the analysis consumer's protocol

### The verdict language

The verification type ([agentic-system-verification](../../agentic-system-analyses/types/agentic-system-verification.md))
fixes the document: frontmatter `verifies: records | profile | synthesis`;
sections `## Verification`, `## Blockers`, `## Limits`. Blockers and Limits
are each exactly `none` or a Markdown list with one `- ` entry per finding,
continuation lines indented. A blocker is a defect that must be repaired
before publication; a limit is a local issue the analysis can be published
with, which the synthesis must carry into its Limitations with the affected
IDs. The set type's rule enforces the format, the `verifies` value against
the role, the addressee prefix on record blockers, and the carriage of every
limit into the synthesis (`rules.py`, the set rule; the repair text for
"limit not carried" is in `directory_layout.py`).

### Three verifications, two routing policies

| Verification | Subjects | Blocker addressing | Apply handler |
|---|---|---|---|
| record-verification | runtime, memory, epistemic, reconciliation | each blocker starts `runtime:`, `memory:`, `epistemic:` or `reconciliation:`; a defect in two reports is two blockers | `verification.apply_verify` |
| profile-verification | memory-profile | none; the one author owns every blocker | `profile.apply_verify_profile` |
| synthesis-verification | synthesis | none | `profile.apply_verify_synthesis` |

All three handlers first run the shared check on the verdict document
itself, with the subjects excluded from the content acceptance's scope.
A verdict that fails its own content check is refused like any candidate
and judges nothing. Only a valid verdict goes on to judge its subjects.

**Record verification, partial verdicts.** With blockers, the handler
refuses each addressed role's handed version over
`record-verification:cites:<role>`, with a feedback document holding that
role's blockers and the declarations of records from other reports those
blockers cite (`_feedback`). Roles no blocker addresses are not judged at
all: their gates stay unsettled until a blocker-free verdict. With
Blockers `none`, the handler accepts all four handed versions. The record
verifier's instruction states the same: a verdict with blockers supplies
refusals only to addressed authors and settles no other gate.

**The record-check gate.** Before verification, the code job
`record-check` validates the five record members as one pinned snapshot
and writes its findings as a document (`# Record check`, a list or
`none`). The verifier reads it. If it reported failures and the verdict has
no blockers, the apply handler refuses the verdict: a structural failure
requires an explicit blocker addressed to its report. The verifier's
instruction adds that a failure it cannot route within its authority
becomes `problem`, not a dismissal.

**Profile and synthesis verification, single subject.** The handler
refuses the handed subject over `<stage>-verification:cites:<subject>`
with the Blockers section as findings, or accepts it when Blockers is
`none`. For the synthesis, the handler additionally validates the handed
synthesis against this exact verdict and adds any "limit not carried"
findings to the refusal, so a limit the verifier declares that the
synthesis does not carry is a refusal of the synthesis, not of the
verdict. Both refusals append the verdict's Limits section.

### The producer's side

The worker rules ([follow the engine analysis worker rules](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/follow-worker-rules.md),
"Answer correction obligations") and the records contract fix what a
producer does with a refusal:

- Analysts, the profile, the synthesis and the two single-subject verifiers
  write `output-answers`; the boundary, the reconciliation and the record
  verifier repair in their primary output without answers.
- Each blocker is answered in order, `corrected` or `declined` with a
  reason. A `corrected` answer needs a changed primary output. All
  `declined` may leave the output byte-identical; that completes the
  attempt and settles nothing. Repeating both output and answers fails.
- A corrected analyst report keeps every record ID its predecessor
  declared; the analyst check enforces this against the incumbent
  (`handlers._check_analyst`).
- A structural refusal of a correction attempt carries the earlier semantic
  blockers, and the producer answers those too.

### The verifier's side on retry

A verifier's later attempt receives its previous verdict by identity and
the producers' answers, reads them, and judges afresh: an answered blocker
is not settled; `corrected` is checked against the changed passage,
`declined` against the evidence, and a previous verifier can be wrong.

### One cycle, records

1. The memory analyst completes. `check-memory` refuses: `## Findings`
   lists validation failures, `## Blockers` is `none`. The analyst's next
   attempt repairs, with an empty answers file.
2. `check-memory` accepts. `record-check` runs and writes `none`. `verify`
   is handed the five records and the record check.
3. The verifier completes with two blockers, both `memory:`.
   `apply-verify` validates the verdict, accepts it over its relations to
   boundary, refuses the handed memory version with the two blockers as
   findings, and judges nothing about runtime, epistemic or reconciliation.
4. The memory analyst is ready again, with the refusal as input. It
   corrects and writes two answers. `check-memory` checks the answers
   against that exact refusal and the handed previous version, then accepts.
5. `record-check` reruns on the new snapshot. `verify` is ready because its
   memory input changed; its hand-out carries the previous verdict and the
   memory answers. It completes with Blockers `none`. `apply-verify`
   accepts all four handed versions; the profile's judgment gates are now
   present.

## What varies and what is fixed

| Element | Where it lives | Fixed or variable today |
|---|---|---|
| Judgment, refusal input, answered refusal, auxiliary-output rule | engine | fixed for every consumer |
| Max attempts | plan, per model job | variable |
| Refusal packet sections, answers grammar, scope rule | `checks.py` | fixed for consumers that use the module |
| Which roles a verifier judges | handler constants (`RECORDS`, `subject_role`) | variable, in Python |
| Blocker addressing grammar | verification type rule and verifier instruction | fixed to the four record roles |
| Partial-verdict policy: refuse addressed, leave the rest unsettled | `apply_verify` | fixed, in Python |
| Record-check gate | plan job plus `apply_verify` | fixed, in Python |
| Limits carried into the synthesis | set type rule plus `apply_verify_synthesis` | fixed, in Python and the rule |
| Which producers write answers | plan outputs plus worker rules | variable in the plan, repeated in prose |
| Feedback composition with cited records | `_feedback` | this consumer's alone |
| Materiality: what is a blocker, what is a limit | verification type and verifier instructions | prose, not code |

The policy choices a generic apply handler would have to take as given or
as parameters are the partial-verdict policy, the addressee grammar, the
record-check gate and the limits rule. The first two have one natural
reading for any multi-subject verifier: a blocker names the subject it
addresses, addressed subjects are refused, unaddressed subjects wait. The
other two are relations between this consumer's roles that a type rule can
state. The feedback composition and the materiality rules are not
protocol; they are this consumer's content.
