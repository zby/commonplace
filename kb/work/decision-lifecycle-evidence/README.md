# Decision lifecycle and evidence

## Live question

**What should maintained architectural accounts retain, and what can remain in
Git history, so agents can understand and reconsider decisions without the
originating sessions?**

The live alternatives are maintained ADR files, rich marked decision commits,
and combinations. Compare them before selecting a carrier or adding machinery.
The [Git and retained-artifact exploration](./git-and-retained-artifacts.md)
records the operator discussion and the unresolved division of labour.

## Intent and constraints

The operator opened this investigation on 2026-09-25 after an accepted ADR was
recorded before implementation. On 2026-10-26 the operator asked to explore concise
architectural accounts over richer retained reasoning: alternatives and criticism
should not disappear merely because the current account omits them.

On 2026-11-07 the operator shifted attention to Git as durable project memory,
including richer commit messages and marked commits closing larger changes.
Requiring Git for all Commonplace KBs is an option to evaluate, not adopted policy.
The operator then requested cleanup around this direction.

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
- ADRs are mutable and consolidate information, but also record history. Commit
  messages can contain rationale and consolidate several changes. Neither
  “current view versus history” nor “rationale versus detail” settles the boundary.

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
2. What does an editable ADR contribute over a rich marked decision commit?
   Which history belongs in the maintained account, and which is affordable to
   recover on demand? Useful overlap is allowed; duplication needs a purpose.
3. Can ADR history, nearby changes and `Decision:` trailers usually find the
   consequential commits? Add explicit anchors where they help. Finding files
   within the right commit is normally easier than finding the right commit.
4. What must be captured in commit messages or other retained records before
   temporary sources expire? Check existing capture before extracting copies.
   A reason to inspect evidence and an opportunity to run a search are different.
5. How can a revised account improve understanding without hiding original
   expectations, rejected alternatives, qualifications and failures? Shorter
   text alone is not compression progress.

## Evaluation

Compare concrete histories on recording, discovery, interpretation, maintenance
and retention cost. Include a decision committed with its implementation, one
spread across commits, an edited ADR, and the marked closing-commit alternative.

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
history contract, discovery routes, consumers and adoption criteria. Dispose of
the Git-required and marked-commit alternatives explicitly. Record worked-case
limits and whether theory-side reconciliation is useful or needs more evidence.

Extract durable findings and preserve essential evidence with usable discovery
paths before deleting the workshop and removing its active-list entry. A finished
proposal does not claim its implementation has shipped.
