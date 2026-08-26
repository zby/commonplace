---
description: "A CHI diary study gives bounded human evidence that contextual local steps complement direct keyword jumps, without testing LLM agents or KB metadata designs."
source: https://people.csail.mit.edu/teevan/work/publications/papers/chi04.pdf
captured: "2026-08-26"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: a8b4b8839b5c0401ced39586bc4d03f99ed747253e0418972eedc635c5450b26
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [information-seeking, navigation, context-engineering]
---

# Ingest: The Perfect Search Engine Is Not Enough

## Classification

This CHI 2004 scientific paper reports an exploratory qualitative observational study based on repeated interviews, with supplementary direct observation and longer interviews.
Author: Jaime Teevan, Christine Alvarado, and David R. Karger were affiliated with MIT CSAIL, and Mark S. Ackerman was affiliated with the University of Michigan; the conference publication and explicit account of sampling, coding, and study limits provide the main credibility signals.

## Summary

The authors studied how 15 MIT computer-science graduate students found known and general information in email, files, and the Web. Participants often reached a target through contextual local steps, which the paper calls orienteering, rather than trying to jump directly to it with keywords, which it calls teleporting. Keyword search could serve either strategy. The paper argues that local steps can reduce the need to specify a target up front, preserve a sense of location, and supply context for interpreting positive and negative results. For Commonplace, the study is useful as bounded human evidence for distinguishing local link-following from long-range search, but it does not test LLM-agent navigation or establish the KB metadata designs that should follow.

## Quotes

- **Source extract (verbatim):** This paper presents a modified diary study that investigated
  how people performed personally motivated searches in
  their email, in their files, and on the Web. Although earlier
  studies of directed search focused on keyword search, most
  of the search behavior we observed did not involve
  keyword search. Instead of jumping directly to their
  information target using keywords, our participants
  navigated to their target with small, local steps using their
  contextual knowledge as a guide, even when they knew
  exactly what they were looking for in advance. This
  stepping behavior was especially common for participants
  with unstructured information organization. The observed
  advantages of searching by taking small steps include that it
  allowed users to specify less of their information need and
  provided a context in which to understand their results. We
  discuss the implications of such advantages for the design
  of personal information management tools.
  - **Source location:** Abstract, paper p. 415 (PDF p. 1)

## Connections Found

The paper is a bounded empirical anchor for the human side of [link-following and search impose different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md). Its contextual local-step versus direct-jump distinction bears on that note's navigation-mode contrast, but not on its LLM-specific metadata prescriptions. It also compares with [agents navigate by deciding what to read next](../notes/agents-navigate-by-deciding-what-to-read-next.md): the observed participants repeatedly chose context-bearing next steps toward known targets, providing a human analogue without establishing the agent mechanism or its token and interaction costs.

## Extractable Value

1. **Human evidence for distinct navigation modes.** The observed contrast between contextual local steps and direct jumps gives the KB's link-following versus search distinction an empirical human anchor while keeping the agent transfer explicit. [quick-win]
2. **Strategy is not tactic.** Keyword search appeared inside both orienteering and teleporting, so an evaluation should classify the path and decision pattern rather than infer a navigation strategy from the tool invoked. [deep-dive]
3. **Sources and paths can be stronger cues than target properties.** Participants often remembered a source, sender, date, folder, or familiar route when they could not state enough target attributes for a direct query. This motivates an agent-side test of source-aware metadata and contextual browsing surfaces. [experiment]
4. **Traversal may help make confidence inspectable.** Participants used an understandable or exhaustible path to interpret results and sometimes accept absence. Testing whether visible traversal paths improve agent verification would extend the design hypothesis without treating the human observation as agent evidence. [experiment]

## Limitations (our opinion)

The study is exploratory and context-bound. It covers 151 short interviews with 15 MIT computer-science graduate students over five weekdays, uses participant-defined effort to distinguish looking for from looking at, and draws qualitative conclusions from non-randomly selected incidents. Its reported proportions therefore should not be treated as population estimates, and its 2004 email, file, and Web environment may not represent current retrieval behavior.

No perfect search engine or alternative interface was tested, and participants were not assigned to search strategies. The proposed benefits of cognitive ease, location, understanding, and trust are interpretations of observed incidents rather than causal effects or benchmark results.

Under the lens that [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), this is not a learning-system experiment with a stated hypothesis class. Participants could condition open-ended human actions on prior associations and local cues, composing URL entry, link following, file and email navigation, and keyword or site search. The researchers' observation and inference space was fixed instead: recent-activity reports and supplemental observations supplied the signals, while the orienteering/teleporting split and tactic coding supplied the representation. Because those choices were not varied, the findings do not show that the taxonomy is exhaustive or that the proposed designs are preferable. They also do not test LLM agents, context costs, or KB metadata requirements.

## Recommended Next Action

Update [link-following and search impose different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md) with a bounded-evidence paragraph that cites this ingest for the human local-step/direct-jump contrast and identifies the LLM-agent metadata prescription as a local inference.
