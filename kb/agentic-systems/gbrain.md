---
description: "How GBrain works as a whole agentic system — host-agent adoption protocol, the dream-cycle scheduler, the Minions durable job queue with crash-resumable subagent loops, the operations trust boundary, and the SkillOpt self-modification loop — beyond the memory subsystem reviewed separately"
type: kb/types/note.md
traits: []
tags: [computational-model, tool-loop]
---

# GBrain as an agentic system

**Evidence basis:** first-hand reading of the `garrytan/gbrain` checkout at commit [9a0bae8d](https://github.com/garrytan/gbrain/commit/9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac) (2026-06-12), the same commit the memory-subsystem review pins.

GBrain presents as a memory layer, but the codebase is a second agentic system that installs itself *inside* a host agent: it ships an adoption protocol the host must follow on every message, runs its own LLM loops on a schedule, orchestrates crash-resumable subagents through a durable job queue, and rewrites its own instructions behind validation gates. The memory subsystem (pages, facts, search, embeddings) is reviewed in [the agent-memory review](../agent-memory-systems/reviews/gbrain.md); this analysis covers the rest.

## Host-agent adoption protocol

GBrain does not own the top-level loop — it colonizes one. `skills/_AGENT_README.md` is an operating contract the host agent reads on cold start: discover all bundled skills by parsing `triggers:` frontmatter from every `skills/<slug>/SKILL.md`, match every inbound user message against every trigger list, and on match read and follow the full skill body (a managed routing table in `RESOLVER.md` was retired in v0.36; routing lives in frontmatter). Two skills are always-on: `signal-detector` (capture candidate ideas/entities from every message, spawning non-blocking background jobs) and `brain-ops` (brain-first lookup before external sources, citation discipline). `INSTALL_FOR_AGENTS.md` and `AGENTS.md` are written *to the installing agent*, not the human — installation, trust boundary, and read order are agent-facing prose. Adoption is thus itself prose-executable system definition: the strongest behavior changes (per-message capture, brain-first routing) bind only if the host obeys the markdown.

## Execution loops it owns

Three distinct loop tiers, all host-independent once triggered:

- **Dream cycle** (`src/core/cycle.ts`, ~20 ordered phases in `ALL_PHASES`): lint → backlinks → sync → synthesize → extract → extract_facts → extract_atoms → symbol resolution → patterns → concept synthesis → emotional-weight recompute → consolidate → propose/grade takes → calibration → schema-suggest → skillopt → embed → orphans → purge. The orchestrator is plain TypeScript control flow; phases are a mix of deterministic maintenance and bounded LLM calls (Sonnet transcript synthesis, Haiku atom/take extraction, judge-model grading), coordinated under an advisory lock with per-phase scope annotations (per-source / global / mixed) added explicitly for future parallelization. Triggered by `gbrain dream` (one-shot) or the `autopilot` daemon (interval scheduling with quiet-hours policy).
- **Minions** (`src/core/minions/`): a Postgres-native BullMQ-style job queue — priorities, exponential backoff, stall detection, parent/child dependencies with failure policies, idempotency keys, per-job token accounting — whose flagship handler (`handlers/subagent.ts`) runs an Anthropic Messages tool-use loop with the conversation and every tool execution journaled to tables (`subagent_messages`, `subagent_tool_executions`), so a crashed subagent resumes by trusting completed rows and re-running only pending idempotent tools. Caps: `max_turns`, `allowed_tools` whitelist, `allowed_slug_prefixes` write bounds, rate leases around every LLM call. An aggregator handler waits on N children and synthesizes their results.
- **Think** (`src/core/think/`): a retrieve→synthesize pipeline (intent classification, hybrid gather, schema-validated synthesis call) with round-loop scaffolding for gap-driven follow-up retrieval — a bounded reasoning call, not a tool loop.

## Operations layer and trust boundary

`src/core/operations.ts` (~4,700 lines, ~100 operations) is the single contract from which both CLI and MCP surfaces are generated. Every operation declares a scope (`read`/`write`/`admin`), some `localOnly`; every call carries `OperationContext.remote`, fail-closed: remote (MCP/agent-facing) callers lose auto-linking on writes (anti prompt-injection), get strict upload path confinement, see only world-visible takes, and cannot invoke protected job types (`subagent`, `synthesize`, `consolidate`, …) or local-only operations (`run_skillopt`, `run_doctor`). Source scoping threads through every read. The notable stance: *the host agent that GBrain instructs so carefully is itself classified as untrusted at the API boundary* — prose-level trust (follow my skills) and code-level trust (remote = confined) are managed separately.

## Self-modification

SkillOpt (`src/core/skillopt/`) is an epoch-based optimization loop over skill markdown: batched rollouts, two-pass LLM reflection proposing edits, a cosine-decay "learning rate" bounding edit aggressiveness, a validation gate (median of three runs per task must beat the incumbent by ε), per-skill and brain-wide dollar caps, and a safety split — locally-authored skills mutate in place, bundled skills only ever get a `proposed.md` for human review. It is the highest-authority loop in the system (it rewrites instructions future agents follow) and the most heavily gated.

## Reading against the orchestration cluster

The dream cycle is a clean shipped instance of [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md): TypeScript control flow plays `select` over bounded LLM calls, with no framework graph layer. Minions reifies run-state exactly where [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) predicts: the journal (messages, tool executions, token rollups) lives in durable tables because crash-resume demands it, while the strategies (skills, phase order) live in markdown and code under version control. Against [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) the contrast is authorship and persistence: workflows have the model write a disposable orchestrator per run inside the harness; GBrain ships a fixed, versioned orchestrator outside any harness, durable by construction. And where the workflow sandbox withholds capability composition, GBrain's subagent handler grants it per job (`allowed_tools`, slug-prefix write bounds) — caller-constructed capability surfaces, the thing the workflows API reserves to a registry.

## Reading against Commonplace

Both are agent-operated markdown knowledge systems with types, links, skills, maintenance loops, and promotion paths — and both are *systems* in the same sense, since prose instructions execute on LLMs in each. The structural differences are placement, not kind:

- **Codification placement.** GBrain codifies the write path (extraction, consolidation, ranking as TypeScript with embedded LLM calls) and leaves consumption prose-instructed (skills advise the host agent). Commonplace inverts this: writing and navigation are prose-instructed (conventions, COLLECTION contracts), while checking is codified (validators, schemas, review ledger). Code writes / prose reads, versus prose writes / code checks.
- **Execution locus.** GBrain's deciding loops run in its own runtime — daemon, queue, scheduled cycle, LLM calls outside any host-agent context. Commonplace's deciding runs inside the harness agent's context window; its only owned runtime is a thin deterministic CLI. Decisions land as job rows and table state in one, as conversation turns and git diffs in the other.
- **Admission polarity.** GBrain default-ingests (signal detector on every message; writes fan out into derived structures) and services the resulting curation debt with the dream cycle. Commonplace default-excludes (quality bar, typed write path, review gates) and carries capture debt instead — observations never recorded because no capture surface exists.
- **Revision semantics.** GBrain manages belief change numerically and temporally — confidence scores, validity windows, supersession fields, decay — executed by code. Commonplace revises dialectically — contestable claims, contradicts/refines edges, review gates — executed by agents under review.
- **Oracle.** GBrain's learning loops settle against machine oracles (retrieval benchmarks, judge models, SkillOpt's median-score gate; the bundled-skill `proposed.md` carve-out is its one human checkpoint). Commonplace's loops settle against human acceptance (the acceptance ledger; gate-learning keeps promotion human-gated by design).

---

Relevant Notes:

- [GBrain (agent-memory review)](../agent-memory-systems/reviews/gbrain.md) — contains: the memory, retrieval, and trace-derived-learning subsystem this analysis deliberately excludes
- [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md) — rationale: the dream cycle and Minions instantiate host-language `select` with run-state reified only where durability forces it
- [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — rationale: Minions journals K in Postgres while strategies stay versioned markdown/code
- [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) — see-also: the inverse authorship/persistence answer — model-authored disposable orchestrators inside the harness versus a shipped durable orchestrator outside it
