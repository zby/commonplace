---
description: One worked recipe for onboarding an operator who wants to build a personal Second Brain on top of Commonplace. Use as a starting template, not the canonical path.
type: kb/types/instruction.md
---

# Example: Onboard a Second Brain on Commonplace

This is one opinionated recipe for turning a fresh `commonplace-init` workspace into a personal Second Brain — a knowledge base shaped around a specific operator, their projects, and their context.

It is **not** the canonical Commonplace onboarding. Phases 1–3 use only Commonplace primitives (collections, registers, note types, distillation, the connect/validate skills). Phases 4–5 add Claude Code harness extensions (hooks, custom skills) that sit *alongside* Commonplace — adopt or skip them independently.

Treat each phase as a gate: confirm it works before moving on. If a step fails, propose two alternatives rather than retrying.

## Prerequisites

- A workspace initialised by `commonplace-init` (ships `kb/notes/`, `kb/reference/`, `kb/instructions/`, the `cp-skill-*` family, and a pre-compiled collection topology).
- `qmd` installed and the `COMMONPLACE_QMD_INDEX` env var pointing at a writable index path.
- The operator available for an interview (Phase 1 is conversational, not a form).

Read `CLAUDE.md`, `kb/notes/COLLECTION.md`, and `kb/instructions/COLLECTION.md` before starting so register vocabulary is loaded.

## Phase 1 — Profile and collection design

### 1a. Profile the operator

Interview the operator with 5–7 conversational questions covering: role and day-to-day work, what they're optimising for this year, real working style (tools they actually use, not aspirational), growth edges and recurring feedback, and what they care about outside work.

Write the result to `kb/notes/me.md` as a `structured-claim` or `text` note (whichever fits — `me.md` is descriptive about a person, so a plain note with no claim title is fine; mark with the standard frontmatter and seedling status).

Run `/cp-skill-connect kb/notes/me.md` to surface candidate links. Apply the ones that hold.

### 1b. Design new collections

Commonplace ships three collections that are already register-anchored:

| Path | Register | Quality goal |
|---|---|---|
| `kb/notes/` | theoretical | reach |
| `kb/reference/` | descriptive | accuracy |
| `kb/instructions/` | prescriptive | executability |

A Second Brain usually needs more. Interview the operator about what else they want to capture. Common candidates (ask, don't assume):

- Journal/log (narrative register — what happened, what was noticed)
- People/contacts (descriptive — relationship context)
- Project notes (descriptive, plus workshop layer for in-flight work)
- Evaluations (evaluative — pitches, tools, opportunities)
- Distilled context (theoretical or descriptive — strategic, role, historical summaries)
- Personal reference (descriptive — the operator's own systems, separate from Commonplace's)
- Personal instructions (prescriptive — the operator's own procedures, separate from Commonplace's)

For each agreed collection:

1. Create the directory under `kb/`.
2. Write a `COLLECTION.md` defining: register, quality goal, title conventions, scope (what belongs and what doesn't), and outbound linking conventions. Use the existing three `COLLECTION.md` files as models — do not invent a new schema.
3. Distinguish library collections (value accumulates) from workshop collections (value is consumed). In-flight project work belongs in `kb/work/<project-name>/`, not in a long-lived collection. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`.
4. Add the collection to the routing table in `CLAUDE.md`.

Run `/cp-skill-compile-collections` once all new `COLLECTION.md` files are written. This rebuilds the topology document the connect skill relies on.

**Verify Phase 1**: every new collection has a `COLLECTION.md` whose register and quality goal an agent could state without re-reading. The routing table in `CLAUDE.md` mentions every collection. `me.md` exists, validates, and has at least one connection.

## Phase 2 — Populate the knowledge base

Bulk-import the operator's existing material into the collections designed in Phase 1.

1. Ask where documents live: Google Docs, Notion exports, local files, web pages, GitHub issues, X threads.
2. Route each document to the collection whose register matches its content. A pitch deck evaluation is evaluative; a meeting transcript is narrative; a project status doc is descriptive. The routing table in `CLAUDE.md` is the source of truth.
3. For web sources, use `/cp-skill-snapshot-web <url>`. For local files, place them in the right collection and run `/cp-skill-ingest <path>` to classify and connect.
4. Refresh the semantic index:
   ```bash
   qmd --index "$COMMONPLACE_QMD_INDEX" update
   qmd --index "$COMMONPLACE_QMD_INDEX" embed
   ```
5. Test together. Ask the operator for three things they remember working on. Search the KB with both `rg` (keyword) and `qmd` (semantic). If recall is poor, troubleshoot — bad results here mean Phases 3–5 are building on sand.

**Verify Phase 2**: at least one note in each populated collection passes `cp-skill-validate`. The operator can find at least 80% of the things they remember via combined `rg` + `qmd` search.

## Phase 3 — Distill context summaries

Phase 3 is [distillation](../notes/definitions/distillation.md) in the Commonplace sense: directed compression whose purpose is the capacity change it produces in the consuming agent. The consumer here is *every future Claude Code session* on this workspace — the summaries should let it act competently with bounded context.

In the context collection designed in Phase 1 (commonly `kb/context/`), write:

- `strategic-context.md` — what the operator is trying to accomplish across projects, and why
- `role-context.md` — responsibilities and how multiple roles fit together
- `historical-context.md` — key decisions, pivots, lessons
- `personal-growth.md` — patterns in feedback and coaching themes

For each note, follow the standard Commonplace content workflow:

1. Search first (`rg` + `qmd`, ≥10 queries mixing both).
2. Read the target collection's `COLLECTION.md` before writing.
3. Use `/cp-skill-write` with the appropriate type.
4. Cite source notes with markdown links and the right link semantics for the register pair (`evidence`, `derived-from`, `since`, `because` — see each `COLLECTION.md`).
5. Flag inferences explicitly. Do not blur quotation and synthesis.
6. Run `/cp-skill-validate <note>` before considering it done.

**Verify Phase 3**: each summary cites ≥5 source notes, validates clean, and a fresh agent loaded with only that summary plus `me.md` can answer "what is this operator trying to do" coherently.

---

## Harness-level extensions (optional)

The remaining phases are **not** Commonplace methodology. They wire the KB into the Claude Code harness — useful, but a different layer. Skip them if you want a pure Commonplace setup.

## Phase 4 — Automatic context injection (Claude Code only)

Add a `UserPromptSubmit` hook that enriches every prompt with relevant KB context.

1. Create `~/.claude/hooks/context-enrichment.sh` that:
   - Extracts key terms from the prompt.
   - Runs `qmd --index "$COMMONPLACE_QMD_INDEX" query` and `rg` in parallel against `kb/`.
   - Returns top results inside a `<context>` block.
   - Times out at 2 seconds — kill any search that runs longer.
2. Register it in `~/.claude/settings.local.json` under `hooks.UserPromptSubmit`.
3. Test by typing a deliberately under-specified prompt about something in the KB. Confirm the hook injected useful context.

If the hook is slow or noisy, prefer turning it off over tuning it for hours — context engineering at the harness level is a separate research problem.

## Phase 5 — Learning loops (Claude Code only)

Three feedback loops, separately useful:

**Per-session** — `.claude/skills/learn/SKILL.md`: at session end, review the conversation for mistakes, surprises, and validated approaches. Update `CLAUDE.md` with new tool gotchas or workflow preferences. Save genuinely-new context to memory files. Bias toward brevity.

**Per-day** — `.claude/scripts/morning-brief.sh`: list KB notes touched yesterday (`git log --since`), surface unconnected notes and pending items in `kb/work/`, run `cp-skill-validate` on the changed set, output a 2-minute brief.

**Per-month** — `.claude/skills/retro/SKILL.md`: ask what was attempted, how it went, what patterns emerged. Search the KB for notes created or modified this month. Update the Phase 3 context summaries with anything that shifted. Append a monthly entry to a retro log under `kb/work/retros/`.

## Verify the whole onboarding

- Every new collection has a valid `COLLECTION.md` and appears in the `CLAUDE.md` routing table.
- `commonplace-generate-notes-index kb/notes` runs clean.
- `cp-skill-validate` passes on a sampled note from each collection.
- The operator can ask a fresh Claude Code session a project-specific question and get an answer grounded in their KB, not invented.

## What this recipe is NOT

- The canonical Commonplace onboarding. Commonplace itself does not require a profile, context summaries, hooks, or learning loops.
- A spec for Phases 4–5. The hook and skill bodies sketched there are illustrative; treat them as prompts for design, not finished code.
- A justification of *why* these choices work. The reasoning lives in the methodology notes under `kb/notes/` (distillation, registers, workshop layer). This file is execution-only.
