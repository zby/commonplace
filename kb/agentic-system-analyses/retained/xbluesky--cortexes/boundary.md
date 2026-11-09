---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Cortexes knowledge-vault plugin and companion CLI at frozen commit 2b8e79f0099203e0453147b708346349952bb963."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/xbluesky/cortexes
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/cortexes-ce9cf1445c07/related-systems/xbluesky--cortexes
  revision: 2b8e79f0099203e0453147b708346349952bb963
  sha256: null
---

# Cortexes boundary

## Boundary and evidence

This run examines Cortexes as a shipped knowledge-vault system, not just the `cortex-vec` library or its search endpoint. Its intended use is retaining Claude Code session material, turning it into notes, maintaining related pages, and retrieving that content in later sessions. It qualifies as a memory/knowledge/context-engineering system: the retained-state loop combines executable lifecycle hooks and indexing code with model-followed writing, review and retrieval instructions (SRC-1, `hooks/hooks.json`, `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md`, `skills/cortex-query/SKILL.md`).

> A personal knowledge vault plugin for Claude Code — session recording, memory distillation, semantic retrieval.
> --- `README.md`

The boundary is whole-system at the frozen repository revision. It includes the plugin manifests, all shipped commands and skills, SessionStart and SessionEnd hooks, transcript filtering and its optional nested classifier, the deck UI, ephemeral takeoff batons, the Python CLI and its state/index maintenance, and retrieval evaluation tooling. These are complementary parts of one shipped loop, not external callers excluded because they invoke a CLI. Genesis initializes the vault and index; evolve writes retained pages; distill reviews Raw material and records outcomes; broadcast updates existing pages; query and takeoff resume supply content to later host sessions (SRC-1, `commands/genesis.md`, `skills/cortex-evolve/SKILL.md`, `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md`, `skills/cortex-query/SKILL.md`, `skills/cortex-takeoff/SKILL.md`).

> The cortex vault is the user's own knowledge base: distilled Notes,
> Projects, and Raw session records.
> --- `skills/using-cortex/SKILL.md`

Entry-point tracing found the hook manifest invoking the two shell lifecycle scripts and registering the deck module. SessionEnd invokes the transcript filter and metadata classifier, writes Raw material, optionally reclaims superseded captures and commits/pushes; SessionStart emits vault-topic metadata and menu actions that lead to retrieval, distillation or baton resume. The query command explicitly routes into the query skill, which searches and then reads selected pages. The Python console script routes indexing/search to `store`, maintenance commands to their modules, and evaluation to `eval.run` (SRC-1, `hooks/hooks.json`, `hooks/scripts/session-end-record.sh`, `hooks/scripts/session-start-inject.sh`, `hooks/deck.tsx`, `commands/query.md`, `cortex-vec/pyproject.toml`, `cortex-vec/src/cortex_vec/cli.py`). These traces establish coverage of production, maintenance, admission and later consumption at the boundary level; they do not establish successful execution or model compliance.

> If multiple matches, list them and ask which one to read
> --- `skills/cortex-query/SKILL.md`

> Read the target page's full content.
> --- `skills/cortex-broadcast/SKILL.md`

The target depends on Claude Code for model execution, tool permissions, lifecycle events, transcript production and the deck engine API. Its filter also invokes the Claude CLI; the companion store uses ChromaDB and OpenAI embedding/summary services, with local lexical retrieval support. Filesystem, Git, shell utilities, Python and the declared Python dependencies are environmental dependencies, not separately frozen implementations. Human decisions specified by the skills are part of the system's prescribed operation, not evidence that those decisions occurred (SRC-1, `hooks/scripts/filter-transcript.py`, `hooks/deck.tsx`, `cortex-vec/src/cortex_vec/store.py`, `cortex-vec/pyproject.toml`, `skills/cortex-distill/SKILL.md`).

The reviewed boundary is commit `2b8e79f0099203e0453147b708346349952bb963`; the applicability cutoff is 2026-11-08. The overall evidence tier is code-grounded. Skill text supplies doctrine/design, not executable guarantees. No target code, tests, examples or provider calls were executed. No private vault, host implementation, real-session trace or evaluation run artifact was supplied. These gaps prevent conclusions about deployed reliability, actual agent adherence, retrieval quality on a user's corpus, or causal benefit. They do not remove the shipped evaluators or prompt-driven maintenance from scope. Later revisions, the data branch described by the README, live website content and externally linked issue discussions are outside the frozen evidence; this prevents characterizing their current contents or operation (SRC-1, `README.md`, `cortex-vec/src/cortex_vec/eval/run.py`).

### Top-level coverage

The tracked tree was enumerated at the frozen commit. Included means within the analysis boundary, not that every file has already been read. Initial inspection traced all principal state-loop entry points above. Where only selected files or ranges were inspected, remaining material stays included and available for later source inspection; it is not an access gap.

| Top-level tracked paths | Status and role | Initial inspection and limits |
|---|---|---|
| `.claude-plugin/` | Included: plugin and marketplace registration | `plugin.json` inspected; marketplace manifest tree-listed, not yet read. |
| `commands/` | Included: user command entry points for genesis, evolve, distill, query, broadcast and takeoff | Genesis and query read; remaining wrappers tree-listed; their destination skills read. |
| `skills/` | Included: all six shipped skills, including `using-cortex` routing | All skill files read; covers writing, admission, maintenance, retrieval and baton consumption instructions. |
| `hooks/` | Included: `hooks.json`, `deck.tsx`, `deck-core.ts`, module tests, lifecycle shell scripts, takeoff helper, `lib/`, transcript filtering, `rtk_cmd/`, TOML filters, metadata and diagnostic helpers | Manifest, lifecycle scripts and deck module read; classifier function and takeoff helper opening inspected. Remaining implementation and tests tree-listed, not yet inspected in detail. |
| `cortex-vec/` | Included: packaging, CLI, store, parser/config, BM25/fusion/graph/rerank, Raw navigation and distill-plan/queue/reclaim modules, evaluation and tests | Packaging and CLI read; store setup/summary/search and `eval/run.py` inspected. Remaining modules and test files tree-listed, not yet inspected in detail. No evaluation results inferred from evaluator availability. |
| `tests/` | Included: plugin regression and prompt-contract tests | Query-skill contract opening inspected; capture, filtering, lifecycle, privacy, command and takeoff suites tree-listed. Tests supply assertions, not an observed passing run. |
| `types/` | Included: deck/host interface declarations in `index.d.ts` | Tree-listed; deck consumer inspected, declaration details not yet read. |
| `docs/` | Included: `index-audit.md` and branding image | Tree-listed; audit linked by inspected README/genesis, not yet read. No audit conclusions adopted. |
| `scripts/` | Included: `run-checks.sh` and `raw-map-corpus-check.py` | Check driver read; corpus-check helper tree-listed. No checks executed. |
| `README.md`, `README.zh-TW.md`, `PRIVACY.md`, `PRIVACY.zh-TW.md`, `CHANGELOG.md` | Included: use, data-flow contracts and reported history | English README read; other files tree-listed, not yet read. Historical claims remain attributed declarations unless independently supported. |
| `.github/` | Included: CI, release/site workflows and contribution templates | Tree-listed, not yet read; no CI success inferred. |
| `.cc-marketspec/` | Excluded: presentation catalog and marketplace overlays | Tree-listed. Prevents assessing catalog-generation correctness; plugin runtime manifest remains included. |
| `site/` | Excluded: static public website generator, assets and renderer tests | `site/README.md` read for role, rest tree-listed. Prevents assessing published-site fidelity or deployment success, not vault operation. |
| `package.json`, `package-lock.json` | Excluded: website/marketplace build dependencies | `package.json` read; lockfile tree-listed. Prevents assessing build dependency integrity; Python runtime packaging remains included. |
| `.gitignore`, `.pre-commit-config.yaml`, `ruff.toml` | Included: repository hygiene and development checks | Tree-listed; referenced check driver read, configuration details not yet inspected. No lint/compliance result claimed. |
| `LICENSE`, `NOTICE`, `CODE_OF_CONDUCT.md`, `CODE_OF_CONDUCT.zh-TW.md`, `CONTRIBUTING.md`, `CONTRIBUTING.zh-TW.md`, `SECURITY.md`, `SECURITY.zh-TW.md` | Excluded: legal, community and contribution/security reporting policy | Tree-listed. Prevents conclusions about legal compliance, contributor governance or security-response practice; operational security behavior remains in included code and privacy contracts. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/xbluesky/cortexes` | 2b8e79f0099203e0453147b708346349952bb963 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/cortexes-ce9cf1445c07/related-systems/xbluesky--cortexes`. Implementation: hook wiring, lifecycle scripts, deck module, filter classifier, takeoff helper opening, CLI dispatcher, store setup/summary/search, evaluation runner and query-skill test opening. Doctrine/design: README, plugin manifest, genesis/query commands, all six skills, Python packaging, check driver and site role documentation. Complete tracked tree enumerated; detailed initial coverage above. | Implementation: [hook wiring](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/hooks/hooks.json), [CLI](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/cortex-vec/src/cortex_vec/cli.py), [evaluator](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/cortex-vec/src/cortex_vec/eval/run.py). Doctrine/design: [distill](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/skills/cortex-distill/SKILL.md), [query](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/skills/cortex-query/SKILL.md), [README](https://github.com/xbluesky/cortexes/blob/2b8e79f0099203e0453147b708346349952bb963/README.md). | No checkout access gap encountered. Host/provider implementations, private vaults and observed execution/evaluation evidence absent: cannot establish actual model behavior, real-corpus performance, deployment correctness or causal gains. Source-native reports are attributable claims, not observed runs. |
