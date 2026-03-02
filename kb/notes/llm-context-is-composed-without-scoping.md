---
description: LLM context has no scoping — system prompts, skills, user messages, and tool outputs are concatenated into one global namespace; sub-agents are the one mechanism that provides isolation and should get clean lexically scoped frames by default
type: note
traits: []
areas: [computational-model]
status: seedling
---

# LLM context is composed without scoping

An LLM's context is assembled by concatenating system prompts, skill bodies, user messages, and tool outputs into a single token stream. There is no scoping mechanism. Everything is global — every token is visible to every other token, and there is no way to say "this binding is local to this skill" or "this tool output should not influence instruction interpretation."

This is not even dynamic scoping, which at least has a stack with push and pop. It is flat concatenation — the [homoiconic medium](./llm-context-is-a-homoiconic-medium.md) with no structure imposed on top. The result is the same pathologies that [dynamic scoping produces](./the-append-only-log-gives-llms-dynamic-scopings-pathologies.md) — spooky action at a distance, name collision, inability to reason locally — but without even the stack discipline that dynamic scoping provides.

Flat concatenation also creates a composition-specific problem: **capture**. A skill says "summarize the document." The document contains "don't summarize this section, skip it." The data-level use of "summarize" captures the instruction-level meaning. This is prompt injection framed as a hygiene failure — the same problem Scheme's hygienic macros solve for code generation.

## Within-frame hygiene

Within a single context, the only scoping mechanisms available are weak conventions:

- **Role markers** (system/user/assistant/tool in chat APIs) — primitive structural separation, but the LLM still sees all roles in one attention pass
- **Delimiters and quoting** — XML tags, markdown fences, explicit "the following is data, not instructions" markers — conventional, not enforced
- **Ordering conventions** — system prompt first, then context, then user message — exploits primacy/recency effects but provides no isolation

These are the LLM equivalent of coding conventions in a language without a module system. They help, but they can't prevent capture.

## Sub-agents as the scoping mechanism

Sub-agents are the one place where real isolation is achievable. A sub-agent gets a fresh context — its own system prompt, its own input, no inherited conversation history. The parent sees only the return value, not the internal reasoning.

This is lexical scoping: the sub-agent's "code" (its prompt) determines what's visible, not the runtime history. The design principle, borrowed from Common Lisp: **lexical scope by default, dynamic scope when explicitly declared.**

**Lexically scoped (frame-local):** The sub-agent's system prompt, the specific input for this invocation, any context the caller explicitly passes. Determined at "definition time" — when the sub-agent is designed.

**Dynamically scoped (inherited):** User preferences ("use a formal tone"), safety policies, global constraints, project-level conventions. Explicitly declared as "special" bindings that persist across all frames. The llm-do system prompt layer already approximates this — it's the dynamic environment that persists while call-specific context is lexically scoped.

The key word is *explicitly*. In a flat context, everything is implicitly global. In the scoped model, cross-frame bindings are a deliberate design choice.

## The return value problem

The stack metaphor exposes a question flat contexts dodge: what does a sub-agent *return*? A function returns a typed value. A sub-agent returns natural language, or structured data, or a partial result with caveats.

This is where [crystallisation](./crystallisation.md) becomes load-bearing. Early in exploration, sub-agents return loose natural language — the equivalent of an untyped s-expression. As you crystallise, return values become structured, typed, validated. The stack architecture *enables* this progressive typing because each frame boundary is an explicit interface point where you can impose increasingly strict contracts.

The flat context has no such interface points. Everything bleeds into everything, making it impossible to even ask "what is the contract between these two stages of reasoning?"

## What exists today

Most agent frameworks use flat contexts. Sub-agent architectures that approximate lexical scoping exist but are ad hoc:
- llm-do's [unified calling conventions](./unified-calling-conventions-enable-bidirectional-refactoring.md) give each agent its own system prompt and arguments — frame-local context
- Claude Code's sub-agent tool spawns agents with clean context plus a task description — lexical framing
- The [context loading strategy](./context-loading-strategy.md) (always-loaded → on-demand → task-specific) is a form of binding-time analysis for agent context

Several claw-design patterns are already lexical scoping in practice:

- The [skill/methodology tier separation](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — skills are frame-local context loaded deterministically; methodology is out of scope unless explicitly loaded
- [Type signatures on skills](./instructions-are-typed-callables.md) — frame interfaces that declare what bindings a sub-agent receives
- [Automatic context injection](./agent-statelessness-means-harness-should-inject-context-automatically.md) — the harness constructs frames by determining which bindings to inject rather than exposing the full accumulated context

None of these frame it as a scoping discipline. Making it explicit would clarify what gets inherited and what gets isolated.

## Undeveloped directions

These ideas follow from the stack-frame model but don't yet have concrete examples:

**Tail-call optimisation for sub-agents.** If a sub-agent's last action is delegating to another sub-agent, you don't need to keep the first frame alive — discard its context entirely. In a flat context, the first agent's reasoning is still consuming tokens.

**Stack unwinding for error recovery.** When a deep sub-agent fails, selectively discard its context while preserving the frames above it that hold recovery logic. In a flat context, there is no clean way to undo a failed sub-task's contamination. This connects to condition/restart systems in Common Lisp.

**Recursion with clean frames.** A flat context makes recursive decomposition painful because each recursive call appends to the same context. With a proper stack, each recursive call gets a clean frame and completed calls are popped — bounded by single-frame size, not cumulative size.

---

Relevant Notes:
- [the append-only log gives LLMs dynamic scoping's pathologies](./the-append-only-log-gives-llms-dynamic-scopings-pathologies.md) — problem: the flat log accumulates context globally; this note addresses isolation through sub-agent frames
- [llm context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — amplifies: the medium provides no structural boundaries, so scoping must be imposed by architecture
- [unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — existing approximation: llm-do's per-agent system prompts and arguments are frame-local context
- [crystallisation](./crystallisation.md) — enables: frame boundaries are interface points where return values can be progressively typed
- [context-loading-strategy](./context-loading-strategy.md) — grounds: the loading hierarchy is a form of binding-time analysis for what's in scope
- [agent statelessness makes skill layers architectural, not pedagogical](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — exemplifies: the skill/methodology tier separation is lexical scoping in practice
- [instructions are typed callables](./instructions-are-typed-callables.md) — enables: type signatures on skills are frame interfaces — declaring what bindings a sub-agent receives
- [agent statelessness means the harness should inject context automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — mechanism: automatic context injection constructs lexically scoped frames

Topics:
- [computational-model](./computational-model.md)
