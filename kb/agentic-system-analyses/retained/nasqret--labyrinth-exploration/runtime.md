---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Labyrinth Exploration's host-directed research loop, result admission and project-local engine at 019a93da59313e697dc6f28bcfe1588a376c7565."
run-id: AAS-2026-11-23-labyrinth-exploration-4000731242d4-01
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
---

# Labyrinth Exploration runtime report

## Runtime account

Labyrinth Exploration supplies a research protocol and a separate file-processing engine. The protocol tells a coordinator what to attempt, what counts as progress and what may be admitted as established. The engine summarizes the project's records and checks selected consistency conditions. It does not choose the next experiment, perform research, or decide whether a proof or certificate deserves admission (SRC-1 `SKILL.md`, `references/loop.md`, `templates/lab.py`).

### Ordinary invocation

1. **Enter and resume.** The user asks the installed skill to continue a research programme. Codex supports explicit `$labyrinth-exploration`, skill selection and implicit matching; Claude Code documents `/labyrinth-exploration` and matching. Host selection and delivery are external. The coordinator resolves references and templates from the installed skill but works on the research project. For first setup it copies the engine and dashboard template and seeds state; on resumption it uses existing state rather than copying over it. The copied engine resolves project paths from its own file location, not the current directory. The coordinator runs status, opens the dashboard, checks previous agents/jobs and chooses at most three questions, preferring a cheap experiment or a proof step that would change the map ([RT-RTE-research-iteration](#rt-rte-research-iteration); SRC-1 `agents/openai.yaml`, `docs/tutorial.md`, `SKILL.md`, `references/codex.md`, `references/loop.md`, `templates/lab.py`).
2. **Produce and check a result.** The coordinator owns the next research step under natural-language guidance. It can work directly through the host shell, use available literature tools, or delegate. It specifies a conjecture with a test before running it, records a proposed event, and saves code, outputs and counterexamples. It logs the outcome even before admission. For a count to be used as established, the protocol calls for a referee independently implementing the definitions, returning an itemized verdict and exact corrections, plus the coordinator's own small check. A co-author can referee; a replay of the attacker's script is not independent. The project may have an exact reference calculation at small sizes, not a general answer key. Literature leads need verification at their sources. On a gap or false result the coordinator withholds establishment and can revise or record a dead end with a lesson and a successor question ([RT-RTE-review-integration](#rt-rte-review-integration), [RT-RTE-event-append](#rt-rte-event-append); SRC-1 `SKILL.md`, `references/loop.md`, `references/compute.md`, `references/codex.md`, `references/schema.md`).
3. **Integrate and return.** The coordinator applies corrections, updates proof notes, graph and table (moving displaced best results into history), and regenerates frontier inputs from computations as needed. Proof tier and review state are separate: code validated independently at earlier sizes can support a T3 run at a new size with independent replay still pending; exhaustive output from unchecked code stays T4 under review. The prescribed close is `check && build`, document rebuild, local or authorized private dashboard handoff, journal/plan/project memory update and commit if in scope. The user gets changes in resolved fractions and research status, including pending work. The next coordinator starts from the project state; Codex instructions recover from saved reports and the event log, checking host thread/job state before launching replacements. No transaction coordinates the project writes. Project memory is not permission to change persistent client memory, which requires a user request ([RT-RTE-build-views](#rt-rte-build-views); SRC-1 `SKILL.md`, `references/codex.md`, `references/loop.md`, `references/schema.md`, `templates/lab.py`).

> Use the project's journal, plan and memory files for durable research context. Update
> persistent client memory only at the user's request.
> --- `references/codex.md`

**Campaign and heavy computation.** When there are too many promising questions or progress stalls after changing approaches, the coordinator can launch a campaign. It builds briefs from labeled proofs, what's missing, closed routes and their lessons; assigns distinct directories, roles and shares of the session budget; and forwards literature leads while attackers work. Agents return final messages saved verbatim (with separate provenance); referees receive the claims and raw evidence rather than the attacker's reasoning context where the host permits that choice. Writers receive corrected results and produce exact edits tested on a copy, not an authority to modify the notes. A supervised editor may edit derived documents only. Long runs can commit data/events before review, then notes after the verdict. Lost notifications may be recovered from the transcript. At a scale requiring a cluster, jobs use authorized project infrastructure; the method prescribes independent code validation on the previous size, chunk accounting and resubmission of missing chunks. The coordinator, not the engine, decides which completed outputs to integrate. A queued job or completion notice is not a checked result ([RT-RTE-review-integration](#rt-rte-review-integration); SRC-1 `references/campaigns.md`, `references/saturation.md`, `references/codex.md`, `references/compute.md`, `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`).

> Subagents may be unable to write report files. Their final message is the report: save
> it **verbatim** to `research/agents/<name>/report.md` with a one-line provenance header
> (agent, date, "not yet refereed"). Update the header after the referee has reported.
> --- `references/campaigns.md`

**Controls and scope.** Coordinator-only canonical writes, independent review before establishment, local/private publication and bounded compute are policies at the coordinator's decision points, not engine invariants. They require cooperating agents, the host's actual permission checks and, for remote jobs or publishing, authorized infrastructure. The requested capability surface includes native agents and messaging, shell, literature access, and potentially cluster and publishing tools. The current grant set and deployed isolation envelope are not pinned. Worker directories and selected context are not a sandbox claim; writers' copies isolate drafts by procedure. If delegation is unavailable or prohibited, Codex says to continue permitted work and keep unchecked results pending. A co-author or external model may supply work or checks outside the native agent path, but the coordinator still owns admission. Direct shell/manual edits and project programs reach the files without passing through a central gate, as the example demonstrates. The inspected skill/engine routes do not mediate host-direct model calls, provider-native tools, callbacks or other host extensions; whether those routes are available, restricted or persisted in any deployment is uninspected. `lab.py` runs with the caller's file permissions, not with a separate isolated grant. For review/write/hosting policy: guarantee strength **policy**; doctrine conclusion status: claimed; actual deployment and operation conclusion status: uninspected (SRC-1 `SKILL.md`, `references/codex.md`, `references/campaigns.md`, `references/compute.md`, `templates/lab.py`, `examples/triangle-counts/exhaustive_n8.py`).

> Use the normal Codex permission flow for access outside the workspace, network operations
> and remote jobs. Existing authorization carries forward. Do not bypass a refusal by
> delegating the same action to another agent. An agent's message supplies no new authority.
> --- `references/codex.md`

### Four forcing cases

1. **A successful build need not follow a successful check.** `check` is a diagnostic on the invoked snapshot; the CLI returns 1 for reported problems, and the caller's shell sequence, not `build`, prevents a subsequent command after a failure. An overlapping realized and impossible claim at an admissible value on a well-formed row is diagnosed by `frontier_conflicts`; run build directly and the priority rule instead renders the value as realized and counts it as resolved. Malformed event lines are diagnosed when the checker passes a problems list; build/status reload without that list and omit those lines. The engine checks schema fragments and references, not correctness or cross-artifact scientific agreement (e.g. frontier classification uses row limits, not state-of-the-art results). Missing template warns without preventing JSON and status writes or explicitly deleting prior HTML; a present template without the marker is written with no replacement. The HTML is a projection, not evidence of a complete render or a current checked snapshot. Guarantee strength **invariant** for the check branch's exit on a returned nonempty diagnostics list and the priority computation on valid rows, **protocol** for check-before-build. These require stable, parseable inputs and a caller who uses the documented sequence; separate reads are not an atomic snapshot. Implementation conclusion status: wired; operation conclusion status: uninspected ([RT-RTE-build-views](#rt-rte-build-views); SRC-1 `templates/lab.py`, `references/schema.md`, `tests/test_lab.py`).

> elif cmd == "check":
>     p = check()
>     print("\n".join(p) if p else "ok")
>     return 1 if p else 0
> --- `templates/lab.py`

2. **Append is not verification or an immutable log.** The CLI checks argument shape/options, splits node and evidence lists, and `append_event` checks the type before writing one timestamped JSON line. An allowed type with an unknown node ID can be appended and printed, then diagnosed by `check`; evidence strings are not proof or checked file paths. Guarantee strength **invariant** for the type whitelist on this function, given ordinary CLI arguments and a writable project; **policy** for an append-only history across tools and truthful attribution. Direct file writes/backfill do not go through the append function. No locking or reconciliation with other project edits is established by that write. Implementation conclusion status: wired; operation conclusion status: uninspected ([RT-RTE-event-append](#rt-rte-event-append); SRC-1 `templates/lab.py`, `SKILL.md`, `references/schema.md`).

> if etype not in EVENT_TYPES:
>     sys.exit(f"unknown event type {etype!r}; use one of {', '.join(EVENT_TYPES)}")
> --- `templates/lab.py`

3. **Optional blueprint is a project-code path, not just a data file.** A project with `tools/blueprint_data.py` supplies a Python module imported through the project tools path, with the privileges of the engine call. This runs during node merge for check, build and status, before those consumers can inspect its data. Without the file the loader returns an empty list. The merge assigns defaults (including T2 for unrecognized provenance and established for non-conjecture kind), accepts per-ID overrides, adds dependency links and then appends curated nodes. `check` requires tests on open *curated* conjectures, not blueprint ones, and checks names on supplied refereed/human-checked review objects, not presence of a referee for every established node. Neither import nor overlay is a validation or approval gate. Guarantee strength **no claimed guarantee** of isolated import or reviewed provenance. Implementation conclusion status: wired; operation conclusion status: uninspected ([RT-RTE-blueprint-import](#rt-rte-blueprint-import); SRC-1 `references/schema.md`, `templates/lab.py`).

> if kind == "conjecture" and n.get("status") == "open" and not n.get("test") and n.get("source") == "labyrinth":
>     problems.append(f"{nid}: open conjecture without a stated test")
> --- `templates/lab.py`

4. **Shipped tutorial update can write established and refereed metadata without consuming a verdict.** The public initial example copies fixtures, enumerates small sizes and samples size eight, then checks and builds. The tutorial orders manual proposal, computation and review events before the later update. The executable NumPy route enumerates all seven-vertex graphs and neighbor subsets and prints the observed value set's size and complement as computed outputs. With `--write`, it checks for an existing exhaustive `k.n8`, then rewrites frontier, graph/history and state-of-the-art files in sequence. It supplies fixed review metadata and a fixed answered-door sentence; it does not check a report file, an event verdict or agreement with the conjecture before admission. The example docs identify review metadata as illustrative. Interruption after the graph write could leave the table stale and the idempotence guard could then stop a retry. Restore or reconcile the affected project files before rerunning; no automatic rollback is wired. Guarantee strength **protocol** for tutorial sequencing, not an invariant of the writer. Implementation conclusion status: wired; operation conclusion status: uninspected ([RT-RTE-example-update](#rt-rte-example-update); SRC-1 `docs/tutorial.md`, `examples/triangle-counts/README.md`, `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py`, `tests/test_lab.py`).

> review={"state": "refereed", "by": ["research/agents/referee-n8"], "verdict": "ESTABLISHED", "date": today})
> --- `examples/triangle-counts/exhaustive_n8.py`

**Changing the machinery.** Project-authored scripts, blueprint code and copies of the engine/template can change subsequent execution or output. The engine's optional table/status destinations are code settings, off by default. This is distinct from editing the installed package: maintainers change the method/templates, test, release and update installed clones by Git. Updating a clone is not a migration of project copies. Prior incidents shaped reusable guidance such as distinct scratch names and shared budgets, but the reported incidents do not wire project logs into a package updater ([RT-RTE-maintainer-update](#rt-rte-maintainer-update); SRC-1 `MAINTAINING.md`, `.github/workflows/tests.yml`, `references/lessons.md`, `templates/lab.py`).

**Evidence limits.** This is a source trace, not a target run. Expanded inspection of SRC-1 includes the tutorial writer and its retry guard, blueprint loader and validation/consumer branches, the campaign briefs and compute/saturation guidance, and the maintenance/test split. The engine tests specify expected classifier and example behavior, including example consistency after the tutorial update; discovery checks and live Codex recipes are distinct from those tests. None establishes an observed run here. The campaign and infrastructure anecdotes in `references/campaigns.md` and `references/lessons.md` are reported operation only. Client invocation, isolation, referee independence, rendering, grant enforcement, activation and benefit are not observed (SRC-1 `tests/test_lab.py`, `docs/codex-testing.md`, `references/campaigns.md`, `references/lessons.md`).

## Shared records

### Components

#### RT-CMP-lab
Label: Copied lab.py engine

Project-local Python code (symbolic, filesystem), dispatched by CLI. Computes projections and diagnostics and appends events; research agents are not its executors or outputs. SRC-1 `templates/lab.py`, `examples/triangle-counts/README.md`.

#### RT-CMP-host-models
Label: Host coordinator and delegated models

Distributed-parametric inference components supplied by Codex or Claude Code, with model state and serving substrate outside the project. SRC-1 `agents/openai.yaml`, `SKILL.md`, `references/codex.md`. Neither coordinator nor delegate versions are pinned by the skill. No weight update is requested or implemented on these routes; whether parameters actually change during provider operation is uninspected. Whether the endpoint or role selection can resolve to a different model is uninspected; there is no resolved endpoint or immutable version contract here. Optional external model submissions are imported results, not a pinned provider path.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-research-iteration
Label: Research iteration

User task and current project map → coordinator → next question/test → research output and handoff. Explicit or implicit selection is delegated to the host; choices within the iteration are made by the coordinator under the natural-language loop. Open research mode; stalled progress triggers changes in approach or scale. Humans authorize the task, may supply leads and set limits; no per-choice human approval is specified. Exact computations, proofs and checked sources are task-specific references, not an installed answer oracle. The content and assessment of conjecture revision are covered in [RT-RTE-review-integration](#rt-rte-review-integration). SRC-1 `SKILL.md`, `references/loop.md`, `references/saturation.md`, `references/codex.md`.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Research progress and pending work, with local or authorized private dashboard handoff.
- Later read-back: Later session starts from status, dashboard and project files; follow-up checks outstanding jobs and agents.
- Delegated visibility: Selected statement, known routes, closed routes and reference paths via briefs, subject to host access.
- Selection predicate: Choose up to three promising questions where a single computation or proof would change the map.
- Invalidation or expiry: Stale plans give way to updated map and journal; no automatic expiry of the research state is specified.
- Activation or effect: Prescribes changes of experiment, tool family and scale; behavioral dependence is not observed.
- Evidence limits: Shipped instructions and invocation metadata, not a host trace.

#### RT-RTE-review-integration
Label: Referee and integrate research results

Attack, long-run or external result → saved report/data and pending metadata → independent referee verdict/corrections and coordinator spot check → admitted, revised or withheld result. The coordinator owns canonical edits and may reject unsupported changes; the referee supplies grounds to withhold establishment, not file-write authority. A human co-author may check; user authorization is distinct from admission. In open research and campaigns, exact independent computation can provide a bounded reference outcome, with stated sample if full comparison is too expensive; model judgment is not itself an oracle. Writers propose only edits shaped by the verdict and style guide. The coordinator checks unique anchors and builds incrementally, corrects/reverts drift and re-anchors competing edits. The prescribed ordering permits pending data to persist before canonical note changes, not a transaction. SRC-1 `SKILL.md`, `references/loop.md`, `references/campaigns.md`, `references/schema.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Verdict per item and exact corrections; integrated result or a gap/refutation with pending or revised status.
- Later read-back: Updated notes/map and lessons inform subsequent choices and briefs; earlier table results remain in history.
- Delegated visibility: Attackers get selected write-ups and failed routes; a fresh referee gets claim, definitions, evidence and specific worries; writers get referee corrections and the affected section.
- Selection predicate: An eligible established result needs the appropriate proof/certificate and the prescribed independent check; a GAP or FALSE verdict is not admission as established.
- Invalidation or expiry: Correct or withdraw unsupported claims; retain a refutation and its lesson, and preserve old best results in history.
- Activation or effect: The protocol authorizes edits to the canonical research product after review, not proof by declaration.
- Evidence limits: Prompts and reported examples, with neither independent review traces nor a programmatic gate.

For mathematical conjectures (not the skill method itself), `theory-builder conditions 1–4`: (1) localized content conclusion status: claimed — a precise statement and test in a node or proof text; (2) consumption conclusion status: claimed — tested statement determines the target and conditions of the test; (3) content-directed criticism conclusion status: claimed — itemized counterexample or flaw (e.g. a missing hypothesis), verdict and exact correction shape what is retained; (4) iteration conclusion status: claimed — try a modified statement after refutation and brief later attacks with the closed route and its lesson. The scope and assumptions can be individually named in the statement, proofs and itemized objections, but there is no general formal decomposition. Persistence is across research sessions through project files and briefs. Learning (improved future capacity) is uninspected: the reported research progress does not isolate a capacity change. Reflection and reflective theory building are not established by revising mathematical claims; the separately reported changes to briefs are not a demonstrated iterative critique of the installed method. Autonomous theory building is not established: the model is instructed to coordinate, agents can compute and criticize, a co-author may supply review and the host/user controls are external; there is no observed all-computational sequence in the evidence. SRC-1 `references/loop.md`, `references/schema.md`, `references/campaigns.md`, `references/lessons.md`.

#### RT-RTE-event-append
Label: Append research event

CLI caller supplies type, summary, node IDs and evidence references. Engine checks type and writes timestamped JSONL. This admits trace data, not a result as established; a caller can decline/correct the input or edit files separately. SRC-1 `templates/lab.py`, `references/schema.md`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed event object on success.
- Later read-back: Later builds and status calls read the log for timeline and summary; coordinator may consult it in recovery.
- Delegated visibility: inapplicable — CLI has no delegation.
- Selection predicate: Recognized event type and accepted argument shape; no node existence or evidence check on append.
- Invalidation or expiry: No expiry or immutable-log enforcement; malformed lines are skipped on reads and reported in check.
- Activation or effect: Extends the project timeline.
- Evidence limits: Static command trace, not an audit of historical writers.

#### RT-RTE-build-views
Label: Check and build project views

Caller chooses check, build or status. CLI reloads project files; build classifies frontier claims in priority order, emits status and dashboard data, optionally tables/status copies, and substitutes data in the browser template when present. Browser readers interact with views, not canonical writes. SRC-1 `templates/lab.py`, `templates/dashboard.html`, `references/schema.md`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Check diagnostics/exit, status text, or build summary and files; HTML is conditional on a template.
- Later read-back: Rebuilt projections summarize accumulated events, research status and frontier in later sessions; the engine rebuilds from sources, not the prior dashboard.
- Delegated visibility: inapplicable — the engine delegates nothing; people and agents can open supplied files.
- Selection predicate: Explicit CLI verb; local input presence, classification priority, template presence and optional output settings govern outputs.
- Invalidation or expiry: Rebuild after corrections; old views can remain stale if not rebuilt or if a template is missing.
- Activation or effect: Produces derived views, not certification; on a well-formed row resolved fraction counts realized and impossible values only.
- Evidence limits: Inspected local code and browser consumers; no exercised rendering or authorized hosting result, and network dependencies are external.

#### RT-RTE-blueprint-import
Label: Import project blueprint

Project maintainer exposes Python `N`; CLI imports it when the project file exists, combines admitted statements with JSON overrides and curated nodes, then checks or projects them. Project authors determine code and overrides; no separate verdict, oracle or activation approval occurs in the loader. Trigger is the next status/check/build with the module present. Remove or revert the module/overrides to change the next merge; broken import fails rather than falling back. SRC-1 `templates/lab.py`, `references/schema.md`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Merged nodes to the caller's check, build or status function.
- Later read-back: Edited project statements and overrides can reach fresh engine invocations, with generated graph available to later readers.
- Delegated visibility: inapplicable — no worker launch.
- Selection predicate: File presence and per-ID override values; curated nodes are appended, not filtered through the blueprint defaults.
- Invalidation or expiry: No expiry; change or remove project inputs, rerun and rebuild.
- Activation or effect: Extends the graph source and admits executable project code on the import path.
- Evidence limits: Loader contract and code; no supplied project module execution or assurance about third-party module behavior.

#### RT-RTE-example-update
Label: Tutorial computation and update

Caller runs a bounded example, first generating frontier/scatter alongside copied fixtures; the later NumPy script computes all size-eight counts by one-vertex extension. Definitions and enumeration give the computation's reference procedure, while the tutorial separately calls for independent enumeration. The caller chooses printed result versus persistent write. The code, not a human verdict input, determines the admitted update after the flag and existing-node guard. Fixed fixture metadata and computed sets enter different fields. The prior state-of-the-art row is retained in history but is not a rollback mechanism. SRC-1 `examples/triangle-counts/README.md`, `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py`, `docs/tutorial.md`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed counts and, with the write option, updated frontier, graph/history and table.
- Later read-back: Subsequent check/status/build use those files; a later run inspects the existing kind of the target node.
- Delegated visibility: inapplicable — script does not launch a referee; tutorial review is a separate action.
- Selection predicate: Caller supplies the write option and a project path; existing exhaustive node short-circuits. No test of actual review evidence.
- Invalidation or expiry: Restore or reconcile files manually if interrupted or incorrect; no rollback, and rerunning the initial producer can replace frontier/scatter independently.
- Activation or effect: Replaces example result status and frontier classification; the script does not select the next conjecture.
- Evidence limits: Source and fixture/test expectations, not a supplied independent result or revision trace.

The conjecture and its test are localized in the tutorial/fixture (condition 1, doctrine conclusion status: claimed). For the **script**, condition 2 (consumption of the conjecture's content in deciding updates) is not established: the script embodies the fixed test but does not read the node's statement to determine the test or use agreement to choose a verdict. Condition 3 (content-directed criticism) and condition 4 (iteration from critique) are not established by this writer: its branches are for persistence and existing-kind detection, not comparing and revising formulations. The tutorial's human/coordinator route is separate. The named node is addressable as a unit and project files persist across runs; this update alone does not establish learning, reflection or an autonomous or reflective theory-building loop.

#### RT-RTE-maintainer-update
Label: Maintain and install skill changes

Human maintainer edits method, metadata, templates or examples, reviews tests and releases; installer updates checkout by Git. Tests are software checks on the proposal, not a runtime answer oracle for research or a content-specific acceptance arbiter. Maintainers can decline changes or revert in Git. No automatic per-project template update or log-fed edit is specified by this path. SRC-1 `MAINTAINING.md`, `.github/workflows/tests.yml`, `docs/codex-testing.md`, `references/lessons.md`.
- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate source change and test diagnostics; release procedure tags the accepted source for installation.
- Later read-back: Updated installed instructions affect later skill loads, and updated templates affect later copies.
- Delegated visibility: inapplicable — maintenance procedure does not dispatch a runtime research agent.
- Selection predicate: Human change and release decisions, with tests configured on pushes and pull requests and a separate install/update action.
- Invalidation or expiry: Git revision replacement or revert; existing project copies must be managed separately.
- Activation or effect: Can change future prompts and tooling, not evidence that an existing project switched to new behavior.
- Evidence limits: Maintenance instructions and workflow definition, no observed release or improvement attributable to a change.

### Claims

#### RT-CLM-map-progress
Label: Advance open research by changing the map

The skill claims progress when a proof, computation or refutation changes what the project knows or should try next, with refutations recorded rather than discarded. SRC-1 `SKILL.md`, `references/loop.md`. This is a declared objective, not a guarantee that a loop will yield a result.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-coordinator
Label: Skill guidance to coordinator

The host supplies skill instructions and the selected references to the coordinator. Natural-language procedural force over one task and its continuation on subsequent loads, subordinate to user scope and host enforcement. SRC-1 `SKILL.md`, `references/codex.md`. Delivery and compliance are unobserved.

#### RT-BAP-brief-worker
Label: Brief to worker

Coordinator supplies the filled role brief and specified evidence to an attacker, referee or writer through host delegation. It directs work and return for that assignment, not filesystem access control. A referee report supplies evidence and corrective proposals to the coordinator, not user authority. SRC-1 `references/campaigns.md`, `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`.

## Annotations

none
