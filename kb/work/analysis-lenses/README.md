# Analysis lenses

## Governing question

**How do we allocate limited analysis resources across repositories whose code
is too large to cover exhaustively?** Resources include worker context, model
and tool time, review effort, and the operator's cost of consuming the result.

The intended result is a defensible account of what to investigate, how deeply,
when to stop, and how to report what remains unknown. The operator commissioned
this workshop on 2026-10-11 after discussing the
[analysis audits](../analysis-audit-evidence/README.md), then clarified this
resource-versus-coverage question as its main goal.

The [analysis design brief](../../reference/agentic-system-analysis-design-brief.md)
already establishes the overall goals: map the design space and identify solutions
worth borrowing for Commonplace. This workshop develops how analysis scope and
worker responsibilities serve those goals; it does not replace the brief.

## Standing premise

The process has only recently stabilized and has substantial supporting
machinery. Preserve that investment. This is a design investigation, not
authorization to redesign the engine or implement a new workflow. Retaining the
current arrangement with clearer scope is a valid result.

The current method already has the shape discussed with the operator: a general
runtime layer, question-driven memory and epistemic lenses that receive the
runtime record, reconciliation, and independent verification. The workshop's
real question is therefore depth, stopping and coverage reporting inside those
roles, not whether to introduce the shape. See
[current arrangement](./current-arrangement.md) before reading anything else.

## Documents

| Document | Contents |
|---|---|
| [Current arrangement](./current-arrangement.md) | What the live plan and role instructions already decide about layers, lens inputs, stopping and coverage; the baseline every option is compared against |
| [Design direction](./design-direction.md) | Intentions established with the operator, preservation defaults and the least-disruptive-change ladder |
| [Open questions](./open-questions.md) | Each unresolved question with its current answer and the evidence that would discriminate |
| [Evidence base](./evidence-base.md) | Audits, trace measurements and the frozen source worktrees; what each can and cannot show about coverage |
| [First deliverable](./first-deliverable.md) | The first comparison to produce, its evaluation criteria and the return-to-operator condition |
| [Comparison plan](./comparison-plan.md) | Executable handoff for correcting workshop premises and comparing three coverage policies using retained cases; no live method changes |
| [Multi-repository scope plan](./multi-repository-scope-plan.md) | Use Ars Umbris to compare component analyses with a fixed repository bundle, balancing coverage against workflow and implementation complexity |
| [Retained multi-repository scope comparison](../../reports/retained/multi-repository-analysis-scope-2026-10-11/multi-repository-scope-comparison.md) | Prefer one frozen source tree for the Ars Umbris cross-component question; retain component evidence, quotation/source-ID audit and change footprint |
| [Proposal: multi-repository agentic-system analysis](../../reference/proposals/multi-repository-agentic-system-analysis.md) | Cover multi-repository systems using repository directories while preserving roles, source IDs and path-only quotations; unadopted |
| [Coverage policy comparison](./coverage-policy-comparison.md) | Adopted prose-only clarification: consequential-question omission checks with effort-sensitive stopping and brief coverage reporting; retained-case evidence and implementation footprint |
| [Proposal: verification coverage bounds](./proposals/verification-coverage-bounds.md) | Unadopted operator proposal of 2026-10-11: add structural accounting at runtime and bound lens omission checks; original exhaustive-duty premise qualified against the live type |

## Scope and coordination

The operator also commissioned the
[multi-repository scope plan](./multi-repository-scope-plan.md): use Ars Umbris
to compare bounded component runs with an explicitly frozen repository bundle.
This authorizes local read-only scoping and workshop design work, not acquisition,
source-ID removal or bundle implementation.

This workshop owns resource allocation and coverage limits in analysis; lens
and scope design are possible means of addressing that question. The
[audit evidence workshop](../analysis-audit-evidence/README.md) continues to own
audit accumulation and cross-run evidence, including any coverage audit this
workshop asks for. The
[amendments workshop](../analyse-agentic-system-amendments/README.md) contains
related correction and contract-design history; its candidates are not an
implementation backlog for this workshop.

The initial commission authorized workshop framing, navigation and comparison.
The operator subsequently authorized revising and implementing the comparison's
prose-only recommendation: report-verifier stopping and search authority, and
brief coverage reporting. That change is implemented in the canonical worker
instructions and verification type; no roles, dependencies, schemas or engine
code changed. Existing analyses and run state remain unchanged. Quality and cost
improvements remain unmeasured. Commit the method before new runs; repeat-run
commands requested by the operator are a separate invocation, not a run launched
by this workshop. Transfer scans, integration, commits and worktree disposal
still need separate authorization. Deterministic measurements over retained records
and frozen worktrees are within scope when they write only under this workshop.
Before separately authorized method work, follow
[method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md).

## Closure

Close when the operator has accepted a minimal-change design, chosen to retain
the current process, or explicitly deferred the question. Extract any adopted
requirements and useful evidence to their appropriate durable locations. If
implementation is commissioned, give it a bounded plan and explicit acceptance
criteria; this framing is not that plan. Remove the workshop and its active-list
entry only after extraction or explicit disposition.
