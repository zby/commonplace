---
type: types/note.md
description: "Shared record contract for agentic analyses: identity, annotations, amendments, evidence statuses, record fields and conditional theory assessments"
---

# Agentic analysis records

This contract defines records used across the runtime, memory and
epistemic members. Their authors, reconciliation and verification receive
it as a declared dependency. Member types add their own fields and section
placement; the [source contract](./agentic-analysis-sources.md) supplies
evidence layers, anchors and quotations.

## Identity and grammar

The record kinds are components (`CMP-*`), operative objects (`OBJ-*`),
routes (`RTE-*`), claims (`CLM-*`), evidenced absences (`ABS-*`) and
behavioral-authority paths (`BAP-*`). `SRC-*` sources belong only to the
Source register. The analyst that establishes a record declares it in its
member, with its permanent prefix: runtime has `RT-` (`RT-OBJ-1`), memory has
`MEM-` (`MEM-OBJ-1`), epistemic has `EPI-` (`EPI-OBJ-1`).
The prefix identifies the declaring analyst, not the member discussing the
record. Keep a supplied ID unchanged in references, annotations and amendments.

Within `## Shared records`, kind headings group declarations:
`### Components`, `### Operative objects`, `### Routes`, `### Claims`,
`### Evidenced absences`, `### Behavioral-authority paths`. A declaration
is one level-four heading, `#### RT-OBJ-1 — Short label`. Prose, lists and
tables do not declare records. Member types specify which empty kind
headings remain. IDs are unique across the set and resolve within it.
References use full IDs, separated by commas or words; suffixes and ranges
are not inferred. Explicit `through` and dash ranges are refused even when
both endpoints resolve, including adjacent endpoints; list every full ID
instead. Ordinary `to` prose may relate two records but does not enumerate
intervening IDs. Source quotations and fenced excerpts are excluded from
identifier checks.

An annotation, `#### On RT-OBJ-1 — Short label`, supplies another analyst's
fields on a record declared elsewhere. It does not repeat generic identity
or redefine the referent, and never annotates a record the member declares.
Its location and permitted fields come from the annotating member's type.

Only the reconciliation member amends records. An `Amendment:`
paragraph gives the full ID, superseded value, replacement, evidence anchor
and affected findings. An anchored conflict retains both values. A
supersession uses `Amendment: MEM-RTE-3 is superseded by RT-RTE-7`, with
identity evidence; both IDs stay declared. A split supersedes the combined
record only by parts already declared in analyst members, for example
`Amendment: RT-OBJ-3 is superseded by EPI-OBJ-1 and EPI-OBJ-2`, with identity
evidence and affected findings. Reconciliation never allocates IDs. Supersede
a combined record only when its findings are wrong once the parts are
separated; a valid container can remain alongside its parts. No ID changes referent, and
no step renames IDs or rewrites another analyst's member. Provisional
labels are local tags. Allocate IDs monotonically within a prefix and
never reuse dropped numbers; gaps are harmless.

When other members are supplied, a new declaration records its closest
supplied full IDs and distinct identity, possible-duplicate evidence, or
no counterpart after comparison. An existing referent receives an
annotation rather than another declaration; a different prefix or label
does not establish a distinct referent. Material parts with different
checks or consumers are declared and assessed separately. A declaration
whose referent is a material part of exactly one supplied record writes
`Part of: RT-OBJ-1` on its own unindented line within that declaration,
using its parent's full record ID. The field carries exactly one ID,
without backticks or other text, and cannot name the declaring record itself.
Local and set checks enforce its syntax; existing set resolution checks its
target. Explain a parent of a different record kind beside the relation.
Semantic verification checks containment; matching kinds alone does not prove it.
A candidate that can replace a record's referent is not thereby a part of it.

The part owns its fields and status; the container keeps its identity.
Containment alone requires neither possible-duplicate evidence nor
supersession. A record spanning several supplied records without being part
of exactly one keeps the distinct-identity comparison, naming each overlap.

When a required part is undeclared, reconciliation returns it to the memory
analyst if that analyst should declare it and returning is permitted.
Otherwise retain an `Unresolved conflict:` naming the combined ID, missing
part, evidence and prevented conclusion. Name the undeclared part in prose,
without inventing an unresolved ID. This adds no runtime or epistemic rewrite
and no new return round.

## Status fields

Conclusion status is exactly one of `absent`, `inapplicable`, `uninspected`,
`claimed`, `afforded`, `wired`, `observed`, or `causally supported`.
Different layers have separate labelled fields, such as `implementation
conclusion status: wired` and `operation conclusion status: observed`;
`wired; observed` is not one value. Guarantee strength is a separate field:
`invariant`, `protocol`, `policy`, `best effort`, `deployment guarantee`,
or `no claimed guarantee`. Epistemic architectural status and observed
candidate state retain their own vocabularies.

Every route declaration has at least one conclusion-status field on its
own line. For example:

```markdown
- implementation conclusion status: wired
- operation conclusion status: uninspected
```

Write one controlled value only; keep its evidence and
explanation outside the value. A field cannot come from another record,
annotation or source excerpt. Member acceptance checks presence, duplicate
layer labels and controlled values; semantic verification judges the choice.

## Record fields

| Kind | Required content |
|---|---|
| Component / operative object | Source-native identity, representational form, storage substrate and evidence |
| Route | Endpoints, progression, owner, context/state/action effects, applicable status fields and evidence |
| Claim | Claimed operation and its source |
| Evidenced absence | `absent` status, searched roots or files, query and revision, evidence, and conclusion supported or prevented |
| Behavioral-authority path | Consumer, channel, force and horizon |

[Representational form](../../notes/definitions/representational-form.md)
classifies encoding and consumption, independently of storage. Natural-language
content receives consequences through model or human interpretation. Symbolic
content has localized units and fixed consumer rules determining its permitted
behavior. Distributed-parametric content spreads numerical state across weights
or dense representations. Split mixed objects by operative part or consumption
path when their evidence, invalidation or rollback differs. Prompt names model
input supply, not a fourth form.

Each distributed-parametric component used by inspected routes separately
states whether parameters change during operation, whether its exact
version is pinned, and whether a mutable endpoint can resolve to another
model. Provider internals remain uninspected when inaccessible. Fixed
weights do not establish absence of learning through other retained
material.

Each route records immediate return, later read-back, delegated visibility,
selection predicate, invalidation or expiry, activation or effect and
evidence limits. An inapplicable or uninspected field gives a reason.
Read-back is material accumulated or changed through use that reaches a
later consumer invocation; static shipped material and ordinary current-run
state are excluded. A summary that compacts or replaces current-run state
is retained memory when a later invocation receives it, within or across
runs. Activation requires evidence that delivered material changed behavior.

### Route field syntax

Within each route declaration, write each of these exact labels once as an
unindented bullet, with a non-empty answer on the same line:

```markdown
- Immediate return: ...
- Later read-back: ...
- Delegated visibility: ...
- Selection predicate: ...
- Invalidation or expiry: ...
- Activation or effect: ...
- Evidence limits: ...
```

Replace every `...` with the finding. When a field is inapplicable or
uninspected, use exactly `inapplicable — reason` or `uninspected — reason`,
replacing `reason` with the explanation. Supporting prose, tables and
quotations may follow. Another record or an annotation cannot supply these
fields for the declaration.

Local member validation and set validation reject missing, empty or duplicate
fields and uncertainty values without reasons. They check presence and form;
semantic verification judges the answers and their evidence. The separate
status-field check above enforces conclusion-status form. Component fixity
and conditional route fields retain their requirements without new presence
checks.

## Conditional route fields

These requirements apply to the named route classes. Inapplicability is
not evidence of an absent epistemic phase.

| Applies to | Required content |
|---|---|
| Diagnosis, candidate comparison, admission or successor selection | Who proposes, decides and can veto; separate computational and human contributions; any answer oracle (expected answer or reference outcome, provider, use); operating mode and improvement triggers |
| Routes admitting product, knowledge/instruction, capability or production-machinery changes | Trigger, proposed change, admission, rejection ability, rollback/recovery; guidance that shaped the proposal, what it says and what persists |
| Routes involving formulated theories | The theory account and separately evidenced properties below |

Model judgment alone establishes no answer oracle. Operating modes distinguish
open requests, bounded experiments/curricula and multiple modes; oracle use
belongs to its mode. Routine logs, counters and unchanged checkpoints need
no separate revision account unless they change later decisions or recovery.
Writes governed by one admission mechanism may be grouped.

## Theory account

A theory route states the guidance it applies, derives from, criticizes,
revises/replaces, and retains or reconstructs. It names what persists:
formulated theories, criticisms, input/outcome records, parameters or other
source-native material. A rule set can express a theory without historical
rationale; classification depends on its content and exposed assumptions,
scope conditions and parts, not its storage label. Missing rationale does
not establish absent formulated criticism. Retained rationale names its
later reader, if any.

Each [theory-builder](../../notes/definitions/theory-builder.md) condition has
its own conclusion status and evidence under the label
`theory-builder conditions 1–4`:

| Condition | Evidence required and limits |
|---|---|
| 1. Localized content | A theory stated in natural or formal language; its minimum is one whole unit carrying what the theory says. Whole replacement meets this minimum. |
| 2. Consumption | Decisions depend on what the theory says. Storage, citation and delivery alone do not establish it. |
| 3. Content-directed criticism | Stated criticism names the challenged claim, result and placement of blame (theory, test, data or auxiliary assumption), and resulting revision or changed reliance. Derivation under an unchanged theory and scores selecting variants do not establish it. A prose contradiction is an interpretation unless codified. A surviving theory can change reliance or test selection without changing text; rejection and replacement count as revision. |
| 4. Iteration | Criticism's result is kept and shapes a next round, including within one run. Reconstruction from retained criticisms counts; unused critic reports or retained input/outcome records alone do not. A builder ends when another system freezes its product for deployment. |

No condition is inferred from another. The report distinguishes absent
formulation or criticism from inaccessible model processing; opacity alone
establishes neither presence nor absence. Additional properties are assessed
separately:

| Property | Required finding |
|---|---|
| [Addressability](../../notes/definitions/addressable-theory.md) | Degree to which assumptions, scope conditions and parts are individually inspectable and revisable, and the assessment boundary; finer grades exceed condition 1's minimum |
| Persistence | What persists, later consumer and attained horizon: reasoning episode, rounds of one run, runs on one task, or problems/sessions |
| Learning | Under `learning`: improved capacity for future action, assessment boundary, improvement evidence and attribution evidence. Membership, revision, persistence or connected steps alone do not establish it; capacity need not have been exercised. Later capacity traces persistence to that time; later/recurrent use also traces the retained result and consumer. The memory axis `trace_learning` has its own write-route meaning. |
| [Reflection](../../notes/definitions/reflective-system.md) | Selected aspects within the boundary, their self-representation and both causal directions: aspect changes can update the representation; representation-mediated operations can affect later behavior. Subject matter alone is insufficient; direct machinery modification is unnecessary. |
| Reflective theory builder | Its method texts meet conditions 1–4 and are criticized against records of its own operation |
| Autonomous theory builder | Role-by-role evidence that computation performs every internal operation; users supplying problems and judging products are outside the boundary. Autonomy does not establish reliability. |

Learning, reflection and autonomy remain independent claims. Revision
selection prefers
[explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
among revisions that fit the evidence; it does not trade fit away for reach.
Explanatory-reach means that a criticizable account of why a pattern works
continues to apply beyond its originating case because the mechanism persists.
Vary a load-bearing premise and ask what change the explanation predicts;
transfer or local success alone does not establish that account.
