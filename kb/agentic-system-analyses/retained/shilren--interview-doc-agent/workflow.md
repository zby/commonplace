---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Interview Doc Agent's user-triggered material consolidation and JD-tailored resume workflow, including missing-data handling and permission-dependent delivery."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
---

# Interview Doc Agent workflow report

## Workflow account

This account selects the shipped **raw materials → experience dossiers → JD-tailored resume → user use** workflow. It is representative because the usage guide explicitly joins maintenance and generation, while SKILL.md supplies the transformation and selection instructions. It is a sequence of user-triggered requests, not an autonomous end-to-end job. All evidence is SRC-1's doctrine/design at the frozen revision; no real input/output trace establishes execution or successful delivery (SRC-1, `SKILL.md`, `docs/04-使用指南.md`; [boundary](boundary.md#boundary-and-evidence)).

> ① 加素材   把项目经历（任何格式）粘进 materials/
> ② 整理     对 AI 说「整理进经历库」→ 沉淀成 经历库/ 里的完善档案
> ③ 生成     说「写简历」/「写某项目逐字稿」/「按这份 JD 定制」
> ④ 取用     产出在 output/，按需微调
> --- `docs/04-使用指南.md`

**1. Establish the workspace and hand over materials.** The user makes SKILL.md available to a file-capable host AI and supplies the organization request and raw project records. If the prescribed directories are missing on first use, [RT-RTE-initialize-workspace](runtime.md#rt-rte-initialize-workspace) asks that AI to create them, the blank personal profile and the lookup index, then tell the user where materials and templates belong. This is a prerequisite branch, not a mandatory repeated phase. Actual workspace resolution and tool permissions belong to the external host; no source-inspected initializer verifies them (SRC-1, `SKILL.md`).

**2. Consolidate and persist the experience.** In [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience), the same host AI reads the new material, extracts a corresponding dossier and updates both the personal-profile index and wiki lookup table. The user delegates transformation and file writing to that AI, not to a separately instructed specialist. The requested retained result includes background judgment, problem, actions/results, why/how, numbers and persona strengths. The next generation request receives a model-organized dossier rather than necessarily receiving the original material in full (SRC-1, `SKILL.md`, `docs/04-使用指南.md`).

> 用户新增/修改 materials/ 原始素材后：读新文件 → 提炼整合进 `经历库/` 对应档案 → 更新 `00-个人档案.md` 索引和 `wiki/index.md` 检索表。
> --- `SKILL.md`

The instruction to preserve every number is the policy in [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity), not a checked extraction outcome. The model directly admits dossier/index changes in the local workflow; initiating organization is not per-dossier human approval. The inspected procedure specifies no independent checker, acceptance test or atomic multi-file commit. Consequently, this handoff does not establish that every fact survives consolidation or that both indexes describe the same persisted state (SRC-1, `SKILL.md`, `docs/04-使用指南.md`).

**3. Supply the JD and request a tailored resume.** The user places the target job description in `jd/` and requests a matching resume. This is a new invocation of [RT-RTE-generate-document](runtime.md#rt-rte-generate-document), using the retained library from step 2. The model is instructed first to read `wiki/index.md` to locate relevant dossiers and templates, read the personal profile/persona keywords, and match experience against JD capability requirements. The lookup table carries paths and keyword/quick-data fields; it is routing guidance, not the complete factual payload. The selected dossiers supply facts, the JD supplies selection priorities and the resume template supplies structure/style (SRC-1, `SKILL.md`, `wiki/index.md`, `docs/04-使用指南.md`).

> 1. 把目标岗位 JD 粘进 `jd/`（新建一个文件，如 `jd/字节-增长PM.md`）
> 2. 「参照 jd/ 里的字节增长 PM，生成匹配的简历」
> 3. AI 会挑出与 JD 最相关的经历、突出对应数据、弱化无关项
> --- `docs/04-使用指南.md`

**4. Select and rewrite, without an independent acceptance oracle.** The AI owns the matching, reordering and cutting decisions. Resume instructions call for condensed bullets with a bold topic, action and quantified result rather than expanded reasoning. No numerical JD scorer, expected resume or separate reviewing agent is supplied. Neither matching a JD nor following a style template verifies the truth of the selected facts. The local workflow prescribes writing the result without a mandatory user approval gate; the user may edit it afterward (SRC-1, `SKILL.md`, `docs/04-使用指南.md`; [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)).

> 3. 生成：高度浓缩，每条 bullet = 加粗主题 + 动作 + 量化结果（不展开 why）
> --- `SKILL.md`

**5. Handle insufficient detail and missing numbers.** The source supports a concrete degraded-input branch: when a dossier lacks detail, the AI may consult `materials/`; when genuine numbers are missing, it must leave `___` and remind the user to supply them. This rejects fabricated completion rather than rejecting the whole document. The AI owns fallback reading and placeholder insertion; the user owns supplying missing facts. No automatic wait/resume cycle or validator confirms that the returned document actually retains those placeholders. The shipped index marks its example dossier for replacement with real experience, so simply reading that starter dossier cannot authenticate its numbers (SRC-1, `SKILL.md`, `wiki/index.md`; [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity)).

> - materials 仅在经历库细节不足时回查
> --- `SKILL.md`

The minimum verbatim missing-number instruction is retained in [RT-CLM-numeric-fidelity](runtime.md#rt-clm-numeric-fidelity). Its enforcement is model-interpreted policy, not an observed rejection test. This distinction matters because the documented promise of aligned data does not inspect the consolidation-to-generation transformation or later user edits (SRC-1, `SKILL.md`, `docs/04-使用指南.md`).

**6. Deliver and revise on request.** In the local workflow, delivery means the requested resume is saved in `output/` for the user to take and adjust. It does not mean PDF compilation, quality certification or employer submission. The user must request renewed consolidation after modifying source material; no automatic invalidation or regeneration links those edits to already-written outputs (SRC-1, `SKILL.md`, `docs/04-使用指南.md`; [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)).

> - **改了素材记得重新整理**：materials 更新后说一句「更新经历库」
> --- `docs/04-使用指南.md`

There is also an explicit permission-dependent persistence branch in the cloud adaptation: [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback) returns organized content in conversation when the assistant cannot write to the knowledge base, and the user manually pastes it. This introduces a human persistence handoff absent from automatic local writes. The fallback's quoted contract is retained in that runtime record. It is not evidence of a shipped cloud adapter, successful output-document creation or transactional recovery from a partial write. Local failed-write recovery remains unspecified in the inspected skill; the cloud tutorial supplies a bounded manual alternative, not a general retry protocol (SRC-1, `docs/03-接入-飞书.md`, `SKILL.md`).

The workflow therefore coordinates through user requests, persistent dossiers/indexes and one host AI's interpretation of fixed instructions. The inspected path does not prescribe parallel workers, reviewer delegation, checkpoints or rollback. That is a limit of the shipped procedure, not a conclusion about what an external host could provide. Its supported delivery contract is document placement or permission-dependent conversational handoff; successful execution, factual fidelity and benefit remain unobserved (SRC-1, `SKILL.md`, `docs/04-使用指南.md`, `docs/03-接入-飞书.md`). Source inspection for this member covered those three behavioral files and `wiki/index.md`, all already included by the boundary; no additional source coverage or evidence layer was introduced.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience)

Workflow handoff: the persistent dossier and two updated indexes connect user-requested organization to a later generation request. The usage guide requires the user to retrigger organization after source edits. No prescribed reviewer accepts the transformation before direct local persistence; numerical preservation is a requested condition, not a verified handoff result (SRC-1, `SKILL.md`, `docs/04-使用指南.md`).

#### On [RT-RTE-generate-document](runtime.md#rt-rte-generate-document)

Workflow position: downstream of consolidation, with a separate user-supplied JD and request. The model chooses and rewrites relevant experience; the template and JD guide the proposal but provide no independently checked answer. Missing facts can yield a delivered document with placeholders and a reminder, not a completed factual record. Local delivery is placement in `output/`, followed by optional user adjustment (SRC-1, `SKILL.md`, `wiki/index.md`, `docs/04-使用指南.md`).

#### On [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback)

Workflow recovery handoff: denied automatic knowledge-base writeback shifts persistence to the human receiving conversational text. This can preserve a proposed result without establishing that it was stored or consumed later. The tutorial does not specify partial-write detection, rollback or reconciliation between automatic and manual copies (SRC-1, `docs/03-接入-飞书.md`).
