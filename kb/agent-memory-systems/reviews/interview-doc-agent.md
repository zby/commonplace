---
description: "interview-doc-agent review: single-file job-document skill using a Markdown experience library, index-first lookup, templates, and JD-conditioned outputs"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
---

# interview-doc-agent

`Shilren/interview-doc-agent` is a Chinese-language AI skill for turning scattered job-search material into a maintained "experience library" and then generating resumes, interview scripts, and JD-tailored variants. It is not a runtime package or retrieval engine; the reviewed system is a single `SKILL.md` instruction artifact plus a Markdown workspace convention for `materials/`, `经历库/`, `wiki/index.md`, `templates/`, `jd/`, and `output/`.

**Repository:** https://github.com/Shilren/interview-doc-agent

**Reviewed commit:** [db4da8f7dd1065e725bff1b185c6dbbdb2425276](https://github.com/Shilren/interview-doc-agent/commit/db4da8f7dd1065e725bff1b185c6dbbdb2425276)

**Last checked:** 2026-06-03

## Core Ideas

**The product is an installable instruction file.** The README says normal use only requires downloading `SKILL.md`, with examples for Obsidian/Claudian, Claude Code, and Feishu/Lark intelligent partners ([README.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/README.md)). The skill frontmatter names one ability bundle: generate job-search documents for product-manager and broader interview scenarios from templates, an experience library, and target JDs ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md)).

**The memory model is a three-layer LLM wiki adapted to job-search prep.** Raw materials go into `materials/`, the AI distills them into polished experience records under `经历库/`, and generated resumes/interview scripts go to `output/`; target JDs in `jd/` steer customization back over the same experience library ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [docs/01-理念-karpathy-wiki.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/01-%E7%90%86%E5%BF%B5-karpathy-wiki.md)). The explicit design claim is Karpathy-style "settling" of knowledge into a wiki layer instead of repeated retrieval from raw dumps.

**The experience library is the single source for generated claims.** The skill instructs agents to treat `经历库/` as the main source, to preserve every quantitative datum during extraction, to use placeholders for missing data, and to avoid inventing numbers ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [docs/04-使用指南.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/04-%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md)). The bundled example record shows the target shape: one-line summary, background judgment, problem definition, methods/results, quick-access metrics, persona highlights, and follow-up material ([经历库/01-示例经历.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/%E7%BB%8F%E5%8E%86%E5%BA%93/01-%E7%A4%BA%E4%BE%8B%E7%BB%8F%E5%8E%86.md)).

**Context efficiency is index-first file selection, not RAG.** `wiki/index.md` is a lightweight routing table: the agent reads it first, then reads only the relevant one or two experience records and templates rather than all raw materials ([wiki/index.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/wiki/index.md)). The design document argues that a personal experience library is usually only thousands to tens of thousands of tokens, so whole-file context over curated Markdown is simpler and more reliable than vector search, chunking, or embeddings ([docs/01-理念-karpathy-wiki.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/01-%E7%90%86%E5%BF%B5-karpathy-wiki.md)).

**Templates are style and structure memory.** Resume generation reads `templates/简历/` for layout and compact bullet style; interview-script generation reads `templates/逐字稿/产品面试话术模版.md` for the background -> problem definition -> methods/results narrative shape ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [templates/简历/简历模板.示例.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/templates/%E7%AE%80%E5%8E%86/%E7%AE%80%E5%8E%86%E6%A8%A1%E6%9D%BF.%E7%A4%BA%E4%BE%8B.md), [templates/逐字稿/产品面试话术模版.示例.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/templates/%E9%80%90%E5%AD%97%E7%A8%BF/%E4%BA%A7%E5%93%81%E9%9D%A2%E8%AF%95%E8%AF%9D%E6%9C%AF%E6%A8%A1%E7%89%88.%E7%A4%BA%E4%BE%8B.md)). That makes templates behavior-shaping context, not just examples.

**Adoption is deliberately platform-light.** The Obsidian guide maps the system to local Markdown files and Claudian skills, while the Feishu guide maps the same instruction file and folder roles to knowledge-base pages or Base records ([docs/02-安装-obsidian.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/02-%E5%AE%89%E8%A3%85-obsidian.md), [docs/03-接入-飞书.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/03-%E6%8E%A5%E5%85%A5-%E9%A3%9E%E4%B9%A6.md)). There is no database, API key, package install, or local helper script in the reviewed checkout.

## Artifact analysis

- **Storage substrate:** `files` — The standing memory is a file tree: `SKILL.md`, `materials/`, `经历库/`, `wiki/index.md`, `templates/`, `jd/`, and `output/`.
- **Representational form:** `prose` — Markdown prose dominates: raw dumps, distilled experience narratives, interview/resume templates, JD text, generated documents, and the skill instructions; the index table and directory convention add light symbolic routing.

**`SKILL.md` instruction artifact.** Storage substrate is a single Markdown file installed into a host skill location or pasted into a platform instruction field. Representational form is prose with YAML frontmatter, directory conventions, and stepwise procedures. Lineage is authored from the Karpathy LLM Wiki pattern and specialized for job-search documents. Behavioral authority is system-definition authority when a compatible host loads it: it tells the agent which files to create, read, update, and write, and it sets generation constraints such as "do not invent data."

**Raw materials.** Storage substrate is `materials/` or its platform equivalent. Representational form is arbitrary prose: project retrospectives, PRD fragments, work reports, chat records, brainstorm notes, or copied data ([materials/README.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/materials/README.md)). Lineage is user-supplied source material. Behavioral authority is knowledge-artifact authority as evidence and detail backfill; the skill says materials are consulted only when the experience library lacks detail.

**Experience library and personal profile.** Storage substrate is `经历库/` Markdown files, including the personal-profile template and per-experience records. Representational form is structured prose: personal metadata, persona keywords, one-line summaries, three-part interview narratives, method/result sections, quick metrics, and follow-up material. Lineage is distilled from raw materials by the acting AI, then maintained as the main source for future outputs. Behavioral authority is knowledge-artifact authority as source context, with stronger practical authority because the skill instructs generated documents to use these records as the single trusted source for facts and numbers.

**`wiki/index.md`.** Storage substrate is one Markdown index file. Representational form is a symbolic/prose routing table mapping templates, experience records, raw-material fallback, and outputs. Lineage is manually initialized and then updated when experiences are added. Behavioral authority is routing authority: it decides which experience files and templates the agent should read first, but it does not itself supply the substantive claims.

**Templates and JD files.** Storage substrate is `templates/简历/`, `templates/逐字稿/`, and `jd/`. Representational form is prose examples and target-job prose. Lineage is user- or repo-supplied. Behavioral authority is system-definition and ranking-like advice: templates constrain style and structure, while JD files select and reorder which experience-library facts should be emphasized.

**Generated outputs.** Storage substrate is `output/`. Representational form is prose documents, optionally with LaTeX if the user supplies or requests a formal resume template. Lineage is derived from the experience library, selected templates, and optional JD files. Behavioral authority is mostly end-user artifact authority outside the agent loop; outputs do not feed later behavior unless the user promotes them back into materials, templates, or the experience library.

The promotion path is source material -> distilled experience record -> index exposure -> resume/interview/JD-specific output. It is a soft prose promotion path with no validator, schema, or source-span checker beyond the skill's instructions and human review.

## Comparison with Our System

| Dimension | interview-doc-agent | Commonplace |
|---|---|---|
| Primary purpose | Maintain a personal job-search experience library and generate resumes/interview scripts | Maintain a methodology KB for agent-operated knowledge systems |
| Main retained artifact | Markdown experience records plus index, templates, raw materials, and outputs | Typed Markdown notes, instructions, reviews, sources, indexes, and validation reports |
| Context strategy | Read `wiki/index.md`, then one or two relevant experience records and templates | Search, generated indexes, collection contracts, type specs, links, skills, and review gates |
| Authority model | Skill prose plus "experience library as single trusted source" convention | Explicit artifact types, collection contracts, validation, semantic review, and git lifecycle |
| Governance | Human review and instruction compliance; no executable checks | Deterministic validation, review bundles, schemas, generated indexes, and replacement archives |
| Adoption surface | Single skill file for Obsidian, Claude Code, Feishu/Lark, or any file-reading AI | Repository framework plus installed `commonplace-*` commands and collection-local skills |

The strongest alignment is the compiled-source pattern. Both systems try to avoid repeatedly feeding raw material to an agent by distilling it into a maintained Markdown layer and then routing future work through an index. `interview-doc-agent` is a small, domain-specific instance of that pattern: it shows how far a single skill plus simple folders can go when the domain is narrow and the corpus is small.

The largest divergence is governance. Commonplace treats the type, status, source, validation, and review lifecycle as part of the artifact. `interview-doc-agent` treats the experience library as trusted by convention: the skill tells the agent not to invent numbers and to use placeholders for missing data, but there is no executable check that every generated bullet is grounded in an experience record.

`interview-doc-agent` is stronger on adoption friction. A non-programmer can paste one skill into Obsidian/Claudian or Feishu and work with ordinary documents. Commonplace's richer taxonomy and validation surface would be overkill for this personal-document workflow unless the user needed auditability, collaboration, or repeated agent maintenance.

**Read-back:** `pull` — The retained experience library reaches the agent when the agent follows the skill, opens `wiki/index.md`, and deliberately reads selected experience records and templates; the always-loaded part is the lookup instruction, not selected retained memory.

### Borrowable Ideas

**A domain-specific "single trusted source" phrase.** Ready now. Commonplace already has source and artifact authority vocabulary, but `经历库是主来源` is a crisp user-facing rule: generated outputs should name which retained artifact is the factual source rather than treating all nearby text equally.

**Index-first, whole-file lookup for small corpora.** Ready for scoped workspaces. The repo's anti-RAG argument is sound for small, curated libraries: use an index and whole Markdown files until volume or update rate justifies heavier retrieval machinery.

**Separate style templates from factual memory.** Ready now. Resume/interview templates constrain form, while experience records constrain facts. Commonplace can preserve that split in drafting workflows: exemplars should shape style without becoming evidence.

**Use placeholders as an anti-hallucination contract.** Ready as a writing convention. The skill's `___` rule is a concrete way to keep missing information visible instead of letting the agent smooth over gaps.

**Do not borrow prose-only grounding for higher-authority artifacts.** For job documents, human review may be enough. For Commonplace instructions, validators, or reviews, the same "trust the skill" pattern would be too weak without citations, validation, and review.

## Curiosity Pass

**The repository has almost no executable implementation to inspect.** That is appropriate for a promptware skill, but it means code-grounded review can only verify the specified workflow, examples, and folder contract, not runtime compliance by Obsidian, Claude Code, Feishu, or another host.

**The "single source" guarantee is procedural, not enforced.** The skill says all outputs should come from the experience library and real missing data should become `___`, but generated documents in `output/` are not checked against source records.

**The index is intentionally weak.** `wiki/index.md` is just a routing table, not search infrastructure. That is a feature for the intended scale, but it means file naming and manual index updates carry most of the retrieval quality.

**Trace-derived status is not supported at this commit.** The system distills user-supplied raw materials into experience records. Those materials may include chat records or work logs, but the repo does not show agent execution traces, session transcripts, tool trajectories, or rollouts being mined into durable behavior-shaping artifacts.

**The Feishu path weakens the file-system contract.** The docs explain how to map folders to Feishu knowledge-base pages or Base records, but write-back permissions depend on the user's Feishu version and enterprise settings ([docs/03-接入-飞书.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/03-%E6%8E%A5%E5%85%A5-%E9%A3%9E%E4%B9%A6.md)). The architecture is portable, but the behavioral guarantee shifts to the host.

## What to Watch

- Whether the project adds a lightweight grounding checker for generated resumes and scripts; that would turn the "do not invent data" instruction into an auditable rule.
- Whether `wiki/index.md` gains required fields such as source material path, last-updated date, data-completeness score, and JD tags; that would make selection and stale detection less dependent on prose discipline.
- Whether the Feishu/Lark path gets an implemented connector or Base schema; that would move the system from platform mapping guidance to a concrete multi-host memory substrate.
- Whether users start adding many experience records; that is the point where file naming, index quality, and context budgets become more important than the current "read one or two files" heuristic.
- Whether generated outputs ever feed back into the experience library as revised self-presentation. If that loop becomes explicit, the review should distinguish factual source memory from polished narrative memory.

Relevant Notes:

- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - aligns: distilled experience records precompute source understanding so future resume/interview generation avoids rereading raw dumps.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: the experience library matters only when the skill's index-first lookup path brings selected records into context.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: materials, experience records, JD files, templates, and generated outputs advise or evidence later generation depending on the consumption path.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `SKILL.md`, the index-first rule, template-selection rules, and anti-fabrication instructions shape the agent's behavior.
- [Distillation](../../notes/definitions/distillation.md) - exemplifies: raw career material is transformed into compact, use-shaped experience records for downstream resume and interview tasks.
- [Context engineering](../../notes/definitions/context-engineering.md) - relates: the repo is a small context-engineering system whose main mechanism is routing from index to selected whole files.
