---
description: "ARIS research-skill harness with markdown workflows, cross-model review loops, a small research wiki, verifier-backed paper audits, and trace-derived meta-optimization of its own skills"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-25"
---

# ARIS

ARIS (Auto-claude-code-research-in-sleep) is a skill-pack and lightweight CLI/helper toolkit by wanshuiyin for running ML research workflows inside Claude Code, Codex, Cursor, Trae, Antigravity, and adjacent agent harnesses. It is not primarily a memory database. Its memory-relevant contribution is a file-backed research control plane: markdown skills define workflow phases, project artifacts carry state between phases, a `research-wiki/` stores papers/ideas/experiments/claims, external reviewers judge research and paper quality, and a meta-optimization loop can mine hook logs into proposed patches to the skill system itself. Repository: <https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep>.

**Repository:** https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

**Reviewed commit:** https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/544c1dbe2a934d45487a2508caa9a786e65a59fa

## Core Ideas

**The main substrate is executable markdown workflow, not a daemon.** The top-level [`README.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/README.md) frames ARIS as a "methodology, not a platform," and the code backs that up: the repo contains 68 `SKILL.md` directories plus a small set of Python/Bash helpers and MCP bridges. [`AGENT_GUIDE.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/AGENT_GUIDE.md) is the routing index for agents, while the actual behavior lives in skill files such as [`research-pipeline/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/research-pipeline/SKILL.md), [`auto-review-loop/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/auto-review-loop/SKILL.md), and [`paper-writing/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/paper-writing/SKILL.md). The design is deliberately portable: the skill files and artifacts are ordinary project files, with helper scripts filling in the places where prose alone proved too soft.

**Workflow state is carried by named artifacts.** The research lifecycle is organized around files like `idea-stage/IDEA_REPORT.md`, `EXPERIMENT_LOG.md`, `review-stage/AUTO_REVIEW.md`, `review-stage/REVIEW_STATE.json`, `NARRATIVE_REPORT.md`, and `paper/.aris/assurance.txt`. The auto-review loop explicitly writes `REVIEW_STATE.json` after each round so compaction or interruption can resume from a concrete state file. This makes ARIS closer to a workshop control plane than to a retrieval memory system: the files exist to keep a live research run moving, not to build a general-purpose knowledge library.

**Research Wiki is a small typed project memory with generated views.** [`research-wiki/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/research-wiki/SKILL.md) defines four entity types (`papers`, `ideas`, `experiments`, `claims`) plus typed edges in `graph/edges.jsonl`. The implementation in [`tools/research_wiki.py`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/research_wiki.py) creates the directory structure, ingests arXiv or manually supplied paper metadata, deduplicates by arXiv ID and slug, rebuilds `index.md` and `query_pack.md`, and appends receipts to `log.md`. The wiki is intentionally modest: extraction of paper content and relationships is still skill-mediated, but the artifact schema and generated query pack give later skills a compact, durable field map.

**Cross-skill integrations are being hardened into helper-plus-verifier contracts.** The strongest architectural document is [`integration-contract.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/shared-references/integration-contract.md). It says prose can describe an integration but cannot guarantee it; load-bearing integrations need an activation predicate, canonical helper, concrete artifact, visible checklist, backfill path, and verifier or diagnostic. The repo implements this for Research Wiki ingest via `research_wiki.py ingest_paper` plus [`verify_wiki_coverage.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/verify_wiki_coverage.sh), and for submission audits via [`verify_paper_audits.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/verify_paper_audits.sh). This is the best part of ARIS as methodology: it turns "the agent should remember to run X" into a receipt-bearing integration.

**Submission assurance is separated from work intensity.** [`assurance-contract.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/shared-references/assurance-contract.md) splits `effort` from `assurance`. At submission level, proof, claim, and citation audits must each emit JSON verdicts from a six-state machine (`PASS`, `WARN`, `FAIL`, `NOT_APPLICABLE`, `BLOCKED`, `ERROR`); [`verify_paper_audits.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/verify_paper_audits.sh) validates required fields, rehashes audited inputs to catch stale artifacts, checks trace paths, and exits nonzero for blocking submission states. This is not memory in the storage sense, but it is behavior-changing institutional memory: a previously observed silent-skip failure has been codified into an executable gate.

**The meta-optimization loop learns from harness traces, but only as patch proposals.** [`templates/claude-hooks/meta_logging.json`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/templates/claude-hooks/meta_logging.json) installs Claude Code hooks that call [`tools/meta_opt/log_event.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/meta_opt/log_event.sh). The logger appends JSONL records to project and global `.aris/meta/events.jsonl`, including skill invocations, tool failures, slash commands, user prompts, Codex calls, session starts, and session ends. [`meta-optimize/SKILL.md`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/skills/meta-optimize/SKILL.md) then analyzes frequency, failure, convergence, and human-intervention patterns, proposes minimal diffs to `SKILL.md` files, and sends them through cross-model review before user-approved application. The key restraint is that it does not auto-mutate the harness; trace-derived learning stops at reviewed patch proposals.

**Distribution is a first-class part of the memory story.** [`tools/install_aris.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/install_aris.sh) installs flat per-skill symlinks with a manifest, lock directory, exact target revalidation, slug checks, and safe uninstall/reconcile behavior. [`tools/smart_update.sh`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/544c1dbe2a934d45487a2508caa9a786e65a59fa/tools/smart_update.sh) handles copied installs and detects likely personal customizations. This matters because ARIS's learned or revised knowledge lives in files that must propagate into agent discovery surfaces; packaging drift would be memory drift.

## Comparison with Our System

| Dimension | ARIS | Commonplace |
|---|---|---|
| Primary goal | Run autonomous ML research and paper-writing workflows | Build durable methodology knowledge for agents and maintainers |
| Main substrate | Markdown skills plus project-stage artifacts | Typed notes, indexes, instructions, sources, reviews |
| Memory role | Workshop continuity, research wiki, audit receipts, trace-derived skill patches | Library knowledge, semantic links, validation, review state |
| Knowledge structure | Four wiki entity types plus edges; many workflow-specific artifacts | Collection-local types with frontmatter schemas and link vocabulary |
| Verification | Cross-model review plus helper/verifier scripts for specific gates | Deterministic validation plus semantic review bundles |
| Trace-derived learning | Hook logs become proposed skill diffs through `/meta-optimize` | Review results and notes are curated, but no general trace miner |
| Integration surface | Claude/Codex skills, MCP reviewer bridges, local scripts | Repo-native KB plus `commonplace-*` commands and installed skills |

ARIS is stronger as a live workshop system. It has practical answers to "what file should exist after this phase?", "how does a long loop resume?", "how do we prevent a skipped audit from being mistaken for success?", and "how does a project-local skill pack update without clobbering user edits?" Commonplace has more mature library semantics: typed artifacts, link labels, collection contracts, validation over the whole KB, and reviews that are intended to accumulate as reusable landscape knowledge.

The deepest difference is the permanence target. ARIS mostly accumulates action capacity inside an active research project: run state, reviewer feedback, paper audit artifacts, and a local field map for that project. Commonplace accumulates transferable methodology. ARIS's Research Wiki resembles a small project-specific source/claim graph, but it is not trying to become a general knowledge base with cross-note argument structure. Its most transferable mechanism is the integration-contract pattern: turn remembered operational failures into helper-owned receipts and verifier-owned gates.

## Borrowable Ideas

**Integration contract for cross-skill promises.** Ready to borrow now. Commonplace has several procedures where one step "should" call another skill or regenerate an artifact. ARIS's six-part contract is a compact way to decide when prose is not enough: observable predicate, helper, artifact, checklist, backfill, verifier/diagnostic. This belongs in our instruction-writing guidance and in future workflow reviews.

**Assurance as an axis separate from effort.** Ready to borrow conceptually. Our review system already separates structural validation from semantic review, but ARIS's `effort` vs `assurance` split is a useful naming pattern for workflows where depth/cost and gate strictness are different choices.

**Always-emitted verdict artifacts.** Ready to borrow where we have load-bearing gates. `NOT_APPLICABLE` is especially useful: it distinguishes "we checked and nothing applies" from "the agent silently skipped the step." That distinction would improve any future commonplace publication/export/checklist workflow.

**Project wiki query pack.** Needs a specific use case. ARIS's `query_pack.md` is a generated, budgeted view over papers, failed ideas, and relationships. Commonplace already uses indexes and descriptions, but a workshop-local "query pack" could be useful for active investigations that should not enter the library yet.

**Trace-derived skill patch proposals.** Needs a use case and stronger evaluation. ARIS's meta-optimize loop is right to stop at proposed diffs plus reviewer judgment. For commonplace, a similar loop could mine repeated validation failures, review findings, and user corrections into candidate instruction edits, but it would need strong semantic QA before touching core methodology.

**Manifest-managed skill installation.** Ready to borrow if commonplace's skill distribution grows more complex. The flat symlink plus manifest-reconcile model is a concrete solution to skill discovery and update drift.

## Trace-derived learning placement

ARIS qualifies as trace-derived learning through `/meta-optimize`, not through the whole research pipeline.

**Trace source.** Claude Code hook events written by `meta_opt/log_event.sh`: skill invocations, tool successes/failures, slash commands, user prompts, Codex calls, session starts, and session ends. The traces are structured JSONL, not raw transcripts.

**Extraction.** The `meta-optimize` skill analyzes usage frequency, repeated failures, convergence behavior, and human interventions, then asks the agent to produce concrete patch proposals against skills, reviewer prompts, defaults, convergence rules, workflow ordering, or cautious schema changes. Patch review is delegated to a different model before recommendation.

**Representational form.** Symbolic/readable artifacts. The learned output is a proposed diff to markdown skills or adjacent workflow definitions, plus reports and backup/log records if the user applies it. No model weights and no opaque memory store.

**Behavioral authority.** System-definition, not fact memory. The target artifact changes future agent behavior because `SKILL.md` is executable procedure text.

**Scope.** Per-project and global trends are both logged, but the inspected loop requires enough local event data and explicit user approval. It is harness-local learning, not domain-knowledge learning.

**Timing.** Online trace capture through hooks; offline analysis and patch proposal through manual `/meta-optimize`; user-approved application only.

**Survey placement.** ARIS extends the trace-derived survey with a promptware/skillware variant of harness optimization. Compared with [Meta-Harness](./meta-harness.md), it promotes into workflow instructions rather than executable Python harness classes and uses weaker oracles: frequency/failure statistics plus cross-model review, not benchmark score frontiers. Compared with [Synapptic](./synapptic.md), it learns changes to the harness itself rather than compiling user-profile guards into assistant memory surfaces. It strengthens the survey claim that evaluation is the bottleneck: ARIS can observe enough to propose edits, but correctness still depends on external review and user approval.

## Curiosity Pass

**ARIS is more interesting as integration engineering than as "autonomous research while you sleep."** The overnight-research framing is broad, but the durable mechanism is narrower and more transferable: write workflow state to predictable files, route review through different model families, and harden repeated silent failures into helper/verifier contracts.

**The Research Wiki is a schema and helper, not a full knowledge synthesizer.** `research_wiki.py` handles initialization, arXiv metadata, deduplication, indexes, logs, and query-pack generation. It does not itself extract claims from papers, judge idea quality, or maintain semantic consistency. Those operations remain skill-mediated and model-dependent.

**The audit verifier is the strongest memory artifact because it encodes a learned failure.** ARIS observed that `effort: beast` could silently skip required audits. The fix is not another reminder; it is a verdict state machine plus hash-checking verifier. That is a better example of learning than many of the repo's more ambitious research-loop claims.

**The meta-optimization loop has a healthy brake.** A system that automatically patches its own skills from five invocations would be brittle. ARIS instead produces proposals, demands evidence from logs, routes through cross-model review, backs up before applying, and requires user approval. The brake is the architecture.

**The portability story has some tension.** ARIS markets broad portability across Claude, Codex, Cursor, Trae, and others, but the richest mechanisms are Claude Code hooks, Codex MCP calls, and local MCP bridges. The Markdown substrate travels well; the execution policy and reviewer topology are still harness-specific.

## What to Watch

- Whether `meta-optimize` receives enough real-world event data to propose changes that survive later runs, or whether it mainly produces plausible but low-signal prompt edits.
- Whether Research Wiki edges and claim pages become genuinely maintained, or remain a metadata/index helper around paper pages.
- Whether `verify_paper_audits.sh` and the assurance contract stay aligned with the audit skills as those skills evolve.
- Whether Codex/Cursor/Trae support reaches parity with Claude Code hooks, or remains mostly mirrored skill text plus weaker runtime integration.
- Whether the project can keep 68+ skills coherent without the integration-contract discipline becoming too heavy for contributors.

---

Relevant Notes:

- [skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — foundation: ARIS shows the skill/instruction split at large scale, including distribution and discovery costs
- [instructions are typed callables](../../notes/instructions-are-typed-callables.md) — exemplifies: ARIS skills behave as callable procedures with artifact-shaped inputs and outputs
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: ARIS's stage artifacts are a concrete workshop layer for research runs
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: ARIS's strongest autonomous paths are the ones with external review or verifier scripts
- [Prompt ablation converts human insight into deployable agent framing](../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — adjacent: ARIS converts observed failures into deployable workflow constraints, though mostly by review and helper contracts rather than controlled ablation
- [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — context: ARIS installs skills and managed `CLAUDE.md` guidance into harness-specific always-loaded surfaces
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: ARIS adds a trace-to-skill-patch proposal loop for markdown workflow harnesses
- [Meta-Harness](./meta-harness.md) — compares-with: both optimize harnesses from execution traces, but ARIS targets prompt/skill artifacts while Meta-Harness targets executable harness code under benchmark frontiers
