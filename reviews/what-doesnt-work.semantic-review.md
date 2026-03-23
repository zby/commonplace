=== SEMANTIC REVIEW: what-doesnt-work.md ===

Claims identified: 8

1. "Hook-driven automatic commits after every note operation created a mess" (Auto-commits section)
2. "Commits were noisy, hard to review" (Auto-commits section)
3. "we spent significant effort removing them" (Auto-commits section)
4. "Agents should not commit without explicit human approval" (Auto-commits section — prescriptive generalization)
5. Together with what-works, this is "the manual observation log that a KB learning loop would eventually feed from" (Auto-commits section, paragraph 2)
6. "these anti-patterns are ground truth for what mutations the loop should avoid proposing" (Auto-commits section, paragraph 2)
7. Five areas enumerated under "Observations needing more evidence" constitute the areas that showed friction but lack sufficient evidence (implicit scope claim)
8. "orphan rate reached ~90%" (Connection requirements bullet)

WARN:
- [Completeness] The note's title claims to cover "what doesn't work," but the confirmed anti-pattern section contains only one item (auto-commits). Everything else is explicitly marked as needing more evidence. This means the note has exactly one confirmed negative finding. The title overstates the note's coverage — a reader expecting a catalog of proven failures will find one confirmed case and five tentative observations. A title like "auto-commits don't work and five areas need more evidence" would be more accurate, though admittedly less usable as a link target.
- [Completeness] The "Observations needing more evidence" list enumerates five areas of friction but provides no indication of what space it was drawn from. Are these the only areas that showed friction? Were other candidates considered and excluded? The note offers no framing for how these five were selected, making it impossible to assess whether the list is complete. For example, the companion note what-works.md discusses patterns like prose-as-title, template nudges, discovery-first, frontmatter queries, semantic search, and public/internal boundary — yet the "doesn't work" note doesn't mention negative experiences with any of these or explain why they don't appear here. The asymmetry is not necessarily wrong (perhaps nothing went wrong with those patterns), but the absence of a selection rationale is a gap.

INFO:
- [Completeness] The prescriptive claim "Agents should not commit without explicit human approval" generalizes from one observed failure (hook-driven auto-commits) to a blanket rule. The observed failure was specifically about hook-driven commits after every note operation. Other commit automation strategies (e.g., agent commits at session end after human review of a diff, or agent commits only when explicitly asked) are not addressed. The generalization may be correct, but it covers a broader space than the evidence strictly supports.
- [Completeness] The "connection requirements outpace connection-making" bullet reports "orphan rate reached ~90%" but does not clarify the denominator — 90% of all notes? Of notes created in a specific period? Of notes created by agents? The statistic is striking but ungrounded enough that different readers might interpret it differently.
- [Grounding alignment] The note claims it and what-works together form "the manual observation log that a KB learning loop would eventually feed from." The linked note automating-kb-learning-is-an-open-problem.md does reference both notes in its body ("keep building the KB manually, pay attention to what works and what doesn't") and its Relevant Notes section ("the anti-pattern log; complements what-works as ground truth for what the loop should avoid proposing"). The attribution is accurate — the linked note does assign this role to the pair. However, the framing in what-doesnt-work.md subtly elevates the status: "ground truth for what mutations the loop should avoid proposing" implies these observations have the standing of verified negative examples, when the note itself marks four of five observations as needing more evidence. The tension between "ground truth" and "needing more evidence" is worth noting.
- [Internal consistency] The note's type is `review` (per frontmatter), which aligns with its observational register. However, the auto-commits section shifts from observational ("created a mess") to prescriptive ("Agents should not commit without explicit human approval") without signaling the shift. The "Observations needing more evidence" section maintains a consistently tentative register. The prescriptive claim in the auto-commits section is the only place the note makes a recommendation, creating a mild register inconsistency between the two sections.

PASS:
- [Internal consistency] No pairwise contradictions found between sections. The auto-commits section presents a confirmed finding; the observations section presents tentative findings. These are complementary, not contradictory.
- [Internal consistency] No definition drift detected. Terms are used consistently throughout.
- [Grounding alignment] The link to what-works.md is used correctly — the note references it as the companion positive-pattern log, and what-works.md does serve that role.
- [Grounding alignment] The link to automating-kb-learning-is-an-open-problem.md accurately reflects the relationship described there: both notes are positioned as manual observation logs feeding a future learning loop.
- [Completeness] The five "needing more evidence" items are appropriately hedged. Each uses qualifying language ("unclear," "may pay off differently," "the question is whether," "unclear whether," "may not be the problem") that avoids overclaiming. The note does not assert these are failures — only that they showed friction.

Overall: 2 warnings, 4 info
===
