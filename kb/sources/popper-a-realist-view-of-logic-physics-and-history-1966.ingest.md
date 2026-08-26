---
description: "Popper's problem-theory-criticism cycle anchors KB error elimination but leaves acceptance and operational checks unspecified"
source: https://mercaba.org/SANLUIS/Filosofia/autores/Contempor%C3%A1nea/Popper/Objective%20knowledge.pdf
captured: "2026-08-26"
capture: pdftotext
genre: conceptual-essay
snapshot_sha256: 4822638bd1557571cc3ef7316df0eb5caa4134767904f2b32095b567c77a491b
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [epistemology, learning-theory, critical-rationalism]
---

# Ingest: A Realist View of Logic, Physics, and History

## Classification

This is a philosophical essay that develops a realist account of objective knowledge, theory growth, emergence, and logic rather than reporting a controlled study. Author: Karl Popper presents his own tetradic problem-solving schema and its philosophical basis, making the essay a primary authorial statement even though the captured PDF is hosted by a third party.

## Summary

Popper treats theories as objective, human-made artifacts whose implications and logical relations exceed any producer's mental state. He models knowledge growth as `P1 → TT → EE → P2`: a problem prompts one or more tentative theories, criticism attempts to eliminate their errors, and the result is usually a new, ideally deeper and more unexpected problem. He embeds that cycle in a pluralist realism that resists merely linguistic reductions, casts logic chiefly as an instrument of criticism in empirical inquiry, and treats correspondence with facts as a regulative ideal rather than a mechanically decidable criterion. For Commonplace, the essay is most useful as the primary conceptual anchor for conjecture-and-criticism workflows, not as an operational design for agent knowledge bases.

## Quotes

- **Source extract (verbatim):** I suggest that we may look upon these myths, these ideas and theories, as some of the most characteristic products of human activity. Like tools, they are organs evolving outside our skins. They are exosomatic artefacts. Thus we may count among these characteristic products especially what is called 'human knowledge'; where we take the word 'knowledge' in the objective or impersonal sense, in which it may be said to be contained in a book; or stored in a library; or taught in a university.
  - **Source location:** Opening section, before the heading "1. Realism and Pluralism: Reduction versus Emergence"; paragraph beginning "I suggest that we may look upon these myths", between printed page markers 1 and 2.
- **Source extract (verbatim):** I shall only mention an argument or two against the very popular and very naive view that theories can be reduced to the mental states of those who produce them, or of those who understand them.
  - **Source location:** Section "2. Pluralism and emergence in History"; paragraph beginning "But there are other arguments for the emergent character of theories", just after printed page marker 13.
- **Source extract (verbatim):** So we have actually these two different worlds, the world of thought-processes, and the world of the products of thought-processes. While the former may stand in causal relationships, the latter stand in logical relationships.
  - **Source location:** Section "2. Pluralism and emergence in History"; end of the paragraph containing the Buddha, Schopenhauer, and Nietzsche example.
- **Source extract (verbatim):** The fact that certain theories are incompatible is a logical fact, and holds quite independently of whether or not anybody has noticed or understood this incompatibility. These purely objective logical relationships are characteristic of the entities which I have called theories, or knowledge, in the objective sense.
  - **Source location:** Section "2. Pluralism and emergence in History"; paragraph beginning "The fact that certain theories are incompatible", immediately before printed page marker 14.
- **Source extract (verbatim):** This may also be seen from the fact that the person who produces a theory may very often not understand it.
  - **Source location:** Section "2. Pluralism and emergence in History"; first sentence of the paragraph immediately after printed page marker 14 (the Schrodinger and Kepler examples follow).
- **Source extract (verbatim):** there are infinitely many situations of infinite variety to which the theory might be applicable; that is to say, upon which some of its logical consequences may bear; and many of these situations have never been thought of; their possibility may not yet have been discovered. But this means that nobody, neither its creator nor anybody who has tried to grasp it, can have a full understanding of all the possibilities inherent in a theory; which shows again that the theory, in its logical sense, is something objective and something objectively existing - an object that we can study, something that we try to grasp.
  - **Source location:** Section "2. Pluralism and emergence in History"; paragraph beginning "Theories are similar", between printed page markers 14 and 15.
- **Source extract (verbatim):** I shall, therefore, before going any further into my topic, present a general tetradic schema which I have found more and more useful as a description of the growth of theories. It is as follows: P1 » TT » EE » P2. Here 'P' stands for 'problem'; 'TT' stands for 'tentative theory'; and 'EE' stands for '(attempted) error-elimination', especially by way of critical discussion. My tetradic schema is an attempt to show that the result of criticism, or of error-elimination, applied to a tentative theory, is as a rule the emergence of a new problem; or, indeed, of several new problems.
  - **Source location:** Opening section, before the heading "1. Realism and Pluralism: Reduction versus Emergence"; the paragraphs introducing the tetradic schema, between printed page markers 2 and 3.
- **Source extract (verbatim):** 'To consume' means here, first of all, 'to digest', as in the case of the bees. But it means more: our consumption of theories, whether those produced by other people or by ourselves, also means criticising them, changing them, and often even demolishing them, in order to replace them by better ones. All these are operations which are necessary for the growth of our knowledge; and I again mean here, of course, knowledge in the objective sense.
  - **Source location:** Opening section, before the heading "1. Realism and Pluralism: Reduction versus Emergence"; paragraph beginning "'To consume' means here" and the paragraph immediately following it, between printed page markers 2 and 3.

## Connections Found

The source's strongest role is as primary evidence for [Mechanistic constraints make Popperian KB recommendations actionable](../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md): it supplies the problem, competing tentative theories, error elimination, and successor-problem cycle that the note translates into bounded-context KB practices. It also provides a useful counterpoint to the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md). Commonplace separates testing, acceptance, and integration and ends one lifecycle instance at integration, whereas Popper makes the newly generated `P2` an immediate output of criticism. Finally, Popper's objective, externally stored theories compare with [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md): his own account says that consuming stored theories requires criticism, change, or replacement, while the Commonplace note supplies the missing ingress and retrieval mechanics.

## Extractable Value

1. **Problem-generating criticism as a growth model** -- The `P1 → TT → EE → P2` cycle grounds the KB's existing Popperian practices and distinguishes productive criticism, which exposes a changed problem situation, from correction that merely restores the starting point. [quick-win]
2. **A possible post-integration transition for the discovery lifecycle** -- Popper's `P2` suggests that a successfully criticized or accepted theory can itself generate the next observation or anomaly; deciding whether to represent that transition requires preserving the current lifecycle's acceptance and integration boundaries. [deep-dive]
3. **Problem distance as a progress signal** -- Popper proposes judging progress partly by the depth and unexpectedness of the successor problem, offering a review heuristic that values newly exposed questions as well as accepted answers; the source supplies no operational measure, so the heuristic needs a bounded trial. [experiment]
4. **Objective artifacts still require active consumption** -- The essay separates theories from their makers and argues that their consequences can remain undiscovered, but it also makes criticism, revision, and replacement part of consuming them. This strengthens the distinction between preserving text and creating usable agent memory. [quick-win]
5. **Different economies for proof and criticism** -- Popper favors the weakest sufficient means for proof but the strongest available means for criticism. That asymmetry is a useful reference point for review design, though his defense of classical logic does not by itself justify a Commonplace rule. [just-a-reference]

## Limitations (our opinion)

The essay argues at a high philosophical level and does not test the tetradic schema against alternative inquiry models or define how to identify, compare, or measure problems. Its `P2` transition therefore cannot replace the explicit evidence, acceptance, and integration boundaries in the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md). Its account of objective stored knowledge also does not address bounded context, retrieval, provenance, authority, or oracle quality; those mechanisms must come from the [Popperian KB practices note](../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) and [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), not from analogy alone. The discussions of reduction, quantum physics, and logic are historically situated arguments from 1966, so they should not be treated as current scientific consensus or imported wholesale into KB methodology.

## Recommended Next Action

Update [Mechanistic constraints make Popperian KB recommendations actionable](../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) to cite this ingest with the `(snapshot required)` marker as primary support for the `P1 → TT → EE → P2` cycle it operationalizes.
