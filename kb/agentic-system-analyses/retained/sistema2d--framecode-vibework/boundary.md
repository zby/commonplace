---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "FrameCode-VibeWork's Markdown governance, technical memory and optional local tooling at frozen commit 847cdcedc02d08531961c8367f4e2ddb2dc392f1."
run-id: AAS-2026-11-08-framecode-vibework-d38fb53e8013-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/sistema2d/framecode-vibework
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/framecode-vibework-e112886c90b7/related-systems/sistema2d--framecode-vibework
  revision: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
  sha256: null
---

# FrameCode-VibeWork boundary

## Boundary and evidence

FrameCode-VibeWork (FCVW) is in scope as a memory/knowledge/context-engineering system for AI-assisted software development. Its shipped artifact combines agent-facing instructions, routed policies, plans and evidence records, curated Markdown memory, and optional deterministic Python tools. It is not classified as an enclosing agent runtime. The intended use of this analysis is to explain how the shipped governance and memory loop structures an external agent's work, what its tools implement, and what still depends on that agent or a human following instructions. SRC-1, `README.md`, `AGENTS.md`, `FCVW/wiki/README.md`, `FCVW/AI.md`.

> FrameCode VibeWork (FCVW) is a Markdown governance layer for projects built by people and AI agents. Every change follows a verifiable path: minimum context → plan → scoped execution → evidence → version record.
> --- `README.md`

> FCVW is not an agent runtime and does not replace tests, CI or human review.
> --- `README.md`

The boundary is **whole-system**, meaning the shipped FCVW system, not an entire consuming application's model-execution loop. It includes both the portable Markdown baseline and the optional tooling; treating the target as only its retriever or MCP API would omit its shipped state writers and later readers. Root `AGENTS.md` and the editor bridges route the host into policies and skills. The plan workflow governs persisted work records. The curator governs promotion, source review, handoffs and rotation. Later sessions are instructed to reload relevant plans and handoffs; the index builder and retriever provide optional machine paths for locating retained content. These responsibilities are present within this repository, even though the host executes the model-dependent steps. SRC-1, `AGENTS.md`, `.cursorrules`, `.windsurfrules`, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/AI.md`, `tools/build_context_index.py`, `tools/retrieve_context.py`.

> 1. **Locate relevant state**: read the active plan and latest relevant session, selected by date, unique ID, and scope rather than highest sequential number.
> 2. **Verify current state**: compare the handoff with the filesystem, plan status, and validation evidence.
> 3. **Load narrowly**: follow the handoff's links and `context_files`; do not load the whole archive.
> --- `FCVW/AI.md`

> Promote only when knowledge is reusable, sourced, and not already canonical. Prefer updating an existing page. Link the plan, failure, decision, source, or session that supports the claim.
> --- `FCVW/wiki/README.md`

Initial entry-point tracing covered `build_context_index.py` writing JSONL chunks from Markdown; `retrieve_context.py` loading that index, resolving mandatory routes and returning complementary results; the MCP handlers calling routing, section reading, queue, digest and validation functions; and harness hooks injecting session context, checking plan presence and invoking validation at stop. The local validation runner invokes tests, governance checks, a retrieval benchmark and installed-layout verification. These are included consumers and drivers, not excluded external applications. SRC-1, `tools/build_context_index.py`, `tools/retrieve_context.py`, `tools/mcp_server_fcvw.py`, `tools/hook_fcvw.py`, `tools/check_fcvw.py`.

The exact frozen source is Git commit `847cdcedc02d08531961c8367f4e2ddb2dc392f1`; checkout HEAD was checked against acquisition. The applicability cutoff is 2026-11-08. No additional repository, downloaded release asset, live issue, external page or later revision is frozen. Links within target documents do not admit their destinations as evidence. Overall evidence is **code-grounded** for the optional tooling and **doctrine/design** for instructions the host must execute. No target code, tests, examples, model providers or services were executed for this boundary.

### Top-level coverage

The tracked tree was enumerated before classification. Included means admitted to this functional boundary, not a claim that every line has already been inspected. Initial inspection established the material entry points, state-production and maintenance instructions, consumers and evaluators. Available supporting files not yet inspected are identified below; they are not access gaps.

| Top-level tracked path | Treatment and material paths | Role, initial inspection and limits |
|---|---|---|
| `AGENTS.md` | Included; read in full | Operational entry point, instruction routing, plan creation/closure, validation and navigation obligations. |
| `.cursorrules` | Included; read in full | Editor bridge to `AGENTS.md` and FCVW governance; does not establish that an editor loaded it. |
| `.windsurfrules` | Included; read in full | Equivalent editor bridge; host activation remains external evidence. |
| `README.md` | Included; read in full | Product scope, installation entry and stated non-runtime boundary. |
| `FCVW/` | Included: `README.md`, `CONTEXT_MAP.md`, `AI.md`, `wiki/README.md`, `wiki/index.md`, `skills/`, `governance/`, root policies/profiles/lock, `Plans/`, `audits/`, `decisions/`, `framework-releases/`, `troubleshooting/` | Persistent governance and knowledge surface. Initial full reads: operational index, context map, AI policy, wiki contract, curator, orchestrator and self-improvement skills, testing policy. Initial partial read: automation contract. These cover loading, writing, admission, curation, reload, delegation and evaluation responsibilities. Remaining skills (including QA and governance-validator), templates, profiles, ownership/upgrade policies and historical records remain available but not yet substantively inspected. Framework history is not evidence of successful deployment in a consuming project. |
| `tools/` | Included: index/retrieval/routing/selection, document/knowledge graphs and source checks; plan queue/dependencies; validator/frontmatter/path/role/cache utilities; MCP and hook adapters; QA checker and trace; upgrade, locale, packaging, release-layout and verification tools; benchmark, local runner and all `test_*.py` files | Executable support for state admission, derivation, later consumption, maintenance and evaluation. Initial body inspection: index writing, retrieval CLI, MCP tool handlers, hook lifecycle handlers, source-digest/dependent-review checks, benchmark/check runner and release-layout mapping. Other modules and test bodies are available but not yet inspected; no pass claim is made. Source `tools/` maps into installed `FCVW/tools/`, so the source-root location does not make these external. |
| `TODO.md` | Included as source-only maintainer backlog; opening portion inspected | Target-authored reported findings and improvement work, not policy or independent verification. It is excluded from installed payloads by `tools/release_layout_fcvw.py`. Remaining backlog is available but not yet inspected. |
| `.gitignore` | Included; read in full | Cache, editor state, secrets and generated manifest exclusions; ignoring a path does not prove runtime privacy or deletion. |
| `.gitattributes` | Excluded from functional analysis; tree presence inspected, content not inspected | Repository text-handling metadata; no conclusion about checkout normalization or byte-identical cross-platform packaging follows from this exclusion. |
| `.github/` | Excluded: tracked `FUNDING.yml` only; tree inspected | Funding metadata, not a shipped CI execution path at this pin. No conclusion about sponsorship configuration is attempted. |
| `LICENSE` | Excluded from functional analysis; tree presence inspected | Legal terms; no license-compliance judgment. Its packaging location remains within the admitted release-layout mechanism. |
| `NOTICE` | Excluded from functional analysis; tree presence inspected | Attribution notice; no attribution-compliance judgment. Its packaging location remains within the admitted release-layout mechanism. |

### External dependencies and evidential limits

The external agent harness, model, user approvals, consuming application's code/data/tests and project-specific credentials are outside the target. Their responsibilities are not attributed to FCVW. Optional Python tools require an interpreter and local filesystem; Git is used by maintenance/validation paths. Editor bridges and optional MCP/hook integrations require a compatible, configured host. The baseline explicitly distinguishes describing automation from running it. SRC-1, `FCVW/AUTOMATION.md`, `FCVW/README.md`, `tools/hook_fcvw.py`, `tools/mcp_server_fcvw.py`, `tools/check_fcvw.py`.

> A Markdown contract describes expected behavior. It does not prove execution. Evidence must identify who or what ran the contract, when, inputs, result, and remaining failures.
> --- `FCVW/AUTOMATION.md`

No consuming-project state, host/model execution trace or independently observed evaluation was supplied. This prevents conclusions about actual instruction adherence, real-task quality, model-token savings, automatic memory promotion or deployment reliability. It does not prevent describing the shipped procedures and executable support. The synthetic benchmark and local runner are included as evaluation mechanisms, not as observed runs in this analysis. SRC-1, `FCVW/TESTS.md`, `tools/benchmark_retrieval_fcvw.py`, `tools/check_fcvw.py`.

> "notice": "Caller-supplied outcomes; no model was executed. Estimated JSON tokens are not model usage. "
> --- `tools/benchmark_retrieval_fcvw.py`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sistema2d/framecode-vibework` | 847cdcedc02d08531961c8367f4e2ddb2dc392f1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/framecode-vibework-e112886c90b7/related-systems/sistema2d--framecode-vibework`. Implementation: bounded source reads of index production, retrieval CLI, MCP handlers, hooks, source freshness, benchmark, local checks and release layout. Doctrine/design: root README/AGENTS/editor bridges, FCVW index, AI/context/wiki/testing contracts, curator/orchestrator/self-improvement skills and automation opening. Reported operation: AI context-size measurements, testing descriptions and opening maintainer backlog; not independently reproduced. Whole tracked tree enumerated; supporting files not yet inspected remain available at the same pin. | Implementation: [index writer](https://github.com/sistema2d/framecode-vibework/blob/847cdcedc02d08531961c8367f4e2ddb2dc392f1/tools/build_context_index.py), [retrieval consumer](https://github.com/sistema2d/framecode-vibework/blob/847cdcedc02d08531961c8367f4e2ddb2dc392f1/tools/retrieve_context.py), `tools/mcp_server_fcvw.py`, `tools/hook_fcvw.py`, `tools/knowledge_sources_fcvw.py`, `tools/benchmark_retrieval_fcvw.py`, `tools/check_fcvw.py`, `tools/release_layout_fcvw.py`. Doctrine/design: [entry point](https://github.com/sistema2d/framecode-vibework/blob/847cdcedc02d08531961c8367f4e2ddb2dc392f1/AGENTS.md), `README.md`, `.cursorrules`, `.windsurfrules`, `FCVW/README.md`, `FCVW/AI.md`, `FCVW/CONTEXT_MAP.md`, `FCVW/wiki/README.md`, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/skills/orchestrator/SKILL.md`, `FCVW/skills/self-improvement/SKILL.md`, `FCVW/AUTOMATION.md`, `FCVW/TESTS.md`. Reported operation: `FCVW/AI.md`, `FCVW/TESTS.md`, `TODO.md`. | No access failure encountered in the inspected checkout. No observed host/model run, external application corpus or downloaded release assets supplied: no actual adherence, real-task efficacy, token-usage or release-artifact verification conclusion. Uninspected local files are available evidence, not access gaps. |
