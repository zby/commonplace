---
description: "Generated memory comparisons from retained main-review evidence"
type: types/note.md
traits: [has-comparison]
---

# Memory mechanisms in agentic systems

Each row uses one main-review result and its stated memory boundary. Values
carry their evidence basis. Absence, inapplicability, uninspected mechanisms,
and indeterminate classifications remain distinct. This is the selected
population, not the historical memory-review corpus.

## code-grounded (3)

| System | Compared boundary | Storage | Read-back | Push selection | Trace learning | Authority | Evidence |
|---|---|---|---|---|---|---|---|
| [Dynamic Cheatsheet](../../../../agentic-systems/reviews/dynamic-cheatsheet.md) | Use-accumulated cheatsheets, earlier input/output and tool traces, imported seed/checkpoint state, retrieval vectors and index alignment, plus the bounded provider-native execution object, in the six advanced_generate variants and benchmark caller. Static templates and benchmark targets are context/evaluation evidence, not memory-profile members. Provider payloads and imported-vector production remain unknown. | files [observed], in-memory [wired], service-object [wired], vector [wired]; partial coverage | pull [wired], push [observed]; partial coverage | coarse [observed], inferred-embedding [wired], inferred-judgment [wired]; partial coverage | yes [wired]; partial coverage | instruction [wired], knowledge [observed], ranking [wired]; partial coverage | [AAS-2026-09-26-dynamic-cheatsheet-02](../../agentic-system-analysis-archive/AAS-2026-09-26-dynamic-cheatsheet-02/result.md) |
| [Mem0](../../../../agentic-systems/reviews/mem0.md) | OSS synchronous Python Memory with default Qdrant/OpenAI adapters and SQLite history/messages: inferred and raw add, procedural summaries, explicit CRUD, get/get_all/search/history, entity access records, default search, expiration and immutable identity handling, and caller extraction instructions. Excludes AsyncMemory, other providers, optional reranker internals, vision, cloud/server/SDK integrations, evaluation packages and enclosing-agent execution. Static prompts guide writes but are not changed-through-use memory. | sqlite [wired], vector [wired] | pull [afforded], push [wired] | identifier [wired], inferred-embedding [wired] | yes [wired] | knowledge [wired], ranking [wired], routing [wired] | [AAS-2026-09-26-mem0-02](../../agentic-system-analysis-archive/AAS-2026-09-26-mem0-02/result.md) |
| [Napkin](../../../../agentic-systems/reviews/napkin.md) | Current Napkin package retained vault notes and context, mutable templates and structured views, compiled access caches, shipped distill/tend procedures, documented session-context consumers, and benchmark import/read paths. Excludes legacy code, static shipped instructions as memory, external agent/provider implementations, and unretained deployments. Transient SQLite base access structures are included but distinguished from durable storage. | files [wired], in-memory [wired], sqlite [wired] | pull [afforded], push [afforded] | coarse [afforded]; partial coverage | yes [afforded] | instruction [afforded], knowledge [afforded], ranking [wired], routing [afforded] | [AAS-2026-09-27-napkin-01](../../agentic-system-analysis-archive/AAS-2026-09-27-napkin-01/result.md) |

## doc-grounded (0)

No selected results in this tier.

## Input identities

- `kb/agentic-systems/reviews/dynamic-cheatsheet.md`: `76c76c5e7e2aea281012933a60b42b338f68e6363f98e0b5a02ff7cad0a36445`; exact result `kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/result.md`: `69cf228433d975ac518c02f315ac81aaa26a6b29c3e3db63b932e6a199194cfa`; source `https://github.com/suzgunmirac/dynamic-cheatsheet` at `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.
- `kb/agentic-systems/reviews/mem0.md`: `f0ed4295059b4885a886892e7731bda966eb8a89dba4c51366cfb5aac70abfe4`; exact result `kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-mem0-02/result.md`: `b4a541c5e6a90e37dbb0115bf9e230c41c5fc635023b519a57c447d4b7ffabd1`; source `https://github.com/mem0ai/mem0` at `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`.
- `kb/agentic-systems/reviews/napkin.md`: `1d5b8e3ef19c834de3242ebf99002010e83fd7413256bcd6995f66fb4c3fdae7`; exact result `kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-01/result.md`: `8484f622335c134237968326c9971d8fbb1e71f97128e411f96b8d46ccba41db`; source `https://github.com/Michaelliv/napkin` at `7582d6a46f5a11995956e60a59c41a5b242109f1`.
