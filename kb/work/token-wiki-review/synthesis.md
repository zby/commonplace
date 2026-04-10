# Token Wiki — synthesis against commonplace theory

**Source.** `related-systems/token-wiki/` — a 10-chapter practitioner synthesis by the Token
Wiki authors, comparing token-optimization mechanisms across four production LLM harnesses:
Claude Code, Cline, Codex, and OpenCode. The headline claim: these four systems converged
independently on roughly the same 5-layer architecture (modular prompt assembly + multi-layer
tool output truncation + message normalization + threshold-based compaction + cache
coordination), plus cross-cutting diagnostics and observability.

**Scope of this synthesis.** Map each major token-wiki claim to the KB theory it instantiates,
extends, challenges, or leaves uncovered. Flag candidate new notes and additions to existing
notes. Do not mutate KB files — this is a workshop-layer analysis.

Per-chapter analyses live in `chapter-analyses.md`.

---

## 1. The central convergence: context is the binding constraint

Token Wiki is the strongest independent empirical confirmation this KB has seen of
[context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md).
Four production systems, built by different teams on different stacks, converge on:

- Context is the scarce resource. Every optimization is motivated by preserving it.
- Tool results (not model output) consume ~45% of context in agentic sessions. This is the
  single biggest token-consumer bucket, and everything else is secondary.
- A single file read is 5–10k tokens. A typical agentic session fills a 200k window within
  tens of turns if nothing manages it.
- Compaction (in some form) is not optional — all four systems implement it — but the cheapest
  useful interventions come *before* compaction, not through it.

These are not theoretical arguments. They are default numbers in shipping systems. That is the
strongest convergence signal on context-as-scarce-resource we have.

## 2. What token-wiki instantiates from KB theory

The KB already has theory for most of what token-wiki describes. Token-wiki is useful because
it gives concrete mechanism defaults and production numbers against which the theory can be
sharpened.

### 2.1. The architectural response taxonomy already predicts most of it

[context-efficiency-is-the-central-design-concern-in-agent-systems.md](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
lists six architectural responses: frontloading, progressive disclosure, context management,
sub-agent isolation, navigation design, and instruction notes over data dumps. Token-wiki's
12 patterns map onto those six categories with one genuinely-missing bucket (observability):

| Token Wiki pattern | KB architectural response |
|---|---|
| Stable-first prompt ordering; modular system prompt; variants | Progressive disclosure (routing, instruction specificity) |
| Tool output multi-layer truncation; pagination; disk spill | Context management (volume dimension) |
| Cache-aware microcompaction; structured summaries; post-compact file restoration | Context management (both dimensions) |
| Fork-based subagent seeding; guardian budgets; nesting limits | Sub-agent isolation |
| "Instructions never summarized"; re-inject from source | Frontloading + progressive disclosure |
| Save full output, return previews; `expand_topic`-style paging | Navigation design (agents decide what to read next) |
| Defense in depth (layering prevent → truncate → cache → prune → compact) | (implicit in KB but not explicitly named) |
| Instrument before optimizing; attribution; cache hit ratio | (not currently a KB component) |

Most rows are direct instantiations. Two rows are interesting: defense-in-depth is implicit
but not named in the KB, and observability is genuinely absent.

### 2.2. Subagent isolation — the mechanically cleanest match

The KB's [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md)
argues sub-agents are the one real scoping mechanism: they provide lexically scoped frames,
parent sees only return value, not internal reasoning. Token-wiki Chapter 8 describes the
same pattern mechanically:

- Fork-based history seeding (Codex): drop tool results, reasoning, intermediate messages;
  keep only system/user/final-answer. ~90% token reduction.
- Coordinator pattern (Claude Code): workers get restricted tool sets, own compaction
  lifecycle; coordinator sees only XML result notifications.
- Guardian subagent budgets (Codex): separate pools for message transcript vs. tool transcript
  so they can't crowd each other out.

This is lexical scoping, explicitly. Token-wiki's "filter out tool results and reasoning,
keep decisions" rule is an operational definition of which bindings are passed to the frame.
The scoping-note should cite this as the strongest available empirical confirmation that
production systems independently land on the frame discipline.

### 2.3. Effective-window calculation mechanically instantiates the soft bound — but only the output-reservation piece

The KB argues in [agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)
that the binding constraint is a soft degradation surface, not the advertised token limit.
Token-wiki Chapter 7 shows every production system computes an "effective window" < advertised:

- Claude Code: `advertised − min(maxOutput, 20_000) − overhead`
- OpenCode: `advertised × 0.95`
- Cline: explicit reserves by window size (42% overhead at 64k, 4% at 1M)

This is practitioner-level mechanical support for the distinction. **But the reason token-wiki
gives is different from the reason our theory gives.** Token-wiki's delta is mostly about
*output-token reservation* and *system-prompt fixed overhead*. Our theory argues the soft bound
is *task-dependent* and shifts with compositional depth, distractor density, and prompt framing.
Neither token-wiki chapter nor any of the four studied systems measures or adjusts for
task-dependent degradation.

This is a complementarity worth naming. Practitioners need a single number; they compute one
by subtracting known-fixed overhead. Theory says the *remaining* number is still task-dependent
and that the remaining uncertainty is the bigger one. Both are right; they are answering
different questions. An addition to the soft-degradation note would strengthen both: cite
token-wiki as the practitioner effective-window convention and note that it only covers the
first-order volume corrections.

### 2.4. Stable-first prompt ordering extends progressive disclosure

The KB's [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md)
argues always-loaded content should be slim and on-demand content should be detailed. Token-wiki
Chapter 3 (Prompt Caching) adds a second reason for the same ordering: **caching economics**.
Cache hits are 10x cheaper than fresh input, and any prefix mutation invalidates everything
after it. So the ordering "most stable → least stable" is both an attention/context discipline
(our theory) and a cost discipline (token-wiki).

This is convergent pressure from two independent arguments on the same design — a stronger case
than either alone. A small addition to the loading-frequency note would cite Chapter 3 as a
second, independent reason for the ordering.

### 2.5. "Instructions must never be summarized" formalizes a KB implicit

All four systems in token-wiki share one rule: **system instructions are never part of the
summarizable content; they are always re-injected fresh from source** after compaction. This
is implicit in [always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)
and [AGENTS.md should be organized as a control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md),
but not stated as a sharp invariant. Token-wiki states it explicitly as a design principle:
"never summarize instructions, always re-inject from source to prevent instruction drift across
compaction cycles."

This is worth promoting to an explicit claim in the always-loaded-context note: the content of
always-loaded surfaces must be re-loaded from source on every call, not passed through any
lossy transformation, because instruction drift compounds with each compaction cycle.

## 3. What token-wiki adds that KB theory doesn't yet cover

Three topics are genuinely thin in KB theory and worth new notes (or major additions).

### 3.1. Cache economics as a second scarce resource

**The gap.** The KB treats context as the scarce resource. Token-wiki reveals a *second*
scarce resource: the **cache prefix**. A cache hit is 10x cheaper than fresh input; any prefix
mutation invalidates everything after. This constraint shapes architecture in ways the KB does
not currently discuss:

- Compaction and caching are in direct tension. Naive compaction rewrites history → cache
  break → 10x cost spike on the next turn. Cache-aware compaction uses server-side
  `cache_edits` to delete tool results without mutating the cached prefix.
- The prompt ordering principle has two reinforcing motivations (attention + cache) rather
  than one.
- Per-tool schema hashing is a diagnostic pattern specifically for finding the *source* of
  cache breaks: 77% of breaks in Claude Code are MCP tool schema changes.
- The single-marker-on-messages rule prevents KV memory waste.

**Candidate new note.** Something like *"Prompt caching is a second scarce resource that
constrains context management mechanisms."* Key claims:
1. Cache hits are an order of magnitude cheaper than fresh input, making them the largest
   available cost lever.
2. Cache invalidation is prefix-based and silent; any mutation to a stable-layer token
   invalidates the entire suffix.
3. This constrains which context-management mechanisms are legal: destructive truncation and
   non-cache-aware compaction trade 10x cost savings for small token savings.
4. Stable-first prompt ordering is motivated by both attention and cache; the constraints are
   aligned.
5. Diagnostic observability (per-component hashing) is needed because the cache economy is
   silent — breaks produce no error, just a quiet cost regression.

This note would also be a good landing place for the "cost of verbosity" observation:
commonplace's own AGENTS.md is a symlink to CLAUDE.md — so by sitting in a stable always-loaded
position, it gets the full cache benefit *only* if it stays byte-identical across sessions.
Dynamic substitution (timestamps, session tokens) in the prompt file would silently kill the
cache.

### 3.2. Observability as a prerequisite, not a finishing step

**The gap.** [Context engineering](../../notes/definitions/context-engineering.md) lists
routing, loading, scoping, and maintenance as the operational components. Observability is
missing. Token-wiki argues, with citations to production practice, that **observability is a
prerequisite for the other four being tunable**: you can't optimize what you can't attribute.
Chapter 9 lists:

- Per-source attribution (tool results, tool requests, assistant, human, system, attachments).
- Per-tool breakdown (which tools cost the most tokens, which are re-invoked).
- Duplicate read detection (the #1 waste pattern: file re-reads indicate the model has lost
  track of files it already read — a concrete symptom of context instability).
- Cache hit ratio as health metric (below 80% something is breaking).
- Query-source tracking (which agent/compaction/tool initiated each API call).
- Ablation testing as a measurement primitive.

**Candidate addition.** Observability could be a fifth operational component in the
[context-engineering definition note](../../notes/definitions/context-engineering.md):
*"attribution — knowing where tokens went and why, as a prerequisite for the other four."*
The strong empirical claim from token-wiki is "developers assume model output is the biggest
cost; in agentic systems, tool *results* dominate (~45%). Without measurement, you optimize
the wrong thing."

Duplicate read detection is a particularly interesting signal: it's an observability mechanism
that directly measures the cost of the flat-context anti-pattern. Every duplicate read is a
symptom of the model losing track of what it already read, which is what
[session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
argues against at a higher level. The empirical waste numbers are citable evidence for that
claim.

### 3.3. Output token reservation is a hidden context tax

**The gap.** The KB discusses context scarcity almost entirely in terms of *input* context.
Token-wiki Chapter 2 and Chapter 7 surface an overlooked dimension: **reserving output tokens
from the context window is a hidden input-context tax.** Claude Code's empirical finding:

- Models advertise 128k output limits.
- 99th-percentile actual responses use ~5k tokens.
- Reserving the advertised limit wastes ~123k of usable input context per request.
- Solution: cap output reservation at 8k, retry with 64k on overflow.

This is a concrete instance of [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md)
inverted: committing less output budget *frees* input budget. The static knowledge (empirical
response distribution: 99% of responses ≤ 5k) moves commitment cost out of the bounded call.

**Candidate addition.** A short section or note on "output token reservation is a commitment
cost on input context" — citing the Claude Code data. This is small enough to fit as an
addendum to the frontloading note or to live in a new note on budget discipline.

### 3.4. Defense in depth as an explicit discipline

**Minor gap.** The KB has all six architectural responses in the context-efficiency note, but
does not explicitly say "use them in layers, cheapest first." Token-wiki's "prevent → truncate
→ cache → prune → compact" ordering is the missing meta-pattern. This might be a one-paragraph
addition to the context-efficiency note rather than a new note.

## 4. Where token-wiki and KB theory are in tension

### 4.1. Token-wiki optimizes a path the KB argues should be avoided

This is the most important tension and the one worth thinking through carefully.

The KB's [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
and [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md)
argue that the core problem in chat-loop agents is **the conflation of two decisions**: what
to persist and what to load into the next call. Chat interfaces and framework-owned tool loops
default to "load everything," which forces compaction as remediation. The KB argues the right
move is upstream: store everything in `K` (symbolic scheduler state), select a clean view for
each bounded call, stop making history the default input.

Token-wiki takes the chat-loop architecture as given. All four studied systems are tool-loop
agents that treat conversation history as the primary state carrier. Their entire optimization
vocabulary — compaction, pruning, cache-aware deletion, circuit breakers, fork-based seeding —
is mitigation for the cost of history-as-state. The convergent 5-layer architecture it
documents is the cost of making that architectural choice work.

Neither position is wrong. But they are answering different questions. Token-wiki says:
"given that you have built a chat-loop agent, here is how the four biggest production systems
manage its token economics." KB theory says: "the chat-loop architecture is a degraded variant
of symbolic scheduling; you can avoid most of the cost by not making history the default
next-call input." Both are useful. The tension is load-bearing for anyone designing a new
system.

Two concrete observations follow:

1. **Token-wiki's best mechanisms are exactly the ones that push toward the symbolic-scheduling
   model.** Save-full-output-to-disk with reference handles. Fork with aggressive filtering.
   Never summarize instructions. Non-destructive truncation with deletedRange metadata.
   Subagent coordinator pattern. Each of these moves state *out* of the bounded call and into
   a symbolic store whose view into the call is explicit. The convergent architecture is
   already bending toward `K` + `select(K)`, even if the studied systems don't formalize it
   that way. The [LLM-mediated schedulers are a degraded variant](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)
   note is validated here: these systems are hybrid degraded variants improving themselves by
   recovering the clean model piece by piece.

2. **The mechanisms token-wiki frames as "hard to implement" (ranked High effort in the top-20
   table) are exactly the ones that require commitment to the clean model.** Cache-aware
   microcompaction (rank 13, High effort). Variant-based system prompts (rank 15, High effort).
   Both require explicit architectural moves that chat-loop-first systems struggle to retrofit.

This tension deserves a workshop note or a thread in an existing note. Candidate framing:
*"Token-wiki's convergent production architecture is the highest-effort implementation of a
remediation strategy for a choice that doesn't have to be made. Systems designed around the
bounded-context orchestration model from the start can skip most of the 5-layer stack."*

### 4.2. Effective-window approximations are volume-only

Covered in §2.3. Practitioner effective-window calculations are all first-order volume
corrections. Our soft-degradation theory argues the remaining window is still task-dependent.
Not a contradiction but a place where practitioner and theoretical framings stop at different
points.

### 4.3. "4 bytes = 1 token" and the irrelevance of tokenizers to threshold decisions

Token-wiki's universal heuristic (`length / 4`) is a soft but interesting data point against
attempting precise token measurement in the symbolic layer of a scheduler. All four systems
deliberately avoid shipping a tokenizer; exact counts come from API responses after the fact.
This validates the [bounded-context orchestration](../../notes/bounded-context-orchestration-model.md)
principle that the scheduler should do cheap, approximate, deterministic bookkeeping while
reserving costly judgment for the bounded call. The tokenizer is judgment; the heuristic is
bookkeeping.

## 5. Candidate follow-ups

Listed in rough priority order. None of these are done automatically — this list is for later
human review.

### 5.1. New notes

1. **Prompt caching is a second scarce resource that constrains context management** (§3.1).
   Highest priority. Genuinely new theory ground and strong production evidence. Would cite
   Chapter 3 directly and add a new constraint-type to the context-engineering vocabulary.

2. **Observability is a prerequisite component of context engineering** (§3.2). Could live
   as an extension to the [context-engineering definition](../../notes/definitions/context-engineering.md)
   or as a standalone. The duplicate-read waste pattern is the best single piece of evidence
   for [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
   that the KB currently has access to.

3. **Token-wiki as a related-system review** (`kb/notes/related-systems/token-wiki.md`). Follows
   the shape of the existing `llm-wiki.md` and `virtual-context.md` reviews. Captures:
   convergent 5-layer architecture, strongest borrowable patterns, comparison with commonplace
   (which is not a runtime, so borrowing is at the theoretical/convergence-signal level rather
   than implementation-level), tension with bounded-context orchestration model.

### 5.2. Additions to existing notes

1. **[context-efficiency-is-the-central-design-concern-in-agent-systems.md](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)**
   - Add token-wiki to the practitioner-convergence section alongside Lopopolo, Raschka, etc.:
     "Four production LLM harnesses (Claude Code, Cline, Codex, OpenCode) independently converge
     on a 5-layer token-management architecture, empirical support for context-as-scarce-resource
     at production scale."
   - Add defense-in-depth as the layering discipline across the existing architectural responses
     (§3.4).

2. **[agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)**
   - Add practitioner "effective window" conventions as first-order volume corrections.
     Token-wiki's Chapter 7 is the citation. Note that practitioner deltas are from
     output-reservation and fixed overhead, while theoretical soft-degradation is
     task-dependent — these are complementary corrections at different layers.

3. **[llm-context-is-composed-without-scoping.md](../../notes/llm-context-is-composed-without-scoping.md)**
   - Add token-wiki Chapter 8 as the strongest available production-level confirmation of the
     frame discipline. Codex fork-based seeding (keep system/user/final-answer, drop tool
     results/reasoning) is almost an operational definition of lexically-scoped frames.

4. **[instruction-specificity-should-match-loading-frequency.md](../../notes/instruction-specificity-should-match-loading-frequency.md)**
   - Add the cache-cost argument for stable-first ordering. This gives the note a second
     independent motivation beyond attention economics.

5. **[always-loaded-context-mechanisms-in-agent-harnesses.md](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md)**
   - Promote "always-loaded content must be re-injected from source, never passed through
     lossy transformation" to an explicit design principle. Cite token-wiki's unanimous
     convergence on "instructions never summarized."
   - Add Codex's 32 KiB cap on AGENTS.md as a data point — unbounded always-loaded files are
     a production risk, not a theoretical concern.

6. **[frontloading-spares-execution-context.md](../../notes/frontloading-spares-execution-context.md)**
   - Add output-token reservation as an inverted frontloading instance: empirical response
     distribution (static knowledge) moves commitment cost out of the bounded call. Cite
     Claude Code's 8k/64k retry strategy and the 99%-at-5k finding.

7. **[session-history-should-not-be-the-default-next-context.md](../../notes/session-history-should-not-be-the-default-next-context.md)**
   - Use duplicate-read-detection (~10-20% of context wasted on re-reads) as empirical
     evidence for the cost of transcript inheritance.
   - Note that token-wiki's strongest mechanisms (save-to-disk + reference handle, fork with
     filtering, coordinator pattern) are partial recoveries of the clean model.

8. **[bounded-context-orchestration-model.md](../../notes/bounded-context-orchestration-model.md)**
   - Cite token-wiki as convergent practitioner evidence. The convergent 5-layer stack is a
     remediation for the cost of not using the clean model; the highest-effort mechanisms
     (cache-aware compaction, variants) are partial recoveries.

### 5.3. Curiosity flags

- **The circuit breaker story is evidence for oracle-gated iteration.** Claude Code discovered
  1,279 sessions had 50+ consecutive auto-compact failures wasting ~250k API calls/day before
  they added a MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3 cap. This is a production instance of
  an unbounded loop consuming resources without verification — the same failure mode our KB's
  workshop theory warns about in iterative review/fix loops. Worth a brief log entry if we have
  a note on oracle-gated loops or retry caps.

- **The per-tool cache-break attribution (77% are MCP tool schema changes) is a striking
  operational signal.** It says that in practice, the most unstable component of the
  always-loaded context is the tool schema layer — exactly the layer that practitioners
  historically treat as fixed infrastructure. Worth noting when we think about tool surface
  design.

- **Codex's ghost snapshot pattern (background git commit, filtered out of API calls) is a
  clever use of the execution substrate to provide undo at zero token cost.** This maps
  perfectly onto [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md)
  applied to runtime: git itself is the substrate, and it already provides the invariants
  needed for rollback. Worth citing when we discuss execution substrate patterns.

- **OpenCode's chain-collapse pattern for tool traces is similar to Virtual Context's approach**
  (see existing `virtual-context.md` review). Both compress tool traces into visible stubs with
  restore paths. This is convergent evidence for a pattern.

## 6. What token-wiki does not cover

Worth naming the limits so the theory doesn't over-borrow:

- **All four systems are chat-loop agents.** Token-wiki's evidence doesn't say whether
  non-chat-loop architectures (symbolic-scheduler-first systems like Spacebot, or the
  bounded-context orchestration model) face the same problems. Probably they face fewer; the
  mechanisms aren't needed if you avoid the problem upstream.
- **All four systems target conversational coding assistants.** Agentic systems in other domains
  (long-horizon research, multi-agent coordination, code-repair-at-scale) may have different
  token economies. Token-wiki's defaults are evidence for coding agents, not universal.
- **Task-dependent soft-degradation is invisible to these systems.** Their effective-window
  calculations are first-order volume corrections only. Complexity-dimension degradation (see
  ConvexBench, the KB's theory of compositional depth) is not addressed. These systems will
  silently degrade on tasks where the token count fits but the compositional structure doesn't.
- **No theory of what to cache vs. what to regenerate.** The studied systems treat caching as
  a binary of cached-or-not; there is no discussion of the relative value of different cached
  items or of tradeoffs between cache-prefix stability and content freshness.
- **No empirical comparison across tasks.** The data is per-system averages, not per-task
  distributions. We can't tell from token-wiki whether the 45% tool-result share is universal
  or specific to a particular workload mix.

## 7. One-paragraph summary

Token Wiki is a practitioner synthesis of token-management mechanisms across four production
LLM coding agents. It is the strongest available independent empirical confirmation of the
KB's core claim that context is the scarce resource in agent systems, and its 12 patterns map
almost one-to-one onto the KB's existing architectural-response taxonomy. The three topics it
adds which the KB does not yet cover well are: **cache economics as a second scarce resource**
whose fragility constrains compaction and ordering decisions; **observability as a prerequisite
component of context engineering** rather than a finishing step; and **output-token reservation
as a hidden input-context tax** that should be sized by actual response distributions rather
than advertised limits. The deepest tension with KB theory is that token-wiki takes the
chat-loop architecture as given and optimizes within it, while the bounded-context orchestration
model argues the chat loop is a degraded variant that forces most of these mechanisms into
existence; the most effortful mechanisms in the convergent production stack (cache-aware
microcompaction, fork-based subagent seeding, variant-based system prompts, non-destructive
truncation) are precisely the ones that partially recover the clean symbolic-scheduling model
from inside a chat-loop architecture.
