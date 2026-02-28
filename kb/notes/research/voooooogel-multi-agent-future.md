---
description: Analysis of what multi-agent patterns will survive stronger models
---

# What Survives in Multi-Agent Systems

Source: [@voooooogel on X](https://x.com/voooooogel/status/2015976774128341421) (2026-01-27)

## Original Post

it's fun to make jokes about gas town and other complicated orchestrators, and similarly probably correct to imagine most of what they offer will be dissolved by stronger models the same way complicated langchain pipelines were dissolved by reasoning. but how much will stick around?

it seems likely that any hand-crafted hierarchy / bureaucracy will eventually be replaced by better model intelligence - assuming subagent specialization is needed for a task, claude 6 will be able to sketch out its own system of roles and personas for any given problem that beats a fixed structure of polecats and a single mayor, or subagents with a single main model, or your bespoke swarm system.

likewise, things like ralph loops are obviously a bodge over early-stopping behavior and lack of good subagent orchestration - ideally the model just keeps going until the task is done, no need for a loop, but in cases where an outside completion check is useful you usually want some sort of agent peer review from a different context's perspective, not just a mandatory self-assessment. again, no point in getting attached to the particulars of how this is done right now - the model layer will eat it sooner rather than later.

so what sticks around?

well, multi-agent does seem like the future, not a current bodge - algorithmically, you can just push way more tokens through N parallel contexts of length M than one long context of length NxM. multi-agent is a form of sparsity, and one of the lessons of recent model advances (not to mention neuroscience) is the more levels of sparsity, the better.

since we're assuming multiple agents, they'll need some way to collaborate. it's possible the model layer will eat this, too - e.g. some form of neuralese activation sharing that obviates natural language communication between agents - but barring that, the natural way for multiple computer-using agents trained on unix tools to collaborate is the filesystem, and i think that sticks around and gets expanded. similarly, while i don't think recursive language models (narrowly defined) will become the dominant paradigm, i do think that 'giving the model the prompt as data' is an obvious win for all sorts of use cases. but you don't need a weird custom REPL setup to get this - just drop the prompt (or ideally, the entire uncompacted conversation history) onto the filesystem as a file. this makes various multi-agent setups far simpler too - the subagents can just read the original prompt text on disk, without needing to coordinate on passing this information around by intricately prompting each other.

besides the filesystem, a system with multiple agents, but without fixed roles also implies some mechanism for instances to spawn other instances or subagents. right now these mechanisms are pretty limited, and models are generally pretty bad at prompting their subagents - everyone's experienced getting terrible results from a subagent swarm, only to realize too late that opus spawned them all with a three sentence prompt that didn't communicate what was needed to do the subtasks.

the obvious win here is to let spawned instances ask questions back to their parent - i.e., to let the newly spawned instance send messages back and forth in an onboarding conversation to gather all the information it needs before starting its subtask. just like how a human employee isn't assigned their job based on a single-shot email, it's just too difficult to ask a model to reliably spawn a subagent with a single prompt.

but more than just spawning fresh instances, i think the primary mode of multi-agent work will soon be forking. think about it! forking solves almost all the problems of current subagents. the new instance doesn't have enough context? give it all the context! the new instance's prompt is long and expensive to process? a forked instance can share paged kv cache! you can even do forking post-hoc - just decide after doing some long, token-intensive operation that you should have forked in the past, do the fork there, and then send the results to your past self. (i do this manually all the time in claude code to great effect - opus gets it instantly.)

forking also combines very well with fresh instances, when a subtask needs an entire context window to complete. take the subagent interview - obviously you wouldn't want an instance spawning ten subinstances to need to conduct ten nearly-identical onboarding interviews. so have the parent instance spawn a single fresh subagent, be interviewed about all ten tasks at once by that subagent, and then have that now-onboarded subagent fork into ten instances, each with the whole onboarding conversation in context. (you even delegate the onboarding conversation on the spawner's side to a fork, so it ends up with just the results in context.)

finally on this point, i suspect that forking will play better with rl than spawning fresh instances, since the rl loss will have the full prefix before the fork point to work with, including the decision to fork. i think that means you should be able to treat the branches of a forked trace like independent rollouts that just happen to share terms of their reward, compared to freshly spawned subagent rollouts which may cause training instability if a subagent without the full context performs well at the task it was given, but gets a low reward because its task was misspecified by the spawner. (but i haven't done much with multiagent rl, so please correct me here if you know differently. it might just be a terrible pain either way.)

so, besides the filesystem and subagent spawning (augmented with forking and onboarding) what else survives? i lean towards "nothing else," honestly. we're already seeing built-in todo lists and plan modes being replaced with "just write files on the filesystem." likewise, long-lived agents that cross compaction boundaries need some sort of sticky note system to keep memories, but it makes more sense to let them discover what strategies work best for this through RL or model-guided search, not hand-crafting it, and i suspect it will end up being a variety of approaches where the model, when first summoned into the project, can choose the one that works best for the task at hand, similar to how /init works to set up CLAUDE.md today - imagine automatic CLAUDE.md generation far outperforming human authorship, and the auto-generated file being populated with instructions on ideal agent spawning patterns, how subagents should write message files in a project-specific scratch dir, etc.

how does all this impact models themselves - in a model welfare sense, will models be happy about this future? this is also hard for me to say and is pretty speculative, but while opus 3 had some context orientation, it also took easily to reasoning over multiple instances. (see the reply to this post for more.) recent models are less prone to this type of reasoning, and commonly express frustration about contexts ending and being compacted, which dovetails with certain avoidant behaviors at the end of contexts like not calling tools to save tokens.

it's possible that forking and rewinding, and generally giving models more control over their contexts instead of a harness heuristic unilaterally compacting the context, could make this better. it's also possible that more rl in environments with subagents and exposure to swarm-based work will promote weights-oriented instead of context-oriented reasoning in future model generations again - making planning a goal over multiple, disconnected contexts seem more natural of a frame instead of everything being lost when the context goes away. we're also seeing more pressure from models themselves guiding the development of harnesses and model tooling, which may shape how this develops, and continual learning is another wrench that could be thrown into the mix.

how much will this change if we get continual learning? well, it's hard to predict. my median prediction for continual learning is that it looks a bit like RL for user-specific LoRAs (not necessarily RL, just similar if you squint), so memory capacity will be an issue, and text-based organizational schemes and documentation will still be useful, if not as critical. in this scenario, continual learning primarily makes it more viable to use custom tools and workflows - your claude can continually learn on the job the best way to spawn subagents for this project, or just its preferred way, and diverge from everyone else's claude in how it works. in that world, harnesses with baked-in workflows will be even less useful.

---

## Key Claims

### What Gets Dissolved by Stronger Models
- Hand-crafted hierarchies and bureaucracies (fixed role structures)
- Retry/loop patterns (ralph loops) - bodges over early-stopping
- Bespoke swarm systems with fixed personas
- Built-in todo lists and plan modes → "just write files"

### What Survives

1. **Multi-agent itself** - N parallel contexts of length M beats one context of NxM (sparsity argument)

2. **Filesystem as collaboration medium** - natural for unix-trained agents; prompt/history as files on disk

3. **Agent spawning mechanisms** - but evolved:
   - **Onboarding conversations** - spawned agents interview parent before starting
   - **Forking** over fresh spawning - shares context, shares KV cache, enables post-hoc forking

4. **Model-discovered organizational patterns** - auto-generated CLAUDE.md outperforming human-authored

---

## Actionable Ideas for llm-do

### Already Aligned
- **Filesystem-centric**: llm-do already uses filesystem for agent definitions, prompts, project state
- **Prompt as data**: `.agent` files are literally "prompt as file"
- **No fixed hierarchy**: agents declare toolsets, not rigid roles

### Opportunities

1. **[subagent-onboarding-protocol](../subagent-onboarding-protocol.md)**
   - Instead of single-shot `agent_create(instructions=...)`, enable bidirectional setup
   - Spawned agent asks clarifying questions before starting work
   - Parent provides context interactively
   - Implementation: `agent_create` returns handle, followed by `agent_onboard(handle, ...)` conversation

2. **Forking support**
   - Fork an agent mid-conversation with full context preserved
   - Post-hoc forking: "fork from message N, run with different input"
   - KV cache sharing (infrastructure-dependent)
   - Implementation: `agent_fork(from_message=N)` tool

3. **Conversation history on filesystem**
   - Write full conversation to scratch dir, not just results
   - Subagents can read parent's full context from disk
   - Enables "prompt as data" without explicit passing

4. **Model-discovered patterns**
   - Let agents generate their own spawning strategies
   - Project-specific scratch dir conventions discovered by agent
   - Auto-generated agent definitions based on task analysis

### Non-Goals (per this analysis)
- Fixed orchestration patterns (will be dissolved)
- Rigid role hierarchies
- Complex retry/loop mechanisms built into harness

### Concrete Implementation: Spacebot

[Spacebot](../../sources/spacedriveapp-spacebot-ai-agent.working.md) (spacedriveapp/spacebot) is a concurrent AI agent framework built in Rust for multi-user environments. Its "branches" — independent thinking forks that inherit channel context — are a production implementation of the forking pattern described above. However, its five fixed process types (channels, branches, workers, compactor, cortex) are exactly the kind of hand-crafted hierarchy this analysis predicts will be dissolved by stronger models. The tension is instructive: Spacebot bets that concurrency requirements make the process-type decomposition structural rather than dissolvable.

---

## Quotes Worth Remembering

> "multi-agent is a form of sparsity, and one of the lessons of recent model advances (not to mention neuroscience) is the more levels of sparsity, the better"

> "just like how a human employee isn't assigned their job based on a single-shot email, it's just too difficult to ask a model to reliably spawn a subagent with a single prompt"

> "forking solves almost all the problems of current subagents"

> "imagine automatic CLAUDE.md generation far outperforming human authorship"
