# Evidence packet — run `AAS-20260820-CCDW-01`

Prepared once by the orchestrator under step 2.4 of `analyse-agentic-system`.
Lens workers consume this packet and may make targeted reads **inside** the frozen
boundary only (i.e. re-reading `SRC-1` itself). No lens may reacquire, refresh, or widen
sources, rename a record, or mint a parallel ID namespace.

---

## 1. Run and staging identity

| Field | Value |
|---|---|
| Run / result ID | `AAS-20260820-CCDW-01` |
| System identifier | Claude Code **dynamic workflows** — the Workflow orchestration facility inside the Claude Code harness (model-authored JavaScript orchestrator over sub-agents) |
| Orchestrating instruction | `analyse-agentic-system` (candidate under trial) |
| Staging identity | `kb/work/multistage-write-analyse-agentic-system-20260820/trials/cc-dynamic-workflows/` |
| Publication target | **none authorized for this run** — publication blocker recorded (see result §11) |
| Analysis cutoff | 2026-06-03 (capture date of `SRC-1`) |
| Run date | 2026-08-20 |

## 2. Scope confirmation (step 1.2)

In scope. Dynamic workflows are an **orchestration framework**: a runtime that executes a
script which schedules and dispatches up to 1,000 model-backed sub-agents, holds
intermediate results, and returns one synthesized output. Deployed behavior depends on
model calls (script authoring, every sub-agent) plus surrounding machinery (runtime,
permission gate, command registry, progress/control UI).

## 3. Boundary declaration (step 1.3–1.4)

**This is a subsystem-only boundary and is named as such.** Dynamic workflows are one
facility inside the Claude Code harness. **No whole-system conclusion about Claude Code
may be drawn from this run.**

Included — components whose scheduling, context selection, retained state, action
execution, checking, acceptance, or authority decisions produce or constrain workflow
behavior:

- the workflow **runtime** (isolated background executor) — `CMP-1`
- the model-authored **orchestrator script** — `CMP-2`
- the **script-authoring path** inside the main Claude session (`ultracode` keyword,
  `/effort ultracode`, natural-language request) — `CMP-3`
- the **sub-agent worker pool** the script dispatches — `CMP-4`
- the **launch approval gate** and its permission-mode table — `CMP-5`
- the **`/workflows` progress-and-control surface** (TUI, task panel, Desktop pane) — `CMP-6`
- the **workflow command registry** (bundled + project + personal) — `CMP-7`
- the **per-run script archive** under `~/.claude/projects/` — `CMP-8`
- the **resume / agent-result store** — `CMP-9`
- the **feature disable surface** (`/config`, `disableWorkflows`, env var, managed settings) — `CMP-10`
- the bundled **`/deep-research`** workflow as an instance — `CMP-11`
- the **main Claude conversation session** in its two workflow-facing roles only: script
  author and final-report recipient — `CMP-12`

Excluded (named, so the conclusions they prevent are visible):

- Claude Code's ordinary turn-by-turn agent loop, skills, and agent teams, except where the
  docs' comparison table is cited as doctrine about workflows.
- The sub-agent primitive's own internals (`/en/sub-agents` was not in the source bundle).
- The `/deep-research` script's actual source text — never inspected; only its documented
  behavior.
- Model inference, provider routing (Bedrock / Vertex / Foundry), billing and rate-limit
  accounting internals.
- Claude Code's general permission engine beyond the workflow-specific rows quoted.

External dependencies: the model provider (Anthropic API / Bedrock / Vertex / Foundry);
the `WebSearch` tool (required by `/deep-research`); the host filesystem and shell reached
**only** through sub-agents; the user's tool allowlist; MCP servers when agents call them.

## 4. Source register (step 2.3)

| ID | Kind | Identity / location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps |
|---|---|---|---|---|---|---|---|
| `SRC-1` | Supplied document snapshot | `kb/sources/claude-code-dynamic-workflows-docs.md`, from `https://code.claude.com/docs/en/workflows` | captured **2026-06-03**, `capture: web-fetch`, genre `tool-announcement`; frontmatter states the feature is in research preview and requires Claude Code **v2.1.154+** | **doctrine/design** (vendor documentation); its permission/limit tables are also *doctrine about implemented behavior*, not inspected implementation | Whole file, all sections | Section headings used as anchors: `#when-to-use`, `#bundled`, `#watch-the-run`, `#have-claude-write`, `#ask-in-prompt`, `#ultracode`, `#approve`, `#save`, `#args`, `#how-it-runs`, `#limits`, `#resume`, `#cost`, `#turn-off` | Linked pages (`/en/sub-agents`, `/en/skills`, `/en/agent-teams`, `/en/agents`, `/en/costs`) **not** in the bundle and not fetched. No source code, no script text, no run trace, no changelog. Doc's own "Date: Unknown". |
| `SRC-2` | Live-session capture (negative) | `./capture-live-session-tool-roster.md` | captured **2026-08-20T20:09:31+02:00**; host `claude --version` = `2.1.237` | **observed run**, scope: roster-only / negative | This sub-agent process's full tool roster + a `ToolSearch` probe | Whole capture file | Sub-agent tier ≠ main-session tier; establishes only that *this* process exposes no workflow tool. Supports **no positive finding** about the target. |

**Cutoff conflict, preserved as a conflict (not resolved):** `SRC-1` is pinned at
2026-06-03 and documents behavior at/near v2.1.154–v2.1.160; the host observed under
`SRC-2` runs v2.1.237. The run's analysis cutoff is **2026-06-03**. Any behavior change
between those versions is outside the boundary and is recorded as a limitation.

## 5. Evidence tier (step 3)

**`doc-grounded`.** The material loops recorded in the runtime baseline rest on vendor
documentation, not on inspected implementation material. No implementation, no observed
run of the target, no causal experiment. Per step 3, this tier is fixed for the whole run
and no lens may upgrade it.

---

## 6. Shared canonical records

### 6.1 Components (`CMP-*`) — orchestrator-owned

| ID | Component | Form / substrate | Anchor |
|---|---|---|---|
| `CMP-1` | Workflow runtime | Executor process, isolated environment separate from the conversation; runs in background | `#how-it-runs` |
| `CMP-2` | Orchestrator script | JavaScript source text, model-authored; holds loop, branching, intermediate results | `#when-to-use`, `#how-it-runs` |
| `CMP-3` | Script-authoring path in main session | Model call in the conversation, triggered by keyword/effort/natural language | `#have-claude-write`, `#ask-in-prompt`, `#ultracode` |
| `CMP-4` | Sub-agent worker pool | Model-backed workers; ≤16 concurrent (fewer on low-CPU hosts), ≤1000 per run; `acceptEdits` mode; inherit user tool allowlist; use session model unless the script routes a stage elsewhere | `#limits`, `#approve`, `#cost` |
| `CMP-5` | Launch approval gate | Interactive prompt (CLI) / approval card (Desktop); behavior varies by permission mode; can record persistent consent | `#approve` |
| `CMP-6` | Progress-and-control surface | `/workflows` TUI list + phase/agent drill-down; task-panel progress line; Desktop Background-tasks pane | `#watch-the-run`, `#manage-runs` |
| `CMP-7` | Workflow command registry | Files in `.claude/workflows/` (project, shared via repo) and `~/.claude/workflows/` (personal); bundled commands; project wins on name collision; appear in `/` autocomplete | `#save`, `#bundled` |
| `CMP-8` | Per-run script archive | File written per run under the session's directory in `~/.claude/projects/` | `#how-it-runs` |
| `CMP-9` | Resume / agent-result store | Runtime-tracked per-agent results; session-scoped | `#how-it-runs`, `#resume` |
| `CMP-10` | Feature disable surface | `/config` toggle, `"disableWorkflows"` in `~/.claude/settings.json`, `CLAUDE_CODE_DISABLE_WORKFLOWS=1`, managed settings, admin page | `#turn-off` |
| `CMP-11` | `/deep-research` bundled workflow | A specific `CMP-2` instance shipped with Claude Code; requires `WebSearch` | `#bundled`, `#run-a-bundled-workflow` |
| `CMP-12` | Main conversation session (workflow-facing roles only) | Model context window; author of `CMP-2`, recipient of the final report and the run-script path | `#how-it-runs`, `#when-to-use` |

### 6.2 Operative objects (`OBJ-*`) — orchestrator-owned generic identity

| ID | Object | Representational form | Substrate | Anchor |
|---|---|---|---|---|
| `OBJ-1` | Workflow script text | symbolic (JavaScript) | file (`CMP-8`) + runtime memory | `#how-it-runs` |
| `OBJ-2` | `args` global | structured data (array/object), passed at invocation | script global | `#args` |
| `OBJ-3` | Script variables / intermediate results | in-language values; may hold natural-language agent output | runtime process memory | `#when-to-use`, `#how-it-runs` |
| `OBJ-4` | Agent result (per sub-agent, with its prompt and recent tool calls) | natural-language + tool-call trace | runtime store (`CMP-9`), surfaced in `CMP-6` | `#watch-the-run`, `#how-it-runs` |
| `OBJ-5` | Phase record (agent count, token total, elapsed time) | numeric/structured telemetry | `CMP-6` | `#watch-the-run` |
| `OBJ-6` | Final report / answer | natural language, cited in the `/deep-research` case | delivered into `CMP-12` context | `#run-a-bundled-workflow`, `#when-to-use` |
| `OBJ-7` | Saved workflow command file | symbolic (JavaScript) + command name | `CMP-7` | `#save` |
| `OBJ-8` | Permission consent record | configuration entry | user settings / project-scoped consent | `#approve` |
| `OBJ-9` | Deep-research **claim** | natural-language proposition with source citation | `OBJ-3` then `OBJ-6` | `#bundled` |
| `OBJ-10` | Fetched web source | external document | fetched by agents | `#run-a-bundled-workflow`, `#bundled` |
| `OBJ-11` | Cross-check / vote result on a claim | disposition value | script variables | `#bundled` |
| `OBJ-12` | Tool allowlist | configuration | user settings; inherited by `CMP-4` | `#approve` |
| `OBJ-13` | Session effort setting (`ultracode`) | configuration | session-scoped, resets on new session | `#ultracode` |
| `OBJ-14` | Session model selection | configuration | session | `#cost` |

### 6.3 Routes (`RTE-*`) — runtime-owned endpoints and progression

Lenses **annotate** these; they do not re-inventory or rename them.

**Control routes**

| ID | Route | Trigger / decision policy | Anchor |
|---|---|---|---|
| `RTE-C1` | Trigger → script authoring | `ultracode` keyword in prompt, natural-language request ("use a workflow"), or `/effort ultracode` (Claude then decides per substantive task). Pre-v2.1.160 the literal keyword was `workflow`. Decision form: **model judgement**, keyword-gated. | `#ask-in-prompt`, `#ultracode` |
| `RTE-C2` | Launch approval | Per-run prompt showing planned phases; options Yes / Yes-and-don't-ask-again / View raw script / No; `Ctrl+G` opens the script, `Tab` edits the prompt. Prompt presence is a **table-driven** function of permission mode. Decision form: **human**, with configurable bypass. | `#approve` |
| `RTE-C3` | Script execution | Runtime executes `OBJ-1` in an isolated environment, in the background; session stays responsive. Decision form: **code** — the script holds loop and branching. | `#how-it-runs`, `#when-to-use` |
| `RTE-C4` | Agent dispatch | Script spawns sub-agents; runtime enforces ≤16 concurrent and ≤1000 total. Next-step owner: **the script**. | `#when-to-use`, `#limits` |
| `RTE-C5` | Interactive run control | In `/workflows`: `p` pause/resume, `x` stop agent or whole run, `r` restart a running agent, `s` save script. Decision form: **human, mid-run**. | `#watch-the-run` |
| `RTE-C6` | Resume | Completed agents return **cached** results from `CMP-9`; the rest run live. Works **only within the same session**; exiting Claude Code makes the next session start the workflow fresh. | `#resume` |
| `RTE-C7` | Command invocation | `/<name>` resolves in `CMP-7`; project beats personal on collision; optional `args`. | `#save`, `#args`, `#bundled` |
| `RTE-C8` | Feature disable | `/config`, settings key, env var (read at startup), managed settings/admin page. When disabled: bundled commands unavailable, `ultracode` keyword no longer triggers, `ultracode` removed from `/effort`. | `#turn-off` |
| `RTE-C9` | Mid-run tool permission prompt | Shell commands, web fetches, and MCP tools **outside** the allowlist can still prompt mid-run. Only agent permission prompts can pause a run; there is otherwise **no mid-run user input**. In `claude -p`/SDK there is nobody to prompt, so configured rules apply without confirmation. | `#approve`, `#limits` |

**Context routes**

| ID | Route | Selection / delivery | Anchor |
|---|---|---|---|
| `RTE-X1` | Script → sub-agent prompt | The script composes each agent's prompt from `OBJ-3`/`OBJ-2`. Selection signal is **script-authored code**, not model judgement at dispatch time. | `#when-to-use`, `#watch-the-run` (agent prompt is inspectable) |
| `RTE-X2` | Sub-agent result → script variables | `OBJ-4` returns into `OBJ-3`, **not** into `CMP-12`'s context window. | `#when-to-use`, `#how-it-runs` |
| `RTE-X3` | Final answer → main session | Only the final answer lands in `CMP-12`'s context. | `#when-to-use` |
| `RTE-X4` | Run-script path → main session | Claude **receives the path** to the archived script at run start and can be asked for it. | `#how-it-runs` |
| `RTE-X5` | `args` → script global | Claude passes user-named input as **structured data**; script calls array/object methods directly; `undefined` if omitted. | `#args` |
| `RTE-X6` | Run internals → human | `/workflows` drill-down exposes each phase's agent count, token total, elapsed time, and each agent's prompt, recent tool calls, and result. | `#watch-the-run` |

**State / action routes**

| ID | Route | Reads / writes | Anchor |
|---|---|---|---|
| `RTE-S1` | Run-script archive write | **Every run** writes `OBJ-1` to a file under the session dir in `~/.claude/projects/`. User may open, diff against a previous run's script, or edit it and ask Claude to relaunch from the edited version. | `#how-it-runs` |
| `RTE-S2` | Save run script as command | `s` in `/workflows` → save dialog → `.claude/workflows/` (project, shared via repo) or `~/.claude/workflows/` (personal). Becomes `/<name>` in **future sessions**. | `#save` |
| `RTE-S3` | Consent record write | "Yes, and don't ask again for `<name>` in `<path>`" persists for that workflow in that project; in **Auto** mode any Yes records consent in **user settings** and later launches start without prompting. | `#approve` |
| `RTE-S4` | Agent-mediated external action | **The script has no direct filesystem or shell access.** Agents read, write, and run commands; the script coordinates. Agents run in `acceptEdits`: file edits auto-approved regardless of session mode. | `#limits`, `#approve` |
| `RTE-S5` | Agent-result tracking | Runtime tracks each agent's result as the run progresses — the stated mechanism behind resumability. | `#how-it-runs` |
| `RTE-S6` | Usage accounting | Runs count toward plan usage and rate limits; per-agent token usage visible live; stopping keeps completed work. | `#cost` |

**Deep-research routes (`CMP-11`)** — documented behavior of one bundled script

| ID | Route | Description | Anchor |
|---|---|---|---|
| `RTE-E1` | Search fan-out | Fans out web searches on the question across several angles. | `#bundled`, `#run-a-bundled-workflow` |
| `RTE-E2` | Source fetch | Fetches the sources it finds. | same |
| `RTE-E3` | Cross-check | Cross-checks the sources it finds **against each other**. | same |
| `RTE-E4` | Vote | Votes on each claim. | `#bundled` |
| `RTE-E5` | Filter | Claims that didn't survive cross-checking are filtered out of the report. | `#bundled`, `#run-a-bundled-workflow` |
| `RTE-E6` | Cited synthesis | Synthesizes a cited report; it cites the sources each claim came from. | same |
| `RTE-E7` | Adversarial peer review (generic pattern) | A workflow "can have independent agents adversarially review each other's findings before they're reported". Stated as a **capability of the pattern**, not as shipped behavior of a named workflow. | `#when-to-use` |
| `RTE-E8` | Multi-angle drafting and weighing (generic pattern) | "draft a plan from several angles and weigh them against each other". Same capability status as `RTE-E7`. | `#when-to-use` |

### 6.4 Behavioral-authority paths (`BAP-*`) — orchestrator-owned

Fields: consumer | channel | force | horizon (run-level extension).

| ID | Consumer | Channel | Force | Horizon | Anchor |
|---|---|---|---|---|---|
| `BAP-1` | Workflow runtime (`CMP-1`) | Execution of `OBJ-1` in the isolated environment | **enforcing** — the script *is* the control flow ("Who decides what runs next: the script") | one run | `#when-to-use`, `#how-it-runs` |
| `BAP-2` | Future sessions' command resolver + Claude/user | `CMP-7` registry lookup on `/<name>` | **enforcing on invocation** — running that saved orchestration; project entry overrides personal | persistent across sessions; project-scoped (repo-shared) or user-scoped | `#save` |
| `BAP-3` | Sub-agent (`CMP-4`) | Spawn prompt via `RTE-X1` | **directive** for that worker's task | that agent's lifetime | `#when-to-use` |
| `BAP-4` | Main session Claude + user (`CMP-12`) | `RTE-X3` context delivery | **advisory** — content informing the conversation | session / turn | `#when-to-use`, `#run-a-bundled-workflow` |
| `BAP-5` | Launch approval gate (`CMP-5`) | `OBJ-8` consent record in project/user settings | **permissive** — suppresses the launch prompt | persistent, per workflow+project (default/acceptEdits) or per user (Auto) | `#approve` |
| `BAP-6` | Sub-agent tool executor | Inherited `OBJ-12` allowlist + forced `acceptEdits` | **permissive/enforcing** — auto-approves file edits, still prompts for non-allowlisted shell/web/MCP | run | `#approve`, `#limits` |
| `BAP-7` | Whole feature | `CMP-10` settings / env var / managed settings | **enforcing prohibition** | persistent; organization-wide via managed settings | `#turn-off` |
| `BAP-8` | Main session Claude's planning (`CMP-3`) | `OBJ-13` `/effort ultracode` session setting | **directive default** — Claude plans a workflow for *every* substantive task | current session; resets on new session | `#ultracode` |
| `BAP-9` | Claude / user, on request | Archived `OBJ-1` file (`CMP-8`) read via the path from `RTE-X4` | **material for relaunch** — read, diffed, edited, then relaunched; advisory until relaunched, at which point it becomes `BAP-1` | persists on disk under the session directory | `#how-it-runs` |
| `BAP-10` | Runtime scheduler | Concurrency (≤16) and total (≤1000) agent caps | **enforcing** ceiling | every run | `#limits` |

### 6.5 Claims (`CLM-*`) — orchestrator namespace; the epistemic lens owns truth/scope/warrant fields

| ID | Claim (as stated) | Kind | Anchor |
|---|---|---|---|
| `CLM-1` | Independent agents adversarially reviewing each other's findings, or drafting a plan from several angles and weighing them, gives "a more trustworthy result than a single pass". | **warrant claim** | `#when-to-use` |
| `CLM-2` | `/deep-research` "votes on each claim, and returns a cited report with claims that didn't survive cross-checking filtered out". | knowledge-production / operation claim | `#bundled` |
| `CLM-3` | "A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer." | operation claim (context economy) | `#when-to-use` |
| `CLM-4` | "The runtime tracks each agent's result as the run progresses, which is what makes a run resumable within the same session." | mechanism claim | `#how-it-runs` |
| `CLM-5` | The 1,000-agent cap "prevents runaway loops"; the caps "bound the cost of a runaway script". | control claim | `#limits`, `#cost` |
| `CLM-6` | "No direct filesystem or shell access from the workflow itself" — agents act, the script coordinates. | isolation claim | `#limits` |
| `CLM-7` | What is repeatable in a workflow is "the orchestration itself"; the plan moves into code. | design claim | `#when-to-use` |
| `CLM-8` | "Your permission mode controls only the launch prompt" — spawned sub-agents always run in `acceptEdits` and inherit the allowlist regardless of session mode. | authority claim | `#approve` |

---

## 7. Runtime baseline (step 4)

Scheduling, context assembly, and external state/action are treated as **causal
responsibilities**, not module boundaries. In this system one facility spans several: the
script (`CMP-2`) is simultaneously the scheduler and the context assembler, while it is
deliberately *not* an actor on the outside world.

### Loop A — Workflow authoring loop (in the conversation)

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | User prompt containing `ultracode`, a natural-language request ("use a workflow"), or any substantive task while `/effort ultracode` is set. Highlight is dismissible (`Option/Alt+W`, backspace after the keyword) and the trigger is disableable in `/config`. | `claimed` | `SRC-1#ask-in-prompt`, `#ultracode` |
| Next-step owner | Main-session Claude (`CMP-3`) | `claimed` | `SRC-1#have-claude-write` |
| Decision policy and form | **Model judgement**, keyword- or setting-gated. Under `ultracode` the model decides *per task* whether a workflow is warranted, and a single request can become several workflows in a row (understand → change → verify). | `claimed` | `SRC-1#ultracode` |
| Context selection / framing | Not documented. What the authoring model reads to write the script is uninspected. An existing orchestrator (a folder of sub-agent prompts, or a fan-out skill) can be pointed at as input. | `uninspected` for the general case; `claimed` for the point-at-an-orchestrator path | `SRC-1#ask-in-prompt` |
| State reads / writes | Writes `OBJ-1`; reads `OBJ-13`. | `claimed` | `SRC-1#ultracode`, `#how-it-runs` |
| Action executor / boundary | None — authoring produces text only. | `claimed` | `SRC-1#how-it-runs` |
| Persistence | `RTE-S1` archives every run's script (`CMP-8`). | `claimed` | `SRC-1#how-it-runs` |
| Coordination / return | Hands `OBJ-1` to `RTE-C2` then `CMP-1`; receives the archive path back (`RTE-X4`). | `claimed` | `SRC-1#how-it-runs` |
| Retry / cancellation / recovery | User dismisses the keyword highlight, edits the prompt with `Tab`, or answers **No** at the gate. | `claimed` | `SRC-1#ask-in-prompt`, `#approve` |
| Output | `OBJ-1`, a JavaScript orchestrator script, plus the phase list shown at the gate. | `claimed` | `SRC-1#approve` |

### Loop B — Launch-approval loop

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | A composed `OBJ-1` about to run. | `claimed` | `SRC-1#approve` |
| Next-step owner | The human, except where the permission mode removes them. | `claimed` | `SRC-1#approve` |
| Decision policy and form | **Table-driven configuration** selecting between human decision and automatic start: Default/accept-edits → every run unless "don't ask again"; Auto → first launch only, any Yes records consent in user settings, and the prompt is skipped entirely when ultracode is on; Bypass permissions / `claude -p` / Agent SDK → **never** prompt, run starts immediately. | `claimed` | `SRC-1#approve` |
| Context selection / framing | The gate shows the **planned phases**; the raw script is available on demand (View raw script, `Ctrl+G`). Desktop shows name, phase list, and a token-usage caution. So the human's default decision surface is a **summary**, with full text opt-in. | `claimed` | `SRC-1#approve` |
| State reads / writes | Reads permission mode and prior consent; writes `OBJ-8` (`RTE-S3`). | `claimed` | `SRC-1#approve` |
| Action executor / boundary | Starts or cancels the run. | `claimed` | `SRC-1#approve` |
| Coordination / return | On Yes, control passes to `CMP-1`. | `claimed` | `SRC-1#approve` |
| Retry / cancellation | **No**, or `Tab` to adjust the prompt before the run starts. | `claimed` | `SRC-1#approve` |
| Materiality | This is the run's only pre-execution human control point, and the point where a persistent authority record is created. | — | — |

### Loop C — Script execution loop (the core scheduler)

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | Approved launch, or `/<name>` invocation with optional `args`. | `claimed` | `SRC-1#approve`, `#args` |
| Next-step owner | **The script** (`OBJ-1`), executed by `CMP-1`. Explicitly contrasted with subagents/skills/agent-teams where "Claude, turn by turn" or "the lead agent, turn by turn" decides. | `claimed` | `SRC-1#when-to-use` |
| Decision policy and form | **Symbolic** — loop and branching are JavaScript. This is the system's defining property: the plan is in code, and "the orchestration itself" is what is repeatable. | `claimed` | `SRC-1#when-to-use` |
| Context selection / framing | The script composes each agent's prompt from `OBJ-3`/`OBJ-2` (`RTE-X1`). Selection is code-determined, not model-determined at dispatch. | `claimed` (mechanism documented; no example script inspected) | `SRC-1#when-to-use`, `#watch-the-run` |
| State reads / writes | Intermediate results live in **script variables** (`OBJ-3`) inside the isolated environment, not in a context window and not on the filesystem. Runtime separately tracks per-agent results (`RTE-S5`). | `claimed` | `SRC-1#how-it-runs` |
| Action executor / boundary | **The script itself has no direct filesystem or shell access.** All external action is delegated to sub-agents (`RTE-S4`). This is a hard architectural line: the orchestrator is a pure coordinator. | `claimed` | `SRC-1#limits` |
| Persistence | `OBJ-3` is process-local and not documented as persisted; `OBJ-1` is archived (`RTE-S1`); `OBJ-4` is tracked in `CMP-9`. | `claimed` for archive and tracking; **`uninspected`** for whether `OBJ-3` survives the process | `SRC-1#how-it-runs` |
| Coordination / return | Fan-out to ≤16 concurrent agents, ≤1000 total; results return into script variables; one final answer returns to the session. | `claimed` | `SRC-1#limits`, `#when-to-use` |
| Retry / cancellation / recovery | Pause/resume (`p`), stop agent or run (`x`), restart a running agent (`r`); resume replays cached results for completed agents. Recovery is **session-bounded**: exiting Claude Code loses it and the next session starts fresh. | `claimed` | `SRC-1#watch-the-run`, `#resume` |
| Output | `OBJ-6`, one report or answer, delivered to `CMP-12`. | `claimed` | `SRC-1#run-a-bundled-workflow`, `#when-to-use` |

### Loop D — Sub-agent execution loop

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | Dispatch from the script with a composed prompt. | `claimed` | `SRC-1#when-to-use` |
| Next-step owner | The sub-agent itself, turn by turn, within its task. | `claimed` (by reference to the sub-agent primitive; that primitive's docs were **not** in the bundle) | `SRC-1#related` |
| Decision policy and form | Model judgement inside the agent. | `uninspected` in detail | — |
| Context selection | The agent receives its prompt; what else it loads is undocumented here. | `uninspected` | — |
| State reads / writes | Reads and writes the real filesystem; runs commands. | `claimed` | `SRC-1#limits` |
| Action executor / boundary | Runs in `acceptEdits` **regardless of session mode**; file edits auto-approved; inherits the user's tool allowlist; non-allowlisted shell/web/MCP calls can still prompt mid-run. | `claimed` | `SRC-1#approve` |
| Persistence | Its result is tracked by the runtime (`OBJ-4`) and is inspectable in `/workflows` (prompt, recent tool calls, result). | `claimed` | `SRC-1#watch-the-run`, `#how-it-runs` |
| Coordination / return | Returns into `OBJ-3` via `RTE-X2`. | `claimed` | `SRC-1#when-to-use` |
| Retry / cancellation | `x` stops it; `r` restarts it. | `claimed` | `SRC-1#watch-the-run` |
| Model | Session model unless the script routes a stage to a different one. | `claimed` | `SRC-1#cost` |

### Loop E — Observation and mid-run control loop (human)

| Field | Finding | Status | Evidence |
|---|---|---|---|
| Trigger / input | A running or completed workflow. | `claimed` | `SRC-1#watch-the-run` |
| Next-step owner | The human, asynchronously; the run does **not** wait for them. | `claimed` | `SRC-1#limits` ("No mid-run user input") |
| Decision policy | Human, from telemetry: phase agent counts, token totals, elapsed time; drill-down to an agent's prompt, recent tool calls, and result. | `claimed` | `SRC-1#watch-the-run` |
| Actions available | pause/resume, stop agent, stop run, restart agent, save script. | `claimed` | `SRC-1#watch-the-run` |
| Boundary | The **only** thing that can pause a run besides `p` is an agent permission prompt. Staged human sign-off requires splitting into separate workflows. | `claimed` | `SRC-1#limits` |
| Output | Control actions; optionally `OBJ-7` via `RTE-S2`. | `claimed` | `SRC-1#save` |

### Anti-conflation checks held (step 4.3)

- **A filesystem is not a scheduler.** `CMP-8` and `CMP-7` store scripts; neither dispatches. The scheduler is `OBJ-1` running inside `CMP-1`.
- **Retaining material is not selecting it into context.** `CMP-9` retains every agent result; only what the script reads into a prompt (`RTE-X1`) or the final answer (`RTE-X3`) enters any model's context. Most `OBJ-4` content documentedly never reaches `CMP-12`.
- **A tool schema present in context is not tool execution.** The inherited allowlist (`OBJ-12`) defines what agents *may* call; execution happens in Loop D and can still be blocked mid-run.
- **Capability is not deployment.** `RTE-E7`/`RTE-E8` describe what a workflow *can* be written to do; no shipped workflow is documented as doing them.

### Conditional surfaces inspected under step 4.4 (materiality stated)

- **Permissions / governance** — material: it changes the control path. The launch gate is the only pre-execution check, it is removable by mode or by a persistent consent record, sub-agents are forced into `acceptEdits` independent of the session's mode, and org-level `disableWorkflows` is the only hard off switch. This directly bounds what any authority conclusion can say.
- **Observability** — material: it is the evidence surface for the human and the sole mid-run control channel; agent prompts, tool calls, and results are inspectable, and the archived script makes the orchestration itself readable and diffable.
- **Packaging / distribution** — material: `RTE-S2` turns a one-off run into a repo-shared command, which is the mechanism behind the run's strongest memory read-back finding and behind `BAP-2`.
- **Cost / resource limits** — material: caps are an enforcing control (`BAP-10`) and the doc ties them to a safety claim (`CLM-5`).
- **Providers, UI surfaces, performance** — inspected only enough to record availability (paid plans, API, Bedrock, Vertex, Foundry; CLI, Desktop, IDE, `claude -p`, Agent SDK) and the headless behavioral difference (no prompts). Not otherwise material.

This inventory is deliberately **open**: it is not a taxonomy, template, maturity ladder,
ranking, or adoption advice.

---

## 8. Instructions to lens workers

1. Cite only `SRC-1` (and `SRC-2` for its negative scope). Do not fetch, search, or open
   any other file — in particular nothing else under `kb/`.
2. Extend records **by existing ID**. Do not rename, re-inventory, or create a parallel
   namespace. Genuinely new material records are returned to the orchestrator as
   "PROPOSED NEW RECORD: ..." for canonical registration.
3. The overall evidence tier is `doc-grounded` and fixed. Use only the conclusion statuses
   `absent`, `inapplicable`, `uninspected`, `claimed`, `implemented`, `observed`,
   `causally supported`. Nothing here reaches `implemented` or above.
4. Every negative or uncertain result names the inspected boundary and the exact conclusion
   it prevents.
5. Never upgrade: context presence → activation; implementation → observed operation;
   observation → causality; operational continuation → warrant.
