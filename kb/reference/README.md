# Reference

Reference documentation for the shipped Commonplace system — how to work with your agent on a KB, how the system is put together, and where its contracts and decisions live.

For transferable methodology theory, see [kb/theory/](../theory/README.md). For writing conventions, each collection has a [COLLECTION.md](./COLLECTION.md) at its root.

## Working with your agent

You direct an agent toward outcomes rather than running procedures by hand. Ask in ordinary language for what you want; your agent discovers the current skills, collection contracts, and command `--help` on its own.

- **First time?** Start with [Getting started](./getting-started.md) — a worked example of turning a rough thought into a linked, source-grounded note.
- **Setup or broken commands?** See [INSTALL.md](../../INSTALL.md) (or ask your agent to run a health check).

| What you want to do | Does it edit your KB? | High-level overview |
|---|---|---|
| Write or update a note | Yes (creates or edits a file under `kb/`) | [Getting started](./getting-started.md) |
| Discover links for a note | No (writes a connect report for you to review) | [Connect skill](../instructions/cp-skill-connect/SKILL.md) |
| Ingest an external source | Yes (saves a local snapshot + tracked ingest) | `kb/sources/COLLECTION.md` |
| Check structural validity | No (deterministic validator, no LLM calls) | [Validation contract](./validation-contract.md) |
| Review notes semantically | No (`commonplace-review` never writes notes; paid launches) | [Review and editing system](./README-REVIEW-SYSTEM.md) |
| Improve, triage, or rewrite a note | Yes (simplification passes write uncommitted diffs; rewrites hold for approval) | [Review and editing system](./README-REVIEW-SYSTEM.md) |
| Search and navigate | No (uses `rg`, descriptions, curated heads, and links) | [Browse by topic](../tags/README.md) |
| Run CLI commands directly | Depends on command (`relocate` dry-runs without `--apply`) | [CLI commands](./commands.md) |

## Architecture and contracts

For exact implementation facts, inspect `src/commonplace/` (or locate the installed package with `commonplace-source`) and use each command's `--help`. These pages retain the stable boundaries, invariants, and contracts that code does not cheaply supply.

### System architecture and operation

- [Getting started](./getting-started.md) — first worked session with an agent
- [Review and editing system](./README-REVIEW-SYSTEM.md) — high-level operator overview of review, improvement modes, publication boundaries, and order of concerns
- [CLI commands](./commands.md) — complete checked catalogue of published `commonplace-*` commands
- [Commonplace architecture](./architecture.md) — installed topology, library/user ownership, skill stubs, and path invariance
- [Storage architecture](./storage-architecture.md) — authority and lifecycle boundaries among authored files, local copies, derived views, and operational state
- [Review architecture](./review-architecture.md) — code/worker ownership, durable state, freshness hash boundary, and checkout guard
- [Coordination between workflow runs](./workflow-architecture.md) — what crosses the boundary between workflow invocations
- [Documentation site](./documentation-site.md) — ProperDocs README-vs-index rule, nav generation, and landing-page inventory

### Type system, contracts, and authoring

- [Global type specs](../types/README.md) — shared type specs and schemas every collection can use
- [Collections and types](./collections-and-types.md) — how collection contracts and path-valued type specs compose and resolve
- [Validation contract](./validation-contract.md) — the four finding sources (`base`, `collection`, `type`, `schema`), base checks, directory artifacts, and unquoted-source limits
- [Content routing](./content-routing.md) — routing table from content kind to destination
- [Link vocabulary](./link-vocabulary.md) — linking approach, reader-need label catalogue, and lineage semantics
- [Vocabulary collision ledger](./vocabulary-collision-ledger.md) — tolerated near-collisions and writing decisions for new text
- [Vocabulary unification ledger](./vocabulary-unification-ledger.md) — candidate vocabulary unifications and current writing decisions
- Definitions: [Answerability](./definitions/answerability.md), [Collection and text contract](./definitions/collection.md), [Commonplace doctrine](./definitions/commonplace-doctrine.md), [Directory artifact](./definitions/directory-artifact.md), [Special collection](./definitions/special-collection.md)

## System-coupled notes and declarations

Commonplace develops its methodology by running on itself. The notes below record this repository's own declared frames, assessments, and local historical records — too coupled to Commonplace's choices to stand as general theory, and separate from the operational contracts above.

- [Epistemic stance](./epistemic-stance.md) — Popperian commitments this KB's assertions assume
- [Commonplace declared frame](./commonplace-declared-frame.md) — boundary under which self-improvement attributions hold
- [Source-adoption policy](./source-adoption-policy.md) — borrowing gates by source domain
- [Commonplace as an instrument](./commonplace-as-an-instrument.md) — what this KB tests in the design program
- [Design rationale management](./design-rationale-management.md) — how workshops, proposals, ADRs, contracts, and validators distribute rationale
- [Where change candidates come from in Commonplace](./where-change-candidates-come-from-in-commonplace.md) — noticing and candidate-drafting mechanisms in this repository
- [Agent memory coverage](./agent-memory-coverage.md) — how shipped surfaces map onto agent-memory requirements and current limits
- [Collections never own frontmatter semantics](./collections-never-own-frontmatter-semantics.md) — why the collection/type split is asymmetric
- [Collection prototypes](./collection-prototypes.md) — clone-once starter contracts for new collections
- [Control-plane goals](./control-plane-goals.md) — how `AGENTS.md` ships always-loaded KB goals and templates
- [Scenario architecture](./scenario-architecture.md) — scenario-derived decomposition of the installed surfaces
- [Tag-readme trace as a self-improving loop](./tag-readme-trace-as-self-improving-loop.md) — one observed trace mapped onto search, evaluation, and retention
- [Commonplace agent memory gap plan](./commonplace-agent-memory-gap-plan.md) — earlier gap-closure plan (unadopted roadmap)
- [Harness sub-agent model selection regression](./harness-sub-agent-model-selection-regression.md) — dated July/August Codex model-attribution incident record

## Decision history

Architecture decision records live under [adr/](./adr/). Each ADR records a decision at its date (later ADRs amend or supersede earlier clauses). Search ADRs by description with `rg "^description:" kb/reference/adr/ --glob "*.md"`.

## Collection boundary

- Use `kb/theory/` for transferable claims about KB methodology.
- Use `kb/reference/` for Commonplace's selections, shipped architecture/contracts, and system-coupled assessments.
- Use `kb/instructions/` for imperative procedures and promoted skills.
- Keep operational reference docs self-contained within the shipped library so consuming projects can read them without the source repository.
