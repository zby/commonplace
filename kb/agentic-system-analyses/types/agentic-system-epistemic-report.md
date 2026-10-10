---
type: types/type-spec.md
name: agentic-system-epistemic-report
description: "Epistemic member of an analysis set: the five-block sparse overlay tracing the system's truth-apt routes over the set's records, and the EPI- records the epistemic analyst establishes"
schema: ./agentic-system-epistemic-report.schema.yaml
record-prefix: EPI-
---

# Agentic system epistemic report

The member of a run's retained set that carries the epistemic analyst's
findings: a sparse overlay on the set's canonical records tracing whether
and how the system acquires or produces truth-apt content, checks it, grants
or withholds reliance, retains or integrates it, and lets it affect later
behavior. It cites the records other members declare, and it declares the
records the epistemic analyst establishes under their `EPI-` IDs, with the
evidence passages that support them. The
[record contract](../instructions/agentic-analysis-records.md) governs
identity, common fields, statuses and evidence interpretation.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-epistemic-report.md` |
| `description` | Yes | Retrieval description naming the system and the analysis question |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's frozen revision or capture identity |

## Terms

An **epistemic architecture** is the set of routes by which a system
acquires or produces truth-apt content, checks it, grants or withholds
reliance, retains or integrates it, and lets it affect later behavior.
**Truth-apt content** is content whose truth or falsity can be stated over
a named scope. A route is **material**, and inside the epistemic analyst's scope, when
it produces or changes truth-apt content; checks or disposes a candidate;
grants, withholds, or changes epistemic or operational authority; retains
or integrates a candidate for later reliance; directly adapts behavior or
policy from evaluation; or is necessary to assess a consequential
knowledge or warrant claim the system makes. Transport, storage,
retrieval, formatting, freshness, and recovery plumbing is material only
when it changes lineage or warrant, carries consequential force, or
belongs to such a claim.

The **check target** is the object, proposition, or class and domain being
assessed. The **evaluator** is the human, model, program, environment,
proof, measurement, or hybrid procedure that judges it. An **operative
result** is consumed to change admission, rejection, revision, acceptance,
retention, integration, rollback, use, ranking, or continuation.
**Epistemic authority** is the content and scope licensed for reliance;
**operational authority** is the behavior a result permits, blocks, or
changes before another check; the **behavioral-authority path** is the
consumer, channel, force (advisory, ranking, permissive, or enforcing),
and horizon through which a result affects behavior. **Acceptance**
is a recorded, evidence-consuming decision against a named criterion for
an intended use and scope. **Lifecycle integration** occurs only after
acceptance, when the accepted claim is connected to evidence or changes
organization or use; retention or operational use before acceptance is a
separate ledger function.

## Assessment limits

Each content edge is assessed separately. Entailed derivation carries
warrant only from warranted premises through a checked interpretation or
formal domain. Novelty, fluency and plausibility establish candidate
generation only. A produced accepted ampliative claim requires an
evidence-consuming acceptance decision naming criterion, intended use and
scope; retention, retrieval, reshaping or operational use alone does not
establish it. Imported content is acquired, not produced. Acceptance does
not establish infallibility, and integration does not establish acceptance.

Architectural status is separate from activation conditions and evidence
that a route operated. Implementation or doctrine does not establish observed
operation. A persisted candidate artifact with no provenance or trace links to
the routes establishes only that a candidate instance is available; it does
not establish which routes produced, checked or accepted it. A
recorded result without a consequential consumer has no implemented force.
An evidenced absence does not require an invented evaluator.

A check's license is bounded by target, contrast, domain, horizon and
route. Outcome success does not establish the producing process,
explanation, replay safety, transfer or component effect. A reconstructed
route does not prove it produced the observed outcome. Consequence fit
does not warrant the proposed mechanism or its transfer. Formal validity
does not establish source truth, encoding fidelity, omitted premises or
claims beyond the checked domain. Freshness does not establish endorsement;
operational continuation does not establish epistemic warrant. Causal
attribution follows the record contract's comparison limits.

An intentionally operational or lab-tracking scope is not product failure;
broader knowledge-production claims still require comparison with the
routes. The assessment imposes no natural-language claim format, proposal
loop, Commonplace storage model or universal ontology. Heterogeneous routes
retain separate evaluators, statuses and authorities. Coverage, uncertainty
and the independence of learning, reflection, autonomy, self-improvement and
theory-builder conclusions follow the record contract's coverage rules.

## Required blocks

The body contains five level-two sections in order, as readable Markdown
tables or compact records, followed by `## Shared records`. Each block
cites records by link and repeats at most the citation, one source-native
short label, and one local evidence anchor; a field the declaring record owns
says `see` and cites the record. Architectural status is this report's own field;
use its controlled values rather than the set's conclusion-status vocabulary.

**1. Source-and-claim boundary.** Declared scope and excluded components,
the analysis question, assessed and unassessed route families, each
missing item of evidence with the conclusion it prevents, and the
system's knowledge-production or warrant claims, citing their `CLM-*` records, or
`none found`. It cites the boundary's Source register and does not copy it.

Retain a compact coverage table: entry point or operation, source path,
citations of the supplied or new records covering it, or exclusion/uninspected reason and conclusion
prevented. Distinguish direct source reads from supplied runtime findings;
an unassessed relevant operation prevents a system-complete negative.

**2. Epistemic-object inventory.** One row per operative part within the
material-route boundary, split where parts differ in content, form,
checks, producers or consumers, or authority paths:

`object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit`

**3. Authority-route ledger.** One row per consequential function, split
where the function, target, evaluator domain, timing, result, force,
epistemic license, operational consequence, consumer, channel, or horizon
differs; linked rows where one implementation performs several functions:

`route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit`

Route function is one of `content transformation`, `check/evidence
production`, `disposition/acceptance`, `retention`, `lifecycle
integration`, `operational admission/selection/consumption`,
`behavior/policy adaptation`, `lineage/freshness/recovery`, or `other —
describe`. Checking is never merged with disposition, nor retention with
lifecycle integration.

Table rows stay contiguous with their header and Markdown separator. Put
supporting quotations after the table, or repeat the header and separator
before resuming rows. Escape a literal pipe inside a cell as `\|`, including
inside an inline code span. Orphan rows, unequal cell counts, and invalid
route-function or architectural-status values are refused.

In compact records, start each record with `Route ID: <record citation or citations>`
on its own line. Use `Route function: <value>` and
`Architectural status: <value>` once each on their own lines, followed by
the other named ledger fields and evidence. These labels are literal;
the values may use inline code formatting. For an empty ledger use exactly
`no route found within boundary`, with its searched scope elsewhere in
the report.

Architectural status is one of `implemented` (inspected implementation
supports the route); `observed, implementation uninspected` (run evidence
shows the route operated, but its implementation was not inspected);
`doctrine only` (the route is declared, but no implementation or observed
route was found within the recorded search boundary); `no route found
within boundary` (neither inspected implementation, observed operation,
nor doctrine establishes the route within the recorded search boundary);
or `not determinable` (the available evidence cannot distinguish these
states).

Content/update relation is one of `truth-apt transformation:
acquisition/import` (external content enters the system, with source
warrant recorded as preserved, degraded, or unknown); `truth-apt
transformation: non-ampliative reshaping` (truth-apt content is only
reordered, indexed, grouped, reformatted, deduplicated, or compressed);
`truth-apt transformation: entailed derivation` (a new proposition follows
from its inputs); `truth-apt transformation: ampliative conjecture` (a
truth-apt proposition does not follow from its inputs); `truth-apt
transformation: indeterminate` (semantic preservation or entailment cannot
be established, with the remaining classifications and the evidence needed
to decide); `non-truth-apt policy/content update: <description>`; or `no
content change`.

The list supplies a checking order: assign the first value whose test is
established. Ampliative conjecture requires evidence of non-entailment;
failure to prove entailment alone leaves the relation indeterminate.

**4. System-claim versus route comparison.** One row per consequential
public or design claim, or an explicit statement that none was found:

`claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown`

**5. Bounded conclusion.** Only findings that change the answer to the
analysis question, grouping homogeneous records whose warrant and force are
the same: what the system retains, retrieves, reshapes, or uses; what it
acquires and whether source warrant is preserved, degraded, or unknown;
what it derives, from which warranted premises, and within what domain;
what it conjectures, tests, accepts, and integrates; each material
acceptance criterion, intended use, scope, operational authority, and
behavioral-authority path; any direct behavior or policy adaptation
without a truth-apt route; and which claims remain unsupported because
implementation, run, or causal evidence is missing. It gives the system no
single epistemic score, oracle, status, or unqualified verdict.

## Shared records

This section declares records the epistemic analyst establishes, with
`EPI-` IDs, under the shared record contract. Include the kind headings
for declared kinds, source anchors and minimum load-bearing passages;
state `none declared in this member` when there are no declarations.
Apply conditional route fields only within their stated scope. Read-back
fields give an inapplicable reason when neither retention nor read-back
occurs.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} epistemic report

## Source-and-claim boundary

## Epistemic-object inventory

## Authority-route ledger

## System-claim versus route comparison

## Bounded conclusion

## Shared records
```
