---
source: https://www.mindfiretechnology.com/blog/archive/the-no-free-lunch-theorem-why-no-learning-algorithm-is-universally-best/
description: Bruce Nielson's No Free Lunch explainer connecting inductive bias, optimization, neural-network smoothness assumptions, and Popperian fallibility
captured: 2026-05-19
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# The No Free Lunch Theorem: Why No Learning Algorithm Is Universally Best

Author: Bruce Nielson
Source: https://www.mindfiretechnology.com/blog/archive/the-no-free-lunch-theorem-why-no-learning-algorithm-is-universally-best/
Date: 2026-05-14

In my [previous post on inductive bias](https://www.mindfiretechnology.com/blog/archive/the-inductive-bias-problem-why-machine-learning-needs-assumptions/), I ended with an open question: is there an "optimal" inductive bias -- one whose search space is universal but whose search strategy is still efficient and tractable for any problem?

Aren't humans an "optimal" general learner compared to, say, existing machine learning algorithms? So intuitively it seems like the answer should be "yes, there is an optimal learner."

As it turns out, there is a mathematical proof known as the "No Free Lunch Theorem" that proves the answer is actually "no." It is one of the most important results in the theory of optimization.

In 1997, David Wolpert and William Macready published a paper called ["No Free Lunch Theorems for Optimization"](https://www.cs.ubc.ca/labs/algorithms/reading_group/no_free_lunch.pdf) that proved something remarkable: averaged over all possible problems, no optimization strategy performs better than any other. Including random search. Including random guessing. Including humans in the loop. Every strategy that gains an advantage on some class of problems pays for it with equal disadvantage on another class.

And when they say "strategy," they mean it broadly. As Ho and Pepyne put it in their [accessible explanation of the theorem](https://faculty.cc.gatech.edu/~bboots3/CS4641-Fall2019/Lectures/08-20-2019-NoFreeLunch.pdf): "Strategies include methods involving search, adaptation, learning, voting, feedback, dynamic programming, evolution, randomization, and even humans in the loop. In short, the concept of strategy covers any method for coming up with a solution to an optimization problem. Nothing can be more general or more inclusive" (Ho and Pepyne, 2001).

This sounds absurd. We know that some algorithms work better than others in practice. How can all strategies be equally good? The answer lies in those three words: "all possible problems." Let me show you why.

## A Simple Pathfinding Problem

Imagine a robot that needs to find the shortest path from point A to point D through a small network:

```text
    B
   / \
  A   D
   \ /
    C
```

There are two possible routes:

- Path 1: A -> B -> D
- Path 2: A -> C -> D

Each path has a total distance. The robot does not know the distances in advance -- it must pick a path and find out. The goal is to pick the shorter one.

## The Universe of All Possible Problems

Let us say each path's total distance can be Short (1), Medium (5), or Long (10). A "problem" is a specific assignment of distances to both paths. In the formal framework, each such assignment is a function -- labeled f0, f1, and so on -- that maps each path to a distance. Since each path can independently be 1, 5, or 10, there are 3 x 3 = 9 possible functions. Here they all are:

```text
The P-Matrix: All 9 Possible Problems
Problem:    f0   f1   f2   f3   f4   f5   f6   f7   f8
Path 1:      1    5   10    1    5   10    1    5   10
Path 2:      1    1    1    5    5    5   10   10   10
```

This table is what Ho and Pepyne call the P-matrix. The rows represent the available choices. The columns represent every possible problem -- every possible assignment of distances to paths. The entries are the distances.

Most of these nine problems will never occur in the real world. Some of them might correspond to a real map. Others are pure mathematical fiction -- worlds where both paths are equally short, or where the path that looks longer on a map is actually shorter. The P-matrix does not care about physical plausibility. It enumerates everything.

Now consider two strategies:

Strategy 1: Always take Path 1.

Strategy 2: Always take Path 2.

Strategy 1 gets the Path 1 distance on every problem: 1, 5, 10, 1, 5, 10, 1, 5, 10. Total: 48.

Strategy 2 gets the Path 2 distance on every problem: 1, 1, 1, 5, 5, 5, 10, 10, 10. Total: 48.

The totals are identical. Averaged over all nine possible problems, neither strategy is better than the other.

## Where Each Strategy Wins

The totals are the same, but the individual problems tell a more interesting story.

Strategy 1 wins on f3, f6, and f7 -- problems where Path 1 is shorter than Path 2. Strategy 2 wins on f1, f2, and f5 -- problems where Path 2 is shorter. They tie on f0, f4, and f8.

On the problems where Strategy 1 wins, it wins by a combined total of (5-1) + (10-1) + (10-5) = 18.

On the problems where Strategy 2 wins, it wins by a combined total of (5-1) + (10-1) + (10-5) = 18.

The gains and losses cancel perfectly. This is not a coincidence.

## Why the P-Matrix Makes This Inevitable

Look at the P-matrix again. The columns enumerate every possible combination of distances. In the Path 1 row, every possible distance (1, 5, 10) appears exactly three times. The same is true for the Path 2 row.

Ho and Pepyne point out that mathematically this is a counting matrix -- a matrix whose columns count through all possible value assignments. The key property of a counting matrix is that all row sums are equal. You can verify this by inspection: both rows sum to 48. No row can have a higher total than any other when the columns enumerate every possible assignment. This is a mathematical certainty. We showed this for our small 2 x 9 matrix, but the property holds for any size.

As long as the columns enumerate every possible combination of values, the matrix is a counting matrix and the row sums will always be equal.

And that is the No Free Lunch theorem. No matter what strategy you use -- no matter how sophisticated, how clever, how well-informed -- if you sum its performance across all possible problems, you get the same total as any other strategy. The P-matrix is a counting matrix, and counting matrices have equal row sums. There is no way around this.

## But Real Algorithms Do Work Better

If all strategies are truly equal, why do real algorithms outperform random guessing in practice?

Because real problems are not drawn uniformly from all possible problems. The real world has structure.

Consider the A-star algorithm, one of the most effective pathfinding algorithms ever developed. A-star uses a heuristic to decide which paths to explore first. In our network, if B is geographically close to D, A-star's heuristic estimates that the path through B is likely shorter. It explores that path first.

This heuristic relies on a specific assumption about the world: that geographic proximity correlates with travel distance. In Euclidean space, this is guaranteed. If B is close to D as the crow flies, then the travel distance from B to D cannot be wildly longer than the straight-line distance. This property -- essentially the triangle inequality -- is what makes A-star's heuristic admissible, meaning it never overestimates the true remaining distance.

In the real world, this assumption holds. Roads may be winding, but a point that is one mile away as the crow flies is never a thousand miles away by road. A-star exploits this structure to prune bad paths without exploring them, which is what makes it fast and effective.

But now imagine a world with a trans-dimensional hopper -- a device that warps space so that two points that are far apart as the crow flies can have a travel distance of nearly zero--or even a physically impossible negative distance. In this world, node C might be geographically far from D, but the hopper road from C to D is absurdly short.

A-star's heuristic looks at C, estimates a long remaining distance based on the straight-line measurement, and concludes "that direction is not worth exploring." It prunes the path through C -- the path that, thanks to the hopper, is actually the shortest.

A-star does not just miss the optimal path. It confidently excludes it. Its heuristic, which is so reliable in the real world, becomes actively misleading in a world where the relationship between straight-line distance and travel distance is broken. But a random search strategy -- which assigns no meaning to geographic proximity and just tries paths arbitrarily -- would have an equal chance of stumbling onto the hopper path.

This is the No Free Lunch theorem made concrete. A-star's inductive bias is the assumption that geometry is well-behaved. That assumption makes it brilliant in our world and blind in the hopper world. The P-matrix contains both kinds of worlds, and the gains and losses cancel.

## The Connection to Neural Networks

The same logic applies to every learning algorithm we have discussed in this series.

Recall from the [inductive bias post](https://www.mindfiretechnology.com/blog/archive/the-inductive-bias-problem-why-machine-learning-needs-assumptions/) that Mitchell characterized backpropagation's inductive bias as "smooth interpolation between data points." A neural network trained with backpropagation assumes that the underlying function is smooth -- that nearby inputs produce nearby outputs. This is what allows it to generalize from training data to new examples.

But the NFL theorem tells us: for every smooth function where this assumption helps, there exists an anti-smooth function where it hurts by exactly the same amount. A function where nearby inputs map to wildly different outputs will fool the neural network into confidently predicting smooth transitions that do not exist. On that function, random guessing would do just as well.

The neural network's situation is identical to A-star's. Its inductive bias -- smoothness -- makes it powerful on the kinds of problems the real world actually presents. But that power comes at a cost: poor performance on problems that violate the assumption. The P-matrix contains both kinds, and the row sums are equal.

## The Connection to Popper

This is Mitchell's "futility of bias-free learning" -- from our [first post in this series](https://www.mindfiretechnology.com/blog/archive/bias-free-learning-is-impossible/) -- generalized to all of optimization.

Mitchell showed that a single learning algorithm with no inductive bias cannot generalize at all. The NFL theorem shows something broader: not only do you need an inductive bias to generalize, but no single inductive bias is universally best. Every bias helps on some problems and hurts on others. There is no free lunch.

And this is Karl Popper's point yet again. There is no universal method of discovery. There is no algorithm that works for everything. Every act of learning, every act of optimization, every act of scientific discovery requires prior assumptions about the structure of the problem. Those assumptions are what make progress possible -- but they are also what make us fallible. For some class of problems, they necessarily fail.

The question is never whether your algorithm has assumptions. It always does. The question is whether those assumptions match the world you are actually in.

The No Free Lunch Theorem was first proved by [Wolpert and Macready (1997)](https://www.cs.ubc.ca/labs/algorithms/reading_group/no_free_lunch.pdf). The P-matrix framework and counting matrix explanation is from [Ho and Pepyne (2001)](https://faculty.cc.gatech.edu/~bboots3/CS4641-Fall2019/Lectures/08-20-2019-NoFreeLunch.pdf). All references to Mitchell are from [Machine Learning (McGraw-Hill, 1997)](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/mitchell/ftp/mlbook.html).
