# Worker information map

- **Commissioned:** 2026-10-01, by the operator: map what each worker needs, reorganize the files around that map, remove redundancies, commit, then check for further simplification.
- **Purpose:** reduce required reading while preserving the analysis questions, evidence standards, report fields, correction policy and publication behavior.
- **Acceptance:** every required definition reaches its worker through a declared dependency; each rule has one owner; affected jobs reopen after a dependency change; publication pins the shared files; contracts and instructions validate; Python checks pass.

## Information each worker needs

| Worker | Result and judgment | Required information | Run inputs | Information outside this job |
|---|---|---|---|---|
| Orchestrator | Launch the jobs code names and report events | Skill scope, repository-root precondition, driver loop, exact launch and stop protocol | Run directory and saved prompts, permitted block records | Analytical contracts, source findings and worker outputs |
| Boundary | Establish scope and freeze the evidence | Worker authority and parameters; target and boundary classifications; source identity, evidence layers and Source register contract | Opening metadata and caller source data | Route fields, memory axes, epistemic lifecycle, synthesis and verification |
| Runtime | Trace invocation, alternate paths and guarantees | Worker rules; source/evidence contract; shared record fields and interpretation; runtime account and probe contract | Boundary | Memory profile enums, epistemic ledger, overview synthesis and publication mechanics |
| Memory, first round | Explain retained memory and classify its routes | Worker rules; source/evidence contract; shared record fields and interpretation; memory scope, axes and report contract | Boundary and runtime member | Runtime account/probe production, epistemic ledger production, overview synthesis |
| Memory, correction | Revise its report against returned findings | First-round requirements plus correction ID continuity and replacement protocol | Boundary, runtime, previous memory, returned findings and epistemic member | Other members' production procedures |
| Epistemic | Assess truth-apt content, checks, authority and lifecycle | Worker rules; source/evidence contract; shared record fields and interpretation; epistemic terms, ledger and dispositions | Boundary and runtime member | Runtime account/probe production, memory profile enums, overview synthesis |
| Reconciliation | Resolve cross-member findings and write public synthesis | Worker rules; source/evidence and shared records; all four member contracts; amendment and return protocol | Boundary and three members; prior reconciliation after a correction; verification and set check after blockers | Driver launch loop and publication commands |
| Verification | Judge the assembled set and name blockers | Worker rules; source/evidence and shared records; all four member contracts; semantic verification and blocker protocol | Overview draft, three members and set check | Source freezing, correction authorship and publication commands |

The source and record contracts are required in full. Conditional field applicability is stated inside the record contract; workers do not decide which definition files to load. The runtime's read-back definition currently points into the memory contract without declaring that file: the shared record contract must carry that definition directly.

## Ownership and file boundaries

| Information | Owner after reorganization | Consumers |
|---|---|---|
| Common invocation parameters, authority, missing input/access handling, command discipline, bounded reads, quotation command, prior-analysis exclusion | `jobs/worker-rules.md` | Every worker |
| Target classification, frozen boundary, source declaration, evidence layers, source anchors, retained quotation semantics | `kb/reference/agentic-analysis-sources.md` | Every worker |
| Record namespace, declarations, annotations, amendments, evidence statuses, generic and conditional record fields, theory/learning/reflection/autonomy interpretation | `kb/reference/agentic-analysis-records.md` | Runtime, memory, epistemic, reconciliation, verification |
| Runtime account, guarantees, execution preflight and probe capsules | Runtime type | Runtime, reconciliation, verification |
| Memory boundary, profile axes and meaning, memory-specific records/annotations, report content | Memory type | Memory, reconciliation, verification |
| Epistemic scope and terms, ledger, content relations, candidate disposition, conclusions | Epistemic type | Epistemic, reconciliation, verification |
| Overview identity, reconciliation, synthesis, limitations and verification content | Overview type | Reconciliation, verification; code assembles it |
| Inspection order, source coverage, correction procedure, validation command and job result | Each job instruction | Its worker |
| Scheduling, launch application, recovery and stop reporting | Skill and driver | Orchestrator |
| Manifest membership, completion hashes and public projection | Set, run-state and generated-review types; implementation | Code and downstream consumers; not required analyst reads |

`judging-norms.md` has no independent information after its norms and ownership rules enter the two shared contracts. Remove that dependency and file rather than retain a forwarding layer.

## Review rules

1. Preserve meaning when moving a rule. Remove a repeated statement only after its consumer loads the surviving owner.
2. Keep symbolic values and copyable templates available to authors. Do not replace short authoring guidance with a requirement to inspect large schemas.
3. Put instance properties in contracts and production steps in instructions. Keep evidence qualifications next to the findings they limit.
4. Update declared dependencies and publication method pins together. An inline documentation link alone does not deliver a requirement.
5. Preserve the existing uncommitted coverage, overlap, annotation and ledger fixes. Do not commit unrelated working-tree changes.

## Starting measurements

Type-contract bytes before reorganization, excluding job instructions and run-specific inputs:

| Worker | Bytes |
|---|---:|
| Boundary | 15,581 |
| Runtime | 28,562 |
| Memory | 43,789 |
| Epistemic | 42,050 |
| Reconciliation / verification | 57,277 |

These are UTF-8 byte counts, not tokenizer measurements. Reduced reading does not replace bounded tool deliveries.

## Reorganization measurements

Measured from the job constructors' declared dependencies after the first
pass. Fixed reading includes the job instruction, worker rules and shared
and member contracts; it excludes launch-message bindings and run inputs.
The starting versions include the pending audit fixes already present when
this work began.

| Worker | Fixed bytes before | Fixed bytes after | Reduction |
|---|---:|---:|---:|
| Boundary | 25,449 | 15,371 | 39.6% |
| Runtime | 39,933 | 28,765 | 28.0% |
| Memory | 57,998 | 39,016 | 32.7% |
| Epistemic | 62,706 | 41,118 | 34.4% |
| Reconciliation | 70,567 | 67,592 | 4.2% |
| Verification | 67,835 | 65,709 | 3.1% |

Most savings come from delivering fewer unrelated requirements. The
epistemic type grows because unique assessment limits moved out of its job;
the combined packet shrinks. All field vocabularies, templates, evidence
distinctions and correction limits remain available.

The reorganization removes one file (`judging-norms.md`), splits two shared
contracts out of the member types, consolidates common parameters and stop
rules, and updates the two downstream memory-classification consumers.
The existing ledger implementation and its fixture changes remain a
separate working-tree change; its formatting contract is preserved there.

## Verification

The targeted analysis, publication, member and instruction checks passed
(198 tests). Explicit validation of the shared files, four member contracts,
workflow instructions, downstream consumers, type landing and this map
reported zero failures and warnings. The full working-tree suite passed
1,197 tests. The isolated commit candidate, excluding the pending ledger
implementation, passed all 1,184 tests. Ruff passed for `src`, `tests` and
`scripts`; repository-wide Ruff found two existing import-order defects
inside the frozen retained reliability trial bundle.

The [post-commit simplification check](./post-commit-simplification-check.md)
records the remaining delivery gap and the larger changes that would be
needed for further cuts.
