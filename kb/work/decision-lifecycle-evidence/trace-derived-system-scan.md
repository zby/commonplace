# Trace-derived systems: evidence capture and search triggers

## Scope and evidence boundary

Commissioned by the operator on 2026-09-26 to broaden the
[session-evidence design map](./session-evidence-triggers.md) to all systems
marked as deriving retained material from traces, including the older
agent-memory collection.

“Trace derived” maps to two existing markings: the older `trace-learning`
tag and `trace-extracted` lineage, and the newer normalized `trace_learning`
assessment. They do not mean the same thing. Raw trace preservation can have
trace-extracted lineage without a learning loop. Conversely, a newer review
can count a retained continuation summary as trace learning without claiming
cross-task knowledge or improvement.

Scanned at repository revision
`f54a2e90bcdd00e5df8490e2aa1e1d55e90db37c`:

- **105 tagged older entries:** 100 reviews and five lightweight entries.
- **Nine additional older reviews** positively declaring trace-extracted
  lineage without that tag. Negative mentions of the lineage were excluded.
- **30 newer exact analyses** marked trace learning `yes`: 28 selected by the
  [comparison table](../../agentic-systems/comparisons/memory-systems-table.md),
  plus oh-my-pi and Prime Agent from their exact results. All 30 result hashes
  matched their public-review receipts. The table alone would miss two.

These are entry counts, not distinct-system counts; some systems occur in
both collections at different revisions or scopes. This pass inspected
reported trace sources, timing, write routes, and relevant limitations. It
did not rerun upstream systems or refresh their reviews. A code-grounded
review can still describe a particular operation as merely instructed or
afforded. The inventory preserves those limits.

The [older trace-learning survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md)
helped navigation, but individual reviews control this scan. For example,
the survey describes a Pi distillation extension under Napkin; the current
[Napkin review](../../agent-memory-systems/reviews/napkin.md) explicitly bounds
the inspected package to storage and retrieval, with host distillation
outside it. Napkin is therefore not counted as a currently marked mining
implementation here.

## Findings that change the design map

**There are two independent questions: when to look, and what warrants
retention.** A hook, timer, or backlog threshold creates an opportunity. A
user correction, failed attempt, repeated problem, settled choice, or missing
answer supplies a reason to examine particular evidence. Many systems combine
the two. Commonplace should avoid making a generic session boundary do both
jobs implicitly.

**Capture should have weaker selection than promotion.** Tracecraft and Pond
preserve material without deciding which lesson it teaches. DocMason can
promote grouped interaction evidence without writing a new rule. Ars Contexta,
Enoch, and ARIS keep intermediate observations or proposals before changing
instructions. This supports separate source, evidence, proposal, and adopted
decision stages; it does not select their storage format.

**Search failure can itself be a trigger.** A missing answer, repeated
correction, or recurring failed command can launch a search over prior work.
This extends the earlier candidate beyond planned lifecycle milestones.
However, retrieval from a warm index is not evidence retention: a subsequent
step must copy essential evidence into an owned record if it is to survive
loss of the source.

**Success-based selection is unsuitable as the only evidence filter.**
Voyager, OS-Copilot, SkillWeaver, and workflow induction favor successful
reusable artifacts. That can serve skill libraries while discarding the
failures needed to assess improvement. ModularRSI's paired success/failure
investigation and ReasoningBank's separate treatment of both outcomes are
closer to this workshop's evaluation needs. Neither establishes causal truth
merely by retaining both sides.

**Demand and activity are useful priorities, not complete coverage.** Heat,
turn counts, tool counts, queue depth, and invocation counts can allocate
extraction effort. They can also overlook one consequential decision, a quiet
abandoned task, or a session that ended in failure. Source-loss protection
still needs an independent route.

## Most relevant mechanisms from the expanded scan

| Mechanism and evidence | Trigger and retained result | Consequence for this workshop |
|---|---|---|
| [Pond](../../agent-memory-systems/reviews/pond.md) and [Tracecraft](../../agent-memory-systems/reviews/tracecraft.md) | Pond syncs client traces manually, periodically, or at lifecycle boundaries into a canonical indexed corpus. Tracecraft's mirror tails harness sessions, redacts copied data, uploads append-disjoint parts, and records cursor ranges. | Concrete source-preservation options before choosing an extraction question. Pond canonicalizes; Tracecraft mirrors. Neither should be described as a semantic lesson extractor, and their adapters' omissions still matter. |
| [DocMason](../../agent-memory-systems/reviews/docmason.md) | Hooks and transcript reconciliation collect interaction entries; sync groups conversations, copies attachment context, validates/publishes interaction memories, and records promotion IDs. | An intermediate evidence artifact can be mostly deterministic. Marking source entries promoted is separate from deciding what architectural claim they support. |
| [cass-memory](../../agent-memory-systems/reviews/cass_memory_system.md) | Reflection over a session or batch first extracts diaries, then consults related history to propose deltas; validation checks additions against session evidence before curation. Processed logs suppress repeat reflection. | A two-stage search can use cheap episode accounts to select deeper evidence. A per-session processed flag would need a question/version dimension for our open-ended future searches. |
| [Ars Contexta](../../agent-memory-systems/reviews/arscontexta.md) | `/remember` targets corrections, redirections, confusion, undocumented decisions, and workflow failures; `/rethink` consumes accumulated observations and tensions to choose a disposition. | Especially close to the motivating ADR mistake. Most semantic extraction is skill procedure; the review does not establish a complete automatic transcript-ingestion implementation. |
| [cq](../../agent-memory-systems/reviews/cq.md) and [SkillNote](../../agent-memory-systems/reviews/skillnote.md) | cq instructs capture when an insight stabilizes, with session-end reflection as a backstop. SkillNote detects explicit save/convention phrases in user prompts and writes pending drafts. | Semantic triggers can operate before session end. Preserve the source slice: cq does not independently retain enough raw lineage to reconstruct each candidate. Phrase detection also misses implicit decisions. |
| [deja-vu](../../agent-memory-systems/reviews/deja-vu.md) and [llm-project-wiki](../../agent-memory-systems/reviews/llm-project-wiki.md) | deja-vu uses prompts about earlier work, imminent file edits/commands, and failed commands to retrieve relevant past sessions. llm-project-wiki instructs agents to record a gap when later work exposes missing knowledge, then address it at ingest/audit. | Current need and failure are concrete search triggers. The former primarily retrieves; the latter records a demand for later acquisition. Neither alone supplies the essential evidence retention policy. |
| [MemPalace](../../agent-memory-systems/reviews/mempalace.md), [mem0](../../agent-memory-systems/reviews/mem0.md), and [Signet](../../agent-memory-systems/reviews/signetai.md) | MemPalace combines configured Stop intervals, precompaction capture, and backfill. mem0 combines every-third-substantial-prompt capture, Stop, and compaction routes. Signet extracts transcript deltas at checkpoints as well as session-end/compaction events. | Multiple opportunities cover long-lived sessions better than session-end alone. They still require proof of completed capture and correct delta boundaries. A Stop event is not necessarily a closed session. |
| [Hermes Agent](../../agent-memory-systems/reviews/hermes-agent.md) and [Prime Agent](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/result.md) | Hermes uses user-turn and tool-loop cadences for background review. Prime Agent uses explicit refinement or automatic interval/compaction review, with a reviewer deciding whether extraction should run. | Cheap eligibility/review can precede expensive extraction. Hermes skips interrupted turns and lacks per-entry source links in the inspected route; these are gaps for evidence retention. |
| [MemoryOS](../../agent-memory-systems/reviews/MemoryOS.md), [Spacebot](../../agent-memory-systems/reviews/spacebot.md), and [Continuity](../../agent-memory-systems/reviews/continuity.md) | MemoryOS extracts from hot mid-term sessions; Spacebot uses message/time/event-density thresholds; Continuity checks debounce, staleness, and unabsorbed learning signals. | Prioritize by use, activity, or backlog. Heat can favor already-retrieved material; low activity does not imply low evidential value. |
| [Enoch, RTE-11](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-enoch-01/result.md) | Threshold, explicit, or scheduled scans select unscanned conversation turns and changed task snapshots; isolated extraction produces referenced signals and scan records; later synthesis and curation propose work for human admission. | The closest inspected decomposition of scan coverage → evidence → proposal → disposition. Scheduled proposal delivery does not itself approve or launch implementation. |
| [ARIS](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) and [CORAL](../../agent-memory-systems/reviews/CORAL.md) | ARIS logs events/reviewer traces and reminds after enough skill invocations; explicit meta-optimization stages patches for separate application. CORAL records attempts, scores, and checkpoints, then uses heartbeat prompts for consolidation or reflection. | A deterministic trigger can commission an evidence review without automatically adopting its interpretation. CORAL links an attempt to contemporaneous shared state, useful for before/after reconstruction. |
| [ModularRSI, RTE-1/2](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/result.md) | Completed-task batches trigger background reflection. Classification routes mixed outcomes, fixable failures, and cooldown cases; investigators compare same-task successes/failures where possible and retain structured findings. | Outcome differences and repeated failure can select valuable evidence. Keep infrastructure failures visible even if excluded from semantic diagnosis; selection exclusions are part of an evaluation's denominator. |
| [HALO](../../agent-memory-systems/reviews/halo.md), [PrimeScientist, RTE-5/8](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-primescientist-01/result.md), and [SoL-Pi, RTE-6](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/result.md) | HALO stages diagnostic work over selected traces with bounded drill-down. PrimeScientist supplies compact diagnostics and retained raw-trace pointers when expanding an evaluated node. SoL-Pi selects bounded exact quotations from archived tool diagnostics and validates the smaller receipt. | Search can progress from overview to specific spans rather than loading whole sessions. Retain enough source and locators to inspect an extracted claim later. Compact diagnostics are not a substitute for the original failure evidence. |

## Implications to carry into a proposal

Extend the candidate policy with **exception-driven searches**: a user
correction, recurring failure, unexpected result, or retrieval gap can trigger
a focused evidence search before ordinary closure. Treat the reason to search
separately from the host event that gives the search execution time.

Compare three concrete routes on the ADR episode: immediate capture of the
operator's correction; a later focused search over a retained session; and
periodic broad extraction. Assess which preserves the original choice,
mistaken placement, implementation state, and correction without turning
the agent's later diagnosis into a contemporaneous fact.

Add two probes to the earlier design map: a long-lived session with useful
new evidence after its first extraction, and a rare consequential decision
that never crosses an activity threshold. Test whether raw-source capture
still works when the semantic extractor fails or has no budget.

No inspected mechanism establishes a general guarantee that third-party
sessions will be searched before deletion. Owned archives can remove that
particular dependency only for material successfully copied and retained.
Archival capture, examination, evidence acceptance, and instruction adoption
need separate completion claims.

## Coverage register

The following register keeps every selected entry discoverable, including
ones that add little to session mining. Older timing cells are short excerpts
from their declared learning-timing paragraphs, with ellipses where shortened;
they are navigation aids, not newly verified classifications. A missing timing
declaration is recorded explicitly. The newer register names the inspected
route and preserves its trace-learning evidence basis.

### Older tagged entries (105)

| Entry | Declared source tier | Reported timing (excerpt) |
|---|---|---|
| [IsaacCLupus_mnemosyn_spec](../../agent-memory-systems/lightweight/IsaacCLupus_mnemosyn_spec.md) | doc-grounded | `online` `staged` — Conversations and receipts are recorded during use; profile extraction, heat decay, memory promotion, audit, and publish are described as staged jobs or approval steps. |
| [agemem](../../agent-memory-systems/lightweight/agemem.md) | doc-grounded | No standard learning-timing declaration; inspect the linked lightweight account. |
| [incremental-self-improvement](../../agent-memory-systems/lightweight/incremental-self-improvement.md) | doc-grounded | No standard learning-timing declaration; inspect the linked lightweight account. |
| [nams](../../agent-memory-systems/lightweight/nams.md) | doc-grounded | `staged` — a trigger starts a pollable job, memory is allowed to settle under a workspace lock, the candidate passes generation and gates, and human review precedes publication. |
| [trajectory-informed-memory-generation](../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) | doc-grounded | No standard learning-timing declaration; inspect the linked lightweight account. |
| [AI-Context-OS](../../agent-memory-systems/reviews/AI-Context-OS.md) | code-grounded | `staged` — The trace store updates online during context serving, but optimization records are produced when `run_optimization_analysis` is invoked. |
| [Agent-S](../../agent-memory-systems/reviews/Agent-S.md) | code-grounded | `online` `offline` `staged` — S1/S2 write summaries during or at the end of normal inference runs; default KB imports and BBON evaluation/fact-caption generation are offline/staged script workflows. |
| [AgentFly](../../agent-memory-systems/reviews/AgentFly.md) | code-grounded | `staged` — Case rows are appended online during benchmark execution, but parametric learning is a separate offline training step that writes checkpoints. |
| [AriGraph](../../agent-memory-systems/reviews/AriGraph.md) | code-grounded | `online` — TextWorld memory updates happen during the acting loop before each planning/action decision; QA memory is built before answering each question. |
| [Auto-claude-code-research-in-sleep](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) | code-grounded | `offline` `staged` — Logging happens during normal operation, but `/meta-optimize` analyzes accumulated traces after the fact; landing is staged through pending patches and `/meta-apply`. |
| [CORAL](../../agent-memory-systems/reviews/CORAL.md) | code-grounded | `online` `staged` — Attempt records, logs, eval counters, checkpoints, and resume prompts update during operation; consolidation, role evolution, skill creation, note organization, and warm-start research are staged agent tasks triggered … |
| [Kompl](../../agent-memory-systems/reviews/Kompl.md) | code-grounded | `online` — The candidate draft is created during the chat request after synthesis succeeds. |
| [LLM-WIKI-MCP](../../agent-memory-systems/reviews/LLM-WIKI-MCP.md) | code-grounded | `online` `staged` - Ask turns and metrics are recorded immediately after the ask path runs; compression and recursive-context assembly happen as a staged maintenance/read step when history exceeds budget or future prompts are built. |
| [Memori](../../agent-memory-systems/reviews/Memori.md) | code-grounded | `online` `staged` - Registered SDK calls persist and augment after each model response; collector augmentation is background/best-effort after durable turn writes; Rust and Python augmentation workers process jobs asynchronously and expose … |
| [MemoryOS](../../agent-memory-systems/reviews/MemoryOS.md) | code-grounded | `online` — Writes, condensation triggers, heat updates, extraction, retrieval, generation, and write-back happen during normal use; `force_mid_term_analysis()` can manually lower the threshold for testing. |
| [MiroShark](../../agent-memory-systems/reviews/MiroShark.md) | code-grounded | `online` `staged` — graph memory updates can run during simulation, report traces are captured during report generation, and community summaries/export surfaces are built or served in later stages. |
| [OS-Copilot](../../agent-memory-systems/reviews/OS-Copilot.md) | code-grounded | `online` `staged` — ordinary task execution can promote a successful Python subtask immediately; self-learning runs staged lesson sequences through the same agent loop. |
| [OpenSage](../../agent-memory-systems/reviews/OpenSage.md) | code-grounded | `online` `offline` `staged` — Tool-result observation, history compaction, message-board append/read, and file memory happen during runs; evaluation export and RL handoff happen after benchmark or rollout execution; generated Skills are … |
| [Pratiyush--llm-wiki](../../agent-memory-systems/reviews/Pratiyush--llm-wiki.md) | code-grounded | `offline` `staged` — Conversion and synthesis run after traces already exist, either by explicit command or external hook; the agent-delegate backend stages pending prompts for a later slash-command completion step. |
| [REM](../../agent-memory-systems/reviews/REM.md) | code-grounded | `online` `staged` — Parsing, embedding, and episode storage happen during the write path; consolidation is queued or scheduled and would run later when enough unconsolidated episodes exist. |
| [Self-Training-LLM](../../agent-memory-systems/reviews/Self-Training-LLM.md) | code-grounded | `offline` — The scripts generate data, train, then evaluate in batches. I did not find an online loop that updates a deployed model during interaction. |
| [SkillRL](../../agent-memory-systems/reviews/SkillRL.md) | code-grounded | `offline` `staged` — The SFT pipeline and shipped SkillBanks are batch-generated. During RL, dynamic update can run at validation/test frequency or configured training update frequency, but new skills affect later training prompts rather … |
| [SkillWeaver](../../agent-memory-systems/reviews/SkillWeaver.md) | code-grounded | `online` `staged` — During exploration, a successful iteration can update the KB before later iterations; evaluation and demo runs can also load a previously staged KB prefix. |
| [SkillX](../../agent-memory-systems/reviews/SkillX.md) | code-grounded | `offline` `staged` — The ordinary pipeline builds and saves libraries in batch epochs. Expansion can add new synthetic trajectories between epochs when configured, but the inspected inference service does not update the library during a … |
| [TheKnowledge](../../agent-memory-systems/reviews/TheKnowledge.md) | code-grounded | `offline` `staged` - Filter examples are accumulated online as operations run, but distillation into a candidate policy is a separate `wiki finetune --distill` step and live promotion is not automatic. |
| [WeKnora](../../agent-memory-systems/reviews/WeKnora.md) | code-grounded | `online` `offline` `staged` - Pure-chat memory is retrieved online before completion and stored asynchronously after completion; wiki ingest is staged through task queues, per-KB locks, retries, and dead letters; document parsing/indexing … |
| [Zikkaron](../../agent-memory-systems/reviews/Zikkaron.md) | code-grounded | `online` `staged` — `remember`, recall heat boosts, reconsolidation, hooks, and prompt recall happen online; consolidation, sleep compute, action-log processing, compression, and seeding are staged cycles or explicit commands. |
| [ace](../../agent-memory-systems/reviews/ace.md) | code-grounded | `online` `offline` `staged` — Offline mode trains on train samples and validates periodically; online mode tests each window with the current playbook and then trains on that window; saved playbooks create a staged handoff into later … |
| [agent-r](../../agent-memory-systems/reviews/agent-r.md) | code-grounded | `offline` `staged` — MCTS data collection, path-to-training-data conversion, external Xtuner training, and evaluation are separate offline stages. The evaluated agent does not update a memory store online while solving a test task. |
| [agent-skills-for-context-engineering](../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) | code-grounded | `offline` `staged` - Traces are captured during execution, then analyzed and distilled across loop iterations before artifacts or generated skills are written. |
| [agent-workflow-memory](../../agent-memory-systems/reviews/agent-workflow-memory.md) | code-grounded | `online` `offline` `staged` — Mind2Web supports offline induction from training data and online induction after batches of test examples; WebArena's pipeline stages run, evaluation, and workflow update steps. |
| [agentic-harness-engineering](../../agent-memory-systems/reviews/agentic-harness-engineering.md) | code-grounded | `staged` — Evaluation writes traces, analysis writes reports, evolution edits the workspace, and the next iteration evaluates whether the prior edit helped or hurt. |
| [agentic-local-brain](../../agent-memory-systems/reviews/agentic-local-brain.md) | code-grounded | `online` — chat turns and reading-history events are recorded during web/API interactions and can affect later calls or recommendations. |
| [ai-memex-cli](../../agent-memory-systems/reviews/ai-memex-cli.md) | code-grounded | `offline` `staged` — `memex distill` converts a current/latest or specified session after it exists, and ingest later turns the raw session source into wiki knowledge. |
| [amazon-science--SAGE](../../agent-memory-systems/reviews/amazon-science--SAGE.md) | code-grounded | `offline` `staged` — expert-data extraction and SFT are offline; the GRPO loop stages first-subtask skills into the second subtask within a training rollout before policy updates. |
| [arscontexta](../../agent-memory-systems/reviews/arscontexta.md) | code-grounded | `online` `offline` `staged` — Explicit/contextual `/remember` can run during work; session mining runs later over stored sessions; `/rethink` stages triage, pattern detection, proposals, and approved implementation. |
| [auto-harness](../../agent-memory-systems/reviews/auto-harness.md) | code-grounded | `online` `staged` — The loop learns after each benchmark/gate cycle: run, inspect failures, edit, gate, record, update learnings, repeat. |
| [autocontext](../../agent-memory-systems/reviews/autocontext.md) | code-grounded | `online` `staged` — Playbooks, hints, role outputs, telemetry, dead ends, and context-selection records update during runs; production-trace ingest, distillation, exports, and training are staged workflows. |
| [basic-memory](../../agent-memory-systems/reviews/basic-memory.md) | code-grounded | `online` `staged` — The checkpoint fires during the agent lifecycle just before compaction; reflection is a staged skill workflow when run by cron, heartbeat, or explicit request. |
| [beever-atlas](../../agent-memory-systems/reviews/beever-atlas.md) | code-grounded | `online` `staged` — Sync/extraction/persistence happen during ingestion jobs, while settled-memory summarization and wiki maintenance are staged behind dirty flags, queues, debounces, and manual/auto modes. |
| [browzy-ai](../../agent-memory-systems/reviews/browzy-ai.md) | code-grounded | `online` `staged` — Sessions and activity logs are written during use; digest generation happens on a later startup, and crystallized insight drafting runs asynchronously after a qualifying answer. |
| [byterover-cli](../../agent-memory-systems/reviews/byterover-cli.md) | code-grounded | `online` `staged` — Search access hits and curate sidecar updates happen during ordinary task execution, while curation sessions, review approval/rejection, dream scans, finalization, and version-control sync are staged workflows. |
| [cass_memory_system](../../agent-memory-systems/reviews/cass_memory_system.md) | code-grounded | `online` `offline` `staged` — Context logging, manual feedback, outcome application, and MCP writes can happen online; `cass` history and local files work offline once present; reflection, onboarding, validation, and trauma scanning are … |
| [claude-context-guard](../../agent-memory-systems/reviews/claude-context-guard.md) | code-grounded | `online` `staged` - The template asks agents to update safeguard files incrementally during work, while `/save`, `/end`, `/start`, `/audit`, `/itemise`, pre-commit reminders, and pre-compaction backups are staged occasions. |
| [claude-obsidian](../../agent-memory-systems/reviews/claude-obsidian.md) | code-grounded | `online` `staged` — Save, ingest, hot-cache updates, log updates, and hook reads happen during ordinary agent sessions; chunking, BM25 rebuilds, methodology-mode setup, linting, DragonScale folds, and autoresearch are staged workflows. |
| [claude-workstream-kit](../../agent-memory-systems/reviews/claude-workstream-kit.md) | code-grounded | `online` `staged` - Workstream files are updated during work and session exit, while creation, work, handoff, close, and session-start reconciliation are staged skill/hook occasions. |
| [clawvault](../../agent-memory-systems/reviews/clawvault.md) | code-grounded | `online` `staged` — Hook-time checkpointing, prompt context selection, fact extraction, and observer cursor updates can happen during operation; `sleep`, `wake`, `reflect`, `maintain`, embedding rebuilds, and QMD updates are staged … |
| [cludebot](../../agent-memory-systems/reviews/cludebot.md) | code-grounded | `online` `offline` `staged` — Store-time embeddings, tags, links, access reinforcement, event-triggered reflection, and MCP writes can happen online; local SQLite/JSON and MemoryPack operations can run offline; dream cycles, compaction, … |
| [cognee](../../agent-memory-systems/reviews/cognee.md) | code-grounded | `online` `staged` — Decorator/session writes and session completion storage happen during operation; `improve()`, memify pipelines, global-context indexing, feedback-weight application, and graph-to-session sync are staged workflows. |
| [compound-engineering-plugin](../../agent-memory-systems/reviews/compound-engineering-plugin.md) | code-grounded | `online` `staged` — Skill runs write artifacts during the current task, but the extraction and maintenance loops are staged workflows: compounding after a solved problem, refresh after drift evidence, product pulse on a time window, and … |
| [continuity](../../agent-memory-systems/reviews/continuity.md) | code-grounded | `online` `staged` — Memory writes and learning records can happen during conversations; narrative synthesis is staged on launch, after a debounce, when stale, or when enough unabsorbed learning signals accumulate. |
| [cortex](../../agent-memory-systems/reviews/cortex.md) | code-grounded | `online` — Query logging, read access counting, feedback recording, and threshold promotion happen during normal CLI/MCP/dashboard use; demotion through `adjust_tiers()` requires an explicit call path. |
| [cq](../../agent-memory-systems/reviews/cq.md) | code-grounded | `online` `staged` — The skill prefers immediate mid-task proposals when an insight stabilizes; `/cq:reflect` is a staged session-end backstop; remote review is another staged gate before shared read-back. |
| [crewai-memory](../../agent-memory-systems/reviews/crewai-memory.md) | code-grounded | `online` `staged` — Crew and kickoff saves happen in the runtime path after producing output, often through background `remember_many`; HITL lessons are distilled during feedback handling; recall-time `last_accessed` updates and storage … |
| [decapod](../../agent-memory-systems/reviews/decapod.md) | code-grounded | `online` `staged` — Event capture and worker lesson creation happen during operation; LCM summary, procedural promotion, validation/proof baselines, internalization creation, and graph export are staged or explicit commands. |
| [deja-vu](../../agent-memory-systems/reviews/deja-vu.md) | code-grounded | `staged` — Indexing happens when commands such as search, warmup, stats, sync export, or MCP recall ensure the cache; the Claude hook intentionally reads only an already-warm index. |
| [dense-mem](../../agent-memory-systems/reviews/dense-mem.md) | code-grounded | `online` `staged` — Live `remember` calls process current conversation evidence online; historical imports and skill-pack imports are staged/reviewed paths, with auto-promotion off by default for historical imports. |
| [docmason](../../agent-memory-systems/reviews/docmason.md) | code-grounded | `online` `staged` — Hooks and native reconciliation capture traces during operation; durable promotion happens during sync and publish, after grouping, metadata normalization, validation, and publication. |
| [dynamic-cheatsheet](../../agent-memory-systems/reviews/dynamic-cheatsheet.md) | code-grounded | `online` — Each processed example can update memory for the next example in the same sequential run. |
| [echoes-vault-opencode](../../agent-memory-systems/reviews/echoes-vault-opencode.md) | code-grounded | `online` `staged` - Scratchpad writes happen during the session, while `/echoes-end` is a staged end-of-session distillation command. |
| [eidetic](../../agent-memory-systems/reviews/eidetic.md) | code-grounded | `online` `staged` — SessionStart read-back and indexing happen online at session start; Stop-hook extraction runs asynchronously at session end; vector/index rebuilds, lint, doctor, vault export, and manual promotion are staged operations. |
| [equipa](../../agent-memory-systems/reviews/equipa.md) | code-grounded | `online` `staged` — Prompt read-back and telemetry capture happen during orchestration; Q-value/session updates happen between cycles; ForgeSmith, SIMBA, and GEPA are staged improvement passes. |
| [expel](../../agent-memory-systems/reviews/expel.md) | code-grounded | `online` `offline` `staged` - Training accumulates traces online; `insight_extraction.py` performs an offline/staged distillation pass; `eval.py` can create or load fold rules before evaluation and performs prompt-time retrieval during … |
| [g-memory](../../agent-memory-systems/reviews/g-memory.md) | code-grounded | `staged` - Raw task records are written after each task; insight finetuning starts after a threshold and repeats every configured number of rounds, while rule merging runs every 20 stored tasks. |
| [gbrain](../../agent-memory-systems/reviews/gbrain.md) | code-grounded | `online` `offline` `staged` — `extract_facts` and the facts backstop can run inline or queue near a write; dream-cycle phases and skillopt are staged/offline maintenance; sync/import and eval capture can run continuously as background side … |
| [graphiti](../../agent-memory-systems/reviews/graphiti.md) | code-grounded | `online` `staged` — MCP writes are queued and processed asynchronously per group; SDK/API ingestion can run during application operation or as a background task; community building and index/constraint setup are explicit staged operations. |
| [halo](../../agent-memory-systems/reviews/halo.md) | code-grounded | `offline` `staged` — Traces are captured or imported first, then selected/exported and analyzed through a queued local HALO run. Engine telemetry can stream during the analysis run, but the durable learning artifact is produced after a … |
| [hermes-agent](../../agent-memory-systems/reviews/hermes-agent.md) | code-grounded | `online` `staged` — The review runs asynchronously after a qualifying live turn, so learning can affect a later turn or session without an offline batch. Counter thresholds make it periodic, and approval mode inserts a staged pending-diff … |
| [hindsight](../../agent-memory-systems/reviews/hindsight.md) | code-grounded | `online` `staged` — Hooks can retain after turns and recall before prompts during normal agent operation; async retain, background consolidation, graph maintenance, file conversion, and mental-model refresh are staged worker operations. |
| [hyperagents](../../agent-memory-systems/reviews/hyperagents.md) | code-grounded | `offline` `staged` — Meta-agent editing, staged evaluation, full evaluation, archive append, parent selection, ensemble evaluation, and plotting are separate outer-loop stages. The checked-in task agent does not update a memory store … |
| [kenhuangus--llm-wiki](../../agent-memory-systems/reviews/kenhuangus--llm-wiki.md) | code-grounded | `online` `staged` — Metrics are recorded as pipeline tools run; prompt optimization, research hypotheses, validation, and paper generation run on daemon schedules. |
| [lacp](../../agent-memory-systems/reviews/lacp.md) | code-grounded | `online` `staged` `offline` - Stop hooks write trace-extracted state online; `brain-expand` promotes staged signals and synthesizes epochs in a staged workflow; RAG builds, promotion suggestions, consolidation, probes, and benchmark … |
| [letta](../../agent-memory-systems/reviews/letta.md) | code-grounded | `online` `staged` — Foreground tool writes and compaction happen during or around agent steps; sleeptime agents run after turns or at configured frequency; document-sleeptime ingestion is triggered after source/file events. |
| [link](../../agent-memory-systems/reviews/link.md) | code-grounded | `staged` — Trace material is saved, proposed, reviewed, and accepted in separate steps; Link does not silently learn durable memory from every live turn. |
| [llm-project-wiki](../../agent-memory-systems/reviews/llm-project-wiki.md) | code-grounded | `online` `staged` — Gap capture happens during the future task that discovered the missing knowledge; resolution is staged into the next ingest or gap-audit pass. |
| [llm-wiki](../../agent-memory-systems/reviews/llm-wiki.md) | code-grounded | `online` `staged` — Lesson extraction runs during or at the end of the current session; dry-run and article update stages make promotion staged rather than silent. Research/audit provenance is appended during those workflows and reused … |
| [mem0](../../agent-memory-systems/reviews/mem0.md) | code-grounded | `online` `staged` - SDK adds run during requests, UserPromptSubmit auto-capture runs in the background every third substantial prompt, Stop and PreCompact hooks capture at lifecycle boundaries, compact summaries are captured on the next … |
| [mempalace](../../agent-memory-systems/reviews/mempalace.md) | code-grounded | `online` `staged` — Stop hooks trigger every configured message interval, precompact hooks fire just before context compaction, and backfills/sweeps run as explicit staged maintenance. |
| [memwiki](../../agent-memory-systems/reviews/memwiki.md) | code-grounded | `online` `staged` — Online learning happens during ordinary work and at session end; staged learning happens when the user invokes `/memwiki-ingest`, `/memwiki-lint`, or `/memwiki-fold`. |
| [mentisdb](../../agent-memory-systems/reviews/mentisdb.md) | code-grounded | `online` `staged` — Agents can call extraction during a run, but extracted records are staged candidates until reviewed/signed/appended through the normal write path. |
| [meta-harness](../../agent-memory-systems/reviews/meta-harness.md) | code-grounded | `staged` `offline` - The loop stages candidate creation, validation, benchmarking, frontier update, and optional final evaluation. It is not an online per-turn learner inside a live user conversation, even when an evaluated … |
| [nao](../../agent-memory-systems/reviews/nao.md) | code-grounded | `online` — Extraction is scheduled immediately after the agent request is sent, runs asynchronously, and records both memory counts and a `memory_extraction` inference row. |
| [nuggets](../../agent-memory-systems/reviews/nuggets.md) | code-grounded | `online` `staged` — Tool-result capture, preference extraction, remembers, recalls, and hit-count updates happen during normal sessions; compaction summaries and `MEMORY.md` promotion happen at compaction boundaries. |
| [openviking](../../agent-memory-systems/reviews/openviking.md) | code-grounded | `online` `staged` — Hooks capture messages during normal agent use; commits archive immediately and run extraction asynchronously; archive ordering and done/failed markers create a staged pipeline. |
| [origin](../../agent-memory-systems/reviews/origin.md) | code-grounded | `online` `offline` `staged` — Capture and enrichment run during work, import is staged from exported archives, distill/refinery/background cycles run later, and `/handoff` closes a session with captures plus status files. |
| [phantom](../../agent-memory-systems/reviews/phantom.md) | code-grounded | `online` `staged` — Qdrant consolidation runs non-blocking after a session; self-evolution is staged through a persistent queue drained on cadence or demand depth. |
| [pi-self-learning](../../agent-memory-systems/reviews/pi-self-learning.md) | code-grounded | `online` `staged` — Task-end reflection runs online after `agent_end`; monthly summarization and global redistill are staged command-driven maintenance. |
| [pond](../../agent-memory-systems/reviews/pond.md) | code-grounded | `offline` `staged` — Sync runs manually, periodically, or at host lifecycle boundaries after clients have written source traces; index maintenance can run after row commits. |
| [reasoning-bank](../../agent-memory-systems/reviews/reasoning-bank.md) | code-grounded | `online` `staged` — The ordinary pipeline updates memory after each benchmark instance; the scaling path stages multiple trials before one induction pass. |
| [reflexion](../../agent-memory-systems/reviews/reflexion.md) | code-grounded | `staged` — Reflexion attempts, evaluates, reflects on failure, inserts the reflection, and retries. |
| [sage-wiki](../../agent-memory-systems/reviews/sage-wiki.md) | code-grounded | `online` `staged` — MCP capture and learn write during an agent session; compilation, verification, trust promotion, and scribe invocation are staged operations. |
| [sage](../../agent-memory-systems/reviews/sage.md) | code-grounded | `online` `staged` — `sage_turn`, `sage_remember`, SessionEnd, and reflection writes happen during agent operation; governance upgrades, content-validator activation, and some lifecycle/task effects are staged through operator or consensus … |
| [scroll](../../agent-memory-systems/reviews/scroll.md) | code-grounded | `online` `staged` — Turn capture, headline extraction, index updates, and continuation-summary updates occur online during the agent loop; startup import and retention maintenance are staged lifecycle work. |
| [signetai](../../agent-memory-systems/reviews/signetai.md) | code-grounded | `online` `staged` — Explicit remember/modify/forget and hook writes happen online around agent sessions; extraction jobs, document ingest, compaction artifacts, MEMORY.md projection, dream promotion, retention, and repair are staged … |
| [skillnote](../../agent-memory-systems/reviews/skillnote.md) | code-grounded | `online` `staged` — Hooks run during sessions and can write draft candidates or log use immediately; publishing a durable skill from those candidates is staged through skill-push/manual review. |
| [smriti-mcp](../../agent-memory-systems/reviews/smriti-mcp.md) | code-grounded | `online` `staged` — `remember` and `record_trace` write online during agent use; `suggest_consolidation` and `consolidate_memory` are staged review-and-promotion steps. |
| [spacebot](../../agent-memory-systems/reviews/spacebot.md) | code-grounded | `online` `staged` — Channels record conversations and working-memory events online; memory-persistence branches fire after message/time/event-density thresholds; cortex synthesis and maintenance run as background staged loops … |
| [supermemory](../../agent-memory-systems/reviews/supermemory.md) | code-grounded | `online` `staged` — Middleware retrieves before a call and can save conversation traces in the same request path or background task; browser/import/connector flows are staged ingestion; hosted processing queues documents through … |
| [synapptic](../../agent-memory-systems/reviews/synapptic.md) | code-grounded | `online` `staged` - The SessionEnd hook can enqueue background extraction after a Claude session closes, while the explicit CLI supports staged `extract`, `merge`, `synthesize`, `integrate`, and `benchmark` runs. |
| [synto](../../agent-memory-systems/reviews/synto.md) | code-grounded | `online` `staged` — Rejections, compile runs, cache/metrics, and MCP audit rows are written during normal use; their behavior-shaping effect is staged into the next compile, review, doctor/backlog, or maintenance pass. |
| [theafh--ai-modules](../../agent-memory-systems/reviews/theafh--ai-modules.md) | code-grounded | `staged` — The trace is mined at session close/wrapup time, diffed against existing wiki state, presented as a proposal, and only written after user approval. |
| [virtual-context](../../agent-memory-systems/reviews/virtual-context.md) | code-grounded | `online` `staged` — Inbound tagging/retrieval and request capture happen online before a model call; response tagging and compaction run after the turn; manual compaction, backfill, import, and dashboard replay are staged operations. |
| [voyager](../../agent-memory-systems/reviews/voyager.md) | code-grounded | `online` `staged` — During lifelong learning, skills, task lists, QA cache, chest memory, and events are written as the agent acts. Reusing a learned skill library for inference is a staged/offline transfer step. |
| [wuphf](../../agent-memory-systems/reviews/wuphf.md) | code-grounded | `online` `offline` `staged` — Artifact extraction runs asynchronously after artifact commits; `/lookup`, learning search, and notebook search happen during use; lint, archive, skill compile, promotion sweep, and boot reconcile are … |
| [xMemory](../../agent-memory-systems/reviews/xMemory.md) | code-grounded | `online` `staged` - Episode creation can happen online as messages are added or when a caller flushes the buffer; semantic generation is asynchronous after episode creation; theme and graph updates are staged through explicit facade calls … |

### Additional older lineage-only entries (9)

| Entry | Retained mechanism and boundary |
|---|---|
| [ReframeWeb](../../agent-memory-systems/reviews/ReframeWeb.md) | Runtime conversation history is retained; inline memory is authored. No automatic transcript distillation. |
| [cobusgreyling--llm-wiki](../../agent-memory-systems/reviews/cobusgreyling--llm-wiki.md) | The agent protocol records ingest/query/lint operations; no mined lesson loop. |
| [exo](../../agent-memory-systems/reviews/exo.md) | Continuous event/tool-result retention; rebuild outcomes and rollback-surviving history. See the earlier trigger map. |
| [exocomp](../../agent-memory-systems/reviews/exocomp.md) | Session, child-agent, debug, and work-report traces support continuity/audit; no automatic distilled guidance. |
| [openwiki](../../agent-memory-systems/reviews/openwiki.md) | Run metadata and optional checkpoints/tracing support update scope, continuity, and diagnostics. |
| [pal](../../agent-memory-systems/reviews/pal.md) | Agno-managed chat history and learned knowledge; the extraction algorithm is outside Pal-local code. |
| [synthadoc](../../agent-memory-systems/reviews/synthadoc.md) | Audit/query/job/chat/lifecycle records preserve operational interaction evidence. |
| [tracecraft](../../agent-memory-systems/reviews/tracecraft.md) | Explicit session mirror tails/redacts/uploads trace parts with cursor metadata; preservation without semantic mining. |
| [voiden](../../agent-memory-systems/reviews/voiden.md) | Enabled post-request hooks preserve request/response history, then prune by retention days; no learned-rule promotion. |

### Newer exact analyses (30)

| Entry and exact evidence | Trace-learning basis | Inspected trigger/route |
|---|---|---|
| [Apache Maka](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-06/result.md) | yes [wired] | RTE-12: explicit foreground/background extraction or compaction checkpoint; cited user evidence, localization/canonicalization, atomic item/cursor receipts. RTE-9/10 also cover continuation. |
| [AREX-Skill](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/result.md) | yes [afforded] | RTE-9/10: verification feedback and setup/probe results become refinement and environment handoff guidance; prescribed host-agent work. |
| [arsumbris](../../reports/retained/agentic-system-analysis/AAS-2026-09-23-arsumbris-02/result.md) | yes [afforded] | RTE-8: instructed capture of corrections during work, followed by later improve/derive review and adoption. |
| [ContextPilot](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/result.md) | yes [wired] | RTE-5/7/8: model-requested notes, context transformation, and partial-rollout continuation; task/training context rather than a general session-retention scheduler. |
| [DualGraph](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/result.md) | yes [wired] | RTE-4: evidence-batch graph extraction/merge for later report planning; default-route helper defects limit operational claims. |
| [EAL-bench](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-eal-bench-01/result.md) | yes [wired] | RTE-7: scheduled one-shot history or incremental conversation blocks update the accepted profile; old artifacts stay in the run collection. |
| [Ecdysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/result.md) | yes [wired] | RTE-1/2/9: training-round failure diagnosis and resumable review checkpoints; scalar failure summaries omit available raw trace contents from diagnosis prompts. |
| [Enoch](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-enoch-01/result.md) | yes [wired] | RTE-11: threshold/explicit/scheduled scans of unscanned turns and changed tasks → evidence signals → candidates → human admission. |
| [EvoOntology](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-evoontology-01/result.md) | yes [afforded] | RTE-3/4: recorded trajectories and trigger checkpoints produce reminders; user-invoked evolution diagnoses and tests a hypothesis. |
| [GBrain](../../reports/retained/agentic-system-analysis/AAS-2026-09-23-gbrain-01/result.md) | yes [wired] | RTE-6/24: Stop/PreCompact/SessionEnd source capture plus queued or sweep extraction; optional routes and failure backstops. |
| [LHTB](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-lhtb-01/result.md) | yes [wired] | RTE-7: verification outcome/timeout becomes continuation guidance for the next attempt; no independent cross-task lesson store implied. |
| [mem](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-instinctual-memory-01/result.md) | yes [wired] | RTE-1/2/5: session backfill, explicit consolidation, and detached SessionEnd sync with backlog threshold; filtered cursors can skip coverage. |
| [MerchantBench](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-merchantbench-01/result.md) | yes [afforded] | RTE-3/8: context pressure prompts a model to save continuation notes; trimming can proceed even if the write did not happen. |
| [Meta^n](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-meta-n-01/result.md) | yes [wired] | RTE-6/11/15: archive-selected parent evidence drives offspring proposals; context pressure and within-task repair also derive retained guidance. |
| [ModularRSI](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/result.md) | yes [wired] | RTE-1/2: completed-task batches trigger reflection, classified outcomes select investigations, and structured findings enter a proposal backlog. |
| [OpenViking](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-openviking-01/result.md) | yes [wired] | RTE-2/3/5: explicit/automatic commit archives and queues work; later extraction and continuation checkpoints consume retained messages. |
| [pi-posthorse](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-pi-posthorse-01/result.md) | yes [claimed] | RTE-2/7: turn-end usage checks and overflow/threshold recovery produce a host-persisted handoff; end-to-end continuity is claimed. |
| [PrimeScientist](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-primescientist-01/result.md) | yes [wired] | RTE-5/8: expansion of an evaluated search node triggers reflection over compact diagnostics and raw evidence pointers. |
| [Reflexion](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-reflexion-02/result.md) | yes [wired] | RTE-3/6: incorrect or halted attempts trigger reflection before retry; retained guidance is bounded to the question/attempt loop. |
| [RSIAgent](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-rsiagent-01/result.md) | yes [wired] | RTE-7/8: learning phases distill Actor history, reconcile the memory bank, audit benchmark boundaries, and publish; audit is not a truth test. |
| [SkillLift](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-skilllift-01/result.md) | yes [wired] | RTE-2/3: nonterminal rounds use prior plans/outcomes and verifier feedback to revise portfolio or rubric under admission checks. |
| [SoL-Pi](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/result.md) | yes [wired] | RTE-6/10: eligible diagnostic tool results produce bounded quote receipts; retained token-growth statistics drive later compaction scheduling. |
| [SwarmWorld](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/result.md) | yes [wired] | RTE-3/4: action feedback, sensing, inspection, and experiments create episode-local evidence for later plans. |
| [Tardigrade](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/result.md) | yes [wired] | RTE-3/4: context pressure selects a completed-exchange cut; summary checkpoints and output-validation feedback guide later calls. |
| [WikiSkill (Stahl-G)](../../reports/retained/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md) | yes [wired] | RTE-1/2/3/9: product execution phases lead to wiki learning and candidate evaluation; research compaction supplies optimizer context. |
| [AIDE2](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-aide2-01/result.md) | yes [claimed] | RTE-2/3/4: execution review derives scores/feedback; outer proposals consult prior agents/grades. Separately persisted compact summaries are not established. |
| [Prove2Me](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-prove2me-01/result.md) | yes [afforded] | RTE-9/10: instructed proof/failure explanations and upload checkpoints support later solver/uploader work; host/backend operation is outside inspection. |
| [WikiSkill](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md) | yes [claimed] | RTE-2/6: post-training maintenance samples failures and successes; candidate outcomes append after acceptance or rejection, surviving skill rollback. |
| [oh-my-pi](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-02/result.md) | yes [wired] | RTE-23/28/29: startup historical extraction, user-message decision deltas, and substantive-turn capture; RTE-21/22/31 add continuation and experiment feedback. |
| [prime-agent](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/result.md) | yes [wired] | RTE-8/9/10: compaction, branch summaries, and explicit or interval/compaction refinement; automatic reviewer decides whether to extract. |

The newer comparison explicitly marks fragility-grid and JEPA-Anything `no`,
and Supermemory `not-determinable`; these were checked and excluded from the
positive population. The older Supermemory review remains in its tagged
population. Different scope/revision and visibility of remote transformation
prevent silently carrying that older label into the newer analysis.
