---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "CORAL memory: island-local notes, mutable skills and roles, checkpoint lineage, query consumers and host-owned session context."
run-id: AAS-2026-10-15-coral-25e5fdab9dc4-01
source-identity: https://github.com/Human-Agent-Society/CORAL
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
---

# CORAL memory report

## Boundary and evidence

CORAL retains experiment state and shared knowledge outside the coding harness's conversation. This report includes notes and raw captures, indices and coverage ledgers, evolved skills and roles, attempt/checkpoint lineage, migration announcements, query/dashboard read-back, warm-start and maintenance instructions, and session-recovery pointers. Candidate code remains a product snapshot, not automatically a memory abstraction. External harness compaction, provider state and weight updates are outside the inspectable implementation boundary.

All source evidence is SRC-1 at the revision above, registered in [boundary](boundary.md#source-register). Direct inspection extended the supplied runtime baseline with `coral/hub/notes.py`, `coral/hub/skills.py`, `coral/hub/checkpoint.py`, the note/skill handlers in `coral/cli/query.py`, CLI registration in `coral/cli/__init__.py`, knowledge handlers in `coral/web/api.py`, seeding in `coral/workspace/project.py`, shared-state setup in `coral/workspace/worktree.py`, `coral/agent/warmstart.py`, arrival-note writing in `coral/agent/manager.py`, archive filtering in `coral/hub/attempts.py`, and the bundled skills and scripts identified below. Executable source supports implementation findings; prompt/skill instructions support doctrine/design findings only. No target execution, supplied run trace or intervention establishes actual compliance, activation or benefit.

| Entry point or operation | Source path / evidence basis | Coverage and prevented conclusion |
|---|---|---|
| Shared-state seeding and links | Direct: `coral/workspace/project.py`, `coral/workspace/worktree.py` | [MEM-OBJ-skills](#mem-obj-skills), [MEM-OBJ-roles](#mem-obj-roles); launch progression remains [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch). Runtime-specific parity is not established. |
| Note authoring, reflect, pivot, consolidate | Direct: `coral/template/skills/create-notes/SKILL.md`, `coral/hub/prompts/reflect.md`, `coral/hub/prompts/consolidate.md`; pivot references searched | [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision); framework delivers requests, not verified revisions. |
| Research and warm-start | Direct: `coral/agent/warmstart.py`, `coral/template/skills/deep-research/SKILL.md`, grounding-check body | [MEM-OBJ-raw-sources](#mem-obj-raw-sources), [MEM-OBJ-note-navigation](#mem-obj-note-navigation), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision). Source-type capture recipes and reviewer implementation remain uninspected; cannot establish capture fidelity or review validity. |
| Notes list/search/read; legacy notes and insights | Direct: complete `coral/hub/notes.py`, note handler in `coral/cli/query.py`; dispatch searched | [MEM-RTE-knowledge-query](#mem-rte-knowledge-query). Includes raw opt-in, status filters, numeric/non-numeric read divergence and graph projection. |
| Skills list/read and alternative service read | Direct: complete `coral/hub/skills.py`, CLI skill handler, web knowledge handlers | [MEM-OBJ-skills](#mem-obj-skills), [MEM-RTE-knowledge-query](#mem-rte-knowledge-query). CLI ambiguity and dashboard first-match behavior differ. |
| Organization, deduplication, movement, linking | Direct: complete organize-files skill, move/index scripts; resolver loading and matching body inspected | [MEM-RTE-note-maintenance](#mem-rte-note-maintenance). Dedup scorer, judge prompt, resolver write tail and audit shell internals remain uninspected; cannot claim complete preservation or correct merge decisions. |
| Note lint / grounding check | Direct: lint checks and main; grounding checks and main | [MEM-CLM-grounding-gate](#mem-clm-grounding-gate). Checks inspect metadata/links, not semantic truth; ordinary invocation is advisory. |
| Skill extraction, testing and packaging | Direct: complete `coral/template/skills/skill-creator/SKILL.md`; bundled-file inventory | [MEM-OBJ-skills](#mem-obj-skills), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision). Several prescribed helper modules are not bundled here; external resolution uninspected. |
| Eval checkpoint and history/diff | Direct: complete `coral/hub/checkpoint.py`; submission linkage searched and supplied runtime | [MEM-OBJ-checkpoint](#mem-obj-checkpoint); [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission). Captures existing files, not a derived lesson or semantic admission gate. |
| Grader result → manager feedback | Supplied [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback) | Attempt annotation below; not an independently observed learning loop. |
| Rewind, soft deletion, direct-hash recovery | Direct: `coral/hub/attempts.py` archive/read bodies; supplied resume route | Annotation on [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering). Does not establish shared-knowledge rollback. |
| Island migration and arrival note | Direct: arrival writer and shared-state link setup; supplied migration route | [MEM-OBJ-migration-arrival](#mem-obj-migration-arrival), annotation on [RT-RTE-island-migration](runtime.md#rt-rte-island-migration). Destination links are not source-context erasure. |
| Session IDs, logs and opaque host recovery | Manager symbol search plus supplied resume/delegation routes | [MEM-OBJ-session-state](#mem-obj-session-state), annotations below. Exact host replay/summary/compaction policies are uninspected. |
| Plugin hook and runtime tool surface | Supplied [RT-RTE-machinery-admission](runtime.md#rt-rte-machinery-admission), [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation); CLI command registration searched | Plugin supplies skill pointers; external harness tools perform file edits. No separate CORAL memory-tool server was established by these inspected paths; this is not a repository-wide absence claim. |
| Frontend and alternate harness context | Available but not directly inspected: `web/src/pages/Knowledge.tsx`, remaining adapters and single-agent template | Backend read-back is established, not frontend rendering fidelity, uniform skill discovery, or adapter-equivalent context handling. |

## Core ideas

1. **Shared files are the learning substrate offered to agents.** Research findings, experiment explanations and reusable skills are separate from attempt JSON and logs. Prompts ask the model to turn results into reasons and future actions; code does not automatically synthesize a true lesson ([MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision)).
2. **There are several different selectors.** A model follows an index or filesystem path, CLI code performs literal substring/status/date selection, dashboard code builds projections, and manager code pushes selected score feedback. None of these establishes semantic retrieval or a common token budget ([MEM-RTE-knowledge-query](#mem-rte-knowledge-query), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback)).
3. **Curation changes reachability differently for different readers.** `_archive/` is excluded by the generated index but not by the hub's user-note walker. Supersession metadata produces graph edges, not automatic withdrawal from the default list. A file remaining on disk can therefore still be delivered by a broad read ([MEM-RTE-note-maintenance](#mem-rte-note-maintenance)).
4. **Checkpoints preserve lineage, not adoption decisions.** A submission snapshots shared state before grading. The lock serializes checkpoint commits, not all agent file writes; checkpoint failure is tolerated. A later score cannot certify the checkpoint's notes ([MEM-OBJ-checkpoint](#mem-obj-checkpoint)).
5. **Context continuity has two independent channels.** Shared files remain available after a fresh start, while saved conversation state is host-owned. Migration changes shared roots without necessarily removing old conversation material ([MEM-OBJ-session-state](#mem-obj-session-state)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Authored notes and synthesized knowledge

Markdown bodies in `public/notes/` or `islands/<id>/notes/` are natural-language material: research, experiment, infrastructure, focus and synthesis notes. YAML metadata is a separate symbolic access/lineage part: creator/date, claim/status/confidence, attempt references, supersedes/refutes and tags. Textual claims still need interpretation; parsed status does not establish truth. Metadata is surfaced to JSON and graph consumers; bodies go to models or operators. Legacy `notes.md` and `insights/` are alternative admission/read-back formats. This is distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt): notes interpret results rather than merely recording candidate/result identity.

Source: SRC-1, `coral/hub/notes.py`, `coral/template/skills/create-notes/SKILL.md`. Parser lenience keeps malformed/legacy content visible and labels missing creators `unknown`. Reasons, failures and counter-evidence are requested by the skill, not verified properties of runtime-created notes.

> Falls back to a lenient line-by-line parse
> if the block isn't valid YAML, so a malformed frontmatter never drops the
> note.
> --- `coral/hub/notes.py`

#### MEM-OBJ-raw-sources
Label: Raw research captures and review sidecars

`notes/raw/*.md` holds saved external-source text with provenance metadata, not raw agent execution traces. Captures are readable natural-language content plus symbolic URL/type/capture/retriever fields. Their initial evidence may originate in web pages, papers or other sources; capture completeness is unresolved. The deep-research skill requests retrieval before synthesis and links from derived research notes back to raw material. It also requests `<slug>.review.json` per-claim reviewer verdicts. Those JSON sidecars are symbolic review artifacts, not an independent correctness certificate. The producer and updater are model/tool operations; immutability of raw files is prescribed, not physically enforced by the note reader.

Distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt): external research input and synthesis review are not candidate grading. Source: SRC-1, `coral/template/skills/deep-research/SKILL.md`, `coral/hub/notes.py`, `coral/web/api.py`.

> Use `WebFetch` to get the full page, then write it to `notes/raw/`. These are immutable — never edit raw sources, only reference them from research notes.
> --- `coral/template/skills/deep-research/SKILL.md`

Hub note enumeration excludes raw by default; dashboard opts in, and an agent can follow a research-note link through its file tool. Thus default CLI exclusion is not absence of a raw-source read path.

#### MEM-OBJ-note-navigation
Label: Index, coverage ledger and aggregate knowledge files

`notes/index.md` is a generated or agent-edited Markdown discovery surface. `research/_coverage.md` records task-specific dimensions and coverage judgments; `_connections.md`, `_open-questions.md` and `_organization-log.md` retain cross-note patterns, contradictions and maintenance history. These are natural-language coordination material with structured tables/links, not model weights. The index is derived from filenames, headings and metadata; the coverage ledger is model-authored judgment. Direct model reads can use these files even though hub enumeration excludes underscore-prefixed basenames and index files. They differ from ordinary [MEM-OBJ-notes](#mem-obj-notes) in reader and indexing treatment; no supplied runtime counterpart was found after comparison with [RT-OBJ-attempt](runtime.md#rt-obj-attempt) and [RT-BAP-generated-instructions](runtime.md#rt-bap-generated-instructions).

Source: SRC-1, `coral/template/skills/deep-research/SKILL.md`, `coral/template/skills/organize-files/scripts/generate_index.py`, `coral/hub/notes.py`.

> If it doesn't exist, create it with every dimension `missing`; if it does, read it first and target the gaps rather than re-covering what's done:
> --- `coral/template/skills/deep-research/SKILL.md`

#### MEM-OBJ-skills
Label: Shared mutable skills and executable resources

Each island's `skills/<name>/SKILL.md` contains natural-language guidance with symbolic name/description/creator metadata. Optional Python/shell scripts are symbolic executable capability, not merely prose memory. References/assets are separately loaded files. Initial bundled skills are static shipped guidance; later agent edits or new skills can retain experience for later invocation. Project setup copies bundled skills only when absent, but user-configured skill directories replace an existing same-name directory. Generic configured paths do not establish human authorship or per-content approval.

Source: SRC-1, `coral/workspace/project.py`, `coral/hub/skills.py`, `coral/template/skills/skill-creator/SKILL.md`. Distinct from [RT-OBJ-task-config](runtime.md#rt-obj-task-config): a config selects seeds; the seeded/evolved content is another artifact. Related launch authority remains [RT-BAP-generated-instructions](runtime.md#rt-bap-generated-instructions).

> if dst.exists():
>     shutil.rmtree(dst)
> shutil.copytree(src, dst)
> --- `coral/workspace/project.py`

The skill-creator prescribes trace/diff analysis, draft → paired tests → grading → revision → trigger-description optimization → packaging. It supplies a model-directed procedure, not an implemented autonomous optimizer service. Its references to `scripts.aggregate_benchmark`, `scripts.run_loop` and `scripts.package_skill` are not backed by a bundled `scripts/` directory in the inspected skill inventory. An external installation could supply them; the frozen package alone does not establish a runnable end-to-end loop.

#### MEM-OBJ-roles
Label: Evolving agent role descriptions

`roles/<agent_id>.md` is a natural-language self-description with symbolic generation/revision metadata and artifact citations. Setup seeds generation zero or a supplied file, preserving an existing file. The reflect instruction asks the owner to revise only after meaningful change and preserve history. Other agents and consolidation are instructed to read roles for complementary posture/lane selection. Only-own-file authorship is prompt policy, not an access-control conclusion. Initial seed authority and subsequent model revision are separate admission mechanisms.

Source: SRC-1, `coral/workspace/project.py`, `coral/hub/prompts/reflect.md`, `coral/template/coral.md.template`. Distinct retained content from the launch and delegation processes in [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch) and [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation).

> if dst.exists():
>     return dst
> --- `coral/workspace/project.py`

> Keep the prior History entries — drift visibility is the point.
> --- `coral/hub/prompts/reflect.md`

#### MEM-OBJ-checkpoint
Label: Shared-state checkpoint repository

A local Git repository under each shared root retains symbolic snapshots and patches of the files present at checkpoint time. Submission stores its hash and parent shared-state hash in [RT-OBJ-attempt](runtime.md#rt-obj-attempt); history and diff commands expose messages/patches to later callers. This is a distinct repository artifact, not a duplicate attempt or a model-generated summary. Whole-root staging can include others' current edits; agent name in a checkpoint message does not establish sole authorship. Unchanged state returns no new hash; failure also returns `None`, so lineage can be incomplete. No knowledge-quality check runs here.

Source: SRC-1, `coral/hub/checkpoint.py`, `coral/hooks/post_commit.py`, `coral/cli/query.py`.

> Acquires a file lock for concurrency safety. Never raises — logs warnings.
> --- `coral/hub/checkpoint.py`

> if result.returncode == 0:
>     return None  # nothing to commit
> --- `coral/hub/checkpoint.py`

#### MEM-OBJ-migration-arrival
Label: Migration arrival announcement

Part of: [RT-RTE-island-migration](runtime.md#rt-rte-island-migration)

This object is the retained output part of the supplied route. Manager code writes Markdown under destination `notes/migrations/`, with `creator: coral`, date, agent identity, source island and recent-best score rendered as prose. It is an automatic derived coordination summary from migration state, not a full explanation of why a technique succeeded. Later note lists/dashboard readers can see it; it is not guaranteed to be read by a model. Source: SRC-1, `coral/agent/manager.py`.

> surfaces in ``coral notes --recent`` without polluting the
> ``notes_by`` author lookups, which the framework uses to attribute
> work back to specific agents.
> --- `coral/agent/manager.py`

#### MEM-OBJ-session-state
Label: Session pointers and opaque conversation payload

The manager's `public/sessions.json` maps agent IDs to saved session IDs. These are symbolic access metadata, not the conversation itself or its readable summary. Manager lookup also considers `public/sessions/` and local Claude project session JSONL files. External harnesses own payload creation, replay and any compression. Raw adapter logs may expose turns, but are not thereby a derived knowledge artifact. Exact effective context on host resume is uninspected. This is distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt) and annotates, rather than duplicates, the recovery route [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering).

Source: SRC-1, `coral/agent/manager.py`; supplied route supports recovery behavior. No inference about host summary correctness or model-visible transcript completeness follows from storing an ID.

### Routes

#### MEM-RTE-knowledge-revision
Label: Prompt-directed knowledge and skill revision

Finalized results or new research → foreground/specialist model reads evidence → writes notes, role updates or skills → later agent reads retained output. CORAL's heartbeat delivery is already [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback); this route is the distinct requested content-transformation work, not another declaration of the interrupt/relaunch route. Warm-start is an alternative producer: its main-phase prompt explicitly points back to research notes. Sources: SRC-1, `coral/hub/prompts/reflect.md`, `coral/hub/prompts/consolidate.md`, `coral/template/skills/create-notes/SKILL.md`, `coral/template/skills/deep-research/SKILL.md`, `coral/template/skills/skill-creator/SKILL.md`, `coral/agent/warmstart.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: requested note/skill/role files, optional reviewer sidecar or specialist summary; actual production is not checked by the outer heartbeat route.
- Later read-back: orientation/planning requests index, relevant notes, roles and available skills; warm-start main prompt asks for prior research before coding.
- Delegated visibility: shared-file side effects are island-visible; external host owns specialist inputs and summary transport.
- Selection predicate: model judges relevant results, mechanisms, surprises and reusable patterns; consolidate requests synthesis of three or more related notes; role revision depends on meaningful shift.
- Invalidation or expiry: model may refute/supersede notes, mark sources for reverification, revise skills, or remove stale focus notes; no universal automatic content expiry is established.
- Activation or effect: retained text can shape subsequent model decisions; scripts can shape tool execution when invoked. No observed dependence or benefit is established.
- Evidence limits: prescribed workflow does not prove completed transformation, semantic checking, or independent oracle quality; helper-module gaps limit the skill optimization recipe.

Admission is model judgment plus ordinary file writes, not mandatory human approval or a score gate for knowledge. Starting a run is not approval of every note or script. Lint/review are advisory or host-mediated; rejection and recovery are requested revision, supersession, preserved originals/history and checkpoints. The task grader is an outcome/reference signal, not an oracle for a causal explanation in a note. The mode combines open research, metric-driven experiments and requested bounded skill tests.

> Read the skill, then write the note. The skill covers the mechanics; this
> prompt is just the trigger.
> --- `coral/hub/prompts/reflect.md`

> Before you cite another agent's "this is the floor" synthesis as a reason to stop, ask: did they actually try the structural ideas they themselves listed as untested?
> --- `coral/template/coral.md.template`

The requested raw-result → explanation → later-planning chain preserves reasons in mechanism, failures, references and counter-evidence sections. Skill extraction can preserve procedural guidance and source evidence, but actual reason retention is content-dependent. This supports an afforded trace-fed update path, not demonstrated improved future capacity. Templates request formulated claims and criticism; no instantiated runtime theory or successful theory-building episode was inspected. For this afforded route, theory-builder conditions 1–4 each remain operation conclusion status: uninspected: no produced whole theory, dependence on its content, attributable content-directed criticism, or retained criticism shaping another round was observed. Addressable sections and file-level revision are available; their actual granularity depends on generated content. Persistence can span iterations and resumed sessions on one task; cross-problem use is not established. Reflection is requested through role self-representation and result analysis, but its exercised causal loop, autonomous completion, learning benefit and self-improvement attribution remain unestablished independently.

#### MEM-RTE-knowledge-query
Label: Requested knowledge selection and delivery

CLI caller → note/skill hub reader → stdout; dashboard request → API reader → JSON; foreground model → filesystem index/path → file-tool content. These requested read paths are distinct from the score-triggered automatic feedback selector in [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback). Source: SRC-1, `coral/cli/query.py`, `coral/hub/notes.py`, `coral/hub/skills.py`, `coral/web/api.py`, `coral/template/coral.md.template`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: note listing titles/date/creator, selected body, concatenated bodies, skill text/file names, or API JSON; not a universal full-payload retrieval.
- Later read-back: a later agent/caller invocation can retrieve files accumulated by previous experiments/research; operator/dashboard requests expose the same retained island material through projections.
- Delegated visibility: worktree CLI discovery scopes to its island; outside callers may aggregate islands. Notes raw captures require API opt-in or direct file access. Listing is not a model-context broadcast.
- Selection predicate: literal case-insensitive substring over note title/body; optional exact normalized status; recent by parsed creation date then mtime; numeric read by current list position; skill exact-directory/prefix matching. Model-driven index/path selection is judgment, not code-ranked semantic search.
- Invalidation or expiry: files are reread; numeric positions can change with sorting/content; graph/list projections omit some files; replacement/removal affects future reads. Status/supersession do not automatically hide notes without an explicit applicable filter.
- Activation or effect: selected text is printed/returned for caller interpretation; no trace proves that an agent acted on it.
- Evidence limits: external tool truncation/token limits and actual host ingestion are uninspected; there is no inspected common token-budget allocator for these paths.

The CLI's nonnumeric `--read` argument does not resolve a named note: it prints all collected note bodies. Numeric `--read` does not forward the requested status filter. Search/recent normally print discovery summaries, not bodies. Thus a filtered list position is not a reliable filtered-body addressing contract. Dashboard notes include bodies and metadata; graph nodes are summaries plus typed edges, not the complete note or a truth verifier. Skill listing deduplicates same names by first sorted island, CLI read can reject ambiguous multiple paths, and API detail returns the first matching island directory. These differences prevent a claim of uniform cross-island access.

> except ValueError:
>     print(read_all_notes(str(coral_dir), island_id=island_id))
> --- `coral/cli/query.py`

> full_text = f"{entry['title']} {entry['body']}".lower()
> if query_lower in full_text:
>     results.append(entry)
> --- `coral/hub/notes.py`

#### MEM-RTE-note-maintenance
Label: Note reorganization and lineage maintenance

Model/librarian request → audit and duplicate candidates → model/judge decision → merge/archive or move → generated index and link edits → later readers. Distinct from [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation): that is delegation transport; this route covers mutable retained artifacts and maintenance helpers. Source: SRC-1, `coral/template/skills/organize-files/SKILL.md`, `coral/template/skills/organize-files/scripts/move_note.py`, `coral/template/skills/organize-files/scripts/generate_index.py`, `coral/template/skills/organize-files/scripts/resolve_links.py`, `coral/hub/notes.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: changed file paths/content, index, requested audit-log entry and specialist summary; helper code is wired when explicitly invoked, but the end-to-end workflow is model-mediated.
- Later read-back: orientation uses regenerated index; direct note reads and hub/API enumeration see modified or archived content according to different predicates.
- Delegated visibility: librarian can change shared files; judge is instructed to return verdicts. Actual isolated host frames and inherited inputs are uninspected.
- Selection predicate: model decides organization is needed; skill scopes restructuring to research/experiments and asks not to merge contradictions; move helper checks source, destination and file age unless forced; index uses directory/filename exclusions.
- Invalidation or expiry: proposed duplicate originals move to `_archive/`; contradictions stay separate with warning metadata; path rewrites and regeneration alter discovery, not every consumer's eligibility.
- Activation or effect: scripts can move files and derive navigation; model determines semantic merges. Neither correct deduplication nor preservation of all structured lineage is demonstrated.
- Evidence limits: helper internals are partly inspected; direct writes bypass helper checks; successful writes do not establish concurrent safety or semantic equivalence.

Model judgment proposes and admits semantic edits; software move checks can veto a helper call but not arbitrary edits. No mandatory human gate or independent truth oracle is established. Recovery guidance keeps originals and an audit trail; checkpoints may provide older bytes but do not automatically restore them. The move helper writes and verifies destination before deleting source. However, it parses frontmatter as flat colon-delimited lines and serializes a flat mapping, so nested/list YAML provenance cannot be assumed preserved by this helper. The index writer uses a temporary file and replacement; that prevents a partially written index, not lost-update races among agents.

> Move originals to `_archive/` so the merge is reversible.
> --- `coral/template/skills/organize-files/SKILL.md`

> SKIP_DIRS = {"raw", "_synthesis", "_archive"}
> --- `coral/template/skills/organize-files/scripts/generate_index.py`

In contrast, the hub walker prunes only top-level raw and underscore-prefixed **filenames**, not `_archive/` directories. Archived ordinary Markdown filenames can therefore remain in CLI lists, searches and concatenated reads. The generated index also includes unknown categories despite skill prose saying only research and experiments. Link resolution loads only notes with a frontmatter `title`, whereas the main hub reader can derive a title from a body heading. Not every readable note is automatically cross-linked.

### Claims

#### MEM-CLM-grounding-gate
Label: Grounding and structured trace are not truth gates

The source claims structured trace enables filtering, relating and verification, and deep-research requests a reviewer pass before high confidence. Inspected machinery supports link/provenance checks and projections, not independent semantic verification of each claim. `check_grounding.py` checks only the existence of a sibling review file for high-confidence notes; it does not inspect the verdict. The note linter tests the supplied `evidence.verified` flag rather than re-running the referenced attempt. Both tools normally exit zero with findings and require explicit `--strict` for failure. Consumers can still read these files. Source: SRC-1, `coral/hub/notes.py`, `coral/template/skills/deep-research/SKILL.md`, `coral/template/skills/deep-research/scripts/check_grounding.py`, `coral/template/skills/create-notes/scripts/lint.py`. Related, but not a duplicate, to grader limitations in [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution): note validation is a different consumer and oracle.

> review = note.with_suffix(".review.json")
> if not review.exists():
> --- `coral/template/skills/deep-research/scripts/check_grounding.py`

> return 1 if (args.strict and hard_total) else 0
> --- `coral/template/skills/deep-research/scripts/check_grounding.py:358-358`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-guidance
Label: Retained knowledge to later agent guidance

Consumer: later foreground coding model, librarian/researcher or other specialist, and human/operator reader. Channel: explicitly requested CLI stdout, file reads, or knowledge API; later invocation of retained executable resources is a separate symbolic effect. Force: advisory natural-language interpretation for note/role/skill bodies, executable behavior for invoked scripts, fixed filtering/projection rules for metadata. Horizon: subsequent rounds and resumed sessions while shared files persist; migration changes file neighborhood. This is distinct from [RT-BAP-generated-instructions](runtime.md#rt-bap-generated-instructions): static/generated instructions direct a reader to mutable retained artifacts; this path is those artifacts' downstream authority. Source: SRC-1, `coral/template/coral.md.template`, `coral/cli/query.py`, `coral/hub/notes.py`, `coral/hub/skills.py`.

> 7. Read notes: Start with `{shared_dir}/notes/index.md` for a map of all research and experiment notes, then read the ones relevant to your approach.
> --- `coral/template/coral.md.template`

## Annotations

#### On [RT-OBJ-attempt](runtime.md#rt-obj-attempt)

Storage is filesystem JSON plus candidate Git objects; score/status/budget/checkpoint links are symbolic, while title/feedback become natural-language evidence when an agent reads them. Submission identity and daemon outcomes are raw experiment records relative to later explanatory notes. A checkpoint snapshots state before grading; the interpretation written after feedback is not guaranteed to be in that attempt's checkpoint. Manager-selected feedback is a derived display of result fields, not a full historical transcript. Source: SRC-1, `coral/hooks/post_commit.py`, `coral/hub/checkpoint.py`; supporting passage and feedback consumer in [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission) and [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback).

#### On [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering)

Discarded attempt JSON remains on disk but `read_attempts` removes archived records from views; explicit hash reading can still recover them. This is symbolic access-state withdrawal rather than physical erasure. Notes or sessions that relied on discarded results are not automatically retracted by that filtering. Checkpoint history/diff can expose prior knowledge bytes, but the inspected checkpoint API does not supply a restore operation and the supplied route does not establish atomic knowledge restoration. Source: SRC-1, `coral/hub/attempts.py`, `coral/hub/checkpoint.py`.

> return [a for a in attempts if not a.archived]
> --- `coral/hub/attempts.py`

#### On [RT-RTE-island-migration](runtime.md#rt-rte-island-migration)

Read-back targeting changes when links repoint to destination files. Roles/cadence/attempt lineage follow identity; note/skill stores stay source-local. The manager's automatic arrival summary is described by [MEM-OBJ-migration-arrival](#mem-obj-migration-arrival). Same-session recovery can preserve knowledge from the source neighborhood even while future file reads target destination; this is not a clean context reset. Source: SRC-1, `coral/agent/manager.py`, `coral/workspace/worktree.py`; move/relaunch evidence remains in the supplied route.

#### On [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation)

The requested working-context mechanism resembles a separate frame: selected inputs enter, a concise summary returns, and detailed research/organization need not fill the foreground window. The analogy breaks because direct shared-file edits escape as well as the return value. Host frame creation, preferential exclusion of tool results, summary size, eviction and reload policies are uninspected. Plain files remain reloadable through [MEM-RTE-knowledge-query](#mem-rte-knowledge-query), but no source proves what detailed turns the host leaves in either model window. Source: SRC-1, `coral/template/skills/organize-files/SKILL.md`, `coral/template/skills/deep-research/SKILL.md`; supplied librarian passage establishes the requested summary, not actual isolation.

## Write side

The principal admission mechanisms are distinct:

- **Initialization:** configuration selects external skill seeds and optional role files. Software copies them; same-name user skills replace existing directories, whereas an existing role survives. Bundled guidance is not learned merely because copied ([MEM-OBJ-skills](#mem-obj-skills), [MEM-OBJ-roles](#mem-obj-roles)).
- **Model-authored revision:** experiment results, source captures, own transcript and sibling notes can feed requested notes/skills/role updates. The model chooses the claim or procedure and writes files. Human approval of each item is not established. Optional reviewer outputs and lint flags do not create a universal admission gate ([MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision), [MEM-CLM-grounding-gate](#mem-clm-grounding-gate)).
- **Mechanical maintenance:** helpers stamp/check/move/index/link content; the model still chooses semantic synthesis and duplicate adjudication. Metadata rewrite and visibility inconsistencies prevent assuming lossless curation ([MEM-RTE-note-maintenance](#mem-rte-note-maintenance)).
- **Automatic retention and summaries:** evaluation preserves an attempt and shared-state checkpoint; migration writes an arrival announcement derived from identity/score/move state. The latter can guide later coordination, but it is not an automatic distilled experimental technique ([RT-OBJ-attempt](runtime.md#rt-obj-attempt), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-OBJ-migration-arrival](#mem-obj-migration-arrival)).
- **Rejection/withdrawal:** queue/grader failure belongs to the supplied eval routes; it does not delete the candidate or invalidate related notes. Attempt archival excludes default active views but preserves direct-hash access. Note supersession/refutation flags do not enforce withdrawal; `_archive/` visibility differs by reader. Source invalidation guidance asks for reverification/superseded markers before rewriting or deleting ([RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission), [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution), [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering), [MEM-RTE-note-maintenance](#mem-rte-note-maintenance)).

For trace-fed knowledge, the actual chain is result/log/source → requested interpretation → retained Markdown or skill → later explicitly requested read. Mechanism explanations and discarded alternatives are prescribed; they are not guaranteed products of a checkpoint or score. Raw conversation recovery is an alternative checkpoint form, not proven semantic compaction. No inspected CORAL path establishes host summarization, preferential turn trimming or a fixed verbatim tail. Those unknowns do not negate known model-directed synthesis and file persistence.

## Read-back

The later consumer must be named at each edge. An agent's orientation/planning instruction points it to the index, roles, notes, attempts and skills. Its own file/CLI requests determine what actually enters context. CLI search/recent yields summaries; body requests can return one note or unbounded concatenation, and API projections have different payloads. These are request-driven routes with identifier/literal/status/date selection, not automatic unsolicited semantic recall ([MEM-RTE-knowledge-query](#mem-rte-knowledge-query)).

The independent push route is manager feedback: a finalized-attempt event and heartbeat configuration select one result header/feedback plus action prompts, delivered through interrupt/resume to the committing agent. Its budget is a selected result and selected prompt bodies, not a documented token allowance. Full notes/skills are not automatically embedded by this selector; consolidation and reflection request later reads. Batching and session fallback limits remain as stated in [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback).

Warm-start's main-phase pointer is explicit, but does not prove which research notes were read. Session recovery can restore opaque historical context as well as pointers; fallback fresh launch can reread durable artifacts without restoring all former turns. Skill-creator's progressive-disclosure description requests metadata first, skill body on triggering and references on demand; host implementation, always-in-context coverage and budget enforcement are uninspected ([MEM-OBJ-session-state](#mem-obj-session-state), [MEM-OBJ-skills](#mem-obj-skills), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision)).

## Integration issues

1. **No supplied runtime fact requires correction from this inspection.** Runtime's qualified claims about knowledge updates, migration and non-atomic rewind remain supported. New content-level corrections concern source-native instructions, not a contradiction of the baseline.
2. **No duplicate declaration is proposed.** [MEM-OBJ-migration-arrival](#mem-obj-migration-arrival) explicitly identifies an output part of [RT-RTE-island-migration](runtime.md#rt-rte-island-migration). Other overlaps are annotations on attempts/recovery/migration/delegation or explicitly distinct mutable content versus transport. Reconciliation should not merge [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision) into [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback): delivery is wired, completion of synthesis is afforded.
3. **Withdrawal semantics conflict across readers.** `_archive/` is index-excluded but hub-visible; superseded/refuted notes remain eligible absent explicit selection. This prevents interpreting archival or metadata as uniform epistemic retirement ([MEM-RTE-note-maintenance](#mem-rte-note-maintenance), [MEM-RTE-knowledge-query](#mem-rte-knowledge-query)).
4. **Source-native verification language overstates enforced checking.** Review-file existence and a supplied verified flag are not verdict inspection or independent truth tests. Strict-mode diagnostics still do not prohibit subsequent reads ([MEM-CLM-grounding-gate](#mem-clm-grounding-gate)).
5. **Skill optimizer dependency resolution is unresolved.** The frozen skill directory lacks several prescribed helper modules. External availability and successful execution cannot be inferred; retain a requested optimization workflow, not an implemented autonomous optimization engine ([MEM-OBJ-skills](#mem-obj-skills), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision)).
6. **Maintenance can alter lineage representation.** Flat frontmatter serialization prevents a claim that move helpers preserve arbitrary nested trace metadata. Index scope and resolver title requirements differ from prose expectations; broader automatic cross-link coverage is unsupported ([MEM-RTE-note-maintenance](#mem-rte-note-maintenance)).
7. **Query/UI/context unknowns remain local.** Named-note CLI help is misleading, status-filtered numeric reads can disagree with the filtered listing, and frontend fidelity/adapter parity are uninspected. Host session replay and specialist context budgets are opaque. These prevent claims of uniform retrieval, bounded context or clean island knowledge isolation, not the established file/query routes ([MEM-RTE-knowledge-query](#mem-rte-knowledge-query), [MEM-OBJ-session-state](#mem-obj-session-state), [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation)).

## Limitations and checks

Frozen checkout HEAD was rechecked as `0123dfb939b35228cf2c1fde224cd0561e727408`; Git status was clean. Supplied run ID, source identity and reviewed boundary were retained exactly. The job instruction, member/input types, collection, worker rules, complete supplied inputs and records contract were read; no other run or prior analysis was used. Read-only source inspection did not execute the target or its helpers. Evidence is implementation and doctrine/design only. There are no observations of learned behavior, actual theory criticism, autonomous maintenance completion, or causal improvement. Uninspected source surfaces are named in the coverage table rather than described as absent.

Validation: `commonplace-run validate-output` passed for this invocation after disambiguating the grounding-check exit quotation. The check establishes form and quotation occurrence, not semantic correctness or acceptance.
