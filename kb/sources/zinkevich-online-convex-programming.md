---
source: https://www.cs.cmu.edu/~maz/publications/techconvex.pdf
description: Carnegie Mellon technical report introducing online convex programming, regret guarantees, and generalized infinitesimal gradient ascent (GIGA).
captured: 2026-07-21
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Online Convex Programming and Generalized Infinitesimal Gradient Ascent

Author: Martin Zinkevich
Source: https://www.cs.cmu.edu/~maz/publications/techconvex.pdf
Date: February 2003
Online Convex Programming
             and Generalized Infinitesimal Gradient Ascent

                                      Martin Zinkevich
                                        February 2003

                                               CMU-CS-03-110

                                         School of Computer Science
                                         Carnegie Mellon University

                                             Pittsburgh, PA 15213

                                                    Abstract
Convex programming involves a convex set F  Rn and a convex function c : F  R.
The goal of convex programming is to find a point in F which minimizes c. In this paper,
we introduce online convex programming. In online convex programming, the convex set is
known in advance, but in each step of some repeated optimization problem, one must select
a point in F before seeing the cost function for that step. This can be used to model factory
production, farm production, and many other industrial optimization problems where one
is unaware of the value of the items produced until they have already been constructed. We
introduce an algorithm for this domain, apply it to repeated games, and show that it is really
a generalization of infinitesimal gradient ascent, and the results here imply that generalized
infinitesimal gradient ascent (GIGA) is universally consistent.

Keywords: multiagent learning, online algorithms

1 Introduction

Imagine a farmer who decides what to plant each year. She has certain restrictions on
her resources, both land and labour, as well as restrictions on the output she is allowed to
produce. How can she select which crops to grow without knowing in advance what the
prices will be? Here we present an algorithm based on gradient descent which will earn her
almost as much as she could given that she knew all prices in advance but produced the same
amount of each crop year after year. This is an example of an online convex programming
problem.

    Online convex programming is a generalization of the well-studied experts problem [9, 23].
Imagine that one has n experts, each of which has a plan at each step with some cost. At
each round, one selects a probability distribution over experts. If x  Rn is defined such that
xi is the probability that one selects expert i, then the set of all probability distributions is
a convex set. Also, the cost function on this set is linear, and therefore convex.

    In this paper, we present an algorithm for general convex functions based on gradient
descent. The algorithm applies gradient descent in Rn, and then moves back to the set of
feasible points. There are three advantages to this algorithm. The first is that gradient
descent is a simple, natural algorithm that is widely used, and studying its behavior is of
intrinsic value. Secondly, this algorithm is more general than the experts setting, in that it
can handle an arbitrary sequence of convex functions, which has yet to be solved. Finally,
in online linear programs this algorithm can in some circumstances perform better than an
experts algorithm. While the bounds on the performance of most experts algorithms depends
on the number of experts, these bounds are based on other criterion which may sometimes be
lower. This relationship is discussed further in Section 4, and further comments on related
work can be found in Section 5. The main theorem is stated and proven in Section 2.1.

    The algorithm that motivated this study was infinitesimal gradient ascent [25], which
is an algorithm for repeated games. First, this result shows that infinitesimal gradient
ascent is universally consistent [11], and secondly it shows that GIGA, a nontrivial extension
developed here of infinitesimal gradient ascent to games with more than two actions, is
universally consistent. GIGA is defined in Section 3.3 and is proven universally consistent
in Section 3.4.

    Also, Bansal et al [2] use the results of this paper in the oblivious routing domain.

2 Online Convex Programming

Definition 1 A set of vectors S  Rn is convex if for all x, x  S, and all   [0, 1],
x + (1 - )x  S.

Definition 2 For a convex set F , a function f : F  R is convex if for all x, y  F , for
all   [0, 1],

                                 f (x) + (1 - )f (y)  f (x + (1 - )y)

    If one were to imagine a convex function R2  R, where the function described the
altitude, then the function would look like a valley.

Definition 3 A convex programming problem consists of a convex feasible set F and
a convex cost function c : F  R. The optimal solution is the solution that minimizes
the cost.

An example of a convex programming problem is that of a farmer who knows the restrictions
on labor and land before she begins, and also knows the demand for her goods in advance.

    Suppose that the farmer is not aware of the demand for her products before she begins.
She knows that the corresponding cost function is convex, but she is unaware of its actual
values. After the year is over and she has sold her items, she then becomes aware of her
profit, and can use this to plan the next year. This is an instance of an online convex
programming problem.

Definition 4 An online convex programming problem consists of a feasible set F 
Rn and an infinite sequence {c1, c2, . . . } where each ct : F  R is a convex function.

    At each time step t, an online convex programming algorithm selects a vector
xt  F . After the vector is selected, it receives the cost function ct.

Because all information is not available before decisions are made, online algorithms do not
reach "solutions",but instead achieve certain goals. See Section 2.1.

    Define x = x · x and d(x, y) = x - y . Throughout the remainder of the paper we
will make seven assumptions:

   1. The feasible set F is bounded. There exists N  R such that for all x, y  F ,
       d(x, y)  N .

   2. The feasible set F is closed. For all sequences {x1, x2, . . . } where xt  F for all t, if
       there exists a x  Rn such that x = limt xt, then x  F .

   3. The feasible set F is nonempty. There exists an x  F .
   4. For all t, ct is differentiable1.

   5. There exists an N  R such that for all t, for all x  F , ct(x)  N .
   6. For all t, there exists an algorithm, given x, which produces ct(x).
   7. For all y  Rn, there exists an algorithm which can produce argminxF d(x, y). We

       define the projection P (y) = argminxF d(x, y).

Given this machinery, we can describe our algorithm.

Algorithm 1 Greedy Projection Select an arbitrary x1  F and a sequence of learning
rates 1, 2, . . .  R+. In time step t, after receiving a cost function, select the next vector
xt+1 according to:

                                          xt+1 = P xt - tct(xt) .

The basic principle at work in this algorithm is quite clear if we consider the case where the
sequence {c1, c2, . . . } is constant. In this case, our algorithm is operating in an unchanging
valley. The boundary of the feasible set is the edge of the valley. By proceeding along the
direction opposite the gradient, we walk down into the valley. By projecting back into the
convex set, we skirt the edges of the valley.

    1Although we make the assumption that ct is differentiable, the algorithm can also work if there exists
an algorithm that, given x, can produce a vector g such that for all y, g · (y - x)  ct(y) - ct(x).

2.1 Analyzing the Performance of the Algorithm

We measure the performance of an algorithm in comparison to the the best algorithm in
hindsight that knows all of the cost functions and selects one fixed vector.

Definition 5 Given an algorithm A, and a convex programming problem (F, {c1, c2, . . . }),
if {x1, x2, . . . } are the vectors selected by A, then the cost of A until time T is

                                                                                          T

                                              CA(T ) = ct(xt).

                                                                                         t=1

The cost of a static feasible solution x  F until time T is

                                                                                           T

                                               Cx(T ) = ct(x).

                                                                                         t=1

The regret of algorithm A until time T is

                                       RA(T ) = CA(T ) - min Cx(T ).

                                                                                                 xF

    Our goal is to prove that the average regret of Greedy Projection approaches
zero. In order to state our results about bounding the regret of this algorithm, we need to
specify some parameters. First, let us define:

F = max d(x, y)

                 x,yF

c =                                              sup  ct(x) .

         xF,t{1,2,... }

Here is the first result derived in this paper:

Theorem 1 If t = t-1/2, the regret of the Greedy Projection algorithm is:

RG(T )   F 2T                                         1                                       c 2
                    +                                   T-2

Therefore, lim supT  RG(T )/T  0.

The first part of the bound is because we might begin on the wrong side of F . The second
part is because we always respond after we see the cost function.

Proof: First we show that without loss of generality, for all t there exists a gt  Rn such
that for all x, ct(x) = gt · x.

    First, begin with arbitrary {c1, c2, . . . }, run the algorithm and compute {x1, x2, . . . }.
Then define gt = ct(xt). If we were to change ct such that for all x, ct(x) = gt · x, the
behavior of the algorithm would be the same. Would the regret be the same?

    Because ct is convex, for all x:

ct(x)  (ct(xt)) · (x - xt) + ct(xt).

Therefore, for all x  F : ct(x)  gt · (x - xt) + ct(xt). Thus:

                  ct(xt) - ct(x)  ct(xt) - gt · (x - xt) + ct(xt)
                                       gt · xt - gt · x

Thus the regret would be at least as much with the modified sequence of functions.

    We define for all t, yt+1 = xt - tgt. Observe that xt+1 = P (yt+1). We will attempt to
bound the regret of not playing action x on round t.

                  yt+1 - x = (xt - x) - tgt
               (yt+1 - x)2 = (xt - x)2 - 2t(xt - x) · gt + t2 gt 2

Observe that in the expression a2 - 2ab + b2, a2 is a potential, 2ab is the immediate cost, and
b2 is the error (within a factor of 2t). We will now begin to fully flush out these properties.
For all y  Rn, for all x  F , (y - x)2  (P (y) - x)2 [13]. Also, gt  c . So

               (xt+1 - x)2  (xt - x)2 - 2t(xt - x) · gt + t2 c 2

               (xt - x) · gt  1 (xt - x)2 - (xt+1 - x)2 + t c 2
                                    2t                                                       2

Now, by summing we get:

          T

RG(T ) = (xt - x) · gt

          t=1

          T    1                                             t

                         t       2      t+1             2                                2
                      (x - x ) - (x - x ) + c
          t=1 2t 2

                                                                                   T  11     (xt - x)2 +  c 2 T
                                                                                         -                 2 t
          1 1  2 1 T +1  2 1
 (x - x ) - (x - x ) +                                                                t t-1                           t=1
          21                2T                             2 t=2

                1 1T 1 1                                        c 2 T
 F2 + -                                                    + 2 t

               21 2 t=2 t t-1                                                 t=1

          2 1 c 2 T
 F 2T + 2 t

                                              t=1

Now,  if  we  define  t  =  1 ,  then

                              t

                                       T T1
                                                   t =       
                                    t=1 t=1 t

                                                                T dt
                                                    1+ 

                                                              t=1 t

                                                               T
                                                    1+ 2 t

                                                    2 T -1

Plugging this into the above equation yields the result.

2.2 Regret Against a Dynamic Strategy

Another possibility for the offline algorithm is to allow a small amount of change. For
instance, imagine that the path that the offline algorithm follows is of limited size.

Definition 6 The path length of a sequence x1, . . . , xT is:

                                                                          T -1

                                                      d(xt, xt+1).

                                                                           t=1

Define A(T, L) to be the set of sequences with T vectors and a path length less than or equal
to L.

Definition 7 Given an algorithm A and a maximum path length L, the dynamic regret
RA(T, L) is:

                                   RA(T, L) = CA(T ) - min CA (T ).

                                                                                              A A(T,L)

Theorem 2 If  is fixed, the dynamic regret of the Greedy Projection algorithm is:

                                                  7 F 2 L F T  c 2
                              RG(T, L)  4 +  + 2

    The proof is in the appendix.

2.3 Lazy Projection

In this section, we define a different algorithm that performs suprisingly well.

Algorithm 2 (Lazy Projection) Select an arbitrary x1  F and a sequence of learning
rates 1, 2, . . .  R+. Define y1 = x1. In time step t, after receiving a cost function, define
yt+1:

                                             yt+1 = yt - tct(xt)

and select the vector:

                        xt+1 = P (yt+1).

Theorem 3 Given a constant learning rate , Lazy Projection's regret is:
                                                       F 2  c 2T

                                        RL(T )  2 + 2
    The proof is in the appendix.

3 Generalized Infinitesimal Gradient Ascent

In this section, we establish that repeated games are online linear programming problems,
and an application of our algorithm is universally consistent.

3.1 Repeated Games

From the perspective of one player, a repeated game is two sets of actions A and Y , and a

utility function u : A × Y  R. A pair in A × Y is called a joint action. For the example

in this section, we will think of a matching game. A = {a1, a2, a3}, Y = {y1, y2, y3}, where

u(a1, y1) = u(a2, y2) = u(a3, y3) = 1, and everywhere else u is zero.

As a game is being played, at each step the player will be selecting an action at random

based on past joint actions, and the environment will be selecting an action at random based

on past joint actions. We will formalize this later.

A history is a sequence of joint actions. Ht = (A × Y )t is the set of all histories of length

t. Define H =       Ht  to  be  the  set  of  all  finite  histories,  and  for  any  history  h    H,  define
               t=0

|h| to be the length of that history. An example of a history is:

               h = {(a3, y1), (a1, y2), (a2, y3), (a2, y2), (a3, y3), (a1, y2)}

In order to access the history, we define hi to be the ith joint action. Thus, h3 = (a2, y3),
h1,1 = a3 and h6,1 = a1. The utility of a history h  H is:

                                                           |h|

                                     utotal(h) = u(hi,1, hi,2).

                                                          i=1

The utility of the above example is utotal(h) = 2. We can define what the history would look
like if we replaced the action of the player with a2 at each time step.

                     ha2 = {(a2, y1), (a2, y2), (a2, y3), (a2, y2), (a2, y3), (a2, y2)}

Now, utotal(ha2) = 3. Thus we would have done better playing this action all the time.
The definition of regret of not playing action a for all h  H, for all a  A is:

                                Ra(h) = utotal(ha) - utotal(h)

In this example, the regret of not playing action a2 is Ra2(h) = 3 - 2 = 1. This regret of
not playing an action need not be positive. For instance, Ra1(h) = 1 - 2 = -1. Now, we

define the maximum regret, or just regret, to be:

                                     R(h) = max Ra(h).

                                                     aA

Here R(h) = 1. The most important aspect of this definition of regret is that regret is a
function of the resulting history, independent of the strategies that generated that history.

    Now, we introduce the definition of the behavior and the environment. For any set S,
define (S) to be the set of all probabilities over S. For a distribution D and a boolean

predicate P , we use the notation PrxD[P (x)] to indicate the probability that P (x) is true
given that x was selected from D.

    A behavior  : H  (A) is a function from histories of past actions to distributions
over the next action of the player. An environment  : H  (Y ) is a function from
the history of past actions to distributions over the next action of the environment. Define
H = (A × Y ) to be the set of all infinite histories, and h|t to be the history truncated
to the first t rounds. Define F,  (H) to be the distribution over histories of infinite
length when  and  play with each other.

Definition 8 A behavior  is universally consistent2 if for any  > 0 there exists a T

such that for all :

                     Pr t > T, R(h|t) > < .
                     hF,     t

    In other words, after some time, with high probability the average regret never again

exceeds . Observe that this convergence over time is uniform over all environments.

    We will need other distributions on histories later, so we define them now. We define
F T,  (HT ) to be the distribution over histories of length T when  and  play each other.
In addition to these operations, for all h where |h| < T we define FT,(h)  (HT ) as the
distribution when  and  begin with a history h and then play for T - |h| rounds.

3.2 Oblivious Deterministic Environments

An environment is an oblivious deterministic environment if it plays the same sequence of
actions regardless of the actions of the player. We will use this type of environment to bridge
the gap between the results in online linear programming and repeated games.

    Formally, an environment  : H  (Y ) is an oblivious deterministic environment if
there exists a function r : {1, 2, . . . }  Y where for all h  H:

                                            Pr [y = r(|h| + 1)] = 1.

                                                                y(h)

3.3 Formulating a Repeated Game as an Online Linear Program

For simplicity, suppose that we consider the case where A = {1, . . . , n}. Before each time
step in a repeated game, we select a distribution over actions. This can be represented as a
vector in a n-standard closed simplex, the set of all points x  Rn such that for all i, xi  0,
and i=1 n xi = 1. Define this to be F .

    Since we have a utility u instead of cost c, we will perform gradient ascent instead of
descent. The utility u is a linear function when the environment's action becomes known.

Algorithm 3 (Generalized Infinitesimal Gradient Ascent) Choose a sequence of
learning rates {1, 2, . . . }. Begin with an arbitrary vector x1  F . Then for each round
t:

    2This is the generally accepted definition of universally consistent, appearing in [12, 11, 15, 22]. A less
restrictive definition originally appeared in [10].

1. Play according to xt: play action i with probability xti.

2. Observe the action ht,2 of the other player and calculate:

                                           yit+1 = xit + tu(i, ht,2)
                                           xt+1 = P (yt+1)

  where P (y) = argminxF d(x, y), as before.                                             |A||u|, where:
In this online convex programming problem, F  2, and c 

|u| = max u(a, y) - min u(a, y).
                              (a,y)A×Y                (a,y)A×Y

Now, we can apply the result about greedy projection to get the following result:

Theorem 4 If t = t-1/2, the expected regret of GIGA for all oblivious deterministic envi-

ronments  : H  (Y ), for all a  A, for all T is:

            a                                            1            |A||u|2
EhF,[R (h|T )]  T +                                        T-2

3.4 Self-Oblivious Behavior

It is important to observe that the above is more a method of constructing a behavior than

an actual behavior. By proper simulation, the above can be reformulated into a behavior.

Before we begin, we fix x1. Then, whenever we see a history h  Ht, we simulate how

we would have constructed x2, . . . , xt based on the actions of the environment. Thus, given

x1, the above can be reformulated into  : H  (A) for any game.

Moreover,  here is self-oblivious, in that it only depends on the history of actions of

the environment. Define Y  =        Y  i,  and  2  :  H    Y    such  that  for  all  h    H,
                               i=0

2(h) = {h1,2, h2,2, h3,2, . . . , h|h|,2}

Definition 9 A behavior  is self-oblivious if there exists a function f : Y   (A) such
that for all h  H, (h) = f (2(h)).

Self-oblivious algorithms tend to be robust against adaptive adversaries, those that change
their technique based on past actions of the behavior.

    GIGA is self-oblivious, in that the strategy in the current time step can be calculated
given x1 (a constant) and the past actions of the environment. It should be noted that not
all algorithms are self-oblivious. For instance, Kalai and Vempala [19] describe an algorithm
that is not self-oblivious, because it uses a "random seed" at the beginning that an adaptive
adversary could learn over time and then use in some settings.

    The following lemma compartmentalizes the technique used at the end of [9].

Lemma 1 Given a self-oblivious behavior , if for every > 0 there exists a T such that,
for all deterministic, oblivious environments  : H  (Y ), for all a  A, for all t > T :

                               EhF,        Ra(h|t)         <

                                                   t

Then  is universally consistent. Therefore, GIGA is universally consistent.

The proof is in the appendix.

3.5 Lazy Projection and Fictitious Play

There have been some techniques presented to smooth fictitious play in [10], and here we
present a very simple version which has much of the "spirit" of fictitious play.

Algorithm 4 (Z Fictitious Play)Choose  > 0. At time step t define:

                                                                                 t-1

                                               yit = u(i, hj,2)

                                                                                 j=1

In other words, the total reward one would have received if one had played action i over the
entire history. Define:

                                     xt = P (yt) = argminx(A)d(x, yt)
Play according to xt in round t.

This algorithm is an instance of Lazy Projection.

4 Converting Old Algorithms

In this section, in order to compare our work with that of others, we show how one can
na¨ively translate algorithms for mixing experts into algorithms for online linear programs,
and online linear programming algorithms into algorithms for online convex programs. This
section is a discussion and no formal proofs are given.

4.1 Formal Definitions

We begin with defining the expert's problem.

Definition 10 An experts problem is a set of experts E = {e1, . . . , en} and a sequence
of cost vectors c1, c2, . . . where for all i, ci  Rn.

    On each round t, an expert algorithm (EA) first selects a distribution Dt  (E),
and then observes a cost vector ct.

    We assume that the EA can handle both positive and negative values. If not, it can be
easily extended by shifting the values into the positive range.

    Now, we define an abstract online linear programming problem.

Definition 11 An online linear programming problem is a closed convex polytope
F  Rn and a sequence of cost vectors c1, c2, . . . where for all i,ci  Rn.

    On each round t, an online linear programming algorithm (OLPA) first plays a
distribution Dt  (F ), and then observes a cost vector ct.

    An OLPA can be constructed from an EA, as described below.

Algorithm 5 Define v1, . . . , vk to be the vertices of the polytope for an online linear pro-
gram. Choose E = {e1, . . . , ek} to be the experts, one for each vertex.

    On each round t, receive a distribution Dt from the EA, and select vector vi if expert ei
is selected. Define c  Rk such that ci = ct · vi. Send EA the cost vector c  Rk.

    The optimal static vector must be a vertex of the polytope, because a linear program
always has a solution at a vertex of the polytope. If the original EA can do almost as well
as the best expert, this OLPA can do at least as well as the best static vector.

    The second observation is that most EA have bounds that depend on the number of
experts. The number of vertices of the convex polytope is totally unrelated to the diameter,
so any normal expert's bound is incomparable to our bound on Greedy Projection.

    There are some EA that begin with a distribution or uneven weighting over the experts.
These EA may perform better in this scenario, because that one might be able to tweak the
distribution such that it is spread evenly over the space (in some way) and not the experts,
giving more weight to lonely vertices and less weight to clustered vertices.

4.2 Converting an OLPA to an Online Convex Programming Al-
       gorithm

There are two reasons that the algorithm described above will not work for an online convex
program. The first is that an online convex program can have an arbitrary convex shape as
a feasible region, such as a circle, which cannot be described as the convex hull of any finite
number of points.

    The second reason is that a convex function may not have an minimum on the edge of
the feasible set. For instance, if F = {x : x · x  1} and c(x) = x · x, the minimum is in the
center of the feasible set.

    Now, this first issue is difficult to handle directly3, so we will simply assume that the
OLPA can handle the feasible region of the online convex programming problem. This can
be either because that the OLPA can handle an arbitrary convex region as in [19], or because
that the convex region of the convex programming problem is a convex polytope.

    We handle the second issue by converting the cost function to a linear one. In Theorem 1,
we find that the worst case is when the cost function is linear. This assumption depends on
two properties of the algorithm; the algorithm is deterministic, and the only property of the
cost function ct that is observed is ct(xt).

    Now, we form an Online Convex Programming algorithm.

Algorithm 6 (Exact) On each round t, receive Dt from the OLPA, and play xt = EXDt[X].
Send the OLPA the cost vector ct(xt).

    The algorithm is discrete and only observes the gradient at the point xt, thus we can
assume that the cost function is linear. If the cost function is linear, then:

                                       EXDt[ct(X)] = ct(EXDt[X]).

    xt may be difficult to compute, so instead of explicitly calculating xt, we can sample.

    3One can approximate a convex region by a series of increasingly complex convex polytopes, but this
solution is very undesirable.

Algorithm 7 (Approx) Select the number of samples s1, s2, . . . to be taken each round.
On each round t, sample X1, . . . , Xst independently from the distribution Dt. Play:

                                                  zt = 1 st Xi
                                                         st i=1

Send OLPA the cost vector ct(zt).

    We will bound the worst-case difference between Approx and Exact. There are several
difficulties in doing so. The first is that Approx is a randomized algorithm, so although
it only eventually takes the derivative at a single point, it has a probability of taking the
derivative at one of many points, and so both the value and the derivative matter at those
points. Secondly, the long-term strategy of the adversary, how it forces the algorithm to move
in certain directions, might depend on the random result. Therefore, we try to separate the
random element from the deterministic element in a new game. At round t:

1. Receive Dt from the OLPA.

2. Sample X1, . . . , Xst independently from distribution Dt.

3.  Calculate  and  reveal  to  the  adversary  zt  =    1   i=1 st Xi.
                                                         st

4. Calculate and reveal to the adversary xt = EXDt[X].

5. The adversary selects gt, ht  Rn where gt , ht  c .

6. Send the OLPA gt.

This game updates the OLPA in the same fashion as the Exact algorithm. We define the
super regret S as:

                            T                       T                      T

                   S(T ) = ht · (zt - xt) + gt · xt - min gt · x
                                                             xF
                            t=1                     t=1                    t=1

We can relate this super regret to the regret of both the Exact and Approx algorithms.

The second half of the super regret is the regret of the Exact algorithm on a sequence of

linear functions.                               T

                    E[S(T )] = E[ ht · (zt - xt)] + RExact(T )

                                     t=1

We can bound E[ht · (zt - xt)] based on the number of samples taken:

                            E[ht · (zt - xt)]  E[ c d(zt, xt)]
                            E[ht · (zt - xt)]  c E[d(zt, xt)]

Without loss of generality, we assume that xt = 0, 0  F .

                                E[d(0, zt)] = 1 E               Xi Xj 
                                                 st
                                                             i,j

For a random variable Y :                E[Y ]  E[Y 2]
We use this fact to prove that:

                         E[d(0, zt)]  1 E                    Xi · Xj
                                           st i,j

                         E[d(0, zt)]  1                 E     Xi 2
                                             st
                                                     i

                         E[d(0, zt)]  1              st F 2
                                             st

                                      t    F
                         E[d(0, z )]  
                                                 st

                     E[S(T )] = c F              T1
                                                      + RExact(T )
                                                 t=1 st

By choosing st = t,  T1
                     t=1 st  2 T - 1. Thus, by selecting st properly:

                     E[S(T )] = c F (2 T - 1) + RExact(T )

    We will now prove that S(T )  RApprox(T ). Imagine that in the approx algorithm
each round the adversary knew in advance the random selection zt before it selects the
cost function ct. This only increases the regret. In the new game, the adversary selects
gt = ct(zt). Therefore:

                     ct(zt) - ct(x)  gt · (zt - x)
                                          gt · (zt - xt + xt - x)
                                          gt · (zt - xt) + gt · (xt - x)

The adversary selects ht to be a vector of length c in the direction of zt - xt.

                         ht · (zt - xt) = c d(xt, zt)
                                            gt d(xt, zt)
                                            gt · (zt - xt)

So, finally:

                   ct(zt) - ct(x)  ht · (zt - xt) + gt · xt - gt · x

              T                       T                    T                 T

                   ct(zt) - ct(x)          ht · (zt - xt) + gt · xt - min gt · x
                                                                      xF
              t=1                     t=1                  t=1            t=1

                   RApprox(T )  S(T )

Therefore, for the proper number of samples:                          
                          E[RApprox(T )]  RExact(T ) + c        F (2 T - 1)

5 Related Work

Kalai and Vempala [19] have developed algorithms to solve online linear programming, which
is a specific type of online convex programming. They are attempting to make the algorithm
behave in a lazy fashion, changing its vector slowly, whereas here we are attempting to be
more dynamic, as is highlighted in sections 2.2 and 3.4.

    These algorithms were motivated by the algorithm of [25] which applies gradient ascent
to repeated games. We extend their algorithm to games with an arbitrary number of actions,
and prove universal consistency. There has been extensive work on regret in repeated games
and in the experts domain, such as [3, 8, 7, 9, 10, 12, 14, 15, 16, 23]. What makes this
work noteworthy in a very old field is that it proves that a widely-used technique in artificial
intelligence, gradient ascent, has a property that is of interest to those in game theory. As
stated in Section 4, experts algorithms can be used to solve online online linear programs
and online convex programming problems, but the bounds may become significantly worse.

    There are several studies of online gradient descent and related update functions, for ex-
ample [5, 20, 17, 21]. These studies focus on prediction problems where the loss functions are
convex Bregman divergences. In this paper, we are considering arbitrary convex functions,
in problems that may or may not involve prediction.

    Finally, in the offline case, [6] have done work on proving that gradient descent and
projection for arbitrary Bregman distances converges to the optimal result.

6 Conclusions and Future Work

In this paper, we have defined an online convex programming problem. We have established
that gradient descent is a very effective technique on this problem. This work was motivated
by trying to better understand the infinitesimal gradient ascent algorithm, and the techniques
developed we applied to that problem to establish an extension to infinitesimal gradient
ascent that is universally consistent.

    The simplicity of the algorithm allows for the expansion of these results into other areas.
For instance, here we deal with a Euclidean geometry: what if one considered gradient
descent on a noneuclidean geometry, like [1, 24]? Also, the simplicity of GIGA allows for
this algorithm to be extended for even stronger results, like WoLF[4].

Acknowledgements

As always, any errors or omissions in the work are the sole responsibility of the author.
We would like to thank Pat Riley for great help in developing the algorithm for the case
of repeated games, Adam Kalai for improving the proof and bounds of the main theorem,
and Michael Bowling, Avrim Blum, Nikhil Bansal, and Manfred Warmuth for their help and
suggestions with this research.

References

 [1] S. Amari. Natural gradient works efficiently in learning. Neural Computation, 10:251-
      276, 1998.

 [2] N. Bansal, A. Blum, S. Chawla, and A. Meyerson. Online oblivious routing. Submitted,
      2003.

 [3] D. Blackwell. An analog of the minimax theorem for vector payoffs. South Pacific J. of
      Mathematics, pages 1-8, 1956.

 [4] M. Bowling and M. Veloso. Convergence of gradient dynamics with a variable learning
      rate. In Proceedings of the Eighteenth International Conference on Machine Learning,
      pages 27-34, 2001.

 [5] N. Cesa-Bianchi, P. Long, and M. K. Warmuth. Worst-case quadratic bounds for on-
      line prediction of linear functions by gradient descent. IEEE Transactions on Neural
      Networks, 7:604-619, 1994.

 [6] S. Della Pietra, V. Della Pietra, and J. Lafferty. Duality and auxilary functions for
      Bregman distances. Technical Report CMU-CS-01-109, Carnegie Mellon University,
      1999.

 [7] D. Foster. A proof of calibration via Blackwell's approachability theorem. In Games
      and Economic Behavior, volume 29, pages 73-79, 1999.

 [8] D. Foster and R. Vohra. Regret in the on-line decision problem. Games and Economic
      Behavior, 29(1):7-35, 1999.

 [9] Y. Freund and R. Schapire. Adaptive game playing using multiplicative weights. In
      Games and Economic Behavior, volume 29, pages 79-103, 1999.

[10] D. Fudenberg and D. Levine. Universal consistency and cautious fictitious play. Journal
      of Economic Dynamics and Control, 19:1065-1089, 1995.

[11] D. Fudenberg and D. Levine. The Theory of Learning in Games. MIT Press, 1998.

[12] D. Fudenberg and D. Levine. Conditional universal consistency. Games and Economic
      Behavior, 29, 1999.

[13] C. Gentile and M. Warmuth. Proving relative loss bounds for online learning algorithms
      by the Bregman divergence. In The 13th Annual Conference on Computational Learning
      Theory, June 2000. Tutorial.

[14] J. Hannan. Approximation to bayes risk in repeated play. Annals of Mathematics
      Studies, 39:97-139, 1957.

[15] S. Hart and A. Mas-Colell. A simple adaptive procedure leading to correlated equilib-
      rium. Econometrica, 68:1127-1150, 2000.

[16] S. Hart and A. Mas-Colell. A general class of adaptive strategies. Journal of Economic
      Theory, 98:26-54, 2001.

[17] M. Herbster and M. K. Warmuth. Tracking the best linear predictor. Journal of Machine
      Learning Research, 1:281-309, 2001.

[18] W. Hoeffding. Probability inequalities for sums of bounded random variables. Journal
      of the American Statistical Association, 58:13-30, March 1963.

[19] A. Kalai and S. Vempala. Geometric algorithms for online optimization. Technical
      report, MIT, 2002.

[20] J. Kivinen and M. Warmuth. Exponentiated gradient versus gradient descent for linear
      predictors. Information and Computation, 132:1-64, 1997.

[21] J. Kivinen and M. Warmuth. Relative loss bounds for multidimensional regression
      problems. Machine Learning Journal, 45:301-329, 2001.

[22] D. Levine. Personal communication, 2003.

[23] N. Littlestone and M. K. Warmuth. The weighted majority algorithm. In Proceedings
      of the Second Annual Conference on Computational Learning Theory, 1989.

[24] R. Mahony and R. Williamson. Prior knowledge and preferential structures in gradient
      descent algorithms. Journal of Machine Learning Research, 1:311-355, 2001.

[25] S. Singh, M. Kearns, and Y. Mansour. Nash convergence of gradient dynamics in
      general-sum games. In Proceedings of the Sixteenth Conference in Uncertainty in Arti-
      ficial Intelligence, pages 541-548, 2000.

A Proof of Dynamic Bounds

Proof: Define zt to be the dynamic optimal strategy at time t. As before, we can argue
that:

R 1 T 1 G(T )  (xt - zt)2 - (xt+1 - zt)2 + c 2 T 
2                          2
t=1                           t=1

R 1 G(T )  (xt)2 - (xt+1)2 T + 1 T 1 2(xt+1 - xt) · (zt) + T  c 2
2         2                                          2
   t=1    t=1

RG(T )  1 (x1)2 - (xT +1)2 + 1 xT +1 · zT - 1 x1 · z1 T + 1 (zt-1 - zt) · (xt) + T  c 2
2                                                                  2
                                   t=2

Without loss of generality, assume 0  F . Thus for any a, b  F , a , b  F , and
- 4F 2  a · b  F 2. So:

R 7 F 2 T 1 G(T )  + d(zt-1, zt) F + T  c 2
4                                  2
                     t=2

                7 F 2 L F T  c 2
RG(T )  4 +  + 2

B Proof of Lazy Projection

In analyzing Greedy Projection, we had one potential: the distance from the optimal point.
In analyzing Lazy Projection, we have two potentials: the distance from yt to the optimal
point (ideal potential), and the distance to the set F (projection potential). The ideal
potential is "good", in the sense that we grow distant from the optimal point when we are
performing better than the optimal point. However, the projection potential is "bad", in
the sense that the farther we go from F , the more difference there is between the vector we
wanted to use (yt) and the vector we did use (xt). What makes Lazy Projection work is that
these two potentials cancel each other.

    For all y  Rn, for all closed, convex sets F  Rn, define d(y, F ) = minxF d(y, x).
    The following two proofs are the subcomponents of our general proof. We prove them in
Section B.3.

Lemma 2 (ideal potential) For any convex set F and any linear cost sequence ct, defining
yt as in the definition of Lazy Projection with a fixed learning rate , and any x  F :

 T                   F 2 d(yT +1, x)2 T  c 2
                      2 - 2 + 2
    ct(yt) - ct(x) 

t=1

Lemma 3 (projection potential) For any convex set F and any linear cost sequence ct,
defining yt and xt as in the definition of Lazy Projection:

T ct(xt) - ct(yt)  d(yT +1, F )2

t=1

    In Section B.1, we present an example highlighting the issues of Lemma 3. In Section B.2,
we prove the critical connection between the n-dimensional case and the one-dimensional
case. In Section B.3, we complete the proofs of Lemma 2, Lemma 3, and Theorem 3.

B.1 A Motivating Example

In order to motivate the following technical lemmas, let us consider an example. Choose
F = {x  R : x  a}. If yt  a, xt = P (yt) = a. Assume that  = 1 and the cost function
at time t is ct(x) = gt · x. We will attempt to bound the following difference D:

                                        T

                             D = ct(P (yt)) - ct(yt)

                                       i=1

D is how much less cost we would have accrued had we played the point yt instead of xt.
Let us assume that for all t, yt > a. So,

                                        T

                             D = ct(a) - ct(yt)

                                       i=1

Since gt = yt+1 - yt, then:

                                        T

                             D = (yt+1 - yt) · (yt - a)

                             i=1

Let us define zt = d(yt, F ) = minxF d(yt, x) = yt - a. The equation becomes:

                                        T

                             D = (zt+1 - zt)zt

                                       i=1

We can use the following lemma here:

Lemma 4 For all a, b  R:

                                           a2 - b2
                             (a - b)b  2

Proof: This is an algebraic manipulation of 0  (a - b)2.

Thus, we can form a potential:

                                                     T (zt+1)2 - (zt)2
                                          D 2

                                                                               i=1

                                                    (zT +1)2 - (z1)2
                                          D 2

                                                    (zT +1)2
                                          D 2

    The key step which varies from the general case is that in general (yt+1 -yt)·(yt -P (y)) =
(zt+1 - zt)(zt). However, we prove in the next section that the dot product is always less.

B.2 Geometric Lemmas

This section contains the technical details of the proof.
                                              Figure 1: Lemma 5
                                                               y

                                                             P(y)
                                                                  Fx

Lemma 5 Given a convex set F  Rn, if y  Rn and x  F , then (y-P (y))·(x-P (y))  0.
In other words, the angle between y,P (y), and x is not acute.
Proof: We will prove the contrapositive of the theorem. Consider a point x  F such that
(y - x ) · (x - x ) > 0. We will prove x = P (y). For all   [0, 1], define:

                                z() = (1 - )x + ()x = x + (x - x ).
We will prove that for small positive values of , z() is closer to y than x . Since F is
convex, z() is in F .

                   (y - z())2 = (y - x - (x - x ))2
                   (y - z())2 = 2(x - x )2 - 2(y - x ) · (x - x ) + (y - x )2
Observe that for 0 <  < (x-x )2 2(y-x )·(x-x ) , (y - z())2 < (y - x )2. Thus, P (y) = x .

                                              Figure 2: Lemma 6
                                                          y

                                                                  y'

                                                        x

Lemma 6 Given y, x, y  Rn, then
                              (y - x) · (y - y)  d(y, x)(d(y , x) - d(y, x)).

Proof: We begin with a simple example. Suppose that x, y, y  R2, x = (0, 0), and
y = (1, 0). We can prove that the property holds for these three vectors.

                                                   (y - x) · (y - y) = (y1 - 1)
                          d(y, x)(d(y , x) - d(y, x)) = (y1)2 + (y2)2 - 1

                                        d(y, x)(d(y , x) - d(y, x))  (y1) - 1

Now, suppose that for a specific y,x,y , we have proven that the property holds. Then, it
will hold for y + a, x + a, y + a (a translation), because:
((y + a) - (x + a)) · ((y + a) - (y + a)) = (y - x) · (y - y)

                                                      d(y, x)(d(y , x) - d(y, x))
                                                      d(y + a, x + a)(d(y + a, x + a) - d(y + a, x + a))
Also, if it holds for y,x,y , then it will hold for ky, kx, and ky (a scaling), because:
                    (ky - kx) · (ky - ky) = k2(y - x) · (y - y)
                                                    k2d(y, x)(d(y , x) - d(y, x))
                                                    d(ky, kx)(d(ky , kx) - d(ky, kx))
Also, the property is invariant under a rotation. Define AT to be the transpose of the matrix
A, and aT to be the transpose of the vector a. Suppose that R is an orthonormal matrix
(where RT R = I). Now, for all a, b  Rn:
                            (Ra) · (Rb) = (Ra)T Rb = aT RT Rb = aT b = a · b
               d(Ra, Rb) = (R(a - b)) · (R(a - b)) = (a - b) · (a - b) = d(a, b)
We can now prove that if the property holds for y,x,y , then it will hold for Ry, Rx, Ry .
                 (Ry - Rx) · (Ry - Ry) = (R(y - x)) · (R(y - y))
                                                  = (y - x) · (y - y)
                                                   d(y, x)(d(y , x) - d(y, x))
                                                   d(Ry, Rx)(d(Ry , Rx) - d(Ry, Rx))

Observe that we can think of R2 as embedded in Rn without changing distance or dot product.
Any three vectors y, x, y can be obtained from (0, 1, 0, . . . , 0), (0, 0, 0, . . . , 0), (y1, y2, 0, . . . , 0)
using translation, scaling, and rotation. So the property holds for all vectors y, x, y .

                                              Figure 3: Lemma 7
                                                     y

                                                            y'' y'
                                                   x

                                                             x'

Lemma 7 Given y, x, x , y  Rn, where (y - x) · (x - x)  0(i.e. the angle is not acute),
then:

                              (y - x) · (y - y)  d(y, x)(d(y , x ) - d(y, x))
Corollary 1 Given y, y  Rn, if z = d(y, P (y)) and z = d(y , P (y )):

                                                                           (z )2 - z2
                              (y - P (y)) · (y - y)  z(z - z)  2
Proof: If y = x, then the result is trivial. Thus, assume y = x. We begin with an example,
as before. We assume y, x, x , y  R3, y = (1, 0, 0), x = (0, 0, 0), and x3 = 0.
    Throughout the next part of the proof, we prove that the worst case occurs when x = x .
We do this by defining y = y - x + x, and replacing y with y and x with x. Observe
first that d(y , x) = d(y , x ).
    Observe that (y - x) · (y - y) = y1 - 1, and (y - x) · (y - y) = y1 - x1 - 1. Since
(y - x) · (x - x) = x1, x1  0. Thus, (y - x) · (y - y)  (y - x) · (y - y), so the relationship
only gets tighter as we force x = x . Thus, the property holds for these vectors by Lemma 6.
    As in Lemma 6, we can prove that the property is invariant under a transformation,
rotation, or scaling.

B.3 Completing the Proof

Now, we complete the proofs. The first part is similar to Theorem 1, and the second is a
generalization of the argument in Section B.1.

Proof (of Lemma 2, ideal potential): First, define A (the quantity we are trying to

bound):

                                                 T

                                      A = ct(yt) - ct(x)

                                          i=1

For all t there exists a gt such that ct(x) = gt · x.

                                                 T

                                      A = gt · (yt - x)

                                               t=1

By definition, yt+1 = yt - gt. Similar to Theorem 1:

                  yt+1 - x = yt - x - gt

                  (yt+1 - x)2 = (yt - x - gt)2

                  gt · (yt - x) = (yt - x)2 - (yt+1 - x)2 +  gt 2
                                                   2                 2

                  gt · (yt - x)  (yt - x)2 - (yt+1 - x)2 +  c 2
                                                   2                    2

Summing, we get:

                                  T   (yt - x)2 - (yt+1 - x)2  c 2
                                                              +
                  A                            2                     2

                                 t=1

                  A  (y1 - x)2 - (yT +1 - x)2 T  c 2
                                                       +
                                          2                       2

Since y1, x  F :

                             F 2 d(yT +1, F )2 T  c 2
                     A  2 - 2 + 2

Proof (of Lemma 3, projection potential): First, define B (the quantity we are trying
to bound):

                                      B=  T

                                             ct(xt) - ct(yt)

                                          t=1

                                      B=  T

                                             ct(P (yt)) - ct(yt)

                                          t=1

For all t there exists a gt such that ct(x) = gt · x.

                                                 T

                                      B = gt · (P (yt) - yt)

                                                t=1

Also, gt =  yt-yt+1 . Thus:

                                    1  T

                                            t  t+1          t  t
                             B =  (y - y ) · (P (y ) - y )
                                       t=1

                                    1  T

                                            t       t     t+1  t
                             B =  (y - P (y )) · (y - y )
                                       t=1

Using Corollary 1:

                                       1 T d(yt+1, F )2 - d(yt, F )2
                             B 2

                                                t=1

                                       d(yT +1, F )2
                             B  2

Proof (of Theorem 3): Since lazy projection is a deterministic algorithm, and it only
considers ct(xt), then the worst case is a linear function. Therefore, we only need to
consider linear functions.

                                 T

                    RG(T ) =        ct(xt) - ct(x)

                              t=1

                                 T                     T

                    RG(T ) = (ct(xt) - ct(yt)) + (ct(yt) - ct(x))

                              t=1                      t=1

Thus, by Lemma 2 and Lemma 3:

RG(T )                       F 2 d(yT +1, F )2 T  c 2 d(yT +1, F )2
                             2 - 2 + 2 + 2

                             F 2 T  c 2
                                    +
                              2             2

C Proof of Universal Consistency

Our analysis of universal consistency first fixes a behavior , a time step T , an > 0 and an
action a  A. Then, we attempt to develop the environment  that maximizes the value:

                                               Pr [Ra(h) > T ]

                                                                     hFT,

We will use Doob's Decomposition from the theory of stochastic processes to divide the
regret into an "expected" part and a "random" part. We will then bound the expected part
of the regret to be lower than the worst case oblivious deterministic environment, due to the
fact that the behavior we are studying is self-oblivious. Then, we will bound the random
part with an old result from the theory of martingales.

    We first introduce some concepts from stochastic processes that will be useful later in
the proof.

Definition 12 A martingale difference sequence is a sequence of variables X1, X2, . . .
such that for all k, for all sequences X1, . . . , Xk:

E[Xk+1|X1, . . . , Xk] = 0

Lemma 8 (Azuma's Lemma) [18]: If X1, X2, . . . is a martingale difference sequence,
and for all i, |Xi|  b, then:

       k a2
Pr Xi > a  exp - 2b2k

        i=1

    Now, Doob's Decomposition allows us to construct a martingale difference sequence out
of an arbitrary random sequence Z1, Z2, . . . by:

Yi = Zi - E[Zi|Zi-1, . . . , Z1]

Corollary 2 If Z1, Z2, . . . is a random sequence and |Zi|  b, then:

       k a2
Pr Zi - E[Zi|Zi-1, . . . , Z1] > a  exp - 8b2k

        i=1

In this spirit, we define the functions V : H  R and V rem  : H  R:

        |h|

V(h) =       Ea (h|i-1)[Ra(a , hi,2)]

        i=1

V rem  (h) = Ra(h) - V(h)

Lemma 9 For any self-oblivious , for any T , a  A, there exists an oblivious, deterministic
environment  such that, for all h  HT :

                                          V(h)  EhFT, [Ra(h)]

Proof: Observe that HT is a finite set. Define h  HT :
                                            h = argmaxhHT V(h)

Now, choose some y  Y , and define  such that:

       Pr [y = h|h|+1,2  ] = 1 if |h| < T

     y(h)

             Pr [y = y ] = 1 if |h| > T

              y(h)

By construction,  is a deterministic, oblivious environment.  will play the actions in

2(h) for the first T rounds. Observe, that since  is self-oblivious, the distribution
of the actions of  at time step i is the same when  plays the actions in 2(h),
as when the past history is h|i-1. Therefore:

T

     Ea (h|i-1)[Ra(a                    , hi,2  )]  =  EhF T   [Ra(h)].
                                                       ,

i=1

We can use this fact to bound Ra with high probability. Define:

     |u| = max u(a, y) - min u(a, y)
     (a,y)A×Y                                       (a,y)A×Y

Lemma 10 If for a self-oblivious behavior  and an a  A, for every > 0 there exists a
time t such that for every oblivious, deterministic environment , for every time T > t:

     EhFT, [Ra(h)] < T

Then, for any arbitrary environment  :

       Pr [Ra(h) > 2T ] < exp                          -T 2
                                                       8|u|2
     hF T,

Proof: Choose  to be any arbitrary environment and T > t. From Lemma 9, we can
define a oblivious, deterministic environment  such that:

     V (h)    EhF T                       [Ra(h)]      <      T
                                        ,

Thus, we have captured the "expected" part of the regret in an arbitrary environment.
Define Ra : A × Y such that:

     Ra(a , y) = u(a, y) - u(a , y)

Now, for all i  {1, . . . , T }, we define Yi:
                             Yi(h) = Ra(hi) - Ea (h|i-1)[Ra(a , hi,2))]

For all h  H,

                                        T

                        V rem  (h) =         Yi(h)

                                        i=1

                                                    T

                        Ra(h) = V(h) + Yi(h)

                                                    i=1

                                               T

                        Ra(h) < T + Yi(h)

                                               i=1

Also, for all h  Hi-1:

                        Eh F i (h)[Yi(h )] = 0

                                     ,

Also, for all i, for all h  H, |Yi(h)|  2|u|. Therefore, by Azuma's Lemma:

                                        T                -T 2
                                                         8|u|2
                           Pr [ Yi(h) < T ] < exp
                                                         -T 2
                         hF T, i=1                       8|u|2

                          Pr [Ra(h) < 2T ] < exp

                        hFT,

Lemma 11 If for a behavior , for every > 0 there exists a time t such that for every
oblivious, deterministic , for every a  A, for every time T > t:

                        EhFT, [Ra(h)] < T

Then, for any arbitrary environment  :

                          Pr [R(h) > 2T ] < |A|exp       -T 2
                                                         8|u|2
                        hF T,

Proof:

               Pr [R(h) > 2T ] = Pr [a  A, Ra(h) > 2T ]
               hF T,                    hF T,

                                               Pr [Ra < 2T ]
                                        aA hF T,

                                        -T 2
                         |A|exp 8|u|2

Proof (of Lemma 1): For a given > 0, we wish to find t such that:

                             Pr [T > t , R(h|T ) > T ] <

                            hF,

We begin by decomposing the infinite sequence of events. Now, for all t:

        Pr [T > t, R(h|T ) > T ]                               Pr [R(h|T )]
        hF,                                                    hF,
                                                       T =t+1

                                                               Pr [R(h)]
                                                       T =t+1 hFT,

Define  = /2. There exists a t such that, for all T > t :

              Pr [R(h) > 2T ] < |A|exp                         -T ( )2
                                                                8|u|2
             hFT,

Summing we get, for all t  t :

                                                        -T ( )2
         Pr [T > t, R(h|T ) > T ]                              |A|exp 32|u|2
                                                       T =t+1
        hF,

This is a geometric series. For simplicity, define r:

                                             -( )2
                                r = exp 32|u|2

The important fact is that 0 < r < 1. Calculating the sum:

                            Pr [T > t, R(h|T ) > T ]           |A|rt+1

             hF,                                               1-r  -1

Define t :                      1  (1 - r-1)
Thus, for all t > t :           t = ln r ln |A| - 1.
Thus, if t = max(t , t ) :
                                   |A|rt+1
                                   1 - r-1 < .

                             Pr [T > t , R(h|T ) > T ] 

                            hF,


