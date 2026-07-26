---
source: https://x.com/dexhorthy/status/2081058573556306030
captured: 2026-07-26T07:26:05.314114+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2081058573556306030
conversation_id: 2081058573556306030
post_count: 6
---

# Why Software Factories Fail: Turning the lights back on

Author: @dexhorthy
Post: https://x.com/dexhorthy/status/2081058573556306030
Created: 2026-07-25T16:46:42.000Z

This is part two of Why Software Factories Fail
The talk version of this post is live on youtube: https://www.youtube.com/watch?v=Ib5GBkD555M
Turning the lights back on
In part 1, I went deep on why models can't be trusted to maintain codebase quality over time. Why no amount of harness engineering or tokenmaxxing will solve a model-training and benchmarks problem. Why "model as judge" for code quality doesn't work as well as some folks want to tell you.
For now, the judge is you -- so we're gonna put the code review back.
 
We're gonna embrace that same thing we've been doing since before AI, which is to do a little bit of planning up front, to reduce the odds of a long and difficult review.
We're gonna find leverage, and we're gonna use AI to help with this, across 4 phases:
Product Requirements
System Architecture
Program Design
Vertical Slices
Product review
Everything starts with a product review: a short doc that pins down what we're building and why. The goal is to be able to take two sentences or a long voice note ramble and turn it into something semi-structured.
First, we align on the problem to solve -- the actual user pain, in the user's terms. Second, what success looks like -- what can we read after shipping to decide the thing was worth building. Ideally this is a user outcome like "can do XYZ workflow in less time" or "reaches onboarding milestone ABC earlier". Sometimes it's lower level like an error rate or a latency number, sometimes just "the support tickets about X stop."
We try to keep this pretty grounded in the product space, not the technical. As someone who lives with one foot in the product world and one foot in the tech, I often find myself drifting into the technical details here. When that happens, I try to just jot it down for later phases and get back to what the user actually experiences. If tech decisions are blocking product decisions, then we commit what we have and get into the architecture or do more prototype research on what's feasible
And since most of this is about what the user sees, I don't describe it -- I mock it up. A rough HTML mockup of the actual screen settles an argument that three paragraphs would only prolong.
Here's a real one in progress -- the doc pins down the feature with a JSON outline, then two rough HTML mockups of the actual screens:
https://x.com/dexhorthy/status/2078592010852982977
Of course, not everything gets a product review. A copy tweak, a one-off script, a bug with an obvious repro -- we still just oneshot those straight to the agent. This is for the changes where an agent misunderstanding our intent is expensive.
For this and all docs in the series, we do author-opt-in reviews. If you wanna save time during review, you pick the person who would review the PR, and run through the product/tech specs with them, either async via doc comments (we dogfood humanlayer for this, but you can just as easily do this in github/notion/plannotator/etc).
System architecture
Once the product review is settled, we do system architecture. This is not particularly novel and is something even vibe coders are starting to swear by.
If you wanna save time during review, you pick the person who would review the PR, and run through the product/tech specs with them before you get to the coding part.
In this phase we align on how the services, endpoints, schemas, queues, and stores talk to each other, without getting into the details of program design. To maximize human<>agent communication bandwidth, we make heavy use of visualizations here - for example sequence diagrams:
 
Contract / endpoint shapes:
 
Data models and transformations:
 
Mermaid is fine here but it can sometimes be overkill and sometimes lure you into a false sense that you are aligned. Architecture is fairly high leverage and there's a lot of potentially-bad model tics that you can head off during this phase. But it is insufficient to produce high-quality code. For that we need program design.
Program design
After architecture we do this thing that I think is criminally underemphasized in agentic coding: program design.
Most people assume that once the architecture is right, the model can just cook. You can go ahead and do this, but you might not like what you get back.
But what I see working well is that before anyone (human or agent) writes the implementation, we go a level down from architecture into the shape of code: the types, the method signatures, the program layout, and the call stacks.
The first version of our program design skill sucked. It was hard to read, it was exhausting. We tried mermaid, which has its place, but what we actually love are light visualizations in pseudocode:
Call-stack trees, for any orchestration or control-flow change. Use diff syntax when the interesting part is what's changing:
 
Dillon Mulroy talks about using call graphs as part of his planning process, and I think that's exactly right.
File-tree diffs - so you can stay in touch with the layout of your codebase and where stuff lives
 
Types and method signatures for the key new functions -- the stuff that's too internal for an architecture doc but that an agent might still get wrong
 
None of these take long to produce (the model drafts them, you argue with it), and every one of them is a decision you'd otherwise be making implicitly during code review -- at the most expensive possible time to change your mind.
Vertical slices
Next we love doing what I call "vertical slices" - Matt Pocock and I had a
chat about vertical slices or "tracer bullets" on a live stream back in January 2026 - this is also referred to as - tracer bullets
Models love what I call "horizontal plans" - doing things in stack-order:
Database Migrations
Service Layer
API
Frontend
 
In practice, what this means is there's no real way to "touch" the solution as you're going. You can test things with code, but for almost any feature I've ever built, reading the tests was a start but pulling something up in a browser, or hitting it with curl while I was working was always a frequent part of the workflow.
Before AI, it was rare for anyone to write 2000+ lines of code or even 500 lines of code without checking something along the way.
It took me a while to notice the difference in what I was used to - when I wrote code before AI, I would always start in the middle and work outwards. Vaguely:
Create API contract and serve mock data, test with curl
Create frontend to consume mock data, iterate+polish in browser
Wire API to services layer (services serves mock data/behavior)
Add database migrations, wire services to database
Add a bunch of business logic
Add a bunch of error handling
And I'd be testing/iterating/polishing at each step.
 
If I care about the code a lot or skeptical about the model's ability to do good work in this part of the codebase, I'm reviewing the code at each step too. Checking 100-200 lines and resteering is a lot cheaper
here, I would.Most frontier models won't design a plan like this without human steering, and it's hard to generalize per codebase or even per task, so I prefer to stay in the loop here. Trust me. If I couldoutsource the thinking
30 minutes of planning saves hours of review
And so we have some steps that I would argue that humans need to be in the loop for, if you want to maintain a near-human level of quality without slaving over mountains of slop code trying to clean it up after the fact. (i.e. you actually wanna go fast)
Product Design
System Architecture
Program Design
Vertical Slices
). I would guess the distribution is roughly:Obviously we don't do this whole process for everything we ship (seethe 80/20 rule, below
~40% of tasks get oneshot or oneshot w/ 1-2 rounds of light feedback
for medium tasks, we do product/system design all in one plan document, and don't bother breaking the work into phases
for large things, we do all the steps. we'll skip the product part for things where it doesn't make sense like big refactors.
And in most cases, I'll send off a model to do 1-3 slices at a time, and review the code as I go. It's a lot easier to resteer early on, whether it's the internals or the actual functionality, than to end up on the other side of 2k+ lines of code with no idea what's broken.
You probably feel like you have too many pull requests
You don't have too many PRs. You have too many bad PRs.
We've all reviewed a lot of PRs that needed rework, since long before AI.
But a great PR is a joy to review. You're scrolling through every file, the code is clean, it follows all your decisions/discussions/hard-won opinions about how software should be.
On the other hand, if a Pull Request needs even 20% rework (and that's generous, I'd say most AI oneshot PRs trend closer to 50%), that's both an intellectual burden and an emotional burden on both the submitter and the reviewer. (Even if the submitter is an AI, someone probably kicked off this work or vibe polished the AI result or at the very least, cares about the outcome).
To spare you time (we're almost at the end), I rambled more about this in a side quest:
"where does the time go"
a theory of constraints (2026 edition)
It's easy to be a little bummed by the core thesis here: "for now we're stuck reading the code".
I was pretty excited for a world where we could just ask for things and let the models cook and not read the code and get beautiful production software that evolves over time and doesn't go to shit.
But what I've done my best to lay out here are nothing but constraints. Models are good at some things, not so good at others. How do you optimize your process in light of those constraints?
Models are good at some things, not so good at others. How do you optimize your process in light of those constraints?
It is possible you are too busy trying to move 10-100x faster and trying to convince yourself code quality doesn't matter any more, when you could embrace the constraints and move 2-3x faster, safely.
My kind of closing advice here is basically:
Learn the constraints well, develop intuition by working with models a lot
Optimize systems within the arena of these constraints
Seek leverage
Read the dang code
That's it. If you wanna stay for the pitch, keep scrolling I guess. I hope this helps you avoid disaster or at least that you had fun watching some cute little animations.
Thanks for reading
  -dex
PS We're obsessed with this
We're building humanlayer.com, an agentic IDE and collaboration platform to help you move 2-3x faster while maintaining a human (or pretty-dang-close-to-human) level of code quality.
We're building towards two ideas: "building blocks for your software factory" and "better verifiers for software maintainability" (perhaps better models even).
HumanLayer is free for small teams of up to 3 people, and if you want help getting started, you can come hang in our discord or drop us a line at founders@humanlayer.dev
A quick shout out to @calvinfo for inspiration, to my cofounder @0xBlacklight, to @swyx and the team at @aiDotEngineer for giving me an arena to explore these ideas, and to all our incredible customers, investors, friends, and family cheering us on.
If you wanna learn more, I basically won't shut up about this, so you can find all the links from this post as well as a few other projections of the material into podcasts, long form whiteboard, etc, below.
PPS Other resources
Podcasts and Articles:
Dex and Gergely talk context engineering and software factories on The Pragmatic Engineer - July 2026
Dex and Matt Pocock talk evergreen ai coding advice (and ralph loops) - January 2026
AI That Works Episodes:
Benchmarks prove nothing
Product Specs for AI Coding
Learning Tests for better backpressure
Applying 12-factor agents principles to AI coding
Links from this post:
Why Software Factories Fail keynote — AI Engineer World's Fair 2026
StrongDM's lights-off software factory
OpenAI: Harness Engineering (Feb 2026)
Ryan Lopopolo on Symphony (talk, Apr 2026)
Mario at AI Engineer Europe: "Building pi in a world of slop"
FT: Amazon outages from coding-agent mishaps
Matt Pocock: codebases falling apart
Faros AI: the AI acceleration whiplash report
Advanced Context Engineering for Coding Agents (talk 8/25)
No Vibes Allowed (talk 11/25)
Everything We Got Wrong About RPI (talk 3/26)
Awesome-RLVR - Reinforcement Learning resources
Advanced Context Engineering for Coding Agents (write-up)
12-Factor Agents
Addy Osmani on vibe-coding vs. maintenance
NATO Software Engineering Conference, 1968
DoD DevSecOps Reference Design (PDF)
Ramp's coding-agent platform
Stripe: Minions, one-shot end-to-end coding agents
WorkOS: Project Horizon
Brex (Latent Space)
Dan Shapiro: the five levels to the software factory
Simon Willison on StrongDM's software factory
"Boil the ocean"
Shotgun surgery (refactoring.guru)
John Ousterhout — A Philosophy of Software Design
Robert C. Martin — Clean Code
Martin Fowler — Refactoring
aider
cline
codebuff
SWE-Agent paper (2024)
OpenAI Codex talk (Nov)
Calvin French-Owen — AI Council talk
SWE-bench Multilingual (dataset)
AIE Worlds Fair 2026 - The Great Loops Debate ("the hype is outrunning the discipline")
SWE-Marathon (Abundant AI)
DeepSWE (Datacurve)
Frontier Code (Cognition)
Mutation testing (Wikipedia)
Dillon Mulroy on call graphs in planning
Dex × Matt Pocock: vertical slices / tracer bullets (livestream, Jan 2026)
"The hard work of thinking can't be outsourced" (Jake Nations)
