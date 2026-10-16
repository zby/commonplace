---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SkillNote workflow: user-reviewed skill authoring, registry admission and later Claude Code delivery at the frozen revision."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
---

# SkillNote workflow report

## Workflow account

The representative workflow is **turn a persistent convention into a reviewed registry skill, then distribute it to a configured Claude Code project**. It is selected because the shipped authoring prompt explicitly connects drafting, user decisions, existence checks and POST/PATCH; the registry and session hooks supply the subsequent persistence and delivery path. This is a source-supported workflow contract plus implementation, not an observed execution. Registry acceptance and local installation are separate delivery milestones; neither establishes successful use on a later task.

The workflow joins [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) to [RT-RTE-project-sync](runtime.md#rt-rte-project-sync). A configured project, reachable registry and host hook execution are prerequisites for that second stage, not results of saving a skill. All evidence is SRC-1 at the revision in [the boundary](boundary.md). No host transcript, approval exchange or live synchronization result was supplied.

### 1. Request and permission to draft

The user can explicitly request a skill. Alternatively, the authoring agent can notice repeated instructions or conduct a session retrospective. The `skill-push` prompt restricts suggestions to persistent conventions and requires permission before drafting when the user did not initiate creation. The user is the first decision owner and can stop the workflow by withholding confirmation. This is a natural-language policy enforced by the external host's instruction following, not a backend prerequisite. SRC-1, `plugin/skills/skill-push/SKILL.md`; the API distinction is already established in [RT-RTE-registry-write](runtime.md#rt-rte-registry-write).

> Stop and wait for an explicit yes. Do NOT draft the name/description/content, fetch collections, or present a preview until the user confirms. Unsolicited drafts feel pushy and waste attention.
> --- `plugin/skills/skill-push/SKILL.md`

### 2. Authorship and the dedicated-agent option

The foreground agent can follow `skill-push` directly. SkillNote also ships a dedicated `skill-creator` agent definition. Its description offers creation/refinement triggers, its model is `inherit`, and its process permits reading relevant code after confirmation. This provides an optional specialist role; it does not establish that a dispatcher launches that agent for every creation request. The inspected hook manifest wires sync and context handlers, not a required skill-creator launch. The caller's actual handoff payload, child-context isolation and return channel remain unestablished. SRC-1, `plugin/agents/skill-creator.md`, `plugin/hooks/hooks.json`.

When invoked, the dedicated agent is instructed to understand the convention, draft the name, description and body, check quality, let the user select a collection, obtain approval and use the skill-push skill for persistence mechanics. This is delegation of a bounded authoring responsibility, followed by reuse of a procedure; invoking the procedure is not evidence of another model frame.

> 6. **Push** — Use the `skillnote:skill-push` skill for the push mechanics (check exists, POST or PATCH, handle errors).
> --- `plugin/agents/skill-creator.md`

The specialist's requested quality checks concern trigger keywords, short descriptions, actionable instructions and examples. They are agent judgments, not an independent test of task correctness. Its under-250-character description check is stricter than the 1024-character schema limit. The body-length guidance is likewise a prompt constraint, not an inspected API body-length check. SRC-1, `plugin/agents/skill-creator.md`, `backend/app/schemas/skill.py`, `backend/app/validators/skill_validator.py`.

### 3. Review and admission

`skill-push` directs the author to show the draft, GET the proposed slug, fetch collections, offer existing or new collection choices, then show the complete preview and wait for approval. The review supplies the user with the proposed content and description; the collection choice supplies the downstream scope label. The existence query supplies the author with the information needed to choose POST versus PATCH. The user can reject the preview or request revision, but the prompt defines no fixed critic loop, trial task or expected-answer oracle. SRC-1, `plugin/skills/skill-push/SKILL.md`; see the approval passage retained in [RT-RTE-registry-write](runtime.md#rt-rte-registry-write).

The author sends name, description, body and collections; POST also sends the slug. Backend schema and endpoint checks provide a second, different acceptance boundary. Name/description rules, collection presence, collection-name validity, collection capacity and slug conflicts can reject writes. These checks do not verify the instruction's utility or receive a user-approval receipt. SRC-1, `backend/app/schemas/skill.py`, `backend/app/validators/skill_validator.py`, `backend/app/api/skills.py`.

>     if not collections:
>         errors.append("At least one collection is required")
> --- `backend/app/validators/skill_validator.py`

On acceptance the backend stores current content, creates a content version, records activity, notifies MCP listeners on commit and returns skill detail. This is the registry delivery milestone, not publication of a ZIP archive. The authoring prompt then directs the agent to provide a viewing link. Persistence/version recovery and alternate admission paths remain as bounded in [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) and [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install).

### 4. Rejection and recovery

A concrete rejected path is an invalid new collection name. The endpoint checks canonicalized names and raises 422 `COLLECTION_NAME_INVALID`; the prompt assigns recovery to the authoring agent and user, not to an autonomous backend repair. SRC-1, `backend/app/api/skills.py`, `plugin/skills/skill-push/SKILL.md`.

> If the user types an invalid name, the POST /v1/skills call will return 422 `COLLECTION_NAME_INVALID`. Surface the error, explain the rule, and ask them to type a valid name before retrying.
> --- `plugin/skills/skill-push/SKILL.md`

A second rejection is a slug collision: the prompt says to switch from POST to PATCH after 409. The API supplies the conflict check; the author owns the decision to update existing content. That instruction does not provide an independent ownership check or require a new preview after every error. Connection refusal is listed as API unreachability, but the push procedure specifies no durable pending draft queue or automatic retry schedule. These are limits of this procedure, not claims about every client. SRC-1, `plugin/skills/skill-push/SKILL.md`, `backend/app/api/skills.py`.

### 5. Distribution and terminal result

On a subsequent configured session startup/resume/compact, the Claude Code hook runs sync. The code reads `.skillnote.json`, requests current content for the selected collections, prefixes the local name, adds collection information to the description, substitutes URL placeholders and writes project-local SKILL.md files plus a manifest. It therefore delivers transformed current instruction text, not the exact original payload or a selected published archive. The terminal implementation result is an installed file reachable by host discovery. SRC-1, `plugin/hooks/hooks.json`, `plugin/hooks-handlers/sync.sh`; [RT-RTE-project-sync](runtime.md#rt-rte-project-sync) retains the write and offline passages.

Network failure preserves existing cached instructions. A filtered empty response or bodyless response also protects caches, so successful registry editing does not imply that every project has received the new instruction. Normal accepted responses can remove stale managed files. The host remains responsible for selecting, reading and applying the skill. No task executor, expected-answer check or completed-task return is implemented by this distribution step. Later rating requests are a separate feedback path, not verification of delivery or correctness: [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report), [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions).

### Inspection extent

Additional direct inspection used SRC-1 `plugin/agents/skill-creator.md`, all of `plugin/skills/skill-push/SKILL.md`, `plugin/hooks/hooks.json`, `backend/app/schemas/skill.py` create/update definitions, `backend/app/validators/skill_validator.py`, `backend/app/api/skills.py` create/update bodies and `plugin/hooks-handlers/sync.sh` configuration through manifest persistence. The prompts supply doctrine/design evidence; backend and sync bodies supply implementation evidence. No target code was executed. The dedicated agent's actual launch, host context inheritance, reliable user interaction and later task benefit remain unobserved.

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

#### On [RT-RTE-registry-write](runtime.md#rt-rte-registry-write)

Workflow-specific responsibility: the optional skill-creator role owns understanding, drafting and requested quality checks; the user supplies collection choice and final approval; skill-push supplies existence checks and HTTP write/error mechanics. The optional role's procedure is retained above, rather than declared as another identity for registry authoring. No fixed caller-to-specialist payload or verified child-return protocol is established. User approval and structural API acceptance are distinct gates; neither supplies an expected-answer oracle.

#### On [RT-RTE-project-sync](runtime.md#rt-rte-project-sync)

Workflow-specific delivery boundary: committed authoring content is eligible for a later configured fetch, not pushed synchronously to every consumer by the authoring request. The file writer is the delivery executor; host discovery and application are external steps. Cached-file continuity recovers from unavailable fetches but can preserve instructions older than the newly reviewed registry version.
