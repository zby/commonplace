---
type: ingest-report
description: "HEP records evidence-linked hypothesis revision in materials simulations; its audit trail supports inspection, while self-assessed beliefs and bundled comparisons limit epistemic claims."
source: https://arxiv.org/abs/2607.09195
captured: "2026-09-19"
ingested: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d208cc0502cb0e3a21fc59fd024035e755f486ee6bffe5f3a986fe04cf464515
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
domains: [scientific-discovery, theory-refinement, agent-harnesses, evidence-provenance]
learning_claims: true
---

# Ingest: Toward Auditable AI Scientists: A Hypothesis Evolution Protocol

## Classification

Scientific paper: a July 2026 arXiv preprint by Izumi Takahara and Teruyasu Mizoguchi of the University of Tokyo. It presents an agent protocol, materials-simulation case studies, a planning-agent comparison, and a comparison across base models. The authors report their own system's results. The captured paper promises source code upon publication; this analysis neither inspects an implementation nor reproduces the experiments.

## Summary

The Hypothesis Evolution Protocol (HEP) turns hypotheses into persistent, addressable records containing testable predictions, evidence, elicited beliefs, lifecycle states, and parentage. Tools enforce evidence attachment before belief changes and numeric thresholds before support or refutation verdicts, while an append-only history preserves the sequence. A GPT-5.5 agent reportedly used proposal, testing, revision, and merging across three questions about the behavior of a fixed machine-learned interatomic potential (MLIP). Its comparison with a planning agent finds explicit belief updates under HEP but none under planning alone; this tests the combined protocol and hypothesis-discipline prompt with different stopping criteria, not the registry's isolated effect. Stronger base models exercised more of the same protocol. The contribution is an inspectable record of scientific reasoning, including reported refutations that redirected later search. Evidence adequacy and belief values remain the same agent's judgments, and the resulting rules concern the simulator rather than established physical truth.

## Quotes

No source quotes have been retained yet.

## Connections Found

HEP is a concrete comparison for the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md): hypotheses become explicit objects that can be tested, revised, supported, refuted, or shelved. Its terminal status rules are implementation choices, rather than a demonstration that a discovery has earned integration. For the occasion, this makes HEP useful as an executable conjecture-and-revision design without treating elicited probability thresholds as consequences of Popper's epistemology.

The paper supplies a bounded illustration of [failure explanations changing later branch decisions](../notes/failure-explanation-changes-later-branch-decisions.md). In its double-perovskite task, two mechanisms were successively refuted before search moved toward an A-site exception retained in the final rule. This is a reported same-run continuation trace. Neither that example nor the bundled planning comparison isolates the causal contribution of retained explanations.

The append-only record also compares with [retaining superseded choices while withdrawing refuted beliefs' standing](../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md). HEP keeps historical events while separately recording current disposition. Audit retention does not by itself recommend continued use of a refuted claim.

## Learning Claims (our opinion)

HEP's adapting objects are natural-language hypotheses about material families. The agent can create a new proposal, draw inspiration from another, refine a parent, or merge several parents. It observes simulation results and retained histories, assigns evidence direction and adequacy, and records a new belief with its rationale. Refine and merge require parents to have reached a verdict or have attached evidence. New statements and search decisions can therefore change within a run; neither model weights nor the protocol's evidence rules and verdict thresholds are reported as learned.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), conditions 1 to 3 are met within an investigation. Hypotheses are natural-language records with stated predictions, separately [addressable](../notes/definitions/addressable-theory.md) (condition 1). They direct which simulations run next (condition 2). Simulation results test their stated predictions, and the reported replacement and merging of mechanisms is criticism of explanatory content, which a belief change alone would not be (condition 3). Evidence adequacy and belief values remain the proposer's own judgments, and lineage alone does not show that every child repairs an identified error.

Condition 4 (iteration) is met at the strength of the reported traces. In the double-perovskite task, two refuted mechanisms raised the question of the A-site exception, which new simulations then pursued; refine and merge take up parents that carry verdicts or evidence; and the resulting rule is tested on compositions not examined when it was formed. Each revised hypothesis is a new conjecture shaped by the criticism of its parents, which is what the condition asks. Persistence reaches the grade of rounds within one investigation: the paper shows no reuse across its three questions or in later sessions. Learning is a separate claim: the report does not isolate whether conjecture and formulated criticism improved future capacity, nor test whether revisions preserve useful prior predictions. The external target makes this domain-theory revision, not evidence that the system is reflective.

The source supports separating criticism, revision, and retention from the machinery used to administer them. The 0.8 support and 0.2 refutation thresholds apply to probabilities supplied by the agent, not calculated posteriors or calibrated error rates. A supported record therefore remains a tentative theory in Commonplace's sense. For a Popper-grounded paradigm, the protocol offers useful operations; its confidence-based acceptance policy requires separate justification.

As [learning within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, these results concern an update space fixed by the registry, available atomistic tools, and simulator. Natural-language hypotheses and authored analysis scripts permit considerable flexibility within that space. The reported model comparison shows differing ability to exploit it, not that its hypothesis representation, self-certification gate, or confidence thresholds are preferable to alternatives. Nor does it establish that those choices are mistaken.

## Extractable Value

1. **Separate traceability from epistemic warrant.** A record can enforce evidence linkage and lifecycle consistency while leaving evidence quality, relevance, and belief assessment to the proposer. This distinction matters directly to a Popper-grounded design: inspectable criticism is a prerequisite for auditing its severity, not proof of severe criticism. [quick-win]
2. **Retain the refutation-to-search example at its demonstrated scope.** The double-perovskite sequence illustrates discarded mechanisms changing the next explanatory candidate within one investigation. It is useful evidence for the existing branch-decision note, with the qualification that no matched intervention isolates the explanation's effect. [quick-win]
3. **Test the registry separately from prompting.** The planning comparison changes protocol access, hypothesis discipline, and stopping behavior together. A matched comparison with the same belief-oriented prompt and budget, varying structured records, would test what persistence and enforced transitions add beyond elicitation. [experiment]
4. **Use lineage and disposition as separate fields.** HEP's distinction between historical parentage, current belief, and lifecycle state offers a concrete design reference for retaining rejected or subsumed candidates without confusing their audit value with present acceptance. Evidence does not establish this schema's superiority over other representations. [just-a-reference]

## Limitations (our opinion)

The main comparison has three runs per condition and evaluates process traces rather than independently assessed explanatory accuracy or discovery quality. Planning spends 83% of classified steps on tests and none on belief updates, but HEP explicitly asks for and instruments belief updates. Tool events map deterministically to HEP loop categories, whereas free text is classified by GPT-5.5. More recorded cycle steps may partly reflect elicitation and measurement design. Normalizing step counts does not remove differences in stopping policy or isolate the registry from its prompt.

All three questions concern the behavior of one fixed MLIP. Successful predictions for additional compositions remain evidence about that potential. The paper itself leaves correspondence with established materials physics unresolved. More elaborate explanations, deeper hypothesis trees, and higher confidence do not independently measure truth or explanatory improvement.

The validation gate accepts the agent's certification of computational adequacy and result validity. Hash-chained event history can preserve what was asserted without checking those assertions. No hypothesis assigned a prior above 0.7 was later overturned; the paper explicitly leaves open whether this reflects good priors or insufficiently severe tests. Final beliefs separating by final status are also partly enforced by the threshold rules, so that separation is not independent evidence of calibration.

The base-model comparison varies the model within fixed prompts, tools, and stopping conditions, with three runs per model. Its hypothesis counts, lineage depth, and completion rates establish differences in observed protocol use, not a general scaling law for scientific understanding. Implementation and experiment artifacts were not examined here, and no code was executed.

## Recommended Next Action

Review [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) for adding HEP's double-perovskite refutation sequence as a bounded same-run example, retaining source support before promotion and explicitly separating the reported trace from causal evidence for the registry.
