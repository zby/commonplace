# Instructions: read-back direction-verdict backfill (Tier A)

**For an execution agent (Codex). Self-contained — do not assume access to prior conversation.**

You are working in the `commonplace` repo at its root. Your job is to add a one-line **read-back direction verdict** to legacy agent-memory-system reviews that do not already contain the new read-back treatment. This is the cheap, no-source-needed half ("Tier A") of a larger plan; the expensive full-section half ("Tier B") is **out of scope here** and is handled later when each system is re-reviewed.

Read [`read-back-backfill-plan.md`](./read-back-backfill-plan.md) in this directory for the full rationale. This file is the executable subset.

## Background you need

The review type at `kb/agent-memory-systems/types/agent-memory-system-review.md` now has a **Read-back Placement** concept. The core idea is the **direction** of read-back, judged **from the agent's perspective**:

- **pull** — the agent's *own deliberate memory lookup*: a query/search tool call, a file the agent chose to read, a link it chose to follow. Pull has exactly one source: the agent asked.
- **push** — memory enters the agent's context *without the agent soliciting it*, whatever the trigger: an always-loaded file/prompt, a hook on an agent action, a situation/relevance match, **or any user-initiated event** (the user asks a question, or the user tells the system to load a memory). User-initiated retrieval uses pull machinery but is **push from the agent's perspective**, because the agent did not ask.
- **both** — the system has both an agent-driven lookup path and an unsolicited-injection path.
- Net rule: **pull = the agent's deliberate lookup; everything else is push.**

Notes for edge cases:
- Unconditional **always-load** is **push** (the agent didn't ask for it) — label it `push (always-loaded)`.
- For a **library/SDK** (not an end-to-end agent), report **capability** from the API surface, not deployed behavior: `search(query)` can only pull; an `on_action(context) → memories`-style hook affords push. Say so, e.g. `pull — exposes a query API; push integration left to the host`.

## Task

For each in-scope legacy review assigned to you, derive the direction verdict from **what the review already says** about retrieval / activation / navigation, and insert one line. Do **not** re-read the system's source unless a review is genuinely unclassifiable from its own text (see Step 4).

### Single-file sub-agent mode

Default execution is one review per worker. If the parent prompt gives you an `assigned_review` path:

- Process **only** that file.
- Do not scan, edit, normalize, or validate any other review file except for quick source lookup in Step 4 when the assigned review is unclear.
- Append or update only the ledger row for the assigned review.
- Final-report only that review's direction, tier, source-check status, validation result, and any ambiguity.

The full target queue is [`read-back-backfill-targets.txt`](./read-back-backfill-targets.txt). Use it only to verify that an assigned path is in scope; do not start processing additional paths from it unless the parent prompt explicitly assigns them.

### Scope

- **In scope:** every `*.md` file in `kb/agent-memory-systems/reviews/` that is a system review, EXCEPT:
  - `dir-index.md`
  - any file matching `*.replaced.*` (archived — skip)
  - the four new reviews that already contain read-back treatment: `a-mem.md`, `graphiti.md`, `letta.md`, and `mem0.md`
- If a file is not actually a single-system review (e.g. a survey, comparison, or meta doc with no read-back semantics), **skip it** and record `skipped: not-a-system-review` in the ledger.

### The one-liner: format and placement

Insert exactly one line, in this format:

```
**Read-back:** {pull | push | both | unclear} — {short phrase, from the agent's perspective}.
```

Examples:
- `**Read-back:** pull — agent calls a vector-search tool; no proactive injection.`
- `**Read-back:** push (always-loaded) — memory file is concatenated into the system prompt each turn.`
- `**Read-back:** both — agent can query the store, and a pre-action hook injects matching guards.`
- `**Read-back:** unclear (needs source) — review describes storage but not how memory re-enters the loop.`

**Placement:** append it as the last line of the `## Comparison with Our System` section. If that heading is absent, append it as the last line of `## Core Ideas`. One line only; no new heading.

### Per-review procedure

1. **Read** the review file.
2. **Classify** the direction from the existing prose (retrieval model, activation, navigation, integration surface). Apply the rules above.
3. **Bucket** it:
   - `pull-only` → `pull`
   - `always-load-only` → `push (always-loaded)`
   - `engineered-activation` (the review describes a matcher — embedding / action-classifier / LLM-judge / typed cue — or a scope budget, before-action hook, or faithfulness/ablation test) → `push` or `both`, **and** mark `tier: B` in the ledger (a Tier-B full section is owed later — but do NOT write it now).
   - `unclear` → go to Step 4.
4. **Unclear only:** if the review text cannot support a classification, do a *quick* source peek. Find the clone path in [`systems.csv`](./systems.csv) (`path to cloned repo` column, matched by system name). Look only at integration/retrieval code (how memory enters context). If you can now classify, do so and set `source_checked: yes` in the ledger. If still unclear, write `unclear (needs source)` and move on — **never invent a push/pull claim the evidence doesn't support.**
5. **Insert** the one-liner per the placement rule.
6. **Append** a ledger row (see below).
7. **Validate** the file (see below).

### CRITICAL constraints

- **Do NOT modify frontmatter.** No `last-checked` change, no `reviewed_revision` change, no tags. The one-liner is a *body* edit only. This task is a re-classification of existing findings, **not** a re-inspection — bumping freshness metadata would be a bug. (`push-activation` tag and the full section are Tier B, added only on real re-review.)
- **Do NOT write a `## Read-back placement` section.** That is Tier B.
- **Do NOT touch** `*.replaced.*` files, `dir-index.md`, or the four already-updated new reviews (`a-mem.md`, `graphiti.md`, `letta.md`, `mem0.md`).
- **Do NOT** `git add -A`. If you commit, stage only the review files and the ledger by explicit path. Prefer one commit at the end, or batched commits; never sweep unrelated working-tree changes.

## Ledger

Create/maintain `kb/work/agentic-memory-review/read-back-backfill-ledger.csv` with header:

```
review_file,direction,tier,source_checked,notes
```

One row per processed in-scope legacy review. `direction` ∈ {pull, push, push (always-loaded), both, unclear}. `tier` ∈ {A, B} (B = full section owed later). `source_checked` ∈ {yes, no}. `notes` for skips or ambiguity.

## Validation

After editing (per file, or per batch), run:

```bash
uv run commonplace-validate kb/agent-memory-systems/reviews/<file>.md
```

Each must end in `Overall: PASS`. The one-liner is plain body text and should not trip any check. If a file was already failing before your edit, note it in the ledger and leave that pre-existing failure alone (don't try to fix unrelated problems).

## Definition of done

- Every in-scope legacy review has exactly one `**Read-back:**` line, or is recorded as skipped.
- The ledger has a row for every processed in-scope legacy review.
- No frontmatter was modified anywhere.
- Validation passes for every edited file.

## Final report

When finished, report:
- counts by direction (pull / push / push-always-loaded / both / unclear) and skips;
- the list of `tier: B` candidates (these owe a full section + `push-activation` tag at next re-review);
- the list of `unclear (needs source)` reviews;
- any files where validation failed (pre-existing vs introduced).
