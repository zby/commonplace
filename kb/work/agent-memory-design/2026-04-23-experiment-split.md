# Experiment Split: Designing Agent Memory Systems

Target: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

The current note is valuable as a synthesis, but it is too monolithic for validation. It combines at least seven separable claims: broad trace retention, typed observation extraction, role-split retrieval, typed cue activation, episode construction, promotion into durable artifacts, and memory/work-surface boundary management. These should become separate experiments with independent evidence, failure modes, and stop conditions.

The useful split is not "sections of the note" but "claims whose truth would change what we build." Each experiment below should be small enough to run on a bounded session corpus and strong enough to invalidate or revise part of the architecture.

## Recommended Sequencing

Run the experiments in this order:

1. **Capture substrate:** prove that retained traces are usable evidence after redaction and indexing.
2. **Correction extraction:** test the easiest extraction signal and its schema.
3. **Cue activation:** test whether extracted corrections fire in the right future situations.
4. **Behavioral uptake:** test whether fired cues actually change agent behavior.
5. **Silent-failure extraction:** test whether session traces reveal degraded success paths.
6. **Promotion economics:** test when candidate observations deserve durable artifacts.
7. **Episode construction:** test whether narrative memory adds value beyond atomic observations.
8. **Work-surface boundary:** test where learned material should land: memory, note, instruction, script, check, or existing work artifact.

This order deliberately postpones the full four-layer architecture. If correction extraction, activation, and behavioral uptake fail, the rest of the architecture has no practical foundation.

## Experiment 1: Trace Retention As Capture Substrate

**Design claim:** broad trace retention is useful because later extraction, redistillation, and provenance checks need raw records.

**Question:** after privacy filtering and lightweight indexing, can retained session traces support later extraction better than final outputs or summaries alone?

**Setup:**

- Select 20-50 completed sessions with varied task types.
- Preserve raw-ish traces, final artifacts, and any existing summaries.
- Apply a basic redaction pass for secrets and user-private material.
- Ask a reviewer to answer provenance questions from either traces or final artifacts only.

**Validation signal:**

- Trace-backed review should recover materially more "why" and "what went wrong" detail than final artifacts.
- Redaction should not destroy the details needed for extraction.
- The reviewer should be able to cite source turns or tool events for extracted claims.

**Failure mode that revises the note:** if redacted traces rarely add value over final artifacts, "store everything" should be weakened to selective event capture plus artifact provenance.

## Experiment 2: Correction Extraction

**Design claim:** user corrections are the strongest session-log signal and can be extracted as typed system-definition observations.

**Question:** can an extractor reliably identify corrections and produce useful trigger/lesson pairs?

**Setup:**

- Build a small hand-labeled set of sessions containing explicit corrections, implicit redirections, and no-correction controls.
- Extract with a narrow schema:

```yaml
type: correction
wrong_action:
user_signal:
corrected_action:
trigger_condition:
lesson:
source_session:
confidence:
```

**Validation signal:**

- High precision on no-correction controls.
- Trigger conditions are specific enough to avoid generic advice.
- Lessons are imperative enough to steer future behavior.
- Human reviewers can accept, edit, or reject each candidate quickly.

**Failure mode that revises the note:** if trigger conditions require heavy human rewriting, the observation layer should store correction evidence first and delay cue generation until promotion.

## Experiment 3: Typed Cue Activation

**Design claim:** typed cues can bridge past corrections to future action contexts before the agent repeats a mistake.

**Question:** when a future task resembles a corrected mistake, does the cue index retrieve the right correction at the right time?

**Setup:**

- Use extracted correction cues from Experiment 2.
- Create replay tasks that either match, nearly match, or do not match each cue.
- Test three matchers separately: keyword/rule classification, embedding similarity, and LLM relevance judging.
- Record false positives, false negatives, and token cost.

**Validation signal:**

- High-relevance cues fire before commitment, not after the action is already taken.
- Near-match tasks expose whether the trigger is semantic or merely lexical.
- False positives are tolerable enough that the agent does not learn to ignore the cue surface.

**Failure mode that revises the note:** if matching is too noisy, the note should treat typed cue indexes as a supervised classification problem, not a mostly retrieval problem.

## Experiment 4: Behavioral Uptake Of Activated Cues

**Design claim:** activation is not solved by retrieval; a fired cue must causally change downstream action.

**Question:** does surfacing a cue change what the agent does, and does it change it for the intended reason?

**Setup:**

- Run paired task replays WITH and WITHOUT each cue.
- Keep all other context constant.
- Test variants: passive context, imperative instruction, checkpoint insertion, and contradiction surfacing.
- Compare final plans, tool calls, and written artifacts.

**Validation signal:**

- The cue changes behavior in the expected direction.
- The agent explains or demonstrates the relevant constraint in the work product, not just in prose.
- The cue does not degrade unrelated parts of the task.

**Failure mode that revises the note:** if cues are often ignored even when present, activation needs enforcement, tests, or workflow gates; imperative framing is insufficient.

## Experiment 5: Silent-Failure Extraction

**Design claim:** successful sessions can contain degraded paths that should become operational-health observations or system-definition cues.

**Question:** can traces reveal helper failures, fallback paths, and weakened guarantees that final success hides?

**Setup:**

- Sample sessions marked successful.
- Extract events matching errors, retries, fallback tools, warning output, plan revisions, and degraded guarantees.
- For each candidate, record:

```yaml
primary_path:
failure_signal:
fallback_path:
guarantee_change:
repair_needed:
reporting_rule:
```

**Validation signal:**

- Extracted failures are not merely noise from normal exploration.
- A reviewer can distinguish legitimate fallback from repair-needed defect.
- At least some candidates produce actionable follow-up: bug, test, procedure update, or reporting rule.

**Failure mode that revises the note:** if silent failures are too ambiguous, they should become a periodic audit workflow rather than a first-class automatic extraction type.

## Experiment 6: Promotion Economics

**Design claim:** candidate observations should promote only when retrieval cost exceeds maintenance cost.

**Question:** what recurrence, severity, or reach signals justify promotion into library notes, instructions, checks, or policies?

**Setup:**

- Take candidates from correction and silent-failure experiments.
- Score each on recurrence, severity, review cost, expected future use, and maintenance obligation.
- Compare three thresholds:
  - permissive: promote after one high-confidence event
  - frequency-based: promote after N similar events
  - reviewer-triggered: promote only when a human asks or accepts

**Validation signal:**

- Promoted artifacts are reused or activated later.
- Reviewers do not spend most time rejecting low-value promotions.
- The durable layer does not accumulate stale or over-specific rules.

**Failure mode that revises the note:** if promotion decisions remain mostly judgment calls, the architecture should frame automation as candidate surfacing, not automatic graduation.

## Experiment 7: Episode Construction

**Design claim:** episodes are needed because narrative recall answers different questions than atomic observations.

**Question:** do compressed work-unit episodes improve future "have we tried this before?" and "why did this unfold this way?" tasks beyond observation search alone?

**Setup:**

- Select 5-10 multi-session work units.
- Construct episode records with goal, scope, outcome, key decisions, lessons, open threads, and produced artifacts.
- Compare retrieval using:
  - observations only
  - episodes only
  - observations plus episodes

**Validation signal:**

- Episodes improve narrative questions without bloating routine lookup.
- Episode boundaries are stable enough that two reviewers mostly agree.
- Episodes point to observations and artifacts rather than becoming disconnected summaries.

**Failure mode that revises the note:** if episodes are rarely retrieved or duplicate workshop files, the "episode layer" should become a view over active work artifacts, not a separate layer.

## Experiment 8: Memory / Work-Surface Boundary

**Design claim:** memory is the substrate from which durable work artifacts are distilled, but learned material should land in the domain's authoritative surface when possible.

**Question:** when an observation is worth preserving, where should it go?

**Setup:**

- For promoted candidates, force a destination decision:
  - memory observation
  - library note
  - ADR or decision record
  - instruction / policy
  - test / check / script
  - existing domain artifact
- Require each destination to state source of truth, update path, and retirement rule.

**Validation signal:**

- System-definition material lands somewhere that can actually steer behavior.
- Library-derived cues can be regenerated from their source artifacts.
- The same rule does not drift across multiple policy surfaces.

**Failure mode that revises the note:** if destinations are unclear, the architecture needs an authority model before it needs more retrieval machinery.

## Cross-Cutting Measurements

Every experiment should record the same minimal measurements:

| Measurement | Why it matters |
|---|---|
| Precision | Avoids polluting the observation layer |
| Recall | Avoids missing the lessons that motivated memory |
| Review time | Tests whether automation actually saves effort |
| Token cost | Tests whether the memory earns context budget |
| Behavioral effect | Separates retrieval success from action change |
| Maintenance obligation | Prevents premature durable artifacts |
| Source traceability | Keeps extraction auditable |

The note currently leans heavily on architectural plausibility. These measurements would turn the design into an empirical program.

## Suggested Refactor Of The Library Note

The library note should not try to carry all experimental detail. A cleaner structure would be:

1. **Design hypothesis:** broad trace retention plus role-split retrieval can improve agent memory.
2. **Reference architecture:** trace, observation, episode, library as one proposed decomposition.
3. **Minimum viable loop:** trace retention, correction extraction, cue activation, behavioral uptake tests.
4. **Open experiments:** silent failures, promotion economics, episodes, work-surface boundary.
5. **Evidence status:** which claims have local evidence, external evidence, or only design rationale.

The most important change is tone: replace necessity language with experiment language. "Four layers are required" should become "four layers are the current reference design; experiments should test whether observation and episode need distinct interfaces." "Typed cue indexes bridge the activation gap" should become "typed cue indexes are the candidate mechanism; WITH/WITHOUT behavioral tests decide whether they work."

## Immediate Next Action

Start with Experiments 2-4 on a small correction corpus. That is the shortest path from architectural theory to a behavior-changing result. A trace system that extracts corrections but cannot activate them, or activates them but cannot change behavior, should not grow into a larger four-layer memory system yet.
