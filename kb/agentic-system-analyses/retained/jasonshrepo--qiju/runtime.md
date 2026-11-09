---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Qiju runtime baseline: explicit capture, filtered retrieval, host review and installed-skill admission at the frozen revision."
run-id: AAS-2026-11-08-qiju-1a12c31c13d1-01
reviewed-boundary: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
---

# Qiju runtime report

## Runtime account

### Boundary and ordinary work

Qiju's consequential work is to preserve intentionally authored coding-session records and return selected history to an external coding agent. It ships a deterministic Python CLI and natural-language host skills, not an enclosing model execution loop. The entry point is `qiju.cli:main` in SRC-1, `pyproject.toml`; `src/qiju/cli.py` parses commands and calls the corresponding implementation. The complete entry surface is `init`, `log`, `temp-entry`, `search`, `show`, `redact`, `maintain`, `update`, `uninstall`, `migrate` and `projects`. `projects` lists stored project names; it does not consume a model. SRC-1, `docs/host-integration.md`, explicitly locates orchestration outside Qiju:

> Qiju is not an agent framework and does not orchestrate hosts.
> --- `docs/host-integration.md`

An ordinary shipped invocation begins after `qiju init --host <host>` installs the three skills and creates the project marker. A user requests a checkpoint or invokes the log skill. The host model owns interpretation of the request, scope, narrative and tool choices. Its context includes the session and skill; Qiju neither acquires that context nor verifies the narrative against code. The skill requests a workspace-local empty staging file, a Read, a Write of JSON, then `qiju log --source manual --agent <host> --body <literal-path> --cleanup`. The `manual` source label is not proof of human authorship: this is the model-authored shipped path. The CLI reads one JSON object, resolves project identity, normalizes metadata, repairs malformed/missing timestamps, redacts selected fields, validates shape, allocates or accepts an ID, and appends missing copies under a user-home lock. It prints the ID and attempts guarded staging deletion. See [RT-RTE-record-capture](#rt-rte-record-capture).

On a later history question, the host chooses a scope and query, invokes search, inspects candidates and requests an exact-ID show. The result returns to the host through tool output; the host owns subsequent answer or action. Keyword matching is deterministic OR matching, not model relevance ranking. The skill's two-phase procedure is optional at the executable boundary: default search returns full records, and show can be called directly. Summary/IDs/field projection can keep bodies out of a model window until hydration, but Qiju neither trims the host's accumulated turns nor creates isolated sub-agent frames. See [RT-RTE-record-retrieval](#rt-rte-record-retrieval).

All findings here are implementation or doctrine/design findings from SRC-1. No supplied run trace, actual store or comparison experiment demonstrates activation, reliable host compliance, effectiveness, privacy completeness or benefit. Operation conclusion status is therefore uninspected, not absent. Additional inspected coverage beyond the boundary's initial survey includes full `src/qiju/schema.py`, `src/qiju/redact.py`, `src/qiju/allowlist.py`, both shipped JSON redaction configurations, `src/qiju/staging.py`, `src/qiju/paths.py`, `src/qiju/id_gen.py`, `src/qiju/util.py`, `src/qiju/archive.py`, `src/qiju/retro_redact.py`, `src/qiju/update_cmd.py`, the remaining installer branches, and the migration/cleanup passages cited below. These add implementation evidence at the same frozen revision, not new sources. Detailed record storage, curation and memory revisions belong to the memory member.

### Principals, capability and enforcement

The user can request capture, retrieval or review and can authorize proposed skill edits. The host model interprets natural-language instructions. Qiju code executes filesystem operations under the caller's OS authority. Host identity is an argument/environment label, not an authenticated principal; optional `model` and `model_effort` are strings, not provider selection. External host model weights, version pinning and endpoint mutability are uninspected; Qiju does not instantiate a distributed-parametric component in the inspected CLI routes. [RT-CMP-host-model](#rt-cmp-host-model) separates this dependency from Qiju's symbolic CLI.

The capability surface includes reading arbitrary caller-specified body files or stdin, writing local/global records, cross-project search, rewriting records, installing/replacing skills and explicit durable-store purge. The current grant set and deployed isolation envelope are unknown: no host permission configuration or deployed filesystem authority was supplied. Qiju's project scope is a selection/routing rule, not an access-control boundary. `QIJU_HOME`, `QIJU_PROJECT_ROOT`, explicit scope and filesystem permissions affect reach. The Git subprocess in `src/qiju/paths.py` only discovers the top-level directory. The inspected paths provide no Qiju model-tool dispatch, worker delegation, provider-native tool or remote execution route; this is a bounded account of these files, not an assertion about external host capabilities.

### Load-bearing controls and forcing cases

1. **Canonical capture identity.** The owner is `capture.log_entry`; its enforcement point compares a normalized explicit project with a valid authoritative marker before directory creation. Strength: invariant within that function when the marker exists. Implementation conclusion status: wired. Operation conclusion status: uninspected. Covered paths: CLI body/stdin and direct calls to `log_entry`. Alternate paths: environment-root selection, markerless explicit projects and Git-root fallback are deliberately allowed; search, init and migration have different responsibilities. `nearest_marker_slug` respects `QIJU_PROJECT_ROOT` even if it names a markerless root. Thus the control prevents a conflicting explicit slug at a valid selected marker, not every cross-project write or accidental identity. It depends on a valid marker/environment and filesystem integrity. SRC-1, `src/qiju/capture.py`, `src/qiju/paths.py`; retained evidence in [RT-RTE-record-capture](#rt-rte-record-capture).

2. **Privacy before captured persistence.** The owner is `prepare_entry`/`redact_entry`; strength: best effort, not secret exclusion. Implementation conclusion status: wired. Operation conclusion status: uninspected. The redactor traverses values only in six named fields. Supported JSON may carry optional model metadata and unknown extra keys; normalization preserves them, schema validation does not reject unknown keys, and logging serializes the resulting dictionary. Explicit IDs are also accepted as arbitrary nonempty strings. Those values do not pass the six-field redactor. This is reachable through supported CLI body input, not merely an unused type possibility. Rule and entropy matches also admit allowlisted strings. Staging contains caller-authored pre-redaction JSON until cleanup, and imported legacy records take a separate route. No comprehensive privacy guarantee follows. The external host may transmit returned content to its provider, as SRC-1, `docs/redaction-and-privacy.md`, warns. Evidence is retained in [RT-RTE-record-capture](#rt-rte-record-capture), [RT-RTE-privacy-repair](#rt-rte-privacy-repair) and [RT-RTE-store-migration](#rt-rte-store-migration).

3. **ID retry and durability.** The owner is `log_entry` plus `util`; strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. Cooperating capture/maintenance/repair writers use the same home lock; append flushes and fsyncs each file. Reads do not take that lock. The short and long appends are sequential, not one transaction. A failure after the first append can leave only the short copy; retrying the same explicit ID can fill a missing tier, but a freshly generated retry need not retain that identity. Existing IDs skip existing copies rather than verify payload equality; an archived ID returns immediately. The guarantee is duplicate-ID avoidance/partial retry support, not exactly-once semantic capture, cross-file atomicity or truth verification. Filesystem and platform lock semantics are external contracts. SRC-1, `src/qiju/capture.py`, `src/qiju/id_gen.py`, `src/qiju/util.py`.

4. **Cleanup and edit permissions.** Staging cleanup owner: `staging.safe_cleanup`; strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. It checks symlink status, resolved direct-child containment, managed filename and regular-file status; stale sweeps reuse that guard. It is not an OS sandbox or a proof against concurrent path replacement. `--cleanup` with stdin or an unrelated file warns rather than deleting it; CLI success can coexist with cleanup refusal. Separately the retrospective's user-authorization rule is a natural-language policy owned by the host, not a CLI veto. Implementation conclusion status for instruction installation: wired. Operation conclusion status: uninspected. Direct `qiju update` replaces eligible installed skills without per-file approval. The review policy therefore cannot be treated as a universal change gate. See [RT-RTE-skill-review](#rt-rte-skill-review) and [RT-RTE-skill-install](#rt-rte-skill-install).

These four forcing cases challenge the ordinary path with markerless/environment routing, unguarded record fields/imports, explicit-ID retry collisions, and direct update/cleanup alternatives. No concurrent execution, filesystem fault injection, host bypass test or provider behavior was observed.

### Change and return boundaries

Record admission is schema/redaction code, not a content-approval queue or answer oracle. Retention maintenance is threshold-controlled code, not model revision. Retroactive literal scrub and project migration admit user/caller-selected transformations without factual judgment. The retrospective is a separate open-ended model procedure over recent records: it diagnoses mistakes and proposes edits, but asks for explicit user permission before applying them. It does not execute a benchmark or automatically promote a winning candidate. Installed skill changes from init/update are package-body replacements; they are not produced from the retrospective's findings. See the admission fields in the route records below.

## Shared records

### Components

#### RT-CMP-host-model
Label: External host model

Identity: the model of Claude Code, Codex, Kiro or Cursor interpreting installed skills, not a Qiju-owned endpoint. Representational form: distributed-parametric. Storage substrate: external provider or host model machinery, uninspected. SRC-1, `docs/host-integration.md`, `src/qiju/init_cmd.py`, establish the host interface; they do not expose provider internals. Parameter changes during operation: uninspected. Exact version pinning: uninspected. Mutable endpoint resolving to another model: uninspected. Record fields named `model` and `model_effort` describe claimed session metadata; they do not pin this component or mutate weights.

> - `model`: the exact model identifier, only when it is authoritative for this
>      session; omit it when unknown.
> --- `src/qiju/init_cmd.py`

### Operative objects

#### RT-OBJ-qiju-skills
Label: Installed Qiju skills

Identity: generated `qiju-log`, `qiju-search` and `qiju-review` SKILL.md bodies. Representational form: natural-language operating instructions consumed by the external host model; YAML skill metadata is symbolic discovery input. Storage substrate: project `.claude/skills`, `.agents/skills`, `.kiro/skills` or `.cursor/skills`, or corresponding user-level locations, with additional global copies under Qiju home `agents`. Lineage: embedded constants and renderer in SRC-1, `src/qiju/init_cmd.py`. The model receives these only if its host discovers/loads them; discovery and compliance are not demonstrated. These are shipped instruction artifacts, distinct from use-written record content left for the memory analyst.

> return f"---\nname: {name}\ndescription: {description}\n---\n\n{body.strip()}\n"
> --- `src/qiju/init_cmd.py`

### Routes

#### RT-RTE-record-capture
Label: Intentional record capture

Endpoints/progression: user request → host skill interpretation → temp-entry/Read/Write → log → project short and user long stores → printed ID. Owner: host for composition and calls, code for identity, redaction, schema and I/O. State is the supplied JSON plus resolved project and session identity; symbolic schema/branch rules transform it, while narrative construction is natural-language model work. SRC-1, `src/qiju/init_cmd.py`, `src/qiju/cli.py`, `src/qiju/capture.py`, `src/qiju/schema.py`, `src/qiju/id_gen.py`, `src/qiju/staging.py`, `src/qiju/util.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: log prints the record ID; ordinary host procedure reports it to the user. Error handling emits stderr and failure for handled parse/schema/I/O errors.
- Later read-back: persisted entries can be selected by search and hydrated by show in later host invocations.
- Delegated visibility: inapplicable — no Qiju child worker is launched; cross-host access is shared local storage, not delegated context.
- Selection predicate: explicit save/checkpoint request in the skill; CLI also accepts direct body/stdin invocations with source manual or agent.
- Invalidation or expiry: staging can be deleted after success or by stale sweep; retained record movement is maintenance, not automatic content expiry.
- Activation or effect: code appends absent copies by ID; downstream host behavior from a record remains unobserved.
- Evidence limits: source establishes executable admission and installed requests, not narrative verification, actual capture, exactly-once delivery or comprehensive secret removal.

Admission: the host/caller proposes JSON; code can reject malformed shapes, marker conflicts and invalid metadata. No human per-record review is wired. A user trigger supplies scope, not approval of every sentence. Open-request operating mode; no expected-answer oracle. Guidance asks for anchors, explicit decision status and rationale, excludes unagreed suggestions from next steps, and warns against sensitive data. What persists is the normalized/redacted record, not the raw session unless deliberately included. Recovery includes preserved staging on failed log and explicit-ID filling of missing tiers; no multi-file rollback is implemented here.

> entry = schema.normalize_entry(raw)
> --- `src/qiju/capture.py`

> normalized = dict(entry)
> --- `src/qiju/schema.py`

> for field in ("agent", "title", "tags", "search_terms", "next_steps", "body_md"):
> --- `src/qiju/redact.py`

The latter is the exact redaction field boundary. Optional model fields and arbitrary extras survive the dictionary copy and serialization without that traversal.

> if "archive" in locations:
>             return entry_id
>         if "short" not in locations:
>             util.append_jsonl(qiju_paths.short_jsonl, entry)
>         if "long" not in locations:
>             util.append_jsonl(qiju_paths.long_jsonl, entry)
> --- `src/qiju/capture.py`

> if explicit_project != marker_project:
>             raise ValueError(
> --- `src/qiju/capture.py`

The marker comparison does not run when no valid authoritative marker exists. The staging deletion control returns a refusal reason without undoing capture:

> if not deleted and reason:
>                 print(f"qiju log: --cleanup skipped: {reason}", file=sys.stderr)
> --- `src/qiju/cli.py`

#### RT-RTE-record-retrieval
Label: Search and hydrate records

Endpoints/progression: history question → host-selected search arguments → merge short/long/archive → ID deduplication, predicates, sort and limit → renderer → optional exact-ID show → external host reasoning. Code owns selection mechanics; host owns query planning, candidate choice and final answer. SRC-1, `src/qiju/search.py`, `src/qiju/storage.py`, `src/qiju/archive.py`, `src/qiju/cli.py`, `src/qiju/init_cmd.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: search renders JSON by default, or JSONL/summary/table/actions; show returns one projected or full record, or reports not found.
- Later read-back: search/show are the later-consumer routes for previously captured/imported records; they do not write new memory themselves.
- Delegated visibility: inapplicable — output crosses the CLI/host tool boundary, not a Qiju delegation boundary.
- Selection predicate: current project by default, all or comma-separated named scope; optional exact metadata/source, session prefix, all required tags, inclusive parsed date bounds, case-insensitive OR keywords or regex; sorting and limit apply before rendering. IDs-only reduces records to id/project/title.
- Invalidation or expiry: inapplicable — retrieval imposes query filters, not retention expiry; deleted/rewritten data changes later results.
- Activation or effect: delivers selected text/metadata; effects on host answers/actions remain unobserved.
- Evidence limits: no semantic relevance, complete recall or stale-history correction is demonstrated; skill instructions request timestamp checks and fallback but CLI does not enforce them.

The two-phase design is host guidance, not an enforced data-minimization invariant. Explicit fields project only JSON/JSONL output; summary uses fixed fields, table its columns, and actions consumes `next_steps`. Search with default JSON and no fields returns full entries. show with no project searches all stored projects. Scope all enumerates long/archive projects, not every possible project-local short-only store. Read order is short then long then archive with first-ID wins; no payload reconciliation verifies conflicting duplicates. Queries load tiers before shaping output; a cheap manifest is a smaller output, not evidence of indexed backend performance.

> return any(re.search(re.escape(term), text, flags=re.IGNORECASE) for term in terms)
> --- `src/qiju/search.py`

> if ids_only:
>             results.append({"id": entry_id, "project": entry.get("project"), "title": entry.get("title")})
>         else:
>             results.append(entry)
> --- `src/qiju/search.py`

> scope = "all" if project is None else "current_project"
> --- `src/qiju/search.py`

Working-context control: model/user chooses output shape and hydration. The manifest or projected fields remain visible while omitted bodies stay reachable by exact ID; plain search can omit nothing. No Qiju summary replaces an accumulated host conversation. The skill's widened all-project fallback trades narrower scope for recovery of fragmented project history; this is not an authorization grant or verified relevance decision.

#### RT-RTE-skill-review
Label: Requested retrospective review

Endpoints/progression: explicit user retrospective request → external host computes seven-day bounds → project and all-project summary searches → selected show calls → model diagnoses patterns → proposed wording/report → optional user-requested targeted edits. Owner: external host model; Qiju supplies instructions and record retrieval, not a review executor. Representational form: natural-language policy over natural-language records with symbolic CLI date/selection rules. SRC-1, `src/qiju/init_cmd.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: requested concise report of mistakes, evidence, lessons, skill recommendations, do-not-change items and highest-leverage edits.
- Later read-back: uninspected — no report storage or automatic reload is wired; optional applied skill edits could be read later by the host.
- Delegated visibility: inapplicable — review uses the foreground external host; no separate reviewer context is specified.
- Selection predicate: recent project and global records; summaries suggesting mistakes, repeated fixes, prompt confusion, verification failure or skill lessons are to be hydrated.
- Invalidation or expiry: seven-day evidence window bounds the requested review, not the lifetime of applied edits; monitor is a possible recommendation.
- Activation or effect: proposals can shape user decisions; only explicitly requested follow-up asks the host to edit targeted skills. No observed application or improved behavior supplied.
- Evidence limits: installed review text is a requested procedure, not a demonstrated autonomous correction loop or causal improvement experiment.

Admission and diagnosis: the model proposes, diagnoses skill relevance and recommends add/rewrite/remove/split/keep/monitor. The user can veto by withholding the requested application; software does not enforce that veto on host file tools. Open retrospective operating mode, not a bounded test curriculum. There is no supplied expected-answer oracle: records are evidence and the model judges patterns. Guidance distinguishes recurring/high-impact issues from weak isolated signals and cautions against blaming skills for external failure. Proposed text is to be copy-ready and scoped. Applied guidance may persist in targeted skill files; rollback/recovery is not specified for these model-authored edits. This differs from package replacement/backups in [RT-RTE-skill-install](#rt-rte-skill-install).

> Do not edit any skill files unless the user explicitly asks. Produce recommendations and proposed wording only.
> --- `src/qiju/init_cmd.py`

> Do not blame a skill when the record points to missing project context, user preference, external failure, or one-off environment trouble.
> --- `src/qiju/init_cmd.py`

Theory account: this route can criticize existing guidance and propose revised method text, but arbitrary skill text and actual critiques were not supplied. What it requests retaining is recommendations or, on authorization, changed skill files; it does not implement a retained critic-report queue. Theory-builder conditions 1–4: condition 1 conclusion status: afforded — whole localized guidance and proposed replacement wording can be handled, but the content of actual reviewed theories is uninspected. Condition 2 conclusion status: claimed — instructions request review decisions based on that guidance's failings, without observed dependence. Condition 3 conclusion status: afforded — prompts ask to identify unclear/missing/counterproductive instructions and avoid misplaced blame; no actual claim-specific criticism or resulting changed reliance is supplied. Condition 4 conclusion status: uninspected — later review of applied edits is possible but neither retained criticism nor another affected round is shown. These conditions do not establish a functioning theory builder.

Addressability is at least targeted skill-file/proposed-wording granularity in the requested procedure; finer semantic units are uninspected. Persistence horizon of an applied skill could span sessions, but actual applied content and later loading are unobserved. Learning conclusion status: uninspected — no improved future capacity or attribution evidence. Reflection conclusion status: afforded — a host can use operation records to represent mistakes and revise guidance capable of affecting later host work; actual bidirectional use is not observed. Reflective theory builder conclusion status: uninspected — operation records exist architecturally, but an exercised conditions-1–4 method-text loop is not supplied. Autonomous theory builder conclusion status: uninspected — internal review is requested of a model, while application expressly requires user authorization and full internal operations are not evidenced. For self-improvement of the bounded host-plus-installed-guidance pathway, the objective is preventing repeated mistakes and unclear instructions across sessions. The route affords improvement-directed proposals; causal links from evidence to an actual admitted update, live authority and later dependent operation remain unestablished. Neither exercised nor successful self-improvement is demonstrated.

#### RT-RTE-skill-install
Label: Install or refresh skills

Endpoints/progression: caller init/update → host selection and project/root discovery → bundled skill rendering → local/global files; update discovers registered/current/optionally scanned projects and refreshes enabled hosts. Code owns admission. SRC-1, `src/qiju/init_cmd.py`, `src/qiju/update_cmd.py`, `src/qiju/cli.py`, `docs/host-integration.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: init reports hosts/files; update reports updated/unchanged/skipped/missing/failed project outcomes and warnings, optionally JSON.
- Later read-back: host skill discovery can load the replaced files in future sessions; actual discovery is external and unobserved.
- Delegated visibility: inapplicable — multiple host installations are file targets, not spawned workers.
- Selection predicate: init explicit canonical hosts/all/list or environment detection; update intersects enabled agents with requested hosts, and refreshes existing global skill installations after project processing.
- Invalidation or expiry: differing contents are replaced with timestamped backup; unchanged content is skipped. No time-based expiry.
- Activation or effect: changes installed instruction bytes and project initialization metadata, not host weights; later behavioral activation remains unobserved.
- Evidence limits: deterministic replacement establishes installation, not safety, user approval of each content unit or retention of local custom edits as active guidance.

Admission: invoking caller selects installation/update; bundled package text supplies the candidate, code compares bytes, and dry-run permits inspection before update. No model selector, answer oracle or content approval gate. Operating mode is explicit administrative maintenance. Update does not fetch or upgrade the Python package itself; the docs prescribe an external package upgrade first. Installed instructions in [RT-OBJ-qiju-skills](#rt-obj-qiju-skills) persist; timestamped prior files afford manual recovery but no automatic rollback command is specified here. Direct update is a separate admission path from retrospective application. A no-project early return precedes global refresh when no roots were found and scan was not requested, so global replacement is not guaranteed on every update invocation.

> if path.exists() and path.read_text(encoding="utf-8") == content:
>         return False
>     if path.exists():
>         shutil.copy2(path, path.with_name(f"{path.name}.bak.{_timestamp()}"))
>     path.write_text(content, encoding="utf-8")
> --- `src/qiju/init_cmd.py`

> if not deduped and not scan_projects:
>         result.warnings.append(_RECOVERY_MSG)
>         return result
> --- `src/qiju/update_cmd.py`

#### RT-RTE-store-maintenance
Label: Retention maintenance

Endpoints/progression: caller maintain → home lock → rotate current short, sweep current staging, archive selected long projects → JSON report. Owner: threshold code; context is current paths, wall clock and retained files. SRC-1, `src/qiju/maintain.py`, `src/qiju/archive.py`, `src/qiju/staging.py`, `src/qiju/util.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dry-run flag, rotation/sweep counts and archive reports; warnings go to stderr.
- Later read-back: retrieval reads surviving short, long and archived records through storage merging.
- Delegated visibility: inapplicable — one synchronous CLI operation, no delegated model context.
- Selection predicate: short older than 14 days; managed staging older than 24 hours; month groups all older than 92 days and over 2 MiB, or all older than 366 days, or all older than 31 days under a long-file size over 50 MiB. Invalid timestamps stay in their tier.
- Invalidation or expiry: removes qualifying current short copies and stale staging; archive movement removes corresponding long copies after partition write.
- Activation or effect: changes storage placement/working-set availability, not record narrative meaning by model judgment.
- Evidence limits: no executed recovery or performance result; multi-file transitions are not one transaction and external filesystem/DuckDB contracts remain necessary.

Admission/recovery: explicit caller trigger; fixed code rules propose and decide movement, dry-run suppresses content mutations. No human per-record decision, factual oracle or improvement-directed candidate selection. Parquet writing verifies row count and ID set before replacement, not field-by-field semantic equivalence. Atomic file replacements and write-archive-before-prune reduce loss risks without proving universal losslessness. Guidance is shipped thresholds; output persists as tier placement, not revised methodology.

> if validated_ids != expected_ids:
>             raise RuntimeError(f"Parquet validation failed for {parquet_tmp_path}: ID set mismatch")
>         util.replace_atomic(parquet_tmp_path, path)
> --- `src/qiju/archive.py`

#### RT-RTE-privacy-repair
Label: Literal privacy repair

Endpoints/progression: caller supplies nonblank value/reason/placeholder → redact command → home lock → current short plus all home long/archive values rewritten → redacted audit append → result. Owner: caller chooses value; recursive replacement code decides matches. SRC-1, `src/qiju/retro_redact.py`, `src/qiju/redact.py`, `src/qiju/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: event with timestamp, reason, placeholder and changed file/entry counts; errors return failure.
- Later read-back: search/show consume rewritten records; audit event is retained separately.
- Delegated visibility: inapplicable — no worker boundary; caller receives event output.
- Selection predicate: exact literal substring in recursively visited string values; nonblank required. The project option resolves current short but does not restrict all home long/archive iteration.
- Invalidation or expiry: matches are replaced rather than expired; no automatic restoration specified.
- Activation or effect: changes stored values, including more fields than write-time redaction, and appends redaction metadata.
- Evidence limits: not universal deletion of a secret: other workspaces' short files, staging, backups, transformed variants and external host copies are not covered by this traversal. Returned event is not the redacted audit copy.

Admission: explicit caller proposes literal/replacement and reason; code rejects empty/whitespace values and admits replacements without semantic review or answer oracle. Operating mode: administrative repair. No multi-file rollback; atomic per-file rewrite is the recovery unit. This is separate from regex write-time redaction and may change identifiers if their string values match. An audit is not evidence of improved privacy outcomes across the external host boundary.

> for long_path in paths_mod.all_long_files(qiju_paths.home):
> --- `src/qiju/retro_redact.py`

> redacted_event, _ = redact.redact_value(event, "redaction_log")
>         util.append_jsonl(qiju_paths.redaction_log, redacted_event)
>     return event
> --- `src/qiju/retro_redact.py`

#### RT-RTE-store-migration
Label: Explicit store migration

Endpoints/progression: caller migrate selects name normalization, retag-from or legacy Kedu copy → operation-specific transformations under home lock → files/marker or new store and report. Owner: deterministic code, caller supplies mode/source. SRC-1, `src/qiju/cli.py`, `src/qiju/migrate.py`. These are administrative alternatives, not learned record revisions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: operation report with changes, warnings or skipped reasons; CLI catches exceptions.
- Later read-back: normal search/show can consume migrated records under their resulting project/store identities.
- Delegated visibility: inapplicable — no model/delegation call.
- Selection predicate: normalization targets selected/all long and archive plus current short/marker; retag target comes only from a valid authoritative marker; legacy copy enumerates legacy long/archive/audit and optional project files, with a new-home sentinel preventing ordinary repeat migration.
- Invalidation or expiry: identity repair merges records with ID deduplication; legacy source is preserved, new-home sentinel persists. No time-based expiry.
- Activation or effect: changes record addressing and, for legacy migration, replaces KEDU/Kedu/kedu substrings throughout string values and keys; this is not byte-preserving archival capture.
- Evidence limits: no executed migration, full field-equivalence check or cross-file transaction demonstrated; normalization helper details beyond the inspected orchestrator are not assessed here.

Admission/recovery: caller invocation and dry-run; code selects fixed transformations, not model proposals or a factual oracle. Retag preflights source project identity, archive layout and readability, and performs a dry archive transformation before mutating tiers. That gate is not full schema/factual validation. Legacy copy takes JSONL/Parquet input without the capture redactor; it preserves old source as backup, merges target-first by ID and skips archive migration with a warning if DuckDB is unavailable, yet can write a sentinel. Thus neither capture's redaction coverage nor retag's fail-closed preflight extends to every migration branch. Affected content persists in new files/marker; there is no automatic multi-file rollback. Operating mode: explicit repair/import, not self-improvement.

> def _rebrand_text(value: str) -> str:
>     """Case-aware kedu->qiju rewrite for a single string."""
>     return value.replace("KEDU", "QIJU").replace("Kedu", "Qiju").replace("kedu", "qiju")
> --- `src/qiju/migrate.py`

> if not _DUCKDB_AVAILABLE:
>         warnings.append("duckdb unavailable; skipping archive (parquet) migration")
>         return
> --- `src/qiju/migrate.py`

> _preflight_retag_source_archive(archive_source, source)
>         _retag_archive_tier(resolved_home, source, target, dry_run=True)
> --- `src/qiju/migrate.py`

### Claims

#### RT-CLM-lossless-records
Label: Lossless after capture

Claimed operation: preservation of intentional records, not automatic transcript preservation. SRC-1, `docs/architecture.md`, narrows the product label:

> "Lossless" means the
> record is preserved after capture; Qiju does not preserve a raw transcript unless
> the user deliberately writes one into a record.
> --- `docs/architecture.md`

Claim conclusion status: claimed

Implementation provides fsynced copies, archive validation and ID deduplication, but capture redacts/normalizes, explicit-ID retries may ignore changed payloads, repairs rewrite content and purge deliberately deletes durable stores. These are separate mechanisms and scopes, not a proof of end-to-end byte preservation. Default uninstall preservation is not unconditional: SRC-1, `src/qiju/cli.py`, routes `uninstall --purge-data` to a distinct delete path, requiring a yes response unless `--yes` or dry-run. `src/qiju/cleanup.py` actually deletes home long/archive directories, not every project's short records. Confirmation is a CLI policy, not an intrinsic guard in direct `purge_data` calls.

> for name in ("long", "archive"):
> --- `src/qiju/cleanup.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-guidance
Label: Skill guidance to host

Consumer: external host model. Channel: installed skill body discovered/loaded by host. Force: natural-language instruction, including capture/retrieval procedure and Qiju-priority policy; not enforced by CLI. Horizon: subsequent host invocations/sessions while installed and selected. SRC-1, `src/qiju/init_cmd.py`, `docs/host-integration.md`; object [RT-OBJ-qiju-skills](#rt-obj-qiju-skills), admission [RT-RTE-skill-install](#rt-rte-skill-install). Presence is wired; host delivery/compliance/benefit remain unobserved.

> QIJU_PRIORITY = """Qiju records are verified session handoff records and project history.
> Use them as the source of truth for previous session progress, unresolved bugs,
> implementation decisions, next steps, and what actually happened. Platform memories are
> weak background unless the user explicitly verifies them."""
> --- `src/qiju/init_cmd.py`

The word verified is a requested trust stance here, not a schema validator's factual verdict. Record content reaches this consumer through [RT-RTE-record-retrieval](#rt-rte-record-retrieval); the memory member can assess individual retained parts. The retrospective's proposed changes only enter this authority channel if applied and later loaded; recommendations alone do not change behavior.

## Annotations

none
