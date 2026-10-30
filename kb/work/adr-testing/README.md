# Testing ADR usefulness during system changes

## Commission

Opened on 2026-10-30 at the operator's request. Make preliminary measurements
and tests of whether Commonplace's architecture decision records (ADRs) help
agents recover and apply consequential design decisions during changes. Include
a bounded retrospective search for ADRs consulted too late. Missing consultation
when it was needed is more important, but harder to establish from traces.

The system includes Python and LLM instructions: both instruct machines. Include
schemas, contracts and their execution paths when relevant. Do not treat ADRs
as a complete compressed specification of the system. Design extends into the
operational artifacts and their interactions; needing to read them is not an
ADR failure.

The operator's working hypothesis is that LLM search, reading and link-following
can recover task-relevant decisions much as they recover relevant code. A feature
may span several areas. Its applicable commitments might fit in one context,
with supporting material reached through links. This is a hypothesis to test,
not a requirement to force each feature into one subsystem or to preload every
ADR. More archiving and more explicit relationships are competing or complementary
responses only if observed failures warrant them.

## Authority and boundaries

This workshop authorizes measurement, read-only trace investigation, and small
investigative tests using existing artifacts. Write observations and experimental
materials here, plus this workshop's active-list entry. Do not change ADRs,
operational instructions, schemas, code, archive policy or routing machinery as
part of this commission. Do not run unbounded agent experiments or treat an
investigative task as authority to implement its proposed change. Later tests
that need mutations or additional access must return for authorization.

Prefer instructions and observed cases before committing to finer structure or
code. Repeated behavior is not sufficient evidence of correctness: check whether
the recovered guidance preserves consequential limits and surviving commitments.

## Evaluation boundary

Test useful preservation, discovery and interpretation, not a percentage of the
whole design. Separate these possible failures:

- Capture: a consequential reason was never retained.
- Discovery: the reason existed but the investigation did not find it.
- Interpretation: the record was found but its meaning or scope was misread.
- Maintenance: a record no longer describes the relevant state.
- Legitimate expansion: the task needed code, instructions or another artifact;
  this alone is not a failure.

ADRs describe implemented choices; they are not independently binding merely
because they exist. Consultation may be unnecessary when operative contracts
already supply the relevant requirement. A deliberate, authorized revision is
not a violation of the old choice.

For timing evidence, distinguish an ADR read after an edit from a warranted claim
that it was read too late. The latter needs an applicable prior decision and an
observable consequence, correction or intervention that makes earlier consultation
material. New ADR drafting is not prior-decision consultation. Check the decision
and artifact versions applicable at the time; unresolved version checks lower
confidence. A later edit alone does not establish a causal effect of reading.

A trace with no observed read does not prove no knowledge: instructions, earlier
sessions, compacted context, delegated work, excerpts and other contracts may
supply it. Likewise, ADR path mentions and search hits are not evidence of full
reading. Report partial/truncated reads and missing history explicitly.

## Initial work and next decision

- [Size baseline](./size-baseline.md): document and section sizes, not a resolved
  inventory of current commitments.
- [Trace pilot](./trace-pilot.md): bounded local screening, case evidence and
  limitations. This is a convenience sample, not a consultation failure rate.

After these probes, choose the next test from the observed gaps. A useful
prospective probe is a read-only investigation of a real proposed change, with
an independently checked account of consequential decisions. Include both a
code change and an LLM-instruction change before generalizing across them.
Measure guidance size, material read, missed commitments and additional
link-following; distinguish selected-text size from peak context occupancy and
include tool outputs when claiming the latter. Do not define the expected answer
only from whichever ADRs the tested agent happened to find.

Return to the operator before building a benchmark suite or adopting a remedy.
A justified result that existing navigation suffices is as acceptable as a
specific improvement proposal. Missing evidence should narrow the conclusion,
not trigger an assumption that a graph or index is required.

## Relationship to existing work

[ADR routing](../adr-routing/README.md) already asks when consultation is useful
and how a change run finds relevant decisions. Its 2026-08 baseline is historical;
this workshop provides a new operator-commissioned measurement/test track, not
a replacement routing design. Send any justified routing proposal there rather
than maintaining a competing mechanism.

[Decision lifecycle and evidence](../decision-lifecycle-evidence/README.md)
investigates retention and architectural views. This workshop measures whether
existing records serve change tasks; it does not choose that workshop's storage
or projection model.

The current [ADR contract](../../reference/types/adr.md) and
[design-rationale account](../../reference/design-rationale-management.md)
provide the starting representation, not an assertion that every current ADR
meets every newer requirement.

## Evidence bookkeeping and closure

Each probe records date, repository revision/dirty-state caveat, accessible
inputs, sampling rule, counts, evidence locators, observations, interpretation
and limits. Retain minimum necessary excerpts so an essential finding survives
loss of local sessions; local paths remain supplementary and are not published
as raw dumps. Do not retain credentials or unrelated private content.

Close when the preliminary evidence and test results support a bounded conclusion
about existing ADR use and a next decision: no change, a specific further test,
or a separately authorized improvement. Extract useful durable findings to the
appropriate library collection, coordinate routing/lifecycle implications with
the workshops above, then remove this temporary directory and its active entry.
