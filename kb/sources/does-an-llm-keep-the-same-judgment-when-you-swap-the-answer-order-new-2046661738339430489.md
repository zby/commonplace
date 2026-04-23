---
source: https://x.com/LechMazur/status/2046661738339430489
captured: 2026-04-23T16:14:07.941709+00:00
capture: xdk
type: kb/sources/types/snapshot.md
tags: [x-thread]
status_id: 2046661738339430489
conversation_id: 2046661738339430489
post_count: 13
---

# Thread by @LechMazur

Source post: https://x.com/LechMazur/status/2046661738339430489

## 1. 2026-04-21T18:45:58.000Z https://x.com/LechMazur/status/2046661738339430489

Does an LLM keep the same judgment when you swap the answer order? New LLM Position Bias Benchmark!

Judge models compare two lightly edited versions of the same story twice, with the order swapped. The median model flips in 45% of decisive case pairs. GPT-5.4 is worst at 66%! https://t.co/Ydgkz1TdIe

Links:
- https://x.com/LechMazur/status/2046661738339430489/photo/1

## 2. 2026-04-21T18:45:58.000Z https://x.com/LechMazur/status/2046661740998586793

As LLMs are used more often as graders and preference labelers, judge reliability matters more. This benchmark isolates one basic and frustrating failure mode.

The model-average first-shown pick rate is 63%. GPT-5.4 (high) is the most position-sensitive model in the run. https://t.co/t74VKC84vb

Links:
- https://x.com/LechMazur/status/2046661740998586793/photo/1

## 3. 2026-04-21T18:45:59.000Z https://x.com/LechMazur/status/2046661743888486508

Many models don't just pick the first story more often, they also rate it higher. Average first-position rating bonus is +0.26 on a 1-7 scale. Mistral Large 3 is the outlier in the opposite direction. https://t.co/Wj24qyu4rb

Links:
- https://x.com/LechMazur/status/2046661743888486508/photo/1

## 4. 2026-04-21T18:46:00.000Z https://x.com/LechMazur/status/2046661746635763960

Two failure modes in one chart: directional first-position pull, and order instability even when net first-position lift looks modest. https://t.co/sLkye2c8hO

Links:
- https://x.com/LechMazur/status/2046661746635763960/photo/1

## 5. 2026-04-21T18:46:00.000Z https://x.com/LechMazur/status/2046661749425021090

This chart decomposes each model's two-view outcomes into stable picks, position-following flips, and unresolved cases. Xiaomi MiMo V2 Pro has the lowest flip rate (20%) but only 55% coverage. ByteDance Seed2.0 Pro and DeepSeek V3.2 are the cleanest with solid coverage. https://t.co/98CdOGOZ2Z

Links:
- https://x.com/LechMazur/status/2046661749425021090/photo/1

## 6. 2026-04-21T18:46:01.000Z https://x.com/LechMazur/status/2046661752549671122

Worked example: Case 3 "midnight bakery". Same pair, opposite orders.

https://t.co/MdkgSpGMiV

GPT-5.4 (high) returns &lt;answer&gt;1&lt;/answer&gt; in both prompts. Always the first-shown story, so the underlying winner flips on swap.

Links:
- https://github.com/lechmazur/position_bias#worked-example

## 7. 2026-04-21T18:46:02.000Z https://x.com/LechMazur/status/2046661754722398345

More info, including charts, per-case metrics, raw judge outputs, and the parsed answer dump: https://t.co/253BJNvbqw

Links:
- https://github.com/lechmazur/position_bias/

## 8. 2026-04-21T20:06:44.000Z https://x.com/LechMazur/status/2046682066184740926

@RamonVi25791296 On this chart, yes.

## 9. 2026-04-21T20:18:39.000Z https://x.com/LechMazur/status/2046685064529141971

@StartWaiting Yes
https://t.co/8UaAGb0h97

Links:
- https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2007/2007%20Response%20Order%20Effects%20in%20Dichotomous%20Categorical%20Questions.pdf

## 10. 2026-04-21T20:21:19.000Z https://x.com/LechMazur/status/2046685734313271623

@StartWaiting Also https://t.co/uaqkWWIA1k and https://t.co/0viBr5Fy4s (thanks ChatGPT)

Links:
- https://www.cambridge.org/core/journals/judgment-and-decision-making/article/order-effects-in-the-results-of-song-contests-evidence-from-the-eurovision-and-the-new-wave/C03D0D5AA384362736FE1EB59A75516C
- https://pubmed.ncbi.nlm.nih.gov/7381797/

## 11. 2026-04-21T22:21:21.000Z https://x.com/LechMazur/status/2046715943959532017

@the_internaut Yes, GPT-5.4 annoyed me so much by doing this in my regular-use ChatGPT comparison prompts that I decided to turn it into a benchmark to shame the labs into eliminating this failure mode in future models.

## 12. 2026-04-22T16:10:03.000Z https://x.com/LechMazur/status/2046984888478249124

@JeremyNguyenPhD Humans look less order-biased than the LLM judges.
https://t.co/8UaAGaZJjz

Links:
- https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2007/2007%20Response%20Order%20Effects%20in%20Dichotomous%20Categorical%20Questions.pdf

## 13. 2026-04-22T20:59:53.000Z https://x.com/LechMazur/status/2047057828154577216

@_Suresh2 I haven't tested longer stories. The models have the option to avoid being decisive, which removes one reason length might make a difference.
