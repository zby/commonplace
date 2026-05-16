---
source: https://x.com/shivsakhuja/status/2047124337191444844
captured: 2026-04-23T07:19:24.259560+00:00
capture: xdk
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2047124337191444844
conversation_id: 2047124337191444844
post_count: 1
---

# A new way to think about composing skills to increase leverage: Skill Graphs 2.0

Author: @shivsakhuja
Post: https://x.com/shivsakhuja/status/2047124337191444844
Created: 2026-04-23T01:24:10.000Z

One of the most valuable things I've learned recently is how to think about composing skills to get more leverage in my work.
The skill graph idea got a lot of interest recently. The idea is to create a graph of skills by linking dependent skills in markdown files, similar to how you might link notes in Obsidian.
A skill encodes knowledge + process into a markdown file + optional scripts that an agent can run repeatably.
So a skill graph makes a ton of sense intuitively – when you try to encode larger processes or job functions into skills, you'll probably have skills that depend on other skills.
For example, a skill to draft a marketing email might depend on a graphic design skill.
Where Skill Graphs Break
But when your skill graph gets big enough, Agents may not reliably call skills past a certain depth. The more the dependencies the less reliable it gets. (a lot of people on reddit and X who've tried this out in practice have pointed this out too).
If Skill A explicitly instructs to call Skill B, it will probably be pretty reliable.
But in a dense graph (think Wikipedia), there may be an enormous depth to the dependency chains, so you can't really be sure what will happen.
This is a problem because a human driver with a specific intent is now confronted with a lot of non-determinism, and is handing off a lot of judgement to the agent (maybe too much).
 Circular dependencies can also be problematic.
So do we abandon the idea as a dud?
Definitely not.
The underlying idea of composing skills is still really important, and if you can compose skills effectively you can unlock an additional step function of leverage in any kind of work.
A Different Way to Compose Skills
I believe the solution is to compose skills differently.
Here's how I think about it.
Skills operate at different levels: atoms, molecules, and compounds. 
Higher level skills provide the agent with more judgement on how to orchestrate, lower level skills provide the model with a very clear workflow to execute.
 
ATOMS
These are the base-level atomic skills. These are single-purpose building blocks, narrow in scope - primitives.
Examples:
scrape LinkedIn profiles
find a competitor's blog posts
find a person on Apollo
verify an email with Hunter
check email deliverability
research a topic
review this PR
These should be super reliable. Almost deterministic (or as close as you can get with an LLM).
Atoms (typically) don't call other skills at all.
MOLECULES
Molecules solve larger problems.
A molecule might use 2-10 atomic skills to complete a scoped task.
It should have explicit instructions on when and how to call the atomic skills.
It will allow the agent more judgement than atoms, but still try to provide explicit instructions on when to use which skill is very helpful.
You push as much of the composition into the skill, and minimize the agent's runtime decision-making.
Molecules should also be very reliable. An example:
1. a structured workflow that chains together a few atoms.
find leads using atom-1 and atom-2 -> then qualify them using atom-3 and enrich them using atom-4 and then add them to my spreadsheet with atom-5.
2. an orchestrator that knows about 5 atoms, and will use its judgement to compose them to solve the prompt
There might be other structures too.
The agent will naturally have more judgement and autonomy here than with atoms, but we're still aiming to keep things as explicit as possible.
COMPOUNDS
Compounds are higher-level orchestrators that run multiple molecules.
"run outbound sales playbook"
"plan and build this feature, then review and QA it"
This is the level where you actually hand the agent meaningful autonomy.
These are likely going to be less deterministic by nature, because there's so many levels at which the agent might need to make judgements.
These are also the trickiest to actually get right, and they will probably require a human to drive them.
Yes, a human probably needs to drive the compounds (at least today).
Leverage & Brain RAM
Each level is an order of magnitude of leverage higher, so if you are driving compounds instead of atoms, you can probably do 100x more.
Here's why.
Your brain's RAM (ability to hold multiple tasks in memory and context switch effectively) is actually the limiting resource now.
For example, consider this scenario.
Let's say your brain is capable of context switching between up to 5 agents in parallel.
Now suppose:
1 compound orchestrates 10 molecules
1 molecule orchestrates 10 atoms (RELIABLY of course)
If you are driving your agents to do atomic work, you're just clogging up 1 RAM slot with low-leverage work because that work is basically deterministic. 
Why are you sitting in the driver's seat when your car has full self-driving?
But if you're driving 5 agents that you're orchestrating in parallel to do molecule or compound level work, that's:
5 compound tasks
50 molecular tasks
500 atomic units of work
It takes a similar amount of brain RAM and time to execute 5 atomic tasks in parallel vs 5 compound tasks in parallel.
 
For the same amount of time and brain RAM spent, work output varies massively if you drive atomic work vs compound work
There's a good parallel here with how a CTO of a company with 1000 employees is not going to be fixing every bug himself. He can trust the ICs to do that work reliably.
Where This Breaks (Still Figuring It Out)
Of course, the key here is that:
every atom has to be solid
the molecules have to chain them dependably
the agent needs enough autonomy at the compound level to make real decisions
Your judgement is at the compound level (or higher).
Still figuring out where this breaks.
My guess: compounds that span more than 8-10 molecules start hitting their own reliability ceiling.
At some point, compounds will be good enough that we'll need even higher abstraction above that.
I haven't hit it yet.
I'm still driving molecules and compounds, and even that does not feel trivial to get right.
But the goal is to keep moving up to higher levels for every workstream.
We set up our skills library with this atoms / molecules / compounds structure and it's pretty good.
We called them:
capabilities (atoms)
composites (molecules)
playbooks (compounds)
So far it's working pretty well.
The big challenge
The reliability / consistency of the skills at every level is non-trivial to get right and testing the skills takes a lot of time.
I imagine an autoresearch type solution might be able to solve this, but I haven't tried that yet for this problem. Hopefully someday soon.
