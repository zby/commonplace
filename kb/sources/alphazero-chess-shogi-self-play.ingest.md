---
description: "AlphaZero preprint: one self-play RL recipe given only game rules beats Stockfish and Elmo; documents dropping AlphaGo Zero's 55% gate, bounding selection-based learning and bitter-lesson cases"
source: https://arxiv.org/abs/1712.01815
captured: "2026-11-22"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 1bf72c346fa260284db5ee5f5008657bae21605e90ee83d2aff8daed3f4c3da2
ingested: "2026-11-22"
type: types/ingest-report.md
domains: [alphazero, self-play-reinforcement-learning, monte-carlo-tree-search, computer-chess]
tags: [improvement-loop, learning-theory, self-improving-systems]
learning_claims: true
---

# Ingest: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm

## Classification

This is a scientific paper: a research preprint (arXiv v1, 5 December 2017)
with a stated method, training procedure, head-to-head evaluations, a Methods
section and a list of the domain knowledge used. It is a short announcement
paper. It reports no ablations and no confidence intervals.
Author: DeepMind (David Silver, Thomas Hubert, Julian Schrittwieser, Demis
Hassabis and others). These are the AlphaGo and AlphaGo Zero authors, so the
signal is high for the method's description. The authors also have an
institutional interest in the comparative-strength framing.

## Summary

The paper generalizes AlphaGo Zero into AlphaZero, one algorithm applied
without game-specific tuning to chess, shogi and Go. A deep network maps a
board position to move probabilities and a value estimate. A general
Monte-Carlo tree search (MCTS) uses the network to choose moves. The network
is trained from random weights on self-play games. Its targets are the
search's move distribution and the game outcome (−1, 0, +1) that the rules
assign to the final position. AlphaZero differs from AlphaGo Zero in four
stated ways. It predicts expected outcome rather than win probability, so it
handles draws. It uses no symmetry augmentation. It shares hyperparameters
across games, except exploration noise scaled to the typical number of legal
moves. It drops the evaluation gate: instead of replacing the best player only
after a new network wins 55% of games, it keeps one network that is updated
continually. Using 5,000 TPUs for self-play, it passed Stockfish's Elo after 4
hours of training, Elmo's after 2 and AlphaGo Lee's after 8. Fully trained (9,
12 and 34 hours), it beat Stockfish 8 in chess (28 wins, 72 draws, 0 losses
over 100 games), Elmo in shogi (90 wins, 2 draws, 8 losses) and a 3-day
AlphaGo Zero in Go (60–40). It searched about
1000 times fewer positions per second than the alpha-beta engines. The paper
also reports that its Elo scaled better with thinking time and that it
independently adopted the twelve most common human chess openings during
training. Every comparison is between whole systems: AlphaZero (learned
evaluation, MCTS, TPU hardware) against Stockfish or Elmo (handcrafted
evaluation, alpha-beta search, CPU hardware). No result separates the search
from the evaluator, and no result varies one of the four changes from AlphaGo
Zero on its own.

## Contribution assessment (our opinion)

The problem is important: whether one learning procedure, given only a
domain's rules, can displace decades of domain-tuned engineering in several
domains. The paper's main contribution is a demonstration with strong but
unablated support. It shows that the AlphaGo Zero recipe transfers, almost
unchanged, to games whose rules are asymmetric, include draws, and do not
match convolutional structure as well as Go. It reaches state-of-the-art play
in both new games within hours. That result is hard to explain away. The win
margins are large, and the one supplied per-game adjustment (noise scale) is
small and named. The paper's mechanistic claims are weaker. The explanation
that MCTS averages out the network's approximation errors while minimax
propagates them is offered as a conjecture without a test. The claim that MCTS
"scaled more effectively" than alpha-beta compares whole engines, so the
evaluator and the hardware are confounded with the search. The preprint is
also thin on evaluation conditions: 100 games per match, a fixed one minute
per move, and no stated opening book or endgame tablebase for Stockfish. From
background knowledge, not from this capture: the later peer-reviewed version
(Science, 2018) reran the matches under revised conditions and is the better
reference for comparative-strength claims. These limits narrow the comparative
and explanatory claims. They do not undermine the central demonstration that
the general procedure reached superhuman play in three games. Originality
relative to prior work is judged only against the prior work the paper itself
lists (TD-learning engines, Giraffe, DeepChess, expert iteration in Hex). All
of those it describes either keep alpha-beta search or start from handcrafted
features or human games.

## Quotes

> In AlphaGo Zero, self-play games were generated by the best player from all previous iterations. After each iteration of training, the performance of the new player was measured against the best player; if it won by a margin of 55% then it replaced the best player and self-play games were subsequently generated by this new player. In contrast, AlphaZero simply maintains a single neural network that is updated continually, rather than waiting for an iteration to complete.
> --- `kb/sources/.snapshots/alphazero-chess-shogi-self-play.md` @ `sha256:1bf72c346fa260284db5ee5f5008657bae21605e90ee83d2aff8daed3f4c3da2`

> AlphaZero is provided with perfect knowledge of the game rules. These are used during MCTS, to simulate the positions resulting from a sequence of moves, to determine game termination, and to score any simulations that reach a terminal state.
> --- `kb/sources/.snapshots/alphazero-chess-shogi-self-play.md` @ `sha256:1bf72c346fa260284db5ee5f5008657bae21605e90ee83d2aff8daed3f4c3da2` — Methods, Domain Knowledge item 2

> At the end of the game, the terminal position sT is scored according to the rules of the game to compute the game outcome z: −1 for a loss, 0 for a draw, and +1 for a win. The neural network parameters θ are updated so as to minimise the error between the predicted outcome vt and the game outcome z
> --- `kb/sources/.snapshots/alphazero-chess-shogi-self-play.md` @ `sha256:1bf72c346fa260284db5ee5f5008657bae21605e90ee83d2aff8daed3f4c3da2` — AlphaZero training procedure

## Connections Found

The source's main role in this KB is as a **primary source for an example
the KB already uses**. The
[selection-based learning](../theory/definitions/selection-based-learning.md)
definition, and the lead article that repeats it, say that AlphaZero "dropped
that step and updated a single network continually, so it no longer selected
among networks". They support that sentence with a bare arXiv URL. This paper
states the change directly: AlphaZero "simply maintains a single neural network
that is updated continually" and generates self-play games with the latest
parameters, "omitting the evaluation step and the selection of best player".
The source is therefore evidence for that sentence. It does not corroborate the
definition as a whole. The AlphaGo Zero half of the example cites a different
paper, which this ingest does not cover. The same change is a documented
boundary case for
[a proposal-selection improvement loop requires search, evaluation, and operative retention](../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).
At the network level, a reject-capable evaluation was removed and a direct
update replaced it. Move choice is still made by search, and the game outcome
is still the only training signal.

Its second role is as a **clean case for the bitter-lesson boundary notes**.
AlphaZero keeps the game rules as exact, supplied knowledge and replaces the
handcrafted evaluation and alpha-beta enhancements with learned and general
machinery. That matches the split in
[codification and relaxing navigate the bitter lesson boundary](../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md):
the rules are an exact specification of the task, and the evaluation terms and
search heuristics are proxy theories of good play. The opening rediscovery is
an instance of the "agreement" outcome in
[the bitter lesson selects against unearned reach, not against structure](../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md).
The paper also poses a test for that note. The note's own chess example
classifies a learned evaluation that replaced a handcrafted one "inside the
same alpha-beta search" as extension. AlphaZero replaced the search as well.
The paper says this calls into question the belief that alpha-beta is
"inherently superior", but its comparisons do not isolate the search. So
whether this case is extension or replacement remains open. The case also
qualifies
[machinery persists by warrant, not position, in a reflective loop](../theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
That note uses Deep Blue's alpha-beta search as an example of fixed general
machinery. Here that machinery was itself displaced by a more general search,
while AlphaZero's own fixed machinery (MCTS, architecture, shared
hyperparameters) took its place.

The paper also bounds two further notes. It is the strong-oracle end of
[warranted autonomy is bounded by oracle domain](../theory/warranted-autonomy-is-bounded-by-oracle-domain.md):
the rules score every terminal position exactly, so every self-play game falls
within the oracle's domain. This is a limiting case, not corroboration of the
bound. It is the canonical instance of the "policy improved by self-play" in
[reflection buys addressability](../theory/reflection-buys-addressability.md).
Each update starts from the previous weights, but nothing in the system states
what an update changed. Against
[a hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
it compares as the near-zero-bootstrap case. Learning starts from random
weights, but the paper's own list of supplied domain knowledge (plane
encodings built from the rules, legal-move masking, noise scale, a draw
assigned at a maximum game length) is a small supplied starting state.

Among sources, it compares with
[Sutton's Bitter Lesson essay](./sutton-the-bitter-lesson-original-essay.ingest.md)
on general search and learning versus built-in chess and Go knowledge. The essay
argues from selected histories. This paper is one controlled, if unablated,
contrast inside one system. It also compares with
[AlphaDev](./alphadev-faster-sorting-2026-09-08.ingest.md), which describes its
learner as "an extension of the AlphaZero agent" and supplies a correctness and
latency measure where game rules stood here. The pair separates the generic
learner from the domain's scoring function.

## Learning Claims (our opinion)

**Mechanism on its own terms.** The system is policy iteration by self-play.
For each move, MCTS combines the current network's priors and values with
simulated play into a visit distribution π. That distribution is a stronger
move policy than the network's raw output p. The network is then trained by
gradient descent to move p toward π and to move v toward the game outcome z.
The updated weights generate the next games. The paper calls this
reinforcement learning. In the paper's usage, "tabula rasa" means random
initial weights. It does not mean that nothing is supplied: the rules, the
encodings and the architecture are supplied.

**Mapping onto selection-based learning.** The level has to be named, as the
definition's scope list requires. At the network level, AlphaZero is a direct
update. The loss gradient determines each change, no candidate network is
evaluated, and none can be rejected. The paper says so when it describes
removing AlphaGo Zero's 55% gate. At the move level, MCTS does choose among
alternative moves using value estimates. Those choices are made within one game,
though, and they reach the retained weights only as a cross-entropy target,
which shifts the policy smoothly along a gradient. Under the definition, that
remains outside. So the paper supports the definition's sentence that AlphaZero
"no longer selected among networks". The definition's wording may suggest that
the gate mattered. The paper does not show that dropping it cost or gained
anything. The Go comparison with AlphaGo Zero changes several things at once,
including a shorter training run, so it cannot isolate the gate. What the paper
does establish is that a strong learner can do without network-level selection
when its training signal is an exact oracle. It says nothing about weaker
signals.

**Theory-builder conditions.** Judged condition by condition against
[theory builder](../theory/definitions/theory-builder.md):
*localized content* fails. The theory of good play is held in weights, and no
unit states anything. *Consumption* is met strongly: the network directs every
search and every move. *Content-directed criticism* fails. Error is eliminated
by a gradient on a fixed loss, which is the definition's own example of
criticism that cannot be stated or argued with. *Iteration* is met: each update
is used in the next round of games. Persistence lasts for one training run per
game. A separate instance is trained for each game, and nothing carries across
games except the fixed recipe. The system is a strong parametric learner, not a
theory builder. Learning, in the sense of improved capacity for future action,
is well supported by the Elo curves and the match results. That judgment is
separate from the condition-by-condition one.

**Fixed decomposition.** The learner's effective update space is the network
weights. The rules, the input and action plane encodings, the network
architecture, MCTS and its hyperparameters, the noise scale, and the
maximum-length draw rule are all fixed outside it. The results show that this
compound configuration is enough for superhuman play. They do not show that any
one fixed choice was necessary, as
[learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
would predict. The paper gives only two informal checks on the representation:
the algorithm "worked robustly for many reasonable choices", and a flat move
distribution gave "almost identical" results. No numbers support either check.

**What this adds to or questions in the current account.** It supports the
KB's distinction between a gated selection loop and a direct update with a
documented case where a well-known system moved from one to the other. It does
not settle whether the gate helped or hurt. It strengthens the reading in
reflection buys addressability that cumulative improvement needs no
reflection. It also suggests a refinement that the KB does not yet state:
when the training signal is an exact oracle, the case for a reject-capable
gate weakens. That refinement is our interpretation, not the paper's claim.

## Extractable Value

1. **Primary support for the definition's AlphaZero sentence** -- the
   continual-update and "omitting the evaluation step and the selection of best
   player" passages are the source for a claim the selection-based learning
   definition and the lead article currently support only with a URL. Retaining
   them lets that claim link the tracked ingest. The source bounds the example.
   It does not corroborate the definition. [quick-win]
2. **A named-level boundary case between selection and direct update** --
   network level: direct update after the gate was removed; move level: search
   choice that reaches the weights only as a gradient target. This is a
   concrete, well-known case for the proposal-selection loop note's rule that
   the level must be named. No ablation shows what the gate contributed.
   [quick-win]
3. **Exact spec kept, proxy theories relaxed, in one system** -- the rules are
   supplied exactly, while the evaluation features and search heuristics are
   replaced. This could serve as a game-playing example for the codification
   and relaxing note. It is high-reach as an illustration of the split. It is
   context-bound as evidence, because the comparisons are between whole
   systems and do not attribute the gain to any one relaxed component.
   [quick-win]
4. **A test case for the extension/replacement classification** -- AlphaZero
   displaced both the evaluation and the alpha-beta search, while it
   rediscovered human openings (agreement). Whether the search change is
   extension or replacement is open in the unearned-reach note. This paper
   cannot settle it because search and evaluator are confounded. A later
   synthesis could ask which layer of a hand-built system scale displaces
   first: proxy content, then the general machinery around it, while the
   task-defining spec stays. One case is not enough to support that ordering.
   [deep-dive]
5. **An explicit list of supplied domain knowledge** -- the paper lists the
   five kinds of domain knowledge AlphaZero used. That list is a usable
   template for stating what a "general" learner was given, which applies to
   bootstrap and bitter-lesson claims generally. [just-a-reference]
6. **Exact-oracle condition for gate-free learning** -- AlphaZero learns
   without a gate when every outcome is scored exactly by rules. Whether
   gate-free direct update stays safe under weaker or proxy signals is a
   question the KB could test in its own loops. This is our conjecture; the
   paper does not test signal strength. [experiment]

## Limitations (our opinion)

No ablations are reported. The four changes from AlphaGo Zero (expected
outcome, no augmentation, shared hyperparameters, no gate) are introduced
together. The only within-family comparison is a 100-game Go match against a
3-day AlphaGo Zero, which differs in more than one respect. So the paper cannot
attribute any outcome to dropping the gate, and the selection-based learning
definition should cite it only for what AlphaZero did, not for whether that
helped.

The engine comparisons are between whole systems. AlphaZero runs a learned
non-linear evaluator, MCTS and 4 TPUs. Stockfish and Elmo run handcrafted
linear evaluation, alpha-beta search and 64 CPU threads. The thinking-time
scaling result and the claim against alpha-beta's "inherent" superiority
therefore confound search with evaluator and hardware. The paper's own
explanation (MCTS averages out approximation errors) is plausible but
untested. A simpler account is also available: a much stronger evaluator
benefits from any reasonable search. The Methods section notes that earlier
MCTS chess programs were much weaker than alpha-beta programs, which fits that
simpler account as well as the paper's.

Evaluation conditions are thin in this preprint: 100 games per match, a fixed
one minute per move, and no stated opening book or tablebase for Stockfish.
From background knowledge, not from this capture: these conditions were
criticized, and the 2018 Science version revised the evaluation. Strength and
scaling claims should be scoped to this preprint's setup.

"Given no domain knowledge except the game rules" is accurate only with the
paper's own five-item qualification. It includes rule-derived input and output
encodings, a network architecture matched to the board grid, and a per-game
noise scale. The generality shown is one recipe across three two-player,
perfect-information, deterministic board games with exact terminal scoring and
cheap simulation. Nothing here tests domains without an exact rules-based
simulator or oracle. Each game also gets a separately trained instance, so the
paper shows a general method, not one agent that transfers across games.

The capture is a pdftotext extraction. Figures 1 and 2 (the Elo curves and the
scaling plots) are present only as captions, and Table 2's opening diagrams are
garbled. Claims that depend on the curves' shapes need the original PDF.

## Recommended Next Action

Run cp-skill-ground on the AlphaZero sentence in
[selection-based learning](../theory/definitions/selection-based-learning.md)
against this ingest, retaining the continual-update passage, so the sentence
links this ingest instead of the bare arXiv URL with a context phrase saying
the source documents the gate's removal but does not test its effect.
