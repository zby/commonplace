---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenClerk's shipped knowledge operating layer, agent instructions, local storage, modules and evaluation drivers at commit 092fb98d243c2d9d95867ad04618ebce88983552."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/yazanabuashour/openclerk
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-openclerk/related-systems/yazanabuashour--openclerk
  revision: "092fb98d243c2d9d95867ad04618ebce88983552"
  sha256: null
---

# OpenClerk boundary

## Boundary and evidence

OpenClerk is in scope as a **memory/knowledge/context-engineering system**, not an enclosing agent runtime. Its intended use is to govern coding agents' retained Markdown knowledge through a local command interface, agent instructions, citation-bearing retrieval and document lifecycle operations. Its shipped instructions serve an external model-driven agent; the absence of an enclosing model loop in the core CLI does not make this merely an unrelated Markdown utility (SRC-1, `README.md`, `skills/openclerk/SKILL.md`, `docs/agent-contract.md`).

> OpenClerk gives coding agents a local, citation-bearing knowledge runtime over
> Markdown. Canonical Markdown stays the authority; generated indexes and
> optional modules stay derived.
> --- `README.md`

The boundary is **whole-system**: the shipped CLI and demo callers, runner actions, local client and SQLite storage, Chronicler session planning and context consumption, skills, optional module integration, examples, and evaluation/maintenance drivers. It is not restricted to the store API. The CLI dispatches `document`, `retrieval`, `clerk`, configuration and module commands; the document runner separates mutating actions from read-only requests and opens the corresponding local client (SRC-1, `cmd/openclerk/main.go`, `internal/runner/document.go`, `internal/runclient/local.go`).

Initial tracing covers the retained-state loop. Document creation writes canonical content, synchronizes it into derived state, and reloads the registered document. Vault synchronization scans Markdown and imports it in batches. Retrieval calls the client search API; the SQLite implementation supplies lexical search and token fallback. Chronicler consumes that retrieval for task context and passes explicit session files to artifact candidate planning. These are included shipped consumers, not excluded applications (SRC-1, `internal/infra/sqlite/documents.go`, `internal/infra/sqlite/sync.go`, `internal/runner/retrieval.go`, `internal/chronicler/chronicler.go`).

> if err := s.syncDocumentFromDisk(ctx, relPath, input.Title); err != nil {
> 		return domain.Document{}, err
> 	}
> 	return s.getDocumentByPath(ctx, relPath)
> --- `internal/infra/sqlite/documents.go`

The agent-facing contract describes the larger cycle: obtain context, perform application work outside OpenClerk, then submit explicit session evidence for planning and approved document changes. This establishes the intended consumption path, not proof that a deployed agent follows the contract (SRC-1, `docs/agent-contract.md`).

> 4. Do the work outside OpenClerk.
> 5. After work, pass an explicit session note, handoff, or inbox artifact to the
>    read-only `openclerk clerk` planning surface.
> 6. Apply durable writes only through approved `openclerk document` lifecycle
>    APIs.
> --- `docs/agent-contract.md`

The shipped evaluation harness is included. Its driver prepares scenario state, installs a variant, builds the runner, seeds data, invokes scenario turns and verifies results, including carrying a session ID across turns. Excluding it merely because it invokes Codex would omit a shipped producer and consumer of knowledge state (SRC-1, `scripts/agent-eval/ockp/codex_runner.go`).

### Frozen scope and limits

The evidence is the acquired repository at full commit `092fb98d243c2d9d95867ad04618ebce88983552`, with applicability cutoff **2026-10-16**. HEAD matched the supplied pin and the checkout had no reported changes. Overall evidence is **code-grounded** source inspection; no target execution, provider invocation or new experiment was performed. The source register covers the repository at that commit, not only the initially inspected files.

External dependencies include the coding-agent host and its model provider, local filesystem and SQLite implementation, optional Ollama or Gemini embedding services, and OCR tooling. Their integration code, manifests and skills belong to this boundary; external implementations, credentials, service operation and user vaults do not. This prevents conclusions about host scheduling or model reasoning, actual provider reliability/privacy behavior, OCR accuracy, or deployment-specific knowledge quality. The adapter explicitly names Ollama and Gemini and imports SQLite; the product lists its optional OCR module (SRC-1, `modules/semantic-retrieval-adapter/main.go`, `README.md`). No external source was acquired.

No required source access gap was found. Available files not yet inspected are distinguished below from deliberate exclusions. Inclusion means they remain available for later investigation at the same pin, not that all their claims or code paths have already been checked. In particular, bundled evaluations are not automatically observed-run evidence, and design documents do not establish executable behavior.

### Top-level coverage

All rows refer to SRC-1 at the frozen revision. Paths in directory rows identify material responsibilities, not an evidence allowlist.

| Top-level tracked path | Treatment and material scope | Inspection status and conclusion limit |
|---|---|---|
| `.github/` | Included: workflows, release delivery, skill validation, issue/PR governance. | Workflow search inspected `.github/workflows/pull-request.yml`; other files not yet inspected. No release-integrity or CI-success conclusion. |
| `.gitignore` | Included: repository artifact/state hygiene. | Not yet inspected; no claim about ignored state completeness. |
| `.golangci.yml` | Included: development static-check configuration. | Not yet inspected; no lint-quality conclusion. |
| `AGENTS.md` | Included: maintainer instructions and evaluation/decision taste checks. | Read in full as target doctrine, not worker authority. |
| `CHANGELOG.md` | Included: release intent/history. | Not yet inspected; no historical behavior claim. |
| `CODEBASE_AUDIT.md` | Included: target-authored audit evidence. | Not yet inspected; no audit finding adopted. |
| `CODE_OF_CONDUCT.md` | Excluded: community conduct policy. | Deliberate nonfunctional exclusion; no community-governance assessment. |
| `CONTEXT.md` | Included: knowledge authority and storage vocabulary. | Read in full as doctrine. |
| `CONTRIBUTING.md` | Included: development/maintenance procedure. | Not yet inspected; no contributor-workflow assessment. |
| `LICENSE` | Excluded: legal terms. | Deliberate exclusion; no licensing conclusion. |
| `README.md` | Included: supported product surface, agent loop and module inventory. | Read in full as doctrine/design. |
| `SECURITY.md` | Included: security operating contract. | Not yet inspected; no security-policy effectiveness claim. |
| `cmd/` | Included: `cmd/openclerk/main.go`, `inspect.go`, `demo_templates.go` and tests; CLI admission, inspection and demo state producers/consumers. | Dispatch read and document/retrieval/clerk/demo call sites searched in `main.go`; demo bodies and tests not yet inspected in detail. |
| `docs/` | Included: `agent-contract.md`, `architecture/`, `evals/`, evaluation results, installation, release/security and knowledge-pack instructions. | Agent contract read in full; remaining documents not yet inspected. No bundled evaluation outcomes or comparison claims adopted. |
| `examples/` | Included: `knowledge-packs/` commands, inbox/handoff inputs, source/decision/synthesis vault fixtures. | Tree inspected and `knowledge-packs/agent-session-to-docs/commands.md` read; other packs not yet inspected in detail. Example outcomes remain declared expectations. |
| `go.mod` | Included: module/dependency contract. | Module and Go-version declarations searched; dependency details not yet inspected. |
| `go.sum` | Included: dependency checksums. | Not yet inspected; no dependency-integrity assessment. |
| `internal/` | Included: `runner/` admission, planning, lifecycle, retrieval, synthesis, audit and maintenance reports; `runclient/` local configuration/client/module integration; `infra/sqlite/` canonical-file persistence, import, indexes/projections and provenance; `chronicler/` session intake/context packs; `domain/` contracts; `evals/`, `skilltest/`, `tools/` checks. | Initial code trace reads document/retrieval runners, runtime open modes, SQLite creation/search/sync, Chronicler planning/context; client calls searched. Remaining actions, projections, tools and tests not yet inspected in detail. No exhaustive correctness claim. |
| `mise.toml` | Included: pinned development tooling. | Tool-version declarations searched; tooling not executed. |
| `modules/` | Included: `semantic-retrieval-adapter/` executable and manifest; `ollama-embeddings/`, `gemini-embeddings/`, `tesseract-ocr/` manifests/skills; `docs/install.md`. | Adapter request/provider structure read and manifests searched for integration/installation contract; execution and remaining implementation not yet inspected. No provider-quality or OCR-result claim. |
| `scripts/` | Included: install/release bundles, skill/artifact validation, checkpoint review, and `agent-eval/ockp/` drivers, seeding, verification, telemetry and reporting. | Installer registration/output searched; Codex evaluation driver setup/turn/verification flow read and subprocess call sites searched. Other scripts not yet inspected in detail; no successful-install or evaluation-pass conclusion. |
| `skills/` | Included: `openclerk/SKILL.md` routing, proposal/approval, recall and maintenance instructions. | Read in full as shipped agent doctrine; instruction compliance is not observed. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/yazanabuashour/openclerk` | 092fb98d243c2d9d95867ad04618ebce88983552 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-openclerk/related-systems/yazanabuashour--openclerk`. Implementation: CLI dispatch/call sites in `cmd/openclerk/main.go`; document/retrieval routing in `internal/runner/document.go` and `internal/runner/retrieval.go`; open modes in `internal/runclient/local.go`, client call searches in `internal/runclient/client.go`; create/search in `internal/infra/sqlite/documents.go` and vault import in `internal/infra/sqlite/sync.go`; session planning and context consumption in `internal/chronicler/chronicler.go`; evaluation driver in `scripts/agent-eval/ockp/codex_runner.go`; provider/request structures in `modules/semantic-retrieval-adapter/main.go`; installer, manifests and CI searches. Doctrine/design: full `README.md`, `skills/openclerk/SKILL.md`, `docs/agent-contract.md`, `CONTEXT.md`, `AGENTS.md`, and `examples/knowledge-packs/agent-session-to-docs/commands.md`. | Implementation: [CLI](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/cmd/openclerk/main.go), [store lifecycle](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/internal/infra/sqlite/documents.go), [Chronicler](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/internal/chronicler/chronicler.go), [evaluation driver](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/scripts/agent-eval/ockp/codex_runner.go). Doctrine/design: [skill](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/skills/openclerk/SKILL.md), [agent contract](https://github.com/yazanabuashour/openclerk/blob/092fb98d243c2d9d95867ad04618ebce88983552/docs/agent-contract.md). | No checkout access gap. Initial inspection is not exhaustive; uninspected files remain available under this source. No new observed run or causal experiment; no runtime-compliance, performance or deployment-quality conclusion. External hosts/providers and private vault contents are outside the source. |
