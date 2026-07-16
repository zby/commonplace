---
source: https://arxiv.org/abs/2307.16405
description: Zheng et al. describe causal-learn, a Python library collecting causal discovery methods for inferring causal structure from observational data under method-specific assumptions
captured: 2026-07-16
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Causal-learn: Causal Discovery in Python

Author: Yujia Zheng, Biwei Huang, Wei Chen, Joseph Ramsey, Mingming Gong, Ruichu Cai, Shohei Shimizu, Peter Spirtes, and Kun Zhang
Source: https://arxiv.org/abs/2307.16405 (PDF: https://arxiv.org/pdf/2307.16405)
Date: arXiv:2307.16405v1, 31 July 2023

Capture note: text extracted from the arXiv PDF. Mathematical notation and tables are reproduced as the extractor rendered them.

```text
                                                                Causal-learn: Causal Discovery in Python




                                                        Causal-learn: Causal Discovery in Python

                                         Yujia Zheng1,6                                                                 yujiazh@cmu.edu
                                         Biwei Huang2                                                                   bih007@ucsd.edu
                                         Wei Chen3                                                           chenweidelight@gmail.com
                                         Joseph Ramsey1                                                       jdramsey@andrew.cmu.edu
                                         Mingming Gong4                                                  mingming.gong@unimelb.edu.au
                                         Ruichu Cai3                                                                cairuichu@gmail.com
                                         Shohei Shimizu5,7
arXiv:2307.16405v1 [cs.LG] 31 Jul 2023




                                                                                                     shohei-shimizu@biwako.shiga-u.ac.jp
                                         Peter Spirtes1                                                            ps7z@andrew.cmu.edu
                                         Kun Zhang1,6                                                                     kunz1@cmu.edu
                                         1
                                           Carnegie Mellon University
                                         2
                                           University of California, San Diego
                                         3
                                           Guangdong University of Technology
                                         4
                                           University of Melbourne
                                         5
                                           Shiga University
                                         6
                                           Mohamed bin Zayed University of Artificial Intelligence
                                         7
                                           RIKEN


                                                                                    Abstract
                                             Causal discovery aims at revealing causal relations from observational data, which is a fun-
                                             damental task in science and engineering. We describe causal-learn, an open-source Python
                                             library for causal discovery. This library focuses on bringing a comprehensive collection
                                             of causal discovery methods to both practitioners and researchers. It provides easy-to-use
                                             APIs for non-specialists, modular building blocks for developers, detailed documentation
                                             for learners, and comprehensive methods for all. Different from previous packages in R
                                             or Java, causal-learn is fully developed in Python, which could be more in tune with the
                                             recent preference shift in programming languages within related communities. The library
                                             is available at https://github.com/py-why/causal-learn.
                                             Keywords: Causal Discovery, Python, Conditional Independence, Independence, Ma-
                                             chine Learning


                                         1 Introduction

                                         A traditional way to uncover causal relationships is to resort to interventions or randomized
                                         experiments, which are often impractical due to their cost or logistical limitations. Hence,
                                         the importance of causal discovery, i.e., the process of revealing causal information through
                                         the analysis of purely observational data, has become increasingly apparent across diverse
                                         disciplines, including genomics, ecology, neuroscience, and epidemiology, among others (Gly-
                                         mour et al., 2019). For instance, in genomics, causal discovery has been instrumental in
                                         understanding the relationships between certain genes and diseases. Researchers might not
                                         have the resources to manipulate gene expressions, but they can analyze observational data,
                                         which are usually widely available, such as genomic databases, to uncover potential causal

                                                                                          1
                                        Zheng et al.




relationships. This can lead to breakthroughs in disease treatment and prevention strategies
without the cost of traditional experimentation.
    Current strategies for causal discovery can be broadly classified into constraint-based,
score-based, functional causal models-based, and methods that recover latent variables.
Constraint-based and score-based methods have been employed for causal discovery since
the 1990s, using conditional independence relationships in data to uncover information
about the underlying causal structure. Algorithms such as Peter-Clark (PC) (Spirtes et al.,
2000) and Fast Causal Inference (FCI) (Spirtes et al., 1995) are popular, with PC assuming
causal sufficiency and FCI handling latent confounders. In cases without latent confounders,
score-based algorithms like the Greedy Equivalence Search (GES) (Chickering, 2002) aim
to find the causal structure by optimizing a score function. These methods provide asymp-
totically correct results, accommodating various data distributions and functional relations
but do not necessarily provide complete causal information as they usually output Markov
equivalence classes of causal structures (graphs within the same Markov equivalence class
have the same conditional independence relations among the variables).
    On the other hand, algorithms based on Functional Causal Models (FCMs) have exhib-
ited the ability to distinguish between different Directed Acyclic Graphs (DAGs) within the
same equivalence class, thanks to additional assumptions on the data distribution beyond
conditional independence relations. An FCM represents the effect variable as a function of
the direct causes and a noise term; it renders causal direction identifiable due to the indepen-
dence condition between the noise and cause: one can show that under appropriate assump-
tions on the functional model class and distributions of the involved variables, the estimated
noise cannot be independent from the hypothetical cause in the reverse direction (Shimizu
et al., 2006; Hoyer et al., 2008; Zhang and Hyvärinen, 2009). More recently, the General-
ized Independent Noise condition (GIN) (Xie et al., 2020) has demonstrated its potential
in learning hidden causal variables and their relations in the linear, non-Gaussian case.
    To equip both practitioners and researchers with computational tools, several packages
have been developed for or can be adapted for causal discovery. The Java library TETRAD
(Glymour and Scheines, 1986; Scheines et al., 1998; Ramsey et al., 2018) contains a variety
of well-tested causal discovery algorithms and has been continuously developed and main-
tained for over 40 years; R packages pcalg (Kalisch et al., 2012) and bnlearn (Scutari, 2010)
also include some classical constraint-based and score-based methods such as PC and GES.
However, these tools are based on Java or R, which may not align with the recent trend
favoring Python in certain communities, particularly within machine learning. While there
are Python wrappers available for these packages (e.g., py-tetrad (Andrew and Ramsey,
2023)/py-causal (Wongchokprasitti et al., 2019) for TETRAD, and Causal Discovery Tool-
box (Kalainathan et al., 2020) for pcalg and bnlearn), they still rely on Java or R. This
dependency can complicate deployment and does not cater directly to Python users seeking
to develop their own methods based on an existing codebase. Thus, there is a pronounced
need for a Python package that covers representative causal discovery algorithms across
all primary categories. Such a tool would significantly benefit a diverse range of users by
providing access to both classical methods and the latest advancements in causal discovery.
    In this paper, we describe causal-learn, an open-source python library for causal discov-
ery. The library incorporates an extensive range of causal discovery algorithms, providing
accessible APIs and thorough documentation to cater to a diversity of practical requirements

                                               2
                       Causal-learn: Causal Discovery in Python




and data assumptions. Moreover, it provides independent modules for specific functionali-
ties, such as (conditional) independence tests, score functions, graph operations, and evalua-
tion metrics, thereby facilitating custom needs and fostering the development of user-defined
methods. An essential attribute of causal-learn is its full implementation in Python, elimi-
nating dependencies on any other programming languages. As such, users are not required to
have expertise in Java or R, enhancing the ease of integration within the enormous and grow-
ing Python ecosystem and promoting seamless utilization for a range of computational and
scripting tasks. With causal-learn, modification and extensions based on the existing imple-
mentation of causal discovery methods also become plausible for developers and researchers
who may not be familiar with Java or R, which could significantly accelerate the progress in
related fields by lowering the threshold of the integration of causality into various pipelines.

2 Design
The design philosophy of causal-learn is centered around building an open-source, modular,
easily extensible and embeddable Python platform for learning causality from data and
making use of causality for various purposes. Due to the different goals, assumptions, and
techniques between causal learning and traditional learning tasks, newcomers to the field
often find it hard to get a clear picture of the developments in modern causality research.
Thus, we briefly introduce the algorithms and functionalities in causal-learn with a special
focus on their use cases and suitable application scenarios.

2.1 Search methods
Causal-learn covers representative causal discovery methods across all major categories with
official implementation of most algorithms. We briefly introduce the methods as follows. It
is worth noting that we are actively updating the library to incorporate latest algorithms.

   • Constraint-based causal discovery methods. Current algorithms under that cat-
     egory are PC (Spirtes et al., 2000), FCI (Spirtes et al., 1995), and CD-NOD (Huang
     et al., 2020). PC is a classical and widely-used algorithm with consistency guarantee
     under independent and identically distributed (i.i.d.) sampling assuming no latent
     confounders, the faithfulness assumption, and the causal Markov condition, which
     has been extensively applied in many fields. By continuously applying (conditional)
     independence tests on subsets of variables of increasing size in a smart way, its search
     procedure returns a Markov Equivalence Class (MEC), of which the graphical object
     consists of a mixture of directed and undirected edges, known as a Completed Partially
     Directed Acyclic Graph (CPDAG). PC is highly adaptable to various use cases, facil-
     itated by the selection of an appropriate independence test; it can handle data with
     different assumptions, such as Fisher-Z test (Fisher et al., 1921) for linear Gaussian
     data, Chi/G-squared test (Tsamardinos et al., 2006) for discrete data, and Kernel-
     based Conditional Independence (KCI) test (Zhang et al., 2011) for the nonparametric
     case. Moreover, causal-learn provides an extension, Missing-Value PC (MV-PC) (Tu
     et al., 2019), to address issues of missing data. Furthermore, we have implemented
     FCI for causal structures that include hidden confounders (it indicates the possible
     existence of hidden confounders whenever the possibility cannot be excluded, but it

                                               3
                                   Zheng et al.




  cannot help determine possible relations among them), and causal discovery from
  nonstationary/heterogeneous data (CD-NOD). These constraint-based methods offer
  wide applicability as they can accommodate various types of data distributions and
  causal relations, provided that appropriate conditional independence testing methods
  are utilized. However, genenerally speaking, they may not be able to determine the
  complete causal graph uniquely and, accordingly, there usually exist some undirected
  edges in the returned CPDAGs.


• Score-based causal discovery methods. Different from the search style of constraint-
  bed methods, score-based methods find the causal structure by optimizing a properly
  defined score function. Greedy Equivalence Search (GES) (Chickering, 2002) is a
  well-known two-phase procedure that directly searches over the space of equivalence
  classes. Similarly, exact search (e.g., A* (Yuan and Malone, 2013), Dynamic Program-
  ming (Silander and Myllymäki, 2006)), and permutation-based search (e.g., GRaSP
  (Lam et al., 2022)) apply different search strategies to return a set of the sparsest Di-
  rected Acyclic Graphs (DAGs) that contains the true model under assumptions strictly
  weaker than faithfulness. These score-based methods are versatile, able to accommo-
  date a wide array of data and causal relations by choosing suitable score functions,
  such as BIC (Schwarz, 1978) for linear Guassian data, BDeu (Buntine, 1991) for dis-
  crete data, and Generalized Score (Huang et al., 2018) for the nonparametric case.
  The choice of score function can be conveniently adjusted as a hyperparameter.


• Causal discovery methods based on constrained functional causal models.
  While constraint-based and score-based methods offer flexibility through the selection
  of an appropriate independence test or score function, they are limited to returning
  equivalence classes, yielding non-unique solutions where the causal direction between
  certain variable pairs remains indeterminate. In contrast, assuming specific Functional
  Causal Models (FCMs)–that is, functions in a particular functional class to specify
  how the effect is generated from its direct causes and noise–allows for the full deter-
  mination of the causal structure, albeit at the cost of certain trade-offs. Causal-learn
  incorporates algorithms based on several FCM variants, capable of producing unique
  causal directions. Examples include the linear non-Gaussian acyclic model (LiNGAM)
  (Shimizu et al., 2006) and its variant, i.e., DirectLiNGAM (Shimizu et al., 2011), which
  have been extensively applied for non-Gaussian noises with linear relations. VAR-
  LiNGAM (Hyvärinen et al., 2010), which combines LiNGAM with vector autoregres-
  sive models (VAR), to estimate both time-delayed and instantaneous causal relations
  from time series. RCD (Maeda and Shimizu, 2020), an extension of LiNGAM, allows
  for hidden confounders, while CAM-UV (Maeda and Shimizu, 2021) further extends
  this to the nonlinear additive noise case. In addition, the additive noise model (ANM)
  (Hoyer et al., 2008) has been proven to be identifiable in the presence of nonlinearity
  and additive noises. Furthermore, we have also incorporated the post-nonlinear (PNL)
  causal model (Zhang and Hyvärinen, 2009), a highly general form (with LiNGAM and
  ANM as special cases) that has been demonstrated to be identifiable in the generic
  case, barring five specific situations described in (Zhang and Hyvärinen, 2009).

                                          4
                        Causal-learn: Causal Discovery in Python




   • Causal representation learning: Finding causally related hidden variables.
     Latent variables play an instrumental role in a multitude of real-world scenarios, of-
     ten acting as hidden confounders that influence observed variables. Unfortunately,
     most existing methods may fail to produce convincing results in cases with latent
     variables (confounders). In causal-learn, we implement the Generalized Independent
     Noise (GIN) condition (Xie et al., 2020) for estimating linear non-Gaussian latent
     variable causal model, which allows causal relationships between latent variables and
     multiple latent variables behind any two observed variables. This promises to improve
     the detection and understanding of the complex, often hidden, causal structures that
     govern real-world phenomena.

    Besides, causal-learn also has Granger causality (Granger, 1969, 1980) implemented for
statistical but not causal1 time series analysis. Through the collective efforts of various
teams and the contributions of the open-source community, causal-learn is always under
active development to incorporate the most recent advancements in causal discovery and
make them available to both practitioners and researchers.

2.2 (Conditional) independence tests
In addition to its comprehensive search methods, causal-learn also provides a variety of
(conditional) independence tests as independent modules. Besides being an essential parts
of several search methods, these tests can also be independently utilized and seamlessly
integrated into existing statistical analysis pipelines. Currently,the library features a diverse
array of such tests including Fisher-z test (Fisher et al., 1921), Missing-value Fisher-z test,
Chi-Square test, Kernel-based conditional independence (KCI) test and independence test
(Zhang et al., 2011), and G-Square test (Tsamardinos et al., 2006), each with distinct
capabilities and benefits. The Fisher-z test is ideally suited for linear-Gaussian data, while
the Missing-value Fisher-z test addresses the challenges of missing values by implementing
a testwise-deletion approach. For categorical variables, the Chi-Square and G-Square tests
are most effective. For users interested in a nonparametric test or the case with mixed
categorical and continuous data types, the KCI test is an option. Overall, the range of tests
offered by causal-learn underscores its versatility in handling diverse data types.

2.3 Score functions
Moreover, a diverse range of score functions is available in causal-learn. These score func-
tions quantify the goodness of fit of a model to the data, a crucial measure in score-based
causal discovery methods, and can also be utilized independently for model selection in a
broader range. Among these, the Bayesian Information Criterion (BIC) score (Schwarz,
1978) is used extensively, offering a balance between model complexity and fit to the data.
Another important score function is the Bayesian Dirichlet equivalent uniform (BDeu) score
1. As mentioned by Granger, Granger causality is not necessarily true causality. In fact, If one assumes 1)
   that there is no latent confounding process, 2) that the data are sampled at the right causal frequency,
   and 3) that there are no instantaneous causal influences, then Granger causality defined by Granger
   (Granger, 1980) can be seen as causal relations that can be discovered from stochastic processes with
   constraints-based methods such as PC. Of course, if those assumptions are violated, one may still apply
   Granger causal analysis, but the estimated relations may not be true causal influences.


                                                    5
                                            Zheng et al.




    (Buntine, 1991). This score function, especially beneficial for discrete data, incorporates a
    uniform prior over the set of Bayesian networks. Additionally, the Generalized Score (Huang
    et al., 2018) is also available in causal-learn, which offers the flexibility to accommodate more
    complex scenarios and is beneficial for nonparametric cases where the true data-generating
    process does not align with the assumptions of BIC (linear Gaussian) or BDeu (discrete).

    2.4 Utilities
    Causal-learn further offers a suite of utilities designed to streamline the assembly of causal
    analysis pipelines. The package features a comprehensive range of graph operations encom-
    passing transformations among various graphical objects integral to causal discovery. These
    include Directed Acyclic Graphs (DAGs), Completed Partially Directed Acyclic Graphs
    (CPDAGs), Partially Directed Acyclic Graphs (PDAGs), and Partially Ancestral Graphs
    (PAGs). Additionally, to enhance the convenience of experimental processes, causal-learn
    features a set of commonly used evaluation metrics to appraise the quality of the causal
    graphs discovered. These metrics include precision and recall for arrow directions or adja-
    cency matrices, along with the Structural Hamming Distance (Acid and de Campos, 2003).

    2.5 Demos, documentation, and benchmark datasets
    The causal-learn package also contains extensive usage examples of all search methods,
    (conditional) independence tests, score functions, and utilities at
                 https://github.com/py-why/causal-learn/tree/main/tests.
    Furthermore, detailed documentation is available at
                      https://causal-learn.readthedocs.io/en/latest/.
    It is worth noting that it also includes a collection of well-tested benchmark datasets–
    since ground-truth causal relations are often unknown for real data, evaluation of causal
    discovery methods has been notoriously known to be hard, and we hope the availability
    of such benchmark datasets can help alleviate this issue and inspire the collection of more
    real-world datasets with (at least partially) known causal relations.

    3 Example
    In this section, let us demonstrate how causal-learn discovers causal relations from obser-
    vational data in one line of code. First, we could easily install the library via pip:

1   pip install causal - learn

    Then we are ready to take a look into the causal world. Causal discovery in Python is as
    simple as follows:

1   # apply PC with default parameters
2   cg = pc ( data )
3
4   # visualization
5   cg . draw_pydot_graph ()

    The visualization of the returned causal graph is shown in Figure 1.
                                                   6
                       Causal-learn: Causal Discovery in Python




 Figure 1: Visualization of the causal graph returned by causal-learn with PC algorithm.


4 Conclusion
The causal-learn library serves as a comprehensive toolset for causal discovery, significantly
advancing the field of causal analysis and its applications in domains such as machine learn-
ing. It provides a robust platform for not only applying causal analysis techniques but also
for facilitating the development of novel or enhanced algorithms. This is achieved by provid-
ing an infrastructure fully in Python that allows users to efficiently modify, extend, and tailor
existing implementations, contribute new ones, and maintain high-quality standards. Given
the current demand for causal learning and the rapid progress in this field, coupled with the
active development and contribution from our team and the community, the causal-learn li-
brary is poised to bring causality into an indispensable component across diverse disciplines.


Acknowledgments and Disclosure of Funding

We are grateful for the collective efforts of all open-source contributors that continue to fos-
ter the growth of causal-learn. Especially, we would like to thank Yuequn Liu, Zhiyi Huang,
Feng Xie, Haoyue Dai, Erdun Gao, Aoqi Zuo, Takashi Nicholas Maeda, Takashi Ikeuchi,
Madelyn Glymour, Ruibo Tu, Wai-Yin Lam, Ignavier Ng, Bryan Andrews, Yewen Fan, and
Xiangchen Song. The work of MG is supported in part by ARC DE210101624. The work of
RC is supported in part by National Key R&D Program of China (2021ZD0111501). This
project is partially supported by the National Institutes of Health (NIH) under Contract
R01HL159805, by the NSF-Convergence Accelerator Track-D award #2134901, by a grant

                                               7
                                        Zheng et al.




from Apple Inc., a grant from KDDI Research Inc, and generous gifts from Salesforce Inc.,
Microsoft Research, and Amazon Research.

References
Silvia Acid and Luis M de Campos. Searching for bayesian network structures in the space
   of restricted acyclic partially directed graphs. Journal of Artificial Intelligence Research,
   18:445–490, 2003.

Bryan Andrew and Joseph Ramsey.             py-tetrad, 2023.     URL https://github.com/
  cmu-phil/py-tetrad.

Wray Buntine. Theory refinement on bayesian networks. In Uncertainty proceedings 1991,
 pages 52–60. Elsevier, 1991.

David Maxwell Chickering. Optimal structure identification with greedy search. Journal of
  machine learning research, 3(Nov):507–554, 2002.

Ronald Aylmer Fisher et al. 014: On the” probable error” of a coefficient of correlation
  deduced from a small sample. 1921.

Clark Glymour and Richard Scheines. Causal modeling with the tetrad program. Synthese,
  68:37–63, 1986.

Clark Glymour, Kun Zhang, and Peter Spirtes. Review of causal discovery methods based
  on graphical models. Frontiers in genetics, 10:524, 2019.

Clive WJ Granger. Investigating causal relations by econometric models and cross-spectral
  methods. Econometrica: journal of the Econometric Society, pages 424–438, 1969.

Clive WJ Granger. Testing for causality: A personal viewpoint. Journal of Economic
  Dynamics and control, 2:329–352, 1980.

Patrik Hoyer, Dominik Janzing, Joris M Mooij, Jonas Peters, and Bernhard Schölkopf.
  Nonlinear causal discovery with additive noise models. Advances in neural information
  processing systems, 21, 2008.

Biwei Huang, Kun Zhang, Yizhu Lin, Bernhard Schölkopf, and Clark Glymour. Gener-
  alized score functions for causal discovery. In Proceedings of the 24th ACM SIGKDD
  international conference on knowledge discovery & data mining, pages 1551–1560, 2018.

Biwei Huang, Kun Zhang, Jiji Zhang, Joseph D Ramsey, Ruben Sanchez-Romero, Clark
  Glymour, and Bernhard Schölkopf. Causal discovery from heterogeneous/nonstationary
  data. J. Mach. Learn. Res., 21(89):1–53, 2020.

Aapo Hyvärinen, Kun Zhang, Shohei Shimizu, and Patrik O Hoyer. Estimation of a struc-
 tural vector autoregression model using non-gaussianity. Journal of Machine Learning
 Research, 11(5), 2010.

                                               8
                      Causal-learn: Causal Discovery in Python




Diviyan Kalainathan, Olivier Goudet, and Ritik Dutta. Causal discovery toolbox: Uncov-
  ering causal relationships in python. The Journal of Machine Learning Research, 21(1):
  1406–1410, 2020.

Markus Kalisch, Martin Mächler, Diego Colombo, Marloes H. Maathuis, and Peter
 Bühlmann. Causal inference using graphical models with the R package pcalg. Jour-
 nal of Statistical Software, 47(11):1–26, 2012. doi: 10.18637/jss.v047.i11.

Wai-Yin Lam, Bryan Andrews, and Joseph Ramsey. Greedy relaxations of the sparsest
 permutation algorithm. In Uncertainty in Artificial Intelligence, pages 1052–1062. PMLR,
 2022.

Takashi Nicholas Maeda and Shohei Shimizu. Rcd: Repetitive causal discovery of linear
  non-gaussian acyclic models with latent confounders. In International Conference on
  Artificial Intelligence and Statistics, pages 735–745. PMLR, 2020.

Takashi Nicholas Maeda and Shohei Shimizu. Causal additive models with unobserved
  variables. In Uncertainty in Artificial Intelligence, pages 97–106. PMLR, 2021.

Joseph D Ramsey, Kun Zhang, Madelyn Glymour, Ruben Sanchez Romero, Biwei Huang,
  Imme Ebert-Uphoff, Savini Samarasinghe, Elizabeth A Barnes, and Clark Glymour.
  Tetrad—a toolbox for causal discovery. In 8th international workshop on climate in-
  formatics, page 29, 2018.

Richard Scheines, Peter Spirtes, Clark Glymour, Christopher Meek, and Thomas Richard-
  son. The tetrad project: Constraint based aids to causal model specification. Multivariate
  Behavioral Research, 33(1):65–117, 1998.

Gideon Schwarz. Estimating the dimension of a model. The annals of statistics, pages
  461–464, 1978.

Marco Scutari. Learning bayesian networks with the bnlearn R package. Journal of Statis-
 tical Software, 35(3):1–22, 2010. doi: 10.18637/jss.v035.i03.

Shohei Shimizu, Patrik O Hoyer, Aapo Hyvärinen, Antti Kerminen, and Michael Jordan.
  A linear non-Gaussian acyclic model for causal discovery. Journal of Machine Learning
  Research, 7(10), 2006.

Shohei Shimizu, Takanori Inazumi, Yasuhiro Sogawa, Aapo Hyvarinen, Yoshinobu Kawa-
  hara, Takashi Washio, Patrik O Hoyer, Kenneth Bollen, and Patrik Hoyer. Directlingam:
  A direct method for learning a linear non-gaussian structural equation model. Journal of
  Machine Learning Research-JMLR, 12(Apr):1225–1248, 2011.

Tomi Silander and Petri Myllymäki. A simple approach for finding the globally optimal
  bayesian network structure. In Proceedings of the Twenty-Second Conference on Uncer-
  tainty in Artificial Intelligence, pages 445–452, 2006.

Peter Spirtes, Christopher Meek, and Thomas Richardson. Causal inference in the pres-
  ence of latent variables and selection bias. In Proceedings of the Eleventh conference on
  Uncertainty in artificial intelligence, pages 499–506, 1995.

                                             9
                                      Zheng et al.




Peter Spirtes, Clark N Glymour, Richard Scheines, and David Heckerman. Causation,
  prediction, and search. MIT press, 2000.

Ioannis Tsamardinos, Laura E Brown, and Constantin F Aliferis. The max-min hill-climbing
  bayesian network structure learning algorithm. Machine learning, 65:31–78, 2006.

Ruibo Tu, Cheng Zhang, Paul Ackermann, Karthika Mohan, Hedvig Kjellström, and Kun
 Zhang. Causal discovery in the presence of missing data. In The 22nd International
 Conference on Artificial Intelligence and Statistics, pages 1762–1770. PMLR, 2019.

Chirayu (Kong) Wongchokprasitti, Harry Hochheiser, Jeremy Espino, Eamonn Maguire,
 Bryan Andrews, Michael Davis, and Chris Inskip. bd2kccd/py-causal v1.2.1, December
 2019. URL https://doi.org/10.5281/zenodo.3592985.

Feng Xie, Ruichu Cai, Biwei Huang, Clark Glymour, Zhifeng Hao, and Kun Zhang. Gen-
  eralized independent noise condition for estimating latent variable causal graphs. In
  NeurIPS, 2020.

Changhe Yuan and Brandon Malone. Learning optimal bayesian networks: A shortest path
 perspective. Journal of Artificial Intelligence Research, 48:23–65, 2013.

K Zhang and A Hyvärinen. On the identifiability of the post-nonlinear causal model. In 25th
  Conference on Uncertainty in Artificial Intelligence (UAI 2009), pages 647–655. AUAI
  Press, 2009.

Kun Zhang, Jonas Peters, Dominik Janzing, and Bernhard Schölkopf. Kernel-based condi-
 tional independence test and application in causal discovery. In Proceedings of the Twenty-
 Seventh Conference on Uncertainty in Artificial Intelligence, pages 804–813, 2011.




                                            10
```
