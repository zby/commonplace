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
- **Read-back (activation):** How does stored memory re-enter a future agent action — by **pull** (the agent's own deliberate lookup) or **push** (unsolicited arrival: always-load, hook, situation match, or a user event), judged from the agent's perspective? Can relevant behavior-changing memory load before the agent repeats a mistake, or is the system pull-only (limited to question-answer retrieval the agent must think to call)? See the Read-back Placement section for the full axis treatment.
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
- read-back model: how stored memory re-enters a future agent action — direction (pull vs push, from the agent's perspective), what trips it, timing relative to the action, scope, and authority at consumption
- learning/distillation/promotion model if any
- validation/governance model if any
- behavioral authority: whether retained artifacts advise, instruct, enforce, route, validate, evaluate, rank, or feed learning
- integration surface (CLI, MCP, API, editor plugin, etc.)
- what is genuinely implemented versus only proposed
- whether the system qualifies as trace-derived learning; if it does not, leave the placement section out and do not add the `trace-derived` tag
- whether the system has a non-trivial push/activation path; if it is pull-only or unconditional always-load, give a one-line direction verdict and add neither a full Read-back placement section nor the `push-activation` tag

## Write the Review

Write from the code outward:

- **Opening paragraph:** what the system is, what it is for, who built it. Include caller-supplied source identity when available.
- **Source metadata:** before the section headings, include source identity and reviewed revision when available. Use labels that match the source metadata the caller provided.
- **Core Ideas:** 3-6 mechanisms and design choices, not feature lists. Use bolded lead phrases for scanning.
- **Comparison with Our System:** concrete alignments, divergences, and tradeoffs vs commonplace.
- **Borrowable Ideas:** for each idea, say what it would look like in commonplace and whether it is ready now or needs a use case first.
- **Trace-derived learning placement:** include this section only when the code-grounded review finds a qualifying trace-derived learning mechanism; if included, also add `trace-derived` to `tags`.
- **Read-back placement:** give every review a one-line direction verdict (pull / push / both, from the agent's perspective). Include the full section only when the activation path is relevance-gated or otherwise engineered; if included, also add `push-activation` to `tags`.
- **Curiosity Pass:** second-pass review. Re-read the draft and look for surprising claims, simpler alternatives, and mechanisms that sound more powerful than they really are.
- **What to Watch:** future changes in the reviewed system that might affect our design.

Every review should end with explicit `Relevant Notes:` links into the KB.

## Frontmatter

Use:

- `description` — discriminating retrieval filter (50-200 chars, double-quoted)
- `type: ../types/agent-memory-system-review.md`
- `tags` — add `trace-derived` only if the code-grounded review finds that the system learns from agent traces, and `push-activation` only if it finds a non-trivial push/activation path (relevance-gated or engineered read-back, not pull-only or unconditional always-load). Each finding drives both its tag and its placement section. A review may carry neither, either, or both. Otherwise omit `tags`. Collection membership is defined by location in `kb/agent-memory-systems/`, not by a tag.
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

## Read-back Placement

The read-back path is how stored memory re-enters a future agent action. The trace-derived section captures how memory is *made*; this section captures how it *acts*, and the two are independent — a system can have an elaborate learning loop and a trivial read-back path, or the reverse. Specify it as deliberately as the learning loop rather than collapsing it into "can the system retrieve?".

Every memory system reads memory back somehow, so unlike trace-derived learning this is near-universal. Give **every** review a one-line **direction verdict**: does memory reach the agent's context by **pull** (the agent's own deliberate lookup — a query/search tool call, a chosen read), by **push** (memory arrives unsolicited — always-load, a hook on an agent action, a situation/relevance match, or any user-initiated event), or both? Push/pull is judged **from the agent's perspective**: user-initiated retrieval uses pull machinery but is push to the agent, because the agent did not ask. The single most discriminating finding is whether the system has any push path at all or is **pull-only** (a retrieval tool the agent must think to call) — pull-only is the large, under-tested class.

Include a full `## Read-back placement` section and add `push-activation` to `tags` **only when the activation path is relevance-gated or otherwise engineered**: a matcher (embedding, action-classifier, LLM-judge, or typed cue), a selection/scope budget, a before-action hook, or a faithfulness test. Pure pull-only RAG and unconditional always-load get only the one-line direction verdict (name always-load as a deliberate push choice, not the absence of one) and no tag.

Two cautions on what code can show:

- **Structural vs quality layer.** Report the observable *mechanism* per axis and explicitly mark precision/recall, context dilution, and effective authority as *not verified from code* — the same discipline the trace-derived section lives under (you can see the extraction mechanism, not whether the lessons are good).
- **Capability vs deployed behavior.** For end-to-end agents, report what the loop actually wires. For libraries/SDKs the push wiring often lives in the host harness, not the reviewed repo: report the **API surface** as capability (`search(query)` cannot push; `on_action(context) → memories` affords push) rather than asserting the system pushes or has no activation.

If a full section is warranted, address:

1. **Direction** — pull, push, or both, from the agent's perspective. Pull = the agent's own deliberate lookup; push = unsolicited arrival, whatever the trigger. Note "push riding on the pull interface" when a query *also* injects unsolicited behavior-shaping material; documented related-record expansion on a query is still pull (the agent solicited the query contract), and how much expands is a scope question. In multi-agent setups, an orchestrator's or sub-agent's pull is push for the receiving agent.
2. **Trigger and relevance signal** — what trips the read-back and how it matches: unconditional, event-keyed, embedding, action-classifier, LLM-judge, or typed cue. Mechanism is code-grounded; precision/recall is runtime.
3. **Timing relative to action** — where in the loop the read sits. A pre-action hook fires before the action and can change the next move; a reflection or summary step fires after and can only explain or audit.
4. **Selection and scope** — top-k, token budget, and task/project/session scoping. The policy is code-grounded; actual context dilution (soft degradation) is runtime.
5. **Authority at consumption** — how the surfaced memory is wired: advisory context, system instruction, hard gate (enforcement), router input, or audit trigger. The same stored memory can be read back as a soft reminder or a hard gate; this is set on the read path, not at write time. Nominal authority is code-grounded; effective authority needs a faithfulness check.
6. **Faithfulness** — whether the system *itself* tests that fired read-back changes behavior (WITH/WITHOUT ablation, perturbation, post-action trace audit) rather than assuming context presence equals use. [Synapptic](../reviews/synapptic.md) is the reviewed example.
7. **Other consumers** — the axes above describe read-back to the agent, the primary consumer. Note when the same memory is also consumed directly by the human user, or by schedulers, reviewers, or governance (the Consumer-surfaces lens). This is a consumer dimension, not a push/pull value.

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

## Read-back placement

{State the one-line direction verdict (pull / push / both, from the agent's perspective) somewhere in the review even without this section. Include this full section only when the activation path is relevance-gated or engineered; otherwise delete it. When included, also add `push-activation` to `tags`. Cover direction, trigger/relevance signal, timing relative to action, selection/scope, authority at consumption, faithfulness, and other consumers. Mark precision/dilution/effective-authority as not verified from code, and report library API surface as capability rather than deployed behavior.}

## Curiosity Pass

- {Surprises or curiosities}
- {Simpler alternatives worth checking}
- {What the mechanism could actually achieve, even if it works perfectly}

## What to Watch

- {What might change that affects our design?}
- {What experiments are worth tracking?}
```
