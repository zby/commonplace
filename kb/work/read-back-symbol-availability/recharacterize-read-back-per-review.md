# Re-characterize read-back — orchestrated pass

**For an orchestrator agent.** Input: `kb/agent-memory-systems/systems.csv`. You drive a re-characterization of read-back under the symbol-availability model by selecting target reviews from the matrix and fanning out one sub-agent per review. You are working in the `commonplace` repo at its root.

## Input

`kb/agent-memory-systems/systems.csv` — the comparison matrix, one row per reviewed system. Columns you use: `review_file`, `clone_path` (the system's cloned source, used as `source_dir`), `read_back_direction`, `push_engineered`.

## Orchestrator procedure

1. **Select targets.** Rows where `read_back_direction` ∈ `push` | `both`, **or** `push_engineered = yes` — the systems the old flat trigger list may have mislabeled. Pull-only rows rarely change; skip them.
2. **Resolve inputs per target.** `review_path` = `review_file`; `source_dir` = `clone_path`. If a target row lacks a `review_file` or a clone path, skip it and report it — this pass needs both the review and its source.
3. **Fan out**, one sub-agent per target, each given its `review_path` + `source_dir` and the **per-review task** below (verbatim). Sub-agents edit different files and write nothing shared, so they run in parallel safely.
4. **Watch progress** via each sub-agent's returned one-line summary — ephemeral, for your visibility only; do not save it.
5. **When all finish, regenerate the matrix:** `python3 scripts/build_systems_matrix.py`, then `python3 scripts/analyze_matrix.py` to see the new read-back distribution. The parser reads the updated `**Read-back:**` tokens and `push-activation` tags from the edited reviews; the targeting/signal detail stays in prose until tokenized (workshop Thread 3).

---

## Per-review sub-agent task (hand this block to each sub-agent verbatim)

**You are an execution agent re-characterizing one review's read-back, grounded in the system's source. Self-contained — do not assume prior conversation.** You are in the `commonplace` repo root.

**Inputs:** `review_path` (a non-archived file under `kb/agent-memory-systems/reviews/`) and `source_dir` (the system's cloned repo under `related-systems/`). Verify the review's `type` resolves to `agent-memory-system-review` and `source_dir` is readable (`test -d`); if either is missing, stop and report. Do not mutate `source_dir`.

### The model (the contract)

**Scope cut — read-back is the return of *retained memory* only.** Retained = content the system *accumulated from use*, whether **authored** (a user's note, a project decision, a maintained artifact) or **trace-learned**. Runtime injection of **shipped/static baseline documentation** — tool specs, repo docs, installed skills, system manuals — is **not read-back**; it is a baseline context surface. Boundary test: *does the content accumulate from use of this system, or arrive with the system?* The direction verdict (`pull`/`push`/`both`) counts memory read-back only — pushing static documentation does **not** make a system `push`/`both`.

For genuine memory pushes, two fields:

- **targeting** ∈ `coarse` (always-present or action-type symbol — always-load of memory, session start, any tool call — generic recall) | `instance` (selects for *this* instance). Always-load is the degenerate corner.
- **signal** (only when `instance`) ∈ `identifier` (matches an identifier the instance carries by design — tag, type, path, tool name, id, declared scope) | `inferred` (relevance derived from content), `inferred` sub-kind `lexical` (keyword/BM25 — exact-token but content-keyed, sense-blind), `embedding` (learned similarity), or `judgment` (an LLM relevance call).

Discriminator: classify by **what it keys on**, not the mechanism — keyword keys on content words, not an assigned identifier, so it is `inferred / lexical`. Examples — `identifier`: a tag/type/tool-name/`project_id` match, Atomic-style report scope filters. `inferred`: embedding on the current message (CrewAI), current-input-as-query (REM), an LLM relevance judge; keyword overlap is `lexical`. **mixed**: identifier narrowing then inferred ranking (EQUIPA) — record the final selector, note the composition.

### Procedure

1. Read both the review's read-back content (the `**Read-back:** \`…\`` verdict line and any `## Read-back placement` section) **and the system's read-back/activation path in `source_dir`** — where memory is selected and injected into a future action.
2. **Scope cut (from code):** is the injected content retained memory or shipped baseline documentation? Documentation is not read-back.
3. **Memory-only direction:** `pull`/`push`/`both`, counting only genuine memory paths.
4. **Targeting + signal (from code):** for each memory push path, read off `targeting`, and when `instance`, `signal` + sub-kind, from how the code actually selects.
5. **Edit the review** (rules below). Report the observable mechanism but mark precision/recall, context dilution, and effective authority *not verified from code*; for libraries/SDKs whose push wiring lives in the host harness, report the **API surface** as capability, not deployed behavior.
6. **Flag** only genuine ambiguity — the activation path is absent, host-dependent, or the code doesn't settle it.

### Edit rules

- Set `**Read-back:** \`…\`` to the memory-only direction.
- In `## Read-back placement`, state `targeting` and, when `instance`, `signal` + sub-kind in the model's terms (add the section if the system warrants a full treatment and lacks one).
- When a former "push" is documentation, say so in one line ("X injects shipped skill docs — a baseline context surface, not read-back").
- `push-activation` tag: keep/add iff there is a genuine instance-targeted (or otherwise engineered) *memory* push, and ensure a `## Read-back placement` section exists (the schema requires it when the tag is present); remove iff read-back is now documentation-only or coarse.
- Do **not** bump `last-checked` — this is a targeted read-back pass, not a full review refresh. Preserve all other sections, citations, and frontmatter.

### Validate & output

- Run `uv run commonplace-validate <review_path>`; fix any `push-activation`-tag ↔ `## Read-back placement`-section inconsistency; if it newly fails for a reason you can't resolve, revert your change and flag it.
- **Edit the review only** — do not modify `systems.csv` or write any ledger.
- **Return a one-line summary** (`old → new` direction, targeting/signal, push-activation change, any flag) for the orchestrator's progress visibility only — it is not saved. The single durable output is the edited review.

---

Source of the model: [workshop README](./README.md) and the review type's [Read-back placement](../../agent-memory-systems/types/agent-memory-system-review.md) section, resting on [symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md). (Meta-reader links; the task above is self-contained.)
