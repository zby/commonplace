---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Echel's shipped SDLC memory, workflow, context and runtime-adapter paths at aee36de4d2d1c404fb36e9ad68cc0a920784ee61."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/alirezabbasi/echel
  revision: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-echel/related-systems/alirezabbasi--echel
  sha256: null
---

# Echel boundary

## Boundary and evidence

Echel is in scope as a memory/knowledge/context-engineering system serving agent execution. Its intended use is progressive software-product knowledge: retain project meaning, select work context, record execution and verification, and review proposed changes. It is not the enclosing model runtime. The whole-system boundary includes the shipped CLI, both storage/workflow families, context compiler, runtime protocol and Hermes adapter, verification driver, methodology skills, maintenance services, schemas, tests and benchmark assets. SRC-1 supplies implementation and declared design evidence.

The target's own division of responsibility is explicit (SRC-1, `README.md`):

> Echel owns methodology and product truth. Hermes is the first supported multi-model agent runtime; it owns sessions, tools, delegation, and model execution.
> --- `README.md`

The installed entry point is `echel = "echel.cli.main:main"` (SRC-1, `pyproject.toml`). Inspection traced its `init` branch into canonical record creation, `clarify` into canonical record reload, and the other workflow branches into `FileStore`. It traced `context` and `run` through context compilation to Hermes, run persistence back to `FileStore`, and `verify` through command execution to evidence persistence (SRC-1, `src/echel/cli/main.py`, `src/echel/initialization.py`, `src/echel/methodology/clarification.py`, `src/echel/storage/files.py`, `src/echel/verification/runner.py`). These callers are part of Echel, not excluded applications.

This boundary preserves a consequential distinction for later analysis: the canonical initializer writes a schema-versioned project and claim beneath `.echel/records`, whereas the older workflow/context path uses `.echel/knowledge`, uppercase record IDs and the older project model. The shared CLI does not establish that these paths compose into a working end-to-end journey. Both belong to the target; neither is silently discarded to make the architecture appear uniform (SRC-1, `src/echel/initialization.py`, `src/echel/storage/files.py`, `src/echel/workflow.py`, `src/echel/cli/main.py`). In particular, canonical knowledge authority must not be attributed automatically to the separate `FileStore` write path.

The retained-content consumer is inspectable, rather than inferred from a library description (SRC-1, `src/echel/context/compiler.py`):

> related = set(work.get("relates_to", []))
> knowledge = []
> for record in self.store.records("knowledge"):
>     if record.get("id") in related:
>         knowledge.append(record)
> --- `src/echel/context/compiler.py`

The shipped implementation skill also constrains what the agent should return. This is doctrine, not evidence that a runtime enforces promotion policy (SRC-1, `skills/implementation/SKILL.md`):

> Work only within the supplied objective and permissions. Inspect relevant code before editing. Run the declared verification. Return code changes, evidence, unresolved findings, and proposed knowledge updates separately. Never silently rewrite accepted product truth.
> --- `skills/implementation/SKILL.md`

External dependencies are Python, the declared `jsonschema` package, the local filesystem and SQLite, Git repository structure, and the separately installed Hermes executable when actual agent execution is requested (SRC-1, `pyproject.toml`, `src/echel/runtimes/hermes.py`, `docs/architecture.md`). Hermes internals, provider services, human identity infrastructure, Git internals, CI service execution and deployment infrastructure are outside this source boundary. Their absence prevents conclusions about actual model behavior, provider safety, authenticated human identity, isolation enforcement or production release outcomes. The in-repository adapters and CI definitions remain included. No dependency repository or live service is registered as evidence.

The frozen revision is `aee36de4d2d1c404fb36e9ad68cc0a920784ee61`; checkout HEAD was checked against the acquired pin. The applicability cutoff is 2026-10-15, not a claim about source activity after that revision. The overall evidence tier is code-grounded. No target commands, examples or tests were executed. Test source supports intended contracts, not passing execution. The repository's local synthetic kernel result is attributed reported operation, not an independently observed run or causal experiment. Its own limitation is (SRC-1, `benchmarks/kernel/evidence/2026-07-15-local.json`):

> "synthetic deterministic kernel dataset, not a product-scenario benchmark"
> --- `benchmarks/kernel/evidence/2026-07-15-local.json`

### Top-level coverage

Every top-level tracked entry is classified below. Included means within the functional evidence boundary, not that every file has already been read. Initial inspection traced the state-producing and state-consuming CLI paths, canonical admission service, query consumer, shipped skills and evaluator entry point. Available but not yet inspected material is identified explicitly; it is not an access gap. There is no material shipped responsibility deliberately excluded from the functional loop.

| Top-level entry | Classification and role | Initial inspection and limits |
|---|---|---|
| `.github/` | Included: development admission and automation | Read `.github/workflows/quality.yml`; `.github/PULL_REQUEST_TEMPLATE.md` enumerated, not yet inspected. No CI run evidence. |
| `.gitignore` | Excluded: local ignore configuration | Tree entry only; cannot infer ignored local artifacts or historical implementations from it. |
| `AGENTS.md` | Included: shipped maintainer/agent instructions | Read in full; instructions are target doctrine, not worker authority. |
| `CONTRIBUTING.md` | Included: contribution entry point | Enumerated, not yet inspected; no conclusions about its detailed procedure. |
| `LICENSE` | Excluded: legal text | Tree entry only; no independent licensing assessment. |
| `Makefile` | Included: quality/evaluator callers | Read test, scenario, packaging, security and verification targets; no execution. |
| `README.md` | Included: product intent and public entry paths | Read in full; reset narrative does not supply historical code evidence. |
| `benchmarks/` | Included: evaluators, metrics, scenarios and supplied result | Read `README.md`, `kernel/gate.py`, `kernel/evidence/2026-07-15-local.json`. `metrics/v1.json`, `scenarios/{BF-01,BF-02,BF-03,GF-01,GF-02,GF-03,index}.json` and kernel documentation enumerated, not yet inspected. Catalog selection is not product-scenario execution. |
| `docs/` | Included: design, maintenance and lifecycle contracts | Read `architecture.md` and `hermes.md`. `methodology.md`, `v2-reset.md`, `product/`, `decisions/`, `reference/` and `contributing/` remain available for detailed contract inspection; not treated as implemented behavior by their existence. |
| `examples/` | Included: shipped usage guidance | Read `first-product.md`; it connects work context omissions to explicit relationships, not a separate host application. |
| `pyproject.toml` | Included: package and command wiring | Read in full; entry point, packaged schema assets and actual dependency declarations control implementation scope. |
| `schemas/` | Included: schema documentation and fixtures | `v1/README.md`, `v1/fixtures/{valid-records,invalid-records}.json` enumerated, not yet inspected; executable schema asset is under `src/`. |
| `skills/` | Included: agent-facing prompts for creating, consuming and maintaining product knowledge | Read all eleven `SKILL.md` files: problem-definition, vision-and-opportunity, product-strategy, requirements, domain-model, architecture, implementation-planning, implementation, validation, deployment and operations. Their presence does not establish automatic loading by Hermes. |
| `src/` | Included: full shipped implementation, not only the public library API | Read `echel/cli/main.py`, `workflow.py`, `storage/files.py`, `context/compiler.py`, `runtimes/hermes.py`, `verification/runner.py`, `authority.py`; bounded inspection of initialization preview/apply, clarification reload/selection, canonical store load/scan/write, and query/search/impact consumers. Enumerated service entry points include `storage/{layout,transactions,index}.py`, `lifecycle.py`, `profiles.py`, `relationships.py`, `findings.py`, `migrations.py`, `portability.py`, `integrity.py`, model/domain/methodology modules, runtime protocol and schema registry/assets; their internals remain for detailed analysis. All are included, with no assumption that CLI wires every service. |
| `tests/` | Included: contract checks and consumers of implementation APIs | Read `unit/test_core.py` and `integration/test_cli.py`, including legacy store/context consumption and canonical two-record init expectations. `m0/`, `m1/`, `m2/` contract suites enumerated, not yet inspected in detail; no test results inferred. |

The untracked/ignored historical `v1/` mentioned by the README is not part of the pinned tracked source set. That exclusion prevents comparison with the old implementation's actual behavior. Available unread files above remain part of SRC-1 and may be inspected at this revision without changing the boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alirezabbasi/echel` | aee36de4d2d1c404fb36e9ad68cc0a920784ee61 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-echel/related-systems/alirezabbasi--echel`. Implementation: tracked tree and entry-point inventory; CLI, workflow, file store, context compiler, Hermes adapter, verification runner, authority service; bounded initializer, canonical store, clarification and query inspection; kernel gate and two test consumers. Doctrine/design: README, architecture, Hermes documentation, agent instructions, all eleven skills, example, package and quality configuration. Reported operation: local synthetic kernel JSON. Coverage table identifies available unread material. | Implementation: [CLI](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/src/echel/cli/main.py), [canonical store](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/src/echel/storage/records.py), [context compiler](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/src/echel/context/compiler.py). Doctrine/design: [README](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/README.md), [implementation skill](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/skills/implementation/SKILL.md). Reported operation: [local kernel result](https://github.com/alirezabbasi/echel/blob/aee36de4d2d1c404fb36e9ad68cc0a920784ee61/benchmarks/kernel/evidence/2026-07-15-local.json). | No source access failure encountered. External runtime/provider internals and live service operation are outside this repository; no execution was performed. The local benchmark artifact supplies attributed measurements only, not an independently observed end-to-end product/agent run. |
