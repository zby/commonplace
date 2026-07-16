---
source: https://arxiv.org/abs/2102.11107
description: Schoelkopf et al. review how causal models, interventions, and reusable mechanisms bear on transfer, robustness, and out-of-distribution generalization
captured: 2026-07-16
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Towards Causal Representation Learning

Author: Bernhard Schoelkopf, Francesco Locatello, Stefan Bauer, Nan Rosemary Ke, Nal Kalchbrenner, Anirudh Goyal, and Yoshua Bengio
Source: https://arxiv.org/abs/2102.11107 (PDF: https://arxiv.org/pdf/2102.11107)
Date: arXiv:2102.11107v1, 22 February 2021

Capture note: text extracted from the arXiv PDF. Mathematical notation, figures, and tables are reproduced as the extractor rendered them.

```text
                                                                                                                                                                                           1




                                                          Towards Causal Representation Learning
                                                 Bernhard Schölkopf † , Francesco Locatello † , Stefan Bauer ? , Nan Rosemary Ke ? , Nal Kalchbrenner
                                                                                   Anirudh Goyal, Yoshua Bengio



                                            Abstract—The two fields of machine learning and graphical                    natural language processing [54], and speech recognition [85],
                                         causality arose and developed separately. However, there is now                 a substantial body of literature explored the robustness of the
                                         cross-pollination and increasing interest in both fields to benefit             prediction of state-of-the-art deep neural network architectures.
                                         from the advances of the other. In the present paper, we review
                                         fundamental concepts of causal inference and relate them to                     The underlying motivation originates from the fact that in the
arXiv:2102.11107v1 [cs.LG] 22 Feb 2021




                                         crucial open problems of machine learning, including transfer                   real world there is often little control over the distribution from
                                         and generalization, thereby assaying how causality can contribute               which the data comes from. In computer vision [75, 228],
                                         to modern machine learning research. This also applies in the                   changes in the test distribution may, for instance, come
                                         opposite direction: we note that most work in causality starts                  from aberrations like camera blur, noise or compression
                                         from the premise that the causal variables are given. A central
                                         problem for AI and causality is, thus, causal representation                    quality [106, 129, 170, 206], or from shifts, rotations, or
                                         learning, the discovery of high-level causal variables from low-                viewpoints [7, 11, 63, 282]. Motivated by this, new benchmarks
                                         level observations. Finally, we delineate some implications of                  were proposed to specifically test generalization of classification
                                         causality for machine learning and propose key research areas                   and detection methods with respect to simple algorithmically
                                         at the intersection of both communities.                                        generated interventions like spatial shifts, blur, changes in
                                                                                                                         brightness or contrast [106, 170], time consistency [94, 227],
                                                                                                                         control over background and rotation [11], as well as images
                                                                   I. I NTRODUCTION
                                                                                                                         collected in multiple environments [19]. Studying the failure
                                            If we compare what machine learning can do to what animals                   modes of deep neural networks from simple interventions has
                                         accomplish, we observe that the former is rather limited at some                the potential to lead to insights into the inductive biases of
                                         crucial feats where natural intelligence excels. These include                  state-of-the-art architectures. So far, there has been no definitive
                                         transfer to new problems and any form of generalization that                    consensus on how to solve these problems, although progress
                                         is not from one data point to the next (sampled from the                        has been made using data augmentation, pre-training, self-
                                         same distribution), but rather from one problem to the next —                   supervision, and architectures with suitable inductive biases
                                         both have been termed generalization, but the latter is a much                  w.r.t. a perturbation of interest [233, 59, 63, 137, 170, 206]. It
                                         harder form thereof, sometimes referred to as horizontal, strong,               has been argued [188] that such fixes may not be sufficient,
                                         or out-of-distribution generalization. This shortcoming is not                  and generalizing well outside the i.i.d. setting requires learning
                                         too surprising, given that machine learning often disregards                    not mere statistical associations between variables, but an
                                         information that animals use heavily: interventions in the world,               underlying causal model. The latter contains the mechanisms
                                         domain shifts, temporal structure — by and large, we consider                   giving rise to the observed statistical dependences, and allows
                                         these factors a nuisance and try to engineer them away. In accor-               to model distribution shifts through the notion of interventions
                                         dance with this, the majority of current successes of machine                   [183, 237, 218, 34, 188, 181].
                                         learning boil down to large scale pattern recognition on suitably                     b) Issue 2 – Learning Reusable Mechanisms: Infants’
                                         collected independent and identically distributed (i.i.d.) data.                understanding of physics relies upon objects that can be
                                            To illustrate the implications of this choice and its relation to            tracked over time and behave consistently [52, 236]. Such a
                                         causal models, we start by highlighting key research challenges.                representation allows children to quickly learn new tasks as
                                               a) Issue 1 – Robustness: With the widespread adoption                     their knowledge and intuitive understanding of physics can
                                         of deep learning approaches in computer vision [101, 140],                      be re-used [15, 52, 144, 250]. Similarly, intelligent agents that
                                                                                                                         robustly solve real-world tasks need to re-use and re-purpose
                                            †: equal contribution.                                                       their knowledge and skills in novel scenarios. Machine
                                            ?: equal contribution.
                                            B. Schölkopf is at the Max-Planck Institute for Intelligent Systems, Max-    learning models that incorporate or learn structural knowledge
                                         Planck-Ring 4, 72076 Tübingen, Germany, bs@tuebingen.mpg.de.                    of an environment have been shown to be more efficient and
                                            F. Locatello is at ETH Zurich, Computer Science Department and the Max       generalize better [14, 10, 16, 84, 197, 212, 8, 274, 26, 76, 83,
                                         Planck Institute for Intelligent Systems. Work partially done while interning
                                         at Google Research Amsterdam. francesco.locatello@gmail.com                     141, 157, 177, 211, 245, 258, 272, 57, 182]. In a modular
                                            S. Bauer is at the Max-Planck Institute for Intelligent Systems,             representation of the world where the modules correspond to
                                         stefan.bauer@tuebingen.mpg.de.                                                  physical causal mechanisms, many modules can be expected to
                                            N. R. Ke is at Mila and the University of Montreal, rose-
                                         mary.nan.ke@gmail.com.                                                          behave similarly across different tasks and environments. An
                                            N. Kalchbrenner is at Google Research Amsterdam, nalk@google.com.            agent facing a new environment or task may thus only need
                                            A. Goyal is at Mila and the University of Montreal,                          to adapt a few modules in its internal representation of the
                                         anirudhgoyal9119@gmail.com
                                            Y. Bengio is at Mila, the University of Montreal, CIFAR Senior Fellow        world [220, 84]. When learning a causal model, one should
                                         yoshua.bengio@mila.quebec                                                       thus require fewer examples to adapt as most knowledge, i.e.,
                                                                                                                                                    2



modules, can be re-used without further training.                       learning, data augmentation, and pre-training. We discuss
      c) A Causality Perspective: Causation is a subtle concept         examples at the intersection between causality and machine
that cannot be fully described using the language of Boolean            learning in scientific applications and speculate on the
logic [151] or that of probabilistic inference; it requires the         advantages of combining the strengths of both fields to
additional notion of intervention [237, 183]. The manipulative          build a more versatile AI.
definition of causation [237, 183, 118] focuses on the fact that
conditional probabilities (“seeing people with open umbrellas                        II. L EVELS OF C AUSAL M ODELING
suggests that it is raining”) cannot reliably predict the outcome
                                                                        The gold standard for modeling natural phenomena is a set of
of an active intervention (“closing umbrellas does not stop the
                                                                    coupled differential equations modeling physical mechanisms
rain”). Causal relations can also be viewed as the components
                                                                    responsible for the time evolution. This allows us to predict
of reasoning chains [151] that provide predictions for situations
                                                                    the future behavior of a physical system, reason about the
that are very far from the observed distribution and may even
                                                                    effect of interventions, and predict statistical dependencies
remain purely hypothetical [163, 183] or require conscious
                                                                    between variables that are generated by coupled time evolution.
deliberation [128]. In that sense, discovering causal relations
                                                                    It also offers physical insights, explaining the functioning of
means acquiring robust knowledge that holds beyond the
                                                                    the system, and lets us read off its causal structure. To this
support of an observed data distribution and a set of training
                                                                    end, consider the coupled set of differential equations
tasks, and it extends to situations involving forms of reasoning.
   Our Contributions: In the present paper, we argue that                                       dx
                                                                                                     = f (x), x ∈ Rd ,                          (1)
causality, with its focus on representing structural knowledge                                  dt
about the data generating process that allows interventions and with initial value x(t0 ) = x0 . The Picard–Lindelöf theorem
changes, can contribute towards understanding and resolving states that at least locally, if f is Lipschitz, there exists a unique
some limitations of current machine learning methods. This solution x(t). This implies in particular that the immediate
would take the field a step closer to a form of artificial intelli- future of x is implied by its past values.
gence that involves thinking in the sense of Konrad Lorenz, i.e.,       If we formally write this in terms of infinitesimal differentials
acting in an imagined space [163]. Despite its success, statistical dt and dx = x(t + dt) − x(t), we get:
learning provides a rather superficial description of reality that
only holds when the experimental conditions are fixed. Instead,                         x(t + dt) = x(t) + dt · f (x(t)).                       (2)
the field of causal learning seeks to model the effect of inter-
                                                                    From this, we can ascertain which entries of the vector x(t)
ventions and distribution changes with a combination of data-
                                                                    mathematically determine the future of others x(t + dt). This
driven learning and assumptions not already included in the
                                                                    tells us that if we have a physical system whose physical
statistical description of a system. The present work reviews and
                                                                    mechanisms are correctly described using such an ordinary
synthesizes key contributions that have been made to this end:
                                                                    differential equation (1), solved for dx        dt (i.e., the derivative only
• We describe different levels of modeling in physical systems      appears on the left-hand side), then its causal structure can be
   in Section II and present the differences between causal and directly read off.1
   statistical models in Section III. We do so not only in terms        While a differential equation is a rather comprehensive
   of modeling abilities but also discuss the assumptions and description of a system, a statistical model can be viewed as a
   challenges involved.                                             much more superficial one. It often does not refer to dynamic
• We expand on the Independent Causal Mechanisms (ICM)              processes; instead, it tells us how some of the variables allow
   principle as a key component that enables the estimation prediction of others as long as experimental conditions do not
   of causal relations from data in Section IV. In particular, change. E.g., if we drive a differential equation system with
   we state the Sparse Mechanism Shift hypothesis as a con- certain types of noise, or we average over time, then it may
   sequence of the ICM principle and discuss its implications be the case that statistical dependencies between components
   for learning causal models.                                      of x emerge, and those can then be exploited by machine
• We review existing approaches to learn causal relations           learning. Such a model does not allow us to predict the effect
   from appropriate descriptors (or features) in Section V. We of interventions; however, its strength is that it can often be
   cover both classical approaches and modern re-interpretations learned from observational data, while a differential equation
   based on deep neural networks, with a focus on the usually requires an intelligent human to come up with it. Causal
   underlying principles that enable causal discovery.              modeling lies in between these two extremes. Like models in
• We discuss how useful models of reality may be learned            physics, it aims to provide understanding and predict the effect
   from data in the form of causal representations, and discuss of interventions. However, causal discovery and learning try
   several current problems of machine learning from a causal to arrive at such models in a data-driven way, replacing expert
   point of view in Section VI.                                     knowledge with weak and generic assumptions. The overall
• We assay the implications of causality for practical machine
   learning in Section VII. Using causal language, we revisit          1 Note that this requires that the differential equation system describes the

   robustness and generalization, as well as existing common        causal physical mechanisms. If, in contrast, we considered a set of differential
                                                                    equations that phenomenologically correctly describe the time evolution of a
   practices such as semi-supervised learning, self-supervised system without capturing the underlying mechanisms (e.g., due to unobserved
                                                                           confounding, or a form of course-graining that does not preserve the causal
  The present paper expands [221], leading to partial text overlap.        structure [207]), then (2) may not be causally meaningful [221, 190].
                                                                                                                                            3



                                                               TABLE I
 A SIMPLE TAXONOMY OF MODELS . T HE MOST DETAILED MODEL ( TOP ) IS A MECHANISTIC OR PHYSICAL ONE , USUALLY IN TERMS OF DIFFERENTIAL
 EQUATIONS . AT THE OTHER END OF THE SPECTRUM ( BOTTOM ), WE HAVE A PURELY STATISTICAL MODEL ; THIS CAN BE LEARNED FROM DATA , BUT IT
OFTEN PROVIDES LITTLE INSIGHT BEYOND MODELING ASSOCIATIONS BETWEEN EPIPHENOMENA . C AUSAL MODELS CAN BE SEEN AS DESCRIPTIONS THAT
     LIE IN BETWEEN , ABSTRACTING AWAY FROM PHYSICAL REALISM WHILE RETAINING THE POWER TO ANSWER CERTAIN INTERVENTIONAL OR
                                                    COUNTERFACTUAL QUESTIONS .

                    Model             Predict in i.i.d.   Predict under distr.   Answer counter-         Obtain         Learn from
                                          setting          shift/intervention    factual questions   physical insight      data
            Mechanistic/physical            yes                    yes                  yes                yes               ?
             Structural causal              yes                    yes                  yes                 ?                ?
             Causal graphical               yes                    yes                   no                 ?                ?
                 Statistical                yes                    no                    no                no              yes



situation is summarized in Table I, adapted from [188]. Below,             production. The robustness of deep neural networks has recently
we address some of the tasks listed in Table I in more detail.             been scrutinized and become an active research topic related
                                                                           to causal inference. We argue that predicting under distribution
A. Predicting in the i.i.d. setting                                        shift should not be reduced to just the accuracy on a test set. If
                                                                           we wish to incorporate learning algorithms into human decision
   Statistical models are a superficial description of reality
                                                                           making, we need to trust that the predictions of the algorithm
as they are only required to model associations. For a given
                                                                           will remain valid if the experimental conditions are changed.
set of input examples X and target labels Y , we may be
interested in approximating P (Y |X) to answer questions like:
“what is the probability that this particular image contains C. Answering Counterfactual Questions
a dog?” or “what is the probability of heart failure given
                                                                      Counterfactual problems involve reasoning about why things
certain diagnostic measurements (e.g., blood pressure) carried
                                                                   happened, imagining the consequences of different actions in
out on a patient?”. Subject to suitable assumptions, these
                                                                   hindsight, and determining which actions would have achieved
questions can be provably answered by observing a sufficiently
                                                                   a desired outcome. Answering counterfactual questions can
large amount of i.i.d. data from P (X, Y ) [257]. Despite the
                                                                   be more difficult than answering interventional questions.
impressive advances of machine learning, causality offers an
                                                                   However, this may be a key challenge for AI, as an intelligent
under-explored complement: accurate predictions may not
                                                                   agent may benefit from imagining the consequences of its
be sufficient to inform decision making. For example, the
                                                                   actions as well as understanding in retrospect what led to
frequency of storks is a reasonable predictor for human birth
                                                                   certain outcomes, at least to some degree of approximation.2
rates in Europe [168]. However, as there is no direct causal link
                                                                   We have above mentioned the example of statistical predictions
between those two variables, a change to the stork population
                                                                   of heart failure. An interventional question would be “how
would not affect the birth rates, even though a statistical model
                                                                   does the probability of heart failure change if we convince a
may predict so. The predictions of a statistical model are only
                                                                   patient to exercise regularly?” A counterfactual one would be
accurate within identical experimental conditions. Performing
                                                                   “would a given patient have suffered heart failure if they had
an intervention changes the data distribution, which may lead
                                                                   started exercising a year earlier?”. As we shall discuss below,
to (arbitrarily) inaccurate predictions [183, 237, 218, 188].
                                                                   counterfactuals, or approximations thereof, are especially
                                                                   critical in reinforcement learning. They can enable agents to
B. Predicting Under Distribution Shifts                            reflect on their decisions and formulate hypotheses that can be
   Interventional questions are more challenging than predic- empirically verified in a process akin to the scientific method.
tions as they involve actions that take us out of the usual i.i.d.
setting of statistical learning. Interventions may affect both
the value of a subset of causal variables and their relations. D. Nature of Data: Observational, Interventional,
For example, “is increasing the number of storks in a country (Un)structured
going to boost its human birth rate?” and “would fewer people         The data format plays a substantial role in which type
smoke if cigarettes were more socially stigmatized?”. As of relation can be inferred. We can distinguish two axes
interventions change the joint distribution of the variables of data modalities: observational versus interventional, and
of interest, classical statistical learning guarantees [257] no hand-engineered versus raw (unstructured) perceptual input.
longer apply. On the other hand, learning about interventions
may allow to train predictive models that are robust against         2 Note that the two types of questions occupy a continuum: to this

the changes in distribution that naturally happen in the real      end, consider a probability which is both conditional and interventional
                                                                   P (A|B, do(C)). If B is the empty set, we have a classical intervention;
world. Here, interventions do not need to be deliberate actions if B contained all (unobserved) noise terms, we have a counterfactual. If B is
to achieve a goal. Statistical relations may change dynamically not identical to the noise terms, but nevertheless informative about them, we
over time (e.g., people’s preferences and tastes) or there may get something in between. For instance, reinforcement learning practitioners
                                                                   may call Q functions as providing counterfactuals, even though they model
simply be a mismatch between a carefully controlled training P (return from t| agent state at time t, do (action at time t)), and therefore
distribution and the test distribution of a model deployed in closer to an intervention (which is why they can be estimated from data).
                                                                                                                                                        4



   Observational and Interventional Data: an extreme form of                  (3) we employ high-performance computing systems, and
data which is often assumed but seldom strictly available is                  finally (often ignored, but crucial when it comes to causality)
observational i.i.d. data, where each data point is independently             (4) the problems are i.i.d. The latter can be guaranteed by
sampled from the same distribution. Another extreme is                        the construction of a task including training and test set (e.g.,
interventional data with known interventions, where we observe                image recognition using benchmark datasets). Alternatively,
data sets sampled from multiple distributions each of which                   problems can be made approximately i.i.d., e.g.. by carefully
is the result of a known intervention. In between, we have                    collecting the right training set for a given application problem,
data with (domain) shifts or unknown interventions. This                      or by methods such as “experience replay” [171] where a
is observational in the sense that the data is only observed                  reinforcement learning agent stores observations in order to
passively, but it is interventional in the sense that there are               later permute them for the purpose of re-training.
interventions/shifts, but unknown to us.                                         For i.i.d. data, strong universal consistency results from
   Hand Engineered Data vs. Raw Data: especially in classical                 statistical learning theory apply, guaranteeing convergence of
AI, data is often assumed to be structured into high-level and                a learning algorithm to the lowest achievable risk. Such algo-
semantically meaningful variables which may partially (modulo                 rithms do exist, for instance, nearest neighbor classifiers, sup-
some variables being unobserved) correspond to the causal                     port vector machines, and neural networks [257, 217, 239, 66].
variables of the underlying graph. Raw Data, in contrast, is                  Seen in this light, it is not surprising that we can indeed match
unstructured and does not expose any direct information about                 or surpass human performance if given enough data. However,
causality.                                                                    current machine learning methods often perform poorly when
   While statistical models are weaker than causal models, they               faced with problems that violate the i.i.d. assumption, yet seem
can be efficiently learned from observational data alone on                   trivial to humans. Vision systems can be grossly misled if
both hand-engineered features and raw perceptual input such                   an object that is normally recognized with high accuracy is
as images, videos, speech etc. On the other hand, although                    placed in a context that in the training set may be negatively
methods for learning causal structure from observations exist                 correlated with the presence of the object. Distribution shifts
[237, 188, 229, 113, 174, 187, 139, 17, 246, 277, 175, 123,                   may also arise from simple corruptions that are common in
186, 176, 36, 82, 161], learning causal relations frequently                  real-world data collection pipelines [9, 106, 129, 170, 206].
requires collecting data from multiple environments, or the                   An example of this is the impact of socio-economic factors in
ability to perform interventions [251]. In some cases, it is                  clinics in Thailand on the accuracy of a detection system for
assumed that all common causes of measured variables are also                 Diabetic Retinopathy [18]. More dramatically, the phenomenon
observed (causal sufficiency).3 Overall, a significant amount of              of “adversarial vulnerability” [249] highlights how even tiny but
prior knowledge is encoded in which variables are measured.                   targeted violations of the i.i.d. assumption, generated by adding
Moving forward, one would hope to develop methods that                        suitably chosen perturbations to images, imperceptible to hu-
replace expert data collection with suitable inductive biases and             mans, can lead to dangerous errors such as confusion of traffic
learning paradigms such as meta-learning and self-supervision.                signs. Overall, it is fair to say that much of the current practice
If we wish to learn a causal model that is useful for a particular            (of solving i.i.d. benchmark problems) and most theoretical
set of tasks and environments, the appropriate granularity of                 results (about generalization in i.i.d. settings) fail to tackle the
the high-level variables depends on the tasks of interest and on              hard open challenge of generalization across problems.
the type of data we have at our disposal, for example which                      To further understand how the i.i.d. assumption is problem-
interventions can be performed and what is known about the                    atic, let us consider a shopping example. Suppose Alice is
domain.                                                                       looking for a laptop rucksack on the internet (i.e., a rucksack
                                                                              with a padded compartment for a laptop). The web shop’s
            III. C AUSAL M ODELS AND I NFERENCE                               recommendation system suggests that she should buy a laptop
   As discussed, reality can be modeled at different levels,                  to go along with the rucksack. This seems odd because she
from the physical one to statistical associations between                     probably already has a laptop, otherwise she would not be
epiphenomena. In this section, we expand on the difference                    looking for the rucksack in the first place. In a way, the laptop
between statistical and causal modeling and review a formal                   is the cause, and the rucksack is an effect. Now suppose we are
language to talk about interventions and distribution changes.                told whether a customer has bought a laptop. This reduces our
                                                                              uncertainty about whether she also bought a laptop rucksack,
                                                                              and vice versa —- and it does so by the same amount (the
A. Methods driven by i.i.d. data                                              mutual information), so the directionality of cause and effect
   The machine learning community has produced impressive                     is lost. However, the directionality is present in the physical
successes with machine learning applications to big data                      mechanisms generating statistical dependence, for instance the
problems [148, 171, 223, 231, 53]. In these successes, there                  mechanism that makes a customer want to buy a rucksack once
are several trends at work [215]: (1) we have massive amounts                 she owns a laptop.4 Recommending an item to buy constitutes
of data, often from simulations or large scale human labeling,                an intervention in a system, taking us outside the i.i.d. setting.
(2) we use high capacity machine learning systems (i.e.,                      We no longer work with the observational distribution, but a dis-
complex function classes with many adjustable parameters),
                                                                                 4 Note that the physical mechanisms take place in time, and if available,
  3 There are also algorithms that do not require causal sufficiency [237].   time order may provide additional information about causality.
                                                                                                                                            5



tribution where certain variables or mechanisms have changed.         structural properties inherited from the graph [147, 183]: it
                                                                      satisfies the causal Markov condition stating that conditioned
B. The Reichenbach Principle: From Statistics to Causality            on its parents, each Xj is independent of its non-descendants.
                                                                         Intuitively, we can think of the independent noises as
   Reichenbach [198] clearly articulated the connection
                                                                      “information probes” that spread through the graph (much like
between causality and statistical dependence. He postulated:
                                                                      independent elements of gossip can spread through a social
     Common Cause Principle: if two observables X and Y               network). Their information gets entangled, manifesting itself
     are statistically dependent, then there exists a variable        in a footprint of conditional dependencies making it possible
     Z that causally influences both and explains all the             to infer aspects of the graph structure from observational data
     dependence in the sense of making them independent               using independence testing. Like in the gossip analogy, the
     when conditioned on Z.                                           footprint may not be sufficiently characteristic to pin down
                                                                      a unique causal structure. In particular, it certainly is not if
                                                                      there are only two observables, since any nontrivial conditional
   As a special case, this variable can coincide with X or Y .
                                                                      independence statement requires at least three variables. The
Suppose that X is the frequency of storks and Y the human
                                                                      two-variable problem can be addressed by making additional
birth rate. If storks bring the babies, then the correct causal
                                                                      assumptions, as not only the graph topology leaves a footprint
graph is X → Y . If babies attract storks, it is X ← Y . If there
                                                                      in the observational distribution, but the functions fi do, too.
is some other variable that causes both (such as economic
                                                                      This point is interesting for machine learning, where much
development), we have X ← Z → Y .
                                                                      attention is devoted to properties of function classes (e.g., priors
   Without additional assumptions, we cannot distinguish these
                                                                      or capacity measures), and we shall return to it below.
three cases using observational data. The class of observational
                                                                            a) Causal Graphical Models: The graph structure along
distributions over X and Y that can be realized by these
                                                                      with the joint independence of the noises implies a canonical
models is the same in all three cases. A causal model thus
                                                                      factorization of the joint distribution entailed by (3) into causal
contains genuinely more information than a statistical one.
                                                                      conditionals that we refer to as the causal (or disentangled)
   While causal structure discovery is hard if we have only two
                                                                      factorization,
observables [187], the case of more observables is surprisingly
                                                                                                                n
easier, the reason being that in that case, there are nontrivial                                               Y
                                                                                      P (X1 , . . . , Xn ) =       P (Xi | PAi ).          (4)
conditional independence properties [238, 51, 74] implied by
                                                                                                               i=1
causal structure. These generalize the Reichenbach Principle
and can be described by using the language of causal graphs While many other entangled factorizations are possible, e.g.,
                                                                                                           n
or structural causal models, merging probabilistic graphical                                              Y
models and the notion of interventions [237, 183]. They are best                P (X  1 , . . . , X n ) =     P (Xi | Xi+1 , . . . , Xn ), (5)
                                                                                                          i=1
described using directed functional parent-child relationships
rather than conditionals. While conceptually simple in hindsight, the factorization (4) yields practical computational advantages
this constituted a major step in the understanding of causality. during inference, which is in general hard, even when it comes
                                                                      to non-trivial approximations [210]. But more interestingly,
                                                                      it is the only one that decomposes the joint distribution into
C. Structural causal models (SCMs)
                                                                      conditionals corresponding to the structural assignments (3). We
   The SCM viewpoint considers a set of observables (or think of these as the causal mechanisms that are responsible for
variables) X1 , . . . , Xn associated with the vertices of a directed all statistical dependencies among the observables. Accordingly,
acyclic graph (DAG). We assume that each observable is the in contrast to (5), the disentangled factorization represents the
result of an assignment                                               joint distribution as a product of causal mechanisms.
              Xi    := fi (PAi , Ui ),   (i = 1, . . . , n),      (3)       b) Latent variables and Confounders: Variables in a
                                                                      causal graph may be unobserved, which can make causal
using a deterministic function fi depending on Xi ’s parents in inference particularly challenging. Unobserved variables may
the graph (denoted by PAi ) and on an unexplained random confound two observed variables so that they either appear
variable Ui . Mathematically, the observables are thus random statistically related while not being causally related (i.e., neither
variables, too. Directed edges in the graph represent direct of the variables is an ancestor of the other), or their statistical
causation, since the parents are connected to Xi by directed relation is altered by the presence of the confounder (e.g., one
edges and through (3) directly affect the assignment of Xi . variable is a causal ancestor for the other, but the confounder
The noise Ui ensures that the overall object (3) can represent is a causal ancestor of both). Confounders may or may not be
a general conditional distribution P (Xi |PAi ), and the set of known or observed.
noises U1 , . . . , Un are assumed to be jointly independent. If            c) Interventions: The SCM language makes it straight-
they were not, then by the Common Cause Principle there forward to formalize interventions as operations that modify a
should be another variable that causes their dependence, and subset of assignments (3), e.g., changing Ui , setting fi (and
thus our model would not be causally sufficient.                      thus Xi ) to a constant, or changing the functional form of fi
   If we specify the distributions of U1 , . . . , Un , recursive (and thus the dependency of Xi on its parents) [237, 183].
application of (3) allows us to compute the entailed observa-            Several types of interventions may be possible [62] which
tional joint distribution P (X1 , . . . , Xn ). This distribution has can be categorized as: No intervention: only observational
                                                                                                                                         6



data is obtained from the causal model. Hard/perfect: the                  a) Causal Learning and Reasoning: The conceptual basis
function in the structural assignment (3) of a variable (or, of statistical learning is a joint distribution P (X1 , . . . , Xn )
analogously, of multiple variables) is set to a constant (implying (where often one of the Xi is a response variable denoted
that the value of the variable is fixed), and then the entailed as Y ), and we make assumptions about function classes used
distribution for the modified SCM is computed. Soft/imperfect: to approximate, say, a regression E[Y |X]. Causal learning
the structural assignment (3) for a variable is modified by considers a richer class of assumptions, and seeks to exploit the
changing the function or the noise term (this corresponds fact that the joint distribution possesses a causal factorization
to changing the conditional distribution given its parents). (4). It involves the causal conditionals P (Xi | PAi ) (e.g.,
Uncertain: the learner is not sure which mechanism/variable represented by the functions fi and the distribution of Ui in (3)),
is affected by the intervention.                                     how these conditionals relate to each other, and interventions
   One could argue that stating the structural assignments as or changes that they admit. Once a causal model is available,
in (3) is not yet sufficient to formulate a causal model. In either by external human knowledge or a learning process,
addition, one should specify the set of possible interventions causal reasoning allows to draw conclusions on the effect
on the structural causal model. This may be done implicitly of interventions, counterfactuals and potential outcomes. In
via the functional form of structural equations by allowing any contrast, statistical models only allow to reason about the
intervention over the domain of the mechanisms. This becomes outcome of i.i.d. experiments.
relevant when learning a causal model from data, as the SCM
depends on the interventions. Pragmatically, we should aim                      IV. I NDEPENDENT C AUSAL M ECHANISMS
at learning causal models that are useful for specific sets of
tasks of interest [207, 267] on appropriate descriptors (in terms       We now return to the disentangled factorization (4) of the
of which causal statements they support) that must either be         joint  distribution P (X1 , . . . , Xn ). This factorization according
provided or learned. We will return to the assumptions that          to  the   causal graph is always possible when the Ui are
allow learning causal models and features in Section IV.             independent,    but we will now consider an additional notion of
                                                                     independence relating the factors in (4) to one another.
                                                                        Whenever we perceive an object, our brain assumes that the
D. Difference Between Statistical Models, Causal Graphical           object   and the mechanism by which the information contained
Models, and SCMs                                                     in its  light reaches our brain are independent. We can violate
                                                                     this by looking at the object from an accidental viewpoint,
   An example of the difference between a statistical and a which can give rise to optical illusions [188]. The above
causal model is depicted in Figure 1. A statistical model may independence assumption is useful because in practice, it
be defined for instance through a graphical model, i.e., a holds most of the time, and our brain thus relies on objects
probability distribution along with a graph such that the former being independent of our vantage point and the illumination.
is Markovian with respect to the latter (in which case it can be Likewise, there should not be accidental coincidences, such as
factorized as (4)). However, the edges in a (generic) graphical 3D structures lining up in 2D, or shadow boundaries coinciding
model do not need to be causal [97]. For instance, the two with texture boundaries. In vision research, this is called the
graphs X1 → X2 → X3 and X1 ← X2 ← X3 imply the same generic viewpoint assumption.
conditional independence(s) (X1 and X3 are independent given            If we move around the object, our vantage point changes,
X2 ). They are thus in the same Markov equivalence class, i.e., but we assume that the other variables of the overall generative
if a distribution is Markovian w.r.t. one of the graphs, then process (e.g., lighting, object position and structure) are
it also is w.r.t. the other graph. Note that the above serves unaffected by that. This is an invariance implied by the above
as an example that the Markov condition is not sufficient for independence, allowing us to infer 3D information even without
causal discovery. Further assumptions are needed, cf. below stereo vision (“structure from motion”).
and [237, 183, 188].                                                    For another example, consider a dataset that consists of
   A graphical model becomes causal if the edges of its altitude A and average annual temperature T of weather stations
graph are causal (in which case the graph is referred to as a [188]. A and T are correlated, which we believe is due to
“causal graph”), cf. (3). This allows to compute interventional the fact that the altitude has a causal effect on temperature.
distributions as depicted in Figure 1. When a variable is Suppose we had two such datasets, one for Austria and one for
intervened upon, we disconnect it from its parents, fix its Switzerland. The two joint distributions P (A, T ) may be rather
value, and perform ancestral sampling on its children.               different since the marginal distributions P (A) over altitudes
   A structural causal model is composed of (i) a set of causal will differ. The conditionals P (T |A), however, may be (close
variables and (ii) a set of structural equations with a distribution to) invariant, since they characterize the physical mechanisms
over the noise variables Ui (or a set of causal conditionals). that generate temperature from altitude. This similarity is lost
While both causal graphical models and SCMs allow to com- upon us if we only look at the overall joint distribution, without
pute interventional distributions, only the SCMs allow to com- information about the causal structure A → T . The causal fac-
pute counterfactuals. To compute counterfactuals, we need to fix torization P (A)P (T |A) will contain a component P (T |A) that
the value of the noise variables. Moreover, there are many ways generalizes across countries, while the entangled factorization
to represent a conditional as a structural assignment (by picking P (T )P (A|T ) will exhibit no such robustness. Cum grano salis,
different combinations of functions and noise variables).            the same applies when we consider interventions in a system.
                                                                                                                                                                 7




                 Statistical model




                                                                           Causal model
Fig. 1. Difference between statistical (left) and causal models (right) on a given set of three variables. While a statistical model specifies a single probability
distribution, a causal model represents a set of distributions, one for each possible intervention (indicated with a in the figure).



For a model to correctly predict the effect of interventions,                             Aldrich [4] discusses the historical development of these ideas
it needs to be robust to generalizing from an observational                               in economics. He argues that the “most basic question one
distribution to certain interventional distributions.                                     can ask about a relation should be: How autonomous is
   One can express the above insights as follows [218, 188]:                              it?” [71, preface]. Pearl [183] discusses autonomy in detail,
                                                                                          arguing that a causal mechanism remains invariant when other
    Independent Causal Mechanisms (ICM) Principle.                                        mechanisms are subjected to external influences. He points out
    The causal generative process of a system’s variables                                 that causal discovery methods may best work “in longitudinal
    is composed of autonomous modules that do not inform                                  studies conducted under slightly varying conditions, where
    or influence each other. In the probabilistic case, this                              accidental independencies are destroyed and only structural
    means that the conditional distribution of each variable                              independencies are preserved.” Overviews are provided by
    given its causes (i.e., its mechanism) does not inform                                Aldrich [4], Hoover [111], Pearl [183], and Peters et al.
    or influence the other mechanisms.                                                    [188, Sec. 2.2]. These seemingly different notions can be
                                                                                          unified [120, 240].
   This principle entails several notions important to causality,                            We view any real-world distribution as a product of causal
including separate intervenability of causal variables,                                   mechanisms. A change in such a distribution (e.g., when
modularity and autonomy of subsystems, and invariance                                     moving from one setting/domain to a related one) will always
[183, 188]. If we have only two variables, it reduces to                                  be due to changes in at least one of those mechanisms.
an independence between the cause distribution and the                                    Consistent with the implication (a) of the ICM Principle, we
mechanism producing the effect distribution.                                              state the following hypothesis:
   Applied to the causal factorization (4), the principle tells us
that the factors should be independent in the sense that                Sparse Mechanism Shift (SMS). Small distribution
 (a) changing (or performing an intervention upon) one mech-            changes tend to manifest themselves in a sparse or local
      anism P (Xi |PAi ) does not change any of the other               way in the causal/disentangled factorization (4), i.e.,
      mechanisms P (Xj |PAj ) (i 6= j) [218], and                       they should usually not affect all factors simultaneously.
 (b) knowing some other mechanisms P (Xi |PAi ) (i 6= j) does
      not give us information about a mechanism P (Xj |PAj )          In contrast, if we consider a non-causal factorization, e.g.,
      [120].                                                       (5), then many, if not all, terms will be affected simultaneously
This notion of independence thus subsumes two aspects: the as we change one of the physical mechanisms responsible for
former pertaining to influence, and the latter to information.     a system’s statistical dependencies. Such a factorization may
   The notion of invariant, autonomous, and independent thus be called entangled, a term that has gained popularity in
mechanisms has appeared in various guises throughout the machine learning [23, 109, 158, 247].
history of causality research [99, 71, 111, 183, 120, 240, 188].      The SMS hypothesis was stated in [181, 24, 221, 115], and
Early work on this was done by Haavelmo [99], stating the in earlier form in [218, 279, 220]. An intellectual ancestor
assumption that changing one of the structural assignments is Simon’s invariance criterion, i.e., that the causal structure
leaves the other ones invariant. Hoover [111] attributes to remains invariant across changing background conditions [235].
Herb Simon the invariance criterion: the true causal order is The hypothesis is also related to ideas of looking for features
the one that is invariant under the right sort of intervention. that vary slowly [69, 270]. It has recently been used for
                                                                                                                                                       8



learning causal models [131], modular architectures [84, 28]                   sition of the joint Kolmogorov complexity in analogy to (4), and
and disentangled representations [159].                                        prove that they are implied by the structural causal model [120].
   We have informally talked about the dependence of two                       Interestingly, in this case, independence of noises and indepen-
mechanisms P (Xi |PAi ) and P (Xj |PAj ) when discussing                       dence of mechanisms coincide, since the independent programs
the ICM Principle and the disentangled factorization (4). Note                 play the role of the unexplained noise terms. This approach
that the dependence of two such mechanisms does not coincide                   shows that causality is not intrinsically bound to statistics.
with the statistical dependence of the random variables Xi and
Xj . Indeed, in a causal graph, many of the random variables
will be dependent even if all mechanisms are independent.                           V. C AUSAL D ISCOVERY AND M ACHINE L EARNING
Also, the independence of the noise terms Ui does not translate                   Let us turn to the problem of causal discovery from data.
into the independence of the Xi . Intuitively speaking, the                    Subject to suitable assumptions such as faithfulness [237], one
independent noise terms Ui provide and parameterize the                        can sometimes recover aspects of the underlying graph6 from
uncertainty contained in the fact that a mechanism P (Xi |PAi )                observational data by performing conditional independence
is non-deterministic,5 and thus ensure that each mechanism                     tests. However, there are several problems with this approach.
adds an independent element of uncertainty. In this sense, the                 One is that our datasets are always finite in practice, and
ICM Principle contains the independence of the unexplained                     conditional independence testing is a notoriously difficult
noise terms in an SCM (3) as a special case.                                   problem, especially if conditioning sets are continuous and
   In the ICM Principle, we have stated that independence                      multi-dimensional. So while, in principle, the conditional
of two mechanisms (formalized as conditional distributions)                    independencies implied by the causal Markov condition hold
should mean that the two conditional distributions do not                      irrespective of the complexity of the functions appearing
inform or influence each other. The latter can be thought of as                in an SCM, for finite datasets, conditional independence
requiring that independent interventions are possible. To better               testing is hard without additional assumptions [225]. Recent
understand the former, we next discuss a formalization in terms                progress in (conditional) independence testing heavily relies on
of algorithmic independence. In a nutshell, we encode each                     kernel function classes to represent probability distributions in
mechanism as a bit string, and require that joint compression                  reproducing kernel Hilbert spaces [90, 91, 73, 278, 60, 191, 42].
of these strings does not save space relative to independent                   The other problem is that in the case of only two variables,
compressions.                                                                  the ternary concept of conditional independence collapses and
   To this end, first recall that we have so far discussed links               the Markov condition thus has no nontrivial implications.
between causal and statistical structures. Of the two, the more                   It turns out that both problems can be addressed by making
fundamental one is the causal structure, since it captures the                 assumptions on function classes. This is typical for machine
physical mechanisms that generate statistical dependencies in                  learning, where it is well-known that finite-sample general-
the first place. The statistical structure is an epiphenomenon                 ization without assumptions on function classes is impossible.
that follows if we make the unexplained variables random.                      Specifically, although there are universally consistent learning
It is awkward to talk about statistical information contained                  algorithms, i.e., approaching minimal expected error in the
in a mechanism since deterministic functions in the generic                    infinite sample limit, there are always cases where this
case neither generate nor destroy information. This serves                     convergence is arbitrarily slow. So for a given sample size, it
as a motivation to devise an alternative model of causal                       will depend on the problem being learned whether we achieve
structures in terms of Kolmogorov complexity [120]. The                        low expected error, and statistical learning theory provides
Kolmogorov complexity (or algorithmic information) of a bit                    probabilistic guarantees in terms of measures of complexity of
string is essentially the length of its shortest compression on a              function classes [55, 257].
Turing machine, and thus a measure of its information content.                    Returning to causality, we provide an intuition why assump-
Independence of mechanisms can be defined as vanishing                         tions on the functions in an SCM should be necessary to learn
mutual algorithmic information; i.e., two conditionals are                     about them from data. Consider a toy SCM with only two
considered independent if knowing (the shortest compression                    observables X → Y . In this case, (3) turns into
of) one does not help us achieve a shorter compression of the
other.                                                                                                     X=U                                       (6)
   Algorithmic information theory provides a natural framework                                             Y = f (X, V )                             (7)
for non-statistical graphical models [120, 126]. Just like the
latter are obtained from structural causal models by making the                with U ⊥  ⊥ V . Now think of V acting as a random selector
unexplained variables Ui random, we obtain algorithmic graph-                  variable choosing from among a set of functions F = {fv (x) ≡
ical models by making the Ui bit strings, jointly independent                  f (x, v) | v ∈ supp(V )}. If f (x, v) depends on v in a non-
across nodes, and viewing Xi as the output of a fixed Turing ma-               smooth way, it should be hard to glean information about the
chine running the program Ui on the input PAi . Similar to the                 SCM from a finite dataset, given that V is not observed and
statistical case, one can define a local causal Markov condition,              its value randomly selects among arbitrarily different fv .
a global one in terms of d-separation, and an additive decompo-
                                                                                 6 One can recover the causal structure up to a Markov equivalence class,
  5 In the sense that the mapping from PA to X is described by a non-trivial   where DAGs have the same undirected skeleton and “immoralities” (Xi →
                                         i    i
conditional distribution, rather than by a function.                           Xj ← Xk ).
                                                                                                                                      9



  This motivates restricting the complexity with which f                         VI. L EARNING C AUSAL VARIABLES
depends on V . A natural restriction is to assume an additive
                                                                        Traditional causal discovery and reasoning assume that
noise model
                                                                     the units are random variables connected by a causal graph.
                                                                     However, real-world observations are usually not structured
                        X=U                                   (8)    into those units to begin with, e.g., objects in images [162].
                        Y = f (X) + V.                        (9)    Hence, the emerging field of causal representation learning
                                                                     strives to learn these variables from data, much like machine
                                                                     learning went beyond symbolic AI in not requiring that the
If f in (7) depends smoothly on V , and if V is relatively           symbols that algorithms manipulate be given a priori (cf.
well concentrated, this can be motivated by a local Taylor           Bonet and Geffner [33]). To this end, we could try to connect
expansion argument. It drastically reduces the effective size of     causal variables S1 , . . . , Sn to observations
the function class — without such assumptions, the latter could
depend exponentially on the cardinality of the support of V .                              X = G(S1 , . . . , Sn ),                (10)
Restrictions of function classes not only make it easier to learn
                                                                     where G is a non-linear function. An example can be seen in
functions from data, but it turns out that they can break the
                                                                     Figure 2, where high-dimensional observations are the result of
symmetry between cause and effect in the two-variable case:
                                                                     a view on the state of a causal system that is then processed by
one can show that given a distribution over X, Y generated
                                                                     a neural network to extract high-level variables that are useful
by an additive noise model, one cannot fit an additive noise
                                                                     on a variety of tasks. Although causal models in economics,
model in the opposite direction (i.e., with the roles of X
                                                                     medicine, or psychology often use variables that are abstractions
and Y interchanged) [113, 174, 187, 139, 17], cf. also [246].
                                                                     of underlying quantities, it is challenging to state general condi-
This is subject to certain genericity assumptions, and notable
                                                                     tions under which coarse-grained variables admit causal models
exceptions include the case where U, V are Gaussian and f is
                                                                     with well-defined interventions [41, 207]. Defining objects or
linear. It generalizes results of Shimizu et al. [229] for linear
                                                                     variables that can be causally related amounts to coarse-graining
functions, and it can be generalized to include non-linear rescal-
                                                                     of more detailed models of the world, including microscopic
ings [277], loops [175], confounders [123], and multi-variable
                                                                     structural equation models [207], ordinary differential equa-
settings [186]. Empirically, there is a number of methods that
                                                                     tions [173, 208], and temporally aggregated time series [78].
can detect causal direction better than chance [176], some of
                                                                     The task of identifying suitable units that admit causal models
them building on the above Kolmogorov complexity model [36],
                                                                     is challenging for both human and machine intelligence. Still,
some on generative models [82], and some directly learning to
                                                                     it aligns with the general goal of modern machine learning to
classify bivariate distributions into causal vs. anticausal [161].
                                                                     learn meaningful representations of data, where meaningful can
   While restrictions of function classes are one possibility to     include robust, explainable, or fair [142, 133, 276, 130, 260].
allow to identify the causal structure, other assumptions or            To combine structural causal modeling (3) and representation
scenarios are possible. So far, we have discussed that causal        learning, we should strive to embed an SCM into larger
models are expected to generalize under certain distribution         machine learning models whose inputs and outputs may be
shifts since they explicitly model interventions. By the SMS         high-dimensional and unstructured, but whose inner workings
hypothesis, much of the causal structure is assumed to remain        are at least partly governed by an SCM (that can be parame-
invariant. Hence distribution shifts such as observing a system      terized with a neural network). The result may be a modular
in different “environments / contexts” can significantly help to     architecture, where the different modules can be individually
identify causal structure [251, 188]. These contexts can come        fine-tuned and re-purposed for new tasks [181, 84] and the SMS
from interventions [218, 189, 192], non-stationary time series       hypothesis can be used to enforce the appropriate structure.
[117, 100, 193] or multiple views [89, 115]. The contexts can        We visualize an example in Figure 3 where changes are sparse
likewise be interpreted as different tasks, which provide a          for the appropriate causal variables (the position of the finger
connection to meta-learning [22, 67, 213].                           and the cube changed as a result of moving the finger), but
   The work of Bengio et al. [24] ties the generalization            dense in other representations, for example in the pixel space
in meta-learning to invariance properties of causal models,          (as finger and cube move, many pixels change their value).
using the idea that a causal model should adapt faster to            At the extreme, all pixels may change as a result of a sparse
interventions than purely predictive models. This was extended       intervention, for example, if the camera view or the lighting
to multiple variables and unknown interventions in [131],            changes.
proposing a framework for causal discovery using neural                 We now discuss three problems of modern machine learning
networks by turning the discrete graph search into a continuous      in the light of causal representation learning.
optimization problem. While [24, 131] focus on learning a                  a) Problem 1 – Learning Disentangled Representations:
causal model using neural networks with an unsupervised              We have earlier discussed the ICM Principle implying both
loss, the work of Dasgupta et al. [50] explores learning a           the independence of the SCM noise terms in (3) and thus the
causal model using a reinforcement learning agent. These             feasibility of the disentangled representation
approaches have in common that semantically meaningful                                                      n
abstract representations are given and do not need to be                                                    Y
                                                                                   P (S1 , . . . , Sn ) =         P (Si | PAi )    (11)
learned from high-dimensional and low-level (e.g., pixel) data.                                             i=1
                                                                                                                                                                  10




Fig. 2. Illustration of the causal representation learning problem setting. Perceptual data, such as images or other high-dimensional sensor measurements,
can be thought of as entangled views of the state of an unknown causal system as described in (10). With the exception of possible task labels, none of the
variables describing the causal variables generating the system may be known. The goal of causal representation learning is to learn a representation (partially)
exposing this unknown causal structure (e.g., which variables describe the system, and their relations). As full recovery may often be unreasonable, neural
networks may map the low-level features to some high-level variables supporting causal statements relevant to a set of downstream tasks of interest. For
example, if the task is to detect the manipulable objects in a scene, the representation may separate intrinsic object properties from their pose and appearance
to achieve robustness to distribution shifts on the latter variables. Usually, we do not get labels for the high-level variables, but the properties of causal models
can serve as useful inductive biases for learning (e.g., the SMS hypothesis).



                                                                               f1 , . . . , fn . Finally, we apply a decoder p : Rn → Rd . For
                                                                               suitable n, the system can be trained using reconstruction error
                                                                               to satisfy p ◦ f ◦ q ≈ id on the observed images. If the causal
                                                                               graph is known, the topology of a neural network implementing
                                                                               f can be fixed accordingly; if not, the neural network decoder
                                                                               learns the composition p̃ = p ◦ f . In practice, one may not
                                                                               know f , and thus only learn an autoencoder p̃ ◦ q, where the
                                                                               causal graph effectively becomes an unspecified part of the
                                                                               decoder p̃, possibly aided by a suitable choice of architecture
                                                                               [149].
                                                                                  Much of the existing work on disentanglement [109, 158,
                                                                               159, 256, 157, 135, 202, 61] focuses on independent factors
                                                                               of variation. This can be viewed as the special case where the
                                                                               causal graph is trivial, i.e., ∀i : PAi = ∅ in (12). In this case,
Fig. 3. Example of the SMS hypothesis where an intervention (which may
or may not be intentional/observed) changes the position of one finger ( ), the factors are functions of the independent exogenous noise
                                                                                                                                   7
and as a consequence, the object falls. The change in pixel space is entangled variables, and thus independent themselves. However, the ICM
(or distributed), in contrast to the change in the causal model.               Principle is more general and contains statistical independence
                                                                               as a special case.
as well as the property that the conditionals P (Si | PAi )                       Note that the problem of object-centric representation
be independently manipulable and largely invariant across                      learning        [10, 39, 83, 86, 87, 138, 155, 160, 262, 255] can
related problems. Suppose we seek to reconstruct such a                        also   be    considered    a special case of disentangled factorization
disentangled representation using independent mechanisms                       as   discussed       here.   Objects are constituents of scenes that
(11) from data, but the causal variables Si are not provided to                in   principle      permit     separate interventions. A disentangled
us a priori. Rather, we are given (possibly high-dimensional)                  representation        of a  scene   containing objects should probably
X = (X1 , . . . , Xd ) (below, we think of X as an image with                  use    objects     as  some      of the building blocks of an overall
                                                                                                          8
pixels X1 , . . . , Xd ) as in (10), from which we should construct            causal      factorization    ,  complemented    by mechanisms such as
causal variables S1 , . . . , Sn (n  d) as well as mechanisms,                orientation,      viewing    direction, and  lighting.
cf. (3),                                                                          The problem of recovering the exogenous noise variables
                                                                               is ill-defined in the i.i.d. case as there are infinitely many
                Si := fi (PAi , Ui ),         (i = 1, . . . , n),        (12) equivalent solutions yielding the same observational distribu-
modeling the causal relationships among the Si . To this                               7 For an example to see why this is often not desirable, note that the

end, as a first step, we can use an encoder q : Rd → Rn                             presence of fork and knife may be statistically dependent, yet we might want
taking X to a latent “bottleneck” representation comprising the                     a disentangled representation to represent them as separate entities.
                                                                                       8 Objects can be represented at different levels of granularity [207], i.e. as
unexplained noise variables U = (U1 , . . . , Un ). The next step                   a single entity or as a composition of other causal variables encoding parts,
is the mapping f (U ) determined by the structural assignments                      properties, and other factors of variation.
                                                                                                                                      11



tion [158, 116, 188]. Additional assumptions or biases can            learn such models is to look for independent causal mechanisms
help favoring certain solutions over others [158, 205]. Leeb          [180] and competitive training can play a role in this. For
et al. [149] propose a structured decoder that embeds an SCM          pattern recognition tasks, [181, 84] suggest that learning causal
and automatically learns a hierarchy of disentangled factors.         models that contain independent mechanisms may help in
   To make (12) causal, we can use the ICM Principle, i.e.,           transferring modules across substantially different domains.
we should make the Ui statistically independent, and we                     c) Problem 3 – Learning Interventional World Models and
should make the mechanisms independent. This could be done            Reasoning: Deep learning excels at learning representations of
by ensuring that they are invariant across problems, exhibit          data that preserve relevant statistical properties [23, 148]. How-
sparse changes to actions, or that they can be independently          ever, it does so without taking into account the causal properties
intervened upon [221, 21, 29]. Locatello et al. [159] showed          of the variables, i.e., it does not care about the interventional
that the sparse mechanism shift hypothesis stated above               properties of the variables it analyzes or reconstructs. Causal
is theoretically sufficient when given suitable training data.        representation learning should move beyond the representation
Further, the SMS hypothesis can be used as supervision signal         of statistical dependence structures towards models that support
in practice even if PAi 6= ∅ [252]. However, which factors of         intervention, planning, and reasoning, realizing Konrad Lorenz’
variation can be disentangled depend on which interventions           notion of thinking as acting in an imagined space [163].
can be observed [230, 159]. As discussed by Schölkopf et al.          This ultimately requires the ability to reflect back on one’s
[220], Shu et al. [230], different supervision signals may be         actions and envision alternative scenarios, possibly necessitating
used to identify subsets of factors. Similarly, when learning         (the illusion of) free will [184]. The biological function of
causal variables from data, which variables can be extracted and      self-consciousness may be related to the need for a variable
their granularity depends on which distribution shifts, explicit      representing oneself in one’s Lorenzian imagined space, and
interventions, and other supervision signals are available.           free will may then be a means to communicate about actions
      b) Problem 2 – Learning Transferable Mechanisms: An             taken by that variable, crucial for social and cultural learning,
artificial or natural agent in a complex world is faced with          a topic which has not yet entered the stage of machine learning
limited resources. This concerns training data, i.e., we only have    research although it is at the core of human intelligence [107].
limited data for each task/domain, and thus need to find ways
of pooling/re-using data, in stark contrast to the current industry          VII. I MPLICATIONS FOR M ACHINE L EARNING
practice of large-scale labeling work done by humans. It also
concerns computational resources: animals have constraints on            All of this discussion calls for a learning paradigm that does
the size of their brains, and evolutionary neuroscience knows         not rest on the usual i.i.d. assumption. Instead, we wish to
many examples where brain regions get re-purposed. Similar            make a weaker assumption: that the data on which the model
constraints on size and energy apply as ML methods get em-            will be applied comes from a possibly different distribution,
bedded in (small) physical devices that may be battery-powered.       but involving (mostly) the same causal mechanisms [188]. This
Future AI models that robustly solve a range of problems in the       raises serious challenges: (a) in many cases, we need to infer
real world will thus likely need to re-use components, which          abstract causal variables from the available low-level input
requires them to be robust across tasks and environments [220].       features; (b) there is no consensus on which aspects of the
An elegant way to do this is to employ a modular structure            data reveal causal relations; (c) the usual experimental protocol
that mirrors a corresponding modularity in the world. In other        of training and test set may not be sufficient for inferring and
words, if the world is indeed modular, in the sense that com-         evaluating causal relations on existing data sets, and we may
ponents/mechanisms of the world play roles across a range of          need to create new benchmarks, for example with access to
environments, tasks, and settings, then it would be prudent for       environment information and interventions; (d) even in the
a model to employ corresponding modules [84]. For instance,           limited cases we understand, we often lack scalable and numer-
if variations of natural lighting (the position of the sun, clouds,   ically sound algorithms. Despite these challenges, we argue
etc.) imply that the visual environment can appear in brightness      this endeavor has concrete implications for machine learning
conditions spanning several orders of magnitude, then visual          and may shed light on desiderata and current practices alike.
processing algorithms in our nervous system should employ
methods that can factor out these variations, rather than building    A. Semi-Supervised Learning (SSL)
separate sets of face recognizers, say, for every lighting condi-
tion. If, for example, our nervous system were to compensate            Suppose our underlying causal graph is X → Y , and at the
for the lighting changes by a gain control mechanism, then this       same time we are trying to learn a mapping X → Y . The
mechanism in itself need not have anything to do with the physi-      causal factorization (4) for this case is
cal mechanisms bringing about brightness differences. However,                          P (X, Y ) = P (X)P (Y |X).                  (13)
it would play a role in a modular structure that corresponds to
the role that the physical mechanisms play in the world’s modu-       The ICM Principle posits that the modules in a joint distribu-
lar structure. This could produce a bias towards models that ex-      tion’s causal decomposition do not inform or influence each
hibit certain forms of structural homomorphism to a world that        other. This means that in particular, P (X) should contain no
we cannot directly recognize, which would be rather intriguing,       information about P (Y |X), which implies that SSL should be
given that ultimately our brains do nothing but turn neuronal         futile, in as far as it is using additional information about P (X)
signals into other neuronal signals. A sensible inductive bias to     (from unlabelled data) to improve our estimate of P (Y |X = x).
                                                                                                                                                          12



   In the opposite (anticausal) direction (i.e., the direction of phenomenon also shows that the kind of robustness current
prediction is opposite to the causal generative process), however, classifiers exhibit is rather different from the one a human
SSL may be possible. To see this, we refer to Daniušis et al. exhibits. If we knew both robustness measures, we could try to
[49] who define a measure of dependence between input P (X) maximize one while minimizing the other. Current methods can
and conditional P (Y |X).9 Assuming that this measure is zero be viewed as crude approximations to this, effectively modeling
in the causal direction (applying the ICM assumption described the human’s robustness as a mathematically simple set, say, an
in Section IV to the two-variable case), they show that it is lp ball of radius  > 0: they often try to find examples which
strictly positive in the anticausal direction. Applied to SSL in lead to maximal changes in the classifier’s output, subject to
the anticausal direction, this implies that the distribution of the the constraint that they lie in an lp ball in the pixel metric. As
input (now: effect) variable should contain information about we think of a classifier as the approximation of a function, the
the conditional of output (cause) given input, i.e., the quantity large gradients exploited by these attacks are either a property
that machine learning is usually concerned with.                    of this function or a defect of the approximation.
   The study [218] empirically corroborated these predictions,         There are different ways of relating this to causal models. As
thus establishing an intriguing bridge between the structure of described in [188, Section 1.4], different causal models can gen-
learning problems and certain physical properties (cause-effect erate the same statistical pattern recognition model. In one of
direction) of real-world data generating processes. It also led to those, we might provide a writer with a sequence of class labels
a range of follow-up work [279, 266, 280, 77, 114, 281, 32, 96, y, with the instruction to produce a set of corresponding images
263, 243, 195, 152, 156, 153, 167, 204, 115], complementing x. Clearly, intervening on y will impact x, but intervening on
the studies of Bareinboim and Pearl [12, 185], and it inspired a x will not impact y, so this is an anticausal learning problem.
thread of work in the statistics community exploiting invariance In another setting, we might ask the writer to decide for herself
for causal discovery and other tasks [189, 192, 105, 104, 115]. which digits to write, and to record the labels alongside the
   On the SSL side, subsequent developments include further digit (in this case, the classifier would try to predict one effect
theoretical analyses [121, 188, Section 5.1.2] and a form from another one, a situation which we might call a confounded
of conditional SSL [259]. The view of SSL as exploiting one). In a last one, we might provide images to a person, and
dependencies between a marginal P (X) and a non-causal con- ask the person to generate labels by classifying them.
ditional P (Y |X) is consistent with the common assumptions            Let us now assume that we are in the causal setting
employed to justify SSL [44]. The cluster assumption asserts where the causal generative model factorizes into independent
that the labeling function (which is a property of P (Y |X)) components, one of which is (essentially) the classification
should not change within clusters of P (X). The low-density function. As discussed in Section III, when specifying a causal
separation assumption posits that the area where P (Y |X) model, one needs to determine which interventions are allowed,
takes the value of 0.5 should have small P (X); and the and a structural assignment will then, by definition, be valid
semi-supervised smoothness assumption, applicable also to under every possible (allowed) intervention. One may thus
continuous outputs, states that if two points in a high-density expect that if the predictor approximates the causal mechanism
region are close, then so should be the corresponding output that is inherently transferable and robust, adversarial examples
values. Note, moreover, that some of the theoretical results should be harder to find [216, 134].10 Recent work supports this
in the field use assumptions well-known from causal graphs view: it was shown that a possible defense against adversarial
(even if they do not mention causality): the co-training theorem attacks is to solve the anticausal classification problem by
[31] makes a statement about learnability from unlabelled data, modeling the causal generative direction, a method which in
and relies on an assumption of predictors being conditionally vision is referred to as analysis by synthesis [222]. A related
independent given the label, which we would normally expect if defense method proceeds by reconstructing the input using an
the predictors are (only) caused by the label, i.e., an anticausal autoencoder before feeding it to a classifier [95].
setting. This is nicely consistent with the above findings.
                                                                                C. Robustness and Strong Generalization
B. Adversarial Vulnerability                                                       We can speculate that structures composed of autonomous
    One can hypothesize that the causal direction should also                   modules, such as given by a causal factorization (4), should
have an influence on whether classifiers are vulnerable to                      be relatively robust to swapping out or modifying individual
adversarial attacks. These attacks have recently become                         components. Robustness should also play a role when studying
popular, and consist of minute changes to inputs, invisible to a                strategic behavior, i.e., decisions or actions that take into
human observer yet changing a classifier’s output [249]. This is                account the actions of other agents (including AI agents).
related to causality in several ways. First, these attacks clearly              Consider a system that tries to predict the probability of
constitute violations of the i.i.d. assumption that underlies statis-           successfully paying back a credit, based on a set of features.
tical machine learning. If all we want to do is a prediction in an              The set could include, for instance, the current debt of a person,
i.i.d. setting, then statistical learning is fine. In the adversarial           as well as their address. To get a higher credit score, people
setting, however, the modified test examples are not drawn from                 could thus change their current debt (by paying it off), or
the same distribution as the training examples. The adversarial                 they could change their address by moving to a more affluent
   9 Other dependence measures have been proposed for high-dimensional linear     10 Adversarial attacks may still exploit the quality of the (parameterized)
settings and time series [124, 226, 27, 122, 119, 125].                         approximation of a structural equation.
                                                                                                                                        13



neighborhood. The former probably has a positive causal impact        D. Pre-training, Data Augmentation, and Self-Supervision
on the probability of paying back; for the latter, this is less
likely. Thus, we could build a scoring system that is more                 Learning predictive models solving the min-max opti-
robust with respect to such strategic behavior by only using            mization problem of (18) is challenging. We now interpret
causal features as inputs [132].                                        several common techniques in Machine Learning as means of
   To formalize this general intuition, one can consider a form         approximating (18).
of out-of-distribution generalization, which can be optimized              The first approach is enriching the distribution of the
by minimizing the empirical risk over a class of distributions          training set. This does not mean obtaining more examples
induced by a causal model of the data [5, 204, 169, 189,                from P (X, Y ), but training on a richer dataset [244, 53],
218]. To describe this notion, we start by recalling the usual          for example, through pre-training on a huge and diverse
empirical risk minimization setup. We have access to data from          corpus [196, 54, 112, 137, 59, 35, 45, 253]. Since this strategy
a distribution P (X, Y ) and train a predictor g in a hypothesis        is based on standard empirical risk minimization, it can achieve
space H (e.g., a neural network with a certain architecture             stronger generalization in practice only if the new training
predicting Y from X) to minimize the empirical risk R̂                  distribution is sufficiently diverse to contain information about
                                                                        other distributions in PG .
                     g ? = argmin R̂P (X,Y ) (g)                   (14)    The second approach, often coupled with the previous one,
                             g∈H
                                                                        is to rely on data augmentation to increase the diversity of the
where                                                                   data by “augmenting” it through a certain type of artificially
             R̂P (X,Y ) (g) = ÊP (X,Y ) [loss(Y, g(X))] .         (15) generated interventions [9, 234, 140]. For the visual domain,
                                                                        common augmentations include performing transformations
Here, we denote by ÊP (X,Y ) the empirical mean computed such as rotating the image, translating the image by a few
from a sample drawn from P (X, Y ). When we refer to “out-of- pixels, or flipping the image horizontally, etc. The high-level
distribution generalization” we mean having a small expected idea behind data augmentation is to encourage a system to
risk for a different distribution P † (X, Y ):                          learn underlying invariances or symmetries present in the
              OOD
            RP † (X,Y ) (g) = EP † (X,Y ) [loss(Y, g(X))] .        (16) augmented data distribution. For example, in a classifica-
                                                                        tion task, translating the image by a few pixels does not
                                                     OOD
Clearly, the gap between R̂P (X,Y ) (g) and RP        † (X,Y ) (g) will change the class label. One may view it as specifying a
depend on how different the test distribution P † is from the set of interventions E the model should be robust to (e.g.,
training distribution P . To quantify this difference, we call random crops/interpolations/translation/rotations, etc). Instead
environments the collection of different circumstances that of computing the maximum over all distributions in E, one
give rise to the distribution shifts such as locations, times, can relax the problem by sampling from the interventional
experimental conditions, etc. Environments can be modeled in distributions and optimize an expectation over the different
a causal factorization (4) as they can be seen as interventions augmented images on a suitably chosen subset [38], using
on one or several causal variables or mechanisms. As a a search algorithm like reinforcement learning [48] or an
motivating example, one environment may correspond to where algorithm based on density matching [154].
a measurement is taken (for example a certain room), and from              The third approach is to rely on self-supervision
each environment, we obtain a collection of measurements to learn about P (X). Certain pre-training methods
(images of objects in the same room). It is nontrivial (and [196, 54, 112, 35, 45, 253] have shown that it is possible to
in some cases provably hard [20]) to learn statistical models achieve good results using only very few class labels by first
that are stable across training environments and generalize to pre-training on a large unlabeled dataset and then fine-tuning
novel testing environments [189, 204, 167, 5, 2] drawn from on few labeled examples. Similarly, pre-training on large
the same environment distribution.                                      unlabeled image datasets can improve performance by learning
   Using causal language, one could restrict P † (X, Y ) to be representations that can efficiently transfer to a downstream
the result of a certain set of interventions, i.e., P † (X, Y ) ∈ PG task, as demonstrated by [179, 110, 102, 46, 92]. These
where PG is a set of interventional distributions over a causal methods fall under the umbrella of self-supervised learning, a
graph G. The worst case out-of-distribution risk then becomes           family of techniques for converting an unsupervised learning
                                                                        problem into a supervised one by using so-called pretext tasks
       RPOOD   (g) = max EP † (X,Y ) [loss(Y, g(X))] .             (17)
           G             †
                       P ∈PG                                            with  artificially generated labels without human annotations.
                                                                        The basic idea behind using pretext tasks is to force the
To learn a robust predictor, we should have available a subset
                                                                        learner to learn representations that contain information about
of environment distributions E ⊂ PG and solve
                                                                        P (X) that may be useful for (an unknown) downstream task.
       g ? = argmin max ÊP † (X,Y ) [loss(Y, g(X))] .             (18) Much of the work on methods that use self-supervision relies
                g∈H P † ∈E                                              on carefully constructing pretext tasks. A central challenge
In practice, solving (18) requires specifying a causal model here is to extract features that are indeed informative about
with an associated set of interventions. If the set of observed the data generating distribution. Ideas from the ICM Principle
environments E does not coincide with the set of possible could help develop methods that can automate the process of
environments PG , we have an additional estimation error that constructing pretext tasks. Finally, one can explicitly optimize
may be arbitrarily large in the worst case [5, 20].                     (18), for example, through adversarial training [79]. In that case,
                                                                                                                                    14



PG would contain a set of attacks an adversary might perform,        learn invariances in a causal graph structure. A key requirement
while presently, we consider a set of natural interventions.         to learn invariances from data may be the possibility to
   An interesting research direction is the combination of all       perform and learn from interventions. Work in developmental
these techniques, large scale training, data augmentation, self-     psychology argues that there is a need to experiment in order
supervision, and robust fine-tuning on the available data from       to discover causal relationships [80]. This can be modelled
multiple, potentially simulated environments.                        as an RL environment, where the agent can discover causal
                                                                     factors through interventions and observing their effects.
E. Reinforcement Learning                                            Further, causal models may allow to model the environment as
                                                                     a set of underlying independent causal mechanisms such that,
   Reinforcement Learning (RL) is closer to causality research
                                                                     if there is a change in distribution, not all the mechanisms need
than the machine learning mainstream in that it sometimes
                                                                     to be re-learned. However, there are still open questions about
effectively directly estimates do-probabilities. E.g., on-policy
                                                                     the right way to think about generalization in RL, the right
learning estimates do-probabilities for the interventions speci-
                                                                     way to formalize the problem, and the most relevant tasks.
fied by the policy (note that these may not be hard interventions
                                                                           c) Counterfactuals: Counterfactual reasoning has been
if the policy depends on other variables). However, as soon as
                                                                     found to improve the data efficiency of RL algorithms [37, 165],
off-policy learning is considered, in particular in the batch (or
                                                                     improve performance [50], and it has been applied to communi-
observational) setting [146], issues of causality become subtle
                                                                     cate about past experiences in the multi-agent setting [68, 241].
[164, 81]. An emerging line of work devoted to the intersection
                                                                     These findings are consistent with work in cognitive psychology
of RL and causality includes [13, 21, 164, 37, 50, 275, 1].
                                                                     [64], arguing that counterfactuals allow to reason about the use-
Causal learning applied to reinforcement learning can be
                                                                     fulness of past actions and transfer these insights to correspond-
divided into two aspects, causal induction and causal inference.
                                                                     ing behavioral intentions in future scenarios [203, 199, 145].
Causal induction (discovery) involves learning causal relations
                                                                        We argue that future work in RL should consider coun-
from data, for example, an RL agent learning a causal model of
                                                                     terfactual reasoning as a critical component to enable acting
the environment. Causal inference learns to plan and act based
                                                                     in imagined spaces and formulating hypotheses that can be
on a causal model. Causal induction in an RL setting poses
                                                                     subsequently tested with suitably chosen interventions.
different challenges than the classic causal learning settings
                                                                           d) Offline RL: The success of deep learning methods in
where the causal variables are often given. However, there is
                                                                     the case of supervised learning can be largely attributed to
accumulating evidence supporting the usefulness of an appro-
                                                                     the availability of large datasets and methods that can scale to
priate structured representation of the environment [2, 26, 258].
                                                                     large amounts of data. In the case of reinforcement learning,
                                                                     collecting large amounts of high-fidelity diverse data from
      a) World Models: Model-based RL [248, 67] is                   scratch can be expensive and hence becomes a bottleneck.
related to causality as it aims at modeling the effect of            Offline RL [72, 150] tries to address this concern by learning a
actions (interventions) on the current state of the world.           policy from a fixed dataset of trajectories, without requiring any
Particularly relevant for causal leaning are generative              experimental or interventional data (i.e., without any interaction
world models that capture some of the causal relations               with the environment). The effective use of observational data
underlying the environment and serve as Lorenzian                    (or logged data) may make real-world RL more practical by
imagined spaces (see I NTRODUCTION above) to train RL                incorporating diverse prior experiences. To succeed at it, an
agents [127, 248, 98, 47, 271, 178, 232, 214, 268]. Structured       agent should be able to infer the consequence of different sets of
generative approaches further aim at decomposing an                  actions compared to those seen during training (i.e., the actions
environment into multiple entities with causally correct relations   in the logged data), which essentially makes it a counterfactual
among them, modulo the completeness of the variables, and            inference problem. The distribution mismatch between the
confounding [58, 265, 43, 264, 14, 136]. However, many of            current policy and the policy that was used to collect offline
the current approaches (regardless of structure), only build         data makes offline RL challenging as this requires us to move
partial models of the environment [88]. Since they do not            well beyond the assumption of independently and identically
observe the environment at every time step, the environment          distributed data. Incorporating invariances, by factorizing
may become an unobserved confounder affecting both the               knowledge in terms of independent causal mechanisms can
agent’s actions and the reward. To address this issue, a model       help make progress towards the offline RL setting.
can use the backdoor criterion conditioning on its policy [200].
      b) Generalization, Robustness, and Fast Transfer:
While RL has already achieved impressive results, the sample         F. Scientific Applications
complexity required to achieve consistently good performance           A fundamental question in the application of machine learn-
is often prohibitively high. Further, RL agents are often brittle    ing in natural sciences is to which extent we can complement
(if data is limited) in the face of even tiny changes to the         our understanding of a physical system with machine learning.
environment (either visual or mechanistic changes) unseen in         One interesting aspect is physics simulation with neural
the training phase. The question of generalization in RL is          networks [93], which can substantially increase the efficiency
essential to the field’s future both in theory and practice. One     of hand-engineered simulators [103, 143, 269, 211, 264].
proposed solution towards the goal of designing machines that        Significant out-of-distribution generalization of learned physical
can extrapolate experience across environments and tasks is to       simulators may not be necessary if experimental conditions are
                                                                                                                                    15



carefully controlled, although the simulator has to be completely       At the same time, we have clearly come a long way already
re-trained if the conditions change.                                 without explicitly treating the multi-task problem as a causal
   On the other hand, the lack of systematic experimental            one. Fuelled by abundant data and compute, AI has made re-
conditions may become problematic in other applications such         markable advances in a wide range of applications, from image
as healthcare. One example is personalized medicine, where           processing and natural language processing [35] to beating
we may wish to build a model of a patient health state through       human world champions in games such as chess, poker and
a multitude of data sources, like electronic health records and      Go [223], improving medical diagnoses [166], and generating
genetic information [65, 108]. However, if we train a clinical       music [56]. A critical question thus arises: “Why can’t we just
system on doctors’ actions in controlled settings, the system        train a huge model that learns environments’ dynamics (e.g.
will likely provide little additional insight compared to the        in a RL setting) including all possible interventions? After all,
doctors’ knowledge and may fail in surprising ways when              distributed representations can generalize to unseen examples
deployed [18]. While it may be useful to automate certain            and if we train over a large number of interventions we may
decisions, an understanding of causality may be necessary            expect that a big neural network will generalize across them”.
to recommend treatment options that are personalized and             To address this, we make several points. To begin with, if data
reliable [201, 242, 224, 273, 6, 3, 30, 165].                        was not sufficiently diverse (which is an untestable assumption
   Causality also has significant potential in helping understand    a priori), the worst-case error to unseen shifts may still be
medical phenomena, e.g., in the current Covid-19 pandemic,           arbitrarily high (see Section VII-C). While in the short term,
where causal mediation analysis helps disentangle different          we can often beat “out-of-distribution” benchmarks by training
effects contributing towards case fatality rates when a textbook     bigger models on bigger datasets, causality offers an important
example of Simpson’s paradox was observed [261].                     complement. The generalization capabilities of a model are tied
   Another example of a scientific application is in astronomy,      to its assumptions (e.g., how the model is structured and how
where causal models were used to identify exoplanets under the       it was trained). The causal approach makes these assumptions
confounding of the instrument. Exoplanets are often detected         more explicit and aligned with our understanding of physics and
as they partially occlude their host star when they transit in       human cognition, for instance by relying on the Independent
front of it, causing a slight decrease in brightness. Shared         Causal Mechanisms principle. When these assumptions are
patterns in measurement noise across stars light-years apart         valid, a learner that does not use them should fare worse than
can be removed in order to reduce the instrument’s influence         one that does. Further, if we had a model that was successful
on the measurement [219], which is critical especially in the        in all interventions over a certain environment, we may want
context of partial technical failures as experienced in the Kepler   to use it in different environments that share similar albeit not
exoplanet search mission. The application of [219] lead to the       necessarily identical dynamics. The causal approach, and in
discovery of 36 planet candidates [70], of which 21 were             particular the ICM principle, point to the need to decompose
subsequently validated as bona fide exoplanets [172]. Four           knowledge about the world into independent and recomposable
years later, astronomers found traces of water in the atmosphere     pieces (recomposable depending on the interventions or changes
of the exoplanet K2-18b — the first such discovery for an            in environment), which suggests more work on modular ML
exoplanet in the habitable zone, i.e., allowing for liquid water     architectures and other ways to enforce the ICM principle in
[25, 254]. This planet turned out to be one that had first been      future ML approaches.
detected in [70, exoplanet candidate EPIC 201912552].                   At its core, i.i.d. pattern recognition is but a mathematical
                                                                     abstraction, and causality may be essential to most forms of
G. Multi-Task Learning and Continual Learning                        animate learning. Until now, machine learning has neglected a
   State-of-the-art AI is relatively narrow, i.e., trained to        full integration of causality, and this paper argues that it would
perform specific tasks, as opposed to the broad, versatile           indeed benefit from integrating causal concepts. We argue
intelligence allowing humans to adapt to a wide range of             that combining the strengths of both fields, i.e., current deep
environments and develop a rich set of skills. The human             learning methods as well as tools and ideas from causality, may
ability to discover robust, invariant high-level concepts and        be a necessary step on the path towards versatile AI systems.
abstractions, and to identify causal relationships from obser-
vations appears to be one of the key factors allowing for a
                                                                                       VIII. C ONCLUSION
successful generalization from prior experiences to new, often
quite different, “out-of-distribution” settings.                    In this work, we discussed different levels of models, includ-
   Multi-task learning refers to building a system that can solve ing causal and statistical ones. We argued that this spectrum
multiple tasks across different environments [40, 209]. These builds upon a range of assumptions both in terms of modeling
tasks usually share some common traits. By learning similarities and data collection. In an effort to bring together causality
across tasks, a system could utilize knowledge acquired from and machine learning research programs, we first presented a
previous tasks more efficiently when encountering a new task. discussion on the fundamentals of causal inference. Second,
One possibility of learning such similarities across tasks is we discussed how the independent mechanism assumptions
to learn a shared underlying data-generating process as a and related notions such as invariance offer a powerful bias for
causal generative model whose components satisfy the SMS causal learning. Third, we discussed how causal relations might
hypothesis [220]. In certain cases, causal models adapt faster be learned from observational and interventional data when
to sparse interventions in distribution [131, 194].               causal variables are observed. Fourth, we discussed the open
                                                                                                                                      16



problem of causal representation learning, including its relation is important for causal induction in real-world reinforcement
to recent interest in the concept of disentangled representations learning settings. Moreover, building a causal description
in deep learning. Finally, we discussed how some open for both a model of the agent and the environment (world
research questions in the machine learning community may models) should be essential for robust and versatile model-
be better understood and tackled within the causal framework, based reinforcement learning.
including semi-supervised learning, domain generalization, and
adversarial robustness.                                                               IX. ACKNOWLEDGMENTS
   Based on this discussion, we list some critical areas for
future research:                                                       Many thanks to the past and present members of the Tübin-
      a) Learning Non-Linear Causal Relations at Scale: Not         gen causality team, without whose work and insights this article
all real-world data is unstructured and the effect of interventions would not exist, in particular to Dominik Janzing, Chaochao
can often be observed, for example, by stratifying the data Lu and Julius von Kügelgen who gave helpful comments on
collection across multiple environments. The approximation [221]. The text has also benefitted from discussions with
abilities of modern machine learning methods may prove Elias Bareinboim, Christoph Bohle, Leon Bottou, Isabelle
useful to model non-linear causal relations among large Guyon, Judea Pearl, and Vladimir Vapnik. Thanks to Wouter
numbers of variables. For practical applications, classical van Amsterdam for pointing out typos in the first version.
tools are not only limited in the linearity assumptions often We also thank Thomas Kipf, Klaus Greff, and Alexander
made but also in their scalability. The paradigms of meta- d’Amour for the useful discussions. Finally, we thank the
and multi-task learning are close to the assumptions and thorough anonymous reviewers for highly valuable feedback
desiderata of causal modeling, and future work should consider and suggestions.
(1) understanding under which conditions non-linear causal
relations can be learned, (2) which training frameworks allow to                              R EFERENCES
best exploit the scalability of machine learning approaches, and      [1] Ossama Ahmed, Frederik Träuble, Anirudh Goyal, Alexander
(3) providing compelling evidence on the advantages over (non-            Neitz, Manuel Wuthrich, Yoshua Bengio, Bernhard Schölkopf,
causal) statistical representations in terms of generalization, re-       and Stefan Bauer. Causalworld: A robotic manipulation
                                                                          benchmark for causal structure and transfer learning. In
purposing, and transfer of causal modules on real-world tasks.            International Conference on Learning Representations, 2021.
      b) Learning Causal Variables: “Disentangled” represen-          [2] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej, Mateusz
tations learned by state-of-the-art neural network methods                Litwin, Bob McGrew, Arthur Petron, Alex Paino, Matthias
are still distributed in the sense that they are represented in           Plappert, Glenn Powell, Raphael Ribas, et al. Solving rubik’s
a vector format with an arbitrary ordering in the dimensions.             cube with a robot hand. arXiv preprint 1910.07113, 2019.
                                                                      [3] Ahmed Alaa and Mihaela Schaar. Limits of estimating hetero-
This fixed-format implies that the representation size cannot             geneous treatment effects: Guidelines for practical algorithm
be dynamically changed; for example, we cannot change the                 design. In International Conference on Machine Learning,
number of objects in a scene. Further, structured and modular             pages 129–138, 2018.
representation should also arise when a network is trained            [4] J. Aldrich. Autonomy. Oxford Economic Papers, 41:15–34,
for (sets of) specific tasks, not only auteoncoding. Different            1989.
                                                                      [5] Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and David
high-level variables may be extracted depending on the task               Lopez-Paz. Invariant risk minimization. arXiv preprint
and affordances at hand. Understanding under which conditions             1907.02893, 2019.
causal variables can be recovered could provide insights into         [6] Onur Atan, James Jordon, and Mihaela van der Schaar.
which interventions we are robust to in predictive tasks.                 Deep-treat: Learning optimal personalized treatments from
      c) Understanding the Biases of Existing Deep Learning               observational data using neural networks. In Thirty-Second
                                                                          AAAI Conference on Artificial Intelligence, 2018.
Approaches: Scaling to massive data sets, relying on data             [7] Aharon Azulay and Yair Weiss. Why do deep convolutional
augmentation and self-supervision have all been successfully              networks generalize so poorly to small image transformations?
explored to improve the robustness of the predictions of deep             Journal of Machine Learning Research, 20(184):1–25, 2019.
learning models. It is nontrivial to disentangle the benefits of      [8] Dzmitry Bahdanau, Shikhar Murty, Michael Noukhovitch,
the individual components and it is often unclear which “trick”           Thien Huu Nguyen, Harm de Vries, and Aaron Courville.
                                                                          Systematic generalization: what is required and can it be
should be used when dealing with a new task, even if we have              learned? arXiv preprint 1811.12889, 2018.
an intuition about useful invariances. The notion of strong           [9] H. Baird. Document image defect models. In Proc., IAPR
generalization over a specific set of interventions may be used           Workshop on Syntactic and Structural Pattern Recognition,
to probe existing methods, training schemes, and datasets in              pages 38–46, Murray Hill, NJ, 1990.
order to build a taxonomy of inductive biases. In particular, it     [10] Victor Bapst, Alvaro Sanchez-Gonzalez, Carl Doersch, Kim-
                                                                          berly Stachenfeld, Pushmeet Kohli, Peter Battaglia, and Jessica
is desirable to understand how design choices in pre-training             Hamrick. Structured agents for physical construction. In
(e.g., which datasets/tasks) positively impact both transfer and          International Conference on Machine Learning, pages 464–
robustness downstream in a causal sense.                                  474, 2019.
      d) Learning Causally Correct Models of the World and the       [11] Andrei Barbu, David Mayo, Julian Alverio, William Luo,
Agent: In many real-world reinforcement learning (RL) settings,           Christopher Wang, Dan Gutfreund, Josh Tenenbaum, and Boris
                                                                          Katz. Objectnet: A large-scale bias-controlled dataset for
abstract state representations are not available. Hence, the              pushing the limits of object recognition models. In Advances
ability to derive abstract causal variables from high-dimensional,        in Neural Information Processing Systems, pages 9448–9458,
low-level pixel representations and then recover causal graphs            2019.
                                                                                                                                             17



[12] E. Bareinboim and J. Pearl. Transportability from multiple           [28] M. Besserve, R. Sun, D. Janzing, and B. Schölkopf. A theory of
     environments with limited experiments: Completeness results.              independent mechanisms for extrapolation in generative models.
     In Advances in Neural Information Processing Systems 27,                  In 35th AAAI Conference on Artificial Intelligence: A Virtual
     pages 280–288, 2014.                                                      Conference, February 2021.
[13] E. Bareinboim, A. Forney, and J. Pearl. Bandits with unobserved      [29] Michel Besserve, Rémy Sun, and Bernhard Schölkopf. Coun-
     confounders: A causal approach. In Advances in Neural                     terfactuals uncover the modular structure of deep generative
     Information Processing Systems 28, pages 1342–1350, 2015.                 models. arXiv preprint 1812.03253, published at ICLR 2020,
[14] Peter Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez              2018.
     Rezende, et al. Interaction networks for learning about objects,     [30] Ioana Bica, Ahmed M Alaa, and Mihaela van der Schaar. Time
     relations and physics. In Advances in neural information                  series deconfounder: Estimating treatment effects over time in
     processing systems, pages 4502–4510, 2016.                                the presence of hidden confounders. arXiv preprint 1902.00450,
[15] Peter W Battaglia, Jessica B Hamrick, and Joshua B Tenenbaum.             2019.
     Simulation as an engine of physical scene understanding.             [31] Avrim Blum and Tom Mitchell. Combining labeled and
     Proceedings of the National Academy of Sciences, 110(45):                 unlabeled data with co-training. In Proceedings of the Eleventh
     18327–18332, 2013.                                                        Annual Conference on Computational Learning Theory, pages
[16] Peter W Battaglia, Jessica B Hamrick, Victor Bapst, Alvaro                92–100, New York, NY, USA, 1998. ACM.
     Sanchez-Gonzalez, Vinicius Zambaldi, Mateusz Malinowski,             [32] Patrick Blöbaum, Takashi Washio, and Shohei Shimizu. Error
     Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner,              asymmetry in causal and anticausal regression. arXiv preprint
     et al. Relational inductive biases, deep learning, and graph              1610.03263, 2016.
     networks. arXiv preprint 1806.01261, 2018.                           [33] Blai Bonet and Hector Geffner. Learning first-order symbolic
[17] S. Bauer, B. Schölkopf, and J. Peters. The arrow of time                  representations for planning from the structure of the state
     in multivariate time series. In Proceedings of the 33nd                   space. arXiv preprint 1909.05546, 2019.
     International Conference on Machine Learning, volume 48              [34] L. Bottou, J. Peters, J. Quiñonero-Candela, D. X. Charles, D. M.
     of JMLR Workshop and Conference Proceedings, pages 2043–                  Chickering, E. Portugualy, D. Ray, P. Simard, and E. Snelson.
     2051, 2016.                                                               Counterfactual reasoning and learning systems: The example
[18] Emma Beede, Elizabeth Baylor, Fred Hersch, Anna Iurchenko,                of computational advertising. Journal of Machine Learning
     Lauren Wilcox, Paisan Ruamviboonsuk, and Laura M Var-                     Research, 14:3207–3260, 2013.
     doulakis. A human-centered evaluation of a deep learning             [35] Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah,
     system deployed in clinics for the detection of diabetic                  Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav
     retinopathy. In Proceedings of the 2020 CHI Conference on                 Shyam, Girish Sastry, Amanda Askell, et al. Language models
     Human Factors in Computing Systems, pages 1–12, 2020.                     are few-shot learners. arXiv preprint 2005.14165, 2020.
[19] Sara Beery, Grant Van Horn, and Pietro Perona. Recognition           [36] Kailash Budhathoki and Jilles Vreeken. Causal inference by
     in terra incognita. In Proceedings of the European Conference             compression. In IEEE 16th International Conference on Data
     on Computer Vision (ECCV), pages 456–473, 2018.                           Mining, 2016.
[20] S. Ben-David, T. Lu, T. Luu, and D. Pál. Impossibility               [37] Lars Buesing, Theophane Weber, Yori Zwols, Sebastien
     theorems for domain adaptation. In Proceedings of the                     Racaniere, Arthur Guez, Jean-Baptiste Lespiau, and Nicolas
     International Conference on Artificial Intelligence and Statistics        Heess. Woulda, coulda, shoulda: Counterfactually-guided policy
     13 (AISTATS), pages 129–136, 2010.                                        search. arXiv preprint 1811.06272, 2018.
[21] Emmanuel Bengio, Valentin Thomas, Joelle Pineau, Doina               [38] C. J. C. Burges and B. Schölkopf. Improving the accuracy and
     Precup, and Yoshua Bengio. Independently controllable features.           speed of support vector learning machines. In M. Mozer,
     arXiv preprint 1703.07718, 2017.                                          M. Jordan, and T. Petsche, editors, Advances in Neural
[22] Yoshua Bengio, Samy Bengio, and Jocelyn Cloutier. Learning                Information Processing Systems, volume 9, pages 375–381,
     a synaptic learning rule. IJCNN-91-Seattle International Joint            Cambridge, MA, USA, 1997. MIT Press.
     Conference on Neural Networks (Vol. 2, pp. 969-vol). IEEE.,          [39] Christopher P Burgess, Loic Matthey, Nicholas Watters,
     1990.                                                                     Rishabh Kabra, Irina Higgins, Matt Botvinick, and Alexander
[23] Yoshua Bengio, Aaron Courville, and Pascal Vincent. Rep-                  Lerchner. Monet: Unsupervised scene decomposition and
     resentation learning: A review and new perspectives. arXiv                representation. arXiv preprint 1901.11390, 2019.
     preprint 1206.5538, 2012.                                            [40] Rich Caruana. Multitask learning. Machine learning, 28(1):
[24] Yoshua Bengio, Tristan Deleu, Nasim Rahaman, Rosemary                     41–75, 1997.
     Ke, Sébastien Lachapelle, Olexa Bilaniuk, Anirudh Goyal, and         [41] Krzysztof Chalupka, Pietro Perona, and Frederick Eberhardt.
     Christopher Pal. A meta-transfer objective for learning to                Multi-level cause-effect systems. arXiv preprint 1512.07942,
     disentangle causal mechanisms. arXiv preprint 1901.10912,                 2015.
     2019.                                                                [42] Krzysztof Chalupka, Pietro Perona, and Frederick Eberhardt.
[25] Björn Benneke, Ian Wong, Caroline Piaulet, Heather A.                     Fast conditional independence test for vector variables with
     Knutson, Ian J. M. Crossfield, Joshua Lothringer, Caroline V.             large sample sizes. arXiv preprint 1804.02747, 2018.
     Morley, Peter Gao, Thomas P. Greene, Courtney Dressing,              [43] Michael B Chang, Tomer Ullman, Antonio Torralba, and
     Diana Dragomir, Andrew W. Howard, Peter R. McCullough,                    Joshua B Tenenbaum. A compositional object-based approach
     Eliza M. R. Kempton Jonathan J. Fortney, and Jonathan Fraine.             to learning physical dynamics. In 5th International Conference
     Water vapor on the habitable-zone exoplanet K2-18b. arXiv                 on Learning Representations (ICLR), 2017.
     preprint 1909.04642, 2019.                                           [44] O. Chapelle, B. Schölkopf, and A. Zien, editors. Semi-
[26] Christopher Berner, Greg Brockman, Brooke Chan, Vicki                     Supervised Learning. MIT Press, Cambridge, MA, USA, 2006.
     Cheung, Przemysław Dkebiak, Christy Dennison, David Farhi,                URL http://www.kyb.tuebingen.mpg.de/ssl-book/.
     Quirin Fischer, Shariq Hashme, Chris Hesse, et al. Dota 2            [45] Mark Chen, Alec Radford, Rewon Child, Jeff Wu, Heewoo Jun,
     with large scale deep reinforcement learning. arXiv preprint              Prafulla Dhariwal, David Luan, and Ilya Sutskever. Generative
     1912.06680, 2019.                                                         pretraining from pixels. In Proceedings of the 37th International
[27] M. Besserve, N. Shajarisales, B. Schölkopf, and D. Janzing.               Conference on Machine Learning, 2020.
     Group invariance principles for causal generative models. In         [46] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geof-
     Proceedings of the 21st International Conference on Artificial            frey Hinton. A simple framework for contrastive learning of
     Intelligence and Statistics (AISTATS), pages 557–565, 2018.               visual representations. arXiv preprint 2002.05709, 2020.
                                                                                                                                           18



[47] Silvia Chiappa, Sébastien Racaniere, Daan Wierstra, and                   Volodymyr Kuleshov, Mark DePristo, Katherine Chou, Claire
     Shakir Mohamed. Recurrent environment simulators. In 5th                  Cui, Greg Corrado, Sebastian Thrun, and Jeff Dean. A guide
     International Conference on Learning Representations (ICLR),              to deep learning in healthcare. Nature Medicine, 25(1):24–29,
     2017.                                                                     2019.
[48] Ekin D Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan,          [66] András Faragó and Gábor Lugosi. Strong universal consistency
     and Quoc V Le. Autoaugment: Learning augmentation                         of neural network classifiers. IEEE Transactions on Information
     strategies from data. In Proceedings of the IEEE conference               Theory, 39(4):1146–1151, 2006.
     on computer vision and pattern recognition, pages 113–123,           [67] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-
     2019.                                                                     agnostic meta-learning for fast adaptation of deep networks.
[49] P. Daniušis, D. Janzing, J. M. Mooij, J. Zscheischler, B. Steudel,        arXiv preprint 1703.03400, 2017.
     K. Zhang, and B. Schölkopf. Inferring deterministic causal           [68] Jakob N Foerster, Gregory Farquhar, Triantafyllos Afouras,
     relations. In Proceedings of the 26th Annual Conference on                Nantas Nardelli, and Shimon Whiteson. Counterfactual multi-
     Uncertainty in Artificial Intelligence (UAI), pages 143–150,              agent policy gradients. In Thirty-second AAAI conference on
     2010.                                                                     artificial intelligence, 2018.
[50] Ishita Dasgupta, Jane Wang, Silvia Chiappa, Jovana Mitrovic,         [69] Peter Földiák. Learning invariance from transformation
     Pedro Ortega, David Raposo, Edward Hughes, Peter Battaglia,               sequences. Neural Computation, 3(2):194–200, 1991.
     Matthew Botvinick, and Zeb Kurth-Nelson. Causal reasoning            [70] D. Foreman-Mackey, B. T. Montet, D. W. Hogg, T. D. Morton,
     from meta-reinforcement learning. arXiv preprint 1901.08162,              D. Wang, and B. Schölkopf. A systematic search for transiting
     2019.                                                                     planets in the K2 data. The Astrophysical Journal, 806(2),
[51] A. P. Dawid. Conditional independence in statistical theory.              2015. URL http://stacks.iop.org/0004-637X/806/i=2/a=215.
     Journal of the Royal Statistical Society B, 41(1):1–31, 1979.        [71] R. Frisch, T. Haavelmo, T.C. Koopmans, and J. Tinbergen.
[52] Stanislas Dehaene. How We Learn: Why Brains Learn Better                  Autonomy of economic relations. Universitets Socialøkonomiske
     Than Any Machine... for Now. Penguin, 2020.                               Institutt, Oslo, Norway, 1948.
[53] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and           [72] Scott Fujimoto, David Meger, and Doina Precup. Off-
     Li Fei-Fei. Imagenet: A large-scale hierarchical image database.          policy deep reinforcement learning without exploration. In
     In 2009 IEEE conference on computer vision and pattern                    International Conference on Machine Learning, pages 2052–
     recognition, pages 248–255. Ieee, 2009.                                   2062, 2019.
[54] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina               [73] K. Fukumizu, A. Gretton, X. Sun, and B. Schölkopf. Kernel
     Toutanova. Bert: Pre-training of deep bidirectional transformers          measures of conditional dependence. In Advances in Neural
     for language understanding. arXiv preprint 1810.04805, 2018.              Information Processing Systems 20, pages 489–496, 2008.
[55] L. Devroye, L. Györfi, and G. Lugosi. A Probabilistic Theory of      [74] D. Geiger and J. Pearl. Logical and algorithmic properties
     Pattern Recognition, volume 31 of Applications of Mathematics.            of independence and their application to Bayesian networks.
     Springer, New York, NY, 1996.                                             Annals of Mathematics and Artificial Intelligence, 2:165–178,
[56] Prafulla Dhariwal, Heewoo Jun, Christine Payne, Jong Wook                 1990.
     Kim, Alec Radford, and Ilya Sutskever. Jukebox: A generative         [75] Robert Geirhos, Patricia Rubisch, Claudio Michaelis, Matthias
     model for music. arXiv preprint 2005.00341, 2020.                         Bethge, Felix A Wichmann, and Wieland Brendel. Imagenet-
[57] Andrea Dittadi, Frederik Träuble, Francesco Locatello, Manuel             trained cnns are biased towards texture; increasing shape bias
     Wüthrich, Vaibhav Agrawal, Ole Winther, Stefan Bauer, and                 improves accuracy and robustness. arXiv preprint 1811.12231,
     Bernhard Schölkopf. On the transfer of disentangled repre-                2018.
     sentations in realistic settings. In International Conference on     [76] Muhammad Waleed Gondal, Manuel Wüthrich, Djordje Miladi-
     Learning Representations, 2021.                                           nović, Francesco Locatello, Martin Breidt, Valentin Volchkov,
[58] Carlos Diuk, Andre Cohen, and Michael L Littman. An object-               Joel Akpo, Olivier Bachem, Bernhard Schölkopf, and Stefan
     oriented representation for efficient reinforcement learning. In          Bauer. On the transfer of inductive bias from simulation to
     Proceedings of the 25th international conference on Machine               the real world: a new disentanglement dataset. In Advances in
     learning, pages 240–247, 2008.                                            Neural Information Processing Systems, pages 15740–15751,
[59] Josip Djolonga, Jessica Yung, Michael Tschannen, Rob Romi-                2019.
     jnders, Lucas Beyer, Alexander Kolesnikov, Joan Puigcerver,          [77] M. Gong, K. Zhang, T. Liu, D. Tao, C. Glymour, and
     Matthias Minderer, Alexander D’Amour, Dan Moldovan, et al.                B. Schölkopf. Domain adaptation with conditional transfer-
     On robustness and transferability of convolutional neural                 able components. In Proceedings of the 33nd International
     networks. arXiv preprint 2007.08558, 2020.                                Conference on Machine Learning, pages 2839–2848, 2016.
[60] G. Doran, K. Muandet, K. Zhang, and B. Schölkopf. A                  [78] M. Gong, K. Zhang, B. Schölkopf, C. Glymour, and D. Tao.
     permutation-based kernel conditional independence test. In                Causal discovery from temporally aggregated time series. In
     N. L. Zhang and J. Tian, editors, Proceedings of the 30th                 Proceedings of the Thirty-Third Conference on Uncertainty in
     Conference on Uncertainty in Artificial Intelligence, pages               Artificial Intelligence (UAI), page ID 269, 2017.
     132–141, Corvallis, OR, 2014. AUAI Press. URL http:                  [79] Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy.
     //auai.org/uai2014/proceedings/individuals/194.pdf.                       Explaining and harnessing adversarial examples. arXiv preprint
[61] Cian Eastwood and Christopher KI Williams. A framework for                1412.6572, 2014.
     the quantitative evaluation of disentangled representations. In      [80] Alison Gopnik, Clark Glymour, David M Sobel, Laura E Schulz,
     International Conference on Learning Representations, 2018.               Tamar Kushnir, and David Danks. A theory of causal learning
[62] Daniel Eaton and Kevin Murphy. Exact Bayesian structure                   in children: causal maps and Bayes nets. Psychological review,
     learning from uncertain interventions. In Artificial Intelligence         111(1):3, 2004.
     and Statistics, pages 107–114, 2007.                                 [81] Omer Gottesman, Fredrik Johansson, Joshua Meier, Jack Dent,
[63] Logan Engstrom, Brandon Tran, Dimitris Tsipras, Ludwig                    Donghun Lee, Srivatsan Srinivasan, Linying Zhang, Yi Ding,
     Schmidt, and Aleksander Madry. Exploring the landscape of                 David Wihl, Xuefeng Peng, Jiayu Yao, Isaac Lage, Christopher
     spatial robustness. arXiv preprint 1712.02779, 2017.                      Mosch, Li wei H. Lehman, Matthieu Komorowski, Matthieu
[64] Kai Epstude and Neal J Roese. The functional theory of                    Komorowski, Aldo Faisal, Leo Anthony Celi, David Sontag,
     counterfactual thinking. Personality and social psychology                and Finale Doshi-Velez. Evaluating reinforcement learning
     review, 12(2):168–192, 2008.                                              algorithms in observational health settings. arXiv preprint
[65] Andre Esteva, Alexandre Robicquet, Bharath Ramsundar,                     1805.12298, 2018.
                                                                                                                                            19



 [82] Olivier Goudet, Diviyan Kalainathan, Philippe Caillou, Isabelle          nonlinear ica: Unsupervised learning from nonstationary time
      Guyon, David Lopez-Paz, and Michèle Sebag. Causal genera-                series. arXiv preprint 2006.12107, 2020.
      tive neural networks. arXiv preprint 1711.08936, 2017.             [101] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
 [83] Anirudh Goyal, Alex Lamb, Phanideep Gampa, Philippe                      Deep residual learning for image recognition. In Proceedings
      Beaudoin, Sergey Levine, Charles Blundell, Yoshua Bengio,                of the IEEE conference on computer vision and pattern
      and Michael Mozer. Object files and schemata: Factorizing                recognition, pages 770–778, 2016.
      declarative and procedural knowledge in dynamical systems.         [102] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross
      arXiv preprint 2006.16225, 2020.                                         Girshick. Momentum contrast for unsupervised visual represen-
 [84] Anirudh Goyal, Alex Lamb, Jordan Hoffmann, Shagun Sodhani,               tation learning. In Proceedings of the IEEE/CVF Conference on
      Sergey Levine, Yoshua Bengio, and Bernhard Schölkopf. Re-                Computer Vision and Pattern Recognition, pages 9729–9738,
      current independent mechanisms. In International Conference              2020.
      on Learning Representations, 2021.                                 [103] Siyu He, Yin Li, Yu Feng, Shirley Ho, Siamak Ravanbakhsh,
 [85] Alex Graves, Abdel-rahman Mohamed, and Geoffrey Hinton.                  Wei Chen, and Barnabás Póczos. Learning to predict the
      Speech recognition with deep recurrent neural networks. In               cosmological structure formation. Proceedings of the National
      2013 IEEE international conference on acoustics, speech and              Academy of Sciences, 116(28):13825–13832, 2019.
      signal processing, pages 6645–6649. IEEE, 2013.                    [104] Christina Heinze-Deml and Nicolai Meinshausen. Conditional
 [86] Klaus Greff, Raphaël Lopez Kaufman, Rishabh Kabra, Nick                  variance penalties and domain shift robustness. arXiv preprint
      Watters, Christopher Burgess, Daniel Zoran, Loic Matthey,                1710.11469, 2017.
      Matthew Botvinick, and Alexander Lerchner. Multi-object            [105] Christina Heinze-Deml, Jonas Peters, and Nicolai Meinshausen.
      representation learning with iterative variational inference. In         Invariant causal prediction for nonlinear models. arXiv preprint
      International Conference on Machine Learning, pages 2424–                1706.08576, 2017.
      2433, 2019.                                                        [106] Dan Hendrycks and Thomas Dietterich. Benchmarking neural
 [87] Klaus Greff, Sjoerd van Steenkiste, and Jürgen Schmidhuber.              network robustness to common corruptions and perturbations.
      On the binding problem in artificial neural networks. arXiv              arXiv preprint 1903.12261, 2019.
      preprint 2012.05208, 2020.                                         [107] Joseph Henrich. The Secret of our Success. Princeton University
 [88] Karol Gregor, Danilo Jimenez Rezende, Frederic Besse, Yan                Press, 2016.
      Wu, Hamza Merzic, and Aaron van den Oord. Shaping belief           [108] Katharine E Henry, David N Hager, Peter J Pronovost, and
      states with generative environment models for rl. In Advances            Suchi Saria. A targeted real-time early warning score (trews-
      in Neural Information Processing Systems, pages 13475–13487,             core) for septic shock. Science translational medicine, 7(299):
      2019.                                                                    299ra122–299ra122, 2015.
 [89] Luigi Gresele, Paul K Rubenstein, Arash Mehrjou, Francesco         [109] Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess,
      Locatello, and Bernhard Schölkopf. The incomplete rosetta                Xavier Glorot, Matthew Botvinick, Shakir Mohamed, and
      stone problem: Identifiability results for multi-view nonlinear          Alexander Lerchner. beta-vae: Learning basic visual concepts
      ica. arXiv preprint 1905.06642, 2019.                                    with a constrained variational framework. In International
 [90] A. Gretton, O. Bousquet, A. Smola, and B. Schölkopf. Mea-                Conference on Learning Representations, 2016.
      suring statistical dependence with Hilbert-Schmidt norms. In       [110] R Devon Hjelm and William Buchwalter. Learning represen-
      Algorithmic Learning Theory, pages 63–78. Springer-Verlag,               tations by maximizing mutual information across views. In
      2005.                                                                    Advances in Neural Information Processing Systems, pages
 [91] A. Gretton, R. Herbrich, A. Smola, O. Bousquet, and                      15535–15545, 2019.
      B. Schölkopf. Kernel methods for measuring independence.           [111] K. D. Hoover. Causality in economics and econometrics. In
      Journal of Machine Learning Research, 6:2075–2129, 2005.                 S. N. Durlauf and L. E. Blume, editors, The New Palgrave
 [92] Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin              Dictionary of Economics. Palgrave Macmillan, Basingstoke,
      Tallec, Pierre H Richemond, Elena Buchatskaya, Carl Doersch,             UK, 2nd edition, 2008.
      Bernardo Avila Pires, Zhaohan Daniel Guo, Mohammad Ghesh-          [112] Jeremy Howard and Sebastian Ruder. Universal language model
      laghi Azar, et al. Bootstrap your own latent: A new approach             fine-tuning for text classification. arXiv preprint 1801.06146,
      to self-supervised learning. arXiv preprint 2006.07733, 2020.            2018.
 [93] Radek Grzeszczuk, Demetri Terzopoulos, and Geoffrey Hinton.        [113] P. O. Hoyer, D. Janzing, J. M. Mooij, J. Peters, and
      Neuroanimator: Fast neural network emulation and control                 B. Schölkopf. Nonlinear causal discovery with additive noise
      of physics-based models. In Proceedings of the 25th annual               models. In Advances in Neural Information Processing Systems
      conference on Computer graphics and interactive techniques,              21 (NIPS), pages 689–696, 2009.
      pages 9–20, 1998.                                                  [114] B. Huang, K. Zhang, J. Zhang, R. Sanchez-Romero, C. Gly-
 [94] Keren Gu, Brandon Yang, Jiquan Ngiam, Quoc Le, and                       mour, and B. Schölkopf. Behind distribution shift: Mining
      Jonathan Shlens. Using videos to evaluate image model                    driving forces of changes and causal arrows. In IEEE 17th
      robustness. arXiv preprint 1904.10076, 2019.                             International Conference on Data Mining (ICDM 2017), pages
 [95] Shixiang Gu and Luca Rigazio. Towards deep neural                        913–918, 2017.
      network architectures robust to adversarial examples, 2014.        [115] Biwei Huang, Kun Zhang, Jiji Zhang, Joseph Ramsey, Ruben
      arXiv:1412.5068.                                                         Sanchez-Romero, Clark Glymour, and Bernhard Schölkopf.
 [96] Ruocheng Guo, Lu Cheng, Jundong Li, P. Richard Hahn, and                 Causal discovery from heterogeneous/nonstationary data. Jour-
      Huan Liu. A survey of learning causality with data: Problems             nal of Machine Learning Research, 21(89):1–53, 2020. URL
      and methods. arXiv preprint 1809.09337, 2018.                            http://jmlr.org/papers/v21/19-232.html.
 [97] I. Guyon, D. Janzing, and B. Schölkopf. Causality: Objectives      [116] Aapo Hyvärinen and Petteri Pajunen. Nonlinear independent
      and assessment. In I. Guyon, D. Janzing, and B. Schölkopf,               component analysis: Existence and uniqueness results. Neural
      editors, JMLR Workshop and Conference Proceedings: Volume                networks, 12(3):429–439, 1999.
      6, pages 1–42, Cambridge, MA, USA, 2010. MIT Press.                [117] AJ Hyvarinen and Hiroshi Morioka. Nonlinear ica of temporally
 [98] David Ha and Jürgen Schmidhuber. World models. arXiv                     dependent stationary sources. In Proceedings of Machine
      preprint 1803.10122, 2018.                                               Learning Research, 2017.
 [99] T. Haavelmo. The probability approach in econometrics.             [118] Guido W Imbens and Donald B Rubin. Causal inference
      Econometrica, 12:S1–S115 (supplement), 1944.                             in statistics, social, and biomedical sciences. Cambridge
[100] Hermanni Hälvä and Aapo Hyvärinen. Hidden markov                         University Press, 2015.
                                                                                                                                              20



[119] D. Janzing. Causal regularization. In Advances in Neural                  Puigcerver, Jessica Yung, Sylvain Gelly, and Neil Houlsby.
      Information Processing Systems 33, 2019.                                  Big transfer (bit): General visual representation learning. arXiv
[120] D. Janzing and B. Schölkopf. Causal inference using the algo-             preprint 1912.11370, 2019.
      rithmic Markov condition. IEEE Transactions on Information          [138] Adam Kosiorek, Hyunjik Kim, Yee Whye Teh, and Ingmar
      Theory, 56(10):5168–5194, 2010.                                           Posner. Sequential attend, infer, repeat: Generative modelling
[121] D. Janzing and B. Schölkopf. Semi-supervised interpolation in             of moving objects. Advances in Neural Information Processing
      an anticausal learning scenario. Journal of Machine Learning              Systems, 31:8606–8616, 2018.
      Research, 16:1923–1948, 2015.                                       [139] S. Kpotufe, E. Sgouritsa, D. Janzing, and B. Schölkopf.
[122] D. Janzing and B. Schölkopf. Detecting non-causal artifacts in            Consistency of causal inference under the additive noise model.
      multivariate linear regression models. In Proceedings of the              In Proceedings of the 31th International Conference on Machine
      35th International Conference on Machine Learning (ICML),                 Learning, pages 478–486, 2014.
      pages 2250–2258, 2018.                                              [140] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.
[123] D. Janzing, J. Peters, J. M. Mooij, and B. Schölkopf. Identifying         Imagenet classification with deep convolutional neural networks.
      confounders using additive noise models. In Proceedings of the            In Advances in neural information processing systems, pages
      25th Annual Conference on Uncertainty in Artificial Intelligence          1097–1105, 2012.
      (UAI), pages 249–257, 2009.                                         [141] Tejas D Kulkarni, Ankush Gupta, Catalin Ionescu, Sebas-
[124] D. Janzing, P. Hoyer, and B. Schölkopf. Telling cause from                tian Borgeaud, Malcolm Reynolds, Andrew Zisserman, and
      effect based on high-dimensional observations. In J. Fürnkranz            Volodymyr Mnih. Unsupervised learning of object keypoints
      and T. Joachims, editors, Proceedings of the 27th International           for perception and control. In Advances in Neural Information
      Conference on Machine Learning, pages 479–486, 2010.                      Processing Systems, pages 10723–10733, 2019.
[125] D. Janzing, J. M. Mooij, K. Zhang, J. Lemeire, J. Zscheischler,     [142] Matt J Kusner, Joshua Loftus, Chris Russell, and Ricardo Silva.
      P. Daniušis, B. Steudel, and B. Schölkopf. Information-                   Counterfactual fairness. In Advances in Neural Information
      geometric approach to inferring causal directions. Artificial             Processing Systems 30, pages 4066–4076. Curran Associates,
      Intelligence, 182–183:1–31, 2012.                                         Inc., 2017.
[126] D. Janzing, R. Chaves, and B. Schölkopf. Algorithmic indepen-       [143] L’ubor Ladickỳ, SoHyeon Jeong, Barbara Solenthaler, Marc
      dence of initial condition and dynamical law in thermodynamics            Pollefeys, and Markus Gross. Data-driven fluid simulations
      and causal inference. New Journal of Physics, 18(9), 2016.                using regression forests. ACM Transactions on Graphics (TOG),
      URL http://stacks.iop.org/1367-2630/18/i=9/a=093052.                      34(6):1–9, 2015.
[127] Leslie Pack Kaelbling, Michael L Littman, and Andrew W              [144] Brenden M Lake, Tomer D Ullman, Joshua B Tenenbaum, and
      Moore. Reinforcement learning: A survey. Journal of artificial            Samuel J Gershman. Building machines that learn and think
      intelligence research, 4:237–285, 1996.                                   like people. Behavioral and brain sciences, 40, 2017.
[128] Daniel Kahneman.           Thinking, fast and slow.       Farrar,   [145] Janet Landman, Elizabeth A Vandewater, Abigail J Stewart,
      Straus and Giroux, New York, 2011.                         ISBN           and Janet E Malley. Missed opportunities: Psychological
      9780374275631 0374275637.                   URL https://www.              ramifications of counterfactual thought in midlife women.
      amazon.de/Thinking-Fast-Slow-Daniel-Kahneman/dp/                          Journal of Adult Development, 2(2):87–97, 1995.
      0374275637/ref=wl_it_dp_o_pdT1_nS_nC?ie=UTF8&colid=                 [146] Sascha Lange, Thomas Gabel, and Martin Riedmiller. Batch
      151193SNGKJT9&coliid=I3OCESLZCVDFL7.                                      reinforcement learning. In Marco Wiering and Martijn van Ot-
[129] Samil Karahan, Merve Kilinc Yildirum, Kadir Kirtac, Fer-                  terlo, editors, Reinforcement Learning: State-of-the-Art, pages
      hat Sukru Rende, Gultekin Butun, and Hazim Kemal Ekenel.                  45–73. Springer, Berlin, Heidelberg, 2012.
      How image degradations affect deep cnn-based face recog-            [147] S. L. Lauritzen. Graphical Models. Oxford University Press,
      nition? In 2016 International Conference of the Biometrics                New York, NY, 1996.
      Special Interest Group (BIOSIG), pages 1–5. IEEE, 2016.             [148] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep
[130] Amir-Hossein Karimi, Julius von Kügelgen, Bernhard                        learning. Nature, 521(7553):436–444, 2015.
      Schölkopf, and Isabel Valera. Algorithmic recourse under            [149] Felix Leeb, Yashas Annadani, Stefan Bauer, and Bernhard
      imperfect causal knowledge: a probabilistic approach. arXiv               Schölkopf. Structural autoencoders improve representations for
      2006.06831, 2020. Published at NeurIPS.                                   generation and transfer. arXiv preprint 2006.07796, 2020.
[131] Nan Rosemary Ke, Olexa Bilaniuk, Anirudh Goyal, Stefan              [150] Sergey Levine, Aviral Kumar, George Tucker, and Justin
      Bauer, Hugo Larochelle, Bernhard Schölkopf, Michael Mozer,                Fu. Offline reinforcement learning: Tutorial, review, and
      Chris Pal, and Yoshua Bengio. Learning neural causal models               perspectives on open problems. arXiv preprint 2005.01643,
      from unknown interventions. arXiv preprint 1910.01075v2,                  2020.
      2020.                                                               [151] David Lewis. Causation. The journal of philosophy, 70(17):
[132] Moein Khajehnejad, Behzad Tabibian, Bernhard Schölkopf,                   556–567, 1974.
      Adish Singla, and Manuel Gomez-Rodriguez. Optimal decision          [152] Ya Li, Mingming Gong, Xinmei Tian, Tongliang Liu, and
      making under strategic behavior. arXiv preprint 1905.09239,               Dacheng Tao. Domain generalization via conditional invariant
      2019.                                                                     representation. arXiv preprint 1807.08479, 2018.
[133] N. Kilbertus, M. Rojas Carulla, G. Parascandolo, M. Hardt,          [153] Ya Li, Xinmei Tian, Mingming Gong, Yajing Liu, Tongliang
      D. Janzing, and B. Schölkopf. Avoiding discrimination through             Liu, Kun Zhang, and Dacheng Tao. Deep domain generalization
      causal reasoning. In Advances in Neural Information Processing            via conditional invariant adversarial networks. In The European
      Systems 30, pages 656–666, 2017.                                          Conference on Computer Vision (ECCV), 2018.
[134] Niki Kilbertus, Giambattista Parascandolo, and Bernhard             [154] Sungbin Lim, Ildoo Kim, Taesup Kim, Chiheon Kim, and
      Schölkopf. Generalization in anti-causal learning. arXiv                  Sungwoong Kim. Fast autoaugment. In Advances in Neural
      preprint 1812.00524, 2018.                                                Information Processing Systems, pages 6665–6675, 2019.
[135] Hyunjik Kim and Andriy Mnih. Disentangling by factorising.          [155] Zhixuan Lin, Yi-Fu Wu, Skand Vishwanath Peri, Weihao
      In International Conference on Machine Learning, 2018.                    Sun, Gautam Singh, Fei Deng, Jindong Jiang, and Sungjin
[136] Thomas Kipf, Ethan Fetaya, Kuan-Chieh Wang, Max Welling,                  Ahn. Space: Unsupervised object-oriented scene representation
      and Richard Zemel. Neural relational inference for interacting            via spatial attention and decomposition. In International
      systems. In International Conference on Machine Learning,                 Conference on Learning Representations, 2019.
      pages 2688–2697, 2018.                                              [156] Zachary C. Lipton, Yu-Xiang Wang, and Alex Smola. Detecting
[137] Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Joan                     and correcting for label shift with black box predictors. arXiv
                                                                                                                                           21



      preprint 1802.03916, 2018.                                              case. In A. Nicholson and P. Smyth, editors, Proceedings of the
[157] Francesco Locatello, Gabriele Abbati, Tom Rainforth, Stefan             Twenty-Ninth Conference Annual Conference on Uncertainty
      Bauer, Bernhard Schölkopf, and Olivier Bachem. On the                   in Artificial Intelligence, pages 440–448, Corvallis, OR, 2013.
      fairness of disentangled representations. In Advances in Neural         AUAI Press. URL http://www.is.tuebingen.mpg.de/fileadmin/
      Information Processing Systems, pages 14544–14557, 2019.                user_upload/files/publications/2013/MooijJS2013-uai.pdf.
[158] Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar            [174] J. M. Mooij, D. Janzing, J. Peters, and B. Schölkopf. Regression
      Rätsch, Sylvain Gelly, Bernhard Schölkopf, and Olivier Bachem.          by dependence minimization and its application to causal
      Challenging common assumptions in the unsupervised learning             inference. In Proceedings of the 26th International Conference
      of disentangled representations. Proceedings of the 36th                on Machine Learning (ICML), pages 745–752, 2009.
      International Conference on Machine Learning, 2019.               [175] J. M. Mooij, D. Janzing, T. Heskes, and B. Schölkopf. On
[159] Francesco Locatello, Ben Poole, Gunnar Rätsch, Bernhard                 causal discovery with cyclic additive noise models. In Advances
      Schölkopf, Olivier Bachem, and Michael Tschannen. Weakly-               in Neural Information Processing Systems 24 (NIPS), 2011.
      supervised disentanglement without compromises. In Proceed-       [176] J. M. Mooij, J. Peters, D. Janzing, J. Zscheischler, and
      ings of the 37th International Conference on Machine Learning           B. Schölkopf. Distinguishing cause from effect using obser-
      (ICML), 2020.                                                           vational data: methods and benchmarks. Journal of Machine
[160] Francesco Locatello, Dirk Weissenborn, Thomas Unterthiner,              Learning Research, 17(32):1–102, 2016.
      Aravindh Mahendran, Georg Heigold, Jakob Uszkoreit, Alexey        [177] Damian Mrowca, Chengxu Zhuang, Elias Wang, Nick Haber,
      Dosovitskiy, and Thomas Kipf. Object-centric learning with              Li Fei-Fei, Josh Tenenbaum, and Daniel L K Yamins. Flexible
      slot attention. In Advances in Neural Information Processing            neural representation for physics prediction. In Advances
      Systems, 2020.                                                          in Neural Information Processing Systems, pages 8799–8810,
[161] D. Lopez-Paz, K. Muandet, B. Schölkopf, and I. Tolstikhin.              2018.
      Towards a learning theory of cause-effect inference. In           [178] Junhyuk Oh, Xiaoxiao Guo, Honglak Lee, Richard L Lewis, and
      Proceedings of the 32nd International Conference on Machine             Satinder Singh. Action-conditional video prediction using deep
      Learning, pages 1452–1461, 2015.                                        networks in atari games. In Advances in neural information
[162] D. Lopez-Paz, R. Nishihara, S. Chintala, B. Schölkopf, and              processing systems, pages 2863–2871, 2015.
      L. Bottou. Discovering causal signals in images. In IEEE          [179] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representa-
      Conference on Computer Vision and Pattern Recognition                   tion learning with contrastive predictive coding. arXiv preprint
      (CVPR), pages 58–66, 2017.                                              1807.03748, 2018.
[163] K. Lorenz. Die Rückseite des Spiegels. R. Piper & Co. Verlag,     [180] G. Parascandolo, M. Rojas-Carulla, N. Kilbertus, and
      1973.                                                                   B. Schölkopf. Learning independent causal mechanisms.
[164] Chaochao Lu, Bernhard Schölkopf, and José Miguel Hernández-             In Workshop: Learning Disentangled Representations: from
      Lobato. Deconfounding reinforcement learning in observational           Perception to Control at the 31st Conference on Neural
      settings. arXiv preprint 1812.10576, 2018.                              Information Processing Systems (NIPS), 2017.
[165] Chaochao Lu, Biwei Huang, Ke Wang, José Miguel Hernández-         [181] G. Parascandolo, N. Kilbertus, M. Rojas-Carulla, and
      Lobato, Kun Zhang, and Bernhard Schölkopf. Sample-efficient             B. Schölkopf. Learning independent causal mechanisms. In
      reinforcement learning via counterfactual-based data augmen-            Proceedings of the 35th International Conference on Machine
      tation. arXiv preprint 2012.09092, 2020.                                Learning, PMLR 80:4036-4044, 2018.
[166] Alexander Selvikvåg Lundervold and Arvid Lundervold. An           [182] Giambattista Parascandolo, Alexander Neitz, ANTONIO ORVI-
      overview of deep learning in medical imaging focusing on MRI.           ETO, Luigi Gresele, and Bernhard Schölkopf. Learning
      Zeitschrift für Medizinische Physik, 29(2):102–127, 2019.               explanations that are hard to vary. In International Conference
[167] Sara Magliacane, Thijs van Ommen, Tom Claassen, Stephan                 on Learning Representations, 2021.
      Bongers, Philip Versteeg, and Joris M. Mooij. Domain              [183] J. Pearl. Causality: Models, Reasoning, and Inference. Cam-
      adaptation by using causal inference to predict invariant               bridge University Press, New York, NY, 2nd edition, 2009.
      conditional distributions. In Proc. NeurIPS, 2018.                [184] J. Pearl. Giving computers free will. Forbes, 2009.
[168] Robert Matthews. Storks deliver babies (p= 0.008). Teaching       [185] Judea Pearl and Elias Bareinboim. External validity: From do-
      Statistics, 22(2):36–38, 2000.                                          calculus to transportability across populations. arXiv preprint
[169] Nicolai Meinshausen. Causality from a distributional robustness         1503.01603, 2015.
      point of view. In 2018 IEEE Data Science Workshop (DSW),          [186] J. Peters, J. M. Mooij, D. Janzing, and B. Schölkopf. Identifia-
      pages 6–10. IEEE, 2018.                                                 bility of causal graphs using functional models. In Proceedings
[170] Claudio Michaelis, Benjamin Mitzkus, Robert Geirhos, Evgenia            of the 27th Annual Conference on Uncertainty in Artificial
      Rusak, Oliver Bringmann, Alexander S Ecker, Matthias Bethge,            Intelligence (UAI), pages 589–598, 2011.
      and Wieland Brendel. Benchmarking robustness in object            [187] J. Peters, J. M. Mooij, D. Janzing, and B. Schölkopf. Causal
      detection: Autonomous driving when winter is coming. arXiv              discovery with continuous additive noise models. Journal
      preprint 1907.07484, 2019.                                              of Machine Learning Research, 15:2009–2053, 2014. URL
[171] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A.              http://jmlr.org/papers/v15/peters14a.html.
      Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin         [188] J. Peters, D. Janzing, and B. Schölkopf. Elements of Causal
      Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig                 Inference - Foundations and Learning Algorithms. MIT Press,
      Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou,              Cambridge, MA, USA, 2017.
      Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg,          [189] Jonas Peters, Peter Bühlmann, and Nicolai Meinshausen. Causal
      and Demis Hassabis. Human-level control through deep                    inference by using invariant prediction: identification and
      reinforcement learning. Nature, 518(7540):529–533, 2015.                confidence intervals. Journal of the Royal Statistical Society:
[172] B. T. Montet, T. D. Morton, D. Foreman-Mackey, J. A. Johnson,           Series B (Statistical Methodology), 78(5):947–1012, 2016.
      D. W. Hogg, B. P. Bowler, D. W. Latham, A. Bieryla, and           [190] Jonas Peters, Stefan Bauer, and Niklas Pfister. Causal models
      A. W. Mann. Stellar and planetary properties of K2 campaign             for dynamical systems. arXiv preprint 2001.06208, 2020.
      1 candidates and validation of 17 planets, including a planet     [191] N. Pfister, P. Bühlmann, B. Schölkopf, and J. Peters. Kernel-
      receiving earth-like insolation. The Astrophysical Journal, 809         based tests for joint independence. Journal of the Royal
      (1):25, 2015.                                                           Statistical Society: Series B (Statistical Methodology), 80(1):
[173] J. Mooij, D. Janzing, and B. Schölkopf. From ordinary differ-           5–31, 2018.
      ential equations to structural causal models: the deterministic   [192] Niklas Pfister, Stefan Bauer, and Jonas Peters. Learning stable
                                                                                                                                              22



      and predictive structures in kinetic systems. Proceedings of the         learning, or on learning how to learn: the meta-meta-... hook.
      National Academy of Sciences, 116(51):25405–25411, 2019.                 PhD thesis, Technische Universität München, 1987.
[193] Niklas Pfister, Peter Bühlmann, and Jonas Peters. Invariant        [214] Jürgen Schmidhuber. Curious model-building control systems.
      causal prediction for sequential data. Journal of the American           In Proc. international joint conference on neural networks,
      Statistical Association, 114(527):1264–1276, 2019.                       pages 1458–1463, 1991.
[194] Rémi Le Priol, Reza Babanezhad Harikandeh, Yoshua Bengio,          [215] B. Schölkopf. Artificial intelligence: Learning to see and act.
      and Simon Lacoste-Julien. An analysis of the adaptation speed            Nature, 518(7540):486–487, 2015.
      of causal models. arXiv preprint 2005.09136, 2020.                 [216] B. Schölkopf. Causal learning, 2017. Invited Talk, 34th
[195] Stephan Rabanser, Stephan Günnemann, and Zachary C. Lipton.              International Conference on Machine Learning (ICML), https:
      Failing loudly: An empirical study of methods for detecting              //vimeo.com/238274659.
      dataset shift. arXiv preprint 1810.11953, 2018.                    [217] B. Schölkopf and A. J. Smola. Learning with Kernels. MIT
[196] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya                 Press, Cambridge, MA, 2002.
      Sutskever. Improving language understanding by generative          [218] B. Schölkopf, D. Janzing, J. Peters, E. Sgouritsa, K. Zhang, and
      pre-training, 2018.                                                      J. M. Mooij. On causal and anticausal learning. In Proceedings
[197] Nasim Rahaman, Anirudh Goyal, Muhammad Waleed Gondal,                    of the 29th International Conference on Machine Learning
      Manuel Wuthrich, Stefan Bauer, Yash Sharma, Yoshua Bengio,               (ICML), pages 1255–1262, 2012.
      and Bernhard Schölkopf. Spatially structured recurrent modules.    [219] B. Schölkopf, D. Hogg, D. Wang, D. Foreman-Mackey, D. Janz-
      In International Conference on Learning Representations, 2021.           ing, C.-J. Simon-Gabriel, and J. Peters. Modeling confounding
[198] H. Reichenbach. The Direction of Time. University of California          by half-sibling regression. Proceedings of the National Academy
      Press, Berkeley, CA, 1956.                                               of Science (PNAS), 113(27):7391–7398, 2016.
[199] Laine K Reichert and John R Slate. Reflective learning: The        [220] B. Schölkopf, D. Janzing, and D. Lopez-Paz. Causal and
      use of “if only...” statements to improve performance. Social            statistical learning. In Oberwolfach Reports, volume 13(3),
      Psychology of Education, 3(4):261–275, 1999.                             pages 1896–1899, 2016. doi: 10.14760/OWR-2016-33. URL
[200] Danilo J Rezende, Ivo Danihelka, George Papamakarios,                    https://publications.mfo.de/handle/mfo/3537.
      Nan Rosemary Ke, Ray Jiang, Theophane Weber, Karol Gregor,         [221] Bernhard Schölkopf. Causality for machine learning. arXiv
      Hamza Merzic, Fabio Viola, Jane Wang, et al. Causally correct            preprint 1911.10500, 2019.
      partial models for reinforcement learning. arXiv preprint          [222] Lukas Schott, Jonas Rauber, Matthias Bethge, and Wieland
      2002.02836, 2020.                                                        Brendel. Towards the first adversarially robust neural network
[201] Jonathan G Richens, Ciarán M Lee, and Saurabh Johri.                     model on MNIST. In International Conference on Learning
      Improving the accuracy of medical diagnosis with causal                  Representations, 2019. URL https://openreview.net/forum?id=
      machine learning. Nature Communications, 11(1):3923, 2020.               S1EHOsC9tX.
[202] Karl Ridgeway and Michael C Mozer. Learning deep disen-            [223] Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert,
      tangled embeddings with the f-statistic loss. In Advances in             Karen Simonyan, Laurent Sifre, Simon Schmitt, Arthur Guez,
      Neural Information Processing Systems, pages 185–194, 2018.              Edward Lockhart, Demis Hassabis, Thore Graepel, et al.
[203] Neal J Roese. The functional basis of counterfactual thinking.           Mastering atari, go, chess and shogi by planning with a learned
      Journal of personality and Social Psychology, 66(5):805, 1994.           model. arXiv preprint 1911.08265, 2019.
[204] M. Rojas-Carulla, B. Schölkopf, R. Turner, and J. Peters.          [224] Peter Schulam and Suchi Saria. Reliable decision support using
      Invariant models for causal transfer learning. Journal of                counterfactual models. In Advances in Neural Information
      Machine Learning Research, 19(36):1–34, 2018.                            Processing Systems, pages 1697–1708, 2017.
[205] Michal Rolinek, Dominik Zietlow, and Georg Martius. Varia-         [225] Rajen D. Shah and Jonas Peters. The hardness of conditional
      tional autoencoders pursue PCA directions (by accident). In              independence testing and the generalised covariance measure.
      Proceedings of the IEEE Conference on Computer Vision and                arXiv preprint 1804.07203, 2018.
      Pattern Recognition, pages 12406–12415, 2019.                      [226] N. Shajarisales, D. Janzing, B. Schölkopf, and M. Besserve.
[206] Prasun Roy, Subhankar Ghosh, Saumik Bhattacharya, and                    Telling cause from effect in deterministic linear dynamical
      Umapada Pal. Effects of degradations on deep neural network              systems. In Proceedings of the 32nd International Conference
      architectures. arXiv preprint 1807.10108, 2018.                          on Machine Learning (ICML), pages 285–294, 2015.
[207] P. K. Rubenstein, S. Weichwald, S. Bongers, J. M. Mooij,           [227] Vaishaal Shankar, Achal Dave, Rebecca Roelofs, Deva Ra-
      D. Janzing, M. Grosse-Wentrup, and B. Schölkopf. Causal                  manan, Benjamin Recht, and Ludwig Schmidt. Do image
      consistency of structural equation models. In Proceedings                classifiers generalize across time? arXiv preprint 1906.02168,
      of the Thirty-Third Conference on Uncertainty in Artificial              2019.
      Intelligence, pages 808–817, 2017.                                 [228] Rakshith Shetty, Bernt Schiele, and Mario Fritz. Not using the
[208] P. K. Rubenstein, S. Bongers, B. Schölkopf, and J. M. Mooij.             car to see the sidewalk–quantifying and controlling the effects of
      From deterministic ODEs to dynamic structural causal models.             context in classification and segmentation. In Proceedings of the
      In Proceedings of the 34th Conference on Uncertainty in                  IEEE Conference on Computer Vision and Pattern Recognition,
      Artificial Intelligence (UAI), 2018.                                     pages 8218–8226, 2019.
[209] Sebastian Ruder. An overview of multi-task learning in deep        [229] S. Shimizu, P. O. Hoyer, A. Hyvärinen, and A. J. Kerminen. A
      neural networks. arXiv preprint 1706.05098, 2017.                        linear non-Gaussian acyclic model for causal discovery. Journal
[210] Stuart Russell and Peter Norvig. Artificial intelligence: a              of Machine Learning Research, 7:2003–2030, 2006.
      modern approach. Prentice Hall, 2002.                              [230] Rui Shu, Yining Chen, Abhishek Kumar, Stefano Ermon, and
[211] Alvaro Sanchez-Gonzalez, Jonathan Godwin, Tobias Pfaff, Rex              Ben Poole. Weakly supervised disentanglement with guarantees.
      Ying, Jure Leskovec, and Peter W Battaglia. Learning to                  arXiv preprint 1910.09772, 2019.
      simulate complex physics with graph networks. arXiv preprint       [231] David Silver, Aja Huang, Chris J Maddison, Arthur Guez,
      2002.09405, 2020.                                                        Laurent Sifre, George Van Den Driessche, Julian Schrittwieser,
[212] Adam Santoro, David Raposo, David G Barrett, Mateusz                     Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al.
      Malinowski, Razvan Pascanu, Peter Battaglia, and Timothy                 Mastering the game of go with deep neural networks and tree
      Lillicrap. A simple neural network module for relational                 search. Nature, 529(7587):484–489, 2016.
      reasoning. In Advances in neural information processing            [232] David Silver, Hado Hasselt, Matteo Hessel, Tom Schaul, Arthur
      systems, pages 4967–4976, 2017.                                          Guez, Tim Harley, Gabriel Dulac-Arnold, David Reichert, Neil
[213] Jürgen Schmidhuber. Evolutionary principles in self-referential          Rabinowitz, Andre Barreto, et al. The predictron: End-to-end
                                                                                                                                           23



      learning and planning. In International Conference on Machine           Artificial Intelligence (UAI), pages 512–522, 2001.
      Learning, pages 3191–3199. PMLR, 2017.                            [252] Frederik Träuble, Elliot Creager, Niki Kilbertus, Anirudh
[233] Patrice Simard, Bernard Victorri, Yann LeCun, and John                  Goyal, Francesco Locatello, Bernhard Schölkopf, and Stefan
      Denker. Tangent prop - a formalism for specifying selected              Bauer. Is independence all you need? on the generalization of
      invariances in an adaptive network. In J. Moody, S. Hanson,             representations learned from correlated data. arXiv preprint
      and R. P. Lippmann, editors, Advances in Neural Informa-                2006.07886, 2020.
      tion Processing Systems, volume 4, pages 895–903. Morgan-         [253] Michael Tschannen, Josip Djolonga, Marvin Ritter, Aravindh
      Kaufmann, 1992. URL https://proceedings.neurips.cc/paper/               Mahendran, Neil Houlsby, Sylvain Gelly, and Mario Lucic.
      1991/file/65658fde58ab3c2b6e5132a39fae7cb9-Paper.pdf.                   Self-supervised learning of video-induced visual invariances.
[234] Patrice Y Simard, David Steinkraus, John C Platt, et al. Best           In Proceedings of the IEEE/CVF Conference on Computer
      practices for convolutional neural networks applied to visual           Vision and Pattern Recognition, pages 13806–13815, 2020.
      document analysis. In Proceedings of the Seventh International    [254] Angelos Tsiaras, Ingo Waldmann, G. Tinetti, Jonathan Ten-
      Conference on Document Analysis and Recognition (ICDAR                  nyson, and Sergei Yurchenko. Water vapour in the atmosphere
      2003), volume 3, 2003.                                                  of the habitable-zone eight-earth-mass planet K2-18b. Nature
[235] H. A. Simon. Causal ordering and identifiability. In W. C. Hood         Astronomy, 2019. doi: 10.1038/s41550-019-0878-9.
      and T. C. Koopmans, editors, Studies in Econometric Methods,      [255] Sjoerd Van Steenkiste, Michael Chang, Klaus Greff, and Jürgen
      pages 49–74. John Wiley & Sons, New York, NY, 1953. Cowles              Schmidhuber. Relational neural expectation maximization:
      Commission for Research in Economics, Monograph No. 14.                 Unsupervised discovery of objects and their interactions. In 6th
[236] Elizabeth S Spelke. Principles of object perception. Cognitive          International Conference on Learning Representations (ICLR),
      science, 14(1):29–56, 1990.                                             2018.
[237] P. Spirtes, C. Glymour, and R. Scheines. Causation, Prediction,   [256] Sjoerd van Steenkiste, Francesco Locatello, Jürgen Schmid-
      and Search. MIT Press, Cambridge, MA, 2nd edition, 2000.                huber, and Olivier Bachem. Are disentangled representations
[238] W. Spohn. Grundlagen der Entscheidungstheorie. Scriptor-                helpful for abstract visual reasoning? In Advances in Neural
      Verlag, 1978.                                                           Information Processing Systems, pages 14178–14191, 2019.
[239] I. Steinwart and A. Christmann. Support Vector Machines.          [257] V. N. Vapnik. Statistical Learning Theory. Wiley, New York,
      Springer, New York, NY, 2008.                                           NY, 1998.
[240] B. Steudel, D. Janzing, and B. Schölkopf. Causal Markov           [258] Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki,
      condition for submodular information measures. In Proceedings           Michaël Mathieu, Andrew Dudzik, Junyoung Chung, David H
      of the 23rd Annual Conference on Learning Theory (COLT),                Choi, Richard Powell, Timo Ewalds, Petko Georgiev, et al.
      pages 464–476, 2010.                                                    Grandmaster level in StarCraft II using multi-agent reinforce-
[241] Jianyu Su, Stephen Adams, and Peter A Beling. Counterfactual            ment learning. Nature, 575(7782):350–354, 2019.
      multi-agent reinforcement learning with graph convolution         [259] J. von Kügelgen, A. Mey, M. Loog, and B. Schölkopf. Semi-
      communication. arXiv preprint 2004.00470, 2020.                         supervised learning, causality and the conditional cluster
[242] Adarsh Subbaswamy and Suchi Saria. Counterfactual nor-                  assumption. Conference on Uncertainty in Artificial Intelligence
      malization: Proactively addressing dataset shift and improving          (UAI), 2020.
      reliability using causal mechanisms. arXiv preprint 1808.03253,   [260] Julius von Kügelgen, Umang Bhatt, Amir-Hossein Karimi,
      2018.                                                                   Isabel Valera, Adrian Weller, and Bernhard Schölkopf. On
[243] Adarsh Subbaswamy, Peter Schulam, and Suchi Saria. Prevent-             the fairness of causal algorithmic recourse. arXiv 2010.06529,
      ing failures due to dataset shift: Learning predictive models           2020.
      that transport. arXiv preprint 1812.04597, 2018.                  [261] Julius von Kügelgen, Luigi Gresele, and Bernhard Schölkopf.
[244] Chen Sun, Abhinav Shrivastava, Saurabh Singh, and Abhinav               Simpson’s paradox in Covid-19 case fatality rates: a mediation
      Gupta. Revisiting unreasonable effectiveness of data in deep            analysis of age-related causal effects. arXiv 2005.07180, 2020.
      learning era. In Proceedings of the IEEE international            [262] Julius von Kügelgen, Ivan Ustyuzhaninov, Peter Gehler,
      conference on computer vision, pages 843–852, 2017.                     Matthias Bethge, and Bernhard Schölkopf. Towards causal
[245] Chen Sun, Per Karlsson, Jiajun Wu, Joshua B Tenenbaum, and              generative scene models via competition of experts. arXiv
      Kevin Murphy. Stochastic prediction of multi-agent interactions         2004.12906, 2020.
      from partial observations. arXiv preprint 1902.09641, 2019.       [263] Haohan Wang, Zexue He, Zachary C. Lipton, and Eric P.
[246] X. Sun, D. Janzing, and B. Schölkopf. Causal inference                  Xing. Learning robust representations by projecting superficial
      by choosing graphs with most plausible Markov kernels. In               statistics out. arXiv preprint 1903.06256, 2019.
      Proceedings of the 9th International Symposium on Artificial      [264] Nicholas Watters, Daniel Zoran, Theophane Weber, Peter
      Intelligence and Mathematics, 2006.                                     Battaglia, Razvan Pascanu, and Andrea Tacchetti. Visual
[247] Raphael Suter, Djordje Miladinovic, Bernhard Schölkopf, and             interaction networks: Learning a physics simulator from video.
      Stefan Bauer. Robustly disentangled causal mechanisms:                  In Advances in neural information processing systems, pages
      Validating deep representations for interventional robustness.          4539–4547, 2017.
      In International Conference on Machine Learning, pages 6056–      [265] Nicholas Watters, Loic Matthey, Matko Bosnjak, Christopher P
      6065. PMLR, 2019.                                                       Burgess, and Alexander Lerchner. Cobra: Data-efficient model-
[248] Richard S Sutton, Andrew G Barto, et al. Introduction to                based rl through unsupervised object discovery and curiosity-
      reinforcement learning, volume 135. MIT press Cambridge,                driven exploration. arXiv preprint 1905.09275, 2019.
      1998.                                                             [266] S. Weichwald, B. Schölkopf, T. Ball, and M. Grosse-Wentrup.
[249] Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan               Causal and anti-causal learning in pattern recognition for
      Bruna, Dumitru Erhan, Ian Goodfellow, and Rob Fergus.                   neuroimaging. In 4th International Workshop on Pattern
      Intriguing properties of neural networks. arXiv preprint                Recognition in Neuroimaging (PRNI). IEEE, 2014.
      1312.6199, 2013.                                                  [267] Sebastian Weichwald. Pragmatism and Variable Transforma-
[250] Ernő Téglás, Edward Vul, Vittorio Girotto, Michel Gonzalez,            tions in Causal Modelling. PhD thesis, ETH Zurich, 2019.
      Joshua B Tenenbaum, and Luca L Bonatti. Pure reasoning in         [268] Marco Wiering and Martijn Van Otterlo. Reinforcement
      12-month-old infants as probabilistic inference. Science, 332           learning, volume 12. Springer, 2012.
      (6033):1054–1059, 2011.                                           [269] Steffen Wiewel, Moritz Becher, and Nils Thuerey. Latent space
[251] J. Tian and J. Pearl. Causal discovery from changes. In                 physics: Towards learning the temporal evolution of fluid flow.
      Proceedings of the 17th Annual Conference on Uncertainty in             In Computer Graphics Forum, volume 38, pages 71–82. Wiley
                                                                         24



      Online Library, 2019.
[270] Laurenz Wiskott and Terrence J Sejnowski. Slow feature anal-
      ysis: unsupervised learning of invariances. Neural computation,
      14(4):715–70, April 2002. ISSN 0899-7667.
[271] Chris Xie, Sachin Patil, Teodor Moldovan, Sergey Levine,
      and Pieter Abbeel. Model-based reinforcement learning with
      parametrized physical models and optimism-driven exploration.
      In 2016 IEEE international conference on robotics and au-
      tomation (ICRA), pages 504–511. IEEE, 2016.
[272] Kexin Yi, Chuang Gan, Yunzhu Li, Pushmeet Kohli, Jiajun
      Wu, Antonio Torralba, and Joshua B Tenenbaum. CLEVRER:
      Collision events for video representation and reasoning. arXiv
      preprint 1910.01442, 2019.
[273] Jinsung Yoon, James Jordon, and Mihaela van der Schaar.
      Ganite: Estimation of individualized treatment effects using
      generative adversarial nets. In International Conference on
      Learning Representations, 2018.
[274] Vinicius Zambaldi, David Raposo, Adam Santoro, Victor Bapst,
      Yujia Li, Igor Babuschkin, Karl Tuyls, David Reichert, Timothy
      Lillicrap, Edward Lockhart, et al. Deep reinforcement learning
      with relational inductive biases. In International Conference
      on Learning Representations, 2018.
[275] J. Zhang and E. Bareinboim. Near-optimal reinforcement
      learning in dynamic treatment regimes. In Advances in Neural
      Information Processing Systems 33, pages 13401–13411, 2019.
[276] Junzhe Zhang and Elias Bareinboim. Fairness in decision-
      making - the causal explanation formula. In Proceedings of
      the Thirty-Second AAAI Conference on Artificial Intelligence,
      New Orleans, Louisiana, USA, pages 2037–2045, 2018.
[277] K. Zhang and A. Hyvärinen. On the identifiability of the post-
      nonlinear causal model. In Proceedings of the 25th Annual
      Conference on Uncertainty in Artificial Intelligence (UAI),
      pages 647–655, 2009.
[278] K. Zhang, J. Peters, D. Janzing, and B. Schölkopf. Kernel-
      based conditional independence test and application in causal
      discovery. In Proceedings of the 27th Annual Conference on
      Uncertainty in Artificial Intelligence (UAI), pages 804–813,
      2011.
[279] K. Zhang, B. Schölkopf, K. Muandet, and Z. Wang. Domain
      adaptation under target and conditional shift. In Proceedings
      of the 30th International Conference on Machine Learning
      (ICML), pages 819–827, 2013.
[280] K. Zhang, M. Gong, and B. Schölkopf. Multi-source domain
      adaptation: A causal view. In Proceedings of the 29th AAAI
      Conference on Artificial Intelligence, pages 3150–3157, 2015.
[281] K. Zhang, B. Huang, J. Zhang, C. Glymour, and B. Schölkopf.
      Causal discovery from nonstationary/heterogeneous data: Skele-
      ton estimation and orientation determination. In Proceedings
      of the Twenty-Sixth International Joint Conference on Artificial
      Intelligence (IJCAI 2017), pages 1347–1353, 2017.
[282] Richard Zhang. Making convolutional networks shift-invariant
      again. arXiv preprint 1904.11486, 2019.
```
