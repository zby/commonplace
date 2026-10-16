---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Kompl's shipped knowledge-compilation, maintenance and consumption system at commit 17970c969b0c2576bf722840e0e2db3c6416a7aa."
run-id: AAS-2026-10-14-kompl-9cffb1e5eb86-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/tuirk/Kompl
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/kompl-9cffb1e5eb86/related-systems/tuirk--Kompl
  revision: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
  sha256: null
---

# Kompl boundary

## Boundary and evidence

This run examines Kompl as a knowledge system that compiles incoming sources into retained wiki pages and serves those pages to people and agents. The intended use is to establish its source-native operation, including how knowledge is produced, admitted, persisted, maintained and consumed. It does not evaluate Commonplace adoption.

The target class is **memory/knowledge/context-engineering system**, not an enclosing general-purpose agent runtime. Kompl issues model calls for extraction, drafting and query answering, while its shipped MCP server serves retained pages to an external agent. The boundary kind is **whole-system**: the target includes the Next.js application and its state-owning callers, Python NLP/model/storage service, shipped n8n workflow, CLI startup maintenance, operator instructions and evaluation paths. The built-in chat is included even though the README calls it replaceable. It consumes retained content and can produce another draft. SRC-1: `README.md`, `app/src/app/api/chat/route.ts`, `mcp-server/index.ts`.

> The agent answers questions; Kompl stores and serves the
> compiled pages.
> --- `README.md`

The initial trace establishes a complete shipped loop rather than only a library API:

- **Produce and update:** onboarding staging and finalization lead through the shipped n8n webhook to the application's compile driver. That driver dispatches ingestion, extraction, resolution, matching, planning, drafting, cross-reference, commit and schema steps. Existing pages and the retained schema are loaded into later drafting calls. SRC-1: `app/src/app/api/onboarding/stage/route.ts`, `app/src/app/api/onboarding/finalize/route.ts`, `n8n/workflows/session-compile.json`, `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/draft/route.ts`, `nlp-service/routers/pipeline.py`.
- **Admit and persist:** compile commit includes automatic/manual approval paths; explicit draft approval uses a shared commit implementation. Database outbox content is flushed through the Python storage service, and startup instrumentation reattempts pending flushes. These are included responsibilities, not external host behavior. SRC-1: `app/src/app/api/compile/commit/route.ts`, `app/src/lib/approve-plan.ts`, `app/src/lib/flush-pending.ts`, `app/instrumentation.ts`, `nlp-service/services/file_store.py`.
- **Maintain and reload:** source deletion/recompilation, wiki lint, import/export, vector maintenance and schema migrations are in scope. The CLI invokes startup lint and backup against the application API. SRC-1: `app/src/lib/source-delete.ts`, `app/src/lib/recompile.ts`, `app/src/app/api/sources/[source_id]/recompile/route.ts`, `app/src/app/api/wiki/lint-pass/route.ts`, `app/src/app/api/import/route.ts`, `app/src/app/api/export/route.ts`, `cli/src/startup-tasks.ts`, `scripts/migrate.py`.
- **Consume and feed back:** the wiki reads retained markdown; MCP calls the wiki's HTTP API; built-in chat retrieves retained pages, calls answer synthesis, persists conversation history and may create a pending query-generated draft. SRC-1: `app/src/app/wiki/[page_id]/page.tsx`, `app/src/app/api/wiki/[page_id]/data/route.ts`, `app/src/lib/retrieval.ts`, `app/src/app/api/chat/route.ts`, `mcp-server/index.ts`.

The following implementation excerpts anchor the classification and inclusion of both later update and query-feedback paths. They establish shipped code, not successful execution or answer fidelity.

> if existing_content:
>         parts += ["Existing page content (update this, don't rewrite from scratch):",
>                   existing_content, ""]
> --- `nlp-service/services/llm_client.py`

> // 7. Compounding: if answer used 3+ pages, create a pending draft
>     if (pages.length >= 3) {
> --- `app/src/app/api/chat/route.ts`

### Frozen evidence and limits

The only source is SRC-1, the acquired repository at full commit `17970c969b0c2576bf722840e0e2db3c6416a7aa`. Its checkout HEAD was checked against that pin. The analysis cutoff is **2026-10-14**, the supplied run date; this is not a claim that the source's last commit occurred on that date. Later commits, live issues, linked but untracked documents and other repositories do not supply evidence. The evidence tier is **code-grounded**.

External dependencies include Docker/Compose, n8n's upstream runtime, Node/Next.js, FastAPI and local NLP/vector libraries and models, Gemini/DeepSeek provider services, and ingestion services such as Firecrawl and YouTube. Their Kompl-facing calls and configuration belong to the target; their independent internals do not. External MCP clients' scheduling, context assembly, decisions and memory writes are excluded, preventing attribution of an enclosing agent loop to Kompl. SRC-1: `docker-compose.yml`, `README.md`, `nlp-service/routers/pipeline.py`, `mcp-server/index.ts`.

No target code, tests, examples or model calls were executed. This prevents claims of observed correctness, crash recovery, security or sustained compounding at this revision. The repository's May provider-validation reports are attributed historical evidence, not fresh tests of the reviewed commit. The May 22 Flash report still marks its results pending. The corpus referenced by the validation runners, `nlp-service/test_corpus/`, is absent from the tracked tree; that access gap prevents reproducing or inspecting those exact input texts within this boundary. Initial inspection of evaluator entry points does not establish causal comparisons or semantic accuracy. SRC-1: `validation/2026-05-05-multi-provider-corpus/REPORT.md`, `validation/2026-05-05-multi-provider-corpus/runner.py`, `validation/2026-05-22-deepseek-flash/REPORT.md`.

### Top-level coverage

All top-level tracked entries are classified below. Included means part of the functional target, not fully audited. “Tree/search” identifies initial bounded inspection; available files not yet read in full remain available to later analysts under SRC-1 and are not access gaps. Deliberate exclusions are peripheral to the knowledge loop.

| Tracked entry | Boundary treatment | Material paths, role and initial inspection | Exclusion or inspection limit |
|---|---|---|---|
| `.dockerignore` | Included | Image-build input filtering; tree inspected | Contents not yet inspected; no build-reproducibility claim |
| `.env.example` | Included | Operator/service configuration; tree inspected alongside Compose configuration | Template contents not yet inspected |
| `.gitattributes` | Excluded | Git file-handling policy; tree inspected | No assessment of checkout normalization |
| `.github/` | Included | `workflows/integration-test.yml` evaluator wiring searched; `scorecard.yml`, dependency updates and contribution templates inventoried | Remaining automation not yet inspected; no CI success or security-score claim |
| `.gitignore` | Excluded | Git tracking policy; tree inspected | No assessment of secret exclusion or untracked local artifacts |
| `AGENTS.md` | Included | Complete operator-guide read, including wiki safety, backup/update and MCP guidance | Instructions are doctrine, not evidence of agent compliance |
| `AUTHORS` | Excluded | Attribution metadata | No authorship assessment |
| `CHANGELOG.md` | Excluded | Historical release narrative | No release-history reconstruction; current implementation governs |
| `CODE_OF_CONDUCT.md` | Excluded | Community conduct policy | No community-governance assessment |
| `CONTRIBUTING.md` | Included | Developer operating instructions; inventoried and linked by operator guide | Contents not yet inspected; no compliance claim |
| `LICENSE` | Excluded | Legal license text | No independent legal interpretation |
| `NOTICE` | Excluded | Third-party attribution | No license-compliance audit |
| `README.md` | Included | Complete read of purpose, pipeline, deployment, consumption, backup and limitations | Declared behavior requires implementation confirmation |
| `SECURITY.md` | Included | Deployment/security policy; inventoried, referenced by Compose | Contents not yet inspected; no security audit |
| `app/` | Included | `src/app/api/onboarding/{stage,finalize}`, `api/compile/{run,draft,commit,schema}`, `api/drafts`, `api/chat`, `api/wiki`, `api/{import,export}`, source-recompile API; `src/lib/{db,retrieval,approve-plan,flush-pending,source-delete,recompile}`, ingestion steps; `instrumentation.ts`; wiki page caller; build manifest and representative durability/recompile tests. Core loop files read in full or bounded ranges; remaining paths searched/inventoried | Not every route/UI component or test read in full; no exhaustive defect or test-coverage claim |
| `cli/` | Included | `src/index.ts`, `src/startup-tasks.ts` read; `commands/{start,backup,update}` searched; remaining lifecycle commands and tests inventoried | Host scheduling and platform behavior not observed |
| `docker-compose.ci.yml` | Included | CI deployment overlay; tree/search inspection | Full overlay not yet inspected; no environment-parity claim |
| `docker-compose.yml` | Included | Complete read of service wiring, volumes, dependencies and configuration | Upstream service internals excluded; cannot certify them |
| `docs/` | Included, with peripheral assets excluded | `security/{codeql-false-positives,scorecard-deferred}.md` inventoried; `assets/` supplies presentation images | Security records not yet inspected; images excluded from operational evidence, preventing visual UX evaluation |
| `install.ps1` | Included | Setup handoff searched | Full installer/platform behavior not yet inspected |
| `install.sh` | Included | Setup handoff searched | Full installer/platform behavior not yet inspected |
| `mcp-server/` | Included | Complete `index.ts` read: four tool handlers and stdio transport; manifests inventoried | External client behavior excluded; no agent-task efficacy claim |
| `n8n/` | Included | Complete `workflows/session-compile.json` read: webhook, compile start and failure logging; `auto-import.sh` inventoried | Bootstrap script not yet read; n8n upstream execution not observed |
| `nlp-service/` | Included | `main.py` router wiring searched; `routers/{pipeline,chat}` read; conversion, extraction, resolution, storage and vector endpoints inventoried/searched; `services/llm_client.py` drafting prompts and provider dispatch read in bounded range; `file_store.py` read; `vector_store.py` searched; providers and tests inventoried | Remaining prompt/call implementations not yet inspected in full; no provider reliability or semantic accuracy claim |
| `scripts/` | Included | `migrate.py` schema-maintenance search; `integration-test.sh` evaluator-stage search; schema-sync, truncation, demos and manual regression harnesses inventoried | Harnesses not run; helper contents not all inspected |
| `setup.js` | Included | Configuration/install driver searched and linked to installers | Complete implementation not yet inspected; no installation-success claim |
| `validation/` | Included | Both dated `REPORT.md` files and May 5 `runner.py` read; retained `results.json`, timeout rerunner and May 22 runner inventoried | Exact corpus inputs unavailable; retained results not yet inspected; reports alone support attributed historical operation only |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/tuirk/Kompl` | 17970c969b0c2576bf722840e0e2db3c6416a7aa | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/kompl-9cffb1e5eb86/related-systems/tuirk--Kompl`. Implementation: tracked tree; shipped app ingestion/compile/admission/storage/retrieval/chat/wiki paths, CLI maintenance, MCP tool handlers, n8n workflow, Python router and prompt/storage paths, evaluator entry points listed above. Doctrine/design: complete README and AGENTS guide, Compose configuration, drafting prompts. Reported operation: both dated provider-validation reports. | Implementation: [compile driver](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/app/src/app/api/compile/run/route.ts), [chat caller](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/app/src/app/api/chat/route.ts), [MCP consumer](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/mcp-server/index.ts). Doctrine/design: [README](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/README.md), [prompts](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/nlp-service/services/llm_client.py). Reported operation: [May 5 report](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/validation/2026-05-05-multi-provider-corpus/REPORT.md), [May 22 pending report](https://github.com/tuirk/Kompl/blob/17970c969b0c2576bf722840e0e2db3c6416a7aa/validation/2026-05-22-deepseek-flash/REPORT.md). | No live instance, provider execution or external client trace supplied; no observed current-revision behavior or causal support. Historical validation input corpus absent from tracked source; exact-input reconstruction unavailable. Available but uninspected files are inspection limits, not access gaps. External links do not expand the source set. |
