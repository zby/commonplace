---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Link's local agent memory and wiki system at frozen commit cc92f3632121b04063b24eaaf3a8c5429eaf2b57."
run-id: AAS-2026-10-14-link-595f6f9cba36-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/gowtham0992/link
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/link-595f6f9cba36/related-systems/gowtham0992--link
  revision: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
  sha256: null
---

# Link boundary

## Boundary and evidence

This run analyses Link as a local memory, knowledge and context-engineering system for AI agents, not as an enclosing agent runtime. Its intended use is to retain user context and source-backed wiki knowledge in local Markdown, then return bounded context across agent sessions. The frozen target includes the shipped callers and instructions, not just the `link_core` library. SRC-1, `README.md`, `ARCHITECTURE.md`, `LINK.md`, `mcp_package/pyproject.toml`.

> Link is an open-source memory layer for local AI agents. Raw sources become an
> inspectable Markdown wiki. Explicit "remember this" requests become reviewable
> memories. Agents retrieve compact, source-backed context through the CLI, MCP,
> official skills, or the local viewer without dumping the whole wiki into a chat
> window.
> --- `README.md`

The whole-system boundary includes raw capture and proposal production; explicit memory admission and lifecycle operations; agent-authored and structured wiki ingestion; project seeding; persistence, indexes and retrieval; session hooks and handoffs; maintenance, backup, sync and sharing; CLI, MCP, local HTTP and LinkBar consumers; shipped agent steering and skills; and evaluation code and reported results. The agent-authored wiki path is a shipped procedure executed by an external model-driven agent, not an autonomous compiler inside Link. SRC-1, `LINK.md`, `link.py`, `serve.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/structured_ingest.py`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`.

> Use the agent-authored path below for arbitrary notes, articles, conversations,
> images, and unsupported formats. `ingest-status` reports representation and
> staleness; it does not itself compile those sources into wiki pages.
> --- `LINK.md`

Initial tracing establishes both production and later consumption of retained state. The package ships `lnk` through the root CLI and `link-mcp` through the MCP server. `write_memory_page` writes Markdown with `review_status: pending`, updates the index and optionally rebuilds backlinks; `memory_records` reloads Markdown from `wiki/memories/`. The CLI's session-end hook filters proposals before storing captures, while its session-start hook builds a memory brief and prepends pending handoffs. MCP `remember` delegates to the write path and `recall` returns briefs, focused memories or query packets. LinkBar is a shipped caller: it invokes the CLI for recall, remember, review, archive and capture acceptance. The HTTP server also has mutation routes; the architecture document's description of a “read-only web viewer” is not used to exclude those routes. SRC-1, `mcp_package/pyproject.toml`, `mcp_package/link_core/memory.py`, `link.py`, `mcp_package/link_mcp/server.py`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`, `serve.py`.

>     for path in sorted(memories_dir.rglob("*.md")):
>         if path.name.startswith("."):
>             continue
>         records.append(memory_record_from_page(wiki_dir, path, include_body=include_body))
> --- `mcp_package/link_core/memory.py`

>     /// Accept a session capture proposal into the reviewed memory flow.
>     func acceptCapture(_ capture: CaptureItem, index: Int = 1) {
>         act(["accept-capture", capture.path, LinkCLI.workspace, "--index", "\(index)"],
>             success: "Accepted \u{2014} now pending your review.")
>     }
> --- `apps/LinkBar/Sources/LinkBar/LinkStore.swift`

Approval is part of the shipped agent contract and user interaction, not an independently authenticated approval token established by this boundary. In particular, MCP `remember` tells its caller to use it only for user-approved memories; this instruction must not be mistaken for evidence that every actual caller obeys it. SRC-1, `mcp_package/link_mcp/server.py`, `skills/link-memory/SKILL.md`.

>     Use only when the user asks Link to remember something or approves a memory
>     proposal. Duplicate and conflict candidates should be resolved by updating,
>     reviewing, or archiving existing memory instead of forcing a new page.
> --- `mcp_package/link_mcp/server.py`

### Dependencies and exclusions

External agent hosts, their model providers, user decisions and live transcripts are outside the frozen source. Link's steering, installers, hook logic and MCP interfaces are included, but the host's model calls, instruction adherence, session scheduling and final answers are not attributed to Link. This prevents conclusions about actual cross-agent compliance or end-to-end user outcomes from source inspection alone. Optional local embedding and reranking dependencies are declared in the package; their implementation and model weights are not frozen here, preventing independent assessment of those external models. Git remotes and package distribution services are external dependencies for explicit sync or installation, not inspected services. SRC-1, `integrations/claude-code/install.sh`, `integrations/_shared/link-instructions.md`, `mcp_package/pyproject.toml`, `mcp_package/link_core/semantic.py`, `mcp_package/link_core/sync.py`.

The source is the acquired checkout at full commit `cc92f3632121b04063b24eaaf3a8c5429eaf2b57`; HEAD was verified against that pin. The applicability cutoff is the supplied run date, 2026-10-14. No later repository state, live documentation, third-party repository or actual installed workspace supplies evidence. No target execution, tests or benchmarks were run. Implementation inspection supports a code-grounded boundary, not observed operation or causal effects.

Published benchmark results remain attributed reports. The end-to-end QA section says its adapter and judgments live in a separate benchmark workspace; those artifacts are not supplied by this frozen repository inspection. This prevents independently checking its end-to-end scores, judge conditions and causal attribution. The shipped recall evaluator and dataset remain in scope for subsequent code analysis, but no reproduction is claimed. SRC-1, `benchmarks/RESULTS.md`, `scripts/eval_recall_quality.py`.

> Full provenance notes,
> the Link backend adapter, and every judgment live in our benchmark
> workspace; config: top-50 memories per answer (single cutoff),
> claude-haiku-4-5 as answerer and judge, ~2.7k mean tokens per answer
> call, zero LLM calls and zero cost at ingest.
> --- `benchmarks/RESULTS.md`

### Top-level coverage

Included means within the functional evidence boundary, not that every line has already been inspected. The initial inspection mapped material responsibilities through the tree, entry points, selected implementations and instructions. Unread auxiliary files remain available at this same commit; they are not access gaps or silently excluded parts of the loop.

| Top-level tracked path | Status | Role and initial inspection | Exclusion limit or remaining inspection |
|---|---|---|---|
| `.github/` | Included | CI and contribution templates; read CI test/build steps in `.github/workflows/ci.yml`. | Remaining workflow steps and templates not yet inspected; no successful CI execution inferred. |
| `.gitignore` | Included | Workspace/repository retention configuration, located in tree. | Contents not yet inspected. |
| `.linkignore` | Included | Shipped ingest exclusion configuration, identified in package force-includes. | Contents not yet inspected. |
| `.mailmap` | Excluded | Contributor identity normalization. | No author-identity audit. |
| `ARCHITECTURE.md` | Included | Read complete component map, schema, write/recall paths and declared invariants. | Doctrine is not proof of every implementation claim. |
| `CHANGELOG.md` | Included | Release history in frozen tree. | Not yet inspected; no historical behavior inferred. |
| `CONTRIBUTING.md` | Included | Maintainer procedure. | Not yet inspected; no contribution-process assessment. |
| `LICENSE` | Excluded | Legal terms. | No legal/licensing assessment. |
| `LINK.md` | Included | Read remember, ingest, query and lint protocols; templates, research, API and remaining conventions located by headings. | Remaining sections available for later inspection. |
| `README.md` | Included | Read purpose, quick start and functional moves. | Remaining documentation not yet inspected. |
| `SECURITY.md` | Included | Security contract in frozen tree. | Not yet inspected; no complete threat-model assessment. |
| `apps/` | Included | `LinkBar/Sources/LinkBar/LinkCLI.swift` bridge located; `LinkStore.swift` recall/write/review/accept implementations read. UI, notification, model and package paths located. | Other Swift bodies and bundle scripts not yet inspected; no macOS execution evidence. |
| `benchmarks/` | Included | `RESULTS.md` sections located; end-to-end QA and limitations read. | Attributed results only; external benchmark workspace unavailable. |
| `docs/` | Included | API, CLI, concepts, memory contract, security, skills and UI pages; demo snapshot/pages; structured-ingest specs and media located. | Bodies not yet inspected; visual assets are illustrations, not execution traces. |
| `integrations/` | Included | Shared global steering and Claude Code installer read; scaffold references traced. Other host installers/uninstallers and project steering located. | Host-specific variants not yet inspected; no installed-host behavior inferred. |
| `link.py` | Included | CLI command/dispatch map searched; memory wrappers, capture acceptance, session hooks, retrieval and maintenance entry points located; session-start and proposal filtering read. | Other handlers available for subsequent inspection. |
| `logo.svg` | Excluded | Branding. | No visual-design assessment. |
| `mcp_package/` | Included | `pyproject.toml` read; `link_mcp/server.py` recall/remember/ingest read; core memory reload/write, structured ingest apply, semantic setup contract and sync scope read. Capture, project seed, handoff, consolidation, journal, backup, team sync and web modules mapped. | Other implementation bodies and package build details remain to inspect; this is not a complete code audit. |
| `mypy.ini` | Included | Static-analysis configuration located. | Not yet inspected; no typing-quality result inferred. |
| `packaging/` | Included | Homebrew formula, LinkBar cask/release guidance located. | Not yet inspected; no distribution reproducibility claim. |
| `pyproject.toml` | Included | Development tooling configuration searched. | Full contents not yet inspected. |
| `raw/` | Included | Tracked `.gitkeep` only: empty source-storage scaffold. | No real user sources or capture history supplied. |
| `scripts/` | Included | Recall evaluator imports/modes/metrics read; LoCoMo evaluator and hygiene, poisoning, salience, staleness, token economics, smoke, release and contract guards located. | Other bodies not yet inspected; no measured execution asserted. |
| `serve.py` | Included | State reload, query and maintenance routes searched; remember/update/review/archive/restore POST dispatch read. | Other server and security bodies remain to inspect. |
| `skills/` | Included | All four `SKILL.md` files read: memory, ingest, retrieve and health. | Instructions establish required agent behavior, not compliance. |
| `tests/` | Included | `test_memory_core.py` imports and fixture-based test entry read; subsystem and MCP harness files located. | Other tests not yet inspected or run; tests are executable specifications, not retained successful runs. |
| `wiki/` | Included | Index, log, backlinks and category scaffolds located, including memories and source pages. | Contents not yet inspected; no deployed knowledge corpus inferred. |

All coverage entries refer to SRC-1 at the reviewed commit. The source register's inspected paths document initial inspection rather than restricting later analysts to those paths.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/gowtham0992/link` | cc92f3632121b04063b24eaaf3a8c5429eaf2b57 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/link-595f6f9cba36/related-systems/gowtham0992--link`. Full tracked tree enumerated and HEAD verified. Implementation: selected sections of `link.py`, `serve.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/memory.py`, `mcp_package/link_core/structured_ingest.py`, `mcp_package/link_core/semantic.py`, `mcp_package/link_core/sync.py`, `apps/LinkBar/Sources/LinkBar/LinkStore.swift`, `integrations/claude-code/install.sh`, `scripts/eval_recall_quality.py`, `tests/test_memory_core.py`, `.github/workflows/ci.yml`; symbol/entry-point searches additionally mapped core maintenance, seed, handoff and sync paths. Doctrine/design: complete `ARCHITECTURE.md`, all four skills, shared global steering, package metadata; selected `README.md` and `LINK.md` sections. Reported operation: selected `benchmarks/RESULTS.md` QA and limitations sections. | Implementation: [memory persistence/reload](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/mcp_package/link_core/memory.py), [CLI/hooks](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/link.py), [MCP](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/mcp_package/link_mcp/server.py), [HTTP](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/serve.py), [LinkBar consumer](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/apps/LinkBar/Sources/LinkBar/LinkStore.swift). Doctrine/design: [architecture](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/ARCHITECTURE.md), [agent wiki procedure](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/LINK.md), [memory skill](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/skills/link-memory/SKILL.md). Reported operation: [benchmark report](https://github.com/gowtham0992/link/blob/cc92f3632121b04063b24eaaf3a8c5429eaf2b57/benchmarks/RESULTS.md). | Frozen repository available; no known repository access gap. External agent runtimes, model weights, live user state and the separately described benchmark workspace are not supplied. No observed run or causal experiment registered: actual compliance, production effectiveness and independent benchmark verification are not established. |
