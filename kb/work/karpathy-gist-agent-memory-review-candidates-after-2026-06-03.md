# Agent Memory Review Candidates from Karpathy LLM Wiki Comments After 2026-06-03

Created: 2026-06-18T13:26:05Z

Source: comments on Andrej Karpathy's LLM Wiki gist, fetched via the GitHub gist comments API across 20 pages on 2026-06-18.

Original cutoff: 2026-06-03T12:09:23Z, from [karpathy-gist-agent-memory-review-candidates.md](./karpathy-gist-agent-memory-review-candidates.md).

Fetch endpoint pattern:

```text
https://api.github.com/gists/442a6bf555914893e9891c11519de94f/comments?per_page=100&page=N
```

Fetch result:

```text
total comments: 901
post-cutoff comments: 34
post-cutoff range: 2026-06-03T18:27:19Z through 2026-06-18T13:26:05Z
```

This is a second workshop triage list, not a review. It applies the same screen as the original triage list: prioritize systems that implement durable memory, wiki compilation, agent-facing read-back, lifecycle governance, provenance, contradiction handling, security boundaries, or multi-agent coordination. De-prioritize pure context preprocessors, narrow demos, source-capture helpers, generic note apps, and comments without stable inspectable sources.

## Review Now

| Candidate | Source comment | Why it belongs in the review queue | First inspection question |
|---|---|---|---|
| [Synto](https://github.com/kytmanov/synto) | [comment 6181761](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6181761#gistcomment-6181761), [comment 6199498](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6199498#gistcomment-6199498) | Local-first Markdown/Obsidian wiki with no vector DB, local model support, concept rename/merge/split, stable concept identity, curation tools, and MCP serving. | Are concept identity, merge/split state, and inbound link migrations enforced by durable schema/code or only by command convention? |
| [LLM-WIKI-MCP](https://github.com/Electro-resonance/LLM-WIKI-MCP) | [comment 6183384](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6183384#gistcomment-6183384) | MCP-accessible wiki with provenance-aware ingestion, recursive conversational memory, self-maintaining notes, runtime introspection, and agent-callable maintenance tools. | What is canonical memory: wiki pages, sidecar notes, MCP state, or derived indexes? |
| [LLM-Wiki-v3](https://github.com/vvvvvivekkk/LLM-Wiki-v3) | [comment 6185820](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6185820#gistcomment-6185820) | Markdown+Git source of truth, disposable BM25/vector/graph indexes, source/span/timestamp provenance, supersession rather than deletion, gated autonomous writes, and audit trails. | Which gates prevent autonomous writes from becoming canonical, and are they deterministic, LLM-judged, or human-approved? |
| [memwiki](https://github.com/hereisSwapnil/memwiki) | [comment 6190759](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6190759#gistcomment-6190759) | Project-local persistent memory for coding agents using `.memory/`, `hot.md`, `log.md`, agent hook files, and domain pages. Directly addresses cross-session coding-agent amnesia. | What artifacts are loaded automatically by each supported agent, and how are stale or duplicated project facts corrected? |
| [llmwiki-marimo](https://github.com/Clod/llmwiki-marimo) | [comment 6192749](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6192749#gistcomment-6192749) | Local-first Marimo + SQLite LLM Wiki that generates persistent Markdown pages, keeps document/chunk/FTS/citation state in SQLite, exposes a chat agent that reads wiki pages before raw chunks, and has human-in-the-loop answer promotion. | What is canonical memory: generated Markdown pages, SQLite rows, citation graph state, or the local wiki git history, and which parts can change future agent behavior? |
| [Link](https://github.com/gowtham0992/link) | [comment 6199251](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6199251#gistcomment-6199251) | Local, source-backed memory for AI agents with CLI, MCP support, and official CLI skills for lazy-loaded workflows. | What is the source-backed memory schema, and how do CLI skills or MCP calls select what enters agent context? |
| [EchoesVault](https://github.com/psinetron/echoes-vault-opencode) | [comment 6202181](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6202181#gistcomment-6202181) | Persistent memory plugin for OpenCode with Markdown memory, event-driven logging, OKF structure, Obsidian-native vault, and surgical index updates. | Are event-driven memory writes triggered and constrained by OpenCode hooks, explicit skills, or model instructions? |
| [Smriti-MCP](https://github.com/deepak-bhardwaj-ps/smriti-mcp) | [comment 6202957](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6202957#gistcomment-6202957) | MCP-native portable memory service meant to persist across sessions, tools, models, and runtimes. Strong fit for cross-agent read-back and memory authority questions. | What memory operations are available through MCP, and what governance separates remembered facts from retrieved context? |
| [Eidetic](https://github.com/LARIkoz/eidetic) | [comment 6205516](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6205516#gistcomment-6205516) | Claude Code memory with compounding pages, schema contract, typed pages, op-log, session-end auto-extraction, and drift detection based on stale-age, broken links, and confidence escalation. | Does drift detection produce advisory reports, retrieval penalties, or write-time gates? |
| [OKF Harness](https://github.com/pumblus/okf-harness) | [comment 6206100](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6206100#gistcomment-6206100) | Portable agent-maintainable wiki with local folders, immutable raw sources, OKF-compatible Markdown, JSON CLI for Claude Code or Codex, bounded reads, validation, citations, and graph report. | Which maintenance invariants are validated mechanically, and which remain agent instructions? |

## Review Later

| Candidate | Source comment | Reason to keep on deck |
|---|---|---|
| Knolo Wiki Librarian Skill | [comment 6184352](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6184352#gistcomment-6184352) | Product implementation of raw sources -> generated wiki -> schema assistant with ingest/query/lint loop and scheduled lint agent, but no public inspectable source was found. Review only if a stable public source, docs page, export, or reproducible demo appears. |
| [Matryca Plumber](https://github.com/MarcoPorcellato/matryca-plumber) | [comment 6199277](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6199277#gistcomment-6199277) | Relevant to safe concurrent note mutation via block AST, optimistic concurrency control, MCP, and CLI. From the comment alone, it is more a write-safety substrate than a full memory system. |
| [ContextSlice](https://github.com/llcortex/ContextSlice.git) | [comment 6184540](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6184540#gistcomment-6184540) | Context preprocessor for coding agents. Relevant to context engineering, but not clearly a durable memory system. |
| [FrameCode-VibeWork](https://github.com/Sistema2D/FrameCode-VibeWork) | [comment 6186108](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6186108#gistcomment-6186108) | Real document-framework/executable-spec candidate. Keep on deck until a review decides whether its operational `AGENTS.md` and Markdown framework are an agent-memory system, a context-engineering framework, or outside this collection's scope. |

## Already Covered or Check Before Duplicating

These appeared in the post-cutoff comments but were already in the 2026-06-03 triage list or already reviewed:

- [Mnemosyne / IsaacCLupus mnemosyn spec](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec) — already listed as review-later in the first triage file.
- [Dense-Mem](https://github.com/markhuangai/dense-mem) — already listed and reviewed as `kb/agent-memory-systems/reviews/dense-mem.md`.
- [Synthadoc](https://github.com/axoviq-ai/synthadoc) — already listed and reviewed as `kb/agent-memory-systems/reviews/synthadoc.md`; post-cutoff comments are release updates.
- [AutoSci](https://github.com/skyllwt/AutoSci) — already listed as review-later in the first triage file.
- [ai-modules](https://github.com/theafh/ai-modules) — already listed and reviewed as `kb/agent-memory-systems/reviews/theafh--ai-modules.md`; post-cutoff comment expands the same project framing.
- [OpenClerk](https://github.com/yazanabuashour/openclerk) — already listed and reviewed as `kb/agent-memory-systems/reviews/openclerk.md`; post-cutoff comment restates the boundary between canonical Markdown, derived recall state, and agent write authority.

## Local Duplicate Check

Checked on 2026-06-18 against `related-systems/` top-level directory names, `related-systems/*/.git/config` remote URLs where available, exact likely review filenames, and exact repo/name hits under `kb/agent-memory-systems/reviews/`. Generic content fallback was not used for `Link` because `link` is a common word in nearly every review.

| Candidate | `related-systems/` checkout | Review file |
|---|---|---|
| Synto (`kytmanov/synto`) | none found | none found |
| LLM-WIKI-MCP (`Electro-resonance/LLM-WIKI-MCP`) | none found | none found |
| Knolo Wiki Librarian Skill | none found | none found |
| LLM-Wiki-v3 (`vvvvvivekkk/LLM-Wiki-v3`) | none found | none found |
| memwiki (`hereisSwapnil/memwiki`) | none found | none found |
| llmwiki-marimo (`Clod/llmwiki-marimo`) | missed in original check; added as `related-systems/Clod--llmwiki-marimo` on 2026-06-18 for review | missed in original check; review added after follow-up inspection |
| Link (`gowtham0992/link`) | none found | none found |
| EchoesVault (`psinetron/echoes-vault-opencode`) | none found | none found |
| Smriti-MCP (`deepak-bhardwaj-ps/smriti-mcp`) | none found | none found |
| Eidetic (`LARIkoz/eidetic`) | none found | none found |
| OKF Harness (`pumblus/okf-harness`) | none found | none found |
| Matryca Plumber (`MarcoPorcellato/matryca-plumber`) | none found | none found |
| ContextSlice (`llcortex/ContextSlice`) | none found | none found |
| FrameCode-VibeWork (`Sistema2D/FrameCode-VibeWork`) | none found | none found |

Post-cutoff comments that were already covered locally:

| Existing system | `related-systems/` checkout | Review file / local status |
|---|---|---|
| Dense-Mem (`markhuangai/dense-mem`) | `related-systems/markhuangai--dense-mem` | `kb/agent-memory-systems/reviews/dense-mem.md` |
| Synthadoc (`axoviq-ai/synthadoc`) | `related-systems/axoviq-ai--synthadoc` | `kb/agent-memory-systems/reviews/synthadoc.md` |
| ai-modules (`theafh/ai-modules`) | `related-systems/theafh--ai-modules` | `kb/agent-memory-systems/reviews/theafh--ai-modules.md` |
| OpenClerk (`yazanabuashour/openclerk`) | `related-systems/yazanabuashour--openclerk` | `kb/agent-memory-systems/reviews/openclerk.md` |
| AutoSci (`skyllwt/AutoSci`) | `related-systems/skyllwt--OmegaWiki` — checkout origin is `https://github.com/skyllwt/OmegaWiki`, but the README now identifies the system as AutoSci and says AutoSci evolved from the earlier OmegaWiki prototype | first triage file only; no review found |
| Mnemosyne / IsaacCLupus spec (`noirblue/IsaacCLupus_mnemosyn_spec`) | none found | first triage file only; no review found |

Deferral reasons from the first triage file:

- AutoSci was put in "Review Later" because memory is important but embedded in a larger autonomous-science system (`ideate -> experiment -> write -> rebuttal`). If reviewed, it probably needs either a whole-system analysis under `kb/agentic-systems/` or a deliberately scoped memory-subsystem review that carves out SciMem/OmegaWiki from the broader research lifecycle.
- Mnemosyne / IsaacCLupus was put in "Review Later" because the first triage read it as a spec-level artifact rather than a conventional implementation. That should not mean "not real" or "not reviewable": Commonplace itself is partly an executable specification, and an external executable spec can be worth reviewing if its contracts, schemas, examples, or glue code constrain behavior. The right next question is whether Mnemosyne should receive doc-grounded/executable-spec coverage or whether enough runnable machinery exists for a code-grounded review.

## Recommended Parallel Review Queue

Primary repo-backed targets from this second pass:

- Synto
- LLM-WIKI-MCP
- LLM-Wiki-v3
- memwiki
- llmwiki-marimo
- Link
- EchoesVault
- Smriti-MCP
- Eidetic
- OKF Harness

Carryover targets now known to be reviewable:

- AutoSci — review either as a whole agentic system under `kb/agentic-systems/` or as a scoped memory-subsystem review around SciMem/OmegaWiki.
- Mnemosyne / IsaacCLupus spec — review as executable-spec/doc-grounded coverage unless inspection shows enough runnable machinery for code-grounded treatment.

Defer unless a specific paper gap needs them:

- Matryca Plumber — strong write-safety/context-engineering substrate, weaker as a memory system from current evidence.
- FrameCode-VibeWork — strong executable-spec/document framework candidate; classify carefully before putting it in the agent-memory comparison set.
- ContextSlice — context preprocessor, not durable memory.
- Knolo Wiki Librarian Skill — no public source found.

## Public Repo Reality Check

Checked on 2026-06-18 against GitHub repository metadata, default-branch recursive file trees, README files, and activation files where the repo is spec-first or document-heavy. "Real repo" here means more than an empty placeholder: it has a reachable public repository with substantive files. "Implementation repo" means the repository appears to ship runnable code, package metadata, commands, tests, or integration surfaces rather than only a proposal.

Executable-spec criterion: a spec-first system needs an **activation mechanism**. An `AGENTS.md`-style file counts only when it activates the described system for an external agent in the target workspace, or when it is a template/generated artifact for that activation. A normal repo-maintenance `AGENTS.md` that only tells contributors how to edit the repository is evidence of project hygiene, not evidence that the specification is executable.

| Candidate | Repo status | Evidence snapshot |
|---|---|---|
| [Synto](https://github.com/kytmanov/synto) | real implementation repo | 206 files, 180 code files, `pyproject.toml`, `uv.lock`, scripts, docs; pushed 2026-06-16. |
| [LLM-WIKI-MCP](https://github.com/Electro-resonance/LLM-WIKI-MCP) | real implementation repo | 67 files, 29 code files, `pyproject.toml`, MCP/CLI docs; pushed 2026-05-21. |
| Knolo Wiki Librarian Skill | no public repo found | The gist comment has no repository URL; web search found no stable public repo for this named skill. |
| [LLM-Wiki-v3](https://github.com/vvvvvivekkk/LLM-Wiki-v3) | real implementation repo | 100 files, 51 code files, `pyproject.toml`, evals, sample knowledge tree, audit log; pushed 2026-06-06. |
| [memwiki](https://github.com/hereisSwapnil/memwiki) | real small implementation repo | 22 files, 6 code files, `package.json`, `package-lock.json`, `.memory/` scaffold, agent hook files; pushed 2026-06-06. |
| [llmwiki-marimo](https://github.com/Clod/llmwiki-marimo) | real implementation repo | Marimo notebook apps, Python core, SQLite schema, tests, UAT/eval scripts, programmer manual, and local wiki git snapshot behavior; pushed 2026-06-18. |
| [Link](https://github.com/gowtham0992/link) | real implementation repo | 215 files, 156 code files, Python package metadata, MCP package metadata, docs/assets; pushed 2026-06-14. |
| [EchoesVault](https://github.com/psinetron/echoes-vault-opencode) | real small implementation repo | 8 files, TypeScript entrypoint, `package.json`, `tsconfig.json`, README; pushed 2026-06-16. |
| [Smriti-MCP](https://github.com/deepak-bhardwaj-ps/smriti-mcp) | real implementation repo | 23 files, 13 code files, `pyproject.toml`, `requirements.txt`, MCP server/store code and tests; pushed 2026-06-11. |
| [Eidetic](https://github.com/LARIkoz/eidetic) | real implementation repo | 100 files, 54 code files, many `bin/` scripts, tests/workflows/docs; pushed 2026-06-18. |
| [OKF Harness](https://github.com/pumblus/okf-harness) | real implementation repo with generated activation path | 147 files, 68 code files, package workspace, CLI/core/MCP packages, ADR docs. Root `AGENTS.md` is mostly repo-maintenance guidance; the activation surface appears to be `packages/agent-pack` plus `okfh --json` and rendered Claude/Codex adapters. Pushed 2026-06-18. |
| [Matryca Plumber](https://github.com/MarcoPorcellato/matryca-plumber) | real implementation repo | 370 files, 278 code files, Python/frontend package metadata, CLI/MCP/docs; pushed 2026-06-18. |
| [ContextSlice](https://github.com/llcortex/ContextSlice) | real implementation repo, but still marginal for memory review | 23 files, 16 code files, `pyproject.toml`, MCP server, tests; the repo is a context preprocessor rather than durable memory. |
| [FrameCode-VibeWork](https://github.com/Sistema2D/FrameCode-VibeWork) | real substantial executable-spec/document-framework repo, not a code-heavy implementation | 181 files, 175 Markdown/docs files, governance/technical-memory framework. Root `AGENTS.md` is an operational guide for humans and agents using the framework, with selective loading and workflow routing; verify in review whether it is meant as a copied target-workspace activation file or only as the framework repo's own entrypoint. |
| [AutoSci](https://github.com/skyllwt/AutoSci) | real implementation repo with activation contract | 261 files, 48 code files, Claude skills, requirements, MCP review server, research lifecycle docs. Root `CLAUDE.md` is an OmegaWiki runtime contract, not ordinary contributor guidance; pushed 2026-06-14. |
| [Mnemosyne / IsaacCLupus spec](https://github.com/noirblue/IsaacCLupus_mnemosyn_spec) | real spec-first repo; possibly executable-spec coverage if activation is accepted | 46 files, mostly specification/docs, plus config samples, diagrams, and `prior-art/v0-glue/` Python code. Root `AGENTS.md` describes agents as clients of the memory OS through MCP/REST/CLI and the memory lifecycle; `SPECIFICATION.md` also names `pack/AGENTS.md` as the human-readable entrypoint. Review should verify whether that is an actual activation artifact or still only an architectural description. |

## Notes

- The source cutoff is comment creation time, not repository creation time or release time.
- The fetched GitHub API result is mutable in principle because comments can be edited or deleted. For paper-grade reproducibility, snapshotting the JSON response under `kb/sources/` or an external archive would be stronger than relying on this workshop triage file alone.
- Local duplicate checks found no existing KB review or `related-systems/` checkout for the new candidate names as of this pass.
