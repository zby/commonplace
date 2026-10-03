# Separate the analysis collection and publish into a stable path per system

Draft decision material, not an accepted ADR. Assign the ADR number and adoption
date only after the decision is made and implemented. Revises
[ADR 099](../../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md).
The operator took the decisions below on 2026-10-03; the
[collection design](../collection-design.md) states them and the
[motivation record](../evidence/motivation.md) holds their reasoning.

## Context

Analysis workers fail parts of their jobs. The chosen response is to simplify
each job: an analyst should hold only the analysis. Sharing the mandatory
collection contract with review authors, comparison writers and method authors
exposes analysts to unrelated rules and to their future growth. Measured per
analyst role, a separate collection removes five to seven unrelated concerns;
shortening the shared contract removes one. Reduced input does not by itself
establish better analyses.

## Proposed decision

Create `kb/agentic-system-analyses/` as a self-contained collection. It owns
its contract, the analysis method (skill, run driver, job instructions and
shared analysis contracts), the member and run-state types, ignored run state,
current accepted sets and archives. `kb/agentic-systems/` keeps hand-authored
reviews, comparisons, landscape synthesis and taxonomy maintenance.

The accepted overview is the reader-facing review; the workflow writes no
second synthesis. The current analysis of a system lives at
`retained/<system-slug>/`, a path that does not change between runs. Links to
it follow the newest analysis. Publication moves the previous set unchanged to
`retained-archive/<run-id>/` and copies the accepted set into the stable path,
in one commit. The list of current analyses is generated at site build from
the sets in `retained/`; no list file or per-system reference is committed.
Comparison tools enumerate the current sets through the same function.

Migrate nothing. Every analysis is regenerated under the new method, and the
new collection starts empty. The old `kb/agentic-systems/reports/` tree stays
in place as frozen history, excluded from validation and from the comparison
population. No hash map or repinning is needed. The one generated review that
pins an old set is retired when the member types move.

## Considered alternatives

**Shorten the existing contract.** Avoids relocation and obtains most of the
byte reduction. Lost because it keeps rules for other artifact classes in the
analyst's contract and leaves that contract open to their growth.

**Exempt workers from the collection read.** Lost because it resolves a
contradiction between root doctrine and job packets by exemption.

**Move only the types.** Violates local type eligibility.

**Keep the method in `kb/agentic-systems/`.** Lost to self-containment: no
worker packet should name a file in another collection.

**Per-system reference files, or a committed list file.** Lost because
directory membership already states what is current, and a generated list
needs no pointer type, hash pin or atomic list update.

**Run-ID directories with generated or committed redirects.** Redirects keep
web addresses stable but not Markdown links inside the KB, which target file
paths. About 65 KB files link to a review by path. Lost for that reason;
see the first revisit condition.

**Migrate the retained sets and archive.** Lost because all analyses are
regenerated; migration would add a hash map and repinning for sets that are
about to be replaced.

**A separate `superseded/` area.** Not chosen, to avoid a third area without
evidence of need. Since nothing is migrated, the new archive holds only
superseded sets of the current contract; see the second revisit condition.

## Consequences

Workers receive the new contract explicitly as a job dependency. Local type
resolution and validators enforce membership. The site build and comparison
tools consume the sets in `retained/`; validation enforces one set per source
identity and that a directory's name matches its set's source. Projected
research skills point at the new collection. These are the decision's
consumption paths.

A retained directory is no longer named by its run ID, and its content is
replaced on publication. A link to the current path changes target when a new
analysis is accepted; a claim that depends on a specific analysis must cite
the run ID and commit.

The decision does not alter analytical definitions, waive acceptance gates,
authorize correction of retained findings, change generic collection rules, or
allow old runs to adopt a new method commit. A live evaluation run is separate
authority.

## Revisit conditions

Both choices below were made without evidence from use. Keep the literal
`TODO` markers when this draft becomes the ADR, so a search over ADRs finds
them. Remove a marker only when its check has been done and recorded.

**TODO: revisit the stable path per system and links that follow the newest
analysis.** Check after the first few systems have been analysed twice under
the new layout, or earlier if one of these is observed:

- a note, comparison or synthesis whose claim no longer matches the analysis
  its link now reaches;
- a reader or tool that needed a superseded set and could not find it from
  the current path;
- a publication that left `retained/<system-slug>/` partial or replaced the
  wrong set;
- citations by run ID and commit proving too awkward for authors to use.

Count the inbound links to current paths, how many needed a pinned version,
and how often a replacement changed a cited finding. The alternative to weigh
is run-ID directories with generated or committed redirects.

**TODO: revisit the archive for superseded sets.** Superseded sets go to
`retained-archive/`, which is excluded from current validation. Check at the
same time as the condition above, or earlier if one of these is observed:

- a need to validate superseded sets under the current schema, which the
  archive's validation exclusion prevents;
- a comparison of two analyses of one system that is hard to assemble from
  the archive;
- archive growth that makes the directory hard to use.

The alternative to weigh is a separate `superseded/` area.
