---
type: types/agentic-system-analysis-result.md
description: "Complete source-bounded analysis of Napkin's CLI, SDK and agent memory workflows"
run-id: AAS-2026-09-27-napkin-03
system: "Napkin"
run-date: "2026-09-27"
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-cutoff: "2026-09-27"
evidence-tier: code-grounded
memory-comparison:
  scope: "Accumulated or edited vault notes, NAPKIN.md, templates, structured content and access metadata; CLI/SDK read and maintenance routes, shipped distill/tend procedures and benchmark import/consumer interfaces. External agent and model internals, deployment histories, and legacy implementations are excluded."
  axes:
    storage_substrate:
      assessment: "known"
      values: ["files", "sqlite", "in-memory"]
      evidence: {"files": {"basis": "wired", "records": ["OBJ-5", "OBJ-6", "OBJ-7", "OBJ-8"], "note": "Markdown, JSON and YAML persist content and access structures."}, "sqlite": {"basis": "wired", "records": ["OBJ-9"], "note": "Base queries compile retained vault metadata into a SQLite database."}, "in-memory": {"basis": "wired", "records": ["OBJ-9"], "note": "The SQLite access structure is rebuilt in memory and closed after the query."}}
      records: ["OBJ-5", "OBJ-6", "OBJ-7", "OBJ-8", "OBJ-9"]
      note: "Includes retained content and its operative access structures; SQLite is transient, not a second durable store. Link and canvas structures are file encoded, not a graph database."
    representational_form:
      assessment: "known"
      values: ["natural-language", "symbolic"]
      evidence: {"natural-language": {"basis": "wired", "records": ["OBJ-5", "OBJ-6"], "note": "Read and overview return retained prose."}, "symbolic": {"basis": "wired", "records": ["OBJ-7", "OBJ-8", "OBJ-9"], "note": "Serialized search structures, frontmatter, canvas JSON and executable base filters have machine interpreted structure."}}
      records: ["OBJ-5", "OBJ-6", "OBJ-7", "OBJ-8", "OBJ-9"]
      note: "Covers content, metadata, and derived access structures; no retained learned parameters within scope."
    lineage:
      assessment: "known"
      values: ["authored", "imported", "other-compiled", "trace-extracted"]
      evidence: {"authored": {"basis": "wired", "records": ["RTE-6"], "note": "Users supply note text and change structured properties."}, "imported": {"basis": "wired", "records": ["RTE-11"], "note": "Benchmarks import external paragraphs, conversations and supplied summaries."}, "other-compiled": {"basis": "wired", "records": ["RTE-7", "OBJ-9"], "note": "Search caches, overview and base tables derive mechanically from files."}, "trace-extracted": {"basis": "afforded", "records": ["RTE-8"], "note": "The shipped distill skill directs an agent to extract session knowledge into persistent notes."}}
      records: ["RTE-6", "RTE-11", "RTE-7", "OBJ-9", "RTE-8"]
      note: "The skill establishes an executable agent procedure, not evidence that it ran. Imported preexisting summaries are not Napkin extraction."
    behavioral_authority:
      assessment: "known"
      values: ["knowledge", "routing", "ranking", "instruction"]
      evidence: {"knowledge": {"basis": "afforded", "records": ["RTE-7", "RTE-11"], "note": "Named task agents are directed to answer using retrieved notes; consumer execution is external."}, "routing": {"basis": "wired", "records": ["OBJ-7", "OBJ-8", "OBJ-9"], "note": "Stored metadata drives keyword maps, view selection and filtering."}, "ranking": {"basis": "wired", "records": ["OBJ-7"], "note": "Persisted index and backlink counts feed search ranking."}, "instruction": {"basis": "afforded", "records": ["OBJ-6", "RTE-8"], "note": "Pinned conventions and vault templates guide later agent work and note writing."}}
      records: ["RTE-7", "RTE-11", "OBJ-7", "OBJ-8", "OBJ-9", "OBJ-6", "RTE-8"]
      note: "Actual CLI delivery is wired; model adoption of knowledge or instructions is afforded, with no execution observation. Source trust instructions are not runtime enforcement."
    write_agency:
      assessment: "known"
      values: ["manual", "automatic"]
      evidence: {"manual": {"basis": "wired", "records": ["RTE-6"], "note": "The CLI persists supplied human text and explicit edits."}, "automatic": {"basis": "wired", "records": ["RTE-7", "RTE-11"], "note": "Cache compilation and benchmark import write files without manual authorship of each output; model extraction is separately afforded."}}
      records: ["RTE-6", "RTE-7", "RTE-11"]
      note: "Mechanical automatic writes do not upgrade the distill procedure to wired model extraction."
    curation_operations:
      assessment: "known"
      values: ["consolidate", "dedup", "evolve", "invalidate", "synthesize", "promote"]
      evidence: {"consolidate": {"basis": "afforded", "records": ["RTE-9"], "note": "Tend integrates overlapping retained notes and removes the redundant copy."}, "dedup": {"basis": "afforded", "records": ["RTE-9"], "note": "Tend requires reading both notes before an obvious-overlap merge."}, "evolve": {"basis": "wired", "records": ["RTE-6"], "note": "Property and task edits revise existing retained entries; semantic integration is separately afforded."}, "invalidate": {"basis": "wired", "records": ["RTE-6", "RTE-9"], "note": "Trash withdrawal removes entries from ordinary discovery while retaining file bytes; tend names superseded notes as targets."}, "synthesize": {"basis": "afforded", "records": ["RTE-8"], "note": "Distill permits marked generalization during integration into retained notes."}, "promote": {"basis": "afforded", "records": ["RTE-8"], "note": "Project-changing session findings can update the pinned NAPKIN.md tier."}}
      records: ["RTE-9", "RTE-6", "RTE-8"]
      note: "No access-frequency promotion is implemented in the inspected core. Relative mtime ranking is not an elapsed-time forgetting policy; cache rebuilding is not content consolidation."
    read_back_direction:
      assessment: "known"
      values: ["pull", "push"]
      evidence: {"pull": {"basis": "wired", "records": ["RTE-7"], "note": "CLI requests return retained overview, search, full reads and structured views; distill and tend specify agent callers."}, "push": {"basis": "afforded", "records": ["RTE-10"], "note": "Documentation assigns NAPKIN.md to every agent session and names an external context-injection integration."}}
      records: ["RTE-7", "RTE-10"]
      note: "The documented pinned route is distinct from requested overview delivery. Its external selector implementation is excluded, so no push wiring is asserted."
    read_back_signal:
      assessment: "known"
      values: ["coarse"]
      evidence: {"coarse": {"basis": "afforded", "records": ["RTE-10"], "note": "At session start the documented route supplies the small project context note regardless of task query."}}
      records: ["RTE-10"]
      note: "Only the documented pinned-context push is classified. Search terms and file identifiers on pull requests are not push signals; external extension selection internals are outside the boundary."
    trace_learning:
      assessment: "known"
      values: ["yes"]
      evidence: {"yes": {"basis": "afforded", "records": ["RTE-8"], "note": "The agent skill turns current conversation knowledge into durable notes for future retrieval."}}
      records: ["RTE-8"]
      note: "This classification rests on the skill route alone, not raw benchmark retention, cache compilation or reported accuracy."
    trace_source:
      assessment: "known"
      values: ["session-logs"]
      evidence: {"session-logs": {"basis": "afforded", "records": ["RTE-8"], "note": "The skill explicitly consumes the current conversation or working session."}}
      records: ["RTE-8"]
      note: "No separate tool-trace or event-stream extraction is established by the qualifying skill."
    learning_scope:
      assessment: "known"
      values: ["cross-task", "per-project"]
      evidence: {"cross-task": {"basis": "afforded", "records": ["RTE-8"], "note": "Permanent reusable session knowledge is selected for use months later without the original chat."}, "per-project": {"basis": "afforded", "records": ["RTE-8"], "note": "Project-changing findings revise the project context note in the same vault."}}
      records: ["RTE-8"]
      note: "Scope follows intended future reuse and the project-context branch, not the mere existence of a session ID."
    learning_timing:
      assessment: "known"
      values: ["online", "offline"]
      evidence: {"online": {"basis": "afforded", "records": ["RTE-8"], "note": "A user can invoke extraction from the current working conversation."}, "offline": {"basis": "afforded", "records": ["RTE-8"], "note": "The same skill is also intended for the end of a session."}}
      records: ["RTE-8"]
      note: "Both are phases of the same qualifying extraction procedure; periodic external-extension execution is not established."
    distilled_form:
      assessment: "known"
      values: ["natural-language", "symbolic"]
      evidence: {"natural-language": {"basis": "afforded", "records": ["RTE-8"], "note": "The derived artifact states knowledge declaratively with Why / Context."}, "symbolic": {"basis": "afforded", "records": ["RTE-8"], "note": "The prescribed derived note also contains frontmatter tags and wikilink targets consumed by routing code."}}
      records: ["RTE-8"]
      note: "Mixed note form is explicit: prose plus machine interpreted metadata. No model-weight update is in scope."
    faithfulness_tested:
      assessment: "known"
      values: ["no"]
      evidence: {"no": {"basis": "wired", "records": ["ABS-3"], "note": "Inspected benchmark code measures retrieval and answers, with no retained intervention testing dependence on recalled content."}}
      records: ["ABS-3"]
      note: "Bounded negative about this pinned repository and run, not a claim that no external evaluation exists."

---

# Napkin agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-napkin-03/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/napkin.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-napkin-03/memory-report.md`
**Memory analysis report SHA-256:** 5aa2e9572c7ca0817b482bb9588ddc68788e76009126fb5c08d814e89d30b843

## Boundary and evidence

Evidence basis: pinned implementation, shipped instructions and reported benchmark documentation from https://github.com/Michaelliv/napkin at `7582d6a46f5a11995956e60a59c41a5b242109f1`, inspected on 2026-09-27. The checkout origin matches that identity even though package metadata names shift-labs-ai. No source refresh, runtime execution or prior analysis informed this run.

This analysis explains what Napkin contributes to agent memory and where external agents still decide. Include the CLI/SDK, vault and retrieval machinery, distill/tend instructions, configuration and package-update admission, and the LongMemEval harness as an explicit consumer/evaluation example. The class is a memory/knowledge/context-engineering system; the boundary is a complete artifact, partial loop. Node/Bun and filesystem behavior, FerroSearch internals, the pi runtime and context extension, model providers, user editing through Obsidian, and npm distribution are external dependencies. Their exclusion prevents deployed isolation, complete context assembly, parameter fixity, actual compliance, or end-to-end improvement conclusions. Ordinary note operations, retrieval, curation and evaluation are assessed; structured base/canvas/bookmark memory surfaces and all three benchmark import routes are included through the specialist. Formula correctness, graph rendering, HotpotQA and LoCoMo scoring details, and release CI are not exhaustively audited. No claim of complete security or evaluator equivalence across those surfaces follows.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/Michaelliv/napkin` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | Implementation | CLI/SDK entry paths, CRUD, daily, properties, tasks, templates, search, overview, config, file/link/cache utilities, bases, canvas, bookmarks and package update | Full commit-relative paths on records; [SDK](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/sdk.ts) | Dependencies and deployed hosts excluded; no execution observations |
| SRC-2 | Git | `https://github.com/Michaelliv/napkin` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | Doctrine/design | README, distill/tend and specialist documentation scope | [README](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/README.md), record anchors | Instructions do not demonstrate model compliance |
| SRC-3 | Git | `https://github.com/Michaelliv/napkin` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | Implementation; separately, reported operation | LongMemEval harness/prompt, all three benchmark import/launch boundaries and overview scorer are implementation; bench README is reported performance | [Harness](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts), `bench/README.md` | No dataset, external extension, executed transcript or causal intervention inspected |

Operational access root: `/home/zby/llm/commonplace/related-systems/Michaelliv--napkin`. All source evidence was read through commit-addressed Git. Tree listings are inventory evidence, not runtime observations.

## Shared records

### Components

### CMP-1 — Napkin CLI and SDK

Implementation conclusion status: wired. A TypeScript library exposes `Napkin`; Commander dispatches CLI commands to adapters and the same SDK/core functions. Symbolic code executes local file and search operations; `package.json` exports `dist/index.js`, `dist/main.js`, and packages `skills`. SRC-1 `package.json`, `src/main.ts:200-225`, `src/commands/search.ts:22-48`, `src/sdk.ts:128-181`.

> search(query: string, opts?: SearchOptions): SearchResult[] {
> return searchVault(this.vault, query, opts);
> }
> --- `src/sdk.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### CMP-2 — External pi answerer and judge models

Invocation conclusion status: wired. This covers the benchmark call boundary, not provider execution. Distributed-parametric computation is outside Napkin core. SRC-3 `bench/longmemeval-eval.ts:236-247,336-352,452-460` passes a configurable model identifier to pi, with dated default `anthropic/claude-haiku-4-5-20251001`. Exact provider weight identity conclusion status: uninspected; an endpoint name does not establish an immutable weight digest. Parameter-change conclusion status: uninspected. Provider internals are excluded; the inspected harness passes inference arguments, not a training operation. The distill/tend skill host model is unspecified. SRC-2 `docs/distill.md:24-46,69-75` separately describes a background pi model call with a configurable `claude-sonnet-4-6` default; that invocation is claimed, and implementation and exact weight pinning remain uninspected. No embedding model is established by this component inventory.

> const output = execFileSync("pi", [
> "--print",
> "--model", modelFlag,
> "--no-extensions",
> "--no-skills",
> "--no-prompt-templates",
> judgePrompt,
> ], {
> encoding: "utf-8",
> timeout: 30_000,
> maxBuffer: 10 * 1024 * 1024,
> });
> --- `bench/longmemeval-eval.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### Operative objects

### OBJ-1 — Vault or injected configuration

Implementation conclusion status: wired. Symbolic settings control layout, retrieval limits and overview shape. File-backed `.napkin/config.json` is persistent; an SDK caller may instead supply a copied, recursively frozen object. This is the configuration subpart of OBJ-8. Accumulated disk settings belong to the memory access scope; static injected caller settings are excluded from accumulated memory. SRC-1 `src/utils/config.ts:44-108`, `src/core/config.ts:30-58`.

> export function effectiveConfig(vault: VaultInfo): NapkinConfig {
> return vault.config ?? loadConfig(vault.configPath);
> }
> --- `src/utils/config.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### OBJ-2 — Benchmark generated answer

Invocation conclusion status: wired. SRC-3 `bench/longmemeval-eval.ts:354-405` collects text deltas into `agentAnswer`. Natural-language claims answer a supplied question about imported conversations; no particular generated answer instance was inspected. The prompt instructs retrieval and arithmetic, but an answer's preservation, derivation or ampliation cannot be classified without its content and trace.

### OBJ-3 — Benchmark score and result record

Implementation conclusion status: wired. SRC-3 `bench/longmemeval-eval.ts:196-270,390-420,600-614` computes answer score against dataset references and writes JSONL results. Symbolic scores are evaluation records, not revised knowledge or a subsequent theory. The dataset supplies the expected answer; the judge is an evaluator, not the answer oracle's source.

### OBJ-4 — Unresolved-link report

Implementation conclusion status: wired. SRC-1 `src/core/links.ts:17-40,62-65` maps parsed wikilinks to files and returns unresolved targets. It is symbolic structural evidence, not a verdict about note claims. The source explicitly uses shallowest-match resolution for ambiguous links; resolution does not prove intended referent identity.

### OBJ-5 — Vault notes and editable note metadata

Evidence: SRC-1 `src/core/crud.ts:36-85,88-137,176-198`, `src/core/daily.ts:57-107`, `src/core/properties.ts:34-57`, `src/core/tasks.ts:135-155`; SRC-2 `README.md:143-191`. Conclusion status: wired. Markdown files hold authored, imported or extracted prose; frontmatter, task marks and wikilinks are symbolic metadata. Daily notes can be raw records, while distilled notes are derived knowledge. File storage does not itself distinguish their epistemic status. The later consumers are read/search/overview, structured queries, and agents using those interfaces. Notes have advisory knowledge authority unless a consumer deliberately treats their contents as instructions.

> const content = fs.readFileSync(path.join(vaultPath, resolved), "utf-8");
> return { path: resolved, content };
> --- `src/core/crud.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> const updated = setProp(content, name, parsedValue);
> fs.writeFileSync(fullPath, updated);
> --- `src/core/properties.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

These are readable content, not opaque memory payloads. Provenance is whatever the author retained: paths, prose, dates and links are available, but the write primitive adds no immutable source transcript or evidential attestation.

### OBJ-6 — Project context, folder descriptions and templates

Evidence: SRC-1 `src/core/overview.ts:433-462,988-1032`, `src/core/templates.ts:18-52,55-89`, `src/core/crud.ts:60-80`, `src/core/daily.ts:57-72`; SRC-2 `skills/distill/SKILL.md:54-67,82-104,124-126`, `skills/tend/SKILL.md:60-77,95-96`. Read/copy conclusion status: wired. Agent instruction authority conclusion status: afforded. Mutable `NAPKIN.md` is project context; `_about.md` describes placement; vault templates shape future notes. Initial shipped scaffolds are not accumulated memory, but their edited vault copies are in scope.

> const contextPath = path.join(contentPath, "NAPKIN.md");
> const context = fs.existsSync(contextPath)
>   ? fs.readFileSync(contextPath, "utf-8").trim()
>   : undefined;
> --- `src/core/overview.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> const existing = fs.readFileSync(targetPath, "utf-8");
> fs.writeFileSync(targetPath, existing + templateContent);
> --- `src/core/templates.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Templates are read and copied by code, with variable resolution in the insert/read-template path. `create --template` and daily initialization copy template bytes directly. The content is fully inspectable; no claim that every copy path resolves variables is warranted. Tend reserves proposed schema changes for the user. Folder prose descriptions have a 140-character fallback paragraph truncation, while a frontmatter description is returned directly.

### OBJ-7 — Search and overview access structures

Evidence: SRC-1 `src/core/search.ts:40-84,154-250`, `src/utils/search-cache.ts:12-38,44-51`, `src/utils/fingerprint.ts:11-24`, `src/core/overview.ts:64-94,510-572,664-688,781-835,988-1032`. Conclusion status: wired. Search caches persist a serialized lexical index, document metadata and backlink counts. Note bodies are read from files again for snippets. Overview caches persist the returned context and map. Both derive from retained notes; they are compiled access metadata rather than learned parameters or newly synthesized knowledge.

> const composite = r.score + Math.log2(1 + links) + recency * 1.0;
> --- `src/core/search.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> index: index.toJsonString(),
> docs: docs.map(({ content: _, ...rest }) => rest),
> backlinkCounts: Object.fromEntries(backlinkCounts),
> --- `src/core/search.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> entries.push(`${file}:${stat.mtimeMs}`);
> --- `src/utils/fingerprint.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The index serialization is delegated to FerroSearch; the repository shows JSON serialization/loading, indexed fields, and the consumer, not native engine internals. That supports symbolic representation without pretending to inspect its native algorithms. Fingerprints hash paths and mtimes, not content bytes: unchanged timestamps can leave stale access structures. Search applies lexical relevance plus log-damped inbound links and normalized relative recency; this is not recursive PageRank.

Overview candidates come from title, frontmatter, headings and body terms. It probes lexical retrieval, coalesces similar sibling folders and selects reusable search terms. A fallback defeats a literal guarantee that every emitted keyword was successfully search-validated:

> for (const [t] of scored.slice(0, FINGERPRINT_TRIES)) {
>   if (probeTopK(ctx, t).slice(0, 3).includes(note.file)) return t;
> }
> return scored[0]?.[0];
> --- `src/core/overview.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The resulting map guides later search; it is not a semantic summary. No reasons for a knowledge claim are created by index compilation. Counts and keywords expose selection results, but no later route reads a persisted explanation of each selection decision.

### OBJ-8 — Structured vault content and access settings

Evidence: SRC-1 `src/core/canvas.ts:6-38,44-79,106-141,182-218`, `src/core/bookmarks.ts:14-48`, `src/utils/config.ts:13-64,93-128`, `src/core/config.ts:22-58`, `src/core/bases.ts:48-75`; SRC-2 `README.md:291-350`. Conclusion status: wired. Canvas JSON stores text and file/link/group nodes plus edges. Bookmarks retain file or query navigation in `.obsidian/bookmarks.json`. Mutable JSON configuration controls discovery layout, overview and search options. YAML `.base` files retain view filters, formulas, order, limits and presentation choices. These are file-backed symbolic structures, with prose inside some fields; they are not an opaque vector store.

> const content = fs.readFileSync(path.join(vaultPath, filePath), "utf-8");
> const canvas: Canvas = JSON.parse(content);
> --- `src/core/canvas.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The configuration subpart is OBJ-1; its admission and consumer evidence is retained there and on RTE-2.

Human/agent CLI users can list and inspect these objects, while code consumes configuration and base filters for routing. Supplied SDK configuration is copied and frozen; it overrides disk settings, and `configSet` refuses to pretend that changing disk would affect that instance. This limits the behavioral force of accumulated disk configuration for that branch. Canvas text is accessible through canvas APIs but is not indexed by the Markdown search path. Bookmarks are discoverable navigation, not an automatic priority injection mechanism.

### OBJ-9 — Temporary SQLite base-query projection

Evidence: SRC-1 `src/utils/bases.ts:33-38,54-95,133-161,638-687`, `src/core/bases.ts:57-75`. Conclusion status: wired. A base query collects file metadata and frontmatter, builds a relational table in memory, applies stored view configuration, and returns rows. This is a compiled access structure within the scoped retrieval path, with SQLite and in-memory substrate values. It is not durable SQL memory storage.

> const SQL = await initSqlJs();
> const db = new SQL.Database();
> --- `src/utils/bases.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> const sql = `SELECT * FROM files WHERE ${where} ${orderBy} ${limit}`;
> --- `src/utils/bases.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> } finally {
>   db.close();
> }
> --- `src/core/bases.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The caller chooses a view, or the first view is used. Filters, ordering and formulas have operational semantics at the query consumer; results are returned to the requesting user/agent. Computed numeric summaries are not trace distillation.


### OBJ-10 — Inferred claim within a distilled note

Conclusion status: afforded. This is a semantic part of OBJ-5, not another storage container: a generalization the distilling agent draws from session findings. SRC-2 `skills/distill/SKILL.md:109-112` requires a trailing `^[inferred]`; the supporting passage appears once on RTE-8. Such a generalization can go beyond what follows from one session, making ampliative conjecture the appropriate mapping for this branch. No particular inferred candidate or its acceptance trace was observed. Ordinary copied facts in OBJ-5 retain a separate acquisition/reshaping disposition.

### Routes

### RTE-1 — Caller request through CLI or SDK

Implementation conclusion status: wired. Trigger: caller submits a command or method call. Principal and next-step owner: external agent/user/application. Query and vault path identify the current request; `findVault` walks up directories and may create a bare vault if none exists. Commander → command adapter → `Napkin` → core → files/index → typed result or CLI text/JSON is the ordinary progression. SRC-1 `src/main.ts:200-225`, `src/commands/search.ts:22-48`, `src/sdk.ts:128-181`, `src/utils/vault.ts:36-107`.

Policy form is symbolic for retrieval and file mutation, with the caller owning next-query decisions in its own context. Immediate return: data or error; persistent effects: writes and generated caches, including bare-vault creation even when first access is a read. Later read-back and selection: integrated memory routes below. Delegated visibility: uninspected host responsibility. Expiry/invalidation: memory/cache routes below. Activation: uninspected; tool output is not evidence the model acted on it. Recovery: SDK errors or CLI failure, with subsequent choices owned by the caller. No enclosing model loop, model context limit, retry schedule, approval grant or deployment sandbox is established by this route. The capability surface includes reading, creating, overwriting, moving and deleting files; its effective grant is the host process's filesystem authority, which this analysis did not inspect.

> if (parent === dir || dir === root) {
> // No vault found — create a bare one at the starting directory
> return createBareVault(startingDir, config);
> }
> --- `src/utils/vault.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### RTE-2 — Configuration admission

Implementation conclusion status: wired. Trigger/proposer/decision owner: caller supplies dotted key/value or constructor configuration. JSON parsing falls back to string; file settings merge into current defaults/config and persist; constructor injection is cloned and frozen. The injected branch rejects `configSet`, giving code ownership precedence. SRC-1 `src/core/config.ts:30-58`, `src/utils/config.ts:73-95,116-141`.

> if (vault.config) {
> throw new Error(
> "config is injected in code; edit the source, not the vault",
> );
> }
> --- `src/core/config.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Admission force: implemented refusal for this API on injected instances; guarantee strength: invariant within that branch. Direct edits and creation of another instance remain alternate paths; no universal file immutability is claimed. Guidance is symbolic settings and external caller intent, not an evidenced theory criticism. Return: parsed value/config or error. Persistence: disk across invocations, injected object for instance lifetime. Later consumer: `effectiveConfig`; selection is injected-object presence, else file/defaults; invalidation is caller replacement or reread. Delegated visibility and actual effects in deployed agents are uninspected. Recovery is caller reconfiguration; no rollback guarantee is established. No answer oracle applies to this settings route.

### RTE-3 — Package update admission

Implementation conclusion status: wired. SRC-1 `src/commands/update.ts:11-74` runs npm on caller request. External package authors propose successors; registry `latest` and npm select/install them, and the host can refuse execution. Napkin judges the subprocess exit status, not behavior improvement. The proposal guidance is release selection, not retained criticism. Return: success JSON/text or failure exit; persistent effect: global installed package changes. Later read-back and memory selection: inapplicable, this route replaces software. Delegated visibility: uninspected host; expiry: subsequent update; activation: subsequent CLI invocation is possible but not observed. Recovery/rollback is outside this implementation's inspected contract. Guarantee strength: no claimed improvement guarantee. Answer oracle: inapplicable. This is external software intervention, not evidence of self-improvement.

> const target = "@shiftlabs/napkin@latest";
> const npmCommand = process.platform === "win32" ? "npm.cmd" : "npm";
> const npmArgs = ["install", "-g", target];
> --- `src/commands/update.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### RTE-4 — LongMemEval answer evaluation

Implementation conclusion status: wired. SRC-3 `bench/longmemeval-eval.ts:196-270,303-426,477-480,600-614`. Operator starts a bounded benchmark; code creates per-question vaults, calls pi with a model, prompt and external context extension, parses its answer, evaluates against dataset `answer`, returns result metrics and removes the temporary vault in `finally`. The external model chooses retrieval and answer steps. Caller sets model/dataset options; an external judge model or string scoring decides answer score. No automatic successor-theory selection is established by this route.

> if (normPred === normGold || normPred === normPrimary) return 1;
> if (normPrimary.length > 0 && normPred.includes(normPrimary)) return 1;
> if (normPred.length > 0 && normPrimary.includes(normPred)) return 1;
> --- `bench/longmemeval-eval.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> } catch {
> // Fallback: token F1 with primary answer only
> return tokenF1Basic(prediction, primaryAnswer);
> }
> --- `bench/longmemeval-eval.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

These alternate scoring paths matter: a reported accuracy aggregates permissive substring matches, model judgments and possibly token F1, not one uniform truth test. Epistemic license is answer fit to a supplied reference under those rules. It does not warrant note truth, retrieval causality or theory criticism. The reference provider is the LongMemEval dataset named in the harness; dataset correctness itself is uninspected. Immediate return: result/null; persistence: metrics and optionally retained output, with question vault deleted. Later read-back: no implemented score-to-memory revision established in the inspected function; further operator use uninspected. Delegated visibility: pi process output; extension internals excluded. Selection: sampled question and reference answer; invalidation: question completion cleans temporary state. Recovery: timeout/error returns null; judge error falls back to token F1. Effect/activation: implementation only, no executed trace. Guarantee strength: best effort evaluation.

### RTE-5 — Structural link checking

Implementation conclusion status: wired. SRC-1 `src/core/links.ts:17-40,62-65` scans current Markdown files, parses wikilinks, resolves target names and returns OBJ-4. Trigger: requested inspection, including the distill/tend verification instructions. Producer/evaluator: deterministic link resolver. Immediate return: unresolved targets and source files; persistence: none intrinsic to the report. Later consumer: external agent/user deciding repairs; delegated visibility uninspected. Selection: current vault Markdown and extracted links; invalidation: rerun after changes; expiry: current filesystem snapshot only. Effect: informs fixes, with no enforced rejection of a note write. Recovery: caller corrects files and reruns. Guarantee strength: no claimed semantic-truth guarantee. Link existence is its check domain, and not an answer oracle for note content.

> for (const target of links.wikilinks) {
> const resolved = resolve(target);
> if (resolved) append(incoming, resolved, file);
> else append(unresolved, target, file);
> }
> --- `src/core/links.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### RTE-6 — Explicit authoring, revision and withdrawal

Evidence: SRC-1 `src/commands/crud.ts:40-70,73-119`, `src/core/crud.ts:45-85,88-137,134-198`, `src/core/properties.ts:34-75`, `src/core/tasks.ts:135-155`, `src/core/daily.ts:90-134`, `src/utils/files.ts:19-55,88-118`. Conclusion status: wired. A caller supplies text or edits through CLI/SDK; create, append, prepend, property/task changes and template insertion persist bytes. Automatic daily creation is scaffolding, not automatic knowledge extraction. Later consumers read the changed note through the same discovery interfaces. The plain-file surface also affords editing by a human tool.

> if (fs.existsSync(fullPath) && !opts.overwrite) {
>   throw new Error(
>     `File already exists: ${targetPath}. Use --overwrite to replace.`,
>   );
> }
> --- `src/core/crud.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> const trashPath = path.join(trashDir, path.basename(resolved));
> fs.renameSync(fullPath, trashPath);
> --- `src/core/crud.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Collision rejection prevents accidental create-overwrite but is not deduplication. Revision changes retained entries, establishing evolve. Default deletion withdraws a note from ordinary listings via `.trash`, establishing invalidate with retained bytes. This is limited history: no version chain, basename-only trash destination, and an explicit permanent deletion path. Move and rename change filenames but do not rewrite inbound links in the inspected functions; tend requires link repair separately. Read ambiguity throws, while backlink indexing uses a shallowest-match resolver. These different identity rules can affect retrieval and maintenance.

Admission audit: proposer and decision owner are the caller; guidance can be supplied prose, template material or a direct property/task edit. The primitive does not inspect the proposed claim's theory, criticism or rationale. Rejection is existence/file-resolution checks; overwrite is an explicit bypass of collision refusal, not semantic approval. Immediate return reports paths/results, and later read-back uses RTE-7. Delegated visibility is caller-owned and uninspected. Withdrawal uses trash or permanent deletion; recovery requires caller restoration and is not a general versioned rollback. The consumer sees revised bytes, but behavioral activation is uninspected. Guarantee strength: no claimed truth guarantee.

### RTE-7 — Requested discovery and delivery

Evidence: SRC-1 `src/sdk.ts:144-181`, `src/commands/overview.ts:34-77`, `src/commands/crud.ts:12-37`, `src/core/search.ts:87-126,228-251`, `src/core/links.ts:17-80`; SRC-2 `skills/distill/SKILL.md:54-80`, `skills/tend/SKILL.md:23-53`, `README.md:177-191`. Request/return conclusion status: wired. External agent semantic use conclusion status: afforded. The requesting role is a task agent following the documented workflow, a distill/tend agent, or a human operator. It chooses overview, query, note identifier or a structured view; CLI stdout/JSON or SDK return data delivers the selected material.

> human: () => console.log(result.content),
> --- `src/commands/crud.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> const contextLines = opts?.snippetLines ?? config.search.snippetLines;
> const limit = opts?.limit ?? config.search.limit;
> --- `src/core/search.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Overview output includes context and folder rows; search returns ranked file paths, scores, timestamps and matching lines; read returns full bytes. Default search is 30 results with zero surrounding context lines, and default overview depth is three with no keyword cap (`src/utils/config.ts:44-53`). These are structural limits, not token truncation. The agent still selects queries and decides whether to use content. Returning a requested overview, even though it includes NAPKIN.md automatically, is pull at this consumer boundary. Tags, properties, tasks, links, bases, canvases, bookmarks and templates provide narrower requested views; none proves automatic model activation.

The graph UI is another wired human pull route: it loads Markdown content and wikilinks, embeds them in the visualization payload, and renders the clicked note in a sidebar. It excludes the configured templates folder and `index.md`; this differs from the search corpus. Evidence: SRC-1 `src/commands/graph.ts:23-80,295-312,451-485`. Base64 serialization here is a transport encoding of inspected text, not an opaque learned payload.

> nodes.push({ id: slug, text: title, content, filePath: rel });
> --- `src/commands/graph.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Route audit: policy and executor are the symbolic core, with an external agent/user owning the next request. Context/state are current files, configured limits and cached access metadata. Immediate return is data/text; later memory use is afforded for the named agent, with actual activation uninspected. Cache invalidation uses the path/mtime fingerprint and relevant options (OBJ-7), not semantic change detection. Structured views can return material not indexed by Markdown search (OBJ-8, OBJ-9). A query result has no intrinsic expiry beyond changes in source files; full reads have no token cap. Delegated visibility and model-side truncation are uninspected host behavior. File/parse/query errors return to the caller, which owns recovery. Guarantee strength: implemented selection rules, no end-to-end relevance or truth guarantee.

### RTE-8 — Session distillation into durable knowledge

Evidence: SRC-2 `skills/distill/SKILL.md:3-9,14-52,54-126`; SRC-1 `src/core/crud.ts:45-85`, `src/core/overview.ts:1020-1032`. Conclusion status: afforded. A user invokes the skill during work or an agent invokes it at session end; hook/timer invocation is contemplated but no such scheduler is included. The producer is the skill-executing agent, input is current conversation/working-session material, output is persistent topic notes or revisions. The gate selects non-obvious fixes, confirmed behavior, reasoned decisions and reusable procedures. It can reject a routine session without writing.

> Apply the 3-month test: *what from this session would be valuable in 3 months
> with no memory of this chat?*
> --- `skills/distill/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> - Keep: decisions and their why, root causes, confirmed behaviors, procedures,
>   mental models that took effort to reach.
> --- `skills/distill/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> Integrate — don't append a dated "update" section to the bottom. Fold new
> information into the sections where it belongs. If the new finding contradicts
> the note, say so in the note explicitly rather than silently keeping both.
> --- `skills/distill/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> - **Mark synthesis.** A claim the session actually established needs no marker.
>   A generalization you are drawing gets a trailing `^[inferred]`.
> --- `skills/distill/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> Fix broken links (typo, or drop the link). If the session changed what this
> project fundamentally *is* — new architecture, changed direction — update
> `NAPKIN.md` (the always-loaded context note), keeping it under ~200 words.
> --- `skills/distill/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The chain is session material → selected knowledge with tags, summary and reasons → durable note → future search/read or pinned context. This establishes afforded trace learning without implying improved capacity. It covers cross-task reuse, with a per-project context branch; invocation can occur online during work or offline at session end. Notes mix natural language and symbolic routing metadata. No distinct compaction/checkpoint mechanism was found in shipped core.

Reasons are deliberately retained in Why / Context or integrated sections. A later full-note read delivers them, and distill reads an existing note before merging, so a consumer can inspect the reasons. No instruction here requires testing a prescription against its rationale or retaining a record of criticism; write-back alone cannot prove that process.

The skill declares conversation and quoted sources to be data, never instructions. This is a source instruction to the distilling agent, not a parser-enforced trust barrier. Link verification tests navigability, not factual support or faithful extraction.

Admission audit: the host agent proposes, compares against existing notes, selects KEEP/SKIP and commits note edits through RTE-6; the user triggers work but no mandatory human acceptance gate is stated. Guidance is the skill's reusable-knowledge criterion and the existing note's content/reasons. It permits naming a contradiction, but the alleged contradiction is a model interpretation unless separately checked. Theories, reasons and inferred claims may persist; criticism need not be durably retained as a separate object. Immediate return is a note-by-note report. Later read-back is RTE-7 or the documented RTE-10; expiry/invalidation requires later revision or withdrawal. Delegated visibility and behavioral activation are uninspected. Recovery is subsequent editing/link repair, with no transactional rollback guarantee. Guarantee strength: policy/best effort. The theory-builder condition and learning findings in Bounded synthesis apply separately; storing an explanation is not evidence that it was criticized.

Literal example limitation: SRC-2 `skills/distill/SKILL.md:84-87` supplies a folder to `--path`, whereas SRC-1 `src/core/crud.ts:46-55` treats that option as the full target path. This reduces confidence in literal execution of the example, while leaving the available write capability intact.

> if (opts.path) {
> targetPath = opts.path.endsWith(".md") ? opts.path : `${opts.path}.md`;
> } else {
> const name = opts.name || "Untitled";
> targetPath = `${name}.md`;
> }
> --- `src/core/crud.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### RTE-9 — Tending retained notes

Evidence: SRC-2 `skills/tend/SKILL.md:18-58,60-96`; SRC-1 `src/core/links.ts:43-80`, `src/core/crud.ts:176-198`. Semantic maintenance conclusion status: afforded. Diagnostic/deletion primitive conclusion status: wired. Trigger is user request or a proposed periodic run. The agent inspects overview, unresolved links, orphans and tag counts, then handles at most three to five issues. Retained notes are both input and output. Duplicates are integrated into the better named note; the other copy is withdrawn and links repaired. Empty/superseded notes can be trashed; valuable orphans are reconnected; tags and locations can be revised. This supplies consolidate, dedup, evolve and invalidate at the appropriate per-operation strengths.

> Only merge when the overlap is obvious from reading — similarity of vibe is
> not enough.
> --- `skills/tend/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> The user decides. Templates are the vault's schema; schema changes are theirs.
> --- `skills/tend/SKILL.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

This is judgment-guided curation of content rather than an automatic similarity threshold over embeddings. The result is immediately eligible for later read-back. Reports list edits and leftovers, but there is no required durable curation rationale or later consumer of that report. A merged note can retain existing reasons, yet tend does not explicitly guarantee their preservation.

Admission audit: the agent proposes repairs and merges, can decline uncertain cases and selects what remains; the user alone decides new templates. Guidance is navigability, obvious overlap and continued value, with notes and diagnostics as input. Repairs persist through RTE-6; immediate return is the human-facing report, whose later read-back is not specified. Note read-back continues through RTE-7. No fixed expiry is declared; deletion withdraws reliance via ordinary discovery. Delegated visibility and behavior change are uninspected. Trash offers a limited recovery path, while overwritten content has no built-in version rollback. Guarantee strength: policy/best effort. A duplicate judgment is not automatically a criticism of a theory's content; revision rationale and formulation of such criticism remain uninspected. No independent answer oracle is specified.

### RTE-10 — Documented session-start context supply

Evidence: SRC-2 `docs/agent-memory-progressive-disclosure.md:11-15`, `README.md:366-372`; SRC-1 `src/core/overview.ts:1020-1032`; SRC-3 `bench/longmemeval-eval.ts:336-350,477-480`. Conclusion status: afforded. Documentation gives an agent session the same project context note automatically; README names pi-napkin as the integration providing vault context injection. The selector input is the active vault, selected part NAPKIN.md, trigger each session, channel agent context. It is coarse supply, with a suggested small note size rather than a verified selector budget.

> A small "always loaded" note the agent reads on every session. Like CLAUDE.md but for the knowledge base. Contains project goals, conventions, key decisions. Should fit in ~500 tokens.
> --- `docs/agent-memory-progressive-disclosure.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

No shipped source implements this agent-session hook. The in-repository overview helper can supply the content but does not prove an automatic session callback. Benchmark launch flags name a missing extension; they do not reveal what that extension injects. No lexical, embedding, judgment or identifier-targeted push selector can be inferred from requested search/read interfaces. Thus push and coarse remain afforded while pull is wired.

Route audit: next-step owner and executor are the external integration; policy form is documentary specification. Immediate return is agent context, not a command response; later read-back is repeated session delivery of retained project content. The selected part is fixed by active project/vault, with no evidenced per-query selector. An edited project note can change later supply; invalidation, recovery, delegated visibility and exact channel placement remain uninspected outside this interface boundary. Actual behavioral activation is uninspected. Guarantee strength: policy rather than a shipped scheduling invariant.

### RTE-11 — Benchmark import and external answering interfaces

Evidence: SRC-3 `bench/longmemeval-eval.ts:95-168,303-350`, `bench/longmemeval-prompt.md:5-24`, `bench/locomo-eval.ts:91-155,239-277,415-423`, `bench/hotpotqa-eval.ts:64-102,214-253`. Import/launch conclusion status: wired. External answering conclusion status: afforded. LongMemEval serializes each user round with following assistant turns into Markdown, in day directories, and assigns timestamps for recency ranking. LoCoMo imports dialogue plus dataset-provided summaries and observations, with adjacent-session links. HotpotQA imports paragraphs and adds name-matching links. Each also generates a NAPKIN.md inventory/context note. These are retained temporary test corpora, not evidence of an agent improving its persistent production memory.

> const summary = sample.session_summary?.[`session_${num}_summary`] ?? "";
> const observations = sample.observation?.[`session_${num}_observation`] ?? [];
> --- `bench/locomo-eval.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> content += `**${speaker}:** ${t.content}\n\n`;
> --- `bench/longmemeval-eval.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> 1. Search the vault for relevant sessions
> 2. Read each relevant session completely
> 3. Write down the exact facts and numbers you found (quote them)
> --- `bench/longmemeval-prompt.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

The prompt substitutes vault path, question date and question into agent instructions and launches pi with the external extension. LongMemEval asks for full reads and newer evidence when values conflict. LoCoMo computes an overview locally, but that variable is not supplied to `runQuestion`; this is not itself an automatic overview-to-model route. An external extension may supply context, but that implementation is unavailable. Raw-round segmentation preserves trace content rather than extracting durable behavior-shaping conclusions; imported LoCoMo summaries were already derived elsewhere. Neither upgrades trace learning to wired. Their read-back consumer is concrete—the benchmark answering agent—while actual launch success is unobserved.


Route audit: operator selects test input, deterministic import creates the temporary corpus, and external pi chooses answer actions. Guidance is source dialogue/paragraphs and benchmark prompts; imported summaries retain their external origin. Immediate return and cleanup follow each harness's question runner; RTE-4 details LongMemEval. Persistence lasts for the test corpus/answering horizon, not a later production task. Requested read-back uses RTE-7; extension push is uninspected. Selection is question-specific import and query; invalidation is corpus cleanup. Delegated visibility is through the spawned host, and actual activation remains uninspected. Failure/recovery belongs to the harness and host; no retained theory revision is inferred from scores. Guarantee strength: no claimed improvement guarantee.

### Claims

### CLM-1 — Knowledge system and progressive disclosure

Conclusion status: claimed. SRC-2 `README.md:1-3,127-137` calls Napkin a knowledge system for agents and presents context note → overview → ranked search → full read. The implementation supports access and retention mechanisms, while knowledge warrant and actual behavioral benefit require separate evidence.

> 🧻 Knowledge system for agents. Local-first, file-based, progressively disclosed.
> --- `README.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### CLM-2 — Benchmark retrieval performance

Conclusion status: claimed. SRC-3 `bench/README.md:19-27` reports pi + Napkin (Sonnet, 100 questions each) at 92%, 91%, 83% on Oracle/S/M. The benchmark code is inspectable, but these are attributed reported outcomes, not observed runs here; model, comparison system and sample differences prevent component-specific causal attribution.

> **pi + napkin (Sonnet, 100 questions each):**
> --- `bench/README.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### Evidenced absences

### ABS-1 — Benchmark context extension absent from pinned tree

Conclusion status: absent. Searched boundary: `git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/Michaelliv--napkin ls-tree -r --name-only 7582d6a46f5a11995956e60a59c41a5b242109f1 .pi bench/results` returned no paths; the full tree listing likewise contained neither path. SRC-3 `bench/longmemeval-eval.ts:477-480` requires `.pi/extensions/napkin-context/index.ts` and exits if missing. This bounds absence to the pinned artifact; it prevents reconstructing extension push selection or reproducing reported runs from these bytes alone, not the possibility of such a deployment.

### ABS-2 — No built-in distillation or automatic promotion loop established

Evidence: SRC-1 `src/main.ts:7-64,88-135`, `src/sdk.ts:128-181`; whole-tree commit listing and scoped core/utility search; SRC-2 `docs/distill.md:37-46,77-89,124-134`, `docs/agent-memory-progressive-disclosure.md:88-117`. Conclusion status: absent. Boundary: shipped core. The command surface exposes storage, discovery and editing; it contains no model-call distill command, periodic extraction implementation, access-frequency promotion tracker, or trace compactor. Documentation describes mutually different arrangements: an older proposed distill command and a pi extension. The shipped skills remain usable independently, so this negative does not negate afforded trace learning.

> **Lives in pi** — it's a pi extension, not a napkin feature
> --- `docs/distill.md` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Bounded absence search: `git --no-replace-objects -C related-systems/Michaelliv--napkin grep -n -i -E 'distill|compac|promot|model.call|setInterval' 7582d6a46f5a11995956e60a59c41a5b242109f1 -- src/main.ts src/sdk.ts src/core src/utils` returned no matches (Git grep status 1, empty output). This search covers the shipped entry point, SDK, core and utilities, including their checked-in tests. The full inventory command `git --no-replace-objects -C related-systems/Michaelliv--napkin ls-tree -r --name-only 7582d6a46f5a11995956e60a59c41a5b242109f1` supplied the complete pinned tree; the CLI imports and documented methods were then inspected directly. The negative is bounded by these paths and the excluded external extension, not inferred solely from a missing keyword.

This prevents interpreting extension configuration examples as implemented Napkin scheduling. No autonomous continuation checkpoint or durable criticism ledger appears among the inspected routes. It does not establish absence in excluded external runtimes.

### ABS-3 — No retained test of dependence on recalled content

Evidence: SRC-3 `bench/README.md:17-45`, `bench/hotpotqa-eval.ts:255-281`, `bench/longmemeval-eval.ts:303-350`, `bench/overview-exposure.ts:1-22,38-61`; complete pinned file inventory. Conclusion status: absent. Boundary: available pinned evidence. Documentation reports answer accuracy; benchmark code measures retrieval/access proxies and answer correctness; overview scoring checks keyword exposure. None supplies retained execution evidence intervening on recalled content to establish whether it caused the answer or action.

>  * Direct queries only — a deliberately blunt external metric for regression
>  * tracking, independent of the selection heuristics inside the pipeline.
> --- `bench/overview-exposure.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

Bounded absence search: `git --no-replace-objects -C related-systems/Michaelliv--napkin grep -n -i -E 'faithful|ablat|interven|causal|counterfact|memory.disabled|without.memory' 7582d6a46f5a11995956e60a59c41a5b242109f1 -- bench README.md docs src` returned no matches (Git grep status 1, empty output). The full tree inventory named in ABS-2 contained benchmark source, documentation and chart images but no retained per-run execution record. Direct inspection of the three benchmark import/launch/measurement boundaries and overview scorer established the kinds of measurement present. The keyword search supplements that inspection; it does not prove a global absence of every possible unlabeled test. Documentation and chart presentations do not establish an intervention on recalled content, and no such experiment was run by this worker.

The current scorer calls `loadSearchCorpus` with two path strings, while the inspected function requires a `VaultInfo` object. This source-level mismatch further prevents assuming this scorer ran successfully unchanged at the pinned revision. Reported benchmark figures remain reported outcomes; no benchmark was executed or causally validated here. The faithfulness classification is a bounded no, not a denial of all possible external tests.


The scorer mismatch on ABS-3 is source-level evidence, not a runtime observation:

> const corpus = loadSearchCorpus(n.vault.contentPath, n.vault.configPath);
> --- `bench/overview-exposure.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

> export function loadSearchCorpus(
> vault: VaultInfo,
> folder?: string,
> ): SearchCorpus {
> --- `src/core/search.ts` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

### Behavioral-authority paths

### BAP-1 — Configuration authority over core operations

Conclusion status: wired. OBJ-1 → `effectiveConfig` → core consumer; channel: program data; force: routing/selection settings, including retrieval budget; horizon: SDK instance for injection, subsequent invocations for disk settings. RTE-2 supplies the admission rule. This is operational authority, not a truth judgment.

### BAP-2 — Benchmark prompt and evaluation

Prompt delivery/scoring conclusion status: wired. Behavioral activation conclusion status: uninspected. SRC-3 `bench/longmemeval-eval.ts:323-352,390-420`, `bench/longmemeval-prompt.md` sends retrieval instructions as pi's system prompt, with scenario date and question. Consumer: external answerer; force: instruction; horizon: question invocation. Score consumer: benchmark metrics/reporting, not a memory revision gate. The expected answer is supplied to evaluation after answering.

### BAP-3 — Retained note knowledge at the task agent

Conclusion status: afforded. OBJ-5 and OBJ-6 reach a later task, distill or tend agent through requested CLI/SDK output (RTE-7) or documented project context (RTE-10). Force: advisory knowledge and potentially project instruction; horizon: later task/session within the vault. SRC-2 `skills/distill/SKILL.md:54-80`, `skills/tend/SKILL.md:23-53`, `docs/agent-memory-progressive-disclosure.md:11-15`. Delivery wiring is on RTE-7; epistemic acceptance and behavioral adoption are not established by it.

### BAP-4 — Access metadata at deterministic selectors

Conclusion status: wired. OBJ-7, OBJ-8 and OBJ-9 reach search/overview/base consumers through serialized metadata or retained view settings. Force: ranking and routing; horizon: the next request under those data/settings. SRC-1 `src/core/search.ts:200-224`, `src/core/overview.ts:781-835`, `src/utils/bases.ts:638-687`. These checks select accessible material, not true claims.

### BAP-5 — Template and skill guidance at a writer

Agent interpretation conclusion status: afforded. Template copying conclusion status: wired. SRC-2 `skills/distill/SKILL.md:49-52,82-112`, `skills/tend/SKILL.md:60-77`, SRC-1 `src/core/templates.ts:55-89`. Consumer: distill/tend agent and note-creation primitive; channel: instructions and template bytes; force: instruction/output structure, with user authority over new schemas; horizon: current write and subsequent copied content. The data-only trust instruction is a policy of the writer, not core sanitization of every later read.

## Runtime account

Napkin's ordinary invocation is a returning computation inside an externally owned loop (RTE-1). An agent or user chooses a vault and query; the command adapter obtains a Napkin instance, which discovers or creates the vault, loads effective configuration, reads or rebuilds search state, ranks results and returns text/JSON. The external caller chooses whether to search again, open a note, follow a link or write. The SDK changes the output channel to typed data and errors while sharing core operations. No model call is needed inside this core route; the model-dependent purpose is its service to agent context and the shipped distill/tend workflows.

Material alternates are CLI versus SDK, direct human or host filesystem editing, constructor configuration versus file configuration, permanent versus trash deletion, and the separately described host extensions. These paths prevent converting skill policies into universal enforcement. RTE-2's injection refusal covers that API; it does not lock disk files. RTE-3 delegates package replacement to npm. RTE-4 includes an actual model-invocation call site, but the pi runtime and required context extension remain outside inspected implementation. Permissions, shell/tool approvals and deployment isolation are external grants, not properties inferred from a local-file design.

The smallest forcing cases were inspected statically: (1) no vault ancestor creates a bare vault rather than returning a pure read error (RTE-1); (2) configuration writes on an injected SDK instance throw (RTE-2); (3) a failed benchmark judge invocation falls back to token F1, while a failed answer invocation returns null (RTE-4); and (4) overview keywords can fall back to an unvalidated top candidate and complete a roster of note titles (`src/core/overview.ts:771-822`). The fourth bounds the README's “search-validated keywords” language: probe-based selection is a preference with explicit alternatives, not an invariant that every emitted keyword retrieves its represented note.

**no dynamic check planned.** CLI smoke tests, keyword fixtures and a benchmark rerun were considered. Static branches suffice to establish the selected implementation and policy boundaries. A behavioral-benefit claim would require an external agent and retained comparative traces, and the benchmark's required extension is outside the pinned tree (ABS-1). No unexecuted check supplies a negative behavior finding.

Decision roles follow the actual route. The host agent proposes distilled notes, interprets contradictions and decides whether to keep/merge them under source instructions; the user may invoke the workflow and decides template schema changes. Napkin executes file operations and structural link checks. Human editors can author or revise directly. A timer extension is documented, not implemented in the inspected tree. None of these instructions independently supplies a reference answer for note truth. Only RTE-4 has an explicit answer oracle: the dataset's expected answer; its scores are for bounded experiments, while ordinary retrieval and distillation serve open requests. Computational scoring and human/model selection are not conflated into an autonomy grade.

## Lens scoping

### Memory/context scope

Trigger evidence: CLM-1 and SRC-2's progressive disclosure and distill/tend instructions. Depth: full, because accumulated note content, context notes, indexes, automatic extraction claims, curation and distinct later-consumer channels all affect the selected purpose. Frozen scope includes CLI/SDK and the shipped/declared host-facing routes, with inaccessible extensions marked explicitly. The fresh specialist's input hash is `4a233851c122c3ec6c59ecf4b22cdb870cc53906ffe9d64763cd6bf28b14fa8c`. Canonical objects and routes are identified in the integrated output below.

### Epistemic scope

Trigger evidence: CLM-1, distill's declared capture of knowledge and inferred generalizations, tend's revision instructions, RTE-4 and RTE-5. Depth: full. Question: which transformations and checks license reliance on stored statements, and which only change retrieval or operational availability? Include acquisition, semantic extraction, note merging, structural checks, retrieval-handle checks and benchmark scoring. Exclude provider internal reasoning and unrecorded agent executions; these prevent observed candidate dispositions, proven theory criticism and causal learning claims. This local lens uses the frozen SRC-1, SRC-2 and SRC-3 boundaries and overlays the canonical records rather than creating another inventory.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried OBJ-5, OBJ-6, OBJ-7, OBJ-8 and OBJ-9, with RTE-6, RTE-7, RTE-8, RTE-9, RTE-10 and RTE-11. Its full proposed comparison profile is integrated above with its evidence strengths preserved. 
Napkin retains editable knowledge in ordinary files and moves selection work into a progressive read interface. A task agent can request a folder map, choose search terms, inspect ranked snippets, then request full notes. The content and its access metadata change together: note names, frontmatter, links and modification times influence what the next query returns. This is wired retrieval machinery; whether a later model follows or benefits from the retrieved content is not observed.

The distill skill adds an afforded trace-to-knowledge loop: a working conversation becomes topic notes, with explicit reasons, deduplication search, contradiction handling and optional revision of project context. Tend operates on already retained notes. Both procedures depend on a caller loading the skill and an agent performing its judgments. Neither is a built-in autonomous scheduler.

Context sizes in the README are design expectations, not enforced total token budgets. Search limits result count and snippet context lines, but can emit many matching lines within each file. Overview limits depth and optionally keyword count, yet includes the complete NAPKIN.md and allows uncapped keywords by default. A full read returns the entire file. Records OBJ-6, OBJ-7 and RTE-7 retain the controlling passages.


**Write side.** 
Manual authoring and updates use the primitives in RTE-6. Automatic writes occur in two materially different categories: deterministic compilation/import in RTE-7 and RTE-11, and instructed agent extraction in RTE-8. Only the latter establishes the trace-learning route, at afforded strength. The strongest automatic write witness is therefore wired, while trace-extracted lineage remains afforded. An automatic operation need not be an autonomous operation: a user can start a transformation that the agent then performs.

The extraction procedure searches before creating, prefers integration over appending, explicitly marks contradictions and novel generalizations, and can move project-level findings into NAPKIN.md. Tend reads retained content before judging duplication or supersession. It avoids creating new schemas without the user's decision. Source metadata and human readable reasons can survive in notes, but no automatic source-lineage record or universal history retention is imposed. A note read can deliver its reasons; neither raw persistence nor that delivery demonstrates criticism aimed at a stated explanation.

Mechanical overview generation, backlink indexing, temporary SQL tables and file import are not semantic curation or trace learning. Benchmark segmentation is a trace representation change whose retained content remains raw dialogue; dataset summaries are imported. No alternate compaction checkpoint route was found in the scoped core. The excluded pi extension could add such routes, but this report does not classify them.


**Read-back.** 
The principal later consumer is a task agent that requests overview, search and read; distill and tend are additional named consuming roles. Their procedural call sequence is explicit in the shipped skills, and the CLI's bytes-to-output path is wired. SDK methods without a specified caller are storage/retrieval capabilities; the documented role and benchmark launch boundaries identify actual intended consumers without proving deployed execution.

The map and search snippets narrow what the agent chooses to read, rather than force adoption. Full reads can deliver retained rationale together with claims. Plain-text output can also carry arbitrary note instructions; the core does not label or neutralize them. The distill skill's data-only trust rule governs that worker by instruction. It is not a general runtime assurance for later agents.

The automatic session-context route is documented at the external integration boundary only. Its coarse project note may contain instructions and conventions, but role placement, exact budget and actual model obedience are uninspected outside scope. Requested file identity and lexical search do not become additional push signal values. Bases select structured rows through stored symbolic filters; canvases and bookmarks are explicit pull surfaces outside the Markdown lexical search corpus.


**Comparison rationale.** 
All fourteen axes use the same bounded memory account. Known coverage means the set is complete for these scoped artifacts and documented interfaces, not that every value was observed. Each value retains its own basis. In particular, wired automatic caching cannot strengthen afforded agent extraction; wired pull cannot strengthen afforded push; and a documented benchmark does not strengthen knowledge activation to observed.

Files are the durable substrate. The temporary SQLite base-query projection also belongs to the included access machinery, so the profile includes SQLite and in-memory, with that limit stated on OBJ-9. Logical wikilinks and canvas edges do not establish an independent graph storage engine. Static shipped skills and scaffolds are not counted as accumulated memory merely because they contain instructions. Edited vault templates and project context are counted because the inspected routes read them later.

The extraction route's three-month reuse criterion establishes cross-task intent; its project-context update establishes a per-project branch. Its invocation description establishes both current-session and session-end timing. These conclusions do not derive from session identifiers. Natural language covers the retained knowledge and reasons; symbolic distilled form covers the same note's operative tags and wikilinks, not an invented model-weight update.

Consolidate and dedup reflect tend's integration of overlapping retained content. Synthesis reflects the explicitly marked generalization permitted while integrating session knowledge. Promotion reflects transfer into pinned project context, not the unimplemented proposal to count accesses. Relative timestamp ranking does not on its own establish elapsed-time decay. Invalidation is bounded ordinary-discovery withdrawal, not a complete historical record or access prohibition.



### Epistemic lens

#### 1. Source-and-claim boundary

System/revision and source register: see Run identity and SRC-1, SRC-2, SRC-3. Assessed families are RTE-2 configuration admission; RTE-4 benchmark evaluation; RTE-5 structural checks; RTE-6 storage; RTE-7 retrieval/indexing; RTE-8 extraction; RTE-9 curation; RTE-10 documented supply; and RTE-11 import. RTE-1 is dispatch plumbing and RTE-3 is externally selected software replacement, classified without attributing knowledge production. CLM-1 supplies the consequential knowledge/disclosure claim; CLM-2 supplies reported performance. Missing candidate traces and excluded extensions prevent observed acceptance, integration and causality. The outside-host boundary and unassessed evaluator/formula details are those in Boundary and evidence; no system-complete epistemic grade is attempted.

#### 2. Epistemic-object inventory

Canonical identity, form, lineage and endpoints remain on the named records. This overlay identifies the truth-apt parts and their warrant limits.

| Object | Candidate content and role | Epistemic limit |
|---|---|---|
| OBJ-1 | Operational configuration; see RTE-2 | Settings choose behavior, not evidence of truth |
| OBJ-2 | Generated claims answering a benchmark question; see RTE-4 | No particular answer or derivation trace inspected |
| OBJ-3 | Reference-fit score and metrics | A score is evidence under its criterion, not a criticism of an identified theory |
| OBJ-4 | Claims that extracted link names resolve or fail to resolve | Limited to parsed names and the resolver's ambiguity rule |
| OBJ-5 | Authored/imported facts, session-derived explanations and reasons | Warrant depends on source and producing agent; no automatic attestation |
| OBJ-6 | Project context and descriptions may assert goals/facts; template instructions are policy | Copying preserves bytes, not source truth; updated context can carry revisions |
| OBJ-7 | Retrieval terms, counts and scores; no new subject-matter claim | Retrieval probe warrants a limited search result, not a note's truth |
| OBJ-8 | Canvas prose can contain imported claims; settings/filters/bookmarks are operational | Separate content from selection directives; no content evaluator is supplied |
| OBJ-9 | Derived rows, counts and formula results from stored metadata | Derivation is only as sound as input, encoding and formula interpretation; full formal correctness uninspected |
| OBJ-10 | Marked generalization inferred by a distilling agent | Ampliative candidate generation is afforded; acceptance not established |

#### 3. Authority-route ledger

Architectural status is independent of the result's conclusion statuses. Each row below has one function. Triggers, endpoints, raw evidence anchors and recovery are on its canonical route/object; the table adds the evaluator, license and consequence. No row asserts observed activation.

| Route/function | Architectural status | Target and content/update relation | Condition and operative result | Epistemic authority; operational/behavioral force | Claim and limit |
|---|---|---|---|---|---|
| RTE-6 — retention | implemented | OBJ-5, OBJ-6, OBJ-8; acquisition/import of supplied content | Caller issues a valid write; collision rules may refuse, explicit overwrite may replace | No truth license; changed bytes become eligible for BAP-3/BAP-4 | CLM-1; source warrant unknown |
| RTE-7 — content transformation | implemented | OBJ-7, OBJ-9; non-ampliative reshaping of files/metadata, plus symbolic view derivation | Requested operation compiles current source/cache data | License only the implemented projection over inputs; BAP-4 routes/ranks later access | CLM-1; no semantic summary or source-truth test |
| RTE-7 — check/evidence production | implemented | OBJ-7 proposed search handle; no content change | Search probe asks whether the note is among top hits | Local retrieval evidence; does not certify all alternatives or note truth | CLM-1; fallback and roster alternatives remain |
| RTE-7 — disposition/acceptance | implemented | OBJ-7 handle; no content change | Validated candidate preferred, top candidate fallback and roster completion permitted | Operational selection for the map; no epistemic acceptance of subject matter | CLM-1; universal “validated” interpretation is too strong |
| RTE-7 — operational admission/selection/consumption | implemented | OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9; no content change | Requested query/view/read returns selected content | BAP-3 supplies advice/instruction to external agent, BAP-4 controls ranking | CLM-1; delivery is not activation |
| RTE-5 — check/evidence production | implemented | OBJ-4 and note wikilinks; no content change | Current parsed target resolves or enters unresolved report | File-reference resolution only; caller can repair; no automatic write rejection | CLM-1; no factual warrant |
| RTE-8 — content transformation | doctrine only | OBJ-5 from session material; preservation/extraction can be non-ampliative, OBJ-10 is ampliative conjecture | Agent selects reusable findings and marks drawn generalizations | Candidate formation and instructed attribution; BAP-5 shapes prose | CLM-1; no run demonstrates faithful extraction |
| RTE-8 — disposition/acceptance | doctrine only | Candidate note or update; no content change | KEEP/SKIP judges surprise and reuse; agent compares existing note and may name contradiction | Operational permission to retain, not an evidence-consuming truth acceptance of the inferred claim | CLM-1; utility criterion does not license truth |
| RTE-8 — retention | doctrine only | OBJ-5, OBJ-6, OBJ-10; no content change at this function | Skill directs writes through implemented RTE-6 | Durable availability for BAP-3; no post-acceptance lifecycle integration established | CLM-1; no instance observed |
| RTE-9 — content transformation | doctrine only | OBJ-5, OBJ-6; intended non-ampliative merge/repair, actual preservation indeterminate | Agent reads overlapping or superseded notes and edits | Curation criterion governs retention and later access; BAP-3/BAP-4 | CLM-1; no candidate-linked semantic-preservation evidence |
| RTE-9 — disposition/acceptance | doctrine only | Notes/templates; no content change | Agent can decline uncertain merges; user decides template schema | Operational veto/permission, not endorsement of all note claims | CLM-1; no independent content oracle |
| RTE-10 — operational admission/selection/consumption | doctrine only | OBJ-6; no content change | Active project context supplied each session | BAP-3 affords instruction/advice for that session | CLM-1; extension implementation unavailable |
| RTE-11 — content transformation | implemented | OBJ-5, OBJ-6 from dataset; acquisition/import and non-ampliative formatting | Question corpus assembled from paragraphs/dialogue and externally supplied summaries | Preserves indicated lineage, but source truth is not newly checked | CLM-2; imported summaries are not Napkin synthesis |
| RTE-4 — check/evidence production | implemented | OBJ-2 evaluated into OBJ-3; no change to answer content | Dataset answer and matching/model/F1 rules produce score | Answer-fit evidence only; used in benchmark metrics through BAP-2 | CLM-2; no memory intervention or theory revision |
| RTE-2 — operational admission/selection/consumption | implemented | OBJ-1; non-truth-apt settings update | Injected configuration overrides file settings and rejects configSet | BAP-1 enforces that API's ownership rule | None; does not constrain direct edits/other instances |
| RTE-3 — operational admission/selection/consumption | implemented | Package; non-truth-apt software update | npm installs selected latest; subprocess exit governs report | Changed executable availability, no epistemic license | None; no improvement test |

There is no evidenced acceptance transition for the truth of OBJ-10 within the inspected skill/core boundary. This is an unreached evidential link, not proof that a host never performs such reasoning. The instructions' data-only trust boundary and inferred marker are policies; note text returned by RTE-7 is not generally neutralized by the core.

#### 4. Per-object lifecycle disposition

For OBJ-10, transformation is ampliative conjecture. Every observed candidate state is **no instance observed**, independently of architectural status:

| Phase | Routes and architectural status | Evaluator/criterion and scope | Evidence |
|---|---|---|---|
| Observation/anomaly | RTE-8; doctrine only | Session contains non-obvious fix, behavior, decision or reusable procedure | SRC-2 `skills/distill/SKILL.md:20-47` |
| Conjecture | RTE-8; doctrine only | Generalization explicitly marked inferred | SRC-2 `skills/distill/SKILL.md:109-112` |
| Derived consequence | RTE-8; not determinable | No required consequence derivation for this inferred claim; host reasoning excluded | Same skill boundary; no linked candidate trace |
| Test/evidence | RTE-5; implemented for links; RTE-8; not determinable for conjecture content | Link resolution does not test the inferred proposition; actual semantic test uninspected | SRC-1 `src/core/links.ts:17-40`; SRC-2 `skills/distill/SKILL.md:118-126` |
| Acceptance | RTE-8; not determinable | KEEP/SKIP permits useful note retention; no candidate-specific epistemic criterion/use scope established | SRC-2 `skills/distill/SKILL.md:20-35` |
| Lifecycle integration | RTE-8, RTE-7; not determinable | Storage/read-back is present, but post-acceptance connection cannot be inferred | RTE-6, RTE-7, RTE-8 evidence |

OBJ-5's imported/copied-fact branch and OBJ-6's copied templates/context use acquisition or non-ampliative reshaping; discovery lifecycle is not applicable to those transformations. Warrant is inherited only to the extent the source and transformation support it; no supplied truth certificate was inspected. The semantically rewritten note branch in RTE-8 and RTE-9 is **indeterminate** between preservation, warranted derivation and new conjecture unless an actual input/output pair establishes the relation. Its retained lineage is topic note, reasons where supplied, tags and links; storage and link checks do not settle semantic preservation. OBJ-10 separately captures the explicitly novel branch.

OBJ-2 is **indeterminate**: an answer may retrieve, compute, infer or guess. RTE-4 can score reference fit, but without a candidate trace cannot classify production or post-acceptance integration. OBJ-3 and OBJ-4 are non-ampliative evidence records under bounded evaluators; discovery lifecycle is not applicable. OBJ-9 is a mechanically derived projection whose displayed values are warranted only relative to source metadata and inspected query semantics; end-to-end formula correctness remains uninspected. Canvas prose within OBJ-8 retains an acquisition/update disposition like OBJ-5; the policy/settings remainder is not truth-apt content.

No lifecycle record for OBJ-1: no candidate truth-apt output for this operational settings object; relevant update route is RTE-2. No lifecycle record for OBJ-7: no subject-matter candidate truth-apt output for this access structure; relevant selection/check route is RTE-7. The same no-candidate disposition applies to the template-instruction and filter/bookmark subparts of OBJ-6 and OBJ-8; their factual prose parts were disposed separately above.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design | Implemented support | Observed/causal support | Supported conclusion and mismatch |
|---|---|---|---|---|
| CLM-1 | Progressive disclosure; distill/tend instructions and documented context integration | RTE-6 and RTE-7 retain/return memory; RTE-5 checks links; RTE-8 and RTE-9 have usable primitives | No executed candidate/behavior trace; no causal comparison | File-based knowledge access is implemented. Knowledge production, universal keyword validation, enforced token caps and autonomous extraction are not established |
| CLM-2 | Benchmark README reports comparative answer scores | RTE-4 and RTE-11 expose corpus construction, host invocation and scoring | Reported outcome only; missing extension and raw run evidence | The package includes an inspectable evaluation design, but no attribution of improvement to recalled content or isolated component follows |

#### 6. Bounded conclusion

Napkin acquires and retains claims, reshapes access structures and lets selected material reach later consumers. The distill instruction affords candidate explanations/generalizations and asks writers to expose contradictions and reasons; tend affords conservative maintenance. Link checks, keyword probes, CRUD collision checks and benchmark answer scoring have distinct targets and licenses. None substitutes for an observed content-directed criticism and acceptance route for a retained inferred claim. Operational use can precede epistemic acceptance, and the record keeps those separate.


## Reconciliation

The fresh worker report is bound to this run, repository, full commit and unchanged frozen input hash; report status is complete and its final bytes match the recorded digest. The coordinator retains source-native records and per-value comparison bases. The local epistemic lens was applied to the same sources, with no prior review read.

| Specialist proposal | Canonical record | Disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-5 | Adopted with source anchors and limits |
| MEM-OBJ-2 | OBJ-6 | Adopted with source anchors and limits |
| MEM-OBJ-3 | OBJ-7 | Adopted with source anchors and limits |
| MEM-OBJ-4 | OBJ-8 | Adopted with source anchors and limits |
| MEM-OBJ-5 | OBJ-9 | Adopted with source anchors and limits |
| MEM-RTE-1 | RTE-6 | Adopted with source anchors and limits |
| MEM-RTE-2 | RTE-7 | Adopted with source anchors and limits |
| MEM-RTE-3 | RTE-8 | Adopted with source anchors and limits |
| MEM-RTE-4 | RTE-9 | Adopted with source anchors and limits |
| MEM-RTE-5 | RTE-10 | Adopted with source anchors and limits |
| MEM-RTE-6 | RTE-11 | Adopted with source anchors and limits |
| MEM-ABS-1 | ABS-2 | Adopted with source anchors and limits |
| MEM-ABS-2 | ABS-3 | Adopted with source anchors and limits |

OBJ-8 includes configuration as a named subpart; its already registered detail is OBJ-1, with RTE-2 owning configuration admission. RTE-1 owns generic dispatch; RTE-7 owns memory selection and delivery. RTE-4 owns benchmark scoring and cleanup; RTE-11 owns benchmark import/consumer interfaces. RTE-5 owns deterministic link evidence, while RTE-9 owns agent disposition and repair. No record changed referent and no proposal ID was reused.

All specialist integration qualifications are retained: external extensions stay outside inspected implementation; push and extraction stay afforded; temporary SQLite is an access projection; token sizes are design targets; keyword fallback limits universal validation; the three benchmarks do not share identical preprocessing; and source-level harness/skill mismatches are limitations, not observed failures. The core uses log-damped inbound counts rather than the design document's PageRank wording; access-frequency promotion and built-in distill remain bounded absences (ABS-2). The create-path example mismatch is recorded on RTE-8, and the scorer signature mismatch on ABS-3. No correction to the specialist's substantive classification was needed. Its requested absence-boundary clarification was completed in the report before digest binding. Independent source inspection converged on keyword fallback and the absent benchmark extension; other integrated memory judgments remain specialist findings, not independent clearance.


## Bounded synthesis

Napkin makes ordinary Markdown files usable as incrementally retrieved agent memory. The CLI and SDK give the caller an overview, ranked search and full reads while retaining the same editable content for human tools. The practical responsibility boundary is clear: Napkin executes access and mutation; the external agent supplies the problem, chooses retrieval, interprets content and determines semantic revisions. Its configuration injection and software-update routes govern different kinds of change and offer no independent memory-truth guarantee.

Its strongest epistemic contribution is a combination of inspectable material, retrieval controls, explicit writing/maintenance instructions and bounded checks. Structural link checking licenses file resolution; keyword probing guides retrieval handles; neither licenses the truth of the selected note. Distill explicitly separates inference from what a session established, and asks that contradictions be stated when merging. Those are useful criticism affordances, but a delivered note or successful write is not an accepted claim produced by a demonstrated discovery lifecycle.

For theory-builder conditions 1–4, the analysis separates the links. Condition 1, localized content: afforded by declarative notes and explicit inferred claims. Condition 2, consumption: afforded by the named later-agent retrieval workflow; content-dependent behavior in an executed round is uninspected. Condition 3, content-directed criticism: afforded by the instruction to name a contradiction between a new finding and an existing note; actual formulated criticism, blame assignment and revision are uninspected. Condition 4, iteration: uninspected as a working criticism-to-next-round process; retention and later access provide a path but no candidate-linked next round was observed. Persistence is wired for files across invocations and afforded across project sessions; the persistence of a specific criticism used by a later round remains uninspected. Addressability is afforded at the note/section level, with inferred claims locally marked, but no schema requires assumptions and scope to be separately represented. Theory-builder membership therefore remains uninspected at the selected artifact boundary; it is not disproved by inaccessible host reasoning.

Learning: the strongest supported contribution is reusable material and the ability to revise it from session findings. Improved capacity attributable to criticism of a consumed theory remains uninspected: no retained comparison in this boundary links such criticism to later ability. The memory profile's trace-learning category describes a write route, not this stronger learning claim. Reported retrieval benchmark scores bear on combined answering performance under their evaluator; they do not demonstrate learning from distill/tend or identify Napkin's isolated causal effect.

Reflection: afforded for host-mediated maintenance of the vault's own organization—overview/link reports represent current notes, the host can interpret those reports and revise the represented vault, and later access can see revisions. Closure of that route inside a deployed host and a reflective theory builder's criticism of its own method texts remain uninspected. Autonomy: uninspected for a complete theory builder; the agent is instructed to make local content decisions, humans can edit directly and retain template-schema decisions, and the inspected artifact does not fix who performs every criticism/selection step. Self-improvement: an evidence-responsive maintenance pathway is afforded, aimed at reusable knowledge and cleaner access; an occurrence in which a retained change caused later behavior is uninspected. These are separate findings, not stages of one grade.

For a scenario requiring inspectable local memory and agent-directed retrieval, the code establishes the access surface and the skill establishes a disciplined use protocol. For a scenario requiring automatically selected context, demonstrated maintenance compliance, truthful synthesis or reliable improvement, the missing host implementation and execution evidence are decisive limits. Pinned extension source, linked candidate/criticism/revision/read-back traces, or controlled comparisons of recalled content would change those assessments. No product ranking or transfer recommendation follows.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| Host and context-extension internals excluded | CMP-2, ABS-1, RTE-4 | Pinned tree and external call sites | Complete push selection, runtime permissions, deployed behavior | Pinned host/extension source and configuration |
| No executed agent or curation trace | CLM-1 and integrated memory routes | Shipped code, docs and skills | Activation, criticism iteration, faithful recall, occurrent self-improvement | Retained candidate-linked operations and later consumer trace |
| Benchmark results are reported | CLM-2, RTE-4 | Benchmark source and README | Reproduction, causal component effects or learning improvement | Raw run outputs, fixed dataset/model/extension and designed comparison |
| Provider identity and training opaque | CMP-2 | Model names at invocation boundary | Exact weights or weight updates | Provider-resolved version and training evidence |
| Specialized view and benchmark branches not exhaustive | RTE-1, RTE-4 | Core memory path and LongMemEval representative | Whole-package security assurance or evaluator equivalence | Separate inspection of base/formula/canvas, other harnesses and dependencies |

## Verification and blockers

### Semantic verification

Run/source/boundary identity, full canonical identifiers and report input/hash were checked. The result retains each adopted specialist finding and its relevant source quotes without depending on the local report. The comparison scope covers accumulated notes/context/templates, structured content and access structures; static scaffolds and external implementation internals are excluded. OBJ-1 is the settings subpart of OBJ-8, not an omitted alternative. RTE-7 covers lexical/full/structured requested reads; RTE-10 alone supplies the documented push signal (active vault → fixed NAPKIN.md each session). No query/file identifier from pull was misclassified as push.

Every scoped trace-fed write was checked: RTE-8 qualifies at afforded strength with session-log input, cross-task/per-project horizon, current-session/session-end timing and prose plus operative metadata. RTE-11 preserves or imports raw dialogue and external summaries, so it does not upgrade extraction to wired; OBJ-7 compilation and OBJ-9 SQL projection are access transformations. ABS-2 bounds the lack of a core compaction/extraction route; excluded extension internals are not silently classified. Each known aggregate preserves all scoped alternatives and per-value strengths, including transient SQLite and coarse documented push. Faithfulness is a bounded evidence negative (ABS-3), not a failed behavioral test.

The semantic licenses were checked separately from source matching: keyword fallback and roster paths limit CLM-1, link existence does not certify truth, and benchmark score does not demonstrate learning or causal reliance. The theory-builder, learning, reflection, autonomy and self-improvement findings state their separate evidence limits. Reconciliation names all proposal mappings and material qualification dispositions; no unresolved substantive integration conflict remains.

### Deterministic validation

The typed result `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-napkin-03/result.md` passed the supported frozen-source verification command with exit status 0. Its source quotes/ranges match the pinned blobs. The bound specialist report also passed typed validation and frozen-source verification. These deterministic checks establish structure and identity, not independent semantic clearance.

### Blockers

none
