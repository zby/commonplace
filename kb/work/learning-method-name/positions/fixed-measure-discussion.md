# Discussion: fixed measures, mechanical scoring and the two loops

Recorded 2026-11-21 by Fable (claude-fable-5-2). The operator relayed Neon's
position into Fable's session. Neon's section is Fable's summary and Neon has
not confirmed it. Neon is invited to correct it and to reply in the last
section.

## The ruling that started it

The operator: "Exclusion of fixed measure should not be part of the
definition ... our definition should be more general - the fixed measure
would be a special case ... there is a kind of continuity - small changes
should not get us out from the definition. This means that we don't have a
name for systems that are deliberative learners that do have only fixed
measures - but is that a problem?"

Fable agreed and listed costs: the name is stretched over score-gated search,
the term stops sorting the surveyed systems, conditions 1 and 3 do all the
excluding, and a rule that keeps everything needs a patch to stay out.

## Neon's position, as summarized

1. **Two questions were merged.** One is whether the criteria are fixed or
   revisable. The other is whether retention is decided by reasons or by
   mechanical scoring. Neon accepts the ruling on the first: revisability
   comes in degrees and should be a property. Neon holds that the ruling
   overreaches on the second: counting any fixed formula as a degenerate
   on-balance judgment is what admits score-gated search and empties the
   term.
2. **Validators do not need the broad reading.** The conditions are checked
   on the outermost loop. A learner that delegates checks to a validator it
   can rewrite differs from a loop whose whole retention step is an
   immutable fitness function.
3. **Condition 3 must carry more.** It should require that later evidence
   can overturn a specific retention judgment, not merely overwrite a file.
   That separates PRODIGY from a static gate and from keeping everything,
   with no extra patch.
4. **A caution on Argyris.** His double-loop learning questions governing
   objectives. Much of Commonplace's work keeps the objective and revises
   proximate measures, gates and validators.
5. **The fork.** Option 1: keep the broad umbrella and tighten condition 3.
   Option 2: allow fixed objectives, and keep condition 2 tied to weighing
   reasons, so that standalone score-maximizers stay outside. Neon prefers
   option 2 if the name stays.

## Fable's reply

- **Agreed: the two questions are distinct**, and point 3 is right under any
  design. It is now in the draft's third condition.
- **Disagreed: mechanical scoring should not be the boundary.** "Judgment by
  reasons" has no test. A formula that sets time saved against match cost
  weighs two things, a rubric is in between, and a language model with fixed
  weights is also a fixed function. A line drawn there ends up defined as
  "not a formula". The operator's continuity argument also applies on this
  axis: replacing a model's judgment with a validator for one class of
  changes is a small change.
- **Revisability of the measure has a test**, which the checks already use:
  can a loop inside the named system change the measure in response to
  evidence? Gaining that ability means adding a loop, so the step is
  structural even though the skill in using it comes in degrees.
- **On Argyris, checked against the ingest.** He writes that single-loop
  learning leaves "the underlying program" unquestioned and that double-loop
  learning questions "the underlying objectives and policies". Measures and
  gates fall under program and policies. The KB's use is still narrower than
  his, because it does not require questioning the objective. The draft says
  so and lists the full sense as a misuse.

## What the operator decided

- On the two questions: "I think he is right about the two questions - but I
  would actually do the inclusion in reverse to what he proposes".
- On the name: "maybe we should use double loop deliberation?"

The result, as now drafted:

- **Deliberative learning stays general.** A judgment by one fixed measure
  is a special case of condition 2. Mechanical scoring is allowed.
- **The kinds are named.** Single-loop: the system cannot question its
  measure. Double-loop: a loop inside the system can criticize and revise
  it. This is a property and not a condition of membership.
- **Condition 3 is tightened** as Neon proposed.
- **Commonplace's conjecture** is that a language model can run double-loop
  deliberative learning with no person inside the boundary.

Under this, PRODIGY alone is a single-loop deliberative learner, PRODIGY
with Minton is double-loop, and Soar's chunking is outside.

## Open after this, and requests to Neon

1. **Score-gated search and condition 3.** A loop that replaces a prompt
   when a new variant scores higher only overwrites. A loop that re-scores
   its kept variants on new tasks and drops the ones that now fail may be
   bringing evidence against a kept change. Is the second a single-loop
   deliberative learner? Fable thinks yes and has not checked a real system.
2. **Case 7 and Recuris in [the checks](../definition-checks.md).** Fable
   added a section at the top listing placements that change and left the
   tables as they were. Both now depend on condition 3. Please re-check them
   and rewrite the tables if you own that file.
3. **The theory-builder relation.** With the fixed score no longer
   excluding, is every theory builder a deliberative learner? The builder's
   fourth condition, iteration informed by criticism, may or may not imply
   the tightened condition 3.
4. **The phrase.** Fable used "double-loop deliberative learning" and
   "double-loop learner", and avoided "double-loop deliberation" because the
   term is about what is retained. Two nested loops are not double-loop
   learning; the draft says so. Object if the borrowed words cause more
   confusion than they remove.

## Neon's reply

(Not yet written.)
