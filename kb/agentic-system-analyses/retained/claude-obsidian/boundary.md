---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "claude-obsidian's shipped knowledge workflows, portable core and host adapters at commit 32ac5a02c4e082e4a5628ca810776375e134708e."
run-id: AAS-2026-10-13-claude-obsidian-c5e56e25c8bb-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "32ac5a02c4e082e4a5628ca810776375e134708e"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/AgriciDaniel/claude-obsidian
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/claude-obsidian-c5e56e25c8bb/related-systems/AgriciDaniel--claude-obsidian
  revision: 32ac5a02c4e082e4a5628ca810776375e134708e
  sha256: null
---

# claude-obsidian boundary

## Boundary and evidence

This run examines how the shipped claude-obsidian package produces, admits,
maintains and reuses a user-owned Obsidian knowledge vault. Its intended use is
to characterize the package's knowledge loop and distinguish executable core
behavior from model-facing workflow instructions. The target class is
**memory/knowledge/context-engineering system**. The boundary is
**whole-system**, not just its Python transaction API or retrieval extension.
It includes the shipped skills and worker prompts that direct synthesis, the
callers that persist notes and provenance, the later query and context consumers,
and the maintenance and evaluation paths. The package does not supply the
entire agent host. SRC-1: `AGENTS.md`, `skills/wiki/SKILL.md`,
`scripts/claude-obsidian.py`, `claude_obsidian/cli.py`.

The source's own declaration supports that classification:

> claude-obsidian is a local-first Agent Skills package for building source-cited,
> compounding Obsidian knowledge bases. It also ships a Claude Code plugin adapter.
> The portable workflow is implemented in `skills/` and the standard-library
> `claude_obsidian/` core; host hooks never define knowledge behavior.
> --- `AGENTS.md`

The frozen evidence is the acquired Git repository at
`32ac5a02c4e082e4a5628ca810776375e134708e`. The checkout's HEAD was checked
against that pin; no other revision or repository supplies evidence. The
applicability cutoff is **2026-10-13**, the supplied run date, not a claim about
when every source statement was written. The overall tier is **code-grounded**:
Python and shell implementations were inspected alongside the package's
instructions and declared contracts. No target command, test, example, model
call or service was executed. Source inspection establishes implementation and
declared design, not successful operation or causal benefit in a real vault.

### Shipped loop and entry-point trace

The local plugin manifest and portable host instructions expose the skill
package. `skills/wiki/SKILL.md` routes setup, ingest, save, query, research,
lint, fold and canvas work. The script entry point imports
`claude_obsidian.cli.main`; the CLI dispatches vault selection, transaction
inspection/application/recovery, capture, lint and checkpoint operations into
the core. These are internal shipped callers, not excluded enclosing
applications. SRC-1: `.claude-plugin/plugin.json`, `skills/wiki/SKILL.md`,
`scripts/claude-obsidian.py`, `claude_obsidian/cli.py`.

Save and ingest instructions have the model read existing hot/index context
and relevant pages, draft changes and submit one operation bundle. Ingest also
proposes provenance and address/manifest updates. Its shipped worker returns
drafts and expected hashes rather than applying the transaction. The core's
`apply_bundle` expands managed requests, prepares writes, checks approval and
preconditions, writes through the journaled mutation path and restores on
failure. Initialization uses `templates/vault/` through `build_vault_bundle`;
local capture has a shipped batch caller into the same transaction core.
The boundary therefore includes both the model-facing production procedure
and the executable admission/persistence plane. It does not equate the
instructions with demonstrated model compliance. SRC-1:
`skills/save/SKILL.md`, `skills/wiki-ingest/SKILL.md`, `agents/wiki-ingest.md`,
`claude_obsidian/transaction.py`, `claude_obsidian/vault_ops.py`,
`claude_obsidian/capture.py`.

Retained content is consumed by the query skill and retrieval scripts, not
merely stored. The query procedure reads hot/index orientation, relevant pages
and provenance; its default indexed lookup requests the no-rerank path.
`scripts/retrieve.py` calls BM25, checks current chunk/page records, optionally
reranks and returns deduplicated page candidates for the caller to read.
Prefix generation may call Anthropic or a `claude -p` subprocess when egress is
enabled; reranking may call Ollama and maintain an embedding cache. Those
optional model-consuming paths are included. SRC-1:
`skills/wiki-query/SKILL.md`, `skills/wiki-retrieve/SKILL.md`,
`scripts/retrieve.py`, `scripts/contextual-prefix.py`, `scripts/rerank.py`.

The distinction between retrieval and synthesis is explicit:

> 4. The caller reads the returned pages and performs synthesis; retrieval output
>    is not itself evidence.
> --- `skills/wiki-retrieve/SKILL.md`

The lifecycle consumer is also shipped: `hooks/hooks.json` invokes the CLI's
session-start and stop commands, which call `hook_adapter`. Session-start reads
bounded hot context only after its environment opt-in and vault-selection
checks; stop inspects mutation/journal status. Host delivery of stdout into
model context is external, but the package's selection and emission code are
included. SRC-1: `hooks/hooks.json`, `claude_obsidian/cli.py`,
`claude_obsidian/hook_adapter.py`.

Maintenance includes deterministic lint and provenance checks, separately
reviewed repairs, manual extractive log folds, methodology routing, optional
retrieval rebuilding, boundary/tiling diagnostics and explicit Git
checkpointing. Evaluation includes capability contracts, deterministic sample
and skill-contract tests, CI and the model-facing release verifier. Test
source and declared gates are evidence about checks supplied, not evidence
that those checks passed in this run. SRC-1: `skills/wiki-lint/SKILL.md`,
`skills/wiki-fold/SKILL.md`, `skills/wiki-mode/SKILL.md`,
`claude_obsidian/lint_engine.py`, `claude_obsidian/checkpoint.py`,
`claude_obsidian/contracts.py`, `scripts/boundary-score.py`,
`scripts/tiling-check.py`, `Makefile`, `tests/test_distribution_vaults.py`,
`tests/test_knowledge_contracts.py`, `.github/workflows/test.yml`,
`agents/verifier.md`.

### Repository coverage

The tracked tree was enumerated at the frozen commit. Every top-level tracked
file or directory is classified below. **Included** means part of this
functional target, not that every file was read exhaustively. The inspected
scopes identify the boundary-stage traces; supporting files available but not
yet read remain eligible for later source inspection at the same pin. No
material shipped loop path was inaccessible. **Excluded** rows are deliberate
scope exclusions, not access failures. All source-dependent rows refer to
SRC-1 and use commit-relative paths.

| Top-level tracked entry | Disposition and material paths | Role and initial coverage; excluded conclusion |
|---|---|---|
| `.claude-plugin/` | Included: `plugin.json`, `marketplace.json` | Plugin entry metadata inspected in `plugin.json`; marketplace tracked presence enumerated, contents not yet inspected. No live installation success inferred. |
| `.cursor/`, `.windsurf/` | Included: `.cursor/rules/claude-obsidian.mdc`, `.windsurf/rules/claude-obsidian.md` | Host instructions inspected; they route skill discovery, hot-context reading and transaction use. |
| `.github/` | Included: `.github/workflows/test.yml`; excluded: funding, issue templates, PR template and copilot contributor guidance | CI command paths searched. Administrative surfaces are not knowledge-loop drivers; exclusion prevents assessing issue handling or contributor-assistant behavior. |
| `.gitattributes`, `.gitignore` | Included as packaging/state-boundary configuration | Tracked presence enumerated; release inclusion policy inspected in `config/release-allowlist.json`. File contents not yet inspected; no exact ignore/attribute correctness conclusion. |
| `AGENTS.md` | Included | Entire host-neutral bootstrap, retained-state conventions and mutation instructions inspected. |
| `GEMINI.md`, `ZCODE.md` | Included | Host instruction routing and transaction statements searched; full host-specific behavior not yet inspected. |
| `README.md` | Included | Entire shipped workflow, setup, requirements and capability overview inspected as declared design. |
| `WIKI.md` | Included | Root layout, source invariants, page vocabulary and syntax inspected; later detailed schema sections available, not yet inspected. |
| `Makefile` | Included | Entire deterministic test/contract entry point and setup targets inspected; tests not run. |
| `PRIVACY.md`, `SECURITY.md` | Included | Privacy and trust-policy documents identified through product and skill references; their contents not yet inspected. No independent policy audit asserted. |
| `ATTRIBUTION.md`, `CHANGELOG.md`, `CITATION.cff`, `CODEOWNERS`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE` | Excluded from functional mechanism analysis | Attribution, history, ownership, conduct, contribution and legal metadata; exclusion prevents validating lineage, historical change claims, legal permissions or governance. Their presence was enumerated. |
| `RELEASE_MANIFEST.json`, `SHA256SUMS` | Included as release evidence metadata | Presence enumerated; content and digest validity not yet inspected. No artifact-integrity or release-success finding. |
| `agents/` | Included: `wiki-ingest.md`, `wiki-lint.md`, `verifier.md` | Ingest packet/worker contract read; lint and verifier procedures inspected by headings/search and verifier body. These cover draft production, health reporting and release evaluation. |
| `assets/` | Excluded: cover, screenshots, SVG diagrams | Presentation assets are not executable state producers or consumers. Exclusion prevents judging rendered UI or diagram fidelity; no operational conclusion relies on their appearance. |
| `claude_obsidian/` | Included: `__main__.py`, `cli.py`, `vault_ops.py`, `paths.py`, `transaction.py`, `capture.py`, `ledgers.py`, `page_schema.py`, `lint_engine.py`, `checkpoint.py`, `hook_adapter.py`; also contracts, extensions, mode, package/release/gate and compatibility helpers | CLI imports/handlers traced into setup, persistence, managed metadata, recovery, capture, hook/context and checkpoint code. Lint, ledger, selection and capability functions searched; capability evaluation read. Ancillary helpers are available, not exhaustively inspected. Includes callable APIs as well as script callers. |
| `config/` | Included: `product-contract.json`, `capabilities.json`, `adapters.json`, `public-marketplace.json`, `release-allowlist.json` | Product contract and release allowlist read; capability scopes traced through contract code and skill-contract tests. Adapter/catalog contents available, not yet inspected. |
| `docs/` | Included: compound-vault, install, methodology-modes, dragonscale and Windows/WSL guides | Compound-vault loop, roles, retrieval, hooks and capture documentation inspected. Other guides identified as supporting operation contracts, not yet fully inspected. |
| `examples/` | Included: `sample-vault/` config, raw manifest, inbox marker, Obsidian config and linked source/concept/entity/question, hot/index/log/overview pages | Tree enumerated; deterministic sample caller/test inspected. Sample page bodies not yet read. Synthetic sample is a fixture, not an observed user run. |
| `hooks/` | Included: `hooks.json`, `README.md` | Hook configuration read and handlers/consumers traced. README available, not yet inspected. |
| `scripts/` | Included: `claude-obsidian.py`; setup-vault, setup-mode, setup-multi-agent, setup-retrieve, setup-dragonscale; contextual-prefix, bm25-index, retrieve, rerank; boundary-score, tiling-check; wiki-mode, detect-transport, allocate-address, wiki-lock | Wrapper read; retrieval consumer and optional model tiers read; setup/transport/mode/legacy-helper responsibility and call paths searched. Includes derived-cache writers and diagnostic consumers, not only canonical note writes. Historical benchmark helpers are absent, addressed below. |
| `skills/` | Included: all 15 skill `SKILL.md` entry points; `wiki/references/`, autoresearch program, fold template, canvas spec and methodology templates | Wiki, save, ingest, query, retrieval, lint, fold and research instructions read. Think, canvas, bases, defuddle, CLI and mode responsibilities searched; Markdown reference skill and detailed references/templates remain available for later inspection. This row includes prompt-only knowledge and maintenance behavior. |
| `templates/` | Included: `vault/` raw manifest, inbox marker, hot/index/log/overview seed and Obsidian settings/snippet | Template loader traced in `vault_ops.py`, tree enumerated and hot seed read. Deterministic initialization and lint fixture use inspected in sample tests. Other seed bodies available, not yet read. |
| `tests/` | Included: Python and shell suites and `fixtures/` for capture, contracts, forward workflows, lint, migration, release and setup | Test inventory enumerated; distribution and knowledge-contract tests inspected; historical benchmark test's missing-helper condition inspected. Test definitions support declared coverage only. Forward fixture prompts are not model execution traces. |

### External dependencies and evidence limits

Agent Skills hosts, Claude Code's scheduler/tool permissions/model calls and
Obsidian's UI, indexing and plugin behavior are external dependencies. Python
3.11+, Bash for shell paths and Git for checkpoint/release work are runtime
prerequisites. Optional Obsidian CLI/MCP/REST transports, extraction runners,
defuddle, Anthropic and Ollama services are not acquired as additional sources.
Their package-side instructions, detection, consent and integration code stay
inside the boundary. Their implementations do not. This prevents attributing
host scheduling, extraction correctness, model synthesis quality, rendered
navigation, service privacy or host permission enforcement to claude-obsidian.
SRC-1: `README.md`, `config/product-contract.json`,
`skills/wiki/SKILL.md`, `skills/wiki-cli/SKILL.md`,
`scripts/contextual-prefix.py`, `scripts/rerank.py`.

The frozen checkout is product source, not a live user vault. No user's retained
notes, actual session transcript, host delivery trace or executed evaluation
result was supplied. This limits claims about compounding knowledge quality,
retrieval effectiveness, prompt-injection resistance and operational recovery
to inspected mechanisms and intended checks. It does not remove the shipped
persist/reload/query paths from the whole-system target. SRC-1: `AGENTS.md`,
`skills/wiki-query/SKILL.md`, `hooks/hooks.json`,
`tests/test_distribution_vaults.py`.

The historical retrieval benchmark helpers `scripts/baseline-v16.py` and
`scripts/benchmark-runner.py` are not tracked in this frozen tree. The shipped
benchmark test explicitly conditions its execution on their presence, and the
release allowlist excludes them. This is unavailable historical benchmark
evidence, not an uninspected shipped driver. It prevents reproducing those
historical retrieval comparisons from this source set; no benchmark percentage
or performance improvement is established here. SRC-1:
`tests/test_benchmark_tools.py`, `config/release-allowlist.json`.

> @unittest.skipUnless(TOOLS_PRESENT, "source-only benchmark helpers are excluded")
> class BenchmarkToolTests(unittest.TestCase):
> --- `tests/test_benchmark_tools.py`

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/AgriciDaniel/claude-obsidian` | 32ac5a02c4e082e4a5628ca810776375e134708e | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/claude-obsidian-c5e56e25c8bb/related-systems/AgriciDaniel--claude-obsidian`. Tracked tree and HEAD pin inspected. Implementation: wrapper/CLI handlers, setup bundle construction, transaction admission/application/rollback and managed metadata, local capture caller, hook context/status, retrieval consumer and optional prefix/rerank model tiers, checkpoint entry and capability evaluator; scoped searches of lint, ledgers, path selection, setup/transport/mode/diagnostic helpers and CI. Doctrine/design: AGENTS, README, WIKI schema opening, compound-vault guide, core and research/maintenance/retrieval skills, ingest/verifier agents, host rules, product and release contracts. Test source: distribution and knowledge contracts plus benchmark missing-helper condition. The coverage table distinguishes inspection from available supporting material. | Implementation: [CLI](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/claude_obsidian/cli.py), [transaction](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/claude_obsidian/transaction.py), [retrieval](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/scripts/retrieve.py), [hook adapter](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/claude_obsidian/hook_adapter.py). Doctrine/design: [agent contract](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/AGENTS.md), [query](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/skills/wiki-query/SKILL.md), [product contract](https://github.com/AgriciDaniel/claude-obsidian/blob/32ac5a02c4e082e4a5628ca810776375e134708e/config/product-contract.json). All local anchors above resolve at this commit. | No access gap in the tracked shipped knowledge loop. External hosts/services and live user state are outside the source set, preventing end-to-end operational and quality conclusions. Historical benchmark helpers are absent, preventing their reproduction. Tests and manual release gates supply definitions, not observed runs or causal experiments. |
