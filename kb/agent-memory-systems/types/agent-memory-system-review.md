---
type: kb/types/type-spec.md
name: agent-memory-system-review
description: Code-grounded review of an external agent memory or context-engineering system
schema: ./agent-memory-system-review.schema.yaml
---

# Agent memory system review

A **code-grounded** review of an external agent memory, knowledge, or context-engineering system. It captures what the system actually does, not what it claims.

These reviews serve two readers. For someone **surveying or choosing** a system, the review is a faithful, code-grounded account of what it is and does. For **Commonplace itself**, it surfaces ideas worth borrowing for our own design. The characterization sections (Core Ideas, Artifact analysis, the placement sections) serve the first reader; `Comparison with Our System` and its nested `### Borrowable Ideas` serve the second.

**Requires readable local source.** A system documented only by paper, README, or blog — with no accessible code — gets a lightweight note instead, not this type. Abandoned-but-readable code is fine.

This spec is also the **worker contract** for the `write-agent-memory-system-review` skill. The parent skill owns source preparation, archiving, index edits, QA, validation, and reporting. The worker owns only code inspection and drafting from the inputs below.

The section specs below distill [designing-agent-memory-systems](../../notes/designing-agent-memory-systems.md) and its requirements inventory into a review-time contract — don't load that note during ordinary review writing.

## Inputs

The caller provides:

- `source_dir` — local source directory (already prepared; the parent does all cloning/refresh)
- `note_path` — target path under `kb/agent-memory-systems/reviews/`
- `reviewed_revision` and any source identity / citation format — caller-supplied context, used for metadata and citations

If any required input is missing, stop and report which. Verify `source_dir` is readable (e.g. `test -d`) and do not mutate it; if it isn't, stop and report. Never update `last-checked` without actually reading `source_dir`.

## Workflow

1. **Read for style.** Read 1–2 current reviews in `kb/agent-memory-systems/reviews/` and `kb/agent-memory-systems/README.md` to match local style and depth.
2. **Read for mechanism.** Ground the review in primary sources — `README.md`, architecture/design docs, `CLAUDE.md`/`AGENTS.md`, package manifests, and the core source files implementing the central claims. Where the implementation clarifies or contradicts the README, report what the code does and note the divergence. Read out the material for **Artifact analysis** (the four fields) and the placement sections, plus the retrieval/navigation and read-back model, any learning/distillation model, any validation/governance model, the integration surface (CLI, MCP, API, editor plugin), and what is genuinely implemented versus only proposed.
3. **Write the review**, from the code outward — see Sections.

## Sections

Write from the code outward. Required sections are enforced by the schema; the two placement sections are optional and governed by their own trigger rules below.

- **Opening paragraph** — what the system is, what it is for, who built it. Include caller-supplied source identity.
- **Source metadata** — source identity and reviewed revision, before the section headings, using the caller's labels.
- **Core Ideas** — 3–6 mechanisms and design choices, not a feature list; bold lead phrases for scanning. **Every review states how the system manages context efficiency** — the volume *and* complexity of what it puts in the agent's context (selection budgets, progressive disclosure, navigation, compaction, sub-agent isolation), named even when the answer is "unbounded / loads everything." A memory system is a context-engineering tool; this is its central design question, not an optional angle. Also frame the ideas by what future action the remembered material can change, and surface where distinctive: how far the memory can be **trusted** (preserved source, metadata, review state, validation) and its **adoption affordances** (fits the native editor/terminal/git environment, avoids metered-API lock-in, degrades to inspectable files and scripts).
- **Artifact analysis** — the four-field record for the central retained artifacts. Required; see Artifact analysis.
- **Comparison with Our System** — concrete alignments, divergences, and tradeoffs vs Commonplace. Close with a `### Borrowable Ideas` subsection: for each idea, what it would look like in Commonplace, and whether it is ready now or needs a use case first.
- **Trace-derived learning placement** — *optional; see rule below.*
- **Read-back placement** — *optional; see rule below.* Every review states a one-line direction verdict somewhere even without the full section.
- **Curiosity Pass** — second pass: surprising claims, simpler alternatives, mechanisms that sound more powerful than they are.
- **What to Watch** — *specific* pending changes, each tied to a consequence for our design or a tracked decision. Cut generic maturity ("they add features / get more robust"); an honestly-short section beats filler.

Every review ends with explicit `Relevant Notes:` links into the KB.

## Artifact analysis

Classify the reviewed system's central retained behavior-shaping artifacts using the four-field record. This is the architectural vocabulary applied to the reviewed system — it is what makes reviews comparable across systems, and what the position paper is grounded in. **Required in every review.**

Identify the artifacts that actually shape the agent's later behavior — not every file. Split a bundled object into **operative parts or consumption paths** when it carries several behavior-shaping parts under different forms or authorities (a skill package = prose guidance + symbolic manifest + tests). Classify each by:

- **Storage substrate** — where the retained state persists (files, repo, database, vector/graph store, prompt registry, model-artifact store, service object). Locates access, deletion, versioning, rollback.
- **Representational form** — prose, symbolic, or distributed-parametric (or mixed). Form sets the default inspection method: read prose, test/check symbolic, probe distributed-parametric.
- **Lineage** — where it came from (authored, imported, or trace-extracted) and its derivation status (source material vs derived view, index, compiled, assembled, learned); what source change invalidates or regenerates it.
- **Behavioral authority** — consumer, channel, and force: knowledge artifact (evidence / reference / context / advice) vs system-definition artifact (instruction, enforcement, routing, validation, evaluation, ranking, learning).

**Extractable lead tokens.** So the cross-system comparison matrix can be built by parsing rather than hand-classification, open the storage-substrate and representational-form findings with a backticked controlled-value token, written as part of the finding once you have reached it: `**Storage substrate:** \`graph\` — …` and `**Representational form:** \`prose\` — …`. The token is the lead of its own justifying sentence, so the value and its reasoning cannot drift apart. Vocabularies:

- storage substrate ∈ `files` · `repo` · `sqlite` · `rdbms` · `vector` · `graph` · `kv` · `in-memory` · `prompt-registry` · `model-weights` · `service-object`
- representational form ∈ `prose` · `symbolic` · `parametric` · `mixed` (use `mixed` only when no single form dominates the central artifact; the prose then says which part is which)

Note any **promotion path**: whether the system can move a candidate toward a stronger representational form or behavioral authority (prose advice → symbolic validator → enforced gate). That trajectory crosses form, lineage, and authority at once, and is often the most design-relevant question.

Mark effective authority and quality (does the prose carry forward, is the retrieval precise) as *not verified from code* where it cannot be read off the source — the same discipline as Read-back placement.

For systems that learn from agent traces, the Trace-derived learning placement section deepens this with the raw → distilled two-stage treatment; this section still records the system's standing retained surfaces.

## Trace-derived learning placement

This section is the trace-learning deepening of **Artifact analysis**: where that section classifies the system's standing retained surfaces, this one classifies the raw → distilled loop that produces them.

**Trigger:** include the `## Trace-derived learning placement` section **and** add `trace-derived` to `tags` only when the code-grounded read finds a qualifying mechanism. Otherwise omit both.

A system qualifies when it derives durable retained artifacts from agent traces. Qualifying **traces:** session logs, transcripts, tool/action traces, event streams, repeated trajectories, rollouts. Qualifying **outputs:** prose (notes, rules, playbooks, lessons), symbolic units (schemas, scripts, tools), or distributed-parametric state (weights, embeddings, adapters, rankers, controllers).

Many systems run a two-stage loop: raw traces accumulate as knowledge artifacts (logs, episode buffers), then a distillation step — automatic or manual — produces system-definition artifacts (rules, validators, route entries, fine-tunes). Document both stages; the distillation step's trigger, oracle, and curation policy is often the most discriminating part. Address:

1. **Trace source** — what raw signal is consumed, with what trigger boundaries.
2. **Extraction** — what gets pulled out, and what oracle or judge decides what becomes signal.
3. **Four fields** — record storage substrate, representational form, lineage, and behavioral authority for the raw and distilled stages in **Artifact analysis** rather than repeating them here.
4. **Scope and timing** — per-task / per-benchmark / per-project / cross-task, and online / offline / staged in cycles.
5. **Survey placement** — position on the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), and whether the system strengthens, weakens, or splits any survey claim.

## Read-back placement

The read-back path is how stored memory re-enters a future action. The trace-derived section captures how memory is *made*; this captures how it *acts* — independent axes (a system can have an elaborate learning loop and a trivial read-back, or the reverse).

**Every review** states a one-line **direction verdict**: does memory reach the agent's context by **pull** (the agent's own deliberate lookup), **push** (unsolicited arrival — always-load, hook, situation match, or user event), or both? Judge from the agent's perspective: user-initiated retrieval uses pull machinery but is push to the agent. The most discriminating finding is whether there is *any* push path or the system is **pull-only** — the large, under-tested class. Name always-load as a deliberate push choice, not the absence of one.

Write the verdict as a backticked controlled-value lead token, the same extractable convention as the Artifact analysis lead tokens: `**Read-back:** \`pull\` — …` with value ∈ `pull` · `push` · `both`. This line is required even when the full section below is omitted.

**Trigger:** include the full `## Read-back placement` section **and** add `push-activation` to `tags` only when the activation path is relevance-gated or otherwise engineered — a matcher (embedding, action-classifier, LLM-judge, typed cue), a selection/scope budget, a before-action hook, or a faithfulness test. Pure pull-only RAG and unconditional always-load get only the verdict, no section, no tag.

Two cautions on what code can show:

- **Structural vs quality layer.** Report the observable mechanism per axis; mark precision/recall, context dilution, and effective authority as *not verified from code*.
- **Capability vs deployed behavior.** For end-to-end agents, report what the loop wires. For libraries/SDKs the push wiring often lives in the host harness — report the **API surface** as capability (`search(query)` cannot push; `on_action(context) → memories` affords push) rather than asserting deployed behavior.

When a full section is warranted, address:

1. **Direction** — pull, push, or both, from the agent's perspective. Note "push riding on the pull interface" when a query *also* injects unsolicited behavior-shaping material; documented related-record expansion on a query is still pull (how much expands is a scope question). In multi-agent setups, an orchestrator's or sub-agent's pull is push for the receiving agent.
2. **Trigger and relevance signal** — what trips the read-back and how it matches: unconditional, event-keyed, embedding, action-classifier, LLM-judge, typed cue. Mechanism is code-grounded; precision/recall is runtime.
3. **Timing relative to action** — a pre-action hook fires before the action and can change the next move; a reflection or summary step fires after and can only explain or audit.
4. **Selection, scope, and complexity** — top-k, token budget, task/project/session scoping, and how deep or indirect the loaded material is (complexity, not just volume, drives degradation). Policy is code-grounded; actual context dilution is runtime.
5. **Authority at consumption** — advisory context, system instruction, hard gate, router input, or audit trigger. The same memory can be read back as a soft reminder or a hard gate; this is set on the read path, not at write time. Effective authority needs a faithfulness check.
6. **Faithfulness** — whether the system *itself* tests that fired read-back changes behavior (WITH/WITHOUT ablation, perturbation, post-action audit) rather than assuming context presence equals use. [Synapptic](../reviews/synapptic.md) is the reviewed example.
7. **Other consumers** — note when the same memory is also consumed by the human user, schedulers, reviewers, or governance (the Consumer-surfaces lens). A consumer dimension, not a push/pull value.

## Frontmatter

- `description` — discriminating retrieval filter (50–200 chars, double-quoted)
- `type: ../types/agent-memory-system-review.md`
- `status: current` unless clearly stale
- `last-checked: "{today}"`
- `tags` — add `trace-derived` and/or `push-activation` only per the placement rules above. A review may carry neither, either, or both; otherwise omit `tags`. Collection membership comes from location, not a tag.

## Citations

Use the caller-supplied citation format when provided. Otherwise cite source files in prose with **source-relative paths in code spans** — not markdown links into the local directory. Review notes must remain readable without access to the local source.

### Quote-anchored citations

For a **load-bearing claim** — one a reader could reasonably dispute, or that the system's own docs contradict — anchor it to the exact source text instead of a bare file reference. Write the supporting passage as a blockquote whose final line is a `---` attribution naming the source location pinned to the reviewed revision:

```markdown
> the verbatim line(s) the claim rests on, copied exactly from the source
> --- `src/memory/store.py` @ `abc123`
```

For GitHub-backed sources the attribution may instead be a commit-pinned blob URL, consistent with the caller's citation format:

```markdown
> the verbatim line(s) the claim rests on, copied exactly from the source
> --- [src/memory/store.py](https://github.com/org/repo/blob/abc123/src/memory/store.py)
```

The quoted text is the anchor; the attribution pins where it came from. Do not record byte offsets, character spans, or ids — the quote is self-relocating (it can be re-found by search) and the pinned commit is immutable, so nothing else is needed to verify it.

This is **optional and additive** — use it on the claims that carry the review, not on every sentence. It strengthens the "readable without the source" goal above: the evidence now travels inline rather than hiding behind a file path. Resolution (does the quote actually appear in the pinned source?) is a write-time check run against the live checkout — see [verify-review-quote-grounding](../../instructions/verify-review-quote-grounding.md) — not something a later reader or the standing validator can redo, because the source is not retained in the KB. The validator checks only that each quote-anchored citation is well-formed and names a source.

## Constraints

- Don't put the source directory under `kb/agent-memory-systems/reviews/`.
- Don't write markdown links from a review into local source paths (`../../../related-systems/...`).
- Don't treat proposed docs as implemented behavior without checking the code.
- Don't update `last-checked` without actually re-reading the system.

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

## Artifact analysis

{Four-field record for the central retained artifacts, at the operative-part level. See Artifact analysis. Lead the first two with extractable controlled-value tokens:}

- **Storage substrate:** `{files|repo|sqlite|rdbms|vector|graph|kv|in-memory|prompt-registry|model-weights|service-object}` — {justification}
- **Representational form:** `{prose|symbolic|parametric|mixed}` — {justification}
- **Lineage** — {authored/imported/trace-extracted + derivation status}
- **Behavioral authority** — {knowledge-artifact vs system-definition; consumer, channel, force}

## Comparison with Our System

{Alignments, divergences, tradeoffs vs Commonplace.}

### Borrowable Ideas

{For each idea: what it would look like in Commonplace; ready now or needs a use case first.}

## Trace-derived learning placement

{Optional — qualifying trace-learning only; delete otherwise, and add `trace-derived` to `tags` when kept. Deepens Artifact analysis with the raw → distilled loop. See Trace-derived learning placement.}

## Read-back placement

**Read-back:** `{pull|push|both}` — {one-line justification; required regardless}

{Full section only when relevance-gated/engineered; delete the rest otherwise, and add `push-activation` to `tags` when kept. See Read-back placement.}

## Curiosity Pass

- {Surprises or curiosities}
- {Simpler alternatives worth checking}
- {What the mechanism could actually achieve, even if it works perfectly}

## What to Watch

- {A *specific* pending change + its consequence for our design or a tracked decision.}
- {Cut generic "they get more robust" filler — an honestly-short section beats it.}
```
