---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llm-wiki workflow account: skill-guided retrieval, caller investigation and gated knowledge recording through the CLI."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
---

# llm-wiki workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the skill's prescribed rules→list→search→get→create chain: an external agent consults domain knowledge before doing work, investigates a gap, then records reusable knowledge, subject to directory confirmation rules. It was selected because the source explicitly connects retrieval and recording, rather than merely exposing unrelated tools. The CLI supplies concrete handoff and rejection behavior. This is a source-supported procedure, not an observed completed session. SRC-1 supplies implementation and doctrine/design only; no execution trace establishes that an agent followed the chain or delivered a correct domain answer.

The skill names both the progression and the division of responsibility (SRC-1, `packages/skill/SKILL.md`):

> - `SKILL.md` 与本 skill 只负责通用流程（rules→list→search→get→create）；具体
>   「什么场景自动记、什么场景先确认」以各目录规则为准。
> --- `packages/skill/SKILL.md`

The external host loads the skill, schedules tools and supplies any model reasoning. llm-wiki supplies bundle data, directory guidance, executable write checks and persistence. It does not create an internal model worker to investigate the gap. The supplied [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-concept-create](runtime.md#rt-rte-concept-create) already identify these routes; this account does not redeclare them.

### 1. Request becomes a sequence of knowledge reads

A user request involving existing facts, conventions or known pitfalls is the skill's trigger. The host is instructed to consult the bundle before answering or acting. CLI availability and an accessible bundle are prerequisites. Each command resolves its bundle independently from arguments, environment or registry, so continuity depends on the caller keeping the intended bundle selected; the sequence is not one target-managed transaction (SRC-1, `packages/skill/SKILL.md`, `packages/skill/bin/wiki.mjs`).

The prescribed first handoff is `wiki rules`: without a directory argument it collects all APPEND behavior text and root AGENTS rules. Next, `wiki list` returns an overview; `wiki search` accepts caller-selected keywords, optional type/tag filters and a limit; `wiki get` accepts the selected ID or title. These are text returns to the host, not delegated reasoning frames. The core rebuilds graph state from Markdown and supplies retrieval results; the caller decides the next command. The sequence is natural-language guidance, not an executable dependency that prevents a direct create ([RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)).

The inspected CLI shows what actually crosses the get handoff: formatted identity, type/status, optional runtime and description, backlinks, body and a scoped rule appendix. This is more useful than a search hit alone, but not a guarantee that all relevant knowledge was selected. The appendix helper can silently return empty text on error. Search failure is not proof that knowledge is absent; the host must interpret its query and results (SRC-1, `packages/skill/bin/wiki.mjs`).

### 2. Investigation and proposal remain with the caller

For an unmet knowledge need, the skill tells the agent to investigate before answering, then create a concept when missing facts or a discovered root cause warrant recording. It explicitly distinguishes direct recording from user-confirmed content (SRC-1, `packages/skill/SKILL.md`):

> - 用到库里没有的**事实/结构**（新表、新接口、新系统、新术语）→ 探查后用 `wiki create` 补录
> - 踩了坑 / 查出根因 → 记 `Pitfall`；与用户确认过的口径/约定 → 记 `Metric` 或 `Attested Computation`
> - 规则声明需 human 确认的类型 → 先向用户展示、确认后加 `--confirmed`
> --- `packages/skill/SKILL.md`

The host must supply the investigation, content synthesis, proposed path, type and body. The target does not inspect the domain tools' results or certify their interpretation. There is no expected-answer oracle in this open recording workflow. The rule text guides the proposal; gate code decides whether the create invocation may proceed. Human approval is requested for configured types, not for every write or every inference ([RT-RTE-concept-create](runtime.md#rt-rte-concept-create)).

### 3. Confirmation refusal and recovery

Before writing, the skill requests `wiki rules <target-directory>`. The CLI then independently checks the nearest applicable AGENTS gate for the proposed type. If that type needs confirmation and the flag is missing, the CLI prints a request to show the proposal to the user and retry after consent, then exits 2 before calling core create (SRC-1, `packages/skill/bin/wiki.mjs`):

> if (gate.needConfirm && !has(rest, '--confirmed')) {
> --- `packages/skill/bin/wiki.mjs`

> process.exit(2)
> --- `packages/skill/bin/wiki.mjs:299-299`

Recovery belongs to the external agent: obtain the requested approval, revise or abandon the proposal, or retry with `--confirmed` after consent. The target has no suspended approval session to resume. The flag and WIKI_USER string are caller assertions, not authenticated proof of a human decision. Thus this path provides a protocol-level veto opportunity through a cooperating host, not a universal human approval guarantee. Direct core callers, updates and ingest do not share this particular admission check; these limits are already established by [RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

A second rejection can occur in core create: an invalid ID, missing type or existing destination throws rather than accepting the proposed concept. Existing-file rejection directs the caller toward update. This checks structural preconditions, not knowledge truth (SRC-1, `packages/core/lib/write.mjs`):

> if (existing) throw new Error(`概念已存在: ${p.id}（如需修改用 update）`)
> --- `packages/core/lib/write.mjs`

### 4. Persistence, optional checks and delivery

After admission, core serializes the proposed frontmatter/body, writes the concept, appends a Creation log entry and updates the directory index. Generated metadata identifies the agent producer; confirmed creates also retain a human-labelled verified entry. These labels record the supplied provenance assertions, not an independent validation result. Core's write precedes log/index maintenance, so later failure can leave a durable concept without complete derived maintenance. Recovery is caller-driven inspection, index repair or explicit update, not automatic transactional rollback ([RT-RTE-concept-create](runtime.md#rt-rte-concept-create); SRC-1, `packages/core/lib/write.mjs`).

The CLI awaits core create and an online-flush attempt before printing `created` with ID/link and flush status; it then prints scoped rules. Local persistence and remote publication are separate outcomes. Flush/conflict handling is bounded by [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync); neither the text label nor a successful local write proves remote delivery. The create handler does not automatically run validate or lint (SRC-1, `packages/skill/bin/wiki.mjs`).

The skill makes lint an optional wrap-up action. CLI validate can exit 1 on schema errors; lint prints issues and a summary. These diagnostics can inform further caller repair but are not mandatory acceptance gates in this chain. Neither checks the domain claim against an answer oracle (SRC-1, `packages/skill/SKILL.md`, `packages/skill/bin/wiki.mjs`).

Delivery therefore has two boundaries. llm-wiki's deliverable is returned retrieval text or a locally persisted concept with a CLI result and rule appendix. The domain answer or action remains the host's deliverable; no target-side completion or acceptance step certifies it. Later graph reconstruction can expose the new concept to another invocation, while retained rules can guide later host behavior. Those are read-back and authority channels, not evidence that this particular knowledge was consumed, that instructions were obeyed, or that future answers improved ([RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery)).

### Inspection coverage and limits

This member inspected the complete skill plus CLI loader/bundle resolution, rule appendix, list/search/get/create/update, diagnostics and rules-dispatch regions, and core create/update regions under SRC-1 at the frozen commit. The added inspection supports implementation and doctrine/design, not observed operation. The workflow-specific quotes above retain the prescription and rejection witnesses; supplied runtime records retain the shared route evidence. This account intentionally follows the skill/CLI chain rather than asserting equivalent end-to-end coordination across all five adapters. External investigation quality, host scheduling, user consent and final-answer delivery remain unobserved.

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

none
