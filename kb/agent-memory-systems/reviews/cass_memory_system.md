---
description: "cass-memory review: file-backed procedural memory for coding agents with cass session search, diary summaries, LLM reflection, scored playbook rules, MCP tools, and trauma guards"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# cass_memory_system

cass-memory, by Dicklesworthstone, is a Bun/TypeScript CLI and HTTP MCP server for turning AI coding-agent sessions into procedural memory. At the reviewed commit it reads raw session history through `cass`, writes structured diary JSON, reflects over those diaries with an LLM to propose playbook deltas, deterministically curates YAML playbook rules with scoring/decay/anti-pattern handling, serves task-specific context through CLI/MCP calls, and can install a trauma guard that blocks commands matching retained safety patterns.

**Repository:** https://github.com/Dicklesworthstone/cass_memory_system

**Reviewed commit:** [4d76f61969cbc382a030bdcaab2cdd159058fcfe](https://github.com/Dicklesworthstone/cass_memory_system/commit/4d76f61969cbc382a030bdcaab2cdd159058fcfe)

**Last checked:** 2026-06-04

## Core Ideas

**The durable memory target is a procedural playbook, not raw recall alone.** The README describes three layers: raw sessions in `cass`, diary summaries, and playbook bullets; the source model makes that concrete with `DiaryEntrySchema`, `PlaybookBulletSchema`, feedback events, maturity, provenance fields, and defaults for `~/.cass-memory/playbook.yaml` and `~/.cass-memory/diary` ([README.md](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/README.md), [src/types.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/types.ts)).

**Reflection is LLM-proposed but curator-governed.** `orchestrateReflection()` discovers unprocessed sessions, creates diaries, asks `reflectOnSession()` for deltas, validates add-deltas against historical evidence, then locks and reloads the global/repo playbooks before applying deterministic curation ([src/orchestrator.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/orchestrator.ts), [src/reflect.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/reflect.ts), [src/validate.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/validate.ts), [src/curate.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/curate.ts)). That split is the system's strongest quality-control design: generative extraction is allowed, but merge, dedup, feedback, inversion, promotion, demotion, and persistence are code paths.

**Read context is task-bounded and score-ranked.** `cm context` loads the merged playbook, filters workspace-scoped bullets, optionally embeds the query and bullets, falls back to keyword scoring, searches `cass` history with a bounded query, and returns limited `relevantBullets`, `antiPatterns`, `historySnippets`, warnings, suggested queries, and degraded-mode metadata ([src/commands/context.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/commands/context.ts), [src/semantic.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/semantic.ts), [src/cass.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/cass.ts)). Context efficiency is therefore explicit: top-k limits, history limits, workspace filters, decay-weighted effective scores, semantic/keyword scoring, snippet truncation, and JSON/TOON output modes bound both volume and parsing complexity.

**Feedback changes future ranking and survival.** Manual marks, outcome records, context logs, inline feedback comments, and auto-classified session outcomes become feedback events on rule bullets; scoring applies half-life decay and a harmful multiplier, while curation can invert repeatedly harmful rules into anti-patterns or retire them ([src/outcome.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/outcome.ts), [src/scoring.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/scoring.ts), [src/curate.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/curate.ts)).

**Agent adoption is a first-class interface concern.** The CLI exposes JSON output across main workflows, an HTTP MCP server exposes `cm_context`, `cm_feedback`, `cm_outcome`, `memory_search`, and `memory_reflect`, and the repo ships a skill file that tells agents to call `cm context` before non-trivial tasks ([src/cm.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/cm.ts), [src/commands/serve.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/commands/serve.ts), [SKILL.md](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/SKILL.md)). The implemented behavior still depends on host wiring: MCP tools and CLI commands are pull surfaces unless an agent harness or generated prompt file actually calls them.

**Safety memory can become enforcement.** Trauma records persist as JSONL in global or project scope; installed Claude Code and git hooks load active traumas and deny matching Bash commands or staged diffs ([src/trauma.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/trauma.ts), [src/commands/guard.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/commands/guard.ts), [src/trauma_guard_script.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/trauma_guard_script.ts)). This is not merely advice: when the hook is installed, retained memory is consumed as a hard pre-tool or pre-commit gate.

## Artifact analysis

- **Storage substrate:** `files` — The primary retained state is file-backed: `~/.cass-memory/playbook.yaml`, `~/.cass-memory/diary/*.json`, processed logs, outcome/context/usage JSONL, onboarding state, embedding caches, global trauma JSONL, and repo-local `.cass/*` files. Secondary substrates include the external `cass` session index, an in-memory embedding/model cache, optional remote `cass` hosts over SSH, and HTTP MCP service objects.
- **Representational form:** `prose` `symbolic` `parametric` — Playbook bullets, diary summaries, history snippets, reasons, and exported prompts carry prose; schemas, rule ids, categories, scopes, maturity, feedback events, deltas, logs, regex traumas, MCP schemas, and config are symbolic; optional embedding vectors/cache entries and transformer/Ollama similarity are parametric retrieval aids.
- **Lineage:** `authored` `imported` `trace-extracted` — Users can manually add/import playbook rules and traumas; `cass` imports raw session history from other agent tools; diaries, playbook deltas, feedback signals, outcome logs, related sessions, onboarding state, and trauma candidates are extracted from session transcripts, tool traces, context uses, and command outcomes.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Returned context and diaries advise agents as knowledge; exported `AGENTS.md`/Claude snippets and the skill instruct agents; trauma hooks enforce command denial; workspace scope, categories, MCP schemas, and query construction route access; Zod/config/rule validation gate writes; scores and embeddings rank read-back; reflection, curation, and feedback update learned procedural memory.

**Raw session and `cass` history.** Storage substrate: outside cass-memory's own files, in the `cass` index and raw agent session paths. Representational form: prose transcripts plus symbolic metadata such as path, agent, workspace, timestamp, score, and origin. Lineage: imported from Claude/Codex/Cursor/Aider/other sessions through `cassSearch`, `cassExport`, and session discovery. Behavioral authority: evidence for diary extraction, rule validation, context snippets, onboarding samples, audit scans, and cross-agent enrichment.

**Diary entries.** Storage substrate: JSON files under `config.diaryDir`. Representational form: prose summaries, decisions, challenges, preferences, and key learnings inside a symbolic `DiaryEntrySchema`. Lineage: trace-extracted from exported sessions, either by fast heuristics or LLM extraction, with optional related-session enrichment from cross-agent `cass` search. Behavioral authority: working-memory evidence for later reflection and provenance for processed-session logs ([src/diary.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/diary.ts), [src/tracking.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/4d76f61969cbc382a030bdcaab2cdd159058fcfe/src/tracking.ts)).

**Playbook bullets.** Storage substrate: global YAML and optional repo-local `playbook.yaml`, merged at read time. Representational form: prose procedural rules and anti-patterns plus symbolic ids, scopes, categories, kinds, maturity, counters, feedback events, source sessions, source agents, tags, embeddings, and deprecation metadata. Lineage: authored manually or imported, trace-extracted through reflection/onboarding/outcome flows, and further derived by curation operations such as dedup reinforcement, content revision, merge, inversion, promotion, demotion, and deprecation. Behavioral authority: knowledge when returned by `cm context`; instruction when exported to prompt files; ranking/learning through effective score, feedback events, and embeddings.

**Processed logs, context logs, outcomes, usage, and onboarding state.** Storage substrate: JSON/JSONL files in `~/.cass-memory` or repo `.cass`. Representational form: symbolic event records with some prose task, notes, reasons, and snippets. Lineage: trace-extracted from command runs, selected context, session processing, user-supplied outcome records, and onboarding progress. Behavioral authority: learning and audit input: they prevent reprocessing, link outcomes back to rules, and drive later feedback application.

**Embedding cache and semantic scoring.** Storage substrate: file-backed embedding cache plus process-local model state. Representational form: parametric vectors keyed by content hashes, with symbolic cache version/model metadata. Lineage: derived from playbook bullet content and query text; invalidated when content hash or model changes. Behavioral authority: ranking, because `scoreBulletsEnhanced()` can blend keyword relevance with cosine similarity before applying effective score.

**Trauma records and installed guards.** Storage substrate: `traumas.jsonl` in global and project locations, plus generated Python hook files under `.claude/hooks` or `.git/hooks`. Representational form: symbolic regex patterns, severity/scope/status, trigger metadata, and Python enforcement scripts. Lineage: authored manually/imported or trace-extracted by scanning recent `cass` sessions for apology/destruction patterns. Behavioral authority: enforcement when hooks are installed, because matching active traumas deny commands or commits before the action proceeds.

Promotion path: cass-memory has a real authority ladder. A raw session can become a diary, then an LLM-proposed playbook delta, then a validated and curated rule, then a ranked context item, then an exported prompt instruction or feedback-reweighted proven rule. A safety trace can similarly become a trauma candidate, then an active regex record, then an installed hard gate.

## Comparison with Our System

| Dimension | cass-memory | Commonplace |
|---|---|---|
| Primary purpose | Procedural memory for AI coding agents across sessions/tools | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | YAML playbook bullet plus diary/outcome/log sidecars | Typed Markdown note/review/instruction/source artifact |
| Raw evidence | External `cass` session index and exported transcripts | Source snapshots, citations, code checkouts, authored links |
| Write path | Reflection over sessions, deterministic curation, manual CLI/MCP writes, outcome feedback | Direct file edits, snapshots, validation, semantic review, generated indexes |
| Read path | `cm context`, MCP tools/resources, search, exports, installed guards | `rg`, indexes, links, skills, loaded repo instructions |
| Governance | Zod schemas, evidence gate, LLM validator, file locks, dedup/conflict heuristics, scoring decay | Collection/type contracts, schema validation, git diff, semantic gates, review archives |

cass-memory is stronger than Commonplace as an operational agent-memory product. It has a packaged CLI, machine-readable output, MCP tools, automatic session discovery, feedback loops, scoring decay, onboarding helpers, and hook installation. Commonplace is stronger as a durable review and methodology corpus: the source-of-truth artifacts are directly inspectable Markdown with collection contracts, source citations, and a review workflow designed for semantic fidelity.

The sharpest design difference is the treatment of trace-extracted state. cass-memory intentionally lets session traces affect future behavior through generated rules and feedback weights. Commonplace uses trace-extracted inputs more cautiously: sources and reports can inform notes, but promoted artifacts remain reviewed prose or symbolic contracts. cass-memory's approach gives faster adaptation; Commonplace's approach gives more stable meaning and easier review.

### Borrowable Ideas

**Separate LLM proposal from deterministic curation.** Ready now. Commonplace's review and note-writing flows can borrow the explicit proposal/curation split: let an LLM suggest deltas, but make merge, dedup, archive, promotion, and validation symbolic.

**Outcome feedback tied to recalled rule ids.** Needs a concrete use case. If Commonplace ever serves operational rules into agents, logging which rule ids were loaded and later applying success/failure feedback would be a useful ranking signal.

**Make degraded retrieval explicit in machine output.** Ready now. `cm context` reports when semantic search or `cass` history degrades, which is better than silently falling back to weaker context.

**Use sidecar feedback for ranking, not for claim truth.** Ready as a design constraint. cass-memory's feedback events are useful for procedural helpfulness; Commonplace should not let usage frequency upgrade theoretical truth without semantic review.

**Borrow hard-gate memory only for narrow safety patterns.** Needs care. Trauma guards are appropriate for concrete dangerous commands; applying the same enforcement model to broad methodology claims would overfit quickly.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually add/import/remove/mark rules, outcomes, traumas, and project exports through CLI/MCP flows; automatic writes create diaries from sessions, propose and apply reflected playbook deltas, record processed logs, apply inline/outcome feedback, maintain scores/maturity, write embedding caches, and install generated guard artifacts.

**Curation operations:** `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — The curator reinforces exact or similar duplicate rules instead of adding copies; replaces existing bullet content; can create merged bullets; deprecates, retires, or inverts bad rules; score calculation applies half-life decay; and promotion/demotion changes maturity from candidate through proven or deprecated.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Raw agent session transcripts, `cass` search hits, context-use logs, outcome records, inline feedback comments, command-run usage events, and trauma scans feed durable state.

**Learning scope:** `per-project` `cross-task` — Global playbooks and diaries are cross-task; repo-local `.cass` files and workspace-scoped bullets make part of the memory project-specific.

**Learning timing:** `online` `offline` `staged` — Context logging, manual feedback, outcome application, and MCP writes can happen online; `cass` history and local files work offline once present; reflection, onboarding, validation, and trauma scanning are staged workflows.

**Distilled form:** `prose` `symbolic` `parametric` — Sessions become prose diary summaries and procedural rules, symbolic deltas/logs/scores/regex guards, and optional embedding vectors for semantic scoring.

**Extraction.** The main loop extracts a diary from a raw session, uses the diary and related history as an LLM prompt for deltas, validates add-deltas against `cass` evidence and optional LLM judgment, then curates accepted deltas into playbook state. A separate onboarding path samples sessions and prompts the acting agent to extract rules without external LLM cost. Outcome and inline-feedback paths extract rule ids from transcripts or context logs and convert success/failure signals into feedback events.

**Scope and timing.** The learning unit is usually a session or batch of sessions, with processed logs preventing repeat reflection. Cross-agent enrichment requires explicit config consent before attaching related sessions from other agents. Reflection and validation can use remote or local `cass` history, but the retained playbook remains file-backed.

**Survey fit.** cass-memory is a strong trace-to-procedural-rule system: raw traces are not merely searchable evidence but can be distilled into ranked rules and anti-patterns. It also demonstrates a split authority model: trace-extracted diaries and logs are knowledge artifacts, while accepted playbook bullets and trauma guards can become instruction or enforcement artifacts.

## Read-back

**Read-back:** `both` — Most memory read-back is pull through `cm context`, `cm similar`, `memory_search`, MCP resources, playbook inspection, and `cass` history search; exported prompt files and installed trauma hooks can also push retained memory into future action without the agent making a fresh lookup.

**Read-back signal:** `coarse` `inferred / lexical` — Prompt exports are coarse always-load surfaces when a host loads the generated `AGENTS.md` or Claude-format project rules; trauma hooks use inferred lexical matching over command text or staged diff lines. Task-specific playbook and history selection through `cm context` remains pull, even when it uses keyword or embedding relevance.

**Faithfulness tested:** `no` — The repository tests CLI/MCP/tool/hook mechanics and scoring behavior, but I did not find an ablation showing that agents reliably change behavior after pushed prompt rules or retrieved context.

**Targeting and signal.** Pull read-back is the primary path: task text becomes keywords and optional embeddings, workspace scope filters bullets, effective scores and relevance rank them, and `cass` searches return bounded history snippets. Push read-back exists when operators materialize playbook rules into prompt files through `cm project` or install trauma guards; the trauma path is more precise because it fires on matching command/diff content, but it is regex/lexical rather than semantic judgment.

**Injection point.** `cm context` and MCP `cm_context` serve memory before the model call only when the agent or user asks. Exported prompt files are consumed at host startup or prompt assembly. Trauma guards fire before Bash tool use or before commit completion; post-session reflection, outcome application, embedding updates, and processed-log writes are write-side maintenance for later calls.

**Selection, scope, and complexity.** Context selection is bounded by `maxBulletsInContext`, `maxHistoryInContext`, CLI `--limit`/`--history`, workspace filters, lookback days, semantic/keyword scoring, deprecated-pattern warnings, and snippet truncation. Prompt export can be less bounded unless operators set per-category/top limits. Trauma read-back is narrow in volume but can be broad in effect because a single regex match denies the action.

**Authority at consumption.** Returned bullets and history snippets are advisory knowledge unless the host instruction tells the agent to obey them. Exported playbooks become soft instructions in prompt context. MCP tool schemas route reads/writes. Trauma hooks are hard enforcement artifacts because they return deny decisions or fail the pre-commit hook.

**Other consumers.** Humans consume the same memory through CLI list/get/top/stale/why/stats, onboarding flows, audits, exports, and MCP resources. The tool is therefore not only an LLM memory layer; it is also an operator-facing procedural-memory maintenance interface.

## Curiosity Pass

**The README's "automatic" learning is partly host-dependent.** The code can reflect, curate, and serve context, but agents still need to call `cm context` or use the MCP/skill/prompt integration for the memory to affect ordinary tasks.

**The curator is more trustworthy than the extracted content.** Dedup, locking, scoring, deprecation, and schema validation are code-grounded. Whether an LLM-extracted rule is actually wise remains only as good as the evidence gate, validator, and later feedback.

**Trauma guards are the most authority-dense memory surface.** A playbook rule advises; an installed trauma record blocks. That makes trauma quality and healing workflows more important than ordinary rule quality.

**Parametric state is local to ranking, not the source of truth.** Embeddings affect ordering when enabled, but playbook prose and symbolic metadata remain inspectable and recoverable without the vector cache.

**The system records several traces that could become privacy liabilities.** It has sanitization and cross-agent consent controls, but diary entries, context logs, outcomes, usage logs, and audit logs still accumulate behaviorally sensitive traces.

## What to Watch

- Whether `autoReflect` becomes an actually scheduled or hook-driven loop; that would make trace-extracted writes more autonomous than the current command-triggered reflection path.
- Whether agents commonly install the skill/MCP/prompt export path; adoption determines whether the system is pull-first in practice or mostly prompt-pushed.
- Whether validation gains stronger semantic review of rule truth; current evidence counts and LLM validation are useful but not equivalent to source-grounded review.
- Whether remote `cass` history and cross-agent enrichment become common defaults; that would increase memory coverage and privacy risk at the same time.
- Whether prompt export grows automatic budget management; unbounded always-loaded procedural rules could dilute context even if `cm context` remains well-bounded.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: cass-memory stores playbooks and diaries, but task memory usually affects an agent only after explicit retrieval or installed prompt/hook wiring.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw sessions, diary JSON, playbook bullets, embedding caches, logs, MCP schemas, and trauma guards have different authority despite sharing one product.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: diaries, history snippets, query results, and many playbook returns advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: exported prompt rules, MCP tool contracts, validators, scoring policies, and trauma guards shape or enforce later behavior.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: cass-memory turns session logs and feedback traces into durable procedural rules, anti-patterns, and safety gates.
