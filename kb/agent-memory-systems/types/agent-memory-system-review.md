---
type: kb/types/type-spec.md
name: agent-memory-system-review
description: Code-grounded review of an external agent memory or context-engineering system
schema: ./agent-memory-system-review.schema.yaml
---

# Agent memory system review

## Authoring Instructions

Use this type for a **code-grounded** review of an external agent memory, knowledge, or context-engineering system, comparing it against commonplace.

**A local source directory with readable code is required.** This type captures what the reviewed system actually does, not what it claims. If the system is only documented via a paper, README, or blog post without accessible source code, use a lightweight note instead. Abandoned code is acceptable if the directory is still readable.

This type spec is also the worker contract for delegated drafting from the local `write-agent-memory-system-review` skill. The parent skill owns source preparation, archive moves, index edits, semantic QA, validation, and reporting; the worker owns only code inspection and review-note drafting from the inputs below.

## Comparison Lens

Use this embedded lens when comparing the reviewed system with commonplace. Do not load a separate memory-system design note during ordinary review writing; this distillation is the review-time contract. It is a comparison aid, not a required section template. Mention only the axes where the reviewed system has a distinctive mechanism, absence, or tradeoff.

Agent memory is a context-engineering problem: it improves future agent action by making prior work discoverable, composable, trustworthy, activatable, and maintainable under bounded context. The important question is not "does the system store memories?" but "what future answer, action, artifact, or rule can change because of the remembered material?"

Check the reviewed system against these needs selectively:

- **Creation and import:** Can useful memory be authored directly, imported from existing artifacts, or extracted from traces without losing provenance or structure?
- **Evidence and trust:** Does the system preserve enough source material, metadata, review state, validation, or confidence information for a future agent to rely on the memory without redoing the original work?
- **Artifact contracts:** Does it distinguish retained surfaces by storage substrate, representational form, lineage, and behavioral authority, including knowledge-artifact and system-definition-artifact use?
- **Consumer surfaces:** Does it serve different consumers differently: acting agents, humans, context schedulers, reviewers, learning loops, governance, and active work surfaces?
- **Activation:** Can relevant behavior-changing memory load before the agent repeats a mistake, or is the system limited to question-answer retrieval?
- **Promotion and codification:** Is there a path from candidate observations toward notes, instructions, skills, tests, scripts, guardrails, or other stronger behavior-changing surfaces when evidence and authority justify the cost?
- **Compiled views and lifecycle:** Are generated reminders, indexes, rules, assistant files, and other derived surfaces tied back to sources of truth, with retirement, redaction, supersession, regeneration, and relaxation paths?
- **Authority and evaluation:** Who or what can write, promote, activate, enforce, revise, and retire memory, and does the system evaluate memory by downstream effects rather than by storage volume?
- **Adoption affordances:** Does the system fit the agent's native work environment, reuse existing editor/terminal/git workflows, avoid unnecessary metered API surfaces, or degrade gracefully into inspectable files and scripts?

## Required Inputs

Before writing, you must have:

- `source_dir` — local directory containing the source code to inspect
- `note_path` — target review path under `kb/agent-memory-systems/reviews/`

The caller may also provide source identity or a citation format. Treat that as caller-supplied context, not as part of this type's required contract.

If any required input is missing, stop and report exactly which one is missing. Do not infer source state from a different directory.

## Establish Source State

Before reading or writing, establish the source state from `source_dir`.

Verify the directory exists and is readable:

```bash
test -d "{source_dir}"
```

If the command fails, stop and report that the source directory could not be established.

If `source_dir` is a git repository, derive `reviewed_revision`:

```bash
git -C "{source_dir}" rev-parse HEAD
```

If the command fails because the directory is not a git repository, continue without a revision but say so in the final report. Do not refresh, fetch, pull, or otherwise mutate `source_dir`; source preparation belongs to the caller.

Use `reviewed_revision` and any caller-supplied source metadata for review metadata and citations. Do not update `last-checked` without actually reading `source_dir`.

## Read for Style

Read 1-2 existing reviews in `kb/agent-memory-systems/reviews/` to match local style and comparison depth. Also read `kb/agent-memory-systems/README.md`.

## Read for Mechanism

Ground the review in primary source files:

- `README.md`
- architecture/design docs
- `CLAUDE.md` / `AGENTS.md` if present
- package manifests and build metadata
- core source files implementing the system's central claims

Do not rely only on the README if the implementation clarifies or contradicts it.

Focus on:

- storage model
- representational form of the behavior-shaping operative parts
- lineage, derivation, invalidation, and regeneration paths
- retrieval/navigation model
- learning/distillation/promotion model if any
- validation/governance model if any
- behavioral authority: whether retained artifacts advise, instruct, enforce, route, validate, evaluate, rank, or feed learning
- integration surface (CLI, MCP, API, editor plugin, etc.)
- what is genuinely implemented versus only proposed
- whether the system qualifies as trace-derived learning; if it does not, leave the placement section out and do not add the `trace-derived` tag

## Write the Review

Write from the code outward:

- **Opening paragraph:** what the system is, what it is for, who built it. Include caller-supplied source identity when available.
- **Source metadata:** before the section headings, include source identity and reviewed revision when available. Use labels that match the source metadata the caller provided.
- **Core Ideas:** 3-6 mechanisms and design choices, not feature lists. Use bolded lead phrases for scanning.
- **Comparison with Our System:** concrete alignments, divergences, and tradeoffs vs commonplace.
- **Borrowable Ideas:** for each idea, say what it would look like in commonplace and whether it is ready now or needs a use case first.
- **Trace-derived learning placement:** include this section only when the code-grounded review finds a qualifying trace-derived learning mechanism; if included, also add `trace-derived` to `tags`.
- **Curiosity Pass:** second-pass review. Re-read the draft and look for surprising claims, simpler alternatives, and mechanisms that sound more powerful than they really are.
- **What to Watch:** future changes in the reviewed system that might affect our design.

Every review should end with explicit `Relevant Notes:` links into the KB.

## Frontmatter

Use:

- `description` — discriminating retrieval filter (50-200 chars, double-quoted)
- `type: ../types/agent-memory-system-review.md`
- `tags: [trace-derived]` — add `trace-derived` only if the code-grounded review finds that the system learns from agent traces; the finding drives both the tag and the placement section. Otherwise omit `tags`. Collection membership is defined by location in `kb/agent-memory-systems/`, not by a tag.
- `status: current` unless clearly stale/outdated
- `last-checked: "{today}"`

## Trace-Derived Learning Placement

Decide whether the reviewed system learns from traces during the mechanism read. Qualifying source traces: agent/assistant session logs, conversation transcripts, tool/action traces, event streams, repeated task trajectories, rollouts. Qualifying outputs are durable retained artifacts derived from those traces: natural-language notes/rules/playbooks/lessons/memories (prose representational form), formal-semantic units like schemas/scripts/tools (symbolic representational form), or learned numerical state such as weights, embeddings, adapters, rankers, or controllers (distributed-parametric representational form).

Many systems have a two-stage loop: raw traces accumulate as source evidence or knowledge artifacts (session logs, episode buffers), then a distillation step — automatic or manual — produces system-definition artifacts (rules, playbooks, validators, route entries, fine-tunes). When this pattern is present, document both stages using the artifact-analysis fields: storage substrate, representational form, lineage, and behavioral authority at "raw" and at "distilled". The trigger, oracle, and curation policy of the distillation step is often the most discriminating part of the system.

If the system qualifies, include a `## Trace-derived learning placement` section and add `trace-derived` to the frontmatter `tags`. The section should address:

1. **Trace source** — what raw signal is consumed, and with what trigger boundaries.
2. **Extraction** — what gets pulled out, and what oracle or judge decides what becomes signal.
3. **Storage substrate** — where the raw and distilled retained state lives: files, database, vector store, graph store, prompt registry, model-artifact store, service object, etc.
4. **Representational form** — prose, symbolic, distributed-parametric, or mixed; classify operative parts separately when one stored object bundles several forms.
5. **Lineage** — source traces, derivation chain, regeneration/invalidation rule, and whether the distilled artifact is canonical source or derived view.
6. **Behavioral authority** — knowledge artifact when consumed as evidence, reference, context, explanation, or advice; system-definition artifact when consumed with instruction, enforcement, routing, validation, configuration, evaluation, ranking, or learning force.
7. **Scope** — per-task, per-benchmark, per-project, or cross-task generalizable.
8. **Timing** — online during deployment, offline from collected traces, or staged in cycles.
9. **Survey placement** — position the system on the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), and state whether it strengthens, weakens, or splits any survey claim.

## Citations

Use the caller-supplied citation format when one is provided.

If no citation format is provided, cite source files in prose with source-relative paths in code spans, not as markdown links into the local directory. Local source paths are fine for inspection notes or final reports, but review notes must remain readable without access to the local directory.

## Constraints

**Always:**

- write the review into `kb/agent-memory-systems/reviews/`
- ground claims in source code/docs, not just project marketing
- cite source evidence using the caller-supplied citation format when available, otherwise use readable source-relative path references in prose
- treat trace-derived status as a code-grounded review finding

**Never:**

- put the source directory under `kb/agent-memory-systems/reviews/`
- write Markdown links from review notes into `../../../related-systems/...` or other local source paths
- treat proposed docs as implemented behavior without checking the code
- update `last-checked` without actually re-reading the system

## Template

```markdown
---
description: Template for related-system reviews — external system comparisons with fixed sections, borrowable ideas, and review freshness metadata
type: ../types/agent-memory-system-review.md
status: current
last-checked: "YYYY-MM-DD"
---

# {System name}

{One-paragraph summary}

**Source:** {source identity, if available}

**Reviewed revision:** {revision, if available}

## Core Ideas

{Core ideas}

## Comparison with Our System

{Comparison}

## Borrowable Ideas

{Borrowable ideas}

## Trace-derived learning placement

{Optional. Include only when the code-grounded review finds a qualifying trace-derived learning mechanism; otherwise delete this section. When included, also add `trace-derived` to `tags`. Cover trace source, extraction, storage substrate, representational form, lineage, behavioral authority, scope, timing, survey-axis placement, and whether the system strengthens, weakens, or splits any survey claim.}

## Curiosity Pass

- {Surprises or curiosities}
- {Simpler alternatives worth checking}
- {What the mechanism could actually achieve, even if it works perfectly}

## What to Watch

- {What might change that affects our design?}
- {What experiments are worth tracking?}
```
