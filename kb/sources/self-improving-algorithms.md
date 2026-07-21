---
source: https://page.mi.fu-berlin.de/mulzer/pubs/selfimpSICOMP.pdf
description: Ailon et al.'s self-improving algorithms that learn an unknown product input distribution and converge to entropy-optimal sorting and Delaunay-triangulation performance
captured: 2026-07-21
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Self-Improving Algorithms

Author: Nir Ailon, Bernard Chazelle, Kenneth L. Clarkson, Ding Liu, Wolfgang Mulzer, and C. Seshadhri
Source: https://page.mi.fu-berlin.de/mulzer/pubs/selfimpSICOMP.pdf

Capture note: text extracted from the 26-page PDF. The PDF text layer's mathematical notation and occasional line/page artifacts are retained; page headers and footers are not interpreted.

SELF-IMPROVING ALGORITHMS∗
NIR AILON†, BERNARD CHAZELLE‡, KENNETH L. CLARKSON§, DING LIU‡,
WOLFGANG MULZER¶, AND C. SESHADHRI§
Abstract. We investigate ways in which an algorithm can improve its expected performance
by fine-tuning itself automatically with respect to an unknown input distribution D. We assume
here that D is of product type. More precisely, suppose that we need to process a sequence I1, I2, . . .
of inputs I = (x1, x2, . . . , xn) of some fixed length n, where each xi is drawn independently from
some arbitrary, unknown distribution Di. The goal is to design an algorithm for these inputs so that
eventually the expected running time will be optimal for the input distribution D =
Q
i Di.
We give such self-improving algorithms for two problems: (i) sorting a sequence of numbers and
(ii) computing the Delaunay triangulation of a planar point set. Both algorithms achieve optimal
expected limiting complexity. The algorithms begin with a training phase during which they collect
information about the input distribution, followed by a stationary regime in which the algorithms
settle to their optimized incarnations.
Key words. average case analysis, Delaunay triangulation, low entropy, sorting
AMS subject classifications. 68Q25, 68W20, 68W40
1. Introduction. The classical approach to analyzing algorithms draws a familiar litany of complaints: worst-case bounds are too pessimistic in practice, say the
critics, while average-case complexity too often rests on unrealistic assumptions. The
charges are not without merit. Hard as it is to argue that the only permutations we
ever want to sort are random, it is a different level of implausibility altogether to pretend that the sites of a Voronoi diagram should always follow a Poisson process or that
ray tracing in a BSP tree should be spawned by a Gaussian. Efforts have been made
to analyze algorithms under more complex models (eg, Gaussian mixtures, Markov
model outputs) but with limited success and lingering doubts about the choice of
priors.
Suppose we wish to compute a function f that takes I as input. We get a sequence
of inputs I1, I2, . . ., and wish to compute f(I1), f(I2), . . .. It is quite plausible to
assume that all these inputs are somehow related to each other. This relationship,
though exploitable, may be very difficult to express concisely. One way of modeling
this situation is to postulate a fixed (but complicated) unknown distribution D of
inputs. Each input Ij is chosen independently at random from D. Is it possible to
learn quickly something about D so that we can compute f(I) (I chosen from D)
faster? (Naturally, this is by no means the only possible input model. For example,
we could have a memoryless Markov source, where each Ij depends only on Ij−1.
However, for simplicity we will here focus on a fixed source that generates the inputs
independently.)
That is what a self-improving algorithm attempts to do. Initially, since nothing
is know about D, our self-improving algorithm can only provide some worst-case
∗Preliminary versions appeared as N. Ailon, B. Chazelle, S. Comandur, and D. Liu, Self-improving
Algorithms in Proc. 17th SODA, pp. 261–270, 2006; and K. L. Clarkson and C. Seshadhri, Selfimproving Algorithms for Delaunay Triangulations in Proc. 24th SoCG, pp. 148–155, 2008. This
work was supported in part by NSF grants CCR-998817, 0306283, ARO Grant DAAH04-96-1-0181.
†Computer Science Faculty, Technion, Haifa, Israel
‡Department of Computer Science, Princeton University, Princeton, NJ, USA
§
IBM Almaden Research Center, San Jose, CA, USA
¶Institut f¨ur Informatik, Freie Universit¨at Berlin, 14195 Berlin, Germany
D
I1, I2, I3, . . .
A
f(I1), f(I2), f(I3), . . .
Fig. 1.1. A self-improving algorithm A processes a sequence I1, I2, . . . of inputs drawn independently from a random source D.
guarantee. As the algorithm sees more and more inputs, it can learn something about
the structure of D. We call this the training phase of the self-improving algorithm.
During this phase, the algorithm collects and organizes information about the inputs
in the hope that it can be used to improve the running time (with respect to inputs
from D). The algorithm then moves to the limiting phase. Having decided that
enough has been learned about D, the algorithm uses this information to compute
f(I) faster. Note that this behavior is tuned to the distribution D.
Obviously, there is no reason why we should get a faster running time for all D.
Indeed, if f is the sorting function and D is the uniform distribution over permutations, then we require expected Ω(n log n) time to sort. On the other hand, if D was
a low-entropy source of inputs, it is quite reasonable to hope for a faster algorithm.
So when can we improve our running time? An elegant way of expressing this is to
associate (using information theory) an “optimal” running time for each distribution.
This is a sort of estimate of the best expected running time we can hope for, given
inputs chosen from a fixed distribution D. Naturally, the lower the entropy of D, the
lower this running time will be. In the limiting phase, our self-improving algorithm
should achieve this optimal running time.
To expect a good self-improving algorithm that can handle all distributions D
seems a bit ambitious, and indeed we show that even for the sorting problem there
can be no space-efficient such algorithm (even when the entropy is low). Hence, it
seems necessary to impose some kind of restriction on D. However, if we required D
to be, say, uniform or a Gaussian, we would again be stuck with the drawbacks of
traditional average case analysis. Hence, for self-improvement to be of any interest,
the restricted class of distributions should still be fairly general. One such class is
given by product distributions.
1.1. Model and Results. We will focus our attention on distributions D of
product type. Think of each input as an n-dimensional vector (x1, . . . , xn) over some
appropriate domain. This could be a list of numbers (in the case of sorting) or a list of
points (for Delaunay triangulations). Each xiis generated independently at random
from an arbitrary distribution Di, so D =
Q
i Di
. All the Di’s are independent of each
other. It is fairly natural to think of various portions of the input as being generated
by independent sources. For example, in computational geometry, the convex hull
of uniformly independently distributed points in the unit square is a well studied
problem.
Note that all our inputs are of the same size n. This might appear to be a rather
unnatural requirement for (say) a sorting algorithm. Why must the 10th number in
our input come from the same distribution? We argue that this is not a major issue
(for concreteness, let us focus on sorting). The right way to think of the input is as a
set of sources D1, D2, . . ., each independently generating a single number. The actual
“order” in which we get these numbers is not important. What is important is that
for each number, we know its source. For a given input, it is realistic to suppose that
numbers). Our self-improving sorters essentially perform an independent processing
on each input number, after which O(n) time is enough to sort.1 The algorithm is
completely unaffected by the inactive sources. To complete the training phase, we
only need to get enough information about each source. What if new sources are
introduced during the stationary phase? Note that as long as O(n/ log n) new sources
(and hence new numbers) are added, we can always include these extra numbers in
the sorted list in O(n) time. Once the number of new sources becomes too large, we
will have to go back to the training phase. This is, of course, quite acceptable: if
the underlying distribution of inputs changes significantly, we have to recalibrate the
algorithm. For these reasons, we feel that it is no loss of generality to deal with a
fixed input length, especially for product distributions.
Our first result is a self-improving sorter. Given a source D =
Q
i Di of realnumber sequences I = (x1, . . . , xn), let π(I) denote the permutation induced by the
ranks of the xi’s, using the indices i to break ties. Observe that since I is a random
variable, so is π(I). We can define the entropy H(π(I)), over the randomness of
D, and the limiting complexity of our algorithm will depend on H(π(I)). Note this
quantity may be much smaller than the entropy of the source itself but can never
exceed it.
As we mentioned earlier, the self-improving algorithm initially undergoes a training phase. At the end of this phase, some data structures storing information about
the distributions are constructed. In the limiting phase, the self-improving algorithm
is fixed, and these data structures do not change. In the context of sorting, the
self-improving sorter becomes some fixed comparison tree.
Theorem 1.1. There exists a self-improving sorter of O(n + H(π(I))) limiting
complexity, for any input distribution D =
Q
i Di. Its worst case running time is
O(n log n). No comparison-based algorithm can sort an input from D in less than
H(π(I)) time. For any constant ε > 0, the storage can be made O(n
1+ε
) for an
expected running time of O(ε
−1
(n+H(π(I)))). The training phase lasts O(n
ε
) rounds
and the probability that it fails is at most 1/n.
Why do we need a restriction on the input distribution? In §3.3, we show that a
self-improving sorter that can handle any distribution requires an exponentially large
data structure. Fredman [31] gave an algorithm that could optimally sort permutations from any distribution D. His algorithm needs to know D explicitly, and it
constructs lookup tables of exponential size. Our bound shows that Fredman’s algorithm cannot be improved. Furthermore, we show that even for product distributions
any self-improving sorter needs super-linear space. Hence, our time-space tradeoffs
are essentially optimal. We remind the reader that we focus on comparison-based
algorithms.
Theorem 1.2. Consider a self-improving algorithm that, given any fixed distribution D, can sort a random input from D in expected O(n + H(π(I))) time. Such
an algorithm requires 2
Ω(n log n)
bits of storage.
Let ε ∈ (0, 1). Consider a self-improving algorithm that, given any product distribution D =
Q
i Di, can sort a random input from D in expected ε
−1
(n + H(π(I)))
time. Such an algorithm requires a data structure of bit size n
1+Ω(ε)
.
For our second result, we take the notion of self-improving algorithms to the
angulation of a set of points in the Euclidean plane. Given a source D =
Q
i Di of
sequences I = (x1, . . . , xn) of points in R
2
, let T(I) denote the Delaunay triangulation
of I. If we interpret T(I) as a random variable on the set of all undirected graphs with
vertex set {1, . . . , n}, then T(I) has an entropy H(T(I)), and the limiting complexity
of our algorithm depends on this entropy.
Theorem 1.3. There exists a self-improving algorithm for planar Delaunay triangulations of O(n+H(T(I))) limiting complexity, for any input distribution D =
Q
Di.
Its worst case running time is O(n log n). For any constant ε > 0, the storage can be
made O(n
1+ε
) for an expected running time of O(ε
−1
(n + H(T(I)))). The training
phase lasts O(n
ε
) rounds and the probability that it fails is at most 1/n.
From the linear time reduction from sorting to computing Delaunay triangulations [14, Theorems 8.2.2 and 12.1.1], the lower bounds of Theorem 1.2 carry over to
Delaunay triangulations.
Both our algorithms follow the same basic strategy. During the training phase,
we collect data about the inputs in order to obtain a typical input instance V for D
with |V | = O(n), and we compute the desired structure S (a sorted list or a Delaunay
triangulation) on V . Then for each distribution Di, we construct an entropy optimal
search structure Di for S (ie, an entropy optimal binary search tree or a distribution
sensitive planar point location structure). In the limiting phase, we use the Di’s in
order to locate the components of a given input I in S. The fact that V is a typical
input ensures that I will be broken into individual subproblems of expected constant
size that can be solved separately, so we can obtain the desired structure for the input
V ∪ I in expected linear time (plus the time for the Di-searches). Finally, for both
sorting and Delaunay triangulation it suffices to know the solution for V ∪ I in order
to derive the solution for I in linear expected time [21, 22]. Thus, the running time of
our algorithms is dominated by the Di-searches, and the heart of the analysis lies in
relating this search time to the entropies H(π(I)) and H(T(I)), respectively.
1.2. Previous Work. Related concepts to self-improving algorithms have been
studied before. List accessing algorithms and splay trees are textbook examples of how
simple updating rules can speed up searching with respect to an adversarial request
sequence [5, 15, 35, 45, 46]. It is interesting to note that self-organizing data structures
were investigated over stochastic input models first [4, 6, 13, 32, 40, 44]. It was the
observation [11] that memoryless sources for list accessing are not terribly realistic
that partly motivated work on the adversarial models. It is highly plausible that both
approaches are superseded by more sophisticated stochastic models: for example,
hidden Markov models for gene finding or speech recognition or time-coherent models
for self-customized BSP trees [8] or for randomized incremental constructions [23].
Recently, Afshani et al. [1] introduced the notion of instance optimality, which can be
seen as a generalization of output-sensitivity. They consider the inputs as sets and
try to exploit the structure within each input for faster algorithms.
Much research has been done on adaptive sorting [30], especially on algorithms
that exploit near-sortedness. Our approach is conceptually different: we seek to
exploit properties, not of individual inputs, but of their distribution. Algorithmic
self-improvement differs from past work on self-organizing data structures and online
computation in two fundamental ways. First, there is no notion of an adversary: the
inputs are generated by a fixed, oblivious, random source D, and we compare ourselves
against an optimal comparison-based algorithm for D. In particular, there is no
within any given input but, rather, within the ensemble of input distributions.
A simple example highlights this difference between previous sorters and the selfimproving versions. For 1 ≤ i ≤ n, fix two random integers ai
, bi from {1, . . . , n2}.
The distribution Diis such that Pr[xi = ai] = Pr[xi = bi
Q
] = 1/2, and we take D =
n
i=1 Di
. Observe that every permutation generated by D is a random permutation,
since the ai’s and bi’s are chosen randomly. Hence, any solution in the adaptive, selforganizing/adjusting framework requires Ω(n log n) time, because no input Ij exhibits
any special structure to be exploited. On the other hand, our self-improving sorter
will sort a permutation from D in expected linear time during the limiting phase:
since D generates at most 2n different permutations, we have H(π(I)) = O(n).
2. Entropy and Comparison-based Algorithms. Before we consider sorting
and Delaunay triangulations, let us first recall some useful properties of information
theoretic entropy [28] and explain how it relates to our notion of comparison-based
algorithms.
Let X be a random variable with a finite range X . The entropy of X, H(X), is
defined as H(X) := P
x∈X Pr[X = x] log(1/Pr[X = x]). Intuitively, the event that
X = x gives us log(1/Pr[X = x]) bits of information about the underlying elementary
event, and H(X) represents the expected amount of information that can be obtained
from observing X. We recall the following well-known property of the entropy of the
Cartesian product of independent random variables [28, Theorem 2.5.1].
Claim 2.1. Let H(X1, . . . , Xn) be the joint entropy of independent random variables X1, . . . , Xn. Then
H(X1, . . . , Xn) = X
i
H(Xi).
We now define our notion of a comparison-based algorithm. Let U be an arbitrary
universe, and let X be a finite set. A comparison-based algorithm to compute a
function X : U → X is a rooted binary tree A such that (i) every internal node of
A represents a comparison of the form f(I) ≤ g(I), where f, g : U → R are arbitrary
functions on the input universe U; and (ii) the leaves of A are labeled with outputs
from X such that for every input I ∈ U, following the appropriate path for I leads
to the correct output X(I). If A has maximum depth d, we say that A needs d
comparisons (in the worst case). For a distribution D on U, the expected number of
comparisons (with respect to D) is the expected length of a path from the root to a
leaf in A, where the leaves are sampled according to the distribution that D induces
on X via X.
Note that our comparison-based algorithms generalize both the traditional notion
of comparison-based algorithms [27, Chapter 8.1], where the functions f and g are
required to be projections, as well as the notion of algebraic computation trees [9,
Chapter 16.2]. Here the functions f and g must be composed of elementary functions
(addition, multiplication, square root) such that the complexity of the composition is
proportional to the depth of the node. Naturally, our comparison-based algorithms
can be much stronger. For example, deciding whether a sequence x1, x2, . . . , xn of
real numbers consists of n distinct elements needs one comparison in our model,
whereas every algebraic computation tree for the problem has depth Ω(n log n) [9,
Chapter 16.2]. However, for our problems of interest, we can still derive meaningful
Claim 2.2. Let D be a distribution on a universe U and let X : U → X be a
random variable. Then any comparison-based algorithm to compute X needs at least
H(X) expected comparisons.
Proof. This is an immediate consequence of Shannon’s noiseless coding theorem [28, Theorem 5.4.1] which states that any binary encoding of an information
source such as X(I) must have an expected code length of at least H(X). Any
comparison-based algorithm A represents a coding scheme: the encoder sends the
sequence of comparison outcomes, and the decoder descends along the tree A, using
the transmitted sequence to determine comparison outcomes. Thus, any comparisonbased algorithm must perform at least H(X) comparisons in expectation.
Note that our comparison-based algorithms include all the traditional sorting
algorithms [27] (selection sort, insertion sort, quicksort, etc) as well as classic algorithms for Delaunay triangulations [12] (randomized incremental construction, divide
and conquer, plane sweep). A notable exception are sorting algorithms that rely
on table lookup or the special structure of the input values (such as bucket sort or
radix sort) as well as transdichotomous algorithms for sorting [33, 34] or Delaunay
triangulations [16–18].
The following lemma shows how we can use the running times of comparisonbased algorithms to relate the entropy of different random variables. This is a very
important tool that will be used to prove the optimality of our algorithms.
Lemma 2.3. Let D be a distribution on a universe U, and let X : U → X and
Y : U → Y be two random variables. Suppose that the function f defined by f :
(I, X(I)) 7→ Y (I) can be computed by a comparison-based algorithm with C expected
comparisons (where the expectation is over D). Then H(Y ) = C + O(H(X)), where
all the entropies are with respect to D.
Proof. Let s : X(U) → {0, 1}
∗ be a unique binary encoding of X(U). By unique
encoding, we mean that the encoding is 1−1. We denote the expected code length of s
with respect to D, ED[|s(X(I))|], by Es. By another application of Shannon’s noiseless
coding theorem [28, Theorem 5.4.1]), we have Es ≥ H(X) for any unique encoding s
of X(U), and there exists a unique encoding s
∗ of X(U) with Es
∗ = O(H(X)).
Using f, we can convert s
∗
into a unique encoding t of Y (U). Indeed, for every
I ∈ U, Y (I) can be uniquely identified by a string t(I) that is the concatenation of
s
∗
(X(I)) and additional bits that represent the outcomes of the comparisons for the
algorithm to compute f(I, X(I)). Thus, for every element y ∈ Y (U), we can define
t(y) as the lexicographically smallest string t(I) for which Y (I) = y, and we obtain a
unique encoding t for Y (U). For the expected code length Et of t, we get
Et = ED[|t(Y (I))|] ≤ ED[C + |s
∗
(X(I))|] = C + Es
∗ = C + O(H(X)).
Since Shannon’s theorem implies Et ≥ H(Y ), the claim follows.
3. A Self-Improving Sorter. We are now ready to describe our self-improving
sorter. The algorithm takes an input I = (x1, x2, . . . , xn) of real numbers drawn
from a distribution D =
Q
i Di (ie, each xi
is chosen independently from Di). Let
π(I) denote the permutation induced by the ranks of the xi’s, using the indices i
to break ties. By applying Claim 2.2 with U = R
n, X the set of all permutations
on {1, . . . , n}, and X(I) = π(I), we see that any sorter must make at least H(π(I))
expected comparisons. Since it takes Ω(n) steps to write the output, any sorter needs
Ω(H(π(I)) + n) steps. This is, indeed, the bound that our self-improving sorter
For simplicity, we begin with the steady-state algorithm and discuss the training
phase later. We also assume that the distribution D is known ahead of time and that
we are allowed some amount of preprocessing before having to deal with the first input
instance (§3.1). Both assumptions are unrealistic, so we show how to remove them to
produce a bona fide self-improving sorter (§3.2). The surprise is how strikingly little
of the distribution needs to be learned for effective self-improvement.
3.1. Sorting with Full Knowledge. We consider the problem of sorting I =
(x1, . . . , xn), where each xiis a real number drawn from a distribution Di. We can
assume without loss of generality that all the xi’s are distinct. (If not, simply replace
xi by xi + iδ for an infinitesimally small δ > 0, so that ties are broken according to
the index i.)
The first step of the self-improving sorter is to sample D a few times (the training
phase) and create a “typical” instance to divide the real line into a set of disjoint,
sorted intervals. Next, given some input I, the algorithm sorts I by using the typical
instance, placing each input number in its respective interval. All numbers falling
into the same intervals are then sorted in a standard fashion. The algorithm needs a
few supporting data structures.
• The V -list: Fix an integer parameter λ = dlog ne, and sample λ input
instances from Q
Di. Form their union and sort the resulting λn-element
multiset into a single list u1 ≤ · · · ≤ uλn. Next, extract from it every λth item and form the list V = (v0, . . . , vn+1), where v0 = 0, vn+1 = ∞,
and vi = uiλ for 1 ≤ i ≤ n. Keep the resulting V -list in a sorted table as
a snapshot of a “typical” input instance. We will prove the remarkable fact
that, with high probability, locating each xiin the V -list is linearly equivalent
to sorting I. We cannot afford to search the V -list directly, however. To do
that, we need auxiliary search structures.
• The Di-trees: For any i ≥ 1, let B
V
i be the predecessor2 of a random y
from Diin the V -list, and let HV
i be the entropy of B
V
i
. The Di-tree is
defined to be an optimum binary search tree [41] over the keys of the V -list,
where the access probability of vk is PrDi

xi ∈ [vk, vk+1)

= PrB
V
i = k

, for
any 0 ≤ k ≤ n. This allows us to compute B
V
i using O(HV
i + 1) expected
comparisons.
The self-improving sorter. The input I is sorted by a two-phase procedure.
First we locate each xiin the V -list using the Di-trees. This allows us to partition
I into groups Z0 < Z1 < · · · of xi’s sharing the same predecessor in the V -list. The
first phase of the algorithm takes O(n +
P
i HV
i
) expected time.3 The next phase
involves going through each Zk and sorting their elements naively, say using insertion
sort, in total time O(
P
k
|Zk|
2
). See Fig. 3.1.
The expected running time is O(n+ED[
P
i HV
i +
P
k
|Zk|
2
]), and the total space
used is O(n
2
). This can be decreased to O(n
1+ε
) for any constant ε > 0; we describe
how at the end of this section. First, we show how to bound the running time of the
first phase. This is where we really show the optimality of our sorter.
2Throughout this paper, the predecessor of y in a list refers to the index of the largest list element
≤ y; it does not refer to the element itself.
3The HV
i
’s themselves are random variables depending on the choice of the V -list. Therefore,
Training phase
D
I1, I2, I3, . . .
A
· · ·
D1 D2 D3
V
Limiting phase
I = (x1, x2, . . . , xn)
· · ·
D1 D2 Dn
V ∪ I
I
Fig. 3.1. The self-improving sorter: during the training phase, the algorithm constructs a
typical sorted list, the V -list, and a sequence D1, D2, . . . of optimal search trees for V with respect
to D1, D2, . . .. In the limiting phase, the algorithm uses the Di’s to locate the xi’s in the V -list,
sorts the individual buckets, and removes the elements from V .
Lemma 3.1.
X
i
HV
i = O(n + H(π(I))).
Proof. Our proof actually applies to any linear sized sorted list V . Let B
V
:=
(B
V
1
, . . . , B
V
n
) be the sequence of predecessors for all elements in I. By Claim 2.1, we
have H(B
V
) = P
i HV
i
, so it suffices to bound the entropy of H(B
V
). By Lemma 2.3
applied with U = R
n, X(I) = π(I) and Y (I) = BV
, it suffices to give a comparisonbased algorithm that can determine B
V
(I) from (I, π(I)) with O(n) comparisons. But
this is easy: just use π(I) to sort I (which needs no further comparisons) and then
merge the sorted list I with V . Now the lemma follows from Claim 2.1.
Next we deal with the running time of the second phase. As long as the groups
Zk are small, the time to sort each group will be small. The properties of the V -list
ensure that this is the case.
Lemma 3.2. For 0 ≤ k ≤ n, let Zk = {xi| vk ≤ xi < vk+1} be the elements with
predecessor k. With probability at least 1 − n
−2 over the construction of the V -list,
we have ED

|Zk|

= O(1) and ED

|Zk|
2

= O(1), for all 0 ≤ k ≤ n.
Proof. Remember that the V -list was formed by taking certain elements from a
sequence ˆI = s1, s2, . . . , sλn that was obtained by concatenating λ = dlog ne inputs
I1, I2, . . .. Let si ≤ sj be any two elements from ˆI, and let t = [si, sj ). Note that
all the other λn − 2 numbers are independent of si and sj . Suppose we fix the values
of si and sj (in other words, we condition on the values of si and sj ). For every
` ∈ {1, . . . , λn} \ {i, j}, let Y
(t)
`
be the indicator random variable for the event that
s` ∈ t, and let Y
(t)
:= P
`
Y
(t)
`
. Since all the Y
(t)
`
’s are independent, by Chernoff’s
bound [42, Theorem 4.2], for any β ∈ [0, 1],
Pr[Y
(t) ≤ (1 − β)E[Y(t)
]] ≤ exp−β
2E[Y(t)
]/2

. (3.1)
Setting β = 10/11, we see that if E[Y
(t)
] > 11dlog ne, then Y
(t) > dlog ne with
probability at least 1 − 1/(λ
2n4
Therefore, we get the above statement even with the unconditioned random variable
Y
(t)
. Now, by applying the same argument to any pair si, sj with i 6= j and taking
a union bound over all
λn
2

such pairs, we get that with probability at least 1 − n
−2
over the construction of ˆI the following holds for all half-open intervals t defined by
pairs si, sj with i 6= j: if E[Y
(t)
] > 11dlog ne, then Y
(t) > dlog ne. From now on we
assume that this implication holds.
The V -list is constructed such that for tk = [vk, vk+1), Y
(tk) ≤ dlog ne, and hence
E[Y
(tk)
] = O(log n). Let X
(tk)
i
be the indicator random variable for the event that
xi ∈R Dilies in tk, and X(tk):= P
i X
(tk)
i = |Zk|. Note that (where a and b denote
the indices of vk and vk+1 in ˆI)
E[Y
(tk)
] = X
`6=a,b
E[Y
(tk)
`
] ≥
X
i
λE[X
(tk)
i
] − 2 = dlog neE[X(tk)] − 2,
and therefore E[X(tk)] = O(1). Now, since the expectation of X(tk)is constant, and
since X(tk)is a sum of independent indicator random variables, we can apply the
following standard claim in order to show that the second moment of X(tk)is also
constant.
Claim 3.3. Let X =
P
i Xi be a sum of independent positive random variables
with Xi = O(1) for all i and E[X] = O(1). Then E[X2] = O(1).
Proof. By linearity of expectation,
E

X2

= E
hX
i
Xi
2
i
=
X
i
E

X2
i

+ 2X
i<j
E[Xi]E[Xj ]
≤
X
i
O (E[Xi]) + X
i
E[Xi]
2
= O(1).
This concludes the proof of Lemma 3.2.
Combining Lemmas 3.1 and 3.2, we get the running time of our self-improving
sorter to be O(n + H(π(I))). This proves the optimality of time taken by the sorter.
We now show that the storage can be reduced to O(n
1+ε
), for any constant ε > 0.
The main idea is to prune each Di-tree to depth ε log n. This ensures that tree has size
O(n
ε
), so the total storage used is O(n
1+ε
). We also construct a completely balanced
binary tree T for searching in the V -list. Now, when we wish to search for xiin the
V -list, we first search using the pruned Di-tree. At the end, if we reach a leaf of the
unpruned Di-tree, we stop since we have found the right interval of the V -list which
contains xi. On the other hand, if the search in the Di-tree was unsuccessful, then
we use T for searching.
In the first case, the time taken for searching is simply the same as with unpruned
Di-trees. In the second case, the time taken is O((1+ε) log n). But note that the time
taken with unpruned Di-trees is at least ε log n (since the search on the pruned Di-tree
failed, we must have reached some internal node of the unpruned tree). Therefore,
the extra time taken is only a O(ε
−1
) factor of the original time. As a result, the
space can be reduced to O(n
1+ε
) with only a constant factor increase in running time
(for any fixed ε > 0).
3.2. Learning the Distribution. In the last section we showed how to obtain
The V -list is built in the first dlog ne rounds, as before. The Di-trees will be built
after O(n
ε
) additional rounds, which will complete the training phase. During that
phase, sorting is handled via, say, mergesort to guarantee O(n log n) complexity. The
training part per se consists of learning basic information about B
V
i
for each i. For
notational simplicity, fix i and let pk = Pr[B
V
i = k] = Pr Di
[ vk ≤ xi < vk+1 ]. Let
M = cnε, for a large enough constant c. For any k, let χk be the number of times,
over the first M rounds, that vk is found to be the V -list predecessor of xi. (We
use standard binary search to compute predecessors in the training phase.) Finally,
define the Di-tree to be a weighted binary search tree defined over all the vk’s such
that χk > 0. Recall that the crucial property of such a tree is that the node associated
with a key of weight χk is at depth O(log(M/χk)). We apply this procedure for each
i = 1, . . . , n.
This Di-tree is essentially the pruned version of the tree we used in §4.1. Like
before, its size is O(M) = O(n
ε
), and it is used in a similar way as in §4.1, with a
few minor differences. For completeness, we go over it again: given xi, we perform
a search down the Di-tree. If we encounter a node whose associated key vk is such
that xi ∈ [vk, vk+1), we have determined B
V
i
and we stop the search. If we reach a
leaf of the Di-tree without success, we simply perform a standard binary search in
the V -list.
Lemma 3.4. Fix i. With probability at least 1 − 1/n3, for any k, if pk > n−ε/3
then M pk/2 < χk < 3M pk/2.
Proof. The expected value of χk is M pk. If pk > n−ε/3then, by Chernoff’s
bound [7, Corollary A.17] the count χk deviates from its expectation by more than
a = M pk/2 with probability less than (recall that M = cnε)
2 exp(−2a
2
/M) = 2 exp(−M p2
k/2) < 2 exp(−(c/2)n
2ε/3
) ≤ n
−4
,
for c large enough. A union bound over all k completes the proof.
Suppose now the implication of Lemma 3.4 holds for all k (and fixed i). We show
now that the expected search time for xiis O(ε
−1 HV
i + 1). Consider each element in
the sum HV
i =
P
k
pk log(1/pk). We distinguish two cases.
• Case 1: pk > n−ε/3. In this case, vk must be in Di, as otherwise we would
have χk = 0 by the definition of Di, a contradiction (for n large enough)
to Lemma 3.4, which states that χk > Mn−ε/3/2 . Hence, the cost of the
search is O(log(M/χk)), and its contribution to the expected search time is
O(pk log(M/χk)). By Lemma 3.4, this is also O(pk(1 + log p
−1
k
)), as desired.
• Case 2: pk ≤ n
−ε
. The search time is always O(log n); hence the contribution to the expected search time is O(ε
−1pk log p
−1
k
).
By summing up over all k, we find that the expected search time is O(ε
−1 HV
i +1).
This assumes the implication of Lemma 3.4 for all i. By a union bound, this holds
with probability at least 1 − 1/n2. The training phase fails when either this does not
hold, or if the V -list does not have the desired properties (Lemma 3.2). The total
probability of this is at most 1/n.
3.3. Lower Bounds. Can we hope for a result similar to Theorem 1.1 if we
drop the independence assumption? The short answer is no. As we mentioned earlier, Fredman [31] gave a comparison-based algorithm that can optimally sort any
distribution of permutations. This uses an exponentially large data structure to decide which comparisons to perform. Our lower bound shows that the storage used by
To understand the lower bound, let us try to abstract out the behavior of a
self-improving sorter. Given inputs from a distribution D, at each round, the selfimproving sorter is just a comparison tree for sorting. After any round, the selfimproving sorter may wish to update the comparison tree. At some round (eventually), the self-improving sorter must be able to sort with expected O(n + H(π(I)))
comparisons: the algorithm has “converged” to the optimal comparison tree. The
algorithm uses some data structure to represent (implicitly) this comparison tree.
We can think of a more general situation. The algorithm is explicitly given an
input distribution D. It is allowed some space where it stores information about D (we
do not care about the time spent to do this). Then, (using this stored information) it
must be able to sort a permutation from D in expected O(n + H(π(I))) comparisons.
So the information encodes some fixed comparison based procedure. As a shorthand
for the above, we will say that the algorithm, on input distribution D, optimally sorts
D. How much space is required to deal with all possible D’s? Or just to deal with
product distributions? These are the questions that we shall answer.
Lemma 3.5. Let h = (n log n)/α, for some sufficiently large constant α < 0, and
let A be an algorithm that can optimally sort any input distribution D with H(π(I)) ≤
h. Then A requires 2
Ω(n log n)
bits of storage.
Proof. Consider the set of all n! permutations of {1, . . . , n}. Every subset Π of 2h
permutations induces a distribution DΠ defined by picking every permutation in Π
with equal probability and none other. Note that the total number such distributions
DΠ is n!
2h

> (n!/2
h
)
2
h
and H(DΠ
<) = h, where DΠ< is the distribution on the output
π(I) induced by DΠ. Suppose there exists a comparison-based procedure AΠ that
sorts a random input from DΠ in expected time at most c(n + h), for some constant
c > 0. By Markov’s inequality this implies that at least half of the permutations in Π
are sorted by AΠ in at most 2c(n+h) comparisons. But, within 2c(n+h) comparisons,
the procedure AΠ can only sort a set P of at most 22c(n+h) permutations. Therefore,
any other Π0such that AΠ0 = AΠ will have to draw at least half of its elements from
P. This limits the number of such Π0to

n!
2
h/2
2
2c(n+h)
2
h/2

< (n!)2
h−1
2
c(n+h)2h
.
This means that the number of distinct procedures needed exceeds
(n!/2
h
)
2
h
/((n!)2
h−1
2
c(n+h)2h
) > (n!)2
h−1
2
−(c+1)(n+h)2h
= 2Ω(2hn log n),
assuming that h/(n log n) is small enough. A procedure is entirely specified by a string
of bits; therefore at least one such procedure must require storage logarithmic in the
previous bound.
We now show that a self-improving sorter dealing with product distributions
requires super-linear size. In fact, the achieved tradeoff between the O(n
1+ε
) storage
bound and an expected running time off the optimal by a factor of O(1/ε) is optimal.
Lemma 3.6. Let c > 0 be a large enough parameter, and let A be an algorithm
that, given a product distribution D, can sort a random permutation from D in expected
time c(n + H(π(I))). Then A requires a data structure of bit size n
1+Ω(1/c)
.
Proof. The proof is a specialization of the argument used for proving Lemma 3.5.
in {1, . . . , n} and making them equally likely to be picked as xi. (For convenience, we
use the tie-breaking rule that maps xi7→ nxi+i−1. This ensures that π(I) is unique.)
We then set D := Q
i Di
. By Claim 2.1, D has entropy n · bh/nc = Θ(h). This leads
to n
κ
n
> (n/κ)
κn choices of distinct distributions D. Suppose that A uses s bits of
storage and can sort each such distribution in c(n + h) expected comparisons. Some
fixing S of the bits must be able to accommodate this running time for a set G of at
least (n/κ)
κn2−s distributions D. In other words, some comparison-based procedure
can deal with (n/κ)
κn2−s distributions D. Any input instance that is sorted in at
most 2c(h + n) time by S is called easy: the set of easy instances is denoted by E.
Because S has to deal with many distributions, there must be many instances
that are easy for S. This gives a lower bound for |E|. On the other hand, since easy
instances are those that are sorted extremely quickly by S, there cannot be too many
of them. This gives an upper bound for |E|. Combining these two bounds, we get a
lower bound for s. We will begin with the easier part: the upper bound for |E|.
Claim 3.7. |E| ≤ 2
2c(h+n)+2
Proof: In the comparison-based algorithm represented by S, each instance I ∈ E
is associated with a leaf of a binary decision tree of depth at most 2c(h + n), ie,
with one of at most 22c(h+n)leaves. This would give us an upper bound on s if each
I ∈ E was assigned a distinct leaf. However, it may well be that two distinct inputs
I, I0 ∈ E have π(I) = π(I
0
) and lead to the same leaf. Nonetheless, we have a collision
bound, saying that for any permutation π, there are at most 4n instances I ∈ E with
π(I) = π. This implies that |E| ≤ 4
n22c(h+n)
.
To prove the collision bound, first fix a permutation π. How many instances can
map to this permutation? We argue that knowing that π(I) = π for an instance
I ∈ E, we only need 2n − 1 additional bits to encode I. This immediately shows that
there must be less than 4n such instances I. Write I = (x1, . . . , xn), and let I be
sorted to give the vector I = (y1, . . . , yn). Represent the ground set of I as an n-bit
vector α (αi = 1 if some xj = i, else αi = 0). For i = 2, . . . , n, let βi = 1 if yi = yi−1,
else βi = 0. Now, given α and β, we can immediately deduce the vector I, and by
applying π
−1
to I, we get I. This proves the collision bound.
Claim 3.8. |E| ≥ n
nκ−2n2−2s/κ
Proof: Each Diis characterized by a vector vi = (ai,1, . . . , ai,κ), so that D itself is
specified by v = (v1, . . . , vn) ∈ R
nκ. (From now on, we view v both as a vector and a
distribution of input instances.) Define the j-th projection of v as v
j = (a1,j , . . . , an,j ).
Even if v ∈ G, it could well be that none of the projections of v are easy. However,
if we consider the projections obtained by permuting the coordinates of each vector
vi = (ai,1, . . . , ai,κ) in all possible ways we enumerate each input instance from v
the same number of times. Note that applying these permutations gives us different
vectors which also represent D. Since the expected time to sort an input chosen
from D ∈ G is at most c(h + n), by Markov’s inequality, there exists a choice of
permutations (one for each 1 ≤ i ≤ n) for which at least half of the projections of the
vector obtained by applying these permutations are easy.
Let us count how many distributions have a vector representation with a choice
of permutations placing half its projections in E. There are fewer than |E|κ/2choices
of such instances and, for any such choice, each v
0
i = (ai,1, . . . , ai,κ) has half its entries
already specified, so the remaining choices are fewer than n
κn/2
. This gives an upper
bound of n
κn/2
|E|κ/2 on the number of such distributions. This number cannot be
smaller than |G| ≥ (n/κ)
κn2−s
; therefore |E| ≥ n
It now just remains to put the bounds together.
n
nκ−2n
2
−2s/κ ≤ 22c(h+n)+2
=⇒ n log n − 2n log κ − 2s/κ ≤ 2ch + 2cn + 2
=⇒ κn(log n − 2 log κ) − 2cκh − 2cκn − 2κ ≤ 2s.
We have κ = n
Θ(1/c) and h = (n log n)/(3c). Since c is sufficiently large, we get
s = n
1+Ω(1/c)
.
4. Delaunay Triangulations. We now consider self-improving algorithms for
Delaunay triangulations. The aim of this section is to prove Theorem 1.3. Let I =
(x1, . . . , xn) denote an input instance, where each xiis a point in the plane, generated
by a point distribution Di. The distributions Di are arbitrary, and may be continuous,
although we never explicitly use such a condition. Each xiis independent of the others,
so in each round the input I is drawn from the product distribution D =
Q
i Di
, and
we wish to compute the Delaunay triangulation of I, T(I). To keep our arguments
simple, we will assume that the points of I are in general position (ie, no four points
in I lie on a common circle). This is no loss of generality and does not restrict the
distribution D, because the general position assumption can always be enforced by
standard symbolic perturbation techniques [29]. Also we will assume that there is
a bounding triangle that always contains all the points in I. Again, this does not
restrict the distribution D in any way, because we can always simulate the bounding
triangle symbolically by adding virtual points at infinity.
The distribution D induces a (discrete) distribution on the set of Delaunay triangulations, viewed as undirected graphs with vertex set {1, . . . , n}. Consider the
entropy of this distribution: for each graph G on {1, . . . , n}, let pG be the probability
that it represents the Delaunay triangulation of I ∈R D. We have the output entropy H(T(I)) := −
P
G pG log pG. By Claim 2.2, any comparison-based algorithm
to compute the Delaunay triangulation of I ∈R D needs at least H(T(I)) expected
comparisons. Hence, an optimal algorithm will be one that has an expected running
time of O(n + H(T(I))) (since it takes O(n) steps to write the output).
We begin by describing the basic self-improving algorithm. (As before, we shall
first assume that some aspects of the distribution D are known.) Then, we shall
analyze the running time using our information theory tools to argue that the expected
running time is optimal. Finally, we remove the assumption that D is known and give
the time-space tradeoff in Theorem 1.3.
4.1. The algorithm. We describe the algorithm in two parts. The first part
explains the learning phase and the data structures that are constructed (§4.1.1).
Then, we explain how these data structures are used to speed up the computation in
the limiting phase (§4.1.2). As before, the expected running time will be expressed
in terms of certain parameters of the data structures obtained in the learning phase.
In the next section (§4.2), we will prove that these parameters are comparable to the
output entropy H(T(I)). First, we will assume that the distributions Di are known
to us, and the data structures described will use O(n
2
) space. Section 4.3 repeats
the arguments of §3.2 to remove this assumption and to give the space-time tradeoff
bounds of Theorem 1.3.
As outlined in Fig. 4.1, our algorithm for Delaunay triangulation is roughly a
generalization of our algorithm for sorting. This is not surprising, but note that while
Sorting Delaunay Triangulation
Intervals (xi, xi
0 ) containing no values
of I
Delaunay disks
Typical set V Range space ε-net V [26,39], ranges are
disks, ε = 1/n
log n training instance points with the
same BV value
log n training instance points in each
Delaunay disk
Expect O(1) values of I within each
bucket (of the same B
V
index)
Expect O(1) points of I in each Delaunay disk of V
Optimal weighted binary trees Di Entropy-optimal planar point location
data structures Di[10]
Sorting within buckets Triangulation within V(Zs) ∩ s (Claim
4.5)
Sorted list of V ∪ I T(V ∪ I)
Build sorted V from sorted V ∪I (trivial)Build T(I) from T(V ∪ I) [21, 22]
(analysis) merge sorted V and I (analysis) merge T(V ) and T(I) [19]
(analysis) recover the indices B
V
i
from
the sorted I (trivial)
(analysis) recover the triangles B
V
i
in
T(V ) from T(I) (Lemma 4.8)
Fig. 4.1. Delaunay triangulation algorithm as a generalization of the sorting algorithm
step for sorting is trivial, but the corresponding step for Delaunay triangulation uses
some relatively recent and sophisticated prior work.
4.1.1. Learning Phase. For each round in the learning phase, we use a standard
algorithm to compute the output Delaunay triangulation. We also perform some extra
computation to build some data structures that will allow speedup in the limiting
phase.
The learning phase is as follows. Take the first λ := dlog ne input lists I1, I2, . . .,
Iλ. Merge them into one list ˆI of λn = ndlog ne points. Setting ε := 1/n, find an
ε-net V ⊆ ˆI for the set of all open disks. In other words, find a set V such that for
any open disk C that contains more than ελn = dlog ne points of ˆI, C contains at
least one point of V . It is well known that that there exist ε-nets of size O(1/ε) for
disks [26, 38, 39, 43], which here is O(n). Furthermore, it is folklore that our desired
ε-net V can be constructed in time n(log n)
O(1), but there seems to be no explicit
description of such an algorithm for our precise setting. Thus, we present an algorithm
based on a construction by Pyrga and Ray [43] in Appendix A
Having obtained V , we construct the Delaunay triangulation of V , which we
denote by T(V ). This is the analog of the V -list for the self-improving sorter. We
also build an optimal planar point location structure (called D) for T(V ): given a
point, we can find in O(log n) time the triangle of T(V ) that it lies in [12, Chapter 6].
Define the random variable B
V
i
to be the triangle of T(V ) that xi falls into.4 Now
let the entropy of B
V
i be HVi
. If the probability that xi falls in triangle t of T(V ) is
p
t
i
, then HV
i = −
P
t
p
t
i
log p
t
i
. For each i, we construct a search structure Di of size
O(n) that finds B
V
i
in expected O(HV
i
) time. These Di’s can be constructed using
the results of Arya et al. [10], for which the expected number of primitive comparisons
4Assume that we add the vertices of the bounding triangle to V . This will ensure that xi will
always fall in some triangle B
V
i
T(V )
y
z
t x 1
t2
t3
Fig. 4.2. Conflicts between T(V ) and the inputs: the input point x conflicts with triangles t1
and t2, y conflicts with t1, t2, and t3, and z conflicts only with t3.
is HV
i + o(HVi
). These correspond to the Di-trees used for sorting.
We will now prove an analog to Lemma 3.2 which shows that the triangles of
T(V ) do not contain many points of a new input I ∈R D on the average. Consider a
triangle t of T(V ) and let Ct be its circumscribed disk; Ct is a Delaunay disk of V .
If a point xi ∈ I lies in Ct, we say that xiis in conflict with t and call t a conflict
triangle for xi. Refer to Fig. 4.2. (The “conflict” terminology arises from the fact
that if xi were added to V , triangles with which it conflicts would no longer be in the
Delaunay triangulation.) Let Zt := I ∩ Ct, the random variable that represents the
points of I ∈R D that fall inside Ct, the conflict set of t. Furthermore, let Xt := |Zt|.
Note that the randomness comes from the random distribution of ˆI (on which V and
T(V ) depend), as well as the randomness of I. We are interested in the expectation
E[Xt] over I of Xt. All expectations are taken over a random input I chosen from D.
Lemma 4.1. For any triangle t of T(V ), let Zt = {xi| xi ∈ Ct} be the conflict
set of t, and define Xt := |Zt|. With probability at least 1 − n
−2 over the construction
of T(V ), we have E[Xt] = O(1) and E[X2
t
] = O(1), for all triangles t of T(V ).
Proof. This is similar to the argument given in Lemma 3.2 with a geometric twist.
Let the list of points ˆI be s1, . . . , sλn, the concatenation of I1 through Iλ. Fix three
distinct indices i, j, k and the triangle t with vertices si, sj , sk (so we are effectively
conditioning on si, sj , sk). Note that all the remaining λn − 3 points are chosen
independently of si, sj , sk, from some distribution D`. For each ` ∈ {1, . . . , λn} \
{i, j, k}, let Y
(t)
`
be the indicator variable for the event that s` is inside Ct. Let
Y
(t) =
P
`
Y
(t)
`
. Setting β = 11/12 in (3.1), we get that if E[Y
(t)
] > 12dlog ne, then
Y
(t) > dlog ne with probability at least 1 − 1/(λ3n5
). This is true for every fixing
of si, sj , sk, so it is also true unconditionally. By applying the same argument to
any triple i, j, k of distinct indices, and taking a union bound over all
λn
3

triples,
we obtain that with probability at least 1 − n
−2
, for any triangle t generated by the
points of ˆI, if E[Y
(t)
] > 12dlog ne, then Y
(t) > dlog ne. We henceforth assume that
this event happens.
Consider a triangle t of T(V ) and its circumcircle Ct. Since T(V ) is Delaunay, Ct
contains no point of V in its interior. Since V is a (1/n)-net for all disks with respect
to ˆI, Ct contains at most dlog ne points of ˆI, that is, Y
(t) ≤ dlog ne. This implies that
E[Y
(t)
] = O(log n), as in the previous paragraph. Since E[Y
(t)
] > log nE[Xt] − 3, we
obtain E[Xt] = O(1), as claimed. Furthermore, since Xt can be written as a sum of
independent indicator random variables, Claim 3.3 shows that E[X2
t
T(V )
xi
B
V
i
Fig. 4.3. Determining the conflict set for xi: the triangle B
V
i
containing xi is found via Di.
Then we perform a breadth-first search from B
V
i
until we encounter triangles that no longer conflict
with xi. The dark gray triangles form the conflict set of xi, the light gray triangles mark the end
of the BFS. Since the conflict set Si is connected, and since the dual graph has bounded degree, this
takes O(|Si|) steps.
4.1.2. Limiting Phase. We assume that we are done with the learning phase,
and have T(V ) with the property given in Lemma 4.1: for every triangle t ∈ T(V ),
E[Xt] = O(1) and E[X2
t
] = O(1). We have reached the limiting phase where the
algorithm is expected to compute the Delaunay triangulation with the optimal running
time. We will prove the following lemma in this section.
Lemma 4.2. Using the data structures from the learning phase, and the properties
of them that hold with probability at least 1−1/n2, in the limiting phase the Delaunay
triangulation of input I can be generated in expected O(n +
Pn
i=1 HV
i
) time.
The algorithm, and the proof of this lemma, has two steps. In the first step,
T(V ) is used to quickly compute T(V ∪ I), with the time bounds of the lemma.
In the second step, T(I) is computed from T(V ∪ I), using a randomized splitting
algorithm proposed by Chazelle et al. [21], who provide the following theorem.
Theorem 4.3. [21, Theorem 3] Given a set of n points P and its Delaunay
triangulation, for any partition of P into two disjoint subsets P1 and P2, the Delaunay triangulations T(P1) and T(P2) can be computed in O(n) expected time, using a
randomized algorithm.
The remainder of this section is devoted to showing that T(V ∪I) can be computed
in expected time O(n +
Pn
i=1 HV
i
). The algorithm is as follows. For each xi ∈ I, we
use Di to find the triangle B
V
i
of T(V ) that contains it. By the properties of the Di’s
as described in §4.1.1, this takes O(
Pn
i=1 HV
i
) expected time. We now need to argue
that given the B
V
i
’s, the Delaunay triangulation T(V ∪I) can be computed in expected
linear time. For each xi, we walk through T(V ) and find all the Delaunay disks of
T(V ) that contain xi, as in incremental constructions of Delaunay triangulations [12,
Chapter 9]. This is done by breadth-first search of the dual graph of T(V ), starting
from B
V
i
. Refer to Fig. 4.3. Let Si denote the set of triangles whose circumcircles
contain xi. We remind the reader that Zt is the conflict set of triangle t.
Claim 4.4. Given all B
V
i
’s, all Si and Zt sets can be found in expected linear
time.
Proof. To find all Delaunay disks containing xi, do a breadth-first search from
B
V
i
. For any triangle t encountered, check if Ct contains xi. If it does not, then we
V(V )
t
Ct
(a) (b) GI (V )
s
v
t1
t2 t3
Fig. 4.4. (a) V(V ) is dual to T(V ). Each vertex t of V(V ) corresponds to the center of
the circumcircle of a triangle t of T(V ), and it has the same conflict set Zt of size Xt. (b) The
geode triangulation GI (V ) is obtained by connecting the vertices of each region of V(V ) to the
lexicographically smallest incident vertex with the smallest Xt. The conflict set of a triangle s is the
union of the conflict sets of its vertices and point v defining the region.
Since Siis connected in the dual graph of T(V ),5 we will visit all Ct’s that contain
xi. The time taken to find Siis O(|Si|). The total time taken to find all Si’s (once all
the B
V
i
’s are found) is O(
Pn
i=1 |Si
|). Define the indicator function χ(t, i) that takes
value 1 if xi ∈ Ct and zero otherwise. We have
Xn
i=1
|Si| =
Xn
i=1
X
t∈T(V )
χ(t, i) = X
t∈T(V )
Xn
i=1
χ(t, i) = X
t
Xt.
Therefore, by Lemma 4.1,
E
hXn
i=1
|Si|
i
= E
hX
t
Xt
i
=
X
t
E[Xt] = O(n).
This implies that all Si’s and Zt’s can be found in expected linear time.
Our aim is to build the Delaunay triangulation T(V ∪ I) in linear time using
the conflict sets Zt. To that end, we will use divide-and-conquer to compute the
Voronoi diagram V(V ∪ I), using a scheme that has been used for nearest neighbor
searching [24] and for randomized convex hull constructions [20, 25]. It is well known
that the Voronoi diagram of a point set is dual to the Delaunay triangulation, and that
we can go from one to the other in linear time [12, Chapter 9]. Refer to Fig. 4.4(a).
Consider the Voronoi diagram of V , V(V ). By duality, the vertices of V(V ) correspond
to the triangles in T(V ), and we identify the two. In particular, each vertex t of
V(V ) has a conflict set Zt, the conflict set for the corresponding triangle in T(V ),
and |Zt| = Xt, by our definition of Xt (see Fig. 4.4(a)). We triangulate the Voronoi
diagram as follows: for each region r of V(V ), determine the lexicographically smallest
Voronoi vertex tr in r with minimum Xt. Add edges from all the Voronoi vertices
in r to tr. Since each region of V(V ) is convex, this yields a triangulation6 of V(V ).
5Since the triangles in Si cover exactly the planar region of triangles incident to xi in T(V ∪{xi}).
6We need to be a bit careful when handling unbounded Voronoi regions: we pretend that there is
a Voronoi vertex p∞ at infinity which is the endpoint of all unbounded Voronoi edges, and when we
triangulate the unbounded region, we also add edges to p∞. By our bounding triangle assumption,
s v
y
p
t1
B(v, y)
Ct1
Fig. 4.5. The nearest neighbor of a point y ∈ s is either v or needs to be in the conflict set of
one of its vertices.
We call it the geode triangulation of V(V ) with respect to I, GI (V ) [20, 24]. Refer to
Fig. 4.4(b). Clearly, GI (V ) can be computed in linear time. We extend the notion
of conflict set to the triangles in GI (V ): Let s be a triangle in GI (V ) and let t1,
t2, t3 be its incident Voronoi vertices. Then the conflict set of s, Zs, is defined as
Zs := Zt1 ∪Zt2 ∪Zt3 ∪{v}, where v ∈ V is the point whose Voronoi region contains the
triangle s. In the following, for any two points x and y, |x − y| denotes the Euclidean
distance between them.
Claim 4.5. Let s be a triangle of GI (V ) and let Zs be its conflict set. Then the
Voronoi diagram of V ∪ I restricted to s, V(V ∪ I) ∩ s, is the same as the Voronoi
diagram of Zs restricted to s, V(Zs) ∩ s.
Proof. Consider a point p in the triangle s, and let y be the nearest neighbor
of p in V ∪ I. If y ∈ V , then y has to be v, since s lies in the Voronoi region of v
with respect to V . Now suppose that y ∈ I. Let B(v, y) be the perpendicular bisector
of the line segment (v, y) (ie, the line containing all points in the plane that have
equal distance from v and y). Refer to Figure 4.5. Let B+ be the halfplane defined
by B(v, y) that contains y. Since B+ intersects s, by convexity it also contains a
vertex of s, say t1. Because t1 and y are on the same side (B+), |y − t1| < |v − t1|.
Note that Ct1 has center t1 and radius |v − t1|, because t1 is a vertex of the Voronoi
region corresponding to v (in V(V )). Hence, y ∈ Zt1. It follows that y ∈ Zs, so
V(V ∪ I) ∩ s = V(Zs) ∩ s, as claimed.
Claim 4.5 implies that V(V ∪ I) can be found as follows: for each triangle s of
GI (V ), compute V(Zs) ∩ s, the Voronoi diagram of Zs restricted to s. Then, traverse
the edges of GI (V ) and fuse the bisectors of the adjacent diagrams, yielding V(V ∪I).
Lemma 4.6. Given V(V ), the Voronoi diagram V(V ∪ I) can be computed in
expected O(n) time.
Proof. The time to find V(Zs) ∩ s for a triangle s in GI (V ) is O(|Zs| log |Zs|) =
O(|Zs|
2
) [12, Chapter 7]. For a region r of V(V ), let S(r) denote the set of triangles
of GI (V ) contained in r, and let E(r) denote the set of edges in V(V ) incident to r.
Recall that tr denotes the common vertex of all triangles in S(r). The total running
time is O(E
hP
s∈GI (V )
|Zs|
2
i
), which is proportional to
E
h X
r∈V(V )
X
s∈S(r)
|Zs|
2
i
≤ E
h X
r∈V(V )
X
(t1,t2)∈E(r)
(1 + Xtr + Xt1 + Xt2)
2
i
≤ E
h X
r∈V(V )
X
(t1,t2)∈E(r)
(1 + 2Xt1 + Xt2
)
2
i
since Xtr ≤ min(Xt1, Xt2). For e = (t1, t2), let Ye = 1 + 2Xt1 + Xt2. Note that
E[Ye] = O(1), by Lemma 4.1. We can write Ye =
P
i
(1/n+ 2χ(t1, i) +χ(t2, i)), where
χ(t, i) was the indicator random variable for the event that xi ∈ Ct. Hence, since
1/n + 2χ(t1, i) + χ(t2, i) < 4, Claim 3.3 implies that E[Y
2
e
] = O(1). Thus,
E
h X
s∈GI (V )
|Zs|
2
i
≤
X
r∈V(V )
X
e∈E(r)
e=(t1,t2)
E[(Ye)
2
] = X
r∈V(V )
X
e∈E(r)
e=(t1,t2)
O(1).
The number of edges in V(V ) is linear, and each edge e is incident to exactly two
Voronoi regions r. Therefore, E[
P
s∈GI (V )
|Zs|
2
] = O(n). Furthermore, assembling
the restricted diagrams takes time O

E
P
s∈GI (V )
|Zs|
, and as |Zs| ≤ |Zs|
2
, this is
also linear.
4.2. Running time analysis. In this section, we prove that the running time
bound in Lemma 4.2 is indeed optimal. As discussed at the beginning of §4, Claim 2.2
implies that any comparison-based algorithm for computing the Delaunay triangulation of input I ∈R D needs at least H(T(I)) expected comparisons. Recall that
by Lemma 4.2, the expected running time of our algorithm is O(n +
P
i HV
i
). The
following is the main theorem of this section.
Theorem 4.7. For HV
i
, the entropy of the triangle B
V
i
of T(V ) containing xi,
and H(T(I)), the entropy of the Delaunay triangulation of I, considered as a labeled
graph,
X
i
HV
i = O(n + H(T(I))).
Proof. Let B
V
:= (B
V
1
, . . . , B
V
n
) be the vector of all the triangles that contain
the xi’s. By Claim 2.1, we have H(B
V
) = P
i HY
i
. Now we apply Lemma 2.3
with U =

R
2
n
, X = T(I) and Y . In Lemma 4.8 we will show that the function f :
(I, T(I)) 7→ (B
V
1
, . . . , B
V
n
) can be computed in linear time, so H(B
V
i
) = O(n+H(T(I)),
by Lemma 2.3. This proves the theorem.
We first define some notation — for a point set P ⊆ V ∪ I and p ∈ P, let ΓP (p)
denote the neighbors of p in T(P). It remains to prove the following lemma.7
Lemma 4.8. Given I and T(I), for every xi in I we can compute the triangle
B
V
i
in T(V ) that contains xi in total expected time O(n).
Proof. First, we compute T(V ∪ I) from T(V ) and T(I) in linear time [19, 36].
Thus, we now know T(V ∪ I) and T(V ), and we want to find for every point xi ∈ I
the triangle B
V
i
of T(V ) that contains it. For the moment, let us be a little less
ambitious and try to determine for each xi ∈ I, a conflict triangle C
V
i
in T(V ), ie, C
V
i
is a triangle t with xi ∈ Zt. If x ∈ I and v ∈ V such that xv is an edge of T(V ∪I), we
can find a conflict triangle for x in T(V ) in time O(n) by inspecting all the incident
triangles of v in T(V ). Actually, we can find conflict triangles for all neighbors of v
in T(V ∪ I) that lie in I, by merging the two neighbor lists (see below). Noting that
on average the size of these lists will be constant, we could almost determine all the
C
V
i
, except for one problem: there might be inputs x ∈ I that are not adjacent to any
7A similar lemma is used in [22] in the context of hereditary algorithms for three-dimensional
v ∈ V in T(V ∪ I). Thus, we need to dynamically modify T(V ) to ensure that there
is always a neighbor present. Details follow.
Claim 4.9. Let p ∈ V ∪ I and write Vp := V ∪ {p}. Suppose that T(V ∪ I)
and T(Vp) are known. Then, in total time O(|ΓV ∪I (p)| + |ΓVp
(p)|), for every xi ∈
ΓV ∪I (p) \ Vp, we can compute a conflict triangle C
Vp
i
of xi in T(Vp).
Proof. Let xi ∈ ΓV ∪I (p) \ Vp, and let C
Vp
i
be the triangle of T(Vp) incident to p
that is intersected by line segment pxi
. We claim that C
Vp
i
is a conflict triangle for
xi. Indeed, since pxi
is an edge of T(V ∪ I), by the characterization of Delaunay
edges (eg, [12, Theorem 9.6(ii)]), there exists an circle C through p and xi which
does not contain any other points from V ∪ I. In particular, C does not contain any
other points from Vp ∪ {xi}. Hence pxiis also an edge of T(Vp ∪ {xi}), again by the
characterization of Delaunay edges applied in the other direction. Therefore, triangle
C
Vp
i
is destroyed when xiis inserted into T(V ∪ J), and is a conflict triangle for xi
in T(Vp). It follows that the conflict triangles for ΓV ∪I (p) \ Vp can be computed by
merging the cyclically ordered lists ΓV ∪I (p) and ΓVp(p). This requires a number of
steps that is linear of the size of the two lists, as claimed.
For certain pairs of points p, xi, the previous claim provides a conflict triangle
C
Vp
i
. The next claim allows us to get C
V
i
from this, which is what we wanted in the
first place.
Claim 4.10. Let xi ∈ I and let p ∈ V ∪ I. Let C
Vp
i
be the conflict triangle for xi
in T(Vp) incident to p, as determined in Step 2c. Then we can find a conflict triangle
C
V
i
for xi in T(V ) in constant time.
Proof. If p ∈ V , there is nothing to prove, so assume that p ∈ I. If C
Vp
i
has all
vertices in V , then it is also a triangle in T(V ), and we are trivially done. So assume
that one vertex of C
Vp
i
is p. Let e be the edge of C
Vp
i
not incident to p, and let v, w
be the endpoints of e. We will show that xiis in conflict with at least one of the two
triangles in T(V ) that are incident to e. Given e, such a triangle can clearly be found
in constant time. Refer to Fig. 4.6 for a depiction of the following arguments.
Since v, w ∈ V , by the characterization of Delaunay edges, it follows that e is also
an edge of T(V ). If xi does not lie in C
Vp
i
, then xi must also be in conflict with the
other triangle t that is incident to e (since t is intersected by the Delaunay edge pxi).
Note that t cannot have p as a vertex and is a triangle of T(V ).
Suppose xilies in C
Vp
i
. Since C
Vp
i
is a triangle in T(Vp), the interior has no points
other than xi. Thus, the segments vxi and wxi are edges of T(Vp ∪ {xi}). These must
also be edges of T(V ∪ {xi}). But this means that xi must conflict with the triangle
in T(V ) incident to e at the same side as C
Vp
i
.
The conflict triangles for all points in I can now be computed using breadth-first
search (see Algorithm 1). The loop in Step 2 maintains the invariant that for each
point xi ∈ Q ∩ I, a conflict triangle C
V
i
in T(V ) is known. Step 2b is performed as in
the traditional randomized incremental construction of Delaunay triangulations [12,
Chapter 9]: walk from C
V
i
through the dual graph if T(V ) to determine the conflict
set Si of xi (as in the proof of Claim 4.4), insert new edges from all points incident
to the triangles in Si to xi, and remove all the old edges that are intersected by these
new edges. The properties of the conflict set ensure that this yields a valid Delaunay
triangulation. By Claim 4.10, Step 2d can be performed in constant time.
The loop in Step 2 is executed at most once for each p ∈ V ∪ I. It is also
Algorithm 1 Determining the conflict triangles.
1. Let Q be a queue containing the elements in V .
2. While Q 6= ∅.
(a) Let p be the next point in Q.
(b) If p = xi ∈ I, then insert p into T(V ) using the conflict triangle C
V
i
for
xi, to obtain T(Vp). If p ∈ V , then T(Vp) = T(V ).
(c) Using Claim 4.9, for each unvisited neighbor xj ∈ ΓV ∪I (p) ∩ I, compute
a conflict triangle C
Vp
j
in T(Vp).
(d) For each unvisited neighbor xj ∈ ΓV ∪I (p) ∩ I, using C
Vp
j
, compute a
conflict triangle C
V
j
of xj in T(V ). Then insert xj into Q, and mark it
as visited.
w
v
p
e
xi
C
Vp
i
t
w
v
p
e
xi
C
Vp
i
(a) (b)
t
0
Fig. 4.6. (a) If xi is outside C
Vp
i
, it conflicts with the triangle t of T(V ) on the other side of
e. (b) If xi lies inside C
Vp
i
, it conflicts with the triangle t
0 of T(V ) at the same side of e, since vxi
and wxi are both edges of T(V ).
we perform a BFS. The insertion in Step 2b takes O(|ΓVxi(xi)|) time. Furthermore,
by Claim 4.9, the conflict triangles of p’s neighbors in T(V ∪ I) can be computed in
O(|ΓVp(p)|+|ΓV ∪I (p)|) time. Finally, as we argued above, Step 2d can be carried out
in total O(|ΓV ∪I (p)|) time. Now note that for xi ∈ I, |ΓVxi(xi)| is proportional to
|Si|, the number of triangles in T(V ) in conflict with xi. Hence, the total expected
running time is proportional to
E
h X
p∈V ∪I

|ΓVp(p)| + |ΓV ∪I (p)|

i
= E
hX
v∈V
|ΓV (v)| +
Xn
i=1
|Si| +
X
p∈V ∪I
|ΓV ∪I (p)|
i
= O(n).
Finally, using BFS as in the proof of Claim 4.4, given the conflict triangles C
V
i
, the
triangles B
V
i
that contain the xi’s can be found in O(n) expected time, and the result
follows.
4.3. The time-space tradeoff. We show how to remove the assumption that
we have prior knowledge of the Di’s (to build the search structures Di) and prove
the time-space tradeoff given in Theorem 1.3. These techniques are identical to those
used in §3.2. For the sake of clarity, we give a detailed explanation for this setting.
Let ε ∈ (0, 1) be any constant. The first dlog ne rounds of the learning phase are used
as in §4.1.1 to construct the Delaunay triangulation T(V ). We first build a standard
search structure D over the triangles of T(V ) [12, Chapter 6]. Given a point x, we
The learning phase takes M = cnεrounds, for some large enough constant c. The
main trick is to observe that (up to constant factors), the only probabilities that are
relevant are those that are at least n
−ε/3
. In each round, for each xi, we record the
triangle of T(V ) that xi falls into. Fix i, and for any triangle t of T(V ), let χt be the
number of times over the first M rounds that B
V
i = t. At the end of M rounds, we
take the set Ri of triangles t with χt > 0. We remind the reader that p(t, i) is the
probability that xilies in triangle t. The proof of the following lemma is identical to
the proof of Lemma 3.4.
Lemma 4.11. Fix i. With probability at least 1 − 1/n3, for every triangle t of
T(V ), if p(t, i) > n−ε/3, then M p(t, i)/2 < χt < 3M p(t, i)/2.
For every triangle t in Ri, we estimate p(t, i) as ˆp(t, i) = χt/M, and we use ˆp(t, i)
to build the approximate search structure Di. For this, we take the planar subdivision
Giinduced by the triangles in Ri, compute the convex hull of Gi, and triangulate the
remaining polygonal facets. Then we use the construction of Arya et al. [10] to build
an optimal planar point location structure Di for Gi according to the distribution
pˆi (the triangles of Gi not in Ri are assigned probability 0). This structure Gi has
the property that a point in a triangle t with probability ˆp(t, i) can be located in
O(log(1/pˆ(t, i))) steps [10, Theorems 1.1 and 1.2].
The limiting phase uses these structures to find B
V
i
for every xi: given xi, we
use Di to search for it. If the search does not terminate in log n steps or Di fails to
find B
V
i
(ie, B
V
i ∈/ Ri), then we use the standard search structure, D, to find B
V
i
.
Therefore, we are guaranteed to find B
V
i
in O(log n) time. Clearly, each Di stores
O(M) = O(n
ε
) triangles, so by the bounds given in [10], each Di can be constructed
with size O(n
ε
) in O(n
ε
log n) time. Hence, the total space is bounded by n
1+ε and
the time required to build all the Di’s is O(n
1+ε
log n).
Now we just repeat the argument given in §3.2. Instead of doing it through words,
we write down the expressions (for some variety). Let s(t, i) denote the time to search
for xi given that p(i, t) > n−ε/3. By Lemma 4.11, we have χt > Mn−ε/3/2, so t ∈ Ri,
for c large enough, and thus s(t, i) = O(log(1/pˆ(t, i))) = O(1 − log p(t, i)). Thus,
X
t:p(t,i)>n−ε/3
p(t, i)s(t, i) = O
 X
t:p(t,i)>n−ε/3
p(t, i)(1 − log p(t, i))
= O

1 −
X
t:p(t,i)>n−ε/3
p(t, i) log p(t, i)

.
We now bound the expected search time for xi.
X
t
p(t, i)s(t, i) = X
t:p(t,i)≤n−ε/3
p(t, i)s(t, i) + X
t:p(t,i)>n−ε/3
p(t, i)s(t, i)
= O

1 + X
t:p(t,i)≤n−ε/3
p(t, i) log n −
X
t:p(t,i)>n−ε/3
p(t, i) log p(t, i)
Noting that for p(t, i) ≤ n
−ε/3
, we have O(log n) = O(ε
−1
log(1/p(t, i))), we get
X
t
p(t, i)s(t, i)
= O

1 − ε
−1 X
t:p(t,i)≤n−ε/3
p(t, i) log p(t, i) −
X
t:p(t,i)>n−ε/3
p(t, i) log p(t, i)

= O

1 − ε
−1X
t
p(t, i) log p(t, i)

= O(1 + ε
−1HV
i
).
If follows that the total expected search time is O(n+ε
−1 P
i HV
i
). By the analysis of
§4.1 and Theorem 4.7, we have that the expected running time in the limiting phase is
O(ε
−1
(n+H(T(I)))). If the conditions in Lemmas 4.1 and 4.11 do not hold, then the
training phase fails. But this happens with probability at most 1/n. This completes
the proof of Theorem 1.3.
5. Conclusions and future work. Our overall approach has been to deduce
a “typical” instance for the distribution, and then use the solution for the typical
instance to solve the current problem. This is a very appealing paradigm - even
though the actual distribution D could be extremely complicated, it suffices to learn
just one instance. It is very surprising that such a single instance exists for product
distributions. One possible way of dealing with more general distributions is to have a
small set of typical instances. It seems plausible that even with two typical instances,
we might be able to deal with some dependencies in the input.
We could imagine distributions that are very far from being generated by independent sources. Maybe we have a graph labeled with numbers, and the input is
generated by a random walk. Here, there is a large dependency between various components of the input. This might require a completely different approach than the
current one.
Currently, the problems we have focused upon already have O(n log n) time algorithms. So the best improvement in the running time we can hope for is a factor
of O(log n). The entropy optimality of our algorithms is extremely pleasing, but our
running times are always between O(n) and O(n log n). It would be very interesting
to get self-improving algorithms for problems where there is a much larger scope for
improvement. Ideally, we want a problem where the optimal (or even best known)
algorithms are far from linear. Geometric range searching seem to a good source of
such problems. We are given some set of points and we want to build data structures
that answer various geometric queries about these points [2]. Suppose the points came
from some distribution. Can we speed up the construction of these structures?
A different approach to self-improving algorithms would be to change the input
model. We currently have a memoryless model, where each input is independently
drawn from a fixed distribution. We could have a Markov model, where the input
Ik depends (probabilistically) only on Ik−1, or maybe on a small number of previous
inputs.
REFERENCES
[1] Peyman Afshani, Jer´ emy Barbay, and Timothy M. Chan ´ , Instance-optimal geometric algorithms, in Proc. 50th Annu. IEEE Sympos. Found. Comput. Sci. (FOCS), 2009, pp. 129–
138.
[2] Pankaj Agarwal and Jeff Erickson, Geometric range searching and its relatives, Advances
[3] Alok Aggarwal, Leonidas J. Guibas, James Saxe, and Peter W. Shor, A linear-time algorithm for computing the Voronoi diagram of a convex polygon, Discrete Comput. Geom.,
4 (1989), pp. 591–604.
[4] Susanne Albers and Michael Mitzenmacher, Average case analyses of list update algorithms, with applications to data compression, Algorithmica, 21 (1998), pp. 312–329.
[5] Susanne Albers and Jeffery Westbrook, Self-organizing data structures, in Online algorithms (Schloss Dagstuhl, 1996), vol. 1442 of Lecture Notes in Comput. Sci., Springer
Verlag, Berlin, 1998, pp. 13–51.
[6] Brian Allen and Ian Munro, Self-organizing binary search trees, J. ACM, 25 (1978).
[7] Noga Alon and Joel H. Spencer, The probabilistic method, Wiley-Interscience Series in
Discrete Mathematics and Optimization, Wiley-Interscience, New York, second ed., 2000.
[8] Sigal Ar, Bernard Chazelle, and Ayellet Tal, Self-customized BSP trees for collision
detection, Comput. Geom. Theory Appl., 15 (2000), pp. 91–102.
[9] Sanjeev Arora and Boaz Barak, Computational Complexity: A Modern Approach, Cambridge University Press, 2009.
[10] Sunil Arya, Theocharis Malamatos, David M. Mount, and Ka Chun Wong, Optimal
expected-case planar point location, SIAM J. Comput., 37 (2007), pp. 584–610.
[11] Jon L. Bentley and Catherine C. McGeoch, Amortized analyses of self-organizing sequential search heuristics, Comm. ACM, 28 (1985), pp. 404–411.
[12] Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars, Computational Geometry: Algorithms and Applications, Springer-Verlag, Berlin, third ed., 2008.
[13] James R. Bitner, Heuristics that dynamically organize data structures, SIAM J. Comput., 8
(1979), pp. 82–110.
[14] Jean-Daniel Boissonnat and Mariette Yvinec, Algorithmic geometry, Cambridge University Press, 1998.
[15] Allan Borodin and Ran El-Yaniv, Online computation and competitive analysis, Cambridge
University Press, 1998.
[16] Kevin Buchin and Wolfgang Mulzer, Delaunay triangulations in O(sort(n)) time and more,
in Proc. 50th Annu. IEEE Sympos. Found. Comput. Sci. (FOCS), 2009, pp. 139–148.
[17] Timothy M. Chan and Mihai Patras¸cu ˇ , Voronoi diagrams in n2
O(
√
lg lg n)
time, in Proc.
39th Annu. ACM Sympos. Theory Comput. (STOC), 2007, pp. 31–39.
[18] , Transdichotomous results in computational geometry, I: Point location in sublogarithmic time, SIAM J. Comput., 39 (2009), pp. 703–729.
[19] Bernard Chazelle, An optimal algorithm for intersecting three-dimensional convex polyhedra,
SIAM J. Comput., 21 (1992), pp. 671–696.
[20] , The discrepancy method, Cambridge University Press, 2000.
[21] Bernard Chazelle, Olivier Devillers, Ferran Hurtado, Merce Mora, Vera Sacrist ` an, ´
and Monique Teillaud, Splitting a Delaunay triangulation in linear time, Algorithmica,
34 (2002), pp. 39–46.
[22] Bernard Chazelle and Wolfgang Mulzer, Computing hereditary convex structures, in
Proc. 25th Annu. ACM Sympos. Comput. Geom. (SoCG), 2009, pp. 61–70.
[23] , Markov incremental constructions, Discrete Comput. Geom., 42 (2009), pp. 399–420.
[24] Kenneth L. Clarkson, A randomized algorithm for closest-point queries, SIAM J. Comput.,
17 (1988), pp. 830–847.
[25] Kenneth L. Clarkson and Peter W. Shor, Applications of random sampling in computational geometry, II, Discrete Comput. Geom., 4 (1989), pp. 387–421.
[26] Kenneth L. Clarkson and Kasturi Varadarajan, Improved approximation algorithms for
geometric set cover, Discrete Comput. Geom., 37 (2007), pp. 43–58.
[27] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, Introduction to Algorithms, MIT Press, third ed., 2009.
[28] Thomas M. Cover and Joy A. Thomas, Elements of information theory, Wiley-Interscience,
second ed., 2006.
[29] Herbert Edelsbrunner and Ernst P. Mucke ¨ , Simulation of simplicity: a technique to cope
with degenerate cases in geometric algorithms, ACM Trans. Graph., 9 (1990), pp. 66–104.
[30] Vladmir Estivill-Castro and Derick Wood, A survey of adaptive sorting algorithms, ACM
Comput. Surv., 24 (1992), pp. 441–476.
[31] Michael L. Fredman, How good is the information theory bound in sorting?, Theoret. Comput. Sci., 1 (1975/76), pp. 355–361.
[32] Gaston H. Gonnet, J. Ian Munro, and Hendra Suwanda, Exegesis of self-organizing linear
search, SIAM J. Comput., 10 (1981), pp. 613–637.
[33] Yijie Han, Deterministic sorting in O(n log log n) time and linear space, J. Algorithms, 50
[34] Yijie Han and Mikkel Thorup, Integer sorting in O(n
√
log log n) expected time and linear
space, in Proc. 43rd Annu. IEEE Sympos. Found. Comput. Sci. (FOCS), 2002, pp. 135–144.
[35] James H. Hester and Daniel S. Hirschberg, Self-organizing linear search, ACM Comput.
Surv., 17 (1985), pp. 295–311.
[36] David G. Kirkpatrick, Efficient computation of continuous skeletons, in Proc. 20th Annu.
IEEE Sympos. Found. Comput. Sci. (FOCS), 1979, pp. 18–27.
[37] Der Tsai Lee, On k-nearest neighbor Voronoi diagrams in the plane, IEEE Trans. Comput.,
31 (1982), pp. 478–487.
[38] Jirˇ´ı Matouˇsek, Reporting points in halfspaces, Comput. Geom. Theory Appl., 2 (1992),
pp. 169–186.
[39] Jirˇ´ı Matouˇsek, Raimund Seidel, and E. Welzl, How to net a lot with little: small -nets
for disks and halfspaces, in Proc. 6th Annu. ACM Sympos. Comput. Geom. (SoCG), 1990,
pp. 16–22.
[40] John McCabe, On serial files with relocatable records, Operations Res., 13 (1965), pp. 609–618.
[41] Kurt Mehlhorn, Data structures and algorithms 1: Sorting and Searching, EATCS Monographs on Theoretical Computer Science, Springer Verlag, Berlin, 1984.
[42] Rajeev Motwani and Prabhakar Raghavan, Randomized algorithms, Cambridge University
Press, 1995.
[43] Evangelia Pyrga and Saurabh Ray, New existence proofs for -nets, in Proc. 24th Annu.
ACM Sympos. Comput. Geom. (SoCG), 2008, pp. 199–207.
[44] Ronald Rivest, On self-organizing sequential search heuristics, Comm. ACM, 19 (1976),
pp. 63–67.
[45] Daniel D. Sleator and Robert E. Tarjan, Amortized efficiency of list update and paging
rules, Comm. ACM, 28 (1985), pp. 202–208.
[46] , Self-adjusting binary search trees, J. ACM, 32 (1985), pp. 652–686.
Appendix A. Constructing the ε-net V . Recall that λ = dlog ne. Given a
set ˆI of m := nλ points in the plane, we would like to construct a set V ⊆ ˆI of size
O(n) such that any open disk C with |C ∩ ˆI| > λ intersects V . (This is a (1/n)-net
for disks.) We describe how to construct V in deterministic time n(log n)
O(1), using
a technique by Pyrga and Ray [43]. This is by no means the only way to obtain V .
Indeed, it is possible to use the older techniques of Clarkson and Varadarajan [26] to
get a another—randomized—construction with a better running time.
We set some notation. For a set of points S, a k-set of S is a subset of S of size
k obtained by intersecting S with an open disk. A (> k)-set is is such a subset with
size more than k. We give a small sketch of the construction. We take the collection
ˆI=λ of all λ-sets of ˆI. We need to obtain a small hitting set for ˆI=λ. To do this, we
trim ˆI=λ to a collection of λ-sets that have small pairwise intersection. Within each
such set, we will choose an ε-net (for some ε). The union of these ε-nets will be our
final (1/n)-net. We now give the algorithmic construction of this set and argue that
it is a (1/n)-net. Then, we will show that it has size O(n).
It is well known that the collection ˆI=λ has O(mλ) sets [25,37] and that an explicit
description of ˆI=λ can be found in time O(mλ2) [3,37], since ˆI=λ corresponds to the λth-order Voronoi diagram of ˆI, each of whose cells represents some λ-set of ˆI [37]. Let
I ⊆ ˆI=λ be a maximal subset of ˆI=λ such that for any J1, J2 ∈ I, |J1 ∩ J2| ≤ λ/100.
We will show in Claim A.1 how to construct I in O(mλ5) time. To construct V , take
a (1/200)-net VJ for each J ∈ I, and set V := S
J∈I VJ .
8
It is well known that each
VJ has constant size and can be found in time O(|J|) = O(λ) [20, p. 180, Proof I].
The set V is an (1/n)-net for ˆI: if an open disk C intersects ˆI in more than λ-points,
by the maximality of I, it must intersect a set J ∈ I in more than λ/100 points. Now
V contains a (1/200)-net for J (recall that |J| = λ), so V must meet the disk C. We
will argue in Claim A.2 that |V | = O(n). This completes the proof.
8That is, VJ is a subset of J such that any open disk that contains more than |J|/200 points
Claim A.1. The set I can be constructed in time O(mλ5).
Proof. We use a simple greedy algorithm. For each J ∈ ˆI=λ, construct the
collection J>λ/100 of all (> λ/100)-sets of J. The set J has size λ, and the total
number of disks defined by the points in J is at most λ
3
. Thus, there are at most
λ
3
sets in J>λ/100, and they can all be found in O(λ
4
) time. Since there are at most
O(mλ) sets J (as we argued earlier), the total number of (> λ/100)-sets is O(mλ4),
and they can be obtained in O(mλ5) time. Next, perform a radix sort on the multiset
J := S
J∈Iˆ=λ
J>λ/100. This again takes time O(mλ5). Note that for any J1, J2 ∈ ˆI=λ,
|J1 ∩ J2| > λ/100 precisely if J1 and J2 share some (> λ/100)-set. Now I is obtained
as follows: pick a set J ∈ ˆI=λ, put J into I, and use the sorted multiset J to find all
J
0 ∈ ˆI=λ that share a (> λ/100)-set with J. Discard those J0
from ˆI=λ. Iterate until
ˆI=λ is empty. The resulting set I has the desired properties.
Claim A.2. |V | = O(n).
Proof. The set V is the union of (1/200)-nets for each set J ∈ I. Since each
net has constant size, it suffices to prove that I has O(n) sets. This follows from a
charging argument due to Pyrga and Ray [43, Theorem 12]. They show [43, Lemma 7]
how to construct a graph GI = (I, EI) on vertex set I with at most |EI| ≤ 24|I|
edges with the following property: for p ∈ ˆI, let Ip be the set of all J ∈ I that contain
p, and let Gp = (Ip, Ep) be the induced subgraph on vertex set Ip. Then, for all p,
|Ep| ≥ |Ip|/4 − 1. Thus,
X
p∈Iˆ
(|Ip|/4 − |Ep|) ≤ |ˆI| = m.
Consider the sum P
p∈Iˆ |Ip|. All sets in I contain exactly λ points, so each set
contributes λ to the sum. By double counting, P
p∈Iˆ |Ip|/4 = λ|I|/4. Furthermore,
an edge (J1, J2) ∈ EI can appear in Ep only if p ∈ J1∩J2, so again by double-counting,
X
p∈Iˆ
|Ep| ≤ λ|EI|/100 ≤ 24λ|I|/100.
Hence, m ≥
P
p∈Iˆ(|Ip|/4 − |Ep|) ≥ λ|I|/100, and |I| = O(m/λ) = O(n).

