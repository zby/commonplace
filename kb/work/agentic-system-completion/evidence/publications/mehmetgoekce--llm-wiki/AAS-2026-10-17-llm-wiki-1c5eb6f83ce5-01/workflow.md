---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llm-wiki workflow account tracing source ingest from user request through page admission, self-check and reported delivery."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
---

# llm-wiki workflow report

## Workflow account

### Selection and evidence

The representative workflow is `/llm-wiki ingest <source>`, selected because the skill labels ingest its default workflow and explicitly connects source analysis, existing-state inspection, page writes, a quality gate and a terminal report. It is one prescribed multi-step operation, not a chain assembled from unrelated commands. Its canonical route is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); this member adds workflow annotations rather than redeclaring that route.

The evidence is doctrine/design in SRC-1, `SKILL.md`, at the frozen revision. Inspection here covers configuration, format and L1/L2 instructions, the complete ingest procedure, the adjacent query procedure and final constraints. These passages confirm and focus the runtime baseline's already inspected scope; no new source or execution evidence is introduced. This account describes requested behavior, not a successful ingest run.

### Request, ownership and inputs

The user delegates knowledge maintenance to the foreground Claude Code agent by supplying a URL, file or text. The skill maps those inputs to WebFetch, Read or direct parsing. It supplies the maintainer role and the sequence; the agent interprets the material and owns progression. There is no separate worker handoff in this ingest procedure: tool calls acquire data or perform effects, not independent delegated judgment. Host tool execution and permissions remain external, as described in [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) and [RT-BAP-skill-dispatch](runtime.md#rt-bap-skill-dispatch) (SRC-1, `SKILL.md`).

Before processing, the configuration instructions require the agent to resolve the installed wiki root and read `llm-wiki.yml`. Tool and path settings select the persisted format: Logseq outliner pages with block properties, or Obsidian Markdown with YAML. The agent then extracts entities, facts, relationships, dates and decisions, classifies them, and distinguishes quick rules to recommend for Memory from deep knowledge for the wiki. This recommendation does not establish an L1 write. It reads the retained Schema, locates candidate pages with Glob, reads existing targets and chooses creations, updates and cross-references. Those inputs pass between phases within the same foreground context, not through a typed task envelope (SRC-1, `SKILL.md`; [RT-OBJ-schema](runtime.md#rt-obj-schema), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

### Transformation and consequential handoff

The agent writes new pages with required properties. For existing state, it distinguishes an additional fact from a superseding fact: the latter replaces current wording while preserving the old wording in dated collapsed History. It also updates dates and cross-references. The ordinary target is 5–15 page touches; the later check warns outside 5–20. Neither number is an independent correctness test (SRC-1, `SKILL.md`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

The important downstream handoff is not to another agent. It is from the ingest writer to a later query invocation through retained hub routing descriptions:

>   - Maintain the hub routing line (REQUIRED for every created/updated page): in the hub's `### Index`
>     section, set/update the routing line — `[[Wiki/NS/Page]] -- <one-sentence description, <=120 chars> #tag #tag`.
>     New page -> append a line; refocused page -> refresh the description. The description is the routing
>     key for query Phase 0 — keep it terse, distinctive, no filler ("Notes about ...").
> --- `SKILL.md`

The later selector initially receives a compressed description and tags rather than every full page. Query matches those lines to the question, selects three children with a maximum of five, then reads selected pages. Thus saving a page alone does not establish preferred discoverability: ingest must maintain its routing entry. Query's fallback scan can still find pages when routing fails, so missing routing is not an access prohibition. This is a specified later consumption path, not observed answer improvement (SRC-1, `SKILL.md`; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)).

### Verification, rejection and recovery

The same foreground agent performs the post-write quality gate: required properties, cross-references, routing lines, credential exclusion and page-touch warning. The baseline retains the gate's verbatim passage in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Schema and skill rules supply structural criteria, not known-correct answers to the source's factual claims. There is no separate reviewer or independent truth oracle specified in these phases. The user initiates ingest but is not asked to approve each admitted fact; the model both proposes and writes the transformation (SRC-1, `SKILL.md`).

A supported early rejection path is missing configuration:

> Read `llm-wiki.yml` from the wiki root FIRST (every command except `setup`, which creates it). If the
> file is missing, stop with: "llm-wiki.yml not found in <wiki root>. Run /llm-wiki setup to create one."
> --- `SKILL.md`

Here the agent stops and returns recovery guidance; the user must invoke setup before retrying. An unresolved root also requires a stop rather than guessing. A conflicting configured path is different: the agent warns and continues using the installed root. These are prompt policies, not filesystem-enforced guards (SRC-1, `SKILL.md`).

The inspected ingest phases do not specify a failed-quality-gate retry loop, transactional rejection or automatic rollback after writes. Their order places checking after page operations. It would therefore be misleading to describe the gate as an atomic admission barrier. The final report can expose warnings and skipped items; History preserves superseded statements and Git supplies a manual recovery affordance, not guaranteed restoration. This limit concerns the shipped ingest procedure and final constraints, not arbitrary host recovery behavior (SRC-1, `SKILL.md`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

### Delivery

The prescribed terminal result is persisted page and routing changes plus a user-facing summary of pages created, pages updated, cross-references added, warnings and skipped items. Final constraints additionally require a Git commit after every structural change; ingest does not spell out commit failure handling. The report is the foreground agent's return, not a worker result awaiting a separate integration step. These completion instructions establish neither a successful commit nor factual correctness, subsequent retrieval, actual compliance or measured benefit (SRC-1, `SKILL.md`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

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

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow selection: the ingest branch is the representative default operation; the import branch is not traced here. Phase transitions are foreground-agent progression, not worker scheduling or child-context returns. The load-bearing delivery dependency is maintaining routing descriptions alongside pages so a later query can select the retained content. The quality check follows writes and does not specify automatic rollback or a rejection/retry controller. Completion combines the terminal change/warning report with the global structural-commit instruction; successful execution remains unobserved.
