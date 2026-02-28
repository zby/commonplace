# RLM Implementations vs llm-do

## Context

Two open-source Recursive Language Model implementations — `ysz/recursive-llm` and
`alexzhang13/rlm-minimal` — explore how LLMs can recursively decompose tasks by
writing and executing code. We compare them with llm-do to understand where the
designs overlap and where they diverge.

A third RLM implementation, Shesha, is covered separately in `shesha-comparison.md`
(it adds a full document ingestion pipeline). Observations that apply to the RLM
family as a whole are noted here.

## The Implementations

### ysz/recursive-llm

- Repo: `https://github.com/ysz/recursive-llm`
- Single `RLM` class with `completion()` / `acompletion()` running a model-in-the-loop
  REPL until `FINAL(...)` is emitted.
- Recursion via `recursive_llm(sub_query, sub_context)` injected into the REPL; creates
  a fresh `RLM` instance at `_current_depth + 1`.
- Context stored as a Python variable, not embedded in the prompt.
- Sandboxing via RestrictedPython with whitelisted builtins. No file/network tools,
  no approval boundary.
- Per-instance depth and iteration limits; no global usage aggregation.

### alexzhang13/rlm-minimal

- Repo: `https://github.com/alexzhang13/rlm-minimal` (commit `1bed65d`)
- Intentionally stripped-down "minimal version."
- Model emits ` ```repl``` ` blocks; the system executes them and appends output back
  into the message list. `FINAL(...)` / `FINAL_VAR(...)` terminates the loop.
- Single-depth recursion by default via `llm_query` (`Sub_RLM`). Deeper nesting
  requires manual wiring.
- Execution via `exec`/`eval` with curated `__builtins__`; allows `__import__` and
  `open` — not a hard sandbox.
- OpenAI-only, GPT-5 defaults, presentation-first logging (ANSI/rich).

### What They Share

Both implementations follow the same pattern:

- **Model-driven REPL.** The LLM decides what code to write and execute; the system
  runs whatever the model emits.
- **FINAL protocol.** Explicit termination signal rather than structured tool returns.
- **Context as a variable.** Large context passed as data in the REPL namespace.
- **Pure computation.** Generated code reads data and produces answers but causes no
  side effects.
- **Ephemeral code.** Generated code is discarded after each run — every query starts
  from scratch.
- **Single concern.** Both focus on long-context exploration / recursive decomposition,
  not general agent orchestration.

## How Novel Is the RLM Pattern?

The RLM authors frame their work as a breakthrough. The key insight is real:
sub-agents orchestrated in code can do map-reduce over large contexts, aggregating
results programmatically and only passing the outcome back to the LLM. This is
genuinely more efficient than naively forwarding everything through prompts.

But none of the ingredients are new. The underlying primitive — a tool that calls an
LLM — has been available in agent frameworks for a long time. PydanticAI has
documented [agent delegation](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation-and-dependencies)
since its early releases: you call `other_agent.run(...)` inside a tool function, and
the parent agent resumes with the result. Many coding agents (Cursor, Claude Code,
Devin) also spawn sub-agents that can recursively invoke further sub-agents. You could
have built an RLM on top of PydanticAI long before the term existed.

What RLM implementations contribute is a specific *recipe* — the right proportions of
known ingredients:

1. **Model-driven REPL** — the LLM writes arbitrary code, not just tool calls
2. **Context as a variable** — large data passed in the execution namespace, not the
   prompt
3. **FINAL protocol** — explicit termination rather than structured returns

Discovering the right proportions matters — the combination produces results that the
individual ingredients don't. But it is a usage pattern on top of existing
capabilities, not a new computational primitive.

### Map-Reduce Without a REPL

A stronger version of the novelty argument claims that standard CLI agents *cannot*
do map-reduce at all — that you need RLM's REPL to aggregate sub-agent results
programmatically rather than forwarding them through the parent's context. This is
wrong. CLI agents can replicate the pattern using files and shell tools:

1. **Map**: Spawn N sub-agents (e.g. Claude Code's Task tool), each writing results to
   a file.
2. **Reduce**: A shell command (`jq`, `paste`, a Python script) combines those files
   programmatically.
3. **Parent context**: Only sees the final reduced output — the intermediate results
   never enter any LLM context.

The file system plays the role of RLM's Python variables, and the shell plays the
role of RLM's inline code. The reduction is programmatic in both cases — no LLM
needed for the combine step, and the parent's context cost is near zero.

Note that the CLI agent also *writes* the reduction code — the shell commands or
scripts that combine results are LLM-authored, just like the REPL code in RLMs.
The model is authoring both the decomposition strategy and the reduction logic in
both cases.

The remaining difference is *cohesion* (see §5 below): in an RLM the decomposition
and reduction are a single program visible in one context. In the CLI pattern, the
same logic is spread across multiple tool calls — the model writes the map step,
sees the results, then writes the reduce step. The plan is sequential rather than
expressed as one coherent program. But this is a difference of ergonomics, not of
computational capability. The programmatic map-reduce that RLMs claim as exclusive
to their architecture is achievable with standard CLI tooling.

## Where llm-do Diverges

The RLM implementations and llm-do both support recursive dispatch between LLM and
code, but they optimize for different things. Five differences follow from this, the
first four building on each other, and a fifth addressing a genuine RLM advantage.

### 1. Power vs. Evolvability

**RLMs optimize for power** — solve harder problems at a point in time. The LLM writes
divide-and-conquer algorithms over large contexts. An explicit boundary between LLM
calls and code calls is fine because you're not planning to move things across it.

**llm-do optimizes for evolvability** — systems that grow and mature. The core insight
is *stabilizing*: LLM applications evolve by progressively converting stochastic
behavior into deterministic code, and vice versa (see [agentic systems are probabilistic programs](../agentic-systems-are-probabilistic-programs.md)).

```
Stochastic (prompt)  →  Deterministic (code)
         ↑                      ↓
         └── soften ←── stabilize ──┘
```

This requires a **unified calling convention** — whether a capability is implemented
as a prompt or as code must be invisible at the call site, because logic will migrate
between them as patterns emerge. Refactoring cost is everything.

Recursion in llm-do wasn't a design goal. It emerged from following software's natural
structure: functions call functions, workers call workers, and the refactoring
shouldn't stop because you hit framework limitations.

### 2. Ephemeral vs. Versioned Code

This is the most practically significant difference.

RLM-generated code is **ephemeral** — written per query, executed once, discarded.
Every run re-derives logic from scratch.

llm-do tools are **versioned infrastructure** — stored in files, checked into version
control, tested, reviewed, and reused across runs. They participate in the standard
software lifecycle:

- **Version control** — `git diff`, `git blame`, `git bisect` all work
- **Testing** — stable interfaces that can be unit-tested
- **Code review** — same review process as any other code
- **Reuse** — a tool written for one agent is available to all agents in the project
- **Debugging** — when something breaks, the code is there to read and fix

Code versioning is a solved problem with decades of tooling. Ephemeral code opts out
of all of it.

Crucially, versioned does **not** mean human-written. The LLM can generate tool code
too — via bootstrapping (LLM generates tools at runtime that graduate into permanent
infrastructure) or out-of-band (a coding assistant writes tools that get committed).
The difference is what happens *after* generation: in RLM systems the code vanishes;
in llm-do it enters the codebase and accumulates value.

```
RLM:    LLM generates code → executes → discards
llm-do: LLM generates code → executes → saves → tests → versions → reuses
```

This is the concrete mechanism behind progressive stabilization — patterns the LLM
discovers don't have to be rediscovered. They become permanent, tested, cheap-to-run
infrastructure.

### 3. Purity vs. Side Effects

The first two differences lead to a third: RLMs and llm-do operate in fundamentally
different trust regimes.

RLM-generated code is pure — it reads data and produces answers but causes no side
effects. This is what makes the approval problem disappear: if code can't cause side
effects, there's nothing to approve. The sandbox *is* the approval policy.

llm-do agents do real work — file writes, shell commands, API calls — so they need
approval gates at the trust boundary. This gives llm-do both modes when sandboxed
execution is available:

- **Pure sandbox**: LLM-generated code for computation/analysis, no approvals needed
- **Side-effectful tools**: developer-written tools for real work, approval-gated

The RLM approach only needs the first mode. llm-do needs both.

### 4. Trivial vs. Managed Reentrancy

The first three differences combine to create a fourth: recursion in RLMs is almost
free, while in llm-do it's a significant engineering concern.

In RLM implementations, `recursive_llm(sub_query, sub_context)` creates a fresh
instance with its own REPL namespace. There is no shared mutable state, no side
effects, no resource lifecycle. The fresh instance runs, returns a value, and
disappears. Reentrancy is trivial because there's nothing to re-enter — each call is a
self-contained computation in an isolated namespace.

In llm-do, when a worker calls another worker (or itself), the system must:

- **Isolate state per call** — each depth gets a fresh `CallFrame` with its own message
  history and fresh toolset instances, so nested calls don't leak database handles, file
  cursors, or other stateful resources from the parent.
- **Stay async throughout** — nested calls must `await` directly rather than creating
  new event loops, or the system deadlocks.
- **Route approvals per depth** — side-effectful tools need consent at each level, with
  session-level caching that spans the call tree.
- **Manage toolset lifecycles** — each call scope runs `__aenter__`/`__aexit__` hooks
  for resource setup and cleanup, and these must nest correctly even under exceptions.
- **Enforce depth limits** — without guards, agents can recurse infinitely; llm-do
  tracks depth per `CallFrame` and raises at `max_depth`.

This complexity is the direct cost of the previous three design choices. Side effects
require approval routing. Stateful toolsets require lifecycle management. The unified
calling convention means the same dispatch path handles both plain code tools and nested
LLM calls. RLMs avoid all of this by being pure, ephemeral, and single-concern —
reentrancy is trivial precisely because there's nothing stateful to protect.

### 5. Opaque Delegation vs. Conversation Horizon

This is a genuine RLM advantage that the previous four divergences don't capture,
clarified by researcher Omar Khattab.

In subagent architectures (including llm-do's current design), delegation happens
through explicit tool invocations. When agent A calls agent B, the call is opaque: A
doesn't see B's instructions, reasoning, or internal decomposition — only the returned
result. Each delegation is a black box at the call site. The parent agent cannot reason
about the recursive structure of the work it's orchestrating.

In RLMs, recursion is integrated directly into the model's self-understanding of its
conversation horizon. The LLM writes
`results = [recursive_llm("summarize", chunk) for chunk in chunks]` — it *sees* the
decomposition strategy, understands that sub-calls will happen, and reasons about
aggregation as part of the same cognitive process. The recursion is part of the model's
plan, not hidden behind an API boundary.

This has a concrete efficiency consequence: subagent delegation requires the parent to
re-attend over its full context at each step (quadratic attention cost in the number of
delegations), while RLM's code-driven recursion allows linear or superlinear LLM
calls — intermediate results live in Python variables, not in any model's context
window.

**Replicating this in llm-do.** Two approaches could close the gap:

1. **Make agent instructions visible to the caller.** If the calling agent can see the
   system prompts and schemas of the agents it delegates to, it gains a model of what
   sub-agents do — closing the opacity gap. The caller can reason about delegation
   structure and plan multi-step decompositions, even though execution remains separate.

2. **Restructure agent composition around conversation horizon.** Redesign how agents
   describe their delegation capabilities so the orchestrator reasons about the full
   plan upfront — more like writing a program than making one-at-a-time opaque tool
   calls. Python entry points (like `pitchdeck_eval_code_entry`) already move in this
   direction: orchestration logic is code that structures the full delegation plan,
   rather than an agent that discovers the next step incrementally.

Neither approach gives llm-do the pure efficiency win of RLM's in-variable
intermediates. But they address the deeper issue — opacity — which is what prevents
the calling agent from reasoning well about recursive work.

## Comparison Table

| Aspect | RLM implementations | llm-do |
|--------|---------------------|--------|
| **Priority** | Power | Evolvability |
| **Control flow** | Model-driven REPL | Code-driven orchestration |
| **Recursion** | Injected REPL function | Named workers with schemas |
| **Composition** | Implicit (code writes code) | Explicit (worker declares toolsets) |
| **Code lifespan** | Ephemeral | Versioned infrastructure |
| **Side effects** | None (pure computation) | Full (file, shell, API) |
| **Trust boundary** | Sandbox (containment) | Approval system (consent) |
| **Calling convention** | Explicit (LLM ≠ code) | Unified (LLM = code) |
| **Refactoring cost** | Pay the tax | Free (call sites don't change) |
| **Reentrancy cost** | Trivial (nothing to protect) | Managed (isolation, lifecycles, approvals) |
| **State isolation** | Fresh instance per call | `CallFrame` per call |
| **Delegation transparency** | Integrated — model sees its own decomposition strategy | Opaque — tool call returns result only |

## Open Questions

- Do we want an RLM-style REPL toolset (stateful Python exec) as a built-in or
  example? If so, should approvals gate arbitrary code execution or only
  side-effectful tools within that environment?
- Should we add a long-context exploration example that mimics `context` as a
  variable, or keep long-context handling out of scope?
- Is there value in an iterative runner that loops a worker until a FINAL-style
  termination signal, or does the standard agent loop already cover this?

## Conclusion

RLM implementations and llm-do both support true recursion — LLM calls that trigger
new LLM conversations — but from different motivations, with different consequences:

- **RLM implementations** solve specific problems (context length, recursive
  decomposition) with a clever trick: let the LLM write its own algorithms. Code is
  ephemeral — powerful in the moment, but nothing accumulates between runs.

- **llm-do** provides a framework for evolving LLM applications. Code — whether
  human-written or LLM-generated — is versioned infrastructure that participates in
  the standard software lifecycle. The unified calling convention makes refactoring
  across the stochastic-deterministic boundary cheap, so the system can breathe:
  stabilize as patterns emerge, soften when rigidity hurts.

The two key differentiators: *code that accumulates value* (versioned, tested, reused
rather than re-derived on every run) and *seamless refactoring* (a worker can become a
tool, a tool can become a worker, and call sites never change).
