# Git and retained artifacts: division of labour

## Origin and status

Recorded on 2026-11-07 from the operator–assistant discussion that prompted the
workshop refresh. This is a selective account of the discussion, not a verbatim
session export, an executed comparison or an adopted architecture. The operator
requested systematic investigation; examples and candidate rules below remain
open unless identified as existing contracts. The [workshop framing](./README.md)
owns scope and authority.

## Memory beyond session logs

The operator rejected treating session logs as the sole source from which project
knowledge must be derived. Broad capture and indexing are useful, but retaining
everything forever is not feasible. The working picture includes:

- untracked material, including session logs and source snapshots, which can be
  long-lived and indexed but subject to expiry, volume, privacy and copyright
  limits;
- Git history as durable project memory, including exact prior tracked states,
  diffs and commit messages;
- retained KB artifacts as maintained accounts of knowledge, instructions and
  decisions;
- access to the external world for new observations, checks and reacquisition.

These are roles, not four disjoint stores: current KB files are versioned in Git.
Untracked does not necessarily mean short-lived or regenerable. External access
does not guarantee recovery of an old observation. Operational state also keeps
its scoped authority under the current [storage contract](../../reference/storage-architecture.md);
this framing does not replace accepted freshness baselines with repository history.

The requirement that essential evidence survive session loss can be satisfied by
retained Git history. It is not a demand to copy every essential fact into an ADR
or another currently visible file. The combined retained system must make the
facts discoverable and sufficient for their intended use.

## Git as a framework substrate

The operator proposed examining the assumption that all Commonplace KBs use Git.
That would permit framework-level rules about commit records and ADR navigation.
The current contract is narrower: [ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md)
gives Git a declared change-history role in this source checkout, while installed
KBs may work without it. Evaluating the broader assumption is a real architectural
decision, not merely adding a formatting convention.

The working durability assumption is that retained history is ordinarily stable.
Rewrites and squashes are exceptions to manage, not grounds for rejecting Git as
a durable carrier. A candidate rewrite policy would preserve or remap historical
dependencies before replacing history. Remapping a pointer suffices only when the
replacement retains what the reference was needed to recover. A squash that drops
an original expectation or intermediate correction is not equivalent merely
because the final tree matches. No policy or retention mechanism is adopted here.

Requiring Git for KB memory would not by itself require `commonplace-*` commands
to invoke it, give every commit adoption semantics, or move operational state out
of its store. Those are separate choices.

## Finding consequential commits

The operator's navigation judgment is that finding the right commit is usually
harder than finding the relevant files after reaching that commit. Do not design
a dense historical file-link graph by default.

The operator also noted that an ADR's own Git history often supplies the needed
entry point. If its record and implementation change land together, the agent can
inspect that commit directly. Separate changes can be found through existing
`Decision: ADR 0NN` trailers, introduced by [ADR 075](../../reference/adr/075-commit-messages-carry-read-path-trailers.md).

The candidate default is to start with the ADR's history and add explicit commit
anchors only where they materially improve discovery. A reference should explain
why a commit matters when that is not obvious. A historical file locator can help
with a broad or ambiguous commit, but should be exceptional rather than mandatory.
This route's adequacy has not been measured.

## Rich commit messages and marked closing commits

The operator proposed retaining more in commit messages. Reasons, constraints,
alternatives, expectations, uncertainty and verification can accompany the exact
diff. Existing conventions already put migration narrative in commit bodies and
capture intent when the subject and diff do not show it
([ADR 077](../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md)).

The stronger alternative is a marker on selected commits that close a larger
change. Such a commit could consolidate the architectural decision and identify
earlier implementation and evidence commits. It need not explain only its own
diff. Git history is a graph, but that does not prevent a commit message from
summarizing work across several commits.

Compare at least these arrangements:

| Arrangement | Candidate benefit | Question to test |
|---|---|---|
| Maintained ADR files plus ordinary commits | Editable consolidated account with exact historical versions and implementation diffs behind it | Which content is useful consolidation and which is unnecessary repetition? |
| Rich marked decision commits without separate ADR files | Consolidated decision record fixed to a historical identity, discoverable by a marker | How does a reader recover current applicability, amendments and supersession? |
| Marked decision commits plus a maintained navigation or summary surface | Historical decision records with a current entry point | Does maintaining the extra surface cost less than searching history directly? |

No marker syntax, mandatory message template, new index or renderer is selected.
A closure-only convention must also handle choices made before implementation,
work that is abandoned, and later evaluations; not every important event closes
a successful change.

## Mutability is an input, not a clean partition

The operator identified an important difference: ADR files can be edited, while
changing a commit message changes the commit identity. An ADR can consolidate
later understanding, correct an explanation, add outcomes or narrow scope. Git
retains earlier versions of that editable account.

That does not make the division “current view versus history.” An ADR also
preserves selected history needed to understand the choice: original constraints,
rejected alternatives and reasons for reversal. Nor is the division “rationale
versus detail”: rich commit messages can hold rationale and consolidated decisions.
A marked closing commit challenges the assumption that only an ADR can cover
several changes.

The open placement question is: **which historical facts should be brought
together in a maintained account, and which can remain recoverable through
historical investigation?** Consider mutability, retrieval and interpretation
cost, consolidation, exactness, current applicability and contemporaneous capture.
Do not force a non-overlapping taxonomy before worked cases establish one.

Editing an explanation is different from changing the choice; adding later
outcomes is different from replacing the original expectation with hindsight.
A candidate design must keep those operations distinguishable, whichever carrier
it uses. Recoverability from history can justify omission from routine reading,
but it can also be too expensive or unreliable to replace explicit consolidation.

## Connection to compression progress

The operator connected this architecture to inquiry driven by compression
progress. A concise architectural account can improve while more detailed
records remain available for criticism and reinterpretation. Removing material
from the current view need not delete it from memory.

The [recent compression exploration](../open-ended-work-economics/curiosity-exploration/turn-05/integration.md)
retained preservation requirements but selected no memory architecture and
established no compression-steering advantage. Here the question is concrete:
what must remain available to check whether a revised account preserves important
distinctions, earlier permissions, counterexamples and original expectations?
Git is a candidate carrier for that comparison basis, not a lossless record of
anything that was never captured.

Shorter prose, fewer files or a uniform explanation do not alone establish
improved understanding. Neither keeping all logs forever nor reconstructing every
future answer from them is assumed. Name acceptable losses and remaining
uncertainties when temporary evidence expires.

## Inputs to the next comparison

Use real decision histories to distinguish capture failures, discovery failures,
misinterpretation and stale accounts. Include a decision recorded with its
implementation, one spread across commits, an ADR whose rationale was revised,
and evidence retained only in history. Compare the marked closing-commit option
on the same needs rather than judging it against requirements invented for ADR
files. Identify what ordinary reading needs and what reconsideration must recover.

The operator authorized refreshing and cleaning up the workshop, not adopting
these alternatives, rewriting history or running an agent experiment. The
[workshop framing](./README.md) identifies the existing contracts and authority
boundary.
