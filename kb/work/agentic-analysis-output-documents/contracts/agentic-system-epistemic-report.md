# Agentic system epistemic report (draft type)

The member of a run's retained set that carries the epistemic lens: a
sparse overlay on the set's canonical records tracing whether and how the
system acquires or produces truth-apt content, checks it, grants or
withholds reliance, retains or integrates it, and lets it affect later
behavior. It declares no records and holds no evidence passages; it cites
them. Set-wide conventions are those of the
[overview](./agentic-system-analysis-overview.md#the-set).

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-epistemic-report.md` |
| `description` | Yes | Retrieval description naming the system and the analysis question |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's frozen revision or capture identity |

## Terms

An **epistemic architecture** is the set of routes by which a system
acquires or produces truth-apt content, checks it, grants or withholds
reliance, retains or integrates it, and lets it affect later behavior.
**Truth-apt content** is content whose truth or falsity can be stated over
a named scope. A route is **material**, and inside the lens boundary, when
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
and horizon through which a result affects behavior. The **discovery
lifecycle** comprises observation or anomaly, conjecture, consequence
derivation, test or evidence, acceptance, and integration. **Acceptance**
is a recorded, evidence-consuming decision against a named criterion for
an intended use and scope. **Lifecycle integration** occurs only after
acceptance, when the accepted claim is connected to evidence or changes
organization or use; retention or operational use before acceptance is a
separate ledger function, and a candidate retained or used without
acceptance has integration `not reached`.

## Required blocks

The body contains six level-two sections in order, as readable Markdown
tables or compact records. Each cites canonical IDs and repeats at most
the ID, one source-native short label, and one local evidence anchor; a
field the canonical record owns says `see <canonical ID>`. Architectural
status and observed candidate state are this report's own fields and are
never concatenated with one another or translated into the set's
conclusion-status vocabulary; `implemented and observed` is not a value in
any field.

**1. Source-and-claim boundary.** Declared scope and excluded components,
the analysis question, assessed and unassessed route families, each
missing item of evidence with the conclusion it prevents, and the
system's knowledge-production or warrant claims by `CLM-*` ID, or `none
found`. It cites the overview's Source register and does not copy it.

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

**4. Per-object lifecycle disposition.** For every ampliative candidate,
one record keyed to its object ID, giving for each phase the route's
architectural status separately from the observed candidate state:

`candidate object ID | relevant route IDs | transformation: ampliative conjecture | observation/anomaly: route IDs + architectural status + observed candidate state + evidence | conjecture: route IDs + architectural status + observed candidate state + evidence | derived consequence: route IDs + architectural status + observed candidate state + evidence | test/evidence: route IDs + architectural status + observed candidate state + evidence | acceptance: route IDs + evaluator + criterion + intended use + architectural status + observed candidate state + accepted scope + evidence | lifecycle integration: route IDs + post-acceptance change/consumer + architectural status + observed candidate state + evidence | missing phase/evidence`

Observed candidate state is one of `no instance observed` (no candidate
artifact or trace is available within the evidence boundary); `not
reached` (an observed candidate exists and evidence shows that it did not
reach this phase); `phase evidenced` (an observed candidate traversed this
phase); `accepted`, `rejected`, `revised`, `failed`, `suspended`, or
`integrated` (an observed disposition supports that specific state,
`suspended` only for a candidate deliberately held pending, not a disabled
route); or `not determinable` (candidate evidence exists but does not
determine the state).

For non-ampliative truth-apt content:

`candidate object ID | relevant route IDs | transformation | discovery lifecycle: not applicable | applicable acquisition, lineage, derivation, or update route and warrant | missing evidence/limit`

When preservation, entailment, or ampliation cannot be decided:

`candidate object ID | relevant route IDs | transformation: indeterminate | classifications still possible | preserved lineage | implemented checks, retention, or use | current warrant limit | evidence needed to decide preservation, entailment, or ampliation`

For an object with no candidate truth-apt output: `No lifecycle record for
<object ID>: no candidate truth-apt output for this object; relevant
direct-adaptation or update routes: <route IDs or none>.` Only when the
entire inventory contains no candidate truth-apt output, additionally: `No
candidate lifecycle records: no candidate truth-apt output found within
the source boundary.`

**5. System-claim versus route comparison.** One row per consequential
public or design claim, or an explicit statement that none was found:

`claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown`

**6. Bounded conclusion.** Only findings that change the answer to the
analysis question, grouping homogeneous IDs whose warrant and force are
the same: what the system retains, retrieves, reshapes, or uses; what it
acquires and whether source warrant is preserved, degraded, or unknown;
what it derives, from which warranted premises, and within what domain;
what it conjectures, tests, accepts, and integrates; each material
acceptance criterion, intended use, scope, operational authority, and
behavioral-authority path; any direct behavior or policy adaptation
without a truth-apt route; and which claims remain unsupported because
implementation, run, or causal evidence is missing. It gives the system no
single epistemic score, oracle, status, or unqualified verdict.

## Template

```markdown
---
type: types/agentic-system-epistemic-report.md
description: "Epistemic routes of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} epistemic report

## Source-and-claim boundary

## Epistemic-object inventory

## Authority-route ledger

## Per-object lifecycle disposition

## System-claim versus route comparison

## Bounded conclusion
```
