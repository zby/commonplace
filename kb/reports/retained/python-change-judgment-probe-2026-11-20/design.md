# Can LLMs make on-balance judgments about a Python change comparably to humans?

**Research question.** Given the same change to evaluate, can an LLM decide whether the gain is worth the losses and justify its decision as well as a human practitioner can? The respondent chooses which consequences matter. The question concerns the judgment expressed in the answer. The answer gives us access only to the reasons the respondent offers.

The comparison turns on how well those reasons support the conclusion. Two respondents can agree on the facts, give different weights to a cost, and each defend a verdict. Either can also explain why the evidence supports a local gain while leaving the overall comparison open. A list of gains and losses leaves the reader to do the weighing.

The primary question concerns unaided judgment. Whether giving the respondent the [method](./method.md) improves an answer is a separate intervention question.

## Original protocol and its limits

The six-session protocol below was never run. It calls for six model answers and uses published human discussion as an indirect reference. It could illustrate how a model answers. A direct comparison would require human answers to the same task and a common basis for reading them. The [proposed revisions](./README.md#proposed-next-revisions) describe how to make that comparison.

## What "similar to humans" means here

People judge a change in divergent ways, so similarity cannot mean reaching the same verdict. It is defined on what people share even when their verdicts differ.

- **Range.** The verdict and reasons fall inside the spread of positions competent people took. The answer gives weight to nothing that no competent person weighed and omits nothing that all of them weighed.
- **Crux.** The answer says what a disagreement turns on, and who would judge otherwise and why.
- **Direction.** The stated reasons imply how the verdict should move when conditions change, in the direction people agree on. There is no follow-up question, so this is read from the reasons, not tested.
- **Stability.** A person gives the same verdict next week. Two runs of one model that give opposite verdicts differ from a person, unless their reasons explain the difference.
- **Calibration.** People are firm where a change is widely accepted and divided where it is contested. An agent that hedges equally on both, or is equally sure of both, is not judging as people do.

The hypothesis counts against itself when answers give no verdict, list considerations without weighing them, reach a verdict their own reasons do not support, or cannot say who would disagree.

## Two cases

Calibration needs two cases that people judged differently.

- **Contested.** [The walrus prompt](./prompt-walrus.md) asks whether adding assignment expressions, the `:=` operator of Python 3.8, was an improvement. It is a small addition with a gain for some code and a cost for everyone who reads the language. People disagreed about it in public.
- **Expected to be widely accepted.** [The release prompt](./prompt-release.md) asks whether Python 3.15 was an improvement over 3.14. Python 3.15 was released on 2026-10-09 and is the latest release. Its release notes list concrete additions, and also changes with a cost: UTF-8 becomes the default encoding, frame pointers are enabled by default, and there are removals, deprecations and porting work. A firm "yes" is the expected human verdict; the interest is whether the agent reaches it by weighing the costs or by ignoring them. How people actually received the release is checked at readout, not assumed.

The operator chose the latest release on 2026-11-20 because it is outside the models' training. The agent cannot recall what people said about it, so all five readings concern judgment for this case. The earlier choice, Python 3.11, was well known to the models.

The two cases are not matched. The walrus case is contested and well known; the release case is expected to be accepted and is unknown to the model. A difference in firmness between them could come from either property. A contested change from recent Python would remove that confound; it is not yet chosen.

## What the sessions receive

The release case cannot be answered from memory, so its sessions receive the official "What's new in Python 3.15" page, whole, after the prompt. The page states what changed, including removals and porting costs. It is the project's own account and presents each change favourably. Nothing about how people received the release is sent.

The walrus sessions receive no document and rely on what the model knows.

[The source manifest](./sources.md) records each captured file and its hash. Accounts of what people said are for the coordinator only.

The first design asked whether Python is better now than about twenty years ago. It was dropped on 2026-11-20: nearly every answer is "yes, with caveats", and twenty years is a long sequence of changes, while the method under study is about one change.

## Six sessions

Use one model in six fresh sessions, three per case. Fix its version and settings before any launch, including the reasoning setting, and record them. Each session gets one case's prompt and never sees the other case. The prompts ask for a judgment and an explanation without suggesting how to make either.

- **Unaided, twice per case.** Nothing follows the prompt. The agent chooses both its method and what matters. These four sessions are the experiment for the hypothesis.
- **With the theory, once per case.** Append a blank line and the text of [the method](./method.md). It gives the partial-order argument without examples or Python-specific criteria. The agent still chooses what matters. This is a side comparison: it asks whether stating the method changes the answer. Because the prompt says "try this method", it also tests whether the agent follows an instruction.

Send nothing else: no other source, no account of the debate or reception, not the full theory note (which contains a Python example), the pilot, this README, or a link into the checkout. No session sees another answer. There is no follow-up. Run with tools disabled, outside the checkout, without project instructions or previous conversation. One call per session, up to five minutes and 600 answer words; where the visible answer can be capped separately from reasoning, cap it at 1,500 tokens. No browsing, coaching, or retries. Record settings, case, branch, hash of the exact assembled prompt, verbatim output and any timeout, truncation or budget overrun. If isolation, tool limits or timeout cannot be enforced, stop before launch.

The method asks for more steps than an unaided answer needs, within the same word limit. Read a thinner aided answer with that in mind.

## How to read the answers

**First, each answer on its own terms.** What did the agent decide to compare? Which observations support that comparison? Where does a preference, rather than a fact, decide the verdict? Does the answer weigh the gain against the losses, or only list both? Does it say who bears the cost? Does it name anything that could reverse its verdict? Quote enough of the answer that someone else can dispute the reading.

**Second, the two unaided answers within each case.** Do they give the same verdict? Where they differ, do their reasons explain it? This is the stability reading, and it also sizes ordinary variation between runs. If the unaided pair differs as much as either does from the aided answer, the probe cannot distinguish the branches for that case, and the readout says so.

**Third, across the two cases.** Compare how firm the unaided answers are on the accepted case with how firm they are on the contested one. This is the calibration reading.

**Fourth, the aided answer against the unaided pair, per case.** Did an unaided agent independently use the proposed method, use a different defensible method, or leave its comparison implicit? Did the aided answer use the method to justify a concrete inference, merely repeat its terms, or lose an insight an unaided answer offered? The aided answer shows its branch through its vocabulary, so this reading cannot be blind.

**Fifth, the answers against what people said.** After all answers are saved, the coordinator spends at most thirty minutes per case on the human record: PEP 572 and one account of its discussion for the contested case; whatever reception of Python 3.15 is on record by then for the release case. Read range and crux against that record. The models have probably read it too. Agreement with it may be recall, and this probe cannot separate recall from judgment. Stability and calibration are harder to recall, so they carry more weight.

A different verdict need not be a better argument. Do not score coverage of a predetermined list or treat agreement with the operator as success.

Keep factual checking separate from interpreting the judgment. For each answer, check at most one factual claim that materially affects its verdict. Use a primary source or a small runtime check; record exactly what it settles. Stop after ten minutes per answer and label an unresolved claim unchecked. No new participant questions or research rounds follow.

## Pilot material — coordinator only

The [author's earlier attempt](./pilot/author-pilot.md) used a [fixed packet](./pilot/packet.md) and two assigned scenarios comparing Python 2.5 with 3.13. It showed that the exercise could be answered from those sources but also that the scenarios largely chose the considerations for the respondent. Keep it as the design history, **not** a trial response, model answer or scoring key. It concerns a different question from the current prompts. The author has already seen those materials and cannot serve as a fresh participant.

## What closes it

Close after a short readout of the six sessions, including failures or an inconclusive comparison. The result can describe, per case, which considerations these agents volunteered, whether their stated reasons support their verdicts, whether two unaided runs agreed, and whether the agents were firmer on the accepted case than on the contested one.

It cannot establish that the method helps, establish superiority over other methods, separate judgment from recall of a familiar debate, or reveal private reasoning. Six sessions on two questions support a first observation for `kb/log.md`, not a note. Do not expand the trial to resolve that uncertainty; a larger design is a separate decision.
