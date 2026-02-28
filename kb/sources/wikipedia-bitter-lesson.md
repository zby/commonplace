---
source: https://en.wikipedia.org/wiki/Bitter_lesson
captured: 2026-02-23
capture: fetch
type: encyclopedia-article
---

# The Bitter Lesson

Source: Wikipedia — https://en.wikipedia.org/wiki/Bitter_lesson
Author: Richard S. Sutton (original essay, 2019); Wikipedia contributors (article)

The bitter lesson is the observation in artificial intelligence that, in the long run, approaches that scale with available computational power (such as brute-force search or statistical learning from large datasets) tend to outperform ones based on domain-specific understanding because they are better at taking advantage of Moore's law. The principle was proposed and named in a 2019 essay by Richard Sutton and is now widely accepted.

## The Essay

Sutton gives several examples that illustrate the lesson:

**Game playing.** In chess, the Deep Blue system that became the first computer opponent to defeat a world champion relied on a relatively simple alpha-beta search algorithm that scaled up by applying large amounts of specialized hardware to search for the best move. This defeated previous attempts to exploit the unique structure of chess or to include grandmaster knowledge directly. Likewise in the game of Go, the AlphaGo algorithm that surpassed human performance relied much less on expert skill at the game itself than previous generations of AI, and was further surpassed by AlphaGo Zero, which removed human expertise completely and trained only by self-play.

**Speech recognition.** Approaches based on training a general-purpose hidden Markov model with large numbers of speech samples consistently outperformed the hand-crafted approaches of the 1970s, and deep learning has continued this trend.

**Computer vision.** Algorithms that were assumed to approximate the human visual system (such as explicitly encoded edge detection or detecting high-level features with SIFT) were outperformed by convolutional neural networks that make far fewer assumptions about the nature of visual perception.

Sutton concludes that time is better invested in finding simple scalable solutions that can take advantage of Moore's law, rather than introducing ever-more-complex human insights, and calls this the "bitter lesson". He also cites two general-purpose techniques that have been shown to scale effectively: search and learning. The lesson is considered "bitter" because it is less anthropocentric than many researchers expected and so they have been slow to accept it.

## Impact

The essay was published on Sutton's website incompleteideas.net in 2019, and has received hundreds of formal citations according to Google Scholar. Some of these provide alternative statements of the principle; for example, the 2022 paper "A Generalist Agent" from Google DeepMind summarized the lesson as:

> Historically, generic models that are better at leveraging computation have also tended to overtake more specialized domain-specific approaches, eventually.

Another phrasing of the principle is seen in a Google paper on switch transformers coauthored by Noam Shazeer:

> Simple architectures -- backed by a generous computational budget, data set size and parameter count -- surpass more complicated algorithms.

The principle is further referenced in many other works on artificial intelligence. For example, *From Deep Learning to Rational Machines* draws a connection to long-standing debates in the field, such as Moravec's paradox and the contrast between neats and scruffies. In "Engineering a Less Artificial Intelligence", the authors concur that "flexible methods so far have always outperformed handcrafted domain knowledge in the long run" although note that "[w]ithout the right (implicit) assumptions, generalization is impossible". More recently, "The Brain's Bitter Lesson: Scaling Speech Decoding With Self-Supervised Learning" continues Sutton's argument, contending that (as of 2025) the lesson has not been fully learned in the fields of speech recognition and brain data.

Other work has looked to apply the principle and validate it in new domains. For example, the 2022 paper "Beyond the Imitation Game" applies the principle to large language models to conclude that "it is vitally important that we understand their capabilities and limitations" to "avoid devoting research resources to problems that are likely to be solved by scale alone". In 2024, "Learning the Bitter Lesson: Empirical Evidence from 20 Years of CVPR Proceedings" looked at further evidence from the field of computer vision and pattern recognition, and concludes that the previous twenty years of experience in the field shows "a strong adherence to the core principles of the 'bitter lesson'". In "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning", the authors look at generalization of actor-critic algorithms and find that "general methods that are motivated by stabilization of gradient-based learning significantly outperform RL-specific algorithmic improvements across a variety of environments" and note that this is consistent with the bitter lesson.

## Key References

- Sutton, Rich. "The Bitter Lesson." incompleteideas.net, March 13, 2019. http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- Reed et al. "A Generalist Agent." Transactions on Machine Learning Research, 2022.
- Fedus, Zoph, Shazeer. "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity." JMLR, 2022.
- Srivastava et al. "Beyond the Imitation Game." 2022.
- Sinz et al. "Engineering a Less Artificial Intelligence." Neuron, 2019.
- Buckner, Cameron J. *From Deep Learning to Rational Machines.* Oxford University Press, 2023.
