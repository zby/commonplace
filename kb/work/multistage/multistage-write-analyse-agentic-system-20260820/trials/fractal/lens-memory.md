# Lens: memory / context — run `AAS-2026-08-20-fractal-01`

**System:** Fractal (`github.com/Trampoline-AI/fractal`). **Frozen revision:** `5954a07d464feeaf6c311a9fa5ca2e54200a6794`.
**Lens:** accumulated-from-use retention and read-back. **Sources:** cites the shared `SRC-*` register in
`evidence-packet.md` §2; no source was reacquired, refreshed, or widened.

**Status vocabulary available in this run:** `absent`, `inapplicable`, `uninspected`, `claimed`, `implemented`.
No run was executed, so no `observed` and no `causally supported` conclusion appears anywhere below.

**Working definition applied throughout** (packet §5): *memory read-back* = material accumulated or changed
**through use** returning to a later invocation. Static shipped material and ordinary within-turn state are
retained state, not read-back.

---

## 1. Retained operative parts inventory

Rows are keyed to registered `OBJ-*` IDs. Where one registered ID bundles parts with different producers or
authority paths, the row is split as `OBJ-nn (part: …)` — this annotates the existing ID, it does not mint a
new one. Genuinely new material objects are requested in §7.

| ID (part) | Storage substrate | Representational form | Persistence | Lineage (how it comes to exist) | Producer | Consumer | Invalidation / regeneration | Promotion path |
|---|---|---|---|---|---|---|---|---|
| OBJ-03 `SessionSummary` / `SummaryTurn` | session JSON on disk (OBJ-13) | typed pydantic records | **unbounded** turn count; never trimmed | one record appended per user message, completed after the call | host (`FractalSession.add_user_message`, `add_agent_turn`) — never the model directly | `render_session_summary` → OBJ-02 | none: no trim, no expiry, no compaction, no rewrite path exists | none implemented |
| OBJ-02 rendered session summary | prompt string, in memory | natural-language text block | **regenerated from OBJ-03 every turn**; not stored | pure projection of OBJ-03 at call time | `render_session_summary` (SRC-1 `session.py:368-390`) | main LM, unconditionally (baked into signature docstring) | regenerated per turn; stale only if OBJ-03 is stale | none implemented |
| OBJ-04 `session_history` list | session JSON on disk (OBJ-13) | typed pydantic, delivered as a REPL variable | **capped at last 20 turns** (`MAX_HISTORY_TURNS = 20`) | same append/complete lifecycle as OBJ-03 | host | main LM **only if it chooses to inspect the variable** | trimmed by count on every save and on every payload build (`session.py:188, 200, 218, 262, 278-279`) | none implemented |
| OBJ-05 `RunTrace` | nested inside OBJ-04 in the session JSON | typed object produced by CMP-12 (external) | persisted, subject to the 20-turn cap | returned by the external RLM call, or extracted from the raised exception (`runtime.py:326-347`) | CMP-12 (**uninspected**, SRC-8) | main LM via OBJ-04; host via `turn_usage_from_trace` | evicted with its history turn at turn 21 | none implemented |
| OBJ-06 `TurnUsage` (part: token/cost/duration/iteration counters) | inside OBJ-03 on disk | typed numeric | persisted, unbounded (rides OBJ-03) | derived from OBJ-05, explicitly not from model output (`session.py:38-44, 306-322`) | host | `/usage` display; `summarize_usage` totals | none | none implemented |
| OBJ-06 `TurnUsage` (part: `context_tokens`) | as above | integer | as above | last positive `step.usage.main.input_tokens` scanned backwards through the trace (`session.py:309-314`) | host | operator display only; **overwritten, not summed**, in `summarize_usage` (`session.py:301-302`) | replaced by each later non-zero turn value | none implemented |
| OBJ-07 `response` | OBJ-03 (verbatim) **and** OBJ-04 indirectly via the trace | natural language, **model-produced** | persisted, unbounded via OBJ-03 | model output field (`signature.py:97-102`) | main LM | main LM next turn via OBJ-02; operator via stdout/TUI | none | none implemented |
| OBJ-08 `changed_files` | OBJ-03 as a **count**; OBJ-04 as the full list | list[str], **model-produced** | persisted | model output field, passed through `_prediction_to_result` unchecked against host observation (`agent/service.py:205-217`) | main LM | main LM next turn (count via OBJ-02, list via OBJ-04); operator via stderr; caller via OBJ-15 | none; not reconciled against host hooks | none implemented |
| OBJ-09 (part: `files_read`) | OBJ-03 as a count; OBJ-04 as the full list | list[str], **host-recorded** | persisted | `RuntimeEventTracker` `after`-phase reduction over 12 file-API hooks (`events.py:206-219`) | host (CMP-07) | main LM next turn (count via OBJ-02, list via OBJ-04) | turn-local tracker; list evicted with its history turn | none implemented |
| OBJ-09 (part: `commands_run`) | as above | list[str], **host-recorded** | persisted | `before`-phase capture over 5 subprocess hooks, deduplicated, compound-call collapsed (`events.py:102-118`) | host (CMP-07) | as above | as above | none implemented |
| OBJ-09 (part: **persisted `files_modified` field**) | OBJ-04 field named `files_modified` | list[str] | persisted | **fed from OBJ-08, the model-reported `changed_files`** — `session.py:239` assigns `files_modified_list = _require_string_list(changed_files, …)` and `session.py:257` writes it to `history_turn.files_modified` | **main LM**, not the host | main LM next turn | none | none implemented |
| OBJ-13 session JSON file | `<state-root>/workspaces/<workspace-key>/sessions/<id>.json` (SRC-1 `session.py:435-471`) | JSON, `schema_version: 1` | durable across processes; workspace-keyed by resolved-path slug + SHA-256 prefix (`session.py:451-458`) | rewritten in full on every save (`session.py:187-192`) | host | `FractalSession.load`, `list_sessions` | **gated**: a mismatched `schema_version`, a non-object payload, a validation failure, or an embedded/requested `session_id` mismatch each yields an empty session plus a `RuntimeWarning` (`session.py:150-185`); unreadable files are copied to a `.bad-<UTC-stamp>` sidecar first (`session.py:483-494`) | none implemented |
| OBJ-11 workspace `AGENTS.md` | user's workspace filesystem | natural language, user-authored, truncated at 20 000 chars with an explicit truncation notice (`agent/service.py:28-43`) | as durable as the user's file | **authored by the human, not accumulated from Fractal runs** | human operator | main LM, unconditionally, in a dedicated prompt section (`signature.py:41-50`) | re-read fresh from disk each turn; no cache to invalidate | none implemented |
| OBJ-12 shipped skill texts | in-repo Python constants + `predict_rlm.skills` | natural language | static at the shipped revision | authored by Fractal's developers | developers | main LM via `skills=[…]` (`agent/service.py:96`) | changes only by shipping a new version | none implemented |
| OBJ-17 pre-turn context estimate | in-memory TUI cache | integer | ephemeral; cache key includes a SHA-256 digest of the summary plus per-history-turn `(turn_id, status, updated_at)` and the `AGENTS.md` `mtime_ns`/size (`context_meter.py:19-53, 188-203`) | recomputed by rebuilding the *next* turn's message list and token-counting it | host (CMP-09) | **operator toolbar only** (`tui/app.py:425-446`) | invalidated whenever the cache key changes | none implemented |

**Promotion path finding: `absent`.** Across the whole inspected host layer there is no code path that moves any
retained part to a stronger representational form or a stronger binding force — no distillation of OBJ-03 into a
rule file, no writing of learned material into OBJ-11, no derivation of a skill (OBJ-12) from history. Inspected
boundary: the whole `src/fractal/**` host layer (SRC-1). This prevents any conclusion that Fractal accumulates
durable knowledge beyond a single session's transcript-shaped record.

---

## 2. Write side, separated from read-back

### 2.1 Write agency

| Question | Finding | Status | Evidence |
|---|---|---|---|
| Manual write (operator or model can deliberately commit something to memory) | **absent**. The full slash-command surface is `/help /sessions /resume /new /model /provider /usage /verbose /exit /quit` — none writes, edits, deletes, or compacts retained material. No model output field targets memory: the signature declares exactly two outputs, `response` and `changed_files`. | `absent` | SRC-1 `tui/app.py:59-70`; `signature.py:97-106` |
| Automatic write | **implemented**, and it is the only write agency. Every turn writes unconditionally, with no gate, filter, salience test, or relevance judgment anywhere in the path. | `implemented` | SRC-1 `runtime.py:222-223, 263-322` |

Consequence: what is retained is a function of *what happened*, never of *what was judged worth keeping*. There
is no curation stage to inspect.

### 2.2 Acquisition and index maintenance vs curation

| Stage | Finding | Status | Evidence |
|---|---|---|---|
| Acquisition (pre-call) | `add_user_message` appends a `SummaryTurn` **and** a `pending` `SessionHistoryTurn`, then saves to disk **before** the RLM call is issued. | `implemented` | `runtime.py:222-223`; `session.py:203-219` |
| Acquisition (post-call) | The same turn records are completed in place with status, response, file/command lists, trace, and error; the file is rewritten. Four distinct statuses are written: `succeeded`, `max_iterations`, `failed`, `interrupted`. | `implemented` | `runtime.py:263-322`; `session.py:221-262` |
| Index maintenance | The only index is `list_sessions`, a directory `glob` over `sessions/*.json` sorted by filesystem `mtime`. It is computed on demand, never stored, and skips unreadable or foreign files — the docstring itself says listing "is a navigation aid, not a validation pass". No content index, no embedding, no keyword index, no cross-session index exists. | `implemented` (listing) / `absent` (content index) | `session.py:402-432` |
| Curation | **absent**. No selection, ranking, scoring, tagging, or approval step exists between acquisition and retention. | `absent` | inspected boundary: `session.py`, `runtime.py` in full (SRC-1) |

### 2.3 The named maintenance operations

Each row states the finding for the inspected boundary (the `fractal` host package, SRC-1, read in full for the
files named in the register).

| Operation | Status | Evidence and reasoning |
|---|---|---|
| Consolidation | **absent** for OBJ-03. The rendered summary is a per-turn loop that emits each turn's fields in order; nothing merges, groups, or rewrites across turns. `render_session_summary` is the only transformation and it is a field projection. | `session.py:368-390` |
| Deduplication | **absent at the turn level**; **implemented only within one turn's event lists**, where `_append_unique` suppresses repeats of the same path or command string. Two turns that read the same file produce two independent records. | `events.py:420-423` vs `session.py:203-262` |
| Evolution / revision of a retained record | **absent** after completion. `add_agent_turn` writes a pending record once; no later call reopens or amends a completed turn, and no API for doing so exists. | `session.py:221-262` |
| Synthesis | **absent**. Nothing generates new retained content from retained content. No LM call is made for summarization, compaction, or reflection anywhere in the host layer — the only LM call per turn is the single `predictor.acall`. | `agent/service.py:120-129`; grep over `src/fractal/**` finds no second call site |
| Invalidation (semantic) | **absent**. There is no staleness model, no contradiction check, no supersession, and no way to mark a retained turn wrong. Failed and interrupted turns are retained *as* failures, not invalidated. | `runtime.py:263-296`; `session.py:57` |
| Invalidation (structural) | **implemented**, and it is whole-file, not per-record: schema-version mismatch, non-object JSON, validation failure, or session-id mismatch each discards the *entire* stored session and starts empty, with a `RuntimeWarning` and (for read errors) a `.bad-<stamp>` backup copy. | `session.py:133-185, 483-494` |
| Decay | **absent** as a time or relevance function. The only eviction is a **positional count cap**: `history = history[-20:]`. It is age-ordered only incidentally, because turns are appended in order. OBJ-03 has no cap at all. | `session.py:23, 278-279` |
| Promotion | **absent** — see §1. | whole host layer (SRC-1) |

### 2.4 Raw traces vs distilled retained artifacts

The two layers are materially different artifacts with different bounds, and the distinction is real:

| | OBJ-03/OBJ-02 (summary layer) | OBJ-04/OBJ-05 (history layer) |
|---|---|---|
| Content | user message **verbatim**, agent status, agent response **verbatim**, three integer counts, error string | user message, status, full path lists, command list, full `RunTrace`, error |
| Bound | unbounded turn count | last 20 turns |
| Delivery | prompt text, always present | REPL variable, opt-in |
| Evidence | `session.py:66-74, 368-390` | `session.py:76-87, 23` |

**The "compressed" label does not survive inspection as semantic compression.** CLM-11 and SRC-3
§"Structured Session Summary" call the summary "compressed structured trajectory context". The implemented
mechanism is **field projection plus cardinality reduction**: it drops the trace, the code, the REPL outputs and
the path/command *lists*, replacing the lists with `len()` counts; it copies the user message and the agent
response through **unchanged and untruncated**. So the summary grows without bound in the two fields most likely
to be long, and it is not a distillation of the trace — it is a different, thinner recording made in parallel
from the same turn. Status of "compression" as a semantic operation: `absent`. Status of "field projection":
`implemented`. Per the standing rule, the curation label "compressed" does not establish semantic
transformation.

**Producer-provenance defect on the retained modification record.** `RuntimeEventTracker` computes a
host-observed `files_modified` list (`events.py:89, 216-219`), but **no caller ever reads it**: `runtime.py`
passes only `files_read` and `commands_run` from the tracker (lines 233-234, 267-268, 279-280, 291-292,
306-307, 317-318), and the persisted field named `files_modified` is filled from the **model-reported**
`changed_files` (`session.py:239, 257`). A repository-wide grep for `files_modified` outside `events.py`
returns only the `session.py` sites. Two consequences for the retained record:

1. What a later turn reads back as "files modified" is model self-report, matching the project's own caveat
   CLM-08 and standing against the contributor policy CLM-05 ("prefer host-side truth over model-reported
   truth"). Status: `implemented` (the wiring), and the conflict between CLM-05 and CLM-08 is preserved, not
   resolved.
2. On `failed` and `interrupted` turns `changed_files` is not passed at all, so the retained `files_modified`
   is `[]` even where the host tracker had observed writes. The retained record therefore understates
   modification exactly on the turns where a later turn most needs it. Evidence: `runtime.py:263-296` omits
   `changed_files=`; `session.py:239` defaults `None` to `[]`.

### 2.5 What a failed, interrupted, or exhausted turn retains

| Turn outcome | Retained | Evidence |
|---|---|---|
| `succeeded` | response, model `changed_files`, host `files_read`/`commands_run`, full trace, usage | `runtime.py:312-321` |
| `max_iterations` | same as succeeded **plus** an explicit error string; deliberately not marked success | `runtime.py:298-311`; `session.py:24-26` |
| `failed` | error text, trace extracted from the exception, host `files_read`/`commands_run`; **no response, no changed_files** | `runtime.py:286-295` |
| `interrupted` (SIGINT) | `INTERRUPTED_ERROR`, trace if extractable, host `files_read`/`commands_run` | `runtime.py:229-238, 263-272` |
| interrupted **before** the call | the `pending` history turn plus an `interrupted` summary turn — the pre-call write already happened | `runtime.py:222-223, 229-238` |

The pre-call write is what makes this possible: the user message is durable before any model call, so a crash
mid-call still leaves a `pending` record. This is write-side durability, not read-back.

---

## 3. Annotation of the runtime-owned context routes

Read-back direction is stated **from the receiving agent's perspective**: *push* = the material arrives in the
receiving agent's context without any act by that agent; *pull* = the receiving agent must act to obtain it.

| Route | Delivers | Accumulated from use? | Direction | Selection signal | Targeting | Scope and budget | Delivery / consumption point | Behavioral-faithfulness test |
|---|---|---|---|---|---|---|---|---|
| **RTE-06** | OBJ-02 (rendered summary) + OBJ-11 + base instructions | **Yes** for the summary portion — this is the one unconditional memory read-back path | **push** | **none** — every turn of the current session is included; there is no query, no recency weighting, no relevance filter | **untargeted**; not conditioned on the current `user_message` (which is a separate input field, `signature.py:87-89`) | scope = the whole current session; **budget = none**, no token cap, no turn cap, no truncation on OBJ-03 (contrast the 20 000-char cap that *does* exist for OBJ-11 at `agent/service.py:38-42`) | the `dspy.Signature` docstring, i.e. prompt text present before the model's first decision | **absent** — nothing checks that the delivered text changed behavior; nothing even checks it was read |
| **RTE-07** | OBJ-04 (+ nested OBJ-05) | **Yes** | **pull** — declared as an `InputField` that PredictRLM exposes "primarily as REPL variables with prompt previews"; the model must run Python to inspect it | model's own initiative, prompted by the instruction text "For exact prior REPL reasoning, code, outputs, tool calls, or predict calls, inspect `session_history` from Python" | self-targeted by the model; Fractal supplies no query and no index | last 20 turns, whole payload handed over at once; **no host-side budget on trace size** — the docstring at `session.py:198-200` acknowledges "Full traces can be large" and gives the cap as the mitigation | REPL variable inside the external interpreter (CMP-12/CMP-13, **uninspected**) | **absent**; moreover whether the variable is ever materialized, previewed, or truncated is `uninspected` (SRC-8) |
| **RTE-08** | OBJ-10 workspace + included paths | **No** — these are live host paths, not material accumulated by Fractal's own use. Workspace *files* do change across turns, but as the object of work, not as a memory store Fractal maintains. | push (the variable) / pull (the file contents) | n/a for memory purposes | n/a | n/a | REPL variables naming real sandbox-visible paths | n/a |
| **RTE-09** | OBJ-12 shipped skills | **No** — static shipped material; identical on every invocation | push | fixed list `[filesystem_coding_skill, spreadsheet, pdf, docx]`, unconditional | none | fixed | injected into `PredictRLM(skills=…)` | `absent`; handling is `uninspected` (CMP-12) |
| **RTE-11** | (state) the 20-turn trim | write-side | — | — | — | — | — | — |
| **RTE-19** | session selection | **gates every route above** | — | see §3.2 | — | — | — | — |

### 3.1 Why OBJ-11 and OBJ-12 are *not* memory read-back

Both are delivered into the model's context every turn, and both carry real behavioral authority (BAP-02,
BAP-05). Neither is memory read-back under the packet's §5 definition, and the reason differs:

- **OBJ-11 (workspace `AGENTS.md`)** is user-authored and read fresh from the workspace each turn
  (`agent/service.py:31-43`, called at `signature`-build time from `agent/service.py:91`). Fractal never writes
  it — a grep of `src/fractal/**` finds `AGENTS.md` only at the two read sites (`agent/service.py:33`,
  `context_meter.py:38`). It changes only when the human edits it. It is *durable instruction*, and it would be
  memory read-back only if the system could write into it from experience; no such path exists, so calling it
  memory would upgrade a static-file read into accumulation-through-use. Status: retained state, **not**
  read-back.
- **OBJ-12 (shipped skills)** is a compiled-in constant (`agent/skills.py`, 315 lines) plus three imported
  `predict_rlm.skills` modules. It cannot vary within an installation. Status: static shipped material,
  **not** read-back.

Their presence in context is `implemented`. Their *activation* is `uninspected` for OBJ-12 and `uninspected`
for OBJ-11 alike — see §4.

### 3.2 RTE-19 and what fresh-by-default does to read-back in practice

`FractalRuntime.create` calls `FractalSession.load(workspace)` with **no** `session_id`, and `load` returns a
brand-new empty session whenever `session_id is None` — the in-code comment is explicit: "Multi-session storage
exists before resume selection does… each process gets a fresh ID instead of silently choosing the wrong prior
conversation" (`session.py:120-128`; `runtime.py:92`). Resume happens only on an explicit
`--resume SESSION_ID` (`cli.py:108-112`, applied at `runtime.py:109-111`) or the `/resume <id>` slash command
(`tui/app.py:516-517, 544-554`); `/new` discards the current session object outright (`runtime.py:118-119`).

Consequences, stated without upgrading implementation to deployment:

1. In the **default** interactive invocation, RTE-06 and RTE-07 carry read-back **only within the running
   process**. On the first turn of a fresh session, RTE-06 delivers the literal string
   "No prior Fractal session context." and RTE-07 delivers `[]` (`session.py:369-370`; `signature.py:54`).
2. In the **default headless** invocation (`fractal -p`, one process = one turn, RTE-03), the session is fresh
   and single-turn, so **no memory read-back occurs at all** on that turn — the summary is the empty sentinel
   and the history is empty. Headless Fractal writes a session file that, by default, nothing will ever read.
   This applies to the external-delegation route RTE-20 / CLM-03 as well: a calling agent that shells out to
   `fractal -p` per CMP-11 gets a memoryless worker unless it threads `--resume` itself.
3. Cross-session read-back is therefore **implemented but opt-in and manually keyed**: the operator must know
   or look up a 32-hex `session_id`. `/sessions` exists to make that findable, showing id, mtime, turn count,
   and first message (`session.py:393-432`; `tui/app.py:566-582`), but no default, no "last session", and no
   "most recent" shortcut exists.
4. Retention outlives its consumer. Session files accumulate under
   `<state-root>/workspaces/<key>/sessions/` with **no deletion, expiry, quota, or pruning path anywhere in
   the host layer**. Status: retention `implemented`, garbage collection `absent`.

### 3.3 `context_meter` (OBJ-17) is a meter, not a read-back path

`build_next_context_messages` reconstructs the entire next-turn message list — it builds the signature from
`session.summary()` and `load_workspace_instructions`, instantiates a `PredictRLM` with `lm=None`, runs
`_prepare_file_io` and `_build_variables`, and formats through `ChatAdapter` — then stops (`context_meter.py:61-121`).
Its own docstring says it "mirrors the setup path in `FractalAgent.aforward` but stops before calling the LM".
The output is an integer consumed by the TUI bottom toolbar (`tui/app.py:425-430`). No model ever sees it.
**Classification: instrumentation for the human operator, not a read-back path.** Status: `implemented` as a
meter; `inapplicable` as memory read-back.

Two lens-relevant properties fall out of it anyway. First, it is the only place in the host layer where the
size of accumulated context is measured at all — but it only *displays*, it never gates, trims, or triggers
anything, so it is a gauge with no actuator. Second, it silently swallows every failure
(`except Exception: tokens = None`, `tui/app.py:441-444`; and `count_messages_tokens` falls back
litellm → tiktoken-by-model → `o200k_base` → `cl100k_base` → `None`), so a displayed number and an absent
number are not distinguishable as to cause.

---

## 4. Four separate findings per delivered item

Kept strictly separate: **(a) context presence** = the material is in the assembled input; **(b) deployed
wiring** = the delivery path exists and is reached in a default installation; **(c) activation** = the
receiving model actually attended to it; **(d) causal effect** = it changed behavior.

| Delivered item | (a) Context presence | (b) Deployed wiring | (c) Activation | (d) Causal effect |
|---|---|---|---|---|
| OBJ-02 rendered summary (RTE-06) | `implemented` — concatenated into the signature `__doc__` at `signature.py:55-65`, from `runtime.py:244` | `implemented` for the host handoff; whether DSPy/PredictRLM transmits the docstring verbatim to the provider is `uninspected` (SRC-8) | `uninspected`. No run occurred; and the host records nothing about attention. The design comment "must be visible before the RLM chooses to inspect variables" (`signature.py:52-53`) states an *intent*, not a measurement | `uninspected`. No experiment; the packet forbids `causally supported` in this run |
| OBJ-04 `session_history` (RTE-07) | `implemented` as an `InputField` declaration (`signature.py:90-95`) and as a passed argument (`agent/service.py:126`). **Whether it is present as prompt text or only as a REPL binding is `uninspected`** — the mechanism belongs to CMP-12 | `implemented` up to the call boundary | `uninspected`, and structurally weaker than for OBJ-02: activation here requires an affirmative model act. Nothing in the host layer records whether `session_history` was ever touched — no hook targets variable access (`events.py:15-52` hooks only file and subprocess APIs) | `uninspected` |
| OBJ-11 `AGENTS.md` (RTE-06) | `implemented` when the file exists — its own prompt section (`signature.py:41-50`) | `implemented`; empty-string short-circuit when the file is missing or unreadable (`agent/service.py:34-37, 41`) | `uninspected` | `uninspected`. Note that BAP-02's declared subordination to `user_message` is prompt text asserting a precedence rule; it is unenforced, so even its *stated* effect is `claimed` |
| OBJ-12 shipped skills (RTE-09) | `implemented` at the argument boundary (`agent/service.py:96`) | `implemented`; how PredictRLM renders a `Skill` into context is `uninspected` (SRC-8) | `uninspected` | `uninspected` |
| Host-recorded `files_read` / `commands_run` reaching a later turn | `implemented` — counts in OBJ-02, lists in OBJ-04 | `implemented`, **conditional**: SRC-3 §"Known Limits" states tracking works only when the active backend supports runtime hook events, and `build_predict_runtime_hooks` returns `[]` if `predict_rlm.RuntimeHook` cannot be imported (`events.py:277-281`), which silently disables the whole observation path with no warning | `uninspected` | `uninspected` |
| "Files modified" reaching a later turn | `implemented`, but the delivered content is **model self-report** (§2.4) | wiring `implemented`; the host-observed alternative is computed and discarded | `uninspected` | `uninspected` |

**The distinction that matters most here:** for OBJ-02 the host controls presence, so (a) is a host fact. For
OBJ-04 the host controls only the handoff; presence-as-text, activation, and effect all sit behind the
uninspected CMP-12 boundary. Reporting both as "the model has access to session history" would collapse (a)
into (c) for the second and would collapse a host fact into an external one for both.

---

## 5. Authority

Registered `BAP-*` records carry the retained material. Restated by consumer / channel / force / horizon rather
than by family label:

| BAP | Carries | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|---|
| BAP-03 | OBJ-02 | main LM | always-visible prompt text | **informative, unenforced** | the turn; content spans the session |
| BAP-04 | OBJ-04 (+OBJ-05) | main LM | REPL variable, model-initiated | **informative, opt-in, unenforced** | the turn |
| BAP-02 | OBJ-11 | main LM | dedicated prompt section | directive, explicitly subordinate to `user_message`, **unenforced** | the turn |
| BAP-05 | OBJ-12 | main LM | `Skill` instruction text | prescriptive ("Do not implement grep by recursively reading every file in Python", `agent/skills.py:24-25`), **unenforced** | the turn |
| BAP-06 | OBJ-01 | main LM | `user_message` input field | overriding directive, by declaration only | the turn |

Three separations the evidence requires:

1. **No retained-material channel is enforcing.** Every path above is text handed to a model. The only
   enforcing paths in the whole system (BAP-09 sandbox mounts, BAP-10 config rejection, BAP-11 exit codes) carry
   no accumulated material. So Fractal's memory has **no** mechanism by which retention could constrain a later
   turn; it can only inform one. Status: enforcement over retained material `absent`.
2. **Precedence is asserted, not implemented.** BAP-02's subordination to `user_message` and BAP-06's override
   exist as sentences inside the same docstring the model may or may not follow (`signature.py:46-48`). No code
   resolves a conflict between them. Treating the declared ordering as an operative authority structure would
   upgrade prompt text to enforcement.
3. **Lineage and curation labels establish nothing epistemic.** Three labels in this system invite exactly that
   upgrade and must be blocked from it: "compressed" (§2.4 — field projection); "trustworthy" in CLM-06 /
   `session.py:38-44` (host-derived provenance for *token accounting* only, and it does not extend to the
   `files_modified` field on the same record, §2.4); and "preserves prior user messages and compressed agent
   results" in CLM-11 / `signature.py:61-64` (a description of which fields survive, not a warrant that the
   surviving text means what it meant in the original turn). None of the three is an acceptance step, and no
   acceptance step exists: nothing in the host layer ever judges a retained turn correct, current, or
   applicable. Status: acceptance/warrant machinery over retained material `absent`.

---

## 6. Limitations, each paired with the conclusion it prevents

| # | Limitation | Exact conclusion it prevents |
|---|---|---|
| L1 | `predict-rlm` 0.7.0 (SRC-8) was not obtained. How an `InputField` becomes a REPL variable, whether a prompt preview of `session_history` is emitted, whether traces are truncated in transit, and how `Skill` text is rendered are all unknown. | Prevents any conclusion about **what the model actually sees** for RTE-07 and RTE-09, and therefore any statement about the real context cost or real accessibility of the history layer. RTE-06 is unaffected only up to the same handoff. |
| L2 | No execution: no `sbx`, no credentials, no virtualenv, and the checkout must not be mutated (packet §2). | Prevents every `observed` and `causally supported` status in this file. Specifically prevents concluding that the summary is read, that `session_history` is ever inspected, that read-back changes any output, or that the 20-turn cap is ever reached in practice. |
| L3 | `RunTrace`'s internal schema is defined in the uninspected dependency; only `trace.steps[*].usage.main.input_tokens`, `trace.usage.{main,sub}`, `trace.duration_ms`, `trace.iterations`, and `trace.status` are touched by Fractal (`session.py:306-322`; `runtime.py:301`). | Prevents any conclusion about the **fidelity or completeness** of the retained trace, and so about what "exact recall" (`signature.py:93-94`) actually recovers. CLM-09 ("every peek, chunk, sub-call… fully readable in the trace") stays `claimed`. |
| L4 | Test bodies were not read; only the 22 filenames are registered (SRC-7). `tests/test_runtime_interrupt_recovery.py` is named in a source comment (`runtime.py:262`) but its assertions are unread. | Prevents any conclusion that the persistence, trimming, schema-gating, or interrupt-retention behaviors described above are **verified** rather than merely written. Every status in §1–§3 is `implemented`, never "checked". |
| L5 | Single frozen revision, no history inspected. | Prevents any conclusion about direction of travel — e.g. whether the absent consolidation/decay/promotion paths are deliberate scope or unbuilt work. The in-code comments ("Multi-session storage exists before resume selection does", `session.py:124-127`; "History is bounded and passed directly as structured data **for now**", SRC-3 §"Known Limits") signal intent but are `claimed`, not evidence of a trajectory. |
| L6 | The doctrine layer (SRC-2, SRC-3, SRC-4) is stale in known ways — CONF-1 (three artifacts state the wrong session path), CONF-5 (two statuses documented, four implemented), plus the new §7 discrepancy on summary contents. | Prevents using any documentation statement about the memory layers as independent corroboration of implementation. Where doctrine and code disagree here, both are reported; neither resolves the other. |
| L7 | Backend-conditional observation: the runtime-hook path silently yields `[]` when `RuntimeHook` is unimportable (`events.py:277-281`), and SRC-3 §"Known Limits" makes the same caveat. No backend inventory was obtained. | Prevents concluding that host-recorded `files_read`/`commands_run` are present in **any given deployment**, and therefore prevents treating OBJ-09's host provenance as an unconditional property of the retained record. |
| L8 | The hot sandbox (CMP-13, `reuse=True` by default, `agent/service.py:158-175`) persists across turns and across processes, and its internal state — interpreter globals, container filesystem outside the mounts — was not inspected. | Prevents a complete answer to "what accumulates through use in Fractal". A second accumulation substrate exists outside the session store, and this run can say nothing about whether it constitutes read-back. See NEW-2. |

---

## 7. NEW RECORDS REQUESTED (orchestrator must assign canonical IDs)

| Ref | Kind | Proposed description | Evidence |
|---|---|---|---|
| NEW-1 | Operative object (or an authorized split of OBJ-09) | **Host-observed `files_modified` list — computed and discarded.** `RuntimeEventTracker.files_modified` is maintained on every write-mode file hook but has **no reader anywhere outside `events.py`**. The persisted field of the same name is fed from the model-produced OBJ-08. Requesting either a distinct ID for the discarded host list, or an authorized three-way split of OBJ-09 by producer, because OBJ-09's current single description ("host-recorded from runtime hooks") is accurate for `files_read` and `commands_run` and inaccurate for the persisted `files_modified`. | SRC-1 `events.py:89, 216-219` (produced); `runtime.py:233-234, 267-268, 279-280, 291-292, 306-307, 317-318` (not passed); `session.py:239, 257` (field filled from `changed_files`) |
| NEW-2 | Operative object | **Hot sandbox residual state.** The `sbx` container is named deterministically per (workspace + include set) and reused by default across turns *and across processes*; on SIGINT the interpreter is deliberately **not** rebuilt. Interpreter globals and container-local files therefore persist through use, outside the session store and outside every registered route. Substrate: container. Status within this run: `uninspected` (CMP-13/SRC-8). | SRC-1 `agent/service.py:140-175`; `runtime.py:255-262`; RTE-04, RTE-18 |
| NEW-3 | Route | **Session listing as an operator-facing navigation route:** `list_sessions` → `/sessions` display → operator reads a `session_id` → `/resume`. This is the only implemented mechanism by which cross-session read-back is initiated, its selection signal is human, and it is not covered by RTE-19's "explicit `--resume`/`/resume`" phrasing. | SRC-1 `session.py:393-432`; `tui/app.py:556-582` |
| NEW-4 | Evidence conflict (proposed CONF-6) | **Documented summary contents vs implemented summary contents.** SRC-3 `docs/session-management.md:26-28` states the summary preserves "files read from runtime hook events", "files modified", and "commands run from runtime hook events". The implementation renders only `files_read_count`, `files_changed_count`, `commands_run_count` — integers, never the lists — and `files_changed_count` derives from model-reported `changed_files`, not from hook events at all. | SRC-3 `docs/session-management.md:20-29` vs SRC-1 `session.py:239, 244-246, 385-387` |
| NEW-5 | Evidence conflict (proposed CONF-7) | **Stale `.fractal` workspace exclusion.** Both `FractalAgent.aforward` and `context_meter` append `.fractal` to `Workspace.exclude` to keep session data out of the workspace view, but sessions are stored in the global state dir (CONF-1's implementation side), so the exclusion protects a location that this revision no longer writes. Small, but it is a second artifact carrying the superseded storage model into executable code rather than into docs. | SRC-1 `agent/service.py:79-80`; `context_meter.py:76-77`; vs `session.py:435-471` |
