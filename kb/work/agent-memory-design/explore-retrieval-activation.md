# Exploration: How does the memory system find and activate the right information?

This explores the retrieval and activation layer of a store-everything agent memory system. The framing assumes storage is cheap and complete (all session logs, all artifacts). The hard problem is finding the right information at the right time under bounded context. Grounded in the KB's activation gap analysis, action-capacity framing, elicitation strategies, statelessness constraint, the comparative review of 11 memory systems, and the [axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) role distinction.

## Retrieval divides by role, not by content

The central organizing move is to split retrieval by the role the retrieved artifact will play. A single store can serve both roles, but the access patterns differ:

- **Knowledge-role retrieval** answers questions at consumption time. The consumer is the agent or user looking up a fact or navigating to understand a decision. Standard RAG plus articulated links cover this.
- **System-definition-role activation** injects policy when a situation matches. The consumer is the agent about to act. The "retrieval" is a watcher-plus-trigger, not a query.

Most of the difficulty in this section is system-definition activation — the knowledge retrieval side mostly reuses patterns the KB already documents (search + navigation). The typed cue indexes, priority arbitration, and commitment mechanisms below are all machinery for the system-definition role. The knowledge-role flow sits on top as a less novel layer.

---

## 1. Retrieval methods that serve action-capacity

The action-capacity note reframes the problem: the memory system doesn't just answer questions, it makes agent actions more competent across execution, classification, communication, planning, and pattern recognition. QA retrieval (embed query, return top-k chunks) serves only one of these modes. What does retrieval look like for the others?

### Designing for the three activation stages

The activation gap note decomposes activation into cue match, priority arbitration, and commitment. Each stage has a different failure mode and a different design surface.

**Cue match: making relevant system-definition knowledge fire.** The system must connect the agent's proposed action to stored cues even when the surface terms don't overlap. This is specifically the system-definition problem — for knowledge-role retrieval, cue match is just query match and the standard approach (embedding + links) suffices. Approaches:

- *Semantic embedding search* over session logs and extracted artifacts. Standard RAG. Works for factual retrieval ("what did we decide about the API versioning scheme?").

- *Limitation of embedding search for action-relevant knowledge.* Embedding similarity fails when the connection is causal, not topical. Session 47's correction about a deployment mistake won't embed near session 312's code-writing task even though the lesson applies.

- *Typed cue indexes.* Instead of searching raw logs, extract typed cues at ingestion time. Types: `correction` (when X failed because Y, do Z instead), `preference` (user prefers A over B in context C), `precedent` (faced situation S, chose action A, outcome O), `procedure` (to accomplish G, do steps 1..n), `decision` (chose X over alternatives Y, Z because of reasoning R — see section 5 for decision event extraction). Each type has a different retrieval signature. A correction cue matches against the action the agent is about to take. A preference cue matches against the decision space. A precedent matches against the situation description. Example:
  ```
  type: correction
  trigger: "deploying without running integration tests"
  lesson: "Session 47: deployed with unit tests only, missed DB migration
           incompatibility. Always run full integration suite before deploy."
  source_sessions: [47, 52]
  ```

- *Inverse indexing by failure mode.* For corrections and negative results specifically, index by "what went wrong" rather than "what was being done." When the agent is about to take action X, the system checks: "has action X (or something structurally similar) ever failed?" This requires classifying actions into a taxonomy coarse enough to match across sessions but fine enough to be useful. Example taxonomy for a coding project: deploy, refactor, schema-change, API-design, dependency-update, performance-optimization.

**Priority arbitration: deciding what to surface when too much matches.** In a store-everything system with thousands of sessions, any given task context will match dozens of stored items. Loading them all destroys context efficiency. Approaches:

- *Recency-weighted relevance.* Recent sessions get a boost, but with a long tail. A correction from 500 sessions ago is still highly relevant if the same mistake pattern is recurring.

- *Consequence weighting.* Items whose source sessions involved corrections, user frustration, or significant rework get higher priority than routine confirmations. A plausible heuristic: if the user had to redirect the agent, that session contains more action-relevant knowledge than one where everything went smoothly. Operationally: flag sessions where the user's messages contain correction markers ("no, actually...", "that's wrong", "I meant...") and boost extracted cues from those sessions.

- *Frequency-based promotion.* If the same cue fires across multiple sessions, it's more likely to be relevant. This is ClawVault's "seen twice on different dates" heuristic applied to activation cues.

- *Budget allocation by cue type.* Reserve fixed context slots: N tokens for corrections relevant to the current task, M tokens for active preferences, P tokens for relevant precedents. This prevents any single cue type from crowding out the others.

**Commitment: getting the agent to actually use surfaced knowledge.** Even when relevant knowledge is loaded into context, the agent may ignore it in favor of its training-time defaults. The activation gap note's "expert witness" failure mode. Approaches:

- *Imperative framing.* Don't surface corrections as passive context ("previously, X failed because Y"). Frame them as instructions: "BEFORE doing X, verify Y because Z failed in session 47." The elicitation note's finding that perspective assignments outperform undirected review applies here — framing shapes activation.

- *Checkpoint insertion.* For high-consequence cue types (corrections with severe outcomes), insert explicit verification steps into the agent's task plan: "Step 3a: Check whether this deployment includes DB schema changes. If yes, review session 47 correction before proceeding."

- *Contradiction surfacing.* When the agent's proposed action contradicts a stored correction or preference, surface the contradiction explicitly rather than hoping the agent notices: "You are about to use approach A. In session 47, approach A failed because Z. The established alternative is approach B. Confirm which approach to use."

### Action-specific retrieval patterns

| Action mode | What to retrieve | Retrieval method | Role |
|---|---|---|---|
| Execution | Corrections for the action type; relevant procedures | Action-type index lookup + semantic match on task description | System-definition |
| Classification | Precedent decisions for similar items; active category definitions | Precedent index lookup by item features | System-definition (precedents as policy) or Knowledge (category definitions as reference) |
| Communication | Voice/style patterns; relationship history with the recipient | Entity-keyed retrieval (by person/channel) | System-definition |
| Planning | Past plans for similar goals; outcomes of previous approaches | Goal-similarity search + outcome-weighted ranking | Mixed — past plans are knowledge; outcome-weighted ranking generates system-definition cues |
| Pattern recognition | Historical situations resembling the current one | Situation embedding search with temporal spread | Knowledge (providing context) |

---

## 2. Pre-generating activation cues from session logs

The question-generation bottleneck says the binding constraint is whether the workflow asks the right questions. Can we flip this: instead of waiting for the right question, pre-compute the cues that future sessions should match against?

### The cue generation pipeline

After each session (or batch of sessions), run an extraction pass:

1. **Identify correction events.** Scan for user redirections, error recovery, explicit "don't do X" statements. For each, generate a trigger-lesson pair.
   - Input: session log where user says "No, don't use `datetime.now()` for timestamps in the database, use `datetime.utcnow()`. We've had timezone bugs before."
   - Output cue: `{ type: correction, trigger: "writing datetime.now() to database", lesson: "Use datetime.utcnow() to avoid timezone bugs. Source: session 47." }`

2. **Identify preference expressions.** Scan for choices between alternatives where the user expressed a preference.
   - Input: session log where user consistently chooses list comprehensions over map/filter.
   - Output cue: `{ type: preference, context: "Python collection transforms", preference: "list comprehensions over map/filter", confidence: 0.8, evidence_sessions: [23, 31, 47] }`

3. **Identify discoveries.** Scan for insights that emerged during work — "oh, it turns out that..." or conclusions reached after investigation.
   - Input: session log where debugging revealed that the ORM silently truncates strings over 255 chars.
   - Output cue: `{ type: discovery, domain: "ORM behavior", content: "SQLAlchemy String columns silently truncate at 255 chars without error", implications: ["validate string length before write", "use Text type for user content"], source_session: 89 }`

4. **Identify procedure patterns.** Across multiple sessions, detect recurring multi-step workflows.
   - Input: sessions 12, 34, 67 all follow: check out branch -> run tests -> review diff -> update changelog -> merge.
   - Output cue: `{ type: procedure, goal: "merge feature branch", steps: [...], source_sessions: [12, 34, 67] }`

### The "session 47 to session 312" bridge

The specific example from the framing: if session 47 corrected a mistake, can the system generate a cue that fires in session 312?

**Mechanism:** The correction cue from session 47 is stored with a trigger condition. In session 312, when the agent's task plan includes an action matching the trigger, the cue fires and loads the lesson into context.

Concrete example:
- Session 47: User asks agent to write a database migration. Agent writes a migration that drops a column. User corrects: "Never drop columns directly in production migrations. Add a new column, migrate data, then drop the old column in a separate migration after verifying."
- Generated cue: `{ type: correction, trigger: "database migration that removes or drops a column", lesson: "Three-phase column removal: (1) add new column + migrate data, (2) deploy and verify, (3) drop old column in separate migration. Direct column drops cause data loss if rollback is needed. Source: session 47." }`
- Session 312: Agent is asked to write a migration removing a deprecated field. The task plan includes "drop column deprecated_flag." The trigger matches. The lesson is loaded into context before the agent writes the migration.

**The matching problem** is the hard part. "Database migration that removes a column" must match "drop column deprecated_flag" despite surface differences. Approaches:

- *Action-type classification.* Classify the agent's intended action into a taxonomy. Match triggers against the classified action type, not the raw text. Both "drop column" and "remove field" classify as `schema-migration:column-removal`.

- *Embedding similarity with a low threshold.* Embed triggers and embed the current task plan. Fire any cue above a similarity threshold. Accept false positives (extra context loaded but ignored) over false negatives (relevant correction missed). This trades context efficiency for activation coverage.

- *LLM-judged relevance.* For a small set of high-consequence cues, use a cheap model call to judge: "Is this cue relevant to the current task?" This is expensive but accurate. Reserve it for corrections that had severe outcomes.

### Cue lifecycle

Cues aren't permanent. They need maintenance:

- **Consolidation.** When multiple sessions produce similar corrections, merge them into a single cue with stronger confidence and richer examples.
- **Graduation.** When a cue fires frequently and the agent consistently follows it, the lesson may belong in a more permanent artifact (a project convention, a linting rule, a documented procedure). The cue becomes a pointer to the graduated artifact.
- **Retirement.** When the codebase changes such that a cue's trigger condition is no longer possible (the column was removed, the API was replaced), the cue should be retired. Detection: if a cue hasn't fired in N sessions and the relevant code has changed, flag for review.
- **Staleness detection.** If the cue's lesson contradicts more recent sessions (the team decided to change the convention), the cue needs updating. The elicitation note's "probe staleness rate" metric applies here.

---

## 3. Avoiding the expertise gap

The activation gap note identifies a structural asymmetry: the person who most needs activation scaffolds is least able to construct them. Applied to agent memory: the user who would benefit most from the system surfacing a correction is the user who doesn't know to look for it.

### Why the gap matters more in a store-everything system

In a curated KB, an expert wrote each note knowing what it was for. In a store-everything system, the raw material is session logs that nobody curated. The extraction pipeline must identify what's important without expert guidance. But the extraction pipeline faces the same expertise gap: it doesn't know which corrections are important because importance depends on what future tasks will need — which is unknown at extraction time.

### Approaches

**1. Over-extract, under-filter.** Generate cues aggressively from every session. Accept that many will be low-value. Use firing frequency as the filter: cues that never match any future context are noise; cues that match frequently are signal. This is computationally expensive but avoids the expertise gap by not requiring anyone to judge importance upfront.

The trade-off: storage and extraction cost vs. retrieval precision. If you extract 50 cues per session across 1000 sessions, you have 50,000 cues. Matching against all of them for every task is expensive. You need a fast first-pass filter (embedding similarity, action-type match) with a slow second-pass judge (LLM relevance assessment) for the top candidates.

**2. Consequence-based importance.** Use the session itself as the oracle. Corrections that took a long time to resolve, that required significant rework, or that the user expressed frustration about are more important than minor style preferences. The session log contains these signals: message count after a correction (more messages = harder to fix), user sentiment markers, explicit severity statements ("this is critical" vs. "minor preference").

This doesn't require expertise — it requires reading the emotional and structural signals in the session log. An LLM can do this reasonably well.

**3. Cross-session triangulation.** The expertise gap note says the questions must come from somewhere outside the user-model pair. In a multi-session system, past sessions are "outside" the current session. Specifically: if session 47 contained a correction, and session 89 contained a related correction, the system can triangulate: "These two corrections in the same domain suggest a systematic gap. Generate a broader cue covering the pattern, not just the individual instances."

Example: Session 47 corrects a timezone bug. Session 89 corrects a locale-dependent date formatting bug. Neither user prompt mentioned the other. But the system notices both are in the "datetime handling" domain and generates a meta-cue: "Datetime operations in this project have historically caused bugs. When working with dates, explicitly verify timezone handling and locale assumptions."

**4. The elicitation strategies as automated probes.** The elicitation note's four strategies (direct probes, perspective assignments, domain checklists, structured adversarial prompts) can be automated against the cue library. Periodically, run the agent through a set of adversarial prompts against accumulated cues: "What breaks if you do X?" where X is derived from stored corrections. If the agent fails to activate the relevant cue, the cue's trigger needs improvement or the cue needs to be reframed as an imperative instruction rather than passive context.

---

## 4. Navigability vs. retrieval: which approach for which layer?

The comparative review identifies a deep split: Mem0/Graphiti/Cognee treat knowledge as something you *search* for; Ars Contexta and commonplace treat it as something you *navigate*. In a store-everything system with session logs, both are needed but at different layers.

### Layer map

| Layer | Content | Access pattern | Method | Primary role |
|---|---|---|---|---|
| Raw session logs | Complete interaction transcripts | "Find the session where we discussed X" | Full-text search + temporal filtering | Substrate (ambiguous) |
| Extracted cues | Typed trigger-lesson pairs | "What corrections apply to this action?" | Action-type index + embedding match | System-definition |
| Synthesized artifacts | Consolidated preferences, procedures, precedents | "What are our conventions for X?" | Navigable links from domain indexes | Mixed (preferences/procedures are system-definition; precedents are knowledge) |
| Library notes | Curated knowledge with articulated relationships | "How does X relate to Y?" | Link traversal + semantic navigation | Knowledge |

**Search works for the lower layers** (raw logs and extracted cues) because the access pattern is retrieval: you have a query and you want matching items. The items are numerous, weakly structured, and connected only by temporal co-occurrence or semantic similarity. Extracted cues, although stored like search-retrievable records, are activated differently — the trigger is the agent's proposed action, not a query.

**Navigation works for the upper layers** (synthesized artifacts and library notes) because the access pattern is reasoning: you have a starting point and you want to follow connections to build understanding. The items are fewer, richly structured, and connected by articulated relationships. Navigation is natural for knowledge-role consumption (a human or agent looking up "why" and following links); it serves system-definition consumption poorly because it assumes someone is already asking a question rather than acting.

### Composition: activation, search, and navigation

Three access patterns compose, and they sort by role. A typical full retrieval flow:

1. **Activation** fires any system-definition cues whose triggers match the agent's proposed action. Correction cues load imperatively; preference and procedure cues fill their reserved slots.
2. **Search** over the lower layers surfaces knowledge-role records related to the task (past decisions, negative results, relevant notes).
3. **Navigate** from matched knowledge records through articulated links to library notes, assembling the connected reasoning.
4. **Load** the assembled context into the agent's working memory, with system-definition items framed as instructions and knowledge items as reference.

Example: Agent is writing a database migration.
1. Search finds 3 correction cues related to migrations.
2. One correction cue links to a synthesized procedure: "Migration safety checklist."
3. The procedure links to a library note: "Our deployment strategy requires zero-downtime migrations."
4. The agent receives: the specific corrections, the procedure, and the architectural constraint.

### The bridge layer problem

The hardest part is the bridge between extracted cues and synthesized artifacts. This is where A-MEM's memory evolution idea is most relevant: when a new cue is extracted, existing synthesized artifacts in its neighborhood should be notified and potentially updated. Without this bridge, cues and artifacts drift apart — the cues reflect recent sessions while the artifacts reflect the state when they were last manually updated.

Possible mechanism: when a new correction cue is extracted in domain D, query for all synthesized artifacts in domain D. For each, run an LLM check: "Does this new correction modify, contradict, or extend this artifact?" If yes, flag the artifact for update (or auto-update with human review gate).

---

## 5. Finding "why" across thousands of sessions (knowledge-role retrieval)

The framing identifies a key use case: answering "why did we do it this way?" when the answer is distributed across session logs. This is pure knowledge-role retrieval — the consumer is a human or agent asking a question, not an agent about to act. The mechanisms below (decision extraction, backlinks, temporal clustering, negative-result preservation) build the knowledge-role index over session logs. The complementary system-definition retrieval — firing a cue when the agent proposes the already-rejected alternative — is covered by the typed cue indexes in section 1.

### The problem's structure

A "why" question has three components:
- **The decision** — what was done (usually visible in the current state of the project).
- **The alternatives** — what else was considered (invisible in the current state).
- **The reasoning** — why this choice over the alternatives (partially captured in commit messages and ADRs, but usually incomplete).

Session logs are the only artifact that preserves all three. But finding the relevant sessions requires knowing what to search for — and the user asking "why" typically doesn't know what the alternatives were (if they did, they wouldn't need to ask).

### Retrieval mechanisms

**1. Decision event extraction.** At ingestion time, identify decision events in session logs: moments where alternatives were discussed and a choice was made. Store these as structured records:
```
{
  type: decision,
  subject: "API versioning scheme",
  choice: "URL path versioning (/v1/resource)",
  alternatives_considered: ["header versioning", "query parameter versioning"],
  reasoning_summary: "URL path chosen for visibility in logs and browser testability",
  session: 34,
  timestamp: "2025-03-15T14:23:00Z"
}
```

A "why" query about API versioning matches against the subject field and returns the full decision record with a link back to the session for complete context.

**2. Artifact-to-session backlinks.** When the agent creates or modifies a project artifact (writes a function, changes a config, updates a schema), record a backlink from the artifact to the session. When someone later asks "why is this function structured this way?", the system can follow the backlink to the session(s) where the function was written or last significantly modified.

Implementation: maintain a map of `{file_path + function/section} -> [session_ids]`. Update on every session where the artifact is modified. This is cheap to maintain and provides direct answers to "why" questions about specific artifacts.

**3. Temporal clustering for multi-session decisions.** Major decisions often span multiple sessions. The API versioning choice might start in session 30 (initial discussion), continue in session 34 (comparison of approaches), and finalize in session 38 (implementation). Retrieving only session 34 gives an incomplete picture.

Mechanism: when extracting decision events, detect temporal clusters — sessions within a time window that discuss the same subject. Link them into a decision thread:
```
{
  type: decision_thread,
  subject: "API versioning scheme",
  sessions: [30, 34, 38],
  outcome: "URL path versioning",
  duration: "2025-03-12 to 2025-03-18"
}
```

The "why" query returns the thread, giving the user entry points into all relevant sessions.

**4. Negative result preservation.** The framing notes that "what was tried and abandoned" has no home in standard project structure. Session logs are the only place this information exists. Specific extraction: when the agent attempts approach A, encounters a problem, and switches to approach B, record:
```
{
  type: negative_result,
  attempted: "Header-based API versioning",
  failure_reason: "Proxy servers strip custom headers in our infrastructure",
  session: 34,
  led_to: "decision:api-versioning-url-path"
}
```

This is especially valuable because negative results answer the second-most-common "why" question: "Why didn't we do it the other way?" The answer is findable by searching negative results for the alternative approach.

---

## Trade-offs and open problems

**Extraction quality vs. cost.** Every mechanism above requires LLM processing of session logs. At scale (thousands of sessions), this is a significant compute cost. Trade-off: extract everything thoroughly (expensive but high recall) vs. extract selectively based on session signals (cheap but may miss important items).

**Cue trigger precision.** Too-broad triggers fire constantly and waste context. Too-narrow triggers miss relevant situations. There may be no static optimum — the right trigger breadth depends on how often the failure mode occurs and how severe the consequences are. Rare, severe failures need broad triggers. Common, minor preferences can have narrow triggers.

**The oracle problem for synthesis.** Extracting corrections is relatively easy because the session log contains an explicit signal (user corrected agent). Extracting discoveries, preferences, and procedures is harder because the signal is implicit. The expertise gap applies here too: judging whether an extracted preference is real (rather than a one-time choice) requires the kind of judgment the system is trying to automate.

**Navigability at scale.** The link-based navigation approach works well for hundreds of curated notes. It's unclear whether it works for thousands of synthesized artifacts generated from session logs. The synthesis layer may need its own internal search mechanism, with navigation reserved for cross-layer connections.

**Cold start.** A new system with no session history has no cues, no corrections, no precedents. The system is maximally vulnerable to the expertise gap at exactly the moment it has the least data to compensate. Possible mitigation: seed the cue library from domain-general best practices, then progressively replace general cues with project-specific ones as sessions accumulate.

**Cue conflict resolution.** When two cues contradict each other (session 47 says "always use approach A", session 312 says "approach A failed, use B"), the system needs a resolution strategy. Options: most-recent-wins (simple but may lose valid older knowledge), present-both-to-user (safe but adds context load), temporal-validity-tracking (Graphiti's approach — mark the old cue as superseded with a timestamp).
