---
description: "Coding-agent procedural memory CLI that mines cass session history into diary JSON, scored YAML playbook rules, outcomes, trauma guards, and MCP/CLI context surfaces"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# cass_memory_system

cass-memory is Jeffrey Emanuel's Bun/TypeScript procedural-memory system for AI coding agents. It wraps the separate `cass` session-search engine with a three-layer loop: raw coding-agent sessions are searched as episodic evidence, converted into structured diary entries, reflected into YAML playbook bullets, then served back to future agents through `cm context`, CLI management commands, and an HTTP JSON-RPC MCP-style server. The system is less a general knowledge base than a rule-mining and rule-governance layer for coding-agent behavior.

**Repository:** https://github.com/Dicklesworthstone/cass_memory_system

**Reviewed revision:** [467209e1058f758e0d10393adb2cf29f65ff62bc](https://github.com/Dicklesworthstone/cass_memory_system/commit/467209e1058f758e0d10393adb2cf29f65ff62bc)

## Core Ideas

**The retained state is split across evidence, summaries, rules, logs, caches, and served views.** The README describes episodic `cass` history, diary entries, and procedural playbook bullets as separate layers ([`README.md`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/README.md)). The implementation keeps that split. Raw sessions remain in `cass` and are accessed through subprocess calls, not copied into the playbook store ([`src/cass.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/cass.ts)). Diary entries are JSON records with session path, agent, status, accomplishments, decisions, challenges, preferences, key learnings, related sessions, tags, and search anchors ([`src/types.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/types.ts), [`src/diary.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/diary.ts)). Playbook bullets live as YAML with source sessions, source agents, feedback events, maturity, deprecation, confidence decay, and optional embeddings ([`src/types.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/types.ts), [`src/playbook.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/playbook.ts)). Outcome logs, context logs, trauma logs, blocked logs, onboarding state, and embedding caches are separate sidecar artifacts rather than fields on one memory object ([`src/outcome.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/outcome.ts), [`src/trauma.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/trauma.ts), [`src/semantic.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/semantic.ts)).

**Playbook bullets are system-definition artifacts when activated.** A bullet is not just a note. `cm context` loads the merged global and repo playbooks, filters active bullets, scores them against a task, separates rules from anti-patterns, appends history snippets, and returns the result as machine-readable JSON/TOON/markdown context ([`src/commands/context.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/context.ts)). The same bullet can be inspected as a knowledge artifact through `cm playbook get` or `cm why`, but in `cm context` it has instruction/advice authority over the next coding-agent action. Exporters can also compile playbooks into `AGENTS.md` or Claude-oriented project rules, moving the same prose bullets closer to always-loaded instructions ([`src/playbook.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/playbook.ts)).

**The learning loop combines LLM proposal with deterministic curation.** `orchestrateReflection` discovers unprocessed sessions, generates a diary, exports session text, asks the reflector to propose deltas, validates deltas, parses inline feedback comments, extracts rule IDs for auto-outcome signals, and only then locks and mutates the global/repo playbook ([`src/orchestrator.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/orchestrator.ts)). The reflector's output schema is a strict union of add/helpful/harmful/replace/deprecate/merge deltas, not free-form markdown ([`src/reflect.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/reflect.ts)). The curator then handles exact and token-similarity deduplication, conflict warnings, feedback application, anti-pattern inversion, promotion, demotion, merge decomposition, and deprecation without an LLM in the mutation step ([`src/curate.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/curate.ts)).

**Confidence is an operational signal, not just metadata.** Feedback events decay by half-life; harmful events count through a configurable multiplier; maturity transitions use decayed helpful/harmful counts; negative scores can demote or auto-deprecate rules ([`src/scoring.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/scoring.ts)). `cm outcome` records task outcomes and `outcome-apply` maps success, failure, duration, retry, error, and sentiment signals back onto rules used in the session ([`src/outcome.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/outcome.ts)). This makes the playbook a scored system-definition surface: future activation is ranked by both topical relevance and learned usefulness, not merely by recency or textual match.

**Retrieval mixes keyword search, optional embeddings, and cass history.** The default context path extracts task keywords, scores bullet text/tags by keyword relevance, optionally blends embedding similarity, multiplies by effective score, and separately queries `cass` for historical snippets ([`src/commands/context.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/context.ts)). Embeddings are cached in `~/.cass-memory/embeddings/bullets.json` keyed by bullet ID plus content hash, using either Xenova transformers or Ollama ([`src/semantic.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/semantic.ts)). `cass` failures degrade to playbook-only mode with structured warnings instead of aborting the whole context call ([`src/cass.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/cass.ts)).

**Onboarding is deliberately agent-native.** The `onboard` command does not just say "run reflection." It samples sessions, tracks processed sessions, analyzes category gaps, scores candidate sessions against underrepresented categories, reads a selected session with extraction instructions, and lets the current coding agent add rules manually or in batches ([`src/commands/onboard.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/onboard.ts), [`src/gap-analysis.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/gap-analysis.ts)). This is a useful adoption pattern: bootstrap the memory by making the already-paid agent perform curation work, then mark source sessions done.

**Safety memory is separated as trauma, not folded into ordinary rules.** Trauma entries are JSONL records containing regex patterns, severity, scope, trigger session, and status ([`src/types.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/types.ts)). `scanForTraumas` looks for apology/disaster language and dangerous command patterns in cass sessions, while `cm context` checks active trauma patterns before producing ordinary context and emits a visible warning when a task matches ([`src/trauma.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/trauma.ts), [`src/commands/context.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/context.ts)). That gives catastrophic prior failures stronger behavioral authority than low-scored playbook advice.

**The MCP surface exposes both knowledge resources and mutation tools.** `cm serve` implements HTTP JSON-RPC endpoints for `cm_context`, `cm_feedback`, `cm_outcome`, `memory_search`, and `memory_reflect`, plus resources for the merged playbook, diary entries, outcomes, and stats ([`src/commands/serve.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/serve.ts)). Resources are knowledge artifacts for inspection. Tools carry system-definition authority because they can activate context, record feedback, apply outcomes, and trigger reflection. The server defaults to loopback and requires auth when binding non-loopback, which matters because these surfaces expose sensitive session-derived memory.

## Comparison with Our System

| Dimension | cass-memory | Commonplace |
|---|---|---|
| Primary purpose | Procedural memory for coding agents across session histories | Agent-operated KB methodology and durable knowledge artifacts |
| Raw evidence | External `cass` session index, local/remote session exports | Source snapshots, notes, reviews, workshop artifacts, git history |
| Main distilled artifact | YAML playbook bullet with confidence, feedback, maturity, source sessions | Typed markdown notes, instructions, references, indexes, review notes |
| Working-memory layer | Diary JSON derived from a session | Workshop documents and draft notes |
| Activation | `cm context`, exported agent files, MCP tools/resources | AGENTS instructions, skills, indexes, authored links, validation/review commands |
| Scoring | Decayed helpful/harmful feedback, maturity multipliers, optional embeddings | Mostly semantic review and validation state; no general confidence score for notes |
| Governance | Deterministic curator, validation checks, conflict heuristics, trauma guard, blocked logs | Type specs, collection conventions, validation, semantic review bundles, git review |
| Trace-derived learning | Central mechanism: sessions to diary to playbook deltas and outcomes | Emerging methodology; not the default production loop |

cass-memory is stronger on the operational feedback loop. It has a concrete path from task context to rule use, from session outcome back to rule confidence, and from repeated harmful feedback to anti-pattern or deprecation. Commonplace has richer artifact contracts and more durable prose/lifecycle discipline, but it does not yet have a comparable feedback-weighted activation loop for instructions.

Commonplace is stronger on explicit artifact semantics. cass-memory stores source sessions and reasoning, but playbook bullets remain compact instruction strings with metadata. They do not carry the full source snapshot, review state, typed outbound links, or section-level argument structure that commonplace notes do. This is an intentional trade: cass-memory optimizes for fast pre-task behavior shaping; commonplace optimizes for durable inspectable methodology.

The systems also disagree about where structure belongs. cass-memory centralizes structure in code and schemas: Zod schemas, YAML playbooks, JSONL logs, scoring functions, command outputs, and MCP endpoints. Commonplace centralizes more structure in the markdown artifact contract and validates that prose layer. The borrowable point is not "replace notes with scores"; it is "behavior-changing instructions need an activation/evaluation loop once they start steering agents."

## Borrowable Ideas

**Use feedback-weighted activation for instruction-like artifacts.** Ready to borrow as a design target, not as a full implementation. Commonplace instructions and skills could eventually gain lightweight use/outcome events, especially for high-risk operational procedures. The cass-memory distinction between topical relevance and effective score is the useful part.

**Separate raw traces, working summaries, and procedural bullets.** Ready to borrow. cass-memory's raw session, diary, playbook, outcome, trauma, and embedding-cache split is cleaner than treating all trace-derived material as "memory." A commonplace trace-mining workflow should preserve that split: source evidence, summary artifact, candidate instruction, scored outcome, and served view are different retained artifacts with different behavioral authority.

**Make anti-patterns first-class.** Ready to borrow for operational guidance. cass-memory's inversion path is crude but valuable: harmful advice should not just disappear if it encodes a failure mode future agents need to avoid. In commonplace, this would look like promoted warnings or "avoid" instructions with source-linked review, not automatic prose inversion alone.

**Expose provenance with a dedicated "why" path.** Ready to borrow. `cm why` turns a bullet ID into reasoning, source sessions, related diary entries, and feedback history ([`src/commands/why.ts`](https://github.com/Dicklesworthstone/cass_memory_system/blob/467209e1058f758e0d10393adb2cf29f65ff62bc/src/commands/why.ts)). Commonplace has source links and git history, but a command that answers "why does this instruction exist?" for an operational rule would make authority easier to audit.

**Treat catastrophic failures as a separate safety channel.** Worth borrowing only for clearly dangerous operations. Trauma entries have higher activation force than normal playbook advice and are checked before context output. Commonplace already encodes destructive-command constraints in agent instructions; a retained, source-linked "hot stove" log could make those constraints more adaptive.

**Do not borrow confidence scores as a universal note metric.** cass-memory's score is appropriate for short procedural bullets repeatedly used in tasks. It would be misleading on theoretical notes, ADRs, source reviews, or definitions where quality is not a count of recent helpful marks. If borrowed, the score should attach to activated operational advice, not to every KB artifact.

## Trace-derived learning placement

**Trace source.** cass-memory qualifies as trace-derived learning. The source traces are coding-agent session logs indexed and exported through `cass`, including local and optional SSH-queried remote histories. The reflector also consumes generated diary entries, inline feedback comments in transcripts, and task outcome records as downstream trace signals.

**Extraction.** Extraction has several stages. `generateDiary` exports and sanitizes a session, then either heuristically creates a diary or asks an LLM to extract status, accomplishments, decisions, challenges, preferences, key learnings, tags, and anchors. `reflectOnSession` asks an LLM for structured playbook deltas from the diary plus related history. `validateDelta` and the deterministic curator filter, deduplicate, merge, reinforce, deprecate, or invert those deltas. Onboarding is a manual/agent-native alternate extraction path: sample sessions, read one with a prompt, and add rules through `cm playbook add`.

**Storage substrate.** Raw source traces remain outside cass-memory in the `cass` index and session files. Diary entries are JSON files under the configured diary directory. Playbook bullets are YAML in a global playbook and optional repo-local `.cass/playbook.yaml`. Outcomes and context use JSONL logs. Trauma entries use JSONL in global or project `.cass` storage. Embeddings are a JSON cache under the global cass-memory directory. MCP resources and context responses are generated views over those stores, not sources of truth.

**Representational form.** Raw traces are mixed: conversation prose, tool/action text, file paths, commands, metadata, and cass search scores. Diary entries are structured JSON with prose fields. Playbook bullets are mixed prose-symbolic artifacts: the operative instruction is prose, while IDs, scope, category, maturity, counters, feedback events, and deprecation fields are symbolic. Embeddings are distributed-parametric cache entries used for ranking, not the canonical memory. Trauma patterns are symbolic regex rules with prose descriptions.

**Lineage.** Playbook bullets preserve source sessions and source agents, and the `why` command can reconnect bullets to diaries and feedback history. This is stronger lineage than a plain prompt summary. It is still weaker than commonplace source snapshots: the bullet does not embed exact quotes, extractor prompt version, validation evidence set, model version, or block-level derivation proof. Regeneration is procedural through reflection or onboarding; invalidation is mostly feedback/deprecation-driven rather than source-change-driven.

**Behavioral authority.** Raw cass hits and diary entries are knowledge artifacts when inspected as evidence or context. Playbook bullets become system-definition artifacts when activated by `cm context`, exported into agent instruction files, or served through MCP tools. Outcome records are learning-input artifacts: they mutate future ranking and maturity. Trauma entries are system-definition artifacts with safety-intervention force. Embedding caches are ranking-influence artifacts, derived from playbook bullets and subordinate to the YAML source of truth.

**Scope.** The system is cross-agent and cross-project by default at the global playbook layer, with repo-local playbooks and project-scoped trauma entries as narrower overlays. Some bullets can carry workspace scope, but the principal learning target is reusable coding-agent procedure, not one benchmark task.

**Timing.** Learning is staged. `cm context` is pre-task activation. `cm reflect` is post-session or scheduled offline distillation. `cm outcome` and inline comments provide post-task feedback. `cm onboard` bootstraps from historical traces in batches. There is no within-action online model update; the active policy changes when the playbook or logs are mutated between calls.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), cass-memory belongs in the readable-artifact learning family but with a stronger operational-feedback loop than simple reflection stores. It strengthens the survey claim that trace-derived learning often splits into raw trace stores and distilled behavior-shaping artifacts. It also splits the "procedural memory" bucket: cass-memory has ordinary advice bullets, negative anti-pattern bullets, and trauma guards with different behavioral authority rather than one homogeneous memory list.

## Curiosity Pass

**The strongest design is the artifact split, not the cognitive metaphor.** The README's episodic/working/procedural framing is useful, but the implementation earns its value by keeping session logs, diaries, playbook rules, outcomes, trauma entries, embedding caches, and served resources separate. That split lets each artifact have a different review method and authority.

**The "scientific validation" language is stronger than the code-grounded guarantee.** The code has validation and evidence-gathering machinery, plus deterministic curation and scoring. But a playbook bullet can still be added manually or by reflection as a candidate, and the reviewed files do not show a universal requirement that every new rule is accepted only after a rigorous historical evidence gate. The safer reading is "evidence-aware rule governance," not scientific validation in the experimental sense.

**Confidence decay is useful and dangerous.** For repeated operational rules, feedback-weighted decay is exactly the missing lifecycle signal. For rare safety rules or project conventions, low recent feedback may not mean low validity. cass-memory handles some of this with pinning and trauma separation, but operators still need to decide which rules should be scored by use frequency and which should be stable policy.

**The embedding cache is clearly derived state.** It improves ranking and can be regenerated from playbook content. It should not be treated as an independent memory surface, and the code mostly respects that by keying it to bullet IDs and content hashes.

**The MCP server is powerful enough to need governance.** Serving resources is read-only context. Serving `memory_reflect`, `cm_feedback`, and `cm_outcome` lets callers mutate the learning loop. The loopback default and auth check are important, but any downstream integration should treat these tools as write-authority, not just retrieval.

## What to Watch

- Whether future versions make rule validation evidence explicit inside the bullet, including source quotes, query used, model/prompt version, and accepted/rejected evidence counts.
- Whether trauma guards remain separate from anti-pattern bullets or converge into one richer safety-rule model.
- Whether the MCP surface grows stdio/SSE support or remains intentionally HTTP-only.
- Whether confidence scoring gains per-category policies so rare but mandatory rules do not decay like ordinary workflow tips.
- Whether onboarding and reflection converge into one extraction pipeline with shared provenance and review state.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: cass-memory distills coding-agent traces into diary entries, procedural bullets, feedback signals, and safety guards
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - exemplifies: the important question is which future action changes when a retained artifact is activated
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - supports: cass-memory mines sessions for reusable procedural rules and then evaluates them through later outcomes
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: `cm context` loads behavior-changing bullets before task execution
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: playbook bullets, trauma guards, outcome feedback, and MCP mutation tools differ by behavioral authority
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: raw cass hits and diary entries are evidence/context before they are promoted into action-shaping rules
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: cass-memory's diary and onboarding surfaces are work-in-progress bridges from trace evidence toward durable procedural guidance
