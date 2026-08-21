# Fractal — agentic-system analysis · run `AAS-2026-08-20-fractal-01`

**Canonical entry document.** This run's logical result is one package of five physical parts sharing
one identity; every `SRC-*`, `CMP-*`, `OBJ-*`, `RTE-*`, `BAP-*`, `CLM-*`, and `CONF-*` ID resolves
across all of them.

| Physical part | Logical records it carries |
|---|---|
| `result.md` (this file) | 1, 2, 6, 8, 9, 10, 11 (+ pointers to the rest) |
| [`evidence-packet.md`](./evidence-packet.md) | 3 (source register), 4 (shared records), frozen boundary text |
| [`runtime-account.md`](./runtime-account.md) | 5 (mandatory runtime baseline) |
| [`lens-memory.md`](./lens-memory.md) | 7a (memory/context lens output) |
| [`lens-epistemic.md`](./lens-epistemic.md) | 7b (epistemic lens output, via the invoked instruction) |
| `trial-notes.md` | **not part of the result** — trial apparatus |

---

## Record 1 — Run and staging identity

- **Run/result ID:** `AAS-2026-08-20-fractal-01`
- **Staging identity:** `kb/work/multistage-write-analyse-agentic-system-20260820/trials/fractal/`
- **Status:** retained under the staging identity. **Not published** — see record 11.
- **Consumer:** an analysing agent or maintainer. **Force:** analysis, not endorsement; nothing here
  accepts Fractal's own claims.

## Record 2 — System boundary, revision, evidence tier

**System.** Fractal — `github.com/Trampoline-AI/fractal`, PyPI `fractal-rlm`. A terminal CLI coding
agent that is a thin host layer over `predict-rlm`, described by its authors as a "self-harnessed
Recursive Language Model" runtime. In scope for this instruction: its deployed behavior depends on
model calls plus surrounding machinery.

**Boundary (by function).** The `fractal` Python package as checked out — every facility that decides
scheduling, context selection, retained state, action execution, checking, acceptance, or authority
for a turn. Actors in scope: the human operator, the main LM, the sub-LM, and an external calling
agent. **Excluded:** `predict-rlm` 0.7.0 (`CMP-12`), `sbx`/Docker Sandboxes (`CMP-13`), `dspy`,
`litellm`, `tiktoken`, and all provider services. Full list in [`evidence-packet.md` §1](./evidence-packet.md).

> **Boundary kind: subsystem-only with respect to deployed agentic behavior.** Fractal's host layer
> is inspected whole; the loop that actually produces the behavior (`RTE-05`, inside `CMP-12`) is an
> external dependency inspected only at its call interface. **No whole-system conclusion about the
> RLM recursion, its context management, its trace fidelity, or its sandbox isolation is available
> from this run.**

**Revision.** `5954a07d464feeaf6c311a9fa5ca2e54200a6794`, authored 2026-06-23. Working tree clean at
inspection; nothing was fetched, pulled, or mutated. **Analysis cutoff:** 2026-08-20.

**Overall evidence tier: `code-grounded`, scoped to the declared host-layer boundary.** Every material
loop Fractal owns (L-A, L-C, L-D, L-E, L-F in record 5) rests on inspected implementation. The one
material loop it does not own — L-B / `RTE-05` — is recorded as `uninspected`, non-silently, with
every conclusion it prevents named. **No run was executed**, so no `observed` and no
`causally supported` status exists anywhere in this result. (The instruction's tier rule does not
cleanly decide this split-boundary case; the choice and its alternative are recorded in
`trial-notes.md` F-2.)

## Record 3 — Source register

→ [`evidence-packet.md` §2](./evidence-packet.md). Nine sources, `SRC-1`…`SRC-9`, each with kind,
identity, revision, evidence layer, inspected scope, citation-anchor convention, and access gaps.
`SRC-8` (`predict-rlm` 0.7.0) is registered as **named, pinned by hash, and not obtained**; `SRC-9`
records an artifact that doctrine references and that does not exist at this revision.

No source was added, reacquired, refreshed, or widened after the packet was frozen. Both lens workers
consumed the packet and confirmed the same.

## Record 4 — Shared component / object / route / claim / authority records

→ [`evidence-packet.md` §3](./evidence-packet.md): 14 `CMP-*`, 17 `OBJ-*`, 20 `RTE-*`, 11 `BAP-*`,
13 `CLM-*`, plus five pre-registered evidence conflicts `CONF-1`…`CONF-5` in §4.

**Registration deltas from this run** (record 8.1 explains each): `OBJ-09` split into `OBJ-09a` and
`OBJ-09b`; `OBJ-18` added; `RTE-21`, `RTE-22`, `RTE-23` added; `CONF-6`, `CONF-7`, `CONF-8` added.

## Record 5 — Runtime account (mandatory baseline)

→ [`runtime-account.md`](./runtime-account.md). Six material loops (L-A outer turn loop, L-B inner RLM
loop, L-C per-turn context assembly, L-D session write and outcome classification, L-E interrupt and
sandbox continuity, L-F headless single-turn), plus session selection, host-side action observation,
and six conditional surface inspections each with its materiality stated.

## Record 6 — Lens applicability dispositions

Both dispositions are explicit records. Neither is implied by an absent section.

### 6a. Memory/context lens — **applicable**

| Field | Value |
|---|---|
| Lens | memory/context |
| Disposition | **`applicable`** |
| Trigger evidence IDs | `OBJ-02`, `OBJ-03`, `OBJ-04`, `OBJ-05`, `OBJ-13`; routes `RTE-06`, `RTE-07`, `RTE-10`, `RTE-19` |
| Inspected boundary | `src/fractal/**` at `5954a07d` (`SRC-1`), plus `SRC-3` doctrine |
| Rationale | Two implemented paths carry material accumulated **through use** into a later invocation: the rendered session summary is pushed into the next turn's prompt text, and the bounded `session_history` (with the full `RunTrace`) is offered as a REPL variable. Both are written from the outcomes of prior turns and persisted to disk (`session.py:203-262, 187-192`). Not a borderline call. |
| Action | Lens run in a fresh worker on the frozen packet → [`lens-memory.md`](./lens-memory.md) |
| Prevented conclusions | None prevented by the disposition itself. The lens's own limits are its L1–L8. |

### 6b. Epistemic lens — **applicable**

| Field | Value |
|---|---|
| Lens | epistemic |
| Disposition | **`applicable`** |
| Trigger evidence IDs | `OBJ-07`, `OBJ-08`, `OBJ-09a`; claims `CLM-03`, `CLM-05`, `CLM-06`, `CLM-08`, `CLM-09`, `CLM-11` |
| Inspected boundary | `src/fractal/**` at `5954a07d` (`SRC-1`), plus `SRC-2`–`SRC-5` doctrine |
| Rationale | Two independent triggers. (i) A material route handles truth-apt content: `OBJ-07`, the agent `response`, is a natural-language claim about the workspace, and it is the marketed deliverable for audits, tracing, root-cause, and synthesis (`CLM-03`, `SRC-5` SKILL.md:36-51). (ii) The system makes consequential warrant claims: `CLM-05` is an explicit provenance policy ("prefer host-side truth over model-reported truth… for files changed, commands run, verification status, and errors") and `CLM-06` asserts a retained record "stays trustworthy". A system that writes down which of its records may be relied on has made a warrant claim. |
| Action | Invoked *Analyse an external system's epistemic architecture* in a fresh worker with a bounded subquestion, the frozen boundary and revision, the `SRC-*` register, the registered records, and the trigger evidence → [`lens-epistemic.md`](./lens-epistemic.md) |
| Prevented conclusions | None prevented by the disposition. The trigger fires on the *route*, not on whether the finding turns out positive — the eventual finding here is largely absence, which is a result, not a reason to withhold the lens. |
| Direct-adaptation exception | **Does not apply.** Config layering and model admission (`RTE-17`) and sandbox naming/reuse (`RTE-18`) are non-truth-apt policy updates; they stay in the runtime account and are additionally covered inside the invoked epistemic method because another trigger already made the lens applicable. |

## Record 7 — Lens outputs

- **7a — memory/context:** [`lens-memory.md`](./lens-memory.md). Retained-parts inventory; write side
  separated from read-back; annotation of `RTE-06`–`RTE-09`, `RTE-11`, `RTE-19`; four separate
  findings (presence / wiring / activation / causal effect) per delivered item; authority by
  consumer-channel-force-horizon; eight limitations paired with prevented conclusions.
- **7b — epistemic:** [`lens-epistemic.md`](./lens-epistemic.md). The invoked instruction's six
  blocks: source-and-claim boundary; epistemic-object inventory; authority-route ledger split by
  function; per-object lifecycle disposition; claim-versus-route comparison for all thirteen `CLM-*`;
  bounded conclusion.

Neither lens established its own boundary, revision, publication, or ID namespace. Neither used
`observed` or `causally supported`. Both cited only the frozen register.

---

## Record 8 — Cross-lens reconciliation

### 8.1 New records registered centrally

Both lenses returned new-record requests instead of minting IDs. Registered here; both lenses'
placeholder references resolve to these canonical IDs.

| Canonical ID | Kind | Content | Requested by | Evidence |
|---|---|---|---|---|
| **`OBJ-09a`** | object (split) | `RuntimeEventTracker.files_read` and `.commands_run` — genuinely host-recorded from runtime hooks, consumed into `OBJ-03` counts and `OBJ-04` lists | memory NEW-1, epistemic NEW-3 | `events.py:87, 89, 102-118, 215-219`; `runtime.py:233-234, 267-268, 291-292, 306-307, 317-318` |
| **`OBJ-09b`** | object (split) | `RuntimeEventTracker.files_modified` — host-observed write targets, **computed every turn and read by nothing outside `events.py`** | memory NEW-1, epistemic NEW-3 | `events.py:88, 219`; exhaustive `rg` for `files_modified` over `src/**` |
| **`OBJ-18`** | object | **Hot-sandbox residual state.** The sbx container is named deterministically per (workspace + include-set) and reused by default across turns *and across processes*; on SIGINT the interpreter is deliberately not rebuilt. Interpreter globals and container-local files therefore persist through use, outside the session store and outside every other registered route. Status: `uninspected` (`CMP-13`, `SRC-8`) | memory NEW-2, epistemic `RTE-18.E1` | `agent/service.py:140-183`; `runtime.py:255-262` |
| **`RTE-21`** | route | **Session-listing navigation route:** `list_sessions` → `/sessions` display → operator reads a `session_id` → `/resume`. The only implemented mechanism initiating cross-session read-back; its selection signal is a human | memory NEW-3 | `session.py:393-432`; `tui/app.py:556-582` |
| **`RTE-22`** | route | **Pre-turn context estimation.** `CMP-09` reconstructs the next turn's initial action-LM messages through `PredictRLM` private APIs, formats via `ChatAdapter`, token-counts with a `litellm`→`tiktoken` fallback chain; cache-keyed on workspace, include-set, session digest, model, `max_iterations`, and `AGENTS.md` stat. Consumed only by the TUI toolbar; never computed headless | epistemic NEW-1 | `context_meter.py:19-121, 124-168`; `tui/app.py:434, 442` |
| **`RTE-23`** | route | **Model-output type gate.** `_prediction_to_result` raises `TypeError` unless `response` is `str`, `changed_files` is `list[str]`, and `trace` is `RunTrace` or `None`; the error is caught and recorded as a `failed` turn. The only implemented gate anywhere on the path of `OBJ-07`/`OBJ-08` | epistemic NEW-2 | `agent/service.py:200-223`; `runtime.py:273-296` |
| **`CONF-6`** | conflict | **Documented vs implemented summary contents.** `docs/session-management.md:26-28` says the summary preserves "files read from runtime hook events", "files modified", and "commands run from runtime hook events". The implementation renders three integers, never the lists, and `files_changed_count` derives from model-reported `changed_files`, not from hook events | memory NEW-4 | `SRC-3` vs `session.py:239, 244-246, 385-387` |
| **`CONF-7`** | conflict | **Stale `.fractal` workspace exclusion.** Both `FractalAgent.aforward` and `context_meter` append `.fractal` to `Workspace.exclude` to keep session data out of the model's workspace view, but this revision stores sessions in the global state dir. The exclusion now guards the project config directory, not session state — a second artifact carrying the superseded storage model, this time in executable code rather than docs (cf. `CONF-1`) | memory NEW-5 | `agent/service.py:79-80`; `context_meter.py:76-77`; vs `session.py:435-471` |
| **`CONF-8`** | conflict | **Persisted `files_modified` contradicts its own field name and `CLM-05`.** `SessionHistoryTurn.files_modified` sits beside `files_read` and `commands_run` — both genuinely host-recorded — but is filled from model output, while an unused host-recorded list of the same name exists in `RuntimeEventTracker`. A reader of the session JSON cannot distinguish the provenances | epistemic NEW-4 | `session.py:80-82, 239, 257`; `events.py:88, 219`; `runtime.py:305-318`; `SRC-4` `CLM-05`/`CLM-08` |

**No rerun was triggered.** These are registrations of records already grounded in the frozen
boundary, not new sources or targeted reads that would invalidate downstream findings. `OBJ-09`'s
original packet description ("host-recorded from runtime hooks") was **inaccurate for the persisted
`files_modified` field**; the split corrects the lineage rather than renaming an object, and both
lenses had already worked with the corrected lineage, so their outputs stand as written.

### 8.2 Convergence — the strongest signal in the run

The two lenses ran **in parallel, in separate fresh contexts**, on the same frozen packet, with no
communication. They independently reached the same central finding by different routes:

- The **memory lens** reached it from the write side: the retained record a later turn reads back as
  "files modified" is model self-report, and the host's own measurement is discarded.
- The **epistemic lens** reached it from the warrant side: the host holds two independent claims about
  the same fact in the same process at the same moment, never compares them, and keeps the model's.

Because the finding rests on `rg`-verifiable absence of a call site rather than on either lens's
judgment, the convergence corroborates the *reading*, not merely agreement between two models.

### 8.3 Ownership — checked, and one overlap noted

| Owner | Owns | Verified |
|---|---|---|
| Runtime baseline | complete control and context routes, endpoints, progression | ✓ Both lenses annotated `RTE-06`–`RTE-11`, `RTE-13`, `RTE-19` by ID; neither redefined a route's endpoints |
| Memory lens | read-back direction, selection, targeting, budget, delivery point, activation | ✓ |
| Epistemic lens | transformation class, checking, disposition/acceptance, retention vs lifecycle integration, epistemic and operational authority | ✓ |

**Overlap:** `lens-memory.md` §5 states that "acceptance/warrant machinery over retained material is
`absent`". That is an epistemic-owned finding reached inside the memory lens. It is consistent with
the epistemic lens's `RTE-15.E3`, but the **epistemic lens's scoped statement governs**: the absence
is scoped to `src/fractal/**` at `5954a07d` and does not establish that no check occurs inside
`CMP-12`, nor that operators do not check by hand.

### 8.4 Shared-route consistency

Every shared route was checked for one revision, consistent sources, endpoints, objects, and `BAP-*`
references.

- `RTE-06` — runtime: assembly of three prompt sections. Memory: push, unconditional, no selection
  signal, **no budget**. Epistemic: `RTE-06.E1` non-ampliative lossy reshaping; `RTE-06.E2`
  acquisition/import. Consistent; no endpoint drift.
- `RTE-07` — runtime: REPL-variable delivery. Memory: **pull**, model-initiated. Epistemic:
  `implemented` delivery / `uninspected` inspection. Consistent.
- `RTE-13` — runtime: hook reduction. Memory: producer provenance. Epistemic: `RTE-13.E1`
  check/evidence production, `RTE-13.E2` evidenced discard. Consistent, and the `OBJ-09a`/`OBJ-09b`
  split resolves the packet's original conflation.
- `RTE-19` — runtime: fresh-by-default, explicit resume. Memory: consequences for read-back.
  Epistemic: `RTE-19.E1` integrity check → `RTE-19.E1d` disposition. Consistent; `RTE-21` now names
  the operator-mediated navigation half the packet's phrasing left implicit.

**Two label-to-status upgrades were blocked and stay blocked.** A curation label does not determine an
epistemic transformation: "compressed" (`CLM-11`) is a lossy field projection, not semantic
compression, and both lenses say so. Behavioral influence does not imply epistemic or operational
authority: `OBJ-02` reaches the model every turn and carries **no** enforcing force — the only
enforcing paths in the system (`BAP-09` sandbox mounts, `BAP-10` config rejection, `BAP-11` exit
codes) carry no accumulated material at all.

### 8.5 Preserved conflicts

`CONF-1`…`CONF-8` are preserved **as conflicts**. None was resolved by selecting the
strongest-sounding status. Where doctrine and code disagree, both are reported and neither resolves
the other. In particular `CLM-05` (host-side truth preferred) and `CLM-08` (changed files coerced from
model output) are recorded as a standing, self-declared contradiction that inspection sharpens rather
than settles.

---

## Record 9 — Bounded synthesis

Organized around the deployed system's progression. No system-wide epistemic grade is given. Nothing
here accepts Fractal's claims.

**Scheduling is human-paced and deliberately thin.** One submitted message becomes exactly one
`PredictRLM.acall`; there is no planner, no queue, no autonomous continuation, and no retry anywhere
(`RTE-02`, `RTE-03`). Slash commands are intercepted before any model call. The host's entire
iteration policy is the constant `max_iterations`, default 30. This is what `CLM-01` ("Fractal's loop
_is_ the model") amounts to at the host layer, and the claim is **supported there and only there**:
inspection confirms *where* the loop is, not *what it does*, because `CMP-12` was not obtained.
`CLM-07` ("adds exactly one thing: session management") understates what was found — the host also
implements action observation, turn-outcome classification, operational admission, sandbox lifecycle,
and a public output contract, and several of those are the only epistemically consequential host
routes that exist.

**Context assembly is two-tier by design, and the tiers differ in more than delivery.** A rendered
summary is pushed into prompt text and is always visible; the fuller `session_history` is a REPL
variable the model must choose to inspect (`RTE-06`, `RTE-07`). The in-code rationale — that
PredictRLM exposes input fields "primarily as REPL variables with prompt previews", so always-visible
memory needs prompt text (`CLM-13`) — is a claim about the uninspected dependency, though the
mechanism it justifies is plainly implemented. The consequences are the substance:

- The push tier has **no selection signal, no targeting, no token budget, and no trimming**. It is not
  conditioned on the current request. It carries every turn of the session.
- The pull tier is hard-capped at the last 20 turns, so file lists, command lists, and traces older
  than that are irrecoverable; only counts survive.
- What the reshaping keeps and drops is not neutral. `render_session_summary` copies the user message
  and the agent's `response` **verbatim** while collapsing the host-observed file and command lists
  into three integers and dropping the trace and usage entirely. **The channel drops precisely the
  host-measured evidence and preserves verbatim precisely the unchecked model assertion**, and it
  re-injects that assertion into the next prompt with nothing marking it as unverified. `CLM-11`
  describes this as "compressed structured trajectory context"; that is accurate for the evidential
  fields and false for the response, and the claim is made *to the model*, inside the prompt it reads.

Fractal measures the growth of the one context channel it fully owns (`RTE-22`) and displays the
number in a toolbar — never in headless mode — and **no route consumes it** to trim, compact, or warn.
A gauge with no actuator. `CLM-02` ("without context rot") is about `CMP-12` and is unsupported within
this run; the host-layer observation is a separate, narrower tension.

**State and action.** Session state is written twice per turn — a pending record before the call, a
completed record after — on every terminal path including failure and interrupt, into a
workspace-keyed JSON file under a global state root. Corruption, schema mismatch, and identity
mismatch are handled by refusal plus a timestamped backup, never by repair (`RTE-19.E1`,
`RTE-19.E1d`); this is the system's only implemented disposition, and it judges **artifact integrity
and identity, not content truth**. Action execution is entirely delegated: Fractal constructs
`DirectWorkspaceMount(host_path == sandbox_path)` for the workspace and every `--include` directory,
names the sandbox deterministically, and reuses it hot by default. It implements **no approval gate,
no command policy, and no allow/deny list**; `CLM-10`'s isolation and no-network guarantees are
implemented wholly outside the boundary and are **not assessable here**. Fractal's doctrine says the
same thing in its own words (`CLM-12`). Hot reuse also means a second accumulation substrate exists
(`OBJ-18`) — interpreter globals and container-local files persisting across turns and processes —
about which this run can say nothing.

**Memory return, where applicable.** Read-back is implemented and real, but narrower in practice than
the architecture suggests. Write agency is **automatic only**: no slash command and no model output
field can commit, edit, or delete retained material, so what is kept is a function of what happened,
never of what was judged worth keeping. There is no curation stage, no consolidation, no synthesis, no
semantic invalidation, no decay, and no promotion path anywhere in the host layer — the only eviction
is a positional count cap, and the only invalidation is whole-file structural refusal. And because
`FractalSession.load` returns a *fresh* session whenever no id is supplied (an explicit choice, to
avoid silently picking the wrong prior conversation), the default population of the read-back channel
is **empty**: in the headless single-turn mode that `CLM-03` and the bundled skill are built around,
**no memory read-back occurs at all** unless the caller threads `--resume` itself. Headless Fractal
writes a session file that, by default, nothing will ever read. Session files accumulate with no
deletion, expiry, or quota.

Workspace `AGENTS.md` and the shipped skill texts travel the same prompt route and carry real
directive force, but they are **static shipped material, not read-back** — Fractal never writes to
either from experience. Worth flagging for a delegating caller: an `AGENTS.md` inside a workspace the
caller points Fractal at becomes an instruction channel to Fractal's model (`BAP-02`).

**Truth-apt and warrant routes.** Two ampliative candidates are produced per turn — the `response`
(`OBJ-07`) and `changed_files` (`OBJ-08`) — both by the uninspected `CMP-12`. **Neither is tested and
neither is accepted.** The only implemented gate on their path is a Python `isinstance` check
(`RTE-23`), whose domain is type conformance and which establishes nothing about truth, relevance, or
completeness. Turn-outcome classification looks like a check and is not one: its evaluator is a single
equality test on `trace.status`, and a `None` trace falls through to `succeeded`. It licenses "the
loop did or did not report budget exhaustion" — nothing about the answer — while being operationally
consequential through exit codes a calling script branches on. Because there is no acceptance, there
is no lifecycle integration anywhere in the boundary; re-injecting the summary and handing stdout to
another agent are **pre-acceptance use**.

Against that, Fractal's `CLM-05` provenance policy is genuinely implemented for commands run, files
read, usage, and errors. Its host-side action observation is careful work — fd-to-path mapping,
compound-call collapsing, mode decoding from open flags — and produces the strongest warrant in the
system: "these hooked Python calls occurred inside the interpreter during this turn". Its bounds are
real too: it is blind to file effects of subprocesses, it depends on `CMP-12` injecting the hooks at
all, and adapter exceptions are swallowed, so under-recording is silent.

**Which makes the sharpest finding a wiring gap, not a capability gap.** `RuntimeEventTracker`
computes `files_modified` on every write-mode hook event, and **no code outside `events.py` reads it**
(`OBJ-09b`, `RTE-13.E2`). The persisted field of that same name is filled from the model's
`changed_files`, counted into the summary, printed to stderr, and returned in the `--json` envelope.
Two independent claims about the same fact exist in the same process at the same moment; they are
never compared; the model's is kept. `CLM-08` honestly declares the coercion — inspection adds that
the alternative is already computed. Two qualifications keep this from being overstated: the
hook-derived list would warrant "opened for writing", not "content differs", so wiring it would not by
itself produce a change check; and on failed and interrupted turns no `changed_files` is passed at
all, so the retained field is empty exactly where a later turn would most need it. `CLM-05`'s fifth
category, "verification status", is **vacuous**: no route in the boundary produces one, and the base
prompt's instruction to "verify important edits" is an unenforced directive with no place to record a
result.

**Governing controls.** The only enforcing paths in the system are the sandbox mount/network
configuration (`BAP-09`, external), config-layered model admission with `restricted_models` rejection
(`BAP-10`), and the process interface — stdout/stderr split, exit codes 0/1/2/130, the `--json`
envelope (`BAP-11`). **None of them carries accumulated material.** Everything that carries retained
or truth-apt content — the summary, the history, `AGENTS.md`, the skills, the user message — is text
handed to a model with advisory or directive force and no enforcement. Precedence among those channels
(the user message overriding `AGENTS.md`) is **asserted in prose inside the same docstring**, not
resolved by code.

**The consumer that matters most is another agent.** `CLM-03` and the bundled skill route audits,
request-tracing, root-cause analysis, and cross-file synthesis to `fractal -p`, promising a "distilled
answer". The delivery route is fully implemented and carefully built — stream separation, exit-code
semantics, a stdin grace period specifically so agent harnesses cannot hang the turn, update-check
suppression under `--json`. The **warrant** route is absent. For an audit or a root-cause task the
answer *is* the epistemic product, and it crosses into the calling agent's reasoning as an unchecked
ampliative claim, on a turn that by default has no memory, with nothing in Fractal or in the skill file
instructing the caller to verify it. That is the gap between the claim's epistemic register and the
implemented route — and it is a limit on `CLM-03`, not a contradiction of Fractal's own doctrine,
which says plainly that there is no approval, diff review, or rollback.

**Capability versus deployment, held open throughout.** Every finding above is `implemented` or
`absent` within `src/fractal/**` at `5954a07d`. Nothing was deployed, run, or observed. Implementation
is not deployment; presence in context is not activation; retention is not read-back; a curation label
is not a transformation; use is not acceptance.

## Record 10 — Limitations, each with the conclusion it prevents

| # | Limitation | Scope | Conclusion prevented |
|---|---|---|---|
| LIM-1 | **`predict-rlm` 0.7.0 (`SRC-8`) not obtained** — pinned by hash in `uv.lock`, not vendored, no virtualenv | `CMP-12`, `RTE-05`, `RTE-12` | Any conclusion about how `OBJ-07`/`OBJ-08` are produced; whether the loop performs its own checking; whether `OBJ-05` faithfully records production (`CLM-09`); whether recursion manages context as claimed (`CLM-02`); whether input fields behave as `CLM-13` asserts; whether hooks are injected at all — which bounds every warrant resting on `OBJ-09a` |
| LIM-2 | **sbx/Docker implementation not obtained** | `CMP-13`, `BAP-09` | Any conclusion about `CLM-10` (isolation, no network by default), about what persists inside a reused sandbox (`OBJ-18`), or about whether `RTE-12` execution is contained |
| LIM-3 | **No observed run** — no `sbx`, no provider credentials, no virtualenv, and the checkout must not be mutated | whole run | Every `observed` and `causally supported` status. Specifically: that the summary is ever read, that `session_history` is ever inspected, that read-back changes any output, that the 20-turn cap is ever reached, what a real `RunTrace` contains, and how fast `OBJ-02` grows in practice |
| LIM-4 | **No causal experiment** — no interventional comparison of any kind | whole run | Any attribution of an outcome to the RLM architecture, to a model choice (`CLM-04`), to the summary format, or to any individual component |
| LIM-5 | **Test bodies unread** (`SRC-7`, filenames only) | `tests/**` | Any conclusion that the persistence, trimming, schema-gating, or interrupt-retention behaviors are **verified** rather than merely written — including the interrupt-recovery property that `runtime.py:262` cites a named test to support |
| LIM-6 | **Symbol-level reads only** for `providers.py`, `onboarding.py`, `credentials.py`, `config_commands.py`, `connectivity.py`, `runtime_lms.py`, `version_check.py` | `SRC-1` partial | Any fine-grained conclusion about admission behavior beyond the `restricted_models` allowlist, about credential handling, or about `CMP-14`'s network behavior |
| LIM-7 | **Doctrine is stale in known ways** — `CONF-1`, `CONF-3`, `CONF-4`, `CONF-5`, `CONF-6`, `CONF-7` | `SRC-2`–`SRC-5` | Any use of a documentation statement as independent corroboration of implementation. Where the two disagree, both are reported; neither resolves the other |
| LIM-8 | **Backend-conditional observation** — hooks yield `[]` when `RuntimeHook` is unimportable, silently; `SRC-3` "Known Limits" makes the same caveat; no backend inventory obtained | `RTE-13`, `OBJ-09a` | That host-recorded `files_read`/`commands_run` are present in **any given deployment**; therefore that `OBJ-09a`'s host provenance is an unconditional property of the retained record |
| LIM-9 | **Single frozen revision, no history inspected** | whole run | Any conclusion about direction of travel — whether the absent consolidation, decay, promotion, and acceptance routes are deliberate scope or unbuilt work. In-code "for now" comments signal intent but are `claimed`, not evidence of a trajectory |
| LIM-10 | **Unresolved applicability: none.** Both lens dispositions are `applicable`; neither is `uncertain` | — | Recorded for completeness: no conclusion is prevented on applicability grounds in this run |
| LIM-11 | **Conflicting evidence preserved unresolved** — `CONF-1`…`CONF-8`, notably `CLM-05` vs `CLM-08` | as listed | Any single statement of "what Fractal does" about session storage location, summary contents, or files-changed provenance without naming which artifact is being cited |
| LIM-12 | **`OBJ-08` vs `OBJ-09b` was never compared** — the system does not do it, and no run could do it here | `RTE-13.E2` | Any quantification of how far model-reported `changed_files` diverges from host-observed write targets, i.e. how consequential the `CLM-05`/`CLM-08` gap is in operation |

## Record 11 — Verification and blocker report

### 11.1 Structural verification (step 10.1)

| Check | Result |
|---|---|
| Source anchors and statuses | ✓ Nine `SRC-*` with kind, identity, revision, evidence layer, inspected scope, anchors, access gaps. Every lens record cites the register; no lens replaced a boundary or an evidence layer |
| Unique, resolving IDs | ✓ No collisions. Both lenses used provisional placeholders and returned them for central registration (record 8.1); `OBJ-09` was split rather than renamed |
| One boundary and revision across all records | ✓ `5954a07d` and the packet §1 boundary appear in the header of every physical part |
| Mandatory runtime coverage | ✓ Six material loops with trigger, next-step owner, decision policy and form, context selection, state reads/writes, action executor and boundary, persistence, coordination, retry/cancellation/recovery, output; six conditional surfaces each with stated materiality |
| Both lens dispositions present as explicit records | ✓ Records 6a, 6b — neither implied by an absent section |
| All applicable lens outputs present | ✓ Both lenses were `applicable` and both ran; no early exit was needed |
| Prevented conclusions stated for every non-run | ✓ Record 10; plus per-finding scoping inside both lens files |
| Shared-route ownership respected | ✓ Records 8.3, 8.4; one overlap noted and resolved in favour of the owning lens |
| No forbidden evidence upgrades | ✓ Record 11.2 |

### 11.2 Distinction checks (step 10.2)

| Distinction | Where it was load-bearing in this run |
|---|---|
| Retention is not read-back | `OBJ-11`/`OBJ-12` are delivered into context every turn by the same route as the summary, yet are static shipped material — argued explicitly rather than assumed (`lens-memory.md` §3.1) |
| Context presence is not activation | Four separate findings per delivered item; activation is `uninspected` for **every** item, including the always-visible summary (`lens-memory.md` §4) |
| Implementation is not deployment | Every host finding is `implemented`, never "in use". `RTE-22` is implemented and never runs headless |
| Observation is not causality | No `observed` status exists at all, so the upgrade was unavailable by construction |
| Curation is not warrant | "compressed" (`CLM-11`) is a lossy field projection; "trustworthy" (`CLM-06`) is provenance about token accounting only; neither establishes semantic preservation |
| Use is not acceptance | The summary is re-injected every turn and stdout is consumed by another agent — both recorded as **pre-acceptance use**, and lifecycle integration is therefore `no route found within boundary` |
| Behavioral authority is not epistemic or operational authority | The three enforcing paths carry no accumulated material; every path that carries retained content is advisory or directive and unenforced |

### 11.3 Deterministic validation

**No deterministic validation is applicable to this result, and none was manufactured.** The result is
retained under a staging identity with no collection contract, no type, and no frontmatter. A probe of
the shipped validator against the result path returned `No matching note found`, confirming that no
existing parser or schema covers it. Per step 10.3 no schema or parser was changed to create a
validation path. Verification therefore rests on 11.1 and 11.2.

### 11.4 Blockers

| Blocker | Kind | Detail |
|---|---|---|
| **BLK-1 — no authorized target contract** | publication blocker | This run was given no authorized publication target, and no existing collection contract was identified that can represent an eleven-record agentic-system analysis result. Per step 9 the logical result is **retained under the staging identity** `kb/work/multistage-write-analyse-agentic-system-20260820/trials/fractal/`. No collection contract was improvised and the agent-memory review schema was **not** reused. |

**No other blockers.** No logical record is missing (all eleven are present or pointed to from the map
at the top). No ID collisions. No unsupported material claim: every claim carries a `SRC-*` anchor and
a conclusion status, and every absence names its search boundary. No applicable validation failed —
none was applicable.

**Publishable limitations** (record 10), classified: doc-only evidence — LIM-1, LIM-2, LIM-7;
inaccessible components — LIM-1, LIM-2, LIM-5, LIM-6; no observed run — LIM-3, LIM-8; no causal
experiment — LIM-4; unresolved applicability — none (LIM-10); conflicting evidence — LIM-11, LIM-12.

### 11.5 Report

- **Result identity:** `AAS-2026-08-20-fractal-01`
- **Location:** `kb/work/multistage-write-analyse-agentic-system-20260820/trials/fractal/` (staging;
  five physical parts, one identity)
- **Boundary:** Fractal's host layer at `5954a07d`; **subsystem-only** with respect to deployed
  agentic behavior — `predict-rlm` and sbx excluded and uninspected
- **Revision:** `5954a07d464feeaf6c311a9fa5ca2e54200a6794`
- **Tier:** `code-grounded` for the declared boundary; `RTE-05` `uninspected`; no observed run
- **Lens dispositions:** memory/context `applicable` (ran); epistemic `applicable` (ran, via the
  invoked instruction)
- **Limitations:** LIM-1 … LIM-12
- **Blockers:** BLK-1 (publication — no authorized target contract)
