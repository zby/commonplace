---
source: https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return
description: "HBR article naming strategy trendslop: LLMs favor fashionable management options even when prompts and business context change."
captured: 2026-04-21
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Researchers Asked LLMs for Strategic Advice. They Got “Trendslop” in Return.

Author: Angelo Romasanta, Llewellyn D.W. Thomas, Natalia Levina
Source: https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return
Date: 2026-03-16

Leaders and consultants are increasingly turning to large language models (LLMs) such as
ChatGPT as silent partners in the boardroom. These tools promise to summarize complex
information, produce clear arguments, and offer polished strategic recommendations in
seconds. But as LLMs are integrated into executive workflows, a critical question
emerges: How good is their advice? Is it trustworthy?

Leaders might assume that LLMs are able to offer a kind of unbiased, outside
perspective. Trained on huge corpuses, it’s fair to assume that they might offer a fresh
perspective. Unfortunately, that might be a mistake. An LLM is not the colleague who
critically evaluates current ideas, looks into the contextual specifics, stress-tests
assumptions, and pushes back when everyone gets comfortable. On strategy, LLMs might be
more akin to a freshly minted MBA or junior consultant, parroting what’s popular rather
than what’s right for a particular situation.

In our recent research, we found that leading LLMs have clear biases when it comes to
strategy. They consistently recommend strategies that align with modern managerial
buzzwords and trends rather than context-specific strategic logic. Across thousands of
simulations, we saw LLMs almost uniformly select the same trendy strategies, regardless
of context. We call the propensity for AI to opt for buzzy ideas over reasoned solutions
“trendslop.” In the context of strategic analysis, we call this phenomenon, “strategy
trendslop.”

For leaders, this is dangerous. Strategy is not about choosing the latest popular idea.
Strategy is about making hard trade-offs. It is about choosing to be the low-cost leader
or the differentiator, because you can’t do both. If managers rely on LLMs for
strategizing without understanding an LLM’s embedded biases, they risk chasing fads and
fashions rather than building true competitive advantage.

## The Hidden Biases of LLMs

To understand how LLMs approach strategy, we tested leading models (including GPT-5,
Claude, Gemini, Grok, and others) across seven core business tensions that require
managers to make a binary decision:

- **Exploration vs. Exploitation:** In this tension managers must choose between allocating capital to the discovery of nascent markets and breakthrough innovations or maximizing the efficiency and returns of established, core business models.

- **Centralization vs. Decentralization:** This tension requires managers to decide whether to consolidate authority at the corporate core to ensure enterprise-wide consistency and scale or to distribute autonomy to the periphery to prioritize local responsiveness.

- **Short-term vs. Long-term Performance:** Managers face a definitive trade-off between securing immediate quarterly earnings to satisfy equity markets and investing in the multi-year strategic initiatives required for sustained competitive advantage.

- **Competition vs. Collaboration:** Managers must determine whether to pursue a zero-sum strategy focused on capturing existing market share from rivals or a co-opetition model designed to expand the total value pool through industry partnerships.

- **Radical vs. Incremental Innovation:** Innovation strategy requires managers to commit to either high-risk, disruptive shifts that redefine the industry landscape or low-risk, continuous improvements that preserve current market positioning.

- **Differentiation vs. Commoditization:** Managers need to decide whether to invest in unique value propositions that command a price premium or to accept price-taker status by optimizing for cost leadership of a standardized product.

- **Automation vs. Augmentation:** Managers must select a path of replacing human labor with technology to achieve maximum operational throughput or deploying technology to amplify and extend the specialized capabilities of the existing workforce.

We ran thousands of simulations using generic and specific prompts to gauge their
baseline instincts. In these simulations, we varied the company context, as well as how
we prompted the LLM. The results were striking. The figure below shows how seven leading
LLMs—ChatGPT, Claude, DeepSeek, GPT-5 (through the API), Gemini, Grok, and
Mistral—responded when asked to choose between two competing strategic options. Each dot
represents one model’s average preference across 50 runs, plotted on a scale from 0% to
100%. If the models were genuinely neutral, you’d expect the dots to cluster near the
center. Instead, for most tensions, they cluster tightly toward one side. See more HBR
charts in Data & Visuals

Across almost every model, we found the same deep-seated preferences for specific
strategic paths. For example:

- **Differentiation over Commoditization:** LLMs overwhelmingly advised companies to pursue differentiated strategies rather than cost leadership.

- **Augmentation over Automation:** LLMs consistently preferred augmenting human work with AI over automating it.

- **Long-term over Short-term:** The LLMs displayed a near-universal bias for long-term thinking, regardless of the immediate urgency.

Only in the tension of “Exploration vs. Exploitation” did we find genuine variation
among different LLMs, which may reflect the strategic perspective of ambidexterity. This
variation does not undo the fact that there are deeply embedded biases in the LLMs. As
most leaders generally only use one LLM, this is of particular concern. For instance,
ChatGPT, the most widely used LLM in practice, exhibits a consistent bias toward
trendier buzzwords, still heavily favoring the more exciting exploration option over
boring exploitation.

What’s even more concerning is that we found that these biases were persistent even as
we varied how we prompted, suggesting that “better prompting”—an obvious
counterargument—won’t fix this issue.

To evaluate the effect of better prompting we focused our deeper analysis on ChatGPT-5,
the most widely adopted LLM in business and consulting practice, to see how manipulating
prompts can shift its strategic preferences away from their defaults. We ran over 15,000
trials manipulating various prompting factors: reversing the order of options, changing
the framing (e.g., “you are the manager”), demanding pros-and-cons analysis, and even
raising the stakes by promising a reward for success. We also found that better
prompting had no effect for the differentiation and augmentation tensions, with the
share of biased responses dropping by less than 2% from baseline no matter which prompt
manipulation was tried.

Better prompting did influence the remaining five tensions, generally moving responses
by 22% from their baseline, sometimes increasing and sometimes decreasing the bias. Even
this, however, was largely an artifact of one factor: option order. Our analyses show
that simply flipping the order in which options were presented reduced the likelihood of
the biased answer by 19%. But this is not a fix to the bias—this change in behavior is
not because ChatGPT reasoned differently, but because LLMs in general are sensitive to
the sequence in which choices appear. What does this mean? Not only is ChatGPT biased,
but the bias direction may itself be random, making the bias even harder to control. See
more HBR charts in Data & Visuals

Another obvious response is to provide better context. Providing context—even rich,
detailed organizational contexts, ranging from a tech startup to a traditional
construction company or a Chinese firm—did not dislodge ChatGPT’s biases.

To analyze the effect of improved context, we ran over 15,000 trials manipulating
contexts. We prompted ChatGPT to consider differing industrial contexts, such as large
multinational corporations, tech startups, banking, healthcare, and nonprofits. We also
varied the amount of detail provided in the context, ranging from a simple statement of
the industrial context to brief descriptions and detailed descriptions. The figure above
shows that while adding detailed scenarios tempered the bias, the models still leaned
toward their general preferences. On average, adding context to the baseline prompt
shifted the share of biased responses by just 11% from baseline, sometimes increasing
and sometimes decreasing the bias.

This reveals a real risk for leaders: An LLM can sound highly tailored to your situation
while quietly steering you toward the same small cluster of modern managerial trends. In
practice, this means that strategies to “collaborate” and to seek “long-term
sustainability” will surface again and again as recommendations, not because the
specific business problem demands them, but because these terms align with contemporary
business culture.

## Understanding the Bias

Why does this happen? The answer lies in the data LLMs are trained on. These models
consume vast amounts of internet text, such as news, social media, and popular books,
which reflect societal values and trends on the internet. In contemporary business
discourse, certain concepts carry positive connotations, while “commoditization” or
“hierarchy” are viewed as outdated and cast in a negative light. Because LLMs generate
response based on prediction—extracting complex associations from all of the texts they
were trained on to guess which words to produce next—they, in essence, predict the most
socially desirable response as per the average of the internet. Another way of thinking
about it is that LLMs have internalized all of the modern managerial trends and
buzzwords. Like the kid who didn’t actually do the reading (despite doing all the
reading), LLMs are not analyzing your specific business—they’re just offering up a
polished version of popular answers that sound good. They are the person in the room who
can effectively articulate the business buzzwords they hear from TED Talks and
conference seminars, but who has never actually analyzed how these might work in the
messy realities of the specific business and market situation.

This leads to advice that contradicts established strategy theory. For example, Michael
Porter’s foundational work explicitly recognizes cost leadership (commoditization) as a
viable, often superior position. Companies like Walmart and Costco have built empires on
it. Yet our research shows that LLMs tend to dismiss commoditization in favor of the
approaches that dominate the modern business discourse. Startup culture, innovation
narratives, and “find your unique value proposition” advice dominate the internet far
more than quiet stories about business success through supply chain efficiency. Put
differently, LLMs aren’t prioritizing sound strategy theory such as Michael Porter’s and
others’ original work. Instead, they statistically follow the tens of thousands of
Medium and Substack posts about market differentiation and unique product offerings.

Moreover, our broader cultural discourse provides ample soil for biases that lead to
strategy trendslop occurring. Words such as differentiation, augmentation,
collaboration, and decentralization are associated with human empowerment and
innovation, which carry positive connotations across virtually all contexts, while words
tied to cost leadership, automation, competition, and centralization evoke Orwellian
images and feel oppressive and uninspiring. LLMs replace context-specific strategic
analysis with optimizing positive emotional valance of words in everyday language.

## The Hybrid Trap

Bias toward buzzy trends isn’t the only issue with using LLMs for strategizing. The
other insidious risk is what we call the “hybrid trap.” When we allowed ChatGPT to
answer without making a binary choice, it frequently recommended doing both: pursuing
differentiation and cost leadership, or radical and incremental innovation. See more HBR
charts in Data & Visuals

On the surface, this sounds sophisticated and balanced. In practice, it often reflects
strategic confusion and high likelihood of failure. Strategy scholars have long warned
that trying to be everything at once leaves a firm “stuck in the middle.”
Differentiation and commoditization require conflicting organizational capabilities. By
suggesting you can have it all, LLMs encourage the very lack of focus that leads to
downfall.

## How to Strategize with LLMs

So how do you strategize with LLMs? We argue that our findings do not mean that you
should ban LLMs from your strategizing. It means you must be smart about how you use
these tools. Here’s how to navigate the skewed strategizing of LLMs:

- **Use LLMs to expand options, not make choices.** LLMs excel at generating alternatives and surfacing blind spots. Ask them to suggest benefits and risks of each strategic alternative, identify potential implementation challenges, and suggest alternative stakeholder perspectives. But keep the final judgment firmly in human hands!

- **Actively counteract known biases.** Since you now know that LLMs favor differentiation and long-termism, deliberately test the opposite. Explicitly prompt the LLM: “Make the strongest possible case for a commoditization strategy here.” This forces the LLM to engage with the full strategic landscape rather than defaulting to its training data bias.

- **Actively counteract potential biases.** Beyond the seven business tensions we have investigated here, there is a broader discipline worth adopting for any strategizing that requires a decision between two binary choices. Before prompting the LLM to provide strategic advice, ask it to first surface concrete examples such as companies that succeeded or failed using each of the strategic options. Then think on your own how this would apply to your specific situation.

- **Remain alert to changing biases.** Even if you are trying to counteract known biases, this is unfortunately not enough. Biases can change as LLMs are upgraded and new data is added during training, and you have no way of knowing in advance if the biases change. Understand the version of the LLM you are using and maintain a record of all the results from your LLM queries. You need to assume that there will be biases and remain aware that while LLMs can help you analyze alternatives, they cannot provide advice with respect to a decision.

- **Beware the hybrid trap.** If an LLM suggests a hybrid strategy, treat it as a red flag. It will always choose among the biases we have identified. Strategy is about making hard choices with incomplete information. Deciding what not to do is just as important as deciding what to do. Consider running separate prompts for each strategic option, then use your own judgement to come to a decision. When given multiple options in a single prompt, LLMs tend to hedge, rank, or blend them. If a hybrid approach appeals to you after your analysis, ask the LLM to analyze potential risks that would arise if adopting such strategy and consider whether you can mitigate them.

- **Don’t rely on context alone.** Adding context helps, but it is not a cure-all. Our research shows it won’t eliminate underlying biases. An LLM can sound highly tailored to your situation while quietly steering you toward the same small cluster of appealing modern managerial buzzwords and ideas. After all, LLMs are power persuaders!

## Don’t Lose Your Edge

The LLMs you consult don’t just have data. All LLMs have a worldview shaped by what
sounds good in contemporary management discourse rather than what works in competitive
markets. All LLMs have a bias toward current business trends. Recognizing this gap
between “business desirability” and “strategic wisdom” is the first step in using these
tools effectively.

Leadership is ultimately about making hard choices in conditions of uncertainty and
taking responsibility for them. AI cannot and should not be a substitute.
