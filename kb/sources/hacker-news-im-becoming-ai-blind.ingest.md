---
description: "Hacker News readers describe AI prose as low-yield, misleadingly polished, and costly to verify, while counterexamples limit style-based detection"
source: https://news.ycombinator.com/item?id=49386699
captured: "2026-08-22"
capture: web-fetch
genre: conversation-thread
snapshot_sha256: 1f7433c426612c81ae131f4bdb31293d3bcc8caa878538b33a1fe8aa988bfb5c
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [ai-writing, substantive-writing, review-burden]
---

# Ingest: I'm becoming AI-blind — Hacker News discussion

## Classification

This is a conversation thread: its evidence comes from many participants' reports, disagreements, and examples rather than a sustained single-author argument. Author: the submitter `rcymerys` introduced a linked first-person essay, while the captured body consists of 435 comments from pseudonymous Hacker News participants, many describing technical writing and software-workplace experience without independently verifiable credentials.

## Summary

The thread is useful as a broad failure-mode and boundary-case inventory for AI-assisted knowledge writing. Participants repeatedly describe small informational payloads expanded into polished prose, missing mechanisms hidden by fluent presentation, generic comparison structures, invented terminology, loss of author voice, poor recall, reader fatigue, automatic rejection, and review work shifted from sender to recipient. Other participants report effective technical use, better results from explicit style constraints or iterative dialogue, false positives in AI detection, and survivorship bias toward conspicuously bad outputs. Read it to generate and discriminate hypotheses about document quality and review burden, not to estimate how common the effects are or establish what causes them.

## Quotes

No source quotes have been retained yet.

## Connections Found

The thread serves as a qualitative field corpus for [reverse compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), especially the claim that a longer artifact can leave the reader to recover a much smaller payload. Reports of polished pseudo-language and plans whose missing high-level logic must be reconstructed also bear on [hidden constraint relaxation](../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md). Workplace triage accounts support [cheap generation breaking text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), while the false-positive and high-quality-output counterexamples reinforce that this signal is not an AI detector. Relative to the [original essay ingest](./im-becoming-ai-blind.ingest.md), the discussion's main role is to broaden the candidate failure inventory and supply boundaries; its recurring distinction between polished topical coverage and an actual contribution also exemplifies why [warranted reader update](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) is a better objective than stylistic fluency.

## Extractable Value

1. **A four-layer failure map** — The reports separate content and epistemic failures, discourse failures, reader effects, and social or operational costs; those layers imply different checks and should not be collapsed into a list of stylistic tells. [deep-dive]
2. **Reader-side recompression as a recurring mechanism** — Several participants independently describe extracting a small payload from long prose, re-deriving the missing point, or finding less structure under closer inspection. This is direct qualitative support for the reader-cost side of reverse compression. [quick-win]
3. **Style detection and substantive review are different tasks** — Participants report both false positives and plausible high-quality AI text that escapes notice. Removing familiar model tics can therefore improve reception without restoring a missing contribution, mechanism, or constraint. [quick-win]
4. **Cheap documents can create retained review debt** — Examples include methodology documents, proposals, code comments, PR descriptions, and AI-heavy internal documentation that recipients avoid, manually compress, or feed into another model. These cases connect generation cost asymmetry to maintenance and coordination burden. [just-a-reference]
5. **Repeated low-yield exposure may condition channel rejection** — Reports of eyes glazing over, automatic skimming, poor recall, and `AI;DR` responses suggest an exposure-dependent rejection hypothesis, but static overload, prior attitudes, cue learning, and survivorship bias remain competing explanations. [experiment]
6. **Mitigations are plausible but unevaluated** — Plain-language instructions, source-first answers, model switching, iterative questioning, and human editing are all reported as useful, yet the thread supplies no controlled comparison showing which intervention improves contribution, truth, or extraction cost. [experiment]

## Limitations (our opinion)

The thread is self-selected, ranked by a platform, and dominated by pseudonymous anecdotes; replies influence one another, so 435 comments are not 435 independent observations. Model versions, system prompts, user prompts, editing, document purposes, and reader expertise are usually unknown. Strong claims about cognition, intent, intelligence, and model internals are argued rather than demonstrated. Detection reports are especially vulnerable to false positives and survivorship bias: conspicuous failures are visible while successful or heavily edited generation may not be recognized. As [the effort-signal note](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) cautions, apparent generation style can rationally affect triage without establishing authorship or incorrectness. The source can enumerate failure modes, counterexamples, and testable hypotheses; it cannot establish their prevalence, causal mechanism, or applicability to all models, writers, readers, and document types.

## Recommended Next Action

Write a note provisionally titled **AI-writing review must test contribution, constraint satisfaction, and reader extraction cost separately from style**, using the thread's four-layer failure map and counterexamples to define the distinct checks.
