---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Project Wiki's instruction-based project memory skill and deterministic helpers at commit 3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41."
run-id: AAS-2026-11-08-project-wiki-b055e5c71dc7-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/giodra96/project-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/project-wiki-d88135c77d9c/related-systems/giodra96--project-wiki
  revision: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
  sha256: null
---

# Project Wiki boundary

## Boundary and evidence

Project Wiki is in scope as a memory/knowledge/context-engineering system: a portable agent skill that specifies how a coding agent captures project knowledge, admits reviewed source content into canonical records, maintains those records, and retrieves them in later tasks. The target is the complete shipped skill, not merely its extraction or validation scripts. It is not an enclosing agent runtime. Its model-dependent semantic work is performed by the host agent following shipped instructions (SRC-1, `SKILL.md`, `references/update-workflows.md`, `references/automatic-workflows.md`).

> Project Wiki is a portable instruction-based skill rather than a hosted service. It can be installed personally or committed with a repository, and the generated knowledge remains plain Markdown and YAML inside the target project.
> --- `README.md`

The intended use is durable project memory beside source code. The functional boundary includes task routing; init and repository scanning; instruction bootstrap; notes and document intake; source deduplication and provenance; review ledger management; canonical classification and integration; requirements, decisions, technical records and traceability; automatic context preflight and impact-based updates; explicit sync; maintenance, migration and semantic lint; configuration and help; and shipped structural checks and tests. These are responsibilities of the delivered system even where implemented as agent instructions rather than executable Python (SRC-1, `SKILL.md`, `references/initialization-workflows.md`, `references/document-ingestion.md`, `references/common-policies.md`, `references/maintenance-workflows.md`).

The whole-system boundary follows the shipped state loop. `SKILL.md` routes explicit modes and automatic triggers to reference procedures. Initialization calls `scripts/wiki_scaffold.py`, which loads the schema and templates, stages files, invokes `validate_wiki`, and publishes a new wiki; project-specific semantic completion and instruction installation remain in the initialization procedure. `references/source-inbox.md` routes preflight to `scripts/check_inbox.py`, followed by hash-bound extraction through `scripts/ingest_document.py`. The latter writes intake artifacts, including chunks and the review ledger. `scripts/review_progress.py` reloads those artifacts for inspection, source views, ledger updates and digest checkpoints. The document-ingestion procedure assigns semantic classification, comparison, canonical writes and final status changes to the agent. Maintenance consumes `scripts/validate_wiki.py` results before semantic lint; `scripts/check_contracts.py` checks the skill's own schema/documentation/template alignment (SRC-1, those paths).

Later consumption and maintenance are inside the boundary, not treated as an unspecified external caller. Generated project instruction blocks and automatic workflows direct future coding tasks to retained knowledge and then update it when warranted (SRC-1, `assets/core-templates.md`, `references/automatic-workflows.md`):

> 1. Read `.project-wiki/INDEX.md` first.
> --- `references/automatic-workflows.md`

> 3. Read the section `INDEX.md`, then only the linked documents needed for the task.
> --- `references/automatic-workflows.md`

> Assess wiki impact automatically after source code changes made by the agent through chat. The user should not need to invoke `sync` for changes that require immediate documentation. Finalize once per coherent task, rather than after each intermediate edit.
> --- `references/automatic-workflows.md`

These instructions establish the designed retrieval/update loop, not proof that any host always invokes or obeys it. In particular, the host supplies model inference, task interpretation, filesystem/tool permissions, instruction loading, code execution and user interaction. No host implementation or provider is frozen here, so this analysis cannot establish host scheduling, enforcement, context-window behavior, permissions or model quality. The skill's generated `AGENTS.md` and Copilot block remain included as shipped integration instructions; their actual loading by each named host is not established (SRC-1, `README.md`, `assets/core-templates.md`).

### Repository coverage

The tracked tree was enumerated at the frozen HEAD and shipped entry points were traced to their instruction consumers and helper calls. Every top-level tracked file or directory is classified below. Inclusion is analytical scope, not a claim that every line was inspected. Initial inspection covered the routes and material state-loop responsibilities; deeper implementation details remain available at the same pin, not excluded evidence.

| Top-level tracked path | Classification and inspected material paths | Role and limit |
| --- | --- | --- |
| `SKILL.md` | Included; read in full | Agent entry point, explicit modes, automatic triggers, operating contract and invariants. |
| `README.md` | Included; read in full | Installation, intended use, architecture and host compatibility declarations; examples are documentation, not observed executions. |
| `references/` | Included; all workflow files read: `automatic-workflows.md`, `initialization-workflows.md`, `update-workflows.md`, `synchronization-workflow.md`, `maintenance-workflows.md`, `common-policies.md`, `configuration.md`, `source-inbox.md`, `document-ingestion.md`, `repository-scope.md`; section inventory inspected for `wiki-structure.md` | Shipped semantic drivers for production, admission, maintenance and later consumption. Detailed structure clauses beyond the initial inventory remain available but are not yet fully inspected. No material workflow is deliberately excluded. |
| `assets/` | Included: `core-templates.md` root index, registry, version and always-on block inspected; template section inventories inspected for `document-templates.md`, `requirements-change-templates.md`, `technical-implementation-templates.md`, `intake-source-templates.md`, `governance-templates.md`, `user-help.md`; `banner.png` deliberately excluded as presentation | Generated routing/instruction surfaces and record/template families. Remaining template bodies are not yet fully inspected, not inaccessible. Banner exclusion prevents conclusions about visual presentation only. |
| `schema/` | Included: `project-wiki.yml` artifact versions, review states, semantic paths, canonical-tree opening, source action map and template contracts inspected | Machine contract consumed by the helpers. Remaining schema sections are available for later exact-contract inspection. |
| `scripts/` | Included: CLI/function/import inventories; control flow inspected in `wiki_scaffold.py`, `check_inbox.py`, `ingest_document.py`, `review_progress.py`, `validate_wiki.py`, `check_contracts.py`, `wiki_scope.py`; configuration and help implementations inspected in `wiki_config.py`, `wiki_help.py`; loader inspected in `schema_contract.py`; `requirements.txt` read | Executable production, source admission, retained-state reload, validation, source access, preference and help planes. Inspection establishes their place in the loop, not correctness of every helper branch. All helper implementations remain in scope. |
| `tests/` | Included: tracked suite inventory plus `test_wiki_config_integration.py` CLI runner and scaffold/configuration/validation cases inspected | Tests cover inbox, ingestion and ingestion units, review progress, schema, validation, configuration, configuration integration, help, scaffold and scope; `wiki_fixtures.py` supplies fixtures. Remaining assertions are not yet fully inspected. Tests are implementation evidence of checks, not run results or evaluation of agent semantic quality. |
| `.github/` | Included: `workflows/tests.yml` read; `ISSUE_TEMPLATE/bug_report.yml`, `ISSUE_TEMPLATE/config.yml`, `ISSUE_TEMPLATE/feature_request.yml`, and `pull_request_template.md` deliberately excluded | CI invokes unittest, contract checking, compilation and CLI smoke checks. Excluded collaboration forms prevent conclusions about issue/PR intake policy, not wiki knowledge intake. The generated consumer Copilot instructions are specified in the included templates, not supplied as a target-project instance here. |
| `.gitignore` | Excluded deliberately; tracked-path inventory only | Development ignore policy is not analysed; no conclusion about packaging/ignore completeness. |
| `CODE_OF_CONDUCT.md` | Excluded deliberately; tracked-path inventory only | No conclusion about community conduct policy or enforcement. |
| `CONTRIBUTING.md` | Excluded deliberately; README and CI testing routes inspected instead | No conclusion about contributor setup completeness or process compliance. |
| `LICENSE` | Excluded deliberately; tracked-path inventory only | No legal interpretation or licensing-compliance conclusion. |
| `SECURITY.md` | Excluded deliberately; tracked-path inventory only | No conclusion about vulnerability reporting or security response practice. |

Coverage anchors are SRC-1's commit-relative paths named in the table. The `tests/` directory and CI workflow provide shipped evaluators of deterministic helper behavior, not a supplied model-task benchmark or a trace of a populated wiki used across sessions. No target scripts, tests or examples were executed. No populated consuming-project wiki or host trace was supplied as run evidence; therefore retrieval effectiveness, semantic integration quality, actual cross-session persistence/use and operational reliability cannot be established from this boundary.

The frozen evidence is the acquired Git repository at full commit `3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41`; checkout HEAD was verified against that pin. The applicability cutoff is 2026-11-08, the supplied run date, not a claim about upstream changes after the pin. Overall evidence is code-grounded for inspected helper control flow, with doctrine/design evidence for the model-dependent workflows. External links in the README, host products, dependency implementations, consuming repositories and subsequent upstream revisions are not additional sources. Their exclusion prevents independent claims about upstream inspiration, host behavior, dependency internals and deployed project outcomes. Python and the packages in `scripts/requirements.txt` are execution dependencies; Git is used by the source-scope helper (SRC-1, `scripts/requirements.txt`, `scripts/wiki_scope.py`). No access failure occurred for the frozen repository; available material not yet read in depth is identified above rather than presented as unavailable evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/giodra96/project-wiki` | 3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/project-wiki-d88135c77d9c/related-systems/giodra96--project-wiki`. Implementation: tracked tree, helper entry/control-flow ranges, schema loader, configuration/help implementations, schema fields, CI and selected CLI integration tests as detailed in coverage. Doctrine/design: complete README, SKILL and routed workflow procedures, core generated instructions/routing templates and remaining template/structure inventories. | Implementation: [scaffolding](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/scripts/wiki_scaffold.py), [ingestion](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/scripts/ingest_document.py), [review reload/update](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/scripts/review_progress.py), [validation](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/scripts/validate_wiki.py), [CI](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/.github/workflows/tests.yml). Doctrine/design: [skill entry](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/SKILL.md), [later use and update](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/references/automatic-workflows.md), [intake admission](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/references/document-ingestion.md), [generated instructions](https://github.com/giodra96/project-wiki/blob/3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41/assets/core-templates.md). | No repository access gap. Uninspected detail and deliberate nonfunctional exclusions are distinguished in coverage. No observed run or causal experiment is registered; tests and instructions alone cannot establish host adherence, semantic quality, retrieval benefit or deployed reliability. |
