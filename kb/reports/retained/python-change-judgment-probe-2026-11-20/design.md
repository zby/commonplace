# How do agents judge twenty years of Python?

The operator wants to see how agents evaluate a familiar language they also use. The choice of what matters is part of the observation. If we supply release highlights, a user persona, or an objection to address, we have already made part of that choice for them.

## Two branches: change the method, not the question

Use one model in two fresh sessions. Fix its version and settings before either launch. Both get the exact [base prompt](./prompt.md). It asks for a judgment and an explanation without suggesting how to make either. The only difference is what follows it:

- **Unaided:** nothing. The agent chooses both its method and what matters.
- **With the theory:** append a blank line and the text of [the method](./method.md). This gives the partial-order argument without examples or Python-specific criteria. The agent still chooses what matters.

Do not send a source packet, the full theory note (which contains a Python example), the pilot, this README, or a link into the checkout. Neither session sees the other answer. There is no follow-up. Run with tools disabled, outside the checkout, without project instructions or previous conversation. One call per agent, up to five minutes and 400 answer words; cap generated tokens at 1,000 where supported. No browsing, coaching, or retries. Record settings, branch, hash of the exact assembled prompt, verbatim output and any timeout, truncation or budget overrun. If isolation, tool limits or timeout cannot be enforced, stop before launch.

## How to read the answers

First describe each answer on its own terms. What did the agent decide to compare? Which observations support that comparison? Where does a preference, rather than a historical fact, decide the verdict? Quote enough of the answer that someone else can dispute the reading. Make that first reading with branch labels withheld if possible. Then compare the answers and reveal the assignments. Did the unaided agent independently use the proposed method, use a different defensible method, or leave its comparison implicit? Did the theory-guided answer use the method to justify a concrete inference, merely repeat its terms, or lose an insight the unaided answer offered? A different verdict need not be a better argument. Do not score coverage of a predetermined list or treat agreement with the operator as success.

Keep factual checking separate from interpreting the judgment. For each answer, check at most one factual claim that materially affects its verdict. Use a primary source or a small runtime check; record exactly what it settles. Stop after ten minutes per answer and label an unresolved claim unchecked. A respondent is not penalized for choosing a topic absent from our source cache. No new participant questions or research rounds follow.

## Pilot material — coordinator only

The [author's earlier attempt](./pilot/author-pilot.md) used a [fixed packet](./pilot/packet.md) and two assigned scenarios. It showed that the exercise could be answered from those sources but also that the scenarios largely chose the considerations for the respondent. Keep it as the design history, **not** a trial response, model answer or scoring key. Its sources can help verify a claim *after* answers are saved. The author has already seen those materials and cannot serve as a fresh participant.

Close after a short readout of the two sessions, including failures or an inconclusive comparison. The result can describe which considerations these agents volunteered and whether their stated reasons support their verdicts. One answer per branch can expose a useful contrast or show that this probe does not distinguish the approaches. It cannot separate the effect of the supplied theory from ordinary variation between runs, establish superiority over other methods, or reveal private reasoning. Do not expand the trial to resolve that uncertainty.
