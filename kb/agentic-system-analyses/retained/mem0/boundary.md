---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Mem0's shipped memory engines, clients and consumption integrations at commit 0724291bd864cf807e88ee8981c8226644e8fb42, with the hosted backend and evaluation submodule unavailable."
run-id: AAS-2026-10-14-mem0-5b642a1731b4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "0724291bd864cf807e88ee8981c8226644e8fb42"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/mem0ai/mem0
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mem0-5b642a1731b4/related-systems/mem0ai--mem0
  revision: 0724291bd864cf807e88ee8981c8226644e8fb42
  sha256: null
---

# Mem0 boundary

## Boundary and evidence

This run analyses Mem0 as a memory/knowledge/context-engineering system. Its intended use is retaining information from conversations and returning relevant retained content to applications and agents. The target includes the repository's self-hosted engines, hosted-service clients, shipped drivers, agent integrations and memory instructions. It is not an enclosing general-purpose agent runtime. Classification is grounded in the exported memory APIs, the model-dependent extraction path and shipped consumers, rather than in the repository's marketing alone (SRC-1, `mem0/__init__.py`, `mem0/memory/main.py`, `README.md`, `integrations/openclaw/index.ts`).

The Python package exports both local engines and hosted clients:

> from mem0.client.main import AsyncMemoryClient, MemoryClient  # noqa
> from mem0.memory.main import AsyncMemory, Memory  # noqa
> --- `mem0/__init__.py`

The local engine's extraction path invokes its configured model; it is not merely a storage wrapper (SRC-1, `mem0/memory/main.py`):

> response = self.llm.generate_response(
>     messages=[
>         {"role": "system", "content": system_prompt},
>         {"role": "user", "content": user_prompt},
>     ],
>     response_format={"type": "json_object"},
> )
> --- `mem0/memory/main.py`

The boundary kind is **complete artifact, partial loop**. The complete repository artifact is frozen, but it does not provide the hosted backend or the contents of its evaluation submodule. This is not a claim of whole-system inspection, operational completeness or Python/TypeScript parity. A complete disposition means that a coherent target and usable frozen evidence boundary have been established; later analysis must retain these limits.

The reviewed boundary is commit `0724291bd864cf807e88ee8981c8226644e8fb42` of `https://github.com/mem0ai/mem0`. The checkout's HEAD was verified against that acquisition pin and its worktree status was clean. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim about when every feature was released or deployed. The overall evidence tier is **code-grounded**. No target code, examples, tests, providers or services were executed. Source text establishes implementation and declared contracts, not successful operation or causal efficacy.

### Functional inclusions and initial coverage

All tracked content in the pinned repository remains available for later inspection under SRC-1, except that a Git submodule pointer supplies no contents from the referenced repository. Initial inspection is deliberately distinguished from evidence still to be read. Paths not yet inspected are not access gaps.

| Shipped surface | Included responsibility and initial inspection | Coverage limit |
| --- | --- | --- |
| Python engines and dependencies | `mem0/__init__.py`; portions of `mem0/memory/main.py` covering construction, input admission, retained-message reload, retrieval of existing memories and model extraction; `mem0/configs/base.py`. Retention, search, updates, deletion, procedural memory, entity handling, provider adapters, prompts and telemetry throughout `mem0/` are included. | Remaining methods and adapters are available but not yet inspected in detail. Do not generalize initial extraction inspection to all configurations. |
| Python persistence and prompts | `mem0/memory/storage.py` method inventory; prompt definitions in `mem0/configs/prompts.py` searched and imports traced from the engine. SQLite history and conversation storage, extraction instructions and custom instructions belong to the target. | Persistence method bodies and full prompt text remain to be inspected; no durability or instruction-following result is established. |
| Hosted Python client | Constructor and HTTP setup in `mem0/client/main.py`; public exports in `mem0/__init__.py`. Client-side scoping, request construction, polling and project operations are included. | Only the shipped client is executable evidence about this path. Remote backend behavior is unavailable. |
| TypeScript engine and client | `mem0-ts/package.json`, `mem0-ts/src/client/index.ts`, `mem0-ts/src/oss/src/index.ts`; tracked tree of `mem0-ts/src/oss/`. Separate hosted-client and OSS exports are included, along with OSS memory, storage, providers, prompts and tests. | Engine implementation and client request bodies are available but not yet traced. Python behavior cannot be attributed to TypeScript without that inspection. |
| Shipped API server and dashboard | `server/server_state.py` inspected; `server/main.py` routes searched. The server constructs and replaces an OSS `Memory` instance and exposes creation, search, retrieval, updates, history, deletion and reset. Server configuration persistence and dashboard consumers are included, not treated as external merely because they call the library. | Route bodies, authorization, dashboard flows and restart behavior require further inspection. |
| Shipped answer-producing consumers | `README.md` basic chat driver and `mem0/proxy/main.py` inspected. The driver retrieves memories, supplies them to answer generation, then stores the conversation. The proxy selects local versus hosted memory, starts addition, retrieves content and formats model input. OSS examples in `examples/misc/` were identified by imports. | Other examples and notebooks are available but not yet read; illustrative source is not a recorded successful run. |
| Agent and framework integrations | `integrations/openclaw/index.ts` prompt-build hook inspected; capture hooks searched; portions of `integrations/openclaw/providers.ts` inspected. `integrations/openclaw/skills/memory-triage/SKILL.md` inspected through its decision gates. Python OSS consumers in `integrations/hermes-plugin-mem0/_backend.py` and `integrations/mem0-strands/python/src/mem0_strands/client.py` identified by search. All shipped integrations, hook lifecycle, scope management, recall, capture and maintenance instructions are included. | Most integration implementations remain to be read. Host runtimes themselves are external; their scheduling or model execution is not attributed to Mem0. |
| CLI and integration skills | `cli/python/src/mem0_cli/backend/platform.py` HTTP backend inspected; CLI trees enumerated; `skills/mem0/SKILL.md` initial integration instructions inspected. Both CLI implementations, reference skills, integration/testing/migration workflows and plugin manifests are included. | Other CLI commands, skills and plugin packaging remain to be inspected. Declared procedures do not establish that an agent carried them out. |
| Documentation and evaluators | `README.md` benchmark qualification inspected; `docs/` and `tests/` tracked trees sampled; `.gitmodules` inspected. Repository documentation, unit/integration test source and integration-local tests are included as design or implementation evidence where read. | Most tests and docs are uninspected, not unavailable. The separate `evaluation` repository is unavailable; no tests were run. |

The consumption loop is therefore not bounded at `Memory.search`. For example, the shipped README driver explicitly inserts retrieved content into the next answer's system prompt (SRC-1, `README.md`):

> system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
> --- `README.md`

Likewise, agent-side retention instructions are target content, not merely documentation about an external caller. The OpenClaw plugin's shipped protocol directs the host agent to evaluate a turn for persistent facts (SRC-1, `integrations/openclaw/skills/memory-triage/SKILL.md`):

> You have persistent long-term memory powered by mem0. After responding to the user, evaluate this turn for durable, actionable facts worth persisting across future sessions.
> --- `integrations/openclaw/skills/memory-triage/SKILL.md`

These establish included responsibilities and consumption paths, not that a particular host follows the protocol or that an end-to-end loop succeeded.

### Exclusions, dependencies and prevented conclusions

- **Hosted backend implementation is unavailable.** `MemoryClient` points at the hosted service, and the CLI has a Platform HTTP backend (SRC-1, `mem0/client/main.py`, `cli/python/src/mem0_cli/backend/platform.py`). Neither is evidence of the service's internal memory extraction, maintenance, temporal reasoning, admission or retrieval implementation. Hosted features may be described only as client contracts or attributed documentation unless this repository supplies implementation evidence.
- **The evaluation submodule's contents are unavailable within this source.** The tracked `evaluation` entry is a Gitlink to another repository; the local directory supplied no files. `.gitmodules` identifies `https://github.com/mem0ai/memory-benchmarks` (SRC-1, `.gitmodules`). That repository is not a second registered source and must not be fetched. This prevents inspection of its evaluation protocol, datasets and run artifacts or independent support for benchmark accuracy claims.
- **External model, embedding, database and host implementations are excluded.** The target includes Mem0's adapters, factory selection, connection/configuration code and shipped host hooks; it does not include the corresponding service internals or enclosing host runtime. Construction dependencies are visible in `mem0/memory/main.py`, `mem0/configs/base.py` and `pyproject.toml`; OpenClaw hook use is visible in `integrations/openclaw/index.ts` (SRC-1). This prevents conclusions about provider reliability, model quality, database guarantees beyond inspected adapter contracts, or host-wide scheduling and safety.
- **Moving websites, deployed applications and linked papers are excluded.** Frozen repository documentation can supply attributed declarations, but links do not freeze their destinations. This prevents claims about current deployments, later revisions or external research results based on those destinations.
- **Repository administration and packaging are contextual rather than independent memory mechanisms.** Root governance files, CI, plugin marketplace descriptors, build metadata and scripts remain inspectable when they explain shipping, entry points or instructions. Their presence alone does not support behavior or performance claims.

The repository itself explicitly separates platform benchmark numbers from open-source behavior (SRC-1, `README.md`):

> Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md`

This qualification is retained as a source declaration. It does not establish equivalent gains in OSS. No observed-run or causal-experiment evidence was supplied or established at this boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/mem0ai/mem0` | 0724291bd864cf807e88ee8981c8226644e8fb42 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mem0-5b642a1731b4/related-systems/mem0ai--mem0`. Implementation: exports, Python engine construction and extraction portions, proxy, server state, client and CLI HTTP setup, TypeScript export surfaces, OpenClaw prompt-build hook and provider configuration portions. Doctrine/design: README usage, Python configuration, initial SDK skill instructions and memory-triage gates. Reported operation: README benchmark summary and platform/OSS qualification. Tree and bounded searches additionally located other consumers, persistence methods, prompts and tests; these are not full behavioral inspections. | Implementation: [Python engine](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/mem0/memory/main.py), [proxy](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/mem0/proxy/main.py), [server state](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/server/server_state.py), [client](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/mem0/client/main.py), [CLI backend](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/cli/python/src/mem0_cli/backend/platform.py), [TypeScript OSS exports](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/mem0-ts/src/oss/src/index.ts), [OpenClaw hooks](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/integrations/openclaw/index.ts). Doctrine/design: [SDK skill](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/skills/mem0/SKILL.md), [memory protocol](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/integrations/openclaw/skills/memory-triage/SKILL.md). Doctrine/design and reported operation: [README](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/README.md). Submodule boundary: [.gitmodules](https://github.com/mem0ai/mem0/blob/0724291bd864cf807e88ee8981c8226644e8fb42/.gitmodules). | Hosted backend and evaluation-submodule contents are not supplied. External providers and host runtimes are outside this repository. Implementation inspection supports source behavior, doctrine supports declared contracts, and reported benchmarks remain attributed claims. No target execution or experiment supports end-to-end success, reliability or causal performance attribution. Available but uninspected paths are listed separately above and remain within the registered repository boundary. |
