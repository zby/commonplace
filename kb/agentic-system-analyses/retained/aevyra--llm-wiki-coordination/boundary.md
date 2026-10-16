---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Wiki Coordination's shipped wiki coordination protocols and audit tool at commit 126749634d1c8c2fd6141f59711c882c2d629699."
run-id: AAS-2026-10-14-llm-wiki-coordination-a12f3c7007f2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "126749634d1c8c2fd6141f59711c882c2d629699"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/AEVYRA/llm-wiki-coordination
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-coordination-a12f3c7007f2/related-systems/AEVYRA--llm-wiki-coordination
  revision: "126749634d1c8c2fd6141f59711c882c2d629699"
  sha256: null
---

# LLM Wiki Coordination boundary

## Boundary and evidence

The intended use is to characterize the shipped coordination layer for AI-maintained Markdown wikis: durable discussion entries, subsequent peer evaluation, closure and canon admission, revision-specific endorsements, identity continuity doctrine, and integrity maintenance. The target is an in-scope memory/knowledge/context-engineering system, not an enclosing agent runtime. Its model-dependent work is assigned to agents through protocols; its executable component is a deterministic audit CLI. SRC-1: `README.md`, `protocols/dialogue-thread-format.md`, `protocols/multi-ai-consensus.md`, `protocols/rolespace-coordination.md`, `concepts/persona-manifest-ontology.md`, `tools/llm-wiki-audit.py`.

> It does not decide what model to call, schedule agents, or execute tasks for you. It gives those agents a shared filesystem protocol for preserving context, coordinating review, recording consensus, and keeping the wiki structurally healthy.
> --- `README.md`

The boundary is **whole-system**, meaning the complete shipped coordination package, including its normative agent procedures and its audit driver, not a complete autonomous agent application. Every tracked file was inspected. The repository ships neither a adopting wiki nor a model-calling host. External agents and the user perform discussion, semantic review, file updates and approval; those responsibilities are described as protocol obligations, not implemented runtime behavior. There is no shipped caller beyond the audit CLI to trace for automatic persistence or later context injection. SRC-1: `README.md`, `protocols/integrity-audit.md`, `tools/llm-wiki-audit.py`.

The retained-content loop is included at both evidence levels: the protocols instruct agents to write entry files, read previous contributions, calculate cumulative assessments, propose canon pages, review existing consensus and invalidate endorsements after revision. The audit driver consumes wiki files and dialogue metadata, runs structural checks and prints findings, with a Hard-finding-dependent exit code. It does not implement the agents' semantic judgments or author the resulting canon. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`, `tools/llm-wiki-audit.py`.

> Any agent can calculate `current` by reading the entries.
> --- `protocols/dialogue-thread-format.md`

> When working with a document in scope:
> 1.  **Review the consensus block** to understand existing endorsements and revisions.
> --- `protocols/multi-ai-consensus.md`

>     audit.run()
>     audit.print_report(as_json=args.json)
>     sys.exit(0 if audit._summary()[HARD] == 0 else 1)
> --- `tools/llm-wiki-audit.py`

### Tracked-path coverage

All rows refer to SRC-1 at the frozen commit. “Included” establishes inspection coverage, not agreement with claims or proof of successful operation.

| Top-level tracked path | Coverage | Material paths and role | Exclusion and conclusion prevented |
|---|---|---|---|
| `README.md` | Included; fully inspected | Installation entry point, intended use, external-agent boundary, release scope and adoption instructions; points adopters to protocols and audit CLI. | None. Installation prose is not evidence of successful adoption. |
| `AGENTS.md` | Included; fully inspected | Repository-maintainer instructions, explicitly not downstream-wiki agent instructions; mentions historical `templates/` and `docs/` paths absent at this revision. | No paths silently excluded; those absent directories cannot establish shipped downstream startup prompts or templates. |
| `CHANGELOG.md` | Included; fully inspected | Release history, stated protocol repairs, historical private-use claims and deferred signatures. | No private-use traces supplied; reported use cannot establish measured reliability. Historical listings do not establish files shipped at this commit. |
| `concepts/` | Included; fully inspected | `concepts/persona-manifest-ontology.md`: persistent manifest/identity doctrine, recognition, continuity and portability limits. | None; identity doctrine does not establish observed subjectivity or continuity. |
| `protocols/` | Included; fully inspected | `protocols/dialogue-thread-format.md`: append-only persistence, metadata, closure/reopen and historical migration. `protocols/rolespace-coordination.md`: previous-entry consumption, deficit calculation and participation instructions. `protocols/multi-ai-consensus.md`: retained-page rereading, revision endorsement, stale invalidation and user-approved canon admission. `protocols/integrity-audit.md`: automated and semantic evaluation, reporting/logging, escalation and tombstones. These are the shipped agent-facing workflow instructions. | None. Semantic procedures remain doctrine unless backed by execution evidence. |
| `tools/` | Included; fully inspected | `tools/llm-wiki-audit.py`: sole executable entry point and `GenericWikiAudit` consumer; traces CLI root/layer arguments through L0–L3 dispatch, wiki traversal, link/index checks, thread/entry evaluation, consensus/crypto checks and text/JSON findings. | None; no tool execution performed, so runtime outcomes and actual adoption are unestablished. |
| `.gitignore` | Included; fully inspected | Development and local-secret ignore patterns. | None; ignore patterns do not establish security enforcement. |
| `LICENSE` | Included; fully inspected | MIT distribution terms. | None. |

External dependencies are a downstream filesystem wiki, agents capable of following the instructions, user recognition/approval, and Python with PyYAML for the audit CLI. The tool's implemented traversal assumes `wiki/` and `wiki/agents/dialogue/`; the protocol documentation allows adopter-chosen dialogue roots. The boundary includes both surfaces without assuming automatic adaptation between them. SRC-1: `README.md`, `protocols/dialogue-thread-format.md`, `protocols/multi-ai-consensus.md`, `tools/llm-wiki-audit.py`.

The frozen evidence is repository `https://github.com/AEVYRA/llm-wiki-coordination` at full commit `126749634d1c8c2fd6141f59711c882c2d629699`, applicable through the supplied run cutoff **2026-10-14**. HEAD matched the acquired revision and the checkout reported no tracked modifications. The overall tier is **code-grounded** because the audit implementation and shipped entry point are inspectable; the larger agent-operated knowledge workflow is **doctrine/design**, not an implemented orchestration loop. No target execution, provider calls, tests or dependency installation were performed.

Excluded external systems are the adopting agent runtime, provider/model implementation, private source wiki and any unshipped crystallization/signing tooling. These exclusions prevent conclusions about scheduling, automated content generation, concurrency control in a real host, retrieval into model context, operational quality, or cryptographic authenticity. The release explicitly defers cryptographic signatures and full trace-ledger implementation. No supplied observed runs or causal experiments establish downstream performance. SRC-1: `README.md`, `CHANGELOG.md`.

> - Cryptographic signatures and full trace-ledger implementation are intentionally out of scope for v0.2.0.
> --- `README.md`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/AEVYRA/llm-wiki-coordination` | 126749634d1c8c2fd6141f59711c882c2d629699 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-coordination-a12f3c7007f2/related-systems/AEVYRA--llm-wiki-coordination`. Implementation: complete `tools/llm-wiki-audit.py`, from CLI to all check methods and findings output. Doctrine/design: complete `README.md`, `AGENTS.md`, four `protocols/*.md` files, `concepts/persona-manifest-ontology.md`, `CHANGELOG.md`, `.gitignore`, `LICENSE`. Reported operation: private-use statements in `AGENTS.md` and `CHANGELOG.md`. | Implementation: [audit CLI and checker](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py). Doctrine/design: [README](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md), [thread format](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md), [RoleSpace](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/rolespace-coordination.md), [consensus](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/multi-ai-consensus.md), [integrity audit](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/integrity-audit.md), [persona manifest](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/concepts/persona-manifest-ontology.md). Reported operation: [maintainer instructions](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/AGENTS.md), [changelog](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/CHANGELOG.md). | No inaccessible tracked files or material paths left uninspected. No private wiki, execution traces, benchmark/evaluation results or causal experiments supplied. Implementation supports source-level behavior, doctrine supports intended agent duties, and reported private use supports attribution only; none establishes actual effectiveness or end-to-end enforcement. |
