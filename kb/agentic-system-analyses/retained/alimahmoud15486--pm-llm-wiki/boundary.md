---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "pm-llm-wiki's prompt-defined product-management knowledge system and fictional pilot at commit 64fb748ac9d187be4c51636aa56bfee1d9e5b116."
run-id: AAS-2026-11-09-pm-llm-wiki-4c3839e25928-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
analysis-cutoff: "2026-11-09"
evidence-tier: doc-grounded
source:
  identity: https://github.com/alimahmoud15486/pm-llm-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/pm-llm-wiki-61a4e13cd848/related-systems/alimahmoud15486--pm-llm-wiki
  revision: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
  sha256: null
---

# pm-llm-wiki boundary

## Boundary and evidence

This run covers the shipped PM Wiki as a prompt-defined product-management knowledge system: its reusable schema, setup and operating instructions, content-model rationale, and complete fictional FitLoop pilot. The intended use is to retain source-linked product knowledge and reuse it for decisions, discovery plans and generated deliverables. It is in scope because an external model-backed coding agent performs the prescribed ingestion, synthesis, retrieval and maintenance; the repository is not itself an enclosing agent runtime (SRC-1, `README.md`, `template/SCHEMA.md`).

> You (the LLM agent) are the maintainer of this product-management knowledge wiki. The human PM
> curates sources, directs analysis, and makes the calls; you do all filing, cross-referencing,
> synthesis, and bookkeeping. This file defines the structure, conventions, and workflows. Follow it
> exactly; propose changes to it rather than silently deviating.
> --- `template/SCHEMA.md`

The boundary is **whole-system** for that shipped knowledge system, not for its external agent host. Inspection traced the README setup into the schema, its ingest/query/lint instructions, the pilot's instantiated instructions, raw fictional inputs, retained pages, index, operation journal and filed-back PRD. The prescribed loop includes admission by the PM, agent-maintained persistence, index-first later consumption, proposal gates and recurring maintenance. The pilot is included as shipped state illustrating this loop, not excluded as an application caller. Its PRD is a retained downstream consumer of that state (SRC-1, `README.md`, `template/SCHEMA.md`, `pilot/CLAUDE.md`, `pilot/index.md`, `pilot/log.md`, `pilot/wiki/prd-adaptive-plans-v1.md`).

> 1. Read `index.md`, then only the relevant pages. 2. Synthesize with evidence chains. 3. Offer to
> file valuable answers back as a wiki page (analyses, comparisons, prioritizations compound too —
> file under `wiki/` and log as `exploration`).
> --- `template/SCHEMA.md`

The Git checkout's HEAD was verified against the acquired full commit. Only this repository at **64fb748ac9d187be4c51636aa56bfee1d9e5b116** supplies evidence; the applicability cutoff is **2026-11-09**. The evidence tier is **doc-grounded**: shipped instructions and example Markdown state support intended operation, not executable enforcement. The tracked tree contains no executable host, provider adapter, automated evaluator or test suite. The contribution guide prescribes fresh-agent testing, but supplies no inspectable transcript or evaluation results from which to establish reliability (SRC-1, `CONTRIBUTING.md`, `README.md`).

> Test schema changes the way this repo was tested: give the changed schema to a fresh agent
> session with a minimal prompt and check it behaves. Say in your PR what you observed.
> --- `CONTRIBUTING.md`

### Tracked top-level coverage

All tracked files were inspected. “Included” means inside the functional or contextual analysis boundary; it does not promote prose to implementation evidence. The table accounts for every top-level tracked file or directory (SRC-1).

| Top-level path | Coverage and inspected material paths | Role and limits |
|---|---|---|
| `.gitignore` | Included; `.gitignore` | Repository hygiene (`.DS_Store`), not a state-admission or security mechanism. |
| `CONTRIBUTING.md` | Included; `CONTRIBUTING.md` | Change constraints, fictional-data requirement and manual fresh-agent test prescription. No automated evaluator or retained test trace is supplied. |
| `LICENSE` | Included; `LICENSE` | Distribution terms and reference attribution; not operational evidence. |
| `PM-Wiki-Content-Model.md` | Included; `PM-Wiki-Content-Model.md` | Draft design rationale for sources, entities, outputs, rituals and deferred extensions. Distinguish its proposals from the shipped schema. |
| `README.md` | Included; `README.md` | Operator entry point: copy schema, create directories, supply sources, invoke an external agent; ingest/query/lint prompts, deliverable consumers and optional tooling. Performance and cost claims remain attributed prose. |
| `template/` | Included; `template/SCHEMA.md` | Reusable maintainer prompt: persistent file layout, entity/status rules, source admission, evidence requirements, direct-PM approval, writes, reload via index, file-back and maintenance. These are instructions to a model, not code-enforced controls. |
| `pilot/` | Included; `pilot/CLAUDE.md`, `pilot/index.md`, `pilot/log.md`; all seven files under `pilot/sources/`; `pilot/wiki/overview.md`, `pilot/wiki/assumptions.md`, `pilot/wiki/open-questions.md`, `pilot/wiki/prd-adaptive-plans-v1.md`; both `pilot/wiki/problems/` pages; `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`; `pilot/wiki/competitors/gymjoy.md` | Instantiated prompt and retained state across ingest, gating, later query, file-back, lint and schema progression. Sources cover two interviews, analytics, feedback digest, leadership meeting and two competitor-intel notes. The log describes pending and direct approvals and the PRD describes consumption; neither is a host execution trace. All product evidence is fictional. |
| `reference/` | Included as contextual doctrine; `reference/karpathy-llm-wiki-original.md`, `reference/llm-wiki-v2-notes.md` | Repository-retained pattern text and author's extension notes explain lineage. Only their committed contents are frozen; linked external gists and tools are not independently inspected evidence. They do not establish the PM adaptation's implemented or observed behavior. |

### External dependencies and prevented conclusions

The PM curates inputs, starts operations and approves gated edits. A separately supplied agentic tool with local-file access executes the model calls and file operations; the README names Claude Code as reference tooling and Codex or similar agents as alternatives. A folder is required; Obsidian and Git are optional user tools (SRC-1, `README.md`). Their implementations, permission systems, context loading and model behavior are outside this repository boundary. Consequently this run cannot establish runtime scheduling, context-window policy, approval enforcement, atomicity, concurrency safety or provider-specific behavior from this source.

The source explicitly requires the pilot's product evidence to remain fictional (SRC-1, `CONTRIBUTING.md`; also `pilot/CLAUDE.md`):

> Everything in `pilot/sources/` and `pilot/wiki/` is **fictional** and must stay clearly
> marked as such. Never add real customer data to this repo.
> --- `CONTRIBUTING.md`

Its populated pages and journal permit analysis of example structure and declared operation, not real customer outcomes, observed model compliance or causal benefits. No independent execution trace or causal experiment was supplied. This prevents claims of measured effectiveness, real-world maintenance cost or reliable gate adherence. Proposed later search, scheduled automation and graph tooling are not treated as deployed dependencies or implemented features (SRC-1, `template/SCHEMA.md`). These limits are evidence limits, not uninspected material shipped paths; no material portion of the repository's own prompt-and-state loop is deliberately excluded.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alimahmoud15486/pm-llm-wiki` | 64fb748ac9d187be4c51636aa56bfee1d9e5b116 | doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/pm-llm-wiki-61a4e13cd848/related-systems/alimahmoud15486--pm-llm-wiki`. Doctrine/design: complete tracked tree listed above, including schema, instantiated prompt, setup guide, design draft, references and fictional source/wiki state. Reported operation: README's fresh-agent testing assertion and pilot journal/PRD's descriptions of ingestion, approval and file-back. | Doctrine/design: [README](https://github.com/alimahmoud15486/pm-llm-wiki/blob/64fb748ac9d187be4c51636aa56bfee1d9e5b116/README.md), [schema](https://github.com/alimahmoud15486/pm-llm-wiki/blob/64fb748ac9d187be4c51636aa56bfee1d9e5b116/template/SCHEMA.md), [pilot prompt](https://github.com/alimahmoud15486/pm-llm-wiki/blob/64fb748ac9d187be4c51636aa56bfee1d9e5b116/pilot/CLAUDE.md), `PM-Wiki-Content-Model.md`, `CONTRIBUTING.md`, `pilot/index.md`, `pilot/wiki/`. Reported operation: [pilot journal](https://github.com/alimahmoud15486/pm-llm-wiki/blob/64fb748ac9d187be4c51636aa56bfee1d9e5b116/pilot/log.md), `pilot/wiki/prd-adaptive-plans-v1.md`, `README.md`. | No repository-file access gaps. No executable host, raw agent session, automated evaluation results or real-product evidence supplied. Doctrine does not establish enforcement; reported operation does not establish observed compliance or effectiveness. External links are not additional frozen sources. |
