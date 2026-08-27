# Decision 1 — do the representation gates keep a target limit?

## What the two gates read

- `sentence/misleading-link-text` — for each link: the link text, its sentence, then the target's **title and opening paragraph**. A head check; per-target cost is a title and one paragraph.
- `sentence/concept-attribution` — for each sentence that *identifies* a concept here with one in a linked note: the target's **treatment of that concept**. A targeted read, not a head check; but it fires only on identity claims, which are rare.

Both currently say "read at most 5 distinct target notes per review; if the limit leaves anything unchecked, name it." The number is inherited; the distinct-target counting was applied on 2026-08-25.

## Corpus data (kb/notes/, 348 notes, 2026-08-27)

Distinct linked targets inside `kb/notes/` per note:

| statistic | value |
|---|---|
| median | 6 |
| p90 | 13 |
| max | 29 (`designing-agent-memory-systems`, the synthesis monograph) |
| notes > 5 | 192 (55%) |
| notes > 10 | 59 |
| notes > 16 | 6 |

Identity claims per note (crude pattern count — "is the … [link]", "same mechanism as"): 114 notes have at least one; none has more than four.

Consequences:

- For `misleading-link-text` the cap binds on the **majority** of notes. The disclosure clause ("name what was left unchecked") is the normal case, not the exception — which is exactly the silent-lag failure mode the atomic-step note describes for review-side caps, except here it is not even silent; it is routine.
- For `concept-attribution` the cap is near-inert: it counts identity-claim targets, and no note appears to have more than four.

## Cost of removing the caps

Head check at ~200–400 tokens per target: p90 note costs 13 targets ≈ 3–5k tokens; the maximum costs 29 ≈ 6–12k. Against a typical review pass this is a small fraction. The instruction can make the read cheap by saying *how* to read the head (title plus opening paragraph, not the file) — currently a reviewer that opens the whole file pays for the body it does not need.

For `concept-attribution` the per-target read is heavier but the count is bounded by identity claims, which the co-loading bound already holds down.

## The two gates are not the same kind of check

The maintainer's correction (2026-08-27): concept attribution is close to claim grounding and is not cheap per target, even though no note currently needs more than four such checks.

`misleading-link-text` is a head check. The claim-titled target puts what the check needs where the check reads, so there is no finding-step; a second checker can redo 13 of them from the same 13 heads. The atomic-step note's reason for N — auditability of finding-steps — does not apply, so no N is needed.

`concept-attribution` reads the target's *treatment of a concept*. Only when the identity claim is on the target's title claim is that a head check. The typical identity claim names an interior concept ("the scoping note's return-value problem"), and then the reviewer must locate that treatment inside the target — the finding-step the atomic-step note prices, the same cost as an unquoted source. The exemption note's Scope clause already names this case: a linked note whose certificate does not cover what is invoked has become a source. Its cost is bounded today by rarity of the sentence shape, not by construction.

The consistent treatment, in the two notes' terms:

| identity claim points at | cost | discharged by |
|---|---|---|
| the target's title claim | head check | nothing needed |
| an interior concept, quoted verbatim in the citing note | judge the passage on the page | ADR 046 validator — it already matches against any linked file, notes included |
| an interior concept, paraphrased | finding-step | nothing; counts like an unquoted source |

The third row is what N is for. A validator cannot recognise an identity claim mechanically, so a code-enforced count is not available; and the count is ≤4 today because the sentence shape is rare, not because of a cap.

## Recommendation

- **`misleading-link-text`**: remove the cap. Check every link; read the target's title and opening paragraph; open further only when the head does not settle it. Drop the disclosure clause; keep "name any target that could not be resolved."
- **`concept-attribution`**: remove the cap — it is inert and its disclosure clause is the wrong shape — but rewrite the test head-first: read the target's head; if the concept is the target's title claim, judge there; if the citing note quotes the target's formulation verbatim, judge the quote; only otherwise locate the target's treatment. Have the ADR record that the paraphrased-interior case is a finding-step outside the artifact-side bound, tolerated on rarity, with quote-or-title as the author-side remedy if it stops being rare.
- Neither gate gains a count. If a future measurement shows a real cost problem in `misleading-link-text`, the answer is an artifact-side bound on distinct note links (the co-loading bound made explicit), not a reviewer cap.

## What this leaves for decision 2

If the sentence gates now read every linked note's head, the grounding gate's linked-note route overlaps with them. The remaining question is whether the *claim-level* representation check — a linked note cited as grounding more broadly than its claim reaches — stays in `grounding-alignment` (semantic lens, uncounted, head-only reading) or is treated as covered by the two sentence gates. My leaning: keep it in the grounding gate, because the failure it catches ("broader mechanism attributed to a link that disclaims it", the fourth of the four misses) is about the note's inference, not its link text or an identity sentence — but read only the head, and count nothing.
