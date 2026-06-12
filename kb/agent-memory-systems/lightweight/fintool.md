---
description: "Lightweight doc-grounded coverage of Fintool — a production finance agent whose founder reports S3-backed files, markdown skills, always-loaded user memories, and eval gates"
type: ../types/agent-memory-system-review.md
source-tier: doc-grounded
traits: [has-comparison, has-external-sources]
status: current
last-checked: "2026-06-02"
---

# Fintool

Fintool is an AI agent product for professional investors, covered here from a founder-authored practitioner report rather than inspectable application source. The report presents Fintool as a high-stakes finance agent built around normalized financial context, filesystem tools, markdown skills, S3-backed user data, sandboxed execution, and domain-specific evaluation. Because no reachable source was inspected, every mechanism below is **doc-grounded and reported**, not code-grounded.

**Source:** [snapshot of @nicbstme's public practitioner report](../../sources/lessons-from-building-ai-agents-for-financial-services-201517481849743.md) and its [local ingest report](../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md).

**Reviewed version:** X article created 2026-01-24; local snapshot captured 2026-03-03 and ingest dated 2026-03-09.

## Core Ideas

- **Filesystem-first product architecture.** The report says Fintool retired an embedding/RAG pipeline and moved to agentic filesystem search after adopting Claude Code's filesystem-first approach. S3 is reported as the source of truth for user data, with PostgreSQL serving as a derived index for fast list and metadata queries.
- **Markdown skills as the procedural surface.** Skills are reported as markdown files with YAML frontmatter and optional supporting references. Analysts and customers can author them directly, and a private > shared > public priority chain lets a user override a default skill by placing a replacement at the same path.
- **Context efficiency through normalization and progressive disclosure.** Fintool's reported context strategy has two layers: financial data is normalized into markdown, CSV/tables, and JSON metadata so retrieval returns cleaner context; skill discovery loads metadata first and full documentation only when a skill is activated, avoiding token waste from mounting every skill.
- **User memory as direct markdown injection.** The report describes `/private/memories/UserMemories.md` as a user-editable markdown file loaded on every conversation and injected as context, carrying preferences such as investment focus or comparison policy.
- **Evaluation as deployment control.** The report says Fintool maintains roughly 2,000 finance-specific test cases, 50 adversarial grounding cases, companion evals for every skill, and a pull-request gate when eval score drops more than 5%. These are reported process claims, not inspected tests.
- **Scaffolding is designed for deletion.** The founder argues that models will absorb many basic skills, so markdown is preferred over code because it is easier to update, shorten, or remove. Fiscal-period normalization remains the counterexample: the report frames it as a deterministic company-calendar problem, not something to leave to model intuition.

## Artifact analysis

Claim-level (no code inspected):

- **Storage substrate:** `files` — the central retained artifacts are reported as YAML/markdown files in S3, with PostgreSQL as a derived metadata/query index rather than the source of truth.
- **Representational form:** `prose` `symbolic` — skills and user memories are prose/markdown; metadata, watchlists, fiscal calendars, confidence scores, and eval records are symbolic. The source does not expose enough implementation detail to split every sub-artifact cleanly.
- **Lineage** — mixed authored/imported/derived: skills are reportedly authored by analysts or customers, user memories by users, financial context by imported source data normalized through a parsing pipeline, PostgreSQL rows by S3 sync, and eval outcomes by test execution. The report does not document a durable agent-trace-to-memory distillation loop.
- **Behavioral authority** — skills act as **system-definition artifacts** because they instruct task execution; user memories and normalized financial documents act as **knowledge artifacts** injected or retrieved as context; eval suites act as system-definition artifacts at deployment time by blocking regressions. Effective runtime obedience is not verified.

## Comparison with Our System

Fintool and Commonplace make the same substrate bet: behavior-shaping knowledge should remain inspectable and agent-readable, while derived indexes provide query capabilities files alone do not. Commonplace turns that bet into typed markdown, link semantics, validation, and generated indexes for an agent-operated methodology KB. Fintool's reported version is a commercial product architecture: S3 durability, access-controlled prefixes, SQL discovery, sandbox tools, and low-friction user or analyst customization in one finance domain.

The useful divergence is governance. Commonplace emphasizes reviewable accumulated knowledge; Fintool emphasizes operational context delivery to paying users under high accuracy pressure. That makes Fintool strong convergence evidence for filesystem-first context engineering at product scale, but a weak architecture source until implementation docs, source, or test internals are inspectable.

### Borrowable Ideas

- **Copy-on-write skill shadowing.** Ready to borrow conceptually. A private > shared > public resolution chain would let Commonplace installations override skills without forking the shared methodology, provided validation can show which version won.
- **Adversarial grounding tests.** Ready as an evaluation pattern. Plant false material beside real source material, then require the model to cite the real source; this maps cleanly to the [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md).
- **User-editable memory file.** Needs a concrete user-preference layer first. A single markdown file injected into every session is a simple constraining surface, but Commonplace would need ownership, privacy, and scope rules before adopting it.
- **S3 source of truth plus derived query index.** Useful as production evidence rather than an immediate migration target. Commonplace's repo substrate already supplies versioning and inspection; the Fintool pattern matters when a consuming product needs multi-user storage, access control, and fast metadata queries.

## Write side

**Write agency:** `manual` — the reported durable skills and user memories are authored by analysts, customers, or users through the product's file/skill surfaces; the source reports normalization and indexing infrastructure but not an autonomous memory-curation loop.

## Read-back

**Read-back:** `push` — the report says user memories are loaded and injected on every conversation, which is unsolicited from the agent's perspective. This is unconditional always-load, not a relevance-gated activation path, so it does not warrant `push-activation`.

## Curiosity Pass

- The strongest reported novelty is not "files instead of databases" by itself; it is the layered combination of S3 as source of truth, PostgreSQL as derived index, SQL skill selection, and copy-on-write override.
- The report treats analyst/customer-authored skills as easy to maintain, but does not expose adoption data, review policy, or failure handling when a user skill is wrong.
- The "model will eat your scaffolding" thesis is plausible for proxy-theory skills, but the source itself provides calculator-regime counterexamples such as fiscal-period normalization and ticker history.
- Simpler alternative worth checking: whether a repo-backed or local-file implementation can get most of the skill-shadowing benefit before needing S3, Lambda, and PostgreSQL.

## What to Watch

- Public source, SDK, architecture docs, or test artifacts. If inspectable implementation appears and is read, this should promote from lightweight coverage to `agent-memory-system-review`.
- More detail on skill shadowing: conflict resolution, validation, auditability, and how often customer-authored skills are actually used.
- Whether always-loaded user memories remain a small preference file or grow into a context-dilution problem requiring relevance-gated read-back.
- Whether the S3-first pattern continues to hold for workloads needing complex relational queries, transactions, or stronger consistency than the report's file/list/read split.

## Relevant Notes

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — evidence: Fintool reports S3 as source of truth with PostgreSQL as a derived index for fast queries
- [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md) — evidence: the reported eval suite and adversarial grounding tests are a production example of oracle hardening
- [fixed artifacts split into exact specs and proxy theories](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — rationale: "model eats scaffolding" applies unevenly across proxy-theory skills and exact-spec modules
- [Agent Skills for Context Engineering](../reviews/agent-skills-for-context-engineering.md) — compares-with: both use markdown skill packages, frontmatter discovery, and progressive disclosure, but Fintool is doc-grounded product coverage
- [Sig](./sig.md) — compares-with: both are lightweight product reports for file-backed agent memory, with Fintool at commercial finance scale and Sig at personal/workplace capture scale
