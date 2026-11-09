---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Profile verification of the memory profile of the instruction-only recall skill (recall/) of Parcha-ai/parcha-skills at c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) profile verification

## Verification

**What was checked.** I checked the scope, all ten axes, every unit and every
finding of the handed memory profile. The checks used the profile type, the
record contract and the accepted runtime, memory, epistemic and workflow
records. I resolved superseded IDs through the reconciliation's four
amendments. For each unit I checked four things:

- whether its scope is the axis's natural unit;
- whether the cited records support the value and its basis;
- whether the unit assessment matches its coverage;
- whether the axis assessment matches the inventory.

I judged the profile afresh. The previous verification's two blockers and the
profile author's answers were treated as arguments, not as established
repairs. I read no source file, and the profile records no source reads.

**Previous blockers.**

- *Engine-ingest update consumer.* The previous blocker is corrected.
  `behavioral_authority` now has a unit for host transcripts consumed by engine
  ingest. The unit carries `learning` at basis `claimed` and cites
  [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance),
  [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts) and
  [RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction). It is kept
  apart from the index output's downstream `ranking` and `routing` unit, and it
  matches the engine-ingest unit under `trace_learning`. `claimed` is the right
  basis: the ingest record splits trigger (`wired`) from ingest (`claimed`).
  The rationale answers the memory annotation's "retrievable evidence, not
  behavior-shaping instructions" with the type's rule that retained
  trace-derived context qualifies. That answer is consistent with the
  trace-learning finding.
- *`recall_forget` decay basis.* The previous blocker is corrected. `decay` is
  now `claimed`, and the unit is `partial`. The unit names the missing service
  deletion semantics, which would separate `decay` from `invalidate`.
  [EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget) supports that
  account: the service deletes, the removal is "as declared", and the deletion
  semantics are absent. A partial unit that keeps a classified finding and names
  its unresolved alternative matches the type.

**Previous limit.** The profile now includes host retention deletion
(`automatic` and `decay`, both `claimed`). Generated-skill removal is
`not-determinable` under both write agency and curation. The previous limit
therefore no longer applies. The scope string does not name these two
withdrawal mechanisms in its parenthetical list. The memory member's scope
includes host retention deletion as withdrawal, and generated skills are an
included object, so the surfaces still agree. I dismissed that wording point.
Leaving generated-skill removal `not-determinable` is cautious but faithful.
The records say only that removal is "manual". They do not record a human
decision on particular content, and they do not record a route.

**Supersessions.** The YAML cites only surviving IDs:
[EPI-OBJ-search-results](epistemic.md#epi-obj-search-results) and
[EPI-RTE-why-assessment](epistemic.md#epi-rte-why-assessment). The rationale
lists all four amendments and correctly says which two carry classifications.
No value depends on a superseded finding.

**Axis dispositions.**

- `storage_substrate` (known): supported. Each retained object in scope has one
  substrate unit. `files` for transcripts and generated skills is `wired`. The
  index (`sqlite`), Brain content (`service-object`) and cursors (`files`) are
  `claimed`, and their records cite the absent engine and service as the
  reason. Synced content has a classified substrate but an unresolved form.
  That is consistent, because substrate and encoding are separate.
- `representational_form` (partial): supported. Transcripts are split by
  consumption path: the model reads text, and the engine parses symbolic JSON.
  Index structures and model-read snippets are split the same way. Possible
  dense ranking state and the form of synced Brain content stay
  `not-determinable`. That matches
  [RT-CMP-recall-engine](runtime.md#rt-cmp-recall-engine) and
  [MEM-OBJ-brain-synced-content](memory.md#mem-obj-brain-synced-content).
- `lineage` (known): supported at the stated bases. Transcripts are
  `imported` because the target acquires them from the host. I considered
  whether sync should be `imported`, as a raw copy, rather than
  `trace-extracted`. The declared sync is from local Recall session history, so
  `trace-extracted` at `claimed` follows the record. The unit also keeps
  `imported` for the external connectors. I dismissed the question.
- `behavioral_authority` (known): supported. The consumers and effects are:
  - `knowledge` for retrieved windows and Brain records;
  - `instruction` for repeat prompts and for generated skills, the latter at
    `afforded` through the host loader;
  - `learning` at both update consumers that read retained material (engine
    ingest and skill-ify);
  - `ranking` and `routing` for index content;
  - `routing` for cursors.

  I considered three objections:
  - *Mixed bases in the `knowledge` and `routing` units.* Index-backed windows
    and `WHY` lines exist only through the claimed engine, yet these units
    carry `wired`. The type attaches a basis to the part or mechanism that
    supports the authority, and here that mechanism is the model's instructed
    consumption. The procedure wires it
    ([EPI-RTE-why-assessment](epistemic.md#epi-rte-why-assessment),
    [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)). Production remains
    `claimed` under `ranking` and `trace_learning`. I dismissed this objection.
  - *No `learning` unit for capture's update consumer.* `trace_learning` counts
    capture as a qualifying write. The capture records, however, establish
    only that the model selects decisions or findings
    ([RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)). They do not
    establish that capture reads retained, read-back material rather than the
    current session's working context. Behavioral authority classifies
    retained parts, so this omission is not shown to be a gap. I dismissed it.
  - *Continue playbook classified only as `knowledge`.*
    [RT-BAP-retrieved-sessions](runtime.md#rt-bap-retrieved-sessions) says
    retrieved state can drive new actions after confirmation. The records,
    however, place the effect in a resume summary that informs the user's
    decision ([EPI-OBJ-resume-summary](epistemic.md#epi-obj-resume-summary)).
    They record no standing directions taken from the tail. I dismissed this
    objection.

  The grouping of `related` output is a limit (see Limits).
- `write_agency` (partial): supported. Capture and direct skill-ify are
  `automatic`, because the user starts the workflow but approves no text. That
  follows the type's rule that starting a workflow is not per-content
  admission. `recall_forget` is `manual`:
  [EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget) records a
  user request and exact-receipt selection. Host writing, ingest, host
  retention deletion and cursor writing are `automatic` at `claimed`. Three
  included mechanisms remain unresolved: the external creator, Brain sync and
  import, and generated-skill removal. Those unresolved units make the axis
  `partial`.
- `curation_operations` (partial): supported. `consolidate` for capture and
  recipe separation follows the type's extraction example. The memory
  annotation's "meaning-changing generalization ... as requested" does not
  establish `synthesize`. The record contract says requested behavior does not
  establish a new claim. [EPI-RTE-recipe-separation](epistemic.md#epi-rte-recipe-separation)
  also classifies the recipe as non-truth-apt. Both `decay` units are
  `claimed`. Engine and service curation are correctly `not-determinable`, and
  indexing and redaction establish no controlled operation.
- `read_back_direction` (partial): supported. Pull is classified for the
  session-material routes under the bounded absence
  [MEM-ABS-push-hook](memory.md#mem-abs-push-hook). Generated-skill direction
  stays `not-determinable`, as
  [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load) and
  the reconciliation require.
- `read_back_signal` (not-determinable): supported. The session-material unit
  is `inapplicable` on a bounded pull-only warrant. The unresolved
  generated-skill unit prevents an `inapplicable` axis. With no controlled
  findings, `not-determinable` is the type's value.
- `trace_learning` (partial): supported. Engine ingest (`claimed`), capture
  (`claimed`) and skill-ify (`afforded`) each record an automatic trace-fed
  write whose retained output reaches later invocations. Brain sync stays
  `not-determinable` because its admission control is unknown. The system
  `"yes"` with partial coverage follows the type's example, and no `"no"` is
  emitted.
- `trace_source` (partial): supported. Index values follow the declared ingest
  content. The capture unit is `partial`, with tool-trace origin unresolved.
  Skill-ify `tool-traces` rests on the commands and steps that
  [EPI-RTE-recipe-separation](epistemic.md#epi-rte-recipe-separation) records
  as taken from the window.

**Consistency between axes.** Write agency, trace learning and behavioral
authority now treat engine ingest, capture and skill-ify consistently.
Read-back direction and read-back signal share the same unresolved
generated-skill unit. The decay-versus-invalidate question is stated in both
the curation unit and the rationale.

## Blockers

none

## Limits

- The `behavioral_authority` unit "Host transcripts and index-backed windows
  read by the current model in find/verify, continue, cold scan and related"
  groups the `related` output under `knowledge`. Its recorded effect is
  different. [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions)
  returns sessions that share a project, branch or touched files, as candidates
  for reading. The epistemic ledger row on that route gives its force as
  ranking and its operational authority as proposing candidates. That makes
  the effect closer to selecting which session to open. The system value set
  is unchanged, because `ranking` and `routing` are already supported for index
  content. The `knowledge` finding stays supported for windows the model reads.
  Readers should not take this unit as a per-route classification of `related`
  output, or compare query-free retrieval authority across systems from it.
