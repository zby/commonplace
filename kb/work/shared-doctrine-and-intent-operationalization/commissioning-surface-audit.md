# Commissioning-surface audit

## Result

The Outcome 4 cohort was frozen at commit
`20cc50f82f88f50e7b0dca71ec843d7ca28b647a`. The audit found sixteen reusable
commissioning or handoff cohorts. Four are revised, seven retain their exact
controls, and five remain behind named evidence or design gates.

The revisions are narrow. Outcome 3 already revised the multistage writer.
Outcome 4 removes repeated generic parent-lifecycle and no-nested-delegation
text from the warning-fix and standalone compression-review surfaces, whose
workers receive verified root Commonplace doctrine. It also corrects one
Second Brain example that described task evidence as if it excluded ambient
project instructions. Exact task purpose, inputs, write ownership, acceptance,
return, and failure controls remain local.

No broad packet format, schema, runtime branch, or checked-text reuse mechanism
is added. The audit does not reopen exact protocols merely because they contain
more words.

## Frozen boundary and searches

The sweep covered the 230 tracked files at the frozen commit under
`AGENTS.md`, `AGENTS.md.template`, `kb/instructions/`, `kb/types/`,
`kb/messages/`, `kb/tasks/`, and `src/commonplace/`. Canonical source files
were inspected, not their `.agents/skills/` and `.claude/skills/` symlink
projections. Run-instance messages, generated reports, source ingests,
historical workshops, and vendored artifacts are evidence or task instances,
not reusable packet producers. Active workshop and task *contracts* remain in
scope.

The frozen searches were:

```bash
git grep -Il -E 'delegate|delegation|sub-agent|subagent|worker|handoff|dispatch|spawn|parallel|fresh context' 20cc50f8 -- AGENTS.md AGENTS.md.template kb/instructions kb/types kb/messages kb/tasks src/commonplace
git grep -Il -E 'prompt|brief|packet|plan|checklist|task text|command' 20cc50f8 -- AGENTS.md AGENTS.md.template kb/instructions kb/types kb/messages kb/tasks src/commonplace
git grep -Il -E 'defer|pending|follow-up|future work|revisit|resume|trigger|return condition' 20cc50f8 -- AGENTS.md AGENTS.md.template kb/instructions kb/types kb/messages kb/tasks src/commonplace
git grep -Il -E 'invoke|execute|run-review-batches|cp-skill-|review bundle|review gate' 20cc50f8 -- AGENTS.md AGENTS.md.template kb/instructions kb/types kb/messages kb/tasks src/commonplace
```

They returned 39, 93, 40, and 65 candidate files respectively. Every tracked
instruction and type file was also enumerated, so a surface did not depend on
matching one term. Screening removed criterion bodies, composition callees,
documentation, validation dispatch, ordinary shell launch language, and files
that merely mention agents. The only shipped code that generates a model task
is `src/commonplace/review/protocol/prompt.py`.

Files added after the frozen commit belong to follow-up unless they invalidate
the shared doctrine. No such file appeared before this audit began.

## Delivery baseline used by the audit

Codex fresh workers receive root `AGENTS.md` as binding repository instruction.
Native Claude Code 2.1.251 non-fork `general-purpose` workers receive the same
text through `CLAUDE.md` → `AGENTS.md`. The audit treats only those direct
paths as verified. Commonplace code creates and finalizes review jobs but
launches no model runtime, so generated review prompts retain their
self-contained controls.

A Bash-launched agent process, different working directory, custom agent
definition, remote isolation, or another harness is not covered. A packet on
one of those paths must carry every relied-on rule until that path is verified.
Mailbox messages remain self-contained by default because their recipient path
may be unknown.

## Disposition records

Each record names the baseline, task intent and acceptance, inherited choices,
delegated choices, retained exact controls, and any gap. `Retain exact` means
the current wording has a task-specific or protocol reason. `Defer behind
evidence` keeps the current bytes and names what would reopen them.

### Workshop commissions — retain exact

- **Baseline:** The executing session's verified Commonplace doctrine, then
  `kb/work/COLLECTION.md`.
- **Intent and acceptance:** The framing states the question, who posed it,
  what would close it, and any evaluation or coordination premises a later
  session cannot reconstruct.
- **Inherited choices:** Parent scheduling, integration, recovery, and no
  unauthorized nested delegation.
- **Delegated choices:** Routes, methods, and later decisions for which the
  framing names discriminating evidence or bounded authority.
- **Exact controls retained:** Task authority, owned mutations, accessible
  inputs, cross-work coordination, acceptance, and return conditions.
- **Gap and disposition:** None found. Individual workshop files are task
  instances, not standing producers; retain the contract exact.

### Mailbox requests — retain exact

- **Baseline:** None by default. A message may name a verified recipient path.
- **Intent and acceptance:** The request states the result and what it is for,
  its verification, and its return channel.
- **Inherited choices:** Only rules delivered on the named verified path.
- **Delegated choices:** Consequential choices the request deliberately leaves
  to the recipient.
- **Exact controls retained:** Authority, owned outputs, inputs, coordination,
  and stop conditions. Posting neither launches an agent nor grants authority.
- **Gap and disposition:** None found. Cross-session and cross-harness transport
  makes the conservative self-contained rule necessary.

### Source-checkout task documents — defer behind subsystem design

- **Baseline:** A future agent's repository doctrine plus the applicable
  `kb/tasks/types/` task contract; `kb/tasks/` is an operational, source-only
  surface without a collection contract.
- **Intent and acceptance:** Active tasks carry a goal, prerequisites, context,
  decisions, next steps, and current state; recurring tasks carry scope,
  procedure, and output location.
- **Inherited choices:** Repository authority and normal parent lifecycle.
- **Delegated choices:** Execution route where the task's current state leaves
  it open.
- **Exact controls retained:** Task-specific decisions, triggers, verification,
  and durable run-log destinations.
- **Gap and disposition:** Whether this subsystem should ship or remain
  source-only is unsettled, and current backlog files are already complete.
  Do not redesign its templates until that ownership decision is made.

### Multistage writing — revised in Outcome 3

- **Baseline:** Verified Codex and native-Claude root doctrine, the instruction
  collection and type contracts, the invoked skill, and its promotion
  reference.
- **Intent and acceptance:** Produce one grounded artifact through isolated
  reconstruction, staged authorship, exact-byte independent review, and guarded
  promotion.
- **Inherited choices:** Generic parent scheduling, integration, recovery, and
  no unauthorized nested delegation.
- **Delegated choices:** Investigative sequence, reconstruction form,
  disposition form, decomposition, examples, and prose inside fixed evidence
  and result boundaries.
- **Exact controls retained:** Per-role inputs and outputs, incumbent isolation,
  grounding, invalidation, one repair, accepted digest, drift, mutation,
  rollback, and user-decision boundaries.
- **Gap and disposition:** None. Four fresh evaluators found no behavioral
  divergence; the lean revision was adopted at commit `20cc50f8`.

### Source ingest and re-ingest — retain exact

- **Baseline:** Verified root doctrine plus `cp-skill-ingest`, its standalone
  `draft-ingest-report.md` worker instruction, source contracts, and the
  composition-owned `re-ingest.md` route.
- **Intent and acceptance:** Produce one current analysis from one exact
  snapshot while preserving snapshot identity and retained Quotes bytes.
- **Inherited choices:** Generic parent lifecycle and default denial of
  unapproved nested delegation.
- **Delegated choices:** Source analysis, value selection, and prose within the
  snapshot, connect report, occasion, and artifact contract.
- **Exact controls retained:** Clean context, fixed paths, checksum guards,
  opaque Quotes, one worker replacement, byte backup and restore, anti-skill
  recursion, sole output, and validation. The optional `occasion` already
  carries task-specific intent without contaminating source classification.
- **Gap and disposition:** None in the drafting handoff. `re-ingest.md` is a
  composition caller, not a second worker packet. The prior kept-exact
  disposition still applies.

### Agentic-system lens workers — defer behind the active result-shape design

- **Baseline:** Verified root doctrine plus `analyse-agentic-system`, one frozen
  evidence boundary, its canonical records, and the invoked epistemic method.
- **Intent and acceptance:** Emit one bounded system synthesis with a mandatory
  runtime account and both proportionately scoped lenses.
- **Inherited choices:** Generic parent lifecycle and no unauthorized nested
  delegation.
- **Delegated choices:** Lens depth, targeted reads inside the frozen boundary,
  and analytical organization consistent with the canonical record set.
- **Exact controls retained:** One revision, source register, ID ownership,
  correction/invalidation rules, no evidence upgrades, both lens outputs, and
  prevented-conclusion limits.
- **Gap and disposition:** The skill deliberately leaves physical result layout
  open, so a reusable concrete lens-output packet would choose an output shape
  the active `kb/work/analyse-agentic-system/` migration still owns. Keep the
  current topology exact and defer packet templating until that design settles
  or a failed handoff demonstrates a narrower repair.

### External-literature bilateral isolation — retain exact

- **Baseline:** Verified root doctrine, the multistage skill, the literature
  instruction, and `cp-skill-ground` with its authorized ingest chain.
- **Intent and acceptance:** Decide the smallest faithful artifact disposition
  from direct claim-grained source evidence.
- **Inherited choices:** Parent lifecycle and default no-nested-delegation
  outside the explicit grounding exception.
- **Delegated choices:** Source candidacy inside the fixed search boundary,
  direct-evidence reconstruction, and isolated comparison judgment.
- **Exact controls retained:** Conditional trigger for bilateral isolation,
  three named outputs, target/source blindness, exact grounding caller,
  admitted-source authority, mutation ownership, and user approval for an
  agent-nominated URL. The `cp-skill-ground` → ingest chain is an explicit
  nested exception, not authority inferred by a worker.
- **Gap and disposition:** The earlier nested-authority concern is closed by the
  live role and composition text. Retain exact.

### Warning-fix sweep — revise

- **Baseline:** Verified root doctrine plus `FIX-SYSTEM.md`, the sweep, and the
  per-note fix instruction.
- **Intent and acceptance:** Apply current warn findings to disjoint notes,
  produce an auditable fix report, validate each note, and return substantive
  choices instead of deciding them in a worker.
- **Inherited choices:** Parent scheduling, integration, recovery, and no
  unauthorized nested delegation.
- **Delegated choices:** Minimal wording fixes and strategy classification
  within each note's exact warning set.
- **Exact controls retained:** Queue freshness, disjoint note/report paths, sole
  writes, input scope, validation and return, anti-orchestration rule,
  substantive-decision stop, single-use lifecycle, and parent diff review.
- **Gap and disposition:** None. Remove only the repeated generic lifecycle and
  no-delegation wording; the root rules arrive on both supported worker paths.

### `revise-note` tag follow-up — retain exact

- **Baseline:** Verified root doctrine plus the revision instruction and the
  current note/tag contracts.
- **Intent and acceptance:** Reconcile only the exact navigation surfaces made
  stale by an already-authorized tag change.
- **Inherited choices:** Parent lifecycle and no unauthorized nested
  delegation.
- **Delegated choices:** A settled disjoint follow-up only when independent
  judgment or parallel capacity has a named benefit.
- **Exact controls retained:** Parent-held rationale, exact affected paths and
  deltas, authority before external edits, validation, return, and stop.
- **Gap and disposition:** None. The surface already treats delegation as a
  task-specific delta and does not repeat generic rules.

### Standalone compression review — revise

- **Baseline:** Verified root doctrine plus the complete packet assembled from
  the captured note text, four criteria, synthesis instruction, and output
  contract.
- **Intent and acceptance:** Produce one disposable, report-only compression
  assessment over authoritative captured bytes.
- **Inherited choices:** Parent lifecycle and no unauthorized nested
  delegation.
- **Delegated choices:** Criterion application, cross-finding synthesis, and
  analytic route.
- **Exact controls retained:** Criterion order, captured-byte authority, sole
  output, no live-note or review-store mutation, report grammar, fresh
  independence, and single-use closure.
- **Gap and disposition:** None. Remove only the repeated `or delegate` phrase;
  the independent reviewer still has no delegation authority through root
  doctrine.

### Standalone critique, friction, and premise checkers — retain exact

- **Baseline:** Verified root doctrine plus the selected checker instruction
  and caller-supplied target/output destination.
- **Intent and acceptance:** Produce routed adversarial attention without
  editing or accepting the note. Each method has its own exact result shape.
- **Inherited choices:** Parent lifecycle and no unauthorized nested
  delegation.
- **Delegated choices:** Objection, counterexample, and inferential-joint search
  within the method's test.
- **Exact controls retained:** Fresh independence, report-only mutation,
  no-verdict boundary where applicable, skeptical defaults, output shape, and
  single-use lifecycle.
- **Gap and disposition:** None. These controls create decorrelation and are not
  generic packet ceremony.

### Full improvement pass — defer behind its state-machine audit

- **Baseline:** Verified root doctrine plus the full-pass instruction, report
  schema, method siblings, generated review prompts, and deterministic guards.
- **Intent and acceptance:** Select a warranted contribution, apply only a
  bounded `keep` edit, and close with exact review, one recovery, or rollback
  and author hand-back.
- **Inherited choices:** Generic parent lifecycle and no unauthorized nested
  delegation.
- **Delegated choices:** Independent method judgment and the bounded copyedit's
  local flow choices.
- **Exact controls retained:** Captures and hashes, phase transitions,
  ownership lock, job grouping, author-owned claim boundary, copyeditor packet,
  closing suite, recovery count, guard, and rollback.
- **Gap and disposition:** The known source-capture identity question spans the
  wrapper, every report method, concurrent live drift, schema, and recovery.
  Simplification must change that state machine as a unit. Keep bytes exact
  until its active coherence work supplies the decision and failure tests.

### Review-job dispatch and generated prompt — retain exact

- **Baseline:** Verified ambient root doctrine plus the generated prompt, which
  is the complete job-specific contract. Parent conversation is excluded.
- **Intent and acceptance:** Produce one parser-valid block for every persisted
  review pair, then finalize atomically under the selected model partition.
- **Inherited choices:** Ambient repository governance and generic parent
  lifecycle.
- **Delegated choices:** Criterion judgment and permitted linked-artifact reads
  inside the pre-resolved scope.
- **Exact controls retained:** Captured note/criterion bytes, job grouping,
  model-partition selection, exact output path, no other writes, reading scope,
  consumption telemetry, sentinels, result-kind grammar, single-use contexts,
  all-or-nothing finalization, and freshness verification.
- **Gap and disposition:** None. ADR 067 deliberately makes the generated
  prompt self-contained and forbids a second dispatch wrapper. Its
  no-delegation line remains exact because prompt portability and one-file
  authority are part of that accepted protocol.

### Agent-memory review drafting — defer behind a focused recovery design

- **Baseline:** Verified root doctrine plus the local skill's complete drafting
  packet, review type contract, prepared checkout, and later generated semantic
  review prompts.
- **Intent and acceptance:** Produce a code-grounded review at a pinned commit,
  then pass taxonomy QA, semantic QA, and final validation.
- **Inherited choices:** Generic parent lifecycle outside the explicit packet.
- **Delegated choices:** Code reading, trace-learning classification, review
  organization, and prose inside the type contract.
- **Exact controls retained:** Anti-skill recursion, sole review write,
  read-only checkout, pinned citations, no shell-launched agent, worker-side
  validation, archive lifecycle, and parent QA.
- **Gap and disposition:** The incumbent is archived before worker availability
  and a clean replacement are known. A drafting failure can therefore leave no
  active review. Fixing it requires a checked candidate/promotion or exact
  restore protocol, including staged rename recovery; removing duplicated
  packet text does not solve it. Retain bytes and defer until a focused
  failure-path design can exercise those states or the active agentic-system
  corpus migration replaces this workflow.

### AutoReason revision — defer behind versioned protocol evidence

- **Baseline:** Verified root doctrine plus the experimental skill's complete
  role prompts and blind mapping.
- **Intent and acceptance:** Compare incumbent, critic-led revision, and
  synthesis without changing the source until user approval, while routing
  substantive revision outside the prose tournament.
- **Inherited choices:** Repository authority and generic parent lifecycle.
- **Delegated choices:** Role-local critique, revision, synthesis, audit, and
  blind ranking.
- **Exact controls retained:** Seven-role topology, per-role files, balanced
  mappings, parseable decisions/rankings, hard semantic checks, Borda rule,
  rerun bounds, pass budget, fallback incumbent, and user apply gate.
- **Gap and disposition:** No current failure justifies a protocol version
  change. Compression would need isolation, malformed-return, rerun, and
  recovery tests. Retain the versioned algorithm unchanged.

### Second Brain fresh-agent example — revise

- **Baseline:** The fresh worker's ambient project doctrine plus two named task
  artifacts.
- **Intent and acceptance:** Test whether a context summary and `me.md` let a
  fresh worker explain what the operator is trying to do.
- **Inherited choices:** Ordinary repository governance and parent lifecycle.
- **Delegated choices:** How to synthesize the answer from those two artifacts.
- **Exact controls retained:** The read-only boundary, two-file task-evidence
  boundary, and question used as the observable check.
- **Gap and disposition:** “Loaded with only” could be read as excluding the
  ambient project instructions the real harness always supplies. State the
  actual baseline and prohibit opening other task evidence; do not add a new
  evaluation framework to an illustrative recipe.

## Non-surfaces and composition-only hits

- `AGENTS.md`, `AGENTS.md.template`, `kb/instructions/COLLECTION.md`,
  `kb/types/instruction.md`, and `kb/instructions/write-instruction.md` govern
  or generate commissioning artifacts; they are not themselves task packets.
- `cp-skill-ground`, `re-ingest.md`, `cp-skill-connect`, and semantic-QA callers
  invoke a sibling that owns any worker packet. They do not create a second
  commission.
- Criterion bodies and review gates tell an already commissioned reviewer what
  judgment to make. Their caller owns identity, inputs, output, lifecycle, and
  result transport.
- Runtime projections are symlinks to canonical skills. Tests inspect contracts
  but do not commission production workers.
- One-off mailbox messages, workshop prompts, task instances, and retained
  generated reports are governed instances, not reusable producers. Their
  standing authoring contracts are recorded above.

## Complexity account

The operative changes consolidate generic rules into one verified root carrier.
They add no state, branch, handoff, exception, parser field, or runtime test.
The warning and compression packets keep every task-specific control. The
Second Brain edit adds one accurate consumption-path qualification to an
existing evaluation example.

The five deferred cohorts preserve their current bytes. Each deferral names
the evidence or design decision that would reopen it; none is disguised as a
completed simplification.
