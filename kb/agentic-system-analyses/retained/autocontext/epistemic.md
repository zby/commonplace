---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Autocontext epistemic routes: evaluation domains, retained advice, imported warrant and the limits of improvement claims."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
---

# Autocontext epistemic report

## Source-and-claim boundary

The question is how attempts, judgments and retained context acquire warrant and consequential force. The frozen whole-system boundary and exclusions are [the boundary](boundary.md#boundary-and-evidence); evidence identity is its [Source register](boundary.md#source-register). All new inspection below is SRC-1, implementation or explicitly labelled doctrine/design. There was no target execution, inspected run trace or causal experiment. Accessible implementation supports differentiated architectural findings, not an exercised system-wide learning verdict.

The product claim is [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement). A narrower instruction to derive operational rules from outcomes is [EPI-CLM-lessons-derived](#epi-clm-lessons-derived). Scores, format checks, context promotion, imported metadata and an instruction to produce explanations are not interchangeable evidence of truth. Most advice is prescriptive; conditional empirical statements inside it can be truth-apt. No concrete generated lesson or explanation with a linked producing run was supplied. Its precise propositional content and semantic update relation therefore remain not determinable, rather than being classified as conjecture solely because a model generated it.

### Coverage

“Supplied” means reliance on the runtime record, not a fresh source read. “Direct” means source inspected in this job. Available but uninspected paths remain included; this report makes no system-complete negative about acceptance or knowledge production.

| Entry point or operation | SRC-1 source path | Coverage and record, or limit and conclusion prevented |
| --- | --- | --- |
| Python CLI dispatch and subcommand registration | `autocontext/src/autocontext/cli.py` | Direct registration search; main loop and task routing supplied: [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), [RT-RTE-task-revision](runtime.md#rt-rte-task-revision). Registered epoch, labels, prescreen, probes, rescore, investigate, simulate, campaign, self-improve and sharing algorithms not fully traced; no complete evaluator/maintenance inventory follows. |
| Python support-role production | `autocontext/src/autocontext/prompts/templates.py` | Direct coach/analyst/architect tasks and prompt assembly: [EPI-RTE-role-proposals](#epi-rte-role-proposals). Delivery/budget supplied: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly). |
| Tournament and gate | `autocontext/src/autocontext/loop/stages.py` | Supplied: [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation). Individual scenario scoring/holdout/probe implementations uninspected here; no universal correctness oracle or score-to-mechanism inference. |
| Context-bundle evaluation/promotion | `autocontext/src/autocontext/context_bundles/promotion.py` | Direct comparison dispatch and component-attribution restriction; supplied full admission route: [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion). Evaluator internals/statistical assumptions not independently audited. |
| Judge, hooks, revision and verifier/checkpoint consumers | `autocontext/src/autocontext/execution/judge.py`; `autocontext/src/autocontext/execution/improvement_loop.py` | Direct judge evaluation and downstream verifier, checkpoint and best-selection branches: [EPI-RTE-judge-evaluation](#epi-rte-judge-evaluation), [RT-RTE-task-revision](runtime.md#rt-rte-task-revision). |
| MCP registered operations | `autocontext/src/autocontext/mcp/server.py` | Direct function/registration enumeration and package/skill evaluation wrappers. Reads, solve, judge, tournament, task generation, feedback, distillation, artifact publication, package import/export, monitors and evidence are exposed. Package mutation traced below; feedback calibration, distillation/publication consumers and evidence-producing internals remain uninspected, preventing complete truth-route enumeration. |
| SDK/HTTP and lifecycle operations | `autocontext/src/autocontext/server/knowledge_api.py`; `autocontext/src/autocontext/knowledge/lifecycle.py`; `autocontext/src/autocontext/storage/artifacts.py`; `autocontext/src/autocontext/storage/artifact_skill_lessons.py` | Direct lesson approve/reject/curate and live reader/writer paths: [EPI-RTE-lesson-curation](#epi-rte-lesson-curation). SDK dispatch supplied by boundary; full authentication and pending-playbook implementation not reaudited. |
| Portable knowledge packages | `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/knowledge/export.py`; `autocontext/src/autocontext/loop/stages.py` | Direct complete package module, skill rendering and metadata export, and active-bundle selection passages: [EPI-RTE-package-import](#epi-rte-package-import). Payload parts below separate guidance, attributed history and harness source. Source provenance/score veracity and downstream harness execution remain unverified. Optional task/reference fields are rendered into agent-task skills, not installed as a new task evaluator by the importer; full host consumption remains uninspected. |
| npm generation and promotion recommendation | `ts/src/loop/generation-runner.ts`; `ts/src/control-plane/promotion/decide.ts` | Supplied: [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation) and runtime account. Full rollout consumers and TS judge implementation uninspected; no Python parity conclusion. |
| Session consolidation | `ts/src/session/memory-consolidation.ts` | Direct complete file: [EPI-RTE-report-consolidation](#epi-rte-report-consolidation). Persistence and callers uninspected; returned lessons alone establish no live admission. Python session route remains independently unassessed. |
| Pi tools/command | `pi/src/index.ts` | Direct judge/improve handlers; all six tool names and command found by registration search. They expose npm implementations; Python judge findings are not projected onto them. Queue/status/scenario/snapshot internals not freshly traced: supplied [RT-RTE-task-revision](runtime.md#rt-rte-task-revision) and runtime account cover only the described seams. |
| Runtime hooks/extensions | `autocontext/src/autocontext/extensions/loader.py` | Supplied [RT-RTE-runtime-dispatch](runtime.md#rt-rte-runtime-dispatch); direct judge hook effects additionally traced below. Arbitrary extension behavior and enclosing host state are opaque alternatives, not a universal gate. |
| Training, ambient and kernel evolution | `autocontext/src/autocontext/training/runner.py`; `autocontext/src/autocontext/ambient/promote.py`; `autocontext/src/autocontext/kernel_evolution/runner_lifecycle.py` | Supplied [RT-RTE-training-experiments](runtime.md#rt-rte-training-experiments), [RT-RTE-ambient-promotion](runtime.md#rt-rte-ambient-promotion), [RT-RTE-kernel-evolution](runtime.md#rt-rte-kernel-evolution). Backend measurements, hardware correctness and actual checkpoints uninspected. |
| Solve/scenario creation, missions, sharing, shipped studies and other maintenance | Paths identified in [the boundary](boundary.md#boundary-and-evidence) | Solver/task dispatch supplied; creation quality, mission verification, complete sharing admission, benchmark archives and remaining shipped skill instructions not inspected here. Prevents a whole-system negative or observed improvement claim, not the positive routes below. |

No external provider or host implementation is frozen. Hosted model inference and trainer-produced checkpoints have separate mutability findings in [RT-CMP-role-models](runtime.md#rt-cmp-role-models) and [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints). Neither parameter knowledge content nor exact weight versions can be individuated from the source pin. Missing run evidence prevents observed acceptance/benefit findings; missing evaluator and artifact provenance prevents source-truth and mechanism/transfer findings even if a scalar result were supplied.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-strategy](runtime.md#rt-obj-strategy) | Usually policy/action parameters; explanatory fields may contain assertions | see record | SRC-1, `autocontext/src/autocontext/execution/supervisor.py` | Execution success checks the strategy in a scenario, not every explanation. Code-bearing mapping has separate executable force. |
| [EPI-OBJ-coach-lessons](#epi-obj-coach-lessons) | Conditional outcome claims can be truth-apt; imperatives are policy | see record | SRC-1, `autocontext/src/autocontext/prompts/templates.py` | Concrete generated content unavailable; requested consolidation is not proven non-ampliative reshaping. |
| [EPI-OBJ-judge-result](#epi-obj-judge-result) | Score/reasoning asserting rubric fit; optional factual dimensions | see record | SRC-1, `autocontext/src/autocontext/execution/judge.py` | Default confidence is not measured confidence; reference truth is external to judge implementation. |
| [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) | Bundle effect/comparison metadata, alongside candidate instructions | see record | SRC-1, `autocontext/src/autocontext/context_bundles/promotion.py` | Route cites a mixed container, not a declaration of its internal semantic content; bundle-level contrast does not isolate every component. |
| [EPI-OBJ-derived-lesson](#epi-obj-derived-lesson) | Existing lesson text plus symbolic active/stale status | see record | SRC-1, `autocontext/src/autocontext/knowledge/lifecycle.py` | `lastValidatedGen` is derived from current status, not an independent validation history. |
| [EPI-OBJ-strategy-package](#epi-obj-strategy-package) | Transport container; see payload parts | see record | SRC-1, `autocontext/src/autocontext/knowledge/package.py` | No unitary warrant or consumer. |
| [EPI-OBJ-package-playbook](#epi-obj-package-playbook) | Imported advice; conditional assertions may be truth-apt | see record | SRC-1, `autocontext/src/autocontext/knowledge/package.py` | Source warrant unknown; active bundle can supersede mutable playbook. |
| [EPI-OBJ-package-hints](#epi-obj-package-hints) | Imported hints; imperatives versus empirical assertions depend on content | see record | SRC-1, `autocontext/src/autocontext/knowledge/package.py` | Append is not conflict resolution of claims; active bundle has hint precedence. |
| [EPI-OBJ-package-lessons](#epi-obj-package-lessons) | Imported operational bullets | see record | SRC-1, `autocontext/src/autocontext/knowledge/export.py` | Text deduplication and skill emission do not establish truth or host use. |
| [EPI-OBJ-package-history](#epi-obj-package-history) | Attributed strategy, score/Elo and provenance assertions | see record | SRC-1, `autocontext/src/autocontext/knowledge/package.py` | Synthetic accepted/completed history is not fresh evaluation. |
| [EPI-OBJ-package-harness](#epi-obj-package-harness) | Executable validator policy; no particular proposition individuated | see record | SRC-1, `autocontext/src/autocontext/knowledge/package.py` | Source installed; execution, isolation and truth of checks untraced. |
| [EPI-OBJ-consolidation-result](#epi-obj-consolidation-result) | Prefixes of session reports, which may contain scoped assertions | see record | SRC-1, `ts/src/session/memory-consolidation.ts` | Name `promotedLessons` supplies no acceptance or persistence evidence. |
| [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints) | Not determinable at proposition level | see record | SRC-1, `autocontext/src/autocontext/training/runner.py` | Numerical state and metadata are distinct; no supplied weights, run or downstream assessment. |

## Authority-route ledger

Each row is a consequential function, not necessarily a different implementation. Repeated record citations intentionally split checking, disposition, retention and consumption. Record-owned fields say “see”; the columns assess the epistemic edge separately. No observed operation is asserted.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-role-proposals](#epi-rte-role-proposals) | content transformation | implemented | [EPI-OBJ-coach-lessons](#epi-obj-coach-lessons) | truth-apt transformation: indeterminate | Outcomes/prior advice to replacement guidance and explanations | Model interpretation; task instructions, no entailment checker | see record | Possible advice, hypotheses, findings | Candidate generation | No truth license from generation alone | Proposes later instructions/tools | Support roles → output text → advisory/proposal → generation and later storage | SRC-1, `autocontext/src/autocontext/prompts/templates.py` | [EPI-CLM-lessons-derived](#epi-clm-lessons-derived) | requested derivation is not checked derivation | Concrete text needed to distinguish reshaping, derivation and non-entailed conjecture; imperatives separately update policy. |
| [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation) | check/evidence production | implemented | [RT-OBJ-strategy](runtime.md#rt-obj-strategy) | no content change | Strategy validity and scenario performance | see record; scenario-specific evaluation | see record | Possible scores/replays/validation errors | Evidence for gate | At most outcome under supplied scenario/seed/executor | Supplies gate/retry input | Tournament → scores/replay → evidential → current generation | SRC-1, `autocontext/src/autocontext/loop/stages.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | none | Does not verify analyst causal explanation, transfer, or independent lesson contribution. |
| [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation) | disposition/acceptance | implemented | [RT-OBJ-strategy](runtime.md#rt-obj-strategy) | no content change | Continue with strategy, retry or roll back | see record | see record | advance/retry/rollback | Enforcing scheduler/selection | Operational performance selection, not acceptance of every associated claim | Changes current strategy and next attempts | Gate → runner state → enforcing → bounded run | SRC-1, `autocontext/src/autocontext/loop/stages.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | strategy versus lesson target | Existing bundle suppresses legacy playbook publication even on advance. |
| [EPI-RTE-judge-evaluation](#epi-rte-judge-evaluation) | check/evidence production | implemented | [EPI-OBJ-judge-result](#epi-obj-judge-result) | truth-apt transformation: indeterminate | Task output against rubric/reference | Model plus parsing, averaging, pinned dimensions and narrow guardrail; see record | see record | Possible score/reasoning/dimensions/provenance | Evidential, conditional veto by hooks | Rubric-relative assessment; caller reference assumed authoritative, not authenticated | Feeds revision/selection when consumed; standalone judge only returns result | Judge → structured result → evidential → invocation | SRC-1, `autocontext/src/autocontext/execution/judge.py` | none | score label versus factual warrant | Missing factual confidence defaults to 0.5; disagreement is not calibration. |
| [RT-RTE-task-revision](runtime.md#rt-rte-task-revision) | disposition/acceptance | implemented | [EPI-OBJ-judge-result](#epi-obj-judge-result) | no content change | Best task output and threshold termination | see record; optional external verifier can zero score; fact check only discounts | see record | Possible best output, threshold/not met, retry/stop | Ranking and enforcing threshold | Acceptance only for configured task criterion, not universal truth | Selects output/revisions; checkpoint failure does not veto | Loop → score/dimension predicates and revision feedback → enforcing/ranking → invocation | SRC-1, `autocontext/src/autocontext/execution/improvement_loop.py` | none | verifier versus non-vetoing checkpoint | No actual output or verifier result; a returned best output may remain below threshold. |
| [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) | check/evidence production | implemented | Context candidate/incumbent: see record | no content change | Matched bundle outcome contrast | see record; evaluator with fixture/seed identity | see record | Matched trials/comparison | Evidence for distinct promotion decision | Relative bundle effect under evaluator plan; attribution constrained by manifest diff | Enables or denies later promotion evidence | Evaluator/store → matched trial records → evidential → candidate campaign | SRC-1, `autocontext/src/autocontext/context_bundles/promotion.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | no general mechanism warrant | Static paired-evaluation wiring is not a causal experiment observation. |
| [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) | disposition/acceptance | implemented | Context candidate/incumbent: see record | no content change | Activate evaluated bundle for scenario routing/context | see record; comparison confirmation, plan/lifecycle checks and optional audit/campaign authorization | see record | Promotion, defer, negative result | Enforcing at coordinator | Scoped admission based on matched outcome criterion, not validation of every proposition | Switches active digest/routing or preserves incumbent | Coordinator → active store/orchestrator → permissive/enforcing → later generations | SRC-1, `autocontext/src/autocontext/context_bundles/promotion.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | narrower than universal admission | Audit optional; independent direct/import/npm/training paths remain. |
| [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation) | disposition/acceptance | implemented | Playbook: see record | no content change | Publish or stage coach replacement | see record; marker/guard, optional curator/approval | see record | Live write, pending or rejection | Admission policy | Format and optional model/operator approval; no matched-effect criterion shown here | Can change later npm context | Store → live/pending playbook → permissive → later generations/runs | SRC-1, `ts/src/loop/generation-runner.ts` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | not Python matched admission | Does not establish evidence-consuming acceptance of an ampliative factual claim. |
| [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation) | retention | implemented | Role outputs, guidance, run outcomes: see records | no content change | Persist generation/report/context artifacts | see records | see records | Stored attempts/reports/advice | Retention, not acceptance | No added warrant from durable storage | Makes artifacts available for future selection | Stores → files/SQLite → available → later runs | SRC-1, `autocontext/src/autocontext/loop/stages.py`; `ts/src/loop/generation-runner.ts` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | retention is not integration | No claim that all retained reports are accepted or always delivered. |
| [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) | operational admission/selection/consumption | implemented | Playbook, lessons, hints, reports: see record | no content change | Deliver selected retained guidance | see record | see record | Constructed prompts, possible trimming/compaction | Advisory through model interpretation | Delivery does not authenticate content | Permits guidance to shape later proposals | see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) | SRC-1, `autocontext/src/autocontext/loop/stages.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | delivery versus dependence | Semantic compaction and opaque host alternatives not fully inspected. |
| [EPI-RTE-lesson-curation](#epi-rte-lesson-curation) | disposition/acceptance | implemented | [EPI-OBJ-derived-lesson](#epi-obj-derived-lesson) | no content change | Active/stale/deadEnd/delete transitions | Caller action plus ID lookup; no truth evaluator in inspected function | see record | Status change, removal or not found | Enforcing mutation; partial downstream suppression | User-selected reliance state, not measured validation | Changes skill injection/dead-end advice; raw playbook remains separately delivered | HTTP → markdown rewrite → filter/advisory → future reads | SRC-1, `autocontext/src/autocontext/knowledge/lifecycle.py`; `autocontext/src/autocontext/storage/artifacts.py` | none | status is not universal withdrawal | Stale skill line filtered, stale playbook text not filtered by read_playbook; previously delivered context not revoked. |
| [EPI-RTE-package-import](#epi-rte-package-import) | content transformation | implemented | [EPI-OBJ-package-playbook](#epi-obj-package-playbook) | truth-apt transformation: acquisition/import | External playbook into mutable file and potentially rendered skill | see record; overwrite or empty destination under merge/skip | see record | File write or preservation | Permissive file installation | Source warrant unknown; no content/effect acceptance | Makes advice available, not necessarily active | File readers → selected prompt text → advisory → later generations; active bundle takes precedence | SRC-1, `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/loop/stages.py` | none | imported not accepted | Conditional on truth-apt payload; imperatives remain policy. Skill and playbook conflict branches can diverge. |
| [EPI-RTE-package-import](#epi-rte-package-import) | content transformation | implemented | [EPI-OBJ-package-hints](#epi-obj-package-hints) | truth-apt transformation: acquisition/import | External hints into mutable hints file | see record; overwrite, merge append, skip only if empty | see record | Replaced/appended/preserved hints | Permissive file installation | Source warrant unknown; appending does not reconcile incompatible claims | Makes hints available to later selection | Hint file → selected role context → advisory → later generations, subject to active bundle precedence | SRC-1, `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/loop/stages.py` | none | imported not accepted | Conditional on truth-apt payload; no observed activation. |
| [EPI-RTE-package-import](#epi-rte-package-import) | content transformation | implemented | [EPI-OBJ-package-lessons](#epi-obj-package-lessons) | truth-apt transformation: acquisition/import | External lessons into SKILL operational bullets | see record; overwrite/new skill rendering or merge exact-bullet deduplication | see record | Skill write, merged bullets, or preservation | Permissive skill installation/sync | Source warrant unknown; duplicate suppression is not validation | Makes lesson text available to skill readers | SKILL → skill context/host discovery → advisory → later invocations; host use uninspected | SRC-1, `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/knowledge/export.py` | none | imported not accepted | Conditional on truth-apt payload; formatting supplies no acceptance. |
| [EPI-RTE-package-import](#epi-rte-package-import) | content transformation | implemented | [EPI-OBJ-package-history](#epi-obj-package-history) | truth-apt transformation: acquisition/import | Attributed strategy/results/provenance into metadata and optional synthetic history | see record; metadata unconditional; SQLite restoration uses separate predicate and score/conflict comparisons | see record | Metadata plus possible imported completed run/snapshot | Symbolic persistence and snapshot eligibility | Attributed source warrant unknown; accepted/completed labels do not license local performance claims | Exposes package scores to history/export and potential inheritance selection | Metadata/SQLite → export/snapshot readers → descriptive/ranking inputs → later requests/runs | SRC-1, `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/knowledge/export.py` | none | synthetic history not measurement | Merge compares supplied scores without checking evaluator comparability; no observed downstream dependence. |
| [EPI-RTE-package-import](#epi-rte-package-import) | operational admission/selection/consumption | implemented | [EPI-OBJ-package-harness](#epi-obj-package-harness) | non-truth-apt policy/content update: imported executable validator source | Install named harness source, not evaluate its propositions | see record; overwrite replaces, otherwise existing source retained | see record | Source written/skipped; possible fenced copy in game-like skill | Permissive source installation, not demonstrated execution | No truth or correctness license; executable policy is distinct from advice | Changes available validator source; no traced execution consumer | Importer → harness source files → installed source → future potential validator use; execution horizon untraced | SRC-1, `autocontext/src/autocontext/knowledge/package.py`; `autocontext/src/autocontext/knowledge/export.py` | none | installation versus execution | No fresh validator test, runtime admission, sandbox or immediate activation established. |
| [EPI-RTE-report-consolidation](#epi-rte-report-consolidation) | content transformation | implemented | [EPI-OBJ-consolidation-result](#epi-obj-consolidation-result) | truth-apt transformation: indeterminate | Report text to 200-character prefix | Type/length and count thresholds; no semantic evaluator | see record | Returned promotedLessons array | Return only; live consumer uninspected | No added warrant; scope can be lost | Caller receives candidate text, not proven installation | Consolidator → return object → available → caller invocation | SRC-1, `ts/src/session/memory-consolidation.ts` | none | promotion name versus force | Concrete deduction below refutes guaranteed meaning-preserving consolidation. |
| [RT-RTE-training-experiments](runtime.md#rt-rte-training-experiments), [RT-RTE-ambient-promotion](runtime.md#rt-rte-ambient-promotion) | behavior/policy adaptation | implemented | [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints) | non-truth-apt policy/content update: weights, training source and active model binding | Keep/publish checkpoint or activate candidate | see records; backend trials or ambient anchor metadata, distinct admission policies | see records | Possible accepted checkpoint/registry binding | Executable training and serving selection | Empirical performance criterion, no proposition-level acceptance shown | Changes available training machinery and later model routing | see records; registry/serving channel, permissive, later inference | SRC-1, `autocontext/src/autocontext/training/runner.py`; `autocontext/src/autocontext/ambient/promote.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | none | No observed parameters, trial or later use; summary-derived training mode is not independent repeated measurement. |
| [RT-RTE-kernel-evolution](runtime.md#rt-rte-kernel-evolution) | disposition/acceptance | implemented | Kernel candidate/source: see record | no content change | Campaign champion selection | see record; benchmark correctness/performance policy and optional confirmation | see record | Accept/reject champion candidate | Enforcing within campaign | Benchmark-domain eligibility/performance, not explanation/transfer | Updates champion; feedback disclosure limits next proposal | see record; primary feedback to generator, enforcing selection, campaign horizon | SRC-1, `autocontext/src/autocontext/kernel_evolution/runner_lifecycle.py` | [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | none | Hardware/reference provenance and actual benchmark results uninspected. |

No lifecycle-integration finding is inferred from these retention or activation rows. Accepted bundle context is installed for use; the evidence here does not establish acceptance of an identified new explanatory claim followed by integration of that claim with its evidence. Included uninspected operations prevent turning that limit into a system-wide absence.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion), [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation), [RT-RTE-training-experiments](runtime.md#rt-rte-training-experiments), [RT-RTE-kernel-evolution](runtime.md#rt-rte-kernel-evolution) | None inspected | Bundle comparison can test aggregate effect; one-component manifest restriction bounds component attribution. No observed interventions/results supplied. | Attempts, evaluators, retained guidance and later consumers are wired; several improvement-directed change paths exist. | “Useful” lessons, successful self-improvement and transfer unestablished. Dead ends are also retained as avoidance advice, not universally discarded from all stores. |
| [EPI-CLM-lessons-derived](#epi-clm-lessons-derived) | see record | SRC-1, `autocontext/src/autocontext/prompts/templates.py`, doctrine/design in executable prompt construction | Requests conditional rules from worked/failed outcomes, deduplication and stale-advice removal | [EPI-RTE-role-proposals](#epi-rte-role-proposals), [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) | None inspected | No concrete lesson/source-outcome pair or isolated lesson intervention supplied | Implemented request to produce prescriptive guidance, with later delivery wiring | A request for empirical derivation is not a checked entailment or accepted generalization. |

## Bounded conclusion

**Retention and use are more strongly established than claim warrant.** Python and npm retain outcomes and support-role material, select it into later prompts, and have different publication gates. These are not merely static documents. The consumer is a role model, the channel is constructed context, the force is advisory, and the horizon can extend to later scenario runs: see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery). No supplied observation closes the gap from delivery to causal dependence or benefit.

**Evaluation licenses differ by target.** Scenario scoring judges behavior in its environment. The Python task judge assesses caller-defined rubric fit, optionally against caller-provided reference; its factual-confidence fallback is metadata, not external corroboration. External verification can veto threshold success, whereas a failed checkpoint is only reported. Context-bundle comparison can support scoped relative-effect admission rather than truth of each instruction. Kernel campaigns and training/ambient model selection target other objects under other criteria. None is a system-wide oracle. See the distinct check and disposition rows above.

**Imported and transformed material needs local warrant accounting.** [EPI-RTE-package-import](#epi-rte-package-import) handles separate payload parts, not one knowledge object. Imported playbook, hints and lessons have unknown source warrant and distinct replacement/append/deduplication branches. Their force is advisory through later file/skill selection; existing active-bundle playbook/hints take precedence, so successful import is not immediate activation. Imported strategy/results/provenance enter metadata and optionally synthetic accepted/completed SQLite history; those labels and score comparisons do not locally verify the attributed historical results. Imported harness source is available executable validator policy, not merely advice; its downstream execution and actual enforcement remain untraced. None of these import branches supplies fresh empirical acceptance. [EPI-RTE-report-consolidation](#epi-rte-report-consolidation) can drop a report's scope condition through prefix slicing. Its returned promotion label supplies neither an evidence-consuming acceptance decision nor an implemented downstream effect.

**Rejection and withdrawal are real but local.** [EPI-RTE-lesson-curation](#epi-rte-lesson-curation) removes or marks live bullets and can move a lesson into retained dead-end advice. Stale skill lines are suppressed by the skill injector, but marking stale is not universal revocation: the playbook reader returns its full body, and already delivered or external host copies are outside this mutation's enforcement. Approval toggles state; the derived last-validation field is not evidence of a fresh empirical check.

**No identified produced ampliative claim is shown accepted and integrated.** Prompt instructions request explanations, hypotheses and rules; actual outputs and outcome/provenance links were not inspected. Their relation could include reshaping, entailed statements about a particular result, non-entailed generalization, or policy-only advice. That unresolved classification does not negate implemented candidate generation or operational admission. Nor does it establish absence across the unassessed routes.

**Properties remain independent.** The training/model-routing and retained-guidance paths afford improvement-directed self-change of behavior-determining organization. Actual later behavior causally depending on the installed change is unobserved, so exercised self-improvement and success are not established. Improved future capacity (learning) is independently unestablished. Model-directed diagnosis of outcomes and harness proposals affords reflection-like work, but content-specific self-representations and both causal directions were not observed. For actual generated theories, theory-builder conditions 1–4 remain individually uninspected; requested explanations and score-selected candidates do not establish formulated criticism or its reuse. Bounded computational scheduling is implemented, but that does not establish autonomous theory building. These limits coexist with the supported evaluator, retention and admission architectures.

## Shared records

### Operative objects

#### EPI-OBJ-coach-lessons
Label: Coach lessons and replacement guidance

Source-native identity: `coach_task` requested lesson/playbook sections and the analyst/architect task descriptions. Natural-language assertions and imperatives; in-memory prompt/output strings, later artifacts through supplied routes. Distinct from [RT-OBJ-strategy](runtime.md#rt-obj-strategy), which is an execution mapping, and [RT-CMP-role-models](runtime.md#rt-cmp-role-models), which is the producer. No supplied operative-object counterpart after comparison. SRC-1, `autocontext/src/autocontext/prompts/templates.py`, implementation of request, doctrine/design of desired output. Concrete produced content is uninspected.

> analyst_task = (
>         "Analyze strengths/failures and return markdown with sections: Findings, Root Causes, Actionable Recommendations."
>     )
> --- `autocontext/src/autocontext/prompts/templates.py`

#### EPI-OBJ-judge-result
Label: JudgeResult and factual dimensions

Source-native identity: `JudgeResult` score/reasoning, dimension scores, raw responses and evaluator/fixture provenance. Mixed natural-language reasoning and symbolic numerical/identity metadata; in-process result, with consumer round/cache records. It is an output part of [RT-RTE-task-revision](runtime.md#rt-rte-task-revision), not the role-model component itself. No supplied object counterpart. SRC-1, `autocontext/src/autocontext/execution/judge.py`.

> if reference_context and not effective_pinned_dimensions:
>             if "factual_accuracy" not in avg_dims:
>                 avg_dims["factual_accuracy"] = avg_score
>             if "factual_confidence" not in avg_dims:
>                 # Default confidence: moderate when reference context available.
>                 # The judge cannot verify claims against external sources beyond
>                 # its training data — this is self-reported confidence only.
>                 avg_dims["factual_confidence"] = DEFAULT_FACTUAL_CONFIDENCE
> --- `autocontext/src/autocontext/execution/judge.py`

#### EPI-OBJ-derived-lesson
Label: Derived live lesson view

Source-native identity: `_DerivedLesson` / `_lesson_view` from playbook LESSONS blocks and SKILL operational bullets. Natural-language lesson and symbolic ID/status/view metadata. Markdown is durable substrate; view dictionary is reconstructed. Unlike [EPI-OBJ-coach-lessons](#epi-obj-coach-lessons), this object is the lifecycle projection of existing text, potentially imported or manually authored, not a particular coach output. Closest supplied [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) is a consumer route, not the same object.

SRC-1, `autocontext/src/autocontext/knowledge/lifecycle.py`: `_normalize_text` strips stale marker, leading bullet and whitespace differences; ID hashes normalized text; duplicate IDs collapse. `build_lifecycle` ignores supplied lesson store and staleness window. Active view receives the supplied current generation without evaluating its claim; HTTP supplies zero.

> "lastValidatedGen": current_generation if lesson.status == "active" else None,
> --- `autocontext/src/autocontext/knowledge/lifecycle.py`

#### EPI-OBJ-strategy-package
Label: Imported StrategyPackage content

Source-native identity: `StrategyPackage` used by `import_strategy_package`. This remains the transport container, not a unitary operative content license. Its serialized JSON/model carries the separately declared playbook, hints, lessons, history and harness payload parts below; hydration distributes them into different stores and consumers. Distinct from [RT-OBJ-strategy](runtime.md#rt-obj-strategy), which is an execution mapping, not this transport container. SRC-1, `autocontext/src/autocontext/knowledge/package.py`, import implementation. Optional task/rubric/reference/example fields can enter rendered agent-task skill text through `autocontext/src/autocontext/knowledge/export.py`; complete later host consumption is uninspected, so no authenticated reference or evaluator installation follows from their presence.

> if conflict_policy == ConflictPolicy.OVERWRITE or (conflict_policy == ConflictPolicy.MERGE and is_empty):
>             artifacts.write_playbook(scenario, package.playbook)
>             result.playbook_written = True
> --- `autocontext/src/autocontext/knowledge/package.py`

#### EPI-OBJ-package-playbook
Label: StrategyPackage playbook payload
Part of: [EPI-OBJ-strategy-package](#epi-obj-strategy-package)

Source-native identity: `StrategyPackage.playbook`. Natural-language advice and potential conditional assertions; package string, mutable playbook file, and potentially rendered SKILL copy. Distinct from generated [EPI-OBJ-coach-lessons](#epi-obj-coach-lessons): import supplies external text, with unknown original producer/warrant. No supplied runtime object counterpart. SRC-1, `autocontext/src/autocontext/knowledge/package.py`. Overwrite replaces; merge/skip write only when empty. The container's retained import passage supports this branch. In SRC-1, `autocontext/src/autocontext/loop/stages.py`, active bundle selection can replace this file's delivered playbook:

> playbook = bundle_text(
>             active_context,
>             ComponentKind.PLAYBOOK,
>             "playbook",
>             default=playbook,
>         )
> --- `autocontext/src/autocontext/loop/stages.py`

#### EPI-OBJ-package-hints
Label: StrategyPackage hints payload
Part of: [EPI-OBJ-strategy-package](#epi-obj-strategy-package)

Source-native identity: `StrategyPackage.hints`. Natural-language hints stored in package and mutable hint file; no supplied object counterpart. SRC-1, `autocontext/src/autocontext/knowledge/package.py`. Source warrant remains unknown. Overwrite replaces; skip preserves a nonempty destination. Merge appends, not checks truth or consistency:

> merged = existing_hints.rstrip() + "\n\n" + package.hints.strip() + "\n"
>                 artifacts.write_hints(scenario, merged)
> --- `autocontext/src/autocontext/knowledge/package.py`

Active-bundle hints remain serving authority in SRC-1, `autocontext/src/autocontext/loop/stages.py`; installing a mutable hint file does not establish its immediate delivery:

> # An immutable promoted bundle is the serving authority. Legacy
>         # hint_state.json may describe an older baseline and must not overwrite
>         # the bundle's matched-and-promoted hint component.
> --- `autocontext/src/autocontext/loop/stages.py`

#### EPI-OBJ-package-lessons
Label: StrategyPackage lessons payload
Part of: [EPI-OBJ-strategy-package](#epi-obj-strategy-package)

Source-native identity: `StrategyPackage.lessons`. Natural-language list rendered as operational bullets in SKILL Markdown, then synced to the Claude skill directory. Distinct from [EPI-OBJ-derived-lesson](#epi-obj-derived-lesson), a reconstructed lifecycle view; no supplied runtime object counterpart. SRC-1, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/knowledge/export.py`. New/overwrite skill renders the package, whereas merge appends only missing exact bullet strings. Skill/context readers can consume these as advice; neither deduplication nor emission authenticates empirical statements or proves host use.

> for lesson in package.lessons:
>             bullet = lesson if lesson.startswith("- ") else f"- {lesson}"
>             if bullet not in merged_lessons:
>                 merged_lessons.append(bullet)
> --- `autocontext/src/autocontext/knowledge/package.py`

#### EPI-OBJ-package-history
Label: StrategyPackage strategy results and provenance
Part of: [EPI-OBJ-strategy-package](#epi-obj-strategy-package)

Source-native identity: `best_strategy`, `best_score`, `best_elo`, `metadata`, and synthetic imported run/snapshot. Symbolic strategy mapping and numerical/provenance fields; package JSON, `package_metadata.json`, optional SQLite generation/agent-output/snapshot rows, and rendered skill strategy/score text. Distinct from [RT-OBJ-strategy](runtime.md#rt-obj-strategy): these are attributed historical strategy/results, not a strategy already submitted to execution. SRC-1, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/knowledge/export.py`. Metadata writes precede content conflict branches, even under skip. Optional history restoration requires a strategy, nondefault score/Elo or snapshot flag; skip preserves existing snapshot, merge rejects a lower supplied score. Those comparisons consume imported numbers without fresh evaluation or demonstrated cross-evaluator comparability. History/export/snapshot readers can later expose these values; exact subsequent strategy execution is not established.

> sqlite.create_run(run_id, package.scenario_name, 1, "import", agent_provider="package")
> --- `autocontext/src/autocontext/knowledge/package.py`

The import route's retained generation passage shows synthetic accepted/completed status. Export can propagate provenance from imported metadata when no snapshot supplies it:

> elif isinstance(imported_meta.get("metadata"), dict):
>             resolved_source_run_id = imported_meta["metadata"].get("source_run_id")
>             source_generation = imported_meta["metadata"].get("source_generation")
> --- `autocontext/src/autocontext/knowledge/export.py`

#### EPI-OBJ-package-harness
Label: StrategyPackage harness validator source
Part of: [EPI-OBJ-strategy-package](#epi-obj-strategy-package)

Source-native identity: `StrategyPackage.harness` named source strings. Symbolic executable Python source, persisted through `write_harness`; game-like skill rendering also embeds fenced source as text. No supplied runtime object counterpart: [RT-OBJ-strategy](runtime.md#rt-obj-strategy) is the executed strategy mapping, not imported validators. SRC-1, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/knowledge/export.py`. Caller proposes source; conflict policy admits installation without evaluating validator correctness. Existing harness is preserved except under overwrite. The intended validator role could enforce checks upon execution, but full execution consumers, isolation and effective authority are untraced; successful import establishes available source only. No particular truth-apt proposition is individuated in this payload.

> if conflict_policy == ConflictPolicy.OVERWRITE:
>             artifacts.write_harness(scenario, name, source)
>             result.harness_written.append(name)
>         elif existing_harness is not None:
>             result.harness_skipped.append(name)
> --- `autocontext/src/autocontext/knowledge/package.py`

#### EPI-OBJ-consolidation-result
Label: ConsolidationResult promotedLessons

Source-native identity: `ConsolidationResult.promotedLessons` and `dryRun`; natural-language prefixes plus symbolic result metadata. In-memory array returned by the TS session consolidator. Closest supplied reference is runtime's session-memory coverage limit, not a declared object; no supplied counterpart. SRC-1, `ts/src/session/memory-consolidation.ts`; retained storage and later consumer uninspected.

### Routes

#### EPI-RTE-role-proposals
Label: Support-role guidance proposals
Part of: [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation)

This narrows the parent route to semantic candidate production requested from analyst, coach and architect, not execution, scoring or storage. Owner: prompt constructor and role orchestrator; endpoints: scenario/prior context → role tasks → proposed natural-language guidance or tooling. SRC-1, `autocontext/src/autocontext/prompts/templates.py`. Models propose; this subroute does not decide publication or provide a separate answer oracle. Operating mode is the parent's bounded generations; requested guidance persists only through downstream storage.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Role task strings within PromptBundle; completion outputs through parent orchestration.
- Later read-back: Proposed playbook/lessons may reach later generations through parent persistence and context selection; no actual artifact lineage supplied.
- Delegated visibility: Role-specific task plus assembled scenario/context and selected evidence blocks; not every raw record is necessarily delivered.
- Selection predicate: Role and scenario context, hint style, constraint mode and notebook/evidence selections.
- Invalidation or expiry: Replacement playbook is requested to remove stale advice; compliance and semantic correctness uninspected.
- Activation or effect: Requests candidate guidance and executable proposals; no observed interpretation or benefit.
- Evidence limits: Executable prompt construction establishes instructions, not actual explanation, criticism or preservation of prior meaning.

> "1. A COMPLETE replacement playbook between markers. Consolidate all prior guidance, "
>         "deduplicate, and remove stale advice. This replaces the current playbook entirely.\n\n"
> --- `autocontext/src/autocontext/prompts/templates.py`

#### EPI-RTE-judge-evaluation
Label: Python judge evidence production
Part of: [RT-RTE-task-revision](runtime.md#rt-rte-task-revision)

This is the parent route's judge check, separated from its disposition, and can also be called independently. Owner: LLMJudge and hook bus. Endpoints: output/rubric/reference → provider samples → parsed/averaged/filtered JudgeResult. SRC-1, `autocontext/src/autocontext/execution/judge.py`; downstream consumer SRC-1, `autocontext/src/autocontext/execution/improvement_loop.py`. Computation proposes judgments; caller supplies rubric, optional reference/calibration and hook configuration. No independent answer oracle arises from model agreement. The optional reference is treated as authoritative by instruction, not authenticated. Mode: configured samples within open task evaluation or bounded revisions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JudgeResult including score, reasoning, dimensions and provenance.
- Later read-back: Loop caches verdicts by content/context fingerprint and uses reasoning for later revisions; standalone callers may simply return it.
- Delegated visibility: Judge receives output/task, rubric, optional reference/concepts/calibration; BEFORE_JUDGE can rewrite requests and AFTER_JUDGE responses.
- Selection predicate: Configured sample count; two attempts per sample on parse failure; parsed samples exclude failed samples when any parse succeeds; pinned dimensions filter result keys.
- Invalidation or expiry: Hook-altered prompt/response or mixed effective models prevents verified serving-spec/epoch assertion; parent handles evaluator-epoch comparisons.
- Activation or effect: Result is evidential to selection, not enforcing by itself; hooks can block; no observed factual correctness.
- Evidence limits: Parseability and consistent model identity do not establish truth, calibration or causal improvement; narrow same-span contradiction cap is a heuristic, not general logical validation.

> if not unbound_hook_effect and len(effective_models) == 1:
>             verified_spec = spec.model_copy(update={"judge_model": next(iter(effective_models))})
> --- `autocontext/src/autocontext/execution/judge.py`

The consequential consumer distinguishes fact-check penalties, external verifier veto and non-vetoing checkpoints. These are distinct force paths, not synonyms for validation:

> effective_score = max(0.0, effective_score * 0.9)
>                     cacheable_score = max(0.0, cacheable_score * 0.9)
>                     round_result.score = effective_score
> --- `autocontext/src/autocontext/execution/improvement_loop.py`

> effective_score = 0.0
>                     cacheable_score = 0.0
>                     round_result.score = 0.0
>                     verifier_vetoed = True
> --- `autocontext/src/autocontext/execution/improvement_loop.py`

> # AC-727: run the optional checkpoint command after the round
>             # has been judged + (optionally) verified. Non-vetoing -- a
>             # failed checkpoint logs a warning and emits an event but does
>             # not influence the round's score or termination.
> --- `autocontext/src/autocontext/execution/improvement_loop.py`

Additional inspected counterexample to unconstrained component-causal labels: SRC-1, `autocontext/src/autocontext/context_bundles/promotion.py`, restricts attribution to a single added manifest component and heldout trials. This qualifies, rather than supersedes, [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion).

> manifest_diff = context_bundle_manifest_diff(candidate, incumbent)
>         if len(manifest_diff.changes) != 1:
>             return
>         change = manifest_diff.changes[0]
>         if change.tested_component_digest is None or change.comparison_component_digest is not None:
>             return
> --- `autocontext/src/autocontext/context_bundles/promotion.py`

#### EPI-RTE-lesson-curation
Label: Live lesson approval rejection and curation

No supplied route counterpart after comparison: [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) admits bundles by evaluation; this route directly edits markdown by caller action. Owner: lifecycle functions exposed by knowledge HTTP routes. Endpoints: scenario/derived lesson ID/action → playbook and skill rewrite or dead-end movement → status/not found; subsequent artifact readers determine delivery. SRC-1, `autocontext/src/autocontext/knowledge/lifecycle.py`, `autocontext/src/autocontext/server/knowledge_api.py`, `autocontext/src/autocontext/storage/artifacts.py`, `autocontext/src/autocontext/storage/artifact_skill_lessons.py`.

Caller chooses action; code matches text-derived ID and mutates both lesson sources. Caller identity does not prove human deliberation. Approval reactivates a located lesson without empirical evaluation. Rejection deletes its bullet; deadEnd moves it to avoidance material; activate can move a dead-end block back into a playbook lesson. Open maintenance operation, not a trial; no answer oracle. No transaction across all copies or revocation of previously delivered prompts established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: active/stale/deleted/deadEnd or missing; HTTP returns status or 404.
- Later read-back: Fresh playbook/skill/dead-end reads see rewritten live source; full external host caches and copies uninspected.
- Delegated visibility: Lifecycle views expose reconstructed text/status/source; skill injector excludes marked lines while raw playbook reader returns full body.
- Selection predicate: Caller action, valid scenario and derived lesson/dead-end ID; existing source bullet/block must match.
- Invalidation or expiry: Explicit stale/delete/reject; automatic generation-age expiry is not applied by build_lifecycle, which discards staleness_window.
- Activation or effect: Writes/removes source text; suppression is reader-specific; observed downstream behavior uninspected.
- Evidence limits: State labels and current-generation view metadata are not evidence-consuming truth decisions; no exhaustive host-wide withdrawal or recovery audit.

> del lesson_store, current_generation
>     found, _text = _set_lesson_stale(artifacts, scenario, lesson_id, stale=False)
>     return "active" if found else None
> --- `autocontext/src/autocontext/knowledge/lifecycle.py`

> active_lines = [line for line in section.splitlines() if "<!-- autocontext:lesson-status=stale -->" not in line]
>         return "\n".join(active_lines).strip()
> --- `autocontext/src/autocontext/storage/artifacts.py`

> content = self._playbook_store(scenario_name).read("playbook.md")
>         if not content:
>             return EMPTY_PLAYBOOK_SENTINEL
>         return content
> --- `autocontext/src/autocontext/storage/artifacts.py`

#### EPI-RTE-package-import
Label: Strategy package live import

No supplied route counterpart after comparison: [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) is matched admission, whereas import writes live files under conflict policy. Owner: package importer, exposed by MCP wrapper. Endpoints: package data → conflict resolution → live guidance/harness/skill files and optional SQLite imported snapshot. SRC-1, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/mcp/server.py`. Caller supplies package and conflict policy, code chooses writes; no per-content human decision is established. The intended use is portable scenario hydration; rejection/skipping follows existing content and policy, not evaluated usefulness. Imported guidance shapes later roles via [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery). Imported harness source is installed as potential executable validator policy; its actual execution consumer, validation and security are untraced. Relative to the peer fragment [MEM-RTE-package-import](memory.md#mem-rte-package-import), this is the same import mechanism, not a distinct route; its payload objects above supply this member's separate warrant assessments.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ImportResult reporting written/skipped resources and optional snapshot.
- Later read-back: Scenario artifact readers and skill discovery consume imported content; SQLite can expose imported metadata to history/snapshot consumers.
- Delegated visibility: Playbook, hints and lessons become delivered text through later selection; a package's original evaluation record is not rerun in inspected importer.
- Selection predicate: Nonempty fields; overwrite/merge/skip and existing-file checks; optional sqlite enables imported snapshot persistence.
- Invalidation or expiry: Later overwrite/curation can replace mutable content; unified atomic rollback uninspected. Existing active-bundle playbook/hints retain serving precedence; this importer does not refresh those bundles.
- Activation or effect: Direct artifact and harness-source writes, skill sync and optional synthetic history; installed content is available, not demonstrated immediately active. Harness execution and later behavior on imported content are unobserved.
- Evidence limits: Imported score and accepted/completed labels are attributed package metadata, not newly measured success or matched admission.

> mean_score=package.best_score,
>         best_score=package.best_score,
>         elo=package.best_elo,
>         wins=0,
>         losses=0,
>         gate_decision="accepted",
>         status="completed",
> --- `autocontext/src/autocontext/knowledge/package.py`

#### EPI-RTE-report-consolidation
Label: Session report prefix consolidation

No supplied route counterpart after comparison: runtime names session consolidation as an uninspected surface; it does not declare this function. Owner: TS MemoryConsolidator. Endpoints: turn/session counters, force/dryRun and session_reports → threshold/type/length selection → prefix array in ConsolidationResult. SRC-1, `ts/src/session/memory-consolidation.ts`, complete direct implementation inspection. Code alone selects; no human/model semantic check or answer oracle in this function. Trigger defaults to ten completed turns or one completed session, with force override. No approval, rejection or rollback of durable knowledge is established because this function only returns a result.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ConsolidationResult, threshold-not-met or promotedLessons prefixes with dryRun flag.
- Later read-back: uninspected — callers and storage consumers not traced; returning a result establishes no later invocation delivery.
- Delegated visibility: Caller gets only selected report prefixes and metadata, not preserved scope/provenance links in each lesson.
- Selection predicate: Counter threshold or force; session_reports must be array; element string and trimmed length greater than twenty.
- Invalidation or expiry: inapplicable — no retained state is mutated by this function.
- Activation or effect: Returns candidate lesson strings; no live authority change demonstrated.
- Evidence limits: Prefix extraction is deterministic, not semantic summarization; system-level callers and actual reports uninspected.

> if (typeof r === "string" && r.trim().length > 20) lessons.push(r.trim().slice(0, 200));
> --- `ts/src/session/memory-consolidation.ts`

> return new ConsolidationResult({ promotedLessons: lessons, dryRun: opts.dryRun });
> --- `ts/src/session/memory-consolidation.ts`

Concrete static deduction, not target execution: with `force: true` and one session report equal to `"The test passed" + " ".repeat(185) + "only in simulation, not on hardware."`, trimming removes no internal spaces. The fifteen-character opening plus 185 spaces fills the first 200 characters. The returned lesson is that opening plus spaces; it omits the simulation/hardware qualification. This is not guaranteed meaning-preserving reshaping and gives no additional warrant to the broader apparent claim. Actual report semantics may differ; the overall truth-apt relation remains indeterminate rather than universally ampliative.

### Claims

#### EPI-CLM-lessons-derived
Label: Operational lessons derived from outcomes

Claimed operation: the coach should consolidate prior guidance and produce prescriptive operational rules from worked/failed outcomes. SRC-1, `autocontext/src/autocontext/prompts/templates.py`, doctrine/design embedded in implemented prompt. Narrower than [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement): this concerns the requested content-production relation, not product-wide benefit. It remains a request, not observed derivation.

> "2. Operational lessons learned between markers. Each lesson should be a concrete, "
>         "prescriptive rule derived from what worked or failed.\n\n"
> --- `autocontext/src/autocontext/prompts/templates.py`
