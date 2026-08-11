---
source: https://x.com/henrytdowling/status/2054246434506199529
description: "Opinionated agent-memory design across retrieval, injection policy, and organization-scoped retention"
captured: 2026-08-11T10:29:52.213702+00:00
capture: xdk
genre: conceptual-essay
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2054246434506199529
conversation_id: 2054246434506199529
post_count: 1
---

# Three Dimensions That Matter To An Agent Memory Store

Author: @henrytdowling
Post: https://x.com/henrytdowling/status/2054246434506199529
Created: 2026-05-12T17:04:50.000Z

There are a lot of different approaches to building memory for coding agents (see here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, here, and here for some example implementations.)
In this article, I’m going to give my opinionated stance on how you should approach this problem, examining three key decisions that memory builders need to make. This article is kinda a grab bag.
TLDR:
Use semantic retrieval and grep to retrieve memories over some form of structured knowledge base, and do not use knowledge graphs. Generally, the agent should request memories rather than force-feeding them. You should store organization-specific knowledge in your memory store- not personal preferences and not information generally available on the internet.
Dimension 1: Retrieval
How do we structure the data so that it’s easy to retrieve? Here are the most common approaches:
Semantic retrieval (specifically, vector embeddings) is the most common naive approach that people use to build agent memory. Here’s a thread talking about common patterns. It’s great and you should incorporate it.
Grep over filesystem is also much-talked-about (here’s an example, here’s the supermemory founder talking about it, here’s a vercel blog about this). It’s great and you should incorporate it. This feels spiritually the most “bitter-lesson-pilled” (hence the refrain “filesystem + grep is all you need”).
Knowledge graphs are a popular and enticing approach. Mem0’s entity linking is an example of this approach. Shortly I will argue that you should not incorporate a knowledge graph into your memory system.
LLM Wiki (source) is the idea of structuring your codebase/organization’s memory as a collection of documents that an AI continually maintains / cleans up. It’s very promising and you should use it. Here’s a more formal academic paper advocating for this approach.
Subagent summary- take a large piece of stored text and summarizing it with several smaller subagents in parallel. This paper on “agentic mapreduce” is an example.
Q: Which ones should I use?
A: All of the above except knowledge graphs.
If you’re building on the Claude Agent SDK your agent will have grep and subagent summary out of the box.
Here’s a summary of why it’s necessary to include each of the above four components:
Grep over filesystem is the gold standard for agent memory. It plays to what agents are already posttrained to be great at- writing bash commands, understanding filesystems, and iteratively using tools. E.g. “why did we decide to bump the rate limit on our API gateway” -> `grep -n "rate" src/scheduler/gateway/server.py | head -20`
Semantic retrieval is helpful to agents looking for answers to semantic questions that aren’t easy to grep for. E.g. “where do we constrain our users’ ability to configure their pipeline?”
Curated LLM Wiki -> Essentially indexes your filesystem to make grepping easier. E.g. you don’t want to have many redundant entries for “caching strategy” in your filesystem. Additionally allows the memory to evolve based on your organization’s needs over time.
Agentic Mapreduce -> Useful for “summary” queries. E.g. what are the most common ways our past 1000 customers have churned?
Q: Why shouldn’t I use a knowledge graph?
First, I’ll claim that you shouldn’t use a knowledge graph as your primary way of representing memory.
 
Most knowledge graph implementations store facts, and memory != facts. Here’s an illustrative example: Suppose my friend Joy texted me “I broke up with Dylan…”
The way a knowledge graph would update in response to this information is to...
Change the edge between Joy and Dylan from “couple” to “exes”
Maybe write to the “Joy” / “Dylan” nodes something to the effect of “recently had a breakup”
But there’s so much semantic information in that text that wasn’t captured! The “...” indicates that there’s probably some spicy tea. The fact that the text was short, and came out of the blue indicates that maybe she had been expecting it or knows that I had been expecting it. Sam Whitmore makes this point very convincingly in her talk on memory last year (at the 2:05 mark)
Second, I’ll claim that even in addition to another way of representing memory (e.g. a document store), a knowledge graph is still not worth using in your product. Here’s some empirical evidence: Mem0 tried graph memory and was only able to squeeze out a 2% performance gain on benchmarks. This paper tried it and found that while token costs go down, so does performance. Similarly, in this paper, some researchers found that between a simple retrieval-based memory, and a simple retrieval-based memory augmented with a graph, the retrieval-based memory actually performed worse.
Dimension 2: Memory Injection Policy
Should the agent ask for things to be added to its memory, or should things be added to the agent’s memory proactively?
Pull the agent asks for memory based on a query (via semantic search, asking a subagent to summarize, etc), and then receives a result. Eg Letta
Push relevant memories are proactively added to the agent’s context without any explicit request on the part of the agent. Eg most 2023-era RAG systems
 
Q: We should never push to memory, because pushing irrelevant stuff into memory will cause context rot, right?
A: I don’t think these are quite the same thing! LLMs are able to do great things under long context windows- consider that *coding agents* routinely hit 1M context and they are the main workhorse for AI productivity.
So really, the problem is that if you add *irrelevant* context, LLM performance decreases. But the success of coding agents suggests to us that it’s totally possible to do great work with relevant context, if you’re smart.
Q: Okay, that’s a neat fun fact, but why would I ever want to push? That’s not very bitter-lesson-pilled! Just let the agent decide.
Yes, generally it’s better to let the coding agent manage its own resources! But you really do have to push sometimes. Here’s an example of a time where you’d want to push memory:
The user has previously mentioned that `curl` isn’t working on their local network, and they need to use `wget` instead
The agent tries to use `curl`.
No reasonable agent would think to check whether there have been historical problems with `curl` before using it. But also, clearly a desideratum of any reasonable memory system would be that the agent is able to remember this fact. So, this fact needs to be pushed to the agent. This example comes from a friend of mine, who presents an extremely interesting version of the “push” approach here.
Also, I would push back on “push” being inherently not bitter-lesson-pilled. What if we RL’d a memory injector in tandem with an agent on a task? That would be very bitter-lesson-pilled.
A few additional thoughts on push versus pull: (1) if you are pushing memory, you should probably push as a user message rather than as part of the system prompt, so as to save money on prompt caching (2) instead of pushing a full “memory” to an agent’s context window, it may be a better idea to push a lightweight “title” of the memory, and to allow the agent to decide whether or not to double click into any of the memories based on their title- analogous to how skills work.
Dimension 3: What to store: Transcripts vs commentary on transcripts vs LLM wiki
A good general policy is: “Store everything that you would consider `company knowledge`”.
Here are some things that many peope like to put in their memory store:
Context from various knowledge resources (eg Slack, Granola)
Their codebase
Things that the agent decides to write to memory (eg a persistent “notebook”)
Past conversation transcripts
Here are some other, less talked about things that you might consider adding to memory:
Q: Should you include your collaborator’s conversation transcripts
A: Yes, if they’ll let you! Here’s a post that explains the benefits of this in greater detail- tldr you can make your agents 48% more efficient on a team of 2 by sharing transcripts in memory.
Q: Should you include facts about the world in your agent’s memory store? Eg: should there be an entry for “potato”? Seems like that would be a useful thing to remember, but also it’s already in the weights of any llm.
A: Sometimes! Here’s an analogy that might be helpful: imagine that wikipedia is what’s outside of your agent’s memory, and your company has an internal wiki. If your organization has a specific insight on ACME corp (eg “they’re our number one competitor”) that wouldn’t be ACME corp’s wikipedia page, then you should “fork” wikipedia and create your own page for ACME corp, which is stored in agent memory.
Q: Should you include secrets in your agent’s memory store? Eg: Cursor API key
A: Nope. Authenticating your agent is a separate task from your agent remembering things. A better model is to keep secrets in a separate server that stores authentication info for the agent (here’s a nice article on a common design pattern)
Q: Should you include user preferences in your agent’s memory store? Eg: “Please return all your responses in spanish”
A: Nope. That should go in a user-scoped file like `~/.claude/CLAUDE.md` or `CLAUDE.local.md`. The reasoning here is that we expect agent memory to become multiplayer soon, and agent memory should encode org-level preferences (eg: “we always make reports <2k words”) rather than user-level preferences.
Thanks to Sam Liu and Bryan Houlton for comments on this article!
