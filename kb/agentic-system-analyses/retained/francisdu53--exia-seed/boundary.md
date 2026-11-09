---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EXIA SEED's shipped conversational-memory loop and evaluation tooling at commit c7497ac96da20bd1818096e35a59b6c0237f9730."
run-id: AAS-2026-11-07-exia-seed-804e805b7a8d-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: c7497ac96da20bd1818096e35a59b6c0237f9730
analysis-cutoff: "2026-11-07"
evidence-tier: code-grounded
source:
  identity: https://github.com/francisdu53/exia-seed
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/exia-seed-c2176cbd6b2b/related-systems/francisdu53--exia-seed
  revision: c7497ac96da20bd1818096e35a59b6c0237f9730
  sha256: null
---

# EXIA SEED boundary

## Boundary and evidence

This run examines EXIA SEED as a **memory/knowledge/context-engineering system**: its shipped conversational-memory plugin, maintenance tools, prompts and evaluation drivers. The intended use is to explain how conversations and explicit notes become retained, cited subject pages and how later queries consume that state. It is not an analysis of the enclosing Hermès assistant runtime. The boundary is **whole-system** for EXIA SEED's shipped artifact, including its callers and evaluators, rather than just its retrieval API (SRC-1, `README.md`, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/outils/consolider.py`, `banc/locomo/preparer.py`, `banc/locomo/repondre.py`).

The target qualifies because its consolidation issues model calls to produce retained content, and its provider serves that content back to a model-driven host. The host-facing registration and consolidation adapter establish this boundary in implementation (SRC-1):

> def register(ctx) -> None:
>     ctx.register_memory_provider(ExiaSeedProvider())
> --- `plugin/exia_seed/__init__.py`

> rep = call_llm(task="exia_seed_consolidation",
>                        provider=modele_cfg.get("provider") or None,
>                        model=modele or modele_cfg.get("default") or None,
>                        messages=messages, reasoning_config=parse_reasoning_effort(effort), timeout=timeout)
> --- `plugin/exia_seed/consolidation.py`

The included functional loop covers provider initialization and configuration; primary-conversation ingestion and explicit-note/native-memory admission; privacy and secret handling; batch closure; model prompting and deterministic fragment checks; page, index, provenance and graph maintenance; automatic recall and explicit search/read tools; and the shipped replay and scoring paths. The provider's shipped subprocess caller and nightly shell driver are included, not treated as external merely because they call the consolidation API. The loop was traced through `sync_turn`, `_lancer_consolidation`, `_consolider`, `prefetch`, `_souvenirs` and `handle_tool_call` in SRC-1 `plugin/exia_seed/__init__.py`; the consolidation CLI in `plugin/exia_seed/outils/consolider.py`; page admission and progress recording in `plugin/exia_seed/consolidation.py`; and state reload in `plugin/exia_seed/rappel.py`. The latter reconstructs its memory cache when the graph timestamp changes. These are source-level paths, not observations of execution.

Admission and downstream consumption are both material to the boundary. The checker rejects agent-only cited material, while tool descriptions tell the host model how to search retained content (SRC-1):

> if que_agent:
>             return False, "repose seulement sur des paroles de l'agent"
> --- `plugin/exia_seed/consolidation.py`

> "Search your long-term memory (EXIA SEED) when the INDEX.md summary is not enough. Give a SHORT "
> --- `plugin/exia_seed/langues/en.py`

The frozen evidence is the acquired Git checkout at **c7497ac96da20bd1818096e35a59b6c0237f9730**, verified against its HEAD. The applicability cutoff is **2026-11-07**. The overall tier is **code-grounded**; documentation supplies declared intent and attributed operation, not independently observed deployment. Version labels do not replace the commit pin: the manifest says 0.9.1 while the changelog describes further changes (SRC-1, `plugin/exia_seed/plugin.yaml`, `CHANGELOG.md`).

### Shipped-path coverage

The tracked tree has the following top-level entries. All included paths remain available for later inspection at this commit. “Not yet inspected” means available source detail, not an access failure. Table roles are grounded in SRC-1 at the named paths; the initial inspection is deliberately shallower than the later mechanism analysis.

| Top-level entry | Treatment | Material paths and responsibilities | Initial inspection and limits |
|---|---|---|---|
| `.gitignore` | Included | Python cache exclusions. | Read completely; no memory-loop responsibility. |
| `README.md` | Included | Architecture, usage, reported deployment, benchmarks and limitations. | Read completely; operational and performance statements remain author reports. |
| `CHANGELOG.md` | Included | Version history and deployment/repository distinctions. | Read completely; chronology is not proof of deployed code identity. |
| `LICENSE` | Excluded deliberately | Legal license text. | Listed, not read; no legal interpretation or licensing-compliance conclusion is supported. This does not exclude executable behavior. |
| `NOTICE` | Included | Attribution of the incorporated EXIA GHOST propagation engine. | Read completely; no independent verification of the upstream engine or its lineage. |
| `plugin/` | Included | `exia_seed/__init__.py` and `plugin.yaml`: provider hooks and tools; `config.py`: settings; `ingestion.py`, `registre.py`, `secrets.py`, `consignes.py`, `enveloppes.py`: admission; `consolidation.py`, `pages.py`, `fiches.py`, `temps.py`, `graphe.py`: retained-state production and maintenance; `rappel.py`, `requete.py`, `creux.py`, `moteur/`: reload and retrieval; `langues/`: French/English prompts, schemas and masks; `outils/`: consolidation, concept, identity-card, timestamp and graph maintenance; `exia_seed_consolider.sh`: nightly caller. | Provider, manifest, config and shell driver read completely; consolidation production/admission/model-adapter ranges, recall reload/cache range, English prompt/schema range and CLI entry points inspected. Other implementation details, French prompt variants and some maintenance bodies are available but not yet inspected. They are included, not assumed absent. |
| `banc/` | Included | `locomo/`: preparation, consolidation, memory fusion, retrieval, embedding baseline, response prompts, judging and summaries; `longmemeval/`: conversion, shared-stage launcher, reader and judge; `nexa/`: reconsolidation and measurements on copied real-memory data; `modeles/`: model/prompt comparison drivers and `consigne_terra.txt`; root benches and `souvenirs/`: retrieval, acceptance, tuning and recall diagnostics. | LoCoMo launcher, preparation and response ranges; LongMemEval launcher and judge range; Nexa reconsolidation and model-consolidation entry ranges; judge and model-measurement structure inspected. These shipped drivers persist/reload/consume state and remain inside the target. Detailed baseline algorithms, remaining diagnostics, scoring bodies and the Terra prompt are not yet inspected; no benchmark score is independently established here. |
| `docs/` | Included | `01`–`07`: skeleton, ingestion, register, consolidation, graph, recall and querying; `08`–`17`: retrieval/model experiments, LoCoMo/LongMemEval protocols, language masks, automatic recall and revisions; `A1`/`A2`: secrets and retention instructions; `R1`–`R3`: target-authored reviews/revisions; `SOURCES.md`: lineage; `00-AVERTISSEMENT.md`: public-data substitutions. | Warning read completely; other documents are available but not yet inspected. They may supply target-authored design and reported operation, not trusted external judgments or new evidence sources. |
| `tests/` | Included | `banc.sh`: disposable-container harness using the host's real plugin loader; `test_*.py`: ingestion, admission, consolidation, graph, querying, language, recall, voice, empty-memory and regression checks. | Harness read completely and suite paths inventoried. Test bodies not yet inspected; no test was run and no pass rate is asserted. |

### External dependencies and prevented conclusions

Hermès provides the `MemoryProvider` contract, hook dispatch, agent context, threading helper, configuration/home/logging facilities and auxiliary model client. Its source is not frozen in this run. Host-side scheduling, context placement, tool selection, authentication renewal and final assistant behavior therefore cannot be established independently; only EXIA SEED's side of those interfaces can be analyzed. The Docker image named by the test and benchmark launchers is also not captured, so loader compatibility and reproducible execution in that image remain unverified (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/consolidation.py`, `tests/banc.sh`, `banc/locomo/lancer.sh`). Provider services and model weights are external; source inspection cannot establish model quality, latency, cost or successful calls.

Private Nexa memories, private benchmark panels, generated run caches and full public benchmark datasets are not supplied as frozen run evidence. Included drivers still permit analysis of their construction and consumption paths, but not independent reconstruction of reported scores or actual production retention. `banc/modeles/consolider.py` also expects a separate production-plugin copy under its benchmark root; that copy is not the acquired source and cannot be silently substituted for it. The internal specification named in the plugin is expressly unpublished, preventing verification against that complete private contract (SRC-1, `README.md`, `banc/modeles/consolider.py`, `plugin/exia_seed/config.py`).

Public examples are not literal production data. The source's warning says (SRC-1):

> *English summary: names of people, companies and places, and private information, are fictitious in this public
> version, but based on real cases.
> --- `docs/00-AVERTISSEMENT.md`

This prevents treating substituted names, prices or sensitive examples as original deployment traces. No observed-run or causal-experiment layer is established by this boundary; later use of target-authored measurements must preserve their attributed status and stated conditions. References to upstream systems, protocols and papers do not register those repositories or live pages as evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/francisdu53/exia-seed` | c7497ac96da20bd1818096e35a59b6c0237f9730 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/exia-seed-c2176cbd6b2b/related-systems/francisdu53--exia-seed`. Implementation: tracked tree, provider, config, manifest, consolidation production/checker/adapter ranges, recall reload/cache range, English prompt/schema range, maintenance entry points, test harness and benchmark drivers identified above. Doctrine/design: README, configuration comments, English prompts and public warning. Reported operation: README and changelog. This is initial inspection, not a path allowlist. | Implementation: [provider](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/plugin/exia_seed/__init__.py), [consolidation](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/plugin/exia_seed/consolidation.py), [benchmark preparation](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/banc/locomo/preparer.py). Doctrine/design: [English mask](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/plugin/exia_seed/langues/en.py), [public-data warning](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/docs/00-AVERTISSEMENT.md). Reported operation: [README](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/README.md), [changelog](https://github.com/francisdu53/exia-seed/blob/c7497ac96da20bd1818096e35a59b6c0237f9730/CHANGELOG.md). | No checkout access gap encountered. External host/image, unpublished specification, production memory/plugin copy, datasets and generated runs are not frozen here: host guarantees, private-contract compliance, original deployment traces, reproduced scores and causal effects are not established. Available but uninspected source details are identified in the coverage table, not classified as unavailable. |
