# Repo-review backlog brief (subagent run)

**Temporary workshop file.** Purpose: hand a subagent everything it needs to write a code-grounded `agent-memory-system-review` for each backlog system that has a public repo. Run one subagent per system. Delete this file once all four reviews exist and the README backlog callout is empty.

These four systems currently have only an ingest report in `kb/sources/` and a mention in the README "Review backlog" callout. They have public repos, so they belong in `kb/agent-memory-systems/reviews/`, not `lightweight/`.

**Repo reality check (2026-05-30).** Verified each repo actually contains the real implementation, not a paper-stub placeholder (authors sometimes publish a paper + empty repo "to be cleaned up later" and never populate it):

- `mem0ai/mem0` — 56 MB Python, 57k★, pushed same day. Real.
- `getzep/graphiti` — 15 MB Python, 27k★, active. Real.
- `letta-ai/letta` — 294 MB Python, 23k★, active. Real.
- `agiresearch/A-mem` — small repo (~1 MB) but the core `agentic_memory/memory_system.py` is ~32 KB plus `retrievers.py`, `llm_controller.py`, `tests/`, and `examples/`; no "coming soon" phrasing. **Real implementation.** (`WujiangXu/A-mem-sys` is an equivalent variant with multi-backend `llm_controller`; `agiresearch/A-mem` is the canonical org repo — use it.)

## Shared contract (same for every system)

The authoritative process is the local skill — read it before orchestrating:

- **Skill (parent-owned steps):** `kb/instructions/write-agent-memory-system-review/SKILL.md`
- **Worker contract (the review type spec):** `kb/agent-memory-systems/types/agent-memory-system-review.md`
- **Collection conventions:** `kb/agent-memory-systems/COLLECTION.md`
- **Style:** worker reads 1–2 existing reviews under `kb/agent-memory-systems/reviews/` (e.g. `cognee.md`, `hindsight.md` — nearby database-backed systems).

Per the skill, the **parent** owns: clone/refresh into `related-systems/`, capture `reviewed_commit`, delegate drafting to a fresh worker, taxonomy + semantic QA, `commonplace-validate`, index refresh, final report. The **worker** owns only: read the contract + COLLECTION + 1–2 reviews, inspect `source_dir`, write `note_path`, decide trace-derived status.

Operational invariants:

- Checkouts live **outside `kb/`**, under `related-systems/{owner}--{repo}/` (the dir exists and is currently empty of these). Clone fresh: `git clone "{repo_url}" "related-systems/{owner}--{repo}/"`.
- After clone, capture `reviewed_commit = git -C <checkout> rev-parse HEAD` and write the refresh marker (skill step 6).
- Cite source files as `{repo_url}/blob/{reviewed_commit}/{path}`, directories as `.../tree/{...}`.
- No existing review collides with any of these four (checked) — use the lowercase slug as the filename.

⚠️ **Stale skill step.** Skill step 9 says "add the system to the `## Systems` list" in the README. That list was **removed today** — the README now defers to `reviews/dir-index.md`. So instead, after each review: (a) remove the system from the README **"Review backlog"** callout, (b) run `commonplace-refresh-indexes` so `reviews/dir-index.md` picks it up. (The skill itself should be updated to reflect this; tracked separately.)

## Systems

### 1. Mem0
- `repo_url`: https://github.com/mem0ai/mem0
- `owner/repo`: `mem0ai/mem0` · slug `mem0`
- `checkout_dir`: `related-systems/mem0ai--mem0/`
- `note_path`: `kb/agent-memory-systems/reviews/mem0.md`
- Existing coverage: `kb/sources/mem0-memory-layer.ingest.md`; synthesized in the [comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md).
- Focus to verify in code: the **two-phase add pipeline** (extract facts → LLM-judged CRUD reconciliation `ADD/UPDATE/DELETE/NOOP`). The comparative review calls Mem0 the "purest production example of automated accretion-without-synthesis" — confirm or correct against the implementation. Storage substrate (vector store + optional graph), and whether anything synthesizes/curates beyond per-fact CRUD.

### 2. Graphiti
- `repo_url`: https://github.com/getzep/graphiti
- `owner/repo`: `getzep/graphiti` · slug `graphiti`
- `checkout_dir`: `related-systems/getzep--graphiti/`
- `note_path`: `kb/agent-memory-systems/reviews/graphiti.md`
- Existing coverage: `kb/sources/graphiti-temporal-knowledge-graph.ingest.md` (Apache-2.0; arXiv paper accompanies).
- Focus to verify in code: **bi-temporal knowledge graph** with edge invalidation (event time vs ingestion time), node/edge schema, pluggable graph DB backends, LLM-driven ingestion pipeline. Strongest temporal model in the survey — pin down exactly how edge invalidation and point-in-time queries are implemented.

### 3. Letta (MemGPT lineage)
- `repo_url`: https://github.com/letta-ai/letta
- `owner/repo`: `letta-ai/letta` · slug `letta`
- `checkout_dir`: `related-systems/letta-ai--letta/`
- `note_path`: `kb/agent-memory-systems/reviews/letta.md`
- Existing coverage: `kb/sources/letta-memgpt-stateful-agents.ingest.md`.
- Focus to verify in code: **agent-self-managed three-tier memory** (main context ≈ RAM, archival ≈ disk, recall ≈ conversation log) and the self-editing memory tools the agent calls. Letta is the survey's exemplar of the **agent-self-managed agency model** — confirm where the agency boundary actually sits (which memory ops the agent invokes vs framework-driven).

### 4. A-MEM
- `repo_url`: https://github.com/agiresearch/A-mem  *(verified canonical, real code — see reality check above; variant `WujiangXu/A-mem-sys` is equivalent)*
- `owner/repo`: `agiresearch/A-mem` · slug `a-mem`
- `checkout_dir`: `related-systems/agiresearch--A-mem/`
- `note_path`: `kb/agent-memory-systems/reviews/a-mem.md`
- Existing coverage: `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` (paper-only, arXiv 2502.12110). This is a **paper→repo upgrade**: previously paper-only, now has code, so it qualifies for a repo-backed review.
- Focus to verify in code: **Zettelkasten-inspired dynamic memory** — atomic notes with LLM-generated keywords/tags/contextual descriptions, flexible link generation between notes, and memory evolution/update of neighbors. Verify the "no static, predetermined memory operations" claim against the actual operation set, and how linking/evolution is triggered.

## How to run

For each system, invoke the `write-agent-memory-system-review` skill (or replicate its parent steps) with the per-system `repo_url`; it clones, delegates drafting to a fresh worker against the type contract, QAs, and validates. The four are independent — they can run in parallel. After all four: confirm the README "Review backlog" callout is empty (or only non-repo systems remain), refresh indexes, and delete this brief.
