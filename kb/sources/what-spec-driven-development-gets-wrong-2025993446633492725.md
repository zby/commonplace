---
source: https://x.com/augmentcode/status/2025993446633492725
captured: 2026-03-10T13:09:52.885228+00:00
capture: xdk
type: x-article
status_id: 2025993446633492725
conversation_id: 2025993446633492725
post_count: 1
---

# What spec-driven development gets wrong

Author: @augmentcode
Post: https://x.com/augmentcode/status/2025993446633492725
Created: 2026-02-23T17:57:33.000Z

The only documentation you can 100% trust is the code itself.
Design docs, changelogs, READMEs, architecture diagrams, onboarding wikis. Every one of these is almost instantly out of date.
Keeping a written artifact in sync with a changing system is a continuous cost, and engineers are built for bursts. Write the doc, ship the feature, move on. The updating part is invisible work that competes with everything else on a given day, and it loses that competition almost every time. We've tried process. We've tried tooling. We've tried making it a team value. None of it has worked because we keep asking humans to do a thing that humans reliably won't do.
This is where spec-driven development usually fails. The idea is sound: when you're working with coding agents, write down what you want before you turn them loose. Obviously better than pasting prompts into a chat window and crossing your fingers.
But a spec is a document. And we just established what happens to documents.
The difference is what's at stake. A stale design doc misleads the next engineer who happens to read it. A stale spec misleads agents that don't know any better. They'll execute a plan that no longer matches reality, confidently, and they won't flag that anything is wrong.
So when we started building Intent, the question we kept circling was: what if the spec wasn't something you maintained? What if it maintained itself?
Here's what we landed on.
The spec isn't a human artifact or an agent artifact. Both sides read from it and write to it.
You describe what you want to build. A coordinator agent drafts a spec, breaks it into tasks. You look at it, edit it, approve before anything runs. Once agents start working, they write updates back: what they found, what changed, what constraints they hit that weren't in the plan. You can pause at any point, rewrite part of the spec, and agents pick up from the new state.
Think about what happens when you hand a task to a good junior engineer. You give them the ticket, they go off and work on it, and when they discover the API doesn't support pagination the way the ticket assumed, they update the ticket themselves. They don't wait for you to notice something is off. They don't just build the wrong thing. They come back and say: "this assumption was wrong, here's what I did instead, here's why." You review their update and either approve or push back.
That's the relationship we wanted between the developer and the spec. The ticket stays honest because both sides are maintaining it.
The junior engineer analogy goes further than you'd think. A good junior doesn't narrate every line of code. They surface the decisions that change direction: "I found an existing auth context, so I wired into that instead of creating a new one." That's the signal. That's what you want from agents too. Getting this granularity right turns out to be one of the genuinely interesting design problems in the system. Too much and the spec becomes noise you learn to ignore. Too little and you're back to guessing what happened.
Here's what a task actually looks like. You write: "Add a dark mode toggle to the settings page that respects system preferences." The coordinator reads your codebase, drafts a spec with three subtasks: add the toggle component, wire it to a preference store, update the CSS variables.
You scan it, notice it missed the bit about persisting the choice across sessions, and add a line.
You approve.
Agents pick up the work.
Fifteen minutes later, one of them has updated the spec: "Found an existing theme context provider in the codebase. Wired into that instead of creating a new store."
You review the code change (clearly grouped by agent and task).
The spec now reflects what was actually built, not what was originally planned. And nobody had to remember to update it.
Every documentation-first initiative in software has failed for the same reason: it asked developers to do continuous maintenance work that nobody sees and nobody rewards.
SDD will fail for the same reason unless the agents do their share of the maintenance.
If agents can write code, they can update the plan. Let them.
