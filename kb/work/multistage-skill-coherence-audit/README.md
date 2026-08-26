# Multistage write skill coherence audit

Started 2026-08-26 at the operator's request, after the full-pass audit and ADR 080, to check whether `kb/instructions/cp-skill-write-multistage/SKILL.md` has the same classes of defect: agent-applied claim repair without the author's theory, unreachable or self-contradictory branches, missing guards and interruption state, and policy stated in more than one place.

Evidence: the skill text (275 lines at audit time, 288 after `c9cdc70e` added a conditional external-literature branch to Step 1; `context: fork`; one `agents/openai.yaml`), the seven run directories under `kb/work/multistage/` (three complete with trial records from 2026-08-20, one active edit-mode run from 2026-08-26, one stalled at brief from 2026-08-14, two empty), the two proposals that call the skill "new and untested", and the ADR 080 record.


## Goal and boundary

Same as the full-pass audit: make the procedure one executable state machine whose decision rules, stage contracts, guards, and recovery behaviour agree. This workshop audits the skill and the contracts it invokes; it does not decide whether the multistage path should be retained, and it does not repair the skill. Deterministic validation is not the problem: the skill validates. The defects are semantic and operational.

## Where the skill is already ahead of the full pass

State this first, because it bounds the findings. The full pass reconstructed what a note was for from the note's own text and could not extend its evidence, so repair was subtractive and drifted (six episodes). The multistage skill was designed around both gaps:

- **The commission is fixed before any prose exists.** `brief.md` (Step 3) carries the governing question, the user-supplied claim "without expanding it", the reader, and the retained intent with its source and role — before reconstruction. Every later stage is audited against the brief and the skeleton, not against the incumbent. This is the reference point the full pass lacked.
- **Evidence can be extended, and its absence blocks.** Step 3 acquires or ingests inputs; Step 10 invokes `cp-skill-ground`; a claim the governing question needs but the evidence cannot support is a *blocking* gap that stops the run, not a reason to narrow the claim. The evidence-scope escape is closed by construction.
- **Claim changes have a decision gate.** Step 5 records `DECISION NEEDED: central contribution` and asks the user when task and evidence do not determine the claim; folds into other artifacts and additional artifacts also ask.
- **Additions are tracked, not silently made.** `NEW COMMITMENT FOR AUDIT:` markers, the claim-delta audit, and the `keep` finding that must name its basis.

The findings below are therefore narrower than the full pass's. None reproduces the drift mechanism; most concern edit mode, guards, and lifecycle.

## Major findings

### 1. Edit mode can replace the incumbent's claim without an explicit decision

The decision gate fires when "the task and evidence do not determine which of several claims is central." When the sources determine one central claim and it differs from the incumbent's title-level claim, no gate fires: the source-first disposition names the new contribution, the incumbent reconciliation disposes the old claim (`omit/retain in workshop` is available for an unsupported commitment "when the governing question and supplied intent do not require it"), and the run proceeds to draft the replacement. The incumbent "is not evidence for that claim" — correct — but its author's claim is then replaced on the strength of whichever sources the brief happened to list, under a governing question the orchestrator wrote.

The active run shows the intended path working: its README records that the user selected the relocation candidate and accepted the reframe, and its brief's governing question already encodes the new claim ("why must … be evaluated across the whole path"). But that decision is recorded by good practice, not required by the text. ADR 080 settled the neighbouring case for the full pass: a claim change is the author's decision.

Repair direction: in edit mode, when the source-first central contribution differs from the incumbent's title-level claim in strength, direction, scope, modality, or category, record `DECISION NEEDED: claim replacement` naming both claims, and stop before Step 6 unless the brief already carries an explicit user direction to replace the claim. Treat a governing question that presupposes the replacement as that direction only when the user wrote it.

### 2. A retitled edit-mode target has no relocation step

Step 1 fixes the run key and lets the "current intended target" change when the final title changes the destination. Step 10 then says "write `candidate.md` to the resolved target path" and, for a *new* artifact, derive a filename. Nothing says what happens to the incumbent file, its inbound link paths, or the redirect map when an edit-mode target moves — which is exactly the active run's situation (run key `charting-the-knowledge-access-problem-beyond-rag.md`, current target `knowledge-access-architecture-must-be-evaluated-end-to-end.md`). Writing the candidate to the new path leaves the old file in place, no redirect, and six inbound consumers pointing at the old claim — the run's own pending handoff.

Repair direction: before the promotion write in edit mode with a changed target path, relocate the incumbent with `commonplace-relocate-note` as a pure relocation (own commit), then write the candidate over the relocated file. Citer link-text reconciliation stays a handoff; path rewriting and the redirect do not.

### 3. Promotion has no live-target guard

`original.md` is captured at Step 1; runs span hours to days (the stalled 2026-08-14 run still holds its `original.md`); nothing compares the live target with `original.md` before the promotion write. A concurrent edit to the incumbent — this repository runs several sessions at once, and today's full pass recorded exactly such a collision — is silently overwritten. The rollback rule ("restore `original.md` byte-for-byte") would then restore a stale text.

Repair direction: record the incumbent's SHA-256 in `README.md` at Step 1; before the promotion write, compare the live target with `original.md` and stop on mismatch. The full pass's `commonplace-guard-full-pass-report` is packet-specific; a hash check in the skill is enough here.

### 4. `context: fork` contradicts the fresh-context precondition for the orchestrator

The skill requires fresh sub-agent contexts and says "do not imitate source-first independence in a context that has already read the incumbent draft." It runs as a fork, so the orchestrator inherits the invoking conversation — which, in edit mode, has usually just read or discussed the incumbent. The sub-agents are fresh (Task), but the orchestrator writes `brief.md`, and the brief's "target claim or purpose supplied by the user, without expanding it" is where an orchestrator that has read the incumbent leaks the incumbent's framing or its own proposed reframe into the commission the fresh reconstruction is then held to.

Repair direction: require the brief's governing question and target claim to be quoted from the user's words or from a named retained-intent input, with the source marked; anything the orchestrator adds is labelled as its own proposal and is not binding on reconstruction. Alternatively declare the orchestrator's context non-fresh in the text and confine independence claims to the sub-agents.

### 5. Every user decision invalidates reconstruction

Step 5's closing rule — "Because the brief or target inputs changed, uncheck reconstruction and every dependent stage, then resume at Step 4" — is attached to the retargeting paragraph but the Verify list generalizes it: "a direction added to the brief after a user decision caused reconstruction and every dependent stage to be rebuilt." A choice between two central claims changes the commission, not the sources; the reconstruction is source-only by design and does not depend on which claim was chosen. Rebuilding it costs a fresh 30–50 KB sub-agent run (the observed sizes) for no new information, and the text is ambiguous about whether it is required.

Repair direction: one invalidation table — sources or governing question changed → from Step 4; central claim, fold, or artifact-set decision → from Step 5; target identity/mode/collection/type changed → from Step 1. Delete the Verify bullet or restate it to match.

### 6. Abandoned and empty runs are invisible to resume

Step 2 resumes a run whose README run key matches; an empty directory (`multistage-write-eigenius-20260818/`, `multistage-write-adr-073-rollout-evidence-20260825/`) has no README and matches nothing, so a rerun on the same target creates a `-2` directory and the orphan persists. A run stalled at `brief.md` for twelve days (`select-call-cordis-20260814`) is "unfinished" and would be resumed silently. Nothing distinguishes an orphan, a stalled run, and an active run.

Repair direction: treat a run directory without `README.md` as an orphan (stop; delete or complete), and record a `last-advanced` date in the README so a stale run is surfaced for a decision rather than resumed.

### 7. The acceptance trigger is not decidable

"For public-facing, high-stakes, causal, or quantitative work — or whenever the audit found material drift" — four undefined predicates decided by the orchestrator, recorded in README as required/not required. Every retained run marked it required, which suggests the branch is not discriminating. If acceptance is always run, say so; if not, the trigger needs a checkable form (type, collection, or an audit-finding count).

### 8. Promotion deletes the decision record

Successful promotion removes the workshop unless the user asked to retain it, so `brief.md` (the commission, the retained intent with its sources and roles, the user decisions) is gone; the proposals already note that "successful promotion normally deletes the workshop." The commit message is the only surviving record, and the skill says nothing about committing. Under ADR 074 git is the change-history layer, so the repair is small: the skill's final report must carry the commission, the decisions, and every `quotes added` result in a form the operator can paste into the commit body.

## Additional incoherences

- **Step 1 "prefer revising a near-duplicate" has no path.** Switching a new-write run to edit mode on the near-duplicate changes target identity, mode, and possibly type; the text says only to prefer it. It should route through the Step 1 re-resolution the Step 5 retarget paragraph describes.
- **Near-duplicate searches in Step 5 can leak the incumbent.** The architect is told not to open the target, but notes that cite the incumbent paraphrase its claim in their link text and summaries; the search is not scoped away from them. Small, and probably acceptable; worth a sentence.
- **`ask user` inside a fork.** Steps 3, 5, and 9 "ask the user" and "stop"; a forked background skill cannot ask interactively, so asking means ending the run with the marker and relying on Step 2 resume. That is workable but unstated; the text should say a decision marker ends the run and names the resume step.
- **Two `DECISION NEEDED` homes.** Markers live in `brief.md`, `claim-disposition.md`, and `README.md`; Step 5 says to clear the marker in README and add the direction to the brief, but not to clear it in `claim-disposition.md`, which is then "invalidated" — the rule works only because the file is regenerated. State it once: markers live in README; stage files quote them.
- **`Status: blocked` has no exit.** Step 9 allows `blocked` findings; Step 10 forbids promotion while any is blocked; nothing says how a blocked finding becomes resolved (evidence acquired → Step 4; user decision → Step 5). Cross-reference the invalidation table from finding 5.
- **Source-guard block duplicates `cp-skill-write` Step 7.** The grounding paragraphs in Step 10 restate ADR 078's writer-side guard. One canonical statement (in the write skill or a shared instruction) with a pointer would keep the two from drifting — today's full-pass audit found exactly this class of drift.

## What this audit does not find

No self-contradiction of the reframe kind (a repair declared possible that no packet could express), and no place where a checker's output is converted into an applied edit by the same agent without a reference point: the audit's recommendations are resolved by the orchestrator against the brief and skeleton, and an unresolved or blocked finding stops promotion. The skill's authority boundary is coherent; its gaps are guards, lifecycle, and the one edit-mode decision that is practised but not required.

## Suggested repair order

1. Finding 1 — the edit-mode claim-replacement gate; aligns the skill with ADR 080 and costs one paragraph.
2. Findings 2 and 3 — relocation step and live-target hash guard; both bite on the active run.
3. Finding 5 with the `blocked` exit — one invalidation table.
4. Findings 4, 6, 7, 8 and the fork/ask-user wording.
5. Deduplicate the source guard against `cp-skill-write`.

## Scenario matrix

| Scenario | Required observable result |
|---|---|
| new write, one determined claim | brief quotes the user's commission; reconstruction never sees a draft; promotion validates |
| new write, two candidate claims | `DECISION NEEDED: central contribution` ends the run; resume regenerates from Step 5, not Step 4 |
| edit, same claim, better evidence | incumbent reconciled; no claim-replacement marker; live-target hash matches at promotion |
| edit, sources support a different claim | `DECISION NEEDED: claim replacement` unless the brief carries the user's direction |
| edit with retitle | pure relocation commit precedes the promotion write; redirect present; link paths rewritten; citer text a handoff |
| concurrent edit to the incumbent during the run | promotion refused on hash mismatch; workshop retained |
| missing evidence the question needs | run stops at Step 3/5 with the exact evidence gap; no narrowed claim |
| orphan directory / stalled run | detected at Step 2, not silently resumed or duplicated |
| audit finding blocked | named exit (evidence → Step 4, decision → Step 5); promotion refused meanwhile |
| promotion then workshop removal | final report carries commission, decisions, and quotes-added results for the commit body |

## Outcome of the active edit-mode run (2026-08-26, evening)

The `knowledge-access-architecture` run completed in the other session after this audit was written. What it shows against the findings:

- **Finding 2 (no relocation step) — confirmed, and worked around by hand.** The operator's session relocated the incumbent first as a pure commit (`c63fca67`: "Move one note, update six tracked Markdown consumers, and add its published redirect. Keep the note body unchanged so the substantive reframe follows separately"), then promoted the candidate (`e4a9d0ee`). That is exactly the repair direction; the skill text still does not say it.
- **Finding 3 (no live-target guard) — untested.** No concurrent edit hit the incumbent during the run, so nothing was overwritten; the guard is still absent.
- **Finding 1 (claim replacement) — practised, not required.** The decision is recorded in the run's README and in the operator's session, nowhere the skill demands.
- **Finding 8 (decision record deleted) — confirmed.** The run directory was consumed (an empty `source-originals/` shell remains, a git leftover); the two commit bodies carry a one-line summary each, not the commission, the retained-intent inputs, or the user decisions. The evidence that would let a later reader reconstruct why the claim changed is gone.
- **Finding 6, corrected.** The empty run directories (`eigenius-20260818`, `adr-073-rollout-evidence-20260825`, now `knowledge-access-architecture-20260826/source-originals`) are git leftovers — git removes tracked files, not directories — rather than abandoned runs. They still trigger Step 2's `-2` suffix rule on a rerun, so the repair (treat a README-less directory as an orphan and delete it) stands, with the cause named.
- **New since the audit.** `c9cdc70e` adds a conditional branch to Step 1 that loads `assess-a-claim-bearing-artifact-against-external-literature.md` as "the governing source-selection and disposition contract" for literature-disposition tasks. That is a second procedure governing the same run, layered by prose condition — the policy-in-two-places shape the full-pass audit found. Not a defect yet; a watch item for the next revision.

Findings 1–4 remain edit-mode-specific; 5–8 apply to new writes. Repair is deferred until the operator decides whether edit mode is a supported use.
