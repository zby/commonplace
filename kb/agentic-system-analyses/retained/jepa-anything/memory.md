---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "JEPA-Anything memory: persisted design contracts, bounded numerical history and externally owned host context."
run-id: AAS-2026-10-15-jepa-anything-434b01ab7774-01
source-identity: "https://github.com/Gen-Verse/JEPA-Anything"
reviewed-boundary: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
---

# JEPA-Anything memory report

## Boundary and evidence

The memory boundary follows the builder's task compilation, configuration validation and rendering, generated consumers, numerical support operations, and structural/provenance evaluators. It includes both persisted products and numerical history that influences subsequent calls. It does not recast all tensor computation as agent memory. Static Skill/reference files are working-context inputs, not material accumulated through use. Ordinary rollout state is current-call state, not a cross-invocation memory service. The enclosing host's inference history, context budget, compaction and session reload remain outside the implementation supplied here. See [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation), [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption) and [boundary](boundary.md).

All new source inspection uses SRC-1 at c6e6c88f3ef75a4ce7acd660d6fa5779d995512c. HEAD matched that revision and `git status --short` returned no changes. Evidence layers are implementation and doctrine/design; no execution evidence was supplied or produced. The table distinguishes direct reads from supplied runtime evidence. Listed paths are commit-relative SRC-1 anchors, not new source declarations.

| Entry or operation | Paths and inspection | Coverage and limits |
|---|---|---|
| Skill invocation, requested project/reference reads and repair | Direct: `jepa-anything-skill/SKILL.md`; supplied: `jepa-anything-skill/agents/openai.yaml`, reference documents | [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation), [RT-OBJ-design-protocol](runtime.md#rt-obj-design-protocol), [MEM-OBJ-compiler-assumptions](#mem-obj-compiler-assumptions). No host context scheduler or observed reference loading established. |
| Standalone validator CLI/API and diagnostic persistence | Direct report, loader and CLI: `jepa-anything-skill/scripts/validate_design.py`; supplied validation branches | [RT-OBJ-design-config](runtime.md#rt-obj-design-config). Both valid and invalid reports can be written; exhaustive schema audit not attempted. |
| Generator CLI and direct Python renderer | Direct complete: `jepa-anything-skill/scripts/generate_scaffold.py` | [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission). Direct API does not repeat CLI validity admission. |
| Generated import, test and use consumers | Direct: `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`, test template imports/static and claim checks; supplied adapter/model/evaluation/capacity contracts | [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest), [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract). Persistent code is consumed; callbacks and real backend adoption remain unobserved. |
| Numerical basis and QR hooks | Supplied: `jepa-anything-core/src/jepa_anything_core/opf.py` | [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection), [RT-RTE-core-projection](runtime.md#rt-rte-core-projection). No independent exhaustive OPF inspection here. |
| Public streaming monitor, update/read/reset and wrapper | Direct tracker/monitor implementation: `jepa-anything-core/src/jepa_anything_core/losses.py`; direct guide section and public-export search; test-name search only | [MEM-OBJ-online-variance-tracker](#mem-obj-online-variance-tracker), [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor). Additional retained history beyond runtime's basis account. |
| Baseline target initialization, EMA and later encoding | Direct lifecycle: `jepa-anything-core/src/jepa_anything_core/baselines.py` | [MEM-CMP-target-encoder](#mem-cmp-target-encoder); annotation on [RT-RTE-core-projection](runtime.md#rt-rte-core-projection). Initial encoder provenance and external optimizer inputs unresolved. |
| Recipe diagnostics and source hashes | Direct report/CLI: `recipes/synthetic-linear-dynamics/run_recipe.py`; supplied audit account | [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks). Not an exhaustive audit of synthetic calculations; no later automated report consumer established. |
| Checkpoint metadata, unpublished/published alternatives and local integrity verification | Direct complete: `checkpoints/README.md`, `checkpoints/manifest.json`, `checkpoints/verify_manifest.py` | [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest). Future artifact bytes are opaque/unpublished, not a hidden inspected checkpoint; verifier does not deserialize weights. |
| Repository check dispatch | Supplied: `Makefile`, `.github/workflows/ci.yml` | [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks). No executed CI, model-provider tools, hooks or remote service consumer established. |

No material memory responsibility in these routes is deliberately excluded. Source images, legal metadata and packaging details do not establish a retention consumer and were not independently reviewed here. Missing domain implementations, host/session machinery, actual saved checkpoints and run traces prevent claims about deployed reload, user/model compliance, improved capacity or actual learned results, not the implemented numerical-history mechanism below.

## Core ideas

1. **The main durable output is a design-dependent program, not an experience store.** A configuration is copied into a generated package while selected fields become literal constants in fixed Python templates. Later imports and function calls apply those constants. Admission differs between the CLI and direct renderer, and file editing can change the result after generation. The source-defined consumers establish a route for retained products, not deployed adoption. [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission), [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract).
2. **The numerical core has genuine bounded history.** Welford statistics accumulate factor samples and affect a later monitor invocation. Their compact numeric form loses sample identities and reasons. EMA similarly carries prior online-encoder state into later target encoding. These are not a retrieval index, a dialogue summary or evidence of improving the compiler. [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor), [MEM-CMP-target-encoder](#mem-cmp-target-encoder).
3. **Reports and provenance are not the thing they describe.** Diagnostics preserve rule results; the checkpoint manifest preserves planned lineage and availability. Neither contains a trained model, and integrity verification does not assess prediction quality. The published-artifact branch verifies caller-staged bytes, not an automatic fetch/load route. [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope), [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest).
4. **Context management is mostly an external responsibility.** The Skill requests particular reference reads and project inspection, but supplies neither token-budget selection nor isolated worker frames, trimming or host compaction. No conclusion about the enclosing host's mechanisms follows. Guidance delivery is not observed compliance. [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).

## Shared records

### Components

#### MEM-CMP-target-encoder
Label: Baseline target encoder

Source-native identity: `_BaseJEPABaseline.target_encoder`. Representational form: distributed-parametric encoder, with possible symbolic/non-floating buffers depending on the supplied module. Storage substrate: local PyTorch module parameters and buffers. Initialization is a caller-supplied target module or a deep copy of the context encoder. The supplied encoder's original training/data provenance is uninspected. Target parameters are frozen against gradients, but an explicit update changes them by EMA; floating/complex buffers are averaged and other buffers copied. Exact parameter values/model version are not pinned; no remote endpoint is involved in this local component. The code version alone does not pin weights. SRC-1: `jepa-anything-core/src/jepa_anything_core/baselines.py`.

Distinct identity: the target encoder is not the projection basis in [RT-CMP-orthogonal-factor-projection](runtime.md#rt-cmp-orthogonal-factor-projection) or the enclosing compiler in [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Its update/consumer path is already included in [RT-RTE-core-projection](runtime.md#rt-rte-core-projection); this component adds its separate storage, lineage and mutability, not a duplicate route.

> self.target_encoder = (
>     copy.deepcopy(context_encoder) if target_encoder is None else target_encoder
> )
> --- `jepa-anything-core/src/jepa_anything_core/baselines.py`

> target_parameter.mul_(momentum).add_(online_parameter, alpha=1.0 - momentum)
> --- `jepa-anything-core/src/jepa_anything_core/baselines.py`

> with torch.no_grad():
>     target_state = self.target_encoder(target_observation)
> return context_state, target_state.detach()
> --- `jepa-anything-core/src/jepa_anything_core/baselines.py`

### Operative objects

#### MEM-OBJ-online-variance-tracker
Label: OnlineVarianceTracker sufficient statistics

Source-native identity: `OnlineVarianceTracker` buffers `count`, `mean`, `m2`. Representational form: numerical sufficient statistics with localized fixed Welford consumer rules, rather than prose or learned encoder weights. Storage substrate: PyTorch registered buffers, int64 count and floating mean/M2 maintained at least at float32. Lineage: zero initialization followed by caller-provided factor batches; no sample-origin identity is retained. The buffers represent derived historical statistics, not the raw batches. `reset` removes all history. The public guide exposes a `state_dict()` checkpoint mapping, but no on-disk save/reload consumer is established by that example. A state mapping is not the metadata-only publication manifest.

No counterpart was found among supplied operative objects: [RT-OBJ-design-config](runtime.md#rt-obj-design-config) and [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) concern compiler products, not running factor statistics. The closest numerical route is [RT-RTE-core-projection](runtime.md#rt-rte-core-projection), which does not describe this monitor. SRC-1: `jepa-anything-core/src/jepa_anything_core/losses.py`, `jepa-anything-core/README.md`.

> self.register_buffer("count", torch.zeros((), dtype=torch.int64, device=device))
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> self.mean.copy_(mean_for_storage)
> self.m2.copy_(m2_for_storage)
> self.count.fill_(int(total_count))
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> checkpoint = variance_monitor.state_dict()  # count, mean, and M2 are preserved
> --- `jepa-anything-core/README.md`

#### MEM-OBJ-compiler-assumptions
Label: Compiler assumptions in task metadata

Part of: [RT-OBJ-design-config](runtime.md#rt-obj-design-config)

Source-native identity: `task.metadata.compiler_assumptions`. Representational form: natural-language source-task summary and provisional choices inside a symbolic configuration. Storage substrate: authored config mapping/file, copied into generated `config/design.json` or YAML. Lineage: the host is instructed to extract task facts and record reversible defaults. This is requested authorship, not an observed summary or an automatic transcript-to-memory transformation. It is distinct from diagnostic checks, which test the declared contract. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/scripts/generate_scaffold.py`.

> Propose reversible defaults for JEPA design choices and record them under `task.metadata.compiler_assumptions`; never make the user design JEPA for you.
> --- `jepa-anything-skill/SKILL.md`

This passage is a substring of the Skill's step 2 instruction, not a claim of compliance. The renderer serializes the whole mapping, preserving assumptions if supplied. Its `_template_values` does not select this metadata into generated executable constants. Thus reasons can remain inspectable in the copied configuration, but this source establishes no subsequent model reload or deterministic decision using the assumptions' meaning.

#### MEM-OBJ-checkpoint-manifest
Label: Checkpoint publication manifest

Source-native identity: `checkpoints/manifest.json`, schema `jepa-anything.checkpoint-manifest/v1`. Representational form: symbolic availability, source hashes, file descriptors and training/claims metadata, with natural-language provenance/evidence limits. Storage substrate: maintained repository JSON; no binary model payload in its current entry. Lineage names repository maintainers and exact recipe/design/schema hashes, while `provenance.repository_commit` is null. This is access/provenance metadata, not the encoded checkpoint or a display summary proving its contents. The planned synthetic fixture has no files, immutable URI or executed training. SRC-1: `checkpoints/manifest.json`, `checkpoints/README.md`.

Distinct identity: this is verifier input, not the generated file list in [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest) or a product of [RT-OBJ-design-config](runtime.md#rt-obj-design-config). Its consumer is the verifier within [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks). File hash verification establishes integrity relative to supplied metadata, not authenticity of training claims or scientific quality. The guide requires future consumers to verify before loading; this is a documented role, not a wired loader.

> The current entry has `availability: "not_published"`, an empty `files` list,
> and `training.executed: false`. It is a provenance record for a planned fixture,
> not a downloadable checkpoint and not evidence of a result.
> --- `checkpoints/README.md`

> Each `files[].path` is resolved beneath a caller-supplied local artifact root;
> paths that escape that root are rejected.
> --- `checkpoints/README.md`

Verifier admission is numerical/structural software checking, not an artifact-publication decision. Maintainers can edit the metadata; this source does not implement their review/approval process. The verifier checks source hashes and publication consistency, and for published records checks caller-staged file sizes and hashes under a root. Rejection produces failed checks/nonzero status, not deletion, revoked loading authority or rollback of earlier external loads. No raw traces are transformed into this manifest, and no later agent-context supply is shown. SRC-1: `checkpoints/verify_manifest.py`.

### Routes

#### MEM-RTE-streaming-monitor
Label: Streaming factor monitoring

Endpoints/progression: caller factor batch → `OnlineVarianceTracker.combined_variance` merging current samples with retained count/mean/M2 → standard-deviation hinge loss → optional tracker update → subsequent monitor call. Owner: local core function or `OnlineVarianceLoss` wrapper; caller supplies samples and mode. Context/state are factor coordinates and numerical summaries, not host dialogue. Distinct from [RT-RTE-core-projection](runtime.md#rt-rte-core-projection): this updates sufficient statistics used by a loss, not basis geometry. SRC-1: `jepa-anything-core/src/jepa_anything_core/losses.py`.

- Immediate return: reduced activity penalty; optional mutation of historical buffers.
- Later read-back: subsequent monitor calls consume all accumulated sufficient statistics through `combined_variance`; `variance` can also read current statistics. Checkpoint mapping is afforded, but durable save/reload deployment is uninspected.
- Delegated visibility: inapplicable — no worker or remote inference context is involved.
- Selection predicate: caller chooses tracker and factor batches; function `update` defaults true, while wrapper defaults to its training flag. Consumer combines every accumulated sample statistically, with no semantic retrieval or top-k selector.
- Invalidation or expiry: `reset` zeros count, mean and M2; no age-based expiry, per-sample deletion or retained sample IDs are implemented by this tracker.
- Activation or effect: retained numeric history enters the next penalty calculation. Gradients reach the current batch while history remains detached; an optimizer using the returned loss is external and unobserved.
- Evidence limits: supplied sample provenance, monitor callers in an actual training run, saved bytes and observed benefit are uninspected. This does not establish compiler learning or autonomous training.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Write admission: caller selects inputs/update flag, then code rejects wrong dimensions/device, nonfinite samples, count overflow and nonfinite stored statistics before copying buffers. There is no quality judge or expected correct prediction oracle; numerical preconditions are the gate. Generic caller identity does not establish human approval of each batch. The proposed change is replacing sufficient statistics under fixed Welford rules; initialization and reset are explicit code operations. Rejection preserves pre-update statistics for the checked failure cases; successful updates have no per-batch undo. This is an automatic data-fed state transformation once invoked, not a raw agent-execution-trace learning route. The loss may shape an external optimizer but has no training loop itself.

> coordinate_variance = tracker.combined_variance(factors)
> standard_deviation = torch.sqrt(coordinate_variance + eps)
> penalties = torch.relu(min_std - standard_deviation)
> loss = _reduce(penalties, reduction)
> if update:
>     tracker.update(factors)
> return loss
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> should_update = self.training if update is None else update
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

> old_mean = self.mean.detach().clone().to(dtype=samples.dtype)
> old_m2 = self.m2.detach().clone().to(dtype=samples.dtype)
> old_count = int(self.count.item())
> --- `jepa-anything-core/src/jepa_anything_core/losses.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-design-protocol](runtime.md#rt-obj-design-protocol)

Memory-specific limit: shipped guidance is static rather than trace-derived. The Skill requests conversion-reference, design-protocol and config-contract reads in that order of workflow use. No numeric context budget, tail retention, context-window isolation or removed-content reload procedure is specified in the inspected Skill. That bounds the finding to target-owned context instructions, not the host's capabilities. SRC-1: `jepa-anything-skill/SKILL.md`.

#### On [RT-OBJ-design-config](runtime.md#rt-obj-design-config)

The config copy and diagnostic report have different consumers. The generator loads current config data and validates it afresh; it does not admit a design by loading an older report. Standalone validator `--output` writes diagnostics even for invalid designs; the return code separately reports validity. Report `checks` and summary counts are derived rule feedback, not retained raw task conversation or measured training evidence. The Skill requests host repair from diagnostics but supplies no cross-session reload selector. SRC-1: `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/SKILL.md`.

> if args.output is not None:
>     args.output.parent.mkdir(parents=True, exist_ok=True)
>     args.output.write_text(rendered, encoding="utf-8")
> --- `jepa-anything-skill/scripts/validate_design.py`

#### On [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest)

The container has materially distinct persisted parts: complete normalized design copy, validator feedback, file-list manifest and generated program/documentation. `_write_config` serializes the whole config; `_template_values` selects contract fields for literal Python substitution. This is a deterministic transformation of a product, not a trace summarizer. Consumer authority differs: generated Python constants select execution/check branches, while the copied report and file list are inspectable outputs with no automatic import-driven admission role shown. Supplied runtime already identifies these parts; this annotation does not allocate duplicate objects. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`.

> rendered = json.dumps(config, indent=2, ensure_ascii=False) + "\n"
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

> output.write_text(_render_template(text, values, template), encoding="utf-8")
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

#### On [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission)

Read-back is caller-requested by config path, not an unsolicited push or a content-relevance query. All selected executable fields come from the current config; there is no context/token budget. Host-model authorship is requested, but a human can edit the file or call the tools directly. Starting the Skill is not per-field approval. CLI validity and destination checks are software admission; direct renderer admission only covers declared format and destination availability, as the supplied route already states. Temporary files are deleted on exceptions; successful products have no automatic expiry, withdrawal propagation or rollback. Manual editing after creation can diverge code from its stored report/config. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`.

> except Exception:
>     shutil.rmtree(temp_path, ignore_errors=True)
>     raise
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

#### On [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract)

The concrete later consumers are generated test/module imports and function invocations. The tests import persisted constants and invoke static/claim checks; usage dispatch reads the configured mode and details. Callback inputs and output values remain caller-supplied, not trustworthy merely because the package passed a declaration check. Activity audits accept arrays of supplied measurements and check numeric floors; they do not authenticate their empirical origin or retain accepted/rejected arrays. SRC-1: `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/activity.py.tmpl`.

> def test_static_contract(self) -> None:
>     assert_contract()
> --- `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`

#### On [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption)

Repeated transitions retain selected horizon states only in the return mapping of the current call. Selection is numeric horizon membership, not retrieval from accumulated experience. There is no copy at insertion, so independent immutable snapshots are not guaranteed if callbacks mutate and return the same object. No cross-invocation persistence is implemented in this dispatcher. Its exogenous availability checks concern world-model causal inputs, not the enclosing language model's context-window management. SRC-1: `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`; the supplied record retains the decisive assignment passage.

#### On [RT-RTE-core-projection](runtime.md#rt-rte-core-projection)

The supplied basis route also mentions EMA, whose distinct consumer is clarified by [MEM-CMP-target-encoder](#mem-cmp-target-encoder). Caller-triggered EMA merges online parameters into target parameters; later `_encode` uses the resulting target module for target observations under no-grad. No parameter-quality admission or human candidate approval occurs within that update. Code checks momentum and matching parameter/buffer structures, dimensions, dtype, device and direct tensor sharing before mutation. Initial module content and external optimizer inputs remain unresolved, independently of the known subsequent numerical transformation. Persistence is module lifetime; no durable checkpoint writer is established here. Update control and downstream encoding control are distinct from the host compiler's instruction authority. SRC-1: `jepa-anything-core/src/jepa_anything_core/baselines.py`.

> def update_target_encoder(self, momentum: float | None = None) -> None:
>     """EMA-update the target encoder; call once after each optimizer step."""
> --- `jepa-anything-core/src/jepa_anything_core/baselines.py`

#### On [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks)

The recipe report retains exact input hashes, per-check results and an evidence envelope; `--output` serializes both pass and fail reports. The checkpoint verifier likewise optionally retains its result. Those writes preserve derived diagnostics, not a new trained state or a source change. The caller may inspect them; no automatic agent-method update, report replay or successor installation is wired by the inspected report/CLI code. Make/CI consumes status under the supplied runtime account. Neither report writer supplies a human content-approval requirement; caller identity and later manual use are unspecified. SRC-1: `recipes/synthetic-linear-dynamics/run_recipe.py`, `checkpoints/verify_manifest.py`.

> "allowed_interpretation": (
>     "Structural smoke audit of a synthetic fixture; activity values "
>     "come from oracle state coordinates, not a learned model."
> ),
> --- `recipes/synthetic-linear-dynamics/run_recipe.py`

## Write side

The host is instructed to author a task design and retain provisional assumptions, then repair design errors. Its criticism-to-product path is the requested workflow in [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation), not an implemented host memory controller. No execution trace is converted automatically into revised Skill instructions. The persisted reasons have a bounded location in [MEM-OBJ-compiler-assumptions](#mem-obj-compiler-assumptions); retention does not establish a later reader of their meaning.

Validator reports can persist rejection feedback without admitting a product. The generator CLI instead rejects invalid input before rendering; rendering writes a complete package in a temporary sibling and promotes it only after completing its output set. Direct calls and later manual edits are counterexamples to treating the report as enduring certification. No per-content human approval follows from the generic caller role. There is no generated-artifact deletion/revocation propagation in this path. See annotations on [RT-OBJ-design-config](runtime.md#rt-obj-design-config) and [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).

Numerical writes have separate control. [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor) turns batches into count/mean/M2 and reads them at later calls; reset withdraws all their contribution, not individual records. [MEM-CMP-target-encoder](#mem-cmp-target-encoder) retains a numerical mixture of encoder states, without explicit historical reasons or a sample log. Externally optimized basis mutation and scheduled QR retraction remain as supplied in [RT-RTE-core-projection](runtime.md#rt-rte-core-projection). None establishes an automatic host execution-trace-to-instruction update, and no beneficial learning is inferred from persistence alone.

## Read-back

- **Persisted design → renderer:** explicit caller config path selects a whole JSON/YAML mapping; load/validation/render consume it. No relevance ranking or token budget applies. The actual later authority is template specialization and generated fixed checks, not permission to execute arbitrary text in config. See [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).
- **Generated package → tests/developer calls:** module imports deliver literal constants; checks and dispatch use them when invoked. Copied free-text assumptions, report and manifest do not automatically become host context. The repository requests contract tests; their successful execution is unobserved. See [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract).
- **Historical factor samples → later monitor:** derived sufficient statistics, not raw batches, enter `combined_variance`; all accumulated history contributes numerically, with no per-sample targeting or reason recovery. Module lifetime is wired; exported `state_dict` is documented, but storage export alone does not establish a later on-disk reload caller. See [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor).
- **EMA target → subsequent encoder call:** target state is automatically used by `_encode` after a caller invokes an update; the external scheduler and original training provenance remain uninspected. See [MEM-CMP-target-encoder](#mem-cmp-target-encoder).
- **Checkpoint provenance → integrity checker:** caller/default manifest path and artifact root select records and exact bytes. A future published entry causes size/hash checks on local files; it does not deserialize, download, install or activate them. The current entry is unpublished. See [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest).
- **Reports → later agent:** optional persistence is implemented, but the inspected report writers do not establish an automatic later agent consumer. Manual reading is possible; it is not a demonstrated reload policy. See [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks).

No unsolicited retained-memory push to host inference is established by these paths. Skill/reference selection is static instruction delivery, and user-task/project inspection is requested host work. Its foreground caller chooses what files to inspect; neither a preferential eviction order nor what would survive host compaction can be determined from SRC-1. The classical isolated-frame analogy does not describe a target-owned mechanism here: callbacks pass ordinary Python values, not isolated model windows; no popped worker frame or escaping summary is implemented by those functions.

## Integration issues

1. **Additional operative history, not a correction:** [MEM-OBJ-online-variance-tracker](#mem-obj-online-variance-tracker) and [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor) add a public numerical-history surface absent from the supplied route inventory. The runtime's direct-core scope includes it, but projection/EMA alone do not exhaust numerical retention. Evidence is SRC-1 `jepa-anything-core/src/jepa_anything_core/losses.py` and the guide. Consequence: a system-wide claim of no retained state would be wrong, even though agent-session memory remains host-owned.
2. **Containment and overlap:** [MEM-OBJ-compiler-assumptions](#mem-obj-compiler-assumptions) is explicitly part of [RT-OBJ-design-config](runtime.md#rt-obj-design-config), with a different natural-language consumer limit. [MEM-CMP-target-encoder](#mem-cmp-target-encoder) adds the component used by [RT-RTE-core-projection](runtime.md#rt-rte-core-projection), not a second projection component. [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest) is the input to the verifier portion of [RT-RTE-structural-checks](runtime.md#rt-rte-structural-checks), not the generated scaffold manifest. No possible duplicate referent remains after these comparisons.
3. **Unresolved original provenance and deployment:** caller encoders and monitor samples have no inspected original data/training lineage; subsequent EMA/Welford transformations are known. No actual host reload, durable numeric checkpoint reload, external optimizer use, callback persistence, training run or post-generation manual adoption is supplied. These limits affect [MEM-CMP-target-encoder](#mem-cmp-target-encoder), [MEM-RTE-streaming-monitor](#mem-rte-streaming-monitor) and [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption); they prevent learned-benefit/deployment conclusions without erasing the implementation positives.
4. **Published alternative is only integrity:** [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest) contains no current payload. A documented future consumer role can be named, but no actual weight-loading route follows from the verifier. Full schema-validation equivalence and authenticity of future training metadata are not established. SRC-1 `checkpoints/README.md`, `checkpoints/verify_manifest.py`.

No supported correction to a supplied factual claim is required. The issues above are additional coverage and bounded unknowns for reconciliation, not authority to revise another member.

## Limitations and checks

The report does not establish observed host behavior, automated cross-session knowledge reuse, empirical learning, successful training, benefit or self-improvement. The frozen implementation and requested workflow support narrower conclusions. Review specifically challenged the apparent no-memory boundary with numerical-history exports, and challenged universal validity/causal-safety interpretations with direct renderer calls, mutable callbacks and caller-supplied measurements. These checks preserve the runtime's qualifications rather than strengthen them.

Required job, member types, boundary/runtime inputs, collection, worker rules and records contract were read completely, recovering bounded continuations. Source and run identities were rechecked against supplied frontmatter and checkout HEAD. New source evidence stays within SRC-1; no target code/tests/examples or model providers were executed. An attempted scaffold README read returned ENOENT; actual template inventory was then used, without treating the missing guessed filename as an access gap or absence claim. Runtime and method-input trailing-range checks reached EOF.

Validation: the prescribed `commonplace-run validate-output` check was executed. Its initial result identified only the unfinished validation-status line; that line was corrected. The final correctly addressed invocation returned: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” One intervening mistyped-path call failed before checking content. This deterministic check establishes form and quotation occurrence, not semantic acceptance.
