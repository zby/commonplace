# Plan: promote the tool-loop workshop + reconcile "expose the loop" framing

## Goal

Promote the three workshop notes into `kb/notes/`, and align the existing
published tool-loop family (which still says "expose the loop" / "loop
exposure") with the sharpened framing the workshop produced.

## Conceptual reconciliation (no contradiction)

The vocabularies are nested, not conflicting — each is a sharper statement of
the same architectural claim:

1. **"expose the loop"** (old) — the framework should let the application get at the loop.
2. **"keep the tool loop optional"** (A) — the practical form: run the frozen loop by default, but let application code own progression when needed.
3. **"make the loop a returning value; the host language is `select`/`K`"** (B) — the concrete mechanism.

The index's *current* Resolution already defines exposing the loop as
"spawning child loops and composing them in application code" — which **is** B's
host-language-scheduler picture. So the **forcing-case arguments do not change**;
only the resolution vocabulary and one stale title do.

## The three notes to promote

- **A** `llm-frameworks-should-keep-the-tool-loop-optional` — the design case
- **B** `the-practical-scheduler-is-the-host-language` — the mechanism
- **C** `orchestration-strategies-and-run-state-have-opposite-persistence` — cross-task promotion

## Decisions for your review

**D1 — Fate of `tool-loop-index`.** It is both a curated essay *and* a tag-index hub.
Recommendation: **keep it as the tag-index hub, rewrite its Resolution to the new
vocabulary, and lead it with A/B/C.** A becomes the promoted standalone top-level
argument; the index points to it rather than duplicating it. (Alternative: let A
literally replace the index essay and demote the index to a pure generated hub —
heavier, and loses the curated forcing-case framing.)

**D2 — How aggressively to reframe.** Recommendation: **moderate-to-targeted**, file by file:
- `tool-loop-index` — rewrite the **Resolution** section to "keep the loop optional / the loop is a value" and link A, B, C; optionally add the frozen-`select` line to the intro. (essay edit)
- `stateful-tools-...` — line 11 "the 'expose the loop' argument" → "the 'keep the loop optional' argument" (one phrase).
- `agent-is-a-tool-loop` — line 15 "whether frameworks should expose the loop" → "...keep the loop optional"; link text update only.
- `codified-scheduling-...` — "a framework that exposes tools but not progression" is fine as-is (it's "exposes tools", not the dated frame). **No change.**
- `semantic-sub-goals-...` — no framing language; only a footer link to the subtasks note (updates only if D3 renames it).

**D3 — Retitle the subtasks note?** `subtasks-that-need-different-tools-force-loop-exposure-in-agent.md`
is the most dated title. Options:
- (a) **Rename** to drop "force loop exposure," e.g. `subtasks-that-need-different-tools-need-fresh-bounded-calls.md`, and keep the body's defined term "loop exposure" but gloss it as the older name for keeping the loop optional. Cost: file rename + update ~5 inbound backlinks (tool-loop-index, semantic-sub-goals, codified-scheduling, stateful-tools, agent-is-a-tool-loop) + the note's own self-references.
- (b) **Keep the title**, treat "loop exposure" as a still-valid synonym, add one sentence tying it to "keep the loop optional." Cheaper, less churn.
Recommendation: **(b)** for now — the title is a defensible synonym and renaming ripples through 5 notes; revisit if it grates.

**D4 — Tags.** A/B/C currently lack the `tool-loop` tag, so they would not appear in the
tag-aggregated index. Recommendation: **add `tool-loop`** to all three so they aggregate,
and so the index's generated "Other tagged notes" picks them up.

## Candidate operations (the batch list — execute only after approval)

Assuming D1=hub-rewrite, D2=targeted, D3=(b) keep title, D4=add tag:

1. **Move** A, B, C: `kb/work/tool-loop-control/*.md` → `kb/notes/*.md` (3 files).
2. **Rewrite intra-note links** in A, B, C: `../../notes/X` → `./X`; `../../sources/X` → `../sources/X`; sibling `./A↔B↔C` links stay `./`.
3. **Add `tool-loop` tag** to A, B, C frontmatter (D4).
4. **Edit `tool-loop-index`**: rewrite Resolution to new vocabulary; add A (case), B (mechanism), C (persistence) into the body and footer.
5. **Edit `stateful-tools-...`** (one phrase, D2).
6. **Edit `agent-is-a-tool-loop`** (one link-text phrase, D2).
7. **Edit `subtasks-...`**: add one sentence glossing "loop exposure" = "keep the loop optional" (D3b).
8. **Update workshop README + dir-index**: mark A/B/C promoted (move them to a "Promoted notes" line, like the earlier forcing-case promotions); the workshop then holds only the README + this plan + retired pointers.
9. **Validate** the moved notes + edited family with `cp-skill-validate`.
10. **Refresh indexes**; commit (one commit for the promotion+reframe, or split moves vs reframe).

## Open question on commit shape

One commit ("Promote tool-loop host-language trio; reframe expose-the-loop →
keep-optional") vs two (moves first, reframe second). Recommendation: **one** —
the reframe is what makes the promotion coherent.

## Step 2 done (2026-05-30): strip the index to a thin hub

`tool-loop-index` no longer carries the essay. The forcing-case, mechanism, and
persistence claims live in their promoted notes, and the design stance lives in
`llm-frameworks-should-keep-the-tool-loop-optional`, so the index's argued prose
was duplicative. The index is now a navigation hub: a short framing intro plus
grouped curated links (model / design stance / forcing cases / mechanism /
downstream consequences / related approaches / broader context), related
indexes, and the generated tag tail (now just `the-chat-history-model`). This
brings it into line with the index type spec. `Downstream consequences` and
`Related approaches` stayed as curated link groups rather than moving into the
promoted note, since they map sibling notes rather than develop the stance.

This workshop's work is complete and can be retired.
