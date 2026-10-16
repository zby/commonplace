---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "WikiSkill's shipped experience-to-Wiki-to-skill loops at commit da6984caca09d5f81b2336cf3067b59c0c18bb1e."
run-id: AAS-2026-10-15-wikiskill-baafad05d35e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: da6984caca09d5f81b2336cf3067b59c0c18bb1e
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/Stahl-G/WikiSkill
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-baafad05d35e/related-systems/Stahl-G--WikiSkill
  revision: da6984caca09d5f81b2336cf3067b59c0c18bb1e
  sha256: null
---

# WikiSkill boundary

## Boundary and evidence

This analysis covers the independent WikiSkill implementation shipped in SRC-1, not the original paper's implementation or the external BriefLoop application. Its intended use is to improve reusable agent instructions from task outcomes and user feedback through persistent Wiki knowledge and candidate evaluation. It qualifies as a memory/knowledge/context-engineering system: model-produced lessons persist, feed a separate skill proposal, and affect later task execution. It is not an enclosing general-purpose agent runtime. The boundary is whole-system, including the product controller, host-facing instructions and role assets, feedback-first API, research engine, domain drivers, isolated study, scoring and installation paths (SRC-1, `README.md`, `src/wikiskill/product.py`, `src/wikiskill/engine.py`, `src/wikiskill/feedback_loop.py`).

The source declares the host/controller division explicitly:

> Help the user improve a recurring agent task through experience. Use the user's current agent, chosen model and normal tools. WikiSkill owns the work requests, records, scores and retained skill versions; it does not select a model or change host permissions.
> --- `skills/wikiskill/SKILL.md`

The installed console entry is `wikiskill.cli:main`; its routing reaches both product commands and the research evolution/study commands. MCP wraps the product functions, rather than creating a separate model runtime (SRC-1, `pyproject.toml`, `src/wikiskill/cli.py`, `src/wikiskill/mcp_server.py`). Native handoffs, controller persistence and host execution are all material parts of the product loop, not reasons to restrict this analysis to an API. Native-agent creation itself remains the external host's responsibility:

> 'action': 'Use the host native subagent tool with fresh context. Bind its actual returned ID, wait, then collect. Do not launch another model CLI.' if handoffs else work.get('action'),
> --- `src/wikiskill/native_agents.py`

Initial tracing covers production, maintenance, admission and consumption of retained state. Product `start` can inherit Wiki patterns, original feedback and a retained skill; `_load` replays journal events and validates referenced artifacts; `next_work` emits tasks or learning requests; `learn` commits sourced patterns; `propose` stages a candidate; `_advance` gates it; later requests carry the retained or candidate skill. Export and installation provide a further consumption path (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/native_agents.py`, `src/wikiskill/product_install.py`). Role instructions are included as doctrine, not treated as filesystem enforcement (SRC-1, `src/wikiskill/resources/product/roles/executor.md`, `src/wikiskill/resources/product/roles/maintainer.md`, `src/wikiskill/resources/product/roles/proposer.md`).

Research paths are also included. `engine.evolve` loads train/validation cases, invokes rollouts with the current skill, runs Maintainer and Proposer, gates a candidate, persists accepted skills and records impact history. The default role factories stage Wiki and training evidence and call the executor; the Spreadsheet rollout injects skill text into its task prompt. The isolated Spreadsheet driver separately orchestrates baseline, training, learning, candidate validation and final skill retention (SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/spreadsheet/rollout.py`, `src/wikiskill/spreadsheet/study.py`). The research contract confirms that its callers and drivers do not replace engine-owned admission:

> Adapters supply data, scored rollouts and validated role results; this engine
> still owns iteration, validation selection, rollback and experiment records.
> Callers must bind custom adapter sources/configuration in their manifest.
> --- `src/wikiskill/engine.py`

The frozen revision is `da6984caca09d5f81b2336cf3067b59c0c18bb1e`; applicability stops at 2026-10-15. Overall evidence is code-grounded, supplemented by source-authored doctrine and reported operation. No target execution, tests, provider calls or fresh experiments were performed. Source reports and bundled result artifacts remain attributed evidence until their contents and conditions are inspected; their presence does not establish an independently observed run or causal improvement.

### Shipped-path coverage

Every tracked top-level entry is classified below. “Included” establishes functional scope, not a claim that every descendant was read. Named inspected paths describe initial boundary tracing; available but unread files remain available to later source-grounded jobs, not access gaps. Entries whose contents were only inventoried cannot support behavioral conclusions yet. All locations in this table belong to SRC-1 at the registered revision.

| Top-level entry | Included or excluded | Role, initial inspection and limits |
|---|---|---|
| `.github/` | Included | Inventoried `workflows/tests.yml`; CI evaluation configuration is available but not yet inspected. No CI success claim. |
| `.gitignore` | Excluded | Repository housekeeping; exclusion prevents conclusions about ignored local artifacts, not shipped loop behavior. |
| `AGENTS.md` | Included | Inventoried source contributor/agent instructions; not yet inspected and not adopted as instructions for this analysis. No claim about contributor compliance. |
| `CHANGELOG.md` | Included | Inventoried release narrative, not yet inspected. No release-history finding. |
| `CONTRIBUTING.md` | Included | Inventoried development guidance, not yet inspected. No process-compliance finding. |
| `LICENSE` | Excluded | Legal terms, inventoried only; no licensing assessment. |
| `MANIFEST.in` | Included | Inventoried distribution selection, not yet inspected. Installed-wheel completeness is not established by the source tree. |
| `NOTICE.md` | Included | Inventoried provenance notices, not yet inspected. No independent provenance verification. |
| `README.md` | Included | Read product/research overview, external integration claims, installation and API descriptions; doctrine and attributed operation, not independent execution evidence. |
| `README_zh-CN.md` | Included | Inventoried alternate-language documentation, not yet inspected. No translation-equivalence claim. |
| `assets/` | Included | Inventoried evolution diagrams, workflow JSON and validation image; not yet inspected. No visual or workflow-JSON conformance finding. |
| `docs/` | Included | Read `code-navigation.md`; inventoried product guide, recovery, native subagents, reproduction, datasets, isolated study, research results, limitations and provenance files. These are source-native documentation/evaluation surfaces, not additional frozen sources. Other document contents are not yet inspected. |
| `examples/` | Included | Inventoried `text-cleanup/` and `workbook-delivery/` task sets, scorers and workbook inputs; read `text-cleanup/score.py` to establish a shipped evaluation consumer. Other example contents are not yet inspected; no workbook-example success claim. |
| `pyproject.toml` | Included | Read package dependencies, console entry, optional extras and package-data patterns. Establishes declared entry point, not installation success. |
| `scripts/` | Included | Inventoried research recomputation checks, snapshot import, plotting and native-asset synchronization. Bodies not yet inspected; no recomputed-result or synchronization-correctness claim. |
| `skills/` | Included | Read `wikiskill/SKILL.md`; inventoried host metadata and `references/workflow.md`, `references/native-subagents.md`. Main skill supplies shipped orchestration and later-consumption instructions; reference bodies not yet inspected. |
| `src/` | Included | Read `wikiskill/cli.py`; inspected product state replay, inheritance, work issuance, maintenance, proposal, scoring, gate, export; read `feedback_loop.py`, `native_agents.py`, `results.py`, `skill_proposer.py`; inspected `mcp_server.py`, `product_install.py`, `engine.py`, `wiki_maintainer.py`, `officeqa/wiki_agents.py`, `spreadsheet/rollout.py`, `spreadsheet/study.py`; read all three `resources/product/roles/*.md`. Inventoried `product_cli.py`, `product_views.py`, `scorer_trust.py`, `score_rules.py`, `wiki.py`, domain adapters/rollouts/scorers, `paper_alignment/`, `isolated/`, runtime tools and packaged resources. These remain included: domain datasets/splits, Wiki seed files and maintenance prompts, paper prompts, host role definitions, research score/skill artifacts and runtime support. Unread bodies require inspection before detailed claims about particular adapters, prompt equivalence, security or measured results. |
| `tests/` | Included | Inventoried product/native-agent/MCP, research engine, scoring, isolation, domain, paper-contract and workbook tests and fixtures. Test contents not yet inspected and tests not run; no passing-test inference. |
| `third_party/` | Included | Inventoried Acorn and OfficeQA notices/licenses as provenance dependencies; contents not yet inspected. Their presence does not verify provenance or runtime safety. |

External dependencies and exclusions are functional, not hidden subtractions from the shipped repository. The host's native subagent implementation, model inference services, credentials, user task corpora, user-selected scorer programs and optional tools such as LibreOffice are not frozen here. They prevent conclusions about actual host isolation, inference availability, evaluation validity on arbitrary user tasks, and end-to-end reproducibility without further evidence. Shipped host roles, scorer interfaces, domain drivers and isolated-runtime policy code remain included. BriefLoop is described only by this repository's claims; its code and application-specific evaluator are outside the source set, so no independent conclusion about its deployed learning behavior is available (SRC-1, `README.md`, `pyproject.toml`, `src/wikiskill/native_agents.py`, `src/wikiskill/product.py`, `src/wikiskill/product_install.py`). The original paper and linked websites were not acquired and cannot supply evidence for this run.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Stahl-G/WikiSkill` | da6984caca09d5f81b2336cf3067b59c0c18bb1e | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-baafad05d35e/related-systems/Stahl-G--WikiSkill`. Implementation: `pyproject.toml`, `src/wikiskill/cli.py`, selected ranges of `src/wikiskill/product.py`, `src/wikiskill/engine.py`, `src/wikiskill/mcp_server.py`, `src/wikiskill/product_install.py`, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/spreadsheet/rollout.py`, `src/wikiskill/spreadsheet/study.py`; full `src/wikiskill/native_agents.py`, `src/wikiskill/feedback_loop.py`, `src/wikiskill/skill_proposer.py`, `src/wikiskill/results.py`, `examples/text-cleanup/score.py`. Doctrine/design: `README.md`, `docs/code-navigation.md`, `skills/wikiskill/SKILL.md`, `src/wikiskill/resources/product/roles/executor.md`, `src/wikiskill/resources/product/roles/maintainer.md`, `src/wikiskill/resources/product/roles/proposer.md`. Reported operation: README's research and host-integration claims only. Entire tracked tree inventoried; initial paths are not an allowlist. | Implementation: [CLI](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/src/wikiskill/cli.py), [product](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/src/wikiskill/product.py), [research engine](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/src/wikiskill/engine.py), [feedback API](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/src/wikiskill/feedback_loop.py). Doctrine: [entry skill](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/skills/wikiskill/SKILL.md). Reported operation: [README](https://github.com/Stahl-G/WikiSkill/blob/da6984caca09d5f81b2336cf3067b59c0c18bb1e/README.md). | No access gap encountered in the checkout. External hosts, services, application code and user datasets are not captured. No independently inspected live trace or intervention/comparison is established by this boundary; implementation and source reports alone do not prove deployed isolation, reproducibility or general improvement. |
