---
source: https://arxiv.org/abs/2108.13518
description: Sharma et al. argue causal estimates depend on explicit assumptions and describe DoWhy support for expressing and partially validating those assumptions
captured: 2026-07-16
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

Author: Amit Sharma, Vasilis Syrgkanis, Cheng Zhang, and Emre Kiciman
Source: https://arxiv.org/abs/2108.13518 (PDF: https://arxiv.org/pdf/2108.13518)
Date: arXiv:2108.13518v1, 27 August 2021

Capture note: text extracted from the arXiv PDF. Mathematical notation, figures, and tables are reproduced as the extractor rendered them.

```text
                                                                         DoWhy: Addressing Challenges in
                                                                    Expressing and Validating Causal Assumptions


                                                                   Amit Sharma 1 Vasilis Syrgkanis 1 Cheng Zhang 1 Emre Kıcıman 1


                                                                   Abstract                                  process based on the assumptions, identifying the desired
arXiv:2108.13518v1 [cs.LG] 27 Aug 2021




                                              Estimation of causal effects involves crucial as-              effect based on the causal model, and estimating the effect.
                                              sumptions about the data-generating process, such              In recent years, there has been substantial progress in better
                                              as directionality of effect, presence of instrumen-            estimation methods for causal inference, in part by fusing
                                              tal variables or mediators, and whether all rele-              machine learning algorithms with the traditional effect esti-
                                              vant confounders are observed. Violation of any                mation methods (Wager & Athey, 2018; Athey et al., 2019;
                                              of these assumptions leads to significant error                Hartford et al., 2017; Chernozhukov et al., 2017; Shalit et al.,
                                              in the effect estimate. However, unlike cross-                 2017; Alaa & van der Schaar, 2017; Powers et al., 2018;
                                              validation for predictive models, there is no global           Lewis & Syrgkanis, 2018; Syrgkanis et al., 2019; Foster &
                                              validator method for a causal estimate. As a re-               Syrgkanis, 2019; Bennett et al., 2019; Jacob, 2021; Kennedy,
                                              sult, expressing different causal assumptions for-             2020; Nie & Wager, 2021; Dikkala et al., 2020). Specifi-
                                              mally and validating them (to the extent possible)             cally, in addition to estimating the average treatment effect
                                              becomes critical for any analysis. We present                  (ATE), recent methods allow estimation of fine-grained con-
                                              DoWhy, a framework that allows explicit decla-                 ditional effects on based on given covariates, the conditional
                                              ration of assumptions through a causal graph and               average causal effect (CATE). Given an observed dataset,
                                              provides multiple validation tests to check a sub-             many of these methods claim to estimate the causal effect
                                              set of these assumptions. Our experience with                  of an intervention, even under heterogeneity of the effect
                                              DoWhy highlights a number of open questions                    across units, high-dimensional data, and non-linear effects.
                                              for future research: developing new ways beyond
                                              causal graphs to express assumptions, the role of              The challenge, however, is that the prerequisites for the
                                              causal discovery in learning relevant parts of the             estimation task—building a causal model or graph for the
                                              graph, and developing validation tests that can bet-           problem—have not kept pace with the advances in estima-
                                              ter detect errors, both for average and conditional            tion. As a result, advances in estimation do not immediately
                                              treatment effects. DoWhy is available at https:                transfer to the practical process of causal inference because
                                              //github.com/microsoft/dowhy.                                  estimation methods assume that the causal graph has already
                                                                                                             been built and available. In practice, obtaining plausible
                                                                                                             assumptions to develop the causal graph either by human
                                                                                                             experts or by causal discovery algorithms is potentially the
                                         1. Introduction
                                                                                                             biggest challenge of doing causal analysis and that is often
                                         Given observed data, causal inference is the process of us-         overlooked in the recent causal machine learning literature.
                                         ing domain assumptions to estimate the effect of a desired          Moreover, educating users about causal machine learning
                                         action. Formally, a causal effect is always defined w.r.t. to a     algorithms (e.g., what are the causal graph assumptions that
                                         causal model (e.g., a structural causal model (Pearl, 2009))        are implicitly being made by these techniques), so that they
                                         that encodes assumptions that typically cannot be learned           can construct the appropriate datasets where these assump-
                                         from observed data. Therefore, in practice, causal inference        tions are satisfied is the biggest challenge in adoption and
                                         involves a sequence of steps that start with specifying the         correct use of these statistically powerful techniques. In this
                                         necessary assumptions: asserting domain assumptions, con-           paper, we highlight the fundamental importance of these
                                         structing a causal model or graph for the data-generating           assumptions, describe a framework for causal inference that
                                           1
                                                                                                             helps analysts to express and test those assumptions, and
                                             Microsoft Research. Correspondence to: Amit Sharma              propose open questions for future research.
                                         <amshar@microsoft.com>.
                                                                                                             Assumptions are fundamental to causal inference. Ev-
                                         Workshop on the Neglected Assumptions in Causal Inference           ery causal estimate depends on assumptions that cannot be
                                         (NACI) at the 38 th International Conference on Machine Learning,
                                         2021                                                                fully tested from observed data. Importantly, the bias due to
                      DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

these assumptions does not wash out even with infinite data.                            Estimator                                 Estimator
Take for example, the common assumption for almost all                                  y~t+w+z                                    y~t+m
CATE estimators, that there is a set of known confounders                               y~t+w (Correct)                            y~t (Correct)
(common causes) of the treatment and outcome. What hap-                       0.030                                 1.25
pens if one of the confounders is actually an instrumental                    0.025                                 1.00
variable or a mediator? If it is an instrumental variable, then               0.020




                                                                                                          Density
                                                                    Density
                                                                                                                    0.75
conditioning on the instrumental variable will lead to a high                 0.015
                                                                                                                    0.50
variance estimate. In this case, the error is in the modelling                0.010
(or identification) phase whereas it may appear as a problem                  0.005                                 0.25
with the estimator’s variance properties. If a mediator is                    0.000                                 0.00
                                                                                   200 100 0 100 200                       0           5           10
incorrectly assumed as a confounder, the estimate will be                            Estimated Effect                          Estimated Effect
biased but the error may not even be detectable. Finally,           (a) DGP: w → {t, y}; z → (b) DGP: t → m → y. m is a
there can always be unknown and unobserved confounders              t; t → y. z is an instrument. mediator from t to y.
that can lead to errors. Sec. 2 shows simple examples on the
difficulty of catching modelling versus estimation errors.        Figure 1. Distribution of effect estimates under correct and incor-
                                                                  rect identification. A data scientist works only with a single dataset;
The end result is that we are left with advanced estimators
                                                                  however, to illustrate the distribution of the estimator, in each fig-
with confidence intervals that assume that the modelling          ure, we sample 100 datasets from the same data-generating process:
step is already correct, and thereby overestimate the cer-        blue lines show the correctly identified estimator, orange lines show
tainty in their estimates. Importantly, there is no clear way     the faulty estimator, and dotted line shows the true causal effect.
of incorporating the uncertainty or bias due to errors in the
modelling or identification phase. Moreover, there is no
reliable method to validate an estimate after the full causal
analysis, unlike in supervised machine learning where cross-      2. The importance of modelling assumptions
validation can determine the quality of any predictor. In         Biases in estimation due to unobserved confounders are
general, therefore, it is difficult to judge the quality of any   well-known (Greenland, 2003; Robins et al., 2000) and can
obtained causal estimate from observed data, since the “cor-      even change the sign of an estimated effect. While unob-
rect” causal effect depends on the modelling assumptions.         served variables are a significant challenge to any causal
DoWhy: Expressing and validating assumptions.                     analysis, estimation can go wrong even when all variables
DoWhy is a popular open-source python library for causal          are observed. To complicate matters, it is usually difficult
inference, having more than 300K downloads and used               to even detect the error. And when errors are detected, it is
across many scenarios and fields. Sec. 3 discusses how            difficult to know why: is it a modeling/identification error
DoWhy is designed to make assumptions “first-class” citi-         or an estimation error?
zens of a causal analysis. Its API implements causal infer-       To illustrate the difficulty of detecting errors in causal esti-
ence in four steps: model, identify, estimate, and validate.      mation, we present two simple examples. The first example
The first two steps focus on expressing causal assumptions        shows a faulty estimator that leads to high variance estimate.
transparently using a causal graph while the last step pro-       It is possible to detect such high variance, but hard to de-
vides multiple methods to validate the resultant effect es-       termine the reason for it. The second example shows an
timator based on the assumptions. The API structure is            estimator with bias where it is not even possible to detect
designed to help understand the interplay of the different        that the effect estimate is incorrect. In particular, these es-
steps in analysis. For example, to evaluate robustness of         timators cannot recover the average treatment effect (ATE)
the estimate, one may try the same estimator with different       over all units, which is a simpler problem than estimating the
causal models or identification strategies; or the same model     heterogeneous conditional average treatment effects (CATE)
with different estimators and validation tests to find the best   that most recent work aims to estimate.
estimator for a dataset.
                                                                  Throughout this paper, the goal is to estimate causal effect
Open questions. In Sec. 4, we describe the practical chal-        of a treatment variable t on the outcome y, E[y|do(t =
lenges in applying causal inference through our experience        1)] − E[y|do(t = 0)]. As mentioned above, we consider
in working with users of DoWhy. One of the biggest chal-          the simplest case where all variables in the causal graph are
lenges is that a causal graph is often difficult to obtain and    observed and relationship of y with other variables is linear.
there is a need for developing alternative abstractions for
inputting causal assumptions. Moreover, there are funda-          2.1. High variance estimate due to instrument
mental challenges to building robust validation tests using
observed data and interpreting their results.                     Consider a dataset with four variables: treatment t, outcome
                                                                  y and two covariates (z and w). Using the backdoor crite-
                       DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

rion, a data scientist conditions on z and w to estimate the       to detect the quality of a predictive model and thereby as-
effect of t on y. In this case, they use linear regression since   certain whether the model’s assumptions were plausible. In
it is known that the functional form for y is linear. However,     the absence of a global validator to choose among causal
they observe that the resultant estimate has a high variance,      estimators, there are two key challenges:
as depicted in Fig. 1(a). High-variance can be detected, for
                                                                     1. What are the right causal assumptions? The prac-
example, by creating multiple bootstrapped datasets and
                                                                        tice of modeling assumptions (i.e., translating domain
repeating estimation on each of them. To decrease variance,
                                                                        knowledge into a causal graph) and the implications of
data scientists can apply more advanced estimation methods
                                                                        these assumptions for identification and estimation.
or can collect more data.
                                                                     2. How to check those assumptions? The practice of
The above solutions presume that the problem is due to the              validating causal assumptions to the extent possible
estimator, but it is equally possible that the problem is in            through tests and sensitivity analysis, since observa-
the identification of effect. What if one of the covariates             tional causal inference tasks has no ground-truth data
is an instrumental variable instead of a common cause?                  available to evaluate on.
If that’s the case, then the correct remedy is to remove
                                                                   We believe that the right abstraction for causal analysis can
that variable from the list of confounders and proceed as
                                                                   help lay equal focus on these two questions, in addition to
usual with the backdoor estimation. As it turns out, z is an
                                                                   estimation. To this end, we discuss DoWhy, an end-to-end
instrumental variable in the dataset for Fig. 1(a) (see DGP in
                                                                   library for causal inference, that organizes causal analysis
Appendix) and therefore the correct estimator is to condition
                                                                   around the four key steps: Model, Identify, Estimate, and
on only w, as shown by the blue line. It is not possible to
                                                                   Refute/Validate. Model encodes prior knowledge as a for-
distinguish from observed data whether the estimation or
                                                                   mal causal graph, identify uses graph-based methods to
identification step step causes the high variance. In practice,
                                                                   identify the causal effect, estimate uses statistical methods
we need domain knowledge or extra assumptions to rule out
                                                                   for estimating the identified estimand, and finally refute
identification flaws before dealing with estimation issues.
                                                                   tries to refute the obtained estimate by testing robustness to
                                                                   initial model’s assumptions.
2.2. High bias estimate due to mediator
                                                                   model = CausalModel(data, graph,
Consider the same data scientist having a different dataset,           treatment, outcome)
treatment t, outcome y, and a variable m. Suspecting m to          estimand = model.identify_effect()
be a common cause confounder, they condition on m and              estimate = model.estimate_effect(estimand,
obtain an effect estimate of zero, as shown in Fig. 1(b). The       method_name="propensity_score_weighting")
estimate is precise with small confidence intervals and one        refute = model.refute_estimate(estimand,
                                                                       estimate,
may be tempted to conclude that the treatment has no effect.           method_name="placebo_treatment_refuter")
But what if the variable is a mediator on the path from t
and y, and not a confounder? In that case, the estimate is         The focus on all the four steps, going from data to the final
biased (assuming that the goal is to estimate the total effect     causal estimate (along with a measure of its robustness) al-
of treatment (which is often the case) and not just the direct     lows a user to formally express and test causal assumptions.
effect). The true estimate is obtained without conditioning,       None of the existing libraries for causal inference support
as shown by blue line in Fig. 1(b) (effect estimate of 10).        an easy way to conduct multiple refutations, even though
For an analyst relying on the estimate’s precision on the          sensitivity and robustness checks are an important part of
observed data, there is no way to know that they have made         causal analysis. Most libraries in Python and R focus only
an error in their analysis. Any remedy for such errors can         on one of the steps. For example, pcalg (Kalisch et al.,
only come from assumptions that the data scientist brings          2012) and dagitty (Textor et al., 2016) focus on modeling;
from external knowledge. No amount of estimation tuning is         causaleffect (Tikka & Karvanen, 2017) on identification;
going to fix this, and one will never know the error (unless       and EconML (Battocchi et al., 2019) and CausalML (Chen
there is a randomized experiment to confirm the effect).           et al., 2020) on estimation. While the Ananke library (Bhat-
Finally, as mentioned above, these problems exacerbate in          tacharya et al., 2020) has support for modelling, identifica-
the presence of unobserved confounders.                            tion and estimation, it supports a limited set of estimation
                                                                   methods. Instead, DoWhy is designed as a general API
                                                                   framework that can work with externally available imple-
3. DoWhy framework                                                 mentations of methods for each step. For example, DoWhy
The above problems occur due to the lack of a reliable             integrates seamlessly with EconML and CausalML pack-
validation mechanism for causal estimates, unlike in super-        ages and allows calling any of their estimation methods
vised prediction tasks where one can use cross-validation          (e.g., method name=‘econml.dml.DML’ for the dou-
                                                                   ble ML estimator (Chernozhukov et al., 2017)).
                       DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

Below we discuss how DoWhy’s API addresses the two                 Recent work on developing validation tests for causal esti-
challenges described above: the expression of causal as-           mators can be divided into two types. Similar to the cross-
sumptions, and the validation of causal estimators.                validation loss metric, the first type of methods (Alaa &
                                                                   Van Der Schaar, 2019; Schuler et al., 2018; Powers et al.,
3.1. Expressing causal assumptions                                 2018; Athey & Wager, 2019; Nie & Wager, 2021; Foster &
                                                                   Syrgkanis, 2019; Dwivedi et al., 2020) use observed data to
Based on the seminal work of Pearl (Pearl, 2009) in ex-            create a metric that denotes the quality of an obtained causal
pressing a causal model through graphs, causal graphs have         estimate. However, in the absence of ground-truth data with
emerged as a popular abstraction for representing domain           the true causal effects, and in the absence of experimental
assumptions. Besides their presentational simplicity, causal       data from a randomized-controlled trial, these methods use
graphs are also backed by do-calculus (Pearl, 2012), a set         secondary estimators to estimate auxiliary predictive models
of rules and associated algorithms for identifying the causal      that are being used in the quality metric. The validity of
effect in any given causal graph.                                  these metrics as evaluators of the quality of the causal effect,
Before starting any causal analysis, DoWhy stipulates that         depends on the quality of these auxiliary estimators. Even
the user provide a causal graph over the observed variables.       though many of these techniques argue that the estimation
Drawing the causal graph encourages a user to think about          error of these auxiliary models has a second order impact
the relationships between variables and determine the type         on the validity of the metric, this is only the case if these
for different variables (e.g., are they a confounder, instru-      auxiliary estimators are already quite good and importantly
mental variable, or a mediator?). Based on the causal graph,       are non-parametrically consistent. Achieving these require-
DoWhy uses graph-based criteria and do-calculus to find            ment can be sometimes hard, if not harder, than the task of
expressions that can identify the causal effect. That is, it au-   fitting the final causal model.
tomatically identifies the causal effect (including mediation      The second type of methods (Neal et al., 2020) construct a
effects) using different identification algorithms, including      new, simulated dataset where the full data-generating pro-
Back-door, Front-door criterion (Pearl, 2009), Instrumental        cess (DGP) is known and hence the ground-truth causal
Variables, and the ID algorithm (Shpitser & Pearl, 2008).          effect is also known. Candidate estimators are evaluated
Given that identification is automatic given a causal graph,       on their error on the new dataset, hoping that the extent of
the focus is on obtaining the causal graph and making sure         errors on the new dataset will transfer to the original dataset
that it expresses the desired causal assumptions. The benefit      too. The challenge here is to create a simulated dataset that
of expressing assumptions formally is that their effect on         is close enough to the original dataset, but yet it is possible
the downstream estimation tasks can be quantified easily.          to ascertain relevant parts of its DGP to know the ground-
For example, a user may construct multiple versions of the         truth causal effect. Different simulated datasets may give a
graph based on their domain knowledge, and then rerun the          different ranking of candidate estimators.
estimation method for these graphs to observe how different        Acknowledging the limitations in developing a ground-truth
causal assumptions affect the final estimate. In the exam-         auxiliary metric from the first type of methods and the strong
ple discussed in Sec. 2.2, a user may supply two causal            assumptions therein, DoWhy provides a suite of validation
graphs: one with m as a confounder and one with m as               tests based on creating simulated datasets similar to the
a mediator. Both these graphs can be used to identify the          original one, where the ground-truth causal effect is already
effect and construct an estimator, and the differences in the      known. It also provides sensitivity analyses to help evaluate
resultant estimates will help understand the significance of       causal estimators in conjunction with domain knowledge.
the different causal assumptions for the particular dataset.       It is important to note here that causal assumptions cannot
                                                                   be fully verified. Rather, the intent is to validate some
3.2. Validating causal assumptions and estimators                  necessary conditions entailed from a given assumption, and
While causal graphs provide a formal abstraction for express-      thereby filter out the models that do not satisfy them. Below
ing causal assumptions, no such well-accepted method ex-           we outline the supported validation tests.
ists for validating those assumptions. Most work on testing        Replacing treatment or outcome. These tests replace the
causal assumptions focuses on sensitivity analyses (Rosen-         treatment or outcome variable to create a new dataset where
baum, 2014; Robins et al., 2000; Veitch & Zaveri, 2020) that       the causal effect is trivially known. These are the closest
describe how an obtained estimate changes if we change             to opaque-box cross-validation for predictive models—they
any of the identifying assumptions. An analyst can use the         can detect errors but not reveal which of the assumptions
sensitivity of the estimate to ascertain its robustness, per-      is violated. These tests are global in the sense that they
haps based on plausible values of the assumption violations.       can detect error due to any part of the analysis: incorrect
However, a key limitation is the qualitative nature of such        identification, estimator, or even implementation bugs.
analyses that prevent development of a more general test.
                      DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

   • Placebo Treatment: When we replace the true treat-           from domain experts. Often, it is difficult for domain experts
     ment variable with an independent random variable,           to appropriately circumscribe the causal factors relevant to
     the estimated causal effect should go to zero.               their study, separating exogenous from endogenous factors,
   • Dummy Outcome: When we replace the true out-                 and capturing key relationships at an appropriate abstrac-
     come variable with an independent random variable,           tion. Sometimes, domain experts do not understand core
     the estimated causal effect should go to zero.               causal concepts, confusing correlational with causal rela-
   • Simulated Outcome (Neal et al., 2020): When we               tionships. Perhaps most challenging is when even domain
     replace the outcome with a simulated outcome based           experts do not have a sufficient understanding of the given
     on a known data-generating process close to the given        system. Especially when a large set of variables is included
     dataset, the estimated causal effect should match the        in the dataset, it is a daunting and cumbersome task to de-
     effect parameter from the data-generating process.           fine a full causal model, capturing the relationship among
                                                                  a potentially high-dimensional set of variables. There are
Adding “unobserved” confounders. These methods add
                                                                  several promising possibilities for addressing these issues,
random confounders where it is known that the effect should
                                                                  by allowing human input in a different format than graphs.
not change, or introduce correlated confounders to study the
sensitivity of an estimate to unobserved confounding.             Machine teaching. Machine teaching methods developed
                                                                  to elicit domain knowledge for conventional machine learn-
   • Add Random Common Cause: Adding a synthetic
                                                                  ing models may be adaptable to elicit causal domain knowl-
     independent random variable as a common cause
                                                                  edge (Simard et al., 2017). Such a human-in-the-loop
     should not affect the estimated causal effect.
                                                                  approach may allow experts to refine their assumptions
   • Add Unobserved Common Causes: The effect es-
                                                                  through iterative probing. For example, a system might
     timate should not be too sensitive to additions of a
                                                                  guide experts by presenting them with what-if scenarios,
     common cause (confounder) to the dataset that is cor-
                                                                  data-driven feedback, or other mechanisms to solicit con-
     related with the treatment and the outcome?
                                                                  founders, mediators, and other common causal structures.
Creating subsets of the dataset. These methods use sub-
                                                                  Expressing assumptions as constraints. Often people
sets or bootstrap samples to check variance of the estimator.
                                                                  may not be able to express causal relationships as edges be-
   • Data Subsets Validation: When we replace the given           tween variables, but provide constraints that the causal graph
     dataset with a randomly selected subset, the estimated       should satisfy. The constraint may be pair-wise indepen-
     effect should not change significantly.                      dence constraints, no direct-effect constraint, monotonicity
   • Bootstrap Validation: When we replace the dataset            constraint (Effect of A on B is positive), and so on. These
     with bootstrapped samples from the same dataset, the         constraints do not necessarily lead to a unique graph and
     estimated effect should not change significantly.            thus require modified identification and estimation methods.
Many of the above methods aim to refute the full causal           High-level causal graphs. For some tasks, we may be able
analysis, including modeling, identification and estimation       to use minimal causal graph representations rather than a
(as in Placebo Treatment or Dummy Outcome) whereas oth-           full description of a system. In domains like images or text,
ers refute a specific step (e.g., Data Subsets and Bootstrap      it is unlikely that a causal graph over the raw inputs would
only test the estimation step). Borrowing terminology from        be meaningful. For example, in the computer vision task
the software testing literature, the former can be called “in-    of object recognition, the causal relationships may be at
tegration” tests whereas the latter can be called “unit” tests.   level of high-level features object shape, color, and texture,
                                                                  rather than relationships expressible at the granularity of
4. Open research questions                                        individual pixels. For prediction tasks, high-level causal
                                                                  graphs have been proposed that help enforce certain invari-
Through our work and the many users of DoWhy, we have             ances (Arjovsky et al., 2019). It will be useful to extend
improved our understanding of the challenges people face          such high-level graphs to effect inference tasks.
while applying causal methods. Here we describe three of
                                                                  Sufficient partial graphs. Moreover, in many application
the most critical fundamental research challenges.
                                                                  settings, there is a target outcome variable of interest and a
                                                                  known treatment variable and typically only a subset of the
4.1. Eliciting assumptions from experts                           graph needs to be defined to devise an identification strat-
Causal methods require causal domain knowledge, ex-               egy (i.e., specifying confounders, instruments, mediators).
pressed in the form of a Directed Acyclic Graph (DAG)             Eliciting a sufficient partial causal graph will likely require
or a Structural Causal Model (SCM), to guide the causal           both interaction and iteration with a domain expert, and new
reasoning task. Despite the seeming user-friendliness of          strategies for testing the validity threat posed by unidentified
DAGs, we find it is often difficult to elicit such knowledge      relationships in the context of a particular data set.
                       DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

4.2. Causal discovery methods                                      do not agree? Can we create better, more robust tests?
Causal discovery methods (Spirtes et al., 2000; Peters et al.,     Interpreting violations of assumptions. We have found
2017; Glymour et al., 2019) may assist domain experts in           that understanding and interpreting the results of sensitivity
identifying key structures, and for validating a given DAG’s       analyses and refutation tests is not always straightforward.
plausability in the context of specific data set. In addition to   For example, if a data scientists collects multiple observa-
domain knowledge, one can consider using causal discovery          tional data sets from a system, and a given refutation test
methods to determine the causal graph. However, the fields         fails on only one of them, should the data scientist trust
of causal discovery and inference have evolved separately          results from any of the data sets?
and many challenges remain for causal discovery to be
                                                                   A related question is to understand when can sensitivity anal-
useful in the downstream effect inference task.
                                                                   yses and validation tests help us choose between estimators.
Incorporating domain knowledge. In many applications,              Are there specific dataset properties or DGP properties that
we may have partial domain knowledge. To obtain the most           make validation tests more conclusive? Another direction
accurate causal graph, utilizing both domain knowledge             is to design validation tests as debugging methods in the
and causal discovery methods would be critical. However,           process of improving an estimator: a good estimator has the
most causal discovery algorithms are designed without a            fewest failed validation tests. This has parallels in assessing
trivial way to incorporate the domain knowledge. Thus, it is       robustness and out-of-distribution generalization of predic-
important to design an interactive system that allows users        tive models (Ribeiro et al., 2020; Dash et al., 2020), where
to express their partial graph, obtain the discovered graph,       perturbation and other stress tests have been proposed.
and then update it based on domain knowledge. We also
                                                                   Building better validation tests. Finally, there is the fun-
need to build discovery algorithms that can work iteratively
                                                                   damental question on the limits to validation testing from
with partial domain knowledge.
                                                                   observed data. While there may be a natural limit on general
Graph representations. Without experimental data or ad-            validators, a promising direction is to develop specific val-
ditional assumptions, most discovery algorithms can only           idators based on known assumptions. For example, would
identify the causal graph up to Markov equivalent classes          validators be more powerful if we knew the direction of
and the output is represented as, for example, complete par-       the confounding effect, monotonicity of relationships, or
tial DAG (CPDAG), acyclic directed mixed graphs (ADMG)             specific independence constraints (and that are known to be
and partial ancestral graphs (PAG) (Spirtes et al., 2000; Pe-      true)? Recent progress has been made in some of these direc-
ters et al., 2017; Bhattacharya et al., 2021). However, causal     tions (Cinelli & Hazlett, 2020; Jesson et al., 2021), but there
inference typically requires one DAG and needs to be ex-           remains many opportunities for more domain-expert guided
tended to handle these formulations.                               validation tests, to improve on their practical relevance.
Additional untestable assumptions. Use of causal discov-           Given that randomized data is the gold-standard to evaluate
ery algorithms will include additional assumptions on the          a causal estimate, a second direction is to explore how much
causal inference pipeline. Markov condition and faithful-          randomized data is needed. Can validation methods be used
ness assumptions are the most common ones. Functional              alongside randomized data, and reduce the amount of ran-
causal models (Shimizu et al., 2006; Zhang & Hyvärinen,           domized data needed? Can we close the circle and automate
2009; 2010), which can be used to discovery the unique             the generation of candidate experiments that would validate
DAG require further assumptions regarding functional and           an effect estimate, based on testing specific assumptions
noise form of the structured equations. It is unclear how          that a domain expert may flag? (Hyttinen et al., 2013)
these assumptions will interact with the assumptions of the
downstream effect inference task, and how the errors may           5. Conclusion
propagate. More work is needed on combining discovery
and effect inference as a single task and determining the          We highlighted the importance of modeling assumptions
quality of estimators possible under the scenario, includ-         in causal effect estimation, and how this provided the mo-
ing concerns such as multiple testing due to different graph       tivation for including of modeling and validation as first
structures and invalidity of subsequent p-values from the es-      class stages in the DoWhy API. We see the improvement of
timation methods deployed on the discovered causal graph.          modeling assumptions and their validation as a research area
                                                                   critical to broadening the reliable usage of causal methods
4.3. Validating causal assumptions                                 in practice. Based on our experiences, we highlight three
                                                                   areas of open research questions to improve the elicitation
Given the impossibility of a global validator metric for           of assumptions from experts, the incorporation of causal
causal effect, there will always be multiple validation tests      discovery methods across the causal inference process, and
to choose from. How does one choose estimators when tests          opportunities to improve the validation of assumptions.
                      DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

References                                                      Dikkala, N., Lewis, G., Mackey, L., and Syrgkanis, V.
                                                                  Minimax estimation of conditional moment models. In
Alaa, A. and Van Der Schaar, M. Validating causal inference
                                                                  NeurIPS, volume 33, pp. 12248–12262. Curran Asso-
  models via influence functions. In ICML, pp. 191–201.
                                                                  ciates, Inc., 2020.
  PMLR, 2019.
Alaa, A. M. and van der Schaar, M. Bayesian inference of        Dwivedi, R., Tan, Y. S., Park, B., Wei, M., Horgan, K.,
  individualized treatment effects using multi-task gaussian     Madigan, D., and Yu, B. Stable discovery of interpretable
  processes. In NeurIPS, volume 30. Curran Associates,           subgroups via calibration in causal studies. International
  Inc., 2017.                                                    Statistical Review, 2020.

Arjovsky, M., Bottou, L., Gulrajani, I., and Lopez-             Foster, D. J. and Syrgkanis, V. Statistical learning with a
  Paz, D. Invariant risk minimization. arXiv preprint             nuisance component. In Learning Theory, volume 99 of
  arXiv:1907.02893, 2019.                                         PMLR, pp. 1346–1348, Phoenix, USA, 25–28 Jun 2019.
                                                                  PMLR.
Athey, S. and Wager, S. Estimating treatment effects
  with causal forests: An application. arXiv preprint           Glymour, C., Zhang, K., and Spirtes, P. Review of causal
  arXiv:1902.07409, 2019.                                         discovery methods based on graphical models. Frontiers
                                                                  in genetics, 10:524, 2019.
Athey, S., Tibshirani, J., and Wager, S. Generalized random
  forests. The Annals of Statistics, 47(2):1148 – 1178, 2019.   Greenland, S. Quantifying biases in causal models: classical
  doi: 10.1214/18-AOS1709.                                        confounding vs collider-stratification bias. Epidemiology,
Battocchi, K., Dillon, E., Hei, M., Lewis, G., Oka, P.,           pp. 300–306, 2003.
  Oprescu, M., and Syrgkanis, V. EconML: A Python
                                                                Hartford, J., Lewis, G., Leyton-Brown, K., and Taddy, M.
  Package for ML-Based Heterogeneous Treatment Effects
                                                                  Deep IV: A flexible approach for counterfactual predic-
  Estimation. https://github.com/microsoft/EconML, 2019.
                                                                  tion. In ICML, volume 70 of PMLR, pp. 1414–1423.
  Version 0.x.
                                                                  PMLR, 06–11 Aug 2017.
Bennett, A., Kallus, N., and Schnabel, T. Deep generalized
  method of moments for instrumental variable analysis. In      Hyttinen, A., Eberhardt, F., and Hoyer, P. O. Experiment se-
  NeurIPS, volume 32. Curran Associates, Inc., 2019.              lection for causal discovery. Journal of Machine Learning
                                                                  Research, 14:3041–3071, 2013.
Bhattacharya,     R.,    Lee,    J.,    and Nabi, R.
  Ananke:        A module for causal inference.                 Jacob, D. Cate meets ml-the conditional average treat-
  https://ananke.readthedocs.io/en/latest/, 2020.                 ment effect and machine learning. arXiv preprint
                                                                  arXiv:2104.09935, 2021.
Bhattacharya, R., Nagarajan, T., Malinsky, D., and Shpitser,
  I. Differentiable causal discovery under unmeasured con-      Jesson, A., Mindermann, S., Gal, Y., and Shalit, U. Quan-
  founding. In International Conference on Artificial Intel-      tifying ignorance in individual-level causal-effect es-
  ligence and Statistics, pp. 2314–2322. PMLR, 2021.              timates under hidden confounding. arXiv preprint
                                                                  arXiv:2103.04850, 2021.
Chen, H., Harinen, T., Lee, J.-Y., Yung, M., and Zhao, Z.
  Causalml: Python package for causal machine learning,         Kalisch, M., Mächler, M., Colombo, D., Maathuis, M. H.,
  2020.                                                           and Bühlmann, P. Causal inference using graphical mod-
Chernozhukov, V., Chetverikov, D., 19 Demirer, M., Duflo,         els with the r package pcalg. Journal of statistical soft-
  E., Hansen, C., and Newey, W. Double/debiased/neyman            ware, 47(11):1–26, 2012.
  machine learning of treatment effects. American Eco-
  nomic Review, 107(5):261–65, 2017.                            Kennedy, E. H. Optimal doubly robust estimation of hetero-
                                                                  geneous causal effects. arXiv preprint arXiv:2004.14497,
Cinelli, C. and Hazlett, C. Making sense of sensitivity:          2020.
  extending omitted variable bias. Journal of the Royal
  Statistical Society: Series B (Statistical Methodology), 82   Lewis, G. and Syrgkanis, V. Adversarial generalized method
  (1):39–67, 2020. doi: https://doi.org/10.1111/rssb.12348.       of moments. arXiv preprint arXiv:1803.07164, 2018.

Dash, S., Balasubramanian, V., and Sharma, A. Counterfac-       Neal, B., Huang, C.-W., and Raghupathi, S. Realcause:
  tual generation and fairness evaluation using adversarially     Realistic causal inference benchmarking. arXiv preprint
  learned inference. arXiv e-prints, pp. arXiv–2009, 2020.        arXiv:2011.15007, 2020.
                      DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

Nie, X. and Wager, S. Quasi-oracle estimation of hetero-         Syrgkanis, V., Lei, V., Oprescu, M., Hei, M., Battocchi, K.,
  geneous treatment effects. Biometrika, 108(2):299–319,           and Lewis, G. Machine learning estimation of heteroge-
  2021.                                                            neous treatment effects with instruments. NeurIPS, 32:
                                                                   15193–15202, 2019.
Pearl, J. Causality. Cambridge university press, 2009.
                                                                 Textor, J., van der Zander, B., Gilthorpe, M. S., Liśkiewicz,
Pearl, J. The do-calculus revisited.         arXiv preprint        M., and Ellison, G. T. Robust causal inference using
  arXiv:1210.4852, 2012.                                           directed acyclic graphs: the r package ‘dagitty’. Interna-
                                                                   tional journal of epidemiology, 45(6):1887–1894, 2016.
Peters, J., Janzing, D., and Schölkopf, B. Elements of causal
  inference: foundations and learning algorithms. The MIT        Tikka, S. and Karvanen, J. Identifying causal effects with
  Press, 2017.                                                     the r package causaleffect. Journal of Statistical Software,
                                                                   76(i12), 2017.
Powers, S., Qian, J., Jung, K., Schuler, A., Shah, N. H.,
  Hastie, T., and Tibshirani, R. Some methods for hetero-        Veitch, V. and Zaveri, A. Sense and sensitivity analysis:
  geneous treatment effect estimation in high dimensions.          Simple post-hoc analysis of bias due to unobserved con-
  Statistics in Medicine, 37(11):1767–1787, 2018. doi:             founding. arXiv preprint arXiv:2003.01747, 2020.
  https://doi.org/10.1002/sim.7623.
                                                                 Wager, S. and Athey, S. Estimation and inference of hetero-
Ribeiro, M. T., Wu, T., Guestrin, C., and Singh, S. Beyond        geneous treatment effects using random forests. Journal
  accuracy: Behavioral testing of nlp models with checklist.      of the American Statistical Association, 113(523):1228–
  In ACL, pp. 4902–4912, 2020.                                    1242, 2018.
Robins, J. M., Rotnitzky, A., and Scharfstein, D. O. Sen-        Zhang, K. and Hyvärinen, A. On the identifiability of the
  sitivity analysis for selection bias and unmeasured con-         post-nonlinear causal model. In UAI, pp. 647–655. AUAI
  founding in missing data and causal inference models. In         Press, 2009.
  Statistical models in epidemiology, the environment, and
  clinical trials, pp. 1–94. Springer, 2000.                     Zhang, K. and Hyvärinen, A. Distinguishing causes from ef-
                                                                   fects using nonlinear acyclic causal models. In Causality:
Rosenbaum, P. R. Sensitivity analysis in observational stud-       Objectives and Assessment, pp. 157–164. PMLR, 2010.
  ies. Wiley StatsRef: Statistics Reference Online, 2014.

Schuler, A., Baiocchi, M., Tibshirani, R., and Shah, N.          A. DGP for the Motivating Examples
  A comparison of methods for model selection when es-
  timating individual treatment effects. arXiv preprint          A.1. Example 1
  arXiv:1804.05146, 2018.

Shalit, U., Johansson, F. D., and Sontag, D. Estimating
  individual treatment effect: generalization bounds and                 y ← 10t + 10w +                                  (1)
  algorithms. In ICML, pp. 3076–3085. PMLR, 2017.                         t ← (sigmoid(2z − 1 + w) >= 0.5, 1, 0)           (2)
                                                                         z ∼ Bernoulli(0.5)                                (3)
Shimizu, S., Hoyer, P. O., Hyvärinen, A., Kerminen, A.,
  and Jordan, M. A linear non-gaussian acyclic model for                 w ∼ N ormal(0, 0.4)                               (4)
  causal discovery. Journal of Machine Learning Research,                  ∼ N ormal(0, 100)                              (5)
  7(10), 2006.
                                                                 A.2. Example 2
Shpitser, I. and Pearl, J. Complete identification methods
  for the causal hierarchy. Journal of Machine Learning
  Research, 9:1941–1979, 2008.
                                                                            y ← 10m +                                     (6)
Simard, P. Y., Amershi, S., Chickering, D. M., Pelton, A. E.,
                                                                             t ∼ Bernoulli(0.5)                            (7)
  Ghorashi, S., Meek, C., Ramos, G., Suh, J., Verwey, J.,
  Wang, M., et al. Machine teaching: A new paradigm                        m ∼ Bernoulli(0.95t + 0.05(1 − t))              (8)
  for building machine learning systems. arXiv preprint                      ∼ N ormal(0, 1)                              (9)
  arXiv:1707.06742, 2017.

Spirtes, P., Glymour, C. N., Scheines, R., and Heckerman,
  D. Causation, prediction, and search. MIT press, 2000.
```
