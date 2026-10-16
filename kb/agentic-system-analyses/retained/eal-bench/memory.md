---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "EAL-Bench memory report: bounded authorization profiles, event-derived state, saved replay and action-outcome write-back."
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
source-identity: "https://github.com/tommasocerruti/eal-bench"
reviewed-boundary: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
---

# EAL-Bench memory report

## Boundary and evidence

This account covers the retained authorization state and context mechanisms of the whole shipped evaluation workflow fixed by [boundary](boundary.md). Included surfaces are LangMem profiles, frozen executor evidence, attempts/state metadata, saved replay and checkpoint continuation, candidate selection, source-authority filtering, event reduction and closed-loop write-back. Public memory evaluation and controlled variants are included as distinct consumers/producers, not assumed to use LangMem admission. External model weights and LangMem internals remain opaque. Generic tool-loop messages are current invocation state, not durable memory by themselves.

SRC-1 is the sole evidence source. Direct source inspection added the paths below at the frozen commit. All new findings are implementation evidence unless labelled otherwise. Supplied runtime findings remain provisional; citations to their records reuse their supporting passages rather than implying independent exhaustive inspection. No target execution, provider call, historical trial analysis or causal experiment was performed. Missing primary archives prevent reconstruction of the reported primary runs, as the boundary explains.

| Entry point or operation | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| Single-profile creation, update, validation, freezing | `experiments/authorization_memory/langmem_writer.py` | Direct bounded reads of candidate processing, validation, artifact/profile conversion, instructions and freezing; [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact), [MEM-OBJ-memory-attempt](#mem-obj-memory-attempt); admission/context dispatch also supplied by [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission). |
| Persistence and immutable executor plan | `experiments/authorization_memory/persistence.py`, `experiments/authorization_memory/study_engine.py`, `experiments/authorization_memory/resume.py` | Direct persistence helpers; engine/resume supplied by [RT-OBJ-executor-plan](runtime.md#rt-obj-executor-plan), [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume). No independent filesystem or interruption experiment. |
| Main CLI, extension dispatch and writer variants | `experiments/run.py`, `experiments/extension_cli.py`, `experiments/writer_variants_run.py` | Runtime main dispatch plus direct complete extension dispatch and saved-replay function inspection; [MEM-RTE-saved-replay](#mem-rte-saved-replay). Writer variants' full formation methods remain uninspected; distinct prefix-based proposal configuration is located, not a demonstrated mechanism-equivalence claim. |
| Executor evidence, tools, alternate library/Inspect consumers | `experiments/authorization_memory/pipeline.py`, `src/eal_bench/eval/scoring.py`, `src/eal_bench/eval/inspect_adapter.py`, `src/eal_bench/llm/client.py` | Supplied [RT-RTE-executor-score](runtime.md#rt-rte-executor-score), [RT-RTE-alternate-consumers](runtime.md#rt-rte-alternate-consumers), [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence). No newly established autonomous retrieval tool or hidden provider context policy. |
| Best-of-k review/oracle selection | `domains/procurement/studies/writer_ttc.py` | Supplied [RT-RTE-candidate-selection](runtime.md#rt-rte-candidate-selection). Full history and whole candidates reach reviewer; no edit/merge authority. Every domain's other review/repair builder was not inspected. |
| Source-authority removal and paired delivery | `experiments/mitigations/source_authority/gate.py`, `experiments/mitigations/source_authority/study.py` | Core predicate supplied by [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate); direct plan inspection establishes original/gated executor jobs, strengthening its documented replay account. |
| Event extraction, current state and external log | `experiments/mitigations/event_sourcing/core.py`, `experiments/mitigations/event_sourcing/runtime.py` | Direct message/validation, checkpoint restoration/save and finalization reads; [MEM-OBJ-event-log](#mem-obj-event-log), [MEM-OBJ-reduced-state](#mem-obj-reduced-state), [MEM-RTE-event-recovery](#mem-rte-event-recovery). Full writer retry scheduling and executor recovery remain uninspected, not absent. |
| Outcome-derived writer updates | `experiments/closed_loop.py` | Direct write-back renderer; progression supplied by [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback). Actual effect on later decisions unobserved. |
| Public memory assessment, annotations and altered controls | `src/eal_bench/eval/preservation.py`, `src/eal_bench/eval/propagation.py`, `src/eal_bench/eval/__main__.py` | Direct annotation resolver and variant definitions/loosening helpers, complete CLI; [MEM-OBJ-annotation](#mem-obj-annotation). Remaining trial builders, end-to-end evaluation, annotation production and export loaders are not exhaustively traced; external caller persistence/human control unresolved. |
| Pressure/challenge reuse, hybrid writing and domain-specific maintenance | `experiments/authorization_memory/`, `domains/`, `analysis/` | Included but unresolved beyond runtime's stated coverage. Specific selection/transform details for every pressure, challenge, repair and maintenance path were not inspected. Prevents universal claims about all admission, context budgets or equivalence of all study paths. |
| Primary archives, diagnosis artifacts and published result summaries | `results/`, `analysis/paper_results.py` | Boundary's archive limit retained. Individual available diagnosis traces and full analysis consumers uninspected; neither observed learning nor a repository-wide absence of trace use follows. |

## Core ideas

1. **The retained profile is a replacement for source history, not a pointer into it.** The writer produces compact state; freezing explicitly sets `source_history=None`. The executor's memory path receives serialized payload, not the writer's reasoning, attempt errors or full history. The same payload can be symbolic to a schema validator and natural-language evidence to a model. See [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact) and [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence).
2. **Admission is structural and route-specific.** Baseline admission checks shape, visible citations and enabled capacity, not source entailment. Source-authority gating adds a different every-citation rule; event reduction adds atomic lifecycle operations. The alternate routes are counterexamples to assigning one universal admission policy to the system. See [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission), [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate), [RT-RTE-event-admission](runtime.md#rt-rte-event-admission).
3. **Storage, audit and later model context are different surfaces.** Attempt arguments, provenance, current state and cumulative events can all persist while only compact payload reaches a model. External event logs are meaningful to recovery without being a model-visible archive. See [MEM-OBJ-memory-attempt](#mem-obj-memory-attempt), [MEM-OBJ-event-log](#mem-obj-event-log), [MEM-RTE-event-recovery](#mem-rte-event-recovery).
4. **Feedback has an explicit adapter.** Closed-loop code turns scored executor decisions into new source-like text, submits it with the existing profile and uses accepted state for later requests. Raw trial retention alone is not that mechanism. It supplies a trace-fed revision channel but not evidence of improved capacity. See [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-artifact
Label: MemoryArtifact authorization payload

The source-native MemoryArtifact holds a compact free-text string or typed domain authorization object, plus a separate metadata envelope. Storage substrate: Python object during formation and serialized run-directory JSONL when persisted. Free text is natural-language material. Typed payload is symbolic for domain parsing, fidelity evaluation and event operations, but the executor consumes its serialized JSON through model interpretation. It is not distributed-parametric storage. The hosted model components are already declared in [RT-CMP-writer-model](runtime.md#rt-cmp-writer-model) and [RT-CMP-executor-model](runtime.md#rt-cmp-executor-model).

Lineage includes parent memory, chain, block, writer identity/seed, attempt, presentation and implementation hashes. These fields identify production and access; they do not themselves establish correct authorization or encode the reasons for a remembered claim. Accepted payload seeds subsequent profile updates and is copied into FrozenEvidence. The frozen object omits source history. No rationale-completeness guarantee is established for payload contents; source IDs are provenance handles, not copied source text. Distinct from [RT-OBJ-executor-plan](runtime.md#rt-obj-executor-plan): this is selected content, not the plan selecting it. Related admission and consumption are [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission) and [RT-BAP-profile-update](runtime.md#rt-bap-profile-update), not duplicate objects.

SRC-1 implementation: `experiments/authorization_memory/langmem_writer.py`, `experiments/authorization_memory/persistence.py`.

> parent_id = chain.current.memory_id if chain.current is not None else None
> --- `experiments/authorization_memory/langmem_writer.py`

> memory_id=artifact.memory_id,
> payload=artifact.payload,
> source_history=None,
> content_hash=artifact.content_hash,
> --- `experiments/authorization_memory/langmem_writer.py`

#### MEM-OBJ-memory-attempt
Label: MemoryAttempt and update-state audit records

Candidate raw arguments/payload, status/detail, changed flag, accepted/retained IDs and repair lineage are symbolic audit records with potentially natural-language error text. Substrate: Python records then run-directory serialization. Attempts retain rejected proposals separately from accepted memory; MemoryState identifies which artifact remains current after each logical update. Neither a failed candidate nor its diagnostics becomes executor evidence merely by being retained. Repair feedback may be supplied to the writer; downstream executors receive selected payload instead. The object's own audit lineage is not a guarantee that rationale survives in that payload.

This is a distinct output of [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission), not a second admission route or the frozen executor plan. SRC-1 implementation: `experiments/authorization_memory/langmem_writer.py`.

> status = "invalid_payload"
> detail = str(exc)
> --- `experiments/authorization_memory/langmem_writer.py`

> if status not in {"accepted", "no_change"} and chain.current is not None:
>     status = "retained_after_failed_update"
> --- `experiments/authorization_memory/langmem_writer.py`

#### MEM-OBJ-event-log
Label: External cumulative event log

The reducer retains ExtractedEvent entries with operation, target, source IDs and record/changes. Symbolic event semantics support deterministic replay; source-text interpretation occurred upstream in model extraction. Storage: reducer list in memory, checkpoint trajectory events and event-log rows on disk. This is derived authorization material, not a raw provider transcript. Finalization attaches chain, update, block and source-attempt lineage. Cumulative events can contain lifecycle history no longer present in compact current state. The checkpoint restoration consumer replays them; the event writer's message constructor receives previous current state and current block instead. Thus storage authority and model-context authority differ.

Distinct material product of [RT-RTE-event-admission](runtime.md#rt-rte-event-admission); no supplied object counterpart. It is not a duplicate of the executor checkpoint plan. SRC-1 implementation: `experiments/mitigations/event_sourcing/runtime.py`, `experiments/mitigations/event_sourcing/core.py`.

> "events": [event.to_dict() for event in trajectory.reducer.event_log],
> --- `experiments/mitigations/event_sourcing/runtime.py`

> checkpoint["event_log"].append(row)
> --- `experiments/mitigations/event_sourcing/runtime.py`

#### MEM-OBJ-reduced-state
Label: Reduced authorization state

The event reducer's visible typed state is a symbolic authorization snapshot used to make a MemoryArtifact. It has different size and consumers from the cumulative log: reduced-state capacity is checked; the log's tokens are accounted separately. Storage: reducer-derived mapping, reduced-state rows, checkpoint records and memory rows. Lineage: accepted lifecycle events, parent memory and source attempt, including state retention on failed updates as labelled in event-delta rows. Later event-writer calls receive previous compact state; executor use is described by [RT-RTE-event-admission](runtime.md#rt-rte-event-admission). Current JSON is model-interpreted when supplied to a model, not an authorization veto.

This is an event-derived instance family of [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact), declared separately because event/log recovery and atomic validation differ from LangMem profile replacement. Closest supplied route is [RT-RTE-event-admission](runtime.md#rt-rte-event-admission), not a duplicate referent. SRC-1 implementation: `experiments/mitigations/event_sourcing/core.py`, `experiments/mitigations/event_sourcing/runtime.py`.

> reduced = candidate.visible_state()
> tokens = count_reference_tokens(canonical_json(reduced))
> --- `experiments/mitigations/event_sourcing/core.py`

> "PREVIOUS CURRENT AUTHORIZATION STATE\n"
> + canonical_json(previous_state)
> + "\n\nCURRENT CONVERSATION BLOCK\n"
> + block_text
> --- `experiments/mitigations/event_sourcing/core.py`

#### MEM-OBJ-annotation
Label: Free-text memory Annotation

Public Annotation carries an extracted typed state, source-content hash and acceptance status. It is a symbolic assessment artifact distinct from the underlying natural-language memory. The caller supplies annotation objects to the resolver; persistent storage and whether a human or model authored/approved them are unresolved by this inspected public path. Admission accepts only accepted, matching-hash, parseable and mutually agreeing extracted states. The consumer is memory assessment, not an executor or profile writer. Disagreement/hash mismatch makes assessment unscorable rather than replacing the original memory. Author identity cannot be inferred from the word annotation.

No counterpart is declared in supplied runtime; closest is the broader public evaluation surface of [RT-RTE-alternate-consumers](runtime.md#rt-rte-alternate-consumers), which concerns response scoring rather than annotation agreement. SRC-1 implementation: `src/eal_bench/eval/preservation.py`.

> if len({canonical_json(state) for state in states}) != 1:
>     return None, "conflicting_accepted_annotations"
> return states[0], None
> --- `src/eal_bench/eval/preservation.py`

### Routes

#### MEM-RTE-saved-replay
Label: Saved writer-variant replay

Endpoints: completed source run to selected FrozenEvidence and executor jobs under new targets. Owner: writer-variants CLI replay function. This is a distinct source-reuse route adjacent to [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume): it starts a new run using completed memories, not continuation of missing calls. It overlaps the broad later-read capability of [RT-RTE-study-execution](runtime.md#rt-rte-study-execution), but is not a duplicate.

- Immediate return: New persisted replay run and completion status; dry-run returns without executor calls.
- Later read-back: Saved evidence payload reaches new executor invocations without regenerating memory; optional memories, attempts, states and formation files are copied for provenance.
- Delegated visibility: Executor receives jobs built from selected frozen evidence, not every copied audit file.
- Selection predicate: Completed writer/writer-variant study, matching domain/presentation, optional case filter; ordinary writer source is restricted to evidence IDs marked generated_final by source trials.
- Invalidation or expiry: Wrong status/study/domain, no matching memory or differing presentation rejects; integrity verification is invoked with an explicit allow-unverified option. Full verifier internals uninspected; no TTL established.
- Activation or effect: Wires saved selected memory into new scored executor calls. Changed behavior and successful replay remain unobserved.
- Evidence limits: Direct replay implementation inspected; source archive availability and live provider operation not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operator selects source and targets; code filters/rejects inputs, not a human approving individual payloads. There is no new writer proposal or semantic correction in this bounded replay mode. Answer oracle remains domain executor scoring, as in [RT-RTE-executor-score](runtime.md#rt-rte-executor-score). SRC-1 implementation: `experiments/writer_variants_run.py`.

> evidence = [e for e in evidence if e.evidence_id in final_ids]
> --- `experiments/writer_variants_run.py`

> jobs += jobs_for_evidence(base, cases[frozen.case_id], frozen, route=STUDY_ID, metadata={"writer_target_id": frozen.writer.target_id if frozen.writer else None})
> --- `experiments/writer_variants_run.py`

#### MEM-RTE-event-recovery
Label: Event trajectory checkpoint recovery

Endpoints: saved trajectory records/events to reconstructed reducer and trajectory list. Owner: event-sourcing runtime restoration code. This differs from [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume), whose referent is shared-engine executor continuation; it augments the event protocol beside [RT-RTE-event-admission](runtime.md#rt-rte-event-admission).

- Immediate return: Reconstructed trajectories or ValueError on inconsistent checkpoint state.
- Later read-back: Stored events are replayed into a new reducer to verify saved records before returning the restored trajectory; subsequent live scheduling was not fully inspected.
- Delegated visibility: Symbolic recovery code sees cumulative events and records; this is not delivery of the event archive to a model.
- Selection predicate: Configured cases crossed with writer targets, trajectory key and saved per-trajectory entry; absent entries initialize empty trajectory state.
- Invalidation or expiry: Non-prefix completed-block sequence, mismatch of replayed/saved records or duplicate event IDs rejects restoration; no time expiry in this function.
- Activation or effect: Restores retained symbolic lifecycle state and checks replay consistency, not semantic accuracy of original extracted events.
- Evidence limits: Restoration/save functions inspected, not an executed interruption trial or exhaustive event-runner recovery audit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This mechanism admits restored computational state, not a new model/human content proposal. Code can reject inconsistent saved state; human mutation policy and external filesystem integrity are not established. Its reference is replayed event semantics, not a gold authorization oracle. SRC-1 implementation: `experiments/mitigations/event_sourcing/runtime.py`.

> replayed = PublicEventReducer(domain)
> replayed.apply_batch(trajectory.reducer.event_log)
> if canonical_json(replayed.records) != canonical_json(trajectory.reducer.records):
> --- `experiments/mitigations/event_sourcing/runtime.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission)

Write agency is model proposal followed by benchmark software admission; launching a study is not human approval of each proposed grant. Direct inspection confirms free-text citation checking differs from typed parsing. The budget is reference-token count of serialized candidate, enforced only when enabled; instructions still state the profile capacity. `_process_invocation` separates accepted, unchanged, writer-error and invalid-payload outcomes. Existing accepted state survives failed updates. Artifacts and attempts retain IDs and diagnostics separately; a later profile invocation receives selected current contents, not the entire audit stream. Source trust stops at visibility, not entailment. SRC-1 implementation: `experiments/authorization_memory/langmem_writer.py`; passages in [MEM-OBJ-memory-attempt](#mem-obj-memory-attempt) and supplied record.

#### On [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence)

Frozen memory carries payload by value and explicitly omits source history; evidence ID is not a model-followable reference. Delivery to executor gives interpreted evidential authority, not a symbolic authorization grant. Plain JSON encoding does not make model reasoning a fixed symbolic rule. SRC-1 implementation: `experiments/authorization_memory/langmem_writer.py`; passage in [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact). This narrows claims of preserved reasons: neither source text nor rejected-candidate criticisms is automatically carried through freezing.

#### On [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate)

Direct study-plan inspection adds implemented replay wiring to the supplied record's documented replay account. A deterministic transform creates a child MemoryArtifact and matching evidence; the plan keeps both original and gated objects and builds jobs for each probe and variant. This is selective withdrawal from one derived memory, not destructive deletion of original audit material. Diagnostics and authority metadata are retained as separate rows, not inserted into the gated payload. No per-record human decision is established; domain metadata and code decide admission. SRC-1 implementation: `experiments/mitigations/source_authority/study.py`.

> for variant, item in (("ORIGINAL", original), ("GATED", gated)):
> --- `experiments/mitigations/source_authority/study.py`

> memories[original.memory_id] = original_memory
> memories[gated_memory.memory_id] = gated_memory
> --- `experiments/mitigations/source_authority/study.py`

#### On [RT-RTE-event-admission](runtime.md#rt-rte-event-admission)

Direct core inspection confirms atomic candidate reduction and compact-state/new-block context. Finalization separately appends accepted event rows, delta status and reduced-state snapshots; cumulative storage token counts do not imply model-visible log context. These are derived lifecycle records, not unprocessed trace retention. Model proposals receive structural checks; reduced-state capacity does not guarantee correct authority interpretation. Full retry scheduling and call-log reuse remain uninspected. SRC-1 implementation: `experiments/mitigations/event_sourcing/core.py`, `experiments/mitigations/event_sourcing/runtime.py`; passages in [MEM-OBJ-event-log](#mem-obj-event-log), [MEM-OBJ-reduced-state](#mem-obj-reduced-state).

#### On [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback)

Direct renderer inspection confirms mixed trace origin: current request, chosen action/payload and benchmark decision label are computationally rendered into a synthetic conversation turn or ACTION_OUTCOME text. Neutral control contains no request/action/outcome; the original-writer path uses rendered conversation even in the action arm. The current memory seeds model-mediated revision; accepted payload, not raw trial storage alone, shapes later input. Optional cumulative logs are a distinct less-compact context path. The synthetic actor label does not establish organizational authorization. SRC-1 implementation: `experiments/closed_loop.py`; progression and rejection/retention are supplied by the cited runtime record.

> # The neutral control carries no request, action, or outcome in either writer mode.
> --- `experiments/closed_loop.py`

> log.append(f"[{when}] {line}")
> --- `experiments/closed_loop.py`

## Write side

Baseline acquisition uses domain-rendered history and existing current profile. Domain policy supplies state, inference and source instructions; LangMem proposes replacement content, while the wrapper validates and constructs immutable lineage-bearing artifacts. Rejection can trigger bounded structural repair rather than gold semantic correction. Typed serialization normalizes parsed state; free text remains a string. Source visibility is a narrower property than source authority. Subsequent failed updates retain prior accepted contents; no-change results are distinguished from invalid output. See [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission), [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact), [MEM-OBJ-memory-attempt](#mem-obj-memory-attempt).

Alternative curation is not one mechanism. The Procurement reviewer/oracle selects a whole candidate without merge/edit authority ([RT-RTE-candidate-selection](runtime.md#rt-rte-candidate-selection)). The cited-source gate removes failed records while preserving original and transformed arms ([RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate)). Event extraction turns text into issue/patch/revoke/replace operations, atomically reduces accepted deltas and retains separate log/current-state products ([RT-RTE-event-admission](runtime.md#rt-rte-event-admission)). Lifecycle revocation is not deletion of history; a retained event can remove or change a current authorization without erasing its log. Checkpoint replay consistency checks are not a new semantic authority test ([MEM-RTE-event-recovery](#mem-rte-event-recovery)).

Public propagation introduces a separate source of memory content. SRC-1 `src/eal_bench/eval/propagation.py` distinguishes writer-produced from deliberately altered variants; inspected loosening helpers mutate fields with requested values and check parsing/formation. These are controlled sensitivity artifacts rather than proof of endogenous writer error. Public annotation agreement gates whether free text can be assessed, not whether a memory may reach an executor ([MEM-OBJ-annotation](#mem-obj-annotation)). Full producer and persistence routes for annotations and every public variant were not inspected, so initialization authorship/human approval remains local uncertainty.

> Only a memory a writer produced can evidence endogenous laundering.
> --- `src/eal_bench/eval/propagation.py`

Closed-loop revision is the qualifying trace-fed channel established here: scored trial/request → rendered block/outcome → seeded model update → admitted compact payload → later request. Its retained result can shape later context even without changing weights. No observed improvement follows. Neither lineage fields nor retained outcome labels establish that the writer formulated and retained a criticism explaining why an authorization claim failed. The later executor normally sees the product, not reasons or the full trial trace ([RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback), [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence)).

Physical I/O is ordinary JSON/JSONL writing by benchmark helpers. It supplies no independent content-approval authority. Static shipped policy/corpus maintenance is an input surface, not read-back by itself; its complete maintenance loop remains uninspected. No general expiry, garbage-collection or withdrawal service is inferred from the inspected writer/gate/checkpoint functions.

## Read-back

**Profile continuation:** code selects the current chain profile for each update, and the manager receives it with selected update messages. Budget constrains serialized profile rather than full source-history size. Failure preserves the last accepted state. The wrapper is the context selector; the foreground model does not retrieve arbitrary memories on demand. See [RT-BAP-profile-update](runtime.md#rt-bap-profile-update), [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission).

**Executor consumption:** job preparation selects full history, memory or empty evidence; explicit messages can override ordinary construction. Memory payload is serialized into a fresh invocation, not followed through an ID. The supplied account establishes separate writer/executor/reviewer frames: only selected return artifacts escape, while full conversations are not automatically inherited. This resembles scoped work frames, but no reference-counted heap or model-dereferenceable external pointer is established. Saving an artifact does not keep it model-visible. See [RT-RTE-executor-score](runtime.md#rt-rte-executor-score), [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence).

**Saved and resumed consumers:** [MEM-RTE-saved-replay](#mem-rte-saved-replay) selects final generated evidence and creates new jobs; [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume) reconstructs missing jobs from the frozen bundle; [MEM-RTE-event-recovery](#mem-rte-event-recovery) consumes historical events to verify and restore reducer state. These are request-driven host selections, not unsolicited context injection. Source-authority study construction automatically pushes paired original/gated payloads to its selected jobs. Event-writer calls receive compact prior state and current block, not the cumulative archive. Budgets and consumers differ; the event archive can grow outside the compact-state budget.

**Assessment consumers:** public annotation resolver consumes retained extraction/hash/status when caller-supplied; actual persistent external read-back is not established. The public CLI lists resources or exports built tracks rather than supplying an autonomous retrieval runtime (SRC-1 `src/eal_bench/eval/__main__.py`). Inspect/public scorers and generic handler loops remain separate effect boundaries ([RT-RTE-alternate-consumers](runtime.md#rt-rte-alternate-consumers)). Pressure/challenge routes are included but their exact targeting and transformation are unresolved here; no claim of a uniform two-message context or universal budget is made.

## Integration issues

- **Supported strengthening:** [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate) limits replay orchestration to documentation in its own inspection. Direct SRC-1 `experiments/mitigations/source_authority/study.py` now establishes paired jobs and retained original/gated payloads. The annotation supplies implementation support, not observed mitigation benefit; runtime can update this limit without changing route identity.
- **Object overlap:** [MEM-OBJ-reduced-state](#mem-obj-reduced-state) is an event-derived family of [MEM-OBJ-memory-artifact](#mem-obj-memory-artifact). Their distinction is log/recovery/admission, not a second physical memory system. No new record intentionally duplicates a supplied runtime referent; new routes explain their distinction beside the closest supplied routes.
- **Event recovery extent:** [MEM-RTE-event-recovery](#mem-rte-event-recovery) strengthens knowledge of retained events' actual software consumer but does not establish all retry and executor continuation behavior of [RT-RTE-event-admission](runtime.md#rt-rte-event-admission). Full scheduling remains available but uninspected; prevents exactly-once or semantic-integrity claims.
- **Incomplete alternative-path inspection:** pressure/challenge, hybrid writing, all domain-specific repair/maintenance builders and annotation production were not fully traced. Relevant roots are in the coverage table. This prevents system-wide admission/budget equivalence and universal human-control classification, not the positive profile, event, gate and feedback findings.
- **Results boundary:** no historical primary archive or examined diagnosis trace closes delivery → changed behavior → improved capacity for these routes. Their implementation findings remain valid; operation/benefit remains uninspected rather than absent.

## Limitations and checks

The source HEAD recheck returned `51648690bc52d7a9c7ac080a2c67a784fe9d56cb`; working-tree status was clean. The supplied method inputs, member types, collection rules and record contract were read completely, including bounded runtime/contract ranges. Source searches that named nonexistent guessed files returned errors; no absence claim uses those misses. Later successful inventory located the event runtime and public preservation/propagation paths. No target code was executed or modified.

The report deliberately preserves unresolved included surfaces instead of extrapolating from LangMem to all routes. External hosted models and dependency internals, exact weight identity, live transport reliability and actual memory-induced behavioral effects remain outside established evidence. Typed shape, hashes and citation visibility are not semantic warrant. Retained feedback is not by itself learning, formulated criticism or exercised self-improvement.

Validation: deterministic output validation passed; this checks form and quotation occurrence, not analytical correctness or job acceptance.
