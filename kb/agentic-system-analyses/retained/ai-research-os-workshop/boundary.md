---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AI Research OS Workshop's shipped research-memory plugin and helper scripts at dc6660555266239cd36483cf51b5ab39febacf02."
run-id: AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: dc6660555266239cd36483cf51b5ab39febacf02
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/iusztinpaul/ai-research-os-workshop
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/ai-research-os-workshop-1a93869f8e7f/related-systems/iusztinpaul--ai-research-os-workshop
  revision: dc6660555266239cd36483cf51b5ab39febacf02
  sha256: null
---

# AI Research OS Workshop boundary

## Boundary and evidence

This run analyses the shipped local research-memory plugin, not an independent agent runtime or the production system advertised by its authors. Its intended use is to preserve research across sessions as a topic-scoped Markdown wiki and catalog that an agent can extend and consult. It qualifies as a **memory/knowledge/context-engineering system** because its shipped prompts direct model-mediated source selection, synthesis, maintenance and later retrieval of retained knowledge. The executable helper scripts support those workflows; they do not themselves own the enclosing model loop. SRC-1: `README.md`, `plugins/ai-research-os/skills/research/SKILL.md`.

> `AI Research OS` is a set of local AI skills for building and querying a persistent research wiki from your own sources:
> --- `README.md`

> The point is not to replace Codex. The point is to stop re-researching the same topic
> every week.
> --- `README.md`

The boundary is **whole-system** for this shipped plugin. It includes the marketplace registration, plugin manifest, four research entry skills, their agent prompts, data conventions, source-connector usage skills and local Python helpers. It follows the material loop from request routing and admission through source discovery/copying, wiki synthesis, canonical catalog persistence, later query/save-back, lint maintenance and distill/render consumption. The shipped orchestration prompts are part of the target, not excluded callers of the Python scripts. SRC-1: `.claude-plugin/marketplace.json`, `plugins/ai-research-os/.claude-plugin/plugin.json`, `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/CONVENTIONS.md`.

> The data contract for research directories. The `/research`, `/research-lint`, `/research-distill`, and `/research-render` skills all read and write against this layout. If you're operating on a research dir, this file is authoritative — when a SKILL.md and CONVENTIONS.md disagree, CONVENTIONS.md wins.
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

Initial tracing established these shipped responsibilities:

- `/research` routes init, append, deep and query requests; ingestion is directed through researcher, gap-analyzer, GitHub-spec, builder, source-page and synthesis-page prompts. The builder persists source material, while the orchestrator calls the index builders after wiki generation. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research/agents/source_writer.md`.
- The YAML builder reads discovery/seed JSON and optionally a prior catalog, preserves prior sources not superseded by matching `original_path`, and writes the canonical catalog. The Markdown builder reloads that catalog and scans the wiki tree to generate its navigation view. These are inspected implementation paths, not merely README intentions. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.
- Later query requests reload the catalog and follow pointers into source pages, wiki synthesis, highlights or full content. The query prompt also contains knowledge-document and question-pointer save-back instructions. Its opening write prohibition and later save-back instructions are both within scope; this boundary does not resolve their consistency. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.
- `/research-lint` combines mechanical checks with model-mediated contradiction, stale-claim and open-question judgments. It is a shipped maintenance/evaluation path, not evidence of measured research quality. Distill reads retained research against user content and exports a compact appendix; render delegates wiki consumption to format-specific writers and regenerates navigation. SRC-1: `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`, `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`, `plugins/ai-research-os/skills/research-distill/SKILL.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`.

> Read `<research_dir>/index.yaml`. The YAML is canonical and has the full schema. The MD is for humans browsing in Obsidian.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

### Top-level coverage

Every tracked top-level entry was inventoried. “Included” means part of the functional boundary, not that every line has already been analysed. Partial initial inspection below is not an access gap: all tracked blobs are available at the pin. No material shipped persistence, maintenance or consumption path was found inaccessible.

| Tracked entry | Treatment and material paths | Initial inspection and role | Exclusion or remaining limit |
|---|---|---|---|
| `.claude-plugin/` | Included: `marketplace.json` | Read fully; routes plugin installation to `plugins/ai-research-os`. SRC-1: `.claude-plugin/marketplace.json`. | Does not establish actual installation or host discovery. |
| `.gitignore` | Included as repository support metadata | Read fully; ignores local Python environments/caches and OS files. SRC-1: `.gitignore`. | Not a research-state persistence policy. |
| `DEPENDENCIES.md` | Included | Read fully; declares inline-script dependencies, external CLI/auth requirements and vault assumptions. SRC-1: `DEPENDENCIES.md`. | Dependency availability and connector success were not observed. |
| `LICENSE` | Excluded: licensing text | Inventoried, not read; not a state producer, maintainer or consumer. | No licensing assessment. |
| `README.md` | Included | Read fully; installation, entry skills, architecture, source types, query usage and output layout. SRC-1: `README.md`. | Marketing/comparison assertions are attributed intent, not measured advantages. Linked slides, video and course are outside the frozen source. |
| `examples/` | Included as illustrative inputs/artifact layout, not as independent validation: `example_1_deep_research/`, `example_2_github/`, `example_3_ingest_links/` | Tracked tree inventoried; GitHub example prompt read as a shipped invocation requesting ingestion without discovery. SRC-1: `examples/example_2_github/prompt.md`. Generated wiki bodies and other example prompts have not been inspected. | No execution trace, reproducibility or factual-quality conclusion from example outputs. No characterization of the other systems described in those artifacts. |
| `media/` | Excluded: `course_clip.gif` and README illustration PNGs | Inventoried; presentation assets, not workflow code or retained research-state drivers. | No visual-output or UI-quality assessment. |
| `plugins/` | Included: `ai-research-os/.claude-plugin/plugin.json`; `skills/research/` including `CONVENTIONS.md`, `agents/` and `scripts/`; `skills/research-lint/` including judge and mechanical scripts; `skills/research-distill/`; `skills/research-render/` including four writer prompts; `skills/obsidian-cli/`, `skills/readwise-cli/`, `skills/nlm-skill/` and its references | Manifest and main data contract read; research routing/query, GitHub path and wiki/index construction inspected in bounded sections; builder/source-writer, lint and distill prompts read fully; render dispatch/index sections read. Index-builder implementations read fully; broken-link checker read fully; remaining agent/helper responsibilities searched at their input/output and file-read/write anchors. Obsidian skill read fully; Readwise/NotebookLM opening contracts read. SRC-1: `plugins/ai-research-os/.claude-plugin/plugin.json`, `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-distill/SKILL.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`. | Included beyond initial inspected ranges: full discovery/connector recipes, all synthesis/format agent bodies, extraction/cache/dedup helpers, other mechanical checkers and NotebookLM reference documents. Later analysis may inspect them at this same pin. Their presence alone proves neither successful operation nor enforcement of prompt rules. |
| `pyproject.toml` | Included as dependency/package metadata | Read fully; local dependency declarations, Python minimum and `package = false`. SRC-1: `pyproject.toml`. | Not evidence of an independent installed runtime. |
| `uv.lock` | Excluded from operational mechanism analysis | Inventoried, not read; development dependency lock. SRC-1: `DEPENDENCIES.md` distinguishes inline-script environments from root development setup. | No exact resolved-environment or supply-chain assessment. |

### External dependencies and evidence limits

Claude Code or Codex supplies model inference, tool execution, agent dispatch and the enclosing session. Those hosts are external dependencies, not implementations shipped here. Their scheduler, permissions, sandboxing, context lifecycle and guarantees must not be attributed to this plugin. The bundled source CLI skills are included instruction artifacts; the Obsidian, Readwise and NotebookLM binaries/services and their authentication behavior are excluded implementations. Git, curl, Python, uv, extraction libraries and optional rendering/viewer dependencies likewise supply external execution capability. SRC-1: `README.md`, `DEPENDENCIES.md`, `plugins/ai-research-os/skills/obsidian-cli/SKILL.md`, `plugins/ai-research-os/skills/readwise-cli/SKILL.md`, `plugins/ai-research-os/skills/nlm-skill/SKILL.md`.

> The root `pyproject.toml`
> is kept for local dev convenience only — the skills do not rely on it.
> --- `DEPENDENCIES.md`

The frozen evidence is the acquired Git repository at **dc6660555266239cd36483cf51b5ab39febacf02**, with applicability cutoff **2026-10-12**, the supplied run date. HEAD was checked against the supplied pin and the checkout inspected read-only. No additional repository, linked live page or capture is registered. The overall tier is **code-grounded** because executable index and lint paths were inspected alongside the prompt contracts. Model-directed orchestration remains doctrine/design evidence unless supported by executable implementation or a retained run artifact. This run neither executes target scripts nor calls providers or source services. It cannot establish prompt compliance, successful end-to-end updates, long-term research quality, actual latency or causal performance benefits.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/iusztinpaul/ai-research-os-workshop` | dc6660555266239cd36483cf51b5ab39febacf02 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/ai-research-os-workshop-1a93869f8e7f/related-systems/iusztinpaul--ai-research-os-workshop`. Implementation: complete `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py`, `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`; bounded input/output searches in remaining research helpers and lint scripts. Doctrine/design: complete README, dependency document, manifests, conventions, builder/source-writer prompts, lint skill/judge, distill skill, Obsidian skill and GitHub example prompt; bounded research routing/query/GitHub/build sections, render dispatch/index sections, Readwise/NotebookLM opening contracts and remaining agent responsibility searches. | Implementation: [YAML index builder](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research/scripts/build_index_yaml.py), [Markdown index builder](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research/scripts/build_index_md.py), [broken-link checker](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py). Doctrine/design: [research driver](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research/SKILL.md), [data contract](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research/CONVENTIONS.md), [lint driver](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/plugins/ai-research-os/skills/research-lint/SKILL.md), [README](https://github.com/iusztinpaul/ai-research-os-workshop/blob/dc6660555266239cd36483cf51b5ab39febacf02/README.md). | No inaccessible material tracked path established. Host/service implementations and linked course/slides/video are outside the source boundary, preventing conclusions about their internals. No observed-run or causal-experiment layer established; generated examples are not treated as execution verification. Available but uninspected material is distinguished in the coverage table and remains inspectable at this commit. |
