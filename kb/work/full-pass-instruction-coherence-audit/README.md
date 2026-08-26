# Full-pass instruction coherence audit

Started 2026-08-26 at the operator's request after
`kb/instructions/run-full-improvement-pass-on-note.md` had accumulated several
new decision branches. The operator asked for self-contradictions, bugs, and
other incoherences to be identified and recorded before further changes make
the workflow harder to reason about.

## Goal and boundary

Make the full-pass procedure one executable state machine whose decision rules,
packet contract, guards, and recovery behavior agree.

This workshop audits the instruction and the contracts it directly invokes. It
does not decide whether the full-pass methodology itself should be retained,
and it does not repair the instruction yet. Deterministic validation is not the
problem found here: `commonplace-validate kb/instructions/run-full-improvement-pass-on-note.md`
passed cleanly on 2026-08-26. The defects below are semantic and operational.

The workshop closes when every major finding has been either fixed or
explicitly rejected, the duplicated rules have one canonical expression, and
the scenario matrix at the end has been exercised against the resulting
procedure.

## Major findings

### 1. Upward reframing is declared but unreachable

The modality branch says reframing runs in both directions: a title hedged below
its warrant should be reframed upward. The rest of the procedure defines a
reframe only as weakening an overreaching title:

- step 8 tells the editor to write the warranted *weaker* claim;
- the packet template asks for a *weaker* claim;
- the Do-not rule rejects every reframe whose strongest objection is not
  `bites`.

An upward reframe normally follows positive warrant, not a biting objection.
It therefore cannot produce a packet that satisfies the current rules.

Repair direction: replace the single overreach branch with a title/update
mismatch decision. A downward reframe requires a biting objection or equivalent
warrant failure. An upward reframe requires affirmative warrant for the
stronger mode and does not require a biting objection. Templates should say
`replacement claim`, not `weaker claim`.

### 2. The required post-reframe operation cannot pass the required guard

A keep reframe edits the source note in step 8. That necessarily makes the live
note differ from the immutable pass-start `source.txt`. The procedure then
requires a later rename and citer reconciliation, but its final Do-not rule
requires a successful `commonplace-guard-full-pass-report` result before *any
packet-driven edit*. The guard can only report `changed` at that point.

The required follow-up is therefore prohibited by the same procedure that
requires it.

Repair direction: either include rename and citer reconciliation in the same
guarded transaction, or retain a canonical final-text capture and define a
second guard against that state. Do not use the pass-start capture to authorize
post-edit follow-up.

### 3. Routed attention is used as an automatic verdict

`composition-friction-gate` and `premise-decomposition-gate` say their product
is routed attention for a human rather than an acceptance or repair verdict.
The full pass repeats that restriction, but then uses premise outcomes as
decision authority:

- `HOLDS` can nullify the independent critique;
- `DEFEATED GLOBAL` can select delete or a keep reframe;
- a keep reframe is then applied automatically in step 8.

Calling this a note-level exception does not preserve the no-verdict boundary.
The same agent still converts the checker result into a consequential editorial
decision. `HOLDS` is especially weak authority: the premise method defines it
only as an active counterexample hunt finding no defeater, not as proof that a
separate objection is false.

Repair direction: choose one boundary. Either require human confirmation before
premise or friction output changes a disposition, or explicitly authorize the
synthesis agent to decide and remove the claim that these results remain
unresolved. Passage-level versus note-level scope does not resolve the
epistemic conflict.

### 4. The equivocation defense permits post-hoc immunization

The bite rule says a counterexample must meet the premise's antecedent under the
note's own definitions. It then says that when no passage fixes the term's
meaning, the missing definition is itself an answerable finding. This allows an
editor to see a counterexample, invent a narrower antecedent, and call the
counterexample an equivocation.

That conflicts with two other rules:

- an answerable objection must be answered from the artifact's own material and
  retained source;
- changing claim scope or a load-bearing precondition is not a hedge.

It also defeats the stated safety argument in
[`sixth-episode-critique-defeats-by-equivocation.md`](../popperian-maintenance-episode/sixth-episode-critique-defeats-by-equivocation.md):
that record says a note that never defined its term cannot use the defense.

Repair direction: allow the defense only when an incumbent passage or
authoritative retained intent already selects the narrower meaning. Otherwise
record an underdetermined term or Open item. A new definition that changes the
claim's extension must go through the same reframe test as any other scope
change.

### 5. Step 9 has no executable copyedit handoff

The execution-role section says only the orchestrator edits the note. Step 9
gives a fresh worker only the current note text and the exact prompt, with no
target path, output path, or return contract. The procedure nevertheless
expects the worker's result to become the stable on-disk note used by step 10.

The same step permits the orchestrator to perform the copyedit directly, even
though the isolation section says step 9 has the strictest isolation and its
worker must be new to the pass. An orchestrator that has synthesized and applied
the packet cannot receive only the note text and prompt.

Repair direction: have the worker write a pass-scoped candidate file. The
orchestrator checks its diff for claim preservation and applies it to the note.
Either remove the direct-orchestrator alternative or explicitly weaken the
isolation invariant.

### 6. An interrupted keep pass has no discoverable state

A keep packet begins with `resolution: not-required` before step 8 edits the
note. Re-entrancy preflight ignores `not-required` packets. No field records
whether the pass is collecting reports, planned, editing, closing, or complete.

An interruption after packet creation can therefore leave a partly edited note
or incomplete closing cycle that the next invocation treats as an ordinary new
baseline. Orphan pass directories created before packet synthesis are also
ignored.

Repair direction: add an execution phase distinct from disposition resolution,
or define deterministic incomplete-directory detection. Re-entry must stop on
or reconcile an unfinished active pass, including a keep pass.

### 7. `rehome` did not propagate through every report contract

Step 7 and the schema correctly require a `rehome` report to start pending. The
instruction's rendered Resolution template says pending only for delete and
merge. Its retention rule likewise names only unactioned delete and merge
packets. [`full-pass-report.md`](../../reports/types/full-pass-report.md) still
documents only delete and merge as pending, although
[`full-pass-report.schema.yaml`](../../reports/types/full-pass-report.schema.yaml)
correctly treats every non-keep disposition, including rehome, as pending.

Repair direction: update the instruction template, retention rule, report type,
and ADR 051 together. Add a regression fixture that renders and retains a
pending rehome packet from the documented template.

### 8. The required final hash has no canonical persistence slot

The synchronization section twice requires the final note SHA-256 to be
recorded before closing jobs are created. Neither packet frontmatter nor the
Closing cycle template provides a field for it. The sixth-episode packet had to
invent `**Final note SHA-256:**`.

Without a validated final hash or capture, later inspection cannot prove that
the direct closing methods and snapshot-anchored review jobs assessed the same
text. It also leaves no usable guard for the post-reframe operation described in
finding 2.

Repair direction: add a canonical final capture and hash, or at minimum a
validated `final_note_sha256` field. If it authorizes later work, a capture is
needed so a changed result can show a diff rather than only refuse.

### 9. Final artifacts are not deterministically validated

The procedure validates the initial packet before editing. It does not run
`commonplace-validate` on the note after the substantive edit and copyedit, and
it does not validate the packet after Open items and the Closing cycle are
appended.

Catalog assays do not replace deterministic schema, link, and required-section
checks. A pass can therefore complete with an invalid note or malformed final
packet.

Repair direction: validate the edited note after step 9 and the complete packet
after step 10. A validation failure should leave the pass incomplete rather
than silently count as a closed cycle.

### 10. The log-based evidence handoff has a producer but no consumer

The bite rule says a `kb/log.md` FIX entry carries a defeated premise with an
answer in place into a later pass because later passes do not read keep packets.
No preflight or synthesis step reads matching FIX entries, and the contribution
rule says not to add an ad hoc history search.

The evidence is written but is not routed into any later execution context.

Repair direction: define a deterministic retrieval step keyed by note identity
and pass ID, or stop claiming that the log carries the evidence. A structured
follow-up field or explicit packet lineage would be less accidental than log
search.

## Additional incoherences

### Collection fit and contribution have contradictory ordering

The fit branch says a misfit *is* rehome before warranted contribution is
selected. The next paragraph says warranted contribution must be written before
choosing any disposition. A split rehome in particular cannot be chosen until
the separable transferable contribution has been identified.

The shortcut that any note describing a specific system fails `kb/notes/` is
also stronger than the collection contract. `kb/notes/COLLECTION.md` allows a
bounded claim about one fixed design when a substantive design-space claim
remains after the local choices are scoped.

### A title finding is also called a Body edit

The reframe heading says an overreaching title is a title finding, *not a body
edit*. The same paragraph and packet contract require the retitle-and-rethesis
to be the first Body edit. The intended contrast appears to be "title-level
finding, not a body qualification."

### The model partition is an undeclared required input

The instruction declares the note path as its first and only argument, but both
review selector commands contain `{model-partition}`. `run-review-batches.md`
says this value is required, has no default, and must not be guessed. The full
pass neither accepts, derives, nor records it.

### Mixed guard failures have no precedence

A merge packet guards both source and target. The guard command reports every
input and returns exit 1 for any nonmatching combination. The procedure says a
`changed` input should supersede the report, while a `missing` or
`corrupt-capture` input requires reconciliation. It does not say what to do when
one result is changed and the other is missing or corrupt.

### Connect is treated as stronger evidence than its contract supplies

`cp-skill-connect` produces a standard-depth candidate-discovery report under
collection-authorized link topology. The full pass says to use it to
"establish" what the KB already supplies and permits a surfaced near-duplicate
to support merge. Candidate discovery can inform that judgment, but it is not
an exhaustive duplicate or ownership proof.

### `Assay` is used for non-assay methods

The Closing cycle table calls every row an Assay, including compression,
composition friction, premise decomposition, and connect. Commonplace reserves
`assay` for snapshot-anchored evaluation through the review job pipeline; each
of those methods explicitly says it is not such an assay.

### A Body edit may say `split` without a split protocol

The packet template permits `split` as a Body-edit action. Applying a real
artifact split requires creating and validating another artifact, selecting its
collection and type, and guarding more than the original note. Step 8 only
defines direct edits to the original note. Split should either be a pending
disposition/follow-up or receive its own transaction contract.

## Cross-cutting cause

The same policy is repeated in the procedural steps, Reconciling disagreement,
the packet template, and the Do-not list. The copies have drifted:

- rehome is pending in one place but omitted in two others;
- reframe is bidirectional in one place but downward-only elsewhere;
- premise findings are unresolved in one place but decisive elsewhere;
- the final hash is required operationally but absent from the packet type.

A safer shape would separate three things:

1. one orchestration state machine for capture, review, edit, close, interrupt,
   and resume;
2. one decision table for fit, update, objection, and disposition;
3. one typed packet contract that carries both disposition resolution and
   execution phase without duplicating its allowed values in prose templates.

## Suggested repair order

1. Decide whether premise/friction findings may drive agent-applied note-level
   changes. This determines the workflow's authority boundary.
2. Define execution phases, final capture, interruption handling, and the guard
   used for post-edit follow-up.
3. Replace the reframe prose with one bidirectional decision table.
4. Repair the equivocation branch so a missing definition cannot select its own
   narrowing.
5. Make step 9's handoff executable and add final validation.
6. Reconcile rehome, model-partition, guard-precedence, and vocabulary drift
   across the instruction, type, schema, ADR, and tests.
7. Remove repeated policy prose after the canonical state and decision tables
   exist.

## Scenario matrix for verification

Exercise each case from a clean source and from an interrupted state where
applicable:

| Scenario | Required observable result |
|---|---|
| plain keep | one guarded edit transaction; validated final note and packet |
| keep with no Body edits | explicit completion without an unnecessary copyedit mutation |
| downward reframe | biting objection, guarded replacement claim, final capture, executable citer follow-up |
| upward reframe | affirmative stronger warrant without a fabricated biting objection |
| answerable objection | answer selected by incumbent material or retained intent; closing attack targets the answer |
| missing definition under counterexample | underdetermined/Open item unless an authorized input selects the meaning |
| `UNDETERMINED` update | byte-identical note and discoverable stopped packet |
| delete | pending packet; no edit; successful guarded resolution path |
| merge | both inputs captured; deterministic mixed-failure precedence |
| whole rehome | pending packet represented consistently in type, template, retention, and resolver |
| split rehome | every new or moved artifact named, guarded as needed, and validated |
| interruption before packet synthesis | orphan run detected or safely reconciled |
| interruption during steps 8–10 | next invocation detects unfinished keep pass rather than silently restarting |
| concurrent edit during closing | closing evidence rejected unless every result matches the canonical final capture |

## Dispositions (2026-08-26, ADR 080)

The operator assigned the repair and chose simplification for finding 3. The decision: the pass no longer changes a note's claim; every claim-level finding is a pending `revise` hand-back (ADR 080). Each finding below is marked against the rewritten instruction.

| # | Finding | Disposition |
|---|---|---|
| 1 | upward reframing unreachable | **dissolved** — no in-pass reframe in either direction; an upward mismatch is `revise` with the stronger mode in the brief |
| 2 | post-reframe follow-up cannot pass the guard | **dissolved** — no in-pass claim change, so no rename follows a pass; the guard now compares each path with its latest capture (`final.txt` after a keep), so post-pass follow-ups on a completed keep have a guard that can pass |
| 3 | routed attention used as a verdict | **fixed** — friction/premise output feeds only the objection question, which can select a hand-back and nothing else; the `HOLDS`-nullifies-critique lever is reduced to "a critique that re-asserts an objection against a held premise does not lower warrant by itself", and no premise result is applied to the note |
| 4 | equivocation defense permits immunization | **fixed by removal** — the clause is gone; whether a counterexample meets the antecedent is the author's judgment in the revise hand-back, and the packet quotes both sides; narrowing a definition in-pass is named a claim change |
| 5 | step 9 has no handoff | **fixed** — worker writes `copyedit-candidate.md`; orchestrator applies the acceptable diff; the direct-orchestrator alternative is removed |
| 6 | interrupted keep pass invisible | **fixed** — `phase` field (`packet`/`editing`/`closing`/`complete`); preflight stops on orphan directories and on keep packets in `editing`/`closing` |
| 7 | rehome not propagated | **fixed** — template, retention rule, type doc, resolve instruction, and ADR 051 amendment all name the four pending dispositions; schema fixture tests cover `revise` |
| 8 | final hash has no slot | **fixed** — `final_capture`/`final_sha256` fields, schema-enforced non-null in `closing`/`complete`; validation verifies the capture hash; the guard uses it |
| 9 | final artifacts not validated | **fixed** — note validated after step 9, packet after each phase change and after step 10 |
| 10 | log handoff has no consumer | **dissolved** — the revise packet is the handoff and preflight reads pending packets; the log clause is removed |
| add. | fit/contribution ordering | **fixed** — contribution first, fit second; a split needs the separable claim from question 1; the system-specific shortcut now states the COLLECTION.md allowance |
| add. | title finding also a body edit | **dissolved** with reframes |
| add. | model partition undeclared | **fixed** — second declared input, recorded in the packet |
| add. | mixed guard failures | **fixed** — reconcile-first precedence stated in the resolve instruction |
| add. | connect as proof | **fixed** — "inform", with the candidate-discovery caveat |
| add. | `Assay` for non-assays | **fixed** — column renamed `Method` |
| add. | `split` body-edit action | **fixed** — removed; split is a rehome remedy |
| cross-cutting | duplicated policy prose | **fixed** — one decision table; "Reconciling disagreement" reduced to passage-level rules; Do-not list reduced to eight non-inferable rules |

Code: `full_pass.py` parses `revise`, the closing state, and a `final` capture role, and guards each path against its latest capture; the schema enforces phase/disposition, final-capture, closing-status, and one-recovery constraints; validation verifies every capture. The focused full-pass suite has 37 tests; the repository suite has 580.

One instrumented run now exercises a guarded `keep` with an answerable
objection, pre-packet orphan detection, closing-phase interruption/re-entry, and
a concurrent-edit mismatch. Still not run: keep with no body edits, `revise`
(each direction), undetermined update, delete, merge with mixed guard failure,
whole and split rehome, an editing-phase interruption, and a successful bounded
closing recovery. The rows for downward/upward reframe now read as `revise`
hand-backs.

## Instrumented keep run (2026-08-26/27)

Pass `20260826T214434Z-8272bf` ran the rewritten procedure over
`kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md` under the
`codex` partition with one pass ID. It began at 21:44:34 UTC and reached a
validated `phase: complete` packet under the then-current contract at 22:29
UTC, about 45 minutes later. The pass used 25 fresh worker executions: 16
snapshot-anchored review jobs, eight direct method workers (compression,
friction, premise decomposition, and connect in both phases), and one copyedit
worker. Each of `initial/` and `closing/` retained 46 reports: 41 catalog gate
results plus critique, compression, friction, premises, and connect.

The substantive branch was `keep` with an answerable objection. The initial
critique and premise hunt raised the counterexample that one cheap artifact can
both nominate an assessment and decide a narrow verdict. Synthesis selected an
answer already implied by the incumbent's first two definitions and its linked
warrant rule: the labels name the authority the evidence currently carries,
not an intrinsic artifact kind, so one item can separately satisfy both roles
without routing authority transferring into verdict authority. The body edit
made that answer explicit, removed the cheapness-as-definition inference,
compressed both witnesses, removed one ungrounded historical claim, and passed
an isolated copyedit candidate through orchestrator diff review. The title and
thesis were not changed.

The interruption and concurrency observations were deterministic:

- After `source.txt` was captured but before the packet existed, re-entry
  inspection found the pass directory without `full-pass-report.md` and
  classified it as an orphan that must stop. `source.txt` and the live note
  both hashed to
  `eff95c5ee6ecdd1d313ab671b836288967041cd7dade7fd0ca6d8024d52dfc96`.
- After copyedit, `final.txt` was written, the packet entered `phase: closing`,
  and the guard compared the live note with that latest capture successfully.
  This exercised discoverable closing-phase interruption and resumability
  before any closing jobs were created.
- A controlled concurrent-edit probe then appended one uniquely named HTML
  comment to the live note. The guard exited 1, reported `status: changed`, and
  returned the exact diff against `final.txt`. Removing the probe restored the
  note byte-for-byte; both paths hashed to
  `32bd38b26793dfdb2702d7be01d9cc89f3dc477a428d2ea9183f7256983856c8`,
  and the guard returned `all_matching: true`. Closing jobs were created only
  after that restoration.

The closing cycle attacked the added answer rather than merely replaying the
initial wording. It preserved the selected update but left material residuals:
critique questioned whether the new distinction adds a prospective
discriminator beyond warrant non-distribution; premise decomposition left two
`DOUBTFUL GLOBAL` pressure points; frontmatter returned one FAIL and one WARN
on the unchanged title's apparent breadth; and sentence review found two real
misleading link texts plus a missing verb introduced by the edit. The latter
made one Pirolli sentence syntactically incomplete even though deterministic
validation remained clean. Per the procedure then in force, all residuals were
routed to Open items and did not start a second edit cycle. The exact failed
sentence, closing verdict, hashes, and state contradiction are retained in
[closing-completion-failure-evidence.md](./closing-completion-failure-evidence.md).

At the time, deterministic checks passed cleanly for the note, its packet, and
both connect reports; the guard reported the live note matching `final.txt`.
That combination is the failure evidence: exact retention and schema validity
did not imply semantic acceptability. This run therefore covers the observable
mechanics of the matrix's guarded keep, answerable-objection, pre-packet
interruption, closing interruption, and concurrent-edit rows, while
disconfirming the old completion rule.

## Post-run closing-state repair (2026-08-27)

The operator accepted one more repair after reviewing this evidence. ADR 080
now makes closing a three-way retention gate:

- `ready` is the only closing status compatible with `phase: complete`;
- `repair-needed` permits one local correction, a new immutable capture, and a
  complete rerun under `closing-recovery/`; and
- `hand-back` covers claim-level failure, a newly introduced angle, or any
  defect remaining after that recovery. It restores `source.txt` before
  stopping.

The packet schema requires `closing_status` and
`closing_repair_attempted`, forbids a second `repair-needed` state, and binds
each status to its legal phase. Claim-level hand-back takes precedence over
local cleanup, so this run's title/body failure makes the historical result a
hand-back even though the missing verb and link texts would otherwise be
locally repairable. The live note is restored to its pass-start text; the
failed final capture and closing reports remain inspection evidence.
