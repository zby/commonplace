---
source: https://x.com/ashpreetbedi/status/2084301728363462919
description: "Agno walkthrough deriving probes from an agent specification and usage traces, then editing instructions, tools, and parameters until the probes pass"
captured: 2026-08-03T18:05:02.311358+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2084301728363462919
conversation_id: 2084301728363462919
post_count: 1
---

# How to Recursively Improve Your Agents

Author: @ashpreetbedi
Post: https://x.com/ashpreetbedi/status/2084301728363462919
Created: 2026-08-03T15:33:51.000Z

Today I'm going to show you how to recursively improve your agents. We'll build an agent that starts at 7/10, then run a recursive auto-improvement loop until every probe passes.
Here's how it works: my coding agent reads the agent's instructions and mines its usage data to derive probes. Then it runs those probes against the live agent, reviews the logs, and edits the agent until each probe passes. 
Here's what the end result looks like:
 
Not RSI
Recursive self-improvement (RSI) has a specific meaning in the community. 1) the system improves itself, 2) the improvements target its ability to improve, and 3) the gains compound. RSI is a divergent process. Here, one AI improves another. A coding agent edits a target agent's instructions, tools, and parameters. Recursive auto-improvement (RAI) is a convergent process: it pulls the agent toward a fixed point, i.e. its own spec. For production software, convergent is exactly what we want.
Try it yourself
To build an auto-improvement loop, you need a system that is set up for it.
Your coding agent needs to be able to:
Query the live system via an API. So it can test the improvements against the live agent.
Watch the logs. So it has full visibility into the agent's trajectory. Every tool call, error, and debug message is available to the coding agent.
Make code changes and test the updates. So it can fix, improve, and extend the agent to pass the probes.
Mine the usage data. So it can derive probes from real usage patterns. Questions, answers, and fumbles help it understand where the agent is struggling.
Look up framework information. So it can reliably make updates by tuning parameters.
This "system" is exactly what I've spent the last year building, and the results are MARVELOUS.
If you're an agent builder, I highly recommend you follow along. Even if you're not an Agno user, the coding-agent-driven paradigm is a see it to believe it experience. We're going to do everything from setting up the platform, to creating agents, to improving them using coding agents.
Let's start by setting up our platform first.
Set up your platform
Step 1: Start up your coding agent. I'm using claude code with --dangerously-skip-permissions.
 
Step 2: Create your agent platform.
Make sure docker is installed and running.
Export your OpenAI API key using `export OPENAI_API_KEY=...`
Get your prompt from os.agno.com and give it to your coding agent.
 
Once the platform is up, connect to the AgentOS UI (where you got the prompt from) and play around before creating the agent we'll use for auto-improvement.
Create the agent to improve
The setup platform skill ends with recommending an agent called Radar, go along with it.
 
Radar is a great example for the auto-improvement loop, because its spec is dense with rules a judge can check mechanically:
Max 5 items, one line each, every item with a source link.
No hype adjectives.
Keeps a ledger of items already reported, so briefs don't repeat.
Optional: Use it before you improve it
The auto-improvement loop's strongest probes come from usage data. So before improving an agent, I just... use it a couple of times. Asked for briefs. Asked follow-ups. Asked adversarial questions.
The usage data is stored in Postgres as sessions. When the improvement loop runs, it mines this usage data to derive probes: recurring shapes, visible fumbles, out-of-scope asks.
Note: you might run into rate limit errors on the Parallel MCP, to fix those, get a key from platform.parallel.ai and set it in the .env file.
Run the improvement loop
Now coming to the main event: the auto-improvement loop. I'm going to cd into the platform directory and open another coding agent. We'll cd in so the coding agent can pick up the skills and I can run them using a slash command.
/improve-agent
 
The loop runs for ~25 minutes, I've trimmed (and sped up) the video aggressively to condense it into 2 minutes. I rarely deploy an agent without running this loop first.
My favorite version of this is the overnight run. I kick off the loop with 300-500 probes then go to bed. The loop works through rare edge cases, odd phrasings, failures that only show up once in a hundred runs. My coding agent works through them while I sleep, fixing every bug it can find.
You can then ask the agent to provide a report. Mine looks like this (because it has access to my internal design system):
 
Here's how it works
The coding agent reads Radar's instructions and mines the sessions to build a set of probes: golden path, edge cases, tool selection, adversarial. For each probe it writes a one-line expected behavior, drawn from the spec. Then it runs them against the live agent, reads the tool calls, errors, and debug messages from the container logs, and judges every response.
For every failure it picks one lever to change: tighten a rule, add a rule, swap a tool. It edits the agent code in agents/radar.py, restarts, and re-runs only what failed. Most fixes are one sentence or one parameter change.
Note: you can also turn the failures into evals :)
Wrapping up
Here's the new agent development lifecycle, managed entirely using coding agents:
 
Thanks for reading! This article is also available on my blog.
Ashpreet
