---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Labyrinth Exploration's project research state, derived views, and selective session and campaign read-back"
run-id: AAS-2026-11-23-labyrinth-exploration-4000731242d4-01
source-identity: "https://github.com/nasqret/labyrinth-exploration"
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
---

# Labyrinth Exploration memory report

## Boundary and evidence

The memory boundary is the shipped research skill and project tooling at the revision in [boundary](boundary.md), including the browser's own view preference and the example's actual file producers. Project files are the unit of retention, not a bundled model memory service. Direct SRC-1 reads extend the supplied [runtime](runtime.md) baseline as follows. Executable paths support implementation conclusions; briefs and project conventions support doctrine only; campaign and engineering anecdotes are reported operation only.

| Entry or operation | Direct SRC-1 paths and layer | Coverage or limit |
|---|---|---|
| Setup, restart, close, side-project read, journal backfill | `SKILL.md`, `agents/openai.yaml`, `references/codex.md`, `references/loop.md`, `docs/tutorial.md` (doctrine) | [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration), [MEM-OBJ-project-handoff](#mem-obj-project-handoff). Initial seed content beyond fixtures and project-specific selection of documents are not pinned. |
| Campaign archives, fresh referee, writer/derived editor, escalation | `references/campaigns.md`, `references/compute.md`, `references/saturation.md`, `references/lessons.md`, `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md` (doctrine and attributed anecdotes) | [RT-RTE-review-integration](runtime.md#rt-rte-review-integration), [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker), [MEM-OBJ-agent-archive](#mem-obj-agent-archive), [MEM-RTE-extract-writeups](#mem-rte-extract-writeups). No actual briefs, provider payload or independent verdict archive. |
| CLI and callable functions | `templates/lab.py` (implementation), `references/schema.md` (doctrine) | Dispatch is help, event, check, build, status or usage error; loaders and transformations are callable Python, not a registered service. Tests import helpers; unsupported hypothetical library callers do not establish read-back. [RT-RTE-event-append](runtime.md#rt-rte-event-append), [RT-RTE-build-views](runtime.md#rt-rte-build-views), [RT-RTE-blueprint-import](runtime.md#rt-rte-blueprint-import). |
| Optional state-of-the-art exports | `templates/lab.py` (implementation), `references/schema.md` (doctrine) | [EPI-RTE-table-project](epistemic.md#epi-rte-table-project) produces distinct LaTeX and Markdown files ([MEM-OBJ-sota-tex](#mem-obj-sota-tex), [MEM-OBJ-sota-md](#mem-obj-sota-md)) when configured. Document integration is project-specific. |
| Browser resolution, filtering, view preference | `templates/dashboard.html` (implementation) | Inline snapshot, not a fetch of sibling JSON; [MEM-RTE-snapshot-browse](#mem-rte-snapshot-browse), [MEM-RTE-restore-tab](#mem-rte-restore-tab). |
| Example seed, generation and forced update | `examples/triangle-counts/README.md`, `examples/triangle-counts/knowledge.json`, `examples/triangle-counts/events.jsonl`, `examples/triangle-counts/sota.json`, `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py` (fixtures, doctrine, implementation) | [RT-RTE-example-update](runtime.md#rt-rte-example-update); fixture review labels cannot stand in for unbundled reports. |
| Evaluation and package maintenance | `tests/test_lab.py`, `tests/test_skill.py`, `tests/test_codex.py`, `.github/workflows/tests.yml`, `MAINTAINING.md`, `tools/codex_smoke.py`, `docs/codex-testing.md` (test/configuration source and procedure) | [RT-RTE-maintainer-update](runtime.md#rt-rte-maintainer-update); engine tests and discovery do not demonstrate live memory use. |
| Host state and services | `references/codex.md`, `references/campaigns.md`, `agents/openai.yaml` (doctrine); frozen tree and CLI dispatch checked | Skill metadata supplies instructions, not a memory tool registration or host hook contract. Shell, web, messaging, transcript and follow-up use exposed host capabilities; no MCP server required. Persistent client memory, context checkpoints/compaction, provider state and job scheduler internals are outside the pin: no verified storage, snapshot/reload or context isolation semantics. Private notes, blueprint, cluster runs, literature access and deployed hosting are not supplied; no conclusion about actual content, recoverability or access enforcement. |

## Core ideas

- **Keep the evidence and the decision separately.** An append or a saved report can precede review. The coordinator curates statements, tests, review fields and current best results; it can also keep a counterexample and a lesson for the next attack. The same JSON object may carry a claim and its pointers, but a referee name or status tag is not the verdict evidence. See [MEM-OBJ-review-metadata](#mem-obj-review-metadata) and [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).
- **Build several deliberately unequal views.** A short status and a browser snapshot are derived from the same project inputs but omit different material. Frontier projection ranks assertions and compresses reasons; it does not adjudicate them. A coordinator can return to raw sources. No engine output is an admission token. See [MEM-OBJ-status-summary](#mem-obj-status-summary) and [MEM-RTE-snapshot-browse](#mem-rte-snapshot-browse).
- **Select briefing content before delegation.** The coordinator selects a precise question, labeled proofs, missing steps and failed routes, aiming at about one page for an attacker. It limits iteration goals to three, not the model's token window. These are separate from CPU, concurrency and shared usage limits. A fresh referee receives claims, definitions and evidence rather than the attacker's reasoning where supported. Files are locators a worker must actually open. The frame analogy fits the distinct assignment and returned report, but imposes neither file isolation nor host context eviction. See [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker) and [MEM-OBJ-proof-documents](#mem-obj-proof-documents).

## Shared records

### Components

none declared in this member

### Operative objects

The runtime baseline declares no operative objects. Below, the checked, appended or transformed materials are distinct from the supplied routes and engine that operate on them.

#### MEM-OBJ-knowledge-nodes
Label: Curated knowledge nodes

Project-local `knowledge.json` stores interpreted statements, conjecture tests, hunch rationales, dead-end lessons and next steps with symbolic IDs, kinds, tiers, statuses and link edges. The coordinator seeds from project knowledge and can edit after review; initial human versus model authorship is not fixed. An ID or evidence path is a locator, not proof. Code uses fields for checks, counts and render categories; the coordinator and agents interpret content for research choices. The schema permits explicitly speculative and rejected material. SRC-1 `SKILL.md`, `references/schema.md`, `references/loop.md`, `templates/lab.py`; distinct inputs to [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-review-metadata
Label: Node review metadata

Project JSON `review` fields are symbolic state and metadata (reviewer pointers, date) plus a verdict label. The coordinator is instructed to derive them from independent review and its own spot check. The example writer can manufacture identical-shaped metadata without such an input. The checker tests shape, vocabulary and named reviewers for positive review labels; it does not resolve the reports or read their reasons. Status uses the pending state for a rollup/list, graph detail displays state, names and verdict, and table readers may instead see provenance in free-text SOTA status. SRC-1 `references/schema.md`, `templates/lab.py`, `templates/dashboard.html`, `examples/triangle-counts/exhaustive_n8.py`; distinct from the review procedure [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).

#### MEM-OBJ-blueprint-data
Label: Blueprint N and overrides

The project Python module contains executable symbolic code and may expose statement text, provenance, dependencies and locations. JSON overrides carry selected symbolic classifications/links and text fields for the matching ID, not a second independent proof. The actual project's production of `N` and authorship of overrides are unspecified. Code chooses defaults and copies the merged fields into checks and projections; human and model readers can see them as project results but default tier/status do not warrant that interpretation. No module is supplied for the example. SRC-1 `templates/lab.py`, `references/schema.md`; distinct input to [RT-RTE-blueprint-import](runtime.md#rt-rte-blueprint-import).

#### MEM-OBJ-events
Label: Research events

Local `events.jsonl`: timestamp, type, node and evidence locators are symbolic fields, summary is interpreted prose. CLI takes caller's account and timestamps it; initial journal backfill and direct file edits are separate admission paths. This is a narrated trace, not a verbatim conversation capture. Engine checks selected references, reflects the event in the timeline/summary and counts types, not the substantive verdict. Coordinators can reread it for progress or recovery. SRC-1 `templates/lab.py`, `templates/dashboard.html`, `references/schema.md`, `references/codex.md`, `SKILL.md`; distinct output of [RT-RTE-event-append](runtime.md#rt-rte-event-append).

#### MEM-OBJ-frontier
Label: Frontier claims

Local `frontier.json` stores explicit keyed numerical sizes, admissible ranges, witness values and interval classifications (symbolic, not learned embeddings); optional reason strings point to definitions, witnesses or arguments. Project scripts write it from computations and project claims, with example code also inserting analytic and conjectural intervals. Until reviewed, exact computation and its labels alone do not confer authority. Engine projection consumes the asserted intervals, then status and dashboard expose counts to the coordinator selecting next problems. SRC-1 `templates/lab.py`, `references/schema.md`, `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py`; input to [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-scatter
Label: Secondary scatter data

Optional project `scatter.json`: explicit keyed coordinates, series labels and source fields, not distributed weights. An example computation generates points; generic project-specific lineage is not fixed. Build passes the object through to a separate browser display, with no checked frontier admission by this path. SRC-1 `references/schema.md`, `examples/triangle-counts/make_example.py`, `templates/lab.py`, `templates/dashboard.html`; distinct from [MEM-OBJ-frontier](#mem-obj-frontier), shares [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-sota
Label: State-of-the-art rows

Local `sota.json` stores human/model-interpreted current result and status prose (also optional TeX) separately from symbolic IDs, grouping, reference/citation locators and dates. Coordinator controls the canonical table in the method; tutorial script directly updates a row. The dated `previous` entries retain old result text, not full provenance or rollback state. Browser and Markdown ([MEM-OBJ-sota-md](#mem-obj-sota-md)) display previous results; LaTeX ([MEM-OBJ-sota-tex](#mem-obj-sota-tex)) uses current fields and citations, not history. Both files derive from this input; neither is read back as the canonical table by the engine. SRC-1 `SKILL.md`, `references/schema.md`, `templates/lab.py`, `templates/dashboard.html`, `examples/triangle-counts/exhaustive_n8.py`; input to [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-sota-tex
Label: Generated LaTeX state-of-the-art table

A text file at the project-configured `SOTA_TEX` path (for example, `notes/sota-table.tex`; default off). When the caller requests a build with `sota.json` present and the path set, the formatter admits rows matching the listed groups in group and source row order and drops empty groups. It writes a LaTeX longtable. Current class and result use `cls_tex` and `result_tex` when present, otherwise escaped plain text. Status prose survives; note labels and bibliography keys become symbolic `\cref` and `\cite` commands. Row ID, kind, update date and dated previous results do not have output columns. The build inherits the input's claims; it makes no independent admission decision on their merits. A project notes build can resolve the locators against its labels and bibliography and deliver the typeset current result to readers. This is an afforded document use, not a verified inclusion or citation resolution. SRC-1 `templates/lab.py`, `references/schema.md`. This file is an output of [EPI-RTE-table-project](epistemic.md#epi-rte-table-project), not the producing operation or [MEM-OBJ-sota](#mem-obj-sota).

>                 refs = r"\cref{" + ",".join(e.get("refs", [])) + "}" if e.get("refs") else ""
>                 lit = r"\cite{" + ",".join(e.get("lit", [])) + "}" if e.get("lit") else ""
>                 where = "; ".join(x for x in (refs, lit) if x)
>                 cls = e.get("cls_tex", tex_escape(e.get("cls", "")))
>                 res = e.get("result_tex", tex_escape(e.get("result", "")))
>                 T.append(f"{cls} & {res} & {tex_escape(e.get('status', ''))} & {where}\\\\")
> --- `templates/lab.py:382-387`

#### MEM-OBJ-sota-md
Label: Generated Markdown state-of-the-art table

A separate text file at the project-configured `SOTA_MD` path (for example, `book/sota.md`; default off). The same build and group filter apply, but this switch is independent of LaTeX. Cells carry the plain class, current result and status prose, plus the update date and the ordered, dated prior result strings. The proof column carries note labels as code spans and bibliography keys as text, not resolved references or citation commands. Row IDs, kinds and TeX overrides do not drive this projection; past proof pointers, statuses and reasons cannot be reconstructed from the `date` and `was` pairs. A book author or direct Markdown reader can compare current and displaced results and use the locators to seek evidence; this is document read-back, not engine input, an established book inclusion, or validation of a result. SRC-1 `templates/lab.py`, `references/schema.md`. This file is another output of [EPI-RTE-table-project](epistemic.md#epi-rte-table-project), not the route, the source table or the LaTeX file.

>                 where = " · ".join(x for x in (", ".join(f"`{r}`" for r in e.get("refs", [])), ", ".join(e.get("lit", []))) if x)
>                 prev = "; ".join(f"{p.get('date', '?')}: {p.get('was', '?')}" for p in e.get("previous", [])) or "–"
>                 M.append("| " + " | ".join(md_cell(x) for x in (e.get("cls", ""), e.get("result", ""), e.get("status", ""),
>                                                                 where, e.get("updated", ""), prev)) + " |")
> --- `templates/lab.py:399-402`

#### MEM-OBJ-frontier-history
Label: Frontier history milestones

Local `knowledge.json` contains this separate JSON list, with symbolic size/date/resolved fraction and interpreted `why`. The example writer appends a fixed 1.0 and a method description after computing the size-eight result; build forwards the list, does not synthesize it from the timeline, and the browser filters milestones with a resolved value and shows the reason on hover. General projects' milestone admission is unspecified beyond the data contract. SRC-1 `references/schema.md`, `templates/lab.py`, `templates/dashboard.html`, `examples/triangle-counts/exhaustive_n8.py`; distinct input to [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-agent-archive
Label: Agent report and provenance

Project filesystem `research/agents/<name>/report.md` contains the final message verbatim, including statements, verdicts or exact replacement proposals in prose, plus a separately maintained provenance header. This is a selected return, not a transcript or proof of execution. Coordinator saves the message as it arrives or recovers it from host transcript, then changes the header after review. Review consumers receive the report and check independently; the header alone has no admission force. SRC-1 `references/campaigns.md`, `references/codex.md`, `templates/briefs/referee.md`; distinct material in [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).

#### MEM-OBJ-compute-evidence
Label: Computation and source evidence

The agent archive and cluster run directories hold scripts, source papers, counterexamples, counts and outputs named in reports/events. Filesystem substrates include code, natural-language documents, JSON data and compressed archives with manifests. Project programs produce machine-readable data, agents or authors supply claims and checks; full literature text goes to a gitignored subfolder by brief policy. The independent verifier can read authors' code for definitions only and work from raw evidence. Chunk manifests, job IDs and quotas bear on completeness/recovery, not mathematical validity. Actual remote formats, storage and job states are not supplied. SRC-1 `references/compute.md`, `references/loop.md`, `templates/briefs/attack.md`, `templates/briefs/referee.md`; supporting material, not [RT-RTE-review-integration](runtime.md#rt-rte-review-integration) itself.

#### MEM-OBJ-project-handoff
Label: Project journal, plan and memory

Project files carry interpreted progress, pending work and next door; journal also records thread ID, role, directory and state as access/recovery metadata. Coordinator updates them at stable points; prior journal can seed a backfilled event log. No common codec or automatic edit or initial writer specified. Later coordinator may check saved state against current host/job state; IDs are not evidence of liveness. Dashboard handoff location in project README is a pointer, not the view. SRC-1 `SKILL.md`, `references/codex.md`, `references/loop.md`; distinct material in [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration).

#### MEM-OBJ-proof-documents
Label: Notes, guide and write-ups

Project-authored mathematical prose and proofs in documents with symbolic labels used as extraction and cross-reference anchors. The coordinator edits canonical notes after checking drafts; derived guide, write-ups and book are rebuilt or explicitly made working copies with a designated canonical version. Readers use the proofs; workers are asked to read selected sections. Project-specific originals, extraction code and working-copy choices are not pinned. SRC-1 `SKILL.md`, `references/loop.md`, `references/campaigns.md`, `templates/briefs/writer.md`; supporting material, not the route [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker).

#### MEM-OBJ-status-summary
Label: Status summary

Generated local Markdown or stdout combines symbolic counts/IDs and interpreted node and event text. Status lists the last 25 loaded event entries in file order, not the latest by timestamp, with no event node/evidence paths. The board-like sections list selected kinds without the browser board's status filters; titles and statements do not include lessons/tests as separate fields. Status counts project state; it does not write that state. Optional book copy is a separate destination for the summary, off by default. SRC-1 `templates/lab.py`; output of [RT-RTE-build-views](runtime.md#rt-rte-build-views).

> for e in events[-25:]:
>     L.append(f"- {str(e.get('ts', ''))[:16]} · {e.get('type', '?')} · {e.get('summary', '')}")
> --- `templates/lab.py`

#### MEM-OBJ-dashboard-snapshot
Label: Dashboard snapshot

Two generated local representations of the same assembled data: standalone JSON and data embedded in HTML with browser code. Contains merged nodes, parsed event objects, optional scatter and SOTA, separately supplied frontier history, priority-projected frontier and summary. Payload includes links/evidence fields not rendered in every view. Code admits parseable event objects even when `check` would flag them. The page reads its inline payload; no canonical-file write-back or automatic freshness on later page opening. SRC-1 `templates/lab.py`, `templates/dashboard.html`; distinct output of [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### MEM-OBJ-labyrinth-tab
Label: Browser tab preference

Symbolic string stored in browser localStorage under `labyrinth-tab`, independent of the project snapshot. Click or startup selection writes it through page code, with storage failures ignored. Later page initialization may use it if there is no valid route selection and storage is available. No research content persisted by this key. SRC-1 `templates/dashboard.html`; no counterpart in [RT-RTE-build-views](runtime.md#rt-rte-build-views), which produces files rather than browser state.

### Routes

#### MEM-RTE-snapshot-browse
Label: Browse generated snapshot

A browser reader opens built HTML and selects a view. Browser code takes the embedded snapshot, not a live external store. This downstream consumer is distinct from [RT-RTE-build-views](runtime.md#rt-rte-build-views), which ends at output files. SRC-1 `templates/dashboard.html`, `templates/lab.py`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered map/frontier, scatter, graph, board, timeline, SOTA or tables.
- Later read-back: A later page load can inspect a prior build; no canonical reload until rebuild and new page load.
- Delegated visibility: inapplicable — page code does not dispatch workers.
- Selection predicate: Tab and filters; graph matches title and ID substrings to dim rather than remove nonmatches, and node detail shows at most 12 incoming and 12 outgoing links; timeline sorts by timestamp.
- Invalidation or expiry: Rebuild after edits and reload the new snapshot; previous copies can remain.
- Activation or effect: Requested detail shows tests/lessons and review information if present; bins omit individual reasons. Browser choices do not revise research state.
- Evidence limits: Source wiring, not a live rendering or observed research decision.

#### MEM-RTE-restore-tab
Label: Restore prior tab

Browser JS saves the selected tab ID on selection and reads it at initialization; the subject is a preference, distinct from the projection in [RT-RTE-build-views](runtime.md#rt-rte-build-views). SRC-1 `templates/dashboard.html`.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected panel and best-effort preference write.
- Later read-back: Later dashboard initialization reads prior ID when the URL-derived candidate is invalid or missing.
- Delegated visibility: inapplicable — browser UI only.
- Selection predicate: Query tab before hash, then stored ID, then map if missing or invalid; only visible tab IDs accepted.
- Invalidation or expiry: Replacement on selection, storage clearing or rejection by current tab set; no application expiry.
- Activation or effect: Restores a view, and graph selection invokes graph construction; does not select a research claim.
- Evidence limits: Browser storage availability, retention and partitioning in a deployment are uninspected.

#### MEM-RTE-extract-writeups
Label: Extract anchored write-ups

Coordinator or project document tooling derives briefing/reading artifacts from proof notes. Distinct upstream document transformation before [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker), not the engine projection in [RT-RTE-build-views](runtime.md#rt-rte-build-views). SRC-1 `SKILL.md`, `references/loop.md`, `references/campaigns.md`, `templates/briefs/attack.md`.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Regenerated guide/write-ups for human readers and campaigns.
- Later read-back: Later coordinator references relevant labels and a worker opens selected sections; proofs and status guidance survive at project scope.
- Delegated visibility: Only selected sections and pointers are requested in the brief, not the whole body of notes.
- Selection predicate: Project-set anchors and coordinator-selected topic and missing ingredient; aim at one relevant self-contained write-up, not a token cap.
- Invalidation or expiry: Rebuild after changed anchors; if made a working copy, stop regenerating it and name the canonical copy.
- Activation or effect: Supplies reusable interpreted proofs and evidence; build-success checks do not establish correctness.
- Evidence limits: Project extractor and actual per-invocation read set not supplied.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Resumption uses narrower status text for starting selection, then dashboard and project reads for detail; the instructions do not specify a token budget or automatic transcript condensation. The useful read-back inputs include recent changes, unresolved bands and outstanding job/review state. The actual retained project handoff and transcript payload are not pinned. SRC-1 `SKILL.md`, `references/codex.md`, `references/loop.md`, `templates/lab.py`.

#### On [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Keep the exact report, independent check, reason and raw counterexample distinct from the changed text and symbolic metadata. A gap or false result can survive as a dead end with a lesson and link, not as an established claim, and a future brief carries that lesson. The engine neither synthesizes the lesson from the event stream nor infers a correctly modified claim from a verdict label. SRC-1 `references/loop.md`, `references/campaigns.md`, `templates/briefs/referee.md`, `templates/briefs/attack.md`, `templates/lab.py`.

> - **Refuted:** add a `deadend` node with the counterexample and a `lesson`, and link it
>   (`refutes`) from what refutes it. Then write the modified statement and test it.
> --- `references/loop.md`

#### On [RT-RTE-event-append](runtime.md#rt-rte-event-append)

Build embeds parsed event objects without a type/reference recheck; status reduces the same parsed stream to a short tail; browser timeline exposes timestamp/type/summary, not event pointers. A `computed` append can be under review: timeline counters grouping it with `proved` do not upgrade authority. SRC-1 `templates/lab.py`, `templates/dashboard.html`, `references/loop.md`.

#### On [RT-RTE-build-views](runtime.md#rt-rte-build-views)

The three commands do not have identical read sets. Check does not read scatter or regenerate outputs; status reads merged nodes, classified frontier and events only; build also reads scatter, SOTA and project presentation data and writes views. In-memory rendering intermediates are not checkpoints. Classification clips to the admissible grid and selects the highest-priority reason, first-listed on ties. Adjacent equal-status runs can keep only the first reason and a gloss; beyond 1,500 runs, up to 400 bins carry status counts, not reasons. Bounds and history metadata are carried separately. SRC-1 `templates/lab.py`, `templates/dashboard.html`.

> runs = runs_of(segs, step)
> --- `templates/lab.py`

> "runs": runs if len(runs) <= RUN_LIMIT else None,
> "bins": None if len(runs) <= RUN_LIMIT else bins_of(segs, lo, top, step, log_scale),
> --- `templates/lab.py`

#### On [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker)

An attacker reads selected proof sections, named examples, closed routes with reasons and available data; the coordinator can send fresh literature leads mid-assignment. A referee reads definitions and raw evidence, ideally without inherited reasoning; a writer reads reviewed results and exact corrections by ID, with a copy used for tests. Each selection controls supplied input, not guaranteed visibility or compliance. Return paths include original files and final message, with the coordinator explicitly selecting the message for durable storage; a lost notification has a documented transcript fallback. SRC-1 `references/campaigns.md`, `references/codex.md`, `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`.

#### On [RT-RTE-example-update](runtime.md#rt-rte-example-update)

The persistence flag delegates content selection to code; it is not per-item human admission. Computed values and their complement shape the retained frontier; the answered-door statement, attainment milestone and review fields are preset, and the writer does not consume the preceding review events. The guarded rerun and table history do not restore prior frontier or knowledge state. SRC-1 `examples/triangle-counts/exhaustive_n8.py`, `docs/tutorial.md`.

## Write side

**Fixture counterexample to a single authority flag.** The initial example's `ex.small` is simultaneously T3, `established` and `under-review`; its SOTA row says “exhaustive (under review),” and the event marks the size-seven computation as pending. A different node, `x.allbelow`, retains the rejected statement and a size-five counterexample as a lesson, while the refutation event retains its own summary and evidence pointer. These are inspectable fixture distinctions, not observations of a review or refutation process. SRC-1 `examples/triangle-counts/knowledge.json`, `examples/triangle-counts/events.jsonl`, `examples/triangle-counts/sota.json`; [MEM-OBJ-review-metadata](#mem-obj-review-metadata), [MEM-OBJ-events](#mem-obj-events).

> "lesson": "Removing edges destroys triangles in discrete amounts, so gaps also appear below the top band: n = 5 misses 6.",
> --- `examples/triangle-counts/knowledge.json`

**Setup and acquisition.** New-project instructions prescribe an empty or seeded graph, event backfill from a journal, initial SOTA rows and separate copies of the engine/template. The coordinator is the instructed performer, with no fixed human approval operation for each seed; the example fixture author supplied a different starting state. Reuse existing state on resume. Later a CLI caller supplies an event's meaning and paths while the engine admits recognized types and performs append; the code is not its author or referee. The coordinator physically saves reports, while the reporting worker authors the body; a provenance edit changes the header, not the underlying report. Side projects are read-only and their changes can be logged; literature agents offer leads, which must be checked at the source before relying on them. See [MEM-OBJ-project-handoff](#mem-obj-project-handoff), [MEM-OBJ-events](#mem-obj-events), [MEM-OBJ-agent-archive](#mem-obj-agent-archive) (SRC-1 `SKILL.md`, `references/codex.md`, `references/loop.md`, `templates/lab.py`).

**Curation, rejection and withdrawal.** [RT-RTE-review-integration](runtime.md#rt-rte-review-integration) admits via a coordinator decision, not a human-confirmation requirement or a Python gate; a human co-author may supply review. The spot check and independent code test are bounded task-specific evidence. Unchecked imported claims may be logged while pending, but do not meet the protocol for establishment. For refutation, preserve the counterexample, exact correction or lemma scope, and a concise lesson; change status or add a dead-end node and successor with its own test. Writers cannot change canonical notes under this policy; unsupported edits are reverted, exact-old replacements must be uniquely anchored, and derived docs rebuilt. Old table text remains in history but does not preserve a full rollback. Direct edits, blueprint import and the example's guarded writer bypass verdict checking; no invalidation propagates atomically to data, references, old exports or other copies. SRC-1 `references/loop.md`, `references/campaigns.md`, `references/saturation.md`, `templates/lab.py`, `examples/triangle-counts/exhaustive_n8.py`.

**Generated table maintenance.** A project author can configure either export destination; invoking build does not approve individual rows. The formatter rewrites the enabled files from the current input when reached. After correction or withdrawal, rebuild the enabled exports and any downstream documents. Disabling an output or removing `sota.json` does not delete an old export. [MEM-OBJ-sota-tex](#mem-obj-sota-tex) loses previous results; [MEM-OBJ-sota-md](#mem-obj-sota-md) keeps earlier result text, not a recovery snapshot or a justification for replacement. SRC-1 `templates/lab.py`, `references/schema.md`.

> - In `lab.py`: `SOTA_TEX` and `SOTA_MD` (paths, default `None`) also write the
>   state-of-the-art table as a LaTeX longtable and as Markdown, and `BOOK_STATUS` copies
>   `STATUS.md` somewhere else.
> --- `references/schema.md`

**Automatic transformations and evidence maintenance.** Computational observations → explicit frontier values/intervals in JSON → priority projection, summaries and display snapshot → future coordinator/browser consumption. Human/model-curated tests, dead ends and lessons are trace-derived by protocol, not automatically learned from the log; the event-to-timeline and tail transformations organize the trace but do not infer a new research claim. Summary variants are re-readable outputs, not snapshots of the model's accumulated token context. Text extraction retains proof reasons by design; status, bins and other narrower views can drop them. Test source compares the classifier to brute force, asserts generated example outputs and plants diagnostics; these and CI operate on software behavior, not referee results. Heavy-compute instructions distinguish submitted/completed/verified jobs; compare manifests before deleting originals, leave restoration directions, atomically publish chunk summaries and use a separate checker before resubmitting missing chunks. That is conditional cleanup and evidence recovery, not scientific retraction or a proven cluster workflow. See [MEM-OBJ-frontier](#mem-obj-frontier), [MEM-OBJ-status-summary](#mem-obj-status-summary), [MEM-OBJ-compute-evidence](#mem-obj-compute-evidence) (SRC-1 `references/compute.md`, `references/campaigns.md`, `templates/lab.py`, `tests/test_lab.py`, `.github/workflows/tests.yml`).

> - **Archive finished run directories**:
>   - one `.tar.gz` per directory, with a manifest;
>   - delete the originals only after the archive lists every file (compare the counts);
>   - leave a README that explains how to restore.
> --- `references/compute.md`

## Read-back

| Consumer | Trigger, selection and delivery | Authority and limits |
|---|---|---|
| Coordinator on restart or stalled iteration | Explicit status/dashboard and project file opens; from unresolved band, current statements and expected impact select up to three questions. Check journal/thread and job state before replacements; on missing delivery consult transcript, on restart use saved reports/event log, or resume a still-available agent by host follow-up. | [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration); tailored manual/model selection, not project auto-injection or proof of a live host checkpoint. |
| Attacker, referee, writer, editor | Coordinator composes role-specific brief; references are followed on demand. Forward selected literature leads as they arrive instead of waiting for worker requests. Under-review report arrival triggers the prescribed referee dispatch, short fresh context where available; exact corrections and a copy go to the writer. Editor works one supervised pass on derived docs when writers are not active. | [RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker); selected guidance plus file access, no observed compliance; no evidence of independent automatic push from a retrieval service. |
| Engine and tutorial writer | Explicit command/function call reloads named inputs, or imports project code per file presence; next example write inspects target node's existing kind. Build emits data/index/status and optional configured outputs; `check` emits diagnostics/status code, not a retained verdict. | [RT-RTE-build-views](runtime.md#rt-rte-build-views), [RT-RTE-blueprint-import](runtime.md#rt-rte-blueprint-import), [RT-RTE-example-update](runtime.md#rt-rte-example-update); deterministic branches on accepted input shapes, no scientific approval. |
| Browser/document reader | Open generated artifact, select a front-page view, follow graph/board/detail or project document links and labels. Browser may remember a tab; reader can return to original files when rendered metadata omits evidence. Local handoff by path is default; authorized private publishing is conditional, not a shipped service. | [MEM-RTE-snapshot-browse](#mem-rte-snapshot-browse), [MEM-RTE-restore-tab](#mem-rte-restore-tab), [MEM-RTE-extract-writeups](#mem-rte-extract-writeups); opening an old snapshot does not replay decisions or revalidate sources. |
| Notes compiler or Markdown/book reader | After a configured build, include the generated longtable or open/include the Markdown file. Both get the grouped current results; LaTeX can resolve current citation keys through document machinery, while Markdown exposes raw locators and keeps dated result history. | [MEM-OBJ-sota-tex](#mem-obj-sota-tex), [MEM-OBJ-sota-md](#mem-obj-sota-md); advised by project conventions, but no pinned include site or exercised citation resolution. Neither view validates the underlying research. |

## Integration issues

- **Projection correction.** Read the combined [RT-RTE-build-views](runtime.md#rt-rte-build-views) as distinct modes, not a shared load-all path. Status omits SOTA/scatter and has a file-order tail; timeline uses sorted parsed events and does not display their evidence fields. The label “Established (proved, computed)” is a count of event types, not a review decision. Board's “Dead ends” also includes dropped hunches, and a display class inferred from SOTA status is not a new verdict. SRC-1 `templates/lab.py`, `templates/dashboard.html`; [MEM-OBJ-status-summary](#mem-obj-status-summary), [MEM-RTE-snapshot-browse](#mem-rte-snapshot-browse).
- **Admission qualification.** Status and build may carry pending, malformed-in-shape, stale or mutually inconsistent claims; syntactically malformed JSONL is skipped, whereas parseable dictionaries can survive even with unknown types/IDs. A refuted item can still appear in a history, table or older build. Check does not compare frontier bounds to SOTA or resolve evidence files; fixture `review` and blueprint defaults do not establish vetting. SRC-1 `templates/lab.py`, `references/lessons.md`, `examples/triangle-counts/exhaustive_n8.py`; [RT-RTE-blueprint-import](runtime.md#rt-rte-blueprint-import), [RT-RTE-example-update](runtime.md#rt-rte-example-update), [MEM-OBJ-review-metadata](#mem-obj-review-metadata).
- **Recovery and provenance unknowns.** Private project seed authorship, exact extractor and document canonicality, archive manifests, actual review provenance, resolved job/thread IDs and host transcript retention are not supplied. These prevent claims of complete reconstruction, exercised isolation, reliable withdrawal propagation or guaranteed independent review. SRC-1 `references/codex.md`, `references/compute.md`, `references/loop.md`; [MEM-OBJ-project-handoff](#mem-obj-project-handoff), [MEM-OBJ-proof-documents](#mem-obj-proof-documents), [MEM-OBJ-compute-evidence](#mem-obj-compute-evidence).
- **Optional exports.** [EPI-RTE-table-project](epistemic.md#epi-rte-table-project) supplies the producer, not either retained file. [MEM-OBJ-sota-tex](#mem-obj-sota-tex) and [MEM-OBJ-sota-md](#mem-obj-sota-md) cover separately enabled artifacts with different information reaching readers. No pinned notes or book inclusion establishes actual consumption; stale copies can remain after reconfiguration or withdrawal. SRC-1 `templates/lab.py`, `references/schema.md`.
- **Separate identities.** No duplicate of a supplied declaration identified. Browser snapshot consumption and tab restore begin after output generation; document extraction creates briefing material before briefing, and does not dispatch a worker. Runtime baseline declares no operative objects.

## Limitations and checks

Source identity rechecked by listing SRC-1's frozen Git tree at `019a93da59313e697dc6f28bcfe1588a376c7565` and reading source at that commit. Method checkout HEAD rechecked as `726fb8936eaf510febfdb077e94319d3cd5f5789`; run identity and boundary fields match the supplied invocation and boundary. No target, model service, browser or test suite executed; there is no run evidence for actual recall, accepted corrections, suppression of repeated mistakes or improved capacity. Campaign anecdotes in SRC-1 `references/campaigns.md` and `references/lessons.md` do not isolate effects.

Validation: passed the deterministic memory-member content check; this is not a claim of analytical acceptance.
