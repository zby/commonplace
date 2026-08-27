# Evidence packet — run `AAS-2026-08-20-fractal-01`

Prepared once by the orchestrator. **Lens workers must not reacquire, refresh, or widen sources.**
Targeted reads *inside* the frozen boundary are permitted; every new material record or
targeted-evidence request returns to the orchestrator for a canonical ID.

---

## 1. Boundary declaration

**System:** Fractal — `github.com/Trampoline-AI/fractal`, PyPI `fractal-rlm`. A terminal CLI coding
agent that is a thin host layer over `predict-rlm`, Trampoline's "self-harnessed Recursive Language
Model" runtime.

**In scope (reviewed boundary, by function):** the `fractal` Python package as checked out at the
frozen revision — everything that decides *scheduling*, *context selection*, *retained state*,
*action execution*, *checking*, *acceptance*, or *authority* for a Fractal turn:

- CLI entry, argument surface, and mode selection (`src/fractal/cli.py`)
- interactive loop, slash commands, interrupt handling (`src/fractal/tui/app.py`)
- turn coordinator and outcome classification (`src/fractal/runtime.py`)
- PredictRLM adapter, sandbox construction, skill wiring (`src/fractal/agent/service.py`)
- per-turn prompt/context assembly (`src/fractal/agent/signature.py`)
- session store: summary, history, usage, persistence (`src/fractal/session.py`)
- host-side observation of file/command actions (`src/fractal/events.py`)
- config layering, provider/model resolution, credentials, onboarding
  (`src/fractal/config.py`, `config_commands.py`, `providers.py`, `credentials.py`,
  `onboarding.py`, `runtime_lms.py`, `connectivity.py`)
- pre-turn context estimation (`src/fractal/context_meter.py`)
- shipped instruction artifacts: `src/fractal/agent/skills.py`, `.agents/skills/**`
- the project's own doctrine: `README.md`, `docs/**`, `AGENTS.md`

**Actors in scope:** the human operator; the main LM; the sub-LM; an external calling agent that
invokes `fractal -p` via the bundled skill.

**Excluded (external dependencies, NOT inspected — no source obtained):**

- `predict-rlm` 0.7.0 — the actual RLM iteration/recursion loop, code generation, sub-LM spawning,
  `RunTrace` production, `RuntimeHook` injection, `Skill` handling, `Workspace` semantics,
  `SbxBackend` implementation. Pinned in `uv.lock`; source is not vendored and no virtualenv exists
  in the checkout.
- `sbx` / Docker Sandboxes — the container, its mount and network policy.
- `dspy`, `litellm`, `tiktoken`, and every model provider service.

**Boundary kind:** **subsystem-only with respect to deployed agentic behavior.** Fractal's host
layer is inspected whole; the inner agent loop that actually produces the behavior is an external
dependency inspected only at its call interface. **No whole-system conclusion about the RLM loop,
its recursion, its context management, or its sandbox isolation may be drawn from this run.**

**Analysis cutoff:** 2026-08-20. **Frozen revision:** `5954a07d464feeaf6c311a9fa5ca2e54200a6794`
(authored 2026-06-23). Working tree clean at inspection.

**Overall evidence tier:** `code-grounded` **for the host layer only**; every claim about the inner
RLM loop, the sandbox, or trace contents is at best `claimed` (doctrine) and is marked
`uninspected` where evidence was needed. **No run was executed** — no `observed` or
`causally supported` status is available anywhere in this run.

---

## 2. Source register

| ID | Kind | Identity / location | Revision / capture | Evidence layer | Inspected scope | Citation anchors | Access gaps |
|---|---|---|---|---|---|---|---|
| SRC-1 | git checkout, host source | `related-systems/Trampoline-AI--fractal/src/fractal/**` | `5954a07d` | implementation | read in full: `runtime.py`, `session.py`, `cli.py`, `events.py`, `context_meter.py`, `agent/service.py`, `agent/signature.py`, `agent/schema.py`, `agent/skills.py`; symbol-level greps only: `config.py`, `tui/app.py` | file path + symbol/line | `providers.py`, `onboarding.py`, `credentials.py`, `config_commands.py`, `connectivity.py`, `errors.py`, `runtime_lms.py`, `version_check.py` not read line-by-line |
| SRC-2 | project doctrine | `README.md` | `5954a07d` | doctrine/design | read in full | section heading | marketing register; pseudo-trace explicitly labelled non-real |
| SRC-3 | project doctrine | `docs/session-management.md`, `docs/headless.md` | `5954a07d` | doctrine/design | read in full | section heading | `docs/config.md` not read |
| SRC-4 | contributor doctrine | `AGENTS.md` | `5954a07d` | doctrine/design | read in full | section heading | internally stale in places (see conflicts) |
| SRC-5 | shipped instruction artifact | `.agents/skills/fractal/SKILL.md`, `.agents/skills/fractal/RECIPES.md`, `.agents/skills/fractal_add_provider/SKILL.md` | `5954a07d` | implementation *as an artifact*, doctrine/design *as content* | SKILL.md full; RECIPES.md first 40 lines; add_provider first 40 lines | line number | RECIPES.md and add_provider tails unread |
| SRC-6 | dependency manifest | `pyproject.toml`, `uv.lock` | `5954a07d` | implementation | grep for `predict` | line number | — |
| SRC-7 | test suite | `tests/**` (22 files) | `5954a07d` | implementation | **file listing only**; no test body read | filename | test bodies uninspected; no conclusion about what is actually verified |
| SRC-8 | external dependency, **not obtained** | `predict-rlm` 0.7.0 (PyPI sdist/wheel hashes in `uv.lock:1398-1400`) | 0.7.0 | *none — not inspected* | none | — | **Entire inner RLM loop uninspected.** Prevents any conclusion about recursion, context management, code execution, trace fidelity, sandbox isolation, or sub-LM behavior. |
| SRC-9 | absent artifact | `docs/predict-rlm-notes.md`, referenced by `AGENTS.md:26` | — | *absent within boundary* | `ls docs/` → `config.md`, `headless.md`, `session-management.md` | — | Referenced file does not exist at this revision |

**Access gaps common to the whole run:** no execution environment (`sbx` absent, no provider
credentials, no virtualenv), and the checkout must not be mutated. Therefore **no observed run and
no causal experiment** exist for any record.

---

## 3. Registered canonical records

### Components (`CMP-*`) — orchestrator-owned generic identity/form/substrate

| ID | Name | Substrate / form | Evidence |
|---|---|---|---|
| CMP-01 | `fractal.cli` — entry, argv surface, mode select (TUI vs headless vs `config`) | Python module | SRC-1 `cli.py` |
| CMP-02 | `TerminalFractalApp` — interactive loop, slash commands, SIGINT | Python module | SRC-1 `tui/app.py` |
| CMP-03 | `FractalRuntime` — turn coordinator, outcome classification, persistence | Python class | SRC-1 `runtime.py:45-323` |
| CMP-04 | `FractalAgent` — PredictRLM adapter (dspy.Module) | Python class | SRC-1 `agent/service.py:46-137` |
| CMP-05 | `build_edit_workspace_signature` — per-turn prompt assembly | Python function producing a `dspy.Signature` | SRC-1 `agent/signature.py:32-107` |
| CMP-06 | `fractal.session` — session store (summary, history, usage, on-disk JSON) | Python module + JSON files | SRC-1 `session.py` |
| CMP-07 | `RuntimeEventTracker` + `build_predict_runtime_hooks` — host-side action observation | Python module | SRC-1 `events.py` |
| CMP-08 | config/provider/credential stack — layering, model resolution, auth | TOML files + env + Python | SRC-1 `config.py`, SRC-5 add_provider skill |
| CMP-09 | `context_meter` — pre-turn context-size estimate | Python module | SRC-1 `context_meter.py` |
| CMP-10 | `filesystem_coding_skill` — shipped `predict_rlm.Skill` instruction text | natural-language, in-repo constant | SRC-1 `agent/skills.py:5-315` |
| CMP-11 | bundled `fractal` agent skill (+ RECIPES) — teaches an *external* agent to delegate | natural-language SKILL.md | SRC-5 |
| CMP-12 | `predict_rlm.PredictRLM` — **external, uninspected** inner RLM loop | Python package (not obtained) | SRC-8 |
| CMP-13 | `SbxBackend` / sbx Docker sandbox — **external, uninspected** execution boundary | container | SRC-8, SRC-2 |
| CMP-14 | `UpdateNotifier` — background PyPI version check | Python module | SRC-1 `version_check.py` (grep only) |

### Operative objects (`OBJ-*`)

| ID | Object | Form | Substrate / lifetime | Evidence |
|---|---|---|---|---|
| OBJ-01 | `user_message` for the turn | natural language | in-memory + persisted | `runtime.py:222`, `signature.py:87` |
| OBJ-02 | **rendered session summary** (prompt text) | natural language, baked into signature docstring | regenerated per turn | `session.py:368-390`, `signature.py:54-64` |
| OBJ-03 | `SessionSummary` / `SummaryTurn` structured record | typed pydantic (JSON) | on disk, unbounded turn count | `session.py:66-74, 203-262` |
| OBJ-04 | `session_history: list[SessionHistoryTurn]` | typed pydantic, delivered as a REPL variable | on disk, **capped at last 20 turns** | `session.py:76-87, 23, 278-279` |
| OBJ-05 | `RunTrace` (REPL reasoning, code, output, tool/predict calls, usage, status) | typed object produced by CMP-12 | persisted inside OBJ-04 | `session.py:83`, `runtime.py:326-346` |
| OBJ-06 | `TurnUsage` — tokens, cost, duration, iterations, live context size | typed numeric | on disk, per turn + session totals | `session.py:38-53, 306-322` |
| OBJ-07 | agent `response` — the user-facing answer/deliverable | natural language, **model-produced** | returned + persisted | `agent/schema.py:13`, `session.py:58` |
| OBJ-08 | `changed_files` | list[str], **model-produced** | returned + persisted as a *count* in summary, full list in history | `signature.py:103`, `session.py:239` |
| OBJ-09 | `files_read` / `files_modified` / `commands_run` | list[str], **host-recorded from runtime hooks** | persisted | `events.py:87-89`, `session.py:255-258` |
| OBJ-10 | workspace files (+ `--include` dirs) | arbitrary files, mounted read/write into the sandbox | host filesystem, mutated in place | `agent/service.py:186-197`, SRC-2 "How it works" |
| OBJ-11 | workspace `AGENTS.md` instructions | natural language, user-authored, truncated at 20 000 chars | read fresh each turn | `agent/service.py:28-43`, `signature.py:42-50` |
| OBJ-12 | shipped skill instruction texts (`filesystem-coding`, `spreadsheet`, `pdf`, `docx`) | natural language | static, shipped | `agent/service.py:96`, `agent/skills.py` |
| OBJ-13 | session JSON file | JSON on disk, `schema_version: 1` | `<state-root>/workspaces/<key>/sessions/<id>.json` | `session.py:187-192, 435-471` |
| OBJ-14 | effective config + credentials | TOML + env + keyring/env references | global < project < env < flags | `config.py:256-310`, SRC-5 |
| OBJ-15 | `HeadlessResult` JSON envelope | JSON on stdout — the public CLI output contract | per invocation | `session.py:325-365` |
| OBJ-16 | `FractalRuntimeEvent` live stream | operator-facing status lines | ephemeral (stderr/TUI) | `events.py:61-69` |
| OBJ-17 | pre-turn context-token estimate | integer | ephemeral (toolbar) | `context_meter.py:56-58` |

### Routes (`RTE-*`) — runtime owns endpoints and progression; lenses annotate

| ID | Class | Route |
|---|---|---|
| RTE-01 | control | invocation → arg parse → mode select → config resolution → `FractalRuntime.create` → sandbox prewarm |
| RTE-02 | control | interactive loop: one submitted user message → exactly one RLM call → render → back to prompt |
| RTE-03 | control | headless: one process = one turn = one RLM call; exit code carries status |
| RTE-04 | control/recovery | SIGINT → flag → `asyncio.CancelledError` → interrupted turn persisted → **interpreter deliberately retained** |
| RTE-05 | control | **inner RLM iteration loop (CMP-12, uninspected)**, bounded by `max_iterations` (default 30); exhaustion yields fallback extraction + `status == "max_iterations"` |
| RTE-06 | context | per-turn prompt assembly: base instructions + AGENTS.md section + rendered session summary → signature docstring (always visible) |
| RTE-07 | context | `session_history` delivered as a REPL *variable*, inspected by the model on its own initiative |
| RTE-08 | context | `workspace` + `included_paths` delivered as REPL variables naming real sandbox-visible paths |
| RTE-09 | context | skills list injected into PredictRLM (`filesystem-coding`, `spreadsheet`, `pdf`, `docx`) |
| RTE-10 | state write | pending summary+history turn appended and saved **before** the call; completed record saved **after** |
| RTE-11 | state | history trimmed to the last `MAX_HISTORY_TURNS = 20`; summary is **not** trimmed |
| RTE-12 | action | generated Python + subprocesses execute in the sbx container against **directly mounted host paths** (external executor, uninspected) |
| RTE-13 | observation | PredictRLM runtime hooks on 12 file APIs + 5 subprocess APIs → `RuntimeEventTracker` → OBJ-09 + OBJ-16 |
| RTE-14 | state | usage derived from `RunTrace`, explicitly **not** from model output; `context_tokens` = prompt size of the last main-LM call |
| RTE-15 | output | `response` → stdout/TUI; `changed_files` → stderr line; `HeadlessResult` JSON under `--json` |
| RTE-16 | recovery | failed / interrupted / `max_iterations` turns persisted with error + trace so the next turn and future resumes see them |
| RTE-17 | config | global TOML < project `.fractal/config.toml` < `FRACTAL_*` env < CLI flags → provider + model + sub-model |
| RTE-18 | action/lifecycle | deterministic per-(workspace + include-set) sandbox name, hot reuse, `--fresh` teardown, `--ephemeral` throwaway |
| RTE-19 | control | session selection: **fresh session by default**, never auto-resume; `--resume` / `/resume` explicit; `/new`; `/sessions` lists workspace-scoped sessions |
| RTE-20 | control | external delegation: another agent runs `fractal -p …` per CMP-11 and consumes stdout as a distilled answer |

### Behavioral-authority paths (`BAP-*`) — consumer, channel, force, **horizon**

| ID | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|
| BAP-01 | main LM | signature docstring (base instructions) | directive, unenforced | the turn |
| BAP-02 | main LM | prompt section "Workspace instructions (AGENTS.md)" | directive, explicitly subordinate to `user_message`, unenforced | the turn |
| BAP-03 | main LM | prompt text, always-visible session summary | informative context, unenforced | the turn; content spans the session |
| BAP-04 | main LM | REPL variable `session_history`, model-initiated inspection | informative, opt-in | the turn |
| BAP-05 | main LM | PredictRLM `Skill` instruction text (CMP-10) | prescriptive rules ("Do not use absolute paths"), unenforced | the turn |
| BAP-06 | main LM | `user_message` input field | overriding directive (declared to beat AGENTS.md) | the turn |
| BAP-07 | **external calling agent** | `.agents/skills/fractal/SKILL.md` loaded into that agent's context | routing/advisory | that agent's session |
| BAP-08 | contributor agent | `.agents/skills/fractal_add_provider/SKILL.md` | prescriptive engineering policy | the contribution task |
| BAP-09 | generated-code executor | sbx container mount/network configuration | enforcing (operational), **external and uninspected** | sandbox lifetime |
| BAP-10 | runtime LM builder | config layering + `restricted_models` rejection | enforcing (operational) | the run |
| BAP-11 | calling script/agent | process interface: stdout/stderr split, exit codes 0/1/2/130, `--json` envelope | enforcing on the caller's control flow | the invocation |

### Claims (`CLM-*`) — orchestrator namespace; **epistemic lens owns truth/scope/warrant fields**

| ID | Claim (verbatim or close paraphrase) | Source anchor | Evidence layer of the claim |
|---|---|---|---|
| CLM-01 | "Most agents call a model in a loop that humans hand-engineer… **Fractal's loop _is_ the model**"; "The runtime is the agent; there's no orchestration to assemble." | SRC-2 §"What is Fractal?", §"What you get" | doctrine |
| CLM-02 | The RLM "reasons over context programmatically… **without context rot**". | SRC-2 §"What is Fractal?"; SRC-5 SKILL.md frontmatter | doctrine |
| CLM-03 | A main agent "hands Fractal the work in headless mode and **gets back a distilled answer**" for audits, tracing, root-cause, synthesis over many files. | SRC-2 §"Use it with your coding agent", §"Where it shines"; SRC-5 SKILL.md:36-51 | doctrine |
| CLM-04 | "capability scales with the underlying model instead of with harness engineering". | SRC-2 §"What is Fractal?" | doctrine |
| CLM-05 | "**Prefer host-side truth over model-reported truth** for state, files changed, commands run, verification status, and errors." | SRC-4 §"Engineering Guidelines" | doctrine (contributor policy) |
| CLM-06 | `TurnUsage` is "derived from the PredictRLM RunTrace, **not from model output, so it stays trustworthy** across failed and interrupted turns". | SRC-1 `session.py:38-44` | doctrine embedded in implementation |
| CLM-07 | "Fractal adds **exactly one thing** on top: session management." | SRC-2 §"What is Fractal?" | doctrine |
| CLM-08 | "**Changed files are currently coerced from model output.**" (self-declared caveat) | SRC-4 §"Current Caveats" | doctrine |
| CLM-09 | "every peek, chunk, sub-call, and verification step is **fully readable in the trace**". | SRC-2 §"How it works" | doctrine |
| CLM-10 | "Every Fractal turn runs fully inside a Docker Sandbox… an isolated container with **no network access by default**"; workspace mounted so edits land on the host immediately. | SRC-2 §"How it works" | doctrine |
| CLM-11 | The session summary is "**compressed structured trajectory context**… It preserves prior user messages and compressed agent results." | SRC-1 `signature.py:61-64`; SRC-3 session-management.md §"Structured Session Summary" | doctrine embedded in implementation |
| CLM-12 | "There is no robust approval/sandbox policy yet"; "There is no host command execution tool yet"; "no git checkpoint, diff review, or rollback layer yet". | SRC-4 §"Current Caveats" | doctrine |
| CLM-13 | The summary "needs to be always visible to the main model", so it is embedded in prompt text rather than declared as an input field, because PredictRLM exposes input fields "primarily as REPL variables with prompt previews". | SRC-1 `signature.py:66-71`; SRC-3 | doctrine embedded in implementation |

---

## 4. Recorded evidence conflicts (preserve as conflicts; do not resolve by picking the strongest)

| # | Conflict | Anchors |
|---|---|---|
| CONF-1 | **Session storage location.** Implementation stores sessions in a *global* state dir keyed by workspace (`$FRACTAL_STATE_HOME` / `$XDG_STATE_HOME/fractal` / `~/.local/state/fractal` → `workspaces/<key>/sessions/<id>.json`). Three doctrine artifacts instead tell readers sessions live at `<workspace>/.fractal/sessions/<id>.json`. | impl: `session.py:435-471`; doc: `AGENTS.md:21`, `RECIPES.md:26`, `SKILL.md:93`; correct doc: `docs/session-management.md:1-12` |
| CONF-2 | **Dependency source.** `AGENTS.md` says Fractal "depends on a local editable checkout of `../predict-rlm`" at `/Users/emile/git/predict-rlm`; `pyproject.toml` declares the PyPI dependency `predict-rlm[sbx]>=0.7.0`. | `AGENTS.md:31-42` vs `pyproject.toml:23`, `uv.lock:1387-1400` |
| CONF-3 | **Referenced file absent.** `AGENTS.md:26` routes predict-rlm issue notes to `docs/predict-rlm-notes.md`; that file does not exist at this revision. | `AGENTS.md:26`, SRC-9 |
| CONF-4 | **Documented flag set is incomplete.** README's option table omits `--fresh`, `--ephemeral`, and `--json`, all implemented in `cli.py`. `--quiet`'s argparse help still reads "reserved for quieter terminal output" though it is fully wired. | `README.md:257-268` vs `cli.py:113-147` |
| CONF-5 | **Turn-status vocabulary.** `docs/session-management.md` describes only success/failure; the implementation records four statuses (`succeeded`, `failed`, `max_iterations`, `interrupted`). | `docs/session-management.md:47-55` vs `session.py:57`, `runtime.py:263-321` |

---

## 5. Standing rules for lens workers

- Cite by `SRC-*` + local anchor. Never replace the boundary or an evidence layer.
- Extend `CMP-*`/`OBJ-*`/`RTE-*`/`BAP-*`/`CLM-*` **by ID**; never rename or re-inventory.
  A genuinely new material record goes back to the orchestrator for a canonical ID.
- Conclusion statuses, exactly: `absent`, `inapplicable`, `uninspected`, `claimed`, `implemented`,
  `observed`, `causally supported`. **No `observed` or `causally supported` status is available in
  this run** — no execution occurred.
- Never upgrade: context presence → activation; implementation → deployment/observed operation;
  observation → causality; operational continuation → warrant.
- Every negative or uncertain result must name the inspected boundary and the exact conclusion it
  prevents.
- **Memory read-back** = material accumulated or changed *through use* returning to a later
  invocation. Static shipped material (OBJ-11, OBJ-12) and ordinary current-run state are retained
  state, not read-back.
- **Behavioral authority** (consumer/channel/force/horizon) is not epistemic authority and not
  operational authority. Keep all three separate.
