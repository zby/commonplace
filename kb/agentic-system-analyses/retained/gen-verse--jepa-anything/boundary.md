---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "JEPA-Anything's model-assisted task-design builder and shipped support paths at commit c6e6c88f3ef75a4ce7acd660d6fa5779d995512c."
run-id: AAS-2026-10-15-jepa-anything-434b01ab7774-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/Gen-Verse/JEPA-Anything
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/jepa-anything-434b01ab7774/related-systems/Gen-Verse--JEPA-Anything
  revision: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
  sha256: null
---

# JEPA-Anything boundary

## Boundary and evidence

JEPA-Anything is in scope as a **builder or improvement plane**: its shipped agent Skill directs a host model to interpret a user's world-model task, propose a structured design, correct deterministic validation errors, and deliver configuration and a code skeleton. This is not an enclosing agent runtime and is not merely the tensor library. The model-dependent operation is the Skill's task-to-design compilation; the Python validator and renderer provide its deterministic support. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`, `docs/architecture.md`.

> Turn the user's existing world-model intent into a verifiable JEPA Anything world-state interface. The user supplies the domain task in their own language; do not require them to know JEPA, OPF, context-target terminology, or `d`, `K`, and `r`. Deliver configuration and inspectable interfaces, never a hidden training run.
> --- `jepa-anything-skill/SKILL.md`

> The LLM may fill this contract but cannot waive validator diagnostics.  A valid
> contract can be rendered into an implementation skeleton.  The renderer has no
> training loop side effect, network side effect, or checkpoint side effect.
> --- `docs/architecture.md`

The intended use is conversion of an ordinary world-model request or existing project into an inspectable implementation contract, not execution of a trained world model. The **whole-system** boundary includes the shipped Skill and reference instructions, agent-discovery metadata, design validator, scaffold generator and templates, numerical support library, structural recipe and expected design, checkpoint provenance checks, and repository evaluators. The shipped recipe driver and generated state consumer remain inside the boundary; neither is excluded as an external caller. SRC-1: `README.md`, `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/scripts/generate_scaffold.py`, `recipes/synthetic-linear-dynamics/run_recipe.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

Initial entry-point tracing establishes these paths:

- The Skill and agent metadata expose model-assisted compilation. Its three reference documents constrain causal inputs, proposed architecture and the design contract. The model is instructed to write a configuration, validate it, repair errors, generate the skeleton and run generated contract tests. This is a declared host workflow, not an observed invocation. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`, `jepa-anything-skill/references/world-model-conversion.md`, `jepa-anything-skill/references/design-protocol.md`, `jepa-anything-skill/references/config-contract.md`.
- The generator CLI loads the design through the validator, stops on invalid input, renders templates into a temporary directory, persists the normalized configuration, validation report and scaffold manifest, and replaces a missing or empty destination. Generated contract tests import the generated interfaces; the usage dispatcher invokes supplied readout, analysis or transition callbacks, including repeated transitions at configured horizons. These consumers are shipped responsibilities, although implementing a real domain model remains a downstream task. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/scripts/validate_design.py`, `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.
- The core supplies numerical primitives rather than the host model-call loop. Initial inspection includes its public guide, API/function inventory, and tensor decomposition/synthesis implementation. The structural recipe independently loads its recipe and expected design and can write a JSON audit report; checkpoint verification consumes provenance and publication metadata. Make and CI connect these checks to the repository's evaluators. SRC-1: `jepa-anything-core/README.md`, `jepa-anything-core/src/jepa_anything_core/opf.py`, `recipes/synthetic-linear-dynamics/run_recipe.py`, `checkpoints/verify_manifest.py`, `Makefile`, `.github/workflows/ci.yml`.

The generator's validity gate is explicit:

> raw = load_config(args.config)
> report = validate_config(raw)
> if not report["valid"]:
>     sys.stdout.write(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
>     return 1
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

### Top-level tracked coverage

The tracked tree was inspected at the frozen commit. “Included” establishes functional coverage for subsequent source inspection, not an assertion that every numerical routine or test was exhaustively reviewed during boundary declaration. No material shipped loop path is deliberately excluded. Ancillary files listed as inventoried are available, not access gaps. All rows refer to SRC-1.

| Top-level tracked path | Treatment and material paths | Role and present inspection limits |
|---|---|---|
| `.github/` | Included: `workflows/ci.yml`, read | CI installs development dependencies and calls `make check`; source evidence only, not evidence of a successful CI run. |
| `.gitignore` | Included, inventoried | Repository output hygiene; no behavioral finding based on its uninspected contents. |
| `CONTRIBUTING.md` | Included, inventoried | Contributor instructions available for later inspection; no contributor-process conclusion established here. |
| `LICENSE` | Included, inventoried | Licensing metadata; legal obligations not assessed here. |
| `Makefile` | Included, read | Connects core/Skill tests, design validation, structural recipe, metadata integrity, JSON and compilation checks. |
| `README.md` | Included, read | Project scope, user entry commands, and explicit research-evidence limits. |
| `README.zh-CN.md` | Included, inventoried | Alternate-language documentation available; no translation-equivalence conclusion established. |
| `assets/` | Included: `figures/framework-overview.png`, `figures/scenario-atlas.png`, inventoried | Research illustrations; image content not independently inspected or treated as results. |
| `checkpoints/` | Included: `README.md`, `manifest.json`, `manifest.schema.json`, `verify_manifest.py`, `.gitignore` | Read guide, manifest and verifier's main verification function; schema inventoried. Covers planned artifact provenance and local integrity checking, not trained-model performance. |
| `docs/` | Included: `architecture.md`, read | Component boundaries, model/compiler contract and downstream responsibilities. |
| `jepa-anything-core/` | Included: `src/jepa_anything_core/{__init__,opf,losses,baselines,audit}.py`, `py.typed`, `tests/test_{opf,losses,baselines,audit}.py`, `README.md`, `pyproject.toml`, `MANIFEST.in`, `LICENSE` | Numerical library, serialization/monitoring support and its evaluators. Guide read; executable function inventory searched and OPF decomposition/synthesis read. Other internals and test bodies remain available for analysis; no test-pass finding is made. |
| `jepa-anything-skill/` | Included: `SKILL.md`, `agents/openai.yaml`, all three `references/*.md`, `scripts/{validate_design,generate_scaffold}.py`, `assets/scaffold/`, `tests/` | Model instructions produce designs; deterministic gate admits designs; renderer persists configuration/reports/code; generated adapters, model protocols, activity/capacity/evaluation contracts and usage callbacks consume them. Skill, metadata, references, generator, validator dispatch, usage template and generated test template read; regression-test names searched. Remaining validator branches and template/test bodies are available, not excluded. |
| `pyproject.toml` | Included, section inventory searched | Root test/coverage configuration; not a model-serving entry point. Detailed settings remain available. |
| `recipes/` | Included: `README.md`, `.gitignore`, `synthetic-linear-dynamics/{README.md,recipe.json,design.expected.json,run_recipe.py}` | Shipped source task, expected compiler output and audit driver. Example guide and driver report/CLI path read; JSON inputs and audit internals remain available. Reports are structural evidence by contract, not learned-model results. |

### External responsibilities and evidence limits

The enclosing agent host supplies model inference, tool execution, workspace permissions and orchestration of the Skill instructions. Those responsibilities are not attributed to JEPA-Anything. The source supplies a Skill contract and discovery metadata, not a frozen trace of a host executing that contract. This prevents conclusions about actual host compliance, model-call reliability, latency or autonomous completion. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/agents/openai.yaml`, `docs/architecture.md`.

Python is required for the deterministic tools, PyTorch for the numerical core, and PyYAML for optional YAML handling. User task data, real adapter/encoder implementation, callback implementations, optimizer/EMA scheduling, training and scientific interpretation belong to downstream execution. These exclusions prevent conclusions about trained model quality, domain validity, or real planning/control performance; they do not remove the shipped scaffold, callback dispatcher or synthetic driver from inspection. SRC-1: `README.md`, `jepa-anything-core/README.md`, `jepa-anything-skill/scripts/generate_scaffold.py`, `jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl`.

> This repository contains the reusable core, task-design tools, and a synthetic structural example; it does not include the domain datasets or trained model weights depicted in the atlas.
> --- `README.md`

The manifest records a planned, unpublished fixture with no artifact files and no training. The paper and externally hosted models linked by the README are not frozen sources in this run; their exclusion prevents independent assessment of the broader research results. No execution trace or causal experiment is supplied, and no target code or tests were executed for this boundary. SRC-1: `checkpoints/manifest.json`, `README.md`, `recipes/synthetic-linear-dynamics/README.md`.

The frozen evidence is the acquired Git repository at **c6e6c88f3ef75a4ce7acd660d6fa5779d995512c**, with applicability cutoff **2026-10-15**. The checkout's HEAD matched this revision and its working tree was clean when inspected. The overall evidence tier is **code-grounded**; model instructions and design statements remain doctrine/design rather than observed operation. This boundary makes no claims about later repository revisions.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Gen-Verse/JEPA-Anything` | c6e6c88f3ef75a4ce7acd660d6fa5779d995512c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/jepa-anything-434b01ab7774/related-systems/Gen-Verse--JEPA-Anything`. Implementation: tracked-tree and API inventories; complete scaffold generator; validator dispatch; generated usage and contract-test templates; OPF decomposition/synthesis; recipe report and CLI; manifest verification function; Make/CI wiring. Doctrine/design: README, architecture, complete Skill and references, agent metadata, core guide, recipe guide, checkpoint guide and manifest. Remaining paths in the coverage table are available for subsequent inspection at this same pin. | Implementation: [generator](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/scripts/generate_scaffold.py), [validator](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/scripts/validate_design.py), [consumer](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/assets/scaffold/src/jepa_task/usage.py.tmpl), [recipe driver](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/recipes/synthetic-linear-dynamics/run_recipe.py). Doctrine/design: [Skill](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/jepa-anything-skill/SKILL.md), [architecture](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/docs/architecture.md), [project scope](https://github.com/Gen-Verse/JEPA-Anything/blob/c6e6c88f3ef75a4ce7acd660d6fa5779d995512c/README.md). | No access gap identified in the frozen tracked source. No supplied host execution, trained weights, domain datasets or experimental trace: prevents observed-compliance, empirical-performance and causal-effect conclusions. External paper/model links are not registered evidence. |
