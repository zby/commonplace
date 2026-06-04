---
description: "interview-doc-agent review: single-file job-document skill using a file-native experience library, templates, and index-guided context"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# interview-doc-agent

`interview-doc-agent`, from Shilren's `interview-doc-agent` repository, is a Chinese-language AI skill for turning raw job-search experience material into a maintained "experience library" and then generating resumes, interview scripts, and JD-tailored variants. The inspected repository is mostly a portable `SKILL.md` plus folder conventions, examples, templates, and setup docs for Obsidian/Claudian, Claude Code, Feishu/Lark, and similar file-capable agents; I did not find an executable package, API server, vector index, or model-training component.

**Repository:** https://github.com/Shilren/interview-doc-agent

**Reviewed commit:** [db4da8f7dd1065e725bff1b185c6dbbdb2425276](https://github.com/Shilren/interview-doc-agent/commit/db4da8f7dd1065e725bff1b185c6dbbdb2425276)

**Last checked:** 2026-06-04

## Core Ideas

**The skill is the system boundary.** The README says the skill body is `SKILL.md` and that users do not need to clone the whole repository for ordinary use; installation copies that one file into a host skill location or prompt box ([README.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/README.md)). `SKILL.md` is therefore the central system-definition artifact: it tells any compatible file-reading agent how to initialize folders, update the experience library, read templates, and write outputs ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md)).

**The memory model is a small LLM-wiki, not RAG.** The repository maps raw user dumps to `materials/`, distilled interview-ready records to `经历库/`, a lightweight locator table to `wiki/index.md`, and generated documents to `output/` ([docs/01-%E7%90%86%E5%BF%B5-karpathy-wiki.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/01-%E7%90%86%E5%BF%B5-karpathy-wiki.md)). Its design note explicitly rejects vector RAG for this scale: a personal experience library is expected to be a few thousand to tens of thousands of tokens, so the agent should read whole relevant Markdown files instead of chunking and embedding them.

**Context efficiency is index-guided file selection.** `SKILL.md` instructs the agent to read `wiki/index.md` first, then only the relevant experience records plus templates, using `materials/` only as a fallback when the distilled library lacks detail ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [wiki/index.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/wiki/index.md)). This is cheap lexical/navigation discipline rather than a retrieval engine: the index lists paths and keywords, and the host agent reads complete Markdown records.

**The experience library is the single trusted source for downstream documents.** The skill describes `经历库/` as the generation main source, with each project record shaped into a one-sentence summary, three-part interview narrative, quick data lookup, and persona highlights. Resume, interview-script, and JD-tailoring workflows all draw from that layer so numbers and claims stay aligned ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [%E7%BB%8F%E5%8E%86%E5%BA%93/00-%E4%B8%AA%E4%BA%BA%E6%A1%A3%E6%A1%88.%E6%A8%A1%E6%9D%BF.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/%E7%BB%8F%E5%8E%86%E5%BA%93/00-%E4%B8%AA%E4%BA%BA%E6%A1%A3%E6%A1%88.%E6%A8%A1%E6%9D%BF.md)).

**Trust is instruction-level, not enforced by code.** The skill repeatedly instructs the agent not to fabricate quantitative data and to use `___` placeholders when real data is missing ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md), [docs/04-%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/docs/04-%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md)). I found no validator, citation checker, schema, or deterministic gate that proves generated resumes and scripts stayed faithful to the experience library.

## Artifact analysis

- **Storage substrate:** `files` — The retained behavior-shaping state is file-backed: `SKILL.md`, docs, templates, `materials/`, `经历库/`, `jd/`, `output/`, and `wiki/index.md` live as local Markdown or template files in a vault/repo/cloud-document analogue.
- **Representational form:** `prose` `symbolic` — Instructions, templates, raw materials, experience records, and generated documents are prose; directory conventions, path names, frontmatter, tables in `wiki/index.md`, placeholder tokens, and workflow steps are symbolic. I found no parametric memory.
- **Lineage:** `authored` `imported` — `SKILL.md`, docs, templates, example records, and index scaffolds are authored; user job materials and JDs are imported; generated experience records are distilled from imported materials by the host agent under the skill's prose instructions.
- **Behavioral authority:** `knowledge` `instruction` `routing` — Experience records, templates, raw materials, and JDs act as knowledge; `SKILL.md` instructs the host agent; `wiki/index.md`, personal-profile indexes, folder names, and JD matching route attention toward the relevant records. Anti-fabrication and formatting rules are instructions, not code-enforced validation.

**Skill instructions.** `SKILL.md` has the strongest authority because compatible hosts are expected to read it as the operating procedure. It defines initialization, resume generation, interview-script generation, JD tailoring, experience-library update rules, and anti-fabrication behavior ([SKILL.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/SKILL.md)).

**Experience library and personal profile.** `经历库/` holds the durable distilled records that future resumes and scripts should use as the main source. The profile template includes personal information, persona keywords, and an experience index, making it both a knowledge artifact and a routing surface ([%E7%BB%8F%E5%8E%86%E5%BA%93/00-%E4%B8%AA%E4%BA%BA%E6%A1%A3%E6%A1%88.%E6%A8%A1%E6%9D%BF.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/%E7%BB%8F%E5%8E%86%E5%BA%93/00-%E4%B8%AA%E4%BA%BA%E6%A1%A3%E6%A1%88.%E6%A8%A1%E6%9D%BF.md)).

**Index and templates.** `wiki/index.md` is a lightweight locator table rather than a search index in the vector/RAG sense. Templates under `templates/` carry writing-style authority for resumes and interview scripts, especially the three-part product-interview script format ([wiki/index.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/wiki/index.md), [templates/%E9%80%90%E5%AD%97%E7%A8%BF/%E4%BA%A7%E5%93%81%E9%9D%A2%E8%AF%95%E8%AF%9D%E6%9C%AF%E6%A8%A1%E7%89%88.%E7%A4%BA%E4%BE%8B.md](https://github.com/Shilren/interview-doc-agent/blob/db4da8f7dd1065e725bff1b185c6dbbdb2425276/templates/%E9%80%90%E5%AD%97%E7%A8%BF/%E4%BA%A7%E5%93%81%E9%9D%A2%E8%AF%95%E8%AF%9D%E6%9C%AF%E6%A8%A1%E7%89%88.%E7%A4%BA%E4%BE%8B.md)).

**Promotion path.** The promotion path is raw user material -> distilled experience-library record -> index update -> generated resume/script/JD-tailored output. It does not promote records into validators, executable tools, embeddings, or ranked learned models.

## Comparison with Our System

| Dimension | interview-doc-agent | Commonplace |
|---|---|---|
| Primary purpose | Personal job-search document generation | Methodology KB for agent-operated knowledge bases |
| Main retained artifact | File-native skill instructions, experience records, templates, and index | Typed Markdown notes, reviews, instructions, sources, schemas, indexes, and commands |
| Write path | Host agent distills user materials into `经历库/` and generated outputs | Human/agent-authored artifacts governed by collection contracts, validation, review, and git |
| Read path | Agent reads index, selected experience records, templates, and JDs on demand | Agents navigate through `rg`, indexes, links, collection contracts, skills, and validation/report outputs |
| Governance | Prose instructions: single trusted source, no fabricated data, placeholders for gaps | Deterministic validation, type specs, link checks, review gates, and source-grounded citations |

The alignment with Commonplace is the file-native "library before generation" pattern. `interview-doc-agent` does not ask the agent to regenerate from raw dumps every time; it creates a durable intermediate layer and then uses that layer for repeated downstream work. Commonplace uses the same broad move, but with stronger typed frontmatter, validation, source citation, and review machinery.

The main divergence is authority. In `interview-doc-agent`, the host model is trusted to follow `SKILL.md`, preserve all quantitative data, update indexes, and avoid fabrication. Commonplace pushes more of that behavior into explicit type contracts, deterministic checks, generated indexes, and review workflows.

### Borrowable Ideas

**A tiny domain skill can be enough when the corpus is small.** Ready now as a reminder. Commonplace does not need vector or graph machinery for every local workflow; a good folder contract plus index can be the right abstraction for small, stable corpora.

**Make the intermediate layer the product, not just a cache.** Ready now. The experience library is useful because it is interview-ready, structured, and reusable, not because it is a hidden retrieval artifact. Commonplace should keep treating durable Markdown artifacts as maintained products.

**Use placeholders as an anti-fabrication convention.** Ready for prose-heavy generation tasks. `___` placeholders for missing facts are a simple way to keep absence visible when deterministic validation is not available.

**Do not borrow the weak governance as-is.** Needs stronger checks for Commonplace. A Commonplace analogue would need type validation, source links, and review state before agent-distilled personal or operational records gained durable authority.

## Write side

**Write agency:** `manual` `automatic` — Users manually add raw materials, templates, and JDs, and can edit the library directly; the host agent, when instructed by the skill, can initialize folders, distill `materials/` into `经历库/`, update `00-个人档案.md` and `wiki/index.md`, and write generated documents to `output/`.

**Curation operations:** `not-determinable` — The repository gives prose instructions for distilling and integrating new raw material, but I found no executable curation implementation that deterministically performs the controlled curation operations on existing stored entries. Creating experience records from raw materials is acquisition/import, while updating the index is access-structure upkeep.

## Read-back

**Read-back:** `pull` — Retained experience-library memory re-enters future work when the host agent deliberately reads `wiki/index.md`, then selected `经历库/` records, templates, and JD files in response to a user request; I found no hook, always-load memory injector, event trigger, or relevance engine that pushes retained records into context without that file-read workflow.

The static skill text itself may be loaded by a host as baseline instruction, but that is not read-back of accumulated user memory. The memory-specific path is explicit navigation over files. Context volume is bounded by the index-first convention and by reading relevant records rather than the whole raw-material layer, but actual selection quality depends on the host agent and the maintained index.

## Curiosity Pass

**The repo is closer to a portable agent operating manual than an application.** Its strongest claim is that a single `SKILL.md` plus folders can carry a useful personal KB workflow across Obsidian, Feishu, Claude Code, Cursor, and similar hosts.

**The "no RAG" argument is appropriate but relies on corpus discipline.** The design works if the experience library stays small and well indexed. If users accumulate many loosely maintained records, the index becomes the real bottleneck because there is no fallback ranking engine.

**The anti-fabrication rule is important but soft.** The skill tells the agent to preserve all numbers and use placeholders for missing data. Without a checker comparing generated output against `经历库/`, faithfulness remains a host-model behavior, not an implemented guarantee.

**The library/output boundary is clean.** `经历库/` is the reusable memory layer and `output/` is disposable generation. That distinction is simple and worth preserving in small agent-operated KBs.

## What to Watch

- Whether the project adds a deterministic verifier that checks generated resumes and scripts against `经历库/` numbers and flags unsupported claims.
- Whether `wiki/index.md` gains a more structured schema for capability tags, project names, metrics, and JD-match dimensions as user libraries grow.
- Whether the Feishu/Lark path becomes an implemented connector rather than prose mapping guidance; that would change storage substrate and write/read authority.
- Whether the skill adds source pointers from distilled experience-library bullets back to `materials/`; that would make the intermediate layer more auditable.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: `interview-doc-agent` stores experience memory, but read-back happens only when the agent navigates the files.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: skill instructions, experience records, raw materials, templates, and indexes differ by form and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: experience records, templates, JDs, and raw materials mostly act as evidence and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `SKILL.md` and folder/index conventions instruct and route the host agent.
