---
description: "Synapptic review: Claude Code transcript learning into user archetypes, multi-assistant memory writes, relay visibility, and guard faithfulness benchmarks"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
tags: [trace-derived, push-activation]
---

# Synapptic

Synapptic, from `appcuarium/synapptic`, is a Python CLI for learning a developer-facing user profile from AI coding sessions. At this commit it reads Claude Code JSONL transcripts, filters them, extracts observations with a configurable LLM provider and prompt pattern, merges observations into weighted global/project profiles, synthesizes markdown archetypes, writes those archetypes into multiple coding-assistant memory surfaces, and offers a local relay/browser for session visibility.

**Repository:** https://github.com/appcuarium/synapptic

**Reviewed commit:** [bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f](https://github.com/appcuarium/synapptic/commit/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f)

**Last checked:** 2026-06-02

## Core Ideas

**The central memory is a learned user-archetype document.** Synapptic is not a vector-memory library for arbitrary facts. Its main retained behavior-shaping output is markdown with `## User Archetype`, `## Guards`, and `## Known Weaknesses`, generated from accumulated observations and written to assistant-specific instruction or memory files ([README.md](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/README.md), [src/synapptic/synthesize.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/synthesize.py), [src/synapptic/outputs.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/outputs.py)).

**Trace filtering is deliberately lossy before LLM extraction.** `filter_transcript()` stream-parses Claude Code JSONL, drops progress/system/file-history records, strips tool outputs, tool calls, and thinking blocks from the extraction stream, keeps user/assistant text, boosts likely corrections and preferences, and truncates to a token budget by prioritizing boosted turns plus recent filler ([src/synapptic/filter.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/filter.py), [src/synapptic/config.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/config.py)). This is Synapptic's first context-efficiency boundary: raw sessions can be huge, but extraction sees a compact preference-relevant transcript.

**Extraction is profile-aware after the first run.** `build_extraction_prompt()` loads the active prompt pattern, lists active dimensions, wraps the filtered transcript as reference data, and when a profile exists includes high-weight prior observations so the LLM should skip known patterns and focus on new or corrective signal ([src/synapptic/extract.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/extract.py), [src/synapptic/patterns.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/patterns.py)). Custom extraction patterns are user-editable `prompt.md` files under `~/.synapptic/patterns/`, with built-in patterns as fallback.

**The profile is weighted state, not just append-only notes.** Observations are saved per session, routed by dimension, merged with text-similarity matching, evidence counts, time/merge decay, source-session caps, and project-origin tracking. Mixed dimensions such as expectations, triggers, AI failures, and guards can promote to global when similar observations appear across enough projects ([src/synapptic/state.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/state.py), [src/synapptic/profile.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/profile.py), [src/synapptic/config.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/config.py)).

**Read-back is through native assistant memory surfaces.** `integrate_archetypes()` combines global and project archetypes, resolves configured output targets, filters redundant/backfire guards when benchmark verdicts exist for a target model family, and writes to Claude Code memory, Cursor rules, Copilot instructions, Gemini styleguide, Codex `AGENTS.md`, Windsurf, Cline, Aider, and Continue files ([src/synapptic/integrate.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/integrate.py), [src/synapptic/outputs.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/outputs.py)). Context efficiency at read-back is mostly project scoping, model-family guard filtering, and Claude Code `MEMORY.md` placement near the top to avoid the documented line cutoff; there is no per-query semantic memory matcher.

**It has a behavior-faithfulness benchmark, not just presence in context.** `benchmark.py` generates adversarial scenarios for guards, compares WITH and WITHOUT conditions, scores responses with an LLM judge, injects control tests, records per-model verdicts on profile guards, and can exclude backfire or redundant guards from later synthesis/output ([src/synapptic/benchmark.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/benchmark.py), [src/synapptic/cli.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/cli.py)). That makes Synapptic unusually explicit about whether a retained rule changes future behavior.

**The relay/browser preserves observability but is not the learning substrate.** The optional FastAPI relay logs requests, token counts, summaries of messages, response content, active sessions, and indexed Claude Code session metadata into local SQLite with FTS search and browser/WebSocket views ([src/synapptic/relay/store.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/store.py), [src/synapptic/relay/indexer.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/indexer.py), [src/synapptic/relay/routers/browser.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/routers/browser.py)). Those records support inspection and metrics; the implemented profile-learning pipeline still reads Claude Code JSONL transcripts rather than relay request logs.

## Artifact analysis

- **Storage substrate:** `files` — `~/.claude/projects/*/*.jsonl`, discovered by `find_session_transcripts()` and parsed by the filter/indexer/browser paths
- **Representational form:** `prose` `symbolic` — symbolic JSON/YAML/SQLite/settings records carry prose messages, observations, archetypes, guards, and assistant instructions
- **Lineage:** `authored` `trace-extracted` — package hooks/skills/output templates are authored, while observations, profiles, archetypes, benchmark verdicts, and assistant memory files derive from Claude Code session traces
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — traces and relay state are evidence; archetypes instruct assistants; project/model routing, weights, thresholds, exclusions, benchmark verdicts, and output filtering decide what is learned, synthesized, pruned, and written

**Claude Code session JSONL transcripts.** Storage substrate: `~/.claude/projects/*/*.jsonl`, discovered by `find_session_transcripts()` and parsed by the filter/indexer/browser paths. Representational form: symbolic JSONL with prose messages, tool call/result blocks, model usage, timestamps, and system records. Lineage: generated by Claude Code sessions, not by Synapptic. Behavioral authority: source-trace knowledge artifacts; they do not guide later agents until filtered, extracted, merged, synthesized, and integrated.

**Filtered transcript turns.** Storage substrate: transient Python `Turn` objects during extraction. Representational form: prose conversation text plus symbolic role/timestamp/boost metadata. Lineage: derived lossy view of session JSONL, with tool outputs and thinking stripped and likely correction/preference turns boosted. Behavioral authority: extraction input only; these turns shape what the LLM can observe but are not retained as user memory.

**Observation JSON files.** Storage substrate: `~/.synapptic/global/observations/*.json` and `~/.synapptic/projects/<slug>/observations/*.json`, each embedding `project_slug`, `session_id`, and observations. Representational form: symbolic JSON records with dimension, observation text, confidence, evidence, session id, timestamp, and project. Lineage: trace-extracted by the LLM from filtered transcripts and active extraction pattern. Behavioral authority: knowledge artifacts and learning inputs for merge/synthesis; they are evidence, not direct prompt instructions.

**Profile YAML files.** Storage substrate: `~/.synapptic/global/profile.yaml`, `~/.synapptic/projects/<slug>/profile.yaml`, and copied snapshots under `~/.synapptic/profile_history/`. Representational form: symbolic YAML with prose observations, weights, evidence counts, first/last seen timestamps, source-session ids, project origins, exclusions, and model verdicts. Lineage: derived from observation JSON through dimension routing, similarity merge, decay, global promotion, and benchmark verdict recording. Behavioral authority: system-definition learning state because weights, thresholds, exclusions, and model verdicts decide what can be synthesized and written to future assistant memory.

**Archetype markdown files.** Storage substrate: `~/.synapptic/global/archetype.md` and `~/.synapptic/projects/<slug>/archetype.md`. Representational form: prose markdown with a user archetype, imperative guards, and known weaknesses. Lineage: LLM-synthesized from filtered profile YAML, with lower evidence requirements for guard/failure dimensions and optional target-model filtering. Behavioral authority: candidate system-definition artifact; its effective authority depends on the output target that consumes it.

**Integrated assistant memory files.** Storage substrate: native assistant files such as Claude Code `memory/user_archetype.md` plus `MEMORY.md` reference, `.cursor/rules/synapptic.mdc`, `.github/copilot-instructions.md`, `.gemini/styleguide.md`, `AGENTS.md`, `.windsurfrules`, `.clinerules`, `CONVENTIONS.md`, and `.continuerules`. Representational form: prose markdown/MDC with light frontmatter or marker blocks. Lineage: assembled from global and project archetypes, then filtered by target model family when benchmark verdicts exist. Behavioral authority: prompt-level system-definition context for the target assistant; for targets whose host actually auto-loads the file, this is push read-back at session/startup scope.

**Session-end hook and bundled skill.** Storage substrate: installed files under `~/.claude/hooks/synapptic-session-end.sh`, `~/.claude/skills/synapptic/SKILL.md`, and `~/.claude/settings.json` hook registration. Representational form: shell script, JSON settings, and prose skill instructions. Lineage: copied from package bundle by `synapptic install`. Behavioral authority: system-definition trigger surface; it starts background extraction/merge/synthesis after selected SessionEnd reasons and tells Claude Code when to invoke Synapptic commands ([src/synapptic/cli.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/cli.py), [src/synapptic/bundle/hooks/synapptic-session-end.sh](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/bundle/hooks/synapptic-session-end.sh), [src/synapptic/bundle/skill/SKILL.md](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/bundle/skill/SKILL.md)).

**Benchmark test caches, results, and guard verdicts.** Storage substrate: JSON files under `~/.synapptic/benchmarks/` plus `model_verdicts` and exclusion flags written back into profile YAML. Representational form: symbolic JSON/YAML with generated scenarios, responses, judge verdicts, classifications, CIs, controls, and per-model outcomes. Lineage: derived from current guard profile, generated tests, target-model responses, and LLM-as-judge scoring. Behavioral authority: evaluation and pruning authority because redundant/backfire verdicts can remove guards from later archetypes for a target model.

**Relay SQLite and browser state.** Storage substrate: `~/.synapptic/relay.db`, `relay.log`, token metrics JSONL, active-session websocket state, and parsed browser views. Representational form: symbolic SQLite rows plus FTS entries and prose-rendered turns. Lineage: generated by the local relay, Claude Code JSONL indexing, and API proxy traffic. Behavioral authority: knowledge artifacts for humans and operators, plus metrics/search surfaces; they do not currently feed the profile-learning loop.

**Promotion path.** Synapptic promotes raw session traces into observations, observations into weighted profiles, profiles into prose archetypes, archetypes into assistant memory files, and benchmark outcomes back into guard filtering. The strongest authority jump is profile/archetype to integrated assistant instructions: conversational traces become startup context for future agents.

## Comparison with Our System

| Dimension | Synapptic | Commonplace |
|---|---|---|
| Primary purpose | Learn a personal developer/AI-interaction profile from coding sessions | Maintain a typed methodology KB for agents and maintainers |
| Main substrate | Home-directory state, Claude Code JSONL, profile YAML, generated markdown, native assistant files, optional SQLite relay | Git-tracked markdown collections, type specs, indexes, validation scripts, sources, reviews, and reports |
| Learning loop | Automatic or CLI-driven trace filtering, LLM extraction, weighted merge, LLM synthesis, integration | Deliberate artifact writing, source review, validation, semantic gates, and promotion |
| Read-back | Project/model-scoped prompt push through assistant memory files, plus human CLI reads | Mostly pull through `rg`, indexes, links, skills, reports, and explicit validation/review |
| Governance | Filtering, dimensions, weights, decay, promotion thresholds, profile history, guard benchmark, model verdict filtering | Collection contracts, schemas, deterministic validation, semantic review, git diffs, archive/replacement workflow |
| Context efficiency | Compresses raw transcripts before extraction; synthesizes profile before read-back; writes the whole selected archetype to assistant context | Loads selected artifacts by search/link/type; stronger citation and validation, weaker automatic startup selection |

Synapptic is a sharper trace-derived system than most "memory file" tools because it includes the full loop from session transcript to prompt-loaded behavioral rule. It also has an unusually practical evaluation story: if a guard backfires for a model, the benchmark can mark it and later output filtering can omit it for that model family.

The tradeoff is provenance and artifact discipline. Synapptic keeps source session ids and profile snapshots, but the generated archetype does not carry per-claim citations, reviewer state, schema validation, or invalidation rules. That is a tolerable choice for a personal assistant profile where local usefulness matters more than public argument quality. It is too weak for Commonplace's methodology layer, where durable claims should remain reviewable as claims.

**Read-back:** `push` — With engineered project/model scoping and faithfulness testing. Future agents receive the archetype through host memory/instruction files rather than asking Synapptic to search. The memory push is instance-targeted by project and target-assistant identifiers, not by per-query semantic retrieval.

### Borrowable Ideas

**Treat user corrections as first-class trace signal.** Commonplace could mine review comments, validation failures, and operator corrections for candidate workflow rules. Ready as a workshop/report experiment, but not as automatic instruction promotion.

**Keep raw traces, learned observations, and prompt instructions separate.** Synapptic's transcript -> observation JSON -> profile YAML -> archetype split is directly borrowable as vocabulary discipline. Commonplace should keep any trace-derived notes in a candidate lane until reviewed and validated.

**Use profile-aware extraction to avoid re-learning known patterns.** Synapptic sends high-weight existing observations into extraction so the LLM focuses on novelty. Commonplace could use the same shape for recurring review sweeps: include accepted prior findings so a reviewer spends budget on deltas. Ready where prior findings are already structured.

**Benchmark individual instructions with ablations.** The guard benchmark is the most important borrow. Commonplace could test high-authority instructions by creating adversarial tasks and comparing behavior with and without the candidate rule. Needs a narrow evaluation harness before it should affect production instructions.

**Filter prompt rules by target model.** A guard can be useful for one assistant and redundant or harmful for another. Commonplace can borrow this principle for agent-specific instruction bundles, but only after it has per-agent evidence rather than assumptions.

**Use native host memory files for adoption.** Synapptic writes into the files assistants already load. Commonplace should continue favoring plain files and documented host conventions over hidden service state. Ready now as an adoption criterion.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` — Claude Code session JSONL files supply user/assistant messages plus tool-use and tool-result records

**Learning scope:** `per-project` `cross-task` — project profiles stay local, while global dimensions and promoted mixed dimensions follow the user across projects and sessions

**Learning timing:** `offline` `staged` — ingestion can run manually or after SessionEnd, then proceeds through extraction, merge, synthesis, integration, and benchmark verdict filtering stages

**Distilled form:** `prose` `symbolic` — LLM-extracted observations and profile YAML are symbolic records containing prose observations, then archetype markdown and assistant memory files carry prose instructions

**Trace source.** Synapptic qualifies as trace-derived learning. Its source traces are Claude Code session JSONL files containing user/assistant messages, tool-use records, tool-result records, timestamps, model usage, and system/progress records. The extraction path deliberately strips many of those fields, but the raw trace source is still agent-session history.

**Extraction.** Extraction has two stages. A deterministic Python filter keeps conversation text and boosts likely correction/preference turns. Then an LLM, prompted by a configurable extraction pattern and optional existing-profile summary, emits observation JSON across configured dimensions. The oracle is partly heuristic, partly LLM judgment, and partly later reinforcement: observations gain or lose authority through merge weights, evidence counts, decay, cross-project promotion, synthesis thresholds, and benchmark verdicts.

**Scope and timing.** Scope is personal and project-aware. Global dimensions follow the user across projects; project dimensions stay local; mixed dimensions can promote globally after appearing across multiple projects. Timing can be manual through `ingest`, `extract`, `merge`, and `synthesize`, or automatic after Claude Code SessionEnd when the hook runs extraction/merge/synthesis for the closed session's project.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Synapptic belongs in the chat/session-to-prompt-instruction family. It strengthens the survey split between raw trace preservation, distilled knowledge artifacts, and higher-authority system-definition artifacts: transcripts are evidence, observations/profiles are learned state, and integrated archetypes are behavior-shaping prompt material.

## Read-back placement

**Direction.** Push, with auxiliary pull surfaces. The acting assistant does not ask Synapptic for memory at action time; Synapptic writes retained archetype memory into files that the target assistant is expected to load. Humans can pull profile/archetype/stats through CLI commands and browse sessions through the relay UI.

**Read-back signal:** `identifier` — project slug/path, configured output target, and target model family decide which retained archetype reaches the future assistant

**Read-back timing:** `pre-action` — host memory and instruction files are loaded before the future assistant session or request acts

**Faithfulness tested:** `yes` — the guard benchmark compares WITH and WITHOUT conditions and records verdicts that can filter later output

**Targeting and signal.** Targeting is `instance` at project/session scope: Synapptic resolves a Claude Code project directory into a project slug and project root, combines global memory with that project's archetype, and writes the result to the configured assistant target for that project. The signal is `identifier`: project slug/path and configured output target/model family decide which retained archetype reaches the future assistant. Host loading then uses always-on memory or instruction conventions such as Claude Code memory references, Cursor always-apply rules, Copilot/Gemini/Codex-style instruction files, and similar target files. It does not infer relevance from the current user query.

**Timing relative to action.** Read-back happens before the future assistant session or request acts, through startup or host instruction loading. Session-end extraction and synthesis run after a session, so they can only affect later sessions.

**Selection, scope, and complexity.** Complexity is reduced by filtering raw transcripts before extraction and by synthesizing many observations into one archetype before read-back. At consumption time, however, the selected archetype is loaded as prose; there is no token-aware per-query selection. Claude Code output tries to keep the `user_archetype.md` reference within `MEMORY.md`'s early lines, which is a practical host-specific scope control.

**Authority at consumption.** Integrated archetypes are prompt-level system-definition artifacts: guards are phrased as imperative rules, target files are instruction surfaces, and model verdict filtering controls which guards reach each target. Effective authority still depends on the host assistant honoring those files.

**Faithfulness.** Synapptic's benchmark explicitly tests behavioral uptake. It generates adversarial scenarios for guards, compares WITH and WITHOUT conditions, uses an LLM judge, includes controls, classifies guards as effective/redundant/backfire/ineffective, and writes verdicts back into the profile for later output filtering. The benchmark is not perfect, but it is a real implemented ablation rather than assuming "present in context" means "used."

**Other consumers.** Humans consume the same state through `profile`, `archetype`, `stats`, `diff`, `results`, `guards`, and relay/browser views. The relay also serves pair-programming and cost-visibility workflows, so retained traces are both learning inputs and operator-facing evidence.

## Curiosity Pass

**The strongest memory artifact is not the profile YAML.** The profile is the learned state, but the archetype files have stronger behavioral authority because they enter assistant prompts.

**The relay preserves richer traces than the learning path consumes.** Browser parsing keeps tool calls, tool results, thinking blocks, compaction markers, and token metrics for inspection. Extraction strips most of that for cost and safety, so Synapptic optimizes the learning path for interaction preferences rather than codebase-specific technical memory.

**The hook appears narrower than the README's "ingest" shorthand.** The bundled SessionEnd hook runs `extract -s`, `merge`, and project `synthesize`; it does not call `integrate` in the inspected script. That means automatic background processing updates Synapptic archetype state, while writing to configured assistant targets may still depend on the CLI path or a later integration command.

**Guard benchmarking closes one loop but opens another.** Verdicts can suppress harmful or redundant guards, but test generation and judging are also LLM-mediated. Synapptic mitigates this with controls, separate judge options, deterministic seeds, retries, and cached tests, but the benchmark is still an empirical signal, not proof.

**The implementation names still leak older "synaptic" strings.** Some docstrings/messages say `synaptic` while package metadata and user-facing README say `synapptic`. That does not change the architecture, but it is worth watching because install/uninstall paths and user instructions should not drift.

## What to Watch

- Whether the SessionEnd hook begins running `integrate` after synthesis. That would make the automatic trace-to-read-back loop fully closed at session end.
- Whether archetype sections gain per-guard source session ids or evidence links. That would make prompt-loaded instructions auditable instead of only traceable through profile YAML.
- Whether the benchmark moves from guard-only tests to testing the whole archetype's profile claims and known weaknesses.
- Whether additional session sources become implemented. Cursor/Copilot/Aider transcript import would widen the trace source and test the project/global routing model.
- Whether read-back gains query-time selection. That would move Synapptic from startup/project push to relevance-gated memory activation and reduce context dilution.
- Whether relay request logs become a first-class extraction source. That would merge the observability subsystem with the learning subsystem and require stronger privacy/governance boundaries.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Synapptic distills Claude Code session traces into weighted profiles and prompt-loaded assistant instructions.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Synapptic extracts future interaction policy from prior user/agent sessions.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Synapptic couples storage with native assistant read-back files, then benchmarks whether rules affect behavior.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: Synapptic keeps transcripts/observations/profiles as evidence while loading distilled archetypes.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Synapptic separates transcripts, observations, profiles, archetypes, output files, hooks, benchmark state, and relay state by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: integrated archetypes, output writers, hooks, benchmark filtering, and guard verdicts configure or constrain future assistant behavior.
