---
source: https://x.com/BrainsAndTennis/status/2065190286519906657
captured: 2026-06-12T10:11:23.632350+00:00
capture: xdk
type: kb/sources/types/snapshot.md
tags: [x-article]
status_id: 2065190286519906657
conversation_id: 2065190286519906657
post_count: 13
---

# Building a Good Vertical Agent

Author: @BrainsAndTennis
Post: https://x.com/BrainsAndTennis/status/2065190286519906657
Created: 2026-06-11T21:51:48.000Z

How do you build an agent that actually wins in a domain — one customers pick because it's better?
The basics of an agent have been standardized over the past year: it's a while-loop around a model that calls tools until the task is done. Give it a filesystem, a shell, and let it do most things through that. You can write it in an afternoon, and most people have. Everyone can build an agent — it really isn't that hard, and, as I'll spell out, it isn't that deep either. What separates a good one from a toy isn't cleverness; it's a real understanding of your domain and the patience to do some tedious, careful work in the few places that matter.
I've spent almost a year now building the Shortcut agent, which is widely considered the most accurate spreadsheet agent around — it's deployed inside three of the largest five multi-strategy hedge funds, where being wrong is expensive and nobody grades on a curve. We don't have Microsoft's or Anthropic's distribution. What we have is that the agent is right more often, and in this domain that has been the single most compelling reason customers pick us. So agent performance is the question I think about all day.
And here's the gap I keep running into: plenty is written about building agents, but few about building smart ones. Look at how much the field varies on something as basic as tool count — Codex and Claude Code ship ~30 tools each; Pi ships 7. When popular agents disagree 4x on the most basic design question, it's a tell: there's no agreed-on principle. So I'm sharing mine, from a year of building one, to demystify the process for anyone building their own.
Here it is: a smart agent is a compression of its task distribution. The rest of this is just what that means, and what it forces you to build.
It all comes down to context compression
Assume you don't own the environment and you didn't train the model. Then three things are yours to design — the system prompt, the tools, and the artifacts (skills, curated docs, references) — and they're all the same thing: the agent's context.
So the game is simple to state. With the model fixed, accuracy is a function of context quality: bloated context buries the signal, missing context forces guessing, and both cost you accuracy. And accuracy is what you're selling — the relationship isn't linear, a task at 99% instead of 95% is generally more than the 5x in error reduction.
But your users don't bring you a uniform distribution of problems to solve. They bring you a long tail:
 
The agent has to handle all of it. But it cannot hold the union of everything in context at once — that's the bloated-prompt failure mode. So the real objective is sharper than "have everything available": minimize the context spent per task, averaged over the task distribution.
This is exactly the problem a CPU faces. A program might touch gigabytes of data, but the storage right next to the processor is tiny — so computers stack memory in tiers: a small, instant cache (L1), bigger-and-slower ones below it (L2, L3), then main memory and disk. It works because access is long-tailed too: keep the hot set in the fast tier, reach down to the slow tiers only for the rare stuff. A "cache miss" is when what you need isn't in the fast tier and you pay to fetch it from a slower one — exactly the cost you're avoiding on the common path.
Agents have the same shape, so borrow the same structure. Build your context as L1 / L2 / L3.
 
And here is the law that governs every decision inside this hierarchy: almost every optimization trades compression of information against speed of discovery.
Put something in L1 and it's instant, but it costs prompt tokens on every single task whether it's used or not. Push it to L3 and it costs nothing until needed — but then it costs several tool calls to find. Your job is to place each capability at the tier that minimizes total cost across the distribution. That's the whole craft. Let me make it concrete with the domain I know best.
Aside: one tool, not thirty
Before the hierarchy, the substrate. Every spreadsheet capability I'm about to describe — every read, every write, every curated lookup — is code executed under a single tool.
 
The agent writes code; the code calls our functions; the functions touch the sheet. There is no read_range tool, no write_range tool, no make_chart tool. There is one tool, and the API lives inside the code.
Why? Because model accuracy degrades as you add tools. That's been consistent in our own experiments, and the effect was larger than I'd assumed going in. Every tool you add is more schema in the prompt, more surface to confuse, more ways to pick the wrong one, especially if the tools occupy overlapping responsibilities. A single execute_code tool collapses all of that into one decision — write code — and lets the model compose capabilities with the full expressive power of a programming language or DSL instead of stitching together rigid tool calls (More on this in a future post.)
This matters for the hierarchy because it means all three cache tiers are reachable from the same place: the model is always writing code, and L1/L2/L3 are just which functions it knows it can call, and how much work it had to do to find them.
L1 — the bread and butter: reading and writing cells
This is the 80%. If reading and writing cell ranges isn't excellent, nothing else matters. So this is where we've spent absurd, disproportionate effort. Look at what a single getCellRange actually does.
Reading a range is an act of compression
A naive range read returns a grid of values. Ours returns a compressed, semantically enriched snapshot designed to maximize signal per token. 
Reading a 200-row revenue table where the last column is Units × Price:
 
Three things are happening.
First, formula aliasing. A 500-row column of =A2*B2, =A3*B3, … is 500 near-identical formulas. We normalize each formula to R1C1 form — so =A2*B2 and =A3*B3 both become =RC[-2]*RC[-1] — count the patterns, and any pattern that appears more than ten times collapses to a short alias like F1. The model sees F1 repeated plus one legend line, instead of 500 formulas. Big token savings, zero information loss.
Second, free row and column context. When you read C5:E20, what do those bare numbers mean? We scan leftward for the row labels and upward for the header row (picking the header by voting on which nearby row has the most text cells) and attach them, so the model gets Region | Q1 | Q2 and North America | … for free and never has to guess what a grid of numbers represents.
Third, style compression. Formatting is information too — a bold red cell with a 0.00% number format is telling you something — but listing the full style of every cell would swamp the values. So we group cells by identical style, collapse each group to its connected range, and print one line per group: the range, the cell count, and a compact description. Repeated formatting costs one line no matter how many cells share it, capped at the ten most common styles.
Every cell is address:value, with its formula appended in parentheses (aliased to (F1) here). Six hundred formulas became one legend line. Four hundred styled cells became two lines. And the header row the model never explicitly asked for is right there at the bottom. That's the whole table, losslessly, in a fraction of the tokens a raw dump would cost.
Every one of these is the compression-vs-discovery tradeoff, won decisively for the common case.
Writing cells: tell the model what it actually changed, and what looks wrong
Writing is harder than it looks, because a single execute_code call can change hundreds of cells, and the agent needs to know what happened without re-reading the whole sheet. So after the code runs, we hand back a structured diff of every cell that changed — and, just as importantly, we compress and triage it.
Here's a real write and the feedback it produces. The code:
 
The diff that comes back:
 
Two kinds of compression are doing the work here.
First, the diff is grouped and sampled, not dumped. Changed cells are grouped by sheet and row, each row shown as a column range with a count (Row 2 (D): 1 cells), and only a deterministic sample of cells per row and rows per section is printed, with "… and N more" tallies for the rest. Two hundred writes don't become two hundred lines; they become a handful, and the agent still knows the totals.
Second, and more useful, the diff is categorized. It doesn't just report what changed — it triages each change. Clean writes land under "Changed without issues." Anything that looks suspicious — an invalid formula like #REF!, an untagged hardcoded number, a hardcoded number buried inside a formula, an implausibly large percentage — gets pulled into a "Cells that need review" section, and the worst offenders are flagged MUST FIX. That #REF! in row 57 would be trivial to miss in a wall of two hundred green diffs; here it's surfaced at the top with a label. The feedback loop isn't "here's what changed," it's "here's what changed, and here's the part you probably got wrong" — a built-in linter on the agent's own edits.
L1 in one line: the operations on the steep part of the curve get feature-engineered, token-compressed, consequence-reporting wrappers that live in the prompt forever. They're expensive to build, and you build them anyway, because the agent pays the cost on every task.
L2 — curated English, on demand
You cannot put everything in L1. Conditional formatting, pivot tables, charts, data validation, copy/move semantics — each is important, each shows up a few times a session, and each has enough surface that documenting it in the system prompt would bloat every task that doesn't use it. Classic L2.
So we wrote curated capability specs in English, fetched on demand. The model calls, from inside its code:
 
These aren't dumps of type signatures. They're hand-written prose — a few hundred lines each — that describe the canonical way to accomplish the task, including the knowledge the raw API will never give you. Take the pivot-table spec. It doesn't just list methods; it teaches the whole recipe, in the right order:
 
and it bakes in the things you would otherwise learn only by failing repeatedly: that you must suspendLayout()/resumeLayout() around a batch of changes or the table rebuilds on every call; that a value field's aggregation has to be passed as a raw integer (8 for sum) because the friendly enum doesn't exist at runtime. None of that is a quirky footgun — it's the actual shape of doing pivots correctly, written down once by someone who already paid for it.
That's institutional knowledge encoded as a cache line. A raw API reference would give you the method names and leave you to discover the ordering and the runtime gaps yourself. A curated spec hands you the working pattern. The model reads ~1,000 tokens, gets the canonical recipe and the constraints, and writes correct code on the first try.
The key property: this costs zero tokens until the task needs it. A task that never touches pivots never pays for the pivot docs. One console.log is the entire discovery cost — a single cache miss, served fast.
The same idea, for executable tools
L2 isn't only for docs. We apply the identical pattern to deferred tools — web_search, web_crawl, create_website, etc. Their schemas don't sit in the prompt. Instead there's a meta-tool wall:
 
The set of fetched tools is, literally, a session-scoped cache. The model loads a schema once, and from then on it's resident. Same compression-vs-discovery tradeoff, same resolution: keep the prompt small, pay a one-step miss when you actually need the capability. This is the same idea as deferred tools on Claude but we're not locked to one vendor's tool-loading feature to get the behavior.
L3 — the raw tome, and the skill that maps it
Then there's the long tail: the one obscure thing we never wrapped and never wrote a spec for. You can't anticipate it — by definition. But the agent still has to be able to get there, or it hits a wall and fails the task. Concretely, this is where requests like these end up:
"Add a sparkline to each row summarizing its trend" — sparklines are a real but rarely-touched API surface.
"Set the chart's secondary axis to log scale and recolor just the third series" — a chart property three levels deep that no curated spec bothered to cover.
"Insert a hyperlink from this cell to that named range, and group these shapes" — drawing/shape/hyperlink corners nobody asked about until now.
So L3 is the complete raw API — the entire Office.js surface (Excel plugin) or the entire SpreadJS surface (Shortcut web), dumped to disk. It's a machine-generated reference that is 70k lines long. It contains everything. It's also completely unusable as prompt context — you'd never paste it in.
The trick: you give it a skill — a short map that teaches it how to mine the tome with bash:
 
The skill is ~100 lines. It says: here's the structure, here's how each method and type entry is shaped, here's the grep recipe for each kind of question. With it, the agent goes from "tens of thousands of lines I can't read" to "the 3-6 greps that surface exactly the signature I need." That's the L3 access cost — real, but bounded, and only paid by the rare task that reaches this deep.
And the system prompt makes the escape hatch explicit, so the model knows the path exists and when to take it:
API HIERARCHY — There are 2 levels of API capability. Wrapped API: convenience functions; some listed directly, others via getAPIInfo(...). NEVER guess — read the docs in FULL. Raw API: use when the wrapped API doesn't cover your need… If the wrapped API can't do it, use the raw API — don't compromise.
That last clause is the whole point of L3. The agent should never be stuck. It can miss in L1, drop to L2, and if even the curated spec is silent, descend into the raw tome and still come out with the answer in a sane number of calls.
How the prompt budget actually splits
It's worth looking at where the tokens go, because the hierarchy shows up directly in the system prompt's shape.
The bulk of the prompt is L1 — on the order of a few hundred lines. Core read/write operations, the execute_code contract, the key types and the handful of methods the agent uses on essentially every task, plus the execution and safety guidelines. This is the part that's resident on every single call, so it's also the part we fight hardest to keep tight.
L2 is a thin slice on top — roughly 50 lines. It isn't the specs themselves; it's a curated allowlist of the "blessed" methods and the pointers that tell the agent the getXInfo(...) specs exist and when to reach for them. The specs' actual content stays out of the prompt until a console.log pulls it in.
L3 is essentially 5 lines, the name and description of the skill.md, and other references scattered elsewhere. The raw reference — 70k lines — lives entirely on disk and never touches the prompt. All that's resident is the short skill file and the one line in the API-hierarchy section pointing at it.
So the budget mirrors the frequency curve: most of the prompt is spent on the 80% case, a little on signposting the 15%, and almost nothing on the long tail — which is exactly the allocation the cache-hierarchy framing predicts.
The recipe, ported to your domain
Spreadsheets are just my example. The structure transfers to any domain. The compression in those system prompts and curated specs is really an encoding of the distribution of your users and the tasks they do — and you, in your domain, understand that distribution better than anyone. So your job is three questions:
1. What do you wrap into L1? The bread-and-butter operations on the steep part of the frequency curve. Make them brutally token-efficient and fast, and make them report consequences. Spend disproportionate effort here — the agent pays this cost on every task.
2. What do you defer to L2? The important-but-occasional capabilities. Write them as curated, English, gotcha-aware specs reachable in one discovery step. Encode the canonical recipe and the constraints, not just the signatures.
3. What is your escape hatch (L3)? The raw, complete substrate — plus a skill that teaches the agent to mine it. It doesn't have to be ergonomic. It has to be reachable, complete, and findable in a bounded number of steps. The agent must be able to — and will — eventually find the right information.
Get those three placements right and you've built an agent that is fast on the common case, capable on the occasional one, and never truly stuck on the rare one — all while keeping context small enough that the model stays sharp.
The hierarchy doesn't disappear — it moves
One closing observation. What counts as L1 is not fixed; it drifts with model strength.
Early, weak models needed tiny, single-purpose tools and everything spelled out. Today's models can absorb a larger L2 spec in one shot and reason over more raw L3 detail without choking. So as models improve, yesterday's L3 becomes tomorrow's L2, and yesterday's L2 collapses into L1. The agent's responsibility expands outward; the tiers slide down a level.
But the hierarchy itself never goes away — because context will always be scarce relative to everything you could put in it, and noise will always cost you accuracy. There is no model so large that "put the right thing in front of it at the right time" stops mattering.
Bigger context windows tempt people to paste in more. The better instinct is the one CPUs settled on decades ago: summaries in cache, details on demand, the raw substrate as the last resort. Build your agent's context like a memory hierarchy, and accuracy follows.
