---
type: kb/types/type-spec.md
name: agent-memory-system-review
description: Review of an external agent memory or context-engineering system; source-tier marks code-grounded vs doc-grounded evidence
schema: ./agent-memory-system-review.schema.yaml
---

# Agent memory system review

A review of an external agent memory, knowledge, or context-engineering system. It captures what the system actually does, not what it claims — stated at the confidence the evidence supports: mark what you can't verify, and never present reported behavior as observed.

These reviews serve two readers. For someone **surveying or choosing** a system, the review is a faithful account of what it is and does. For **Commonplace itself**, it surfaces ideas worth borrowing for our own design. The characterization sections (Core Ideas, Artifact analysis, Write side, Read-back) serve the first reader; `Comparison with Our System` and its nested `### Borrowable Ideas` serve the second.

**Two evidence tiers, one type.** The `source-tier` frontmatter field records which: `code-grounded` (the default this spec assumes — findings rest on inspected source; abandoned-but-readable code counts) or `doc-grounded` (no reachable source; findings rest on paper/README/blog, kept claim-level, filed under `lightweight/`). The instructions below are tier-neutral — the evidence-stance, source-metadata, and citation rules phrase for both — so only the Inputs/Workflow, written for the common code-grounded path, need the distinction.

This spec is also the **worker contract** for the `write-agent-memory-system-review` skill. The parent skill owns source preparation, archiving, index edits, QA, validation, and reporting. The worker owns only code inspection and drafting from the inputs below.

The section specs below distill [designing-agent-memory-systems](../../notes/designing-agent-memory-systems.md) and its requirements inventory into a review-time contract — don't load that note during ordinary review writing.

## Inputs

These Inputs and the Workflow describe the **code-grounded** path (the skill's contract); a `doc-grounded` review skips source preparation (no `source_dir`) and otherwise follows the same tier-neutral section, source-metadata, citation, and evidence-stance rules. The caller provides:

- `source_dir` — local source directory (already prepared; the parent does all cloning/refresh)
- `note_path` — target path under `kb/agent-memory-systems/reviews/`
- `reviewed_revision` and any source identity / citation format — caller-supplied context, used for metadata and citations

If any required input is missing, stop and report which. Verify `source_dir` is readable (e.g. `test -d`) and do not mutate it; if it isn't, stop and report. Never update `last-checked` without actually reading `source_dir`.

## Frontmatter

- `description` — discriminating retrieval filter (50–200 chars, double-quoted)
- `type: ../types/agent-memory-system-review.md`
- `source-tier` — `code-grounded` (findings rest on inspected source; abandoned-but-readable code counts) or `doc-grounded` (no reachable source; findings rest on docs/papers, kept claim-level, filed under `lightweight/`, excluded from the matrix). Required — the **only** authority difference between reviews. Promote a `doc-grounded` review by flipping to `code-grounded` once source is read.
- `status: current` unless clearly stale
- `last-checked: "{today}"`
- `tags` — add `trace-derived` only when trace-learning applies (per the Write side rule below); otherwise omit `tags`. Collection membership comes from location, not a tag.

## Citations

Use the caller-supplied citation format when provided. Otherwise cite the source where the finding is reached — **commit-pinned source files/blobs** for code-grounded reviews (source-relative paths in code spans, not markdown links into the local directory), or **document URLs and `kb/sources/` ingest/snapshot links** for doc-grounded reviews (never local source paths). Review notes must remain readable without access to the source.

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

## Workflow

1. **Read for style.** Read 1–2 current reviews in `kb/agent-memory-systems/reviews/` and `kb/agent-memory-systems/README.md` to match local style and depth.
2. **Read for mechanism.** Ground the review in primary sources — `README.md`, architecture/design docs, `CLAUDE.md`/`AGENTS.md`, package manifests, and the core source files implementing the central claims. Where the implementation clarifies or contradicts the README, report what the code does and note the divergence. Read out the material for **Artifact analysis** (the four fields), Write side, Read-back, retrieval/navigation, any learning/distillation model, any validation/governance model, the integration surface (CLI, MCP, API, editor plugin), and what is genuinely implemented versus only proposed.
3. **Write the review** from the code outward. The schema checks the required review sections; the template below shows their order.

## Opening and source metadata

The opening paragraph states what the system is, what it is for, who built it, and any caller-supplied source identity. Put source identity and reviewed revision before the review section headings, using the caller's labels: a repo + commit for `code-grounded`, or a document + version/date for `doc-grounded`.

## Core Ideas

Write 3–6 mechanisms and design choices, not a feature list; use bold lead phrases for scanning. **Every review states how the system manages context efficiency** — the volume *and* complexity of what it puts in the agent's context (selection budgets, progressive disclosure, navigation, compaction, sub-agent isolation), named even when the answer is "unbounded / loads everything." A memory system is a context-engineering tool; this is its central design question, not an optional angle.

Also frame the ideas by what future action the remembered material can change, and surface where distinctive: how far the memory can be **trusted** (preserved source, metadata, review state, validation) and its **adoption affordances** (fits the native editor/terminal/git environment, avoids metered-API lock-in, degrades to inspectable files and scripts).

## Artifact analysis

Classify the reviewed system's central retained behavior-shaping artifacts using the four-field record. This is the architectural vocabulary applied to the reviewed system — it is what makes reviews comparable across systems, and what the position paper is grounded in. **Required in every review.**

Identify the artifacts that actually shape the agent's later behavior — not every file. Split a bundled object into **operative parts or consumption paths** when it carries several behavior-shaping parts under different forms or authorities (a skill package = prose guidance + symbolic manifest + tests). Classify each by:

- **Storage substrate** — where the retained state persists (files, repo, database, vector/graph store, prompt registry, model-artifact store, service object). Locates access, deletion, versioning, rollback.
- **Representational form** — prose, symbolic, and/or distributed-parametric. Form sets the default inspection method: read prose, test/check symbolic, probe distributed-parametric. When several forms apply, list each component token; do not use a `mixed` token.
- **Lineage** — where it came from (authored, imported, or trace-extracted) and its derivation status (source material vs derived view, index, compiled, assembled, learned); what source change invalidates or regenerates it.
- **Behavioral authority** — consumer, channel, and force: knowledge artifact (evidence / reference / context / advice) vs system-definition artifact (instruction, enforcement, routing, validation, evaluation, ranking, learning).

**Extractable lead tokens.** So the cross-system comparison matrix can be built by parsing rather than hand-classification, open the artifact-analysis findings with backticked controlled-value tokens, written as part of the finding once you have reached it: `**Storage substrate:** \`graph\` — …`, `**Representational form:** \`prose\` \`symbolic\` — …`, `**Lineage:** \`authored\` — …`, and `**Behavioral authority:** \`knowledge\` \`routing\` — …`. Each token line is the lead of its own justifying sentence, so the value and its reasoning cannot drift apart. Vocabularies:

- storage substrate ∈ `files` · `repo` · `sqlite` · `rdbms` · `vector` · `graph` · `kv` · `in-memory` · `prompt-registry` · `model-weights` · `service-object`
- representational form ∈ `prose` · `symbolic` · `parametric` (list all that apply; legacy `mixed` must be decomposed)
- lineage ∈ `authored` · `imported` · `trace-extracted`
- behavioral authority ∈ `knowledge` · `instruction` · `enforcement` · `routing` · `validation` · `ranking` · `learning`

For applicable multi-valued axes where the review truly does not contain enough evidence to classify the value, write the lead token as `not-determinable` with a one-line reason, e.g. `**Read-back signal:** \`not-determinable\` — …`. Do not omit the lead line for an applicable axis; omission means the retrofit is incomplete. Do not mix `not-determinable` with controlled values on the same line.

Note any **promotion path**: whether the system can move a candidate toward a stronger representational form or behavioral authority (prose advice → symbolic validator → enforced gate). That trajectory crosses form, lineage, and authority at once, and is often the most design-relevant question.

Mark effective authority and quality (does the prose carry forward, is the retrieval precise) as *not verified from code* where it cannot be read off the source — the same discipline as Read-back.

For systems that learn from agent traces, the Write side section deepens this with the raw → distilled two-stage treatment; this section still records the system's standing retained surfaces.

## Comparison with Our System

Write concrete alignments, divergences, and tradeoffs vs Commonplace. Close with a `### Borrowable Ideas` subsection: for each idea, state what it would look like in Commonplace and whether it is ready now or needs a concrete use case first.

## Write side

The write side is everything that *changes* the store; the read side (below) only *serves* it. Two axes describe it:

- **Agency** — does the store change by `manual` curation (a human authoring or editing through the write interface) or by `automatic` system operations (rule-driven, scheduled, or trace-learned)? A system can be both. Manual curation is **not a separate mechanism** — it is the authoring channel pointed at existing content, so record it here as agency only: its provenance is the Artifact-analysis Lineage `authored` value, and its quality is an *adoption-affordances* question (editability, diffability, links that survive a rename) handled in Core Ideas. The automatic side is where the system itself does something worth classifying.
- **Operations** — which store-changing operations the system performs beyond trivial create/update/delete. Each token is a distinct design choice:
  - `consolidate` — summarise or compress a group (or an oversized entry) into a more compact, higher-level memory (abstraction; reduces count or size).
  - `dedup` — detect and merge near-duplicate entries (redundancy removal, *not* abstraction).
  - `evolve` — automatically modify an *existing* entry in place — its content, links, or metadata — in light of newly arriving entries (A-MEM-style enrichment), without merging or deleting it.
  - `synthesize` — generate a *new* entry capturing an insight across existing entries (additive and generative; the sources remain). The rare, high-value operation.
  - `invalidate` — supersede or mark an entry stale on contradiction or replacement, retaining history (truth maintenance, e.g. bi-temporal `valid_at`/`invalid_at`).
  - `decay` — remove or down-weight entries by age, recency, or capacity (forgetting / eviction).
  - `promote` — change an entry's tier or salience (promotion-by-recurrence, heat reweighting) without changing its content.

  These are the *automatic* operations the system itself performs; manual maintenance is recorded as agency only (it is authoring on existing content, not a separate operation). Index/embedding rebuilds are access-structure upkeep, not content curation — note them in prose, not here.

Write the agency verdict and the automatic operations as lead tokens:

- `**Write agency:**` `manual` · `automatic` — list all that apply.
- `**Curation operations:**` — the automatic operations from the list above; omit when agency is manual-only.

Every `## Write side` section carries the `**Write agency:**` verdict. Add `**Curation operations:**` and the `### Trace-derived learning` sub-section only when the system has a non-trivial automatic write or curation path (trace-learned or rule-based maintenance). A manual-curation-only system keeps just the agency verdict.

### Trace-derived learning

When automatic writes are fed by agent traces, deepen the write side with the raw → distilled loop. **Add `trace-derived` to `tags`** and include this sub-section only when the code-grounded read finds a qualifying mechanism.

A system qualifies when it derives durable retained artifacts from agent traces. Qualifying **traces:** session logs, transcripts, tool/action traces, event streams, repeated trajectories, rollouts. Qualifying **outputs:** prose (notes, rules, playbooks, lessons), symbolic units (schemas, scripts, tools), or distributed-parametric state (weights, embeddings, adapters, rankers, controllers).

Many systems run a two-stage loop: raw traces accumulate as knowledge artifacts (logs, episode buffers), then a distillation step — automatic or manual — produces system-definition artifacts (rules, validators, route entries, fine-tunes). Document both stages; the distillation step's trigger, oracle, and curation policy is often the most discriminating part. Address:

1. **Trace source** — what raw signal is consumed, with what trigger boundaries. Lead token values: `**Trace source:**` `session-logs` · `tool-traces` · `event-streams` · `trajectories`.
2. **Extraction** — what gets pulled out, and what oracle or judge decides what becomes signal.
3. **Four fields** — record storage substrate, representational form, lineage, and behavioral authority for the raw and distilled stages in **Artifact analysis** rather than repeating them here.
4. **Scope and timing** — per-task / per-project / cross-task, and online / offline / staged in cycles. Lead token values: `**Learning scope:**` `per-task` · `per-project` · `cross-task`; `**Learning timing:**` `online` · `offline` · `staged`; `**Distilled form:**` `prose` · `symbolic` · `parametric`.
5. **Survey placement** — position on the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), and whether the system strengthens, weakens, or splits any survey claim.

## Read-back

The read-back path is how stored memory re-enters a future action — the *serve* side. **Read-back is defined in [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)** — including what does and does not count as it (retained memory that accumulates from use, not shipped baseline documentation), and how it differs from activation. This section is the *operational* classification for a review: how to read a system's read-back path off its code. The Write side section captures how memory is *made and maintained*; this captures how it *acts* — independent axes (a system can have an elaborate write/curation loop and a trivial read-back, or the reverse).

**Every review** states a one-line **direction verdict over memory read-back only**: does retained memory reach the agent's context by **pull** (the agent's own deliberate lookup), **push** (unsolicited arrival — always-load of memory, hook, situation match, or user event), or both? Judge from the agent's perspective: user-initiated retrieval uses pull machinery but is push to the agent. Static baseline documentation does not count (per the definition) — it never lifts a system from `pull` to `both`. The most discriminating finding is whether there is *any* push of memory or the system is **pull-only** — the large, under-tested class.

Write the verdict as a backticked controlled-value lead token, the same extractable convention as the Artifact analysis lead tokens: `**Read-back:** \`pull\` — …` with value ∈ `pull` · `push` · `both`. This line is required in every `## Read-back` section.

When the verdict is `push` or `both`, also write **read-back signal** and **faithfulness tested** lead tokens. Read-back signal is the *set* of targeting/signal kinds the push fires on, since a system can do several at once (always-load coarse recall *and* an identifier match *and* an inferred query). List one backticked token per kind: `**Read-back signal:** \`coarse\` \`identifier\` \`inferred / embedding\` — …` with each token ∈ `coarse` · `identifier` · `inferred / lexical` · `inferred / embedding` · `inferred / judgment` (the same vocabulary as **Targeting and signal** below). Faithfulness tested is a single `yes` or `no` token, or `not-determinable` when the review does not contain enough evidence. The matrix parser one-hots whatever tokens appear into indicator columns; these authored lines take precedence over mining the section prose. Omit for pull-only systems (their push-only axes are recorded as all-absent).

**Push-specific detail:** add the remaining read-back detail only when the verdict is `push` or `both` — the system pushes retained memory. Pull-only systems keep the section short. **Targeting is recorded by the Read-back signal, not a tag:** an `identifier` or `inferred` signal (below) is a *targeted* push; `coarse` always-load is not. There is no separate `push-activation` tag or `push_engineered` flag — an `instance` signal *is* the targeted push.

Two cautions on what code can show:

- **Structural vs quality layer.** Report the observable mechanism per axis; mark precision/recall, context dilution, and effective authority as *not verified from code*.
- **Capability vs deployed behavior.** For end-to-end agents, report what the loop wires. For libraries/SDKs the push wiring often lives in the host harness — report the **API surface** as capability (`search(query)` cannot push; `on_action(context) → memories` affords push) rather than asserting deployed behavior.

When the push-specific part is warranted, address:

1. **Direction edge cases** — the verdict token above is the headline; here record the tricky calls. Note "push riding on the pull interface" when a query *also* injects unsolicited behavior-shaping material; documented related-record expansion on a query is still pull (how much expands is a scope question). In multi-agent setups, an orchestrator's or sub-agent's pull is push for the receiving agent.
2. **Targeting and signal** — the two fields behind the `**Read-back signal:**` token.
   - **Targeting**: `coarse` — fired by an always-present or action-type symbol (always-load of memory, session start, any tool call), delivering *generic* recall; or `instance` — selecting for *this* instance. Always-load is the degenerate corner: name it `coarse`, not a peer trigger.
   - **Signal** (only when `instance`): `identifier` — matches an identifier the instance carries by design (tag, type, path, tool name, id, declared scope); or `inferred` — relevance derived from content, sub-kind `lexical` (keyword/BM25: exact-token but content-keyed, hence sense-blind — fires on a term the context negates), `embedding` (learned similarity), or `judgment` (an LLM relevance call). Classify by *what it keys on*: keyword keys on content words, not an assigned identifier, so it is `inferred / lexical`.
   This is where [symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) bites: a genuine `instance` push needs an `identifier` already emitted, or `inferred` selection.
3. **Injection point — there is one, and it is pre-invocation.** A read serves whatever the store holds at the moment it assembles context, just before a model call; relevance must be resolved *at that read*, because between it and the action's completion no new relevant memory arrives — the only thing produced is the agent's own output. So there is no "post-action read-back": operations that fire after the turn (capturing the output, consolidating, re-indexing, decaying) are write-side **maintenance** (see Write side), not a second read. Record the *trigger/occasion* that assembles the read if it is distinctive (session start, user prompt, pre-compact, tool call), not a pre/post "timing".
4. **Selection, scope, and complexity** — top-k, token budget, task/project/session scoping, and how deep or indirect the loaded material is (complexity, not just volume, drives degradation). Policy is code-grounded; actual context dilution is runtime.
5. **Authority at consumption** — advisory context, system instruction, hard gate, router input, or audit trigger. The same memory can be read back as a soft reminder or a hard gate; this is set on the read path, not at write time. Effective authority needs a faithfulness check.
6. **Faithfulness** — whether the system *itself* tests that fired read-back changes behavior (WITH/WITHOUT ablation, perturbation, post-action audit) rather than assuming context presence equals use. [Synapptic](../reviews/synapptic.md) is the reviewed example.
7. **Other consumers** — note when the same memory is also consumed by the human user, schedulers, reviewers, or governance (the Consumer-surfaces lens). A consumer dimension, not a push/pull value.

## Curiosity Pass

Use the second pass for surprising claims, simpler alternatives, mechanisms that sound more powerful than they are, and boundary cases where the reviewed system's own framing may overstate what the implementation proves.

## What to Watch

Track *specific* pending changes, each tied to a consequence for our design or a tracked decision. Cut generic maturity claims ("they add features / get more robust"); an honestly short section beats filler.

## Relevant Notes

Every review ends with explicit `Relevant Notes:` links into the KB. Link notes that define the vocabulary used in the review, provide a theoretical rationale for a classification, or should receive evidence from this system.

## Constraints

- Don't put the source directory under `kb/agent-memory-systems/reviews/`.
- Don't present `doc-grounded` reported behavior as observed; don't invent four-field or read-back detail the sources don't support.
- Don't write markdown links from a review into local source paths (`../../../related-systems/...`).
- Don't treat proposed docs as implemented behavior without checking the code.
- Don't update `last-checked` without actually re-reading the system.

## Template

```markdown
---
description: Template for related-system reviews — external system comparisons with fixed sections, borrowable ideas, and review freshness metadata
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
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

{Four-field record for the central retained artifacts, at the operative-part level. See Artifact analysis. Lead each field with extractable controlled-value tokens:}

- **Storage substrate:** `{files|repo|sqlite|rdbms|vector|graph|kv|in-memory|prompt-registry|model-weights|service-object}` — {justification}
- **Representational form:** `{prose|symbolic|parametric}` `{...}` — {justification; list all that apply}
- **Lineage:** `{authored|imported|trace-extracted}` `{...}` — {derivation status}
- **Behavioral authority:** `{knowledge|instruction|enforcement|routing|validation|ranking|learning}` `{...}` — {consumer, channel, force}

## Comparison with Our System

{Alignments, divergences, tradeoffs vs Commonplace.}

### Borrowable Ideas

{For each idea: what it would look like in Commonplace; ready now or needs a use case first.}

## Write side

**Write agency:** `{manual|automatic}` `{...}` — {how the store changes; manual = curation via the authoring channel, see Lineage + affordances}

{Required heading + `**Write agency:**` verdict. Add `**Curation operations:** \`consolidate\` …` and the `### Trace-derived learning` sub-section only with a non-trivial automatic write/curation path; a manual-only system keeps just the heading and agency verdict. See Write side.}

### Trace-derived learning

{Optional sub-section — qualifying trace-learning only; delete otherwise, and add `trace-derived` to `tags` when kept. Deepens Artifact analysis with the raw → distilled loop. Lead tokens: `**Trace source:**`, `**Learning scope:**`, `**Learning timing:**`, `**Distilled form:**`.}

## Read-back

**Read-back:** `{pull|push|both}` — {one-line justification; required regardless}

{Add the remaining read-back detail only when read-back is `push`/`both`; delete this optional part for pull-only. Targeting is the Read-back signal (`coarse` vs `instance`), no tag. There is no read-back "timing" — read-back is pre-invocation; after-the-turn work is Write-side maintenance. See Read-back.}

## Curiosity Pass

- {Surprises or curiosities}
- {Simpler alternatives worth checking}
- {What the mechanism could actually achieve, even if it works perfectly}

## What to Watch

- {A *specific* pending change + its consequence for our design or a tracked decision.}
- {Cut generic "they get more robust" filler — an honestly-short section beats it.}

Relevant Notes:

- [{relevant note}](../../notes/{note}.md) - {relationship}
```
