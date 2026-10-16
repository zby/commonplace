---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AutoSci's shipped research and persistent-wiki workflows at Git revision f5c2fe009c6683b6aa5b668de759a0610c938aaf."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/skyllwt/AutoSci
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autosci/related-systems/skyllwt--AutoSci
  revision: f5c2fe009c6683b6aa5b668de759a0610c938aaf
  sha256: null
---

# AutoSci boundary

## Boundary and evidence

AutoSci is in scope as a **memory/knowledge/context-engineering system** whose model-directed research workflows produce and reuse a persistent wiki. The intended use is literature intake, research ideation, experiment design and evaluation, and paper production. This analysis covers the **whole shipped system at the acquired commit**, not only the Python wiki API. The boundary includes the agent prompts, their setup and language sources, the research orchestrator, unattended intake, browser callers, maintenance helpers, and the optional Hiera experiment sidecar. It does not treat AutoSci as the enclosing coding-agent runtime.

The classification follows the shipped producer-to-consumer loop. `/init` prepares sources and manifests and delegates paper processing to `/ingest`; `/ingest` writes entity pages and relationships and requests derived-context rebuilds. `/ask`, `/ideate`, and `/paper-plan` later load retained pages and context. `/exp-eval` specifies updates to ideas and graph edges from experiment results, and `/check` specifies structural and semantic maintenance. These are model-facing procedures, not proof that an agent obeyed them (SRC-1: `.claude/skills/init/SKILL.md`, `.claude/skills/ingest/SKILL.md`, `.claude/skills/ask/SKILL.md`, `.claude/skills/ideate/SKILL.md`, `.claude/skills/paper-plan/SKILL.md`, `.claude/skills/exp-eval/SKILL.md`, `.claude/skills/check/SKILL.md`).

> - `wiki/graph/context_brief.md` — global compressed context (ideas, gaps, failed ideas, papers, edges)
> - `wiki/index.md` — page catalog for locating relevant pages
> - `wiki/graph/open_questions.md` — open questions, helps identify whether the question touches known gaps
> --- `.claude/skills/ask/SKILL.md`

The executable layer is also inside the boundary. `runtime/loader.py` loads schema and policy data; `tools/research_wiki.py` exposes graph, metadata, lifecycle, checkpoint and context operations. Its context compiler reloads wiki files and writes a bounded `wiki/graph/context_brief.md`. The browser server is a shipped state consumer and writer, not an excluded application: entity PATCH requests call the same metadata CLI and append audit entries. The scheduled workflow can call `/ingest` and commit wiki/raw changes (SRC-1: `runtime/loader.py`, `tools/research_wiki.py`, `tools/serve.py`, `.github/workflows/daily-arxiv.yml`).

> pack_path = root / DERIVED_DIR / "context_brief.md"
> pack_path.parent.mkdir(parents=True, exist_ok=True)
> pack_path.write_text(pack, encoding="utf-8")
> --- `tools/research_wiki.py`

The optional Hiera path is included because it admits candidates, retains an evaluation ledger, and derives experience summaries from that ledger. Its separation from wiki writeback is part of the system boundary, not a reason to omit it. The CLI finalizer writes a sidecar report with `wiki_writeback` set to `none`; the skill requires returning to the normal experiment workflow for formal confirmation (SRC-1: `tools/hiera/cli.py`, `tools/hiera/experience.py`, `.claude/skills/hiera-experiment/SKILL.md`).

> It does not replace /exp-design, /exp-run, /exp-eval, or /research. A confirmatory result must return to the normal, user-gated workflow.
> --- `.claude/skills/hiera-experiment/SKILL.md`

### Frozen revision and limits

The sole source is SRC-1 at **f5c2fe009c6683b6aa5b668de759a0610c938aaf**. The acquired checkout's HEAD matched that pin and its status was clean on inspection. The applicability cutoff is **2026-10-15**, the opening's run date; it is not an observed-operation date. No additional repository, branch, web page or capture is admitted.

The overall evidence tier is **code-grounded**: executable helpers and their shipped callers are inspectable, alongside substantial prompt-level doctrine. Source inspection establishes implementation and declared contracts, not successful scientific operation, effective long-term learning, reviewer independence in practice, or causal performance gains. No target program, test, model call or external service was executed. The shipped `wiki/index.md`, `wiki/log.md` and entity placeholders are a scaffold, not a populated research-session trace (SRC-1: `wiki/index.md`, `wiki/log.md`; tracked tree).

The README describes separate Codex, OpenCode and paper branches. Those revisions are outside this pin, even when the current README describes their features. Their runtime adaptations and the full paper-system claims therefore cannot be established here. The inspected setup script activates `.claude/skills` from `i18n/<lang>/skills`; README claims about generated trees on other branches are not substituted for this implementation (SRC-1: `README.md`, `setup.sh`).

> cp "$I18N_DIR/CLAUDE.md" CLAUDE.md
> for src in "$I18N_DIR/skills"/*/SKILL.md; do
>     skill_dir=$(dirname "$src")
>     name=$(basename "$skill_dir")
>     mkdir -p ".claude/skills/$name"
>     cp -R "$skill_dir"/. ".claude/skills/$name/"
> done
> --- `setup.sh`

External dependencies remain external: Claude Code supplies the interactive model/tool loop; the CI action supplies unattended host execution; OpenAI-compatible services supply review/recommendation responses; literature APIs and downloads supply source material; SSH/GPU hosts and local commands execute experiments; browser CDN libraries render the UI. The shipped integration code, configuration and prompts are included, but the providers' internals, live responses, credentials, remote environments and actual experiment outcomes are not frozen. These limits prevent attributing host permissions, model behavior, scientific validity or deployed reliability to AutoSci alone (SRC-1: `.mcp.json`, `mcp-servers/llm-review/server.py`, `.github/workflows/daily-arxiv.yml`, `tools/remote.py`, `tools/hiera/evaluator.py`, `app/modules/reader.js`, `app/modules/graph.js`). No material shipped path was inaccessible; initial inspection is not an exhaustive audit of every function or translation.

### Top-level coverage

Every top-level tracked entry is classified below. Included means inside the functional boundary, not that every byte has already been examined. Tree-only or searched material is distinguished from source bodies initially read; these are inspection-depth limits, not access gaps. All path references in this table belong to SRC-1.

| Top-level tracked entry | Treatment and material paths | Initial inspection and role; exclusion consequence |
|---|---|---|
| `.claude/` | Included: `skills/*/SKILL.md`, local references and shared references | Bodies of init, ingest, ask, check and opening sections of research, ideate, exp-eval, paper-plan and hiera-experiment read; remaining skill tree inventoried. Model-facing state production, reuse, maintenance, experiments and writing are included, including exp-run/status/pilot, edit/reset/refine/review and citation guidance. Detailed behavior of remaining prompts is not yet established. |
| `.env.example` | Included | Tree inventory; credentials/configuration surface, not actual secrets. |
| `.gitattributes` | Excluded: repository file handling | Tree inventory only; no conclusion about cross-platform checkout normalization. |
| `.github/` | Included: `workflows/daily-arxiv.yml`, issue and PR templates | Scheduled recommendation/ingest, artifact retention and writeback body inspected; templates inventoried as contribution support. No observed CI run. |
| `.gitignore` | Included | Tree inventory; local/generated state visibility belongs to later retention checks, not an inference from absent tracked files. |
| `.mcp.json` | Included | Read; wires the local review MCP server into the host. |
| `.sleepcode/` | Included: `tests/test_discover_from_venue.py` | Imports and test-class surface searched; discovery regression specification, not a run result. |
| `CHANGELOG.md` | Included | Inventoried; shipped change narrative available as attributed doctrine, not used to infer present executable behavior. |
| `CLAUDE.md` | Included | Read; root ownership and runtime-contract instructions. |
| `CODE_OF_CONDUCT.md` | Excluded: community policy | Tree inventory only; no assessment of community governance. |
| `CONTRIBUTING.md` | Excluded: contribution procedure | Tree inventory only; no conclusion about contributor workflow quality. |
| `LICENSE` | Excluded: licensing terms | Tree inventory only; no legal assessment. |
| `README.md` | Included | Read; intended use, skills, host dependencies and branch distinctions. Marketing and paper claims remain attributed, not operational evidence. |
| `app/` | Included: `index.html`, `app.css`, `modules/{api,reader,graph,intent,state,schema,main,router,ui,wikilink,dashboard}.js` | Module imports/API and intent surfaces searched; reader/graph retention consumers traced to `tools/serve.py`. Rendering internals not exhaustively inspected. Includes browser mutation, not just visualization. |
| `assets/` | Excluded: logos, portraits, architecture/demo figures, poster images and `papers/*.pdf` | Tree inventory only. No conclusions about illustrated architecture, example papers' scientific quality, or whether advertised end-to-end results were produced by this revision. |
| `config/` | Included: environment, daily-arXiv, host permissions, remote server and visualization examples; setup guides | README searched and tree inventoried; integration configuration. Actual machine-local settings are not supplied. |
| `docs/` | Included: daily-arXiv deployment and runtime-directory charts | English chart searched; remaining bodies not yet read. Available supporting doctrine, not observed deployment. |
| `i18n/` | Included: `en/` and `zh/` root contracts, skills, references and foundations catalogs | Tree inventoried; setup activation traced from language source to active skills. No assertion of translation equivalence; setup's selected language can change the active prompt surface. |
| `mcp-servers/` | Included: `llm-review/server.py`, requirements | Server configuration and Chat Completions implementation read. Cross-model review service adapter; remote model internals excluded. |
| `raw/` | Included: `papers/`, `notes/`, `web/`, `discovered/`, `tmp/` | Tracked placeholders inventoried; ownership read in root contract and conventions. User input, fetched source and prepared sidecar zones; no supplied research corpus. |
| `requirements.txt` | Included | Inventoried dependency declaration; no installation or compatibility check performed. |
| `runtime/` | Included: `CLAUDE.md`, `loader.py`, `schema/{entities,edges,xref,conventions}.yaml`, `policy/writers.yaml`, `templates/*.md.tmpl`, package marker | Contract, loader and conventions read; writer-policy status searched; schema/template tree traced through loader and skills. Legality, entity skeletons and declared writer permissions are inside scope. Policy must not be presumed an enforced authorization gate. |
| `setup.ps1` | Included | Language-copy and tool-check sites searched; Windows activation path. Not executed. |
| `setup.sh` | Included | Language/configuration activation body read and tool-check sites searched; installs/activates prompt and helper environment. Not executed. |
| `templates/` | Included: `poster/poster_template.html` | Tree inventory; shipped dissemination output template, with poster and LaTeX helpers in scope. No rendering result claimed. |
| `tests/` | Included: `test_hiera_local.py` | Lifecycle fixture and CLI calls read; test specification for candidate admission/approval/evaluation, not observed execution. |
| `tools/` | Included: `research_wiki.py`, `lint.py`, `init_discovery.py`, `prepare_paper_source.py`, fetch/discover/backfill helpers, `daily_arxiv.py`, `serve.py`, `reset_wiki.py`, `remote.py`, visualization/poster/LaTeX/email/env helpers, and all `hiera/` modules | Function and caller searches plus selected bodies establish persistence/context compilation, validation, intake, browser writes and Hiera evaluation/reporting. Hiera includes adapter, candidate admission, contract, ledger, acquisition/scheduler/tuner, local evaluator and remote worker/adapter. Remaining helper internals are available for later source tracing, not excluded responsibilities. |
| `wiki/` | Included: `index.md`, `log.md`, entity directories, `Summary/`, `graph/`, `outputs/` | Index/log read and placeholders inventoried. Persistent product surface and future derived context; this checkout does not supply populated operation evidence. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/skyllwt/AutoSci` | f5c2fe009c6683b6aa5b668de759a0610c938aaf | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autosci/related-systems/skyllwt--AutoSci`. Implementation: complete tracked-tree inventory; `runtime/loader.py`; context compiler in `tools/research_wiki.py`; API dispatch and entity mutation in `tools/serve.py`; review API in `mcp-servers/llm-review/server.py`; Hiera experience, status/finalize and evaluator bodies; setup activation and CI ingest/writeback. Function/import searches additionally covered lint, intake/discovery, remote, reset, visualization, poster DAG support, Hiera adapters/ledger, browser callers and tests. Doctrine/design: `README.md`, root/runtime contracts, conventions, init/ingest/ask/check prompts; selected research/ideate/exp-eval/paper-plan/Hiera sections; configuration, directory and writer-policy searches; wiki scaffold. The coverage table records uninspected available bodies. | Implementation: [context compiler](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/tools/research_wiki.py), [browser server](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/tools/serve.py), [Hiera CLI](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/tools/hiera/cli.py), [CI caller](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/.github/workflows/daily-arxiv.yml). Doctrine/design: [root contract](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/CLAUDE.md), [ask consumer](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/.claude/skills/ask/SKILL.md), [ingest producer](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/.claude/skills/ingest/SKILL.md), [branch declarations](https://github.com/skyllwt/AutoSci/blob/f5c2fe009c6683b6aa5b668de759a0610c938aaf/README.md). | No access failure for the pinned shipped tree. Other branches and external host/service implementations are outside the frozen source, preventing conclusions about their behavior. No registered observed run or causal experiment: source and test specifications cannot establish deployed success, scientific validity or measured improvement. Excluded assets prevent assessment of advertised paper results. |
