# Decision lifecycle and evidence

## Live question

**How should decision accounts be indexed, discovered and updated across ADR
files and Git commits, so agents can understand and reconsider decisions without
the originating sessions?**

The live alternatives are maintained ADR files, rich marked decision commits,
and combinations. They can carry essentially the same decision text, including
rationale, alternatives, links to other documents and consolidation across changes.
Do not infer a content division from the carrier. First establish what needs
retaining; compare access and maintenance arrangements with that content held
constant. The [Git and retained-artifact exploration](./git-and-retained-artifacts.md)
records the operator discussion and the unresolved division of labour.

The subsequent [admission-to-the-main-record discussion](./admission-to-the-main-record.md)
adds the upstream economic question: which products and accounts of automated
work earn Git retention when session traces already supply a process record?
Possible future usefulness, including debugging, is not sufficient by itself.
Compare the additional value of Git admission with trace recovery, working
storage, regeneration and incorporation into a maintained result. This is an
open design analysis, not an adopted retention policy.

## Intent and constraints

The operator opened this investigation on 2026-09-25 after an accepted ADR was
recorded before implementation. On 2026-10-26 the operator asked to explore concise
architectural accounts over richer retained reasoning: alternatives and criticism
should not disappear merely because the current account omits them.

On 2026-11-07 the operator shifted attention to Git as durable project memory,
including richer commit messages and marked commits closing larger changes.
Requiring Git for all Commonplace KBs is an option to evaluate, not adopted policy.
The operator then requested cleanup around this direction and clarified that
essentially the same content can be put in an ADR or a commit message. Indexing,
rather than an assumed difference in explanatory content, must organize the
comparison. ADR mutability remains relevant through how updates are made and
how readers find the applicable account.

The following constraints remain:

- Essential evidence must survive session loss. Retained Git history can satisfy
  this requirement; the evidence need not be duplicated in current artifacts.
- Session logs and source snapshots may be long-lived and indexed without being
  permanent. Volume, privacy and copyright limit retention. External access does
  not guarantee recovery of an old observation.
- Adoption is an authorized choice, not corroboration of its rationale.
  Implementation and observed benefit require separate evidence.
- Preserve original expectations, consequential operator contributions, deciding
  reasons and contrary outcomes where needed for reconsideration. Git cannot
  recover information never recorded; retrospective reconstruction is not
  contemporaneous capture.
- Content quality, completeness and consolidation are not carrier advantages:
  the same account can be placed in either carrier. Neither “current view versus
  history” nor “rationale versus detail” settles the boundary. An ADR has an
  editable current path; a commit-based account can be updated through later
  commits and an index. Compare how those routes expose the applicable version,
  not editable prose against an artificially frozen decision process.

## Existing contract

Checked on 2026-11-07 against source-checkout HEAD `91810b276`:

- The [ADR type](../../reference/types/adr.md) remains for made and implemented
  choices. A settled but unimplemented decision stays in workshop material under
  current rules. The [ADR 089 episode](./adr-089-premature-placement.md) preserves
  the concrete mismatch; implementation later completed in `b745bcc8`.
- [ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md) assigns
  change history to Git for this source checkout. The [storage contract](../../reference/storage-architecture.md)
  still permits installed KBs without Git. Extending that dependency is a
  framework decision, separate from making runtime commands invoke Git or
  replacing database freshness baselines.
- [ADR 075](../../reference/adr/075-commit-messages-carry-read-path-trailers.md)
  supplies decision/workshop trailers and migration narrative in commit bodies.
  [ADR 077](../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md)
  adds change intent and placement by regeneration source and consumer. Start
  from these existing practices rather than assuming a new event store.

## Questions to settle

1. What durability and history-availability contract would Git-required KBs need?
   Treat squashing and rewriting as exceptions with preservation obligations.
2. With equivalent decision text, what access and update arrangement does each
   carrier need? Compare a current ADR path with marked commits, including any
   index needed to locate the latest relevant account. Count maintaining that
   index, links and update relationships on either side.
3. How does an agent reach the account from affected code, contracts or
   instructions? Can ADR history, nearby changes and `Decision:` trailers find
   consequential commits? Add explicit anchors where they help. Finding files
   within the right commit is normally easier than finding the right commit.
   Both carriers can link to documents. Does following a link from a commit
   message require extra repository, base-path or version conventions compared
   with a file-relative ADR link? Separate resolving a link from merely storing it.
4. What must be captured in commit messages or other retained records before
   temporary sources expire? Check existing capture before extracting copies.
   A reason to inspect evidence and an opportunity to run a search are different.
5. How can a revised account improve understanding without hiding original
   expectations, rejected alternatives, qualifications and failures? Shorter
   text alone is not compression progress.
6. What earns admission to the main record beyond existing session traces and
   working outputs? Compare remaining expected uses after consumption, recovery
   and access costs, capture gaps, durability and the costs of selection. Coordinate
   any class-level retention policy with the lineage-mechanisms workshop.

## Evaluation

Start with an operation-level design comparison, not an agent-performance trial.
The operator noted that creating realistic alternative environments is difficult:
existing ADRs already have paths, links, search visibility and conventions, while
a marked-commit alternative would need comparable support. Comparing the live KB
with a small mock-up would confound the carrier with environment maturity.

For one real decision, trace how each arrangement identifies the account, connects
consumers to it, resolves supporting-document references, records corrections and
exposes the applicable account and its predecessors. Inspect actual file and Git
operations where useful. Record required conventions, dependencies, ambiguities
and maintenance obligations; this is design analysis, not measured retrieval or
agent-performance evidence. Do not select a marker or index merely to make a
trial runnable.

Only propose an execution test after identifying a consequential uncertainty
that the design comparison cannot settle. Scope the environment to that question
and justify realism, cost and how the result could change the choice. A complete
alternative KB or benchmark is not a prerequisite for continuing this workshop.
Mechanism inspection or evidence from ordinary use may suffice; otherwise retain
the uncertainty explicitly.

Separate two comparisons. Real histories reveal what was captured or omitted;
those differences do not establish a carrier's capabilities. To compare carriers,
use the same decision text and evidence references in an ADR file and a marked
commit. Include an equally consolidated account on both sides, including when a
decision spans several implementation commits.

Compare entry points, ordinary search visibility, links from consumers and to
supporting documents, discovery of the applicable version, and correction,
amendment and supersession paths. Test local agent navigation and the intended
published interface: a stored path may be usable by an agent without being a
clickable link. Distinguish a reference to a document's current version from one
to its version at the decision; both carriers need that distinction.
Give both arrangements the same later information and compare their update routes
without rewriting historical commits. An index or maintained summary is a valid
candidate, not a free capability: count its creation, maintenance and navigation
cost, just as for ADR listings and links. Differences in completeness or writing
quality must not be reported as evidence for one carrier.

Include a decision committed with its implementation, one spread across commits
and an ADR edited after implementation. Distinguish capture, discovery,
interpretation and maintenance failures, and name which arrangement caused or
exposed a difference rather than attributing it to the stored text.

A candidate must distinguish settled but unimplemented work, partial adoption,
abandonment, shipped but unevaluated changes and contrary later outcomes. Test
reconsideration when a deciding assumption changes and a rejected option becomes
viable. Remove session access but retain the chosen durable substrate. Separately
check missing history and a squashed referenced commit: retaining a final tree is
not necessarily retaining the evidence a reader needs.

Name missing evidence and narrow conclusions rather than adding machinery to hide
the gap. This framing commissions no worker launches, behavioral experiment or
implementation. A design that keeps existing records with a small procedural
repair is an acceptable result.

## Coordination and authority

Writes stay within this workshop and its active-list entry. Current contracts
remain binding; framework adoption and peer-workshop changes need separate
authorization.

- [Lineage mechanisms](../lineage-mechanisms/README.md) owns general provenance,
  retention and storage-weight design. Coordinate rather than duplicate it.
- [ADR testing](../adr-testing/README.md) tests existing record usefulness;
  [ADR routing](../adr-routing/README.md) owns consultation routes.
- [Use-and-outcome records](../use-and-outcome-records/README.md) owns growing
  observational histories; [design-space studies](../design-space-studies/README.md)
  explores richer design maps, leaving durable retention here.
- [Conjecture-store](../conjecture-store/README.md) develops independently. The
  operator prefers eventual unification, but its schema and thresholds do not
  bind this investigation. Reconcile differences before adopting shared machinery.
- The [compression exploration](../open-ended-work-economics/curiosity-exploration/turn-05/integration.md)
  supplies preservation questions, not a selected storage architecture or a
  demonstrated advantage for compression-driven inquiry.

## Historical material

Older external-system scans, the ADRs4AI comparison, session-trigger survey and
evidence-link audit with its batch manifests are no longer active work here. Recover them only
for a specific question from the retained pre-cleanup tree:

```bash
git ls-tree -r --name-only 91810b276 -- kb/work/decision-lifecycle-evidence/
git show 91810b276:kb/work/decision-lifecycle-evidence/<path>
```

The audit's three label decisions had been resolved; batch completion was not
established by the refresh. Removing its stale working list neither applies its
suggested edits nor declares cleanup complete. Its old paths and classifications
need checking before any future use.

## Closure

Close with a design proposal or a reasoned decision that existing records suffice,
possibly with procedural repairs. State the division of labour, lifecycle and
history contract, indexing and update routes, consumers and adoption criteria.
Justify carrier choices by access and maintenance differences with equivalent
content, not by assigning richer explanations to one side. Dispose of the
Git-required and marked-commit alternatives explicitly. Record worked-case
limits and whether theory-side reconciliation is useful or needs more evidence.

Extract durable findings and preserve essential evidence with usable discovery
paths before deleting the workshop and removing its active-list entry. A finished
proposal does not claim its implementation has shipped.
