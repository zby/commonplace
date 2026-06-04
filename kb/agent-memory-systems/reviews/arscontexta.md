---
description: "Claude Code plugin that derives file-backed agent knowledge systems with generated context files, skills, hooks, methodology claims, and session-learning loops"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Ars Contexta

Ars Contexta is `agenticnotetaking/arscontexta`, a Claude Code plugin for generating local-first, agent-operated knowledge systems from an onboarding conversation. It is not primarily a memory server or vector-store runtime: its retained behavior lives in generated markdown vaults, `CLAUDE.md` context, transformed command skills, hook scripts, queue/config files, and a bundled methodology graph that the plugin uses to justify and evolve the generated system ([README.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/README.md), [.claude-plugin/plugin.json](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/.claude-plugin/plugin.json)).

**Repository:** https://github.com/agenticnotetaking/arscontexta

**Reviewed commit:** [2acfd5cc4473c4d06c46be63df748e77e00e2746](https://github.com/agenticnotetaking/arscontexta/commit/2acfd5cc4473c4d06c46be63df748e77e00e2746)

**Last checked:** 2026-06-01

## Core Ideas

**Conversational derivation is the setup interface.** The plugin-level `/arscontexta:setup` skill conducts a short domain conversation, extracts signals for eight configuration dimensions, applies preset defaults and interaction constraints, proposes a system, then generates the vault. The distinctive claim is derivation rather than template selection: `ops/derivation.md` is written first as the source of truth for subsequent generation, so later files can be regenerated from a persisted rationale rather than the agent's fading conversation context ([skills/setup/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/setup/SKILL.md)).

**The generated vault has three retained spaces.** Every system separates durable domain knowledge, agent self-knowledge, and operational coordination into domain-named `notes/`, `self/`, and `ops/` equivalents. `ops/derivation.md`, `ops/config.yaml`, `ops/derivation-manifest.md`, `ops/methodology/`, `ops/queue/`, and `ops/sessions/` are not side files; they are the system's memory and control plane for future agents ([README.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/README.md), [generators/claude-md.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/generators/claude-md.md), [reference/kernel.yaml](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/reference/kernel.yaml)).

**A generated `CLAUDE.md` is the main operating system.** The Claude Code context template gives the agent session rhythm, discovery-first writing rules, routing tables, pipeline constraints, self-improvement rules, and feature blocks for wiki links, MOCs, schema, maintenance, self-evolution, templates, graph analysis, and optional semantic search. This makes prompt-loaded prose a high-authority system-definition artifact: it tells future agents where to put memory, how to process it, and what checks must happen before a note counts as usable ([generators/claude-md.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/generators/claude-md.md), [generators/features/processing-pipeline.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/generators/features/processing-pipeline.md)).

**Command skills are generated from invariant sources, then vocabulary-transformed.** The plugin ships `skill-sources/*/SKILL.md` templates for reduce, reflect, reweave, verify, validate, seed, ralph, pipeline, tasks, stats, graph, next, learn, remember, rethink, and refactor. Setup reads those templates, transforms vocabulary from `ops/derivation.md`, and writes them into the user's `.claude/skills/` directory; the generated skills then read `ops/derivation-manifest.md` and `ops/config.yaml` at runtime to stay domain-specific without forking the underlying method ([skills/setup/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/setup/SKILL.md), [skill-sources/reduce/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/reduce/SKILL.md), [skill-sources/reflect/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/reflect/SKILL.md)).

**Hooks turn some memory from advice into activation and enforcement.** The checked-in hook config registers a `SessionStart` orientation hook and `PostToolUse` hooks for write validation and async auto-commit. The orientation hook emits the workspace tree, prior session state, goals, identity, recent methodology snippets, and condition-based maintenance signals; the write hook validates note frontmatter fields; the auto-commit hook persists vault changes when enabled ([hooks/hooks.json](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/hooks.json), [hooks/scripts/session-orient.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/session-orient.sh), [hooks/scripts/write-validate.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/write-validate.sh), [hooks/scripts/auto-commit.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/auto-commit.sh)).

**The methodology corpus is both reference material and generator fuel.** The `methodology/` directory contains hundreds of claim-style markdown files, while `reference/kernel.yaml` declares fifteen primitives that generated systems should satisfy. Plugin-level commands such as `/arscontexta:ask`, `/arscontexta:architect`, `/arscontexta:reseed`, and `/arscontexta:upgrade` read this corpus and the local vault's derivation/config state to answer methodology questions or propose changes ([skills/ask/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/ask/SKILL.md), [skills/architect/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/architect/SKILL.md), [reference/kernel.yaml](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/reference/kernel.yaml), [methodology/](https://github.com/agenticnotetaking/arscontexta/tree/2acfd5cc4473c4d06c46be63df748e77e00e2746/methodology)).

## Artifact analysis

- **Storage substrate:** `files` — Plain markdown files in the generated domain notes directory, connected by wiki links and YAML frontmatter
- **Representational form:** `prose` `symbolic` — Prose notes, context files, methodology claims, and skill bodies carry the memory; YAML/frontmatter/config, hook scripts, routing tables, and validation scripts carry symbolic structure
- **Lineage:** `authored` `imported` `trace-extracted` — Generated vaults combine authored plugin templates and methodology, imported user/source material, and session/friction traces promoted through generated workflows
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Notes and methodology advise; `CLAUDE.md`, skills, hooks, config, validators, and session-learning loops instruct, route, validate, warn/enforce, and promote operational learning

**Generated vault notes and MOCs.** Storage substrate: plain markdown files in the generated domain notes directory, connected by wiki links and YAML frontmatter. Representational form: prose with symbolic metadata; optional qmd embeddings are a derived retrieval index, not the authoritative memory. Lineage: derived from user-provided sources, inbox items, research runs, and processing skills; MOC placement and links are generated or updated by `/reflect` and `/reweave`. Behavioral authority: knowledge artifacts when read as evidence or context, and weak system-definition artifacts when `CLAUDE.md` or skills treat descriptions, topics, and MOC membership as required gates.

**Generated `CLAUDE.md` and feature blocks.** Storage substrate: a context file generated from `generators/claude-md.md` and `generators/features/*.md`. Representational form: instructional prose with embedded routing tables and examples. Lineage: assembled from plugin templates, selected feature blocks, user conversation signals, `ops/derivation.md`, and vocabulary transformation rules. Behavioral authority: system-definition artifact with prompt-instruction force; it shapes session orientation, note creation, routing, pipeline compliance, maintenance, and self-improvement.

**Derivation and runtime configuration files.** Storage substrate: `ops/derivation.md`, `ops/config.yaml`, and `ops/derivation-manifest.md` inside the generated vault. Representational form: mixed prose and symbolic YAML. Lineage: `ops/derivation.md` is generated from onboarding signals and coherence checks; `ops/config.yaml` is the live editable state; `ops/derivation-manifest.md` is the machine-readable operational view for inherited skills. Behavioral authority: system-definition artifacts for generation, runtime vocabulary, routing, and later drift detection.

**Generated skills.** Storage substrate: copied/transformed `SKILL.md` files under `.claude/skills/` in the generated vault. Representational form: mixed YAML frontmatter and prescriptive prose. Lineage: authored template sources in `skill-sources/`, transformed by setup using the derivation vocabulary and configuration. Behavioral authority: system-definition artifacts when Claude Code activates a skill; the frontmatter description controls routing, while the body carries procedural instructions, quality gates, and handoff formats.

**Hooks and marker config.** Storage substrate: `.claude/settings.json` hook entries and shell scripts under `.claude/hooks/`, sourced from the plugin's `hooks/` directory, plus the `.arscontexta` marker/config file. Representational form: symbolic JSON and shell code. Lineage: generated or installed from checked-in hook templates, with runtime behavior gated by `.arscontexta`. Behavioral authority: enforcement, scheduling, persistence, and push-context authority; hooks can inject orientation, validate writes, commit changes, and surface maintenance conditions without the agent choosing to search.

**Methodology graph and reference kernel.** Storage substrate: plugin repository files under `methodology/` and `reference/`. Representational form: prose claims, structured reference docs, YAML kernel definitions, and validation scripts. Lineage: authored research/methodology corpus bundled with the plugin; generated vaults reference it through `/ask`, `/architect`, `/reseed`, and setup derivation. Behavioral authority: knowledge artifact when consulted for explanations, and system-definition artifact when setup or architecture skills use it to derive, validate, or recommend concrete vault changes.

**Trace-derived methodology outputs.** Storage substrate: generated vault files under `ops/sessions/`, `ops/observations/`, and `ops/methodology/`. Representational form: session records or transcripts, observation notes, tension notes, and directive methodology notes. Lineage: current hook code records session ids and archives session JSON, while `/remember --mine-sessions` is a skill-defined path from stored session transcripts to methodology notes or observations. Behavioral authority: raw sessions are knowledge artifacts; promoted methodology notes become system-definition artifacts because session-start orientation, `/ask`, `/architect`, and `/rethink` read them as the vault's canonical self-specification ([hooks/scripts/session-orient.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/session-orient.sh), [skill-sources/remember/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/remember/SKILL.md), [skill-sources/rethink/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/rethink/SKILL.md)).

The promotion path is explicit but uneven. Ars Contexta can move material from raw source or session trace, to inbox or session evidence, to notes/observations/tensions, to methodology directives, and sometimes into context-file or config changes. The strongest authority boundary is crossed when `/remember` or `/rethink` turns operational evidence into `ops/methodology/` directives; the weakest part is provenance and invalidation, because generated notes and methodology files do not consistently carry a regenerate-from-source contract.

## Comparison with Our System

| Dimension | Ars Contexta | Commonplace |
|---|---|---|
| Primary purpose | Generate a customized agent-operated vault for a user/domain | Maintain and ship a typed methodology KB and framework |
| Main retained unit | Generated markdown vault plus context file, skills, hooks, config, and methodology corpus | Typed markdown artifacts under collection contracts with validation and review gates |
| Setup model | Conversational derivation into a full system | Repository conventions, skills, commands, and explicit authoring workflows |
| Activation | Hook-injected orientation, skill routing, command invocation, generated context instructions | Mostly deliberate pull through `rg`, indexes, links, skills, and validation/review commands |
| Governance | Kernel primitives, generated validators, hook warnings, health checks, methodology drift loops | Type specs, schemas, collection contracts, semantic review bundles, generated indexes |
| Learning loop | Session/friction capture -> observations/methodology -> rethink/architect/reseed | Workshop/source/review artifacts -> notes/instructions/reference changes through explicit review |

Ars Contexta and Commonplace share the local-file premise: durable agent memory is inspectable markdown plus symbolic metadata and scripts, not an opaque service. The difference is product shape. Ars Contexta is a derivation engine that creates a user's vault and hands it an operating system; Commonplace is itself the maintained methodology library and framework.

Ars Contexta is stronger on initial system generation and runtime activation. Setup is opinionated enough to produce folders, templates, context, skills, hooks, manual pages, and config in one pass. Commonplace has stronger artifact typing and review semantics: path-valued types, collection contracts, validation, and semantic gates make each retained artifact's status and authority easier to audit after the system grows.

The closest Commonplace analogue is the split between library and workshop. Ars Contexta's `ops/` area is a workshop/control plane: queues, sessions, observations, tensions, derivation, config, methodology, and health reports are consumed to keep the vault operating. Its `notes/` graph is the library. Commonplace already has that distinction in principle; Ars Contexta shows a more productized bootstrapping and session-start surface around it.

The main caution is that Ars Contexta sometimes describes stronger automation than this checkout fully wires. The README names a `Stop` session-capture hook that persists session state, and setup documentation describes generating a `session-capture.sh`; the checked-in `hooks/hooks.json` only registers `SessionStart` and `PostToolUse`, and the checked-in session hook records session JSON rather than full transcripts ([README.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/README.md), [hooks/hooks.json](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/hooks.json), [hooks/scripts/session-orient.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/session-orient.sh), [skills/setup/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/setup/SKILL.md)). The session-mining skill is a real retained procedure, but automatic transcript capture appears partially ahead of the installed hook surface at this revision.

**Read-back:** `both` — Agents can pull notes, MOCs, research claims, and skills deliberately, while hooks push retained vault state, maintenance signals, and validation warnings into the agent's path

### Borrowable Ideas

**Derivation record before generation.** Ready to borrow. Writing the derivation/rationale artifact first is a clean way to survive context compaction and make generated systems auditable. Commonplace could use the same pattern for larger scaffold or migration workflows.

**Runtime vocabulary manifest.** Ready for selected workflows. `ops/derivation-manifest.md` separates human rationale from machine-readable vocabulary and folder mapping. Commonplace skills currently rely on collection conventions and repo paths; a compact runtime manifest would help when adapting instructions into consuming projects.

**Hooked session orientation as a real read-back path.** Worth borrowing with a stricter authority contract. Ars Contexta's SessionStart hook pushes tree, goals, identity, methodology snippets, and maintenance counts before work begins. Commonplace could adopt a narrower version for project-local workshop state, while keeping library notes out unless selected by explicit routing.

**Generated skills from canonical sources.** Ready as a packaging pattern. Ars Contexta keeps one set of skill-source templates and transforms them into domain language. Commonplace could reuse this for project installers that need domain-specific command names without forking the underlying procedure.

**Methodology notes as the system's self-specification.** Needs care but is valuable. `/remember` writes directives into `ops/methodology/`, and `/rethink` treats them as the baseline for drift detection. Commonplace has analogous instruction and workshop artifacts, but would need review status and provenance before letting operational friction become authoritative methodology.

**Condition-based maintenance signals at session start.** Ready for workshop areas. Counting observations, tensions, unprocessed sessions, and inbox items is cheap and useful. The Commonplace version should separate "surface a condition" from "decide what to do," as Ars Contexta's `/next` does.

## Trace-derived learning placement

- **Trace source:** `session-logs` `event-streams` — The review identifies session transcripts/current session JSON and current-conversation corrections or redirections as the retained trace signal
- **Learning scope:** `per-project` `cross-task` — Learning is per generated vault, while mined observations and methodology directives can shape later tasks in that vault
- **Learning timing:** `staged` — Session artifacts or current friction are mined later by `/remember --mine-sessions`, then triaged by `/rethink` or used by `/architect`
- **Distilled form:** `prose` `symbolic` — Session evidence becomes observation/methodology prose and can later inform config, context, validation, or architecture changes

**Trace source.** Ars Contexta qualifies through the generated `/remember --mine-sessions` path and its supporting session infrastructure. The intended raw signal is stored session transcripts in `ops/sessions/*.md`, plus corrections and redirections in the current conversation for contextual mode. The checked-in SessionStart hook records session ids and archives `ops/sessions/current.json`, while docs and kernel references still describe fuller transcript capture; therefore the durable trace-learning path is implemented as a generated skill workflow, with automatic transcript capture only partially evidenced in the current hooks ([skill-sources/remember/SKILL.md](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/remember/SKILL.md), [hooks/scripts/session-orient.sh](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/session-orient.sh), [reference/kernel.yaml](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/reference/kernel.yaml)).

**Extraction.** `/remember` has three modes: explicit user-provided friction, contextual detection of recent corrections, and session mining. Session mining scans unmined sessions for corrections, repeated redirections, workflow breakdowns, agent confusion, undocumented decisions, and escalation patterns. It then creates methodology notes for actionable behavioral changes or observation notes for signals needing more evidence, deduplicates against existing methodology/observation files, and marks sessions as mined.

**Scope and timing.** Scope is per generated vault. Timing is staged: a hook or user process creates session artifacts, `/remember --mine-sessions` mines them later, `/rethink` triages accumulated observations/tensions and methodology notes, and `/architect` can use health plus friction patterns to propose system changes. This is not online model learning; it is trace-to-prose and trace-to-instruction promotion in a file-backed operating layer.

**Survey placement.** On the trace-derived survey axes, Ars Contexta belongs in trace-to-methodology and trace-to-configuration-advice, not weight learning. It strengthens the claim that useful operational learning can be expressed as reviewed directives and drift checks. It also shows the fragile boundary: unless trace capture, provenance, deduplication, and promotion review are all wired, the system may have a strong learning procedure but a weak evidence chain.

## Read-back placement

**Direction.** Ars Contexta uses both pull and push. Pull includes `/ask`, `/architect`, `/health`, `/next`, qmd/grep search, reading notes/MOCs, and command skill invocation. Push includes hook-driven session orientation, write validation feedback, and condition messages emitted before the agent starts ordinary work. Auto-commit is hook-driven persistence rather than cognitive read-back.

**Read-back signal:** `coarse` `identifier` — SessionStart emits coarse vault/session orientation and maintenance conditions; PostToolUse write validation targets the written file by path

**Read-back timing:** `pre-action` `post-action` — Session orientation fires before work, while write validation fires after a write and can shape the next correction

**Faithfulness tested:** `no` — The review found structural activation and scope controls, but no ablation or post-action audit proving intended behavioral effect

**Targeting and signal.** The `SessionStart` push is `coarse`: it fires from a session-boundary symbol in any detected Ars Contexta vault and emits generic retained orientation from session state, goals, identity, recent methodology snippets, and count-based maintenance conditions. It is engineered by timing and scope limits, not by instance relevance. The `PostToolUse` `Write` validation path is `instance` targeting with an `identifier` signal: the hook reads the `tool_input.file_path`, narrows to `*/notes/*` or `*/thinking/*`, then emits warnings for that written file. Precision, recall, context dilution, and effective authority of the pushed material are not verified from code.

**Timing relative to action.** Session orientation fires before work and can change the next action by surfacing goals, identity, methodology, and maintenance conditions. Write validation fires after a write, so it can affect the next correction but not the write that already happened. Auto-commit is asynchronous persistence, not cognitive read-back.

**Selection, scope, and complexity.** Scope is intentionally bounded: tree output is limited to three levels and markdown files; methodology snippets are the first three lines of the five newest files; conditions are simple counts for observations, tensions, archived sessions, and inbox files. This limits volume but not necessarily authority: even a short condition line can steer the next action.

**Authority at consumption.** Hook-injected orientation has advisory-to-instruction force because it enters the agent context without a search decision. Write validation has warning/enforcement force through `additionalContext`, but the shell script emits warnings rather than blocking writes. Auto-commit has persistence authority in git-enabled vaults. Generated skills have stronger procedural authority when invoked, but their activation depends on the host skill router or user command.

**Faithfulness.** I did not find an ablation or post-action audit proving that pushed orientation changes agent behavior in the intended direction. The implementation shows structural activation and scope controls; behavioral faithfulness remains a runtime quality question.

**Other consumers.** Humans consume the same system through the README, generated manual pages, MOCs, health reports, and git history. Shell hooks, qmd, and generated scripts consume symbolic files; meta-skills consume methodology and config as governance inputs.

## Curiosity Pass

Ars Contexta is more generator than memory runtime. The memory system it creates is a file-backed cognitive architecture: context, skills, hooks, queue, config, methodology, and notes. That makes it closer to a Commonplace installer than to mem0/Letta-style service memory.

The strongest idea is the authority ladder from notes to methodology to context/config/hooks. The repo repeatedly distinguishes ordinary knowledge, operational learning, and hardening into validation or hooks. That is exactly the axis most memory-system reviews need, even when the project itself uses different terminology.

The weakest implementation seam is session capture. The methodology and README emphasize transcript capture, mining, and session-end persistence, but the checked-in hook config at this commit has no `Stop` hook and the current orientation hook saves session metadata rather than transcript content. The trace-derived tag is justified by the generated `/remember` promotion workflow, not by a fully verified automatic transcript pipeline.

The generated skills are verbose by design. They encode anti-shortcut language, quality gates, and command-specific procedures. That improves behavioral authority when the right skill loads, but it shifts the context-cost problem to skill routing and description budgets.

The optional qmd integration is treated as an enhancer, not the system's substrate. Ars Contexta still works through markdown, wiki links, MOCs, ripgrep, and hooks if semantic search is absent. That is a useful local-first constraint.

## What to Watch

- Whether the checked-in hook suite converges with the setup docs by adding a real `Stop` transcript-capture hook or revising the docs/kernel to match SessionStart-only session metadata.
- Whether generated methodology notes gain stronger provenance fields tying them to session ids, transcript spans, prompts, and reviewer decisions before they become canonical self-specification.
- Whether `/rethink` and `/architect` evolve from proposal workflows into reviewed, typed promotion paths with explicit approval records.
- Whether skill activation descriptions and generated command names get tested the way Ars Contexta tests note retrieval and schema quality; skill routing is now a major read-back surface.
- Whether qmd integration remains optional or becomes part of the kernel for larger vaults, which would shift the representational form of retrieval from mostly prose/symbolic toward mixed symbolic/distributed indexes.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Ars Contexta needs separate treatment for generated notes, context files, skills, hooks, config, methodology, and trace-derived directives.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Ars Contexta has explicit hook and skill paths that move some stored files into future context.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: `/remember --mine-sessions` turns session evidence into observations or methodology directives.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: generated `CLAUDE.md`, skills, hooks, config, validators, and methodology directives instruct, route, validate, or enforce behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw sessions, research claims, notes, MOCs, health reports, and source captures advise until a read path grants stronger authority.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares: Ars Contexta's `ops/` space is a generated workshop/control plane around the durable notes graph.
