# Gate noise audit (runs 05-08)

Scope: all WARN findings across accessibility, sentence, prose, semantic, complexity, structural, and frontmatter reviews for four runs on the same baseline. Evaluated against the change catalogue and target.

## Gates with clean signal (true positives, stable)

- **[parsing-ambiguity]**: Fires on "The mistake is not storing a trace" in all four runs with identical reasoning (negation-scope ambiguity parses as "failing to store"). Matches change-catalogue C1. Stable wording, stable severity, correct diagnosis. The most reliable gate in the bundle.

- **[stock-phrases]**: Fires on "This is not just summarization — it is interface design" in all four runs. Correctly identifies the "not just X — it is Y" elevation pattern and applies a deletion test showing the next sentence already carries the point. Matches C4. Stable and well-calibrated.

- **[broken-link-path]**: Fires on `./distillation.md` (should be `./definitions/distillation.md`) in all four runs. Objective, deterministic, matches X2. No noise possible — the file either exists or it doesn't.

- **[compound-bullet]**: Fires on line 99 (artifact-first loading + "does not mean minimal" caveat) in all four runs. Correctly identifies two separable claims joined by "but." Matches S6. Stable.

- **[bullet-capitalization]**: Fires on lowercase-starting bullets in the breakdown list (lines 42-46) and practical principle (lines 97-100) in all four runs. Matches X1. One minor variation: run 05 also flags lines 13-14, which runs 06-08 correctly treat as sentence-completing continuations (INFO or omitted). The gate's core findings are stable.

- **[notation-opacity]**: Fires on `K`, `select(K)`, and `P` notation in all four runs. Correctly identifies that the symbols are from another note and do no formal work here. Matches A2. The recommendations are consistent: replace with plain language. Run 05 includes `P` as a separate finding; other runs fold it in or note it's already glossed. Minor presentational variation, not signal variation.

- **[undefined-terms] on "execution boundary"**: Fires in all four runs on the missing gloss for "execution boundary" on first use. Matches A1. Stable and correct.

- **[connection-inflation]**: Fires in runs 06, 07, 08 (not 05). Correctly identifies that most Relevant Notes entries restate relationships already articulated in the body. Not in the change catalogue, but the target preserves this structure unchanged, so the finding identifies a genuine issue the target chose not to address. The finding is consistent across the three runs that fire it; run 05's complexity review produced 0 WARNs, making it the outlier (see Unstable section).

## Gates with noise or wrong-direction findings

- **[undefined-terms] on "external symbolic state"**: Fires as WARN in runs 05 and 07, does not fire as WARN in 06 and 08. The target replaces the phrase with plain language (matching A2's direction), so the finding is directionally correct. But the gate conflates this with the notation-opacity finding — "external symbolic state" is an English phrase, not notation, and the real problem is that `K` substitutes for it without local definition. When the notation is replaced with plain language (as the target does), "external symbolic state" becomes self-explanatory. Flagging it as a separate undefined-term finding alongside the notation-opacity WARN is double-counting the same problem.

- **[undefined-terms] on "clean model"**: Fires as WARN only in run 08 ("In the clean model, loading happens through `select(K)`"). The phrase "clean model" is indeed unclear in isolation, but the target removes the notation entirely and rewrites the passage, making this finding moot. It is a real but low-value finding that only one run catches — and it disappears when the notation-opacity fix is applied. Noise in the sense that it will never survive into an actionable recommendation independent of A2.

- **[jargon-persistence] on "bounded call/context"**: Fires as WARN in runs 06, 07, 08 but not in run 05. Run 05 demotes it to INFO. The finding matches A4 and the target does strip "bounded" from body occurrences, so it's directionally correct. But the framing varies significantly: run 06 says 14 occurrences, run 07 says "at least 12," run 08 says "~10." These counts are on the same baseline. The instability is cosmetic (the recommendation is the same), but the severity flip between run 05 (INFO) and runs 06-08 (WARN) means the gate's WARN threshold is subjective.

- **[unidentified-references] on Spacebot**: Fires as WARN in runs 05, 06, 08 but drops to INFO in run 07. The target does not add an identification for Spacebot — it leaves the bullet unchanged. The change catalogue lists A3 (identify Slate) but has no equivalent for Spacebot. The finding is reasonable in principle (readers don't know what Spacebot is), but the note already links to the Spacebot related-system page. Adding a gloss like "a branching agent system" (as runs 05 and 06 recommend) would require the reviewer to fabricate a characterization not present in the baseline. The gate text should clarify whether a link to a dedicated page is sufficient identification or whether inline glossing is always required.

- **[completeness-boundary-cases] on the trace taxonomy gap**: Fires as WARN in runs 06, 07, 08 but only as INFO in run 05. All three WARN runs identify a gap in the three-type trace taxonomy, but each invents a *different* missing type:
  - Run 06: "structured intermediate artifacts" (relevance labels, partial syntheses, claim lists)
  - Run 07: "state-change / artifact-mutation traces" (file diffs, database writes, API mutations)
  - Run 08: "hybrid traces where reasoning and tool use are interleaved"

  These are three different boundary cases. The target's response was to compress the entire taxonomy into a single sentence rather than expand it (change S3), which suggests the right answer was not "add a fourth type" but "the taxonomy was overbuilt." The gate is correctly identifying that the taxonomy has soft edges, but its recommendations (expand the taxonomy) point in the opposite direction from what the target actually does (compress it). This is a **wrong-direction finding** — the gate correctly detects a problem but prescribes expansion when compression was the right fix.

- **[grounding-alignment] on distillation vs execution-boundary compression**: Fires as WARN in runs 05 and 07, INFO in runs 06 and 08. Runs 05 and 07 flag that equating execution-boundary compression with distillation is a semantic stretch (some boundary artifacts are codification, not distillation). This is a legitimate conceptual point, but the target keeps the distillation link and the relationship framing intact — it just fixes the broken path. The gate is identifying a real but debatable semantic tension that the author chose to leave as-is. The instability (WARN vs INFO across runs) confirms the finding is at the subjective boundary.

- **[framing-mismatch] on "For orchestration"**: INFO in runs 05 and 06, WARN in runs 07 and 08. The finding matches C2 (reframe as cognitive-capacity argument, not orchestration-specific). The target does reframe this way, grounding it in soft degradation. The finding is correct, but the severity flip across runs makes it unreliable as a gate signal — a run that produces only INFO here would not trigger a revision.

- **[concept-attribution] on ad-hoc prompts link**: Fires as WARN only in run 08. Claims the ad-hoc-prompts note "does not discuss judgment-heavy caller selection or search-trace inheritance." But the target keeps this exact bullet unchanged (line 46), suggesting the author considers the attribution valid. The finding appears to be a misread of the linked note's scope — ad-hoc prompts are precisely about the caller assembling a focused task frame, which is judgment-heavy selection. This is a **false positive**.

- **[anthropomorphic-framing] on "sessions want"**: Fires as WARN only in run 08 ("Interactive sessions want continuity and visibility"). The target keeps this sentence unchanged (line 69). The objection is pedantically correct ("want" attributes desire to software), but this is conventional shorthand that no technical reader would misinterpret. Previous runs flagged "how the agent thought" at INFO level but did not flag "sessions want" at all. This is a **false positive** — the gate is overcounting standard metonymy.

- **[bridge-paragraph-duplication]**: Fires as WARN only in run 08. Matches change-catalogue S1 (cut duplicate bridge paragraph). The finding is correct and directionally aligned with the target. But it only fires in one of four runs — the other three runs' prose reviews do not catch it. This means the gate is **unreliable** for detecting this pattern, not that it's wrong when it fires.

## Gates with unstable severity

- **[framing-mismatch]**: INFO in runs 05 and 06, WARN in runs 07 and 08. Same baseline, same sentence ("For orchestration, that is usually the wrong trade"). The finding is correct in all four runs — the mechanism is not orchestration-specific. The severity flip suggests the WARN/INFO threshold is too subjective for this gate. Since the target does address this (C2), the runs that rated it INFO missed a real change.

- **[general-before-specific]**: INFO in runs 05 and 06, WARN in runs 07 and 08. Same structural issue (Slate tension section before the general execution-boundary compression section). Runs 05 and 06 explicitly note "flagging as INFO rather than WARN because both orderings have defensible rationale." Runs 07 and 08 promote to WARN without acknowledging the defensible counterargument. The target reorders these sections (S5), so the WARN runs got it right, but the flip reveals that the gate's criteria don't deterministically distinguish "defensible alternative order" from "wrong order."

- **[unidentified-references] on Spacebot**: WARN in runs 05, 06, 08; INFO in run 07. The demotion in run 07 appears to reflect a judgment that the link to the Spacebot page provides sufficient context, while the other runs consider inline identification mandatory regardless of links. The gate text should specify which standard applies.

- **[connection-inflation]**: No WARN in run 05, WARN in runs 06, 07, 08. Run 05's complexity review found 0 WARNs and only flagged inflation at INFO level. The other three runs consistently fire WARN. Since the finding is the same in all runs (most footer entries duplicate body explanations), run 05 is the outlier — likely a threshold judgment call rather than a different analysis.

- **[redundant-restatement]**: Fires as WARN in runs 05 and 07 but on *different passages*. Run 05 flags the opening of "Why transcript inheritance breaks down" as restating the prior section. Run 07 flags the closing paragraph (lines 101-102) as restating the thesis. Run 06 demotes the closing-paragraph restatement to INFO. Run 08's prose review finds no redundant-restatement WARN at all. The gate is catching a real pattern (the note does restate) but cannot agree on *which* restatement is severe enough for WARN.

- **[confidence-miscalibration]**: WARN in run 06 only (trace taxonomy presented with assertive framing). Runs 05, 07, 08 find no miscalibration WARN — run 07 explicitly marks this CLEAN ("introduced with 'at least three trace types,' which proposes rather than asserts exhaustiveness"). Direct contradiction between runs on the same text. The gate cannot reliably distinguish "one useful framing" from "assertive framing" on this baseline.

## Recommendations

1. **[completeness-boundary-cases]**: The gate's recommendation to expand taxonomies is systematically wrong-direction for notes that are already overbuilt. Add guidance: "If the taxonomy is already longer than it needs to be, the right fix may be compression rather than adding a fourth category. Check whether the taxonomy's weight is justified before recommending expansion."

2. **[framing-mismatch]**: The INFO/WARN threshold flips on identical text. Sharpen the gate: promote to WARN when the framing *excludes* cases the mechanism covers (as here, where "for orchestration" excludes general bounded-call consumers). Keep at INFO when the framing merely *emphasizes* one domain without excluding others.

3. **[general-before-specific]**: Same instability. Add a tiebreaker: "If the specific case *qualifies* the general rule (i.e., is a counterexample or tension), specific-before-general is defensible. If the specific case *exemplifies* the general rule, general should come first." The Slate section is a tension case, which explains why runs 05-06 correctly rated it defensible — but the target still reordered, suggesting the author preferred general-first regardless.

4. **[unidentified-references]**: Clarify whether a link to a dedicated page (e.g., a related-system note) satisfies the identification requirement, or whether inline glossing is always required. This would stabilize the Spacebot finding.

5. **[redundant-restatement]**: The gate fires on different passages across runs, suggesting it lacks specificity. Consider adding a structural heuristic: "Flag as WARN only when a restatement appears in the same argumentative role as the original (e.g., both are thesis statements). If one is setup and the other is summary, the restatement may be intentional reinforcement — flag as INFO."

6. **[confidence-miscalibration]**: Run 06 fires WARN on "History conflates at least three trace types" while run 07 marks the same text CLEAN because "at least" hedges the claim. The gate cannot reliably distinguish hedged from assertive framing here. Consider removing this gate or narrowing it to cases where quantitative claims are made without evidence (the trace taxonomy is a qualitative analytical move, not an empirical finding that needs calibration).

7. **[concept-attribution]**: The run-08-only WARN on the ad-hoc prompts link is a false positive. The gate may be reading linked notes too narrowly. Add guidance: "If the linked note's core concept (e.g., flexible prompt-layer assembly) supports the claim being made, the attribution is valid even if the exact phrase used in the link text does not appear verbatim in the target."

8. **[anthropomorphic-framing]**: The run-08 WARN on "sessions want" is a false positive. Add an exception for conventional metonymy applied to software systems ("the system wants," "the API expects," "the protocol requires") — these are standard technical shorthand, not anthropomorphism claims.

9. **[undefined-terms]**: The gate double-counts when it flags "external symbolic state" alongside `K` notation-opacity. These are the same access barrier. Add: "If a term is opaque primarily because it is used as a label for notation defined elsewhere, and the notation-opacity gate already covers the notation, do not double-flag the English phrase."
