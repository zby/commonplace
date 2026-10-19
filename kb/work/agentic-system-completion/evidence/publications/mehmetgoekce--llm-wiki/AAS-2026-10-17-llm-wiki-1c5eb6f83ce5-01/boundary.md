---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-wiki's complete shipped knowledge-maintenance skill, plugin packaging and wiki scaffolding at commit 11538c1195666db24e25e23cc64bb1d70587aef9."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
analysis-cutoff: "2026-10-17"
evidence-tier: doc-grounded
source:
  identity: https://github.com/MehmetGoekce/llm-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-mehmetgoekce--llm-wiki/related-systems/MehmetGoekce--llm-wiki
  revision: "11538c1195666db24e25e23cc64bb1d70587aef9"
  sha256: null
---

# llm-wiki boundary

## Boundary and evidence

llm-wiki is an in-scope memory/knowledge/context-engineering system for maintaining a personal or team wiki through Claude Code. Its whole-system boundary includes the shipped plugin and copied-command entry paths, wiki initialization, schema and page templates, and the agent instructions for ingest, import, retrieval, access logging, pruning, L1 rule verification, lint and status. These paths jointly specify how retained knowledge is produced, admitted, maintained and later consumed. The boundary is not limited to the initialization library or shell scripts (SRC-1, `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`, `.claude-plugin/plugin.json`).

The classification follows the shipped maintainer role rather than an assumption that this repository owns an agent runtime:

> Wiki maintainer for a personal or team knowledge base. You process source material and distribute extracted knowledge across wiki pages, maintain cross-references, and ensure structural integrity.
> --- `SKILL.md`

The plugin's marketplace entry points at the repository root; its manifest supplies the required wiki-root directory configuration. The root skill consumes that setting and dispatches its subcommands. The alternate `setup.sh` calls the same initialization script and optionally copies `SKILL.md` into a project's `.claude/commands/wiki.md`, replacing plugin placeholders with filesystem paths. The root `wiki.md` is a migration pointer, not a second maintained command implementation (SRC-1, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `SKILL.md`, `setup.sh`, `wiki.md`).

The setup consumer is explicit:

> One-time. Creates the wiki skeleton in the wiki root. Pages and the config file are created by a
> script; you collect the answers and run it. Do not create or edit wiki pages yourself.
> --- `SKILL.md`

Initialization reads the selected tool's Schema, Dashboard, Hub and Access-Log templates and writes missing pages plus `llm-wiki.yml`; subsequent skill commands read that configuration and the generated schema. Ingest maintains pages and routing lines; query reloads selected retained pages, synthesizes an answer and appends access records; prune consumes those records; lint supplies the shipped quality-check procedure. These are instructions for the host agent, not independently executable implementations of those maintenance algorithms (SRC-1, `scripts/init-wiki.sh`, `templates/logseq/Schema.md`, `templates/obsidian/Schema.md`, `SKILL.md`).

> Phase 1 - Targeted Read (Stage 2, only the chosen pages):
>   - Read ONLY the 3-5 pages chosen in Phase 0 (max 3 loaded simultaneously, JIT — batch if needed)
> --- `SKILL.md`

The immutable evidence is the acquired Git repository at `11538c1195666db24e25e23cc64bb1d70587aef9`, with an applicability cutoff of 2026-10-17. HEAD matched that pin and the checkout had no reported changes at inspection. The overall tier is **doc-grounded**: the central knowledge loop is a model-consumed prompt contract. The executable initialization and installation paths supply a narrower implementation layer. No target execution, provider call or independent experiment was performed; source inspection cannot establish actual compliance, retrieval accuracy, safety or sustained operating quality.

### Functional exclusions and dependencies

Claude Code supplies model execution, tool access, plugin loading and automatic L1 memory loading. Those external host implementations are not frozen here, so their loading guarantees, permission enforcement and actual model behavior cannot be established. llm-wiki's instructions for consulting and modifying a configured L1 directory remain included. In particular, the source disclaims an action-time freshness gate (SRC-1, `SKILL.md`):

> Out of scope: warning at the moment a due rule is about to justify an action. Claude Code loads L1, not
> llm-wiki — there is no hook to enforce that gate, so do not claim one.
> --- `SKILL.md`

Logseq and Obsidian are external storage/UI consumers; their implementations and link resolution behavior are not inspected. Git, Bash and Python provide local execution and persistence facilities. User confirmation and any periodic scheduler are external inputs, not autonomous services shipped by the target. User wiki contents, actual L1 memory files, URL sources passed to ingest, external inspiration links and external release services are not captured. Accordingly, this boundary supports the shipped format and workflow contracts, not compatibility demonstrated in a real vault, actual memory loading, deployed scheduling, ingested fact correctness or the security of real credentials (SRC-1, `README.md`, `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`).

### Top-level coverage

The tracked tree was enumerated at the frozen commit. “Included; not initially inspected” below denotes available supporting evidence, not an access gap or a missing operational path. All shipped operational entry paths, generated-state templates and maintenance/consumption instructions were inspected. The source register covers the repository at the pin; later jobs may inspect its remaining supporting documents without adding a source.

| Top-level tracked path | Status and material paths | Role and limits |
|---|---|---|
| `.claude-plugin/` | Included; `plugin.json` and `marketplace.json` inspected; `icon.png` deliberately excluded | Plugin identity, root source and wiki-path configuration. Icon exclusion prevents visual-branding assessment only. SRC-1, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`. |
| `.github/` | Excluded; issue templates, pull-request template and `SECURITY.md` | Repository collaboration and reporting metadata, not the knowledge loop. No conclusion about contribution triage or security-report handling. |
| `.gitignore` | Excluded | Development-checkout ignore policy; not the generated wiki ignore rules, which are inspected in the initializer. No conclusion about repository development hygiene. |
| `CHANGELOG.md` | Included; not initially inspected | Available release history; no historical evolution claim established here. |
| `CONTRIBUTING.md` | Excluded | Contributor workflow. No conclusion about development governance. |
| `LICENSE` | Excluded | Legal terms; no legal interpretation supplied. |
| `README.md` | Included; inspected | Installation, supported entry paths, command account, architecture and attributed privacy/operation claims. SRC-1, `README.md`. |
| `SECURITY.md` | Included; not initially inspected | Available security policy; no security-policy assessment established here. |
| `SKILL.md` | Included; inspected in full | Main model-consumed command dispatcher; production, admission checks, reload, synthesis, access feedback, L1/L2 maintenance, confirmation and commit instructions. Includes lint/status evaluation procedures, not an independent evaluator executable. SRC-1, `SKILL.md`. |
| `config.example.yml` | Included; inspected | Example paths, namespaces and L1 verification interval. SRC-1, `config.example.yml`. |
| `diagrams/` | Included; `ingest-flow.mmd`, `l1-l2-architecture.mmd`, `query-routing.mmd` not initially inspected | Supporting design diagrams; no separate operational implementation attributed to them. |
| `docs/` | Included text: `faq.md`, `l1-l2-architecture.md`, `logseq-vs-obsidian.md`, `schema-reference.md`, `troubleshooting.md`; not initially inspected. `graph-view.png` deliberately excluded | Supporting design, format and operating documentation remains available. Screenshot exclusion prevents treating that image as observed operating evidence. |
| `examples/` | Included; `before-after.md`, `l1-memory-examples.md` not initially inspected | Illustrative retained content and L1 forms, not yet assessed as examples or execution evidence. |
| `openspec/` | Included; `AGENTS.md`, `project.md`, current `specs/{config,ingest,l1-l2-routing,lint,plugin,prune,query,schema,setup}.md` and archived plugin-packaging change documents not initially inspected | Available normative/design and change records; no conformance or completed-task claim inferred from their presence. No separate executable evaluator or caller appeared in the tracked tree. |
| `scripts/` | Included; `init-wiki.sh` inspected in full | Shared non-interactive initializer: template loading, missing-file creation, config creation, optional Git init and commit. SRC-1, `scripts/init-wiki.sh`. |
| `setup.sh` | Included; inspected in full | Interactive shipped driver, existing-config handling, initializer invocation and copied-skill installation. It is part of the system, not an excluded caller. SRC-1, `setup.sh`. |
| `templates/` | Included; both `logseq/` and `obsidian/` versions of `Schema.md`, `Dashboard.md`, `Hub.md`, `Access-Log.md` inspected | Persisted schema and initial routing, health and access-log state consumed by the main skill. SRC-1, `templates/logseq/Schema.md`, `templates/logseq/Hub.md`, `templates/logseq/Dashboard.md`, `templates/logseq/Access-Log.md`, `templates/obsidian/Schema.md`, `templates/obsidian/Hub.md`, `templates/obsidian/Dashboard.md`, `templates/obsidian/Access-Log.md`. |
| `wiki.md` | Included; inspected | Legacy-location pointer to root skill, not a separate live loop. SRC-1, `wiki.md`. |

No inaccessible material shipped operational path was identified. Available supporting files not initially read must be inspected before making claims specific to them; their availability is not itself corroboration of the main skill's claims.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/MehmetGoekce/llm-wiki` | 11538c1195666db24e25e23cc64bb1d70587aef9 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-mehmetgoekce--llm-wiki/related-systems/MehmetGoekce--llm-wiki`. Implementation: complete `setup.sh`, `scripts/init-wiki.sh`, plugin manifests and all eight templates. Doctrine/design: complete `SKILL.md`, `config.example.yml`, `wiki.md`, `README.md`, manifests and templates. Reported operation: README's attributed setup/testing and operating account only. Tracked-tree enumeration covers all paths; remaining supporting text is available but not initially inspected as detailed above. | Implementation: [setup driver](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/setup.sh), [initializer](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/scripts/init-wiki.sh), [manifest](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/.claude-plugin/plugin.json). Doctrine/design: [skill](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/SKILL.md), [Logseq schema](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/templates/logseq/Schema.md), [Obsidian schema](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/templates/obsidian/Schema.md). Reported operation: [README](https://github.com/MehmetGoekce/llm-wiki/blob/11538c1195666db24e25e23cc64bb1d70587aef9/README.md). | No checkout access gap identified. External host, UI and user-state implementations are outside this frozen source. No inspected execution trace or causal experiment: actual host integration, instruction compliance and effectiveness remain unestablished. Reported operation is attribution, not observed execution. |
