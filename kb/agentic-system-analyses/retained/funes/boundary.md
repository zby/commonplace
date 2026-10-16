---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Funes's shipped Librarian instructions, library scaffold and supporting tools at commit 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/ulyssestenn/funes
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-funes/related-systems/ulyssestenn--funes
  revision: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
  sha256: null
---

# Funes boundary

## Boundary and evidence

Funes is in scope as a memory/knowledge/context-engineering system. Its intended use is an LLM-maintained, cited Markdown library: preserve raw sources, compile source notes and concepts, organize topic maps, answer questions from retained content, and maintain that content. It ships instructions for an externally supplied agent rather than an enclosing model runtime. SRC-1, `README.md`, `AGENTS.md`, `protocol.md`.

> **No application stack required.** Funes needs no server, vector database, embedding pipeline, or proprietary runtime. It is a repository structure, an operating protocol, and optional maintenance and extraction tools.
> --- `README.md`

The whole-system boundary includes the repository's agent entry points, all shared operating and setup instructions, every starter-library scaffold file, extraction helpers, mechanical evaluators and their CI caller. The instruction-mediated state loop is part of the target, not an excluded application. The root `AGENTS.md` directs the agent to the library-specific `AGENTS.md` and shared `protocol.md`; those instructions assign raw persistence, compilation, index and changelog updates, later wiki consumption, output persistence and proposed filing-back. There is no shipped model-call driver in the inspected tree. SRC-1, `AGENTS.md`, `starter-library/AGENTS.md`, `protocol.md`, `library.md`, `tools/README.md`.

> **Q&A:** search the wiki first (INDEX → sources → concepts); answer with
> relative-link citations; say so plainly if it isn't covered. Write substantial
> outputs to `outputs/` and offer to file durable parts back in.
> --- `protocol.md`

> - Close the loop each session: update `INDEX.md` files + `meta/CHANGELOG.md`.
> --- `protocol.md`

The boundary is commit `3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11`, verified against the acquired checkout's HEAD. The applicability cutoff is 2026-10-15; later revisions and external linked material are not evidence. The overall evidence tier is code-grounded because the supporting executable paths and their shipped caller were inspected. The semantic Librarian workflow is doctrine/design evidence, not demonstrated enforcement or an observed run. The starter library is empty, and no target code, examples or tests were executed. SRC-1, `starter-library/README.md`, `starter-library/wiki/INDEX.md`, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`.

### Shipped-path coverage

All top-level tracked entries are accounted for below. Included directories name the material paths inspected; no material shipped path remains uninspected.

| Top-level entry | Classification and inspected material paths | Role and evidence limit |
|---|---|---|
| `.github/` | Included: `.github/workflows/funes-lint.yml` | Shipped CI consumer invokes Python syntax checking, link/orphan/frontmatter audit and compile-depth lint. Workflow text establishes configuration, not successful CI execution. SRC-1. |
| `AGENTS.md` | Included: read in full | Root agent entry point routes to library instructions, protocol, setup recipe and helpers. Instruction loading by an external host is not verified. SRC-1. |
| `LICENSE` | Deliberately excluded; available but not inspected | Legal terms, not a state-loop path. No legal or licensing conclusion is established. |
| `README.md` | Included: read in full | Declared purpose, host onboarding, workflow and example artifact shapes. Examples are documentation, not run evidence. SRC-1. |
| `library.md` | Included: read in full | Library creation, convention confirmation, scaffold, agent instructions, index seeds and commit/push instructions. No actual provisioning run is established. SRC-1. |
| `protocol.md` | Included: read in full | Shipped Librarian prompt governs ingest, compilation, retrieval, output, maintenance, citations, cross-library approval and session closure. Instructions do not demonstrate agent compliance. SRC-1. |
| `starter-library/` | Included: `starter-library/AGENTS.md`, `starter-library/README.md`, `starter-library/raw/INDEX.md`, `starter-library/raw/assets/README.md`, `starter-library/wiki/INDEX.md`, `starter-library/wiki/sources/README.md`, `starter-library/wiki/concepts/README.md`, `starter-library/wiki/topics/README.md`, `starter-library/outputs/README.md`, `starter-library/meta/CHANGELOG.md`, `starter-library/meta/health/README.md`; all read in full | Reference state layout and local prompt routing; registry, navigation, raw assets, compiled layers, outputs and maintenance records. These are empty scaffolds, not a populated library or evidence of later retrieval quality. SRC-1. |
| `tools/` | Included: `tools/README.md`, `tools/check_links.py`, `tools/compile_lint.py`, `tools/pdf_text.py`, `tools/youtube_transcript.py`, `tools/requirements-youtube.txt`; all read in full | Deterministic link and compile evaluators; PDF sidecar production; targeted caption retrieval and dependency declaration. CLI entry points were traced through file reads, subprocess/API calls, output writes and exit behavior; protocol and CI consumers were inspected. Source inspection does not establish extraction accuracy, semantic grounding or successful network operation. SRC-1. |

### Dependencies and exclusions

The caller supplies a file-reading/editing LLM agent and model provider. Their scheduling, context limits, authorization and instruction-loading behavior are outside this repository boundary; no enclosing-runtime guarantees are attributed to Funes. Git and GitHub provide repository/versioning and CI infrastructure, not Funes-owned orchestration. SRC-1, `README.md`, `library.md`, `.github/workflows/funes-lint.yml`.

The PDF helper depends on external Poppler commands and Tesseract; the caption helper depends on `youtube-transcript-api>=1.2.4,<2` and YouTube access. Those implementations and services were not acquired. This prevents conclusions about their correctness, availability and extraction fidelity; the wrappers' declared and implemented handling remains included. SRC-1, `tools/pdf_text.py`, `tools/youtube_transcript.py`, `tools/requirements-youtube.txt`, `tools/README.md`.

The linked example-library repository, inspirational posts and videos, and user-created libraries are deliberately outside the single acquired source. This prevents conclusions about populated-library performance, real maintenance outcomes and generality across domains. No required source file was inaccessible. The absence of supplied execution evidence prevents claims of observed agent adherence, retrieval quality or causal improvement. A historical compile failure described in the linter's own docstring is attributed reported operation only, not an independently inspectable experiment. SRC-1, `README.md`, `starter-library/README.md`, `tools/compile_lint.py`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ulyssestenn/funes` | 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-funes/related-systems/ulyssestenn--funes`. Implementation: complete reads of all four Python helpers, optional requirements and CI workflow. Doctrine/design: complete reads of root `README.md`, `AGENTS.md`, `library.md`, `protocol.md`, `tools/README.md` and every tracked starter-library file listed in coverage. Reported operation: historical shallow-compilation account in `tools/compile_lint.py` docstring. Tracked tree inspected; LICENSE deliberately excluded. | Implementation: [link audit](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/tools/check_links.py), [compile audit and historical account](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/tools/compile_lint.py), [PDF helper](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/tools/pdf_text.py), [caption helper](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/tools/youtube_transcript.py), [CI caller](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/.github/workflows/funes-lint.yml). Doctrine/design: [root entry](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/AGENTS.md), [protocol](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/protocol.md), [setup](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/library.md), [local entry](https://github.com/ulyssestenn/funes/blob/3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11/starter-library/AGENTS.md). | No source access gap within the shipped functional loop. External host, providers, extraction dependencies, linked repositories and services are not frozen here. No observed run or causal experiment supplied; code supports wrapper/evaluator behavior, instructions support intended workflow, and the historical account supports only attributed reporting. Empty scaffolds cannot establish operational efficacy. |
