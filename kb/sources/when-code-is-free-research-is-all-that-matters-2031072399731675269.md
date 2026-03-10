---
source: https://x.com/amytam01/status/2031072399731675269
captured: 2026-03-10T13:19:25.932591+00:00
capture: xdk
type: x-article
status_id: 2031072399731675269
conversation_id: 2031072399731675269
post_count: 1
---

# When code is free, research is all that matters

Author: @amytam01
Post: https://x.com/amytam01/status/2031072399731675269
Created: 2026-03-09T18:19:30.000Z

The most important people of this new era won't be engineers; they'll be researchers. When anyone can build for free, the differentiator is knowing what's worth building and whether it’s buildable at all. That's what researchers do: they take problems that might not have solutions and decide if they're worth the bet.
The market has priced this in for decades. Top quant firms pay $600k to undergrads who've never managed a portfolio, because someone who can reason about uncertainty well is worth more than five engineers who can implement that solution. AI labs have inherited the same dynamic at a larger scale; Meta's Superintelligence Labs has reportedly offered individual researchers packages reaching $300 million over four years. When a single training run costs hundreds of millions of dollars, a researcher who improves data efficiency by a few percent pays for themselves many times over.
Why is this so valuable and hard to automate? Software engineering has a defined target: the solution exists, you just have to find it. Research doesn't work that way. "Is there a model architecture that achieves K perplexity on FineWeb in under N training hours?" is a question you can spend a year on, and the answer might just be no. It's a version of the halting problem: you often can't know in advance whether a solution exists, let alone find it.
How to flip really, really valuable coins
For researchers, intelligence is just table stakes. What sets the best researchers apart is a willingness to stake their career on bets that might not pay off, repeatedly, and a compensation structure that enforces it. Quants get paid on P&L: if your strategies don't make money, you're out. ML researchers get promoted by shipping models that actually generalize. Mathematicians get faculty jobs by finding something genuinely new. In every case the feedback loop is: can you be right, not just once, but consistently?
Imagine research as a coin-flipping game. You’re in a room with a quadrillion biased coins, and you want to maximize the number of heads in the shortest amount of time. Almost all coins are “duds:” they’ll almost always come up tails. The novice coin-flipper might start flipping one-by-one, but heads come few and far between. The learned coin-flipper weaves through the quadrillion-coin room with a preternatural air; they flip many coins at once, which tend to come up heads time after time. What comes across as luck is really the refinement of taste: years of feeling faint differences in the weight of the metal, the subtle offsets of a mis-mint, and more. Research taste is about how well you choose your coins: how well you choose which problems are worth working on at all. When each coin is worth a million dollars, the researcher’s job becomes clear: they must not only flip coins fast enough to compound what they learn, but also know which 20 are worth flipping in the first place.
Taste transfers even as domain knowledge shifts.  Theoretical physicists become quants. Quants move into AI. Computational biologists end up running drug discovery programs that look nothing like their PhD work. As AI tools keep dropping domain-specific barriers, taste becomes the only thing left that's truly portable, and the hardest to train.
The shelf life of being right
The agentic coding tools eating SWE alive right now work precisely because engineering has a built-in feedback signal: a test to pass, a spec to meet, a benchmark to clear. You can RL on SWE-bench because the ground truth exists. Research has no equivalent. It’s not clear what it means to RL on a research question, because it’s not clear what definition of “ground truth” one should optimize.
That doesn't mean the tools aren't getting better. Karpathy's autoresearch ran 126 experiments overnight on a single GPU: agents modifying LLM training code, running a five-minute training loop, checking if the result improved, and repeating. That's a lot more coins flipped than the average human in the same time. But look at what “coins” the agent chose to flip: it explored weight decay values and initialization scales. Hyperparameter sweeps. The flipping got faster, but the weighting didn't change.
The best training data for research taste doesn't exist in any corpus. The most valuable research happens behind closed doors: not just successful quant strategies that never get published, but all the failures. Think internal experiments at labs that only share the wins, built upon hundreds of judgment calls about what to abandon that leave no public paper trail. You can scrape arXiv for methods and ideas; you can't scrape the hundred ideas a researcher killed before breakfast.
Success makes taste legible, but it also makes it rigid. The researcher who was right about everything from 2018 to 2024 may be pattern-matching by 2026 and not know it yet. Taste is the hardest thing to train: hardest to teach a person, hardest to define a loss function for, and hardest to notice when your own has gone stale.
This gap will close, probably faster than most people expect. But right now the bottleneck is still the person deciding what to try, and more importantly, what to not try at all.
Cowritten by Amy Tam and E Chi (@echinaceous), with contributions from Trenton Chang (@chang_trenton). Amy Tam is an investor at Bloomberg Beta focused on the future of work, and an investor in Quadrillion. E Chi is a researcher and founder of Quadrillion. Trenton is a researcher at Quadrillion.
