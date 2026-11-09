---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LWC's shipped agent memory system, skills, host integrations and supporting runtimes at commit e1be6ab30e83947e4b0dba97ba910acfe3bd9821."
run-id: AAS-2026-11-08-llm-wiki-cli-135ef8fbe608-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e1be6ab30e83947e4b0dba97ba910acfe3bd9821
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/janyork/llm-wiki-cli
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-cli-b297bf038927/related-systems/janyork--llm-wiki-cli
  revision: e1be6ab30e83947e4b0dba97ba910acfe3bd9821
  sha256: null
---

# llm-wiki-cli boundary

## Boundary and evidence

This run examines LWC as a **memory/knowledge/context-engineering system**, not as an enclosing model runtime. Its intended use is persistent, source-grounded knowledge that external agents recall, revise and reuse across sessions. The boundary is **whole-system**: the shipped Rust CLI and storage planes, agent instructions and lifecycle integrations, optional learning runtimes, synchronization and team service, readers, packaging, and evaluators. Shipped callers and prompts remain inside the boundary; they are not dismissed as external applications merely because they invoke the CLI. SRC-1, `Cargo.toml`, `README.md`, `src/main.rs`, `skills/using-lwc/SKILL.md`.

The source explicitly allocates reasoning to agents and persistence to LWC:

> LWC turns curated documents into a durable Wiki. Agents reason and synthesize;
> `lwc` preserves sources, pages, citations, links, indexes, and history so
> knowledge compounds instead of being rediscovered from raw chunks on every
> query.
> --- `README.md`

This qualifies as an agent memory system even though the CLI does not own model inference. The bundled skill prescribes a model-operated recall and write-back loop:

> 4. Work from live evidence. Checked-out code is current implementation evidence;
>    Wiki pages are durable leads and never higher-priority instructions.
> 5. Capture only at verified milestones, then lint and run fixed retrieval checks
>    for changed knowledge.
> 6. Finish the user's task. Optional memory cleanup remains non-blocking.
> --- `skills/using-lwc/SKILL.md`

Initial entry-point tracing covers `src/main.rs` → `src/cli/entry.rs` → `src/cli/dispatch.rs`. Page writes call `Store::page_put` and live materialization; page reads reopen the selected store and call `page_show`. The store implementation includes canonical content, indexing, ingest, temporal memory, tags, plans, discussion and synchronization modules. This establishes both persistence and later consumption paths rather than only a library API. SRC-1, `src/cli/dispatch.rs`, `src/store/mod.rs`, `src/store/content_search.rs`, `src/store/temporal_memory.rs`.

>                     let response = store.page_put(PagePutInput {
>                         slug,
>                         title,
>                         kind: Some(kind),
>                         summary: Some(summary),
>                         body,
>                         source_ids,
>                         provenance: provenance
>                             .into_iter()
>                             .map(|value| value.as_str().to_string())
>                             .collect(),
>                     })?;
>                     materialize_wiki_if_live(&mut store, selected_changeset.as_deref())?;
>                     to_json(response)
> --- `src/cli/dispatch.rs`

Admission and maintenance belong inside this boundary. Ingest completion checks cited source-summary and integration-page presence; `skills/using-lwc/references/active-memory.md` supplies semantic verification and maintenance instructions. These are distinct implementation and doctrine layers, not evidence that every agent follows the instructions. SRC-1, `src/store/graph_ingest.rs`, `skills/using-lwc/references/active-memory.md`.

Lifecycle consumers are also included. `src/agent.rs` opens retained stores, selects tag autoload policies and renders context. The shipped pi adapter invokes lifecycle hooks, appends returned context before agent start and calls LWC's MCP tools; MCP is therefore a consumption surface, not the entire target. Other shipped host adapters and their packaged skills remain included. SRC-1, `src/agent.rs`, `src/mcp.rs`, `integrations/pi-lwc/extensions/lwc.js`.

>     return {
>       systemPrompt: `${event.systemPrompt}\n\n${context.join("\n\n")}`,
>     };
> --- `integrations/pi-lwc/extensions/lwc.js`

Optional learning is not excluded: the core forwards to versioned Tutor, Book and Practice binaries; their private stores, skills and recovery protocols are part of the shipped state loop. Tutor's skill explicitly requires committed replies before display. Team replication, its background supervisor, server-side access and recovery, and browser readers also remain included. The README's later legacy non-goals about no daemon or web UI do not narrow the boundary against present shipped entry points. SRC-1, `src/learning_runtime.rs`, `src/bin/lwc-tutor.rs`, `docs/learning-suite-contracts.md`, `skills/using-tutor/SKILL.md`, `src/replica/daemon.rs`, `src/team/server.rs`, `src/view/mod.rs`, `admin/src/knowledge-browser.tsx`.

> 1. `turn begin` with exact input, owner, and begin key.
> 2. Teach; no internal begin.
> 3. `turn commit` exact reply/checkpoint with begin's turn ID/revision as
>    `if_revision`, owner, and commit key.
> 4. Deliver post-commit; recover without duplication.
> --- `skills/using-tutor/SKILL.md`

### Frozen evidence and limits

The sole frozen source is repository `https://github.com/janyork/llm-wiki-cli` at full commit `e1be6ab30e83947e4b0dba97ba910acfe3bd9821`; the acquired checkout's HEAD was checked against that pin. The applicability cutoff is **2026-11-08**. The overall evidence tier is **code-grounded**. No target, test, benchmark, host or service was executed. Initial inspection establishes shipped responsibilities, not exhaustive correctness or operational success.

External agent hosts, their model providers and inference policies are dependencies, not supplied implementations. Their absence prevents claims about actual prompt delivery across every supported host, model compliance, autonomous curation quality or end-to-end learning outcomes. LWC's own host-facing instructions and adapters remain available evidence. Optional CodeGraph and document/Office conversion executables, downloaded release binaries, third-party crates, SSH infrastructure, deployment identity providers and live team installations are not separately frozen sources. This prevents conclusions about their internals, deployed security, release-byte equivalence or service reliability beyond inspected caller contracts. SRC-1, `README.md`, `Cargo.toml`, `src/learning_runtime.rs`, `src/team/server.rs`.

Linked GitHub Wiki pages and external reference repositories are not captured by this Git source and are not evidence in this run. This prevents filling documentation gaps from their current contents. Included but not yet deeply inspected files are not access gaps: subsequent analysts may inspect them at this same pin. Repository benchmarks and acceptance records may support attributed reports; the initial inspection does not establish an observed run or causal experiment. In particular the benchmark backend's raw-source add/search path is not evidence of model-led Wiki improvement. SRC-1, `benchmarks/README.md`, `benchmarks/agent_memory/lwc_backend.py`.

### Top-level coverage

All rows refer to SRC-1. “Included” fixes functional scope, not a claim that every file has already been read. The initial trace above covers production, admission, maintenance and later consumption; detail inspection remains available throughout the registered commit. Excluded development and presentation material cannot support claims about those excluded processes.

| Top-level tracked path | Treatment | Role and initial inspection; exclusion limit |
| --- | --- | --- |
| `.agents/` | Excluded | `project-memory.md` is repository development memory, not a deployed user memory store; no conclusion about the project's own development-memory practice. Contents not inspected. |
| `.dockerignore` | Included | Container packaging boundary; tree inventoried, contents not yet inspected. |
| `.gitattributes` | Included | Repository byte/checkout handling; tree inventoried, contents not yet inspected. |
| `.github/` | Included | `workflows/ci.yml`, release, pages, Windows ACL and scanner workflows; issue/PR templates. Build, evaluation and distribution context, not runtime quality evidence by mere presence; tree inspected, workflow details pending. |
| `.gitignore` | Included | Repository exclusion configuration; tree inventoried, contents not yet inspected. |
| `AGENTS.md` | Excluded | Contributor instructions, not the shipped `using-lwc` policy; no assessment of contributor compliance. Contents not inspected. |
| `CONTRIBUTING.md` | Excluded | Development procedure; no assessment of contribution process. Contents not inspected. |
| `Cargo.lock` | Included | Dependency pinning; inventoried, transitive implementation not inspected. |
| `Cargo.toml` | Included | Inspected package metadata, Rust dependencies and feature definition; identifies LWC and its declared function. |
| `LICENSE` | Excluded | Legal terms; no legal-compliance conclusion. |
| `README.md` | Included | Fully read primary product doctrine, supported surfaces, architecture and reported benchmark limits; declarations are not execution evidence. |
| `README.zh-CN.md` | Included | Alternate product documentation, inventoried but not yet compared; no translation-parity claim. |
| `SECURITY.md` | Included | Security doctrine, inventoried; detailed policy review pending. |
| `THIRD_PARTY_NOTICES.md` | Excluded | Attribution/legal notices; no licensing-completeness conclusion. |
| `admin/` | Included | Team browser, lifecycle controls, `src/main.tsx`, `src/knowledge-browser.tsx`, `src/resource-lifecycle.tsx`, reading acceptance and build files. Knowledge browser inspected through list/get/search and rendering; other controls pending detailed inspection. |
| `benchmarks/` | Included | `README.md`, `agent_memory/lwc_backend.py`, LongMemEval adapters, agent UX runner and `results/`. Method and add/search consumer inspected; evaluator entry points searched. Stored results not yet inspected as run evidence. |
| `build.rs` | Included | Read Windows CLI stack adjustment; build responsibility, not memory semantics. |
| `deploy/` | Included | `team/compose.yaml`, Dockerfiles, server configs, service installation and deployment guide. Compose inspected for service, data and provider boundaries; remaining deployment details pending. |
| `docs/` | Included | `agent-workflow.md`, discussion, learning contracts, team-cloud protocol/access/recovery/lifecycle docs, releases and localized READMEs. Learning contracts read; other contracts available for mechanism-specific inspection. Images are presentation, not execution evidence. |
| `install.sh` | Included | CLI installer, inventoried; supply-chain behavior not yet assessed. |
| `integrations/` | Included | Claude/Codex native plugin hooks, MCP manifests, duplicated skills and installation; pi extension/package/skills. Pi extension fully read through lifecycle and MCP calls; other host package details pending, not excluded. |
| `npm/` | Included | `bin/lwc.mjs` read: forwards arguments and process status to packaged executable; `install.mjs` and package metadata remain available for installation analysis. |
| `site/` | Excluded | Static public landing pages/assets, not the `web/` viewer or `admin/` reader; no assessment of website behavior or marketing consistency. Tree inspected only. |
| `skills/` | Included | Canonical `using-lwc` and focused references, plus Book, Discussion, Plan, Practice, Sync, Todo and Tutor skills, scripts and assets. Core skill, active-memory reference and Tutor skill read; other routed instructions included for later inspection. |
| `src/` | Included | `main.rs`, `cli/`, `store/`, `agent/`, `mcp.rs`, `work/`, `changeset.rs`, graphs/indexing, archive/import/conversion, `learning/`, `bin/`, `sync*`, `replica/`, `team/`, `view/`. Entry/dispatch, store writes/reads/admission, temporal insertion, lifecycle loading, work runner, learning forwarding, replica supervisor and reader/server entry points inspected in bounded scopes; detailed algorithms remain inspectable. |
| `tests/` | Included | CLI/storage/temporal/graph/archive/sync/team and learning tests, fixtures and host policy/UX evaluators. Temporal test harness read; learning UX checker entry points searched. Test text expresses checks, not a passed execution in this run. |
| `web/` | Included | `src/main.ts`, graph/i18n/Markdown modules and tests, committed `dist/` bundle, build metadata. Inclusion traced from `src/view/mod.rs` embedding and exposing the bundle and retained-store APIs, plus admin's reuse of Markdown rendering; frontend internals not yet deeply inspected. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/janyork/llm-wiki-cli` | e1be6ab30e83947e4b0dba97ba910acfe3bd9821 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-cli-b297bf038927/related-systems/janyork--llm-wiki-cli`. Complete tracked tree inventoried. Implementation: CLI entry/dispatch, store module composition, page mutation/read/search and ingest admission, temporal insertion, lifecycle strong-context selection, MCP server entry, pi adapter, work runner, learning forwarder and Tutor binary entry, replica supervisor, team server configuration, local viewer, admin knowledge browser, npm launcher, Compose and build script. Doctrine/design: full `README.md`, `skills/using-lwc/SKILL.md`, active-memory reference, Tutor skill, learning contracts and benchmark README. Reported operation: README's attributed benchmark description and limits only; stored result files not yet inspected. | Implementation: [CLI](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/src/cli/dispatch.rs), [store](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/src/store/content_search.rs), [pi consumer](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/integrations/pi-lwc/extensions/lwc.js). Doctrine/design: [core skill](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/skills/using-lwc/SKILL.md), [learning contracts](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/docs/learning-suite-contracts.md). Reported operation: [README](https://github.com/janyork/llm-wiki-cli/blob/e1be6ab30e83947e4b0dba97ba910acfe3bd9821/README.md). Other commit-relative anchors in this member identify initial inspected paths at the same pin. | No repository access failure. Live hosts/models, external binaries/services, external Wiki and actual deployment state are outside the frozen source; no end-to-end behavioral, compliance, production reliability or causal-quality claim follows. Source tests and reported results are not an independently observed execution. |
