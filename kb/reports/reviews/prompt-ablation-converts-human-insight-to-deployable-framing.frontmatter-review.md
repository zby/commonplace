<!-- REVIEW-METADATA
note-path: kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md
last-full-review-note-sha: 5c24c6cd5ea58e587a6a57daff8bcf7bbd1d979b
last-full-review-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-full-review-at: 2026-03-24T20:56:22+01:00
last-accepted-note-sha: 5c24c6cd5ea58e587a6a57daff8bcf7bbd1d979b
last-accepted-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-accepted-at: 2026-03-24T20:56:22+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: prompt-ablation-converts-human-insight-to-deployable-framing.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism beyond the title: "controlled variation against a human-verified finding to identify which cognitive moves agents can reliably execute." The title names the conversion (human insight to deployable framing); the description explains the how (controlled variation, cognitive move identification) and the output form (deployed as instruction). An agent seeing 5 results for "prompt testing" or "ablation" would use this description to distinguish the note from general prompt engineering advice.
- [Title composability] "since prompt ablation converts human insight into deployable agent framing, we designed the curiosity-prompts experiment..." reads naturally as a sentence fragment. The title functions well as a linkable clause.
- [Claim strength] The claim is specific and contestable. Someone could argue that ablation is overkill (just pick the framing that seems right), that the conversion is too lossy to be useful, or that human insight doesn't reliably translate to agent-executable framings. The note itself acknowledges the conversion is "inherently lossy," which means the title is asserting something non-obvious: that the lossy conversion is still worth doing. The seedling status is also consistent with asserting a claim that needs further evidence.
- [Title-body alignment] The body delivers what the title promises. The 8-step pattern describes the full conversion pipeline from human finding (step 1) through ablation (steps 2-6) to deployment (step 8). The "Why it works" section grounds the mechanism. The "Deployments" section documents two real instances where the conversion produced deployed artifacts. No drift detected.

Overall: CLEAN
===
