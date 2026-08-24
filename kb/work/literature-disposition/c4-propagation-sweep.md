# How far the pointer-context monotone actually spread

Sweep executed 2026-08-24 over every tracked artifact citing
`agents-navigate-by-deciding-what-to-read-next`, after the
[first source-grounding case](../source-grounding/worked-case-agents-navigate.md)
found its C4 — "the more context a pointer carries, the cheaper the navigation
decision" — absent from the source and wrong by the source's own lights.

The question was not whether the note overlaps the literature. It was whether a
defect in it had propagated, and how expensively.

## Result: 1 inheritor, 15 uses of the sound claims, 4 incidental

Twenty tracked artifacts cite the note. One rests on the monotone; fifteen rest
only on the claims the source does support (the follow/skip unit, the
probabilistic judgment, judging a target from its pointer); four are incidental.

**The one inheritor is a verbatim copy, not an inference.**
[`linking-theory.md`](../../notes/linking-theory.md) line 17 reproduces the
sentence while attributing it to the note.

## The error is not operative

Nothing shipped encodes the monotone. The note has **zero reach** into
`kb/reference/`, `kb/instructions/`, `kb/types/`, `kb/agent-memory-systems/`,
`kb/agentic-systems/`, and `kb/articles/` — every citation is from `kb/notes/` or
a source ingest. Checked and clear: the note schemas, every `COLLECTION.md`, the
review gates, the ADR set, and `src/commonplace/`, which carries no
description-length logic at all.

So this is a prose defect. No contract, schema, gate, or validator migration
follows from correcting it.

## The shipped system already holds the corrected model

This is the part that reverses the expected direction of repair.

The description warning band is enforced at
`kb/types/note-base.schema.yaml` (50–250 characters, warn). Its rationale is
[ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md)'s
2026-07-28 amendment, which set it from a controlled retrieval assay comparing
120/160/200/250/300-character allowances at 44 trials each:

> In 44 trials per allowance, 250 was the shortest allowance with no false skips
> or irrelevant opens; 300 added no retrieval benefit and exceeded the assay's
> declared 8,000-token estimate at an 80-result slice, while 250 remained within
> it.

That is the corrected model, arrived at empirically and eleven months before the
source was read: an interior optimum, with the break-even priced against
result-set size. The ADR adds that the ceiling "is an allowance, not a target."
The two other operative surfaces agree and are diagnosticity-shaped rather than
volume-shaped — the `description-discrimination` gate asks whether a description
"adds retrieval value beyond the title," and `fix-descriptions.md` names "summary
creep" as a failure and allows the extra room "only when it changes the read/skip
decision."

**The shipped system is ahead of the note.** The theory layer is the stale one.

## The KB already contradicts the monotone — including inside the inheritor

Not an isolated error, an unresolved internal disagreement:

- `linking-theory.md` **contradicts itself**. Line 17 carries C4; line 39 states
  the note's actual thesis — "link quality is the reduction of navigation
  uncertainty per unit of context consumed" — and prediction 4 states the
  interior optimum outright: "If the marginal link carries less decision-relevant
  information than the context cost of processing it, it hurts navigation rather
  than helping it." Its own frontmatter description carries the per-token form.
  The wrong sentence is the imported one; the note's own argument refutes it.
- [`addressability-grain-sets-a-matched-selective-read-floor`](../../notes/addressability-grain-sets-a-matched-selective-read-floor.md)
  prices pointer and target in one currency and notes that a collection-wide
  search "can fan out across many candidates, multiplying those units."
- [description-length-optimization](../description-length-optimization/README.md)
  is a live workshop whose goal is anti-monotone by construction.

`pointer-design-tradeoffs-in-progressive-disclosure` does **not** counterweight
it: its cost axis is precomputation and authoring cost, not cue-token
consumption. That is a gap in that note, not a contradiction of this one.

## What this implies for disposition — evidence, not a verdict

The [input critique](./chatgpt-critique.md) proposed "retire or reduce to a thin
claim adapter," on the theory that the note is information scent in local
vocabulary. Three claims overlap that literature, but the later strict re-run
found that none is wholly subsumed as written. The disposition the evidence
points at is different in kind:

- retiring the note at sweep time would have removed claims that needed
  narrowing rather than deletion **and left the monotone standing in
  `linking-theory.md`**, which is where the only propagation damage was;
- the corrected claim does not need inventing. `linking-theory.md` already states
  the per-token half in its own thesis, and
  [`two-context-boundaries-govern-collection-operations`](../../notes/two-context-boundaries-govern-collection-operations.md)
  states the result-set half — "how much higher depends on description length,
  context window size, and what else competes for the window";
- so the shape is closer to **delete one paragraph in two places, promote the
  formulation `linking-theory.md` already owns, and attach the result-set
  break-even to a durable note** than to any of the critique's four dispositions.

Two independent routes arrived at `linking-theory.md`: this sweep found it the
sole inheritor, and the Pirolli ingest — written without access to this sweep —
independently recommended it as the update target, noting that "prediction 4
(link density has diminishing returns) is the patch model under another name."

Still open, and genuinely: whether `agents-navigate-...` survives the correction
at all. After correction it contains three narrowed source-adjacent claims, an
explicit human-to-LLM transfer argument, and local pointer-mode design
implications. Whether those warrant a separate note, a merge into
`linking-theory.md`, a thinner node, or retirement remains an artifact-level
decision.

## Execution update — 2026-08-24

The correction has now been executed. `agents-navigate-...` narrows the three
source-adjacent claims, states the human-to-LLM transfer boundary, and replaces
C4 with uncertainty reduction per unit of context consumed. `linking-theory.md`
received the same source route and no longer carries the monotone. Source review
pairs passed for both artifacts with no stale pair.

The artifact-level disposition remains open. The correction removed the known
error and its only propagation edge; it did not decide whether the first note
should survive, merge into `linking-theory.md`, become thinner, or retire.
