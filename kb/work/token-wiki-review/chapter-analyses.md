# Token Wiki — per-chapter analyses

Compact ingest-style notes on each of the ten chapters of `related-systems/token-wiki/`.
Source: practitioner synthesis by the Token Wiki authors based on four production systems
(Claude Code, Cline, Codex, OpenCode). Each chapter describes convergent mechanisms and
reports concrete defaults.

Each entry below lists: central claim → key mechanisms → data points → the KB note(s)
the chapter lands against.

---

## 01 — Context Compaction

**Central claim.** Compaction is the single most important token technique. "Fail or compress"
is the only binary; every production system compacts, but cost-wise interventions live on
a spectrum from free (prune stale tool results) to expensive (LLM summarization).

**Mechanisms.**
- Tool-result pruning (zero-cost): walk backward, replace old results with marker, keep last 5
  or last 40k tokens of results.
- Microcompaction: cache-aware (`cache_edits` server-side deletion) vs. time-based (cold-cache
  direct mutation).
- Sliding-window truncation (Cline): keep strategies none/lastTwo/half/quarter, first pair
  always preserved.
- LLM summarization with structured templates (Goal/Instructions/Discoveries/Accomplished/Files).
- Post-compaction restoration: Claude Code restores 50k of recently-read files + 25k of active
  skills; system instructions are *never* summarized, always re-injected.
- Circuit breaker: Claude Code caps consecutive auto-compact failures at 3 after discovering
  1,279 sessions with 50+ failures wasting ~250k API calls/day.

**Data points.**
- Trigger thresholds: 75% (Cline), 85% warn / 93% auto (Claude Code), 90% (Codex), 95% (OpenCode).
- Compaction decision tree layers cheap-before-expensive.

**KB alignment.**
- Maintenance component of [context engineering](../../notes/definitions/context-engineering.md).
- "Never summarize instructions" = always-loaded content belongs to a stable layer that should
  not drift; [always-loaded context mechanisms](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md),
  [AGENTS.md as control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md).
- The circuit breaker is a hard oracle on a tool loop — connects to our theme of oracle-gated
  iteration in workshop systems.
- Tension with [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md):
  compaction exists because history *is* being loaded into the next call; it is the remediation
  for a problem our theory says to avoid upstream.

---

## 02 — Token Counting & Estimation

**Central claim.** Cheap heuristic estimation (`length / 4`) is good enough for threshold decisions;
combine it with API-reported actuals for precision when needed. Don't ship a tokenizer.

**Mechanisms.**
- Two-tier: API actuals (exact, post-response) + heuristic estimate for delta since last call.
- Content-type adjustments: JSON tokenizes at ~2 bytes/token (denser); images flat 2k; code ~4.
- Safety padding: Claude Code multiplies estimates by 4/3 for compaction decisions to avoid
  false negatives.
- Effective window formula: `context_window − min(maxOutput, 20_000) − overhead`.
- Output token budget: 99th-percentile actual response is ~5k tokens though models advertise
  128k, so reserving the full output limit wastes ~123k of usable context. Solution: cap at 8k,
  retry with 64k on overflow.

**Data points.**
- All four systems converge on `length / 4`. The universal constant.
- 150k conversation: $0.45 no-cache → $0.06 with cache (~87% savings).
- Claude Code falls back to Haiku for exact counts when heuristics aren't enough.

**KB alignment.**
- The heuristic/actual split instantiates the [symbolic scheduling over bounded LLM calls](../../notes/bounded-context-orchestration-model.md)
  separation: exact bookkeeping in code (cheap, deterministic), expensive judgment reserved for
  the bounded call.
- Output budget cap is a concrete instance of [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md)
  inverted: committing less output budget *frees* input budget. Same principle — static knowledge
  (empirical response distribution) moves cost out of the bounded call.

---

## 03 — Prompt Caching

**Central claim.** A cache hit is 10x cheaper than fresh input. Cache fragility is the dominant
constraint on architecture — any prefix mutation invalidates everything after it. Design prompts
stable-first to maximize the cacheable prefix.

**Mechanisms.**
- 2–3 breakpoint strategy: system prompt block, dynamic context block, last message.
- Single-marker rule on conversation: multiple cache_control markers on messages waste KV memory
  because intermediate positions prevent reclamation.
- Two-phase break detection: pre-call hash of system prompt + per-tool schema + model; post-call
  compare `cache_read_input_tokens` between turns, flag >5% drop and >2k absolute decrease.
- Per-tool schema hashing isolates the *specific* tool whose schema changed (77% of breaks are
  MCP tool schema changes).
- Cache-aware microcompaction uses `cache_edits` server-side delete instead of rewriting history.
- TTL latched at session start to prevent mid-session invalidation from rate-limit flipping.

**Data points.**
- Fresh input $3.00/Mtok, cache write $3.75/Mtok (+25%), cache read $0.30/Mtok (−90%).
- 77% of cache breaks are MCP tool schema changes.
- Healthy sessions maintain 80–95% cache hit ratio after a few turns.

**KB alignment.**
- **Gap in KB theory.** We have no note on prompt caching as an architectural constraint. The
  KB treats context as the scarce resource; token-wiki surfaces a *second* scarce resource,
  the **cache prefix**, whose fragility constrains what mechanisms are legal. Compaction that
  rewrites history and caching are in direct tension. This is a candidate for a new note.
- Stable-first ordering mechanically reinforces [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md):
  the content that loads every turn goes first (longest cache hit).
- Per-tool schema hashing is a diagnostic response to [LLM context is a homoiconic medium](../../notes/llm-context-is-a-homoiconic-medium.md) —
  because everything is concatenated text, you can't tell which contribution broke the cache
  without hashing each component separately.

---

## 04 — System Prompt Optimization

**Central claim.** The system prompt is present on every call, so its cost multiplies by every
turn. Assemble it from stable-to-volatile layers, use model variants for different capabilities,
and defer detail to on-demand surfaces.

**Mechanisms.**
- Layered assembly: provider template → tool schemas → agent instructions → skills → environment
  → user instructions (CLAUDE.md) → conditionals.
- Variant-based prompts (Cline): XS 2-3k/9 tools, Generic 5-6k/18, Next-Gen 5.5-6.5k/20. XS is
  ~50% smaller than Generic.
- Component filtering: conditionally include MCP docs, timeout parameters, structured-output
  instructions.
- Hard caps on user instructions: Codex caps AGENTS.md at 32 KiB (~8k tokens). OpenCode uses
  hierarchical discovery with shared byte budget, root-to-leaf, skip on exhaustion.
- Instructions always injected fresh after compaction; Codex uses `reference_context_item` to
  force full re-injection.
- Tool schema deferral (Codex): ship only `tool_search` meta-tool, model discovers tools on
  demand. Saves ~10k tokens per turn with 50 MCP tools.
- Template post-processing strips empty sections.

**Data points.**
- 6k system prompt × 50 turns = 300k tokens = $0.90 in repetition alone.
- XS variant vs. Generic: ~50% reduction.

**KB alignment.**
- Strong convergence with [always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)
  and [AGENTS.md should be organized as a control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md).
- Hierarchical discovery with shared byte budget maps to [directory-scoped types are cheaper than global types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md).
- Tool schema deferral is a striking instance of [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md)
  extended to *tool* surfaces — most systems treat the tool list as always-loaded. Codex
  demonstrates that tool descriptions can be on-demand routed by a meta-tool. This strengthens
  the note: the routing hierarchy applies to tools too.
- Capping AGENTS.md at 32 KiB (Codex) is a hard constraint our KB lacks. Commonplace's CLAUDE.md
  is a symlink to AGENTS.md and is not size-capped. Worth noting as a production signal that
  unbounded always-loaded files are a risk, not just a theoretical concern.

---

## 05 — Tool Output Management

**Central claim.** Tool outputs are the single largest token source in agentic systems. Apply
multiple truncation layers in sequence. Prefer pagination over truncation; save full output to
disk; strip media early.

**Mechanisms.**
- Four layers: tool-specific limit → raw byte buffer (1 MiB head/tail) → token budget (10k/result)
  → serialization overhead padding (1.2x).
- Head/tail preservation: beginning has errors and headers, end has final results, middle is
  often repetitive.
- Per-tool limits: Read 2000 lines/50 KB, Grep 100 matches, Glob 100 files, Web 8 results,
  directory listing 25 entries.
- Pagination: return "more results available" hint instead of truncating silently.
- Persistent storage (OpenCode): write full output to `tool-output/{id}.json` with 7-day TTL,
  give model a reference.
- Media stripping before summarization (~1-5k tokens each).
- Duplicate detection: track `Map<filePath, readCount>`, waste = avg × (count−1).
- Sort-before-truncate: glob sorted by mtime so the most relevant survive.

**Data points.**
- Tool results are ~45% of context in agentic sessions (cited on README).
- A single file read is 5-10k tokens.

**KB alignment.**
- The four-layer defense mechanically instantiates the maintenance component of
  [context engineering](../../notes/definitions/context-engineering.md).
- Persistent storage with reference handle = externalization pattern: the scheduler's symbolic
  state stores the full output while the bounded call sees a pointer. Maps cleanly to the
  [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) —
  `K` stores everything; `select(K)` injects a summary plus a recall handle.
- Duplicate read detection is empirical evidence for the "amnesia" problem that
  [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
  argues against upstream: the model re-reads files because its effective working set *is* the
  flat chat history, which doesn't stably retain what was already read.
- Pagination > truncation is the same pattern as [agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md):
  give the agent a decision surface, don't collapse upstream.

---

## 06 — Message Architecture

**Central claim.** The message array is the central data structure. Normalization, tool pairing,
and post-processing order are load-bearing. Separate API history (strict) from UI history (rich).

**Mechanisms.**
- Dual history: API-history strict (alternating roles, paired tools, truncated); UI-history rich
  (cost/timing/metadata, never truncated).
- Non-destructive truncation: apply a `deletedRange` at call time rather than mutating the array.
  Enables checkpoint restoration and undo.
- Tool result pairing invariants: inject synthetic `[Tool result missing]` for orphaned
  `tool_use`; remove orphaned `tool_result`; dedupe duplicate IDs.
- Typed message parts (OpenCode): TextPart / ToolPart / ReasoningPart / FilePart / CompactionPart
  with explicit state machines (pending/running/completed/error).
- O(1) lookup maps for long conversations (tool_use_id → block).
- Post-processing order matters; stripping trailing thinking must happen before non-empty
  validation.

**Data points.**
- 10 enumerated API invariants (first msg user, roles alternate, tool pairs, etc.).

**KB alignment.**
- "Dual history" formalizes the split our theory hints at but doesn't name: the substrate state
  (UI history, rich trace) vs. the bounded-call input (API history, minimal). This is
  [execution-boundary compression](../../notes/session-history-should-not-be-the-default-next-context.md)
  materialized as a data structure. Token-wiki's framing is that they maintain both because the
  API and UI have different requirements; our framing would say the bounded call should always
  receive a compressed/selected view of a richer substrate. Same structure, different motivation.
- Non-destructive truncation is a clean implementation detail for the [bounded-context orchestration](../../notes/bounded-context-orchestration-model.md)
  invariant that `K` is monotone: `K += r` rather than `K = select(K)`. Deletion as metadata
  means the selector can be re-run or rolled back.
- Typed parts with state machines are an expression of [instructions are typed callables](../../notes/instructions-are-typed-callables.md)
  applied to message fragments — type discipline at the data-structure level.

---

## 07 — Context Window Management

**Central claim.** Context is a hard ceiling. Compute the effective window (not advertised),
define multiple threshold levels for graceful degradation, and cap output reservations based on
*actual* rather than advertised usage.

**Mechanisms.**
- Effective window = advertised − output reservation − safety buffer.
- Graceful degradation ladder: 75% warn → 85-90% microcompact → 90-93% summarize → 95-99.7%
  block → 100% API error.
- Claude Code's output-cap insight: advertised 128k → cap reservation at 8k → retry with 64k if
  hit → recovers ~56k usable context in the common case.
- Cline's fixed reserves scale proportionally: 64k window reserves 27k (42% overhead); 1M
  window reserves 40k (4% overhead). Small windows have higher fixed-cost overhead.
- Codex's model-switch compaction: when downshifting to smaller window, run compaction with the
  *previous* (larger) model.
- Configurability knobs: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`, `CLAUDE_CODE_AUTO_COMPACT_WINDOW`,
  `DISABLE_AUTO_COMPACT`, `CLAUDE_CODE_DISABLE_1M_CONTEXT`.

**Data points.**
- 99.99% of compact summaries ≤ 17,387 tokens (empirical).
- Context window resolution has a priority chain: env var → `[1m]` suffix → SDK cache → beta
  header → experiment → registry → default 200k.

**KB alignment.**
- Empirically operationalizes [agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md):
  the "effective window" calculation is exactly the hard/effective distinction that note makes
  theoretical. Token-wiki shows practitioners universally compute the effective window as a
  different number from the advertised one — but their deltas are from *output reservations and
  safety buffers*, not from task-dependent soft-degradation. Practitioners approximate the soft
  bound using fixed buffers; our theory argues the bound is task-dependent. These are
  complementary: practitioners need a number, theory explains why it's wrong by a task-dependent
  margin.
- The graceful-degradation ladder is a [soft-bound traditions](../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md)-adjacent
  pattern: provide multiple responses at escalating severity so the system never hits the hard
  limit.
- Model-switch compaction is a small but interesting detail — the scheduler knows when the
  context requirement exceeds the next call's capacity and runs the compression pass with the
  previous model's capabilities. This is a concrete symbolic-scheduling move.

---

## 08 — Multi-Agent Context

**Central claim.** Subagents create a distributed token-management problem. Isolate their
context from the parent: fork with aggressive filtering, restrict tool sets, track nesting
depth, roll up costs to the parent.

**Mechanisms.**
- Fork-based seeding (Codex): keep system/user/final-answer messages; drop tool results,
  reasoning, intermediate messages. Produces a 10k-token seed from a 100k parent (~90%
  reduction).
- Coordinator pattern (Claude Code): workers get their own full context, restricted tool set
  (ASYNC_AGENT_ALLOWED_TOOLS), own compaction lifecycle; coordinator sees only the final
  XML notification.
- Guardian subagent budgets (Codex): separate 10k pools for message transcript and tool
  transcript so they can't crowd each other out.
- Ghost snapshots (Codex): background git commit of working tree, recorded in history as a
  GhostSnapshot item, filtered out before API calls — zero-token undo capability.
- Subagent usage rollup: track input/output tokens per agent, aggregate for cost attribution.
- Nesting limits: Codex caps at 1 level / 6 concurrent threads.

**Data points.**
- With isolation, parent sees ~2k per subagent instead of 140k.

**KB alignment.**
- This chapter is the most direct mechanical validation of [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md):
  "fork with filtering, drop tool results and reasoning, keep only instructions and decisions"
  is almost a direct transcription of lexically-scoped frames. The Codex guardian subagent
  budget (separate message vs. tool transcripts) is a concrete instance of a frame that declares
  what bindings it inherits.
- Ghost snapshots (zero-token state capture via git) are a beautiful instance of
  [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md)
  applied to runtime: the execution substrate holds state outside the bounded call, providing
  undo for free.
- The sub-agent filtering rule ("drop tool results, keep decisions") is [execution-boundary
  compression](../../notes/session-history-should-not-be-the-default-next-context.md) specialized
  to the parent→child direction. Our theory discusses it mostly child→parent; token-wiki shows
  the parent→child version is where the bigger savings live.

---

## 09 — Diagnostics & Observability

**Central claim.** You can't optimize what you can't see. Attribute tokens by source, detect
waste (especially duplicate reads), track cache hit ratio, instrument from day one.

**Mechanisms.**
- Token breakdown by source: tool results / tool requests / assistant / human / system / etc.
- Per-tool attribution: which tools consume most tokens; which tools are read most often.
- Duplicate detection: track `Map<filePath, readCount>`, waste = avg × (count−1).
- Three-tier counting: API actuals (exact, billing), Haiku fallback (near-exact, edge cases),
  heuristic (±30%, thresholds and UI).
- Cache hit ratio as health metric: >80% healthy, 50-80% degraded, <50% poor.
- Query-source tracking: tag each API call with its originator (`agent:builtin:read`, `compact`,
  `agent:custom`, etc.).
- Ablation testing: `CLAUDE_CODE_ABLATION_BASELINE=1` strips all optimizations for measurement.
- Display-aware truncation: middle-ellipsis paths, grapheme-safe for emoji/CJK.

**Data points.**
- Example breakdown: tool results 45%, tool requests 12%, assistant 18%, human 8%, system 7%.
- Healthy cache hit ratio 80-95% after first few turns.

**KB alignment.**
- Observability is underdeveloped in our theory. [Context engineering](../../notes/definitions/context-engineering.md)
  lists routing/loading/scoping/maintenance as components but has no dedicated observability
  component. Token-wiki makes the argument that *attribution* (where tokens go) is a prerequisite
  for the other four being tunable.
- The 45% figure for tool results is citable empirical support for several notes — confirms the
  intuition that tool outputs dominate agentic context, which underpins [session history should
  not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
  and [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md).
- Ablation testing as infrastructure is a pattern worth surfacing: it is the measurement
  analogue of the [decomposition heuristics](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md),
  making local comparative results possible.

---

## 10 — Design Patterns & Takeaways

**Central claim.** Twelve cross-cutting patterns emerge from the four systems. Convergence is
strong: all four systems end up with roughly the same 5-layer architecture (system prompt
assembly → tool output truncation → message normalization → context window manager → compaction
engine → cache coordinator → diagnostics).

**The 12 patterns:**
1. Defense in depth (prevent → truncate → cache → prune → compact)
2. Estimation for heuristics, actuals for decisions
3. Stable-first prompt ordering
4. Graceful degradation (warn → cheap compact → expensive compact → block → recover)
5. Preserve continuity through compaction (summary + restored files + re-injected instructions)
6. Save full output, return previews
7. Provider-agnostic error handling (normalize 29+ overflow patterns)
8. Budget output tokens explicitly
9. Non-destructive operations
10. Cache SDK and model objects
11. Separate metadata from content
12. Instrument before optimizing

**Top-20 optimization table** is ordered by impact × effort: prompt caching, stable ordering,
output cap, tool result truncation, pruning, heuristic estimates, structured summaries, file
restoration, instruction preservation, duplicate detection, attribution, pagination, cache-aware
compaction, circuit breaker, variants, tool schema deferral, subagent isolation, disk spill,
non-destructive truncation, error normalization.

**KB alignment.**
- The convergent 5-layer architecture across four independent systems is a major convergence
  signal — the same kind of evidence our KB uses for related-systems comparison. Worth a
  paragraph in the convergence-signals section of the related-systems index: "Four production
  LLM harnesses independently arrive at the same component layering when optimizing the token
  economy of chat-loop agents."
- The top-20 table is an implicit priority ordering over [context engineering](../../notes/definitions/context-engineering.md)
  levers. Several patterns lack KB coverage and deserve notes of their own — see the synthesis
  for which.

---

## Cross-chapter synthesis notes

See `synthesis.md` for:
- The main theoretical alignment (where token-wiki instantiates existing KB theory)
- The gaps token-wiki reveals in KB theory (cache economics, observability, output budget)
- The tension with [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
  and the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md):
  token-wiki optimizes the path our theory argues should be avoided upstream
- Candidate follow-ups (new notes, additions to existing notes, curiosity flags)
