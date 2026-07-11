---
description: "Synapptic review: trace-derived user-model builder that mines Claude transcripts into weighted profiles, benchmarked guards, and assistant memory files"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-05"
---

# Synapptic

Synapptic, from `appcuarium/synapptic`, is a local Python CLI for learning a developer/user archetype from Claude Code session transcripts and writing that learned profile into AI coding assistant memory surfaces. At the reviewed commit it filters Claude JSONL sessions, asks a configured LLM to extract observations across user and agent-failure dimensions, merges them into global and per-project weighted profiles, synthesizes Markdown archetypes, writes those archetypes to tool-specific memory/config files, and includes a benchmark loop that tests individual guards by comparing behavior with and without the archetype.

**Repository:** https://github.com/appcuarium/synapptic

**Reviewed commit:** [bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f](https://github.com/appcuarium/synapptic/commit/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f)

**Last checked:** 2026-06-05

## Core Ideas

**The central artifact is a learned user model, not a conversation memory store.** Synapptic does not retrieve old facts for arbitrary task queries. It converts session transcripts into observations, observations into weighted profiles, and profiles into an archetype with user style, guards, and known weaknesses ([README.md](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/README.md), [src/synapptic/extract.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/extract.py), [src/synapptic/profile.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/profile.py), [src/synapptic/synthesize.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/synthesize.py)).

**Context efficiency is frontloaded into extraction and synthesis.** Transcript filtering strips progress/system/tool records, keeps user and assistant text, boosts likely correction/preference turns, and truncates to a token budget before any LLM extraction call. Profile-aware extraction then includes only high-weight existing observations, and synthesis emits a bounded archetype rather than replaying sessions into future agents ([src/synapptic/filter.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/filter.py), [src/synapptic/extract.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/extract.py), [src/synapptic/synthesize.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/synthesize.py)). The read-back side is intentionally coarse: the generated archetype is loaded as a compact standing profile, not selected per request.

**Profiles are weighted, decayed, and routed by dimension.** `config.py` defines global, project-local, and mixed dimensions. `profile.py` routes observations, reinforces similar observations with sequence matching, applies per-merge and time-based decay, removes low-weight items, promotes mixed observations after recurrence across projects, and keeps source session ids and project origins ([src/synapptic/config.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/config.py), [src/synapptic/profile.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/profile.py), [tests/test_profile.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/tests/test_profile.py)).

**Output integration is multi-surface and model-aware.** The same learned archetype can be written to Claude Code memory, Cursor rules, Copilot instructions, Gemini styleguide, Codex `AGENTS.md`, Windsurf, Cline, Aider, and Continue files. Benchmark verdicts can mark guards redundant or harmful for a target model family, and integration resolves a target model before writing that target's archetype ([src/synapptic/outputs.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/outputs.py), [src/synapptic/integrate.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/integrate.py), [src/synapptic/benchmark.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/benchmark.py)).

**Faithfulness is treated as a measurable property for guards.** The benchmark path generates adversarial scenarios from guard observations, compares responses with and without the archetype or tested guard, uses an LLM judge with controls, records classifications such as effective/redundant/backfire, and can exclude guards from future synthesis while retaining them in the profile ([src/synapptic/benchmark.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/benchmark.py), [src/synapptic/cli.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/cli.py)).

**The relay is observability, not the main memory loop.** The optional relay stores session/request metrics, request/response bodies, an FTS session index, and active-session state in SQLite for local browsing and token accounting. It supports inspection and search of conversations, but the durable behavior-changing memory remains the observation/profile/archetype path ([src/synapptic/relay/store.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/store.py), [src/synapptic/relay/indexer.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/indexer.py)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` - The profile memory lives under `~/.synapptic/` as JSON observations, YAML profiles, Markdown archetypes, history snapshots, pattern prompts, config, benchmark JSON, and generated assistant memory/config files; the optional relay adds SQLite tables for request metrics, session index, FTS search, and ended-session state ([src/synapptic/config.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/config.py), [src/synapptic/state.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/state.py), [src/synapptic/relay/store.py](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/store.py)).
- **Representational form:** `prose` `symbolic` - Transcripts, observations, archetypes, guards, known weaknesses, extraction patterns, and assistant memory files are prose; dimensions, weights, evidence counts, source session ids, project slugs, model verdicts, output targets, hooks, settings, benchmark classifications, and relay indexes are symbolic. Synapptic calls LLMs, but the inspected retained memory is not stored as embeddings or model weights.
- **Lineage:** `authored` `trace-extracted` - Users author config, output selection, patterns, and exclusions; the core profile and archetype are derived from Claude Code JSONL session traces, filtered conversation pairs, LLM-extracted observations, weighted merge state, benchmark scenarios/results, and per-model verdicts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` - Observations and relay records serve as knowledge evidence; generated archetypes and guard files instruct future coding assistants; project slugs, dimensions, output targets, and model-family resolution route memories; extraction validation, benchmark controls, and judge verdicts validate guard behavior; weights, decay, model verdicts, and exclusions rank/filter what reaches the archetype; the whole extract/merge/synthesize/benchmark loop is a learning path from traces into future prompt policy.

**Observation files.** Per-session observation JSON is the raw distilled evidence layer: LLM output plus session id, timestamp, project metadata, dimension, confidence, and evidence text. It is retained mainly for traceability and later profile merging.

**Weighted profiles.** `profile.yaml` is the standing learned state. It is symbolic enough to sort, decay, promote, filter, and benchmark, but its operative content is prose observations that later synthesis interprets.

**Archetype files.** `archetype.md` and generated assistant files are the high-authority read-back artifacts. They convert learned observations into natural-language behavior policy and become instruction-like when loaded by Claude Code, Cursor, Codex, or another assistant.

**Benchmark records and model verdicts.** Benchmark JSON files and `model_verdicts` do not themselves tell the agent how to behave; they govern which guards should survive synthesis for a target model. This is validation and ranking authority over the instruction layer.

**Promotion path.** Synapptic has a clear promotion ladder: raw Claude transcript -> filtered turns -> extracted observations -> weighted profile entries -> synthesized archetype -> assistant-specific memory file -> benchmark verdict/exclusion feedback. That path crosses from trace evidence into reviewed-by-benchmark prompt policy, though not into typed repo-native notes or deterministic validators.

## Comparison with Our System

| Dimension | Synapptic | Commonplace |
|---|---|---|
| Primary purpose | Learn a personal/user model and behavioral guards from AI coding sessions | Maintain a typed, git-native methodology KB for agents and maintainers |
| Canonical retained artifact | Weighted profile plus synthesized archetype | Typed Markdown artifact with schema, links, citations, validation, and review |
| Write path | Automatic trace extraction, merge, synthesis, benchmark feedback, plus manual config/exclusions | Human/agent-authored artifacts, snapshots, indexes, validation, review gates |
| Read-back | Generated profile is pushed through assistant memory/config files; CLI can also show/pull profile state | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Weighting, decay, source ids, benchmark controls, model verdicts, exclusions | Collection contracts, schemas, deterministic validation, semantic review, git diffs |

Synapptic is much stronger than Commonplace at closing the loop from actual session friction to future prompt policy. Commonplace records and reviews knowledge deliberately; Synapptic watches repeated interaction failures, creates candidate guards, tests whether they help, and can remove guards that backfire. That is the missing operational loop for personal agent memory.

Commonplace is stronger at artifact inspectability and authority boundaries. A Synapptic archetype can become high-authority prompt text even though its supporting observations are LLM-extracted and not citation-pinned to exact transcript spans in the generated file. Commonplace would require the artifact's type, provenance, links, validation status, and intended authority to be explicit before it changes durable methodology.

The tradeoff is speed versus review. Synapptic's local file substrate and benchmark loop make learned behavior cheap to adopt, but the generated archetype is still a coarse always-loaded profile. Commonplace's slower note lifecycle avoids silent overgeneralization, but it lacks Synapptic's automatic trace-mining and guard ablation pressure.

### Borrowable Ideas

**Guard effectiveness as a first-class field.** Ready now for review vocabulary. Commonplace could record whether a prescriptive instruction is untested, effective, redundant, or harmful for a model/harness, instead of treating all prose rules as equal once accepted.

**Trace-derived candidates should start outside the library.** Ready for workshop workflows. Synapptic's observation/profile/archetype tiers map well to Commonplace's workshop-to-library promotion: raw traces and extracted candidate guards should live in work/report space until reviewed or benchmarked.

**Profile-aware extraction as anti-duplication.** Needs a concrete extraction workflow. Passing high-confidence existing profile entries into a future extractor is a practical way to reduce repeated discoveries, but Commonplace would need source-span preservation so "skip known patterns" does not hide drift or contradictions.

**Model-specific guard filtering.** Useful but needs policy design. Commonplace could track whether a rule is needed for Codex, Claude, or another harness separately, while keeping the canonical rule and its evidence independent of any one model family.

**Coarse startup memory should be visibly bounded.** Ready as a caution. Synapptic's generated archetype is compact, but always-loaded learned policy can still dilute context or overfit. Commonplace should keep any generated startup memory short, sourced, and separable from hand-authored project instructions.

## Write side

**Write agency:** `manual` `automatic` - Users configure providers, modes, output targets, patterns, projects, benchmark choices, and guard exclusions; automatic paths discover unprocessed sessions, filter transcripts, extract observations, merge weighted profiles, promote cross-project patterns, synthesize archetypes, integrate outputs, run session-end hooks, record benchmark verdicts, and maintain relay/index state.

**Curation operations:** `dedup` `evolve` `decay` `promote` `consolidate` `synthesize` - Similar observations reinforce existing profile entries instead of creating endless duplicates; profile entries evolve through weight, evidence count, source list, project list, last-seen timestamp, and sometimes more-specific observation text; old entries decay by merge cycle and wall-clock age; mixed dimensions promote to global after recurrence across projects; synthesis consolidates profile entries into a compact archetype and can generate higher-level user archetype/known-weakness prose from the profile.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` - The primary traces are Claude Code project JSONL transcripts. The filter keeps direct user and assistant text and strips tool-use bodies, tool results, thinking blocks, system/progress records, and file-history snapshots; the optional relay can also persist request and response bodies plus token metrics.

**Learning scope:** `per-project` `cross-task` - Profiles are split into global and per-project state; dimensions such as communication, workflow, values, and expertise go global, project-local observations stay local, and mixed dimensions can promote after appearing across enough projects.

**Learning timing:** `online` `staged` - The SessionEnd hook can enqueue background extraction after a Claude session closes, while the explicit CLI supports staged `extract`, `merge`, `synthesize`, `integrate`, and `benchmark` runs.

**Distilled form:** `prose` `symbolic` - Distilled outputs include prose observations, archetypes, guards, and known weaknesses plus symbolic dimensions, weights, evidence counts, source ids, project slugs, model verdicts, exclusion flags, and benchmark result rows.

**Extraction.** The extraction oracle is a configured LLM called over a prompt template. The prompt wraps transcript and profile YAML as reference-only material, asks for JSON observations across active dimensions, and validates dimensions before saving. Custom user patterns can replace the default prompt.

**Scope and timing.** Synapptic is a personal/cross-project learning loop rather than a per-task retrieval memory. The important timing boundary is session close: a completed session can produce observations that affect later sessions through the generated archetype, but the current turn is not modified by extraction that happens after it.

**Survey placement.** Synapptic belongs in the trace-to-prompt-policy family. It strengthens the trace-derived survey's distinction between acquisition and promotion: extraction creates observations from session traces, merge turns them into durable profile state, synthesis creates behavior-shaping prompt policy, and benchmark results provide an explicit quality signal before guards remain active.

## Read-back

**Read-back:** `both` - Users and agents can pull profile/archetype state through CLI commands such as `profile`, `archetype`, `stats`, results, and relay browsing, but Synapptic's intended behavior-changing path pushes the generated archetype into assistant memory/config files that future agents load before acting.

**Read-back signal:** `coarse` `identifier` - Startup/project memory is coarse within the selected project/tool: the whole generated archetype is available rather than per-request selected. Project slugs, Claude project directories, output target, and model-family verdict resolution are identifier signals that decide which archetype file is written and therefore later loaded.

**Faithfulness tested:** `yes` - The benchmark system tests whether a guard changes model behavior by comparing with-archetype or with-guard responses against without-archetype/without-guard responses under adversarial scenarios, then uses an LLM judge and controls. This tests guard influence in benchmark prompts, not every real installed assistant session.

**Direction edge cases.** `synapptic profile`, `synapptic archetype`, benchmark result viewing, and the relay dashboard are pull surfaces. Generated files such as Claude Code `user_archetype.md`, Cursor `synapptic.mdc` with `alwaysApply: true`, Copilot instructions, Gemini styleguide, Codex `AGENTS.md`, and other rule files are push from the receiving agent's perspective because the agent does not first choose a memory lookup.

**Targeting and signal.** Targeting is mostly project/tool identity, not semantic relevance. The system combines global and project-specific archetypes for each resolved project, and output writers place the same compact learned profile into configured assistants. There is no implemented vector/BM25/judgment retrieval over profile entries at prompt time.

**Injection point.** Read-back is pre-invocation through host memory/config loading. The SessionEnd hook's extraction and synthesis happen after a session ends and are write-side maintenance for later sessions, not read-back into the just-finished action.

**Selection, scope, and complexity.** Selection happens before write-back: transcript filtering caps extraction input, profile-aware extraction caps known observations, narrative filtering selects high-weight/evidenced preferences, and target-model filtering can exclude guards. The final read-back artifact is compact but coarse; effective context dilution in real assistant sessions is not measured beyond the guard benchmark.

**Authority at consumption.** The generated archetype has instruction authority when loaded into a coding assistant's memory/rules surface. Underlying profiles and observations have knowledge/learning authority until synthesis promotes them into prompt policy. Benchmark verdicts have validation/ranking authority over whether guards remain active.

**Other consumers.** Humans consume the same retained state through CLI summaries, diffs, benchmark output, results comparison, excluded-guard commands, and the relay browser. The SessionEnd hook and integration code consume profiles operationally to produce future assistant memory files.

## Curiosity Pass

**The interesting artifact is not the README's final Markdown, but the weighted YAML beneath it.** The archetype is what agents read, yet the profile is the durable learning state with decay, evidence counts, project routing, and model verdicts.

**Synapptic tests prompt-policy activation more directly than most memory systems.** Many systems assume that injecting memory means memory worked. Synapptic's benchmark path at least asks whether a guard changes judged behavior under a controlled prompt comparison.

**The read-back is intentionally coarse.** There is no semantic activation of a particular guard for a particular prompt; Synapptic compresses learned history into startup policy. That avoids retrieval misses but risks overgeneralizing a user's past corrections into always-present constraints.

**The provenance chain weakens at synthesis.** Observations preserve session ids and evidence snippets, but generated archetypes do not expose exact transcript spans beside each guard. A user can inspect the profile and observations separately, but the high-authority output is not itself citation-rich.

**The source still has small naming drift.** Some strings and comments say "synaptic" or old state paths while package metadata and constants use `synapptic` and `~/.synapptic`. I treated constants, CLI behavior, and tests as authoritative.

## What to Watch

- Whether future versions preserve exact transcript-span provenance from each synthesized guard back to source JSONL records; that would make trace-derived prompt policy more reviewable.
- Whether the benchmark path moves from synthetic adversarial prompts to post-action audits of real sessions; that would test installed read-back rather than only prompt-comparison behavior.
- Whether Synapptic adds per-request guard selection instead of always-loaded archetypes; that would change the read-back signal from coarse/project identifier toward inferred or identifier-based instance targeting.
- Whether additional session sources beyond Claude Code are implemented; that would broaden trace lineage and change how project identity and transcript filtering should be trusted.
- Whether benchmark exclusions become automatic by policy rather than interactive/user-mediated; that would increase the system's automatic curation authority.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Synapptic derives observations, profile entries, prompt-policy archetypes, and guard verdicts from session traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Synapptic's profile state only changes behavior after synthesis and assistant memory/config read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: observations, weighted profiles, archetypes, output files, benchmarks, and relay indexes have different substrates, forms, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: session failures and corrections become durable behavior guidance for later agents.
- [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) - frames: Synapptic turns repeated interaction evidence into compact prompt-policy rules.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - explains: Synapptic precomputes user-model context before future sessions instead of replaying transcripts.
