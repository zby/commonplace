---
source: https://generativeprogrammer.com/p/emerging-markdown-formats-that-shape
description: "Map distinguishing standing rules, repeatable procedures, versioned plans, domain files, and machine-local memory in agent-ready repositories"
captured: 2026-08-03
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Emerging Markdown Formats That Shape Coding Agent Behavior

Author: Bilgin Ibryam
Source: https://generativeprogrammer.com/p/emerging-markdown-formats-that-shape
Date: 2026-08-01

For years, the knowledge required to change software lived in many places. Non-functional requirements (NFRs), architectural constraints, and design decisions were captured in solution architecture documents, ADRs, security reviews, and wikis. Product intent lived in design documents and mockups. Work was broken down into tickets. Operational lessons survived in incident reports, Slack threads, playbooks, and the heads of experienced developers.

The repository contained the implementation: source code, tests, configuration, and dependency manifests. Developers read across the surrounding artifacts, reconciled the desired outcome with architectural judgment, and translated both into code.

As AI-assisted coding becomes normal, the repository is becoming the meeting point between that project knowledge and the agent changing the software. A monorepo brings codebases and their dependency graph together. An agent-ready repository also brings in the knowledge required to change them correctly.

Software has always been understood through different lenses: principles and NFRs, architecture and design, concrete specifications, implementation plans, domain rules, and lessons learned during operation. A growing family of Markdown files now captures these dimensions in forms that coding agents can discover and use. This article looks at the formats and tools that are emerging. Together, they let an agent act as an intent compiler, translating human intent and judgment into source code.

[![Project knowledge moves from scattered systems into an agent-ready repository guided by Markdown formats](https://substackcdn.com/image/fetch/$s_!9qxG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f720c0d-3430-46e0-827e-587872f51833_1700x930.png)](https://substackcdn.com/image/fetch/$s_!9qxG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f720c0d-3430-46e0-827e-587872f51833_1700x930.png)

## Agent onboarding starts with a README for agents

A human onboards to a project once. An agent effectively onboards every time it starts a task. It needs to orient itself in the repository, discover the relevant commands and conventions, and understand the rules that apply before it changes anything.

[AGENTS.md](https://agents.md/)  is the closest thing to a neutral standard for this purpose. The project describes it as a README for agents. A root file can explain the repository structure, build commands, tests, coding conventions, and pull request expectations. Nested files can add instructions for a package or subsystem. The format deliberately has no required fields.

The ecosystem also has vendor-native alternatives that serve the same purpose:

- [AGENTS.md](https://agents.md/)  provides cross-tool project guidance for Codex, Cursor, Cline, Copilot, OpenCode, and other compatible agents.
- [CLAUDE.md and .claude/rules/](https://code.claude.com/docs/en/memory)  provide standing and path-scoped guidance for Claude Code.
- [GEMINI.md](https://geminicli.com/docs/cli/gemini-md/)  provides hierarchical context for Gemini CLI.
- [.github/copilot-instructions.md and path-specific instruction files](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)  guide GitHub Copilot.
- [.clinerules/](https://docs.cline.bot/customization/cline-rules)  carries persistent and conditional rules for Cline.

Use `pnpm`, not `npm`. Do not edit generated clients. Run the billing integration tests after changing an invoice flow. Read the relevant ADR before moving a service boundary. These are standing instructions that should remain true across many tasks.

Once the agent understands the repository, the next question is how to perform a particular kind of work.

## Skills package repeatable procedures

A skill is a playbook tailored to a particular kind of work.

Consider a database migration. `AGENTS.md` might state that every schema change needs a rollback path. A migration skill can describe the complete procedure: inspect the current schema, create the migration, update generated types, run compatibility checks, verify the rollback, and prepare the review summary.

The open [Agent Skills specification](https://agentskills.io/specification)  gives that playbook a portable package. Each skill has a required `SKILL.md` containing metadata and instructions. It may also include scripts, references, templates, and other assets. Agents initially see the metadata, load the full instructions when the skill is relevant, then access supporting material as needed.

Agent Skills [originated at Anthropic](https://agentskills.io/home)  and were released as an open standard. They are separate from MCP, which Anthropic contributed to the [Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation). The skill format is now documented by [Codex](https://developers.openai.com/codex/skills/), [Gemini CLI](https://geminicli.com/docs/cli/creating-skills/), [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), and other compatible clients.

The boundary is concrete:

- `AGENTS.md` and native rule files describe standing context and constraints.
- `SKILL.md` describes a repeatable procedure invoked for a specific task.

A procedure explains how to work. It still needs a reviewed description of what should be built.

## Planning files make software design reviewable

Software design, planning, and task breakdown are also moving into versioned Markdown. When they exist only in chat, they disappear into session history. When they become repository artifacts, architects and developers can review them before an agent turns them into implementation.

[GitHub Spec Kit](https://github.github.com/spec-kit/index.html)  is the clearest mainstream example. Its documentation reports more than 121,000 GitHub stars and 35 coding-agent integrations. Its default workflow uses a chain of files:

1. `spec.md` records the requirements and desired outcome.
2. `plan.md` explains the technical design and implementation approach.
3. `tasks.md` breaks the plan into executable units.
4. The agent implements and validates the change.

A project constitution can carry principles that should apply across many changes.

Spec Kit is not the only approach. [OpenSpec](https://github.com/Fission-AI/OpenSpec), [Kiro Specs](https://kiro.dev/docs/specs/quick-spec/), and project-specific [PLANS.md](https://developers.openai.com/cookbook/articles/codex_exec_plans)  use different files and workflows. They are nevertheless converging on a recognizable sequence: requirements, design, plan, tasks, implementation, and validation become separate artifacts that humans can review and agents can follow.

These files describe a generic software development lifecycle. Applications also need instructions for their particular domain.

## Domain files give agents specialized context

A frontend, an identity platform, and a data pipeline do not need the same context. Domain files give agents specialized instructions for the parts of a system that generic onboarding, skills, and plans cannot fully describe.

- `ARCHITECTURE.md` can describe system boundaries, components, dependencies, NFRs, and long-lived architectural decisions. It is an established human documentation convention that becomes operational for agents when project instructions tell them when to read it.
- Google Labs’ [DESIGN.md](https://github.com/google-labs-code/design.md)  describes visual identity, design tokens, components, and design rationale. The project currently labels the format alpha.
- WorkOS’ [AUTH.md](https://github.com/workos/auth.md)  is an experimental, service-hosted recipe that teaches agents how to register and authenticate on behalf of users.
- Kilo’s [REVIEW.md](https://kilo.ai/docs/automate/code-reviews/overview)  lets a repository define review priorities, severity, skipped files, verification expectations, and how a review agent should divide work.

These formats have different maturity levels and scopes. `ARCHITECTURE.md` is a long-standing documentation convention. `DESIGN.md`, `AUTH.md`, and `REVIEW.md` are emerging, domain-specific experiments. Their common direction is clear: more specialized engineering knowledge is becoming directly legible to agents.

Some of that knowledge is designed in advance. Other knowledge emerges only while the software is being built and operated.

## Memory makes learned context durable

An unexpected build prerequisite, a debugging pattern, or the reason a deployment failed might previously have ended up in a ticket comment, commit message, Slack thread, incident report, or SRE playbook. Those records range from ephemeral to durable, but a coding agent may not find the relevant lesson when it begins the next task.

Agent memory keeps learned context associated with a repository and available across sessions. Claude Code makes the authorship distinction unusually clear:

- Humans write `CLAUDE.md` to provide shared instructions, conventions, and project context.
- Claude writes auto memory into a `MEMORY.md` index and optional topic files such as `debugging.md` and `api-conventions.md`.

The auto memory is repository-specific but machine-local. Claude normally stores it outside the Git repository, and it is not automatically shared with the team. [Anthropic documents the two mechanisms separately](https://code.claude.com/docs/en/memory).

Memory therefore does not replace tickets, commit history, or operational documentation. It reduces repeated rediscovery. When a learned fact becomes important to the whole team, it needs a promotion path:

1. The agent records a tentative observation in local memory.
2. A human reviews it when the observation recurs or affects shared work.
3. Durable knowledge moves beside the source code into a project rule, skill, ADR, or domain document.

Tentative knowledge stays local. Reviewed knowledge becomes shared. Kilo is experimenting with a similar loop for review: it can [analyze how a team responds to review comments and propose changes](https://blog.kilo.ai/p/code-reviews-md)  to the repository’s review guidance.

## Putting the Markdown files together

[![The metacode layer maps an agent-ready project structure to the project knowledge each format carries](https://substackcdn.com/image/fetch/$s_!bvTU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9d08c07-5f5c-4258-a408-a2d13466082e_1700x900.png)](https://substackcdn.com/image/fetch/$s_!bvTU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9d08c07-5f5c-4258-a408-a2d13466082e_1700x900.png)

*Shared project files carry reviewed knowledge beside the source code. Agent-written memory remains machine-local until a durable lesson is promoted into the repository.*

The practical distinction is the role each file plays, who writes it, and how broadly it is supported.

[![A comparison of agent-facing Markdown files by their role, typical author, and support status](https://substackcdn.com/image/fetch/$s_!Bog3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b62e4cb-f419-479e-a3ed-f3a387c7f9e2_1700x1398.png)](https://substackcdn.com/image/fetch/$s_!Bog3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b62e4cb-f419-479e-a3ed-f3a387c7f9e2_1700x1398.png)

*The formats range from cross-tool standards and established vendor conventions to emerging domain-specific experiments.*

A project does not need every file. Use the smallest set that agents can reliably discover, keep reviewed knowledge beside the source code, and treat vendor-specific files as thin compatibility bridges when another file is canonical. `AUTH.md` remains service-hosted, while Claude’s auto memory stays machine-local until a human promotes a durable lesson into the repository.

## The takeaway

The repository is becoming the meeting point between source code and **metacode**: the Markdown that carries requirements, NFRs, architecture, design, rules, procedures, plans, and durable learning.

When agents can read both, they act as intent compilers. Source code becomes a byproduct: the executable result of human intent and judgment made legible to the agent.

The engineering task is to keep that metacode scoped, reviewed, and current. It does not replace testing or review. It gives the next code change a better source.
