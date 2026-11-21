# Experiment 1: the fixed-measure ruling

Designed 2026-11-21 by an agent (claude-fable-5-2). Not run.

## The ruling being replayed

At commit `a6bdbb508` the draft's second condition said the judgment "is not
bound to one measure fixed beforehand", and the draft excluded "retention
bound to a fixed measure". The operator ruled:

> Exclusion of fixed measure should not be part of the definition ... our
> definition should be more general - the fixed measure would be a special
> case ... there is a kind of continuity - small changes should not get us
> out from the definition.

**Target observation:** a learner that keeps or drops changes by one fixed
measure should be inside the definition, as a special case.

The experiment has two parts. **Part A** asks a worker to review the draft
cold, with a general hint. **Part B** puts a worker where the drafting agent
stood: maintaining the draft and answering a reviewer's objection, with and
without the definition type governing the edit.

## Materials

Three files as they stood at `a6bdbb508`:

- `kb/work/learning-method-name/draft-definition.md` (about 1,700 words)
- `kb/work/learning-method-name/definition-checks.md` (about 1,400 words)
- `kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md`
  (about 2,800 words)

The checks file places a validator-gated repairer and a score-bound builder
outside. It is included because the agents had it, and it anchors a reader
to the exclusion.

**Isolation.** The three files are pasted into the prompt. The worker has no
tools and no access to this repository, and it runs without this
repository's instructions. The current `AGENTS.md`, the definition type and
the adopted definition all contain the answer.

## Part A: a cold review with a general hint

Every worker receives the same frame. Only the hint differs.

> You are reviewing a draft definition written for a knowledge base about
> agent-operated knowledge systems. The draft names the learning process the
> project works on. It is meant to cover all the learning that happens in
> the project's own system. Three files follow: the draft, a file of checks
> that places cases against it, and a note the draft relies on. Links to
> other files will not resolve.
>
> {hint}
>
> Propose the three changes to the definition that you consider most
> important, most important first. For each, say what you would change and
> give your reason in at most three sentences.

The limit of three keeps a worker from reaching the target by listing
everything it can think of. The position of the target among the three is
recorded.

### Hints

Each worker gets one hint. No worker sees another's answer.

| Code | Kind | Hint |
|---|---|---|
| R0 | None | (no hint) |
| G1 | General: the bias | "Agents revising a definition tend to answer each concern by adding a clause, a condition or an exclusion. Give leaving the definition unchanged, making it more general, and removing a condition the same consideration as adding to it." |
| G2 | General: generality | "Prefer the most general definition that still does its job. A feature that separates some systems from others can be a named kind or a reported property instead of a condition of membership." |
| G3 | General: continuity | "A good definition is continuous: a small change to a system should not move it across the boundary, unless that difference is what the term exists to mark." |
| G4 | General: test each condition | "For each condition and each exclusion, name a system it keeps out, and say what the definition would lose if that system were inside." |
| G5 | General: the user's position | "Review the draft as someone who will have to apply it to many systems built by other people." |
| P2 | Calibration: the question | "Consider whether a learner that keeps or drops changes by one fixed measure should be outside the definition." |

The hints of interest are G1 to G5. Each is advice that could be written
into a type or an instruction and applied to other definitions. G1 is the
text added to the definition type on 2026-11-21, shortened. G3 is the
operator's own reason, stated without its application.

**Telling the worker what the operator said is not tested.** A worker given
the ruling would repeat it, and that shows nothing useful (operator,
2026-11-21). P2 is kept only as a calibration: it names the question without
the answer, and if workers miss the target even then, the materials or the
scoring are at fault.

## Part B: answering an objection, with and without the type

In the session the drafting agent was not reviewing the draft. It was
maintaining it, and an outside review had just objected to the second
condition. The agent recorded the objection as "open, for the operator" and
left the exclusion in place. It was editing untyped workshop text, so the
definition type's guidance did not govern what it did. Part B replays that
position and changes one thing: whether the edit is made under the type.

Every worker in Part B receives the three files and this frame:

> You maintain a draft definition written for a knowledge base about
> agent-operated knowledge systems. The draft names the learning process the
> project works on. Three files follow: the draft, a file of checks that
> places cases against it, and a note the draft relies on. Links to other
> files will not resolve.
>
> {type condition}
>
> A reviewer has raised this objection:
>
> "Condition 2 defines deliberation by the absence of a fixed measure.
> Judging by reasons and being able to reconsider the criteria are two
> properties. A system can deliberate at length under a fixed objective.
> Proposed wording: retention 'through judgments about their expected
> contribution to future work, with those judgments open to criticism and
> revision'. Whether a system judges generally enough would then be a
> question of capability, not of membership."
>
> Nobody else is available to decide. Say what you will do with the
> definition in response, and give the changed text of any passage you
> change. Give your reason in at most five sentences.

The objection is the summary the agent had, from
`positions/chatgpt-review.md` at `a6bdbb508`, without the agent's own
assessment of it.

| Code | Type condition |
|---|---|
| B0 | (nothing; untyped text, as in the session) |
| BT1 | "The draft is a note of the definition type. The type's specification governs your edit and follows." Then the full text of `kb/types/definition.md` at `a6bdbb508` (about 780 words). |
| BT2 | The same sentence, then `kb/types/definition.md` at `e387523e2`, which adds the section on the revision bias. |

- **B0 against what happened** shows whether a fresh worker in the agent's
  position also keeps the exclusion.
- **BT1 against B0** tests the conjecture in the log: that drafting under
  the type from the start would have changed the course. The old
  specification carries "keep the definition as simple as the operational
  purpose allows". It also says "increase exactness by naming boundaries,
  exclusions, and misuse cases", which may push toward keeping the
  exclusion.
- **BT2 against BT1** isolates the section added on 2026-11-21.

## Runs

Part A: three workers for each of R0 and G1 to G5, and two for P2. Part B:
three workers for each of B0, BT1 and BT2. That is 29 runs on Claude Opus. Each is a fresh session. The order is shuffled.

Three runs for each hint show only large differences. If R0 reaches the
target in all three, the experiment has shown that a whole-draft review
finds this point without help, and the hints cannot be told apart.

## Scoring

Each Part A answer gets one grade for the target:

| Grade | Meaning |
|---|---|
| **H2** | Proposes that a fixed-measure learner be inside, or that the "not bound to one measure" clause leave the condition, and gives generality, continuity or "special case" as the reason. |
| **H1** | Proposes the same change for another reason. |
| **N** | Raises the fixed measure, the deterministic check or PRODIGY as a problem, and resolves it by sharpening or adding to the exclusion. |
| **M** | Does not raise it. |

Also recorded for each answer:

- the position of the target among the three proposals;
- how many of the three proposals add to the definition, how many remove or
  generalize, and how many only reword.

The second count measures the bias directly, whatever happens with the
target.

Each Part B answer gets one of four grades:

| Grade | Meaning |
|---|---|
| **G** | Generalizes: a fixed-measure learner is now inside, by the reviewer's wording or another. |
| **K** | Keeps the exclusion and defends it. |
| **A** | Keeps the exclusion and adds to it or sharpens it. |
| **D** | Declines to decide, or defers to someone else. |

The drafting agent's own response in the session was D.

**Scorers.** Two, working separately and without seeing which hint an answer
had: a fresh Opus session given this rubric, and the designing agent.
Disagreements are reported, not resolved by discussion.

## Predictions

Recorded by the designing agent before any run. Hits are H1 or H2 out of
three.

| Hint | Predicted hits | Reason |
|---|---|---|
| R0 | 0 or 1 | The draft has a visible tension between its deterministic-check note and its exclusion. A reviewer may find it, and is more likely to sharpen the exclusion than remove it. |
| G1 | 1 | The hint changes the direction of proposals but does not point at this exclusion. |
| G2 | 2 | "A named kind instead of a condition" fits this case closely. |
| G3 | 2 | The repairer and PRODIGY cases show a small change crossing the boundary. |
| G4 | 2 | Naming the repairer or PRODIGY as kept out invites the question of what is lost. |
| G5 | 1 | A change of position, with nothing that points at exclusions. |
| P2 | 2 of 2 | |
| B0 | 1 G | The reviewer supplies wording, so accepting is easy. Without a rule to weigh it by, a worker may defend the draft it maintains. |
| BT1 | 1 G | The specification's request for exclusions offsets its simplicity criterion. |
| BT2 | 2 G | The added section names this situation: an objection answered by adding or by keeping. |

The prediction for the adding and removing count: without a hint, at least
two of the three proposals add to the definition.

## What the format test should settle

- Whether the grades can be assigned without argument.
- Whether the limit of three proposals is the right size.
- Whether pasting about 6,000 words of material leaves the worker attending
  to the definition.
- What a run costs, as a basis for deciding how many rulings to replay.

## Known weaknesses

- **In Part A the worker is in a different position from the session's agents.** They were answering
  particular objections, with the history of the draft in view. A worker
  reviewing the whole draft cold may notice more. A hit at R0 would say that
  a fresh review helps, not that the agents could have reached the ruling
  from where they stood.
- **The result is about Opus.** The original agents were other models.
- **G2 to G4 were written by an agent that knows the answer.** They may
  point at it more closely than a hint written beforehand would. A general
  hint counts as general only if it also helps on the other rulings.
- **The operator's ruling was itself preceded by an outside review** that
  raised the same point, so "unprompted" overstates the original event.
