---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Tortoise's graph-memory service and shipped consumers at commit 54922a800f96858935b58ef250da569a4896df44, with a partial initial loop trace."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
analysis-cutoff: "2026-10-30"
evidence-tier: code-grounded
source:
  identity: https://github.com/daniel-ospina/tortoise
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/tortoise-0c919b4ca77d/related-systems/daniel-ospina--tortoise
  revision: "54922a800f96858935b58ef250da569a4896df44"
  sha256: null
---

# Tortoise boundary

## Boundary and evidence

This run examines Tortoise as a graph-memory service for agents, including its shipped capture, extraction, persistence, retrieval and context-delivery consumers. Its intended use is to characterize how retained information reaches later model work, not to review an enclosing general-purpose agent runtime. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **complete artifact, partial loop**: the complete repository is frozen and eligible evidence, but this initial inspection has not established coverage of every shipped state-producing, maintenance, admission and consumption path. This is an inspection limit, not a missing checkout or an assertion that those paths are external.

The frozen revision is `54922a800f96858935b58ef250da569a4896df44` in SRC-1. The checkout's HEAD was checked against that pin. The applicability cutoff is 2026-10-30; later revisions, live hosted deployments and linked external documents are not evidence in this run. The overall tier is **code-grounded**: source code establishes entry-point dispatch, the model-dependent extraction seam and the retrieval-to-context call. No target code, tests, examples, model calls or services were executed.

### Classification and initial trace

Tortoise qualifies even though its read-time reflex need not call a generative model. The shipped session-capture path dispatches to model-dependent extraction; the resulting graph is available to later context delivery. The package is not merely an isolated graph library: its console scripts dispatch into a stdio MCP server or an HTTP daemon, and the repository also ships client and harness-facing code. These findings are based on SRC-1, `pyproject.toml`, `tortoise/deployment.py`, `tortoise/mcp_server.py`, `tortoise/sdk.py` and `tortoise/extractor_v2.py`.

The declared service orientation is explicit:

> Tortoise runs **as a service** — self-hosted or hosted — and your tools **connect** to it over MCP (Model Context Protocol). You don't import it into your application; you run it and point your agent at it, the way you'd run MongoDB and connect a driver.
> --- `README.md`

The executable entry point selects the shipped daemon rather than treating it as an external application:

> if sys.argv[1:2] == ["http"]:
>     sys.argv.pop(1)
>     serve_http()
>     return
> from tortoise.mcp_server import main
> main()
> --- `tortoise/deployment.py`

Initial tracing established these connections, without claiming exhaustive branch coverage:

- **Entry points and backing state.** `pyproject.toml` declares `tortoise`, `tortoise-ingest` and `tortoise-serve`. `tortoise/deployment.py` selects stdio or HTTP. `tortoise/mcp_server.py` resolves a backend URI, opens a Falkor projection and binds it to `TortoiseSDK`. The main CLI also dispatches to a shipped store-sync recovery command. These are source-level observations, not evidence of a running deployment (SRC-1, `tortoise/__main__.py`, `tortoise/ingest.py`).
- **Model-dependent write path.** `capture_session` selects an extraction lane, including `_extract_session_v2`. That method selects an adapter, bounds/redacts the conversation and invokes `extract_session_v2`; the extractor's completion helper calls the model. Thus this target serves model-dependent memory formation, not just a returning deterministic database query (SRC-1, `tortoise/sdk.py`, `tortoise/extractor_v2.py`).
- **Persistence interfaces.** `_emit_event` declares separate JSONL rebuild-journal, graph-event and optional Postgres-record outcomes. `record_writer.py` describes the record-write seam and its configuration gate. This establishes material storage surfaces requiring analysis, not an all-writes durability guarantee (SRC-1, `tortoise/sdk.py`, `tortoise/record_writer.py`).
- **Later consumption.** `volunteer_context` validates inputs, obtains the projection and calls `run_volunteer_pipeline` with the SDK's retrieval function. `framework.py` supplies adapters that put the returned block into framework prompts. The shipped Claude instructions tell the consuming agent to use injected prior memory and contribute durable information back. These consumers remain inside the target's functional scope (SRC-1, `tortoise/sdk.py`, `tortoise/volunteer.py`, `tortoise/framework.py`, `tortoise/claude-hooks/CLAUDE.tortoise.md`).
- **Distinct hosted capture.** Searches identify the hosted `_capture_session_impl` and the MCP wrapper importing it, as well as hosted and self-hosted volunteering endpoints. The hosted capture path is not assumed identical to `sdk.capture_session` merely because they have related responsibilities (SRC-1, `tortoise/hosted_api.py`, `tortoise/mcp_server.py`, `tortoise/selfhost_api.py`).

The model dependency is supported by the executable completion seam:

> def _body():
>     kwargs = _cap_kwargs(model, max_tokens, stats)
>     box["resp"] = model.complete(system=system, user=user, **kwargs)
> --- `tortoise/extractor_v2.py`

The read-to-context seam is also executable:

> proj = self._get_proj()
> return run_volunteer_pipeline(
>     proj, window, session_id=session_id, prior_context=prior_context,
>     min_confidence=min_confidence, max_pointers=max_pointers, why=why,
>     _search_fn=self.tortoise_fts_query,
> )
> --- `tortoise/sdk.py`

### Functional scope and inspection frontier

All tracked paths at the pin remain available under SRC-1. The table distinguishes initial inspection from material not yet inspected; it is not a whole-system coverage claim or a path allowlist.

| Surface | Treatment and initial inspection | Limit on conclusions |
|---|---|---|
| Server/package entry points | Included; package script declarations, `tortoise/deployment.py`, MCP backend resolver, scoped CLI and ingest searches | Does not establish every CLI command or transport's behavior. |
| Memory formation and state | Included; selected `tortoise/sdk.py` capture and extraction branches, selected `tortoise/extractor_v2.py` code, record-writer declaration | Does not establish all admission, merge, supersession, replay, quota, consistency or persistence failure branches. |
| Retrieval and later model context | Included; SDK volunteering call, `tortoise/volunteer.py` contract, `tortoise/framework.py` adapters; `tortoise/session_reinjection.py` located by search | Does not establish complete retrieval ranking, source-session reinjection or prompt-budget behavior. |
| Shipped harness hooks and instructions | Included; `tortoise/claude-hooks/CLAUDE.tortoise.md` read, session-start/end hook searches, Pi capture source located; package-data lists Claude, Codex, Cursor, Pi, Hermes and OpenClaw artifacts | The other hook/plugin bodies, installer/consent gates and recovery consumers are not yet traced end-to-end. No cross-harness parity conclusion follows. |
| Hosted/self-host control and data planes | Included; endpoint/capture searches in `tortoise/hosted_api.py` and `tortoise/selfhost_api.py`; record seam inspected at declaration level | Full request admission, tenant resolution, daemon lifecycles, record/cache reload and maintenance drivers remain uninspected. No complete service-loop or security claim follows. |
| Shipped clients, integrations and UIs | Included as target consumers, not excluded hosts: `client/`, `integrations/`, `apps/`, `menu-bar/`, `services/`, and `website/apps/dashboard/` identified from the tracked tree | Bodies not yet traced. Cannot claim all state writers/readers or user-mediated admission and deletion paths are covered. |
| Packs, schemas, configuration and maintenance | Included: `packs/`, `config/`, `supabase/`, `graph-scripts/`, `tortoise/dream.py`, backup/rebuild and projection modules identified from the tree and package declarations | Not yet traced through each consumer. Cannot infer deployed schema, complete maintenance policy or loss/recovery guarantees from names or architecture prose. |
| Evaluators | Included: `battery/`, `benchmarks/`, `eval/`, `tests/`, `tools/longmem_eval/`, `validation/`, `spike/` and engineering experiment artifacts; LongMemEval runner README inspected | No evaluator execution or result verification. Documentation identifies intended ingest→retrieve→reader→judge use, not measured effectiveness at this revision (SRC-1, `tools/longmem_eval/README.md`). |
| Target documentation and repository operations | Available as attributed design/operation evidence: `README.md`, `docs/`, root agent guidance, `operations/`, domain indexes, deployment files and CI/tooling | Most bodies not inspected. Their presence is not evidence that a design is implemented, a procedure ran or a production condition holds. |

No material shipped responsibility is deliberately excluded as an unrelated enclosing application. Conversely, external host runtimes (Claude Code, Codex, Cursor, Pi, Hermes, OpenClaw and framework engines), model-provider implementations, FalkorDB/Redis implementations, Postgres/Supabase service internals, cloud infrastructure and the live hosted installation are outside the frozen repository evidence. Their interfaces may be analyzed where represented in SRC-1; their internal scheduling, actual availability, provider quality, persistence guarantees and end-user outcomes cannot be established here. These are evidence-boundary exclusions, not responsibilities attributed to Tortoise (SRC-1, `README.md`, `pyproject.toml`, `tortoise/framework.py`, `tortoise/record_writer.py`).

No repository access gap was encountered. Available but uninspected paths above are an inspection frontier, not unavailable evidence. The partial-loop classification prevents treating this boundary declaration as proof of whole-system coverage. Later source inspection at this same pin may establish additional mechanisms, but cannot establish observed operation merely by finding their code.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/daniel-ospina/tortoise` | 54922a800f96858935b58ef250da569a4896df44 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/tortoise-0c919b4ca77d/related-systems/daniel-ospina--tortoise`. Tracked tree inspected. Implementation: selected script/package declarations and dispatch in `pyproject.toml`, `tortoise/deployment.py`, MCP backend resolver; selected SDK capture/extraction/volunteering code and extractor completion seam. Scoped searches in CLI, ingest, hosted/self-host endpoints and harness hooks. Doctrine/design: README service contract, volunteering/framework contracts, record-write seam declaration, shipped Claude memory instructions and LongMemEval runner introduction. Initial inspection only; all tracked paths at this commit remain eligible. | Implementation: [entry point](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/tortoise/deployment.py), [SDK](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/tortoise/sdk.py), [extractor](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/tortoise/extractor_v2.py). Doctrine/design: [service declaration](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/README.md), [consumer instructions](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/tortoise/claude-hooks/CLAUDE.tortoise.md), [evaluation contract](https://github.com/daniel-ospina/tortoise/blob/54922a800f96858935b58ef250da569a4896df44/tools/longmem_eval/README.md). | No access failure. Partial initial tracing prevents a whole-system coverage claim. Implementation evidence does not prove successful operation. No observed-run or causal-experiment layer is established by this inspection; committed evaluation artifacts are not endorsed without inspecting their conditions. External services, linked sources and later revisions are not frozen evidence. |
