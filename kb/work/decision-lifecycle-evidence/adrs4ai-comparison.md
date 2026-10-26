# ADRs4AI and Commonplace: deliberation records and architectural projections

## Status and scope

Retained on 2026-10-26 from the operator-requested comparison in this session.
This is a direct, selective inspection of the public repositories under the
[ADRs4AI GitHub account](https://github.com/ADRs4AI), not a completed
`analyse-agentic-system` run or an adopted Commonplace design.

All 12 repositories returned by the account's public repository listing were
shallow-cloned into `/tmp/adrs4ai-inspection/`. Inspection concentrated on the
methodology, templates, authoring skills, evaluation evidence and VS Code
implementation. That temporary directory is not a retention guarantee; pinned
public links below identify the inspected sources. No extension execution,
independent corpus measurement or reproduction of their evaluations was done.

## Main comparison

ADRs4AI expands ADR as **Architectural Deliberation Record**. Its record starts
before a choice is settled and retains originating context, the author's
interpretation, questions, attributed recommendations, answers, the decision,
follow-ups and iterations. A rough correspondence is a Commonplace workshop
plus its eventual ADR, rather than our ADR alone.

Commonplace's current [ADR type](../../reference/types/adr.md) is for made and
implemented architectural decisions. It retains recurring forces, the actual
choice, considered alternatives, consequences, applicability limits and the
consumer path through which the decision affects behavior. Unsettled design
work stays in the workshop layer; [ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md)
assigns change narrative to Git. These are the current contracts, not a
conclusion that they are the final retention model.

| Dimension | ADRs4AI | Current Commonplace contract |
|---|---|---|
| Entry condition | A topic needs deliberation; the choice can remain open | A choice has been made and implemented |
| Context | Originating input, sometimes verbatim; interpretation and assumptions | Forces that explain the choice and would recur if it were reverted |
| Alternatives | Options precede an attributed recommendation | Considered alternatives support later audit and revision |
| Open work | Questions, answers, follow-ups and action items within the record | Unresolved design work in workshops |
| Evolution | Stack attributed recommendations and append iterations | Retain decision lineage; leave change narrative to Git |
| Main consumption path | Find and answer pending questions; continue deliberation | Understand and revise implemented choices; apply rules through their operative consumers |

## Useful mechanisms in ADRs4AI

### Self-contained requests for judgment

The [ORRCF convention](https://github.com/ADRs4AI/orrcf/blob/5badd090e9ffe89fc37f152f5e0f0fa2dd97ce1d/README.md)
is Options, Recommendation, Rationale, Confidence, Falsifier. The author shows
the option space, attributes a recommendation, ties it to checkable evidence,
explains uncertainty and names what would change the recommendation. Questions
and option descriptions must be answerable when displayed separately from the
surrounding document.

Commonplace already requires alternatives and limits in final ADRs. The extra
value is at decision time: a consequential workshop question or escalation can
arrive ready to answer, rather than requiring the operator to reconstruct the
author's context. Numerical confidence action bands are not independently
calibrated by this inspection and are not a recommended import.

The ORRCF guide also warns that several endorsements can repeat one analysis.
It asks whether agreement adds independent evidence or derivation, and whether
the preferred option was challenged. A count of supporters is not verification.

### Questions encode whose turn it is

Their [ADR template](https://github.com/ADRs4AI/human-ai-collaboration-template-A/blob/081555af6ef5e35e0afc47a9bf809eac306f4519/docs/adr/templates/adr.md)
distinguishes `unanswered` (the human's turn), `unresolved` (the model's turn)
and `deferred` (nobody owes a move now), with separate closing states for
answered, withdrawn, superseded and moot. This is a candidate for active
workshop coordination, not a proposal to add a question lifecycle to every
Commonplace ADR.

### Records have a practical consumption interface

The inspected [VS Code MCP implementation](https://github.com/ADRs4AI/vscode-adrs4ai-no-adrs/blob/66eace3e0c7b6a172455fd591b268ce1b73d22b4/src/mcp/stdioServer.ts)
registers project overview, reference lookup, section retrieval, open-question
listing and write operations. Answer writes have replace semantics; new
recommendations stack. The broader source tree includes question parsing,
draft persistence, deep links and curated question sets called tours.

A tour selects and orders references to existing questions without becoming
another store for their answers. This is a useful candidate for assembling an
operator's decision workload without duplicating source records. Their
[tour readiness implementation](https://github.com/ADRs4AI/vscode-adrs4ai-no-adrs/blob/66eace3e0c7b6a172455fd591b268ce1b73d22b4/src/index/tourReadiness.ts)
distinguishes structural checks from warnings about thin content, absent
recommendations and status/answer inconsistencies. The practical lesson is to
inspect the exact material the operator will see: resolvable references alone
do not establish that a question is ready to answer.

This interface primarily surfaces pending deliberation. It does not by itself
solve the [ADR-routing workshop's](../adr-routing/README.md) problem of finding
settled decisions relevant to a proposed change.

## Costs and evidence limits

- A record retaining context, interpretations, recommendations and iterations
  can grow beyond what routine revision needs to load. Rich retention and a
  concise reading surface must be evaluated separately.
- Parseable Markdown is a real interface contract, not just prose. Their
  [authoring skill](https://github.com/ADRs4AI/plugins/blob/ba42da41a3dd076c3b48559dd6ed92bbfdac9d59/plugins/adr/skills/adr-authoring/SKILL.md)
  documents malformed headings, placeholders mistaken for answers, commentary
  absorbed into answer blocks and a "no open questions" heading that creates
  an open question. Tolerant parsing, diagnostics and explicit teaching carry
  maintenance costs. Borrowing the interaction principles does not require
  adopting that grammar.
- The public extension is a mirror without its deliberation record. Its
  [notice](https://github.com/ADRs4AI/vscode-adrs4ai-no-adrs/blob/66eace3e0c7b6a172455fd591b268ce1b73d22b4/DELIBERATIONS-NOTICE.md)
  reports that 46 ADRs and 39 seeds were withheld, along with other material.
  This limits independent inspection of the reasoning behind the tooling.
- The plugin's [small with/without evaluation summary](https://github.com/ADRs4AI/plugins/blob/ba42da41a3dd076c3b48559dd6ed92bbfdac9d59/proof/2026-10-19-adr-shape-ablation.txt)
  reports better ADR-format compliance with the plugin. That is evidence
  reported by the project about teaching the format, not an independent test
  of architectural decision quality. The summary points to a local untracked
  full report, so it is not a complete retained replication package.
- Making a deliberation accessible does not establish that its decision was
  implemented or affects later behavior. Commonplace's explicit consumer-path
  requirement remains useful in any revised model.

## Operator correction: compression should be a projection

The initial comparison recommended keeping our ADR format and improving the
deliberation that feeds it. The operator corrected the framing: Commonplace is
exploring the current theory set as a projection from a larger retained space
of claims; architecture should be explored in the same direction. A useful
compressed account need not be the primary or complete retained record.

The revised working direction is:

> Retain the design space and its criticism; project the currently adopted
> architecture from it.

That makes ADRs4AI's richer records more relevant than a final-format comparison
suggests. Rejected options, unresolved objections and superseded assumptions
can remain inputs to later design, rather than only historical residue. But
preserving a chronological conversation alone does not ensure that a later
reader can find which assumption supported a choice, which objection remains
open, or which changed constraint makes a rejected option viable again.

Three logical responsibilities help frame the exploration without fixing
three file types:

| Responsibility | What it retains or presents |
|---|---|
| Design reasoning | Candidate designs, explanatory claims, assumptions, constraints, evidence, objections and revision conditions |
| Adoption record | Which choice was authorized, for what scope, and its implementation, amendment or supersession |
| Current architecture view | A concise account of the adopted choice, grounds, limits and consumers |

Architecture includes both conjectures and commitments. "This layout will
reduce context cost" is a claim that evidence can undermine. "We adopt this
layout" is an authorized choice. "The implementation follows it" is a separate
factual claim. New criticism may weaken the rationale without revoking the
choice; adoption must not make the supporting conjecture appear established.
A current architecture view therefore needs both reasoning and adoption state,
not simply the claims with the strongest evidential standing.

The candidate safeguard is that the compressed view must not become an
independent source of architectural truth. A consequential statement should be
traceable to its grounds, and revision should not erase the earlier position.
How to achieve that, including editing and refresh rules, remains open.

## Consequence for this workshop

The operator requested independent architectural exploration parallel to
[conjecture-store](../conjecture-store/README.md), with eventual unification
preferred but not imposed during exploration. That workshop already sketches
a shared theory/design store; it is a comparison candidate, not a binding
architecture for this investigation. The [workshop framing](./README.md)
retains the commission and acceptance boundaries.

Small candidates worth testing are self-contained consequential questions,
explicit next responsibility, and checking an operator-facing batch in the
form the operator will actually read. The larger question is what retained
reasoning lets us revisit a choice when a deciding assumption changes, without
forcing routine work to load the whole record. Neither the external comparison
nor the operator's direction selects a database, schema, renderer or migration.
