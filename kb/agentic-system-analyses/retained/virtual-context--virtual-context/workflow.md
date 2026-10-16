---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Virtual Context engagement workflow from caller-supplied memory candidates through verification, bounded drafting and optional staging delivery."
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
reviewed-boundary: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
---

# Virtual Context workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the optional engagement runner: an external caller asks `run_once` to turn retained-message retrieval results into one follow-up question, normally a dry-run report and optionally a staged message. It was selected because it joins model-dependent qualification and drafting, independent source checks, rejection recovery and an outward effect in one shipped orchestration function. It does not stand for every chat, proxy or maintenance path. The enclosing route is [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage); its supplied model roles are [RT-CMP-engagement-models](runtime.md#rt-cmp-engagement-models).

All new inspection is implementation evidence from SRC-1 at the boundary revision. Added coverage comprises `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/candidates.py`, `virtual_context/core/engagement/verify.py`, `virtual_context/core/engagement/live_source.py`, `virtual_context/core/engagement/compose.py`, `virtual_context/core/engagement/select.py`, `virtual_context/core/engagement/poster.py`, qualification in `virtual_context/core/engagement/continuation.py`, repetition checks in `virtual_context/core/engagement/history.py`, and the gate function in `virtual_context/core/engagement/fidelity.py`. No target execution or run artifact was inspected. Wiring supports the sequence below, not successful delivery, source truth, reliable model judgment or improved community engagement.

### Request, identities and first handoffs

The caller supplies retrieval results, attested source records, sender labels, an allowlist, posting history, time, conversation ID and the qualifier, drafter and source-fetcher callables. A sender and `post=True` are additionally needed to attempt outward delivery. The runner schedules nothing and owns no transport credential. It controls ordering, not the internal implementation of arbitrary supplied callables. SRC-1, `virtual_context/core/engagement/runner.py` states:

> Dry run is the default and posting is a separate, explicit argument. A caller
> that forgets the flag produces a report and sends nothing, which is the
> behaviour you want from the mistake that is easiest to make.
> --- `virtual_context/core/engagement/runner.py`

Collection converts retrieval results into candidate objects, retaining canonical-turn, source-message, actor and channel identities, text and decoded send time. It requires requester provenance, a sourceable channel and a timeable message ID; it removes a known sender prefix from the body. The default collection deduplicates by message ID before verification. Thus the verifier's contradiction sweep applies to the surviving candidates and associated records, not necessarily every contradictory retrieval row. This bounds the runtime baseline's general description of source verification. SRC-1, `virtual_context/core/engagement/candidates.py`, `virtual_context/core/engagement/verify.py`:

> if dedupe and message_id in seen:
>     _reject("duplicate_source_message_id", f"message_id={message_id}")
>     continue
> --- `virtual_context/core/engagement/candidates.py`

The verifier rejects missing attestation, message-ID mismatch, author mismatch and channel mismatch. These compare caller-supplied canonical and source records; they do not authenticate the original ingestion or compare live message content. Each rejection carries the canonical turn, stage, reason and optional detail. Verified candidates alone cross the next handoff to the qualifier. SRC-1, `virtual_context/core/engagement/verify.py`, `virtual_context/core/engagement/runner.py`:

> qualified, qualify_rejections = qualifier(verified, now=now)
> rejections += list(qualify_rejections)
> --- `virtual_context/core/engagement/runner.py`

The bundled qualifier illustrates the expected structure without proving that every supplied callable uses it. It labels eligible recent items `timed`; otherwise it seeks a continuation hook and labels it `personal`. It attaches hook evidence and stance after checking later-thread state. These fields travel on the candidate rather than being recomputed during composition. SRC-1, `virtual_context/core/engagement/continuation.py`, `virtual_context/core/engagement/compose.py`. This is functional delegation through callables, not evidence of separate autonomous agents or isolated subprocess contexts.

### Selection, live evidence and model handoff

Before ranking, the runner checks posting history for reused threads, actor cooldown and applicable destination-channel limits. Question similarity runs later because the draft does not yet exist. The history is consequently behavioral state: records from earlier invocations can veto a candidate or draft in this invocation. Ranking orders survivors by a cheap text-specificity score and stable canonical-turn tiebreak. The runner does not supply the ranking function's optional recent-actor/channel arguments. SRC-1, `virtual_context/core/engagement/history.py`, `virtual_context/core/engagement/select.py`, `virtual_context/core/engagement/runner.py`.

Each draft attempt first calls the live-source selector. Its default walk checks at most three candidates per call and returns the first passing candidate. A fetch exception, rate limit or unreachable source blocks further walking in that call; deletion or an edited marker can reject one candidate and allow another. The check requires a successful response, an author ID matching the actor suffix and, when supplied, matching channel ID. It does not compare body text, and it does not check the timestamp against the stored timestamp. A successful result therefore supports these specific checks, not exact quote equivalence. SRC-1, `virtual_context/core/engagement/live_source.py`:

> if payload.get("edited_timestamp"):
>     return LiveVerification(
>         False, LIVE_EDITED, str(payload.get("edited_timestamp")),
>     )
> --- `virtual_context/core/engagement/live_source.py`

The runner then passes only the selected candidate to the drafter. The bundled composer supplies quote, handle, stance guidance, channel label, send time and tone constraints to its injected composer; continuation composition additionally supplies the retained hook and verbatim evidence. This limits model-visible work to one selected item and its supplied framing rather than the full candidate pool. There is no separate context-frame teardown or automatic reload mechanism in this runner. Candidate selection is distinct from removing older turns in chat context. SRC-1, `virtual_context/core/engagement/compose.py`, `virtual_context/core/engagement/runner.py`.

The drafter returns a draft and fidelity verdict. The supplied gate function asks a judge about quote and draft and maps errors/unreadable answers to a negative verdict, but the runner does not itself require that supplied drafters call this function. More importantly, runner admission has a type-dependent gap: the selection helper applies its negative-verdict veto only to `personal`, not `timed`. The bundled qualifier can produce both. [WF-RTE-draft-selection](#wf-rte-draft-selection) establishes the exact acceptance and recovery boundary. The runtime record's broad fidelity-gate description must be read with this qualification; it is not a universal rejection guarantee.

### Recovery, effect and delivered result

A re-paste request, repeated draft, empty text or applicable fidelity rejection advances the walk to the next ranked candidate. There are at most three draft attempts, with live verification repeated for each attempt. The cap counts drafts, not all live-source fetches. Exhaustion returns a report with `every_draft_rejected` if a draft was attempted, otherwise `no_verified_candidate`. Rejections remain available in the returned report/result. This is bounded candidate fallback, not revision of the same draft under criticism. Arbitrary qualifier/drafter exceptions are not caught by `run_once`; the bundled composer handles its own composer-call errors, but absence of a configured composer raises. SRC-1, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/compose.py`.

An accepted dry run returns the report and `dry_run` refusal marker without calling the sender. With explicit posting intent, the poster separately enforces shipped posting enablement, staging destination, matching-message live verification, day availability and nonempty question. The runner constructs its verification token from the chosen candidate after selection; this is an internal sequencing assertion, not an unforgeable transport attestation. See [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage), SRC-1, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`.

The poster records a pending claim before calling the sender with delivery body, destination, reply-reference and mention metadata. Repetition uses the question text rather than its presentation wrapper. After a nonempty returned message ID, it updates that claim to `staged`, with a staged-message ID, then returns through `RunResult.posted_message_id`. That field's name does not mean community publication. SRC-1, `virtual_context/core/engagement/poster.py`:

> history.update(handle, staged_message_id=message_id, status="staged")
> day = now.astimezone(ZoneInfo(POSTING_ZONE)).date().isoformat()
> return PostResult(message_id=message_id, channel_id=channel_id, day=day)
> --- `virtual_context/core/engagement/poster.py`

If a day claim loses a race, the poster converts `DayAlreadyClaimed` to `PostRefused`; the runner returns its reason. An empty sender result also becomes `PostRefused`, leaving the claim pending because the send may have landed. There is deliberately no automatic retry of pending sends; `pending_claims` exposes them for human resolution. Other sender or history exceptions are not universally converted into reports by this sequence. Claim strength depends on the supplied history implementation; sender conformance, transport receipt and database/transport atomicity are not established. SRC-1, `virtual_context/core/engagement/poster.py`; the minimum claim-before-send failure passage is retained in [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage).

Thus delivery at this inspected boundary means a returned report, or a sender-acknowledged staging message plus successful ledger update. Community publication, owner review and external scheduling are not established by this workflow trace. No expected-answer oracle is used: stored source identity and live metadata checks are evidentiary checks; fidelity is model judgment, not a known correct answer.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-draft-selection
Label: Draft selection and bounded fallback

Part of: [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage)

This is the material draft-admission subroute within the supplied engagement container, not a second identity for the whole workflow. Endpoints: ranked candidates → per-attempt live check → candidate-only drafter call → re-paste/similarity/fidelity selection → chosen draft or exhaustion report. Runner code owns progression and final acceptance; the supplied drafter proposes text and a verdict. SRC-1, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/select.py`.

- Immediate return: chosen candidate, draft, verdict and outcome to the enclosing runner, or exhaustion leading to a refusal/report.
- Later read-back: an admitted question can enter the poster's history ledger and constrain future candidate/draft admission; a dry-run draft is only returned, with no ledger write by this runner.
- Delegated visibility: drafter receives the selected candidate, not the ranked pool or history; internal model visibility depends on the supplied callable, with bundled composition using quote and structured framing.
- Selection predicate: live-pass candidate, non-re-paste draft, no question-similarity rejection, nonempty text and non-skip outcome; negative fidelity verdict changes the outcome only when its kind is `personal`.
- Invalidation or expiry: rejection abandons this candidate and advances to later-ranked candidates; at most three draft attempts per invocation; history windows constrain later repetitions.
- Activation or effect: accepted draft reaches report construction and, with posting intent and poster guards, an outward sender; no observed model compliance or resulting engagement effect.
- Evidence limits: caller-supplied qualification/drafting internals are opaque; static code establishes a timed-type veto bypass, not a demonstrated unfaithful post or deployment incidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The load-bearing branch is explicit:

> if outcome.kind != "personal":
>     return outcome
> if any(getattr(v, "faithful", False) for v in (verdicts or [])):
>     return outcome
> --- `virtual_context/core/engagement/select.py`

The caller checks the resulting outcome and draft text rather than independently checking `faithful`:

> if attempt_outcome.kind != "skip" and (attempt_draft.text or "").strip():
>     chosen = candidate
>     draft, verdict, outcome = (
>         attempt_draft, attempt_verdict, attempt_outcome,
>     )
>     break
> --- `virtual_context/core/engagement/runner.py`

The bundled qualifier supplies the bypass-relevant type:

> question_type = "timed"
> hook_kind = ""
> hook_evidence = ""
> if not timed_ok:
> --- `virtual_context/core/engagement/continuation.py`

Admission is software/model-controlled, not per-draft human approval. Caller posting intent authorizes an attempted send, not the truth of each draft. Guidance includes source quote, hook/stance and tone in bundled composition; question and fingerprint persist only through subsequent posting history, while reports persist only if their caller retains them. Rejection recovery advances candidates, not model weights or product machinery. Operating mode is a caller-triggered bounded candidate walk. There is no expected-answer oracle or demonstrated improvement trigger; the gate tests a model's judgment of source fidelity.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage)

Workflow-specific verification scope: apply [WF-RTE-draft-selection](#wf-rte-draft-selection)'s type-dependent fidelity finding rather than treating all negative verdicts as vetoes. The inspected runner's default pre-verification deduplication also limits contradiction detection to survivors. Neither qualification negates the independent live-source, repetition, posting-intent or staging checks.

Workflow delivery boundary: `posted_message_id` acknowledges the inspected staging path, not a published community message. Claim-before-send chooses duplicate avoidance over automatic retry after ambiguous transport failure. A dry-run report needs no transport; a staged delivery depends on a conforming sender and history implementation. Those external contracts and successful operation remain unobserved.
