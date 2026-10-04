# Phase 2 ADR check and change packet

2026-10-04, before changing the run. The operator commissioned continuation of
phase 2 and approved amending ADR 093's carrier clauses in the conversation:
"Amend ADR 093’s carrier clauses (recommended)". Definitions, per-value evidence
and counting rules remain unchanged. The initial worktree was clean at 9bc0b9c7e.

## ADR 083

| Clause | Profile design disposition |
|---|---|
| One exact result and minimal completion state | The exact result is the manifest-pinned set under ADR 095; profile becomes its sixth member, not a second result or state model. |
| Frozen source identity and completed output hashes | Source pin remains unchanged; manifest pins the profile with its supporting members. |
| A failed run is not resumed; a new ID repeats work | Preserved. One bounded profile correction is within an open run, like the existing synthesis correction; it does not resume a failed run. |
| Validate before replacing; failed candidate leaves incumbent unchanged | Preserved. Both profile checks complete before publication; no archive or public write happens during profiling. |
| Git supplies tracked history; workflow does not stage or commit | Preserved. This commissioned method implementation is committed by the operator's direction, not by the analysis workflow. |
| Rejected intermediate state machinery | No additional public completion-state fields or persisted receipt protocol. Existing workflow-owned job state handles the two jobs. |

ADR 083's original single-file layout is already amended by ADR 095; collection
paths are amended by ADR 099 and ADR 102. Its current-path annotation still names
the old state root and needs a faithful path correction, not a policy change.
No new conflict with ADR 083's remaining rules was found.

## ADR 093

| Clause | Profile design disposition |
|---|---|
| Per-value basis, canonical records and rationale | Exact existing shape and vocabularies preserved. |
| Axis coverage independent of evidence strength | known/partial and other assessments keep their existing meanings. |
| Strongest witness establishes existence; weaker routes retain limits | Preserved; profiling may only cite accepted records. |
| Positive membership versus complete-profile counts | Same matrix columns and counting rules; only member input changes. |
| Omitted or weak values are not observed negatives | Preserved. Missing recorded facts weaken coverage rather than license source-only values. |
| Scope is an evidence boundary, not a way to drop alternatives | Preserved. Scope agreement is checked against all relevant members and amendments. |
| Memory specialists author, and memory report type owns the profile | Carrier conflict reported before adoption. Operator approved amendment to the new profile author/type, keeping every analytical rule above. |
| Structural checks cannot establish warrant | Separate independent verify-profile remains mandatory. |
| Historical retained bytes immutable; admission needs new analysis | Preserved. Replay uses disposable stripped copies; no historical member or pin is edited. |

## Consumer inventory and enforcement

[Scoped searches](./evidence/phase2-consumer-inventory.json) cover the executable
readers, method/types/schemas, current comparison instructions, scripts, tests,
site member rules and reference carriers. Original retained trees are read-only
witnesses, outside this change's consumer population.

| Consumer | Planned disposition |
|---|---|
| Memory type/schema and job | Remove profile mapping, rationale and locally annotated-profile-reference rule; retain source-native descriptive fields. |
| Reconcile and record verification | Remove axis checks and profile-only return reasons; retain record reconciliation and independent verification. |
| Workflow constructors, ordering and acceptance | Profile then verify-profile after record closure; one correction; copy accepted profile unchanged before synthesis. |
| Set manifest/type and loaders | Sixth required member for complete sets; preserve blocked/out-of-scope singleton behavior and exact member hashes. |
| Profile validator and shared comparison reader | Shape/vocabularies unchanged; references resolve against canonical set declarations, not local profile declarations. |
| Source quotation and public completion checks | Continue checking all actual set members; profile declares no records or new evidence. |
| Matrix, landscape and taxonomy procedures | Read memory-profile.md with no fallback to the old memory location. |
| Site | Publish the sixth retained member; retain state/archive exclusions and historical evidence rules. |
| Publication method guard and projections | Pin new type/schema/jobs; keep canonical skill projections and no old-run resumption. |
| ADR/reference and tests | Amend ADR 093 carrier, write a second implemented ADR, test job order, bounded correction, profile-only checks and reference/hash failures. |

The replay gates any runtime changes. No compatibility reader, migration or
repinning is planned; the new current population is empty. Every changed byte
belongs to current method or test fixtures, not retained historical evidence.
