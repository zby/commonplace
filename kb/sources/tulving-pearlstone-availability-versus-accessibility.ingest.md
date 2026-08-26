---
description: "A controlled word-recall experiment shows category cues recovering otherwise unrecalled items, supporting a bounded distinction between storage and retrieval access."
source: "https://www.rotman-baycrest.on.ca/files/publicationmodule/%40random45f5724eba2f8/_16AvailabilityAccessibilityInformationMemoryWords76_19448340de45d29b.pdf"
captured: "2026-08-26"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: aa4c42278a4e1ad4bb0fd0ba718d40b25d999867318f2d385e4a8235c30d8b77
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [human-memory, retrieval, evaluation]
---

# Ingest: Availability versus accessibility of information in memory

## Classification

This is a scientific paper reporting a controlled factorial experiment, with explicit manipulations of list length, items per category, and category-cue presence, followed by statistical analysis of recall outcomes. Author signal: Endel Tulving and Zena Pearlstone report their own experiment, originally published in the *Journal of Verbal Learning and Verbal Behavior* in 1966.

## Summary

Tulving and Pearlstone tested 929 Toronto-area high-school students on one-trial learning of categorized word lists, then varied whether category names appeared during the first recall test. Category-cued recall exceeded uncued recall for nearly every list, with the gap increasing for longer lists and decreasing as more words shared each category. Decomposing total word recall into categories reached and words recovered within a reached category localized the cue effect mainly to category access. The paper is worth reading as a classic, experimentally bounded demonstration that failure to reproduce an item does not establish its absence from memory; it does not establish that retrieved or context-present knowledge will affect later action.

## Quotes

- **Source extract (verbatim):** Cued recall was higher than noncued recall
  - **Source location:** Opening abstract, reprinted article page 194; result of the category-cue comparison.
- **Source extract (verbatim):** available in the memory storage, but not accessible for retrieval
  - **Source location:** Opening abstract, reprinted article page 194; authors' interpretation of the category-cue result.
- **Source extract (verbatim):** Immediate recall was tested either in presence or absedce of category names as retrieval cues. Cued recall was higher than noncued recall, the difference varying directly with list length and inversely with number of items per category. This finding was interpreted as indicating that suficiently intact memory traces of many words not recalled under the noncued recall conditions were available in the memory storage, but not accessible for retrieval.
  - **Source location:** Opening abstract, reprinted article page 194; manipulation, result, and authors' bounded interpretation.

## Connections Found

The paper is a bounded empirical anchor for [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md): holding study conditions constant and adding category names only at recall made some previously unrecalled words reproducible. Its role stops at the human storage-to-retrieval boundary; it supplies no evidence for Commonplace's stronger read-back or context-to-action distinctions.

It is also a concrete methodological case for [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md). The observed comparison supports a cue-dependent accessibility claim within immediate recall of category-organized word lists. The category partition, adjacent presentation of category members, written word-reproduction response, and participants' unrestricted internal encoding processes remained fixed, so the improvement does not validate that decomposition as a general memory architecture.

## Extractable Value

1. **Primary evidence for availability without unaided accessibility** -- The category-cue contrast provides a controlled human baseline for the narrower storage-to-retrieval step in the KB's activation account, while making the boundary to action-level activation explicit. [quick-win]
2. **A test-time intervention for separating retrieval from prior storage conditions** -- Introducing the critical cue only when recall begins is a reusable design pattern for asking whether an observed miss reflects retrieval conditions rather than a difference in exposure or encoding. [deep-dive]
3. **A two-level diagnostic for aggregate retrieval performance** -- Separating categories reached from items recovered within reached categories shows how one recall total can hide a routing-like failure and an item-recovery failure; an agent-memory analogue would require its own validated partition and experiment. [experiment]
4. **A fixed-decomposition boundary on the headline result** -- Because the study supplied semantic categories and adjacent category members, it establishes cue effectiveness inside that organization, not the superiority or generality of category-based memory organization. [just-a-reference]

## Limitations (our opinion)

The result is limited to immediate written recall after a single presentation of categorized nouns, using mostly 15- to 18-year-old students. Participants could condition recall on the presented category labels, target words, and their presentation history, and could respond only by reproducing words; their internal encoding and retrieval mappings were neither specified nor experimentally bounded. The semantic partition, within-category adjacency, recall timing, and response interface were fixed outside the varied cue condition. As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) cautions, success within that setup cannot establish that the fixed organization is necessary or preferable to alternatives.

The cued-versus-uncued contrast shows that category cues enabled additional correct reproductions, not that every unrecalled trace remained intact, persisted beyond the immediate test, or could influence behavior without explicit prompting. The authors estimate that category-based guessing is too small to explain the main difference, but successful reproduction still does not directly expose a stored trace. Their inference of two independent retrieval processes comes from a factorization of recall and differential patterns across measures, not from independently manipulating the proposed processes, so that mechanistic conclusion is less secure than the cue effect itself.

## Recommended Next Action

Update [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) with one bounded historical-evidence paragraph citing this ingest for category-cue recovery while marking context-to-action activation as outside the experiment.
