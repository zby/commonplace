# Explore: Where does the memory system end and the project begin?

Workshop: [agent-memory-design](./framing.md)

## 1. The boundary, artifact by artifact

The framing proposes: "the memory system stores what project artifacts don't preserve." Let's stress-test this against every artifact type in a typical software project.

### Code

Code preserves *what* the system does. It does not preserve: why this approach was chosen over alternatives, what was tried and abandoned, what subtle invariants the author was maintaining in their head, what the code *almost* was. The memory system's contribution is **decision provenance** and **negative results**. Example: a function uses a retry loop with exponential backoff instead of a circuit breaker. The code says "retry loop." The memory system says "we tried a circuit breaker in session 47 but it interacted badly with the connection pool; the retry loop is a deliberate fallback."

### Tests

Tests preserve *what invariants hold*. They don't preserve: why this invariant was worth testing, what bug motivated the test, what the failure mode looked like before the fix. The memory system adds **failure genealogy** — the chain from bug discovery to test creation. This matters because when someone later asks "can I delete this test, it seems redundant?", the answer depends on whether the original failure mode is still possible.

### Documentation (README, API docs)

Docs preserve *how to use the system*. They don't preserve: what the docs used to say and why they changed, what questions users actually asked that the docs failed to answer, what tradeoffs shaped the documented API surface. The memory system adds **documentation debt signals** — patterns in session logs where the agent or user had to explain something the docs should have covered.

### CI configuration

CI config preserves *what checks run*. It doesn't preserve: why a check was added (the incident that motivated it), why a check was removed (the false-positive rate that killed it), the evolution path from "no CI" to the current setup. The memory system adds **operational rationale**.

### CLAUDE.md / agent instructions

This is the interesting edge case. CLAUDE.md is *already* a memory artifact — it stores routing knowledge the agent needs every session. The boundary question: what belongs in CLAUDE.md vs. the broader memory system?

Proposed distinction: **CLAUDE.md is compiled routing; the memory system is the source.** CLAUDE.md holds the distilled, always-load instructions. The memory system holds the session experiences that revealed what CLAUDE.md needs to say. When a user corrects the agent three times for the same mistake, the correction pattern lives in session logs (memory system) and eventually graduates to a CLAUDE.md entry (project artifact). CLAUDE.md is the deployment artifact; the memory system is the learning substrate.

This means CLAUDE.md and the memory system have a producer-consumer relationship, not a boundary. The memory system feeds CLAUDE.md; CLAUDE.md is one of several graduation destinations.

### ADRs

ADRs are manually authored distillations of decisions. The framing already covers this well: session logs contain the raw deliberation, ADRs contain the conclusion. The memory system *complements* ADRs by preserving what ADRs discard — the alternatives explored, the dead ends, the context that made the decision feel obvious at the time.

But there's a subtlety: **ADRs are also triggers for memory system queries.** When someone reads an ADR and asks "but why didn't we just do X?", the answer is almost always in the session logs. An ADR that links back to its source sessions is more useful than one that stands alone.

### Changelogs

Changelogs preserve *what changed and when*. They don't preserve why or how. Thin boundary — changelogs are almost entirely derivable from commit history plus memory system. A changelog entry like "switched from SQLite to PostgreSQL" becomes meaningful only when the memory system can answer "why?"

### Issue trackers (Jira, GitHub Issues, project boards)

Issues preserve *what work was planned, assigned, and completed*. They often contain surprisingly rich decision context — the discussion thread on a GitHub issue may record why an approach was chosen, what alternatives were raised, and what constraints shaped the solution. This makes issues an interesting boundary case: they're durable project artifacts, but they also function as memory artifacts. The boundary question: what does the memory system add on top of issue history?

Two things. First, **cross-issue patterns.** An individual issue captures one decision or task, but the memory system can detect that issues #34, #78, and #112 all stem from the same architectural weakness — a pattern invisible when issues are viewed one at a time. Second, **context that didn't make it into the issue.** Much of the deliberation happens in sessions, in Slack, or in the agent's reasoning before it even opens an issue. The issue records the conclusion; the memory system records the path to the conclusion. Issues are the closest existing artifact type to a memory system — they already store rationale, provenance, and context — but they're structured around units of work, not units of knowledge. The memory system organizes the same material around what was learned.

### Code comments

Code comments are inline memory — context that the author judged belongs *next to* the code. The boundary question: when does something belong in a code comment vs. the memory system?

Proposed heuristic: **if the knowledge is load-bearing for understanding the adjacent code, it's a comment. If it's load-bearing for understanding the project's trajectory, it's memory.** A comment saying `// O(n^2) but n < 100 so it doesn't matter` is about this code. A memory entry saying "we profiled the sort and it's not a bottleneck; don't optimize it" is about the project's priorities.

### Summary: where the framing breaks down

The "stores what project artifacts don't preserve" principle is *necessary but not sufficient*. Two problems:

1. **Overlap zone.** Some knowledge legitimately belongs in both places. An ADR is a project artifact *and* a memory artifact. A CLAUDE.md entry is a project artifact *and* routing knowledge derived from memory. The boundary isn't a line — it's a gradient with artifacts that have a foot in both worlds.

   The overlap is structural, not accidental. Consider a code comment that says `// Retries capped at 3 — see incident #412`. The comment is a project artifact (it lives in the codebase, gets versioned, gets reviewed). But it's also memory — it encodes a decision, points to a historical event, and would lose meaning if the incident context disappeared. A test that was written in response to a specific bug is the same: the test is a project artifact, but the connection between the test and the bug it guards against is memory-layer knowledge that the test file alone doesn't preserve. The overlap zone consists of artifacts that *partially* capture process knowledge but incompletely — they record the conclusion without the deliberation, the fix without the diagnosis, the convention without the three corrections that established it. The memory system doesn't duplicate these artifacts; it holds the surrounding context that makes them intelligible.

2. **The aspiration gap.** The principle describes the steady state, but much project knowledge *should* be in project artifacts and isn't. Undocumented conventions, tribal knowledge, implicit architectural invariants — these aren't in project artifacts because nobody wrote them down, not because they don't belong there. The memory system captures them by default (they appear in session logs), but their proper home is elsewhere. The memory system is a safety net for project artifacts that haven't been written yet.

   The gap is wider than it looks. Consider: a team knows that the `payments` module must never be deployed independently of `billing` because of a subtle data-consistency dependency. This constraint lives in the heads of senior engineers. No test enforces it, no ADR documents it, no CI check catches it. When an agent works on the project, it has no way to discover this constraint except by violating it and being corrected. The memory system captures the correction, but the constraint's *proper* home is a test, or a deployment guard, or at minimum an architectural note. The aspiration gap includes not just knowledge that hasn't been written down, but knowledge that *can't easily be extracted* — implicit performance expectations ("this endpoint should respond in under 200ms"), aesthetic preferences ("we prefer composition over inheritance in this codebase"), and contextual judgments ("this area of the code is fragile, tread carefully"). These are hard to articulate as discrete artifacts because they're distributed across many decisions rather than concentrated in one. The memory system's value is that it accumulates evidence of these implicit constraints through repeated observations, even when no single observation is sufficient to codify them.

A better formulation: **The memory system is the substrate from which project artifacts are distilled. It preserves everything; project artifacts are curated projections of it.**

## 2. Graduation pathways

When does a pattern in session logs become a durable artifact?

### Session log -> ADR

**Trigger:** A decision was debated across multiple sessions, or a past decision was questioned and the answer required reconstructing context that wasn't documented.

**Concrete signal:** The agent or user says something like "we discussed this before" or "why did we decide X?" and the answer requires searching through session history. That search cost is the graduation signal — if finding the reasoning was expensive, it should be distilled.

**Graduation process:**
1. Identify the sessions where the decision was made
2. Extract: the question, the alternatives, the constraints, the chosen option, the reasoning
3. Write the ADR, linking back to source sessions for provenance
4. The session logs remain as the detailed record; the ADR is the navigable summary

**Example:** Sessions 12, 15, and 23 all touch on whether to use a monorepo or multi-repo. Session 23 finally commits to monorepo. An ADR captures the conclusion; the sessions preserve the full deliberation.

### Session log -> Documented procedure

**Trigger:** The same workflow appears in 3+ sessions, possibly with slight variations that converge over time.

**Concrete signal:** Repetition detection. The agent performs a sequence of steps (e.g., "check CI status, pull latest, run local tests, then push") that recurs. Or the user gives the same multi-step instruction repeatedly.

**Graduation process:**
1. Identify the recurring sequence across sessions
2. Extract the canonical version (most recent, or the one with fewest corrections)
3. Write the procedure, noting which steps vary and which are fixed
4. Optionally: turn it into a skill or script if the procedure is deterministic enough

**Example:** In sessions 8, 14, 22, and 31, the user asks the agent to "do the release process." Each time, the agent figures out the steps from scratch (or loads the same context). After the fourth occurrence, the pattern graduates to a documented release procedure.

### Session log -> Linting rule or test

**Trigger:** A constraint was violated repeatedly, and each violation was caught and corrected manually.

**Concrete signal:** The user corrects the agent for the same mistake 2+ times. Or the agent itself catches an error it's seen before.

**Graduation process:**
1. Identify the recurring correction pattern
2. Determine whether the constraint is expressible as a deterministic check
3. If yes: write a linting rule or test that catches the violation automatically
4. If no: write a documented convention (CLAUDE.md or equivalent) that makes the constraint explicit

**Example:** The user corrects the agent three times for committing files with trailing whitespace. First correction: session log. Second correction: the memory system surfaces "you've been corrected for this before." Third correction: graduation to a pre-commit hook that strips trailing whitespace. The constraint moves from implicit (human notices) to explicit (automated check).

This is the constraining gradient in action: observation -> documented convention -> automated check -> deterministic enforcement.

### Session log -> CLAUDE.md entry

**Trigger:** The agent repeatedly needs the same routing or context knowledge at session start, and it's not currently in the always-loaded context.

**Concrete signal:** The first few messages of multiple sessions involve the same orientation ("this project uses X framework," "always run Y before committing," "the main branch is called Z"). If the agent asks the same clarifying question across sessions, the answer belongs in CLAUDE.md.

**Graduation process:**
1. Identify the recurring orientation pattern
2. Distill it into a concise, imperative instruction
3. Add to CLAUDE.md (or equivalent always-loaded context)
4. The memory system no longer needs to surface this per-session; CLAUDE.md handles it

**Example:** In five consecutive sessions, the user reminds the agent that this project uses pnpm, not npm. The correction graduates from session-level to CLAUDE.md: "This project uses pnpm. Do not use npm."

### Session log -> Code comment

**Trigger:** A piece of context was needed to understand or modify a specific code location, and it wasn't obvious from the code itself.

**Concrete signal:** The agent or user had to explain *why* a piece of code works the way it does, and the explanation would help anyone encountering that code in the future.

**Graduation process:**
1. Identify the explanation
2. Determine whether it's specific to the code location (comment) or general to the project (memory/docs)
3. If specific: add as a code comment adjacent to the relevant lines
4. If general: route to docs or memory

**Example:** The agent asks why a function ignores the first element of a list. The user explains it's a header row artifact from the CSV parser. This graduates to a comment: `# First element is CSV header row, skip it`.

### The graduation meta-pattern

A useful way to model the shared structure:

1. **Observation** — something happens in a session (a decision, a correction, a recurring pattern)
2. **Accumulation** — the memory system records it
3. **Recognition** — the pattern is noticed (by repetition count, by search cost, by correction frequency)
4. **Distillation** — the raw observations are compressed into a durable artifact
5. **Placement** — the artifact goes to its proper home (ADR, procedure, test, CLAUDE.md, comment)
6. **Provenance** — the session logs remain as source material, linked from the graduated artifact

Recognition is the bottleneck. Automated recognition is possible for some signals (repetition count, correction frequency) but hard for others (when a decision becomes "load-bearing enough" to warrant an ADR). This maps directly to the agency trilemma from the comparative review: high-quality graduation decisions require context that costs reasoning budget.

## 3. Relationship to existing manual distillation processes

Three possible relationships: complement, replace, feed.

**The answer is "feed into" — the memory system provides raw material for manual distillation processes, and over time automates the triggers that tell you when to run them.**

Consider how ADRs work today without a memory system:
1. Someone notices a decision was made
2. They remember (or reconstruct) the reasoning
3. They write the ADR

With a memory system:
1. The decision is captured in session logs automatically
2. The memory system detects that a decision was debated across sessions (trigger)
3. It surfaces the relevant sessions and extracts the key points (raw material)
4. A human (or agent) writes the ADR (manual distillation, but with dramatically lower cost)

The memory system doesn't replace the human judgment in step 4 — deciding what matters, what to emphasize, what the consequences are. But it eliminates the reconstruction cost in step 2 and automates the trigger in step 1.

The same pattern applies to WRITING.md conventions. Today: someone notices a convention is needed, writes it up. With memory: the system detects recurring corrections around the same issue and flags "this might be a convention worth documenting." The human still decides whether it is.

This is the complement-to-feed spectrum:
- **Short term:** complement. The memory system is a better notebook — it captures what manual processes miss.
- **Medium term:** feed. The memory system provides triggers and raw material, making manual processes cheaper to run.
- **Long term (speculative):** partial automation. For graduation pathways with clear signals (correction frequency -> linting rule), the system can propose the graduated artifact. For pathways requiring judgment (when to write an ADR), it can only flag and assist.

## 4. Reach and the boundary

The KB's reach concept (from Deutsch via the ephemerality note) maps cleanly onto the boundary question.

**High-reach knowledge wants to be in the library layer.** "Systems that optimize for normal-load efficiency sacrifice overload resilience" applies to many contexts. It belongs in a permanent note, not in session logs.

**Low-reach knowledge can stay in session logs.** "The bug in PR #247 was caused by a race condition in the connection pool" is specific to that PR. It doesn't need to graduate — the PR itself and the fix commit carry the essential information.

**But here's the tension: you often can't tell the reach of an observation when you first make it.** The connection pool race condition might be a one-off (low reach), or it might be the third instance of a pattern where async resource pools need explicit shutdown ordering (high reach). You only discover the reach by accumulating instances.

This creates a two-phase dynamic:
1. **Accumulate promiscuously** — store everything, including low-reach observations, because you don't know what's low-reach yet
2. **Graduate based on revealed reach** — when multiple low-reach observations cluster around the same structural pattern, the pattern has high reach and should graduate to the library

The reach-revealing mechanism is exactly the recognition step from the graduation meta-pattern. Signals that an observation has more reach than it appeared:
- It recurs in a different context (same pattern, different module)
- It explains a previously mysterious behavior elsewhere
- Someone asks a question whose answer depends on it
- A new observation directly contradicts it (contradiction implies both have reach — they're making claims about the same territory)

The ephemerality note's boundary — "ephemerality is safe where embedded operational knowledge has low reach" — applies directly: session logs are safely ephemeral (can be archived, compressed, eventually deleted) when the operational knowledge they contain has low reach. But they must be retained long enough for reach to be revealed, which might take months.

### The aggregation problem

Low-reach observations that reveal high-reach patterns when aggregated is the hardest case. Consider:
- Session 12: "The deploy failed because the staging config wasn't updated"
- Session 28: "The migration failed because the test env config was stale"
- Session 45: "The feature flag rollout broke because the production config wasn't in sync"

Each is low-reach (specific incident). Together they reveal a high-reach pattern: "this project's configuration management doesn't have a single source of truth, and every environment drift is a potential failure." That pattern should graduate to an ADR or architectural note.

But detecting this cluster requires something the current memory model doesn't address: **cross-session pattern matching that looks for structural similarity, not surface similarity.** The three incidents above don't share keywords — they share a causal structure. This is where the agency trilemma bites hardest: detecting structural patterns across sessions requires deep reasoning (expensive), and the value is speculative (you're betting the pattern has reach before you've confirmed it).

## 5. Different project types

### Software project

The boundary is clearest here because software projects have the richest artifact ecosystem (code, tests, docs, CI, ADRs, changelogs). The memory system fills the gaps between these artifacts — decision provenance, negative results, implicit conventions.

**Graduation is mostly into existing artifact types.** The destination slots (ADR, test, linting rule, doc) already exist. The memory system's job is to detect when graduation should happen and lower the cost of doing it.

### Research project

The artifact ecosystem is thinner: papers, data, notebooks, maybe a literature database. The boundary shifts dramatically — more knowledge lives in the memory system because there are fewer project artifacts to graduate into.

**Key difference: negative results are first-class.** In software, "we tried X and it didn't work" is useful but secondary. In research, "we tried X and it didn't work, here's why" is a primary finding. The memory system's role in preserving negative results becomes central, not supplementary.

**Graduation pathways are different:** session observations -> hypotheses -> experiments -> findings -> paper sections. The intermediate representations (hypotheses, experiment designs) don't exist in the software artifact taxonomy.

### Writing project

The boundary is blurriest. The "project artifacts" are drafts, and drafts are themselves evolving memory — each version preserves decisions about structure, voice, emphasis. The memory system overlaps heavily with the draft history.

**What the memory system uniquely adds:** editorial reasoning ("I cut this section because it slowed the pace"), reader feedback patterns ("three people were confused by the same passage"), and voice calibration ("this draft sounds too formal, last week's was better"). These are meta-knowledge about the writing process, not part of the written artifact.

**Graduation is often into the draft itself** rather than into a separate artifact. A decision about structure graduates when you actually restructure the draft. The memory system's role is to preserve the *reasoning* behind structural choices so you can revisit them.

### Personal productivity system

The project/memory boundary almost disappears. The "project" is your life, and most knowledge about how you work is memory-system knowledge by nature — preferences, habits, recurring patterns, what works and what doesn't.

**CLAUDE.md becomes the dominant graduation destination.** In a personal system, routing knowledge (how you want things done) is the most valuable artifact type. The graduation pathway is: observed preference -> confirmed preference (seen across sessions) -> CLAUDE.md entry.

**The reach concept behaves differently.** In a personal system, even low-reach knowledge (this specific meeting has this specific preparation ritual) can be high-value because the system's purpose is to serve one person's specific needs, not to produce transferable insights.

## Tensions and edge cases

**The bootstrap problem.** A new project has no session history, so the memory system is empty. But it also has few project artifacts, so the boundary is undefined. Where does the memory system start providing value? Likely: after 5-10 sessions, when patterns begin to emerge. Before that, CLAUDE.md entries written by hand serve the same role.

**The staleness asymmetry.** Project artifacts go stale slowly (code still runs even if the docs are outdated). Memory system knowledge can go stale fast (a preference expressed in session 5 might be reversed by session 15). This means the memory system needs *more* aggressive staleness detection than project artifacts, not less — which runs counter to the "store everything" premise. Resolution: store everything, but weight recency in retrieval. Old preferences are evidence, not policy.

**The graduation cost.** Every graduation creates a maintenance obligation. An ADR must be kept current. A linting rule must be updated when conventions change. A CLAUDE.md entry must be revised when the project evolves. The memory system imposes no such obligation — session logs are append-only. This means premature graduation is worse than late graduation. Better to have the knowledge in session logs (cheap to store, no maintenance) and graduate only when the retrieval cost exceeds the maintenance cost.

**Who graduates?** In a human-only system, graduation is a conscious human act. In an agent-assisted system, the agent can propose graduations but probably shouldn't execute them unilaterally — especially for high-reach artifacts (ADRs, architectural notes) where judgment matters. The agent's role is detection and drafting; the human's role is approval and refinement. For low-reach, high-confidence graduations (adding a pre-commit hook for a repeatedly-violated convention), agent autonomy is more defensible.

**The double-entry problem.** Once knowledge graduates from the memory system to a project artifact, you have it in two places. Does the memory system entry become provenance-only (linked but not surfaced in search)? Or does it remain active? If active, you risk contradictions when the project artifact is updated but the session log isn't. Proposed resolution: graduated knowledge in session logs gets a "graduated-to" marker that deprioritizes it in retrieval while preserving the link for provenance.
