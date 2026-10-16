---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "JEPA-Anything runtime baseline: host-model task compilation, deterministic scaffold admission, generated consumers and structural evaluators."
run-id: AAS-2026-10-15-jepa-anything-434b01ab7774-01
reviewed-boundary: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
---

# JEPA-Anything runtime report

## Runtime account

### Consequential work and ordinary invocation

The shipped agent-facing operation is a design compiler, not a trained prediction service. A user supplies a world-model task or existing repository. An enclosing agent interprets the Skill, derives one causal context/target boundary, proposes a JEPA configuration, repairs validator errors, generates interfaces, and is instructed to run generated contract tests. Its terminal product is an inspectable design handoff, not weights or an empirical result. This is the requested workflow in [RT-RTE-task-compilation](#rt-rte-task-compilation); actual host completion is unobserved. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`.

For an ordinary history-to-future rollout request, the host model first establishes the system instance, available history/actions, target/horizon and intended consumer. It asks the user only for unrecoverable causal blockers. It chooses provisional architecture/dimensions itself, records assumptions, and selects `repeated_transition` because the downstream intent requires repeated state advancement. The user's task identity becomes `task.id`, system identity becomes `task.system_id`, instance keys bind context to target, and `model.id` labels the proposed model. These are contract identities, not authentication principals. The host owns next-step choice and shell/tool invocation; the validator owns only deterministic design diagnostics. SRC-1: `jepa-anything-skill/references/world-model-conversion.md`, `jepa-anything-skill/references/design-protocol.md`, `jepa-anything-skill/scripts/validate_design.py`.

The context supplied to the host consists of the user request, inspected project facts, Skill and reference texts, current proposed configuration and returned diagnostics. The shipped instructions request those reads; the repository does not implement model-context isolation, compaction or a model-call scheduler. Tool execution permissions, inference, model version selection and any host recovery remain external under the [boundary](boundary.md). The host's model is [RT-CMP-host-model](#rt-cmp-host-model). Its natural-language guidance is [RT-OBJ-design-protocol](#rt-obj-design-protocol), with authority limited as [RT-BAP-skill-guidance](#rt-bap-skill-guidance) records.

A candidate JSON/YAML configuration is loaded as data, validated, and repaired by the host until valid. The validator returns machine-readable checks with diagnostic code, status, path and message, plus counts and a validity bit. The generator CLI independently repeats validation before rendering. It uses the validated mapping to substitute Python representations into fixed templates, writes configuration/report/manifest in a sibling temporary directory, and replaces a missing or empty destination. On success it prints generated paths; invalid design returns 1; handled loading/filesystem/scaffold errors return 2. This is [RT-RTE-scaffold-admission](#rt-rte-scaffold-admission). SRC-1: `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/scripts/generate_scaffold.py`.

Generated contract tests inspect declarations and exercise checks using fabricated values and callbacks. They do not implement the actual adapter or train a domain model. The generated adapter raises `NotImplementedError` after checking allowlists; the model is a `Protocol`. A downstream developer must provide implementations and measured evidence. Generated state consumption is nevertheless executable: [RT-RTE-state-consumption](#rt-rte-state-consumption) dispatches a supplied state through the selected callback mode. SRC-1: `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/adapter.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

### Alternate paths and forcing cases

Four source-inspected forcing cases bound the strongest claims. None was executed in this analysis.

1. **CLI versus direct rendering API.** The CLI validates first, but exported `render_scaffold(config, report, destination)` accepts its report argument without checking its validity or re-running validation. It checks declared output format and destination availability, not the complete design contract. Consequently “generator refuses invalid designs” is a CLI-path invariant, not a guarantee across every Python call. A caller could also write/edit generated Python directly. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`; [RT-CLM-validation-scope](#rt-clm-validation-scope).
2. **Declared lineage versus actual inputs and callbacks.** Generated adapter methods reject extra fields, and explicit helper methods compare system/instance/cutoff facts. Those helpers are separate calls; `consume_state` neither invokes them nor checks the model's numerical geometry. Caller-supplied callback code runs directly. During repeated transition, missing required exogenous input raises before that step, but previous callbacks may already have executed. There is no callback rollback or side-effect confinement in the dispatcher. SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/adapter.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.
3. **Soft geometry versus hard enforcement.** The core can store fixed orthonormal rows or learnable rows. Learnable initialization checks full rank, but optimization can change rank/conditioning. Forward analysis does not QR-project rows. An explicit scheduled post-optimizer hook can retract them in `qr_retraction` mode; merely configuring this mode does not invoke an external optimizer or hook. SRC-1: `jepa-anything-core/src/jepa_anything_core/opf.py`; [RT-RTE-core-projection](#rt-rte-core-projection).
4. **Successful structural checking versus learned evidence.** Generated claim-envelope checks compare supplied metadata, not measured statistical support. The recipe computes synthetic activity from oracle state coordinates, while its report explicitly disclaims learned activity and scientific results. Manifest verification checks publication consistency and integrity, not model performance. SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`, `recipes/synthetic-linear-dynamics/run_recipe.py`, `checkpoints/verify_manifest.py`; [RT-RTE-structural-checks](#rt-rte-structural-checks).

Material alternatives therefore include implicit or explicit Skill invocation, standalone validator CLI/API, generator CLI/direct API, generated direct callback consumers, direct numerical-core calls, synthetic recipe auditing, and checkpoint verification. The inspected paths contain no provider-native tool dispatch, remote-worker controller or approval mechanism of their own; that is a limit of these paths, not an assertion about the enclosing host. Callback implementations and host shell commands are outside the deterministic gate's coverage. SRC-1: `jepa-anything-skill/agents/openai.yaml`, `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

### Guarantees, execution authority and recovery

| Load-bearing guarantee | Owner / enforcement / strength | Coverage and external requirement | Separate conclusions |
|---|---|---|---|
| Invalid declared design is not rendered by generator CLI | Generator `main`, validity branch; invariant | CLI only; depends on the shipped validator and unchanged templates. Direct rendering bypasses this admission step. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Existing non-empty destination is refused | `_ensure_destination_available`; invariant for its checked state | Both renderer and CLI. Not a filesystem isolation or race-proof concurrent-writer guarantee; requires suitable filesystem permissions and no interfering writer. | implementation conclusion status: wired; operation conclusion status: uninspected |
| No hidden training during the requested Skill workflow | Skill instruction; policy | Host must obey. Renderer emits fixed non-training templates, but callback implementations and arbitrary host shell work are not sandboxed by it. | instruction conclusion status: claimed; operation conclusion status: uninspected |
| Configuration validity does not imply scientific support | Validator disclaimer and planned-claim contracts; protocol | Declaration/metadata checking only; real backend measurements and statistical interpretation required externally. | implementation conclusion status: wired; operation conclusion status: uninspected |

SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/assets/scaffold/src/jepa_task/evaluation.py.tmpl`. The table's guarantees are supported by the records below, not assertions of successful operation.

The capability surface is host file inspection/writing and deterministic Python tools, plus downstream arbitrary Python callbacks and optional numerical parameter updates. The current grant set is not supplied: “within the requested workspace” is instruction text, not an inspected permission object. The deployed isolation envelope is likewise unspecified; the repository does not establish what the host OS allows. No human per-candidate approval is required by the described Skill loop. User authorization to create/adapt a task is distinct from accepting each generated field. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

Rendering cleans the temporary directory on exceptions; it has no versioned rollback after successful replacement. Host design repair is a requested diagnosis loop, not implemented retry orchestration. Transition failures propagate without transaction recovery. Core retraction leaves optimizer state to the caller. These are different recovery boundaries and should not be collapsed into one reliability claim. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`, `jepa-anything-core/src/jepa_anything_core/opf.py`.

### Evidence coverage

All additional inspection remains SRC-1 implementation or doctrine/design at the frozen revision. Beyond the boundary's initial coverage, this report inspected validator report/dispatch, schema/naming and claim/output branches; generated adapter/model/evaluation and complete generated contract tests; OPF construction, basis access and retraction hooks; baseline EMA lifecycle; synthetic activity generation/reporting; checkpoint verification; and Make check wiring. Remaining validator branches and recipe audit branches were not exhaustively reviewed. This prevents a complete schema-audit or exhaustive recipe-correctness conclusion, not the route conclusions stated here. No target code, tests, providers or experiments were executed. No observed activation, completion, latency, reliability, learned benefit or causal effect is established. SRC-1: the paths cited in the relevant records.

## Shared records

### Components

#### RT-CMP-host-model
Label: Enclosing host compiler model

The Skill depends on a host model interpreting natural-language task and design instructions. Representational form: distributed-parametric inference component; instructions/input/output are separate natural-language or symbolic material. Storage substrate: host/provider model state, inaccessible in SRC-1. Parameters changing during operation: uninspected; the repository does not implement this inference service. Exact model version pinned: no host-model version is specified in the inspected Skill/agent metadata. Mutable endpoint resolving to another model: uninspected because no provider endpoint is configured there. This is not the proposed world-model encoder. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`.

> default_prompt: "Use $jepa-anything-skill to convert my world-model task into a validated JEPA Anything design and code skeleton."
> --- `jepa-anything-skill/agents/openai.yaml`

#### RT-CMP-orthogonal-factor-projection
Label: OrthogonalFactorProjection numerical component

Source-native identity: `OrthogonalFactorProjection`. Representational form: distributed-parametric basis when learnable, numerical fixed basis otherwise. Storage substrate: PyTorch `nn.Parameter` or registered tensor buffer in process. Parameters can change through external optimization and explicit retraction when learnable; fixed mode has no trainable basis parameter. Source code is pinned but actual tensor values, supplied encoder weights and any downstream checkpoint version are not pinned by this report. A remote mutable model endpoint is inapplicable to this local tensor module. Baseline target encoders separately expose EMA updates from online encoders; there is no basis for calling the entire numerical system immutable. SRC-1: `jepa-anything-core/src/jepa_anything_core/opf.py`, `jepa-anything-core/src/jepa_anything_core/baselines.py`.

> self.raw_basis = nn.Parameter(basis.detach().clone())
> --- `jepa-anything-core/src/jepa_anything_core/opf.py`

> self.register_buffer("fixed_basis", basis.detach().clone())
> --- `jepa-anything-core/src/jepa_anything_core/opf.py`

### Operative objects

#### RT-OBJ-design-protocol
Label: Task-design guidance

Source-native identity: Skill and `references/design-protocol.md` plus conversion/configuration references. Representational form: natural-language design rules with formal equations and illustrative schema fragments. Storage substrate: shipped Markdown files delivered by an external host to its model. The content explains causal separation, analysis versus synthesis, losses, fair baselines and evidence planning. It is static methodology, not a trace-fed learned artifact. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/references/design-protocol.md`, `jepa-anything-skill/references/world-model-conversion.md`, `jepa-anything-skill/references/config-contract.md`.

> This concatenation is not itself a reconstruction of `z`. Complete state synthesis is
> --- `jepa-anything-skill/references/design-protocol.md`

#### RT-OBJ-design-config
Label: Design configuration and diagnostic report

Source-native identity: schema `2.0` design and validator report. Representational form: symbolic mappings/lists whose fields drive deterministic validation/rendering; free-text summary and compiler assumptions are natural-language parts interpreted by the host. Storage substrate: JSON or optional YAML file and in-process mappings; report JSON on stdout/optional file; generated copy at `config/design.json` or YAML. Material parts differ: the mapping is the candidate product, while diagnostic checks are feedback for repair, not a license to claim empirical support. SRC-1: `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/scripts/generate_scaffold.py`.

> "A valid design has complete declared controls and experiment coverage; "
> "it does not prove coordinate activity, semantics, model quality, or claim support."
> --- `jepa-anything-skill/scripts/validate_design.py`

#### RT-OBJ-scaffold-manifest
Label: Generated scaffold package

Source-native identity: scaffold files, `validation-report.json` and `scaffold-manifest.json`. Representational form: symbolic Python/configuration/manifest, with natural-language documentation and comments. Storage substrate: filesystem directory promoted from a temporary sibling. Generated constants specialize downstream adapters, audit interfaces and callback dispatch; protocols/stubs are not a trained model. The manifest records file names and `contains_training_loop: False`, not content integrity hashes or successful training. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`.

> This module defines observable obligations, not a model implementation or a
> training loop. Complete state synthesis is distinct from concatenating factor
> coordinates: it must apply the Moore-Penrose pseudoinverse of the stacked
> projector-transpose analysis map after a measured full-rank audit.
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`

### Routes

#### RT-RTE-task-compilation
Label: Host task compilation and repair

Endpoints/progression: user's task/project → host model reading guidance → causal boundary/configuration → validator diagnostics → requested repair → scaffold generation and user handoff. Owner: host agent; user provides problem and unresolved causal facts. Policy/form: natural-language instructions shape model proposals; symbolic checks decide declared validity, not scientific truth. Context/state are current task facts, candidate and diagnostic history; filesystem effects are executed by host tools. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/references/world-model-conversion.md`, `jepa-anything-skill/scripts/validate_design.py`.

- Immediate return: requested conversion map, design files, validation result, skeleton paths and unresolved assumptions.
- Later read-back: generated design may be read by generation and downstream developers; cross-session host reload policy is uninspected — it belongs to the enclosing runtime.
- Delegated visibility: inapplicable — this Skill specifies no worker delegation protocol.
- Selection predicate: implicit world-model/rollout intent or explicit Skill invocation; recover facts from supplied project before questioning the user.
- Invalidation or expiry: design errors require repair; no automatic expiry/version history specified by this workflow.
- Activation or effect: instructions request changed host choices; reliable model compliance is not established by delivery.
- Evidence limits: source-defined workflow only, with no supplied host trace.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Proposer: host model; deciding/veto contributions: deterministic validator vetoes declared errors on gated paths, host chooses revisions, user answers only causal blockers. No mandatory human field-by-field approval. Answer oracle: no expected correct task design supplied for open requests; validator supplies fixed constraint tests, not an empirical oracle. Operating mode: open task conversion with bounded diagnostic repair, not an experimental training curriculum. Trigger: user authorizes creation/adaptation. Proposed change: external design and generated capability interfaces; guidance prescribes causal separation and reversible JEPA defaults. Admission/rejection: validity gate and destination checks on the generator CLI. Recovery: revise configuration and retry; no retained previous-version mechanism is required. What persists: proposed configuration, assumptions, report and skeleton, not a revised Skill method.

Theory account: the guidance presents an inspectable mathematical/design account; the requested loop derives a task-specific proposal under it. Diagnostics criticize declared contract violations, not necessarily the truth of the general methodology. theory-builder conditions 1–4: (1) afforded — localized method statements and equations are present; (2) claimed — host decisions are instructed to depend on their content, with actual consumption unobserved; (3) claimed — the host is told to correct errors identified by code/path/message, but observed attribution of blame and revision are not supplied; (4) claimed — repeated validation after repair is requested, not observed. Addressability: sections and configuration paths expose separable parts. Persistence: method files span sessions as shipped guidance; generated assumptions persist in the product, with later host reuse uninspected. learning: improved future capacity is unestablished; design iteration alone is insufficient. Reflection: the represented subject is the external task, not an evidenced feedback-controlled representation of this compiler's own operation. Reflective theory builder: unestablished because method revision against its own run records is not shown. Autonomous theory builder: host-computed proposal/repair is requested, but every internal operation including criticism is not evidenced as exercised. No exercised self-improvement is attributed: external product modification is not by itself modification of the compiler's behavioral organization.

> Write the proposed configuration, run the deterministic validator, and correct every design error:
> --- `jepa-anything-skill/SKILL.md`

#### RT-RTE-scaffold-admission
Label: Deterministic scaffold admission

Endpoints: configuration path → loader → `validate_config` → generator CLI gate → renderer → destination plus stdout manifest. Owner: Python CLI; caller selects input, format and output directory. JSON parsing or YAML safe loading produces data; fixed templates and `_python_repr` produce files rather than evaluating config expressions. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/scripts/validate_design.py`.

- Immediate return: JSON generated/file list and exit 0, invalid-design report/exit 1, or handled error/exit 2.
- Later read-back: configuration, validation report and generated modules are persisted for subsequent contract tests and downstream use.
- Delegated visibility: inapplicable — no remote/sub-agent work is dispatched.
- Selection predicate: CLI accepts only report-valid input; renderer separately requires a declared format and missing/empty destination.
- Invalidation or expiry: no time expiry or automatic regeneration; subsequent edits are caller responsibility.
- Activation or effect: filesystem package creation is wired; actual creation in a supplied run is unobserved.
- Evidence limits: direct rendering API can bypass validation; destination checks do not establish concurrent-writer safety or OS sandboxing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles/mode: host/human caller proposes the mapping; code decides via declared constraints; user approval is not required by the function. Answer oracle: fixed schema/rule predicates, not correct scientific predictions. Trigger: explicit invocation. Proposed change: new package, configuration and reports. Rejection: failed validity, unsupported format, nonempty destination or rendering error. Recovery: remove temporary tree on exceptions and retry; no general rollback of an installed package. Guidance: static templates and design contract shape the product; persisted content is exactly the rendered package/report/config, not an update to validator source. Guarantee strength: invariant for the CLI validity gate, not all callers.

> report = validate_config(raw)
> if not report["valid"]:
>     sys.stdout.write(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
>     return 1
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

> _ensure_destination_available(destination)
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

#### RT-RTE-state-consumption
Label: Generated state consumption

Endpoints: caller's state and `extras` mapping → mode dispatch → supplied callback(s) → callback result or selected horizon states. Owner: synchronous generated Python dispatcher; caller supplies state and executable callbacks. State representations are backend-defined, potentially numerical; the generated policy is symbolic constants. SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

- Immediate return: single readout result, single analysis result, or horizon-to-state mapping after repeated transitions.
- Later read-back: inapplicable — dispatcher itself retains no cross-invocation artifact; callback persistence is external and uninspected.
- Delegated visibility: callbacks receive state and mode-specific task/metric/probe/intervention or step/exogenous arguments; this is local call visibility, not worker delegation.
- Selection predicate: exactly the generated `USAGE_MODE`; repeated transition selects ascending steps through maximum horizon and retains declared horizons.
- Invalidation or expiry: local working state lasts the call; selected outputs escape to caller; no eviction/reload mechanism.
- Activation or effect: direct callback calls are wired; effect boundary is arbitrary callback code, without sandbox or transaction wrapper.
- Evidence limits: callback implementations, real models and actual observed behavior are not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision policy: terminal readout and factor analysis each call once; repeated transition calls once per step, requires callable transition and, when configured, each exogenous input. Caller owns recovery after errors. No product admission or theory revision occurs inside this dispatcher. Fixed modes do not validate the truth of a callback's result.

> current = transition(current, step=step, exogenous=exogenous)
> if step in horizons:
>     selected[step] = current
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`

#### RT-RTE-core-projection
Label: Core projection and explicit updates

Endpoints: caller constructs OPF tensor module → decomposition/pseudoinverse composition; external optimization may change learnable basis → optional scheduled QR retraction. Baseline callers can separately request EMA target updates. Owner: local Python/PyTorch functions; optimizer/EMA/hook scheduling belongs to caller. Context is tensors and explicit dimensions/modes/step counters, not agent dialogue. SRC-1: `jepa-anything-core/src/jepa_anything_core/opf.py`, `jepa-anything-core/src/jepa_anything_core/baselines.py`.

- Immediate return: numerical states/factors, or boolean indicating whether retraction ran; baseline updater mutates target parameters.
- Later read-back: subsequent module calls consume current parameter/buffer values; durable checkpoint save/reload is not established by this inspected path.
- Delegated visibility: inapplicable — no delegated model/worker context is created.
- Selection predicate: dimensions validate at construction; learnable/fixed and orthogonality mode select behavior; step modulus selects explicit retraction.
- Invalidation or expiry: mutations replace tensor values in process; invalid constructor inputs raise; numerical geometry after external optimization requires audits.
- Activation or effect: parameter updates and retraction are implemented affordances, not evidence of a training run or improved prediction.
- Evidence limits: no supplied weights/training trace, downstream optimizer or domain evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Change admission: caller decides to optimize or call hooks, code checks mode/step and shapes; no model or human quality judge selects a successor here. Proposed change is tensor state, guided by numerical update rules; persisted horizon is module lifetime unless caller saves it. Answer oracle: none for model quality; validity/geometry predicates only. Operating mode: reusable numerical computation, not autonomous optimization. Recovery: exceptions for invalid requests; retraction does not rewrite optimizer state. This is parameter mutability, not evidence of learning, reflection or compiler self-improvement.

> if self.orthogonality_mode != "qr_retraction":
>     return False
> if step % self.qr_retraction_frequency != 0:
>     return False
> self.retract_orthogonal_()
> return True
> --- `jepa-anything-core/src/jepa_anything_core/opf.py`

#### RT-RTE-structural-checks
Label: Structural recipe and provenance checks

Endpoints: recipe plus expected design → fixed audits and seeded oracle-state activity calculation → JSON report; separately checkpoint manifest plus local referenced files → consistency/hash checks → report. Owner: deterministic drivers, selected by caller or Make/CI. These are distinct consumers grouped here only as non-admitting repository checks; neither changes or installs a trained model. SRC-1: `recipes/synthetic-linear-dynamics/run_recipe.py`, `checkpoints/verify_manifest.py`, `Makefile`.

- Immediate return: pass/fail report and status; optional JSON output file.
- Later read-back: report can be retained at caller-selected path; this driver supplies no later agent reload or update policy.
- Delegated visibility: inapplicable — local checks do not delegate inference.
- Selection predicate: caller-selected/default recipe, expected design and manifest paths; manifest availability selects unpublished metadata versus local published-artifact checks.
- Invalidation or expiry: rerun on changed inputs; reports record recipe/design hashes but do not automatically expire themselves.
- Activation or effect: fixed assertions produce reports; synthetic activity is computed from source-system states, not learned encoders.
- Evidence limits: audit internals were sampled rather than exhaustively reviewed; no run/pass or real model result is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code compares declared fields and calculated fixture values; caller may use failure to revise files, but drivers do not automatically select/install successors. Answer oracle: supplied synthetic dynamics/recipe and expected design provide a bounded fixture reference, not an oracle for open user-task designs or trained performance. Operating mode: bounded synthetic structural checking plus metadata integrity checking. Improvement trigger/admission: these checks can return nonzero to `make check`; repository source-change approval/merge decisions remain uninspected. The optional report write admits diagnostics only, not capability changes. SRC-1: `Makefile`.

> "training_executed": False,
> "checkpoint_produced": False,
> "scientific_result": False,
> "learned_factor_activity_measured": False,
> --- `recipes/synthetic-linear-dynamics/run_recipe.py`

> "evidence_scope": "Integrity and publication-boundary verification only; no model result is evaluated.",
> --- `checkpoints/verify_manifest.py`

### Claims

#### RT-CLM-validation-scope
Label: Validation is declared completeness, not scientific support

The validator's claimed operation is deterministic internal-completeness checking. Its report itself separates declared experiment coverage from measured activity/model quality/support. The implementation checks top-level structure, identity, naming, leakage declarations, state/losses, use mode, baselines, audits, claim coverage and outputs. That establishes the gate's intended decision basis, not truth of declarations. Direct render calls and downstream callback execution are outside its enforcement point. SRC-1: `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/scripts/generate_scaffold.py`.

> "disclaimer": (
>     "A valid design has complete declared controls and experiment coverage; "
>     "it does not prove coordinate activity, semantics, model quality, or claim support."
> ),
> --- `jepa-anything-skill/scripts/validate_design.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Skill guidance to host decisions

Consumer: enclosing host compiler model. Channel: supplied/discovered Skill plus requested reference reads. Force: natural-language instruction/policy, not Python enforcement; the separate validator gate constrains only its covered tools. Horizon: current conversion and later invocations if host reloads the shipped files; no observed reload trace. The agent metadata permits implicit invocation but does not prove activation. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`.

> allow_implicit_invocation: true
> --- `jepa-anything-skill/agents/openai.yaml`

#### RT-BAP-generated-contract
Label: Generated contracts to downstream calls

Consumer: generated adapters/audits/dispatcher and callers importing their constants. Channel: literal Python constants and function calls rendered from the configuration. Force: fixed branches, checks and exceptions when those functions are invoked; independent callback/model code can bypass these checks. Horizon: package lifetime and subsequent imports/calls until edited/replaced. Actual downstream adoption remains unobserved. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/model.py.tmpl`.

> if USAGE_MODE == "terminal_readout":
>     readout = _require_callable(supplied, "readout")
> --- `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`

## Annotations

none
