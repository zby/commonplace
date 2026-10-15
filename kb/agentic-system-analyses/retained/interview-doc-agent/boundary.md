---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Interview Doc Agent's prompt-operated experience library and document workflow at commit 6ebfe9aba989d7949dadea0fc4af6fb64892c6aa."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  identity: https://github.com/Shilren/interview-doc-agent
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/interview-doc-agent-c7597c33f23d/related-systems/Shilren--interview-doc-agent
  revision: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
  sha256: null
---

# Interview Doc Agent boundary

## Boundary and evidence

The target is the shipped Interview Doc Agent skill, its persistent experience-library structure, templates and usage instructions. Its intended use is to turn personal experience materials into reusable project dossiers, then generate resumes and interview scripts, optionally tailored to a job description. It qualifies as a memory/knowledge/context-engineering system because model-directed instructions maintain retained dossiers and indexes and later select those dossiers for document generation (SRC-1, `SKILL.md`, `wiki/index.md`). It is not an enclosing runtime: the supplied skill delegates execution and file access to a host AI.

> 由读到本 skill 的 AI 直接执行（Obsidian Claudian / 飞书智能伙伴 / Claude Code 均可），直接读写文件。无需 API key。
> --- `SKILL.md`

The functional boundary includes initialization, user-supplied materials and job descriptions, dossier organization, index maintenance, selective rereading, template-guided generation, and output placement. The maintenance-to-consumption loop is shipped as instructions rather than executable application code (SRC-1, `SKILL.md`).

> 用户新增/修改 materials/ 原始素材后：读新文件 → 提炼整合进 `经历库/` 对应档案 → 更新 `00-个人档案.md` 索引和 `wiki/index.md` 检索表。
> --- `SKILL.md`

> - 生成时**先读 `wiki/index.md`** 这张轻量索引表定位，再只读相关经历库档案 + 模板，不必全读（省 token）
> --- `SKILL.md`

The boundary kind is **whole-system** for this shipped prompt-and-document artifact, not for its external hosts. All tracked files were inspected, including the empty output placeholder. No shipped executable driver, evaluator, test suite or provider integration appears in the tracked tree. Therefore the evidence tier is **doc-grounded**: instructions and examples establish the intended loop, not successful execution, reliable data preservation, privacy guarantees or measured token savings (SRC-1, `README.md`, `SKILL.md`, `docs/01-理念-karpathy-wiki.md`, `docs/04-使用指南.md`). The experience example explicitly identifies its data as fictional, so it is not an observed execution artifact (SRC-1, `经历库/01-示例经历.md`).

> 这是一篇**示例经历档案**，展示经历库该长什么样。数据为虚构演示。
> --- `经历库/01-示例经历.md`

External dependencies are a model-capable host with conversation and read/write access, its authentication and permissions, and the local or cloud storage it exposes. Obsidian/Claudian/Claude Code installation and Feishu adaptation instructions are included; the implementations of those products, lark-cli, model providers, and linked Karpathy and resume-template sources are excluded. This prevents conclusions about host instruction loading, tool enforcement, actual provider data handling, cloud persistence or synchronization, and the correctness of external design claims (SRC-1, `README.md`, `docs/02-安装-obsidian.md`, `docs/03-接入-飞书.md`). Feishu writeback is explicitly permission-dependent and may require manual copying; it is not treated as a shipped automatic integration.

> 飞书智能伙伴能否「写回」知识库取决于版本权限。若不能自动写回，它会把整理好的内容输出在对话里，你手动粘进知识库页面即可。
> --- `docs/03-接入-飞书.md`

The frozen source is the acquired Git checkout at **6ebfe9aba989d7949dadea0fc4af6fb64892c6aa**, verified as its HEAD. The applicability cutoff is **2026-10-14**. Links to moving download URLs in source instructions do not expand this evidence boundary. There are no unavailable repository files or material paths left uninspected. Actual user dossiers, generation outputs, execution traces and comparative experiments are not supplied; their absence prevents operational and causal conclusions, not inspection of the shipped artifact.

### Tracked top-level coverage

Every row below is included and inspected. Directory rows enumerate the material tracked paths. Each source reference uses SRC-1 at the frozen revision.

| Top-level file or directory | Coverage | Material paths and role | Limits / conclusion prevented |
|---|---|---|---|
| `.gitignore` | Included; inspected | SRC-1, `.gitignore`: editor/build exclusions and commented-out personal-data ignore patterns. | Not evidence that personal files are automatically excluded or kept private. |
| `LICENSE` | Included; inspected | SRC-1, `LICENSE`: MIT distribution terms. | No operational evidence. |
| `README.md` | Included; inspected | SRC-1, `README.md`: entry point, single-file deployment, initialization and caller requests, architecture and host choices. | Usage and benefit claims are documentation, not measured results. |
| `SKILL.md` | Included; inspected | SRC-1, `SKILL.md`: host-loaded behavioral entry point; creates directories/profile/index, ingests and updates dossiers, maintains both indexes, reads retained content, matches JD, writes outputs, prescribes missing-data placeholders. | Model adherence and durable writes are not verified. |
| `docs/` | Included; inspected | SRC-1, `docs/01-理念-karpathy-wiki.md`: design rationale and retention/retrieval workflow; `docs/02-安装-obsidian.md`: Claudian loading and local-file caller; `docs/03-接入-飞书.md`: cloud mapping, permission-dependent writeback and manual fallback; `docs/04-使用指南.md`: user-triggered ingest, regeneration and output use. | Tutorials are not host implementation or run evidence; efficiency, consistency and privacy claims remain unverified. |
| `jd/` | Included; inspected | SRC-1, `jd/README.md`: job-description admission and requests selecting retained experience for customized outputs. | No real job-description input or matching evaluation is supplied. |
| `materials/` | Included; inspected | SRC-1, `materials/README.md`: raw-material admission conventions and user-triggered consolidation. | No actual raw-material-to-dossier trace is supplied. |
| `output/` | Included; inspected | SRC-1, `output/.gitkeep`: empty tracked destination placeholder; output writing and user consumption are prescribed in `SKILL.md` and `docs/04-使用指南.md`. | No generated-output artifact or quality evaluation is supplied. |
| `templates/` | Included; inspected | SRC-1, `templates/简历/简历模板.示例.md`: resume structure and bullet style; `templates/逐字稿/产品面试话术模版.示例.md`: introduction and project-narrative scaffolds consumed during generation. | Illustrative examples do not establish factual output quality. |
| `wiki/` | Included; inspected | SRC-1, `wiki/index.md`: lightweight lookup table connecting retained dossiers and templates; raw-material fallback and output locations. | The shipped index is a starter artifact, not proof of maintained links in deployment. |
| `经历库/` | Included; inspected | SRC-1, `经历库/00-个人档案.模板.md`: profile fields, persona keywords and dossier index, intended to be renamed on use; `经历库/01-示例经历.md`: dossier structure, quick-access metrics and follow-up detail. | Template/example content is not real personal memory or observed consolidation. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Shilren/interview-doc-agent` | 6ebfe9aba989d7949dadea0fc4af6fb64892c6aa | doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/interview-doc-agent-c7597c33f23d/related-systems/Shilren--interview-doc-agent`. Complete tracked tree and all 15 tracked files, as enumerated in the coverage table; behavioral instructions, installation and usage docs, indexes, templates, examples, ignore rules and license. | Doctrine/design: [skill](https://github.com/Shilren/interview-doc-agent/blob/6ebfe9aba989d7949dadea0fc4af6fb64892c6aa/SKILL.md), [entry/readme](https://github.com/Shilren/interview-doc-agent/blob/6ebfe9aba989d7949dadea0fc4af6fb64892c6aa/README.md), [retained-content index](https://github.com/Shilren/interview-doc-agent/blob/6ebfe9aba989d7949dadea0fc4af6fb64892c6aa/wiki/index.md); full commit-relative paths in the coverage table anchor the remaining inspected files. | No repository access gaps. External host implementations and linked sources are outside the frozen source; no observed run, real input/output pair or causal experiment is supplied. Supports declared operation only, not execution reliability, privacy, token savings or output accuracy. |
