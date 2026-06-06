# Agent-runtime review targets

Candidate runtimes to review once topology and grain are settled (see [README.md](./README.md)). A target here is registered, not yet scheduled — the review type/skill and collection are still open decisions.

## Queue

### 1. flue — `withastro/flue`
- **Repo:** https://github.com/withastro/flue
- **Self-description:** "The sandbox agent framework."
- **Language:** TypeScript
- **Why a runtime, not a memory system:** describes itself as an agent *framework* built around a sandbox — i.e. the execution-substrate + scheduler layers, with memory (if any) as a subsystem. Good first probe of whether the Scheduler / Context-engine / Execution-substrate skeleton holds against a real runtime.
- **Status:** registered (first target). Not yet reviewed.
- **Captured:** 2026-06-06

### 2. cocoindex — `cocoindex-io/cocoindex`
- **Repo:** https://github.com/cocoindex-io/cocoindex
- **Self-description:** "Incremental engine for long horizon agents."
- **Language:** Rust (Python bindings)
- **Topics:** `context-engineering`, `indexing`, `rag`, `data-indexing`, `change-data-capture`, `knowledge-graph`, `semantic-search`, `long-horizon-agent`, `agentic-data-framework`
- **Boundary flag:** likely a **Context-engine / Execution-substrate subsystem** (incremental indexing, CDC, RAG pipeline) rather than a full scheduler-bearing runtime — it feeds context in, it doesn't run the loop. Good test of the grain/boundary decision: does a runtime *subsystem* get its own review, slot into a runtime review, or sit closer to the existing memory corpus? Contrast with flue, which is execution-substrate + scheduler.
- **Status:** registered. Not yet reviewed.
- **Captured:** 2026-06-06
