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

The subsequent [economic considerations for admission](./admission-to-the-main-record.md)
make this comparison explicit. A possible future debugging use does not by
itself justify a second record when the trace already captures the information.
The additional value may instead be cheaper access, clearer interpretation,
direct reuse or durability beyond trace retention. An intermediate's primary
value may also be consumed by its committed result. Trace completeness and
availability must be checked rather than assumed; no retention threshold has
been adopted.

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

## Content equivalence governs the comparison

The operator clarified that essentially the same content can go in a commit
message as in an ADR. Rationale, alternatives, original expectations, links to
other documents, outcomes and a consolidated account spanning many changes are not
exclusive to either carrier. This corrects a possible bias in the earlier
framing: a concise ADR must not be compared with terse implementation messages
as though their content difference were required by Git.

Separate what should be captured from how the captured account is indexed and
accessed. For the carrier comparison, hold decision text and evidence references
constant. The live question is how an agent finds the account, reaches the
applicable version and records or discovers updates. A marked-commit arrangement
may include a maintained index; an ADR arrangement also relies on paths, listings,
search and links. Count the costs of each rather than assuming one has navigation
for free.

Mutability remains a relevant input, but does not mean commit-based knowledge
cannot evolve. Later commits can carry revised accounts. Compare their update
and discovery paths with editing an ADR at a stable current path. Differences in
content quality or completeness in existing histories identify capture practices,
not inherent carrier limitations.

## Document links are an access question

The operator added that both carriers can link to other documents, while linking
from commit messages may be more complicated. A file-based ADR has a location
from which relative links can be resolved. A commit message has a repository and
a commit identity, but no containing Markdown file directory; its document
references need a base-path convention or another explicit locator.

Compare following equivalent references locally and through the intended reading
interface. A repository-relative path may suffice for an agent even if a viewer
does not make it clickable. A hosting URL may improve that interface while adding
a dependency on the host or repository location. Do not assume a rendering or
resolution behavior without checking the actual interface.

Both arrangements must distinguish a document's current version from its version
at the decision. Test the effort and ambiguity of resolving that choice, and what
happens when the target moves. Treat any additional convention or maintenance as
an access cost, not an inability to carry links. This does not imply that precise
historical file links should become the default.

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

Compare these arrangements with equivalent consolidated decision text. Their
differences concern indexing and update paths, not the ability to explain a choice.

| Arrangement | Entry and update path | Question to test |
|---|---|---|
| Maintained ADR files plus ordinary commits | Current file path, ordinary file search and links; edits retain earlier versions in Git | What indexing and maintenance keep the applicable account discoverable from its consumers? |
| Rich marked decision commits without separate ADR files | Marker queries or commit references; later commits record revisions | How does an agent find the applicable account and follow amendments or supersession without stale entry points? |
| Marked decision commits plus a maintained index or summary | Current entry surface routes to historical accounts or presents their current synthesis | Does that surface provide useful access at lower total cost than ADR files or direct Git search? |

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

Which facts should be consolidated is a content question that applies to both
carriers. The placement question is: **how should an equivalent account be indexed,
reached and kept applicable?** Consider retrieval and interpretation cost, stable
entry points, search visibility, update relationships and preservation of earlier
versions. Do not count consolidation or contemporaneous rationale as exclusive
benefits of ADR files; a marked decision commit can supply the same text.

Editing an explanation is different from changing the choice; adding later
outcomes is different from replacing the original expectation with hindsight.
A candidate design must keep those operations distinguishable, whichever carrier
it uses. A revised account may appear in an edited ADR or a later decision commit.
The comparison must show how a reader reaches it and how the record distinguishes
those operations. An expensive historical search is an access problem; it does
not establish that consolidated text cannot be stored in a commit message.

## Connection to compression progress

The operator connected this architecture to inquiry driven by compression
progress. A concise architectural account can improve while more detailed
records remain available for criticism and reinterpretation. That account could
live in an ADR or a marked commit; explanatory compression does not select its
carrier. Removing material from the current view need not delete it from memory.

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

Use real decision histories to identify necessary content and distinguish capture
failures, discovery failures, misinterpretation and stale accounts. Include a
decision recorded with its implementation, one spread across commits, an ADR whose
rationale was revised, and evidence retained only in history. Do not attribute
content omitted by past authors to a carrier's inability to hold it.

First trace the operations as a design comparison. The operator cautioned that
realistic execution environments would be difficult to construct: the established
ADR environment and a minimal marked-commit mock-up would have unequal navigation
support. Map decision identity, consumer entry points, document-link resolution,
correction and supersession routes, and discovery of current and earlier accounts.
Actual file and Git operations can check mechanisms without establishing agent
performance. Do not build a benchmark or freeze indexing conventions just to run
an example.

Propose a bounded execution test only if an unresolved practical difference could
change the architectural choice. Name that uncertainty, the environment needed
to test it fairly and the expected decision value relative to setup cost. A full
alternative Commonplace environment is not required; inspection, ordinary-use
evidence or an explicitly unresolved question may be the appropriate outcome.

Apply the content-equivalence constraint above, then give both arrangements the
same correction, later outcome or superseding choice. Compare reaching the account
from an affected consumer, locating the applicable version and recovering the
earlier account. Include any maintained index, summary, listing and link upkeep
in the costs. Identify what routine reading needs and what reconsideration must
recover. Existing search may suffice; neither separate ADR files nor a new index
is a presumed outcome.

The operator authorized refreshing and cleaning up the workshop, not adopting
these alternatives, rewriting history or running an agent experiment. The
[workshop framing](./README.md) identifies the existing contracts and authority
boundary.
