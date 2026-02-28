---
source: https://x.com/koylanai/status/2025286163641118915
captured: 2026-02-22T11:51:03.499122+00:00
capture: xdk
type: x-article
status_id: 2025286163641118915
conversation_id: 2025286163641118915
post_count: 12
---

# The File System Is the New Database: How I Built a Personal OS for AI Agents

Author: @koylanai
Post: https://x.com/koylanai/status/2025286163641118915
Created: 2026-02-21T19:07:04.000Z

Every AI conversation starts the same way. You explain who you are. You explain what you're working on. You paste in your style guide. You re-describe your goals. You give the same context you gave yesterday, and the day before, and the day before that. Then, 40 minutes in, the model forgets your voice and starts writing like a press release.
I got tired of this. So I built a system to fix it.
I call it Personal Brain OS. It's a file-based personal operating system that lives inside a Git repository. Clone it, open it in Cursor or Claude Code, and the AI assistant has everything: my voice, my brand, my goals, my contacts, my content pipeline, my research, my failures. No database, no API keys, no build step. Just 80+ files in markdown, YAML, and JSONL that both humans and language models read natively.
 
I'm sharing the full architecture, the design decisions, and the mistakes so you can build your own version. Not a copy of mine; yours. The specific modules, the file schemas, the skill definitions will look different for your work. But the patterns transfer. The principles for structuring information for AI agents are universal. Take what fits, ignore what doesn't, and ship something that makes your AI actually useful instead of generically helpful.
Here's how I built it, why the architecture decisions matter, and what I learned the hard way.
 
1) THE CORE PROBLEM: CONTEXT, NOT PROMPTS
Most people think the bottleneck with AI assistants is prompting. Write a better prompt, get a better answer. That's true for single interactions and production agent prompts. It falls apart when you want an AI to operate as you across dozens of tasks over weeks and months.
The Attention Budget: Language models have a finite context window, and not all of it is created equal. This means dumping everything you know into a system prompt isn't just wasteful, it actively degrades performance. Every token you add competes for the model's attention. 
 
Our brains work similarly. When someone briefs you for 15 minutes before a meeting, you remember the first thing they said and the last thing they said. The middle blurs. Language models have the same U-shaped attention curve, except theirs is mathematically measurable. Token position affects recall probability. The newer models are getting better at this, but still, you are distracting the model from focusing on what matters most. Knowing this changes how you design information architecture for AI systems. 
 
Instead of writing one massive system prompt, I split Personal OS into 11 isolated modules. When I ask the AI to write a blog post, it loads my voice guide and brand files. When I ask it to prepare for a meeting, it loads my contact database and interaction history. The model never sees network data during a content task, and never sees content templates during a meeting prep task.
 
Progressive Disclosure: This is the architectural pattern that makes the whole system work. Instead of loading all 80+ files at once, the system uses three levels. Level 1 is a lightweight routing file that's always loaded. It tells the AI which module is relevant. Level 2 is module-specific instructions that load only when that module is needed. Level 3 is the actual data JSONL logs, YAML configs, research documents, loaded only when the task requires them. 
This mirrors how experts operate. The three levels create a funnel: broad routing, then module context, then specific data. At each step, the model has exactly what it needs and nothing more. 
 
My routing file is `SKILL.md` that tells the agent "this is a content task, load the brand module" or "this is a network task, load the contacts." The module instruction files (`CONTENT.md`, `OPERATIONS.md`, `NETWORK.md`) are 40-100 lines each, with file inventories, workflow sequences, and an `<instructions>` block with behavioural rules for that domain. Data files load last, only when needed. The AI reads contacts line by line from JSONL rather than parsing the entire file. Three levels, with a maximum of two hops to any piece of information.
 
The Agent Instruction Hierarchy: I built three layers of instructions that scope how the AI behaves at different levels. At the repository level, `CLAUDE.md` is the onboarding document -- every AI tool reads it first and gets the full map of the project. At the brain level, `AGENT.md` contains seven core rules and a decision table that maps common requests to exact action sequences. At the module level, each directory has its own instruction file with domain-specific behavioral constraints. 
 
This solves the "conflicting instructions" problem that plagues large AI projects. When everything lives in one system prompt, rules contradict each other. A content creation instruction might conflict with a networking instruction. By scoping rules to their domain, you eliminate conflicts and give the agent clear, non-overlapping guidance. The hierarchy also means you can update one module's rules without risking regression in another module's behavior. 
 
My `AGENT.md` is a decision table. The AI reads "User says 'send email to Z'" and immediately sees: 
Step 1, look up contact in HubSpot. 
Step 2, verify email address. 
Step 3, send via Gmail. 
Module-level files like `OPERATIONS.md` define priority levels (P0: do today, P1: this week, P2: this month, P3: backlog) so the agent triages tasks consistently. The agent follows the same priority system I use because the system is codified, not implied.
 
2) THE FILE SYSTEM AS MEMORY
One of the most counterintuitive decisions I made: no database. No vector store. No retrieval system except Cursor or Claude Code's features. Just files on disk, versioned with Git.
 
Format-Function Mapping: Every file format in the system was chosen for a specific reason related to how AI agents process information. JSONL for logs because it's append-only by design, stream-friendly (the agent reads line by line without parsing the entire file), and every line is self-contained valid JSON. YAML for configuration because it handles hierarchical data cleanly, supports comments, and is readable by both humans and machines without the noise of JSON brackets. Markdown for narrative because LLMs read it natively, it renders everywhere, and it produces clean diffs in Git. 
 
JSONL's append-only nature prevents a category of bugs where an agent accidentally overwrites historical data. I've seen this happen with JSON files agent writes the whole file, loses three months of contact history. With JSONL, the agent can only add lines. Deletion is done by marking entries as `"status": "archived"`, which preserves the full history for pattern analysis. YAML's comment support means I can annotate my goals file with context the agent reads but that doesn't pollute the data structure. And Markdown's universal rendering means my voice guide looks the same in Cursor, on GitHub, and in any browser. 
 
My system uses 11 JSONL files (posts, contacts, interactions, bookmarks, ideas, metrics, experiences, decisions, failures, engagement, meetings), 6 YAML files (goals, values, learning, circles, rhythms, heuristics), and 50+ Markdown files (voice guides, research, templates, drafts, todos). Every JSONL file starts with a schema line: `{"_schema": "contact", "_version": "1.0", "_description": "..."}`. The agent always knows the structure before reading the data.
 
Episodic Memory: Most "second brain" systems store facts. Mine stores judgment as well. The `memory/` module contains three append-only logs: `experiences.jsonl` (key moments with emotional weight scores from 1-10), `decisions.jsonl` (key decisions with reasoning, alternatives considered, and outcomes tracked), and `failures.jsonl` (what went wrong, root cause, and prevention steps). 
 
There's a difference between an AI that has your files and an AI that has your judgment. Facts tell the agent what happened. Episodic memory tells the agent what mattered, what I'd do differently, and how I think about tradeoffs. When the agent encounters a decision similar to one I've logged, it can reference my past reasoning instead of generating generic advice. The failures log is the most valuable, it encodes pattern recognition that took real pain to acquire. 
When I was deciding whether to accept Antler Canada's $250K investment or join Sully.ai as Context Engineer, the decision log captured both options, the reasoning for each, and the outcome. If a similar career tradeoff comes up, the agent doesn't give me generic career advice. It references how I actually think about these decisions: "Learning > Impact > Revenue > Growth" is my priority order, and "Can I touch everything? Will I learn at the edge of my capability? Do I respect the founders?" is my company-joining framework.
Cross-Module References: The system uses a flat-file relational model. No database, but structured enough for agents to join data across files. `contact_id` in `interactions.jsonl` points to entries in `contacts.jsonl`. `pillar` in `ideas.jsonl` maps to content pillars defined in `identity/brand.md`. Bookmarks feed content ideas. Post metrics feed weekly reviews. The modules are isolated for loading, but connected for reasoning.
Isolation without connection is just a pile of folders. The cross-references let the agent traverse the knowledge graph when needed. "Prepare for my meeting with Sarah" triggers a lookup chain: find Sarah in contacts, pull her interactions, check pending todos involving her, compile a brief. The agent follows the references across modules without loading the entire system. 
My pre-meeting workflow chains three files: `contacts.jsonl` (who they are), `interactions.jsonl` (filtered by contact_id for history), and `todos.md` (any pending items). The agent produces a one-page brief with relationship context, last conversation summary, and open follow-ups. No manual assembly. The data structure makes the workflow possible.
 
3) THE SKILL SYSTEM: TEACHING AI HOW TO DO YOUR WORK
Files store knowledge. Skills encode process. I built Agent Skills following the Anthropic Agent Skills standard, structured instructions that tell the AI how to perform specific tasks with quality gates baked in.
 
Auto-Loading vs. Manual Invocation: Two types of skills solve two different problems. Reference skills (`voice-guide`, `writing-anti-patterns`) set `user-invocable: false` in their YAML frontmatter. The agent reads the description field and injects them automatically whenever the task involves writing. I never invoke them, they activate silently, every time. Task skills (`/write-blog`, `/topic-research`, `/content-workflow`) set `disable-model-invocation: true`. The agent can't trigger them on its own. I type the slash command, and the skill becomes the agent's complete instruction set for that task. 
 
Auto-loading solves the consistency problem. I don't have to remember to say "use my voice" every time I ask for a draft. The system remembers for me. Manual invocation solves the precision problem. A research task has different quality gates than a blog post. Keeping them separate prevents the agent from conflating two different workflows. The YAML frontmatter is the mechanism, and a few metadata fields control the entire loading behaviour. 
 
When I type `/write-blog context engineering for marketing teams`, five things happen automatically: the voice guide loads (how I write), the anti-patterns load (what I never write), the blog template loads (7-section structure with word count targets), the persona folder is checked for audience profiles, and the research folder is checked for existing topic research. One slash command triggers a full context assembly. The skill file itself says "Read `brand/tone-of-voice.md`", it references the source module, never duplicates the content. Single source of truth.
 
The Voice System: My voice is encoded as structured data and ngl with some vibes. The voice profile rates five attributes on a 1-10 scale: Formal/Casual (6), Serious/Playful (4), Technical/Simple (7), Reserved/Expressive (6), Humble/Confident (7). The anti-patterns file contains 50+ banned words across three tiers, banned openings, structural traps (forced rule of three, copula avoidance, excessive hedging), and a hard limit of one em-dash per paragraph. 
 
Most people describe their voice with adjectives: "professional but approachable." That's useless for an AI. A 7 on the Technical/Simple scale tells the model exactly where to land. The banned word list is even more powerful; it's easier to define what you're NOT than what you are. The agent checks every draft against the anti-patterns list and rewrites anything that triggers it. The result is content that sounds like me because the guardrails prevent it from sounding like AI. 
Every content template includes voice checkpoints every 500 words: "Am I leading with insight? Am I being specific with numbers? Would I actually post this?" The blog template has a 4-pass editing process built in: structure edit (does the hook grab?), voice edit (banned words scan, sentence rhythm check), evidence edit (claims sourced?), and a read-aloud test. The quality gates are part of the skill, not something I add after the fact.
 
Templates as Structured Scaffolds: Five content templates define the structure for different content types. The long-form blog template has seven sections (Hook, Core Concept, Framework, Practical Application, Failure Modes, Getting Started, Closing) with word count targets per section totaling 2,000-3,500 words. The thread template defines an 11-post structure with a hook, deep-dive, results, and CTA. The research template has four phases: landscape mapping, technical deep-dive, evidence collection, and gap analysis. 
Templates not only constrain creativity but also constrain chaos. Without structure, the agent produces amorphous blobs of text. With structure, it produces content that has rhythm, progression, and payoff. Each template also includes a quality checklist so the agent can self-evaluate before presenting the draft. 
The research template outputs to `knowledge/research/[topic].md` with a structured format: Executive Summary, Landscape Map, Core Concepts, Evidence Bank (with statistics, quotes, case studies, and papers each cited with source and date), Failure Modes, Content Opportunities, and a Sources List graded HIGH/MEDIUM/LOW on reliability. That research document then feeds into the blog template's outline stage. The output of one skill becomes the input of the next. The pipeline builds on itself.
 
4) THE OPERATING SYSTEM: HOW I ACTUALLY USE THIS DAILY
Architecture is nothing without execution. 
Here's how the system runs in practice.
The Content Pipeline: Seven stages: Idea, Research, Outline, Draft, Edit, Publish, Promote. 
Ideas are captured to `ideas.jsonl` with a scoring system, each idea rated 1-5 on alignment with positioning, unique insight, audience need, timeliness, and effort-versus-impact. Proceed if total score hits 15 or higher. 
Research outputs to the knowledge module. 
Drafts go through four editing passes. 
Published content gets logged to `posts.jsonl` with platform, URL, and engagement metrics. 
Promotion uses the thread template to create an X announcement and a LinkedIn adaptation. 
 
I batch content creation on Sundays: 3-4 hours, target output of 3-4 posts drafted and outlined. The content calendar maps each day to a platform and content type.
The Personal CRM: Contacts organized into four circles with different maintenance cadences: inner (weekly), active (bi-weekly), network (monthly), dormant (quarterly reactivation). Each contact record has `can_help_with` and `you_can_help_with` fields that enable the introduction matching system. cross-referencing these fields surfaces mutually valuable intros. Interactions are logged with sentiment tracking (positive, neutral, needs_attention) so relationship health is visible at a glance. 
 
Most people keep contacts in their head and let relationships decay through neglect. The `stale_contacts` script cross-references contacts (who they are), interactions (when we last talked), and circles (how often we should talk) to surface outreach needs. A 30-second scan each week shows me which relationships need attention. 
Specialized groups in `circles.yaml`founders, investors, ai_builders, creators, mentors, mentees, each have explicit relationship development strategies. For AI builders: share useful content, collaborate on open source, provide tool feedback, amplify their work. For mentors: bring specific questions, update on progress from previous advice, look for ways to add value back. These are operational instructions the agent follows when I ask "Who should I reach out to this week?"
Automation Chains: Five scripts handle recurring workflows. They chain together for compound operations. The Sunday weekly review runs three scripts in sequence: `metrics_snapshot.py` updates the numbers, `stale_contacts.py` flags relationships, `weekly_review.py` generates a summary document with completed-versus-planned, metrics trends, and next week's priorities. The content ideation chain reads recent bookmarks, checks undeveloped ideas, generates fresh suggestions, and cross-references with the content calendar to find scheduling gaps. These aren't cron jobs -- the agent runs them when I ask for a review, or I trigger them with `npm run weekly-review`. 
 
Scripts that output to stdout in agent-readable format close the loop between data and action. The weekly review script doesn't just tell me what happened -- it references my goals and identifies which key results are on track, which are behind, and what to prioritize next week. The scripts read from the same files the agent reads during normal operation, so there's no data duplication or synchronization problem. 
 
After running the weekly review, the agent has everything it needs to update `todos.md` for next week, adjust `goals.yaml` progress numbers, and suggest content topics that align with underperforming key results. The review isn't a report -- it's the starting point for next week's planning. The automation creates a feedback loop: goals drive content, content drives metrics, metrics drive reviews, reviews drive goals.
 
5) WHAT I GOT WRONG AND WHAT I'D DO DIFFERENTLY
I over-engineered the schema first pass. My initial JSONL schemas had 15+ fields per entry. Most were empty. Agents struggle with sparse data -- they try to fill in fields or comment on the absence. I cut schemas to 8-10 essential fields and added optional fields only when I actually had data for them. Simpler schemas, better agent behavior.
The voice guide was too long at first. Version one of `tone-of-voice.md` was 1,200 lines. The agent would start strong, then drift by paragraph four as the voice instructions fell into the lost-in-middle zone. I restructured it to front-load the most distinctive patterns (signature phrases, banned words, opening patterns) in the first 100 lines, with extended examples further down. The critical rules need to be at the top, not the middle.
Module boundaries matter more than you think. I initially had identity and brand in one module. The agent would load my entire bio when it only needed my banned words list. Splitting them into two modules cut token usage for voice-only tasks by 40%. Every module boundary is a loading decision. Get them wrong and you load too much or too little.
Append-only is non-negotiable. I lost three months of post engagement data early on because an agent rewrote `posts.jsonl` instead of appending to it. JSONL's append-only pattern isn't just a convention -- it's a safety mechanism. The agent can add data. It cannot destroy data. This is the most important architectural decision in the system.
 
6) THE RESULTS AND THE PRINCIPLE BEHIND THEM
The real result is simpler than any metric. I open Cursor or Claude Code, start a conversation, and the AI already knows who I am, how I write, what I'm working on, and what I care about. It writes in my voice because my voice is encoded as structured data. It follows my priorities because my goals are in a YAML file it reads before suggesting what to work on. It manages my relationships because my contacts and interactions are in files it can query.
The principle behind all of it: this is context engineering, not prompt engineering. Prompt engineering asks "how do I phrase this question better?" Context engineering asks "what information does this AI need to make the right decision, and how do I structure that information so the model actually uses it?"
The shift is from optimizing individual interactions to designing information architecture. It's the difference between writing a good email and building a good filing system. One helps you once. The other helps you every time.
 
The entire system fits in a Git repository. Clone it to any machine, point any AI tool at it, and the operating system is running. Zero dependencies. Full portability. And because it's Git, every change is versioned, every decision is traceable, and nothing is ever truly lost.
 
Muratcan Koylan is Context Engineer at Sully.ai, where he designs context engineering systems for healthcare AI. His on-source work on context engineering (8,000+ GitHub stars) is cited in academic research alongside Anthropic. Previously AI Agent Systems Manager at 99Ravens AI, building multi-agent systems handling 10,000+ weekly interactions.
Framework: [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
