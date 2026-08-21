# Runtime account — run `AAS-2026-08-20-fractal-01`

Logical record 5 of one result. System: **Fractal**, revision `5954a07d464feeaf6c311a9fa5ca2e54200a6794`.
Records and sources cited by the shared IDs registered in [`evidence-packet.md`](./evidence-packet.md).

Scheduling, context assembly, and external state/action are treated as **causal responsibilities,
not module boundaries**. In Fractal one facility routinely spans several: `FractalRuntime.submit`
(CMP-03) is simultaneously the scheduler for one turn, the state writer, and the outcome classifier;
`build_edit_workspace_signature` (CMP-05) is both context assembly and the delivery of behavioral
authority to the model.

---

## 5.1 Material loops

A loop is material here when it alters the analysis question, a control path, evidence strength, or
a lens result.

### L-A — The outer turn loop (interactive), `RTE-02`

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | One operator-submitted line at the prompt. Slash commands (`/help`, `/sessions`, `/resume`, `/new`, `/model`, `/provider`, `/usage`, `/verbose`, `/exit`) are intercepted **before** any model call and never reach the LM. | `implemented` | SRC-1 `tui/app.py:267-282, 513-537` |
| Next-step owner | The operator. There is no planner, no queue, no autonomous continuation: the loop blocks on `read_message()` until a human types. | `implemented` | SRC-1 `tui/app.py:272` |
| Decision policy and its form | Trivial and imperative: `if slash → handle locally; else → exactly one RLM call`. The policy is Python control flow, not a model decision and not a configurable rule set. | `implemented` | SRC-1 `tui/app.py:277-282` |
| Context selection and framing | Delegated to L-C below (`RTE-06`…`RTE-09`). | — | — |
| State reads / writes | Reads `FractalSession`; writes a pending turn before the call and a completed turn after (L-D). | `implemented` | SRC-1 `runtime.py:222-223, 263-322` |
| Action executor and boundary | None at this level. All action happens inside L-B, outside the boundary. | — | — |
| Persistence | Session JSON written twice per turn (L-D). | `implemented` | SRC-1 `runtime.py:223, 322` |
| Coordination and return | Single `asyncio.Task` per turn; the task's result is rendered, then control returns to the prompt. No concurrency across turns. | `implemented` | SRC-1 `tui/app.py:347-376` |
| Retry / cancellation / recovery | No retry anywhere. SIGINT during a turn sets a flag and cancels the task (L-E). A failed turn is persisted and the loop continues. | `implemented` | SRC-1 `tui/app.py:378-388`, `runtime.py:273-296` |
| Output | Response body, turn footer, changed-file list, and (when no live iteration events were seen) a trace summary. | `implemented` | SRC-1 `tui/app.py:286-300` |

**Anti-conflation note.** Slash-command handling is *scheduling* (it chooses whether a turn happens),
not context assembly, even though `/model` and `/provider` mutate what the next turn's context will
be built from.

### L-B — The inner RLM iteration loop, `RTE-05` — **outside the boundary**

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | `predictor.acall(workspace=…, included_paths=…, user_message=…, session_history=…)`, one call per turn. | `implemented` (the call site) | SRC-1 `agent/service.py:120-128` |
| Next-step owner | **The model.** Doctrine states the model writes and runs its own code, spawns sub-LMs, and manages its own context; `CLM-01` puts this as "Fractal's loop _is_ the model". | `claimed` | SRC-2 §"What is Fractal?", §"How it works" |
| Decision policy and its form | Uninspected. The iteration policy, recursion policy, and context-management policy all live in `CMP-12` / `SRC-8`, which was not obtained. | `uninspected` | SRC-8 |
| Bound | `max_iterations`, default 30, resolvable from `--max-iterations` → config `defaults.max_iterations` → 30. | `implemented` | SRC-1 `cli.py:52-58, 17` |
| Exhaustion behavior | On exhaustion PredictRLM **returns fallback output rather than raising**; Fractal detects `trace.status == "max_iterations"`, keeps the response, and marks the turn distinctly (exit code 2 headless). | `implemented` (Fractal's handling); `claimed` (PredictRLM's fallback semantics) | SRC-1 `runtime.py:298-311`, `cli.py:545-547` |
| Observability | Per-iteration `on_rlm_iteration_end` callback → `FractalIterationEvent` → live rendering; plus the persisted `RunTrace`. | `implemented` (the plumbing) | SRC-1 `agent/service.py:226-255` |
| Cost / usage | Recorded per turn from the trace, main + sub LM separately summed. | `implemented` | SRC-1 `session.py:306-322` |

**Materiality:** this loop *is* the deployed agentic behavior. Its being `uninspected` is the single
largest evidence limit of the run and is what makes the boundary a subsystem boundary
(evidence packet §1).

### L-C — Per-turn context assembly, `RTE-06`–`RTE-09`

Fractal assembles the turn's model input from four channels with **different visibility semantics**:

| Channel | Content | Visibility | Route | Authority | Evidence |
|---|---|---|---|---|---|
| Signature docstring, part 1 | `BASE_EDIT_WORKSPACE_INSTRUCTIONS` — static role framing, an input-field glossary, and file-editing preferences | always in prompt | `RTE-06` | `BAP-01` | SRC-1 `signature.py:8-29, 55` |
| Signature docstring, part 2 | Workspace `AGENTS.md` (OBJ-11), read fresh each turn, truncated at 20 000 chars with an explicit truncation marker; declared subordinate to `user_message` | always in prompt | `RTE-06` | `BAP-02` | SRC-1 `agent/service.py:28-43`, `signature.py:42-50` |
| Signature docstring, part 3 | Rendered session summary (OBJ-02) | always in prompt | `RTE-06` | `BAP-03` | SRC-1 `signature.py:52-64` |
| Input fields | `workspace`, `included_paths`, `user_message`, `session_history` | exposed as REPL **variables** with prompt previews, per the in-code rationale | `RTE-07`, `RTE-08` | `BAP-04`, `BAP-06` | SRC-1 `signature.py:75-95, 66-71` |
| Skills | `filesystem-coding` (in-repo, 300 lines of `os`/`rg` guidance and hard rules) plus `spreadsheet`, `pdf`, `docx` imported from PredictRLM | mechanism uninspected | `RTE-09` | `BAP-05` | SRC-1 `agent/service.py:96`, `agent/skills.py` |

Two engineered properties are worth recording because they constrain later claims:

1. **Deliberate ordering for prompt-cache stability.** Static workspace instructions are placed
   before the dynamic summary "so the prompt keeps a stable cacheable prefix across turns"
   (SRC-1 `signature.py:38-40`). This is a cost/latency decision embedded in context assembly.
2. **The summary is prompt text, not an input field, on purpose.** The in-code comment states that
   PredictRLM exposes input fields "primarily as REPL variables with prompt previews", and that
   always-visible memory needs prompt text; a future PredictRLM API may add prompt-only context
   fields (`CLM-13`, SRC-1 `signature.py:66-71`). The consequence is a genuine two-tier context:
   push-delivered summary vs pull-on-demand history.

`.fractal` is force-excluded from the `Workspace` so Fractal's own project config directory cannot
re-enter model context (SRC-1 `agent/service.py:79-80`; SRC-4 §"Engineering Guidelines"). Note that
at this revision the *session* files no longer live there (CONF-1), so the exclusion now guards the
project config directory rather than session state.

**Anti-conflation note.** Retaining the trace (L-D) is not selecting it into context: `session_history`
is *available* as a variable, and only the model's own inspection brings its content into the working
context. Presence of the variable is not activation.

### L-D — Session write and outcome classification, `RTE-10`, `RTE-11`, `RTE-14`, `RTE-16`

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Write before the call | `add_user_message` appends a `SummaryTurn` and a `pending` `SessionHistoryTurn`, then saves. Crash-before-response therefore leaves a durable pending record. | `implemented` | SRC-1 `runtime.py:222-223`, `session.py:203-219` |
| Write after the call | Exactly one of four statuses is recorded: `succeeded`, `max_iterations`, `failed`, `interrupted`. Each path saves. | `implemented` | SRC-1 `runtime.py:263-322`, `session.py:57` |
| Two retained layers | (a) `SessionSummary` — ordered turns with user message, status, response, three **counts**, error; unbounded. (b) `history` — full `SessionHistoryTurn` incl. `RunTrace` and the full path/command **lists**; hard-capped at the last 20 turns. | `implemented` | SRC-1 `session.py:66-93, 23, 278-279, 368-390` |
| Usage accounting | `TurnUsage` derived from `RunTrace`, main + sub summed; `context_tokens` is the prompt size of the **last** main-LM call, deliberately not cumulative. Session totals sum everything except `context_tokens`, which carries the latest value. | `implemented` | SRC-1 `session.py:285-322` |
| Persistence substrate | JSON under a per-user state root (`FRACTAL_STATE_HOME` → `XDG_STATE_HOME/fractal` → `~/.local/state/fractal`), keyed `workspaces/<slugged+sha256 workspace key>/sessions/<session_id>.json`. Session ids are validated to be plain filenames so a resume selector cannot become path access. | `implemented` | SRC-1 `session.py:435-480` |
| Corruption handling | Unreadable/malformed/version-mismatched/id-mismatched session files are **not** repaired: a timestamped `.bad-*` backup is copied, a `RuntimeWarning` is raised, and a fresh empty session with the requested id is returned. | `implemented` | SRC-1 `session.py:130-185, 483-494` |
| Recovery intent | Doctrine: "Persist enough state to recover from failures. A failed agent turn should leave useful session records, error details, changed files, and verification context." | `claimed` | SRC-4 §"Engineering Guidelines" |

### L-E — Interrupt and sandbox-continuity loop, `RTE-04`, `RTE-18`

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger | SIGINT while `_sigint_mode == "turn"`. Outside a turn the handler deliberately returns without raising, because raising from the signal handler would escape prompt_toolkit/asyncio and crash the CLI. | `implemented` | SRC-1 `tui/app.py:378-388` |
| Propagation | Flag set → active task cancelled → `CancelledError` reaches `FractalRuntime.submit`, which distinguishes user-initiated cancellation from model/tool failure and persists `status="interrupted"` before re-raising. | `implemented` | SRC-1 `runtime.py:250-272` |
| Sandbox continuity | The interpreter is **deliberately not rebuilt** on interrupt: the code comment states the cancellation propagates into the in-flight `aexecute`, whose cancellation-safe handler leaves the interpreter quiescent, so the next turn reuses it. A regression test is named in the comment. | `implemented` (Fractal's decision); `claimed` (the quiescence property, which lives in PredictRLM) | SRC-1 `runtime.py:256-262`; SRC-7 `tests/test_runtime_interrupt_recovery.py` (filename only) |
| Sandbox identity | Deterministic name `fractal-<workspace-basename>-<sha256[:12] of workspace+sorted includes>`; a different mount set must get a different sandbox because bind mounts are fixed at `sbx create` time and reattach cannot add them. | `implemented` | SRC-1 `agent/service.py:140-155` |
| Lifecycle controls | Hot reuse by default; `--fresh` force-removes the named sandbox before start; `--ephemeral` disables reuse and creates a throwaway. Shutdown is itself interruptible, and a second Ctrl-C during shutdown prints explicit `sbx ls` / `sbx rm --force` recovery instructions and exits 130. | `implemented` | SRC-1 `cli.py:124-139, 265-311` |

### L-F — Headless single-turn loop, `RTE-03`, `RTE-15`, `RTE-20`

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | `-p TEXT`; `-p -` reads the whole prompt from stdin; a normal `-p TEXT` with non-TTY stdin **appends** stdin as `<Fractal stdin context>…</Fractal stdin context>`. | `implemented` | SRC-1 `cli.py:554-576` |
| Input guards | 10 MiB stdin cap; a 1.0 s `select()` grace period so a non-TTY stdin that never delivers data (CI runners, process supervisors, **agent harnesses**) cannot block the turn; streams without a selectable fd are always read; an empty prompt exits 0 **without a model call**. | `implemented` | SRC-1 `cli.py:14-15, 579-611, 336-339` |
| Setup policy | Interactive provider setup is triggered only when stdin is a TTY, so a headless run fails fast rather than blocking on a prompt. | `implemented` | SRC-1 `cli.py:345-351`, SRC-3 headless.md §"Prerequisites" |
| Output contract | stdout = response text only (newline-terminated) or, under `--json`, one `HeadlessResult` object; stderr = banner, session id, live events, changed files, usage, completion. | `implemented` | SRC-1 `cli.py:512-551`, `session.py:325-365` |
| Exit codes | 0 success, 1 error, 2 `max_iterations` (best-effort response still on stdout), 130 interrupted. | `implemented` | SRC-1 `cli.py:16, 474-502, 545-551` |
| Consumer | Explicitly another agent: the bundled skill (CMP-11) instructs a calling agent when and how to delegate, and how to parse the two streams. | `implemented` as an artifact; its effect on any calling agent is `uninspected` | SRC-5 SKILL.md |
| Machine-output hygiene | The background PyPI update check (CMP-14) is skipped entirely under `--json` so machine-readable output stays clean. | `implemented` | SRC-1 `cli.py:630-634` |

---

## 5.2 Session selection — `RTE-19`

Materially unusual and worth its own record: **Fractal never auto-resumes.** `FractalSession.load`
with no `session_id` returns a *fresh* session, with the in-code rationale that multi-session storage
exists before a resume selector does, so "each process gets a fresh ID instead of silently choosing
the wrong prior conversation" (SRC-1 `session.py:120-128`). Resume is always explicit: `--resume <id>`
or `/resume <id>`, and `--resume` on a nonexistent id raises rather than silently starting fresh
(SRC-1 `runtime.py:113-116`). `/sessions` lists only sessions under the current workspace key, and
listing is explicitly "a navigation aid, not a validation pass" — unreadable or foreign files are
skipped silently (SRC-1 `session.py:402-432`).

Consequence for the memory lens: the default read-back population per new process is **empty**.

## 5.3 Host-side action observation — `RTE-13`

Fractal registers PredictRLM `RuntimeHook`s on 12 file-API targets (`builtins.open`,
`pathlib.Path.{open,read_text,read_bytes,write_text,write_bytes}`, `os.{open,pread,pwrite,ftruncate,
replace,unlink}`) and 5 subprocess targets, all three phases (SRC-1 `events.py:15-58, 277-292`).
`RuntimeEventTracker` reduces the raw stream into (a) an ephemeral operator-facing status line and
(b) durable de-duplicated `files_read` / `files_modified` / `commands_run` lists. It carries real
engineering: file descriptors opened via `os.open` are mapped to paths so later `pread`/`pwrite`/
`ftruncate` on that fd attribute correctly (`events.py:120-149`), and compound operations
(`read_text` internally calling `open`; `subprocess.run` internally calling `Popen`) are suppressed
so a single logical action surfaces once (`events.py:40-58, 236-274`). Read/write mode is decoded
from `O_WRONLY`/`O_RDWR`/`O_CREAT`/`O_TRUNC`/`O_APPEND` flags and from open-mode strings
(`events.py:334-364`).

Every observer callback is wrapped so an exception in rendering or tracking cannot fail the turn
(SRC-1 `runtime.py:202-220`).

**Bound:** the hook *injection* happens inside `CMP-12`. `docs/session-management.md` §"Known Limits"
states file and command tracking works only when the active PredictRLM backend supports runtime hook
events. Status of the facts themselves: `implemented` for the reduction, `uninspected` for whether
the hooks actually observe everything the sandbox executes.

**Anti-conflation note.** These host-recorded facts (OBJ-09) are a different object from the
model-reported `changed_files` (OBJ-08). The summary persists *counts* of the former and of the
latter side by side (`session.py:241-249`), which makes the distinction invisible to a reader of the
rendered summary.

---

## 5.4 Conditional surface inspections

Included only where they materially alter the analysis question, a control path, evidence strength,
or a lens result. **This is not a taxonomy and not a maturity ladder.**

| Surface | Why material here | Finding | Status |
|---|---|---|---|
| **Permissions / execution boundary** | It is the only thing standing between model-written code and the operator's real files, and it decides whether "audit this repo" is a safe delegation. | Fractal implements **no approval gate, no command policy, and no allow/deny list**. Isolation is wholly delegated to sbx: `SbxBackend` with `DirectWorkspaceMount(host_path == sandbox_path)` for the workspace and every `--include` dir, i.e. read/write passthrough to real host paths (SRC-1 `agent/service.py:158-197`). Doctrine claims container isolation with no network by default (`CLM-10`) and simultaneously concedes "There is no robust approval/sandbox policy yet" (`CLM-12`). The only host-side input guards found are `include_path` rejecting symlinks and non-directories (SRC-1 `cli.py:70-79`) and the `.fractal` exclusion. | Fractal side `implemented` (as an absence, within the inspected boundary); sbx side `uninspected` (`SRC-8`) |
| **Observability** | It carries the evidence a delegating agent or operator would rely on. | Three tiers: live `FractalRuntimeEvent` lines, per-iteration `FractalIterationEvent` rendering under `--verbose` (default-on for `-p`), and the persisted `RunTrace`. Under `--quiet` all three are suppressed — the skill file itself warns that `--quiet` loses the session id, changed files, and cost, and recommends redirecting stderr instead (SRC-5 SKILL.md:90). | `implemented` |
| **Providers / model authority** | Model choice is the system's main capability lever under `CLM-04`, and it is resolved by a layered policy rather than a flag. | Precedence: global TOML < project `.fractal/config.toml` < `FRACTAL_*` env < CLI flags (SRC-1 `config.py:256-310`). `--lm` is documented as bypassing config resolution entirely (SRC-2 flag table). Sub-model defaults to following the main model unless separately selected (SRC-1 `runtime.py:138-179`). A provider may declare `restricted_models` that rejects any other model id at runtime (SRC-5 add_provider SKILL.md). Secrets are never stored in config — only references: env var names, auth-source names, or paths, enforced by pydantic validators that reject raw secret fields (SRC-1 `config.py:56-80, 107-110, 150-153`). Twelve providers plus a custom OpenAI-compatible endpoint. The TUI warns when a project config overrides an interactive `/model` or `/provider` choice (SRC-1 `tui/app.py:633`). | `implemented` |
| **Governance of the workspace's own instructions** | `AGENTS.md` is user-authored text that enters every prompt, so it is a standing authority channel. | Loaded fresh per turn, truncated at 20 000 chars, and declared subordinate to the current `user_message`. No validation, signing, or provenance check. Note the recursion hazard this creates for a delegating agent: an `AGENTS.md` inside a workspace the caller pointed Fractal at becomes an instruction channel to Fractal's model (`BAP-02`). | `implemented` |
| **Packaging / distribution** | It is how the bundled skill and the `curl | sh` installer reach a machine, and the skill is itself a behavioral-authority artifact (`BAP-07`). | Installed as an isolated uv/pipx tool; the bundled skill is installed into a *calling agent* with `npx skills add <github URL>`; the skill's own preflight instructs the calling agent to run `curl -LsSf https://fractal.trampoline.ai/install.sh | sh` if `fractal` is missing. | `implemented` |
| **Version check** | Inspected and found **non-material** to any control path: a background PyPI check whose failures are silent and which is skipped under `--json`. Recorded only so its exclusion is not implicit. | `implemented`, non-material | SRC-1 `version_check.py` (grep only), `cli.py:630-634` |

Surfaces **not** inspected and the conclusions that prevents: `providers.py`, `onboarding.py`,
`credentials.py`, `connectivity.py`, and `config_commands.py` were read only at symbol level, so no
conclusion is offered about credential storage mechanics, the live connectivity probe, or the
onboarding flow's failure modes. `tests/**` was inspected by filename only (SRC-7), so **no
conclusion is offered about what the 200+ claimed tests actually verify** — including the interrupt-
recovery property that `runtime.py:256-262` cites a test to support.
