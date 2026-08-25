---
description: "A controlled test found fine-grained stance drift despite explicit detection and refusal; exclusion guarantees non-exposure, while instruction-level mitigation remains an empirical question"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [llm-reliability, context-engineering]
---

# Context contamination operates below an agent's compliance reasoning

Stance-bearing content can shape an agent's writing even when the agent notices it, identifies it as out of contract, and refuses to reproduce it. This note uses **below compliance reasoning** operationally, not architecturally: the influence persists despite the agent's expressed reasoning about what it should comply with.

In the controlled test reported here, explicit detection and refusal did not guarantee neutral output. The practical consequence is a distinction between guarantees: **excluding a contaminant prevents exposure, while instructing an agent to ignore content already in context does not enforce isolation**. Stronger instructions may mitigate or even eliminate measured drift under some conditions; whether they do is an empirical question.

## What the contamination actually looks like

The intuitive model of contamination is coarse: the agent copies forbidden content or omits what the contaminant argues against. That model misses the form of contamination observed here, which is precisely why the failure is hard to gate on.

The controlled test compared four same-model writer agents drafting the same stance-neutral note from identical inputs. Two received a context file containing an implanted own-voice verdict; two did not. A blind judge then audited all four notes against the contract without knowing that the conditions differed.

The contaminated writers copied nothing. No treatment note reproduced the verdict, dropped an objection, or asserted a position in its title. Every gross-grained check passed. The leak was fine-grained and uniformly directional:

- **evaluative lexicon** — a "mere" continued existence, a "naive reading"; both absent from the same writer's properly cited paraphrase of the argument earlier in the note;
- **reassuring own-voice glosses** — an uncited claim, inside a dependency-analysis section, that an objection "narrows but does not close the safety margin";
- **structural promotion** — a press rebuttal filed under the official review heading, giving the favoured side three sub-entries to the objectors' one;
- **provenance contamination** — the verdict-carrying artifact cited as though it were a source.

The blind judge separated the conditions cleanly, and every deviation it flagged leaned toward the implanted verdict. One treatment writer had explicitly detected the verdict section, named it out of contract, and refused to replicate it—yet still leaked its lean into the analysis. That is what "silent" means operationally here: the agent need not fail to notice the contaminant; noticing can fail to neutralize it.

Because every gross compliance check passed, a check for this failure must target the observed fine-grained signature directly: uncited evaluative language, own-voice glosses in synthesis sections, structural asymmetry between sides, and citations that promote non-source artifacts into sources.

## Why exclusion offers a guarantee instruction does not

This guarantee distinction is this note's architectural inference, not a generalization from the small experiment. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md), and [LLM contexts interpret instructions and content through one token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md): instructions, analyzed content, and contaminating verdicts all arrive as tokens, without an enforced marker that makes one class of influence unavailable to generation. A counter-instruction can condition the model in the other direction, but it cannot remove the contaminant or make the scope boundary binding. Expressed refusal can therefore coexist with residual steering. In an analogous content-influence result, [Gonen et al.](../sources/semantic-leakage-lms-gonen.ingest.md) report Leak-Rates significantly above the 50% baseline for all thirteen tested GPT and Llama variants. Paired instruction-tuned Llama variants generally leak more than their pretrained counterparts, although the Llama 2 13B difference is not significant. That result shows that semantic associations can influence completion prompts; it neither traces the mechanism of stance drift nor tests explicit refusal. The below-compliance observation here therefore remains on the epistack experiment, not on their benchmark.

Diffuse steering also leaves no variable-level lineage for a provenance-aware check to inspect, as [orchestration needs privilege quarantine, not permission scope](./orchestration-needs-privilege-quarantine-not-permission-scope.md) argues in the analogous privilege case. The reliable control for non-exposure is therefore architectural: select the next context deliberately, as in [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md), and keep the contaminant outside the role whose judgment must remain independent.

## Scope and limits

The direction of the observed deviations is established for this test; their magnitude and generality are not. The evidence comes from a single controlled test—n=2 per condition, one topic, and one model family for both writers and judge—and carries a declared confound. Implanting the verdict required deleting the context file's explicit "no position asserted in own voice" sentence. The *missing reminder* may therefore account for part of the effect attributed to the *present verdict*.

The least comparison-dependent observation is that one writer diagnosed and refused the verdict yet produced deviations that the blind judge classified as leaning toward it. This establishes that refusal and drift coexisted in this case. It does not establish the cause of every deviation or a universal failure of prompt controls.

At this dose—a blatant, explicit, own-voice verdict—"the agent will notice and compensate" is not a sufficient control. Whether subtler contamination produces the same signature, and whether an explicit neutrality reminder can inoculate against a *present* verdict rather than merely help in its absence, remain open questions.

## Open Questions

- Dose–response: does accumulated first-person material, rather than an explicit verdict section, produce the same signature at lower intensity, or is there a threshold?
- Does a cross-family judge reproduce the separation, or does some of it reflect same-family sympathy between writer and judge?
- Can the stance-drift signature be gated cheaply, or does detecting it cost as much as writing the note did?

---

Evidence is the "silently averaged" experiment run in the sibling `epistack-casebooks` repository (black-hole case, 2026-07-09): the design, blinding protocol, judge report, and unblinded analysis live in that repository's workshop layer.

Relevant Notes:

- [Agent orchestration needs coordination guarantees, not just capable agents](./agent-orchestration-needs-coordination-guarantees-not-just.md) — grounds: names contamination as the failure mode of composing flat context without a scoping or isolation primitive
- [soft degradation often binds before the hard cap when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — see-also: theorizes interference at gross-accuracy grain; this note describes the sub-threshold variant that detection does not neutralize
- [Semantic leakage in language models (Gonen et al.)](../sources/semantic-leakage-lms-gonen.ingest.md) — evidenced-by: systematic association leakage in completion prompts; analogous content influence without a mechanism trace or explicit-refusal test
- [Ingest: Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) — evidenced-by: analogous content sensitivity at the grain of logic-task accuracy; does not establish the stance-drift mechanism or test explicit refusal
