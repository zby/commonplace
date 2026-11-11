# Decision accounts in Git and maintained files

## The bounded question

For a decision account already worth retaining, how should readers find it,
interpret its status and reach later corrections or reconsiderations?

This is one case within the [workshop's design-space investigation](./README.md),
not the organizing question for all retention. The [admission map](./admission-to-the-main-record.md)
addresses whether material earns retention first. This comparison selects no
new ADR policy, commit marker, index or framework-wide Git requirement.

The operator's November 7 discussion supplied the main comparison constraint:
**essentially the same content can go in an ADR or a commit message.** Reasons,
alternatives, original expectations, evidence links and consolidated accounts
spanning several changes are not exclusive to either. Compare access and update
arrangements with that content held constant.

## Existing starting points

- The [ADR type](../../reference/types/adr.md) governs made and implemented
  architectural choices. Settled but unimplemented work currently stays in the
  workshop. The [ADR 089 episode](./adr-089-premature-placement.md) records a
  historical violation; implementation subsequently completed in `b745bcc8`.
- [ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md) assigns
  change history to Git for this checkout. The [storage contract](../../reference/storage-architecture.md)
  is the authority for storage roles; considering Git here does not adopt a
  Git-required framework.
- [ADR 075](../../reference/adr/075-commit-messages-carry-read-path-trailers.md)
  supplies `Decision:` and `Workshop:` trailers.
  [ADR 077](../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md)
  includes change intent and placement by regeneration source and consumer.

Start from these routes. An extra event store or new index must earn its cost.
Selected evidence can survive in Git history without a duplicate current file,
but a retained account must remain usable for its intended purpose without
session traces.

## Arrangements and commitments

| Arrangement | Access and update route | Consequences to examine |
|---|---|---|
| Maintain an ADR plus associated commits | Current file path, file search and links; edit the account while Git retains earlier versions | Keep the current explanation and implementation status applicable; ensure consequential history remains discoverable |
| Put rich accounts in selected commits | Search by existing trailers or other agreed entry points; later commits revise the account | Readers need a route to the right account and its updates, including decisions spread over several commits |
| Add an index or maintained summary over commit accounts | A current entry surface identifies or synthesizes applicable accounts | Count its creation, maintenance, links and risk of lagging behind the underlying history |
| Keep existing arrangements with a narrow procedural repair | Use ADR history and existing trailers; improve particular records or links | Less new machinery, but adequacy must be assessed for the actual reading and reconsideration tasks |

These arrangements may coexist. A marked closing commit can consolidate an
account of a larger change, not just explain its own diff. But closure is not
the only event worth recording: abandonment, partial adoption and later contrary
outcomes may matter. No new marker syntax is needed merely to investigate that
possibility.

## Consequences that the carrier alone does not settle

### Finding the applicable account

The operator identified finding the right commit as generally harder than finding
files once that commit is known. ADR history can be an existing entry point;
`Decision:` trailers can connect separate implementation changes. Test their
adequacy for the case before proposing a dense historical link graph.

A stable ADR path does not automatically expose its important historical versions.
A commit-based account is not automatically frozen in understanding: later commits
can correct it. Both need a route to the applicable account and its predecessors.
The cost of maintaining that route belongs in the comparison.

### Resolving references

Both carriers can name documents. A Markdown file provides a directory for
relative links; a commit message provides a repository and revision but no
containing Markdown directory. A repository-relative path may be enough for an
agent without being clickable in a viewer. Compare the intended interfaces,
including any convention needed to resolve the reference.

Both must distinguish a reference to the document now from its version at the
decision. A precise historical locator can help a consequential comparison but
need not be mandatory for every link.

### Updating without erasing the earlier basis

Changing an ADR preserves prior text in Git. Changing an old commit message
changes its identity, but a new commit can provide a revised account without
rewriting history. The comparison is therefore about update and discovery routes,
not mutable understanding versus immutable understanding.

Keep explanation correction, decision change and addition of later outcomes
distinguishable. Preserve original expectations, reasons and rejected alternatives
when reconsideration needs them. A shorter account is not necessarily a better
account; neither carrier guarantees good selection or explanation.

### Depending on retained history

An account needed for future use requires its relevant history to remain
available. A squash can preserve the final tree while losing an original
expectation or deciding reason. Pointing to a replacement commit only suffices
if the replacement preserves what the reference was for.

This is a consequence to name for a history-dependent arrangement, not a commission
to rewrite history or design a universal preservation mechanism. Keeping Git
history also does not give every commit adoption semantics.

## Proportionate comparison

For a real decision worth revisiting, inspect how each plausible arrangement
identifies it, connects it to the affected artifacts, resolves evidence references,
records new information and exposes the applicable account. Hold retained text
and later information constant. Compare an equally consolidated account on both
sides, including when the decision spans several implementation commits.

Real histories can reveal omissions or misleading status, but those differences
do not prove a carrier incapable of holding the missing content. The established
ADR environment and a bare mock-up of commit accounts also have unequal navigation
support. Do not attribute that difference to carrier quality or build a complete
alternative environment merely to remove it.

Include only lifecycle distinctions consequential to the selected case: settled
but unimplemented, partially adopted, abandoned, shipped but unevaluated, or
challenged by later outcomes. The [ADR 089 witness](./adr-089-premature-placement.md)
illustrates the danger of conflating choice with implementation; it does not
establish which alternative arrangement would prevent recurrence.

Mechanism inspection can support a bounded design judgment without establishing
better agent performance. If existing routes suffice, keep them. If a material
uncertainty remains, state it and propose a test only when its likely decision
value warrants the cost. No general carrier winner is required.
