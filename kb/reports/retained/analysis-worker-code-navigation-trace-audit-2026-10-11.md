# Analysis worker code navigation trace audit — 2026-10-11

## Result and retention purpose

Recent analysis workers already use searches and bounded source reads. The observed need is better target selection and cross-file navigation, not simply replacing whole-repository reading with signatures. File outlines, symbol-sized implementation reads, and reference lookup are plausible improvements. These traces do not establish that any tool supplies those improvements reliably or reduces analysis cost.

Retain this dated observation for the operation of selecting and evaluating code-navigation support for `analyse-agentic-system`. The operator requested inspection of recent agent traces, retention of the findings, and a language census of previously covered systems. The census supports coverage priorities; it does not require one universal tool or a separate tool for every language. This report is not a correctness audit, an adopted method change, or authorization for installation or new analysis runs.

## Inputs and observation boundary

Inspection date: 2026-10-11. Auditor: `openai/gpt-6.1-sol`, reasoning level `medium`, in Pi. The commission was to inspect what recent analysis agents search for, following a discussion of compact code structure extraction and existing navigation tools. The later request was: “save this as a retained report”.

Four coordinator sessions supplied embedded worker transcripts. Select only subagent results whose task names an analysis handout at `handouts/<attempt>-<job>/prompt.md`. This excludes launch diagnostics and subsequent audit workers. Worker transcripts are in each selected tool result's `message.details.results[].messages`; they are not separate child-session archives.

| System | Run ID | Selected worker invocations | Source revision |
|---|---|---:|---|
| Letta Code | `AAS-2026-10-11-letta-code-88afa3263646-01` | 12 | `271f119dcf37d58649a18e6c733386b3c710a456` |
| Graphiti | `AAS-2026-10-10-graphiti-85a21a06d35c-01` | 10 | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| Napkin | `AAS-2026-10-10-napkin-b831630d0978-01` | 13 | `7582d6a46f5a11995956e60a59c41a5b242109f1` |
| Letta | `AAS-2026-10-11-letta-d460b458ddad-01` | 1 | `5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a` |

All 36 selected worker results record model `gpt-6.1-sol` and thinking level `medium`. Counts include repair and reverification invocations; they are not counts of distinct roles or independent experiments. The Letta run stopped at the boundary and supplies no implementation-reading case. Letta Code is a separate system and run.

The inspected worktrees had these HEAD revisions when this report was prepared:

- Letta Code: `0265fff4dd8a9d00fa2aba78495b2c95b2abbad6`.
- Graphiti, Napkin, and Letta: `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad`.

These are observed worktree HEADs, not an independent audit of the engine's pinned method record. Different method revisions are not pooled to estimate a common error rate or causal effect.

### Local trace locators

Directory: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/`.

| System | Coordinator JSONL filename |
|---|---|
| Letta Code | `2026-10-11T07-51-46-718Z_01a129f2-491e-711e-8a12-57ed0373030a.jsonl` |
| Graphiti | `2026-10-10T22-09-14-881Z_01a127dc-f680-711e-8a12-57e725ff77d1.jsonl` |
| Napkin | `2026-10-10T22-10-09-558Z_01a127dd-cc16-745a-b8d3-80ae1386ab9d.jsonl` |
| Letta | `2026-10-11T06-44-36-040Z_01a129b4-c847-711e-8a12-57e9467dd961.jsonl` |

The measurements and representative queries below are retained here so that the result remains understandable without these local files. Reproduction requires the original session files. They are local evidence locators, not durable repository links; this report does not authorize deleting them.

## Method and counting rules

The inspection extracted `read` and `bash` tool-call arguments from selected workers and examined representative source-exploration sequences. It counted calls deterministically across all selected workers, including later report verification. It did not inspect every reasoning passage or establish whether each read was necessary.

For the measurements:

1. Parse each coordinator JSONL record and inspect `message.details.results` when present.
2. Select a result when its task matches `handouts/\d+-[^/]+/prompt.md`.
3. Within its `messages`, inspect assistant content items with `type: toolCall`.
4. Count a direct source read when the tool is `read` and its `path` contains `related-systems/`.
5. Count a code read when that source path ends in `.py`, `.ts`, `.tsx`, `.js`, `.rs`, or `.ipynb`.
6. Count a bounded code read when its `limit` argument is non-null. Count a noninitial code read when `(offset or 1) > 1`.

A limit is a requested line bound, not proof that the read was small or that it returned that many lines. The extension filter is operational: it counts Python prompt strings as code, but not separate Markdown prompts. It excludes code returned through shell commands and code extracted into scratch files. Calls are counted, not unique files, unique lines, tokens, or cost.

## Measurements

| Run | All direct read calls | Direct source reads | Code reads | Bounded code reads | Noninitial code reads |
|---|---:|---:|---:|---:|---:|
| Letta Code | 371 | 128 | 116 | 111 (96%) | 72 |
| Graphiti | 304 | 117 | 108 | 100 (93%) | 76 |
| Napkin | 419 | 172 | 136 | 87 (64%) | 60 |
| Letta, boundary stop | 14 | 5 | 0 | 0 | 0 |

“All direct read calls” includes instructions, handouts, reports, and other non-source material. The gap between that column and source reads must not be interpreted as unnecessary reading. Code-navigation tools do not directly replace those other inputs.

Most implementation-reading calls in Letta Code and Graphiti were already bounded. The observed sequence was frequently filename or text search, then a line-range read, then a search for the next mechanism. Napkin had more unbounded calls, but this inspection did not establish the returned file sizes or whether whole-file reads were justified.

## Observed navigation tasks

### N1. Find the active implementation, not merely an interface

Letta Code's boundary worker searched CLI entry points, subcommand routing, backend selection, and executor creation. Its queries included `entrypoints`, `src/index`, `standalone`, `headless`, `createLocal`, `local-backend`, `api-backend`, and `function getBackend`.

The runtime worker then searched execution, approvals, persistence, hooks, subagents, channels, and scheduling. It made 35 code reads. A representative query combined:

```text
execute | permission | approval | sendMessage | while | stop_reason
```

The sequence indicates a need to distinguish reachable execution paths and follow their boundaries. File outlines could locate definitions, while reference lookup could help follow calls. Neither would independently prove which configuration activates a path.

Evidence: Letta Code trace L19, job `000003-boundary`; L23, job `000005-runtime`.

### N2. Trace retained content into a model request

Letta Code's memory worker first located memory, compaction, reflection, and skill files. It searched:

```text
compile | git | pinned | limit | summary | checkpoint | compact
```

It read prompt compilation, local storage, memory formatting, reflection completion, transcript search, and memory-worktree handling. Later it searched for:

```text
consumeSkillContent | takeSkillContent | drainSkillContent | skillContent
```

across approval execution, headless execution, and message construction. This is a path-to-consumer question: finding memory storage or a retrieval interface alone does not answer it. The worker made 32 code reads, plus separate source-document reads.

Evidence: Letta Code trace L27, job `000007-memory`. The same coordinator line also contains the separate epistemic worker; distinguish them by their task handout.

### N3. Trace ingestion, retrieval, persistence, and runtime calls

Graphiti's runtime worker searched declarations alongside runtime dependencies:

```text
async def | def __init__ | llm_client | runtime | add_nodes_and_edges_bulk
```

It inspected ingestion routes, queue services, LLM clients, search, bulk persistence, and an example agent. The memory worker inspected raw episode retention, summaries, temporal invalidation, schema limits, and retrieval outputs. These are related implementation paths, not one API-surface inventory.

The runtime worker also parsed `examples/langgraph-agent/agent.ipynb` and wrote its code cells into a scratch text file before reading them. Notebook code-cell extraction is a distinct compact-reading need that ordinary class/function outlines may not cover. That scratch-file read is outside the code-read counts above.

Evidence: Graphiti trace L27, job `000005-runtime`; L31, job `000007-memory`.

### N4. Approximate outlines with regular expressions

Napkin's memory worker searched exported definitions and method-like declarations before reading ranking, caching, CRUD, SDK, and benchmark implementations. Representative patterns included:

```text
export | contextPath | cached | PROBE_K | rank\( | saveOverview
^  [a-zA-Z]
```

It also searched CLI action and command declarations. These queries approximate a structural outline. A parser-based outline could replace some of this navigation without requiring a whole-repository packed artifact.

Evidence: Napkin trace L26, job `000007-memory`. The epistemic worker shares that coordinator line but is a separate result.

### N5. Inspect conditions and judgments that signatures omit

Workers searched implementation-level conditions as well as definitions:

- Letta Code: approval blocking, reflection merge/conflict conditions, prompt recompilation, compaction fallbacks, and hook behavior.
- Graphiti: contradiction and duplicate handling, temporal invalidation, summary updates, evaluation prompts, and candidate comparisons.
- Napkin: ranking, cache behavior, benchmark scoring, and what evaluation inputs expose.

A signature-only view would omit much of the evidence sought. Retrieval must preserve an easy route to exact source, including Markdown prompts and prompt strings within code.

Evidence: Letta Code L23 and L27; Graphiti L31 and L32; Napkin L26 and report verification at L34 and L46.

## Repeated reads and independent verification

The most frequently read files included:

| Run | File, relative to its source checkout | Direct code-read calls |
|---|---|---:|
| Graphiti | `graphiti_core/graphiti.py` | 24 |
| Napkin | `src/core/overview.ts` | 16 |
| Letta Code | `src/backend/local/local-backend.ts` | 10 |

These are file-level repetitions, not measurements of duplicated line ranges. Different workers often inspect different portions of the same file. Report-verification workers also deliberately revisit source. The counts do not justify eliminating independent evidence checks or sharing analyst conclusions through a navigation index.

Later profile, synthesis, and verification stages also consume substantial instruction and report material. Improving source navigation would address only part of the workflow's reading volume.

## Language coverage census — 2026-10-11

### Historical records and selected population

The historical corpus remains in several locations:

| Location | Observed artifacts |
|---|---:|
| `kb/agent-memory-systems/reviews/` | 159 Markdown files, including superseded copies |
| `kb/agent-memory-systems/lightweight/` | 8 document-grounded reviews |
| `kb/agentic-systems/reviews/` | 12 reviews |
| `kb/agentic-systems/reviews-archive/` | 44 Markdown files, including navigation |
| `kb/agentic-systems/reports/retained-archive/` | 64 historical run directories |
| `kb/agentic-system-analyses/retained-archive/` | 1 archived member-document set |

These are artifact counts, not distinct system counts. Historical reviews and results remain evidence at their recorded boundaries, not inputs to new source analyses.

The census selected 210 review records from the three review directories, excluding `README.md` and filenames containing `.replaced.`. It added the archived member set and the recent Letta Code target, for 212 population records. The lightweight directory and all 64 archived result directories were not separately assayed for additional repository identities. This is a practical coverage sample, not an exhaustive archive census.

Repository matching used source-directory references and explicit repository/source lines within each review's first 40 lines; otherwise it used GitHub commit/blob links in that region. A second pass matched `source-identity` fields for initially unmatched reviews. Matches used cached Git origins. The archived member set used GitHub links in its overview's first 60 lines. Repository aliases were deduplicated by normalized GitHub origin, retaining the alias with the most recognized source files. This metadata heuristic was not manually adjudicated for every record; an early supporting-source citation can select an additional repository.

Of the 212 population records, 207 matched local sources, yielding 197 distinct repository identities. The five unmatched records were ATLAS and kgai, whose local repositories were unavailable, and the document-grounded Claude Code dynamic workflows, AIDE2, and WikiSkill records. A multi-repository system can contribute several repositories; repeated reviews do not multiply the same origin's weight.

The [language census data](./analysis-worker-code-navigation-language-census-2026-10-11.json) retains the population-to-checkout mapping, deduplicated repository identities, committed HEADs, per-language counts, and counting filters. It is the measurement payload for this section, not a source-system analysis.

### Counting method and boundary

Final counts used `git ls-tree -r -z HEAD`, not checked-out files. Some cached repositories have Git history but no source working tree. Count regular blob entries by registered filename extension; exclude symlinks, non-blob entries, and common dependency/build directories. Group `.ts`/`.tsx` as TypeScript, `.js`/`.jsx`/`.mjs`/`.cjs` as JavaScript, `.py`/`.pyi` as Python, and the C/C++ extensions as one group. The full extension map is retained in the census data. Extensionless scripts and unregistered languages are not counted.

The measurements describe the cached repositories' committed HEADs recorded in the payload, not historical reviewed revisions. Files are not lines, bytes, tokens, implementation complexity, or estimated worker effort. Generated files are not systematically excluded. Language-server or parser support was not tested.

An initial filesystem count missed unmaterialized sources. A subsequent blob-content count triggered Git lazy object fetching in partial clones and timed out. The final tree-only count avoided source-content retrieval. Git downloaded objects and performed reported automatic packing during the abandoned attempt; no source file was edited or checkout restored. Those partial counts are not the results below.

### Distribution by repository and file count

197 repositories were matched. 189 contained recognized source files; 8 did not. Absence under this extension filter does not establish absence of implementation.

| Language | Repositories containing it | Repositories where it has most files | Source files | Share of source files |
|---|---:|---:|---:|---:|
| Python | 143 | 107 | 45,282 | 45.4% |
| TypeScript | 87 | 48 | 40,869 | 41.0% |
| Rust | 30 | 13 | 3,395 | 3.4% |
| Go | 17 | 11 | 4,003 | 4.0% |
| Shell | 119 | 8 | 3,061 | 3.1% |
| JavaScript | 95 | 2 | 1,794 | 1.8% |
| C/C++ | 17 | 0 | 864 | 0.9% |
| Other recognized languages/formats | overlapping counts | 0 | 522 | 0.5% |
| **Total** | **189 distinct repositories** | **189** | **99,790** | **100%** |

Presence counts overlap and can reflect one helper script. Largest-language counts use file counts, with ties resolved by Git-tree traversal insertion order. C/C++ can have large files despite being no repository's largest group by file count. These columns must not be read as semantic coverage or effort estimates.

| Supported language set | Repositories whose largest language is supported | Share of source files |
|---|---:|---:|
| Python | 107/189 (56.6%) | 45.4% |
| Python + TypeScript/JavaScript | 157/189 (83.1%) | 88.1% |
| Those + Rust | 170/189 (89.9%) | 91.5% |
| Those + Go | 181/189 (95.8%) | 95.5% |

A repository counted in the second column can still contain unsupported languages. These are coverage priorities, not a guarantee that a tool can analyse the repository.

### Sensitivity and non-code formats

An additional directory/filename filter excluded conventional tests, fixtures, examples, benchmarks, documentation, the named legacy Pi directory, and `.test.*`/`.spec.*` files. It left 65,777 source files. This is a rough filter, not a production-code classification; it retains some tests and generated code.

| Supported language set | Share of filtered source files |
|---|---:|
| Python + TypeScript/JavaScript | 86.1% |
| Those + Rust | 90.1% |
| Those + Go | 96.1% |

All 197 repository trees contained Markdown, 12 contained notebooks, and 37 contained SQL files. These formats are counted separately from language files. The result supports preserving document and exact-text reading alongside code navigation.

## Implications for tool selection

The observed tasks support testing these capabilities, in this order:

1. Locate a symbol and retrieve its implementation as a bounded unit.
2. Find references to follow a mechanism across files.
3. Obtain a scoped file or subsystem outline, including exports and declarations.
4. Retain text search for prompt wording, configuration keys, SQL, and behavioral conditions.
5. Extract notebook code cells when examples are part of the evidence.

The census makes Python and TypeScript/JavaScript the initial coverage priorities, with Rust and Go important for broader coverage. This does not select an architecture. The operator explicitly allowed several tools, potentially one per language. A small combination could expose structural navigation through one route and semantic navigation through language-specific backends; several direct language-specific tools could also supply those capabilities. Tool setup, indexing, worker delivery, and tool-description overhead remain unmeasured.

The preceding conversation named Repomix, Serena, and Pitlane as possible candidates. They are untested candidate names here, not evidence for this report's findings or endorsed capability claims. This report does not retain the external-tool survey or benchmark its tools.

A bounded pilot could compare existing search/range-reading with navigation tooling on observed questions: Letta Code memory compilation and Graphiti ingestion-to-model-context paths. Its intended outcome would be lower navigation effort or returned source volume without missed controlling conditions or weaker citations. This is a proposal, not an executed comparison or a binding procedure.

Any separately authorized pilot should preserve the frozen source boundary, place derived state outside it where possible, and verify that each worker receives the selected tools. A generated map or inferred path remains a navigation aid; original pinned source remains the evidence for behavior.

## Limits and disposition

- This is a small, selected recent sample, not a representative survey of all analysed systems.
- Gbrain, Pi, and Rust-system worker traces were not inspected. The report cannot establish their navigation patterns.
- Different method revisions and system sizes prevent causal comparison of the aggregate counts.
- The counts exclude shell-returned code, notebook scratch reads, and some source-document formats. They are not total context-volume measurements.
- A high bounded-read proportion does not establish efficient target selection. An unbounded read does not establish waste.
- Repeated file reads do not establish repeated evidence or unnecessary independent verification.
- Search intent is inferred from query wording and adjacent reads. This is an auditor interpretation, not direct measurement of worker comprehension.
- No navigation tool was installed, exercised, or compared. Savings, indexing overhead, reference accuracy, and missed mechanisms remain unknown.
- The language census is a metadata-selected repository sample at cached committed HEADs, not an exhaustive system census or reconstruction of reviewed revisions. File counts do not measure reading cost.
- This inspection did not reopen analyses, edit the method, restore working trees, edit source files, or change run state. The census's abandoned content-count attempt did change Git object caches through lazy fetching and automatic packing, as recorded above.

Disposition: retain the observation as evidence for a separately commissioned tool-selection pilot. Do not turn it into a general rule that workers must read signatures first or that implementation reading should be reduced.
