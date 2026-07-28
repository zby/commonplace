---
source: https://x.com/frgx/status/2081739292859421118
captured: 2026-07-28T11:52:12.808321+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
tags: [x-thread]
status_id: 2081739292859421118
conversation_id: 2081739292859421118
post_count: 9
---

# Thread by @frgx

Source post: https://x.com/frgx/status/2081739292859421118

## 1. 2026-07-27T13:51:38.000Z https://x.com/frgx/status/2081739292859421118

1/ Last year, the Figma security team made the bet that agents could review every single line of code we ship, _and_ that developers would actually trust the findings. Today no PR merges at Figma without an agent security review. Here's what we learned getting there.

## 2. 2026-07-27T13:51:39.000Z https://x.com/frgx/status/2081739294000230468

2/ Like any security audit, a key requirement was trust. High noise reviewers get ignored. Week one, only 4 of 27 findings were real. We held the tool back from developers entirely until we could look them in the eye and say "this is worth your time."

## 3. 2026-07-27T13:51:39.000Z https://x.com/frgx/status/2081739295245869168

3/ Improving precision forced us to write down generic precedents for our agent. 68 precedents later, we realized we'd written down our threat model; something that would help onboard new hires. What we thought was just some tweaking turned out to be an asset

## 4. 2026-07-27T13:51:39.000Z https://x.com/frgx/status/2081739296441331883

4/ Now, that artifact powers agent review, repo-wide auditing, and secure code generation. Years of institutional knowledge that lived in people's heads and old incident docs, finally checked in for both humans and agents to use and update over time, tested daily!

## 5. 2026-07-27T13:51:40.000Z https://x.com/frgx/status/2081739297980559775

5/ Our first full-repo audit surfaced 100+ latent vulnerabilities, including two criticals that traditional tooling, human pentests and reviews never saw. Ten-year-old code. That's not just about models being clever  but the leverage of improving precision and recall

## 6. 2026-07-27T13:51:40.000Z https://x.com/frgx/status/2081739299247231123

6/ Bug bounty researchers are among our most valuable security partners. 46 of the 66 bugs in our eval corpus came from our bug bounty. A strong program with great researchers matters more in the AI era, not less.

https://t.co/qJvcVNc5s5

Links:
- https://x.com/frgx/status/2049988380960907552

## 7. 2026-07-27T13:51:40.000Z https://x.com/frgx/status/2081739300715344178

7/ Our security engineers went from triaging one bug at a time to writing the policy that catches hundreds and prevents hundreds more. And the agents to auto fix! You still craft, judgment, but have dramatically more leverage. That's the version of this future I am excited for

## 8. 2026-07-27T13:51:41.000Z https://x.com/frgx/status/2081739302212718764

8/ Enormous credit to Rohan, @sl1nki3283 and Liam for the great work here. If you are interested in working with them, we are hiring! 🙂 

https://t.co/rVSvUDf3gs

Links:
- https://www.figma.com/blog/how-figma-stays-ahead-of-vulnerabilities-with-agents/

## 9. 2026-07-28T00:30:09.000Z https://x.com/frgx/status/2081899979216670904

@ph3t_ aah no; we don't have a lot of secondary repos. that would be interesting; what challenges did you hit? 

and engineers use claude as well as codex; as does our reviewer (we run both anthropic and openai models with the reviewer!)
