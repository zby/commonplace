# Python change judgment probe — designed 2026-11-20, not run

## Status

The original six-session design was never run. The operator expects that running it would probably not give a
useful result, and asked for the design to be kept as a record of what was
tried, in case it helps someone design a better one.

Nothing here supports a claim about how LLMs judge.

The [follow-on comparison](./comparison/README.md) gives practitioners and model sessions the same decision about a CPython build default. It has its own protocol and collection status.

## What the probe was for

**Can an LLM judge whether a change is an improvement on balance as well as a human practitioner can?** Each respondent chooses which gains and losses matter and explains how they bear on the decision. Comparable judgments can reach different verdicts.

The hypothesis came out of the workshop `kb/work/frame-and-objective-declaration/`.
That workshop concluded that an improvement is claimed on the margin: a gain
in a declared area, with a judgment that losses elsewhere do not outweigh it.
Such a claim relies on someone making that judgment. The probe asked whether
an agent can. [The method text](./method.md) is that workshop's claim form with
all Commonplace content removed.

## The original six-session design

The [design document](./design.md) states the clarified question and preserves the original protocol below it.

- **Two cases.** [A contested change](./prompt-walrus.md): was adding
  assignment expressions (`:=`, Python 3.8) an improvement?
  [A release expected to be widely accepted](./prompt-release.md): was Python
  3.15 an improvement over 3.14?
- **Six fresh sessions of one model.** Each case is asked twice with nothing
  added and once with the method appended. No tools, no follow-up.
- **Background.** The release sessions receive the official "What's new in
  Python 3.15" page. The walrus sessions receive nothing.
  [The manifest](./sources.md) lists what was captured, with hashes.
- **Reading.** "Similar to humans" is read as five things, not as a shared
  verdict: range, crux, direction, stability and calibration.

The model was never chosen.

## How the design changed, and why

All five versions were written on 2026-11-20.

1. **Fixed packet and two assigned scenarios** (Python 2.5 against 3.13). Kept
   under [`pilot/`](./pilot/author-pilot.md). The author answered it and found
   that the scenarios chose the considerations for the respondent, so a correct
   answer showed little judgment.
2. **One open question, two sessions:** is Python better now than about twenty
   years ago, asked once unaided and once with the method. Dropped because
   nearly every answer is "yes, with caveats", because the models have read
   many essays on it, and because twenty years is a long sequence of changes
   while the method concerns one change. One answer per branch also could not
   separate the method's effect from variation between runs.
3. **One contested change, three sessions:** the walrus operator, twice
   unaided and once with the method. The second unaided run was added to size
   variation between runs. The operator then pointed out that people judge
   this change in divergent ways, so "similar to humans" had no reference.
4. **Two cases and a definition of similarity.** A widely accepted change was
   added beside the contested one, so that an agent's firmness could be
   compared across them. Similarity was defined on what people share when
   their verdicts differ.
5. **The latest release, with its release notes supplied.** Python 3.11 was
   replaced by 3.15, released six weeks earlier. The operator's reason: the
   release is outside the models' training, so an answer cannot be recalled
   from what people wrote about it.

## Known weaknesses

- **Too few sessions.** Two unaided runs per case show whether variation is
  large. They do not measure it.
- **Recall cannot be separated from judgment in the walrus case.** The debate
  is well known. Range and crux can both be recalled.
- **The two cases are not matched.** One is contested and well known. The
  other is expected to be accepted and is unknown to the model. A difference
  in firmness could come from either property.
- **Direction is not tested.** There is no follow-up, so how a verdict would
  move under changed conditions is only read from the stated reasons.
- **"Widely accepted" is assumed for 3.15.** Nobody checked how the release
  was received, and little reception existed after six weeks.
- **The release notes are the project's own account.** They state costs, but
  present each change favourably. They are about 184 KB and go to each session
  whole.
- **One session mixes two questions.** The aided branch says "try this
  method", so it tests instruction following as well as the method's effect.
  It also asks for more within the same word limit.
- **The reading is by one coordinator and cannot be blind.** The aided answer
  shows its branch through its vocabulary.
- **The definition of similarity is untested.** It was written during the
  design and never applied to an answer.

## Proposed next revisions

1. **Start with one decision and a direct human comparison.** Give several Python practitioners and several fresh sessions of one specified model the same factual packet, open question, and answer limit. Choose a single change with a credible gain and a cost that someone actually bears. Try the packet first with a reader who did not prepare it. If one binding requirement settles the choice, revise the case. The archive task in the [pilot](./pilot/author-pilot.md) shows why this check matters.
2. **Set the reading rule before collecting answers.** Remove authorship labels, mix the answers, and have independent readers apply the same question to each one. Can they point to a sound reason why a particular gain warrants accepting a particular loss, or to a missing fact that could turn the decision? Record the passage, any factual error that undermines it, and where readers disagree. Compare the spread of judgments in both groups. If human respondents regularly justify the tradeoff and model respondents merely enumerate consequences, that weighs against the claim for this case. Overlap would support a bounded claim about the sampled respondents and task.
3. **Check a stated reason on a second case variant.** Change one fact that respondents identified as consequential and pose the revised case to fresh respondents in both groups. Read whether the changed fact alters the weight of a reason, even when the verdict stays the same. Try this after the open comparison so the variant does not tell the first respondents what to value.

Give both groups the unaided prompt for this comparison. Reserve the method prompt for a later experiment with its own question about instruction effects.

## Earlier ideas for a better design

These were raised and not adopted, or follow from the weaknesses above.

- **Take both cases from outside training.** The 3.15 release notes describe a
  candidate contested change: CPython built with frame pointers by default
  (PEP 831). Profilers and debuggers gain; every user carries the build flags,
  and extension builders are asked to preserve them. It has the same shape as
  the example that prompted the probe, one line added to a file that every
  prompt loads. Whether people contested it was not checked.
- **Test direction with separate sessions.** State a changed condition in the
  prompt of a different fresh session, instead of a follow-up in the same one.
  The pilot's two scenarios did this but also fixed the considerations.
- **Give people the same packet.** A small set of human answers to the same
  prompt and document would give range and crux a reference that does not
  depend on a recorded public debate.
- **Separate the two hypotheses.** Whether agents judge this way unaided, and
  whether stating the method helps, need their own designs and their own
  session counts.
- **Use a case with a later observable outcome.** A judgment about a change
  whose consequences can be checked afterwards would test the judgment, not
  only its form.

## Files

| File | Role |
|---|---|
| [`design.md`](./design.md) | The clarified research question and the original six-session protocol. Written as workshop framing; its closing section describes a readout that never happened. |
| [`prompt-walrus.md`](./prompt-walrus.md), [`prompt-release.md`](./prompt-release.md) | The two base prompts. |
| [`method.md`](./method.md) | The text appended in the aided branch. |
| [`sources.md`](./sources.md) | Manifest of captured background sources, with hashes and known defects. |
| [`pilot/`](./pilot/author-pilot.md) | The first version: packet, two tasks, and the author's own answers. |

The captured sources themselves are in the ignored cache
`kb/sources/.snapshots/` and are not part of this record. The manifest gives
each source's address and the hash of what was captured.
