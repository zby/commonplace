---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Secure LLM-Wiki's shipped ingestion, admission, persistence, maintenance and query paths at dfbc60e37487b61e9a5cbce1271a13576a776d51."
run-id: AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: dfbc60e37487b61e9a5cbce1271a13576a776d51
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/nicobleh/secure-llm-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-secure-llm-wiki/related-systems/nicobleh--secure-llm-wiki
  revision: dfbc60e37487b61e9a5cbce1271a13576a776d51
  sha256: null
---

# Secure LLM-Wiki boundary

## Boundary and evidence

Secure LLM-Wiki qualifies as a memory/knowledge/context-engineering system: it uses model calls to extract claims, reviews proposed writes, retains admitted claims, and reloads them for later model queries. The intended use of this analysis is to explain that complete shipped knowledge lifecycle and its security boundaries, not to certify resistance to injection. Its own declared purpose is persistent curated knowledge rather than repeated retrieval of raw sources (SRC-1, `README.md`):

> Instead of re-scanning raw documents on every query (classic RAG), an LLM maintains a persistent,
> linked Markdown wiki: knowledge is compiled once and then curated.
> --- `README.md`

The boundary is **whole-system**, including the shipped CLI rather than only its Python library. The installed entry point resolves directly to that driver (SRC-1, `pyproject.toml`):

> [project.scripts]
> secure-wiki = "secure_wiki.__main__:main"
> --- `pyproject.toml`

Inspection traced `main` through `init`, `ingest`, `list`, `context`, `query` and `clear`. Ingestion reads files, PDFs or HTTP sources; assigns or accepts operator trust; invokes extraction, embeddings and batch review; applies the write gate; and saves admitted or quarantined claims. The driver reloads both active claims and embeddings for later ingestion (SRC-1, `src/secure_wiki/__main__.py`):

>     # Shared wiki state — kept across files so cross-file duplicate detection works
>     store = WikiStore()
>     emb_store = EmbeddingStore(store)
>     existing = store.load_claims()
>     existing_embeddings = emb_store.load_all()
>     sim_cfg = load_similarity_config()
> --- `src/secure_wiki/__main__.py`

The included storage code serializes and reloads YAML-frontmatter Markdown, commits claim writes to a separate data repository, and implements deletion/reset. Read-time code filters retained claims and renders trust-labelled, nonce-delimited context. The shipped query consumer composes that context with its task prompt and sends questions to a model, so later consumption is inside this boundary, not an assumed external host responsibility (SRC-1, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/__main__.py`):

>     system = f"{ctx.system_note}\n\n{ctx.context_block}\n\n{QUERY_TASK_PROMPT}"
>     client = get_review_client()
> --- `src/secure_wiki/__main__.py`

Maintenance includes operator trust overrides, editable trust-rule configuration, quarantine listing, deletion and reset. It does not assume an implemented promotion or query-feedback cycle. Those are future goals, not excluded shipped paths (SRC-1, `docs/roadmap.md`):

> **Current state:** Quarantined claims can be listed but not promoted without manual file editing.
> --- `docs/roadmap.md`

### Tracked-tree coverage

The tracked root tree and all executable Python modules were inspected. Each root entry is accounted for below. “Included” means within the analytical boundary, not executed or certified.

| Top-level tracked entry | Classification and material scope | Inspection and limits |
|---|---|---|
| `.env.example` | Included: provider/model and data-root configuration template. | Read; no actual credentials or deployed configuration supplied. |
| `.gitignore` | Included: excludes local secrets, environments and generated `wiki_data/`. | Read; generated instance content is not frozen by this source checkout. |
| `.vscode/` | Excluded: `settings.json` selects a local Python interpreter. | Read; no conclusions about editor integration or developer environment reproducibility. |
| `LICENSE` | Excluded: legal licensing metadata. | Listed, not read; no licensing assessment. This is an inspection choice, not an access gap. |
| `README.md` | Included: intended knowledge lifecycle, usage, security claims and corpus description. | Read as doctrine/design, not proof of security. |
| `docs/` | Included: `article.md` explains the architecture; `roadmap.md` separates current behavior from maintenance and evaluation plans. | Both read; future features do not count as implementation. |
| `pyproject.toml` | Included: package dependencies, installed CLI entry point and test discovery. | Read and traced to the driver. |
| `requirements.txt` | Included: runtime/development dependency declarations. | Read; dependency implementations and resolved versions are outside the frozen evidence. |
| `src/` | Included: `secure_wiki/__main__.py` owns ingest/query/context/list/init/clear; `models.py` defines retained records; `llm_client.py` supplies model adapters; `prompts.py` contains extraction/review/read/query instructions and builders. `ingestion/sanitizer.py`, `extraction/extractor.py`, `trust/tiering.py`, `review/adversarial.py` and `gate/write_gate.py` implement admission. `store/wiki_store.py`, `store/embedding_store.py` and `read/hygiene.py` persist, reload, maintain and consume state. | All executable modules read, including alternate prompt-builder APIs and the actual CLI consumer. Empty package initializers and `.gitkeep` files were enumerated; they contain no additional shipped responsibility. |
| `tests/` | Included: `test_cli.py`, `test_wiki_store.py`, `test_read_hygiene.py`, `test_trust_tiering.py`, `test_adversarial.py`, `test_injection_corpus.py` and `injection_corpus/manifest.json`; eight named `.txt` corpus fixtures supply crafted inputs. | All six test modules and manifest read. Fixture filenames enumerated; payload bytes not yet inspected. The latter is not an access gap: no individual payload-efficacy conclusion is made here. No tests executed. |

### Frozen scope and exclusions

The only frozen source is SRC-1 at full commit `dfbc60e37487b61e9a5cbce1271a13576a776d51`; the supplied checkout's HEAD matched that revision and its working tree was clean. The applicability cutoff is **2026-10-19**, the supplied run date, not a claim about the date of source authorship. Later repository changes, linked external pages and unregistered sources cannot supply evidence in this run.

External dependencies are the Python environment, filesystem and Git executable; YAML/dotenv/PDF libraries; Ollama or Anthropic SDKs and services; configured extraction/review models; the optional embedding model; fetched source sites; and operator input (SRC-1, `pyproject.toml`, `src/secure_wiki/llm_client.py`, `src/secure_wiki/__main__.py`). Their shipped interfaces and fallback code are included; their external implementations, model weights and service execution are not. This prevents claims about actual model independence, service reliability, model-specific manipulation detection or deployed end-to-end safety.

Generated wiki repositories, actual trust-rule edits, embeddings and operational sessions are not supplied as frozen run evidence. This prevents conclusions about a real instance's retained knowledge, history, effective configuration or outcomes. It does not prevent tracing the shipped creation, reload and deletion code. No material shipped implementation was inaccessible.

The overall evidence tier is **code-grounded**. Documentation supplies declared intent; code and test text supply implementation evidence. Test definitions are not observed results. In particular, the corpus suite prescribes a mocked reviewer verdict rather than measuring a live review model (SRC-1, `tests/test_injection_corpus.py`):

>     review_write is mocked — the adversarial review LLM is not called, keeping
>     tests fast and deterministic. The mock blocks exactly the cases whose
>     expected_stop_gate is 'adversarial_review'.
> --- `tests/test_injection_corpus.py`

No target code, tests, examples or services were executed. This boundary establishes coverage of the shipped loop, not completeness of its security guarantees or of every planned feedback mechanism.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nicobleh/secure-llm-wiki` | dfbc60e37487b61e9a5cbce1271a13576a776d51 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-secure-llm-wiki/related-systems/nicobleh--secure-llm-wiki`. Implementation: all executable modules under `src/secure_wiki/`, all six `tests/test_*.py` modules, corpus manifest, packaging and configuration files. Doctrine/design: `README.md`, `docs/article.md`, `docs/roadmap.md`, prompt instructions in `src/secure_wiki/prompts.py`. Root-tree coverage and selective non-reads are recorded above. | Implementation: [entry point and full driver](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py), [persistence](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [context reload](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/read/hygiene.py), [corpus evaluator](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/tests/test_injection_corpus.py). Doctrine/design: [README](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/README.md), [prompts](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/prompts.py), [roadmap](https://github.com/nicobleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/docs/roadmap.md). | No material shipped-code access gap. No registered observed-run or causal-experiment evidence; no generated instance state or external dependency implementation. Consequently, neither documentation claims nor mocked test definitions establish real-world injection resistance, factual correctness or successful deployed operation. |
