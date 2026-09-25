---
description: "Interface probes suggest Instinct combines Git-backed records, delayed profile derivation and explicit retrieval; useful cases for freshness and activation, with internals unverified."
source: https://x.com/DhravyaShah/status/2101745550752428340
captured: "2026-09-21T17:58:01.983746+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: bd5cf1b317f8ea62f66db43b7bbeca2849125ddf787cae46b10fcb031c0256a5
ingested: "2026-09-21"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, context-engineering, memory-evaluation]
learning_claims: true
status_id: 2101745550752428340
conversation_id: 2101745550752428340
post_count: 17
---

# Ingest: Reverse-engineering Instinct's memory through its interface

## Classification

A practitioner account of probing an assistant through iMessage, followed by a promotional proposal to reproduce its memory behavior with Supermemory. Author Dhravya Shah identifies himself as Supermemory's founder with three years of agent-memory work. That experience informs the hypotheses but also gives him a commercial interest in the comparison. He explicitly reports having no access to Instinct's code.

## Summary

Shah reconstructs Instinct as an assistant that reads Git-tracked Markdown records, receives a user profile and conversation recap, and delegates durable memory updates to a background process. Reported records carry types, IDs, aliases and links; reconciliation can consolidate material, generalize examples and replace incorrect facts while history remains accessible. The most useful observations are a profile reportedly lagging by two days and stronger explicit recall than implicit personalization. The architecture, daily update schedule and absence of vector or BM25 search remain inferences from interface probes and agent reports. His informal evaluation finds within-conversation correction but leaves durable learning and long-term scale unverified. The proposed Supermemory substitute is a vendor claim, not an evaluated comparison.

## Quotes

No source quotes have been retained yet.

## Connections Found

The reported profile lag supplies a concrete, bounded failure case for [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md): maintained records and the derivative injected into an answering model can have different freshness. The source does not establish the derivative's authoritative backing or regeneration mechanism.

The contrast between explicit recall and implicit personalization is practitioner evidence relevant to [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). It illustrates why recall and spontaneous use need separate assessment, without distinguishing failed retrieval from failed uptake of already visible information. Reported corrections, dated notes and Git history also provide a comparison with [Retire, Redact, Supersede, And Relax Memory](../notes/agent-memory-requirements/retire-redact-supersede-relax.md): changing a current record, expiring a fact and removing historical access are separate operations.

## Learning Claims (our opinion)

The proposed adaptation mechanism combines conversation-derived records, background reconciliation and an injected profile. Shah reports that reconciliation turns examples into broader traits and replaces incorrect facts with dated corrections. He separately reports corrected behavior within a conversation, while explicitly leaving durable learning unverified. These are different evidence levels: an inferred update mechanism and an observed local response to correction do not jointly establish improved behavior in later sessions.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, membership is unestablished, and the system's opacity is the reason. The reported Markdown records are stated content (condition 1), on interface evidence only. Explicit recall shows that some record content reaches answers (condition 2). Criticism (condition 3) is unestablished and decides the verdict: reconciliation reportedly replaces incorrect facts, but the account does not show whether anything beyond the user's own correction bears on what a record says. A user's correction is a verdict on a product; counting it as the builder's criticism requires declaring a [boundary](../notes/definitions/theory-builder.md#boundary) that includes the user. Retention (condition 4) is also unestablished: a commit is observed, but no corrected record is traced into a later session. IDs and individually editable records give criticism finer units to name, a grade of [addressability](../notes/definitions/addressable-theory.md) above condition 1; they do not show criticism using them. Learning in later sessions is unverified by the author's own account. The absence of observed procedural records leaves procedural retention unestablished rather than proving its absence.

The reconstruction exposes revision of memory contents, but does not show whether the system can revise its profile generator, search policy, update schedule or division between reader and writer. As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains, adaptation within a supplied arrangement does not validate that arrangement against alternatives. Here even the effective revision boundary is uncertain. The source adds a useful attribution problem, not grounds to revise the theory-builder definition.

## Extractable Value

1. **Profile freshness can differ from record freshness.** The reported two-day lag supplies a specific practitioner case for the existing compiled-view requirement. Its value is the separate observation of a derived surface, not confirmation of a particular cache implementation. [quick-win]
2. **Test spontaneous use separately from explicit recall.** The informal personalization contrast suggests paired tasks that hold the relevant user facts and intended outcome constant while varying whether the prompt names their relevance. The article supplies a motivation for this test, not a measured effect or a diagnosis of its cause. [experiment]
3. **Keep correction, expiry and historical access separate.** The reconstructed combination of revised current records, dated notes and Git history illustrates the existing lifecycle distinctions. It is a context-bound example, not evidence that Git either guarantees or prevents complete forgetting. [just-a-reference]

## Limitations (our opinion)

This is one author's short experience with one account, without a released probe protocol, full response traces, controlled comparisons or inspected implementation. Agent statements about its tools and files can be incomplete or mistaken. An inaccessible backing file does not establish an ad hoc cache; failure to expose an index does not establish that vector or BM25 search is absent. One preference taking about 23 hours to appear in a reported commit does not identify a daily cron schedule. Queuing, selective processing or delayed visibility could produce similar observations.

The informal evaluation does not isolate the contribution of Markdown, Git, aliases, background curation or injected profiles. No alternative decomposition is tested. Even the implicit-personalization example embeds a contestable preference inference: being a founder with a new office does not necessarily imply wanting premium equipment. The claim of exponentially increasing write cost has no cost model or measurements. Month-scale behavior, million-token histories, automatic expiry and deletion propagation remain untested or unresolved.

The captured text refers to file-tree illustrations, example files and a roughly sixty-line implementation that are not reproduced in its body. Those details cannot be verified from this observation. Linked Supermemory documentation was not inspected, and the asserted equivalence, freshness, forgetting guarantees and cost advantage of the proposed substitute have no comparative evaluation here.

## Recommended Next Action

Update [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md) with the narrowly attributed two-day profile-lag observation, preserving the uncertainty about its cause and using a source-support declaration appropriate to the evidence needed.
