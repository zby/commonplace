---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Synapptic's shipped transcript-to-profile pipeline, output integrations, benchmarks and optional relay at commit bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f."
run-id: AAS-2026-10-15-synapptic-9dce97c66546-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/appcuarium/synapptic
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/synapptic-9dce97c66546/related-systems/appcuarium--synapptic
  revision: bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f
  sha256: null
---

# Synapptic boundary

## Boundary and evidence

Synapptic is in scope as a memory/knowledge/context-engineering system. Its intended use is to turn AI coding-session transcripts into persistent user preferences, AI failure observations and preventive rules, then publish narrative profiles to coding-assistant instruction or memory files. It issues model calls for observation extraction, narrative synthesis and behavioral benchmarking; it does not own the coding assistant's enclosing reasoning-and-tool loop. This classification follows the shipped CLI and its consumers, not just the package description (SRC-1, `pyproject.toml`, `src/synapptic/cli.py`, `src/synapptic/extract.py`, `src/synapptic/synthesize.py`, `src/synapptic/outputs.py`).

> synapptic = "synapptic.cli:cli"
> --- `pyproject.toml`

> def ingest(model, max_tokens, project, min_lines, limit):
>     """Full pipeline: extract → merge → synthesize → integrate."""
> --- `src/synapptic/cli.py`

The boundary is **whole-system** for the shipped repository, including its optional relay rather than only the profile library API. Initial inspection traced `ingest` from transcript discovery and processed-session selection through filtering, model extraction, observation persistence, global/project routing, weighted merging, cross-project promotion, narrative persistence and output integration. It also traced the separately installed SessionEnd hook and the standalone `synthesize` command. Those are included shipped drivers even where their paths differ: the hook calls `extract`, `merge` and `synthesize`, while the inspected standalone `synthesize` command saves narratives without calling output integration. Inclusion does not imply that every entry point completes the same publication loop (SRC-1, `src/synapptic/cli.py`, `src/synapptic/bundle/hooks/synapptic-session-end.sh`).

Persistent content has shipped consumers. Extraction reloads the existing profile as prompt context; synthesis reloads weighted profiles; integration reloads saved archetypes; benchmarks reload profiles and narratives. The Claude Code writer creates `user_archetype.md` and, when an existing `MEMORY.md` is present, maintains a reference to it. Other writers publish to assistant-specific project files. These establish production and reuse interfaces inside Synapptic, not proof that each external host actually reads or obeys the output (SRC-1, `src/synapptic/cli.py`, `src/synapptic/state.py`, `src/synapptic/extract.py`, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`, `src/synapptic/benchmark.py`).

>     output_targets = config.get("outputs", ["claude-code"])
>     global_archetype = load_archetype(project_slug=None) or ""
> --- `src/synapptic/integrate.py`

The optional relay is also included: the CLI launches external tools with relay endpoint environment variables; FastAPI routes forward Anthropic/OpenAI requests and retain metrics; SQLite stores request/session data and a transcript index; browser/dashboard routes and templates consume those records or local JSONL transcripts. This is a shipped observability and transcript-browsing path, not an excluded enclosing application. Its inclusion does not attribute the launched tools' planning, transcript generation or instruction-loading semantics to Synapptic (SRC-1, `src/synapptic/cli.py`, `src/synapptic/relay/app.py`, `src/synapptic/relay/routers/anthropic.py`, `src/synapptic/relay/routers/browser.py`, `src/synapptic/relay/store.py`, `src/synapptic/relay/indexer.py`).

The frozen evidence is repository `https://github.com/appcuarium/synapptic` at full commit `bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f`. The read-only acquired checkout's HEAD matched that pin. The applicability cutoff is 2026-10-15; later commits, live documentation, installed packages and external service behavior are outside this evidence set. The overall tier is **code-grounded**. Target documentation supplies declared intent, not independent confirmation of its claims.

### Repository coverage

Every top-level tracked file or directory is classified below. Included scope covers the paths named whether or not every line has already been inspected. Initial inspection is identified separately from remaining detail; an available but unread file is not an access gap. All entries refer to SRC-1.

| Top-level tracked entry | Decision and role | Initial inspection and limits |
|---|---|---|
| `.github/` | Included: `.github/workflows/tests.yml` defines the shipped CI test invocation. | Workflow read. No CI execution trace was supplied; no conclusion about CI success. |
| `.gitignore` | Excluded: repository housekeeping. | Tree entry identified; contents not inspected. Ignore policy and local untracked-file completeness are not assessed. |
| `CHANGELOG.md` | Included: first-party release and feature claims. | Current b5/b4 sections inspected as doctrine/reported operation, not observed results. Older history not yet inspected. |
| `LICENSE` | Excluded: licensing text, not the operational loop. | Tree entry identified; contents not inspected. No legal or licensing assessment. |
| `OLLAMA_SETUP.md` | Included: provider configuration and operating instructions. | Initial setup, presets and text-only operation claims inspected. Remaining guidance not yet inspected; provider correctness requires implementation evidence. |
| `README.md` | Included: intended use, installation, transcript sources, profile flow, output contracts and benchmark claims. | Opening sections through behavioral benchmarking inspected. Later reference/privacy/troubleshooting sections not yet inspected. Claims of efficacy or universal host loading remain unverified. |
| `assets/` | Excluded: `assets/banner.png` is presentation material referenced by README. | Tree and reference inspected, image not inspected. No branding or visual assessment. |
| `pyproject.toml` | Included: package entry point, dependency declarations and bundled resources. | Read completely; no installation or dependency-resolution experiment. |
| `src/` — profile production and maintenance | Included: `src/synapptic/{cli,config,filter,scrub,extract,patterns,profile,state,synthesize}.py` and `__init__.py`; `bundle/patterns/default/prompt.md`, `bundle/skill/SKILL.md`, `bundle/hooks/synapptic-session-end.sh`. Covers shipped prompts, session selection, admission, retention, reload, maintenance commands and installation. | CLI ingest/synthesis/install/tool-launch paths, extraction and merging implementation, narrative filtering, state read/write paths, filter entry point, default prompt, skill and hook inspected. Supporting configuration, scrubbing, custom-pattern loading and maintenance-command details remain available for deeper inspection. |
| `src/` — publication and evaluation | Included: `src/synapptic/{integrate,outputs,benchmark,benchmark_results,providers}.py`. Covers retained-content publication, provider calls, benchmark generation/judging, guard verdicts and result consumption. | Integration read; Claude Code/Cursor output paths, provider dispatch/CLI calling, benchmark entry points and archetype-loading logic inspected. Other writers, benchmark internals and result summarization remain available for deeper inspection. Both per-guard and batched benchmark paths are in scope; their differing comparison conditions must not be conflated. |
| `src/` — optional relay and operator consumers | Included: all `src/synapptic/relay/` modules, `routers/` and `templates/`. Covers forwarding/SSE, token extraction, session identification, SQLite persistence, transcript parsing/indexing, dashboard/browser HTTP and WebSocket consumers. | App factory, Anthropic route entry, browser read/search routes, indexer entry points and store schema read; OpenAI/dashboard functions and template API/WebSocket consumers searched. Forwarding, parsing, streaming and remaining handler details are included but not yet inspected in depth. |
| `tests/` | Included: all shipped `test_*.py`, `conftest.py`, `__init__.py` and `fixtures/sample_session.jsonl` as test/evaluation design, not live user evidence. | Test tree and selected suite class names inspected; mocked benchmark orchestration smoke test read. Other tests and fixture contents not yet inspected. Nothing was executed. |

### External dependencies and evidence limits

External coding assistants supply transcripts, invoke the installed hook, load published files and perform coding work. Their implementations are not captured. This prevents conclusions about actual host admission, instruction precedence, compliance or downstream task improvement. The shipped skill's automatic-loading and cost claims are first-party doctrine, not observed operation (SRC-1, `README.md`, `src/synapptic/bundle/skill/SKILL.md`, `src/synapptic/outputs.py`).

Model inference depends on configured Claude CLI, Anthropic, Ollama or OpenAI-compatible providers. The optional relay additionally depends on FastAPI, httpx and uvicorn. Source inspection establishes adapter responsibilities, not service availability, response quality, compatibility across provider versions or reliable runtime performance (SRC-1, `pyproject.toml`, `src/synapptic/providers.py`, `src/synapptic/relay/app.py`).

No real user transcript corpus, generated profile history, benchmark execution artifact or deployment trace was supplied. Shipped tests and benchmark code are inspectable evaluators, not observed-run or causal-experiment evidence for effectiveness. In particular, the inspected orchestration test mocks all model calls:

> class TestRunBenchmarkSmoke:
>     """Smoke test for run_benchmark() orchestration — all LLM calls mocked."""
> --- `tests/test_benchmark.py`

This limits conclusions about learned-profile accuracy, privacy protection in practice, guard efficacy, cost, throughput and long-term adaptation. No target code, tests, examples or providers were executed. There is no known unavailable repository path that forces a partial-loop boundary; remaining source detail is available for later jobs under the same pin.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/appcuarium/synapptic` | bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/synapptic-9dce97c66546/related-systems/appcuarium--synapptic`. Implementation: tracked tree, package entry point, CLI drivers, extraction/profile/narrative flow, state persistence, output integration, provider dispatch, benchmark entry points, relay app/routes/index/schema and test design as detailed above. Doctrine/design: README opening and benchmark sections, bundled extraction prompt/skill, Ollama setup opening and CI workflow. Reported operation: current changelog and README claims, without retained execution evidence. Listed paths describe initial inspection, not an allowlist. | [Package entry point](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/pyproject.toml); [CLI drivers](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/cli.py); [output consumers](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/outputs.py); [benchmark implementation](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/benchmark.py); [relay app](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/src/synapptic/relay/app.py); [declared workflow](https://github.com/appcuarium/synapptic/blob/bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f/README.md) | No known repository access gap. External hosts, model services and real execution artifacts are not captured: actual loading, compliance, efficacy, performance and operational reliability cannot be established. No observed-run or causal-experiment layer is registered. |
