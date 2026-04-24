---
type: kb/types/type-spec.md
name: agent-memory-system-review
description: Code-grounded review of an external agent memory or context-engineering system
schema: ./agent-memory-system-review.schema.yaml
---

# Agent memory system review

## Authoring Instructions

Use this type for a **code-grounded** review of an external agent memory, knowledge, or context-engineering system, comparing it against commonplace.

**A reachable GitHub repository is required.** This type captures what the reviewed system actually does, not what it claims. If the system is only documented via a paper, README, or blog post without accessible source code, use a source-only note instead. Abandoned repos are acceptable if the code is still readable.

## Required Inputs

Before writing, you must have:

- `repo_url` — canonical full GitHub repository URL for citations, `https://github.com/{owner}/{repo}` with no trailing slash or `.git`
- `checkout_dir` — local checkout under `related-systems/`
- `note_path` — target review path under `kb/agent-memory-systems/reviews/`

If any required input is missing, stop and report exactly which one is missing. Do not infer checkout state from a stale local directory.

## Establish Checkout State

Before reading or writing, establish the checkout state from `checkout_dir`.

Derive `reviewed_commit`:

```bash
git -C "{checkout_dir}" rev-parse HEAD
```

If the command fails, stop and report that the checkout commit could not be established.

Derive `checkout_refreshed_at` from the runner's refresh marker inside the checkout's Git directory:

```bash
git_dir="$(git -C "{checkout_dir}" rev-parse --absolute-git-dir)"
cat "$git_dir/commonplace-checkout-refreshed-at"
```

If the marker does not exist or cannot be read, stop: `Checkout freshness could not be established from {checkout_dir}. Refresh the repo before writing this review.`

Then apply the freshness gate:

- If `checkout_refreshed_at` is more than 24 hours old, stop: `Checkout is stale: last refreshed {checkout_refreshed_at}. Refresh the repo before writing this review.`
- If `checkout_refreshed_at` is more than 1 hour old but no more than 24 hours old, continue but carry this warning into the final report: `Checkout freshness warning: last refreshed {checkout_refreshed_at}.`
- If `checkout_refreshed_at` is no more than 1 hour old, continue normally.

Use `reviewed_commit` for all source citations. Do not update `last-checked` without actually reading the checkout.

## Read for Style

Read 1-2 existing reviews in `kb/agent-memory-systems/reviews/` to match local style and comparison depth. Also read `kb/agent-memory-systems/README.md`.

## Read for Mechanism

Ground the review in primary repo sources:

- `README.md`
- architecture/design docs
- `CLAUDE.md` / `AGENTS.md` if present
- package manifests and build metadata
- core source files implementing the repo's central claims

Do not rely only on the README if the implementation clarifies or contradicts it.

Focus on:

- storage model
- retrieval/navigation model
- learning/distillation/promotion model if any
- validation/governance model if any
- integration surface (CLI, MCP, API, editor plugin, etc.)
- what is genuinely implemented versus only proposed
- whether the system qualifies as trace-derived learning; if it does not, leave the placement section out and do not add the `trace-derived` tag

## Write the Review

Write from the code outward:

- **Opening paragraph:** what the system is, what it is for, who built it. Include the repository URL.
- **Repository metadata:** include `**Repository:** {repo_url}` and `**Reviewed commit:** {repo_url}/commit/{reviewed_commit}` before the section headings.
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
- `tags: [related-systems]` — add `trace-derived` only if the code-grounded review finds that the system learns from agent traces. The finding drives both the tag and the placement section; the tag is not the reason to include the section.
- `status: current` unless clearly stale/outdated
- `last-checked: "{today}"`

## Trace-Derived Learning Placement

Decide whether the reviewed system learns from traces during the mechanism read. Qualifying source traces: agent/assistant session logs, conversation transcripts, tool/action traces, event streams, repeated task trajectories, rollouts. Qualifying outputs: any durable artifact derived from those traces — natural-language notes/rules/playbooks/lessons/memories (prose substrate), formal-semantic units like schemas/scripts/tools (symbolic substrate), or weight updates and other compiled runtime state (opaque substrate).

Many systems have a two-stage loop: raw traces accumulate as a knowledge substrate (session logs, episode buffers), then a distillation step — automatic or manual — produces system-definition artifacts (rules, playbooks, fine-tunes). When this pattern is present, document both stages: substrate and role at "raw" and at "distilled". The trigger, oracle, and curation policy of the distillation step is often the most discriminating part of the system.

If the system qualifies, include a `## Trace-derived learning placement` section and add `trace-derived` to the frontmatter `tags`. The section should address:

1. **Trace source** — what raw signal is consumed, and with what trigger boundaries.
2. **Extraction** — what gets pulled out, and what oracle or judge decides what becomes signal.
3. **Substrate class** — opaque (weights, distributed state), prose (natural-language units), or symbolic (formal-semantic units: schemas, code, tests).
4. **Role** — knowledge (consumed as fact; storage grows reach but not disposition) or system-definition (consumed as policy; reading the artifact *is* part of the disposition).
5. **Scope** — per-task, per-benchmark, per-project, or cross-task generalizable.
6. **Timing** — online during deployment, offline from collected traces, or staged in cycles.
7. **Survey placement** — position the system on the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), and state whether it strengthens, weakens, or splits any survey claim.

## Citations

When linking to repo code/docs, use `repo_url` plus the locally derived `reviewed_commit`:

- files: `{repo_url}/blob/{reviewed_commit}/{path}`
- directories: `{repo_url}/tree/{reviewed_commit}/{path}`

Do not link to `../../../related-systems/...` or other local checkout paths. Local checkout paths are fine for inspection notes or final reports, but review notes must remain readable on GitHub Pages.

## Constraints

**Always:**

- write the review into `kb/agent-memory-systems/reviews/`
- ground claims in repo code/docs, not just project marketing
- cite source files and directories with GitHub URLs pinned to the reviewed commit
- treat trace-derived status as a code-grounded review finding

**Never:**

- put the checked-out repo under `kb/agent-memory-systems/reviews/`
- write Markdown links from review notes into `../../../related-systems/...` or other local checkout paths
- treat proposed docs as implemented behavior without checking the code
- update `last-checked` without actually re-reading the system

## Template

```markdown
---
description: Template for related-system reviews — external system comparisons with fixed sections, borrowable ideas, and review freshness metadata
type: ../types/agent-memory-system-review.md
tags: [related-systems]
status: current
last-checked: "YYYY-MM-DD"
---

# {System name}

{One-paragraph summary}

**Repository:** {URL}

**Reviewed commit:** {GitHub commit URL}

## Core Ideas

{Core ideas}

## Comparison with Our System

{Comparison}

## Borrowable Ideas

{Borrowable ideas}

## Trace-derived learning placement

{Optional. Include only when the code-grounded review finds a qualifying trace-derived learning mechanism; otherwise delete this section. When included, also add `trace-derived` to `tags`. Cover trace source, extraction, promotion target, scope, timing, survey-axis placement, and whether the system strengthens, weakens, or splits any survey claim.}

## Curiosity Pass

- {Surprises or curiosities}
- {Simpler alternatives worth checking}
- {What the mechanism could actually achieve, even if it works perfectly}

## What to Watch

- {What might change that affects our design?}
- {What experiments are worth tracking?}
```
