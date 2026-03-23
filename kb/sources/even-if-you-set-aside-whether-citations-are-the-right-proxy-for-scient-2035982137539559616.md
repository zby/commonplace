---
source: https://x.com/koylanai/status/2035982137539559616
captured: 2026-03-23T08:06:15.726975+00:00
capture: xdk
type: x-post
status_id: 2035982137539559616
conversation_id: 2035982137539559616
post_count: 1
---

# Post by @koylanai

Source post: https://x.com/koylanai/status/2035982137539559616

## 1. 2026-03-23T07:29:02.000Z https://x.com/koylanai/status/2035982137539559616

Even if you set aside whether citations are the right proxy for scientific taste and there are real reasons to question that (Hume's "joint verdict of qualified judges" breaks down when the signal is popularity), there's still valuable learning.

Scoring a single output in open-ended tasks with LLMs is so unreliable (especially when there's no verifiable ground truth), but comparing two outputs is natural and more consistent. The paper uses this by having the policy generate a group of candidates, running round-robin pairwise comparisons via a reward model, and using normalized win rate as the training signal.

1. Pairwise comparison avoids the absolute scoring problem. You don't need to define what a "4 out of 5" means. You just need to reliably say "A is better than B." 

2. The round-robin tournament creates a rank ordering from binary signals. Each candidate competes against every other candidate. Win rate emerges as a scalar reward without ever requiring an absolute score. This converts an open-ended evaluation problem into something GRPO can optimize.

The paper implements this through RL training, but the pattern works without it. I'm noticing that pairwise comparison pattern is powerful and underused in context engineering. Absolute scoring is unreliable in LLM-as-judge variance. Instead of scoring candidate outputs 1-5, we can generate N candidates, run pairwise comparisons with the evaluator, and rank by win rate.

Links:
- https://x.com/koylanai/status/2035982137539559616/photo/1
- https://twitter.com/askalphaxiv/status/2035614942812950906
