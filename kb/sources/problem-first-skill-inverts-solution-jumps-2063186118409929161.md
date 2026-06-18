---
source: https://x.com/nurijanian/status/2063186118409929161
captured: 2026-06-17T09:08:07.099475+00:00
capture: xdk
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2063186118409929161
conversation_id: 2063186118409929161
post_count: 1
---

# /problem-first: a simple skill to invert bad ideas

Author: @nurijanian
Post: https://x.com/nurijanian/status/2063186118409929161
Created: 2026-06-06T09:07:57.000Z

If you're a PM who walked in on day one to find a roadmap full of solutions the team wants you to ship, you know the bad feeling already. You can't push back without looking obstructionist, and you can't say yes without losing your conviction. The move that gets you out: treat every solution someone hands you as a compressed, imprecise confession of a problem the team senses but hasn't articulated, then decompress it back into the problem underneath.
 
The team handed you "we need a new notification system." Your job is to decompress that into the problem underneath, then check whether the solution they picked is one of three reasonable responses to that problem, or whether they jumped to the wrong one entirely.
This is the most reliable move I've learned as a PM walking into a roadmap that's already been written. It also runs in reverse for the opposite PM problem, which is when you're the one with too many half-baked ideas and no way to triage them. Same skill, both directions.
Invert, invert, always invert
Most discovery advice says to stop, do research first, and come back when you have a problem statement. The people giving that advice assume the team will let you slow them down. In real life, teams holding solutions have political and emotional momentum behind those solutions. Telling them to halt and do research is how you burn your influence on day 30.
Instead, you use the solution as the starting point for the research. You treat the proposed solution as a research artifact: evidence of a real pain someone on the team felt, compressed into an answer. Your job is to decompress it back into the underlying problem so the team can see what they were actually responding to.
That gives you a different posture in front of the prebaked roadmap. Instead of standing in front of it blocking it, you're digging underneath it to find the problem it was meant to solve.
/problem-first
Let me walk you through a real example. Team says: "we need to build a new notification system."
The `problem-first` skill runs in one AI call and returns eight sections. This is what comes back:
Solution-jumping diagnosis. What signal did the team detect that made them propose this? Probably: users miss things, support tickets about lost context, complaints that the product doesn't tell them when stuff changes.
Underlying problem. Users can't see when state changes inside the product, and the gap in visibility erodes their trust that the product is doing anything on their behalf.
Assumption challenges. Each with risk-if-wrong and a validation test. Examples:
Assumption: users want more notifications. Risk if wrong: we add noise, adoption drops. Validation: pull notification engagement data from current system.
Assumption: the delivery mechanism is broken. Risk if wrong: we rebuild plumbing and the problem stays. Validation: read the last 50 support tickets tagged "missed update."
Assumption: users want real-time push. Risk if wrong: we ship interruption and they turn it off. Validation: ask in the next 5 user interviews.
Problem statement. Users who rely on the product for time-sensitive decisions struggle to know when their context has changed, because the product doesn't surface state changes proactively, which leads to lost trust and reactive support load. Success would mean users discover relevant changes without checking manually.
Three alternative framings. Three framings that surface the jump most teams made at this stage:
Framing A: users don't know when context changed. Solution space: state-change indicators, activity feeds.
Framing B: users don't trust the system is working. Solution space: status visibility, audit trails, confidence signals.
Framing C: users want to delegate watching to the product. Solution space: subscriptions, smart digests, agent-driven alerts.
Notice none of those are "a notification system" in the way the team meant it. The first framing points to a UI state pattern, the second to a trust-and-status problem, and the third is closer to an agent. Each one would lead to a different build, but the team's brief had folded all three into a single feature spec. That's the move you want to catch before it becomes a quarter of engineering time.
Three sections in there that a human PM under pressure reliably skips: the assumption challenges with risk and validation, the three alternative framings, and the draft message. Skip the framings, and you commit to one solution before seeing the two equally viable alternatives that would have led to different builds. Skip the message, and you end up in an awkward Monday standup where you've quietly stopped working on the roadmap and nobody on the team knows why.
The reverse use, for the ideas person
This is the version that helped me most personally. I'm the kind of PM who has a lot of ideas, so my notes fill up faster than my conviction can keep pace with. Lots of generation, lousy triage.
I started running the skill in reverse. You feed in your own idea, ask it to extract the problem you think it's solving, and check the evidence status field.
Most ideas die at "Evidence Status: none."
I ran this across a backlog of about 50 ideas. 90% died at evidence status. 3-5 survived with real problems underneath. 1 got pitched the following week with the evidence pack already assembled. 
Running this triage protocol finally unblocked the part of me that has lots of ideas. Yes, agents can build anything these days, but you still need to spend time on each idea, even just to write a spec for /goal to execute (and usually it takes more work to babysit).
Being more disciplined about generating ideas doesn't help me, and probably doesn't help other PMs wired this way. In my experience, the real constraint is triage capacity, not idea generation. When you run the skill, you get a triage protocol that addresses the actual bottleneck.
Why this runs better on AI than in your head
You can do this mental work without AI. People have been doing it for decades, after all. A human PM with an hour and a quiet office can produce most of these sections, but under time pressure most PMs skip the hard ones. They skip the assumption challenges with risk and validation. They skip the three alternative framings. They definitely skip the draft message, which is why so many new PMs end up either quietly executing without conviction or making the team feel ambushed.
Running this in AI ensures every section runs every time, because you have to complete all eight outputs before the run produces anything you can use.
Running the skill takes about 90 seconds and produces all eight sections. Writing the same output by hand takes about an hour, and tends to miss the harder sections.
Where this skill lives
`problem-first` is one of the 200+ skills inside PM OS, the Product Manager's AI Operating System. It runs in Claude Code, Cowork or Cursor on top of your company context files, so the assumption challenges and validation plans come back grounded in your product, your users, and your real constraints, instead of generic PM advice that could have come from any blog post.
 
You don't have to assemble any of it. PM OS wires `problem-first` into the broader operating layer alongside workflows for strategy, research, decisions, stakeholder work, and measurement. 
If you want the full system, it's here.
