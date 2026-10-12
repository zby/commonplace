# Agent-R rerun audit

## Disposition

**Integrate with recorded limits.** No consequential defect requiring a hold was established in this bounded audit. The publication already distinguishes conditional example construction from successful export, external training, checkpoint adoption and demonstrated improvement. It also carries the incomplete auxiliary SciWorld epistemic inventory. Those qualifications are in the public synthesis, not supplied only by this audit.

Blockers: none established. This is audit clearance, not integration or certification that every worker obligation was fulfilled.

## Identity and authority

- Run: `AAS-2026-10-12-agent-r-216224d4270a-01`.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/agent-r-216224d4270a` (abbreviated W below).
- Method: `cd6e8250c5277c5c6295b6940a9b01e034c9daa7`.
- Source identity: `https://github.com/ByteDance-Seed/Agent-R`.
- Frozen source: W/`related-systems/ByteDance-Seed--Agent-R`, commit `82fcc1ca7873b460949ed49022146dd988c32e31`. Audit independently confirmed HEAD and clean source Git status.
- Publication: W/`kb/agentic-system-analyses/retained/agent-r/` (P below).
- Run evidence: W/`kb/agentic-system-analyses/state/AAS-2026-10-12-agent-r-216224d4270a-01/` (R below).
- Auditor: fresh independent Pi worker, `openai/gpt-6.1-sol`, medium reasoning; runtime environment explicitly supplies provider/model/effort. No analytical worker or coordinator role in this run.
- Commission: [audit procedure](../audit-a-rerun.md). Only this report was authored; no repair, delegation, advance, integration or commit.

## Inspection and historical comparison

Read the complete historical `kb/agent-memory-systems/reviews/agent-r.md` in origin. It names the same source commit, so the major differences below are not explained by upstream revision drift. Its findings were discrepancy leads, not authority. Commonplace borrowing suggestions and legacy taxonomy values were not acceptance requirements.

Read P's boundary, overview, synthesis, report verification and memory report completely. Searched the memory profile for checkpoint, retrieval and delivery classifications. Inspected attempt and judgment records, ran the supplied worktree's read-only inspection command, and compared all twelve published Markdown members byte-for-byte with R/artifact. All matched. The publication manifest adds member hashes and worker metadata to the minimal artifact manifest; this difference is not content drift.

Independent source work concentrated on the consequential historical differences: full `README.md` and `path_collection.py`; local inference and ordinary/prefix evaluation in `mcts_utils/llm_server.py` through line 215; planning helper excerpts in `mcts_utils/sciworld/eval_utils_sw.py`; source-path searches for evaluator inputs and relevant consumers. No target code, environment, model or training process was executed.

## Consequential findings

### 1. The narrower learning conclusion corrects historical overstatement

The historical account describes trace material becoming an always-present parametric memory through a trained checkpoint, although it acknowledges absent training configuration and weights. The new account does not establish that derivative checkpoint or its consumption. README delegates training to Xtuner and references the absent configuration. `FuncCallOffline` loads caller-selected `MODEL_DIR`; loading alone does not connect those weights to a generated Agent-R dataset.

The new result preserves the intended tree → revision material → external training → later actor chain, but separates source wiring from unprovided update/admission evidence. It also retains the actual cross-invocation tree-to-builder consumer rather than classifying all memory as checkpoint push. This is a supported qualification, not a meaningful coverage regression.

Evidence: source `README.md`, training section; `mcts_utils/llm_server.py:26-43`; P/`memory.md`, Read-back; P/`synthesis.md`, “What the improvement account establishes” and limitations on missing training/promotion machinery.

### 2. Export and correction claims are materially better qualified

Independent reading confirms numeric values are compared with environment strings: `pair_leaf_paths` uses `os.environ["BETA"]`, and both good-only and paired branches test floats against `os.environ["ALPHA"]`. Nonempty shipped CLI export cannot avoid these comparisons. Empty/early-return cases do not deliver examples. The publication explicitly carries this defect in its overview description and synthesis.

The README promises an adjacent correct path sharing a parent. The implementation pairs distinct leaf paths without that gate. Critique receives low-path action/observation text, then substring `good` or `uncertain` controls prefix continuation. Software inserts a stock admission, `Action: wait` and `ok.`, without executing the constructed splice. The old “first-error localization” idea therefore cannot be treated as reliable observed diagnosis or recovery. The new synthesis makes all of these qualifications visible.

Evidence: source `path_collection.py:34-247`, especially `pair_leaf_paths`, `revise_worst_path`, `conversation_generation` and `main`; source `README.md`, Introduction; P/`synthesis.md`, “From retained paths to a synthetic correction example”.

### 3. Retention and helper coverage are usefully separated

The new memory account preserves tree content, score metadata, revision conversations, loss flags, feedback and evaluation traces as distinct consumer paths. It does not lose the historical account's important context-deletion mechanism. Ordinary evaluation deletes from the conversation later saved; prefix evaluation maintains separate full history. Neither creates a retained summary.

Auxiliary SciWorld planning prompts do request world knowledge and retrospective diagnosis. The publication does not silently deny these functions: report verification records an incomplete epistemic inventory, and synthesis carries that limit explicitly. No complete assessment of all afforded knowledge/criticism routes should be inferred. This is acceptable with the published limit; expanding that inventory is follow-up, not an audit-only repair.

Evidence: source `mcts_utils/llm_server.py:83-215`; `mcts_utils/sciworld/eval_utils_sw.py`, `compose_prompt_to_plan`; P/`memory.md`, annotations and `MEM-CMP-context-helpers`; P/`report-verification.md`, Limits; P/`synthesis.md`, final limitations-table row.

## Operational evidence

The worktree inspection reports completed publication, no open/failed attempts, refusals, worker problems or canonical peer drift. Historical stale acceptances have later checks covering the same canonical versions with additional peer relations; the inspected judgments contain no rejection or semantic objection. These engine facts do not alone prove successful worker execution.

Nested Pi evidence was located in:

`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T13-59-16-666Z_01a13069-19ba-745a-b8d3-80c377c91314.jsonl`

At JSONL line 31, `message.details.results[2]` is the Agent-R coordinator result (exit 0). Its nested worker messages pair validation calls with actual tool results. All eleven analytical workers have a member-content-check pass in those embedded results. This is stronger than treating a proposed command as executed, but remains content validation, not semantic certification.

A transient problem is absent from the engine's empty worker-problems summary: the boundary worker's first validation used a nonexistent artifact path and exited 2. In coordinator `messages[18].details.results[0].messages`, exact paired call/result IDs are:

- `call_oqwsdVjAP83IHcenQ2IZFoPn|fc_0f5e71b0a4535e27016acce9be7f9c87d2a02536fce9c5b0a7`: missing artifact path, exit 2.
- `call_s1CrWScBHrotSVC5rBYsOwEW|fc_0f5e71b0a4535e27016acce9d11bc887d2a8d31e61b6f6b9fb`: actual R/artifact path; deterministic ambiguous-quote finding.
- `call_8sXY6ogO5aPBa4Sez8XSPntF|fc_0f5e71b0a4535e27016acce9eabaa087d290adf7fabc20834d`: same actual artifact path; member-content-check pass after qualification of the quotation locator.

Thus no unresolved validation failure is established here. The literal initially supplied command did not succeed; recovery used the actual run artifact path. This audit does not decide method-level permission for that command substitution or claim flawless procedural compliance.

The report verifier's source-read claim also has direct trace support. Coordinator `messages[36].details.results[0].messages` includes paired reads of `eval_utils_sw.py` at offsets 1 and 291, each with limit 290, and the final validation pass:

`call_EXKk1wc4nbYRuEdgd4baL8Aa|fc_068fbf21b95e7777016accf0ad2b9087d2b63858acf2192ca9`.

These reads corroborate auxiliary-source inspection despite the earlier boundary's initial partial-read inventory. They do not turn the deliberately unassessed epistemic functions into complete coverage.

## Coverage limits and follow-up

This audit was not a second analysis. It did not independently recheck every MCTS adapter, all epistemic records, every memory-profile classification, task-data membership, graphics, dependency compatibility or every worker input-reading obligation. Embedded traces were used for executed validation outcomes and selected verifier reads, not exhaustively certified. External environments, checkpoints and Xtuner remain outside the frozen evidence.

Necessary limits are already published: no target execution or causal experiment; defective nonempty export; unclosed training/promotion; unvalidated synthetic recovery; incomplete task/evaluation inputs; and incomplete auxiliary SciWorld epistemic inventory. No additional public qualification requiring a hold was established. Integration still requires the coordinator's normal exact-publication and origin-state checks.

## Validation

Owned report is frontmatter-free workshop text under `kb/work/COLLECTION.md`. Validate only `kb/work/agentic-system-reruns/audits/batch-03-agent-r.md`; no shared navigation or checklist mutation is authorized.
