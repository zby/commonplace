---
type: reference/types/design-proposal.md
description: "Proposal: evaluate a small portfolio of structural and semantic code-navigation tools for analysis workers, allowing language-specific tools while preserving source boundaries and independent verification."
---

# Code navigation tool portfolio for analysis workers

## Problem

Analysis workers need to find implementations, follow cross-file mechanisms, and inspect controlling conditions in large external repositories. Existing search and bounded reads can perform these tasks, but locating the right source and assembling execution paths consumes work. A compact outline alone does not answer behavioral questions.

Propose evaluating a small tool portfolio rather than requiring one universal tool or building a Commonplace extractor first. Different languages may use different tools. The intended result is more useful, source-grounded analysis at reasonable total cost, not less implementation reading as an end in itself. No product, installation, interface, or mandatory reading sequence is selected here.

## Current state (as of 2026-10-11)

The [retained navigation audit](../../reports/retained/analysis-worker-code-navigation-trace-audit-2026-10-11.md) records 36 worker invocations across recent Letta Code, Graphiti, Napkin, and boundary-stopped Letta analyses. Workers searched entry points, backend selection, permissions, context construction, memory revision, and evaluation logic. Some searches approximated file outlines with declaration regexes; other searches sought conditions or prompt wording that signatures omit.

Direct code-read calls were already bounded in 96% of Letta Code calls, 93% of Graphiti calls, and 64% of Napkin calls. These are call counts, not token or efficiency measurements. Repeated reads include different ranges and independent verification; they are not established waste.

The audit's metadata-selected language census matched 197 cached repository identities, of which 189 contained recognized source files at their recorded committed HEADs. Python and TypeScript/JavaScript account for 88.1% of counted source files; adding Rust and Go brings the share to 95.5%. The corresponding rough non-test/example filter yields 86.1% and 96.1%. These are filename-extension counts, not historical reviewed-revision counts, complete semantic coverage, or worker-effort estimates. Markdown, SQL, and notebooks also occur.

The operator allows several tools, potentially one per language. No candidate has been tested on these navigation tasks. The live analysis method still governs frozen source boundaries, worker delivery, isolation, and publication. The [analysis design brief](../agentic-system-analysis-design-brief.md) prioritizes useful learning and comparison at reasonable total cost; adding tools must earn that cost.

## Candidate organization

The portfolio would supply capabilities, not prescribe a product per language:

- **Common fallback:** file discovery, exact text search, and bounded source reads remain available.
- **Structural navigation:** scoped outlines, declaration lookup, and symbol-sized implementation reads.
- **Semantic navigation where useful:** definitions, references, and implementations resolved through language-specific project analysis.
- **Other source formats:** focused reading of Markdown, configuration, SQL, and notebook code cells.

Python and TypeScript/JavaScript are the initial coverage priorities. Rust and Go extend coverage. This order does not exclude a tool with broader support or a pilot on a language where setup is cheaper or a failure is more informative. A mixed-language repository can need several routes within one worker's task.

## Options and consumption paths

A proposed change must reach workers through a specified consumer, channel, and force—the path required for an [operative change](../../notes/definitions/operative-change.md). The relevant horizon here is a worker's analysis invocation. Installed tools that only the operator's session can access do not satisfy it.

### A. Keep existing search and bounded reads

Retain the current tools and introduce no navigation service. This is the comparison baseline, and remains a valid outcome if additional tools do not earn their cost.

**Consumption:** analysts continue using their existing harness tools. No new loading path or rule is required. Existing source and verification obligations retain their force.

**Trade-off:** lowest setup and tool-description cost; workers continue locating declarations and references through text search and manual source assembly.

### B. Add structural tools, selected by language

Make scoped outlines and source-unit retrieval available through existing external tools. One tool may cover several languages, or separate tools may serve different languages. Do not require semantic project indexing for every source.

**Consumption:** a prepared worker receives the executable/tool interface and a short capability guide through its declared harness environment and job inputs. The guide advises when to use structural navigation; it does not require signatures-first reading. Direct source citation remains binding. Tool availability must be verified in the actual child worker.

**Trade-off:** potentially simpler preparation than semantic navigation; syntax alone cannot resolve every reference, registration, or runtime path. Extraction failures and omitted constructs must remain visible.

### C. Combine structural tools with language-specific semantic tools

Add semantic navigation where cross-file reference queries justify it. Permit separate tools per language, or a common agent-facing service with language-specific backends. Neither arrangement is preferred merely because it is more uniform.

**Consumption:** analysts receive the relevant tools and capability guide through the same verified worker-loading path. A setup component must select and bind each backend to the frozen source. No such component is established by this proposal; its necessity and cost are adoption questions. Navigation results advise source selection, not acceptance of behavioral claims.

**Trade-off:** potentially stronger definition/reference lookup, balanced against dependency preparation, indexing time, tool-description size, concurrency, incomplete project resolution, and backend-specific behavior.

**Candidate preference:** compare B and C against A on observed tasks. Allow different selections by language and task rather than choosing a single portfolio globally. This preference is not an adoption decision.

## Forces and boundaries

- **Evidence remains in original source.** Outlines and inferred paths locate evidence. Claims about behavior still require inspection of implementations, configuration, prompts, or tests as appropriate, cited at the pinned source boundary.
- **No repository mutation for convenience.** Tool-generated configuration, indexes, caches, and dependency/build state need an authorized location outside the frozen source, or an explicitly isolated derived copy. A tool that cannot respect the source boundary cannot be silently enabled.
- **Setup must not silently execute external code.** Dependency installation, language-server startup, build scripts, and subprocesses may need authority beyond parsing. Downloads, source upload, external embeddings, and target execution require explicit treatment in the pilot's authorization.
- **Worker isolation survives shared tooling.** A shared derived index may contain source facts at the pinned revision, not other analysts' conclusions, prior reviews, or audit findings. Independent verifiers still inspect source; a navigation shortcut must not become a shared answer.
- **Measure total cost.** Preparation, indexing, repeated startup, tool schemas, failed lookups, fallback reads, and operator work count alongside returned source volume. Shared immutable indexes may amortize setup, but mutable caches and concurrent workers need demonstrated safe behavior.
- **Unsupported means fallback, not absence.** A parse failure, unresolved reference, or excluded file must not be interpreted as evidence that a mechanism does not exist. Plain search and reading remain usable for dynamic code and non-code source.

## Evaluation and adoption criteria

A separately commissioned pilot would determine whether a portfolio reduces navigation work while preserving the conditions that make an analysis faithful. It would compare alternatives on the same pinned sources and bounded questions, with the model and task conditions recorded. The proposal does not commission that pilot or reopen historical runs.

Observed Letta Code memory-compilation and Graphiti ingestion/context paths offer grounded questions. A TypeScript-heavy large repository and a Rust or Go case would test coverage beyond the small recent trace sample. Selection should include conditions or formats where an outline or semantic reference tool can fail, not only easy declaration lookups.

Judge each option on:

- Correct identification of the active implementation and controlling conditions.
- Exact source citations and retained uncertainty when reachability is unresolved.
- Navigation calls, returned source volume, elapsed time, model usage, and preparation/operator effort, reported separately where attribution is unavailable.
- Setup failures, unresolved symbols, fallback frequency, source-boundary compliance, and verified worker access.

Comparison should use fresh workers and independently checked source answers; supplying the audit's answers would contaminate the navigation test. Deterministic counters warrant claims about measured volume or timing only. Human or independent source review would judge behavioral fidelity, with contested findings retained. Existing analysis acceptance is not by itself proof that no mechanism was missed. No new automated truth oracle or numerical success threshold is proposed.

Adoption would require a demonstrated net benefit on the selected tasks without materially weaker conclusions, worker isolation, or source integrity; reproducible setup for the intended languages and harnesses; and an explicit maintainer choice of the supported routes and their costs. A benefit limited to one language or operation warrants narrow adoption, not a universal signatures-first rule.

If selected, implementation would follow the [analysis method-maintenance instruction](../../agentic-system-analyses/instructions/maintain-analysis-method.md), updating affected consumers at a committed method revision before new runs. Tool installation and workflow changes remain separately authorized work.

## Choices left open

- Which existing products supply each capability, and whether any genuine gap warrants custom code.
- Whether language-specific tools are exposed directly or through a common service.
- Which capabilities are always available and which justify on-demand preparation.
- Whether setup is per worker, per run, or shared through immutable source-derived state.
- Which language/task pairs earn adoption, and how much preparation cost operators will accept.

The decision can be to retain the baseline, adopt structural navigation only, or adopt a mixed portfolio. The evidence does not yet discriminate among them.
