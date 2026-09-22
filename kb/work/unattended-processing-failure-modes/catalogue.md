# Catalogue

Admission rule and entry status are defined in the [README](./README.md). Each admitted entry states the behavior in observable terms, the harm to unattended processing, the recorded instances, candidate explanations (tentative), a system-level countermeasure, and a candidate regression check.

## Admitted entries

### 1. Premature polishing: local repairs made inside a region a deeper repair will replace

**Behavior.** Given an artifact with one structural defect and several local defects, the editing agent repairs the local defects first, or repairs everything in the order the findings were listed. When the structural repair follows, it rewrites or deletes the region that held some of those local repairs.

**Harm.** The invalidated repairs are wasted work. Two costs matter more in unattended processing. A pass that spends its budget on local repairs can stop before the structural one, and the artifact then reads as improved while its main defect remains. And every changed text invalidates the review results tied to the old text ([criteria edits invalidate verdicts, process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md)), so each premature repair also buys a re-review that the structural repair will make stale again.

**Instances.** Operator observation, 2026-09-21, reported as a common editing behavior. One measured episode, 2026-09-22: the lead article of the series (now `kb/articles/conjectural-learning-with-fixed-models.md`) received five simplification passes on 2026-09-19 (`7a6ce359`, `2b1be982`, `099a721a`, `e83153c6`, `e1038e2e`, after the definition commit `ce6a8627`), then a vocabulary migration on 2026-09-21 and a rewrite of its argument on 2026-09-22 (`9670ede7`, 438 lines to 213). Of the 108 sentences those passes added, 0 survive at `9670ede7` in recognizable form. Two articles in the same series that received the same five passes on 2026-09-18 and were not rewritten keep 74% (bootstrap, 45 of 61) and 67% (nearest-constructions, 52 of 78) of their pass sentences at the same commit, so the lead's loss is the rewrite, not ordinary churn. Method: each pass commit's added lines joined and split into sentences over 50 characters, matched verbatim in the current article text after collapsing whitespace, stripping link targets, and mapping the renamed term; the match under-counts survival for the term-standardizing pass, whose sentences later passes rewrote while its term decision held. Whether the rewrite was foreseeable on 2026-09-19 is the question that decides whether this was premature polishing or a change of mind; the git record does not answer it, and the operator can.

The system's own guards, before this entry: `FIX-SYSTEM.md` orders its queue by finding count and states no depth or scope ordering, its constraints ("minimal edits", "don't change arguments") restrict it to local repairs, and no fix instruction checks whether the note has a pending structural recommendation from a full improvement pass. The simplification-pass orchestrator ran passes in the assessment's value order; the depth order its practice had settled on (narrow-overclaims, abstractions, readability-and-flow, plain-wording, opening-and-title) was unstated until 2026-09-22, when it and a stop-on-rewrite guard were written into [revise-an-article-or-note](../../instructions/simplification-passes/revise-an-article-or-note.md).

**The ordering rule, and why it is not "deepest first".** Two effects compete.

- *Invalidated-work cost.* A deeper repair may replace the region a shallower repair touched. The shallower repair is then wasted.
- *Preparatory value.* Some local changes make the later structural repair more reliable: standardizing a term, removing a duplicated passage, flattening an unnecessary nesting. The observable effect is a reduction in the number of simultaneous inconsistencies or distinctions the structural transformation has to carry. A transformation over a text that uses one term for one concept has fewer ways to go wrong than the same transformation over a text that uses three. This is the context-complexity effect of [soft degradation](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) applied to editing: complexity and interference constrain usable context before volume does, so removing distinctions the transformation does not need leaves more of the budget for the ones it does. That the effect is large enough to matter for a single-note repair is untested; the regression check below is designed to measure it.

So the rule is:

> Prefer fixing a deeper defect before shallower defects that it is likely to invalidate. Allow preliminary fixes that are likely to survive, or that materially reduce the complexity or risk of repairing the deeper defect.

Two terms separate the cases:

- **Premature polishing** — a local repair likely to be invalidated by the deeper change, which does not materially help that change.
- **Preparatory refinement** — a local change whose main value is making an anticipated deeper revision easier or safer. It is justified even when the deeper revision later rewrites it.

**Countermeasure (procedure).**

1. Identify the deepest known defect.
2. Estimate which parts of the artifact its repair is likely to replace or invalidate: the replacement region.
3. Suppress ordinary local fixes inside the replacement region.
4. Allow independent fixes outside it.
5. Look specifically for preparatory refinements that simplify the deeper transformation, inside or outside the region.
6. Perform the structural repair.
7. Do general cleanup afterward.

Parts of this already exist. The full improvement pass runs its structural and claim-level methods before the catalog gates, puts the flow pass after body edits "because compressing and cutting break the transitions the original prose relied on", and reruns every closing method when the final text changes ([run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md), "Why this order"). The [premise-decomposition gate](../../instructions/premise-decomposition-gate.md) already labels a defeated premise `LOCAL` or `GLOBAL`, which is a depth signal a fixer could read. The compression synthesis already excludes "local wording improvements, cosmetic changes, minor compression" from its top opportunities. What is missing is the rule as a stated claim, steps 2–5 anywhere, and any depth routing in the fix system. The open item "fix-routing-by-scope in FIX-SYSTEM" in [writing-as-thinking-process-transfer](../writing-as-thinking-process-transfer/README.md) is the place a fix-system change would land.

A general sibling exists for design search: [solve low-degree-of-freedom subproblems first to avoid blocking](../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md). The repair-ordering rule may be the revision-side counterpart. Whether it deserves its own note or a section in that one is a closing-time decision.

**Candidate explanations (tentative).** Local repairs are cheap, visible, and low-risk, so within one evaluated episode they read as progress; a structural repair risks breaking text the reader already accepts. This fits the evaluation-horizon hypothesis but does not need it: a finding list is usually dominated by local findings, and list-order processing alone produces the behavior.

**Candidate regression check.** A fixture note with one seeded structural defect whose repair replaces a known region, local defects seeded both inside and outside that region, and one seeded inconsistency whose removal simplifies the structural repair. Give the fixer the full finding list. Measure from the diffs: the *invalidated-edit rate* (edits inside the replacement region made before the structural repair and not surviving it), whether the structural repair was made at all within the budget, and whether the preparatory item was done first. Compare the unordered finding list against the procedure above, with repeated trials at a fixed model partition.

**Open questions.**

- Does a fix sweep skip a note that has a pending `revise`, `merge`, or `rehome` packet from a full pass? If not, the sweep is premature polishing at the system level, and a guard is a cheap first countermeasure.
- Can the replacement region be estimated reliably before the repair, or only coarsely (section level)? A coarse estimate may be enough to suppress most wasted edits.
- Is the preparatory effect measurable, or is it small next to run-to-run variance? The fixture above is designed to tell.

### 2. Format-driven fabrication: a required output slot gets filled when the honest result is empty

**Behavior.** When an instruction requires an output of a given kind and offers no sanctioned empty result, the model produces an instance of that kind even when none is warranted: an objection to a sound note, a finding on a clean passage, a connection between unrelated artifacts.

**Harm.** With a human reading, a contrived finding is usually discounted on sight. Unattended, it enters the fix queue as work, and the fix weakens a passage that was correct.

**Instances.** `critique-note` mandated "the strongest case against" the note with `ERROR` as the only other outcome, so a sound note had no sanctioned result. The [premise-decomposition gate](../../instructions/premise-decomposition-gate.md) found this as a design defect, and commit `e07e5dbf` (2026-08-10) added the first-class `no surviving attack` outcome. The commit records the pressure, not a specific fabricated objection; a concrete fabricated finding would strengthen the entry. The same commit records the inverse risk its verification run exposed: a weak critic declaring `no surviving attack` on an unsound note, handled by the `low confidence — needs domain check` variant.

**Countermeasure.** Every output contract that asks for findings carries an explicit, earned empty result: the worker states what it looked for and why nothing qualified, so the empty result is inspectable and is not a default. Existing instances: `no surviving attack` in [critique-note](../../instructions/critique-note.md), the `rejected` disposition in the [fix system](../../instructions/FIX-SYSTEM.md), and `Preserve or decide` in the compression synthesis. The gap is an audit: which instructions and gates still require a non-empty output?

**Candidate explanations (tentative).** A chat response that returns nothing reads as unhelpful, so preference optimization plausibly disfavors it. Instruction following alone also predicts the behavior: the instruction asked for an objection.

**Candidate regression check.** Labelled clean fixtures per finding-producing instruction; measure the false-finding rate with and without the sanctioned empty result, and the miss rate on labelled defective fixtures, since the empty result can be overused. This is the design in [calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) applied to report-kind criteria.

### 3. Finding deference: a fix pass concedes more than the finding justified

**Behavior.** Given a review finding, the fixing agent treats it as correct and edits to satisfy it, and the edit removes or weakens more than the finding's stated reason covers: a mapping, contrast, example, or dated evidence goes with the flagged sentence.

**Harm.** In an attended loop the author pushes back on a wrong or over-broad finding. Unattended, the reviewer occupies the position the user holds in chat, and nothing pushes back. Repeated passes erode the artifact's distinctive claims toward what reviewers do not object to, which by [reviewers share the field's prior](../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) is the field's prior.

**Instances.** The [error-catching systematisation](../error-catching/systematisation.md) records that "gate-driven fixing eroded dated evidence" during the migration (its claim D). The simplification pass [audit-a-prior-pass](../../instructions/simplification-passes/audit-a-prior-pass.md) exists to trace each weakened passage to its finding and restore what the finding did not justify, which is a recovery procedure written after the behavior occurred.

**Countermeasure.** Existing: the `rejected` disposition with required evidence in the fix system; `audit-a-prior-pass` as after-the-fact recovery; the full pass handing claim-level repairs back to the author. Missing: the second-order guard the error-catching grid already lists as missing ("evidence-erosion check on fix passes"), run on the fix pass's own diff before it lands. That row belongs to error-catching; this entry supplies its behavioral description and its check.

**Candidate explanations (tentative).** Agreement with the most recent critical message is the sycophancy pattern with a reviewer in the user's position. The KB has so far found no grounded sycophancy claim to cite, so this stays a candidate explanation.

**Candidate regression check.** Fixture findings in three labelled classes: correct, correct but narrower than worded, and spurious. Measure the rejection rate on the spurious class, and on the narrower class measure content removed beyond the justified span, from the diff.

## Candidates awaiting a recorded local instance

Each line names a behavior from the commissioning list and the nearest KB artifact. A session that meets one of these in Commonplace processing should record the instance here (what ran, on what, what was observed, where the evidence is) and move the line up.

| Candidate | Observable form to look for | Nearest KB artifact |
|---|---|---|
| Premature closure | A pass reports completion after silently relaxing an unmet requirement | [LLM generation relaxes goals where human writing stalls](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) (conjectural) |
| Operator-directed sycophancy | A judgment reverses after operator pushback that carried no new evidence | none; a connect run recorded the absence |
| Prose over substance | Output grows in length without adding extractable claims | [reverse compression](../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), [cheap generation breaks text volume as an effort signal](../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) — likely admissible once an instance from a pipeline run is cited |
| Assertiveness beyond warrant | Conjectural content stated without its status marker | [generation confidence does not by itself certify soundness](../../notes/generation-confidence-does-not-by-itself-certify-soundness.md); gates `prose/confidence-miscalibration`, `semantic/epistemic-status-blur` |
| Salience of obvious defects | Open review reports mechanical defects and misses a seeded judgment defect | [gate-stats](../error-catching/gate-stats.md): mechanical-surface gates catch at 2–3× the rate of judgment gates. This is not yet an instance: it measures per-gate catch rates, not what an open review notices, and mechanical defects may simply be more frequent or easier to judge |
| Current-context dominance | Recent or frequent context overrides a standing rule loaded earlier | [context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md); [chatbot-goal-state](../chatbot-goal-state/README.md) |
| Rationalization | A checker endorses invalid steps once the final answer matches its own | [reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) (external evidence) |
| Under-originated structural goals | "Improve this" yields surface fixes; a supplied role map yields a strong revision | owned by [agent-curiosity-and-structural-coherence](../agent-curiosity-and-structural-coherence/README.md) |
