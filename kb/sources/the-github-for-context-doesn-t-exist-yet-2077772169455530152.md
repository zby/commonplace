---
source: https://x.com/prukalpa/status/2077772169455530152
captured: 2026-07-17T18:28:59.706584+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2077772169455530152
conversation_id: 2077772169455530152
post_count: 3
---

# The GitHub for Context Doesn’t Exist Yet

Author: @prukalpa
Post: https://x.com/prukalpa/status/2077772169455530152
Created: 2026-07-16T15:07:42.000Z

A walkthrough of my talk at the AI Engineer World’s Fair: two eras of building agents inside my own company, five stack migrations, and the infrastructure question I left the room with.
 
By the middle of last year, we could build an agent in about five minutes. Giving it enough business context to be accurate took forever. In the twelve months that followed, my company moved through five agent-stack configurations. Each change left something important behind: not the agent, which was easy enough to recreate, but the context that made it useful.
At one point, we had roughly 300 skills powering 40 active agents. The lesson from getting there was uncomfortable: the agents were never the hard part.
At the AI Engineer World’s Fair, I opened the build log behind that conclusion. I walked through two eras of building agents inside our company: first, an agent for every job; then, one shared company brain serving many agents. Both worked. Both eventually hit a wall. And the second wall exposed an infrastructure gap I think this community will spend the next few years closing.
Watch the full twenty-minute talk: "WTF Is the Context Layer?"
The agent layer is becoming disposable. Your company’s context is not. Yet most of the tools we use still bind the two together.
The backdrop, in one paragraph, because I have made the full argument before. Models are getting exponentially smarter and not exponentially more useful: only about one in five organizations reports significant value from AI, by Gartner’s count, and 56% of CEOs told PwC they have seen neither higher revenue nor lower costs from AI in the past year. Performance is intelligence times context, and the relationship is multiplicative. I walked through the whole diagnosis in the Knowledge Graph Conference talk and the moat piece. This piece is about what happens after you believe it.
 
 
What the agent needs to know
To make context concrete, I brought back Maya, a character I have used before. At the Knowledge Graph Conference, she was a support rep. For this talk she was promoted to data analyst at McContext Burgers, a name I chose because I thought I was going to be creative and clearly was not.
 
Marcus, a franchisee with fourteen stores, sends her a question first thing in the morning: “Why is my drive-thru time up this week?”
The request sounds simple until you count what Maya must know to answer it.
What does “drive-thru time” mean, and whose definition applies, the one used by finance or the one used by operations? Does “this week” mean Monday through Sunday or the trailing seven days, and in which time zone? That is knowledge: the map of the business.
A strong analyst also knows that Q3 spikes are seasonal and that the company launched a product last quarter, so she rules out those explanations first. That is expertise: the diagnostic sequence nobody thought to write down.
Then there are norms. Who is asking? Does Marcus need a metric, an explanation, or a decision? Who is allowed to see the underlying data? When finance and operations disagree, whose definition governs this answer?
Maya did not learn all of this in onboarding. She learned it by shadowing an excellent analyst, making mistakes, receiving feedback, encountering edge cases, and not making the same mistake twice. That is how people become useful inside a company. The engineering question is: how do you build the agent Maya?
 
Era one: an agent for every job
Eighteen months ago, we started where many companies start. We took one team, mapped its jobs to be done, and formed hypotheses about which jobs AI could perform. Documentation and meeting preparation: yes. Relationship management: not soon. Then we built an agent for each job we believed in.
 
It worked, for a while. Then we met four walls.
The first was accuracy. Spinning up the agent was trivial. Giving it enough business context to be right was the real work. Its quality tracked the quality of its context almost exactly, and every gap created a moment in which a stakeholder learned not to trust it. Trust does not return at the speed it leaves.
The second was dependency management & silos. When marketing changed our positioning, the humans heard about it at the town hall. Our website agent continued pitching the old positioning for weeks. Companies have spent a century building ways to keep human teams aligned: meetings, documents, onboarding, managers. Our agents had none of them. We could not even see how the agents we had shipped related to one another.
The third was root cause analysis & traceability. When an agent produced a bad answer, we often could not tell whether the problem came from the model, the agent design, or the context it received. If you cannot locate the failure, you cannot reliably fix it.
The fourth was sprawl & drift. Every agent had its own memory, so every agent learned separately. Ask two of them a question with one business answer and you might get three.
Under all four sat the wall that drew the most knowing laughter from the engineers in the room: stack churn. In twelve months, we moved through five agent-stack configurations, from a no-code builder to hyperscaler and enterprise-search frameworks to general-purpose coding agents to our own system of claws in slack.
This heterogeneity in our agentic stack amplified organisational silos built in our human stack. Our customer-success team built on one agentic framework, which accumulated context about our customers. Sales used a different agentic framework. Moving context between sales and post-sales was difficult, and the split produced agents that repeated and overlapped one another’s work.
The framework was becoming disposable. The context on the other hand, was not. And the context was what we kept losing.
 
 
Era two: one brain, many agents
This year, general-purpose agents like Claude Code changed what was fundamentally possible, so we inverted the architecture.
Instead of feeding context into each agent separately, domain experts encoded what they knew into shared skills. Those skills lived in one company brain. Retrieval and assembly connected that brain to whichever general-purpose agent was doing the work.
 
The idea came from the human world. Maya is not a lone star; she belongs to a team. Strong teams share a language, a picture of what is true today, playbooks for recurring decisions, norms about who decides what, and memory of what failed. The team learns as a unit.
Our marketing team ran the first experiment. On one side were our business systems. On the other were deliberately heterogeneous agents: coding agents in the terminal, an agent in our chat channels, and external products. The shared context sat between them. We chose a mixed agent surface because era one had taught us that this layer would keep changing.
 
Our best SEO person wrote the SEO skill. Our best competitive-intelligence person wrote the competitive-intelligence skill. Everyone contributed to one shared system; every agent could draw from it.
The brain asked for more than skills. An autonomous ads agent needed to know which tables to query, so we needed a data graph. Then it needed semantics: what does ARR mean here? What counts as a qualified lead when marketing and finance use different definitions?
Over six months, the team created about 300 skills and 40 agents, an active point-in-time snapshot, not a cumulative count. By a skill, I mean an encoded procedure or process that another person can pick up and use in a general-purpose agent. By an agent, I mean a system that proactively performs work without waiting for human intervention.
This architecture let expertise written once become available to a heterogeneous agent fleet. Then it exposed a different class of failure.
 
The wall at 300 skills
Consider what happened when our marketing team changed our core category narrative. That positioning fed email workflows used by sales and customer success. But the narrative had been hardcoded into those workflows as an earlier snapshot. Nothing declared the dependency, so the upstream change never reached the downstream agents. They continued sending the old story.
 
This was not an isolated design quirk, and in principle it was not a surprise: I had argued before that context must be managed like code, versioned, tested, owned. Living that prescription turned out to be different from writing it. Skills learned, evolved, and drifted; we could not always say who owned their quality or what a change might affect.
Security and governance became what I called “a nightmare” on stage. We found secrets hardcoded in environment files while people were also downloading public skill repositories into company workflows. Once we saw the risk, we stopped the affected work and ran a full audit. We are not claiming that a breach occurred. The point is that the context layer had become executable infrastructure before it had the controls executable infrastructure demands.
The obvious answer, especially in a room full of engineers, is: this is what git is for. Put the skills in a repository. Review the pull requests. Done.
We did that. Era two ran on git from day one, and git is a large part of why it worked for as long as it did.
But git versions text, not meaning.
Git can show that a definition changed. It cannot, on its own, tell you that the new definition of a qualified lead changes a battle card two dependencies downstream. It does not know that a competitive-intelligence update contradicts positioning owned by another team, or that this contradiction requires that team’s approval. A repository can store a production trace; it does not turn what 40 agents learned this week into safe, reviewable proposals for improving shared context.
This is not an argument against git. It is the same argument software engineering already made around it. Diffs and history were foundational, but they were not sufficient. Industrial software required version control plus code review, ownership, continuous integration, dependency management, security scanning, package registries, and runtime observability.
Context has the diffs. It does not yet have a coherent version of the rest.
 
What the missing infrastructure must do
“The GitHub for context” is an imperfect shorthand. The missing thing is not a nicer repository. Nor is it necessarily one product. It is the operating layer that lets a company treat context as durable infrastructure rather than agent-specific configuration.
 
Our build log suggests at least five requirements.
First, every unit of context needs a Github like profile: an owner, approvers, maintainers, scope, provenance, and declared dependencies. I believe over time - skills, semantic models, tools will all be managed as “units of context” in companies.
Second, local and company-wide context must remain distinct.Enterprises do not have one frictionless source of truth. Marketing and finance can use different definitions for legitimate reasons. The system needs a governed path for preserving those differences and promoting local knowledge when it should become a shared standard.
Third, change needs semantic review. A text diff is useful; a reviewer also needs to know which decisions, evaluations, and downstream agents the change may affect. Declared dependencies will never capture all emergent behavior, but they can make impact visible enough to test.
Fourth, learning must form a controlled loop. Every AI interaction creates more context, and harnessing it is gold. We experimented with a specialized harness that reads production traces, reverse-constructs candidate improvements, and returns them to maintainers as approve-or-reject proposals. Production traces can also contain errors, sensitive information, and context-specific behavior, so the output cannot become autonomous truth. It needs provenance checks, evaluations, bounded promotion, and human approval.
Fifth, quality and security must be native to the layer. Secrets scanning, permission boundaries, evaluation, rollback, retention, and deletion cannot arrive after an agent has already executed the context.
All of this must remain portable across the interfaces agents use: MCP, SQL, vector retrieval, or hybrid assembly. Betting the context layer on one interface only recreates the lock-in that caused the problem. I mapped the full anatomy of this architecture in the June field guide; this piece is the scar tissue behind it.
Not every company needs this machinery on day one. A small team with a handful of agents may be better served by explicit files, owners, and evaluations. The infrastructure becomes necessary when context crosses teams, changes independently, feeds autonomous work, or must survive a change in the agent layer. That is the boundary our own system crossed.
 
Context is IP
A year ago, my co-founder and I stood on a stage and argued that if content was king at the dawn of the internet, context would be king at the dawn of the agentic era. After building through these two eras, I believe there is a sharper formulation: context is IP.
 
And context goes far beyond the data itself. Satya Nadella recently wrote about IP in the AI age, arguing that a company’s proprietary knowledge is an incredible moat. I would like to take that one step further: the defensible asset isn’t just proprietary knowledge—it’s the company’s accumulated operating model itself. This encompasses definitions, exceptions, playbooks, judgment calls, and norms, along with the provenance and permissions that make them usable and allow them to evolve over time.
When competitors can call many of the same models, the model alone cannot encode why two companies serve the same customer differently. Context carries those differences into autonomous systems. It is the part of the stack a competitor cannot simply download.
That makes portability more than an engineering preference. When context is trapped in an agent framework, a company has coupled its operating knowledge to a disposable layer. When context is unowned, untested, or insecure, a company is managing its most defensible IP with less discipline than its expense reports. Left alone, that drift ends the way the old joke says: ask sales and finance for the revenue number and you get two answers. We are close to the version where two autonomous systems hand the CFO those two numbers, and no human is in the loop to catch the joke.
I said one more thing on that stage that I want in writing: I believe this problem is under-hyped. That is not a sentence anyone gets to say about anything with the word AI in it in 2026, and I stand by it, because the hype is all on the intelligence axis while the failure is on the other one.
 
The five-minute audit
The starting question does not require a new platform.
List every place each production agent in your company gets its context. For each source, name the owner, the scope, the downstream consumers, the last time it changed, and how you would detect a bad change.
If that map is coherent, you have the beginnings of a context layer. If it is a collection of agent-specific memories, prompts, repositories, and connectors, you have islands. The reconciliation bill is already accruing.
The AI Engineer World’s Fair gave context engineering its own track this year, alongside a memory track one day and a full graphs track another, at a conference where the organizers stopped counting attendees around six thousand. One main-stage speaker presented under the job title “Context Engineer.” One recap of the fair put it the way I would have: “a discipline gets real when it earns a conference track, a shared vocabulary and a title on someone’s business card.” And Latent Space’s trends piece named the systems around agents, skills included, as what defined the year. The room did not need another argument that models require context. The people there were already living through the harder question: what happens when that context becomes shared production infrastructure?
Software engineering built its disciplines when code reached this wall. Context has reached it now. We should build the toolchain deliberately, before the next agent migration reminds us which layer was valuable all along.
Watch the full twenty-minute talk: "WTF Is the Context Layer?"
 
The Cats of Context & Chaos
 
This article was originally published on the Context & Chaos platform.
 
That’s all for this edition. Stay curious, keep exploring, and see you all in the next one!
Thanks for reading Context & Chaos! Subscribe for free to receive new posts and support our work.
 
About Context & Chaos
Context & Chaos isn’t just a newsletter. It’s shared community space where practitioners, builders, and thinkers come together to share stories, lessons, and ideas about what truly matters in the world of data and AI: context engineering, governance, architecture, discovery, and the human side of doing meaningful work.
Our goal is simple, to create a space that cuts through the noise and celebrates the people behind the amazing things that are happening in the data & AI domain.
Whether you’re solving messy problems, experimenting with AI, or figuring out how to make data more human, Context & Chaos is your place to learn, reflect, and connect.
Got something on your mind? We’d love to hear from you.
