---
source: https://arxiv.org/pdf/2212.07677
description: Mechanistic ICML paper showing linear self-attention can implement gradient descent for in-context regression and trained Transformers can recover that construction
captured: 2026-04-20
capture: pdf-read
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Transformers Learn In-Context by Gradient Descent

Author: Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, Max Vladymyrov
Source: https://arxiv.org/pdf/2212.07677
Date: 2023-05-31

Transformers Learn In-Context by Gradient Descent

                                                           Johannes von Oswald 1 2 Eyvind Niklasson 2 Ettore Randazzo 2 João Sacramento 1
                                                                  Alexander Mordvintsev 2 Andrey Zhmoginov 2 Max Vladymyrov 2


                                                                   Abstract                                 1. Introduction
                                                                                                            In recent years Transformers (TFs; Vaswani et al., 2017)
arXiv:2212.07677v2 [cs.LG] 31 May 2023




                                                                                                            have demonstrated their superiority in numerous bench-
                                                At present, the mechanisms of in-context learning           marks and various fields of modern machine learning, and
                                                in Transformers are not well understood and re-             have emerged as the de-facto neural network architecture
                                                main mostly an intuition. In this paper, we suggest         used for modern AI (Dosovitskiy et al., 2021; Yun et al.,
                                                that training Transformers on auto-regressive ob-           2019; Carion et al., 2020; Gulati et al., 2020). It has been hy-
                                                jectives is closely related to gradient-based meta-         pothesised that their success is due in part to a phenomenon
                                                learning formulations. We start by providing a              called in-context learning (Brown et al., 2020; Liu et al.,
                                                simple weight construction that shows the equiva-           2021): an ability to flexibly adjust their prediction based on
                                                lence of data transformations induced by 1) a sin-          additional data given in context (i.e. in the input sequence
                                                gle linear self-attention layer and by 2) gradient-         itself). In-context learning offers a seemingly different ap-
                                                descent (GD) on a regression loss. Motivated                proach to few-shot and meta-learning (Brown et al., 2020),
                                                by that construction, we show empirically that              but as of today the exact mechanisms of how it works are not
                                                when training self-attention-only Transformers on           fully understood. It is thus of great interest to understand
                                                simple regression tasks either the models learned           what makes Transformers pay attention to their context,
                                                by GD and Transformers show great similarity                what the mechanisms are, and under which circumstances,
                                                or, remarkably, the weights found by optimiza-              they come into play (Chan et al., 2022b; Olsson et al., 2022).
                                                tion match the construction. Thus we show how
                                                trained Transformers become mesa-optimizers i.e.            In this paper, we aim to bridge the gap between in-context
                                                learn models by gradient descent in their forward           and meta-learning, and show that in-context learning in
                                                pass. This allows us, at least in the domain of re-         Transformers can be an emergent property approximating
                                                gression problems, to mechanistically understand            gradient-based few-shot learning within its forward pass, see
                                                the inner workings of in-context learning in op-            Figure 1. For this to be realized, we show how Transformers
                                                timized Transformers. Building on this insight,             (1) construct a loss function dependent on the data given in
                                                we furthermore identify how Transformers sur-               sequence and (2) learn based on gradients of that loss. We
                                                pass the performance of plain gradient descent              will first focus on the latter, the more elaborate learning task,
                                                by learning an iterative curvature correction and           in sections 2 and 3, after which we provide evidence for the
                                                learn linear models on deep data representations            former in section 4.
                                                to solve non-linear regression tasks. Finally, we           We summarize our contributions as follows1 :
                                                discuss intriguing parallels to a mechanism iden-
                                                tified to be crucial for in-context learning termed
                                                induction-head (Olsson et al., 2022) and show                  • We construct explicit weights for a linear self-attention
                                                how it could be understood as a specific case of                 layer that induces an update identical to a single step
                                                in-context learning by gradient descent learning                 of gradient descent (GD) on a mean squared error loss.
                                                within Transformers.                                             Additionally, we show how several self-attention layers
                                                                                                                 can iteratively perform curvature correction improving
                                                                                                                 on plain gradient descent.

                                            1                                                                  • When optimized on linear regression datasets, we
                                             Department of Computer Science, ETH Zürich, Zürich,
                                         Switzerland 2 Google Research. Correspondence to: Johannes              demonstrate that linear self-attention-only Transform-
                                         von Oswald <voswaldj@ethz.ch>.
                                                                                                               1
                                                                                                                 Main experiments can be reproduced with notebooks
                                         Proceedings of the 40 th International Conference on Machine       provided under the following link: https://github.com/
                                         Learning, Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright         google-research/self-organising-systems/
                                         2023 by the author(s).                                             tree/master/transformers_learn_icl_by_gd

                                                                                                        1


---

                                         Transformers Learn In-Context by Gradient Descent

                                                                                                                            Gradient descent
                                                                                                           0.2              Trained Transformer




                                                                                                    Loss
                                                                                                           0.1

                                                                                                           0.0
                                                                                                                 0          20          40
                                                                                                                 GD Steps / Transformer Layers

Figure 1. Illustration of our hypothesis: gradient-based optimization and attention-based in-context learning are equivalent. Left:
Learning a neural network output layer by gradient descent on a dataset Dtrain . The task-shared meta-parameters θ are obtained by
meta-learning with the goal that after adjusting the neural network output layer, the model generalizes well on unseen data. Center:
Illustration of a Transformer that adjusts its query prediction on the data given in-context i.e. tθ (xquery ; Dcontext ). The weights of the
Transformer are optimized to predict the next token yquery . Right: Our results confirm the hypothesis that learning with K steps of gradient
descent on a dataset Dtrain (green part of the left plot) matches trained Transformers with K linear self-attention layers (central plot) when
given Dtrain as in-context data Dcontext .

     ers either converge to our weight construction and                   initialization which allows for fast adaptation on novel tasks.
     therefore implement gradient descent, or generate lin-               It has been shown that in many circumstances, the solution
     ear models that closely align with models trained by                 found can be approximated well when only adapting the
     GD, both in in- and out-of-distribution validation tasks.            output layer i.e. learning a linear model on a meta-learned
                                                                          deep data representations (Finn et al., 2017; Finn & Levine,
   • By incorporating multi-layer-perceptrons (MLPs) into
                                                                          2018; Gordon et al., 2019; Lee et al., 2019; Rusu et al., 2019;
     the Transformer architecture, we enable solving
                                                                          Raghu et al., 2020; von Oswald et al., 2021). In section 3,
     nonlinear regression tasks within Transformers by
                                                                          we show the equivalence of this framework to in-context
     showing its equivalence to learning a linear model on
                                                                          learning implemented in a common Transformer block i.e.
     deep representations. We discuss connections to kernel
                                                                          when combining self-attention layers with a multi-layer-
     regression as well as nonparametric kernel smooth-
                                                                          perceptron.
     ing methods. Empirically, we compare meta-learned
     MLPs and a single step of GD on its output layer with                In the light of meta-learning we show how optimizing Trans-
     trained Transformers and demonstrate striking similar-               former weights can be regarded as learning on two time
     ities between the identified solutions.                              scales. More concretely, we find that solely through the
                                                                          pressure to predict correctly Transformers discover learning
   • We resolve the dependency on the specific token con-                 algorithms inside their forward computations, effectively
     struction by providing evidence that learned Trans-                  meta-learning a learning algorithm. Recently, this concept
     formers first encode incoming tokens into a format                   of an emergent optimizer within a learned neural network,
     amenable to the in-context gradient descent learning                 such as a Transformer, has been termed “mesa-optimization”
     that occurs in the later layers of the Transformer.                  (Hubinger et al., 2019). We find and describe one pos-
                                                                          sible realization of this concept and hypothesize that the
These findings allow us to connect learning Transformer
                                                                          in-context learning capabilities of language models emerge
weights and the concept of meta-learning a learning algo-
                                                                          through mechanisms similar to the ones we discuss here.
rithm (Schmidhuber, 1987; Hinton & Plaut, 1987; Bengio
et al., 1990; Chalmers, 1991; Schmidhuber, 1992; Thrun &                  Transformers come in different “shapes and sizes”, operate
Pratt, 1998; Hochreiter et al., 2001; Andrychowicz et al.,                on vastly different domains, and exhibit varying forms of
2016; Ba et al., 2016; Kirsch & Schmidhuber, 2021). In this               phase transitions of in-context learning (Kirsch et al., 2022;
extensive research field, meta-learning is typically regarded             Chan et al., 2022a), suggesting variance and significant com-
as learning that takes place on various time scales namely                plexity of the underlying learning mechanisms. As a result,
fast and slow. The slowly changing parameters control and                 we expect our findings on linear self-attention-only Trans-
prepare for fast adaptation reacting to sudden changes in the             formers to only explain a limited part of a complex process,
incoming data by e.g. a context switch. Notably, we build                 and it may be one of many possible methods giving rise to
heavily on the concept of fast weights (Schmidhuber, 1992)                in-context learning. Nevertheless, our approach provides
which has shown to be equivalent to linear self-attention                 an intriguing perspective on, and novel evidence for, an in-
(Schlag et al., 2021) and show how optimized Transformers                 context learning mechanism that significantly differs from
implement interpretable learning algorithms within their                  existing mechanisms based on associative memory (Ram-
weights.                                                                  sauer et al., 2020), or by the copying mechanism termed
                                                                          induction heads identified by (Olsson et al., 2022). We,
Another related meta-learning concept, termed MAML
                                                                          therefore, state the following
(Finn et al., 2017), aims to meta-learn a deep neural network

                                                                      2


---

                                     Transformers Learn In-Context by Gradient Descent

Hypothesis 1 (Transformers learn in-context by gradient              ing Schlag et al. (2021), we now introduce our first (and
descent). When training Transformers on auto-regressive              only) departure from the standard model, and omit the
tasks, in-context learning in the Transformer forward pass is        softmax operation in equation 1, leading to the linear self-
implemented by gradient-based optimization of an implicit                  P (LSA) layer ej ← ej + LSAθ (j, {e1 , . . . , eN }) =
                                                                     attention
auto-regressive inner loss constructed from its in-context           ej + h Ph Vh KhT qh,j We next show that with some sim-
data.                                                                ple manipulations we can relate the update performed by
We acknowledge work done in parallel, investigating the              an LSA layer to one step of gradient descent on a linear
same hypothesis. Akyürek et al. (2023) puts forward a               regression loss.
weight construction based on a chain of Transformer layers
(including MLPs) that together implement a single step of            Data transformations induced by gradient descent
gradient descent with weight decay. Similar to work done             We now introduce a reference linear model y(x) = W x
by Garg et al. (2022), they then show that trained Transform-        parameterized by the weight matrix W ∈ RNy ×Nx , and
ers match the performance of models obtained by gradient             a training dataset D = {(xi , yi )}N
                                                                                                        i=1 comprising of input
descent. Nevertheless, it is not clear that optimization finds       samples xi ∈ RNx and respective labels yi ∈ RNy . The
Transformer weights that coincide with their construction.           goal of learning is to minimize the squared-error loss:
Here, we present a much simpler construction that builds on
Schlag et al. (2021) and only requires a single linear self-                                         N
                                                                                               1 X
attention layer to implement a step of gradient descent. This                      L(W ) =           ∥W xi − yi ∥2 .               (2)
                                                                                              2N i=1
allows us to (1) show that optimizing self-attention-only
Transformers finds weights that match our weight construc-
tion (Proposition 1), demonstrating its practical relevance,         One step of gradient descent on L with learning rate η yields
and (2) explain in-context learning in shallow two layer             the weight change
Transformers intensively studied by Olsson et al. (2022).
Therefore, although related work provides comprehensive                                                  η X
                                                                                                             N
empirical evidence that Transformers indeed seem to im-                 ∆W = −η∇W L(W ) = −                    (W xi − yi )xTi .   (3)
                                                                                                         N i=1
plement gradient descent based learning on the data given
in-context, we will in the following present mechanistic
verification of this hypothesis and provide compelling ev-           Considering the loss after changing the weights, we obtain
idence that our construction, which implements GD in a
Transformer forward pass, is found in practice.                                                  N
                                                                                             1 X                      2
                                                                        L(W + ∆W ) =               ∥(W + ∆W )xi − yi ∥
                                                                                            2N i=1
2. Linear self-attention can emulate gradient                                                                                      (4)
                                                                                                 N
   descent on a linear regression task                                                     1 X
                                                                                        =        ∥W xi − (yi − ∆yi )∥2
                                                                                          2N i=1
We start by reviewing a standard multi-head self-attention
(SA) layer with parameters θ. A SA layer updates each
element ej of a set of tokens {e1 , . . . , eN } according to        where we introduced the transformed targets yi − ∆yi with
                                                                     ∆yi = ∆W xi . Thus, we can view the outcome of a gradient
          ej ← ej + SAθ (j, {e1 , . . . , eN })                      descent step as an update to our regression loss (equation 2),
                    X
                                                          (1)        where data, and not weights, are updated. Note that this
             = ej +   Ph Vh softmax(KhT qh,j )
                                                                     formulation is closely linked to predicting based on nonpara-
                       h
                                                                     metric kernel smoothing, see Appendix A.8 for a discussion.
with Ph , Vh , Kh the projection, value and key matrices, re-
                                                                     Returning to self-attention mechanisms and Transformers,
spectively, and qh,i the query, all for the h-th head. To sim-
                                                                     we consider an in-context learning problem where we are
plify the presentation, we omit bias terms here and through-
                                                                     given N context tokens together with an extra query to-
out. The columns of the value Vh = [vh,1 , . . . , vh,N ] and
                                                                     ken, indexed by N + 1. In terms of our linear regression
key Kh = [kh,1 , . . . , kh,N ] matrices consist of vectors
                                                                     problem, the N context tokens ej = (xj , yj ) ∈ RNx +Ny
vh,i = Wh,V ei and kh,i = Wh,K ei ; likewise, the query is
                                                                     correspond to the N training points in D, and the N +1-th
produced by linearly projecting the tokens, qh,j = Wh,Q ej .
                                                                     token eN +1 = (xN +1 , yN +1 ) = (xtest , ŷtest ) = etest to the
The parameters θ = {Ph , Wh,V , Wh,K , Wh,Q }h of a SA
                                                                     test input xtest and the corresponding prediction ŷtest . We
layer consist of all the projection matrices, of all heads.
                                                                     use the terms training and in-context data interchangeably,
The self-attention layer described above corresponds to              as well as query and test token/data, as we establish their
the one used in the standard Transformer model. Follow-              equivalence now.

                                                                 3


---

                                       Transformers Learn In-Context by Gradient Descent

Transformations induced by gradient descent and a                             sufficient to transform our training targets as well as
linear self-attention layer can be equivalent                                 the test prediction simultaneously.
We have re-cast the task of learning a linear model as di-                  • Uniqueness. We note that the construction is not
rectly modifying the data, instead of explicitly computing                    unique; in particular, it is only required that the prod-
and returning the weights of the model (equation 4). We                       ucts P WV as well as WK WQ match the construc-
proceed to establish a connection between self-attention and                  tion. Furthermore, since no nonlinearity is present,
gradient descent. We provide a construction where learning                    any rescaling s of the matrix products, i.e., P WV s and
takes place simultaneously by directly updating all tokens,                   WK WQ /s, leads to an equivalent result. If we correct
including the test token, through a linear self-attention layer.              for these equivalent formulations, we can experimen-
In other words, the token produced in response to a query                     tally verify that weights of our learned Transformers
(test) token is transformed from its initial value W0 xtest ,                 indeed match the presented construction.
where W0 is the initial value of W , to the post-learning
prediction ŷ = (W0 + ∆W )xtest obtained after one gradient                 • Meta-learned task-shared learning rates. When
descent step.                                                                 training self-attention parameters θ across a family of
Proposition 1. Given a 1-head linear attention layer and                      in-context learning tasks τ , where the data (xτ,i , yτ,i )
the tokens ej = (xj , yj ), for j = 1, . . . , N , one can con-               follows a certain distribution, the learning rate can be
struct key, query and value matrices WK , WQ , WV as well                     implicitly (meta-)learned such that an optimal loss re-
as the projection matrix P such that a Transformer step on                    duction (averaged over tasks) is achieved given a fixed
every token ej is identical to the gradient-induced dynam-                    number of update steps. In our experiments, we find
ics ej ← (xj , yj ) + (0, −∆W xj ) = (xj , yj ) + P V K T qj                  this to be the case. This kind of meta-learning to im-
such that ej = (xj , yj − ∆yj ). For the test data token                      prove upon plain gradient descent has been leveraged
(xN +1 , yN +1 ) the dynamics are identical.                                  in numerous previous approaches for deep neural net-
                                                                              works (Li et al., 2017; Lee & Choi, 2018; Park & Oliva,
The simple construction can be found in Appendix A.1 and                      2019; Zhao et al., 2020; Flennerhag et al., 2020).
we denote the corresponding self-attention weights by θGD .
                                                                            • Task-specific data transformations. A self-attention
Below, we provide some additional insights on what is                         layer is in principle further capable of exploiting statis-
needed to implement the provided LSA-layer weight con-                        tics in the current training data samples, beyond mod-
struction, and further details on what it can achieve:                        eling task-shared curvature information in θ. More
                                                                              concretely, a LSA layer updates an input sample ac-
   • Full self-attention. Our dynamics model training is                      cording to a data transformation xj ← xj + ∆xj =
     based on in-context tokens only, i.e., only e1 , . . . , eN              (I + P (X)V (X)K(X)T WQ )xj = Hθ (X)xj , with
     are used for computing key and value matrices; the                       X the Nx × N input training data matrix, when ne-
     query token eN +1 (containing test data) is excluded.                    glecting influences by target data yi . Through Hθ (X),
     This leads to a linear function in xtest as well as to                   a LSA layer can encode in θ an algorithm for carrying
     the correct ∆W , induced by gradient descent on a                        out data transformations which depend on the actual
     loss consisting only of the training data. This is a                     input training samples in X. In our experiments, we
     minor deviation from full self-attention. In practice,                   see that trained self-attention learners employ a simple
     this modification can be dropped, which corresponds                      form of H(X) and that this leads to substantial speed
     to assuming that the underlying initial weight matrix                    ups in for GD and TF learning.
     is zero, W0 ≈ 0, which makes ∆W in equation 8
     independent of the test token even if incorporating it
     in the key and value matrices. In our experiments, we               3. Trained Transformers do mimic gradient
     see that these assumptions are met when initializing                   descent on linear regression tasks
     the attention weights θ to small values.
                                                                         We now experimentally investigate whether trained
   • Reading out predictions. When initializing the y-                   attention-based models implement gradient-based in-
     entry of the test-data token with −W0 xN +1 , i.e. etest =          context learning in their forward passes. We gradually build
     (xtest , −W0 xtest ), the test-data prediction ŷ can be eas-       up from single linear self-attention layers to multi-layer non-
     ily read out by simply multiplying again by −1 the                  linear models, approaching full Transformers. In this sec-
     updated token, since −yN +1 + ∆yN +1 = −(yN +1 −                    tion, we follow the assumption of Proposition 1 tightly and
     ∆yN +1 ) = yN +1 + ∆W xN +1 . This can easily be                    construct our tokens by concatenating input and target data,
     done by a final projection matrix, which incidentally               ej = (xj , yj ) for 1 ≤ j ≤ N , and our query token by con-
     is usually found in Transformer architectures. Impor-               catenating the test input and a zero vector, eN +1 = (xtest , 0).
     tantly, we see that a single head of self-attention is              We show how to lift this assumption in the last section of the

                                                                     4


---

                                                         Transformers Learn In-Context by Gradient Descent
       0.40                                        2.5                                                                                                                  Test on larger inputs
                            GD                               Preds diff       Model cos
                            Trained TF                       Model diff                    1.00                                                                          GD
       0.35                                        2.0                                                                                                                   Interpolated
                                                                                                                                                                         Trained TF




                                                                                                Cosine sim
                                                   1.5                                     0.95




                                         L2 Norm
                                                                                                                                                            100
Loss



       0.30




                                                                                                                                                    Loss
                                                   1.0                                     0.90
       0.25                                        0.5                                     0.85
                                                                                                                                                           10 1
       0.20                                        0.0                               0.80
              0     2000      4000                       0   1000 2000 3000 4000 5000                                                                             0.5       1.0         1.5      2.0
                  Training steps                                 Training steps                                                                                          where x        U( , )

Figure 2. Comparing one step of GD with a trained single linear self-attention layer. Outer left: Trained single LSA layer performance
is identical to the one of gradient descent. Center left: Almost perfect alignment of GD and the model generated by the SA layer after
training, measured by cosine similarity and the L2 distance between models as well as their predictions. Center right: Identical loss of
GD, the LSA layer model as well as the model obtained by interpolating between the construction and the optimized LSA layer weights
for different N = Nx . Outer right: The trained LSA layer, gradient descent and their interpolation show identically loss (in log-scale)
when provided input data different than during training i.e. with scale of 1. We display the mean/std. or the single runs of 5 seeds.

paper. The prediction ŷθ ({eτ,1 , . . . , eτ,N }, eτ,N +1 ) of the                                          One-step of gradient descent vs. a single trained
attention-based model, which depends on all tokens and on                                                    self-attention layer
the parameters θ, is read-out from the y-entry of the updated
                                                                                                             Our first goal is to investigate whether a trained single, linear
N + 1-th token as explained in the previous section.
                                                                                                             self-attention layer can be explained by the provided weight
The objective of training, visualized in Figure 1, is to mini-                                               construction that implements GD. To that end, we compare
mize the expected squared prediction error, averaged over                                                    the predictions made by a LSA layer with trained weights θ∗
tasks minθ Eτ [||ŷθ ({eτ,1 , . . . , eτ,N }, eτ,N +1 ) − yτ,test ||2 ].                                     (which minimize equation 5) and with constructed weights
We achieve this by minibatch online minimization (by Adam                                                    θGD (which satisfy Proposition 1).
(Kingma & Ba, 2014)): At every optimization step, we con-
                                                                                                             Recall that a LSA layer yields the prediction ŷθ (xtest ) =
struct a batch of novel training tasks and take a step of
                                                                                                             eN +1 + LSAθ ({e1 , . . . , eN }, eN +1 ) = ∆Wθ,D xtest , which
stochastic gradient descent on the loss function:
                                                                                                             is linear in xtest . We denote by ∆Wθ,D the matrix generated
                       B
              1 X                                                                                            by the LSA layer following the construction provided in
       L(θ) =        ||ŷθ ({eτ,i }N
                                   i=1 , eτ,N +1 ) − yτ,test ||
                                                               2
                                                                                          (5)                Proposition 1, with query token eN +1 set such that the initial
              B τ =1
                                                                                                             prediction is set to zero, ŷtest = 0. We compare ŷθ (xtest ) to
where each task (context) τ consists of in-context                                                           the prediction of the control LSA ŷθGD (xtest ), which under
training data Dτ = {(xτ,i , yτ,i )}N         i=1 and test point                                              our token construction corresponds to a linear model trained
(xτ,N +1 , yτ,N +1 ), which we use to construct our tokens                                                   by one step of gradient descent starting from W0 = 0. For
{eτ,i }N +1
       i=1 as described above. We denote the optimal pa-                                                     this control model, we determine the optimal learning rate η
rameters found by this optimization process by θ∗ . In our                                                   by minimizing L(η) over a training set of 104 tasks through
setup, finding θ∗ may be thought of as meta-learning, while                                                  line search, with L(η) defined analogously to equation 5.
learning a particular task τ corresponds to simply evaluat-
ing the model ŷθ ({eτ,1 , . . . , eτ,N }, eτ,N +1 ). Note that we                                           More concretely, to compare trained and constructed LSA
therefore never see the exact same training task twice during                                                layers, we sample Tval = 104 validation tasks and record
training. See Appendix A.12, especially Figure 16 for an                                                     the following quantities, averaged over validation tasks: (1)
analyses when using a fixed dataset size which we cycle                                                      the difference in predictions measured with the L2 norm,
over during training.                                                                                        ∥ŷθ (xτ,test ) − ŷθGD (xτ,test )∥, (2) the cosine similarity be-
                                                                                                                                        ∂ ŷθGD (xτ,test )        ∂ ŷ (xτ,test )
                                                                                                             tween the sensitivities         ∂xtest        and θ∂xtest            as well as
We focus on solvable tasks and similarly to Garg et al.                                                                             ∂ ŷθGD (xτ,test )     ∂ ŷθ (xτ,test )
(2022) generate data for each task using a teacher model                                                     (3) their difference ∥       ∂xtest       − ∂xtest ∥ again accord-
with parameters Wτ ∼ N (0, I). We then sample xτ,i ∼                                                         ing to the L2 norm, which in both cases yields the explicit
U (−1, 1)nI and construct targets using the task-specific                                                    models computed by the algorithm. We show the results
teacher model, yτ,i = Wτ xτ,i . In the majority of our exper-                                                of these comparisons in Figure 2. We find an excellent
iments we set the dimensions to N = nI = 10 and nO = 1.                                                      agreement between the two models over a wide range of
Since we use a noiseless teacher for simplicity, we can ex-                                                  hyperparameters. We note that as we do not have direct ac-
pect our regression tasks to be well-posed and analytically                                                  cess to the initialization of W in the attention-based learners
solvable as we only compute a loss on the Transformers                                                       (it is hidden in θ), we cannot expect the models to agree
last token, which stands in contrast to usual autoregressive                                                 exactly.
training and the training setup of Garg et al. (2022). Full                                                  Although the above metrics are important to show simi-
details and results for training with a fixed training set size                                              larities between the resulting learned models (in-context
may be found in Appendix A.12.

                                                                                                   5


---

                                    Transformers Learn In-Context by Gradient Descent

vs. gradient-based), the underlying algorithms could still          that (approximately) coincide with the LSA-layer weight
be different. We therefore carry out an extended set of             construction of Proposition 1, hence implementing a step of
analyses:                                                           gradient descent, leading to the same learning capabilities
                                                                    on in- and out-of-distribution tasks. We comment on the
 1. Interpolation. We take inspiration on recent work               random seed dependent phase transition of the loss during
    (Benzing et al., 2022; Entezari et al., 2021) that showed       training in Appendix A.11.
    approximate equivalence of models found by SGD af-
    ter permuting weights within the trained neural net-            Multiple steps of gradient descent vs. multiple layers of
    works. Since our models are deep linear networks with           self-attention
    respect to xtest we only correct for scaling mismatches
    between the two models – in this case the construction          We now turn to deep linear self-attention-only Transform-
    that implements GD and the trained weights. As shown            ers. The construction we put forth in Proposition 1, can
    in Figure 2, we observe (and can actually inspect by            be immediately stacked up over K layers; in this case, the
    eye, see Appendix Figure 9) that a simple scaling cor-          final prediction can be read out from the last layer as before
    rection on the trained weights is enough to recover the         by negating the y-entry of the last test token: −yN +1 +
                                                                    PK                              PK
    weight construction implementing GD. This leads to an                   ∆yk,N +1 = −(yN +1 − k=1 ∆yk,N +1 ) = yN +1 +
                                                                    Pk=1
                                                                       K
    identical loss of GD, the trained Transformer and the              k=1 ∆Wk xN +1 , where yk,N +1 are the test token values
    linearly interpolated weights θI = (θ + θGD )/2. See            at layer k, and ∆yk,N +1 the change in the y-entry of the
    details in Appendix A.3 on how our weight correction            test token after applying the k-th step of self-attention, and
    and interpolation is obtained.                                  ∆Wk the k-th implicit change in the underlying linear model
                                                                    parameters W . When optimizing such Transformers with
 2. Out-of-distribution validation tasks. To test if our            K layers, we observe that these models generally outper-
    in-context learner has found a generalizable update             form K steps of plain gradient descent, see Figure 3. Their
    rule, we investigate how GD, the trained LSA layer              behavior is however well described by a variant of gradient
    and its interpolation behave when providing in-context          descent, for which we tune a single parameter γ defined
    data in regimes different to the ones used during train-        through the transformation function H(X) which trans-
    ing. We therefore visualize the loss increase when (1)          forms the input data according to xj ← H(X)xj , with
    sampling the input data from U (−α, α)Nx or (2) scal-           H(X) = (I − γXX T ). We term this gradient descent
    ing the teacher weights by α as αW when sampling                variant GD++ which we explain and analyze in Appendix
    validation tasks. For both cases, we set α = 1 dur-             A.10.
    ing training. We again observe that when training a
    single linear self-attention Transformer, for both inter-       To analyze the effect of adding more layers to the architec-
    ventions, the Transformer performs equally to gradient          ture, we first turn to the arguably simplest extension of a
    descent outside of this training setups, see Figure 2 as        single SA layer and analyze a recurrent or looped 2-layer
    well Appendix Figure 6. Note that the loss obtained             LSA model. Here, we simply repeatably apply the same
    through gradient descent also starts degrading quickly          layer (with the same weights) multiple times i.e. drawing
    outside the training regime. Since we tune the learning         the analogy to learning an iterative algorithm that applies
    rate for the input range [−1, 1] and one gradient step,         the same logic multiple times.
    tasks with larger input range will have higher curvature        Somewhat surprisingly, we find that the trained model sur-
    and the optimal learning rate for smaller ranges will           passes plain gradient descent, which also results in decreas-
    lead to divergence and a drastic increase in loss also          ing alignment between the two models (see center left col-
    for GD.                                                         umn), and the recurrent Transformer realigns perfectly with
 3. Repeating the LSA update. Since we claim that a sin-            GD++ while matching its performance on in- and out-of
    gle trained LSA layer implements a GD-like learning             distribution tasks. Again, we can interpolate between the
    rule, we further test its behavior when applying it re-         Transformer weights found by optimization and the LSA-
    peatedly, not only once as in training. After we correct        weight construction with learned η, γ, see Figure 3 & 6.
    the learning rate of both algorithms, i.e. for GD and           We next consider deeper, non-recurrent 5-layer LSA-only
    the trained Transformer with a dampening parameter              Transformers, with different parameters per layer (i.e. no
    λ = 0.75 (details in Appendix A.6), we see an identi-           weight tying). We see that a different GD learning rate as
    cal loss decrease of both GD and the Transformer, see           well as γ per step (layer) need to be tuned to match the
    Figure 1.                                                       Transformer performance. This slight modification leads
                                                                    again to almost perfect alignment between the trained TF
To conclude, we present evidence that optimizing a single           and GD++ with in this case 10 additional parameters and
LSA layer to solve linear regression tasks finds weights

                                                                6


---

                                                                Transformers Learn In-Context by Gradient Descent

(a) Comparing two steps of gradient descent with trained recurrent two-layer Transformers.
         0.40
                                                               2.5
                                                                         GD vs trained TF                                            GD+ + vs trained TF                              104
                                                                                                                                                                                                  Test on larger inputs
                                        GD                                                                                 2.5
         0.35                           GD+ +                                        Model cos                                                    Model cos                                        GD
                                        Trained TF             2.0                           1.0                           2.0                            1.0                         103          GD+ +
         0.30                                                                                0.9                                                          0.9                                      Interpolated




                                                                                                    Cosine sim
                                                                                                                                                                                      102




                                                                                                                                                                 Cosine sim
                                                               1.5                                                                                                                                 Trained TF




                                                     L2 Norm
                                                                                                                           1.5




                                                                                                                 L2 Norm
                                                                                  Preds diff                                                   Preds diff
  Loss




         0.25




                                                                                                                                                                              Loss
                                                                                  Model diff 0.8                                               Model diff 0.8                         101
         0.20                                                  1.0                                                         1.0
                                                                                             0.7                                                          0.7                         100
         0.15                                                  0.5                           0.6                           0.5                            0.6                        10 1
         0.10                                                  0.0                           0.5                           0.0                            0.5
                    0   1000     2000      3000                      0     1000 2000 3000                                        0      1000 2000 3000                                      0.5       1.0         1.5      2.0
                         Training steps                                    Training steps                                               Training steps                                             where x        U( , )
(b) Comparing five steps of gradient descent with trained five-layer Transformers.
         0.4                                                             GD vs trained TF                                            GD+ + vs trained TF                                          Test on larger inputs
                                 GD                            2.0                                                         2.0
                                 GD+ + 5 steps                                      Model cos 1.05                                               Model cos 1.05                                    GD
         0.3                                                                                                                                                                          101          GD+ +
                                 Trained TF                    1.5                            1.00                         1.5                             1.00                                    Trained TF




                                                                                                    Cosine sim




                                                                                                                                                                 Cosine sim
                                                                                                                                                                                      100
                                                     L2 Norm




                                                                                                                 L2 Norm
                                                                                    Preds diff 0.95                                              Preds diff 0.95




                                                                                                                                                                              Loss
  Loss




         0.2                                                   1.0                                                         1.0
                                                                                    Model diff                                                   Model diff
                                                                                               0.90                                                         0.90                     10 1
         0.1                                                   0.5                                                         0.5
                                                                                                 0.85                                                         0.85
                                                                                                                                                                                     10 2
                                                               0.0                               0.80                      0.0                                0.80                          0.5       1.0         1.5      2.0
                0        20000      40000                            0      20000    40000                                       0       20000    40000                                            where x        U( , )
                        Training steps                                    Training steps                                               Training steps
Figure 3. Far left column: The trained TF performance surpasses standard GD but matches GD++ , our GD variant with simple iterative
data transformation. On both cases, we tuned the gradient descent learning rates as well as the scalar γ which governs the data
transformation H(X). Center left & center right columns: We measure the alignment between the GD as well as the GD++ models and
the trained TF. In both cases the TF aligns well with GD in the beginning of training but aligns much better with GD++ after training. Far
right column: TF performance (in log-scale) mimics the one of GD++ well when testing on OOD tasks (α ̸= 1).

loss close to 0, see Figure 3. Nevertheless, we see that the                                                         plained by gradient descent on linear models. We now show
naive correction necessary for model interpolation used in                                                           that this limitation can be resolved by incorporating one
the aforementioned experiments is not enough to interpolate                                                          additional element of fully-fledged Transformers: preceding
without a loss increase. We leave a search for better weight                                                         self-attention layers by MLPs enables learning linear models
corrections to future work. We further study Transformers                                                            by gradient descent on deep representations which motivates
with different depths for recurrent as well as non-recurrent                                                         our illustration in Figure 1. Empirically, we demonstrate
architectures with multiple heads and equipped with MLPs,                                                            this by solving non-linear sine-wave regression tasks, see
and find qualitatively equivalent results, see Appendix Fig-                                                         Figure 4. Experimental details can be found in Appendix
ure 7 and Figure 8. Additionally, in Appendix A.9, we                                                                A.7. We state
provide results obtained when using softmax SA layers as                                                             Proposition 2. Given a Transformer block i.e. a MLP m(e)
well as LayerNorm, thus essentially retrieving the standard                                                          which transforms the tokens ej = (xj , yj ) followed by an at-
Transformer architecture. We again observe and are able                                                              tention layer, we can construct weights
to explain (after slight architectural modifications) good                                                                                           1
                                                                                                                                                        PN that lead to gradient 2
                                                                                                                     descent dynamics descending 2N       i=1 ||W m(xi ) − yi || .
learning performance and as well as alignment with the con-                                                          Iteratively applying Transformer blocks therefore can solve
struction of Proposition 1, though worse than when using                                                             kernelized least-squares regression problems with kernel
linear self-attention. These findings suggest that the in-                                                           function k(x, y) = m(x)⊤ m(y) induced by the MLP m(·).
context learning abilities of the standard Transformer with
these common architecture choices can be explained by                                                                A detailed discussion on this form of kernel regression as
the gradient-based learning hypothesis explored here. Our                                                            well as kernel smoothing w/wo softmax nonlinearity through
findings also question the ubiquitous use of softmax atten-                                                          gradient descent on the data can be found in Appendix
tion, and suggest further investigation is warranted into the                                                        A.8. The way MLPs transform data in Transformers di-
performance of linear vs. softmax SA layers in real-world                                                            verges from the standard meta-learning approach, where
learning tasks, as initiated by Schlag et al. (2021).                                                                a task-shared input embedding network is optimized by
                                                                                                                     backpropagation-through-training to improve the learning
Transformers solve nonlinear regression tasks by                                                                     performance of a task-specific readout (e.g., Raghu et al.,
gradient descent on deep data representations                                                                        2020; Lee et al., 2019; Bertinetto et al., 2019). On the other
                                                                                                                     hand, given our token construction in Proposition 1, MLPs
It is unreasonable to assume that the astonishing in-context
                                                                                                                     in Transformers intriguingly process both inputs and targets.
learning flexibility observed in large Transformers is ex-
                                                                                                                     The output of this transformation is then processed by a sin-

                                                                                                                 7


---

                                      Transformers Learn In-Context by Gradient Descent

gle linear self-attention layer, which, according to our theory,       before the Transformer performance jumps to the one of
is capable of implementing gradient descent learning. We               GD, token ej transformed by the first self-attention layer
compare the performance of this Transformer model, where               becomes notably dependant on the neighboring token ej+1
all weights are learned, to a control Transformer where the            while staying independent on the others which we denote as
final LSA weights are set to the construction θGD which is             eother in Figure 5.
therefore identical to training an MLP by backpropagation                     0.55                                                         3.5
through a GD updated output layer.                                                                  GD 1 step
                                                                              0.50                                                         3.0




                                                                                                                  Norm part. derivatives
                                                                                                    TF 2 layers
Intriguingly, both obtained functions show again surprising                   0.45                                                         2.5
                                                                              0.40                                                         2.0        t(ej)/ ej
similarity on (1) the initial (meta-learned) prediction, read                                                                                         t(ej)/ ej + 1




                                                                       Loss
out after the MLP, and (2) the final prediction, after altering               0.35                                                         1.5        t(ej)/ eother
the output of the MLP through GD or the self-attention layer.                 0.30                                                         1.0
This is again reflected in our alignment measures that now,                   0.25                                                         0.5
since the obtained models are nonlinear w.r.t. xtest , only rep-              0.20                                                         0.0
                                                                                     0   10000 20000 30000 40000                                 0   10000 20000 30000 40000
resent the two first parts of the Taylor approximation of the                             Training steps                                               Training steps
obtained functions. Our results serve as a first demonstra-            Figure 5. Training a two layer SA-only Transformer using the
tion of how MLPs and self-attention layers can interplay to            standard token construction. Left: The loss of trained TFs
support nonlinear in-context learning, allowing to fine-tune           matches one step of GD, not two, and takes an order of magnitude
deep data representations by gradient descent. Investigating           longer to train. Right: Norm of the partial derivatives of the
the interplay between MLPs and SA-layer in deep TFs is                 output of the first self-attention layer w.r.t. input tokens. Before the
left for future work.                                                  Transformer performance jumps to the one of GD, the first layer
                                                                       becomes highly sensitive to the next token.

4. Do self-attention layers build regression                           We interpret this as evidence for a copying mechanism of
   tasks?                                                              the Transformer’s first layer to merge input and output data
                                                                       into single tokens as required by Proposition 1. Then, in
The construction provided in Proposition 1 and the previ-              the second layer the Transformer performs a single step of
ous experimental section relied on a token structure where             GD. Notably, we were not able to train the Transformer
both input and output data are concatenated into a single              with linear self-attention layers, but had to incorporate the
token. This design is different from the way tokens are typi-          softmax operation in the first layer. These preliminary find-
cally built in most of the related work dealing with simple            ings support the study of Olsson et al. (2022) showing that
few-shot learning problems as well as in e.g. language mod-            softmax self-attention layers easily learn to copy; we con-
eling. We therefore ask: Can we overcome the assumption                firm this claim, and further show that such copying allows
required in Proposition 1 and allow a Transformer to build             the Transformer to proceed by emulating gradient-based
the required token construction on its own? This motivates             learning in the second or deeper attention layers.
Proposition 3. Given a 1-head linear or softmax atten-                 We conclude that copying through (softmax) attention layers
tion layer and the token construction e2j = (xj ), e2j+1 =             is the second crucial mechanism for in-context learning
(0, yj ) with a zero vector 0 of dim Nx − Ny and concate-              in Transformers. This operation enables Transformers to
nated positional encodings, one can construct key, query               merge data from different tokens and then to compute dot
and value matrix WK , WQ , WV as well as the projection                products of input and target data downstream, allowing for
matrix P such that all tokens ej are transformed into tokens           in-context learning by gradient descent to emerge.
equivalent to the ones required in Proposition 1.
                                                                       5. Discussion
The construction and its discussion can be found in Ap-
pendix A.5. To provide evidence that copying is per-                   Transformers show remarkable in-context learning behavior.
formed in trained Transformers, we optimize a two-layer                Mechanisms based on attention, associative memory and
self-attention circuit on in-context data where alternating            copying by induction heads are currently the leading expla-
tokens include input or output data i.e. e2j = (xj ) and               nations for this remarkable feature of learning within the
e2j+1 = (0, yj ). We again measure the loss as well as the             Transformer forward pass. In this paper, we put forward the
mean of the norm of the partial derivative of the first layer’s        hypothesis, similar to Garg et al. (2022) and Akyürek et al.
output w.r.t. the input tokens during training, see Figure 5.          (2023), that Transformer’s in-context learning is driven by
First, the training speeds are highly variant given different          gradient descent, in short – Transformers learn to learn by
training seeds, also reported in Garg et al. (2022). Never-            gradient descent based on their context. Viewed through
theless, the Transformer is able to match the performance              the lens of meta-learning, learning Transformer weights cor-
of a single (not two) step gradient descent. Interestingly,            responds to the outer-loop which then enables the forward

                                                                   8


---

                                             Transformers Learn In-Context by Gradient Descent
                                                                        0.006                                        0.08
         0.6          GT         GD init         Tr. TF init                          GD                                               Partial cosine
                      Data       GD step 1       Tr. TF step 1          0.005         Trained TF                                                        1.0
         0.4                                                                                                         0.06
                                                                        0.004                                                                           0.9




                                                                                                                                                         Cosine sim
         0.2




                                                                                                           L2 Norm
                                                                 Loss
                                                                        0.003                                        0.04                               0.8
     y


         0.0
                                                                        0.002                                                                           0.7
         0.2                                                                                                         0.02
                                                                        0.001                                                    Preds diff             0.6
         0.4                                                                                                                     Partial diff
                                                                        0.000                                        0.00                               0.5
                  4          2      0        2        4                         0       20000      40000                    0     20000         40000
                                    x                                                 Training steps                            Training steps
Figure 4. Sine wave regression: comparing trained Transformers with meta-learned MLPs for which we adjust the output layer
with one step of gradient descent. Left: Plots of the learned initial functions as well as the adjusted functions through either a layer
of self-attention or a step of GD. We observe similar initial functions as well as solutions for the trained TF compared fine-tuning a
meta-learned MLP. Center: The performance of the trained Transformer is matched by meta-learned MLPs. Left: We observe strong
alignment when comparing the prediction as well as the partial derivatives of the the meta-learned MLP and the trained Transformer.

pass to transform tokens by gradient-based optimization.                        gradient descent motives us to investigate how to improve
                                                                                it. We are excited about several avenues of future research.
To provide evidence for this hypothesis, we build on Schlag
                                                                                First, to exceed upon a single step of gradient descent in
et al. (2021) that already provide a linear self-attention layer
                                                                                every self-attention layer it could be advantageous to incor-
variant with (fast-)inner loop learning by the error-correcting
                                                                                porate so called declarative nodes (Amos & Kolter, 2017;
delta rule (Widrow & Hoff, 1960). We diverge from their set-
                                                                                Bai et al., 2019; Gould et al., 2021; Zucchet & Sacramento,
ting and focus on (in-context) learning where we specifically
                                                                                2022) into Transformer architectures. This way, we would
construct a dataset by considering neighboring elements in
                                                                                treat a single self-attention layer as the solution of a fully
the input sequence as input- and target training pairs, see
                                                                                optimized regression loss leading to possibly more efficient
assumptions of Proposition 1. This construction could be
                                                                                architectures. Second, our findings are restricted to small
realized, for example, due to the model learning to imple-
                                                                                Transformers and simple regression problems. We are ex-
ment a copying layer, see section 4 and proposition 3, and
                                                                                cited to delve deeper into research trying to understand how
allows us to provide a simple and different construction to
                                                                                further mechanistic understanding of Transformers and in-
Schlag et al. (2021) that solely is built on the standard lin-
                                                                                context learning in larger models is possible and to what
ear, and approximately softmax, self-attention layer but still
                                                                                extend. Third, we are excited about targeted modifications
implements gradient descent based learning dynamics. We,
                                                                                to Transformer architectures, or their training protocols,
therefore, are able to explain gradient descent based learn-
                                                                                leading to improved gradient descent based learning algo-
ing in these standard architectures. Furthermore, we extend
                                                                                rithms or allow for alternative in-context learners to be im-
this construction based on a single self-attention layer and
                                                                                plemented within Transformer weights, augmenting their
provide an explanation of how deeper K-layer Transformer
                                                                                functionality, as e.g. in Dai et al. (2023). Finally, it would
models implement principled K-step gradient descent learn-
                                                                                be interesting to analyze in-context learning in HyperTrans-
ing, which deviates again from Schlag et al. and allows
                                                                                formers (Zhmoginov et al., 2022) that produce weights for
us to identify that deep Transformers implement GD++, an
                                                                                target networks and already offer a different perspective on
accelerated version of gradient descent.
                                                                                merging Transformers and meta-learning. There, Transform-
We highlight that our construction of gradient descent and                      ers transform weights instead of data and could potentially
GD++ is not suggestive but when training multi-layer self-                      allow for gradient computations of weights deep inside the
attention-only Transformers on simple regression tasks, we                      target network lifting the limitation of GD on linear models
provide strong evidence that the construction is actually                       analyzed here.
found. This allows us, at least in our restricted problems
settings, to explain mechanistically in-context learning in                         Acknowledgments
trained Transformers and its close resemblance to GD ob-
served by related work. Further work is needed to incor-                        João Sacramento and Johannes von Oswald deeply thank
porate regression problems with noisy data and weight reg-                      Angelika Steger for her support and guidance. The authors
ularization into our hypothesis. We speculate aspects of                        also thank Seijin Kobayashi, Marc Kaufmann, Nicolas Zuc-
learning in these settings are meta-learned – e.g., the weight                  chet, Yassir Akram, Guillaume Obozinski and Mark Sandler
magnitudes to be encoded in the self-attention weights. Ad-                     for many valuable insights throughout the project and Dale
ditionally, we did not analyze logistic regression for which                    Schuurmans and Timothy Nguyen for their valuable com-
one possible weight construction is already presented in                        ments on the manuscript. João Sacramento was supported
Zhmoginov et al. (2022).                                                        by an Ambizione grant (PZ00P3 186027) from the Swiss
                                                                                National Science Foundation and an ETH Research Grant
Our refined understanding of in-context learning based on                       (ETH-23 21-1).

                                                                           9


---

                                      Transformers Learn In-Context by Gradient Descent

References                                                               Chalmers, D. J. The evolution of learning: an experiment in
                                                                           genetic connectionism. In Touretzky, D. S., Elman, J. L.,
Akyürek, E., Schuurmans, D., Andreas, J., Ma, T., and
                                                                           Sejnowski, T. J., and Hinton, G. E. (eds.), Connectionist
  Zhou, D. What learning algorithm is in-context learn-
                                                                           Models, pp. 81–90. Morgan Kaufmann, 1991.
  ing? investigations with linear models. In The Eleventh
 International Conference on Learning Representations,                   Chan, S. C. Y., Dasgupta, I., Kim, J., Kumaran, D.,
  2023. URL https://openreview.net/forum?                                  Lampinen, A. K., and Hill, F. Transformers general-
  id=0g0X4H8yN4I.                                                          ize differently from information stored in context vs in
                                                                           weights. arXiv preprint arXiv:2210.05675, 2022a.
Amos, B. and Kolter, J. Z. Optnet: Differentiable opti-
 mization as a layer in neural networks. In International                Chan, S. C. Y., Santoro, A., Lampinen, A. K., Wang, J. X.,
 Conference on Machine Learning, 2017.                                     Singh, A., Richemond, P. H., McClelland, J., and Hill, F.
                                                                           Data distributional properties drive emergent in-context
Andrychowicz, M., Denil, M., Gomez, S., Hoffman, M. W.,                    learning in transformers. Advances in Neural Information
  Pfau, D., Schaul, T., Shillingford, B., and de Freitas, N.               Processing Systems, 2022b.
  Learning to learn by gradient descent by gradient descent.
  In Advances in Neural Information Processing Systems,                  Choromanski, K. M., Likhosherstov, V., Dohan, D., Song,
  2016.                                                                    X., Gane, A., Sarlos, T., Hawkins, P., Davis, J. Q., Mo-
                                                                           hiuddin, A., Kaiser, L., Belanger, D. B., Colwell, L. J.,
Ba, J., Hinton, G. E., Mnih, V., Leibo, J. Z., and Ionescu,                and Weller, A. Rethinking attention with performers. In
  C. Using fast weights to attend to the recent past. In                   International Conference on Learning Representations,
  Advances in Neural Information Processing Systems 29,                    2021. URL https://openreview.net/forum?
  2016.                                                                    id=Ua6zuk0WRH.
Bai, S., Kolter, J. Z., and Koltun, V. Deep equilibrium                  Dai, D., Sun, Y., Dong, L., Hao, Y., Ma, S., Sui, Z., and Wei,
  models. Advances in Neural Information Processing                        F. Why can GPT learn in-context? language models im-
  Systems, 2019.                                                           plicitly perform gradient descent as meta-optimizers. In
Bengio, Y., Bengio, S., and Cloutier, J. Learning a                        ICLR 2023 Workshop on Mathematical and Empirical Un-
  synaptic learning rule. Technical report, Université de                 derstanding of Foundation Models, 2023. URL https:
  Montréal, Département d’Informatique et de Recherche                   //openreview.net/forum?id=fzbHRjAd8U.
  opérationnelle, 1990.                                                 Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn,
                                                                           D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer,
Benzing, F., Schug, S., Meier, R., von Oswald, J., Akram,
                                                                           M., Heigold, G., Gelly, S., Uszkoreit, J., and Houlsby,
  Y., Zucchet, N., Aitchison, L., and Steger, A. Random
                                                                           N. An image is worth 16x16 words: Transformers for
  initialisations performing above chance and how to find
                                                                           image recognition at scale. In International Conference
  them. OPT2022: 14th Annual Workshop on Optimization
                                                                           on Learning Representations, 2021. URL https://
  for Machine Learning, 2022.
                                                                           openreview.net/forum?id=YicbFdNTTy.
Bertinetto, L., Henriques, J. F., Torr, P. H. S., and Vedaldi, A.
                                                                         Entezari, R., Sedghi, H., Saukh, O., and Neyshabur, B. The
  Meta-learning with differentiable closed-form solvers. In
                                                                           role of permutation invariance in linear mode connectivity
  International Conference on Learning Representations,
                                                                           of neural networks. arXiv preprint arXiv:2110.06296,
  2019.
                                                                           2021.
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan,
                                                                         Finn, C. and Levine, S. Meta-learning and universality:
  J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
                                                                           Deep representations and gradient descent can approx-
  Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G.,
                                                                           imate any learning algorithm. In International Confer-
  Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu,
                                                                           ence on Learning Representations, 2018. URL https:
  J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin,
                                                                           //openreview.net/forum?id=HyjC5yWCW.
  M., Gray, S., Chess, B., Clark, J., Berner, C., McCan-
  dlish, S., Radford, A., Sutskever, I., and Amodei, D.                  Finn, C., Abbeel, P., and Levine, S. Model-agnostic meta-
  Language models are few-shot learners. arXiv preprint                    learning for fast adaptation of deep networks. In Interna-
  arXiv:2005.14165, 2020.                                                  tional Conference on Machine Learning, 2017.
Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov,              Flennerhag, S., Rusu, A. A., Pascanu, R., Visin, F., Yin,
  A., and Zagoruyko, S. End-to-end object detection with                   H., and Hadsell, R. Meta-learning with warped gradi-
  transformers. In Computer Vision – ECCV 2020. Springer                   ent descent. In International Conference on Learning
  International Publishing, 2020.                                          Representations, 2020.

                                                                    10


---

                                    Transformers Learn In-Context by Gradient Descent

Garg, S., Tsipras, D., Liang, P., and Valiant, G. What                 Conference on Neural Information Processing Systems,
  can transformers learn in-context? a case study of sim-              2022. URL https://openreview.net/forum?
  ple function classes. In Oh, A. H., Agarwal, A., Bel-                id=t6tA-KB4dO.
  grave, D., and Cho, K. (eds.), Advances in Neural In-
  formation Processing Systems, 2022. URL https:                     Lee, K., Maji, S., Ravichandran, A., and Soatto, S. Meta-
 //openreview.net/forum?id=flNZJ2eOet.                                 learning with differentiable convex optimization. In
                                                                       IEEE/CVF Conference on Computer Vision and Pattern
Gordon, J., Bronskill, J., Bauer, M., Nowozin, S., and                 Recognition, 2019.
 Turner, R. Meta-learning probabilistic inference for
                                                                     Lee, Y. and Choi, S. Gradient-based meta-learning with
  prediction. In International Conference on Learning
                                                                       learned layerwise metric and subspace. In International
 Representations, 2019. URL https://openreview.
                                                                       Conference on Machine Learning, 2018.
  net/forum?id=HkxStoC5F7.
                                                                     Li, Z., Zhou, F., Chen, F., and Li, H. Meta-SGD: Learning
Gould, S., Hartley, R., and Campbell, D. J. Deep declarative
                                                                       to learn quickly for few shot learning. arXiv preprint
  networks. IEEE Transactions on Pattern Analysis and
                                                                       arXiv:1707.09835, 2017.
  Machine Intelligence, 2021.
                                                                     Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., and Neubig,
Gulati, A., Qin, J., Chiu, C.-C., Parmar, N., Zhang, Y., Yu,
                                                                       G. Pre-train, prompt, and predict: A systematic survey of
 J., Han, W., Wang, S., Zhang, Z., Wu, Y., and Pang,
                                                                       prompting methods in natural language processing. arXiv
  R. Conformer: Convolution-augmented transformer for
                                                                       preprint arXiv:2107.13586, 2021.
  speech recognition. arXiv preprint arXiv:2005.08100,
  2020.                                                              Nadaraya, E. A. On estimating regression. Theory of Prob-
                                                                       ability & its Applications, 9(1):141–142, 1964.
Hendrycks, D. and Gimpel, K. Gaussian error linear units
  (gelus). arXiv preprint arXiv:1606.08415, 2016.                    Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma,
                                                                       N., Henighan, T., Mann, B., Askell, A., Bai, Y., Chen,
Hinton, G. E. and Plaut, D. C. Using fast weights to deblur            A., Conerly, T., Drain, D., Ganguli, D., Hatfield-Dodds,
  old memories. 1987.                                                  Z., Hernandez, D., Johnston, S., Jones, A., Kernion,
Hochreiter, S., Younger, A. S., and Conwell, P. R. Learning            J., Lovitt, L., Ndousse, K., Amodei, D., Brown, T.,
  to learn using gradient descent. In Dorffner, G., Bischof,           Clark, J., Kaplan, J., McCandlish, S., and Olah, C. In-
  H., and Hornik, K. (eds.), Artificial Neural Networks                context learning and induction heads. arXiv preprint
 — ICANN 2001, pp. 87–94, Berlin, Heidelberg, 2001.                    arXiv:2209.11895, 2022.
  Springer Berlin Heidelberg. ISBN 978-3-540-44668-2.                Park, E. and Oliva, J. B. Meta-curvature. In Advances in
Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J.,                Neural Information Processing Systems, 2019.
  and Garrabrant, S. Risks from learned optimization                 Power, A., Burda, Y., Edwards, H., Babuschkin, I., and
  in advanced machine learning systems. arXiv [cs.AI],                 Misra, V. Grokking: Generalization beyond overfitting
 Jun 2019. URL http://arxiv.org/abs/1906.                              on small algorithmic datasets. abs/2201.02177, 2022.
  01820.
                                                                     Raghu, A., Raghu, M., Bengio, S., and Vinyals, O. Rapid
Irie, K., Schlag, I., Csordás, R., and Schmidhuber, J. Going          learning or feature reuse? Towards understanding the
   beyond linear transformers with recurrent fast weight               effectiveness of MAML. In International Conference on
   programmers. CoRR, abs/2106.06295, 2021. URL                        Learning Representations, 2020.
   https://arxiv.org/abs/2106.06295.
                                                                     Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich,
Kingma, D. P. and Ba, J. Adam: A method for stochastic                 M., Adler, T., Gruber, L., Holzleitner, M., Pavlović, M.,
  optimization, 2014.                                                  Sandve, G. K., Greiff, V., Kreil, D., Kopp, M., Klambauer,
                                                                       G., Brandstetter, J., and Hochreiter, S. Hopfield networks
Kirsch, L. and Schmidhuber, J. Meta learning backpropaga-
                                                                       is all you need. arXiv preprint arXiv:2008.02217, 2020.
  tion and improving it. In Beygelzimer, A., Dauphin, Y.,
  Liang, P., and Vaughan, J. W. (eds.), Advances in Neural           Rusu, A. A., Rao, D., Sygnowski, J., Vinyals, O., Pascanu,
  Information Processing Systems, 2021. URL https:                     R., Osindero, S., and Hadsell, R. Meta-learning with
  //openreview.net/forum?id=hhU9TEvB6AF.                               latent embedding optimization. In International Confer-
                                                                       ence on Learning Representations, 2019.
Kirsch, L., Harrison, J., Sohl-Dickstein, J., and Metz, L.
  General-purpose in-context learning by meta-learning               Schlag, I., Irie, K., and Schmidhuber, J. Linear transformers
  transformers. In Sixth Workshop on Meta-Learning at the              are secretly fast weight programmers. In ICML, 2021.

                                                                11


---

                                    Transformers Learn In-Context by Gradient Descent

Schmidhuber, J. Evolutionary principles in self-referential
  learning, or on learning how to learn: the meta-meta-...
  hook. Diploma thesis, Institut für Informatik, Technische
  Universität München, 1987.
Schmidhuber, J. Learning to control fast-weight memories:
  An alternative to dynamic recurrent networks. Neural
  Computation, 4(1):131–139, 1992. doi: 10.1162/neco.
  1992.4.1.131.
Thrun, S. and Pratt, L. Learning to learn. Springer US,
  1998.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones,
  L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention
  is all you need, 2017.
von Oswald, J., Zhao, D., Kobayashi, S., Schug, S., Caccia,
  M., Zucchet, N., and Sacramento, J. Learning where to
  learn: Gradient sparsity in meta and continual learning.
  In Advances in Neural Information Processing Systems,
  2021.
Watson, G. S. Smooth regression analysis. Sankhyā: The
 Indian Journal of Statistics, Series A, pp. 359–372, 1964.
Widrow, B. and Hoff, M. E. Adaptive switching circuits.
 In 1960 IRE WESCON Convention Record, Part 4, pp.
 96–104, New York, 1960. IRE.
Yun, S., Jeong, M., Kim, R., Kang, J., and Kim, H. J. Graph
  transformer networks. In Wallach, H., Larochelle, H.,
  Beygelzimer, A., dÁlché-Buc, F., Fox, E., and Garnett,
  R. (eds.), Advances in Neural Information Processing
  Systems, 2019.
Zhang, A., Lipton, Z. C., Li, M., and Smola, A. J. Dive into
  deep learning. arXiv preprint arXiv:2106.11342, 2021.
Zhao, D., Kobayashi, S., Sacramento, J., and von Oswald, J.
  Meta-learning via hypernetworks. In NeurIPS Workshop
  on Meta-Learning, 2020.
Zhmoginov, A., Sandler, M., and Vladymyrov, M. Hy-
  perTransformer: Model generation for supervised and
  semi-supervised few-shot learning. In Chaudhuri, K.,
  Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato,
  S. (eds.), Proceedings of the 39th International Confer-
  ence on Machine Learning, volume 162 of Proceedings
  of Machine Learning Research, pp. 27075–27098. PMLR,
  17–23 Jul 2022. URL https://proceedings.mlr.
  press/v162/zhmoginov22a.html.

Zucchet, N. and Sacramento, J. Beyond backpropagation:
  bilevel optimization through implicit differentiation and
  equilibrium propagation. Neural Computation, 34(12),
  December 2022.


                                                               12


---

                                    Transformers Learn In-Context by Gradient Descent

A. Appendix
A.1. Proposition 1
First, we highlight the dependency on the tokens ei of the linear self-attention operation

                                                   X                           X        X
      ej ← ej + LSAθ ({e1 , . . . , eN }) = ej +       Ph Vh KhT qh,j = ej +       Ph       vh,i ⊗ kh,i qh,j
                                                   h                           h        i
                                                                               X              X
                                                                                                                T
                                                                      = ej +       Ph Wh,V         eh,i ⊗ eh,i Wh,K Wh,Q ej   (6)
                                                                               h               i

with ⊗ the outer P
                 product between two vectors. With this we can now easily draw connections to one step of gradient descent
              1    N               2
on L(W ) = 2N      i=1 ∥W xi − yi ∥ with learning rate η which yields weight change

                                                                        N
                                                                    η X
                                    ∆W = −η∇W L(W ) = −                   (W xi − yi )xTi .                                   (7)
                                                                    N i=1

We first restate
Proposition 1. Given a 1-head linear attention layer and the tokens ej = (xj , yj ), for j = 1, . . . , N , one can construct
key, query and value matrices WK , WQ , WV as well as the projection matrix P such that a Transformer step on every
token ej is identical to the gradient-induced dynamics ej ← (xj , yj ) + (0, −∆W xj ) = (xi , yi ) + P V K T qj such that
ej = (xj , yj − ∆yj ). For the test data token (xN +1 , yN +1 ) the dynamics are identical.
                                                                       
                                                                   Ix 0
We provide the weight matrices in block form: WK = WQ =                   with Ix and Iy the identity matrices of size Nx and
                                                                    0 0
                                                           
                                                 0       0
Ny respectively. Furthermore, we set WV =                      with the weight matrix W0 ∈ RNy ×Nx of the linear model we
                                                 W0 −Iy
wish to train and P = Nη I with identity matrix of size Nx + Ny . With this simple construction we obtain the following
dynamics
                           N                                                              
                    xj   x  η X     0                    0       xi     Ix         0   xi   Ix           0  xj
                       ← j + I                                      ⊗
                    yj   yj N       W0                  −Iy      yi      0         0   yi    0           0  yj
                                        i=1
                                  N                            
                             xj  η X        0         xi xj   xj     0
                          =     + I                 ⊗       =    +          .                                                 (8)
                             yj  N     W 0 xi − yi    0  0    yj   −∆W xj
                                           i=1


for every token ej = (xj , yj ) including the query token eN +1 = etest = (xtest , −W0 xtest ) which will give us the desired
result.

A.2. Comparing the out-of-distribution behavior of trained Transformers and GD
We provide more experimental results when comparing GD with tuned learning rate η and data transformation scalar γ and
the trained Transformer on other data distributions than provided during training, see Figure 6. We do so by changing the
in-context data distribution and measure the loss of both methods averaged over 10.000 tasks when either changing α that
1) affects the input data range x ∼ U (−α, α)Nx or 2) the teacher by αW with W ∼ N (0, I). This setups leads to results
shown in the main text, in the first two columns of Figure 6 and in the corresponding plots of Figure 7. Although the match
for deeper architectures starts to become worse, overall the trained Transformers behaves remarkably similar to GD and
GD++ for layer depth greater than 1.
Furthermore, we try GD and the trained Transformer on input distributions that it never has seen during training. Here, we
chose by chance of 1/3 either a normal, exponential or Laplace distribution (with JAX default parameters) and depict the
average loss value over 10.000 tasks where the α value now simply scales the input values that are sampled from one of
the distributions αx. The teacher scaling is identical to the one described above. See for results the two right columns of
Figure 6, where we see almost identical behavior for recurrent architectures with less good match for deeper non-recurrent

                                                               13


---

                                                             Transformers Learn In-Context by Gradient Descent

(a) Comparing one step of gradient descent with trained one layer Transformers on OOD data.
                      Test on larger inputs                        Test on larger targets                            Test on larger inputs                             Test on larger targets
                                                                                                               101                                               100
                       GD
                       Interpolated
                       Trained TF                                                                              100
          100                                                100
  Loss




                                                     Loss




                                                                                                                                                         Loss
                                                                                                       Loss
                                                                                                                                                                10 1
                                                                                  GD                          10 1                        GD                                          GD
                                                            10 1                  Interpolated                                            Interpolated                                Interpolated
         10 1                                                                     Trained TF                                              Trained TF                                  Trained TF
                                                                                                              10 2                                              10 2
                0.5       1.0         1.5      2.0                 1    2     3       4        5                     1       2        3       4      5                 1    2     3       4        5
                       where x        U( , )                       W where W         N(0, I)                                     where x                               W where W         N(0, I)
(b) Comparing two steps of gradient descent with trained recurrent two layer Transformers on OOD data.
                      Test on larger inputs                        Test on larger targets                            Test on larger inputs                             Test on larger targets
                       GD                                                                                                GD
          101          Interpolated                                                                            101       GD+ +
                       Trained TF                            100                                                         Interpolated
                                                                                                                         Trained TF                             10 1
                                                                                                               100
  Loss




                                                     Loss




                                                                                                                                                         Loss
          100




                                                                                                       Loss
                                                                                  GD                                                                                                  GD
                                                            10 1                  GD+ +                       10 1                                                                    GD+ +
         10 1                                                                     Interpolated                                                                  10 2                  Interpolated
                                                                                  Trained TF                  10 2                                                                    Trained TF
                                                            10 2
                0.5       1.0         1.5      2.0                 1    2     3       4        5                     1       2        3       4      5                 1    2     3       4        5
                       where x        U( , )                       W where W         N(0, I)                                     where x                               W where W         N(0, I)
(c) Comparing five steps of gradient descent with trained five layer Transformers on OOD data.
                      Test on larger inputs                        Test on larger targets                            Test on larger inputs                             Test on larger targets
                                                             101
                       GD                                                                                                GD                                      100
          101          GD+ +                                                                                   101       GD+ +
                       Trained TF                            100                                                         Trained TF
          100                                                                                                  100                                              10 1
  Loss




                                                     Loss




                                                                                                                                                         Loss
                                                                                                       Loss




                                                            10 1                                              10 1
         10 1                                                                                                                                                   10 2
                                                                                   GD                                                                                                  GD
                                                            10 2                   GD+ +                      10 2                                                                     GD+ +
         10 2                                                                      Trained TF                                                                   10 3                   Trained TF
                                                                                                              10 3
                0.5       1.0         1.5      2.0                 1    2     3       4        5                     1       2        3       4      5                 1    2     3       4        5
                       where x        U( , )                       W where W         N(0, I)                                     where x                               W where W         N(0, I)

Figure 6. Left & center left column: Comparing Transformers, GD and their weight interpolation on rescaled training distributions. In
all setups, the trained Transformer behaves remarkably similar to GD or GD++ . Right & center right: Comparing Transformers, GD
and their weight interpolation on data distributions never seen during training. Again, in all setups, the trained Transformer behaves
remarkably similar to GD or GD++ with less good match for deep non-recurrent Transformers far away from training regimes.

architectures far away from the training range of α = 1. Note that for deeper Transformers (K > 2) the corresponding
GD and GD++ version, see for more experimental details Appendix section A.12, we include a harsh clipping of the
token values after every step of transformation between [−10, 10] (for the trained TF and GD) to improve training stability.
Therefore, the loss increase is restricted to a certain value and plateaus.

A.3. Linear mode connectivity between the weight construction of Prop 1 and trained Transformers
In order to interpolate between the construction θGD and the trained weights of the Transformer θ, we need to correct for
some scaling ambiguity. For clarification, we restate here the linear self-attention operation for a single head
                                                            X
                                                                           T
                                          ej ←ej + P WV         ei ⊗ ei WK   WQ ej                                    (9)
                                                                                                   i
                                                                                                       X
                                                                            = ej + WP V                        ei ⊗ ei WKQ ej                                                                      (10)
                                                                                                         i

Now, to match the weight construction of Prop. 1 we have the aim for the matrix product WKQ to match an identify matrix
(except for the last diagonal entry) after re-scaling. Therefore we compute the mean of the diagonal of the matrix product
of the trained Transformer weights WKQ which we denote by β. After resealing both operations i.e. WKQ ← WKQ /β
and WP V ← WP V β we interpolate linearly between the matrix products of GD as well as these rescaled trained matrix
products i.e. WI,KQ = (WGD,KQ + WT F,KQ )/2 as well as WI,P V = (WGD,P V + WT F,P V )/2. We use these parameters
to obtain results throughout the paper denote with Interpolated. We do so for GD as well as GD++ when comparing to

                                                                                                   14


---

                                                               Transformers Learn In-Context by Gradient Descent




                 0.4
                                                                                     2.0
                                                                                                   GD vs trained TF                                                         GD+ + vs trained TF
                                                     GD                                                                                                           2.0
                                                     GD+ +                                                        Model cos 1.05                                                            Model cos 1.05
                 0.3                                 Trained TF                      1.5                                    1.00                                  1.5                                 1.00




                                                                                                                                       Cosine sim




                                                                                                                                                                                                             Cosine sim
                                                                           L2 Norm




                                                                                                                                                        L2 Norm
                                                                                                                      Preds diff 0.95                                                       Preds diff 0.95
          Loss




                 0.2                                                                 1.0                                                                          1.0
                                                                                                                      Model diff                                                            Model diff
                                                                                                                                 0.90                                                                  0.90
                 0.1                                                                 0.5                                                                          0.5
                                                                                                                                    0.85                                                                0.85
                                                                                     0.0                               0.80                                       0.0                          0.80
                        0         5000         10000           15000                           0        5000 10000 15000                                                0       5000 10000 15000
                                  Training steps                                                     Training steps                                                           Training steps
                      Test on larger inputs                            Test on larger targets                                   Test on larger inputs                                        Test on larger targets
                       GD                                                                                                           GD
          101          Interpolated                                                                                       101       GD+ +
                       Trained TF                              100                                                                  Interpolated
                                                                                                                                    Trained TF                                       10 1
                                                                                                                          100
  Loss




                                                       Loss




                                                                                                                                                                              Loss
          100

                                                                                                                  Loss
                                                                                               GD                                                                                                           GD
                                                              10 1                             GD+ +                     10 1                                                                               GD+ +
         10 1                                                                                  Interpolated                                                                          10 2                   Interpolated
                                                                                               Trained TF                10 2                                                                               Trained TF
                                                              10 2
                0.5         1.0       1.5      2.0                     1       2           3        4        5                  1       2           3             4     5                    1    2     3         4       5
                       where x        U( , )                           W where W                   N(0, I)                                  where x                                          W where W         N(0, I)

Figure 7. Comparing ten steps of gradient descent with trained recurrent ten-layer Transformers. Results comparable to recurrent
Transformer with two layers, see Figure 3, but now with 10 repeated layers. We again observe for deeper recurrent linear self-attention
only Transformers that overall GD++ and the trained Transformer align very well with one another and are again interpolatable leading
to very similar behavior insight as well as outside training situations. Note the inferior performance to the non-recurrent five-layer
Transformer which highlights the importance on specific learning rate as well γ parameter per layer/step.




Figure 8. Comparing twelve steps of GD++ with a trained twelve-layer Transformers with MLPs and 4 headed linear self-attention
layer. Results comparable to the deep recurrent Transformer, see Figure 7, but now with 12 independent Transformer blocks including
MLPs and 4-head linear self-attention. We omit LayerNorm. We again observe a close resemblance of the trained Transformers and
GD++ . We hypotheses that even when equipped with multiple heads and MLPs, Transformers approximate GD++ .




                                                                                                                 15


---

                                               Transformers Learn In-Context by Gradient Descent

                 Weights of WKTWV                      Weight of PWV                            Weights of WKTWV                       Weight of PWV
           1                            1.0     1                            1.0          1                                     1
           2                                    2                                         2                                     2
           3                            0.5     3                            0.5          3                            1        3                            1
           4                                    4                                         4                                     4
           5                                    5                                         5                                     5
           6                            0.0     6                            0.0          6                            0        6                            0
           7                                    7                                         7                                     7
           8                             0.5    8                             0.5         8                                     8
           9                                    9                                         9                                1    9                                1
          10                                   10                                        10                                    10
          11                             1.0   11                             1.0        11                                    11
               1 2 3 4 5 6 7 8 9 1011               1 2 3 4 5 6 7 8 9 1011                    1 2 3 4 5 6 7 8 9 1011                1 2 3 4 5 6 7 8 9 1011

Figure 9. Visualizing the weight matrices of trained Transformers. Left & outer left: Weight matrix products of a trained single linear
self-attention layer. We see (after scalar correction) a perfect resemblance of our construction. Right & outer right: Weight matrix
products of a trained 3-layer recurrent linear self-attention Transformer. Again, we see (after scalar correction) a perfect resemblance of
our construction and an additional curvature correction i.e. diagonal values in P WV of the same magnitude except the last entry that
functions as the learning rate.

recurrent Transformers. Note that for non-recurrent Transformers, we face more ambiguity that we have to correct for
since e.g. scalings influence each other across layer. We also see this in practice and are not able (only for some seeds) to
interpolate between weights with our simple correction from above. We leave the search for more elaborate corrections for
future work.

A.4. Visualizing the trained Transformer weights
The simplicity of our construction enables us to visually compare trained Transformers and the construction put forward
in Proposition A.1 in weight space. As discussed in the previous section A.3 there is redundancy in the way the trained
Transformer can construct the matrix products leading to the weights corresponding to gradient descent. We therefore
                     T
visualize WKQ = WK     WQ as well as WP V = PK WV in Figure 9.

A.5. Proof and discussion of Proposition 3
We state here again Proposition 3, provide the necessary construction and a short discussion.
Proposition 3. Given a 1-head linear- or softmax attention layer and the token construction e2j = (xj ), e2j+1 = (0, yj )
with a zero vector 0 of dim Nx − Ny and concatenated positional encodings, one can construct key, query and value matrix
WK , WQ , WV as well as the projection matrix P such that all tokens ej are transformed into tokens equivalent to the ones
required in proposition 1.

To get a simple and clean construction, we choose wlog xj ∈ R2N +1 and (0, yj ) ∈ R2N +1 as well as model the positional
encodings as unit vectors pj ∈ R2N +1 and concatenate them to the tokens i.e. ej = (xj/2 , pj ). We wish for a construction
that realizes
                                                                          
                                                 x                      xj/2
                                          ej ← j/2 + P V K T WQ                                                        (11)
                                                  pj                     pj
                                                                        
                                                    xj/2            0
                                               =          +                   .                                        (12)
                                                     pj       yj/2+1 − pj
This means that a token replaces its own positional encoding by coping the target data of the next token to itself leading
to ej = (xj/2 , 0, yj/2+1 ), with slight abusive of notation. This can simply be realized by (for example) setting P = I,
                                                                 
          0        0                  0 0                   0     0
WV =                      , WK =              and WQ =          T       with Ix,of f the lower diagonal identity matrix fo size
         Ix −Ix,of f                  0 Ix                  0 Ix,of f
Nx . Note that then simply K T WQ ej = pj+1 i.e. it chooses the j + 1 element of V which stays pj+1 if we apply the
softmax operation on K T qj . Since the j + 1 entry of V is (0, yj/2+1 − pj ) we obtain the desired result.
For the (toy-)regression problems considered in this manuscript, the provided result would give N/2 tokens for which we
also copy (parts) of xj underneath yj . This is desired for modalities such as language where every two tokens could be
considered an in-and output pair for the implicit autoregressive inner-loop loss. These tokens do not have be necessarily next
to each other, see for this behavior experimental findings presented in (Olsson et al., 2022). For the experiments conducted
here, one solution is to zero out these tokens which could be constructed by a two-head self-attention layer that given uneven
j simply subtracts itself resulting in a zero token. For all even tokens, we use the construction from above which effectively
coincides with the token construction required in Proposition 1.

                                                                                    16


---

                                               Transformers Learn In-Context by Gradient Descent

Rolling out experiment with different dampening strength
                         Dampening = 1                                 Dampening = 0.875                               Dampening = 0.75
                                        GD                                              GD                                           GD
             0.2                        Trained TF           0.2                        Trained TF           0.2                     Trained TF
      Loss




                                                      Loss




                                                                                                      Loss
             0.1                                             0.1                                             0.1
             0.0                                             0.0                                             0.0
                   0    10   20    30     40     50                0    10   20    30     40     50                0          20        40
                   GD Steps / Transformer Layers                   GD Steps / Transformer Layers                   GD Steps / Transformer Layers
Figure 10. Roll-out experiments: applying a trained single linear self-attention layer multiple times. We observe that different
dampening strengths affect the generalization of both methods with slightly better robustness for GD which matching performance for 50
steps when λ = 0.75.


A.6. Dampening the self-attention layer
As an additional out-of-distribution experiment, we test the behavior when repeating a single LSA-layer trained to lower
our objective, see equation 5, with the aim to repeat the learned learning/update rule. Note that GD as well as the self-
attention layer were optimized to be optimal for one step. For GD we line search the otpimal learning rate η on 10.000
task. Interestingly, for both methods we observe quick divergence when applied multiple times, see left plot of Figure
10. Nevertheless, both of our update functions are described by a linear self-attention layer for which we can control the
norm, post training, by a simple scale which we denote as λ. This results in the new update ytest + λ∆W xtest for GD
and ytest + λP V K T WQ xtest for the trained self-attention layer which effectively re-tunes the learning rate for GD and the
trained self-attention layer. Intriguingly, both methods do generalize similarly well (or poorly) on this out-of-distribution
experiment when changing λ, see again Figure 10. We show in Figure 1 the behavior for λ = 0.75 for which we see both
methods steadily decreasing the loss within 50 steps.

A.7. Sine wave regression
For the sine wave regression tasks, we follow (Finn et al., 2017) and other meta-learning literature and sample for each
task an amplitude a ∼ U (0.1, 5) and a phase ρ ∼ U (0, π). Each tasks consist of N = 10 data points where inputs are
sampled x ∼ U (−5, 5) and targets computed by y = a sin(ρ + x). We choose here for the first time, for GD as well as for
the Transformer, an input embedding emb that maps tokens ei = (xi , yi ) into a 40 dimensional space emb(ei ) = Wemb ei
through an affine projection without bias. We skip the first self-attention layer but, as usually done in Transformers, then
transform the embedded tokens through an MLP m with a single hidden layer, widening factor of 4 (160 hidden neuros) and
GELU nonlinearity (Hendrycks & Gimpel, 2016) i.e. ej ← m(emb(ej )) + emb(ej ).
We interpret the last entry of the transformed tokens as the (transformed) targets and the rest as a higher-dimensional input
data representation on which we train a model with a single gradient descent step. We compare the obtained meta-learned
GD solution with training a Transformer on the same token embeddings but instead learn a self-attention layer. Note that the
embeddings of the tokens, including the transformation through the MLP, are not dependent on an interplay between the
tokens. Furthermore, the initial transformation is dependent on ei = (xi , yi ), i.e., input as well as on the target data except
for the query token for which ytest = 0. This means that this construction is, except for the additional dependency on targets,
close to a large corpus of meta-learning literature that aims to find a deep representation optimized for (fast) fine tuning
and few-shot learning. In order to compare the meta-training of the MLP and the Transformer, we choose the same seed
to initialize the network weights for the MLPs and the input embedding trained by meta-learning i.e. backprop through
training or the Transformer. This leads to the plots and almost identical learned initial function and updated functions shown
in Figure 4.

A.8. Proposition 2 and connections between gradient descent, kernelized regression and kernel smoothing
Let’s consider the data transformation induced by an MLP m̃(x) and a residual connection commonly used in Transformer
blocks i.e. ej ← ej + m̃(ej ) = (xj , yj ) + (m̃(xj ), 0) = (m(xj ), yj ) with m(xj ) = xj + m̃(xj ) and m̃ not changing the
targets y. When simply applying Proposition 1, it is easy to see that given this new token construction, a linear self-attention
layer can induce the token dynamics ej ← (m(xj ), yj ) + (0, −∆W m(xj )) with ∆W = −η∇L(W ) given the loss function
            1
              PN                       2
L(W ) = 2N       i=1 ||W m(xi ) − yi || .


                                                                             17


---

                                       Transformers Learn In-Context by Gradient Descent

Interestingly, for the test token etest = (xtest , 0) this induces, after a multiplication with −1, an initial prediction after a single
Transformer block given by
                                                                           N
                                                                           X                              N
                                                                                                          X
                   ŷ = ∆W m(xtest ) = −η∇W L(0)m(xtest ) =                      yi m(xi )T m(xtest ) =         yi k(xi , xtest )   (13)
                                                                           i=1                            i=1

with m(xi )T m(xtest ) = k(xi , xtest ) ∈ R interpreted as a kernel function. Concluding, we see that the combination of MLPs
and a single self-attention layer can lead to dynamics induced when descending a kernelized regression (squared error) loss
with a single step of gradient-descent.
Interestingly, when choosing W0 = 0, we furthermore see   PNthat a single self-attention layer or Transformer block can be
regarded as doing nonparametric kernel smoothing ŷ = i=1 yi k(xi , xtest ) based on the data given in-context (Nadaraya,
1964; Watson, 1964). Note that we made a particular choice of kernel function here and that this view still holds when
m(xj ) = 1 i.e. consider Transformers without MLPs or leverage the well-known view of softmax self-attention layer as
a kernel function used to measure similarity between tokens (e.g. Choromanski et al., 2021; Zhang et al., 2021). Thus,
implementing one step of gradient descent through a self-attention layer (w/wo softmax nonlinearity) is equivalent to
performing kernel smoothing estimation. We however argue that this nonparametric kernel smoothing view of in-context
learning is limited, and arises from looking only at a single self-attention layer. When considering deeper Transformer
architectures, we see that multiple Transformer blocks can iteratively transform the targets based on multiple steps of
gradient descent leading to minimization of a kernelized squared error loss L(W ). One way to obtain a suitable construction
is by neglecting MLPs everywhere except in the first Transformer block. We leave the study of the exact mechanics,
especially how the Transformer makes use of possibility transforming the targets through the MLPs, and the possibility of
iteratively changing the kernel function throughout depth for future study.

A.9. Linear vs. softmax self-attention as well LayerNorm Transformers
Although linear Transformers and their variants have been shown to be competitive with their softmax counterpart (Irie
et al., 2021), the removal of this nonlinearity is still a major departure from classic Transformers and more importantly from
the Transformers used in related studies analyzing in-context learning. In this section we investigate whether and when
gradient-based learning emerges in trained softmax self-attention layers, and we provide an analytical argument to back our
findings.
First, we show, see Figure 12, that a single layer of softmax self-attention is not able to match GD performance. We tuned
the learning rate as well as the weight initialization but found no significant difference over the hyperparameters we used
througout this study. In general, we hypothesize that GD is an optimal update given the limited capacity of a single layer of
(single-head) self-attention. We therefore argue that the softmax induces (at best) a linear offset of the matrix product of
training data and query vector
                                            T               T         X T
                     softmax(K T qj ) = (ek1 qj , . . . , ekN qj )T /( eki qj )                                          (14)
                                                                           i
                                               xT                   xT
                                                                                     X T
                                        = (e    1 WKQ xj   ,...,e    N WKQ xj T  ) /( exi WKQ xj )                                  (15)
                                                                                        i
                                                                                                 X
                                        ≈ (1 + xT1 WKQ xj , . . . , 1 + xTN WKQ xj )T /(              1 + xTi WKQ xj )              (16)
                                                                                                  i
                                        ∝ K T qj + ϵ                                                                                (17)

proportional to a factor dependent on all {xτ,i }N   +1
                                                   i=1 . We speculate that the dependency on the specific task τ , for large
Nx vanishes or that the x-dependent value matrix could introduce a correcting effect. In this case the softmax operation
introduces an additive error w.r.t. to the optimal GD update. To overcome this disadvantageous offset, the Transformer can
(approximately) introduce a correction with a second self-attention head by a simple subtraction i.e.
              P1 V1 softmax(K1T WQ xj ) + P2 V2 softmax(K2T WQ xj )                                                                 (18)
              ≈ P V ((1 + xT1 W1,KQ xj , . . . , 1 + xTN W1,KQ xj ) − (1 + xT1 W2,KQ xj , . . . , 1 + xTN W2,KQ xj ))               (19)
              = P V (xT1 (W1,KQ − W2,KQ )xj , . . . , xTN (W1,KQ − W2,KQ )xj )                                                      (20)
                        T
              ∝ P V K qj .                                                                                                          (21)

                                                                      18


---

                                         Transformers Learn In-Context by Gradient Descent

                             1W1, KQ                               2W2, KQ                            1W1, KQ + 2W2, KQ
                 1                            4        1                            4           1                            4
                 2                                     2                                        2
                 3                                     3                                        3
                 4                            2        4                            2           4                            2
                 5                                     5                                        5
                 6                            0        6                            0           6                            0
                 7                                     7                                        7
                 8                                2    8                                2       8                                2
                 9                                     9                                        9
                10                                4   10                                4      10                                4
                11                                    11                                       11
                     1 2 3 4 5 6 7 8 9 1011                1 2 3 4 5 6 7 8 9 1011                   1 2 3 4 5 6 7 8 9 1011

Figure 11. Visualizing the correction to the softmax operation when training Transformers on regression tasks. The left and center
                                           T
plot show the matrix product WKQ = WK        WQ including its scaling by η induced through P WV of the two heads of the trained softmax
self-attention layer. We observe that both of the matrices are approximate diagonal almost perfect sign reversed values on the off-diagonal
terms. After adding the matrices (right plot), we observe a diagonal matrix and therefore to much improved approximation of our
construction and therefore gradient descent dynamics.




Here we assume that P V 1) subsumes the dividing factor of the softmax and that 2) is the same (up to scaling) for each
head. Note that if (W1,KQ − W2,KQ ) is diagonal, and P and V chosen as in the Proposition of Appendix A.1, we recover
our gradient descent construction.
We base this derivation on empirical findings, see Figure 12, that, first of all, show the softmax self-attention performance
increases drastically when using two heads instead of one. Nevertheless, the self-attention layer has difficulties to match the
loss values of a model trained with GD. Furthermore, this architecture change leads to a very much improved alignment
of the trained model and GD. Second, we can observe that when training a two-headed softmax self-attention layer on
regression tasks the correction proposed above is actually observed in weight space, see Figure 11. Here, we visualize
the matrix product within the softmax operation Wh,KQ per head which we scale with the last diagonal entry of Ph Wh,V
which we denote by ηh = Ph Wh,V (−1, −1). Intriguingly, this results in an almost perfect cancellation (right plot) of the
off-diagonal terms and therefore in sum to an improved approximation of our construction, see the derivation above.
We would like to reiterate that the stronger inductive bias for copying data of the softmax layer remains, and is not invalidated
by the analysis above. Therefore, even for our shallow and simple constructions they indeed fulfill an important role in
support for our hypotheses: The ability to merge or copy input and target data into single tokens allowing for their dot
product computation necessary for the construction in Proposition 1, see Section 4 in the main text.
We end this section by analysing Transformers equipped with LayerNorm which we apply as usually done before the
self-attention layer: Overall, we observe qualitatively similar results to Transformers with softmax self-attention layer i.e.
a decrease in performance compared to GD accompanied with a decrease in alignment between models generated by the
Transformer and models trained with GD, see Figure 14. Here, we test again a single linear self-attention layer succeeding
LayerNorm as well as two layers where we skip the first LayerNorm and only include a LayerNorm between the two.
Including more heads does not help substantially. We again assume the optimality of GD and argue that information of
targets and inputs present in the tokens is lost by averaging when applying LayerNorm. This naturally leads to decreasing
performance compared to GD, see first row of Figure 14. Although the alignment to GD and GD++ , especially for two
layers, is high, we overall see inferior performance to one or two steps of GD or two steps of GD++ . Nevertheless, we
speculate that LayerNorm might not only stabilize Transformer training but could also act as some form of data normalization
procedure that implicitly enables better generalization for larger inputs as well as targets provided in-context, see OOD
experiments in Figure 14.
Overall we conclude that common architecture choices like softmax and LayerNorm seem supoptimal for the constructed
in-context learning settings when comparing to GD or linear self-attention. Nevertheless, we speculate that the potentially
small performance drops of in-context learning are negligible when turning to deep and wide Transformers for which these
architecture choices have empirically proven to be superior.

                                                                    19


---

                                                            Transformers Learn In-Context by Gradient Descent

(a) Comparing one step of GD with a trained softmax one-headed self-attention layer.
         0.40                                         3.5                                                                               Test on larger inputs                 101
                                                                                                                                                                                    Test on larger targets
                               GD                               Preds diff            Model cos
                               Trained TF             3.0       Model diff                        1.0                                    GD
         0.35                                         2.5                                                                                Trained TF
                                                                                                  0.8




                                                                                                   Cosine sim
                                            L2 Norm
                                                      2.0                                                                   100                                               100
  Loss




         0.30                                                                                     0.6




                                                                                                                    Loss




                                                                                                                                                                      Loss
                                                      1.5
                                                      1.0                                         0.4
         0.25
                                                      0.5                                         0.2                                                                        10 1                  GD
                                                                                                                           10 1                                                                    Trained TF
         0.20                                         0.0                               0.0
                0      2000      4000                       0   1000 2000 3000 4000 5000                                          0.5       1.0       1.5       2.0                 1    2     3     4        5
                     Training steps                                  Training steps                                                      where x      U( , )                        W where W       N(0, I)
(b) Comparing one step of GD with a trained softmax two-headed self-attention layer.
         0.40                                         3.5                                                                               Test on larger inputs                       Test on larger targets
                               GD                               Preds diff            Model cos
                               Trained TF             3.0       Model diff                        1.0                                    GD
         0.35                                         2.5                                                                                Trained TF
                                                                                                  0.8




                                                                                                   Cosine sim
                                                                                                                                                                              100
                                            L2 Norm




                                                      2.0                                                                   100
  Loss




         0.30                                                                                     0.6




                                                                                                                    Loss




                                                                                                                                                                      Loss
                                                      1.5
                                                      1.0                                         0.4
         0.25
                                                      0.5                                         0.2                                                                        10 1                  GD
                                                                                                                           10 1                                                                    Trained TF
         0.20                                         0.0                                0.0
                0   2500 5000 7500 10000                    0   2000 4000 6000 8000 10000                                         0.5       1.0       1.5       2.0                 1    2     3     4        5
                     Training steps                                  Training steps                                                      where x      U( , )                        W where W       N(0, I)

Figure 12. Comparing trained two-headed and one-headed single-layer softmax self-attention with 1 step of gradient descent on
linear regression tasks. Left column: Softmax self-attention is not able to match gradient descent performance with hand-tuned learning
rate, but adding a second attention head significantly reduces the gap, as expected by our analytical argument. Center left: The alignment
suffers significantly for single-head softmax SA. We observe good but not as precise alignment when compared to linear Transformers for
the two-headed softmax SA layer. Center right & right: The two-headed self-attention compared to the single-head layer shows similar
robust out-of-distribution behavior compared to gradient descent.

A.10. Details of curvature correction
We give here a precise construction showing how to implement in a single head, a step of GD and the discussed data
transformation, resulting in GD++ . Recall again the linear self-attention operation with a single head
                                                              X
                                                                             T
                                            ej ←ej + P WV          ei ⊗ ei WK  .                              (22)
                                                                                                                i

We provide again the weight matrices in block form
                                                  of   the construction of Prop. 1 but now enabling additionally our
                                                   Ix 0
described data transformation: WK = WQ =                   with Ix the identity matrix of size Nx , Iy od size Ny resp.
                                                    0 0
                                       
                             Ix     0
Furthermore, we set WV =                  with the weight matrix W ∈ RNy ×Nx of the linear model we wish to train and
                           W    −I  y
       −γIx 0
P =            η . This leads to the following update
         0     N


                                                                   N 
                                                                       X                                                                                                  
                     xj   x   −γIx                                 0                   Ix          0         xi     Ix                                 0   xi   Ix                  0  xj
                        ← j +                                     η                                             ⊗
                     yj   yj   0                                  N                    W          −Iy        yi      0                                 0   yi    0                  0  yj
                                                                             i=1
                                                                              N 
                                                                                                                                           −γXX T xj
                                                                          X                                                              
                                    xj   −γIx                           0                   xi                                xi xj   xj
                                 =     +                               η                                              ⊗             =    +             .                                                      (23)
                                    yj    0                            N                 W xi − yi                            0  0    yj    −∆W xj
                                                                               i=1

for every token ej = (xj , yj ) including the query token eN +1 = etest = (xtest , 0) which will give us the desired result.
Why does GD++ perform better? We give here one possible explanation of the superior performance of GD++ compared
to GD. Note that there is a close resemblance of the GD transformation and a heavily truncated Neuman series approximation
of the inverse XX T . We provide here a more heuristic explanation for the observed acceleration.
Given γ ∈ R, GD++ transforms every input according to xi ← xi − γXX T xi = (I − γXX T )xi . We can therefore look
                                                   PN
at the change of squared regression loss L(W ) = 21 i=0 (W xi − yi )2 induced by this transformation i.e. L++ (W ) =

                                                                                                    20


---

                                        Transformers Learn In-Context by Gradient Descent




Figure 13. GD++ analyses. Left: We visualize the change of the eigenspectrum induced by the input data transformation of GD++ for
different γ observed in practice. Center: Given we know the maximum and minimum of eigenvalues λ1 , λn of the loss Hessian XX T
with X = (x0 , . . . , xN ) for different N , we compare the original condition number (depicted by *’s at γ = 0) and the condition number
(in log scale) of the GD++ altered loss Hessian when varying γ. We plot in dotted lines the γ values that we observe in practice which
are close the optimal ones i.e. the local minimum derived through our analysis. Right: ForN = 25, we plot for different γ values the
distribution of condition numbers κ = λ1 /λn for 10000 tasks and observe favorable κ values close to 1 when approaching the γ = 0.099
value was found in practice. The κ values quickly explode for γ > 0.1.
1
    PN                  T         2  1            T        2
2       i=0 (W (I − γXX )xi − yi ) = 2 (W (I − γXX )X − Y ) which in turn leads to a change of the loss Hessian from
    2           T     2 ++              T           T    T
∇ L = XX to ∇ L              = (I − γXX )X((I − γXX )X) .
Given the original Hessian H = XX T = U ΣU T with it’s set of sorted eigenvalues {λ1 , . . . , λn } and λi ≥ 0 on the
diagonal matrix Σ we can express the new Hessian through U, Σ i.e. H ++ = (I − γXX T )X((I − γXX T )X)T =
(I − γU ΣU T )U ΣU T (I − γU ΣU T )T .
We can simplify H ++ further as

                      H ++ = (I − γU ΣU T )U ΣU T (I − γU ΣU T )T = U (Σ − γΣ2 )U T U (I − γΣ)U T                                    (24)
                                              2     2   3   T
                             = U (Σ − 2γΣ + γ Σ )U                                                                                   (25)

Given the eigenspectrum {λ1 , . . . , λn } of H, we obtain an (unsorted) eigenspecturm for H ++ with {λ1 − 2γλ21 +
γ 2 λ31 , . . . , λn − 2γλ2n + γ 2 λ3n } which we visualize in Figure 13 for different γ observed in practice. We hypotheses
that the Transformer chooses γ in a way that on average, across the distribution of tasks, the data transformation (iteratively)
decreases the condition number λ1 /λn leading to accelerated learning. This could be achieved, for example, by keeping
                                                                                                                          ++
the smallest eigenvalue λn ≈ λ++        n fixed and choosing γ such that the largest eigenvalue of the transformed data λ1    is
                                                   ++    ++
reduced, while the original λ1 stays within [λ1 , λn ].
To support our hypotheses empirically, we computed the minimum and maximum eigenvalues of XX T across 10000 tasks
while changing the number of datapoints N ∈ [10, 25, 50, 100] i.e. X = (x0 , . . . , xN ) leading to better conditioned loss
Hessians i.e. [1e−10, 0.097, 0.666, 2.870] and [4.6, 7.712, 10.845, 17.196] as the minimum and maximum eigenvalues of
XX T across all tasks where we cut the smallest eigenvalue for N = 10 at 1e−10. Furthermore, we extract the γ values
from the weights of optimized recurrent 2-layer Transformers trained on different task distributions and obtain γ values of
[0.179, 0.099, 0.056, 0.029], see again Figure 13. Note that the observed eigenvalues stay within [0, 1/γ] i.e. the two roots
of f (λ, γ) = λ − 2γλ2 + γ 2 λ3 .
Given the derived function of eigenvalue change f (λ, γ), we compute the condition number of H ++ by dividing the novel
maximum eigenvalues λ++   1  = f (1/(3γ), γ) where λ = 1/(3γ) as the local maximum of f (λ, γ), for fixed γ, and the novel
minimum eigenvalue λ++   n   = min(f (λ1 , γ), f (λn , γ)). Note that with too small γ, we move the original λn closer to the
root of f (λ, γ) i.e. λ = 1/γ and therefore can change the smallest eigenvalue.
Given the task distribution and its corresponding eigenvalue distribution, we see that choosing γ reduces the new condition
number κ++ = λ++         ++
                  1 /λn which leads to better conditioned learning, see center plot of Figure 13. Note that the optimal γ
based on our derivation above is based on the maximum and minimum eigenvalue across all tasks and does not take the
change of the eigenvalue distribution into account. We argue therefore that the simplicity of the arguments above does
not capture the task statistics and distribution shifts entirely and therefore obtains a slightly larger γ as an optimal value.

                                                                   21


---

                                                                 Transformers Learn In-Context by Gradient Descent

(a) Comparing one step of GD with a single-layer LSA Transformer with LayerNorm.
         0.40                                             3.5
                                                                                                                                                 101
                                                                                                                                                             Test on larger inputs                                 Test on larger targets
                               GD                                         Preds diff            Model cos                                                                                               101
                               Trained TF                 3.0             Model diff                             1.0                                          GD
         0.35                                             2.5                                                                                                 Trained TF
                                                                                                                 0.8




                                                                                                                         Cosine sim
                                                L2 Norm
                                                          2.0                                                                                                                                           100
                                                                                                                                                 100
  Loss




         0.30                                                                                                    0.6




                                                                                                                                      Loss




                                                                                                                                                                                                Loss
                                                          1.5
                                                          1.0                                                    0.4
         0.25
                                                          0.5                                                    0.2                                                                                   10 1                               GD
                                                                                                                                                10 1                                                                                      Trained TF
         0.20                                             0.0                                              0.0
                0   5000     10000     15000                    0             5000      10000         15000                                            0.5       1.0       1.5          2.0                        1       2        3          4         5
                    Training steps                                             Training steps                                                                 where x      U( , )                                  W where W                  N(0, I)
(b) Comparing two steps of GD with a two-layer LSA Transformer with LayerNorm.
         0.30                                                               GD vs trained TF                                                         GD+ + vs trained TF                                           Test on larger inputs
                                 GD
                                 GD+ +                                                  Model cos                                                                  Model cos 1.0                       103             GD
         0.25                    Trained TF                     1.5                             1.0                                       1.5                                                                          GD+ +
                                                                                                0.9                                                                              0.9                   102             Trained TF




                                                                                                            Cosine sim




                                                                                                                                                                                  Cosine sim
                                                      L2 Norm




                                                                                                                                L2 Norm
                                                                1.0                  Preds diff                                           1.0                      Preds diff 0.8
  Loss




         0.20




                                                                                                                                                                                               Loss
                                                                                     Model diff 0.8                                                                Model diff                          101
                                                                                                0.7                                                                           0.7                      100
         0.15                                                   0.5                                                                       0.5
                                                                                                0.6                                                                              0.6
                                                                                                                                                                                                      10 1
         0.10                                                   0.0                             0.5                                       0.0                           0.5
                0     5000     10000        15000                     0        5000 10000 15000                                                  0       5000 10000 15000                                    0.5         1.0            1.5             2.0
                     Training steps                                           Training steps                                                            Training steps                                                 where x          U( , )

Figure 14. Comparing trained 1-layer and 2-layer Transformers with LayerNorm and 1 step or 2 steps of gradient descent resp.
Left column: The Transformers is not able to match the gradient descent performance with hand-tuned learning rate. Alignment
plots: The alignment suffers significantly when comparing to linear self-attention layers although still reasonable alignment is obtained
which decreases slightly when comparing to GD++ for the two-layer Transformer.Center right & right: The LayerNorm Transformer
outperforms when GD when providing training input data that is significantly larger than the data provided during training.

We furthermore visualize the condition number change for N = 25 and 10000 tasks in the right plot of Figure 13 and
observe the distribution moving to desirable κ values close to 1. For γ values larger than 0.1 the distribution quickly exhibits
exploding condition numbers.

A.11. Phase transitions
We comment shorty on the curiously looking phase transitions of the training loss observed in many of our experiments,
see Figure 2. Nevertheless, simply switching from a single-headed self-attention layer to a two-headed self-attention layer
mitigates the random seed dependent training instabilities in our experiments presented in the main text, see left and center
plot of Figure 15.
Furthermore, these transitions look reminiscent of the recently observed ”grokking” behaviour (Power et al., 2022).
Interestingly, when carefully tuning the learning rate and batchsize we can also make the Transformers trained in these linear
regression tasks grokk. For this, we train a single Transformer block (self-attention layer and MLP) on a limited amount of
data (8192 tasks), see right plot of Figure 15, and observe grokking like train and test loss phase transitions where test set
first increases drastically before experiencing a sudden drop in loss almost matching the desired GD loss of 0.2. We leave a
thorough investigation of these phenomena for future study.

A.12. Experimental details
We use for most experiments identical hyperparameters that were tuned by hand which we list here

   • Optimizer: Adam (Kingma & Ba, 2014) with default parameters and learning rate of 0.001 for Transformer with depth
     K < 3 and 0.0005 otherwise. We use a batchsize of 2048 and applied gradient clipping to obtain gradients with global
     norm of 10. We used the Optax library.

   • Haiku weight initialisation (fan-in) with truncated normal and std 0.002/K where K the number of layers.

   • We did not use any regularisation and observed for deeper Transformers with K > 2 instabilities when reaching GD
     performance. We speculate that this occurs since the GD performance is, for the given training tasks, already close
     to divergence as seen when providing tasks with larger input ranges. Therefore, training Transformers also becomes

                                                                                                                         22


---

                                        Transformers Learn In-Context by Gradient Descent




Figure 15. Phase transitions during training. Left: Loss based on 10 different random seeds when optimizing a single-headed self-
attention layer. We observe for some seeds very long initial phases of virtually zero progress after which the loss drops suddenly to the
desired GD loss. Center: The same experiment but optimizing a two-headed self-attention layer. We observe fast and robust convergence
to the loss of GD. Right: Training a single Transformer block i.e. a self-attention layer with MLP and a reduced training set size of 8192
tasks. We observe grokking like train and test loss phase transitions where test set first increases drastically before experiencing a sudden
drop in loss almost matching the desired GD loss of 0.2.

     instable when we approach GD with an optimal learning rate. In order to stabilize training, we simply clipped the token
     values to be in the range of [−10, 10].
   • When applicable we use standard positional encodings of size 20 which we concatenated to all tokens.
   • For simplicity, and to follow the provided weight construction closely, we did use square key, value and query parameter
     matrix in all experiments.

   • The training length varied throughout our experimental setups and can be read off our training plots in the article.
   • When training meta-parameters for gradient descent i.e. η and γ we used an identical training setup but usually training
     required much less iterations.
   • In all experiments we choose inital W0 = 0 for gradient descent trained models.

Inspired by (Garg et al., 2022), we additionally provide results when training a single linear self-attention layer on a fixed
number of training tasks. Therefore, we iterate over a single fixed batch of size B instead of drawing new batch of tasks at
every iteration. Results can be found in Figure 16. Intriguingly, we find that (meta-)gradient descent finds Transformer
weights that align remarkable well with the provided construction and therefore gradient descent even when provided with an
arguably very small number of training tasks. We argue that this again highlights the strong inductive bias of the LSA-layer
to match (approximately) gradient descent learning in its forward pass.




                                                                    23


---

                                                                 Transformers Learn In-Context by Gradient Descent




(a) Comparing 1 step of gradient descent with training a LSA-layer on 128 tasks.
         5                                                                                                                              Test on larger inputs                       Test on larger targets
                                    GD                     10
                                    Trained TF                                             Model cos                                     GD
         4                                                                                             1.0                               Interpolated
                                                            8
                                                                                                      0.8                                Trained TF
         3




                                                                                                        Cosine sim
                                                 L2 Norm    6                              Preds diff 0.6
  Loss




                                                                                                                     Loss




                                                                                                                                                                       Loss
                                                                                           Model diff
         2                                                  4
                                                                                                      0.4
                                                            2
                                                                                                                                                                                                    GD
                                                                                                       0.2                                                                                          Interpolated
         1
                                                            0                                 0.0                           0.1                                               0.1                   Trained TF
                                                                 0    1000 2000 3000 4000 5000
             0       1000 2000 3000 4000 5000                            Training steps                                           0.5       1.0         1.5      2.0                1    2      3       4       5
                        Training steps                                                                                                    where x       U( , )                      W where W         N(0, I)
(b) Comparing 1 step of gradient descent with training a LSA-layer on 512 tasks.
         0.40                                                                                                                           Test on larger inputs                       Test on larger targets
                                    GD                     3.5
                                    Trained TF                                             Model cos                                     GD
         0.35                                              3.0                                         1.0                               Interpolated
                                                           2.5                                        0.8                                Trained TF
                                                                                                        Cosine sim
                                                 L2 Norm




                                                           2.0                             Preds diff 0.6
  Loss




         0.30                                                                                                        Loss




                                                                                                                                                                       Loss
                                                           1.5                             Model diff
                                                           1.0                                        0.4
         0.25                                                                                                                                                                                       GD
                                                           0.5                                         0.2                                                                                          Interpolated
                                                                                                                                                                              0.1                   Trained TF
                                                           0.0
                                                                  0   1000 2000 3000 4000 5000
                                                                                              0.0                           0.1
         0.20                                                             Training steps
                 0         2000          4000                                                                                     0.5       1.0         1.5      2.0                1    2      3       4       5
                         Training steps                                                                                                   where x       U( , )                      W where W         N(0, I)
(c) Comparing 1 step of gradient descent with training a LSA-layer on 2048 tasks.
         0.40                                                                                                                           Test on larger inputs                       Test on larger targets
                                    GD                     3.5
                                    Trained TF                                             Model cos                                     GD
         0.35                                              3.0                                         1.0                               Interpolated
                                                           2.5                                        0.8                                Trained TF
                                                                                                        Cosine sim
                                                 L2 Norm




                                                           2.0                             Preds diff 0.6
  Loss




         0.30
                                                                                                                     Loss




                                                                                           Model diff                                                                  Loss
                                                           1.5
                                                           1.0                                        0.4
         0.25                                                                                                                                                                                       GD
                                                           0.5                                         0.2                                                                                          Interpolated
                                                                                                                                                                              0.1
                                                           0.0                                0.0                           0.1                                                                     Trained TF
         0.20                                                     0   1000 2000 3000 4000 5000
                 0         2000          4000                             Training steps                                          0.5       1.0         1.5      2.0                1    2      3       4       5
                         Training steps                                                                                                   where x       U( , )                      W where W         N(0, I)
(d) Comparing 1 step of gradient descent training a LSA-layer on 8192 tasks.
         0.40                                                                                                                           Test on larger inputs                       Test on larger targets
                                    GD                     3.5
                                    Trained TF                                             Model cos                                     GD
         0.35                                              3.0                                         1.0                               Interpolated
                                                           2.5                                        0.8                                Trained TF
                                                                                                        Cosine sim
                                                 L2 Norm




                                                           2.0                             Preds diff 0.6
  Loss




         0.30
                                                                                                                     Loss




                                                                                                                                                                       Loss




                                                           1.5                             Model diff
                                                           1.0                                        0.4
         0.25                                                                                                                                                                                       GD
                                                           0.5                                         0.2                                                                                          Interpolated
                                                                                                                                                                              0.1
                                                           0.0                                0.0                           0.1                                                                     Trained TF
         0.20                                                     0   1000 2000 3000 4000 5000
                 0         2000          4000                             Training steps                                          0.5       1.0         1.5      2.0                1    2      3       4       5
                         Training steps                                                                                                   where x       U( , )                      W where W         N(0, I)

Figure 16. Comparing trained Transformers with GD and their weight interpolation when training the Transformer on a fixed
training set size B. Across our alignment measures as well as our tests on out-of-training behaviour, trained Transformers fail to align
with GD when provided with a very small amount of tasks. Nevertheless, we see already almost perfect alignment in our base setting
N = Nx = 10 when provided with B > 2048 tasks. In all settings, we train the Transformer on (non-stochastic) gradient descent
iterating over a single batch of tasks of size B equal to the number provided in the Figure titles (128, 512, 2048, 8192).




                                                                                                                 24


---
