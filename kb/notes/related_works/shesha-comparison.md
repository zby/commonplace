# Shesha vs llm-do

## Context

Shesha (`github.com/ovid/shesha`, v0.5.0) implements Recursive Language Models for
document querying — the LLM writes and executes Python code in a Docker sandbox to
explore document collections, iterating until it produces a cited answer. We compare
it with llm-do to understand overlaps, complementary strengths, and what each project
could learn from the other.

## Different Starting Points

**Shesha** starts from a specific problem: querying large document collections (including
entire codebases) with accurate citations. Its solution: let the LLM write Python that
searches, filters, and analyzes a pre-ingested corpus, iterating in a sandboxed REPL
until it calls `FINAL(answer)`.

**llm-do** starts from a different insight: **stabilizing**. The core idea is that LLM
applications evolve by progressively converting stochastic behavior into deterministic
code, and vice versa. The system breathes between neural and symbolic computation —
agents and tools share a unified calling convention, and logic can migrate between
prompts and code without changing call sites.

## Findings

### Shesha snapshot
- Repo: `github.com/ovid/shesha` (v0.5.0, MIT, author: Curtis "Ovid" Poe)
- Python 3.11+, 49 source files
- Core dependencies: `litellm`, `docker`, `pdfplumber`, `python-docx`, `beautifulsoup4`

### Shesha's key design decisions

- **REPL+LLM loop.** The LLM generates Python code (```repl``` blocks), which executes
  in a Docker container with persistent namespace. Output is fed back; the loop repeats
  until `FINAL(answer)` is called or `max_iterations` (default 20) is reached.
- **Docker sandbox with defense-in-depth.** Containers run with no network, no root,
  512 MB memory, read-only filesystem, all capabilities dropped, 30s execution timeout.
  Output wrapped in `<repl_output type="untrusted_document_content">` tags to mitigate
  prompt injection.
- **Document ingestion pipeline.** Pluggable parsers for PDF, DOCX, HTML, code (with
  line-number tracking), Markdown, CSV, text. Filesystem-based storage with metadata.
- **Git repository ingestion.** Supports GitHub, GitLab, Bitbucket, and local repos.
  Shallow cloning, SHA-based change detection, token-based auth.
- **Sub-LLM calls.** The sandbox exposes `llm_query(instruction, content)` for analyzing
  large content chunks — analogous to recursive-llm's `recursive_llm()` but single-depth.
- **Citation verification.** Post-answer pass verifies that cited passages actually exist
  in the corpus. Semantic verification with adversarial review (v0.5.0).
- **Execution traces.** Step-by-step recording of LLM reasoning, code, and output —
  written incrementally for real-time monitoring.
- **LiteLLM for model access.** Unified proxy to 100+ providers with automatic
  retry/backoff, rather than direct provider SDKs.
- **Programmatic API.** `Shesha().create_project("name").query("question")` — no CLI
  framework, no manifest files, no agent definitions.

### Purity, side effects, and the approval problem

All three RLM implementations (rlm-minimal, recursive-llm, Shesha) concentrate on
**pure computation** — the LLM-generated code reads data and produces answers but
causes no side effects. Shesha enforces this with Docker (read-only filesystem, no
network, all capabilities dropped); rlm-minimal uses RestrictedPython; recursive-llm
uses a permissive builtins whitelist. The only "mutation" in Shesha's sandbox is the
in-memory `context` list, which doesn't persist beyond the query.

This purity is what makes the approval problem disappear for RLM systems: **if code
can't cause side effects, there's nothing to approve.** The Docker container *is* the
approval policy — containment replaces consent.

llm-do operates in a fundamentally different regime. Its agents do real work — file
writes, shell commands, API calls — so it needs approval gates at the trust boundary.
The planned [Monty](https://github.com/pydantic/monty) integration (PydanticAI's
sandboxed code execution) bridges this gap: pure computation runs in a sandbox with
no approvals needed, while side-effectful tools remain gated by the approval system.
This gives llm-do both modes:

- **Pure sandbox** (Monty): LLM-generated code for computation/analysis, no approvals
- **Side-effectful tools**: developer-written tools for real work, approval-gated

The RLM approach (Shesha included) only needs the first mode. llm-do needs both.

### Architecture comparison

| Aspect | Shesha | llm-do |
|--------|--------|--------|
| **Core insight** | LLM can explore documents by writing code | Stabilize stochastic ↔ deterministic |
| **Execution model** | REPL+LLM loop (model writes code, sandbox executes) | PydanticAI agent loop (model calls tools via schemas) |
| **Who writes code?** | The LLM writes all code; developers write nothing | Developers write tools; LLM orchestrates (bootstrapping planned: LLM generates tools too) |
| **Code lifespan** | Ephemeral — generated per query, then discarded | Permanent — tools are versioned infrastructure (bootstrapping: LLM-generated code becomes permanent) |
| **Sandbox** | Docker containers (no network, no root, memory limits) | No sandbox; approval gates at tool boundaries |
| **LLM backend** | LiteLLM (100+ providers via proxy) | PydanticAI (direct provider SDKs) |
| **Multi-agent** | Single agent + sub-LLM calls | First-class — agents call agents, depth-tracked |
| **Configuration** | Python API + optional YAML config | JSON manifest + YAML `.agent` files |
| **Document handling** | Built-in ingestion pipeline (PDF, DOCX, HTML, code) | None built-in |
| **Trust boundary** | Container isolation | Approval callbacks per tool |
| **UI** | None (library) | Textual TUI with interactive approval |
| **Tracing** | Execution traces with step-by-step replay | JSONL message logging |

### What Shesha has that llm-do lacks

- **Document ingestion pipeline** — PDF, DOCX, HTML, code parsers with line-number tracking
- **Git repository ingestion** — clone, parse, SHA-based change detection
- **Sandboxed code execution** — hardened Docker containers with defense-in-depth
  (llm-do plans to add sandboxing via [Monty](https://github.com/pydantic/monty),
  PydanticAI's sandboxed code execution environment)
- **Citation verification** — post-answer verification that cited passages exist in corpus
- **Execution traces** — structured step-by-step replay of reasoning/code/output
- **Prompt injection mitigations** — untrusted content tagging, instruction/content separation

### What llm-do has that Shesha lacks

- **Multi-agent orchestration** — agents calling agents with depth limits and call tracking
- **Progressive stabilization** — migrate logic between prompts and deterministic code
- **Approval/gating system** — fine-grained security for dangerous operations
- **Declarative agent definitions** — `.agent` files with YAML frontmatter
- **Toolset abstraction** — reusable, composable tool bundles (filesystem, shell, dynamic agents)
- **TUI with interactive approval** — Textual-based UI for human-in-the-loop workflows
- **Unified calling convention** — agents and tools are interchangeable callables
- **Bootstrapping** (planned) — LLM generates code that becomes permanent tools,
  closing the loop with stabilization: ephemeral LLM-generated code → tested tool →
  versioned infrastructure

## Open Questions

- llm-do plans to use [Monty](https://github.com/pydantic/monty) (PydanticAI's sandboxed
  code execution) for safe code execution. How does Monty compare to Shesha's custom
  Docker sandbox? Shesha's approach is more battle-tested (defense-in-depth, prompt
  injection tagging, container pooling), but Monty integrates natively with PydanticAI.
- Is Shesha's document ingestion pipeline useful as a standalone toolset, or would llm-do
  projects handle ingestion outside the framework?
- Shesha's LiteLLM integration vs llm-do's PydanticAI — is there value in supporting
  both, or does PydanticAI's direct SDK approach remain preferable?

## Conclusion

Shesha and llm-do share the intuition that LLMs benefit from code execution during
reasoning, but they apply it at different levels:

- **Shesha is a vertical product** — a document Q&A system where code execution is the
  reasoning mechanism. The LLM is a researcher that writes throwaway scripts to explore
  a corpus. Strong on safety (Docker sandbox), document handling (parsers + citations),
  and self-contained deployment.

- **llm-do is a horizontal framework** — a runtime for composing agents and tools where
  the neural/symbolic boundary is fluid. Strong on composition (multi-agent, toolsets),
  evolution (stabilize/soften), and developer ergonomics (`.agent` files, approval gates,
  TUI).

The key differentiator remains the same as with other RLM implementations: llm-do's
refactoring is **seamless across the stochastic-deterministic boundary**. Shesha's LLM
writes code that is discarded after each query; llm-do's tools are permanent
infrastructure that can be promoted from or demoted to LLM behavior. Planned
**bootstrapping** sharpens this contrast further: where Shesha's generated code is
ephemeral by design, llm-do will let the LLM generate code that *graduates* into
permanent tools — the LLM becomes a contributor to the codebase, not just a runtime
reasoning engine. The two approaches are complementary — Shesha's sandbox + ingestion
could serve as a toolset within llm-do's orchestration model.
