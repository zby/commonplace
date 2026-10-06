---
type: types/note.md
description: "Shared record contract for agentic analyses: identity, annotations, supersessions, evidence statuses, record fields and conditional theory assessments"
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
member, with its permanent prefix: runtime has `RT-` (`RT-OBJ-store`), memory has
`MEM-` (`MEM-OBJ-store`), epistemic has `EPI-` (`EPI-OBJ-store`).
The prefix identifies the declaring analyst, not the member discussing the
record. Keep a supplied ID unchanged in references, annotations and supersessions.

Names: one to three lowercase hyphenated words, each starting with a letter;
digits may follow. Components/objects use available source-native names.
Drop extensions; split case changes and separators; lowercase and join.
Attach digit-only fragments to the preceding word (`GPT-4` → `gpt4`). If
longer, keep three distinguishing words. Routes, claims, absences and
behavioral-authority paths use two or three words from the label. Qualify
generic names or split parts by source path or role, never a number.
Without a source-native name, role, input or label may suggest a handle.
Names are handles, not conclusions (`validated-knowledge`).

Within `## Shared records`, kind headings group declarations:
`### Components`, `### Operative objects`, `### Routes`, `### Claims`,
`### Evidenced absences`, `### Behavioral-authority paths`. A declaration
is one level-four heading, `#### RT-OBJ-store — Short label`. Prose, lists and
tables do not declare records. Member types specify which empty kind
headings remain. IDs are unique across the set and resolve within it.
Use full IDs; aliases are not inferred. Named `through`, dash and
`to` grouping prose is permitted; code resolves written IDs without expanding
intervals. Structured citation lists and single-ID fields remain explicit.
Numbered `SRC-*` ranges are refused; list each source ID. Source quotations
and fenced excerpts are excluded from identifier checks.

An annotation, `#### On RT-OBJ-store — Short label`, supplies another analyst's
fields on a record declared elsewhere. It does not repeat generic identity
or redefine the referent, and never annotates a record the member declares.
Its location and permitted fields come from the annotating member's type.

A record's value changes only in the report that declares it: the declaring
analyst corrects it in a correction round. The reconciliation member states
identity between declared records and never replaces a value. A conflict it
cannot settle retains both findings. A
supersession uses `Amendment: MEM-RTE-selection-route is superseded by RT-RTE-policy-check`, with
identity evidence; both IDs stay declared. A split supersedes the combined
record only by parts already declared in analyst members, for example
`Amendment: RT-OBJ-output is superseded by EPI-OBJ-store and EPI-OBJ-input`, with identity
evidence and affected findings. Reconciliation never allocates IDs. Supersede
a combined record only when its findings are wrong once the parts are
separated; a valid container can remain alongside its parts. No ID changes referent, and
no step renames IDs or rewrites another analyst's member. Provisional
labels are local tags. Keep IDs fixed through label or finding changes. A
corrected report keeps every ID its predecessor declared, because other
reports cite them; a record whose finding no longer holds keeps its
declaration and states the corrected finding.

A corrected report comes with the analyst's answers: a list with exactly one
entry per blocker addressed to that report, in the verification's order, each
starting `- corrected: ` or `- declined: `, and no other line starting
`- `. A report identical to its predecessor is accepted only when every
entry is `declined`.

When other members are supplied, a new declaration records its closest
supplied full IDs and distinct identity, possible-duplicate evidence, or
no counterpart after comparison. An existing referent receives an
annotation rather than another declaration; a different prefix or label
does not establish a distinct referent. Material parts with different
checks or consumers are declared and assessed separately. A declaration
whose referent is a material part of exactly one supplied record writes
`Part of: RT-OBJ-store` on its own unindented line within that declaration,
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

When a required part is undeclared, reconciliation retains an
`Unresolved conflict:` naming the combined ID, missing part, evidence and
prevented conclusion. The record verifier addresses it to the analyst who
should declare the part. Name the undeclared part in prose,
without inventing an unresolved ID.

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

## Source-native coverage and uncertainty

Memory and epistemic accounts retain an inventory of included material parts
and mechanisms, including opaque alternatives. Record supported facts beside
their actual part, route, transformation, input or consumer and evidence layer.
A positive witness establishes existence, not complete enumeration. Name each
unresolved included part, the missing fact, inspection/access limit and
conclusion prevented. Available but uninspected evidence is not evidenced
absence; inspected but inconclusive evidence is not an unsupported positive.
Use the existing status vocabularies; do not invent a record conclusion status
for profile coverage. Bounded absence requires a searched boundary and warrant.
Inapplicability requires the relevant boundary and reason.

Source analysts describe these dimensions without assigning controlled profile
values. Preserve enough source-native detail for later classification:

| Dimension | Unit and distinctions to retain |
|---|---|
| Storage | Each operative object/part, including opaque provider state; distinguish encoding from substrate. |
| Form | Each operative part and consumption path; separate mixed text, symbolic and numerical material. |
| Lineage | Each object/part and derivation path; keep unresolved initial or embedding provenance local. |
| Authority | Each retained part, actual consumer and effect; delivery is not compliance, and update and downstream consumers differ. |
| Admission control | Each write/admission mechanism: human decision supplying, editing, approving or replacing that content versus software/model admission; authorship and physical I/O are separate. Starting a workflow is not per-content approval; generic caller identity leaves human control unresolved. Reads alone do not establish writes. |
| Curation | Each implemented transformation with its evidence layer; requested behavior and route names do not establish changed meaning or a new claim. |
| Read-back direction | Request, selection and delivery operations in a chain; requested delivery and independent unsolicited supply differ. |
| Selection | Actual selector input and selected retained part; an identifier on a requested file is not evidence of targeted selection. |
| Trace-fed update | Each automatic trace-fed write, its durable behavior-shaping result and later consumer; retaining raw logs alone is insufficient. |
| Trace origin | Original input to each qualifying write, including mixed or opaque provenance; adapter labels do not establish origin. |

Several effects or transformations can coexist without resolving an opaque
alternative. Group only units sharing the same scope, control and coverage.
A trace-fed artifact update may give retained experience learning authority
at the update consumer while its output gives a later agent knowledge; neither
establishes improved capacity. Preserve these actual paths rather than a
system-wide implication or score.

Faithfully scoped uncertainty is an acceptable result, not a blocker by itself.
Unsupported findings, concealed included parts, unjustified complete coverage,
unsupported negatives and malformed references remain defects. The declaring
analyst may narrow or correct an assertion, and reconciliation may retain a
named conflict; no step erases
supported positives to make another part's uncertainty disappear. A missing
fact becomes a problem only when no faithful bounded account is possible or
required inputs or frozen scope prevent completing the task. Keep learning,
reflection, autonomy and self-improvement, and each theory-builder condition,
as independent route/property conclusions. A supported contribution coexists
with independently unestablished properties; never bundle them into a negative.

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

### Self-improvement attribution

When attributing or qualifying [self-improvement](../../notes/definitions/self-improving-system.md),
assess the named pathway independently of learning, reflection and autonomy.
Self-improvement is operative, evidence-responsive change to the bounded system's
own [behavior-determining organization](../../notes/definitions/behavior-determining-organization.md),
not merely improvement of an external work product. An output can enter that
organization when retained and consumed in later operation; its output label
alone decides neither inclusion nor exclusion.

Declare the boundary, assessment horizon and improvement objective. The objective
must be specifiable independently of the change it licenses. For an exercised
pathway, establish all four causal links within that boundary and horizon:

1. Evidence bearing on the objective causally shapes determination of the update.
2. The result changes the system's own organization, rather than remaining
   evidence, a proposal or an external product.
3. The changed organization enters a live behavioral-authority path: consumer,
   channel and force capable of reaching later behavior.
4. Subsequent operation exercises that path and causally depends on the change.

Storage, retrieval, acceptance, installation and loading alone do not close these
links. Name an unestablished link and the attribution it prevents. A standing but
dormant pathway supports only a marked dispositional claim, not exercised
self-improvement over the horizon. Membership establishes improvement-directed
self-change, not successful improvement; success needs separate outcome evidence.
Neither reflection, autonomy nor a separate evaluator or rejection gate is a
membership condition. This test governs self-improvement claims; it adds no
universal assessment obligation for other routes.

Learning, reflection, autonomy and self-improvement remain independent claims. Revision
selection prefers
[explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
among revisions that fit the evidence; it does not trade fit away for reach.
Explanatory-reach means that a criticizable account of why a pattern works
continues to apply beyond its originating case because the mechanism persists.
Vary a load-bearing premise and ask what change the explanation predicts;
transfer or local success alone does not establish that account.
