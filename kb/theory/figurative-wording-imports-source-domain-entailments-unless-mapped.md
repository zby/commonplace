---
type: types/note.md
description: "Why a figure's implied relations need target-side justification, when conventional or explanatory figures avoid ambiguity, and what remains untested for LLM readers."
traits: [title-as-claim, has-external-sources]
tags: [prose-readability, document-system]
brief: figurative-wording-imports-source-domain-entailments-unless-mapped.brief.md
---

# Figurative wording can suggest relations that the target claim does not justify

A figure of speech offers relations from one domain as a way to understand another. Those relations can suggest more than the intended claim. Calling a parameter “a dial worth turning,” for example, suggests continuous manual control even if the author means only that the parameter should be varied. The reader must distinguish the intended correspondence from the image's other implications. If the text leaves that distinction unresolved, an implication of the image can be mistaken for a property of the target.

This is a proposed explanation of an interpretive risk, not a claim that every reader accepts every implication. Two costs matter: uncertainty about which relation the author intends, and an inference that the target facts do not justify. Neither cost is equivalent to extra reading time or worse recall.

The justification problem is the sentence-scale instance of [a borrowed pattern transferring only as far as source and target share a mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md). A comparison does not itself establish that the target has the causal relations of the source. A stated mapping makes the proposed correspondence inspectable; it still needs justification. Where shared mechanism cannot be established, target-side evidence is needed before the comparison can justify a conclusion.

## When a figure contributes more than it costs

A conventional and precise figure need not require a fresh analogy. If the intended reader already shares its settled sense, that sense can identify the intended relation without reconstructing the image. The exception depends on familiarity and precision, not merely on frequent use.

An explanatory figure does different work: it supplies relational structure that the explanation actually uses. Stating which parts correspond, why the correspondence holds and where it ends gives the reader something to evaluate. This can clarify a mechanism rather than add an image to an otherwise complete claim. A mapping is not a guarantee of truth or of how a reader will interpret the passage.

These are design reasons for keeping useful figures, not measured advantages in the studies below. Literal wording can instead state the intended relation directly. It may take more words than the figure. Word count alone cannot decide between an explicit relation and a shorter expression whose implications remain ambiguous.

The same justification problem occurs at several scales in Commonplace's prose checks. Mannered prose can introduce an unused implication in a sentence. Source residue can leave a general claim dependent on narrower source-domain framing. Unbridged cross-domain evidence can treat a source result as warrant for a target claim without establishing the connection. At method scale, borrowed patterns face the same demand for justified transfer. This connects the checks where a comparison carries an unsupported implication; it does not make every instance of source residue a metaphor or establish one cognitive process behind all three gates.

## Human framing evidence is mixed

In [Thibodeau and Boroditsky (2011)](../sources/metaphors-we-think-with.ingest.md), participants read crime reports about a fictional city. Experiment 1 elicited more enforcement suggestions with crime-as-beast framing than with crime-as-virus framing: 74% versus 56%. Only 3% named the metaphor as the report's most influential feature, and removing them did not change the result. This mismatch supports influence not reflected in that attribution question; it does not prove that participants never noticed the wording. The comparison was between two figures, not a demonstration that literal prose produced better decisions. The study also had limits: disconnected lexical primes did not change policy suggestions, and moving the metaphor to the report's end produced no detected effect on information gathering.

[Steen, Reijnierse and Burgers (2014)](../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) found no framing effect on reasoning across four experiments, including one with over 1,000 participants. Their designs added a non-metaphorical control, versions without supporting metaphors and, in the first two experiments, pre-exposure measures of political preference. Supporting metaphors affected memory in two experiments, but those memory effects did not affect policy preference. Remembering a frame and reasoning differently are distinct outcomes.

The positive and null findings leave the conditions of influence unresolved. The later designs do not prove that the earlier result was a confound. These studies motivate concern about figurative framing while limiting any claim that it automatically determines inference.

## LLM transfer is a conjecture with a test

The cited studies supply no LLM evidence. For specified models and KB tasks, two separate predictions are worth testing: an unmapped figure produces more unsupported source-domain implications than a literal statement of the same intended claim; adding a bounded mapping reduces those implications.

A discriminating test would compare literal, unmapped and explicitly mapped passages with the same target facts and intended conclusion. Multiple figures and tasks, including familiar conventional figures, would keep the result from depending on one image. Position and surrounding information would be controlled, with a length/detail control where mapping adds text. The unsupported implications and comparison criterion would be specified before testing. Inference or application outputs would be scored separately for those implications and task success, blind to condition where possible, with model versions, prompts, sampling settings and independent trials reported.

A reproducible excess in the unmapped condition would support the first prediction in that setting; a reduction with mapping would support the second. Either could fail independently. Null or reversed contrasts would challenge the predictions within the tested range, not establish universal immunity. Output differences alone would not establish a human-like internal process.

## Scope

The empirical cases concern human reasoning about crime policy, not KB reading. They are origins and limits of this proposal, not tests of its general explanation. The proposed interpretive burden of identifying a correspondence still needs a human KB-reading test that distinguishes comprehension and effort from policy preference. No prevalence claim follows for figurative wording in general, and neither literal wording nor explicit mapping is an unconditional remedy.
