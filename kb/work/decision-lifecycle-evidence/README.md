# Decision lifecycle and evidence

## Commission

Opened on 2026-09-25 at the operator's request. Determine how Commonplace
should preserve a decision's development from proposal through deliberation,
implementation, and later evaluation, while making its current state clear
to agents and readers.

The operator connected this to an earlier concern: evidence must be retained
during ordinary work before later self-improvement measurements can use it.
ADRs are one form of evidence of deliberation. The operator proposed exploring
whether ADRs could be views over a richer record, with proposals as an early
stage. This workshop investigates that direction; it does not adopt a new
storage model or change the current ADR contract.

## Retention direction fixed by the operator

On 2026-09-25 the operator clarified the retention policy for this design:
Commonplace must own records containing the most obviously important data.
Those records may point to agent sessions for additional detail, but their
essential evidence must survive loss of access to those sessions. Cleanup
risk motivated this direction. Retention differs between harnesses and must
not serve as Commonplace's evidence guarantee.

Sessions are useful source material. Capture the important facts while that
material is available, and retain a session identifier or link when supplied.
A session pointer supplements the owned record; it cannot be the only place
holding a deciding reason or a result needed to assess the change. Preserve
the relevant excerpt, measurement, or small evidence artifact when a summary
alone would not support later inspection. Missing facts remain missing;
later reconstruction must be distinguished from contemporaneous capture.

The working interpretation of “most obviously important” is the information
needed to understand, revisit, and evaluate the choice:

- the problem, relevant starting state, and constraints;
- the options actually considered, the choice, and deciding reasons;
- who supplied consequential judgments, especially human interventions;
- the expected effect, uncertainty, and what would prompt reconsideration;
- what was implemented and verified, with artifact or commit references;
- observed outcomes, failures, reversals, and available cost measurements;
- dates and source-session references for recovering further detail.

This list is a starting capture scope, not an adopted schema. Record facts as
they become available: a pre-implementation decision cannot already contain
implementation or outcome evidence. Preserve its original expectations when
adding later results. The record's durable home and capture trigger remain
design questions, including how capture covers interrupted or abandoned work.

The acceptance test is to make every session link unavailable: can a later
reader still recover the decision, its grounds, its implementation state, and
the evidence actually retained for its outcome? Detailed reconstruction may
be lost, but essential facts must remain. A missing measurement must still be
identifiable as missing, rather than silently turning into a success claim.

## Motivating problem

The [ADR 089 episode](./adr-089-premature-placement.md) records the immediate
inconsistency. An agent wrote an accepted ADR into `kb/reference/adr/` before
its implementation. Commonplace's ADR contract reserves that location and
type for decided and implemented choices.

The operator reports that this is a recurring, easy mistake. The intended
decision needs to be written before implementation so it can guide the work.
The usual practice is to draft the ADR in the workshop and promote it after
implementation. An agent can produce the needed decision text but place it
directly in the directory named for that artifact, accidentally making it
look like a record of the shipped system.

The current contracts make that distinction awkward: a proposal is undecided,
and an ADR is decided and implemented. Workshops can hold the intervening
state, but its meaning and promotion depend on placement and authoring
discipline. The design should make the necessary pre-implementation record
easy to create without falsely describing implementation as complete.

## Questions to settle

- When should Commonplace search sessions for evidence to retain? The operator
  clarified that future telemetry needs are open-ended and sessions already
  contain much of the material. Map demand-driven searches, lifecycle events,
  session hooks, scheduled processing, and protection against source loss;
  compare concrete mechanisms in the reviewed systems. The [trigger design
  space](./session-evidence-triggers.md) records this follow-up commission,
  candidate policy, and mechanism inventory.
- What is the continuing object: one decision record with several views,
  linked proposal and ADR documents, or another arrangement? What should have
  a stable identity through revisions, partial adoption, and supersession?
- How should acceptance of a choice, implementation progress, and evidence
  of benefit be represented separately? How should rejected, withdrawn,
  abandoned, and partially implemented choices remain available for analysis?
- Which evidence must survive each transition: original problem and available
  evidence, alternatives, deciding reasons, participants and roles, expected
  effects, implementation departures, costs, and observed outcomes? Which
  parts already survive in git, proposals, workshops, or reports?
- Which reader needs each view: deliberation, implementation, understanding
  the shipped architecture, revision, or evaluation? What may each view claim
  about the system, and what evidence permits that claim?
- What prevents the ADR 089 placement error? Compare a clearer drafting and
  promotion procedure with richer records or derived views before selecting
  machinery. Distinguish mechanically checkable evidence links from judgments
  about whether implementation actually fulfills a decision.
- How can decision-time expectations remain distinguishable from later
  explanations and observations? How does a later evaluation find the original
  record, including unsuccessful choices, without treating an ADR citation or
  an accepted implementation as proof of improvement?

## Evaluation boundary

A satisfactory design must represent a settled choice before implementation,
an implementation in progress, a shipped change whose benefit is unmeasured,
and a later outcome that contradicts the original expectation. It must also
handle partial adoption and a proposal that never ships. These are cases to
test the design against, not a prescribed status enum.

Every case must also pass the session-loss test in the retention direction
above. Workshop closure must preserve the owned evidence needed for those
uses, even when the source sessions are still accessible at closure time.

Use the recorded ADR 089 episode as one concrete test. The recurrence claim
comes from the operator; this workshop has not measured its frequency. Added
recording, retrieval, and maintenance costs must be justified by a named use.
No database, event log, generated ADR renderer, schema, or repository-wide
migration is selected at opening.

## Coordination and current contracts

- ADR 089 was implemented by the tag-contract-convergence workshop, which
  closed in commit `b745bcc8`. This workshop records the lifecycle failure;
  that later completion does not erase the earlier mismatch.
- [ADR routing](../adr-routing/README.md) and the [site back-pointer
  proposal](../../reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md)
  concern finding decisions when changing their consumers. This workshop owns
  lifecycle and evidence retention; coordinate changes to shared ADR surfaces.
- The [ADR type](../../reference/types/adr.md), [proposal
  type](../../reference/types/design-proposal.md), and [reference collection
  contract](../../reference/COLLECTION.md) remain binding until changed through
  an adopted design. Drafts belong here under the current workshop exception.
- [ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)
  restricts links into archived proposals; [ADR
  074](../../reference/adr/074-git-is-the-change-history-layer.md) assigns change
  history to git; [ADR
  085](../../reference/adr/085-withdrawn-proposals-are-deleted.md) deletes
  withdrawn proposals after extracting current content. Evaluate whether these
  retention and access rules serve the proposed evidence use before revising
  them. Recording evidence need not mean loading all history into routine work.

## Evidence and conceptual inputs

- [Competing causal theories can guide distinguishing
  experiments](../../notes/competing-causal-theories-can-guide-distinguishing-experiments.md)
  — retained alternatives can guide what evidence to seek before current
  observations favor either explanation. The worked example distinguishes
  statistical discrimination and corroboration from final verification; for
  this workshop, it motivates keeping competing predictions, test assumptions,
  and results alongside the decision record.
- [Trace-derived system scan](./trace-derived-system-scan.md) — follow-up
  commissioned on 2026-09-26: all positively marked entries in both system
  collections, including archival capture, correction/failure triggers,
  activity thresholds, and staged evidence-to-proposal mechanisms.
- [Session evidence: trigger design space](./session-evidence-triggers.md) —
  separates source capture from evidence extraction, compares system triggers,
  and names the choices and failure cases a proposal must resolve.
- [Audit of `evidenced-by` edges](./evidenced-by-audit/README.md) — 356
  edges classified against ADR 091: few name a test, about a quarter record
  origin, and three label decisions block the relabel.
- [Existing articles and system reviews](./corpus-scan.md) — ADR-focused
  search of articles and full agentic analyses, related mechanisms, and
  separately marked legacy decision-history leads.
- [ADR 089 premature placement](./adr-089-premature-placement.md) — dated
  incident, repository anchors, operator account, and limits of the diagnosis.
- [Citing retained theory at the decision point is a mediation
  trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
  — the contribution and limits of recording which knowledge informed a choice.
- [Retaining episode evidence keeps a distilled rule open to
  re-examination](../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
  — why a decision summary may need linked evidence.
- [Compounding is tested in later improvement, not by the accepting
  metric](../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
  — separates acceptance evidence from evidence about later improvement.
- [Downstream evidence
  protocol](../first-downstream-run/commonplace-evidence-protocol.md) — proposed
  outcome and comparison records; designing this lifecycle does not itself
  produce measurements.

## What closes this workshop

Close when the design question has a recorded disposition: either a finished
design proposal naming the retained evidence, lifecycle distinctions, views,
consumers, adoption criteria, and changes to existing contracts, or a reasoned
decision that a smaller procedural repair suffices. Record how the candidate
handles the evaluation cases and what remains untested.

Before deleting the workshop, extract any durable finding and the incident
evidence its future consumers require. Promotion of a design proposal closes
this investigation without claiming that its implementation has shipped.
Remove the workshop from the active list at closure.
