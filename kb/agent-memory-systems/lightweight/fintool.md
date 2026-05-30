---
description: "Lightweight coverage note for Fintool, a production AI agent for professional investors whose practitioner report documents an S3-first filesystem architecture, markdown skills with copy-on-write shadowing, and oracle-hardened evaluation"
type: kb/types/note.md
traits: [has-comparison, has-external-sources]
status: current
---

# Fintool

Fintool is tracked here as lightweight related-system coverage, not as an `agent-memory-system-review`. The coverage comes from a [practitioner report ingest](../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) of a [public write-up by @nicbstme](https://x.com/nicbstme/status/2015174818497437834), the product's founder. There is no inspectable application source, so this note records the reported architecture without treating its claims as code-grounded findings. The review type requires accessible source code, so Fintool stays in `lightweight/` until that exists and is inspected.

Fintool is an AI agent for professional investors, built over two years in a domain with near-zero tolerance for factual error. Its founder's central thesis is that "the model is not the product — the experience around the model is the product," and the report distils eleven production lessons. The system is the strongest production-scale, commercial evidence in this collection for the filesystem-first bet, drawn from paying customers rather than a research benchmark.

## Source-visible design

**S3-first with a derived PostgreSQL index.** S3 is the source of truth; a Lambda function syncs writes into PostgreSQL as a derived index, so lists read from the DB while freshness reads come from S3. Two Lambdas run the sync — a real-time SNS-triggered path plus a 3-hour reconciliation sweep. This is production-grade [files-not-database](../../notes/files-not-database.md): files as durable, auditable source of truth with a query index layered on top, claimed at 11-nines durability.

**Markdown skills as the product surface, with copy-on-write shadowing.** Skills are markdown-with-frontmatter, discovered via SQL metadata queries and loaded fully only on activation (progressive disclosure at the infrastructure level). A private > shared > public priority chain lets a user drop their own `SKILL.md` at the same path to override the shared one without forking — a per-user customization mechanism this KB does not currently have.

**User memories as injectable markdown.** A `UserMemories.md` the user edits directly is injected as context on every conversation ("I focus on small-cap value stocks"). This is user-facing constraining: the user narrows the agent's interpretation space by writing preferences in the same medium the agent reads.

**Agentic search over RAG.** The team retired its embedding/RAG pipeline in favor of agentic filesystem search, explicitly following Claude Code's filesystem-first approach — reportedly against contemporary consensus ("people thought we were crazy").

**Oracle-hardened evaluation as a deployment gate.** ~2,000 domain-specific test cases, with PRs blocked if the eval score drops more than 5%. Adversarial grounding (planting false numbers in context and checking the model cites the real source, ~50 cases) hardens against hallucination. Fiscal-period normalization across 10,000+ company calendars is handled deterministically — a clean calculator-regime case where the spec *is* the problem and the model will not absorb it.

**"The model will eat your scaffolding."** An explicit design principle: prefer markdown over code because it is easy to update and delete, write skills for current leverage, and delete them as models improve. The author distinguishes scaffolding that gets absorbed (vision-feature regime) from scaffolding that persists (the fiscal-calendar calculator regime), though the report conflates the two more than the [bitter-lesson boundary](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) framing would.

## Comparison with Our System

Fintool and commonplace make the same substrate bet: agent-readable files as the source of truth, with derived indexes for what files alone can't answer. The difference is governance versus throughput. Commonplace wraps its files in typed markdown, validation, link semantics, and indexes so the corpus stays reviewable; Fintool's reported emphasis is operational — durability, sync, and low-friction customization for paying users in a single high-stakes domain.

The most useful divergence is audience and evidence tier. Commonplace is an agent-operated methodology KB maintained by technical users and scripts; Fintool is a commercial product whose architecture we know only from a self-reported write-up. That makes Fintool strong *convergence* evidence for filesystem-first at commercial scale, but weak as reviewed architecture — the failed alternatives, the real skill-authoring adoption data, and the test-case internals are not visible.

## Borrowable Ideas

**Copy-on-write skill shadowing (private > shared > public).** The one genuinely new pattern here. A priority chain that lets per-installation overrides win without forking, working precisely because skills are files in a homoiconic medium. The recommended follow-up is a note on how this bridges methodology-distilled skills and expert-authored skills.

**Adversarial grounding as an evaluation technique.** Inject fake data alongside real data and verify the model cites the real source — a concrete, replicable way to harden a hallucination oracle, relevant to the [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md).

**User-editable injected memory file.** A single `UserMemories.md` loaded every conversation is a minimal, schema-free constraining surface worth borrowing if commonplace grows a user-preference layer.

## Review boundary

Do not create `kb/agent-memory-systems/reviews/fintool.md` unless inspectable application source or implementation documentation becomes available. The current evidence is a founder's practitioner report; storage model, sync internals, skill-shadowing implementation, and evaluation harness are all self-reported claims, not code-grounded findings.

## What to Watch

- Whether any Fintool source, SDK, or architecture documentation becomes publicly inspectable
- Whether the copy-on-write skill-shadowing mechanism is documented in enough detail to borrow concretely
- Whether the "model eats scaffolding" prediction is borne out — which skills actually become one-liners versus which persist
- Whether the S3-first pattern is reported to hold under workloads with complex relational or transactional access

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — exemplifies at production scale: S3 source of truth, PostgreSQL derived index, user data as YAML/markdown
- [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md) — exemplifies: ~2,000 test cases and adversarial grounding manufacture and amplify hard oracles, with a 5%-regression deployment gate
- [fixed artifacts split into exact specs and proxy theories](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — "the model will eat your scaffolding" is the bitter-lesson boundary applied to agent infrastructure; fiscal-period normalization is the calculator-regime counterexample
- [Agent Skills for Context Engineering](../reviews/agent-skills-for-context-engineering.md) — compares: independent convergence on markdown-with-frontmatter skills, progressive disclosure, and SQL-driven lazy loading
- [Sig](./sig.md) — compares: both are lightweight, repo-less product coverage betting on files-first agent memory, Fintool at commercial finance scale and Sig at personal workplace scale
