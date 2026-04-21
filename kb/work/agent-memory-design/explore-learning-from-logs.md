# What can be extracted from session logs and how does it graduate to durable knowledge?

Workshop exploration for questions 7-9 from the [framing](./framing.md).

## The extraction taxonomy

Session logs contain at least four distinct signal types. They differ in oracle clarity, extraction difficulty, promotion pathway, and — following the [axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — the role the extracted artifact plays when consumed.

Role sorts the four types cleanly. Corrections, preferences, and procedures are **system-definition**: the extracted artifact is consumed as policy that changes what the agent does. Decision provenance and negative results (covered in the framing and synthesis) are **knowledge**: they are consumed as reference to answer "why" questions. Discoveries start as knowledge candidates and may graduate into either role — or both, if the insight both deserves a note (knowledge) and implies a cue (system-definition).

The role affects how the graduated artifact is used, how retrieval finds it, and what destination makes sense. A correction that graduates as a CLAUDE.md entry (system-definition, prose) serves a different consumer than the ADR that documents *why* the correction exists (knowledge, prose). Both can come from the same underlying pattern.

### 1. Correction consolidation (system-definition)

**What it is.** The user says "no, do X instead," "that's wrong," or rejects a tool call and provides a different instruction. The session log records the wrong output, the rejection signal, and the corrected direction.

**Role.** System-definition. The graduated artifact's job is to prevent the wrong action next time. A correction may also seed a companion knowledge artifact ("why do we prefer approach B?") but the primary product is a constraint on future behavior.

**Example extracted artifact:**

```yaml
type: correction
trigger: "When editing Python imports, agent sorted them alphabetically"
correction: "User prefers grouping by stdlib / third-party / local, not alphabetical"
sessions: [2025-03-12-session-4, 2025-04-01-session-7]
occurrences: 3
```

**Oracle quality: strong.** The user's rejection is an explicit negative signal. The correction itself is the positive signal. Pi Self-Learning's extraction schema targets exactly this — `{"mistakes": [...], "fixes": [...]}`. The trace-derived survey confirms this is the easiest extraction type across all reviewed systems.

**Promotion heuristic:** "Corrected the same mistake N times" is a clean promotion trigger. cass-memory's maturity progression (candidate -> established -> proven) with score decay works here. ClawVault's "seen on two different dates" also applies. Threshold could be as low as 2 occurrences — if you corrected the same thing twice, it is not a fluke.

**Graduated artifact:** A rule in CLAUDE.md, a convention in WRITING.md, a preference in a memory file, or (at the far end of codification) a linting check or validation script.

### 2. Preference mining (system-definition)

**What it is.** The user consistently accepts certain patterns and rejects others, but never explicitly articulates a rule. The signal is distributed across many sessions — no single session contains enough evidence.

**Role.** System-definition. A preference steers future choices; it is not primarily consumed to answer questions.

**Example extracted artifact:**

```yaml
type: preference
pattern: "User accepts commit messages under 72 chars; rejects longer ones"
evidence:
  - {session: "2025-02-10-s3", action: "accepted 'Fix import ordering'"}
  - {session: "2025-02-14-s1", action: "rejected 'Update the configuration file to handle the new edge case' — rewrote as 'Handle edge case in config'"}
  - {session: "2025-03-01-s2", action: "accepted 'Add retry logic for API calls'"}
confidence: 0.8  # 6 accepts, 2 rejects matching pattern
```

**Oracle quality: medium.** Individual accept/reject signals are clear, but the *pattern* connecting them requires inference. The agent must hypothesize "short commit messages" as the latent variable, not just record individual events. This is why preference mining is harder than correction consolidation — the extraction step requires generalization, not just logging.

**Detection approach.** Two strategies:

- **Bottom-up:** Cluster accept/reject decisions by domain (commit messages, code style, file naming, prose tone). Within each cluster, look for feature splits that predict acceptance. This is essentially the ExpeL approach — compare successful and failed trajectories within a task family.
- **Top-down:** Periodically prompt an LLM with "here are the last 50 accept/reject decisions in domain X; what preferences explain the pattern?" This is closer to ClawVault's weekly reflection — a scheduled synthesis pass over accumulated observations.

**Promotion heuristic:** A preference needs both consistency (high accept rate when the pattern is followed) and coverage (enough instances to rule out coincidence). A threshold like "observed in 5+ decisions across 3+ sessions with >80% consistency" could work. But the consistency threshold is itself a design choice with no obvious oracle.

**Graduated artifact:** A style guide entry, a CLAUDE.md instruction, a configuration setting. The hardest preferences to graduate are taste-based ones ("I prefer shorter function names") that resist codification into deterministic rules.

### 3. Procedure extraction (system-definition)

**What it is.** The same workflow recurs across sessions: "search for related notes, read the type template, write the note, connect it, validate." The session log records each step; across sessions, the recurring sequence becomes visible.

**Role.** System-definition. A procedure is consumed to steer how a task is performed. The codification gradient (instruction → skill → script) stays within the system-definition role while shifting class (prose → prose with formal shape → symbolic).

**Example extracted artifact:**

```yaml
type: procedure
name: "Ingest a new source"
steps:
  - "Snapshot the URL with /snapshot-web"
  - "Read the snapshot and classify by source type"
  - "Write .ingest.md with structured analysis"
  - "Connect to related notes and indexes"
  - "Run validate on the ingest file"
observed_in: [session-14, session-23, session-31, session-45]
variations:
  - "GitHub repos use gh CLI instead of WebFetch"
  - "PDFs require page-range reading"
```

**Oracle quality: medium-low.** Recurrence is detectable, but "same workflow" requires alignment across sessions that may differ in surface details. Session 14 might ingest a blog post; session 45 might ingest a paper. The steps are analogous but not identical. Sequence alignment over session traces is a real algorithmic problem.

**Detection approach.** Tool-call sequences are more reliable than natural-language descriptions. If sessions 14, 23, 31, and 45 all contain the subsequence `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]`, that is a detectable pattern even when the surrounding conversation differs. This is why the trace-derived survey emphasizes that log formats matter more than prompts — tool-call structured logs enable pattern detection that prose transcripts cannot support.

**Promotion heuristic:** "Same tool-call subsequence in 3+ sessions" is a reasonable trigger to flag a candidate procedure. But the promotion target is interesting — should it become an instruction document? A skill definition? A script? The answer depends on how stable and codifiable the procedure is.

**Graduated artifact:** An instruction file (if human judgment is needed at steps), a skill (if it can be automated with parameters), or a script (if it is fully deterministic). The graduation pathway mirrors the codification spectrum from the KB's theory.

### 4. Discovery flagging (knowledge, sometimes system-definition)

**What it is.** During work, an insight emerges — a connection between ideas, a design principle, an abstraction that unifies several observations. These are the highest-value extractions and the hardest to detect automatically.

**Role.** Discoveries enter as knowledge: claims that grow the agent's reach when retrieved for reference. Some develop a system-definition companion after the fact — a discovery about async resource cleanup may produce both a note (knowledge) and a cue that fires when the agent writes async cleanup code (system-definition). Role is assigned at graduation, not extraction, because the operational implications are visible only with use.

**Example extracted artifact:**

```yaml
type: discovery
claim: "The oracle problem is not about learning mechanisms but about
        manufacturing evaluation for judgment-heavy mutations"
source_session: "2025-03-15-session-8"
context: "While reviewing AgeMem and Pi Self-Learning side by side,
          noticed that both have functioning learning loops but differ
          entirely on oracle strength, not on extraction technique"
related_notes:
  - automating-kb-learning-is-an-open-problem.md
  - memory-management-policy-is-learnable-but-oracle-dependent.md
confidence: low  # single observation, needs validation
```

**Oracle quality: weak.** How do you know an insight is worth keeping? Unlike corrections (explicit rejection signal) or preferences (statistical pattern), a discovery is a one-off event. The agent or user says something that feels important, but "feels important" is not a verifiable signal.

**Detection heuristics (all weak, all worth trying):**

- **Explicit markers.** The user says "that's interesting," "remember this," "this is a key insight," "write this down." These are the clearest oracle signals for discoveries, but they depend on the user recognizing and flagging the moment.
- **Surprise signals.** The agent produces a claim that connects notes not previously linked, or the conversation shifts topic in a way that suggests a connection was discovered rather than planned. Harder to detect but could be approximated by tracking which note-pairs appear together in a session for the first time.
- **Elaboration depth.** When the user or agent spends unusually long elaborating a point — multiple turns, examples, caveats — that correlates with perceived importance. Turn count and token volume per topic are measurable proxies.
- **Post-hoc validation.** A claimed discovery that gets referenced in later sessions is validated by use. This is a trailing indicator (you only know it was valuable after the fact) but it is the most reliable one.

**Promotion heuristic:** Discoveries should enter as candidates with low confidence and promote based on reference frequency. If the insight from session 8 gets cited or re-derived in sessions 15, 22, and 30, it is accumulating evidence of value. This is the "seen on different dates" heuristic generalized — not just seen, but *used*. A discovery that is never referenced again was probably not worth keeping.

**Graduated artifact:** A note in the KB — possibly a structured-claim with evidence and caveats, possibly a connection between existing notes, possibly a new index entry. Discoveries that survive promotion become the highest-reach artifacts in the system.

## The promotion pipeline

Across all four extraction types, a common pipeline emerges:

```
Session log
  -> Extraction (per-session, runs at session end or on schedule)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

### Stage 1: Extraction

Runs at session end (like Pi Self-Learning's `agent_end` trigger) or on a timer (like Napkin's `intervalMinutes`). Produces typed candidates: corrections, preference observations, procedure fragments, discovery flags.

**Key design choice:** Extraction should be narrow and schema-constrained, not open-ended summarization. Pi Self-Learning's `{"mistakes": [...], "fixes": [...]}` works because it asks a specific question. "Summarize the session" produces mush. The extraction prompt should be one per signal type, each asking for its specific schema.

### Stage 2: Candidate store

A workshop-layer holding area. Candidates are dated, typed, and linked to source sessions. They are *not* yet library artifacts — they have not been reviewed, validated, or connected. The flat-memory failure modes predict that mixing candidates with library notes will cause search pollution. The candidate store must be a separate space.

This is where the three-space model becomes practically useful. Candidates are operational artifacts (high churn, session-derived, not yet knowledge). They live in the operational space until promotion. The workshop layer is exactly this separation.

### Stage 3: Promotion filter

Runs periodically (daily? weekly? on explicit trigger?). Reviews accumulated candidates. Applies type-specific heuristics:

These thresholds are untested starting points for discussion, not empirically validated numbers. They should be calibrated against real session data before any implementation.

| Type | Promotion signal | Threshold sketch | Role |
|------|-----------------|-----------------|------|
| Correction | Same mistake corrected N times | N >= 2, different sessions | System-definition |
| Preference | Consistent accept/reject pattern | 5+ instances, 80%+ consistency, 3+ sessions | System-definition |
| Procedure | Same tool-call subsequence recurs | 3+ sessions with aligned subsequence | System-definition |
| Discovery | Referenced or re-derived in later sessions | 2+ later references, or explicit user flag | Knowledge (may add system-definition companion) |

The promotion filter is itself a judgment-heavy operation. It sits on the inspectability-learnability spectrum from the memory-management-policy note. Starting with inspectable heuristic rules (threshold-based, like the table above) makes sense. Whether to learn the promotion policy from data (like AgeMem's RL-trained policy) depends on having enough volume — and on having an oracle for "was this promotion good?", which loops back to the core problem.

### Stage 4: Graduation

A promoted candidate becomes a library artifact. The specific form depends on both the source type and the role the graduated artifact will play:

- **Correction -> rule/convention (system-definition).** Codifiable corrections become CLAUDE.md entries or validation checks. Judgment-dependent corrections become documented conventions. Optionally produces a companion knowledge artifact (an ADR or note) explaining *why* the convention exists.
- **Preference -> style guide / configuration (system-definition).** Preferences with high consistency become explicit instructions. Preferences with lower consistency become documented tendencies with exceptions noted.
- **Procedure -> instruction / skill / script (system-definition).** Along the codification spectrum: instructions (prose), skills (prose with formal shape), scripts (symbolic). Role stays constant; class tightens.
- **Discovery -> note (knowledge), possibly plus cue (system-definition).** The primary graduation is a knowledge artifact: a note, structured claim, or new index entry. If the discovery has clear operational implications, it also produces a system-definition cue. This is the hardest graduation because the knowledge artifact needs authorial judgment — the only graduation type that cannot be fully automated.

## Session logs as oracle substrate

The automating-KB-learning note identifies the oracle problem as the bottleneck. Most systems lack a training signal for "was this memory operation good?" But session logs in a store-everything system provide a richer oracle substrate than any of the reviewed systems exploit.

**Available signals in session logs:**

Signals 1-3 (corrections, accept/reject, explicit markers) are covered in the per-type oracle quality assessments above. The remaining signals are what session logs uniquely provide beyond what any single extraction type captures:

4. **Questions asked.** What the user asks reveals what they need to know. A question that recurs across sessions signals a gap in the KB or a frequently needed retrieval path.
5. **Elaboration investment.** How much time/tokens the user spends on a topic. A noisy signal but one that correlates with perceived importance.
6. **Session-end state.** Did the session accomplish its goal? A task-completion signal, weaker than AgeMem's benchmark oracle but still informative.
7. **Return patterns.** The user returns to the same topic in a later session. A trailing signal that validates prior importance judgments.
8. **Abandoned lines of investigation.** The user starts exploring something and drops it. Negative signal — this direction was not valuable enough to pursue.

Signals 4-5 are medium-strength, useful for ranking. Signals 6-8 are weak individually but may compose into a useful aggregate.

The key insight: **no single signal is sufficient as an oracle for all extraction types, but the combination is richer than what any reviewed system uses.** Pi Self-Learning uses only corrections. ClawVault uses importance scoring plus recurrence. cass-memory uses helpful/harmful feedback plus score decay. None of them combine corrections, accept/reject patterns, recurrence, elaboration depth, and return patterns into a composite signal.

This is the quality-signals note's argument applied to session logs specifically: manufacture a soft oracle from many weak signals rather than waiting for a strong single signal.

## Session logs and ADR drafting

The framing proposes that session logs contain the raw material ADRs distill. Can the system semi-automate ADR drafting?

**What an ADR needs that session logs contain:**

- **Context.** What problem prompted the decision? Session logs record the initial question or task.
- **Decision.** What was decided? The session log records the final accepted approach.
- **Alternatives considered.** What was tried and rejected? This is the unique value — session logs preserve dead ends that no other artifact captures. When the user says "no, not that approach, try X instead," the log records both the rejected alternative and the reason for rejection.
- **Consequences.** What follows from the decision? Often discussed in the session, sometimes only apparent later.

**A semi-automated ADR pipeline:**

1. **Detection.** Flag sessions where a design decision was made. Heuristic: the conversation includes multiple alternatives discussed, an explicit selection, and reasoning for the selection. Tool calls to write architecture-relevant files are a supplementary signal.
2. **Pre-assembly.** Extract the alternatives discussed, the reasoning for each, the final selection, and any stated consequences. Format these as a draft ADR with sections pre-filled.
3. **Human review.** The draft ADR is a candidate, not a finished artifact. The human reviews for accuracy, adds consequences that became apparent later, and connects the ADR to existing KB notes.

This is a concrete instance of the general pattern: session logs provide raw material, extraction produces a candidate, human review graduates it. The ADR case is particularly valuable because ADRs are high-value artifacts that are expensive to write from scratch — any reduction in authoring cost directly increases the number of decisions that get documented.

**What makes this tractable:** The "alternatives considered" section is the hardest part of ADR writing and the part session logs most directly contain. When you make a decision in a session, the conversation naturally records what you tried first, why it did not work, and what you did instead. Capturing this automatically is extraction from structured dialogue, not open-ended synthesis.

## Difficulty gradient

Arranging the extraction types by difficulty:

1. **Corrections** — easiest. Clear signal, narrow schema, well-validated by existing systems (Pi Self-Learning, cass-memory).
2. **Preferences** — medium. Requires cross-session pattern detection but the individual signals are clear.
3. **Procedures** — medium. Requires sequence alignment across sessions but tool-call structure helps.
4. **ADR pre-assembly** — medium-hard. Requires identifying decision points and extracting structured alternatives.
5. **Discoveries** — hardest. Requires recognizing that an insight has value, which is the oracle problem in its purest form.

A practical system should start at the easy end and work up. Correction consolidation could run today with minimal infrastructure — just session logging and a periodic extraction pass. Preference mining and procedure extraction need enough session volume to detect patterns. Discovery flagging may always need human involvement at the recognition stage, with automated support limited to surfacing candidates for review.

## Open threads

**Deduplication across extraction types.** A correction ("don't sort imports alphabetically") may also be a preference observation ("prefers grouped imports") and eventually a procedure fragment ("import ordering step in code review"). The same underlying knowledge can appear in multiple extraction schemas. Does the system merge them? Keep them separate and let the promotion filter sort it out? The answer probably depends on whether the graduated artifacts differ — if a correction becomes a rule and a preference becomes a style guide entry, they are different artifacts serving different functions even if derived from the same underlying pattern. The role axis adds a further distinction: a single source may legitimately produce both a system-definition cue (the lint rule) and a knowledge note (the explanation of why the convention exists). These are not duplicates; they serve different consumers.

**Extraction timing.** Pi Self-Learning extracts at session end. ClawVault extracts incrementally during the session. Napkin extracts on a timer. The right timing depends on the signal type: corrections are best extracted immediately (the context is fresh), preferences need cross-session accumulation (no single session has enough data), procedures need enough sessions to detect recurrence. A system with multiple extraction types probably needs multiple extraction clocks.

**Taxonomy completeness.** The four-type extraction taxonomy may not be exhaustive. One boundary case: agent-recognized workflow failures — sessions where the agent hit a dead end it recognized without user correction. These sit between corrections (there is a signal that something went wrong) and discoveries (the agent identified the failure itself, without external feedback). Whether these deserve a separate extraction type or fold into corrections-with-no-user-signal is an open question.

**Volume before learning.** The automating-KB-learning note concludes "we need more usage before we can design the learning loop properly." How much is enough? For corrections, even 10 sessions might surface useful patterns. For preferences, probably 50+. For discoveries, the threshold may be indefinite — some discoveries are one-off and never recur, but are still valuable. The "enough volume" threshold is itself type-specific.

**The ephemeral computation trap.** If extraction runs but candidates never promote, the system has the appearance of learning without the substance. The ephemeral-computation note's warning applies: generating artifacts and discarding them trades accumulation for simplicity. A candidate store that fills up and is never reviewed is just a more elaborate form of ephemerality. The promotion filter must actually run, and someone (human or agent) must actually review the promoted candidates. Otherwise the whole pipeline is theater.
