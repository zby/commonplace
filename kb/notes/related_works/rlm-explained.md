# RLM (Recursive Language Model) — For Programmers

## The Strange Regime

To understand RLMs, you first need to understand the regime they operate in — because
it would look strange to any programmer.

In normal software, large data lives on disk. You read what you need, process it, move
on. No one loads a 100k-token codebase into a function's argument list. But RLM
benchmarks (arXiv:2512.24601) work exactly this way: the entire input is handed to the
system as a single blob. No filesystem, no tools. Just "here's your data, answer the
question."

In this regime, there is no good place to put the data. The only default option is
the LLM's prompt — which means the model has to reason over 100k tokens at once. In
any normal coding environment, the data would just live on disk and the agent would
read slices as needed. RLM's contribution is inventing a third place: a REPL variable
in a Python namespace that the LLM accesses by writing code.

The paper's baseline ("CodeAct + Sub-calls") puts data in the prompt. RLM puts it in
the REPL:

| Benchmark    | CodeAct+Sub-calls | RLM   |
|--------------|-------------------|-------|
| CodeQA       | 24.0%             | 62.0% |
| OOLONG       | 40.0%             | 56.5% |
| OOLONG-Pairs | 28.4%             | 58.0% |

The results look dramatic, but any programmer's first instinct — read from disk in
pieces — would sidestep the problem entirely. RLM's trick is an optimization *within*
this constrained regime, solving a problem that agents with file-reading tools don't
have.

## The Recipe

RLM combines three ingredients:

**1. Model-driven REPL.** The LLM emits code blocks, the system executes them and
feeds output back. This repeats until the LLM emits `FINAL("answer")`.

**2. Context as a variable.** The input data is loaded as a Python variable. The LLM
can't see it directly — it writes code like `print(context[:500])` to peek at its own
input. Strange, but it keeps the context window clean for reasoning.

**3. Recursive sub-calls.** A function `recursive_llm(query, context)` spawns a fresh
LLM with its own REPL. The LLM can write map-reduce over sub-problems where each map
step is itself an LLM call.

The key move: **orchestration happens in code, not in the prompt**.

```
Naive agent:
  LLM sees chunk1 → summarizes → result stays in context
  LLM sees chunk2 → summarizes → result stays in context
  LLM sees all summaries → final answer

RLM:
  LLM writes:
    results = [recursive_llm("summarize", chunk) for chunk in chunks]
    FINAL("\n".join(results))
```

The list comprehension runs in Python. Intermediate results never enter the LLM's
context.

## How Novel Is This?

The ingredients are not new. A tool that calls an LLM — the underlying primitive — has
been available in agent frameworks for a long time. PydanticAI has supported agent
delegation (`other_agent.run(...)` inside a tool) since its early releases. Coding
agents like Cursor, Claude Code, and Devin spawn recursive sub-agents routinely.

What RLM contributes is a specific *recipe* — the right proportions of known
ingredients. The combination produces results the parts don't. But it is a usage
pattern, not a new computational primitive.

The benchmarks also flatter RLM by comparing it against an approach no programmer
would choose (all data in the prompt). In practice, "context as variable" is a
constrained version of what file-reading tools already provide.

## Limitations

- **Ephemeral code** — everything is discarded after each run; nothing accumulates.
- **Pure computation** — no side effects, no file writes, no API calls.
- **Sandbox-only trust** — the sandbox *is* the safety boundary, which limits RLMs to
  analysis tasks.

## Implementations

- **ysz/recursive-llm** — RestrictedPython sandboxing, depth limits, async support.
- **alexzhang13/rlm-minimal** — stripped-down `exec`/`eval` version, OpenAI only.
- **Shesha** — adds a document ingestion pipeline on top.

## See Also

- [RLM Implementations vs llm-do](rlm-comparison.md) — detailed comparison of the RLM
  design with llm-do's approach to evolvability, versioned code, and side effects.
