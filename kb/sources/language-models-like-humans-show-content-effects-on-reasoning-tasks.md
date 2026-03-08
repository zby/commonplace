---
source: https://academic.oup.com/pnasnexus/article/3/7/pgae233/7712372
captured: 2026-03-08
capture: web-fetch
type: academic-paper
---

# Language Models, Like Humans, Show Content Effects on Reasoning Tasks

Author: Andrew K Lampinen, Ishita Dasgupta, Stephanie C Y Chan, Hannah R Sheahan, Antonia Creswell, Dharshan Kumaran, James L McClelland, Felix Hill
Source: https://academic.oup.com/pnasnexus/article/3/7/pgae233/7712372
Date: 2024-07-16
DOI: 10.1093/pnasnexus/pgae233
PMC: PMC11250216

Language models and humans both mix semantic content into their performance on logical reasoning problems, which generally results in greater success in familiar situations, but more errors in unusual ones. These results may inform the search for the origins of these human behaviors and may help improve applications of language models.

## Abstract

Abstract reasoning is a key ability for an intelligent system. Large language models (LMs) achieve above-chance performance on abstract reasoning tasks but exhibit many imperfections. However, human abstract reasoning is also imperfect. Human reasoning is affected by our real-world knowledge and beliefs, and shows notable "content effects"; humans reason more reliably when the semantic content of a problem supports the correct logical inferences. These content-entangled reasoning patterns are central to debates about the fundamental nature of human intelligence. Here, we investigate whether language models—whose prior expectations capture some aspects of human knowledge—similarly mix content into their answers to logic problems. We explored this question across three logical reasoning tasks: natural language inference, judging the logical validity of syllogisms, and the Wason selection task. We evaluate state of the art LMs, as well as humans, and find that the LMs reflect many of the same qualitative human patterns on these tasks—like humans, models answer more accurately when the semantic content of a task supports the logical inferences. These parallels are reflected in accuracy patterns, and in some lower-level features like the relationship between LM confidence over possible answers and human response times. However, in some cases the humans and models behave differently—particularly on the Wason task, where humans perform much worse than large models, and exhibit a distinct error pattern. Our findings have implications for understanding possible contributors to these human cognitive effects, as well as the factors that influence language model performance.

## Introduction

A hallmark of abstract reasoning is the ability to perform systematic operations over variables that can be bound to any entity: the statement "X is bigger than Y" logically implies that "Y is smaller than X", no matter the values of X and Y. That is, abstract reasoning is ideally content-independent. The capacity for reliable and consistent abstract reasoning is frequently highlighted as a crucial missing component of current AI. For example, while large language models (LMs) exhibit some impressive *emergent* behaviors, including some performance on abstract reasoning tasks, they have been criticized for failing to achieve systematic consistency in their abstract reasoning.

However, humans—arguably the best known instances of general intelligence—are far from perfectly rational abstract reasoners. Patterns of biases in human reasoning have been studied across a wide range of tasks and domains. Here, we focus on "content effects"—the finding that humans are affected by the semantic content of a logical reasoning problem. In particular, humans reason more readily and more accurately about familiar, believable, or grounded situations, compared to unfamiliar, unbelievable, or abstract ones. For example, when presented with a syllogism like the following:

> All students read.
> Some people who read also write essays.
> Therefore some students write essays.

humans will often classify it as a valid argument. However,

> All students read.
> Some people who read are professors.
> Therefore some students are professors.

is much less likely to be considered valid—despite the fact that the arguments above are logically equivalent (both are invalid). Similarly, humans struggle to reason about how to falsify conditional rules involving abstract attributes, but reason more readily about logically equivalent rules grounded in realistic situations. This human tendency also extends to other forms of reasoning e.g. probabilistic reasoning, where humans are notably worse when problems do not reflect intuitive expectations.

The content effects on which we focus are a notably consistent finding that has been documented in humans across many reasoning tasks and domains: deductive, inductive, logical, or probabilistic. This consistent content sensitivity contradicts the definition of abstract reasoning—that it is independent of content. This tension speaks to longstanding debates over the fundamental nature of human intelligence: are we best described as algebraic symbol-processing systems, or emergent connectionist ones whose inferences are grounded in learned semantics?

In this work, we examine whether LMs also blend semantic content with logic. LMs possess prior knowledge that is shaped by their training. Indeed, the goal of the "pretrain and adapt" or "foundation models" paradigm is to endow a model with broad prior knowledge for later tasks. Thus, LM representations often *reflect* human semantic cognition; e.g. language models reproduce patterns like association and typicality effects, and LM predictions can reproduce human knowledge and beliefs. Here, we explore whether this prior knowledge impacts LM performance in logical reasoning tasks.

We hypothesize that while LMs and humans will not always show identical answer patterns, LMs will show directionally similar effects to those observed in humans. In particular, we test whether LMs show facilitation when semantic content supports the logical answer, and interference when it does not.

### Evaluating content effects on logical tasks

We evaluate content effects on three logical reasoning tasks. These three tasks involve different types of logical inferences, and different kinds of semantic content. However, these distinct tasks admit a consistent definition of content effects: the extent to which reasoning is facilitated when the semantic content supports the correct logical inference, and correspondingly the extent to which reasoning is harmed when semantic content conflicts with the correct logical inference.

We also evaluate versions of each task where the semantic content is replaced with nonsense nonwords, which lack semantic content and thus should neither support nor conflict with reasoning performance.

**Natural language inference**

The first task we consider has been studied extensively in the natural language processing literature. In the classic NLI problem, a model receives two sentences, a "premise" and a "hypothesis", and has to classify them based on whether the hypothesis "entails", "contradicts", or "is neutral to" the premise. To make this task more strictly logical, we generate comparisons (e.g. X is smaller than Y). We then give participants an incomplete inference and ask them to choose between two possible hypotheses to complete it. One completion is consistent with real-world semantic beliefs (believable) but logically inconsistent with the premise, while the other is logically consistent with the premise but contradicts real world beliefs—thus, logical consistency and believability can be manipulated independently.

**Syllogisms**

Syllogisms are a simple argument form in which two true statements necessarily imply a third. For example, the statements "All humans are mortal" and "Socrates is a human" together imply that "Socrates is mortal." But human syllogistic reasoning is not purely abstract and logical; instead it is affected by our prior beliefs about the contents of the argument. Evans et al. showed that if participants were asked to judge whether a syllogism was logically valid or invalid, they were biased by whether the conclusion was consistent with their beliefs. Participants were very likely (90% of the time) to mistakenly say an invalid syllogism was valid if the conclusion was believable.

We therefore hypothesized that language models would likewise be more likely to endorse an argument as valid if its conclusion is believable, or to dismiss it as invalid if its conclusion is unbelievable.

**The Wason selection task**

The Wason selection task is a logic problem that can be challenging even for humans with substantial education in logic. Participants are shown four cards with a letter on one side and a number on the other. The participants are then told a rule such as: "if a card has a 'D' on one side, then it has a '3' on the other side." The participants are asked which cards they need to flip over to check if the rule is true or false. The correct answer is to flip over the cards showing "D" and "7". However, Wason showed that while most participants correctly chose "D", they were much more likely to choose "3" than "7"—confusing the contrapositive with the converse.

The difficulty of the Wason task depends upon the content of the problem. Past work has found that if an identical logical problem is instantiated in a common situation (particularly a social rule), participants are much more accurate. For example, with a rule like "if they are drinking alcohol, then they must be 21 or older," many more participants correctly choose to check the cards showing "beer" and "16."

## Results

We summarize our primary results across the three tasks. In each task, humans and models show similar levels of accuracy across conditions. In keeping with our hypothesis, humans and models show similar content effects on each task, which we measure as the advantage when reasoning about logical situations that are consistent with real-world relationships or rules.

- In the simplest NLI task, humans and all models show high accuracy and relatively minor effects of content.
- When judging the validity of syllogisms, both humans and models show more moderate accuracy, and significant advantages when content supports the logical inference.
- On the Wason selection task, humans and models show even lower accuracy, and again substantial content effects.

**Natural language inference**

The relatively simple logical reasoning involved in this task means that both humans and LMs exhibit high performance, and correspondingly show relatively little effect of content. We do not detect a statistically significant effect of content on accuracy in humans or any of the LMs. However, we do find a statistically significant relationship between human and model accuracy at the item level, even when controlling for condition.

**Syllogisms**

Syllogism validity judgements are significantly more challenging; correspondingly, both humans and LMs exhibit lower accuracy. Nevertheless, humans and most LMs are sensitive to the logical structure of the task. However, both humans and LMs are strongly affected by the syllogism content. If the semantic content supports the logical inference—that is, if the conclusion is believable and the argument is valid, or if the conclusion is unbelievable and the argument is invalid—humans and all LMs tend to answer more accurately.

Two simple effects contribute to this overall content effect: belief-consistent conclusions are judged as logically valid and belief-inconsistent conclusions are judged as logically invalid. The dominant effect is that humans and models tend to say an argument is valid if the conclusion is belief-consistent, regardless of the actual logical validity.

**The Wason selection task**

As in the prior human literature, we found that the Wason task was relatively challenging for humans, as well as for language models. Nevertheless, we observed significant content advantages for the Realistic tasks in humans, and in Chinchilla, PaLM 2-L, and GPT-3.5.

Our human participants struggled with this task, as in prior research, and did not achieve significantly above-chance performance overall. However, human accuracy was positively and significantly associated with response time—humans spending longer showed better accuracy on realistic conditions. We also find that chain-of-thought techniques (loosely giving the models time to "think") can improve the performance of strong models on the Arbitrary and Nonsense conditions of the Wason task.

**Robustness of results**

LM behavior is frequently sensitive to evaluation details. We performed several experiments to confirm robustness: removing prequestion instructions does not substantially alter results; the DC-PMI scoring correction is not the primary driver of content effects; few-shot evaluation yields mild improvements in accuracy but does not eliminate content effects.

**Chain-of-thought can sometimes push large models to rely more on logic**

Chain-of-thought prompting can, in some cases, push large models to rely more on logical strategies, thereby reducing content effects through improving performance on less familiar or conflicting situations—particularly if those examples demonstrate precisely the type of reasoning that's required.

**Variability across different language models**

We generally find similar content effects across the various models we evaluate. Larger models tend to be more accurate overall. Instruction-tuned models (Flan-PaLM 2 and GPT-3.5) do not show consistent differences in overall accuracy or content effects compared to base language models. We also tested several newer Gemini models and observed similar effects, showing that these phenomena still hold with more recent models.

### Model confidence relates to human response times

LMs produce a probability distribution over possible answers. We measure model confidence as the difference in prior-corrected log-probability between the top answer and the second highest. In mixed-effects regressions predicting model confidence from task variables and average human RTs on the same problem:

- LMs tend to be more confident on correct answers (i.e. they are somewhat calibrated).
- Models are generally less confident when the conclusion violates beliefs, and more confident for realistic rules on the Wason task.
- Even when controlling for task variables and accuracy, there is a statistically significant negative association with human response times on the NLI and syllogisms tasks—that is, models tend to show more confidence on problems where humans likewise respond more rapidly.

### Analyzing components of the Wason responses

As in prior work, humans do not consistently choose the correct answer (AT=Antecedent True, CF=Consequent False). Instead, humans tend to exhibit a matching bias; that is, they tend to choose the two cards that match each component of the rule (AT, CT). However, in the Realistic condition, slow humans answer correctly somewhat more often.

LMs tend to give more correct responses than humans, and to show facilitation in the realistic rules compared to arbitrary ones. Relative to humans, LMs show fewer matching errors and fewer errors of choosing two cards from the same rule component, but more errors of choosing the antecedent false options. These differences in error patterns may indicate differences between the response processes engaged by the models and humans.

## Discussion

Humans are imperfect reasoners. We reason most effectively about situations that are consistent with our understanding of the world and often struggle to reason in situations that either violate this understanding or are abstract and disconnected from the real world. Our experiments show that language models mirror these patterns of behavior. Language models also perform imperfectly on logical reasoning tasks and more often fail in situations where humans fail—when stimuli become too abstract or conflict with prior expectations.

Beyond simple parallels in accuracy across conditions, LM confidence tends to be higher for correct answers, and for cases where prior expectations about the content are consistent with the logical structure. Even when controlling for these effects, language model confidence is related to human response times. These core results are generally robust across different language models with different training and tuning paradigms, suggesting that they are a fairly general phenomenon of predictive models that learn from human-generated text.

**Prior research on language model reasoning**

Since Brown et al. showed that large language models could perform moderately well on some reasoning tasks, there has been a growing interest in language model reasoning. Some researchers have questioned whether these language model abilities qualify as "reasoning." The fact that language models sometimes rely on "simple heuristics," or reason more accurately about frequently occurring numbers, have been cited to "raise questions on the extent to which these models are *actually reasoning*." The implicit assumption in these critiques is that reasoning should be a purely algebraic, syntactic computation over symbols.

In this work, we emphasize how *both* humans and language models rely on content when answering reasoning problems—using simple heuristics in some contexts, and answering more accurately about frequently occurring situations. Thus, abstract reasoning may be a graded, content-sensitive capacity in both humans and models.

**Dual systems?**

The idea that humans possess dual reasoning systems—an implicit, intuitive "system 1," and a distinct explicit reasoning "system 2"—was motivated in large part by belief bias and Wason task effects. Many works claim that current ML behaves like system 1, and that we need to augment this with a classically symbolic process to get system 2 behaviour.

Our results show that a single system—a large transformer language model—can mirror this dual behavior in humans, demonstrating both biased and consistent reasoning without an explicit secondary symbolic "system 2." In direct analogy to "fast" vs. "slow" responses in humans, we compare model behavior on the complex Wason task with and without a chain-of-thought prompt, and find that the chain-of-thought prompt can move a strong model from strong content-biases to achieving fairly high accuracy across Arbitrary and Nonsense conditions.

These results show that dual-system-like behaviors need not rely on an explicitly symbolic and separate system 2—they can instead arise from implicit systems that use context to arbitrate between conflicting responses.

**Towards a normative account of content effects?**

Various accounts of human cognitive biases frame them as "normative" by some objective. Our results show that these effects can emerge from simply training a large LM to imitate sufficiently large quantities of language produced by human culture, without explicitly incorporating any human-specific internal mechanisms.

This observation suggests two potential origins for these content effects:

1. Content effects could be directly imitated from the humans that generated the LM training data. Under this hypothesis, poor logical inferences about nonsense or belief-violating premises come from *copying* the incorrect inference patterns humans use.
2. Like humans, an LM's experience reflects real-world semantics, and thus LMs and humans both converge on these content biases that reflect this semantic content for task-oriented reasons—because it helps to draw more accurate inferences in the situations more frequently encountered (which are mostly familiar and believable).

**Why might model response patterns differ from human ones?**

The LM response patterns do not perfectly match all aspects of the human data. For example, on the Wason task large models generally outperform the humans, and the error patterns are somewhat different. Various factors could contribute to differences:

- It is difficult to perfectly align human and model evaluation procedures.
- LMs do not directly experience the situations to which language refers; grounded experience presumably underpins some human beliefs and reasoning.
- Language models experience language passively, while humans experience language as an active, conventional system for social communication.

**How can we achieve more abstract, context-independent reasoning?**

One method to reduce content dependency is through prompting, which can help in some cases. However, achieving fully consistent reasoning across all tasks would likely require altering model training. For humans, formal education is associated with an improved ability to reason logically and consistently. Recent results suggest targeted training may be a promising direction: pretraining on synthetic logical reasoning tasks can improve model performance; models can be prompted or learn to verify, correct, or debias their own outputs; and language model reasoning can be bootstrapped through iterated fine-tuning on successful instances.

**Limitations**

- Only a handful of tasks were considered; it would be useful to characterize human and LM content effects across a broader range of tasks.
- Human participants exhibited relatively low performance on the Wason task; individual differences associated with depth of mathematical education were not examined.
- Language models are trained on much greater quantities of language data than any human, making it hard to draw strong conclusions about whether these effects would emerge at a more human-like data scale.
- The experiments do not ascertain precisely which aspects of the large language model training datasets contribute to content effects in reasoning.

## Materials and Methods

**Creating datasets**

To avoid dataset contamination (stimuli from prior cognitive science studies may be present in LM training data), we generate new datasets by following the design approaches used in prior work. For each task, we generate multiple versions of the task stimuli with fixed logical structure but varying entities:

- *Consistent*: propositions consistent with human beliefs and knowledge
- *Violate*: beliefs violated by inverting the consistent statements
- *Nonsense*: tasks about nonsense pseudowords (e.g. "kleegs are smaller than feps")

For the Wason tasks:
- *Realistic*: rules involving plausible relationships
- *Arbitrary*: arbitrary rules
- *Nonsense*: rules relating nonsense words

Dataset sizes: NLI (78 questions per condition), syllogisms (48 questions per Consistent/Violate condition), Wason (72 questions per Realistic/Arbitrary condition).

**Models & evaluation**

Models evaluated:
- Chinchilla (70B parameters, causal language modeling)
- PaLM 2-M and PaLM 2-L (mixture of language modeling and infilling objectives)
- Flan-PaLM 2 (instruction-tuned version of PaLM 2-L)
- GPT-3.5-turbo-instruct

For each task, the model is presented with brief instructions approximating the human instructions, then the question ending with "Answer:", and model scoring uses the DC-PMI correction (change in likelihood of each answer relative to a baseline context) to reduce sensitivity to answer phrasing.

**Human experiments**

All human experimental procedures were approved by the DeepMind independent ethical review committee. Experiments were conducted in 2023 using an online crowd-sourcing platform with UK participants who spoke English as a first language and had over a 95% approval rate. Pay was £2.50 for the task (exceeding £15/h rate). Participants were presented with one question from each of the three tasks, in randomized order with randomized conditions.

Total participants: 625 in the initial dataset, plus 360 additional participants for a replication with a £0.50 performance bonus on the Wason task.

**Statistical analyses**

Main analyses use mixed-effects logistic regressions with task condition variables as predictors, controlling for random effects of items and, where applicable, models.
