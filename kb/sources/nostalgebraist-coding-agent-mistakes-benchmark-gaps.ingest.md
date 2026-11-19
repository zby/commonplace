---
description: "A coding-agent user reports continued errors and poor prioritization despite greater usefulness, and conjectures that benchmark optimization makes residual gaps harder to name."
source: https://www.lesswrong.com/posts/Gsj36znHDKAihs9qG/nostalgebraist-s-shortform?commentId=5gxpoDRpAoLzKcfa7
captured: "2026-10-30"
capture: lesswrong-embedded-json-html
capture_scope: excerpt
genre: conceptual-essay
snapshot_sha256: 912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716
ingested: "2026-11-19"
type: types/ingest-report.md
domains: [coding-agent reliability, operator steering, benchmark optimization, cross-session carryover]
learning_claims: true
---

# Ingest: Nostalgebraist on persistent coding-agent mistakes and benchmark gaps

## Classification

The [LessWrong shortform comment](https://www.lesswrong.com/posts/Gsj36znHDKAihs9qG/nostalgebraist-s-shortform?commentId=5gxpoDRpAoLzKcfa7) uses firsthand coding episodes and analogies to frame a problem with agent judgment and argue that benchmark progress can obscure it. It does not report a controlled comparison.

Author: nostalgebraist, writing under a handle and drawing on direct use of coding agents. The author reports checking a session log to verify the model used in one set of examples; the comment does not supply the log.

## Summary

Nostalgebraist reports that coding agents became useful through speed and breadth of knowledge while still making basic mistakes and pursuing low-value work. Close supervision lets the author correct mistakes and redirect effort, but later sessions can require the same corrections. Here, judgment means deciding what deserves effort or escalation, not just knowing whether a technical statement is true. The author conjectures that developers can optimize capabilities they can express as evaluations, leaving the remaining gaps harder to name even as measured performance improves.

## Quotes

> They're like smart-but-naive first-year grad students: book-smart, hard-working, lacking in taste/discernment and ability to prioritize, liable to go off on silly low-value tangents (which they treat with the utmost seriousness) if not closely watched and steered.
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, grad-student analogy

> Incidentally, here's a relevant quote from a recent </span><a href="https://www.anthropic.com/research/employment-at-anthropic" rel="noreferrer"><span style="white-space:pre-wrap">Anthropic write-up</span></a><span style="white-space:pre-wrap"> about internal coding agent use and its consequences:
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, lead-in to quoted Anthropic write-up (snapshot preserves raw LessWrong HTML markup around the link)

> Spiraling agent productivity translates into output pitched across humans’ screens and attention. One engineer compared this to babysitting:
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, first paragraph of quoted Anthropic write-up

> They're like, I need my juice box opened and it's an emergency that my juice box is opened. And that is voiced with the same level of concern as the one who has sliced their finger and is bleeding. [...] When you are babysitting, every child brings to you concerns with an equal demand for your attention and the various [Claudes] also do that.
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, second paragraph of quoted Anthropic write-up

> I laughed out loud when I read this, having come up with very similar analogies myself.  The agents have no sense of priorities, and I cannot for the life of me figure out how to give them one.
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, author's reaction immediately following the quoted Anthropic passage

> Everything is flattened out; everything is assigned equal importance; every interaction looks and feels the same; doing things becomes trivially easy, and yet one somehow whiles away all of one's time on the most pointless of trivia, or else on explaining for the Nth time to the Nth Claude why those trivia are not worth anyone's time (and watching the Nth Claude readily agree, only for the (N+1)st Claude to begin the whole tedious game anew).
> --- `kb/sources/.snapshots/nostalgebraist-coding-agent-mistakes-benchmark-gaps.md` @ `sha256:912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716` — Comment body, paragraph on flattened importance following the author's reaction

## Connections Found

The comment gives [Unattended work needs the functions that interaction supplied](../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) a practitioner case: the operator corrects mistakes and supplies stopping decisions when the agent pursues tangents. The account identifies candidate dependencies; it does not show which interventions were necessary or what could replace them. The footnote's conjecture compares with [Weakly discriminated qualities tend to be underselected](../theory/weakly-discriminated-qualities-tend-to-be-underselected.md). That note supplies a conditional mechanism for unequal improvement when acceptance favors some qualities more reliably than others. The comment does not identify the acceptance rule or show that better-prioritized candidates were available and passed over.

## Learning Claims (our opinion)

The comment describes two different processes: improving measured performance by iterating against an evaluation, and an operator correcting decisions during use. The former conjecture concerns the signal used to select improvements, not whether better prioritization lies outside the learner's effective update space. As [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) distinguishes, progress under one set of signals does not compare it with alternatives. The comment does not identify the training signals or track outcomes under different evaluations.

For the human–agent workflow, the [theory-builder conditions](../theory/definitions/theory-builder.md) are only partly visible. **Localized content:** individual choices and assumptions are identifiable in the account, but no stated rule for prioritizing work is shown. **Consumption:** the author reports that steering is useful, but the effect of any particular stated correction is not traced. **Criticism:** the operator challenges specific choices, rather than only scoring outputs; the account does not show criticism of a standing rule. **Iteration:** in-session redirection suggests some corrections shape the next step, but assent alone does not show that a result was kept and used. The recurrence of corrections in later sessions gives no evidence of durable reuse for those cases. It does not establish that the workflow cannot learn; improvement in future decisions would need a separate test.

## Extractable Value

1. **Evaluate prioritization at the decision point.** For unattended KB work, record what the operator stopped or redirected, why, and what would count as an acceptable next step. This makes the abstract dependency in the unattended-work note concrete: an acceptable final artifact can hide costly detours that a final check never sees. [quick-win]
2. **Test carryover separately from immediate compliance.** A fresh session on a comparable case can test whether a retained correction changes a subsequent decision. The reported repetition motivates that test but gives no estimate of its likely effect. [experiment]

## Limitations (our opinion)

The comment gives selected incidents from one user's work, not counts of mistakes or interventions under comparable tasks, models, and configurations. It supports the coexistence of usefulness and persistent frustrations in that workflow, not a flat error-rate trend or a general claim about autonomous work. The benchmark conjecture has no benchmark audit or training comparison that distinguishes weak selection for prioritization from task mismatch or failure to elicit a capability. The capture includes the full linked comment and footnote but excludes replies and other shortform entries, so it cannot establish whether other users corroborated the account or offered counterexamples.

## Recommended Next Action

Retain the minimum source passages needed to support a bounded practitioner example of correction and stopping in [Unattended work needs the functions that interaction supplied](../theory/unattended-work-needs-the-functions-that-interaction-supplied.md).

---

Relevant Notes:

- [Context isolation for focus conflicts with global prioritization](../theory/context-isolation-for-focus-conflicts-with-global-prioritization.md) — abstracted-from: practitioner account of earnest low-value tangents and Anthropic's babysitting urgency-flattening quotes that motivated the structural isolation–prioritization account; origin, not corroboration
