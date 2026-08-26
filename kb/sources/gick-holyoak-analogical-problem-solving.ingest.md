---
description: "Five human experiments separate retaining a remote analogy from noticing its relevance and using it to change problem-solving behavior."
source: "https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FNK23omDLKU.pdf?alt=media&token=9cf50971-e354-4d03-b89a-3bf7e96862e7"
captured: "2026-08-26"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: c7495e59ca5cfd477aefaf78e3661cc0133cd194152a9dd8324196337171dca7
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, learning-theory, evaluation]
---

# Ingest: Analogical Problem Solving

## Classification

This is an empirical cognitive-psychology paper reporting five experiments that vary supplied analogies, structural correspondence, memory context, and relevance hints before scoring proposed solutions to Duncker's radiation problem. Author: Mary L. Gick and Keith J. Holyoak, University of Michigan researchers publishing in *Cognitive Psychology*; the paper reports condition procedures, participant counts, inferential tests, and protocol excerpts.

## Summary

Gick and Holyoak ask when a solution from a semantically distant story changes performance on a target problem. Across five experiments, participants often generated analogous solutions when explicitly told that a prior story might help, while transfer weakened when relational correspondence was poorer or the source solution was self-generated. Most important for KB design, participants who had memorized and could recall a relevant story used it far less often without a relevance cue; cueing restored task use. The paper is worth reading for its experimental separations among encoding, access and noticing, mapping, and solution generation, not as direct evidence about LLM agents.

## Quotes

- **Source extract (verbatim):** 11 out of 12 subjects (92%)
  - **Source location:** Experiment IV, Results and Discussion, page 342; Hint-condition subjects producing the complete dispersion solution.
- **Source extract (verbatim):** only 20% (3 out of 15)
  - **Source location:** Experiment IV, Results and Discussion, page 342; No Hint-condition subjects producing the dispersion solution.
- **Source extract (verbatim):** did not differ significantly between the Hint and No Hint groups
  - **Source location:** Experiment IV, gist-recall check, page 343; comparison of mean propositions recalled from the critical story.
- **Source extract (verbatim):** For subjects in the “Hint” condition, the instructions on solving the radiation problem included the following sentence: “In solving this problem you may find that one of the stories you read before will give you a hint for a solution of this problem.” For subjects in the “No Hint” condition, this sentence was deleted from the instructions.
  - **Source location:** Experiment IV, Method, pages 341–342; the varied relevance-cue instruction.
- **Source extract (verbatim):** For the Hint condition, 11 out of 12 subjects (92%) produced the complete dispersion solution.
  - **Source location:** Experiment IV, Results and Discussion, page 342; hinted participants producing the target solution.
- **Source extract (verbatim):** Whereas 92% of the subjects in the Hint condition produced the dispersion solution, only 20% (3 out of 15) of those in the No Hint condition did so,
  - **Source location:** Experiment IV, Results and Discussion, page 342; direct condition comparison.
- **Source extract (verbatim):** Since subjects were randomly assigned to the two conditions, degree of memory for the critical story should have been equalized across the two conditions. To confirm this, the protocols for the Attack-Dispersion story were scored for gist recall. For this purpose the story was divided into 43 propositions (see Appendix III). This propositional division was made using the procedure outlined by Thorndyke (1977), with the addition that adjectives and prepositional phrases that seemed intuitively important to the story were counted as separate propositions. As anticipated, the mean number of propositions recalled did not differ significantly between the Hint and No Hint groups (32.08 versus 33.53), f < 1.
  - **Source location:** Experiment IV, recall check, page 343; scoring method and null group difference.

## Connections Found

This paper is a bounded human evidence anchor for [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md): Experiment IV pairs comparable story recall with a large hint/no-hint difference in analogous solutions, reaching task use more directly than a recall-only result. It also supplies a concrete recognition bottleneck for [Recognition, not linking, is the hard problem in knowledge systems](../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md). Its role in agent methodology remains a limitation as well as evidence: [Psychology-to-agent transfer needs per-principle failure-mode testing](../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) requires an agent-side test before the human cueing result can support an LLM mechanism claim.

## Extractable Value

1. **Recallable knowledge can remain behaviorally inert.** In Experiment IV, 92% of the hinted group produced the dispersion solution, versus 20% of the unhinted group, despite similar recall of the critical story. This is unusually direct human evidence for separating storage and later usability from spontaneous activation. [quick-win]
2. **The strongest intervention is narrowly identifiable.** Experiment IV varies whether the problem-solving instructions say that one of the memorized stories may provide a hint. It therefore supports the effect of that relevance cue in the tested task, not a general claim that any retrieval or reflection prompt closes an activation gap. [quick-win]
3. **Cueing a useful analogy may narrow search as well as improve the target response.** In Experiments I and II, conditions that more effectively prompted the analogous solution also tended to yield fewer disanalogous alternatives; the Experiment II differences were statistically reliable. Agent-side activation interventions should therefore measure lost alternatives as well as intended uptake. [experiment]
4. **Relational correspondence matters beyond copying a solution outline.** In Experiment II, the more structurally corresponding Attack story produced dispersion solutions more often than the Parade story, even though their solution descriptions were closely matched; both exceeded the no-story control. This supports treating analogy as relational mapping while leaving the causal contribution of any one correspondence unresolved. [deep-dive]
5. **The fixed decomposition bounds what the experiments establish.** Available signals and histories included the radiation problem, prior story encoding and recall, distractor load, and the presence or absence of a hint; participants could retrieve a story, map relations at varying levels of detail, and compose written solution proposals. Story selection and wording, the target problem, cue format, participant population, and scoring criteria remained outside the varied space. Improved solution generation inside that setup does not show that those fixed representations or partitions are optimal. [just-a-reference]
6. **The human result defines an agent experiment rather than an agent conclusion.** A matched agent evaluation could hold stored knowledge and task capability constant, vary whether relevance is cued, and separately score exposure, uptake, alternative-search breadth, and task outcome. Until then, the paper supplies a human failure mode and intervention only. [experiment]

## Limitations (our opinion)

The cleanest causal result is the hint/no-hint contrast in one undergraduate analogical task. It does not distinguish a cue that retrieves the stored story from one that makes already retrieved content salient, and it cannot establish the same mechanism in LLM agents. All five experiments use one target problem and a narrow family of source stories; several conditions are small, solutions are manually coded, and some process claims rely on think-aloud protocols or post-hoc helpfulness reports. Experiment III's self-generated-solution comparison is correlational. Experiment II varies a bundle of story-problem relations, so its ablation bears on that bundled correspondence rather than any single mapping feature. The proposed multilevel representation and solution-focusing strategy are interpretations consistent with the results, not directly measured mechanisms. As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) warns, success within the paper's fixed stories, response format, scoring rules, and participant population does not validate those choices as a general decomposition of analogical transfer.

## Recommended Next Action

Update [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) with one bounded human-evidence paragraph on Experiment IV's recall-matched hint/no-hint contrast, citing this ingest as `(snapshot required)` and stating that agent-system application remains a transfer hypothesis.
