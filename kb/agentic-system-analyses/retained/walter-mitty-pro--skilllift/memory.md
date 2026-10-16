---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SkillLift memory: replayed task portfolios, receipt-guided later rounds, category checkpoints and domain fusion, with diagnostic traces separated from admitted instructions."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
source-identity: https://github.com/walter-mitty-pro/SkillLift
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
---

# SkillLift memory report

## Boundary and evidence

The memory scope follows the task-portfolio, SkillsBench category and tau2 domain routes in [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution), [RT-RTE-category-training](runtime.md#rt-rte-category-training) and [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion). It includes retained skills, scoring instructions, proposal history, trial recovery state, alternative full-snapshot checkpoints, fusion and later test consumption. Static prompts are working-context machinery, not experience memory. Provider state, benchmark tasks/graders and enclosing host memory remain outside the inspectable main-repository loop, as specified by [boundary](boundary.md#boundary-and-evidence). Their exclusion prevents claims about actual skill activation, host compaction and benchmark validity.

All new source findings below use SRC-1 implementation at the frozen commit. Prompt rules are separately identified as requested behavior. Direct reads extend the supplied runtime: portfolio store, planning prompts, mode coordinator, rubricator and evidence serializer, ExperimentStore, category round/fusion/test code, tau2 behavior extraction/fusion/loader, domain checkpoints and imported markdown-update helpers. Supplied runtime findings remain provisional and are cited rather than presented as independently read adapter internals. No target execution or observed run evidence was supplied.

### Coverage inventory

| Entry point or memory operation | SRC-1 paths and inspection basis | Covering records or limit |
|---|---|---|
| Task CLI, task-specific runners, injected planner/generator/verifier and adapter calls | `skilllift_eval/cli.py` dispatch search; supplied runtime reads of `skilllift_eval/runners/skilllift_wildclaw.py` and `skilllift_eval/runners/skilllift_skillsbench_tasks.py` | [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution); constructor injection is an alternative route, not proof of custom consumer behavior. |
| Seed/config admission, candidate replay, final freezing | Direct: `skilllift/skilllift/portfolio/store.py`; supplied patch gate in `skilllift/skilllift/portfolio/ref.py` | [MEM-OBJ-candidate-record](#mem-obj-candidate-record), [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref), [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay). |
| Search history, rejected directions and receipt state read on later rounds/re-entry | Direct: `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/portfolio/prompts.py` | [MEM-OBJ-search-state](#mem-obj-search-state), [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution). |
| Mode A context selection and edit/repair calls | Direct selected generator and selector methods: `skilllift_eval/runners/bounded_edits_skill_generator.py`; supplied runtime repair account | [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement); low-level bounded-edits package internals not independently audited. |
| Mode B evidence filtering, receipt admission, diagnostic retention | Direct: `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/baselines/prompts.py`, `skilllift/skilllift/oracle_contrast.py`, `skilllift/skilllift/persistence.py` | [MEM-OBJ-receipt-rubrics](#mem-obj-receipt-rubrics), [MEM-OBJ-receipt-metadata](#mem-obj-receipt-metadata), [MEM-OBJ-revision-attempts](#mem-obj-revision-attempts), [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision). |
| Logical trial cache and physical attempts; loader/deployment receipts | Direct store methods; supplied `skilllift/skilllift/coordinator/task.py`, WildClaw and SkillsBench adapter findings | [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery). External receipt accuracy remains unresolved. |
| Category CLI train/test, completed-round snapshots, winner fusion and final-skill replacement | Dispatch search: `skilllift_eval/skillsbench_cli.py`; direct: `skilllift_eval/runners/skilllift_skillsbench.py` | [MEM-OBJ-category-round](#mem-obj-category-round), [RT-RTE-category-training](runtime.md#rt-rte-category-training). Adapter reuse authentication not independently traced. |
| Domain train, markdown updates and checkpoint cleanup | Direct: `scripts/skilllift_tau2_run_domain.py`, `scripts/skilllift_tau2_real_llm_train_evolve_smoke.py` | [MEM-OBJ-cluster-checkpoint](#mem-obj-cluster-checkpoint), [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion). Detailed update validator semantics not inspected. |
| tau2 simulation trace reduction, score projection and diagnostic persistence | Direct: `skilllift_eval/runners/skilllift_tau2.py`, `skilllift/skilllift/oracle_contrast.py`; domain store calls | [MEM-OBJ-behavior-summary](#mem-obj-behavior-summary); raw trajectory serialization is identified by source search, not fully read. No full-trace-to-rule conclusion. |
| Cluster artifact fusion, MASTER_SKILL packaging and held-out injection | Direct fusion/packaging: `skilllift_eval/runners/skilllift_tau2.py`; direct rendering/load: `skilllift_eval/skills/tau2_loader.py`; supplied master-loader checks | [MEM-OBJ-master-skill](#mem-obj-master-skill), [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery). |
| Generic ExperimentStore checkpoint/reset APIs | Direct: `skilllift/skilllift/persistence.py`; repository call-site search | Storage/reset capabilities established. Search found definitions but no checkpoint callers in searched `skilllift/skilllift` and `skilllift_eval`; no deployed checkpoint route inferred. |
| Invalid-run archive/pruning | Direct: `scripts/lib/run_retention.sh`; call-site search in `scripts`, supplied script identity finding | Known caller `scripts/run_skilllift.sh` launches coevoskills, not the selected SkillLift task route. Archive pruning cannot establish withdrawal of accepted SkillLift skills. |
| Comparison baselines and alternate batch/standalone entry paths | Dispatch identifies no_skill, human_skill, autoskill, textgrad and coevoskills in `skilllift_eval/cli.py`; wider baseline internals not inspected | Included repository material, unresolved memory mechanisms. Prevents repository-wide claims about learning, feedback filtering, retention or admission across all algorithms. |
| Injection patch and external host working-context control | `scripts/oh_skill_patch.py` not independently inspected; supplied task-adapter loading account | Prevents full loader transformation/host context account. Host memory is not attributed to SkillLift. |
| Opaque model/provider state | Supplied `skilllift/skilllift/llm_client.py` account | [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client); no local weights or embedding store inferred. |

## Core ideas

1. **Task continuation is replay, not just a saved final file.** The store reads the seed and accepted candidate IDs, reapplies original patches and checks parent/candidate hashes. A refined in-memory tree is not necessarily what this replay reconstructs. [MEM-OBJ-candidate-record](#mem-obj-candidate-record) and [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay) qualify resume identity.
2. **Retained evidence reaches different consumers in different forms.** Planning gets public task, current files, prior directions and scalar outcomes; scoring gets receipt and skill content; later benchmark execution gets skill content rather than optimizer audit history. The read-back is program-selected at scheduled calls, not agent-initiated retrieval from a general knowledge service. SRC-1: `skilllift/skilllift/portfolio/prompts.py`, `skilllift/skilllift/baselines/prompts.py`; [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery).
3. **Receipts retain the optimizer's behavior-shaping rules.** Rank contrast can change later verification/refinement inputs, while candidate selection remains separately controlled by benchmark reward and tie-breaking. Retained metadata can preserve a requested diagnosis, but its presence does not certify criticism or make it an enforced scoring rule. [MEM-OBJ-receipt-rubrics](#mem-obj-receipt-rubrics), [MEM-OBJ-receipt-metadata](#mem-obj-receipt-metadata).
4. **A retained execution summary is not automatically learning input.** tau2 derives coarse behavior labels from messages, saves them inside OracleScore feedback, then projects that feedback out of the shared public-score payload used for receipt revision. The scalar outcome still affects selection and calibration. [MEM-OBJ-behavior-summary](#mem-obj-behavior-summary) prevents equating diagnostic retention with trajectory-based instruction induction.
5. **The alternate drivers preserve full content snapshots.** Category round markers and domain cluster checkpoints hold skills and receipts directly. Fusion is a further model-authored transformation with structural checks, not an assurance that all source rules or their reasons survive. [MEM-OBJ-category-round](#mem-obj-category-round), [MEM-OBJ-cluster-checkpoint](#mem-obj-cluster-checkpoint), [MEM-OBJ-master-skill](#mem-obj-master-skill).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-skill-instructions
Label: Portfolio skill instruction bodies

Part of: [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref)

Source-native identity: Markdown `SKILL.md` content in the PortfolioRef tree. Representational form: natural-language instructions; frontmatter and directory/file identity are symbolic packaging, not the instruction semantics. Storage: seed/candidate/final filesystem trees and the replayable patch chain. Lineage: benchmark/native seed plus generator edits under a planner direction. Seed authorship and per-content human approval are unresolved from these interfaces; subsequent proposals and admission are computational in the inspected coordinator. SRC-1: `skilllift/skilllift/portfolio/store.py`, `skilllift/skilllift/portfolio/prompts.py`; [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution).

Consumers: planner/editor/verifier, then external benchmark agent via loader. Natural-language behavioral authority is requested guidance, not a tool restriction. Persistence horizon: rounds, same-task re-entry and final trials; no demonstrated transfer/generalization. Reasons can reside in direction records, but benchmark delivery does not establish delivery of those reasons. Auxiliary scripts and references are distinct operative content within the same container: planner/editor can see selected text; actual host script execution and every auxiliary loading branch are uninspected. This prevents treating every portfolio byte as model-visible knowledge. The existing container remains valid; this part separates instruction content from runtime identity metadata.

> "[Patch Rules]\nChange only target_scope. Preserve curated skill identities. "
> "Use UTF-8 text under SKILL.md, scripts, or references; do not add dependencies or environments.",
> --- `skilllift/skilllift/portfolio/prompts.py`

#### MEM-OBJ-candidate-record
Label: CandidateRecord replay content and validation metadata

Source-native identity: `CandidateRecord`, durable `patch.diff`, `direction.json`, `validation.json`. Storage: task/round/candidate directories committed by staged directory replacement. Form: patch text interpreted by symbolic patch application, natural-language hypotheses/evidence references in direction JSON, and symbolic hashes/validity/error fields. These parts are consumed differently: patch and hashes reconstruct the tree; direction supplies scope/new-skill intent and proposal lineage; failure fields describe rejected proposals. This is not the PortfolioRef tree in [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref), but its retained reconstruction recipe. Closest route: [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution).

Lineage: generator output, planner direction and patch-validation result. A failed proposal is still saved; physical retention is not acceptance. Only accepted IDs drive parent replay, and invalid/mismatched records cannot materialize. Code admits the original patch through the inspected gate, then coordinator reward/verifier policy admits a successor. No per-record human approval is wired in that path. Original hypothesis, evidence refs and cross-skill rationale persist; replay uses scope and patch, not a model's interpretation of the rationale. New rounds can consume direction history separately. Refinement retains the original record; accepted refined content can therefore diverge from replay, as [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay) establishes. No new duplicate claim is declared.

> if not record.is_valid or record.candidate_hash is None:
>     raise PersistenceError(f"cannot materialize invalid candidate: {record.candidate_id}")
> if record.parent_hash != parent.tree_hash:
>     raise PersistenceError(f"candidate parent hash mismatch: {record.candidate_id}")
> --- `skilllift/skilllift/portfolio/store.py`

#### MEM-OBJ-search-state
Label: Task search state and proposal history

Source-native identity: `state.json`, `search_plan.json`, `previous_plan`, `history`, `direction_history`, `prohibited_novelty_keys`, accepted-candidate IDs and receipt field. Storage: PortfolioStore task/round JSON. Form: symbolic round/status/reward/hash/novelty data plus natural-language hypothesis/requirement/rationale content in plans and directions. This is durable control and planning input, not the PortfolioRef content or Receipt object; closest supplied route [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) includes its consumption.

Lineage: parsed planner proposals and scalar candidate evaluation outcomes; coordinator appends histories and serializes the selected receipt. Rejected/invalid/nonaccepted directions add novelty keys, so rejection leaves later search constraints rather than being erased. Code decides continuation/admission; caller launch supplies configuration but is not per-content approval. Store initialization checks seed and algorithm identity. Read-back triggers are scheduled next rounds and re-entry. Code looks up task/round identity, reloads prior plans, then builds explicit planner context containing previous plan, all supplied directions and scalar history. This is task-scoped accumulation, not semantic retrieval. Source: SRC-1, `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/portfolio/store.py`, `skilllift/skilllift/portfolio/prompts.py`.

> for branch in branches:
>     item = by_id.get(branch.record.candidate_id)
>     if item is None or not item.evaluation.is_valid or branch.record.candidate_id != accepted_id:
>         prohibited = frozenset({*prohibited, branch.record.direction.novelty_key})
> --- `skilllift/skilllift/coordinator/modes.py`

> f"[Previous SearchPlan]\n{_json(previous_plan.to_dict() if previous_plan else None)}",
> f"[Prior Direction History]\n{_json([item.to_dict() for item in direction_history])}",
> f"[Scalar SearchHistory]\n{_json(serialize_search_history(history))}",
> --- `skilllift/skilllift/portfolio/prompts.py`

#### MEM-OBJ-receipt-rubrics
Label: Receipt rules and signed scoring points

Part of: [RT-OBJ-receipt](runtime.md#rt-obj-receipt)

Source-native identity: `Receipt.rubrics`, criterion IDs, texts, signed points and computed bounds. Natural-language criteria request model judgments; symbolic IDs/points/hits determine score calculations. Storage: schema objects, task state receipt and ExperimentStore receipt JSON. Lineage: public-task/seed initialization, followed by model revision using visible skill evidence and oracle/verifier contrast. Subsequent admission is computational validation and, in task Mode B, best tested alignment selection. Human control of supplied task/configuration does not establish human approval of criteria. SRC-1: `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/coordinator/modes.py`; [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision).

Consumers: next-round/re-entered verifier requests, and generator guidance based on criterion hits. Natural-language rule interpretation is not mechanically certified; numerical score comparisons are enforced by code. The part differs from the container's metadata/rationale below. Persistent rules can change future decisions without any provider weight changes. The supplied runtime's separate theory-builder and learning limits remain: no observed criticism quality, capacity benefit or exercised self-improvement follows from this wiring.

> state.setdefault("receipt", receipt.to_dict())
> --- `skilllift/skilllift/coordinator/modes.py`

#### MEM-OBJ-receipt-metadata
Label: Receipt diagnosis and removal rationale

Part of: [RT-OBJ-receipt](runtime.md#rt-obj-receipt)

Source-native identity: `receipt.metadata.oracle_contrast_diagnosis` and revision `removed_rubrics` declarations. Form: natural-language hypotheses/reasons/evidence references in symbolic JSON slots. Storage: complete serialized receipts and revision-attempt artifacts. Lineage: rubricator proposal prompted to explain visible-text/score disagreement and explicitly account for removals. This is a requested explanation, not verified causal diagnosis. SRC-1: `skilllift/skilllift/baselines/prompts.py`, `skilllift/skilllift/rubricator.py`.

Reasons are not universally absent: the full receipt is sent to later verifier requests and future receipt revision, so retained metadata can reach those model consumers through `receipt.to_dict()`. The later consumer does not have a separate enforced diagnosis-reading decision rule; actual reliance remains unobserved. Removed criteria are excluded from active rubrics, while reasons can remain audit content. The prompt restricts removal declarations to the immediately prior version, so this is not a guaranteed cumulative rationale ledger. Preservation/admission is computational receipt validation; full validator enforcement of every explanatory requirement is not established here. This part distinguishes textual reasons from [MEM-OBJ-receipt-rubrics](#mem-obj-receipt-rubrics), whose points actively govern scoring.

> "- In receipt.metadata.oracle_contrast_diagnosis, write only an evidence-bounded hypothesis from visible skill text and public scores.",
> --- `skilllift/skilllift/baselines/prompts.py`

> "- removed_rubrics describes only removals from the immediately previous receipt version; do not copy historical removal declarations.",
> --- `skilllift/skilllift/baselines/prompts.py`

> "[Receipt]",
> _json(receipt.to_dict()),
> --- `skilllift/skilllift/baselines/prompts.py`

#### MEM-OBJ-revision-attempts
Label: Receipt revision attempt evidence

Source-native identity: ExperimentStore `receipt_revision_attempts`, with metadata, `prompt.txt`, `parsed_candidate.json` and `receipt_diff.json`; related scores, round states and events. Substrate: local JSON/text/JSONL files. Form: natural-language prompt/candidate/diagnostic content, symbolic acceptance/error/diff fields and numerical scores. Lineage: inputs and outputs of rubricator calls plus validators, not benchmark conversation transcripts. Closest supplied route [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision); distinct from the admitted receipt because rejected proposals and diagnostics also persist. SRC-1: `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/persistence.py`.

Physical writes are automatic. A first invalid candidate and its validation report reach a second repair call within the same revision episode. After two failures, the old receipt survives and an event records rejection. Later rounds consume the selected receipt and newly constructed contrast, not an established automatic reread of the entire attempt archive. Diagnostic artifact paths in round state are pointers for audit, not proof of model retrieval. Generic ExperimentStore reset can delete these files, but no inspected caller wires reset to this task route. This object therefore supports repair-context retention and audit storage, not a general experience-retrieval service.

> if attempt.accepted:
>     return candidate
> previous_payload = payload
> previous_report = report
> --- `skilllift/skilllift/rubricator.py`

#### MEM-OBJ-behavior-summary
Label: tau2 derived execution behavior summary

Source-native identity: OracleScore feedback metadata `execution_behavior_summary`. Storage: aggregate OracleScore objects, ExperimentStore oracle-score JSON and domain round-metrics JSON. Form: symbolic counts/termination counts and coarse textual pattern labels. Lineage: simulation messages → tool names/requestors and retry phrases → event counts/patterns → per-skill aggregation. Raw message content is not retained verbatim in this summary. No counterpart after comparison with [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion): this is its derived diagnostic part, not the domain skill or fusion product. SRC-1: `skilllift_eval/runners/skilllift_tau2.py`, `scripts/skilllift_tau2_run_domain.py`, `skilllift/skilllift/oracle_contrast.py`.

The reducer calls read-like name prefixes observations, user-requested non-read calls external actions, other calls agent actions, and detects retry phrases. These are code heuristics, not independently established action success or causal explanations. Automatic authorship and storage have no human admission step in the inspected path. Crucially, the shared public-score serializer outputs only score/pass/rank; `build_receipt_revision_input` passes scores plus rank and criterion contrast, not this feedback metadata. Thus diagnostic retention is wired but later instruction-authority through this summary is not established. Raw trajectory saving is separately identified in tau2 source; its exact persisted message schema and later readers remain uninspected, preventing a raw-trace replay claim.

> if behavior_summary:
>     metadata["execution_behavior_summary"] = behavior_summary
> --- `skilllift_eval/runners/skilllift_tau2.py`

> return {
>     "oracle_score": score.oracle_score,
>     "oracle_pass": score.oracle_pass,
>     "rank": score.rank,
> }
> --- `skilllift/skilllift/oracle_contrast.py`

#### MEM-OBJ-category-round
Label: SkillsBench completed-round content snapshot

Source-native identity: category/batch `round_result.json` and `batch_result.json`. Storage: train/category/batch/round filesystem JSON. Form: skill text/package contents and receipt rules alongside symbolic config hashes, winner IDs, skill hashes, scores, result paths and stop reasons. It is the persistent snapshot part of the supplied category route, rather than the patch-based PortfolioRef or task search state.

Part of: [RT-RTE-category-training](runtime.md#rt-rte-category-training)

This cross-kind relation means an operative checkpoint produced and consumed inside that route. Lineage: initialized/updated skills, verifier scores and task-by-skill benchmark matrix. Admission: software keeps a Mode A changed-key candidate only on nondecreasing verifier score; outer software selects winners and writes markers. Models author skill/receipt content. No per-marker human approval is wired. Resume reloads full skills and receipt from config-compatible completed rounds; best completed round supplies the batch winner. Fusion gets batch winner payloads, not all round evidence; final category output is a materialized replacement tree. Tests hash that tree and reuse compatible score markers. SRC-1: `skilllift_eval/runners/skilllift_skillsbench.py`.

> if marker is not None:
>     completed_rounds.append(marker)
>     skills = {self._skill_key(token): self._skill_from_dict(data) for token, data in marker["skills"].items()}
>     receipt = self._receipt_from_dict(marker["receipt"])
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

#### MEM-OBJ-cluster-checkpoint
Label: tau2 round checkpoint snapshot

Source-native identity: `skilllift_state/<cluster_id>/round_checkpoint.json`. Storage: domain run-root JSON; source uses generic `write_json`, not PortfolioStore atomic immutable-marker protocol. Form: full natural-language skill/receipt contents with symbolic completed-round index and round metrics. It is not [MEM-OBJ-category-round](#mem-obj-category-round), whose config checks differ.

Part of: [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion)

This is an operative state part of the domain route. Lineage: computational skill update/revision followed by checkpoint serialization after Mode A. Reload deserializes skills and receipt and starts at completed round + 1. `_load_cluster_checkpoint` does not compare a configuration signature in the inspected method; compatible-looking content alone does not establish configuration-complete resume. Generic caller/run-root choice leaves original human content control unresolved, but subsequent transformation/admission is model/code driven. On successful cluster completion the checkpoint is deleted; trained artifacts remain separately available to fusion. SRC-1: `scripts/skilllift_tau2_run_domain.py`.

> return {
>     "start_round": int(data["completed_round_index"]) + 1,
>     "skills": skills,
>     "receipt": Receipt.from_dict(data["receipt"]),
>     "round_metrics": data.get("round_metrics", []),
> }
> --- `scripts/skilllift_tau2_run_domain.py`

> _ckpt = _cluster_checkpoint_path(config.run_root, cluster.cluster_id)
> if _ckpt.is_file():
>     _ckpt.unlink()
> --- `scripts/skilllift_tau2_run_domain.py`

#### MEM-OBJ-master-skill
Label: MASTER_SKILL fused domain guide

Source-native identity: `MASTER_SKILL.md`, matching `best_skill_bundle.json` single-skill content and `fusion_artifact.json` provenance. Storage: domain master_skill_fusion directory. Form: natural-language rules; symbolic bundle domain/skill identity, input hashes, output hash, prompt hash, artifact paths and coverage metadata. Content and access/provenance metadata are not interchangeable: held-out loading checks identity, content equality and hash, while the agent receives rendered skill/policy text. Closest supplied route [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion); no PortfolioRef counterpart because this is separately bundled prompt-context content. SRC-1: `skilllift_eval/runners/skilllift_tau2.py`, `skilllift_eval/skills/tau2_loader.py`.

Lineage: retained cluster SKILL.md bodies → model fusion → nonempty fenced-body extraction and XML/HTML rejection → Markdown and bundle. The fusion prompt requests deduplication, safer conflict handling, disputed-rule retention with source hashes and explicit coverage gaps. These requests are not verified semantic curation. The inspected `_load_cluster_skills` copies input hash labels from artifact metadata without recomputing each input-content hash. Output hash/equality checks consequently certify output association, not authenticity or correctness of all upstream rules. Human selects domain/configuration; code/model admits fusion without a demonstrated per-rule approval. Failure retains prompt/raw-output artifacts and raises; no observed successful fusion is asserted.

> '6. If two safer rules cannot be reconciled, preserve both under a "## Disputed" heading with the source skill hash; do not silently drop either.',
> '7. If an action type in the required list is not covered by any input skill, emit "## Coverage Gap: <action_type>" with no fabricated rules.',
> --- `skilllift_eval/runners/skilllift_tau2.py`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution)

Read-back is code-requested at next rounds and evolve re-entry. Task identity selects a store; accepted IDs select patches; current plan lookup can bypass a new planner call. Planner receives history and hypotheses through an explicit prompt, so rejected experience can shape later search via both model input and code novelty prohibition. Scalar outcome retention is a trace-fed planning update, not full trajectory induction. Skill edits then persist as instructions for benchmark agents. Source: SRC-1, `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/portfolio/prompts.py`, `skilllift/skilllift/portfolio/store.py`; [MEM-OBJ-search-state](#mem-obj-search-state) retains the supporting passages.

Planner working-context control: full portfolio evidence is attempted; optional core-only fallback replaces auxiliary evidence on character overflow, then preflight still rejects oversize input. History is explicitly supplied, not automatically summarized here. Its maximum horizon is task rounds/re-entry, and its growth can stop planning rather than guarantee a fit. This is not unsolicited push retrieval: the coordinator requests a specific next-step operation.

> prompt = prompt_with(_complete_evidence_pack(portfolio))
> if (
>     core_evidence_on_overflow
>     and max_input_chars is not None
>     and len(prompt.system) + len(prompt.user) > max_input_chars
> ):
>     prompt = prompt_with(_core_evidence_pack(portfolio))
> return _preflight(prompt, max_input_chars)
> --- `skilllift/skilllift/portfolio/prompts.py`

#### On [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement)

The editor operates in a fresh explicit request frame. More than 20 scoped files, incompatible snapshots or character overflow trigger a separate file-selector model call. Its inputs are task, direction, manifest byte counts, mandatory/selectable flags, limits and selected skill context. Code preserves mandatory paths, bounds optional count/bytes, then sends a by-value snapshot of selected files. Omitted files remain in the filesystem; a later generator call can select them again, but the model has no in-window dereference operation. The metadata IDs are selectors for this request, not heap references. Only returned edits escape the call, plus diagnostics; no accumulated benchmark chat is inherited. SRC-1: `skilllift_eval/runners/bounded_edits_skill_generator.py`.

> optional_paths = tuple(optional_by_id[file_id] for file_id in selected_ids)
> selected_paths = tuple(sorted((*mandatory_paths, *optional_paths)))
> if not selected_paths:
>     raise PortfolioError("bounded edit file selector selected no files")
> return selected_paths
> --- `skilllift_eval/runners/bounded_edits_skill_generator.py`

Repair requests receive failed output and validation context according to the supplied runtime account. This isolation resembles a selected-input frame with a returned value; it is not host chat compaction. Retained refinement feedback requests instruction changes, but the replay mismatch prevents a blanket claim that accepted refined text survives re-entry. See [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay).

#### On [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision)

Write-side chain: recorded candidate reward + visible skill text + verifier criterion hits → rank/criterion contrast → rubricator proposal → validation/repair → selected receipt → later verifier/refinement. Original oracle origin is benchmark reward through adapters, not a reference answer invented by the verifier. Input evidence excludes private evaluator material and trajectories. Evidence packing protects the full body only under the exact `SKILL.md` key. Task portfolio conversion preserves manifest-relative paths rather than rebasing nested instruction files to that key. Under a configured positive budget, prefixed SKILL.md paths therefore enter the auxiliary list and can be prefix-truncated or omitted; entrypoint/referenced paths have priority, not full-body protection. The ordinary task Mode B caller passes no evidence budget, so its packing includes all file bodies. Its separate request-character preflight can reject the request rather than truncate it. Manifest paths and hashes alone do not establish that complete bodies reach a budgeted consumer. SRC-1: `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/baselines/prompts.py`, `skilllift/skilllift/coordinator/modes.py`.

> aux_paths.sort(
>     key=lambda path: (
>         0 if path == entrypoint else 1 if path in skill_md else 2,
>         path,
>     )
> )
> --- `skilllift/skilllift/rubricator.py`

> skill_md = skill.files.get("SKILL.md", "")
> entrypoint = skill.entrypoint or _first_python_file(skill.files)
> aux_paths = [path for path in sorted(skill.files) if path != "SKILL.md"]
> --- `skilllift/skilllift/rubricator.py`

> remaining -= limit
> aux_files.append({"path": path, "content": content[:limit]})
> --- `skilllift/skilllift/rubricator.py`

> str(entry["path"]): (portfolio.root / str(entry["path"])).read_text(encoding="utf-8")
> for entry in portfolio_manifest(portfolio.root)
> --- `skilllift/skilllift/coordinator/modes.py`

> current_receipt = revise_receipt(
>     revision_input,
>     rubricator_client,
>     experiment_store,
>     max_input_chars=self.config.max_context_chars,
> )
> --- `skilllift/skilllift/coordinator/modes.py`

The packing limit concerns [EPI-RTE-evidence-packing](epistemic.md#epi-rte-evidence-packing) and [EPI-OBJ-evidence-package](epistemic.md#epi-obj-evidence-package), not a guarantee inferred from the evidence-scope label. Their supplied peer passages and the direct caller/key reads support this distinction.

This is automatic experience-responsive rewriting of retained scoring guidance: no full execution trace is needed for scalar rank feedback to shape a later rule set. It does not establish improved capacity or the truth of a model's explanation. Retained rationale may reach later verifier/revision calls in full receipts, while attempt archives have only the repair/audit consumers established in [MEM-OBJ-revision-attempts](#mem-obj-revision-attempts). The supplied runtime's theory condition 3 remains requested/unobserved rather than inferred from these metadata slots.

#### On [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery)

Memory consumers are coordinator and adapter recovery code, not a knowledge-querying model. Symbolic fingerprint selects a logical result; started physical-attempt markers trigger recovery before retry. Raw attempt metadata and results affect whether execution repeats. They do not themselves become skill instructions. Invalid/infrastructure outcomes remain audit history; the supplied coordinator does not permanently finalize an indeterminate cell. SRC-1: `skilllift/skilllift/portfolio/store.py`; supplied runtime passage in this route supports the indeterminate-result distinction. A valid cached result can eliminate a future physical call, but store API existence alone would not establish that consumer—the supplied coordinator route does.

#### On [RT-RTE-category-training](runtime.md#rt-rte-category-training)

Completed-round snapshots reload full skill content/receipt, not replayable patches. `batch_result.json` can short-circuit the whole batch on resume. Fusion sees retained winner payloads and public batch task, without a guaranteed complete causal history. It parses a full agent_skill package and validates the runtime name; it is not reevaluated in the inspected train method before final publication. Requested preservation of complementary workflows is model guidance. Source: SRC-1, `skilllift_eval/runners/skilllift_skillsbench.py`; [MEM-OBJ-category-round](#mem-obj-category-round).

> payload = self.sg_client.call_json(system, user, temperature=0.0)
> package = parse_skill_package(payload, skill_format="agent_skill")
> validate_agent_skill_name(package, runtime_name)
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

Final tree replacement deletes prior category materialization; retained training markers remain independent. Held-out testing selects the category's complete final directory, not a semantic subset of its rules. Compatible config/skill-hash score markers can bypass trials; otherwise adapter reuse or execution receives the final tree. This scheduled read-back reaches downstream agents through benchmark deployment, not necessarily the optimizer's diagnosis metadata.

> root = self.settings.run_root / "final_skills" / category
> if root.exists():
>     shutil.rmtree(root)
> root.mkdir(parents=True)
> self._materialize(skill, root)
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

#### On [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion)

Alternative retained forms are full cluster checkpoints, trained cluster artifacts, aggregate score/metrics files and master bundles. Mode A's imported markdown helper parses/repairs and validates an update, then increments its version; parse/repair failure preserves the old skill. Unlike inspected category Mode A, this helper itself does not require a new verifier score to be nondecreasing before returning the candidate. This is an admission distinction, not evidence of observed degradation. SRC-1: `scripts/skilllift_tau2_real_llm_train_evolve_smoke.py`, `scripts/skilllift_tau2_run_domain.py`.

> except SkillPackageError as exc:
>     # Mode A update package invalid (parse/repair/validation 失败):
>     # 保留旧 skill,不递增 version,继续处理同组其他 skill。
>     # LLMOutputError(call_text 层,底层已重试)不在此捕获,继续向上 raise。
> --- `scripts/skilllift_tau2_real_llm_train_evolve_smoke.py`

Fusion selects SKILL.md content from supplied cluster artifacts; auxiliary files and full optimizer rationale are not loaded by `_load_cluster_skills`. Source identity labels/hashes survive in fusion input/provenance, but explanations need not survive in the master. The model is asked to preserve irreconcilable rules and gaps. Admission checks syntax/nonempty content and prohibited tags, not source-rule completeness. [MEM-OBJ-master-skill](#mem-obj-master-skill) carries these distinctions.

#### On [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery)

tau2 held-out delivery is full bundle skill text rendered beside public domain policy and constraints, persisted as prompt payload then handed through run configuration. Caller/domain/task identity selects the bundle; the loader does not perform semantic retrieval or select only relevant rules inside it. Rendering normalizes line endings/whitespace. Actual external skill_injected behavior is outside the available source. SRC-1: `skilllift_eval/skills/tau2_loader.py`; supplied runtime's master-loader identity checks remain conditional protocol evidence.

> "<public_domain_policy>",
> _plain(domain_policy),
> "</public_domain_policy>",
> skills_block,
> "<constraints>",
> "Use only information visible in the conversation, public policy, tools, and the skills block.",
> "</constraints>",
> --- `skilllift_eval/skills/tau2_loader.py`

## Write side

Task seeds are physically snapshotted/identified through adapters and store initialization; their original authorship and human admission are not fully established by the public interface. Subsequent model proposals are admitted by parser/patch rules and successor selection, not by the mere presence of a diff file. Rejected directions and invalid candidate records persist separately from accepted skill text. Mode A refines against receipt hits; Mode B revises receipt rules against retained scalar benchmark contrast. These are distinct transformations with different rejection gates. [MEM-OBJ-candidate-record](#mem-obj-candidate-record), [MEM-OBJ-search-state](#mem-obj-search-state), [MEM-OBJ-receipt-rubrics](#mem-obj-receipt-rubrics).

The raw-to-derived chain is bounded: benchmark results → scalar histories/rank contrasts → planning/receipt revision → later rules/edits. tau2 additionally maps simulation messages to coarse summaries, but strips summary metadata before shared receipt revision; full transcripts cannot be inferred as learning inputs from saved trajectory files. Neither retaining raw logs nor applying a score comparison establishes improved future capacity. [MEM-OBJ-behavior-summary](#mem-obj-behavior-summary), [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision).

Rationale is partly retained: direction hypotheses/evidence refs, receipt diagnosis/removal metadata and revision attempts. Later planning receives prior direction text; later verification/revision receives the full receipt. Downstream skill execution and fusion do not thereby inherit all optimizer reasons. A skill rule can survive without its originating evidence. This prevents both a universal reason-loss claim and a universal reason-preservation claim.

Maintenance is not one global withdrawal protocol. PortfolioStore validates reconstruction and frozen-final hashes; rejection preserves the parent. Category final publishing removes/replaces its materialized tree, while round markers retain historical content. Domain completion unlinks the round checkpoint but preserves trained/fused artifacts. Generic `ExperimentStore.reset_new_run` can recursively erase an experiment directory; call-site search does not establish use by these inspected paths. Invalid-run archive pruning keeps the lexically newest configured number of directories, but its known shell caller is the separately selected coevoskills driver. No inference that it revokes accepted SkillLift instructions follows. SRC-1: `skilllift/skilllift/persistence.py`, `scripts/lib/run_retention.sh`; [MEM-OBJ-category-round](#mem-obj-category-round), [MEM-OBJ-cluster-checkpoint](#mem-obj-cluster-checkpoint).

> if (( index > keep )); then
>   echo "[prune-invalid] removing ${attempt}"
>   rm -rf -- "$attempt"
> fi
> --- `scripts/lib/run_retention.sh`

## Read-back

| Later consumer | Trigger/selector | Selected retained material and delivery | Budget/authority/limit |
|---|---|---|---|
| Task replay code | evolve re-entry; task identity and accepted IDs | Seed plus original patches and hash metadata → reconstructed parent | Symbolic identity checks; accepted refinement qualification remains. [MEM-OBJ-candidate-record](#mem-obj-candidate-record). |
| Task planner | scheduled new plan; current task/portfolio, prior plan/history | Direction hypotheses, scalar outcomes, current file evidence → explicit model prompt | Character preflight/core fallback; no semantic search and no full task transcript. [MEM-OBJ-search-state](#mem-obj-search-state). |
| Editor/refiner | direction and receipt hits; code/model file selector | Mandatory plus selected optional snapshot content → isolated request | 20-file bound and configured character/byte budget; returned patch crosses back. [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement). |
| Verifier and rubricator | round scoring/calibration or resume | Full receipt; visible skill evidence and projected score/rank contrast → model prompt | Receipt metadata can be delivered, but interpretation is not assured; configured evidence budgets can truncate/omit prefixed instruction bodies as well as other auxiliary paths. Ordinary task Mode B uses no evidence budget; its character preflight can reject the full request. [MEM-OBJ-receipt-metadata](#mem-obj-receipt-metadata). |
| Trial recovery code | matching logical fingerprint or started attempt | Results/attempt markers plus adapter artifacts → reuse/recover/retry decision | Not knowledge instruction authority; not exactly-once remote execution. [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery). |
| Category training/fusion/testing | config-compatible markers; category/batch identity | Round skills/receipt; batch winner payloads; final category directory | Different admission from task replay; no semantic final-rule selection. [MEM-OBJ-category-round](#mem-obj-category-round). |
| Domain training/fusion | cluster checkpoint or supplied artifact paths | Full checkpoint; cluster SKILL.md bodies → next round or fusion request | Checkpoint loader lacks config comparison; copied input hash labels do not authenticate source content. [MEM-OBJ-cluster-checkpoint](#mem-obj-cluster-checkpoint), [MEM-OBJ-master-skill](#mem-obj-master-skill). |
| Held-out benchmark agent | domain/master bundle loaded for each task | Rendered public policy and full master skill → persisted prompt-context payload | Output identity protocol and natural-language guidance, not compliance proof. [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery). |

None of these inspected paths establishes independent unsolicited retrieval into an ongoing foreground conversation. Code requests specific operations and constructs their inputs. Fresh role calls keep benchmark chat and unrelated role state out; selection/fallback reduces what crosses the frame. Persistent files remain reachable to code, not magically dereferenceable by the model. Host trimming/compaction/reload beyond these explicit request builders is unresolved.

## Integration issues

- **No supported correction to supplied runtime facts.** Direct store/mode reads support the conditional refinement/replay risk in [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay); do not turn it into an observed failure. Full snapshots in category/domain routes are counterexamples to a system-wide patch-replay characterization.
- **Parts, not duplicates.** [MEM-OBJ-skill-instructions](#mem-obj-skill-instructions) is content inside [RT-OBJ-portfolio-ref](runtime.md#rt-obj-portfolio-ref); [MEM-OBJ-receipt-rubrics](#mem-obj-receipt-rubrics) and [MEM-OBJ-receipt-metadata](#mem-obj-receipt-metadata) split [RT-OBJ-receipt](runtime.md#rt-obj-receipt). Category/domain checkpoints explicitly belong to their supplied routes. The remaining new objects name persistence recipes, diagnostics or a separately bundled master rather than replacing supplied referents. No possible duplicate remains after that comparison.
- **Trajectory exclusion needs consumer-level interpretation.** [MEM-OBJ-behavior-summary](#mem-obj-behavior-summary) is derived from messages and saved, yet its feedback metadata is projected out of the shared receipt input. Scalar outcomes still affect later policy. Raw trajectory serialization/readers, and external host memory, remain uninspected; this prevents claiming either full-trace learning or a repository-wide absence of trace consumers.
- **Evidence-body preservation is key- and caller-dependent.** The corrected annotation on [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision) agrees with [EPI-RTE-evidence-packing](epistemic.md#epi-rte-evidence-packing) and [EPI-OBJ-evidence-package](epistemic.md#epi-obj-evidence-package): only exact `SKILL.md` keys receive full-body protection under a budget. SRC-1, `skilllift/skilllift/coordinator/modes.py` preserves manifest-relative paths; `skilllift/skilllift/rubricator.py` treats prefixed instruction paths as auxiliary. Consequently a budgeted diagnosis need not receive complete instructions. Ordinary task Mode B supplies no evidence budget and instead applies a rejecting character preflight; this correction does not assert default-path truncation.
- **Rationale delivery is not rationale reliance.** [MEM-OBJ-receipt-metadata](#mem-obj-receipt-metadata) adds evidence that a full serialized receipt reaches later models; [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision) leaves actual diagnostic reliance unobserved. Reconciliation should preserve both rather than converting the delivery into demonstrated criticism.
- **Different admission/recovery gates remain consequential.** [MEM-OBJ-category-round](#mem-obj-category-round) uses config-compatible markers and verifier nondecrease; [MEM-OBJ-cluster-checkpoint](#mem-obj-cluster-checkpoint) reloads without a signature comparison in its loader, and the imported domain update helper returns structurally validated new text without category's immediate nondecrease check. Fusion structural checks do not validate complete rule preservation. These limits qualify [RT-RTE-category-training](runtime.md#rt-rte-category-training) and [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion), not task patch invariants.
- **Remaining included material is not hidden absence.** Comparison baseline stores, every standalone/batch command, injection-patch branches, raw trajectory readers and low-level update/package validator semantics remain partially or wholly uninspected as the inventory states. The analytical consequence is a route-scoped report, not a complete enumeration of all repository memory behavior. Unavailable benchmark/host source separately prevents end-to-end activation and reward verification.

## Limitations and checks

The source checkout HEAD was rechecked as `599358b4d4c4a27c0e004df8228ab93026600653`; `git status --short` produced no changes. Source identity agrees exactly with the supplied boundary/run. The supplied job, member/peer types, collection, worker rules and records contract were read completely, including bounded continuation reads. No target code/tests, providers, submodule fetching or additional agents were run. Evidence is source wiring and prompt intent, not observed operation or causal benefit.

Strong claims were checked against alternatives: failed candidates remain retained without promotion; category/domain snapshots do not use task patch replay; receipt metadata can preserve reasons; tau2 behavior summaries exist despite the trajectory-excluded revision label, but consumer projection prevents assuming they shape revision. Generic storage/reset APIs and path IDs were not promoted to deployed retrieval routes. The working-context conclusions concern explicit model-request construction, not opaque provider/host processing. This correction rechecked evidence packing, manifest-key conversion and the task Mode B caller directly in SRC-1, `skilllift/skilllift/rubricator.py` and `skilllift/skilllift/coordinator/modes.py`. Exact-key protection does not cover every nested instruction body under a budget; the ordinary task caller's omitted budget is the counterexample to a default truncation claim.

Validation: the invocation-specific deterministic validate-output check passed: “Member content check passes; invocation residue not checked.” This establishes structural and quotation checks, not job acceptance, claim support or operational reliability.
