---
description: "Proposal: attach independently verified, run-bound additions and corrections to frozen analysis pages until a full rerun replaces the analysis, without adding approval or statistics migration gates"
type: reference/types/design-proposal.md
brief: temporary-amendments-to-published-analyses.brief.md
---

# Temporary amendments to published analyses

Allow readers to see bounded additions, corrections and staleness qualifications
alongside a published analysis without regenerating its entire report set.
Keep the original analysis frozen. Attach each amendment to one exact run and
remove it from the current display when a replacement run becomes current.

This is a proposed extension to analysis publication and display, not an adopted
workflow. The operator's design constraints are recorded here; writing this
proposal neither authorizes implementation nor changes any active run.

## Current state (as of 2026-10-13)

The [analysis collection contract](../../agentic-system-analyses/COLLECTION.md)
keeps retained analyses frozen and requires a new run for substantive corrections.
The publication implementation in `src/commonplace/lib/agentic_analysis/publication.py`
records member digests and archives a replaced analysis under its original run
identity. The site configuration selects named retained report members for
publication. A separately verified, post-publication amendment and its attachment
to those display pages are not part of that contract.

The [records contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md)
now asks analysts to describe working-context eviction: removal of material from
the model-visible context between invocations, including triggers, decision-makers,
what is removed, what remains reachable and reload routes. It adds descriptive
coverage rather than removing old fields or adding controlled profile values.
Existing analyses can therefore lack this new coverage without their earlier
findings necessarily being wrong.

The [reconciliation report contract](../../agentic-system-analyses/types/agentic-system-reconciliation-report.md)
already governs connections and disagreements within a run. Its record-level
amendments are not the post-publication amendments proposed here. This proposal
does not alter reconciliation or reuse its record grammar as a publication API.

## Problem and forces

A full rerun is expensive when the new question concerns one bounded mechanism.
Editing accepted files in place would obscure what the original run produced.
Leaving them untouched without a visible qualification would hide known errors
or changes from readers.

The design must preserve these distinctions:

- **Additional coverage:** an earlier analysis did not answer a newly introduced
  question. Silence in that analysis is not evidence of absence.
- **Correction:** a claim was wrong or insufficiently qualified even at the
  original source boundary.
- **Later-source change:** the historical account may be correct, but no longer
  describes a newer source revision.
- **Unresolved staleness:** there is a reason to question present applicability,
  but not yet evidence for a replacement claim.

Amendments must be easy to find, independently checked and cheap enough to use
for local changes. They must not become a second, fragmented analysis that a
reader has to assemble mentally. They are temporary for current presentation,
not disposable as historical evidence.

## Options and candidate selection

| Option | Consumption path and effect | Trade-off |
|---|---|---|
| Full rerun for every substantive addition or correction | The existing analysis workflow produces and publishes a replacement set. Readers receive one newly checked account. | Preserves the current contract but repeats unrelated analytical work. |
| Edit the retained reports directly | Existing readers and extractors consume changed report bytes at the old publication location. | Gives immediate visibility but breaks the frozen-output boundary unless the publication model is redesigned. Not the candidate selected here. |
| Separate run-bound amendments | A new production path creates checked amendments; display pages select amendments by exact run identity without changing report bytes. | Adds production and display responsibilities, but limits new analytical work to the commissioned question. This is the proposed direction. |

The third option complements full reruns rather than replacing them. Exact
storage, schemas and commands are deferred. The required new consumers are an
amendment producer with independent verification, a guarded publication path,
and page rendering that attaches amendments to the correct run. No such consumer
is implied merely by placing a Markdown file near an analysis.

## Run-bound amendment

An amendment identifies the original run and the reports or claims it affects.
Its content distinguishes an addition, correction, later-source update or
qualified warning. It records the question, source evidence, source boundary,
findings, verification outcome and limits needed to interpret it.

A same-snapshot addition uses the original frozen source. A later-source update
names the later revision and does not attribute its behavior to the old one.
An unavailable source or unresolved discrepancy remains an explicit limitation,
not an invented negative or a silently broadened evidence boundary.

The amendment remains separate from the accepted report bytes and their recorded
checks. Publishing it does not assert that the original run complied with a
method introduced afterwards. It also does not silently upgrade the original
summary, memory profile or verification result.

For the eviction example, a producer could investigate the original snapshot's
context-removal mechanisms and publish a bounded addendum. It would say what
was found and what remains unknown, rather than claiming the full analysis had
been rerun under the expanded contract.

## Producer-owned independent verification

The producer commissions a fresh verifier as part of producing the amendment.
The verifier receives the proposed amendment, affected original claims, relevant
source evidence and applicable contracts, without inheriting the producer's
conversation. It checks factual support, source-version attribution, affected
scope and whether the amendment remains a coherent local change.

Findings return to the producer for correction through a bounded loop. A passing
verification allows guarded publication under the existing commission; this
proposal adds no separate operator approval for each amendment. Unresolved
findings remain a stopped production result, not a verified correction.

The verifier can determine that a full rerun is required. That outcome does not
itself authorize launching one outside the existing commission. A verified
warning can still identify what readers should not rely on while the rerun is
pending; unsupported replacement claims cannot be published as corrections.

Deterministic checks can establish attachment identity, required metadata and
reference integrity. They cannot establish that a source interpretation is true
or that a change is semantically local. Independent verification provides the
source-based judgment for those questions, with its evidence limits retained;
it is not an infallible oracle. Neither check re-certifies the unchanged analysis.

## Display and reader notice

The overview and each affected report page expose a prominent notice linking
to, or displaying, the amendment. The notice distinguishes original publication
from later material and makes the source boundary and verification status clear.
A reader must not have to discover a separate index to learn that a visible
claim is known to be unreliable.

Additional coverage need not be incorporated into existing summaries. Where a
correction affects a summary or profile conclusion, that page also carries a
warning; its original text remains unchanged. This is a display qualification,
not regeneration of the summary or a silent change to its structured values.

The display consumer matches exact run identity, not just the system name or
current directory. Attachment must remain correct as the current publication
changes. Direct consumers of raw report files would still see the original
bytes; this design must not claim those consumers have received a display-only
qualification. How to expose associated amendment discovery to such consumers
is an adoption choice, not a reason to rewrite the original reports.

## When a full rerun is needed

Local amendments fit when the affected claims can be identified, the added or
corrected account is understandable without rebuilding the surrounding reports,
and cross-report consequences can be clearly bounded.

A full rerun is the appropriate outcome when a change overturns the central
account, requires substantial cross-report reconciliation, rebuilds core
synthesis conclusions, or combines with earlier amendments into a fragmented
replacement analysis. Scope and coherence govern this distinction, not word
count or a fixed number of amendments. A one-sentence correction can have wider
consequences than a long additional description.

Known-outdated or unreliable claims retain visible qualifications while a
required rerun is pending. The absence of a completed replacement is not a
reason to display them without warning.

## Replacement automatically ends applicability

Every amendment belongs to a particular run, not indefinitely to a system.
When a replacement analysis becomes current, the old amendments leave the
current display with the old run. They remain associated with that historical
run as retained evidence, whether or not the archive is publicly rendered.
They are never automatically attached to the replacement.

There is no per-amendment incorporation, resolution or approval gate on the new
run. Replacement ends applicability; it does not certify that each earlier
issue was fixed. A problem discovered in the replacement requires an amendment
that targets the replacement run. Historical amendment findings must not be
silently injected into source-first analysis worker handoffs.

## Statistics remain outside this change

Added descriptive coverage preserves existing report fields so current
statistical procedures can continue to consume their existing inputs.
Amendments do not automatically change statistical extraction, introduce new
structured values or update previously generated statistics. Existing statistics
therefore still describe their original report inputs; reader-facing amendments
are not a claim that those statistics have been recomputed.

When a later report or collection change introduces a field that older reports
lack, that change decides how to treat them for its statistics. Excluding old
reports, narrowing dimensions or backfilling are decisions for that concrete
change. This proposal selects no general eligibility rule, migration framework
or amended-value precedence mechanism.

## Adoption criteria and remaining choices

Adoption needs a producer and independent-verification path, guarded amendment
publication, and a display consumer that can demonstrate all of the following:

- A bounded, source-grounded addition can be produced without rerunning the full
  analysis or altering any frozen report bytes.
- A correction is visible on affected report and summary pages, with its source
  boundary and limits intact.
- An unsupported amendment is refused, and an overly broad change is routed to
  a full rerun rather than accepted as a local patch.
- A replacement run loses the old amendments from its current display without
  losing their historical association or imposing a new resolution gate.
- Existing fields and statistical procedures remain usable without silently
  treating amendment prose as structured replacement data.

Before implementation, choose the storage and publication boundary, how display
pages discover amendments, how direct-file consumers discover them, and the
bounded correction-loop behavior. Test attachment under replacement and archive
movement as well as rejection of mismatched run identities. The adoption
comparison should include production cost and reader clarity against a full
rerun, not only whether a notice can be rendered.
