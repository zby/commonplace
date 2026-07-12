---
source: https://x.com/ashpreetbedi/status/2048817143974613089
captured: 2026-04-27T18:29:20.288781+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
status_id: 2048817143974613089
conversation_id: 2048817143974613089
post_count: 1
---

# Context providers: the missing layer between agents and tools

Author: @ashpreetbedi
Post: https://x.com/ashpreetbedi/status/2048817143974613089
Created: 2026-04-27T17:30:46.000Z

If you've built an agent with a decent number of tools, you've hit the three walls:
Context pollution from too many tools
Degrading performance from overlapping scopes 
The main agent forgets its job because its context is all tool instructions
If you disagree, try giving an agent access to Slack, Google Drive, and Notion at the same time. Let me know if search works.
I've been testing a new protocol that fixes these issues, and the early results are good enough to share broadly.
The three walls
Context pollution. Every tool takes up precious context. 

Schemas, descriptions, example usage, all of it lands in the system prompt. A Slack toolkit is 8 to 12 tools. Gmail is 6 to 10. Calendar another 6. Drive, GitHub, your CRM, the web. You're at 50 tools before adding anything custom. Past 20, models start hallucinating tools that don't exist or calling tools with the wrong shape.
Blurry scopes don't compose. Two tools both take a workspace argument: one is Slack's, one is Google's. Search in one MCP collides with search in another. send_message could be Slack, email, or your CRM. 

The agent picks wrong half the time, and no naming convention fixes it because the same word legitimately means different things in different sources. The minute you compose tools from sources you don't control (MCP servers, third-party SDKs, other teams), you get overlap, and the model has no reliable way to disambiguate.
Tool-use logic lives with the main agent. This is the deepest wall, and the one that causes the most issues. For an agent to use Slack well, the system prompt has to explain Slack: look up the user ID before you DM them, resolve a channel name to an ID before you post. That's hundreds of tokens of Slack-specific guidance. Now do that for Gmail. For Calendar. 

The system prompt becomes the union of every API's quirks. Every turn carries every rule, even when the user just asked about Slack. The main agent is stuck reasoning about both the user's question and the mechanics of every API it might call. Adding a source means editing the prompt and praying nothing else regresses.
The missing layer
Today the canonical agent shape is: Agent <- Tools
or, with MCP: Agent <- MCP server <- Tools
or, with Skills: Agent <- Skill instructions <- Tools
In all cases the agent sees the raw tool surface of every source. Every Slack tool, every Drive tool, every CRM tool. The agent's prompt has to contain how to use every one of them.
The shape I've been testing puts a thin layer in between:
Agent <-> ContextProvider
Each ContextProvider wraps one source (e.g. Slack, FileSystem, Drive)
To the calling agent, it exposes exactly two tools:
query_<source>(question) for natural-language reads
update_<source>(instruction) for natural-language writes
That's it. The main agent doesn't see Slack's twelve tools. It sees query_slack and update_slack. It doesn't see Drive's quirks. It sees query_drive. Add ten more sources and the agent's tool surface stays linear at max 2N.
Behind each tool is a sub-agent scoped to that one source. The sub-agent owns the source's tools, the source's quirks, the lookup-before-write patterns, the pagination weirdness. It runs in its own context, returns an answer, and the main agent gets a clean result.
 
The agent sees four tools: query_slack, query_drive, query_crm, update_crm. 
What about Skills?
Skills are a great attempt at wall 3. A skill packages task-specific instructions ("here's how to use Slack") into a module that the model loads when relevant, instead of carrying it in the system prompt full-time.
Skills move task knowledge out of the always-on prompt and into something more conditional. But the Slack tools will still land on the agent after the skill is invoked. Load 2 skills and search will still collide. In fact there's a higher chance of conflicting skills messing up your agent without you even realizing.
ContextProvider + skills work better together. 
A Slack ContextProvider's sub-agent can itself load a Slack skill, and that's where the skill does its best work, in the context of the thing actually executing against Slack, not in the main agent that just wanted an answer.
The split is roughly: skills compress how to do a task. ContextProvider hides that there's a task until the main agent decides to delegate one.
Examples
A full set of cookbooks live in cookbook/12_context. 
Sources covered out of the box. 
Filesystem (00), database (04), Slack (05), Google Drive (07), GitHub (12), and web via Exa or Parallel, direct SDK or MCP endpoint (01, 02, 03, 11). Every provider follows the same query_<id> / update_<id> shape.
Read/write split with real security. 
04_database_read_write.py spins up a SQLite DB and has the agent insert a contact, read it back, and verify with direct SQL. Read and write go through separate sub-agents with separate engines. 12_github.py does the same shape over a real repo: reads through a read-only sub-agent on a clone, writes through a sub-agent that operates on a per-session worktree on a <prefix>/<task> branch and ends in a PR. The agent cannot push to the main branch, but can read from it.
Compositional multi-source. 
09_web_plus_slack.py is the shape flat tool layouts can't do without orchestration code. The agent pulls topics from a Slack channel, runs a per-topic web search, and returns a briefing tying each internal thread to an external reference. 
MCP wrapper. 
06_mcp_server.py wraps any MCP server (stdio or HTTP) as a single query_<id> tool. The sub-agent's instructions are built from the server's list_tools() response at connect time, so the calling agent never sees stale tool docs. This is the move that collapses a 50-tool MCP server to 1 tool from the main agent's view.
Surprises and open questions
A few interesting observations.
Sub-agents are cheaper than expected. I assumed the extra hops would dominate. They don't. The main agent's context is so much smaller that its calls are faster and better, and the sub-agent only fires on turns that touch its source. On Scout's workload, total tokens are roughly flat at low source counts and improve as the source count grows. Wall-clock latency drops at every source count I've measured.
The main agent's prompt got significantly smaller. I expected to need a bit of orchestration logic, but nope. With a uniform surface, the routing rules collapse to "pick the right query_<source>". 

gpt-5.4 just works out of the box, and needs zero guidance on how to use a source. This is the kind of magic you need to see to really understand why i'm so excited about this pattern.
Composition just works. Two providers can read each other in the same turn (query_slack for the discussion, query_drive for the doc) and the main agent writes the synthesis. Multiple sources work much better together.
Adding a source is one line. Removing one is one line. Swapping a backend (Exa to Parallel for the web provider) stays inside the provider. The agent doesn't notice. And sources just work, because I don't need to update the agent's prompt on how to use them.
A few things I'm still working through.
How thin can the main agent's prompt get? I've been hill-climbing this with evals and seeing how far I can push it. Is there a world where I give zero instructions at all?
Caching across calls in a session. The same query_<source>("who's on the X channel") shouldn't re-do the work two turns later.
Per-user authentication that survives the hop. Partially solved (Scout passes user_id, session_id, metadata, and dependencies through to the sub-agent). More to do for OAuth-shaped sources.
When to expose underlying tools instead. Some sources benefit from the agent driving the tool calls directly, usually when the source is small enough that the schema cost is low and the agent's reasoning is the limiting factor. The protocol has a mode for this. I'm still figuring out where the line sits.
Links:
Examples
Scout
