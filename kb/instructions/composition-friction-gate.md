---
description: Experimental, run-by-hand, report-only gate that reconstructs from outside the filter and signal that frictionless generation strips from a note — does the central claim survive concretization, and which inferential joints are least supported. Run in a fresh adversarial sub-agent. Surfaces weak joints for a human; emits no pass verdict.
type: kb/types/instruction.md
---

# Reconstruct a note's composition friction

Experimental, run by hand. When an LLM denoises a rough idea into fluent prose, it returns the most plausible artifact it can and never marks whether that artifact is a full solution or the best it could manage with one constraint quietly dropped. The human writer's stall is that missing mark, and it does two jobs: the **filter** (a claim with no consistent single form has no witness, and dies at the keyboard) and the **signal** (the stall locates where understanding is thinnest). This gate reconstructs both from outside the text. It is **not a review gate** — it writes no acceptance or freshness state and is not wired into the review system. Write the report; do not touch the note.

Run it in a **fresh sub-agent**, a different runner than wrote the note, so the checker has no sympathy for the note's framing. Separation is what gives the check teeth: the same generator that wrote smoothly over a gap will read smoothly over it too.

## The hard rule

Do **not** emit an overall "consistent / not consistent" verdict, and do not pass or accept the note. A fluent self-grade is exactly the false signal this gate exists to replace — a green check that means nothing is worse than none. The only product is **routed attention**: the surviving contradiction (if any) and a ranked list of the thinnest joints, for a human to judge.

## Check 1 — Filter: does the claim survive concretization?

1. State the note's central claim in **one sentence**. If you cannot — if it resolves to several different claims — record that; a claim that won't concretize to one thing has already failed the filter.
2. Name the properties or goals the claim wants to hold **at once**. Test whether they can coexist, or whether committing to one forces giving up another (the "as fast as C and as dynamic as Lisp" move — beautiful as a wish, contradictory as a build).
3. Record `SURVIVES` (there is one consistent thing the claim commits to) or `DISSOLVES` (concretization splits it into incompatible parts), and name the contradiction if it dissolves.

## Check 2 — Signal: locate the thinnest joints

1. Enumerate every **load-bearing inferential joint** in the note: explicit connectives (`because`, `therefore`, `so`, `thus`, `hence`, `since`, `obviously`, `clearly`, `it follows`) and the implicit ones, where one sentence is offered as the ground for the next without a connective word.
2. For each joint, adversarially test whether the stated reason actually supports the conclusion. **Default to `UNSUPPORTED` when uncertain.** The joint must earn its place; do not extend it the benefit of the doubt the way fluent reading does. This skeptical default is the point — it restores the cost that made a human's "because" mean something.
3. Rank the joints from thinnest support to strongest. Surface the weakest three to five.

## Output

Write to `kb/reports/friction/<note-name>.friction.md`. Mutate nothing else.

```markdown
# Friction check: <note title>

**Note:** <path>
**Central claim (one sentence):** <or "does not concretize to one claim">

## Filter
**Verdict:** SURVIVES | DISSOLVES
<if DISSOLVES: the properties that cannot coexist, and which trade-off the note ignores>

## Signal — thinnest joints
1. **<the connective or implicit inference, quoted>** — <UNSUPPORTED | THIN | HOLDS> — <what the reason fails to establish>
2. ...

## For the human
<one line: where to look first — the dissolved claim, or the joint that most needs the author's missing concretization>
```

---

Relevant Notes:

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — rationale: the composition stall this gate reconstructs, and why a self-graded verdict cannot substitute for it
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — rationale: the no-verdict, routed-attention-to-a-human-judge design is this note's condition for the loop reconstructing the filter, applied here as the hard rule against emitting a pass/fail verdict
