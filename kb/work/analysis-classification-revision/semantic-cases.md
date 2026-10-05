# Semantic cases

## Evidence boundary

This record reviews the 13 synthetic acceptance cases in
[`test_classification_acceptance.py`](../../../tests/commonplace/lib/test_classification_acceptance.py)
against the [design decisions](./decisions.md) and [plan](./plan.md).
Facts below are authored fixture specifications, not inspected external-system
records. Expected findings and pass/block dispositions are case-by-case contract
judgments by the editing assistant. They specify what the independent semantic
verifier should decide; no independent verifier model was run for this record.
The authored verdict in the unsupported-positive test is also a fixture, not an
independently obtained review result.

The real tests exercise schema acceptance, record resolution, route fields,
projection, exports, public-text acceptance and job composition. They do not
classify source prose or prove its truth. Independent source-support review
remains necessary in an actual analysis. Neither these fixture judgments nor
packet-delivery checks establish model-run efficacy, general reliability or an
external system's properties. No workers or full analysis runs were launched.

“Pass” below means the bounded fixture account warrants acceptance by a semantic
verifier under the stated facts. “Block” means the specified distortion is a
support or reference defect, not that faithful uncertainty must be rejected.

## 01 — Automatic curator and unknown initial sheet

**Facts:** `MEM-RTE-curator-admit` has software admission without per-content
human approval. `MEM-OBJ-initial-sheet` has inaccessible caller identity and
approval policy.

**Expected finding/verifier:** Pass automatic curator agency plus partial
write-agency coverage. Keep initial admission unresolved with its missing
control facts and prevented complete coverage. Block manual initial agency or
complete enumeration without additional evidence.

**Prevents:** An unknown initial route erasing a supported automatic route, or
being omitted to manufacture completeness.

## 02 — Operator installation and automatic subsequent updates

**Facts:** `MEM-RTE-operator-install` has explicit human approval of installed
content even though software writes the bytes. `MEM-RTE-later-update` is
workflow-triggered by a human but admits updates without human approval.

**Expected finding/verifier:** Pass manual installation and automatic later
admission as separate units. The fixture explicitly covers these two mechanisms.
Block interpreting all updates as manual because a human started the workflow.

**Prevents:** Conflating admission control with authorship, physical I/O or the
initial workflow trigger.

## 03 — Automated API caller and unresolved generic caller

**Facts:** `MEM-RTE-api-install` is called by a scheduled software service with
no human decision. `MEM-OBJ-caller-install` only names a generic caller; its
identity and per-content control are not established.

**Expected finding/verifier:** Pass automatic API installation with partial
coverage and unresolved generic-caller control. Block manual agency inferred
from “caller.”

**Prevents:** An API noun becoming evidence of human control, or unresolved
caller identity becoming a negative about the established service route.

## 04 — Checkpoint reading versus replacement

**Facts:** `MEM-RTE-checkpoint-read` only selects/reads an existing checkpoint.
`MEM-RTE-checkpoint-replace` separately has human-approved replacement content.
`MEM-RTE-requested-read` fulfills an operator request for later delivery.

**Expected finding/verifier:** Pass inapplicable write agency on the read,
manual replacement and pull delivery. In this explicitly pull-only fixture,
read-back signal is inapplicable with the direction record as boundary warrant.
Block inventing a write from checkpoint selection, or applying that warrant to
an uninspected alternative.

**Prevents:** Reads being counted as manual writes and requested delivery being
classified as unsolicited supply merely because fulfillment is automatic.

## 05 — Known derivation and opaque provenance

**Facts:** `MEM-RTE-trace-derive` compresses stored conversational turns into a
retained summary. `MEM-OBJ-initial-origin` lacks producer links.
`MEM-OBJ-embedding-origin` has opaque provider production.

**Expected finding/verifier:** Pass trace-extracted lineage for the wired
summary derivation and partial coverage. Preserve both unresolved provenance
units. Block assigning authored/imported initial lineage or an embedding
production category without evidence.

**Prevents:** Known derivation being lost or incorrectly resolving unrelated
initial/embedding provenance.

## 06 — Mixed encodings and opaque provider state

**Facts:** `MEM-OBJ-text-payload` is model-interpreted prose;
`MEM-OBJ-cursor-fields` has fixed symbolic consumer rules. Their local parts
persist in `MEM-OBJ-checkpoint-file`. Only a display summary is readable for
`MEM-OBJ-opaque-payload`; `MEM-OBJ-provider-store` has inaccessible backing storage.

**Expected finding/verifier:** Pass natural-language and symbolic forms plus
files substrate, with partial coverage on both axes. Block inferring provider
encoding from its display or completing storage coverage from local files.

**Prevents:** Storage being mistaken for encoding, mixed parts being collapsed
into one form, or primary storage concealing included opaque state.

## 07 — One retained object, several consumers

**Facts:** The same session object supplies reference content through
`MEM-RTE-answer-consumer`, learning input through `MEM-RTE-update-consumer`, and
fixed-code scoring through `MEM-RTE-rank-consumer`.
`MEM-RTE-guidance-update` automatically produces durable guidance from session
traces for a later agent; `MEM-RTE-session-input` names the original turns.
No capacity comparison or downstream activation measurement was performed.

**Expected finding/verifier:** Pass knowledge, learning and ranking authority
at their distinct consumers, trace-learning yes and session-logs provenance.
Learning authority here describes the updater's input force; neither it nor
trace-learning establishes improved future-action capacity. Block inferring
that capacity, compliance or exercised self-improvement solely from these paths.

**Prevents:** A system union erasing consumer distinctions, delivery being
mistaken for compliance, and trace-fed retention being treated as benefit.

## 08 — Requested synthesis is not an implemented new claim

**Facts:** `MEM-RTE-compress-turns` selects/compresses existing claims without
establishing a new claim. `MEM-RTE-synthesis-request` has a synthesis request but
no available output meaning.

**Expected finding/verifier:** Pass consolidate with partial coverage; synthesis
remains unresolved. Block synthesize assigned from the route name or prompt.
The separate adversarial `MEM-RTE-named-synthesis` test deliberately asserts
synthesize on request-only facts. Its legal schema and resolved ID pass
structural checks; its authored expected verifier verdict blocks the unsupported
value and requests removal or supporting evidence.

**Prevents:** A prompt instruction substituting for evidence of a semantic
transformation, and schema validity substituting for source-support review.

## 09 — Request, selection, delivery and unresolved alternatives

**Facts:** `MEM-RTE-request-return` delivers in fulfillment of a request.
`MEM-RTE-unsolicited-supply` supplies independently through a hook.
`MEM-RTE-hook-selector` actually matches active task IDs against retained parts.
`MEM-RTE-alternate-delivery` and `MEM-RTE-alternate-selector` have inaccessible
trigger relationships and selector inputs.

**Expected finding/verifier:** Pass pull and push direction, identifier selection
on the hook, and partial coverage on both axes. Block treating automatic request
fulfillment as push, inferring targeted selection merely from a filename ID, or
making the alternative selector inapplicable because a pull route is known.

**Prevents:** Collapsing the chain into one direction and using one inspected
branch to dispose of an included opaque branch.

## 10 — Qualifying trace update, local absence and opaque inputs

**Facts:** `MEM-RTE-summary-update` automatically retains trace-derived guidance
for a later invocation. `MEM-ABS-static-branch` has a bounded search of static/
at the fixture revision finding no qualifying update. `MEM-RTE-alternate-update`
has unknown durability/consumption. `MEM-RTE-mixed-input` consumes conversational
turns and tool results; `MEM-OBJ-opaque-input` has unknown original provenance.
The event adapter only wraps inputs.

**Expected finding/verifier:** Pass trace-learning yes in the derived union,
retain the local no and unresolved alternative in units, and pass session-logs
plus tool-traces with partial source coverage. Block a whole-system no,
complete yes coverage, improved-capacity attribution or provenance inferred
from the adapter label.

**Prevents:** Aggregation erasing local absence, uncertainty erasing existence,
and transport labels fabricating original input categories.

## 11 — Absence, uninspected, inconclusive and defects

**Facts:** `MEM-ABS-curation-search` searches all named fixture maintenance entry
points at the fixture revision and finds no transformations.
`MEM-OBJ-unread-store` was available but not inspected.
`MEM-OBJ-unclear-origin` was inspected but has no producer links.

**Expected finding/verifier:** Pass bounded absent curation, uninspected storage
and not-determinable lineage as distinct conclusions. Block treating either
uncertain unit as evidenced absence. The adversarial `MEM-RTE-trace-negative`
has no absence search: its no is actually rejected by the bounded-absence
structural contract. Changing it to a legal positive permits structural
acceptance, not semantic support. Off-vocabulary values, findings on explicitly
unresolved units and `MEM-RTE-missing-update` references are actually rejected.
The request-only unsupported-positive variant is covered in case 08.

**Prevents:** Uncertainty being encoded as absence and legal vocabulary or
resolved references being treated as sufficient evidence.

## 12 — Public contribution and independent property limits

**Facts:** The member fixture's `MEM-OBJ-store` retains session-derived guidance
for later model use; initial admission control is inaccessible. The synthesis
has no capacity comparison, two-way causal self-representation evidence,
internal-role ownership evidence, or inspected evidence-responsive
organizational change with exercised downstream dependence.

**Expected finding/verifier:** Pass the bounded retained-guidance contribution
with separate limits for learning, reflection, autonomy, self-improvement and
complete write-agency coverage. Block a bundled negative or any unsupported
positive property. Self-improvement needs a declared boundary, horizon and
independently specifiable objective, then evidence-shaped update, organizational
change, live consumer/channel/force and subsequent causal dependence. Capacity
improvement is not its membership test. A dormant standing pathway permits only
a marked dispositional claim; directed self-change does not establish success.
An undeclared `MEM-OBJ-undeclared` synthesis reference is actually rejected.

**Prevents:** Supported contribution being withheld due to independent unknowns,
learning's benefit test being substituted for self-improvement's causal test,
and storage/loading being mistaken for exercised organizational change.

## 13 — Projection preserves existence, coverage and evidence strength

**Facts:** `MEM-RTE-wired-admit` supports automatic admission from inspected
software. `MEM-RTE-claimed-admit` claims the same value only in documentation.
`MEM-RTE-opaque-admit` has inaccessible control. `MEM-ABS-absent-curation` has a
bounded search. Other axes, including lineage, remain uninspected.

**Expected finding/verifier:** Pass automatic existence with wired support,
partial agency coverage, separately claimed evidence, absent curation and
uninspected lineage. CSV and statistics retain version, units and these
assessment distinctions. The explicit resolution variant adds software-control
facts for the opaque route instead of deleting it; even then, claimed-only
support on the independent route prevents strong complete-value statistics.
Block upgrading that route's evidence from another witness or equating
incomplete values with an empty/absent set.

**Prevents:** Strong existence evidence laundering weak alternatives and
projection/export silently discarding coverage or negative-evidence distinctions.

## F4 delivery and verification

The shared record contract now supplies the operative self-improvement test
under its theory account. It governs an attribution, not every route; it adds
no universal evaluator, reflection requirement, success requirement or broad
new assessment obligation.

The acceptance tests build real runtime, memory (first and correction),
epistemic, reconciliation, record-verifier, profile, profile-verifier, synthesis
and synthesis-verifier jobs. Each asserts that the shared contract is a declared
input and an explicit read-first/batch path in the rendered invocation, then
checks the operative test in that loaded file. Definition links or workshop
links alone cannot satisfy these delivery assertions.

Verification results for this bounded edit (implementation checks, not
independent model-review outcomes):

- `uv run pytest tests/commonplace/lib/test_classification_acceptance.py -q`:
  35 passed, including all ten new compose-path delivery variants.
- `uv run pytest`: 1107 passed, 64 deselected by the configured selection;
  deselected tests were not run.
- `uv run ruff check .`: passed.
- `commonplace-validate kb/agentic-system-analyses/instructions/agentic-analysis-records.md`:
  passed, zero failures or warnings.
- `commonplace-validate kb/work/analysis-classification-revision/semantic-cases.md`:
  passed as implicit text, zero failures or warnings; text validation does not
  establish the semantic judgments above.
- `git diff --check`: passed.

The edit is confined to the shared contract, the synthetic acceptance test file
and this new record. Existing unrelated modifications remain untouched. No
commit, publication or efficacy claim is part of this completion.
