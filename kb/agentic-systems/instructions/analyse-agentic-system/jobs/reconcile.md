---
description: "Job of an analyse-agentic-system run: settle the three analysts' records through amendments, supersessions and explicit unresolved conflicts"
type: types/instruction.md
---

# Reconcile the analysts' records

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first`, `after-correction`, or `after-blockers`. | Always |
| `may-return` | `yes` permits returning findings; `no` prohibits it. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the runtime member. | Always |
| `memory` | Absolute path of the selected memory report. | Always |
| `epistemic` | Absolute path of the epistemic member. | Always |
| `previous-reconciliation` | Absolute path of the previous reconciliation. | `after-correction` or `after-blockers` |
| `verification` | Absolute path of the verification whose blockers you must resolve. | `after-blockers` |
| `set-check` | Absolute path of the structural check for that verification. | `after-blockers` |

## Task

Write `output` with `## Reconciliation`, under the supplied reconciliation
report type. Code writes the retained member's identity and copies this
section unchanged. Do not write Description, Bounded synthesis or Limitations.

## Reconcile

Reconcile the members as they are; when `round` is `after-correction` or
`after-blockers`, read `previous-reconciliation` and recheck anything you
carry over from it rather than copying its text.

Resolve duplicates, corrections and anchored conflicts under the shared
record contract's amendment grammar. Check `Part of:` relations without
superseding valid containers. A split supersedes a combined record only by
parts already declared in analyst members, with identity evidence and
affected findings; never allocate IDs or declare split parts here. If a
required part is missing, return it when the memory analyst should declare
it and `may-return = yes`; otherwise retain an `Unresolved conflict:` naming
the combined ID, missing part in prose, evidence and prevented conclusion.
Report independent convergence only
when the analysts reached it independently. Recheck shared-route ownership.
Attach the admission fields of memory routes from the memory analyst's
findings rather than tracing those mechanisms twice. The memory analyst's
`memory-comparison` profile stays in the memory member with its scope,
per-value evidence bases and records, coverage assessments, uncertainties,
and rationale preserved; check it axis by axis, under the definitions of the
[memory report type](../../../types/agent-memory-analysis-report.md)'s
Memory comparison fields, against the records of the whole set, including
every `EPI-` record of a transformation of retained content. Do not draft a
second memory analysis, and do not silently strengthen the memory analyst's
findings.

Every ID you cite, in amendments too, must resolve in the set your output
makes: the Source register, the runtime member, the memory report and the
epistemic member. Your output is refused with the unresolved IDs otherwise.
Keep the declaring analyst's prefix when amending another member's finding:
an epistemic finding about `RT-RTE-5` is amended as `Amendment: RT-RTE-5`,
with the epistemic member named under affected findings.

## Return findings to the memory analyst

When a substantive conflict needs the memory analyst, add the section
`## Returned to the memory analyst`, listing each returned finding with its
IDs and evidence anchor. Place it after `## Reconciliation`; the accepted
heading order is Reconciliation, then the optional memory return.
Code then runs a correction round of the memory
analyst and gives you its report in the next reconciliation. Return findings
only when `may-return = yes`. When `may-return = no`, retain each unresolved
conflict in a paragraph starting `Unresolved conflict:`, with its full IDs,
evidence and conclusion prevented. The later synthesizer carries these
conflicts into Limitations. A malformed citation in the memory analyst's
report is also a return, not something you fix.

## Resolve a verification's blockers

When `round = after-blockers`, read `verification` and `set-check`. Resolve
each blocker in what you write: correct the reconciliation; amend or
supersede a record through an `Amendment:` paragraph; or return it to the
memory analyst when the memory report is at fault. The runtime and epistemic
members are not rewritten; a blocker in one of them that no amendment
resolves stays an `Unresolved conflict:` with its prevented conclusion. Read
`previous-reconciliation` too: carry over what still holds.
