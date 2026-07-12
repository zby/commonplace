---
source: https://pathway.com/research/beyond-transformers-sudoku-bench
description: Pathway's BDH model achieves 97.4% accuracy on extreme Sudoku while leading LLMs score 0%, using the gap as evidence that transformer architecture has fundamental limits for constraint-satisfaction reasoning and arguing for post-transformer latent-space models.
captured: 2026-03-26
capture: web-fetch
genre: practitioner-report
type: kb/sources/types/snapshot.md
---

# Beyond Transformers: Sudoku Bench

Author: Pathway Team
Source: https://pathway.com/research/beyond-transformers-sudoku-bench
Date: March 17, 2026

## The Canary in the Coal Mine

Some breakthroughs look flashy. Others look like a humble puzzle grid.

At Pathway, we believe Sudoku matters because it exposes a gap that much of today's AI conversation prefers to ignore. The strongest language models can write essays, generate code, and sound uncannily fluent, yet they still struggle with a task that many humans treat as a morning warm-up: solving a hard Sudoku. This isn't a quirky benchmark failure. It's a signal that current large language models face a deeper architectural limit.

Sudoku is not "just a game." It is a tightly structured constraint-satisfaction problem, where every move must satisfy multiple rules at once across rows, columns, and boxes. A finished grid is easy to verify: anyone can check whether the numbers one through nine appear exactly once in each row, column, and square. But producing that grid from an incomplete board is much harder, because the solver has to search through interacting possibilities without breaking the rules. That combination makes Sudoku a clean way to test whether a system can truly reason under constraints rather than merely describe them.

This is where today's transformers start to show their limitations, and why the post-transformer era is critical for the path to artificial superintelligence.

## Why Transformers Struggle With Sudoku

Large language models turn problems into text and then solve them by predicting the next token, one step at a time. While it works brilliantly when language is the right medium for a task, Sudoku does not live in language. So forcing it into a chain of text can be painfully inefficient.

The transformer architecture behind most of today's large language models is built on the idea that thinking happens at the same speed as writing (in language). The transformer processes information token by token, with a limited internal state for each step, which makes search-heavy, non-linguistic reasoning unusually awkward.

The latent space, also understood as the internal representation where the model "thinks", is constrained to roughly a thousand floating-point values per token, and each decision gets locked in as text is generated. Transformers simply cannot hold multiple candidate strategies in parallel, meaning they do not have the ability to step back and reconsider earlier moves without verbalizing every intermediate thought.

You can see the workaround already: if prompted cleverly enough, an LLM may try to write a Sudoku solver in Python and outsource the puzzle to code. But this exposes the difference between understanding a game (native reasoning) and escaping it, a distinction that matters far beyond the Sudoku grid.

## Why Games Matter for Artificial Superintelligence

For decades, games have been one of AI's clearest stress tests because they reveal whether a system can plan, search, adapt, and act under rules, rather than just imitate surface patterns.

Before the LLM era, major milestones in AI were measured through games such as Go, chess, and the Atari 2600 games, such as Breakout or Montezuma's Revenge, precisely because games compress important ingredients of intelligence into benchmarks that are hard to fake.

Think of DeepMind's AlphaGo moment: it was never about simply winning a board game, but rather a proof that machines could master domains requiring deep strategic thinking, long-term planning, and adaptive search. Despite these breakthroughs, each game came with a cost: one architecture per game or, at best, one architecture per narrow family of games. The neural networks were trained separately for each challenge.

Then came language models, and suddenly we had generalist systems that could attempt everything from travel planning to writing poetry to solving math problems. The promise was one model to rule them all. But as reasoning capabilities scaled, especially with models designed for explicit reasoning, like OpenAI's O1, we started to see the limitations of what chain-of-thought reasoning can do.

After all, transformer reasoning was an afterthought glued on top and is fundamentally constrained by language.

## Language is not enough for intelligence

For AI to move forward, we need to free our thoughts from the constraints of language. Current reasoning research is moving toward latent or continuous reasoning spaces, where models can preserve and compare multiple options internally, instead of committing too early in text.

This shift is necessary to enable systems that can become truly autonomous. Fluency in language is not enough for AI. AI needs a reasoning substrate that can navigate constraints, hold alternatives in mind, and converge on a strategy without verbalizing every intermediate thought.

Recent research from NYU Tandon Associate Professor of Computer Science and Engineering and Director of the Game Innovation Lab, Julian Togelius, and others has made a similar point: scaling current reasoning models may help, but some limits are fundamental enough that brute-force scaling alone is unlikely to erase them soon. The road to more general intelligence probably does not run through ever-longer text monologues.

## How BDH Changes the Equation

At Pathway, we built BDH (Dragon Hatchling) as a truly native reasoning model. By creating a larger internal reasoning space called the latent reasoning space, it has intrinsic memory mechanisms that support learning and adaptation during use.

This is key. BDH keeps what transformers are great at, specifically language understanding and generation, while adding the ability to solve non-language problems that stump standard LLMs. A model based on BDH is not a model that can only play games, nor is it a language model that can only write text. It is a model based on a single architecture that excels at both.

Here is what that looks like in practice:

| Model | Sudoku Extreme Accuracy | Relative Cost |
|-------|------------------------|----------------|
| Pathway BDH | 97.4% | 10x lower, No chain-of-thought |
| Leading LLMs (O3-mini, Deepseek R1, Claude 3.7 8K) | 0% | High (chain-of-thought) |

*Table 1: Performance comparison on extreme Sudoku benchmarks (approximately 250,000 difficult puzzles). Source: Pathway internal data and https://arxiv.org/pdf/2506.21734 for the Leading LLMs' accuracy score. Pathway's approach reflects top-1 accuracy and does not rely on chain-of-thought nor solution backtracking.*

BDH reaches 97.4 percent accuracy on Extreme Sudoku benchmarks, a collection of roughly 250,000 of the toughest Sudoku puzzles available, while leading LLMs struggle to perform at all.

This mastery doesn't just come from static pre-training. BDH achieves continual learning, where it learns from every interaction and internalizes that learning over time for reasoning. As such, it can pick up the rules of a new game and reach an advanced-beginner level in as little as 20 minutes. From there, it improves its skills through repeated attempts, gaining expertise in the specific domains and problems the user presents.

In line with this experiential learning, BDH also reasons in a richer internal space before committing to output. Think of it like a chess grandmaster who can play twenty simultaneous games with their eyes closed. A grandmaster is not verbalizing each move in each game; rather, she has internalized the patterns and can navigate the search space seamlessly, the kind of mastery BDH enables.

Finally, BDH achieves this at a materially lower cost. By relying on this internalized reasoning rather than forced language outputs, BDH does not rely on chain-of-thought reasoning that burns GPU by verbalizing every step.

## Why Sudoku Is Useful in R&D - the litmus test for AI

Sudoku is an ideal diagnostic for AI researchers, as it is hard enough to reveal genuine weaknesses, easy to verify with zero ambiguity, and benchmarkable at scale across very large sets of difficult puzzles. For us, that makes Sudoku less of a parlor trick and more of a litmus test for AI.

Sudoku Extreme, the specific benchmark we used, contains about 250,000 extremely difficult instances of Sudoku boards. Progress is measurable in a way that vague "reasoning" demos are not.

More interestingly, this approach generalizes. The ability to solve Sudoku is really about the ability to navigate constraint-satisfaction problems, hold multiple possibilities in parallel, backtrack when needed, and converge on solutions that satisfy all rules simultaneously, which are precisely the skills needed for many real-world challenges.

## From Sudoku to Strategy

Many real workflows in medicine, law, operations, and planning are really constraint problems in disguise: they involve many variables, many rules, many possible paths, and high costs for wrong turns.

- In medicine, professionals choose therapies that must balance efficacy, side effects, drug interactions, and patient history.
- In the legal field, practitioners must navigate changing regulatory constraints, potentially contradictory case precedents, and strategic trade-offs in a specific client context.
- In operations, teams face competing demands to optimize schedules, supply chains, and resource allocation in an often dynamic environment.
- In planning, a professional designing a city's emergency response plan during a major event must balance limited personnel and equipment, road closures, traffic patterns, weather forecasts, and shifting priorities - like which areas need help first - all while ensuring that response times stay within acceptable limits and that no critical area is left uncovered.

A system that can reason through those spaces more natively could eventually do more than summarize information. It could help generate the strategy.

We call this _generative strategy_: the ability to look at a problem, understand the constraints, and creatively propose what should be done, instead of merely remembering what has been done before.

That is why this breakthrough matters: Sudoku is the proof point, but the prize is much stronger decision-making.

## What This Means for the Future of AI

The real unlock on the path towards artificial superintelligence is not an AI that is only good at puzzles, and not an AI that is only good at language, but one architecture that can do both. We need systems that can think before they speak.

When we force AI to verbalize every thought or formalize every step, we constrain its ability to genuinely invent. Human problem-solving often operates less like a rigorous, step-by-step whiteboard proof and more like an unstructured mental "soup" where ideas freely interact until a solution simply hits you.

These "Eureka" moments are the true engine of creativity. Richard Feynman, for instance, arrived at his Nobel Prize-winning breakthroughs not by grinding through mathematical dilemmas, but through sudden inspiration while watching a student spinning a plate at a cafeteria. And to achieve this level of genuine invention, AI must possess a latent reasoning space that allows for unstructured reasoning and intuitive leaps.

We believe that the future of AI will belong to systems that can reason natively across domains, that can hold multiple possibilities in a rich latent space, and that can converge on solutions without needing to verbalize every step.

BDH is our answer to that challenge. It is designed to be a universal reasoning system that can speak our language without being trapped inside it. And yes, it solves Sudoku.

## Looking Ahead

We are actively exploring how this reasoning capacity translates to other tasks and domains, and the early signs are promising. The ability to solve abstract constraint problems appears to help with strategic thinking and planning in contexts far removed from puzzle grids, though there is still work to be done.

Validating that a model can discover things beyond its training data; this would be considered true creativity and that ultimately requires demonstrating something no human has done before. That is the frontier of science that now lies on our horizon.

For now, we have a clear milestone: we solved Sudoku puzzles that stump today's leading LLMs. We did it with an architecture that maintains language fluency, without relying on chain-of-thought, and we did it in a way that points toward something bigger.

This is the beginning of what post-transformer reasoning can look like.

---

"At Pathway, we believe that memory and the ability to learn on the fly is the single biggest limitation facing current transformer-based AI models. Pathway is a post-transformer neo-lab that has solved that problem. We are delivering a faster path to AGI through true continuous learning and long horizon reasoning."
