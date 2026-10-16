---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Interview Doc Agent's host-interpreted initialization, dossier maintenance and document-generation routes at its frozen prompt boundary."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
---

# Interview Doc Agent runtime report

## Runtime account

Interview Doc Agent ships a behavioral instruction file, not its own execution engine. The user supplies a request and materials; an external host supplies the model, conversation, file/page tools and actual permissions. The host model owns the next step by interpreting natural-language instructions. There is no source-inspected scheduler or tool dispatcher within this artifact. This account uses SRC-1's doctrine/design layer, not implementation or run evidence (SRC-1, `SKILL.md`, `README.md`).

> 由读到本 skill 的 AI 直接执行（Obsidian Claudian / 飞书智能伙伴 / Claude Code 均可），直接读写文件。无需 API key。
> --- `SKILL.md`

The shipped entry paths are a Claudian skill file, a Claude Code skill directory, a skill read by another file-capable conversational AI, or the full text pasted into a Feishu assistant's instructions. Download examples target moving `main`; this analysis concerns only the frozen revision, not later downloads. The instructions describe paths relative to the folder containing SKILL.md, but the Claudian installation places the skill in `.claudian/skills/` while the tutorial says initialization happens at the current location. Workspace resolution therefore depends on host/user setup; no inspected resolver reconciles those descriptions (SRC-1, `README.md`, `SKILL.md`, `docs/02-安装-obsidian.md`).

### Ordinary invocation

A local user first asks for initialization, adds raw records to `materials/`, then asks to organize them. [RT-RTE-initialize-workspace](#rt-rte-initialize-workspace) creates the prescribed storage layout; [RT-RTE-consolidate-experience](#rt-rte-consolidate-experience) asks the model to turn raw records into dossiers and maintain two indexes. The user then requests a resume or a named project's interview script. [RT-RTE-generate-document](#rt-rte-generate-document) asks the model to read the lightweight index, select complete relevant dossiers and a template, optionally consult raw material for missing detail, and write to `output/`. The user opens and may refine that document. Local file I/O is the external host's effect boundary. No transactions, concurrency protocol, retry loop or checkpoint recovery are specified by these steps (SRC-1, `SKILL.md`, `docs/04-使用指南.md`).

> 生成时**先读 `wiki/index.md`** 这张轻量索引表定位，再只读相关经历库档案 + 模板，不必全读（省 token）
> --- `SKILL.md`

This is a model-decided read-selection policy, not enforced exclusion from a context window. Unselected dossiers and raw files remain on storage and can be reread; the artifact specifies neither eviction of already-loaded turns nor isolated worker contexts. The external host's compaction, context limits and tool-result handling are uninspected. Index selection can reduce requested reads, but neither actual token savings nor correct selection is observed. The rationale also allows reading the entire small library, so selective reads are not a universal isolation invariant (SRC-1, `docs/01-理念-karpathy-wiki.md`).

> 即便把整个经历库全读进去也放得下，索引只是让它更省而已。
> --- `docs/01-理念-karpathy-wiki.md`

### Material alternate and forcing routes

1. **Empty installation.** Only SKILL.md is required; initialization must construct missing directories and starter files without requiring the repository's templates. The shipped profile is named `00-个人档案.模板.md`, whereas normal reads target `00-个人档案.md`; its instructions permit renaming. Likewise, the script-generation step names a non-example template file while the shipped index points to `.示例.md`. These are user/model setup obligations rather than implemented path fallbacks (SRC-1, `SKILL.md`, `wiki/index.md`, `经历库/00-个人档案.模板.md`).
2. **JD tailoring and insufficient detail.** The generation route additionally reads a chosen JD, matches its capability requirements to persona keywords and projects, and reorders/cuts experience. Raw-material lookup is expressly allowed when dossiers lack detail. Therefore the dossier library is the primary source, not an exclusive source; provenance and numeric consistency are not mechanically checked (SRC-1, `SKILL.md`, `jd/README.md`).
3. **Cloud write denied.** [RT-RTE-feishu-writeback](#rt-rte-feishu-writeback) replaces file I/O with permission-dependent knowledge-page/Base operations. If the assistant cannot write back, it returns text and the user copies it manually. The proposed lark-cli variant names `lark-base` and `lark-doc`, but ships no adapter. Neither host integration is an inspected alternate executor implementation (SRC-1, `docs/03-接入-飞书.md`).
4. **Missing or fictional numbers.** Instructions demand real dossier numbers, placeholders and reminders for gaps; the included example explicitly contains fictional data. This is a concrete reason that loading a dossier is not evidence of factual authenticity. The model/user must replace or recognize the example; no automatic example filter or numeric oracle is specified (SRC-1, `SKILL.md`, `经历库/01-示例经历.md`).

> 这是一篇**示例经历档案**，展示经历库该长什么样。数据为虚构演示。
> --- `经历库/01-示例经历.md`

These are inspected instruction-level forcing cases, not executed tests. Direct model calls, provider-native tools, callbacks, remote workers, manual graph control and durable graph variants have no shipped executable routes in the inspected tracked tree. External hosts may expose such facilities; their implementation and grants remain outside this boundary. Nothing in this prompt artifact mediates all external host actions.

### Guarantees and controls

The numerical-fidelity policy belongs to the skill author and is applied by the host model during consolidation and generation. Its only inspected enforcement point is natural-language instruction, with **policy** strength, not an invariant. It covers the requested local and adapted cloud workflows only to the extent their hosts load and follow it. Manual copying, user edits, fictional examples and raw-material lookup bypass any claim that common storage alone guarantees identical facts. Required external contracts are correct instruction loading, faithful model interpretation, readable genuine inputs and successful durable writes. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. See [RT-CLM-numeric-fidelity](#rt-clm-numeric-fidelity).

The local-only privacy statement is stronger than the evidence. The owner is the tutorial author; local file placement is its stated mechanism, but there is no provider-transmission control in the artifact. Personal-data ignore rules are commented out, and Feishu deliberately stores content in cloud services. A local vault does not establish that model inputs remain local. Guarantee strength: no claimed guarantee at the inspected enforcement layer; the documentation nevertheless claims no upload. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. Its required external contracts—provider data handling, host permissions and user-configured Git exclusions—are not supplied. See [RT-CLM-local-privacy](#rt-clm-local-privacy).

Capability surface: a host AI with conversational and read/write facilities. Current grant set: uninspected, because no deployed host configuration is supplied. Isolation envelope: uninspected; path conventions name intended destinations, not a sandbox or ACL. Human users initiate requests and can edit inputs and results; the local procedure does not require per-content human approval before model writes. The Feishu manual fallback does put a human between proposed content and persistence. No shipped mechanism updates model weights, installs capabilities, revises SKILL.md from performance evidence, or changes production machinery. Manual instruction adaptation is described in the cloud setup, but not an automatic improvement loop (SRC-1, `README.md`, `SKILL.md`, `docs/03-接入-飞书.md`).

The source inspection covered the registered tracked tree's behavioral files, tutorials, indexes, templates, examples and ignore rules at the frozen commit. No additional source or execution evidence was introduced. Reliable adherence, activation, persistence across actual sessions, document quality, privacy and causal benefit remain unobserved.

## Shared records

### Components

#### RT-CMP-host-ai
Label: Host AI

Identity: the AI that reads and executes SKILL.md, exemplified by Claudian/Claude Code or Feishu assistants. Representational form: distributed-parametric model computation; weights and provider infrastructure are external, not stored in this repository. Storage substrate: uninspected provider/host model storage. Exact model version is not pinned. Parameter changes during operation are uninspected; a mutable endpoint's ability to resolve another model is also uninspected because no provider binding is shipped. The host can be exchanged by users, but that is not evidence about any one endpoint. Evidence: SRC-1, `SKILL.md`, `README.md`; the runtime-mode quotation above establishes the delegated executor, not its internals.

### Operative objects

#### RT-OBJ-skill
Label: SKILL

Identity: repository-root SKILL.md, or its copied host instruction body. Representational form: natural-language procedural guidance interpreted by the model; its YAML name/description supply host-facing metadata, whose parser behavior is outside this boundary. Storage substrate: Markdown file or Feishu instruction field. It prescribes initialization, dossier maintenance, selection, generation and numeric constraints. Evidence: SRC-1, `SKILL.md`, `docs/03-接入-飞书.md`.

> 核心不变：**SKILL.md 当指令，经历库当知识源**。
> --- `docs/03-接入-飞书.md`

### Routes

#### RT-RTE-initialize-workspace
Label: Initialize workspace

Endpoints/progression: a user's first call in an incomplete workspace → host model interprets SKILL.md → creates directories, an empty personal profile and empty wiki index → tells the user where to put inputs. Owner: host model for proposed operations; host tools for I/O. Context/state/effects: current request and skill text determine new persistent files; no spawned worker or coordination protocol is prescribed. Operating mode: open user request. Guidance: fixed skill setup instructions. The model proposes/decides file contents under those instructions; the user supplies the invocation, not necessarily approval of each file. Host permissions can reject I/O. Answer oracle: none specified; no checked initialization reference outcome is supplied. Rollback/recovery: no transaction or rollback is specified; missing directories are an initialization trigger, not proof of idempotent partial-write repair.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: notice of initialization and instructions to add materials/templates.
- Later read-back: created profile/index are intended to be read during future organization and generation.
- Delegated visibility: inapplicable — no delegated worker is prescribed; host receives the current request and skill.
- Selection predicate: first invocation with the named directories missing; partial-directory behavior is unspecified.
- Invalidation or expiry: inapplicable — no expiry policy is given for starter files.
- Activation or effect: requested directory/file creation; successful writes and later use are not observed.
- Evidence limits: source instructions only; workspace resolution and tool grants are host-dependent.

Evidence: SRC-1, `SKILL.md`.

> 本 skill 只需要 `SKILL.md` 这一个文件即可工作——其余目录会按需自建。
> --- `SKILL.md`

#### RT-RTE-consolidate-experience
Label: Consolidate experience

Endpoints/progression: user adds or edits raw material and asks to organize/update → model reads new files → extracts dossier content → writes the corresponding experience dossier → updates personal-profile and wiki indexes. Owner/next-step policy: model applying fixed extraction instructions; host tools execute writes. Input and output are natural-language records on local files, or adapted cloud pages. Human supplies the source content and trigger; model proposes and admits the transformed content in the direct-write mode. No per-item human veto is required by the local instructions; host denial or subsequent human edits remain possible. Operating mode: open user-requested maintenance, not a bounded experiment. Answer oracle: none specified; raw materials are factual inputs, not a separately checked expected consolidation outcome. Change guidance: preserve all numbers and express background/problem/actions, why/how and persona strengths. Persistent changes are dossiers and indexes, not revised extraction rules. No rollback, conflict resolution or atomic index update is specified. Memory-specific object and revision assessments are left to the memory member.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: organized dossier content/files are the requested result; a separate conversational acknowledgement is unspecified.
- Later read-back: maintained dossiers and indexes feed later generation requests.
- Delegated visibility: inapplicable — no separate analyst or worker is prescribed.
- Selection predicate: new/modified raw files and their corresponding project dossier, selected by the model from the user request.
- Invalidation or expiry: user changes raw material and asks to update; no automatic stale-content detection or expiry is specified.
- Activation or effect: requested durable dossier/index writes; subsequent behavior change is not observed.
- Evidence limits: model extraction fidelity, completeness, successful multi-file writes and retained-content activation are not demonstrated.

Evidence: SRC-1, `SKILL.md`, `materials/README.md`, `docs/04-使用指南.md`.

> 用户新增/修改 materials/ 原始素材后：读新文件 → 提炼整合进 `经历库/` 对应档案 → 更新 `00-个人档案.md` 索引和 `wiki/index.md` 检索表。
> --- `SKILL.md`

#### RT-RTE-generate-document
Label: Generate document

Endpoints/progression: user requests a resume/script, optionally naming project, length or JD → model reads index/profile and relevant dossiers/templates → optionally rereads raw details or reads JD → selects, reorders and rewrites → saves output. Owner: host model, following skill and style templates; host tools perform file writes. Representation: natural-language instructions and facts, not fixed-rule numerical matching. Working context is selected by model-directed reads, without prescribed compaction/isolation. Terminal output: resume or interview script; scripts usually have short/long versions and optional submodules. Resume instructions may update a `.tex` file for formal PDF use, but no PDF compiler/executor is shipped. Coordination: sequential steps in one host conversation; no parallel agents or shared-state locking specified.

Decision roles: user chooses purpose/JD and supplies or replaces templates; model chooses matching experience, cuts/reorders and drafts. Host permissions can deny output writes; user can refine the product. Operating mode: open document request, with optional JD matching rather than a curriculum/experiment. Answer oracle: none specified; JD is selection guidance, templates are style references, and dossiers supply asserted facts, not an independently validated correct answer. Output admission has no prescribed per-document approval gate. Recovery: missing real numbers require placeholders and a user reminder; missing file/template and failed-write recovery are unspecified. Changes persist as output documents; no route makes those documents instructions for future operation.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: saved resume/script in output/ for user consumption; cloud mode can instead return conversation text.
- Later read-back: retained dossiers/indexes are read into this invocation; no automatic reuse of generated output as future behavioral guidance is specified.
- Delegated visibility: inapplicable — no delegated worker is prescribed.
- Selection predicate: requested document/project and optional JD capability requirements matched against index, persona keywords and experiences by the model.
- Invalidation or expiry: new inputs or a new user request can cause regeneration; no output expiry or automatic regeneration is specified.
- Activation or effect: instructions request fact/style-sensitive generation and output writes; actual influence and factual quality are not observed.
- Evidence limits: no real input/output trace, correctness oracle or quality comparison is supplied; reading references does not prove adherence.

Evidence: SRC-1, `SKILL.md`, `wiki/index.md`, `jd/README.md`, `templates/简历/简历模板.示例.md`, `templates/逐字稿/产品面试话术模版.示例.md`.

> 重排/裁剪经历，突出与 JD 最相关的项目和数据，弱化无关项
> --- `SKILL.md`

#### RT-RTE-feishu-writeback
Label: Feishu writeback

Endpoints/progression: user copies skill text into an assistant, adapts paths to knowledge-page lookups and binds a knowledge source → assistant reads/organizes/generates → writes a page if permitted, otherwise returns text → human manually pastes text. Owner: user for deployment adaptation; assistant for transformation; host authorization for automatic write; human for fallback admission. Forms/substrates: natural-language instructions and dossier/page text in cloud knowledge documents or Base; API/tool internals are excluded. Setup changes the deployed instruction copy's path guidance; it is human-controlled configuration, not performance-fed instruction revision. Proposed lark-cli integration names Base/document tools but supplies no executable implementation. Operating mode: open requests. Answer oracle: none specified. User can reject/edit before manual persistence; that gate is not present in the automatic-write branch. No synchronization, rollback or failed-partial-write protocol is supplied.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: cloud document when writable, or organized/generated text in conversation when not.
- Later read-back: manually or automatically persisted dossier pages are intended to serve as bound knowledge for later requests; provider selection behavior is uninspected.
- Delegated visibility: uninspected — host knowledge-source delivery is described, but actual assistant-visible page content and service-side transformations are not supplied.
- Selection predicate: adapted knowledge-page lookup and current request; automatic host retrieval details are uninspected.
- Invalidation or expiry: manual content updates/copying are described; no automatic expiry or synchronization rule is supplied.
- Activation or effect: requested cloud persistence or human copy; no inspected run establishes either or its later influence.
- Evidence limits: permission/version-dependent tutorial, not a shipped cloud driver or observed integration.

Evidence: SRC-1, `docs/03-接入-飞书.md`.

> 飞书智能伙伴能否「写回」知识库取决于版本权限。若不能自动写回，它会把整理好的内容输出在对话里，你手动粘进知识库页面即可。
> --- `docs/03-接入-飞书.md`

### Claims

#### RT-CLM-numeric-fidelity
Label: Numeric fidelity

Claimed operation: preserve every source number during consolidation, use genuine dossier numbers during generation, and leave placeholders/remind the user where facts are missing. Source and owner: author instructions in SRC-1, `SKILL.md`; execution owner is host model. Guarantee strength: policy. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. There is no independent numeric checker in the shipped tracked files. All-outputs-agree language in `README.md` and `docs/04-使用指南.md` is stronger than common-source selection warrants; raw lookup, model rewriting, manual edits and fictional starter content prevent an invariant conclusion.

> - **量化数据全部保留**，一个数字都不漏
> --- `SKILL.md`

> - 绝不编造数据；真实数据缺失时用 `___` 占位并提醒用户补充
> --- `SKILL.md`

#### RT-CLM-local-privacy
Label: Local privacy

Claimed operation: the Obsidian tutorial says privacy data is not uploaded because the agent reads/writes locally and only a user's Git push uploads. Evidence: SRC-1, `docs/02-安装-obsidian.md`, `.gitignore`. This establishes attributed documentation, not a provider-data guarantee. The ignore file tells users to uncomment personal-data rules; they are not active by default. Feishu is an expressly cloud-based alternate. Host/model traffic is uninspected. Doctrine conclusion status: claimed. Operation conclusion status: uninspected.

> A：不会。Agent 只在你本地 vault 里读写文件。只有你主动 git push 才会上传，且 `.gitignore` 已预留忽略个人数据的配置。
> --- `docs/02-安装-obsidian.md`

> # 模板使用者：取消下面的注释可让自己的数据不进 git
> --- `.gitignore`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-instructions
Label: Skill instructions

Consumer: external host model. Channel: loaded/read skill text or pasted Feishu instruction body. Force: requested procedural guidance, including write destinations, extraction standards and numeric constraints; not an independently enforced tool policy. Horizon: the current conversation/invocation when loaded, and later invocations if the deployed host retains and reloads the instruction copy. Actual loading/activation across sessions is uninspected. Templates additionally guide writing style, while JD and dossiers supply task selection/factual context rather than general execution permissions. Evidence: SRC-1, `SKILL.md`, `README.md`, `docs/03-接入-飞书.md`; the SKILL-as-instructions quotation in [RT-OBJ-skill](#rt-obj-skill) establishes this declared channel. No method-text criticism/revision loop is prescribed by this authority path.

## Annotations

none
